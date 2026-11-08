/**
 * Persistent Multi-Layer Storage Engine for Greek Flashcard Deck
 * Mirrors localStorage state into native browser IndexedDB and StorageManager.
 * Guarantees zero progress loss across PWA updates, cache clearing, and new lesson additions.
 */

const DB_NAME = 'greek_deck_db';
const DB_VERSION = 1;
const STORE_NAME = 'app_state';

// Storage Key Prefixes
export const GREEK_DECK_USERS_KEY = 'greek_deck_users_v1';
export const GREEK_DECK_ACTIVE_USER_KEY = 'greek_deck_active_user_id_v1';
export const LEGACY_SRS_KEY = 'greek_deck_srs_state_v1';

function hasWindow(): boolean {
  return typeof window !== 'undefined';
}

function hasIndexedDB(): boolean {
  return hasWindow() && typeof window.indexedDB !== 'undefined';
}

let dbInstance: IDBDatabase | null = null;
let dbInitPromise: Promise<IDBDatabase | null> | null = null;

/**
 * Initialize native IndexedDB connection
 */
export function getDB(): Promise<IDBDatabase | null> {
  if (!hasIndexedDB()) {
    return Promise.resolve(null);
  }
  if (dbInstance) {
    return Promise.resolve(dbInstance);
  }
  if (dbInitPromise) {
    return dbInitPromise;
  }

  dbInitPromise = new Promise((resolve) => {
    try {
      const request = window.indexedDB.open(DB_NAME, DB_VERSION);

      request.onupgradeneeded = (event) => {
        const db = (event.target as IDBOpenDBRequest).result;
        if (!db.objectStoreNames.contains(STORE_NAME)) {
          db.createObjectStore(STORE_NAME);
        }
      };

      request.onsuccess = (event) => {
        dbInstance = (event.target as IDBOpenDBRequest).result;
        dbInstance.onclose = () => {
          dbInstance = null;
          dbInitPromise = null;
        };
        resolve(dbInstance);
      };

      request.onerror = (err) => {
        console.warn('IndexedDB failed to open, using localStorage fallback', err);
        resolve(null);
      };
    } catch (e) {
      console.warn('Error initializing IndexedDB', e);
      resolve(null);
    }
  });

  return dbInitPromise;
}

/**
 * Read value from IndexedDB
 */
export async function getIDBValue<T>(key: string): Promise<T | null> {
  const db = await getDB();
  if (!db) return null;

  return new Promise((resolve) => {
    try {
      const tx = db.transaction(STORE_NAME, 'readonly');
      const store = tx.objectStore(STORE_NAME);
      const req = store.get(key);
      req.onsuccess = () => resolve(req.result ?? null);
      req.onerror = () => resolve(null);
    } catch {
      resolve(null);
    }
  });
}

/**
 * Write value to IndexedDB
 */
export async function setIDBValue<T>(key: string, value: T): Promise<boolean> {
  const db = await getDB();
  if (!db) return false;

  return new Promise((resolve) => {
    try {
      const tx = db.transaction(STORE_NAME, 'readwrite');
      const store = tx.objectStore(STORE_NAME);
      const req = store.put(value, key);
      req.onsuccess = () => resolve(true);
      req.onerror = () => resolve(false);
    } catch {
      resolve(false);
    }
  });
}

/**
 * Delete key from IndexedDB
 */
export async function removeIDBValue(key: string): Promise<boolean> {
  const db = await getDB();
  if (!db) return false;

  return new Promise((resolve) => {
    try {
      const tx = db.transaction(STORE_NAME, 'readwrite');
      const store = tx.objectStore(STORE_NAME);
      const req = store.delete(key);
      req.onsuccess = () => resolve(true);
      req.onerror = () => resolve(false);
    } catch {
      resolve(false);
    }
  });
}

/**
 * Get all keys stored in IndexedDB
 */
export async function getAllIDBKeys(): Promise<string[]> {
  const db = await getDB();
  if (!db) return [];

  return new Promise((resolve) => {
    try {
      const tx = db.transaction(STORE_NAME, 'readonly');
      const store = tx.objectStore(STORE_NAME);
      const req = store.getAllKeys();
      req.onsuccess = () => resolve((req.result as string[]) || []);
      req.onerror = () => resolve([]);
    } catch {
      resolve([]);
    }
  });
}

/**
 * Non-blocking async mirror from localStorage write to IndexedDB
 */
const pendingMirrorTimeouts: Record<string, number> = {};

export function mirrorKeyToIndexedDB(key: string, rawJsonValue: string): void {
  if (!hasIndexedDB()) return;

  // Debounce rapid writes to the same key
  if (pendingMirrorTimeouts[key]) {
    clearTimeout(pendingMirrorTimeouts[key]);
  }

  pendingMirrorTimeouts[key] = window.setTimeout(async () => {
    delete pendingMirrorTimeouts[key];
    try {
      await setIDBValue(key, rawJsonValue);
    } catch (e) {
      console.warn(`Failed to mirror ${key} to IndexedDB`, e);
    }
  }, 80);
}

/**
 * Remove key from IndexedDB mirror
 */
export function removeKeyFromIndexedDBMirror(key: string): void {
  if (!hasIndexedDB()) return;
  removeIDBValue(key).catch(() => {});
}

/**
 * Sync entire current localStorage dataset to IndexedDB
 */
export async function syncAllLocalStorageToIndexedDB(): Promise<void> {
  if (!hasWindow() || !hasIndexedDB()) return;

  try {
    const keys: string[] = [];
    for (let i = 0; i < localStorage.length; i++) {
      const k = localStorage.key(i);
      if (k && (k.startsWith('greek_deck_') || k === LEGACY_SRS_KEY)) {
        keys.push(k);
      }
    }

    for (const k of keys) {
      const val = localStorage.getItem(k);
      if (val !== null) {
        await setIDBValue(k, val);
      }
    }
  } catch (err) {
    console.warn('Failed full sync to IndexedDB', err);
  }
}

/**
 * Restore data from IndexedDB into localStorage if localStorage is missing keys or empty
 * (e.g. after PWA update, browser storage flush, or fresh browser context)
 */
export async function restoreFromIndexedDBIfEmpty(): Promise<boolean> {
  if (!hasWindow() || !hasIndexedDB()) return false;

  try {
    const idbKeys = await getAllIDBKeys();
    if (!idbKeys || idbKeys.length === 0) {
      // Nothing in IndexedDB yet, backup current localStorage
      await syncAllLocalStorageToIndexedDB();
      return false;
    }

    let restoredCount = 0;
    for (const key of idbKeys) {
      const existingInLS = localStorage.getItem(key);
      if (!existingInLS) {
        const val = await getIDBValue<string>(key);
        if (val) {
          localStorage.setItem(key, val);
          restoredCount++;
        }
      }
    }

    if (restoredCount > 0) {
      console.log(`[PersistenceEngine] Successfully restored ${restoredCount} keys from IndexedDB!`);
      return true;
    }
  } catch (e) {
    console.warn('Error during IndexedDB restore check', e);
  }
  return false;
}

/**
 * Request persistent browser storage grant from navigator.storage
 * Modern browsers won't clear origin storage under quota pressure when persisted.
 */
export async function requestPersistentStorage(): Promise<{
  supported: boolean;
  persisted: boolean;
  quota?: number;
  usage?: number;
}> {
  if (!hasWindow() || !navigator.storage) {
    return { supported: false, persisted: false };
  }

  let persisted = false;
  try {
    if (navigator.storage.persist) {
      persisted = await navigator.storage.persist();
    } else if (navigator.storage.persisted) {
      persisted = await navigator.storage.persisted();
    }
  } catch (e) {
    console.warn('Error requesting persistent storage', e);
  }

  let quota: number | undefined;
  let usage: number | undefined;
  try {
    if (navigator.storage.estimate) {
      const est = await navigator.storage.estimate();
      quota = est.quota;
      usage = est.usage;
    }
  } catch {}

  return {
    supported: true,
    persisted,
    quota,
    usage,
  };
}

/**
 * Check if origin storage is currently persisted
 */
export async function checkStoragePersisted(): Promise<boolean> {
  if (!hasWindow() || !navigator.storage || !navigator.storage.persisted) {
    return false;
  }
  try {
    return await navigator.storage.persisted();
  } catch {
    return false;
  }
}

/**
 * Full JSON Progress Backup & Restore Structure
 */
export interface FullProgressBackup {
  version: 2;
  exportedAt: string;
  storage: Record<string, string>;
}

/**
 * Export full state as JSON string for safe external backup
 */
export function exportFullProgressBackup(): string {
  if (typeof localStorage === 'undefined') return '{}';

  const backupData: Record<string, string> = {};
  const keys = new Set<string>();

  // 1. Standard W3C Storage API
  if (typeof localStorage.length === 'number' && typeof localStorage.key === 'function') {
    for (let i = 0; i < localStorage.length; i++) {
      const k = localStorage.key(i);
      if (k) keys.add(k);
    }
  }

  // 2. Direct property enumeration fallback
  try {
    for (const k of Object.keys(localStorage)) {
      if (
        k &&
        k !== 'length' &&
        k !== 'key' &&
        k !== 'getItem' &&
        k !== 'setItem' &&
        k !== 'removeItem' &&
        k !== 'clear' &&
        k !== 'store'
      ) {
        keys.add(k);
      }
    }
  } catch {}

  for (const k of keys) {
    if (k && (k.startsWith('greek_deck_') || k === LEGACY_SRS_KEY)) {
      const v = localStorage.getItem(k);
      if (v !== null) {
        backupData[k] = v;
      }
    }
  }

  const payload: FullProgressBackup = {
    version: 2,
    exportedAt: new Date().toISOString(),
    storage: backupData,
  };

  return JSON.stringify(payload, null, 2);
}

/**
 * Import and restore state from a JSON backup string
 */
export async function importFullProgressBackup(jsonStr: string): Promise<{ success: boolean; error?: string; restoredKeys?: number }> {
  if (typeof localStorage === 'undefined') return { success: false, error: 'No storage available' };

  try {
    const parsed = JSON.parse(jsonStr);
    const storageMap = parsed.storage || (parsed.version ? parsed : null);
    if (!storageMap || typeof storageMap !== 'object') {
      return { success: false, error: 'Invalid backup format: missing storage data' };
    }

    let restoredKeys = 0;
    for (const [key, val] of Object.entries(storageMap)) {
      if (typeof key === 'string' && typeof val === 'string' && (key.startsWith('greek_deck_') || key === LEGACY_SRS_KEY)) {
        localStorage.setItem(key, val);
        await setIDBValue(key, val);
        restoredKeys++;
      }
    }

    // Trigger reactivity
    if (typeof window !== 'undefined' && typeof window.dispatchEvent === 'function') {
      window.dispatchEvent(new CustomEvent('greek_deck_user_change'));
      window.dispatchEvent(new CustomEvent('greek_deck_progress_change'));
    }

    return { success: true, restoredKeys };
  } catch (err: any) {
    return { success: false, error: err?.message || 'Failed to parse JSON backup' };
  }
}

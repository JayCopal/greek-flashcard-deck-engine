import { UserProfile, LessonStatus } from '../types/schema';

const GREEK_DECK_USERS_KEY = 'greek_deck_users_v1';
const GREEK_DECK_ACTIVE_USER_KEY = 'greek_deck_active_user_id_v1';
const LEGACY_SRS_KEY = 'greek_deck_srs_state_v1';

const USER_COLORS = [
  '#0284c7', // Sky
  '#10b981', // Emerald
  '#8b5cf6', // Violet
  '#f59e0b', // Amber
  '#ec4899', // Pink
  '#06b6d4', // Cyan
  '#f97316', // Orange
];

export function getSRSStorageKey(userId?: string): string {
  const uid = userId || getActiveUserId();
  return `greek_deck_srs_${uid}`;
}

export function getLessonStorageKey(userId?: string): string {
  const uid = userId || getActiveUserId();
  return `greek_deck_lessons_${uid}`;
}

/**
 * Initialize default user and migrate legacy single-user data if needed
 */
export function initializeUsers(): UserProfile[] {
  try {
    const raw = localStorage.getItem(GREEK_DECK_USERS_KEY);
    if (raw) {
      const users: UserProfile[] = JSON.parse(raw);
      if (users && users.length > 0) {
        return users;
      }
    }
  } catch (e) {
    console.warn('Error reading users from localStorage', e);
  }

  // Create initial default user
  const defaultUser: UserProfile = {
    id: 'default',
    name: 'Learner 1',
    createdAt: new Date().toISOString(),
    lastActiveAt: new Date().toISOString(),
    color: USER_COLORS[0],
  };

  try {
    // Migration: Check if legacy SRS data exists
    const legacySRS = localStorage.getItem(LEGACY_SRS_KEY);
    if (legacySRS) {
      localStorage.setItem(`greek_deck_srs_default`, legacySRS);
    }
    localStorage.setItem(GREEK_DECK_USERS_KEY, JSON.stringify([defaultUser]));
    localStorage.setItem(GREEK_DECK_ACTIVE_USER_KEY, defaultUser.id);
  } catch (e) {
    console.error('Error initializing users in localStorage', e);
  }

  return [defaultUser];
}

export function getUsers(): UserProfile[] {
  try {
    const raw = localStorage.getItem(GREEK_DECK_USERS_KEY);
    if (raw) {
      const users: UserProfile[] = JSON.parse(raw);
      if (users && users.length > 0) return users;
    }
  } catch {}
  return initializeUsers();
}

export function saveUsers(users: UserProfile[]): void {
  try {
    localStorage.setItem(GREEK_DECK_USERS_KEY, JSON.stringify(users));
  } catch (err) {
    console.error('Failed to save users', err);
  }
}

export function getActiveUserId(): string {
  try {
    const active = localStorage.getItem(GREEK_DECK_ACTIVE_USER_KEY);
    if (active) return active;
  } catch {}
  const users = getUsers();
  const firstId = users[0]?.id || 'default';
  try {
    localStorage.setItem(GREEK_DECK_ACTIVE_USER_KEY, firstId);
  } catch {}
  return firstId;
}

export function getActiveUser(): UserProfile {
  const users = getUsers();
  const activeId = getActiveUserId();
  const found = users.find((u) => u.id === activeId);
  if (found) return found;

  const fallback = users[0] || {
    id: 'default',
    name: 'Learner 1',
    createdAt: new Date().toISOString(),
    lastActiveAt: new Date().toISOString(),
    color: USER_COLORS[0],
  };
  setActiveUserId(fallback.id);
  return fallback;
}

export function setActiveUserId(userId: string): void {
  try {
    localStorage.setItem(GREEK_DECK_ACTIVE_USER_KEY, userId);
    // Update lastActiveAt
    const users = getUsers();
    const updated = users.map((u) =>
      u.id === userId ? { ...u, lastActiveAt: new Date().toISOString() } : u
    );
    saveUsers(updated);
  } catch (err) {
    console.error('Failed to set active user', err);
  }
  notifyUserChanged();
}

export function createUser(name: string): UserProfile {
  const trimmed = name.trim() || 'Learner';
  const users = getUsers();
  const id = `user_${Date.now()}_${Math.random().toString(36).substring(2, 7)}`;
  const color = USER_COLORS[users.length % USER_COLORS.length];
  
  const newUser: UserProfile = {
    id,
    name: trimmed,
    createdAt: new Date().toISOString(),
    lastActiveAt: new Date().toISOString(),
    color,
  };

  const updated = [...users, newUser];
  saveUsers(updated);
  setActiveUserId(id);
  return newUser;
}

export function renameUser(userId: string, newName: string): UserProfile | null {
  const trimmed = newName.trim();
  if (!trimmed) return null;

  const users = getUsers();
  let updatedUser: UserProfile | null = null;
  const updated = users.map((u) => {
    if (u.id === userId) {
      updatedUser = { ...u, name: trimmed };
      return updatedUser;
    }
    return u;
  });

  if (updatedUser) {
    saveUsers(updated);
    notifyUserChanged();
  }
  return updatedUser;
}

export function deleteUser(userId: string): boolean {
  const users = getUsers();
  if (users.length <= 1) {
    return false; // Cannot delete the sole user profile
  }

  const updated = users.filter((u) => u.id !== userId);
  saveUsers(updated);

  // Clean up user's local storage data
  try {
    localStorage.removeItem(`greek_deck_srs_${userId}`);
    localStorage.removeItem(`greek_deck_lessons_${userId}`);
  } catch {}

  // If the active user was deleted, switch to the first remaining user
  if (getActiveUserId() === userId) {
    setActiveUserId(updated[0].id);
  } else {
    notifyUserChanged();
  }

  return true;
}

/**
 * Reset all card and lesson progress for a given user (or active user)
 */
export function resetUserProgress(userId?: string): void {
  const uid = userId || getActiveUserId();
  try {
    localStorage.removeItem(`greek_deck_srs_${uid}`);
    localStorage.removeItem(`greek_deck_lessons_${uid}`);
    if (uid === 'default') {
      localStorage.removeItem(LEGACY_SRS_KEY);
    }
  } catch (e) {
    console.error('Failed to reset user progress', e);
  }
  notifyProgressChanged();
}

/**
 * Lesson status per-user storage
 */
export function getUserLessonStatusMap(userId?: string): Record<string, LessonStatus> {
  const key = getLessonStorageKey(userId);
  try {
    const raw = localStorage.getItem(key);
    return raw ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}

export function getUserLessonStatus(lessonId: string, fallback?: LessonStatus, userId?: string): LessonStatus {
  const map = getUserLessonStatusMap(userId);
  if (map[lessonId]) return map[lessonId];
  return fallback || 'not_started';
}

export function setUserLessonStatus(lessonId: string, status: LessonStatus, userId?: string): void {
  const key = getLessonStorageKey(userId);
  const map = getUserLessonStatusMap(userId);
  map[lessonId] = status;
  try {
    localStorage.setItem(key, JSON.stringify(map));
  } catch (err) {
    console.error('Failed to save user lesson status', err);
  }
  notifyProgressChanged();
}

// Event notification systems for React reactivity
export function notifyUserChanged(): void {
  window.dispatchEvent(new CustomEvent('greek_deck_user_change'));
  notifyProgressChanged();
}

export function notifyProgressChanged(): void {
  window.dispatchEvent(new CustomEvent('greek_deck_progress_change'));
}

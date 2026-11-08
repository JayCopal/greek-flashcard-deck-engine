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

export function getLessonNotesStorageKey(userId?: string): string {
  const uid = userId || getActiveUserId();
  return `greek_deck_lesson_notes_${uid}`;
}

export function getLessonCompositeKey(unitId?: string, lessonId?: string): string {
  if (!unitId && !lessonId) return 'unknown';
  if (!unitId) return lessonId!;
  if (!lessonId) return unitId;
  // If lessonId already includes unit prefix (e.g. "unit-01/lesson-01"), return as is
  if (lessonId.includes('/') || lessonId.includes(':')) return lessonId;
  return `${unitId}/${lessonId}`;
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
    localStorage.removeItem(`greek_deck_lesson_notes_${userId}`);
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
    localStorage.removeItem(`greek_deck_lesson_notes_${uid}`);
    localStorage.removeItem(`greek_deck_study_prefs_${uid}`);
    if (uid === 'default') {
      localStorage.removeItem(LEGACY_SRS_KEY);
    }
  } catch (e) {
    console.error('Failed to reset user progress', e);
  }
  notifyProgressChanged();
}

/**
 * User study session preferences (remembered filters & UX settings)
 */
export interface UserStudyPreferences {
  hideLearned: boolean;
  hideExcluded: boolean;
  studyDirection?: 'greek_to_english' | 'english_to_greek';
  autoPlayAudio?: boolean;
  playbackSpeed?: number;
  highlightTonos?: boolean;
  hapticFeedback?: boolean;
  themePreference?: 'slate' | 'oled';
  dailyGoal?: number;
}

export const DEFAULT_STUDY_PREFERENCES: UserStudyPreferences = {
  hideLearned: true,
  hideExcluded: true,
  studyDirection: 'greek_to_english',
  autoPlayAudio: true,
  playbackSpeed: 1.0,
  highlightTonos: true,
  hapticFeedback: true,
  themePreference: 'slate',
  dailyGoal: 20,
};

export function getUserStudyPreferences(userId?: string): UserStudyPreferences {
  const uid = userId || getActiveUserId();
  const key = `greek_deck_study_prefs_${uid}`;
  try {
    const raw = localStorage.getItem(key);
    if (raw) {
      const parsed = JSON.parse(raw);
      return {
        hideLearned: parsed.hideLearned !== undefined ? Boolean(parsed.hideLearned) : true,
        hideExcluded: parsed.hideExcluded !== undefined ? Boolean(parsed.hideExcluded) : true,
        studyDirection: parsed.studyDirection === 'english_to_greek' ? 'english_to_greek' : 'greek_to_english',
        autoPlayAudio: parsed.autoPlayAudio !== undefined ? Boolean(parsed.autoPlayAudio) : true,
        playbackSpeed: typeof parsed.playbackSpeed === 'number' ? parsed.playbackSpeed : 1.0,
        highlightTonos: parsed.highlightTonos !== undefined ? Boolean(parsed.highlightTonos) : true,
        hapticFeedback: parsed.hapticFeedback !== undefined ? Boolean(parsed.hapticFeedback) : true,
        themePreference: parsed.themePreference === 'oled' ? 'oled' : 'slate',
        dailyGoal: typeof parsed.dailyGoal === 'number' ? parsed.dailyGoal : 20,
      };
    }
  } catch (e) {
    console.warn('Failed to read study preferences', e);
  }
  return { ...DEFAULT_STUDY_PREFERENCES };
}

export function setUserStudyPreferences(
  prefs: Partial<UserStudyPreferences>,
  userId?: string
): UserStudyPreferences {
  const uid = userId || getActiveUserId();
  const key = `greek_deck_study_prefs_${uid}`;
  const current = getUserStudyPreferences(uid);
  const updated: UserStudyPreferences = {
    ...current,
    ...prefs,
  };
  try {
    localStorage.setItem(key, JSON.stringify(updated));
    if (typeof window !== 'undefined') {
      window.dispatchEvent(new CustomEvent('greek_deck_prefs_change', { detail: updated }));
    }
  } catch (err) {
    console.error('Failed to save study preferences', err);
  }
  return updated;
}

/**
 * Daily Goal & Review Tracker
 */
export interface DailyReviewData {
  date: string;
  count: number;
  goal: number;
  streak: number;
}

export function getTodayKey(): string {
  const d = new Date();
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
}

export function getDailyReviewData(userId?: string): DailyReviewData {
  const uid = userId || getActiveUserId();
  const prefs = getUserStudyPreferences(uid);
  const today = getTodayKey();
  const key = `greek_deck_daily_reviews_${uid}`;
  try {
    const raw = localStorage.getItem(key);
    if (raw) {
      const data = JSON.parse(raw);
      if (data.date === today) {
        return {
          date: today,
          count: Number(data.count) || 0,
          goal: prefs.dailyGoal || 20,
          streak: Number(data.streak) || 1,
        };
      }
      // If it's a new day, check if yesterday had reviews to continue streak
      const yesterday = new Date();
      yesterday.setDate(yesterday.getDate() - 1);
      const yKey = `${yesterday.getFullYear()}-${String(yesterday.getMonth() + 1).padStart(2, '0')}-${String(yesterday.getDate()).padStart(2, '0')}`;
      const streak = data.date === yKey && data.count >= (data.goal || 10) ? (Number(data.streak) || 1) + 1 : 1;
      return {
        date: today,
        count: 0,
        goal: prefs.dailyGoal || 20,
        streak,
      };
    }
  } catch {}
  return {
    date: today,
    count: 0,
    goal: prefs.dailyGoal || 20,
    streak: 1,
  };
}

export function recordDailyCardReview(userId?: string): DailyReviewData {
  const uid = userId || getActiveUserId();
  const current = getDailyReviewData(uid);
  const today = getTodayKey();
  const updated: DailyReviewData = {
    ...current,
    date: today,
    count: current.count + 1,
  };
  try {
    localStorage.setItem(`greek_deck_daily_reviews_${uid}`, JSON.stringify(updated));
    if (typeof window !== 'undefined') {
      window.dispatchEvent(new CustomEvent('greek_deck_daily_change', { detail: updated }));
    }
  } catch {}
  return updated;
}

/**
 * Last Studied Lesson tracker
 */
export interface LastStudiedLesson {
  unitId: string;
  lessonId: string;
  title: string;
  lessonLabel?: string;
  timestamp: string;
}

export function setLastStudiedLesson(
  lesson: { unitId: string; lessonId: string; title: string; lessonLabel?: string },
  userId?: string
): void {
  const uid = userId || getActiveUserId();
  const data: LastStudiedLesson = {
    ...lesson,
    timestamp: new Date().toISOString(),
  };
  try {
    localStorage.setItem(`greek_deck_last_lesson_${uid}`, JSON.stringify(data));
    if (typeof window !== 'undefined') {
      window.dispatchEvent(new CustomEvent('greek_deck_last_lesson_change', { detail: data }));
    }
  } catch {}
}

export function getLastStudiedLesson(userId?: string): LastStudiedLesson | null {
  const uid = userId || getActiveUserId();
  try {
    const raw = localStorage.getItem(`greek_deck_last_lesson_${uid}`);
    return raw ? JSON.parse(raw) : null;
  } catch {
    return null;
  }
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

const VALID_LESSON_STATUSES: Set<string> = new Set([
  'not_started',
  'in_progress',
  'in_progress_1',
  'in_progress_2',
  'in_progress_3',
  'in_progress_4',
  'in_progress_5',
  'learned',
]);

function isLessonStatus(val: any): val is LessonStatus {
  return typeof val === 'string' && VALID_LESSON_STATUSES.has(val);
}

function normalizeLessonStatus(status: LessonStatus | string | undefined): LessonStatus {
  if (!status) return 'not_started';
  if (status === 'in_progress') return 'in_progress_1';
  return status as LessonStatus;
}

export function getUserLessonStatus(
  unitIdOrLessonId: string,
  lessonIdOrFallback?: string | LessonStatus,
  fallback?: LessonStatus,
  userId?: string
): LessonStatus {
  // Determine arguments based on whether unitId and lessonId were both provided
  let compositeKey: string;
  let effectiveFallback: LessonStatus;
  let effectiveUserId: string | undefined;

  if (isLessonStatus(lessonIdOrFallback) || lessonIdOrFallback === undefined) {
    // Single ID signature: getUserLessonStatus(lessonId, fallback, userId)
    compositeKey = unitIdOrLessonId;
    effectiveFallback = normalizeLessonStatus((lessonIdOrFallback as LessonStatus) || fallback);
    effectiveUserId = userId;
  } else {
    // Two-part signature: getUserLessonStatus(unitId, lessonId, fallback, userId)
    compositeKey = getLessonCompositeKey(unitIdOrLessonId, lessonIdOrFallback);
    effectiveFallback = normalizeLessonStatus(fallback);
    effectiveUserId = userId;
  }

  const map = getUserLessonStatusMap(effectiveUserId);
  // Check exact composite key first
  if (map[compositeKey]) return normalizeLessonStatus(map[compositeKey]);

  return effectiveFallback;
}

export function setUserLessonStatus(
  unitIdOrLessonId: string,
  lessonIdOrStatus: string | LessonStatus,
  statusOrUserId?: LessonStatus | string,
  userId?: string
): void {
  let compositeKey: string;
  let status: LessonStatus;
  let effectiveUserId: string | undefined;

  if (isLessonStatus(lessonIdOrStatus)) {
    // Single ID signature: setUserLessonStatus(lessonId, status, userId)
    compositeKey = unitIdOrLessonId;
    status = normalizeLessonStatus(lessonIdOrStatus as LessonStatus);
    effectiveUserId = statusOrUserId as string | undefined;
  } else {
    // Two-part signature: setUserLessonStatus(unitId, lessonId, status, userId)
    compositeKey = getLessonCompositeKey(unitIdOrLessonId, lessonIdOrStatus);
    status = normalizeLessonStatus(statusOrUserId as LessonStatus);
    effectiveUserId = userId;
  }

  const key = getLessonStorageKey(effectiveUserId);
  const map = getUserLessonStatusMap(effectiveUserId);
  map[compositeKey] = status;

  // Clean up legacy global colliding key if present
  if (map['lesson-01']) {
    delete map['lesson-01'];
  }

  try {
    localStorage.setItem(key, JSON.stringify(map));
  } catch (err) {
    console.error('Failed to save user lesson status', err);
  }
  notifyProgressChanged();
}

/**
 * Lesson notes per-user / offline storage
 */
export function getUserLessonNotesMap(userId?: string): Record<string, string> {
  const key = getLessonNotesStorageKey(userId);
  try {
    const raw = localStorage.getItem(key);
    return raw ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}

export function getUserLessonNotes(
  unitIdOrLessonId: string,
  lessonIdOrFallback?: string,
  fallback?: string,
  userId?: string
): string {
  let compositeKey: string;
  let effectiveFallback: string;
  let effectiveUserId: string | undefined;

  // Check if called as (unitId, lessonId, fallback, userId) or (lessonId, fallback, userId)
  if (
    lessonIdOrFallback !== undefined &&
    (lessonIdOrFallback.startsWith('lesson-') || lessonIdOrFallback.includes('-'))
  ) {
    compositeKey = getLessonCompositeKey(unitIdOrLessonId, lessonIdOrFallback);
    effectiveFallback = fallback || '';
    effectiveUserId = userId;
  } else {
    compositeKey = unitIdOrLessonId;
    effectiveFallback = lessonIdOrFallback || fallback || '';
    effectiveUserId = userId;
  }

  const map = getUserLessonNotesMap(effectiveUserId);
  if (map[compositeKey] !== undefined) return map[compositeKey];
  return effectiveFallback;
}

export function setUserLessonNotes(
  unitIdOrLessonId: string,
  lessonIdOrNotes: string,
  notesOrUserId?: string,
  userId?: string
): void {
  let compositeKey: string;
  let notes: string;
  let effectiveUserId: string | undefined;

  if (notesOrUserId !== undefined && (notesOrUserId.length > 0 || userId !== undefined)) {
    // Called as (unitId, lessonId, notes, userId)
    compositeKey = getLessonCompositeKey(unitIdOrLessonId, lessonIdOrNotes);
    notes = notesOrUserId;
    effectiveUserId = userId;
  } else {
    // Called as (lessonId, notes, userId)
    compositeKey = unitIdOrLessonId;
    notes = lessonIdOrNotes;
    effectiveUserId = notesOrUserId;
  }

  const key = getLessonNotesStorageKey(effectiveUserId);
  const map = getUserLessonNotesMap(effectiveUserId);
  map[compositeKey] = notes;

  try {
    localStorage.setItem(key, JSON.stringify(map));
  } catch (err) {
    console.error('Failed to save user lesson notes', err);
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

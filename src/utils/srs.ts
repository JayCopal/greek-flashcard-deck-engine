import { CardSRSData, SRSRating, CardEntry } from '../types/schema';
import { getSRSStorageKey, notifyProgressChanged } from './userStorage';

export function getAllSRSData(userId?: string): Record<string, CardSRSData> {
  const key = getSRSStorageKey(userId);
  try {
    const raw = localStorage.getItem(key);
    return raw ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}

export function saveAllSRSData(data: Record<string, CardSRSData>, userId?: string): void {
  const key = getSRSStorageKey(userId);
  try {
    localStorage.setItem(key, JSON.stringify(data));
    notifyProgressChanged();
  } catch (err) {
    console.error('Failed to save SRS state to localStorage', err);
  }
}

export function getCardSRS(cardId: string, userId?: string): CardSRSData {
  const all = getAllSRSData(userId);
  if (all[cardId]) {
    return all[cardId];
  }
  return {
    cardId,
    isLearned: false,
    isExcluded: false,
    intervalDays: 0,
    repetition: 0,
    easeFactor: 2.5,
  };
}

export function toggleCardLearned(cardId: string, userId?: string): boolean {
  const all = getAllSRSData(userId);
  const current = all[cardId] || {
    cardId,
    isLearned: false,
    isExcluded: false,
    intervalDays: 0,
    repetition: 0,
    easeFactor: 2.5,
  };

  current.isLearned = !current.isLearned;
  all[cardId] = current;
  saveAllSRSData(all, userId);
  return current.isLearned;
}

export function setCardLearned(cardId: string, learned: boolean, userId?: string): void {
  const all = getAllSRSData(userId);
  const current = all[cardId] || {
    cardId,
    isLearned: false,
    isExcluded: false,
    intervalDays: 0,
    repetition: 0,
    easeFactor: 2.5,
  };

  current.isLearned = learned;
  all[cardId] = current;
  saveAllSRSData(all, userId);
}

export function toggleCardExcluded(cardId: string, userId?: string): boolean {
  const all = getAllSRSData(userId);
  const current = all[cardId] || {
    cardId,
    isLearned: false,
    isExcluded: false,
    intervalDays: 0,
    repetition: 0,
    easeFactor: 2.5,
  };

  current.isExcluded = !current.isExcluded;
  all[cardId] = current;
  saveAllSRSData(all, userId);
  return current.isExcluded;
}

export function setCardExcluded(cardId: string, excluded: boolean, userId?: string): void {
  const all = getAllSRSData(userId);
  const current = all[cardId] || {
    cardId,
    isLearned: false,
    isExcluded: false,
    intervalDays: 0,
    repetition: 0,
    easeFactor: 2.5,
  };

  current.isExcluded = excluded;
  all[cardId] = current;
  saveAllSRSData(all, userId);
}

export function recordSRSRating(cardId: string, rating: SRSRating, userId?: string): CardSRSData {
  const all = getAllSRSData(userId);
  const current = all[cardId] || {
    cardId,
    isLearned: false,
    isExcluded: false,
    intervalDays: 0,
    repetition: 0,
    easeFactor: 2.5,
  };

  let { intervalDays, repetition, easeFactor } = current;

  if (rating === 'again') {
    repetition = 0;
    intervalDays = 1;
    easeFactor = Math.max(1.3, easeFactor - 0.2);
  } else if (rating === 'hard') {
    intervalDays = Math.max(1, Math.round(intervalDays * 1.2));
    easeFactor = Math.max(1.3, easeFactor - 0.15);
  } else if (rating === 'good') {
    if (repetition === 0) {
      intervalDays = 1;
    } else if (repetition === 1) {
      intervalDays = 3;
    } else {
      intervalDays = Math.round(intervalDays * easeFactor);
    }
    repetition += 1;
  } else if (rating === 'easy') {
    if (repetition === 0) {
      intervalDays = 2;
    } else if (repetition === 1) {
      intervalDays = 5;
    } else {
      intervalDays = Math.round(intervalDays * easeFactor * 1.3);
    }
    repetition += 1;
    easeFactor += 0.15;
  }

  const now = new Date();
  const nextDue = new Date();
  nextDue.setDate(nextDue.getDate() + intervalDays);

  const updated: CardSRSData = {
    ...current,
    lastRating: rating,
    intervalDays,
    repetition,
    easeFactor: Number(easeFactor.toFixed(2)),
    lastReviewed: now.toISOString(),
    nextReviewDue: nextDue.toISOString(),
  };

  all[cardId] = updated;
  saveAllSRSData(all, userId);
  return updated;
}

export function isCardDue(srs: CardSRSData): boolean {
  if (!srs.nextReviewDue) return true; // new card is always due
  return new Date(srs.nextReviewDue) <= new Date();
}

export type RatingFilterOption = 'all' | 'again' | 'hard' | 'good' | 'easy' | 'new';

export function getCardRatingStatus(srs?: CardSRSData): SRSRating | 'new' {
  if (!srs || !srs.lastReviewed) return 'new';
  if (srs.lastRating) return srs.lastRating;
  if (srs.repetition === 0) return 'again';
  if (srs.easeFactor < 2.0) return 'hard';
  return 'good';
}

export function filterStudyCards(
  cards: CardEntry[],
  options: {
    hideLearned: boolean;
    dueOnly: boolean;
    hideExcluded?: boolean;
    ratingFilter?: RatingFilterOption;
  },
  userId?: string
): CardEntry[] {
  const allSRS = getAllSRSData(userId);
  const hideExcluded = options.hideExcluded ?? true;
  const ratingFilter = options.ratingFilter ?? 'all';

  return cards.filter((card) => {
    const srs = allSRS[card.id] || {
      cardId: card.id,
      isLearned: false,
      isExcluded: false,
      intervalDays: 0,
      repetition: 0,
      easeFactor: 2.5,
    };

    if (hideExcluded && srs.isExcluded) {
      return false;
    }

    if (options.hideLearned && srs.isLearned) {
      return false;
    }

    if (options.dueOnly && !isCardDue(srs)) {
      return false;
    }

    if (ratingFilter !== 'all') {
      const status = getCardRatingStatus(srs);
      if (status !== ratingFilter) {
        return false;
      }
    }

    return true;
  });
}

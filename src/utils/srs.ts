import { CardSRSData, SRSRating, CardEntry } from '../types/schema';

const SRS_STORAGE_KEY = 'greek_deck_srs_state_v1';

export function getAllSRSData(): Record<string, CardSRSData> {
  try {
    const raw = localStorage.getItem(SRS_STORAGE_KEY);
    return raw ? JSON.parse(raw) : {};
  } catch {
    return {};
  }
}

export function saveAllSRSData(data: Record<string, CardSRSData>): void {
  try {
    localStorage.setItem(SRS_STORAGE_KEY, JSON.stringify(data));
  } catch (err) {
    console.error('Failed to save SRS state to localStorage', err);
  }
}

export function getCardSRS(cardId: string): CardSRSData {
  const all = getAllSRSData();
  if (all[cardId]) {
    return all[cardId];
  }
  return {
    cardId,
    isLearned: false,
    intervalDays: 0,
    repetition: 0,
    easeFactor: 2.5,
  };
}

export function toggleCardLearned(cardId: string): boolean {
  const all = getAllSRSData();
  const current = all[cardId] || {
    cardId,
    isLearned: false,
    intervalDays: 0,
    repetition: 0,
    easeFactor: 2.5,
  };

  current.isLearned = !current.isLearned;
  all[cardId] = current;
  saveAllSRSData(all);
  return current.isLearned;
}

export function setCardLearned(cardId: string, learned: boolean): void {
  const all = getAllSRSData();
  const current = all[cardId] || {
    cardId,
    isLearned: false,
    intervalDays: 0,
    repetition: 0,
    easeFactor: 2.5,
  };

  current.isLearned = learned;
  all[cardId] = current;
  saveAllSRSData(all);
}

export function recordSRSRating(cardId: string, rating: SRSRating): CardSRSData {
  const all = getAllSRSData();
  const current = all[cardId] || {
    cardId,
    isLearned: false,
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
    intervalDays,
    repetition,
    easeFactor: Number(easeFactor.toFixed(2)),
    lastReviewed: now.toISOString(),
    nextReviewDue: nextDue.toISOString(),
  };

  all[cardId] = updated;
  saveAllSRSData(all);
  return updated;
}

export function isCardDue(srs: CardSRSData): boolean {
  if (!srs.nextReviewDue) return true; // new card is always due
  return new Date(srs.nextReviewDue) <= new Date();
}

export function filterStudyCards(
  cards: CardEntry[],
  options: {
    hideLearned: boolean;
    dueOnly: boolean;
  }
): CardEntry[] {
  const allSRS = getAllSRSData();

  return cards.filter((card) => {
    const srs = allSRS[card.id] || {
      cardId: card.id,
      isLearned: false,
      intervalDays: 0,
      repetition: 0,
      easeFactor: 2.5,
    };

    if (options.hideLearned && srs.isLearned) {
      return false;
    }

    if (options.dueOnly && !isCardDue(srs)) {
      return false;
    }

    return true;
  });
}

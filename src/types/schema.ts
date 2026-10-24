export type EntryStatus = 'pending_tts' | 'needs_review' | 'verified';

export interface CardEntry {
  id: string;
  greek: string;
  phonetic_hint?: string;
  english: string;
  notes?: string;
  gender_or_pos?: string;
  audio: string | null;
  status: EntryStatus;
}

export interface Lesson {
  unit_id: string;
  lesson_id: string;
  title: string;
  description?: string;
  entries: CardEntry[];
  total_entries?: number;
  verified_entries?: number;
  coverage_percentage?: number;
}

export interface Unit {
  id: string;
  title: string;
  order: number;
  lessons: Lesson[];
  total_entries?: number;
  verified_entries?: number;
  coverage_percentage?: number;
}

export interface DeckManifest {
  deck_title: string;
  source_language: string;
  target_language: string;
  created_at?: string;
}

export interface DeckStats {
  total_units: number;
  total_lessons: number;
  total_entries: number;
  verified_count: number;
  pending_count: number;
  needs_review_count: number;
  coverage_percentage: number;
}

export interface DeckData {
  manifest: DeckManifest;
  stats: DeckStats;
  units: Unit[];
}

export interface ChirpVoice {
  id: string;
  name: string;
  gender: 'FEMALE' | 'MALE';
  description: string;
  isDefault: boolean;
}

export type SRSRating = 'again' | 'hard' | 'good' | 'easy';

export interface CardSRSData {
  cardId: string;
  isLearned: boolean;
  intervalDays: number;
  repetition: number;
  easeFactor: number;
  lastReviewed?: string;
  nextReviewDue?: string;
}


// Test suite for Greek Flashcard Deck SRS logic & mutual exclusivity
import assert from 'node:assert';

// 1. Mock browser localStorage and window event system
class LocalStorageMock {
  private store: Record<string, string> = {};

  get length(): number {
    return Object.keys(this.store).length;
  }

  key(index: number): string | null {
    const keys = Object.keys(this.store);
    return keys[index] ?? null;
  }

  getItem(key: string): string | null {
    return this.store[key] ?? null;
  }

  setItem(key: string, value: string): void {
    this.store[key] = String(value);
  }

  removeItem(key: string): void {
    delete this.store[key];
  }

  clear(): void {
    this.store = {};
  }
}

const mockStorage = new LocalStorageMock();
(globalThis as any).localStorage = mockStorage;
(globalThis as any).window = {
  dispatchEvent: () => true,
};
(globalThis as any).CustomEvent = class {
  type: string;
  constructor(type: string) {
    this.type = type;
  }
};

// 2. Import SRS functions to test
import {
  getAllSRSData,
  getCardSRS,
  toggleCardLearned,
  setCardLearned,
  toggleCardExcluded,
  setCardExcluded,
  recordSRSRating,
  filterStudyCards,
  recordCardPresentation,
  getCardPresentationCount,
} from '../src/utils/srs.ts';
import { exportFullProgressBackup, importFullProgressBackup } from '../src/utils/userStorage.ts';
import { CardEntry } from '../src/types/schema.ts';

console.log('--- STARTING SRS LOGIC & MUTUAL EXCLUSIVITY TESTS ---');

const testUserId = 'test-user-1';

// TEST 1: Initial state
console.log('Test 1: Initial state of an unreviewed card');
mockStorage.clear();
const initialCard = getCardSRS('card-001', testUserId);
assert.strictEqual(initialCard.isLearned, false, 'Card should initially not be learned');
assert.strictEqual(initialCard.isExcluded, false, 'Card should initially not be excluded');
console.log('  ✓ Initial state is clean (isLearned: false, isExcluded: false)');

// TEST 2: Toggle Learned
console.log('Test 2: Marking card as Learned');
const learnedRes = toggleCardLearned('card-001', testUserId);
assert.strictEqual(learnedRes, true, 'toggleCardLearned should return true');
const cardAfterLearned = getCardSRS('card-001', testUserId);
assert.strictEqual(cardAfterLearned.isLearned, true, 'Card must be marked as Learned');
assert.strictEqual(cardAfterLearned.isExcluded, false, 'Card must NOT be Excluded');
console.log('  ✓ toggleCardLearned set isLearned: true, isExcluded: false');

// TEST 3: Marking Learned card as Ignored (Exclude)
console.log('Test 3: Marking an already-learned card as Ignored (Excluded)');
const excludedRes = toggleCardExcluded('card-001', testUserId);
assert.strictEqual(excludedRes, true, 'toggleCardExcluded should return true');
const cardAfterExcluded = getCardSRS('card-001', testUserId);
assert.strictEqual(cardAfterExcluded.isExcluded, true, 'Card must now be Excluded');
assert.strictEqual(cardAfterExcluded.isLearned, false, 'Card must NO LONGER be Learned (mutual exclusivity)');
console.log('  ✓ toggleCardExcluded set isExcluded: true and cleared isLearned: false');

// TEST 4: Marking Ignored card as Learned
console.log('Test 4: Marking an ignored card as Learned');
const learnedRes2 = toggleCardLearned('card-001', testUserId);
assert.strictEqual(learnedRes2, true, 'toggleCardLearned should return true');
const cardAfterRelearn = getCardSRS('card-001', testUserId);
assert.strictEqual(cardAfterRelearn.isLearned, true, 'Card must now be Learned');
assert.strictEqual(cardAfterRelearn.isExcluded, false, 'Card must NO LONGER be Excluded (mutual exclusivity)');
console.log('  ✓ toggleCardLearned set isLearned: true and cleared isExcluded: false');

// TEST 5: setCardLearned & setCardExcluded explicit setters
console.log('Test 5: Explicit setters setCardLearned and setCardExcluded');
setCardExcluded('card-002', true, testUserId);
let c2 = getCardSRS('card-002', testUserId);
assert.strictEqual(c2.isExcluded, true);
assert.strictEqual(c2.isLearned, false);

setCardLearned('card-002', true, testUserId);
c2 = getCardSRS('card-002', testUserId);
assert.strictEqual(c2.isLearned, true);
assert.strictEqual(c2.isExcluded, false, 'setCardLearned must clear isExcluded');

setCardExcluded('card-002', true, testUserId);
c2 = getCardSRS('card-002', testUserId);
assert.strictEqual(c2.isExcluded, true);
assert.strictEqual(c2.isLearned, false, 'setCardExcluded must clear isLearned');
console.log('  ✓ Explicit setters enforce mutual exclusivity');

// TEST 6: Legacy dirty localStorage data sanitization
console.log('Test 6: Sanitizing existing dirty data where both isLearned and isExcluded were true');
const dirtyKey = `greek_deck_srs_${testUserId}`;
mockStorage.setItem(
  dirtyKey,
  JSON.stringify({
    'dirty-card-1': {
      cardId: 'dirty-card-1',
      isLearned: true,
      isExcluded: true, // Corrupted legacy state!
      intervalDays: 5,
      repetition: 2,
      easeFactor: 2.5,
    },
    'pure-ignored-card': {
      cardId: 'pure-ignored-card',
      isLearned: false,
      isExcluded: true,
      intervalDays: 0,
      repetition: 0,
      easeFactor: 2.5,
    },
    'pure-learned-card': {
      cardId: 'pure-learned-card',
      isLearned: true,
      isExcluded: false,
      intervalDays: 10,
      repetition: 4,
      easeFactor: 2.6,
    },
  })
);

const sanitized = getAllSRSData(testUserId);
assert.strictEqual(sanitized['dirty-card-1'].isLearned, true, 'Learned flag preserved');
assert.strictEqual(sanitized['dirty-card-1'].isExcluded, false, 'Excluded flag cleared on dirty card');
assert.strictEqual(sanitized['pure-ignored-card'].isExcluded, true, 'Pure ignored card kept excluded');
assert.strictEqual(sanitized['pure-ignored-card'].isLearned, false, 'Pure ignored card kept unlearned');
assert.strictEqual(sanitized['pure-learned-card'].isLearned, true, 'Pure learned card kept learned');
assert.strictEqual(sanitized['pure-learned-card'].isExcluded, false, 'Pure learned card kept not excluded');
console.log('  ✓ Dirty legacy state was cleanly sanitized');

// TEST 7: recordSRSRating clears excluded status
console.log('Test 7: Assessing an ignored card with SRS rating');
setCardExcluded('card-003', true, testUserId);
assert.strictEqual(getCardSRS('card-003', testUserId).isExcluded, true);
recordSRSRating('card-003', 'good', testUserId);
const ratedCard = getCardSRS('card-003', testUserId);
assert.strictEqual(ratedCard.isExcluded, false, 'Rating a card must un-ignore it');
assert.strictEqual(ratedCard.lastRating, 'good', 'SRS rating recorded');
console.log('  ✓ recordSRSRating un-ignored the rated card');

// TEST 8: filterStudyCards segregation
console.log('Test 8: Study filtering verification');
const mockCards: CardEntry[] = [
  { id: 'c-active', greek: 'νερό', english: 'water', audio: null, status: 'verified' },
  { id: 'c-learned', greek: 'γάλα', english: 'milk', audio: null, status: 'verified' },
  { id: 'c-ignored', greek: 'καφές', english: 'coffee', audio: null, status: 'verified' },
];

setCardLearned('c-learned', true, testUserId);
setCardExcluded('c-ignored', true, testUserId);

// 8A. Normal study session (hideLearned: true, hideExcluded: true)
const normalDrill = filterStudyCards(mockCards, { hideLearned: true, dueOnly: false, hideExcluded: true }, testUserId);
assert.deepStrictEqual(normalDrill.map(c => c.id), ['c-active'], 'Normal drill should only show active card');
console.log('  ✓ Normal drill hides both learned and ignored cards');

// 8B. Already Learnt drill (hideLearned: false, hideExcluded: true)
const learnedDrill = filterStudyCards(mockCards, { hideLearned: false, dueOnly: false, hideExcluded: true }, testUserId);
assert.strictEqual(learnedDrill.some(c => c.id === 'c-ignored'), false, 'Learned drill must NEVER contain ignored cards');
assert.strictEqual(learnedDrill.some(c => c.id === 'c-learned'), true, 'Learned drill contains learned cards');
console.log('  ✓ Already Learnt drill contains learned cards and strictly excludes ignored cards');

// 8C. Ignored drill (hideExcluded: false, hideLearned: true)
const ignoredDrill = filterStudyCards(mockCards, { hideExcluded: false, dueOnly: false, hideLearned: true }, testUserId);
assert.strictEqual(ignoredDrill.some(c => c.id === 'c-learned'), false, 'Ignored drill must NEVER contain learned cards');
assert.strictEqual(ignoredDrill.some(c => c.id === 'c-ignored'), true, 'Ignored drill contains ignored cards');
console.log('  ✓ Ignored drill contains ignored cards and strictly excludes learned cards');

// TEST 9: Card Presentation Tracking
console.log('Test 9: Card Presentation Counter tracking');
const cardP = 'card-presentation-001';
assert.strictEqual(getCardPresentationCount(cardP, testUserId), 0, 'Initially presentation count is 0');

recordCardPresentation(cardP, testUserId);
assert.strictEqual(getCardPresentationCount(cardP, testUserId), 1, 'First presentation increments to 1');
const p1 = getCardSRS(cardP, testUserId);
assert.strictEqual(p1.timesPresented, 1);
assert.ok(p1.lastPresented, 'Timestamp lastPresented must be recorded');

recordCardPresentation(cardP, testUserId);
assert.strictEqual(getCardPresentationCount(cardP, testUserId), 2, 'Second presentation increments to 2');

recordCardPresentation(cardP, testUserId);
assert.strictEqual(getCardPresentationCount(cardP, testUserId), 3, 'Third presentation increments to 3');

// Rating preserves presentation count
recordSRSRating(cardP, 'good', testUserId);
const pRated = getCardSRS(cardP, testUserId);
assert.strictEqual(pRated.timesPresented, 3, 'Rating card preserves existing presentation count');
assert.strictEqual(pRated.lastRating, 'good');

// Toggling learned preserves presentation count
toggleCardLearned(cardP, testUserId);
const pLearned = getCardSRS(cardP, testUserId);
assert.strictEqual(pLearned.timesPresented, 3, 'Toggling learned preserves presentation count');
console.log('  ✓ Card presentation count increments accurately and is preserved across ratings');

// TEST 10: JSON Backup & Restore
console.log('Test 10: JSON Progress Backup Export and Import');
const backupJson = exportFullProgressBackup();
assert.ok(backupJson.includes('card-presentation-001'), 'Backup must contain card presentation data');
const parsedBackup = JSON.parse(backupJson);
assert.strictEqual(parsedBackup.version, 2);
assert.ok(parsedBackup.storage, 'Backup must contain storage map');

// Simulate clearing storage and restoring
mockStorage.clear();
assert.strictEqual(getCardPresentationCount(cardP, testUserId), 0, 'Storage cleared');

await importFullProgressBackup(backupJson);
assert.strictEqual(getCardPresentationCount(cardP, testUserId), 3, 'Import restored presentation count');
const restoredCard = getCardSRS(cardP, testUserId);
assert.strictEqual(restoredCard.timesPresented, 3);
assert.strictEqual(restoredCard.lastRating, 'good');
console.log('  ✓ Progress export & restore completely recovers state');

console.log('\n========================================');
console.log('ALL 10 SRS SUITE TESTS PASSED SUCCESSFULLY!');
console.log('========================================');

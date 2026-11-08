import { sanitizeEnglishPrompt, getProductionHint } from '../src/utils/flashcardPrompt';
import { CardEntry } from '../src/types/schema';

// Test Cases for sanitizeEnglishPrompt
const testCases = [
  {
    input: 'to read / read! (διαβάστε)',
    expected: 'to read / read!',
  },
  {
    input: 'to write / write! (γράψτε)',
    expected: 'to write / write!',
  },
  {
    input: 'the exam / examination (οι εξετάσεις)',
    expected: 'the exam / examination',
  },
  {
    input: 'you are (2nd person singular of είμαι)',
    expected: 'you are (2nd person singular)',
  },
  {
    input: 'we are (1st person plural of είμαι)',
    expected: 'we are (1st person plural)',
  },
  {
    input: 'friend (male)',
    expected: 'friend (male)',
  },
  {
    input: 'friend (female)',
    expected: 'friend (female)',
  },
  {
    input: 'letter (alphabet) / postal letter',
    expected: 'letter (alphabet) / postal letter',
  },
  {
    input: 'airplane / plane',
    expected: 'airplane / plane',
  },
];

let allPassed = true;

for (const tc of testCases) {
  const actual = sanitizeEnglishPrompt(tc.input);
  if (actual !== tc.expected) {
    console.error(`FAIL: "${tc.input}" => "${actual}", expected "${tc.expected}"`);
    allPassed = false;
  } else {
    console.log(`PASS: "${tc.input}" => "${actual}"`);
  }
}

// Test getProductionHint
const card1: CardEntry = {
  id: 'A1-U101-001',
  greek: 'το αεροπλάνο',
  english: 'airplane / plane',
  gender_or_pos: 'noun (neuter)',
  audio: null,
  status: 'verified',
  grammatical_info: { part_of_speech: 'noun (neuter)' }
};

const hint1 = getProductionHint(card1);
console.log('Hint 1:', hint1);

const card2: CardEntry = {
  id: 'A1-U00-001',
  greek: 'διαβάζω',
  english: 'to read / read!',
  gender_or_pos: 'verb',
  audio: null,
  status: 'verified',
  grammatical_info: { verb_type: 'Type A' }
};

const hint2 = getProductionHint(card2);
console.log('Hint 2:', hint2);

if (!allPassed) {
  process.exit(1);
} else {
  console.log('All sanitizer tests passed!');
}

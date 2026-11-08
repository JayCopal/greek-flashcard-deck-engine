import { sanitizeEnglishPrompt, getProductionHint, maskGreekText } from '../src/utils/flashcardPrompt';
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

// Test maskGreekText
const maskCases = [
  {
    input: 'διαβάζω',
    reveal: 1,
    expected: 'δ******',
  },
  {
    input: 'διαβάζω',
    reveal: 2,
    expected: 'δι*****',
  },
  {
    input: 'διαβάζω',
    reveal: 3,
    expected: 'δια****',
  },
  {
    input: 'το αεροπλάνο',
    reveal: 1,
    expected: 'τ* α********',
  },
  {
    input: 'το αεροπλάνο',
    reveal: 2,
    expected: 'το αε*******',
  },
  {
    input: 'δεν είναι εδώ',
    reveal: 1,
    expected: 'δ** ε**** ε**',
  },
  {
    input: 'δεν είναι εδώ',
    reveal: 2,
    expected: 'δε* εί*** εδ*',
  },
  {
    input: '- Γεια σας, πού μένετε;',
    reveal: 1,
    expected: '- Γ*** σ**, π** μ*****;',
  },
  {
    input: '- Γεια σας, πού μένετε;',
    reveal: 2,
    expected: '- Γε** σα*, πο* μέ****;',
  },
];

for (const mc of maskCases) {
  const actual = maskGreekText(mc.input, mc.reveal);
  if (actual !== mc.expected) {
    console.error(`FAIL mask: "${mc.input}" (reveal ${mc.reveal}) => "${actual}", expected "${mc.expected}"`);
    allPassed = false;
  } else {
    console.log(`PASS mask: "${mc.input}" (reveal ${mc.reveal}) => "${actual}"`);
  }
}

// Test getProductionHint on Noun
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
if (hint1.step1Mask !== 'τ* α********' || hint1.step2Mask !== 'το αε*******') {
  console.error('FAIL: hint1 mask mismatch');
  allPassed = false;
}

// Test getProductionHint on Verb
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
if (hint2.step1Mask !== 'δ******' || hint2.grammarClue !== 'Verb: Type A') {
  console.error('FAIL: hint2 mask mismatch');
  allPassed = false;
}

// Test getProductionHint on Sentence with Phonetic Hint
const card3: CardEntry = {
  id: 'A1-U103-010',
  greek: '- Γεια σας! Πού μένετε; - Στην Αθήνα.',
  phonetic_hint: 'YAH sahs! POO MEH-neh-teh? - Steen ah-THEE-nah.',
  english: '- Hello! Where do you live? - In Athens.',
  gender_or_pos: 'phrase',
  audio: null,
  status: 'verified',
  grammatical_info: { part_of_speech: 'phrase' }
};

const hint3 = getProductionHint(card3);
console.log('Hint 3:', hint3);
if (hint3.step1Mask !== '- Γ*** σ**! Π** μ*****; - Σ*** Α****.') {
  console.error(`FAIL: hint3 step1Mask mismatch: got "${hint3.step1Mask}"`);
  allPassed = false;
}
if (hint3.step2Mask !== '- Γε** σα*! Πο* μέ****; - Στ** Αθ***.') {
  console.error(`FAIL: hint3 step2Mask mismatch: got "${hint3.step2Mask}"`);
  allPassed = false;
}
if (hint3.phoneticHint !== 'YAH sahs! POO MEH-neh-teh? - Steen ah-THEE-nah.') {
  console.error(`FAIL: hint3 phoneticHint mismatch`);
  allPassed = false;
}

if (!allPassed) {
  process.exit(1);
} else {
  console.log('All tests passed successfully!');
}

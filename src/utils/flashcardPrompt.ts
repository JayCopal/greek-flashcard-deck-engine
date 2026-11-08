import { CardEntry } from '../types/schema';

/**
 * Sanitizes the English prompt for English -> Greek (EN -> EL) flashcards.
 *
 * Requirements:
 * 1. Strips any parenthetical or bracketed content containing Greek script (e.g. "(διαβάστε)", "(of είμαι)").
 * 2. Strips any stray Greek characters from the prompt.
 * 3. Preserves legitimate English disambiguation hints such as:
 *    - "(male)" / "(female)"
 *    - "(singular)" / "(plural)"
 *    - "(formal)" / "(informal)"
 *    - "(alphabet)" / "(postal)"
 * 4. Cleans double spaces, dangling slashes, and whitespace.
 */
export function sanitizeEnglishPrompt(english: string): string {
  if (!english) return '';

  const greekCharRegex = /[\u0370-\u03ff\u1f00-\u1fff]/;

  // 1. Remove parenthetical segments containing Greek characters
  // e.g. "to read / read! (διαβάστε)" -> "to read / read!"
  // e.g. "you are (2nd person singular of είμαι)" -> "you are (2nd person singular)"
  let result = english.replace(/\(([^)]*)\)/g, (match, inner) => {
    if (!greekCharRegex.test(inner)) {
      return match; // Keep English disambiguation like (male), (female)
    }
    // If the inside has something like "2nd person singular of είμαι", remove only the Greek part ("of είμαι")
    const cleanedInner = inner
      .replace(/\s*(?:of\s+)?[\u0370-\u03ff\u1f00-\u1fff]+/gi, '')
      .trim();

    return cleanedInner.length > 0 ? `(${cleanedInner})` : '';
  });

  // 2. Remove bracketed segments containing Greek characters
  result = result.replace(/\[([^\]]*)\]/g, (match, inner) => {
    if (!greekCharRegex.test(inner)) return match;
    const cleanedInner = inner
      .replace(/\s*(?:of\s+)?[\u0370-\u03ff\u1f00-\u1fff]+/gi, '')
      .trim();
    return cleanedInner.length > 0 ? `[${cleanedInner}]` : '';
  });

  // 3. Strip any stray Greek characters if still present
  if (greekCharRegex.test(result)) {
    result = result.replace(/[\u0370-\u03ff\u1f00-\u1fff]+/g, '').trim();
  }

  // 4. Normalize slashes and redundant whitespace
  result = result
    .replace(/\s*\/\s*/g, ' / ')
    .replace(/\s{2,}/g, ' ')
    .trim();

  // 5. Clean dangling trailing or leading slashes
  result = result.replace(/^\/\s*/, '').replace(/\s*\/$/, '').trim();

  return result || english;
}

export interface ProductionHint {
  step1Mask: string; // e.g. "d*** e***" (1 letter revealed per word)
  step2Mask: string; // e.g. "de** e***" (2 letters revealed per word)
  step3Mask: string; // e.g. "den* e***" (3 letters revealed per word)
  letterClue: string; // backwards compatibility / alias to step1Mask
  articleClue?: string;
  grammarClue?: string;
  phoneticHint?: string;
}

const GREEK_ARTICLES = new Set([
  'ο', 'η', 'το',
  'οι', 'τα',
  'τον', 'την', 'τους', 'τις'
]);

/**
 * Masks Greek or mixed text by revealing a fixed number of initial characters
 * for each word, replacing remaining letters with asterisks (*).
 *
 * Punctuation, symbols, quotes, dashes, numbers, and whitespace are preserved intact.
 *
 * Example:
 * maskGreekText("- Γεια σας, πού μένετε;", 1) => "- Γ*** σ**, π** μ*****;"
 * maskGreekText("- Γεια σας, πού μένετε;", 2) => "- Γε** σα*, πο* μέ****;"
 * maskGreekText("το αεροπλάνο", 1) => "τ* α*********"
 */
export function maskGreekText(text: string, revealCount: number): string {
  if (!text) return '';
  return text.replace(/\p{L}+/gu, (word) => {
    const chars = Array.from(word);
    if (chars.length <= revealCount) {
      return word;
    }
    const revealed = chars.slice(0, revealCount).join('');
    const masked = '*'.repeat(chars.length - revealCount);
    return revealed + masked;
  });
}

/**
 * Computes a non-spoiling, pedagogical 3-step hint for English -> Greek recall.
 *
 * Step 1: Initial letter of each word (e.g. "d*** e***") + grammar classification.
 * Step 2: First two letters of each word (e.g. "de** e***").
 * Step 3: Sounds and guide: Phonetic pronunciation guide (if available) + 3-letter mask.
 */
export function getProductionHint(card: CardEntry): ProductionHint {
  const rawGreek = (card.greek || '').trim();
  const words = rawGreek.split(/\s+/).filter(Boolean);

  let articleClue: string | undefined;
  let grammarClue: string | undefined;

  // Grammar classification
  const gram = card.grammatical_info;
  if (gram && typeof gram === 'object') {
    if (gram.verb_type) {
      grammarClue = `Verb: ${gram.verb_type}`;
    } else if (gram.part_of_speech) {
      grammarClue = `${gram.part_of_speech}`;
    }
  }

  if (!grammarClue && card.gender_or_pos) {
    grammarClue = card.gender_or_pos;
  }

  // Identify leading article only when card is actually a noun
  const isNoun = Boolean(
    card.gender_or_pos?.toLowerCase().includes('noun') ||
    (typeof gram?.part_of_speech === 'string' && gram.part_of_speech.toLowerCase().includes('noun'))
  );
  if (words.length > 1 && GREEK_ARTICLES.has(words[0].toLowerCase()) && isNoun) {
    articleClue = words[0];
  }

  const step1Mask = maskGreekText(rawGreek, 1);
  const step2Mask = maskGreekText(rawGreek, 2);
  const step3Mask = maskGreekText(rawGreek, 3);
  const phoneticHint = (card.phonetic_hint || '').trim() || undefined;

  return {
    step1Mask,
    step2Mask,
    step3Mask,
    letterClue: step1Mask,
    articleClue,
    grammarClue,
    phoneticHint,
  };
}

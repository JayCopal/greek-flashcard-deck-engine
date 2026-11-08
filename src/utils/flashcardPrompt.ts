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
  articleClue?: string;
  letterClue: string;
  grammarClue?: string;
}

const GREEK_ARTICLES = new Set([
  'ο', 'η', 'το',
  'οι', 'τα',
  'τον', 'την', 'τους', 'τις'
]);

/**
 * Computes a non-spoiling, pedagogical hint for English -> Greek recall.
 *
 * Never reveals the full word or full answer. Instead provides:
 * 1. Article clue if the target is a noun with an article (essential for Greek noun learning).
 * 2. First letter and word length (triggers active cognitive retrieval without giving the word away).
 * 3. Grammatical classification (e.g. Type A verb, Neuter noun).
 */
export function getProductionHint(card: CardEntry): ProductionHint {
  const rawGreek = (card.greek || '').trim();
  const words = rawGreek.split(/\s+/).filter(Boolean);

  let articleClue: string | undefined;
  let letterClue = '';
  let grammarClue: string | undefined;

  if (words.length > 1 && GREEK_ARTICLES.has(words[0].toLowerCase())) {
    const article = words[0];
    const noun = words.slice(1).join(' ');
    const firstLetter = noun.charAt(0);
    articleClue = `Article: "${article}"`;
    letterClue = `Noun starts with "${firstLetter}…" (${noun.length} letters)`;
  } else if (rawGreek.length > 0) {
    const firstLetter = rawGreek.charAt(0);
    letterClue = `Starts with "${firstLetter}…" (${rawGreek.length} letters)`;
  }

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

  return {
    articleClue,
    letterClue,
    grammarClue,
  };
}

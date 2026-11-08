import React from 'react';

const TONOS_VOWELS = new Set([
  'ά', 'έ', 'ή', 'ί', 'ό', 'ύ', 'ώ',
  'Ά', 'Έ', 'Ή', 'Ί', 'Ό', 'Ύ', 'Ώ',
  'ΐ', 'ΰ'
]);

/**
 * Highlights accented Greek vowels with subtle emphasis to train syllable stress
 */
export function renderGreekWithTonos(text: string, enabled: boolean = true): React.ReactNode {
  if (!enabled || !text) return text;

  const characters = Array.from(text);
  return (
    <>
      {characters.map((char, index) => {
        if (TONOS_VOWELS.has(char)) {
          return (
            <span
              key={index}
              className="text-amber-300 font-extrabold underline decoration-amber-400/50 underline-offset-4 decoration-2"
              title="Accented vowel (stress mark / τόνος)"
            >
              {char}
            </span>
          );
        }
        return char;
      })}
    </>
  );
}

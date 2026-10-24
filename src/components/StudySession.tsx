import React, { useState, useEffect, useCallback } from 'react';
import { CardEntry } from '../types/schema';
import { AudioPlayer } from './AudioPlayer';
import { 
  ChevronLeft, 
  ChevronRight, 
  RotateCw, 
  Shuffle, 
  ArrowLeft, 
  Volume2, 
  Sparkles,
  Layers
} from 'lucide-react';

interface StudySessionProps {
  cards: CardEntry[];
  title?: string;
  onExit: () => void;
}

export const StudySession: React.FC<StudySessionProps> = ({
  cards: initialCards,
  title = 'Study Drill',
  onExit,
}) => {
  const [cards, setCards] = useState<CardEntry[]>(initialCards);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const [autoPlayAudio, setAutoPlayAudio] = useState(true);

  const currentCard: CardEntry | undefined = cards[currentIndex];

  const handleNext = useCallback(() => {
    setIsFlipped(false);
    setCurrentIndex((prev) => (prev + 1 < cards.length ? prev + 1 : 0));
  }, [cards.length]);

  const handlePrevious = useCallback(() => {
    setIsFlipped(false);
    setCurrentIndex((prev) => (prev - 1 >= 0 ? prev - 1 : cards.length - 1));
  }, [cards.length]);

  const handleFlip = useCallback(() => {
    setIsFlipped((prev) => !prev);
  }, []);

  const handleShuffle = () => {
    const shuffled = [...cards].sort(() => Math.random() - 0.5);
    setCards(shuffled);
    setCurrentIndex(0);
    setIsFlipped(false);
  };

  // Keyboard shortcut listeners
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      // Don't trigger if user is typing in an input
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes((e.target as HTMLElement)?.tagName)) {
        return;
      }

      if (e.code === 'Space') {
        e.preventDefault();
        handleFlip();
      } else if (e.code === 'ArrowRight') {
        e.preventDefault();
        handleNext();
      } else if (e.code === 'ArrowLeft') {
        e.preventDefault();
        handlePrevious();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handleFlip, handleNext, handlePrevious]);

  if (!currentCard || cards.length === 0) {
    return (
      <div className="max-w-md mx-auto text-center py-20 space-y-4">
        <Layers className="w-12 h-12 text-slate-600 mx-auto" />
        <h3 className="text-xl font-bold text-white">No cards to study</h3>
        <p className="text-sm text-slate-400">
          This lesson has no cards yet. Add entries in the Deck Editor first!
        </p>
        <button
          onClick={onExit}
          className="px-4 py-2 rounded-xl bg-sky-500 text-white text-sm font-semibold"
        >
          Back to Dashboard
        </button>
      </div>
    );
  }

  const audioSrc = currentCard.audio ? `/audio/${currentCard.audio}` : null;

  return (
    <div className="max-w-3xl mx-auto space-y-6 pb-20">
      {/* Top Bar */}
      <div className="flex items-center justify-between">
        <button
          onClick={onExit}
          className="inline-flex items-center gap-2 text-sm text-slate-400 hover:text-white transition-colors"
        >
          <ArrowLeft className="w-4 h-4" /> Exit Drill
        </button>
        <div className="flex items-center gap-3">
          <button
            onClick={handleShuffle}
            className="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700 text-xs font-medium flex items-center gap-1.5 transition-all"
            title="Shuffle cards"
          >
            <Shuffle className="w-3.5 h-3.5" /> Shuffle
          </button>
          <button
            onClick={() => setAutoPlayAudio(!autoPlayAudio)}
            className={`px-3 py-1.5 rounded-xl border text-xs font-semibold flex items-center gap-1.5 transition-all ${
              autoPlayAudio
                ? 'bg-sky-500/20 border-sky-500/40 text-sky-400'
                : 'bg-slate-800 border-slate-700 text-slate-400'
            }`}
          >
            <Volume2 className="w-3.5 h-3.5" />
            Auto-Audio: {autoPlayAudio ? 'ON' : 'OFF'}
          </button>
        </div>
      </div>

      {/* Progress Bar & Header */}
      <div className="space-y-2">
        <div className="flex items-center justify-between text-xs font-semibold text-slate-400">
          <span className="truncate max-w-[200px] text-sky-400 font-bold">{title}</span>
          <span>
            Card {currentIndex + 1} of {cards.length}
          </span>
        </div>
        <div className="w-full h-2 bg-slate-800 rounded-full overflow-hidden">
          <div
            className="h-full bg-sky-500 transition-all duration-300 ease-out"
            style={{ width: `${((currentIndex + 1) / cards.length) * 100}%` }}
          />
        </div>
      </div>

      {/* Interactive 3D Flip Flashcard */}
      <div className="perspective-1000 py-4">
        <div
          onClick={handleFlip}
          className={`relative w-full min-h-[380px] sm:min-h-[420px] rounded-3xl cursor-pointer transition-transform duration-500 transform-style-3d select-none shadow-2xl ${
            isFlipped ? 'rotate-y-180' : ''
          }`}
        >
          {/* Card Face (Front - Greek Prompt) */}
          <div className="absolute inset-0 w-full h-full rounded-3xl p-8 sm:p-12 flex flex-col justify-between backface-hidden glass-card border border-sky-500/20 shadow-sky-500/5">
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold uppercase tracking-wider text-sky-400/80 flex items-center gap-1.5">
                <Sparkles className="w-3.5 h-3.5" /> Greek Prompt
              </span>
              {currentCard.gender_or_pos && (
                <span className="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-800/90 text-sky-300 border border-slate-700">
                  {currentCard.gender_or_pos}
                </span>
              )}
            </div>

            {/* Greek Text */}
            <div className="text-center py-8 space-y-4">
              <h2 className="text-4xl sm:text-5xl md:text-6xl font-extrabold text-white tracking-wide font-serif leading-tight">
                {currentCard.greek}
              </h2>

              {/* Native Audio Trigger */}
              <div 
                className="inline-block mt-4"
                onClick={(e) => e.stopPropagation()}
              >
                <AudioPlayer
                  src={audioSrc}
                  autoPlay={autoPlayAudio}
                  mini
                />
              </div>
            </div>

            <div className="flex items-center justify-between text-xs text-slate-500 border-t border-slate-700/40 pt-4">
              <span>Press <kbd className="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-slate-400">Space</kbd> or click to reveal</span>
              <span>Front</span>
            </div>
          </div>

          {/* Card Back (Reveal - English & Notes) */}
          <div className="absolute inset-0 w-full h-full rounded-3xl p-8 sm:p-12 flex flex-col justify-between backface-hidden rotate-y-180 glass-card border border-teal-500/30 bg-slate-900 shadow-teal-500/5">
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold uppercase tracking-wider text-teal-400 flex items-center gap-1.5">
                <Sparkles className="w-3.5 h-3.5" /> English Meaning
              </span>
              <span className="text-xs font-mono text-slate-400">
                {currentCard.greek}
              </span>
            </div>

            {/* English & Phonetics */}
            <div className="text-center py-6 space-y-4">
              <h3 className="text-3xl sm:text-4xl font-bold text-white tracking-tight">
                {currentCard.english}
              </h3>

              {currentCard.phonetic_hint && (
                <div className="inline-block px-3 py-1 rounded-lg bg-slate-800/80 border border-slate-700 text-sm font-mono text-teal-300">
                  /{currentCard.phonetic_hint}/
                </div>
              )}

              {currentCard.notes && (
                <p className="text-sm text-slate-300 max-w-md mx-auto italic mt-2 bg-slate-800/40 p-3 rounded-xl border border-slate-700/50">
                  {currentCard.notes}
                </p>
              )}
            </div>

            <div className="flex items-center justify-between text-xs text-slate-500 border-t border-slate-700/40 pt-4">
              <span>Press <kbd className="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-slate-400">Space</kbd> to flip back</span>
              <span>Back</span>
            </div>
          </div>
        </div>
      </div>

      {/* Navigation Buttons */}
      <div className="flex items-center justify-between pt-2">
        <button
          onClick={handlePrevious}
          className="inline-flex items-center gap-2 px-5 py-3 rounded-2xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold text-sm transition-all hover:scale-105 active:scale-95"
        >
          <ChevronLeft className="w-4 h-4" /> Previous
        </button>

        <button
          onClick={handleFlip}
          className="inline-flex items-center gap-2 px-6 py-3 rounded-2xl bg-slate-800/90 hover:bg-slate-700 text-sky-400 border border-sky-500/20 font-semibold text-sm transition-all hover:scale-105 active:scale-95"
        >
          <RotateCw className="w-4 h-4" /> Flip Card
        </button>

        <button
          onClick={handleNext}
          className="inline-flex items-center gap-2 px-6 py-3 rounded-2xl bg-sky-500 hover:bg-sky-400 text-white font-semibold text-sm shadow-lg shadow-sky-500/20 transition-all hover:scale-105 active:scale-95"
        >
          Next <ChevronRight className="w-4 h-4" />
        </button>
      </div>

      {/* Keyboard Shortcuts Hint */}
      <div className="text-center text-xs text-slate-500 space-x-4 pt-2">
        <span><kbd className="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700">Space</kbd> Flip</span>
        <span><kbd className="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700">←</kbd> Prev</span>
        <span><kbd className="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700">→</kbd> Next</span>
      </div>
    </div>
  );
};

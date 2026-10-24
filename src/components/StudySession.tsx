import { useState, useEffect, useCallback, useRef } from 'react';
import { CardEntry, SRSRating } from '../types/schema';
import { AudioPlayer, AudioPlayerHandle } from './AudioPlayer';
import { 
  getCardSRS, 
  toggleCardLearned, 
  recordSRSRating, 
  filterStudyCards, 
  getAllSRSData 
} from '../utils/srs';
import { 
  ChevronLeft, 
  ChevronRight, 
  RotateCw, 
  Shuffle, 
  ArrowLeft, 
  Volume2, 
  Sparkles,
  CheckCircle,
  EyeOff,
  Clock,
  ArrowUpDown,
  Award,
  FileText
} from 'lucide-react';

type StudyDirection = 'greek_to_english' | 'english_to_greek';

interface StudySessionProps {
  cards: CardEntry[];
  title?: string;
  lessonNotes?: string;
  onExit: () => void;
}

export const StudySession: React.FC<StudySessionProps> = ({
  cards: initialCards,
  title = 'Study Drill',
  lessonNotes,
  onExit,
}) => {
  // Study configuration options
  const [studyDirection, setStudyDirection] = useState<StudyDirection>('greek_to_english');
  const [hideLearned, setHideLearned] = useState<boolean>(true);
  const [dueOnly, setDueOnly] = useState<boolean>(false);
  const [autoPlayAudio, setAutoPlayAudio] = useState<boolean>(false); // Default is OFF as requested
  const [showNotes, setShowNotes] = useState<boolean>(false);

  // Active cards filtered by learned/due status
  const [filteredCards, setFilteredCards] = useState<CardEntry[]>(() =>
    filterStudyCards(initialCards, { hideLearned: true, dueOnly: false })
  );

  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);

  // Audio player ref for imperative play on Down Arrow
  const audioPlayerRef = useRef<AudioPlayerHandle | null>(null);

  // Re-filter cards whenever settings or master list changes
  const applyFilter = useCallback(
    (customHideLearned = hideLearned, customDueOnly = dueOnly) => {
      const updated = filterStudyCards(initialCards, {
        hideLearned: customHideLearned,
        dueOnly: customDueOnly,
      });
      setFilteredCards(updated);
      setCurrentIndex((prev) => (prev < updated.length ? prev : 0));
      setIsFlipped(false);
    },
    [initialCards, hideLearned, dueOnly]
  );

  const currentCard: CardEntry | undefined = filteredCards[currentIndex];
  const srsData = currentCard ? getCardSRS(currentCard.id) : null;

  const handleNext = useCallback(() => {
    setIsFlipped(false);
    setCurrentIndex((prev) => (prev + 1 < filteredCards.length ? prev + 1 : 0));
  }, [filteredCards.length]);

  const handlePrevious = useCallback(() => {
    setIsFlipped(false);
    setCurrentIndex((prev) => (prev - 1 >= 0 ? prev - 1 : filteredCards.length - 1));
  }, [filteredCards.length]);

  const handleFlip = useCallback(() => {
    setIsFlipped((prev) => !prev);
  }, []);

  const handlePlayAudio = useCallback(() => {
    audioPlayerRef.current?.playAudio();
  }, []);

  const handleShuffle = () => {
    const shuffled = [...filteredCards].sort(() => Math.random() - 0.5);
    setFilteredCards(shuffled);
    setCurrentIndex(0);
    setIsFlipped(false);
  };

  // Toggle "Learned" on current card
  const handleToggleLearned = useCallback(() => {
    if (!currentCard) return;
    const isNowLearned = toggleCardLearned(currentCard.id);

    if (hideLearned && isNowLearned) {
      // Remove from active list
      applyFilter(hideLearned, dueOnly);
    } else {
      // Force re-render to update badge
      setFilteredCards((prev) => [...prev]);
    }
  }, [currentCard, hideLearned, dueOnly, applyFilter]);

  // Rate card with SRS rating (Again, Hard, Good, Easy)
  const handleRateSRS = useCallback(
    (rating: SRSRating) => {
      if (!currentCard) return;
      recordSRSRating(currentCard.id, rating);
      if (dueOnly) {
        applyFilter(hideLearned, dueOnly);
      } else {
        handleNext();
      }
    },
    [currentCard, dueOnly, hideLearned, applyFilter, handleNext]
  );

  // Keyboard navigation shortcuts
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      // Ignore if user is inside an input/textarea
      if (['INPUT', 'TEXTAREA', 'SELECT'].includes((e.target as HTMLElement)?.tagName)) {
        return;
      }

      if (e.code === 'ArrowUp') {
        e.preventDefault();
        handleFlip(); // UP ARROW: FLIP CARD
      } else if (e.code === 'ArrowDown') {
        e.preventDefault();
        handlePlayAudio(); // DOWN ARROW: PLAY NATIVE AUDIO
      } else if (e.code === 'ArrowRight') {
        e.preventDefault();
        handleNext(); // RIGHT ARROW: NEXT
      } else if (e.code === 'ArrowLeft') {
        e.preventDefault();
        handlePrevious(); // LEFT ARROW: PREVIOUS
      } else if (e.key === '1') {
        e.preventDefault();
        handleRateSRS('again');
      } else if (e.key === '2') {
        e.preventDefault();
        handleRateSRS('hard');
      } else if (e.key === '3') {
        e.preventDefault();
        handleRateSRS('good');
      } else if (e.key === '4') {
        e.preventDefault();
        handleRateSRS('easy');
      } else if (e.code === 'KeyM') {
        e.preventDefault();
        handleToggleLearned(); // 'M': TOGGLE LEARNED
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handleFlip, handlePlayAudio, handleNext, handlePrevious, handleRateSRS, handleToggleLearned]);

  // Count how many total cards are learned
  const allSRS = getAllSRSData();
  const totalLearnedCount = initialCards.filter((c) => allSRS[c.id]?.isLearned).length;

  if (!currentCard || filteredCards.length === 0) {
    return (
      <div className="max-w-md mx-auto text-center py-20 space-y-5">
        <div className="w-16 h-16 rounded-3xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 flex items-center justify-center mx-auto shadow-xl shadow-emerald-500/10">
          <Award className="w-8 h-8" />
        </div>
        <h3 className="text-2xl font-extrabold text-white">All Active Cards Completed!</h3>
        <p className="text-sm text-slate-400 max-w-sm mx-auto">
          {hideLearned && totalLearnedCount > 0
            ? `You have marked ${totalLearnedCount} of ${initialCards.length} cards as learned. Uncheck "Hide Learned" below to review them.`
            : 'No cards match your current filter settings.'}
        </p>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-3 pt-2">
          {hideLearned && (
            <button
              onClick={() => {
                setHideLearned(false);
                applyFilter(false, dueOnly);
              }}
              className="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold"
            >
              Show Learned Cards ({totalLearnedCount})
            </button>
          )}
          <button
            onClick={onExit}
            className="px-5 py-2.5 rounded-xl bg-sky-500 hover:bg-sky-400 text-white text-xs font-semibold shadow-md shadow-sky-500/25"
          >
            Back to Dashboard
          </button>
        </div>
      </div>
    );
  }

  const audioSrc = currentCard.audio ? `/audio/${currentCard.audio}` : null;

  return (
    <div className="max-w-3xl mx-auto space-y-6 pb-20">
      {/* Top Header & Settings Bar */}
      <div className="glass-panel p-4 rounded-2xl flex flex-col md:flex-row md:items-center justify-between gap-4">
        {/* Back and Title */}
        <div className="flex items-center gap-3">
          <button
            onClick={onExit}
            className="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white transition-colors border border-slate-700"
            title="Exit Drill"
          >
            <ArrowLeft className="w-4 h-4" />
          </button>
          <div>
            <span className="text-[10px] uppercase font-bold text-sky-400 tracking-wider">
              {title}
            </span>
            <div className="text-xs text-slate-400">
              Card {currentIndex + 1} of {filteredCards.length}
              {totalLearnedCount > 0 && (
                <span className="text-emerald-400 ml-2 font-medium">
                  ({totalLearnedCount} learned)
                </span>
              )}
            </div>
          </div>
        </div>

        {/* Filter & Direction Controls */}
        <div className="flex flex-wrap items-center gap-2">
          {/* Study Direction Toggle: Greek -> English vs English -> Greek */}
          <button
            type="button"
            onClick={() => {
              setStudyDirection((prev) =>
                prev === 'greek_to_english' ? 'english_to_greek' : 'greek_to_english'
              );
              setIsFlipped(false);
            }}
            className="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-semibold text-slate-200 flex items-center gap-1.5 transition-all"
            title="Switch prompt direction"
          >
            <ArrowUpDown className="w-3.5 h-3.5 text-sky-400" />
            <span>
              {studyDirection === 'greek_to_english' ? 'Greek → English' : 'English → Greek'}
            </span>
          </button>

          {/* Hide Learned Toggle */}
          <button
            type="button"
            onClick={() => {
              const nextVal = !hideLearned;
              setHideLearned(nextVal);
              applyFilter(nextVal, dueOnly);
            }}
            className={`px-3 py-1.5 rounded-xl border text-xs font-semibold flex items-center gap-1.5 transition-all ${
              hideLearned
                ? 'bg-emerald-950/80 border-emerald-500/40 text-emerald-400'
                : 'bg-slate-800 border-slate-700 text-slate-400 hover:text-white'
            }`}
            title="Hide cards that you've already mastered"
          >
            <EyeOff className="w-3.5 h-3.5" />
            <span>Hide Learned</span>
          </button>

          {/* Due Only (SRS) Toggle */}
          <button
            type="button"
            onClick={() => {
              const nextVal = !dueOnly;
              setDueOnly(nextVal);
              applyFilter(hideLearned, nextVal);
            }}
            className={`px-3 py-1.5 rounded-xl border text-xs font-semibold flex items-center gap-1.5 transition-all ${
              dueOnly
                ? 'bg-amber-950/80 border-amber-500/40 text-amber-400'
                : 'bg-slate-800 border-slate-700 text-slate-400 hover:text-white'
            }`}
            title="Filter by Spaced Repetition due date"
          >
            <Clock className="w-3.5 h-3.5" />
            <span>SRS Due Only</span>
          </button>

          {/* Auto-audio Toggle (default OFF) */}
          <button
            type="button"
            onClick={() => setAutoPlayAudio(!autoPlayAudio)}
            className={`p-2 rounded-xl border text-xs font-semibold flex items-center transition-all ${
              autoPlayAudio
                ? 'bg-sky-500/20 border-sky-500/40 text-sky-400'
                : 'bg-slate-800 border-slate-700 text-slate-500 hover:text-slate-300'
            }`}
            title={`Auto-play audio: ${autoPlayAudio ? 'ON' : 'OFF'}`}
          >
            <Volume2 className="w-4 h-4" />
          </button>

          {/* Notes Toggle Button if notes exist */}
          {lessonNotes && (
            <button
              type="button"
              onClick={() => setShowNotes(!showNotes)}
              className={`px-3 py-1.5 rounded-xl border text-xs font-semibold flex items-center gap-1.5 transition-all ${
                showNotes
                  ? 'bg-sky-500 text-white border-sky-400 shadow-md shadow-sky-500/30'
                  : 'bg-slate-800 text-sky-400 border-slate-700 hover:text-white'
              }`}
              title="Toggle lesson grammar notes"
            >
              <FileText className="w-3.5 h-3.5" />
              <span>Notes</span>
            </button>
          )}

          {/* Shuffle button */}
          <button
            type="button"
            onClick={handleShuffle}
            className="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white border border-slate-700 transition-all"
            title="Shuffle deck"
          >
            <Shuffle className="w-4 h-4" />
          </button>
        </div>
      </div>

      {/* Collapsible Lesson Notes Banner */}
      {showNotes && lessonNotes && (
        <div className="p-4 rounded-2xl bg-sky-950/40 border border-sky-500/30 text-sky-100 text-sm whitespace-pre-line leading-relaxed shadow-lg">
          <div className="flex items-center justify-between pb-2 mb-2 border-b border-sky-500/20 text-xs font-bold text-sky-300">
            <span className="flex items-center gap-1.5">
              <FileText className="w-4 h-4" /> Lesson Notes & Grammar Context
            </span>
            <button 
              onClick={() => setShowNotes(false)} 
              className="text-sky-400 hover:text-white text-xs px-2 py-0.5 rounded bg-sky-900/60"
            >
              Close
            </button>
          </div>
          {lessonNotes}
        </div>
      )}

      {/* Progress Bar */}
      <div className="w-full h-2 bg-slate-800 rounded-full overflow-hidden">
        <div
          className="h-full bg-sky-500 transition-all duration-300 ease-out"
          style={{ width: `${((currentIndex + 1) / filteredCards.length) * 100}%` }}
        />
      </div>

      {/* 3D Flashcard Flip Container */}
      <div className="perspective-1000 py-2">
        <div
          onClick={handleFlip}
          className={`relative w-full min-h-[380px] sm:min-h-[420px] rounded-3xl cursor-pointer transition-transform duration-500 transform-style-3d select-none shadow-2xl ${
            isFlipped ? 'rotate-y-180' : ''
          }`}
        >
          {/* ================= CARD FRONT ================= */}
          <div className="absolute inset-0 w-full h-full rounded-3xl p-8 sm:p-12 flex flex-col justify-between backface-hidden glass-card border border-sky-500/20 shadow-sky-500/5">
            {/* Top Bar on Front */}
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold uppercase tracking-wider text-sky-400/80 flex items-center gap-1.5">
                <Sparkles className="w-3.5 h-3.5" />
                {studyDirection === 'greek_to_english' ? 'Greek Prompt' : 'English Prompt (Recall Greek)'}
              </span>

              <div className="flex items-center gap-2">
                {currentCard.gender_or_pos && (
                  <span className="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-800/90 text-sky-300 border border-slate-700">
                    {currentCard.gender_or_pos}
                  </span>
                )}
                {srsData?.isLearned && (
                  <span className="text-xs font-semibold px-2.5 py-1 rounded-full bg-emerald-950/90 text-emerald-400 border border-emerald-800 flex items-center gap-1">
                    <CheckCircle className="w-3 h-3" /> Learned
                  </span>
                )}
              </div>
            </div>

            {/* Prompt Content */}
            <div className="text-center py-6 space-y-4">
              {studyDirection === 'greek_to_english' ? (
                <>
                  <h2 className="text-4xl sm:text-5xl md:text-6xl font-extrabold text-white tracking-wide font-serif leading-tight">
                    {currentCard.greek}
                  </h2>
                  <div className="inline-block mt-3" onClick={(e) => e.stopPropagation()}>
                    <AudioPlayer
                      ref={audioPlayerRef}
                      src={audioSrc}
                      autoPlay={autoPlayAudio}
                      mini
                    />
                  </div>
                </>
              ) : (
                <>
                  <h2 className="text-3xl sm:text-4xl md:text-5xl font-bold text-white tracking-tight leading-tight">
                    {currentCard.english}
                  </h2>
                  {currentCard.notes && (
                    <p className="text-xs text-slate-400 max-w-md mx-auto italic mt-2">
                      Hint: {currentCard.notes}
                    </p>
                  )}
                </>
              )}
            </div>

            {/* Bottom info on Front */}
            <div className="flex items-center justify-between text-xs text-slate-500 border-t border-slate-700/40 pt-4">
              <span>
                Press <kbd className="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-sky-400 font-bold">↑ Up</kbd> or click to flip
              </span>
              <span>
                Audio: <kbd className="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-sky-400 font-bold">↓ Down</kbd>
              </span>
            </div>
          </div>

          {/* ================= CARD BACK (REVEAL) ================= */}
          <div className="absolute inset-0 w-full h-full rounded-3xl p-8 sm:p-12 flex flex-col justify-between backface-hidden rotate-y-180 glass-card border border-teal-500/30 bg-slate-900 shadow-teal-500/5">
            {/* Top Bar on Back */}
            <div className="flex items-center justify-between">
              <span className="text-xs font-bold uppercase tracking-wider text-teal-400 flex items-center gap-1.5">
                <Sparkles className="w-3.5 h-3.5" /> Answer & Pronunciation
              </span>

              <div className="flex items-center gap-2" onClick={(e) => e.stopPropagation()}>
                <button
                  type="button"
                  onClick={handleToggleLearned}
                  className={`px-3 py-1 rounded-full text-xs font-semibold flex items-center gap-1.5 border transition-all ${
                    srsData?.isLearned
                      ? 'bg-emerald-600 border-emerald-500 text-white shadow-md shadow-emerald-600/30'
                      : 'bg-slate-800 border-slate-700 text-slate-300 hover:text-emerald-400'
                  }`}
                  title="Mark as learned to prevent showing again (Shortcut: M)"
                >
                  <CheckCircle className="w-3.5 h-3.5" />
                  <span>{srsData?.isLearned ? 'Learned (M)' : 'Mark Learned (M)'}</span>
                </button>
              </div>
            </div>

            {/* Answer Content */}
            <div className="text-center py-4 space-y-4">
              {studyDirection === 'greek_to_english' ? (
                <>
                  <h3 className="text-3xl sm:text-4xl font-bold text-white tracking-tight">
                    {currentCard.english}
                  </h3>
                  {currentCard.phonetic_hint && (
                    <div className="inline-block px-3 py-1 rounded-lg bg-slate-800/80 border border-slate-700 text-sm font-mono text-teal-300">
                      /{currentCard.phonetic_hint}/
                    </div>
                  )}
                  {currentCard.notes && (
                    <p className="text-sm text-slate-300 max-w-md mx-auto italic mt-1 bg-slate-800/40 p-3 rounded-xl border border-slate-700/50">
                      {currentCard.notes}
                    </p>
                  )}
                </>
              ) : (
                <>
                  <h2 className="text-4xl sm:text-5xl font-extrabold text-white tracking-wide font-serif leading-tight">
                    {currentCard.greek}
                  </h2>
                  {currentCard.phonetic_hint && (
                    <div className="inline-block px-3 py-1 rounded-lg bg-slate-800/80 border border-slate-700 text-sm font-mono text-teal-300">
                      /{currentCard.phonetic_hint}/
                    </div>
                  )}
                  <div className="inline-block mt-2" onClick={(e) => e.stopPropagation()}>
                    <AudioPlayer
                      ref={audioPlayerRef}
                      src={audioSrc}
                      autoPlay={autoPlayAudio}
                      mini
                    />
                  </div>
                  {currentCard.notes && (
                    <p className="text-sm text-slate-300 max-w-md mx-auto italic mt-1 bg-slate-800/40 p-3 rounded-xl border border-slate-700/50">
                      {currentCard.notes}
                    </p>
                  )}
                </>
              )}
            </div>

            {/* Spaced Repetition Rating Buttons */}
            <div 
              className="border-t border-slate-700/40 pt-4"
              onClick={(e) => e.stopPropagation()}
            >
              <div className="grid grid-cols-4 gap-2">
                <button
                  type="button"
                  onClick={() => handleRateSRS('again')}
                  className="py-2 px-1 rounded-xl bg-rose-950/80 hover:bg-rose-900 border border-rose-500/40 text-rose-300 text-xs font-semibold transition-all text-center"
                  title="Repeat soon (1)"
                >
                  <div className="font-bold">Again</div>
                  <div className="text-[10px] text-rose-400/80 mt-0.5">1d • [1]</div>
                </button>

                <button
                  type="button"
                  onClick={() => handleRateSRS('hard')}
                  className="py-2 px-1 rounded-xl bg-amber-950/80 hover:bg-amber-900 border border-amber-500/40 text-amber-300 text-xs font-semibold transition-all text-center"
                  title="Challenging (2)"
                >
                  <div className="font-bold">Hard</div>
                  <div className="text-[10px] text-amber-400/80 mt-0.5">+20% • [2]</div>
                </button>

                <button
                  type="button"
                  onClick={() => handleRateSRS('good')}
                  className="py-2 px-1 rounded-xl bg-sky-950/80 hover:bg-sky-900 border border-sky-500/40 text-sky-300 text-xs font-semibold transition-all text-center"
                  title="Correct recall (3)"
                >
                  <div className="font-bold">Good</div>
                  <div className="text-[10px] text-sky-400/80 mt-0.5">{srsData?.intervalDays ? `${srsData.intervalDays * 2}d` : '3d'} • [3]</div>
                </button>

                <button
                  type="button"
                  onClick={() => handleRateSRS('easy')}
                  className="py-2 px-1 rounded-xl bg-emerald-950/80 hover:bg-emerald-900 border border-emerald-500/40 text-emerald-300 text-xs font-semibold transition-all text-center"
                  title="Effortless recall (4)"
                >
                  <div className="font-bold">Easy</div>
                  <div className="text-[10px] text-emerald-400/80 mt-0.5">{srsData?.intervalDays ? `${srsData.intervalDays * 3}d` : '5d'} • [4]</div>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Navigation & Action Controls */}
      <div className="flex items-center justify-between pt-2">
        <button
          onClick={handlePrevious}
          className="inline-flex items-center gap-2 px-5 py-3 rounded-2xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold text-sm transition-all hover:scale-105 active:scale-95"
          title="Previous card (← Left Arrow)"
        >
          <ChevronLeft className="w-4 h-4" /> Previous
        </button>

        <div className="flex items-center gap-2">
          {/* Flip button */}
          <button
            onClick={handleFlip}
            className="inline-flex items-center gap-2 px-5 py-3 rounded-2xl bg-slate-800 hover:bg-slate-700 text-sky-400 border border-sky-500/20 font-semibold text-sm transition-all hover:scale-105 active:scale-95"
            title="Flip Card (↑ Up Arrow)"
          >
            <RotateCw className="w-4 h-4" /> Flip [↑]
          </button>

          {/* Audio trigger button */}
          <button
            onClick={handlePlayAudio}
            className="inline-flex items-center gap-2 px-4 py-3 rounded-2xl bg-slate-800 hover:bg-slate-700 text-sky-300 border border-slate-700 font-semibold text-sm transition-all hover:scale-105 active:scale-95"
            title="Play Audio (↓ Down Arrow)"
          >
            <Volume2 className="w-4 h-4" /> [↓]
          </button>
        </div>

        <button
          onClick={handleNext}
          className="inline-flex items-center gap-2 px-6 py-3 rounded-2xl bg-sky-500 hover:bg-sky-400 text-white font-semibold text-sm shadow-lg shadow-sky-500/20 transition-all hover:scale-105 active:scale-95"
          title="Next card (→ Right Arrow)"
        >
          Next <ChevronRight className="w-4 h-4" />
        </button>
      </div>

      {/* Keyboard Shortcuts Hint Bar */}
      <div className="p-3 rounded-xl bg-slate-900/60 border border-slate-800 text-center text-xs text-slate-400 flex flex-wrap items-center justify-center gap-x-4 gap-y-1">
        <span><kbd className="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-white font-semibold">↑</kbd> Flip Card</span>
        <span><kbd className="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-white font-semibold">↓</kbd> Play Audio</span>
        <span><kbd className="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-white font-semibold">←</kbd> / <kbd className="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-white font-semibold">→</kbd> Prev / Next</span>
        <span><kbd className="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-white font-semibold">M</kbd> Mark Learned</span>
        <span><kbd className="px-1.5 py-0.5 rounded bg-slate-800 border border-slate-700 text-white font-semibold">1-4</kbd> SRS Rating</span>
      </div>
    </div>
  );
};

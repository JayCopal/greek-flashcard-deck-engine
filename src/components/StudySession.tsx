import { useState, useEffect, useCallback, useRef } from 'react';
import { CardEntry, SRSRating } from '../types/schema';
import { 
  getActiveUser, 
  getActiveUserId, 
  getUserStudyPreferences, 
  setUserStudyPreferences 
} from '../utils/userStorage';
import { 
  getCardSRS, 
  toggleCardLearned, 
  toggleCardExcluded,
  recordSRSRating, 
  filterStudyCards, 
  getAllSRSData,
  RatingFilterOption,
  getCardRatingStatus
} from '../utils/srs';
import { 
  ChevronLeft, 
  ChevronRight, 
  RotateCw, 
  Shuffle, 
  ArrowLeft, 
  Volume2, 
  VolumeX,
  Pause,
  CheckCircle, 
  EyeOff, 
  Clock, 
  ArrowUpDown, 
  Award, 
  FileText, 
  Ban, 
  Filter,
  HelpCircle
} from 'lucide-react';

type StudyDirection = 'greek_to_english' | 'english_to_greek';

interface StudySessionProps {
  cards: CardEntry[];
  title?: string;
  lessonNotes?: string;
  lessonNumber?: string;
  initialHideExcluded?: boolean;
  initialHideLearned?: boolean;
  onExit: () => void;
  onOpenHelp?: () => void;
}

export const StudySession: React.FC<StudySessionProps> = ({
  cards: initialCards,
  title = 'Study Drill',
  lessonNotes,
  lessonNumber,
  initialHideExcluded,
  initialHideLearned,
  onExit,
  onOpenHelp,
}) => {
  const [activeUser, setActiveUser] = useState(getActiveUser());
  const userPrefs = getUserStudyPreferences(activeUser.id);

  const isAllIgnored = initialCards.length > 0 && initialCards.every((c) => {
    const s = getAllSRSData(getActiveUserId())[c.id];
    return s?.isExcluded;
  });

  const resolvedHideExcluded = initialHideExcluded !== undefined 
    ? initialHideExcluded 
    : (isAllIgnored ? false : userPrefs.hideExcluded);

  const resolvedHideLearned = initialHideLearned !== undefined 
    ? initialHideLearned 
    : userPrefs.hideLearned;

  // Study configuration options
  const [studyDirection, setStudyDirection] = useState<StudyDirection>('greek_to_english');
  const [hideLearned, setHideLearned] = useState<boolean>(resolvedHideLearned);
  const [hideExcluded, setHideExcluded] = useState<boolean>(resolvedHideExcluded);
  const [dueOnly, setDueOnly] = useState<boolean>(false);
  const [ratingFilter, setRatingFilter] = useState<RatingFilterOption>('all');
  const [autoPlayAudio, setAutoPlayAudio] = useState<boolean>(true); // Default is ON as requested
  const [showNotes, setShowNotes] = useState<boolean>(false);

  // Active cards filtered by learned/excluded/due/rating status
  const [filteredCards, setFilteredCards] = useState<CardEntry[]>(() =>
    filterStudyCards(initialCards, { 
      hideLearned: resolvedHideLearned, 
      dueOnly: false, 
      hideExcluded: resolvedHideExcluded,
      ratingFilter: 'all'
    }, getActiveUserId())
  );

  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);

  // Centralized single HTMLAudioElement ref and playback state
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [isAudioPlaying, setIsAudioPlaying] = useState<boolean>(false);

  // Re-filter cards whenever settings or master list changes
  const applyFilter = useCallback(
    (
      customHideLearned = hideLearned, 
      customDueOnly = dueOnly, 
      customHideExcluded = hideExcluded,
      customRatingFilter = ratingFilter
    ) => {
      const updated = filterStudyCards(initialCards, {
        hideLearned: customHideLearned,
        dueOnly: customDueOnly,
        hideExcluded: customHideExcluded,
        ratingFilter: customRatingFilter,
      }, activeUser.id);
      setFilteredCards(updated);
      setCurrentIndex((prev) => (updated.length === 0 ? 0 : Math.min(prev, updated.length - 1)));
      setIsFlipped(false);
    },
    [initialCards, hideLearned, dueOnly, hideExcluded, ratingFilter, activeUser.id]
  );

  useEffect(() => {
    const handleUserChange = () => {
      const user = getActiveUser();
      setActiveUser(user);
      const prefs = getUserStudyPreferences(user.id);
      setHideLearned(prefs.hideLearned);
      setHideExcluded(prefs.hideExcluded);
      applyFilter(prefs.hideLearned, dueOnly, prefs.hideExcluded, ratingFilter);
    };
    window.addEventListener('greek_deck_user_change', handleUserChange);
    return () => {
      window.removeEventListener('greek_deck_user_change', handleUserChange);
    };
  }, [applyFilter, dueOnly, ratingFilter]);

  const currentCard: CardEntry | undefined = filteredCards[currentIndex];
  const srsData = currentCard ? getCardSRS(currentCard.id, activeUser.id) : null;
  const ratingStatus = currentCard ? getCardRatingStatus(srsData || undefined) : null;

  // Helper to extract lesson label from card ID (e.g., A1-U01-001 -> "Lesson 1", A1-U101-001 -> "Lesson 101", A1-U105B-001 -> "Lesson 105B")
  const getCardLessonLabel = (card?: CardEntry): string | null => {
    if (!card?.id) return null;
    const match = card.id.match(/U(\d+[A-Za-z]?)/i);
    if (match) {
      const code = match[1].toUpperCase();
      const numMatch = code.match(/^0*(\d+)([A-Za-z]?)$/);
      if (numMatch) {
        return `Lesson ${numMatch[1]}${numMatch[2]}`;
      }
      return `Lesson ${code}`;
    }
    return null;
  };

  const formatLessonLabel = (val?: string): string | null => {
    if (!val) return null;
    if (val.toLowerCase().startsWith('lesson')) return val;
    return `Lesson ${val}`;
  };

  const displayLessonLabel =
    formatLessonLabel(lessonNumber) ||
    (currentCard ? getCardLessonLabel(currentCard) : null) ||
    'Lesson 1';

  const baseUrl = import.meta.env.BASE_URL.endsWith('/')
    ? import.meta.env.BASE_URL
    : `${import.meta.env.BASE_URL}/`;
  const audioSrc = currentCard?.audio ? `${baseUrl}audio/${currentCard.audio}` : null;

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
    // Anytime a card is flipped, play the native audio
    if (audioRef.current && audioSrc) {
      audioRef.current.currentTime = 0;
      audioRef.current.play().catch(() => {});
    }
  }, [audioSrc]);

  const handlePlayAudio = useCallback(() => {
    if (!audioRef.current || !audioSrc) return;
    if (audioRef.current.paused) {
      audioRef.current.currentTime = 0;
      audioRef.current.play().catch(() => {});
    } else {
      audioRef.current.pause();
    }
  }, [audioSrc]);

  // Single-source audio playback controller: stop previous and auto-play new card once
  useEffect(() => {
    if (audioRef.current) {
      audioRef.current.pause();
      audioRef.current.currentTime = 0;
    }
    setIsAudioPlaying(false);

    // If auto-play is enabled and we are showing Greek on the front (greek_to_english), play once
    if (autoPlayAudio && studyDirection === 'greek_to_english' && audioSrc) {
      const timer = setTimeout(() => {
        if (audioRef.current) {
          audioRef.current.currentTime = 0;
          audioRef.current.play().catch(() => {});
        }
      }, 50);
      return () => clearTimeout(timer);
    }
  }, [currentIndex, currentCard?.id, autoPlayAudio, studyDirection, audioSrc]);

  const handleShuffle = () => {
    const shuffled = [...filteredCards].sort(() => Math.random() - 0.5);
    setFilteredCards(shuffled);
    setCurrentIndex(0);
    setIsFlipped(false);
  };

  // Toggle "Learned" on current card
  const handleToggleLearned = useCallback(() => {
    if (!currentCard) return;
    const isNowLearned = toggleCardLearned(currentCard.id, activeUser.id);

    if (hideLearned && isNowLearned) {
      const updated = filterStudyCards(initialCards, {
        hideLearned,
        dueOnly,
        hideExcluded,
        ratingFilter,
      }, activeUser.id);
      setFilteredCards(updated);
      setCurrentIndex((prev) => (updated.length === 0 ? 0 : Math.min(prev, updated.length - 1)));
    } else {
      // Force re-render to update badge immediately
      setFilteredCards((prev) => [...prev]);
    }
  }, [currentCard, hideLearned, dueOnly, hideExcluded, ratingFilter, initialCards, activeUser.id]);

  // Toggle "Don't Learn" (Exclude) on current card
  const handleToggleExcluded = useCallback(() => {
    if (!currentCard) return;
    const isNowExcluded = toggleCardExcluded(currentCard.id, activeUser.id);

    if (hideExcluded && isNowExcluded) {
      const updated = filterStudyCards(initialCards, {
        hideLearned,
        dueOnly,
        hideExcluded,
        ratingFilter,
      }, activeUser.id);
      setFilteredCards(updated);
      setCurrentIndex((prev) => (updated.length === 0 ? 0 : Math.min(prev, updated.length - 1)));
    } else {
      setFilteredCards((prev) => [...prev]);
    }
  }, [currentCard, hideExcluded, hideLearned, dueOnly, ratingFilter, initialCards, activeUser.id]);

  // Rate card with SRS rating (Again, Hard, Good, Easy)
  const handleRateSRS = useCallback(
    (rating: SRSRating) => {
      if (!currentCard) return;
      recordSRSRating(currentCard.id, rating, activeUser.id);
      if (dueOnly || ratingFilter !== 'all') {
        const updated = filterStudyCards(initialCards, {
          hideLearned,
          dueOnly,
          hideExcluded,
          ratingFilter,
        }, activeUser.id);
        setFilteredCards(updated);
        setCurrentIndex((prev) => (updated.length === 0 ? 0 : Math.min(prev, updated.length - 1)));
      } else {
        handleNext();
      }
    },
    [currentCard, dueOnly, hideLearned, hideExcluded, ratingFilter, initialCards, activeUser.id, handleNext]
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
        handleRateSRS('again'); // [1]: AGAIN
      } else if (e.key === '2') {
        e.preventDefault();
        handleRateSRS('hard'); // [2]: HARD
      } else if (e.key === '3') {
        e.preventDefault();
        handleRateSRS('good'); // [3]: GOOD
      } else if (e.key === '4') {
        e.preventDefault();
        handleRateSRS('easy'); // [4]: EASY
      } else if (e.code === 'KeyM') {
        e.preventDefault();
        handleToggleLearned(); // 'M': TOGGLE LEARNED
      } else if (e.code === 'KeyX') {
        e.preventDefault();
        handleToggleExcluded(); // 'X': TOGGLE IGNORE
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handleFlip, handlePlayAudio, handleNext, handlePrevious, handleRateSRS, handleToggleLearned, handleToggleExcluded]);

  // Count how many total cards are learned and excluded
  const allSRS = getAllSRSData(activeUser.id);
  const totalLearnedCount = initialCards.filter((c) => allSRS[c.id]?.isLearned).length;
  const totalExcludedCount = initialCards.filter((c) => allSRS[c.id]?.isExcluded).length;

  if (!currentCard || filteredCards.length === 0) {
    return (
      <div className="max-w-md mx-auto text-center py-20 space-y-5">
        <div className="w-16 h-16 rounded-3xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 flex items-center justify-center mx-auto shadow-xl shadow-emerald-500/10">
          <Award className="w-8 h-8" />
        </div>
        <h3 className="text-2xl font-extrabold text-white">All Active Cards Completed!</h3>
        <p className="text-sm text-slate-400 max-w-sm mx-auto">
          {ratingFilter !== 'all'
            ? `No cards in this deck currently match status filter "${ratingFilter}".`
            : (hideLearned && totalLearnedCount > 0) || (hideExcluded && totalExcludedCount > 0)
            ? `You have marked ${totalLearnedCount} card${totalLearnedCount === 1 ? '' : 's'} as learned and ${totalExcludedCount} as ignored. Adjust filters below to review them.`
            : 'No cards match your current filter settings.'}
        </p>

        <div className="flex flex-col sm:flex-row items-center justify-center gap-3 pt-2">
          {ratingFilter !== 'all' && (
            <button
              onClick={() => {
                setRatingFilter('all');
                applyFilter(hideLearned, dueOnly, hideExcluded, 'all');
              }}
              className="px-4 py-2.5 rounded-xl bg-sky-500 hover:bg-sky-400 text-white text-xs font-semibold shadow-md shadow-sky-500/25"
            >
              Reset Status Filter (Show All)
            </button>
          )}
          {hideLearned && totalLearnedCount > 0 && ratingFilter === 'all' && (
            <button
              onClick={() => {
                setHideLearned(false);
                applyFilter(false, dueOnly, hideExcluded, ratingFilter);
              }}
              className="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold"
            >
              Show Learned Cards ({totalLearnedCount})
            </button>
          )}
          {hideExcluded && totalExcludedCount > 0 && ratingFilter === 'all' && (
            <button
              onClick={() => {
                setHideExcluded(false);
                applyFilter(hideLearned, dueOnly, false, ratingFilter);
              }}
              className="px-4 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold"
            >
              Show Ignored Cards ({totalExcludedCount})
            </button>
          )}
          <button
            onClick={onExit}
            className="px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 text-xs font-semibold"
          >
            Back to Dashboard
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-3xl mx-auto space-y-6 pb-20">
      {/* Centralized Native Audio Element (Single-source to prevent double playback) */}
      <audio
        ref={audioRef}
        src={audioSrc || undefined}
        preload="auto"
        onPlay={() => setIsAudioPlaying(true)}
        onPause={() => setIsAudioPlaying(false)}
        onEnded={() => setIsAudioPlaying(false)}
        onError={() => setIsAudioPlaying(false)}
      />

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
            <div className="flex items-center gap-2">
              <span className="text-[10px] uppercase font-bold text-sky-400 tracking-wider">
                {title}
              </span>
              <span className="text-[10px] font-semibold px-1.5 py-0.2 rounded bg-slate-800 text-slate-300 border border-slate-700">
                {displayLessonLabel}
              </span>
              {(displayLessonLabel?.includes('105B') || title?.includes('105B') || (currentCard?.id && currentCard.id.includes('U105B'))) && (
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-purple-500/20 text-purple-300 border border-purple-500/40">
                  Expansion • Complementary to Lesson 105
                </span>
              )}
            </div>
            <div className="text-xs text-slate-400">
              Card {currentIndex + 1} of {filteredCards.length}
              {ratingFilter !== 'all' && (
                <span className="text-sky-400 ml-1.5 font-semibold capitalize">
                  [{ratingFilter}]
                </span>
              )}
              {totalLearnedCount > 0 && (
                <span className="text-emerald-400 ml-2 font-medium">
                  ({totalLearnedCount} learned)
                </span>
              )}
              {totalExcludedCount > 0 && (
                <span className="text-rose-400 ml-2 font-medium">
                  ({totalExcludedCount} ignored)
                </span>
              )}
            </div>
          </div>
        </div>

        {/* Filter & Direction Controls */}
        <div className="flex flex-wrap items-center gap-2">
          {/* Card Status / Rating Filter Dropdown */}
          <div className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl bg-slate-800 border border-slate-700 text-xs">
            <Filter className="w-3.5 h-3.5 text-sky-400" />
            <select
              value={ratingFilter}
              onChange={(e) => {
                const val = e.target.value as RatingFilterOption;
                setRatingFilter(val);
                applyFilter(hideLearned, dueOnly, hideExcluded, val);
              }}
              className="bg-transparent text-slate-200 text-xs font-semibold focus:outline-none cursor-pointer pr-1"
              title="Filter drill cards by their SRS rating status"
            >
              <option value="all" className="bg-slate-900 text-slate-200">All Ratings</option>
              <option value="again" className="bg-slate-900 text-rose-300">Again (1)</option>
              <option value="hard" className="bg-slate-900 text-amber-300">Hard (2)</option>
              <option value="good" className="bg-slate-900 text-sky-300">Good (3)</option>
              <option value="easy" className="bg-slate-900 text-emerald-300">Easy (4)</option>
              <option value="new" className="bg-slate-900 text-slate-300">New / Unrated</option>
            </select>
          </div>

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
              setUserStudyPreferences({ hideLearned: nextVal }, activeUser.id);
              applyFilter(nextVal, dueOnly, hideExcluded, ratingFilter);
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

          {/* Hide Ignored Toggle */}
          <button
            type="button"
            onClick={() => {
              const nextVal = !hideExcluded;
              setHideExcluded(nextVal);
              setUserStudyPreferences({ hideExcluded: nextVal }, activeUser.id);
              applyFilter(hideLearned, dueOnly, nextVal, ratingFilter);
            }}
            className={`px-3 py-1.5 rounded-xl border text-xs font-semibold flex items-center gap-1.5 transition-all ${
              hideExcluded
                ? 'bg-rose-950/80 border-rose-500/40 text-rose-400'
                : 'bg-slate-800 border-slate-700 text-slate-400 hover:text-white'
            }`}
            title="Hide cards you've decided to ignore"
          >
            <Ban className="w-3.5 h-3.5" />
            <span>Hide Ignored</span>
          </button>

          {/* Due Only (SRS) Toggle */}
          <button
            type="button"
            onClick={() => {
              const nextVal = !dueOnly;
              setDueOnly(nextVal);
              applyFilter(hideLearned, nextVal, hideExcluded, ratingFilter);
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

          {/* Auto-audio Toggle (default ON) */}
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

          {/* Help & Shortcuts button */}
          {onOpenHelp && (
            <button
              type="button"
              onClick={onOpenHelp}
              className="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white border border-slate-700 transition-all flex items-center gap-1.5 text-xs font-semibold"
              title="Help & Keyboard Shortcuts"
            >
              <HelpCircle className="w-4 h-4 text-sky-400" />
              <span className="hidden sm:inline">Help</span>
            </button>
          )}
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
          <div className="absolute inset-0 w-full h-full rounded-3xl p-6 sm:p-10 flex flex-col justify-between backface-hidden glass-card border border-sky-500/25 bg-gradient-to-b from-slate-900/95 via-slate-900/90 to-slate-950 shadow-2xl shadow-sky-950/30">
            {/* Top Bar on Front: Ignore on Top Left, Center Badges, Learned on Top Right */}
            <div className="flex items-center justify-between gap-2 w-full" onClick={(e) => e.stopPropagation()}>
              {/* Top Left: Ignore Button */}
              <button
                type="button"
                onClick={handleToggleExcluded}
                className={`px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition-all z-10 border shadow-sm ${
                  srsData?.isExcluded
                    ? 'bg-rose-900/90 text-rose-200 border-rose-500/80 shadow-rose-900/30 ring-1 ring-rose-400/40'
                    : 'bg-slate-800/80 hover:bg-rose-950/80 text-slate-400 hover:text-rose-300 border-slate-700/80 hover:border-rose-500/40 backdrop-blur-sm'
                }`}
                title="Ignore card (exclude from drill) (Shortcut: X)"
              >
                <Ban className="w-3.5 h-3.5 shrink-0" />
                <span>{srsData?.isExcluded ? 'Ignored' : 'Ignore'}</span>
                <span className="text-[10px] opacity-75 font-mono hidden sm:inline">[X]</span>
              </button>

              {/* Center Badges: Gender/POS and SRS Rating */}
              <div className="flex items-center gap-1.5 flex-wrap justify-center">
                {currentCard.gender_or_pos && (
                  <span className="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-800/90 text-sky-300 border border-slate-700/80 shadow-sm">
                    {currentCard.gender_or_pos}
                  </span>
                )}
                {ratingStatus && ratingStatus !== 'new' && (
                  <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full border shadow-sm ${
                    ratingStatus === 'again'
                      ? 'bg-rose-950/90 text-rose-300 border-rose-700/60'
                      : ratingStatus === 'hard'
                      ? 'bg-amber-950/90 text-amber-300 border-amber-700/60'
                      : ratingStatus === 'good'
                      ? 'bg-sky-950/90 text-sky-300 border-sky-700/60'
                      : 'bg-emerald-950/90 text-emerald-300 border-emerald-700/60'
                  }`}>
                    {ratingStatus.toUpperCase()}
                  </span>
                )}
              </div>

              {/* Top Right: Learned Button */}
              <button
                type="button"
                onClick={handleToggleLearned}
                className={`px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition-all z-10 border shadow-sm ${
                  srsData?.isLearned
                    ? 'bg-teal-600/90 text-white border-teal-400/80 shadow-teal-600/30 ring-1 ring-teal-400/40'
                    : 'bg-slate-800/80 hover:bg-teal-950/80 text-slate-300 hover:text-teal-300 border-slate-700/80 hover:border-teal-500/40 backdrop-blur-sm'
                }`}
                title="Mark card as learned (Shortcut: M)"
              >
                <CheckCircle className="w-3.5 h-3.5 shrink-0" />
                <span>{srsData?.isLearned ? 'Learned' : 'Learned'}</span>
                <span className="text-[10px] opacity-75 font-mono hidden sm:inline">[M]</span>
              </button>
            </div>

            {/* Prompt Content */}
            <div className="text-center py-6 space-y-4 my-auto">
              {studyDirection === 'greek_to_english' ? (
                <>
                  <h2 className="text-4xl sm:text-5xl md:text-6xl font-extrabold text-white tracking-wide font-serif leading-tight drop-shadow-sm">
                    {currentCard.greek}
                  </h2>
                  {/* Keep Speaker Sign on the Greek side of the card */}
                  <div className="inline-block mt-3" onClick={(e) => e.stopPropagation()}>
                    {audioSrc ? (
                      <button
                        type="button"
                        onClick={handlePlayAudio}
                        title="Play Native Audio (↓)"
                        className={`p-2.5 rounded-2xl transition-all duration-200 border shadow-md ${
                          isAudioPlaying
                            ? 'bg-sky-500 border-sky-400 text-white shadow-sky-500/30 scale-105 ring-2 ring-sky-300/40'
                            : 'bg-slate-800/90 text-sky-400 hover:bg-slate-700 hover:text-sky-300 border-slate-700'
                        }`}
                      >
                        {isAudioPlaying ? <Pause className="w-5 h-5" /> : <Volume2 className="w-5 h-5" />}
                      </button>
                    ) : (
                      <span className="inline-flex items-center gap-1.5 text-xs text-slate-500 italic py-1 px-2.5 rounded-lg bg-slate-800/40 border border-slate-700/50">
                        <VolumeX className="w-3.5 h-3.5 text-slate-500" /> No audio
                      </span>
                    )}
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

            {/* Subtle Flip Hint Footer */}
            <div className="text-center text-[11px] text-slate-500 font-medium tracking-wide flex items-center justify-center gap-1.5">
              <RotateCw className="w-3 h-3 text-slate-600" />
              <span>Tap card or press <kbd className="px-1 py-0.5 rounded bg-slate-800 text-slate-400 border border-slate-700/60 font-mono text-[10px]">↑</kbd> to flip</span>
            </div>
          </div>

          {/* ================= CARD BACK (REVEAL) ================= */}
          <div className="absolute inset-0 w-full h-full rounded-3xl p-6 sm:p-10 flex flex-col justify-between backface-hidden rotate-y-180 glass-card border border-teal-500/30 bg-gradient-to-b from-slate-900/95 via-slate-900/90 to-slate-950 shadow-2xl shadow-teal-950/30">
            {/* Top Bar on Back: Ignore on Top Left, Center Badges, Learned on Top Right */}
            <div className="flex items-center justify-between gap-2 w-full" onClick={(e) => e.stopPropagation()}>
              {/* Top Left: Ignore Button */}
              <button
                type="button"
                onClick={handleToggleExcluded}
                className={`px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition-all z-10 border shadow-sm ${
                  srsData?.isExcluded
                    ? 'bg-rose-900/90 text-rose-200 border-rose-500/80 shadow-rose-900/30 ring-1 ring-rose-400/40'
                    : 'bg-slate-800/80 hover:bg-rose-950/80 text-slate-400 hover:text-rose-300 border-slate-700/80 hover:border-rose-500/40 backdrop-blur-sm'
                }`}
                title="Ignore card (exclude from drill) (Shortcut: X)"
              >
                <Ban className="w-3.5 h-3.5 shrink-0" />
                <span>{srsData?.isExcluded ? 'Ignored' : 'Ignore'}</span>
                <span className="text-[10px] opacity-75 font-mono hidden sm:inline">[X]</span>
              </button>

              {/* Center Badges */}
              <div className="flex items-center gap-1.5 flex-wrap justify-center">
                {currentCard.gender_or_pos && (
                  <span className="text-xs font-semibold px-2.5 py-1 rounded-full bg-slate-800/90 text-sky-300 border border-slate-700/80 shadow-sm">
                    {currentCard.gender_or_pos}
                  </span>
                )}
                {ratingStatus && ratingStatus !== 'new' && (
                  <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full border shadow-sm ${
                    ratingStatus === 'again'
                      ? 'bg-rose-950/90 text-rose-300 border-rose-700/60'
                      : ratingStatus === 'hard'
                      ? 'bg-amber-950/90 text-amber-300 border-amber-700/60'
                      : ratingStatus === 'good'
                      ? 'bg-sky-950/90 text-sky-300 border-sky-700/60'
                      : 'bg-emerald-950/90 text-emerald-300 border-emerald-700/60'
                  }`}>
                    {ratingStatus.toUpperCase()}
                  </span>
                )}
              </div>

              {/* Top Right: Learned Button */}
              <button
                type="button"
                onClick={handleToggleLearned}
                className={`px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition-all z-10 border shadow-sm ${
                  srsData?.isLearned
                    ? 'bg-teal-600/90 text-white border-teal-400/80 shadow-teal-600/30 ring-1 ring-teal-400/40'
                    : 'bg-slate-800/80 hover:bg-teal-950/80 text-slate-300 hover:text-teal-300 border-slate-700/80 hover:border-teal-500/40 backdrop-blur-sm'
                }`}
                title="Mark card as learned (Shortcut: M)"
              >
                <CheckCircle className="w-3.5 h-3.5 shrink-0" />
                <span>{srsData?.isLearned ? 'Learned' : 'Learned'}</span>
                <span className="text-[10px] opacity-75 font-mono hidden sm:inline">[M]</span>
              </button>
            </div>

            {/* Answer Content - No play button here to preserve vertical space */}
            <div className="text-center py-3 space-y-3 my-auto">
              {studyDirection === 'greek_to_english' ? (
                <>
                  <h2 className="text-2xl sm:text-3xl md:text-4xl font-extrabold text-teal-300 tracking-wide font-serif leading-tight">
                    {currentCard.greek}
                  </h2>
                  <h3 className="text-xl sm:text-2xl md:text-3xl font-bold text-white tracking-tight">
                    {currentCard.english}
                  </h3>
                  {currentCard.phonetic_hint && (
                    <div className="inline-block px-3 py-1 rounded-lg bg-slate-800/80 border border-slate-700/70 text-xs sm:text-sm font-mono text-teal-300">
                      /{currentCard.phonetic_hint}/
                    </div>
                  )}
                  {currentCard.example_el && (
                    <div className="text-left bg-slate-800/70 p-3 rounded-xl border border-slate-700/70 max-w-lg mx-auto shadow-sm">
                      <div className="font-serif text-teal-300 text-sm font-medium">{currentCard.example_el}</div>
                      <div className="text-slate-400 text-xs mt-0.5">{currentCard.example_en}</div>
                    </div>
                  )}
                  {currentCard.notes && (
                    <p className="text-xs sm:text-sm text-slate-300 max-w-lg mx-auto italic bg-slate-800/40 p-2.5 rounded-xl border border-slate-700/50">
                      {currentCard.notes}
                    </p>
                  )}
                </>
              ) : (
                <>
                  <h2 className="text-3xl sm:text-4xl font-extrabold text-teal-300 tracking-wide font-serif leading-tight">
                    {currentCard.greek}
                  </h2>
                  <h3 className="text-lg sm:text-xl font-semibold text-slate-300 tracking-tight">
                    {currentCard.english}
                  </h3>
                  {currentCard.phonetic_hint && (
                    <div className="inline-block px-3 py-1 rounded-lg bg-slate-800/80 border border-slate-700 text-xs sm:text-sm font-mono text-teal-300">
                      /{currentCard.phonetic_hint}/
                    </div>
                  )}
                  {currentCard.example_el && (
                    <div className="text-left bg-slate-800/70 p-3 rounded-xl border border-slate-700/70 max-w-lg mx-auto shadow-sm">
                      <div className="font-serif text-teal-300 text-sm font-medium">{currentCard.example_el}</div>
                      <div className="text-slate-400 text-xs mt-0.5">{currentCard.example_en}</div>
                    </div>
                  )}
                  {currentCard.notes && (
                    <p className="text-xs sm:text-sm text-slate-300 max-w-lg mx-auto italic bg-slate-800/40 p-2.5 rounded-xl border border-slate-700/50">
                      {currentCard.notes}
                    </p>
                  )}
                </>
              )}
            </div>

            {/* Subtle Flip Back Indicator */}
            <div className="text-center text-[11px] text-slate-500 font-medium tracking-wide flex items-center justify-center gap-1.5">
              <RotateCw className="w-3 h-3 text-slate-600" />
              <span>Tap card or press <kbd className="px-1 py-0.5 rounded bg-slate-800 text-slate-400 border border-slate-700/60 font-mono text-[10px]">↑</kbd> to flip back</span>
            </div>
          </div>
        </div>
      </div>

      {/* ========================================================================= */}
      {/* ROW 1: Card Assessment & SRS Rating Controls (Equal Sized 4-Button Row)    */}
      {/* ========================================================================= */}
      <div 
        id="study-row-1-assessment" 
        data-testid="study-row-1-assessment"
        className="grid grid-cols-4 gap-2 sm:gap-3 pt-1"
      >
        {/* Again [1] */}
        <button
          type="button"
          onClick={() => handleRateSRS('again')}
          className={`h-12 sm:h-13 w-full rounded-2xl font-semibold text-xs sm:text-sm transition-all hover:scale-[1.02] active:scale-95 flex items-center justify-center gap-1.5 border shadow-sm ${
            ratingStatus === 'again'
              ? 'bg-rose-600 border-rose-400 text-white shadow-rose-600/30 ring-2 ring-rose-400/50'
              : 'bg-rose-950/70 hover:bg-rose-900/90 border-rose-500/40 text-rose-300'
          }`}
          title="Repeat soon • Mark Again (Shortcut: 1)"
        >
          <span>Again</span>
          <span className="text-[10px] sm:text-xs opacity-80 font-mono">[1]</span>
        </button>

        {/* Hard [2] */}
        <button
          type="button"
          onClick={() => handleRateSRS('hard')}
          className={`h-12 sm:h-13 w-full rounded-2xl font-semibold text-xs sm:text-sm transition-all hover:scale-[1.02] active:scale-95 flex items-center justify-center gap-1.5 border shadow-sm ${
            ratingStatus === 'hard'
              ? 'bg-amber-600 border-amber-400 text-white shadow-amber-600/30 ring-2 ring-amber-400/50'
              : 'bg-amber-950/70 hover:bg-amber-900/90 border-amber-500/40 text-amber-300'
          }`}
          title="Challenging card • Mark Hard (Shortcut: 2)"
        >
          <span>Hard</span>
          <span className="text-[10px] sm:text-xs opacity-80 font-mono">[2]</span>
        </button>

        {/* Good [3] */}
        <button
          type="button"
          onClick={() => handleRateSRS('good')}
          className={`h-12 sm:h-13 w-full rounded-2xl font-semibold text-xs sm:text-sm transition-all hover:scale-[1.02] active:scale-95 flex items-center justify-center gap-1.5 border shadow-sm ${
            ratingStatus === 'good'
              ? 'bg-sky-600 border-sky-400 text-white shadow-sky-600/30 ring-2 ring-sky-400/50'
              : 'bg-sky-950/70 hover:bg-sky-900/90 border-sky-500/40 text-sky-300'
          }`}
          title="Correct recall • Mark Good (Shortcut: 3)"
        >
          <span>Good</span>
          <span className="text-[10px] sm:text-xs opacity-80 font-mono">[3]</span>
        </button>

        {/* Easy [4] */}
        <button
          type="button"
          onClick={() => handleRateSRS('easy')}
          className={`h-12 sm:h-13 w-full rounded-2xl font-semibold text-xs sm:text-sm transition-all hover:scale-[1.02] active:scale-95 flex items-center justify-center gap-1.5 border shadow-sm ${
            ratingStatus === 'easy'
              ? 'bg-emerald-600 border-emerald-400 text-white shadow-emerald-600/30 ring-2 ring-emerald-400/50'
              : 'bg-emerald-950/70 hover:bg-emerald-900/90 border-emerald-500/40 text-emerald-300'
          }`}
          title="Effortless recall • Mark Easy (Shortcut: 4)"
        >
          <span>Easy</span>
          <span className="text-[10px] sm:text-xs opacity-80 font-mono">[4]</span>
        </button>
      </div>

      {/* ========================================================================= */}
      {/* ROW 2: Navigation & Playback Controls (Equal Sized 4-Button Row)          */}
      {/* ========================================================================= */}
      <div 
        id="study-row-2-navigation" 
        data-testid="study-row-2-navigation"
        className="grid grid-cols-4 gap-2 sm:gap-3 pt-2"
      >
        {/* 1. Previous button */}
        <button
          onClick={handlePrevious}
          className="h-12 sm:h-13 w-full inline-flex items-center justify-center gap-1 sm:gap-2 px-2 sm:px-4 rounded-2xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-semibold text-xs sm:text-sm transition-all hover:scale-[1.02] active:scale-95 shadow-sm"
          title="Previous card (← Left Arrow)"
        >
          <ChevronLeft className="w-4 h-4 shrink-0" />
          <span className="truncate">Previous</span>
        </button>

        {/* 2. Play Audio button (comes second) */}
        <button
          onClick={handlePlayAudio}
          className={`h-12 sm:h-13 w-full inline-flex items-center justify-center gap-1 sm:gap-2 px-2 sm:px-4 rounded-2xl border font-semibold text-xs sm:text-sm transition-all hover:scale-[1.02] active:scale-95 shadow-sm ${
            isAudioPlaying
              ? 'bg-sky-500 text-white border-sky-400 shadow-lg shadow-sky-500/30'
              : 'bg-slate-800 hover:bg-slate-700 text-sky-300 border-slate-700'
          }`}
          title="Play Audio (↓ Down Arrow)"
        >
          {isAudioPlaying ? <Pause className="w-4 h-4 shrink-0" /> : <Volume2 className="w-4 h-4 shrink-0" />}
          <span>[↓]</span>
        </button>

        {/* 3. Flip button (comes third) */}
        <button
          onClick={handleFlip}
          className="h-12 sm:h-13 w-full inline-flex items-center justify-center gap-1 sm:gap-2 px-2 sm:px-4 rounded-2xl bg-slate-800 hover:bg-slate-700 text-sky-400 border border-sky-500/20 font-semibold text-xs sm:text-sm transition-all hover:scale-[1.02] active:scale-95 shadow-sm"
          title="Flip Card (↑ Up Arrow)"
        >
          <RotateCw className="w-4 h-4 shrink-0" />
          <span>[↑]</span>
        </button>

        {/* 4. Next button */}
        <button
          onClick={handleNext}
          className="h-12 sm:h-13 w-full inline-flex items-center justify-center gap-1 sm:gap-2 px-2 sm:px-4 rounded-2xl bg-sky-500 hover:bg-sky-400 text-white font-semibold text-xs sm:text-sm shadow-lg shadow-sky-500/20 transition-all hover:scale-[1.02] active:scale-95"
          title="Next card (→ Right Arrow)"
        >
          <span className="truncate">Next</span>
          <ChevronRight className="w-4 h-4 shrink-0" />
        </button>
      </div>
    </div>
  );
};

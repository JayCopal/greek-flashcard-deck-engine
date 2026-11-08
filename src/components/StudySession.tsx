import { useState, useEffect, useCallback, useRef, useMemo } from 'react';
import { CardEntry, SRSRating, LessonStatus } from '../types/schema';
import { 
  getActiveUser, 
  getActiveUserId, 
  getUserStudyPreferences, 
  setUserStudyPreferences, 
  getUserLessonStatus, 
  setUserLessonStatus,
  setLastStudiedLesson 
} from '../utils/userStorage';
import { parseLessonCode, extractUnitContext } from '../utils/unitNaming';
import { renderGreekWithTonos } from '../utils/greekTypography';
import { sanitizeEnglishPrompt, getProductionHint, ProductionHint } from '../utils/flashcardPrompt';
import { triggerHaptic } from '../utils/haptics';
import { 
  getCardSRS, 
  toggleCardLearned, 
  toggleCardExcluded,
  recordSRSRating, 
  recordCardPresentation,
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
  Pause,
  CheckCircle, 
  Check,
  Eye,
  EyeOff, 
  Clock, 
  ArrowUpDown, 
  Award, 
  FileText, 
  Ban, 
  Filter,
  HelpCircle,
  Sliders,
  Settings as SettingsIcon,
  Lightbulb,
  X
} from 'lucide-react';

type StudyDirection = 'greek_to_english' | 'english_to_greek';

const STATUS_OPTIONS: {
  value: LessonStatus;
  label: string;
  icon: string;
  endIcon?: string;
  activeClasses: string;
}[] = [
  {
    value: 'not_started',
    label: 'Not Started',
    icon: '⚪',
    activeClasses: 'bg-slate-800 text-slate-200 border-slate-500 ring-2 ring-slate-400/40',
  },
  {
    value: 'in_progress_1',
    label: 'In Progress 1',
    icon: '🟡',
    endIcon: '🟡',
    activeClasses: 'bg-yellow-950/80 text-yellow-200 border-yellow-500 ring-2 ring-yellow-500/40',
  },
  {
    value: 'in_progress_2',
    label: 'In Progress 2',
    icon: '🟡',
    endIcon: '🟡',
    activeClasses: 'bg-yellow-950 text-yellow-300 border-yellow-400 ring-2 ring-yellow-400/50',
  },
  {
    value: 'in_progress_3',
    label: 'In Progress 3',
    icon: '🟠',
    endIcon: '🟠',
    activeClasses: 'bg-amber-950 text-amber-300 border-amber-500 ring-2 ring-amber-500/50',
  },
  {
    value: 'in_progress_4',
    label: 'In Progress 4',
    icon: '🟠',
    endIcon: '🟠',
    activeClasses: 'bg-orange-950 text-orange-300 border-orange-500 ring-2 ring-orange-500/50',
  },
  {
    value: 'in_progress_5',
    label: 'In Progress 5',
    icon: '🟠',
    endIcon: '🟠',
    activeClasses: 'bg-orange-950 text-orange-400 border-orange-400 ring-2 ring-orange-400/60',
  },
  {
    value: 'learned',
    label: 'Learned',
    icon: '🟢',
    activeClasses: 'bg-emerald-950 text-emerald-200 border-emerald-500 ring-2 ring-emerald-500/40',
  },
];

interface StudySessionProps {
  cards: CardEntry[];
  title?: string;
  lessonNotes?: string;
  lessonNumber?: string;
  unitId?: string;
  lessonId?: string;
  initialHideExcluded?: boolean;
  initialHideLearned?: boolean;
  onExit: () => void;
  onOpenHelp?: () => void;
  onOpenSettings?: () => void;
}

export const StudySession: React.FC<StudySessionProps> = ({
  cards: initialCards,
  title = 'Study Drill',
  lessonNotes,
  lessonNumber,
  unitId,
  lessonId,
  initialHideExcluded,
  initialHideLearned,
  onExit,
  onOpenHelp,
  onOpenSettings,
}) => {
  const [activeUser, setActiveUser] = useState(getActiveUser());
  const userPrefs = getUserStudyPreferences(activeUser.id);

  // Auto-scroll progress bar ref
  const progressBarRef = useRef<HTMLDivElement>(null);

  // Deck completion & unit status offer state
  const [showCompletionModal, setShowCompletionModal] = useState<boolean>(false);
  const [statusUpdateMessage, setStatusUpdateMessage] = useState<string | null>(null);

  // Automatically derive effective unit and lesson IDs
  const effectiveUnitId = useMemo(() => {
    if (unitId) return unitId;
    if (initialCards.length > 0 && initialCards[0]?.id) {
      const match = initialCards[0].id.match(/U(\d+[A-Za-z]?)/i);
      if (match) {
        return `unit-${match[1].toLowerCase()}`;
      }
    }
    return undefined;
  }, [unitId, initialCards]);

  const effectiveLessonId = useMemo(() => {
    if (lessonId) return lessonId;
    return 'lesson-01';
  }, [lessonId]);

  const [currentUnitStatus, setCurrentUnitStatus] = useState<LessonStatus>(() => {
    if (effectiveUnitId && effectiveLessonId) {
      return getUserLessonStatus(effectiveUnitId, effectiveLessonId, 'not_started', activeUser.id);
    }
    return 'not_started';
  });

  useEffect(() => {
    if (effectiveUnitId && effectiveLessonId) {
      setCurrentUnitStatus(getUserLessonStatus(effectiveUnitId, effectiveLessonId, 'not_started', activeUser.id));
    }
  }, [effectiveUnitId, effectiveLessonId, activeUser.id]);

  // Handle updating unit status when offered upon completion
  const handleUpdateUnitStatus = async (newStatus: LessonStatus) => {
    setCurrentUnitStatus(newStatus);
    if (effectiveUnitId && effectiveLessonId) {
      setUserLessonStatus(effectiveUnitId, effectiveLessonId, newStatus, activeUser.id);
      try {
        await fetch(`/api/lesson/${effectiveUnitId}/${effectiveLessonId}`, {
          method: 'PUT',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ lesson_status: newStatus }),
        });
      } catch {
        // Offline safe
      }
      const opt = STATUS_OPTIONS.find((o) => o.value === newStatus);
      const label = opt ? `${opt.icon} ${opt.label}${opt.endIcon ? ` ${opt.endIcon}` : ''}` : newStatus;
      setStatusUpdateMessage(`Lesson status updated to "${label}"!`);
      setTimeout(() => setStatusUpdateMessage(null), 3000);
    }
  };

  // Automatically scroll down to the progress bar when a deck is selected
  useEffect(() => {
    const timer = setTimeout(() => {
      if (progressBarRef.current) {
        progressBarRef.current.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }, 120);
    return () => clearTimeout(timer);
  }, []);

  const isAllIgnored = initialCards.length > 0 && initialCards.every((c) => {
    const s = getAllSRSData(getActiveUserId())[c.id];
    return s?.isExcluded && !s?.isLearned;
  });

  const isAllLearned = initialCards.length > 0 && initialCards.every((c) => {
    const s = getAllSRSData(getActiveUserId())[c.id];
    return s?.isLearned && !s?.isExcluded;
  });

  const resolvedHideExcluded = initialHideExcluded !== undefined 
    ? initialHideExcluded 
    : (isAllIgnored ? false : userPrefs.hideExcluded);

  const resolvedHideLearned = initialHideLearned !== undefined 
    ? initialHideLearned 
    : (isAllLearned ? false : userPrefs.hideLearned);

  // Study configuration options
  const [studyDirection, setStudyDirection] = useState<StudyDirection>(userPrefs.studyDirection || 'greek_to_english');
  const [hideLearned, setHideLearned] = useState<boolean>(resolvedHideLearned);
  const [hideExcluded, setHideExcluded] = useState<boolean>(resolvedHideExcluded);
  const [dueOnly, setDueOnly] = useState<boolean>(false);
  const [ratingFilter, setRatingFilter] = useState<RatingFilterOption>('all');
  const [autoPlayAudio, setAutoPlayAudio] = useState<boolean>(userPrefs.autoPlayAudio !== undefined ? userPrefs.autoPlayAudio : true);
  const [playbackSpeed, setPlaybackSpeed] = useState<number>(userPrefs.playbackSpeed || 1.0);
  const [highlightTonos, setHighlightTonos] = useState<boolean>(userPrefs.highlightTonos !== undefined ? userPrefs.highlightTonos : true);
  const [showNotes, setShowNotes] = useState<boolean>(false);
  const [showSettingsDrawer, setShowSettingsDrawer] = useState<boolean>(false);

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
  const [hintStep, setHintStep] = useState<number>(0); // 0 = closed, 1 = Step 1 (first letters), 2 = Step 2 (more letters), 3 = Step 3 (sounds & guide)
  const [showNotesPeek, setShowNotesPeek] = useState<boolean>(false);

  // Centralized single HTMLAudioElement ref and playback state
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [isAudioPlaying, setIsAudioPlaying] = useState<boolean>(false);
  const [playingSentenceAudio, setPlayingSentenceAudio] = useState<string | null>(null);
  const sentenceAudioRef = useRef<HTMLAudioElement | null>(null);

  // Touch gesture coordinates for mobile swipe
  const touchStartX = useRef<number | null>(null);
  const touchStartY = useRef<number | null>(null);

  const handleTouchStart = (e: React.TouchEvent) => {
    touchStartX.current = e.touches[0].clientX;
    touchStartY.current = e.touches[0].clientY;
  };

  const handleTouchEnd = (e: React.TouchEvent) => {
    if (touchStartX.current === null || touchStartY.current === null) return;
    const deltaX = e.changedTouches[0].clientX - touchStartX.current;
    const deltaY = e.changedTouches[0].clientY - touchStartY.current;
    touchStartX.current = null;
    touchStartY.current = null;

    // Vertical swipe up -> Flip card
    if (deltaY < -40 && Math.abs(deltaY) > Math.abs(deltaX)) {
      handleFlip();
      return;
    }

    // Horizontal swipe -> Prev/Next
    if (Math.abs(deltaX) > 50 && Math.abs(deltaX) > Math.abs(deltaY)) {
      if (deltaX < 0) {
        handleNext();
      } else {
        handlePrevious();
      }
    }
  };

  const cyclePlaybackSpeed = () => {
    const speeds = [0.75, 1.0, 1.25];
    const nextIndex = (speeds.indexOf(playbackSpeed) + 1) % speeds.length;
    const nextSpeed = speeds[nextIndex];
    setPlaybackSpeed(nextSpeed);
    setUserStudyPreferences({ playbackSpeed: nextSpeed }, activeUser.id);
    if (audioRef.current) {
      audioRef.current.playbackRate = nextSpeed;
    }
    triggerHaptic('light');
  };

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
  const timesPresented = srsData?.timesPresented ?? 0;

  // Track each presentation of a card during the study session
  const lastPresentedCardIdRef = useRef<string | null>(null);
  useEffect(() => {
    if (!currentCard?.id) return;
    if (lastPresentedCardIdRef.current === currentCard.id) return;
    lastPresentedCardIdRef.current = currentCard.id;
    recordCardPresentation(currentCard.id, activeUser.id);
  }, [currentCard?.id, activeUser.id]);

  const productionHint = useMemo<ProductionHint | null>(() => {
    if (!currentCard) return null;
    return getProductionHint(currentCard);
  }, [currentCard]);

  // Parse lesson code and unit context
  const parsedLessonCode = useMemo(() => {
    if (lessonNumber) return parseLessonCode(lessonNumber);
    if (effectiveUnitId) return parseLessonCode(effectiveUnitId);
    if (currentCard?.id) {
      const match = currentCard.id.match(/U(\d+[A-Za-z]?)/i);
      if (match) return parseLessonCode(`unit-${match[1]}`);
    }
    return parseLessonCode('OG-01-A');
  }, [lessonNumber, effectiveUnitId, currentCard]);

  const displayLessonLabel = parsedLessonCode.lessonLabel;
  const unitContext = useMemo(() => extractUnitContext(title), [title]);

  const baseUrl = import.meta.env.BASE_URL.endsWith('/')
    ? import.meta.env.BASE_URL
    : `${import.meta.env.BASE_URL}/`;
  const audioSrc = currentCard?.audio ? `${baseUrl}audio/${currentCard.audio}` : null;

  const playSentenceAudio = useCallback((audioFile: string) => {
    if (!audioFile) return;
    const url = `${baseUrl}audio/${audioFile}`;
    if (sentenceAudioRef.current) {
      if (playingSentenceAudio === audioFile && !sentenceAudioRef.current.paused) {
        sentenceAudioRef.current.pause();
        setPlayingSentenceAudio(null);
        return;
      }
      sentenceAudioRef.current.pause();
    }
    const audio = new Audio(url);
    sentenceAudioRef.current = audio;
    audio.playbackRate = playbackSpeed;
    setPlayingSentenceAudio(audioFile);
    audio.onended = () => setPlayingSentenceAudio(null);
    audio.onerror = () => setPlayingSentenceAudio(null);
    audio.play().catch(() => setPlayingSentenceAudio(null));
  }, [baseUrl, playbackSpeed, playingSentenceAudio]);

  const handleNext = useCallback(() => {
    setIsFlipped(false);
    setHintStep(0);
    setShowNotesPeek(false);
    triggerHaptic('light');
    if (currentIndex + 1 >= filteredCards.length) {
      // Completed deck from beginning to end!
      setShowCompletionModal(true);
      triggerHaptic('success');
    } else {
      setCurrentIndex((prev) => prev + 1);
    }
  }, [currentIndex, filteredCards.length]);

  const handlePrevious = useCallback(() => {
    setIsFlipped(false);
    setHintStep(0);
    setShowNotesPeek(false);
    triggerHaptic('light');
    setCurrentIndex((prev) => (prev - 1 >= 0 ? prev - 1 : filteredCards.length - 1));
  }, [filteredCards.length]);

  const handleFlip = useCallback(() => {
    setIsFlipped((prev) => !prev);
    triggerHaptic('light');
    if (sentenceAudioRef.current) {
      sentenceAudioRef.current.pause();
    }
    setPlayingSentenceAudio(null);
    // Anytime a card is flipped, play the native audio with selected speed
    if (audioRef.current && audioSrc) {
      audioRef.current.currentTime = 0;
      audioRef.current.playbackRate = playbackSpeed;
      audioRef.current.play().catch(() => {});
    }
  }, [audioSrc, playbackSpeed]);

  const handlePlayAudio = useCallback(() => {
    if (!audioRef.current || !audioSrc) return;
    if (audioRef.current.paused) {
      audioRef.current.currentTime = 0;
      audioRef.current.playbackRate = playbackSpeed;
      audioRef.current.play().catch(() => {});
      triggerHaptic('light');
    } else {
      audioRef.current.pause();
    }
  }, [audioSrc, playbackSpeed]);

  // Track last studied lesson for Quick Resume
  useEffect(() => {
    if (effectiveUnitId) {
      setLastStudiedLesson({
        unitId: effectiveUnitId,
        lessonId: lessonId || effectiveUnitId,
        title,
        lessonLabel: parsedLessonCode.lessonLabel,
      }, activeUser.id);
    }
  }, [effectiveUnitId, lessonId, title, parsedLessonCode.lessonLabel, activeUser.id]);

  // Single-source audio playback controller: stop previous and auto-play new card once
  useEffect(() => {
    if (audioRef.current) {
      audioRef.current.pause();
      audioRef.current.currentTime = 0;
    }
    if (sentenceAudioRef.current) {
      sentenceAudioRef.current.pause();
    }
    setPlayingSentenceAudio(null);
    setIsAudioPlaying(false);
    setHintStep(0);
    setShowNotesPeek(false);

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
    setHintStep(0);
    setShowNotesPeek(false);
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
      triggerHaptic(rating === 'again' ? 'warning' : rating === 'easy' ? 'success' : 'medium');
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
        // In English -> Greek mode, lock native audio before flipping to avoid spoiling the Greek pronunciation
        if (studyDirection === 'english_to_greek' && !isFlipped) {
          return;
        }
        handlePlayAudio(); // DOWN ARROW: PLAY NATIVE AUDIO
      } else if (e.code === 'KeyH') {
        e.preventDefault();
        setHintStep((prev) => (prev >= 3 ? 0 : prev + 1)); // 'H': CYCLE 3-STEP HINT (0 -> 1 -> 2 -> 3 -> 0)
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
      } else if (e.key === 'Escape') {
        e.preventDefault();
        onExit(); // ESC: EXIT DRILL TO LANDING PAGE
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handleFlip, handlePlayAudio, handleNext, handlePrevious, handleRateSRS, handleToggleLearned, handleToggleExcluded, studyDirection, isFlipped]);

  // Count how many total cards are learned and excluded
  const allSRS = getAllSRSData(activeUser.id);
  const totalLearnedCount = initialCards.filter((c) => allSRS[c.id]?.isLearned).length;
  const totalExcludedCount = initialCards.filter((c) => allSRS[c.id]?.isExcluded).length;

  if (!currentCard || filteredCards.length === 0) {
    return (
      <div className="max-w-md mx-auto text-center py-16 space-y-5">
        <div className="w-16 h-16 rounded-3xl bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 flex items-center justify-center mx-auto shadow-xl shadow-emerald-500/10">
          <Award className="w-8 h-8" />
        </div>
        <h3 className="text-2xl font-extrabold text-white">All Active Cards Completed!</h3>
        <p className="text-sm text-slate-400 max-w-sm mx-auto">
          {ratingFilter !== 'all'
            ? `No cards in this deck currently match status filter "${ratingFilter}".`
            : (hideLearned && totalLearnedCount > 0) || (hideExcluded && totalExcludedCount > 0)
            ? `You have marked ${totalLearnedCount} card${totalLearnedCount === 1 ? '' : 's'} as learned and ${totalExcludedCount} as ignored. Adjust filters below to review them.`
            : 'You have finished all active cards in this deck!'}
        </p>

        {/* Offer lesson status change */}
        <div className="p-4 rounded-2xl bg-slate-900/90 border border-slate-800 space-y-3 text-left">
          <div className="flex items-center justify-between">
            <span className="text-xs font-bold uppercase tracking-wider text-slate-400">
              Lesson Mastery Status
            </span>
            <span className="text-xs font-bold text-sky-400">
              {displayLessonLabel}
            </span>
          </div>

          {statusUpdateMessage && (
            <div className="p-2.5 rounded-xl bg-emerald-950/70 border border-emerald-500/40 text-emerald-300 text-xs flex items-center gap-2">
              <Check className="w-4 h-4 text-emerald-400 shrink-0" />
              <span>{statusUpdateMessage}</span>
            </div>
          )}

          <p className="text-xs text-slate-400">
            Update lesson status for your active profile:
          </p>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
            {STATUS_OPTIONS.map((opt) => (
              <button
                key={opt.value}
                type="button"
                onClick={() => handleUpdateUnitStatus(opt.value)}
                className={`p-2.5 rounded-xl text-xs font-semibold flex items-center gap-2 border transition-all text-left ${
                  currentUnitStatus === opt.value
                    ? opt.activeClasses
                    : 'bg-slate-800/80 hover:bg-slate-700/80 border-slate-700 text-slate-300'
                }`}
              >
                <span>{opt.icon}</span>
                <span className="font-bold">{opt.label}</span>
                {opt.endIcon && <span>{opt.endIcon}</span>}
                {currentUnitStatus === opt.value && (
                  <Check className="w-3.5 h-3.5 ml-auto text-current" />
                )}
              </button>
            ))}
          </div>
        </div>

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

  const renderExamples = (card: CardEntry) => {
    if (!card.example_el && !card.example2_el) return null;
    return (
      <div className="space-y-2 max-w-lg w-full mx-auto select-text">
        {card.example_el && (
          <div className="text-left bg-slate-800/80 p-2 sm:p-2.5 rounded-xl border border-slate-700/70 shadow-sm flex items-start justify-between gap-2.5">
            <div className="flex-1 min-w-0">
              <div className="font-serif text-teal-300 text-xs sm:text-sm font-medium leading-relaxed">
                {card.example_el}
              </div>
              {card.example_en && (
                <div className="text-slate-400 text-[11px] sm:text-xs mt-0.5">
                  {card.example_en}
                </div>
              )}
            </div>
            {card.example_audio && (
              <button
                type="button"
                onClick={(e) => {
                  e.stopPropagation();
                  playSentenceAudio(card.example_audio!);
                }}
                className={`p-1.5 rounded-lg border transition-all shrink-0 mt-0.5 ${
                  playingSentenceAudio === card.example_audio
                    ? 'bg-teal-500 text-slate-950 border-teal-400 ring-2 ring-teal-400/50'
                    : 'bg-teal-950/70 hover:bg-teal-900/90 text-teal-300 border-teal-700/60 hover:text-white'
                }`}
                title="Play Sentence 1 audio"
              >
                <Volume2 className="w-3.5 h-3.5" />
              </button>
            )}
          </div>
        )}
        {card.example2_el && (
          <div className="text-left bg-slate-800/80 p-2 sm:p-2.5 rounded-xl border border-slate-700/70 shadow-sm flex items-start justify-between gap-2.5">
            <div className="flex-1 min-w-0">
              <div className="font-serif text-teal-300 text-xs sm:text-sm font-medium leading-relaxed">
                {card.example2_el}
              </div>
              {card.example2_en && (
                <div className="text-slate-400 text-[11px] sm:text-xs mt-0.5">
                  {card.example2_en}
                </div>
              )}
            </div>
            {card.example2_audio && (
              <button
                type="button"
                onClick={(e) => {
                  e.stopPropagation();
                  playSentenceAudio(card.example2_audio!);
                }}
                className={`p-1.5 rounded-lg border transition-all shrink-0 mt-0.5 ${
                  playingSentenceAudio === card.example2_audio
                    ? 'bg-teal-500 text-slate-950 border-teal-400 ring-2 ring-teal-400/50'
                    : 'bg-teal-950/70 hover:bg-teal-900/90 text-teal-300 border-teal-700/60 hover:text-white'
                }`}
                title="Play Sentence 2 audio"
              >
                <Volume2 className="w-3.5 h-3.5" />
              </button>
            )}
          </div>
        )}
      </div>
    );
  };

  return (
    <div className="max-w-3xl mx-auto space-y-4 sm:space-y-5 pb-20">
      {/* Centralized Native Audio Element (Single-source to prevent double playback) */}
      <audio
        ref={audioRef}
        src={audioSrc || undefined}
        preload="auto"
        onPlay={() => setIsAudioPlaying(true)}
        onPause={() => setIsAudioPlaying(false)}
        onEnded={() => setIsAudioPlaying(false)}
        onError={() => setIsAudioPlaying(false)}
        className="hidden"
      />

      {/* Top Header Bar */}
      <div className="glass-panel px-3.5 py-2 sm:px-4 sm:py-2.5 rounded-2xl flex flex-col gap-1 sm:gap-1.5">
        {/* Line 1: Back button, Lesson Name, and Card Counter */}
        <div className="flex items-center justify-between gap-3 min-w-0">
          <div className="flex items-center gap-2 sm:gap-2.5 min-w-0 flex-1">
            <button
              onClick={onExit}
              className="p-1.5 sm:p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white transition-colors border border-slate-700 shrink-0"
              title="Exit Drill (Esc)"
            >
              <ArrowLeft className="w-4 h-4" />
            </button>
            <div className="flex items-center gap-1.5 sm:gap-2 min-w-0 truncate">
              <span className="text-[10px] font-black uppercase tracking-wider px-2 py-0.5 rounded-lg bg-sky-500/15 text-sky-400 border border-sky-500/30 shrink-0">
                {displayLessonLabel}
              </span>
              <span className="text-xs sm:text-sm text-slate-200 font-semibold truncate" title={title}>
                {title}
              </span>
              {unitContext && (
                <span className="text-[10px] sm:text-xs text-slate-400 hidden md:inline shrink-0">
                  • {unitContext}
                </span>
              )}
            </div>
          </div>

          <div className="text-xs text-slate-400 font-medium shrink-0 whitespace-nowrap pl-2">
            Card <span className="text-slate-200 font-bold">{currentIndex + 1}</span> of{' '}
            <span className="text-slate-200 font-bold">{filteredCards.length}</span>
            {ratingFilter !== 'all' && (
              <span className="text-sky-400 ml-1.5 font-semibold capitalize">
                [{ratingFilter}]
              </span>
            )}
          </div>
        </div>

        {/* Line 2: Quick Controls (Direction, Speaker, Speed, and rest of buttons) */}
        <div className="flex items-center justify-between gap-2 pt-1 sm:pt-1.5 border-t border-slate-800/80">
          <div className="flex items-center gap-1 sm:gap-1.5 flex-wrap">
            {/* Study Direction Toggle */}
            <button
              type="button"
              onClick={() => {
                const next = studyDirection === 'greek_to_english' ? 'english_to_greek' : 'greek_to_english';
                setStudyDirection(next);
                setUserStudyPreferences({ studyDirection: next }, activeUser.id);
                setIsFlipped(false);
              }}
              className="px-2 sm:px-2.5 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-xs font-semibold text-slate-200 flex items-center gap-1 transition-all"
              title="Switch prompt direction"
            >
              <ArrowUpDown className="w-3.5 h-3.5 text-sky-400" />
              <span className="text-[11px] font-mono">{studyDirection === 'greek_to_english' ? 'EL→EN' : 'EN→EL'}</span>
            </button>

            {/* Auto-audio Toggle */}
            <button
              type="button"
              onClick={() => {
                const next = !autoPlayAudio;
                setAutoPlayAudio(next);
                setUserStudyPreferences({ autoPlayAudio: next }, activeUser.id);
              }}
              className={`p-1.5 sm:p-2 rounded-xl border text-xs font-semibold flex items-center transition-all ${
                autoPlayAudio
                  ? 'bg-sky-500/20 border-sky-500/40 text-sky-400'
                  : 'bg-slate-800 border-slate-700 text-slate-500 hover:text-slate-300'
              }`}
              title={`Auto-play audio: ${autoPlayAudio ? 'ON' : 'OFF'}`}
            >
              <Volume2 className="w-4 h-4" />
            </button>

            {/* Playback Speed Cycle Button */}
            <button
              type="button"
              onClick={cyclePlaybackSpeed}
              className="px-2 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 border border-slate-700 text-sky-400 hover:text-white text-xs font-bold font-mono transition-all"
              title="Audio Playback Speed (0.75x, 1.0x, 1.25x)"
            >
              {playbackSpeed}x
            </button>

            {/* Shuffle button */}
            <button
              type="button"
              onClick={handleShuffle}
              className="p-1.5 sm:p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white border border-slate-700 transition-all flex items-center"
              title="Shuffle deck"
            >
              <Shuffle className="w-4 h-4" />
            </button>

            {/* Notes Toggle Button if notes exist */}
            {lessonNotes && (
              <button
                type="button"
                onClick={() => setShowNotes(!showNotes)}
                className={`px-2.5 py-1.5 rounded-xl border text-xs font-semibold flex items-center gap-1 transition-all ${
                  showNotes
                    ? 'bg-sky-500 text-white border-sky-400 shadow-md shadow-sky-500/30'
                    : 'bg-slate-800 text-sky-400 border-slate-700 hover:text-white'
                }`}
                title="Toggle lesson grammar notes"
              >
                <FileText className="w-3.5 h-3.5" />
                <span className="hidden sm:inline text-[11px]">Notes</span>
              </button>
            )}
          </div>

          <div className="flex items-center gap-1 sm:gap-1.5 shrink-0">
            {/* Quick Filters / Session Settings Toggle */}
            <button
              type="button"
              onClick={() => setShowSettingsDrawer(!showSettingsDrawer)}
              className={`p-1.5 sm:p-2 rounded-xl border text-xs font-semibold flex items-center transition-all ${
                showSettingsDrawer || ratingFilter !== 'all' || dueOnly || !hideLearned || !hideExcluded
                  ? 'bg-sky-500 text-white border-sky-400 shadow-sm'
                  : 'bg-slate-800 hover:bg-slate-700 text-slate-300 border-slate-700'
              }`}
              title="Drill Filters & Settings"
            >
              <Sliders className="w-4 h-4" />
            </button>

            {/* Help button */}
            {onOpenHelp && (
              <button
                type="button"
                onClick={onOpenHelp}
                className="p-1.5 sm:p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white border border-slate-700 transition-all flex items-center"
                title="Keyboard Shortcuts & Help"
              >
                <HelpCircle className="w-4 h-4 text-sky-400" />
              </button>
            )}
          </div>
        </div>
      </div>

      {/* Quick Filters Drawer when toggled */}
      {showSettingsDrawer && (
        <div className="glass-panel p-3.5 rounded-2xl border-slate-700/80 space-y-3">
          <div className="flex items-center justify-between pb-2 border-b border-slate-800 text-xs">
            <span className="font-bold text-white flex items-center gap-1.5">
              <Filter className="w-3.5 h-3.5 text-sky-400" />
              <span>Drill Filters & Options</span>
            </span>
            {onOpenSettings && (
              <button
                onClick={onOpenSettings}
                className="text-sky-400 hover:text-white text-xs underline flex items-center gap-1"
              >
                <SettingsIcon className="w-3 h-3" />
                <span>Full Settings Tab →</span>
              </button>
            )}
          </div>

          <div className="flex flex-wrap items-center gap-2">
            {/* Rating Filter */}
            <div className="flex items-center gap-1.5 px-2.5 py-1 rounded-xl bg-slate-900 border border-slate-700 text-xs">
              <span className="text-slate-400 text-[11px]">Rating:</span>
              <select
                value={ratingFilter}
                onChange={(e) => {
                  const val = e.target.value as RatingFilterOption;
                  setRatingFilter(val);
                  applyFilter(hideLearned, dueOnly, hideExcluded, val);
                }}
                className="bg-transparent text-slate-200 text-xs font-semibold focus:outline-none cursor-pointer"
              >
                <option value="all" className="bg-slate-900 text-slate-200">All Ratings</option>
                <option value="again" className="bg-slate-900 text-rose-300">Again (1)</option>
                <option value="hard" className="bg-slate-900 text-amber-300">Hard (2)</option>
                <option value="good" className="bg-slate-900 text-sky-300">Good (3)</option>
                <option value="easy" className="bg-slate-900 text-emerald-300">Easy (4)</option>
                <option value="new" className="bg-slate-900 text-slate-300">New / Unrated</option>
              </select>
            </div>

            {/* Hide Learned Toggle */}
            <button
              type="button"
              onClick={() => {
                const nextVal = !hideLearned;
                setHideLearned(nextVal);
                setUserStudyPreferences({ hideLearned: nextVal }, activeUser.id);
                applyFilter(nextVal, dueOnly, hideExcluded, ratingFilter);
              }}
              className={`px-2.5 py-1 rounded-xl border text-xs font-semibold flex items-center gap-1 transition-all ${
                hideLearned
                  ? 'bg-emerald-950/80 border-emerald-500/40 text-emerald-400'
                  : 'bg-slate-900 border-slate-700 text-slate-400 hover:text-white'
              }`}
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
              className={`px-2.5 py-1 rounded-xl border text-xs font-semibold flex items-center gap-1 transition-all ${
                hideExcluded
                  ? 'bg-rose-950/80 border-rose-500/40 text-rose-400'
                  : 'bg-slate-900 border-slate-700 text-slate-400 hover:text-white'
              }`}
            >
              <Ban className="w-3.5 h-3.5" />
              <span>Hide Ignored</span>
            </button>

            {/* Due Only Toggle */}
            <button
              type="button"
              onClick={() => {
                const nextVal = !dueOnly;
                setDueOnly(nextVal);
                applyFilter(hideLearned, nextVal, hideExcluded, ratingFilter);
              }}
              className={`px-2.5 py-1 rounded-xl border text-xs font-semibold flex items-center gap-1 transition-all ${
                dueOnly
                  ? 'bg-amber-950/80 border-amber-500/40 text-amber-400'
                  : 'bg-slate-900 border-slate-700 text-slate-400 hover:text-white'
              }`}
            >
              <Clock className="w-3.5 h-3.5" />
              <span>SRS Due Only</span>
            </button>

            {/* Tonos Stress Highlight Toggle */}
            <button
              type="button"
              onClick={() => {
                const nextVal = !highlightTonos;
                setHighlightTonos(nextVal);
                setUserStudyPreferences({ highlightTonos: nextVal }, activeUser.id);
              }}
              className={`px-2.5 py-1 rounded-xl border text-xs font-semibold flex items-center gap-1 transition-all ${
                highlightTonos
                  ? 'bg-amber-500/20 text-amber-300 border-amber-500/40'
                  : 'bg-slate-900 border-slate-700 text-slate-400 hover:text-white'
              }`}
              title="Highlight stressed vowels with tones"
            >
              <span>Tonos: {highlightTonos ? 'ON' : 'OFF'}</span>
            </button>
          </div>
        </div>
      )}

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

      {/* Progress Bar (Auto-scrolled into view on deck selection) */}
      <div 
        ref={progressBarRef}
        className="scroll-mt-20 w-full h-2 bg-slate-800 rounded-full overflow-hidden shadow-inner !mt-2 sm:!mt-2.5"
      >
        <div
          className="h-full bg-sky-500 transition-all duration-300 ease-out"
          style={{ width: `${((currentIndex + 1) / filteredCards.length) * 100}%` }}
        />
      </div>

      {/* 3D Flashcard Flip Container */}
      <div className="perspective-1000 !mt-2 sm:!mt-2.5 py-0.5">
        <div
          onClick={handleFlip}
          onTouchStart={handleTouchStart}
          onTouchEnd={handleTouchEnd}
          className={`relative w-full h-[430px] sm:h-[475px] min-h-[430px] sm:min-h-[475px] rounded-3xl cursor-pointer transition-transform duration-500 transform-style-3d select-none shadow-2xl ${
            isFlipped ? 'rotate-y-180' : ''
          }`}
        >
          {/* ================= CARD FRONT ================= */}
          <div className="absolute inset-0 w-full h-full rounded-3xl p-5 sm:p-7 flex flex-col justify-between backface-hidden glass-card border border-sky-500/25 bg-gradient-to-b from-slate-900/95 via-slate-900/90 to-slate-950 shadow-2xl shadow-sky-950/30 overflow-hidden">
            {/* Top Bar on Front: Word Info (Gender / POS) on Left, Rating Badge on Right */}
            <div className="h-8 shrink-0 flex items-center justify-between gap-3 w-full select-none">
              {/* Word info (Gender / Part of Speech) - Ample room with no truncation */}
              <div className="flex items-center gap-2 min-w-0 flex-1">
                {currentCard.gender_or_pos ? (
                  <span className="text-xs font-semibold px-3 py-0.5 rounded-full bg-slate-800/90 text-sky-300 border border-slate-700/80 shadow-sm whitespace-nowrap">
                    {currentCard.gender_or_pos}
                  </span>
                ) : (
                  <span className="h-6 inline-block" />
                )}
              </div>

              {/* SRS Rating Badge & Presentation Count */}
              <div className="flex items-center gap-1.5 shrink-0">
                {timesPresented > 0 && (
                  <span
                    className="text-[10px] font-semibold px-2 py-0.5 rounded-full bg-slate-800/90 text-slate-300 border border-slate-700/80 flex items-center gap-1 shadow-sm whitespace-nowrap"
                    title={`This card has been presented ${timesPresented} time${timesPresented === 1 ? '' : 's'}`}
                  >
                    <Eye className="w-3 h-3 text-sky-400" />
                    <span>{timesPresented}x</span>
                  </span>
                )}
                {ratingStatus && ratingStatus !== 'new' && (
                  <span className={`text-[10px] font-bold px-2.5 py-0.5 rounded-full border shadow-sm uppercase shrink-0 whitespace-nowrap ${
                    ratingStatus === 'again'
                      ? 'bg-rose-950/90 text-rose-300 border-rose-700/60'
                      : ratingStatus === 'hard'
                      ? 'bg-amber-950/90 text-amber-300 border-amber-700/60'
                      : ratingStatus === 'good'
                      ? 'bg-sky-950/90 text-sky-300 border-sky-700/60'
                      : 'bg-emerald-950/90 text-emerald-300 border-emerald-700/60'
                  }`}>
                    {ratingStatus}
                  </span>
                )}
              </div>
            </div>

            {/* Prompt Content */}
            <div className="flex-1 min-h-0 flex flex-col justify-center items-center text-center py-1 sm:py-2 space-y-2.5 sm:space-y-3.5 my-auto w-full overflow-y-auto">
              {studyDirection === 'greek_to_english' ? (
                <h2 className="text-3xl sm:text-4xl md:text-5xl font-extrabold text-white tracking-wide font-serif leading-tight drop-shadow-sm px-2">
                  {renderGreekWithTonos(currentCard.greek, highlightTonos)}
                </h2>
              ) : (
                <>
                  <div className="space-y-1">
                    <span className="text-[10px] font-bold uppercase tracking-wider text-sky-400 px-2.5 py-0.5 rounded-full bg-sky-950/70 border border-sky-800/60 inline-flex items-center gap-1">
                      Translate to Greek
                    </span>
                    <h2 className="text-2xl sm:text-3xl md:text-4xl font-bold text-white tracking-tight leading-tight px-2">
                      {sanitizeEnglishPrompt(currentCard.english)}
                    </h2>
                  </div>

                  {/* On-demand 3-Step Production Hint for English -> Greek */}
                  <div className="mt-1 flex flex-col items-center gap-1.5 select-none w-full">
                    {hintStep === 0 || !productionHint ? (
                      <button
                        type="button"
                        onClick={(e) => {
                          e.stopPropagation();
                          setHintStep(1);
                        }}
                        className="inline-flex items-center gap-1.5 px-3 py-1 rounded-xl text-xs font-semibold border transition-all bg-slate-800/80 hover:bg-slate-700 text-slate-400 hover:text-amber-300 border-slate-700/80 shadow-sm"
                        title="Show Hint (Shortcut: H)"
                      >
                        <Lightbulb className="w-3.5 h-3.5 text-amber-400" />
                        <span>Need a Hint? [H]</span>
                      </button>
                    ) : (
                      <div 
                        className="flex flex-col items-center gap-2 animate-fadeIn w-full max-w-lg pt-1 select-none"
                        onClick={(e) => e.stopPropagation()}
                      >
                        {/* Stepper Header Bar */}
                        <div className="flex items-center justify-between w-full px-1 gap-2">
                          {/* 3 Step Pill Tabs */}
                          <div className="flex items-center gap-1">
                            {[
                              { step: 1, label: '1 • First Letters' },
                              { step: 2, label: '2 • More Letters' },
                              { step: 3, label: '3 • Sounds & Notes' },
                            ].map((item) => (
                              <button
                                key={item.step}
                                type="button"
                                onClick={() => setHintStep(item.step)}
                                className={`px-2 py-0.5 rounded-lg text-[10px] sm:text-[11px] font-semibold transition-all ${
                                  hintStep === item.step
                                    ? 'bg-amber-500/20 text-amber-300 border border-amber-500/50 shadow-sm'
                                    : 'bg-slate-800/60 text-slate-400 hover:text-slate-200 border border-slate-700/50'
                                }`}
                              >
                                {item.label}
                              </button>
                            ))}
                          </div>

                          {/* Next / Hide button & Close X */}
                          <div className="flex items-center gap-1 shrink-0">
                            <button
                              type="button"
                              onClick={() => setHintStep((prev) => (prev >= 3 ? 0 : prev + 1))}
                              className="inline-flex items-center gap-1 px-2 py-0.5 rounded-lg text-[10px] sm:text-[11px] font-semibold bg-slate-800 hover:bg-slate-700 text-amber-300 border border-slate-700 transition-colors"
                              title="Next Hint or Hide (Shortcut: H)"
                            >
                              <Lightbulb className="w-3 h-3 text-amber-400" />
                              <span>{hintStep < 3 ? 'Next [H]' : 'Hide [H]'}</span>
                            </button>
                            <button
                              type="button"
                              onClick={() => setHintStep(0)}
                              className="p-1 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800 transition-colors"
                              title="Close Hint"
                            >
                              <X className="w-3.5 h-3.5" />
                            </button>
                          </div>
                        </div>

                        {/* Hint Content Box */}
                        <div className="w-full p-2.5 rounded-xl bg-slate-900/90 border border-amber-500/30 shadow-lg flex flex-col items-center gap-1.5">
                          {/* Compact Grammar Tag */}
                          {productionHint.grammarClue && (
                            <span className="px-2 py-0.5 rounded-full bg-slate-800/80 text-sky-300 border border-slate-700 text-[10px] font-mono tracking-wide">
                              {productionHint.grammarClue}
                            </span>
                          )}

                          {/* Word-by-word Mask Display */}
                          <div className="font-mono text-sm sm:text-base text-amber-300 tracking-wider text-center select-text px-3 py-1.5 bg-black/40 rounded-lg border border-amber-900/40 w-full break-words">
                            {hintStep === 1 && productionHint.step1Mask}
                            {hintStep === 2 && productionHint.step2Mask}
                            {hintStep === 3 && (productionHint.step3Mask || productionHint.step2Mask)}
                          </div>

                          {/* Step 3: Phonetic Pronunciation Guide */}
                          {hintStep === 3 && productionHint.phoneticHint && (
                            <div className="flex items-center gap-1.5 text-xs text-sky-300 font-mono bg-sky-950/60 px-2.5 py-1 rounded-lg border border-sky-800/50">
                              <Volume2 className="w-3.5 h-3.5 text-sky-400 shrink-0" />
                              <span>/{productionHint.phoneticHint}/</span>
                            </div>
                          )}

                          {/* Study Notes Peek */}
                          {currentCard.notes && (
                            <div className="w-full text-center pt-1 border-t border-slate-800/80">
                              {!showNotesPeek ? (
                                <button
                                  type="button"
                                  onClick={() => setShowNotesPeek(true)}
                                  className="text-[11px] text-slate-400 hover:text-sky-300 underline underline-offset-2 transition-colors"
                                >
                                  Peek study notes (may spoil answer)
                                </button>
                              ) : (
                                <p className="text-xs text-slate-300 italic text-center bg-slate-950/60 p-2 rounded-lg border border-slate-800 leading-relaxed">
                                  {currentCard.notes}
                                </p>
                              )}
                            </div>
                          )}
                        </div>
                      </div>
                    )}
                  </div>
                </>
              )}
            </div>

            {/* Bottom Bar on Front: Ignore on Bottom Left, Learned on Bottom Right */}
            <div className="h-8 shrink-0 flex items-center justify-between gap-2 w-full select-none">
              {/* Bottom Left: Ignore Button */}
              <button
                type="button"
                onClick={(e) => {
                  e.stopPropagation();
                  handleToggleExcluded();
                }}
                className={`h-7 sm:h-8 px-2.5 sm:px-3 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition-all z-10 border shadow-sm whitespace-nowrap shrink-0 ${
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

              {/* Bottom Right: Learned Button */}
              <button
                type="button"
                onClick={(e) => {
                  e.stopPropagation();
                  handleToggleLearned();
                }}
                className={`h-7 sm:h-8 px-2.5 sm:px-3 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition-all z-10 border shadow-sm whitespace-nowrap shrink-0 ${
                  srsData?.isLearned
                    ? 'bg-teal-600/90 text-white border-teal-400/80 shadow-teal-600/30 ring-1 ring-teal-400/40'
                    : 'bg-slate-800/80 hover:bg-teal-950/80 text-slate-300 hover:text-teal-300 border-slate-700/80 hover:border-teal-500/40 backdrop-blur-sm'
                }`}
                title="Mark card as learned (Shortcut: M)"
              >
                <CheckCircle className="w-3.5 h-3.5 shrink-0" />
                <span>{srsData?.isLearned ? 'Learned' : 'Learn'}</span>
                <span className="text-[10px] opacity-75 font-mono hidden sm:inline">[M]</span>
              </button>
            </div>
          </div>

          {/* ================= CARD BACK (REVEAL) ================= */}
          <div className="absolute inset-0 w-full h-full rounded-3xl p-5 sm:p-7 flex flex-col justify-between backface-hidden rotate-y-180 glass-card border border-teal-500/30 bg-gradient-to-b from-slate-900/95 via-slate-900/90 to-slate-950 shadow-2xl shadow-teal-950/30 overflow-hidden">
            {/* Top Bar on Back: Word Info (Gender / POS) on Left, Rating Badge on Right */}
            <div className="h-8 shrink-0 flex items-center justify-between gap-3 w-full select-none">
              {/* Word info (Gender / Part of Speech) - Ample room with no truncation */}
              <div className="flex items-center gap-2 min-w-0 flex-1">
                {currentCard.gender_or_pos ? (
                  <span className="text-xs font-semibold px-3 py-0.5 rounded-full bg-slate-800/90 text-sky-300 border border-slate-700/80 shadow-sm whitespace-nowrap">
                    {currentCard.gender_or_pos}
                  </span>
                ) : (
                  <span className="h-6 inline-block" />
                )}
              </div>

              {/* SRS Rating Badge & Presentation Count */}
              <div className="flex items-center gap-1.5 shrink-0">
                {timesPresented > 0 && (
                  <span
                    className="text-[10px] font-semibold px-2 py-0.5 rounded-full bg-slate-800/90 text-slate-300 border border-slate-700/80 flex items-center gap-1 shadow-sm whitespace-nowrap"
                    title={`This card has been presented ${timesPresented} time${timesPresented === 1 ? '' : 's'}`}
                  >
                    <Eye className="w-3 h-3 text-sky-400" />
                    <span>{timesPresented}x</span>
                  </span>
                )}
                {ratingStatus && ratingStatus !== 'new' && (
                  <span className={`text-[10px] font-bold px-2.5 py-0.5 rounded-full border shadow-sm uppercase shrink-0 whitespace-nowrap ${
                    ratingStatus === 'again'
                      ? 'bg-rose-950/90 text-rose-300 border-rose-700/60'
                      : ratingStatus === 'hard'
                      ? 'bg-amber-950/90 text-amber-300 border-amber-700/60'
                      : ratingStatus === 'good'
                      ? 'bg-sky-950/90 text-sky-300 border-sky-700/60'
                      : 'bg-emerald-950/90 text-emerald-300 border-emerald-700/60'
                  }`}>
                    {ratingStatus}
                  </span>
                )}
              </div>
            </div>

            {/* Answer Content */}
            <div className="flex-1 min-h-0 flex flex-col justify-center items-center text-center py-1 sm:py-2 space-y-2 sm:space-y-2.5 my-auto w-full overflow-y-auto">
              {studyDirection === 'greek_to_english' ? (
                <>
                  <h2 className="text-2xl sm:text-3xl md:text-4xl font-extrabold text-teal-300 tracking-wide font-serif leading-tight px-2">
                    {renderGreekWithTonos(currentCard.greek, highlightTonos)}
                  </h2>
                  <h3 className="text-lg sm:text-xl md:text-2xl font-bold text-white tracking-tight px-2">
                    {currentCard.english}
                  </h3>
                  {currentCard.phonetic_hint && (
                    <div className="inline-block px-2.5 py-0.5 rounded-lg bg-slate-800/80 border border-slate-700/70 text-xs sm:text-sm font-mono text-teal-300">
                      /{currentCard.phonetic_hint}/
                    </div>
                  )}
                  {renderExamples(currentCard)}
                  {currentCard.notes && (
                    <p className="text-[11px] sm:text-xs text-slate-300 max-w-lg w-full mx-auto italic bg-slate-800/40 p-2 rounded-xl border border-slate-700/50">
                      {currentCard.notes}
                    </p>
                  )}
                </>
              ) : (
                <>
                  <h2 className="text-2xl sm:text-3xl md:text-4xl font-extrabold text-teal-300 tracking-wide font-serif leading-tight px-2">
                    {renderGreekWithTonos(currentCard.greek, highlightTonos)}
                  </h2>
                  <h3 className="text-base sm:text-lg font-semibold text-slate-300 tracking-tight px-2">
                    {sanitizeEnglishPrompt(currentCard.english)}
                  </h3>
                  {currentCard.phonetic_hint && (
                    <div className="inline-block px-2.5 py-0.5 rounded-lg bg-slate-800/80 border border-slate-700 text-xs sm:text-sm font-mono text-teal-300">
                      /{currentCard.phonetic_hint}/
                    </div>
                  )}
                  {/* Grammatical Highlights (Plural / Rubric form / Verb Type) */}
                  {currentCard.grammatical_info && (
                    <div className="flex flex-wrap items-center justify-center gap-1.5 text-xs text-slate-300 max-w-lg mx-auto pt-0.5">
                      {currentCard.grammatical_info.plural && (
                        <span className="px-2 py-0.5 rounded-md bg-slate-800/90 border border-slate-700/80 text-teal-300 font-serif text-[11px] sm:text-xs">
                          Plural: {currentCard.grammatical_info.plural}
                        </span>
                      )}
                      {currentCard.grammatical_info.imperative_formal && (
                        <span className="px-2 py-0.5 rounded-md bg-slate-800/90 border border-slate-700/80 text-sky-300 font-serif text-[11px] sm:text-xs">
                          Rubric: {currentCard.grammatical_info.imperative_formal}
                        </span>
                      )}
                      {currentCard.grammatical_info.verb_type && (
                        <span className="px-2 py-0.5 rounded-md bg-slate-800/90 border border-slate-700/80 text-amber-300 text-[11px] sm:text-xs">
                          {currentCard.grammatical_info.verb_type}
                        </span>
                      )}
                    </div>
                  )}
                  {renderExamples(currentCard)}
                  {currentCard.notes && (
                    <p className="text-[11px] sm:text-xs text-slate-300 max-w-lg w-full mx-auto italic bg-slate-800/40 p-2 rounded-xl border border-slate-700/50">
                      {currentCard.notes}
                    </p>
                  )}
                </>
              )}
            </div>

            {/* Bottom Bar on Back: Ignore on Bottom Left, Learned on Bottom Right */}
            <div className="h-8 shrink-0 flex items-center justify-between gap-2 w-full select-none">
              {/* Bottom Left: Ignore Button */}
              <button
                type="button"
                onClick={(e) => {
                  e.stopPropagation();
                  handleToggleExcluded();
                }}
                className={`h-7 sm:h-8 px-2.5 sm:px-3 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition-all z-10 border shadow-sm whitespace-nowrap shrink-0 ${
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

              {/* Bottom Right: Learned Button */}
              <button
                type="button"
                onClick={(e) => {
                  e.stopPropagation();
                  handleToggleLearned();
                }}
                className={`h-7 sm:h-8 px-2.5 sm:px-3 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition-all z-10 border shadow-sm whitespace-nowrap shrink-0 ${
                  srsData?.isLearned
                    ? 'bg-teal-600/90 text-white border-teal-400/80 shadow-teal-600/30 ring-1 ring-teal-400/40'
                    : 'bg-slate-800/80 hover:bg-teal-950/80 text-slate-300 hover:text-teal-300 border-slate-700/80 hover:border-teal-500/40 backdrop-blur-sm'
                }`}
                title="Mark card as learned (Shortcut: M)"
              >
                <CheckCircle className="w-3.5 h-3.5 shrink-0" />
                <span>{srsData?.isLearned ? 'Learned' : 'Learn'}</span>
                <span className="text-[10px] opacity-75 font-mono hidden sm:inline">[M]</span>
              </button>
            </div>
          </div>
        </div>
      </div>

      {/* ========================================================================= */}
      {/* Bottom Button Rows: Assessment (Row 1) & Navigation (Row 2)              */}
      {/* ========================================================================= */}
      <div 
        className="space-y-[14px] sm:space-y-4 !mt-[42px]" 
        style={{ marginTop: '42px' }}
      >
        {/* ROW 1: Card Assessment & SRS Rating Controls (Equal Sized 4-Button Row) */}
        <div 
          id="study-row-1-assessment" 
          data-testid="study-row-1-assessment"
          className="grid grid-cols-4 gap-2 sm:gap-3"
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

        {/* ROW 2: Navigation & Playback Controls (Equal Sized 4-Button Row) */}
        <div 
          id="study-row-2-navigation" 
          data-testid="study-row-2-navigation"
          className="grid grid-cols-4 gap-2 sm:gap-3"
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
            disabled={!audioSrc}
            className={`h-12 sm:h-13 w-full inline-flex items-center justify-center gap-1 sm:gap-2 px-2 sm:px-4 rounded-2xl border font-semibold text-xs sm:text-sm transition-all hover:scale-[1.02] active:scale-95 shadow-sm ${
              !audioSrc
                ? 'bg-slate-900/50 text-slate-600 border-slate-800/80 cursor-not-allowed opacity-50'
                : isAudioPlaying
                ? 'bg-sky-500 text-white border-sky-400 shadow-lg shadow-sky-500/30'
                : 'bg-slate-800 hover:bg-slate-700 text-sky-300 border-slate-700'
            }`}
            title={audioSrc ? "Play Audio (↓ Down Arrow)" : "No audio available for this card"}
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

      {/* Deck Completion Modal (Offers status change when deck is completed from beginning to end) */}
      {showCompletionModal && (
        <div className="fixed inset-0 z-50 bg-slate-950/85 backdrop-blur-md flex items-center justify-center p-4">
          <div className="glass-panel p-6 sm:p-8 rounded-3xl max-w-lg w-full border border-sky-500/30 space-y-6 shadow-2xl text-center">
            <div className="w-16 h-16 rounded-3xl bg-emerald-500/15 border border-emerald-500/30 text-emerald-400 flex items-center justify-center mx-auto shadow-xl shadow-emerald-500/10">
              <Award className="w-8 h-8" />
            </div>

            <div className="space-y-1.5">
              <h3 className="text-2xl font-extrabold text-white tracking-tight">
                🎉 Lesson Completed!
              </h3>
              <p className="text-xs sm:text-sm text-slate-300">
                You've completed all {filteredCards.length} cards from beginning to end!
              </p>
            </div>

            {/* Offer to change status of that lesson */}
            <div className="p-4 rounded-2xl bg-slate-900/90 border border-slate-800 space-y-3 text-left">
              <div className="flex items-center justify-between">
                <span className="text-xs font-bold uppercase tracking-wider text-slate-400">
                  Lesson Mastery Status
                </span>
                <span className="text-xs font-bold text-sky-400">
                  {displayLessonLabel}
                </span>
              </div>

              {statusUpdateMessage && (
                <div className="p-2.5 rounded-xl bg-emerald-950/70 border border-emerald-500/40 text-emerald-300 text-xs flex items-center gap-2">
                  <Check className="w-4 h-4 text-emerald-400 shrink-0" />
                  <span>{statusUpdateMessage}</span>
                </div>
              )}

              <p className="text-xs text-slate-400">
                Update status for this lesson:
              </p>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
                {STATUS_OPTIONS.map((opt) => (
                  <button
                    key={opt.value}
                    type="button"
                    onClick={() => handleUpdateUnitStatus(opt.value)}
                    className={`p-2.5 rounded-xl text-xs font-semibold flex items-center gap-2 border transition-all text-left ${
                      currentUnitStatus === opt.value
                        ? opt.activeClasses
                        : 'bg-slate-800/80 hover:bg-slate-700/80 border-slate-700 text-slate-300'
                    }`}
                  >
                    <span>{opt.icon}</span>
                    <span className="font-bold">{opt.label}</span>
                    {opt.endIcon && <span>{opt.endIcon}</span>}
                    {currentUnitStatus === opt.value && (
                      <Check className="w-3.5 h-3.5 ml-auto text-current" />
                    )}
                  </button>
                ))}
              </div>
            </div>

            {/* Action Buttons */}
            <div className="flex flex-col sm:flex-row items-center justify-center gap-3 pt-1">
              <button
                type="button"
                onClick={() => {
                  setShowCompletionModal(false);
                  setCurrentIndex(0);
                  setIsFlipped(false);
                }}
                className="w-full sm:w-auto px-5 py-2.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold flex items-center justify-center gap-1.5 transition-all"
              >
                <RotateCw className="w-3.5 h-3.5" />
                <span>Restart Deck</span>
              </button>

              <button
                type="button"
                onClick={onExit}
                className="w-full sm:w-auto px-6 py-2.5 rounded-xl bg-sky-500 hover:bg-sky-400 text-white text-xs font-bold shadow-lg shadow-sky-500/25 transition-all"
              >
                Back to Dashboard
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

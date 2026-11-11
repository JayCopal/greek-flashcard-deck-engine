import { useState, useEffect, useMemo } from 'react';
import { DeckData, CardEntry } from './types/schema';
import { getUserStudyPreferences, initializePersistenceEngine, TextSizePreference, getActiveUser } from './utils/userStorage';
import { getAllSRSData, isCardDue } from './utils/srs';
import { Dashboard } from './components/Dashboard';
import { Practice } from './components/Practice';
import { OverviewStats } from './components/OverviewStats';
import { DeckEditor } from './components/DeckEditor';
import { StudySession } from './components/StudySession';
import { Help } from './components/Help';
import { Settings } from './components/Settings';
import { UserSelector } from './components/UserSelector';
import { 
  Layers, 
  BookOpen, 
  Play, 
  WifiOff,
  HelpCircle,
  Settings as SettingsIcon,
  Sparkles,
  Award
} from 'lucide-react';

interface BeforeInstallPromptEvent extends Event {
  prompt: () => Promise<void>;
  userChoice: Promise<{ outcome: 'accepted' | 'dismissed' }>;
}

type ActiveTab = 'dashboard' | 'practice' | 'overview' | 'editor' | 'study' | 'settings' | 'help';

export function App() {
  const [deck, setDeck] = useState<DeckData | null>(null);
  const [loading, setLoading] = useState(true);
  const [isOfflineMode, setIsOfflineMode] = useState(false);
  const [activeTab, setActiveTab] = useState<ActiveTab>('dashboard');

  // Study session state
  const [studyCards, setStudyCards] = useState<CardEntry[]>([]);
  const [studyTitle, setStudyTitle] = useState('Study Session');
  const [studyLessonNotes, setStudyLessonNotes] = useState<string | undefined>();
  const [studyLessonNumber, setStudyLessonNumber] = useState<string | undefined>();
  const [studyUnitId, setStudyUnitId] = useState<string | undefined>();
  const [studyLessonId, setStudyLessonId] = useState<string | undefined>();
  const [studyOptions, setStudyOptions] = useState<{ hideExcluded?: boolean; hideLearned?: boolean } | undefined>();

  // Editor jump state
  const [editorUnitId, setEditorUnitId] = useState<string | undefined>();
  const [editorLessonId, setEditorLessonId] = useState<string | undefined>();

  // PWA Install Prompt State
  const [installPrompt, setInstallPrompt] = useState<BeforeInstallPromptEvent | null>(null);
  const [isInstalled, setIsInstalled] = useState(false);

  // Theme & text size preferences
  const [themePreference, setThemePreference] = useState<'slate' | 'oled'>(
    () => getUserStudyPreferences().themePreference || 'slate'
  );
  const [textSizePreference, setTextSizePreference] = useState<TextSizePreference>(
    () => getUserStudyPreferences().textSizePreference || 'normal'
  );

  useEffect(() => {
    const root = document.documentElement;
    root.classList.remove('text-scale-normal', 'text-scale-large', 'text-scale-xlarge');
    root.classList.add(`text-scale-${textSizePreference}`);
  }, [textSizePreference]);

  useEffect(() => {
    const updateThemeAndPrefs = () => {
      const prefs = getUserStudyPreferences();
      setThemePreference(prefs.themePreference || 'slate');
      setTextSizePreference(prefs.textSizePreference || 'normal');
    };
    window.addEventListener('greek_deck_user_change', updateThemeAndPrefs);
    window.addEventListener('greek_deck_prefs_change', updateThemeAndPrefs);
    return () => {
      window.removeEventListener('greek_deck_user_change', updateThemeAndPrefs);
      window.removeEventListener('greek_deck_prefs_change', updateThemeAndPrefs);
    };
  }, []);

  // History & browser/hardware back button handling:
  // When a user is studying cards, pressing browser/hardware back goes to the landing page, not exiting the app!
  useEffect(() => {
    if (!window.history.state || !window.history.state.tab) {
      window.history.replaceState({ tab: 'dashboard' }, '');
    }

    const handlePopState = (e: PopStateEvent) => {
      if (activeTab === 'study') {
        setActiveTab('dashboard');
      } else {
        const targetTab: ActiveTab = e.state?.tab || 'dashboard';
        setActiveTab(targetTab);
      }
    };

    window.addEventListener('popstate', handlePopState);
    return () => window.removeEventListener('popstate', handlePopState);
  }, [activeTab]);

  const navigateToTab = (tab: ActiveTab) => {
    if (tab === activeTab) return;
    window.history.pushState({ tab }, '');
    setActiveTab(tab);
  };

  const handleBackToLanding = () => {
    if (window.history.state?.tab === 'study') {
      window.history.back();
      setTimeout(() => {
        setActiveTab('dashboard');
      }, 50);
    } else {
      setActiveTab('dashboard');
    }
  };

  useEffect(() => {
    const handler = (e: Event) => {
      e.preventDefault();
      setInstallPrompt(e as BeforeInstallPromptEvent);
    };

    const installedHandler = () => {
      setIsInstalled(true);
      setInstallPrompt(null);
    };

    if (window.matchMedia('(display-mode: standalone)').matches || (navigator as any).standalone) {
      setIsInstalled(true);
    }

    window.addEventListener('beforeinstallprompt', handler);
    window.addEventListener('appinstalled', installedHandler);

    return () => {
      window.removeEventListener('beforeinstallprompt', handler);
      window.removeEventListener('appinstalled', installedHandler);
    };
  }, []);

  const handleInstallClick = async () => {
    if (!installPrompt) return;
    await installPrompt.prompt();
    const choice = await installPrompt.userChoice;
    if (choice.outcome === 'accepted') {
      setIsInstalled(true);
    }
    setInstallPrompt(null);
  };

  // Fetch Deck Data from API or offline fallback
  const fetchDeck = async (forceBust = false) => {
    setLoading(true);
    try {
      // First attempt local backend API
      const res = await fetch(`/api/deck${forceBust ? `?t=${Date.now()}` : ''}`, {
        cache: forceBust ? 'no-cache' : 'default',
      });
      if (res.ok) {
        const data = await res.json();
        setDeck(data);
        setIsOfflineMode(false);
        setLoading(false);
        return;
      }
    } catch {
      // Ignore and try static bundle fallback
    }

    // Offline / Exported Static PWA Fallback
    try {
      const baseUrl = import.meta.env.BASE_URL.endsWith('/')
        ? import.meta.env.BASE_URL
        : `${import.meta.env.BASE_URL}/`;
      const url = `${baseUrl}data/deck.json${forceBust ? `?t=${Date.now()}` : ''}`;
      const fallbackRes = await fetch(url, { cache: forceBust ? 'no-cache' : 'default' });
      if (fallbackRes.ok) {
        const data = await fallbackRes.json();
        setDeck(data);
        setIsOfflineMode(true);
      }
    } catch {
      console.error('Could not load deck data from API or static deck.json');
    } finally {
      setLoading(false);
    }
  };

  const handleRefresh = async () => {
    setLoading(true);
    if ('serviceWorker' in navigator) {
      try {
        const regs = await navigator.serviceWorker.getRegistrations();
        for (const reg of regs) {
          await reg.update();
        }
      } catch {
        // ignore
      }
    }
    await fetchDeck(true);
  };

  useEffect(() => {
    initializePersistenceEngine();
    fetchDeck();
  }, []);

  const handleSelectLessonFromDashboard = (unitId: string, lessonId: string) => {
    setEditorUnitId(unitId);
    setEditorLessonId(lessonId);
    navigateToTab('editor');
  };

  const handleStartStudy = (
    cards: CardEntry[],
    title: string,
    lessonNotes?: string,
    lessonNumber?: string,
    options?: { hideExcluded?: boolean; hideLearned?: boolean },
    unitId?: string,
    lessonId?: string
  ) => {
    setStudyCards(cards);
    setStudyTitle(title);
    setStudyLessonNotes(lessonNotes);
    setStudyLessonNumber(lessonNumber);
    setStudyOptions(options);
    setStudyUnitId(unitId);
    setStudyLessonId(lessonId);
    window.history.pushState({ tab: 'study' }, '');
    setActiveTab('study');
  };

  // User profile and SRS due count tracking
  const [activeUser, setActiveUser] = useState(getActiveUser());
  const [srsVersion, setSrsVersion] = useState(0);

  useEffect(() => {
    const handleUserOrProgressChange = () => {
      setActiveUser(getActiveUser());
      setSrsVersion((v) => v + 1);
    };
    window.addEventListener('greek_deck_user_change', handleUserOrProgressChange);
    window.addEventListener('greek_deck_progress_change', handleUserOrProgressChange);
    return () => {
      window.removeEventListener('greek_deck_user_change', handleUserOrProgressChange);
      window.removeEventListener('greek_deck_progress_change', handleUserOrProgressChange);
    };
  }, []);

  const dueCardsCount = useMemo(() => {
    if (!deck) return 0;
    const srsMap = getAllSRSData(activeUser.id);
    const allCards = deck.units.flatMap((u) => u.lessons.flatMap((l) => l.entries));
    return allCards.filter((c) => {
      const srs = srsMap[c.id];
      if (!srs) return true;
      if (srs.isLearned || srs.isExcluded) return false;
      return isCardDue(srs);
    }).length;
  }, [deck, activeUser.id, srsVersion]);

  // Global keyboard shortcuts for tab navigation (1: Lessons, 2: Practice, 3: Stats, 4: Editor, 5: Settings, ?: Help)
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (
        e.target instanceof HTMLInputElement ||
        e.target instanceof HTMLTextAreaElement ||
        (e.target as HTMLElement)?.isContentEditable
      ) {
        return;
      }
      if (activeTab === 'study') return;

      if (e.key === '1') {
        navigateToTab('dashboard');
      } else if (e.key === '2') {
        navigateToTab('practice');
      } else if (e.key === '3') {
        navigateToTab('overview');
      } else if (e.key === '4' && !isOfflineMode) {
        navigateToTab('editor');
      } else if (e.key === '5') {
        navigateToTab('settings');
      } else if (e.key === '?') {
        navigateToTab('help');
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [activeTab, isOfflineMode]);

  return (
    <div className={`min-h-screen text-slate-100 flex flex-col w-full max-w-full overflow-x-hidden transition-colors duration-300 ${
      themePreference === 'oled' ? 'bg-black oled-theme' : 'bg-slate-950'
    }`}>
      {/* Top Navigation Bar */}
      <header className={`sticky top-0 z-50 bg-slate-950/85 backdrop-blur-xl border-b border-slate-800/80 px-3 sm:px-6 lg:px-8 ${activeTab === 'study' ? 'py-1.5 sm:py-2' : 'py-2 sm:py-2.5'} w-full transition-all shadow-lg shadow-black/20`}>
        <div className="max-w-6xl mx-auto flex items-center justify-between gap-3">
          {/* Logo / Brand */}
          <div 
            onClick={() => navigateToTab('dashboard')} 
            className="flex items-center gap-2.5 cursor-pointer group shrink-0"
            title="Go to Landing Page (1)"
          >
            <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-sky-500 via-indigo-600 to-purple-600 flex items-center justify-center shadow-md shadow-sky-500/25 group-hover:scale-105 group-hover:shadow-sky-500/40 transition-all">
              <span className="text-white font-serif font-black text-lg leading-none">Ω</span>
            </div>
            <div>
              <div className="flex items-center gap-1.5">
                <span className="font-extrabold text-white text-base tracking-tight group-hover:text-sky-300 transition-colors">
                  GreekDeck
                </span>
                <span className="text-[10px] font-extrabold px-1.5 py-0.5 rounded-md bg-sky-500/20 text-sky-300 border border-sky-500/30">
                  A1 • A2
                </span>
              </div>
              <p className="text-[10px] text-slate-400 font-medium hidden sm:block leading-none mt-0.5">
                Audio Engine & Flashcard System
              </p>
            </div>
          </div>

          {/* Center (Desktop): Segmented Navigation Pill Bar */}
          <nav className="hidden md:flex items-center bg-slate-900/90 border border-slate-800/90 p-1 rounded-2xl shadow-inner shadow-black/30">
            {/* Landing: Lessons */}
            <button
              onClick={() => navigateToTab('dashboard')}
              className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 ${
                activeTab === 'dashboard'
                  ? 'bg-gradient-to-r from-sky-500 to-indigo-600 text-white shadow-md shadow-sky-500/30 border border-sky-400/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800/70'
              }`}
              title="Lessons List & Curriculum Tracks (1)"
            >
              <Layers className="w-3.5 h-3.5" />
              <span>Lessons</span>
            </button>

            {/* Targeted Practice */}
            <button
              onClick={() => navigateToTab('practice')}
              className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 relative ${
                activeTab === 'practice'
                  ? 'bg-gradient-to-r from-sky-500 to-indigo-600 text-white shadow-md shadow-sky-500/30 border border-sky-400/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800/70'
              }`}
              title="Targeted SRS Practice (2)"
            >
              <Sparkles className={`w-3.5 h-3.5 ${activeTab === 'practice' ? 'text-amber-300' : 'text-amber-400'}`} />
              <span>Practice</span>
              {dueCardsCount > 0 && (
                <span className="px-1.5 py-0.2 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/40 text-[9px] font-extrabold ml-0.5">
                  {dueCardsCount}
                </span>
              )}
            </button>

            {/* Stats & Overview */}
            <button
              onClick={() => navigateToTab('overview')}
              className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 ${
                activeTab === 'overview'
                  ? 'bg-gradient-to-r from-sky-500 to-indigo-600 text-white shadow-md shadow-sky-500/30 border border-sky-400/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800/70'
              }`}
              title="Deck Statistics & Audio Health (3)"
            >
              <Award className={`w-3.5 h-3.5 ${activeTab === 'overview' ? 'text-emerald-300' : 'text-emerald-400'}`} />
              <span>Stats</span>
            </button>

            {/* Deck Editor */}
            <button
              onClick={() => navigateToTab('editor')}
              disabled={isOfflineMode}
              className={`px-3.5 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center gap-1.5 ${
                activeTab === 'editor'
                  ? 'bg-gradient-to-r from-sky-500 to-indigo-600 text-white shadow-md shadow-sky-500/30 border border-sky-400/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800/70'
              } disabled:opacity-40 disabled:hover:bg-transparent`}
              title={isOfflineMode ? 'Editor disabled in offline static bundle' : 'Author & Review TTS (4)'}
            >
              <BookOpen className="w-3.5 h-3.5" />
              <span>Deck Editor</span>
            </button>
          </nav>

          {/* Right Header Controls: Study CTA, Offline Pill, User Selector, Settings, Help */}
          <div className="flex items-center gap-2 shrink-0">
            {/* Quick Drill Study CTA Button (Desktop & Tablet) */}
            {deck && (
              <button
                onClick={() => {
                  const allCards = deck.units.flatMap(u => u.lessons.flatMap(l => l.entries));
                  handleStartStudy(allCards, deck.manifest.deck_title);
                }}
                className="hidden sm:flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-white shadow-md shadow-emerald-500/20 active:scale-95 transition-all"
                title="Start quick study drill of all flashcards"
              >
                <Play className="w-3.5 h-3.5 fill-current" />
                <span>Quick Study</span>
              </button>
            )}

            {/* Offline Status Pill */}
            {isOfflineMode && (
              <span 
                className="inline-flex items-center gap-1 text-[11px] font-semibold text-teal-400 bg-teal-950/80 px-2.5 py-1 rounded-xl border border-teal-800"
                title="PWA Offline Mode Active"
              >
                <WifiOff className="w-3.5 h-3.5" />
                <span className="hidden sm:inline">Offline</span>
              </span>
            )}

            {/* Learner Profile Selector */}
            <UserSelector />

            {/* Settings Tab Button */}
            <button
              onClick={() => navigateToTab('settings')}
              className={`p-2 rounded-xl text-xs font-semibold transition-all border ${
                activeTab === 'settings'
                  ? 'bg-sky-500 text-white border-sky-400 shadow-md shadow-sky-500/30'
                  : 'bg-slate-900 border-slate-800 hover:border-slate-700 text-slate-400 hover:text-white'
              }`}
              title="Settings & Audio Voices (5)"
            >
              <SettingsIcon className="w-4 h-4" />
            </button>

            {/* Help Tab Button (Desktop) */}
            <button
              onClick={() => navigateToTab('help')}
              className={`hidden sm:flex p-2 rounded-xl text-xs font-semibold transition-all border ${
                activeTab === 'help'
                  ? 'bg-sky-500 text-white border-sky-400 shadow-md shadow-sky-500/30'
                  : 'bg-slate-900 border-slate-800 hover:border-slate-700 text-slate-400 hover:text-white'
              }`}
              title="Help & Keyboard Shortcuts (?)"
            >
              <HelpCircle className="w-4 h-4" />
            </button>
          </div>
        </div>
      </header>

      {/* Main Body Content */}
      <main className={`flex-1 max-w-6xl w-full mx-auto p-4 sm:p-6 lg:p-8 ${activeTab !== 'study' ? 'pb-24 md:pb-12' : 'pb-8'}`}>
        {loading && !deck ? (
          <div className="py-24 text-center space-y-3">
            <div className="w-8 h-8 border-2 border-sky-500 border-t-transparent rounded-full animate-spin mx-auto" />
            <p className="text-sm text-slate-400">Loading Greek Deck from YAML files...</p>
          </div>
        ) : !deck ? (
          <div className="py-20 text-center space-y-4 max-w-md mx-auto">
            <h2 className="text-xl font-bold text-white">No Deck Found</h2>
            <p className="text-sm text-slate-400">
              Ensure the Python backend is running on port 8000 and that <code>content/manifest.yaml</code> exists.
            </p>
            <button
              onClick={() => handleRefresh()}
              className="px-4 py-2 rounded-xl bg-sky-500 text-white text-sm font-semibold"
            >
              Retry Connection
            </button>
          </div>
        ) : (
          <>
            {/* Landing page: current list of lessons ONLY */}
            {activeTab === 'dashboard' && (
              <Dashboard
                deck={deck}
                onSelectLesson={handleSelectLessonFromDashboard}
                onStartStudy={handleStartStudy}
                onRefresh={handleRefresh}
              />
            )}

            {/* Dedicated Targeted Practice tab */}
            {activeTab === 'practice' && (
              <Practice
                deck={deck}
                onStartStudy={handleStartStudy}
              />
            )}

            {/* Dedicated Overview & Stats tab */}
            {activeTab === 'overview' && (
              <OverviewStats
                deck={deck}
                onRefresh={handleRefresh}
              />
            )}

            {activeTab === 'editor' && (
              <DeckEditor
                deck={deck}
                initialUnitId={editorUnitId}
                initialLessonId={editorLessonId}
                isOfflineMode={isOfflineMode}
                isPwa={isOfflineMode || isInstalled}
                onBackToDashboard={() => navigateToTab('dashboard')}
                onRefresh={handleRefresh}
              />
            )}

            {activeTab === 'study' && (
              <StudySession
                cards={studyCards.length > 0 ? studyCards : deck.units.flatMap(u => u.lessons.flatMap(l => l.entries))}
                title={studyTitle}
                lessonNotes={studyLessonNotes}
                lessonNumber={studyLessonNumber}
                unitId={studyUnitId}
                lessonId={studyLessonId}
                initialHideExcluded={studyOptions?.hideExcluded}
                initialHideLearned={studyOptions?.hideLearned}
                onExit={handleBackToLanding}
                onOpenHelp={() => navigateToTab('help')}
                onOpenSettings={() => navigateToTab('settings')}
              />
            )}

            {activeTab === 'settings' && (
              <Settings
                isOfflineMode={isOfflineMode}
                onRefreshDeck={handleRefresh}
                loadingDeck={loading}
                installPrompt={installPrompt}
                isInstalled={isInstalled}
                onInstallApp={handleInstallClick}
                onGoToStudy={() => {
                  if (deck) {
                    const allCards = deck.units.flatMap(u => u.lessons.flatMap(l => l.entries));
                    handleStartStudy(allCards, deck.manifest.deck_title);
                  }
                }}
                onGoToDashboard={() => navigateToTab('dashboard')}
              />
            )}

            {activeTab === 'help' && (
              <Help
                onBackToDashboard={() => navigateToTab('dashboard')}
                onStartStudy={() => {
                  if (deck) {
                    const allCards = deck.units.flatMap(u => u.lessons.flatMap(l => l.entries));
                    handleStartStudy(allCards, deck.manifest.deck_title);
                  }
                }}
              />
            )}
          </>
        )}
      </main>

      {/* Mobile Bottom Navigation Dock */}
      {activeTab !== 'study' && (
        <div className="fixed bottom-0 left-0 right-0 z-50 md:hidden bg-slate-950/95 backdrop-blur-xl border-t border-slate-800/90 px-3 py-1.5 shadow-2xl shadow-black">
          <div className="flex items-center justify-around max-w-md mx-auto">
            {/* Lessons */}
            <button
              onClick={() => navigateToTab('dashboard')}
              className={`flex flex-col items-center justify-center py-1 px-2.5 rounded-xl transition-all ${
                activeTab === 'dashboard'
                  ? 'text-sky-400 font-bold'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <Layers className="w-5 h-5" />
              <span className="text-[10px] mt-0.5">Lessons</span>
            </button>

            {/* Practice */}
            <button
              onClick={() => navigateToTab('practice')}
              className={`flex flex-col items-center justify-center py-1 px-2.5 rounded-xl transition-all relative ${
                activeTab === 'practice'
                  ? 'text-amber-400 font-bold'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <Sparkles className="w-5 h-5" />
              <span className="text-[10px] mt-0.5">Practice</span>
              {dueCardsCount > 0 && (
                <span className="absolute top-1 right-2 w-2 h-2 rounded-full bg-amber-400 ring-2 ring-slate-950 animate-pulse" />
              )}
            </button>

            {/* Quick Study (Floating Center Action Button) */}
            <button
              onClick={() => {
                if (deck) {
                  const allCards = deck.units.flatMap(u => u.lessons.flatMap(l => l.entries));
                  handleStartStudy(allCards, deck.manifest.deck_title);
                }
              }}
              className="flex items-center justify-center -mt-5 w-11 h-11 rounded-2xl bg-gradient-to-tr from-emerald-500 via-teal-500 to-sky-500 text-white shadow-lg shadow-emerald-500/30 active:scale-95 transition-all border-2 border-slate-900"
              title="Study all cards"
            >
              <Play className="w-5 h-5 fill-current ml-0.5" />
            </button>

            {/* Stats */}
            <button
              onClick={() => navigateToTab('overview')}
              className={`flex flex-col items-center justify-center py-1 px-2.5 rounded-xl transition-all ${
                activeTab === 'overview'
                  ? 'text-emerald-400 font-bold'
                  : 'text-slate-400 hover:text-slate-200'
              }`}
            >
              <Award className="w-5 h-5" />
              <span className="text-[10px] mt-0.5">Stats</span>
            </button>

            {/* Deck Editor */}
            <button
              onClick={() => navigateToTab('editor')}
              disabled={isOfflineMode}
              className={`flex flex-col items-center justify-center py-1 px-2.5 rounded-xl transition-all ${
                activeTab === 'editor'
                  ? 'text-sky-400 font-bold'
                  : 'text-slate-400 hover:text-slate-200'
              } disabled:opacity-30`}
            >
              <BookOpen className="w-5 h-5" />
              <span className="text-[10px] mt-0.5">Editor</span>
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default App;

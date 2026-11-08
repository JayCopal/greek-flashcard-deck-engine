import { useState, useEffect } from 'react';
import { DeckData, CardEntry } from './types/schema';
import { getUserStudyPreferences, initializePersistenceEngine, TextSizePreference } from './utils/userStorage';
import { Dashboard } from './components/Dashboard';
import { Practice } from './components/Practice';
import { OverviewStats } from './components/OverviewStats';
import { DeckEditor } from './components/DeckEditor';
import { StudySession } from './components/StudySession';
import { Help } from './components/Help';
import { Settings } from './components/Settings';
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
    () => getUserStudyPreferences().textSizePreference || 'large'
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
      setTextSizePreference(prefs.textSizePreference || 'large');
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

  return (
    <div className={`min-h-screen text-slate-100 flex flex-col w-full max-w-full overflow-x-hidden transition-colors duration-300 ${
      themePreference === 'oled' ? 'bg-black oled-theme' : 'bg-slate-950'
    }`}>
      {/* Top Navigation Bar */}
      <header className={`sticky top-0 z-50 glass-panel border-b border-slate-800/80 px-3 sm:px-6 lg:px-8 ${activeTab === 'study' ? 'py-1.5 sm:py-2' : 'py-2 sm:py-3'} w-full transition-all`}>
        <div className="max-w-6xl mx-auto flex flex-wrap items-center justify-between gap-y-2 gap-x-2">
          {/* Logo / Brand */}
          <div 
            onClick={() => navigateToTab('dashboard')} 
            className="flex items-center gap-2 sm:gap-2.5 cursor-pointer group order-1 shrink-0"
            title="Go to Landing Page"
          >
            <div className="w-8 h-8 sm:w-9 sm:h-9 rounded-xl bg-gradient-to-tr from-sky-600 to-indigo-600 flex items-center justify-center shadow-md shadow-sky-500/20 group-hover:scale-105 transition-transform">
              <span className="text-white font-serif font-black text-base sm:text-lg">Ω</span>
            </div>
            <div>
              <div className="flex items-center gap-1.5">
                <span className="font-extrabold text-white text-sm sm:text-base tracking-tight">
                  GreekDeck
                </span>
                <span className="text-[9px] sm:text-[10px] font-bold px-1.5 py-0.5 rounded bg-sky-500/20 text-sky-400 border border-sky-500/30">
                  A1
                </span>
              </div>
              <p className="text-[10px] sm:text-[11px] text-slate-400 font-medium hidden sm:block leading-none mt-0.5">
                Audio Engine & PWA
              </p>
            </div>
          </div>

          {/* Right Header Area: Offline Status Pill */}
          <div className="flex items-center gap-1.5 order-2 md:order-3 shrink-0">
            {isOfflineMode && (
              <span 
                className="inline-flex items-center gap-1 text-[11px] font-semibold text-teal-400 bg-teal-950/80 px-2 sm:px-2.5 py-1 rounded-xl border border-teal-800"
                title="PWA Offline Mode Active"
              >
                <WifiOff className="w-3.5 h-3.5" />
                <span className="hidden sm:inline">Offline</span>
              </span>
            )}
          </div>

          {/* Nav Tabs */}
          <nav className="flex items-center justify-around sm:justify-start gap-1 sm:gap-1.5 order-3 md:order-2 w-full md:w-auto pt-0.5 md:pt-0 overflow-x-auto no-scrollbar">
            {/* Landing: Lessons */}
            <button
              onClick={() => navigateToTab('dashboard')}
              className={`flex-1 md:flex-initial px-2.5 sm:px-3 py-1.5 rounded-xl text-xs sm:text-sm font-semibold transition-all flex items-center justify-center gap-1.5 ${
                activeTab === 'dashboard'
                  ? 'bg-sky-500 text-white shadow-md shadow-sky-500/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
              title="Lessons List (Landing Page)"
            >
              <Layers className="w-4 h-4 shrink-0" />
              <span>Lessons</span>
            </button>

            {/* Targeted Practice */}
            <button
              onClick={() => navigateToTab('practice')}
              className={`flex-1 md:flex-initial px-2.5 sm:px-3 py-1.5 rounded-xl text-xs sm:text-sm font-semibold transition-all flex items-center justify-center gap-1.5 ${
                activeTab === 'practice'
                  ? 'bg-sky-500 text-white shadow-md shadow-sky-500/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
              title="Targeted Practice & SRS Reviews"
            >
              <Sparkles className="w-4 h-4 shrink-0 text-amber-400" />
              <span>Practice</span>
            </button>

            {/* Stats & Overview */}
            <button
              onClick={() => navigateToTab('overview')}
              className={`flex-1 md:flex-initial px-2.5 sm:px-3 py-1.5 rounded-xl text-xs sm:text-sm font-semibold transition-all flex items-center justify-center gap-1.5 ${
                activeTab === 'overview'
                  ? 'bg-sky-500 text-white shadow-md shadow-sky-500/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
              title="Deck Statistics & Audio Coverage"
            >
              <Award className="w-4 h-4 shrink-0 text-emerald-400" />
              <span>Stats</span>
            </button>

            {/* Study Drill */}
            <button
              onClick={() => {
                if (deck) {
                  const allCards = deck.units.flatMap(u => u.lessons.flatMap(l => l.entries));
                  handleStartStudy(allCards, deck.manifest.deck_title);
                }
              }}
              className={`flex-1 md:flex-initial px-2.5 sm:px-3 py-1.5 rounded-xl text-xs sm:text-sm font-semibold transition-all flex items-center justify-center gap-1.5 ${
                activeTab === 'study'
                  ? 'bg-sky-500 text-white shadow-md shadow-sky-500/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
              title="Start Study Session"
            >
              <Play className="w-4 h-4 fill-current shrink-0" />
              <span>Study</span>
            </button>

            {/* Deck Editor */}
            <button
              onClick={() => navigateToTab('editor')}
              disabled={isOfflineMode}
              className={`flex-1 md:flex-initial px-2.5 sm:px-3 py-1.5 rounded-xl text-xs sm:text-sm font-semibold transition-all flex items-center justify-center gap-1.5 ${
                activeTab === 'editor'
                  ? 'bg-sky-500 text-white shadow-md shadow-sky-500/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              } disabled:opacity-40 disabled:hover:bg-transparent`}
              title={isOfflineMode ? 'Editor disabled in offline static bundle' : 'Author & Review TTS'}
            >
              <BookOpen className="w-4 h-4 shrink-0" />
              <span>Deck Editor</span>
            </button>

            {/* Settings */}
            <button
              onClick={() => navigateToTab('settings')}
              className={`flex-1 md:flex-initial px-2.5 sm:px-3 py-1.5 rounded-xl text-xs sm:text-sm font-semibold transition-all flex items-center justify-center gap-1.5 ${
                activeTab === 'settings'
                  ? 'bg-sky-500 text-white shadow-md shadow-sky-500/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
              title="Settings & Learner Profiles"
            >
              <SettingsIcon className="w-4 h-4 shrink-0" />
              <span>Settings</span>
            </button>

            {/* Help */}
            <button
              onClick={() => navigateToTab('help')}
              className={`flex-1 md:flex-initial px-2.5 sm:px-3 py-1.5 rounded-xl text-xs sm:text-sm font-semibold transition-all flex items-center justify-center gap-1.5 ${
                activeTab === 'help'
                  ? 'bg-sky-500 text-white shadow-md shadow-sky-500/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
              title="Help & Keyboard Shortcuts"
            >
              <HelpCircle className="w-4 h-4 shrink-0" />
              <span>Help</span>
            </button>
          </nav>
        </div>
      </header>

      {/* Main Body Content */}
      <main className="flex-1 max-w-6xl w-full mx-auto p-4 sm:p-6 lg:p-8">
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
    </div>
  );
}

export default App;

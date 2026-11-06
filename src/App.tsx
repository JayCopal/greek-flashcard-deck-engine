import { useState, useEffect } from 'react';
import { DeckData, CardEntry } from './types/schema';
import { Dashboard } from './components/Dashboard';
import { DeckEditor } from './components/DeckEditor';
import { StudySession } from './components/StudySession';
import { Help } from './components/Help';
import { UserSelector } from './components/UserSelector';
import { 
  Layers, 
  BookOpen, 
  Play, 
  RefreshCw, 
  WifiOff,
  Download,
  HelpCircle
} from 'lucide-react';

interface BeforeInstallPromptEvent extends Event {
  prompt: () => Promise<void>;
  userChoice: Promise<{ outcome: 'accepted' | 'dismissed' }>;
}

type ActiveTab = 'dashboard' | 'editor' | 'study' | 'help';

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
    fetchDeck();
  }, []);

  const handleSelectLessonFromDashboard = (unitId: string, lessonId: string) => {
    setEditorUnitId(unitId);
    setEditorLessonId(lessonId);
    setActiveTab('editor');
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
    setActiveTab('study');
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col w-full max-w-full overflow-x-hidden">
      {/* Top Navigation Bar */}
      <header className="sticky top-0 z-50 glass-panel border-b border-slate-800/80 px-3 sm:px-6 lg:px-8 py-2.5 sm:py-3.5 w-full">
        <div className="max-w-6xl mx-auto flex flex-wrap items-center justify-between gap-y-2.5 gap-x-2">
          {/* Logo / Brand */}
          <div 
            onClick={() => setActiveTab('dashboard')} 
            className="flex items-center gap-2.5 sm:gap-3 cursor-pointer group order-1 shrink-0"
          >
            <div className="w-9 h-9 sm:w-10 sm:h-10 rounded-xl bg-gradient-to-tr from-sky-600 to-indigo-600 flex items-center justify-center shadow-lg shadow-sky-500/20 group-hover:scale-105 transition-transform">
              <span className="text-white font-serif font-black text-lg sm:text-xl">Ω</span>
            </div>
            <div>
              <div className="flex items-center gap-1.5 sm:gap-2">
                <span className="font-extrabold text-white text-sm sm:text-base tracking-tight">
                  GreekDeck
                </span>
                <span className="text-[9px] sm:text-[10px] font-bold px-1.5 py-0.5 rounded bg-sky-500/20 text-sky-400 border border-sky-500/30">
                  A1
                </span>
              </div>
              <p className="text-[11px] text-slate-400 font-medium hidden sm:block">
                Local-First Audio Engine & PWA
              </p>
            </div>
          </div>

          {/* Right Header Area: PWA Install, Learner Profiles & Mode */}
          <div className="flex items-center gap-1.5 sm:gap-2 order-2 md:order-3 shrink-0">
            {installPrompt && !isInstalled && (
              <button
                onClick={handleInstallClick}
                className="inline-flex items-center gap-1.5 px-2.5 sm:px-3 py-1.5 rounded-xl bg-gradient-to-r from-sky-500 to-indigo-600 hover:from-sky-400 hover:to-indigo-500 text-white text-xs font-bold shadow-md shadow-sky-500/20 transition-all hover:scale-105 active:scale-95"
                title="Install Progressive Web App on your device"
              >
                <Download className="w-3.5 h-3.5" />
                <span className="hidden sm:inline">Install App</span>
              </button>
            )}

            <UserSelector />

            {isOfflineMode && (
              <span 
                className="inline-flex items-center gap-1 text-[11px] font-semibold text-teal-400 bg-teal-950/80 px-2 sm:px-2.5 py-1.5 rounded-xl border border-teal-800"
                title="PWA Offline Mode Active"
              >
                <WifiOff className="w-3.5 h-3.5" />
                <span className="hidden md:inline">Offline</span>
              </span>
            )}
            <button
              onClick={handleRefresh}
              className="p-1.5 sm:p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white transition-colors border border-slate-700"
              title={isOfflineMode ? "Check for updates and reload deck data" : "Reload YAML from disk"}
            >
              <RefreshCw className={`w-4 h-4 ${loading ? 'animate-spin' : ''}`} />
            </button>
          </div>

          {/* Nav Tabs - Wraps gracefully below on mobile/PWA, centers inline on md+ */}
          <nav className="flex items-center justify-around sm:justify-start gap-1 sm:gap-2 order-3 md:order-2 w-full md:w-auto pt-1 md:pt-0">
            <button
              onClick={() => setActiveTab('dashboard')}
              className={`flex-1 md:flex-initial px-3 sm:px-4 py-1.5 sm:py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all flex items-center justify-center gap-1.5 ${
                activeTab === 'dashboard'
                  ? 'bg-sky-500 text-white shadow-md shadow-sky-500/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
            >
              <Layers className="w-4 h-4 shrink-0" />
              <span>Dashboard</span>
            </button>

            <button
              onClick={() => setActiveTab('editor')}
              disabled={isOfflineMode}
              className={`flex-1 md:flex-initial px-3 sm:px-4 py-1.5 sm:py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all flex items-center justify-center gap-1.5 ${
                activeTab === 'editor'
                  ? 'bg-sky-500 text-white shadow-md shadow-sky-500/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              } disabled:opacity-40 disabled:hover:bg-transparent`}
              title={isOfflineMode ? 'Editor disabled in offline static bundle' : 'Author & Review TTS'}
            >
              <BookOpen className="w-4 h-4 shrink-0" />
              <span>Deck Editor</span>
            </button>

            <button
              onClick={() => {
                if (deck) {
                  const allCards = deck.units.flatMap(u => u.lessons.flatMap(l => l.entries));
                  handleStartStudy(allCards, deck.manifest.deck_title);
                }
              }}
              className={`flex-1 md:flex-initial px-3 sm:px-4 py-1.5 sm:py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all flex items-center justify-center gap-1.5 ${
                activeTab === 'study'
                  ? 'bg-sky-500 text-white shadow-md shadow-sky-500/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
            >
              <Play className="w-4 h-4 fill-current shrink-0" />
              <span>Study</span>
            </button>

            <button
              onClick={() => setActiveTab('help')}
              className={`flex-1 md:flex-initial px-3 sm:px-4 py-1.5 sm:py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all flex items-center justify-center gap-1.5 ${
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
            {activeTab === 'dashboard' && (
              <Dashboard
                deck={deck}
                onSelectLesson={handleSelectLessonFromDashboard}
                onStartStudy={handleStartStudy}
                onRefresh={handleRefresh}
              />
            )}

            {activeTab === 'editor' && (
              <DeckEditor
                deck={deck}
                initialUnitId={editorUnitId}
                initialLessonId={editorLessonId}
                onBackToDashboard={() => setActiveTab('dashboard')}
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
                onExit={() => setActiveTab('dashboard')}
                onOpenHelp={() => setActiveTab('help')}
              />
            )}

            {activeTab === 'help' && (
              <Help
                onBackToDashboard={() => setActiveTab('dashboard')}
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

      {/* Subtle Footer */}
      <footer className="border-t border-slate-900 py-4 px-6 text-center text-xs text-slate-500 flex flex-wrap items-center justify-center gap-x-4 gap-y-2">
        <span>Modern Greek Deck Engine • Multi-User Local Storage • High-Fidelity Native Audio</span>
        <button
          onClick={() => setActiveTab('help')}
          className="text-slate-400 hover:text-sky-400 underline underline-offset-2 transition-colors"
        >
          Help & Keyboard Shortcuts
        </button>
      </footer>
    </div>
  );
}
export default App;

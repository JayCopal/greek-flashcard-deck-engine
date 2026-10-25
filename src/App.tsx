import { useState, useEffect } from 'react';
import { DeckData, CardEntry } from './types/schema';
import { Dashboard } from './components/Dashboard';
import { DeckEditor } from './components/DeckEditor';
import { StudySession } from './components/StudySession';
import { UserSelector } from './components/UserSelector';
import { 
  Layers, 
  BookOpen, 
  Play, 
  RefreshCw, 
  WifiOff,
  Download
} from 'lucide-react';

interface BeforeInstallPromptEvent extends Event {
  prompt: () => Promise<void>;
  userChoice: Promise<{ outcome: 'accepted' | 'dismissed' }>;
}

type ActiveTab = 'dashboard' | 'editor' | 'study';

export function App() {
  const [deck, setDeck] = useState<DeckData | null>(null);
  const [loading, setLoading] = useState(true);
  const [isOfflineMode, setIsOfflineMode] = useState(false);
  const [activeTab, setActiveTab] = useState<ActiveTab>('dashboard');

  // Study session state
  const [studyCards, setStudyCards] = useState<CardEntry[]>([]);
  const [studyTitle, setStudyTitle] = useState('Study Session');
  const [studyLessonNotes, setStudyLessonNotes] = useState<string | undefined>();

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
  const fetchDeck = async () => {
    setLoading(true);
    try {
      // First attempt local backend API
      const res = await fetch('/api/deck');
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
      const fallbackRes = await fetch(`${baseUrl}data/deck.json`);
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

  useEffect(() => {
    fetchDeck();
  }, []);

  const handleSelectLessonFromDashboard = (unitId: string, lessonId: string) => {
    setEditorUnitId(unitId);
    setEditorLessonId(lessonId);
    setActiveTab('editor');
  };

  const handleStartStudy = (cards: CardEntry[], title: string, lessonNotes?: string) => {
    setStudyCards(cards);
    setStudyTitle(title);
    setStudyLessonNotes(lessonNotes);
    setActiveTab('study');
  };

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex flex-col">
      {/* Top Navigation Bar */}
      <header className="sticky top-0 z-50 glass-panel border-b border-slate-800/80 px-4 sm:px-8 py-3.5">
        <div className="max-w-6xl mx-auto flex items-center justify-between">
          {/* Logo / Brand */}
          <div 
            onClick={() => setActiveTab('dashboard')} 
            className="flex items-center gap-3 cursor-pointer group"
          >
            <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-sky-600 to-indigo-600 flex items-center justify-center shadow-lg shadow-sky-500/20 group-hover:scale-105 transition-transform">
              <span className="text-white font-serif font-black text-xl">Ω</span>
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-extrabold text-white text-base tracking-tight">
                  GreekDeck
                </span>
                <span className="text-[10px] font-bold px-1.5 py-0.5 rounded bg-sky-500/20 text-sky-400 border border-sky-500/30">
                  Chirp 3 HD
                </span>
              </div>
              <p className="text-[11px] text-slate-400 font-medium hidden sm:block">
                Local-First Audio Engine & PWA
              </p>
            </div>
          </div>

          {/* Nav Tabs */}
          <nav className="flex items-center gap-1 sm:gap-2">
            <button
              onClick={() => setActiveTab('dashboard')}
              className={`px-3 sm:px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all flex items-center gap-1.5 ${
                activeTab === 'dashboard'
                  ? 'bg-sky-500 text-white shadow-md shadow-sky-500/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
            >
              <Layers className="w-4 h-4" />
              <span>Dashboard</span>
            </button>

            <button
              onClick={() => setActiveTab('editor')}
              disabled={isOfflineMode}
              className={`px-3 sm:px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all flex items-center gap-1.5 ${
                activeTab === 'editor'
                  ? 'bg-sky-500 text-white shadow-md shadow-sky-500/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              } disabled:opacity-40 disabled:hover:bg-transparent`}
              title={isOfflineMode ? 'Editor disabled in offline static bundle' : 'Author & Review TTS'}
            >
              <BookOpen className="w-4 h-4" />
              <span>Deck Editor</span>
            </button>

            <button
              onClick={() => {
                if (deck) {
                  const allCards = deck.units.flatMap(u => u.lessons.flatMap(l => l.entries));
                  handleStartStudy(allCards, deck.manifest.deck_title);
                }
              }}
              className={`px-3 sm:px-4 py-2 rounded-xl text-xs sm:text-sm font-semibold transition-all flex items-center gap-1.5 ${
                activeTab === 'study'
                  ? 'bg-sky-500 text-white shadow-md shadow-sky-500/30'
                  : 'text-slate-400 hover:text-white hover:bg-slate-800'
              }`}
            >
              <Play className="w-4 h-4 fill-current" />
              <span>Study</span>
            </button>
          </nav>

          {/* Right Header Area: PWA Install, Learner Profiles & Mode */}
          <div className="flex items-center gap-2">
            {installPrompt && !isInstalled && (
              <button
                onClick={handleInstallClick}
                className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-gradient-to-r from-sky-500 to-indigo-600 hover:from-sky-400 hover:to-indigo-500 text-white text-xs font-bold shadow-md shadow-sky-500/20 transition-all hover:scale-105 active:scale-95"
                title="Install Progressive Web App on your device"
              >
                <Download className="w-3.5 h-3.5" />
                <span className="hidden sm:inline">Install App</span>
              </button>
            )}

            <UserSelector />

            {isOfflineMode ? (
              <span className="inline-flex items-center gap-1 text-[11px] font-semibold text-teal-400 bg-teal-950/80 px-2.5 py-1.5 rounded-xl border border-teal-800">
                <WifiOff className="w-3 h-3" />
                <span className="hidden md:inline">Offline</span>
              </span>
            ) : (
              <button
                onClick={fetchDeck}
                className="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white transition-colors border border-slate-700"
                title="Reload YAML from disk"
              >
                <RefreshCw className={`w-4 h-4 ${loading ? 'animate-spin' : ''}`} />
              </button>
            )}
          </div>
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
              onClick={fetchDeck}
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
                onRefresh={fetchDeck}
              />
            )}

            {activeTab === 'editor' && (
              <DeckEditor
                deck={deck}
                initialUnitId={editorUnitId}
                initialLessonId={editorLessonId}
                onBackToDashboard={() => setActiveTab('dashboard')}
                onRefresh={fetchDeck}
              />
            )}

            {activeTab === 'study' && (
              <StudySession
                cards={studyCards.length > 0 ? studyCards : deck.units.flatMap(u => u.lessons.flatMap(l => l.entries))}
                title={studyTitle}
                lessonNotes={studyLessonNotes}
                onExit={() => setActiveTab('dashboard')}
              />
            )}
          </>
        )}
      </main>

      {/* Subtle Footer */}
      <footer className="border-t border-slate-900 py-4 px-6 text-center text-xs text-slate-500">
        Modern Greek Deck Engine • Multi-User Local Storage • Powered by Google Cloud Chirp 3 HD
      </footer>
    </div>
  );
}
export default App;

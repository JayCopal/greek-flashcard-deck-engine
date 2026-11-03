import React from 'react';
import { 
  ArrowLeft, 
  Keyboard, 
  RotateCw, 
  Volume2, 
  ChevronLeft, 
  ChevronRight, 
  CheckCircle, 
  Ban, 
  Clock, 
  ArrowUpDown, 
  Sliders, 
  Users, 
  Download, 
  HelpCircle,
  Sparkles,
  BookOpen
} from 'lucide-react';

interface HelpProps {
  onBackToDashboard: () => void;
  onStartStudy?: () => void;
}

export const Help: React.FC<HelpProps> = ({ onBackToDashboard, onStartStudy }) => {
  return (
    <div className="max-w-4xl mx-auto space-y-8 pb-16">
      {/* Header Banner */}
      <div className="glass-panel p-6 sm:p-8 rounded-3xl relative overflow-hidden border border-sky-500/20 shadow-xl shadow-sky-950/20">
        <div className="absolute top-0 right-0 w-80 h-80 bg-gradient-to-br from-sky-500/10 via-indigo-500/10 to-transparent rounded-full blur-3xl pointer-events-none -mr-20 -mt-20" />
        
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 relative z-10">
          <div className="flex items-center gap-3.5">
            <button
              onClick={onBackToDashboard}
              className="p-2.5 rounded-2xl bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition-colors border border-slate-700 shadow-sm"
              title="Back to Dashboard"
            >
              <ArrowLeft className="w-5 h-5" />
            </button>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-xs uppercase font-extrabold text-sky-400 tracking-wider flex items-center gap-1.5">
                  <HelpCircle className="w-3.5 h-3.5" /> PWA User Manual
                </span>
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-sky-500/20 text-sky-300 border border-sky-500/30">
                  Version 1.0
                </span>
              </div>
              <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight mt-1">
                Help & Keyboard Shortcuts
              </h1>
            </div>
          </div>

          {onStartStudy && (
            <button
              onClick={onStartStudy}
              className="self-start sm:self-auto px-4 py-2.5 rounded-xl bg-gradient-to-r from-sky-500 to-indigo-600 hover:from-sky-400 hover:to-indigo-500 text-white text-xs font-bold shadow-lg shadow-sky-500/25 transition-all hover:scale-105 active:scale-95 flex items-center gap-2"
            >
              <BookOpen className="w-4 h-4" />
              <span>Resume Study</span>
            </button>
          )}
        </div>
      </div>

      {/* Primary Section: Keyboard Shortcuts */}
      <div className="space-y-4">
        <div className="flex items-center gap-2 text-slate-200 font-bold text-lg">
          <Keyboard className="w-5 h-5 text-sky-400" />
          <h2>Keyboard Shortcuts Reference</h2>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {/* Card Navigation */}
          <div className="glass-panel p-5 rounded-2xl border border-slate-800 space-y-4">
            <h3 className="text-xs font-bold text-sky-400 uppercase tracking-wider flex items-center gap-1.5">
              <RotateCw className="w-3.5 h-3.5" /> Card Navigation & Audio
            </h3>
            <ul className="space-y-3 text-sm">
              <li className="flex items-center justify-between text-slate-300 py-1 border-b border-slate-800/60">
                <span className="flex items-center gap-2">
                  <RotateCw className="w-4 h-4 text-sky-400" /> Flip Card (Front / Back)
                </span>
                <kbd className="px-2.5 py-1 rounded-lg bg-slate-800 border border-slate-700 text-sky-300 font-mono text-xs font-bold shadow-sm">
                  ↑ Up Arrow
                </kbd>
              </li>
              <li className="flex items-center justify-between text-slate-300 py-1 border-b border-slate-800/60">
                <span className="flex items-center gap-2">
                  <Volume2 className="w-4 h-4 text-sky-400" /> Play Native Audio
                </span>
                <kbd className="px-2.5 py-1 rounded-lg bg-slate-800 border border-slate-700 text-sky-300 font-mono text-xs font-bold shadow-sm">
                  ↓ Down Arrow
                </kbd>
              </li>
              <li className="flex items-center justify-between text-slate-300 py-1 border-b border-slate-800/60">
                <span className="flex items-center gap-2">
                  <ChevronLeft className="w-4 h-4 text-slate-400" /> Previous Card
                </span>
                <kbd className="px-2.5 py-1 rounded-lg bg-slate-800 border border-slate-700 text-slate-300 font-mono text-xs font-bold shadow-sm">
                  ← Left Arrow
                </kbd>
              </li>
              <li className="flex items-center justify-between text-slate-300 py-1">
                <span className="flex items-center gap-2">
                  <ChevronRight className="w-4 h-4 text-sky-400" /> Next Card
                </span>
                <kbd className="px-2.5 py-1 rounded-lg bg-slate-800 border border-slate-700 text-slate-300 font-mono text-xs font-bold shadow-sm">
                  → Right Arrow
                </kbd>
              </li>
            </ul>
          </div>

          {/* Quick Status Toggles */}
          <div className="glass-panel p-5 rounded-2xl border border-slate-800 space-y-4">
            <h3 className="text-xs font-bold text-teal-400 uppercase tracking-wider flex items-center gap-1.5">
              <CheckCircle className="w-3.5 h-3.5" /> Quick Status Toggles
            </h3>
            <ul className="space-y-3 text-sm">
              <li className="flex items-center justify-between text-slate-300 py-1 border-b border-slate-800/60">
                <span className="flex items-center gap-2">
                  <CheckCircle className="w-4 h-4 text-teal-400" /> Toggle Learned (Mastered)
                </span>
                <kbd className="px-2.5 py-1 rounded-lg bg-slate-800 border border-teal-500/40 text-teal-300 font-mono text-xs font-bold shadow-sm">
                  M
                </kbd>
              </li>
              <li className="flex items-center justify-between text-slate-300 py-1 border-b border-slate-800/60">
                <span className="flex items-center gap-2">
                  <Ban className="w-4 h-4 text-rose-400" /> Toggle Ignore (Exclude)
                </span>
                <kbd className="px-2.5 py-1 rounded-lg bg-slate-800 border border-rose-500/40 text-rose-300 font-mono text-xs font-bold shadow-sm">
                  X
                </kbd>
              </li>
              <li className="text-xs text-slate-400 leading-relaxed pt-1">
                Both buttons are conveniently located on the top left and top right of the front side of each flashcard for fast 1-click access.
              </li>
            </ul>
          </div>

          {/* Spaced Repetition SRS Ratings */}
          <div className="glass-panel p-5 rounded-2xl border border-slate-800 space-y-4 md:col-span-2">
            <h3 className="text-xs font-bold text-amber-400 uppercase tracking-wider flex items-center gap-1.5">
              <Clock className="w-3.5 h-3.5" /> Spaced Repetition (SRS) Assessment Keys
            </h3>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
              <div className="p-3.5 rounded-xl bg-rose-950/40 border border-rose-500/30 space-y-1.5">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-rose-300">Again</span>
                  <kbd className="px-2 py-0.5 rounded bg-rose-900/80 border border-rose-500/50 text-white font-mono text-xs font-bold">1</kbd>
                </div>
                <p className="text-xs text-slate-400">Total blackout / incorrect recall. Resets interval for urgent repetition.</p>
              </div>

              <div className="p-3.5 rounded-xl bg-amber-950/40 border border-amber-500/30 space-y-1.5">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-amber-300">Hard</span>
                  <kbd className="px-2 py-0.5 rounded bg-amber-900/80 border border-amber-500/50 text-white font-mono text-xs font-bold">2</kbd>
                </div>
                <p className="text-xs text-slate-400">Recalled with significant hesitation or effort. Increases interval slightly.</p>
              </div>

              <div className="p-3.5 rounded-xl bg-sky-950/40 border border-sky-500/30 space-y-1.5">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-sky-300">Good</span>
                  <kbd className="px-2 py-0.5 rounded bg-sky-900/80 border border-sky-500/50 text-white font-mono text-xs font-bold">3</kbd>
                </div>
                <p className="text-xs text-slate-400">Correct recall after normal delay. Standard optimal SRS interval progression.</p>
              </div>

              <div className="p-3.5 rounded-xl bg-emerald-950/40 border border-emerald-500/30 space-y-1.5">
                <div className="flex items-center justify-between">
                  <span className="text-xs font-bold text-emerald-300">Easy</span>
                  <kbd className="px-2 py-0.5 rounded bg-emerald-900/80 border border-emerald-500/50 text-white font-mono text-xs font-bold">4</kbd>
                </div>
                <p className="text-xs text-slate-400">Instant, effortless recall. Bonus interval multiplier applied.</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Secondary Section: Key Features & Study Tips */}
      <div className="space-y-4">
        <div className="flex items-center gap-2 text-slate-200 font-bold text-lg">
          <Sparkles className="w-5 h-5 text-indigo-400" />
          <h2>Core Features & Study Guide</h2>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {/* Smart Defaults & Filter Persistence */}
          <div className="glass-panel p-5 rounded-2xl border border-slate-800 space-y-2.5">
            <div className="flex items-center gap-2 text-sky-400 text-sm font-bold">
              <Sliders className="w-4 h-4" />
              <span>Smart Defaults & Remembered Settings</span>
            </div>
            <p className="text-xs text-slate-300 leading-relaxed">
              <strong>Hide Learned</strong> and <strong>Hide Ignored</strong> are enabled by default so your study sessions focus on words you need to learn. Once you adjust these toggles, your preference is automatically remembered for all subsequent lessons and sessions.
            </p>
          </div>

          {/* Study Direction */}
          <div className="glass-panel p-5 rounded-2xl border border-slate-800 space-y-2.5">
            <div className="flex items-center gap-2 text-teal-400 text-sm font-bold">
              <ArrowUpDown className="w-4 h-4" />
              <span>Two-Way Study Direction</span>
            </div>
            <p className="text-xs text-slate-300 leading-relaxed">
              Switch between <strong>Greek → English</strong> (listening & reading comprehension) and <strong>English → Greek</strong> (active production). Native audio plays automatically on card flip to anchor pronunciation.
            </p>
          </div>

          {/* Audio Engine */}
          <div className="glass-panel p-5 rounded-2xl border border-slate-800 space-y-2.5">
            <div className="flex items-center gap-2 text-purple-400 text-sm font-bold">
              <Volume2 className="w-4 h-4" />
              <span>Google Cloud Chirp 3 HD Audio</span>
            </div>
            <p className="text-xs text-slate-300 leading-relaxed">
              Every card is paired with high-fidelity native pronunciation powered by Google Cloud Chirp 3 HD. The speaker icon on the Greek side allows instant on-demand playback, and auto-play can be toggled on or off at any time.
            </p>
          </div>

          {/* Multi-User & Offline */}
          <div className="glass-panel p-5 rounded-2xl border border-slate-800 space-y-2.5">
            <div className="flex items-center gap-2 text-emerald-400 text-sm font-bold">
              <Users className="w-4 h-4" />
              <Download className="w-4 h-4" />
              <span>Multi-User & 100% Offline PWA</span>
            </div>
            <p className="text-xs text-slate-300 leading-relaxed">
              Multiple learners can use the app on the same device with separate SRS progress and settings. Install as a standalone PWA on mobile or desktop for seamless offline study on planes, subways, or anywhere without internet.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};
export default Help;
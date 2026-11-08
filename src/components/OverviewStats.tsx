import { useState, useMemo } from 'react';
import { DeckData } from '../types/schema';
import { getAllSRSData } from '../utils/srs';
import { getActiveUser } from '../utils/userStorage';
import { 
  Award, 
  Layers, 
  CheckCircle2, 
  Clock, 
  AlertCircle, 
  Download, 
  Volume2, 
  Sparkles,
  RefreshCw
} from 'lucide-react';

interface OverviewStatsProps {
  deck: DeckData;
  onRefresh: () => void;
}

export const OverviewStats: React.FC<OverviewStatsProps> = ({ deck, onRefresh }) => {
  const [isExporting, setIsExporting] = useState(false);
  const [exportMessage, setExportMessage] = useState<string | null>(null);
  const activeUser = getActiveUser();

  const { stats, manifest, units } = deck;
  const allCards = useMemo(() => units.flatMap((u) => u.lessons.flatMap((l) => l.entries)), [units]);
  const srsMap = useMemo(() => getAllSRSData(activeUser.id), [activeUser.id]);
  const learnedCount = useMemo(() => allCards.filter((c) => srsMap[c.id]?.isLearned && !srsMap[c.id]?.isExcluded).length, [allCards, srsMap]);

  const handleExport = async () => {
    setIsExporting(true);
    setExportMessage(null);
    try {
      const res = await fetch('/api/export', { method: 'POST' });
      const data = await res.json();
      if (data.success) {
        setExportMessage(data.message || 'PWA distribution package generated!');
      } else {
        setExportMessage(`Export error: ${data.detail || 'Failed'}`);
      }
    } catch {
      setExportMessage('Export failed. Check backend connection.');
    } finally {
      setIsExporting(false);
    }
  };

  return (
    <div className="space-y-6 max-w-6xl mx-auto pb-16 animate-in fade-in duration-200">
      {/* Hero Welcome & Deck Banner */}
      <div className="relative overflow-hidden rounded-3xl p-6 sm:p-8 bg-gradient-to-r from-sky-950/70 via-slate-900 to-indigo-950/70 border border-sky-500/20 shadow-2xl">
        <div className="absolute top-0 right-0 -mt-12 -mr-12 w-80 h-80 bg-sky-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div className="space-y-2">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sky-500/15 border border-sky-500/30 text-sky-300 text-xs font-semibold">
              <Sparkles className="w-3.5 h-3.5 text-sky-400" />
              <span>Modern Greek (CEFR A1) • Studio Audio & FSRS Engine</span>
            </div>
            <h1 className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
              {manifest.deck_title}
            </h1>
            <p className="text-slate-400 text-sm max-w-2xl leading-relaxed">
              Native Greek pronunciation verified with studio-quality audio. Local-first YAML source of truth with FSRS spaced repetition and full offline PWA support.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-3">
            <button
              type="button"
              onClick={onRefresh}
              className="inline-flex items-center gap-2 px-4 py-3 rounded-xl bg-slate-800/90 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium text-sm transition-all hover:scale-[1.02] active:scale-95"
              title="Refresh Deck Data"
            >
              <RefreshCw className="w-4 h-4" />
              <span>Reload</span>
            </button>
            <button
              type="button"
              onClick={handleExport}
              disabled={isExporting}
              className="inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-sky-500 hover:bg-sky-400 text-white font-semibold text-sm shadow-lg shadow-sky-500/25 transition-all hover:scale-[1.02] active:scale-95 disabled:opacity-50"
            >
              <Download className="w-4 h-4" />
              {isExporting ? 'Exporting...' : 'Export PWA'}
            </button>
          </div>
        </div>

        {exportMessage && (
          <div className="mt-4 p-3 rounded-xl bg-emerald-950/60 border border-emerald-500/30 text-emerald-300 text-xs flex items-center justify-between">
            <span>{exportMessage}</span>
            <button 
              onClick={() => setExportMessage(null)}
              className="text-emerald-400 hover:text-white text-xs underline ml-2"
            >
              Dismiss
            </button>
          </div>
        )}
      </div>

      {/* Global Metrics Row */}
      <div className="grid grid-cols-2 lg:grid-cols-5 gap-3.5 sm:gap-4">
        {/* Total Cards */}
        <div className="glass-panel p-4 sm:p-5 rounded-2xl flex flex-col justify-between border-slate-800 hover:border-slate-700 transition-all">
          <div className="flex items-center justify-between text-slate-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Total Cards</span>
            <Layers className="w-4 h-4 text-sky-400" />
          </div>
          <div className="mt-3">
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-white">{stats.total_entries}</span>
              <span className="text-xs text-slate-400">cards</span>
            </div>
            <p className="text-[11px] text-slate-500 mt-1">{units.length} lessons in deck</p>
          </div>
        </div>

        {/* Mastered / Learned Cards */}
        <div className="glass-panel p-4 sm:p-5 rounded-2xl flex flex-col justify-between border-emerald-500/30 hover:border-emerald-500/50 transition-all">
          <div className="flex items-center justify-between text-emerald-400">
            <span className="text-xs font-semibold uppercase tracking-wider truncate mr-1">{activeUser.name}'s Learned</span>
            <Award className="w-4 h-4 shrink-0" />
          </div>
          <div className="mt-3">
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-emerald-400">{learnedCount}</span>
              <span className="text-xs text-emerald-500/90 font-medium">
                ({stats.total_entries > 0 ? Math.round((learnedCount / stats.total_entries) * 100) : 0}%)
              </span>
            </div>
            <p className="text-[11px] text-emerald-600/90 mt-1">Mastered vocabulary</p>
          </div>
        </div>

        {/* Verified Audio */}
        <div className="glass-panel p-4 sm:p-5 rounded-2xl flex flex-col justify-between border-teal-500/30 hover:border-teal-500/50 transition-all">
          <div className="flex items-center justify-between text-teal-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Audio Coverage</span>
            <CheckCircle2 className="w-4 h-4" />
          </div>
          <div className="mt-3">
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-teal-400">{stats.verified_count}</span>
              <span className="text-xs text-teal-500/90 font-medium">({stats.coverage_percentage}%)</span>
            </div>
            <p className="text-[11px] text-teal-600/90 mt-1">Studio-quality pronunciation</p>
          </div>
        </div>

        {/* Pending TTS */}
        <div className="glass-panel p-4 sm:p-5 rounded-2xl flex flex-col justify-between border-amber-500/30 hover:border-amber-500/50 transition-all">
          <div className="flex items-center justify-between text-amber-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Pending Audio</span>
            <Clock className="w-4 h-4" />
          </div>
          <div className="mt-3">
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-amber-400">{stats.pending_count}</span>
              <span className="text-xs text-amber-500/90">to generate</span>
            </div>
            <p className="text-[11px] text-amber-600/90 mt-1">Local TTS queue</p>
          </div>
        </div>

        {/* Needs Review */}
        <div className="glass-panel p-4 sm:p-5 rounded-2xl flex flex-col justify-between border-rose-500/30 hover:border-rose-500/50 transition-all">
          <div className="flex items-center justify-between text-rose-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Needs Review</span>
            <AlertCircle className="w-4 h-4" />
          </div>
          <div className="mt-3">
            <div className="flex items-baseline gap-2">
              <span className="text-3xl font-extrabold text-rose-400">{stats.needs_review_count}</span>
              <span className="text-xs text-rose-500/90">flagged</span>
            </div>
            <p className="text-[11px] text-rose-600/90 mt-1">Refinements requested</p>
          </div>
        </div>
      </div>

      {/* Audio Health Coverage Bar */}
      <div className="glass-panel p-5 rounded-2xl border-slate-800">
        <div className="flex items-center justify-between mb-2">
          <div className="flex items-center gap-2">
            <Volume2 className="w-4 h-4 text-teal-400" />
            <span className="text-xs sm:text-sm font-semibold text-slate-300">Total Audio Health Coverage</span>
          </div>
          <span className="text-xs sm:text-sm font-bold text-sky-400">{stats.coverage_percentage}% verified</span>
        </div>
        <div className="w-full h-2.5 bg-slate-800 rounded-full overflow-hidden flex">
          <div 
            className="h-full bg-gradient-to-r from-emerald-500 to-teal-400 transition-all duration-500"
            style={{ width: `${stats.coverage_percentage}%` }}
          />
          <div 
            className="h-full bg-amber-500 transition-all duration-500"
            style={{ width: `${(stats.pending_count / (stats.total_entries || 1)) * 100}%` }}
          />
          <div 
            className="h-full bg-rose-500 transition-all duration-500"
            style={{ width: `${(stats.needs_review_count / (stats.total_entries || 1)) * 100}%` }}
          />
        </div>
        <div className="flex items-center gap-6 mt-3 text-xs text-slate-400">
          <div className="flex items-center gap-1.5">
            <span className="w-2 h-2 rounded-full bg-emerald-500" /> Verified ({stats.verified_count})
          </div>
          <div className="flex items-center gap-1.5">
            <span className="w-2 h-2 rounded-full bg-amber-500" /> Pending ({stats.pending_count})
          </div>
          <div className="flex items-center gap-1.5">
            <span className="w-2 h-2 rounded-full bg-rose-500" /> Needs Review ({stats.needs_review_count})
          </div>
        </div>
      </div>
    </div>
  );
};

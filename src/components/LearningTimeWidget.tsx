import React, { useState, useEffect, useMemo } from 'react';
import { getLearningStatsComparison } from '../utils/learningTime';
import { getActiveUser } from '../utils/userStorage';
import { LearningTimeVisualizer } from './LearningTimeVisualizer';
import { 
  Clock, 
  Flame, 
  TrendingUp, 
  X, 
  Sparkles, 
  ArrowUpRight,
  Maximize2
} from 'lucide-react';

interface LearningTimeWidgetProps {
  onStartStudy?: () => void;
  className?: string;
}

export const LearningTimeWidget: React.FC<LearningTimeWidgetProps> = ({
  onStartStudy,
  className = '',
}) => {
  const [activeUser, setActiveUser] = useState(getActiveUser());
  const [version, setVersion] = useState(0);
  const [showModal, setShowModal] = useState(false);

  useEffect(() => {
    const handleUpdate = () => {
      setActiveUser(getActiveUser());
      setVersion((v) => v + 1);
    };

    window.addEventListener('greek_deck_user_change', handleUpdate);
    window.addEventListener('greek_deck_progress_change', handleUpdate);
    window.addEventListener('greek_deck_learning_time_change', handleUpdate);
    window.addEventListener('greek_deck_prefs_change', handleUpdate);

    return () => {
      window.removeEventListener('greek_deck_user_change', handleUpdate);
      window.removeEventListener('greek_deck_progress_change', handleUpdate);
      window.removeEventListener('greek_deck_learning_time_change', handleUpdate);
      window.removeEventListener('greek_deck_prefs_change', handleUpdate);
    };
  }, []);

  const stats = useMemo(() => getLearningStatsComparison(activeUser.id), [activeUser.id, version]);

  return (
    <>
      {/* Dashboard Compact Focus Card */}
      <div className={`glass-panel p-4 sm:p-5 rounded-3xl border border-slate-800 hover:border-slate-700/80 transition-all shadow-xl relative overflow-hidden group ${className}`}>
        {/* Subtle background glow */}
        <div className={`absolute top-0 right-0 w-64 h-64 rounded-full blur-3xl pointer-events-none opacity-20 ${
          stats.isAheadOfYesterday ? 'bg-emerald-500' : 'bg-sky-500'
        }`} />

        <div className="relative z-10 flex flex-col lg:flex-row lg:items-center justify-between gap-4">
          {/* Left: Today's Time and Yesterday Comparison */}
          <div className="flex items-start sm:items-center gap-4">
            {/* Circular Progress Ring */}
            <div 
              onClick={() => setShowModal(true)}
              className="relative w-14 h-14 sm:w-16 sm:h-16 shrink-0 flex items-center justify-center cursor-pointer group-hover:scale-105 transition-transform"
              title="Click to open Learning Time Machine"
            >
              <svg className="w-full h-full transform -rotate-90" viewBox="0 0 36 36">
                <path
                  className="text-slate-800"
                  strokeWidth="3.5"
                  stroke="currentColor"
                  fill="none"
                  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                />
                <path
                  className={`transition-all duration-700 ${
                    stats.isGoalMet ? 'text-emerald-400' : 'text-sky-400'
                  }`}
                  strokeDasharray={`${stats.todayGoalProgressPct}, 100`}
                  strokeLinecap="round"
                  strokeWidth="3.5"
                  stroke="currentColor"
                  fill="none"
                  d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                />
              </svg>
              <div className="absolute inset-0 flex flex-col items-center justify-center text-center pointer-events-none">
                <Clock className={`w-4 h-4 ${stats.isGoalMet ? 'text-emerald-400' : 'text-sky-400'}`} />
                <span className="text-[10px] font-extrabold text-white leading-none mt-0.5">
                  {stats.todayGoalProgressPct}%
                </span>
              </div>
            </div>

            {/* Time Details & Yesterday Delta */}
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <span className="text-xs font-semibold uppercase tracking-wider text-slate-400">
                  Today's Study Time
                </span>
                {stats.isBestDayToday && stats.todaySeconds > 180 && (
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-amber-500/20 text-amber-300 border border-amber-500/30">
                    🏆 Best Record
                  </span>
                )}
              </div>

              <div className="flex flex-wrap items-baseline gap-2">
                <span className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
                  {stats.todayFormatted}
                </span>
                <span className="text-xs text-slate-400 font-medium">
                  / {stats.todayGoalMinutes}m goal
                </span>

                {/* Comparison Badge with Yesterday */}
                {stats.yesterdaySeconds > 0 ? (
                  stats.isAheadOfYesterday ? (
                    <span className="inline-flex items-center gap-1 text-xs font-bold px-2 py-0.5 rounded-lg bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                      <ArrowUpRight className="w-3.5 h-3.5" />
                      +{stats.diffFromYesterdayFormatted} vs yesterday ({stats.pctFromYesterday ? `+${stats.pctFromYesterday}%` : ''})
                    </span>
                  ) : (
                    <span className="inline-flex items-center gap-1 text-xs font-medium px-2 py-0.5 rounded-lg bg-amber-500/15 text-amber-300 border border-amber-500/25">
                      <Flame className="w-3.5 h-3.5 text-amber-400" />
                      {stats.remainingToBeatYesterdayFormatted} to beat yesterday
                    </span>
                  )
                ) : (
                  <span className="inline-flex items-center gap-1 text-xs font-medium px-2 py-0.5 rounded-lg bg-sky-500/15 text-sky-300 border border-sky-500/25">
                    <Sparkles className="w-3.5 h-3.5 text-sky-400" />
                    Today's Pace
                  </span>
                )}
              </div>

              <p className="text-xs text-slate-400 max-w-lg leading-snug">
                {stats.motivationalMessage.text}
              </p>
            </div>
          </div>

          {/* Right: Greek Wisdom Rank & Open Full Modal Button */}
          <div className="flex flex-wrap sm:flex-nowrap items-center justify-between lg:justify-end gap-3 pt-3 lg:pt-0 border-t lg:border-t-0 border-slate-800/80">
            {/* Wisdom Rank badge */}
            <div 
              onClick={() => setShowModal(true)}
              className="flex items-center gap-2.5 px-3 py-2 rounded-2xl bg-slate-900/90 border border-slate-800 hover:border-slate-700 cursor-pointer transition-all"
              title="Click to view Greek Wisdom Ranks & Progression"
            >
              <div className="text-2xl p-1 rounded-xl bg-slate-800 shrink-0">
                {stats.currentRank.icon}
              </div>
              <div>
                <div className="flex items-center gap-1.5">
                  <span className="text-[10px] font-bold text-slate-400 uppercase tracking-wider">
                    Lvl {stats.currentRank.level}
                  </span>
                  <span className={`text-xs font-bold truncate ${stats.currentRank.colorClass}`}>
                    {stats.currentRank.title}
                  </span>
                </div>
                <div className="flex items-center gap-2 mt-0.5">
                  <div className="w-20 bg-slate-800 h-1.5 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-gradient-to-r from-sky-500 to-indigo-500"
                      style={{ width: `${stats.progressToNextRankPct}%` }}
                    />
                  </div>
                  <span className="text-[10px] text-slate-400 font-semibold">
                    {stats.allTimeXP} XP
                  </span>
                </div>
              </div>
            </div>

            {/* Launch Time Machine Modal Button */}
            <button
              type="button"
              onClick={() => setShowModal(true)}
              className="inline-flex items-center gap-1.5 px-3.5 py-2.5 rounded-2xl bg-slate-800/90 hover:bg-slate-700 text-slate-200 hover:text-white border border-slate-700 text-xs font-bold transition-all hover:scale-[1.02] active:scale-95 shrink-0"
              title="Open full learning history, charts, and comparisons"
            >
              <TrendingUp className="w-3.5 h-3.5 text-sky-400" />
              <span>Time Machine</span>
              <Maximize2 className="w-3 h-3 text-slate-400 ml-0.5" />
            </button>
          </div>
        </div>
      </div>

      {/* Full "Time Machine" Analytics & Visualizer Modal */}
      {showModal && (
        <div className="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-3 sm:p-6 animate-in fade-in duration-200">
          <div 
            className="bg-slate-950 border border-slate-800 w-full max-w-4xl max-h-[92vh] rounded-3xl overflow-hidden shadow-2xl flex flex-col animate-in zoom-in-95 duration-200"
            onClick={(e) => e.stopPropagation()}
          >
            {/* Modal Header */}
            <div className="p-5 sm:p-6 border-b border-slate-800/80 flex items-center justify-between bg-slate-900/60 sticky top-0 z-10">
              <div className="flex items-center gap-3">
                <div className="w-10 h-10 rounded-2xl bg-gradient-to-tr from-sky-500 to-indigo-600 flex items-center justify-center shadow-md shadow-sky-500/20 text-white font-serif font-black text-lg">
                  Ω
                </div>
                <div>
                  <h3 className="text-base sm:text-lg font-extrabold text-white tracking-tight flex items-center gap-2">
                    Learning Time Machine & Focus Track
                  </h3>
                  <p className="text-xs text-slate-400">
                    Track your daily study time, compare past performance, and climb Greek wisdom ranks.
                  </p>
                </div>
              </div>

              <button
                type="button"
                onClick={() => setShowModal(false)}
                className="p-2 rounded-xl text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
                title="Close"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {/* Modal Content Scroll Area */}
            <div className="p-5 sm:p-6 overflow-y-auto space-y-6 flex-1">
              <LearningTimeVisualizer
                onStartStudy={() => {
                  setShowModal(false);
                  if (onStartStudy) onStartStudy();
                }}
              />
            </div>

            {/* Modal Footer */}
            <div className="p-4 border-t border-slate-800/80 bg-slate-900/40 flex items-center justify-between text-xs text-slate-400">
              <span className="flex items-center gap-1.5">
                <Sparkles className="w-3.5 h-3.5 text-amber-400" />
                Active Learner: <strong className="text-white">{activeUser.name}</strong>
              </span>
              <button
                type="button"
                onClick={() => setShowModal(false)}
                className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 font-semibold"
              >
                Done
              </button>
            </div>
          </div>
        </div>
      )}
    </>
  );
};

import React, { useState, useMemo } from 'react';
import { 
  getLearningStatsComparison, 
  DayHistoryItem, 
  formatDuration, 
  GREEK_RANKS 
} from '../utils/learningTime';
import { getActiveUser } from '../utils/userStorage';
import { 
  Clock, 
  TrendingUp, 
  Award, 
  Flame, 
  Calendar, 
  Zap, 
  Trophy, 
  Sparkles, 
  CheckCircle2, 
  Lock, 
  ArrowUpRight 
} from 'lucide-react';

interface LearningTimeVisualizerProps {
  onStartStudy?: () => void;
}

export const LearningTimeVisualizer: React.FC<LearningTimeVisualizerProps> = ({
  onStartStudy,
}) => {
  const activeUser = getActiveUser();
  const [viewRange, setViewRange] = useState<'7days' | '14days'>('7days');
  const [selectedDay, setSelectedDay] = useState<DayHistoryItem | null>(null);

  const stats = useMemo(() => getLearningStatsComparison(activeUser.id), [activeUser.id]);

  const history = viewRange === '7days' ? stats.history7Days : stats.history14Days;

  // Compute maximum seconds for scaling bar heights
  const maxSeconds = useMemo(() => {
    const dataMax = Math.max(...history.map((d) => d.seconds), 0);
    // Ensure the goal line has space by taking max of data and 1.25 * goal
    return Math.max(dataMax, stats.todayGoalSeconds * 1.25, 300); // at least 5 mins scale
  }, [history, stats.todayGoalSeconds]);

  // Set default selected day to today if none selected
  const activeSelectedDay = selectedDay || history[history.length - 1];

  return (
    <div className="space-y-6">
      {/* Motivational Banner / Coach Callout */}
      <div className={`p-4 sm:p-5 rounded-2xl border transition-all relative overflow-hidden ${
        stats.isAheadOfYesterday 
          ? 'bg-gradient-to-r from-emerald-950/70 via-slate-900 to-teal-950/70 border-emerald-500/40 shadow-lg shadow-emerald-500/10' 
          : stats.isGoalMet 
          ? 'bg-gradient-to-r from-sky-950/70 via-slate-900 to-indigo-950/70 border-sky-500/40 shadow-lg shadow-sky-500/10'
          : 'bg-gradient-to-r from-amber-950/60 via-slate-900 to-slate-900 border-amber-500/30 shadow-lg shadow-amber-500/10'
      }`}>
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div className="flex items-start gap-3.5">
            <div className="text-3xl sm:text-4xl p-2 rounded-2xl bg-slate-800/80 border border-slate-700/80 shrink-0">
              {stats.motivationalMessage.icon}
            </div>
            <div className="space-y-1">
              <div className="flex items-center gap-2">
                <span className="text-xs font-bold uppercase tracking-wider px-2 py-0.5 rounded-full bg-slate-800/90 text-slate-300 border border-slate-700">
                  Daily Momentum
                </span>
                {stats.isAheadOfYesterday && (
                  <span className="text-xs font-extrabold text-emerald-400 flex items-center gap-0.5 animate-pulse">
                    <ArrowUpRight className="w-3.5 h-3.5" /> Ahead of Yesterday!
                  </span>
                )}
              </div>
              <h3 className="text-base sm:text-lg font-bold text-white tracking-tight">
                {stats.motivationalMessage.title}
              </h3>
              <p className="text-xs sm:text-sm text-slate-300 max-w-2xl leading-relaxed">
                {stats.motivationalMessage.text}
              </p>
            </div>
          </div>

          {onStartStudy && (
            <button
              type="button"
              onClick={onStartStudy}
              className="inline-flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-gradient-to-r from-sky-500 to-indigo-500 hover:from-sky-400 hover:to-indigo-400 text-white font-bold text-xs sm:text-sm shadow-md shadow-sky-500/25 transition-all hover:scale-[1.02] active:scale-95 shrink-0"
            >
              <Zap className="w-4 h-4 fill-current text-amber-300" />
              <span>Study Now & Add Time</span>
            </button>
          )}
        </div>
      </div>

      {/* Head-to-Head Comparisons Grid: Today vs Yesterday & This Week vs Last Week */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3.5">
        {/* Today's Learning Time */}
        <div className="glass-panel p-4 rounded-2xl border-slate-800 flex flex-col justify-between">
          <div className="flex items-center justify-between text-slate-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Today's Focus</span>
            <Clock className="w-4 h-4 text-sky-400" />
          </div>
          <div className="mt-2.5">
            <div className="flex items-baseline gap-2">
              <span className="text-2xl sm:text-3xl font-extrabold text-white">
                {stats.todayFormatted}
              </span>
              <span className="text-xs text-slate-400 font-medium">
                / {stats.todayGoalMinutes}m goal
              </span>
            </div>
            {/* Progress bar towards goal */}
            <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden mt-2">
              <div
                className={`h-full transition-all duration-500 ${
                  stats.isGoalMet ? 'bg-gradient-to-r from-emerald-500 to-teal-400' : 'bg-sky-500'
                }`}
                style={{ width: `${stats.todayGoalProgressPct}%` }}
              />
            </div>
            <p className="text-[11px] text-slate-400 mt-1.5 flex items-center justify-between">
              <span>{stats.todayGoalProgressPct}% completed</span>
              {stats.isGoalMet && <span className="text-emerald-400 font-semibold">Goal Met! ✓</span>}
            </p>
          </div>
        </div>

        {/* Comparison: Today vs Yesterday */}
        <div className={`glass-panel p-4 rounded-2xl border transition-all flex flex-col justify-between ${
          stats.isAheadOfYesterday
            ? 'border-emerald-500/40 bg-emerald-950/20'
            : stats.yesterdaySeconds > 0
            ? 'border-amber-500/30 bg-amber-950/15'
            : 'border-slate-800'
        }`}>
          <div className="flex items-center justify-between">
            <span className="text-xs font-semibold uppercase tracking-wider text-slate-400">vs Yesterday</span>
            <Flame className={`w-4 h-4 ${stats.isAheadOfYesterday ? 'text-emerald-400' : 'text-amber-400'}`} />
          </div>
          <div className="mt-2.5">
            <div className="flex items-baseline gap-1.5">
              <span className={`text-2xl sm:text-3xl font-extrabold ${
                stats.isAheadOfYesterday ? 'text-emerald-400' : 'text-amber-300'
              }`}>
                {stats.isAheadOfYesterday ? `+${stats.diffFromYesterdayFormatted}` : stats.todayFormatted}
              </span>
              {stats.pctFromYesterday !== null && (
                <span className={`text-xs font-bold px-1.5 py-0.5 rounded ${
                  stats.pctFromYesterday >= 0 
                    ? 'bg-emerald-500/20 text-emerald-300' 
                    : 'bg-amber-500/20 text-amber-300'
                }`}>
                  {stats.pctFromYesterday >= 0 ? `+${stats.pctFromYesterday}%` : `${stats.pctFromYesterday}%`}
                </span>
              )}
            </div>
            <p className="text-[11px] text-slate-400 mt-1.5">
              {stats.yesterdaySeconds > 0 ? (
                stats.isAheadOfYesterday ? (
                  <span className="text-emerald-300 font-medium">Surpassed yesterday ({stats.yesterdayFormatted})! 🚀</span>
                ) : (
                  <span>{stats.remainingToBeatYesterdayFormatted} to overtake yesterday ({stats.yesterdayFormatted})</span>
                )
              ) : (
                <span>No study recorded yesterday</span>
              )}
            </p>
          </div>
        </div>

        {/* Weekly Battle: This Week vs Last Week */}
        <div className="glass-panel p-4 rounded-2xl border-slate-800 flex flex-col justify-between">
          <div className="flex items-center justify-between text-slate-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Weekly Momentum</span>
            <TrendingUp className="w-4 h-4 text-indigo-400" />
          </div>
          <div className="mt-2.5">
            <div className="flex items-baseline gap-2">
              <span className="text-2xl sm:text-3xl font-extrabold text-indigo-400">
                {stats.thisWeekFormatted}
              </span>
              {stats.pctFromLastWeek !== null && (
                <span className={`text-xs font-bold px-1.5 py-0.5 rounded ${
                  stats.pctFromLastWeek >= 0 
                    ? 'bg-indigo-500/20 text-indigo-300' 
                    : 'bg-slate-700 text-slate-300'
                }`}>
                  {stats.pctFromLastWeek >= 0 ? `+${stats.pctFromLastWeek}%` : `${stats.pctFromLastWeek}%`}
                </span>
              )}
            </div>
            <p className="text-[11px] text-slate-400 mt-1.5">
              Last week: <span className="text-slate-300 font-medium">{stats.lastWeekFormatted}</span>
            </p>
          </div>
        </div>

        {/* All-Time Study Immersion */}
        <div className="glass-panel p-4 rounded-2xl border-slate-800 flex flex-col justify-between">
          <div className="flex items-center justify-between text-slate-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Total Immersion</span>
            <Trophy className="w-4 h-4 text-amber-400" />
          </div>
          <div className="mt-2.5">
            <div className="flex items-baseline gap-2">
              <span className="text-2xl sm:text-3xl font-extrabold text-amber-400">
                {stats.allTimeFormatted}
              </span>
              <span className="text-xs text-amber-500/90 font-medium">
                ({stats.allTimeXP} XP)
              </span>
            </div>
            <p className="text-[11px] text-slate-400 mt-1.5">
              Best Day: <span className="text-slate-200 font-medium">{stats.bestDay.formatted}</span>
            </p>
          </div>
        </div>
      </div>

      {/* Main Interactive Chart: Day-by-Day Learning Time & Goal Comparison */}
      <div className="glass-panel p-5 sm:p-6 rounded-3xl border-slate-800 space-y-4">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pb-2 border-b border-slate-800/80">
          <div>
            <div className="flex items-center gap-2">
              <Calendar className="w-4 h-4 text-sky-400" />
              <h4 className="text-sm sm:text-base font-bold text-white tracking-tight">
                Daily Learning Time History
              </h4>
            </div>
            <p className="text-xs text-slate-400 mt-0.5">
              Click or tap any day to inspect your focus time, cards reviewed, and wisdom XP.
            </p>
          </div>

          <div className="flex items-center gap-2 self-start sm:self-auto">
            <div className="inline-flex rounded-xl bg-slate-800/90 p-1 border border-slate-700/80 text-xs font-medium">
              <button
                type="button"
                onClick={() => setViewRange('7days')}
                className={`px-3 py-1 rounded-lg transition-all ${
                  viewRange === '7days'
                    ? 'bg-sky-500 text-white font-bold shadow-sm'
                    : 'text-slate-400 hover:text-white'
                }`}
              >
                Last 7 Days
              </button>
              <button
                type="button"
                onClick={() => setViewRange('14days')}
                className={`px-3 py-1 rounded-lg transition-all ${
                  viewRange === '14days'
                    ? 'bg-sky-500 text-white font-bold shadow-sm'
                    : 'text-slate-400 hover:text-white'
                }`}
              >
                14 Days
              </button>
            </div>
          </div>
        </div>

        {/* Visual Bar Chart */}
        <div className="pt-2 pb-1">
          {/* Chart Canvas Area */}
          <div className="relative h-48 w-full flex items-end gap-1.5 sm:gap-3 px-2 pt-6">
            {/* Horizontal Goal Dotted Guideline */}
            <div 
              className="absolute left-0 right-0 border-b border-dashed border-sky-400/30 flex items-center justify-between pointer-events-none z-0"
              style={{
                bottom: `${Math.min(95, Math.max(5, (stats.todayGoalSeconds / maxSeconds) * 100))}%`,
              }}
            >
              <span className="text-[10px] font-bold text-sky-400/80 bg-slate-900/90 px-2 py-0.5 rounded border border-sky-500/20 -translate-y-1/2 ml-1">
                Goal: {stats.todayGoalMinutes}m
              </span>
            </div>

            {/* Bars for each day */}
            {history.map((day) => {
              const heightPct = Math.min(100, Math.max(day.seconds > 0 ? 6 : 2, (day.seconds / maxSeconds) * 100));
              const isSelected = activeSelectedDay.date === day.date;
              const hasActivity = day.seconds > 0;
              const metGoal = day.goalMet;

              return (
                <div
                  key={day.date}
                  onClick={() => setSelectedDay(day)}
                  className="flex-1 h-full flex flex-col justify-end items-center group cursor-pointer relative z-10"
                >
                  {/* Floating tooltip preview on hover or selection */}
                  {isSelected && (
                    <div className="absolute -top-10 bg-slate-900 text-white text-[10px] font-bold px-2 py-1 rounded-lg border border-sky-500/40 shadow-xl whitespace-nowrap z-20 pointer-events-none animate-in fade-in zoom-in-95">
                      {day.formatted}
                    </div>
                  )}

                  {/* The bar element */}
                  <div
                    className={`w-full rounded-t-xl transition-all duration-300 relative ${
                      day.isToday
                        ? 'ring-2 ring-sky-400 shadow-lg shadow-sky-500/20'
                        : isSelected
                        ? 'ring-2 ring-white/60'
                        : ''
                    } ${
                      metGoal
                        ? 'bg-gradient-to-t from-emerald-600 via-teal-500 to-teal-400 group-hover:brightness-110'
                        : hasActivity
                        ? 'bg-gradient-to-t from-sky-600 via-indigo-500 to-indigo-400 group-hover:brightness-110'
                        : 'bg-slate-800/80 group-hover:bg-slate-700/80'
                    }`}
                    style={{ height: `${heightPct}%` }}
                  >
                    {/* Goal met star indicator */}
                    {metGoal && (
                      <div className="absolute -top-3 left-1/2 -translate-x-1/2 text-[9px] pointer-events-none">
                        ⭐
                      </div>
                    )}
                  </div>

                  {/* Day Label */}
                  <div className="mt-2 text-center">
                    <span className={`text-[10px] sm:text-xs font-semibold block ${
                      day.isToday 
                        ? 'text-sky-400 font-extrabold' 
                        : isSelected 
                        ? 'text-white' 
                        : 'text-slate-400 group-hover:text-slate-200'
                    }`}>
                      {day.dayLabel}
                    </span>
                    <span className="text-[9px] text-slate-500 hidden sm:block">
                      {day.fullDate.split(' ')[1]}
                    </span>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Legend row */}
          <div className="flex flex-wrap items-center justify-between gap-3 pt-4 border-t border-slate-800 text-[11px] text-slate-400">
            <div className="flex items-center gap-4">
              <div className="flex items-center gap-1.5">
                <span className="w-2.5 h-2.5 rounded-sm bg-gradient-to-tr from-emerald-500 to-teal-400" />
                <span>Goal Met ({stats.todayGoalMinutes}m+)</span>
              </div>
              <div className="flex items-center gap-1.5">
                <span className="w-2.5 h-2.5 rounded-sm bg-gradient-to-tr from-sky-500 to-indigo-500" />
                <span>Active Study</span>
              </div>
              <div className="flex items-center gap-1.5">
                <span className="w-2.5 h-2.5 rounded-sm bg-slate-800" />
                <span>Rest Day</span>
              </div>
            </div>
            <div>
              <span>7-Day Average: </span>
              <strong className="text-white">{stats.dailyAverage7DaysFormatted}/day</strong>
            </div>
          </div>
        </div>

        {/* Inspector Detail Card for Selected Day */}
        <div className="p-3.5 sm:p-4 rounded-2xl bg-slate-900/90 border border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-3">
          <div className="flex items-center gap-3">
            <div className={`w-10 h-10 rounded-xl flex items-center justify-center font-bold text-lg shrink-0 ${
              activeSelectedDay.goalMet
                ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/30'
                : activeSelectedDay.seconds > 0
                ? 'bg-sky-500/20 text-sky-400 border border-sky-500/30'
                : 'bg-slate-800 text-slate-500 border border-slate-700'
            }`}>
              {activeSelectedDay.goalMet ? '✓' : '⏱'}
            </div>
            <div>
              <div className="flex items-center gap-2">
                <h5 className="text-sm font-bold text-white">
                  {activeSelectedDay.fullDate} ({activeSelectedDay.dayLabel})
                </h5>
                {activeSelectedDay.isToday && (
                  <span className="text-[10px] font-bold px-1.5 py-0.2 rounded bg-sky-500 text-white">
                    Today
                  </span>
                )}
                {activeSelectedDay.isYesterday && (
                  <span className="text-[10px] font-bold px-1.5 py-0.2 rounded bg-slate-800 text-slate-300 border border-slate-700">
                    Yesterday
                  </span>
                )}
              </div>
              <p className="text-xs text-slate-400">
                {activeSelectedDay.seconds > 0 ? (
                  <>
                    Logged <span className="text-white font-semibold">{activeSelectedDay.formatted}</span> of study •{' '}
                    <span className="text-sky-300">{activeSelectedDay.cardsReviewed} cards reviewed</span> •{' '}
                    <span className="text-amber-300">+{activeSelectedDay.xp} XP</span>
                  </>
                ) : (
                  <span>No active study recorded for this day.</span>
                )}
              </p>
            </div>
          </div>

          <div className="text-right text-xs text-slate-400 sm:border-l sm:border-slate-800 sm:pl-4">
            {activeSelectedDay.goalMet ? (
              <span className="text-emerald-400 font-bold inline-flex items-center gap-1">
                <CheckCircle2 className="w-3.5 h-3.5" /> Target Achieved!
              </span>
            ) : activeSelectedDay.seconds > 0 ? (
              <span>
                {formatDuration(Math.max(0, stats.todayGoalSeconds - activeSelectedDay.seconds))} to goal
              </span>
            ) : (
              <span>Rest day</span>
            )}
          </div>
        </div>
      </div>

      {/* Greek Wisdom Level & XP Ladder */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {/* Current Rank Card */}
        <div className={`p-5 rounded-3xl border flex flex-col justify-between ${stats.currentRank.borderClass}`}>
          <div>
            <div className="flex items-center justify-between">
              <span className="text-xs font-semibold uppercase tracking-wider text-slate-400">
                Current Wisdom Rank
              </span>
              <span className="text-xs font-bold px-2 py-0.5 rounded-full bg-slate-800 text-slate-300 border border-slate-700">
                Level {stats.currentRank.level} of {GREEK_RANKS.length}
              </span>
            </div>

            <div className="flex items-center gap-3.5 mt-4">
              <div className="text-4xl p-2.5 rounded-2xl bg-slate-900/80 border border-slate-700/60 shrink-0">
                {stats.currentRank.icon}
              </div>
              <div>
                <h4 className={`text-lg font-black tracking-tight ${stats.currentRank.colorClass}`}>
                  {stats.currentRank.title}
                </h4>
                <p className="text-xs font-serif text-slate-300 font-medium italic">
                  {stats.currentRank.greekTitle}
                </p>
                <p className="text-[11px] text-slate-400 mt-1 leading-tight">
                  {stats.currentRank.description}
                </p>
              </div>
            </div>
          </div>

          {/* XP Progress to Next Level */}
          <div className="mt-5 pt-3 border-t border-slate-800/80">
            <div className="flex items-center justify-between text-xs text-slate-300 mb-1.5">
              <span className="font-semibold flex items-center gap-1">
                <Sparkles className="w-3.5 h-3.5 text-amber-400" />
                {stats.nextRank ? `Next: ${stats.nextRank.title}` : 'Max Rank Reached!'}
              </span>
              <span className="font-bold text-sky-400">{stats.progressToNextRankPct}%</span>
            </div>
            <div className="w-full bg-slate-900 h-2.5 rounded-full overflow-hidden">
              <div
                className="h-full bg-gradient-to-r from-sky-500 via-indigo-500 to-purple-500 transition-all duration-500"
                style={{ width: `${stats.progressToNextRankPct}%` }}
              />
            </div>
            {stats.nextRank && (
              <p className="text-[11px] text-slate-400 mt-1.5">
                {stats.formattedRemainingToNextRank}
              </p>
            )}
          </div>
        </div>

        {/* Unlocked Achievements Gallery (Spans 2 columns) */}
        <div className="md:col-span-2 glass-panel p-5 rounded-3xl border-slate-800 space-y-3 flex flex-col justify-between">
          <div className="flex items-center justify-between pb-2 border-b border-slate-800">
            <div className="flex items-center gap-2">
              <Award className="w-4 h-4 text-amber-400" />
              <h4 className="text-sm font-bold text-white tracking-tight">
                Greek Learning Achievements ({stats.unlockedBadges.length} / {stats.allBadges.length})
              </h4>
            </div>
            <span className="text-xs text-slate-400">
              {Math.round((stats.unlockedBadges.length / stats.allBadges.length) * 100)}% unlocked
            </span>
          </div>

          {/* Badges Grid */}
          <div className="grid grid-cols-2 sm:grid-cols-5 gap-2.5 pt-1">
            {stats.allBadges.map((badge: any) => (
              <div
                key={badge.id}
                className={`p-2.5 rounded-2xl border text-center flex flex-col items-center justify-between transition-all ${
                  badge.isUnlocked
                    ? 'bg-slate-900/90 border-amber-500/40 shadow-sm hover:scale-105'
                    : 'bg-slate-950/40 border-slate-800/80 opacity-50'
                }`}
                title={`${badge.title} (${badge.greekTitle}): ${badge.description}`}
              >
                <div className="text-2xl mb-1 relative">
                  {badge.icon}
                  {!badge.isUnlocked && (
                    <Lock className="w-3 h-3 text-slate-500 absolute -bottom-1 -right-1" />
                  )}
                </div>
                <div className="w-full">
                  <h6 className="text-[11px] font-bold text-white truncate">
                    {badge.title}
                  </h6>
                  <p className="text-[9px] text-slate-400 truncate">
                    {badge.greekTitle}
                  </p>
                </div>
              </div>
            ))}
          </div>

          <p className="text-[11px] text-slate-400 pt-1">
            💡 <strong className="text-slate-300">Tip:</strong> Beat yesterday's study time or practice late at night to earn special badges!
          </p>
        </div>
      </div>
    </div>
  );
};

import { 
  getActiveUserId, 
  getUserStudyPreferences, 
  notifyProgressChanged, 
  getTodayKey 
} from './userStorage';
import { mirrorKeyToIndexedDB } from './indexedDBStorage';

export interface DailyTimeRecord {
  date: string; // YYYY-MM-DD
  seconds: number; // Active learning seconds
  sessionsCount: number;
  cardsReviewed: number;
  xp: number;
  lastActive: string; // ISO string
}

export interface AchievementBadge {
  id: string;
  title: string;
  greekTitle: string;
  description: string;
  icon: string;
  unlockedAt?: string;
  category: 'time' | 'streak' | 'session' | 'record';
}

export interface GreekWisdomRank {
  level: number;
  title: string;
  greekTitle: string;
  icon: string;
  minSeconds: number;
  minXP: number;
  description: string;
  colorClass: string;
  borderClass: string;
}

export interface LearningTimeData {
  userId: string;
  records: Record<string, DailyTimeRecord>;
  allTimeSeconds: number;
  allTimeXP: number;
  bestDay: {
    date: string;
    seconds: number;
  };
  longestSessionSeconds: number;
  unlockedBadgeIds: string[];
}

export const GREEK_RANKS: GreekWisdomRank[] = [
  {
    level: 1,
    title: 'Novice Scribe',
    greekTitle: 'Αρχάριος Γραφέας',
    icon: '🦉',
    minSeconds: 0,
    minXP: 0,
    description: 'Beginning the voyage into the Greek tongue.',
    colorClass: 'text-slate-300',
    borderClass: 'border-slate-500/30 bg-slate-800/40',
  },
  {
    level: 2,
    title: "Philosopher's Apprentice",
    greekTitle: 'Μαθητευόμενος Σοφίας',
    icon: '📜',
    minSeconds: 15 * 60, // 15 mins
    minXP: 150,
    description: 'Taking the first thoughtful steps in the Academy.',
    colorClass: 'text-sky-400',
    borderClass: 'border-sky-500/30 bg-sky-950/40',
  },
  {
    level: 3,
    title: 'Agora Orator',
    greekTitle: 'Ρήτορας της Αγοράς',
    icon: '🏛️',
    minSeconds: 60 * 60, // 1 hr
    minXP: 600,
    description: 'Speaking with increasing confidence in the marketplace.',
    colorClass: 'text-teal-400',
    borderClass: 'border-teal-500/30 bg-teal-950/40',
  },
  {
    level: 4,
    title: 'Delphic Seeker',
    greekTitle: 'Μύστης των Δελφών',
    icon: '⚡',
    minSeconds: 3 * 3600, // 3 hrs
    minXP: 1800,
    description: 'Unlocking the ancient secrets of Greek expression.',
    colorClass: 'text-amber-400',
    borderClass: 'border-amber-500/30 bg-amber-950/40',
  },
  {
    level: 5,
    title: 'Athenian Scholar',
    greekTitle: 'Αθηναίος Σοφός',
    icon: '🏺',
    minSeconds: 6 * 3600, // 6 hrs
    minXP: 3600,
    description: 'A master of vocabulary, syntax, and tones.',
    colorClass: 'text-emerald-400',
    borderClass: 'border-emerald-500/30 bg-emerald-950/40',
  },
  {
    level: 6,
    title: 'Spartan Mind',
    greekTitle: 'Σπαρτιάτης Μελετητής',
    icon: '⚔️',
    minSeconds: 12 * 3600, // 12 hrs
    minXP: 7200,
    description: 'Unshakable discipline and relentless study habit.',
    colorClass: 'text-rose-400',
    borderClass: 'border-rose-500/30 bg-rose-950/40',
  },
  {
    level: 7,
    title: 'Titan of Vocabulary',
    greekTitle: 'Τιτάνας της Γλώσσας',
    icon: '👑',
    minSeconds: 25 * 3600, // 25 hrs
    minXP: 15000,
    description: 'Immense linguistic prowess command of Greek phrases.',
    colorClass: 'text-purple-400',
    borderClass: 'border-purple-500/30 bg-purple-950/40',
  },
  {
    level: 8,
    title: 'Mount Olympus Immortal',
    greekTitle: 'Ολύμπιος Αθάνατος',
    icon: '🌟',
    minSeconds: 50 * 3600, // 50 hrs
    minXP: 30000,
    description: 'Supreme fluency and legendary commitment.',
    colorClass: 'text-yellow-300',
    borderClass: 'border-yellow-500/40 bg-yellow-950/40 ring-1 ring-yellow-400/30',
  },
];

export const ALL_ACHIEVEMENTS: AchievementBadge[] = [
  {
    id: 'first_spark',
    title: 'Promethean Spark',
    greekTitle: 'Προμηθεϊκή Σπίθα',
    description: 'Completed your very first active study session.',
    icon: '🔥',
    category: 'session',
  },
  {
    id: 'yesterday_crusher',
    title: 'Yesterday Crusher',
    greekTitle: 'Νικητής του Χθες',
    description: 'Spent more time learning today than you did yesterday!',
    icon: '🚀',
    category: 'record',
  },
  {
    id: 'daily_champion',
    title: 'Daily Goal Champion',
    greekTitle: 'Πρωταθλητής Στόχου',
    description: 'Fulfilled your daily learning time target.',
    icon: '🎯',
    category: 'time',
  },
  {
    id: 'deep_focus',
    title: 'Deep Focus Immersion',
    greekTitle: 'Βαθιά Συγκέντρωση',
    description: 'Maintained 15+ minutes of continuous active study.',
    icon: '🧘',
    category: 'session',
  },
  {
    id: 'streak_3',
    title: 'Time Voyager',
    greekTitle: 'Χρονοταξιδιώτης',
    description: 'Studied for 3 consecutive days in a row.',
    icon: '⚡',
    category: 'streak',
  },
  {
    id: 'streak_7',
    title: 'Olympian Discipline',
    greekTitle: 'Ολύμπια Πειθαρχία',
    description: 'Achieved a full 7-day study week streak!',
    icon: '🏛️',
    category: 'streak',
  },
  {
    id: 'century_club',
    title: 'Centurion of Time',
    greekTitle: 'Εκατόνταρχος',
    description: 'Surpassed 100 total minutes of Greek learning.',
    icon: '🏆',
    category: 'time',
  },
  {
    id: 'marathon_mind',
    title: 'Marathon Mind',
    greekTitle: 'Μαραθωνοδρόμος',
    description: 'Studied for 30+ minutes in a single day.',
    icon: '💎',
    category: 'time',
  },
  {
    id: 'night_owl',
    title: 'Night Owl Scholar',
    greekTitle: 'Νυκτερινός Σοφός',
    description: 'Studied under the stars after 9:00 PM.',
    icon: '🌙',
    category: 'session',
  },
  {
    id: 'early_bird',
    title: 'Dawn Seeker',
    greekTitle: 'Αυγερινός',
    description: 'Started learning early in the morning before 9:00 AM.',
    icon: '🌅',
    category: 'session',
  },
];

export function getLearningTimeStorageKey(userId?: string): string {
  const uid = userId || getActiveUserId();
  return `greek_deck_learning_time_${uid}`;
}

export function getLearningTimeData(userId?: string): LearningTimeData {
  const uid = userId || getActiveUserId();
  const key = getLearningTimeStorageKey(uid);
  try {
    const raw = localStorage.getItem(key);
    if (raw) {
      const parsed = JSON.parse(raw);
      return {
        userId: uid,
        records: parsed.records || {},
        allTimeSeconds: Number(parsed.allTimeSeconds) || 0,
        allTimeXP: Number(parsed.allTimeXP) || 0,
        bestDay: parsed.bestDay || { date: getTodayKey(), seconds: 0 },
        longestSessionSeconds: Number(parsed.longestSessionSeconds) || 0,
        unlockedBadgeIds: Array.isArray(parsed.unlockedBadgeIds) ? parsed.unlockedBadgeIds : [],
      };
    }
  } catch (e) {
    console.warn('Failed to parse learning time data', e);
  }

  return {
    userId: uid,
    records: {},
    allTimeSeconds: 0,
    allTimeXP: 0,
    bestDay: { date: getTodayKey(), seconds: 0 },
    longestSessionSeconds: 0,
    unlockedBadgeIds: [],
  };
}

export function saveLearningTimeData(data: LearningTimeData, userId?: string): void {
  const uid = userId || getActiveUserId();
  const key = getLearningTimeStorageKey(uid);
  try {
    const raw = JSON.stringify(data);
    localStorage.setItem(key, raw);
    mirrorKeyToIndexedDB(key, raw);
    if (typeof window !== 'undefined') {
      window.dispatchEvent(new CustomEvent('greek_deck_learning_time_change', { detail: data }));
    }
  } catch (err) {
    console.error('Failed to save learning time data', err);
  }
}

/**
 * Format seconds into a friendly compact duration string:
 * e.g. "45s", "8m 12s", "1h 24m"
 */
export function formatDuration(seconds: number): string {
  const s = Math.max(0, Math.round(seconds));
  if (s < 60) return `${s}s`;
  const mins = Math.floor(s / 60);
  const remSec = s % 60;
  if (mins < 60) {
    return remSec > 0 ? `${mins}m ${remSec}s` : `${mins}m`;
  }
  const hours = Math.floor(mins / 60);
  const remMins = mins % 60;
  return remMins > 0 ? `${hours}h ${remMins}m` : `${hours}h`;
}

/**
 * Format seconds into an expanded verbal duration string:
 * e.g. "12 minutes", "1 hour 15 minutes"
 */
export function formatDurationLong(seconds: number): string {
  const s = Math.max(0, Math.round(seconds));
  if (s < 60) return `${s} second${s === 1 ? '' : 's'}`;
  const mins = Math.floor(s / 60);
  if (mins < 60) return `${mins} minute${mins === 1 ? '' : 's'}`;
  const hours = Math.floor(mins / 60);
  const remMins = mins % 60;
  if (remMins === 0) return `${hours} hour${hours === 1 ? '' : 's'}`;
  return `${hours} hr ${remMins} min`;
}

/**
 * Helper to get date key for N days ago (YYYY-MM-DD)
 */
export function getDateKeyOffset(offsetDays: number): string {
  const d = new Date();
  d.setDate(d.getDate() - offsetDays);
  return `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, '0')}-${String(d.getDate()).padStart(2, '0')}`;
}

/**
 * Get current week start (Monday) and end dates
 */
function getWeekRange(offsetWeeks = 0): { start: Date; end: Date } {
  const now = new Date();
  now.setDate(now.getDate() - offsetWeeks * 7);
  const day = now.getDay();
  // Greek / ISO week starts on Monday (1). Sunday is 0 -> convert to 7
  const diffToMon = (day === 0 ? -6 : 1) - day;
  const monday = new Date(now);
  monday.setDate(now.getDate() + diffToMon);
  monday.setHours(0, 0, 0, 0);

  const sunday = new Date(monday);
  sunday.setDate(monday.getDate() + 6);
  sunday.setHours(23, 59, 59, 999);

  return { start: monday, end: sunday };
}

/**
 * Log active study time.
 * Calculates XP earned, updates streaks, checks records & unlocks badges.
 */
export function addActiveLearningTime(
  sessionSeconds: number,
  cardsDelta: number = 0,
  userId?: string
): { updatedData: LearningTimeData; earnedXP: number; newBadges: AchievementBadge[] } {
  if (sessionSeconds <= 0 && cardsDelta <= 0) {
    const current = getLearningTimeData(userId);
    return { updatedData: current, earnedXP: 0, newBadges: [] };
  }

  const uid = userId || getActiveUserId();
  const data = getLearningTimeData(uid);
  const prefs = getUserStudyPreferences(uid);
  const dailyTimeGoalMinutes = prefs.dailyTimeGoalMinutes || 15;
  const dailyTimeGoalSeconds = dailyTimeGoalMinutes * 60;

  const today = getTodayKey();
  const yesterday = getDateKeyOffset(1);
  const yesterdayRecord = data.records[yesterday];
  const yesterdaySeconds = yesterdayRecord ? yesterdayRecord.seconds : 0;

  // XP calculation: 10 XP per active minute + 2 XP per card reviewed
  const baseMinutesXP = Math.round((sessionSeconds / 60) * 10);
  const cardXP = cardsDelta * 2;
  const earnedXP = Math.max(1, baseMinutesXP + cardXP);

  // Update or create today's record
  const currentTodayRecord: DailyTimeRecord = data.records[today] || {
    date: today,
    seconds: 0,
    sessionsCount: 0,
    cardsReviewed: 0,
    xp: 0,
    lastActive: new Date().toISOString(),
  };

  const prevTodaySeconds = currentTodayRecord.seconds;
  const newTodaySeconds = prevTodaySeconds + sessionSeconds;

  const updatedTodayRecord: DailyTimeRecord = {
    ...currentTodayRecord,
    seconds: newTodaySeconds,
    sessionsCount: currentTodayRecord.sessionsCount + 1,
    cardsReviewed: currentTodayRecord.cardsReviewed + cardsDelta,
    xp: currentTodayRecord.xp + earnedXP,
    lastActive: new Date().toISOString(),
  };

  data.records[today] = updatedTodayRecord;
  data.allTimeSeconds += sessionSeconds;
  data.allTimeXP += earnedXP;

  if (sessionSeconds > data.longestSessionSeconds) {
    data.longestSessionSeconds = sessionSeconds;
  }

  // Check personal best day
  if (newTodaySeconds > data.bestDay.seconds) {
    data.bestDay = {
      date: today,
      seconds: newTodaySeconds,
    };
  }

  // Check achievements
  const newBadges: AchievementBadge[] = [];
  const unlockedSet = new Set(data.unlockedBadgeIds);

  const checkBadge = (badgeId: string, condition: boolean) => {
    if (condition && !unlockedSet.has(badgeId)) {
      unlockedSet.add(badgeId);
      data.unlockedBadgeIds.push(badgeId);
      const b = ALL_ACHIEVEMENTS.find((a) => a.id === badgeId);
      if (b) {
        newBadges.push({ ...b, unlockedAt: new Date().toISOString() });
      }
    }
  };

  // 1. Promethean spark
  checkBadge('first_spark', data.allTimeSeconds > 0);

  // 2. Yesterday Crusher: surpassed yesterday (when yesterday had learning time)
  checkBadge('yesterday_crusher', yesterdaySeconds > 0 && newTodaySeconds > yesterdaySeconds);

  // 3. Daily Champion: met daily time goal
  checkBadge('daily_champion', newTodaySeconds >= dailyTimeGoalSeconds);

  // 4. Deep Focus: session >= 15 minutes
  checkBadge('deep_focus', sessionSeconds >= 15 * 60);

  // 5. Marathon Mind: 30+ minutes in a single day
  checkBadge('marathon_mind', newTodaySeconds >= 30 * 60);

  // 6. Centurion: 100+ minutes all time
  checkBadge('century_club', data.allTimeSeconds >= 100 * 60);

  // Time-of-day checks
  const currentHour = new Date().getHours();
  checkBadge('night_owl', currentHour >= 21 || currentHour < 4);
  checkBadge('early_bird', currentHour >= 5 && currentHour < 9);

  // Streak checks
  let consecutiveDays = 0;
  for (let i = 0; i < 30; i++) {
    const dKey = getDateKeyOffset(i);
    const rec = data.records[dKey];
    if (rec && rec.seconds >= 60) {
      consecutiveDays++;
    } else {
      break;
    }
  }
  checkBadge('streak_3', consecutiveDays >= 3);
  checkBadge('streak_7', consecutiveDays >= 7);

  saveLearningTimeData(data, uid);
  notifyProgressChanged();

  return { updatedData: data, earnedXP, newBadges };
}

export interface DayHistoryItem {
  date: string;
  dayLabel: string; // e.g. "Mon"
  fullDate: string; // e.g. "Nov 11"
  seconds: number;
  formatted: string;
  goalMet: boolean;
  isToday: boolean;
  isYesterday: boolean;
  cardsReviewed: number;
  xp: number;
}

export interface LearningStatsComparison {
  todaySeconds: number;
  todayFormatted: string;
  yesterdaySeconds: number;
  yesterdayFormatted: string;
  diffFromYesterdaySeconds: number;
  diffFromYesterdayFormatted: string;
  pctFromYesterday: number | null; // e.g. +45, -20, or null if yesterday was 0
  isAheadOfYesterday: boolean;
  isTiedWithYesterday: boolean;
  remainingToBeatYesterdayFormatted: string;

  thisWeekSeconds: number;
  thisWeekFormatted: string;
  lastWeekSeconds: number;
  lastWeekFormatted: string;
  diffFromLastWeekSeconds: number;
  pctFromLastWeek: number | null;

  allTimeSeconds: number;
  allTimeFormatted: string;
  allTimeXP: number;

  dailyAverage7DaysSeconds: number;
  dailyAverage7DaysFormatted: string;

  bestDay: {
    date: string;
    seconds: number;
    formatted: string;
  };
  isBestDayToday: boolean;

  todayGoalMinutes: number;
  todayGoalSeconds: number;
  todayGoalProgressPct: number;
  isGoalMet: boolean;

  currentRank: GreekWisdomRank;
  nextRank: GreekWisdomRank | null;
  progressToNextRankPct: number;
  secondsToNextRank: number;
  formattedRemainingToNextRank: string;

  history7Days: DayHistoryItem[];
  history14Days: DayHistoryItem[];

  motivationalMessage: {
    title: string;
    text: string;
    type: 'beating_yesterday' | 'goal_reached' | 'ahead' | 'catching_up' | 'start_day' | 'personal_best';
    icon: string;
  };

  unlockedBadges: AchievementBadge[];
  allBadges: AchievementBadge[];
}

/**
 * Compute rich comparisons and motivational analytics
 */
export function getLearningStatsComparison(userId?: string): LearningStatsComparison {
  const uid = userId || getActiveUserId();
  const data = getLearningTimeData(uid);
  const prefs = getUserStudyPreferences(uid);
  const todayGoalMinutes = prefs.dailyTimeGoalMinutes || 15;
  const todayGoalSeconds = todayGoalMinutes * 60;

  const todayKey = getTodayKey();
  const yesterdayKey = getDateKeyOffset(1);

  const todayRecord = data.records[todayKey];
  const todaySeconds = todayRecord ? todayRecord.seconds : 0;

  const yesterdayRecord = data.records[yesterdayKey];
  const yesterdaySeconds = yesterdayRecord ? yesterdayRecord.seconds : 0;

  const diffFromYesterdaySeconds = todaySeconds - yesterdaySeconds;
  const isAheadOfYesterday = todaySeconds > yesterdaySeconds;
  const isTiedWithYesterday = todaySeconds === yesterdaySeconds && yesterdaySeconds > 0;

  let pctFromYesterday: number | null = null;
  if (yesterdaySeconds > 0) {
    pctFromYesterday = Math.round(((todaySeconds - yesterdaySeconds) / yesterdaySeconds) * 100);
  }

  const remainingToBeatYesterdaySeconds = Math.max(0, yesterdaySeconds - todaySeconds + 1);
  const remainingToBeatYesterdayFormatted = formatDuration(remainingToBeatYesterdaySeconds);

  // Weekly calculations
  const thisWeekRange = getWeekRange(0);
  const lastWeekRange = getWeekRange(1);

  let thisWeekSeconds = 0;
  let lastWeekSeconds = 0;

  for (const [dateStr, rec] of Object.entries(data.records)) {
    const d = new Date(dateStr + 'T12:00:00');
    if (d >= thisWeekRange.start && d <= thisWeekRange.end) {
      thisWeekSeconds += rec.seconds;
    } else if (d >= lastWeekRange.start && d <= lastWeekRange.end) {
      lastWeekSeconds += rec.seconds;
    }
  }

  const diffFromLastWeekSeconds = thisWeekSeconds - lastWeekSeconds;
  let pctFromLastWeek: number | null = null;
  if (lastWeekSeconds > 0) {
    pctFromLastWeek = Math.round(((thisWeekSeconds - lastWeekSeconds) / lastWeekSeconds) * 100);
  }

  // 7-day and 14-day history series
  const buildHistory = (days: number): DayHistoryItem[] => {
    const list: DayHistoryItem[] = [];
    const dayNames = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat'];
    const monthNames = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

    for (let i = days - 1; i >= 0; i--) {
      const dateKey = getDateKeyOffset(i);
      const parts = dateKey.split('-');
      const dObj = new Date(Number(parts[0]), Number(parts[1]) - 1, Number(parts[2]));
      const rec = data.records[dateKey];
      const secs = rec ? rec.seconds : 0;

      list.push({
        date: dateKey,
        dayLabel: dayNames[dObj.getDay()],
        fullDate: `${monthNames[dObj.getMonth()]} ${dObj.getDate()}`,
        seconds: secs,
        formatted: formatDuration(secs),
        goalMet: secs >= todayGoalSeconds,
        isToday: i === 0,
        isYesterday: i === 1,
        cardsReviewed: rec ? rec.cardsReviewed : 0,
        xp: rec ? rec.xp : 0,
      });
    }
    return list;
  };

  const history7Days = buildHistory(7);
  const history14Days = buildHistory(14);

  const last7Sum = history7Days.reduce((acc, h) => acc + h.seconds, 0);
  const dailyAverage7DaysSeconds = Math.round(last7Sum / 7);

  // Goal progress
  const todayGoalProgressPct = Math.min(100, Math.round((todaySeconds / todayGoalSeconds) * 100));
  const isGoalMet = todaySeconds >= todayGoalSeconds;

  // Best day
  const isBestDayToday = Boolean(todaySeconds > 0 && todaySeconds >= data.bestDay.seconds);

  // Rank progression
  let currentRank = GREEK_RANKS[0];
  let nextRank: GreekWisdomRank | null = GREEK_RANKS[1];

  for (let i = GREEK_RANKS.length - 1; i >= 0; i--) {
    if (data.allTimeSeconds >= GREEK_RANKS[i].minSeconds) {
      currentRank = GREEK_RANKS[i];
      nextRank = i < GREEK_RANKS.length - 1 ? GREEK_RANKS[i + 1] : null;
      break;
    }
  }

  let progressToNextRankPct = 100;
  let secondsToNextRank = 0;
  let formattedRemainingToNextRank = 'Max Rank Achieved';

  if (nextRank) {
    const span = nextRank.minSeconds - currentRank.minSeconds;
    const progress = data.allTimeSeconds - currentRank.minSeconds;
    progressToNextRankPct = Math.min(100, Math.max(0, Math.round((progress / span) * 100)));
    secondsToNextRank = Math.max(0, nextRank.minSeconds - data.allTimeSeconds);
    formattedRemainingToNextRank = `${formatDurationLong(secondsToNextRank)} to ${nextRank.title}`;
  }

  // Badges status
  const unlockedSet = new Set(data.unlockedBadgeIds);
  const unlockedBadges = ALL_ACHIEVEMENTS.filter((b) => unlockedSet.has(b.id));
  const allBadgesWithStatus = ALL_ACHIEVEMENTS.map((b) => ({
    ...b,
    isUnlocked: unlockedSet.has(b.id),
  }));

  // Construct motivational message based on real data
  let motivationalMessage: LearningStatsComparison['motivationalMessage'];

  if (isBestDayToday && todaySeconds > 180) {
    motivationalMessage = {
      title: '🎉 All-Time Personal Best!',
      text: `You've set a new record today (${formatDuration(todaySeconds)})! Aristotle would be astounded by your focus.`,
      type: 'personal_best',
      icon: '🏆',
    };
  } else if (isGoalMet && isAheadOfYesterday && yesterdaySeconds > 0) {
    motivationalMessage = {
      title: '⚡ Crushing Yesterday & Daily Goal!',
      text: `Εύγε! You're ${formatDuration(diffFromYesterdaySeconds)} ahead of yesterday (${pctFromYesterday ? `+${pctFromYesterday}%` : ''}) and conquered your daily target!`,
      type: 'beating_yesterday',
      icon: '🚀',
    };
  } else if (isAheadOfYesterday && yesterdaySeconds > 0) {
    motivationalMessage = {
      title: '🔥 Beating Yesterday!',
      text: `You've learned ${formatDuration(diffFromYesterdaySeconds)} more than yesterday! Keep this momentum burning!`,
      type: 'beating_yesterday',
      icon: '🔥',
    };
  } else if (isGoalMet) {
    motivationalMessage = {
      title: '🎯 Daily Target Conquered!',
      text: `You've reached your ${todayGoalMinutes}m daily target (${formatDuration(todaySeconds)}). Push further to widen your lead!`,
      type: 'goal_reached',
      icon: '🏛️',
    };
  } else if (yesterdaySeconds > 0 && todaySeconds > 0) {
    motivationalMessage = {
      title: '⚔️ Chasing Yesterday',
      text: `Just ${remainingToBeatYesterdayFormatted} needed to overtake yesterday's ${formatDuration(yesterdaySeconds)} mark! You can do it!`,
      type: 'catching_up',
      icon: '⚔️',
    };
  } else if (todaySeconds > 0) {
    motivationalMessage = {
      title: '🌱 Strong Start Today!',
      text: `${formatDuration(todaySeconds)} logged so far. Every minute builds lasting neural pathways in Greek!`,
      type: 'ahead',
      icon: '🌿',
    };
  } else if (yesterdaySeconds > 0) {
    motivationalMessage = {
      title: '☀️ Ready for Today?',
      text: `You studied for ${formatDuration(yesterdaySeconds)} yesterday. A quick 10-minute drill will keep your streak alive!`,
      type: 'start_day',
      icon: '⚡',
    };
  } else {
    motivationalMessage = {
      title: '🏛️ Begin Your Greek Journey',
      text: 'Start a study session to track your active learning time and unlock ancient wisdom ranks!',
      type: 'start_day',
      icon: '🦉',
    };
  }

  return {
    todaySeconds,
    todayFormatted: formatDuration(todaySeconds),
    yesterdaySeconds,
    yesterdayFormatted: formatDuration(yesterdaySeconds),
    diffFromYesterdaySeconds,
    diffFromYesterdayFormatted: formatDuration(Math.abs(diffFromYesterdaySeconds)),
    pctFromYesterday,
    isAheadOfYesterday,
    isTiedWithYesterday,
    remainingToBeatYesterdayFormatted,

    thisWeekSeconds,
    thisWeekFormatted: formatDuration(thisWeekSeconds),
    lastWeekSeconds,
    lastWeekFormatted: formatDuration(lastWeekSeconds),
    diffFromLastWeekSeconds,
    pctFromLastWeek,

    allTimeSeconds: data.allTimeSeconds,
    allTimeFormatted: formatDuration(data.allTimeSeconds),
    allTimeXP: data.allTimeXP,

    dailyAverage7DaysSeconds,
    dailyAverage7DaysFormatted: formatDuration(dailyAverage7DaysSeconds),

    bestDay: {
      date: data.bestDay.date,
      seconds: data.bestDay.seconds,
      formatted: formatDuration(data.bestDay.seconds),
    },
    isBestDayToday,

    todayGoalMinutes,
    todayGoalSeconds,
    todayGoalProgressPct,
    isGoalMet,

    currentRank,
    nextRank,
    progressToNextRankPct,
    secondsToNextRank,
    formattedRemainingToNextRank,

    history7Days,
    history14Days,

    motivationalMessage,

    unlockedBadges,
    allBadges: allBadgesWithStatus,
  };
}

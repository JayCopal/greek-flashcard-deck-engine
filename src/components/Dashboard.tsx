import { useState, useEffect, useMemo } from 'react';
import { DeckData, Lesson, Unit, LessonStatus } from '../types/schema';
import { getAllSRSData } from '../utils/srs';
import { 
  getUserLessonStatus, 
  setUserLessonStatus, 
  getUserLessonNotes, 
  getActiveUser,
  getLastStudiedLesson,
  getDailyReviewData,
  getUserStudyPreferences
} from '../utils/userStorage';
import { 
  parseLessonCode, 
  formatLessonLabel, 
  getGroupTitle, 
  extractUnitContext, 
  getGroupAccentStyles,
  getGroupMetadata 
} from '../utils/unitNaming';
import { LearningTimeWidget } from './LearningTimeWidget';
import { 
  BookOpen, 
  Play, 
  FileText, 
  Search, 
  Volume2, 
  BookMarked, 
  X, 
  ChevronRight, 
  ChevronDown,
  ChevronUp,
  Filter, 
  Flame, 
  Target, 
  Sparkles, 
  ArrowRight,
  Layers,
  Award,
  Compass,
  Mic,
  GraduationCap,
  Check
} from 'lucide-react';

interface DashboardProps {
  deck: DeckData;
  onSelectLesson: (unitId: string, lessonId: string) => void;
  onStartStudy: (
    cards: Lesson['entries'],
    title: string,
    lessonNotes?: string,
    lessonNumber?: string,
    options?: { hideExcluded?: boolean; hideLearned?: boolean },
    unitId?: string,
    lessonId?: string
  ) => void;
  onRefresh: () => void;
}

type GroupFilter = 'all' | string;
type StatusFilter = 'all' | 'not_started' | 'in_progress_1' | 'in_progress_2' | 'in_progress_3' | 'in_progress_4' | 'in_progress_5' | 'learned';

interface ParsedLessonInfo {
  primaryTitle: string;
  subtitle?: string;
  groupLabel: string;
  unitContext: string;
  pageRange?: string;
  isTextbook: boolean;
  isExpansion: boolean;
  expansionTarget?: string;
}

/**
 * Returns color-coded Tailwind classes with increasing intensity of yellow/orange
 * as lesson mastery progresses from Level 1 to Level 5.
 */
export function getLessonStatusClasses(status: LessonStatus): string {
  switch (status) {
    case 'learned':
      return 'bg-emerald-950/90 text-emerald-300 border-emerald-600/70 hover:bg-emerald-900';
    case 'in_progress_5':
      // Level 5: Deep intense flame orange
      return 'bg-orange-950 text-orange-400 border-orange-500 font-extrabold shadow-sm shadow-orange-500/20 hover:bg-orange-900';
    case 'in_progress_4':
      // Level 4: Bright vibrant orange
      return 'bg-orange-950/80 text-orange-300 border-orange-500/80 hover:bg-orange-900/80';
    case 'in_progress_3':
      // Level 3: Warm golden amber (transitioning into orange)
      return 'bg-amber-950/80 text-amber-300 border-amber-500/80 hover:bg-amber-900/70';
    case 'in_progress_2':
      // Level 2: Medium bright yellow
      return 'bg-yellow-950/70 text-yellow-300 border-yellow-500/70 hover:bg-yellow-900/60';
    case 'in_progress_1':
    case 'in_progress':
      // Level 1: Soft / pale yellow
      return 'bg-yellow-950/40 text-yellow-200 border-yellow-600/50 hover:bg-yellow-950/60';
    case 'not_started':
    default:
      return 'bg-slate-900/90 text-slate-400 border-slate-700 hover:text-slate-200';
  }
}

/**
 * Intelligent parser that extracts clean Greek title, subtitle, textbook page ranges,
 * group metadata, and thematic unit context without repeating titles.
 */
function parseLessonInfo(unit: Unit, primaryLesson?: Lesson): ParsedLessonInfo {
  const code = parseLessonCode(unit.order || unit.id);
  const isTextbook = code.group.toLowerCase().startsWith('klik') || 
    String(unit.order).toUpperCase().startsWith('10') || 
    Number(unit.order) >= 100 ||
    unit.id.startsWith('unit-1');
  const isExpansion = Boolean(
    unit.is_expansion || 
    code.suffix !== 'A' || 
    unit.id.endsWith('b') || 
    unit.id.endsWith('c') || 
    String(unit.order).toUpperCase().endsWith('B') ||
    String(unit.order).toUpperCase().endsWith('C')
  );
  const expansionTarget = unit.expansion_of || (isExpansion ? `${code.group}-${String(code.orderNum).padStart(2, '0')}-A` : undefined);

  // Extract page ranges if present (e.g., "Pages 25-41" or "Σελίδες 25-41")
  const combinedText = `${unit.title} ${primaryLesson?.title || ''}`;
  const pageMatch = combinedText.match(/(?:Pages|Σελίδες)\s*([\d\s–-]+)/i);
  const pageRange = pageMatch ? pageMatch[1].trim() : undefined;

  const rawTitle = primaryLesson?.title || unit.title;
  const unitContext = extractUnitContext(unit.title, unit.order);

  if (isTextbook) {
    let clean = rawTitle;
    clean = clean.replace(/\s*\((?:Pages|Σελίδες)[^)]+\)/i, '').trim();
    clean = clean.replace(/^Κλικ στα Ελληνικά [^:]+:\s*(?:Σελίδες\s*[\d\s–-]+)?\s*\(?/i, '').replace(/\)$/, '').trim();

    return {
      primaryTitle: clean,
      subtitle: primaryLesson?.description || (isExpansion ? 'Grammar patterns, sentence syntax & accusative expressions' : undefined),
      groupLabel: getGroupTitle(code.group),
      unitContext,
      pageRange: pageRange ? `pp. ${pageRange}` : undefined,
      isTextbook: true,
      isExpansion,
      expansionTarget,
    };
  }

  // Core thematic units: format "Greek Title (English Subtitle)"
  const parenMatch = rawTitle.match(/^([^(]+)\s*\(([^)]+)\)$/);
  if (parenMatch) {
    return {
      primaryTitle: parenMatch[1].trim(),
      subtitle: parenMatch[2].trim(),
      groupLabel: getGroupTitle(code.group),
      unitContext,
      isTextbook: false,
      isExpansion: false,
    };
  }

  return {
    primaryTitle: rawTitle,
    subtitle: primaryLesson?.description,
    groupLabel: getGroupTitle(code.group),
    unitContext,
    isTextbook: false,
    isExpansion: false,
  };
}

export const Dashboard: React.FC<DashboardProps> = ({
  deck,
  onSelectLesson,
  onStartStudy,
  onRefresh,
}) => {
  const [activeUser, setActiveUser] = useState(getActiveUser());
  const [version, setVersion] = useState(0);

  // Filter and search states
  const [groupFilter, setGroupFilter] = useState<GroupFilter>('all');
  const [statusFilter, setStatusFilter] = useState<StatusFilter>('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [viewingNotesLesson, setViewingNotesLesson] = useState<{ lesson: Lesson; lessonLabel: string } | null>(null);

  useEffect(() => {
    const handleUpdate = () => {
      setActiveUser(getActiveUser());
      setVersion((v) => v + 1);
    };
    window.addEventListener('greek_deck_user_change', handleUpdate);
    window.addEventListener('greek_deck_progress_change', handleUpdate);
    window.addEventListener('greek_deck_daily_change', handleUpdate);
    window.addEventListener('greek_deck_last_lesson_change', handleUpdate);
    return () => {
      window.removeEventListener('greek_deck_user_change', handleUpdate);
      window.removeEventListener('greek_deck_progress_change', handleUpdate);
      window.removeEventListener('greek_deck_daily_change', handleUpdate);
      window.removeEventListener('greek_deck_last_lesson_change', handleUpdate);
    };
  }, []);

  const { units } = deck;

  // Compute SRS statistics for active user
  const srsMap = useMemo(() => getAllSRSData(activeUser.id), [activeUser.id]);

  const getEffectiveLessonStatus = (lesson: Lesson): LessonStatus => {
    return getUserLessonStatus(lesson.unit_id, lesson.lesson_id, lesson.lesson_status, activeUser.id);
  };

  const getEffectiveLessonNotes = (lesson: Lesson): string => {
    return getUserLessonNotes(lesson.unit_id, lesson.lesson_id, lesson.lesson_notes, activeUser.id);
  };

  // Compute lesson status statistics for active user across levels 1 to 5
  const allLessons = useMemo(() => units.flatMap((u) => u.lessons), [units]);
  const lessonsNotStartedCount = useMemo(() => allLessons.filter((l) => getEffectiveLessonStatus(l) === 'not_started').length, [allLessons, activeUser.id]);
  const lessonsInProgress1Count = useMemo(() => allLessons.filter((l) => {
    const s = getEffectiveLessonStatus(l);
    return s === 'in_progress_1' || s === 'in_progress';
  }).length, [allLessons, activeUser.id]);
  const lessonsInProgress2Count = useMemo(() => allLessons.filter((l) => getEffectiveLessonStatus(l) === 'in_progress_2').length, [allLessons, activeUser.id]);
  const lessonsInProgress3Count = useMemo(() => allLessons.filter((l) => getEffectiveLessonStatus(l) === 'in_progress_3').length, [allLessons, activeUser.id]);
  const lessonsInProgress4Count = useMemo(() => allLessons.filter((l) => getEffectiveLessonStatus(l) === 'in_progress_4').length, [allLessons, activeUser.id]);
  const lessonsInProgress5Count = useMemo(() => allLessons.filter((l) => getEffectiveLessonStatus(l) === 'in_progress_5').length, [allLessons, activeUser.id]);
  const lessonsLearnedCount = useMemo(() => allLessons.filter((l) => getEffectiveLessonStatus(l) === 'learned').length, [allLessons, activeUser.id]);

  const handleQuickLessonStatusChange = async (unitId: string, lessonId: string, newStatus: LessonStatus) => {
    setUserLessonStatus(unitId, lessonId, newStatus, activeUser.id);
    try {
      const res = await fetch(`/api/lesson/${unitId}/${lessonId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ lesson_status: newStatus }),
      });
      if (res.ok) {
        onRefresh();
      }
    } catch {
      // Ignored in offline mode
    }
  };

  // Helper to render appropriate icon for curriculum group
  const renderGroupIcon = (groupId: string, className = "w-5 h-5") => {
    const norm = groupId.trim().toLowerCase().replace(/[-_]/g, '');
    if (norm.startsWith('klika1') || norm === 'klik1') {
      return <BookOpen className={className} />;
    }
    if (norm.startsWith('klika2') || norm === 'klik2') {
      return <BookMarked className={className} />;
    }
    if (norm.startsWith('kega2sp') || norm === 'sp' || norm === 'speaking') {
      return <Mic className={className} />;
    }
    if (norm.startsWith('kega2p2') || norm === 'a2p2') {
      return <Compass className={className} />;
    }
    if (norm.startsWith('kega2') || norm === 'a2p1' || norm === 'a2') {
      return <Award className={className} />;
    }
    if (norm.startsWith('cyp')) {
      return <GraduationCap className={className} />;
    }
    return <Sparkles className={className} />;
  };

  // Group collapse state for default overview
  const [collapsedGroups, setCollapsedGroups] = useState<Record<string, boolean>>({});

  const toggleGroupCollapse = (groupId: string) => {
    setCollapsedGroups((prev) => ({
      ...prev,
      [groupId]: !prev[groupId],
    }));
  };

  // Dynamically group curriculum collections with comprehensive learning & audio metrics
  const availableGroups = useMemo(() => {
    const groupMap = new Map<string, {
      id: string;
      name: string;
      lessonsCount: number;
      cardsCount: number;
      learnedCardsCount: number;
      audioVerifiedCount: number;
      audioTotalCount: number;
      allCards: Lesson['entries'];
    }>();

    for (const unit of units) {
      const code = parseLessonCode(unit.order || unit.id);
      const groupId = code.group;
      const unitCards = unit.lessons.flatMap((l) => l.entries);
      const cardCount = unitCards.length;
      const learnedCount = unitCards.filter((c) => srsMap[c.id]?.isLearned).length;
      const verifiedAudio = unit.verified_entries || 0;
      const totalAudio = unit.total_entries || cardCount;

      const existing = groupMap.get(groupId);
      if (existing) {
        existing.lessonsCount += 1;
        existing.cardsCount += cardCount;
        existing.learnedCardsCount += learnedCount;
        existing.audioVerifiedCount += verifiedAudio;
        existing.audioTotalCount += totalAudio;
        existing.allCards.push(...unitCards);
      } else {
        groupMap.set(groupId, {
          id: groupId,
          name: getGroupTitle(groupId),
          lessonsCount: 1,
          cardsCount: cardCount,
          learnedCardsCount: learnedCount,
          audioVerifiedCount: verifiedAudio,
          audioTotalCount: totalAudio,
          allCards: [...unitCards],
        });
      }
    }

    const priorityOrder: Record<string, number> = {
      'OG-A1': 1,
      'Klik-A1': 2,
      'Klik-A2': 3,
      'KEG-A2-P1': 4,
      'KEG-A2-P2': 5,
      'KEG-A2-SP': 6,
      'CYP-Exam': 7,
    };

    return Array.from(groupMap.values())
      .map((g) => ({
        ...g,
        masteryPercentage: g.cardsCount > 0 ? Math.round((g.learnedCardsCount / g.cardsCount) * 100) : 0,
        audioPercentage: g.audioTotalCount > 0 ? Math.round((g.audioVerifiedCount / g.audioTotalCount) * 100) : 0,
      }))
      .sort((a, b) => {
        const pA = priorityOrder[a.id] ?? 99;
        const pB = priorityOrder[b.id] ?? 99;
        if (pA !== pB) return pA - pB;
        return a.id.localeCompare(b.id);
      });
  }, [units, srsMap]);

  const areAllGroupsCollapsed = useMemo(() => {
    if (availableGroups.length === 0) return false;
    return availableGroups.every((g) => collapsedGroups[g.id]);
  }, [availableGroups, collapsedGroups]);

  const toggleCollapseAll = () => {
    if (areAllGroupsCollapsed) {
      setCollapsedGroups({});
    } else {
      const all: Record<string, boolean> = {};
      for (const g of availableGroups) {
        all[g.id] = true;
      }
      setCollapsedGroups(all);
    }
  };

  const totalCardsCount = useMemo(() => allLessons.flatMap((l) => l.entries).length, [allLessons]);
  const totalLearnedCardsCount = useMemo(() => {
    return units.flatMap((u) => u.lessons.flatMap((l) => l.entries)).filter((c) => srsMap[c.id]?.isLearned).length;
  }, [units, srsMap]);
  const totalMasteryPct = totalCardsCount > 0 ? Math.round((totalLearnedCardsCount / totalCardsCount) * 100) : 0;

  // Filtered units computation
  const filteredUnits = useMemo(() => {
    return units.filter((unit) => {
      const code = parseLessonCode(unit.order || unit.id);
      
      // Group filter (A1, A2, etc.)
      if (groupFilter !== 'all' && code.group.toLowerCase() !== groupFilter.toLowerCase()) {
        return false;
      }

      // Status filter: match if any lesson in the unit matches the status
      if (statusFilter !== 'all') {
        const hasMatchingStatus = unit.lessons.some((l) => {
          const s = getEffectiveLessonStatus(l);
          if (statusFilter === 'in_progress_1') return s === 'in_progress_1' || s === 'in_progress';
          return s === statusFilter;
        });
        if (!hasMatchingStatus) return false;
      }

      // Search query
      if (searchQuery.trim()) {
        const q = searchQuery.toLowerCase().trim();
        const primaryLesson = unit.lessons[0];
        const parsed = parseLessonInfo(unit, primaryLesson);
        const matchTitle = unit.title.toLowerCase().includes(q) || 
          parsed.primaryTitle.toLowerCase().includes(q) || 
          (parsed.subtitle && parsed.subtitle.toLowerCase().includes(q)) ||
          parsed.unitContext.toLowerCase().includes(q) ||
          code.formatted.toLowerCase().includes(q) ||
          code.group.toLowerCase().includes(q) ||
          String(unit.order).toLowerCase().includes(q);
        
        const matchCards = unit.lessons.some(l => 
          l.entries.some(e => e.greek.toLowerCase().includes(q) || e.english.toLowerCase().includes(q))
        );

        if (!matchTitle && !matchCards) return false;
      }

      return true;
    });
  }, [units, groupFilter, statusFilter, searchQuery, activeUser.id]);

  // Is viewing default all groups & no search
  const isDefaultView = groupFilter === 'all' && statusFilter === 'all' && !searchQuery.trim();

  // Quick Resume Lesson
  const lastStudied = useMemo(() => getLastStudiedLesson(activeUser.id), [activeUser.id, version]);
  const resumeUnit = useMemo(() => {
    if (!lastStudied?.unitId) return null;
    return units.find((u) => 
      u.id === lastStudied.unitId || 
      u.order === lastStudied.unitId || 
      `unit-${String(u.order).toLowerCase()}` === lastStudied.unitId.toLowerCase()
    );
  }, [units, lastStudied]);

  const resumeUnitCards = useMemo(() => {
    if (!resumeUnit) return [];
    return resumeUnit.lessons.flatMap((l) => l.entries);
  }, [resumeUnit]);

  const resumeLesson = useMemo(() => {
    if (!resumeUnit) return null;
    if (lastStudied?.lessonId) {
      const found = resumeUnit.lessons.find((l) => l.lesson_id === lastStudied.lessonId);
      if (found) return found;
    }
    return resumeUnit.lessons[0] || null;
  }, [resumeUnit, lastStudied]);

  const resumeUnitLearnedCount = useMemo(() => {
    return resumeUnitCards.filter((c) => srsMap[c.id]?.isLearned).length;
  }, [resumeUnitCards, srsMap]);

  const resumeUnitLearnedPct = resumeUnitCards.length > 0 
    ? Math.round((resumeUnitLearnedCount / resumeUnitCards.length) * 100) 
    : 0;

  // Daily Review & Streak
  const dailyData = useMemo(() => getDailyReviewData(activeUser.id), [activeUser.id, version]);
  const studyPrefs = useMemo(() => getUserStudyPreferences(activeUser.id), [activeUser.id, version]);
  const dailyGoal = studyPrefs.dailyGoal || 20;
  const isGoalReached = dailyData.count >= dailyGoal;
  const dailyGoalPct = Math.min(100, Math.round((dailyData.count / dailyGoal) * 100));

  // Render a clean Lesson Card
  const renderLessonCard = (unit: Unit) => {
    const isSingleLesson = unit.lessons.length === 1;
    const primaryLesson = unit.lessons[0];
    const parsed = parseLessonInfo(unit, primaryLesson);
    const code = parseLessonCode(unit.order || unit.id);
    const lessonLabel = formatLessonLabel(unit);
    
    // Aggregate cards & progress
    const unitCards = unit.lessons.flatMap((l) => l.entries);
    const unitLearnedCount = unitCards.filter((c) => srsMap[c.id]?.isLearned).length;
    const unitLearnedPct = unitCards.length > 0 ? Math.round((unitLearnedCount / unitCards.length) * 100) : 0;
    const unitEffectiveStatus = primaryLesson ? getEffectiveLessonStatus(primaryLesson) : 'not_started';
    const notes = primaryLesson ? getEffectiveLessonNotes(primaryLesson) : '';
    const groupAccent = getGroupAccentStyles(code.group);

    return (
      <div 
        key={unit.id}
        className={`lesson-card bg-slate-900/90 rounded-2xl p-5 sm:p-6 border-2 border-slate-700/80 border-l-[6px] ${groupAccent.borderLeft} ${groupAccent.borderLeftHover} hover:border-y-slate-500 hover:border-r-slate-500 transition-all duration-300 shadow-xl shadow-black/30 ${groupAccent.hoverGlow} group flex flex-col justify-between`}
      >
        <div>
          {/* Line 1: Lesson Name & Progress Status */}
          <div className="flex flex-wrap items-center gap-2 sm:gap-2.5 mb-2.5">
            {/* Lesson Code Pill */}
            <span className={`px-2.5 py-1 rounded-lg text-xs font-black tracking-wider uppercase border shadow-sm ${groupAccent.pillBg}`}>
              {lessonLabel}
            </span>

            {/* Quick Status Selector */}
            {isSingleLesson && primaryLesson && (
              <select
                value={unitEffectiveStatus === 'in_progress' ? 'in_progress_1' : unitEffectiveStatus}
                onChange={(e) => handleQuickLessonStatusChange(unit.id, primaryLesson.lesson_id, e.target.value as LessonStatus)}
                className={`text-[11px] font-bold px-2.5 py-1 rounded-lg border transition-all cursor-pointer focus:outline-none focus:ring-1 focus:ring-amber-500 ${getLessonStatusClasses(unitEffectiveStatus)}`}
                title="Change Lesson Mastery Status (Levels 1 to 5)"
              >
                <option value="not_started">⚪ Not Started ⚪</option>
                <option value="in_progress_1">🟡 In Progress 1 🟡</option>
                <option value="in_progress_2">🟡 In Progress 2 🟡</option>
                <option value="in_progress_3">🟠 In Progress 3 🟠</option>
                <option value="in_progress_4">🟠 In Progress 4 🟠</option>
                <option value="in_progress_5">🟠 In Progress 5 🟠</option>
                <option value="learned">🟢 Learned 🟢</option>
              </select>
            )}
          </div>

          {/* Line 2: Group Badge First, Notes Button, Page Numbers */}
          <div className="flex flex-wrap items-center gap-2 mb-3">
            {/* Group Badge */}
            <button
              type="button"
              onClick={() => setGroupFilter(code.group)}
              className={`px-2.5 py-1 rounded-lg text-[11px] font-bold border flex items-center gap-1.5 transition-all hover:scale-105 active:scale-95 ${groupAccent.badgeBg}`}
              title={`Filter to track: ${code.group}`}
            >
              {parsed.isTextbook ? (
                <BookMarked className={`w-3.5 h-3.5 ${groupAccent.badgeIconColor}`} />
              ) : (
                <BookOpen className={`w-3.5 h-3.5 ${groupAccent.badgeIconColor}`} />
              )}
              <span>Group: {code.group}</span>
            </button>

            {/* Notes Button */}
            {isSingleLesson && primaryLesson && notes && (
              <button
                type="button"
                onClick={() => setViewingNotesLesson({ lesson: primaryLesson, lessonLabel })}
                className="px-2.5 py-1 rounded-lg bg-sky-950/70 text-sky-400 hover:bg-sky-900/80 border border-sky-800 text-[11px] font-bold flex items-center gap-1.5 transition-colors shadow-sm"
                title="View Lesson Notes"
              >
                <FileText className="w-3.5 h-3.5" />
                <span>Notes</span>
              </button>
            )}

            {/* Textbook Page Range */}
            {parsed.pageRange && (
              <span className="px-2.5 py-1 rounded-lg text-[11px] font-semibold bg-slate-800/80 text-slate-300 border border-slate-700/80 font-mono">
                {parsed.pageRange}
              </span>
            )}
          </div>

          {/* Unified Title & Subtitle */}
          <div>
            <h3 className={`text-lg sm:text-xl font-bold text-white tracking-tight ${groupAccent.titleHover} transition-colors leading-snug`}>
              {parsed.primaryTitle}
            </h3>
            {parsed.subtitle && (
              <p className="text-xs sm:text-sm text-slate-400 mt-1 leading-relaxed font-normal">
                {parsed.subtitle}
              </p>
            )}
          </div>

          {/* If Unit has multiple lessons, list them neatly */}
          {!isSingleLesson && (
            <div className="mt-4 pt-3 border-t border-slate-700/80 space-y-2.5">
              <span className="text-[11px] font-bold uppercase tracking-wider text-slate-400">
                Lessons ({unit.lessons.length})
              </span>
              <div className="space-y-2">
                {unit.lessons.map((lesson, idx) => {
                  const lessonStatus = getEffectiveLessonStatus(lesson);
                  const lessonNotes = getEffectiveLessonNotes(lesson);
                  return (
                    <div 
                      key={lesson.lesson_id}
                      className="p-3.5 rounded-xl bg-slate-950/70 border border-slate-700/80 hover:border-slate-600 flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 transition-colors shadow-sm"
                    >
                      <div className="min-w-0">
                        <div className="flex items-center gap-2">
                          <span className="text-xs font-semibold text-slate-400">#{idx + 1}</span>
                          <span className="text-sm font-semibold text-white truncate">{lesson.title}</span>
                          <span className="text-[11px] text-slate-400 px-1.5 py-0.2 rounded bg-slate-800">
                            {lesson.entries.length} cards
                          </span>
                        </div>
                        {lesson.description && (
                          <p className="text-xs text-slate-400 truncate mt-0.5">{lesson.description}</p>
                        )}
                      </div>

                      <div className="flex items-center gap-2 self-end sm:self-auto shrink-0">
                        <select
                          value={lessonStatus === 'in_progress' ? 'in_progress_1' : lessonStatus}
                          onChange={(e) => handleQuickLessonStatusChange(unit.id, lesson.lesson_id, e.target.value as LessonStatus)}
                          className={`text-[10px] font-bold px-2 py-1 rounded-md border cursor-pointer ${getLessonStatusClasses(lessonStatus)}`}
                        >
                          <option value="not_started">⚪ Not Started ⚪</option>
                          <option value="in_progress_1">🟡 In Progress 1 🟡</option>
                          <option value="in_progress_2">🟡 In Progress 2 🟡</option>
                          <option value="in_progress_3">🟠 In Progress 3 🟠</option>
                          <option value="in_progress_4">🟠 In Progress 4 🟠</option>
                          <option value="in_progress_5">🟠 In Progress 5 🟠</option>
                          <option value="learned">🟢 Learned 🟢</option>
                        </select>

                        {lessonNotes && (
                          <button
                            type="button"
                            onClick={() => setViewingNotesLesson({ lesson, lessonLabel: `${lessonLabel} #${idx + 1}` })}
                            className="p-1.5 rounded-lg bg-sky-950/80 text-sky-400 hover:bg-sky-900 border border-sky-800 text-xs"
                            title="Notes"
                          >
                            <FileText className="w-3.5 h-3.5" />
                          </button>
                        )}

                        <button
                          onClick={() => onSelectLesson(unit.id, lesson.lesson_id)}
                          className="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white transition-colors"
                          title="Open Editor"
                        >
                          <ChevronRight className="w-3.5 h-3.5" />
                        </button>

                        <button
                          onClick={() => onStartStudy(lesson.entries, lesson.title, lessonNotes, lessonLabel, undefined, unit.id, lesson.lesson_id)}
                          className="px-2.5 py-1 rounded-lg bg-sky-500 hover:bg-sky-400 text-white font-semibold text-xs flex items-center gap-1 shadow-sm"
                          title="Drill Lesson"
                        >
                          <Play className="w-3 h-3 fill-current" /> Study
                        </button>
                      </div>
                    </div>
                  );
                })}
              </div>
            </div>
          )}
        </div>

        {/* Card Footer: Progress Bar, Audio Health & Action Buttons */}
        <div className="mt-3.5 pt-2.5 border-t border-slate-700/80">
          {/* Progress Indicators */}
          <div className="space-y-1.5 mb-2.5">
            <div className="flex items-center justify-between text-xs">
              <div className="flex items-center gap-2">
                <span className="font-semibold text-emerald-400">
                  {unitLearnedCount} / {unitCards.length} learned
                </span>
                <span className="text-slate-600">•</span>
                <span className="text-slate-400">{unitLearnedPct}%</span>
              </div>
              <div className="flex items-center gap-1.5 text-slate-400">
                <Volume2 className="w-3.5 h-3.5 text-teal-400" />
                <span className="font-medium text-teal-300">
                  {unit.verified_entries || 0}/{unit.total_entries || unitCards.length} audio ({unit.coverage_percentage || 0}%)
                </span>
              </div>
            </div>

            {/* Visual progress bar */}
            <div className="w-full h-1.5 bg-slate-800/90 rounded-full overflow-hidden flex shadow-inner">
              <div 
                className="h-full bg-gradient-to-r from-emerald-500 to-teal-400 transition-all duration-500"
                style={{ width: `${unitLearnedPct}%` }}
                title={`${unitLearnedPct}% of vocabulary learned`}
              />
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex items-center justify-between gap-3">
            {primaryLesson && (
              <button
                type="button"
                onClick={() => onSelectLesson(unit.id, primaryLesson.lesson_id)}
                className="px-3.5 py-2 rounded-xl bg-slate-800/80 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700/80 font-medium text-xs transition-all flex items-center gap-1.5"
                title="Browse vocabulary entries, review pronunciation & audio"
              >
                <span>Inspect Cards</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </button>
            )}

            <button
              type="button"
              onClick={() => {
                const targetCards = unitCards;
                const titleToUse = parsed.primaryTitle;
                onStartStudy(targetCards, titleToUse, notes, lessonLabel, undefined, unit.id, primaryLesson?.lesson_id);
              }}
              disabled={unitCards.length === 0}
              className="px-4 py-2 rounded-xl bg-sky-500 hover:bg-sky-400 active:scale-95 text-white font-bold text-xs shadow-md shadow-sky-500/20 transition-all flex items-center gap-1.5 ml-auto disabled:opacity-40"
              title={`Practice all ${unitCards.length} cards in this lesson`}
            >
              <Play className="w-3.5 h-3.5 fill-current" />
              <span>Study Lesson ({unitCards.length})</span>
            </button>
          </div>
        </div>
      </div>
    );
  };

  return (
    <div className="space-y-6 max-w-6xl mx-auto pb-16">
      {/* Continue Where You Left Off - Quick Resume Hero Card */}
      {resumeUnit && !searchQuery.trim() && groupFilter === 'all' && statusFilter === 'all' && (
        <div className="relative overflow-hidden rounded-2xl p-4 sm:p-5 bg-gradient-to-r from-sky-950/70 via-slate-900 to-indigo-950/60 border border-sky-500/30 shadow-xl flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div className="flex items-start sm:items-center gap-3.5">
            <div className="w-10 h-10 sm:w-12 sm:h-12 rounded-2xl bg-sky-500/20 border border-sky-400/30 flex items-center justify-center shrink-0 text-sky-400 shadow-inner">
              <Sparkles className="w-5 h-5 sm:w-6 sm:h-6" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-[10px] sm:text-xs font-bold uppercase tracking-wider text-sky-400">
                  Continue Where You Left Off
                </span>
                <span className="text-xs text-slate-500">•</span>
                <span className="text-xs font-bold px-2 py-0.5 rounded bg-sky-500/20 text-sky-300 border border-sky-500/30">
                  {lastStudied?.lessonLabel || formatLessonLabel(resumeUnit)}
                </span>
              </div>
              <h3 className="text-base sm:text-lg font-bold text-white tracking-tight mt-0.5">
                {lastStudied?.title || resumeUnit.title}
              </h3>
              <p className="text-xs text-slate-400 mt-0.5">
                {resumeUnitCards.length} cards • {resumeUnitLearnedCount} learned ({resumeUnitLearnedPct}%)
              </p>
            </div>
          </div>
          <div className="flex items-center gap-2.5 sm:self-center">
            <button
              type="button"
              onClick={() => onSelectLesson(resumeUnit.id, resumeLesson?.lesson_id || resumeUnit.lessons[0]?.lesson_id || '')}
              className="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700 text-xs font-semibold transition-all"
            >
              Inspect
            </button>
            <button
              type="button"
              onClick={() => {
                const primary = resumeLesson || resumeUnit.lessons[0];
                const notes = primary ? getEffectiveLessonNotes(primary) : '';
                onStartStudy(
                  resumeUnitCards, 
                  lastStudied?.title || resumeUnit.title, 
                  notes, 
                  lastStudied?.lessonLabel || formatLessonLabel(resumeUnit), 
                  undefined, 
                  resumeUnit.id, 
                  primary?.lesson_id
                );
              }}
              className="px-4 py-2 rounded-xl bg-sky-500 hover:bg-sky-400 active:scale-95 text-white font-bold text-xs shadow-md shadow-sky-500/25 transition-all flex items-center gap-1.5"
            >
              <Play className="w-3.5 h-3.5 fill-current" />
              <span>Resume Study</span>
              <ArrowRight className="w-3.5 h-3.5" />
            </button>
          </div>
        </div>
      )}

      {/* Learning Time & Momentum Tracker Widget */}
      <LearningTimeWidget
        onStartStudy={() => {
          if (resumeUnit) {
            const primary = resumeLesson || resumeUnit.lessons[0];
            const notes = primary ? getEffectiveLessonNotes(primary) : '';
            onStartStudy(
              resumeUnitCards, 
              lastStudied?.title || resumeUnit.title, 
              notes, 
              lastStudied?.lessonLabel || formatLessonLabel(resumeUnit), 
              undefined, 
              resumeUnit.id, 
              primary?.lesson_id
            );
          } else if (units.length > 0) {
            const firstCards = units[0].lessons.flatMap((l) => l.entries);
            onStartStudy(firstCards, units[0].title, undefined, undefined, undefined, units[0].id);
          }
        }}
      />

      {/* Curriculum Tracks & Groups Showcase */}
      <div className="space-y-3.5">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-2">
          <div>
            <div className="flex items-center gap-2">
              <h2 className="text-base sm:text-lg font-bold text-white tracking-tight flex items-center gap-2">
                <Layers className="w-4 h-4 sm:w-5 sm:h-5 text-sky-400" />
                <span>Curriculum Tracks & Groups</span>
              </h2>
              <span className="text-[11px] font-semibold text-slate-300 bg-slate-800/90 px-2.5 py-0.5 rounded-full border border-slate-700/80 shadow-sm">
                {availableGroups.length} Tracks • {units.length} Lessons • {totalCardsCount} Cards • {totalMasteryPct}% Mastered
              </span>
            </div>
            <p className="text-xs text-slate-400 mt-0.5">
              Explore and practice by curriculum track, textbook level, or official exam syllabus.
            </p>
          </div>

          {/* Quick Action when a group filter is active */}
          {groupFilter !== 'all' && (
            <button
              type="button"
              onClick={() => setGroupFilter('all')}
              className="self-start sm:self-auto text-xs font-semibold px-3 py-1.5 rounded-xl bg-sky-500/20 text-sky-300 hover:bg-sky-500/30 border border-sky-500/40 flex items-center gap-1.5 transition-colors shadow-sm"
            >
              <Layers className="w-3.5 h-3.5" />
              <span>Show All Tracks</span>
            </button>
          )}
        </div>

        {/* Grid of Aesthetic Track Cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-4 gap-3.5">
          {availableGroups.map((group) => {
            const isSelected = groupFilter.toLowerCase() === group.id.toLowerCase();
            const meta = getGroupMetadata(group.id);
            return (
              <div
                key={group.id}
                onClick={() => setGroupFilter(isSelected ? 'all' : group.id)}
                className={`relative overflow-hidden rounded-2xl p-4 sm:p-5 border transition-all duration-300 flex flex-col justify-between cursor-pointer group bg-gradient-to-br ${meta.gradientBg} ${
                  isSelected
                    ? `${meta.accentBorderActive} scale-[1.01]`
                    : `${meta.accentBorder} hover:border-slate-500/80 hover:shadow-xl ${meta.glowEffect} hover:-translate-y-0.5`
                }`}
                title={`Click to ${isSelected ? 'show all tracks' : `focus on ${meta.name}`}`}
              >
                {/* Active Accent Glow Pill */}
                {isSelected && (
                  <div className="absolute top-0 right-0 w-28 h-28 bg-white/5 rounded-full blur-2xl pointer-events-none" />
                )}

                <div>
                  {/* Top row: Level Badge & Lessons Count */}
                  <div className="flex items-center justify-between gap-2 mb-3">
                    <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-extrabold uppercase tracking-wider border shadow-sm ${meta.badgeBg} ${meta.badgeBorder} ${meta.badgeText}`}>
                      {meta.levelBadge}
                    </span>
                    <div className="flex items-center gap-1.5">
                      {isSelected ? (
                        <span className="flex items-center gap-1 text-[10px] font-bold text-emerald-300 bg-emerald-950/80 px-2 py-0.5 rounded-full border border-emerald-500/40 shadow-sm animate-pulse">
                          <Check className="w-3 h-3 text-emerald-400" /> Active
                        </span>
                      ) : (
                        <span className="text-[11px] font-semibold text-slate-300 bg-slate-900/80 px-2 py-0.5 rounded-md border border-slate-700/60">
                          {group.lessonsCount} {group.lessonsCount === 1 ? 'lesson' : 'lessons'}
                        </span>
                      )}
                    </div>
                  </div>

                  {/* Middle: Icon & Titles */}
                  <div className="flex items-start gap-3 mb-3.5">
                    <div className={`w-10 h-10 rounded-xl bg-slate-900/90 border ${isSelected ? meta.accentBorderActive : meta.accentBorder} flex items-center justify-center shrink-0 ${meta.accentText} shadow-inner`}>
                      {renderGroupIcon(group.id, "w-5 h-5")}
                    </div>
                    <div className="min-w-0">
                      <h3 className="text-base font-bold text-white tracking-tight group-hover:text-sky-300 transition-colors leading-snug truncate">
                        {meta.greekTitle}
                      </h3>
                      <p className="text-[11px] text-slate-400 mt-0.5 leading-snug line-clamp-1">
                        {meta.subtitle}
                      </p>
                    </div>
                  </div>

                  {/* Progress & Audio Metrics */}
                  <div className="space-y-1.5 pt-2 border-t border-slate-800/80 mb-3.5">
                    <div className="flex items-center justify-between text-[11px]">
                      <span className="text-slate-400 font-medium">Mastery</span>
                      <span className="font-bold text-slate-200">
                        {group.masteryPercentage}% <span className="text-slate-500 font-normal">({group.learnedCardsCount}/{group.cardsCount})</span>
                      </span>
                    </div>
                    <div className="w-full h-1.5 bg-slate-950/90 rounded-full overflow-hidden shadow-inner">
                      <div
                        className={`h-full bg-gradient-to-r ${meta.progressGradient} transition-all duration-500`}
                        style={{ width: `${group.masteryPercentage}%` }}
                      />
                    </div>
                    <div className="flex items-center justify-between text-[10px] text-slate-400 pt-0.5">
                      <span className="flex items-center gap-1 text-teal-400/90 font-medium">
                        <Volume2 className="w-3 h-3 text-teal-400" />
                        <span>{group.audioPercentage}% Audio</span>
                      </span>
                      <span className="text-slate-500">
                        {group.cardsCount} cards total
                      </span>
                    </div>
                  </div>
                </div>

                {/* Bottom Action Row */}
                <div className="flex items-center gap-2 pt-2 border-t border-slate-800/80">
                  <button
                    type="button"
                    onClick={(e) => {
                      e.stopPropagation();
                      setGroupFilter(isSelected ? 'all' : group.id);
                    }}
                    className={`flex-1 py-1.5 px-2.5 rounded-xl text-xs font-bold transition-all text-center flex items-center justify-center gap-1 border ${
                      isSelected
                        ? 'bg-slate-800/90 text-white border-slate-600 hover:bg-slate-700'
                        : 'bg-slate-900/90 text-slate-300 border-slate-700/80 hover:bg-slate-800 hover:text-white'
                    }`}
                  >
                    <span>{isSelected ? 'View All' : 'Explore Track'}</span>
                    <ChevronRight className="w-3.5 h-3.5" />
                  </button>
                  <button
                    type="button"
                    onClick={(e) => {
                      e.stopPropagation();
                      onStartStudy(group.allCards, meta.name, undefined, meta.shortLabel, undefined);
                    }}
                    disabled={group.cardsCount === 0}
                    className={`p-1.5 sm:px-2.5 sm:py-1.5 rounded-xl text-xs font-bold transition-all flex items-center gap-1 shadow-sm disabled:opacity-40 text-white ${
                      isSelected
                        ? 'bg-emerald-500 hover:bg-emerald-400 shadow-emerald-500/20'
                        : 'bg-sky-500 hover:bg-sky-400 shadow-sky-500/20'
                    }`}
                    title={`Study all ${group.cardsCount} cards in ${meta.name}`}
                  >
                    <Play className="w-3.5 h-3.5 fill-current" />
                    <span className="hidden sm:inline">Study ({group.cardsCount})</span>
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Filter Navigation Bar: Group Selection, Search/Streak, & Status Filtering */}
      <div className="glass-panel bg-slate-900/80 p-3.5 sm:p-4 rounded-2xl flex flex-col gap-3.5 border border-slate-700/80">
        {/* Top Controls Row: Group Filters + Streak & Search */}
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-3">
          {/* Group Filter (Dynamic Groups) */}
          <div className="flex flex-wrap items-center gap-1.5 bg-slate-900/90 p-1 rounded-xl border border-slate-800 shrink-0">
            <button
              type="button"
              onClick={() => setGroupFilter('all')}
              className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 ${
                groupFilter === 'all'
                  ? 'bg-sky-500 text-white shadow-sm shadow-sky-500/30'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              <Layers className="w-3.5 h-3.5" />
              <span>All Tracks ({units.length})</span>
            </button>
            {availableGroups.map((group) => {
              const isSelected = groupFilter.toLowerCase() === group.id.toLowerCase();
              const meta = getGroupMetadata(group.id);
              return (
                <button
                  key={group.id}
                  type="button"
                  onClick={() => setGroupFilter(group.id)}
                  className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all flex items-center gap-1.5 ${
                    isSelected
                      ? `bg-slate-800 text-white border ${meta.accentBorder} shadow-sm ring-1 ring-white/10`
                      : 'text-slate-400 hover:text-white'
                  }`}
                >
                  <span className={`w-2 h-2 rounded-full ${meta.dotColor}`} />
                  <span>{meta.shortLabel}</span>
                  <span className="text-[10px] text-slate-500 font-normal">({group.lessonsCount})</span>
                </button>
              );
            })}
          </div>

          {/* Streak & Search Input */}
          <div className="flex items-center gap-2.5 w-full md:w-auto">
            {/* Daily Streak & Goal Card */}
            <div className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-xs shrink-0">
              <div className="flex items-center gap-1 font-bold text-amber-400" title={`${dailyData.streak} day streak`}>
                <Flame className="w-4 h-4 fill-amber-500 text-amber-500" />
                <span>{dailyData.streak}d</span>
              </div>
              <span className="text-slate-600">|</span>
              <div className="flex items-center gap-1.5" title={`Daily review goal: ${dailyData.count}/${dailyGoal} cards`}>
                <Target className={`w-3.5 h-3.5 ${isGoalReached ? 'text-emerald-400' : 'text-sky-400'}`} />
                <span className={`font-semibold ${isGoalReached ? 'text-emerald-300' : 'text-slate-300'}`}>
                  {dailyData.count}/{dailyGoal}
                </span>
                <div className="w-12 h-1.5 bg-slate-800 rounded-full overflow-hidden ml-0.5 hidden sm:block">
                  <div 
                    className={`h-full transition-all duration-300 ${isGoalReached ? 'bg-emerald-400' : 'bg-sky-500'}`}
                    style={{ width: `${dailyGoalPct}%` }}
                  />
                </div>
              </div>
            </div>

            {/* Search Input */}
            <div className="relative flex-1 sm:w-60">
              <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none" />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search lessons or vocabulary..."
                className="w-full pl-9 pr-8 py-1.5 rounded-xl bg-slate-900 border border-slate-700 text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:border-sky-500 transition-colors"
              />
              {searchQuery && (
                <button
                  type="button"
                  onClick={() => setSearchQuery('')}
                  className="absolute right-2.5 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white"
                >
                  <X className="w-3.5 h-3.5" />
                </button>
              )}
            </div>
          </div>
        </div>

        {/* Status Filter with Levels 1-5 In Progress and increasing yellow/orange intensity */}
        <div className="flex flex-wrap items-center gap-1.5 pt-2.5 border-t border-slate-800/80">
          <span className="text-xs font-semibold text-slate-400 mr-1 hidden sm:inline flex items-center gap-1">
            <Filter className="w-3.5 h-3.5 text-slate-400" /> Status:
          </span>
          <button
            type="button"
            onClick={() => setStatusFilter('all')}
            className={`px-2.5 py-1 rounded-lg text-xs font-semibold transition-all ${
              statusFilter === 'all'
                ? 'bg-slate-700 text-white shadow-sm'
                : 'bg-slate-800/80 text-slate-400 hover:text-white'
            }`}
          >
            All
          </button>
          <button
            type="button"
            onClick={() => setStatusFilter('not_started')}
            className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all ${
              statusFilter === 'not_started'
                ? 'bg-slate-600 text-white shadow-sm'
                : 'bg-slate-800/80 text-slate-400 hover:text-white'
            }`}
          >
            <span>⚪ Not Started ({lessonsNotStartedCount})</span>
          </button>

          {/* Level 1: Soft Pale Yellow */}
          <button
            type="button"
            onClick={() => setStatusFilter('in_progress_1')}
            className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1 transition-all ${
              statusFilter === 'in_progress_1'
                ? 'bg-yellow-500/80 text-slate-950 font-bold shadow-sm shadow-yellow-500/25'
                : 'bg-slate-800/80 text-yellow-200/90 hover:text-yellow-200 hover:bg-yellow-950/40'
            }`}
          >
            <span>🟡 In Progress 1 🟡 ({lessonsInProgress1Count})</span>
          </button>

          {/* Level 2: Bright Sunny Yellow */}
          <button
            type="button"
            onClick={() => setStatusFilter('in_progress_2')}
            className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1 transition-all ${
              statusFilter === 'in_progress_2'
                ? 'bg-yellow-400 text-slate-950 font-bold shadow-sm shadow-yellow-400/25'
                : 'bg-slate-800/80 text-yellow-300 hover:text-yellow-200 hover:bg-yellow-950/60'
            }`}
          >
            <span>🟡 In Progress 2 🟡 ({lessonsInProgress2Count})</span>
          </button>

          {/* Level 3: Warm Golden Amber */}
          <button
            type="button"
            onClick={() => setStatusFilter('in_progress_3')}
            className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1 transition-all ${
              statusFilter === 'in_progress_3'
                ? 'bg-amber-500 text-slate-950 font-bold shadow-sm shadow-amber-500/25'
                : 'bg-slate-800/80 text-amber-300 hover:text-amber-200 hover:bg-amber-950/60'
            }`}
          >
            <span>🟠 In Progress 3 🟠 ({lessonsInProgress3Count})</span>
          </button>

          {/* Level 4: Bright Vibrant Orange */}
          <button
            type="button"
            onClick={() => setStatusFilter('in_progress_4')}
            className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1 transition-all ${
              statusFilter === 'in_progress_4'
                ? 'bg-orange-500 text-slate-950 font-bold shadow-sm shadow-orange-500/25'
                : 'bg-slate-800/80 text-orange-300 hover:text-orange-200 hover:bg-orange-950/60'
            }`}
          >
            <span>🟠 In Progress 4 🟠 ({lessonsInProgress4Count})</span>
          </button>

          {/* Level 5: Intense Flame Orange */}
          <button
            type="button"
            onClick={() => setStatusFilter('in_progress_5')}
            className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1 transition-all ${
              statusFilter === 'in_progress_5'
                ? 'bg-orange-600 text-white font-extrabold shadow-sm shadow-orange-600/30'
                : 'bg-slate-800/80 text-orange-400 hover:text-orange-300 hover:bg-orange-950/80'
            }`}
          >
            <span>🟠 In Progress 5 🟠 ({lessonsInProgress5Count})</span>
          </button>

          {/* Learned */}
          <button
            type="button"
            onClick={() => setStatusFilter('learned')}
            className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1 transition-all ${
              statusFilter === 'learned'
                ? 'bg-emerald-500 text-slate-950 font-bold shadow-sm shadow-emerald-500/25'
                : 'bg-slate-800/80 text-slate-400 hover:text-emerald-300'
            }`}
          >
            <span>🟢 Learned ({lessonsLearnedCount})</span>
          </button>
        </div>
      </div>

      {/* Focused Track Banner when group filter is active */}
      {groupFilter !== 'all' && (
        (() => {
          const activeGroupStats = availableGroups.find((g) => g.id.toLowerCase() === groupFilter.toLowerCase());
          const meta = getGroupMetadata(groupFilter);
          return (
            <div className={`relative overflow-hidden rounded-2xl p-5 sm:p-6 border bg-gradient-to-r ${meta.gradientBg} ${meta.accentBorder} shadow-xl flex flex-col md:flex-row md:items-center justify-between gap-5`}>
              <div className="flex items-start sm:items-center gap-4">
                <div className={`w-12 h-12 sm:w-14 sm:h-14 rounded-2xl bg-slate-900/90 border ${meta.accentBorder} flex items-center justify-center shrink-0 ${meta.accentText} shadow-inner`}>
                  {renderGroupIcon(groupFilter, "w-6 h-6 sm:w-7 sm:h-7")}
                </div>
                <div>
                  <div className="flex flex-wrap items-center gap-2">
                    <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-extrabold uppercase tracking-wider border ${meta.badgeBg} ${meta.badgeBorder} ${meta.badgeText}`}>
                      {meta.levelBadge}
                    </span>
                    <span className="text-xs text-slate-500">•</span>
                    <span className="text-xs font-semibold text-slate-300 bg-slate-900/80 px-2 py-0.5 rounded-md border border-slate-700/60">
                      {activeGroupStats?.lessonsCount || filteredUnits.length} Lessons ({activeGroupStats?.cardsCount || 0} Cards)
                    </span>
                    {activeGroupStats && (
                      <>
                        <span className="text-xs text-slate-500">•</span>
                        <span className="text-xs text-teal-400 font-medium flex items-center gap-1">
                          <Volume2 className="w-3.5 h-3.5 text-teal-400" />
                          <span>{activeGroupStats.audioPercentage}% Audio</span>
                        </span>
                      </>
                    )}
                  </div>
                  <h2 className="text-lg sm:text-2xl font-bold text-white tracking-tight mt-1">
                    {meta.greekTitle}
                  </h2>
                  <p className="text-xs sm:text-sm text-slate-300/90 mt-0.5 max-w-2xl">
                    {meta.description}
                  </p>
                </div>
              </div>

              <div className="flex items-center gap-2.5 shrink-0 self-start md:self-center">
                <button
                  type="button"
                  onClick={() => setGroupFilter('all')}
                  className="px-3.5 py-2 rounded-xl bg-slate-800/90 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700 text-xs font-semibold transition-all flex items-center gap-1.5"
                >
                  <ArrowRight className="w-3.5 h-3.5 rotate-180" />
                  <span>All Tracks</span>
                </button>
                {activeGroupStats && (
                  <button
                    type="button"
                    onClick={() => onStartStudy(activeGroupStats.allCards, meta.name, undefined, meta.shortLabel, undefined)}
                    disabled={activeGroupStats.cardsCount === 0}
                    className="px-4 py-2 rounded-xl bg-sky-500 hover:bg-sky-400 active:scale-95 text-white font-bold text-xs shadow-md shadow-sky-500/25 transition-all flex items-center gap-1.5 disabled:opacity-40"
                  >
                    <Play className="w-3.5 h-3.5 fill-current" />
                    <span>Study Entire Track ({activeGroupStats.cardsCount})</span>
                  </button>
                )}
              </div>
            </div>
          );
        })()
      )}

      {/* The Current List of Lessons */}
      {filteredUnits.length === 0 ? (
        <div className="glass-panel p-12 rounded-3xl text-center space-y-3 border-slate-800">
          <BookOpen className="w-10 h-10 text-slate-600 mx-auto" />
          <h3 className="text-base font-bold text-white">No matching lessons found</h3>
          <p className="text-xs text-slate-400 max-w-sm mx-auto">
            No lessons matched your active filters or search query. Try clearing filters to see all lessons.
          </p>
          <button
            type="button"
            onClick={() => {
              setGroupFilter('all');
              setStatusFilter('all');
              setSearchQuery('');
            }}
            className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-sky-400 border border-slate-700 transition-colors"
          >
            Reset Filters
          </button>
        </div>
      ) : isDefaultView ? (
        /* Structured Sections in default view grouped by Curriculum Group */
        <div className="space-y-8">
          {/* Header bar for group list with Expand / Collapse All control */}
          <div className="flex items-center justify-between pb-1 border-b border-slate-800 text-xs text-slate-400">
            <span className="font-semibold text-slate-300 flex items-center gap-1.5">
              <Layers className="w-4 h-4 text-sky-400" />
              <span>All Lessons by Curriculum Track ({units.length} total)</span>
            </span>
            <button
              type="button"
              onClick={toggleCollapseAll}
              className="text-xs text-sky-400 hover:text-sky-300 font-medium transition-colors flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-slate-900 border border-slate-800 hover:border-slate-700"
            >
              {areAllGroupsCollapsed ? (
                <>
                  <ChevronDown className="w-3.5 h-3.5" />
                  <span>Expand All Tracks</span>
                </>
              ) : (
                <>
                  <ChevronUp className="w-3.5 h-3.5" />
                  <span>Collapse All Tracks</span>
                </>
              )}
            </button>
          </div>

          {availableGroups.map((group) => {
            const groupUnits = filteredUnits.filter((u) => parseLessonCode(u.order || u.id).group.toLowerCase() === group.id.toLowerCase());
            if (groupUnits.length === 0) return null;
            const meta = getGroupMetadata(group.id);
            const isCollapsed = Boolean(collapsedGroups[group.id]);

            return (
              <div key={group.id} className="space-y-4">
                {/* Aesthetic Group Section Header Banner */}
                <div className={`relative overflow-hidden rounded-2xl p-4 sm:p-5 border bg-gradient-to-r ${meta.gradientBg} ${meta.accentBorder} shadow-lg transition-all`}>
                  <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
                    {/* Left: Icon & Title info */}
                    <div className="flex items-start sm:items-center gap-3.5">
                      <div className={`w-11 h-11 rounded-xl bg-slate-900/90 border ${meta.accentBorder} flex items-center justify-center shrink-0 ${meta.accentText} shadow-inner`}>
                        {renderGroupIcon(group.id, "w-5 h-5 sm:w-6 sm:h-6")}
                      </div>
                      <div>
                        <div className="flex flex-wrap items-center gap-2">
                          <span className={`px-2.5 py-0.5 rounded-full text-[10px] font-extrabold uppercase tracking-wider border ${meta.badgeBg} ${meta.badgeBorder} ${meta.badgeText}`}>
                            {meta.levelBadge}
                          </span>
                          <span className="text-xs text-slate-500">•</span>
                          <span className="text-xs text-slate-400 font-medium">
                            {groupUnits.length} {groupUnits.length === 1 ? 'lesson' : 'lessons'} ({group.cardsCount} cards)
                          </span>
                          <span className="text-xs text-slate-500">•</span>
                          <span className="text-xs text-teal-400/90 flex items-center gap-1">
                            <Volume2 className="w-3 h-3 text-teal-400" />
                            <span>{group.audioPercentage}% audio</span>
                          </span>
                        </div>
                        <h3 className="text-base sm:text-lg font-bold text-white tracking-tight mt-0.5">
                          {meta.greekTitle}
                        </h3>
                        <p className="text-xs text-slate-400 mt-0.5 max-w-xl">
                          {meta.subtitle}
                        </p>
                      </div>
                    </div>

                    {/* Right: Mastery progress & Action buttons */}
                    <div className="flex flex-wrap items-center gap-2.5 self-end md:self-center shrink-0">
                      {/* Mastery bar */}
                      <div className="w-32 hidden sm:block">
                        <div className="flex items-center justify-between text-[10px] mb-1">
                          <span className="text-slate-400">Mastery</span>
                          <span className="font-bold text-slate-200">{group.masteryPercentage}%</span>
                        </div>
                        <div className="w-full h-1.5 bg-slate-950/90 rounded-full overflow-hidden shadow-inner">
                          <div
                            className={`h-full bg-gradient-to-r ${meta.progressGradient} transition-all duration-500`}
                            style={{ width: `${group.masteryPercentage}%` }}
                          />
                        </div>
                      </div>

                      {/* Study Track Button */}
                      <button
                        type="button"
                        onClick={() => onStartStudy(group.allCards, meta.name, undefined, meta.shortLabel, undefined)}
                        disabled={group.cardsCount === 0}
                        className="px-3.5 py-2 rounded-xl bg-sky-500 hover:bg-sky-400 active:scale-95 text-white font-bold text-xs shadow-md shadow-sky-500/25 transition-all flex items-center gap-1.5 disabled:opacity-40"
                        title={`Study all ${group.cardsCount} cards in ${meta.name}`}
                      >
                        <Play className="w-3.5 h-3.5 fill-current" />
                        <span className="hidden sm:inline">Study Track</span>
                        <span>({group.cardsCount})</span>
                      </button>

                      {/* Focus Track Button */}
                      <button
                        type="button"
                        onClick={() => setGroupFilter(group.id)}
                        className="px-3 py-2 rounded-xl bg-slate-800/90 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700 text-xs font-semibold transition-all flex items-center gap-1"
                        title={`Focus exclusively on ${meta.name}`}
                      >
                        <span>Focus</span>
                        <ChevronRight className="w-3.5 h-3.5" />
                      </button>

                      {/* Collapse / Expand Toggle Button */}
                      <button
                        type="button"
                        onClick={() => toggleGroupCollapse(group.id)}
                        className="p-2 rounded-xl bg-slate-800/90 hover:bg-slate-700 text-slate-300 hover:text-white border border-slate-700 text-xs font-semibold transition-all"
                        title={isCollapsed ? "Expand Lessons" : "Collapse Lessons"}
                      >
                        {isCollapsed ? <ChevronDown className="w-4 h-4" /> : <ChevronUp className="w-4 h-4" />}
                      </button>
                    </div>
                  </div>
                </div>

                {/* Collapsible Lesson Cards Grid */}
                {!isCollapsed ? (
                  <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                    {groupUnits.map(renderLessonCard)}
                  </div>
                ) : (
                  <div 
                    onClick={() => toggleGroupCollapse(group.id)}
                    className="p-3.5 rounded-xl bg-slate-900/60 border border-slate-800/80 hover:border-slate-700 text-center cursor-pointer text-xs text-slate-400 hover:text-slate-300 transition-colors flex items-center justify-center gap-2"
                  >
                    <span>{groupUnits.length} lessons in {meta.greekTitle} collapsed</span>
                    <span className="text-sky-400 font-semibold">• Click to expand</span>
                  </div>
                )}
              </div>
            );
          })}
        </div>
      ) : (
        /* Filtered or Searched Grid View */
        <div className="space-y-4">
          <div className="flex items-center justify-between text-xs text-slate-400 px-1">
            <span>Showing {filteredUnits.length} matching {filteredUnits.length === 1 ? 'lesson' : 'lessons'}</span>
            {(groupFilter !== 'all' || statusFilter !== 'all' || searchQuery.trim()) && (
              <button
                type="button"
                onClick={() => {
                  setGroupFilter('all');
                  setStatusFilter('all');
                  setSearchQuery('');
                }}
                className="text-sky-400 hover:text-sky-300 font-semibold"
              >
                Clear all filters
              </button>
            )}
          </div>
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
            {filteredUnits.map(renderLessonCard)}
          </div>
        </div>
      )}

      {/* Lesson Notes Modal */}
      {viewingNotesLesson && (
        <div className="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4">
          <div className="glass-panel p-6 sm:p-7 rounded-3xl max-w-lg w-full border-slate-700/80 space-y-4 shadow-2xl">
            <div className="flex items-center justify-between pb-3 border-b border-slate-800">
              <div className="flex items-center gap-2.5">
                <FileText className="w-5 h-5 text-sky-400" />
                <div>
                  <h3 className="font-bold text-white text-base">
                    Study Notes • {viewingNotesLesson.lessonLabel}
                  </h3>
                  <p className="text-xs text-slate-400 truncate max-w-xs">
                    {viewingNotesLesson.lesson.title}
                  </p>
                </div>
              </div>
              <button
                type="button"
                onClick={() => setViewingNotesLesson(null)}
                className="text-slate-400 hover:text-white text-xs px-2.5 py-1.5 rounded-xl bg-slate-800 border border-slate-700 transition-colors"
              >
                Close
              </button>
            </div>

            <div className="p-4 rounded-2xl bg-slate-900/90 border border-slate-800 text-slate-200 text-sm whitespace-pre-line leading-relaxed max-h-96 overflow-y-auto">
              {getEffectiveLessonNotes(viewingNotesLesson.lesson) || 'No notes for this lesson.'}
            </div>

            <div className="flex justify-end gap-2 pt-2">
              <button
                type="button"
                onClick={() => {
                  const target = viewingNotesLesson;
                  setViewingNotesLesson(null);
                  onSelectLesson(target.lesson.unit_id, target.lesson.lesson_id);
                }}
                className="px-4 py-2 rounded-xl bg-sky-500 hover:bg-sky-400 text-white text-xs font-semibold flex items-center gap-1.5 transition-colors"
              >
                <span>Edit Notes in Deck Editor</span>
                <ChevronRight className="w-3.5 h-3.5" />
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

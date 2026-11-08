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
import { parseLessonCode, formatLessonLabel, getGroupTitle, extractUnitContext } from '../utils/unitNaming';
import { 
  BookOpen, 
  Play, 
  FileText,
  Search,
  Volume2,
  BookMarked,
  X,
  ChevronRight,
  Filter,
  RefreshCw,
  Flame,
  Target,
  Sparkles,
  ArrowRight
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
    unit.id.startsWith('unit-10');
  const isExpansion = Boolean(
    unit.is_expansion || 
    code.suffix !== 'A' || 
    unit.id === 'unit-105b' || 
    String(unit.order).toUpperCase().endsWith('B')
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

  // Dynamically group curriculum collections (e.g. A1 [KlikA1], A2 [KlikA2], etc.)
  const availableGroups = useMemo(() => {
    const groupMap = new Map<string, { id: string; name: string; lessonsCount: number; cardsCount: number }>();
    for (const unit of units) {
      const code = parseLessonCode(unit.order || unit.id);
      const groupId = code.group;
      const existing = groupMap.get(groupId);
      const cardCount = unit.lessons.flatMap((l) => l.entries).length;
      if (existing) {
        existing.lessonsCount += 1;
        existing.cardsCount += cardCount;
      } else {
        groupMap.set(groupId, {
          id: groupId,
          name: getGroupTitle(groupId),
          lessonsCount: 1,
          cardsCount: cardCount,
        });
      }
    }
    return Array.from(groupMap.values());
  }, [units]);

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

    return (
      <div 
        key={unit.id}
        className="glass-panel bg-slate-900/90 rounded-2xl p-5 sm:p-6 border border-slate-700 hover:border-sky-500/50 transition-all duration-300 shadow-xl shadow-black/30 hover:shadow-sky-500/10 group flex flex-col justify-between"
      >
        <div>
          {/* Card Top Metadata & Status Row */}
          <div className="flex flex-wrap items-center justify-between gap-2.5 mb-3.5">
            <div className="flex flex-wrap items-center gap-2">
              {/* Lesson Code Pill */}
              <span className="px-2.5 py-1 rounded-lg text-xs font-black tracking-wider uppercase bg-sky-500/15 text-sky-400 border border-sky-500/30 shadow-sm">
                {lessonLabel}
              </span>

              {/* Group Badge */}
              <span className={`px-2.5 py-1 rounded-lg text-[11px] font-bold border flex items-center gap-1.5 ${
                parsed.isTextbook 
                  ? 'bg-indigo-950/70 text-indigo-300 border-indigo-700/50' 
                  : 'bg-slate-800 text-slate-300 border-slate-700'
              }`}>
                {parsed.isTextbook && <BookMarked className="w-3.5 h-3.5 text-indigo-400" />}
                <span>Group: {code.group}</span>
              </span>

              {/* Textbook Page Range */}
              {parsed.pageRange && (
                <span className="px-2.5 py-1 rounded-lg text-[11px] font-semibold bg-slate-800/80 text-slate-300 border border-slate-700/80 font-mono">
                  {parsed.pageRange}
                </span>
              )}

              {/* Expansion Badge */}
              {parsed.isExpansion && (
                <span className="px-2 py-0.5 rounded-lg text-[11px] font-bold bg-purple-950/80 text-purple-300 border border-purple-600/60 shadow-sm">
                  Expansion of Lesson {parsed.expansionTarget || 'KlikA1-05-A'}
                </span>
              )}
            </div>

            {/* Quick Status Selector & Notes Button */}
            <div className="flex items-center gap-2">
              {isSingleLesson && primaryLesson && (
                <>
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

                  {notes && (
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
                </>
              )}
            </div>
          </div>

          {/* Unified Title & Subtitle */}
          <div className="mt-1">
            <h3 className="text-lg sm:text-xl font-bold text-white tracking-tight group-hover:text-sky-300 transition-colors leading-snug">
              {parsed.primaryTitle}
            </h3>
            {parsed.subtitle && (
              <p className="text-xs sm:text-sm text-slate-400 mt-1.5 leading-relaxed font-normal">
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
        <div className="mt-5 pt-4 border-t border-slate-700/80">
          {/* Progress Indicators */}
          <div className="space-y-2 mb-4">
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
            <div className="w-full h-2 bg-slate-800/90 rounded-full overflow-hidden flex shadow-inner">
              <div 
                className="h-full bg-gradient-to-r from-emerald-500 to-teal-400 transition-all duration-500"
                style={{ width: `${unitLearnedPct}%` }}
                title={`${unitLearnedPct}% of vocabulary learned`}
              />
            </div>
          </div>

          {/* Action Buttons */}
          <div className="flex items-center justify-between gap-3 pt-1">
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
      {/* Landing Page: List of Lessons Header with Search & Controls */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-xl sm:text-2xl font-bold text-white flex items-center gap-2.5">
            <BookOpen className="w-5 h-5 text-sky-400" />
            <span>Curriculum Lessons</span>
          </h1>
          <p className="text-xs sm:text-sm text-slate-400 mt-0.5">
            {units.length} lessons available • Browse curriculum groups and track mastery
          </p>
        </div>

        <div className="flex flex-wrap items-center gap-2.5">
          {/* Daily Streak & Goal Card */}
          <div className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-900 border border-slate-800 text-xs">
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
              className="w-full pl-9 pr-8 py-2 rounded-xl bg-slate-900 border border-slate-700 text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:border-sky-500 transition-colors"
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

          {/* Refresh Button */}
          <button 
            type="button"
            onClick={onRefresh}
            className="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 hover:text-white border border-slate-700 transition-colors shrink-0 flex items-center gap-1.5"
            title="Reload curriculum from filesystem"
          >
            <RefreshCw className="w-3.5 h-3.5" />
            <span className="hidden sm:inline">Refresh</span>
          </button>
        </div>
      </div>

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

      {/* Filter Navigation Bar: Group Selection & Status Filtering */}
      <div className="glass-panel bg-slate-900/80 p-3.5 sm:p-4 rounded-2xl flex flex-col lg:flex-row lg:items-center justify-between gap-4 border border-slate-700/80">
        {/* Group Filter (Dynamic Groups) */}
        <div className="flex flex-wrap items-center gap-1.5 bg-slate-900/90 p-1 rounded-xl border border-slate-800 shrink-0">
          <button
            type="button"
            onClick={() => setGroupFilter('all')}
            className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
              groupFilter === 'all'
                ? 'bg-sky-500 text-white shadow-sm shadow-sky-500/30'
                : 'text-slate-400 hover:text-white'
            }`}
          >
            All Groups ({units.length})
          </button>
          {availableGroups.map((group) => {
            const isSelected = groupFilter.toLowerCase() === group.id.toLowerCase();
            const isKlik = group.id.toLowerCase().startsWith('klik');
            return (
              <button
                key={group.id}
                type="button"
                onClick={() => setGroupFilter(group.id)}
                className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
                  isSelected
                    ? isKlik
                      ? 'bg-indigo-600 text-white shadow-sm shadow-indigo-600/30'
                      : 'bg-sky-500 text-white shadow-sm shadow-sky-500/30'
                    : 'text-slate-400 hover:text-white'
                }`}
              >
                {group.name} ({group.lessonsCount})
              </button>
            );
          })}
        </div>

        {/* Status Filter with Levels 1-5 In Progress and increasing yellow/orange intensity */}
        <div className="flex flex-wrap items-center gap-1.5">
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
          {availableGroups.map((group) => {
            const groupUnits = filteredUnits.filter((u) => parseLessonCode(u.order || u.id).group.toLowerCase() === group.id.toLowerCase());
            if (groupUnits.length === 0) return null;
            const isKlik = group.id.toLowerCase().startsWith('klik');
            return (
              <div key={group.id} className="space-y-4">
                <div className="flex items-center gap-2 pb-1.5 border-b border-slate-700/80">
                  <span className={`w-2.5 h-2.5 rounded-full ${isKlik ? 'bg-indigo-400' : 'bg-sky-400'}`} />
                  <h3 className="text-base font-bold text-white uppercase tracking-wider">
                    Group: {group.name}
                  </h3>
                  <span className="text-xs text-slate-400 font-medium ml-auto">
                    {groupUnits.length} {groupUnits.length === 1 ? 'lesson' : 'lessons'} ({group.cardsCount} cards)
                  </span>
                </div>
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                  {groupUnits.map(renderLessonCard)}
                </div>
              </div>
            );
          })}
        </div>
      ) : (
        /* Filtered or Searched Grid View */
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
          {filteredUnits.map(renderLessonCard)}
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

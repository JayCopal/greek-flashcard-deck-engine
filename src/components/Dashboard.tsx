import { useState, useEffect, useMemo } from 'react';
import { DeckData, Lesson, Unit, LessonStatus } from '../types/schema';
import { getAllSRSData, isCardDue, getCardRatingStatus } from '../utils/srs';
import { getUserLessonStatus, setUserLessonStatus, getUserLessonNotes, getActiveUser } from '../utils/userStorage';
import { 
  BookOpen, 
  Layers, 
  CheckCircle2, 
  Clock, 
  AlertCircle, 
  Play, 
  Download, 
  Sparkles, 
  Award,
  FileText,
  CheckCircle,
  CircleDot,
  Filter,
  Search,
  Volume2,
  BookMarked,
  X,
  ExternalLink,
  ChevronRight,
  Ban
} from 'lucide-react';

interface DashboardProps {
  deck: DeckData;
  onSelectLesson: (unitId: string, lessonId: string) => void;
  onStartStudy: (
    cards: Lesson['entries'],
    title: string,
    lessonNotes?: string,
    lessonNumber?: string,
    options?: { hideExcluded?: boolean; hideLearned?: boolean }
  ) => void;
  onRefresh: () => void;
}

type TrackFilter = 'all' | 'core' | 'textbook';
type StatusFilter = 'all' | 'not_started' | 'in_progress' | 'learned';

interface ParsedUnitInfo {
  primaryTitle: string;
  subtitle?: string;
  trackLabel: string;
  pageRange?: string;
  isTextbook: boolean;
  isExpansion: boolean;
  expansionTarget?: string;
}

/**
 * Intelligent parser that extracts clean Greek title, subtitle, textbook page ranges,
 * and track metadata while eliminating all duplicated titles.
 */
function parseUnitInfo(unit: Unit, primaryLesson?: Lesson): ParsedUnitInfo {
  const isTextbook = String(unit.order).toUpperCase().startsWith('10') || Number(unit.order) >= 100;
  const isExpansion = Boolean(unit.is_expansion || unit.id === 'unit-105b' || String(unit.order).toUpperCase() === '105B');
  const expansionTarget = unit.expansion_of || (isExpansion ? '105' : undefined);

  // Extract page ranges if present (e.g., "Pages 25-41" or "Σελίδες 25-41")
  const combinedText = `${unit.title} ${primaryLesson?.title || ''}`;
  const pageMatch = combinedText.match(/(?:Pages|Σελίδες)\s*([\d\s–-]+)/i);
  const pageRange = pageMatch ? pageMatch[1].trim() : undefined;

  const rawTitle = primaryLesson?.title || unit.title;

  if (isTextbook) {
    let clean = rawTitle;
    // Strip trailing or inline (Pages ...) or (Σελίδες ...)
    clean = clean.replace(/\s*\((?:Pages|Σελίδες)[^)]+\)/i, '').trim();
    // Strip "Κλικ στα Ελληνικά Α1: Σελίδες XX-YY (" or similar prefix
    clean = clean.replace(/^Κλικ στα Ελληνικά [^:]+:\s*(?:Σελίδες\s*[\d\s–-]+)?\s*\(?/i, '').replace(/\)$/, '').trim();

    return {
      primaryTitle: clean,
      subtitle: primaryLesson?.description || (isExpansion ? 'Grammar patterns, sentence syntax & accusative expressions' : undefined),
      trackLabel: 'Κλικ στα Ελληνικά Α1',
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
      trackLabel: 'Core Foundations',
      isTextbook: false,
      isExpansion: false,
    };
  }

  return {
    primaryTitle: rawTitle,
    subtitle: primaryLesson?.description,
    trackLabel: 'Core Foundations',
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
  const [isExporting, setIsExporting] = useState(false);
  const [exportMessage, setExportMessage] = useState<string | null>(null);
  const [activeUser, setActiveUser] = useState(getActiveUser());
  const [, setVersion] = useState(0);

  // Filter and search states
  const [trackFilter, setTrackFilter] = useState<TrackFilter>('all');
  const [statusFilter, setStatusFilter] = useState<StatusFilter>('all');
  const [searchQuery, setSearchQuery] = useState('');
  const [viewingNotesLesson, setViewingNotesLesson] = useState<{ lesson: Lesson; unitOrder: string | number } | null>(null);

  useEffect(() => {
    const handleUpdate = () => {
      setActiveUser(getActiveUser());
      setVersion((v) => v + 1);
    };
    window.addEventListener('greek_deck_user_change', handleUpdate);
    window.addEventListener('greek_deck_progress_change', handleUpdate);
    return () => {
      window.removeEventListener('greek_deck_user_change', handleUpdate);
      window.removeEventListener('greek_deck_progress_change', handleUpdate);
    };
  }, []);

  const { stats, manifest, units } = deck;

  // Gather all cards across all lessons
  const allCards = useMemo(() => units.flatMap((u) => u.lessons.flatMap((l) => l.entries)), [units]);

  // Compute SRS statistics for active user
  const srsMap = useMemo(() => getAllSRSData(activeUser.id), [activeUser.id]);
  const learnedCount = useMemo(() => allCards.filter((c) => srsMap[c.id]?.isLearned).length, [allCards, srsMap]);
  const excludedCount = useMemo(() => allCards.filter((c) => srsMap[c.id]?.isExcluded).length, [allCards, srsMap]);
  
  const dueCards = useMemo(() => {
    return allCards.filter((c) => {
      const srs = srsMap[c.id];
      if (!srs) return true; // new card is due
      if (srs.isLearned || srs.isExcluded) return false;
      return isCardDue(srs);
    });
  }, [allCards, srsMap]);

  // Filter cards by rating status for active user
  const againCards = useMemo(() => allCards.filter((c) => !srsMap[c.id]?.isExcluded && getCardRatingStatus(srsMap[c.id]) === 'again'), [allCards, srsMap]);
  const hardCards = useMemo(() => allCards.filter((c) => !srsMap[c.id]?.isExcluded && getCardRatingStatus(srsMap[c.id]) === 'hard'), [allCards, srsMap]);
  const goodCards = useMemo(() => allCards.filter((c) => !srsMap[c.id]?.isExcluded && getCardRatingStatus(srsMap[c.id]) === 'good'), [allCards, srsMap]);
  const easyCards = useMemo(() => allCards.filter((c) => !srsMap[c.id]?.isExcluded && getCardRatingStatus(srsMap[c.id]) === 'easy'), [allCards, srsMap]);
  const newCards = useMemo(() => allCards.filter((c) => !srsMap[c.id]?.isExcluded && getCardRatingStatus(srsMap[c.id]) === 'new'), [allCards, srsMap]);
  const learnedCards = useMemo(() => allCards.filter((c) => srsMap[c.id]?.isLearned), [allCards, srsMap]);
  const ignoredCards = useMemo(() => allCards.filter((c) => srsMap[c.id]?.isExcluded), [allCards, srsMap]);

  const getEffectiveLessonStatus = (lesson: Lesson): LessonStatus => {
    return getUserLessonStatus(lesson.unit_id, lesson.lesson_id, lesson.lesson_status, activeUser.id);
  };

  const getEffectiveLessonNotes = (lesson: Lesson): string => {
    return getUserLessonNotes(lesson.unit_id, lesson.lesson_id, lesson.lesson_notes, activeUser.id);
  };

  // Compute lesson status statistics for active user
  const allLessons = useMemo(() => units.flatMap((u) => u.lessons), [units]);
  const lessonsInProgressCount = useMemo(() => allLessons.filter((l) => getEffectiveLessonStatus(l) === 'in_progress').length, [allLessons, activeUser.id]);
  const lessonsLearnedCount = useMemo(() => allLessons.filter((l) => getEffectiveLessonStatus(l) === 'learned').length, [allLessons, activeUser.id]);
  const lessonsNotStartedCount = useMemo(() => allLessons.filter((l) => getEffectiveLessonStatus(l) === 'not_started').length, [allLessons, activeUser.id]);

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

  // Filtered units computation
  const filteredUnits = useMemo(() => {
    return units.filter((unit) => {
      const isTextbook = String(unit.order).toUpperCase().startsWith('10') || Number(unit.order) >= 100;
      
      // Track filter
      if (trackFilter === 'core' && isTextbook) return false;
      if (trackFilter === 'textbook' && !isTextbook) return false;

      // Status filter: match if any lesson in the unit matches the status
      if (statusFilter !== 'all') {
        const hasMatchingStatus = unit.lessons.some((l) => getEffectiveLessonStatus(l) === statusFilter);
        if (!hasMatchingStatus) return false;
      }

      // Search query
      if (searchQuery.trim()) {
        const q = searchQuery.toLowerCase().trim();
        const primaryLesson = unit.lessons[0];
        const parsed = parseUnitInfo(unit, primaryLesson);
        const matchTitle = unit.title.toLowerCase().includes(q) || 
          parsed.primaryTitle.toLowerCase().includes(q) || 
          (parsed.subtitle && parsed.subtitle.toLowerCase().includes(q)) ||
          String(unit.order).toLowerCase().includes(q);
        
        const matchCards = unit.lessons.some(l => 
          l.entries.some(e => e.greek.toLowerCase().includes(q) || e.english.toLowerCase().includes(q))
        );

        if (!matchTitle && !matchCards) return false;
      }

      return true;
    });
  }, [units, trackFilter, statusFilter, searchQuery, activeUser.id]);

  // Split into sections when viewing 'all' with no active search/status filter
  const isDefaultView = trackFilter === 'all' && statusFilter === 'all' && !searchQuery.trim();
  const coreUnits = useMemo(() => filteredUnits.filter((u) => !String(u.order).toUpperCase().startsWith('10') && Number(u.order) < 100), [filteredUnits]);
  const textbookUnits = useMemo(() => filteredUnits.filter((u) => String(u.order).toUpperCase().startsWith('10') || Number(u.order) >= 100), [filteredUnits]);

  // Render a clean, unified Unit Card (no duplicated title, no nested box)
  const renderUnitCard = (unit: Unit) => {
    const isSingleLesson = unit.lessons.length === 1;
    const primaryLesson = unit.lessons[0];
    const parsed = parseUnitInfo(unit, primaryLesson);
    
    // Aggregate cards & progress
    const unitCards = unit.lessons.flatMap((l) => l.entries);
    const unitLearnedCount = unitCards.filter((c) => srsMap[c.id]?.isLearned).length;
    const unitLearnedPct = unitCards.length > 0 ? Math.round((unitLearnedCount / unitCards.length) * 100) : 0;
    const unitEffectiveStatus = primaryLesson ? getEffectiveLessonStatus(primaryLesson) : 'not_started';
    const notes = primaryLesson ? getEffectiveLessonNotes(primaryLesson) : '';

    return (
      <div 
        key={unit.id}
        className="glass-panel rounded-2xl p-5 sm:p-6 border border-slate-800/80 hover:border-sky-500/30 transition-all duration-300 shadow-xl hover:shadow-sky-500/5 group flex flex-col justify-between"
      >
        <div>
          {/* Card Top Metadata & Status Row */}
          <div className="flex flex-wrap items-center justify-between gap-2.5 mb-3.5">
            <div className="flex flex-wrap items-center gap-2">
              {/* Unit Order Pill */}
              <span className="px-2.5 py-1 rounded-lg text-xs font-black tracking-wider uppercase bg-sky-500/15 text-sky-400 border border-sky-500/30 shadow-sm">
                Unit {unit.order}
              </span>

              {/* Track / Curriculum Tag */}
              {parsed.isTextbook ? (
                <span className="px-2.5 py-1 rounded-lg text-[11px] font-bold bg-indigo-950/70 text-indigo-300 border border-indigo-700/50 flex items-center gap-1.5">
                  <BookMarked className="w-3.5 h-3.5 text-indigo-400" />
                  <span>Κλικ στα Ελληνικά Α1</span>
                  {parsed.pageRange && (
                    <span className="text-indigo-200 font-mono text-[10px] opacity-90">• {parsed.pageRange}</span>
                  )}
                </span>
              ) : (
                <span className="px-2.5 py-1 rounded-lg text-[11px] font-semibold bg-slate-800 text-slate-300 border border-slate-700">
                  Core Foundations
                </span>
              )}

              {/* Expansion Badge */}
              {parsed.isExpansion && (
                <span className="px-2 py-0.5 rounded-lg text-[11px] font-bold bg-purple-950/80 text-purple-300 border border-purple-600/60 shadow-sm">
                  Expansion • Unit {parsed.expansionTarget || '105'}
                </span>
              )}
            </div>

            {/* Quick Status Selector & Notes Button */}
            <div className="flex items-center gap-2">
              {isSingleLesson && primaryLesson && (
                <>
                  <select
                    value={unitEffectiveStatus}
                    onChange={(e) => handleQuickLessonStatusChange(unit.id, primaryLesson.lesson_id, e.target.value as LessonStatus)}
                    className={`text-[11px] font-bold px-2.5 py-1 rounded-lg border transition-all cursor-pointer focus:outline-none focus:ring-1 focus:ring-sky-500 ${
                      unitEffectiveStatus === 'learned'
                        ? 'bg-emerald-950/90 text-emerald-300 border-emerald-600/70 hover:bg-emerald-900'
                        : unitEffectiveStatus === 'in_progress'
                        ? 'bg-amber-950/90 text-amber-300 border-amber-600/70 hover:bg-amber-900'
                        : 'bg-slate-900/90 text-slate-400 border-slate-700 hover:text-slate-200'
                    }`}
                    title="Change Unit Mastery Status"
                  >
                    <option value="not_started">⚪ Not Started</option>
                    <option value="in_progress">🟡 In Progress</option>
                    <option value="learned">🟢 Learned</option>
                  </select>

                  {notes && (
                    <button
                      type="button"
                      onClick={() => setViewingNotesLesson({ lesson: primaryLesson, unitOrder: unit.order })}
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

          {/* Unified Title & Subtitle (No Duplication) */}
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

          {/* If Unit has multiple lessons, list them neatly without repeating unit box */}
          {!isSingleLesson && (
            <div className="mt-4 pt-3 border-t border-slate-800/80 space-y-2.5">
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
                      className="p-3 rounded-xl bg-slate-900/60 border border-slate-800 hover:border-slate-700 flex flex-col sm:flex-row sm:items-center justify-between gap-2.5 transition-colors"
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
                          value={lessonStatus}
                          onChange={(e) => handleQuickLessonStatusChange(unit.id, lesson.lesson_id, e.target.value as LessonStatus)}
                          className="text-[10px] font-bold px-2 py-1 rounded-md bg-slate-800 border border-slate-700 text-slate-300 cursor-pointer"
                        >
                          <option value="not_started">⚪ Not Started</option>
                          <option value="in_progress">🟡 In Progress</option>
                          <option value="learned">🟢 Learned</option>
                        </select>

                        {lessonNotes && (
                          <button
                            type="button"
                            onClick={() => setViewingNotesLesson({ lesson, unitOrder: unit.order })}
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
                          <ExternalLink className="w-3.5 h-3.5" />
                        </button>

                        <button
                          onClick={() => onStartStudy(lesson.entries, lesson.title, lessonNotes, `Unit ${unit.order}`)}
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
        <div className="mt-5 pt-4 border-t border-slate-800/80">
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

            {/* Dual visual progress bar */}
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
            {/* Direct Editor Link */}
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

            {/* Study Unit Primary Button */}
            <button
              type="button"
              onClick={() => {
                const targetCards = unitCards;
                const titleToUse = parsed.primaryTitle;
                onStartStudy(targetCards, titleToUse, notes, `Unit ${unit.order}`);
              }}
              disabled={unitCards.length === 0}
              className="px-4 py-2 rounded-xl bg-sky-500 hover:bg-sky-400 active:scale-95 text-white font-bold text-xs shadow-md shadow-sky-500/20 transition-all flex items-center gap-1.5 ml-auto disabled:opacity-40"
              title={`Practice all ${unitCards.length} cards in this unit`}
            >
              <Play className="w-3.5 h-3.5 fill-current" />
              <span>Study Unit ({unitCards.length})</span>
            </button>
          </div>
        </div>
      </div>
    );
  };

  return (
    <div className="space-y-8 max-w-6xl mx-auto pb-16">
      {/* Hero Welcome & Deck Banner */}
      <div className="relative overflow-hidden rounded-3xl p-6 sm:p-8 bg-gradient-to-r from-sky-950/70 via-slate-900 to-indigo-950/70 border border-sky-500/20 shadow-2xl">
        <div className="absolute top-0 right-0 -mt-12 -mr-12 w-80 h-80 bg-sky-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div className="space-y-2">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sky-500/15 border border-sky-500/30 text-sky-300 text-xs font-semibold">
              <Sparkles className="w-3.5 h-3.5 text-sky-400" />
              <span>Modern Greek (CEFR A1) • Chirp 3 HD & FSRS Engine</span>
            </div>
            <h1 className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
              {manifest.deck_title}
            </h1>
            <p className="text-slate-400 text-sm max-w-2xl leading-relaxed">
              Native Greek pronunciation verified with Google Cloud Chirp 3 HD. Local-first YAML source of truth with FSRS spaced repetition and full offline PWA support.
            </p>
          </div>

          {/* Quick Study Action Buttons */}
          <div className="flex flex-wrap items-center gap-3">
            {dueCards.length > 0 && (
              <button
                onClick={() => onStartStudy(dueCards, `${manifest.deck_title} • Due for Review`)}
                className="relative inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-sm shadow-lg shadow-amber-500/25 transition-all hover:scale-[1.02] active:scale-95"
              >
                <span className="w-2 h-2 rounded-full bg-slate-950 animate-ping absolute top-2 right-2" />
                <Clock className="w-4 h-4" /> Review Due ({dueCards.length})
              </button>
            )}
            <button
              onClick={() => onStartStudy(allCards, manifest.deck_title)}
              disabled={allCards.length === 0}
              className="inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-sky-500 hover:bg-sky-400 text-white font-semibold text-sm shadow-lg shadow-sky-500/25 transition-all hover:scale-[1.02] active:scale-95 disabled:opacity-50"
            >
              <Play className="w-4 h-4 fill-current" /> Study Deck ({allCards.length})
            </button>
            <button
              onClick={handleExport}
              disabled={isExporting}
              className="inline-flex items-center gap-2 px-4 py-3 rounded-xl bg-slate-800/90 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium text-sm transition-all hover:scale-[1.02] active:scale-95 disabled:opacity-50"
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
            <p className="text-[11px] text-slate-500 mt-1">{units.length} units in deck</p>
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
            <div className="flex items-center gap-1.5 mt-1">
              {excludedCount > 0 ? (
                <span className="text-[10px] text-rose-400 font-semibold px-1.5 py-0.2 rounded bg-rose-950/60 border border-rose-800/60" title={`${excludedCount} card(s) marked Don't Learn`}>
                  {excludedCount} excluded
                </span>
              ) : (
                <p className="text-[11px] text-emerald-600/90">Active learner progress</p>
              )}
            </div>
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
            <p className="text-[11px] text-teal-600/90 mt-1">Chirp 3 HD pronunciation</p>
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

      {/* Targeted Practice by Card SRS Rating & Status */}
      <div className="glass-panel p-5 rounded-2xl border-slate-800 space-y-3.5">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-1.5">
          <div className="flex items-center gap-2">
            <Sparkles className="w-4 h-4 text-sky-400" />
            <h2 className="text-xs sm:text-sm font-bold text-white tracking-wide uppercase">
              Targeted Practice • Review by Card Status
            </h2>
          </div>
          <span className="text-xs text-slate-400">
            Drill specific SRS ratings, mastered vocabulary, or ignored cards for focused practice
          </span>
        </div>

        <div className="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-7 gap-3 pt-1">
          {/* Again Button */}
          <button
            type="button"
            disabled={againCards.length === 0}
            onClick={() => onStartStudy(againCards, `${manifest.deck_title} • Again Cards`)}
            className="p-3.5 rounded-xl bg-rose-950/40 hover:bg-rose-950/80 border border-rose-500/30 text-left transition-all hover:scale-[1.02] active:scale-95 disabled:opacity-40 disabled:pointer-events-none group"
            title="Drill cards marked Again"
          >
            <div className="text-[10px] xl:text-[11px] font-bold text-rose-400 uppercase tracking-wider flex items-center justify-between gap-1">
              <span className="truncate">Again [1]</span>
              <span className="text-xs px-2 py-0.5 rounded-full bg-rose-900/60 text-rose-200 border border-rose-800/60 shrink-0">{againCards.length}</span>
            </div>
            <div className="text-xs text-slate-300 mt-1.5 font-medium group-hover:text-white truncate">
              Repeat Soon
            </div>
          </button>

          {/* Hard Button */}
          <button
            type="button"
            disabled={hardCards.length === 0}
            onClick={() => onStartStudy(hardCards, `${manifest.deck_title} • Hard Cards`)}
            className="p-3.5 rounded-xl bg-amber-950/40 hover:bg-amber-950/80 border border-amber-500/30 text-left transition-all hover:scale-[1.02] active:scale-95 disabled:opacity-40 disabled:pointer-events-none group"
            title="Drill cards marked Hard"
          >
            <div className="text-[10px] xl:text-[11px] font-bold text-amber-400 uppercase tracking-wider flex items-center justify-between gap-1">
              <span className="truncate">Hard [2]</span>
              <span className="text-xs px-2 py-0.5 rounded-full bg-amber-900/60 text-amber-200 border border-amber-800/60 shrink-0">{hardCards.length}</span>
            </div>
            <div className="text-xs text-slate-300 mt-1.5 font-medium group-hover:text-white truncate">
              Challenging
            </div>
          </button>

          {/* Good Button */}
          <button
            type="button"
            disabled={goodCards.length === 0}
            onClick={() => onStartStudy(goodCards, `${manifest.deck_title} • Good Cards`)}
            className="p-3.5 rounded-xl bg-sky-950/40 hover:bg-sky-950/80 border border-sky-500/30 text-left transition-all hover:scale-[1.02] active:scale-95 disabled:opacity-40 disabled:pointer-events-none group"
            title="Drill cards marked Good"
          >
            <div className="text-[10px] xl:text-[11px] font-bold text-sky-400 uppercase tracking-wider flex items-center justify-between gap-1">
              <span className="truncate">Good [3]</span>
              <span className="text-xs px-2 py-0.5 rounded-full bg-sky-900/60 text-sky-200 border border-sky-800/60 shrink-0">{goodCards.length}</span>
            </div>
            <div className="text-xs text-slate-300 mt-1.5 font-medium group-hover:text-white truncate">
              Remembered
            </div>
          </button>

          {/* Easy Button */}
          <button
            type="button"
            disabled={easyCards.length === 0}
            onClick={() => onStartStudy(easyCards, `${manifest.deck_title} • Easy Cards`)}
            className="p-3.5 rounded-xl bg-emerald-950/40 hover:bg-emerald-950/80 border border-emerald-500/30 text-left transition-all hover:scale-[1.02] active:scale-95 disabled:opacity-40 disabled:pointer-events-none group"
            title="Drill cards marked Easy"
          >
            <div className="text-[10px] xl:text-[11px] font-bold text-emerald-400 uppercase tracking-wider flex items-center justify-between gap-1">
              <span className="truncate">Easy [4]</span>
              <span className="text-xs px-2 py-0.5 rounded-full bg-emerald-900/60 text-emerald-200 border border-emerald-800/60 shrink-0">{easyCards.length}</span>
            </div>
            <div className="text-xs text-slate-300 mt-1.5 font-medium group-hover:text-white truncate">
              Mastered
            </div>
          </button>

          {/* New / Unrated Button */}
          <button
            type="button"
            disabled={newCards.length === 0}
            onClick={() => onStartStudy(newCards, `${manifest.deck_title} • New Cards`)}
            className="p-3.5 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-slate-700 text-left transition-all hover:scale-[1.02] active:scale-95 disabled:opacity-40 disabled:pointer-events-none group"
            title="Drill unreviewed new cards"
          >
            <div className="text-[10px] xl:text-[11px] font-bold text-slate-400 uppercase tracking-wider flex items-center justify-between gap-1">
              <span className="truncate">New</span>
              <span className="text-xs px-2 py-0.5 rounded-full bg-slate-700 text-slate-200 border border-slate-600 shrink-0">{newCards.length}</span>
            </div>
            <div className="text-xs text-slate-300 mt-1.5 font-medium group-hover:text-white truncate">
              Unreviewed
            </div>
          </button>

          {/* Already Learnt Button */}
          <button
            type="button"
            disabled={learnedCards.length === 0}
            onClick={() => onStartStudy(learnedCards, `${manifest.deck_title} • Already Learnt Cards`, undefined, undefined, { hideLearned: false, hideExcluded: false })}
            className="p-3.5 rounded-xl bg-teal-950/40 hover:bg-teal-950/80 border border-teal-500/30 text-left transition-all hover:scale-[1.02] active:scale-95 disabled:opacity-40 disabled:pointer-events-none group"
            title="Drill cards marked as already learnt"
          >
            <div className="text-[10px] xl:text-[11px] font-bold text-teal-400 uppercase tracking-wider flex items-center justify-between gap-1">
              <span className="flex items-center gap-1 min-w-0">
                <CheckCircle className="w-3.5 h-3.5 shrink-0" />
                <span className="truncate">Learnt</span>
              </span>
              <span className="text-xs px-2 py-0.5 rounded-full bg-teal-900/60 text-teal-200 border border-teal-800/60 shrink-0">{learnedCards.length}</span>
            </div>
            <div className="text-xs text-slate-300 mt-1.5 font-medium group-hover:text-white truncate">
              Already Learnt
            </div>
          </button>

          {/* Ignored Cards Button */}
          <button
            type="button"
            disabled={ignoredCards.length === 0}
            onClick={() => onStartStudy(ignoredCards, `${manifest.deck_title} • Ignored Cards`, undefined, undefined, { hideExcluded: false, hideLearned: false })}
            className="p-3.5 rounded-xl bg-slate-800/60 hover:bg-slate-800 border border-rose-500/40 text-left transition-all hover:scale-[1.02] active:scale-95 disabled:opacity-40 disabled:pointer-events-none group"
            title="Drill cards marked as ignored"
          >
            <div className="text-[10px] xl:text-[11px] font-bold text-rose-400 uppercase tracking-wider flex items-center justify-between gap-1">
              <span className="flex items-center gap-1 min-w-0">
                <Ban className="w-3.5 h-3.5 shrink-0 text-rose-400" />
                <span className="truncate">Ignore</span>
              </span>
              <span className="text-xs px-2 py-0.5 rounded-full bg-rose-950 text-rose-300 border border-rose-800/80 shrink-0">{ignoredCards.length}</span>
            </div>
            <div className="text-xs text-slate-300 mt-1.5 font-medium group-hover:text-white truncate">
              Ignored Cards
            </div>
          </button>
        </div>
      </div>

      {/* Curriculum & Units Section */}
      <div className="space-y-6">
        {/* Section Header with Search & Controls */}
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
          <div>
            <h2 className="text-xl sm:text-2xl font-bold text-white flex items-center gap-2.5">
              <BookOpen className="w-5 h-5 text-sky-400" />
              <span>Curriculum & Learning Units</span>
            </h2>
            <p className="text-xs sm:text-sm text-slate-400 mt-0.5">
              Browse foundational topics and structured textbook units
            </p>
          </div>

          <div className="flex items-center gap-2.5">
            {/* Search Input */}
            <div className="relative flex-1 sm:w-64">
              <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none" />
              <input
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search unit or words..."
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
              onClick={onRefresh}
              className="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 hover:text-white border border-slate-700 transition-colors shrink-0"
              title="Reload curriculum from filesystem"
            >
              Refresh
            </button>
          </div>
        </div>

        {/* Filter Navigation Bar: Track Selection & Status Filtering */}
        <div className="glass-panel p-3.5 sm:p-4 rounded-2xl flex flex-col lg:flex-row lg:items-center justify-between gap-4 border-slate-800">
          {/* Track Filter (All vs Core vs Textbook) */}
          <div className="flex items-center gap-1.5 bg-slate-900/90 p-1 rounded-xl border border-slate-800 shrink-0">
            <button
              type="button"
              onClick={() => setTrackFilter('all')}
              className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
                trackFilter === 'all'
                  ? 'bg-sky-500 text-white shadow-sm shadow-sky-500/30'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              All Curriculum ({units.length})
            </button>
            <button
              type="button"
              onClick={() => setTrackFilter('core')}
              className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
                trackFilter === 'core'
                  ? 'bg-sky-500 text-white shadow-sm shadow-sky-500/30'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              Core Units (1–6)
            </button>
            <button
              type="button"
              onClick={() => setTrackFilter('textbook')}
              className={`px-3 py-1.5 rounded-lg text-xs font-bold transition-all ${
                trackFilter === 'textbook'
                  ? 'bg-indigo-600 text-white shadow-sm shadow-indigo-600/30'
                  : 'text-slate-400 hover:text-white'
              }`}
            >
              Κλικ στα Ελληνικά Α1 (101+)
            </button>
          </div>

          {/* Status Filter */}
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
              onClick={() => setStatusFilter('in_progress')}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all ${
                statusFilter === 'in_progress'
                  ? 'bg-amber-500 text-slate-950 font-bold shadow-sm shadow-amber-500/25'
                  : 'bg-slate-800/80 text-slate-400 hover:text-amber-300'
              }`}
            >
              <Clock className="w-3 h-3 text-amber-400" />
              <span>In Progress ({lessonsInProgressCount})</span>
            </button>
            <button
              type="button"
              onClick={() => setStatusFilter('learned')}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all ${
                statusFilter === 'learned'
                  ? 'bg-emerald-500 text-slate-950 font-bold shadow-sm shadow-emerald-500/25'
                  : 'bg-slate-800/80 text-slate-400 hover:text-emerald-300'
              }`}
            >
              <CheckCircle className="w-3 h-3 text-emerald-400" />
              <span>Learned ({lessonsLearnedCount})</span>
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
              <CircleDot className="w-3 h-3 text-slate-400" />
              <span>Not Started ({lessonsNotStartedCount})</span>
            </button>
          </div>
        </div>

        {/* Units Presentation List */}
        {filteredUnits.length === 0 ? (
          <div className="glass-panel p-12 rounded-3xl text-center space-y-3 border-slate-800">
            <BookOpen className="w-10 h-10 text-slate-600 mx-auto" />
            <h3 className="text-base font-bold text-white">No matching units found</h3>
            <p className="text-xs text-slate-400 max-w-sm mx-auto">
              No units matched your active filters or search query. Try clearing filters to see all units.
            </p>
            <button
              type="button"
              onClick={() => {
                setTrackFilter('all');
                setStatusFilter('all');
                setSearchQuery('');
              }}
              className="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-sky-400 border border-slate-700 transition-colors"
            >
              Reset Filters
            </button>
          </div>
        ) : isDefaultView ? (
          /* Structured Sections in default view */
          <div className="space-y-8">
            {/* Section 1: Core Conversational Foundations */}
            {coreUnits.length > 0 && (
              <div className="space-y-4">
                <div className="flex items-center gap-2 pb-1 border-b border-slate-800">
                  <span className="w-2.5 h-2.5 rounded-full bg-sky-400" />
                  <h3 className="text-base font-bold text-white uppercase tracking-wider">
                    Core Conversational Foundations (Units 1–6)
                  </h3>
                  <span className="text-xs text-slate-400 font-medium ml-auto">
                    {coreUnits.length} units
                  </span>
                </div>
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                  {coreUnits.map(renderUnitCard)}
                </div>
              </div>
            )}

            {/* Section 2: Κλικ στα Ελληνικά Α1 Curriculum */}
            {textbookUnits.length > 0 && (
              <div className="space-y-4 pt-2">
                <div className="flex items-center gap-2 pb-1 border-b border-slate-800">
                  <span className="w-2.5 h-2.5 rounded-full bg-indigo-400" />
                  <h3 className="text-base font-bold text-white uppercase tracking-wider">
                    Κλικ στα Ελληνικά Α1 Curriculum (Units 101–105b)
                  </h3>
                  <span className="text-xs text-slate-400 font-medium ml-auto">
                    {textbookUnits.length} units
                  </span>
                </div>
                <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
                  {textbookUnits.map(renderUnitCard)}
                </div>
              </div>
            )}
          </div>
        ) : (
          /* Filtered or Searched Grid View */
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-4">
            {filteredUnits.map(renderUnitCard)}
          </div>
        )}
      </div>

      {/* Lesson Notes Modal */}
      {viewingNotesLesson && (
        <div className="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-4">
          <div className="glass-panel p-6 sm:p-7 rounded-3xl max-w-lg w-full border-slate-700/80 space-y-4 shadow-2xl">
            <div className="flex items-center justify-between pb-3 border-b border-slate-800">
              <div className="flex items-center gap-2.5">
                <FileText className="w-5 h-5 text-sky-400" />
                <div>
                  <h3 className="font-bold text-white text-base">
                    Study Notes • Unit {viewingNotesLesson.unitOrder}
                  </h3>
                  <p className="text-xs text-slate-400 truncate max-w-xs">
                    {viewingNotesLesson.lesson.title}
                  </p>
                </div>
              </div>
              <button
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

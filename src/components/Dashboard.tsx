import { useState } from 'react';
import { DeckData, Lesson, LessonStatus } from '../types/schema';
import { getAllSRSData, isCardDue } from '../utils/srs';
import { 
  BookOpen, 
  Layers, 
  CheckCircle2, 
  Clock, 
  AlertCircle, 
  Play, 
  Download, 
  Sparkles, 
  ChevronRight,
  Award,
  FileText,
  CheckCircle,
  CircleDot,
  Filter
} from 'lucide-react';

interface DashboardProps {
  deck: DeckData;
  onSelectLesson: (unitId: string, lessonId: string) => void;
  onStartStudy: (cards: Lesson['entries'], title: string, lessonNotes?: string) => void;
  onRefresh: () => void;
}

export const Dashboard: React.FC<DashboardProps> = ({
  deck,
  onSelectLesson,
  onStartStudy,
  onRefresh,
}) => {
  const [isExporting, setIsExporting] = useState(false);
  const [exportMessage, setExportMessage] = useState<string | null>(null);

  const { stats, manifest, units } = deck;

  // Gather all cards across all lessons
  const allCards = units.flatMap((u) => u.lessons.flatMap((l) => l.entries));

  // Compute SRS statistics
  const srsMap = getAllSRSData();
  const learnedCount = allCards.filter((c) => srsMap[c.id]?.isLearned).length;
  const dueCards = allCards.filter((c) => {
    const srs = srsMap[c.id];
    if (!srs) return true; // new card is due
    if (srs.isLearned) return false; // learned card not due unless unlearned
    return isCardDue(srs);
  });
  // Lesson status filter state
  const [lessonStatusFilter, setLessonStatusFilter] = useState<'all' | 'not_started' | 'in_progress' | 'learned'>('all');
  const [viewingNotesLesson, setViewingNotesLesson] = useState<Lesson | null>(null);

  // Compute lesson status statistics
  const allLessons = units.flatMap((u) => u.lessons);
  const lessonsInProgressCount = allLessons.filter((l) => l.lesson_status === 'in_progress').length;
  const lessonsLearnedCount = allLessons.filter((l) => l.lesson_status === 'learned').length;
  const lessonsNotStartedCount = allLessons.filter((l) => !l.lesson_status || l.lesson_status === 'not_started').length;

  const handleQuickLessonStatusChange = async (unitId: string, lessonId: string, newStatus: LessonStatus) => {
    try {
      const res = await fetch(`/api/lesson/${unitId}/${lessonId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ lesson_status: newStatus }),
      });
      if (res.ok) {
        onRefresh();
      }
    } catch (err) {
      console.error('Failed to update lesson status', err);
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

  return (
    <div className="space-y-8 max-w-6xl mx-auto pb-12">
      {/* Header Banner */}
      <div className="relative overflow-hidden rounded-3xl p-8 bg-gradient-to-r from-sky-900/60 via-slate-800 to-indigo-950/60 border border-sky-500/20 shadow-2xl">
        <div className="absolute top-0 right-0 -mt-12 -mr-12 w-64 h-64 bg-sky-500/10 rounded-full blur-3xl pointer-events-none" />
        <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div>
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sky-500/10 border border-sky-500/30 text-sky-400 text-xs font-semibold mb-3">
              <Sparkles className="w-3.5 h-3.5" /> Modern Greek Mastery • Local-First PWA
            </div>
            <h1 className="text-3xl sm:text-4xl font-extrabold text-white tracking-tight">
              {manifest.deck_title}
            </h1>
            <p className="text-slate-400 text-sm mt-1 max-w-xl">
              Local filesystem source of truth with verified Google Cloud Chirp 3 native Greek pronunciation.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-3">
            {dueCards.length > 0 && (
              <button
                onClick={() => onStartStudy(dueCards, `${manifest.deck_title} • Due for Review`)}
                className="inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-sm shadow-lg shadow-amber-500/25 transition-all hover:scale-[1.02] active:scale-95"
              >
                <Clock className="w-4 h-4" /> Review Due ({dueCards.length})
              </button>
            )}
            <button
              onClick={() => onStartStudy(allCards, manifest.deck_title)}
              disabled={allCards.length === 0}
              className="inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-sky-500 hover:bg-sky-400 text-white font-semibold text-sm shadow-lg shadow-sky-500/25 transition-all hover:scale-[1.02] active:scale-95 disabled:opacity-50"
            >
              <Play className="w-4 h-4 fill-current" /> Study All ({allCards.length})
            </button>
            <button
              onClick={handleExport}
              disabled={isExporting}
              className="inline-flex items-center gap-2 px-4 py-3 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 font-medium text-sm transition-all hover:scale-[1.02] active:scale-95 disabled:opacity-50"
            >
              <Download className="w-4 h-4" />
              {isExporting ? 'Exporting PWA...' : 'Export Mobile PWA'}
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

      {/* Global Metrics Cards */}
      <div className="grid grid-cols-2 lg:grid-cols-5 gap-4">
        {/* Total Cards */}
        <div className="glass-panel p-5 rounded-2xl flex flex-col justify-between">
          <div className="flex items-center justify-between text-slate-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Total Cards</span>
            <Layers className="w-4 h-4 text-sky-400" />
          </div>
          <div className="mt-3 flex items-baseline gap-2">
            <span className="text-3xl font-extrabold text-white">{stats.total_entries}</span>
            <span className="text-xs text-slate-400">cards</span>
          </div>
        </div>

        {/* Mastered / Learned Cards */}
        <div className="glass-panel p-5 rounded-2xl flex flex-col justify-between border-emerald-500/30">
          <div className="flex items-center justify-between text-emerald-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Learned</span>
            <Award className="w-4 h-4" />
          </div>
          <div className="mt-3 flex items-baseline gap-2">
            <span className="text-3xl font-extrabold text-emerald-400">{learnedCount}</span>
            <span className="text-xs text-emerald-500/80">({stats.total_entries > 0 ? Math.round((learnedCount / stats.total_entries) * 100) : 0}%)</span>
          </div>
        </div>

        {/* Verified Audio */}
        <div className="glass-panel p-5 rounded-2xl flex flex-col justify-between border-teal-500/20">
          <div className="flex items-center justify-between text-teal-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Verified Audio</span>
            <CheckCircle2 className="w-4 h-4" />
          </div>
          <div className="mt-3 flex items-baseline gap-2">
            <span className="text-3xl font-extrabold text-teal-400">{stats.verified_count}</span>
            <span className="text-xs text-teal-500/80">({stats.coverage_percentage}%)</span>
          </div>
        </div>

        {/* Pending TTS */}
        <div className="glass-panel p-5 rounded-2xl flex flex-col justify-between border-amber-500/20">
          <div className="flex items-center justify-between text-amber-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Pending TTS</span>
            <Clock className="w-4 h-4" />
          </div>
          <div className="mt-3 flex items-baseline gap-2">
            <span className="text-3xl font-extrabold text-amber-400">{stats.pending_count}</span>
            <span className="text-xs text-amber-500/80">awaiting audio</span>
          </div>
        </div>

        {/* Needs Review */}
        <div className="glass-panel p-5 rounded-2xl flex flex-col justify-between border-rose-500/20">
          <div className="flex items-center justify-between text-rose-400">
            <span className="text-xs font-semibold uppercase tracking-wider">Needs Review</span>
            <AlertCircle className="w-4 h-4" />
          </div>
          <div className="mt-3 flex items-baseline gap-2">
            <span className="text-3xl font-extrabold text-rose-400">{stats.needs_review_count}</span>
            <span className="text-xs text-rose-500/80">rejected / refine</span>
          </div>
        </div>
      </div>

      {/* Coverage Progress Bar */}
      <div className="glass-panel p-6 rounded-2xl">
        <div className="flex items-center justify-between mb-2">
          <span className="text-sm font-semibold text-slate-300">Total Audio Health Coverage</span>
          <span className="text-sm font-bold text-sky-400">{stats.coverage_percentage}%</span>
        </div>
        <div className="w-full h-3 bg-slate-800 rounded-full overflow-hidden flex">
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
            <span className="w-2.5 h-2.5 rounded-full bg-emerald-500" /> Verified ({stats.verified_count})
          </div>
          <div className="flex items-center gap-1.5">
            <span className="w-2.5 h-2.5 rounded-full bg-amber-500" /> Pending ({stats.pending_count})
          </div>
          <div className="flex items-center gap-1.5">
            <span className="w-2.5 h-2.5 rounded-full bg-rose-500" /> Needs Review ({stats.needs_review_count})
          </div>
        </div>
      </div>

      {/* Units & Lessons Breakdown */}
      <div className="space-y-6">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <h2 className="text-xl font-bold text-white flex items-center gap-2">
            <BookOpen className="w-5 h-5 text-sky-400" /> Curriculum & Lessons
          </h2>
          <button 
            onClick={onRefresh}
            className="text-xs text-slate-400 hover:text-sky-400 transition-colors self-start sm:self-auto"
          >
            Refresh from disk
          </button>
        </div>

        {/* Easily Visible Lesson Status Filter Bar */}
        <div className="glass-panel p-4 rounded-2xl flex flex-col md:flex-row md:items-center justify-between gap-4 border-slate-800">
          <div className="flex items-center gap-2 text-xs font-bold text-slate-300">
            <Filter className="w-4 h-4 text-sky-400" />
            <span>Filter Lessons by Status:</span>
          </div>

          <div className="flex flex-wrap items-center gap-2">
            <button
              type="button"
              onClick={() => setLessonStatusFilter('all')}
              className={`px-3 py-1.5 rounded-xl text-xs font-semibold transition-all ${
                lessonStatusFilter === 'all'
                  ? 'bg-sky-500 text-white shadow-md shadow-sky-500/25'
                  : 'bg-slate-800 text-slate-400 hover:text-white'
              }`}
            >
              All Lessons ({allLessons.length})
            </button>

            <button
              type="button"
              onClick={() => setLessonStatusFilter('in_progress')}
              className={`px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition-all ${
                lessonStatusFilter === 'in_progress'
                  ? 'bg-amber-500 text-slate-950 font-bold shadow-md shadow-amber-500/25'
                  : 'bg-slate-800 text-slate-400 hover:text-amber-300'
              }`}
            >
              <Clock className="w-3.5 h-3.5 text-amber-400" />
              <span>In Progress ({lessonsInProgressCount})</span>
            </button>

            <button
              type="button"
              onClick={() => setLessonStatusFilter('learned')}
              className={`px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition-all ${
                lessonStatusFilter === 'learned'
                  ? 'bg-emerald-500 text-slate-950 font-bold shadow-md shadow-emerald-500/25'
                  : 'bg-slate-800 text-slate-400 hover:text-emerald-300'
              }`}
            >
              <CheckCircle className="w-3.5 h-3.5 text-emerald-400" />
              <span>Learned ({lessonsLearnedCount})</span>
            </button>

            <button
              type="button"
              onClick={() => setLessonStatusFilter('not_started')}
              className={`px-3 py-1.5 rounded-xl text-xs font-semibold flex items-center gap-1.5 transition-all ${
                lessonStatusFilter === 'not_started'
                  ? 'bg-slate-600 text-white shadow-md'
                  : 'bg-slate-800 text-slate-400 hover:text-white'
              }`}
            >
              <CircleDot className="w-3.5 h-3.5 text-slate-400" />
              <span>Not Started ({lessonsNotStartedCount})</span>
            </button>
          </div>
        </div>

        {/* Units List */}
        <div className="space-y-4">
          {units.map((unit) => {
            const filteredLessons = unit.lessons.filter((lesson) => {
              if (lessonStatusFilter === 'all') return true;
              const st = lesson.lesson_status || 'not_started';
              return st === lessonStatusFilter;
            });

            if (filteredLessons.length === 0 && lessonStatusFilter !== 'all') {
              return null; // Hide unit if no lessons match filter
            }

            return (
              <div key={unit.id} className="glass-panel rounded-2xl p-6 border-slate-800 hover:border-slate-700 transition-all">
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 mb-4 pb-4 border-b border-slate-800">
                  <div>
                    <span className="text-xs font-bold text-sky-400 uppercase tracking-wider">Unit {unit.order}</span>
                    <h3 className="text-lg font-bold text-white">{unit.title}</h3>
                  </div>
                  <div className="flex items-center gap-3">
                    <span className="text-xs text-slate-400">
                      {unit.verified_entries || 0} / {unit.total_entries || 0} Verified ({unit.coverage_percentage || 0}%)
                    </span>
                    <button
                      onClick={() => onStartStudy(unit.lessons.flatMap(l => l.entries), unit.title)}
                      className="px-3 py-1.5 rounded-lg bg-sky-500/10 hover:bg-sky-500/20 text-sky-400 text-xs font-semibold transition-colors flex items-center gap-1"
                    >
                      <Play className="w-3 h-3 fill-current" /> Drill Unit
                    </button>
                  </div>
                </div>

                {/* Lessons List */}
                <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
                  {filteredLessons.map((lesson) => (
                    <div
                      key={lesson.lesson_id}
                      className="p-4 rounded-xl bg-slate-800/50 hover:bg-slate-800 border border-slate-700/50 hover:border-sky-500/30 transition-all flex flex-col justify-between group"
                    >
                      <div>
                        <div className="flex items-center justify-between gap-2 mb-1.5">
                          <h4 className="font-semibold text-white text-sm group-hover:text-sky-300 transition-colors truncate">
                            {lesson.title}
                          </h4>
                          <span className="text-xs font-bold px-2 py-0.5 rounded-md bg-slate-900/60 text-slate-300 border border-slate-700 flex-shrink-0">
                            {lesson.entries.length} cards
                          </span>
                        </div>

                        {lesson.description && (
                          <p className="text-xs text-slate-400 line-clamp-1 mb-2">
                            {lesson.description}
                          </p>
                        )}

                        {/* Interactive Status & Notes Badges */}
                        <div className="flex flex-wrap items-center gap-2 mb-2">
                          <select
                            value={lesson.lesson_status || 'not_started'}
                            onChange={(e) =>
                              handleQuickLessonStatusChange(unit.id, lesson.lesson_id, e.target.value as LessonStatus)
                            }
                            className={`text-[11px] font-semibold px-2 py-1 rounded-lg border focus:outline-none transition-all cursor-pointer ${
                              lesson.lesson_status === 'learned'
                                ? 'bg-emerald-950/80 text-emerald-300 border-emerald-700 hover:bg-emerald-900'
                                : lesson.lesson_status === 'in_progress'
                                ? 'bg-amber-950/80 text-amber-300 border-amber-700 hover:bg-amber-900'
                                : 'bg-slate-900 text-slate-400 border-slate-700 hover:text-white'
                            }`}
                            title="Change lesson status"
                          >
                            <option value="not_started">⚪ Not Started</option>
                            <option value="in_progress">🟡 In Progress</option>
                            <option value="learned">🟢 Learned</option>
                          </select>

                          {lesson.lesson_notes && (
                            <button
                              type="button"
                              onClick={() => setViewingNotesLesson(lesson)}
                              className="px-2 py-1 rounded-lg bg-sky-950/80 text-sky-400 hover:bg-sky-900 border border-sky-800 text-[11px] font-semibold flex items-center gap-1 transition-colors"
                              title="View Lesson Notes"
                            >
                              <FileText className="w-3 h-3" />
                              <span>Notes</span>
                            </button>
                          )}
                        </div>
                      </div>

                      <div className="mt-2 pt-3 border-t border-slate-700/40 flex items-center justify-between">
                        <div className="flex items-center gap-2">
                          <span className="text-xs font-medium text-emerald-400">
                            {lesson.verified_entries || 0} verified
                          </span>
                          {((lesson.total_entries || 0) - (lesson.verified_entries || 0)) > 0 && (
                            <span className="text-xs text-amber-400">
                              • {((lesson.total_entries || 0) - (lesson.verified_entries || 0))} pending
                            </span>
                          )}
                        </div>

                        <div className="flex items-center gap-2">
                          <button
                            onClick={() => onSelectLesson(unit.id, lesson.lesson_id)}
                            className="p-1.5 rounded-lg bg-slate-700/50 hover:bg-slate-700 text-slate-300 hover:text-white transition-colors"
                            title="Open Editor / Review Audio & Notes"
                          >
                            <ChevronRight className="w-4 h-4" />
                          </button>
                          <button
                            onClick={() => onStartStudy(lesson.entries, lesson.title, lesson.lesson_notes)}
                            className="p-1.5 rounded-lg bg-sky-500/20 hover:bg-sky-500/30 text-sky-400 transition-colors"
                            title="Drill this lesson"
                          >
                            <Play className="w-4 h-4 fill-current" />
                          </button>
                        </div>
                      </div>
                    </div>
                  ))}
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Lesson Notes Modal */}
      {viewingNotesLesson && (
        <div className="fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="glass-panel p-6 rounded-3xl max-w-lg w-full border-slate-700 space-y-4 shadow-2xl">
            <div className="flex items-center justify-between pb-3 border-b border-slate-800">
              <div className="flex items-center gap-2">
                <FileText className="w-5 h-5 text-sky-400" />
                <h3 className="font-bold text-white text-base">
                  {viewingNotesLesson.title} • Study Notes
                </h3>
              </div>
              <button
                onClick={() => setViewingNotesLesson(null)}
                className="text-slate-400 hover:text-white text-xs px-2 py-1 rounded-lg bg-slate-800 border border-slate-700"
              >
                Close
              </button>
            </div>

            <div className="p-4 rounded-2xl bg-slate-900 border border-slate-800 text-slate-200 text-sm whitespace-pre-line leading-relaxed max-h-96 overflow-y-auto">
              {viewingNotesLesson.lesson_notes || 'No notes for this lesson.'}
            </div>

            <div className="flex justify-end gap-2 pt-2">
              <button
                onClick={() => {
                  const lesson = viewingNotesLesson;
                  setViewingNotesLesson(null);
                  onSelectLesson(lesson.unit_id, lesson.lesson_id);
                }}
                className="px-4 py-2 rounded-xl bg-sky-500 hover:bg-sky-400 text-white text-xs font-semibold"
              >
                Open in Editor to Edit Notes
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
};

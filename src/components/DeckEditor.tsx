import { useState, useEffect, useRef, useMemo } from 'react';
import { DeckData, Lesson, CardEntry, ChirpVoice, LessonStatus, SRSRating } from '../types/schema';
import { formatLessonLabel, parseLessonCode, extractUnitContext } from '../utils/unitNaming';
import { AudioPlayer } from './AudioPlayer';
import { 
  getUserLessonStatus, 
  setUserLessonStatus, 
  getUserLessonNotes, 
  setUserLessonNotes, 
  getActiveUser 
} from '../utils/userStorage';
import { 
  getAllSRSData, 
  getCardSRS, 
  toggleCardLearned, 
  toggleCardExcluded, 
  recordSRSRating, 
  getCardRatingStatus 
} from '../utils/srs';
import { 
  Sparkles, 
  Volume2, 
  Check, 
  X, 
  Edit3, 
  Plus, 
  Loader2, 
  Save, 
  AlertTriangle,
  ArrowLeft,
  FileText,
  CheckCircle,
  CircleDot,
  Award,
  Ban,
  Search,
  LayoutGrid,
  List
} from 'lucide-react';

interface DeckEditorProps {
  deck: DeckData;
  initialUnitId?: string;
  initialLessonId?: string;
  isOfflineMode?: boolean;
  isPwa?: boolean;
  onBackToDashboard: () => void;
  onRefresh: () => void;
}

interface PreviewState {
  entryId: string;
  sessionId: string;
  audioBase64: string;
  filename: string;
}

export const DeckEditor: React.FC<DeckEditorProps> = ({
  deck,
  initialUnitId,
  initialLessonId,
  isOfflineMode,
  isPwa,
  onBackToDashboard,
  onRefresh,
}) => {
  const isPwaMode = Boolean(
    isPwa || 
    isOfflineMode || 
    (typeof window !== 'undefined' && window.matchMedia('(display-mode: standalone)').matches)
  );
  const { units } = deck;

  // Selected Unit and Lesson
  const [selectedUnitId, setSelectedUnitId] = useState<string>(
    initialUnitId || units[0]?.id || ''
  );
  const currentUnit = units.find((u) => u.id === selectedUnitId) || units[0];

  const [selectedLessonId, setSelectedLessonId] = useState<string>(
    initialLessonId || currentUnit?.lessons[0]?.lesson_id || ''
  );
  const currentLesson: Lesson | undefined = currentUnit?.lessons.find(
    (l) => l.lesson_id === selectedLessonId
  ) || currentUnit?.lessons[0];

  // Voice Catalog state
  const [voices, setVoices] = useState<ChirpVoice[]>([]);
  const [selectedVoice, setSelectedVoice] = useState<string>('el-GR-Chirp3-HD-Leda');

  // Preview / In-Memory Audio Decision State
  const [loadingTtsId, setLoadingTtsId] = useState<string | null>(null);
  const [activePreview, setActivePreview] = useState<PreviewState | null>(null);
  const [errorMessage, setErrorMessage] = useState<string | null>(null);

  // Inline editing state (entryId -> CardEntry)
  const [editingEntryId, setEditingEntryId] = useState<string | null>(null);
  const [editFormData, setEditFormData] = useState<Partial<CardEntry>>({});

  // New Card creation form
  const [isAddingCard, setIsAddingCard] = useState(false);
  const [newCardGreek, setNewCardGreek] = useState('');
  const [newCardEnglish, setNewCardEnglish] = useState('');
  const [newCardPhonetic, setNewCardPhonetic] = useState('');
  const [newCardNotes, setNewCardNotes] = useState('');
  const [newCardPos, setNewCardPos] = useState('phrase');

  // In-lesson search and compact view states
  const [searchEntryQuery, setSearchEntryQuery] = useState('');
  const [viewMode, setViewMode] = useState<'cards' | 'table'>('cards');

  const filteredEntries = useMemo(() => {
    const entries = currentLesson?.entries || [];
    if (!searchEntryQuery.trim()) return entries;
    const q = searchEntryQuery.toLowerCase().trim();
    return entries.filter((entry) => (
      entry.greek.toLowerCase().includes(q) ||
      entry.english.toLowerCase().includes(q) ||
      (entry.phonetic_hint && entry.phonetic_hint.toLowerCase().includes(q)) ||
      (entry.gender_or_pos && entry.gender_or_pos.toLowerCase().includes(q)) ||
      (entry.notes && entry.notes.toLowerCase().includes(q))
    ));
  }, [currentLesson?.entries, searchEntryQuery]);

  // Active user & SRS state
  const [activeUser, setActiveUser] = useState(getActiveUser());
  const [, setSrsVersion] = useState(0);

  useEffect(() => {
    const handleUpdate = () => {
      setActiveUser(getActiveUser());
      setSrsVersion((v) => v + 1);
    };
    window.addEventListener('greek_deck_user_change', handleUpdate);
    window.addEventListener('greek_deck_progress_change', handleUpdate);
    return () => {
      window.removeEventListener('greek_deck_user_change', handleUpdate);
      window.removeEventListener('greek_deck_progress_change', handleUpdate);
    };
  }, []);

  // Lesson status & notes state
  const [isEditingNotes, setIsEditingNotes] = useState(false);
  const [lessonNotesText, setLessonNotesText] = useState('');
  const [isSavingLesson, setIsSavingLesson] = useState(false);

  useEffect(() => {
    if (currentUnit && currentLesson) {
      const notes = getUserLessonNotes(currentUnit.id, currentLesson.lesson_id, currentLesson.lesson_notes, activeUser.id);
      setLessonNotesText(notes);
      setIsEditingNotes(false);
    }
  }, [currentUnit?.id, currentLesson?.lesson_id, currentLesson?.lesson_notes, activeUser.id]);

  // Progress container ref for auto-scrolling
  const progressRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    // When a unit/lesson is selected, scroll smoothly to the progress section
    const timer = setTimeout(() => {
      if (progressRef.current) {
        progressRef.current.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    }, 150);
    return () => clearTimeout(timer);
  }, [selectedUnitId, selectedLessonId]);

  const handleUpdateLessonStatus = async (status: LessonStatus) => {
    if (!currentLesson || !currentUnit) return;
    setUserLessonStatus(currentUnit.id, currentLesson.lesson_id, status, activeUser.id);
    try {
      const res = await fetch(`/api/lesson/${currentUnit.id}/${currentLesson.lesson_id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ lesson_status: status }),
      });
      if (!res.ok) throw new Error('Failed to update lesson status');
      onRefresh();
    } catch {
      // In offline mode or local mode, status is already safely saved in localStorage
    }
  };

  const handleSaveLessonNotes = async () => {
    if (!currentLesson || !currentUnit) return;
    setIsSavingLesson(true);
    setUserLessonNotes(currentUnit.id, currentLesson.lesson_id, lessonNotesText, activeUser.id);
    try {
      const res = await fetch(`/api/lesson/${currentUnit.id}/${currentLesson.lesson_id}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ lesson_notes: lessonNotesText }),
      });
      if (!res.ok) throw new Error('Failed to save lesson notes');
      setIsEditingNotes(false);
      onRefresh();
    } catch (err: any) {
      // In offline mode, notes are safely saved in localStorage
      setIsEditingNotes(false);
    } finally {
      setIsSavingLesson(false);
    }
  };

  const handleToggleCardLearnedInEditor = (cardId: string) => {
    toggleCardLearned(cardId, activeUser.id);
    setSrsVersion((v) => v + 1);
  };

  const handleToggleCardExcludedInEditor = (cardId: string) => {
    toggleCardExcluded(cardId, activeUser.id);
    setSrsVersion((v) => v + 1);
  };

  const handleRateCardInEditor = (cardId: string, rating: SRSRating) => {
    recordSRSRating(cardId, rating, activeUser.id);
    setSrsVersion((v) => v + 1);
  };

  // Fetch voices on load
  useEffect(() => {
    fetch('/api/voices')
      .then((res) => res.json())
      .then((data) => {
        if (data.voices) {
          setVoices(data.voices);
          if (data.default) setSelectedVoice(data.default);
        }
      })
      .catch(() => {
        // Fallback default
        setVoices([
          {
            id: 'el-GR-Chirp3-HD-Leda',
            name: 'Leda (Female - Default)',
            gender: 'FEMALE',
            description: 'Clear, natural Greek examiner voice. Excellent articulation for learners.',
            isDefault: true,
          },
          {
            id: 'el-GR-Chirp3-HD-Charon',
            name: 'Charon (Male)',
            gender: 'MALE',
            description: 'Deep, articulate, natural Greek male voice with authentic native cadence.',
            isDefault: false,
          },
        ]);
      });
  }, []);

  // Update selected lesson if unit changes
  useEffect(() => {
    if (currentUnit && (!currentLesson || currentLesson.unit_id !== currentUnit.id)) {
      if (currentUnit.lessons[0]) {
        setSelectedLessonId(currentUnit.lessons[0].lesson_id);
      }
    }
  }, [selectedUnitId, currentUnit, currentLesson]);

  const activeVoiceObj = voices.find((v) => v.id === selectedVoice);

  // TTS Synthesis Trigger (preview in-memory)
  const handleGenerateTTS = async (entry: CardEntry) => {
    setLoadingTtsId(entry.id);
    setErrorMessage(null);
    try {
      const res = await fetch('/api/tts/preview', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          text: entry.greek,
          voice: selectedVoice,
          speaking_rate: 0.9,
        }),
      });

      const data = await res.json();
      if (!res.ok) {
        throw new Error(data.detail || 'TTS generation failed');
      }

      setActivePreview({
        entryId: entry.id,
        sessionId: data.sessionId,
        audioBase64: data.audioBase64,
        filename: data.filename,
      });
    } catch (err: any) {
      setErrorMessage(err.message || 'Error communicating with Google Cloud TTS');
    } finally {
      setLoadingTtsId(null);
    }
  };

  // Accept Audio -> Commit to disk and update YAML
  const handleAcceptAudio = async () => {
    if (!activePreview || !currentLesson) return;
    try {
      const res = await fetch('/api/tts/accept', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          sessionId: activePreview.sessionId,
          entryId: activePreview.entryId,
          unitId: currentUnit.id,
          lessonId: currentLesson.lesson_id,
        }),
      });

      if (!res.ok) {
        const err = await res.json();
        throw new Error(err.detail || 'Failed to accept audio');
      }

      setActivePreview(null);
      onRefresh();
    } catch (err: any) {
      setErrorMessage(err.message || 'Failed to accept and save audio');
    }
  };

  // Reject Audio -> Tag as needs_review, discard preview, open inline editor
  const handleRejectAudio = async (entry: CardEntry) => {
    if (!currentLesson) return;
    try {
      await fetch('/api/tts/reject', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          sessionId: activePreview?.sessionId,
          entryId: entry.id,
          unitId: currentUnit.id,
          lessonId: currentLesson.lesson_id,
        }),
      });

      setActivePreview(null);
      // Immediately open inline editor to refine Greek text/tonos
      startEditing(entry);
      onRefresh();
    } catch (err: any) {
      setErrorMessage(err.message || 'Failed to reject audio');
    }
  };

  // Inline editing handlers
  const startEditing = (entry: CardEntry) => {
    setEditingEntryId(entry.id);
    setEditFormData({
      greek: entry.greek,
      phonetic_hint: entry.phonetic_hint || '',
      english: entry.english,
      notes: entry.notes || '',
      gender_or_pos: entry.gender_or_pos || 'phrase',
    });
  };

  const cancelEditing = () => {
    setEditingEntryId(null);
    setEditFormData({});
  };

  const saveEditing = async (entryId: string) => {
    if (!currentLesson) return;
    try {
      const res = await fetch(`/api/entry/${entryId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          unit_id: currentUnit.id,
          lesson_id: currentLesson.lesson_id,
          ...editFormData,
        }),
      });

      if (!res.ok) {
        const err = await res.json();
        throw new Error(err.detail || 'Failed to update entry');
      }

      setEditingEntryId(null);
      setEditFormData({});
      onRefresh();
    } catch (err: any) {
      setErrorMessage(err.message || 'Failed to save entry');
    }
  };

  // Create new card
  const handleCreateCard = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!newCardGreek.trim() || !newCardEnglish.trim() || !currentLesson) return;

    try {
      const res = await fetch('/api/entry', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          unit_id: currentUnit.id,
          lesson_id: currentLesson.lesson_id,
          greek: newCardGreek.trim(),
          english: newCardEnglish.trim(),
          phonetic_hint: newCardPhonetic.trim(),
          notes: newCardNotes.trim(),
          gender_or_pos: newCardPos,
        }),
      });

      if (!res.ok) {
        const err = await res.json();
        throw new Error(err.detail || 'Failed to add card');
      }

      setNewCardGreek('');
      setNewCardEnglish('');
      setNewCardPhonetic('');
      setNewCardNotes('');
      setIsAddingCard(false);
      onRefresh();
    } catch (err: any) {
      setErrorMessage(err.message || 'Failed to create card');
    }
  };

  return (
    <div className="space-y-6 max-w-5xl mx-auto pb-16">
      {/* Back button & Title */}
      <div className="flex items-center justify-between">
        <button
          onClick={onBackToDashboard}
          className="inline-flex items-center gap-2 text-sm text-slate-400 hover:text-white transition-colors"
        >
          <ArrowLeft className="w-4 h-4" /> Back to Dashboard
        </button>
        <span className="text-xs text-slate-500 font-mono">
          File: content/{currentUnit?.id}/{currentLesson?.lesson_id}.yaml
        </span>
      </div>

      {/* Selector Controls Bar */}
      <div className="glass-panel p-6 rounded-2xl space-y-4">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          {/* Lesson pack selector */}
          <div>
            <label className="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5">
              Select Lesson Pack
            </label>
            <select
              value={selectedUnitId}
              onChange={(e) => setSelectedUnitId(e.target.value)}
              className="w-full bg-slate-800 text-white border border-slate-700 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-sky-500 transition-colors"
            >
              {units.map((u) => {
                const code = parseLessonCode(u.order || u.id);
                return (
                  <option key={u.id} value={u.id}>
                    {formatLessonLabel(u)} [Group: {code.group}]: {u.title}
                  </option>
                );
              })}
            </select>
          </div>

          {/* Lesson selector */}
          <div>
            <label className="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5">
              Select Lesson
            </label>
            <select
              value={selectedLessonId}
              onChange={(e) => setSelectedLessonId(e.target.value)}
              className="w-full bg-slate-800 text-white border border-slate-700 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-sky-500 transition-colors"
            >
              {currentUnit?.lessons.map((l) => (
                <option key={l.lesson_id} value={l.lesson_id}>
                  {l.title} ({l.entries.length} cards)
                </option>
              ))}
            </select>
          </div>

          {/* Native Voice Selector (hidden in PWA / offline inspect mode) */}
          {!isPwaMode && (
            <div>
              <label className="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 flex items-center justify-between">
                <span>Voice</span>
                <span className="text-[10px] text-sky-400 font-medium">Native Audio</span>
              </label>
              <select
                value={selectedVoice}
                onChange={(e) => setSelectedVoice(e.target.value)}
                className="w-full bg-slate-800 text-white border border-slate-700 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-sky-500 transition-colors font-medium"
              >
                {voices.map((v) => (
                  <option key={v.id} value={v.id}>
                    {v.name}
                  </option>
                ))}
              </select>
            </div>
          )}
        </div>

        {/* Selected voice description tooltip */}
        {!isPwaMode && activeVoiceObj && (
          <div className="text-xs text-slate-400 px-3 py-2 rounded-lg bg-slate-800/60 border border-slate-700/60 flex items-center justify-between">
            <span>
              <strong className="text-sky-300">{activeVoiceObj.name}:</strong> {activeVoiceObj.description}
            </span>
            <span className="text-[10px] uppercase font-bold px-2 py-0.5 rounded bg-sky-950 text-sky-400 border border-sky-800">
              {activeVoiceObj.gender}
            </span>
          </div>
        )}
      </div>

      {errorMessage && (
        <div className="p-4 rounded-xl bg-rose-950/80 border border-rose-500/40 text-rose-200 text-sm flex items-center justify-between">
          <div className="flex items-center gap-2">
            <AlertTriangle className="w-4 h-4 text-rose-400 flex-shrink-0" />
            <span>{errorMessage}</span>
          </div>
          <button 
            onClick={() => setErrorMessage(null)}
            className="text-xs text-rose-300 hover:text-white underline ml-3"
          >
            Dismiss
          </button>
        </div>
      )}

      {/* Lesson Info, Status Toggle & Actions Card */}
      <div className="glass-panel p-6 rounded-2xl border-slate-800 space-y-4">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div>
            <div className="flex flex-wrap items-center gap-2 mb-1">
              <span className="text-[10px] uppercase font-bold text-sky-400 tracking-wider">
                {formatLessonLabel(currentUnit)} • Group: {parseLessonCode(currentUnit?.order || currentUnit?.id).group}
              </span>
              {currentUnit && (
                <span className="text-[10px] font-semibold px-2 py-0.5 rounded-lg bg-slate-800 text-slate-300 border border-slate-700">
                  Unit: {extractUnitContext(currentUnit.title)}
                </span>
              )}
              {(currentUnit?.is_expansion || currentUnit?.id === 'unit-105b' || String(currentUnit?.order).toUpperCase().endsWith('B')) && (
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-purple-500/20 text-purple-300 border border-purple-500/40">
                  Expansion • Complementary to Lesson {currentUnit?.expansion_of || 'KlikA1-05-A'}
                </span>
              )}
            </div>
            <h2 className="text-2xl font-bold text-white tracking-tight">
              {currentLesson?.title}
            </h2>
            {currentLesson?.description && (
              <p className="text-xs text-slate-400 mt-1 max-w-xl">{currentLesson.description}</p>
            )}
          </div>

          <div className="flex flex-wrap items-center gap-2 sm:self-center">
            {/* Status Toggle Buttons (5 States: Not Started, In Progress 1, 2, 3, Learned) */}
            <div className="flex flex-wrap items-center p-1 rounded-xl bg-slate-900 border border-slate-700/80 gap-1">
              {(() => {
                const currentStatus = currentUnit && currentLesson
                  ? getUserLessonStatus(currentUnit.id, currentLesson.lesson_id, currentLesson.lesson_status, activeUser.id)
                  : 'not_started';
                return (
                  <>
                    <button
                      type="button"
                      onClick={() => handleUpdateLessonStatus('not_started')}
                      className={`px-2.5 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all ${
                        currentStatus === 'not_started'
                          ? 'bg-slate-700 text-slate-200 shadow-sm'
                          : 'text-slate-400 hover:text-white'
                      }`}
                      title="Mark lesson as Not Started"
                    >
                      <CircleDot className="w-3 h-3 text-slate-400" />
                      <span>Not Started</span>
                    </button>

                    <button
                      type="button"
                      onClick={() => handleUpdateLessonStatus('in_progress_1')}
                      className={`px-2.5 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all ${
                        currentStatus === 'in_progress_1' || currentStatus === 'in_progress'
                          ? 'bg-yellow-500/20 text-yellow-200 border border-yellow-500/40 shadow-sm'
                          : 'text-slate-400 hover:text-yellow-200'
                      }`}
                      title="Mark lesson as In Progress 1"
                    >
                      <span>🟡 In Progress 1 🟡</span>
                    </button>

                    <button
                      type="button"
                      onClick={() => handleUpdateLessonStatus('in_progress_2')}
                      className={`px-2.5 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all ${
                        currentStatus === 'in_progress_2'
                          ? 'bg-yellow-500/30 text-yellow-300 border border-yellow-400/50 shadow-sm'
                          : 'text-slate-400 hover:text-yellow-300'
                      }`}
                      title="Mark lesson as In Progress 2"
                    >
                      <span>🟡 In Progress 2 🟡</span>
                    </button>

                    <button
                      type="button"
                      onClick={() => handleUpdateLessonStatus('in_progress_3')}
                      className={`px-2.5 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all ${
                        currentStatus === 'in_progress_3'
                          ? 'bg-amber-500/25 text-amber-300 border border-amber-500/50 shadow-sm'
                          : 'text-slate-400 hover:text-amber-300'
                      }`}
                      title="Mark lesson as In Progress 3"
                    >
                      <span>🟠 In Progress 3 🟠</span>
                    </button>

                    <button
                      type="button"
                      onClick={() => handleUpdateLessonStatus('in_progress_4')}
                      className={`px-2.5 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all ${
                        currentStatus === 'in_progress_4'
                          ? 'bg-orange-500/25 text-orange-300 border border-orange-500/50 shadow-sm'
                          : 'text-slate-400 hover:text-orange-300'
                      }`}
                      title="Mark lesson as In Progress 4"
                    >
                      <span>🟠 In Progress 4 🟠</span>
                    </button>

                    <button
                      type="button"
                      onClick={() => handleUpdateLessonStatus('in_progress_5')}
                      className={`px-2.5 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all ${
                        currentStatus === 'in_progress_5'
                          ? 'bg-orange-500/35 text-orange-400 border border-orange-400/60 font-bold shadow-sm'
                          : 'text-slate-400 hover:text-orange-400'
                      }`}
                      title="Mark lesson as In Progress 5"
                    >
                      <span>🟠 In Progress 5 🟠</span>
                    </button>

                    <button
                      type="button"
                      onClick={() => handleUpdateLessonStatus('learned')}
                      className={`px-2.5 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all ${
                        currentStatus === 'learned'
                          ? 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 shadow-sm'
                          : 'text-slate-400 hover:text-emerald-300'
                      }`}
                      title="Mark lesson as Learned"
                    >
                      <CheckCircle className="w-3 h-3 text-emerald-400" />
                      <span>Learned</span>
                    </button>
                  </>
                );
              })()}
            </div>

            <button
              onClick={() => setIsAddingCard(!isAddingCard)}
              className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-sky-500/20 hover:bg-sky-500/30 text-sky-300 font-semibold text-xs border border-sky-500/30 transition-all"
            >
              <Plus className="w-4 h-4" /> {isAddingCard ? 'Cancel New Card' : 'Add Card to YAML'}
            </button>
          </div>
        </div>

        {/* Lesson Notes & Grammar Guide Box */}
        <div className="pt-4 border-t border-slate-800">
          <div className="flex items-center justify-between mb-2">
            <div className="flex items-center gap-2 text-xs font-bold text-slate-300 uppercase tracking-wider">
              <FileText className="w-4 h-4 text-sky-400" />
              <span>Lesson Study Notes & Grammar Context</span>
            </div>
            {!isEditingNotes && (
              <button
                type="button"
                onClick={() => setIsEditingNotes(true)}
                className="text-xs text-sky-400 hover:text-sky-300 font-semibold flex items-center gap-1 transition-colors"
              >
                <Edit3 className="w-3.5 h-3.5" />
                <span>
                  {currentUnit && currentLesson && getUserLessonNotes(currentUnit.id, currentLesson.lesson_id, currentLesson.lesson_notes, activeUser.id)
                    ? 'Edit Notes'
                    : 'Add Notes'}
                </span>
              </button>
            )}
          </div>

          {isEditingNotes ? (
            <div className="space-y-3">
              <textarea
                value={lessonNotesText}
                onChange={(e) => setLessonNotesText(e.target.value)}
                placeholder="Add grammar notes, verb conjugations, usage tips, or cultural context for this lesson..."
                rows={4}
                className="w-full bg-slate-900 text-white border border-slate-700 rounded-xl p-3 text-sm focus:outline-none focus:border-sky-500 font-sans"
              />
              <div className="flex justify-end gap-2">
                <button
                  type="button"
                  onClick={() => {
                    const fallbackNotes = currentUnit && currentLesson
                      ? getUserLessonNotes(currentUnit.id, currentLesson.lesson_id, currentLesson.lesson_notes, activeUser.id)
                      : '';
                    setLessonNotesText(fallbackNotes);
                    setIsEditingNotes(false);
                  }}
                  className="px-3 py-1.5 rounded-lg text-xs text-slate-400 hover:text-white"
                >
                  Cancel
                </button>
                <button
                  type="button"
                  onClick={handleSaveLessonNotes}
                  disabled={isSavingLesson}
                  className="inline-flex items-center gap-1.5 px-4 py-1.5 rounded-lg bg-sky-500 hover:bg-sky-400 text-white text-xs font-semibold shadow-md shadow-sky-500/25 disabled:opacity-50"
                >
                  {isSavingLesson ? (
                    <>
                      <Loader2 className="w-3.5 h-3.5 animate-spin" /> Saving...
                    </>
                  ) : (
                    <>
                      <Save className="w-3.5 h-3.5" /> Save Lesson Notes
                    </>
                  )}
                </button>
              </div>
            </div>
          ) : (() => {
            const currentNotes = currentUnit && currentLesson
              ? getUserLessonNotes(currentUnit.id, currentLesson.lesson_id, currentLesson.lesson_notes, activeUser.id)
              : '';
            return currentNotes ? (
              <div className="p-3.5 rounded-xl bg-slate-900/70 border border-slate-800 text-slate-300 text-sm whitespace-pre-line leading-relaxed">
                {currentNotes}
              </div>
            ) : (
              <div 
                onClick={() => setIsEditingNotes(true)}
                className="p-3 rounded-xl bg-slate-900/40 border border-dashed border-slate-800 text-slate-500 text-xs italic cursor-pointer hover:border-slate-700 hover:text-slate-400 transition-colors"
              >
                No lesson notes added yet. Click here or "Add Notes" to write grammar notes, declensions, or tips for this lesson.
              </div>
            );
          })()}
        </div>
      </div>

      {/* Add New Card Form */}
      {isAddingCard && (
        <form onSubmit={handleCreateCard} className="glass-panel p-5 rounded-2xl border-sky-500/30 space-y-4">
          <h3 className="text-sm font-bold text-white flex items-center gap-2">
            <Sparkles className="w-4 h-4 text-sky-400" /> Create New Greek Entry
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-3">
            <div>
              <label className="block text-xs font-medium text-slate-400 mb-1">
                Greek Text (with tonos accents) *
              </label>
              <input
                type="text"
                required
                placeholder="π.χ. Καλημέρα"
                value={newCardGreek}
                onChange={(e) => setNewCardGreek(e.target.value)}
                className="w-full bg-slate-800 text-white border border-slate-700 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-sky-500"
              />
            </div>
            <div>
              <label className="block text-xs font-medium text-slate-400 mb-1">
                English Translation *
              </label>
              <input
                type="text"
                required
                placeholder="e.g. Good morning"
                value={newCardEnglish}
                onChange={(e) => setNewCardEnglish(e.target.value)}
                className="w-full bg-slate-800 text-white border border-slate-700 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-sky-500"
              />
            </div>
            <div>
              <label className="block text-xs font-medium text-slate-400 mb-1">
                Phonetic Hint (Optional)
              </label>
              <input
                type="text"
                placeholder="e.g. kah-lee-MEH-rah"
                value={newCardPhonetic}
                onChange={(e) => setNewCardPhonetic(e.target.value)}
                className="w-full bg-slate-800 text-white border border-slate-700 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-sky-500"
              />
            </div>
            <div>
              <label className="block text-xs font-medium text-slate-400 mb-1">
                Part of Speech / Badge
              </label>
              <select
                value={newCardPos}
                onChange={(e) => setNewCardPos(e.target.value)}
                className="w-full bg-slate-800 text-white border border-slate-700 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-sky-500"
              >
                <option value="phrase">Phrase</option>
                <option value="noun (m)">Noun (m) / Αρσενικό</option>
                <option value="noun (f)">Noun (f) / Θηλυκό</option>
                <option value="noun (n)">Noun (n) / Ουδέτερο</option>
                <option value="verb">Verb / Ρήμα</option>
                <option value="adjective">Adjective / Επίθετο</option>
              </select>
            </div>
          </div>
          <div>
            <label className="block text-xs font-medium text-slate-400 mb-1">
              Usage Notes / Grammar Context (Optional)
            </label>
            <input
              type="text"
              placeholder="e.g. Stress on last syllable, used until 2 PM."
              value={newCardNotes}
              onChange={(e) => setNewCardNotes(e.target.value)}
              className="w-full bg-slate-800 text-white border border-slate-700 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-sky-500"
            />
          </div>
          <div className="flex justify-end gap-2 pt-2">
            <button
              type="button"
              onClick={() => setIsAddingCard(false)}
              className="px-3 py-1.5 rounded-lg text-xs text-slate-400 hover:text-white"
            >
              Cancel
            </button>
            <button
              type="submit"
              className="px-4 py-2 rounded-lg bg-sky-500 hover:bg-sky-400 text-white text-xs font-semibold shadow-md shadow-sky-500/30"
            >
              Save Entry to YAML
            </button>
          </div>
        </form>
      )}

      {/* Lesson Learner Progress & Stats */}
      {(() => {
        const allSRS = getAllSRSData(activeUser.id);
        const entries = currentLesson?.entries || [];
        const learned = entries.filter((e) => allSRS[e.id]?.isLearned && !allSRS[e.id]?.isExcluded).length;
        const easy = entries.filter((e) => !allSRS[e.id]?.isExcluded && !allSRS[e.id]?.isLearned && getCardRatingStatus(allSRS[e.id]) === 'easy').length;
        const good = entries.filter((e) => !allSRS[e.id]?.isExcluded && !allSRS[e.id]?.isLearned && getCardRatingStatus(allSRS[e.id]) === 'good').length;
        const hard = entries.filter((e) => !allSRS[e.id]?.isExcluded && !allSRS[e.id]?.isLearned && getCardRatingStatus(allSRS[e.id]) === 'hard').length;
        const again = entries.filter((e) => !allSRS[e.id]?.isExcluded && !allSRS[e.id]?.isLearned && getCardRatingStatus(allSRS[e.id]) === 'again').length;
        const ignored = entries.filter((e) => allSRS[e.id]?.isExcluded && !allSRS[e.id]?.isLearned).length;

        return (
          <div ref={progressRef} className="scroll-mt-20 glass-panel p-4 rounded-2xl border-slate-800 flex flex-col md:flex-row md:items-center justify-between gap-3 text-xs">
            <div className="flex items-center gap-2">
              <Award className="w-4 h-4 text-emerald-400" />
              <span className="font-bold text-white">{activeUser.name}'s Progress in this Lesson:</span>
              <span className="font-extrabold text-teal-400">{learned} / {entries.length} Learned</span>
              {entries.length > 0 && (
                <span className="text-slate-400">({Math.round((learned / entries.length) * 100)}%)</span>
              )}
            </div>

            <div className="flex flex-wrap items-center gap-2">
              <span className="px-2 py-0.5 rounded bg-emerald-950/60 border border-emerald-800 text-emerald-300 font-semibold">{easy} Easy</span>
              <span className="px-2 py-0.5 rounded bg-sky-950/60 border border-sky-800 text-sky-300 font-semibold">{good} Good</span>
              <span className="px-2 py-0.5 rounded bg-amber-950/60 border border-amber-800 text-amber-300 font-semibold">{hard} Hard</span>
              {again > 0 && <span className="px-2 py-0.5 rounded bg-rose-950/60 border border-rose-800 text-rose-300 font-semibold">{again} Again</span>}
              {ignored > 0 && <span className="px-2 py-0.5 rounded bg-rose-950/60 border border-rose-800 text-rose-400 font-semibold">{ignored} Ignored</span>}
            </div>
          </div>
        );
      })()}

      {/* In-Lesson Filter & View Mode Toolbar */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-3 pt-2">
        {/* Quick Search */}
        <div className="relative flex-1 sm:max-w-xs">
          <Search className="w-3.5 h-3.5 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2 pointer-events-none" />
          <input
            type="text"
            value={searchEntryQuery}
            onChange={(e) => setSearchEntryQuery(e.target.value)}
            placeholder="Search this lesson (Greek, English)..."
            className="w-full pl-8 pr-7 py-1.5 rounded-xl bg-slate-900 border border-slate-700/80 text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:border-sky-500 transition-colors"
          />
          {searchEntryQuery && (
            <button
              type="button"
              onClick={() => setSearchEntryQuery('')}
              className="absolute right-2 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white"
            >
              <X className="w-3 h-3" />
            </button>
          )}
        </div>

        <div className="flex items-center gap-2.5 self-end sm:self-auto">
          <span className="text-xs text-slate-400">
            {filteredEntries.length} {filteredEntries.length === 1 ? 'card' : 'cards'}
          </span>

          {/* View Mode Toggle: Cards vs Table */}
          <div className="flex items-center bg-slate-900 p-0.5 rounded-xl border border-slate-800">
            <button
              type="button"
              onClick={() => setViewMode('cards')}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all ${
                viewMode === 'cards'
                  ? 'bg-sky-500 text-white shadow-sm'
                  : 'text-slate-400 hover:text-white'
              }`}
              title="Card View"
            >
              <LayoutGrid className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">Cards</span>
            </button>
            <button
              type="button"
              onClick={() => setViewMode('table')}
              className={`px-2.5 py-1 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all ${
                viewMode === 'table'
                  ? 'bg-sky-500 text-white shadow-sm'
                  : 'text-slate-400 hover:text-white'
              }`}
              title="Compact Table View"
            >
              <List className="w-3.5 h-3.5" />
              <span className="hidden sm:inline">Table</span>
            </button>
          </div>
        </div>
      </div>

      {filteredEntries.length === 0 ? (
        <div className="glass-panel p-8 rounded-2xl text-center space-y-2 border-slate-800">
          <p className="text-sm font-semibold text-white">No cards match your search</p>
          <p className="text-xs text-slate-400">Try adjusting your search terms or clearing the filter.</p>
          <button
            type="button"
            onClick={() => setSearchEntryQuery('')}
            className="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs text-sky-400 border border-slate-700 mt-1 transition-colors"
          >
            Clear Search
          </button>
        </div>
      ) : viewMode === 'table' ? (
        /* Compact Table / List View */
        <div className="glass-panel rounded-2xl overflow-hidden border border-slate-800 shadow-xl">
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs border-collapse">
              <thead>
                <tr className="border-b border-slate-800 bg-slate-900/90 text-slate-400 font-semibold uppercase tracking-wider text-[10px]">
                  <th className="py-2.5 px-3">Status</th>
                  <th className="py-2.5 px-3">Greek</th>
                  <th className="py-2.5 px-3">English</th>
                  <th className="py-2.5 px-3 hidden sm:table-cell">Phonetic</th>
                  <th className="py-2.5 px-3">Audio</th>
                  <th className="py-2.5 px-3">Rating</th>
                  <th className="py-2.5 px-3 text-right">Actions</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-slate-800/60">
                {filteredEntries.map((entry) => {
                  const cardSrs = getCardSRS(entry.id, activeUser.id);
                  const cardRating = getCardRatingStatus(cardSrs);
                  return (
                    <tr 
                      key={entry.id} 
                      className={`hover:bg-slate-800/40 transition-colors ${
                        cardSrs.isExcluded ? 'opacity-60 bg-rose-950/10' : ''
                      }`}
                    >
                      <td className="py-2.5 px-3 whitespace-nowrap">
                        {cardSrs.isLearned ? (
                          <span className="inline-flex items-center gap-1 px-1.5 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30">
                            <CheckCircle className="w-3 h-3 text-teal-400" />
                            <span className="hidden md:inline">Learned</span>
                          </span>
                        ) : cardSrs.isExcluded ? (
                          <span className="inline-flex items-center gap-1 px-1.5 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30">
                            <Ban className="w-3 h-3 text-rose-400" />
                            <span className="hidden md:inline">Ignored</span>
                          </span>
                        ) : (
                          <span className="inline-block w-2 h-2 rounded-full bg-slate-600 ml-1" />
                        )}
                      </td>
                      <td className="py-2.5 px-3 font-semibold text-white">
                        <div className="flex items-center gap-1.5 flex-wrap">
                          <span className="font-serif text-sm">{entry.greek}</span>
                          {entry.gender_or_pos && (
                            <span className="text-[10px] px-1.5 py-0.5 rounded bg-slate-800 text-sky-300 border border-slate-700/80">
                              {entry.gender_or_pos}
                            </span>
                          )}
                        </div>
                      </td>
                      <td className="py-2.5 px-3 text-slate-300">{entry.english}</td>
                      <td className="py-2.5 px-3 text-slate-400 font-mono text-[11px] hidden sm:table-cell">
                        {entry.phonetic_hint ? `/${entry.phonetic_hint}/` : '—'}
                      </td>
                      <td className="py-2.5 px-3 whitespace-nowrap">
                        {entry.audio ? (
                          <AudioPlayer
                            src={`${import.meta.env.BASE_URL.endsWith('/') ? import.meta.env.BASE_URL : `${import.meta.env.BASE_URL}/`}audio/${entry.audio}`}
                            mini
                          />
                        ) : (
                          <span className="text-[10px] text-slate-500 italic">No audio</span>
                        )}
                      </td>
                      <td className="py-2.5 px-3 whitespace-nowrap">
                        {cardRating !== 'new' ? (
                          <span className={`text-[10px] font-bold px-2 py-0.5 rounded-full border uppercase ${
                            cardRating === 'again'
                              ? 'bg-rose-950/80 text-rose-300 border-rose-700/60'
                              : cardRating === 'hard'
                              ? 'bg-amber-950/80 text-amber-300 border-amber-700/60'
                              : cardRating === 'good'
                              ? 'bg-sky-950/80 text-sky-300 border-sky-700/60'
                              : 'bg-emerald-950/80 text-emerald-300 border-emerald-700/60'
                          }`}>
                            {cardRating}
                          </span>
                        ) : (
                          <span className="text-slate-500 text-[10px]">New</span>
                        )}
                      </td>
                      <td className="py-2.5 px-3 text-right whitespace-nowrap">
                        <button
                          type="button"
                          onClick={() => {
                            setViewMode('cards');
                            startEditing(entry);
                          }}
                          className="p-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white border border-slate-700 inline-flex items-center"
                          title="Edit card"
                        >
                          <Edit3 className="w-3 h-3" />
                        </button>
                      </td>
                    </tr>
                  );
                })}
              </tbody>
            </table>
          </div>
        </div>
      ) : (
        /* Cards List */
        <div className="space-y-4">
          {filteredEntries.map((entry) => {
          const isPreviewing = activePreview?.entryId === entry.id;
          const isEditing = editingEntryId === entry.id;
          const isLoadingTts = loadingTtsId === entry.id;
          const cardSrs = getCardSRS(entry.id, activeUser.id);
          const cardRating = getCardRatingStatus(cardSrs);

          return (
            <div
              key={entry.id}
              className={`glass-panel rounded-2xl p-5 transition-all border ${
                isPreviewing
                  ? 'border-sky-400 shadow-xl shadow-sky-500/10 ring-1 ring-sky-400'
                  : entry.status === 'verified'
                  ? 'border-emerald-500/20'
                  : entry.status === 'needs_review'
                  ? 'border-rose-500/30'
                  : 'border-slate-800'
              }`}
            >
              {isEditing ? (
                /* Inline Editing Form */
                <div className="space-y-3">
                  <div className="flex items-center justify-between text-xs text-sky-400 font-semibold mb-2">
                    <span>Editing Entry {entry.id} (YAML)</span>
                    <span className="text-slate-400 font-normal">Remember to preserve tonos</span>
                  </div>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                    <div>
                      <label className="text-[11px] text-slate-400 block mb-1">Greek Text</label>
                      <input
                        type="text"
                        value={editFormData.greek || ''}
                        onChange={(e) => setEditFormData({ ...editFormData, greek: e.target.value })}
                        className="w-full bg-slate-800 text-white border border-slate-700 rounded-lg px-3 py-1.5 text-base font-semibold focus:outline-none focus:border-sky-500"
                      />
                    </div>
                    <div>
                      <label className="text-[11px] text-slate-400 block mb-1">English Translation</label>
                      <input
                        type="text"
                        value={editFormData.english || ''}
                        onChange={(e) => setEditFormData({ ...editFormData, english: e.target.value })}
                        className="w-full bg-slate-800 text-white border border-slate-700 rounded-lg px-3 py-1.5 text-sm focus:outline-none focus:border-sky-500"
                      />
                    </div>
                    <div>
                      <label className="text-[11px] text-slate-400 block mb-1">Phonetic Hint</label>
                      <input
                        type="text"
                        value={editFormData.phonetic_hint || ''}
                        onChange={(e) => setEditFormData({ ...editFormData, phonetic_hint: e.target.value })}
                        className="w-full bg-slate-800 text-white border border-slate-700 rounded-lg px-3 py-1.5 text-xs focus:outline-none focus:border-sky-500"
                      />
                    </div>
                    <div>
                      <label className="text-[11px] text-slate-400 block mb-1">Part of Speech</label>
                      <input
                        type="text"
                        value={editFormData.gender_or_pos || ''}
                        onChange={(e) => setEditFormData({ ...editFormData, gender_or_pos: e.target.value })}
                        className="w-full bg-slate-800 text-white border border-slate-700 rounded-lg px-3 py-1.5 text-xs focus:outline-none focus:border-sky-500"
                      />
                    </div>
                  </div>
                  <div>
                    <label className="text-[11px] text-slate-400 block mb-1">Notes</label>
                    <input
                      type="text"
                      value={editFormData.notes || ''}
                      onChange={(e) => setEditFormData({ ...editFormData, notes: e.target.value })}
                      className="w-full bg-slate-800 text-white border border-slate-700 rounded-lg px-3 py-1.5 text-xs focus:outline-none focus:border-sky-500"
                    />
                  </div>
                  <div className="flex justify-end gap-2 pt-2">
                    <button
                      type="button"
                      onClick={cancelEditing}
                      className="px-3 py-1.5 text-xs text-slate-400 hover:text-white"
                    >
                      Cancel
                    </button>
                    <button
                      type="button"
                      onClick={() => saveEditing(entry.id)}
                      className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-semibold"
                    >
                      <Save className="w-3.5 h-3.5" /> Save Changes
                    </button>
                  </div>
                </div>
              ) : (
                /* Card Display Mode */
                <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                  <div className="space-y-1.5">
                    <div className="flex items-center gap-2.5">
                      <span className="text-xl sm:text-2xl font-bold text-white tracking-wide font-serif">
                        {entry.greek}
                      </span>
                      {entry.gender_or_pos && (
                        <span className="text-[11px] font-semibold px-2 py-0.5 rounded-full bg-slate-800 text-sky-400 border border-slate-700">
                          {entry.gender_or_pos}
                        </span>
                      )}
                      {/* Status Badges */}
                      {entry.status === 'verified' && (
                        <span className="text-[11px] font-semibold px-2 py-0.5 rounded-full bg-emerald-950/80 text-emerald-400 border border-emerald-800 flex items-center gap-1">
                          <Check className="w-3 h-3" /> Verified
                        </span>
                      )}
                      {entry.status === 'pending_tts' && (
                        <span className="text-[11px] font-semibold px-2 py-0.5 rounded-full bg-amber-950/80 text-amber-400 border border-amber-800">
                          Pending TTS
                        </span>
                      )}
                      {entry.status === 'needs_review' && (
                        <span className="text-[11px] font-semibold px-2 py-0.5 rounded-full bg-rose-950/80 text-rose-400 border border-rose-800">
                          Needs Review
                        </span>
                      )}

                      {/* Learner Progress Badges */}
                      {cardSrs.isLearned && (
                        <span className="text-[11px] font-semibold px-2 py-0.5 rounded-full bg-teal-950/90 text-teal-300 border border-teal-700 flex items-center gap-1">
                          <CheckCircle className="w-3 h-3" /> Learned
                        </span>
                      )}
                      {cardRating !== 'new' ? (
                        <span className={`text-[11px] font-bold px-2 py-0.5 rounded-full border ${
                          cardRating === 'again'
                            ? 'bg-rose-950/90 text-rose-300 border-rose-700/60'
                            : cardRating === 'hard'
                            ? 'bg-amber-950/90 text-amber-300 border-amber-700/60'
                            : cardRating === 'good'
                            ? 'bg-sky-950/90 text-sky-300 border-sky-700/60'
                            : 'bg-emerald-950/90 text-emerald-300 border-emerald-700/60'
                        }`}>
                          {cardRating.toUpperCase()}
                        </span>
                      ) : (
                        <span className="text-[11px] font-medium px-2 py-0.5 rounded-full bg-slate-800 text-slate-400 border border-slate-700">
                          NEW
                        </span>
                      )}
                      {cardSrs.isExcluded && (
                        <span className="text-[11px] font-semibold px-2 py-0.5 rounded-full bg-rose-950/90 text-rose-400 border border-rose-800 flex items-center gap-1">
                          <Ban className="w-3 h-3" /> Ignored
                        </span>
                      )}
                    </div>

                    <div className="text-slate-300 text-sm font-medium">
                      {entry.english}
                      {entry.phonetic_hint && (
                        <span className="text-xs text-slate-400 ml-2 font-mono">
                          [{entry.phonetic_hint}]
                        </span>
                      )}
                    </div>

                    {entry.notes && (
                      <p className="text-xs text-slate-400 max-w-xl italic">
                        {entry.notes}
                      </p>
                    )}

                    {entry.example_el && (
                      <div className="text-xs text-sky-300 font-serif pt-0.5">
                        <span className="text-slate-400 font-sans text-[11px] mr-1">Ex:</span>
                        {entry.example_el}
                        {entry.example_en && (
                          <span className="text-slate-400 font-sans text-[11px] ml-1.5 italic">
                            ({entry.example_en})
                          </span>
                        )}
                      </div>
                    )}

                    {entry.audio && (
                      <div className="text-[10px] text-slate-500 font-mono flex items-center gap-1 pt-1">
                        <span>Audio: {entry.audio}</span>
                      </div>
                    )}
                  </div>

                  {/* Actions Column */}
                  <div className="flex flex-wrap items-center gap-2.5 sm:self-center">
                    {/* Permanent audio player if verified */}
                    {entry.audio && !isPreviewing && (
                      <AudioPlayer
                        src={`${import.meta.env.BASE_URL.endsWith('/') ? import.meta.env.BASE_URL : `${import.meta.env.BASE_URL}/`}audio/${entry.audio}`}
                        mini
                        label="Verified"
                      />
                    )}

                    {/* TTS Generation Button (Hidden in PWA / offline inspect mode) */}
                    {!isPreviewing && !isPwaMode && (
                      <button
                        onClick={() => handleGenerateTTS(entry)}
                        disabled={isLoadingTts}
                        className={`inline-flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs font-semibold transition-all ${
                          entry.status === 'verified'
                            ? 'bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700'
                            : 'bg-sky-500 hover:bg-sky-400 text-white shadow-md shadow-sky-500/20'
                        } disabled:opacity-50`}
                        title="Generate Audio"
                      >
                        {isLoadingTts ? (
                          <>
                            <Loader2 className="w-3.5 h-3.5 animate-spin" />
                            <span>Synthesizing...</span>
                          </>
                        ) : (
                          <>
                            <Volume2 className="w-3.5 h-3.5" />
                            <span>{entry.status === 'verified' ? 'Regenerate' : 'Generate TTS'}</span>
                          </>
                        )}
                      </button>
                    )}

                    {/* Edit button */}
                    {!isPreviewing && (
                      <button
                        onClick={() => startEditing(entry)}
                        className="p-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white border border-slate-700 transition-colors"
                        title="Edit entry fields / Tonos"
                      >
                        <Edit3 className="w-3.5 h-3.5" />
                      </button>
                    )}

                    {/* Learner Progress Controls: Learned, Rating, Ignore */}
                    {!isPreviewing && (
                      <div className="flex items-center gap-1.5 pl-1 border-l border-slate-700/60">
                        {/* Toggle Learned */}
                        <button
                          type="button"
                          onClick={() => handleToggleCardLearnedInEditor(entry.id)}
                          className={`inline-flex items-center gap-1 px-2.5 py-1.5 rounded-xl text-xs font-semibold border transition-all ${
                            cardSrs.isLearned
                              ? 'bg-teal-600 border-teal-500 text-white shadow-sm'
                              : 'bg-slate-800 border-slate-700 text-slate-400 hover:text-white'
                          }`}
                          title={cardSrs.isLearned ? 'Marked as Learned (click to unmark)' : 'Mark card as Learned'}
                        >
                          <CheckCircle className="w-3.5 h-3.5" />
                          <span className="hidden md:inline">{cardSrs.isLearned ? 'Learned' : 'Learn'}</span>
                        </button>

                        {/* Rating Selector */}
                        <select
                          value={cardRating}
                          onChange={(e) => handleRateCardInEditor(entry.id, e.target.value as SRSRating)}
                          className={`text-xs font-semibold px-2 py-1.5 rounded-xl border focus:outline-none cursor-pointer transition-colors ${
                            cardRating === 'easy'
                              ? 'bg-emerald-950/80 text-emerald-300 border-emerald-700'
                              : cardRating === 'good'
                              ? 'bg-sky-950/80 text-sky-300 border-sky-700'
                              : cardRating === 'hard'
                              ? 'bg-amber-950/80 text-amber-300 border-amber-700'
                              : cardRating === 'again'
                              ? 'bg-rose-950/80 text-rose-300 border-rose-700'
                              : 'bg-slate-800 text-slate-300 border-slate-700'
                          }`}
                          title="Set card SRS rating"
                        >
                          <option value="new" className="bg-slate-900 text-slate-400">Rating: New</option>
                          <option value="again" className="bg-slate-900 text-rose-400">Again [1]</option>
                          <option value="hard" className="bg-slate-900 text-amber-400">Hard [2]</option>
                          <option value="good" className="bg-slate-900 text-sky-400">Good [3]</option>
                          <option value="easy" className="bg-slate-900 text-emerald-400">Easy [4]</option>
                        </select>

                        {/* Toggle Ignore */}
                        <button
                          type="button"
                          onClick={() => handleToggleCardExcludedInEditor(entry.id)}
                          className={`p-2 rounded-xl border transition-all ${
                            cardSrs.isExcluded
                              ? 'bg-rose-900 border-rose-600 text-rose-200'
                              : 'bg-slate-800 border-slate-700 text-slate-500 hover:text-rose-400'
                          }`}
                          title={cardSrs.isExcluded ? 'Ignored card (click to un-ignore)' : 'Ignore card'}
                        >
                          <Ban className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    )}

                    {/* THE IN-MEMORY DECISION PIPELINE (Listen, Accept or Reject) */}
                    {isPreviewing && (
                      <div className="flex flex-col sm:flex-row items-center gap-3 p-2.5 rounded-xl bg-slate-900 border border-sky-400/50 shadow-inner">
                        <div className="flex items-center gap-2">
                          <AudioPlayer
                            src={activePreview.audioBase64}
                            autoPlay
                            label="Preview in Memory"
                          />
                        </div>

                        <div className="flex items-center gap-2">
                          {/* Button A: Accept (Green) */}
                          <button
                            type="button"
                            onClick={handleAcceptAudio}
                            className="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold shadow-md shadow-emerald-600/30 transition-all hover:scale-105 active:scale-95"
                            title="Accept pronunciation and commit to /audio"
                          >
                            <Check className="w-4 h-4 stroke-[3]" />
                            <span>Accept</span>
                          </button>

                          {/* Button B: Reject (Red) */}
                          <button
                            type="button"
                            onClick={() => handleRejectAudio(entry)}
                            className="inline-flex items-center gap-1.5 px-3 py-2 rounded-lg bg-rose-600 hover:bg-rose-500 text-white text-xs font-bold shadow-md shadow-rose-600/30 transition-all hover:scale-105 active:scale-95"
                            title="Reject audio, discard buffer, and refine spelling/tonos"
                          >
                            <X className="w-4 h-4 stroke-[3]" />
                            <span>Reject</span>
                          </button>
                        </div>
                      </div>
                    )}
                  </div>
                </div>
              )}
            </div>
          );
        })}
        </div>
      )}
    </div>
  );
};

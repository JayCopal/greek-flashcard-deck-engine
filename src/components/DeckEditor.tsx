import React, { useState, useEffect } from 'react';
import { DeckData, Lesson, CardEntry, ChirpVoice } from '../types/schema';
import { AudioPlayer } from './AudioPlayer';
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
  ArrowLeft
} from 'lucide-react';

interface DeckEditorProps {
  deck: DeckData;
  initialUnitId?: string;
  initialLessonId?: string;
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
  onBackToDashboard,
  onRefresh,
}) => {
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
          speaking_rate: 0.95,
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
          {/* Unit selector */}
          <div>
            <label className="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5">
              Select Unit
            </label>
            <select
              value={selectedUnitId}
              onChange={(e) => setSelectedUnitId(e.target.value)}
              className="w-full bg-slate-800 text-white border border-slate-700 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-sky-500 transition-colors"
            >
              {units.map((u) => (
                <option key={u.id} value={u.id}>
                  Unit {u.order}: {u.title}
                </option>
              ))}
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

          {/* Google Chirp 3 Voice Selector */}
          <div>
            <label className="block text-xs font-semibold text-slate-400 uppercase tracking-wider mb-1.5 flex items-center justify-between">
              <span>Chirp 3 Voice</span>
              <span className="text-[10px] text-sky-400 font-medium">Google Cloud TTS</span>
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
        </div>

        {/* Selected voice description tooltip */}
        {activeVoiceObj && (
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

      {/* Lesson Info & Actions Header */}
      <div className="flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-white tracking-tight">
            {currentLesson?.title}
          </h2>
          {currentLesson?.description && (
            <p className="text-xs text-slate-400 mt-0.5">{currentLesson.description}</p>
          )}
        </div>
        <button
          onClick={() => setIsAddingCard(!isAddingCard)}
          className="inline-flex items-center gap-1.5 px-3.5 py-2 rounded-xl bg-sky-500/20 hover:bg-sky-500/30 text-sky-300 font-semibold text-xs border border-sky-500/30 transition-all"
        >
          <Plus className="w-4 h-4" /> {isAddingCard ? 'Cancel New Card' : 'Add Card to YAML'}
        </button>
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

      {/* Cards List */}
      <div className="space-y-4">
        {currentLesson?.entries.map((entry) => {
          const isPreviewing = activePreview?.entryId === entry.id;
          const isEditing = editingEntryId === entry.id;
          const isLoadingTts = loadingTtsId === entry.id;

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
                      <AudioPlayer src={`/audio/${entry.audio}`} mini label="Verified" />
                    )}

                    {/* TTS Generation Button */}
                    {!isPreviewing && (
                      <button
                        onClick={() => handleGenerateTTS(entry)}
                        disabled={isLoadingTts}
                        className={`inline-flex items-center gap-1.5 px-3 py-2 rounded-xl text-xs font-semibold transition-all ${
                          entry.status === 'verified'
                            ? 'bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700'
                            : 'bg-sky-500 hover:bg-sky-400 text-white shadow-md shadow-sky-500/20'
                        } disabled:opacity-50`}
                        title="Generate Chirp 3 Audio"
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
    </div>
  );
};

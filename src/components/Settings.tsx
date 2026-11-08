import React, { useState, useEffect } from 'react';
import { UserProfile } from '../types/schema';
import {
  getUsers,
  getActiveUser,
  setActiveUserId,
  createUser,
  renameUser,
  resetUserProgress,
  getUserStudyPreferences,
  setUserStudyPreferences,
  UserStudyPreferences,
} from '../utils/userStorage';
import { getAllSRSData } from '../utils/srs';
import {
  Settings as SettingsIcon,
  User,
  UserPlus,
  Edit3,
  RotateCcw,
  Check,
  X,
  Volume2,
  ArrowUpDown,
  EyeOff,
  Ban,
  Download,
  WifiOff,
  RefreshCw,
  Sparkles,
  BookOpen,
  Moon,
  Sun,
  Smartphone,
  Target,
  Gauge,
  Type
} from 'lucide-react';

interface SettingsProps {
  isOfflineMode: boolean;
  onRefreshDeck: () => Promise<void>;
  loadingDeck: boolean;
  installPrompt: any | null;
  isInstalled: boolean;
  onInstallApp: () => Promise<void>;
  onGoToStudy?: () => void;
  onGoToDashboard?: () => void;
}

export const Settings: React.FC<SettingsProps> = ({
  isOfflineMode,
  onRefreshDeck,
  loadingDeck,
  installPrompt,
  isInstalled,
  onInstallApp,
  onGoToDashboard,
}) => {
  const [users, setUsers] = useState<UserProfile[]>([]);
  const [activeUser, setActiveUser] = useState<UserProfile | null>(null);

  // New user state
  const [isAddingUser, setIsAddingUser] = useState(false);
  const [newUserName, setNewUserName] = useState('');

  // Rename state
  const [isRenaming, setIsRenaming] = useState(false);
  const [renameInput, setRenameInput] = useState('');

  // Reset progress confirm
  const [confirmReset, setConfirmReset] = useState(false);

  // Study preferences state
  const [studyPrefs, setStudyPrefs] = useState<UserStudyPreferences>(getUserStudyPreferences());

  const loadData = () => {
    const allUsers = getUsers();
    setUsers(allUsers);
    const currUser = getActiveUser();
    setActiveUser(currUser);
    setStudyPrefs(getUserStudyPreferences(currUser.id));
  };

  useEffect(() => {
    loadData();

    const handleUserChange = () => {
      loadData();
    };

    window.addEventListener('greek_deck_user_change', handleUserChange);
    window.addEventListener('greek_deck_progress_change', handleUserChange);

    return () => {
      window.removeEventListener('greek_deck_user_change', handleUserChange);
      window.removeEventListener('greek_deck_progress_change', handleUserChange);
    };
  }, []);

  const handleSelectUser = (userId: string) => {
    setActiveUserId(userId);
    const currUser = getActiveUser();
    setActiveUser(currUser);
    setStudyPrefs(getUserStudyPreferences(currUser.id));
  };

  const handleCreateUser = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newUserName.trim()) return;
    const created = createUser(newUserName.trim());
    setNewUserName('');
    setIsAddingUser(false);
    setActiveUserId(created.id);
    loadData();
  };

  const handleSaveRename = () => {
    if (!activeUser || !renameInput.trim()) return;
    renameUser(activeUser.id, renameInput.trim());
    setIsRenaming(false);
    loadData();
  };

  const handleReset = () => {
    if (!activeUser) return;
    resetUserProgress(activeUser.id);
    setConfirmReset(false);
    loadData();
  };

  const updatePreference = (patch: Partial<UserStudyPreferences>) => {
    if (!activeUser) return;
    const updated = setUserStudyPreferences(patch, activeUser.id);
    setStudyPrefs(updated);
  };

  const userSRS = activeUser ? getAllSRSData(activeUser.id) : {};
  const learnedCount = Object.values(userSRS).filter((c) => c.isLearned && !c.isExcluded).length;
  const totalReviewed = Object.keys(userSRS).length;

  return (
    <div className="max-w-4xl mx-auto space-y-8 pb-16">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-slate-800">
        <div>
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-sky-500/10 border border-sky-500/20 text-sky-400 text-xs font-semibold mb-2">
            <SettingsIcon className="w-3.5 h-3.5" />
            <span>Preferences & Settings</span>
          </div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
            Settings
          </h1>
          <p className="text-sm text-slate-400 mt-1">
            Manage your learner profile, card study preferences, and application settings
          </p>
        </div>

        {onGoToDashboard && (
          <button
            onClick={onGoToDashboard}
            className="self-start sm:self-auto px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-xs font-semibold text-slate-300 hover:text-white border border-slate-700 transition-colors"
          >
            Back to Dashboard
          </button>
        )}
      </div>

      {/* Section 1: Learner Profile & Multi-User Management */}
      <div className="glass-panel p-6 rounded-2xl border-slate-800 space-y-5">
        <div className="flex items-center justify-between pb-3 border-b border-slate-800/80">
          <div className="flex items-center gap-2.5">
            <div className="w-8 h-8 rounded-lg bg-sky-500/15 border border-sky-500/30 flex items-center justify-center text-sky-400">
              <User className="w-4 h-4" />
            </div>
            <div>
              <h2 className="text-base font-bold text-white">Learner Profile</h2>
              <p className="text-xs text-slate-400">Select or create learner profiles with isolated SRS progress</p>
            </div>
          </div>

          <button
            onClick={() => setIsAddingUser(!isAddingUser)}
            className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl bg-sky-500/20 hover:bg-sky-500/30 text-sky-300 border border-sky-500/30 text-xs font-semibold transition-colors"
          >
            <UserPlus className="w-3.5 h-3.5" />
            <span>Add Learner</span>
          </button>
        </div>

        {/* Add Learner Form */}
        {isAddingUser && (
          <form onSubmit={handleCreateUser} className="p-4 rounded-xl bg-slate-900 border border-slate-800 space-y-3">
            <label className="text-xs font-semibold text-slate-300 block">New Learner Name</label>
            <div className="flex gap-2">
              <input
                type="text"
                placeholder="e.g. Maria, Alex"
                value={newUserName}
                onChange={(e) => setNewUserName(e.target.value)}
                autoFocus
                className="flex-1 px-3 py-2 rounded-xl bg-slate-800 border border-slate-700 text-xs text-white placeholder-slate-500 focus:outline-none focus:border-sky-500"
              />
              <button
                type="submit"
                disabled={!newUserName.trim()}
                className="px-4 py-2 rounded-xl bg-sky-500 hover:bg-sky-400 disabled:opacity-50 text-white text-xs font-semibold"
              >
                Create
              </button>
              <button
                type="button"
                onClick={() => {
                  setIsAddingUser(false);
                  setNewUserName('');
                }}
                className="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 text-xs"
              >
                Cancel
              </button>
            </div>
          </form>
        )}

        {/* Active Profile Card */}
        {activeUser && (
          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div className="flex items-center gap-3">
              <div
                className="w-11 h-11 rounded-xl flex items-center justify-center font-bold text-white shadow-md text-base"
                style={{ backgroundColor: activeUser.color || '#0284c7' }}
              >
                {activeUser.name.charAt(0).toUpperCase()}
              </div>
              <div>
                <div className="flex items-center gap-2">
                  <span className="font-bold text-white text-base">{activeUser.name}</span>
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                    Active
                  </span>
                </div>
                <p className="text-xs text-slate-400 mt-0.5">
                  {learnedCount} mastered • {totalReviewed} total reviewed cards
                </p>
              </div>
            </div>

            <div className="flex items-center gap-2">
              {isRenaming ? (
                <div className="flex items-center gap-1.5">
                  <input
                    type="text"
                    value={renameInput}
                    onChange={(e) => setRenameInput(e.target.value)}
                    className="px-2.5 py-1 rounded-lg bg-slate-800 border border-slate-700 text-xs text-white focus:outline-none focus:border-sky-500 w-32"
                    autoFocus
                  />
                  <button
                    onClick={handleSaveRename}
                    className="p-1.5 rounded-lg bg-sky-500 text-white"
                    title="Save name"
                  >
                    <Check className="w-3.5 h-3.5" />
                  </button>
                  <button
                    onClick={() => setIsRenaming(false)}
                    className="p-1.5 rounded-lg bg-slate-800 text-slate-400"
                    title="Cancel"
                  >
                    <X className="w-3.5 h-3.5" />
                  </button>
                </div>
              ) : (
                <button
                  onClick={() => {
                    setRenameInput(activeUser.name);
                    setIsRenaming(true);
                  }}
                  className="px-3 py-1.5 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-colors flex items-center gap-1.5"
                >
                  <Edit3 className="w-3.5 h-3.5" />
                  <span>Rename</span>
                </button>
              )}

              {confirmReset ? (
                <div className="flex items-center gap-1.5">
                  <span className="text-xs text-rose-400 font-semibold">Reset progress?</span>
                  <button
                    onClick={handleReset}
                    className="px-2.5 py-1 rounded-lg bg-rose-600 hover:bg-rose-500 text-white text-xs font-bold"
                  >
                    Yes
                  </button>
                  <button
                    onClick={() => setConfirmReset(false)}
                    className="px-2.5 py-1 rounded-lg bg-slate-800 text-slate-400 text-xs"
                  >
                    No
                  </button>
                </div>
              ) : (
                <button
                  onClick={() => setConfirmReset(true)}
                  className="px-3 py-1.5 rounded-xl bg-rose-950/40 hover:bg-rose-950/70 text-rose-300 text-xs font-semibold border border-rose-800/60 transition-colors flex items-center gap-1.5"
                  title="Reset all flashcard ratings and mastered status for this learner"
                >
                  <RotateCcw className="w-3.5 h-3.5" />
                  <span>Reset Progress</span>
                </button>
              )}
            </div>
          </div>
        )}

        {/* Switch Learner List */}
        {users.length > 1 && (
          <div className="space-y-2 pt-2">
            <span className="text-xs font-semibold text-slate-400 block uppercase tracking-wider">
              Switch Learner ({users.length})
            </span>
            <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-2.5">
              {users.map((u) => {
                const isSelected = u.id === activeUser?.id;
                const srs = getAllSRSData(u.id);
                const count = Object.values(srs).filter((c) => c.isLearned && !c.isExcluded).length;

                return (
                  <button
                    key={u.id}
                    onClick={() => handleSelectUser(u.id)}
                    className={`p-3 rounded-xl border text-left transition-all flex items-center gap-2.5 ${
                      isSelected
                        ? 'bg-sky-500/15 border-sky-500/50 shadow-sm'
                        : 'bg-slate-900/50 hover:bg-slate-900 border-slate-800 hover:border-slate-700'
                    }`}
                  >
                    <div
                      className="w-8 h-8 rounded-lg flex items-center justify-center font-bold text-white text-xs shrink-0"
                      style={{ backgroundColor: u.color || '#0284c7' }}
                    >
                      {u.name.charAt(0).toUpperCase()}
                    </div>
                    <div className="min-w-0 flex-1">
                      <div className="font-semibold text-xs text-white truncate">{u.name}</div>
                      <div className="text-[11px] text-slate-400">{count} learned</div>
                    </div>
                    {isSelected && <Check className="w-4 h-4 text-sky-400 shrink-0" />}
                  </button>
                );
              })}
            </div>
          </div>
        )}
      </div>

      {/* Section 2: Flashcard Study & Drill Preferences */}
      <div className="glass-panel p-6 rounded-2xl border-slate-800 space-y-5">
        <div className="flex items-center gap-2.5 pb-3 border-b border-slate-800/80">
          <div className="w-8 h-8 rounded-lg bg-indigo-500/15 border border-indigo-500/30 flex items-center justify-center text-indigo-400">
            <Sparkles className="w-4 h-4" />
          </div>
          <div>
            <h2 className="text-base font-bold text-white">Study & Flashcard Preferences</h2>
            <p className="text-xs text-slate-400">Configure default card behavior, prompt direction, and audio</p>
          </div>
        </div>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
          {/* Study Prompt Direction */}
          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-xs font-semibold text-slate-200 flex items-center gap-1.5">
                <ArrowUpDown className="w-3.5 h-3.5 text-sky-400" />
                Prompt Direction
              </span>
              <span className="text-[11px] font-bold text-sky-400">
                {studyPrefs.studyDirection === 'english_to_greek' ? 'English → Greek' : 'Greek → English'}
              </span>
            </div>
            <p className="text-[11px] text-slate-400 leading-relaxed">
              Choose which language is shown on the front prompt and which is revealed on flip.
            </p>
            <div className="flex gap-2 pt-1">
              <button
                type="button"
                onClick={() => updatePreference({ studyDirection: 'greek_to_english' })}
                className={`flex-1 py-1.5 px-3 rounded-lg text-xs font-semibold border transition-all ${
                  studyPrefs.studyDirection !== 'english_to_greek'
                    ? 'bg-sky-500 text-white border-sky-400 shadow-sm'
                    : 'bg-slate-800 text-slate-400 border-slate-700 hover:text-white'
                }`}
              >
                Greek → English
              </button>
              <button
                type="button"
                onClick={() => updatePreference({ studyDirection: 'english_to_greek' })}
                className={`flex-1 py-1.5 px-3 rounded-lg text-xs font-semibold border transition-all ${
                  studyPrefs.studyDirection === 'english_to_greek'
                    ? 'bg-sky-500 text-white border-sky-400 shadow-sm'
                    : 'bg-slate-800 text-slate-400 border-slate-700 hover:text-white'
                }`}
              >
                English → Greek
              </button>
            </div>
          </div>

          {/* Auto-Play Native Audio */}
          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-xs font-semibold text-slate-200 flex items-center gap-1.5">
                <Volume2 className="w-3.5 h-3.5 text-teal-400" />
                Auto-play Native Audio
              </span>
              <button
                type="button"
                onClick={() => updatePreference({ autoPlayAudio: !studyPrefs.autoPlayAudio })}
                className={`px-2.5 py-1 rounded-lg text-xs font-bold border transition-all ${
                  studyPrefs.autoPlayAudio
                    ? 'bg-teal-500/20 text-teal-300 border-teal-500/40'
                    : 'bg-slate-800 text-slate-400 border-slate-700'
                }`}
              >
                {studyPrefs.autoPlayAudio ? 'Enabled' : 'Disabled'}
              </button>
            </div>
            <p className="text-[11px] text-slate-400 leading-relaxed">
              Automatically play native speaker pronunciation when a new Greek card is loaded.
            </p>
          </div>

          {/* Hide Learned Cards Default */}
          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-xs font-semibold text-slate-200 flex items-center gap-1.5">
                <EyeOff className="w-3.5 h-3.5 text-emerald-400" />
                Hide Learned Cards
              </span>
              <button
                type="button"
                onClick={() => updatePreference({ hideLearned: !studyPrefs.hideLearned })}
                className={`px-2.5 py-1 rounded-lg text-xs font-bold border transition-all ${
                  studyPrefs.hideLearned
                    ? 'bg-emerald-500/20 text-emerald-300 border-emerald-500/40'
                    : 'bg-slate-800 text-slate-400 border-slate-700'
                }`}
              >
                {studyPrefs.hideLearned ? 'Hidden' : 'Shown'}
              </button>
            </div>
            <p className="text-[11px] text-slate-400 leading-relaxed">
              Exclude cards marked as learned from study sessions so you can focus on active vocabulary.
            </p>
          </div>

          {/* Hide Ignored Cards Default */}
          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-xs font-semibold text-slate-200 flex items-center gap-1.5">
                <Ban className="w-3.5 h-3.5 text-rose-400" />
                Hide Ignored Cards
              </span>
              <button
                type="button"
                onClick={() => updatePreference({ hideExcluded: !studyPrefs.hideExcluded })}
                className={`px-2.5 py-1 rounded-lg text-xs font-bold border transition-all ${
                  studyPrefs.hideExcluded
                    ? 'bg-rose-500/20 text-rose-300 border-rose-500/40'
                    : 'bg-slate-800 text-slate-400 border-slate-700'
                }`}
              >
                {studyPrefs.hideExcluded ? 'Hidden' : 'Shown'}
              </button>
            </div>
            <p className="text-[11px] text-slate-400 leading-relaxed">
              Skip cards that you have marked to ignore during review sessions.
            </p>
          </div>

          {/* Daily Review Goal */}
          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-xs font-semibold text-slate-200 flex items-center gap-1.5">
                <Target className="w-3.5 h-3.5 text-sky-400" />
                Daily Review Target
              </span>
              <span className="text-xs font-bold text-sky-400">
                {studyPrefs.dailyGoal || 20} cards/day
              </span>
            </div>
            <p className="text-[11px] text-slate-400 leading-relaxed">
              Target number of card reviews per day to maintain your learning streak.
            </p>
            <div className="flex gap-1.5 pt-1">
              {[10, 15, 20, 30, 50].map((goal) => (
                <button
                  key={goal}
                  type="button"
                  onClick={() => updatePreference({ dailyGoal: goal })}
                  className={`flex-1 py-1 px-2 rounded-lg text-xs font-semibold border transition-all ${
                    (studyPrefs.dailyGoal || 20) === goal
                      ? 'bg-sky-500 text-white border-sky-400 shadow-sm'
                      : 'bg-slate-800 text-slate-400 border-slate-700 hover:text-white'
                  }`}
                >
                  {goal}
                </button>
              ))}
            </div>
          </div>

          {/* Theme Preference (Slate Dark vs OLED Pure Black) */}
          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-xs font-semibold text-slate-200 flex items-center gap-1.5">
                <Moon className="w-3.5 h-3.5 text-indigo-400" />
                Display Theme
              </span>
              <span className="text-[11px] font-bold text-indigo-300">
                {studyPrefs.themePreference === 'oled' ? 'OLED Pure Black' : 'Slate Dark'}
              </span>
            </div>
            <p className="text-[11px] text-slate-400 leading-relaxed">
              OLED Pure Black uses true black backgrounds (#000000) for battery saving and high contrast.
            </p>
            <div className="flex gap-2 pt-1">
              <button
                type="button"
                onClick={() => updatePreference({ themePreference: 'slate' })}
                className={`flex-1 py-1.5 px-3 rounded-lg text-xs font-semibold border transition-all flex items-center justify-center gap-1.5 ${
                  studyPrefs.themePreference !== 'oled'
                    ? 'bg-sky-500 text-white border-sky-400 shadow-sm'
                    : 'bg-slate-800 text-slate-400 border-slate-700 hover:text-white'
                }`}
              >
                <Sun className="w-3.5 h-3.5" />
                <span>Slate Dark</span>
              </button>
              <button
                type="button"
                onClick={() => updatePreference({ themePreference: 'oled' })}
                className={`flex-1 py-1.5 px-3 rounded-lg text-xs font-semibold border transition-all flex items-center justify-center gap-1.5 ${
                  studyPrefs.themePreference === 'oled'
                    ? 'bg-sky-500 text-white border-sky-400 shadow-sm'
                    : 'bg-slate-800 text-slate-400 border-slate-700 hover:text-white'
                }`}
              >
                <Moon className="w-3.5 h-3.5" />
                <span>OLED Black</span>
              </button>
            </div>
          </div>

          {/* Default Audio Playback Speed */}
          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-xs font-semibold text-slate-200 flex items-center gap-1.5">
                <Gauge className="w-3.5 h-3.5 text-amber-400" />
                Default Audio Speed
              </span>
              <span className="text-xs font-bold text-amber-400">
                {studyPrefs.playbackSpeed || 1.0}x
              </span>
            </div>
            <p className="text-[11px] text-slate-400 leading-relaxed">
              Choose default native speech speed for pronunciation drills.
            </p>
            <div className="flex gap-2 pt-1">
              {[0.75, 1.0, 1.25].map((speed) => (
                <button
                  key={speed}
                  type="button"
                  onClick={() => updatePreference({ playbackSpeed: speed })}
                  className={`flex-1 py-1.5 px-3 rounded-lg text-xs font-semibold border transition-all ${
                    (studyPrefs.playbackSpeed || 1.0) === speed
                      ? 'bg-amber-500/20 text-amber-300 border-amber-500/50 shadow-sm'
                      : 'bg-slate-800 text-slate-400 border-slate-700 hover:text-white'
                  }`}
                >
                  {speed}x {speed === 1.0 ? '(Normal)' : speed < 1 ? '(Slower)' : '(Faster)'}
                </button>
              ))}
            </div>
          </div>

          {/* Tonos Stressed Vowel Accentuation */}
          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-xs font-semibold text-slate-200 flex items-center gap-1.5">
                <Type className="w-3.5 h-3.5 text-amber-400" />
                Stressed Vowel Highlight (Tonos)
              </span>
              <button
                type="button"
                onClick={() => updatePreference({ highlightTonos: !studyPrefs.highlightTonos })}
                className={`px-2.5 py-1 rounded-lg text-xs font-bold border transition-all ${
                  studyPrefs.highlightTonos !== false
                    ? 'bg-amber-500/20 text-amber-300 border-amber-500/40'
                    : 'bg-slate-800 text-slate-400 border-slate-700'
                }`}
              >
                {studyPrefs.highlightTonos !== false ? 'Enabled' : 'Disabled'}
              </button>
            </div>
            <p className="text-[11px] text-slate-400 leading-relaxed">
              Visually accentuates accented vowels (ά, έ, ή, ί, ό, ύ, ώ) with a soft warm amber highlight to build correct pronunciation instincts.
            </p>
          </div>

          {/* Safe Mobile Haptic Feedback */}
          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-xs font-semibold text-slate-200 flex items-center gap-1.5">
                <Smartphone className="w-3.5 h-3.5 text-teal-400" />
                Mobile Haptic Feedback
              </span>
              <button
                type="button"
                onClick={() => updatePreference({ hapticFeedback: !studyPrefs.hapticFeedback })}
                className={`px-2.5 py-1 rounded-lg text-xs font-bold border transition-all ${
                  studyPrefs.hapticFeedback !== false
                    ? 'bg-teal-500/20 text-teal-300 border-teal-500/40'
                    : 'bg-slate-800 text-slate-400 border-slate-700'
                }`}
              >
                {studyPrefs.hapticFeedback !== false ? 'Enabled' : 'Disabled'}
              </button>
            </div>
            <p className="text-[11px] text-slate-400 leading-relaxed">
              Vibration feedback on supported touch devices when flipping cards and rating SRS assessments.
            </p>
          </div>
        </div>
      </div>

      {/* Section 3: App, PWA & Storage Engine */}
      <div className="glass-panel p-6 rounded-2xl border-slate-800 space-y-5">
        <div className="flex items-center gap-2.5 pb-3 border-b border-slate-800/80">
          <div className="w-8 h-8 rounded-lg bg-teal-500/15 border border-teal-500/30 flex items-center justify-center text-teal-400">
            <BookOpen className="w-4 h-4" />
          </div>
          <div>
            <h2 className="text-base font-bold text-white">Application & PWA Engine</h2>
            <p className="text-xs text-slate-400">Offline status, disk synchronization, and PWA installation</p>
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
          {/* PWA Install */}
          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 flex flex-col justify-between space-y-3">
            <div>
              <div className="flex items-center justify-between mb-1">
                <span className="text-xs font-semibold text-white">Progressive Web App</span>
                {isInstalled ? (
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">
                    Installed
                  </span>
                ) : (
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-slate-800 text-slate-400 border border-slate-700">
                    Browser Tab
                  </span>
                )}
              </div>
              <p className="text-[11px] text-slate-400 leading-relaxed">
                Install GreekDeck as a standalone mobile or desktop application with offline caching.
              </p>
            </div>

            {installPrompt && !isInstalled ? (
              <button
                onClick={onInstallApp}
                className="w-full inline-flex items-center justify-center gap-2 px-3 py-2 rounded-xl bg-gradient-to-r from-sky-500 to-indigo-600 hover:from-sky-400 hover:to-indigo-500 text-white text-xs font-bold shadow-md shadow-sky-500/20 transition-all"
              >
                <Download className="w-3.5 h-3.5" />
                <span>Install PWA App</span>
              </button>
            ) : (
              <div className="text-[11px] text-slate-500 italic">
                {isInstalled ? 'App is running in standalone mode.' : 'Already installed or use browser menu to install.'}
              </div>
            )}
          </div>

          {/* Sync / Reload from Disk */}
          <div className="p-4 rounded-xl bg-slate-900/80 border border-slate-800 flex flex-col justify-between space-y-3">
            <div>
              <div className="flex items-center justify-between mb-1">
                <span className="text-xs font-semibold text-white">Deck Synchronization</span>
                {isOfflineMode ? (
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-teal-500/20 text-teal-300 border border-teal-500/30 flex items-center gap-1">
                    <WifiOff className="w-3 h-3" /> Offline PWA
                  </span>
                ) : (
                  <span className="text-[10px] font-bold px-2 py-0.5 rounded-full bg-sky-500/20 text-sky-300 border border-sky-500/30">
                    Live Local Server
                  </span>
                )}
              </div>
              <p className="text-[11px] text-slate-400 leading-relaxed">
                Reload YAML manifests and card entries from disk or check for cached PWA updates.
              </p>
            </div>

            <button
              onClick={onRefreshDeck}
              disabled={loadingDeck}
              className="w-full inline-flex items-center justify-center gap-2 px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold transition-all disabled:opacity-50"
            >
              <RefreshCw className={`w-3.5 h-3.5 ${loadingDeck ? 'animate-spin' : ''}`} />
              <span>{loadingDeck ? 'Reloading...' : 'Reload Deck from Disk'}</span>
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

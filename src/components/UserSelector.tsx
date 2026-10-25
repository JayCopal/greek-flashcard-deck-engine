import React, { useState, useEffect } from 'react';
import { UserProfile } from '../types/schema';
import {
  getUsers,
  getActiveUser,
  setActiveUserId,
  createUser,
  renameUser,
  deleteUser,
  resetUserProgress,
} from '../utils/userStorage';
import { getAllSRSData } from '../utils/srs';
import { 
  Users, 
  UserCheck, 
  UserPlus, 
  Edit3, 
  Trash2, 
  RotateCcw, 
  X, 
  Check, 
  ChevronDown 
} from 'lucide-react';

export const UserSelector: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [users, setUsers] = useState<UserProfile[]>([]);
  const [activeUser, setActiveUser] = useState<UserProfile | null>(null);
  
  // New user input
  const [isAdding, setIsAdding] = useState(false);
  const [newUserName, setNewUserName] = useState('');

  // Editing state
  const [editingUserId, setEditingUserId] = useState<string | null>(null);
  const [editNameInput, setEditNameInput] = useState('');

  // Confirm delete or reset
  const [confirmDeleteId, setConfirmDeleteId] = useState<string | null>(null);
  const [confirmReset, setConfirmReset] = useState(false);

  const loadUserData = () => {
    const allUsers = getUsers();
    setUsers(allUsers);
    setActiveUser(getActiveUser());
  };

  useEffect(() => {
    loadUserData();

    const handleUserChange = () => {
      loadUserData();
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
    setIsOpen(false);
  };

  const handleCreateUser = (e: React.FormEvent) => {
    e.preventDefault();
    if (!newUserName.trim()) return;
    createUser(newUserName);
    setNewUserName('');
    setIsAdding(false);
    loadUserData();
  };

  const handleStartRename = (user: UserProfile) => {
    setEditingUserId(user.id);
    setEditNameInput(user.name);
  };

  const handleSaveRename = (userId: string) => {
    if (editNameInput.trim()) {
      renameUser(userId, editNameInput.trim());
      setEditingUserId(null);
      loadUserData();
    }
  };

  const handleDeleteUser = (userId: string) => {
    deleteUser(userId);
    setConfirmDeleteId(null);
    loadUserData();
  };

  const handleResetProgress = () => {
    if (!activeUser) return;
    resetUserProgress(activeUser.id);
    setConfirmReset(false);
    loadUserData();
  };

  if (!activeUser) return null;

  return (
    <div className="relative">
      {/* Active User Button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-800/90 hover:bg-slate-700/90 border border-slate-700/80 text-white transition-all shadow-sm group"
        title="Switch or manage learner profile"
      >
        <div
          className="w-5 h-5 rounded-full flex items-center justify-center text-[11px] font-bold text-white shadow-inner"
          style={{ backgroundColor: activeUser.color || '#0284c7' }}
        >
          {activeUser.name.charAt(0).toUpperCase()}
        </div>
        <span className="text-xs font-semibold max-w-[90px] sm:max-w-[120px] truncate">
          {activeUser.name}
        </span>
        <ChevronDown className={`w-3.5 h-3.5 text-slate-400 group-hover:text-white transition-transform ${isOpen ? 'rotate-180' : ''}`} />
      </button>

      {/* Modal / Dropdown Backdrop */}
      {isOpen && (
        <>
          <div
            className="fixed inset-0 z-40 bg-black/60 backdrop-blur-sm sm:hidden"
            onClick={() => setIsOpen(false)}
          />

          <div className="fixed sm:absolute right-4 sm:right-0 top-16 sm:top-full mt-2 w-[calc(100vw-32px)] sm:w-96 max-w-sm z-50 bg-slate-900 border border-slate-700/80 rounded-2xl shadow-2xl p-4 sm:p-5 text-slate-200">
            {/* Header */}
            <div className="flex items-center justify-between pb-3 mb-3 border-b border-slate-800">
              <div className="flex items-center gap-2">
                <Users className="w-4 h-4 text-sky-400" />
                <h3 className="text-sm font-bold text-white">Learner Profiles</h3>
              </div>
              <button
                onClick={() => setIsOpen(false)}
                className="p-1 rounded-lg text-slate-400 hover:text-white hover:bg-slate-800 transition-colors"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <p className="text-[11px] text-slate-400 mb-3">
              Progress, marked cards, and SRS intervals are stored locally on this device for each learner profile.
            </p>

            {/* Profile List */}
            <div className="space-y-2 max-h-56 overflow-y-auto pr-1 mb-4">
              {users.map((user) => {
                const isActive = user.id === activeUser.id;
                const userSRS = getAllSRSData(user.id);
                const learnedCount = Object.values(userSRS).filter((c) => c.isLearned).length;

                return (
                  <div
                    key={user.id}
                    className={`flex items-center justify-between p-2.5 rounded-xl border transition-all ${
                      isActive
                        ? 'bg-sky-500/10 border-sky-500/40 text-white'
                        : 'bg-slate-800/50 border-slate-700/60 hover:bg-slate-800'
                    }`}
                  >
                    {editingUserId === user.id ? (
                      <div className="flex items-center gap-2 flex-1 mr-2">
                        <input
                          type="text"
                          value={editNameInput}
                          onChange={(e) => setEditNameInput(e.target.value)}
                          className="w-full bg-slate-950 border border-sky-500 rounded px-2 py-1 text-xs text-white focus:outline-none"
                          autoFocus
                          onKeyDown={(e) => {
                            if (e.key === 'Enter') handleSaveRename(user.id);
                            if (e.key === 'Escape') setEditingUserId(null);
                          }}
                        />
                        <button
                          onClick={() => handleSaveRename(user.id)}
                          className="p-1 text-emerald-400 hover:bg-emerald-500/20 rounded"
                          title="Save"
                        >
                          <Check className="w-3.5 h-3.5" />
                        </button>
                        <button
                          onClick={() => setEditingUserId(null)}
                          className="p-1 text-slate-400 hover:bg-slate-700 rounded"
                          title="Cancel"
                        >
                          <X className="w-3.5 h-3.5" />
                        </button>
                      </div>
                    ) : (
                      <>
                        <div
                          onClick={() => handleSelectUser(user.id)}
                          className="flex items-center gap-2.5 flex-1 cursor-pointer select-none"
                        >
                          <div
                            className="w-7 h-7 rounded-full flex items-center justify-center text-xs font-bold text-white shadow"
                            style={{ backgroundColor: user.color || '#0284c7' }}
                          >
                            {user.name.charAt(0).toUpperCase()}
                          </div>
                          <div>
                            <div className="flex items-center gap-1.5">
                              <span className="text-xs font-bold text-white leading-tight">
                                {user.name}
                              </span>
                              {isActive && (
                                <span className="text-[9px] font-extrabold uppercase px-1.5 py-0.2 rounded bg-sky-500/20 text-sky-400 border border-sky-500/30">
                                  Active
                                </span>
                              )}
                            </div>
                            <span className="text-[10px] text-slate-400 block">
                              {learnedCount} {learnedCount === 1 ? 'card' : 'cards'} marked learned
                            </span>
                          </div>
                        </div>

                        {/* Actions */}
                        <div className="flex items-center gap-1">
                          {isActive ? (
                            <span className="text-sky-400 p-1">
                              <UserCheck className="w-4 h-4" />
                            </span>
                          ) : (
                            <button
                              onClick={() => handleSelectUser(user.id)}
                              className="px-2 py-0.5 rounded text-[11px] font-semibold bg-slate-700 hover:bg-sky-600 text-slate-300 hover:text-white transition-colors"
                            >
                              Switch
                            </button>
                          )}

                          <button
                            onClick={() => handleStartRename(user)}
                            className="p-1 text-slate-400 hover:text-white hover:bg-slate-700/60 rounded transition-colors"
                            title="Rename learner"
                          >
                            <Edit3 className="w-3 h-3" />
                          </button>

                          {users.length > 1 && (
                            confirmDeleteId === user.id ? (
                              <div className="flex items-center gap-1 ml-1 bg-red-950/80 px-1 py-0.5 rounded border border-red-800">
                                <span className="text-[9px] text-red-300">Del?</span>
                                <button
                                  onClick={() => handleDeleteUser(user.id)}
                                  className="text-[10px] text-red-400 font-bold hover:underline"
                                >
                                  Yes
                                </button>
                                <button
                                  onClick={() => setConfirmDeleteId(null)}
                                  className="text-[10px] text-slate-400 hover:text-white"
                                >
                                  No
                                </button>
                              </div>
                            ) : (
                              <button
                                onClick={() => setConfirmDeleteId(user.id)}
                                className="p-1 text-slate-500 hover:text-red-400 hover:bg-red-500/10 rounded transition-colors"
                                title="Delete profile"
                              >
                                <Trash2 className="w-3 h-3" />
                              </button>
                            )
                          )}
                        </div>
                      </>
                    )}
                  </div>
                );
              })}
            </div>

            {/* Add New Profile Section */}
            {isAdding ? (
              <form onSubmit={handleCreateUser} className="mb-3 p-2.5 rounded-xl bg-slate-800/80 border border-slate-700">
                <label className="block text-[11px] font-semibold text-slate-300 mb-1.5">
                  New Learner Name
                </label>
                <div className="flex gap-2">
                  <input
                    type="text"
                    value={newUserName}
                    onChange={(e) => setNewUserName(e.target.value)}
                    placeholder="e.g. Maria, Jay..."
                    className="flex-1 bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1 text-xs text-white focus:outline-none focus:border-sky-500"
                    autoFocus
                  />
                  <button
                    type="submit"
                    className="px-3 py-1 bg-sky-500 hover:bg-sky-600 text-white rounded-lg text-xs font-semibold"
                  >
                    Add
                  </button>
                  <button
                    type="button"
                    onClick={() => {
                      setIsAdding(false);
                      setNewUserName('');
                    }}
                    className="px-2 py-1 bg-slate-700 hover:bg-slate-600 text-slate-300 rounded-lg text-xs"
                  >
                    Cancel
                  </button>
                </div>
              </form>
            ) : (
              <button
                onClick={() => setIsAdding(true)}
                className="w-full flex items-center justify-center gap-1.5 py-2 px-3 rounded-xl border border-dashed border-slate-700 hover:border-sky-500/60 text-xs font-semibold text-slate-300 hover:text-sky-300 hover:bg-sky-500/5 transition-all mb-3"
              >
                <UserPlus className="w-3.5 h-3.5" />
                <span>Add Learner Profile</span>
              </button>
            )}

            {/* Reset Active Profile Progress */}
            <div className="pt-2 border-t border-slate-800 flex items-center justify-between text-xs">
              {confirmReset ? (
                <div className="flex items-center justify-between w-full bg-red-950/60 p-2 rounded-xl border border-red-800/80">
                  <span className="text-[11px] text-red-200">Reset {activeUser.name}'s progress?</span>
                  <div className="flex items-center gap-2">
                    <button
                      onClick={handleResetProgress}
                      className="px-2 py-0.5 rounded bg-red-600 text-white font-bold text-[10px]"
                    >
                      Confirm
                    </button>
                    <button
                      onClick={() => setConfirmReset(false)}
                      className="px-2 py-0.5 rounded bg-slate-700 text-slate-300 text-[10px]"
                    >
                      Cancel
                    </button>
                  </div>
                </div>
              ) : (
                <button
                  onClick={() => setConfirmReset(true)}
                  className="flex items-center gap-1.5 text-[11px] text-slate-400 hover:text-red-400 transition-colors py-1"
                >
                  <RotateCcw className="w-3 h-3" />
                  <span>Reset {activeUser.name}'s Progress</span>
                </button>
              )}
            </div>
          </div>
        </>
      )}
    </div>
  );
};

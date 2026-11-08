import { useState, useEffect, useMemo } from 'react';
import { DeckData, Lesson } from '../types/schema';
import { getAllSRSData, isCardDue, getCardRatingStatus } from '../utils/srs';
import { getActiveUser } from '../utils/userStorage';
import { 
  Sparkles, 
  Clock, 
  Play, 
  CheckCircle, 
  Ban, 
  Repeat
} from 'lucide-react';

interface PracticeProps {
  deck: DeckData;
  onStartStudy: (
    cards: Lesson['entries'],
    title: string,
    lessonNotes?: string,
    lessonNumber?: string,
    options?: { hideExcluded?: boolean; hideLearned?: boolean },
    unitId?: string,
    lessonId?: string
  ) => void;
}

export const Practice: React.FC<PracticeProps> = ({ deck, onStartStudy }) => {
  const [activeUser, setActiveUser] = useState(getActiveUser());
  const [, setVersion] = useState(0);

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

  const { manifest, units } = deck;
  const allCards = useMemo(() => units.flatMap((u) => u.lessons.flatMap((l) => l.entries)), [units]);
  const srsMap = useMemo(() => getAllSRSData(activeUser.id), [activeUser.id]);

  const dueCards = useMemo(() => {
    return allCards.filter((c) => {
      const srs = srsMap[c.id];
      if (!srs) return true; // new card is due
      if (srs.isLearned || srs.isExcluded) return false;
      return isCardDue(srs);
    });
  }, [allCards, srsMap]);

  const againCards = useMemo(() => allCards.filter((c) => !srsMap[c.id]?.isExcluded && !srsMap[c.id]?.isLearned && getCardRatingStatus(srsMap[c.id]) === 'again'), [allCards, srsMap]);
  const hardCards = useMemo(() => allCards.filter((c) => !srsMap[c.id]?.isExcluded && !srsMap[c.id]?.isLearned && getCardRatingStatus(srsMap[c.id]) === 'hard'), [allCards, srsMap]);
  const goodCards = useMemo(() => allCards.filter((c) => !srsMap[c.id]?.isExcluded && !srsMap[c.id]?.isLearned && getCardRatingStatus(srsMap[c.id]) === 'good'), [allCards, srsMap]);
  const easyCards = useMemo(() => allCards.filter((c) => !srsMap[c.id]?.isExcluded && !srsMap[c.id]?.isLearned && getCardRatingStatus(srsMap[c.id]) === 'easy'), [allCards, srsMap]);
  const newCards = useMemo(() => allCards.filter((c) => !srsMap[c.id]?.isExcluded && !srsMap[c.id]?.isLearned && getCardRatingStatus(srsMap[c.id]) === 'new'), [allCards, srsMap]);
  const learnedCards = useMemo(() => allCards.filter((c) => srsMap[c.id]?.isLearned && !srsMap[c.id]?.isExcluded), [allCards, srsMap]);
  const ignoredCards = useMemo(() => allCards.filter((c) => srsMap[c.id]?.isExcluded && !srsMap[c.id]?.isLearned), [allCards, srsMap]);
  const totalPresentations = useMemo(() => {
    return allCards.reduce((acc, c) => acc + (srsMap[c.id]?.timesPresented || 0), 0);
  }, [allCards, srsMap]);
  const cardsPresentedCount = useMemo(() => {
    return allCards.filter((c) => (srsMap[c.id]?.timesPresented || 0) > 0).length;
  }, [allCards, srsMap]);

  return (
    <div className="space-y-6 max-w-6xl mx-auto pb-16 animate-in fade-in duration-200">
      {/* Top Banner with Quick Actions */}
      <div className="relative overflow-hidden rounded-3xl p-6 sm:p-8 bg-gradient-to-r from-amber-950/60 via-slate-900 to-sky-950/60 border border-amber-500/20 shadow-2xl">
        <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
          <div className="space-y-2">
            <div className="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-amber-500/15 border border-amber-500/30 text-amber-300 text-xs font-semibold">
              <Sparkles className="w-3.5 h-3.5 text-amber-400" />
              <span>Targeted Practice & Spaced Repetition (FSRS)</span>
            </div>
            <h1 className="text-2xl sm:text-3xl font-extrabold text-white tracking-tight">
              Targeted Vocabulary Drills
            </h1>
            <p className="text-slate-400 text-sm max-w-2xl leading-relaxed">
              Active learner: <span className="text-white font-semibold">{activeUser.name}</span> • <span className="text-sky-300 font-semibold">{totalPresentations} presentations</span> ({cardsPresentedCount} of {allCards.length} seen). Drill cards categorized by memory strength, review cards due for retention, or study the entire curriculum.
            </p>
          </div>

          <div className="flex flex-wrap items-center gap-3">
            {dueCards.length > 0 && (
              <button
                type="button"
                onClick={() => onStartStudy(dueCards, `${manifest.deck_title} • Due for Review`)}
                className="relative inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-bold text-sm shadow-lg shadow-amber-500/25 transition-all hover:scale-[1.02] active:scale-95"
              >
                <span className="w-2 h-2 rounded-full bg-slate-950 animate-ping absolute top-2 right-2" />
                <Clock className="w-4 h-4" /> Review Due ({dueCards.length})
              </button>
            )}
            <button
              type="button"
              onClick={() => onStartStudy(allCards, manifest.deck_title)}
              disabled={allCards.length === 0}
              className="inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-sky-500 hover:bg-sky-400 text-white font-semibold text-sm shadow-lg shadow-sky-500/25 transition-all hover:scale-[1.02] active:scale-95 disabled:opacity-50"
            >
              <Play className="w-4 h-4 fill-current" /> Study Entire Deck ({allCards.length})
            </button>
          </div>
        </div>
      </div>

      {/* Targeted Rating Drills Grid */}
      <div className="glass-panel p-5 sm:p-6 rounded-2xl border-slate-800 space-y-4">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-1.5 pb-2 border-b border-slate-800/80">
          <div className="flex items-center gap-2">
            <Repeat className="w-4 h-4 text-sky-400" />
            <h2 className="text-sm sm:text-base font-bold text-white tracking-wide uppercase">
              Filter by Memory Rating
            </h2>
          </div>
          <span className="text-xs text-slate-400">
            Select a bucket to start an instant focused drill
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
            onClick={() => onStartStudy(learnedCards, `${manifest.deck_title} • Already Learnt Cards`, undefined, undefined, { hideLearned: false, hideExcluded: true })}
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
              Mastered
            </div>
          </button>

          {/* Ignored Cards Button */}
          <button
            type="button"
            disabled={ignoredCards.length === 0}
            onClick={() => onStartStudy(ignoredCards, `${manifest.deck_title} • Ignored Cards`, undefined, undefined, { hideExcluded: false, hideLearned: true })}
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
              Ignored
            </div>
          </button>
        </div>
      </div>
    </div>
  );
};

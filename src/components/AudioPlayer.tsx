import { useRef, useState, useEffect, forwardRef, useImperativeHandle } from 'react';
import { Volume2, VolumeX, Play, Pause, RotateCcw } from 'lucide-react';

export interface AudioPlayerHandle {
  playAudio: () => void;
  pauseAudio: () => void;
  replayAudio: () => void;
}

interface AudioPlayerProps {
  src?: string | null;
  autoPlay?: boolean;
  label?: string;
  className?: string;
  mini?: boolean;
}

export const AudioPlayer = forwardRef<AudioPlayerHandle, AudioPlayerProps>(({
  src,
  autoPlay = false,
  label,
  className = '',
  mini = false,
}, ref) => {
  const audioRef = useRef<HTMLAudioElement | null>(null);
  const [isPlaying, setIsPlaying] = useState(false);
  const [hasError, setHasError] = useState(false);

  useImperativeHandle(ref, () => ({
    playAudio: () => {
      if (audioRef.current && src) {
        audioRef.current.currentTime = 0;
        audioRef.current.play().catch(() => setHasError(true));
      }
    },
    pauseAudio: () => {
      if (audioRef.current) {
        audioRef.current.pause();
      }
    },
    replayAudio: () => {
      if (audioRef.current && src) {
        audioRef.current.currentTime = 0;
        audioRef.current.play().catch(() => setHasError(true));
      }
    },
  }));

  useEffect(() => {
    setIsPlaying(false);
    setHasError(false);
    if (src && autoPlay && audioRef.current) {
      audioRef.current.play().catch(() => {
        // Autoplay policy silent catch
      });
    }
  }, [src, autoPlay]);

  if (!src) {
    return (
      <span className="inline-flex items-center gap-1.5 text-xs text-slate-500 italic py-1 px-2.5 rounded-lg bg-slate-800/40 border border-slate-700/50">
        <VolumeX className="w-3.5 h-3.5 text-slate-500" /> No audio
      </span>
    );
  }

  const togglePlay = () => {
    if (!audioRef.current) return;
    if (isPlaying) {
      audioRef.current.pause();
    } else {
      audioRef.current.currentTime = 0;
      audioRef.current.play().catch(() => setHasError(true));
    }
  };

  const handleEnded = () => setIsPlaying(false);
  const handlePause = () => setIsPlaying(false);
  const handlePlay = () => setIsPlaying(true);

  if (mini) {
    return (
      <div className={`inline-flex items-center ${className}`}>
        <audio
          ref={audioRef}
          src={src}
          onEnded={handleEnded}
          onPause={handlePause}
          onPlay={handlePlay}
          onError={() => setHasError(true)}
          preload="auto"
        />
        <button
          type="button"
          onClick={togglePlay}
          title="Play Native Audio (↓)"
          className={`p-2 rounded-xl transition-all duration-200 ${
            isPlaying
              ? 'bg-sky-500 text-white shadow-lg shadow-sky-500/30 scale-105'
              : 'bg-slate-800 text-sky-400 hover:bg-slate-700 hover:text-sky-300 border border-slate-700'
          }`}
        >
          {isPlaying ? <Pause className="w-4 h-4" /> : <Volume2 className="w-4 h-4" />}
        </button>
      </div>
    );
  }

  return (
    <div className={`flex items-center gap-2 px-3 py-1.5 rounded-xl bg-slate-800/80 border border-sky-500/20 shadow-sm ${className}`}>
      <audio
        ref={audioRef}
        src={src}
        onEnded={handleEnded}
        onPause={handlePause}
        onPlay={handlePlay}
        onError={() => setHasError(true)}
        preload="auto"
      />
      <button
        type="button"
        onClick={togglePlay}
        className={`w-8 h-8 rounded-lg flex items-center justify-center transition-all ${
          isPlaying
            ? 'bg-sky-500 text-white shadow-md shadow-sky-500/40'
            : 'bg-slate-700 text-sky-400 hover:bg-slate-600'
        }`}
      >
        {isPlaying ? <Pause className="w-4 h-4" /> : <Play className="w-4 h-4 ml-0.5" />}
      </button>

      <button
        type="button"
        onClick={() => {
          if (audioRef.current) {
            audioRef.current.currentTime = 0;
            audioRef.current.play();
          }
        }}
        className="p-1.5 text-slate-400 hover:text-slate-200 rounded-lg hover:bg-slate-700/50"
        title="Replay from start (↓)"
      >
        <RotateCcw className="w-3.5 h-3.5" />
      </button>

      {label && (
        <span className="text-xs font-medium text-slate-300 truncate max-w-[140px]">
          {label}
        </span>
      )}

      {hasError && (
        <span className="text-xs text-rose-400 ml-auto">Audio load error</span>
      )}
    </div>
  );
});

AudioPlayer.displayName = 'AudioPlayer';

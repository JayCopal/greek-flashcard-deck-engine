# Greek Flashcard Deck Engine & Audio Asset Builder (Local-First PWA)

A local-first, single-user authoring workstation and study engine for Modern Greek. Built with **FastAPI (Python)**, **React (Vite + Tailwind CSS)**, and **Google Cloud Text-to-Speech Chirp 3 HD**.

---

## Highlights

- **Local YAML as Single Source of Truth:** All cards, lessons, and metadata live in human-readable YAML files in `content/`. Zero database bloat.
- **Authentic Google Cloud Chirp-3 HD Greek Audio:**
  - `el-GR-Chirp3-HD-Leda` (Default female examiner voice - maximum articulation)
  - `el-GR-Chirp3-HD-Charon` (Deep, natural Greek male voice)
  - `el-GR-Chirp3-HD-Puck` (Expressive conversational male voice)
  - `el-GR-Chirp3-HD-Aoede` (Melodic gentle female voice)
- **"Listen, Accept or Reject" Review Pipeline:** Preview pronunciation in-memory before committing. Green "Accept" writes the deterministic MP3 file and updates the YAML. Red "Reject" discards the audio buffer and reveals an inline editor to adjust Greek spelling or *tonos* accents.
- **Deterministic Audio Slug Strategy:** Greek text is transliterated to clean Latin slugs with a SHA-256 Unicode hash (e.g. `kalimera-2490ee.mp3`), ensuring portable, collision-free assets.
- **Interactive Flashcard Drilling Mode:** 3D perspective flip cards with keyboard shortcuts (`Space` to flip, `ArrowLeft`/`ArrowRight` to navigate, auto-play audio).
- **Multi-User Local Storage:** Card markings, SRS intervals, review history, and lesson completion status are isolated per learner profile in `localStorage`. Switch learners, create new profiles, or reset progress at any time without server dependencies.
- **One-Click Static Mobile PWA & WebAPK Installation:** `npm run export:pwa` bundles everything into `dist-pwa/` with high-resolution adaptive/maskable icons and a Service Worker. Works 100% offline on iOS and Android with full native WebAPK installation support on Android Chrome.

---

## Quick Start

### 1. Requirements
- Python 3.10+
- Node.js 18+ & npm
- Google Cloud service account credentials file (`gcp_credentials.json`)

### 2. Start Local Development

In terminal 1 (FastAPI backend):
```powershell
python -m uvicorn server.main:app --reload --port 8000
```

In terminal 2 (Vite frontend):
```powershell
npm run dev
```
Open **http://localhost:5173** in your browser.

### 3. Curriculum & Audio Commands

- **Sync Curriculum Batches to YAML (SSOT):**
  ```powershell
  npm run sync:curriculum
  ```
- **Batch Generate Chirp-3 HD Audio for Pending Cards:**
  ```powershell
  npm run audio:generate
  ```
- **Authoring & Audio Guides:**
  - [docs/LESSON_CREATION_GUIDE.md](file:///c:/jay-programs/greek-flashcard-deck-engine/docs/LESSON_CREATION_GUIDE.md): Full YAML schema definitions, validation rules, and lesson authoring workflows.
  - [docs/AUDIO_GENERATION_GUIDE.md](file:///c:/jay-programs/greek-flashcard-deck-engine/docs/AUDIO_GENERATION_GUIDE.md): Chirp-3 HD audio pipeline specifications, deterministic slug hashing, and AI agent execution protocols.

---

## Project Structure

```
greek-flashcard-deck-engine/
├── content/                    # Source of truth (YAML)
│   ├── manifest.yaml           # Deck title, units, lesson order
│   ├── unit-01/
│   │   ├── lesson-01.yaml      # Greetings & Polite Phrases
│   │   └── lesson-02.yaml      # Essential Questions
│   └── unit-02/
│       └── lesson-01.yaml      # Ordering at the Kafeneio
├── audio/                      # Permanent vetted MP3 audio assets
│   └── kalimera-2490ee.mp3
├── server/                     # Python FastAPI backend
│   ├── main.py                 # REST API & static audio mount
│   ├── tts_service.py          # Google Cloud Chirp 3 integration
│   └── requirements.txt
├── src/                        # Vite + React + Tailwind frontend
│   ├── components/
│   │   ├── Dashboard.tsx       # Metrics, progress rollups & PWA export trigger
│   │   ├── DeckEditor.tsx      # In-memory TTS preview, Accept/Reject & Card editor
│   │   ├── StudySession.tsx    # 3D interactive flashcard drill
│   │   └── AudioPlayer.tsx     # Custom audio player & waveform preview
│   ├── types/
│   │   └── schema.ts           # TypeScript interfaces matching YAML
│   ├── App.tsx
│   └── main.tsx
├── scripts/
│   └── export_pwa.py           # Compiles deck.json + copies audio to dist-pwa/
├── dist-pwa/                   # Exported static mobile PWA bundle
└── package.json
```

---

## Exporting for Mobile (Offline PWA)

To generate the standalone zero-server PWA bundle:
```powershell
npm run export:pwa
```
This produces the self-contained `dist-pwa/` folder containing:
1. `dist-pwa/data/deck.json` (compiled deck)
2. `dist-pwa/audio/*.mp3` (all verified audio files)
3. Service Worker & Web Manifest pre-caching all assets

You can test it locally with:
```powershell
npx serve dist-pwa
```
Or host it on Cloudflare Pages, GitHub Pages, or a local network share. On mobile, navigate to the URL and tap **"Add to Home Screen"** for a fully offline Greek learning experience!

# AI Agent Audio Generation Guide (Chirp-3 HD Pipeline)

This guide provides technical specifications, code patterns, and execution protocols for **AI agents** (and developers) responsible for generating Modern Greek audio assets in the **Greek Flashcard Deck Engine**.

---

## 1. Cardinal Directives (System Invariants)

1. **Strictly Chirp-3 HD — NO FALLBACKS:**
   All Greek audio assets **must** be synthesized using **Google Cloud TTS Chirp 3 HD** (`el-GR-Chirp3-HD-Leda`).
   > [!CAUTION]
   > Do **NOT** use `Standard`, `Wavenet`, or `Neural2` Greek voices. If Chirp-3 fails or credentials are missing, the script must fail fast with an informative error rather than falling back to robotic voices.

2. **Deterministic File Naming:**
   Audio files must **never** be named arbitrarily. Every filename is derived deterministically from the Greek text using a Latin slug and a SHA-256 hash.

3. **Single Source of Truth (YAML):**
   Audio generation must operate directly on the YAML lesson files (`content/unit-XX/lesson-YY.yaml`) referenced in `content/manifest.yaml`.

---

## 2. Environment & Authentication Setup

### 2.1 Credentials & Environment Variables
* The Google Cloud service account JSON file is located at the workspace root: `gcp_credentials.json`.
* The environment variable `GOOGLE_APPLICATION_CREDENTIALS` must resolve to this file.
* Default configuration in `.env`:
  ```ini
  GOOGLE_APPLICATION_CREDENTIALS=gcp_credentials.json
  DEFAULT_VOICE=el-GR-Chirp3-HD-Leda
  PORT=8000
  ```

### 2.2 Audio Synthesis Specifications
| Parameter | Value | Reason |
|---|---|---|
| **Voice Model** | `el-GR-Chirp3-HD-Leda` | Authentic Greek female examiner voice with clear phonological articulation |
| **Language Code** | `el-GR` | Modern Greek |
| **Audio Encoding** | `MP3` (`AudioEncoding.MP3`) | Maximum cross-platform browser and mobile compatibility |
| **Speaking Rate** | `0.95` | Slightly slower than native conversational tempo to facilitate learner listening comprehension |
| **Sample Rate** | `24000 Hz` (`24 kHz`) | High-definition clarity for Greek sibilants and velar stops |
| **Rate Limit Delay** | `0.15s` per request | Prevents GCP quota throttling on large batches |

---

## 3. Deterministic Filename Generation Algorithm

To avoid duplicate files and maintain portable references across environments, filenames use a slug + Unicode SHA-256 hash:

```python
import hashlib
import unicodedata
import re

# Greek to Latin transliteration table
TRANSLIT_TABLE = {
    'α': 'a', 'ά': 'a', 'β': 'v', 'γ': 'g', 'δ': 'd',
    'ε': 'e', 'έ': 'e', 'ζ': 'z', 'η': 'i', 'ή': 'i',
    'θ': 'th', 'ι': 'i', 'ί': 'i', 'ϊ': 'i', 'ΐ': 'i',
    'κ': 'k', 'λ': 'l', 'μ': 'm', 'ν': 'n', 'ξ': 'x',
    'ο': 'o', 'ό': 'o', 'π': 'p', 'ρ': 'r', 'σ': 's',
    'ς': 's', 'τ': 't', 'υ': 'y', 'ύ': 'y', 'ϋ': 'y',
    'ΰ': 'y', 'φ': 'f', 'χ': 'ch', 'ψ': 'ps', 'ω': 'o',
    'ώ': 'o'
}

def generate_audio_filename(greek_text: str) -> str:
    """Generates a deterministic filename: <transliterated-slug>-<sha256:6>.mp3"""
    normalized = unicodedata.normalize("NFC", greek_text.strip().lower())
    
    # Transliterate to Latin
    slug = "".join(TRANSLIT_TABLE.get(char, char) for char in normalized)
    slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')[:20] or "greek"
    
    # Hash the original normalized Unicode text (preserving tones)
    text_hash = hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:6]
    return f"{slug}-{text_hash}.mp3"
```

*Example:*
- `"ο καφές"` $\rightarrow$ `o-kafes-733951.mp3`
- `"το νερό"` $\rightarrow$ `to-nero-743b44.mp3`

---

## 4. AI Agent Execution Protocols

### Protocol A: Command-Line Generation (Standard)

When an agent needs to synthesize audio for newly added cards, use the dedicated CLI tool:

```powershell
# Synthesize all ungenerated / pending cards across the entire deck
npm run audio:generate

# Or directly via Python with specific targets:
python scripts/generate_audio_assets.py --unit unit-05
python scripts/generate_audio_assets.py --file content/unit-05/lesson-01.yaml

# Force re-generation of existing files (e.g. after correcting Greek text):
python scripts/generate_audio_assets.py --unit unit-05 --force
```

### Protocol B: Programmatic Generation (In Custom Subagent Scripts)

When building an autonomous script that generates content and synthesizes audio simultaneously:

```python
# -*- coding: utf-8 -*-
import sys
import time
import unicodedata
from pathlib import Path
import yaml
from google.cloud import texttospeech
from server.tts_service import generate_audio_filename

# 1. Windows console encoding safety
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

client = texttospeech.TextToSpeechClient()

def synthesize_and_save(greek_text: str, audio_dir: Path) -> str:
    filename = generate_audio_filename(greek_text)
    out_path = audio_dir / filename
    
    # Idempotent skip if file already exists
    if out_path.exists() and out_path.stat().st_size > 0:
        return filename

    normalized = unicodedata.normalize("NFC", greek_text.strip())
    response = client.synthesize_speech(
        input=texttospeech.SynthesisInput(text=normalized),
        voice=texttospeech.VoiceSelectionParams(
            language_code="el-GR",
            name="el-GR-Chirp3-HD-Leda"
        ),
        audio_config=texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=0.95,
            sample_rate_hertz=24000
        )
    )
    
    if not response.audio_content:
        raise RuntimeError(f"Chirp-3 returned empty audio for: {greek_text}")

    with open(out_path, "wb") as f:
        f.write(response.audio_content)

    # Respect GCP rate limits
    time.sleep(0.15)
    return filename
```

---

## 5. Post-Generation Verification & Export Protocol

Every audio generation task executed by an agent must complete the following 3-step verification:

### 1. Integrity Verification Pass
Check that every entry in the YAML file has a matching physical `.mp3` file on disk:
```python
missing = []
for entry in lesson_data["entries"]:
    expected = entry.get("audio")
    if not expected or not (AUDIO_DIR / expected).exists():
        missing.append(entry["id"])
if missing:
    raise RuntimeError(f"Audio generation incomplete! Missing: {missing}")
```

### 2. Update Entry Status
Set `entry["status"] = "verified"` and `entry["audio"] = filename`. Write the modified dictionary back to the lesson YAML file.

### 3. Synchronize PWA & Offline Bundles
Run the PWA exporter to bundle the new audio files into `dist-pwa/audio/` and update `public/data/deck.json`:
```powershell
npm run export:pwa
```

---

## 6. Common Pitfalls & Agent Troubleshooting

| Symptom | Cause | Solution |
|---|---|---|
| `UnicodeEncodeError: 'charmap' codec can't encode characters` | Windows console defaults to legacy CP1252 | Add `if sys.platform == "win32": sys.stdout.reconfigure(encoding="utf-8")` at the very start of your script. |
| `DefaultCredentialsError` | `gcp_credentials.json` not found or path relative | Ensure `GOOGLE_APPLICATION_CREDENTIALS` resolves to an absolute path pointing to `gcp_credentials.json`. |
| `ResourceExhausted: 429 Quota exceeded` | Too many requests in rapid succession | Increase `time.sleep(0.15)` delay between calls to `0.25` or implement exponential backoff. |
| Audio file exists but size is 0 bytes | Truncated write or network disconnect | Always check `stat().st_size > 0`. Delete zero-byte files and re-synthesize. |
| App shows `pending_tts` despite audio file existing | `audio` filename in YAML does not match file on disk | Run `npm run audio:generate` to auto-repair filenames and statuses across all YAML files. |

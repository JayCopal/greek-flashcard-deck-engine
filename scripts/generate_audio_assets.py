# -*- coding: utf-8 -*-
"""
Generate audio assets for Greek flashcards using Google Cloud TTS Chirp 3 HD.
Strictly ONLY Google Chirp-3 voice (el-GR-Chirp3-HD-Leda), with NO fallbacks.
Single Source of Truth (SSOT): Reads and writes directly to content/ (*.yaml).
"""
import os
import sys
import time
import argparse
import unicodedata
from pathlib import Path
import yaml

# Set UTF-8 encoding on Windows console
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from dotenv import load_dotenv
load_dotenv(BASE_DIR / ".env")

# Ensure credentials exist
creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "gcp_credentials.json")
if not os.path.isabs(creds_path):
    creds_path = str(BASE_DIR / creds_path)

if not os.path.exists(creds_path):
    raise FileNotFoundError(f"GCP credentials file not found at: {creds_path}")

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = creds_path

try:
    from google.cloud import texttospeech
except ImportError:
    raise ImportError("google-cloud-texttospeech is required. Install with: pip install google-cloud-texttospeech")

from server.tts_service import generate_audio_filename

CHIRP_VOICE = os.getenv("DEFAULT_VOICE", "el-GR-Chirp3-HD-Leda")
if "chirp" not in CHIRP_VOICE.lower():
    raise ValueError(f"CRITICAL: Non-Chirp voice requested ({CHIRP_VOICE}). Strictly Chirp-3 is required.")

SPEAKING_RATE = 0.9
SAMPLE_RATE_HERTZ = 24000
CONTENT_DIR = BASE_DIR / "content"
AUDIO_DIR = BASE_DIR / "audio"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"


def synthesize_chirp3(client: texttospeech.TextToSpeechClient, text: str) -> bytes:
    """Synthesizes speech using Google Cloud TTS Chirp 3 HD. NO FALLBACK."""
    normalized_text = unicodedata.normalize("NFC", text.strip())
    synthesis_input = texttospeech.SynthesisInput(text=normalized_text)
    voice = texttospeech.VoiceSelectionParams(
        language_code="el-GR",
        name=CHIRP_VOICE,
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=SPEAKING_RATE,
        sample_rate_hertz=SAMPLE_RATE_HERTZ,
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config,
    )

    if not response.audio_content:
        raise RuntimeError(f"Chirp-3 returned empty audio content for text: {text}")

    return response.audio_content


def process_lesson_yaml(client: texttospeech.TextToSpeechClient, yaml_path: Path, force: bool = False):
    """Processes a lesson YAML file, generating missing or pending audio."""
    if not yaml_path.exists():
        print(f"Warning: Lesson file not found: {yaml_path}")
        return 0, 0, 0

    with open(yaml_path, "r", encoding="utf-8") as f:
        lesson_data = yaml.safe_load(f) or {}

    entries = lesson_data.get("entries", [])
    if not entries:
        return 0, 0, 0

    unit_id = lesson_data.get("unit_id", yaml_path.parent.name)
    lesson_id = lesson_data.get("lesson_id", yaml_path.stem)
    print(f"\n--- Checking {unit_id} / {lesson_id} ({len(entries)} entries) ---")

    modified = False
    generated_count = 0
    total_bytes = 0
    already_verified = 0

    for i, entry in enumerate(entries, start=1):
        card_id = entry.get("id", f"entry-{i}")
        greek_text = entry.get("greek") or entry.get("front", "")
        if not greek_text:
            continue

        existing_audio = entry.get("audio")
        expected_filename = existing_audio or generate_audio_filename(greek_text)
        out_path = AUDIO_DIR / expected_filename

        # Check if physically exists and non-empty
        physically_exists = out_path.exists() and out_path.stat().st_size > 0

        if physically_exists and not force:
            already_verified += 1
            if entry.get("status") != "verified" or entry.get("audio") != expected_filename:
                entry["audio"] = expected_filename
                entry["status"] = "verified"
                modified = True
            continue

        print(f"  [{i:02d}/{len(entries)}] Synthesizing {card_id} ('{greek_text}') -> {expected_filename} ...", end=" ", flush=True)

        try:
            audio_bytes = synthesize_chirp3(client, greek_text)
            with open(out_path, "wb") as f:
                f.write(audio_bytes)
            byte_len = len(audio_bytes)
            total_bytes += byte_len
            generated_count += 1

            entry["audio"] = expected_filename
            entry["status"] = "verified"
            modified = True
            print(f"DONE ({byte_len:,} bytes)")
        except Exception as e:
            print(f"FAILED: {e}")
            raise e

        # Polite delay to respect GCP API rate limits
        time.sleep(0.15)

    if modified:
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(lesson_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        print(f"  [SAVED] Updated YAML file: {yaml_path}")

    return generated_count, total_bytes, already_verified


def main():
    parser = argparse.ArgumentParser(description="Chirp-3 HD Audio Generator for Greek Flashcards (SSOT YAML)")
    parser.add_argument("--unit", type=str, help="Filter by unit ID (e.g., unit-03)")
    parser.add_argument("--file", type=str, help="Process a specific YAML lesson file")
    parser.add_argument("--force", action="store_true", help="Force re-generation of existing audio files")
    parser.add_argument("--skip-export", action="store_true", help="Skip running export_pwa.py after generation")
    args = parser.parse_args()

    print("=" * 70)
    print("Greek Flashcard Audio Generator: Google Cloud TTS Chirp-3 HD")
    print(f"Voice:         {CHIRP_VOICE} (Strictly Chirp-3, No Fallbacks)")
    print(f"Speaking Rate: {SPEAKING_RATE}")
    print(f"Sample Rate:   {SAMPLE_RATE_HERTZ} Hz")
    print(f"Audio Output:  {AUDIO_DIR}")
    print(f"Source:        YAML SSOT ({MANIFEST_PATH.name})")
    print("=" * 70)

    client = texttospeech.TextToSpeechClient()
    print("Google Cloud TTS client initialized successfully.")

    if not MANIFEST_PATH.exists():
        raise FileNotFoundError(f"Manifest not found: {MANIFEST_PATH}")

    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f) or {}

    units = manifest.get("units", [])
    target_files = []

    if args.file:
        target_files.append(Path(args.file).resolve())
    else:
        for u in units:
            if args.unit and u.get("id") != args.unit:
                continue
            for les in u.get("lessons", []):
                rel_file = les.get("file")
                if rel_file:
                    target_files.append(CONTENT_DIR / rel_file)

    print(f"Target lesson files to inspect: {len(target_files)}")

    total_generated = 0
    total_bytes = 0
    total_existing = 0
    start_time = time.time()

    for yaml_path in target_files:
        gen, b, exist = process_lesson_yaml(client, yaml_path, force=args.force)
        total_generated += gen
        total_bytes += b
        total_existing += exist

    elapsed = time.time() - start_time
    print("\n" + "=" * 70)
    print(f"Audio Processing Complete in {elapsed:.1f}s!")
    print(f"Newly synthesized: {total_generated} audio files (~{total_bytes / 1024:.1f} KB).")
    print(f"Already verified:  {total_existing} audio files.")
    print("=" * 70)

    # Automatically run export_pwa unless skipped
    if not args.skip_export and (total_generated > 0 or not (BASE_DIR / "dist-pwa" / "data" / "deck.json").exists()):
        print("\n==> Automatically refreshing static PWA export bundle...")
        from scripts.export_pwa import export
        export()


if __name__ == "__main__":
    main()

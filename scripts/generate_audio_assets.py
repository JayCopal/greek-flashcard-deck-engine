# -*- coding: utf-8 -*-
"""
Generate audio assets for Greek flashcards using Google Cloud TTS Chirp 3 HD.
Strictly ONLY Google Chirp-3 voice (el-GR-Chirp3-HD-Leda), with NO fallbacks.
"""
import os
import sys
import time
import json
import unicodedata
from pathlib import Path

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

SPEAKING_RATE = 0.95
SAMPLE_RATE_HERTZ = 24000
AUDIO_DIR = BASE_DIR / "audio"
AUDIO_DIR.mkdir(parents=True, exist_ok=True)


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


def main():
    if len(sys.argv) > 1:
        target_json = Path(sys.argv[1])
        if not target_json.is_absolute():
            target_json = BASE_DIR / target_json
    else:
        target_json = BASE_DIR / "content" / "keg_a1_units_03_04.json"

    print("=" * 70)
    print("Greek Flashcard Audio Generator: Google Cloud TTS Chirp-3 HD")
    print(f"Voice:         {CHIRP_VOICE} (Strictly Chirp-3, No Fallbacks)")
    print(f"Speaking Rate: {SPEAKING_RATE}")
    print(f"Sample Rate:   {SAMPLE_RATE_HERTZ} Hz")
    print(f"Audio Output:  {AUDIO_DIR}")
    print(f"Input JSON:    {target_json}")
    print("=" * 70)

    if not target_json.exists():
        raise FileNotFoundError(f"Input JSON not found: {target_json}")

    with open(target_json, "r", encoding="utf-8") as f:
        cards = json.load(f)

    unit_counts = {}
    for c in cards:
        u = c.get("unit_number", 0)
        unit_counts[u] = unit_counts.get(u, 0) + 1

    unit_summary = ", ".join(f"Unit {u}: {cnt} cards" for u, cnt in sorted(unit_counts.items()))
    print(f"Loaded {len(cards)} cards total ({unit_summary}).")

    client = texttospeech.TextToSpeechClient()
    print("Google Cloud TTS client initialized successfully.")

    success_count = 0
    total_bytes = 0
    total_cards = len(cards)
    start_time = time.time()

    for i, card in enumerate(cards, start=1):
        card_id = card["id"]
        front_text = card["front"]
        filename = generate_audio_filename(front_text)
        out_path = AUDIO_DIR / filename

        print(f"[{i:02d}/{total_cards}] Synthesizing {card_id} ('{front_text}') -> {filename} ...", end=" ", flush=True)

        try:
            audio_bytes = synthesize_chirp3(client, front_text)
            with open(out_path, "wb") as f:
                f.write(audio_bytes)
            byte_len = len(audio_bytes)
            total_bytes += byte_len
            success_count += 1

            # Attach audio metadata to card
            card["audio"] = filename
            card["audio_status"] = "verified"

            print(f"DONE ({byte_len:,} bytes)")
        except Exception as e:
            print(f"FAILED: {e}")
            raise e

        # Polite delay to respect GCP API rate limits
        time.sleep(0.15)

    elapsed = time.time() - start_time
    print("-" * 70)
    print(f"Audio Generation Complete in {elapsed:.1f}s!")
    print(f"Successfully generated: {success_count}/{total_cards} audio files.")
    print(f"Total audio data written: {total_bytes:,} bytes (~{total_bytes / 1024:.1f} KB).")

    # Save updated cards JSON with audio references
    with open(target_json, "w", encoding="utf-8") as f:
        json.dump(cards, f, ensure_ascii=False, indent=2)
    print(f"Updated {target_json} with 'audio' and 'audio_status' properties.")

    # Verification pass: check every file exists and has size > 0
    missing = []
    empty = []
    for c in cards:
        expected_file = AUDIO_DIR / c["audio"]
        if not expected_file.exists():
            missing.append(c["id"])
        elif expected_file.stat().st_size == 0:
            empty.append(c["id"])

    if missing or empty:
        print(f"VERIFICATION FAILED! Missing: {missing}, Empty: {empty}")
        sys.exit(1)
    else:
        print(f"[VERIFIED] All {total_cards} audio assets physically exist in audio/ and are non-empty.")


if __name__ == "__main__":
    main()

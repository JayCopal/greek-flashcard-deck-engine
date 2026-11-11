# -*- coding: utf-8 -*-
"""
Verify audio assets for all KEG-A2 Part 2 units (unit-a2p2-01 through unit-a2p2-12).
If any audio files are missing, synthesize them via Chirp 3 HD.
"""
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from server.tts_service import synthesize_greek_chirp, generate_audio_filename

AUDIO_DIR = BASE_DIR / "audio"
CONTENT_DIR = BASE_DIR / "content"

def main():
    total_cards = 0
    total_audio_refs = 0
    missing_audio = []

    print("Verifying audio assets across all Part 2 units...")
    for u_idx in range(1, 13):
        unit_id = f"unit-a2p2-{u_idx:02d}"
        lesson_file = CONTENT_DIR / unit_id / "lesson-01.yaml"
        if not lesson_file.exists():
            print(f"  [MISSING UNIT] {lesson_file}")
            continue

        with open(lesson_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
            
        entries = data.get("entries", [])
        total_cards += len(entries)
        
        for card in entries:
            for key, el_key in [("audio", "greek"), ("example_audio", "example_el"), ("example2_audio", "example2_el")]:
                fn = card.get(key)
                text = card.get(el_key)
                if fn and text:
                    total_audio_refs += 1
                    fpath = AUDIO_DIR / fn
                    if not fpath.exists() or fpath.stat().st_size == 0:
                        missing_audio.append((text, fn, unit_id, card.get("id")))

    print(f"Total Part 2 Units checked: 12")
    print(f"Total Part 2 Cards: {total_cards}")
    print(f"Total Audio References: {total_audio_refs}")
    print(f"Missing / 0-byte Audio Files: {len(missing_audio)}")

    if missing_audio:
        print("\nSynthesizing missing audio files now...")
        for text, fn, u_id, c_id in missing_audio:
            print(f"  Synthesizing [{c_id}]: {text[:35]} -> {fn}")
            try:
                audio_bytes = synthesize_greek_chirp(text)
                out_path = AUDIO_DIR / fn
                with open(out_path, "wb") as f:
                    f.write(audio_bytes)
                print(f"    [OK] Saved ({len(audio_bytes)} bytes)")
            except Exception as e:
                print(f"    [FAIL] {e}")

    # Re-verify
    still_missing = 0
    for u_idx in range(1, 13):
        unit_id = f"unit-a2p2-{u_idx:02d}"
        lesson_file = CONTENT_DIR / unit_id / "lesson-01.yaml"
        with open(lesson_file, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)
        for card in data.get("entries", []):
            for key in ["audio", "example_audio", "example2_audio"]:
                fn = card.get(key)
                if fn:
                    fpath = AUDIO_DIR / fn
                    if not fpath.exists() or fpath.stat().st_size == 0:
                        still_missing += 1

    if still_missing == 0:
        print(f"\n[VERIFIED 100%] All {total_cards} cards and {total_audio_refs} audio files in Part 2 are present and valid!")
    else:
        print(f"\n[WARNING] {still_missing} audio files are still missing.")

if __name__ == "__main__":
    main()

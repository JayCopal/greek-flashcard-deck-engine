# -*- coding: utf-8 -*-
import sys
import yaml
import time
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from server.tts_service import synthesize_greek_chirp

audio_dir = BASE_DIR / "audio"
content_dir = BASE_DIR / "content"

# 1. Part 1: unit-a2-00 to unit-a2-12
p1_units = [f"unit-a2-{u:02d}" for u in range(13)]
# 2. Part 2: unit-a2p2-01 to unit-a2p2-12
p2_units = [f"unit-a2p2-{u:02d}" for u in range(1, 13)]

all_units = p1_units + p2_units
print(f"Auditing {len(all_units)} A2 units across Part 1 & Part 2...")

missing = 0
fixed = 0
total_cards = 0

def heal_audio_with_retry(text: str, path: Path, max_retries: int = 4) -> bool:
    for attempt in range(max_retries):
        try:
            time.sleep(1.2 * (attempt + 1))  # Progressive backoff
            b = synthesize_greek_chirp(text)
            with open(path, "wb") as f_out:
                f_out.write(b)
            return True
        except Exception as e:
            print(f"    [Retry {attempt+1}/{max_retries}] Error: {e}")
            time.sleep(3)
    return False

for uid in all_units:
    yp = content_dir / uid / "lesson-01.yaml"
    if not yp.exists():
        print(f"[MISSING UNIT YAML] {yp}")
        continue
    with open(yp, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    
    entries = data.get("entries", [])
    total_cards += len(entries)
    
    unit_missing = 0
    for c in entries:
        cid = c.get("id", "unknown")
        for field, audio_key in [("greek", "audio"), ("example_el", "example_audio"), ("example2_el", "example2_audio")]:
            fn = c.get(audio_key)
            if fn:
                p = audio_dir / fn
                if not p.exists() or p.stat().st_size == 0:
                    unit_missing += 1
                    missing += 1
                    txt = c.get(field)
                    print(f"  [MISSING AUDIO] {cid} {field}: {fn} ('{txt}')")
                    if txt:
                        success = heal_audio_with_retry(txt, p)
                        if success:
                            fixed += 1
                            print(f"    -> FIXED {fn} ({p.stat().st_size} bytes)")
                        else:
                            print(f"    -> FAILED TO FIX {fn}")
            else:
                print(f"  [NO AUDIO KEY] {cid} missing key {audio_key}")
                
    if unit_missing == 0:
        print(f"  [OK] {uid}: {len(entries)} cards, all audio verified 100%.")

print(f"\n==========================================")
print(f"Total A2 Cards audited: {total_cards}")
print(f"Missing audio detected: {missing}")
print(f"Missing audio healed: {fixed}")
print(f"==========================================")

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
missing = 0
fixed = 0

for u in range(13):
    uid = f"unit-a2-{u:02d}"
    yp = BASE_DIR / "content" / uid / "lesson-01.yaml"
    if not yp.exists():
        continue
    with open(yp, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    for c in data.get("entries", []):
        cid = c.get("id", "unknown")
        for field, audio_key in [("greek", "audio"), ("example_el", "example_audio"), ("example2_el", "example2_audio")]:
            fn = c.get(audio_key)
            if fn:
                p = audio_dir / fn
                if not p.exists() or p.stat().st_size == 0:
                    missing += 1
                    txt = c.get(field)
                    print(f"[MISSING] {cid} {field}: {fn} ('{txt}')")
                    if txt:
                        try:
                            time.sleep(1) # polite backoff
                            b = synthesize_greek_chirp(txt)
                            with open(p, "wb") as f_out:
                                f_out.write(b)
                            fixed += 1
                            print(f"  -> FIXED {fn} ({len(b)} bytes)")
                        except Exception as e:
                            print(f"  -> ERROR fixing {fn}: {e}")

print(f"\nAudit complete: Missing detected: {missing}, Fixed: {fixed}")

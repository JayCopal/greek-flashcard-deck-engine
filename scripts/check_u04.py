# -*- coding: utf-8 -*-
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent

yp = BASE_DIR / "content" / "unit-04" / "lesson-01.yaml"
with open(yp, "r", encoding="utf-8") as f:
    yd = yaml.safe_load(f)
print(f"\n=== unit-04: {yd.get('title')} ({len(yd.get('entries', []))} cards) ===")
for e in yd.get("entries", []):
    print(f"  {e['id']} | {e['greek']} ({e['english']})")

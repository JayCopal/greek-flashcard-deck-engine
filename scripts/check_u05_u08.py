# -*- coding: utf-8 -*-
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent

for uid in ["unit-05", "unit-06", "unit-07", "unit-08"]:
    yp = BASE_DIR / "content" / uid / "lesson-01.yaml"
    with open(yp, "r", encoding="utf-8") as f:
        yd = yaml.safe_load(f)
    print(f"\n=== {uid} ===")
    for e in yd.get("entries", []):
        print(f"  {e['id']} | {e['greek']} ({e['english']})")

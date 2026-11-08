# -*- coding: utf-8 -*-
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
MANIFEST_PATH = BASE_DIR / "content" / "manifest.yaml"

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = yaml.safe_load(f)

search_terms = ["ευρώ", "λεπτό", "φτηνός", "φθηνός", "ενοικιάζεται", "πωλείται", "μπάνιο"]

print("Searching across all units in manifest:")
for u in manifest.get("units", []):
    uid = u["id"]
    rel = u["lessons"][0]["file"]
    yp = BASE_DIR / "content" / rel
    if not yp.exists():
        continue
    with open(yp, "r", encoding="utf-8") as f:
        yd = yaml.safe_load(f)
    for e in yd.get("entries", []):
        grk = e.get("greek", "").lower()
        eng = e.get("english", "").lower()
        for t in search_terms:
            if t in grk:
                print(f"  [{uid} | {e['id']}] greek='{e['greek']}' english='{e['english']}'")

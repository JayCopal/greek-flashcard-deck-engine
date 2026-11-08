# -*- coding: utf-8 -*-
"""
Full Audit of CEFR A1 Greek Flashcard Curriculum (Units 01-12)
"""
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
MANIFEST_PATH = BASE_DIR / "content" / "manifest.yaml"
AUDIO_DIR = BASE_DIR / "audio"

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = yaml.safe_load(f)

keg_units = [u for u in manifest.get("units", []) if u["id"].startswith("unit-") and u["id"] != "unit-00"]

print("=" * 78)
print("CEFR A1 GREEK FLASHCARD CURRICULUM AUDIT: UNITS 01 - 12")
print("=" * 78)

total_cards = 0
total_verified = 0
audio_missing_files = []

for u in keg_units:
    rel_path = u["lessons"][0]["file"]
    yaml_path = BASE_DIR / "content" / rel_path
    with open(yaml_path, "r", encoding="utf-8") as yf:
        ydata = yaml.safe_load(yf)
    entries = ydata.get("entries", [])
    verified_in_unit = 0
    for e in entries:
        if e.get("status") == "verified":
            audio_fn = e.get("audio")
            if audio_fn and (AUDIO_DIR / audio_fn).exists():
                verified_in_unit += 1
            else:
                audio_missing_files.append((e["id"], audio_fn))
    total_cards += len(entries)
    total_verified += verified_in_unit
    pct = (verified_in_unit / len(entries) * 100) if entries else 0
    print(f"[{u['id']}] (Order: {u.get('order')}): {ydata.get('title')}")
    print(f"      Cards: {len(entries):2d} | Verified Audio: {verified_in_unit:2d} ({pct:5.1f}%) | Notes: {'Yes' if ydata.get('lesson_notes') else 'No'}")

print("-" * 78)
print(f"SUMMARY: {total_cards} Total Cards across {len(keg_units)} Units.")
print(f"AUDIO INTEGRITY: {total_verified}/{total_cards} verified audio files exist on disk ({total_verified/total_cards*100:.1f}%).")
if audio_missing_files:
    print(f"WARNING: {len(audio_missing_files)} missing audio files detected!")
    for mid, mfn in audio_missing_files:
        print(f"  - {mid}: {mfn}")
else:
    print("ALL AUDIO ASSETS PERFECTLY VERIFIED AND PRESENT ON DISK!")
print("=" * 78)

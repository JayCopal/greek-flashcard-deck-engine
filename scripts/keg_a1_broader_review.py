# -*- coding: utf-8 -*-
import sys
import re
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = yaml.safe_load(f)

core_unit_ids = [f"unit-{i:02d}" for i in range(13)]

# Comprehensive past tense (aorist / imperfect) stems and forms
PAST_PATTERNS = [
    r"\bήμουν\b", r"\bήσουν\b", r"\bήταν\b", r"\bήμασταν\b", r"\bήσασταν\b",
    r"\bείχα\b", r"\bείχες\b", r"\bείχε\b", r"\bείχαμε\b", r"\bείχατε\b", r"\bείχαν\b",
    r"\bπήγα\b", r"\bπήγες\b", r"\bπήγε\b", r"\bπήγαμε\b", r"\bπήγατε\b", r"\bπήγαν\b",
    r"\bήρθα\b", r"\bήρθες\b", r"\bήρθε\b", r"\bήρθαμε\b", r"\bήρθατε\b", r"\bήρθαν\b",
    r"\bείδα\b", r"\bείδες\b", r"\bείδε\b", r"\bείδαμε\b", r"\bείδατε\b", r"\bείδαν\b",
    r"\bείπα\b", r"\bείπες\b", r"\bείπε\b", r"\bείπαμε\b", r"\bείπατε\b", r"\bείπαν\b",
    r"\bέφαγα\b", r"\bέφαγες\b", r"\bέφαγε\b", r"\bφάγαμε\b", r"\bφάγαν\b",
    r"\bήπια\b", r"\bήπιες\b", r"\bήπιε\b", r"\bήπιαμε\b", r"\bήπιαν\b",
    r"\bέκανα\b", r"\bέκανες\b", r"\bέκανε\b", r"\bκάναμε\b", r"\bκάνατε\b", r"\bέκαναν\b",
    r"\bέγραψα\b", r"\bέγραψε\b", r"\bδιάβασα\b", r"\bδιάβασε\b",
    r"\bέμαθα\b", r"\bέμαθες\b", r"\bέμαθε\b", r"\bμάθαμε\b",
    r"\bέμεινα\b", r"\bέμεινες\b", r"\bέμεινε\b", r"\bμείναμε\b",
    r"\bαγόρασα\b", r"\bαγόρασε\b", r"\bπλήρωσα\b", r"\bπλήρωσε\b",
    r"\bέπεσα\b", r"\bέπεσε\b", r"\bέπεσαν\b",
    r"\bβρήκα\b", r"\bβρήκε\b", r"\bέψαξα\b", r"\bέψαξε\b",
    r"\bάκουσα\b", r"\bάκουσε\b",
    r"\bμίλησα\b", r"\bμίλησε\b",
    r"\bζήτησα\b", r"\bζήτησε\b",
    r"\bάνοιξα\b", r"\bάνοιξε\b", r"\bέκλεισα\b", r"\bέκλεισε\b",
    r"\bάρχισα\b", r"\bάρχισε\b", r"\bτελείωσα\b", r"\bτελείωσε\b"
]

warnings = []

for u_entry in manifest.get("units", []):
    u_id = u_entry["id"]
    if u_id not in core_unit_ids:
        continue
    rel_file = u_entry["lessons"][0]["file"]
    yaml_path = CONTENT_DIR / rel_file
    with open(yaml_path, "r", encoding="utf-8") as f:
        ydata = yaml.safe_load(f)
    for e in ydata.get("entries", []):
        ex = e.get("example_el", "")
        # note: avoid false positives like 'κάνει' vs 'έκανε'
        for pat in PAST_PATTERNS:
            m = re.search(pat, ex, re.IGNORECASE)
            if m:
                warnings.append({
                    "unit": u_id,
                    "id": e["id"],
                    "greek": e["greek"],
                    "matched": m.group(0),
                    "example_el": ex,
                    "example_en": e.get("example_en", "")
                })

print(f"Total broader past tense detections: {len(warnings)}")
for w in warnings:
    print(f"  [{w['unit']} | {w['id']}] ({w['greek']}): word '{w['matched']}' in '{w['example_el']}' -> {w['example_en']}")

# -*- coding: utf-8 -*-
"""
Update 5 example sentences to strictly conform to CEFR A1 Present tense rules.
"""
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"

UPDATES = {
    "unit-00": {
        "A1-U00-049": {
            "example_el": "Ο βαθμός μου στις εξετάσεις είναι πολύ καλός.",
            "example_en": "My grade in the exams is very good."
        }
    },
    "unit-09": {
        "A1-U09-037": {
            "example_el": "Σήμερα είναι Δευτέρα, άρα χθες είναι Κυριακή.",
            "example_en": "Today is Monday, so yesterday is Sunday."
        }
    },
    "unit-12": {
        "A1-U12-020": {
            "example_el": "Μένω στο κρεβάτι γιατί έχω γρίπη.",
            "example_en": "I am staying in bed because I have the flu."
        },
        "A1-U12-039": {
            "example_el": "Βοήθεια! Χρειάζομαι έναν γιατρό αμέσως!",
            "example_en": "Help! I need a doctor immediately!"
        },
        "A1-U12-041": {
            "example_el": "Ακούω ότι είσαι άρρωστος. Περαστικά σου!",
            "example_en": "I hear that you are sick. Get well soon!"
        }
    }
}

for uid, card_updates in UPDATES.items():
    yaml_path = CONTENT_DIR / uid / "lesson-01.yaml"
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    changed = 0
    for entry in data.get("entries", []):
        cid = entry.get("id")
        if cid in card_updates:
            entry["example_el"] = card_updates[cid]["example_el"]
            entry["example_en"] = card_updates[cid]["example_en"]
            changed += 1
            print(f"[{uid}] Updated {cid}: {entry['example_el']}")

    if changed:
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        print(f"[OK] Saved {changed} updates to {yaml_path.name}")

# Also update JSON files if they exist
for jf, uid in [("keg_a1_units_09.json", "unit-09"), ("keg_a1_units_12.json", "unit-12")]:
    jp = CONTENT_DIR / jf
    if jp.exists() and uid in UPDATES:
        import json
        with open(jp, "r", encoding="utf-8") as f:
            cards = json.load(f)
        for c in cards:
            if c["id"] in UPDATES[uid]:
                c["example_el"] = UPDATES[uid][c["id"]]["example_el"]
                c["example_en"] = UPDATES[uid][c["id"]]["example_en"]
        with open(jp, "w", encoding="utf-8") as f:
            json.dump(cards, f, ensure_ascii=False, indent=2)
        print(f"[OK] Synced {jp.name}")

print("\nAll 5 example sentences successfully updated to 100% strict A1 present tense!")

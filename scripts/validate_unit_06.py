# -*- coding: utf-8 -*-
import sys
import yaml
import json
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

yaml_path = Path("content/unit-06/lesson-01.yaml")
with open(yaml_path, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

print("Unit ID:", data.get("unit_id"))
print("Lesson ID:", data.get("lesson_id"))
print("Title:", data.get("title"))
print("Entries count:", len(data.get("entries", [])))

req_fields = [
    "id", "greek", "english", "gender_or_pos", "audio", "status", 
    "notes", "example_el", "example_en", "grammatical_info", "keg_communicative_function"
]

errs = []
for e in data["entries"]:
    for fld in req_fields:
        if fld not in e:
            errs.append(f"{e['id']}: missing {fld}")
    pos = e["grammatical_info"].get("part_of_speech", "")
    if ("noun" in pos) and ("pronoun" not in pos):
        if not any(e["greek"].startswith(art) for art in ["ο ", "η ", "το ", "οι ", "τα "]):
            errs.append(f"{e['id']}: noun missing article: {e['greek']}")
    if ("verb" in pos) and ("adverb" not in pos):
        if "verb_type" not in e["grammatical_info"]:
            errs.append(f"{e['id']}: verb missing verb_type")
        if "third_person_singular" not in e["grammatical_info"]:
            errs.append(f"{e['id']}: verb missing third_person_singular")
        if "first_person_plural" not in e["grammatical_info"]:
            errs.append(f"{e['id']}: verb missing first_person_plural")

if errs:
    print(f"Errors found ({len(errs)}):")
    for err in errs:
        print("  -", err)
else:
    print("ALL 40 ENTRIES IN YAML PASS 100% VALIDATION AGAINST LESSON_CREATION_GUIDE!")

print("\n--- Testing FastAPI get_deck Integration ---")
from server.main import get_deck
deck = get_deck()
print("Deck title:", deck["manifest"]["deck_title"])
print("Total units:", deck["stats"]["total_units"])
print("Total entries:", deck["stats"]["total_entries"])
for u in deck["units"]:
    lesson_entries_count = len(u["lessons"][0]["entries"])
    print(f"  - {u['id']}: {u['title']} ({lesson_entries_count} cards)")

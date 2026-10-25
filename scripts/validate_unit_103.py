# -*- coding: utf-8 -*-
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

yaml_path = Path("content/unit-103/lesson-01.yaml")
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
seen_ids = set()
for e in data["entries"]:
    cid = e.get("id")
    if cid in seen_ids:
        errs.append(f"Duplicate card id: {cid}")
    seen_ids.add(cid)

    for fld in req_fields:
        if fld not in e:
            errs.append(f"{cid}: missing field '{fld}'")

    pos = e.get("grammatical_info", {}).get("part_of_speech", "")
    if ("noun" in pos) and ("pronoun" not in pos):
        if not any(e["greek"].startswith(art) for art in ["ο ", "η ", "το ", "οι ", "τα "]):
            errs.append(f"{cid}: noun missing article: {e['greek']}")
        if "plural" not in e["grammatical_info"]:
            errs.append(f"{cid}: noun missing plural")
        if "accusative_singular" not in e["grammatical_info"]:
            errs.append(f"{cid}: noun missing accusative_singular")
    if (pos == "verb" or pos.startswith("verb (")) and ("adverb" not in pos):
        if "verb_type" not in e["grammatical_info"]:
            errs.append(f"{cid}: verb missing verb_type")
        if "third_person_singular" not in e["grammatical_info"]:
            errs.append(f"{cid}: verb missing third_person_singular")
        if "first_person_plural" not in e["grammatical_info"]:
            errs.append(f"{cid}: verb missing first_person_plural")

if errs:
    print(f"FAILED: {len(errs)} errors found:")
    for err in errs:
        print("  -", err)
    sys.exit(1)
else:
    print(f"SUCCESS: All {len(data['entries'])} entries in Unit 103 pass 100% validation!")

print("\n--- Testing FastAPI get_deck Integration ---")
from server.main import get_deck
deck = get_deck()
print("Deck title:", deck["manifest"]["deck_title"])
print("Total units:", deck["stats"]["total_units"])
print("Total entries:", deck["stats"]["total_entries"])
u103 = next((u for u in deck["units"] if u["id"] == "unit-103"), None)
if u103:
    print(f"Found unit-103 in get_deck: '{u103['title']}' with {len(u103['lessons'][0]['entries'])} entries.")
else:
    print("ERROR: unit-103 not found in get_deck!")
    sys.exit(1)

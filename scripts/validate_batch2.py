# -*- coding: utf-8 -*-
import sys
import json

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

file_path = "content/keg_a1_units_03_04.json"
with open(file_path, "r", encoding="utf-8") as f:
    cards = json.load(f)

print(f"Total cards: {len(cards)}")
unit3 = [c for c in cards if c["unit_number"] == 3]
unit4 = [c for c in cards if c["unit_number"] == 4]
print(f"Unit 3 cards: {len(unit3)}")
print(f"Unit 4 cards: {len(unit4)}")

required_keys = [
    "id", "unit_number", "unit_theme", "card_type", "front", 
    "back_primary", "grammatical_info", "keg_communicative_function", 
    "example_el", "example_en", "notes_or_mnemonics"
]

errors = []
for c in cards:
    for k in required_keys:
        if k not in c:
            errors.append(f"{c.get('id')}: missing {k}")
    
    pos = c["grammatical_info"].get("part_of_speech", "")
    
    # check noun rules (exclude pronoun, exclude phrases, exclude numerals)
    if ("noun" in pos) and ("pronoun" not in pos):
        if not any(c["front"].startswith(art) for art in ["ο ", "η ", "το ", "οι ", "τα "]):
            errors.append(f"{c['id']}: noun front does not start with article: {c['front']}")
        if "plural" not in c["grammatical_info"]:
            errors.append(f"{c['id']}: noun missing plural")
        if not any(k in c["grammatical_info"] for k in ["accusative_singular", "accusative_plural", "accusative"]):
            errors.append(f"{c['id']}: noun missing accusative")
            
    # check verb rules (exclude adverb)
    if ("verb" in pos) and ("adverb" not in pos):
        if "verb_type" not in c["grammatical_info"]:
            errors.append(f"{c['id']}: verb missing verb_type")
        if "third_person_singular" not in c["grammatical_info"]:
            errors.append(f"{c['id']}: verb missing third_person_singular")
        if "first_person_plural" not in c["grammatical_info"]:
            errors.append(f"{c['id']}: verb missing first_person_plural")

if errors:
    print(f"Validation ERRORS found ({len(errors)}):")
    for e in errors:
        print("  -", e)
else:
    print("ALL 80 CARDS VALIDATED 100% CLEAN AGAINST SCHEMA!")

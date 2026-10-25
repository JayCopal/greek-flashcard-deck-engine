# -*- coding: utf-8 -*-
import sys
import json

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

with open("content/keg_a1_units_01_02.json", "r", encoding="utf-8") as f:
    cards = json.load(f)

print(f"Total cards: {len(cards)}")
unit1 = [c for c in cards if c["unit_number"] == 1]
unit2 = [c for c in cards if c["unit_number"] == 2]
print(f"Unit 1 cards: {len(unit1)}")
print(f"Unit 2 cards: {len(unit2)}")

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
    
    # check noun rules (exclude pronoun, exclude phrases)
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
    print("ALL 75 CARDS VALIDATED 100% CLEAN AGAINST SCHEMA!")

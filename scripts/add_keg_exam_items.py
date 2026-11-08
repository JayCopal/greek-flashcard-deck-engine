# -*- coding: utf-8 -*-
"""
Enrich Unit 6 and Unit 7 with essential KEG A1 exam items.
"""
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"

# 1. Add to Unit 6: φθηνός, -ή, -ό and το ευρώ
u6_yaml = CONTENT_DIR / "unit-06" / "lesson-01.yaml"
with open(u6_yaml, "r", encoding="utf-8") as f:
    d6 = yaml.safe_load(f)

existing_ids_6 = {e["id"] for e in d6["entries"]}

if "A1-U06-041" not in existing_ids_6:
    d6["entries"].append({
        "id": "A1-U06-041",
        "greek": "φθηνός, -ή, -ό / φτηνός, -ή, -ό",
        "phonetic_hint": "",
        "english": "cheap / inexpensive",
        "notes": "Adjective in -ός, -ή, -ό. Direct opposite of 'ακριβός' (expensive).",
        "gender_or_pos": "adjective",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αυτά τα μήλα είναι πολύ φθηνά σήμερα.",
        "example_en": "These apples are very cheap today.",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine": "φθηνός (φτηνός)",
            "feminine": "φθηνή (φτηνή)",
            "neuter": "φθηνό (φτηνό)",
            "plural": "φθηνοί, φθηνές, φθηνά"
        },
        "keg_communicative_function": "Comparing merchandise prices and identifying bargains"
    })

if "A1-U06-042" not in existing_ids_6:
    d6["entries"].append({
        "id": "A1-U06-042",
        "greek": "το ευρώ",
        "phonetic_hint": "",
        "english": "euro (currency)",
        "notes": "Indeclinable neuter noun (το ευρώ / τα ευρώ). Official currency of Greece.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το ψωμί κοστίζει ένα ευρώ και είκοσι λεπτά.",
        "example_en": "The bread costs one euro and twenty cents.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter indeclinable)",
            "plural": "τα ευρώ",
            "accusative_singular": "το ευρώ"
        },
        "keg_communicative_function": "Stating exact monetary prices and payment amounts"
    })

with open(u6_yaml, "w", encoding="utf-8") as f:
    yaml.dump(d6, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
print(f"[OK] Unit 6 now has {len(d6['entries'])} entries.")

# 2. Add to Unit 7: ενοικιάζεται and πωλείται
u7_yaml = CONTENT_DIR / "unit-07" / "lesson-01.yaml"
with open(u7_yaml, "r", encoding="utf-8") as f:
    d7 = yaml.safe_load(f)

existing_ids_7 = {e["id"] for e in d7["entries"]}

if "A1-U07-044" not in existing_ids_7:
    d7["entries"].append({
        "id": "A1-U07-044",
        "greek": "ενοικιάζεται",
        "phonetic_hint": "",
        "english": "for rent / to let",
        "notes": "3rd person singular passive verb used universally on real estate signs and classified ads.",
        "gender_or_pos": "verb (lexicalized sign formula)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ενοικιάζεται διαμέρισμα στον δεύτερο όροφο.",
        "example_en": "Apartment for rent on the second floor.",
        "grammatical_info": {
            "part_of_speech": "phrase (advertisement formula)",
            "plural": "ενοικιάζονται"
        },
        "keg_communicative_function": "Reading and understanding accommodation rental advertisements"
    })

if "A1-U07-045" not in existing_ids_7:
    d7["entries"].append({
        "id": "A1-U07-045",
        "greek": "πωλείται",
        "phonetic_hint": "",
        "english": "for sale",
        "notes": "Formal 3rd person passive verb used on property and commercial sale signs.",
        "gender_or_pos": "verb (lexicalized sign formula)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πωλείται σπίτι με κήπο κοντά στη θάλασσα.",
        "example_en": "House for sale with garden near the sea.",
        "grammatical_info": {
            "part_of_speech": "phrase (advertisement formula)",
            "plural": "πωλούνται"
        },
        "keg_communicative_function": "Reading real estate and commercial sale notices"
    })

with open(u7_yaml, "w", encoding="utf-8") as f:
    yaml.dump(d7, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
print(f"[OK] Unit 7 now has {len(d7['entries'])} entries.")

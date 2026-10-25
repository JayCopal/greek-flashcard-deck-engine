# -*- coding: utf-8 -*-
"""
Populate content/ YAML files from content/keg_a1_units_01_02.json and content/keg_a1_units_03_04.json
Ensures the app's single source of truth (YAML) reflects all 155 CEFR A1 cards across Units 1-4.
"""
import sys
import json
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
AUDIO_DIR = BASE_DIR / "audio"
JSON_PATH_1_2 = CONTENT_DIR / "keg_a1_units_01_02.json"
JSON_PATH_3_4 = CONTENT_DIR / "keg_a1_units_03_04.json"

cards = []
if JSON_PATH_1_2.exists():
    with open(JSON_PATH_1_2, "r", encoding="utf-8") as f:
        cards.extend(json.load(f))

if JSON_PATH_3_4.exists():
    with open(JSON_PATH_3_4, "r", encoding="utf-8") as f:
        cards.extend(json.load(f))

unit1_cards = [c for c in cards if c["unit_number"] == 1]
unit2_cards = [c for c in cards if c["unit_number"] == 2]
unit3_cards = [c for c in cards if c["unit_number"] == 3]
unit4_cards = [c for c in cards if c["unit_number"] == 4]

print(f"Loaded {len(cards)} cards total (Unit 1: {len(unit1_cards)}, Unit 2: {len(unit2_cards)}, Unit 3: {len(unit3_cards)}, Unit 4: {len(unit4_cards)}).")


def build_card_entry(c):
    audio_file = c.get("audio")
    # Verify physical file existence in audio/
    if audio_file and (AUDIO_DIR / audio_file).exists():
        status = "verified"
    else:
        status = "pending_tts"

    entry = {
        "id": c["id"],
        "greek": c["front"],
        "phonetic_hint": "",
        "english": c["back_primary"],
        "notes": c.get("notes_or_mnemonics", ""),
        "gender_or_pos": c.get("grammatical_info", {}).get("part_of_speech", "phrase"),
        "audio": audio_file,
        "status": status,
        "example_el": c.get("example_el", ""),
        "example_en": c.get("example_en", ""),
        "grammatical_info": c.get("grammatical_info", {}),
        "keg_communicative_function": c.get("keg_communicative_function", ""),
    }
    return entry


# 1. Write Unit 1 Lesson 01 YAML
u1_entries = [build_card_entry(c) for c in unit1_cards]
u1_data = {
    "unit_id": "unit-01",
    "lesson_id": "lesson-01",
    "title": "Χαιρετισμοί & Γνωριμία (Greetings & Introductions)",
    "description": "CEFR A1: Formal & informal greetings, polite addresses, personal pronouns, and core verbs (είμαι, λέω, γράφω).",
    "lesson_status": "not_started",
    "lesson_notes": (
        "Unit 1 Core Grammar Notes:\n"
        "• Vocative Singular: Masculine nouns in -ος end in -ε (κύριε Παπαδόπουλε). Feminine nouns in -α/-η remain unchanged (κυρία, δεσποινίς).\n"
        "• Copular Verb 'είμαι' (Present): εγώ είμαι, εσύ είσαι, αυτός/αυτή/αυτό είναι, εμείς είμαστε, εσείς είστε, αυτοί/αυτές/αυτά είναι.\n"
        "• Stating Names: 'Με λένε + Accusative' (e.g. Με λένε Κώστα) or 'Είμαι ο/η + Nominative'."
    ),
    "entries": u1_entries,
}
u1_file = CONTENT_DIR / "unit-01" / "lesson-01.yaml"
u1_file.parent.mkdir(parents=True, exist_ok=True)
with open(u1_file, "w", encoding="utf-8") as f:
    yaml.dump(u1_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
print(f"Wrote {len(u1_entries)} cards to {u1_file}")

# 2. Write Unit 2 Lesson 01 YAML
u2_entries = [build_card_entry(c) for c in unit2_cards]
u2_data = {
    "unit_id": "unit-02",
    "lesson_id": "lesson-01",
    "title": "Καταγωγή, Εθνικότητες & Γλώσσες (Origins, Nationalities & Languages)",
    "description": "CEFR A1: Countries, nationalities, spoken languages, and verbs of residence & communication (μένω, μιλάω, μαθαίνω).",
    "lesson_status": "not_started",
    "lesson_notes": (
        "Unit 2 Core Grammar Notes:\n"
        "• Expressing Origin: 'από + Accusative' (e.g., Από πού είσαι; — Είμαι από την Ελλάδα).\n"
        "• Expressing Residence: 'σε + Accusative' contracts with article: σε + την = στην, σε + το = στο, σε + τον = στον (e.g., Μένω στην Αθήνα).\n"
        "• Nationalities: Masculine in -ος/-ας/-ης, Feminine in -ίδα/-α (ο Έλληνας / η Ελληνίδα, ο Άγγλος / η Αγγλίδα).\n"
        "• Languages: Neuter plural with definite article (τα ελληνικά, τα αγγλικά, τα γαλλικά)."
    ),
    "entries": u2_entries,
}
u2_file = CONTENT_DIR / "unit-02" / "lesson-01.yaml"
u2_file.parent.mkdir(parents=True, exist_ok=True)
with open(u2_file, "w", encoding="utf-8") as f:
    yaml.dump(u2_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
print(f"Wrote {len(u2_entries)} cards to {u2_file}")

# 3. Write Unit 3 Lesson 01 YAML
u3_entries = [build_card_entry(c) for c in unit3_cards]
u3_data = {
    "unit_id": "unit-03",
    "lesson_id": "lesson-01",
    "title": "Επαγγέλματα & Στοιχεία Επικοινωνίας (Professions & Contact Info)",
    "description": "CEFR A1: Professions (masculine/feminine), workplaces, contact information (numbers 0-100, address, phone), and verbs (δουλεύω, σπουδάζω).",
    "lesson_status": "not_started",
    "lesson_notes": (
        "Unit 3 Core Grammar Notes:\n"
        "• Professions & Gender Suffixes: Masculine in -ος, Feminine in -α/-ος (ο δάσκαλος / η δασκάλα, ο/η γιατρός, ο/η δικηγόρος). Masculine in -ης, Feminine in -τρια (ο καθηγητής / η καθηγήτρια, ο φοιτητής / η φοιτήτρια).\n"
        "• Asking about Profession: 'Τι δουλειά κάνεις;' or 'Με τι ασχολείσαι;'\n"
        "• Cardinal Numerals: μηδέν (0), ένας/μία/ένα (1), δέκα (10), είκοσι (20), εκατό (100)."
    ),
    "entries": u3_entries,
}
u3_file = CONTENT_DIR / "unit-03" / "lesson-01.yaml"
u3_file.parent.mkdir(parents=True, exist_ok=True)
with open(u3_file, "w", encoding="utf-8") as f:
    yaml.dump(u3_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
print(f"Wrote {len(u3_entries)} cards to {u3_file}")

# 4. Write Unit 4 Lesson 01 YAML
u4_entries = [build_card_entry(c) for c in unit4_cards]
u4_data = {
    "unit_id": "unit-04",
    "lesson_id": "lesson-01",
    "title": "Οικογένεια, Περιγραφές & Σχέσεις (Family, Descriptions & Relationships)",
    "description": "CEFR A1: Family members, marital status, physical appearance, the verb 'έχω', and weak possessive clitic pronouns (μου, σου, του/της, μας, σας, τους).",
    "lesson_status": "not_started",
    "lesson_notes": (
        "Unit 4 Core Grammar Notes:\n"
        "• Verb 'έχω' (Present Active): εγώ έχω, εσύ έχεις, αυτός/αυτή/αυτό έχει, εμείς έχουμε, εσείς έχετε, αυτοί/αυτές/αυτά έχουν.\n"
        "• Weak Possessive Clitics: Placed directly after the noun (ο πατέρας μου, η μητέρα σου, το παιδί μας).\n"
        "• Definite Article Rule: Possessive clitics always require the definite article before the noun: 'το μωρό μου' (NOT 'μωρό μου' in declarative statements).\n"
        "• Adjective Agreement: Masculine in -ος, Feminine in -η/-α, Neuter in -ο (ψηλός, ψηλή, ψηλό; νέος, νέα, νέο)."
    ),
    "entries": u4_entries,
}
u4_file = CONTENT_DIR / "unit-04" / "lesson-01.yaml"
u4_file.parent.mkdir(parents=True, exist_ok=True)
with open(u4_file, "w", encoding="utf-8") as f:
    yaml.dump(u4_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
print(f"Wrote {len(u4_entries)} cards to {u4_file}")

# Clean up obsolete lesson-02 in unit-01 if it exists
old_u1_l2 = CONTENT_DIR / "unit-01" / "lesson-02.yaml"
if old_u1_l2.exists():
    old_u1_l2.unlink()
    print(f"Removed obsolete seed file: {old_u1_l2}")

# 5. Write manifest.yaml
manifest_data = {
    "deck_title": "Modern Greek Mastery (CEFR A1)",
    "source_language": "en",
    "target_language": "el",
    "created_at": "2026-10-25",
    "units": [
        {
            "id": "unit-01",
            "title": "Χαιρετισμοί & Γνωριμία (Greetings & Introductions)",
            "order": 1,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-01/lesson-01.yaml",
                    "title": "Χαιρετισμοί & Γνωριμία (Greetings & Introductions)",
                }
            ],
        },
        {
            "id": "unit-02",
            "title": "Καταγωγή, Εθνικότητες & Γλώσσες (Origins, Nationalities & Languages)",
            "order": 2,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-02/lesson-01.yaml",
                    "title": "Καταγωγή, Εθνικότητες & Γλώσσες (Origins, Nationalities & Languages)",
                }
            ],
        },
        {
            "id": "unit-03",
            "title": "Επαγγέλματα & Στοιχεία Επικοινωνίας (Professions & Contact Info)",
            "order": 3,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-03/lesson-01.yaml",
                    "title": "Επαγγέλματα & Στοιχεία Επικοινωνίας (Professions & Contact Info)",
                }
            ],
        },
        {
            "id": "unit-04",
            "title": "Οικογένεια, Περιγραφές & Σχέσεις (Family, Descriptions & Relationships)",
            "order": 4,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-04/lesson-01.yaml",
                    "title": "Οικογένεια, Περιγραφές & Σχέσεις (Family, Descriptions & Relationships)",
                }
            ],
        },
    ],
}

manifest_file = CONTENT_DIR / "manifest.yaml"
with open(manifest_file, "w", encoding="utf-8") as f:
    yaml.dump(manifest_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
print(f"Wrote updated manifest to {manifest_file}")
print("Successfully synced curriculum JSON into YAML source of truth!")

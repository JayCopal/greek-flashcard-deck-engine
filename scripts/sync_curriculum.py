# -*- coding: utf-8 -*-
"""
Curriculum Synchronizer (JSON Batch -> YAML SSOT)
Converts raw CEFR A1 curriculum batches into the project's single source of truth:
  - content/manifest.yaml
  - content/unit-XX/lesson-YY.yaml
Preserves all verified audio assets and existing lesson statuses.
"""
import sys
import glob
import json
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
AUDIO_DIR = BASE_DIR / "audio"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

UNIT_METADATA = {
    1: {
        "title": "Χαιρετισμοί & Γνωριμία (Greetings & Introductions)",
        "description": "CEFR A1: Formal & informal greetings, polite addresses, personal pronouns, and core verbs (είμαι, λέω, γράφω).",
        "lesson_notes": (
            "Unit 1 Core Grammar Notes:\n"
            "• Vocative Singular: Masculine nouns in -ος end in -ε (κύριε Παπαδόπουλε). Feminine nouns in -α/-η remain unchanged (κυρία, δεσποινίς).\n"
            "• Copular Verb 'είμαι' (Present): εγώ είμαι, εσύ είσαι, αυτός/αυτή/αυτό είναι, εμείς είμαστε, εσείς είστε, αυτοί/αυτές/αυτά είναι.\n"
            "• Stating Names: 'Με λένε + Accusative' (e.g. Με λένε Κώστα) or 'Είμαι ο/η + Nominative'."
        ),
    },
    2: {
        "title": "Καταγωγή, Εθνικότητες & Γλώσσες (Origins, Nationalities & Languages)",
        "description": "CEFR A1: Countries, nationalities, spoken languages, and verbs of residence & communication (μένω, μιλάω, μαθαίνω).",
        "lesson_notes": (
            "Unit 2 Core Grammar Notes:\n"
            "• Expressing Origin: 'από + Accusative' (e.g., Από πού είσαι; — Είμαι από την Ελλάδα).\n"
            "• Expressing Residence: 'σε + Accusative' contracts with article: σε + την = στην, σε + το = στο, σε + τον = στον (e.g., Μένω στην Αθήνα).\n"
            "• Nationalities: Masculine in -ος/-ας/-ης, Feminine in -ίδα/-α (ο Έλληνας / η Ελληνίδα, ο Άγγλος / η Αγγλίδα).\n"
            "• Languages: Neuter plural with definite article (τα ελληνικά, τα αγγλικά, τα γαλλικά)."
        ),
    },
    3: {
        "title": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "description": "CEFR A1: Occupations, workplaces, phone numbers, addresses, digits 0-10, and verbs (δουλεύω, σπουδάζω, διδάσκω).",
        "lesson_notes": (
            "Unit 3 Core Grammar Notes:\n"
            "• Inquiring about Profession: 'Τι δουλειά κάνεις;' (informal) or 'Ποιο είναι το επάγγελμά σας;' (formal).\n"
            "• Stating Profession: Copula 'είμαι' + Profession noun WITHOUT indefinite article (e.g., Είμαι γιατρός / Είμαι φοιτητής).\n"
            "• Workplaces with Preposition 'σε': δουλεύω σε γραφείο (in an office), δουλεύω στο νοσοκομείο (at the hospital).\n"
            "• Digits 0–10: μηδέν, ένα, δύο, τρία, τέσσερα, πέντε, έξι, επτά, οκτώ, εννέα, δέκα.\n"
            "• Stating Phone & Address: 'Το τηλέφωνό μου είναι...' / 'Μένω στην οδό... αριθμός...'."
        ),
    },
    4: {
        "title": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "description": "CEFR A1: Family relations, marital status, physical descriptions, the verb 'έχω', and possessive enclitics (μου, σου, του, της).",
        "lesson_notes": (
            "Unit 4 Core Grammar Notes:\n"
            "• Possessive Enclitic Clitics: Placed directly AFTER the noun with definite article: ο πατέρας μου (my father), η μητέρα σου (your mother), το παιδί της (her child).\n"
            "• Double Accent Rule: Proparoxytone nouns (accented on 3rd syllable from end) take an additional accent on the last syllable before a possessive clitic (e.g., το αυτοκίνητό μου).\n"
            "• Describing People: Verb 'είμαι' + Adjective (e.g., Είναι ψηλός, αδύνατος και πολύ συμπαθητικός). Adjectives agree in gender, number, and case with the noun.\n"
            "• The Verb 'έχω' (to have): εγώ έχω, εσύ έχεις, αυτός/αυτή/αυτό έχει, εμείς έχουμε, εσείς έχετε, αυτοί/αυτές/αυτά έχουν."
        ),
    },
    5: {
        "title": "Στο Καφέ & Στην Ταβέρνα (Ordering Food & Drinks)",
        "description": "CEFR A1: Reading Greek menus, ordering food and drinks, coffee preparation styles, taverna etiquette, and consumption verbs (θέλω, πίνω, παίρνω, τρώω).",
        "lesson_notes": (
            "Unit 5 Core Grammar Notes:\n"
            "• Verbs of Consumption & Preference (Present Active Indicative):\n"
            "  - θέλω (Type A): θέλω, θέλεις, θέλει, θέλουμε, θέλετε, θέλουν.\n"
            "  - πίνω (Type A): πίνω, πίνεις, πίνει, πίνουμε, πίνετε, πίνουν.\n"
            "  - παίρνω (Type A): παίρνω, παίρνεις, παίρνει, παίρνουμε, παίρνετε, παίρνουν.\n"
            "  - τρώω (Type A irregular): τρώω, τρως, τρώει, τρώμε, τρώτε, τρώνε.\n"
            "• Direct Object in Accusative with Indefinite Article:\n"
            "  - Masculine: έναν καφέ, έναν χυμό\n"
            "  - Feminine: μία μπίρα (μπύρα), μία σαλάτα\n"
            "  - Neuter: ένα νερό, ένα τοστ, ένα σουβλάκι\n"
            "• Greek Coffee Sweetness Degrees:\n"
            "  - σκέτος (plain / zero sugar)\n"
            "  - μέτριος (medium / 1 spoon sugar)\n"
            "  - γλυκός (sweet / 2 spoons sugar)\n"
            "• Common Ordering Formulas:\n"
            "  - 'Τι θα πάρετε;' (What will you have?)\n"
            "  - 'Για μένα... παρακαλώ.' (For me... please.)\n"
            "  - 'Τον λογαριασμό, παρακαλώ.' (The bill, please.)\n"
            "  - 'Ορίστε!' (Here you are! / Certainly!)\n"
            "  - 'Καλή όρεξη!' (Enjoy your meal!) / 'Στην υγειά μας!' (Cheers!)"
        ),
    },
}


def build_card_entry(c, existing_entry=None):
    audio_file = c.get("audio") or (existing_entry.get("audio") if existing_entry else None)
    
    if audio_file and (AUDIO_DIR / audio_file).exists():
        status = "verified"
    else:
        status = existing_entry.get("status", "pending_tts") if existing_entry else "pending_tts"
        if status == "verified" and not (audio_file and (AUDIO_DIR / audio_file).exists()):
            status = "pending_tts"

    entry = {
        "id": c["id"],
        "greek": c["front"],
        "phonetic_hint": c.get("phonetic_hint", "") or (existing_entry.get("phonetic_hint", "") if existing_entry else ""),
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


def sync_all():
    print("=" * 70)
    print("Curriculum Sync: Aggregating JSON Batches into YAML SSOT")
    print("=" * 70)

    # Find all batch json files
    json_files = sorted(glob.glob(str(CONTENT_DIR / "keg_a1_units_*.json")))
    print(f"Found {len(json_files)} batch JSON files: {[Path(p).name for p in json_files]}")

    all_cards_by_unit = {}
    for jf in json_files:
        with open(jf, "r", encoding="utf-8") as f:
            batch = json.load(f)
            for card in batch:
                u_num = card["unit_number"]
                all_cards_by_unit.setdefault(u_num, []).append(card)

    total_cards = sum(len(cards) for cards in all_cards_by_unit.values())
    print(f"Total aggregated cards: {total_cards} across {len(all_cards_by_unit)} units.")

    # Manifest units container
    manifest_units = []

    for u_num in sorted(all_cards_by_unit.keys()):
        cards = all_cards_by_unit[u_num]
        unit_id = f"unit-{u_num:02d}"
        lesson_id = "lesson-01"
        rel_file = f"{unit_id}/{lesson_id}.yaml"
        yaml_file = CONTENT_DIR / rel_file
        yaml_file.parent.mkdir(parents=True, exist_ok=True)

        meta = UNIT_METADATA.get(u_num, {
            "title": cards[0].get("unit_theme", f"Unit {u_num}"),
            "description": f"CEFR A1 Unit {u_num} curriculum.",
            "lesson_notes": "",
        })

        # Load existing YAML if exists to preserve existing lesson_status/notes
        existing_data = {}
        existing_entries_map = {}
        if yaml_file.exists():
            with open(yaml_file, "r", encoding="utf-8") as f:
                existing_data = yaml.safe_load(f) or {}
                for e in existing_data.get("entries", []):
                    existing_entries_map[e["id"]] = e

        lesson_entries = [
            build_card_entry(c, existing_entries_map.get(c["id"]))
            for c in cards
        ]

        verified_in_unit = sum(1 for e in lesson_entries if e["status"] == "verified")

        lesson_data = {
            "unit_id": unit_id,
            "lesson_id": lesson_id,
            "title": meta["title"],
            "description": meta["description"],
            "lesson_status": existing_data.get("lesson_status", "not_started"),
            "lesson_notes": existing_data.get("lesson_notes") or meta["lesson_notes"],
            "entries": lesson_entries,
        }

        with open(yaml_file, "w", encoding="utf-8") as f:
            yaml.dump(lesson_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

        print(f"-> Unit {u_num}: {len(lesson_entries)} cards written to {rel_file} ({verified_in_unit} verified)")

        manifest_units.append({
            "id": unit_id,
            "title": meta["title"],
            "order": u_num,
            "lessons": [
                {
                    "id": lesson_id,
                    "file": rel_file,
                    "title": meta["title"],
                }
            ],
        })

    # Write Manifest
    manifest_data = {
        "deck_title": "Modern Greek Mastery (CEFR A1)",
        "source_language": "en",
        "target_language": "el",
        "created_at": "2026-10-25",
        "units": manifest_units,
    }

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    print("-" * 70)
    print(f"Manifest updated at {MANIFEST_PATH.name} with {len(manifest_units)} units.")
    print("Curriculum successfully synced to YAML Single Source of Truth!")


if __name__ == "__main__":
    sync_all()

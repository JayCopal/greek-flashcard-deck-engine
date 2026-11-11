# -*- coding: utf-8 -*-
"""
Register unit-sp-01 through unit-sp-06 in content/manifest.yaml and
verify all 240 KEG A2 Speaking cards and 720 Chirp-3 HD audio files.
"""
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from server.tts_service import synthesize_greek_chirp, generate_audio_filename

AUDIO_DIR = BASE_DIR / "audio"
CONTENT_DIR = BASE_DIR / "content"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

SP_UNITS_META = [
    {
        "id": "unit-sp-01",
        "order": "SP-01-A",
        "title": "Προφορικά SP-01: Προσωπική Συνέντευξη & Ζέσταμα (Stage 1 Examiner Q&A Drills)",
        "description": "40 rapid examiner question-and-answer drills for Stage 1 of the KEG A2 Speaking exam: personal identity, family, daily routine, work/studies, weekend habits, hobbies, neighborhood, and motivation for learning Greek.",
    },
    {
        "id": "unit-sp-02",
        "order": "SP-02-A",
        "title": "Προφορικά SP-02: Συνδετικές Εκφράσεις & Διαχείριση Ροής (Conversational Connectors & Fluency Boosters)",
        "description": "40 high-frequency spoken connectors, hesitation managers, opinion frames, active listening tokens, and polite clarification formulas to eliminate silent freezes across all 3 stages of the KEG A2 Speaking exam.",
    },
    {
        "id": "unit-sp-03",
        "order": "SP-03-A",
        "title": "Προφορικά SP-03: Κάρτες Ρόλων & Διάδραση (Stage 2 Cue Card Scenarios & Bilateral Roleplays)",
        "description": "40 bilateral roleplay cue-card prompts and transactional exchanges for Stage 2 of the KEG A2 Speaking exam across 6 high-yield scenarios: travel/ferry agency, pharmacy/clinic, real estate office, clothing store, organizing a celebration, and polite complaints.",
    },
    {
        "id": "unit-sp-04",
        "order": "SP-04-A",
        "title": "Προφορικά SP-04: Περιγραφή Εικόνας & Αφήγηση (Stage 3 Visual Description Lego Framework)",
        "description": "40 structured image-description building blocks and full scene monologues following the 4-step Lego formula for Stage 3 of the KEG A2 Speaking exam: panoramic overview, spatial layout, character/action/clothing breakdown, and weather/mood/context hypothesis.",
    },
    {
        "id": "unit-sp-05",
        "order": "SP-05-A",
        "title": "Προφορικά SP-05: Ερωτήσεις Επέκτασης & Προσωπική Εμπειρία (Stage 3 Examiner Extension Questions)",
        "description": "40 examiner follow-up prompts bridging the Stage 3 visual stimulus to the candidate’s personal life, multi-tense storytelling (comparing past habits in Imperfect/Aorist with Present routines and Future plans), and lifestyle preferences.",
    },
    {
        "id": "unit-sp-06",
        "order": "SP-06-A",
        "title": "Προφορικά SP-06: Προφορά, Επιτονισμός & Παγίδες Προφορικού Λόγου (Spoken Phonology & Trap Drills)",
        "description": "40 orthoepic and morphological trap drills targeting Criterion 4 (Pronunciation & Intonation) and Criterion 2 (Accuracy): nasal stops (μπ/π, ντ/τ, γκ/κ), diphthongs (αυ/ευ), stress shifts across tenses, and polite conditional tone modulation.",
    },
]


def register_in_manifest():
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    units = manifest.get("units", [])
    existing_ids = {u["id"]: idx for idx, u in enumerate(units)}

    added = 0
    updated = 0
    for meta in SP_UNITS_META:
        entry = {
            "id": meta["id"],
            "title": meta["title"],
            "description": meta["description"],
            "order": meta["order"],
            "total_lessons": 1,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": f"{meta['id']}/lesson-01.yaml",
                    "title": meta["title"],
                    "description": meta["description"],
                }
            ],
        }
        if meta["id"] in existing_ids:
            units[existing_ids[meta["id"]]] = entry
            updated += 1
        else:
            units.append(entry)
            added += 1

    manifest["units"] = units
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"[Manifest] Added {added}, updated {updated} Speaking units. Total units in manifest: {len(units)}")


def verify_speaking_units():
    total_cards = 0
    total_audio_refs = 0
    missing_audio = []
    schema_issues = []

    required_fields = [
        "id",
        "greek",
        "english",
        "gender_or_pos",
        "status",
        "grammatical_info",
        "notes",
        "example_el",
        "example_en",
        "example2_el",
        "example2_en",
        "keg_communicative_function",
        "audio",
        "example_audio",
        "example2_audio",
    ]

    for meta in SP_UNITS_META:
        unit_id = meta["id"]
        lesson_path = CONTENT_DIR / unit_id / "lesson-01.yaml"
        if not lesson_path.exists():
            raise FileNotFoundError(f"Missing lesson file: {lesson_path}")

        with open(lesson_path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        entries = data.get("entries", [])
        print(f"  Checking {unit_id}: {len(entries)} cards")
        total_cards += len(entries)

        for card in entries:
            cid = card.get("id", "UNKNOWN")
            for rf in required_fields:
                if not card.get(rf):
                    schema_issues.append((unit_id, cid, f"Missing field: {rf}"))
            ginfo = card.get("grammatical_info") or {}
            if not ginfo.get("stage") or not ginfo.get("focus"):
                schema_issues.append((unit_id, cid, "Missing grammatical_info.stage or focus"))

            for audio_key, text_key in [
                ("audio", "greek"),
                ("example_audio", "example_el"),
                ("example2_audio", "example2_el"),
            ]:
                fn = card.get(audio_key)
                txt = card.get(text_key)
                if fn and txt:
                    total_audio_refs += 1
                    ap = AUDIO_DIR / fn
                    if not ap.exists() or ap.stat().st_size == 0:
                        missing_audio.append((unit_id, cid, audio_key, txt, fn))

    print(f"\nTotal Speaking Units: {len(SP_UNITS_META)}")
    print(f"Total Speaking Cards: {total_cards}")
    print(f"Total Audio References: {total_audio_refs}")
    print(f"Schema Issues: {len(schema_issues)}")
    print(f"Missing / 0-byte Audio Files: {len(missing_audio)}")

    if schema_issues:
        for u, c, msg in schema_issues[:20]:
            print(f"  [SCHEMA ISSUE] {u} / {c}: {msg}")

    if missing_audio:
        print("\nSynthesizing missing audio files...")
        for u, c, k, txt, fn in missing_audio:
            print(f"  Synthesizing {c} ({k}) -> {fn}")
            audio_bytes = synthesize_greek_chirp(txt)
            with open(AUDIO_DIR / fn, "wb") as f:
                f.write(audio_bytes)
            print(f"    [OK] {len(audio_bytes)} bytes")

    if not schema_issues and not missing_audio:
        print(f"\n[VERIFIED 100%] All {total_cards} KEG A2 Speaking cards and {total_audio_refs} Chirp-3 HD audio files are verified!")


if __name__ == "__main__":
    register_in_manifest()
    verify_speaking_units()

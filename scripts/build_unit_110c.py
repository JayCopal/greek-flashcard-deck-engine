import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path("c:/jay-programs/greek-flashcard-deck-engine").resolve()
CONTENT_DIR = BASE_DIR / "content"

# Import verified cards from scratch/verify_final_110c.py
SCRATCH_DIR = Path(
    "C:/Users/chatt/.gemini/antigravity/brain/021c1221-a180-4407-8133-8766351c7604/scratch"
)
sys.path.insert(0, str(SCRATCH_DIR))
import verify_final_110c  # noqa: E402

cards = verify_final_110c.cards_u110c
print(f"Loaded {len(cards)} verified cards for Unit 110c.")

# Prepare unit directory
u110c_dir = CONTENT_DIR / "unit-110c"
u110c_dir.mkdir(parents=True, exist_ok=True)
lesson_file = u110c_dir / "lesson-01.yaml"

lesson_data = {
    "unit_id": "unit-110c",
    "lesson_id": "lesson-01",
    "title": "Ενότητα 10: Διάλογοι & Εξετάσεις — Υγεία, Συμπτώματα, Γιατρός & Φαρμακείο (A1 Synthesis)",
    "description": "Conversational, dialogue, and CEFR A1 oral exam practice focusing on symptoms, body parts, medical appointments, clinical instructions, pharmacy prescriptions, medications, hospital facilities, and traditional Greek convalescence wishes using vocabulary from Lessons 100 to 110.",
    "lesson_status": "not_started",
    "entries": cards,
}

# Dump YAML with clean formatting
with open(lesson_file, "w", encoding="utf-8") as f:
    yaml.dump(lesson_data, f, allow_unicode=True, sort_keys=False, width=120)

print(f"Wrote {lesson_file} successfully.")

# Insert into manifest.yaml directly after unit-110b
manifest_path = CONTENT_DIR / "manifest.yaml"
manifest_text = manifest_path.read_text(encoding="utf-8")

unit_110c_manifest = """- id: unit-110c
  title: 'Κλικ στα Ελληνικά Α1: Σελίδες 219-232 (Ενότητα 10: Περαστικά! - Διάλογοι, Εξετάσεις & Συνομιλίες)'
  order: KlikA1-10-C
  is_expansion: true
  expansion_of: KlikA1-10-A
  lessons:
  - id: lesson-01
    file: unit-110c/lesson-01.yaml
    title: 'Ενότητα 10: Διάλογοι & Εξετάσεις — Υγεία, Συμπτώματα, Γιατρός & Φαρμακείο (A1 Synthesis)'
    description: Conversational, dialogue, and CEFR A1 oral exam practice focusing on symptoms, body parts, medical appointments, clinical instructions, pharmacy prescriptions, medications, hospital facilities, and traditional Greek convalescence wishes using vocabulary from Lessons 100 to 110.
"""

if "- id: unit-110c" not in manifest_text:
    target_pos = manifest_text.find("- id: unit-111\n")
    if target_pos != -1:
        manifest_text = (
            manifest_text[:target_pos] + unit_110c_manifest + manifest_text[target_pos:]
        )
        manifest_path.write_text(manifest_text, encoding="utf-8")
        print("Inserted unit-110c into content/manifest.yaml")
    else:
        print("Warning: could not find '- id: unit-111' marker in manifest.yaml")
else:
    print("unit-110c already present in content/manifest.yaml")

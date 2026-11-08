import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path("c:/jay-programs/greek-flashcard-deck-engine").resolve()
CONTENT_DIR = BASE_DIR / "content"

# Import verified cards from scratch/verify_final_111c.py
SCRATCH_DIR = Path(
    "C:/Users/chatt/.gemini/antigravity/brain/021c1221-a180-4407-8133-8766351c7604/scratch"
)
sys.path.insert(0, str(SCRATCH_DIR))
import verify_final_111c  # noqa: E402

cards = verify_final_111c.cards_u111c
print(f"Loaded {len(cards)} verified cards for Unit 111c.")

# Verify that there are 0 vocabulary errors
total_errs = 0
for c in cards:
    cid = c["id"]
    eg = verify_final_111c.check_text(c["greek"])
    ee = verify_final_111c.check_text(c["example_el"])
    if eg or ee:
        total_errs += 1
        print(f"ERROR in {cid}: greek errs: {eg}, example errs: {ee}")

if total_errs > 0:
    print(f"ABORT: {total_errs} cards have vocabulary errors!")
    sys.exit(1)

print("Pre-flight check passed: 100% vocabulary compliance (0 unknown words).")

# Prepare unit directory
u111c_dir = CONTENT_DIR / "unit-111c"
u111c_dir.mkdir(parents=True, exist_ok=True)
lesson_file = u111c_dir / "lesson-01.yaml"

lesson_data = {
    "unit_id": "unit-111c",
    "lesson_id": "lesson-01",
    "title": "Ενότητα 11: Διάλογοι & Εξετάσεις — Υπηρεσίες, Τράπεζα, Ταχυδρομείο & A1 Capstone (A1 Synthesis)",
    "description": "Conversational, dialogue, and CEFR A1 capstone oral exam practice covering banking transactions, ATM usage, postal dispatch, utility bill payments, priority queues, indirect speech, and comprehensive A1 conversational synthesis using vocabulary from Lessons 100 to 111.",
    "lesson_status": "not_started",
    "entries": cards,
}

# Dump YAML with clean formatting
with open(lesson_file, "w", encoding="utf-8") as f:
    yaml.dump(lesson_data, f, allow_unicode=True, sort_keys=False, width=120)

print(f"Wrote {lesson_file} successfully.")

# Insert into manifest.yaml directly after unit-111b
manifest_path = CONTENT_DIR / "manifest.yaml"
manifest_text = manifest_path.read_text(encoding="utf-8")

unit_111c_manifest = """- id: unit-111c
  title: 'Κλικ στα Ελληνικά Α1: Σελίδες 233-255 (Ενότητα 11: Στη σειρά σας παρακαλώ! & Τελική Επανάληψη - Διάλογοι, Εξετάσεις & Συνομιλίες)'
  order: KlikA1-11-C
  is_expansion: true
  expansion_of: KlikA1-11-A
  lessons:
  - id: lesson-01
    file: unit-111c/lesson-01.yaml
    title: 'Ενότητα 11: Διάλογοι & Εξετάσεις — Υπηρεσίες, Τράπεζα, Ταχυδρομείο & A1 Capstone (A1 Synthesis)'
    description: Conversational, dialogue, and CEFR A1 capstone oral exam practice covering banking transactions, ATM usage, postal dispatch, utility bill payments, priority queues, indirect speech, and comprehensive A1 conversational synthesis using vocabulary from Lessons 100 to 111.
"""

if "- id: unit-111c" not in manifest_text:
    manifest_text = manifest_text.rstrip() + "\n" + unit_111c_manifest
    manifest_path.write_text(manifest_text, encoding="utf-8")
    print("Inserted unit-111c into content/manifest.yaml")
else:
    print("unit-111c already present in content/manifest.yaml")

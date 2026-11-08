import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path("c:/jay-programs/greek-flashcard-deck-engine").resolve()
CONTENT_DIR = BASE_DIR / "content"

# Import verified cards from scratch/test_all_109c_clean.py
SCRATCH_DIR = Path(
    "C:/Users/chatt/.gemini/antigravity/brain/021c1221-a180-4407-8133-8766351c7604/scratch"
)
sys.path.insert(0, str(SCRATCH_DIR))
import test_all_109c_clean  # noqa: E402

cards = test_all_109c_clean.cards
print(f"Loaded {len(cards)} verified cards for Unit 109c.")

# Prepare unit directory
u109c_dir = CONTENT_DIR / "unit-109c"
u109c_dir.mkdir(parents=True, exist_ok=True)
lesson_file = u109c_dir / "lesson-01.yaml"

lesson_data = {
    "unit_id": "unit-109c",
    "lesson_id": "lesson-01",
    "title": "Ενότητα 9: Διάλογοι & Εξετάσεις — Σπουδές, Εργασία, Επαγγέλματα & Αόριστος (A1 Synthesis)",
    "description": "Conversational, dialogue, and CEFR A1 oral exam practice focusing on university studies, courses, stationery, job interviews, professional duties, work schedules, salary negotiations, leave entitlement, and simple past (aorist) narrative interactions using vocabulary from Lessons 100 to 109.",
    "lesson_status": "not_started",
    "entries": cards,
}

# Dump YAML with clean formatting
with open(lesson_file, "w", encoding="utf-8") as f:
    yaml.dump(lesson_data, f, allow_unicode=True, sort_keys=False, width=120)

print(f"Wrote {lesson_file} successfully.")

# Insert into manifest.yaml directly after unit-109b
manifest_path = CONTENT_DIR / "manifest.yaml"
manifest_text = manifest_path.read_text(encoding="utf-8")

unit_109c_manifest = """- id: unit-109c
  title: 'Κλικ στα Ελληνικά Α1: Σελίδες 195-218 (Ενότητα 9: Σπουδάζεις ή δουλεύεις; - Διάλογοι, Εξετάσεις & Συνομιλίες)'
  order: KlikA1-09-C
  is_expansion: true
  expansion_of: KlikA1-09-A
  lessons:
  - id: lesson-01
    file: unit-109c/lesson-01.yaml
    title: 'Ενότητα 9: Διάλογοι & Εξετάσεις — Σπουδές, Εργασία, Επαγγέλματα & Αόριστος (A1 Synthesis)'
    description: Conversational, dialogue, and CEFR A1 oral exam practice focusing on university studies, courses, stationery, job interviews, professional duties, work schedules, salary negotiations, leave entitlement, and simple past (aorist) narrative interactions using vocabulary from Lessons 100 to 109.
"""

if "- id: unit-109c" not in manifest_text:
    # Find unit-109b block and insert right after it
    # Find unit-110
    target_pos = manifest_text.find("- id: unit-110\n")
    if target_pos != -1:
        manifest_text = (
            manifest_text[:target_pos] + unit_109c_manifest + manifest_text[target_pos:]
        )
        manifest_path.write_text(manifest_text, encoding="utf-8")
        print("Inserted unit-109c into content/manifest.yaml")
    else:
        print("Warning: could not find '- id: unit-110' marker in manifest.yaml")
else:
    print("unit-109c already present in content/manifest.yaml")

# -*- coding: utf-8 -*-
"""
Migrates Klik A1 units so that:
  - Unit 100 = Εισαγωγική Ενότητα (Introductory Unit, Pages 25-41) -> KlikA1-00-A
  - Unit 101 = Book Ενότητα 1 (Pages 43-54) -> KlikA1-01-A
  - Unit 102 = Book Ενότητα 2 (Pages 55-68) -> KlikA1-02-A
  ...
  - Unit 111 = Book Ενότητα 11 (Pages 233-255) -> KlikA1-11-A
"""
import sys
import os
import re
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

# Exact mapping from old unit id to new metadata
UNIT_MAPPINGS = [
    # (old_id, new_id, old_prefix, new_prefix, new_order, new_expansion_of)
    ("unit-101",  "unit-100",  "A1-U101",  "A1-U100",  "KlikA1-00-A", None),
    ("unit-102",  "unit-101",  "A1-U102",  "A1-U101",  "KlikA1-01-A", None),
    ("unit-103",  "unit-102",  "A1-U103",  "A1-U102",  "KlikA1-02-A", None),
    ("unit-103b", "unit-102b", "A1-U103B", "A1-U102B", "KlikA1-02-B", "KlikA1-02-A"),
    ("unit-104",  "unit-103",  "A1-U104",  "A1-U103",  "KlikA1-03-A", None),
    ("unit-104b", "unit-103b", "A1-U104B", "A1-U103B", "KlikA1-03-B", "KlikA1-03-A"),
    ("unit-105",  "unit-104",  "A1-U105",  "A1-U104",  "KlikA1-04-A", None),
    ("unit-105b", "unit-104b", "A1-U105B", "A1-U104B", "KlikA1-04-B", "KlikA1-04-A"),
    ("unit-106",  "unit-105",  "A1-U106",  "A1-U105",  "KlikA1-05-A", None),
    ("unit-106b", "unit-105b", "A1-U106B", "A1-U105B", "KlikA1-05-B", "KlikA1-05-A"),
    ("unit-106c", "unit-105c", "A1-U106C", "A1-U105C", "KlikA1-05-C", "KlikA1-05-A"),
    ("unit-107",  "unit-106",  "A1-U107",  "A1-U106",  "KlikA1-06-A", None),
    ("unit-107b", "unit-106b", "A1-U107B", "A1-U106B", "KlikA1-06-B", "KlikA1-06-A"),
    ("unit-107c", "unit-106c", "A1-U107C", "A1-U106C", "KlikA1-06-C", "KlikA1-06-A"),
    ("unit-108",  "unit-107",  "A1-U108",  "A1-U107",  "KlikA1-07-A", None),
    ("unit-108b", "unit-107b", "A1-U108B", "A1-U107B", "KlikA1-07-B", "KlikA1-07-A"),
    ("unit-108c", "unit-107c", "A1-U108C", "A1-U107C", "KlikA1-07-C", "KlikA1-07-A"),
    ("unit-109",  "unit-108",  "A1-U109",  "A1-U108",  "KlikA1-08-A", None),
    ("unit-109b", "unit-108b", "A1-U109B", "A1-U108B", "KlikA1-08-B", "KlikA1-08-A"),
    ("unit-110",  "unit-109",  "A1-U110",  "A1-U109",  "KlikA1-09-A", None),
    ("unit-110b", "unit-109b", "A1-U110B", "A1-U109B", "KlikA1-09-B", "KlikA1-09-A"),
    ("unit-111",  "unit-110",  "A1-U111",  "A1-U110",  "KlikA1-10-A", None),
    ("unit-111b", "unit-110b", "A1-U111B", "A1-U110B", "KlikA1-10-B", "KlikA1-10-A"),
    ("unit-112",  "unit-111",  "A1-U112",  "A1-U111",  "KlikA1-11-A", None),
    ("unit-112b", "unit-111b", "A1-U112B", "A1-U111B", "KlikA1-11-B", "KlikA1-11-A"),
]

MAPPING_BY_OLD = {m[0]: m for m in UNIT_MAPPINGS}

def update_text_references(text: str) -> str:
    """Updates textual mentions in descriptions like 'Lesson 103' -> 'Lesson 102'."""
    replacements = [
        ("Lessons 101 to 108", "Lessons 100 to 107"),
        ("Lessons 101 to 107", "Lessons 100 to 106"),
        ("Units 101 to 106", "Units 100 to 105"),
        ("Synthesis 101-108", "Synthesis 100-107"),
        ("Synthesis 101-107", "Synthesis 100-106"),
        ("Lesson 111", "Lesson 110"),
        ("Lesson 110", "Lesson 109"),
        ("Lesson 109", "Lesson 108"),
        ("Lesson 108", "Lesson 107"),
        ("Lesson 107", "Lesson 106"),
        ("Lesson 106", "Lesson 105"),
        ("Lesson 105", "Lesson 104"),
        ("Lesson 104", "Lesson 103"),
        ("Lesson 103", "Lesson 102"),
        ("Lesson 102", "Lesson 101"),
        ("Lesson 101", "Lesson 100"),
    ]
    for old_s, new_s in replacements:
        text = text.replace(old_s, new_s)
    return text

def migrate():
    print("=== Starting Klik A1 Unit Migration ===")
    
    # Step 1: Migrate folders in order
    for old_id, new_id, old_prefix, new_prefix, new_order, new_exp in UNIT_MAPPINGS:
        old_path = CONTENT_DIR / old_id
        new_path = CONTENT_DIR / new_id
        if not old_path.exists():
            print(f"Skipping {old_id} (does not exist)")
            continue
        
        print(f"Moving folder: {old_id} -> {new_id}")
        old_path.rename(new_path)
        
        # Step 2: Update lesson-01.yaml inside new folder
        lesson_file = new_path / "lesson-01.yaml"
        if lesson_file.exists():
            with open(lesson_file, "r", encoding="utf-8") as f:
                data = yaml.safe_load(f)
            
            # Update unit_id
            if isinstance(data, dict):
                data["unit_id"] = new_id
                if "description" in data and data["description"]:
                    data["description"] = update_text_references(data["description"])
                
                # Update card entries
                entries = data.get("entries", [])
                for entry in entries:
                    cid = entry.get("id", "")
                    # Match old prefix e.g. A1-U101-001 -> A1-U100-001
                    if cid.startswith(old_prefix + "-") or cid.startswith(old_prefix.upper() + "-"):
                        suffix = cid.split("-", 2)[2]
                        entry["id"] = f"{new_prefix}-{suffix}"
            
            with open(lesson_file, "w", encoding="utf-8") as f:
                yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
            print(f"  Updated YAML entries with prefix {new_prefix} in {new_id}/lesson-01.yaml")

    # Step 3: Update manifest.yaml
    print("\nUpdating content/manifest.yaml...")
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)
    
    updated_units = []
    for u in manifest.get("units", []):
        uid = u.get("id")
        if uid in MAPPING_BY_OLD:
            _, new_id, _, _, new_order, new_exp = MAPPING_BY_OLD[uid]
            u["id"] = new_id
            u["order"] = new_order
            if new_exp:
                u["expansion_of"] = new_exp
            elif "expansion_of" in u:
                del u["expansion_of"]
            
            # update lessons list
            for l in u.get("lessons", []):
                old_file = l.get("file", "")
                l["file"] = f"{new_id}/lesson-01.yaml"
                if "description" in l and l["description"]:
                    l["description"] = update_text_references(l["description"])
            
            if "description" in u and u["description"]:
                u["description"] = update_text_references(u["description"])
        
        updated_units.append(u)
    
    manifest["units"] = updated_units
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("content/manifest.yaml updated successfully.")

if __name__ == "__main__":
    migrate()

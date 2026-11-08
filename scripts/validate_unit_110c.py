# -*- coding: utf-8 -*-
"""
Validation script for Unit 110 C:
- Verifies YAML structure and schema integrity
- Checks all required fields for each entry
- Verifies FastAPI server get_deck integration
- Programmatically verifies that all Greek words are in Lessons 100-110 or allowed conversational fillers.
"""

import sys
import re
import unicodedata
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

YAML_PATH = BASE_DIR / "content" / "unit-110c" / "lesson-01.yaml"
if not YAML_PATH.exists():
    print(f"ERROR: {YAML_PATH} does not exist!")
    sys.exit(1)

with open(YAML_PATH, "r", encoding="utf-8") as f:
    data = yaml.safe_load(f)

print("Unit ID:", data.get("unit_id"))
print("Lesson ID:", data.get("lesson_id"))
print("Title:", data.get("title"))
entries = data.get("entries", [])
print("Entries count:", len(entries))

req_fields = [
    "id",
    "greek",
    "english",
    "gender_or_pos",
    "audio",
    "status",
    "notes",
    "example_el",
    "example_en",
    "grammatical_info",
    "keg_communicative_function",
]

errs = []
seen_ids = set()

for e in entries:
    cid = e.get("id")
    if cid in seen_ids:
        errs.append(f"Duplicate card id: {cid}")
    seen_ids.add(cid)

    for fld in req_fields:
        if fld not in e:
            errs.append(f"{cid}: missing field '{fld}'")

# --- Vocabulary Compliance Check (Lessons 100-110 + simple fillers) ---
CONTENT_DIR = BASE_DIR / "content"
units_100_to_110 = [
    "unit-100",
    "unit-101",
    "unit-102",
    "unit-102b",
    "unit-103",
    "unit-103b",
    "unit-104",
    "unit-104b",
    "unit-105",
    "unit-105b",
    "unit-105c",
    "unit-106",
    "unit-106b",
    "unit-106c",
    "unit-107",
    "unit-107b",
    "unit-107c",
    "unit-108",
    "unit-108b",
    "unit-108c",
    "unit-109",
    "unit-109b",
    "unit-109c",
    "unit-110",
    "unit-110b",
]

known_words = set()
for u in units_100_to_110:
    up = CONTENT_DIR / u / "lesson-01.yaml"
    if up.exists():
        udata = yaml.safe_load(up.read_text(encoding="utf-8"))
        for entry in udata.get("entries", []):
            texts = [entry.get("greek", ""), entry.get("example_el", "")]
            ginfo = entry.get("grammatical_info", {})
            if isinstance(ginfo, dict):
                for val in ginfo.values():
                    if isinstance(val, str):
                        texts.append(val)
            for t in texts:
                for w in re.findall(r"[\u0370-\u03ff\u1f00-\u1fff]+", t):
                    nw = unicodedata.normalize("NFC", w.strip().lower())
                    nw = re.sub(r"[^\w]", "", nw, flags=re.UNICODE)
                    if nw:
                        known_words.add(nw)

filler_words = {
    "λοιπόν",
    "εντάξει",
    "μάλιστα",
    "βέβαια",
    "φυσικά",
    "ωραία",
    "τέλεια",
    "συγγνώμη",
    "ορίστε",
    "δηλαδή",
    "ίσως",
    "μήπως",
    "α",
    "ε",
    "μπα",
    "αχ",
    "ωχ",
    "έλα",
    "βρε",
    "πω",
    "αμέσως",
    "βεβαίως",
    "ναι",
    "όχι",
}


def check_words(text):
    words = re.findall(r"[\u0370-\u03ff\u1f00-\u1fff]+", text)
    unknown = []
    for w in words:
        cw = unicodedata.normalize("NFC", w.strip().lower())
        cw = re.sub(r"[^\w]", "", cw, flags=re.UNICODE)
        if cw and cw not in known_words and cw not in filler_words:
            unknown.append(w)
    return unknown


for e in entries:
    cid = e.get("id")
    ug = check_words(e.get("greek", ""))
    if ug:
        errs.append(f"{cid} GREEK field uses unverified words: {ug}")
    ue = check_words(e.get("example_el", ""))
    if ue:
        errs.append(f"{cid} EXAMPLE_EL field uses unverified words: {ue}")

if errs:
    print(f"\nFAILED: {len(errs)} errors found:")
    for err in errs:
        print("  -", err)
    sys.exit(1)
else:
    print(
        f"\nSUCCESS: All {len(entries)} entries in Unit 110 C pass 100% schema & vocabulary validation!"
    )

print("\n--- Testing FastAPI get_deck Integration ---")
from server.main import get_deck  # noqa: E402

deck = get_deck()
print("Deck title:", deck["manifest"]["deck_title"])
print("Total units:", deck["stats"]["total_units"])
print("Total entries:", deck["stats"]["total_entries"])
u110c = next((u for u in deck["units"] if u["id"] == "unit-110c"), None)
if u110c:
    print(
        f"Found unit-110c in get_deck: '{u110c['title']}' with {len(u110c['lessons'][0]['entries'])} entries."
    )
else:
    print("ERROR: unit-110c not found in get_deck!")
    sys.exit(1)

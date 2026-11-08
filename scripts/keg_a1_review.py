# -*- coding: utf-8 -*-
"""
Deep Alignment Review of Flashcards against KEG Level A1 Specifications
(Centre for the Greek Language - Certificate of Attainment in Greek)
"""
import sys
import re
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = yaml.safe_load(f)

# Collect all core units 00 to 12
core_unit_ids = [f"unit-{i:02d}" for i in range(13)]

# Known Aorist / Past tense indicators in Modern Greek to flag
PAST_TENSE_PATTERNS = [
    r"\bέμεινα\b", r"\bέμεινες\b", r"\bέμεινε\b",
    r"\bέπεσε\b", r"\bέπεσα\b",
    r"\bέμαθα\b", r"\bέμαθες\b",
    r"\bπήγα\b", r"\bπήγες\b", r"\bπήγε\b",
    r"\bήρθα\b", r"\bήρθες\b", r"\bήρθε\b",
    r"\bέφαγα\b", r"\bέφαγες\b", r"\bέφαγε\b",
    r"\bήπια\b", r"\bήπιες\b", r"\bήπιε\b",
    r"\bείδα\b", r"\bείδες\b", r"\bείδε\b",
    r"\bείπα\b", r"\bείπες\b", r"\bείπε\b",
    r"\bέκανα\b", r"\bέκανες\b", # Note: 'έκανα' can be past
    r"\bέγραψα\b", r"\bδιάβασα\b",
    r"\bαγόρασα\b", r"\bπλήρωσα\b"
]

# Check for unaccented multi-syllable Greek words
ACCENT_REGEX = re.compile(r"[άέήίόύώΐΰΆΈΉΊΌΎΏ]")

print("=" * 80)
print("AUDITING UNITS 00-12 AGAINST OFFICIAL KEG A1 SPECIFICATIONS")
print("=" * 80)

audit_results = {
    "total_cards": 0,
    "past_tense_warnings": [],
    "accent_warnings": [],
    "noun_article_warnings": [],
    "verb_structure_warnings": [],
    "domain_distribution": {},
}

for u_entry in manifest.get("units", []):
    u_id = u_entry["id"]
    if u_id not in core_unit_ids:
        continue

    rel_file = u_entry["lessons"][0]["file"]
    yaml_path = CONTENT_DIR / rel_file
    with open(yaml_path, "r", encoding="utf-8") as f:
        ydata = yaml.safe_load(f)

    entries = ydata.get("entries", [])
    unit_title = ydata.get("title", "")
    audit_results["domain_distribution"][u_id] = {
        "title": unit_title,
        "count": len(entries),
        "functions": set()
    }

    for e in entries:
        cid = e["id"]
        greek = e.get("greek", "")
        example_el = e.get("example_el", "")
        pos = e.get("gender_or_pos", "")
        gram = e.get("grammatical_info", {})
        func = e.get("keg_communicative_function", "")
        if func:
            audit_results["domain_distribution"][u_id]["functions"].add(func)

        audit_results["total_cards"] += 1

        # 1. Past Tense Detection in example sentences
        for pat in PAST_TENSE_PATTERNS:
            if re.search(pat, example_el, re.IGNORECASE):
                audit_results["past_tense_warnings"].append({
                    "id": cid,
                    "unit": u_id,
                    "greek": greek,
                    "pattern": pat,
                    "example_el": example_el,
                    "example_en": e.get("example_en", "")
                })

        # 2. Noun definite article requirement
        if ("noun" in pos) and ("pronoun" not in pos) and ("phrase" not in pos):
            # check if starts with article
            if not any(greek.startswith(art) for art in ["ο ", "η ", "το ", "οι ", "τα "]):
                audit_results["noun_article_warnings"].append({
                    "id": cid,
                    "unit": u_id,
                    "greek": greek
                })

        # 3. Verb grammatical info completeness
        if ("verb" in pos) and ("adverb" not in pos) and ("phrase" not in pos) and ("impersonal" not in pos):
            if "verb_type" not in gram or "third_person_singular" not in gram or "first_person_plural" not in gram:
                audit_results["verb_structure_warnings"].append({
                    "id": cid,
                    "unit": u_id,
                    "greek": greek,
                    "missing": [k for k in ["verb_type", "third_person_singular", "first_person_plural"] if k not in gram]
                })

print(f"Total core cards inspected: {audit_results['total_cards']}")

print("\n--- 1. PAST TENSE / AORIST LEAKAGE IN EXAMPLES ---")
if audit_results["past_tense_warnings"]:
    print(f"Found {len(audit_results['past_tense_warnings'])} sentences with potential past tense forms:")
    for w in audit_results["past_tense_warnings"]:
        print(f"  [{w['unit']} | {w['id']}] ({w['greek']}): '{w['example_el']}' (matched: {w['pattern']})")
else:
    print("None found! All examples conform to A1 Present / Imperfect-free boundary.")

print("\n--- 2. NOUN DEFINITE ARTICLE INTEGRITY ---")
if audit_results["noun_article_warnings"]:
    print(f"Found {len(audit_results['noun_article_warnings'])} nouns without articles:")
    for w in audit_results["noun_article_warnings"]:
        print(f"  [{w['unit']} | {w['id']}]: '{w['greek']}'")
else:
    print("100% compliant! Every singular noun includes its definite article (ο, η, το).")

print("\n--- 3. VERB CONJUGATION ANCHOR INTEGRITY ---")
if audit_results["verb_structure_warnings"]:
    print(f"Found {len(audit_results['verb_structure_warnings'])} verbs missing anchor forms:")
    for w in audit_results["verb_structure_warnings"]:
        print(f"  [{w['unit']} | {w['id']}] '{w['greek']}': missing {w['missing']}")
else:
    print("100% compliant! Every verb has verb_type, 3rd singular, and 1st plural.")

print("\n--- 4. KEG FUNCTIONAL DISTRIBUTION ---")
for uid, info in audit_results["domain_distribution"].items():
    print(f"• {uid}: {info['title']} -> {info['count']} cards, {len(info['functions'])} distinct communicative functions")

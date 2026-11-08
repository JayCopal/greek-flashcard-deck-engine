# -*- coding: utf-8 -*-
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

core_unit_ids = [f"unit-{i:02d}" for i in range(13)]

# Search for passive/mediopassive endings in cards (excluding accepted A1 lexicalized items like λέγομαι, βρίσκομαι, χρειάζομαι, εργάζομαι)
ACCEPTED_PASSIVES = {
    "λέγομαι", "βρίσκομαι", "βρίσκεται", "βρίσκονται", "χρειάζομαι", "εργάζομαι", "συναντιόμαστε", "ενοικιάζεται", "πωλείται"
}

warnings_passive = []

for u_entry in manifest.get("units", []):
    u_id = u_entry["id"]
    if u_id not in core_unit_ids:
        continue
    rel_file = u_entry["lessons"][0]["file"]
    yaml_path = CONTENT_DIR / rel_file
    with open(yaml_path, "r", encoding="utf-8") as f:
        ydata = yaml.safe_load(f)
    for e in ydata.get("entries", []):
        ex = e.get("example_el", "")
        grk = e.get("greek", "")
        # Check if card itself is a passive verb not in accepted list
        pos = e.get("gender_or_pos", "")
        if "verb" in pos:
            if grk.endswith("μαι") and grk not in ACCEPTED_PASSIVES:
                warnings_passive.append({
                    "unit": u_id,
                    "id": e["id"],
                    "greek": grk,
                    "type": "headword passive",
                    "ex": ex
                })
        # Check words ending in -ηκα, -ηκε, -ηκαν (aorist passive) in examples
        m = re.findall(r"\b\w+(?:ήθηκα|ήθηκε|ήστηκα|ήστηκε|ηκα|ηκες|ηκε|ηκαμε|ηκαν)\b", ex, re.IGNORECASE)
        # filter out false matches like 'γυναίκα', 'δίκη', etc.
        verb_m = [w for w in m if not w.endswith("κα") or w in ["ξεκουράστηκα", "σηκώθηκα", "κοιμήθηκα", "γεννήθηκα", "χάθηκα"]]
        if verb_m:
            warnings_passive.append({
                "unit": u_id,
                "id": e["id"],
                "greek": grk,
                "type": f"aorist passive in example: {verb_m}",
                "ex": ex
            })

print(f"Total passive anomalies detected: {len(warnings_passive)}")
for w in warnings_passive:
    print(f"  [{w['unit']} | {w['id']}] ({w['greek']}): {w['type']} -> '{w['ex']}'")

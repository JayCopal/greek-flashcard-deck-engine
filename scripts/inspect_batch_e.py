# -*- coding: utf-8 -*-
import sys
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

yp = BASE_DIR / "content" / "unit-00" / "lesson-01.yaml"
with open(yp, "r", encoding="utf-8") as f:
    yd = yaml.safe_load(f)

out_lines = [f"# unit-00 ({len(yd['entries'])} cards)"]
for e in yd["entries"]:
    cid = e["id"]
    grk = e["greek"]
    ex1 = e.get("example_el", "")
    en1 = e.get("example_en", "")
    out_lines.append(f"{cid} | {grk} | {ex1} | {en1}")

with open(BASE_DIR / "scripts" / "batch_e_cards.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out_lines))
print("Wrote batch_e_cards.txt successfully")

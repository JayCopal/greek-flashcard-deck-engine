# -*- coding: utf-8 -*-
import json
import sys

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

with open("public/data/deck.json", "r", encoding="utf-8") as f:
    deck = json.load(f)

print(f"Total units in deck: {len(deck.get('units', []))}")
for u in deck.get("units", []):
    if u["id"].startswith("unit-1"):
        l = u["lessons"][0]
        entries = l.get("entries", [])
        sample_id = entries[0]["id"] if entries else "EMPTY"
        sample_greek = entries[0]["greek"] if entries else ""
        print(f"{u['id']:10} | order: {u.get('order'):13} | cards: {len(entries):3} | sample: {sample_id:12} | {sample_greek[:25]}")

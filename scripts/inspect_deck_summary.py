# -*- coding: utf-8 -*-
import sys
import yaml

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

with open("content/manifest.yaml", "r", encoding="utf-8") as f:
    manifest = yaml.safe_load(f)

units = manifest.get("units", [])
print(f"Total units in manifest: {len(units)}")

p1 = [u for u in units if "KEG-A2-P1" in u.get("order", "")]
p2 = [u for u in units if "KEG-A2-P2" in u.get("order", "")]

print(f"\n--- Part 1 Units (Count: {len(p1)}) ---")
for u in p1:
    print(f"  [{u['id']}] {u.get('order')} - {u.get('title')[:55]}")

print(f"\n--- Part 2 Units (Count: {len(p2)}) ---")
for u in p2:
    print(f"  [{u['id']}] {u.get('order')} - {u.get('title')[:55]}")

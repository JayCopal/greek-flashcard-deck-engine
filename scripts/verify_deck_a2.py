# -*- coding: utf-8 -*-
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from server.main import get_deck

deck = get_deck()
print(f"Total units in deck: {len(deck['units'])}")
a2_units = [u for u in deck['units'] if 'A2' in u.get('order', '') or 'a2' in u.get('id', '')]
print(f"Total A2 units found: {len(a2_units)}")

total_a2_cards = 0
for u in a2_units:
    entries = u['lessons'][0]['entries'] if u.get('lessons') else []
    total_a2_cards += len(entries)
    print(f"  [{u['id']}] {u['order']} - {u['title'][:55]}... ({len(entries)} cards)")

print(f"\nTotal A2 Cards: {total_a2_cards}")

import json
from pathlib import Path
from collections import defaultdict

BASE_DIR = Path(__file__).resolve().parent.parent
deck_file = BASE_DIR / "public" / "data" / "deck.json"
audio_dir = BASE_DIR / "audio"

with open(deck_file, "r", encoding="utf-8") as f:
    deck = json.load(f)

groups = defaultdict(lambda: {"units": 0, "cards": 0, "audio_ok": 0, "audio_total": 0, "unit_list": []})

for u in deck.get("units", []):
    order = u.get("order", "")
    unit_id = u.get("id", "")
    
    # Identify group tag
    if order.startswith("KEG-A2-P1"):
        grp = "KEG-A2-P1"
    elif order.startswith("KEG-A2-P2"):
        grp = "KEG-A2-P2"
    elif order.startswith("KEG-A2-WR-P1"):
        grp = "KEG-A2-WR-P1"
    elif order.startswith("KEG-A2-WR-P2"):
        grp = "KEG-A2-WR-P2"
    elif order.startswith("SP-") or "sp" in unit_id:
        grp = "KEG-A2-SP"
    elif order.startswith("KEG-A1") or order.startswith("OG-"):
        grp = "KEG-A1"
    elif order.startswith("KlikA1") or order.startswith("Klik-A1") or "10" in str(order):
        grp = "Klik-A1"
    elif order.startswith("KlikA2") or order.startswith("Klik-A2") or "20" in str(order):
        grp = "Klik-A2"
    elif order.startswith("CYP"):
        grp = "CYP-Exam"
    else:
        grp = "Other"

    cards = sum(len(l.get("entries", [])) for l in u.get("lessons", []))
    groups[grp]["units"] += 1
    groups[grp]["cards"] += cards
    groups[grp]["unit_list"].append((unit_id, order, cards))

    for l in u.get("lessons", []):
        for e in l.get("entries", []):
            groups[grp]["audio_total"] += 1
            af = e.get("audio")
            if af and (audio_dir / af).exists():
                groups[grp]["audio_ok"] += 1

print(f"{'Group':<16} | {'Units':<6} | {'Cards':<6} | {'Audio verified':<14} | {'Coverage':<8}")
print("-" * 60)
for grp, data in sorted(groups.items()):
    cov = f"{data['audio_ok'] / data['audio_total'] * 100:.1f}%" if data['audio_total'] > 0 else "N/A"
    print(f"{grp:<16} | {data['units']:<6} | {data['cards']:<6} | {data['audio_ok']}/{data['audio_total']:<10} | {cov:<8}")

import os
import sys
import yaml
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Import general cards from batch scripts
from scripts.create_keg_a2_batch_3 import CARDS_U06
from scripts.create_keg_a2_batch_4 import CARDS_U07, CARDS_U08
from scripts.create_keg_a2_batch_5 import CARDS_U09, CARDS_U10
from scripts.create_keg_a2_batch_6 import CARDS_U11
from server.tts_service import generate_audio_filename

def ensure_card_audio(card):
    greek = card['greek']
    ex1 = card.get('example_el', '')
    ex2 = card.get('example2_el', '')
    
    card['audio'] = generate_audio_filename(greek)
    card['status'] = 'verified'
    if ex1:
        card['example_audio'] = generate_audio_filename(ex1)
    if ex2:
        card['example2_audio'] = generate_audio_filename(ex2)
    return card

def step1_migrate_writing_and_restore_general():
    print("=== Step 1: Extracting current writing cards ===")
    writing_cards_map = {}
    for i in range(6, 12):
        uid = f"unit-a2-{i:02d}"
        path = BASE_DIR / "content" / uid / "lesson-01.yaml"
        if path.exists():
            with open(path, 'r', encoding='utf-8') as f:
                writing_cards_map[uid] = yaml.safe_load(f)
            print(f"Loaded {len(writing_cards_map[uid].get('entries', []))} cards from {uid}")

    # Now create content/unit-wr2-01 to 06
    print("\n=== Step 2: Creating KEG-A2-WR-P2 (Writing Part 2) ===")
    wr2_units = [
        {
            "dir": "unit-wr2-01",
            "unit_id": "unit-wr2-01",
            "order": "KEG-A2-WR-P2-01-A",
            "title": "Μάθημα 1: Προσκλήσεις & Κοινωνικές Εκδηλώσεις (Task 1: Invitations & Celebrations)",
            "description": "Mastering Task 1 notes: composing and replying to party, birthday, and celebration invitations, accepting or politely declining with justifications.",
            "source_uid": None # we will generate 10 fresh playbook cards
        },
        {
            "dir": "unit-wr2-02",
            "unit_id": "unit-wr2-02",
            "order": "KEG-A2-WR-P2-02-A",
            "title": writing_cards_map["unit-a2-07"]["title"],
            "description": writing_cards_map["unit-a2-07"]["description"],
            "source_uid": "unit-a2-07"
        },
        {
            "dir": "unit-wr2-03",
            "unit_id": "unit-wr2-03",
            "order": "KEG-A2-WR-P2-03-A",
            "title": writing_cards_map["unit-a2-08"]["title"],
            "description": writing_cards_map["unit-a2-08"]["description"],
            "source_uid": "unit-a2-08"
        },
        {
            "dir": "unit-wr2-04",
            "unit_id": "unit-wr2-04",
            "order": "KEG-A2-WR-P2-04-A",
            "title": writing_cards_map["unit-a2-06"]["title"],
            "description": writing_cards_map["unit-a2-06"]["description"],
            "source_uid": "unit-a2-06"
        },
        {
            "dir": "unit-wr2-05",
            "unit_id": "unit-wr2-05",
            "order": "KEG-A2-WR-P2-05-A",
            "title": writing_cards_map["unit-a2-09"]["title"],
            "description": writing_cards_map["unit-a2-09"]["description"],
            "source_uid": "unit-a2-09"
        },
        {
            "dir": "unit-wr2-06",
            "unit_id": "unit-wr2-06",
            "order": "KEG-A2-WR-P2-06-A",
            "title": writing_cards_map["unit-a2-11"]["title"],
            "description": writing_cards_map["unit-a2-11"]["description"],
            "source_uid": "unit-a2-11"
        }
    ]

    for u in wr2_units:
        target_dir = BASE_DIR / "content" / u["dir"]
        target_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_dir / "lesson-01.yaml"
        
        if u["source_uid"]:
            src_data = writing_cards_map[u["source_uid"]]
            src_data["unit_id"] = u["unit_id"]
            src_data["title"] = u["title"]
            src_data["description"] = u["description"]
            with open(target_file, "w", encoding="utf-8") as f:
                yaml.dump(src_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
            print(f"Created {u['dir']} from {u['source_uid']} ({len(src_data.get('entries', []))} cards)")
        else:
            # Generate playbook 1 cards for unit-wr2-01
            pass # will handle in script part 2

    # Step 3: Now restore unit-a2-06 to 11 with general vocabulary
    print("\n=== Step 3: Restoring General A2 Part 1 (unit-a2-06 to 11) ===")
    general_restorations = [
        {
            "uid": "unit-a2-06",
            "title": "Μάθημα 6: Συναλλαγές, Τράπεζα, Ταχυδρομείο & Δημόσιες Υπηρεσίες (Banking, Post Office & Public Services)",
            "description": "Navigating banking counters, ATM withdrawals, postal package dispatches, utility bills, and Citizens' Service Centers (ΚΕΠ) using polite imperatives (περάστε, περιμένετε, δείξτε μου, δώστε μου) and administrative formulas.",
            "notes": """Unit A2-06 Core Notes: Συναλλαγές, Τράπεζα & Δημόσιες Υπηρεσίες (Public Services & Transactions)
• Civic & Administrative Environments:
  - Η τράπεζα: λογαριασμός (account), κατάθεση (deposit), ανάληψη (withdrawal), ΑΤΜ, υπόλοιπο (balance).
  - Το ταχυδρομείο (ΕΛΤΑ): δέμα (parcel), γραμματόσημο (stamp), συστημένο (registered mail).
  - Το ΚΕΠ (Κέντρο Εξυπηρέτησης Πολιτών): αίτηση (application), πιστοποιητικό (certificate), βεβαίωση (attestation), γνήσιο υπογραφής (signature legalization).
• Imperative Directives in Public Counters:
  - Περάστε (step forward), Περιμένετε (wait), Δείξτε μου (show me), Δώστε μου (give me), Υπογράψτε (sign).""",
            "cards": CARDS_U06
        },
        {
            "uid": "unit-a2-07",
            "title": "Μάθημα 7: Ταξίδια, Διακοπές & Κρατήσεις (Travel, Vacations & Reservations)",
            "description": "Making hotel and transport bookings, discussing departure and arrival schedules, and comparing prices and travel duration using comparative adjectives (πιο, καλύτερος, φθηνότερος, ακριβότερος, γρηγορότερος).",
            "notes": """Unit A2-07 Core Notes: Ταξίδια, Διακοπές & Κρατήσεις (Travel & Bookings)
• Travel Logistics:
  - Διαμονή: δίκλινο δωμάτιο (double room), μονόκλινο (single), θέα στη θάλασσα (sea view), πρωινό (breakfast).
  - Μετακινήσεις: δρομολόγιο (schedule), καθυστέρηση (delay), ακύρωση (cancellation), επιστροφή (return).
• Comparative Adjectives & Adverbs:
  - πιο + adjective + από (πιο γρήγορος από το λεωφορείο).
  - Irregular comparatives: καλύτερος (better), χειρότερος (worse), μεγαλύτερος (bigger/older), μικρότερος (smaller/younger).""",
            "cards": CARDS_U07
        },
        {
            "uid": "unit-a2-08",
            "title": "Μάθημα 8: Καιρός, Φύση & Γεωγραφία της Ελλάδας (Weather, Nature & Geography)",
            "description": "Interpreting weather bulletins, seasonal forecasts, and maritime Beaufort scales, describing Greek geography (mountains, islands, rivers, lakes), and mastering adjectives in -ύς, -ιά, -ύ (βαθύς, βαρύς, ελαφρύς, πλατύς).",
            "notes": """Unit A2-08 Core Notes: Καιρός, Φύση & Γεωγραφία (Weather & Greek Geography)
• Weather Forecast Terminology:
  - θερμοκρασία (temperature), βροχή (rain), καταιγίδα (storm), χιόνι (snow), άνεμος (wind), μποφόρ (Beaufort).
  - αίθριος καιρός (clear skies), νεφώσεις (cloud cover), υγρασία (humidity).
• Adjectives in -ύς, -ιά, -ύ:
  - βαθύς/βαθιά/βαθύ (deep), βαρύς/βαριά/βαρύ (heavy), ελαφρύς/ελαφριά/ελαφρύ (light), πλατύς/πλατιά/πλατύ (wide).""",
            "cards": CARDS_U08
        },
        {
            "uid": "unit-a2-09",
            "title": "Μάθημα 9: Εργασία, Επαγγέλματα & Αγγελίες (Workplaces, CVs & Classified Ads)",
            "description": "Navigating job advertisements, employment contracts, working conditions, and interview questions using Type 1 Conditionals (αν + ενεστώτας -> μέλλοντας) and temporal connectives (μόλις, αφού, πριν).",
            "notes": """Unit A2-09 Core Notes: Εργασία & Επαγγέλματα (Work & Employment)
• Workplace Vocabulary:
  - βιογραφικό (CV), συνέντευξη (interview), μισθός (salary), ωράριο (working hours), άδεια (leave/vacation).
  - σύμβαση (contract), προϋπηρεσία (previous experience), προσόντα (qualifications).
• Type 1 Conditionals:
  - Αν + Present -> Future / Imperative: «Αν με προσλάβετε, θα δουλέψω σκληρά.»""",
            "cards": CARDS_U09
        },
        {
            "uid": "unit-a2-10",
            "title": "Μάθημα 10: Υγεία, Ατυχήματα & Φαρμακείο (Health, Accidents & Medical Consultation)",
            "description": "Explaining bodily symptoms, consulting doctors and pharmacists, following medical prescriptions, and reporting emergencies using mediopassive verbs (αισθάνομαι, κουράζομαι, τραυματίζομαι) and anatomy vocabulary.",
            "notes": """Unit A2-10 Core Notes: Υγεία & Φαρμακείο (Health & Medicine)
• Anatomy & Symptoms:
  - πυρετός (fever), πονοκέφαλος (headache), πονόλαιμος (sore throat), βήχας (cough), κρυολόγημα (cold), γρίπη (flu).
  - πονάει το... / πονάνε τα... (my ... hurts).
• Mediopassive Health Verbs:
  - αισθάνομαι (feel), κουράζομαι (get tired), τραυματίζομαι (get injured), κοιμάμαι (sleep).""",
            "cards": CARDS_U10
        },
        {
            "uid": "unit-a2-11",
            "title": "Μάθημα 11: Πολιτισμός, ΜΜΕ & Ψηφιακή Ζωή (Culture, Media & Digital Life)",
            "description": "Engaging with Greek cinema, theater, news, digital platforms, and internet communication, using neuter third-declension nouns in -ος / -ους (το λάθος, το μέρος, το κόστος) and relative pronouns (που, ο οποίος).",
            "notes": """Unit A2-11 Core Notes: Πολιτισμός & Ψηφιακή Ζωή (Culture & Digital Media)
• Cultural Events & Media:
  - θέατρο (theater), παράσταση (performance), εισιτήρια (tickets), συναυλία (concert), έκθεση (exhibition).
  - διαδίκτυο (internet), εφαρμογή (app), κοινωνικά δίκτυα (social media), μήνυμα (message).
• Neuter Nouns in -ος / -ους:
  - το λάθος / τα λάθη (mistake), το μέρος / τα μέρη (place), το κόστος (cost), το κράτος (state).""",
            "cards": CARDS_U11
        }
    ]

    for item in general_restorations:
        uid = item["uid"]
        target_file = BASE_DIR / "content" / uid / "lesson-01.yaml"
        # ensure all cards have audio filename and verified status
        prepared_cards = [ensure_card_audio(dict(c)) for c in item["cards"]]
        
        lesson_data = {
            "unit_id": uid,
            "lesson_id": "lesson-01",
            "title": item["title"],
            "description": item["description"],
            "lesson_status": "not_started",
            "lesson_notes": item["notes"],
            "entries": prepared_cards
        }
        with open(target_file, "w", encoding="utf-8") as f:
            yaml.dump(lesson_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        print(f"Restored {uid} with {len(prepared_cards)} general cards.")

if __name__ == '__main__':
    step1_migrate_writing_and_restore_general()

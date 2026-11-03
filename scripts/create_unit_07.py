# -*- coding: utf-8 -*-
"""
Script to create Unit 7: Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)
Strictly conforming to docs/LESSON_CREATION_GUIDE.md and KEG A1 Standards.
"""
import sys
import json
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
UNIT_DIR = CONTENT_DIR / "unit-07"
UNIT_DIR.mkdir(parents=True, exist_ok=True)
YAML_PATH = UNIT_DIR / "lesson-01.yaml"
JSON_PATH = CONTENT_DIR / "keg_a1_units_07.json"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

cards_u7 = [
    # 1. Types of Residences & Buildings
    {
        "id": "A1-U07-001",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "το σπίτι",
        "back_primary": "house / home",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα σπίτια",
            "accusative_singular": "το σπίτι"
        },
        "keg_communicative_function": "Describing one's residence and home",
        "example_el": "Μένω σε ένα παλιό αλλά όμορφο σπίτι.",
        "example_en": "I live in an old but beautiful house.",
        "notes_or_mnemonics": "Paroxytone neuter in -ι (plural: τα σπίτια). 'Στο σπίτι' means both 'at home' and 'in the house'."
    },
    {
        "id": "A1-U07-002",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "το διαμέρισμα",
        "back_primary": "apartment / flat",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα διαμερίσματα",
            "accusative_singular": "το διαμέρισμα"
        },
        "keg_communicative_function": "Describing apartment living and reading housing ads",
        "example_el": "Ψάχνω ένα διαμέρισμα με δύο δωμάτια στο κέντρο.",
        "example_en": "I am looking for a two-room apartment in the city center.",
        "notes_or_mnemonics": "Neuter in -μα with plural in -ματα (τα διαμερίσματα). Key term in classified real estate ads (αγγελίες)."
    },
    {
        "id": "A1-U07-003",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "η πολυκατοικία",
        "back_primary": "apartment building / block of flats",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πολυκατοικίες",
            "accusative_singular": "την πολυκατοικία"
        },
        "keg_communicative_function": "Identifying building types in urban neighborhoods",
        "example_el": "Η πολυκατοικία μας έχει έξι ορόφους.",
        "example_en": "Our apartment building has six floors.",
        "notes_or_mnemonics": "Compound from πολύς (many) + κατοικία (dwelling/residence). Paroxytone feminine in -ία."
    },
    {
        "id": "A1-U07-004",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "το δωμάτιο",
        "back_primary": "room (in a house or hotel)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα δωμάτια",
            "accusative_singular": "το δωμάτιο"
        },
        "keg_communicative_function": "Specifying number of rooms or booking hotel rooms",
        "example_el": "Θέλω ένα δίκλινο δωμάτιο με θέα στη θάλασσα.",
        "example_en": "I want a double room with a sea view.",
        "notes_or_mnemonics": "Proparoxytone neuter in -ιο (plural: τα δωμάτια). Double room = δίκλινο, single room = μονόκλινο."
    },
    {
        "id": "A1-U07-005",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "το ξενοδοχείο",
        "back_primary": "hotel",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ξενοδοχεία",
            "accusative_singular": "το ξενοδοχείο"
        },
        "keg_communicative_function": "Inquiring about tourist lodging and reservations",
        "example_el": "Το ξενοδοχείο είναι πολύ κοντά στο μετρό.",
        "example_en": "The hotel is very close to the metro.",
        "notes_or_mnemonics": "Compound from ξένος (stranger/guest) + δέχομαι (to receive). Neuter in -είο."
    },
    {
        "id": "A1-U07-006",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "ο όροφος",
        "back_primary": "floor / storey",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι όροφοι",
            "accusative_singular": "τον όροφο"
        },
        "keg_communicative_function": "Stating apartment floor level in addresses or housing ads",
        "example_el": "Μένουμε στον δεύτερο όροφο.",
        "example_en": "We live on the second floor.",
        "notes_or_mnemonics": "Proparoxytone masculine in -ος (accusative: τον όροφο). 1st floor = πρώτος όροφος, 2nd = δεύτερος όροφος."
    },
    {
        "id": "A1-U07-007",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "το ισόγειο",
        "back_primary": "ground floor",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ισόγεια",
            "accusative_singular": "το ισόγειο"
        },
        "keg_communicative_function": "Describing ground level premises or apartment floors",
        "example_el": "Το φαρμακείο είναι στο ισόγειο.",
        "example_en": "The pharmacy is on the ground floor.",
        "notes_or_mnemonics": "Compound from ίσος (equal/level) + γη (earth). Neuter in -ειο (στο ισόγειο)."
    },
    {
        "id": "A1-U07-008",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "το μπαλκόνι",
        "back_primary": "balcony",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μπαλκόνια",
            "accusative_singular": "το μπαλκόνι"
        },
        "keg_communicative_function": "Describing outdoor spaces of an apartment",
        "example_el": "Το διαμέρισμα έχει ένα μεγάλο φωτεινό μπαλκόνι.",
        "example_en": "The apartment has a large sunny balcony.",
        "notes_or_mnemonics": "Paroxytone neuter in -ι (plural: τα μπαλκόνια). Essential feature in Greek housing culture."
    },
    {
        "id": "A1-U07-009",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "ο κήπος",
        "back_primary": "garden / yard",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι κήποι",
            "accusative_singular": "τον κήπο"
        },
        "keg_communicative_function": "Describing gardens and outdoor residential areas",
        "example_el": "Τα παιδιά παίζουν στον κήπο.",
        "example_en": "The children are playing in the garden.",
        "notes_or_mnemonics": "Paroxytone masculine in -ος (accusative: τον κήπο)."
    },

    # 2. Rooms & Parts of the Home
    {
        "id": "A1-U07-010",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "το σαλόνι",
        "back_primary": "living room / sitting room",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα σαλόνια",
            "accusative_singular": "το σαλόνι"
        },
        "keg_communicative_function": "Describing the main living and entertaining room",
        "example_el": "Καθόμαστε στο σαλόνι και βλέπουμε τηλεόραση.",
        "example_en": "We sit in the living room and watch television.",
        "notes_or_mnemonics": "Paroxytone neuter in -ι (plural: τα σαλόνια)."
    },
    {
        "id": "A1-U07-011",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "η κουζίνα",
        "back_primary": "kitchen / cooking stove",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι κουζίνες",
            "accusative_singular": "την κουζίνα"
        },
        "keg_communicative_function": "Referring to the kitchen area or the cooking appliance",
        "example_el": "Μαγειρεύω στην κουζίνα κάθε μεσημέρι.",
        "example_en": "I cook in the kitchen every afternoon.",
        "notes_or_mnemonics": "Feminine in -α (plural: οι κουζίνες). Refers both to the room and the cooking appliance (η ηλεκτρική κουζίνα)."
    },
    {
        "id": "A1-U07-012",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "η κρεβατοκάμαρα",
        "back_primary": "bedroom / master bedroom",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι κρεβατοκάμαρες",
            "accusative_singular": "την κρεβατοκάμαρα"
        },
        "keg_communicative_function": "Describing sleeping quarters in a home",
        "example_el": "Η κρεβατοκάμαρα έχει ένα μεγάλο διπλό κρεβάτι.",
        "example_en": "The bedroom has a large double bed.",
        "notes_or_mnemonics": "Compound from κρεβάτι (bed) + κάμαρα (room). Synonym: το υπνοδωμάτιο."
    },
    {
        "id": "A1-U07-013",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "το μπάνιο",
        "back_primary": "bathroom / bath",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μπάνια",
            "accusative_singular": "το μπάνιο"
        },
        "keg_communicative_function": "Inquiring about bathroom facilities in accommodation",
        "example_el": "Πού είναι το μπάνιο, παρακαλώ;",
        "example_en": "Where is the bathroom, please?",
        "notes_or_mnemonics": "Neuter in -ιο. Also used idiomatically for swimming in the sea: 'κάνω μπάνιο' (to take a bath / to swim)."
    },
    {
        "id": "A1-U07-014",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "ο διάδρομος",
        "back_primary": "hallway / corridor",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι διάδρομοι",
            "accusative_singular": "τον διάδρομο"
        },
        "keg_communicative_function": "Giving directions inside an apartment or hotel",
        "example_el": "Το μπάνιο είναι στο τέλος του διαδρόμου.",
        "example_en": "The bathroom is at the end of the hallway.",
        "notes_or_mnemonics": "Proparoxytone masculine in -ος (accusative: τον διάδρομο)."
    },
    {
        "id": "A1-U07-015",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "η πόρτα",
        "back_primary": "door",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πόρτες",
            "accusative_singular": "την πόρτα"
        },
        "keg_communicative_function": "Referring to home entrances and doors",
        "example_el": "Κλείνω την πόρτα του σπιτιού με το κλειδί.",
        "example_en": "I lock the door of the house with the key.",
        "notes_or_mnemonics": "Paroxytone feminine in -α with plural in -ες (οι πόρτες)."
    },
    {
        "id": "A1-U07-016",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "το παράθυρο",
        "back_primary": "window",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα παράθυρα",
            "accusative_singular": "το παράθυρο"
        },
        "keg_communicative_function": "Describing rooms with natural light and ventilation",
        "example_el": "Ανοίγω το παράθυρο για φρέσκο αέρα.",
        "example_en": "I open the window for fresh air.",
        "notes_or_mnemonics": "Proparoxytone neuter in -ο (plural: τα παράθυρα)."
    },

    # 3. Furniture & Appliances
    {
        "id": "A1-U07-017",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "το έπιπλο",
        "back_primary": "piece of furniture (plural: furniture)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα έπιπλα",
            "accusative_singular": "το έπιπλο"
        },
        "keg_communicative_function": "Talking about home furnishings and interior decor",
        "example_el": "Αγοράζουμε νέα έπιπλα για το σαλόνι.",
        "example_en": "We are buying new furniture for the living room.",
        "notes_or_mnemonics": "Proparoxytone neuter in -ο. English 'furniture' is uncountable, but Greek uses plural 'τα έπιπλα'."
    },
    {
        "id": "A1-U07-018",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "το κρεβάτι",
        "back_primary": "bed",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κρεβάτια",
            "accusative_singular": "το κρεβάτι"
        },
        "keg_communicative_function": "Describing bedroom furniture and hotel room types",
        "example_el": "Το κρεβάτι είναι πολύ αναπαυτικό.",
        "example_en": "The bed is very comfortable.",
        "notes_or_mnemonics": "Paroxytone neuter in -ι (plural: τα κρεβάτια). 'Πάω για ύπνο στο κρεβάτι' = I go to sleep in bed."
    },
    {
        "id": "A1-U07-019",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "ο καναπές",
        "back_primary": "sofa / couch",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι καναπέδες",
            "accusative_singular": "τον καναπέ"
        },
        "keg_communicative_function": "Describing living room seating",
        "example_el": "Ξεκουράζομαι στον καναπέ μετά τη δουλειά.",
        "example_en": "I rest on the sofa after work.",
        "notes_or_mnemonics": "Oxytone masculine in -ές (plural: οι καναπέδες, accusative: τον καναπέ)."
    },
    {
        "id": "A1-U07-020",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "η πολυθρόνα",
        "back_primary": "armchair",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πολυθρόνες",
            "accusative_singular": "την πολυθρόνα"
        },
        "keg_communicative_function": "Describing comfortable seating in living rooms",
        "example_el": "Διαβάζω ένα βιβλίο στην πολυθρόνα.",
        "example_en": "I am reading a book in the armchair.",
        "notes_or_mnemonics": "Compound from πολύς (much) + θρόνος (throne). Paroxytone feminine in -α."
    },
    {
        "id": "A1-U07-021",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "η καρέκλα",
        "back_primary": "chair",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι καρέκλες",
            "accusative_singular": "την καρέκλα"
        },
        "keg_communicative_function": "Asking for chairs or arranging dining seating",
        "example_el": "Χρειαζόμαστε άλλη μία καρέκλα για το τραπέζι.",
        "example_en": "We need another chair for the table.",
        "notes_or_mnemonics": "Paroxytone feminine in -α with plural in -ες (οι καρέκλες)."
    },
    {
        "id": "A1-U07-022",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "η ντουλάπα",
        "back_primary": "wardrobe / closet",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ντουλάπες",
            "accusative_singular": "την ντουλάπα"
        },
        "keg_communicative_function": "Describing bedroom storage and closet space",
        "example_el": "Βάζω τα ρούχα μου στην ντουλάπα.",
        "example_en": "I put my clothes in the wardrobe.",
        "notes_or_mnemonics": "Feminine in -α. In Greek apartments, 'εντοιχισμένη ντουλάπα' denotes a built-in closet."
    },
    {
        "id": "A1-U07-023",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "το ψυγείο",
        "back_primary": "refrigerator / fridge",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ψυγεία",
            "accusative_singular": "το ψυγείο"
        },
        "keg_communicative_function": "Referring to essential kitchen appliances",
        "example_el": "Βάζω το γάλα και το τυρί στο ψυγείο.",
        "example_en": "I put the milk and cheese in the fridge.",
        "notes_or_mnemonics": "Paroxytone neuter in -είο (plural: τα ψυγεία). Derived from ψύχος (cold)."
    },
    {
        "id": "A1-U07-024",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "το πλυντήριο",
        "back_primary": "washing machine",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πλυντήρια",
            "accusative_singular": "το πλυντήριο"
        },
        "keg_communicative_function": "Describing household appliances in rental listings",
        "example_el": "Το διαμέρισμα διαθέτει πλυντήριο ρούχων.",
        "example_en": "The apartment features a washing machine.",
        "notes_or_mnemonics": "Proparoxytone neuter in -ιο. 'Πλυντήριο ρούχων' = clothes washer; 'πλυντήριο πιάτων' = dishwasher."
    },
    {
        "id": "A1-U07-025",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "η τηλεόραση",
        "back_primary": "television / TV set",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι τηλεοράσεις",
            "accusative_singular": "την τηλεόραση"
        },
        "keg_communicative_function": "Describing home entertainment and media devices",
        "example_el": "Βλέπουμε τις ειδήσεις στην τηλεόραση.",
        "example_en": "We watch the news on television.",
        "notes_or_mnemonics": "Feminine noun in -ση with plural in -σεις (οι τηλεοράσεις)."
    },
    {
        "id": "A1-U07-026",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "το φωτιστικό",
        "back_primary": "light fixture / lamp",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα φωτιστικά",
            "accusative_singular": "το φωτιστικό"
        },
        "keg_communicative_function": "Describing room lighting and fixtures",
        "example_el": "Υπάρχει ένα φωτιστικό πάνω στο γραφείο.",
        "example_en": "There is a lamp on the desk.",
        "notes_or_mnemonics": "Oxytone neuter in -ό (plural: τα φωτιστικά). Derived from φως (light)."
    },
    {
        "id": "A1-U07-027",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "το χαλί",
        "back_primary": "rug / carpet",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα χαλιά",
            "accusative_singular": "το χαλί"
        },
        "keg_communicative_function": "Describing floor coverings in home decoration",
        "example_el": "Στο σαλόνι έχουμε ένα μεγάλο κόκκινο χαλί.",
        "example_en": "In the living room we have a large red rug.",
        "notes_or_mnemonics": "Oxytone neuter in -ί (plural: τα χαλιά)."
    },

    # 4. Spatial Adverbs & Prepositions (Accusative Case Governed)
    {
        "id": "A1-U07-028",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "phrase",
        "front": "μέσα σε",
        "back_primary": "in / inside (+ Accusative)",
        "grammatical_info": {
            "part_of_speech": "phrase (spatial preposition)",
            "governs_case": "accusative with article (στο, στη, στον, στα, στις, στους)"
        },
        "keg_communicative_function": "Expressing position inside a space, container, or room",
        "example_el": "Τα κλειδιά είναι μέσα στην τσάντα μου.",
        "example_en": "The keys are inside my bag.",
        "notes_or_mnemonics": "Combines with contracted article: μέσα στο σπίτι, μέσα στο δωμάτιο."
    },
    {
        "id": "A1-U07-029",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "phrase",
        "front": "έξω από",
        "back_primary": "outside of (+ Accusative)",
        "grammatical_info": {
            "part_of_speech": "phrase (spatial preposition)",
            "governs_case": "accusative (από + τον, την, το, τους, τις, τα)"
        },
        "keg_communicative_function": "Expressing location outside a building or room",
        "example_el": "Περιμένω έξω από την πολυκατοικία.",
        "example_en": "I am waiting outside the apartment building.",
        "notes_or_mnemonics": "Direct antonym of 'μέσα σε'. Governs 'από + Accusative'."
    },
    {
        "id": "A1-U07-030",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "phrase",
        "front": "πάνω σε",
        "back_primary": "on / on top of (+ Accusative)",
        "grammatical_info": {
            "part_of_speech": "phrase (spatial preposition)",
            "governs_case": "accusative with article (στο, στη, στον, στα)"
        },
        "keg_communicative_function": "Describing objects resting on surfaces",
        "example_el": "Το βιβλίο είναι πάνω στο τραπέζι.",
        "example_en": "The book is on the table.",
        "notes_or_mnemonics": "Also used simply as 'πάνω στο τραπέζι'. Direct antonym of 'κάτω από'."
    },
    {
        "id": "A1-U07-031",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "phrase",
        "front": "κάτω από",
        "back_primary": "under / underneath (+ Accusative)",
        "grammatical_info": {
            "part_of_speech": "phrase (spatial preposition)",
            "governs_case": "accusative (από + article)"
        },
        "keg_communicative_function": "Describing objects positioned beneath surfaces",
        "example_el": "Η γάτα κοιμάται κάτω από το κρεβάτι.",
        "example_en": "The cat is sleeping under the bed.",
        "notes_or_mnemonics": "Governs 'από + Accusative' (κάτω από το τραπέζι)."
    },
    {
        "id": "A1-U07-032",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "phrase",
        "front": "δίπλα σε",
        "back_primary": "next to / beside (+ Accusative)",
        "grammatical_info": {
            "part_of_speech": "phrase (spatial preposition)",
            "governs_case": "accusative with article (στο, στη, στον, στα)"
        },
        "keg_communicative_function": "Describing adjacent positioning of furniture or buildings",
        "example_el": "Η πολυθρόνα είναι δίπλα στο παράθυρο.",
        "example_en": "The armchair is next to the window.",
        "notes_or_mnemonics": "Combines with 'σε + άρθρο': δίπλα στον καναπέ, δίπλα στην πόρτα."
    },
    {
        "id": "A1-U07-033",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "phrase",
        "front": "απέναντι από",
        "back_primary": "opposite / across from (+ Accusative)",
        "grammatical_info": {
            "part_of_speech": "phrase (spatial preposition)",
            "governs_case": "accusative (από + article)"
        },
        "keg_communicative_function": "Describing facing objects or buildings across the street",
        "example_el": "Το σούπερ μάρκετ είναι απέναντι από το σπίτι μου.",
        "example_en": "The supermarket is across from my house.",
        "notes_or_mnemonics": "Governs 'από + Accusative' (απέναντι από την τράπεζα)."
    },
    {
        "id": "A1-U07-034",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "phrase",
        "front": "μπροστά από",
        "back_primary": "in front of (+ Accusative)",
        "grammatical_info": {
            "part_of_speech": "phrase (spatial preposition)",
            "governs_case": "accusative (από + article)"
        },
        "keg_communicative_function": "Describing spatial placement in front of an object",
        "example_el": "Υπάρχει ένα μικρό τραπέζι μπροστά από τον καναπέ.",
        "example_en": "There is a small table in front of the sofa.",
        "notes_or_mnemonics": "Direct antonym of 'πίσω από'."
    },
    {
        "id": "A1-U07-035",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "phrase",
        "front": "πίσω από",
        "back_primary": "behind (+ Accusative)",
        "grammatical_info": {
            "part_of_speech": "phrase (spatial preposition)",
            "governs_case": "accusative (από + article)"
        },
        "keg_communicative_function": "Describing position behind an object or building",
        "example_el": "Ο κήπος είναι πίσω από την πολυκατοικία.",
        "example_en": "The garden is behind the apartment building.",
        "notes_or_mnemonics": "Governs 'από + Accusative' (πίσω από την πόρτα)."
    },
    {
        "id": "A1-U07-036",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "phrase",
        "front": "ανάμεσα σε",
        "back_primary": "between / among (+ Accusative)",
        "grammatical_info": {
            "part_of_speech": "phrase (spatial preposition)",
            "governs_case": "accusative with article (ανάμεσα στο... και στο...)"
        },
        "keg_communicative_function": "Describing intermediate positioning between two objects",
        "example_el": "Το κομοδίνο είναι ανάμεσα στα δύο κρεβάτια.",
        "example_en": "The nightstand is between the two beds.",
        "notes_or_mnemonics": "Formula: 'ανάμεσα σε + Accusative' or 'ανάμεσα στο Α και στο Β'."
    },

    # 5. Housing, Rental & Accommodation Vocabulary & Verbs
    {
        "id": "A1-U07-037",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "το ενοίκιο",
        "back_primary": "rent (monthly payment)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ενοίκια",
            "accusative_singular": "το ενοίκιο"
        },
        "keg_communicative_function": "Asking for and discussing rental prices in classified ads",
        "example_el": "Πόσο είναι το ενοίκιο τον μήνα;",
        "example_en": "How much is the rent per month?",
        "notes_or_mnemonics": "Proparoxytone neuter in -ιο (plural: τα ενοίκια). Essential classified ad term."
    },
    {
        "id": "A1-U07-038",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "το ασανσέρ",
        "back_primary": "elevator / lift",
        "grammatical_info": {
            "part_of_speech": "noun (neuter indeclinable)",
            "plural": "τα ασανσέρ",
            "accusative_singular": "το ασανσέρ"
        },
        "keg_communicative_function": "Checking building amenities in real estate listings",
        "example_el": "Η πολυκατοικία διαθέτει καινούριο ασανσέρ.",
        "example_en": "The apartment building has a new elevator.",
        "notes_or_mnemonics": "French loanword: indeclinable neuter (το ασανσέρ, τα ασανσέρ)."
    },
    {
        "id": "A1-U07-039",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "vocabulary",
        "front": "η θέρμανση",
        "back_primary": "heating / central heating",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι θερμάνσεις",
            "accusative_singular": "τη θέρμανση"
        },
        "keg_communicative_function": "Inquiring about heating systems (αυτόνομη / κεντρική)",
        "example_el": "Το σπίτι έχει αυτόνομη θέρμανση φυσικού αερίου.",
        "example_en": "The house has autonomous natural gas heating.",
        "notes_or_mnemonics": "Feminine noun in -ση. 'Αυτόνομη θέρμανση' (independent heating) vs 'κεντρική θέρμανση' (central heating)."
    },
    {
        "id": "A1-U07-040",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "verb",
        "front": "νοικιάζω",
        "back_primary": "to rent / to lease / I rent",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό νοικιάζει",
            "first_person_plural": "εμείς νοικιάζουμε"
        },
        "keg_communicative_function": "Talking about renting a house or apartment",
        "example_el": "Νοικιάζω ένα δυάρι στους Αμπελόκηπους.",
        "example_en": "I am renting a two-room apartment in Ambelokipi.",
        "notes_or_mnemonics": "Type A active verb. Means both 'to rent from someone' and 'to rent out to someone'."
    },
    {
        "id": "A1-U07-041",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "verb",
        "front": "υπάρχει / υπάρχουν",
        "back_primary": "there is / there are",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "υπάρχει (there is)",
            "first_person_plural": "υπάρχουν (there are - 3rd pl.)"
        },
        "keg_communicative_function": "Expressing existence and availability of rooms, amenities, or items",
        "example_el": "Στο σαλόνι υπάρχουν δύο μεγάλες πολυθρόνες.",
        "example_en": "In the living room there are two large armchairs.",
        "notes_or_mnemonics": "Existential construction. Singular: υπάρχει + singular noun; Plural: υπάρχουν + plural noun."
    },
    {
        "id": "A1-U07-042",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "adjective",
        "front": "φωτεινός, -ή, -ό",
        "back_primary": "bright / luminous / sunny",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "φωτεινή",
            "neuter": "φωτεινό",
            "plural": "φωτεινοί, φωτεινές, φωτεινά"
        },
        "keg_communicative_function": "Describing well-lit apartments and rooms",
        "example_el": "Είναι ένα πολύ φωτεινό διαμέρισμα με νότιο προσανατολισμό.",
        "example_en": "It is a very bright apartment with south-facing orientation.",
        "notes_or_mnemonics": "Oxytone regular adjective in -ός, -ή, -ό. Ubiquitous descriptor in Greek rental ads."
    },
    {
        "id": "A1-U07-043",
        "unit_number": 7,
        "unit_theme": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "card_type": "adjective",
        "front": "επιπλωμένος, -η, -ο",
        "back_primary": "furnished",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "επιπλωμένη",
            "neuter": "επιπλωμένο",
            "plural": "επιπλωμένοι, επιπλωμένες, επιπλωμένα"
        },
        "keg_communicative_function": "Identifying furnished accommodation in listings",
        "example_el": "Ενοικιάζεται επιπλωμένη γκαρσονιέρα στο κέντρο.",
        "example_en": "Furnished studio apartment for rent in the center.",
        "notes_or_mnemonics": "Participle used as adjective: επιπλωμένος, -η, -ο (from έπιπλο). Antonym: ανεπίπλωτος (unfurnished)."
    }
]

# 1. Write content/keg_a1_units_07.json
with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(cards_u7, f, ensure_ascii=False, indent=2)
print(f"[OK] Wrote {len(cards_u7)} cards to {JSON_PATH.name}")

# 2. Build entries for content/unit-07/lesson-01.yaml
lesson_entries = []
for c in cards_u7:
    entry = {
        "id": c["id"],
        "greek": c["front"],
        "phonetic_hint": "",
        "english": c["back_primary"],
        "notes": c.get("notes_or_mnemonics", ""),
        "gender_or_pos": c["grammatical_info"].get("part_of_speech", "phrase"),
        "audio": None,
        "status": "pending_tts",
        "example_el": c.get("example_el", ""),
        "example_en": c.get("example_en", ""),
        "grammatical_info": c.get("grammatical_info", {}),
        "keg_communicative_function": c.get("keg_communicative_function", "")
    }
    lesson_entries.append(entry)

lesson_notes_u7 = (
    "Unit 7 Core Grammar Notes:\n\n"
    "• Existential Construction 'υπάρχει / υπάρχουν':\n"
    "  - Singular: 'Υπάρχει ένα μεγάλο σαλόνι.' (There is a large living room.)\n"
    "  - Plural: 'Υπάρχουν δύο κρεβατοκάμαρες.' (There are two bedrooms.)\n"
    "  - Negative: 'Δεν υπάρχει ασανσέρ.' (There is no elevator.)\n\n"
    "• Spatial Prepositions & Adverbs (Governing Accusative):\n"
    "  - Governed by 'σε + άρθρο' (contracted): μέσα σε (inside), πάνω σε (on top of), δίπλα σε (next to), ανάμεσα σε (between).\n"
    "  - Governed by 'από + άρθρο': έξω από (outside of), κάτω από (under), απέναντι από (across from), μπροστά από (in front of), πίσω από (behind).\n\n"
    "• Definite Article Grid (Nominative & Accusative):\n"
    "  - Masculine: Nom: ο / οι — Acc: τον / τους\n"
    "  - Feminine:  Nom: η / οι — Acc: τη(ν) / τις\n"
    "  - Neuter:    Nom: το / τα — Acc: το / τα\n\n"
    "• Reading Housing Classified Ads (Αγγελίες Κατοικιών):\n"
    "  - ενοικιάζεται (for rent) / πωλείται (for sale)\n"
    "  - γκαρσονιέρα (studio flat), δυάρι (2-room flat), τριάρι (3-room flat)\n"
    "  - όροφος: 1ος (πρώτος), 2ος (δεύτερος), ισόγειο (ground floor)\n"
    "  - επιπλωμένο (furnished) / αυτόνομη θέρμανση (independent heating)"
)

yaml_payload = {
    "unit_id": "unit-07",
    "lesson_id": "lesson-01",
    "title": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
    "description": "CEFR A1: Describing an apartment, rooms of the house, core furniture, spatial prepositions, and understanding classified accommodation listings.",
    "lesson_status": "not_started",
    "lesson_notes": lesson_notes_u7,
    "entries": lesson_entries
}

with open(YAML_PATH, "w", encoding="utf-8") as f:
    yaml.dump(yaml_payload, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
print(f"[OK] Wrote {len(lesson_entries)} entries to {YAML_PATH.relative_to(BASE_DIR)}")

# 3. Update content/manifest.yaml if unit-07 is not already in manifest
with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = yaml.safe_load(f) or {}

existing_unit_ids = [u["id"] for u in manifest.get("units", [])]
if "unit-07" not in existing_unit_ids:
    manifest["units"].append({
        "id": "unit-07",
        "title": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "order": 7,
        "lessons": [
            {
                "id": "lesson-01",
                "file": "unit-07/lesson-01.yaml",
                "title": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)"
            }
        ]
    })
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"[OK] Added unit-07 to {MANIFEST_PATH.name}")
else:
    print(f"[INFO] unit-07 already exists in {MANIFEST_PATH.name}")

print("\nUnit 7 creation complete!")

# -*- coding: utf-8 -*-
"""
Generate KEG-A2 Batch 4:
- Unit A2-07: KEG-A2-07-A (35 cards) - Travel, Vacations & Reservations (Ταξίδια, Διακοπές & Κρατήσεις)
- Unit A2-08: KEG-A2-08-A (35 cards) - Weather, Nature & Geography of Greece (Καιρός, Φύση & Γεωγραφία)
Includes dual exam-style example sentences and multi-threaded Google Cloud Chirp-3 HD TTS.
"""
import sys
import os
import yaml
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from server.tts_service import synthesize_greek_chirp, generate_audio_filename

AUDIO_DIR = BASE_DIR / "audio"
CONTENT_DIR = BASE_DIR / "content"

# -------------------------------------------------------------
# UNIT A2-07 CARDS (35 cards)
# Theme: Travel, Vacations & Reservations (Ταξίδια & Κρατήσεις)
# -------------------------------------------------------------
CARDS_U07 = [
    {
        "id": "A2-U07-001",
        "greek": "η κράτηση",
        "english": "booking / reservation",
        "notes": "Feminine noun in -η (-εις). Verb: 'κάνω κράτηση' (to book). Found on travel portals and hotel vouchers.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι κρατήσεις",
            "accusative_singular": "την κράτηση",
            "collocation": "επιβεβαίωση κράτησης (booking confirmation)"
        },
        "keg_communicative_function": "Making, confirming, and modifying reservations in hotels and transport",
        "example_el": "Έκανα κράτηση για ένα δίκλινο δωμάτιο με θέα στη θάλασσα.",
        "example_en": "I made a booking for a double room with sea view.",
        "example2_el": "Παρακαλώ δείξτε μου τον αριθμό της κράτησής σας κατά την άφιξη.",
        "example2_en": "Please show me your reservation number upon arrival."
    },
    {
        "id": "A2-U07-002",
        "greek": "το εισιτήριο",
        "english": "ticket",
        "notes": "Neuter noun in -ο (-α). Collocates with 'απλό εισιτήριο' (one-way) or 'εισιτήριο μετ' επιστροφής' (return ticket).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα εισιτήρια",
            "genitive_singular": "του εισιτηρίου",
            "collocation": "εισιτήριο μετ' επιστροφής (round-trip ticket)"
        },
        "keg_communicative_function": "Purchasing transportation tickets at ticket counters or travel agencies",
        "example_el": "Θα ήθελα δύο εισιτήρια μετ' επιστροφής για το πλοίο της γραμμής.",
        "example_en": "I would like two round-trip tickets for the regular ferry.",
        "example2_el": "Μπορείτε να κλείσετε τα εισιτήριά σας ηλεκτρονικά για καλύτερες τιμές.",
        "example2_en": "You can book your tickets online for better prices."
    },
    {
        "id": "A2-U07-003",
        "greek": "η πτήση",
        "english": "flight",
        "notes": "Feminine noun in -η (-εις). Core noun in airport audio announcements (Listening Part 1).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πτήσεις",
            "accusative_singular": "την πτήση",
            "collocation": "αριθμός πτήσης (flight number)"
        },
        "keg_communicative_function": "Following airport flight boards, departure times, and gate changes",
        "example_el": "Η πτήση για τη Θεσσαλονίκη αναχωρεί από την πύλη Β12.",
        "example_en": "The flight to Thessaloniki departs from gate B12.",
        "example2_el": "Η πτήση μας είχε καθυστέρηση μίας ώρας λόγω ομίχλης.",
        "example2_en": "Our flight had a one-hour delay due to fog."
    },
    {
        "id": "A2-U07-004",
        "greek": "το πλοίο",
        "english": "ship / ferry / boat",
        "notes": "Neuter noun in -ο (-α). Main transport mode connecting the Greek islands.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πλοία",
            "genitive_singular": "του πλοίου",
            "synonym": "το καράβι"
        },
        "keg_communicative_function": "Organizing island hopping and maritime voyages",
        "example_el": "Το πλοίο φτάνει στο λιμάνι της Πάρου σε περίπου τέσσερις ώρες.",
        "example_en": "The ship arrives at the port of Paros in approximately four hours.",
        "example2_el": "Το καλοκαίρι τα πλοία για τις Κυκλάδες είναι πάντα γεμάτα ταξιδιώτες.",
        "example2_en": "In summer the ferries to the Cyclades are always full of travelers."
    },
    {
        "id": "A2-U07-005",
        "greek": "το λιμάνι",
        "english": "port / harbor",
        "notes": "Neuter noun in -ι (-ια). Hub for ferry connections (Πειραιάς, Ραφήνα, Λαύριο).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα λιμάνια",
            "genitive_singular": "του λιμανιού"
        },
        "keg_communicative_function": "Navigating port terminals and coordinating maritime connections",
        "example_el": "Πρέπει να βρισκόμαστε στο λιμάνι του Πειραιά μία ώρα πριν από τον απόπλου.",
        "example_en": "We must be at the port of Piraeus one hour before sailing.",
        "example2_el": "Το λιμάνι των Χανίων είναι ένα από τα πιο γραφικά της Κρήτης.",
        "example2_en": "The port of Chania is one of the most picturesque in Crete."
    },
    {
        "id": "A2-U07-006",
        "greek": "η διαμονή",
        "english": "stay / accommodation",
        "notes": "Feminine noun in -ή (-ές). Covers lodging in hotels, rooms, or hostels.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι διαμονές",
            "verb": "διαμένω (to reside / lodge)"
        },
        "keg_communicative_function": "Discussing lodging quality, costs, and services in reviews and emails",
        "example_el": "Η διαμονή μας στο ξενοδοχείο ήταν εξαιρετικά ευχάριστη και άνετη.",
        "example_en": "Our stay at the hotel was extremely pleasant and comfortable.",
        "example2_el": "Στην τιμή του πακέτου περιλαμβάνεται η διαμονή και το πρωινό.",
        "example2_en": "The package price includes accommodation and breakfast."
    },
    {
        "id": "A2-U07-007",
        "greek": "το μονόκλινο",
        "english": "single room",
        "notes": "Neuter substantivized adjective (μόνος + κλίνη: single bed). Antonym: 'το δίκλινο'.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μονόκλινα",
            "contrast": "το δίκλινο (double room)"
        },
        "keg_communicative_function": "Booking specific room categories at reception desks",
        "example_el": "Θα ήθελα να κλείσω ένα μονόκλινο δωμάτιο για δύο βραδιές.",
        "example_en": "I would like to book a single room for two nights.",
        "example2_el": "Υπάρχει διαθέσιμο μονόκλινο με ιδιωτικό μπάνιο;",
        "example2_en": "Is there an available single room with private bathroom?"
    },
    {
        "id": "A2-U07-008",
        "greek": "το δίκλινο",
        "english": "double / twin room",
        "notes": "Neuter substantivized adjective (δύο + κλίνη: two beds).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα δίκλινα",
            "collocation": "δίκλινο με διπλό κρεβάτι (with double bed)"
        },
        "keg_communicative_function": "Reserving accommodation for couples or pairs of travelers",
        "example_el": "Έχουμε κλείσει ένα δίκλινο δωμάτιο στο όνομα Παπαδόπουλος.",
        "example_en": "We have booked a double room under the name Papadopoulos.",
        "example2_el": "Πόσο κοστίζει το δίκλινο με θέα στη θάλασσα;",
        "example2_en": "How much does the double room with sea view cost?"
    },
    {
        "id": "A2-U07-009",
        "greek": "οι αποσκευές",
        "english": "luggage / baggage",
        "notes": "Feminine noun plural (singular 'η αποσκευή' is rare). Essential for weight limits.",
        "gender_or_pos": "noun (feminine plural)",
        "grammatical_info": {
            "part_of_speech": "noun (plural)",
            "genitive_plural": "των αποσκευών",
            "synonym": "οι βαλίτσες",
            "collocation": "παραλαβή αποσκευών (baggage claim)"
        },
        "keg_communicative_function": "Handling baggage allowances, claims, and lost luggage at airports",
        "example_el": "Το επιτρεπόμενο όριο για τις αποσκευές είναι είκοσι τρία κιλά ανά επιβάτη.",
        "example_en": "The permitted luggage allowance is twenty-three kilograms per passenger.",
        "example2_el": "Περιμένουμε τις αποσκευές μας στον ιμάντα παραλαβής νούμερο τρία.",
        "example2_en": "We are waiting for our luggage at baggage carousel number three."
    },
    {
        "id": "A2-U07-010",
        "greek": "η καθυστέρηση",
        "english": "delay",
        "notes": "Feminine noun in -η (-εις). Relates to 'καθυστερώ' (to be delayed/late).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι καθυστερήσεις",
            "collocation": "με καθυστέρηση (with a delay)",
            "verb": "καθυστερώ"
        },
        "keg_communicative_function": "Understanding transit delays and apologizing for arriving late",
        "example_el": "Το τρένο έφτασε με καθυστέρηση σαράντα λεπτών στον σταθμό.",
        "example_en": "The train arrived with a forty-minute delay at the station.",
        "example2_el": "Ζητούμε συγγνώμη για την καθυστέρηση λόγω τεχνικού προβλήματος.",
        "example2_en": "We apologize for the delay due to a technical problem."
    },
    {
        "id": "A2-U07-011",
        "greek": "η ακύρωση",
        "english": "cancellation",
        "notes": "Feminine noun in -η (-εις). Relates to 'ακυρώνω' (to cancel).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ακυρώσεις",
            "verb": "ακυρώνω",
            "collocation": "δωρεάν ακύρωση (free cancellation)"
        },
        "keg_communicative_function": "Handling cancelled trips and understanding refund policies in reading ads",
        "example_el": "Σε περίπτωση ακύρωσης του ταξιδιού, σας επιστρέφεται το σύνολο του ποσού.",
        "example_en": "In case of trip cancellation, the entire amount is refunded to you.",
        "example2_el": "Λόγω της κακοκαιρίας ανακοινώθηκε η ακύρωση όλων των πτήσεων.",
        "example2_en": "Due to bad weather the cancellation of all flights was announced."
    },
    {
        "id": "A2-U07-012",
        "greek": "η αναχώρηση",
        "english": "departure",
        "notes": "Feminine noun in -η (-εις). Antonym: 'η άφιξη' (arrival). Verb: 'αναχωρώ'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι αναχωρήσεις",
            "verb": "αναχωρώ",
            "antonym": "η άφιξη"
        },
        "keg_communicative_function": "Checking departure gates and schedule listings on transit boards",
        "example_el": "Η ώρα αναχώρησης του λεωφορείου είναι ακριβώς στις δέκα και μισή.",
        "example_en": "The departure time of the bus is exactly at half past ten.",
        "example2_el": "Ο πίνακας αναχωρήσεων δείχνει τις επόμενες πτήσεις της ημέρας.",
        "example2_en": "The departures board shows the next flights of the day."
    },
    {
        "id": "A2-U07-013",
        "greek": "η άφιξη",
        "english": "arrival",
        "notes": "Feminine noun in -η (-εις). Antonym: 'η αναχώρηση'. Verb: 'φτάνω'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι αφίξεις",
            "antonym": "η αναχώρηση"
        },
        "keg_communicative_function": "Arranging airport/port pickups and meeting arriving guests",
        "example_el": "Θα σας περιμένω στην αίθουσα αφίξεων του αεροδρομίου.",
        "example_en": "I will be waiting for you in the arrivals hall of the airport.",
        "example2_el": "Η αναμενόμενη ώρα άφιξης του πλοίου είναι στις επτά το απόγευμα.",
        "example2_en": "The expected arrival time of the ship is at seven in the evening."
    },
    {
        "id": "A2-U07-014",
        "greek": "αναχωρώ",
        "english": "to depart / to leave",
        "notes": "Contracted verb (αναχωρεί, αναχωρούν). Formal verb common in announcements.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "αναχώρησα",
            "simple_future": "θα αναχωρήσω",
            "noun_derivative": "η αναχώρηση"
        },
        "keg_communicative_function": "Reporting vehicle departures in formal announcements and travel writing",
        "example_el": "Το πλοίο αναχωρεί καθημερινά από τη Ραφήνα για την Άνδρο και την Τήνο.",
        "example_en": "The ship departs daily from Rafina for Andros and Tinos.",
        "example2_el": "Θα αναχωρήσουμε νωρίς το ξημέρωμα για να αποφύγουμε την κίνηση.",
        "example2_en": "We will depart early at dawn to avoid traffic."
    },
    {
        "id": "A2-U07-015",
        "greek": "επισκέπτομαι",
        "english": "to visit",
        "notes": "Deponent verb (επισκέπτομαι, επισκέπτεσαι, επισκέπτεται). Simple past: 'επισκέφτηκα'.",
        "gender_or_pos": "verb (deponent)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "επισκέφτηκα",
            "simple_future": "θα επισκεφτώ",
            "noun_derivative": "η επίσκεψη"
        },
        "keg_communicative_function": "Describing sightseeing itineraries and museum excursions",
        "example_el": "Κατά τη διαμονή μας στην Αθήνα επισκεφτήκαμε τον Ιερό Βράχο της Ακρόπολης.",
        "example_en": "During our stay in Athens we visited the Sacred Rock of the Acropolis.",
        "example2_el": "Σκοπεύουμε να επισκεφτούμε τα Μετέωρα τον επόμενο μήνα.",
        "example2_en": "We intend to visit Meteora next month."
    },
    {
        "id": "A2-U07-016",
        "greek": "ο προορισμός",
        "english": "destination",
        "notes": "Masculine noun in -ος (-οι). Collocates with 'δημοφιλής προορισμός' (popular destination).",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι προορισμοί",
            "genitive_singular": "του προορισμού"
        },
        "keg_communicative_function": "Discussing vacation destinations and travel recommendations",
        "example_el": "Η Σαντορίνη είναι ένας από τους πιο διάσημους τουριστικούς προορισμούς στον κόσμο.",
        "example_en": "Santorini is one of the most famous tourist destinations in the world.",
        "example2_el": "Ποιος είναι ο επόμενος προορισμός του ταξιδιού σας;",
        "example2_en": "What is the next destination of your trip?"
    },
    {
        "id": "A2-U07-017",
        "greek": "τα αξιοθέατα",
        "english": "sights / tourist attractions",
        "notes": "Neuter plural noun (άξιος + θέαμα: worthy of viewing). Collocates with 'βλέπω τα αξιοθέατα'.",
        "gender_or_pos": "noun (neuter plural)",
        "grammatical_info": {
            "part_of_speech": "noun (plural)",
            "genitive_plural": "των αξιοθεάτων",
            "singular": "το αξιοθέατο"
        },
        "keg_communicative_function": "Asking for recommendations about monuments, sights, and historical ruins",
        "example_el": "Ποια είναι τα σημαντικότερα αξιοθέατα που αξίζει να δει κανείς στην πόλη;",
        "example_en": "What are the most important sights worth seeing in the city?",
        "example2_el": "Περάσαμε όλη την ημέρα περπατώντας και βλέποντας τα αξιοθέατα.",
        "example2_en": "We spent the entire day walking and viewing the sights."
    },
    {
        "id": "A2-U07-018",
        "greek": "ο ξεναγός",
        "english": "tour guide",
        "notes": "Masculine / feminine noun (ο/η ξεναγός). Related to 'η ξενάγηση' (guided tour).",
        "gender_or_pos": "noun (common gender)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "plural": "οι ξεναγοί",
            "noun_activity": "η ξενάγηση",
            "verb": "ξεναγώ"
        },
        "keg_communicative_function": "Booking guided tours or describing historical tour experiences",
        "example_el": "Ο ξεναγός μάς εξήγησε την ιστορία του αρχαιολογικού χώρου με μεγάλη λεπτομέρεια.",
        "example_en": "The tour guide explained the history of the archaeological site to us in great detail.",
        "example2_el": "Κλείσαμε μια ξενάγηση με πιστοποιημένο ξεναγό στα ελληνικά και αγγλικά.",
        "example2_en": "We booked a tour with a certified tour guide in Greek and English."
    },
    {
        "id": "A2-U07-019",
        "greek": "η ξενάγηση",
        "english": "guided tour",
        "notes": "Feminine noun in -η (-εις). Essential tourist activity vocabulary.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ξεναγήσεις",
            "genitive_singular": "της ξενάγησης"
        },
        "keg_communicative_function": "Participating in cultural excursions and museum tours",
        "example_el": "Η ξενάγηση στο μουσείο διαρκεί περίπου μιάμιση ώρα.",
        "example_en": "The guided tour in the museum lasts about an hour and a half.",
        "example2_el": "Περιλαμβάνεται η ξενάγηση στην τιμή του εισιτηρίου εισόδου;",
        "example2_en": "Is the guided tour included in the price of the entrance ticket?"
    },
    {
        "id": "A2-U07-020",
        "greek": "το δρομολόγιο",
        "english": "itinerary / route / timetable",
        "notes": "Neuter noun in -ο (-α). Essential for ferry and train timetables.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα δρομολόγια",
            "collocation": "δρομολόγια πλοίων / τρένων"
        },
        "keg_communicative_function": "Inquiring about bus, train, or boat schedules and routes",
        "example_el": "Μπορείτε να μου πείτε ποιο είναι το επόμενο δρομολόγιο για το αεροδρόμιο;",
        "example_en": "Can you tell me what the next route/service to the airport is?",
        "example2_el": "Το χειμερινό δρομολόγιο του πλοίου έχει λιγότερες αναχωρήσεις την εβδομάδα.",
        "example2_en": "The ship's winter timetable has fewer departures per week."
    },
    {
        "id": "A2-U07-021",
        "greek": "η κάρτα επιβίβασης",
        "english": "boarding pass",
        "notes": "Feminine noun phrase. Essential check-in document at airport and ferry gates.",
        "gender_or_pos": "noun phrase (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "plural": "οι κάρτες επιβίβασης",
            "verb": "επιβιβάζομαι"
        },
        "keg_communicative_function": "Printing or showing boarding passes on smartphones during gate control",
        "example_el": "Παρακαλώ να έχετε την κάρτα επιβίβασης και το διαβατήριό σας έτοιμα για έλεγχο.",
        "example_en": "Please have your boarding pass and passport ready for inspection.",
        "example2_el": "Κατέβασα την ηλεκτρονική κάρτα επιβίβασης στο κινητό μου τηλέφωνο.",
        "example2_en": "I downloaded the electronic boarding pass onto my mobile phone."
    },
    {
        "id": "A2-U07-022",
        "greek": "η πύλη επιβίβασης",
        "english": "boarding gate",
        "notes": "Feminine noun phrase. Key airport audio announcement focus.",
        "gender_or_pos": "noun phrase (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "plural": "οι πύλες επιβίβασης",
            "collocation": "αλλαγή πύλης (gate change)"
        },
        "keg_communicative_function": "Navigating airport terminals to correct departure gates",
        "example_el": "Η πύλη επιβίβασης θα κλείσει είκοσι λεπτά πριν από την αναχώρηση της πτήσης.",
        "example_en": "The boarding gate will close twenty minutes prior to the flight departure.",
        "example2_el": "Παρακαλούνται οι επιβάτες να προσέλθουν άμεσα στην πύλη επιβίβασης.",
        "example2_en": "Passengers are requested to proceed immediately to the boarding gate."
    },
    {
        "id": "A2-U07-023",
        "greek": "το κατάστρωμα",
        "english": "ship deck / open deck",
        "notes": "Neuter noun in -μα (-ματα). Cheapest and most popular ferry ticket tier in Greece.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα καταστρώματα",
            "collocation": "εισιτήριο καταστρώματος (deck ticket)"
        },
        "keg_communicative_function": "Purchasing economy ferry tickets and describing the sea voyage",
        "example_el": "Πήραμε εισιτήρια καταστρώματος και καθίσαμε έξω απολαμβάνοντας τη θέα.",
        "example_en": "We bought deck tickets and sat outside enjoying the view.",
        "example2_el": "Στο κατάστρωμα του πλοίου φυσούσε ένα δροσερό αεράκι.",
        "example2_en": "On the ship deck a refreshing breeze was blowing."
    },
    {
        "id": "A2-U07-024",
        "greek": "η καμπίνα",
        "english": "ship cabin / compartment",
        "notes": "Feminine noun in -α (-ες). Used for overnight ferry voyages (π.χ. Πειραιάς - Χανιά / Ηράκλειο).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι καμπίνες",
            "collocation": "δίκλινη καμπίνα (two-berth cabin)"
        },
        "keg_communicative_function": "Booking overnight sleeping cabins on long maritime crossings",
        "example_el": "Επειδή το ταξίδι είναι νυχτερινό, προτιμήσαμε να κλείσουμε μια δίκλινη καμπίνα.",
        "example_en": "Because the voyage is overnight, we preferred to book a two-berth cabin.",
        "example2_el": "Η καμπίνα είχε δικό της μπάνιο και ήταν πολύ καθαρή.",
        "example2_en": "The cabin had its own bathroom and was very clean."
    },
    {
        "id": "A2-U07-025",
        "greek": "νοικιάζω",
        "english": "to rent / to hire",
        "notes": "Active verb. Simple past: 'νοίκιασα'. Future: 'θα νοικιάσω'. Used for cars, scooters, or apartments.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "νοίκιασα",
            "simple_future": "θα νοικιάσω",
            "noun_derivative": "το ενοίκιο (rent) / η ενοικίαση"
        },
        "keg_communicative_function": "Renting a car, motorcycle, or holiday house during travels",
        "example_el": "Στο νησί νοικιάσαμε ένα μικρό αυτοκίνητο για να γυρίσουμε όλες τις παραλίες.",
        "example_en": "On the island we rented a small car to tour all the beaches.",
        "example2_el": "Πόσο κοστίζει να νοικιάσει κανείς μηχανάκι για μία εβδομάδα;",
        "example2_en": "How much does it cost to rent a scooter for one week?"
    },
    {
        "id": "A2-U07-026",
        "greek": "πιο",
        "english": "more (comparative particle)",
        "notes": "Comparative particle placed before adjectives and adverbs: 'πιο μεγάλος' (bigger), 'πιο γρήγορα' (faster).",
        "gender_or_pos": "adverb / particle",
        "grammatical_info": {
            "part_of_speech": "particle",
            "syntax": "πιο + θετικός βαθμός επιθέτου / επιρρήματος",
            "comparative_structure": "πιο ... από (more ... than)"
        },
        "keg_communicative_function": "Comparing options, prices, hotels, and travel durations",
        "example_el": "Το αεροπλάνο είναι πιο γρήγορο από το πλοίο, αλλά το πλοίο είναι πιο οικονομικό.",
        "example_en": "The plane is faster than the ferry, but the ferry is more economical.",
        "example2_el": "Αναζητούμε ένα ξενοδοχείο πιο κοντά στο κέντρο της παλιάς πόλης.",
        "example2_en": "We are seeking a hotel closer to the center of the old town."
    },
    {
        "id": "A2-U07-027",
        "greek": "καλύτερος",
        "english": "better / best",
        "notes": "Irregular comparative adjective (καλός -> καλύτερος). Feminine: καλύτερη, neuter: καλύτερο.",
        "gender_or_pos": "adjective (comparative)",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "positive": "καλός, -ή, -ό",
            "superlative": "ο καλύτερος (the best)"
        },
        "keg_communicative_function": "Expressing superior quality and personal preferences in debates",
        "example_el": "Ποια είναι η καλύτερη εποχή για να επισκεφτεί κανείς την Ελλάδα;",
        "example_en": "What is the best season to visit Greece?",
        "example2_el": "Αυτό το κατάλυμα έχει πολύ καλύτερη βαθμολογία από το προηγούμενο.",
        "example2_en": "This accommodation has a much better rating than the previous one."
    },
    {
        "id": "A2-U07-028",
        "greek": "φθηνότερος",
        "english": "cheaper",
        "notes": "Regular synthetic comparative of 'φθηνός' (-ότερος, -ότερη, -ότερο). Synonym: 'πιο φθηνός'.",
        "gender_or_pos": "adjective (comparative)",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "positive": "φθηνός",
            "antonym": "ακριβότερος (more expensive)"
        },
        "keg_communicative_function": "Comparing ticket prices and shopping options in commercial dialogues",
        "example_el": "Αν κλείσετε τα εισιτήρια νωρίς, θα βρείτε πολύ φθηνότερες τιμές.",
        "example_en": "If you book the tickets early, you will find much cheaper prices.",
        "example2_el": "Υπάρχει κάποιο φθηνότερο μέσο μεταφοράς για το αεροδρόμιο;",
        "example2_en": "Is there a cheaper means of transport to the airport?"
    },
    {
        "id": "A2-U07-029",
        "greek": "ακριβότερος",
        "english": "more expensive",
        "notes": "Synthetic comparative of 'ακριβός' (-ότερος, -ότερη, -ότερο). Synonym: 'πιο ακριβός'.",
        "gender_or_pos": "adjective (comparative)",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "positive": "ακριβός",
            "antonym": "φθηνότερος"
        },
        "keg_communicative_function": "Discussing cost variations between peak season and off-season",
        "example_el": "Τον Αύγουστο τα δωμάτια στα νησιά είναι πολύ ακριβότερα από τον Ιούνιο.",
        "example_en": "In August rooms on the islands are much more expensive than in June.",
        "example2_el": "Η πρώτη θέση στο τρένο είναι ακριβότερη, αλλά προσφέρει περισσότερη άνεση.",
        "example2_en": "First class on the train is more expensive, but offers more comfort."
    },
    {
        "id": "A2-U07-030",
        "greek": "γρηγορότερος",
        "english": "faster / quicker",
        "notes": "Synthetic comparative of 'γρήγορος'. Adverbial comparative: 'γρηγορότερα' (more quickly).",
        "gender_or_pos": "adjective (comparative)",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "positive": "γρήγορος",
            "adverb": "γρηγορότερα (faster / sooner)"
        },
        "keg_communicative_function": "Comparing transport transit speeds and efficiency",
        "example_el": "Το ταχύπλοο είναι γρηγορότερο από το συμβατικό πλοίο κατά δύο ώρες.",
        "example_en": "The high-speed ferry is faster than the conventional ferry by two hours.",
        "example2_el": "Ποιος είναι ο γρηγορότερος δρόμος για να πάμε στο κέντρο;",
        "example2_en": "Which is the fastest way to get to the center?"
    },
    {
        "id": "A2-U07-031",
        "greek": "η παραλία",
        "english": "beach / seashore",
        "notes": "Feminine noun in -α (-ες). Essential leisure and geography vocabulary.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι παραλίες",
            "genitive_singular": "της παραλίας"
        },
        "keg_communicative_function": "Describing summer beach excursions and coastal scenery",
        "example_el": "Κολυμπήσαμε σε μια υπέροχη παραλία με κρυστάλλινα γαλαζοπράσινα νερά.",
        "example_en": "We swam at a magnificent beach with crystal-clear turquoise waters.",
        "example2_el": "Η παραλία είναι οργανωμένη με ομπρέλες, ξαπλώστρες και ναυαγοσώστη.",
        "example2_en": "The beach is organized with umbrellas, sunbeds, and a lifeguard."
    },
    {
        "id": "A2-U07-032",
        "greek": "το νησί",
        "english": "island",
        "notes": "Neuter noun in -ί (-ιά). Plural: 'τα νησιά'. Central element of Greek geography.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα νησιά",
            "genitive_singular": "του νησιού",
            "adjective": "νησιωτικός, -ή, -ό"
        },
        "keg_communicative_function": "Talking about holidays on Greek islands in oral and written tasks",
        "example_el": "Κάθε καλοκαίρι επισκεπτόμαστε και ένα διαφορετικό ελληνικό νησί.",
        "example_en": "Every summer we visit a different Greek island.",
        "example2_el": "Η ζωή στο νησί τον χειμώνα είναι πολύ πιο ήσυχη.",
        "example2_en": "Life on the island in winter is much quieter."
    },
    {
        "id": "A2-U07-033",
        "greek": "το ξενοδοχείο",
        "english": "hotel",
        "notes": "Neuter noun in -ο (-α). Collocates with 'πεντάστερο ξενοδοχείο' (five-star hotel).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ξενοδοχεία",
            "genitive_singular": "του ξενοδοχείου"
        },
        "keg_communicative_function": "Checking in, checking out, and evaluating hotel amenities",
        "example_el": "Το ξενοδοχείο προσφέρει δωρεάν ασύρματο διαδίκτυο και πρωινό μπουφέ.",
        "example_en": "The hotel offers free wireless internet and a buffet breakfast.",
        "example2_el": "Φτάσαμε στο ξενοδοχείο αργά το βράδυ και κάναμε άμεσα check-in.",
        "example2_en": "We arrived at the hotel late at night and checked in immediately."
    },
    {
        "id": "A2-U07-034",
        "greek": "η βαλίτσα",
        "english": "suitcase",
        "notes": "Feminine noun in -α (-ες). Collocates with 'φτιάχνω / ετοιμάζω τη βαλίτσα' (to pack the suitcase).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι βαλίτσες",
            "collocation": "φτιάχνω τη βαλίτσα (to pack)"
        },
        "keg_communicative_function": "Describing trip preparations and packing essentials in letters",
        "example_el": "Ετοίμασα τη βαλίτσα μου από το προηγούμενο βράδυ για να είμαι έτοιμος.",
        "example_en": "I packed my suitcase from the previous night to be ready.",
        "example2_el": "Η βαλίτσα μου ξεπέρασε το επιτρεπόμενο βάρος κατά δύο κιλά.",
        "example2_en": "My suitcase exceeded the permitted weight by two kilograms."
    },
    {
        "id": "A2-U07-035",
        "greek": "καλό ταξίδι",
        "english": "have a good trip / safe journey",
        "notes": "Formulaic farewell addressed to anyone departing on a voyage.",
        "gender_or_pos": "phrase (farewell)",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "synonym": "καλό δρόμο, καλή επιστροφή"
        },
        "keg_communicative_function": "Wishing safe journeys to departing friends and travelers",
        "example_el": "Σας εύχομαι καλό ταξίδι και να περάσετε υπέροχα!",
        "example_en": "I wish you a good trip and have a wonderful time!",
        "example2_el": "Καλό ταξίδι και περιμένουμε νέα σας μόλις φτάσετε στον προορισμό σας.",
        "example2_en": "Safe journey and we look forward to hearing from you as soon as you reach your destination."
    }
]

# -------------------------------------------------------------
# UNIT A2-08 CARDS (35 cards)
# Theme: Weather, Nature & Geography of Greece (Καιρός & Φύση)
# -------------------------------------------------------------
CARDS_U08 = [
    {
        "id": "A2-U08-001",
        "greek": "ο καιρός",
        "english": "weather / time",
        "notes": "Masculine noun in -ός (-οί). 'Τι καιρό κάνει;' = What's the weather like?",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι καιροί",
            "collocation": "δελτίο καιρού (weather forecast / bulletin)"
        },
        "keg_communicative_function": "Asking about and describing weather conditions in dialogues and listening tasks",
        "example_el": "Τι καιρό προβλέπεται να κάνει το Σαββατοκύριακο στην Αττική;",
        "example_en": "What weather is forecast for the weekend in Attica?",
        "example2_el": "Ο καιρός σήμερα είναι θαυμάσιος με άπλετη ηλιοφάνεια.",
        "example2_en": "The weather today is magnificent with ample sunshine."
    },
    {
        "id": "A2-U08-002",
        "greek": "η θερμοκρασία",
        "english": "temperature",
        "notes": "Feminine noun in -α (-ες). Collocates with 'βαθμοί Κελσίου' and verbs 'ανεβαίνει' / 'πέφτει'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι θερμοκρασίες",
            "collocation": "η θερμοκρασία θα φτάσει τους... βαθμούς"
        },
        "keg_communicative_function": "Interpreting recorded weather bulletins (Listening Part 1 & 3)",
        "example_el": "Η θερμοκρασία θα σημειώσει μικρή άνοδο και θα φτάσει τους τριάντα δύο βαθμούς.",
        "example_en": "The temperature will rise slightly and will reach thirty-two degrees.",
        "example2_el": "Το βράδυ στα ορεινά η θερμοκρασία πέφτει αισθητά.",
        "example2_en": "At night in mountainous areas the temperature drops noticeably."
    },
    {
        "id": "A2-U08-003",
        "greek": "η ηλιοφάνεια",
        "english": "sunshine",
        "notes": "Feminine noun in -α. Characteristic meteorological term in Greek forecasts.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "adjective": "ηλιόλουστος, -η, -ο (sunny)"
        },
        "keg_communicative_function": "Extracting weather details from recorded radio and TV bulletins",
        "example_el": "Στο μεγαλύτερο μέρος της χώρας προβλέπεται ηλιοφάνεια με λίγες αραιές νεφώσεις.",
        "example_en": "In most parts of the country sunshine is forecast with few sparse clouds.",
        "example2_el": "Απολαύσαμε μια ηλιόλουστη μέρα κάνοντας βόλτα δίπλα στη θάλασσα.",
        "example2_en": "We enjoyed a sunny day taking a walk beside the sea."
    },
    {
        "id": "A2-U08-004",
        "greek": "η συννεφιά",
        "english": "cloudiness / overcast sky",
        "notes": "Feminine noun in -ά. Relates to 'το σύννεφο' (cloud). Adjective: 'συννεφιασμένος'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "noun_root": "το σύννεφο",
            "adjective": "συννεφιασμένος, -η, -ο"
        },
        "keg_communicative_function": "Describing sky conditions and impending rain",
        "example_el": "Από το μεσημέρι και μετά αναμένεται αυξημένη συννεφιά στα δυτικά.",
        "example_en": "From noon onwards increased cloudiness is expected in the west.",
        "example2_el": "Παρά τη συννεφιά, η θερμοκρασία παρέμεινε σε υψηλά επίπεδα.",
        "example2_en": "Despite the overcast sky, the temperature remained at high levels."
    },
    {
        "id": "A2-U08-005",
        "greek": "η βροχή",
        "english": "rain",
        "notes": "Feminine noun in -ή (-ές). Verb: 'βρέχει' (it's raining).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι βροχές",
            "impersonal_verb": "βρέχει",
            "adjective": "βροχερός, -ή, -ό"
        },
        "keg_communicative_function": "Describing precipitation and planning indoor activities accordingly",
        "example_el": "Το απόγευμα αναμένονται τοπικές βροχές και σποραδικές καταιγίδες.",
        "example_en": "In the afternoon local rain and sporadic thunderstorms are expected.",
        "example2_el": "Πάρτε ομπρέλα μαζί σας επειδή άρχισε δυνατή βροχή.",
        "example2_en": "Take an umbrella with you because heavy rain has started."
    },
    {
        "id": "A2-U08-006",
        "greek": "η καταιγίδα",
        "english": "thunderstorm / tempest",
        "notes": "Feminine noun in -α (-ες). Accompanied by lightning ('αστραπή') and thunder ('βροντή').",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι καταιγίδες",
            "genitive_singular": "της καταιγίδας"
        },
        "keg_communicative_function": "Understanding severe weather alerts in bulletins and maritime warnings",
        "example_el": "Η σφοδρή καταιγίδα προκάλεσε προσωρινές διακοπές στην κυκλοφορία.",
        "example_en": "The violent thunderstorm caused temporary traffic disruptions.",
        "example2_el": "Μείνετε σε κλειστούς χώρους κατά τη διάρκεια της έντονης καταιγίδας.",
        "example2_en": "Stay indoors during the intense storm."
    },
    {
        "id": "A2-U08-007",
        "greek": "το χιόνι",
        "english": "snow",
        "notes": "Neuter noun in -ι (-ια). Verb: 'χιονίζει' (it is snowing).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα χιόνια",
            "impersonal_verb": "χιονίζει",
            "adjective": "χιονισμένος"
        },
        "keg_communicative_function": "Describing winter weather conditions and mountain scenery",
        "example_el": "Τον χειμώνα πέφτει πολύ χιόνι στα ορεινά χωριά της Πίνδου.",
        "example_en": "In winter a lot of snow falls in the mountain villages of Pindus.",
        "example2_el": "Τα βουνά γύρω από την πόλη είναι ακόμα χιονισμένα.",
        "example2_en": "The mountains around the city are still snow-covered."
    },
    {
        "id": "A2-U08-008",
        "greek": "ο άνεμος",
        "english": "wind",
        "notes": "Masculine noun in -ος (-οι). Formal term for 'ο αέρας'. Measured in Beaufort (μποφόρ).",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι άνεμοι",
            "collocation": "άνεμοι εντάσεως 6 με 7 μποφόρ",
            "verb": "φυσάει"
        },
        "keg_communicative_function": "Understanding maritime sailing advisories and wind force levels",
        "example_el": "Στο Αιγαίο θα πνέουν ισχυροί βόρειοι άνεμοι εντάσεως επτά μποφόρ.",
        "example_en": "In the Aegean strong northern winds of force seven Beaufort will blow.",
        "example2_el": "Ο άνεμος ήταν τόσο δυνατός που δυσκόλευε τη βάδιση.",
        "example2_en": "The wind was so strong that it made walking difficult."
    },
    {
        "id": "A2-U08-009",
        "greek": "το μποφόρ",
        "english": "Beaufort (wind scale)",
        "notes": "Neuter indeclinable noun. Essential in Greek weather bulletins for ferry sailing permissions (απαγορευτικό απόπλου at 8-9 Beaufort).",
        "gender_or_pos": "noun (neuter indeclinable)",
        "grammatical_info": {
            "part_of_speech": "noun (indeclinable)",
            "usage": "measures wind force from 0 to 12"
        },
        "keg_communicative_function": "Interpreting ferry departure delays due to windy conditions in Listening Part 1",
        "example_el": "Λόγω ανέμων οκτώ μποφόρ εκδόθηκε απαγορευτικό απόπλου από τα λιμάνια.",
        "example_en": "Due to eight Beaufort winds a sailing ban was issued from the ports.",
        "example2_el": "Οι άνεμοι δεν θα ξεπεράσουν τα τέσσερα με πέντε μποφόρ.",
        "example2_en": "The winds will not exceed four to five Beaufort."
    },
    {
        "id": "A2-U08-010",
        "greek": "φυσάει",
        "english": "it is windy / it blows",
        "notes": "Impersonal verb (3rd person singular). Past: 'φύσηξε'.",
        "gender_or_pos": "verb (impersonal)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "φύσηξε",
            "noun": "ο άνεμος, ο αέρας"
        },
        "keg_communicative_function": "Remarking on breezy or stormy conditions in conversational exchanges",
        "example_el": "Σήμερα φυσάει πολύ, οπότε καλύτερα να μην πάμε για ιστιοπλοΐα.",
        "example_en": "Today it is very windy, so it is better that we don't go sailing.",
        "example2_el": "Στην κορυφή του λόφου φυσούσε ένας ευχάριστος δροσερός αέρας.",
        "example2_en": "At the top of the hill a pleasant cool breeze was blowing."
    },
    {
        "id": "A2-U08-011",
        "greek": "βρέχει",
        "english": "it is raining",
        "notes": "Impersonal verb (3rd person singular). Simple past: 'έβρεξε'.",
        "gender_or_pos": "verb (impersonal)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "έβρεξε",
            "noun": "η βροχή"
        },
        "keg_communicative_function": "Describing rainy weather in daily conversation",
        "example_el": "Βρέχει καταρρακτωδώς εδώ και δύο ώρες, οι δρόμοι γέμισαν νερό.",
        "example_en": "It has been raining cats and dogs for two hours; the streets flooded with water.",
        "example2_el": "Αν βρέχει αύριο, η εκδήλωση θα γίνει μέσα στην κλειστή αίθουσα.",
        "example2_en": "If it rains tomorrow, the event will take place inside the enclosed hall."
    },
    {
        "id": "A2-U08-012",
        "greek": "ο καύσωνας",
        "english": "heatwave",
        "notes": "Masculine noun in -ας (-ες). Frequent summer phenomenon in Greece (temperatures > 38-40°C).",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι καύσωνες",
            "genitive_singular": "του καύσωνα"
        },
        "keg_communicative_function": "Understanding civil protection heat advisories and precautions",
        "example_el": "Κατά τη διάρκεια του καύσωνα οι ευάλωτες ομάδες πρέπει να παραμένουν σε κλιματιζόμενους χώρους.",
        "example_en": "During the heatwave vulnerable groups must remain in air-conditioned areas.",
        "example2_el": "Το κύμα καύσωνα αναμένεται να υποχωρήσει από την ερχόμενη Τρίτη.",
        "example2_en": "The heatwave is expected to recede starting next Tuesday."
    },
    {
        "id": "A2-U08-013",
        "greek": "η κακοκαιρία",
        "english": "bad weather / severe storm",
        "notes": "Feminine noun in -α (-ες). Antonym: 'η καλοκαιρία' (fine weather).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "antonym": "η καλοκαιρία",
            "collocation": "κύμα κακοκαιρίας (cold snap / storm front)"
        },
        "keg_communicative_function": "Reading storm warnings and news bulletins in Reading Part 1 & 2",
        "example_el": "Η κακοκαιρία έπληξε κυρίως τις παραθαλάσσιες περιοχές της δυτικής Ελλάδας.",
        "example_en": "The severe weather hit mainly the coastal areas of western Greece.",
        "example2_el": "Λόγω της κακοκαιρίας τα σχολεία παρέμειναν κλειστά σήμερα.",
        "example2_en": "Due to bad weather the schools remained closed today."
    },
    {
        "id": "A2-U08-014",
        "greek": "η καλοκαιρία",
        "english": "fine weather / fair skies",
        "notes": "Feminine noun in -α. Antonym: 'η κακοκαιρία'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "antonym": "η κακοκαιρία"
        },
        "keg_communicative_function": "Welcoming sunny skies and planning outdoor weekend trips",
        "example_el": "Η καλοκαιρία θα συνεχιστεί καθ' όλη τη διάρκεια της εβδομάδας.",
        "example_en": "The fine weather will continue throughout the week.",
        "example2_el": "Εκμεταλλευτήκαμε την καλοκαιρία για να κάνουμε πεζοπορία στο βουνό.",
        "example2_en": "We took advantage of the fine weather to go hiking in the mountain."
    },
    {
        "id": "A2-U08-015",
        "greek": "το βουνό",
        "english": "mountain",
        "notes": "Neuter noun in -ό (-ά). Greece is 80% mountainous. Plural: 'τα βουνά'.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα βουνά",
            "genitive_singular": "του βουνού",
            "adjective": "ορεινός, -ή, -ό"
        },
        "keg_communicative_function": "Discussing geography, mountain villages, and hiking routes",
        "example_el": "Ο Όλυμπος είναι το ψηλότερο βουνό της Ελλάδας με υψόμετρο σχεδόν τρεις χιλιάδες μέτρα.",
        "example_en": "Olympus is the highest mountain in Greece with an altitude of nearly three thousand meters.",
        "example2_el": "Πολλοί προτιμούν τις διακοπές στο βουνό αντί για τη θάλασσα.",
        "example2_en": "Many prefer mountain holidays instead of the sea."
    },
    {
        "id": "A2-U08-016",
        "greek": "η θάλασσα",
        "english": "sea",
        "notes": "Feminine noun in -α (-ες). Central geographical feature of Greece.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι θάλασσες",
            "genitive_singular": "της θάλασσας",
            "adjective": "θαλάσσιος, -α, -ο"
        },
        "keg_communicative_function": "Describing maritime landscapes and seaside excursions",
        "example_el": "Η θάλασσα ήταν εντελώς ήρεμη σαν λάδι σήμερα το πρωί.",
        "example_en": "The sea was completely calm like glass this morning.",
        "example2_el": "Η Ελλάδα περιβάλλεται από το Αιγαίο και το Ιόνιο Πέλαγος.",
        "example2_en": "Greece is surrounded by the Aegean and the Ionian Sea."
    },
    {
        "id": "A2-U08-017",
        "greek": "το δάσος",
        "english": "forest / woods",
        "notes": "Neuter noun in -ος (-η, genitive -ους). Plural: 'τα δάση'. Declension paradigm: το δάσος, του δάσους, τα δάση.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα δάση",
            "genitive_singular": "του δάσους",
            "genitive_plural": "των δασών"
        },
        "keg_communicative_function": "Discussing environmental protection, nature walks, and forest ecosystems",
        "example_el": "Πήγαμε για πικνίκ σε ένα πυκνό πευκοδάσος κοντά στην πόλη.",
        "example_en": "We went for a picnic in a dense pine forest near the city.",
        "example2_el": "Η προστασία των δασών από τις πυρκαγιές είναι κρίσιμο καθήκον όλων.",
        "example2_en": "Protecting forests from wildfires is everyone's crucial duty."
    },
    {
        "id": "A2-U08-018",
        "greek": "το ποτάμι",
        "english": "river",
        "notes": "Neuter noun in -ι (-ια). Formal variant: 'ο ποταμός'. Plural: 'τα ποτάμια'.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ποτάμια",
            "formal_variant": "ο ποταμός",
            "genitive_singular": "του ποταμιού"
        },
        "keg_communicative_function": "Describing inland waterways and nature activities (rafting, canoeing)",
        "example_el": "Ο Αξιός είναι ένα από τα μεγαλύτερα ποτάμια της βόρειας Ελλάδας.",
        "example_en": "Axios is one of the largest rivers of northern Greece.",
        "example2_el": "Κάναμε ράφτινγκ στα καθαρά νερά του ποταμού Βοϊδομάτη.",
        "example2_en": "We did rafting in the clear waters of the Voidomatis river."
    },
    {
        "id": "A2-U08-019",
        "greek": "η λίμνη",
        "english": "lake",
        "notes": "Feminine noun in -η (-ες). Major Greek lakes: Πρέσπες, Πλαστήρα, Παμβώτιδα.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι λίμνες",
            "genitive_singular": "της λίμνης"
        },
        "keg_communicative_function": "Discussing scenic lake destinations in Ioannina, Kastoria, or Plastira",
        "example_el": "Η πόλη των Ιωαννίνων είναι χτισμένη στις όχθες μιας πανέμορφης λίμνης.",
        "example_en": "The city of Ioannina is built on the shores of a gorgeous lake.",
        "example2_el": "Στη λίμνη ζουν πολλά σπάνια είδη πουλιών και ψαριών.",
        "example2_en": "Many rare species of birds and fish live in the lake."
    },
    {
        "id": "A2-U08-020",
        "greek": "η πεδιάδα",
        "english": "plain / flatland",
        "notes": "Feminine noun in -α (-ες). Major agricultural plains: Θεσσαλική πεδιάδα.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πεδιάδες",
            "genitive_singular": "της πεδιάδας",
            "adjective": "πεδινός, -ή, -ό"
        },
        "keg_communicative_function": "Describing agricultural geography and rural landscapes in Reading Part 2",
        "example_el": "Η θεσσαλική πεδιάδα είναι η μεγαλύτερη αγροτική περιοχή της χώρας.",
        "example_en": "The Thessalian plain is the largest agricultural region of the country.",
        "example2_el": "Στην πεδιάδα καλλιεργούνται σιτηρά, βαμβάκι και οπωροφόρα δέντρα.",
        "example2_en": "In the plain cereals, cotton, and fruit trees are cultivated."
    },
    {
        "id": "A2-U08-021",
        "greek": "το τοπίο",
        "english": "landscape / scenery",
        "notes": "Neuter noun in -ο (-α). Collocates with 'μαγευτικό τοπίο' (enchanting scenery).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα τοπία",
            "genitive_singular": "του τοπίου"
        },
        "keg_communicative_function": "Describing scenic beauty in travel essays and postcards",
        "example_el": "Το ηλιοβασίλεμα στη Σαντορίνη δημιουργεί ένα ανεπανάληπτο τοπίο.",
        "example_en": "The sunset in Santorini creates an unforgettable landscape.",
        "example2_el": "Το ορεινό τοπίο αλλάζει χρώματα ανάλογα με την εποχή του χρόνου.",
        "example2_en": "The mountainous landscape changes colors according to the season of the year."
    },
    {
        "id": "A2-U08-022",
        "greek": "βαθύς",
        "english": "deep",
        "notes": "Adjective in -ύς, -ιά, -ύ (βαθύς, βαθιά, βαθύ / πληθυντικός: βαθιοί, βαθιές, βαθιά). Crucial A2 declension milestone.",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "βαθιά",
            "neuter": "βαθύ",
            "plural_masculine": "βαθιοί",
            "plural_feminine": "βαθιές",
            "plural_neuter": "βαθιά"
        },
        "keg_communicative_function": "Describing sea depth, waters, or deep ravines",
        "example_el": "Προσέχετε όταν κολυμπάτε, τα νερά σε αυτή την παραλία είναι πολύ βαθιά.",
        "example_en": "Be careful when you swim; the waters at this beach are very deep.",
        "example2_el": "Το φαράγγι της Σαμαριάς έχει εντυπωσιακά βαθιά περάσματα.",
        "example2_en": "The Samaria gorge has impressively deep passes."
    },
    {
        "id": "A2-U08-023",
        "greek": "βαρύς",
        "english": "heavy / severe (winter)",
        "notes": "Adjective in -ύς, -ιά, -ύ (βαρύς, βαριά, βαρύ). Used for physical weight or harsh winter ('βαρύς χειμώνας').",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "βαριά",
            "neuter": "βαρύ",
            "plural_masculine": "βαριοί",
            "plural_feminine": "βαριές",
            "plural_neuter": "βαριά"
        },
        "keg_communicative_function": "Describing luggage weight or harsh climatic conditions",
        "example_el": "Η βαλίτσα μου είναι πολύ βαριά και δυσκολεύομαι να τη σηκώσω.",
        "example_en": "My suitcase is very heavy and I have difficulty lifting it.",
        "example2_el": "Φέτος περιμένουμε έναν βαρύ χειμώνα με πολλά χιόνια στα βόρεια.",
        "example2_en": "This year we expect a severe winter with heavy snow in the north."
    },
    {
        "id": "A2-U08-024",
        "greek": "ελαφρύς",
        "english": "light (weight) / mild (weather)",
        "notes": "Adjective in -ύς, -ιά, -ύ (ελαφρύς, ελαφριά, ελαφρύ). Antonym: 'βαρύς'.",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "ελαφριά",
            "neuter": "ελαφρύ",
            "antonym": "βαρύς"
        },
        "keg_communicative_function": "Describing light clothing, mild breezes, or light meals",
        "example_el": "Το καλοκαίρι στην Ελλάδα καλό είναι να φοράτε ελαφριά βαμβακερά ρούχα.",
        "example_en": "In summer in Greece it is wise to wear light cotton clothes.",
        "example2_el": "Ένα ελαφρύ αεράκι έκανε τη ζέστη του απογεύματος υποφερτή.",
        "example2_en": "A light breeze made the afternoon heat bearable."
    },
    {
        "id": "A2-U08-025",
        "greek": "πλατύς",
        "english": "wide / broad",
        "notes": "Adjective in -ύς, -ιά, -ύ (πλατύς, πλατιά, πλατύ). Antonym: 'στενός' (narrow).",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "πλατιά",
            "neuter": "πλατύ",
            "antonym": "στενός, -ή, -ό"
        },
        "keg_communicative_function": "Describing avenues, rivers, or squares in directional dialogues",
        "example_el": "Η λεωφόρος είναι πολύ πλατιά με τέσσερις λωρίδες κυκλοφορίας.",
        "example_en": "The avenue is very wide with four traffic lanes.",
        "example2_el": "Καθίσαμε κάτω από την πλατιά σκιά ενός μεγάλου πλάτανου στην πλατεία.",
        "example2_en": "We sat under the broad shade of a large plane tree in the square."
    },
    {
        "id": "A2-U08-026",
        "greek": "η υγρασία",
        "english": "humidity",
        "notes": "Feminine noun in -α. High in coastal Greek cities and islands during summer and winter.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "adjective": "υγρός, -ή, -ό (humid / moist)",
            "collocation": "ποσοστό υγρασίας (humidity percentage)"
        },
        "keg_communicative_function": "Discussing comfort levels and weather conditions in different Greek regions",
        "example_el": "Στη Θεσσαλονίκη το καλοκαίρι η υγρασία κάνει τη ζέστη πιο αποπνικτική.",
        "example_en": "In Thessaloniki in summer the humidity makes the heat more suffocating.",
        "example2_el": "Το ποσοστό της υγρασίας σήμερα αγγίζει το ογδόντα τοις εκατό.",
        "example2_en": "The humidity percentage today reaches eighty percent."
    },
    {
        "id": "A2-U08-027",
        "greek": "το κύμα",
        "english": "wave (sea wave / heatwave)",
        "notes": "Neuter noun in -μα (-ματα). Plural: 'τα κύματα'.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κύματα",
            "genitive_singular": "του κύματος",
            "collocation": "κύμα καύσωνα (heatwave)"
        },
        "keg_communicative_function": "Describing sea conditions or metaphorical weather waves (cold/heat)",
        "example_el": "Τα κύματα ήταν τόσο ψηλά που απαγορεύτηκε το κολύμπι στους λουόμενους.",
        "example_en": "The waves were so high that swimming was prohibited to bathers.",
        "example2_el": "Ακούγαμε τον ήχο των κυμάτων να σπάνε πάνω στα βράχια.",
        "example2_en": "We heard the sound of waves crashing on the rocks."
    },
    {
        "id": "A2-U08-028",
        "greek": "παγώνει",
        "english": "it freezes / it turns icy",
        "notes": "Impersonal or active verb. Past: 'πάγωσε'. Used for winter ice on roads or freezing cold.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "πάγωσε",
            "noun": "ο πάγος (ice)"
        },
        "keg_communicative_function": "Discussing sub-zero winter road hazards and ice warnings",
        "example_el": "Τη νύχτα η θερμοκρασία πέφτει κάτω από το μηδέν και ο δρόμος παγώνει.",
        "example_en": "At night the temperature drops below zero and the road freezes.",
        "example2_el": "Πάγωσα από το κρύο περιμένοντας στη στάση του λεωφορείου.",
        "example2_en": "I froze from the cold waiting at the bus stop."
    },
    {
        "id": "A2-U08-029",
        "greek": "η ψύχρα",
        "english": "chill / coolness",
        "notes": "Feminine noun in -α. Mild cold typical of Greek autumn and spring evenings.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "adjective": "ψυχρός, -ή, -ό",
            "phrase": "κάνει ψύχρα (it's chilly)"
        },
        "keg_communicative_function": "Advising friends to bring a jacket for evening breezes",
        "example_el": "Το βράδυ δίπλα στη θάλασσα βγάζει ψύχρα, γι' αυτό πάρε μαζί σου μια ζακέτα.",
        "example_en": "At night beside the sea it gets chilly, so take a cardigan with you.",
        "example2_el": "Παρά την πρωινή ψύχρα, το μεσημέρι ο ήλιος ζέστανε την ατμόσφαιρα.",
        "example2_en": "Despite the morning chill, at noon the sun warmed the atmosphere."
    },
    {
        "id": "A2-U08-030",
        "greek": "η πρόγνωση",
        "english": "forecast / prognosis",
        "notes": "Feminine noun in -η (-εις). Scientific synonym of 'η πρόβλεψη' (forecast).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι προγνώσεις",
            "collocation": "πρόγνωση καιρού (weather forecast)"
        },
        "keg_communicative_function": "Interpreting meteorological bulletins and planning activities according to forecasts",
        "example_el": "Η πρόγνωση του καιρού για τις επόμενες μέρες δείχνει σταδιακή βελτίωση.",
        "example_en": "The weather forecast for the coming days shows gradual improvement.",
        "example2_el": "Σύμφωνα με τις προγνώσεις των ειδικών, η άνοιξη θα ξεκινήσει με ήπιες θερμοκρασίες.",
        "example2_en": "According to experts' forecasts, spring will begin with mild temperatures."
    },
    {
        "id": "A2-U08-031",
        "greek": "η προειδοποίηση",
        "english": "warning / alert",
        "notes": "Feminine noun in -η (-εις). Often issued by the civil protection authority (Πολιτική Προστασία).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι προειδοποιήσεις",
            "verb": "προειδοποιώ"
        },
        "keg_communicative_function": "Understanding emergency text messages and severe weather warnings",
        "example_el": "Λάβαμε έκτακτη προειδοποίηση στο κινητό για επικίνδυνα καιρικά φαινόμενα.",
        "example_en": "We received an emergency alert on our phone for dangerous weather phenomena.",
        "example2_el": "Η μετεωρολογική υπηρεσία εξέδωσε προειδοποίηση για θυελλώδεις ανέμους.",
        "example2_en": "The meteorological service issued a warning for gale-force winds."
    },
    {
        "id": "A2-U08-032",
        "greek": "το φαινόμενο",
        "english": "phenomenon",
        "notes": "Neuter noun in -ο (-α). Plural: 'τα φαινόμενα'. Collocates with 'καιρικά φαινόμενα'.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα φαινόμενα",
            "collocation": "έντονα καιρικά φαινόμενα (severe weather events)"
        },
        "keg_communicative_function": "Analyzing natural phenomena in news articles of Reading Part 2",
        "example_el": "Τα έντονα καιρικά φαινόμενα θα εξασθενήσουν σταδιακά από αύριο το πρωί.",
        "example_en": "The severe weather phenomena will gradually weaken starting tomorrow morning.",
        "example2_el": "Η έκλειψη ηλίου είναι ένα σπάνιο αστρονομικό φαινόμενο.",
        "example2_en": "A solar eclipse is a rare astronomical phenomenon."
    },
    {
        "id": "A2-U08-033",
        "greek": "ο βαθμός Κελσίου",
        "english": "degree Celsius",
        "notes": "Masculine noun phrase. Essential unit for temperatures across Greece.",
        "gender_or_pos": "noun phrase (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "plural": "οι βαθμοί Κελσίου",
            "syntax": "στους είκοσι βαθμούς (at twenty degrees)"
        },
        "keg_communicative_function": "Understanding and stating exact temperatures in weather reports",
        "example_el": "Το θερμόμετρο στην κεντρική πλατεία έδειχνε τριάντα οκτώ βαθμούς Κελσίου.",
        "example_en": "The thermometer in the central square showed thirty-eight degrees Celsius.",
        "example2_el": "Η θερμοκρασία κυμαίνεται από δώδεκα έως είκοσι βαθμούς Κελσίου.",
        "example2_en": "The temperature ranges from twelve to twenty degrees Celsius."
    },
    {
        "id": "A2-U08-034",
        "greek": "το νησιωτικό σύμπλεγμα",
        "english": "island complex / archipelago",
        "notes": "Neuter noun phrase. Formal geographical term (π.χ. Κυκλάδες, Δωδεκάνησα, Επτάνησα).",
        "gender_or_pos": "noun phrase (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "plural": "τα νησιωτικά συμπλέγματα",
            "examples": "Κυκλάδες, Σποράδες, Δωδεκάνησα"
        },
        "keg_communicative_function": "Recognizing major regional island groups in geographic and cultural texts",
        "example_el": "Οι Κυκλάδες είναι ένα διάσημο νησιωτικό σύμπλεγμα στην καρδιά του Αιγαίου.",
        "example_en": "The Cyclades are a famous island complex in the heart of the Aegean.",
        "example2_el": "Το σύμπλεγμα των Δωδεκανήσων βρίσκεται στο νοτιοανατολικό άκρο της Ελλάδας.",
        "example2_en": "The Dodecanese complex is located at the southeastern tip of Greece."
    },
    {
        "id": "A2-U08-035",
        "greek": "το περιβάλλον",
        "english": "the environment",
        "notes": "Neuter noun in -ον (-οντος). Collocates with 'προστασία του περιβάλλοντος' (environmental protection).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "genitive_singular": "του περιβάλλοντος",
            "adjective": "περιβαλλοντικός, -ή, -ό"
        },
        "keg_communicative_function": "Discussing ecology, nature conservation, and recycling in A2 thematic essays",
        "example_el": "Ο σεβασμός προς το φυσικό περιβάλλον αποτελεί βασική αξία της κοινωνίας μας.",
        "example_en": "Respect for the natural environment constitutes a fundamental value of our society.",
        "example2_el": "Η ανακύκλωση και η μείωση του πλαστικού βοηθούν στην προστασία του περιβάλλοντος.",
        "example2_en": "Recycling and reducing plastic help protect the environment."
    }
]

def synthesize_audio_threaded(cards, unit_id):
    tasks = []
    for c in cards:
        cid = c["id"]
        # Headword
        grk = c["greek"]
        h_fn = generate_audio_filename(grk)
        h_path = AUDIO_DIR / h_fn
        c["audio"] = h_fn
        c["status"] = "verified"
        if not h_path.exists() or h_path.stat().st_size == 0:
            tasks.append((cid, "Headword", grk, h_fn, h_path))

        # Ex 1
        ex1 = c["example_el"]
        fn1 = generate_audio_filename(ex1)
        p1 = AUDIO_DIR / fn1
        c["example_audio"] = fn1
        if not p1.exists() or p1.stat().st_size == 0:
            tasks.append((cid, "Ex1", ex1, fn1, p1))

        # Ex 2
        ex2 = c["example2_el"]
        fn2 = generate_audio_filename(ex2)
        p2 = AUDIO_DIR / fn2
        c["example2_audio"] = fn2
        if not p2.exists() or p2.stat().st_size == 0:
            tasks.append((cid, "Ex2", ex2, fn2, p2))

    total_needed = len(tasks)
    print(f"[{unit_id}] Synthesizing {total_needed} missing audio files using 8 parallel worker threads...")

    completed = 0
    t0 = time.time()

    def worker(task):
        cid, label, text, fn, path = task
        try:
            b = synthesize_greek_chirp(text)
            with open(path, "wb") as f_out:
                f_out.write(b)
            return True, cid, label, fn
        except Exception as e:
            return False, cid, label, str(e)

    with ThreadPoolExecutor(max_workers=8) as executor:
        for ok, cid, label, res in executor.map(worker, tasks):
            completed += 1
            if ok:
                if completed % 10 == 0 or completed == total_needed:
                    print(f"  [{unit_id}] {completed}/{total_needed} done ({time.time()-t0:.1f}s)")
            else:
                print(f"  [ERROR] {cid} {label}: {res}")

    print(f"[{unit_id}] Parallel audio synthesis complete in {time.time()-t0:.2f}s ({completed} files).")
    return total_needed

def save_unit_yaml(unit_id, lesson_id, title, description, lesson_notes, cards):
    unit_dir = CONTENT_DIR / unit_id
    unit_dir.mkdir(parents=True, exist_ok=True)
    yaml_file = unit_dir / f"{lesson_id}.yaml"
    
    lesson_data = {
        "unit_id": unit_id,
        "lesson_id": lesson_id,
        "title": title,
        "description": description,
        "lesson_status": "not_started",
        "lesson_notes": lesson_notes,
        "entries": cards
    }
    
    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(lesson_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"[{unit_id}] Saved {len(cards)} cards to {yaml_file}")

def update_manifest():
    manifest_path = CONTENT_DIR / "manifest.yaml"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)
        
    units = manifest.get("units", [])
    existing_ids = {u["id"] for u in units}
    
    batch4_entries = [
        {
            "id": "unit-a2-07",
            "title": "Μάθημα 7: Ταξίδια, Διακοπές & Κρατήσεις (Travel, Vacations & Reservations)",
            "description": "Making hotel and transport bookings, discussing departure and arrival schedules, and comparing prices and travel duration using comparative adjectives (πιο, καλύτερος, φθηνότερος, ακριβότερος, γρηγορότερος).",
            "order": "KEG-A2-07-A",
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2-07/lesson-01.yaml",
                    "title": "Μάθημα 7: Ταξίδια, Διακοπές & Κρατήσεις (Travel, Vacations & Reservations)"
                }
            ]
        },
        {
            "id": "unit-a2-08",
            "title": "Μάθημα 8: Καιρός, Φύση & Γεωγραφία της Ελλάδας (Weather, Nature & Geography)",
            "description": "Interpreting weather bulletins, seasonal forecasts, and maritime Beaufort scales, describing Greek geography (mountains, islands, rivers, lakes), and mastering adjectives in -ύς, -ιά, -ύ (βαθύς, βαρύς, ελαφρύς, πλατύς).",
            "order": "KEG-A2-08-A",
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2-08/lesson-01.yaml",
                    "title": "Μάθημα 8: Καιρός, Φύση & Γεωγραφία της Ελλάδας (Weather, Nature & Geography)"
                }
            ]
        }
    ]
    
    added = 0
    for entry in batch4_entries:
        if entry["id"] not in existing_ids:
            units.append(entry)
            existing_ids.add(entry["id"])
            added += 1
            print(f"[Manifest] Appended {entry['id']} ({entry['order']})")
        else:
            for u in units:
                if u["id"] == entry["id"]:
                    u["lessons"] = entry["lessons"]
            print(f"[Manifest] {entry['id']} already exists, verified lessons array")
            
    manifest["units"] = units
    with open(manifest_path, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"[Manifest] Manifest saved with {len(units)} units total ({added} new).")

def main():
    print("--- Starting KEG-A2 Batch 4 Generation & Parallel Synthesis ---")
    
    # 1. Unit A2-07
    u7_notes = """Unit A2-07 Core Notes: Ταξίδια, Διακοπές & Κρατήσεις (Travel & Comparisons)
• Travel Logistics & Bookings:
  - κράτηση (reservation), εισιτήριο μετ' επιστροφής (return ticket), διαμονή (stay), μονόκλινο / δίκλινο (single/double room).
  - Transit milestones: αναχώρηση (departure), άφιξη (arrival), πύλη επιβίβασης (gate), κάρτα επιβίβασης (boarding pass).
  - Maritime vocabulary: κατάστρωμα (deck), καμπίνα (cabin), λιμάνι (port).

• Degrees of Comparison (Παραθετικά):
  - Analytic comparative: πιο + adjective (πιο άνετος, πιο γρήγορος).
  - Synthetic comparative: -ότερος, -ύτερος (φθηνότερος, ακριβότερος, γρηγορότερος).
  - Irregular comparative: καλός -> καλύτερος (better).
  - Construction: 'Α είναι πιο ... από Β' (A is more ... than B)."""

    synthesize_audio_threaded(CARDS_U07, "unit-a2-07")
    save_unit_yaml(
        unit_id="unit-a2-07",
        lesson_id="lesson-01",
        title="Μάθημα 7: Ταξίδια, Διακοπές & Κρατήσεις (Travel, Vacations & Reservations)",
        description="Making hotel and transport bookings, discussing departure and arrival schedules, and comparing prices and travel duration using comparative adjectives (πιο, καλύτερος, φθηνότερος, ακριβότερος, γρηγορότερος).",
        lesson_notes=u7_notes,
        cards=CARDS_U07
    )

    # 2. Unit A2-08
    u8_notes = """Unit A2-08 Core Notes: Καιρός, Φύση & Γεωγραφία (Weather & Geography)
• Meteorological Lexicon & Radio Bulletins:
  - θερμοκρασία (temperature in βαθμοί Κελσίου), ηλιοφάνεια (sunshine), συννεφιά (cloudiness), καταιγίδα (thunderstorm).
  - Maritime winds: άνεμος (wind) measured in μποφόρ (Beaufort scale 1-12).
  - Severe phenomena: καύσωνας (heatwave), κακοκαιρία (storm/bad weather).

• Adjectives in -ύς, -ιά, -ύ (Third Declension Stems):
  - Singular: ο βαθύς, η βαθιά, το βαθύ.
  - Plural: οι βαθιοί, οι βαθιές, τα βαθιά.
  - Paradigms: βαρύς (heavy), ελαφρύς (light), πλατύς (wide), παχύς (thick).

• Geographical Landscape:
  - το βουνό (mountain), η θάλασσα (sea), το ποτάμι (river), η λίμνη (lake), η πεδιάδα (plain), το δάσος (forest, genitive του δάσους)."""

    synthesize_audio_threaded(CARDS_U08, "unit-a2-08")
    save_unit_yaml(
        unit_id="unit-a2-08",
        lesson_id="lesson-01",
        title="Μάθημα 8: Καιρός, Φύση & Γεωγραφία της Ελλάδας (Weather, Nature & Geography)",
        description="Interpreting weather bulletins, seasonal forecasts, and maritime Beaufort scales, describing Greek geography (mountains, islands, rivers, lakes), and mastering adjectives in -ύς, -ιά, -ύ (βαθύς, βαρύς, ελαφρύς, πλατύς).",
        lesson_notes=u8_notes,
        cards=CARDS_U08
    )

    # 3. Update manifest
    update_manifest()
    print("\n[OK] Batch 4 generation and parallel synthesis finished successfully!")

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Generate KEG-A2 Speaking Examination Curriculum — Batch 2:
- Unit SP-03 (SP-03-A): Stage 2 Cue Card Scenarios & Bilateral Roleplays (40 cards)
- Unit SP-04 (SP-04-A): Stage 3 Visual Description Lego Framework (40 cards)
Includes dual spoken exam responses and multi-threaded Google Cloud Chirp-3 HD TTS.
Note: Does NOT modify content/manifest.yaml (managed by parent coordinator).
"""
import sys
import time
import unicodedata
import yaml
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from server.tts_service import synthesize_greek_chirp, generate_audio_filename

AUDIO_DIR = BASE_DIR / "audio"
CONTENT_DIR = BASE_DIR / "content"


def nfc(text: str) -> str:
    return unicodedata.normalize("NFC", text.strip())


# ---------------------------------------------------------------------------
# UNIT SP-03: Stage 2 Cue Card Scenarios & Bilateral Roleplays (40 cards)
# ---------------------------------------------------------------------------
CARDS_SP_03 = [
    # --- Scenario 1: At the Travel Agency / Ferry Ticket Office (001-007) ---
    {
        "id": "SP-U03-001",
        "greek": "Καλημέρα σας, θα ήθελα να μάθω τι ώρα φεύγει το πρωινό πλοίο για την Πάρο.",
        "english": "Good morning, I would like to find out what time the morning ferry leaves for Paros. (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Polite conditional 'θα ήθελα να μάθω', indirect time question 'τι ώρα φεύγει'"
        },
        "notes": "Examiner Objective: Tests polite indirect question formation at a ticket desk.\nStrategy: Open with a greeting + 'θα ήθελα να μάθω' rather than a blunt question, and mention whether you prefer a morning or evening departure.",
        "example_el": "Καλημέρα σας! Θα ήθελα να μάθω τι ώρα φεύγει το πρωινό πλοίο για την Πάρο την Παρασκευή και πόσες ώρες διαρκεί συνολικά το ταξίδι από τον Πειραιά.",
        "example_en": "Good morning! I would like to find out what time the morning ferry leaves for Paros on Friday and how many hours the trip from Piraeus lasts in total.",
        "example2_el": "Το πρωινό πλοίο αναχωρεί στις επτά και μισή ακριβώς από τον Πειραιά και φτάνει στο λιμάνι της Πάρου σε τέσσερις ώρες.",
        "example2_en": "The morning ferry departs at seven-thirty sharp from Piraeus and arrives at the port of Paros in four hours.",
        "keg_communicative_function": "Inquiring about ferry departure times and journey duration at a travel agency"
    },
    {
        "id": "SP-U03-002",
        "greek": "Μήπως γνωρίζετε αν υπάρχει απογευματινό δρομολόγιο για την επιστροφή την Κυριακή;",
        "english": "Do you happen to know if there is an afternoon route for the return on Sunday? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Tentative polite opener 'μήπως γνωρίζετε αν', return schedule vocabulary"
        },
        "notes": "Examiner Objective: Evaluates ability to verify return schedules using indirect 'αν' clauses.\nStrategy: Combine 'μήπως γνωρίζετε αν...' with the specific day and time of day on your cue card.",
        "example_el": "Μήπως γνωρίζετε αν υπάρχει απογευματινό δρομολόγιο για την επιστροφή μας την Κυριακή, γιατί δεν θέλουμε να φύγουμε πολύ νωρίς το πρωί από το νησί;",
        "example_en": "Do you happen to know if there is an afternoon route for our return on Sunday, because we do not want to leave very early in the morning from the island?",
        "example2_el": "Βεβαίως, την Κυριακή υπάρχει ένα γρήγορο πλοίο στις έξι το απόγευμα και ένα βραδινό στις εννέα παρά τέταρτο.",
        "example2_en": "Certainly, on Sunday there is a fast ferry at six in the afternoon and an evening one at a quarter to nine.",
        "keg_communicative_function": "Asking about return travel schedules and expressing time preferences"
    },
    {
        "id": "SP-U03-003",
        "greek": "Πόσο κοστίζει το απλό εισιτήριο στο κατάστρωμα και πόσο η αριθμημένη θέση;",
        "english": "How much does the standard deck ticket cost and how much is the numbered seat? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Price comparison 'πόσο κοστίζει', ferry seating vocabulary (κατάστρωμα vs. αριθμημένη θέση)"
        },
        "notes": "Examiner Objective: Tests comparative price inquiry and maritime travel terminology.\nStrategy: Ask clearly about both options shown on the roleplay card so your partner can give the full price breakdown.",
        "example_el": "Θα μπορούσατε να μου πείτε πόσο κοστίζει το απλό εισιτήριο στο κατάστρωμα και ποια είναι η διαφορά τιμής αν κλείσουμε αριθμημένη θέση στο σαλόνι;",
        "example_en": "Could you tell me how much the standard deck ticket costs and what the price difference is if we book a numbered seat in the lounge?",
        "example2_el": "Το εισιτήριο στο κατάστρωμα κοστίζει σαράντα ευρώ, ενώ η αριθμημένη θέση αεροπορικού τύπου κοστίζει σαράντα οκτώ ευρώ το άτομο.",
        "example2_en": "The deck ticket costs forty euros, whereas the airplane-style numbered seat costs forty-eight euros per person.",
        "keg_communicative_function": "Comparing ticket classes and prices for ferry travel"
    },
    {
        "id": "SP-U03-004",
        "greek": "Υπάρχουν διαθέσιμες δίκλινες ή τετράκλινες καμπίνες για το βραδινό ταξίδι;",
        "english": "Are there two-bed or four-bed cabins available for the night trip? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Plural adjective agreement 'διαθέσιμες δίκλινες/τετράκλινες καμπίνες', accommodation inquiry"
        },
        "notes": "Examiner Objective: Assesses compound numerical adjectives (δίκλινη, τετράκλινη) and availability questions.\nStrategy: Justify why you need a cabin (e.g., traveling at night or with family) to produce a richer turn.",
        "example_el": "Επειδή ταξιδεύουμε βράδυ με τα παιδιά μας, θα ήθελα να ρωτήσω αν υπάρχουν διαθέσιμες τετράκλινες εσωτερικές καμπίνες και πόσο κοστίζουν συνολικά.",
        "example_en": "Because we are traveling at night with our children, I would like to ask if there are four-bed interior cabins available and how much they cost in total.",
        "example2_el": "Ναι, αυτή τη στιγμή έχουμε δύο διαθέσιμες τετράκλινες καμπίνες με δικό τους μπάνιο στην τιμή των εκατόν εξήντα ευρώ.",
        "example2_en": "Yes, right now we have two available four-bed cabins with their own bathroom at the price of one hundred and sixty euros.",
        "keg_communicative_function": "Inquiring about cabin availability and sleeping accommodations on a ship"
    },
    {
        "id": "SP-U03-005",
        "greek": "Θέλουμε να πάρουμε μαζί και το αυτοκίνητό μας· πόσο είναι το εισιτήριο για το όχημα;",
        "english": "We want to bring our car along too; how much is the ticket for the vehicle? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Subjunctive 'να πάρουμε μαζί', possessive clitic 'το αυτοκίνητό μας', vehicle fare inquiry"
        },
        "notes": "Examiner Objective: Tests enclitic stress rule ('το αυτοκίνητό μας') and practical vehicle booking questions.\nStrategy: Mention the size of the car and ask how early you must arrive at the port for loading.",
        "example_el": "Σκοπεύουμε να πάρουμε μαζί και το μικρό αυτοκίνητό μας στο νησί, οπότε θα ήθελα να μάθω πόσο κοστίζει το εισιτήριο για το όχημα στο γκαράζ.",
        "example_en": "We plan to bring our small car along to the island, so I would like to find out how much the ticket for the vehicle in the garage costs.",
        "example2_el": "Για ένα κανονικό επιβατικό αυτοκίνητο το εισιτήριο κοστίζει εβδομήντα πέντε ευρώ, αλλά πρέπει να είστε στο λιμάνι μία ώρα νωρίτερα.",
        "example2_en": "For a standard passenger car the ticket costs seventy-five euros, but you must be at the port one hour earlier.",
        "keg_communicative_function": "Asking about vehicle ferry fares and boarding requirements"
    },
    {
        "id": "SP-U03-006",
        "greek": "Ισχύει κάποια φοιτητική έκπτωση αν έχω μαζί μου το φοιτητικό μου πάσο;",
        "english": "Does a student discount apply if I have my student pass with me? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Real conditional 'αν έχω...', impersonal verb 'ισχύει', discount terminology"
        },
        "notes": "Examiner Objective: Checks conditional clauses ('αν + present') and student/youth discount vocabulary.\nStrategy: Ask what percentage discount applies and whether you must show the card during boarding.",
        "example_el": "Είμαι φοιτητής στο πανεπιστήμιο της Αθήνας και θα ήθελα να ρωτήσω αν ισχύει κάποια έκπτωση στα εισιτήρια όταν δείξω το φοιτητικό μου πάσο.",
        "example_en": "I am a university student in Athens and I would like to ask if a discount applies to the tickets when I show my student pass.",
        "example2_el": "Φυσικά, με το ελληνικό φοιτητικό πάσο έχετε έκπτωση πενήντα τοις εκατό τόσο στο κατάστρωμα όσο και στις αριθμημένες θέσεις.",
        "example2_en": "Of course, with the Greek student pass you have a fifty percent discount both on deck and in the numbered seats.",
        "keg_communicative_function": "Inquiring about ticket discounts and required identification documents"
    },
    {
        "id": "SP-U03-007",
        "greek": "Από ποια πύλη του λιμανιού φεύγει το πλοίο και πώς μπορούμε να πάμε εκεί;",
        "english": "From which port gate does the ship leave and how can we get there? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Prepositional interrogative 'από ποια πύλη', genitive singular 'του λιμανιού', directions"
        },
        "notes": "Examiner Objective: Tests spatial/directional questions at the close of a travel transaction.\nStrategy: Combine the port gate question with how close it is to the electric train (ηλεκτρικός) or metro station.",
        "example_el": "Τέλεια, θα κλείσουμε αυτά τα δύο εισιτήρια! Μήπως μπορείτε να μου πείτε από ποια πύλη του λιμανιού φεύγει το πλοίο και αν είναι κοντά στο μετρό;",
        "example_en": "Great, we will book these two tickets! Could you perhaps tell me from which gate of the port the ship leaves and whether it is close to the metro?",
        "example2_el": "Το πλοίο για τις Κυκλάδες αναχωρεί από την πύλη Ε7, η οποία βρίσκεται μόλις πέντε λεπτά με τα πόδια από τον σταθμό του μετρό.",
        "example2_en": "The ship for the Cyclades departs from gate E7, which is located just five minutes on foot from the metro station.",
        "keg_communicative_function": "Confirming departure gates and local transit connections at a port"
    },

    # --- Scenario 2: At the Pharmacy / Medical Clinic (008-014) ---
    {
        "id": "SP-U03-008",
        "greek": "Καλησπέρα σας, από χθες το βράδυ έχω δυνατό πονόλαιμο και λίγο πυρετό.",
        "english": "Good evening, since last night I have had a strong sore throat and a slight fever. (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Present tense with 'από χθες' for ongoing symptoms, medical symptom nouns (πονόλαιμος, πυρετός)"
        },
        "notes": "Examiner Objective: Tests ability to describe physical symptoms clearly using Greek present tense for duration ('από χθες έχω...').\nStrategy: Name two symptoms and ask the pharmacist what they recommend.",
        "example_el": "Καλησπέρα σας! Από χθες το βράδυ έχω πολύ δυνατό πονόλαιμο, βήχα και λίγο πυρετό, και δυσκολεύομαι να καταπιώ. Τι θα μπορούσατε να μου δώσετε;",
        "example_en": "Good evening! Since last night I have had a very strong sore throat, a cough, and a slight fever, and I have trouble swallowing. What could you give me?",
        "example2_el": "Κατάλαβα, μάλλον πρόκειται για κάποιο κρυολόγημα. Μπορώ να σας δώσω αυτό το φυτικό σιρόπι και παστίλιες που μαλακώνουν αμέσως τον λαιμό.",
        "example2_en": "I understand, it is probably a cold. I can give you this herbal syrup and lozenges that immediately soothe the throat.",
        "keg_communicative_function": "Describing cold and flu symptoms and asking for advice at a pharmacy"
    },
    {
        "id": "SP-U03-009",
        "greek": "Με έπιασε ξαφνικά αλλεργία από τον ήλιο· έχετε κάποια καταπραϋντική κρέμα;",
        "english": "I suddenly got a sun allergy; do you have a soothing cream? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Idiomatic symptom expression 'με έπιασε αλλεργία', pharmacy product inquiry"
        },
        "notes": "Examiner Objective: Rewards idiomatic Greek medical expressions ('με έπιασε πονοκέφαλος / αλλεργία').\nStrategy: Explain where the rash/irritation is and ask for an ointment or cream.",
        "example_el": "Σήμερα το μεσημέρι στην παραλία με έπιασε ξαφνικά αλλεργία από τον ήλιο και κοκκίνισαν τα χέρια μου. Έχετε κάποια καλή κρέμα για τη φαγούρα;",
        "example_en": "Today at noon at the beach I suddenly got a sun allergy and my arms turned red. Do you have a good cream for the itching?",
        "example2_el": "Ναι, αυτή η δροσιστική αλοιφή με αλόη είναι εξαιρετική για τον ερεθισμό από τον ήλιο και δεν χρειάζεται ιατρική συνταγή.",
        "example2_en": "Yes, this cooling ointment with aloe is excellent for irritation from the sun and does not require a medical prescription.",
        "keg_communicative_function": "Explaining an allergic reaction or skin irritation at a pharmacy"
    },
    {
        "id": "SP-U03-010",
        "greek": "Πόσες φορές την ημέρα πρέπει να παίρνω αυτό το σιρόπι και για πόσες μέρες;",
        "english": "How many times a day must I take this syrup and for how many days? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Frequency expression 'πόσες φορές την ημέρα', obligation 'πρέπει να παίρνω' (continuous aspect)"
        },
        "notes": "Examiner Objective: Tests continuous subjunctive ('να παίρνω') for repeated medical dosage.\nStrategy: Ask both the daily frequency and the total number of days for the treatment.",
        "example_el": "Σας ευχαριστώ πολύ! Θα ήθελα να ρωτήσω πόσες φορές την ημέρα πρέπει να παίρνω αυτό το σιρόπι και για πόσες μέρες συνολικά να συνεχίσω τη θεραπεία.",
        "example_en": "Thank you very much! I would like to ask how many times a day I must take this syrup and for how many days in total I should continue the treatment.",
        "example2_el": "Θα παίρνετε ένα κουταλάκι της σούπας τρεις φορές την ημέρα, πρωί, μεσημέρι και βράδυ, για πέντε συνεχόμενες ημέρες.",
        "example2_en": "You will take one tablespoon three times a day, morning, noon, and night, for five consecutive days.",
        "keg_communicative_function": "Asking for and receiving medication dosage instructions"
    },
    {
        "id": "SP-U03-011",
        "greek": "Τα χάπια αυτά τα παίρνω πριν ή μετά το φαγητό, με γεμάτο στομάχι;",
        "english": "Do I take these pills before or after food, on a full stomach? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Clitic doubling 'τα χάπια αυτά τα παίρνω', temporal prepositions 'πριν / μετά το φαγητό'"
        },
        "notes": "Examiner Objective: Tests natural spoken clitic resumption ('τα χάπια τα παίρνω') and medication precautions.\nStrategy: Mention if you have a sensitive stomach to make the exchange realistic.",
        "example_el": "Επειδή έχω λίγο ευαίσθητο στομάχι, μήπως μπορείτε να μου διευκρινίσετε αν αυτά τα παυσίπονα χάπια πρέπει να τα παίρνω πριν ή μετά το φαγητό;",
        "example_en": "Because I have a slightly sensitive stomach, could you perhaps clarify whether I must take these painkiller pills before or after food?",
        "example2_el": "Είναι πολύ σημαντικό να τα παίρνετε πάντα μετά από ένα καλό γεύμα με ένα μεγάλο ποτήρι νερό, ποτέ με άδειο στομάχι.",
        "example2_en": "It is very important that you always take them after a good meal with a large glass of water, never on an empty stomach.",
        "keg_communicative_function": "Clarifying instructions for taking medication safely with meals"
    },
    {
        "id": "SP-U03-012",
        "greek": "Μήπως χρειάζεται συνταγή γιατρού για αυτό το φάρμακο ή δίνεται ελεύθερα;",
        "english": "Is a doctor's prescription needed for this medicine or is it given over the counter? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Impersonal 'χρειάζεται', genitive modifier 'συνταγή γιατρού', passive 'δίνεται ελεύθερα'"
        },
        "notes": "Examiner Objective: Assesses knowledge of pharmacy regulations vocabulary ('συνταγή γιατρού', 'αντιβίωση').\nStrategy: Contrast prescription antibiotics with simple over-the-counter painkillers.",
        "example_el": "Μήπως χρειάζεται ηλεκτρονική συνταγή γιατρού για να αγοράσω αυτό το φάρμακο, ή μπορώ να το πάρω ελεύθερα από το φαρμακείο σας σήμερα;",
        "example_en": "Is an electronic doctor's prescription needed to buy this medicine, or can I get it over the counter from your pharmacy today?",
        "example2_el": "Τα απλά παυσίπονα δίνονται ελεύθερα χωρίς συνταγή, αλλά αν χρειάζεστε αντιβίωση πρέπει οπωσδήποτε να σας εξετάσει πρώτα ένας γιατρός.",
        "example2_en": "Simple painkillers are given freely without a prescription, but if you need antibiotics a doctor must definitely examine you first.",
        "keg_communicative_function": "Inquiring about prescription requirements at a pharmacy"
    },
    {
        "id": "SP-U03-013",
        "greek": "Θα ήθελα να κλείσω ένα επείγον ραντεβού με τον παθολόγο· πότε έχει διαθέσιμη ώρα;",
        "english": "I would like to book an urgent appointment with the general practitioner; when does he have an available time? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Collocation 'κλείνω επείγον ραντεβού', medical specialty 'παθολόγος', availability inquiry"
        },
        "notes": "Examiner Objective: Tests medical appointment scheduling at a clinic reception.\nStrategy: State that it is urgent ('επείγον') and ask for the earliest slot today or tomorrow morning.",
        "example_el": "Καλημέρα σας, δεν αισθάνομαι καθόλου καλά από το πρωί και θα ήθελα να κλείσω ένα επείγον ραντεβού με τον παθολόγο. Πότε έχει διαθέσιμη ώρα σήμερα;",
        "example_en": "Good morning, I have not been feeling well at all since morning and I would like to book an urgent appointment with the physician. When does he have an available time today?",
        "example2_el": "Ο γιατρός δέχεται στο ιατρείο από τις πέντε το απόγευμα και υπάρχει ένα κενό στις έξι και μισή, αν σας εξυπηρετεί.",
        "example2_en": "The doctor sees patients at the clinic from five in the afternoon and there is an opening at six-thirty, if that suits you.",
        "keg_communicative_function": "Booking an urgent medical appointment at a doctor's office"
    },
    {
        "id": "SP-U03-014",
        "greek": "Πόσο κοστίζει η επίσκεψη στον γιατρό και τι χαρτιά πρέπει να έχω μαζί μου;",
        "english": "How much does the visit to the doctor cost and what documents must I have with me? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Noun 'η επίσκεψη', administrative requirements 'τι χαρτιά / βιβλιάριο υγείας'"
        },
        "notes": "Examiner Objective: Evaluates practical clinic inquiry regarding consultation fees and insurance/health cards.\nStrategy: Ask both the consultation fee and whether your health booklet or ID is needed.",
        "example_el": "Η ώρα στις έξι και μισή με βολεύει μια χαρά! Μπορείτε να μου πείτε πόσο κοστίζει η επίσκεψη στον γιατρό και αν χρειάζεται το βιβλιάριο υγείας μου;",
        "example_en": "The six-thirty slot suits me just fine! Can you tell me how much the visit to the doctor costs and whether my health booklet is needed?",
        "example2_el": "Η απλή επίσκεψη κοστίζει σαράντα ευρώ και καλό είναι να έχετε μαζί σας την ταυτότητά σας και τον αριθμό ασφάλισής σας.",
        "example2_en": "The standard visit costs forty euros and it is good to have your ID card and your insurance number with you.",
        "keg_communicative_function": "Asking about medical consultation fees and required insurance documents"
    },

    # --- Scenario 3: At the Real Estate Office / Renting an Apartment (015-021) ---
    {
        "id": "SP-U03-015",
        "greek": "Είδα την αγγελία σας για το δυάρι στο Παγκράτι· είναι ακόμα διαθέσιμο;",
        "english": "I saw your ad for the one-bedroom apartment in Pangrati; is it still available? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Aorist 'είδα την αγγελία', Greek housing terminology 'δυάρι / γκαρσονιέρα'"
        },
        "notes": "Examiner Objective: Tests opening a real-estate inquiry using authentic Greek apartment terms ('δυάρι' = living room + 1 bedroom).\nStrategy: Reference where you saw the listing (in the newspaper or online) and ask if it is still available.",
        "example_el": "Καλημέρα σας, είδα στο διαδίκτυο την αγγελία σας για το φωτεινό δυάρι στο Παγκράτι και σας τηλεφωνώ για να μάθω αν είναι ακόμα διαθέσιμο.",
        "example_en": "Good morning, I saw your ad online for the bright one-bedroom apartment in Pangrati and I am calling you to find out if it is still available.",
        "example2_el": "Καλημέρα σας! Ναι, το διαμέρισμα στο Παγκράτι είναι ακόμα ελεύθερο και μπορούμε ευχαρίστως να σας δώσουμε όλες τις λεπτομέρειες.",
        "example2_en": "Good morning! Yes, the apartment in Pangrati is still available and we can gladly give you all the details.",
        "keg_communicative_function": "Initiating an inquiry about an apartment rental listing"
    },
    {
        "id": "SP-U03-016",
        "greek": "Πόσο είναι το μηνιαίο ενοίκιο και πόσα περίπου βγαίνουν τα κοινόχρηστα;",
        "english": "How much is the monthly rent and roughly how much do the shared building fees come to? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Key housing collocations 'μηνιαίο ενοίκιο', 'τα κοινόχρηστα', colloquial verb 'πόσα βγαίνουν'"
        },
        "notes": "Examiner Objective: Assesses mastery of essential Greek rental vocabulary ('ενοίκιο', 'κοινόχρηστα', 'εγγύηση').\nStrategy: Always ask about 'κοινόχρηστα' (shared building maintenance costs) alongside the monthly rent.",
        "example_el": "Θα ήθελα να ρωτήσω πόσο είναι το μηνιαίο ενοίκιο για το διαμέρισμα και πόσα ευρώ περίπου βγαίνουν τα κοινόχρηστα της πολυκατοικίας κάθε μήνα.",
        "example_en": "I would like to ask how much the monthly rent for the apartment is and roughly how many euros the building's shared fees come to each month.",
        "example2_el": "Το ενοίκιο είναι τετρακόσια ογδόντα ευρώ τον μήνα και τα κοινόχρηστα είναι πολύ χαμηλά, γύρω στα είκοσι πέντε ευρώ.",
        "example2_en": "The rent is four hundred and eighty euros per month and the shared building fees are very low, around twenty-five euros.",
        "keg_communicative_function": "Asking about monthly rent and shared building maintenance expenses"
    },
    {
        "id": "SP-U03-017",
        "greek": "Σε ποιον όροφο βρίσκεται το διαμέρισμα και υπάρχει ασανσέρ στην πολυκατοικία;",
        "english": "On which floor is the apartment located and is there an elevator in the apartment building? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Prepositional phrase 'σε ποιον όροφο', ordinal numbers ('στον τρίτο όροφο'), building features"
        },
        "notes": "Examiner Objective: Tests accusative interrogative 'σε ποιον όροφο' and ordinal numbers.\nStrategy: Pair the floor question with whether the building has a working elevator ('ασανσέρ').",
        "example_el": "Μήπως μπορείτε να μου πείτε σε ποιον όροφο βρίσκεται το διαμέρισμα, πόσα τετραγωνικά μέτρα είναι και αν υπάρχει σύγχρονο ασανσέρ στην πολυκατοικία;",
        "example_en": "Could you perhaps tell me on which floor the apartment is located, how many square meters it is, and whether there is a modern elevator in the building?",
        "example2_el": "Το διαμέρισμα είναι πενήντα πέντε τετραγωνικά μέτρα, βρίσκεται στον τρίτο όροφο και η πολυκατοικία διαθέτει καινούριο ασανσέρ.",
        "example2_en": "The apartment is fifty-five square meters, is located on the third floor, and the apartment building has a new elevator.",
        "keg_communicative_function": "Inquiring about apartment size, floor level, and building amenities"
    },
    {
        "id": "SP-U03-018",
        "greek": "Τι είδους θέρμανση έχει το σπίτι; Είναι αυτόνομη με φυσικό αέριο ή κεντρική;",
        "english": "What kind of heating does the home have? Is it autonomous with natural gas or central? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Genitive 'τι είδους θέρμανση', feminine adjective agreement 'αυτόνομη / κεντρική θέρμανση'"
        },
        "notes": "Examiner Objective: Evaluates high-frequency Greek real-estate terms ('αυτόνομη θέρμανση', 'φυσικό αέριο', 'κλιματιστικό').\nStrategy: Ask about both winter heating and whether there is air conditioning for the summer.",
        "example_el": "Επειδή τον χειμώνα κάνει αρκετό κρύο, θα ήθελα να μάθω τι είδους θέρμανση έχει το σπίτι· είναι αυτόνομη με φυσικό αέριο ή κεντρική με πετρέλαιο;",
        "example_en": "Because in winter it gets quite cold, I would like to find out what kind of heating the home has; is it autonomous with natural gas or central with oil?",
        "example2_el": "Έχει αυτόνομη θέρμανση με φυσικό αέριο, ώστε να την ανάβετε όποτε θέλετε, και επιπλέον υπάρχουν δύο καινούρια κλιματιστικά.",
        "example2_en": "It has autonomous heating with natural gas, so you can turn it on whenever you want, and additionally there are two new air conditioners.",
        "keg_communicative_function": "Asking about heating and cooling systems when renting a property"
    },
    {
        "id": "SP-U03-019",
        "greek": "Το διαμέρισμα έχει μεγάλο μπαλκόνι και βλέπει στον δρόμο ή στον ακάλυπτο;",
        "english": "Does the apartment have a big balcony and does it face the street or the inner courtyard? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Idiomatic spatial verb 'βλέπει σε...' (faces/overlooks), apartment layout nouns"
        },
        "notes": "Examiner Objective: Tests idiomatic usage of 'βλέπει στον δρόμο / στο πάρκο' and quietness inquiry.\nStrategy: Ask whether the bedroom is quiet and whether the balcony gets sunlight.",
        "example_el": "Θα ήθελα επίσης να ρωτήσω αν το διαμέρισμα έχει άνετο μπαλκόνι και αν βλέπει σε ήσυχο δρόμο, γιατί δουλεύω αρκετές ώρες από το σπίτι.",
        "example_en": "I would also like to ask whether the apartment has a comfortable balcony and whether it faces a quiet street, because I work many hours from home.",
        "example2_el": "Ναι, έχει μια μεγάλη βεράντα στην πρόσοψη που βλέπει σε έναν πολύ ήσυχο πεζόδρομο με δέντρα και έχει ήλιο όλη μέρα.",
        "example2_en": "Yes, it has a large veranda in the front that overlooks a very quiet pedestrian street with trees and gets sun all day.",
        "keg_communicative_function": "Asking about apartment orientation, balcony space, and noise levels"
    },
    {
        "id": "SP-U03-020",
        "greek": "Είναι κοντά σε σταθμό του μετρό, σε στάση λεωφορείου και σε σούπερ μάρκετ;",
        "english": "Is it close to a metro station, a bus stop, and a supermarket? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Spatial preposition 'κοντά σε + accusative', neighborhood infrastructure vocabulary"
        },
        "notes": "Examiner Objective: Tests neighborhood convenience questions and distance expressions ('δέκα λεπτά με τα πόδια').\nStrategy: Explain that you don't have a car, so public transport proximity is important to you.",
        "example_el": "Επειδή δεν έχω αυτοκίνητο, με ενδιαφέρει πολύ η τοποθεσία. Είναι το σπίτι κοντά σε σταθμό του μετρό, σε στάση λεωφορείου και σε σούπερ μάρκετ;",
        "example_en": "Because I do not have a car, the location interests me a lot. Is the house close to a metro station, a bus stop, and a supermarket?",
        "example2_el": "Βρίσκεται σε εξαιρετικό σημείο, μόλις επτά λεπτά με τα πόδια από το μετρό, και ακριβώς απέναντι υπάρχει μεγάλο σούπερ μάρκετ.",
        "example2_en": "It is in an excellent spot, just seven minutes on foot from the metro, and right across the street there is a big supermarket.",
        "keg_communicative_function": "Inquiring about neighborhood amenities and public transport access"
    },
    {
        "id": "SP-U03-021",
        "greek": "Πότε θα μπορούσαμε να συναντηθούμε για να δω το σπίτι από κοντά;",
        "english": "When could we meet so I can see the house in person? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Polite plural conditional 'θα μπορούσαμε να συναντηθούμε', purpose clause 'για να δω από κοντά'"
        },
        "notes": "Examiner Objective: Tests closing the roleplay by negotiating a viewing appointment.\nStrategy: Propose a specific day and afternoon time and ask for the exact street address.",
        "example_el": "Ακούγεται ακριβώς αυτό που ψάχνω! Πότε θα μπορούσαμε να συναντηθούμε, ίσως αύριο το απόγευμα μετά τις πέντε, για να δω το σπίτι από κοντά;",
        "example_en": "It sounds like exactly what I am looking for! When could we meet, perhaps tomorrow afternoon after five, so I can see the house in person?",
        "example2_el": "Αύριο στις έξι το απόγευμα είναι τέλεια. Θα σας περιμένω στην είσοδο της πολυκατοικίας, στην οδό Σπύρου Μερκούρη δώδεκα.",
        "example2_en": "Tomorrow at six in the afternoon is perfect. I will wait for you at the entrance of the apartment building, at 12 Spyrou Merkouri Street.",
        "keg_communicative_function": "Arranging a time and address for an apartment viewing"
    },

    # --- Scenario 4: At the Clothing & Shoe Store (022-028) ---
    {
        "id": "SP-U03-022",
        "greek": "Με συγχωρείτε, μήπως έχετε αυτό το πουκάμισο σε μεσαίο μέγεθος και σε μπλε χρώμα;",
        "english": "Excuse me, do you happen to have this shirt in a medium size and in blue? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Demonstrative 'αυτό το πουκάμισο', prepositional phrases 'σε μεσαίο μέγεθος', 'σε μπλε χρώμα'"
        },
        "notes": "Examiner Objective: Assesses retail shopping inquiries regarding garment size and color.\nStrategy: Use 'με συγχωρείτε' to get the shop assistant's attention and specify both size and color.",
        "example_el": "Με συγχωρείτε, είδα στη βιτρίνα σας αυτό το λινό πουκάμισο και μου άρεσε πολύ. Μήπως το έχετε σε μεσαίο μέγεθος και σε σκούρο μπλε χρώμα;",
        "example_en": "Excuse me, I saw this linen shirt in your shop window and liked it very much. Do you happen to have it in a medium size and in dark blue?",
        "example2_el": "Μισό λεπτό να κοιτάξω στα ράφια μας. Ναι, είστε τυχερός, έχουμε ένα τελευταίο κομμάτι σε μεσαίο μέγεθος ακριβώς στο μπλε που θέλετε.",
        "example2_en": "Just a minute, let me check our shelves. Yes, you are lucky, we have one last piece in medium size right in the blue you want.",
        "keg_communicative_function": "Asking for specific clothing sizes and colors in a retail store"
    },
    {
        "id": "SP-U03-023",
        "greek": "Μπορώ να δοκιμάσω αυτά τα παπούτσια σε νούμερο σαράντα; Πού είναι τα δοκιμαστήρια;",
        "english": "May I try on these shoes in size forty? Where are the fitting rooms? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Aorist subjunctive 'να δοκιμάσω', shoe size 'νούμερο σαράντα', store layout 'τα δοκιμαστήρια'"
        },
        "notes": "Examiner Objective: Distinction between clothing size ('μέγεθος') and shoe size ('νούμερο'), plus verb 'δοκιμάζω'.\nStrategy: Ask to try the item on and inquire where the fitting rooms or mirrors are located.",
        "example_el": "Αυτά τα δερμάτινα παπούτσια φαίνονται πολύ αναπαυτικά. Μπορώ να τα δοκιμάσω σε νούμερο σαράντα, και πού βρίσκονται τα δοκιμαστήρια για το παντελόνι;",
        "example_en": "These leather shoes look very comfortable. May I try them on in size forty, and where are the fitting rooms for the trousers?",
        "example2_el": "Αμέσως να σας φέρω το νούμερο σαράντα! Τα δοκιμαστήρια βρίσκονται στο βάθος του καταστήματος, δίπλα στο ταμείο.",
        "example2_en": "I will bring you size forty right away! The fitting rooms are at the back of the store, next to the cash desk.",
        "keg_communicative_function": "Requesting to try on shoes or clothes and locating fitting rooms"
    },
    {
        "id": "SP-U03-024",
        "greek": "Αυτό το μπουφάν μού πέφτει λίγο στενό στους ώμους· έχετε ένα νούμερο μεγαλύτερο;",
        "english": "This jacket fits me a bit tight in the shoulders; do you have one size larger? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Idiomatic fit expression 'μου πέφτει στενό / φαρδύ', comparative 'ένα νούμερο μεγαλύτερο'"
        },
        "notes": "Examiner Objective: High marks for authentic Greek fit idioms ('μου πέφτει στενό/μεγάλο', 'μου πηγαίνει').\nStrategy: Explain how the garment fits and ask for the next size up or down.",
        "example_el": "Δοκίμασα το μπουφάν αλλά, δυστυχώς, μου πέφτει λίγο στενό στους ώμους και στα μανίκια. Μήπως έχετε το ίδιο σχέδιο σε ένα νούμερο μεγαλύτερο;",
        "example_en": "I tried on the jacket, but unfortunately it fits me a bit tight in the shoulders and sleeves. Do you happen to have the same design in one size larger?",
        "example2_el": "Βεβαίως, ορίστε το μεγάλο μέγεθος. Δοκιμάστε το και είμαι σίγουρη ότι θα σας εφαρμόζει πολύ καλύτερα.",
        "example2_en": "Certainly, here is the large size. Try it on and I am sure that it will fit you much better.",
        "keg_communicative_function": "Describing how clothing fits and asking for a different size"
    },
    {
        "id": "SP-U03-025",
        "greek": "Ποια είναι η τελική τιμή αυτού του φορέματος μετά την έκπτωση;",
        "english": "What is the final price of this dress after the discount? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Genitive singular neuter 'αυτού του φορέματος', retail discount terms ('τελική τιμή', 'έκπτωση')"
        },
        "notes": "Examiner Objective: Tests third-declension neuter genitive ('του φορέματος') and price calculation after sales discount.\nStrategy: Mention the discount percentage sign in the shop and ask for the final price.",
        "example_el": "Βλέπω ότι έχετε εαρινές εκπτώσεις τριάντα τοις εκατό σε όλα τα γυναικεία ρούχα. Ποια είναι η τελική τιμή αυτού του φορέματος μετά την έκπτωση;",
        "example_en": "I see that you have spring discounts of thirty percent on all women's clothes. What is the final price of this dress after the discount?",
        "example2_el": "Από εξήντα ευρώ που ήταν η αρχική του τιμή, με την έκπτωση τριάντα τοις εκατό βγαίνει τώρα στα σαράντα δύο ευρώ.",
        "example2_en": "From sixty euros, which was its original price, with the thirty percent discount it now comes to forty-two euros.",
        "keg_communicative_function": "Inquiring about sale discounts and final retail prices"
    },
    {
        "id": "SP-U03-026",
        "greek": "Μπορώ να πληρώσω με χρεωστική κάρτα ή δέχεστε μόνο μετρητά στο ταμείο;",
        "english": "Can I pay by debit card or do you only accept cash at the register? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Payment vocabulary 'πληρώνω με κάρτα / με μετρητά', verb 'δέχεστε'"
        },
        "notes": "Examiner Objective: Assesses payment transaction vocabulary required in almost all commercial roleplays.\nStrategy: Ask whether card payment is accepted and whether there is any extra discount for cash.",
        "example_el": "Θα το πάρω, μου αρέσει πάρα πολύ! Μπορώ να πληρώσω με την τραπεζική μου κάρτα στο ταμείο ή προτιμάτε να πληρώσω με μετρητά;",
        "example_en": "I will take it, I like it very much! Can I pay with my bank card at the register or do you prefer that I pay in cash?",
        "example2_el": "Δεχόμαστε όλες τις χρεωστικές και πιστωτικές κάρτες, καθώς και πληρωμές με μετρητά, ό,τι σας βολεύει καλύτερα.",
        "example2_en": "We accept all debit and credit cards, as well as cash payments, whatever suits you best.",
        "keg_communicative_function": "Asking about accepted payment methods at a store checkout"
    },
    {
        "id": "SP-U03-027",
        "greek": "Αγόρασα αυτό το πουλόβερ για δώρο· μέχρι πότε γίνεται αλλαγή αν δεν κάνει;",
        "english": "I bought this sweater as a gift; until when can an exchange be made if it doesn't fit? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Gift exchange vocabulary 'κάρτα αλλαγής', idiomatic 'αν δεν του/της κάνει' (if it doesn't fit)"
        },
        "notes": "Examiner Objective: Tests gift-buying follow-up questions ('κάρτα αλλαγής', 'συσκευασία δώρου').\nStrategy: Ask for gift wrapping and an exchange card in case the size doesn't fit your friend.",
        "example_el": "Επειδή παίρνω αυτό το πουλόβερ για δώρο γενεθλίων στον αδελφό μου, μπορείτε να μου βάλετε κάρτα αλλαγής και να μου πείτε μέχρι πότε ισχύει;",
        "example_en": "Because I am getting this sweater as a birthday gift for my brother, can you include an exchange card and tell me until when it is valid?",
        "example2_el": "Βεβαίως, θα σας το τυλίξω σε όμορφη συσκευασία δώρου και με την κάρτα αλλαγής μπορεί να το αλλάξει μέσα σε δεκαπέντε ημέρες.",
        "example2_en": "Certainly, I will wrap it for you in nice gift packaging and with the exchange card he can exchange it within fifteen days.",
        "keg_communicative_function": "Requesting gift wrapping and asking about store exchange policies"
    },
    {
        "id": "SP-U03-028",
        "greek": "Αγόρασα χθες αυτή την μπλούζα αλλά έχει ένα μικρό ελάττωμα στο φερμουάρ· μπορώ να την αλλάξω;",
        "english": "I bought this top yesterday, but it has a small defect on the zipper; can I exchange it? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Aorist 'αγόρασα', neuter noun 'το ελάττωμα', object pronoun 'να την αλλάξω', 'απόδειξη αγοράς'"
        },
        "notes": "Examiner Objective: Evaluates polite consumer return of a defective product.\nStrategy: State when you bought it, describe the specific flaw ('χαλασμένο φερμουάρ' or 'λεκές'), and offer the receipt ('απόδειξη').",
        "example_el": "Καλημέρα σας, αγόρασα χθες από το κατάστημά σας αυτή τη ζακέτα, αλλά όταν γύρισα σπίτι είδα ότι το φερμουάρ είναι χαλασμένο. Έχω την απόδειξη, μπορώ να την αλλάξω;",
        "example_en": "Good morning, yesterday I bought this cardigan from your store, but when I returned home I saw that the zipper is broken. I have the receipt; can I exchange it?",
        "example2_el": "Σας ζητούμε συγγνώμη για την ταλαιπωρία! Φυσικά και μπορείτε να την αλλάξετε αμέσως με μια καινούρια, εφόσον έχετε την απόδειξη αγοράς.",
        "example2_en": "We apologize for the inconvenience! Of course you can exchange it immediately for a new one, since you have the purchase receipt.",
        "keg_communicative_function": "Returning or exchanging a defective garment with a receipt"
    },

    # --- Scenario 5: Organizing a Celebration / Outing with a Colleague or Friend (029-034) ---
    {
        "id": "SP-U03-029",
        "greek": "Τι λες να οργανώσουμε ένα τραπέζι την Παρασκευή το βράδυ για τα γενέθλια της Μαρίας;",
        "english": "What do you say we organize a dinner on Friday night for Maria's birthday? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Collaborative proposal formula 'τι λες να + aorist subjunctive', colloquial 'κάνουμε / οργανώσουμε τραπέζι'"
        },
        "notes": "Examiner Objective: Tests informal peer-to-peer interaction ('Ενικός αριθμός' when roleplaying with a friend/colleague).\nStrategy: Propose a concrete day and time, then invite your partner's opinion.",
        "example_el": "Γεια σου Κώστα! Τι λες να οργανώσουμε ένα ωραίο τραπέζι αυτή την Παρασκευή το βράδυ μετά τη δουλειά για να γιορτάσουμε όλοι μαζί τα γενέθλια της Μαρίας;",
        "example_en": "Hi Kostas! What do you say we organize a nice dinner this Friday night after work so we can celebrate Maria's birthday all together?",
        "example2_el": "Τέλεια ιδέα! Την Παρασκευή όμως τελειώνω αργά το μάθημά μου· μήπως είναι καλύτερα να βγούμε το Σάββατο το βράδυ στις εννέα;",
        "example2_en": "Great idea! On Friday, however, I finish my class late; might it be better to go out on Saturday night at nine?",
        "keg_communicative_function": "Proposing a date and time for a social celebration with a friend"
    },
    {
        "id": "SP-U03-030",
        "greek": "Προτιμάς να κλείσουμε τραπέζι σε μια παραδοσιακή ταβέρνα με μουσική ή σε ιταλικό εστιατόριο;",
        "english": "Do you prefer that we book a table at a traditional taverna with music or at an Italian restaurant? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Preference verb 'προτιμάς να + subjunctive', dining venue comparison"
        },
        "notes": "Examiner Objective: Evaluates comparing two alternatives and reaching a shared decision.\nStrategy: Present both options from the cue card and give a reason why one fits the group better.",
        "example_el": "Πού προτιμάς να κλείσουμε τραπέζι; Να πάμε σε εκείνη την παραδοσιακή ταβέρνα με τη ζωντανή μουσική στο κέντρο ή στο καινούριο ιταλικό εστιατόριο της γειτονιάς;",
        "example_en": "Where do you prefer that we book a table? Should we go to that traditional taverna with live music in the center or to the new Italian restaurant in the neighborhood?",
        "example2_el": "Νομίζω ότι η παραδοσιακή ταβέρνα είναι πολύ καλύτερη επιλογή για μεγάλη παρέα, γιατί έχει ωραία ατμόσφαιρα και ποικιλία από μεζέδες.",
        "example2_en": "I think that the traditional taverna is a much better choice for a large group, because it has a nice atmosphere and a variety of meze dishes.",
        "keg_communicative_function": "Discussing and choosing between dining venues for an outing"
    },
    {
        "id": "SP-U03-031",
        "greek": "Πόσα χρήματα περίπου υπολογίζουμε να δώσουμε το άτομο για το φαγητό και το κρασί;",
        "english": "Roughly how much money do we estimate spending per person for the food and wine? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "First person plural 'υπολογίζουμε να δώσουμε', per-person cost expression 'το άτομο'"
        },
        "notes": "Examiner Objective: Tests budget negotiation in collaborative planning tasks.\nStrategy: Propose a reasonable per-person amount (e.g., 20–25 euros) so everyone in the group can afford it.",
        "example_el": "Για να ξέρουν και οι υπόλοιποι συνάδελφοι, πόσα χρήματα περίπου υπολογίζουμε να δώσουμε το άτομο για το φαγητό, το κρασί και το δώρο της;",
        "example_en": "So that the rest of the colleagues know too, roughly how much money do we estimate spending per person for the food, the wine, and her gift?",
        "example2_el": "Αν βάλουμε από είκοσι πέντε ευρώ ο καθένας, φτάνουν άνετα και για το δείπνο στην ταβέρνα και για ένα πολύ ωραίο δώρο.",
        "example2_en": "If we each put in twenty-five euros, it is comfortably enough both for the dinner at the taverna and for a very nice gift.",
        "keg_communicative_function": "Negotiating and agreeing on a shared budget per person"
    },
    {
        "id": "SP-U03-032",
        "greek": "Τι δώρο λες να της πάρουμε; Ένα ασημένιο κόσμημα, ένα βιβλίο ή ένα άρωμα;",
        "english": "What gift do you say we get her? A silver piece of jewelry, a book, or a perfume? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Indirect object clitic 'να της πάρουμε', gift vocabulary (κόσμημα, βιβλίο, άρωμα)"
        },
        "notes": "Examiner Objective: Assesses genitive/accusative weak pronoun usage ('να της πάρουμε') and justifying a gift choice.\nStrategy: Reject one option politely and explain why another option suits the friend's taste.",
        "example_el": "Τι δώρο λες να της πάρουμε από όλη την παρέα; Σκεφτόμουν ένα ωραίο ασημένιο κολιέ ή μήπως προτιμάς να της αγοράσουμε ένα καλό άρωμα;",
        "example_en": "What gift do you say we get her from the whole group? I was thinking of a nice silver necklace, or do you prefer that we buy her a good perfume?",
        "example2_el": "Το άρωμα είναι λίγο δύσκολο αν δεν ξέρουμε τι φοράει, οπότε ας της πάρουμε καλύτερα το ασημένιο κολιέ που είναι πολύ κομψό.",
        "example2_en": "Perfume is a bit difficult if we don't know what she wears, so let's better get her the silver necklace, which is very elegant.",
        "keg_communicative_function": "Brainstorming and selecting a group birthday gift"
    },
    {
        "id": "SP-U03-033",
        "greek": "Αναλαμβάνω εγώ να παραγγείλω την τούρτα από το ζαχαροπλαστείο· μπορείς εσύ να πάρεις το δώρο;",
        "english": "I will undertake ordering the cake from the pastry shop; can you get the gift? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Task-splitting verb 'αναλαμβάνω να + aorist subjunctive', contrastive pronouns 'εγώ / εσύ'"
        },
        "notes": "Examiner Objective: Tests task delegation and coordination between two speakers.\nStrategy: Volunteer for one specific task and ask your partner to handle the other task.",
        "example_el": "Λοιπόν, αναλαμβάνω εγώ να παραγγείλω μια μεγάλη σοκολατένια τούρτα από το ζαχαροπλαστείο της γειτονιάς μου. Μπορείς εσύ να περάσεις αύριο να αγοράσεις το δώρο;",
        "example_en": "So, I will take care of ordering a big chocolate cake from the pastry shop in my neighborhood. Can you stop by tomorrow to buy the gift?",
        "example2_el": "Έγινε! Θα πάω εγώ αύριο το πρωί στο εμπορικό κέντρο για το δώρο και θα τηλεφωνήσω επίσης στην ταβέρνα για την κράτηση.",
        "example2_en": "Done! I will go tomorrow morning to the shopping center for the gift and I will also call the taverna for the reservation.",
        "keg_communicative_function": "Dividing responsibilities and tasks when organizing an event"
    },
    {
        "id": "SP-U03-034",
        "greek": "Πώς θα πάμε όλοι μαζί το Σάββατο; Έχεις χώρο στο αυτοκίνητό σου να μας πάρεις;",
        "english": "How will we all go together on Saturday? Do you have room in your car to pick us up? (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Future plural 'πώς θα πάμε', idiomatic 'έχεις χώρο να μας πάρεις' (give us a ride)"
        },
        "notes": "Examiner Objective: Tests finalizing transport arrangements at the end of a social planning roleplay.\nStrategy: Ask about carpooling or suggest meeting outside a central metro station.",
        "example_el": "Και κάτι τελευταίο· πώς θα πάμε το Σάββατο το βράδυ στην ταβέρνα; Έχεις χώρο στο αυτοκίνητό σου να περάσεις να μας πάρεις στις οκτώ και μισή;",
        "example_en": "And one last thing: how will we go to the taverna on Saturday night? Do you have room in your car to come pick us up at eight-thirty?",
        "example2_el": "Ναι, αμέ! Θα περάσω με το αυτοκίνητό μου από το σπίτι σου στις οκτώ και μισή για να πάμε όλοι μαζί.",
        "example2_en": "Yes, sure! I will come by your house with my car at eight-thirty so we can all go together.",
        "keg_communicative_function": "Coordinating transportation and meeting times with friends"
    },

    # --- Scenario 6: Lodging a Polite Everyday Complaint (035-040) ---
    {
        "id": "SP-U03-035",
        "greek": "Με συγχωρείτε, παραγγείλαμε πριν από μία ώρα αλλά το φαγητό μας είναι τελείως κρύο.",
        "english": "Excuse me, we ordered an hour ago, but our food is completely cold. (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Polite complaint softener 'με συγχωρείτε', Aorist 'παραγγείλαμε', adverb 'τελείως κρύο'"
        },
        "notes": "Examiner Objective: Tests lodging a firm yet polite complaint in a restaurant without sounding aggressive.\nStrategy: State the problem calmly and ask the waiter to heat it up or bring a fresh plate.",
        "example_el": "Με συγχωρείτε, περιμέναμε σχεδόν μία ώρα να έρθει η παραγγελία μας και δυστυχώς οι μπριζόλες που μας φέρατε είναι τελείως κρύες. Μπορείτε να τις αλλάξετε;",
        "example_en": "Excuse me, we waited almost an hour for our order to arrive and unfortunately the steaks you brought us are completely cold. Can you replace them?",
        "example2_el": "Χίλια συγγνώμη, έχετε απόλυτο δίκιο! Είχαμε πάρα πολύ κόσμο στην κουζίνα, αλλά θα σας φέρω αμέσως καινούριο, ζεστό πιάτο.",
        "example2_en": "A thousand apologies, you are completely right! We were very busy in the kitchen, but I will bring you a new, hot dish immediately.",
        "keg_communicative_function": "Complaining politely about food quality or service delay at a restaurant"
    },
    {
        "id": "SP-U03-036",
        "greek": "Φοβάμαι ότι έγινε κάποιο λάθος στον λογαριασμό· μας έχετε χρεώσει δύο μπουκάλια κρασί.",
        "english": "I am afraid that a mistake was made on the bill; you have charged us for two bottles of wine. (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Diplomatic softener 'φοβάμαι ότι έγινε κάποιο λάθος', Perfect 'μας έχετε χρεώσει'"
        },
        "notes": "Examiner Objective: Rewards diplomatic phrasing ('φοβάμαι ότι έγινε κάποιο λάθος' instead of 'κάνατε λάθος').\nStrategy: Point out the exact item on the receipt and ask for a corrected bill.",
        "example_el": "Με συγχωρείτε, φοβάμαι ότι έγινε κάποιο μικρό λάθος στον λογαριασμό μας. Μας έχετε χρεώσει δύο μπουκάλια λευκό κρασί, ενώ εμείς πήραμε μόνο ένα.",
        "example_en": "Excuse me, I am afraid that a small mistake was made on our bill. You have charged us for two bottles of white wine, whereas we only had one.",
        "example2_el": "Αχ, με συγχωρείτε πάρα πολύ, μπερδεύτηκα με το διπλανό τραπέζι! Το διορθώνω αμέσως και σας φέρνω τον σωστό λογαριασμό.",
        "example2_en": "Oh, excuse me very much, I got mixed up with the next table! I will correct it right away and bring you the proper bill.",
        "keg_communicative_function": "Pointing out a billing error politely at a restaurant or café"
    },
    {
        "id": "SP-U03-037",
        "greek": "Σας τηλεφωνώ γιατί η παραγγελία μου έχει καθυστερήσει πάνω από σαράντα λεπτά.",
        "english": "I am calling you because my delivery order has been delayed by more than forty minutes. (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Present Perfect 'έχει καθυστερήσει', quantitative preposition 'πάνω από σαράντα λεπτά'"
        },
        "notes": "Examiner Objective: Tests telephone complaint handling regarding late food or parcel delivery.\nStrategy: Give your surname and address, explain how long you've waited, and ask when the driver will arrive.",
        "example_el": "Καλησπέρα σας, σας τηλεφωνώ γιατί έκανα μια παραγγελία στο όνομα Παπαδόπουλος πριν από μία ώρα και έχει καθυστερήσει πολύ. Μήπως ξέρετε πότε θα φτάσει;",
        "example_en": "Good evening, I am calling you because I placed an order under the name Papadopoulos an hour ago and it has been delayed a lot. Do you happen to know when it will arrive?",
        "example2_el": "Λυπούμαστε πολύ για την καθυστέρηση! Ο διανομέας μας έφυγε πριν από πέντε λεπτά από το κατάστημα και θα είναι στην πόρτα σας σε λίγο.",
        "example2_en": "We are very sorry for the delay! Our delivery driver left the store five minutes ago and will be at your door shortly.",
        "keg_communicative_function": "Inquiring about a delayed delivery order by telephone"
    },
    {
        "id": "SP-U03-038",
        "greek": "Συγγνώμη που σας ενοχλώ, αλλά η μουσική ακούγεται πολύ δυνατά και αύριο δουλεύω πρωί.",
        "english": "Sorry to bother you, but the music can be heard very loudly and tomorrow I work early. (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Polite apology formula 'συγγνώμη που σας ενοχλώ', passive perception 'ακούγεται πολύ δυνατά'"
        },
        "notes": "Examiner Objective: Assesses neighborly diplomacy during a noise complaint.\nStrategy: Start with 'συγγνώμη που σας ενοχλώ', explain your reason (early work or sleeping children), and ask them to lower the volume ('να χαμηλώσετε λίγο τη μουσική').",
        "example_el": "Καλησπέρα σας, συγγνώμη που σας ενοχλώ τέτοια ώρα, αλλά η μουσική ακούγεται πολύ δυνατά στο διαμέρισμά μου και αύριο πρέπει να ξυπνήσω στις έξι το πρωί.",
        "example_en": "Good evening, sorry to bother you at such an hour, but the music can be heard very loudly in my apartment and tomorrow I have to wake up at six in the morning.",
        "example2_el": "Έχετε δίκιο, δεν καταλάβαμε πόσο πέρασε η ώρα! Θα χαμηλώσουμε αμέσως τη μουσική για να μπορέσετε να κοιμηθείτε ήσυχα.",
        "example2_en": "You are right, we didn't realize how late it had gotten! We will turn the music down immediately so you can sleep peacefully.",
        "keg_communicative_function": "Asking a neighbor politely to reduce noise late at night"
    },
    {
        "id": "SP-U03-039",
        "greek": "Στο δωμάτιό μας δεν δουλεύει το κλιματιστικό και δεν έχουμε ζεστό νερό στο μπάνιο.",
        "english": "In our room the air conditioner is not working and we do not have hot water in the bathroom. (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Malfunction verb 'δεν δουλεύει / δεν λειτουργεί', hotel problem reporting"
        },
        "notes": "Examiner Objective: Tests reporting technical problems at a hotel reception desk.\nStrategy: State your room number clearly, describe the issue, and ask if a technician can come or if you can change rooms.",
        "example_el": "Καλησπέρα σας, μένουμε στο δωμάτιο διακόσια τέσσερα και δυστυχώς δεν δουλεύει καθόλου το κλιματιστικό ούτε υπάρχει ζεστό νερό. Μπορείτε να στείλετε κάποιον τεχνικό;",
        "example_en": "Good evening, we are staying in room 204 and unfortunately the air conditioner is not working at all nor is there hot water. Can you send a technician?",
        "example2_el": "Σας ζητούμε συγγνώμη! Αν ο τεχνικός μας δεν μπορέσει να το φτιάξει μέσα σε μισή ώρα, θα σας μεταφέρουμε αμέσως σε άλλο δωμάτιο.",
        "example2_en": "We apologize to you! If our technician cannot fix it within half an hour, we will move you immediately to another room.",
        "keg_communicative_function": "Reporting room maintenance issues to hotel reception"
    },
    {
        "id": "SP-U03-040",
        "greek": "Σας ευχαριστώ πολύ για την κατανόηση και την άμεση εξυπηρέτηση!",
        "english": "Thank you very much for your understanding and prompt service! (Stage 2 Roleplay Prompt)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay)",
            "focus": "Formulaic closing 'σας ευχαριστώ για + accusative abstract nouns (την κατανόηση, την εξυπηρέτηση)'"
        },
        "notes": "Examiner Objective: Evaluates how smoothly the candidate closes a complaint or transactional roleplay once resolved.\nStrategy: Always end Stage 2 roleplays with a warm expression of thanks and satisfaction.",
        "example_el": "Τέλεια, αυτή η λύση μάς εξυπηρετεί απόλυτα! Σας ευχαριστώ πάρα πολύ για την ευγένεια, την κατανόηση και την τόσο άμεση εξυπηρέτησή σας.",
        "example_en": "Great, this solution suits us completely! Thank you very much for your politeness, understanding, and such prompt service.",
        "example2_el": "Να είστε καλά, είναι χαρά μας να σας εξυπηρετούμε! Σας ευχόμαστε μια υπέροχη συνέχεια στις διακοπές σας.",
        "example2_en": "Be well, it is our pleasure to serve you! We wish you a wonderful continuation of your vacation.",
        "keg_communicative_function": "Expressing gratitude and closing a resolved service interaction politely"
    },
]


# ---------------------------------------------------------------------------
# UNIT SP-04: Stage 3 Visual Description Lego Framework (40 cards)
# ---------------------------------------------------------------------------
CARDS_SP_04 = [
    # --- Step 1: Panoramic Overview & Setting the Scene (001-010) ---
    {
        "id": "SP-U04-001",
        "greek": "Στην εικόνα βλέπουμε μια πολύ όμορφη και καθημερινή σκηνή από τη ζωή στην πόλη.",
        "english": "In the picture we see a very beautiful and everyday scene from life in the city. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Panoramic opener 'στην εικόνα βλέπουμε', feminine accusative agreement 'μια όμορφη καθημερινή σκηνή'"
        },
        "notes": "Examiner Objective: Tests how confidently the candidate initiates the 1–2 minute picture description without hesitation.\nStrategy: Always begin Step 1 with a broad panoramic sentence stating the general theme of the photograph.",
        "example_el": "Στην εικόνα αυτή βλέπουμε μια πολύ όμορφη και ζωντανή καθημερινή σκηνή από τη ζωή σε μια μεγάλη ελληνική πόλη ένα ηλιόλουστο πρωινό.",
        "example_en": "In this picture we see a very beautiful and lively everyday scene from life in a big Greek city on a sunny morning.",
        "example2_el": "Η φωτογραφία μάς παρουσιάζει μια τυπική στιγμή της καθημερινότητας, όπου αρκετοί άνθρωποι βρίσκονται έξω στον δρόμο και κάνουν τις δουλειές τους.",
        "example2_en": "The photograph presents us with a typical moment of everyday life, where several people are out on the street doing their errands.",
        "keg_communicative_function": "Introducing the overall theme and setting of a visual prompt"
    },
    {
        "id": "SP-U04-002",
        "greek": "Η φωτογραφία είναι τραβηγμένη σε εξωτερικό χώρο μια ηλιόλουστη μέρα.",
        "english": "The photograph is taken outdoors on a sunny day. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Passive participle 'είναι τραβηγμένη', spatial classification 'σε εξωτερικό / εσωτερικό χώρο'"
        },
        "notes": "Examiner Objective: Rewards high-value photographic collocations ('είναι τραβηγμένη σε εξωτερικό / εσωτερικό χώρο').\nStrategy: Immediately classify whether the scene is indoors ('σε εσωτερικό χώρο') or outdoors ('σε εξωτερικό χώρο').",
        "example_el": "Η φωτογραφία είναι τραβηγμένη σε εξωτερικό χώρο μια φωτεινή, ηλιόλουστη μέρα, μάλλον την άνοιξη ή το καλοκαίρι, σε ένα μεγάλο πάρκο με πολλά δέντρα.",
        "example_en": "The photograph is taken outdoors on a bright, sunny day, probably in spring or summer, in a large park with many trees.",
        "example2_el": "Αντίθετα, αυτή η φωτογραφία είναι τραβηγμένη σε εσωτερικό χώρο, μέσα σε ένα φωτεινό και μοντέρνο σαλόνι ενός διαμερίσματος.",
        "example2_en": "By contrast, this photograph is taken indoors, inside a bright and modern living room of an apartment.",
        "keg_communicative_function": "Identifying whether a visual scene takes place indoors or outdoors"
    },
    {
        "id": "SP-U04-003",
        "greek": "Η εικόνα παρουσιάζει μια παραδοσιακή λαϊκή αγορά γεμάτη κόσμο και φρέσκα προϊόντα.",
        "english": "The picture shows a traditional open-air market full of people and fresh produce. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Descriptive verb 'παρουσιάζει', adjective 'γεμάτη + accusative (κόσμο, φρέσκα προϊόντα)'"
        },
        "notes": "Examiner Objective: Tests thematic vocabulary for one of KEG's most frequent exam photos: the Greek 'λαϊκή αγορά'.\nStrategy: Mention the stalls ('πάγκοι'), the sellers ('παραγωγοί/πωλητές'), and the shoppers ('καταναλωτές').",
        "example_el": "Η εικόνα παρουσιάζει μια παραδοσιακή λαϊκή αγορά σε μια γειτονιά της Αθήνας, η οποία είναι γεμάτη κόσμο που διαλέγει φρέσκα φρούτα και λαχανικά.",
        "example_en": "The picture shows a traditional open-air market in an Athens neighborhood, which is full of people choosing fresh fruits and vegetables.",
        "example2_el": "Βλέπουμε πολλούς πάγκους με κόκκινες ντομάτες, πορτοκάλια και μήλα, ενώ οι νοικοκυρές κρατούν τσάντες και ψωνίζουν για το σπίτι τους.",
        "example2_en": "We see many stalls with red tomatoes, oranges, and apples, while housewives hold bags and shop for their home.",
        "keg_communicative_function": "Setting the scene of a bustling Greek open-air street market"
    },
    {
        "id": "SP-U04-004",
        "greek": "Βλέπουμε το λιμάνι ενός ελληνικού νησιού το καλοκαίρι την ώρα που φτάνει το πλοίο.",
        "english": "We see the port of a Greek island in the summer at the time the ferry arrives. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Genitive 'ενός ελληνικού νησιού', temporal relative clause 'την ώρα που φτάνει το πλοίο'"
        },
        "notes": "Examiner Objective: Evaluates summer tourism and island port imagery, another classic KEG A2 picture prompt.\nStrategy: Describe the ferry ('το πλοίο της γραμμής'), tourists with suitcases ('βαλίτσες'), and white island houses.",
        "example_el": "Σε αυτή τη φωτογραφία βλέπουμε το γραφικό λιμάνι ενός ελληνικού νησιού το καλοκαίρι, ακριβώς την ώρα που φτάνει το μεγάλο πλοίο και κατεβαίνουν οι τουρίστες.",
        "example_en": "In this photograph we see the picturesque port of a Greek island in the summer, right at the moment the big ferry arrives and the tourists disembark.",
        "example2_el": "Στην προβλήτα του λιμανιού περιμένουν πολλοί ταξιδιώτες με τις βαλίτσες και τα σακίδιά τους κάτω από τον λαμπερό καλοκαιρινό ήλιο.",
        "example2_en": "On the port pier many travelers are waiting with their suitcases and backpacks under the bright summer sun.",
        "keg_communicative_function": "Describing a summer travel scene at a Greek island port"
    },
    {
        "id": "SP-U04-005",
        "greek": "Η φωτογραφία δείχνει μια μεγάλη οικογένεια που τρώει μαζί το μεσημέρι της Κυριακής.",
        "english": "The photograph shows a big family eating together on Sunday at noon. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Relative clause 'που τρώει μαζί', generational nouns (παππούδες, γονείς, εγγόνια)"
        },
        "notes": "Examiner Objective: Tests family gathering and dining vocabulary.\nStrategy: Mention that three generations (grandparents, parents, and children) are gathered around a festive table.",
        "example_el": "Η φωτογραφία δείχνει μια μεγάλη, αγαπημένη οικογένεια που τρώει όλη μαζί στον κήπο του σπιτιού της το μεσημέρι της Κυριακής.",
        "example_en": "The photograph shows a big, loving family eating all together in the garden of their house on Sunday at noon.",
        "example2_el": "Διακρίνουμε τρεις διαφορετικές γενιές, δηλαδή τον παππού και τη γιαγιά, τους γονείς και τα δύο μικρά παιδιά που κάθονται γύρω από το τραπέζι.",
        "example2_en": "We make out three different generations, namely the grandfather and grandmother, the parents, and the two young children sitting around the table.",
        "keg_communicative_function": "Describing a multi-generational family meal or gathering"
    },
    {
        "id": "SP-U04-006",
        "greek": "Βρισκόμαστε στην αίθουσα αναμονής ενός ιατρείου όπου κάθονται διάφοροι ασθενείς.",
        "english": "We are in the waiting room of a medical clinic where various patients are sitting. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "First person plural narrative 'βρισκόμαστε σε...', compound noun 'η αίθουσα αναμονής', locative 'όπου'"
        },
        "notes": "Examiner Objective: Tests healthcare setting description and spatial relative pronoun 'όπου'.\nStrategy: Use 'βρισκόμαστε σε...' to draw the examiner into the scene, then describe who is waiting.",
        "example_el": "Εδώ βρισκόμαστε στην αίθουσα αναμονής ενός ιατρείου ή νοσοκομείου, όπου κάθονται διάφοροι ασθενείς στις καρέκλες και περιμένουν τη σειρά τους για τον γιατρό.",
        "example_en": "Here we are in the waiting room of a clinic or hospital, where various patients are sitting on the chairs waiting their turn for the doctor.",
        "example2_el": "Ο χώρος είναι πολύ καθαρός και φωτεινός, και στους τοίχους υπάρχουν αφίσες με συμβουλές για την υγεία και τη σωστή διατροφή.",
        "example2_en": "The space is very clean and bright, and on the walls there are posters with advice on health and proper nutrition.",
        "keg_communicative_function": "Describing an indoor public service or medical waiting room"
    },
    {
        "id": "SP-U04-007",
        "greek": "Στην εικόνα παρουσιάζεται μια ομάδα εθελοντών που καθαρίζει μια παραλία από τα σκουπίδια.",
        "english": "In the picture a group of volunteers is shown cleaning a beach of rubbish. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Passive 'παρουσιάζεται', genitive plural 'ομάδα εθελοντών', environmental action vocabulary"
        },
        "notes": "Examiner Objective: Ecology and volunteering photos are very common in KEG exams.\nStrategy: Highlight the collective effort ('ομαδική προσπάθεια'), plastic bags ('μεγάλες σακούλες'), and gloves ('γάντια').",
        "example_el": "Στην εικόνα παρουσιάζεται μια ομάδα νέων εθελοντών και μαθητών που καθαρίζει μια μεγάλη αμμώδη παραλία από τα πλαστικά μπουκάλια και τα σκουπίδια.",
        "example_en": "In the picture a group of young volunteers and students is shown cleaning a large sandy beach of plastic bottles and rubbish.",
        "example2_el": "Όλοι φοράνε ειδικά γάντια στα χέρια τους και μαζεύουν με προσοχή τα απορρίμματα μέσα σε μεγάλες μπλε σακούλες ανακύκλωσης.",
        "example2_en": "Everyone is wearing special gloves on their hands and carefully collecting the waste inside large blue recycling bags.",
        "keg_communicative_function": "Describing an environmental cleanup or community volunteering activity"
    },
    {
        "id": "SP-U04-008",
        "greek": "Το κεντρικό θέμα της φωτογραφίας είναι μια παρέα φίλων σε μια καφετέρια του κέντρου.",
        "english": "The central theme of the photograph is a group of friends at a downtown café. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Nominal frame 'το κεντρικό θέμα της φωτογραφίας είναι...', social leisure vocabulary"
        },
        "notes": "Examiner Objective: Tests nominal framing ('το κεντρικό θέμα είναι...') to vary sentence openings.\nStrategy: Mention what they are drinking (iced coffee / φρέντο) and how they are interacting.",
        "example_el": "Το κεντρικό θέμα της φωτογραφίας είναι μια νεανική παρέα τεσσάρων φίλων που πίνουν τον καφέ τους και συζητούν σε μια όμορφη καφετέρια του κέντρου.",
        "example_en": "The central theme of the photograph is a young group of four friends drinking their coffee and chatting at a nice downtown café.",
        "example2_el": "Κάθονται έξω στον πεζόδρομο κάτω από τις μεγάλες λευκές ομπρέλες και απολαμβάνουν τον ελεύθερο χρόνο τους.",
        "example2_en": "They are sitting outside on the pedestrian street under the large white umbrellas and enjoying their free time.",
        "keg_communicative_function": "Identifying the central subject of a social leisure photograph"
    },
    {
        "id": "SP-U04-009",
        "greek": "Βλέπουμε μια σχολική τάξη με μαθητές που παρακολουθούν με προσοχή τη δασκάλα τους.",
        "english": "We see a school classroom with students who are attentively watching their teacher. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Verb 'παρακολουθούν με προσοχή', educational setting vocabulary (σχολική τάξη, θρανία, πίνακας)"
        },
        "notes": "Examiner Objective: Evaluates education and learning vocabulary.\nStrategy: Mention the desks ('θρανία'), open notebooks ('τετράδια'), and the whiteboard ('πίνακας').",
        "example_el": "Σε αυτή την εικόνα βλέπουμε μια φωτεινή σχολική τάξη με μικρούς μαθητές που κάθονται στα θρανία τους και παρακολουθούν με μεγάλη προσοχή τη δασκάλα τους.",
        "example_en": "In this picture we see a bright school classroom with young students sitting at their desks and watching their teacher with great attention.",
        "example2_el": "Η δασκάλα στέκεται όρθια μπροστά στον πίνακα, δείχνει έναν χάρτη της Ελλάδας και εξηγεί το σημερινό μάθημα στα παιδιά.",
        "example2_en": "The teacher is standing in front of the board, pointing to a map of Greece, and explaining today's lesson to the children.",
        "keg_communicative_function": "Describing an educational or classroom scene"
    },
    {
        "id": "SP-U04-010",
        "greek": "Με την πρώτη ματιά καταλαβαίνουμε ότι η σκηνή εκτυλίσσεται σε έναν σταθμό τρένου.",
        "english": "At first glance we understand that the scene unfolds at a train station. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Idiomatic opener 'με την πρώτη ματιά', deponent verb 'εκτυλίσσεται' (takes place/unfolds)"
        },
        "notes": "Examiner Objective: Using 'με την πρώτη ματιά' and 'η σκηνή εκτυλίσσεται' immediately elevates vocabulary marks.\nStrategy: State what visual clues reveal the location (e.g., train tracks, departure board, suitcases).",
        "example_el": "Με την πρώτη ματιά καταλαβαίνουμε ότι η σκηνή εκτυλίσσεται στην αποβάθρα ενός κεντρικού σταθμού τρένου, όπου πολλοί επιβάτες ετοιμάζονται να επιβιβαστούν.",
        "example_en": "At first glance we understand that the scene unfolds on the platform of a central train station, where many passengers are getting ready to board.",
        "example2_el": "Δίπλα στο τρένο βλέπουμε ανθρώπους κάθε ηλικίας που αποχαιρετούν τους συγγενείς τους ή κοιτάζουν τον ηλεκτρονικό πίνακα αναχωρήσεων.",
        "example2_en": "Next to the train we see people of all ages saying goodbye to their relatives or looking at the electronic departure board.",
        "keg_communicative_function": "Summarizing the setting and immediate visual clues of a scene"
    },

    # --- Step 2: Spatial Layout & Positioning (011-020) ---
    {
        "id": "SP-U04-011",
        "greek": "Στο πρώτο πλάνο της εικόνας ξεχωρίζει ένα νεαρό ζευγάρι που περπατάει.",
        "english": "In the foreground of the picture a young couple walking stands out. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Spatial anchor 'στο πρώτο πλάνο', verb 'ξεχωρίζει' (stands out)"
        },
        "notes": "Examiner Objective: Step 2 of the Lego framework requires organized spatial progression (foreground -> center -> background).\nStrategy: Start Step 2 with 'Στο πρώτο πλάνο της εικόνας...' to focus on the closest figures.",
        "example_el": "Στο πρώτο πλάνο της εικόνας ξεχωρίζει ένα νεαρό ζευγάρι που περπατάει χέρι χέρι στον πεζόδρομο και κοιτάζει τις βιτρίνες των εμπορικών καταστημάτων.",
        "example_en": "In the foreground of the picture a young couple stands out walking hand in hand on the pedestrian street and looking at the shop windows.",
        "example2_el": "Μπροστά μπροστά στη φωτογραφία βλέπουμε καθαρά δύο παιδιά που παίζουν με μια μπάλα πάνω στο πράσινο γρασίδι.",
        "example2_en": "Right in the front of the photograph we clearly see two children playing with a ball on the green grass.",
        "keg_communicative_function": "Describing people and objects in the foreground of an image"
    },
    {
        "id": "SP-U04-012",
        "greek": "Στο κέντρο της φωτογραφίας βρίσκονται τρεις άνθρωποι που συζητούν χαμογελαστοί.",
        "english": "In the center of the photograph are three people talking smilingly. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Spatial phrase 'στο κέντρο της φωτογραφίας', plural deponent verb 'βρίσκονται', predicate adjective 'χαμογελαστοί'"
        },
        "notes": "Examiner Objective: Tests accurate subject-verb agreement ('βρίσκονται τρεις άνθρωποι') and central focus description.\nStrategy: Identify how many people are in the center and their main action.",
        "example_el": "Ακριβώς στο κέντρο της φωτογραφίας βρίσκονται τρεις συνάδελφοι, δύο γυναίκες και ένας άντρας, οι οποίοι κάθονται σε ένα γραφείο και συζητούν χαμογελαστοί.",
        "example_en": "Right in the center of the photograph are three colleagues, two women and a man, who are sitting at a desk and talking smilingly.",
        "example2_el": "Στη μέση της σκηνής βλέπουμε ένα μεγάλο ξύλινο τραπέζι γεμάτο με παραδοσιακά ελληνικά φαγητά, σαλάτες και ποτήρια με νερό.",
        "example2_en": "In the middle of the scene we see a large wooden table full of traditional Greek dishes, salads, and glasses of water.",
        "keg_communicative_function": "Directing attention to the central figures or objects in a picture"
    },
    {
        "id": "SP-U04-013",
        "greek": "Στο βάθος της εικόνας διακρίνονται ψηλά κτίρια, πράσινα δέντρα και η γαλάζια θάλασσα.",
        "english": "In the background of the picture tall buildings, green trees, and the blue sea can be made out. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Spatial anchor 'στο βάθος της εικόνας', passive perception verb 'διακρίνονται' (plural)"
        },
        "notes": "Examiner Objective: 'Διακρίνεται / διακρίνονται στο βάθος' is a top-scoring A2/B1 bridge phrase for background details.\nStrategy: Always describe the background ('στο βάθος') to prove you are scanning the entire image.",
        "example_el": "Στο βάθος της εικόνας διακρίνονται μερικά λευκά νησιώτικα σπίτια με μπλε παράθυρα, πράσινα δέντρα και η ήρεμη γαλάζια θάλασσα κάτω από τον ουρανό.",
        "example_en": "In the background of the picture a few white island houses with blue windows, green trees, and the calm blue sea under the sky can be made out.",
        "example2_el": "Πίσω στο βάθος φαίνεται μια μεγάλη οροσειρά με σύννεφα, καθώς και ένας στενός δρόμος που οδηγεί έξω από το χωριό.",
        "example2_en": "Back in the distance a large mountain range with clouds can be seen, as well as a narrow road leading out of the village.",
        "keg_communicative_function": "Describing distant background elements in a photograph"
    },
    {
        "id": "SP-U04-014",
        "greek": "Στα αριστερά της εικόνας στέκεται ένας ηλικιωμένος κύριος που διαβάζει την εφημερίδα του.",
        "english": "On the left of the picture stands an elderly gentleman reading his newspaper. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Left-side spatial marker 'στα αριστερά της εικόνας', posture verb 'στέκεται / κάθεται'"
        },
        "notes": "Examiner Objective: Tests lateral spatial markers ('στα αριστερά', 'στα δεξιά') and posture verbs.\nStrategy: Pair 'στα αριστερά' with 'στα δεξιά' in your next sentence to create a balanced description.",
        "example_el": "Στα αριστερά της εικόνας κάθεται σε ένα ξύλινο παγκάκι ένας ηλικιωμένος κύριος με γυαλιά, ο οποίος διαβάζει ήρεμα την πρωινή του εφημερίδα.",
        "example_en": "On the left of the picture an elderly gentleman with glasses is sitting on a wooden bench, calmly reading his morning newspaper.",
        "example2_el": "Στην αριστερή πλευρά του δρόμου υπάρχει ένα μικρό ανθοπωλείο με πολύχρωμα λουλούδια και γλάστρες πάνω στο πεζοδρόμιο.",
        "example2_en": "On the left side of the street there is a small flower shop with colorful flowers and pots on the sidewalk.",
        "keg_communicative_function": "Locating people and features on the left side of a visual prompt"
    },
    {
        "id": "SP-U04-015",
        "greek": "Στα δεξιά βλέπουμε μια μητέρα που κρατάει από το χέρι την κόρη της.",
        "english": "On the right we see a mother holding her daughter by the hand. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Right-side spatial marker 'στα δεξιά', collocation 'κρατάω από το χέρι'"
        },
        "notes": "Examiner Objective: Evaluates precise physical interaction collocations ('κρατάει από το χέρι', 'έχει στην αγκαλιά της').\nStrategy: Describe both what the person on the right is doing and where they are looking.",
        "example_el": "Στα δεξιά της φωτογραφίας βλέπουμε μια νέα μητέρα που κρατάει σφιχτά από το χέρι τη μικρή της κόρη καθώς περιμένουν να ανάψει το φανάρι.",
        "example_en": "On the right of the photograph we see a young mother holding her little daughter tightly by the hand as they wait for the traffic light to turn green.",
        "example2_el": "Στη δεξιά πλευρά της αίθουσας υπάρχει μια μεγάλη βιβλιοθήκη γεμάτη βιβλία και δίπλα της ένα πράσινο φυτό εσωτερικού χώρου.",
        "example2_en": "On the right side of the room there is a large bookcase full of books and next to it a green indoor plant.",
        "keg_communicative_function": "Locating people and features on the right side of a visual prompt"
    },
    {
        "id": "SP-U04-016",
        "greek": "Ακριβώς πίσω από τους ανθρώπους υπάρχει ένα μεγάλο πέτρινο κτίριο με κήπο.",
        "english": "Right behind the people there is a large stone building with a garden. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Compound preposition 'ακριβώς πίσω από + accusative', material adjective 'πέτρινο / ξύλινο / γυάλινο'"
        },
        "notes": "Examiner Objective: Tests prepositions of relative position ('πίσω από', 'μπροστά από', 'δίπλα σε') with accusative.\nStrategy: Add material or color adjectives ('πέτρινο κτίριο', 'ξύλινη πόρτα') for higher lexical marks.",
        "example_el": "Ακριβώς πίσω από τους ανθρώπους υπάρχει ένα παραδοσιακό διώροφο πέτρινο κτίριο με κεραμίδια στη στέγη και έναν καταπράσινο κήπο με λουλούδια.",
        "example_en": "Right behind the people there is a traditional two-story stone building with roof tiles and a lush green garden with flowers.",
        "example2_el": "Πίσω από τον πάγκο του καταστήματος στέκεται ο υπάλληλος, ο οποίος ετοιμάζει τους καφέδες και εξυπηρετεί με χαμόγελο τους πελάτες.",
        "example2_en": "Behind the counter of the shop stands the employee, who is preparing the coffees and serving the customers with a smile.",
        "keg_communicative_function": "Describing architectural or spatial elements positioned behind the main subjects"
    },
    {
        "id": "SP-U04-017",
        "greek": "Γύρω από το τραπέζι κάθονται τέσσερα άτομα και πάνω στο τραπέζι υπάρχουν πιάτα.",
        "english": "Around the table sit four people and on the table there are plates. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Compound prepositions 'γύρω από το τραπέζι' and 'πάνω στο τραπέζι'"
        },
        "notes": "Examiner Objective: Almost half of KEG A2 photos involve people sitting around a table (home, office, café, taverna).\nStrategy: Describe who is sitting 'γύρω από το τραπέζι' and what objects lie 'πάνω στο τραπέζι'.",
        "example_el": "Γύρω από το στρογγυλό τραπέζι κάθονται τέσσερα άτομα, δύο άντρες και δύο γυναίκες, ενώ πάνω στο τραπέζι υπάρχουν φλιτζάνια καφέ και ένας φορητός υπολογιστής.",
        "example_en": "Around the round table sit four people, two men and two women, while on the table there are coffee cups and a laptop.",
        "example2_el": "Πάνω στο λευκό τραπεζομάντιλο βλέπουμε μια μεγάλη χωριάτικη σαλάτα, φρέσκο ψωμί σε καλάθι και τέσσερα ποτήρια με πορτοκαλάδα.",
        "example2_en": "On the white tablecloth we see a big Greek salad, fresh bread in a basket, and four glasses of orangeade.",
        "keg_communicative_function": "Describing seating arrangements and objects placed on a table"
    },
    {
        "id": "SP-U04-018",
        "greek": "Απέναντι από τη γυναίκα κάθεται ένας νεαρός άντρας και της δείχνει κάτι στο κινητό του.",
        "english": "Across from the woman sits a young man and he is showing her something on his mobile phone. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Spatial preposition 'απέναντι από + accusative', indirect object clitic 'της δείχνει'"
        },
        "notes": "Examiner Objective: Tests 'απέναντι από' (across from/opposite) and interactive body language between figures.\nStrategy: Connect two people in the photo by explaining how they face or interact with each other.",
        "example_el": "Απέναντι από την ξανθιά γυναίκα κάθεται ένας νεαρός άντρας με πουκάμισο, ο οποίος της δείχνει κάτι στην οθόνη του κινητού του τηλεφώνου.",
        "example_en": "Across from the blonde woman sits a young man in a shirt, who is showing her something on the screen of his mobile phone.",
        "example2_el": "Ακριβώς απέναντι από τη στάση του λεωφορείου βλέπουμε έναν φούρνο και ένα φαρμακείο με πράσινη φωτεινή επιγραφή.",
        "example2_en": "Right across from the bus stop we see a bakery and a pharmacy with a green illuminated sign.",
        "keg_communicative_function": "Describing relative positions across from or opposite each other"
    },
    {
        "id": "SP-U04-019",
        "greek": "Ανάμεσα στους δύο γονείς κάθεται το μικρό τους παιδί και κρατάει ένα παιχνίδι.",
        "english": "Between the two parents sits their young child holding a toy. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Preposition 'ανάμεσα σε + accusative plural (ανάμεσα στους δύο γονείς)'"
        },
        "notes": "Examiner Objective: Assesses correct use of 'ανάμεσα σε' + accusative.\nStrategy: Use 'ανάμεσα σε' whenever three people or objects are lined up in a row.",
        "example_el": "Πάνω στον μεγάλο καναπέ του σαλονιού, ανάμεσα στους δύο γονείς, κάθεται το μικρό τους αγόρι και κρατάει στα χέρια του ένα εικονογραφημένο παραμύθι.",
        "example_en": "On the big living room sofa, between the two parents, sits their little boy holding an illustrated storybook in his hands.",
        "example2_el": "Ανάμεσα στα δύο ψηλά κτίρια υπάρχει ένα μικρό, ήσυχο πάρκο με δέντρα, παγκάκια και παιδική χαρά για τα παιδιά.",
        "example2_en": "Between the two tall buildings there is a small, quiet park with trees, benches, and a playground for children.",
        "keg_communicative_function": "Describing someone or something positioned between two other elements"
    },
    {
        "id": "SP-U04-020",
        "greek": "Στην πάνω δεξιά γωνία της εικόνας φαίνεται ο καταγάλανος ουρανός χωρίς καθόλου σύννεφα.",
        "english": "In the upper right corner of the picture the deep blue sky is visible without any clouds at all. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Corner locative 'στην πάνω δεξιά / αριστερή γωνία', intensive adjective 'καταγάλανος'"
        },
        "notes": "Examiner Objective: Shows fine-grained visual observation of the upper/lower corners of the frame.\nStrategy: Use 'στην πάνω γωνία' to transition smoothly from spatial layout to weather and lighting.",
        "example_el": "Στην πάνω δεξιά γωνία της εικόνας φαίνεται ο καταγάλανος ουρανός χωρίς καθόλου σύννεφα, κάτι που δείχνει ότι η μέρα είναι ζεστή και καλοκαιρινή.",
        "example_en": "In the upper right corner of the picture the deep blue sky is visible without any clouds at all, which shows that the day is warm and summery.",
        "example2_el": "Στην κάτω αριστερή γωνία της φωτογραφίας βλέπουμε ένα μικρό καφέ σκυλάκι που κοιμάται ήσυχα δίπλα στα πόδια του ιδιοκτήτη του.",
        "example2_en": "In the lower left corner of the photograph we see a small brown dog sleeping peacefully next to its owner's feet.",
        "keg_communicative_function": "Pointing out details in the corners of a photograph"
    },

    # --- Step 3: Character, Clothing, Action & Emotional Atmosphere (021-030) ---
    {
        "id": "SP-U04-021",
        "greek": "Οι άνθρωποι της εικόνας φοράνε ελαφριά, καλοκαιρινά και άνετα ρούχα.",
        "english": "The people in the picture are wearing light, summer, and comfortable clothes. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Contracted verb 'φοράω -> φοράνε', neuter plural adjective agreement ('ελαφριά, καλοκαιρινά, άνετα ρούχα')"
        },
        "notes": "Examiner Objective: Step 3 requires describing clothing ('τι φοράνε') with accurate neuter plural adjective endings (-α, -ά).\nStrategy: Always connect clothing to the season (light shirts/T-shirts in summer vs. coats/scarves in winter).",
        "example_el": "Όλοι οι άνθρωποι της εικόνας φοράνε ελαφριά, καλοκαιρινά και άνετα ρούχα, δηλαδή κοντομάνικα μπλουζάκια, ανοιχτόχρωμα πουκάμισα, καπέλα και γυαλιά ηλίου.",
        "example_en": "All the people in the picture are wearing light, summer, and comfortable clothes, namely short-sleeved T-shirts, light-colored shirts, hats, and sunglasses.",
        "example2_el": "Επειδή κάνει αρκετό κρύο, οι περαστικοί φοράνε χοντρά χειμωνιάτικα παλτά, μάλλινα κασκόλ γύρω από τον λαιμό τους και ζεστά μπουφάν.",
        "example2_en": "Because it is quite cold, the passersby are wearing thick winter coats, woolen scarves around their necks, and warm jackets.",
        "keg_communicative_function": "Describing people's clothing and seasonal attire in a picture"
    },
    {
        "id": "SP-U04-022",
        "greek": "Η νεαρή γυναίκα έχει μακριά καστανά μαλλιά, φοράει ένα λευκό φόρεμα και χαμογελάει.",
        "english": "The young woman has long brown hair, is wearing a white dress, and is smiling. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Physical appearance ('μακριά καστανά μαλλιά'), three-verb descriptive chain ('έχει... φοράει... χαμογελάει')"
        },
        "notes": "Examiner Objective: Tests physical portrait description (age, hair, clothing, facial expression).\nStrategy: Pick the clearest person in the photo and describe them using three linked verbs.",
        "example_el": "Η νεαρή γυναίκα στα αριστερά είναι γύρω στα τριάντα, έχει μακριά καστανά μαλλιά, φοράει ένα όμορφο λευκό φόρεμα και χαμογελάει πλατιά.",
        "example_en": "The young woman on the left is around thirty, has long brown hair, is wearing a nice white dress, and is smiling broadly.",
        "example2_el": "Ο κύριος δίπλα της έχει κοντά γκρίζα μαλλιά και γυαλιά, και φοράει ένα σκούρο μπλε κοστούμι με λευκό πουκάμισο.",
        "example2_en": "The gentleman next to her has short gray hair and glasses, and is wearing a dark blue suit with a white shirt.",
        "keg_communicative_function": "Describing an individual's physical appearance, age, and attire"
    },
    {
        "id": "SP-U04-023",
        "greek": "Μια κυρία κρατάει στα χέρια της πολλές τσάντες με ψώνια και κοιτάζει μια βιτρίνα.",
        "english": "A lady is holding many shopping bags in her hands and looking at a shop window. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Action verbs in Present ('κρατάει', 'κοιτάζει'), prepositional complement 'τσάντες με ψώνια'"
        },
        "notes": "Examiner Objective: Tests action description using Present tense (which serves as both simple and continuous in Greek).\nStrategy: Specify what people are holding in their hands ('κρατάει στα χέρια του/της...').",
        "example_el": "Μια καλοντυμένη κυρία κρατάει στα χέρια της πολλές χάρτινες τσάντες με ψώνια και στέκεται μπροστά σε ένα κατάστημα για να κοιτάξει τη βιτρίνα.",
        "example_en": "A well-dressed lady is holding many paper shopping bags in her hands and standing in front of a store to look at the shop window.",
        "example2_el": "Ο πωλητής της λαϊκής αγοράς ζυγίζει τα φρούτα στη ζυγαριά και δίνει τη σακούλα με τα μήλα στην πελάτισσα.",
        "example2_en": "The seller at the open-air market is weighing the fruit on the scale and giving the bag of apples to the female customer.",
        "keg_communicative_function": "Describing ongoing physical actions and gestures in a scene"
    },
    {
        "id": "SP-U04-024",
        "greek": "Τα πρόσωπά τους λάμπουν από χαρά και φαίνονται πολύ ευδιάθετοι και ήρεμοι.",
        "english": "Their faces shine with joy and they look very cheerful and calm. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Emotional idiom 'λάμπουν από χαρά', copular verb 'φαίνονται + plural adjectives (ευδιάθετοι, ήρεμοι)'"
        },
        "notes": "Examiner Objective: Rewards rich emotional adjectives beyond basic 'καλός' ('ευδιάθετος', 'ήρεμος', 'ενθουσιασμένος').\nStrategy: Comment on the facial expressions ('τα πρόσωπά τους') to support your mood description.",
        "example_el": "Όλοι γελάνε μεταξύ τους, τα πρόσωπά τους λάμπουν από χαρά και φαίνονται πραγματικά πολύ ευδιάθετοι, ήρεμοι και ξεκούραστοι.",
        "example_en": "Everyone is laughing with one another, their faces shine with joy, and they look truly very cheerful, calm, and well-rested.",
        "example2_el": "Τα μικρά παιδιά δείχνουν κατενθουσιασμένα με τα δώρα τους και αγκαλιάζουν με πολλή αγάπη τον παππού και τη γιαγιά τους.",
        "example2_en": "The young children look thrilled with their gifts and hug their grandfather and grandmother with lots of love.",
        "keg_communicative_function": "Describing positive emotions, facial expressions, and good mood"
    },
    {
        "id": "SP-U04-025",
        "greek": "Ο άντρας δείχνει λίγο αγχωμένος και κουρασμένος επειδή κοιτάζει συνέχεια το ρολόι του.",
        "english": "The man looks a bit stressed and tired because he keeps looking at his watch. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Linking verb 'δείχνει + passive participles (αγχωμένος, κουρασμένος, προβληματισμένος)', causal 'επειδή'"
        },
        "notes": "Examiner Objective: Tests passive participles in '-μένος' ('αγχωμένος', 'κουρασμένος', 'στενοχωρημένος') for negative/tense moods.\nStrategy: Always justify a mood observation with a visual clue using 'επειδή' or 'γιατί'.",
        "example_el": "Ο άντρας που περιμένει στη στάση δείχνει λίγο αγχωμένος και ανυπόμονος, επειδή κοιτάζει συνέχεια το ρολόι του και το λεωφορείο έχει αργήσει.",
        "example_en": "The man waiting at the bus stop looks a bit stressed and impatient, because he keeps looking at his watch and the bus is late.",
        "example2_el": "Η κοπέλα στο γραφείο φαίνεται αρκετά κουρασμένη και προβληματισμένη, γιατί έχει μπροστά της πάρα πολλά χαρτιά και φακέλους.",
        "example2_en": "The young woman in the office looks quite tired and troubled, because she has very many papers and folders in front of her.",
        "keg_communicative_function": "Describing stress, fatigue, or concern based on visual cues"
    },
    {
        "id": "SP-U04-026",
        "greek": "Οι δύο φίλοι συζητούν ζωηρά και φαίνεται ότι απολαμβάνουν πολύ την παρέα ο ένας του άλλου.",
        "english": "The two friends are chattinganimatedly and it seems that they really enjoy each other's company. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Manner adverb 'ζωηρά', reciprocal pronoun 'ο ένας του άλλου'"
        },
        "notes": "Examiner Objective: High syntactic credit for using the reciprocal structure 'ο ένας τον άλλον / ο ένας του άλλου'.\nStrategy: Use this phrase whenever two or more people are talking or helping each other.",
        "example_el": "Οι δύο φίλοι συζητούν ζωηρά πίνοντας τον καφέ τους και φαίνεται καθαρά ότι απολαμβάνουν πάρα πολύ την παρέα ο ένας του άλλου.",
        "example_en": "The two friends are chatting animatedly while drinking their coffee and it is clearly evident that they enjoy each other's company very much.",
        "example2_el": "Τα μέλη της ομάδας συνεργάζονται αρμονικά, χαμογελούν και βοηθούν με προθυμία ο ένας τον άλλον στη δουλειά.",
        "example2_en": "The members of the team cooperate harmoniously, smile, and eagerly help one another with the work.",
        "keg_communicative_function": "Describing interpersonal rapport and mutual cooperation"
    },
    {
        "id": "SP-U04-027",
        "greek": "Η ατμόσφαιρα στην εικόνα είναι πολύ ζεστή, οικογενειακή και γιορτινή.",
        "english": "The atmosphere in the picture is very warm, family-like, and festive. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Abstract noun 'η ατμόσφαιρα', feminine adjective triad ('ζεστή, οικογενειακή και γιορτινή')"
        },
        "notes": "Examiner Objective: Summarizing the overall emotional vibe ('η ατμόσφαιρα είναι...') is a key rubric target in Stage 3.\nStrategy: Group three complementary adjectives to describe the atmosphere of the scene.",
        "example_el": "Γενικά, η ατμόσφαιρα στην εικόνα είναι εξαιρετικά ζεστή, οικογενειακή και γιορτινή, αφού όλοι τρώνε, πίνουν και γιορτάζουν όλοι μαζί.",
        "example_en": "Generally, the atmosphere in the picture is extremely warm, family-like, and festive, since everyone is eating, drinking, and celebrating all together.",
        "example2_el": "Στο δωμάτιο επικρατεί μια πολύ ήρεμη, φιλική και ευχάριστη ατμόσφαιρα που σε κάνει να νιώθεις αμέσως άνετα.",
        "example2_en": "In the room a very calm, friendly, and pleasant atmosphere prevails that makes you feel comfortable immediately.",
        "keg_communicative_function": "Characterizing the overall mood and atmosphere of a scene"
    },
    {
        "id": "SP-U04-028",
        "greek": "Όλοι είναι συγκεντρωμένοι σε αυτό που κάνουν και συνεργάζονται με κέφι.",
        "english": "Everyone is focused on what they are doing and cooperating with enthusiasm. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Participle 'συγκεντρωμένοι σε αυτό που κάνουν', Greek cultural noun 'με κέφι / με όρεξη'"
        },
        "notes": "Examiner Objective: Ideal for workplace, classroom, cooking, or volunteering photos.\nStrategy: Use 'συγκεντρωμένοι' (focused) and 'με κέφι' (with high spirits/enthusiasm) to describe active engagement.",
        "example_el": "Βλέπουμε ότι όλοι οι εθελοντές είναι απόλυτα συγκεντρωμένοι σε αυτό που κάνουν και συνεργάζονται με πολύ κέφι και όρεξη για να τελειώσουν.",
        "example_en": "We see that all the volunteers are completely focused on what they are doing and are cooperating with great enthusiasm and appetite to finish.",
        "example2_el": "Οι μάγειρες στην κουζίνα φαίνονται πολύ προσεκτικοί και ετοιμάζουν τα πιάτα με επαγγελματισμό και καλή διάθεση.",
        "example2_en": "The cooks in the kitchen look very careful and are preparing the dishes with professionalism and a good mood.",
        "keg_communicative_function": "Describing focus, teamwork, and enthusiasm in group activities"
    },
    {
        "id": "SP-U04-029",
        "greek": "Από τα χρώματα και το φως της φωτογραφίας φαίνεται ότι είναι ένα όμορφο ανοιξιάτικο πρωινό.",
        "english": "From the colors and the light of the photograph it seems that it is a beautiful spring morning. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Evidential prepositional phrase 'από τα χρώματα και το φως', seasonal adjectives ('ανοιξιάτικο', 'φθινοπωρινό')"
        },
        "notes": "Examiner Objective: Tests seasonal and time-of-day deduction from lighting and nature cues.\nStrategy: Mention the natural light ('το φυσικό φως'), the green trees, or the blooming flowers.",
        "example_el": "Από τα ζωντανά χρώματα της φύσης και το δυνατό φως της φωτογραφίας φαίνεται ξεκάθαρα ότι είναι ένα όμορφο, ηλιόλουστο ανοιξιάτικο πρωινό.",
        "example_en": "From the vivid colors of nature and the bright light of the photograph it is clearly evident that it is a beautiful, sunny spring morning.",
        "example2_el": "Από τα κίτρινα φύλλα που έχουν πέσει στον δρόμο και τον συννεφιασμένο ουρανό, καταλαβαίνουμε ότι είναι φθινόπωρο.",
        "example2_en": "From the yellow leaves that have fallen on the street and the cloudy sky, we understand that it is autumn.",
        "keg_communicative_function": "Inferring the season and time of day from lighting and environmental details"
    },
    {
        "id": "SP-U04-030",
        "greek": "Παρόλο που έχει αρκετή κίνηση στον δρόμο, οι άνθρωποι δείχνουν ήρεμοι και χαλαροί.",
        "english": "Although there is quite a lot of traffic on the street, the people look calm and relaxed. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Concessive conjunction 'παρόλο που' (although), contrast between setting and mood"
        },
        "notes": "Examiner Objective: Using 'παρόλο που' (although/even though) demonstrates upper-A2 syntactic control.\nStrategy: Contrast a busy or crowded environment with the relaxed demeanor of the people.",
        "example_el": "Παρόλο που έχει αρκετή κίνηση και πολύ κόσμο στην αγορά, οι άνθρωποι της φωτογραφίας δείχνουν ήρεμοι, χαλαροί και καθόλου βιαστικοί.",
        "example_en": "Although there is quite a lot of traffic and many people in the market, the people in the photograph look calm, relaxed, and not at all hurried.",
        "example2_el": "Παρόλο που ο χώρος είναι σχετικά μικρός, όλα είναι τακτοποιημένα και οι εργαζόμενοι δουλεύουν άνετα.",
        "example2_en": "Although the space is relatively small, everything is tidy and the employees work comfortably.",
        "keg_communicative_function": "Expressing contrast between environmental conditions and human mood using concessive clauses"
    },

    # --- Step 4: Hypothesis, Speculation & Concluding Evaluation (031-040) ---
    {
        "id": "SP-U04-031",
        "greek": "Μου φαίνεται ότι είναι Κυριακή μεσημέρι, επειδή όλη η οικογένεια είναι μαζεμένη στο σπίτι.",
        "english": "It seems to me that it is Sunday at noon, because the whole family is gathered at home. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Epistemic frame 'μου φαίνεται ότι...', causal justification 'επειδή', participle 'μαζεμένη'"
        },
        "notes": "Examiner Objective: Step 4 of the Lego framework tests speculation and hypothesis backed by logical reasons.\nStrategy: Never state a hypothesis without adding 'επειδή' or 'γιατί' to explain why you think so.",
        "example_el": "Μου φαίνεται ότι είναι Κυριακή μεσημέρι ή κάποια επίσημη γιορτή, επειδή όλη η οικογένεια είναι μαζεμένη στο σπίτι και κανείς δεν δουλεύει.",
        "example_en": "It seems to me that it is Sunday at noon or some official holiday, because the whole family is gathered at home and nobody is working.",
        "example2_el": "Υποθέτω ότι είναι Σάββατο πρωί, γιατί βλέπουμε γονείς με τα παιδιά τους να κάνουν χαλαρά τα ψώνια τους στην αγορά.",
        "example2_en": "I suppose that it is Saturday morning, because we see parents with their children casually doing their shopping at the market.",
        "keg_communicative_function": "Formulating hypotheses about the day or occasion depicted in an image"
    },
    {
        "id": "SP-U04-032",
        "greek": "Πιθανόν να ετοιμάζονται να ταξιδέψουν σε κάποιο ελληνικό νησί για τις καλοκαιρινές τους διακοπές.",
        "english": "They are probably getting ready to travel to some Greek island for their summer vacation. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Epistemic adverb 'πιθανόν να + subjunctive', purpose phrase 'για τις διακοπές τους'"
        },
        "notes": "Examiner Objective: Tests 'πιθανόν να + ρήμα' or 'ίσως να + ρήμα' for polite speculation about intentions.\nStrategy: Speculate on where the people are going next or what they just finished doing.",
        "example_el": "Επειδή κρατούν μεγάλες βαλίτσες και φοράνε καπέλα ηλίου, πιθανόν να ετοιμάζονται να ταξιδέψουν σε κάποιο ελληνικό νησί για τις καλοκαιρινές τους διακοπές.",
        "example_en": "Because they are holding large suitcases and wearing sun hats, they are probably getting ready to travel to some Greek island for their summer vacation.",
        "example2_el": "Ίσως να επιστρέφουν τώρα στο σπίτι τους μετά από μια κουραστική αλλά όμορφη εκδρομή στη φύση.",
        "example2_en": "Perhaps they are returning home now after a tiring but lovely excursion in nature.",
        "keg_communicative_function": "Speculating about people's plans and intentions using probability markers"
    },
    {
        "id": "SP-U04-033",
        "greek": "Μάλλον γιορτάζουν τα γενέθλια ή την ονομαστική γιορτή κάποιου καλού τους φίλου.",
        "english": "They are probably celebrating the birthday or name day of a good friend of theirs. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Probability adverb 'μάλλον + indicative', Greek cultural concept 'ονομαστική γιορτή'"
        },
        "notes": "Examiner Objective: Mentioning Greek cultural traditions like 'ονομαστική γιορτή' (name day) impresses KEG assessors.\nStrategy: Point to cakes, sweets, gifts, or clinking glasses as evidence for your guess.",
        "example_el": "Βλέποντας την τούρτα και τα κουτιά με τα δώρα πάνω στο τραπέζι, σκέφτομαι ότι μάλλον γιορτάζουν τα γενέθλια ή την ονομαστική γιορτή κάποιου φίλου τους.",
        "example_en": "Seeing the cake and the gift boxes on the table, I think that they are probably celebrating the birthday or name day of a friend of theirs.",
        "example2_el": "Μάλλον πρόκειται για μια ξεχωριστή επέτειο, αφού όλοι φοράνε τα καλά τους ρούχα και τσουγκρίζουν τα ποτήρια τους με κρασί.",
        "example2_en": "It is probably a special anniversary, since everyone is wearing their best clothes and clinking their wine glasses.",
        "keg_communicative_function": "Making culturally grounded inferences about a social celebration"
    },
    {
        "id": "SP-U04-034",
        "greek": "Υποθέτω πως ο καιρός είναι πολύ ζεστός γιατί όλοι κάθονται στη σκιά κάτω από τα δέντρα.",
        "english": "I suppose that the weather is very hot because everyone is sitting in the shade under the trees. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Cognitive verb 'υποθέτω πως / ότι', deduction from behavior ('κάθονται στη σκιά')"
        },
        "notes": "Examiner Objective: Tests linking a hypothesis ('υποθέτω πως...') to behavioral evidence in the image.\nStrategy: Notice if people are seeking shade, drinking cold water/coffee, or holding umbrellas.",
        "example_el": "Υποθέτω πως ο καιρός είναι πάρα πολύ ζεστός, γιατί όλοι οι άνθρωποι κάθονται στη σκιά κάτω από τα δέντρα και πίνουν κρύο νερό και χυμούς.",
        "example_en": "I suppose that the weather is very hot, because all the people are sitting in the shade under the trees and drinking cold water and juices.",
        "example2_el": "Φαντάζομαι πως μόλις σταμάτησε να βρέχει, επειδή ο δρόμος είναι ακόμα βρεγμένος και μερικοί περαστικοί κρατούν ομπρέλες.",
        "example2_en": "I imagine that it just stopped raining, because the street is still wet and some passersby are holding umbrellas.",
        "keg_communicative_function": "Deducing weather conditions from visual clues in a picture"
    },
    {
        "id": "SP-U04-035",
        "greek": "Κατά τη γνώμη μου, οι άνθρωποι αυτοί δεν είναι τουρίστες αλλά κάτοικοι της περιοχής.",
        "english": "In my opinion, these people are not tourists but residents of the area. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Opinion marker 'κατά τη γνώμη μου', correlative contrast 'δεν είναι... αλλά...'"
        },
        "notes": "Examiner Objective: Evaluates contrastive reasoning ('δεν είναι Α, αλλά Β') about who the people are.\nStrategy: Contrast tourists vs. locals, or colleagues vs. family members.",
        "example_el": "Κατά τη γνώμη μου, οι άνθρωποι αυτοί δεν είναι ξένοι τουρίστες αλλά μόνιμοι κάτοικοι της περιοχής, γιατί κρατούν ψώνια από το σούπερ μάρκετ και μιλούν με τον μανάβη.",
        "example_en": "In my opinion, these people are not foreign tourists but permanent residents of the area, because they are holding groceries from the supermarket and talking with the greengrocer.",
        "example2_el": "Νομίζω ότι δεν είναι απλοί συνάδελφοι από τη δουλειά, αλλά πολύ στενοί φίλοι που γνωρίζονται εδώ και πολλά χρόνια.",
        "example2_en": "I think that they are not just colleagues from work, but very close friends who have known each other for many years.",
        "keg_communicative_function": "Inferring the identity and relationship of people in a photograph"
    },
    {
        "id": "SP-U04-036",
        "greek": "Φαντάζομαι ότι σε λίγο θα πληρώσουν τον λογαριασμό και θα συνεχίσουν τη βόλτα τους.",
        "english": "I imagine that shortly they will pay the bill and continue their walk. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Speculative verb 'φαντάζομαι ότι', Future Simple ('θα πληρώσουν', 'θα συνεχίσουν') for next actions"
        },
        "notes": "Examiner Objective: Using Future tense to predict what will happen right after the photo was taken shows great narrative range.\nStrategy: Add one sentence predicting what the people will do 'σε λίγο' (in a little while).",
        "example_el": "Επειδή τα φλιτζάνια τους είναι πλέον άδεια, φαντάζομαι ότι σε λίγο θα πληρώσουν τον λογαριασμό και θα συνεχίσουν τη βόλτα τους στα μαγαζιά.",
        "example_en": "Because their cups are now empty, I imagine that shortly they will pay the bill and continue their walk around the shops.",
        "example2_el": "Πιστεύω ότι μόλις τελειώσουν το καθάρισμα της παραλίας, θα ξεκουραστούν όλοι μαζί και ίσως κάνουν μια βουτιά στη θάλασσα.",
        "example2_en": "I believe that as soon as they finish cleaning the beach, they will rest all together and perhaps take a dip in the sea.",
        "keg_communicative_function": "Predicting what will happen next in a visual narrative using the future tense"
    },
    {
        "id": "SP-U04-037",
        "greek": "Αυτή η εικόνα μού αρέσει πάρα πολύ γιατί μεταδίδει αισιοδοξία και θετική ενέργεια.",
        "english": "I like this picture very much because it conveys optimism and positive energy. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Personal evaluation 'αυτή η εικόνα μού αρέσει', transitive verb 'μεταδίδει + abstract nouns'"
        },
        "notes": "Examiner Objective: Concluding Step 4 with a personal aesthetic/emotional evaluation gives your monologue a polished ending.\nStrategy: Explain what feeling the photo transmits ('μεταδίδει αισιοδοξία / ηρεμία / ζεστασιά').",
        "example_el": "Προσωπικά, αυτή η εικόνα μού αρέσει πάρα πολύ, γιατί είναι γεμάτη ζωή και μεταδίδει στον θεατή αισιοδοξία, χαρά και θετική ενέργεια.",
        "example_en": "Personally, I like this picture very much, because it is full of life and conveys to the viewer optimism, joy, and positive energy.",
        "example2_el": "Η φωτογραφία αυτή μου δημιουργεί πολύ όμορφα συναισθήματα, επειδή δείχνει πόσο σημαντική είναι η ανθρώπινη επικοινωνία και η φιλία.",
        "example2_en": "This photograph creates very warm feelings in me, because it shows how important human communication and friendship are.",
        "keg_communicative_function": "Expressing personal aesthetic evaluation and emotional response to an image"
    },
    {
        "id": "SP-U04-038",
        "greek": "Η σκηνή αυτή μου θυμίζει τις δικές μου καλοκαιρινές διακοπές στην Ελλάδα με την οικογένειά μου.",
        "english": "This scene reminds me of my own summer vacations in Greece with my family. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Evocative verb 'μου θυμίζει + accusative', emphatic possessive 'τις δικές μου διακοπές'"
        },
        "notes": "Examiner Objective: 'Αυτή η εικόνα μού θυμίζει...' is the ideal bridge between the Stage 3 picture monologue and personal follow-up questions.\nStrategy: Connect the photo to a personal memory from your own family, city, or travels.",
        "example_el": "Η σκηνή αυτή στο λιμάνι μού θυμίζει έντονα τις δικές μου καλοκαιρινές διακοπές στην Ελλάδα, όταν ταξίδεψα με την οικογένειά μου στη Νάξο.",
        "example_en": "This scene at the port strongly reminds me of my own summer vacations in Greece, when I traveled with my family to Naxos.",
        "example2_el": "Βλέποντας αυτό το οικογενειακό τραπέζι, θυμάμαι τις Κυριακές στο σπίτι της γιαγιάς μου, όπου μαζευόμασταν όλοι οι συγγενείς.",
        "example2_en": "Seeing this family table, I remember Sundays at my grandmother's house, where all of us relatives used to gather.",
        "keg_communicative_function": "Connecting a visual prompt to personal memories and life experiences"
    },
    {
        "id": "SP-U04-039",
        "greek": "Το μήνυμα της εικόνας είναι ότι πρέπει όλοι να προστατεύουμε το φυσικό περιβάλλον.",
        "english": "The message of the picture is that we must all protect the natural environment. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Conceptual frame 'το μήνυμα της εικόνας είναι ότι...', deontic modal 'πρέπει να προστατεύουμε'"
        },
        "notes": "Examiner Objective: Especially effective for social, ecological, health, or community photos.\nStrategy: State the broader lesson or value illustrated by the photograph.",
        "example_el": "Πιστεύω ότι το βασικό μήνυμα αυτής της εικόνας είναι ότι πρέπει όλοι μας να συνεργαζόμαστε και να προστατεύουμε ενεργά το φυσικό μας περιβάλλον.",
        "example_en": "I believe that the main message of this picture is that all of us must cooperate and actively protect our natural environment.",
        "example2_el": "Η φωτογραφία μάς δείχνει πόσο όμορφο είναι να περνάμε ποιοτικό χρόνο με τους αγαπημένους μας ανθρώπους μακριά από το άγχος.",
        "example2_en": "The photograph shows us how nice it is to spend quality time with our loved ones away from stress.",
        "keg_communicative_function": "Summarizing the thematic message or social value of a photograph"
    },
    {
        "id": "SP-U04-040",
        "greek": "Συνοψίζοντας, πρόκειται για μια πολύ ζωντανή εικόνα της ελληνικής καθημερινότητας.",
        "english": "Summarizing, this is a very lively picture of Greek everyday life. (Stage 3 Image Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue)",
            "focus": "Discourse closing participle 'συνοψίζοντας', impersonal structure 'πρόκειται για + accusative'"
        },
        "notes": "Examiner Objective: Signals clearly to the examiners that you have completed your 4-step monologue in a structured way.\nStrategy: Use 'Συνοψίζοντας, πρόκειται για...' as your final sentence so the interlocutor knows to begin the follow-up questions.",
        "example_el": "Συνοψίζοντας, πρόκειται για μια πολύ ζωντανή και ρεαλιστική εικόνα της σύγχρονης ελληνικής καθημερινότητας, η οποία μου αφήνει τις καλύτερες εντυπώσεις.",
        "example_en": "Summarizing, this is a very lively and realistic picture of modern Greek everyday life, which leaves me with the best impressions.",
        "example2_el": "Κλείνοντας την περιγραφή μου, θα έλεγα ότι η φωτογραφία αποτυπώνει με υπέροχο τρόπο τη χαρά της απλής, καθημερινής ζωής.",
        "example2_en": "Closing my description, I would say that the photograph captures in a wonderful way the joy of simple, everyday life.",
        "keg_communicative_function": "Delivering a structured concluding statement to wrap up an image description"
    },
]


def synthesize_item(text: str, filename: str) -> bool:
    """Synthesize a single Greek string via Google Cloud Chirp-3 HD if not already cached."""
    p = AUDIO_DIR / filename
    if p.exists() and p.stat().st_size > 0:
        return False
    for attempt in range(5):
        try:
            audio_bytes = synthesize_greek_chirp(text)
            with open(p, "wb") as f_out:
                f_out.write(audio_bytes)
            return True
        except Exception as exc:
            if "429" in str(exc) and attempt < 4:
                time.sleep(2.5 * (attempt + 1))
                continue
            print(f"  [ERROR] {filename} ('{text[:40]}...'): {exc}")
            return False
    return False


def process_unit(
    unit_id: str,
    lesson_id: str,
    title: str,
    description: str,
    lesson_notes: str,
    cards: list,
    order_code: str,
):
    print(f"\n>>> Processing {unit_id} ({order_code}) - {len(cards)} cards ...")
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    unit_dir = CONTENT_DIR / unit_id
    unit_dir.mkdir(parents=True, exist_ok=True)
    yaml_file = unit_dir / f"{lesson_id}.yaml"

    tasks = []
    for c in cards:
        c["greek"] = nfc(c["greek"])
        c["example_el"] = nfc(c["example_el"])
        c["example2_el"] = nfc(c["example2_el"])
        c["gender_or_pos"] = "speaking-drill"
        c["status"] = "verified"

        fn_greek = generate_audio_filename(c["greek"])
        c["audio"] = fn_greek
        tasks.append((c["greek"], fn_greek))

        fn_ex1 = generate_audio_filename(c["example_el"])
        c["example_audio"] = fn_ex1
        tasks.append((c["example_el"], fn_ex1))

        fn_ex2 = generate_audio_filename(c["example2_el"])
        c["example2_audio"] = fn_ex2
        tasks.append((c["example2_el"], fn_ex2))

    print(
        f"  Synthesizing audio for {len(tasks)} items using ThreadPoolExecutor(max_workers=6)..."
    )
    synthesized_count = 0
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = {
            executor.submit(synthesize_item, text, fn): fn for text, fn in tasks
        }
        for future in as_completed(futures):
            if future.result():
                synthesized_count += 1

    print(f"  [TTS] Synthesized {synthesized_count} new audio files for {unit_id}.")

    lesson_data = {
        "unit_id": unit_id,
        "lesson_id": lesson_id,
        "title": nfc(title),
        "description": description,
        "lesson_status": "not_started",
        "lesson_notes": nfc(lesson_notes),
        "entries": cards,
    }

    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(
            lesson_data,
            f,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False,
        )

    print(f"  [YAML] Saved {yaml_file}")


def main():
    print("==============================================================")
    print("Generating KEG-A2 Speaking Curriculum: Batch 2 (SP-03 & SP-04)")
    print("==============================================================")

    sp03_notes = """Unit SP-03 Core Notes: Κάρτες Ρόλων & Διάδραση (Stage 2 Cue Card Scenarios & Bilateral Roleplays)
• Official KEG A2 Exam Alignment (Stage 2 — Παιχνίδι Ρόλων / Ανταλλαγή Πληροφοριών, ~5 mins):
  - Scenario 1 (001–007): Travel Agency & Ferry Ticket Office (δρομολόγια, κατάστρωμα vs. αριθμημένη θέση, καμπίνα, όχημα, φοιτητικό πάσο, πύλη αναχώρησης).
  - Scenario 2 (008–014): Pharmacy & Medical Clinic (συμπτώματα, δοσολογία, πριν/μετά το φαγητό, συνταγή γιατρού, επείγον ραντεβού).
  - Scenario 3 (015–021): Real Estate Office & Apartment Rental (ενοίκιο, κοινόχρηστα, όροφος, αυτόνομη θέρμανση, μπαλκόνι, απόσταση από μετρό).
  - Scenario 4 (022–028): Clothing & Shoe Store (μέγεθος, νούμερο, δοκιμαστήριο, έκπτωση, κάρτα/μετρητά, κάρτα αλλαγής, ελάττωμα).
  - Scenario 5 (029–034): Organizing a Celebration with a Friend/Colleague (ημέρα/ώρα, ταβέρνα vs. εστιατόριο, κόστος το άτομο, δώρο, τούρτα).
  - Scenario 6 (035–040): Lodging a Polite Everyday Complaint (κρύο φαγητό, λάθος στον λογαριασμό, καθυστέρηση παραγγελίας, φασαρία, βλάβη στο ξενοδοχείο)."""

    process_unit(
        unit_id="unit-sp-03",
        lesson_id="lesson-01",
        title="Προφορικά SP-03: Κάρτες Ρόλων & Διάδραση (Stage 2 Cue Card Scenarios & Bilateral Roleplays)",
        description="40 bilateral roleplay cue-card prompts and transactional exchanges for Stage 2 of the KEG A2 Speaking exam across 6 high-yield scenarios: travel/ferry agency, pharmacy/clinic, real estate office, clothing store, organizing a celebration, and polite complaints.",
        lesson_notes=sp03_notes,
        cards=CARDS_SP_03,
        order_code="KEG-A2-SP-03-A",
    )

    sp04_notes = """Unit SP-04 Core Notes: Περιγραφή Εικόνας & Αφήγηση (Stage 3 Visual Description Lego Framework)
• Official KEG A2 Exam Alignment (Stage 3 — Περιγραφή Εικόνας, ~4-5 mins):
  - Step 1 (001–010): Panoramic Overview & Setting the Scene (Στην εικόνα βλέπουμε..., Η φωτογραφία είναι τραβηγμένη σε εξωτερικό/εσωτερικό χώρο..., λαϊκή αγορά, λιμάνι, οικογενειακό τραπέζι, ιατρείο, καθαρισμός παραλίας, καφετέρια).
  - Step 2 (011–020): Spatial Layout & Positioning (Στο πρώτο πλάνο..., Στο κέντρο..., Στο βάθος διακρίνονται..., Στα αριστερά/δεξιά..., Ακριβώς πίσω από..., Γύρω από το τραπέζι..., Απέναντι από..., Ανάμεσα σε...).
  - Step 3 (021–030): Character, Clothing, Action & Emotional Atmosphere (φοράνε ελαφριά/χειμωνιάτικα ρούχα, κρατάει τσάντες, φαίνονται ευδιάθετοι/αγχωμένοι, η ατμόσφαιρα είναι ζεστή και γιορτινή).
  - Step 4 (031–040): Hypothesis, Speculation & Concluding Evaluation (Μου φαίνεται ότι..., Πιθανόν να..., Μάλλον γιορτάζουν..., Υποθέτω πως..., Αυτή η εικόνα μού θυμίζει..., Συνοψίζοντας, πρόκειται για...)."""

    process_unit(
        unit_id="unit-sp-04",
        lesson_id="lesson-01",
        title="Προφορικά SP-04: Περιγραφή Εικόνας & Αφήγηση (Stage 3 Visual Description Lego Framework)",
        description="40 structured image-description building blocks and full scene monologues following the 4-step Lego formula for Stage 3 of the KEG A2 Speaking exam: panoramic overview, spatial layout, character/action/clothing breakdown, and weather/mood/context hypothesis.",
        lesson_notes=sp04_notes,
        cards=CARDS_SP_04,
        order_code="KEG-A2-SP-04-A",
    )

    print("\n[OK] Speaking Batch 2 (SP-03 & SP-04) finished successfully!")


if __name__ == "__main__":
    main()

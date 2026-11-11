# -*- coding: utf-8 -*-
"""
Generate KEG-A2 Part 2 Batch 2:
- Unit A2P2-03: KEG-A2-P2-03-A (30 cards) - Housing, Neighborhood & Renting
- Unit A2P2-04: KEG-A2-P2-04-A (30 cards) - Food, Cooking & Culinary Culture
Includes dual exam example sentences and multi-threaded Google Cloud Chirp-3 HD TTS.
"""
import sys
import os
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

# -------------------------------------------------------------
# UNIT A2P2-03 CARDS (30 cards)
# Theme: Σπίτι, Γειτονιά & Ενοικίαση Κατοικίας
# -------------------------------------------------------------
CARDS_U03 = [
    {
        "id": "A2P2-U03-001",
        "greek": "το διαμέρισμα",
        "english": "apartment / flat",
        "notes": "Essential noun for reading housing ads (Reading Task 1). Genitive: του διαμερίσματος.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter",
            "genitive_singular": "του διαμερίσματος",
            "nominative_plural": "τα διαμερίσματα"
        },
        "keg_communicative_function": "Identifying and discussing types of accommodation in housing searches",
        "example_el": "Ενοικιάζεται φωτεινό διαμέρισμα 80 τετραγωνικών μέτρων στο κέντρο της πόλης.",
        "example_en": "Bright 80 square meter apartment for rent in the city center.",
        "example2_el": "Το διαμέρισμα βρίσκεται στον τρίτο όροφο και διαθέτει μεγάλο μπαλκόνι.",
        "example2_en": "The apartment is located on the third floor and features a large balcony."
    },
    {
        "id": "A2P2-U03-002",
        "greek": "η πολυκατοικία",
        "english": "apartment building / block of flats",
        "notes": "Compound: πολύς + κατοικία. Feminine noun in -α.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της πολυκατοικίας",
            "plural": "οι πολυκατοικίες"
        },
        "keg_communicative_function": "Describing residential buildings and shared living facilities",
        "example_el": "Η πολυκατοικία μας διαθέτει σύγχρονο ανελκυστήρα και υπόγειο πάρκινγκ.",
        "example_en": "Our apartment building has a modern elevator and underground parking.",
        "example2_el": "Στην είσοδο της πολυκατοικίας υπάρχει πίνακας ανακοινώσεων για τους ενοίκους.",
        "example2_en": "At the entrance of the apartment building there is a notice board for the residents."
    },
    {
        "id": "A2P2-U03-003",
        "greek": "το δυάρι / το τριάρι",
        "english": "two-room / three-room apartment",
        "notes": "Standard Greek real estate classification: δυάρι (1 bedroom + living room), τριάρι (2 bedrooms + living room).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter",
            "plural": "τα δυάρια / τα τριάρια"
        },
        "keg_communicative_function": "Specifying apartment size and room count when looking for housing",
        "example_el": "Ψάχνουμε ένα επιπλωμένο δυάρι με αυτόνομη θέρμανση για δύο φοιτητές.",
        "example_en": "We are looking for a furnished two-room apartment with autonomous heating for two students.",
        "example2_el": "Το τριάρι είναι πιο κατάλληλο για μια τετραμελή οικογένεια.",
        "example2_en": "The three-room apartment is more suitable for a four-member family."
    },
    {
        "id": "A2P2-U03-004",
        "greek": "η γκαρσονιέρα",
        "english": "studio apartment / bed-sit",
        "notes": "Single room open-plan apartment. Highly frequent in student housing ads.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της γκαρσονιέρας",
            "plural": "οι γκαρσονιέρες"
        },
        "keg_communicative_function": "Inquiring about compact, affordable accommodation",
        "example_el": "Η γκαρσονιέρα είναι πλήρως εξοπλισμένη με ηλεκτρικές συσκευές.",
        "example_en": "The studio apartment is fully equipped with electrical appliances.",
        "example2_el": "Νοίκιασε μια μικρή γκαρσονιέρα μόλις πέντε λεπτά με τα πόδια από τη σχολή.",
        "example2_en": "He rented a small studio apartment just a five-minute walk from college."
    },
    {
        "id": "A2P2-U03-005",
        "greek": "ενοικιάζεται",
        "english": "for rent / to let",
        "notes": "Present mediopassive 3rd person singular of ενοικιάζω. Universal sign in Greece.",
        "gender_or_pos": "verb (mediopassive)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "voice": "mediopassive",
            "tense": "present",
            "active_equivalent": "ενοικιάζω / νοικιάζω"
        },
        "keg_communicative_function": "Interpreting real estate advertisements and public rental signs",
        "example_el": "Ενοικιάζεται διαμέρισμα πρώτου ορόφου, πρόσφατα ανακαινισμένο.",
        "example_en": "First-floor apartment for rent, recently renovated.",
        "example2_el": "Είδαμε πολλές πινακίδες που έγραφαν «Ενοικιάζεται» στους γύρω δρόμους.",
        "example2_en": "We saw many signs saying 'For Rent' in the surrounding streets."
    },
    {
        "id": "A2P2-U03-006",
        "greek": "το ενοίκιο",
        "english": "the rent",
        "notes": "Monthly rental fee. Genitive: του ενοικίου. Plural: τα ενοίκια.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter",
            "genitive": "του ενοικίου",
            "plural": "τα ενοίκια"
        },
        "keg_communicative_function": "Discussing, negotiating, and paying monthly accommodation fees",
        "example_el": "Το μηνιαίο ενοίκιο είναι τετρακόσια ευρώ και πληρώνεται στην αρχή του μήνα.",
        "example_en": "The monthly rent is four hundred euros and is paid at the beginning of the month.",
        "example2_el": "Στην τιμή του ενοικίου περιλαμβάνεται και η σύνδεση στο διαδίκτυο;",
        "example2_en": "Is internet connection included in the rent price?"
    },
    {
        "id": "A2P2-U03-007",
        "greek": "ο ιδιοκτήτης / η ιδιοκτήτρια",
        "english": "landlord / landlady / owner",
        "notes": "Masculine in -ης, feminine in -τρια. From η ιδιοκτησία (property).",
        "gender_or_pos": "noun (masculine / feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "masculine": "ο ιδιοκτήτης (gen: του ιδιοκτήτη)",
            "feminine": "η ιδιοκτήτρια (gen: της ιδιοκτήτριας)"
        },
        "keg_communicative_function": "Addressing and communicating with property owners in oral/written tasks",
        "example_el": "Μίλησα με την ιδιοκτήτρια στο τηλέφωνο και κλείσαμε ραντεβού για να δω το σπίτι.",
        "example_en": "I spoke with the landlady on the phone and we set an appointment to view the house.",
        "example2_el": "Ο ιδιοκτήτης συμφώνησε να αλλάξει τα παλιά κουφώματα στα παράθυρα.",
        "example2_en": "The landlord agreed to replace the old window frames."
    },
    {
        "id": "A2P2-U03-008",
        "greek": "ο ενοικιαστής / η ενοικιάστρια",
        "english": "tenant / renter",
        "notes": "The person renting the property. Plural: οι ενοικιαστές.",
        "gender_or_pos": "noun (masculine / feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "masculine": "ο ενοικιαστής",
            "feminine": "η ενοικιάστρια"
        },
        "keg_communicative_function": "Clarifying roles and contractual obligations between landlord and tenant",
        "example_el": "Ο προηγούμενος ενοικιαστής παρέδωσε το σπίτι σε άριστη κατάσταση.",
        "example_en": "The previous tenant handed over the house in excellent condition.",
        "example2_el": "Οι ενοικιαστές οφείλουν να τηρούν τις ώρες κοινής ησυχίας.",
        "example2_en": "Tenants are required to observe quiet hours."
    },
    {
        "id": "A2P2-U03-009",
        "greek": "η εγγύηση",
        "english": "deposit / guarantee",
        "notes": "Security deposit for rental contract. Usually one or two months' rent.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της εγγύησης",
            "plural": "οι εγγυήσεις"
        },
        "keg_communicative_function": "Discussing rental lease terms and financial deposit conditions",
        "example_el": "Για να υπογράψουμε το συμβόλαιο, ζητείται εγγύηση δύο ενοικίων.",
        "example_en": "To sign the contract, a deposit of two months' rent is requested.",
        "example2_el": "Η εγγύηση επιστρέφεται στον ενοικιαστή κατά την αποχώρησή του.",
        "example2_en": "The deposit is refunded to the tenant upon their departure."
    },
    {
        "id": "A2P2-U03-010",
        "greek": "τα κοινόχρηστα",
        "english": "building maintenance expenses / utilities",
        "notes": "Substantivized neuter plural adjective: κοινός + χρήστος.",
        "gender_or_pos": "noun (neuter plural)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter plural",
            "genitive": "των κοινοχρήστων"
        },
        "keg_communicative_function": "Inquiring about additional monthly building maintenance costs",
        "example_el": "Πόσο περίπου κοστίζουν τα κοινόχρηστα τους χειμερινούς μήνες;",
        "example_en": "About how much do shared utility fees cost during the winter months?",
        "example2_el": "Τα κοινόχρηστα περιλαμβάνουν την καθαριότητα της εισόδου και το ρεύμα της σκάλας.",
        "example2_en": "Shared expenses include entrance cleaning and stairway lighting."
    },
    {
        "id": "A2P2-U03-011",
        "greek": "η θέρμανση",
        "english": "heating",
        "notes": "Third-declension feminine in -ση. Vital in apartment criteria.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της θέρμανσης"
        },
        "keg_communicative_function": "Discussing household climate control and fuel systems",
        "example_el": "Το σπίτι έχει εξαιρετική θέρμανση με φυσικό αέριο και διπλά τζάμια.",
        "example_en": "The house has excellent natural gas heating and double-glazed windows.",
        "example2_el": "Τον χειμώνα ανάβουμε τη θέρμανση για λίγες ώρες το πρωί και το βράδυ.",
        "example2_en": "In winter we turn on the heating for a few hours in the morning and evening."
    },
    {
        "id": "A2P2-U03-012",
        "greek": "η αυτόνομη θέρμανση",
        "english": "autonomous / individual heating",
        "notes": "Contrast with κεντρική θέρμανση (central heating). Individual thermostat control.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η θέρμανση",
            "adjective": "αυτόνομη (self-regulated)"
        },
        "keg_communicative_function": "Inquiring about independent heating control in apartment hunting",
        "example_el": "Προτιμώ διαμέρισμα με αυτόνομη θέρμανση ώστε να ελέγχω τα έξοδά μου.",
        "example_en": "I prefer an apartment with autonomous heating so I can control my expenses.",
        "example2_el": "Η αυτόνομη θέρμανση λειτουργεί με ατομικό λέβητα στο μπαλκόνι.",
        "example2_en": "The autonomous heating operates with an individual boiler on the balcony."
    },
    {
        "id": "A2P2-U03-013",
        "greek": "η κεντρική θέρμανση",
        "english": "central heating",
        "notes": "Shared building boiler system.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η θέρμανση",
            "adjective": "κεντρική"
        },
        "keg_communicative_function": "Describing communal heating schedules in block flats",
        "example_el": "Στην πολυκατοικία μας η κεντρική θέρμανση ανάβει από τις έξι το απόγευμα.",
        "example_en": "In our building, central heating is turned on from six in the evening.",
        "example2_el": "Λόγω του κόστους του πετρελαίου, η κεντρική θέρμανση δεν λειτουργεί όλη μέρα.",
        "example2_en": "Due to heating oil costs, central heating does not run all day."
    },
    {
        "id": "A2P2-U03-014",
        "greek": "ο όροφος",
        "english": "floor / story",
        "notes": "Masculine noun in -ος. Ordinals used: ισόγειο, 1ος, 2ος, 3ος όροφος.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "masculine",
            "genitive": "του ορόφου",
            "plural": "οι όροφοι"
        },
        "keg_communicative_function": "Specifying the storey or floor level of a residence",
        "example_el": "Σε ποιον όροφο βρίσκεται το διαμέρισμα; Στον δεύτερο όροφο.",
        "example_en": "On which floor is the apartment located? On the second floor.",
        "example2_el": "Το ισόγειο έχει κήπο, ενώ ο τελευταίος όροφος έχει υπέροχη θέα.",
        "example2_en": "The ground floor has a garden, while the top floor has a wonderful view."
    },
    {
        "id": "A2P2-U03-015",
        "greek": "το ασανσέρ",
        "english": "elevator / lift",
        "notes": "French loanword, indeclinable neuter. Formal synonym: ο ανελκυστήρας.",
        "gender_or_pos": "noun (neuter indeclinable)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter",
            "declension": "indeclinable",
            "formal_equivalent": "ο ανελκυστήρας"
        },
        "keg_communicative_function": "Inquiring about elevator access in multi-storey buildings",
        "example_el": "Επειδή το διαμέρισμα είναι στον τέταρτο όροφο, το ασανσέρ είναι απαραίτητο.",
        "example_en": "Because the apartment is on the fourth floor, the elevator is essential.",
        "example2_el": "Πάρτε το ασανσέρ και πατήστε το κουμπί για τον τρίτο όροφο.",
        "example2_en": "Take the elevator and press the button for the third floor."
    },
    {
        "id": "A2P2-U03-016",
        "greek": "το μπαλκόνι / η βεράντα",
        "english": "balcony / terrace",
        "notes": "Outdoor spaces typical of Greek homes. Plural: τα μπαλκόνια, οι βεράντες.",
        "gender_or_pos": "noun (neuter / feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "neuter": "το μπαλκόνι",
            "feminine": "η βεράντα"
        },
        "keg_communicative_function": "Describing outdoor leisure amenities of an apartment",
        "example_el": "Μας αρέσει να πίνουμε τον πρωινό μας καφέ στο μπαλκόνι.",
        "example_en": "We like drinking our morning coffee on the balcony.",
        "example2_el": "Η μεγάλη βεράντα έχει τέντα για προστασία από τον ήλιο.",
        "example2_en": "The large terrace has an awning for sun protection."
    },
    {
        "id": "A2P2-U03-017",
        "greek": "η θέα",
        "english": "the view",
        "notes": "Visual panorama. Collocation: με θέα στη θάλασσα / στο βουνό.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της θέας"
        },
        "keg_communicative_function": "Describing panoramic outlooks from living spaces",
        "example_el": "Το ξενοδοχείο έχει δωμάτια με εκπληκτική θέα στην Ακρόπολη.",
        "example_en": "The hotel has rooms with stunning views of the Acropolis.",
        "example2_el": "Από το παράθυρο της κουζίνας έχουμε ανεμπόδιστη θέα στο πάρκο.",
        "example2_en": "From the kitchen window we have an unobstructed view of the park."
    },
    {
        "id": "A2P2-U03-018",
        "greek": "επιπλωμένος, -η, -ο",
        "english": "furnished",
        "notes": "Passive participle of επιπλώνω (to furnish). Opp: ανεπίπλωτος.",
        "gender_or_pos": "adjective / participle",
        "grammatical_info": {
            "part_of_speech": "participle / adjective",
            "masculine": "επιπλωμένος",
            "feminine": "επιπλωμένη",
            "neuter": "επιπλωμένο"
        },
        "keg_communicative_function": "Checking whether furniture is included in a rental property",
        "example_el": "Νοικιάζεται πλήρως επιπλωμένη γκαρσονιέρα με κρεβάτι, γραφείο και ντουλάπα.",
        "example_en": "Fully furnished studio for rent with bed, desk, and wardrobe.",
        "example2_el": "Προτιμάτε επιπλωμένο ή ανεπίπλωτο σπίτι;",
        "example2_en": "Do you prefer a furnished or unfurnished house?"
    },
    {
        "id": "A2P2-U03-019",
        "greek": "ανακαινισμένος, -η, -ο",
        "english": "renovated / refurbished",
        "notes": "Participle of ανακαινίζω. High-frequency keyword in ads.",
        "gender_or_pos": "adjective / participle",
        "grammatical_info": {
            "part_of_speech": "participle / adjective",
            "masculine": "ανακαινισμένος",
            "feminine": "ανακαινισμένη",
            "neuter": "ανακαινισμένο",
            "noun": "η ανακαίνιση"
        },
        "keg_communicative_function": "Describing recent modernizations in property features",
        "example_el": "Το μπάνιο και η κουζίνα είναι πρόσφατα ανακαινισμένα με καινούρια πλακάκια.",
        "example_en": "The bathroom and kitchen are recently renovated with new tiles.",
        "example2_el": "Πρόκειται για ένα πλήρως ανακαινισμένο κτίριο στο ιστορικό κέντρο.",
        "example2_en": "It is a fully renovated building in the historic center."
    },
    {
        "id": "A2P2-U03-020",
        "greek": "φωτεινός, -ή, -ό",
        "english": "bright / luminous",
        "notes": "From το φως (light). Opp: σκοτεινός (dark).",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine": "φωτεινός",
            "feminine": "φωτεινή",
            "neuter": "φωτεινό"
        },
        "keg_communicative_function": "Evaluating natural lighting conditions in living areas",
        "example_el": "Το σαλόνι είναι ιδιαίτερα φωτεινό χάρη στα μεγάλα παράθυρα.",
        "example_en": "The living room is especially bright thanks to the large windows.",
        "example2_el": "Δεν θέλω σκοτεινό διαμέρισμα, ψάχνω έναν χώρο φωτεινό και ευχάριστο.",
        "example2_en": "I don't want a dark apartment, I'm looking for a bright and pleasant space."
    },
    {
        "id": "A2P2-U03-021",
        "greek": "ευρύχωρος, -η, -ο",
        "english": "spacious / roomy",
        "notes": "Compound: ευρύς + χώρος. Opp: στενός (cramped/narrow).",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine": "ευρύχωρος",
            "feminine": "ευρύχωρη",
            "neuter": "ευρύχωρο"
        },
        "keg_communicative_function": "Describing spatial capacity and dimensions of rooms",
        "example_el": "Η κουζίνα είναι ευρύχωρη και χωράει ένα μεγάλο τραπέζι φαγητού.",
        "example_en": "The kitchen is spacious and accommodates a large dining table.",
        "example2_el": "Το υπνοδωμάτιο διαθέτει ευρύχωρη εντοιχισμένη ντουλάπα.",
        "example2_en": "The bedroom features a spacious built-in closet."
    },
    {
        "id": "A2P2-U03-022",
        "greek": "η ήσυχη γειτονιά",
        "english": "quiet neighborhood",
        "notes": "Collocation: ήσυχος (quiet) + η γειτονιά (neighborhood).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η γειτονιά",
            "adjective": "ήσυχη"
        },
        "keg_communicative_function": "Describing district environment and noise levels",
        "example_el": "Το σπίτι βρίσκεται σε μια πολύ ήσυχη γειτονιά κοντά σε άλσος.",
        "example_en": "The house is located in a very quiet neighborhood near a grove.",
        "example2_el": "Είναι ιδανικό μέρος για οικογένειες επειδή η γειτονιά είναι ασφαλής και ήσυχη.",
        "example2_en": "It is an ideal place for families because the neighborhood is safe and quiet."
    },
    {
        "id": "A2P2-U03-023",
        "greek": "κοντά σε μέσα μεταφοράς",
        "english": "close to public transit",
        "notes": "Key selling point in housing listings.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "prepositional phrase",
            "preposition": "κοντά σε",
            "noun_phrase": "μέσα μεταφοράς (means of transport)"
        },
        "keg_communicative_function": "Stating accessibility to public transit lines in housing ads",
        "example_el": "Βρίσκεται κοντά σε μέσα μεταφοράς, μόλις τρία λεπτά από τον σταθμό του μετρό.",
        "example_en": "It is located close to public transit, just three minutes from the metro station.",
        "example2_el": "Ψάχνω κατοικία κοντά σε μέσα μεταφοράς επειδή δεν οδηγώ αυτοκίνητο.",
        "example2_en": "I'm looking for a home near public transit because I don't drive a car."
    },
    {
        "id": "A2P2-U03-024",
        "greek": "η βλάβη",
        "english": "breakdown / damage / defect",
        "notes": "Noun feminine in -η. Used for appliance or plumbing failures.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της βλάβης",
            "plural": "οι βλάβες"
        },
        "keg_communicative_function": "Reporting domestic maintenance malfunctions to a landlord or technician",
        "example_el": "Πρέπει να αναφέρω μια βλάβη στον θερμοσίφωνα που δεν ζεσταίνει το νερό.",
        "example_en": "I need to report a breakdown in the water heater which isn't heating the water.",
        "example2_el": "Η τεχνική υπηρεσία επισκεύασε τη βλάβη στο δίκτυο ηλεκτροδότησης.",
        "example2_en": "The technical service repaired the damage in the electricity grid."
    },
    {
        "id": "A2P2-U03-025",
        "greek": "χάλασε",
        "english": "it broke down / it got spoiled",
        "notes": "Aorist 3rd person singular of χαλάω / χαλάζω. Everyday spoken complaint.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present": "χαλάω / χαλάω (-άς, -άει)",
            "plural": "χάλασαν"
        },
        "keg_communicative_function": "Stating that a machine or fixture has broken down",
        "example_el": "Χάλασε το πλυντήριο ρούχων και γεμίσαμε νερά στο πάτωμα.",
        "example_en": "The washing machine broke down and the floor flooded with water.",
        "example2_el": "Το κλιματιστικό χάλασε ξαφνικά μέσα στον καύσωνα.",
        "example2_en": "The air conditioner broke down suddenly in the middle of the heatwave."
    },
    {
        "id": "A2P2-U03-026",
        "greek": "η διαρροή νερού",
        "english": "water leak",
        "notes": "Collocation: η διαρροή (leak) + νερού (genitive of νερό).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η διαρροή (3rd declension feminine)",
            "genitive_specifier": "νερού / αερίου"
        },
        "keg_communicative_function": "Explaining household emergency situations requiring plumbing intervention",
        "example_el": "Παρατηρήσαμε μια διαρροή νερού κάτω από τον νεροχύτη της κουζίνας.",
        "example_en": "We noticed a water leak under the kitchen sink.",
        "example2_el": "Καλέστε αμέσως την υπηρεσία αν υποψιάζεστε διαρροή φυσικού αερίου.",
        "example2_en": "Call the service immediately if you suspect a gas leak."
    },
    {
        "id": "A2P2-U03-027",
        "greek": "ο υδραυλικός",
        "english": "plumber",
        "notes": "Tradesperson profession. Feminine rarely used (η υδραυλικός).",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "masculine",
            "genitive": "του υδραυλικού",
            "plural": "οι υδραυλικοί"
        },
        "keg_communicative_function": "Summoning tradespeople to resolve household plumbing faults",
        "example_el": "Πρέπει να φωνάξουμε τον υδραυλικό για να αλλάξει τη χαλασμένη βρύση.",
        "example_en": "We must call the plumber to replace the broken faucet.",
        "example2_el": "Ο υδραυλικός θα έρθει αύριο το πρωί στις δέκα για να δει τη διαρροή.",
        "example2_en": "The plumber will come tomorrow morning at ten to look at the leak."
    },
    {
        "id": "A2P2-U03-028",
        "greek": "ο ηλεκτρολόγος",
        "english": "electrician",
        "notes": "Tradesperson profession in -ος. Genitive: του ηλεκτρολόγου.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "masculine",
            "genitive": "του ηλεκτρολόγου",
            "plural": "οι ηλεκτρολόγοι"
        },
        "keg_communicative_function": "Consulting electrical technicians for wiring and repairs",
        "example_el": "Ο ηλεκτρολόγος έλεγξε τον πίνακα και άλλαξε τις παλιές ασφάλειες.",
        "example_en": "The electrician checked the breaker board and changed the old fuses.",
        "example2_el": "Μην αγγίζετε τα καλώδια πριν έρθει ο εξουσιοδοτημένος ηλεκτρολόγος.",
        "example2_en": "Do not touch the wires before the authorized electrician arrives."
    },
    {
        "id": "A2P2-U03-029",
        "greek": "επισκευάζω / φτιάχνω",
        "english": "I repair / I fix",
        "notes": "Synonyms: επισκευάζω (more formal) and φτιάχνω (colloquial everyday).",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verbs": "επισκευάζω (aorist: επισκεύασα) / φτιάχνω (aorist: έφτιαξα)"
        },
        "keg_communicative_function": "Describing repair work and maintenance actions",
        "example_el": "Ο τεχνικός κατάφερε να επισκευάσει το κλιματιστικό μέσα σε μία ώρα.",
        "example_en": "The technician managed to repair the air conditioner within one hour.",
        "example2_el": "Μπορείς σε παρακαλώ να μου φτιάξεις την κλειδαριά της πόρτας;",
        "example2_en": "Can you please fix the door lock for me?"
    },
    {
        "id": "A2P2-U03-030",
        "greek": "μετακομίζω",
        "english": "I move house / relocate",
        "notes": "Regular -ίζω verb. Aorist: μετακόμισα. Noun: η μετακόμιση.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "present": "μετακομίζω",
            "aorist": "μετακόμισα",
            "noun": "η μετακόμιση"
        },
        "keg_communicative_function": "Narrating changes of residence and relocation logistics",
        "example_el": "Τον επόμενο μήνα μετακομίζουμε σε ένα μεγαλύτερο σπίτι στα βόρεια προάστια.",
        "example_en": "Next month we are moving to a bigger house in the northern suburbs.",
        "example2_el": "Η μετακόμιση ήταν κουραστική αλλά είμαστε πολύ χαρούμενοι στη νέα μας γειτονιά.",
        "example2_en": "Moving was tiring, but we are very happy in our new neighborhood."
    }
]

# -------------------------------------------------------------
# UNIT A2P2-04 CARDS (30 cards)
# Theme: Διατροφή, Μαγειρική & Ελληνική Κουζίνα
# -------------------------------------------------------------
CARDS_U04 = [
    {
        "id": "A2P2-U04-001",
        "greek": "η συνταγή",
        "english": "recipe / medical prescription",
        "notes": "Dual meaning: cooking recipe and doctor's prescription. Essential for A2.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της συνταγής",
            "plural": "οι συνταγές"
        },
        "keg_communicative_function": "Following or sharing culinary recipes and procedures",
        "example_el": "Ακολούθησα πιστά τη συνταγή της γιαγιάς για να φτιάξω μουσακά.",
        "example_en": "I followed grandmother's recipe faithfully to make moussaka.",
        "example2_el": "Μπορείς να μου γράψεις τη συνταγή για αυτό το υπέροχο κέικ σοκολάτας;",
        "example2_en": "Can you write down the recipe for this wonderful chocolate cake for me?"
    },
    {
        "id": "A2P2-U04-002",
        "greek": "τα υλικά",
        "english": "ingredients / materials",
        "notes": "Neuter plural: τα υλικά (from το υλικό). Standard recipe heading.",
        "gender_or_pos": "noun (neuter plural)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter plural",
            "genitive": "των υλικών"
        },
        "keg_communicative_function": "Listing culinary ingredients required for dish preparation",
        "example_el": "Πριν ξεκινήσουμε το μαγείρεμα, ας ελέγξουμε αν έχουμε όλα τα απαραίτητα υλικά.",
        "example_en": "Before we start cooking, let's check if we have all the necessary ingredients.",
        "example2_el": "Τα βασικά υλικά για τη χωριάτικη σαλάτα είναι ντομάτες, αγγούρι και φέτα.",
        "example2_en": "The basic ingredients for the Greek salad are tomatoes, cucumber, and feta."
    },
    {
        "id": "A2P2-U04-003",
        "greek": "πλένω τα λαχανικά",
        "english": "I wash the vegetables",
        "notes": "Irregular aorist of πλένω: έπλυνα. Crucial prep action.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "πλένω (aorist: έπλυνα, imperative: πλύνε / πλύντε)",
            "noun": "τα λαχανικά"
        },
        "keg_communicative_function": "Describing pre-cooking cleaning procedures",
        "example_el": "Πρέπει να πλένουμε πολύ καλά τα λαχανικά με άφθονο τρεχούμενο νερό.",
        "example_en": "We must wash the vegetables very well with plenty of running water.",
        "example2_el": "Έπλυνα το μαρούλι και το έκοψα σε λεπτές λωρίδες.",
        "example2_en": "I washed the lettuce and cut it into thin strips."
    },
    {
        "id": "A2P2-U04-004",
        "greek": "καθαρίζω τα φρούτα / τις πατάτες",
        "english": "I peel / clean the fruit / potatoes",
        "notes": "Verb καθαρίζω (aorist: καθάρισα). Covers both peeling and cleaning.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "καθαρίζω (aorist: καθάρισα)"
        },
        "keg_communicative_function": "Instructing how to peel and prepare raw produce",
        "example_el": "Καθάρισε τις πατάτες και κόψε τες σε ίσους κύβους για τη σούπα.",
        "example_en": "Peel the potatoes and cut them into equal cubes for the soup.",
        "example2_el": "Προτιμώ να καθαρίζω τα μήλα πριν τα δώσω στα παιδιά.",
        "example2_en": "I prefer to peel apples before giving them to the children."
    },
    {
        "id": "A2P2-U04-005",
        "greek": "κόβω σε μικρά κομμάτια",
        "english": "I cut into small pieces",
        "notes": "Action instruction: κόβω (aorist: έκοψα) + σε μικρά κομμάτια.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "κόβω (aorist: έκοψα, imperative: κόψε / κόψτε)",
            "prepositional_phrase": "σε μικρά κομμάτια"
        },
        "keg_communicative_function": "Giving precise slicing instructions in recipe execution",
        "example_el": "Κόψτε το κρέας σε μικρά κομμάτια και βάλτε το στο μπολ.",
        "example_en": "Cut the meat into small pieces and put it in the bowl.",
        "example2_el": "Έκοψα το ψωμί σε φέτες για να φτιάξω τοστ.",
        "example2_en": "I cut the bread into slices to make toast."
    },
    {
        "id": "A2P2-U04-006",
        "greek": "τσιγαρίζω το κρεμμύδι",
        "english": "I saute / brown the onion",
        "notes": "Core Greek cooking technique: τσιγαρίζω / σοτάρω.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "τσιγαρίζω (aorist: τσιγάρισα)",
            "noun": "το κρεμμύδι"
        },
        "keg_communicative_function": "Describing pan-frying foundation techniques in Greek cuisine",
        "example_el": "Τσιγαρίζουμε το ψιλοκομμένο κρεμμύδι σε λίγο ελαιόλαδο μέχρι να ροδίσει.",
        "example_en": "We saute the finely chopped onion in a little olive oil until it browns.",
        "example2_el": "Μόλις τσιγαριστεί το κρεμμύδι, προσθέστε τον κιμά στην κατσαρόλα.",
        "example2_en": "As soon as the onion is browned, add the minced meat into the pot."
    },
    {
        "id": "A2P2-U04-007",
        "greek": "βράζω σε μέτρια φωτιά",
        "english": "I boil / simmer on medium heat",
        "notes": "Verb βράζω (aorist: έβρασα). Governs σε μέτρια / χαμηλή / δυνατή φωτιά.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "βράζω (aorist: έβρασα)",
            "noun_phrase": "σε μέτρια φωτιά"
        },
        "keg_communicative_function": "Specifying boiling intensity and temperature controls",
        "example_el": "Αφήνουμε τη σάλτσα να βράσει σε μέτρια φωτιά για είκοσι λεπτά.",
        "example_en": "We let the sauce simmer on medium heat for twenty minutes.",
        "example2_el": "Βράσε τα ζυμαρικά σε άφθονο αλατισμένο νερό για οκτώ λεπτά.",
        "example2_en": "Boil the pasta in plenty of salted water for eight minutes."
    },
    {
        "id": "A2P2-U04-008",
        "greek": "ψήνω στον φούρνο",
        "english": "I bake / roast in the oven",
        "notes": "Verb ψήνω (aorist: έψησα). Used for baking bread, pies, meat.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "ψήνω (aorist: έψησα, passive: ψήνομαι)",
            "noun": "ο φούρνος (oven)"
        },
        "keg_communicative_function": "Specifying oven cooking methods and temperatures",
        "example_el": "Ψήνουμε το κοτόπουλο με πατάτες στον φούρνο στους εκατόν ογδόντα βαθμούς.",
        "example_en": "We roast chicken with potatoes in the oven at one hundred eighty degrees.",
        "example2_el": "Η τυρόπιτα ψήθηκε και μοσχομύρισε όλο το σπίτι.",
        "example2_en": "The cheese pie baked and made the whole house smell fragrant."
    },
    {
        "id": "A2P2-U04-009",
        "greek": "τηγανίζω στο τηγάνι",
        "english": "I fry in the frying pan",
        "notes": "Verb τηγανίζω (aorist: τηγάνισα). Noun: το τηγάνι.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "τηγανίζω (aorist: τηγάνισα)",
            "noun": "το τηγάνι"
        },
        "keg_communicative_function": "Directing pan-frying procedures for fish, potatoes, or eggs",
        "example_el": "Τηγανίζουμε τα καλαμαράκια σε καυτό λάδι μέχρι να γίνουν τραγανά.",
        "example_en": "We fry the calamari in hot oil until they become crispy.",
        "example2_el": "Αποφεύγω να τηγανίζω συχνά επειδή προτιμώ τα ψητά φαγητά.",
        "example2_en": "I avoid frying often because I prefer grilled foods."
    },
    {
        "id": "A2P2-U04-010",
        "greek": "προσθέτω αλάτι και πιπέρι",
        "english": "I add salt and pepper",
        "notes": "Verb προσθέτω (aorist: πρόσθεσα). Basic seasoning collocation.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "προσθέτω (aorist: πρόσθεσα, imperative: πρόσθεσε / προσθέστε)",
            "nouns": "το αλάτι, το πιπέρι"
        },
        "keg_communicative_function": "Instructing seasoning steps during cooking",
        "example_el": "Δοκιμάστε τη σούπα και προσθέστε αλάτι και πιπέρι αν χρειάζεται.",
        "example_en": "Taste the soup and add salt and pepper if needed.",
        "example2_el": "Πρόσθεσα λίγη ρίγανη και φρέσκο πιπέρι στη χωριάτικη σαλάτα.",
        "example2_en": "I added a little oregano and fresh pepper to the Greek salad."
    },
    {
        "id": "A2P2-U04-011",
        "greek": "ανακατεύω καλά",
        "english": "I stir / mix well",
        "notes": "Verb ανακατεύω (aorist: ανακάτεψα). Frequent kitchen imperative.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "ανακατεύω (aorist: ανακάτεψα, imperative: ανακάτεψε / ανακατέψτε)",
            "adverb": "καλά"
        },
        "keg_communicative_function": "Directing stirring and blending of recipe mixtures",
        "example_el": "Ανακατέψτε καλά τα υλικά με μια ξύλινη κουτάλα μέχρι να ομογενοποιηθούν.",
        "example_en": "Stir the ingredients well with a wooden spoon until they homogenize.",
        "example2_el": "Ανακάτεψε το γιαούρτι με το σκόρδο για να φτιάξεις τζατζίκι.",
        "example2_en": "Mix the yogurt with garlic to make tzatziki."
    },
    {
        "id": "A2P2-U04-012",
        "greek": "σερβίρω ζεστό",
        "english": "I serve hot",
        "notes": "Verb σερβίρω (aorist: σέρβιρα). Standard plating instruction.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "σερβίρω (aorist: σέρβιρα, passive: σερβίρομαι)",
            "adjective": "ζεστό (hot) / κρύο (cold)"
        },
        "keg_communicative_function": "Specifying serving temperature and presentation of a meal",
        "example_el": "Το παστίτσιο σερβίρεται ζεστό με συνοδεία πράσινης σαλάτας.",
        "example_en": "Pastitsio is served hot accompanied by a green salad.",
        "example2_el": "Σέρβιρε τη σούπα αμέσως μόλις βγει από τη φωτιά.",
        "example2_en": "Serve the soup immediately once it comes off the heat."
    },
    {
        "id": "A2P2-U04-013",
        "greek": "το ελαιόλαδο",
        "english": "olive oil",
        "notes": "Compound noun: ελιά + λάδι. Quintessential Mediterranean staple.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter",
            "genitive": "του ελαιολάδου",
            "colloquial": "το λάδι"
        },
        "keg_communicative_function": "Discussing key agricultural products and cooking fats",
        "example_el": "Η ελληνική κουζίνα βασίζεται στην εξαιρετική ποιότητα του παρθένου ελαιολάδου.",
        "example_en": "Greek cuisine is based on the exceptional quality of extra virgin olive oil.",
        "example2_el": "Βάλτε δύο κουταλιές ελαιόλαδο στο τηγάνι πριν ρίξετε τα λαχανικά.",
        "example2_en": "Put two spoonfuls of olive oil into the pan before adding the vegetables."
    },
    {
        "id": "A2P2-U04-014",
        "greek": "τα μπαχαρικά",
        "english": "spices",
        "notes": "Neuter plural noun (from το μπαχαρικό).",
        "gender_or_pos": "noun (neuter plural)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter plural",
            "genitive": "των μπαχαρικών"
        },
        "keg_communicative_function": "Discussing seasonings, aromatics, and flavour enhancements",
        "example_el": "Αυτή η συνταγή περιέχει ανατολίτικα μπαχαρικά όπως κύμινο και κανέλα.",
        "example_en": "This recipe contains oriental spices such as cumin and cinnamon.",
        "example2_el": "Αγοράζω φρέσκα μπαχαρικά από την κεντρική αγορά της πόλης.",
        "example2_en": "I buy fresh spices from the central market of the city."
    },
    {
        "id": "A2P2-U04-015",
        "greek": "τα μυρωδικά / τα βότανα",
        "english": "herbs / aromatic greens",
        "notes": "Fresh Greek herbs: ρίγανη, δυόσμος, άνηθος, μαϊντανός, δεντρολίβανο.",
        "gender_or_pos": "noun (neuter plural)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter plural",
            "singular": "το μυρωδικό, το βότανο"
        },
        "keg_communicative_function": "Identifying aromatic herbs in Greek culinary traditions",
        "example_el": "Προσθέτουμε φρέσκα μυρωδικά όπως δυόσμο και μαϊντανό στους κεφτέδες.",
        "example_en": "We add fresh herbs such as spearmint and parsley to the meatballs.",
        "example2_el": "Το τσάι του βουνού είναι ένα παραδοσιακό ελληνικό ρόφημα από βότανα.",
        "example2_en": "Mountain tea is a traditional Greek herbal beverage."
    },
    {
        "id": "A2P2-U04-016",
        "greek": "παραδοσιακός, -ή, -ό",
        "english": "traditional",
        "notes": "Adjective in -ος, -η, -ο. From η παράδοση (tradition).",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine": "παραδοσιακός",
            "feminine": "παραδοσιακή",
            "neuter": "παραδοσιακό"
        },
        "keg_communicative_function": "Characterizing authentic cultural dishes and customs",
        "example_el": "Φάγαμε σε μια παραδοσιακή ταβέρνα δίπλα στο κύμα.",
        "example_en": "We ate at a traditional tavern by the waves.",
        "example2_el": "Η παραδοσιακή ελληνική φιλοξενία εντυπωσιάζει όλους τους τουρίστες.",
        "example2_en": "Traditional Greek hospitality impresses all tourists."
    },
    {
        "id": "A2P2-U04-017",
        "greek": "σπιτικός, -ή, -ό",
        "english": "homemade / home-cooked",
        "notes": "From το σπίτι (home). Synonymous with high quality food.",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine": "σπιτικός",
            "feminine": "σπιτική",
            "neuter": "σπιτικό"
        },
        "keg_communicative_function": "Praising homemade food quality over industrial meals",
        "example_el": "Τίποτα δεν συγκρίνεται με ένα ζεστό σπιτικό φαγητό.",
        "example_en": "Nothing compares to a warm home-cooked meal.",
        "example2_el": "Μας πρόσφεραν σπιτική λεμονάδα και γλυκό του κουταλιού.",
        "example2_en": "They offered us homemade lemonade and spoon sweets."
    },
    {
        "id": "A2P2-U04-018",
        "greek": "νόστιμος, -η, -ο",
        "english": "tasty / delicious",
        "notes": "Opposite: άνοστος (bland). Core culinary compliment.",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine": "νόστιμος",
            "feminine": "νόστιμη",
            "neuter": "νόστιμο",
            "adverb": "νόστιμα"
        },
        "keg_communicative_function": "Expressing appreciation for tasty food at restaurants or gatherings",
        "example_el": "Το ψάρι ήταν εξαιρετικά νόστιμο και ψημένο στην εντέλεια.",
        "example_en": "The fish was exceptionally tasty and cooked to perfection.",
        "example2_el": "Συγχαρητήρια στη μαγείρισσα, όλα τα πιάτα ήταν πεντανόστιμα!",
        "example2_en": "Congratulations to the cook, all dishes were delicious!"
    },
    {
        "id": "A2P2-U04-019",
        "greek": "άνοστος, -η, -ο",
        "english": "bland / tasteless",
        "notes": "Negative prefix αν- + νόστιμος. Feedback in food critique.",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine": "άνοστος",
            "feminine": "άνοστη",
            "neuter": "άνοστο"
        },
        "keg_communicative_function": "Expressing dissatisfaction with unseasoned or bland meals",
        "example_el": "Το φαγητό ήταν αρκετά άνοστο γιατί έλειπε το αλάτι και τα μυρωδικά.",
        "example_en": "The food was quite bland because salt and herbs were lacking.",
        "example2_el": "Αυτές οι ντομάτες του θερμοκηπίου είναι εντελώς άνοστες.",
        "example2_en": "These greenhouse tomatoes are completely tasteless."
    },
    {
        "id": "A2P2-U04-020",
        "greek": "αλμυρός, -ή, -ό",
        "english": "salty / savory / pricey (metaphorical)",
        "notes": "From το αλάτι. Used both for food taste and high prices.",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine": "αλμυρός",
            "feminine": "αλμυρή",
            "neuter": "αλμυρό"
        },
        "keg_communicative_function": "Evaluating salt content in dishes or figurative bill prices",
        "example_el": "Η φέτα είναι λίγο αλμυρή, οπότε μην βάλετε πολύ αλάτι στη σαλάτα.",
        "example_en": "The feta is a bit salty, so don't put too much salt in the salad.",
        "example2_el": "Ο λογαριασμός στο εστιατόριο ήταν αρκετά αλμυρός για όσα παραγγείλαμε.",
        "example2_en": "The restaurant bill was quite steep for what we ordered."
    },
    {
        "id": "A2P2-U04-021",
        "greek": "πικάντικος, -η, -ο",
        "english": "spicy / piquant",
        "notes": "Food seasoning adjective. Loan from Italian piccante.",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine": "πικάντικος",
            "feminine": "πικάντικη",
            "neuter": "πικάντικο"
        },
        "keg_communicative_function": "Indicating spicy flavours and heat levels in food",
        "example_el": "Σας αρέσουν τα πικάντικα φαγητά με καυτερή πιπεριά;",
        "example_en": "Do you like spicy dishes with hot pepper?",
        "example2_el": "Η τυροκαυτερή είναι μια δημοφιλής πικάντικη αλοιφή με φέτα και πιπεριά.",
        "example2_en": "Tirokafteri is a popular spicy dip made with feta and peppers."
    },
    {
        "id": "A2P2-U04-022",
        "greek": "ο/η χορτοφάγος",
        "english": "vegetarian",
        "notes": "Compound: χόρτο + φάγος (eating). Common dietary restriction in restaurants.",
        "gender_or_pos": "noun / adjective",
        "grammatical_info": {
            "part_of_speech": "noun / adjective",
            "masculine": "ο χορτοφάγος",
            "feminine": "η χορτοφάγος",
            "neuter": "το χορτοφαγικό"
        },
        "keg_communicative_function": "Inquiring about vegetarian options on a menu",
        "example_el": "Είμαι χορτοφάγος, ποια πιάτα χωρίς κρέας μου προτείνετε από τον κατάλογο;",
        "example_en": "I am a vegetarian, which meat-free dishes do you recommend from the menu?",
        "example2_el": "Το εστιατόριο προσφέρει πολλές χορτοφαγικές επιλογές με λαδερά και όσπρια.",
        "example2_en": "The restaurant offers many vegetarian options with oil-stewed vegetables and legumes."
    },
    {
        "id": "A2P2-U04-023",
        "greek": "η αλλεργία",
        "english": "allergy",
        "notes": "Medical/dietary term. Plural: οι αλλεργίες.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της αλλεργίας",
            "plural": "οι αλλεργίες"
        },
        "keg_communicative_function": "Notifying food providers of allergies in dining situations",
        "example_el": "Έχετε κάποια τροφική αλλεργία που πρέπει να γνωρίζει ο μάγειρας;",
        "example_en": "Do you have any food allergy that the chef needs to be aware of?",
        "example2_el": "Την άνοιξη υποφέρω από εποχική αλλεργία στη γύρη.",
        "example2_en": "In spring I suffer from seasonal pollen allergy."
    },
    {
        "id": "A2P2-U04-024",
        "greek": "έχω αλλεργία σε...",
        "english": "I have an allergy to... / I am allergic to...",
        "notes": "Crucial safety sentence in dining out dialogues.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "έχω",
            "preposition": "σε + accusative"
        },
        "keg_communicative_function": "Declaring specific food allergens to prevent medical reactions",
        "example_el": "Έχω αλλεργία στους ξηρούς καρπούς, παρακαλώ προσέξτε στο γλυκό.",
        "example_en": "I have an allergy to nuts, please be careful with the dessert.",
        "example2_el": "Ο γιος μου έχει αλλεργία στα θαλασσινά και δεν μπορεί να φάει γαρίδες.",
        "example2_en": "My son is allergic to seafood and cannot eat shrimp."
    },
    {
        "id": "A2P2-U04-025",
        "greek": "η ισορροπημένη διατροφή",
        "english": "balanced diet",
        "notes": "Collocation: ισορροπημένος (balanced) + η διατροφή (diet/nutrition).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η διατροφή",
            "adjective": "ισορροπημένη"
        },
        "keg_communicative_function": "Discussing healthy nutrition, wellness, and lifestyle habits",
        "example_el": "Η μεσογειακή διατροφή θεωρείται πρότυπο ισορροπημένης διατροφής διεθνώς.",
        "example_en": "The Mediterranean diet is internationally considered a model of a balanced diet.",
        "example2_el": "Μια ισορροπημένη διατροφή περιλαμβάνει καθημερινά φρέσκα φρούτα και λαχανικά.",
        "example2_en": "A balanced diet includes fresh fruits and vegetables daily."
    },
    {
        "id": "A2P2-U04-026",
        "greek": "τα γλυκά / το επιδόρπιο",
        "english": "sweets / dessert",
        "notes": "End of meal selections in tavernas.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "neuter_plural": "τα γλυκά",
            "formal_singular": "το επιδόρπιο"
        },
        "keg_communicative_function": "Ordering desserts and post-meal refreshments",
        "example_el": "Θα πάρετε κάποιο επιδόρπιο μετά το κυρίως πιάτο;",
        "example_en": "Will you take any dessert after the main course?",
        "example2_el": "Στο τέλος του γεύματος μας κέρασαν παραδοσιακό γλυκό του κουταλιού και ρακόμελο.",
        "example2_en": "At the end of the meal they treated us to traditional spoon sweets and rakomelo."
    },
    {
        "id": "A2P2-U04-027",
        "greek": "το φιλοδώρημα",
        "english": "tip / gratuity",
        "notes": "Etymology: φίλος + δώρο. Service gratuity in tavernas and cafes.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter",
            "genitive": "του φιλοδωρήματος",
            "plural": "τα φιλοδωρήματα"
        },
        "keg_communicative_function": "Discussing tipping customs in Greek restaurant culture",
        "example_el": "Αφήσαμε ένα γενναιόδωρο φιλοδώρημα στον σερβιτόρο για την άψογη εξυπηρέτηση.",
        "example_en": "We left a generous tip for the waiter for the impeccable service.",
        "example2_el": "Στην Ελλάδα το φιλοδώρημα συνήθως αφήνεται μετρητά πάνω στο τραπέζι.",
        "example2_en": "In Greece, tips are usually left in cash on the table."
    },
    {
        "id": "A2P2-U04-028",
        "greek": "είμαι χορτάτος / χόρτασα",
        "english": "I am full / I have eaten enough",
        "notes": "Adjective: χορτάτος. Verb aorist: χόρτασα (from χορταίνω).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "χορταίνω -> χόρτασα (simple past)",
            "adjective": "χορτάτος / χορτάτη"
        },
        "keg_communicative_function": "Politely declining additional food offers during meals",
        "example_el": "Σας ευχαριστώ πολύ, αλλά χόρτασα, δεν μπορώ να φάω άλλο.",
        "example_en": "Thank you very much, but I am full, I cannot eat any more.",
        "example2_el": "Τα παιδιά έφαγαν με όρεξη και ήταν απολύτως χορτάτα.",
        "example2_en": "The children ate with appetite and were completely full."
    },
    {
        "id": "A2P2-U04-029",
        "greek": "κερνάω",
        "english": "I treat / pay for someone's drink or food",
        "notes": "Greek cultural custom. Aorist: κέρασα. Noun: το κέρασμα.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "present": "κερνάω / κερνώ (-άς, -άει)",
            "aorist": "κέρασα",
            "noun": "το κέρασμα"
        },
        "keg_communicative_function": "Offering to pay for a round of drinks or food as a hospitality gesture",
        "example_el": "Σήμερα είναι η γιορτή μου, οπότε κερνάω εγώ όλη την παρέα!",
        "example_en": "Today is my name day, so I treat the whole group!",
        "example2_el": "Μην βγάζεις πορτοφόλι, θα σε κεράσω εγώ τον καφέ.",
        "example2_en": "Don't take out your wallet, I will treat you to coffee."
    },
    {
        "id": "A2P2-U04-030",
        "greek": "στην υγειά μας!",
        "english": "cheers! / to our health!",
        "notes": "Universal Greek toast before drinking. Short form: «γεια μας!»",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "exclamation / toast",
            "preposition": "σε + την υγειά (health) + κτητικό μας",
            "short_form": "γεια μας!"
        },
        "keg_communicative_function": "Proposing a toast in social gatherings and celebrations",
        "example_el": "Σήκωσαν τα ποτήρια τους και φώναξαν με χαρά: «Στην υγειά μας!»",
        "example_en": "They raised their glasses and cheered with joy: 'To our health!'",
        "example2_el": "Στην υγειά μας και καλή επιτυχία στις εξετάσεις!",
        "example2_en": "To our health and best of success in the examinations!"
    }
]

def synthesize_item(text: str, filename: str) -> bool:
    """Helper to synthesize a single audio string if missing."""
    p = AUDIO_DIR / filename
    if p.exists() and p.stat().st_size > 0:
        return False
    try:
        b = synthesize_greek_chirp(text)
        with open(p, "wb") as f_out:
            f_out.write(b)
        return True
    except Exception as e:
        print(f"  [ERROR] {filename} ('{text}'): {e}")
        return False

def process_unit(unit_id: str, lesson_id: str, title: str, description: str, lesson_notes: str, cards: list, order_code: str):
    print(f"\n>>> Processing {unit_id} ({order_code}) - {len(cards)} cards ...")
    unit_dir = CONTENT_DIR / unit_id
    unit_dir.mkdir(parents=True, exist_ok=True)
    yaml_file = unit_dir / f"{lesson_id}.yaml"
    
    tasks = []
    for c in cards:
        # Greek headword
        fn_greek = generate_audio_filename(c["greek"])
        c["audio"] = fn_greek
        c["status"] = "verified"
        tasks.append((c["greek"], fn_greek))
        
        # Ex 1
        fn_ex1 = generate_audio_filename(c["example_el"])
        c["example_audio"] = fn_ex1
        tasks.append((c["example_el"], fn_ex1))
        
        # Ex 2
        fn_ex2 = generate_audio_filename(c["example2_el"])
        c["example2_audio"] = fn_ex2
        tasks.append((c["example2_el"], fn_ex2))

    print(f"  Synthesizing audio for {len(tasks)} items using ThreadPoolExecutor(max_workers=8)...")
    synthesized_count = 0
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(synthesize_item, text, fn): fn for text, fn in tasks}
        for future in as_completed(futures):
            if future.result():
                synthesized_count += 1

    print(f"  [TTS] Synthesized {synthesized_count} new audio files for {unit_id}.")
    
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
        
    print(f"  [YAML] Saved {yaml_file}")

def update_manifest(new_units: list):
    manifest_path = CONTENT_DIR / "manifest.yaml"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)
        
    units = manifest.get("units", [])
    existing_ids = {u["id"] for u in units}
    
    added = 0
    for entry in new_units:
        if entry["id"] not in existing_ids:
            units.append(entry)
            existing_ids.add(entry["id"])
            added += 1
            print(f"  [Manifest] Appended {entry['id']} ({entry['order']})")
        else:
            print(f"  [Manifest] {entry['id']} already exists, skipping")
            
    manifest["units"] = units
    with open(manifest_path, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"  [Manifest] Manifest updated ({added} new entries). Total: {len(units)} units.")

def main():
    print("==================================================")
    print("Generating KEG-A2 Part 2: Batch 2 (Units 03 & 04)")
    print("==================================================")
    
    u03_notes = """Unit A2P2-03 Core Notes: Σπίτι, Γειτονιά & Ενοικίαση Κατοικίας (Housing, Neighborhood & Renting)
• Official KEG A2 Exam Alignment:
  - Reading Task 1: Real estate classified ads (ενοικιάζεται, δυάρι, κοινόχρηστα, αυτόνομη θέρμανση, εγγύηση).
  - Speaking Stage 2 (Service interaction): Calling a landlord, scheduling apartment viewings, negotiating rental terms.
  - Domestic Repairs: Explaining household malfunctions (βλάβη, χάλασε, διαρροή νερού) to a plumber (υδραυλικός) or electrician (ηλεκτρολόγος)."""

    process_unit(
        unit_id="unit-a2p2-03",
        lesson_id="lesson-01",
        title="Μάθημα 3: Σπίτι, Γειτονιά & Ενοικίαση Κατοικίας (Housing, Neighborhood & Renting an Apartment)",
        description="Navigating classified housing ads, apartment features, lease negotiations, and household repair emergencies for the KEG A2 Reading and Speaking papers.",
        lesson_notes=u03_notes,
        cards=CARDS_U03,
        order_code="KEG-A2-P2-03-A"
    )

    u04_notes = """Unit A2P2-04 Core Notes: Διατροφή, Μαγειρική & Ελληνική Κουζίνα (Food, Cooking & Culinary Culture)
• Official KEG A2 Exam Alignment:
  - Reading Task 2: Following recipe instructions and culinary steps (πλένω, καθαρίζω, τσιγαρίζω, βράζω, ψήνω, προσθέτω, ανακατεύω, σερβίρω).
  - Speaking Stage 2 & 3: Restaurant dining dialogues, ordering special diets (χορτοφάγος, αλλεργία), discussing bills, tipping, and Greek social toasts (στην υγειά μας, κερνάω)."""

    process_unit(
        unit_id="unit-a2p2-04",
        lesson_id="lesson-01",
        title="Μάθημα 4: Διατροφή, Μαγειρική & Ελληνική Κουζίνα (Food, Cooking & Culinary Culture)",
        description="Understanding recipes, cooking steps, Greek culinary terms, restaurant dining, food allergies, and social customs for the KEG A2 Reading and Speaking tasks.",
        lesson_notes=u04_notes,
        cards=CARDS_U04,
        order_code="KEG-A2-P2-04-A"
    )

    manifest_entries = [
        {
            "id": "unit-a2p2-03",
            "title": "Μάθημα 3: Σπίτι, Γειτονιά & Ενοικίαση Κατοικίας (Housing, Neighborhood & Renting an Apartment)",
            "description": "Navigating classified housing ads, apartment features, lease negotiations, and household repair emergencies for the KEG A2 Reading and Speaking papers.",
            "order": "KEG-A2-P2-03-A",
            "total_lessons": 1,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2p2-03/lesson-01.yaml",
                    "title": "Μάθημα 3: Σπίτι, Γειτονιά & Ενοικίαση Κατοικίας (Housing, Neighborhood & Renting an Apartment)"
                }
            ]
        },
        {
            "id": "unit-a2p2-04",
            "title": "Μάθημα 4: Διατροφή, Μαγειρική & Ελληνική Κουζίνα (Food, Cooking & Culinary Culture)",
            "description": "Understanding recipes, cooking steps, Greek culinary terms, restaurant dining, food allergies, and social customs for the KEG A2 Reading and Speaking tasks.",
            "order": "KEG-A2-P2-04-A",
            "total_lessons": 1,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2p2-04/lesson-01.yaml",
                    "title": "Μάθημα 4: Διατροφή, Μαγειρική & Ελληνική Κουζίνα (Food, Cooking & Culinary Culture)"
                }
            ]
        }
    ]

    update_manifest(manifest_entries)
    print("\n[OK] Batch 2 finished successfully!")

if __name__ == "__main__":
    main()

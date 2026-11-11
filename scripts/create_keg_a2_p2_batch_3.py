# -*- coding: utf-8 -*-
"""
Generate KEG-A2 Part 2 Batch 3:
- Unit A2P2-05: KEG-A2-P2-05-A (30 cards) - Shopping, Retail & Consumer Exchanges
- Unit A2P2-06: KEG-A2-P2-06-A (30 cards) - Travel, Transit & Urban Navigation
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
# UNIT A2P2-05 CARDS (30 cards)
# Theme: Αγορές, Καταστήματα & Καταναλωτικές Συνήθειες
# -------------------------------------------------------------
CARDS_U05 = [
    {
        "id": "A2P2-U05-001",
        "greek": "το κατάστημα ρούχων",
        "english": "clothing store",
        "notes": "Collocation: το κατάστημα + genitive plural ρούχων. Standard setting for oral role-play.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "το κατάστημα (neuter)",
            "genitive": "των ρούχων"
        },
        "keg_communicative_function": "Naming retail shop environments in shopping dialogues",
        "example_el": "Μπήκαμε σε ένα κατάστημα ρούχων για να δοκιμάσω ένα χειμωνιάτικο παλτό.",
        "example_en": "We entered a clothing store so I could try on a winter coat.",
        "example2_el": "Το κατάστημα ρούχων προσφέρει μεγάλες εκπτώσεις σε όλα τα καλοκαιρινά είδη.",
        "example2_en": "The clothing store is offering big discounts on all summer items."
    },
    {
        "id": "A2P2-U05-002",
        "greek": "το μέγεθος / το νούμερο",
        "english": "size / shoe or clothing number",
        "notes": "Το μέγεθος (S, M, L) vs. το νούμερο (numeric shoe/dress size, e.g. 38, 42).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter",
            "nouns": "το μέγεθος (gen: του μεγέθους, pl: τα μεγέθη) / το νούμερο (pl: τα νούμερα)"
        },
        "keg_communicative_function": "Specifying clothing or footwear sizes to sales clerks",
        "example_el": "Τι νούμερο παπούτσι φοράτε; Φοράω το σαράντα δύο.",
        "example_en": "What shoe size do you wear? I wear size forty-two.",
        "example2_el": "Αυτό το πουκάμισο είναι σε μέγεθος μεσαίο ή μεγάλο;",
        "example2_en": "Is this shirt in medium or large size?"
    },
    {
        "id": "A2P2-U05-003",
        "greek": "το δοκιμαστήριο",
        "english": "fitting room / dressing room",
        "notes": "From δοκιμάζω (to try on). Genitive: του δοκιμαστηρίου.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter",
            "genitive": "του δοκιμαστηρίου",
            "plural": "τα δοκιμαστήρια"
        },
        "keg_communicative_function": "Asking for the fitting cubicle to try on garments",
        "example_el": "Μπορώ να δοκιμάσω αυτό το παντελόνι; Πού είναι το δοκιμαστήριο;",
        "example_en": "May I try on these trousers? Where is the fitting room?",
        "example2_el": "Όλα τα δοκιμαστήρια είναι κατειλημμένα αυτή τη στιγμή, παρακαλώ περιμένετε.",
        "example2_en": "All fitting rooms are occupied at the moment, please wait."
    },
    {
        "id": "A2P2-U05-004",
        "greek": "μου κάνει / δεν μου κάνει",
        "english": "it fits me / it does not fit me",
        "notes": "Impersonal construction: κάνει + weak indirect clitic (μου, σου, του, της).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "κάνει (3rd person singular present)",
            "clitic": "μου / σου / του / μας / σας"
        },
        "keg_communicative_function": "Stating whether a garment fits one's size properly",
        "example_el": "Αυτό το φόρεμα μου κάνει τέλεια, δεν χρειάζεται καμία αλλαγή.",
        "example_en": "This dress fits me perfectly, it does not need any alteration.",
        "example2_el": "Δυστυχώς το σακάκι δεν μου κάνει στους ώμους, είναι πολύ στενό.",
        "example2_en": "Unfortunately the blazer does not fit me at the shoulders, it is too tight."
    },
    {
        "id": "A2P2-U05-005",
        "greek": "μου πάει / σας πάει πολύ",
        "english": "it suits me / it suits you very well",
        "notes": "Aesthetic compliment: πηγαίνει/πάει + weak clitic. Essential sales formula.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "πάει (3rd singular of πηγαίνω)",
            "adverb": "πολύ / τέλεια"
        },
        "keg_communicative_function": "Paying or receiving compliments on how an outfit looks",
        "example_el": "Αυτό το μπλε χρώμα σας πάει πάρα πολύ με τα μάτια σας!",
        "example_en": "This blue color suits you very much with your eyes!",
        "example2_el": "Πιστεύεις ότι μου πάει αυτό το καπέλο ή φαίνεται περίεργο;",
        "example2_en": "Do you think this hat suits me or does it look strange?"
    },
    {
        "id": "A2P2-U05-006",
        "greek": "είναι στενό / φαρδύ",
        "english": "it is tight / it is loose (baggy)",
        "notes": "Adjectives: στενός (tight/narrow) vs. φαρδύς, -ιά, -ύ (wide/loose).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "adjectives": "στενός, -ή, -ό / φαρδύς, -ιά, -ύ (neuter: φαρδύ)"
        },
        "keg_communicative_function": "Explaining garment fit defects during trying on sessions",
        "example_el": "Το παντελόνι είναι πολύ στενό στη μέση, έχετε ένα νούμερο μεγαλύτερο;",
        "example_en": "The trousers are too tight at the waist, do you have one size larger?",
        "example2_el": "Η μπλούζα μου είναι αρκετά φαρδιά, προτιμώ κάτι πιο εφαρμοστό.",
        "example2_en": "My shirt is quite loose, I prefer something more fitted."
    },
    {
        "id": "A2P2-U05-007",
        "greek": "είναι κοντό / μακρύ",
        "english": "it is short / it is long",
        "notes": "Adjectives of length: κοντός, -ή, -ό vs. μακρύς, -ιά, -ύ (neuter: μακρύ).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "adjectives": "κοντός / μακρύς (neuter: μακρύ)"
        },
        "keg_communicative_function": "Evaluating length parameters of clothing",
        "example_el": "Τα μανίκια είναι πολύ μακριά και χρειάζονται κόντεμα.",
        "example_en": "The sleeves are too long and need shortening.",
        "example2_el": "Αυτή η φούστα είναι πολύ κοντή για επίσημη συνέντευξη εργασίας.",
        "example2_en": "This skirt is too short for a formal job interview."
    },
    {
        "id": "A2P2-U05-008",
        "greek": "η απόδειξη αγοράς",
        "english": "purchase receipt",
        "notes": "Collocation: η απόδειξη + genitive αγοράς. Essential for returns and refunds.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η απόδειξη (3rd declension feminine)",
            "genitive": "αγοράς"
        },
        "keg_communicative_function": "Requesting or retaining commercial receipts for consumer transactions",
        "example_el": "Κρατήστε την απόδειξη αγοράς σε περίπτωση που θελήσετε να αλλάξετε το ρούχο.",
        "example_en": "Keep the purchase receipt in case you want to exchange the garment.",
        "example2_el": "Χωρίς την απόδειξη αγοράς δεν μπορεί να γίνει επιστροφή χρημάτων.",
        "example2_en": "Without the purchase receipt, a money refund cannot be issued."
    },
    {
        "id": "A2P2-U05-009",
        "greek": "η αλλαγή προϊόντος",
        "english": "product exchange",
        "notes": "Collocation: η αλλαγή + genitive neuter του προϊόντος.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η αλλαγή (feminine)",
            "noun_genitive": "του προϊόντος (neuter, gen of το προϊόν)"
        },
        "keg_communicative_function": "Negotiating an exchange of goods at customer service desks",
        "example_el": "Ήρθα για μια αλλαγή προϊόντος επειδή το δώρο δεν ταίριαζε στο μέγεθος.",
        "example_en": "I came for a product exchange because the gift didn't match the size.",
        "example2_el": "Οι αλλαγές προϊόντων γίνονται δεκτές εντός δεκατεσσάρων ημερών.",
        "example2_en": "Product exchanges are accepted within fourteen days."
    },
    {
        "id": "A2P2-U05-010",
        "greek": "η επιστροφή χρημάτων",
        "english": "money refund",
        "notes": "Collocation: η επιστροφή + genitive plural των χρημάτων.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η επιστροφή (feminine)",
            "genitive": "των χρημάτων (from τα χρήματα)"
        },
        "keg_communicative_function": "Requesting monetary reimbursement for returned items",
        "example_el": "Δικαιούμαι επιστροφή χρημάτων αν το προϊόν είναι ελαττωματικό;",
        "example_en": "Am I entitled to a money refund if the product is defective?",
        "example2_el": "Το κατάστημα προσφέρει πιστωτικό σημείωμα ή πλήρη επιστροφή χρημάτων.",
        "example2_en": "The store offers store credit or a full money refund."
    },
    {
        "id": "A2P2-U05-011",
        "greek": "η εγγύηση δύο ετών",
        "english": "two-year warranty / guarantee",
        "notes": "Essential consumer right for electronics and appliances.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η εγγύηση",
            "numeral_genitive": "δύο ετών (genitive plural of το έτος)"
        },
        "keg_communicative_function": "Confirming warranty durations and repair coverage",
        "example_el": "Όλες οι ηλεκτρικές συσκευές καλύπτονται από επίσημη εγγύηση δύο ετών.",
        "example_en": "All electrical appliances are covered by an official two-year warranty.",
        "example2_el": "Σας δίνουμε την κάρτα εγγύησης σφραγισμένη από το κατάστημα.",
        "example2_en": "We give you the warranty card stamped by the shop."
    },
    {
        "id": "A2P2-U05-012",
        "greek": "οι εκπτώσεις",
        "english": "the sales / seasonal discounts",
        "notes": "Plural feminine noun in -σεις (from η έκπτωση). Summer and winter sales.",
        "gender_or_pos": "noun (feminine plural)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine plural",
            "nominative_plural": "οι εκπτώσεις",
            "genitive_plural": "των εκπτώσεων"
        },
        "keg_communicative_function": "Discussing seasonal sales periods and retail shopping opportunities",
        "example_el": "Οι χειμερινές εκπτώσεις ξεκινούν τη δεύτερη Δευτέρα του Ιανουαρίου.",
        "example_en": "Winter sales start on the second Monday of January.",
        "example2_el": "Περιμένω τις εκπτώσεις για να αγοράσω έναν καινούριο φορητό υπολογιστή.",
        "example2_en": "I am waiting for the sales to buy a new laptop computer."
    },
    {
        "id": "A2P2-U05-013",
        "greek": "η προσφορά",
        "english": "special offer / deal",
        "notes": "Feminine noun in -α. Plural: οι προσφορές.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της προσφοράς",
            "plural": "οι προσφορές"
        },
        "keg_communicative_function": "Spotting and discussing promotional bargains in flyers and ads",
        "example_el": "Βρήκα μια καταπληκτική προσφορά: αγοράζεις δύο προϊόντα και παίρνεις το τρίτο δωρεάν.",
        "example_en": "I found an amazing offer: you buy two products and get the third free.",
        "example2_el": "Η ειδική προσφορά ισχύει μέχρι το τέλος της εβδομάδας.",
        "example2_en": "The special offer is valid until the end of the week."
    },
    {
        "id": "A2P2-U05-014",
        "greek": "με έκπτωση είκοσι τοις εκατό",
        "english": "with a twenty percent discount",
        "notes": "Formula: τοις εκατό (%) with numerals.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "preposition": "με έκπτωση",
            "percentage_marker": "τοις εκατό (percent)"
        },
        "keg_communicative_function": "Calculating and discussing discount percentages",
        "example_el": "Αγοράσαμε τα παπούτσια με έκπτωση είκοσι τοις εκατό.",
        "example_en": "We bought the shoes with a twenty percent discount.",
        "example2_el": "Όλα τα βιβλία πωλούνται με έκπτωση τριάντα τοις εκατό.",
        "example2_en": "All books are sold at a thirty percent discount."
    },
    {
        "id": "A2P2-U05-015",
        "greek": "η πιστωτική κάρτα",
        "english": "credit card",
        "notes": "Contrast with η χρεωστική κάρτα (debit card).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η κάρτα",
            "adjective": "πιστωτική / χρεωστική"
        },
        "keg_communicative_function": "Choosing electronic payment methods at checkout counters",
        "example_el": "Δέχεστε πληρωμή με πιστωτική κάρτα ή μόνο μετρητά;",
        "example_en": "Do you accept credit card payment or only cash?",
        "example2_el": "Πλήρωσα ανέπαφα με την πιστωτική μου κάρτα στο μηχάνημα POS.",
        "example2_en": "I paid contactlessly with my credit card on the POS machine."
    },
    {
        "id": "A2P2-U05-016",
        "greek": "πληρώνω με μετρητά",
        "english": "I pay in cash",
        "notes": "Verb πληρώνω + με μετρητά (substantivized neuter plural).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "πληρώνω (aorist: πλήρωσα)",
            "noun_phrase": "με μετρητά"
        },
        "keg_communicative_function": "Selecting cash payment at physical points of sale",
        "example_el": "Προτιμώ να πληρώσω με μετρητά, ορίστε είκοσι ευρώ.",
        "example_en": "I prefer to pay in cash, here is twenty euros.",
        "example2_el": "Στη λαϊκή αγορά οι περισσότεροι παραγωγοί προτιμούν πληρωμή με μετρητά.",
        "example2_en": "At the street farmers' market most producers prefer cash payment."
    },
    {
        "id": "A2P2-U05-017",
        "greek": "το ταμείο",
        "english": "cash desk / checkout counter",
        "notes": "Genitive: του ταμείου. Plural: τα ταμεία.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter",
            "genitive": "του ταμείου",
            "plural": "τα ταμεία"
        },
        "keg_communicative_function": "Directing customers to payment counters in retail stores",
        "example_el": "Παρακαλώ περάστε στο ταμείο νούμερο δύο για να πληρώσετε.",
        "example_en": "Please step to cash register number two to pay.",
        "example2_el": "Υπήρχε μεγάλη ουρά στο ταμείο λόγω των εορταστικών αγορών.",
        "example2_en": "There was a long queue at the checkout due to festive shopping."
    },
    {
        "id": "A2P2-U05-018",
        "greek": "τα ρέστα",
        "english": "change (money returned)",
        "notes": "Neuter plural noun: τα ρέστα (genitive: των ρέστων).",
        "gender_or_pos": "noun (neuter plural)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter plural",
            "genitive": "των ρέστων"
        },
        "keg_communicative_function": "Receiving and checking cash change after a transaction",
        "example_el": "Ορίστε τα ρέστα σας και η απόδειξη, σας ευχαριστούμε πολύ.",
        "example_en": "Here is your change and the receipt, thank you very much.",
        "example2_el": "Μην ξεχάσετε τα ρέστα σας πάνω στον πάγκο!",
        "example2_en": "Don't forget your change on the counter!"
    },
    {
        "id": "A2P2-U05-019",
        "greek": "κρατήστε τα ρέστα",
        "english": "keep the change",
        "notes": "Polite imperative formula when tipping taxi drivers or servers.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "imperative": "κρατήστε (from κρατάω, formal/plural)",
            "noun": "τα ρέστα"
        },
        "keg_communicative_function": "Instructing a driver or server to retain change as a tip",
        "example_el": "Το κόμιστρο ήταν δεκαοκτώ ευρώ, έδωσα είκοσι και είπα: «Κρατήστε τα ρέστα».",
        "example_en": "The fare was eighteen euros, I gave twenty and said: 'Keep the change.'",
        "example2_el": "Είναι εντάξει, κρατήστε τα ρέστα για τον καφέ σας.",
        "example2_en": "It is fine, keep the change for your coffee."
    },
    {
        "id": "A2P2-U05-020",
        "greek": "η σακούλα",
        "english": "shopping bag / plastic bag",
        "notes": "Feminine noun in -α. Modern fee applies in Greek supermarkets.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της σακούλας",
            "plural": "οι σακούλες"
        },
        "keg_communicative_function": "Asking for or declining shopping bags at retail checkouts",
        "example_el": "Χρειάζεστε σακούλα ή έχετε δική σας πάνινη τσάντα;",
        "example_en": "Do you need a bag or do you have your own canvas bag?",
        "example2_el": "Έβαλα όλα τα ψώνια σε μια επαναχρησιμοποιούμενη σακούλα.",
        "example2_en": "I put all the groceries into a reusable shopping bag."
    },
    {
        "id": "A2P2-U05-021",
        "greek": "το ελαττωματικό προϊόν",
        "english": "defective / faulty product",
        "notes": "Collocation: ελαττωματικός (defective) + το προϊόν (product).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "το προϊόν (gen: του προϊόντος, pl: τα προϊόντα)",
            "adjective": "ελαττωματικός, -ή, -ό"
        },
        "keg_communicative_function": "Stating that a purchased good has a defect or manufacturing fault",
        "example_el": "Επέστρεψα το ελαττωματικό προϊόν στο κατάστημα για άμεση αντικατάσταση.",
        "example_en": "I returned the defective product to the store for immediate replacement.",
        "example2_el": "Το ρολόι δεν λειτουργεί σωστά, πρόκειται για ελαττωματικό προϊόν.",
        "example2_en": "The watch doesn't work properly, it is a defective product."
    },
    {
        "id": "A2P2-U05-022",
        "greek": "διαμαρτύρομαι",
        "english": "I complain / protest",
        "notes": "Mediopassive verb. Aorist: διαμαρτυρήθηκα. Noun: η διαμαρτυρία.",
        "gender_or_pos": "verb (mediopassive)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "voice": "mediopassive",
            "present": "διαμαρτύρομαι",
            "aorist": "διαμαρτυρήθηκα"
        },
        "keg_communicative_function": "Lodge formal complaints regarding poor services or products",
        "example_el": "Οι πελάτες διαμαρτυρήθηκαν έντονα για τη μεγάλη καθυστέρηση στην εξυπηρέτηση.",
        "example_en": "The customers complained vigorously about the long delay in service.",
        "example2_el": "Διαμαρτυρήθηκα στη διοίκηση για την κακή ποιότητα του φαγητού.",
        "example2_en": "I complained to management about the poor food quality."
    },
    {
        "id": "A2P2-U05-023",
        "greek": "το παράπονο",
        "english": "complaint / grievance",
        "notes": "Neuter noun in -ο. Collocation: κάνω παράπονα (I make complaints).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter",
            "genitive": "του παραπόνου",
            "plural": "τα παράπονα"
        },
        "keg_communicative_function": "Voicing grievances to store or service authorities",
        "example_el": "Αν έχετε κάποιο παράπονο, μπορείτε να συμπληρώσετε το ειδικό έντυπο.",
        "example_en": "If you have any complaint, you can fill out the special form.",
        "example2_el": "Δεν έχω κανένα παράπονο, όλα ήταν άψογα οργανωμένα.",
        "example2_en": "I have no complaints whatsoever, everything was impeccably organized."
    },
    {
        "id": "A2P2-U05-024",
        "greek": "ο υπεύθυνος του καταστήματος",
        "english": "store manager / person in charge",
        "notes": "Collocation: ο/η υπεύθυνος + genitive του καταστήματος.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "ο υπεύθυνος / η υπεύθυνη",
            "genitive": "του καταστήματος"
        },
        "keg_communicative_function": "Requesting to speak to senior managerial personnel",
        "example_el": "Θα ήθελα να μιλήσω με τον υπεύθυνο του καταστήματος, παρακαλώ.",
        "example_en": "I would like to speak with the store manager, please.",
        "example2_el": "Η υπεύθυνη του καταστήματος έλυσε το πρόβλημα με πολλή ευγένεια.",
        "example2_en": "The store manager solved the problem with great politeness."
    },
    {
        "id": "A2P2-U05-025",
        "greek": "το ωράριο καταστημάτων",
        "english": "store opening hours / operating schedule",
        "notes": "Compound collocation: το ωράριο + καταστημάτων. Crucial for Reading Task 1.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "το ωράριο (schedule/hours)",
            "genitive_plural": "των καταστημάτων"
        },
        "keg_communicative_function": "Reading and understanding retail business hours notices",
        "example_el": "Το εορταστικό ωράριο καταστημάτων περιλαμβάνει και λειτουργία τις Κυριακές.",
        "example_en": "The holiday store opening hours include operating on Sundays.",
        "example2_el": "Ποιο είναι το ωράριο των εμπορικών καταστημάτων την Τετάρτη το απόγευμα;",
        "example2_en": "What are commercial store hours on Wednesday afternoon?"
    },
    {
        "id": "A2P2-U05-026",
        "greek": "τα ψώνια της εβδομάδας",
        "english": "weekly grocery shopping",
        "notes": "Collocation: τα ψώνια + genitive της εβδομάδας.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "τα ψώνια (neuter plural)",
            "genitive": "της εβδομάδας"
        },
        "keg_communicative_function": "Describing household routine procurement chores",
        "example_el": "Κάθε Σάββατο πρωί πηγαίνουμε στο σούπερ μάρκετ για τα ψώνια της εβδομάδας.",
        "example_en": "Every Saturday morning we go to the supermarket for the weekly shopping.",
        "example2_el": "Κάνω μια λίστα πριν φύγω από το σπίτι για να μην ξεχάσω τίποτα.",
        "example2_en": "I make a list before leaving home so I don't forget anything."
    },
    {
        "id": "A2P2-U05-027",
        "greek": "το καλάθι αγορών",
        "english": "shopping cart / shopping basket",
        "notes": "Physical or virtual online shopping cart.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "το καλάθι (basket)",
            "genitive": "αγορών"
        },
        "keg_communicative_function": "Navigating physical or e-commerce supermarket baskets",
        "example_el": "Πάρτε ένα καλάθι αγορών από την είσοδο πριν ξεκινήσετε τα ψώνια.",
        "example_en": "Take a shopping basket from the entrance before you start shopping.",
        "example2_el": "Πρόσθεσα όλα τα προϊόντα στο ηλεκτρονικό καλάθι αγορών.",
        "example2_en": "I added all products to the online shopping cart."
    },
    {
        "id": "A2P2-U05-028",
        "greek": "στα ράφια",
        "english": "on the shelves",
        "notes": "Prepositional phrase: σε + τα ράφια (from το ράφι, gen: του ραφιού).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "prepositional phrase",
            "noun": "το ράφι (plural: τα ράφια)"
        },
        "keg_communicative_function": "Locating merchandise on grocery supermarket displays",
        "example_el": "Σε ποια ράφια βρίσκονται τα γαλακτοκομικά προϊόντα;",
        "example_en": "On which shelves are dairy products located?",
        "example2_el": "Τα καινούρια βιβλία τοποθετήθηκαν στα κεντρικά ράφια του βιβλιοπωλείου.",
        "example2_en": "The new books were placed on the central shelves of the bookstore."
    },
    {
        "id": "A2P2-U05-029",
        "greek": "η ημερομηνία λήξης",
        "english": "expiration date / best before date",
        "notes": "Collocation: η ημερομηνία + genitive feminine της λήξης. Vital product label info.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η ημερομηνία (date)",
            "genitive": "της λήξης (from η λήξη, expiration)"
        },
        "keg_communicative_function": "Checking product safety labels and food expiry dates",
        "example_el": "Ελέγχετε πάντα την ημερομηνία λήξης στα τρόφιμα πριν τα αγοράσετε.",
        "example_en": "Always check the expiration date on foods before buying them.",
        "example2_el": "Αυτό το γιαούρτι έχει περάσει την ημερομηνία λήξης του και δεν πρέπει να καταναλωθεί.",
        "example2_en": "This yogurt has passed its expiration date and should not be consumed."
    },
    {
        "id": "A2P2-U05-030",
        "greek": "συμφέρει οικονομικά",
        "english": "it is economical / it is good value for money",
        "notes": "Verb συμφέρει (impersonal 3rd singular) + adverb οικονομικά.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "συμφέρει (impersonal present)",
            "adverb": "οικονομικά"
        },
        "keg_communicative_function": "Evaluating cost-effectiveness and economic value in purchases",
        "example_el": "Συμφέρει οικονομικά να αγοράσουμε τη μεγάλη οικογενειακή συσκευασία.",
        "example_en": "It is economically advantageous to buy the large family pack.",
        "example2_el": "Η μηνιαία κάρτα απεριορίστων διαδρομών συμφέρει πολύ περισσότερο από τα απλά εισιτήρια.",
        "example2_en": "The monthly unlimited transit card is much more economical than single tickets."
    }
]

# -------------------------------------------------------------
# UNIT A2P2-06 CARDS (30 cards)
# Theme: Ταξίδια, Μεταφορές & Προσανατολισμός στην Πόλη
# -------------------------------------------------------------
CARDS_U06 = [
    {
        "id": "A2P2-U06-001",
        "greek": "το αεροδρόμιο",
        "english": "airport",
        "notes": "Compound noun: αέρας + δρόμος. Genitive: του αεροδρομίου.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter",
            "genitive": "του αεροδρομίου",
            "plural": "τα αεροδρόμια"
        },
        "keg_communicative_function": "Navigating airport environments and transit connections",
        "example_el": "Πρέπει να φτάσουμε στο αεροδρόμιο τουλάχιστον δύο ώρες πριν από την πτήση.",
        "example_en": "We must arrive at the airport at least two hours before the flight.",
        "example2_el": "Το διεθνές αεροδρόμιο της Αθήνας συνδέεται με το μετρό και τον προαστιακό.",
        "example2_en": "Athens International Airport is connected with the metro and suburban railway."
    },
    {
        "id": "A2P2-U06-002",
        "greek": "η πτήση",
        "english": "flight",
        "notes": "Third-declension feminine in -ση. Plural: οι πτήσεις, των πτήσεων.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της πτήσης",
            "plural": "οι πτήσεις"
        },
        "keg_communicative_function": "Tracking air travel flight numbers and statuses",
        "example_el": "Η πτήση για τα Χανιά αναχωρεί στις δέκα και είκοσι το πρωί.",
        "example_en": "The flight to Chania departs at ten twenty in the morning.",
        "example2_el": "Είχαμε μια πολύ ομαλή και ευχάριστη πτήση χωρίς αναταράξεις.",
        "example2_en": "We had a very smooth and pleasant flight without turbulence."
    },
    {
        "id": "A2P2-U06-003",
        "greek": "η κάρτα επιβίβασης",
        "english": "boarding pass",
        "notes": "Collocation: η κάρτα + genitive της επιβίβασης.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η κάρτα (feminine)",
            "genitive": "της επιβίβασης (boarding)"
        },
        "keg_communicative_function": "Presenting travel boarding documentation at airport gates",
        "example_el": "Δείξτε την κάρτα επιβίβασης και την ταυτότητά σας στον υπάλληλο.",
        "example_en": "Show your boarding pass and your ID to the clerk.",
        "example2_el": "Μπορείτε να κατεβάσετε την ηλεκτρονική κάρτα επιβίβασης στο κινητό σας τηλέφωνο.",
        "example2_en": "You can download the digital boarding pass onto your mobile phone."
    },
    {
        "id": "A2P2-U06-004",
        "greek": "ο έλεγχος αποσκευών",
        "english": "baggage inspection / security screening",
        "notes": "Collocation: ο έλεγχος + genitive plural των αποσκευών.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "ο έλεγχος (check/control)",
            "genitive_plural": "των αποσκευών (from η αποσκευή, luggage)"
        },
        "keg_communicative_function": "Following airport security and luggage screening procedures",
        "example_el": "Περάσαμε γρήγορα από τον έλεγχο αποσκευών χωρίς καμία καθυστέρηση.",
        "example_en": "We went through baggage security quickly without any delay.",
        "example2_el": "Απαγορεύονται τα υγρά άνω των εκατό χιλιοστολίτρων στον έλεγχο χειραποσκευών.",
        "example2_en": "Liquids over one hundred milliliters are prohibited in carry-on screening."
    },
    {
        "id": "A2P2-U06-005",
        "greek": "η πύλη επιβίβασης",
        "english": "boarding gate",
        "notes": "Collocation: η πύλη (gate) + genitive επιβίβασης.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η πύλη (feminine)",
            "genitive": "της επιβίβασης"
        },
        "keg_communicative_function": "Locating departure gates on airport display monitors",
        "example_el": "Η πύλη επιβίβασης κλείνει δεκαπέντε λεπτά πριν από την αναχώρηση της πτήσης.",
        "example_en": "The boarding gate closes fifteen minutes before flight departure.",
        "example2_el": "Παρακαλούνται οι επιβάτες για Ρόδο να προσέλθουν στην πύλη Β12.",
        "example2_en": "Passengers for Rhodes are requested to proceed to gate B12."
    },
    {
        "id": "A2P2-U06-006",
        "greek": "η αναχώρηση",
        "english": "departure",
        "notes": "Third-declension feminine in -ση. Opposite: η άφιξη.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της αναχώρησης",
            "verb": "αναχωρώ (I depart)"
        },
        "keg_communicative_function": "Identifying departure timetables in transit hubs",
        "example_el": "Κοιτάξτε τον πίνακα αναχωρήσεων για να δείτε την κατάσταση της πτήσης σας.",
        "example_en": "Look at the departure board to see the status of your flight.",
        "example2_el": "Η προγραμματισμένη ώρα αναχώρησης του τρένου είναι στις δεκατέσσερις και τριάντα.",
        "example2_en": "The scheduled departure time of the train is at fourteen thirty."
    },
    {
        "id": "A2P2-U06-007",
        "greek": "η άφιξη",
        "english": "arrival",
        "notes": "Third-declension feminine in -ξη. Plural: οι αφίξεις.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της άφιξης",
            "plural": "οι αφίξεις",
            "verb": "αφικνούμαι / φτάνω"
        },
        "keg_communicative_function": "Confirming arrival times and terminal meeting points",
        "example_el": "Θα σε περιμένω στην αίθουσα αφίξεων του αεροδρομίου.",
        "example_en": "I will wait for you in the arrivals hall of the airport.",
        "example2_el": "Η ακριβής ώρα άφιξης του πλοίου εξαρτάται από τον καιρό στο Αιγαίο.",
        "example2_en": "The exact arrival time of the ship depends on the weather in the Aegean."
    },
    {
        "id": "A2P2-U06-008",
        "greek": "η καθυστέρηση πτήσης",
        "english": "flight delay",
        "notes": "Collocation: η καθυστέρηση + genitive πτήσης.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η καθυστέρηση (delay)",
            "genitive": "της πτήσης"
        },
        "keg_communicative_function": "Listening to and interpreting transit delay announcements",
        "example_el": "Ανακοινώθηκε καθυστέρηση πτήσης δύο ωρών λόγω τεχνικού ελέγχου.",
        "example_en": "A two-hour flight delay was announced due to a technical inspection.",
        "example2_el": "Ζητούμε συγγνώμη για την απρόβλεπτη καθυστέρηση στην άφιξη του πλοίου.",
        "example2_en": "We apologize for the unforeseen delay in the ship's arrival."
    },
    {
        "id": "A2P2-U06-009",
        "greek": "η ακύρωση δρομολογίου",
        "english": "trip / service cancellation",
        "notes": "Collocation: η ακύρωση + genitive δρομολογίου (from το δρομολόγιο).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η ακύρωση (cancellation)",
            "genitive": "του δρομολογίου (itinerary / route)"
        },
        "keg_communicative_function": "Handling service cancellations and requesting rebooking",
        "example_el": "Λόγω της κακοκαιρίας και των ισχυρών ανέμων υπήρξε ακύρωση δρομολογίων στα πλοία.",
        "example_en": "Due to bad weather and high winds, there was a cancellation of ferry services.",
        "example2_el": "Σε περίπτωση ακύρωσης δρομολογίου, δικαιούστε πλήρη επιστροφή του εισιτηρίου.",
        "example2_en": "In case of trip cancellation, you are entitled to a full ticket refund."
    },
    {
        "id": "A2P2-U06-010",
        "greek": "το λιμάνι",
        "english": "port / harbor",
        "notes": "Neuter noun in -ι. Major Greek transit hub (Πειραιάς, Ραφήνα).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter",
            "genitive": "του λιμανιού",
            "plural": "τα λιμάνια"
        },
        "keg_communicative_function": "Navigating maritime passenger ports and ferry docks",
        "example_el": "Το λιμάνι του Πειραιά είναι ένα από τα μεγαλύτερα επιβατικά λιμάνια της Ευρώπης.",
        "example_en": "The port of Piraeus is one of the largest passenger ports in Europe.",
        "example2_el": "Πρέπει να βρισκόμαστε στο λιμάνι μία ώρα πριν τον απόπλου του πλοίου.",
        "example2_en": "We need to be at the port one hour before the ship's departure."
    },
    {
        "id": "A2P2-U06-011",
        "greek": "το πλοίο της γραμμής / το φέρι μπόουτ",
        "english": "scheduled ferry / ferry boat",
        "notes": "Key terms for island travel in Greece.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "nouns": "το πλοίο (ship) / το φέρι μπόουτ (indeclinable neuter)"
        },
        "keg_communicative_function": "Booking sea crossings and vehicle transport on ferries",
        "example_el": "Το πλοίο της γραμμής συνδέει καθημερινά τα νησιά των Κυκλάδων.",
        "example_en": "The scheduled ferry connects the Cycladic islands daily.",
        "example2_el": "Επιβιβάσαμε το αυτοκίνητο στο φέρι μπόουτ για την Εύβοια.",
        "example2_en": "We boarded the car onto the ferry boat for Evia."
    },
    {
        "id": "A2P2-U06-012",
        "greek": "η αποβάθρα",
        "english": "pier / dock / railway platform",
        "notes": "Dual context: train platform and port pier. Plural: οι αποβάθρες.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της αποβάθρας",
            "plural": "οι αποβάθρες"
        },
        "keg_communicative_function": "Locating train platforms and maritime ferry gates",
        "example_el": "Το τρένο για τη Θεσσαλονίκη αναχωρεί από την αποβάθρα νούμερο τέσσερα.",
        "example_en": "The train for Thessaloniki departs from platform number four.",
        "example2_el": "Περπατήσαμε κατά μήκος της αποβάθρας για να βρούμε την πύλη Ε7 στο λιμάνι.",
        "example2_en": "We walked along the pier to find gate E7 in the port."
    },
    {
        "id": "A2P2-U06-013",
        "greek": "το εισιτήριο με επιστροφή",
        "english": "round-trip / return ticket",
        "notes": "Collocation: εισιτήριο + με επιστροφή. Opp: απλό εισιτήριο.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "το εισιτήριο (ticket)",
            "prepositional_phrase": "με επιστροφή (with return)"
        },
        "keg_communicative_function": "Purchasing return tickets at station ticket booths",
        "example_el": "Ένα εισιτήριο με επιστροφή για Ναύπλιο, παρακαλώ.",
        "example_en": "One round-trip ticket to Nafplio, please.",
        "example2_el": "Τα εισιτήρια με επιστροφή έχουν συχνά έκπτωση είκοσι τοις εκατό.",
        "example2_en": "Return tickets often have a twenty percent discount."
    },
    {
        "id": "A2P2-U06-014",
        "greek": "το απλό εισιτήριο",
        "english": "one-way / single ticket",
        "notes": "Collocation: απλό (single) + εισιτήριο.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "adjective": "απλός, -ή, -ό",
            "noun": "το εισιτήριο"
        },
        "keg_communicative_function": "Requesting a single one-way trip fare",
        "example_el": "Πόσο κοστίζει το απλό ενιαίο εισιτήριο για τα μέσα μαζικής μεταφοράς;",
        "example_en": "How much does a single integrated transit ticket cost?",
        "example2_el": "Χρειάζομαι μόνο ένα απλό εισιτήριο, καθώς θα γυρίσω με αυτοκίνητο.",
        "example2_en": "I only need a one-way ticket, as I will return by car."
    },
    {
        "id": "A2P2-U06-015",
        "greek": "η επικύρωση εισιτηρίου",
        "english": "ticket validation / stamping",
        "notes": "Noun: η επικύρωση. Verb: επικυρώνω το εισιτήριο.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η επικύρωση",
            "genitive": "του εισιτηρίου",
            "verb": "επικυρώνω (I validate)"
        },
        "keg_communicative_function": "Following mandatory ticket validation rules on public transit",
        "example_el": "Η επικύρωση του εισιτηρίου στα ακυρωτικά μηχανήματα είναι υποχρεωτική.",
        "example_en": "Validating the ticket at the validation machines is mandatory.",
        "example2_el": "Μην ξεχάσετε να επικυρώσετε το εισιτήριό σας μόλις μπείτε στο λεωφορείο.",
        "example2_en": "Don't forget to validate your ticket as soon as you enter the bus."
    },
    {
        "id": "A2P2-U06-016",
        "greek": "ο σταθμός λεωφορείων / τρένων",
        "english": "bus station / train station",
        "notes": "Noun: ο σταθμός (gen: του σταθμού, pl: οι σταθμοί).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "ο σταθμός",
            "genitive_plural": "των λεωφορείων / των τρένων"
        },
        "keg_communicative_function": "Locating intercity terminals and central rail hubs",
        "example_el": "Ο κεντρικός σταθμός λεωφορείων του ΚΤΕΛ βρίσκεται στην οδό Κηφισού.",
        "example_en": "The central KTEL bus station is located on Kifissou street.",
        "example2_el": "Συναντηθήκαμε στον σιδηροδρομικό σταθμό μπροστά από το κεντρικό ρολόι.",
        "example2_en": "We met at the railway station in front of the main clock."
    },
    {
        "id": "A2P2-U06-017",
        "greek": "η στάση του λεωφορείου",
        "english": "bus stop",
        "notes": "Collocation: η στάση + genitive του λεωφορείου.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η στάση (stop)",
            "genitive": "του λεωφορείου"
        },
        "keg_communicative_function": "Asking for local bus stop landmarks and wait points",
        "example_el": "Η στάση του λεωφορείου είναι ακριβώς έξω από το δημαρχείο.",
        "example_en": "The bus stop is right outside the town hall.",
        "example2_el": "Ποιο λεωφορείο περνάει από αυτή τη στάση για το κέντρο;",
        "example2_en": "Which bus passes from this stop going to the center?"
    },
    {
        "id": "A2P2-U06-018",
        "greek": "αλλάζω γραμμή",
        "english": "I change lines / transfer",
        "notes": "Metro navigation phrase. Verb αλλάζω + noun γραμμή.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "αλλάζω (aorist: άλλαξα)",
            "noun": "η γραμμή (accusative: γραμμή)"
        },
        "keg_communicative_function": "Describing subway transfers and line changes in urban transit",
        "example_el": "Στον σταθμό Σύνταγμα αλλάζουμε γραμμή για να πάρουμε την κόκκινη γραμμή.",
        "example_en": "At Syntagma station we change lines to take the red line.",
        "example2_el": "Πρέπει να αλλάξεις γραμμή στο Μοναστηράκι για να πας προς Πειραιά.",
        "example2_en": "You have to change lines at Monastiraki to go towards Piraeus."
    },
    {
        "id": "A2P2-U06-019",
        "greek": "η ανταπόκριση",
        "english": "connection / connecting flight or train",
        "notes": "Third-declension feminine in -ση. Transit link between routes.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της ανταπόκρισης",
            "plural": "οι ανταποκρίσεις"
        },
        "keg_communicative_function": "Catching connecting services without missing departure slots",
        "example_el": "Έχουμε μόνο σαράντα λεπτά για την ανταπόκριση της πτήσης στη Φρανκφούρτη.",
        "example_en": "We have only forty minutes for the flight connection in Frankfurt.",
        "example2_el": "Ευτυχώς προλάβαμε την ανταπόκριση του τρένου για Λάρισα.",
        "example2_en": "Fortunately we caught the connecting train for Larissa."
    },
    {
        "id": "A2P2-U06-020",
        "greek": "η πινακίδα κατεύθυνσης",
        "english": "direction sign / road sign",
        "notes": "Collocation: η πινακίδα + genitive κατεύθυνσης.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η πινακίδα (sign/signboard)",
            "genitive": "της κατεύθυνσης (direction)"
        },
        "keg_communicative_function": "Reading highway and urban orientation signage",
        "example_el": "Ακολουθήστε τις πράσινες πινακίδες κατεύθυνσης προς τον αυτοκινητόδρομο.",
        "example_en": "Follow the green direction signs towards the motorway.",
        "example2_el": "Η πινακίδα δείχνει ότι το αρχαίο θέατρο απέχει πεντακόσια μέτρα.",
        "example2_en": "The sign shows that the ancient theater is five hundred meters away."
    },
    {
        "id": "A2P2-U06-021",
        "greek": "στρίβω δεξιά / αριστερά",
        "english": "I turn right / left",
        "notes": "Verb στρίβω (aorist: έστριψα, imperative: στρίψε / στρίψτε). Core navigation verb.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "στρίβω (aorist: έστριψα, imperative: στρίψε / στρίψτε)",
            "adverbs": "δεξιά / αριστερά"
        },
        "keg_communicative_function": "Giving and following directional turn instructions on streets",
        "example_el": "Στο πρώτο στενό στρίψτε δεξιά και θα δείτε το φαρμακείο.",
        "example_en": "At the first alley turn right and you will see the pharmacy.",
        "example2_el": "Στρίψτε αριστερά μετά την εκκλησία και προχωρήστε μέχρι την πλατεία.",
        "example2_en": "Turn left after the church and proceed until the square."
    },
    {
        "id": "A2P2-U06-022",
        "greek": "πηγαίνω ευθεία",
        "english": "I go straight ahead",
        "notes": "Adverb: ευθεία (straight on). Imperative: πηγαίνετε ευθεία / πηγαίνετε ίσια.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "πηγαίνω / πάω (imperative: πήγαινε / πηγαίνετε)",
            "adverb": "ευθεία / ίσια"
        },
        "keg_communicative_function": "Instructing someone to proceed straight forward on a route",
        "example_el": "Πηγαίνετε όλο ευθεία για διακόσια μέτρα μέχρι το μεγάλο σούπερ μάρκετ.",
        "example_en": "Go straight ahead for two hundred meters up to the big supermarket.",
        "example2_el": "Συνεχίστε ευθεία σε αυτόν τον κεντρικό δρόμο χωρίς να στρίψετε πουθενά.",
        "example2_en": "Continue straight on this main road without turning anywhere."
    },
    {
        "id": "A2P2-U06-023",
        "greek": "στο φανάρι",
        "english": "at the traffic light",
        "notes": "Prepositional phrase: σε + το φανάρι (colloquial for traffic light; lit. lantern).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "prepositional phrase",
            "noun": "το φανάρι (gen: του φαναριού, pl: τα φανάρια)",
            "formal_equivalent": "ο φωτεινός σηματοδότης"
        },
        "keg_communicative_function": "Using street landmarks and traffic lights for navigational cues",
        "example_el": "Σταματήστε στο φανάρι και στρίψτε αριστερά όταν ανάψει το πράσινο βέλος.",
        "example_en": "Stop at the traffic light and turn left when the green arrow lights up.",
        "example2_el": "Στο δεύτερο φανάρι μετά τη γέφυρα κάντε αναστροφή.",
        "example2_en": "At the second traffic light after the bridge, make a U-turn."
    },
    {
        "id": "A2P2-U06-024",
        "greek": "στη διασταύρωση",
        "english": "at the intersection / crossroads",
        "notes": "Noun: η διασταύρωση. Prepositional: σε + τη διασταύρωση.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "prepositional phrase",
            "noun": "η διασταύρωση (3rd declension feminine)",
            "genitive": "της διασταύρωσης"
        },
        "keg_communicative_function": "Directing turns and maneuvers at street crossings",
        "example_el": "Προσέξτε στη διασταύρωση γιατί δεν υπάρχει καλή ορατότητα.",
        "example_en": "Watch out at the intersection because there is poor visibility.",
        "example2_el": "Στη διασταύρωση των οδών Πανεπιστημίου και Κοραή βρίσκεται ο κινηματογράφος.",
        "example2_en": "At the intersection of Panepistimiou and Korai streets is the cinema."
    },
    {
        "id": "A2P2-U06-025",
        "greek": "απέναντι από...",
        "english": "opposite from / across from...",
        "notes": "Prepositional locative: απέναντι + από + accusative.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "prepositional phrase",
            "adverb": "απέναντι",
            "preposition": "από + accusative"
        },
        "keg_communicative_function": "Describing relative spatial positions across a street",
        "example_el": "Η τράπεζα είναι ακριβώς απέναντι από το ταχυδρομείο.",
        "example_en": "The bank is directly opposite the post office.",
        "example2_el": "Σταθείτε απέναντι από το περίπτερο και θα έρθω να σας βρω.",
        "example2_en": "Stand across from the kiosk and I will come find you."
    },
    {
        "id": "A2P2-U06-026",
        "greek": "δίπλα σε...",
        "english": "next to / beside...",
        "notes": "Prepositional locative: δίπλα + σε + accusative.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "prepositional phrase",
            "adverb": "δίπλα",
            "preposition": "σε + accusative"
        },
        "keg_communicative_function": "Specifying proximity adjacent to buildings or shops",
        "example_el": "Το ξενοδοχείο είναι χτισμένο δίπλα στη θάλασσα.",
        "example_en": "The hotel is built right next to the sea.",
        "example2_el": "Το φαρμακείο βρίσκεται ακριβώς δίπλα στο ιατρείο.",
        "example2_en": "The pharmacy is located right next to the clinic."
    },
    {
        "id": "A2P2-U06-027",
        "greek": "ανάμεσα σε...",
        "english": "between / among...",
        "notes": "Prepositional locative: ανάμεσα + σε + accusative.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "prepositional phrase",
            "adverb": "ανάμεσα",
            "preposition": "σε + accusative"
        },
        "keg_communicative_function": "Indicating intermediate positions between two landmarks",
        "example_el": "Το κατάστημα βρίσκεται ανάμεσα στον φούρνο και το βιβλιοπωλείο.",
        "example_en": "The shop is located between the bakery and the bookstore.",
        "example2_el": "Υπάρχει ένα όμορφο μικρό πάρκο ανάμεσα στα δύο ψηλά κτίρια.",
        "example2_en": "There is a beautiful small park between the two tall buildings."
    },
    {
        "id": "A2P2-U06-028",
        "greek": "χάθηκα",
        "english": "I got lost",
        "notes": "Simple past of χάνομαι (deponent/mediopassive of χάνω).",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present": "χάνομαι",
            "plural": "χαθήκαμε"
        },
        "keg_communicative_function": "Admitting being lost and asking strangers for assistance",
        "example_el": "Συγγνώμη, χάθηκα στους στενούς δρόμους, πώς μπορώ να βγω στην κεντρική λεωφόρο;",
        "example_en": "Excuse me, I got lost in the narrow streets, how can I get out to the main avenue?",
        "example2_el": "Μην ανησυχείτε αν χαθείτε, οι ντόπιοι είναι πάντα πρόθυμοι να βοηθήσουν.",
        "example2_en": "Don't worry if you get lost, the locals are always willing to help."
    },
    {
        "id": "A2P2-U06-029",
        "greek": "μπορείτε να μου δείξετε στον χάρτη;",
        "english": "can you show me on the map?",
        "notes": "Polite asking formula: modal verb + subjunctive + accusative object.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "modal": "μπορείτε (formal)",
            "verb": "να δείξετε (from δείχνω)",
            "locative": "στον χάρτη (on the map)"
        },
        "keg_communicative_function": "Requesting graphic / cartographic orientation assistance",
        "example_el": "Δεν γνωρίζω την περιοχή, μπορείτε να μου δείξετε στον χάρτη πού βρισκόμαστε;",
        "example_en": "I don't know the area, can you show me on the map where we are?",
        "example2_el": "Μπορείς να μου δείξεις στο κινητό ποια διαδρομή είναι πιο σύντομη;",
        "example2_en": "Can you show me on your phone which route is shorter?"
    },
    {
        "id": "A2P2-U06-030",
        "greek": "καλό ταξίδι!",
        "english": "have a good trip! / safe travels!",
        "notes": "Standard Greek travel wishing formula. Adjective: καλός + noun: το ταξίδι.",
        "gender_or_pos": "phrase / exclamation",
        "grammatical_info": {
            "part_of_speech": "exclamation / greeting",
            "adjective": "καλό (neuter accusative)",
            "noun": "το ταξίδι"
        },
        "keg_communicative_function": "Wishing safe journeys to departing friends or colleagues",
        "example_el": "Σας ευχόμαστε καλό ταξίδι και καλή επιστροφή στην πατρίδα σας!",
        "example_en": "We wish you safe travels and a safe return to your homeland!",
        "example2_el": "Καλό ταξίδι και να περάσετε υπέροχα στις διακοπές σας!",
        "example2_en": "Have a good trip and have a wonderful time on your vacation!"
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
    print("Generating KEG-A2 Part 2: Batch 3 (Units 05 & 06)")
    print("==================================================")
    
    u05_notes = """Unit A2P2-05 Core Notes: Αγορές, Καταστήματα & Καταναλωτικές Συνήθειες (Shopping, Retail & Consumer Exchanges)
• Official KEG A2 Exam Alignment:
  - Speaking Stage 2 (Shop simulation): Asking for sizes (μέγεθος, νούμερο), requesting fitting room (δοκιμαστήριο), trying on clothes (μου κάνει, στενό, φαρδύ, μου πάει).
  - Consumer Transactions: Payment methods (μετρητά, πιστωτική κάρτα), receipts (απόδειξη αγοράς), sales (εκπτώσεις, προσφορές).
  - Consumer Protection & Complaints: Returning defective items (ελαττωματικό προϊόν, αλλαγή προϊόντος, επιστροφή χρημάτων, διαμαρτύρομαι, παράπονο)."""

    process_unit(
        unit_id="unit-a2p2-05",
        lesson_id="lesson-01",
        title="Μάθημα 5: Αγορές, Καταστήματα & Καταναλωτικές Συνήθειες (Shopping, Retail & Consumer Exchanges)",
        description="Mastering shopping role-plays, garment fitting vocabulary, payment methods, sales terms, product exchanges, and consumer complaint dialogues for the KEG A2 Speaking and Reading sections.",
        lesson_notes=u05_notes,
        cards=CARDS_U05,
        order_code="KEG-A2-P2-05-A"
    )

    u06_notes = """Unit A2P2-06 Core Notes: Ταξίδια, Μεταφορές & Προσανατολισμός στην Πόλη (Travel, Transit & Urban Navigation)
• Official KEG A2 Exam Alignment:
  - Listening Section 1 & 2: Transport announcements at airports (πτήση, κάρτα επιβίβασης, πύλη, καθυστέρηση) and ports (λιμάνι, πλοίο της γραμμής, αποβάθρα).
  - Speaking Stage 2 & 3: Ticket booking (εισιτήριο με επιστροφή, απλό εισιτήριο), transit transfers (αλλάζω γραμμή, ανταπόκριση).
  - Street Directions & Orientation: Locative adverbs and navigation imperatives (στρίβω δεξιά/αριστερά, πηγαίνω ευθεία, στο φανάρι, στη διασταύρωση, απέναντι, δίπλα, ανάμεσα)."""

    process_unit(
        unit_id="unit-a2p2-06",
        lesson_id="lesson-01",
        title="Μάθημα 6: Ταξίδια, Μεταφορές & Προσανατολισμός στην Πόλη (Travel, Transit & Urban Navigation)",
        description="Navigating airports, ports, train and metro stations, booking tickets, interpreting transit delays, and giving or following detailed city street directions for the KEG A2 Listening and Speaking exams.",
        lesson_notes=u06_notes,
        cards=CARDS_U06,
        order_code="KEG-A2-P2-06-A"
    )

    manifest_entries = [
        {
            "id": "unit-a2p2-05",
            "title": "Μάθημα 5: Αγορές, Καταστήματα & Καταναλωτικές Συνήθειες (Shopping, Retail & Consumer Exchanges)",
            "description": "Mastering shopping role-plays, garment fitting vocabulary, payment methods, sales terms, product exchanges, and consumer complaint dialogues for the KEG A2 Speaking and Reading sections.",
            "order": "KEG-A2-P2-05-A",
            "total_lessons": 1,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2p2-05/lesson-01.yaml",
                    "title": "Μάθημα 5: Αγορές, Καταστήματα & Καταναλωτικές Συνήθειες (Shopping, Retail & Consumer Exchanges)"
                }
            ]
        },
        {
            "id": "unit-a2p2-06",
            "title": "Μάθημα 6: Ταξίδια, Μεταφορές & Προσανατολισμός στην Πόλη (Travel, Transit & Urban Navigation)",
            "description": "Navigating airports, ports, train and metro stations, booking tickets, interpreting transit delays, and giving or following detailed city street directions for the KEG A2 Listening and Speaking exams.",
            "order": "KEG-A2-P2-06-A",
            "total_lessons": 1,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2p2-06/lesson-01.yaml",
                    "title": "Μάθημα 6: Ταξίδια, Μεταφορές & Προσανατολισμός στην Πόλη (Travel, Transit & Urban Navigation)"
                }
            ]
        }
    ]

    update_manifest(manifest_entries)
    print("\n[OK] Batch 3 finished successfully!")

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Script to create Unit 108 from Klik A1 (Pages 151-174):
Ενότητα 7: Γιορτές! Ώρα για ψώνια - Βασικό Λεξιλόγιο
Strictly conforming to docs/LESSON_CREATION_GUIDE.md and the klik-a1-deck-builder skill.
"""
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
UNIT_DIR = CONTENT_DIR / "unit-108"
UNIT_DIR.mkdir(parents=True, exist_ok=True)
YAML_PATH = UNIT_DIR / "lesson-01.yaml"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

cards_u108 = [
    # =========================================================================
    # 1. Holidays, Celebrations & Party Planning (pp. 155-157, 173-174)
    # =========================================================================
    {
        "id": "A1-U108-001",
        "greek": "η γιορτή",
        "phonetic_hint": "ee yor-TEE",
        "english": "holiday / celebration / feast day",
        "notes": "Klik A1 p. 155, 157. Feminine noun in -ή with plural in -ές. Core thematic word of Unit 7.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Οι γιορτές των Χριστουγέννων είναι οι αγαπημένες μου.",
        "example_en": "The Christmas holidays are my favorite.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι γιορτές",
            "accusative_singular": "τη γιορτή"
        },
        "keg_communicative_function": "Discussing holidays and festive seasons"
    },
    {
        "id": "A1-U108-002",
        "greek": "τα Χριστούγεννα",
        "phonetic_hint": "tah khree-STOO-yeh-nah",
        "english": "Christmas",
        "notes": "Klik A1 p. 155, 156, 157. Neuter noun used only in plural (plurale tantum).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τα Χριστούγεννα μαζεύεται όλη η οικογένεια γύρω από το τραπέζι.",
        "example_en": "At Christmas the whole family gathers around the table.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Χριστούγεννα",
            "accusative_singular": "τα Χριστούγεννα"
        },
        "keg_communicative_function": "Naming the Christmas holiday"
    },
    {
        "id": "A1-U108-003",
        "greek": "η Πρωτοχρονιά",
        "phonetic_hint": "ee pro-toh-khro-NYAH",
        "english": "New Year's Day",
        "notes": "Klik A1 p. 157, 170. Feminine compound noun: πρώτος + χρονιά.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Την Πρωτοχρονιά ανταλλάσσουμε δώρα και ευχές.",
        "example_en": "On New Year's Day we exchange gifts and wishes.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι Πρωτοχρονιές",
            "accusative_singular": "την Πρωτοχρονιά"
        },
        "keg_communicative_function": "Naming the New Year holiday"
    },
    {
        "id": "A1-U108-004",
        "greek": "το Πάσχα",
        "phonetic_hint": "to PAH-skhah",
        "english": "Easter",
        "notes": "Klik A1 p. 157. Indeclinable neuter noun.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το Πάσχα σουβλίζουμε αρνί και τρώμε τσουρέκι.",
        "example_en": "At Easter we roast lamb on a spit and eat sweet bread.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Πάσχα",
            "accusative_singular": "το Πάσχα"
        },
        "keg_communicative_function": "Naming the Easter holiday"
    },
    {
        "id": "A1-U108-005",
        "greek": "τα γενέθλια",
        "phonetic_hint": "tah yeh-NEHTH-lee-ah",
        "english": "birthday",
        "notes": "Klik A1 p. 174. Neuter noun used only in plural (plurale tantum).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κάνω ένα μεγάλο πάρτι για τα γενέθλιά μου το Σάββατο.",
        "example_en": "I am having a big party for my birthday on Saturday.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα γενέθλια",
            "accusative_singular": "τα γενέθλια"
        },
        "keg_communicative_function": "Talking about birthdays"
    },
    {
        "id": "A1-U108-006",
        "greek": "η ονομαστική γιορτή",
        "phonetic_hint": "ee o-no-mah-stee-KEE yor-TEE",
        "english": "name day",
        "notes": "Klik A1 p. 157, 174. Feminine noun phrase: επίθετο + ουσιαστικό.",
        "gender_or_pos": "noun phrase (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Στην Ελλάδα η ονομαστική γιορτή είναι πολύ σημαντική.",
        "example_en": "In Greece the name day is very important.",
        "grammatical_info": {
            "part_of_speech": "noun phrase (feminine)",
            "plural": "οι ονομαστικές γιορτές",
            "accusative_singular": "την ονομαστική γιορτή"
        },
        "keg_communicative_function": "Discussing cultural name day traditions"
    },
    {
        "id": "A1-U108-007",
        "greek": "το πάρτι",
        "phonetic_hint": "to PAHR-tee",
        "english": "party",
        "notes": "Klik A1 p. 158, 174. Indeclinable neuter loan noun.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Σε προσκαλώ στο πάρτι που κάνω στο σπίτι μου.",
        "example_en": "I invite you to the party I am having at my house.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πάρτι",
            "accusative_singular": "το πάρτι"
        },
        "keg_communicative_function": "Inviting people to social parties"
    },
    {
        "id": "A1-U108-008",
        "greek": "η πρόσκληση",
        "phonetic_hint": "ee PRO-sklee-see",
        "english": "invitation",
        "notes": "Klik A1 p. 174. Feminine noun in -ση with plural in -σεις.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Έλαβα μια όμορφη πρόσκληση για τα γενέθλια της Ελένης.",
        "example_en": "I received a lovely invitation for Eleni's birthday.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι προσκλήσεις",
            "accusative_singular": "την πρόσκληση"
        },
        "keg_communicative_function": "Writing and receiving event invitations"
    },
    {
        "id": "A1-U108-009",
        "greek": "το δώρο",
        "phonetic_hint": "to THO-ro",
        "english": "gift / present",
        "notes": "Klik A1 p. 155, 156, 170. Neuter noun in -ο with plural in -α.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αγοράζω ένα όμορφο δώρο για τη μητέρα μου.",
        "example_en": "I buy a beautiful gift for my mother.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα δώρα",
            "accusative_singular": "το δώρο"
        },
        "keg_communicative_function": "Buying and offering gifts"
    },
    {
        "id": "A1-U108-010",
        "greek": "το στολίδι",
        "phonetic_hint": "to sto-LEE-thee",
        "english": "ornament / decoration",
        "notes": "Klik A1 p. 155, 156. Neuter noun in -ι with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βάζουμε πολύχρωμα στολίδια στο χριστουγεννιάτικο δέντρο.",
        "example_en": "We put colorful ornaments on the Christmas tree.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα στολίδια",
            "accusative_singular": "το στολίδι"
        },
        "keg_communicative_function": "Describing festive decorations"
    },
    {
        "id": "A1-U108-011",
        "greek": "το χριστουγεννιάτικο δέντρο",
        "phonetic_hint": "to khree-stoo-yeh-NYAH-tee-ko THEN-dro",
        "english": "Christmas tree",
        "notes": "Klik A1 p. 155, 156. Compound noun phrase with neuter adjective and noun.",
        "gender_or_pos": "noun phrase (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Στολίζουμε το χριστουγεννιάτικο δέντρο με φωτάκια και μπάλες.",
        "example_en": "We decorate the Christmas tree with lights and baubles.",
        "grammatical_info": {
            "part_of_speech": "noun phrase (neuter)",
            "plural": "τα χριστουγεννιάτικα δέντρα",
            "accusative_singular": "το χριστουγεννιάτικο δέντρο"
        },
        "keg_communicative_function": "Referring to Christmas trees"
    },
    {
        "id": "A1-U108-012",
        "greek": "τα φωτάκια",
        "phonetic_hint": "tah foh-TAH-kyah",
        "english": "fairy lights / string lights",
        "notes": "Klik A1 p. 155. Diminutive neuter plural of φως (light).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ανάβουμε τα φωτάκια στο μπαλκόνι κάθε βράδυ.",
        "example_en": "We turn on the fairy lights on the balcony every evening.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα φωτάκια",
            "accusative_singular": "τα φωτάκια"
        },
        "keg_communicative_function": "Describing decorative lighting"
    },

    # =========================================================================
    # 2. Clothing & Garments (pp. 163-167)
    # =========================================================================
    {
        "id": "A1-U108-013",
        "greek": "τα ψώνια",
        "phonetic_hint": "tah PSO-nyah",
        "english": "shopping / purchases / groceries",
        "notes": "Klik A1 p. 155, 163. Neuter noun used predominantly in plural.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πηγαίνω στο κέντρο για ψώνια το απόγευμα.",
        "example_en": "I am going downtown for shopping in the afternoon.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ψώνια",
            "accusative_singular": "τα ψώνια"
        },
        "keg_communicative_function": "Talking about shopping excursions"
    },
    {
        "id": "A1-U108-014",
        "greek": "το ρούχο",
        "phonetic_hint": "to ROO-kho",
        "english": "garment / piece of clothing",
        "notes": "Klik A1 p. 163, 165. Neuter noun in -ο with plural in -α (τα ρούχα).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αυτό το ρούχο είναι από εξαιρετικό βαμβάκι.",
        "example_en": "This garment is made of excellent cotton.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ρούχα",
            "accusative_singular": "το ρούχο"
        },
        "keg_communicative_function": "Describing clothing items"
    },
    {
        "id": "A1-U108-015",
        "greek": "το φόρεμα",
        "phonetic_hint": "to FO-reh-mah",
        "english": "dress",
        "notes": "Klik A1 p. 164, 165, 169. Neuter noun in -μα with plural in -ματα.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η Ελένη φοράει ένα κομψό μαύρο φόρεμα στο πάρτι.",
        "example_en": "Eleni wears an elegant black dress to the party.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα φορέματα",
            "accusative_singular": "το φόρεμα"
        },
        "keg_communicative_function": "Naming and describing dresses"
    },
    {
        "id": "A1-U108-016",
        "greek": "η φούστα",
        "phonetic_hint": "ee FOO-stah",
        "english": "skirt",
        "notes": "Klik A1 p. 166, 168. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αυτή η ροζ φούστα ταιριάζει με το λευκό σου πουκάμισο.",
        "example_en": "This pink skirt matches your white shirt.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι φούστες",
            "accusative_singular": "τη φούστα"
        },
        "keg_communicative_function": "Describing skirts"
    },
    {
        "id": "A1-U108-017",
        "greek": "το παντελόνι",
        "phonetic_hint": "to pahn-deh-LO-nee",
        "english": "trousers / pants",
        "notes": "Klik A1 p. 165, 166. Neuter noun in -ι with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Δοκιμάζω ένα γκρι παντελόνι στο δοκιμαστήριο.",
        "example_en": "I try on grey trousers in the fitting room.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα παντελόνια",
            "accusative_singular": "το παντελόνι"
        },
        "keg_communicative_function": "Selecting and trying on trousers"
    },
    {
        "id": "A1-U108-018",
        "greek": "το τζιν",
        "phonetic_hint": "to dzeen",
        "english": "jeans / denim trousers",
        "notes": "Klik A1 p. 165. Indeclinable neuter loan noun.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Φοράω το αγαπημένο μου μπλε τζιν κάθε μέρα.",
        "example_en": "I wear my favorite blue jeans every day.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα τζιν",
            "accusative_singular": "το τζιν"
        },
        "keg_communicative_function": "Referring to denim jeans"
    },
    {
        "id": "A1-U108-019",
        "greek": "το πουκάμισο",
        "phonetic_hint": "to poo-KAH-mee-so",
        "english": "shirt",
        "notes": "Klik A1 p. 166. Neuter noun in -ο with plural in -α.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο Νίκος φοράει ένα καθαρό λευκό πουκάμισο στο γραφείο.",
        "example_en": "Nikos wears a clean white shirt to the office.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πουκάμισα",
            "accusative_singular": "το πουκάμισο"
        },
        "keg_communicative_function": "Describing men's and women's shirts"
    },
    {
        "id": "A1-U108-020",
        "greek": "το μπλουζάκι",
        "phonetic_hint": "to bloo-ZAH-kee",
        "english": "T-shirt / short-sleeved top",
        "notes": "Klik A1 p. 165. Diminutive neuter noun in -άκι.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το καλοκαίρι προτιμώ βαμβακερά μπλουζάκια.",
        "example_en": "In the summer I prefer cotton T-shirts.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μπλουζάκια",
            "accusative_singular": "το μπλουζάκι"
        },
        "keg_communicative_function": "Describing casual T-shirts"
    },
    {
        "id": "A1-U108-021",
        "greek": "η μπλούζα",
        "phonetic_hint": "ee BLOO-zah",
        "english": "blouse / top / sweater",
        "notes": "Klik A1 p. 165, 169. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αυτή η μάλλινη μπλούζα είναι πολύ ζεστή για τον χειμώνα.",
        "example_en": "This wool blouse is very warm for the winter.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι μπλούζες",
            "accusative_singular": "την μπλούζα"
        },
        "keg_communicative_function": "Identifying blouses and sweaters"
    },
    {
        "id": "A1-U108-022",
        "greek": "το κοστούμι",
        "phonetic_hint": "to ko-STOO-mee",
        "english": "suit",
        "notes": "Klik A1 p. 165. Neuter noun in -ι with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Χρειάζεται ένα επίσημο κοστούμι για τη συνέντευξη.",
        "example_en": "He needs a formal suit for the interview.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κοστούμια",
            "accusative_singular": "το κοστούμι"
        },
        "keg_communicative_function": "Describing formal suits"
    },
    {
        "id": "A1-U108-023",
        "greek": "το σακάκι",
        "phonetic_hint": "to sah-KAH-kee",
        "english": "jacket / blazer",
        "notes": "Klik A1 p. 165. Neuter noun in -ι with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το μαύρο σακάκι ταιριάζει με όλα τα παντελόνια μου.",
        "example_en": "The black blazer matches all my trousers.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα σακάκια",
            "accusative_singular": "το σακάκι"
        },
        "keg_communicative_function": "Identifying suit jackets and blazers"
    },
    {
        "id": "A1-U108-024",
        "greek": "το παλτό",
        "phonetic_hint": "to pahl-TO",
        "english": "coat / overcoat",
        "notes": "Klik A1 p. 165. Neuter noun with stress on ultima, plural: τα παλτά.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Φοράω ζεστό παλτό γιατί έξω χιονίζει.",
        "example_en": "I wear a warm coat because it is snowing outside.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα παλτά",
            "accusative_singular": "το παλτό"
        },
        "keg_communicative_function": "Naming winter overcoats"
    },
    {
        "id": "A1-U108-025",
        "greek": "το μπουφάν",
        "phonetic_hint": "to boo-FAHN",
        "english": "jacket / winter jacket / parka",
        "notes": "Klik A1 p. 168. Indeclinable neuter loan noun.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πάρε το μπουφάν σου γιατί έχει κρύο και αέρα.",
        "example_en": "Take your jacket because it is cold and windy.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μπουφάν",
            "accusative_singular": "το μπουφάν"
        },
        "keg_communicative_function": "Referring to casual jackets and windbreakers"
    },
    {
        "id": "A1-U108-026",
        "greek": "η ζακέτα",
        "phonetic_hint": "ee zah-KEH-tah",
        "english": "cardigan / light zippered jacket",
        "notes": "Klik A1 p. 166. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βάζω μια πλεκτή ζακέτα όταν δροσίζει το βράδυ.",
        "example_en": "I put on a knitted cardigan when it gets cool in the evening.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ζακέτες",
            "accusative_singular": "τη ζακέτα"
        },
        "keg_communicative_function": "Describing light cardigans and knitwear"
    },
    {
        "id": "A1-U108-027",
        "greek": "το πουλόβερ",
        "phonetic_hint": "to poo-LO-ver",
        "english": "sweater / jumper / pullover",
        "notes": "Klik A1 p. 165. Indeclinable neuter loan noun.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αυτό το μάλλινο πουλόβερ είναι πολύ μαλακό και ζεστό.",
        "example_en": "This wool sweater is very soft and warm.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πουλόβερ",
            "accusative_singular": "το πουλόβερ"
        },
        "keg_communicative_function": "Describing warm pullovers"
    },
    {
        "id": "A1-U108-028",
        "greek": "η φόρμα",
        "phonetic_hint": "ee FOR-mah",
        "english": "tracksuit / sweatpants",
        "notes": "Klik A1 p. 168. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Φοράω αθλητική φόρμα όταν πηγαίνω για τρέξιμο.",
        "example_en": "I wear a tracksuit when I go for a run.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι φόρμες",
            "accusative_singular": "τη φόρμα"
        },
        "keg_communicative_function": "Describing athletic sportswear"
    },
    {
        "id": "A1-U108-029",
        "greek": "οι πιτζάμες",
        "phonetic_hint": "ee pee-DZAH-mes",
        "english": "pajamas",
        "notes": "Klik A1 p. 167. Feminine noun used predominantly in plural.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βάζω τις πιτζάμες μου πριν πάω για ύπνο.",
        "example_en": "I put on my pajamas before going to sleep.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πιτζάμες",
            "accusative_singular": "τις πιτζάμες"
        },
        "keg_communicative_function": "Naming sleepwear"
    },
    {
        "id": "A1-U108-030",
        "greek": "το μαγιό",
        "phonetic_hint": "to mah-YO",
        "english": "swimsuit / bathing suit / trunks",
        "notes": "Klik A1 p. 165. Indeclinable neuter noun with stress on ultima.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Παίρνω το μαγιό μου και πάμε στην παραλία για μπάνιο.",
        "example_en": "I take my swimsuit and we go to the beach for a swim.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μαγιό",
            "accusative_singular": "το μαγιό"
        },
        "keg_communicative_function": "Naming swimwear"
    },

    # =========================================================================
    # 3. Footwear & Accessories (pp. 163, 165-168)
    # =========================================================================
    {
        "id": "A1-U108-031",
        "greek": "το παπούτσι",
        "phonetic_hint": "to pah-POOT-see",
        "english": "shoe",
        "notes": "Klik A1 p. 163, 166. Neuter noun in -ι with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αγοράζω ένα καινούργιο ζευγάρι παπούτσια για το σχολείο.",
        "example_en": "I buy a new pair of shoes for school.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα παπούτσια",
            "accusative_singular": "το παπούτσι"
        },
        "keg_communicative_function": "Selecting and purchasing footwear"
    },
    {
        "id": "A1-U108-032",
        "greek": "το ζευγάρι",
        "phonetic_hint": "to zev-GAH-ree",
        "english": "pair / couple",
        "notes": "Klik A1 p. 163, 172. Neuter noun in -ι with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Χρειάζομαι ένα ζευγάρι μαύρα παπούτσια και δύο ζευγάρια κάλτσες.",
        "example_en": "I need a pair of black shoes and two pairs of socks.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ζευγάρια",
            "accusative_singular": "το ζευγάρι"
        },
        "keg_communicative_function": "Quantifying items by the pair"
    },
    {
        "id": "A1-U108-033",
        "greek": "οι μπότες",
        "phonetic_hint": "ee BO-tes",
        "english": "boots",
        "notes": "Klik A1 p. 166. Feminine noun used predominantly in plural.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Φοράω δερμάτινες μπότες όταν βρέχει ή χιονίζει.",
        "example_en": "I wear leather boots when it rains or snows.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι μπότες",
            "accusative_singular": "τις μπότες"
        },
        "keg_communicative_function": "Describing winter boots"
    },
    {
        "id": "A1-U108-034",
        "greek": "τα πέδιλα",
        "phonetic_hint": "tah PEH-thee-lah",
        "english": "sandals / open summer shoes",
        "notes": "Klik A1 p. 165. Neuter noun used predominantly in plural.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το καλοκαίρι φοράμε ανοιχτά πέδιλα στη ζέστη.",
        "example_en": "In the summer we wear open sandals in the heat.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πέδιλα",
            "accusative_singular": "τα πέδιλα"
        },
        "keg_communicative_function": "Describing summer sandals"
    },
    {
        "id": "A1-U108-035",
        "greek": "οι σαγιονάρες",
        "phonetic_hint": "ee sah-yo-NAH-res",
        "english": "flip-flops / thong sandals",
        "notes": "Klik A1 p. 166. Feminine noun used predominantly in plural.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βάζω τις σαγιονάρες μου για να πάω στην παραλία.",
        "example_en": "I put on my flip-flops to go to the beach.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι σαγιονάρες",
            "accusative_singular": "τις σαγιονάρες"
        },
        "keg_communicative_function": "Describing beach footwear"
    },
    {
        "id": "A1-U108-036",
        "greek": "οι κάλτσες",
        "phonetic_hint": "ee KAHL-tses",
        "english": "socks",
        "notes": "Klik A1 p. 165. Feminine noun used predominantly in plural.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αγοράζω ζεστές μάλλινες κάλτσες για τον χειμώνα.",
        "example_en": "I buy warm wool socks for the winter.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι κάλτσες",
            "accusative_singular": "τις κάλτσες"
        },
        "keg_communicative_function": "Describing socks"
    },
    {
        "id": "A1-U108-037",
        "greek": "το καλσόν",
        "phonetic_hint": "to kahl-SON",
        "english": "tights / pantyhose",
        "notes": "Klik A1 p. 165. Indeclinable neuter loan noun.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Φοράει μαύρο καλσόν με τη φούστα της.",
        "example_en": "She wears black tights with her skirt.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα καλσόν",
            "accusative_singular": "το καλσόν"
        },
        "keg_communicative_function": "Naming hosiery and tights"
    },
    {
        "id": "A1-U108-038",
        "greek": "το καπέλο",
        "phonetic_hint": "to kah-PEH-lo",
        "english": "hat",
        "notes": "Klik A1 p. 165. Neuter noun in -ο with plural in -α.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Φοράω ψάθινο καπέλο στον ήλιο για προστασία.",
        "example_en": "I wear a straw hat in the sun for protection.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα καπέλα",
            "accusative_singular": "το καπέλο"
        },
        "keg_communicative_function": "Describing headwear"
    },
    {
        "id": "A1-U108-039",
        "greek": "ο σκούφος",
        "phonetic_hint": "o SKOO-fos",
        "english": "winter beanie / woolly hat",
        "notes": "Klik A1 p. 168. Masculine noun in -ος with plural in -οι.",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βάζει τον μάλλινο σκούφο του όταν κάνει πολύ κρύο.",
        "example_en": "He puts on his woolly beanie when it is very cold.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι σκούφοι",
            "accusative_singular": "τον σκούφο"
        },
        "keg_communicative_function": "Naming winter beanies"
    },
    {
        "id": "A1-U108-040",
        "greek": "τα γάντια",
        "phonetic_hint": "tah GAHN-dyah",
        "english": "gloves",
        "notes": "Klik A1 p. 165, 168. Neuter noun used predominantly in plural.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Φοράω δερμάτινα γάντια για να μην κρυώνουν τα χέρια μου.",
        "example_en": "I wear leather gloves so my hands don't get cold.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα γάντια",
            "accusative_singular": "τα γάντια"
        },
        "keg_communicative_function": "Describing hand protection and gloves"
    },
    {
        "id": "A1-U108-041",
        "greek": "το κασκόλ",
        "phonetic_hint": "to kah-SKOL",
        "english": "scarf / winter muffler",
        "notes": "Klik A1 p. 165. Indeclinable neuter loan noun.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τυλίγω το ζεστό κασκόλ γύρω από τον λαιμό μου.",
        "example_en": "I wrap the warm scarf around my neck.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κασκόλ",
            "accusative_singular": "το κασκόλ"
        },
        "keg_communicative_function": "Describing winter scarves"
    },
    {
        "id": "A1-U108-042",
        "greek": "η γραβάτα",
        "phonetic_hint": "ee grah-VAH-tah",
        "english": "necktie / tie",
        "notes": "Klik A1 p. 165. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Φοράει σκούρα μεταξωτή γραβάτα με το κοστούμι του.",
        "example_en": "He wears a dark silk necktie with his suit.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι γραβάτες",
            "accusative_singular": "τη γραβάτα"
        },
        "keg_communicative_function": "Describing neckties"
    },
    {
        "id": "A1-U108-043",
        "greek": "η ζώνη",
        "phonetic_hint": "ee ZO-nee",
        "english": "belt",
        "notes": "Klik A1 p. 165. Feminine noun in -η with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αυτή η δερμάτινη ζώνη ταιριάζει με το παντελόνι.",
        "example_en": "This leather belt matches the trousers.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ζώνες",
            "accusative_singular": "τη ζώνη"
        },
        "keg_communicative_function": "Describing clothing belts"
    },
    {
        "id": "A1-U108-044",
        "greek": "η τσάντα",
        "phonetic_hint": "ee TSAHN-dah",
        "english": "bag / handbag",
        "notes": "Klik A1 p. 166. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κρατάει μια κομψή καφέ δερμάτινη τσάντα.",
        "example_en": "She holds an elegant brown leather handbag.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι τσάντες",
            "accusative_singular": "την τσάντα"
        },
        "keg_communicative_function": "Describing handbags and accessory bags"
    },
    {
        "id": "A1-U108-045",
        "greek": "η ομπρέλα",
        "phonetic_hint": "ee om-BREH-lah",
        "english": "umbrella",
        "notes": "Klik A1 p. 165. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πάρε την ομπρέλα μαζί σου γιατί θα βρέξει.",
        "example_en": "Take the umbrella with you because it will rain.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ομπρέλες",
            "accusative_singular": "την ομπρέλα"
        },
        "keg_communicative_function": "Naming umbrellas for rain protection"
    },

    # =========================================================================
    # 4. Department Store & Retail Shopping (pp. 163-166)
    # =========================================================================
    {
        "id": "A1-U108-046",
        "greek": "το πολυκατάστημα",
        "phonetic_hint": "to po-lee-kah-TAH-stee-mah",
        "english": "department store",
        "notes": "Klik A1 p. 165. Compound neuter noun: πολύ + κατάστημα.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Στο πολυκατάστημα βρίσκεις ρούχα, παπούτσια και καλλυντικά.",
        "example_en": "In the department store you find clothes, shoes, and cosmetics.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πολυκαταστήματα",
            "accusative_singular": "το πολυκατάστημα"
        },
        "keg_communicative_function": "Identifying department stores"
    },
    {
        "id": "A1-U108-047",
        "greek": "το μαγαζί",
        "phonetic_hint": "to mah-gah-ZEE",
        "english": "shop / store",
        "notes": "Klik A1 p. 165, 170. Neuter noun in -ί with plural in -ιά.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αυτό το μαγαζί έχει πολύ καλές τιμές και προσφορές.",
        "example_en": "This shop has very good prices and special offers.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μαγαζιά",
            "accusative_singular": "το μαγαζί"
        },
        "keg_communicative_function": "Naming retail shops"
    },
    {
        "id": "A1-U108-048",
        "greek": "η βιτρίνα",
        "phonetic_hint": "ee vee-TREE-nah",
        "english": "shop window / display window",
        "notes": "Klik A1 p. 168, 169. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κοιτάζω τα όμορφα ρούχα στη βιτρίνα του καταστήματος.",
        "example_en": "I look at the beautiful clothes in the shop window.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι βιτρίνες",
            "accusative_singular": "τη βιτρίνα"
        },
        "keg_communicative_function": "Window shopping and describing store displays"
    },
    {
        "id": "A1-U108-049",
        "greek": "το ταμείο",
        "phonetic_hint": "to tah-MEE-o",
        "english": "cash desk / cash register / checkout",
        "notes": "Klik A1 p. 164, 165. Neuter noun in -ιο with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πληρώνω τα ρούχα στο ταμείο με την κάρτα μου.",
        "example_en": "I pay for the clothes at the cash desk with my card.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ταμεία",
            "accusative_singular": "το ταμείο"
        },
        "keg_communicative_function": "Locating store checkouts and payment desks"
    },
    {
        "id": "A1-U108-050",
        "greek": "το δοκιμαστήριο",
        "phonetic_hint": "to tho-kee-mah-STEE-ree-o",
        "english": "fitting room / changing room",
        "notes": "Klik A1 p. 163, 164. Neuter noun in -ιο with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πού είναι το δοκιμαστήριο για να δοκιμάσω αυτό το φόρεμα;",
        "example_en": "Where is the fitting room so I can try on this dress?",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα δοκιμαστήρια",
            "accusative_singular": "το δοκιμαστήριο"
        },
        "keg_communicative_function": "Locating fitting rooms in stores"
    },
    {
        "id": "A1-U108-051",
        "greek": "η έκπτωση",
        "phonetic_hint": "ee EHK-pto-see",
        "english": "discount / sale",
        "notes": "Klik A1 p. 163, 164. Feminine noun in -ση with plural in -σεις.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Στις χειμερινές εκπτώσεις βρίσκεις εξαιρετικές τιμές.",
        "example_en": "In the winter sales you find great prices.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι εκπτώσεις",
            "accusative_singular": "την έκπτωση"
        },
        "keg_communicative_function": "Inquiring about store discounts and seasonal sales"
    },
    {
        "id": "A1-U108-052",
        "greek": "η απόδειξη",
        "phonetic_hint": "ee ah-PO-theek-see",
        "english": "receipt",
        "notes": "Klik A1 p. 164. Feminine noun in -ξη with plural in -ξεις.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κρατήστε την απόδειξη σε περίπτωση που θέλετε αλλαγή.",
        "example_en": "Keep the receipt in case you want an exchange.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι αποδείξεις",
            "accusative_singular": "την απόδειξη"
        },
        "keg_communicative_function": "Requesting and keeping retail receipts"
    },
    {
        "id": "A1-U108-053",
        "greek": "το νούμερο",
        "phonetic_hint": "to NOO-meh-ro",
        "english": "clothing or shoe size / number",
        "notes": "Klik A1 p. 163, 164. Neuter noun in -ο with plural in -α.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τι νούμερο παπούτσι φοράτε; — Φοράω το τριάντα οκτώ.",
        "example_en": "What shoe size do you wear? — I wear size thirty-eight.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα νούμερα",
            "accusative_singular": "το νούμερο"
        },
        "keg_communicative_function": "Specifying shoe and apparel sizes"
    },
    {
        "id": "A1-U108-054",
        "greek": "το μέγεθος",
        "phonetic_hint": "to MEH-yeh-thos",
        "english": "size",
        "notes": "Klik A1 p. 164. Neuter noun in -ος with plural in -η.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αυτό το πουκάμισο είναι σε μεγάλο μέγεθος.",
        "example_en": "This shirt is in a large size.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μεγέθη",
            "accusative_singular": "το μέγεθος"
        },
        "keg_communicative_function": "Describing size specifications"
    },
    {
        "id": "A1-U108-055",
        "greek": "τα μετρητά",
        "phonetic_hint": "tah meh-tree-TAH",
        "english": "cash",
        "notes": "Klik A1 p. 164. Neuter adjective used as plural noun (πληρωμή σε μετρητά).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Δεν έχω κάρτα μαζί μου, θα πληρώσω με μετρητά.",
        "example_en": "I don't have a card with me, I will pay with cash.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μετρητά",
            "accusative_singular": "τα μετρητά"
        },
        "keg_communicative_function": "Selecting cash payment"
    },
    {
        "id": "A1-U108-056",
        "greek": "η κάρτα",
        "phonetic_hint": "ee KAHR-tah",
        "english": "credit / debit card",
        "notes": "Klik A1 p. 164. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Δέχεστε πιστωτική κάρτα στο ταμείο;",
        "example_en": "Do you accept credit cards at the checkout?",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι κάρτες",
            "accusative_singular": "την κάρτα"
        },
        "keg_communicative_function": "Selecting card payment"
    },

    # =========================================================================
    # 5. Core Shopping Verbs & Demonstratives (pp. 155-157, 163-165, 169)
    # =========================================================================
    {
        "id": "A1-U108-057",
        "greek": "ψωνίζω",
        "phonetic_hint": "pso-NEE-zo",
        "english": "I shop / buy / make purchases",
        "notes": "Klik A1 p. 163. Type A regular verb. Future: θα ψωνίσω.",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μου αρέσει να ψωνίζω ρούχα όταν έχει εκπτώσεις.",
        "example_en": "I like to shop for clothes when there are sales.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A (active regular)",
            "third_person_singular": "ψωνίζει",
            "first_person_plural": "ψωνίζουμε"
        },
        "keg_communicative_function": "Describing shopping habits"
    },
    {
        "id": "A1-U108-058",
        "greek": "δοκιμάζω",
        "phonetic_hint": "tho-kee-MAH-zo",
        "english": "I try on / test / taste",
        "notes": "Klik A1 p. 163, 164. Type A regular verb. Future: θα δοκιμάσω.",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Δοκιμάζω το πουκάμισο πριν το αγοράσω.",
        "example_en": "I try on the shirt before buying it.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A (active regular)",
            "third_person_singular": "δοκιμάζει",
            "first_person_plural": "δοκιμάζουμε"
        },
        "keg_communicative_function": "Trying on apparel in stores"
    },
    {
        "id": "A1-U108-059",
        "greek": "ταιριάζω",
        "phonetic_hint": "teh-RYAH-zo",
        "english": "I match / fit / suit",
        "notes": "Klik A1 p. 166. Type A regular verb. Often used impersonally: ταιριάζει με...",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αυτή η μπλούζα ταιριάζει πολύ ωραία με το τζιν σου.",
        "example_en": "This top matches your jeans very nicely.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A (active regular)",
            "third_person_singular": "ταιριάζει",
            "first_person_plural": "ταιριάζουμε"
        },
        "keg_communicative_function": "Evaluating aesthetic color and outfit matching"
    },
    {
        "id": "A1-U108-060",
        "greek": "φοράω",
        "phonetic_hint": "fo-RAH-o",
        "english": "I wear",
        "notes": "Klik A1 p. 163, 165, 167. Type B1 contract verb (-άω / -ώ). Future: θα φορέσω.",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τι φοράς όταν βγαίνεις έξω το βράδυ;",
        "example_en": "What do you wear when you go out in the evening?",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type B1 (contract)",
            "third_person_singular": "φοράει",
            "first_person_plural": "φοράμε"
        },
        "keg_communicative_function": "Stating what clothes someone wears"
    },
    {
        "id": "A1-U108-061",
        "greek": "στολίζω",
        "phonetic_hint": "sto-LEE-zo",
        "english": "I decorate / trim / garnish",
        "notes": "Klik A1 p. 155, 156. Type A regular verb. Future: θα στολίσω.",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Στολίζουμε το σπίτι για τις γιορτές των Χριστουγέννων.",
        "example_en": "We decorate the house for the Christmas holidays.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A (active regular)",
            "third_person_singular": "στολίζει",
            "first_person_plural": "στολίζουμε"
        },
        "keg_communicative_function": "Describing holiday home decorating"
    },
    {
        "id": "A1-U108-062",
        "greek": "γιορτάζω",
        "phonetic_hint": "yor-TAH-zo",
        "english": "I celebrate",
        "notes": "Klik A1 p. 155, 157. Type A regular verb. Future: θα γιορτάσω.",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Γιορτάζω τα γενέθλιά μου μαζί με τους καλούς μου φίλους.",
        "example_en": "I celebrate my birthday together with my good friends.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A (active regular)",
            "third_person_singular": "γιορτάζει",
            "first_person_plural": "γιορτάζουμε"
        },
        "keg_communicative_function": "Talking about celebrating personal milestones"
    },
    {
        "id": "A1-U108-063",
        "greek": "καλώ",
        "phonetic_hint": "kah-LO",
        "english": "I invite / call",
        "notes": "Klik A1 p. 170. Type B2 contract verb (-ώ, -είς, -εί). Future: θα καλέσω.",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Καλώ όλους τους συμφοιτητές μου στο πάρτι.",
        "example_en": "I invite all my fellow students to the party.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type B2 (contract)",
            "third_person_singular": "καλεί",
            "first_person_plural": "καλούμε"
        },
        "keg_communicative_function": "Inviting guests to events"
    },
    {
        "id": "A1-U108-064",
        "greek": "εκείνος",
        "phonetic_hint": "eh-KEE-nos",
        "english": "that / that one over there",
        "notes": "Klik A1 p. 169. Demonstrative pronoun pointing to distant items: εκείνος, εκείνη, εκείνο.",
        "gender_or_pos": "pronoun",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μου αρέσει εκείνο το παλτό που είναι στη βιτρίνα.",
        "example_en": "I like that coat over there that is in the shop window.",
        "grammatical_info": {
            "part_of_speech": "pronoun (demonstrative)",
            "forms": "εκείνος, εκείνη, εκείνο"
        },
        "keg_communicative_function": "Pointing out distant items and demonstrative reference"
    }
]

lesson_u108 = {
    "unit_id": "unit-108",
    "lesson_id": "lesson-01",
    "title": "Ενότητα 7: Γιορτές! Ώρα για ψώνια — Βασικό Λεξιλόγιο (Pages 151-174)",
    "description": "CEFR A1: Holidays and festive celebrations (Christmas, New Year, Easter, birthdays, name days), clothing items, footwear, accessories, department store retail vocabulary, and shopping verbs from Klik A1 (Pages 151-174).",
    "lesson_status": "not_started",
    "lesson_notes": (
        "Κλικ στα Ελληνικά Α1 — Ενότητα 7: Γιορτές! Ώρα για ψώνια (Σελίδες 151-174):\n"
        "• Γιορτές & Εκδηλώσεις (Holidays & Celebrations):\n"
        "  - η γιορτή, τα Χριστούγεννα, η Πρωτοχρονιά, το Πάσχα, τα γενέθλια, η ονομαστική γιορτή.\n"
        "  - το πάρτι, η πρόσκληση, το δώρο, το στολίδι, το χριστουγεννιάτικο δέντρο, τα φωτάκια.\n"
        "• Ρούχα & Ενδύματα (Clothes & Garments):\n"
        "  - τα ψώνια, το ρούχο, το φόρεμα, η φούστα, το παντελόνι, το τζιν, το πουκάμισο.\n"
        "  - το μπλουζάκι, η μπλούζα, το κοστούμι, το σακάκι, το παλτό, το μπουφάν, η ζακέτα.\n"
        "  - το πουλόβερ, η φόρμα, οι πιτζάμες, το μαγιό.\n"
        "• Υποδήματα & Αξεσουάρ (Footwear & Accessories):\n"
        "  - το παπούτσι, το ζευγάρι, οι μπότες, τα πέδιλα, οι σαγιονάρες, οι κάλτσες, το καλσόν.\n"
        "  - το καπέλο, ο σκούφος, τα γάντια, το κασκόλ, η γραβάτα, η ζώνη, η τσάντα, η ομπρέλα.\n"
        "• Στο Κατάστημα & Αγορές (Department Store & Retail):\n"
        "  - το πολυκατάστημα, το μαγαζί, η βιτρίνα, το ταμείο, το δοκιμαστήριο.\n"
        "  - η έκπτωση, η απόδειξη, το νούμερο, το μέγεθος, τα μετρητά, η κάρτα.\n"
        "• Ρήματα & Αντωνυμίες (Core Verbs & Demonstratives):\n"
        "  - ψωνίζω, δοκιμάζω, ταιριάζω, φοράω, στολίζω, γιορτάζω, καλώ.\n"
        "  - εκείνος, εκείνη, εκείνο."
    ),
    "entries": cards_u108
}

def main():
    print(f"Writing {len(cards_u108)} cards to {YAML_PATH}...")
    with open(YAML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(lesson_u108, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("YAML successfully written.")

    # Update manifest.yaml
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    units = manifest.get("units", [])
    existing = next((u for u in units if u.get("id") == "unit-108"), None)
    unit_108_entry = {
        "id": "unit-108",
        "title": "Κλικ στα Ελληνικά Α1: Σελίδες 151-174 (Ενότητα 7: Γιορτές! Ώρα για ψώνια - Λεξιλόγιο)",
        "order": "KlikA1-08-A",
        "lessons": [
            {
                "id": "lesson-01",
                "file": "unit-108/lesson-01.yaml",
                "title": "Ενότητα 7: Γιορτές! Ώρα για ψώνια — Βασικό Λεξιλόγιο (Pages 151-174)"
            }
        ]
    }

    if existing:
        print("Updating existing unit-108 in manifest.yaml...")
        idx = units.index(existing)
        units[idx] = unit_108_entry
    else:
        print("Appending unit-108 to manifest.yaml...")
        units.append(unit_108_entry)

    manifest["units"] = units

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("Manifest successfully updated with unit-108!")

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Script to create Unit 103 from Klik A1 (Pages 55-68):
Ενότητα 2: Πού μένεις; - Κατοικία, Πόλεις & Αριθμοί
Strictly conforming to docs/LESSON_CREATION_GUIDE.md and the klik-a1-deck-builder skill.
"""
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
UNIT_DIR = CONTENT_DIR / "unit-103"
UNIT_DIR.mkdir(parents=True, exist_ok=True)
YAML_PATH = UNIT_DIR / "lesson-01.yaml"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

cards_u103 = [
    # --- Asking & Telling Residence & Origin (pp. 55-58, 67) ---
    {
        "id": "A1-U103-001",
        "greek": "Πού μένεις;",
        "phonetic_hint": "poo MEH-nees",
        "english": "Where do you live? (informal)",
        "notes": "Klik A1 p. 55 (Unit title). Core question inquiring about residence using μένω.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πού μένεις τώρα; — Μένω στην Αθήνα.",
        "example_en": "— Where do you live now? — I live in Athens.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking someone where they live"
    },
    {
        "id": "A1-U103-002",
        "greek": "Πού μένετε;",
        "phonetic_hint": "poo MEH-neh-teh",
        "english": "Where do you live? (formal or plural)",
        "notes": "Klik A1 p. 55, 62. Polite/plural form of 'πού μένεις'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Καλησπέρα σας, πού μένετε στην Ελλάδα;",
        "example_en": "Good evening, where do you live in Greece?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking for address or residence formally"
    },
    {
        "id": "A1-U103-003",
        "greek": "Από πού είσαι;",
        "phonetic_hint": "ah-PO poo EE-seh",
        "english": "Where are you from? (informal)",
        "notes": "Klik A1 p. 56, 63. Core question inquiring about hometown, region, or nationality.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Από πού είσαι; — Είμαι από τη Θεσσαλονίκη.",
        "example_en": "— Where are you from? — I am from Thessaloniki.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about someone's geographical origin"
    },
    {
        "id": "A1-U103-004",
        "greek": "Από πού είστε;",
        "phonetic_hint": "ah-PO poo EES-teh",
        "english": "Where are you from? (formal or plural)",
        "notes": "Klik A1 p. 56. Formal or plural question of origin.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Χαίρετε, από πού είστε;",
        "example_en": "Greetings, where are you from?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking about someone's origin politely"
    },
    {
        "id": "A1-U103-005",
        "greek": "Σε ποια πόλη μένεις;",
        "phonetic_hint": "seh PYAH POH-lee MEH-nees",
        "english": "In which city do you live?",
        "notes": "Klik A1 p. 55. Preposition σε + interrogative ποια + feminine noun πόλη.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Σε ποια πόλη μένεις στην Ιταλία;",
        "example_en": "In which city do you live in Italy?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Specifying city of residence"
    },
    {
        "id": "A1-U103-006",
        "greek": "Σε ποια χώρα μένεις;",
        "phonetic_hint": "seh PYAH KHOH-rah MEH-nees",
        "english": "In which country do you live?",
        "notes": "Klik A1 p. 55. Inquiring about country of residence.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Σε ποια χώρα μένεις τώρα;",
        "example_en": "In which country do you live now?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Specifying country of residence"
    },
    {
        "id": "A1-U103-007",
        "greek": "στο κέντρο",
        "phonetic_hint": "stoh KEN-dro",
        "english": "in the city center / downtown",
        "notes": "Klik A1 p. 58, 62, 67. Prepositional phrase: σε + το κέντρο = στο κέντρο.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μένω στο κέντρο της πόλης, κοντά στην πλατεία.",
        "example_en": "I live in the city center, near the square.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Locating an apartment in the downtown area"
    },
    {
        "id": "A1-U103-008",
        "greek": "Δεν καταλαβαίνω.",
        "phonetic_hint": "then kah-tah-lah-VEH-no",
        "english": "I do not understand.",
        "notes": "Klik A1 p. 56. Essential communication survival phrase. Negation δεν + καταλαβαίνω.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Συγγνώμη, δεν καταλαβαίνω, μιλάτε πιο αργά;",
        "example_en": "Excuse me, I don't understand, could you speak more slowly?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Signaling lack of comprehension"
    },
    {
        "id": "A1-U103-009",
        "greek": "Τι σημαίνει;",
        "phonetic_hint": "tee see-MEH-nee",
        "english": "What does it mean?",
        "notes": "Klik A1 p. 56. Essential language learning query.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τι σημαίνει αυτή η λέξη στα ελληνικά;",
        "example_en": "What does this word mean in Greek?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking for clarification of a word's meaning"
    },

    # --- Contact Details & Personal Info (pp. 56, 57, 68) ---
    {
        "id": "A1-U103-010",
        "greek": "η διεύθυνση",
        "phonetic_hint": "ee thee-EF-theen-see",
        "english": "address (street address)",
        "notes": "Klik A1 p. 56, 57. Feminine in -ση (plural: οι διευθύνσεις).",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ποια είναι η διεύθυνση του σπιτιού σου;",
        "example_en": "What is your home address?",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι διευθύνσεις",
            "accusative_singular": "τη διεύθυνση"
        },
        "keg_communicative_function": "Inquiring about or filling out an address"
    },
    {
        "id": "A1-U103-011",
        "greek": "η οδός",
        "phonetic_hint": "ee o-THOS",
        "english": "street / road",
        "notes": "Klik A1 p. 56, 57. Classical feminine in -ος: η οδός, της οδού, οι οδοί.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μένω στην οδό Ερμού, στον αριθμό δέκα.",
        "example_en": "I live on Ermou Street, at number ten.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι οδοί",
            "accusative_singular": "την οδό"
        },
        "keg_communicative_function": "Naming a specific street in addresses"
    },
    {
        "id": "A1-U103-012",
        "greek": "ο αριθμός",
        "phonetic_hint": "o ah-reeth-MOS",
        "english": "number / street number",
        "notes": "Klik A1 p. 56, 57. Masculine in -ός (plural: οι αριθμοί).",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ποιος είναι ο αριθμός του τηλεφώνου σου;",
        "example_en": "What is your telephone number?",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι αριθμοί",
            "accusative_singular": "τον αριθμό"
        },
        "keg_communicative_function": "Stating house numbers or phone digits"
    },
    {
        "id": "A1-U103-013",
        "greek": "η πόλη",
        "phonetic_hint": "ee POH-lee",
        "english": "city / town",
        "notes": "Klik A1 p. 55, 57. Feminine in -η with plural in -εις: οι πόλεις.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η Θεσσαλονίκη είναι μια όμορφη πόλη.",
        "example_en": "Thessaloniki is a beautiful city.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πόλεις",
            "accusative_singular": "την πόλη"
        },
        "keg_communicative_function": "Naming urban settlements"
    },
    {
        "id": "A1-U103-014",
        "greek": "η χώρα",
        "phonetic_hint": "ee KHOH-rah",
        "english": "country / nation",
        "notes": "Klik A1 p. 55, 57. Feminine noun in -α with plural in -ες (οι χώρες).",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η Ελλάδα είναι μια πανέμορφη χώρα.",
        "example_en": "Greece is a very beautiful country.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι χώρες",
            "accusative_singular": "τη χώρα"
        },
        "keg_communicative_function": "Discussing countries of the world"
    },
    {
        "id": "A1-U103-015",
        "greek": "ο ταχυδρομικός κώδικας",
        "phonetic_hint": "o tah-khee-throh-mee-KOS KOH-thee-kahs",
        "english": "postal code / ZIP code",
        "notes": "Klik A1 p. 56. Often abbreviated in Greek as Τ.Κ. (τα-κα).",
        "gender_or_pos": "noun phrase (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ποιος είναι ο ταχυδρομικός κώδικας της περιοχής;",
        "example_en": "What is the postal code of the area?",
        "grammatical_info": {
            "part_of_speech": "noun phrase (masculine)",
            "plural": "οι ταχυδρομικοί κώδικες",
            "accusative_singular": "τον ταχυδρομικό κώδικα"
        },
        "keg_communicative_function": "Providing postal address details"
    },
    {
        "id": "A1-U103-016",
        "greek": "το κινητό",
        "phonetic_hint": "to kee-nee-TOH",
        "english": "mobile phone / cell phone",
        "notes": "Klik A1 p. 57, 68. Short for 'το κινητό τηλέφωνο'. Starts with 69 in Greece.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το κινητό μου είναι 6977003456.",
        "example_en": "My cell phone number is 6977003456.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κινητά",
            "accusative_singular": "το κινητό"
        },
        "keg_communicative_function": "Exchanging mobile numbers"
    },

    # --- Cardinal Numbers 0 - 10 (p. 60) ---
    {
        "id": "A1-U103-017",
        "greek": "μηδέν",
        "phonetic_hint": "mee-THEN",
        "english": "zero (0)",
        "notes": "Klik A1 p. 60. Indeclinable cardinal numeral.",
        "gender_or_pos": "numeral",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η θερμοκρασία είναι στους μηδέν βαθμούς.",
        "example_en": "The temperature is at zero degrees.",
        "grammatical_info": {
            "part_of_speech": "cardinal numeral (indeclinable)"
        },
        "keg_communicative_function": "Reading numbers and digits"
    },
    {
        "id": "A1-U103-018",
        "greek": "ένας, μία, ένα",
        "phonetic_hint": "EH-nahs, MEE-ah, EH-nah",
        "english": "one (1 - m / f / n)",
        "notes": "Klik A1 p. 60. Declinable numeral for 1: ένας άντρας, μία γυναίκα, ένα παιδί.",
        "gender_or_pos": "numeral",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Θέλω έναν καφέ και ένα μπουκάλι νερό.",
        "example_en": "I want one coffee and one bottle of water.",
        "grammatical_info": {
            "part_of_speech": "cardinal numeral (declinable)",
            "masculine": "ένας",
            "feminine": "μία / μια",
            "neuter": "ένα"
        },
        "keg_communicative_function": "Counting and specifying single items"
    },
    {
        "id": "A1-U103-019",
        "greek": "δύο",
        "phonetic_hint": "THEE-o",
        "english": "two (2)",
        "notes": "Klik A1 p. 60. Indeclinable cardinal numeral for 2.",
        "gender_or_pos": "numeral",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Δύο εισιτήρια για το μετρό, παρακαλώ.",
        "example_en": "Two tickets for the metro, please.",
        "grammatical_info": {
            "part_of_speech": "cardinal numeral (indeclinable)"
        },
        "keg_communicative_function": "Counting items and ordering pairs"
    },
    {
        "id": "A1-U103-020",
        "greek": "τρία",
        "phonetic_hint": "TREE-ah",
        "english": "three (3)",
        "notes": "Klik A1 p. 60. Declinable numeral: τρεις (m/f), τρία (n).",
        "gender_or_pos": "numeral",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Έχω τρία αδέρφια στην Ελλάδα.",
        "example_en": "I have three siblings in Greece.",
        "grammatical_info": {
            "part_of_speech": "cardinal numeral",
            "masculine_feminine": "τρεις",
            "neuter": "τρία"
        },
        "keg_communicative_function": "Counting items"
    },
    {
        "id": "A1-U103-021",
        "greek": "τέσσερα",
        "phonetic_hint": "TES-seh-rah",
        "english": "four (4)",
        "notes": "Klik A1 p. 60. Declinable numeral: τέσσερις (m/f), τέσσερα (n).",
        "gender_or_pos": "numeral",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το τραπέζι είναι για τέσσερα άτομα.",
        "example_en": "The table is for four people.",
        "grammatical_info": {
            "part_of_speech": "cardinal numeral",
            "masculine_feminine": "τέσσερις",
            "neuter": "τέσσερα"
        },
        "keg_communicative_function": "Counting items and group sizes"
    },
    {
        "id": "A1-U103-022",
        "greek": "πέντε",
        "phonetic_hint": "PEN-deh",
        "english": "five (5)",
        "notes": "Klik A1 p. 60. Indeclinable cardinal numeral.",
        "gender_or_pos": "numeral",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το μάθημα τελειώνει στις πέντε το απόγευμα.",
        "example_en": "The lesson finishes at five in the afternoon.",
        "grammatical_info": {
            "part_of_speech": "cardinal numeral (indeclinable)"
        },
        "keg_communicative_function": "Counting items and stating time"
    },
    {
        "id": "A1-U103-023",
        "greek": "έξι",
        "phonetic_hint": "EK-see",
        "english": "six (6)",
        "notes": "Klik A1 p. 60. Indeclinable cardinal numeral.",
        "gender_or_pos": "numeral",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αγοράζω έξι αυγά από το σούπερ μάρκετ.",
        "example_en": "I buy six eggs from the supermarket.",
        "grammatical_info": {
            "part_of_speech": "cardinal numeral (indeclinable)"
        },
        "keg_communicative_function": "Counting items"
    },
    {
        "id": "A1-U103-024",
        "greek": "επτά",
        "phonetic_hint": "ep-TAH",
        "english": "seven (7)",
        "notes": "Klik A1 p. 60. Also spelled and pronounced 'εφτά'.",
        "gender_or_pos": "numeral",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η εβδομάδα έχει επτά ημέρες.",
        "example_en": "The week has seven days.",
        "grammatical_info": {
            "part_of_speech": "cardinal numeral (indeclinable)"
        },
        "keg_communicative_function": "Counting days and quantities"
    },
    {
        "id": "A1-U103-025",
        "greek": "οκτώ",
        "phonetic_hint": "ok-TOH",
        "english": "eight (8)",
        "notes": "Klik A1 p. 60. Also spelled and pronounced 'οχτώ'.",
        "gender_or_pos": "numeral",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ξυπνάω στις οκτώ το πρωί κάθε μέρα.",
        "example_en": "I wake up at eight in the morning every day.",
        "grammatical_info": {
            "part_of_speech": "cardinal numeral (indeclinable)"
        },
        "keg_communicative_function": "Stating quantities and clock hours"
    },
    {
        "id": "A1-U103-026",
        "greek": "εννέα",
        "phonetic_hint": "en-NEH-ah",
        "english": "nine (9)",
        "notes": "Klik A1 p. 60. Also colloquially 'εννιά'.",
        "gender_or_pos": "numeral",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το λεωφορείο περνάει στις εννέα.",
        "example_en": "The bus passes at nine.",
        "grammatical_info": {
            "part_of_speech": "cardinal numeral (indeclinable)"
        },
        "keg_communicative_function": "Reading digits and bus timetables"
    },
    {
        "id": "A1-U103-027",
        "greek": "δέκα",
        "phonetic_hint": "THEH-kah",
        "english": "ten (10)",
        "notes": "Klik A1 p. 60. Foundation of the decimal system.",
        "gender_or_pos": "numeral",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Στην τάξη είμαστε δέκα μαθητές.",
        "example_en": "In the classroom we are ten students.",
        "grammatical_info": {
            "part_of_speech": "cardinal numeral (indeclinable)"
        },
        "keg_communicative_function": "Counting up to ten"
    },
    {
        "id": "A1-U103-028",
        "greek": "Πόσο κάνει;",
        "phonetic_hint": "POH-soh KAH-nee",
        "english": "How much does it make? / How much is it?",
        "notes": "Klik A1 p. 60. Used for math calculations (2 + 2 = 4) and prices.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πόσο κάνει πέντε συν πέντε; — Κάνει δέκα.",
        "example_en": "— How much is five plus five? — It makes ten.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking arithmetic sums and costs"
    },

    # --- Spatial Prepositions & Adverbs (pp. 63, 64, 67) ---
    {
        "id": "A1-U103-029",
        "greek": "κοντά σε",
        "phonetic_hint": "kon-DAH seh",
        "english": "near to / close to",
        "notes": "Klik A1 p. 63, 67. Prepositional phrase: κοντά στο σπίτι, κοντά στην πλατεία.",
        "gender_or_pos": "preposition",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το σπίτι μου είναι κοντά στον σταθμό του μετρό.",
        "example_en": "My house is close to the metro station.",
        "grammatical_info": {
            "part_of_speech": "prepositional phrase"
        },
        "keg_communicative_function": "Expressing proximity in space"
    },
    {
        "id": "A1-U103-030",
        "greek": "μακριά από",
        "phonetic_hint": "mah-kree-AH ah-PO",
        "english": "far from",
        "notes": "Klik A1 p. 62, 67. Opposite of κοντά σε.",
        "gender_or_pos": "preposition",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το αεροδρόμιο είναι μακριά από το κέντρο.",
        "example_en": "The airport is far from the city center.",
        "grammatical_info": {
            "part_of_speech": "prepositional phrase"
        },
        "keg_communicative_function": "Expressing distance in space"
    },
    {
        "id": "A1-U103-031",
        "greek": "απέναντι από",
        "phonetic_hint": "ah-PEH-nahn-dee ah-PO",
        "english": "opposite / across from",
        "notes": "Klik A1 p. 63. Key spatial locator across a street or square.",
        "gender_or_pos": "preposition",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η καφετέρια είναι ακριβώς απέναντι από το μουσείο.",
        "example_en": "The cafe is directly across from the museum.",
        "grammatical_info": {
            "part_of_speech": "prepositional phrase"
        },
        "keg_communicative_function": "Locating places directly opposite each other"
    },
    {
        "id": "A1-U103-032",
        "greek": "δίπλα σε",
        "phonetic_hint": "THEEP-lah seh",
        "english": "next to / beside",
        "notes": "Klik A1 p. 63. Followed by accusative: δίπλα στο σπίτι, δίπλα στη στάση.",
        "gender_or_pos": "preposition",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η στάση του λεωφορείου είναι δίπλα στο φαρμακείο.",
        "example_en": "The bus stop is next to the pharmacy.",
        "grammatical_info": {
            "part_of_speech": "prepositional phrase"
        },
        "keg_communicative_function": "Describing adjacent locations"
    },
    {
        "id": "A1-U103-033",
        "greek": "μπροστά από",
        "phonetic_hint": "broh-STAH ah-PO",
        "english": "in front of",
        "notes": "Klik A1 p. 63. Spatial preposition phrase.",
        "gender_or_pos": "preposition",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το πάρκο είναι μπροστά από το νοσοκομείο.",
        "example_en": "The park is in front of the hospital.",
        "grammatical_info": {
            "part_of_speech": "prepositional phrase"
        },
        "keg_communicative_function": "Locating an object in front of another"
    },
    {
        "id": "A1-U103-034",
        "greek": "πίσω από",
        "phonetic_hint": "PEE-soh ah-PO",
        "english": "behind",
        "notes": "Klik A1 p. 63, 64. Opposite of μπροστά από.",
        "gender_or_pos": "preposition",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το γυμναστήριο είναι πίσω από το σχολείο.",
        "example_en": "The gym is behind the school.",
        "grammatical_info": {
            "part_of_speech": "prepositional phrase"
        },
        "keg_communicative_function": "Locating an object behind another"
    },
    {
        "id": "A1-U103-035",
        "greek": "πάνω σε",
        "phonetic_hint": "PAH-no seh",
        "english": "on / on top of",
        "notes": "Klik A1 p. 65. Followed by accusative: πάνω στο τραπέζι, πάνω στην πλατεία.",
        "gender_or_pos": "preposition",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το ξενοδοχείο είναι πάνω στην πλατεία Αριστοτέλους.",
        "example_en": "The hotel is right on Aristotelous Square.",
        "grammatical_info": {
            "part_of_speech": "prepositional phrase"
        },
        "keg_communicative_function": "Locating buildings situated directly on a street or square"
    },

    # --- Urban Places, Public Buildings & Transit (pp. 63-65, 67) ---
    {
        "id": "A1-U103-036",
        "greek": "το σπίτι",
        "phonetic_hint": "to SPEE-tee",
        "english": "house / home",
        "notes": "Klik A1 p. 63, 65, 67. Neuter in -ι (plural: τα σπίτια).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πάω στο σπίτι να ξεκουραστώ.",
        "example_en": "I am going home to rest.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα σπίτια",
            "accusative_singular": "το σπίτι"
        },
        "keg_communicative_function": "Describing one's home"
    },
    {
        "id": "A1-U103-037",
        "greek": "η πλατεία",
        "phonetic_hint": "ee plah-TEE-ah",
        "english": "square / town plaza",
        "notes": "Klik A1 p. 64, 65, 67. Feminine in -α (plural: οι πλατείες). Central meeting spot.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Συναντιόμαστε στην πλατεία Συντάγματος.",
        "example_en": "We are meeting at Syntagma Square.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πλατείες",
            "accusative_singular": "την πλατεία"
        },
        "keg_communicative_function": "Arranging a meeting point in town"
    },
    {
        "id": "A1-U103-038",
        "greek": "ο δρόμος",
        "phonetic_hint": "o THROH-mos",
        "english": "street / road",
        "notes": "Klik A1 p. 64. Common masculine noun for road or street (plural: οι δρόμοι).",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο δρόμος έχει πολλή κίνηση το πρωί.",
        "example_en": "The street has a lot of traffic in the morning.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι δρόμοι",
            "accusative_singular": "τον δρόμο"
        },
        "keg_communicative_function": "Describing streets and routes"
    },
    {
        "id": "A1-U103-039",
        "greek": "η στάση",
        "phonetic_hint": "ee STAH-see",
        "english": "stop (bus / tram stop)",
        "notes": "Klik A1 p. 63. Feminine in -ση: η στάση του λεωφορείου.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Περιμένω το λεωφορείο στη στάση.",
        "example_en": "I am waiting for the bus at the stop.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι στάσεις",
            "accusative_singular": "τη στάση"
        },
        "keg_communicative_function": "Using local public transport"
    },
    {
        "id": "A1-U103-040",
        "greek": "ο σταθμός",
        "phonetic_hint": "o stahth-MOS",
        "english": "station (train / metro / bus terminal)",
        "notes": "Klik A1 p. 64, 67. Oxytone masculine: ο σταθμός του τρένου / μετρό.",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο κεντρικός σταθμός είναι πολύ κοντά.",
        "example_en": "The central station is very close.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι σταθμοί",
            "accusative_singular": "τον σταθμό"
        },
        "keg_communicative_function": "Navigating transportation hubs"
    },
    {
        "id": "A1-U103-041",
        "greek": "το μετρό",
        "phonetic_hint": "to meh-TROH",
        "english": "metro / subway",
        "notes": "Klik A1 p. 63, 67. Neuter indeclinable loanword with oxytone stress.",
        "gender_or_pos": "noun (neuter indeclinable)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Παίρνω το μετρό για να πάω στο κέντρο.",
        "example_en": "I take the metro to go downtown.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter indeclinable)",
            "plural": "τα μετρό",
            "accusative_singular": "το μετρό"
        },
        "keg_communicative_function": "Using subway transport"
    },
    {
        "id": "A1-U103-042",
        "greek": "το ταχυδρομείο",
        "phonetic_hint": "to tah-khee-throh-MEE-o",
        "english": "post office",
        "notes": "Klik A1 p. 64, 65. Neuter noun in -είο (plural: τα ταχυδρομεία).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Στέλνω ένα δέμα από το ταχυδρομείο.",
        "example_en": "I send a parcel from the post office.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ταχυδρομεία",
            "accusative_singular": "το ταχυδρομείο"
        },
        "keg_communicative_function": "Visiting postal service branches"
    },
    {
        "id": "A1-U103-043",
        "greek": "το νοσοκομείο",
        "phonetic_hint": "to noh-soh-koh-MEE-o",
        "english": "hospital",
        "notes": "Klik A1 p. 63, 64, 65, 67. Neuter noun in -είο (plural: τα νοσοκομεία).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο γιατρός δουλεύει στο πανεπιστημιακό νοσοκομείο.",
        "example_en": "The doctor works at the university hospital.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα νοσοκομεία",
            "accusative_singular": "το νοσοκομείο"
        },
        "keg_communicative_function": "Locating healthcare facilities"
    },
    {
        "id": "A1-U103-044",
        "greek": "το φαρμακείο",
        "phonetic_hint": "to fahr-mah-KEE-o",
        "english": "pharmacy / chemist",
        "notes": "Klik A1 p. 67. Neuter in -είο (plural: τα φαρμακεία). Identified by a green cross.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αγοράζω παυσίπονα από το διπλανό φαρμακείο.",
        "example_en": "I buy painkillers from the neighboring pharmacy.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα φαρμακεία",
            "accusative_singular": "το φαρμακείο"
        },
        "keg_communicative_function": "Finding pharmacies and purchasing medicines"
    },
    {
        "id": "A1-U103-045",
        "greek": "το μουσείο",
        "phonetic_hint": "to moo-SEE-o",
        "english": "museum",
        "notes": "Klik A1 p. 63, 64, 65, 67. Neuter in -είο (plural: τα μουσεία).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Επισκεπτόμαστε το Μουσείο της Ακρόπολης.",
        "example_en": "We are visiting the Acropolis Museum.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μουσεία",
            "accusative_singular": "το μουσείο"
        },
        "keg_communicative_function": "Sightseeing and visiting cultural museums"
    },
    {
        "id": "A1-U103-046",
        "greek": "το ξενοδοχείο",
        "phonetic_hint": "to kseh-noh-thoh-KHEE-o",
        "english": "hotel",
        "notes": "Klik A1 p. 64, 65, 67. Neuter in -είο (plural: τα ξενοδοχεία).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μένουμε σε ένα καθαρό ξενοδοχείο κοντά στη θάλασσα.",
        "example_en": "We stay at a clean hotel near the sea.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ξενοδοχεία",
            "accusative_singular": "το ξενοδοχείο"
        },
        "keg_communicative_function": "Arranging hotel accommodation"
    },
    {
        "id": "A1-U103-047",
        "greek": "το γυμναστήριο",
        "phonetic_hint": "to yeem-nah-STEE-ree-o",
        "english": "gym / fitness center",
        "notes": "Klik A1 p. 63, 67. Neuter in -ιο (plural: τα γυμναστήρια).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πηγαίνω στο γυμναστήριο τρεις φορές την εβδομάδα.",
        "example_en": "I go to the gym three times a week.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα γυμναστήρια",
            "accusative_singular": "το γυμναστήριο"
        },
        "keg_communicative_function": "Discussing fitness and workout facilities"
    },
    {
        "id": "A1-U103-048",
        "greek": "η βιβλιοθήκη",
        "phonetic_hint": "ee veev-lee-oh-THEE-kee",
        "english": "library / bookcase",
        "notes": "Klik A1 p. 67. Feminine in -η (plural: οι βιβλιοθήκες).",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Διαβάζω ήσυχα στην πανεπιστημιακή βιβλιοθήκη.",
        "example_en": "I study quietly in the university library.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι βιβλιοθήκες",
            "accusative_singular": "τη βιβλιοθήκη"
        },
        "keg_communicative_function": "Locating study spaces and libraries"
    },
    {
        "id": "A1-U103-049",
        "greek": "η εκκλησία",
        "phonetic_hint": "ee ek-klee-SEE-ah",
        "english": "church",
        "notes": "Klik A1 p. 67. Feminine in -ία (plural: οι εκκλησίες). Prominent Greek urban landmark.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η παλιά εκκλησία είναι πάνω στον λόφο.",
        "example_en": "The old church is up on the hill.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι εκκλησίες",
            "accusative_singular": "την εκκλησία"
        },
        "keg_communicative_function": "Identifying cultural and religious landmarks"
    },
    {
        "id": "A1-U103-050",
        "greek": "η καφετέρια",
        "phonetic_hint": "ee kah-feh-TEH-ree-ah",
        "english": "cafeteria / cafe",
        "notes": "Klik A1 p. 62, 63, 65. Feminine in -ια (plural: οι καφετέριες).",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πίνουμε καφέ στην καφετέρια της πλατείας.",
        "example_en": "We drink coffee at the cafe on the square.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι καφετέριες",
            "accusative_singular": "την καφετέρια"
        },
        "keg_communicative_function": "Meeting friends for coffee"
    },

    # --- Core Present Tense Verbs (pp. 55, 62, 65, 66) ---
    {
        "id": "A1-U103-051",
        "greek": "μένω",
        "phonetic_hint": "MEH-no",
        "english": "to live / to reside / to stay",
        "notes": "Klik A1 p. 55, 66. Type A regular active verb: μένω, μένεις, μένει, μένουμε, μένετε, μένουν.",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μένω σε ένα φωτεινό διαμέρισμα στον τρίτο όροφο.",
        "example_en": "I live in a bright apartment on the third floor.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A (active regular)",
            "third_person_singular": "μένει",
            "first_person_plural": "μένουμε"
        },
        "keg_communicative_function": "Stating place of residence"
    },
    {
        "id": "A1-U103-052",
        "greek": "σπουδάζω",
        "phonetic_hint": "spoo-THAH-zo",
        "english": "to study (at university / college)",
        "notes": "Klik A1 p. 62, 65, 66. Type A active regular verb: σπουδάζω, σπουδάζεις, σπουδάζει.",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο αδερφός μου σπουδάζει ιατρική στην Κρήτη.",
        "example_en": "My brother studies medicine in Crete.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A (active regular)",
            "third_person_singular": "σπουδάζει",
            "first_person_plural": "σπουδάζουμε"
        },
        "keg_communicative_function": "Talking about university studies and majors"
    },
    {
        "id": "A1-U103-053",
        "greek": "αρχίζω",
        "phonetic_hint": "ahr-KHEE-zo",
        "english": "to begin / to start",
        "notes": "Klik A1 p. 66. Type A regular verb: αρχίζω, αρχίζεις, αρχίζει.",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Φέτος αρχίζω μαθήματα νέων ελληνικών.",
        "example_en": "This year I am starting Modern Greek lessons.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A (active regular)",
            "third_person_singular": "αρχίζει",
            "first_person_plural": "αρχίζουμε"
        },
        "keg_communicative_function": "Talking about commencement of activities"
    },
    {
        "id": "A1-U103-054",
        "greek": "πίνω",
        "phonetic_hint": "PEE-no",
        "english": "to drink",
        "notes": "Klik A1 p. 66. Type A regular verb: πίνω, πίνεις, πίνει, πίνουμε, πίνετε, πίνουν.",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πίνουμε έναν ελληνικό καφέ το πρωί.",
        "example_en": "We drink a Greek coffee in the morning.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A (active regular)",
            "third_person_singular": "πίνει",
            "first_person_plural": "πίνουμε"
        },
        "keg_communicative_function": "Ordering and describing beverage consumption"
    },
    {
        "id": "A1-U103-055",
        "greek": "κάνω",
        "phonetic_hint": "KAH-no",
        "english": "to do / to make",
        "notes": "Klik A1 p. 62, 66. High-frequency verb: κάνω ψώνια, κάνω μάθημα, τι κάνεις.",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τι κάνεις σήμερα το απόγευμα;",
        "example_en": "What are you doing this afternoon?",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A (active regular)",
            "third_person_singular": "κάνει",
            "first_person_plural": "κάνουμε"
        },
        "keg_communicative_function": "Asking and describing daily activities"
    },
    {
        "id": "A1-U103-056",
        "greek": "ξέρω",
        "phonetic_hint": "KSEH-ro",
        "english": "to know",
        "notes": "Klik A1 p. 67. Type A verb: ξέρω, ξέρεις, ξέρει. Practicing initial cluster ξ [ks].",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ξέρεις πού είναι το ταχυδρομείο;",
        "example_en": "Do you know where the post office is?",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A (active regular)",
            "third_person_singular": "ξέρει",
            "first_person_plural": "ξέρουμε"
        },
        "keg_communicative_function": "Asking for knowledge and directions"
    },
    {
        "id": "A1-U103-057",
        "greek": "καταλαβαίνω",
        "phonetic_hint": "kah-tah-lah-VEH-no",
        "english": "to understand / to comprehend",
        "notes": "Klik A1 p. 56. Type A regular verb: καταλαβαίνω, καταλαβαίνεις, καταλαβαίνει.",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Καταλαβαίνω ελληνικά αλλά μιλάω λίγο.",
        "example_en": "I understand Greek but I speak only a little.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A (active regular)",
            "third_person_singular": "καταλαβαίνει",
            "first_person_plural": "καταλαβαίνουμε"
        },
        "keg_communicative_function": "Expressing language comprehension ability"
    },

    # --- Family, Co-living & Social Situations (pp. 62, 65, 67) ---
    {
        "id": "A1-U103-058",
        "greek": "οι γονείς",
        "phonetic_hint": "ee goh-NEES",
        "english": "parents",
        "notes": "Klik A1 p. 62, 67. Masculine plural noun: οι γονείς (singular: ο γονέας).",
        "gender_or_pos": "noun (masculine plural)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μένω μαζί με τους γονείς μου στην Αθήνα.",
        "example_en": "I live together with my parents in Athens.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine plural)",
            "plural": "οι γονείς",
            "accusative_singular": "τον γονέα"
        },
        "keg_communicative_function": "Describing family living arrangements"
    },
    {
        "id": "A1-U103-059",
        "greek": "ο μπαμπάς",
        "phonetic_hint": "o bahm-BAHS",
        "english": "dad / father",
        "notes": "Klik A1 p. 62. Masculine in -άς (plural: οι μπαμπάδες). Informal family noun.",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο μπαμπάς μου δουλεύει ως μηχανικός.",
        "example_en": "My dad works as an engineer.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι μπαμπάδες",
            "accusative_singular": "τον μπαμπά"
        },
        "keg_communicative_function": "Talking about family members"
    },
    {
        "id": "A1-U103-060",
        "greek": "η μαμά",
        "phonetic_hint": "ee mah-MAH",
        "english": "mom / mother",
        "notes": "Klik A1 p. 62. Feminine in -ά (plural: οι μαμάδες). Informal family noun.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η μαμά μου είναι δασκάλα στο σχολείο.",
        "example_en": "My mom is a teacher at the school.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι μαμάδες",
            "accusative_singular": "τη μαμά"
        },
        "keg_communicative_function": "Talking about family members"
    },
    {
        "id": "A1-U103-061",
        "greek": "ο φοιτητής",
        "phonetic_hint": "o fee-tee-TEES",
        "english": "university student (male)",
        "notes": "Klik A1 p. 65. Masculine oxytone in -ής (plural: οι φοιτητές).",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο φοιτητής διαβάζει στη βιβλιοθήκη του πανεπιστημίου.",
        "example_en": "The university student is studying in the university library.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι φοιτητές",
            "accusative_singular": "τον φοιτητή"
        },
        "keg_communicative_function": "Describing academic occupation"
    },
    {
        "id": "A1-U103-062",
        "greek": "η φοιτήτρια",
        "phonetic_hint": "ee fee-TEE-tree-ah",
        "english": "university student (female)",
        "notes": "Klik A1 p. 65. Feminine noun in -τρια (plural: οι φοιτήτριες).",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η Ελένη είναι φοιτήτρια νομικής.",
        "example_en": "Eleni is a law student.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι φοιτήτριες",
            "accusative_singular": "τη φοιτήτρια"
        },
        "keg_communicative_function": "Describing academic occupation"
    }
]

lesson_u103 = {
    "unit_id": "unit-103",
    "lesson_id": "lesson-01",
    "title": "Ενότητα 2: Πού μένεις; — Πόλεις, Διευθύνσεις, Αριθμοί 0-10 & Προθέσεις (Pages 55-68)",
    "description": "CEFR A1: Talking about place of residence and origin, filling out contact forms, cardinal numbers 0-10, spatial prepositions, urban landmarks, and core Type A verbs from Klik A1 (pages 55-68).",
    "lesson_status": "not_started",
    "lesson_notes": """Κλικ στα Ελληνικά Α1 — Ενότητα 2: Πού μένεις; (Σελίδες 55-68):
• Κατοικία & Καταγωγή (Residence & Origin):
  - «Πού μένεις;» → «Μένω στην Αθήνα, στην οδό Ερμού 10.»
  - «Από πού είσαι;» → «Είμαι από τη Θεσσαλονίκη / από τον Βόλο.»
• Πτώσεις με προθέσεις (Accusative with Prepositions):
  - σε + αιτιατική (στο / στη / στον / στην):
    • στον Βόλο (αρσενικό)
    • στη(ν) Αθήνα / Θεσσαλονίκη (θηλυκό)
    • στο κέντρο / σπίτι (ουδέτερο)
  - από + αιτιατική (από τον / από τη / από το):
    • από τον Βόλο, από τη Θεσσαλονίκη, από το Παγκράτι
• Αριθμοί 0 - 10 (Cardinal Numbers):
  - 0: μηδέν, 1: ένας/μία/ένα, 2: δύο, 3: τρεις/τρία, 4: τέσσερις/τέσσερα,
  - 5: πέντε, 6: έξι, 7: επτά (εφτά), 8: οκτώ (οχτώ), 9: εννέα (εννιά), 10: δέκα.
• Τοπικοί προσδιορισμοί & Προθέσεις χώρου (Spatial Expressions):
  - κοντά σε (near to) ↔ μακριά από (far from)
  - απέναντι από (across from / opposite)
  - δίπλα σε (next to / beside)
  - μπροστά από (in front of) ↔ πίσω από (behind)
  - πάνω σε (on / on top of)
• Βασικά Ρήματα Α' Συζυγίας (Type A Verbs in Present Tense):
  - μένω, σπουδάζω, αρχίζω, πίνω, κάνω, ξέρω, καταλαβαίνω.""",
    "entries": cards_u103
}

def main():
    print(f"Writing {len(cards_u103)} cards to {YAML_PATH}...")
    with open(YAML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(lesson_u103, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("YAML successfully written.")

    # Update manifest.yaml
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    units = manifest.get("units", [])
    existing = next((u for u in units if u.get("id") == "unit-103"), None)
    unit_103_entry = {
        "id": "unit-103",
        "title": "Κλικ στα Ελληνικά Α1: Σελίδες 55-68 (Ενότητα 2: Πού μένεις; - Κατοικία, Πόλεις & Αριθμοί)",
        "order": 103,
        "lessons": [
            {
                "id": "lesson-01",
                "file": "unit-103/lesson-01.yaml",
                "title": "Ενότητα 2: Πού μένεις; — Πόλεις, Διευθύνσεις, Αριθμοί 0-10 & Προθέσεις (Pages 55-68)"
            }
        ]
    }

    if existing:
        print("Updating existing unit-103 in manifest.yaml...")
        idx = units.index(existing)
        units[idx] = unit_103_entry
    else:
        print("Appending unit-103 to manifest.yaml...")
        units.append(unit_103_entry)

    manifest["units"] = units

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("Manifest successfully updated with unit-103!")

if __name__ == "__main__":
    main()

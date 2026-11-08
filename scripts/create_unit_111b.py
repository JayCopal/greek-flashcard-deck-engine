# -*- coding: utf-8 -*-
"""
Script to create Unit 111b from Klik A1 (Pages 219-232):
Ενότητα 10: Περαστικά! - Γραμματική & Εκφράσεις
Strictly conforming to docs/LESSON_CREATION_GUIDE.md and the klik-a1-deck-builder skill.
Covers the invariant relative pronoun 'που', interrogatives (ποιος/ποιανού/σε ποιον),
emphatic possessive pronouns (ο δικός μου, κλπ.), pain constructions (πονάει/πονάνε),
doctor consultations, pharmacy interactions, and health recovery wishes.
"""
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
UNIT_DIR = CONTENT_DIR / "unit-111b"
UNIT_DIR.mkdir(parents=True, exist_ok=True)
YAML_PATH = UNIT_DIR / "lesson-01.yaml"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

cards_u111b = [
    # =========================================================================
    # 1. The Invariant Relative Pronoun 'που' (pp. 222-223, 226)
    # =========================================================================
    {
        "id": "A1-U111B-001",
        "greek": "Ξέρω έναν γιατρό που είναι πολύ καλός.",
        "phonetic_hint": "KSEH-ro EH-nan yee-ah-TRO poo EE-neh po-LEE kah-LOS",
        "english": "I know a doctor who is very good.",
        "notes": "Klik A1 p. 222. The invariant relative pronoun 'που' connects clauses without repeating the masculine noun in the nominative.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ξέρω έναν γιατρό που είναι πολύ καλός στα καρδιολογικά θέματα.",
        "example_en": "I know a doctor who is very good with cardiological issues.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Using relative clauses to specify people"
    },
    {
        "id": "A1-U111B-002",
        "greek": "Πήρα ένα φάρμακο που με βοήθησε αμέσως.",
        "phonetic_hint": "PEE-rah EH-nah FAHR-mah-ko poo meh vo-EE-thee-seh ah-MEH-sos",
        "english": "I took a medicine that helped me immediately.",
        "notes": "Klik A1 p. 222. The invariant relative pronoun 'που' replaces a neuter noun as subject in the relative clause.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πήρα ένα φάρμακο που με βοήθησε αμέσως να κοιμηθώ.",
        "example_en": "I took a medicine that helped me immediately to fall asleep.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing remedies with relative clauses"
    },
    {
        "id": "A1-U111B-003",
        "greek": "Η γυναίκα που μιλάει με τον γιατρό είναι η μητέρα μου.",
        "phonetic_hint": "ee yee-NEH-kah poo mee-LAH-ee meh ton yee-ah-TRO EE-neh ee mee-TEH-rah moo",
        "english": "The woman who is speaking with the doctor is my mother.",
        "notes": "Klik A1 p. 222. 'Που' acts as an invariant relative pronoun replacing a feminine singular subject.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η γυναίκα που μιλάει με τον γιατρό είναι η μητέρα μου και περιμένει τα αποτελέσματα.",
        "example_en": "The woman who is speaking with the doctor is my mother and is waiting for the results.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Identifying individuals using relative clauses"
    },
    {
        "id": "A1-U111B-004",
        "greek": "Το σιρόπι που μου έδωσε ο φαρμακοποιός έχει ωραία γεύση.",
        "phonetic_hint": "to see-RO-pee poo moo EH-dho-seh o fahr-mah-ko-pee-OS EH-khee o-REH-ah YEV-see",
        "english": "The syrup that the pharmacist gave me has a pleasant taste.",
        "notes": "Klik A1 p. 222. 'Που' functions as direct object in the relative clause without needing inflection.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το σιρόπι που μου έδωσε ο φαρμακοποιός έχει ωραία γεύση πορτοκάλι.",
        "example_en": "The syrup that the pharmacist gave me has a nice orange flavor.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing medical products using relative clauses"
    },
    {
        "id": "A1-U111B-005",
        "greek": "Οι ασθενείς που περιμένουν έχουν ραντεβού;",
        "phonetic_hint": "ee ah-stheh-NEES poo peh-ree-MEH-noon EH-khoon rahn-deh-VOO",
        "english": "Do the patients who are waiting have an appointment?",
        "notes": "Klik A1 p. 222. Relative pronoun 'που' modifying a plural masculine subject.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Οι ασθενείς που περιμένουν στην αίθουσα έχουν ραντεβού για εξετάσεις.",
        "example_en": "The patients who are waiting in the room have an appointment for examinations.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking about clinical waiting lists with relative clauses"
    },
    {
        "id": "A1-U111B-006",
        "greek": "Πού είναι τα χάπια που αγόρασες χθες από το φαρμακείο;",
        "phonetic_hint": "poo EE-neh tah KHAH-pyah poo ah-YO-rah-ses khthes ah-PO to fahr-mah-KEE-o",
        "english": "Where are the pills that you bought yesterday from the pharmacy?",
        "notes": "Klik A1 p. 222-223. Contrasting accented interrogative adverb 'πού' (where) with unaccented relative pronoun 'που' (that/which).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πού είναι τα χάπια που αγόρασες χθες από το φαρμακείο για τον πυρετό;",
        "example_en": "Where are the pills that you bought yesterday from the pharmacy for fever?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about medicine location using 'πού' and 'που'"
    },
    {
        "id": "A1-U111B-007",
        "greek": "Ο γιατρός που με εξέτασε ήταν πολύ προσεκτικός.",
        "phonetic_hint": "o yee-ah-TROS poo meh ek-SEH-tah-seh EE-tan po-LEE pro-sek-tee-KOS",
        "english": "The doctor who examined me was very thorough.",
        "notes": "Klik A1 p. 222, 226. Demonstrating 'που' followed by weak object pronoun and past tense verb.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο γιατρός που με εξέτασε ήταν πολύ προσεκτικός και μου εξήγησε τα πάντα.",
        "example_en": "The doctor who examined me was very thorough and explained everything to me.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Evaluating healthcare professionals"
    },
    {
        "id": "A1-U111B-008",
        "greek": "Το νοσοκομείο που πήγε ο Νίκος είναι στο κέντρο.",
        "phonetic_hint": "to no-so-ko-MEE-o poo PEE-yeh o NEE-kos EE-neh sto KEN-dro",
        "english": "The hospital that Nikos went to is in the city center.",
        "notes": "Klik A1 p. 222. Invariant 'που' standing for place destination in informal speech.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το νοσοκομείο που πήγε ο Νίκος είναι στο κέντρο της Αθήνας.",
        "example_en": "The hospital that Nikos went to is in the center of Athens.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Locating medical facilities"
    },

    # =========================================================================
    # 2. Interrogative Pronouns: ποιος, ποιανού, σε ποιον, ποιον (pp. 222-224)
    # =========================================================================
    {
        "id": "A1-U111B-009",
        "greek": "Ποιος είναι άρρωστος και δεν μπορεί να έρθει σήμερα;",
        "phonetic_hint": "pyos EE-neh AH-ro-stos keh dhen bo-REE nah ER-thee SEE-meh-rah",
        "english": "Who is sick and cannot come today?",
        "notes": "Klik A1 p. 222. Masculine singular nominative interrogative pronoun 'ποιος'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ποιος είναι άρρωστος και δεν μπορεί να έρθει σήμερα στη δουλειά;",
        "example_en": "Who is sick and cannot come to work today?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring who is unwell"
    },
    {
        "id": "A1-U111B-010",
        "greek": "Ποια είναι η γιατρός σας στο νοσοκομείο;",
        "phonetic_hint": "pyah EE-neh ee yee-ah-TROS sahs sto no-so-ko-MEE-o",
        "english": "Who is your doctor at the hospital?",
        "notes": "Klik A1 p. 222. Feminine singular nominative interrogative pronoun 'ποια'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ποια είναι η γιατρός σας στο νοσοκομείο, η κυρία Παπαδοπούλου;",
        "example_en": "Who is your doctor at the hospital, Mrs. Papadopoulou?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking for female doctor identity"
    },
    {
        "id": "A1-U111B-011",
        "greek": "Ποιο φάρμακο παίρνεις όταν έχεις πονοκέφαλο;",
        "phonetic_hint": "pyo FAHR-mah-ko PEHR-nees O-tahn EH-khees po-no-KEH-fah-lo",
        "english": "Which medicine do you take when you have a headache?",
        "notes": "Klik A1 p. 222. Neuter singular interrogative 'ποιο' modifying 'φάρμακο'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ποιο φάρμακο παίρνεις συνήθως όταν έχεις πονοκέφαλο;",
        "example_en": "Which medicine do you usually take when you have a headache?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking about specific medication"
    },
    {
        "id": "A1-U111B-012",
        "greek": "Ποιανού είναι αυτό το βιβλιάριο υγείας;",
        "phonetic_hint": "pyah-NOO EE-neh ahf-TO to veev-lee-AH-ree-o ee-YEE-ahs",
        "english": "Whose health booklet is this?",
        "notes": "Klik A1 p. 222. Genitive interrogative 'ποιανού' (whose?) asking for masculine or neuter owner.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ποιανού είναι αυτό το βιβλιάριο υγείας που βρήκαμε στη ρεσεψιόν;",
        "example_en": "Whose health booklet is this that we found at reception?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about ownership of medical records"
    },
    {
        "id": "A1-U111B-013",
        "greek": "Ποιανής είναι αυτή η ιατρική συνταγή;",
        "phonetic_hint": "pyah-NEES EE-neh ahf-TEE ee ee-ah-tree-KEE seen-dah-YEE",
        "english": "Whose medical prescription is this?",
        "notes": "Klik A1 p. 222. Feminine genitive interrogative pronoun 'ποιανής' (whose?).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ποιανής είναι αυτή η ιατρική συνταγή, της κυρίας Ελένης;",
        "example_en": "Whose medical prescription is this, Mrs. Eleni's?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking about prescription ownership"
    },
    {
        "id": "A1-U111B-014",
        "greek": "Ποιανών είναι αυτά τα φάρμακα στο τραπέζι;",
        "phonetic_hint": "pyah-NON EE-neh ahf-TAH tah FAHR-mah-kah sto trah-PEH-zee",
        "english": "Whose medicines are these on the table?",
        "notes": "Klik A1 p. 222. Genitive plural interrogative pronoun 'ποιανών' (whose?).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ποιανών είναι αυτά τα φάρμακα στο τραπέζι της κουζίνας;",
        "example_en": "Whose medicines are these on the kitchen table?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking about plural owners of medicine"
    },
    {
        "id": "A1-U111B-015",
        "greek": "Σε ποιον γιατρό πηγαίνεις όταν είσαι άρρωστος;",
        "phonetic_hint": "seh pyon yee-ah-TRO pee-YEH-nees O-tahn EE-seh AH-ro-stos",
        "english": "To which doctor do you go when you are sick?",
        "notes": "Klik A1 p. 222. Prepositional phrase 'σε ποιον' inquiring about the medical specialist.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Σε ποιον γιατρό πηγαίνεις όταν είσαι άρρωστος, στον οικογενειακό;",
        "example_en": "Which doctor do you go to when you are sick, to the family doctor?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking for medical recommendations"
    },
    {
        "id": "A1-U111B-016",
        "greek": "Ποιον γιατρό είδες στα επείγοντα περιστατικά;",
        "phonetic_hint": "pyon yee-ah-TRO EE-dhes stah eh-PEE-ghon-dah peh-ree-stah-tee-KAH",
        "english": "Which doctor did you see in the emergency department?",
        "notes": "Klik A1 p. 222. Accusative masculine interrogative 'ποιον' functioning as direct object.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ποιον γιατρό είδες στα επείγοντα περιστατικά χθες το βράδυ;",
        "example_en": "Which doctor did you see in the emergency room yesterday evening?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about hospital visits"
    },

    # =========================================================================
    # 3. Emphatic Possessive Pronouns: ο δικός μου, κλπ. (pp. 222-223)
    # =========================================================================
    {
        "id": "A1-U111B-017",
        "greek": "Αυτό το ψηφιακό θερμόμετρο είναι το δικό μου.",
        "phonetic_hint": "ahf-TO to psee-fee-ah-KO ther-MO-meh-tro EE-neh to dhee-KO moo",
        "english": "This digital thermometer is mine.",
        "notes": "Klik A1 p. 222. Emphatic possessive pronoun 'το δικό μου' (neuter singular nominative).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αυτό το ψηφιακό θερμόμετρο είναι το δικό μου, το άλλο είναι δικό σου.",
        "example_en": "This digital thermometer is mine, the other one is yours.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Claiming ownership with emphatic possessives"
    },
    {
        "id": "A1-U111B-018",
        "greek": "Η δική μου γιατρός μού είπε να ξεκουραστώ.",
        "phonetic_hint": "ee dhee-KEE moo yee-ah-TROS moo EE-peh nah kseh-koo-rah-STO",
        "english": "My own doctor told me to rest.",
        "notes": "Klik A1 p. 222. Emphatic possessive 'η δική μου' (feminine singular nominative).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η δική μου γιατρός μού είπε να ξεκουραστώ για μερικές ημέρες.",
        "example_en": "My own doctor told me to rest for a few days.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Citing one's personal physician"
    },
    {
        "id": "A1-U111B-019",
        "greek": "Το δικό σου παιδί έχει πυρετό ή μόνο βήχα;",
        "phonetic_hint": "to dhee-KO soo peh-DHEE EH-khee pee-reh-TO ee MO-no VEE-khah",
        "english": "Does your child have a fever or only a cough?",
        "notes": "Klik A1 p. 222. Emphatic possessive 'το δικό σου' (second-person singular).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το δικό σου παιδί έχει πυρετό ή μόνο βήχα και συνάχι;",
        "example_en": "Does your child have a fever or only a cough and runny nose?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about another's family health"
    },
    {
        "id": "A1-U111B-020",
        "greek": "Είναι δικό του το σιρόπι ή της αδερφής του;",
        "phonetic_hint": "EE-neh dhee-KO too to see-RO-pee ee tees ah-dher-FEES too",
        "english": "Is the syrup his or his sister's?",
        "notes": "Klik A1 p. 222. Emphatic possessive predicate 'δικό του' (third-person singular masculine).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Είναι δικό του το σιρόπι ή το πήρε για την αδερφή του;",
        "example_en": "Is the syrup his or did he get it for his sister?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Clarifying medicine recipient"
    },
    {
        "id": "A1-U111B-021",
        "greek": "Η δική της πίεση είναι απολύτως φυσιολογική.",
        "phonetic_hint": "ee dhee-KEE tees PEE-eh-see EE-neh ah-po-LEE-tos fee-see-o-lo-yee-KEE",
        "english": "Her blood pressure is completely normal.",
        "notes": "Klik A1 p. 222. Emphatic possessive 'η δική της' (third-person singular feminine).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η δική της πίεση είναι απολύτως φυσιολογική, δώδεκα με οκτώ.",
        "example_en": "Her blood pressure is completely normal, twelve over eight.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Reporting clinical readings"
    },
    {
        "id": "A1-U111B-022",
        "greek": "Τα δικά μας φάρμακα είναι μέσα στο ντουλάπι.",
        "phonetic_hint": "tah dhee-KAH mahs FAHR-mah-kah EE-neh MEH-sah sto dhoo-LAH-pee",
        "english": "Our medicines are inside the cabinet.",
        "notes": "Klik A1 p. 222. Emphatic possessive 'τα δικά μας' (first-person plural neuter).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τα δικά μας φάρμακα είναι μέσα στο ψηλό ντουλάπι του μπάνιου.",
        "example_en": "Our medicines are inside the high cabinet in the bathroom.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Indicating household medicine storage"
    },
    {
        "id": "A1-U111B-023",
        "greek": "Ποιανού είναι αυτές οι βιταμίνες; — Είναι οι δικές σας;",
        "phonetic_hint": "pyah-NOO EE-neh ahf-TES ee vee-tah-MEE-nes — EE-neh ee dhee-KES sahs",
        "english": "Whose vitamins are these? — Are they yours?",
        "notes": "Klik A1 p. 222. Contrast between genitive question 'ποιανού' and plural polite possessive 'οι δικές σας'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ποιανού είναι αυτές οι βιταμίνες στο γραφείο; — Είναι οι δικές σας, κυρία Μαρία;",
        "example_en": "Whose vitamins are these on the desk? — Are they yours, Mrs. Maria?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Clarifying ownership politely"
    },
    {
        "id": "A1-U111B-024",
        "greek": "Οι δικοί τους γιατροί συνέστησαν άμεση θεραπεία.",
        "phonetic_hint": "ee dhee-KEE toos yee-ah-TREE see-NEH-stee-sahn AH-meh-see theh-rah-PEE-ah",
        "english": "Their doctors recommended immediate treatment.",
        "notes": "Klik A1 p. 222. Emphatic possessive 'οι δικοί τους' (third-person plural masculine).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Οι δικοί τους γιατροί συνέστησαν άμεση θεραπεία στο νοσοκομείο.",
        "example_en": "Their doctors recommended immediate treatment at the hospital.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Relaying third-party medical advice"
    },

    # =========================================================================
    # 4. Expressing Symptoms, Pain and Physical Distress (pp. 220, 224-225)
    # =========================================================================
    {
        "id": "A1-U111B-025",
        "greek": "Τι έχεις; Δεν σε βλέπω καλά σήμερα.",
        "phonetic_hint": "tee EH-khees dhen seh VLEH-po kah-LAH SEE-meh-rah",
        "english": "What's wrong? You don't look well today.",
        "notes": "Klik A1 p. 220. Standard informal Greek inquiry when noticing symptoms in a friend.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τι έχεις; Δεν σε βλέπω καλά σήμερα, είσαι χλωμός.",
        "example_en": "What's wrong? You don't look well today, you are pale.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking how someone feels"
    },
    {
        "id": "A1-U111B-026",
        "greek": "Δεν αισθάνομαι καλά, έχω ζάλη και ναυτία.",
        "phonetic_hint": "dhen eh-STHAH-no-meh kah-LAH EH-kho ZAH-lee keh nahf-TEE-ah",
        "english": "I don't feel well, I have dizziness and nausea.",
        "notes": "Klik A1 p. 220, 224. Common response expressing systemic malaise.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Δεν αισθάνομαι καθόλου καλά, έχω ζάλη και ναυτία από το πρωί.",
        "example_en": "I don't feel well at all, I have dizziness and nausea since this morning.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing malaise and nausea"
    },
    {
        "id": "A1-U111B-027",
        "greek": "Πονάει πολύ το κεφάλι μου και ο λαιμός μου.",
        "phonetic_hint": "po-NAH-ee po-LEE to keh-FAH-lee moo keh o leh-MOS moo",
        "english": "My head and my throat hurt very much.",
        "notes": "Klik A1 p. 220, 224. 'Πονάει' (3rd sing.) used impersonally or with singular subjects.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πονάει πολύ το κεφάλι μου και ο λαιμός μου και δεν μπορώ να καταπιώ.",
        "example_en": "My head and my throat hurt very much and I cannot swallow.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Reporting localized pain"
    },
    {
        "id": "A1-U111B-028",
        "greek": "Πονάνε τα πόδια μου και η μέση μου από την κούραση.",
        "phonetic_hint": "po-NAH-neh tah PO-dhya moo keh ee MEH-see moo ah-PO teen KOO-rah-see",
        "english": "My legs and my lower back hurt from exhaustion.",
        "notes": "Klik A1 p. 224. 'Πονάνε' (3rd pl.) agreeing with plural body parts 'τα πόδια'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πονάνε τα πόδια μου και η μέση μου μετά από τόση ορθοστασία.",
        "example_en": "My legs and my lower back hurt after standing for so long.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing musculoskeletal pain"
    },
    {
        "id": "A1-U111B-029",
        "greek": "Έχω δέκατα, το θερμόμετρο δείχνει τριάντα επτά και πέντε.",
        "phonetic_hint": "EH-kho DHEH-kah-tah to ther-MO-meh-tro DHEEKH-nee tree-AHN-dah ep-TAH keh PEN-deh",
        "english": "I have a slight fever, the thermometer shows thirty-seven point five.",
        "notes": "Klik A1 p. 220. Idiomatic 'έχω δέκατα' = low-grade fever (37.1°C to 37.9°C).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Έχω δέκατα, το θερμόμετρο δείχνει τριάντα επτά και πέντε και νιώθω αδυναμία.",
        "example_en": "I have a slight fever, the thermometer shows thirty-seven point five and I feel weak.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Reporting body temperature reading"
    },
    {
        "id": "A1-U111B-030",
        "greek": "Έχω υψηλό πυρετό, σχεδόν τριάντα εννέα, και τρέμω.",
        "phonetic_hint": "EH-kho eep-see-LO pee-reh-TO skheh-DHON tree-AHN-dah eh-NEH-ah keh TREH-mo",
        "english": "I have a high fever, almost thirty-nine, and I am shivering.",
        "notes": "Klik A1 p. 220. Expressing acute illness with high temperature.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Έχω υψηλό πυρετό, σχεδόν τριάντα εννέα, και τρέμω από το κρύο.",
        "example_en": "I have a high fever, almost thirty-nine, and I am shivering with chills.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing severe febrile symptoms"
    },
    {
        "id": "A1-U111B-031",
        "greek": "Έχω έντονο βήχα και συνάχι εδώ και δύο μέρες.",
        "phonetic_hint": "EH-kho EN-do-no VEE-khah keh see-NAH-khee eh-DHO keh DHEE-o MEH-res",
        "english": "I have a bad cough and a runny nose for two days now.",
        "notes": "Klik A1 p. 220. Time expression 'εδώ και δύο μέρες' paired with present symptoms.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Έχω έντονο βήχα και συνάχι εδώ και δύο μέρες και δεν μπορώ να αναπνεύσω.",
        "example_en": "I have a bad cough and a runny nose for two days now and I cannot breathe.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Reporting respiratory symptom duration"
    },
    {
        "id": "A1-U111B-032",
        "greek": "Είμαι πολύ κρυωμένος και δεν έχω καθόλου όρεξη για φαγητό.",
        "phonetic_hint": "EE-meh po-LEE kree-o-MEH-nos keh dhen EH-kho kah-THO-loo O-rek-see yah fah-yee-TO",
        "english": "I have a bad cold and I have no appetite for food at all.",
        "notes": "Klik A1 p. 220. Participle 'κρυωμένος' used as predicate adjective for having a cold.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Είμαι πολύ κρυωμένος και δεν έχω καθόλου όρεξη για φαγητό σήμερα.",
        "example_en": "I have a bad cold and I have no appetite for food at all today.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing cold symptoms and loss of appetite"
    },
    {
        "id": "A1-U111B-033",
        "greek": "Κρύωσα χθες στο γραφείο γιατί είχε πολύ δυνατό κλιματισμό.",
        "phonetic_hint": "KREE-o-sah khthes sto grah-FEE-o yah-TEE EE-kheh po-LEE dhee-nah-TO klee-mah-tees-MO",
        "english": "I caught a cold yesterday at the office because the air conditioning was very strong.",
        "notes": "Klik A1 p. 220, 230. Aorist verb 'κρύωσα' indicating the moment of catching a chill.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κρύωσα χθες στο γραφείο γιατί είχε πολύ δυνατό κλιματισμό όλη μέρα.",
        "example_en": "I caught a chill yesterday at the office because the air conditioning was very strong all day.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Explaining the cause of catching a cold"
    },

    # =========================================================================
    # 5. Doctor Consultations & Clinical Advice (pp. 220, 225-226)
    # =========================================================================
    {
        "id": "A1-U111B-034",
        "greek": "Πού πονάτε ακριβώς και από πότε άρχισαν τα συμπτώματα;",
        "phonetic_hint": "poo po-NAH-teh ah-kree-VOS keh ah-PO PO-teh AHR-khee-sahn tah seem-BTO-mah-tah",
        "english": "Where exactly do you feel pain and when did the symptoms start?",
        "notes": "Klik A1 p. 220, 226. Standard opening questions by a Greek clinician in the formal plural.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πείτε μου, παρακαλώ, πού πονάτε ακριβώς και από πότε άρχισαν τα συμπτώματα;",
        "example_en": "Tell me, please, where exactly do you hurt and since when did the symptoms start?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Doctor's clinical anamnesis"
    },
    {
        "id": "A1-U111B-035",
        "greek": "Ανοίξτε το στόμα σας και βγάλτε τη γλώσσα, παρακαλώ.",
        "phonetic_hint": "ah-NEEKS-teh to STO-mah sahs keh VGHAL-teh tee GHLOS-sah pah-rah-kah-LO",
        "english": "Open your mouth and stick out your tongue, please.",
        "notes": "Klik A1 p. 220, 225. Clinical imperative commands: 'ανοίξτε' and 'βγάλτε'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Καθίστε στην καρέκλα, ανοίξτε το στόμα σας και βγάλτε τη γλώσσα, παρακαλώ.",
        "example_en": "Sit on the chair, open your mouth and stick out your tongue, please.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Giving physical examination instructions"
    },
    {
        "id": "A1-U111B-036",
        "greek": "Πάρτε μια βαθιά ανάσα και κρατήστε την αναπνοή σας.",
        "phonetic_hint": "PAHR-teh myah vah-THYAH ah-NAH-sah keh krah-TEES-teh teen ah-nah-pno-EE sahs",
        "english": "Take a deep breath and hold your breath.",
        "notes": "Klik A1 p. 225. Chest auscultation instructions in the formal imperative.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πάρτε μια βαθιά ανάσα και κρατήστε την αναπνοή σας για δύο δευτερόλεπτα.",
        "example_en": "Take a deep breath and hold your breath for two seconds.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Guiding respiratory examination"
    },
    {
        "id": "A1-U111B-037",
        "greek": "Μην ανησυχείτε, είναι μια απλή ίωση που περνάει σε λίγες μέρες.",
        "phonetic_hint": "meen ah-nee-see-KHEE-teh EE-neh myah ah-PLEE EE-o-see poo per-NAH-ee seh LEE-yes MEH-res",
        "english": "Don't worry, it is a simple viral infection that passes in a few days.",
        "notes": "Klik A1 p. 220. Negative imperative reassurance: 'μην ανησυχείτε'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μην ανησυχείτε καθόλου, είναι μια απλή ίωση που περνάει σε λίγες μέρες.",
        "example_en": "Don't worry at all, it's a simple virus that clears up in a few days.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Offering clinical reassurance"
    },
    {
        "id": "A1-U111B-038",
        "greek": "Πρέπει να μείνετε στο κρεβάτι και να ξεκουραστείτε καλά.",
        "phonetic_hint": "PREH-pee nah MEE-neh-teh sto kreh-VAH-tee keh nah kseh-koo-rah-STEE-teh kah-LAH",
        "english": "You must stay in bed and get plenty of rest.",
        "notes": "Klik A1 p. 220. Modal construction 'πρέπει να + subjunctive' for medical instructions.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πρέπει να μείνετε στο κρεβάτι για τρεις μέρες και να ξεκουραστείτε καλά.",
        "example_en": "You must stay in bed for three days and rest well.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Prescribing bed rest"
    },
    {
        "id": "A1-U111B-039",
        "greek": "Πιείτε πολλά ζεστά υγρά, τσάι του βουνού και χαμομήλι.",
        "phonetic_hint": "PYEE-teh po-LAH zes-TAH ee-GHRAH TSAH-ee too voo-NOO keh khah-mo-MEE-lee",
        "english": "Drink plenty of warm liquids, mountain tea and chamomile.",
        "notes": "Klik A1 p. 220. Imperative advice for hydration and herbal remedies.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πιείτε πολλά ζεστά υγρά, τσάι του βουνού και χαμομήλι με μέλι.",
        "example_en": "Drink plenty of warm fluids, mountain tea and chamomile with honey.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Recommending home remedies"
    },
    {
        "id": "A1-U111B-040",
        "greek": "Θα σας γράψω μια αντιβίωση και μερικά παυσίπονα.",
        "phonetic_hint": "thah sahs GHRAHP-so myah ahn-dee-VEE-o-see keh meh-ree-KAH pahf-SEE-po-nah",
        "english": "I will prescribe you an antibiotic and some painkillers.",
        "notes": "Klik A1 p. 220, 226. Future tense 'θα σας γράψω' meaning 'I will prescribe for you'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Θα σας γράψω μια αντιβίωση για πέντε μέρες και μερικά παυσίπονα.",
        "example_en": "I will prescribe you an antibiotic for five days and some painkillers.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Issuing a medical prescription"
    },

    # =========================================================================
    # 6. At the Pharmacy & Taking Medication (pp. 221, 227)
    # =========================================================================
    {
        "id": "A1-U111B-041",
        "greek": "Γεια σας, χρειάζομαι κάτι αποτελεσματικό για τον πονόλαιμο.",
        "phonetic_hint": "YAH sahs khree-AH-zo-meh KAH-tee ah-po-teh-lez-mah-tee-KO yah ton po-NO-leh-mo",
        "english": "Hello, I need something effective for a sore throat.",
        "notes": "Klik A1 p. 221. Standard pharmacy opening line requesting symptom relief.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Γεια σας, χρειάζομαι κάτι αποτελεσματικό για τον πονόλαιμο και τον βήχα.",
        "example_en": "Hello, I need something effective for a sore throat and cough.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Requesting over-the-counter remedies"
    },
    {
        "id": "A1-U111B-042",
        "greek": "Έχετε ιατρική συνταγή ή θέλετε φάρμακο χωρίς συνταγή;",
        "phonetic_hint": "EH-kheh-teh ee-ah-tree-KEE seen-dah-YEE ee THEH-leh-teh FAHR-mah-ko kho-REES seen-dah-YEE",
        "english": "Do you have a medical prescription or do you want medicine without a prescription?",
        "notes": "Klik A1 p. 221. Distinguishing prescription ('με συνταγή') from OTC ('χωρίς συνταγή') drugs.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Έχετε ιατρική συνταγή από τον γιατρό ή θέλετε φάρμακο χωρίς συνταγή;",
        "example_en": "Do you have a doctor's prescription or do you want an over-the-counter medicine?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Pharmacist clarification of prescription status"
    },
    {
        "id": "A1-U111B-043",
        "greek": "Να παίρνετε ένα χάπι κάθε οκτώ ώρες μετά το φαγητό.",
        "phonetic_hint": "nah PEHR-neh-teh EH-nah KHAH-pee KAH-theh ok-TO O-res meh-TAH to fah-yee-TO",
        "english": "Take one pill every eight hours after meals.",
        "notes": "Klik A1 p. 221. Subjunctive directive 'να παίρνετε' specifying dosage intervals.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Να παίρνετε ένα χάπι κάθε οκτώ ώρες μετά το φαγητό με ένα γεμάτο ποτήρι νερό.",
        "example_en": "Take one pill every eight hours after meals with a full glass of water.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Giving dosage instructions"
    },
    {
        "id": "A1-U111B-044",
        "greek": "Αυτό το σιρόπι είναι ένα κουταλάκι τρεις φορές την ημέρα.",
        "phonetic_hint": "ahf-TO to see-RO-pee EE-neh EH-nah koo-tah-LAH-kee trees fo-RES teen ee-MEH-rah",
        "english": "This syrup is one spoonful three times a day.",
        "notes": "Klik A1 p. 221. Standard frequency phrase: 'τρεις φορές την ημέρα'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αυτό το σιρόπι είναι ένα κουταλάκι τρεις φορές την ημέρα πριν από τον ύπνο.",
        "example_en": "This syrup is one teaspoon three times a day before sleep.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Directing liquid medication frequency"
    },
    {
        "id": "A1-U111B-045",
        "greek": "Βάλτε αυτή την καταπραϋντική αλοιφή δύο φορές την ημέρα στην πληγή.",
        "phonetic_hint": "VAHL-teh ahf-TEEN teen kah-tah-prah-een-dhee-KEE ah-lee-FEE DHEE-o fo-RES teen ee-MEH-rah steen plee-YEE",
        "english": "Apply this soothing ointment twice a day to the wound.",
        "notes": "Klik A1 p. 221. Imperative 'βάλτε' (put/apply) with topical skin remedy.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βάλτε αυτή την καταπραϋντική αλοιφή δύο φορές την ημέρα στην πληγή και καλύψτε την με επίδεσμο.",
        "example_en": "Apply this soothing ointment twice a day to the wound and cover it with a bandage.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Explaining topical medication application"
    },
    {
        "id": "A1-U111B-046",
        "greek": "Μπορείτε να μου μετρήσετε την αρτηριακή πίεση, παρακαλώ;",
        "phonetic_hint": "bo-REE-teh nah moo meh-TREE-seh-teh teen ahr-tee-ree-ah-KEE PEE-eh-see pah-rah-kah-LO",
        "english": "Could you measure my blood pressure, please?",
        "notes": "Klik A1 p. 221, 230. Courteous request in Greek pharmacies: 'μπορείτε να μου μετρήσετε...'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μπορείτε να μου μετρήσετε την αρτηριακή πίεση, παρακαλώ; Νιώθω μια μικρή ζάλη.",
        "example_en": "Could you measure my blood pressure, please? I feel a slight dizziness.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Requesting blood pressure measurement in pharmacy"
    },

    # =========================================================================
    # 7. Recovery Wishes & Social Expressions (pp. 219, 228-229)
    # =========================================================================
    {
        "id": "A1-U111B-047",
        "greek": "Περαστικά σου! Ελπίζω να γίνεις γρήγορα καλά!",
        "phonetic_hint": "peh-rah-stee-KAH soo el-PEE-zo nah YEE-nees GHREE-gho-rah kah-LAH",
        "english": "Get well soon! I hope you recover quickly!",
        "notes": "Klik A1 p. 219, 228. 'Περαστικά!' is the hallmark Greek recovery wish (may it pass!).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Περαστικά σου! Ελπίζω να γίνεις γρήγορα καλά και να τα πούμε από κοντά.",
        "example_en": "Get well soon! I hope you recover quickly and we talk in person.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Wishing someone a speedy recovery"
    },
    {
        "id": "A1-U111B-048",
        "greek": "Σιδερένιος! Χαίρομαι πολύ που γύρισες γερός στη δουλειά!",
        "phonetic_hint": "see-dheh-REH-nyos KHEH-ro-meh po-LEE poo YEE-ree-ses yeh-ROS stee dhoo-LYAH",
        "english": "May you be strong as iron! I'm so glad you returned healthy to work!",
        "notes": "Klik A1 p. 228. 'Σιδερένιος' (masc.) / 'Σιδερένια' (fem.) is a cultural greeting wished to someone recovering from illness or medical procedure.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Σιδερένιος! Χαίρομαι πολύ που γύρισες γερός και δυνατός στη δουλειά μετά την εγχείρηση!",
        "example_en": "May you be strong as iron! I am so glad you came back healthy and strong to work after the operation!",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Welcoming someone back after illness"
    },
    {
        "id": "A1-U111B-049",
        "greek": "Καλή ανάρρωση και γρήγορη επιστροφή στα μαθήματα!",
        "phonetic_hint": "kah-LEE ah-NAHR-o-see keh GHREE-gho-ree eh-pee-stro-FEE stah mah-THEE-mah-tah",
        "english": "Good recovery and a speedy return to classes!",
        "notes": "Klik A1 p. 228. Formal written or spoken expression 'Καλή ανάρρωση'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Σας ευχόμαστε καλή ανάρρωση και γρήγορη επιστροφή στα μαθήματα!",
        "example_en": "We wish you a good recovery and a speedy return to classes!",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Offering formal recovery wishes"
    },
    {
        "id": "A1-U111B-050",
        "greek": "Να προσέχεις τον εαυτό σου και να μην κουράζεσαι!",
        "phonetic_hint": "nah pro-SEH-khees ton eh-ahf-TO soo keh nah meen koo-RAH-zeh-seh",
        "english": "Take care of yourself and don't tire yourself out!",
        "notes": "Klik A1 p. 228, 231. Affectionate caretaking formula: 'Να προσέχεις τον εαυτό σου'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τώρα που ανάρρωσες, να προσέχεις τον εαυτό σου και να μην κουράζεσαι.",
        "example_en": "Now that you recovered, take care of yourself and don't overexert yourself.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Giving caring advice during convalescence"
    }
]

lesson_u111b = {
    "unit_id": "unit-111b",
    "lesson_id": "lesson-01",
    "title": "Ενότητα 10: Περαστικά! — Γραμματική & Εκφράσεις (Pages 219-232)",
    "description": (
        "Grammar paradigms, communicative syntax, and real-world clinical expressions from Unit 10 of Klik sta Ellinika A1: "
        "relative clauses with the invariant pronoun 'που', "
        "interrogative pronouns across cases (ποιος/ποιανού/σε ποιον/ποιον), "
        "emphatic possessive pronouns (ο δικός μου, κλπ.), "
        "symptom and pain expressions (πονάει/πονάνε, έχω δέκατα, κρυωμένος), "
        "doctor consultation dialogues and examination commands, "
        "pharmacy dosage directions (τρεις φορές την ημέρα, με/χωρίς συνταγή), "
        "and cultural health wishes (Περαστικά!, Σιδερένιος!, Καλή ανάρρωση!)."
    ),
    "lesson_status": "not_started",
    "entries": cards_u111b
}

def main():
    print(f"Writing {len(cards_u111b)} cards to {YAML_PATH}...")
    with open(YAML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(lesson_u111b, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("YAML successfully written.")

    # Update manifest.yaml
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    units = manifest.get("units", [])
    existing = next((u for u in units if u.get("id") == "unit-111b"), None)
    unit_111b_entry = {
        "id": "unit-111b",
        "title": "Κλικ στα Ελληνικά Α1: Σελίδες 219-232 (Ενότητα 10: Περαστικά! - Γραμματική & Εκφράσεις)",
        "order": "KlikA1-11-B",
        "is_expansion": True,
        "expansion_of": "KlikA1-11-A",
        "lessons": [
            {
                "id": "lesson-01",
                "file": "unit-111b/lesson-01.yaml",
                "title": "Ενότητα 10: Περαστικά! — Γραμματική & Εκφράσεις (Pages 219-232)"
            }
        ]
    }

    if existing:
        print("Updating existing unit-111b in manifest.yaml...")
        idx = units.index(existing)
        units[idx] = unit_111b_entry
    else:
        print("Appending unit-111b to manifest.yaml...")
        units.append(unit_111b_entry)

    manifest["units"] = units

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("Manifest successfully updated with unit-111b!")

if __name__ == "__main__":
    main()

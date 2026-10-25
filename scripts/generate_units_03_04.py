# -*- coding: utf-8 -*-
"""
Curriculum generator for CEFR Level A1 Modern Greek
Batch 2: Unit 3 & Unit 4
Strictly aligned with KEG guidelines & ΚΛΙΚ στα ελληνικά
"""
import sys
import json
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

cards = [
    # =========================================================================
    # UNIT 3: Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)
    # =========================================================================
    {
        "id": "A1-U03-001",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "το επάγγελμα",
        "back_primary": "profession / occupation / job",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα επαγγέλματα",
            "accusative_singular": "το επάγγελμα"
        },
        "keg_communicative_function": "Inquiring about and stating occupational status",
        "example_el": "Ποιο είναι το επάγγελμά σας;",
        "example_en": "What is your profession?",
        "notes_or_mnemonics": "Neuter in -μα with plural in -ματα. Core field on KEG exam personal registration forms."
    },
    {
        "id": "A1-U03-002",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "ο δάσκαλος",
        "back_primary": "primary school teacher (male)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι δάσκαλοι",
            "accusative_singular": "τον δάσκαλο"
        },
        "keg_communicative_function": "Identifying primary school teaching professionals",
        "example_el": "Ο δάσκαλος διδάσκει τα παιδιά στην τάξη.",
        "example_en": "The teacher teaches the children in the classroom.",
        "notes_or_mnemonics": "Proparoxytone masculine in -ος (accent shifts in genitive, but stays stable at A1 nominative/accusative)."
    },
    {
        "id": "A1-U03-003",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "η δασκάλα",
        "back_primary": "primary school teacher (female)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι δασκάλες",
            "accusative_singular": "τη δασκάλα"
        },
        "keg_communicative_function": "Identifying female primary school educators",
        "example_el": "Η δασκάλα είναι πολύ ευγενική.",
        "example_en": "The teacher is very kind.",
        "notes_or_mnemonics": "Feminine equivalent of ο δάσκαλος; regular feminine in -α with plural in -ες."
    },
    {
        "id": "A1-U03-004",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "ο καθηγητής",
        "back_primary": "professor / secondary school teacher (male)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι καθηγητές",
            "accusative_singular": "τον καθηγητή"
        },
        "keg_communicative_function": "Identifying secondary or tertiary academic instructors",
        "example_el": "Ο καθηγητής διδάσκει στο πανεπιστήμιο.",
        "example_en": "The professor teaches at the university.",
        "notes_or_mnemonics": "Masculine in -ης (plural: -ες). Used for both high school teachers and university professors."
    },
    {
        "id": "A1-U03-005",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "η καθηγήτρια",
        "back_primary": "professor / secondary school teacher (female)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι καθηγήτριες",
            "accusative_singular": "την καθηγήτρια"
        },
        "keg_communicative_function": "Identifying female academic instructors",
        "example_el": "Η κυρία Ανδρέου είναι καθηγήτρια γαλλικών.",
        "example_en": "Mrs. Andreou is a French teacher.",
        "notes_or_mnemonics": "Feminine suffix -τρια derived from masculine in -τής (ο καθηγητής -> η καθηγήτρια)."
    },
    {
        "id": "A1-U03-006",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "ο μαθητής",
        "back_primary": "school pupil / student (male)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι μαθητές",
            "accusative_singular": "τον μαθητή"
        },
        "keg_communicative_function": "Identifying male primary or secondary school students",
        "example_el": "Ο Νίκος είναι επιμελής μαθητής.",
        "example_en": "Nikos is a diligent student.",
        "notes_or_mnemonics": "Masculine noun in -ης. Note distinction: μαθητής (school pupil) vs φοιτητής (university student)."
    },
    {
        "id": "A1-U03-007",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "η μαθήτρια",
        "back_primary": "school pupil / student (female)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι μαθήτριες",
            "accusative_singular": "τη μαθήτρια"
        },
        "keg_communicative_function": "Identifying female primary or secondary school students",
        "example_el": "Η Μαρία είναι μαθήτρια στο γυμνάσιο.",
        "example_en": "Maria is a student in middle school.",
        "notes_or_mnemonics": "Feminine in -τρια (plural: οι μαθήτριες)."
    },
    {
        "id": "A1-U03-008",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "ο φοιτητής",
        "back_primary": "university student (male)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι φοιτητές",
            "accusative_singular": "τον φοιτητή"
        },
        "keg_communicative_function": "Stating university student status",
        "example_el": "Είμαι φοιτητής ιατρικής.",
        "example_en": "I am a medical student.",
        "notes_or_mnemonics": "Refers strictly to tertiary/higher education students."
    },
    {
        "id": "A1-U03-009",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "η φοιτήτρια",
        "back_primary": "university student (female)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι φοιτήτριες",
            "accusative_singular": "τη φοιτήτρια"
        },
        "keg_communicative_function": "Stating female university student status",
        "example_el": "Η Άννα είναι φοιτήτρια στην Αθήνα.",
        "example_en": "Anna is a university student in Athens.",
        "notes_or_mnemonics": "Feminine counterpart of ο φοιτητής."
    },
    {
        "id": "A1-U03-010",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "ο γιατρός",
        "back_primary": "doctor / physician",
        "grammatical_info": {
            "part_of_speech": "noun (masculine / common gender)",
            "plural": "οι γιατροί",
            "accusative_singular": "τον γιατρό"
        },
        "keg_communicative_function": "Talking about healthcare professions",
        "example_el": "Ο γιατρός εξετάζει τον ασθενή.",
        "example_en": "The doctor is examining the patient.",
        "notes_or_mnemonics": "Oxytone masculine in -ός. In modern Greek, often used with feminine article for female doctors: η γιατρός."
    },
    {
        "id": "A1-U03-011",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "η νοσοκόμα",
        "back_primary": "nurse (female)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι νοσοκόμες",
            "accusative_singular": "τη νοσοκόμα"
        },
        "keg_communicative_function": "Describing nursing staff and hospital personnel",
        "example_el": "Η νοσοκόμα δουλεύει στο νοσοκομείο.",
        "example_en": "The nurse works at the hospital.",
        "notes_or_mnemonics": "Compound from νόσος (illness) + κομώ (care for). Male form is ο νοσοκόμος."
    },
    {
        "id": "A1-U03-012",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "ο δικηγόρος",
        "back_primary": "lawyer / attorney",
        "grammatical_info": {
            "part_of_speech": "noun (masculine / common gender)",
            "plural": "οι δικηγόροι",
            "accusative_singular": "τον δικηγόρο"
        },
        "keg_communicative_function": "Describing legal professions",
        "example_el": "Ο δικηγόρος έχει γραφείο στο κέντρο.",
        "example_en": "The lawyer has an office in the city centre.",
        "notes_or_mnemonics": "Compound from δίκη (trial/justice) + αγορεύω (speak publicly). Female lawyer: η δικηγόρος."
    },
    {
        "id": "A1-U03-013",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "ο γραμματέας",
        "back_primary": "secretary / administrative assistant",
        "grammatical_info": {
            "part_of_speech": "noun (masculine / feminine)",
            "plural": "οι γραμματείς",
            "accusative_singular": "τον / τη γραμματέα"
        },
        "keg_communicative_function": "Describing office administration roles",
        "example_el": "Η γραμματέας απαντάει στο τηλέφωνο.",
        "example_en": "The secretary answers the phone.",
        "notes_or_mnemonics": "Common-gender noun: ο γραμματέας (male), η γραμματέας (female). Plural: οι γραμματείς."
    },
    {
        "id": "A1-U03-014",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "ο υπάλληλος",
        "back_primary": "employee / office clerk",
        "grammatical_info": {
            "part_of_speech": "noun (masculine / common gender)",
            "plural": "οι υπάλληλοι",
            "accusative_singular": "τον υπάλληλο"
        },
        "keg_communicative_function": "Describing employment in offices, stores, and banks",
        "example_el": "Είναι υπάλληλος σε μία τράπεζα.",
        "example_en": "He/she is an employee in a bank.",
        "notes_or_mnemonics": "Proparoxytone noun in -ος. Female equivalent is η υπάλληλος."
    },
    {
        "id": "A1-U03-015",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "ο πωλητής",
        "back_primary": "salesperson / shop assistant (male)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι πωλητές",
            "accusative_singular": "τον πωλητή"
        },
        "keg_communicative_function": "Identifying retail commerce staff",
        "example_el": "Ο πωλητής εξυπηρετεί τους πελάτες.",
        "example_en": "The shop assistant serves the customers.",
        "notes_or_mnemonics": "Agent noun in -τής with oxytone stress."
    },
    {
        "id": "A1-U03-016",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "η πωλήτρια",
        "back_primary": "salesperson / shop assistant (female)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πωλήτριες",
            "accusative_singular": "την πωλήτρια"
        },
        "keg_communicative_function": "Identifying female retail personnel",
        "example_el": "Η πωλήτρια δουλεύει σε κατάστημα ρούχων.",
        "example_en": "The saleswoman works in a clothing store.",
        "notes_or_mnemonics": "Feminine agent suffix -τρια with paroxytone stress (η πωλήτρια)."
    },
    {
        "id": "A1-U03-017",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "ο σερβιτόρος",
        "back_primary": "waiter",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι σερβιτόροι",
            "accusative_singular": "τον σερβιτόρο"
        },
        "keg_communicative_function": "Addressing and describing dining staff in tavernas and cafes",
        "example_el": "Ο σερβιτόρος φέρνει τον κατάλογο.",
        "example_en": "The waiter brings the menu.",
        "notes_or_mnemonics": "From French 'serviteur'. Standard paroxytone masculine in -ος."
    },
    {
        "id": "A1-U03-018",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "η σερβιτόρα",
        "back_primary": "waitress",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι σερβιτόρες",
            "accusative_singular": "τη σερβιτόρα"
        },
        "keg_communicative_function": "Describing dining service staff",
        "example_el": "Η σερβιτόρα παίρνει την παραγγελία.",
        "example_en": "The waitress takes the order.",
        "notes_or_mnemonics": "Feminine form of ο σερβιτόρος."
    },
    {
        "id": "A1-U03-019",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "ο οδηγός",
        "back_primary": "driver / guide",
        "grammatical_info": {
            "part_of_speech": "noun (masculine / common gender)",
            "plural": "οι οδηγοί",
            "accusative_singular": "τον οδηγό"
        },
        "keg_communicative_function": "Describing transport and transit operators",
        "example_el": "Ο οδηγός του λεωφορείου είναι πολύ προσεκτικός.",
        "example_en": "The bus driver is very careful.",
        "notes_or_mnemonics": "Oxytone masculine in -ός (plural: οι οδηγοί). Used for drivers (ταξί, λεωφορείου) and tourist guides."
    },
    {
        "id": "A1-U03-020",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "ο μάγειρας",
        "back_primary": "cook / chef",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι μάγειρες",
            "accusative_singular": "τον μάγειρα"
        },
        "keg_communicative_function": "Describing culinary and restaurant occupations",
        "example_el": "Ο μάγειρας ετοιμάζει νόστιμο φαγητό.",
        "example_en": "The chef prepares delicious food.",
        "notes_or_mnemonics": "Proparoxytone masculine in -ας with plural in -ες (οι μάγειρες)."
    },
    {
        "id": "A1-U03-021",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "το γραφείο",
        "back_primary": "office / desk",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα γραφεία",
            "accusative_singular": "το γραφείο"
        },
        "keg_communicative_function": "Specifying workplace locations",
        "example_el": "Δουλεύω σε ένα μεγάλο γραφείο.",
        "example_en": "I work in a big office.",
        "notes_or_mnemonics": "Regular neuter in -ο. Governed by 'σε + άρθρο' (στο γραφείο)."
    },
    {
        "id": "A1-U03-022",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "το σχολείο",
        "back_primary": "school",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα σχολεία",
            "accusative_singular": "το σχολείο"
        },
        "keg_communicative_function": "Referring to places of primary and secondary education",
        "example_el": "Τα παιδιά πάνε στο σχολείο κάθε πρωί.",
        "example_en": "The children go to school every morning.",
        "notes_or_mnemonics": "Paroxytone neuter in -είο (plural: τα σχολεία)."
    },
    {
        "id": "A1-U03-023",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "το πανεπιστήμιο",
        "back_primary": "university",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πανεπιστήμια",
            "accusative_singular": "το πανεπιστήμιο"
        },
        "keg_communicative_function": "Referring to higher education institutions",
        "example_el": "Σπουδάζω νομικά στο πανεπιστήμιο.",
        "example_en": "I study law at the university.",
        "notes_or_mnemonics": "Proparoxytone neuter in -ιο (plural: τα πανεπιστήμια)."
    },
    {
        "id": "A1-U03-024",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "το νοσοκομείο",
        "back_primary": "hospital",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα νοσοκομεία",
            "accusative_singular": "το νοσοκομείο"
        },
        "keg_communicative_function": "Referring to healthcare workplaces and facilities",
        "example_el": "Ο γιατρός είναι τώρα στο νοσοκομείο.",
        "example_en": "The doctor is at the hospital right now.",
        "notes_or_mnemonics": "Neuter in -είο. Frequent landmark in KEG city direction questions."
    },
    {
        "id": "A1-U03-025",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "η εταιρεία",
        "back_primary": "company / firm / business",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι εταιρείες",
            "accusative_singular": "την εταιρεία"
        },
        "keg_communicative_function": "Describing corporate employment",
        "example_el": "Δουλεύει σε μία πολυεθνική εταιρεία.",
        "example_en": "He/she works at a multinational company.",
        "notes_or_mnemonics": "Feminine noun in -εια (plural: οι εταιρείες)."
    },
    {
        "id": "A1-U03-026",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "η διεύθυνση",
        "back_primary": "address / street address",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι διευθύνσεις",
            "accusative_singular": "τη διεύθυνση"
        },
        "keg_communicative_function": "Asking for and writing postal/residential address",
        "example_el": "Ποια είναι η διεύθυνσή σας;",
        "example_en": "What is your address?",
        "notes_or_mnemonics": "Feminine noun in -ση with plural in -σεις. Core item in KEG Writing Task 1 forms."
    },
    {
        "id": "A1-U03-027",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "η οδός",
        "back_primary": "street / road",
        "grammatical_info": {
            "part_of_speech": "noun (feminine in -ος)",
            "plural": "οι οδοί",
            "accusative_singular": "την οδό"
        },
        "keg_communicative_function": "Specifying street names on contact forms",
        "example_el": "Μένω στην οδό Σταδίου, στον αριθμό 10.",
        "example_en": "I live on Stadiou Street, at number 10.",
        "notes_or_mnemonics": "Grammatical exception: feminine gender despite ending in -ος (accusative: την οδό)."
    },
    {
        "id": "A1-U03-028",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "ο αριθμός",
        "back_primary": "number / street number",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι αριθμοί",
            "accusative_singular": "τον αριθμό"
        },
        "keg_communicative_function": "Stating house, flat, and phone numbers",
        "example_el": "Ποιος είναι ο αριθμός του σπιτιού σου;",
        "example_en": "What is your house number?",
        "notes_or_mnemonics": "Oxytone masculine noun in -ός (plural: οι αριθμοί)."
    },
    {
        "id": "A1-U03-029",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "το τηλέφωνο",
        "back_primary": "telephone / landline / phone number",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα τηλέφωνα",
            "accusative_singular": "το τηλέφωνο"
        },
        "keg_communicative_function": "Exchanging personal contact telephone numbers",
        "example_el": "Ποιο είναι το τηλέφωνό σου;",
        "example_en": "What is your phone number?",
        "notes_or_mnemonics": "Proparoxytone neuter. Takes enclitic accent before possessive pronoun: το τηλέφωνό μου."
    },
    {
        "id": "A1-U03-030",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "το κινητό",
        "back_primary": "mobile phone / cellphone",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κινητά",
            "accusative_singular": "το κινητό"
        },
        "keg_communicative_function": "Giving and asking for mobile phone numbers",
        "example_el": "Έχεις το κινητό της Μαρίας;",
        "example_en": "Do you have Maria's mobile number?",
        "notes_or_mnemonics": "Short for 'το κινητό τηλέφωνο'. Always neuter in -ό."
    },
    {
        "id": "A1-U03-031",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "το ταχυδρομείο",
        "back_primary": "post office / postal service",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ταχυδρομεία",
            "accusative_singular": "το ταχυδρομείο"
        },
        "keg_communicative_function": "Referring to postal services and public buildings",
        "example_el": "Το ταχυδρομείο είναι ανοιχτό μέχρι τις δύο.",
        "example_en": "The post office is open until two o'clock.",
        "notes_or_mnemonics": "Compound from ταχύς (swift) + δρόμος (run/path). Abbreviated on Greek signs as ΕΛΤΑ."
    },
    {
        "id": "A1-U03-032",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "vocabulary",
        "front": "ο ταχυδρομικός κώδικας",
        "back_primary": "postal code / ZIP code",
        "grammatical_info": {
            "part_of_speech": "noun phrase (masculine)",
            "plural": "οι ταχυδρομικοί κώδικες",
            "accusative_singular": "τον ταχυδρομικό κώδικα"
        },
        "keg_communicative_function": "Completing postal code entries on registration forms",
        "example_el": "Ο ταχυδρομικός κώδικας της περιοχής είναι 10679.",
        "example_en": "The postal code of the area is 10679.",
        "notes_or_mnemonics": "Often abbreviated as Τ.Κ. in Greek forms and exam papers."
    },
    {
        "id": "A1-U03-033",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "verb",
        "front": "δουλεύω",
        "back_primary": "to work / to have a job",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό δουλεύει",
            "first_person_plural": "εμείς δουλεύουμε"
        },
        "keg_communicative_function": "Talking about current work, employment, and workplace",
        "example_el": "Δουλεύω ως προγραμματιστής στην Αθήνα.",
        "example_en": "I work as a developer in Athens.",
        "notes_or_mnemonics": "Standard Type A active verb (-ω, -εις, -ει, -ουμε, -ετε, -ουν). Synonym of εργάζομαι."
    },
    {
        "id": "A1-U03-034",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "verb",
        "front": "σπουδάζω",
        "back_primary": "to study (academic field)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό σπουδάζει",
            "first_person_plural": "εμείς σπουδάζουμε"
        },
        "keg_communicative_function": "Talking about university majors and fields of study",
        "example_el": "Σπουδάζω αρχιτεκτονική στο πολυτεχνείο.",
        "example_en": "I am studying architecture at the polytechnic.",
        "notes_or_mnemonics": "Distinct from 'διαβάζω' (to read / do homework): 'σπουδάζω' means enrolled in higher education studies."
    },
    {
        "id": "A1-U03-035",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "numeral",
        "front": "μηδέν",
        "back_primary": "zero (0)",
        "grammatical_info": {
            "part_of_speech": "cardinal numeral (indeclinable)",
            "value": 0
        },
        "keg_communicative_function": "Dictating and reading phone numbers and postal codes",
        "example_el": "Το τηλέφωνό μου αρχίζει από μηδέν.",
        "example_en": "My phone number starts with zero.",
        "notes_or_mnemonics": "Oxytone indeclinable numeral."
    },
    {
        "id": "A1-U03-036",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "numeral",
        "front": "ένας, μία / μια, ένα",
        "back_primary": "one (1) / a / an",
        "grammatical_info": {
            "part_of_speech": "cardinal numeral / indefinite article",
            "forms": "ένας (masculine), μία/μια (feminine), ένα (neuter)",
            "accusative": "έναν / ένα (m), μία/μια (f), ένα (n)"
        },
        "keg_communicative_function": "Counting units and serving as the indefinite article",
        "example_el": "Έχω έναν αδελφό και μία αδελφή.",
        "example_en": "I have one brother and one sister.",
        "notes_or_mnemonics": "The numbers 1, 3, 4 inflect for gender in Modern Greek. Masculine accusative is 'έναν' before vowels/plosives."
    },
    {
        "id": "A1-U03-037",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "numeral",
        "front": "δέκα",
        "back_primary": "ten (10)",
        "grammatical_info": {
            "part_of_speech": "cardinal numeral (indeclinable)",
            "value": 10
        },
        "keg_communicative_function": "Stating quantities, street numbers, and dates",
        "example_el": "Μένω στον αριθμό δέκα.",
        "example_en": "I live at number ten.",
        "notes_or_mnemonics": "Indeclinable cardinal numeral."
    },
    {
        "id": "A1-U03-038",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "numeral",
        "front": "είκοσι",
        "back_primary": "twenty (20)",
        "grammatical_info": {
            "part_of_speech": "cardinal numeral (indeclinable)",
            "value": 20
        },
        "keg_communicative_function": "Telling age, prices, and contact details",
        "example_el": "Είμαι είκοσι χρονών.",
        "example_en": "I am twenty years old.",
        "notes_or_mnemonics": "Indeclinable cardinal base for numbers 21-29 (είκοσι ένα, είκοσι δύο...)."
    },
    {
        "id": "A1-U03-039",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "numeral",
        "front": "εκατό",
        "back_primary": "one hundred (100)",
        "grammatical_info": {
            "part_of_speech": "cardinal numeral (indeclinable)",
            "value": 100,
            "euphonic_variant": "εκατόν (before vowels in compounds, e.g. εκατόν ένα)"
        },
        "keg_communicative_function": "Reading three-digit numbers, prices, and street addresses",
        "example_el": "Το εισιτήριο κάνει εκατό ευρώ.",
        "example_en": "The ticket costs one hundred euros.",
        "notes_or_mnemonics": "Takes final -ν in compound numerals starting with a vowel: εκατόν ένα (101), εκατόν οκτώ (108)."
    },
    {
        "id": "A1-U03-040",
        "unit_number": 3,
        "unit_theme": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "card_type": "adverb",
        "front": "πού",
        "back_primary": "where",
        "grammatical_info": {
            "part_of_speech": "interrogative adverb"
        },
        "keg_communicative_function": "Asking for workplace, residence, and geographical location",
        "example_el": "Πού δουλεύετε;",
        "example_en": "Where do you work?",
        "notes_or_mnemonics": "Must always be written with a written accent (τόνος) in questions to distinguish from the relative pronoun 'που'."
    },

    # =========================================================================
    # UNIT 4: Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)
    # =========================================================================
    {
        "id": "A1-U04-001",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "η οικογένεια",
        "back_primary": "family",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι οικογένειες",
            "accusative_singular": "την οικογένεια"
        },
        "keg_communicative_function": "Introducing and discussing family composition",
        "example_el": "Έχω μία μεγάλη οικογένεια.",
        "example_en": "I have a big family.",
        "notes_or_mnemonics": "Feminine in -εια (plural: οι οικογένειες). Theme word for KEG personal description emails."
    },
    {
        "id": "A1-U04-002",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "οι γονείς",
        "back_primary": "parents",
        "grammatical_info": {
            "part_of_speech": "noun (masculine plural)",
            "plural": "οι γονείς",
            "accusative_plural": "τους γονείς"
        },
        "keg_communicative_function": "Talking about father and mother collectively",
        "example_el": "Οι γονείς μου μένουν στη Θεσσαλονίκη.",
        "example_en": "My parents live in Thessaloniki.",
        "notes_or_mnemonics": "Plural noun in -είς. Accusative plural is 'τους γονείς'."
    },
    {
        "id": "A1-U04-003",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "ο πατέρας",
        "back_primary": "father",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι πατέρες",
            "accusative_singular": "τον πατέρα"
        },
        "keg_communicative_function": "Identifying one's father in family descriptions",
        "example_el": "Ο πατέρας μου είναι γιατρός.",
        "example_en": "My father is a doctor.",
        "notes_or_mnemonics": "Paroxytone masculine in -ας (plural: οι πατέρες). Accusative drops final -ς: τον πατέρα."
    },
    {
        "id": "A1-U04-004",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "η μητέρα",
        "back_primary": "mother",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι μητέρες",
            "accusative_singular": "τη μητέρα"
        },
        "keg_communicative_function": "Identifying one's mother in family descriptions",
        "example_el": "Η μητέρα μου είναι δασκάλα.",
        "example_en": "My mother is a teacher.",
        "notes_or_mnemonics": "Paroxytone feminine in -α (plural: οι μητέρες)."
    },
    {
        "id": "A1-U04-005",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "ο μπαμπάς",
        "back_primary": "dad / papa",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι μπαμπάδες",
            "accusative_singular": "τον μπαμπά"
        },
        "keg_communicative_function": "Informal and affectionate reference to father",
        "example_el": "Ο μπαμπάς μου μαγειρεύει πολύ καλά.",
        "example_en": "My dad cooks very well.",
        "notes_or_mnemonics": "Oxytone masculine in -άς; forms plural with suffix -άδες (οι μπαμπάδες)."
    },
    {
        "id": "A1-U04-006",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "η μαμά",
        "back_primary": "mom / mama",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι μαμάδες",
            "accusative_singular": "τη μαμά"
        },
        "keg_communicative_function": "Informal and affectionate reference to mother",
        "example_el": "Η μαμά μου είναι πολύ γλυκιά.",
        "example_en": "My mom is very sweet.",
        "notes_or_mnemonics": "Oxytone feminine in -ά; plural takes suffix -άδες (οι μαμάδες)."
    },
    {
        "id": "A1-U04-007",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "ο γιος",
        "back_primary": "son",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι γιοι",
            "accusative_singular": "τον γιο"
        },
        "keg_communicative_function": "Describing offspring (male child)",
        "example_el": "Έχουν έναν γιο και μία κόρη.",
        "example_en": "They have a son and a daughter.",
        "notes_or_mnemonics": "Monosyllabic masculine with diphthong (ο γιος, οι γιοι, τους γιους)."
    },
    {
        "id": "A1-U04-008",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "η κόρη",
        "back_primary": "daughter",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι κόρες",
            "accusative_singular": "την κόρη"
        },
        "keg_communicative_function": "Describing offspring (female child)",
        "example_el": "Η κόρη τους σπουδάζει στην Αγγλία.",
        "example_en": "Their daughter is studying in England.",
        "notes_or_mnemonics": "Paroxytone feminine in -η with plural in -ες (οι κόρες)."
    },
    {
        "id": "A1-U04-009",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "ο αδελφός / ο αδερφός",
        "back_primary": "brother",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι αδελφοί / οι αδερφοί",
            "accusative_singular": "τον αδελφό / τον αδερφό"
        },
        "keg_communicative_function": "Identifying male siblings",
        "example_el": "Ο αδελφός μου είναι είκοσι πέντε χρονών.",
        "example_en": "My brother is twenty-five years old.",
        "notes_or_mnemonics": "Both forms 'αδελφός' (formal/written) and 'αδερφός' (spoken/demotic) are standard in Greece."
    },
    {
        "id": "A1-U04-010",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "η αδελφή / η αδερφή",
        "back_primary": "sister",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι αδελφές / οι αδερφές",
            "accusative_singular": "την αδελφή / την αδερφή"
        },
        "keg_communicative_function": "Identifying female siblings",
        "example_el": "Η αδελφή μου δουλεύει σε τράπεζα.",
        "example_en": "My sister works at a bank.",
        "notes_or_mnemonics": "Oxytone feminine in -ή (plural in -ές)."
    },
    {
        "id": "A1-U04-011",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "ο παππούς",
        "back_primary": "grandfather",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι παππούδες",
            "accusative_singular": "τον παππού"
        },
        "keg_communicative_function": "Talking about grandparents and elderly family members",
        "example_el": "Ο παππούς μου είναι εβδομήντα χρονών.",
        "example_en": "My grandfather is seventy years old.",
        "notes_or_mnemonics": "Spelled with double π (ππ). Plural forms in -ούδες: οι παππούδες."
    },
    {
        "id": "A1-U04-012",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "η γιαγιά",
        "back_primary": "grandmother",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι γιαγιάδες",
            "accusative_singular": "τη γιαγιά"
        },
        "keg_communicative_function": "Talking about grandmother",
        "example_el": "Η γιαγιά μου φτιάχνει τέλεια πίτα.",
        "example_en": "My grandmother makes perfect pie.",
        "notes_or_mnemonics": "Oxytone feminine with plural in -άδες (οι γιαγιάδες)."
    },
    {
        "id": "A1-U04-013",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "το παιδί",
        "back_primary": "child / kid",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα παιδιά",
            "accusative_singular": "το παιδί"
        },
        "keg_communicative_function": "Referring to children or family dependents",
        "example_el": "Έχουν δύο παιδιά.",
        "example_en": "They have two children.",
        "notes_or_mnemonics": "Oxytone neuter in -ί (plural: τα παιδιά). Colloquially used among young adults: 'Γεια σας, παιδιά!' (Hi guys!)."
    },
    {
        "id": "A1-U04-014",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "το μωρό",
        "back_primary": "baby / infant",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μωρά",
            "accusative_singular": "το μωρό"
        },
        "keg_communicative_function": "Referring to infants and very young children",
        "example_el": "Το μωρό κοιμάται τώρα.",
        "example_en": "The baby is sleeping right now.",
        "notes_or_mnemonics": "Oxytone neuter in -ό with plural in -ά (τα μωρά)."
    },
    {
        "id": "A1-U04-015",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "ο άντρας",
        "back_primary": "man / husband",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι άντρες",
            "accusative_singular": "τον άντρα"
        },
        "keg_communicative_function": "Referring to an adult male or one's husband",
        "example_el": "Ο άντρας της είναι αρχιτέκτονας.",
        "example_en": "Her husband is an architect.",
        "notes_or_mnemonics": "Paroxytone masculine in -ας. Context determines whether it means 'man' or 'husband'."
    },
    {
        "id": "A1-U04-016",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "η γυναίκα",
        "back_primary": "woman / wife",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι γυναίκες",
            "accusative_singular": "τη γυναίκα"
        },
        "keg_communicative_function": "Referring to an adult female or one's wife",
        "example_el": "Η γυναίκα μου δουλεύει στο πανεπιστήμιο.",
        "example_en": "My wife works at the university.",
        "notes_or_mnemonics": "Paroxytone feminine in -α. Context determines whether it means 'woman' or 'wife'."
    },
    {
        "id": "A1-U04-017",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "ο θείος",
        "back_primary": "uncle",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι θείοι",
            "accusative_singular": "τον θείο"
        },
        "keg_communicative_function": "Describing extended family relations",
        "example_el": "Ο θείος μου μένει στην Κρήτη.",
        "example_en": "My uncle lives in Crete.",
        "notes_or_mnemonics": "Regular masculine in -ος (plural: οι θείοι)."
    },
    {
        "id": "A1-U04-018",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "η θεία",
        "back_primary": "aunt",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι θείες",
            "accusative_singular": "τη θεία"
        },
        "keg_communicative_function": "Describing extended family relations",
        "example_el": "Η θεία Ελένη έχει τρία παιδιά.",
        "example_en": "Aunt Eleni has three children.",
        "notes_or_mnemonics": "Feminine counterpart of ο θείος."
    },
    {
        "id": "A1-U04-019",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "ο ξάδελφος / ο ξάδερφος",
        "back_primary": "cousin (male)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι ξάδελφοι / οι ξάδερφοι",
            "accusative_singular": "τον ξάδελφο / τον ξάδερφο"
        },
        "keg_communicative_function": "Describing extended family members",
        "example_el": "Ο ξάδελφός μου σπουδάζει πληροφορική.",
        "example_en": "My cousin is studying computer science.",
        "notes_or_mnemonics": "Both forms 'ξάδελφος' and 'ξάδερφος' are standard. Takes second accent with clitic: ο ξάδελφός μου."
    },
    {
        "id": "A1-U04-020",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "η ξαδέλφη / η ξαδέρφη",
        "back_primary": "cousin (female)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ξαδέλφες / οι ξαδέρφες",
            "accusative_singular": "την ξαδέλφη / την ξαδέρφη"
        },
        "keg_communicative_function": "Describing female cousins",
        "example_el": "Η ξαδέλφη μου μένει δίπλα στο σπίτι μας.",
        "example_en": "My cousin lives next to our house.",
        "notes_or_mnemonics": "Feminine form in -η (plural: οι ξαδέλφες)."
    },
    {
        "id": "A1-U04-021",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "ο άνθρωπος",
        "back_primary": "human being / person / man",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι άνθρωποι",
            "accusative_singular": "τον άνθρωπο"
        },
        "keg_communicative_function": "Referring to persons in general",
        "example_el": "Είναι πολύ καλός άνθρωπος.",
        "example_en": "He is a very good person.",
        "notes_or_mnemonics": "Proparoxytone masculine in -ος (root of English 'anthropology')."
    },
    {
        "id": "A1-U04-022",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "adjective",
        "front": "παντρεμένος, -η, -ο",
        "back_primary": "married",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "παντρεμένη",
            "neuter": "παντρεμένο",
            "plural": "παντρεμένοι, παντρεμένες, παντρεμένα"
        },
        "keg_communicative_function": "Stating marital status on questionnaires and forms",
        "example_el": "Είστε παντρεμένος ή ελεύθερος;",
        "example_en": "Are you married or single?",
        "notes_or_mnemonics": "Participle used as descriptive adjective of marital status (οικογενειακή κατάσταση)."
    },
    {
        "id": "A1-U04-023",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "adjective",
        "front": "ελεύθερος, -η, -ο",
        "back_primary": "single (unmarried) / free",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "ελεύθερη",
            "neuter": "ελεύθερο",
            "plural": "ελεύθεροι, ελεύθερες, ελεύθερα"
        },
        "keg_communicative_function": "Indicating single marital status",
        "example_el": "Ο αδελφός μου είναι ακόμη ελεύθερος.",
        "example_en": "My brother is still single.",
        "notes_or_mnemonics": "Standard demographic term for 'single / unmarried' on Greek registration forms."
    },
    {
        "id": "A1-U04-024",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "το πρόσωπο",
        "back_primary": "face / person",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πρόσωπα",
            "accusative_singular": "το πρόσωπο"
        },
        "keg_communicative_function": "Describing facial features and physical appearance",
        "example_el": "Έχει πολύ γλυκό πρόσωπο.",
        "example_en": "He/she has a very sweet face.",
        "notes_or_mnemonics": "Proparoxytone neuter in -ο. Takes second accent with possessive: το πρόσωπό του."
    },
    {
        "id": "A1-U04-025",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "τα μαλλιά",
        "back_primary": "hair (on head)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter plural)",
            "plural": "τα μαλλιά",
            "accusative_plural": "τα μαλλιά"
        },
        "keg_communicative_function": "Describing hair color and style in physical descriptions",
        "example_el": "Η Ελένη έχει μακριά καστανά μαλλιά.",
        "example_en": "Eleni has long brown hair.",
        "notes_or_mnemonics": "Modern Greek expresses head hair in the plural neuter (τα μαλλιά)."
    },
    {
        "id": "A1-U04-026",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "vocabulary",
        "front": "τα μάτια",
        "back_primary": "eyes",
        "grammatical_info": {
            "part_of_speech": "noun (neuter plural)",
            "plural": "τα μάτια",
            "accusative_plural": "τα μάτια"
        },
        "keg_communicative_function": "Describing eye color in person descriptions",
        "example_el": "Ο γιος μου έχει μπλε μάτια.",
        "example_en": "My son has blue eyes.",
        "notes_or_mnemonics": "Neuter plural of 'το μάτι'. Common colors: μπλε (blue), πράσινα (green), καστανά (brown)."
    },
    {
        "id": "A1-U04-027",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "adjective",
        "front": "ψηλός, -ή, -ό",
        "back_primary": "tall / high",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "ψηλή",
            "neuter": "ψηλό",
            "plural": "ψηλοί, ψηλές, ψηλά"
        },
        "keg_communicative_function": "Describing height and stature",
        "example_el": "Ο πατέρας μου είναι ψηλός άντρας.",
        "example_en": "My father is a tall man.",
        "notes_or_mnemonics": "Oxytone adjective. Spelled with ψι (ψ) + ήτα (η)."
    },
    {
        "id": "A1-U04-028",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "adjective",
        "front": "κοντός, -ή, -ό",
        "back_primary": "short (stature / length)",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "κοντή",
            "neuter": "κοντό",
            "plural": "κοντοί, κοντές, κοντά"
        },
        "keg_communicative_function": "Describing physical height",
        "example_el": "Η αδελφή μου είναι λίγο κοντή.",
        "example_en": "My sister is a little short.",
        "notes_or_mnemonics": "Direct antonym of ψηλός."
    },
    {
        "id": "A1-U04-029",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "adjective",
        "front": "αδύνατος, -η, -ο",
        "back_primary": "thin / slim / weak",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "αδύνατη",
            "neuter": "αδύνατο",
            "plural": "αδύνατοι, αδύνατες, αδύνατα"
        },
        "keg_communicative_function": "Describing slender build or body type",
        "example_el": "Ο Νίκος είναι ψηλός και αδύνατος.",
        "example_en": "Nikos is tall and slim.",
        "notes_or_mnemonics": "Proparoxytone adjective in -ος, -η, -ο. Alpha-privative: α- + δυνατός (not strong / thin)."
    },
    {
        "id": "A1-U04-030",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "adjective",
        "front": "χοντρός, -ή, -ό",
        "back_primary": "stout / heavy-set / thick",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "χοντρή",
            "neuter": "χοντρό",
            "plural": "χοντροί, χοντρές, χοντρά"
        },
        "keg_communicative_function": "Describing body build or thick objects",
        "example_el": "Φοράει ένα χοντρό παλτό.",
        "example_en": "He/she is wearing a thick coat.",
        "notes_or_mnemonics": "Oxytone regular adjective."
    },
    {
        "id": "A1-U04-031",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "adjective",
        "front": "όμορφος, -η, -ο",
        "back_primary": "beautiful / handsome / pretty",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "όμορφη",
            "neuter": "όμορφο",
            "plural": "όμορφοι, όμορφες, όμορφα"
        },
        "keg_communicative_function": "Describing attractive appearance of persons or places",
        "example_el": "Η μητέρα της είναι πολύ όμορφη γυναίκα.",
        "example_en": "Her mother is a very beautiful woman.",
        "notes_or_mnemonics": "Proparoxytone adjective (accent on first syllable ό-)."
    },
    {
        "id": "A1-U04-032",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "adjective",
        "front": "νέος, -α, -ο",
        "back_primary": "young / new",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "νέα",
            "neuter": "νέο",
            "plural": "νέοι, νέες, νέα"
        },
        "keg_communicative_function": "Talking about age and novelty",
        "example_el": "Ο καθηγητής μας είναι αρκετά νέος.",
        "example_en": "Our professor is quite young.",
        "notes_or_mnemonics": "Feminine ends in -α (νέα) because a vowel precedes the ending."
    },
    {
        "id": "A1-U04-033",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "adjective",
        "front": "μεγάλος, -η, -ο",
        "back_primary": "elderly / old (in age) / big",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "μεγάλη",
            "neuter": "μεγάλο",
            "plural": "μεγάλοι, μεγάλες, μεγάλα"
        },
        "keg_communicative_function": "Describing older age or large size",
        "example_el": "Ο παππούς μου είναι μεγάλος άνθρωπος.",
        "example_en": "My grandfather is an elderly person.",
        "notes_or_mnemonics": "When referring to people, 'μεγάλος' is the polite way to say older/elderly (rather than γέρος)."
    },
    {
        "id": "A1-U04-034",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "adjective",
        "front": "καλός, -ή, -ό",
        "back_primary": "good / kind-hearted",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "καλή",
            "neuter": "καλό",
            "plural": "καλοί, καλές, καλά"
        },
        "keg_communicative_function": "Expressing positive character and quality evaluation",
        "example_el": "Είναι πολύ καλοί φίλοι.",
        "example_en": "They are very good friends.",
        "notes_or_mnemonics": "Base oxytone adjective used in numerous daily formulas (καλημέρα, καλό ταξίδι)."
    },
    {
        "id": "A1-U04-035",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "adjective",
        "front": "συμπαθητικός, -ή, -ό",
        "back_primary": "pleasant / likeable / friendly",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "συμπαθητική",
            "neuter": "συμπαθητικό",
            "plural": "συμπαθητικοί, συμπαθητικές, συμπαθητικά"
        },
        "keg_communicative_function": "Describing agreeable personality traits",
        "example_el": "Η νέα γειτόνισσα είναι πολύ συμπαθητική.",
        "example_en": "The new neighbor is very likeable.",
        "notes_or_mnemonics": "False friend: means 'likeable/pleasant', not 'feeling pity/sympathy'."
    },
    {
        "id": "A1-U04-036",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "verb",
        "front": "έχω",
        "back_primary": "to have / I have",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό έχει",
            "first_person_plural": "εμείς έχουμε"
        },
        "keg_communicative_function": "Expressing family relations, age, and possession",
        "example_el": "Έχω δύο αδέλφια και έναν σκύλο.",
        "example_en": "I have two siblings and a dog.",
        "notes_or_mnemonics": "Crucial verb for A1 personal descriptions. Present: έχω, έχεις, έχει, έχουμε, έχετε, έχουν."
    },
    {
        "id": "A1-U04-037",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "pronoun",
        "front": "μου",
        "back_primary": "my / of mine (possessive enclitic)",
        "grammatical_info": {
            "part_of_speech": "possessive clitic pronoun",
            "person_number": "1st person singular",
            "position": "post-nominal enclitic"
        },
        "keg_communicative_function": "Indicating family relations and personal ownership",
        "example_el": "Αυτή είναι η μητέρα μου.",
        "example_en": "This is my mother.",
        "notes_or_mnemonics": "Enclitic follows the noun. Causes a second accent if noun is proparoxytone: το αυτοκίνητό μου."
    },
    {
        "id": "A1-U04-038",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "pronoun",
        "front": "σου",
        "back_primary": "your / of yours (informal singular)",
        "grammatical_info": {
            "part_of_speech": "possessive clitic pronoun",
            "person_number": "2nd person singular",
            "position": "post-nominal enclitic"
        },
        "keg_communicative_function": "Inquiring about someone's family or possessions",
        "example_el": "Πώς λένε τον αδελφό σου;",
        "example_en": "What is your brother's name?",
        "notes_or_mnemonics": "Informal singular possessive clitic."
    },
    {
        "id": "A1-U04-039",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "pronoun",
        "front": "του / της / του",
        "back_primary": "his / her / its (possessive enclitic)",
        "grammatical_info": {
            "part_of_speech": "possessive clitic pronoun",
            "person_number": "3rd person singular",
            "forms": "του (masculine / neuter), της (feminine)"
        },
        "keg_communicative_function": "Expressing possession relating to a third person",
        "example_el": "Ο άντρας της είναι καθηγητής.",
        "example_en": "Her husband is a professor.",
        "notes_or_mnemonics": "Agrees with the possessor, not the possessed object: το σπίτι της (her house), το σπίτι του (his house)."
    },
    {
        "id": "A1-U04-040",
        "unit_number": 4,
        "unit_theme": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "card_type": "pronoun",
        "front": "μας / σας / τους",
        "back_primary": "our / your (polite/pl.) / their",
        "grammatical_info": {
            "part_of_speech": "possessive clitic pronoun",
            "person_number": "plural possessives",
            "forms": "μας (1st pl), σας (2nd pl/polite), τους (3rd pl)"
        },
        "keg_communicative_function": "Expressing group possession and polite address",
        "example_el": "Αυτός είναι ο καθηγητής μας.",
        "example_en": "This is our professor.",
        "notes_or_mnemonics": "'σας' is used politely to a single person: 'Ποιο είναι το τηλέφωνό σας;'."
    }
]

out_dir = Path("content")
out_dir.mkdir(exist_ok=True)
json_path = out_dir / "keg_a1_units_03_04.json"

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(cards, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(cards)} cards in {json_path}")

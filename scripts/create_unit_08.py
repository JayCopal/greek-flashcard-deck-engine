# -*- coding: utf-8 -*-
"""
Script to create Unit 8: Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)
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
UNIT_DIR = CONTENT_DIR / "unit-08"
UNIT_DIR.mkdir(parents=True, exist_ok=True)
YAML_PATH = UNIT_DIR / "lesson-01.yaml"
JSON_PATH = CONTENT_DIR / "keg_a1_units_08.json"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

cards_u8 = [
    # 1. Times of Day, Meals & Concepts of Routine
    {
        "id": "A1-U08-001",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "vocabulary",
        "front": "το πρόγραμμα",
        "back_primary": "schedule / daily routine / program",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα προγράμματα",
            "accusative_singular": "το πρόγραμμα"
        },
        "keg_communicative_function": "Describing daily schedule and daily time management",
        "example_el": "Το καθημερινό μου πρόγραμμα είναι πολύ γεμάτο.",
        "example_en": "My daily schedule is very full.",
        "notes_or_mnemonics": "Neuter noun in -μα with plural in -ματα (τα προγράμματα)."
    },
    {
        "id": "A1-U08-002",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "vocabulary",
        "front": "η συνήθεια",
        "back_primary": "habit / routine / custom",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι συνήθειες",
            "accusative_singular": "τη συνήθεια"
        },
        "keg_communicative_function": "Talking about personal habits and daily customs",
        "example_el": "Έχω τη συνήθεια να πίνω καφέ κάθε πρωί.",
        "example_en": "I have the habit of drinking coffee every morning.",
        "notes_or_mnemonics": "Proparoxytone feminine in -εια with plural in -ειες (οι συνήθειες)."
    },
    {
        "id": "A1-U08-003",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "vocabulary",
        "front": "το πρωί",
        "back_primary": "morning / in the morning",
        "grammatical_info": {
            "part_of_speech": "noun (neuter) / adverbial",
            "plural": "τα πρωινά",
            "accusative_singular": "το πρωί"
        },
        "keg_communicative_function": "Specifying morning time frames for routines",
        "example_el": "Το πρωί ξυπνάω στις επτά και παίρνω πρωινό.",
        "example_en": "In the morning I wake up at seven and have breakfast.",
        "notes_or_mnemonics": "Neuter noun in -ί. Functions adverbially with or without article ('το πρωί' = in the morning)."
    },
    {
        "id": "A1-U08-004",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "vocabulary",
        "front": "το μεσημέρι",
        "back_primary": "noon / midday / in the middle of the day",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μεσημέρια",
            "accusative_singular": "το μεσημέρι"
        },
        "keg_communicative_function": "Specifying midday lunch time and work breaks",
        "example_el": "Το μεσημέρι τρώμε μεσημεριανό με την οικογένεια.",
        "example_en": "At noon we eat lunch with the family.",
        "notes_or_mnemonics": "Compound from μέσος (middle) + ημέρα (day). Neuter in -ι (plural: τα μεσημέρια)."
    },
    {
        "id": "A1-U08-005",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "vocabulary",
        "front": "το απόγευμα",
        "back_primary": "afternoon / in the afternoon",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα απογεύματα",
            "accusative_singular": "το απόγευμα"
        },
        "keg_communicative_function": "Talking about late afternoon activities and study hours",
        "example_el": "Το απόγευμα διαβάζω ελληνικά και ακούω μουσική.",
        "example_en": "In the afternoon I study Greek and listen to music.",
        "notes_or_mnemonics": "Compound from από + γεύμα (after-meal time). Neuter in -μα (plural: τα απογεύματα)."
    },
    {
        "id": "A1-U08-006",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "vocabulary",
        "front": "το βράδυ",
        "back_primary": "evening / night / at night",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα βράδια",
            "accusative_singular": "το βράδυ"
        },
        "keg_communicative_function": "Describing evening relaxation, dinner, and social outings",
        "example_el": "Το βράδυ βγαίνω για φαγητό με φίλους.",
        "example_en": "In the evening I go out for dinner with friends.",
        "notes_or_mnemonics": "Irregular neuter noun ending in -υ with plural in -ια (τα βράδια)."
    },
    {
        "id": "A1-U08-007",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "vocabulary",
        "front": "η νύχτα",
        "back_primary": "night / nighttime",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι νύχτες",
            "accusative_singular": "τη νύχτα"
        },
        "keg_communicative_function": "Specifying late night hours or sleep periods",
        "example_el": "Τη νύχτα η πόλη είναι πολύ ήσυχη.",
        "example_en": "At night the city is very quiet.",
        "notes_or_mnemonics": "Feminine in -α with plural in -ες (οι νύχτες). 'Τη νύχτα' = during the night."
    },
    {
        "id": "A1-U08-008",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "vocabulary",
        "front": "το πρωινό",
        "back_primary": "breakfast",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πρωινά",
            "accusative_singular": "το πρωινό"
        },
        "keg_communicative_function": "Describing the first meal of the day",
        "example_el": "Για πρωινό τρώω φρυγανιές με μέλι και πίνω τσάι.",
        "example_en": "For breakfast I eat rusks with honey and drink tea.",
        "notes_or_mnemonics": "Substantivized neuter adjective (το πρωινό = breakfast, τα πρωινά = breakfasts / hotel breakfasts)."
    },
    {
        "id": "A1-U08-009",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "vocabulary",
        "front": "το μεσημεριανό",
        "back_primary": "lunch / midday meal",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μεσημεριανά",
            "accusative_singular": "το μεσημεριανό"
        },
        "keg_communicative_function": "Describing the main midday meal in Greece",
        "example_el": "Το μεσημεριανό στην Ελλάδα είναι συνήθως στις τρεις.",
        "example_en": "Lunch in Greece is usually at three o'clock.",
        "notes_or_mnemonics": "Neuter in -ό. In Greek culture, lunch is traditionally the main cooked meal of the day."
    },
    {
        "id": "A1-U08-010",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "vocabulary",
        "front": "το βραδινό",
        "back_primary": "dinner / supper / evening meal",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα βραδινά",
            "accusative_singular": "το βραδινό"
        },
        "keg_communicative_function": "Describing the evening meal",
        "example_el": "Τρώμε ελαφρύ βραδινό στις εννέα.",
        "example_en": "We eat a light dinner at nine.",
        "notes_or_mnemonics": "Substantivized neuter adjective (το βραδινό = dinner)."
    },
    {
        "id": "A1-U08-011",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "vocabulary",
        "front": "το διάλειμμα",
        "back_primary": "break / recess / pause",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα διαλείμματα",
            "accusative_singular": "το διάλειμμα"
        },
        "keg_communicative_function": "Talking about study pauses or coffee breaks at work",
        "example_el": "Στη δουλειά κάνουμε ένα μικρό διάλειμμα για καφέ.",
        "example_en": "At work we take a short break for coffee.",
        "notes_or_mnemonics": "Spelled with double μ (μμ). Plural: τα διαλείμματα."
    },
    {
        "id": "A1-U08-012",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "vocabulary",
        "front": "το μάθημα",
        "back_primary": "lesson / class / lecture",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μαθήματα",
            "accusative_singular": "το μάθημα"
        },
        "keg_communicative_function": "Talking about school, language classes, and university lectures",
        "example_el": "Το μάθημα των ελληνικών αρχίζει στις πέντε.",
        "example_en": "The Greek lesson starts at five.",
        "notes_or_mnemonics": "Neuter in -μα with plural in -ματα (τα μαθήματα)."
    },

    # 2. Daily Routine Verbs: Type A
    {
        "id": "A1-U08-013",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "verb",
        "front": "αρχίζω",
        "back_primary": "to begin / to start / I begin",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό αρχίζει",
            "first_person_plural": "εμείς αρχίζουμε"
        },
        "keg_communicative_function": "Stating starting times for work, classes, or films",
        "example_el": "Η δουλειά μου αρχίζει στις οκτώ το πρωί.",
        "example_en": "My work starts at eight in the morning.",
        "notes_or_mnemonics": "Standard Type A verb: αρχίζω, αρχίζεις, αρχίζει, αρχίζουμε, αρχίζετε, αρχίζουν."
    },
    {
        "id": "A1-U08-014",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "verb",
        "front": "τελειώνω",
        "back_primary": "to finish / to end / I finish",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό τελειώνει",
            "first_person_plural": "εμείς τελειώνουμε"
        },
        "keg_communicative_function": "Stating finishing times for daily activities",
        "example_el": "Τελειώνω το μάθημα στις δύο το μεσημέρι.",
        "example_en": "I finish the class at two in the afternoon.",
        "notes_or_mnemonics": "Direct antonym of 'αρχίζω'. Type A verb with diphthong -ει-."
    },
    {
        "id": "A1-U08-015",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "verb",
        "front": "διαβάζω",
        "back_primary": "to read / to study / I study",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό διαβάζει",
            "first_person_plural": "εμείς διαβάζουμε"
        },
        "keg_communicative_function": "Describing reading books, newspapers, or doing homework",
        "example_el": "Κάθε βράδυ διαβάζω ένα βιβλίο πριν τον ύπνο.",
        "example_en": "Every night I read a book before sleep.",
        "notes_or_mnemonics": "Type A verb. Means both 'to read' (διαβάζω εφημερίδα) and 'to study for class' (διαβάζω για το μάθημα)."
    },
    {
        "id": "A1-U08-016",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "verb",
        "front": "ακούω",
        "back_primary": "to listen to / to hear / I listen",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό ακούει",
            "first_person_plural": "εμείς ακούμε"
        },
        "keg_communicative_function": "Talking about listening to music, radio, or podcasts",
        "example_el": "Ακούω ραδιόφωνο όταν οδηγώ.",
        "example_en": "I listen to the radio when I drive.",
        "notes_or_mnemonics": "Type A verb with vowel stem: ακούω, ακούς, ακούει, ακούμε, ακούτε, ακούν(ε)."
    },
    {
        "id": "A1-U08-017",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "verb",
        "front": "βλέπω",
        "back_primary": "to watch / to see / I watch",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό βλέπει",
            "first_person_plural": "εμείς βλέπουμε"
        },
        "keg_communicative_function": "Talking about watching television, movies, or seeing friends",
        "example_el": "Τα απογεύματα βλέπω μία ελληνική σειρά.",
        "example_en": "In the afternoons I watch a Greek TV series.",
        "notes_or_mnemonics": "Type A active verb: βλέπω, βλέπεις, βλέπει, βλέπουμε, βλέπετε, βλέπουν."
    },
    {
        "id": "A1-U08-018",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "verb",
        "front": "μαγειρεύω",
        "back_primary": "to cook / to prepare food / I cook",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό μαγειρεύει",
            "first_person_plural": "εμείς μαγειρεύουμε"
        },
        "keg_communicative_function": "Describing cooking habits at home",
        "example_el": "Μαγειρεύω ελληνικά φαγητά για τους φίλους μου.",
        "example_en": "I cook Greek dishes for my friends.",
        "notes_or_mnemonics": "Type A verb with suffix -εύω: μαγειρεύω, μαγειρεύεις, μαγειρεύει, μαγειρεύουμε."
    },
    {
        "id": "A1-U08-019",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "verb",
        "front": "φεύγω",
        "back_primary": "to leave / to depart / I leave",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό φεύγει",
            "first_person_plural": "εμείς φεύγουμε"
        },
        "keg_communicative_function": "Stating departure times from home or work",
        "example_el": "Φεύγω από το σπίτι στις επτά και μισή.",
        "example_en": "I leave the house at half past seven.",
        "notes_or_mnemonics": "Type A verb. Governs 'από + Accusative' for departure point: φεύγω από τη δουλειά."
    },
    {
        "id": "A1-U08-020",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "verb",
        "front": "γυρίζω",
        "back_primary": "to return / to come back / to turn",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό γυρίζει",
            "first_person_plural": "εμείς γυρίζουμε"
        },
        "keg_communicative_function": "Describing returning home after work or study",
        "example_el": "Γυρίζω στο σπίτι κατά τις έξι το απόγευμα.",
        "example_en": "I return home around six in the afternoon.",
        "notes_or_mnemonics": "Type A verb. Synonym of 'επιστρέφω'. Formula: γυρίζω στο σπίτι (return home)."
    },
    {
        "id": "A1-U08-021",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "verb",
        "front": "ψωνίζω",
        "back_primary": "to shop / to buy groceries / I shop",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό ψωνίζει",
            "first_person_plural": "εμείς ψωνίζουμε"
        },
        "keg_communicative_function": "Talking about regular grocery or weekly shopping",
        "example_el": "Ψωνίζω τρόφιμα από τη λαϊκή κάθε Τρίτη.",
        "example_en": "I shop for groceries at the street market every Tuesday.",
        "notes_or_mnemonics": "Type A verb: ψωνίζω, ψωνίζεις, ψωνίζει. Derived from 'τα ψώνια' (purchases/shopping)."
    },

    # 3. Daily Routine Verbs: Type B1 (-άω / -ώ)
    {
        "id": "A1-U08-022",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "verb",
        "front": "ξυπνάω / ξυπνώ",
        "back_primary": "to wake up / I wake up",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "B1",
            "third_person_singular": "αυτός / αυτή / αυτό ξυπνάει (ξυπνά)",
            "first_person_plural": "εμείς ξυπνάμε"
        },
        "keg_communicative_function": "Describing the start of the morning routine",
        "example_el": "Τις καθημερινές ξυπνάω πολύ νωρίς.",
        "example_en": "On weekdays I wake up very early.",
        "notes_or_mnemonics": "Contracted Type B1 verb: ξυπνάω/-ώ, ξυπνάς, ξυπνάει/-ά, ξυπνάμε, ξυπνάτε, ξυπνάνε/-ούν."
    },
    {
        "id": "A1-U08-023",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "verb",
        "front": "περπατάω / περπατώ",
        "back_primary": "to walk / I walk",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "B1",
            "third_person_singular": "αυτός / αυτή / αυτό περπατάει (περπατά)",
            "first_person_plural": "εμείς περπατάμε"
        },
        "keg_communicative_function": "Describing walking to work, school, or for exercise",
        "example_el": "Περπατάω σαράντα λεπτά στο πάρκο κάθε απόγευμα.",
        "example_en": "I walk for forty minutes in the park every afternoon.",
        "notes_or_mnemonics": "Type B1 verb: περπατάω, περπατάς, περπατάει, περπατάμε, περπατάτε, περπατάνε."
    },
    {
        "id": "A1-U08-024",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "verb",
        "front": "τραγουδάω / τραγουδώ",
        "back_primary": "to sing / I sing",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "B1",
            "third_person_singular": "αυτός / αυτή / αυτό τραγουδάει (τραγουδά)",
            "first_person_plural": "εμείς τραγουδάμε"
        },
        "keg_communicative_function": "Talking about leisure and musical hobbies",
        "example_el": "Τραγουδάμε ελληνικά τραγούδια στο μάθημα.",
        "example_en": "We sing Greek songs in class.",
        "notes_or_mnemonics": "Type B1 contracted active verb."
    },

    # 4. Daily Routine Verbs: Type B2 (-ώ, -είς)
    {
        "id": "A1-U08-025",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "verb",
        "front": "οδηγώ",
        "back_primary": "to drive / I drive",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "B2",
            "third_person_singular": "αυτός / αυτή / αυτό οδηγεί",
            "first_person_plural": "εμείς οδηγούμε"
        },
        "keg_communicative_function": "Talking about commuting by car",
        "example_el": "Οδηγώ προσεκτικά όταν έχει κίνηση στους δρόμους.",
        "example_en": "I drive carefully when there is traffic on the roads.",
        "notes_or_mnemonics": "Type B2 verb: οδηγώ, οδηγείς, οδηγεί, οδηγούμε, οδηγείτε, οδηγούν."
    },
    {
        "id": "A1-U08-026",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "verb",
        "front": "ζω",
        "back_primary": "to live / to reside / I live",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "B2",
            "third_person_singular": "αυτός / αυτή / αυτό ζει",
            "first_person_plural": "εμείς ζούμε"
        },
        "keg_communicative_function": "Talking about lifestyle and city of residence",
        "example_el": "Ζω στην Αθήνα εδώ και δύο χρόνια.",
        "example_en": "I live in Athens for two years now.",
        "notes_or_mnemonics": "Monosyllabic Type B2 verb: ζω, ζεις, ζει, ζούμε, ζείτε, ζουν."
    },
    {
        "id": "A1-U08-027",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "verb",
        "front": "μπορώ",
        "back_primary": "to be able to / can / I can",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "B2",
            "third_person_singular": "αυτός / αυτή / αυτό μπορεί",
            "first_person_plural": "εμείς μπορούμε"
        },
        "keg_communicative_function": "Expressing ability or making polite requests with 'μπορώ να...'",
        "example_el": "Μπορώ να μιλήσω λίγο ελληνικά τώρα.",
        "example_en": "I can speak a little Greek now.",
        "notes_or_mnemonics": "Key modal auxiliary: μπορώ, μπορείς, μπορεί, μπορούμε, μπορείτε, μπορούν. Triggers 'να + verb'."
    },

    # 5. Core Routine Active Verbal Phrases (Avoiding Mediopassive)
    {
        "id": "A1-U08-028",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "phrase",
        "front": "παίρνω πρωινό",
        "back_primary": "to have breakfast",
        "grammatical_info": {
            "part_of_speech": "phrase (routine)",
            "verb_involved": "παίρνω (Type A)"
        },
        "keg_communicative_function": "Describing morning eating routine",
        "example_el": "Παίρνω πρωινό στην κουζίνα πριν φύγω για τη δουλειά.",
        "example_en": "I have breakfast in the kitchen before I leave for work.",
        "notes_or_mnemonics": "Standard active colloquial formula for eating breakfast in Greek."
    },
    {
        "id": "A1-U08-029",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "phrase",
        "front": "κάνω μπάνιο / κάνω ντους",
        "back_primary": "to take a bath / to take a shower",
        "grammatical_info": {
            "part_of_speech": "phrase (routine)",
            "verb_involved": "κάνω (Type A)"
        },
        "keg_communicative_function": "Describing personal hygiene routine actively",
        "example_el": "Κάνω ένα γρήγορο ντους κάθε πρωί.",
        "example_en": "I take a quick shower every morning.",
        "notes_or_mnemonics": "Active periphrastic alternative to the mediopassive verb (πλένομαι), preferred in CEFR A1 standards."
    },
    {
        "id": "A1-U08-030",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "phrase",
        "front": "κάνω γυμναστική",
        "back_primary": "to exercise / to work out",
        "grammatical_info": {
            "part_of_speech": "phrase (routine)",
            "verb_involved": "κάνω (Type A)"
        },
        "keg_communicative_function": "Describing health and fitness routines",
        "example_el": "Κάνω γυμναστική τρεις φορές την εβδομάδα.",
        "example_en": "I work out three times a week.",
        "notes_or_mnemonics": "Universal daily expression: κάνω γυμναστική (to do gymnastics/fitness)."
    },
    {
        "id": "A1-U08-031",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "phrase",
        "front": "κάνω διάλειμμα",
        "back_primary": "to take a break",
        "grammatical_info": {
            "part_of_speech": "phrase (routine)",
            "verb_involved": "κάνω (Type A)"
        },
        "keg_communicative_function": "Describing pauses during work or study",
        "example_el": "Κάνουμε διάλειμμα για δέκα λεπτά.",
        "example_en": "We are taking a break for ten minutes.",
        "notes_or_mnemonics": "Formula: 'κάνω διάλειμμα'."
    },
    {
        "id": "A1-U08-032",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "phrase",
        "front": "πάω για ύπνο",
        "back_primary": "to go to sleep / to go to bed",
        "grammatical_info": {
            "part_of_speech": "phrase (routine)",
            "verb_involved": "πάω / πηγαίνω (irregular)"
        },
        "keg_communicative_function": "Describing bedtime routine",
        "example_el": "Πάω για ύπνο στις έντεκα το βράδυ.",
        "example_en": "I go to bed at eleven in the evening.",
        "notes_or_mnemonics": "Active equivalent for going to bed (literally: 'I go for sleep')."
    },

    # 6. Adverbs of Frequency & Temporal Markers
    {
        "id": "A1-U08-033",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "adverb",
        "front": "πάντα",
        "back_primary": "always",
        "grammatical_info": {
            "part_of_speech": "adverb (frequency)",
            "scale": "100% frequency"
        },
        "keg_communicative_function": "Expressing actions that occur consistently without exception",
        "example_el": "Πίνω πάντα έναν καφέ πριν φύγω.",
        "example_en": "I always drink a coffee before I leave.",
        "notes_or_mnemonics": "Paroxytone adverb. Contrasted with 'ποτέ' (never)."
    },
    {
        "id": "A1-U08-034",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "adverb",
        "front": "συνήθως",
        "back_primary": "usually / typically / normally",
        "grammatical_info": {
            "part_of_speech": "adverb (frequency)",
            "scale": "~80% frequency"
        },
        "keg_communicative_function": "Expressing habitual routine actions",
        "example_el": "Συνήθως τρώω μεσημεριανό στο σπίτι.",
        "example_en": "I usually eat lunch at home.",
        "notes_or_mnemonics": "Proparoxytone adverb with accent on υ (συνήθως)."
    },
    {
        "id": "A1-U08-035",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "adverb",
        "front": "συχνά",
        "back_primary": "often / frequently",
        "grammatical_info": {
            "part_of_speech": "adverb (frequency)",
            "scale": "~60% frequency"
        },
        "keg_communicative_function": "Expressing high recurrence of an action",
        "example_el": "Πηγαίνουμε συχνά στον κινηματογράφο το Σάββατο.",
        "example_en": "We often go to the cinema on Saturday.",
        "notes_or_mnemonics": "Oxytone adverb. Direct antonym of 'σπάνια' (rarely)."
    },
    {
        "id": "A1-U08-036",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "phrase",
        "front": "μερικές φορές",
        "back_primary": "sometimes / occasionally",
        "grammatical_info": {
            "part_of_speech": "phrase (frequency)",
            "scale": "~40% frequency"
        },
        "keg_communicative_function": "Expressing intermediate or occasional activities",
        "example_el": "Μερικές φορές δουλεύω από το σπίτι.",
        "example_en": "Sometimes I work from home.",
        "notes_or_mnemonics": "Adverbial phrase: μερικές (some) + φορές (times)."
    },
    {
        "id": "A1-U08-037",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "adverb",
        "front": "σπάνια",
        "back_primary": "rarely / seldom",
        "grammatical_info": {
            "part_of_speech": "adverb (frequency)",
            "scale": "~10% frequency"
        },
        "keg_communicative_function": "Expressing activities done with very low frequency",
        "example_el": "Τρώμε σπάνια γλυκά.",
        "example_en": "We rarely eat sweets.",
        "notes_or_mnemonics": "Paroxytone adverb. Opposite of 'συχνά'."
    },
    {
        "id": "A1-U08-038",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "adverb",
        "front": "ποτέ",
        "back_primary": "never (with negation 'δεν')",
        "grammatical_info": {
            "part_of_speech": "adverb (frequency)",
            "syntax": "requires double negative: δεν + verb + ποτέ"
        },
        "keg_communicative_function": "Expressing zero recurrence of an action",
        "example_el": "Δεν πίνω ποτέ καφέ το βράδυ.",
        "example_en": "I never drink coffee in the evening.",
        "notes_or_mnemonics": "Crucial syntax rule: Modern Greek requires a double negative ('δεν... ποτέ')."
    },
    {
        "id": "A1-U08-039",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "phrase",
        "front": "κάθε μέρα",
        "back_primary": "every day / daily",
        "grammatical_info": {
            "part_of_speech": "phrase (temporal frequency)"
        },
        "keg_communicative_function": "Describing activities that happen on a daily basis",
        "example_el": "Κάθε μέρα μαθαίνω πέντε νέες λέξεις.",
        "example_en": "Every day I learn five new words.",
        "notes_or_mnemonics": "'Κάθε' is an indeclinable distributive adjective ('κάθε μέρα', 'κάθε πρωί', 'κάθε εβδομάδα')."
    },
    {
        "id": "A1-U08-040",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "adverb",
        "front": "νωρίς",
        "back_primary": "early",
        "grammatical_info": {
            "part_of_speech": "adverb of time"
        },
        "keg_communicative_function": "Indicating timing early in the day or before expected time",
        "example_el": "Ξυπνάω νωρίς το πρωί.",
        "example_en": "I wake up early in the morning.",
        "notes_or_mnemonics": "Oxytone adverb. Direct antonym of 'αργά'."
    },
    {
        "id": "A1-U08-041",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "adverb",
        "front": "αργά",
        "back_primary": "late",
        "grammatical_info": {
            "part_of_speech": "adverb of time"
        },
        "keg_communicative_function": "Indicating timing late in the day or after schedule",
        "example_el": "Γυρίζω αργά από το γραφείο.",
        "example_en": "I return late from the office.",
        "notes_or_mnemonics": "Oxytone adverb. Opposite of 'νωρίς'."
    },
    {
        "id": "A1-U08-042",
        "unit_number": 8,
        "unit_theme": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "card_type": "phrase",
        "front": "θέλω να",
        "back_primary": "I want to (+ Present Active Indicative)",
        "grammatical_info": {
            "part_of_speech": "phrase (modal connective syntax)",
            "construction": "θέλω να + present active indicative"
        },
        "keg_communicative_function": "Expressing desires, intentions, and personal goals for the day",
        "example_el": "Θέλω να μάθω καλά ελληνικά.",
        "example_en": "I want to learn Greek well.",
        "notes_or_mnemonics": "Crucial A1 syntax bridge: 'θέλω να' followed by present indicative in A1 to express intent."
    }
]

# 1. Write content/keg_a1_units_08.json
with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(cards_u8, f, ensure_ascii=False, indent=2)
print(f"[OK] Wrote {len(cards_u8)} cards to {JSON_PATH.name}")

# 2. Build entries for content/unit-08/lesson-01.yaml
lesson_entries = []
for c in cards_u8:
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

lesson_notes_u8 = (
    "Unit 8 Core Grammar Notes:\n\n"
    "• Daily Routine Active Verbs:\n"
    "  - Type A (-ω, -εις, -ει, -ουμε, -ετε, -ουν): αρχίζω, τελειώνω, διαβάζω, γράφω, ακούω, βλέπω, μαγειρεύω, φεύγω, γυρίζω, ψωνίζω.\n"
    "  - Type B1 (-άω/-ώ, -άς, -άει/-ά, -άμε, -άτε, -άνε/-ούν): ξυπνάω/ξυπνώ, περπατάω/περπατώ, τραγουδάω/τραγουδώ.\n"
    "  - Type B2 (-ώ, -είς, -εί, -ούμε, -είτε, -ούν): οδηγώ, μπορώ, ζω.\n\n"
    "• Strict A1 Active Routine Phrases (Avoiding Mediopassive):\n"
    "  - παίρνω πρωινό (have breakfast)\n"
    "  - κάνω μπάνιο / κάνω ντους (take a bath / shower)\n"
    "  - κάνω γυμναστική (work out / exercise)\n"
    "  - πάω για ύπνο (go to bed / sleep)\n\n"
    "• Adverbs of Frequency & Scale:\n"
    "  - πάντα (100%) > συνήθως (80%) > συχνά (60%) > μερικές φορές (40%) > σπάνια (10%) > ποτέ (0%).\n"
    "  - Double Negative Rule with ποτέ: 'Δεν' + verb + 'ποτέ' (e.g. Δεν πίνω ποτέ καφέ το βράδυ).\n\n"
    "• Times of the Day & Temporal Markers:\n"
    "  - το πρωί, το μεσημέρι, το απόγευμα, το βράδυ, τη νύχτα.\n"
    "  - νωρίς (early) vs. αργά (late).\n\n"
    "• Modal Connective Syntax:\n"
    "  - θέλω να + Present Active Indicative (θέλω να μάθω...)\n"
    "  - μπορώ να + Present Active Indicative (μπορώ να μιλήσω...)"
)

yaml_payload = {
    "unit_id": "unit-08",
    "lesson_id": "lesson-01",
    "title": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
    "description": "CEFR A1: Describing daily routines, work and study schedule, frequency adverbs (πάντα, συχνά, ποτέ), Type A, B1, and B2 active verbs, and modal connectors (θέλω να).",
    "lesson_status": "not_started",
    "lesson_notes": lesson_notes_u8,
    "entries": lesson_entries
}

with open(YAML_PATH, "w", encoding="utf-8") as f:
    yaml.dump(yaml_payload, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
print(f"[OK] Wrote {len(lesson_entries)} entries to {YAML_PATH.relative_to(BASE_DIR)}")

# 3. Update content/manifest.yaml if unit-08 is not already in manifest
with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = yaml.safe_load(f) or {}

existing_unit_ids = [u["id"] for u in manifest.get("units", [])]
if "unit-08" not in existing_unit_ids:
    # insert directly after unit-07
    units = manifest.get("units", [])
    insert_idx = len(units)
    for idx, u in enumerate(units):
        if u["id"] == "unit-07":
            insert_idx = idx + 1
            break
    units.insert(insert_idx, {
        "id": "unit-08",
        "title": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "order": "OG-08-A",
        "lessons": [
            {
                "id": "lesson-01",
                "file": "unit-08/lesson-01.yaml",
                "title": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)"
            }
        ]
    })
    manifest["units"] = units
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"[OK] Added unit-08 to {MANIFEST_PATH.name} right after unit-07 (order: OG-08-A)")
else:
    print(f"[INFO] unit-08 already exists in {MANIFEST_PATH.name}")

print("\nUnit 8 creation complete!")

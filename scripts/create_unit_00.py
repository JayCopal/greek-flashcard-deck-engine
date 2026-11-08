# -*- coding: utf-8 -*-
"""
Script to create Unit 0: Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)
Designed specifically for learners using the 'Κλικ στα Ελληνικά' (Klik) book series and preparing
for the Greek Citizenship Examination (ΠΕΓΠ) and CEFR Attainment in Greek (ΚΕΓ A1/A2/B1).
"""
import sys
import json
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
UNIT_DIR = CONTENT_DIR / "unit-00"
UNIT_DIR.mkdir(parents=True, exist_ok=True)
YAML_PATH = UNIT_DIR / "lesson-01.yaml"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

cards_u0 = [
    # -------------------------------------------------------------
    # Category 1: Exam & Exercise Imperatives / Action Verbs (1-20)
    # -------------------------------------------------------------
    {
        "id": "A1-U00-001",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "διαβάζω",
        "back_primary": "to read / read! (διαβάστε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "διαβάζει",
            "first_person_plural": "διαβάζουμε",
            "imperative_formal": "διαβάστε"
        },
        "keg_communicative_function": "Understanding exam reading instructions and exercise prompts",
        "example_el": "Διαβάστε το παρακάτω κείμενο προσεκτικά και απαντήστε στις ερωτήσεις.",
        "example_en": "Read the following text carefully and answer the questions.",
        "notes_or_mnemonics": "Core regular Type A verb. In exams and textbooks, the polite/plural imperative 'διαβάστε' (read!) is universally used for rubrics."
    },
    {
        "id": "A1-U00-002",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "γράφω",
        "back_primary": "to write / write! (γράψτε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "γράφει",
            "first_person_plural": "γράφουμε",
            "imperative_formal": "γράψτε"
        },
        "keg_communicative_function": "Understanding written production tasks and writing instructions",
        "example_el": "Γράψτε ένα σύντομο κείμενο 40-50 λέξεων για τις συνήθειές σας.",
        "example_en": "Write a short text of 40-50 words about your habits.",
        "notes_or_mnemonics": "Imperative 'γράψτε' marks all written production tasks on citizenship and KEG test papers."
    },
    {
        "id": "A1-U00-003",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "ακούω",
        "back_primary": "to listen / listen! (ακούστε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "ακούει",
            "first_person_plural": "ακούμε",
            "imperative_formal": "ακούστε"
        },
        "keg_communicative_function": "Understanding listening comprehension section instructions",
        "example_el": "Ακούστε τον διάλογο δύο φορές και σημειώστε τη σωστή απάντηση.",
        "example_en": "Listen to the dialogue twice and mark the correct answer.",
        "notes_or_mnemonics": "Essential for listening tests (κατανόηση προφορικού λόγου). Test recordings always begin with 'Ακούστε'."
    },
    {
        "id": "A1-U00-004",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "κοιτάζω",
        "back_primary": "to look at / look! (κοιτάξτε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "κοιτάζει",
            "first_person_plural": "κοιτάζουμε",
            "imperative_formal": "κοιτάξτε"
        },
        "keg_communicative_function": "Directing visual attention to diagrams, pictures, or tables",
        "example_el": "Κοιτάξτε την εικόνα και γράψτε τι βλέπετε.",
        "example_en": "Look at the picture and write what you see.",
        "notes_or_mnemonics": "Frequent in Klik exercises (e.g. 'Κοιτάξτε τις εικόνες'). Imperative plural: κοιτάξτε."
    },
    {
        "id": "A1-U00-005",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "βλέπω",
        "back_primary": "to see / see! / look! (δείτε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "βλέπει",
            "first_person_plural": "βλέπουμε",
            "imperative_formal": "δείτε"
        },
        "keg_communicative_function": "Referring students to visual prompts and examples",
        "example_el": "Δείτε το παράδειγμα και συμπληρώστε τις υπόλοιπες προτάσεις.",
        "example_en": "See (look at) the example and complete the remaining sentences.",
        "notes_or_mnemonics": "Irregular aorist imperative: δείτε (see! / look!). Constantly used with 'Δείτε το παράδειγμα'."
    },
    {
        "id": "A1-U00-006",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "αντιστοιχίζω",
        "back_primary": "to match / match! (αντιστοιχίστε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "αντιστοιχίζει",
            "first_person_plural": "αντιστοιχίζουμε",
            "imperative_formal": "αντιστοιχίστε"
        },
        "keg_communicative_function": "Matching columns, items, or definitions in test sections",
        "example_el": "Αντιστοιχίστε τις ερωτήσεις της στήλης Α με τις απαντήσεις της στήλης Β.",
        "example_en": "Match the questions of column A with the answers of column B.",
        "notes_or_mnemonics": "The universal command for matching exercises in Klik books and Greek citizenship exams."
    },
    {
        "id": "A1-U00-007",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "συμπληρώνω",
        "back_primary": "to fill in / complete! (συμπληρώστε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "συμπληρώνει",
            "first_person_plural": "συμπληρώνουμε",
            "imperative_formal": "συμπληρώστε"
        },
        "keg_communicative_function": "Completing gap-fill sentences, forms, and vocabulary blanks",
        "example_el": "Συμπληρώστε τα κενά με τη σωστή μορφή του ρήματος.",
        "example_en": "Fill in the blanks with the correct form of the verb.",
        "notes_or_mnemonics": "Imperative 'συμπληρώστε' introduces fill-in-the-blank questions (συμπλήρωση κενών) everywhere."
    },
    {
        "id": "A1-U00-008",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "επιλέγω",
        "back_primary": "to choose / select! (επιλέξτε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "επιλέγει",
            "first_person_plural": "επιλέγουμε",
            "imperative_formal": "επιλέξτε"
        },
        "keg_communicative_function": "Selecting the correct alternative in multiple-choice exams",
        "example_el": "Επιλέξτε τη σωστή απάντηση ανάμεσα στις επιλογές α, β και γ.",
        "example_en": "Choose the correct answer among options a, b, and c.",
        "notes_or_mnemonics": "Formal term for 'choose' used in official test rubrics. Imperative: επιλέξτε."
    },
    {
        "id": "A1-U00-009",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "διαλέγω",
        "back_primary": "to pick / choose! (διαλέξτε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "διαλέγει",
            "first_person_plural": "διαλέγουμε",
            "imperative_formal": "διαλέξτε"
        },
        "keg_communicative_function": "Picking answers or topics in textbook tasks",
        "example_el": "Διαλέξτε ένα θέμα και γράψτε τη γνώμη σας.",
        "example_en": "Pick a topic and write your opinion.",
        "notes_or_mnemonics": "Slightly less formal synonym of 'επιλέγω', commonly found in Klik textbook exercises."
    },
    {
        "id": "A1-U00-010",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "κυκλώνω",
        "back_primary": "to circle / circle! (κυκλώστε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "κυκλώνει",
            "first_person_plural": "κυκλώνουμε",
            "imperative_formal": "κυκλώστε"
        },
        "keg_communicative_function": "Circling the correct letter or word in exam papers",
        "example_el": "Κυκλώστε το σωστό γράμμα για κάθε ερώτηση.",
        "example_en": "Circle the correct letter for each question.",
        "notes_or_mnemonics": "From 'ο κύκλος' (circle). 'Κυκλώστε το σωστό' is a standard instruction across all A1-B1 exams."
    },
    {
        "id": "A1-U00-011",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "υπογραμμίζω",
        "back_primary": "to underline / underline! (υπογραμμίστε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "υπογραμμίζει",
            "first_person_plural": "υπογραμμίζουμε",
            "imperative_formal": "υπογραμμίστε"
        },
        "keg_communicative_function": "Underlining grammatical targets or keywords in text",
        "example_el": "Υπογραμμίστε όλα τα ρήματα στο απόσπασμα.",
        "example_en": "Underline all the verbs in the passage.",
        "notes_or_mnemonics": "From 'υπό' (under) + 'γραμμή' (line). Imperative: υπογραμμίστε."
    },
    {
        "id": "A1-U00-012",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "σημειώνω",
        "back_primary": "to mark / tick / note! (σημειώστε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "σημειώνει",
            "first_person_plural": "σημειώνουμε",
            "imperative_formal": "σημειώστε"
        },
        "keg_communicative_function": "Marking boxes or choices with symbols (X or checkmark)",
        "example_el": "Σημειώστε με ένα [X] στο κατάλληλο κουτάκι.",
        "example_en": "Mark with an [X] in the appropriate box.",
        "notes_or_mnemonics": "Universal in True/False and multiple-choice rubrics: 'Σημειώστε Σ ή Λ'."
    },
    {
        "id": "A1-U00-013",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "απαντώ",
        "back_primary": "to answer / answer! (απαντήστε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type B1",
            "third_person_singular": "απαντάει / απαντά",
            "first_person_plural": "απαντάμε",
            "imperative_formal": "απαντήστε"
        },
        "keg_communicative_function": "Responding to questions in oral and written exam sections",
        "example_el": "Απαντήστε στις ερωτήσεις με πλήρεις προτάσεις.",
        "example_en": "Answer the questions in complete sentences.",
        "notes_or_mnemonics": "Type B1 contract verb. Takes preposition 'σε': απαντώ σε μία ερώτηση (I answer a question)."
    },
    {
        "id": "A1-U00-014",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "βρίσκω",
        "back_primary": "to find / find! (βρείτε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "βρίσκει",
            "first_person_plural": "βρίσκουμε",
            "imperative_formal": "βρείτε"
        },
        "keg_communicative_function": "Locating information, synonyms, or answers in text",
        "example_el": "Βρείτε στο κείμενο τη λέξη που σημαίνει 'διακοπές'.",
        "example_en": "Find in the text the word that means 'vacation'.",
        "notes_or_mnemonics": "Irregular aorist imperative: βρείτε (find!). Common prompt: 'Βρείτε το λάθος' (Find the error)."
    },
    {
        "id": "A1-U00-015",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "βάζω",
        "back_primary": "to put / put! (βάλτε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "βάζει",
            "first_person_plural": "βάζουμε",
            "imperative_formal": "βάλτε"
        },
        "keg_communicative_function": "Ordering scrambled sentences or organizing items",
        "example_el": "Βάλτε τις λέξεις στη σωστή σειρά για να φτιάξετε προτάσεις.",
        "example_en": "Put the words in the correct order to make sentences.",
        "notes_or_mnemonics": "Imperative: βάλτε. Often paired with 'στη σωστή σειρά' (in the correct order) or 'σε κύκλο' (in a circle)."
    },
    {
        "id": "A1-U00-016",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "διαγράφω",
        "back_primary": "to cross out / strike through! (διαγράψτε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "διαγράφει",
            "first_person_plural": "διαγράφουμε",
            "imperative_formal": "διαγράψτε"
        },
        "keg_communicative_function": "Eliminating incorrect choices or intruder words (odd-one-out)",
        "example_el": "Διαγράψτε τη λέξη που δεν ταιριάζει με τις άλλες.",
        "example_en": "Cross out the word that does not belong with the others.",
        "notes_or_mnemonics": "Used in 'odd-one-out' (βρες το περιττό) vocabulary drills in Klik A1. Imperative: διαγράψτε."
    },
    {
        "id": "A1-U00-017",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "διορθώνω",
        "back_primary": "to correct / correct! (διορθώστε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "διορθώνει",
            "first_person_plural": "διορθώνουμε",
            "imperative_formal": "διορθώστε"
        },
        "keg_communicative_function": "Correcting errors in sentences and proofreading written texts",
        "example_el": "Διορθώστε τα λάθη στις παρακάτω προτάσεις.",
        "example_en": "Correct the mistakes in the following sentences.",
        "notes_or_mnemonics": "Imperative: διορθώστε. Core skill for self-editing before submitting citizenship test sheets."
    },
    {
        "id": "A1-U00-018",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "ξαναδιαβάζω",
        "back_primary": "to re-read / re-read! (ξαναδιαβάστε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "ξαναδιαβάζει",
            "first_person_plural": "ξαναδιαβάζουμε",
            "imperative_formal": "ξαναδιαβάστε"
        },
        "keg_communicative_function": "Reviewing text passages and verifying exam answers",
        "example_el": "Ξαναδιαβάστε το κείμενο για να ελέγξετε τις απαντήσεις σας.",
        "example_en": "Re-read the text to check your answers.",
        "notes_or_mnemonics": "Prefix 'ξανα-' denotes repetition ('again'). Essential exam strategy reminder."
    },
    {
        "id": "A1-U00-019",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "συνεχίζω",
        "back_primary": "to continue / continue! (συνεχίστε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A",
            "third_person_singular": "συνεχίζει",
            "first_person_plural": "συνεχίζουμε",
            "imperative_formal": "συνεχίστε"
        },
        "keg_communicative_function": "Continuing patterns, dialogues, or story prompts",
        "example_el": "Συνεχίστε τον διάλογο σύμφωνα με το παράδειγμα.",
        "example_en": "Continue the dialogue according to the example.",
        "notes_or_mnemonics": "Imperative: συνεχίστε. Frequent in textbook pair-work and speaking role-play tasks."
    },
    {
        "id": "A1-U00-020",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "εξηγώ",
        "back_primary": "to explain / explain! (εξηγήστε)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type B2",
            "third_person_singular": "εξηγεί",
            "first_person_plural": "εξηγούμε",
            "imperative_formal": "εξηγήστε"
        },
        "keg_communicative_function": "Clarifying reasons or answering why questions in oral exams",
        "example_el": "Εξηγήστε γιατί επιλέξατε αυτή την απάντηση.",
        "example_en": "Explain why you chose this answer.",
        "notes_or_mnemonics": "Contract Type B2 verb. In speaking examinations, examiners frequently prompt: 'Εξηγήστε μου...' (Explain to me...)."
    },

    # -------------------------------------------------------------
    # Category 2: Question Types, Formats & Rubric Formulas (21-31)
    # -------------------------------------------------------------
    {
        "id": "A1-U00-021",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "το σωστό",
        "back_primary": "the correct / right / true",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα σωστά",
            "accusative_singular": "το σωστό"
        },
        "keg_communicative_function": "Identifying true/correct alternatives in test items",
        "example_el": "Βρείτε ποιο είναι το σωστό και κυκλώστε το.",
        "example_en": "Find which is the correct one and circle it.",
        "notes_or_mnemonics": "Adjective used as neuter noun. The counterpart of 'το λάθος'. Represented by 'Σ' in True/False questions."
    },
    {
        "id": "A1-U00-022",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "το λάθος",
        "back_primary": "the wrong / mistake / false",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα λάθη",
            "accusative_singular": "το λάθος"
        },
        "keg_communicative_function": "Detecting false statements, errors, and incorrect answers",
        "example_el": "Αυτή η πρόταση είναι λάθος, γιατί ο Νίκος δεν μένει στην Αθήνα.",
        "example_en": "This sentence is false/wrong, because Nikos does not live in Athens.",
        "notes_or_mnemonics": "Neuter in -ος, plural: τα λάθη (genitive: των λαθών). Represented by 'Λ' in tests."
    },
    {
        "id": "A1-U00-023",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "Σωστό ή Λάθος (Σ/Λ)",
        "back_primary": "True or False (T/F)",
        "grammatical_info": {
            "part_of_speech": "phrase / exam instruction"
        },
        "keg_communicative_function": "Understanding binary verification tasks in reading & listening tests",
        "example_el": "Σημειώστε Σ (Σωστό) ή Λ (Λάθος) για κάθε πρόταση του κειμένου.",
        "example_en": "Mark T (True) or F (False) for each sentence of the text.",
        "notes_or_mnemonics": "Every Greek language test and citizenship exam includes a 'Σωστό ή Λάθος' section. Always mark 'Σ' for True and 'Λ' for False."
    },
    {
        "id": "A1-U00-024",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η πολλαπλή επιλογή",
        "back_primary": "multiple choice",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πολλαπλές επιλογές",
            "accusative_singular": "την πολλαπλή επιλογή"
        },
        "keg_communicative_function": "Navigating multiple-choice testing formats and options",
        "example_el": "Το γραπτό τεστ αποτελείται από είκοσι ερωτήσεις πολλαπλής επιλογής.",
        "example_en": "The written test consists of twenty multiple-choice questions.",
        "notes_or_mnemonics": "'Πολλαπλή' (multiple) + 'επιλογή' (choice). Citizenship knowledge exams in Greece (ΠΕΓΠ) heavily feature multiple choice."
    },
    {
        "id": "A1-U00-025",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "συμπληρώστε τα κενά",
        "back_primary": "fill in the blanks / gaps",
        "grammatical_info": {
            "part_of_speech": "phrase / exam instruction"
        },
        "keg_communicative_function": "Executing cloze and gap-fill exercise prompts",
        "example_el": "Συμπληρώστε τα κενά από το 1 έως το 6 με τις λέξεις του πλαισίου.",
        "example_en": "Fill in the blanks from 1 to 6 with the words in the box.",
        "notes_or_mnemonics": "One of the most frequent rubric headings in 'Κλικ στα Ελληνικά' and KEG language tests."
    },
    {
        "id": "A1-U00-026",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "αντιστοιχίστε τη στήλη Α με τη στήλη Β",
        "back_primary": "match column A with column B",
        "grammatical_info": {
            "part_of_speech": "phrase / exam instruction"
        },
        "keg_communicative_function": "Connecting related entries across two visual columns",
        "example_el": "Αντιστοιχίστε τη στήλη Α (ερωτήσεις) με τη στήλη Β (απαντήσεις).",
        "example_en": "Match column A (questions) with column B (answers).",
        "notes_or_mnemonics": "Standard two-column matching prompt used in grammar and vocabulary assessment."
    },
    {
        "id": "A1-U00-027",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "κυκλώστε το σωστό",
        "back_primary": "circle the correct answer",
        "grammatical_info": {
            "part_of_speech": "phrase / exam instruction"
        },
        "keg_communicative_function": "Executing item selection by drawing a circle around choices",
        "example_el": "Κυκλώστε το σωστό γράμμα: α, β ή γ.",
        "example_en": "Circle the correct letter: a, b, or c.",
        "notes_or_mnemonics": "Clear mechanical command seen on paper-and-pencil test formats."
    },
    {
        "id": "A1-U00-028",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "βάλτε στη σωστή σειρά",
        "back_primary": "put in the correct order",
        "grammatical_info": {
            "part_of_speech": "phrase / exam instruction"
        },
        "keg_communicative_function": "Sequencing scrambled narratives, sentences, or chronological events",
        "example_el": "Βάλτε στη σωστή σειρά τις παραγράφους του κειμένου (1-4).",
        "example_en": "Put in the correct order the paragraphs of the text (1-4).",
        "notes_or_mnemonics": "Critical for reading comprehension sequencing tasks in A1-A2 exams."
    },
    {
        "id": "A1-U00-029",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "απαντήστε στις ερωτήσεις",
        "back_primary": "answer the questions",
        "grammatical_info": {
            "part_of_speech": "phrase / exam instruction"
        },
        "keg_communicative_function": "Directing candidates to open-ended or short-answer question sections",
        "example_el": "Απαντήστε στις ερωτήσεις σύμφωνα με όσα ακούσατε στον διάλογο.",
        "example_en": "Answer the questions according to what you heard in the dialogue.",
        "notes_or_mnemonics": "Universal instruction heading appearing right after reading or listening passages."
    },
    {
        "id": "A1-U00-030",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "διαλέξτε τη σωστή απάντηση",
        "back_primary": "choose / pick the correct answer",
        "grammatical_info": {
            "part_of_speech": "phrase / exam instruction"
        },
        "keg_communicative_function": "Executing item selection in multiple choice or gap-fill prompts",
        "example_el": "Διαλέξτε τη σωστή απάντηση για να ολοκληρώσετε την πρόταση.",
        "example_en": "Pick the correct answer to complete the sentence.",
        "notes_or_mnemonics": "Everyday textbook phrasing in Klik sta Ellinika exercises."
    },
    {
        "id": "A1-U00-031",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "σημειώστε με ένα τικ",
        "back_primary": "mark with a checkmark / tick",
        "grammatical_info": {
            "part_of_speech": "phrase / exam instruction"
        },
        "keg_communicative_function": "Marking boxes on standardized survey or test response forms",
        "example_el": "Σημειώστε με ένα τικ (✓) στις δηλώσεις που ταιριάζουν σε εσάς.",
        "example_en": "Mark with a checkmark (✓) the statements that match you.",
        "notes_or_mnemonics": "Common in textbook self-assessment grids and citizenship application forms."
    },

    # -------------------------------------------------------------
    # Category 3: Examination & Textbook Core Terminology (32-50)
    # -------------------------------------------------------------
    {
        "id": "A1-U00-032",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η εξέταση",
        "back_primary": "the exam / examination (οι εξετάσεις)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι εξετάσεις",
            "accusative_singular": "την εξέταση"
        },
        "keg_communicative_function": "Discussing official tests, exams, and citizenship certifications",
        "example_el": "Προετοιμάζομαι για τις εξετάσεις της ελληνομάθειας και της πολιτογράφησης.",
        "example_en": "I am preparing for the exams of Greek attainment and citizenship.",
        "notes_or_mnemonics": "Feminine noun in -ση (plural: -σεις). Frequently used in plural: 'δίνω εξετάσεις' (I sit for exams)."
    },
    {
        "id": "A1-U00-033",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "το τεστ",
        "back_primary": "the test / quiz",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα τεστ",
            "accusative_singular": "το τεστ"
        },
        "keg_communicative_function": "Referring to classroom and end-of-unit tests",
        "example_el": "Στο τέλος κάθε ενότητας του βιβλίου κάνουμε ένα μικρό τεστ.",
        "example_en": "At the end of each unit of the book, we do a short test.",
        "notes_or_mnemonics": "Indeclinable neuter loanword (το τεστ, τα τεστ). Used colloquially and in textbook section headers."
    },
    {
        "id": "A1-U00-034",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η οδηγία",
        "back_primary": "the instruction / direction (οι οδηγίες)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι οδηγίες",
            "accusative_singular": "την οδηγία"
        },
        "keg_communicative_function": "Reading and understanding rubric directions on test papers",
        "example_el": "Διαβάστε προσεκτικά τις οδηγίες πριν αρχίσετε να γράφετε.",
        "example_en": "Read the instructions carefully before you begin writing.",
        "notes_or_mnemonics": "Almost always plural on exams: 'Οι οδηγίες της εξέτασης' (The exam instructions)."
    },
    {
        "id": "A1-U00-035",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η ερώτηση",
        "back_primary": "the question",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ερωτήσεις",
            "accusative_singular": "την ερώτηση"
        },
        "keg_communicative_function": "Identifying test items and asking clarifying questions",
        "example_el": "Αυτή η ερώτηση έχει τρεις πιθανές απαντήσεις.",
        "example_en": "This question has three possible answers.",
        "notes_or_mnemonics": "Feminine in -ση (plural: οι ερωτήσεις). Pair with 'η απάντηση' (the answer)."
    },
    {
        "id": "A1-U00-036",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η απάντηση",
        "back_primary": "the answer / reply / response",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι απαντήσεις",
            "accusative_singular": "την απάντηση"
        },
        "keg_communicative_function": "Formulating answers and locating answer keys",
        "example_el": "Σημειώστε την τελική απάντηση στο φύλλο απαντήσεων.",
        "example_en": "Mark the final answer on the answer sheet.",
        "notes_or_mnemonics": "From verb 'απαντώ'. Plural: οι απαντήσεις. 'Φύλλο απαντήσεων' = answer sheet."
    },
    {
        "id": "A1-U00-037",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "το θέμα",
        "back_primary": "the topic / subject / exam task",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα θέματα",
            "accusative_singular": "το θέμα"
        },
        "keg_communicative_function": "Navigating designated exam sections and essay subjects",
        "example_el": "Το Θέμα 1 της εξέτασης αφορά την κατανόηση γραπτού κειμένου.",
        "example_en": "Task (Section) 1 of the exam concerns reading comprehension.",
        "notes_or_mnemonics": "In Greek official examinations, each major section or question is designated as 'Θέμα 1', 'Θέμα 2', etc."
    },
    {
        "id": "A1-U00-038",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "το παράδειγμα",
        "back_primary": "the example",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα παραδείγματα",
            "accusative_singular": "το παράδειγμα"
        },
        "keg_communicative_function": "Analyzing sample answers before starting an exercise",
        "example_el": "Κοιτάξτε το παράδειγμα (0) πριν αρχίσετε την άσκηση.",
        "example_en": "Look at example (0) before beginning the exercise.",
        "notes_or_mnemonics": "In exams and books, item (0) is almost always the solved model example (το παράδειγμα)."
    },
    {
        "id": "A1-U00-039",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "το κείμενο",
        "back_primary": "the text / reading passage",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κείμενα",
            "accusative_singular": "το κείμενο"
        },
        "keg_communicative_function": "Identifying reading comprehension texts and articles",
        "example_el": "Το κείμενο περιγράφει τη ζωή μιας οικογένειας στην Κύπρο.",
        "example_en": "The text describes the life of a family in Cyprus.",
        "notes_or_mnemonics": "Neuter in -ο (plural: τα κείμενα). The central piece of all reading comprehension modules."
    },
    {
        "id": "A1-U00-040",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "ο διάλογος",
        "back_primary": "the dialogue / conversation",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι διάλογοι",
            "accusative_singular": "τον διάλογο"
        },
        "keg_communicative_function": "Following conversational exchanges in audio and textbooks",
        "example_el": "Ακούστε τον σύντομο διάλογο και βρείτε πού βρίσκονται οι δύο ομιλητές.",
        "example_en": "Listen to the short dialogue and find where the two speakers are.",
        "notes_or_mnemonics": "Masculine in -ος (plural: οι διάλογοι). Primary basis of CEFR A1 listening tests."
    },
    {
        "id": "A1-U00-041",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η πρόταση",
        "back_primary": "the sentence",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι προτάσεις",
            "accusative_singular": "την πρόταση"
        },
        "keg_communicative_function": "Constructing and analyzing grammatical sentences",
        "example_el": "Φτιάξτε μια ολοκληρωμένη πρόταση με τις παρακάτω λέξεις.",
        "example_en": "Form a complete sentence with the words below.",
        "notes_or_mnemonics": "Feminine in -ση. Means both 'grammatical sentence' and 'suggestion/proposal'."
    },
    {
        "id": "A1-U00-042",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η λέξη",
        "back_primary": "the word",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι λέξεις",
            "accusative_singular": "τη λέξη"
        },
        "keg_communicative_function": "Identifying lexical units and checking word limits",
        "example_el": "Γράψτε ένα κείμενο τουλάχιστον 50 λέξεων.",
        "example_en": "Write a text of at least 50 words.",
        "notes_or_mnemonics": "Feminine noun (genitive: της λέξης, plural: οι λέξεις). Essay prompts enforce strict word counts (π.χ. 40-60 λέξεις)."
    },
    {
        "id": "A1-U00-043",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "το κενό",
        "back_primary": "the blank / gap / empty space",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κενά",
            "accusative_singular": "το κενό"
        },
        "keg_communicative_function": "Locating fill-in positions within cloze exercises",
        "example_el": "Γράψτε μία μόνο λέξη σε κάθε κενό.",
        "example_en": "Write only one word in each blank.",
        "notes_or_mnemonics": "Neuter noun (plural: τα κενά). Cloze tests instruct: 'Συμπληρώστε τα κενά'."
    },
    {
        "id": "A1-U00-044",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η εικόνα",
        "back_primary": "the picture / image",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι εικόνες",
            "accusative_singular": "την εικόνα"
        },
        "keg_communicative_function": "Interpreting visual prompts in oral examinations and textbooks",
        "example_el": "Περιγράψτε την εικόνα και πείτε τι κάνουν οι άνθρωποι.",
        "example_en": "Describe the picture and tell what the people are doing.",
        "notes_or_mnemonics": "Feminine noun (plural: οι εικόνες). In speaking exams (προφορικά), examiners give you a picture to describe."
    },
    {
        "id": "A1-U00-045",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η φωτογραφία",
        "back_primary": "the photograph / photo",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι φωτογραφίες",
            "accusative_singular": "τη φωτογραφία"
        },
        "keg_communicative_function": "Describing photograph stimulus materials in speaking tests",
        "example_el": "Στη φωτογραφία βλέπουμε μια παραλία το καλοκαίρι.",
        "example_en": "In the photograph, we see a beach in summer.",
        "notes_or_mnemonics": "Often abbreviated as 'η φωτό' in informal contexts; formal on exam sheets."
    },
    {
        "id": "A1-U00-046",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "ο πίνακας",
        "back_primary": "the table / chart / board",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι πίνακες",
            "accusative_singular": "τον πίνακα"
        },
        "keg_communicative_function": "Reading and completing data charts and grammar grids",
        "example_el": "Συμπληρώστε τον πίνακα γραμματικής με τα κατάλληλα άρθρα.",
        "example_en": "Complete the grammar table with the appropriate articles.",
        "notes_or_mnemonics": "Masculine in -ας (plural: οι πίνακες). Used for both 'table/chart' in books and 'blackboard/whiteboard' in classrooms."
    },
    {
        "id": "A1-U00-047",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η στήλη",
        "back_primary": "the column",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι στήλες",
            "accusative_singular": "τη στήλη"
        },
        "keg_communicative_function": "Locating paired elements in matching tasks",
        "example_el": "Η πρώτη στήλη περιέχει τα ρήματα και η δεύτερη τα αντικείμενα.",
        "example_en": "The first column contains the verbs and the second the objects.",
        "notes_or_mnemonics": "Feminine noun (plural: οι στήλες). Paired with 'η γραμμή' (row/line)."
    },
    {
        "id": "A1-U00-048",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η γραμμή",
        "back_primary": "the line / row",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι γραμμές",
            "accusative_singular": "τη γραμμή"
        },
        "keg_communicative_function": "Writing on lined exam paper and referencing text rows",
        "example_el": "Γράψτε την απάντησή σας στην επόμενη κενή γραμμή.",
        "example_en": "Write your answer on the next blank line.",
        "notes_or_mnemonics": "Feminine noun (plural: οι γραμμές). Refers to horizontal writing lines or rows in tables."
    },
    {
        "id": "A1-U00-049",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "ο βαθμός",
        "back_primary": "the grade / mark / score",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι βαθμοί",
            "accusative_singular": "τον βαθμό"
        },
        "keg_communicative_function": "Understanding pass marks and grading criteria",
        "example_el": "Ο τελικός βαθμός μου ήταν αρκετά υψηλός για να περάσω.",
        "example_en": "My final grade was high enough to pass.",
        "notes_or_mnemonics": "Masculine in -ος (plural: οι βαθμοί). 'Βάση' is the minimum passing score."
    },
    {
        "id": "A1-U00-050",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η βαθμολογία",
        "back_primary": "the scoring / mark evaluation",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι βαθμολογίες",
            "accusative_singular": "τη βαθμολογία"
        },
        "keg_communicative_function": "Understanding exam point values per question",
        "example_el": "Κάθε σωστή απάντηση δίνει μία μονάδα στη συνολική βαθμολογία.",
        "example_en": "Each correct answer gives one point towards the overall score.",
        "notes_or_mnemonics": "Feminine noun. In exams, 'Μέγιστη βαθμολογία: 100 μονάδες'."
    },
    {
        "id": "A1-U00-051",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "ο χρόνος",
        "back_primary": "time / duration / exam time",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι χρόνοι",
            "accusative_singular": "τον χρόνο"
        },
        "keg_communicative_function": "Managing exam time allocation and pace",
        "example_el": "Ο χρόνος για το πρώτο μέρος της εξέτασης είναι 45 λεπτά.",
        "example_en": "The time for the first part of the exam is 45 minutes.",
        "notes_or_mnemonics": "Masculine in -ος. Examiners announce: 'Ο χρόνος τελείωσε' (Time is up)."
    },
    {
        "id": "A1-U00-052",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η σελίδα",
        "back_primary": "the page",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι σελίδες",
            "accusative_singular": "τη σελίδα"
        },
        "keg_communicative_function": "Navigating textbooks and multi-page exam booklets",
        "example_el": "Ανοίξτε το βιβλίο 'Κλικ' στη σελίδα 43.",
        "example_en": "Open the book 'Klik' to page 43.",
        "notes_or_mnemonics": "Feminine noun (plural: οι σελίδες). Abbreviated as 'σελ.' or 'σ.' in Greek books."
    },
    {
        "id": "A1-U00-053",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η άσκηση",
        "back_primary": "the exercise / drill (οι ασκήσεις)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ασκήσεις",
            "accusative_singular": "την άσκηση"
        },
        "keg_communicative_function": "Identifying practice exercises and homework activities",
        "example_el": "Κάντε την άσκηση 4 για το επόμενο μάθημα.",
        "example_en": "Do exercise 4 for the next lesson.",
        "notes_or_mnemonics": "Feminine in -ση (plural: οι ασκήσεις). Numbered throughout every chapter of Klik."
    },

    # -------------------------------------------------------------
    # Category 4: Language Skills & Examination Sections (54-58)
    # -------------------------------------------------------------
    {
        "id": "A1-U00-054",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η κατανόηση γραπτού λόγου",
        "back_primary": "reading comprehension",
        "grammatical_info": {
            "part_of_speech": "phrase / exam section",
            "accusative_singular": "την κατανόηση γραπτού λόγου"
        },
        "keg_communicative_function": "Identifying the written reading comprehension section of exams",
        "example_el": "Η κατανόηση γραπτού λόγου εξετάζει αν καταλαβαίνετε κείμενα και ανακοινώσεις.",
        "example_en": "Reading comprehension tests whether you understand texts and announcements.",
        "notes_or_mnemonics": "Official title on citizenship and KEG exam booklets: 'Κατανόηση Γραπτού Λόγου' (Reading)."
    },
    {
        "id": "A1-U00-055",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η κατανόηση προφορικού λόγου",
        "back_primary": "listening comprehension",
        "grammatical_info": {
            "part_of_speech": "phrase / exam section",
            "accusative_singular": "την κατανόηση προφορικού λόγου"
        },
        "keg_communicative_function": "Identifying the audio listening comprehension section of exams",
        "example_el": "Στην κατανόηση προφορικού λόγου θα ακούσετε ηχογραφημένους διαλόγους.",
        "example_en": "In listening comprehension, you will hear recorded dialogues.",
        "notes_or_mnemonics": "Official exam term: 'Κατανόηση Προφορικού Λόγου' (Listening)."
    },
    {
        "id": "A1-U00-056",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η παραγωγή γραπτού λόγου",
        "back_primary": "written expression / writing exam",
        "grammatical_info": {
            "part_of_speech": "phrase / exam section",
            "accusative_singular": "την παραγωγή γραπτού λόγου"
        },
        "keg_communicative_function": "Identifying the free writing/essay section of exams",
        "example_el": "Στην παραγωγή γραπτού λόγου πρέπει να γράψετε ένα email σε έναν φίλο.",
        "example_en": "In written production, you must write an email to a friend.",
        "notes_or_mnemonics": "Official exam term: 'Παραγωγή Γραπτού Λόγου' (Writing task / essay)."
    },
    {
        "id": "A1-U00-057",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η παραγωγή προφορικού λόγου",
        "back_primary": "oral production / speaking exam",
        "grammatical_info": {
            "part_of_speech": "phrase / exam section",
            "accusative_singular": "την παραγωγή προφορικού λόγου"
        },
        "keg_communicative_function": "Identifying the speaking interview component with examiners",
        "example_el": "Η παραγωγή προφορικού λόγου περιλαμβάνει συνομιλία με τον εξεταστή.",
        "example_en": "Oral production includes a conversation with the examiner.",
        "notes_or_mnemonics": "Official exam term: 'Παραγωγή Προφορικού Λόγου' (Speaking interview)."
    },
    {
        "id": "A1-U00-058",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "η πολιτογράφηση",
        "back_primary": "citizenship / naturalization",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πολιτογραφήσεις",
            "accusative_singular": "την πολιτογράφηση"
        },
        "keg_communicative_function": "Discussing citizenship goals and application requirements in Greece/Cyprus",
        "example_el": "Στόχος μου είναι να αποκτήσω το πιστοποιητικό για την ελληνική πολιτογράφηση.",
        "example_en": "My goal is to obtain the certificate for Greek naturalization (citizenship).",
        "notes_or_mnemonics": "From 'πολίτης' (citizen). The exam is officially named 'Πιστοποιητικό Επάρκειας Γνώσεων για Πολιτογράφηση (Π.Ε.Γ.Π.)'."
    },

    # -------------------------------------------------------------
    # Category 5: Grammar & Linguistic Terms in Textbooks (59-65)
    # -------------------------------------------------------------
    {
        "id": "A1-U00-059",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "ο κανόνας",
        "back_primary": "the rule (οι κανόνες)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι κανόνες",
            "accusative_singular": "τον κανόνα"
        },
        "keg_communicative_function": "Understanding grammatical and structural rules in language textbooks",
        "example_el": "Αυτός είναι ένας βασικός κανόνας της γραμματικής.",
        "example_en": "This is a basic rule of grammar.",
        "notes_or_mnemonics": "Masculine in -ας (plural: οι κανόνες). Boxed in yellow/blue in 'Κλικ' textbook grammar sections."
    },
    {
        "id": "A1-U00-060",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "το ουσιαστικό",
        "back_primary": "the noun",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ουσιαστικά",
            "accusative_singular": "το ουσιαστικό"
        },
        "keg_communicative_function": "Identifying parts of speech in grammar charts",
        "example_el": "Κάθε ελληνικό ουσιαστικό έχει γένος: αρσενικό, θηλυκό ή ουδέτερο.",
        "example_en": "Every Greek noun has a gender: masculine, feminine, or neuter.",
        "notes_or_mnemonics": "Literally 'substantive'. Categorized into masculine (αρσενικό), feminine (θηλυκό), neuter (ουδέτερο)."
    },
    {
        "id": "A1-U00-061",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "το ρήμα",
        "back_primary": "the verb",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ρήματα",
            "accusative_singular": "το ρήμα"
        },
        "keg_communicative_function": "Recognizing verbs and verb conjugations",
        "example_el": "Βρείτε το ρήμα στην πρόταση και γράψτε το στον σωστό χρόνο.",
        "example_en": "Find the verb in the sentence and write it in the correct tense.",
        "notes_or_mnemonics": "Neuter in -μα, plural: τα ρήματα. Conjugation in Greek is 'η κλίση των ρημάτων'."
    },
    {
        "id": "A1-U00-062",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "το επίθετο",
        "back_primary": "the adjective",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα επίθετα",
            "accusative_singular": "το επίθετο"
        },
        "keg_communicative_function": "Recognizing adjective agreements with nouns",
        "example_el": "Το επίθετο πρέπει να συμφωνεί σε γένος, αριθμό και πτώση με το ουσιαστικό.",
        "example_en": "The adjective must agree in gender, number, and case with the noun.",
        "notes_or_mnemonics": "Neuter in -ο. Note: also means 'surname/last name' in administrative forms (Όνομα / Επίθετο)."
    },
    {
        "id": "A1-U00-063",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "το άρθρο",
        "back_primary": "the article (definite / indefinite)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα άρθρα",
            "accusative_singular": "το άρθρο"
        },
        "keg_communicative_function": "Identifying and applying definite and indefinite articles",
        "example_el": "Βάλτε το σωστό οριστικό άρθρο: ο, η ή το.",
        "example_en": "Put the correct definite article: ο, η, or το.",
        "notes_or_mnemonics": "Neuter in -ο. 'Οριστικό άρθρο' = definite article; 'αόριστο άρθρο' = indefinite article."
    },
    {
        "id": "A1-U00-064",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "ο ενικός αριθμός",
        "back_primary": "the singular number",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι ενικοί αριθμοί",
            "accusative_singular": "τον ενικό αριθμό"
        },
        "keg_communicative_function": "Distinguishing singular grammatical forms",
        "example_el": "Μετατρέψτε τις προτάσεις από τον ενικό στον πληθυντικό αριθμό.",
        "example_en": "Transform the sentences from the singular to the plural number.",
        "notes_or_mnemonics": "Abbreviated as 'ενικ.' in dictionaries and textbooks."
    },
    {
        "id": "A1-U00-065",
        "unit_number": 0,
        "unit_theme": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "card_type": "vocabulary",
        "front": "ο πληθυντικός αριθμός",
        "back_primary": "the plural number",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι πληθυντικοί αριθμοί",
            "accusative_singular": "τον πληθυντικό αριθμό"
        },
        "keg_communicative_function": "Distinguishing plural grammatical forms and polite address",
        "example_el": "Στα ελληνικά χρησιμοποιούμε τον πληθυντικό ευγενείας για να μιλήσουμε ευγενικά.",
        "example_en": "In Greek we use the polite plural to speak politely.",
        "notes_or_mnemonics": "Abbreviated as 'πληθ.'. 'Πληθυντικός ευγενείας' is the polite plural used in all test instructions (διαβάστε, γράψτε)."
    }
]

# Convert internal card format to standard lesson yaml entry schema
lesson_entries = []
for c in cards_u0:
    entry = {
        "id": c["id"],
        "greek": c["front"],
        "phonetic_hint": "",
        "english": c["back_primary"],
        "notes": c["notes_or_mnemonics"],
        "gender_or_pos": c["grammatical_info"].get("part_of_speech", "vocabulary"),
        "audio": None,
        "status": "pending_tts",
        "example_el": c["example_el"],
        "example_en": c["example_en"],
        "grammatical_info": c["grammatical_info"],
        "keg_communicative_function": c["keg_communicative_function"]
    }
    lesson_entries.append(entry)

lesson_notes_u0 = (
    "Unit 0 Core Notes: Γλώσσα Εξετάσεων & Βιβλίου (Exam Rubrics & Textbook Instructions)\n\n"
    "• The Polite Imperative in Instructions (Πληθυντικός Ευγενείας):\n"
    "  In Modern Greek textbooks (like 'Κλικ στα Ελληνικά') and official certification exams\n"
    "  (ΠΕΓΠ Citizenship & ΚΕΓ Ellinomatheia), rubrics are consistently written in the polite 2nd-person plural (-τε / -στε):\n"
    "  - διαβάστε (read!)\n"
    "  - γράψτε (write!)\n"
    "  - ακούστε (listen!)\n"
    "  - κοιτάξτε / δείτε (look!)\n"
    "  - αντιστοιχίστε (match!)\n"
    "  - συμπληρώστε (fill in!)\n"
    "  - επιλέξτε / διαλέξτε (choose!)\n"
    "  - κυκλώστε (circle!)\n"
    "  - υπογραμμίστε (underline!)\n"
    "  - σημειώστε (mark / tick!)\n"
    "  - απαντήστε (answer!)\n\n"
    "• The Standard 4 Skills of Language & Citizenship Exams:\n"
    "  1. Κατανόηση Γραπτού Λόγου (Reading Comprehension): short texts, public signs, advertisements, emails.\n"
    "  2. Κατανόηση Προφορικού Λόγου (Listening Comprehension): announcements, telephone dialogues, voicemail messages.\n"
    "  3. Παραγωγή Γραπτού Λόγου (Writing): short personal notes, emails, invitation replies (usually 40-60 words at A1/A2).\n"
    "  4. Παραγωγή Προφορικού Λόγου (Speaking): self-introduction, describing picture cards, interview with examiners.\n\n"
    "• Question Types & Symbols:\n"
    "  - Σωστό ή Λάθος: Mark 'Σ' for True (Σωστό) and 'Λ' for False (Λάθος).\n"
    "  - Πολλαπλή Επιλογή (Multiple Choice): typically 3 or 4 options (α, β, γ, δ).\n"
    "  - Συμπλήρωση Κενών: Gap fill where one word per numbered blank is required.\n"
    "  - Αντιστοίχιση: Matching Column A (Στήλη Α) with Column B (Στήλη Β).\n\n"
    "• Exam Caution — Watch Out for Negative Instructions:\n"
    "  - 'Ποιο ΔΕΝ είναι σωστό;' (Which one is NOT correct?)\n"
    "  - 'Διαγράψτε τη λάθος λέξη' (Cross out the wrong word / odd-one-out)."
)

yaml_payload = {
    "unit_id": "unit-00",
    "lesson_id": "lesson-01",
    "title": "Μάθημα 0: Οδηγίες Εξετάσεων & Ασκήσεων (Lesson 0: Exam Instructions & Rubrics)",
    "description": "Essential exam instructions, rubric imperatives, question formats (true/false, multiple choice, matching), and test terminology for Greek citizenship & CEFR exams (ΠΕΓΠ & ΚΕΓ) and Klik textbooks.",
    "lesson_status": "not_started",
    "lesson_notes": lesson_notes_u0,
    "entries": lesson_entries
}

with open(YAML_PATH, "w", encoding="utf-8") as f:
    yaml.dump(yaml_payload, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
print(f"[OK] Wrote {len(lesson_entries)} entries to {YAML_PATH.relative_to(BASE_DIR)}")

# Update content/manifest.yaml if unit-00 is not already in manifest
with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = yaml.safe_load(f) or {}

existing_unit_ids = [u["id"] for u in manifest.get("units", [])]
if "unit-00" not in existing_unit_ids:
    unit_00_entry = {
        "id": "unit-00",
        "title": "Γλώσσα Εξετάσεων & Οδηγίες Βιβλίου (Exam Instructions & Textbook Rubrics)",
        "order": "OG-00-A",
        "lessons": [
            {
                "id": "lesson-01",
                "file": "unit-00/lesson-01.yaml",
                "title": "Μάθημα 0: Οδηγίες Εξετάσεων & Ασκήσεων (Lesson 0: Exam Instructions & Rubrics)"
            }
        ]
    }
    # Insert unit-00 at the very top of units list
    manifest["units"].insert(0, unit_00_entry)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"[OK] Added unit-00 at position 0 in {MANIFEST_PATH.name}")
else:
    print(f"[INFO] unit-00 already exists in {MANIFEST_PATH.name}")

print("\nUnit 0 creation script finished successfully!")

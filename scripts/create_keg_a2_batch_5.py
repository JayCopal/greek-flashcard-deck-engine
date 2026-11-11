# -*- coding: utf-8 -*-
"""
Generate KEG-A2 Batch 5:
- Unit A2-09: KEG-A2-09-A (35 cards) - Workplaces, CVs & Classified Ads (Εργασία, Επαγγέλματα & Αγγελίες)
- Unit A2-10: KEG-A2-10-A (35 cards) - Health, Accidents & Medical Consultation (Υγεία, Ατυχήματα & Φαρμακείο)
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
# UNIT A2-09 CARDS (35 cards)
# Theme: Workplaces, CVs & Classified Ads (Εργασία & Αγγελίες)
# -------------------------------------------------------------
CARDS_U09 = [
    {
        "id": "A2-U09-001",
        "greek": "η αγγελία εργασίας",
        "english": "job advertisement / vacancy listing",
        "notes": "Feminine noun phrase. Fundamental authentic genre in KEG A2 Reading Section 3 (matching job ads with candidates).",
        "gender_or_pos": "noun phrase (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "plural": "οι αγγελίες εργασίας",
            "genitive": "της αγγελίας εργασίας"
        },
        "keg_communicative_function": "Analyzing job offers, qualifications, and employment terms in classifieds",
        "example_el": "Είδα μια πολύ ενδιαφέρουσα αγγελία εργασίας για γραμματέα σε δικηγορικό γραφείο.",
        "example_en": "I saw a very interesting job advertisement for a secretary at a law office.",
        "example2_el": "Η αγγελία ζητάει άτομο με άριστη γνώση υπολογιστών και εμπειρία στις πωλήσεις.",
        "example2_en": "The ad asks for an individual with excellent computer knowledge and sales experience."
    },
    {
        "id": "A2-U09-002",
        "greek": "ο μισθός",
        "english": "salary / wage",
        "notes": "Masculine noun in -ός (-οί). Collocates with 'βασικός μισθός' (minimum wage) and 'καθαρός μισθός' (net salary).",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι μισθοί",
            "collocation": "βασικός μισθός (minimum wage)"
        },
        "keg_communicative_function": "Inquiring about remuneration and payment terms in job interviews",
        "example_el": "Ο μηνιαίος μισθός καταβάλλεται στον τραπεζικό λογαριασμό την τελευταία εργάσιμη ημέρα.",
        "example_en": "The monthly salary is paid into the bank account on the last working day.",
        "example2_el": "Προσφέρουν ικανοποιητικό μισθό και δυνατότητα επαγγελματικής εξέλιξης.",
        "example2_en": "They offer a satisfactory salary and potential for career development."
    },
    {
        "id": "A2-U09-003",
        "greek": "η προϋπηρεσία",
        "english": "previous work experience",
        "notes": "Feminine noun in -α. Compound: προ + υπηρεσία. Prime requirement in Greek job applications.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "collocation": "προϋπηρεσία τουλάχιστον δύο ετών (at least two years of experience)"
        },
        "keg_communicative_function": "Detailing professional background and years of service in CVs",
        "example_el": "Απαιτείται προϋπηρεσία τουλάχιστον τριών ετών σε αντίστοιχη θέση.",
        "example_en": "At least three years of previous experience in an equivalent position is required.",
        "example2_el": "Έχω πενταετή προϋπηρεσία στον τομέα της φιλοξενίας και του τουρισμού.",
        "example2_en": "I have five years of previous work experience in the hospitality and tourism sector."
    },
    {
        "id": "A2-U09-004",
        "greek": "τα προσόντα",
        "english": "qualifications / credentials",
        "notes": "Neuter plural noun (singular 'το προσόν' is rare). Essential heading in CVs and vacancies.",
        "gender_or_pos": "noun (neuter plural)",
        "grammatical_info": {
            "part_of_speech": "noun (plural)",
            "genitive_plural": "των προσόντων",
            "collocation": "απαιτούμενα προσόντα (required qualifications)"
        },
        "keg_communicative_function": "Matching candidate profiles with employment prerequisites",
        "example_el": "Τα βασικά προσόντα για τη θέση περιλαμβάνουν πτυχίο πανεπιστημίου και ξένες γλώσσες.",
        "example_en": "The basic qualifications for the position include a university degree and foreign languages.",
        "example2_el": "Διαθέτει όλα τα απαραίτητα τυπικά και ουσιαστικά προσόντα.",
        "example2_en": "He possesses all the necessary formal and substantive qualifications."
    },
    {
        "id": "A2-U09-005",
        "greek": "η πλήρης απασχόληση",
        "english": "full-time employment",
        "notes": "Feminine noun phrase. Contrast: 'η μερική απασχόληση' (part-time).",
        "gender_or_pos": "noun phrase (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "antonym": "η μερική απασχόληση (part-time)",
            "adjective": "πλήρης (full)"
        },
        "keg_communicative_function": "Specifying contract working modality in job searches and interviews",
        "example_el": "Η εταιρεία αναζητά υπάλληλο γραφείου για πλήρη απασχόληση.",
        "example_en": "The company is seeking an office clerk for full-time employment.",
        "example2_el": "Προτιμώ την πλήρη απασχόληση επειδή παρέχει μεγαλύτερη σταθερότητα.",
        "example2_en": "I prefer full-time employment because it provides greater stability."
    },
    {
        "id": "A2-U09-006",
        "greek": "η μερική απασχόληση",
        "english": "part-time employment",
        "notes": "Feminine noun phrase. Contrast: 'η πλήρης απασχόληση'.",
        "gender_or_pos": "noun phrase (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "antonym": "η πλήρης απασχόληση"
        },
        "keg_communicative_function": "Discussing flexible student jobs and part-time shifts",
        "example_el": "Ως φοιτητής εργαζόμουν με μερική απασχόληση σε ένα βιβλιοπωλείο.",
        "example_en": "As a student I worked part-time at a bookstore.",
        "example2_el": "Η θέση αφορά μερική απασχόληση τεσσάρων ωρών ημερησίως.",
        "example2_en": "The position concerns part-time employment of four hours daily."
    },
    {
        "id": "A2-U09-007",
        "greek": "η συνέντευξη εργασίας",
        "english": "job interview",
        "notes": "Feminine noun phrase. Relates to 'δίνω συνέντευξη' (to give an interview).",
        "gender_or_pos": "noun phrase (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "plural": "οι συνεντεύξεις εργασίας",
            "collocation": "περνάω από συνέντευξη"
        },
        "keg_communicative_function": "Preparing for and describing employment interviews in speaking Stage 1",
        "example_el": "Αύριο το πρωί έχω μια κρίσιμη συνέντευξη εργασίας με τον υπεύθυνο προσωπικού.",
        "example_en": "Tomorrow morning I have a crucial job interview with the HR manager.",
        "example2_el": "Στη συνέντευξη εργασίας με ρώτησαν για την εμπειρία μου και τους στόχους μου.",
        "example2_en": "In the job interview they asked me about my experience and my goals."
    },
    {
        "id": "A2-U09-008",
        "greek": "η σύμβαση",
        "english": "employment contract / agreement",
        "notes": "Feminine noun in -η (-εις). Collocates with 'σύμβαση αορίστου χρόνου' (permanent contract) or 'ορισμένου χρόνου' (fixed-term).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι συμβάσεις",
            "collocation": "υπογράφω σύμβαση (to sign a contract)"
        },
        "keg_communicative_function": "Understanding formal employment terms and contract conditions",
        "example_el": "Υπέγραψα σύμβαση εργασίας αορίστου χρόνου με την εταιρεία πληροφορικής.",
        "example_en": "I signed an open-ended employment contract with the IT company.",
        "example2_el": "Διαβάστε προσεκτικά όλους τους όρους πριν υπογράψετε τη σύμβαση.",
        "example2_en": "Read all terms carefully before signing the contract."
    },
    {
        "id": "A2-U09-009",
        "greek": "οι υπερωρίες",
        "english": "overtime (hours)",
        "notes": "Feminine noun plural (singular 'η υπερωρία'). Collocates with 'πληρώνομαι υπερωρίες'.",
        "gender_or_pos": "noun (feminine plural)",
        "grammatical_info": {
            "part_of_speech": "noun (plural)",
            "singular": "η υπερωρία",
            "verb": "κάνω υπερωρίες"
        },
        "keg_communicative_function": "Negotiating working schedule limits and overtime payments",
        "example_el": "Όταν υπάρχει πολλή δουλειά, κάνουμε υπερωρίες οι οποίες πληρώνονται επιπλέον.",
        "example_en": "When there is a lot of work, we work overtime which is paid extra.",
        "example2_el": "Ο νόμος καθορίζει το ανώτατο όριο υπερωριών ανά μήνα.",
        "example2_en": "The law defines the maximum limit of overtime per month."
    },
    {
        "id": "A2-U09-010",
        "greek": "η ασφάλιση",
        "english": "insurance / social security coverage",
        "notes": "Feminine noun in -η (-εις). Core civic entitlement (ΕΦΚΑ).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ασφαλίσεις",
            "collocation": "κοινωνική ασφάλιση, ασφάλιση υγείας"
        },
        "keg_communicative_function": "Clarifying social security benefits and health coverage in employment inquiries",
        "example_el": "Η θέση παρέχει πλήρη ασφάλιση υγείας και συνταξιοδοτικά δικαιώματα.",
        "example_en": "The position provides full health insurance and pension rights.",
        "example2_el": "Πρέπει να ελέγξετε αν η ασφάλισή σας είναι ενεργή.",
        "example2_en": "You must check whether your insurance coverage is active."
    },
    {
        "id": "A2-U09-011",
        "greek": "τα ένσημα",
        "english": "social security contributions / stamps",
        "notes": "Neuter plural noun. Quintessential Greek labor system concept denoting registered workdays.",
        "gender_or_pos": "noun (neuter plural)",
        "grammatical_info": {
            "part_of_speech": "noun (plural)",
            "singular": "το ένσημο",
            "collocation": "κολλάω ένσημα (to accrue social security stamps)"
        },
        "keg_communicative_function": "Confirming legal registration of working days and insurance stamps",
        "example_el": "Ο εργοδότης είναι υποχρεωμένος να κολλάει όλα τα νόμιμα ένσημα στον εργαζόμενο.",
        "example_en": "The employer is obliged to contribute all legal social security stamps for the employee.",
        "example2_el": "Χρειάζομαι βεβαίωση ενσήμων από τον ασφαλιστικό μου φορέα.",
        "example2_en": "I need an attestation of insurance stamps from my social security agency."
    },
    {
        "id": "A2-U09-012",
        "greek": "ο εργαζόμενος",
        "english": "employee / worker",
        "notes": "Masculine substantivized participle (-ος, -η, -ο). Plural: 'οι εργαζόμενοι'.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "feminine": "η εργαζόμενη",
            "plural": "οι εργαζόμενοι",
            "antonym": "ο εργοδότης"
        },
        "keg_communicative_function": "Discussing workers' rights, schedules, and responsibilities",
        "example_el": "Οι εργαζόμενοι της επιχείρησης δικαιούνται ετήσια άδεια με αποδοχές.",
        "example_en": "Employees of the enterprise are entitled to annual paid leave.",
        "example2_el": "Είναι ένας πολύ συνεπής και εργατικός εργαζόμενος.",
        "example2_en": "He is a very punctual and hardworking employee."
    },
    {
        "id": "A2-U09-013",
        "greek": "ο εργοδότης",
        "english": "employer",
        "notes": "Masculine noun in -ης (-ες). Feminine: 'η εργοδότρια'. Antonym: 'ο εργαζόμενος'.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι εργοδότες",
            "feminine": "η εργοδότρια",
            "antonym": "ο εργαζόμενος"
        },
        "keg_communicative_function": "Referring to management and employer responsibilities in workplace texts",
        "example_el": "Ο εργοδότης οφείλει να διασφαλίζει συνθήκες υγιεινής και ασφάλειας στον χώρο εργασίας.",
        "example_en": "The employer is obliged to ensure health and safety conditions in the workplace.",
        "example2_el": "Είχαμε μια εποικοδομητική συζήτηση με τον νέο εργοδότη.",
        "example2_en": "We had a constructive discussion with the new employer."
    },
    {
        "id": "A2-U09-014",
        "greek": "η πρόσληψη",
        "english": "hiring / recruitment",
        "notes": "Feminine noun in -η (-εις). Verb: 'προσλαμβάνω' (to hire). Antonym: 'η απόλυση'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι προσλήψεις",
            "verb": "προσλαμβάνω",
            "antonym": "η απόλυση"
        },
        "keg_communicative_function": "Recognizing announcement of new hirings or job vacancy offers",
        "example_el": "Η εταιρεία ανακοίνωσε την πρόσληψη είκοσι νέων προγραμματιστών.",
        "example_en": "The company announced the hiring of twenty new software developers.",
        "example2_el": "Μετά τη δεύτερη συνέντευξη έλαβα την επίσημη ειδοποίηση πρόσληψης.",
        "example2_en": "After the second interview I received the official hiring notification."
    },
    {
        "id": "A2-U09-015",
        "greek": "προσλαμβάνω",
        "english": "to hire / to employ",
        "notes": "Active compound verb (προς + λαμβάνω). Simple past: 'προσέλαβα'. Simple future: 'θα προσλάβω'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "προσέλαβα",
            "simple_future": "θα προσλάβω",
            "noun_derivative": "η πρόσληψη"
        },
        "keg_communicative_function": "Describing recruitment decisions and employer actions in business dialogues",
        "example_el": "Το ξενοδοχείο προσλαμβάνει προσωπικό για την καλοκαιρινή τουριστική περίοδο.",
        "example_en": "The hotel is hiring staff for the summer tourist season.",
        "example2_el": "Με προσέλαβαν αμέσως μόλις είδαν τις συστατικές μου επιστολές.",
        "example2_en": "They hired me immediately as soon as they saw my reference letters."
    },
    {
        "id": "A2-U09-016",
        "greek": "παραιτούμαι",
        "english": "to resign / to step down",
        "notes": "Deponent verb (παραιτούμαι, παραιτείσαι, παραιτείται). Simple past: 'παραιτήθηκα'.",
        "gender_or_pos": "verb (deponent)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "παραιτήθηκα",
            "simple_future": "θα παραιτηθώ",
            "noun_derivative": "η παραίτηση"
        },
        "keg_communicative_function": "Explaining past career transitions and resignation motives in interviews",
        "example_el": "Παραιτήθηκα από την προηγούμενη δουλειά μου επειδή δεν υπήρχε προοπτική εξέλιξης.",
        "example_en": "I resigned from my previous job because there was no prospect of advancement.",
        "example2_el": "Υπέβαλε την παραίτησή του και αποφάσισε να κάνει ένα νέο ξεκίνημα.",
        "example2_en": "He submitted his resignation and decided to make a fresh start."
    },
    {
        "id": "A2-U09-017",
        "greek": "αναζητώ",
        "english": "to seek / to look for",
        "notes": "Formal verb (αναζητώ, αναζητάς/αναζητείς). Standard formula in job ads: 'εταιρεία αναζητά...'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "αναζήτησα",
            "noun_derivative": "η αναζήτηση"
        },
        "keg_communicative_function": "Identifying employer search criteria in newspaper and online vacancy listings",
        "example_el": "Μεγάλη εμπορική εταιρεία αναζητά άμεσα πωλητή με άριστες επικοινωνιακές δεξιότητες.",
        "example_en": "A large commercial company is actively seeking a salesperson with excellent communication skills.",
        "example2_el": "Αναζητώ μια σταθερή εργασία με προοπτικές μακροχρόνιας συνεργασίας.",
        "example2_en": "I am seeking a stable job with long-term collaboration prospects."
    },
    {
        "id": "A2-U09-018",
        "greek": "αν",
        "english": "if (conditional particle)",
        "notes": "Conditional conjunction. Variant: 'εάν'. At A2 level, introduces Type 1 conditionals: 'αν + ενεστώτας -> μέλλοντας'.",
        "gender_or_pos": "conjunction",
        "grammatical_info": {
            "part_of_speech": "conditional conjunction",
            "variant": "εάν",
            "type_1_rule": "αν + ενεστώτας -> θα + συνοπτικός μέλλοντας"
        },
        "keg_communicative_function": "Stating realistic conditions and their future outcomes in advice & proposals",
        "example_el": "Αν περάσετε τις εξετάσεις του Μαΐου, θα αποκτήσετε το επίσημο πιστοποιητικό.",
        "example_en": "If you pass the May exams, you will obtain the official certificate.",
        "example2_el": "Αν έχετε απορίες σχετικά με την αγγελία, καλέστε στο τηλέφωνο της εταιρείας.",
        "example2_en": "If you have questions regarding the advertisement, call the company phone."
    },
    {
        "id": "A2-U09-019",
        "greek": "μόλις",
        "english": "as soon as / just now",
        "notes": "Temporal conjunction taking subjunctive or past: 'μόλις λάβω' (as soon as I receive), 'μόλις έφτασα' (I just arrived).",
        "gender_or_pos": "conjunction / adverb",
        "grammatical_info": {
            "part_of_speech": "conjunction",
            "syntax": "μόλις + υποτακτική (future time) / μόλις + αόριστος (immediate past)"
        },
        "keg_communicative_function": "Sequencing immediate successive actions in business correspondence",
        "example_el": "Θα σας ενημερώσω μόλις ολοκληρωθεί η αξιολόγηση των βιογραφικών.",
        "example_en": "I will inform you as soon as the evaluation of CVs is completed.",
        "example2_el": "Μόλις έλαβα την επιστολή αποδοχής της αίτησής μου.",
        "example2_en": "I just received the letter of acceptance of my application."
    },
    {
        "id": "A2-U09-020",
        "greek": "αφού",
        "english": "after / since",
        "notes": "Subordinating temporal conjunction taking past tense or subjunctive.",
        "gender_or_pos": "conjunction",
        "grammatical_info": {
            "part_of_speech": "conjunction",
            "temporal_role": "marks prior action before main clause"
        },
        "keg_communicative_function": "Narrating chronological sequences in past career achievements",
        "example_el": "Αφού τελείωσε το πανεπιστήμιο, έκανε πρακτική άσκηση σε μεγάλη τράπεζα.",
        "example_en": "After finishing university, she did an internship at a major bank.",
        "example2_el": "Αφού συμφωνήσουμε στους όρους, θα προχωρήσουμε στην υπογραφή της σύμβασης.",
        "example2_en": "After we agree on the terms, we will proceed to signing the contract."
    },
    {
        "id": "A2-U09-021",
        "greek": "πριν",
        "english": "before",
        "notes": "Temporal conjunction/adverb. Followed by 'να + subjunctive': 'πριν υπογράψετε'.",
        "gender_or_pos": "conjunction / adverb",
        "grammatical_info": {
            "part_of_speech": "conjunction",
            "syntax": "πριν να + υποτακτική / πριν από + ουσιαστικό",
            "antonym": "μετά"
        },
        "keg_communicative_function": "Setting cautionary pre-conditions in administrative and legal processes",
        "example_el": "Ελέγξτε προσεκτικά τα στοιχεία σας πριν στείλετε το ηλεκτρονικό μήνυμα.",
        "example_en": "Check your details carefully before sending the email.",
        "example2_el": "Πριν από τη συνέντευξη καλό είναι να ενημερωθείτε για το προφίλ της εταιρείας.",
        "example2_en": "Before the interview it is wise to get informed about the company's profile."
    },
    {
        "id": "A2-U09-022",
        "greek": "η προϋπόθεση",
        "english": "prerequisite / condition",
        "notes": "Feminine noun in -η (-εις). Essential in criteria descriptions: 'υπό την προϋπόθεση ότι'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι προϋποθέσεις",
            "collocation": "βασική προϋπόθεση (key prerequisite)"
        },
        "keg_communicative_function": "Comprehending strict admission criteria and prerequisites in job and exam ads",
        "example_el": "Η καλή γνώση της ελληνικής γλώσσας είναι απαραίτητη προϋπόθεση για την πρόσληψη.",
        "example_en": "Good knowledge of the Greek language is an essential prerequisite for hiring.",
        "example2_el": "Πληροίτε όλες τις προϋποθέσεις που ορίζει ο διαγωνισμός;",
        "example2_en": "Do you meet all the conditions set by the competition?"
    },
    {
        "id": "A2-U09-023",
        "greek": "τα καθήκοντα",
        "english": "duties / responsibilities / tasks",
        "notes": "Neuter plural noun (singular 'το καθήκον'). Key section in any employment specification.",
        "gender_or_pos": "noun (neuter plural)",
        "grammatical_info": {
            "part_of_speech": "noun (plural)",
            "singular": "το καθήκον",
            "genitive_plural": "των καθηκόντων",
            "collocation": "εκτελώ τα καθήκοντά μου"
        },
        "keg_communicative_function": "Describing job role responsibilities and daily functions",
        "example_el": "Στα κύρια καθήκοντά σας περιλαμβάνεται η καθημερινή επικοινωνία με τους πελάτες.",
        "example_en": "Your main duties include daily communication with clients.",
        "example2_el": "Ανέλαβε τα νέα του καθήκοντα ως υπεύθυνος τμήματος από την 1η του μηνός.",
        "example2_en": "He assumed his new duties as department head starting on the 1st of the month."
    },
    {
        "id": "A2-U09-024",
        "greek": "το περιβάλλον εργασίας",
        "english": "working environment",
        "notes": "Neuter noun phrase. Standard term in attractive employer branding.",
        "gender_or_pos": "noun phrase (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "collocation": "ευχάριστο περιβάλλον εργασίας (pleasant work environment)"
        },
        "keg_communicative_function": "Describing company culture and physical work atmosphere",
        "example_el": "Η εταιρεία προσφέρει ευχάριστο και δυναμικό περιβάλλον εργασίας με συνεχή εκπαίδευση.",
        "example_en": "The company offers a pleasant and dynamic working environment with continuous training.",
        "example2_el": "Ένα υγιές περιβάλλον εργασίας ενισχύει τη δημιουργικότητα και τη συνεργασία.",
        "example2_en": "A healthy working environment fosters creativity and collaboration."
    },
    {
        "id": "A2-U09-025",
        "greek": "η εξέλιξη",
        "english": "development / career progression / evolution",
        "notes": "Feminine noun in -η (-εις). Collocates with 'δυνατότητα εξέλιξης' (advancement opportunity).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι εξελίξεις",
            "verb": "εξελίσσομαι",
            "collocation": "επαγγελματική εξέλιξη (career progression)"
        },
        "keg_communicative_function": "Discussing career ambitions and professional growth prospects in interviews",
        "example_el": "Αναζητώ μια θέση που να προσφέρει πραγματικές δυνατότητες επαγγελματικής εξέλιξης.",
        "example_en": "I am seeking a position that offers real possibilities for professional advancement.",
        "example2_el": "Η τεχνολογική εξέλιξη έχει αλλάξει τον τρόπο με τον οποίο εργαζόμαστε.",
        "example2_en": "Technological evolution has changed the way we work."
    },
    {
        "id": "A2-U09-026",
        "greek": "ικανός",
        "english": "capable / competent / skilled",
        "notes": "Adjective in -ός, -ή, -ό. Antonym: 'ανίκανος'. Collocates with 'ικανός να' + subjunctive.",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "ικανή",
            "neuter": "ικανό",
            "noun": "η ικανότητα (ability)"
        },
        "keg_communicative_function": "Highlighting personal competences and problem-solving abilities in CVs",
        "example_el": "Είναι ένας ιδιαίτερα ικανός επαγγελματίας που ανταποκρίνεται σε δύσκολες προκλήσεις.",
        "example_en": "He is an exceptionally capable professional who rises to difficult challenges.",
        "example2_el": "Αισθάνομαι ικανός να αναλάβω αυξημένες ευθύνες στο τμήμα.",
        "example2_en": "I feel capable of undertaking increased responsibilities in the department."
    },
    {
        "id": "A2-U09-027",
        "greek": "έμπειρος",
        "english": "experienced",
        "notes": "Adjective in -ος, -η, -ο. Derived from 'η εμπειρία' (experience). Antonym: 'άπειρος'.",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "feminine": "έμπειρη",
            "neuter": "έμπειρο",
            "antonym": "άπειρος (inexperienced)",
            "noun": "η εμπειρία"
        },
        "keg_communicative_function": "Presenting accumulated professional experience in applications and dialogues",
        "example_el": "Η ομάδα μας αποτελείται από έμπειρους καθηγητές με πολυετή διδακτική πείρα.",
        "example_en": "Our team consists of experienced teachers with multi-year teaching experience.",
        "example2_el": "Ζητείται έμπειρος λογιστής για πλήρη απασχόληση.",
        "example2_en": "An experienced accountant is sought for full-time employment."
    },
    {
        "id": "A2-U09-028",
        "greek": "υπεύθυνος",
        "english": "responsible / in charge",
        "notes": "Adjective in -ος, -η, -ο. Substantivized 'ο υπεύθυνος' means the manager / person in charge.",
        "gender_or_pos": "adjective / noun",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "noun_use": "ο υπεύθυνος (the manager in charge)",
            "noun_quality": "η υπευθυνότητα (responsibility)"
        },
        "keg_communicative_function": "Demonstrating reliability and designating departmental heads",
        "example_el": "Είμαι υπεύθυνος για την εξυπηρέτηση των πελατών και τη διαχείριση παραγγελιών.",
        "example_en": "I am responsible for customer service and order management.",
        "example2_el": "Μπορώ να μιλήσω με τον υπεύθυνο του καταστήματος παρακαλώ;",
        "example2_en": "May I speak with the store manager please?"
    },
    {
        "id": "A2-U09-029",
        "greek": "η συνεργασία",
        "english": "cooperation / collaboration",
        "notes": "Feminine noun in -α (-ες). Relates to 'συνεργάζομαι' (to cooperate). Standard in formal letter closings.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι συνεργασίες",
            "verb": "συνεργάζομαι",
            "collocation": "προσβλέπω σε μια γόνιμη συνεργασία"
        },
        "keg_communicative_function": "Expressing desire for professional teamwork and successful partnerships",
        "example_el": "Σας ευχαριστώ εκ των προτέρων και προσβλέπω σε μια άριστη συνεργασία.",
        "example_en": "I thank you in advance and look forward to an excellent collaboration.",
        "example2_el": "Η καλή συνεργασία μεταξύ των συναδέλφων είναι απαραίτητη για την επιτυχία του έργου.",
        "example2_en": "Good collaboration among colleagues is essential for the project's success."
    },
    {
        "id": "A2-U09-030",
        "greek": "η απόλυση",
        "english": "dismissal / layoff / termination",
        "notes": "Feminine noun in -η (-εις). Verb: 'απολύω' (to dismiss). Antonym: 'η πρόσληψη'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι απολύσεις",
            "verb": "απολύω",
            "antonym": "η πρόσληψη"
        },
        "keg_communicative_function": "Discussing labor news and employment disruptions in Reading Part 2",
        "example_el": "Σε περίπτωση απόλυσης, ο εργαζόμενος δικαιούται νόμιμη αποζημίωση.",
        "example_en": "In case of dismissal, the employee is entitled to statutory compensation.",
        "example2_el": "Το εργοστάσιο ανακοίνωσε ότι δεν θα προχωρήσει σε απολύσεις προσωπικού.",
        "example2_en": "The factory announced that it will not proceed with staff layoffs."
    },
    {
        "id": "A2-U09-031",
        "greek": "το επίδομα",
        "english": "allowance / benefit / subsidy",
        "notes": "Neuter noun in -μα (-ματα). Examples: επίδομα ανεργίας (unemployment benefit), επίδομα αδείας (holiday bonus).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα επιδόματα",
            "genitive_singular": "του επιδόματος",
            "collocation": "επίδομα ανεργίας (unemployment benefit)"
        },
        "keg_communicative_function": "Understanding state welfare allowances and social benefits at public agencies",
        "example_el": "Υπέβαλε τα δικαιολογητικά στη ΔΥΠΑ για να λάβει το επίδομα ανεργίας.",
        "example_en": "He submitted the supporting documents to DYPA to receive the unemployment benefit.",
        "example2_el": "Ο νόμος προβλέπει επίδομα τέκνων για οικογένειες με χαμηλό εισόδημα.",
        "example2_en": "The law provides a child allowance for low-income families."
    },
    {
        "id": "A2-U09-032",
        "greek": "η άδεια με αποδοχές",
        "english": "paid leave",
        "notes": "Feminine noun phrase. 'Αποδοχές' = earnings/salary.",
        "gender_or_pos": "noun phrase (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "contrast": "άδεια άνευ αποδοχών (unpaid leave)"
        },
        "keg_communicative_function": "Inquiring about statutory annual vacation rights in employment negotiations",
        "example_el": "Κάθε εργαζόμενος στον ιδιωτικό τομέα δικαιούται κανονική άδεια με αποδοχές.",
        "example_en": "Every worker in the private sector is entitled to regular paid leave.",
        "example2_el": "Ζήτησε τρεις μέρες άδεια με αποδοχές για οικογενειακούς λόγους.",
        "example2_en": "She requested three days paid leave for family reasons."
    },
    {
        "id": "A2-U09-033",
        "greek": "το ωράριο εργασίας",
        "english": "working hours / work schedule",
        "notes": "Neuter noun phrase. Collocates with 'ευέλικτο ωράριο' (flexible hours) or 'συνεχές ωράριο'.",
        "gender_or_pos": "noun phrase (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "plural": "τα ωράρια εργασίας",
            "collocation": "ευέλικτο ωράριο (flexible schedule)"
        },
        "keg_communicative_function": "Agreeing on daily shift hours and weekly schedules",
        "example_el": "Το ωράριο εργασίας είναι οκτάωρο, από τις εννιά το πρωί έως τις πέντε το απόγευμα.",
        "example_en": "The working schedule is eight hours, from nine in the morning until five in the afternoon.",
        "example2_el": "Προτιμώ μια δουλειά με σταθερό ωράριο χωρίς νυχτερινές βάρδιες.",
        "example2_en": "I prefer a job with fixed hours without night shifts."
    },
    {
        "id": "A2-U09-034",
        "greek": "διαπραγματεύομαι",
        "english": "to negotiate",
        "notes": "Deponent verb. Simple past: 'διαπραγματεύτηκα'. Relates to 'η διαπραγμάτευση'.",
        "gender_or_pos": "verb (deponent)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "διαπραγματεύτηκα",
            "noun_derivative": "η διαπραγμάτευση"
        },
        "keg_communicative_function": "Negotiating salary terms, schedules, or commercial agreements",
        "example_el": "Στη συνέντευξη διαπραγματεύτηκε έναν καλύτερο βασικό μισθό.",
        "example_en": "In the interview he negotiated a better base salary.",
        "example2_el": "Είναι σημαντικό να γνωρίζεις τα δικαιώματά σου πριν διαπραγματευτείς τους όρους.",
        "example2_en": "It is important to know your rights before you negotiate the terms."
    },
    {
        "id": "A2-U09-035",
        "greek": "το επάγγελμα",
        "english": "profession / occupation",
        "notes": "Neuter noun in -μα (-ματα). Key question in Speaking Stage 1 ('Ποιο είναι το επάγγελμά σας;').",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα επαγγέλματα",
            "genitive_singular": "του επαγγέλματος",
            "adjective": "επαγγελματικός, -ή, -ό"
        },
        "keg_communicative_function": "Stating one's profession, trade, and career history in candidate interviews",
        "example_el": "Ποιο είναι το επάγγελμά σας και πόσα χρόνια εργάζεστε σε αυτόν τον τομέα;",
        "example_en": "What is your profession and how many years have you been working in this sector?",
        "example2_el": "Το επάγγελμα του μεταφραστή απαιτεί διαρκή γλωσσική εξάσκηση και ακρίβεια.",
        "example2_en": "The profession of translator requires continuous linguistic practice and precision."
    }
]

# -------------------------------------------------------------
# UNIT A2-10 CARDS (35 cards)
# Theme: Health, Accidents & Medical Consultation (Υγεία & Φαρμακείο)
# -------------------------------------------------------------
CARDS_U10 = [
    {
        "id": "A2-U10-001",
        "greek": "πονάω",
        "english": "to hurt / to ache / I feel pain",
        "notes": "Group B1 verb (πονάω / πονώ). Takes direct object of body part: 'πονάει το κεφάλι μου' (my head hurts) or 'πονάω στο στομάχι'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "third_person": "πονάει / πονούν",
            "simple_past": "πόνεσα",
            "noun_derivative": "ο πόνος (pain)"
        },
        "keg_communicative_function": "Describing localized pain and physical discomfort to a doctor or pharmacist",
        "example_el": "Με πονάει πολύ ο λαιμός μου και δυσκολεύομαι να καταπιώ.",
        "example_en": "My throat hurts a lot and I have difficulty swallowing.",
        "example2_el": "Πονάει το στομάχι μου από χθες το βράδυ, χρειάζομαι ένα παυσίπονο.",
        "example2_en": "My stomach has been aching since yesterday evening; I need a painkiller."
    },
    {
        "id": "A2-U10-002",
        "greek": "αισθάνομαι",
        "english": "to feel / I feel",
        "notes": "Deponent verb (αισθάνομαι, αισθάνεσαι, αισθάνεται). Simple past: 'αισθάνθηκα' or 'ένιωσα'. Collocates with 'αισθάνομαι άρρωστος / καλά'.",
        "gender_or_pos": "verb (deponent)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "αισθάνθηκα",
            "synonym": "νιώθω",
            "noun_derivative": "το αίσθημα"
        },
        "keg_communicative_function": "Explaining general physical and psychological symptoms during clinical consultations",
        "example_el": "Αισθάνομαι έντονη αδυναμία και ζαλάδα από το πρωί.",
        "example_en": "I feel intense weakness and dizziness since morning.",
        "example2_el": "Πώς αισθάνεστε σήμερα μετά τη λήψη των φαρμάκων;",
        "example2_en": "How do you feel today after taking the medicines?"
    },
    {
        "id": "A2-U10-003",
        "greek": "ο πυρετός",
        "english": "fever / temperature",
        "notes": "Masculine noun in -ός (-οί). Collocates with 'έχω / ανεβάζω πυρετό' (to have/run a fever).",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι πυρετοί",
            "collocation": "έχω πυρετό (I have a fever), βάζω θερμόμετρο"
        },
        "keg_communicative_function": "Reporting body temperature and fever spikes to medical staff",
        "example_el": "Το παιδί ανέβασε υψηλό πυρετό, σχεδόν τριάντα εννέα βαθμούς.",
        "example_en": "The child developed a high fever, nearly thirty-nine degrees.",
        "example2_el": "Πάρτε αυτό το αντιπυρετικό σιρόπι για να πέσει ο πυρετός.",
        "example2_en": "Take this antipyretic syrup to bring the fever down."
    },
    {
        "id": "A2-U10-004",
        "greek": "ο πονοκέφαλος",
        "english": "headache",
        "notes": "Masculine compound noun: πόνος + κεφάλι. Plural: 'οι πονοκέφαλοι'.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι πονοκέφαλοι",
            "collocation": "έντονος πονοκέφαλος"
        },
        "keg_communicative_function": "Stating head aches and asking for analgesic tablets in pharmacy role-plays",
        "example_el": "Έχω έναν αφόρητο πονοκέφαλο, έχετε κάτι αποτελεσματικό για να μου δώσετε;",
        "example_en": "I have an unbearable headache; do you have something effective to give me?",
        "example2_el": "Η πολλή ώρα μπροστά στην οθόνη του υπολογιστή μού προκαλεί συχνά πονοκέφαλο.",
        "example2_en": "Too much time in front of the computer screen often causes me a headache."
    },
    {
        "id": "A2-U10-005",
        "greek": "ο πονόλαιμος",
        "english": "sore throat",
        "notes": "Masculine compound noun: πόνος + λαιμός. Common symptom of seasonal infections.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι πονόλαιμοι",
            "collocation": "καραμέλες για τον πονόλαιμο"
        },
        "keg_communicative_function": "Requesting throat lozenges or sprays at the pharmacy",
        "example_el": "Ο πονόλαιμος δεν με αφήνει να μιλήσω καθαρά, θα ήθελα καραμέλες με μέλι.",
        "example_en": "My sore throat won't let me speak clearly; I would like lozenges with honey.",
        "example2_el": "Αν ο πονόλαιμος επιμένει για μέρες, πρέπει να σας εξετάσει ένας γιατρός.",
        "example2_en": "If the sore throat persists for days, a doctor must examine you."
    },
    {
        "id": "A2-U10-006",
        "greek": "ο βήχας",
        "english": "cough",
        "notes": "Masculine noun in -ας (-ες). Relates to 'βήχω' (to cough).",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "verb": "βήχω",
            "collocation": "ξηρός βήχας (dry cough)"
        },
        "keg_communicative_function": "Describing respiratory cough symptoms and buying cough syrups",
        "example_el": "Έχω έναν έντονο ξηρό βήχα που με ταλαιπωρεί κυρίως τη νύχτα.",
        "example_en": "I have an intense dry cough that bothers me mainly at night.",
        "example2_el": "Ο φαρμακοποιός μού συνέστησε ένα φυτικό σιρόπι για τον βήχα.",
        "example2_en": "The pharmacist recommended a herbal syrup for my cough."
    },
    {
        "id": "A2-U10-007",
        "greek": "το κρυολόγημα",
        "english": "common cold",
        "notes": "Neuter noun in -μα (-ματα). Relates to 'κρυολογώ' (to catch a cold).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κρυολογήματα",
            "verb": "κρυολογώ"
        },
        "keg_communicative_function": "Explaining school/work absences due to mild seasonal illness",
        "example_el": "Έμεινα στο σπίτι σήμερα επειδή με έπιασε ένα βαρύ κρυολόγημα.",
        "example_en": "I stayed home today because I caught a bad cold.",
        "example2_el": "Πίνετε ζεστό τσάι του βουνού με λεμόνι για να ανακουφιστείτε από το κρυολόγημα.",
        "example2_en": "Drink warm Greek mountain tea with lemon to relieve your cold."
    },
    {
        "id": "A2-U10-008",
        "greek": "η γρίπη",
        "english": "flu / influenza",
        "notes": "Feminine noun in -η. Relates to 'εποχική γρίπη' (seasonal flu).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "collocation": "εμβόλιο γρίπης (flu vaccine)"
        },
        "keg_communicative_function": "Distinguishing between a simple cold and contagious flu infections",
        "example_el": "Ο γιατρός είπε ότι δεν είναι απλό κρυολόγημα αλλά εποχική γρίπη.",
        "example_en": "The doctor said it is not a simple cold but seasonal flu.",
        "example2_el": "Χρειάζεται τουλάχιστον μία εβδομάδα ανάπαυση για να αναρρώσει κανείς από τη γρίπη.",
        "example2_en": "At least one week of rest is needed for someone to recover from the flu."
    },
    {
        "id": "A2-U10-009",
        "greek": "το φαρμακείο",
        "english": "pharmacy / chemist's shop",
        "notes": "Neuter noun in -ο (-α). Distinctive green cross sign across Greece. Open on rotational night shifts ('διανυκτερεύον φαρμακείο').",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα φαρμακεία",
            "collocation": "διανυκτερεύον φαρμακείο (on-duty night pharmacy)"
        },
        "keg_communicative_function": "Locating open pharmacies on weekends or during night emergencies",
        "example_el": "Πού μπορώ να βρω ένα εφημερεύον φαρμακείο ανοιχτό αυτή την ώρα;",
        "example_en": "Where can I find an on-duty pharmacy open at this hour?",
        "example2_el": "Τα φαρμακεία στην Ελλάδα προσφέρουν πρώτες βοήθειες και μέτρηση πίεσης.",
        "example2_en": "Pharmacies in Greece offer first aid and blood pressure checks."
    },
    {
        "id": "A2-U10-010",
        "greek": "το φάρμακο",
        "english": "medicine / medication / drug",
        "notes": "Neuter noun in -ο (-α). Collocates with 'παίρνω το φάρμακο' (to take medicine).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα φάρμακα",
            "genitive_singular": "του φαρμάκου",
            "genitive_plural": "των φαρμάκων"
        },
        "keg_communicative_function": "Asking for medicine dosages and usage instructions",
        "example_el": "Πρέπει να παίρνετε αυτό το φάρμακο τρεις φορές την ημέρα μετά το φαγητό.",
        "example_en": "You must take this medicine three times a day after meals.",
        "example2_el": "Μην παίρνετε φάρμακα χωρίς τη συμβουλή του γιατρού σας.",
        "example2_en": "Do not take medications without your doctor's advice."
    },
    {
        "id": "A2-U10-011",
        "greek": "η ιατρική συνταγή",
        "english": "medical prescription",
        "notes": "Feminine noun phrase. Collocates with 'γράφω / εκτελώ συνταγή'.",
        "gender_or_pos": "noun phrase (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "plural": "οι ιατρικές συνταγές",
            "collocation": "ηλεκτρονική συνταγογράφηση"
        },
        "keg_communicative_function": "Presenting electronic or paper prescriptions to pharmacists",
        "example_el": "Αυτό το αντιβιοτικό χορηγείται αποκλειστικά με ιατρική συνταγή.",
        "example_en": "This antibiotic is dispensed exclusively with a medical prescription.",
        "example2_el": "Ο γιατρός μού έστειλε τον κωδικό της ηλεκτρονικής συνταγής στο κινητό.",
        "example2_en": "The doctor sent me the electronic prescription code to my mobile."
    },
    {
        "id": "A2-U10-012",
        "greek": "το παυσίπονο",
        "english": "painkiller / analgesic",
        "notes": "Neuter compound noun: παύω (to stop) + πόνος (pain).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα παυσίπονα",
            "literal": "pain stopper"
        },
        "keg_communicative_function": "Requesting over-the-counter painkillers for toothache or headache",
        "example_el": "Πήρα ένα παυσίπονο επειδή δεν άντεχα άλλο τον πονόδοντο.",
        "example_en": "I took a painkiller because I couldn't bear the toothache any longer.",
        "example2_el": "Δώστε μου ένα κουτί παυσίπονα σε αναβράζοντα δισκία.",
        "example2_en": "Give me a box of painkillers in effervescent tablets."
    },
    {
        "id": "A2-U10-013",
        "greek": "το αντιβιοτικό",
        "english": "antibiotic",
        "notes": "Neuter noun in -ο (-α). Plural: 'τα αντιβιοτικά'.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα αντιβιοτικά",
            "collocation": "θεραπεία με αντιβιοτικά (antibiotic course)"
        },
        "keg_communicative_function": "Understanding prescription schedules for antibiotic treatments",
        "example_el": "Πρέπει να ολοκληρώσετε όλη τη θεραπεία με το αντιβιοτικό για επτά ημέρες.",
        "example_en": "You must complete the entire antibiotic treatment for seven days.",
        "example2_el": "Έχετε κάποια αλλεργία σε συγκεκριμένα αντιβιοτικά;",
        "example2_en": "Do you have any allergy to specific antibiotics?"
    },
    {
        "id": "A2-U10-014",
        "greek": "η πίεση",
        "english": "blood pressure",
        "notes": "Feminine noun in -η (-εις). Collocates with 'μετράω την πίεση' (to measure blood pressure).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πιέσεις",
            "collocation": "υψηλή πίεση (hypertension), μέτρηση πίεσης"
        },
        "keg_communicative_function": "Requesting a blood pressure check at a clinic or pharmacy",
        "example_el": "Μπορείτε να μου μετρήσετε την πίεση παρακαλώ; Νιώθω μια μικρή ζαλάδα.",
        "example_en": "Could you please measure my blood pressure? I feel a little dizzy.",
        "example2_el": "Η πίεσή σας είναι απολύτως φυσιολογική, δώδεκα με οκτώ.",
        "example2_en": "Your blood pressure is completely normal, twelve over eight."
    },
    {
        "id": "A2-U10-015",
        "greek": "η δόση",
        "english": "dosage / dose",
        "notes": "Feminine noun in -η (-εις). Essential instructions on medicine boxes.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι δόσεις",
            "collocation": "ημερήσια δόση (daily dosage)"
        },
        "keg_communicative_function": "Comprehending medicine intake schedules and dosage limits",
        "example_el": "Η συνιστώμενη δόση είναι ένα χάπι κάθε οκτώ ώρες.",
        "example_en": "The recommended dose is one pill every eight hours.",
        "example2_el": "Μην υπερβαίνετε τη μέγιστη ημερήσια δόση που αναγράφεται στο φυλλάδιο.",
        "example2_en": "Do not exceed the maximum daily dose indicated on the leaflet."
    },
    {
        "id": "A2-U10-016",
        "greek": "το ιατρικό ραντεβού",
        "english": "doctor's appointment",
        "notes": "Neuter noun phrase. Collocates with 'κλείνω ραντεβού με γιατρό'.",
        "gender_or_pos": "noun phrase (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "plural": "τα ιατρικά ραντεβού",
            "collocation": "κλείνω ραντεβού"
        },
        "keg_communicative_function": "Scheduling medical appointments with clinic receptionists over the phone",
        "example_el": "Θα ήθελα να κλείσω ένα ραντεβού με τον οφθαλμίατρο για την επόμενη εβδομάδα.",
        "example_en": "I would like to book an appointment with the ophthalmologist for next week.",
        "example2_el": "Υπάρχει διαθέσιμο ραντεβού το απόγευμα της Τετάρτης;",
        "example2_en": "Is there an available appointment on Wednesday afternoon?"
    },
    {
        "id": "A2-U10-017",
        "greek": "οι εξετάσεις αίματος",
        "english": "blood tests",
        "notes": "Feminine noun phrase plural (singular: η εξέταση αίματος). Routine diagnostic procedure.",
        "gender_or_pos": "noun phrase (feminine plural)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "singular": "η εξέταση αίματος",
            "collocation": "κάνω εξετάσεις αίματος"
        },
        "keg_communicative_function": "Arranging diagnostic lab tests and discussing results with medical practitioners",
        "example_el": "Ο παθολόγος μού συνέστησε να κάνω γενικές εξετάσεις αίματος και ούρων.",
        "example_en": "The general practitioner recommended that I do general blood and urine tests.",
        "example2_el": "Πρέπει να πάτε νηστικός στο μικροβιολογικό εργαστήριο για τις εξετάσεις αίματος.",
        "example2_en": "You must go fasting to the microbiology laboratory for the blood tests."
    },
    {
        "id": "A2-U10-018",
        "greek": "το ατύχημα",
        "english": "accident",
        "notes": "Neuter noun in -μα (-ματα). Examples: τροχαίο ατύχημα (traffic accident), εργατικό ατύχημα (workplace accident).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ατυχήματα",
            "genitive_singular": "του ατυχήματος",
            "collocation": "τροχαίο ατύχημα (traffic accident)"
        },
        "keg_communicative_function": "Reporting emergency incidents and vehicle collisions in dialogues and essays",
        "example_el": "Συνέβη ένα τροχαίο ατύχημα στη διασταύρωση, αλλά ευτυχώς χωρίς σοβαρούς τραυματισμούς.",
        "example_en": "A traffic accident occurred at the intersection, but fortunately without serious injuries.",
        "example2_el": "Η τροχαία διερευνά τα αίτια του ατυχήματος.",
        "example2_en": "The traffic police are investigating the causes of the accident."
    },
    {
        "id": "A2-U10-019",
        "greek": "το τραύμα",
        "english": "wound / injury / trauma",
        "notes": "Neuter noun in -μα (-ματα). Relates to 'τραυματίζομαι' (to get injured).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα τραύματα",
            "verb": "τραυματίζομαι",
            "adjective": "τραυματισμένος"
        },
        "keg_communicative_function": "Describing wounds and seeking emergency medical dressing",
        "example_el": "Ο γιατρός καθάρισε και απολύμανε προσεκτικά το τραύμα στο πόδι.",
        "example_en": "The doctor carefully cleaned and disinfected the wound on the leg.",
        "example2_el": "Ευτυχώς το τραύμα ήταν επιφανειακό και δεν χρειάστηκε ράμματα.",
        "example2_en": "Fortunately the injury was superficial and did not require stitches."
    },
    {
        "id": "A2-U10-020",
        "greek": "ο επίδεσμος",
        "english": "bandage / dressing",
        "notes": "Masculine noun in -ος (-οι). First aid supply.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι επίδεσμοι",
            "collocation": "ελαστικός επίδεσμος (elastic bandage)"
        },
        "keg_communicative_function": "Purchasing first aid supplies and managing sprains or cuts",
        "example_el": "Έβαλε έναν ελαστικό επίδεσμο στον αστράγαλό του επειδή έπαθε διάστρεμμα.",
        "example_en": "He placed an elastic bandage on his ankle because he suffered a sprain.",
        "example2_el": "Χρειαζόμαστε οινόπνευμα, βαμβάκι και αποστειρωμένους επιδέσμους.",
        "example2_en": "We need rubbing alcohol, cotton wool, and sterile bandages."
    },
    {
        "id": "A2-U10-021",
        "greek": "το ασθενοφόρο",
        "english": "ambulance",
        "notes": "Neuter compound noun: ασθενής (patient) + φέρω (to carry). Emergency number: 166 (ΕΚΑΒ).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ασθενοφόρα",
            "emergency_number": "166 (ΕΚΑΒ)"
        },
        "keg_communicative_function": "Calling emergency medical services in crisis scenarios",
        "example_el": "Καλέστε αμέσως ασθενοφόρο στο 166, κάποιος λιποθύμησε στον δρόμο!",
        "example_en": "Immediately call an ambulance on 166; someone fainted on the street!",
        "example2_el": "Το ασθενοφόρο έφτασε στο σημείο μέσα σε δέκα λεπτά και μετέφερε τον τραυματία.",
        "example2_en": "The ambulance reached the scene within ten minutes and transferred the injured person."
    },
    {
        "id": "A2-U10-022",
        "greek": "το νοσοκομείο",
        "english": "hospital",
        "notes": "Neuter noun in -ο (-α). Collocates with 'εφημερεύον νοσοκομείο' (hospital on call/duty).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα νοσοκομεία",
            "collocation": "εφημερεύον νοσοκομείο (on-call hospital)"
        },
        "keg_communicative_function": "Directing patients to emergency departments and on-call hospitals",
        "example_el": "Ποιο νοσοκομείο εφημερεύει απόψε στην Αθήνα για έκτακτα περιστατικά;",
        "example_en": "Which hospital is on call tonight in Athens for emergency cases?",
        "example2_el": "Τον μετέφεραν στο γενικό νοσοκομείο για περαιτέρω ιατρικές εξετάσεις.",
        "example2_en": "They transferred him to the general hospital for further medical examinations."
    },
    {
        "id": "A2-U10-023",
        "greek": "η θεραπεία",
        "english": "treatment / therapy / cure",
        "notes": "Feminine noun in -α (-ες). Relates to 'θεραπεύω' (to cure/treat).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι θεραπείες",
            "verb": "θεραπεύω"
        },
        "keg_communicative_function": "Following prescribed treatment regimens and medical guidelines",
        "example_el": "Η προτεινόμενη θεραπεία περιλαμβάνει ανάπαυση και φαρμακευτική αγωγή.",
        "example_en": "The proposed treatment includes rest and medication regimen.",
        "example2_el": "Ανταποκρίθηκε πολύ θετικά στη θεραπεία και η υγεία του βελτιώθηκε.",
        "example2_en": "He responded very positively to the treatment and his health improved."
    },
    {
        "id": "A2-U10-024",
        "greek": "η ανάρρωση",
        "english": "recovery / convalescence",
        "notes": "Feminine noun in -η (-εις). Relates to 'αναρρώνω' (to recover).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "verb": "αναρρώνω",
            "collocation": "ταχεία ανάρρωση (speedy recovery)"
        },
        "keg_communicative_function": "Wishing a speedy recovery to friends or reporting on convalescence",
        "example_el": "Σας εύχομαι ολόψυχα γρήγορη ανάρρωση και επιστροφή στις δραστηριότητές σας.",
        "example_en": "I wholeheartedly wish you a speedy recovery and return to your activities.",
        "example2_el": "Η περίοδος ανάρρωσης μετά την επέμβαση διήρκεσε δύο εβδομάδες.",
        "example2_en": "The recovery period after the surgery lasted two weeks."
    },
    {
        "id": "A2-U10-025",
        "greek": "κουράζομαι",
        "english": "to get tired / to be fatigued",
        "notes": "Mediopassive verb (κουράζομαι, κουράζεσαι, κουράζεται). Simple past: 'κουράστηκα'. Adjective: 'κουρασμένος'.",
        "gender_or_pos": "verb (mediopassive)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "κουράστηκα",
            "simple_future": "θα κουραστώ",
            "adjective": "κουρασμένος, -η, -ο"
        },
        "keg_communicative_function": "Expressing bodily exhaustion, strain, and need for rest",
        "example_el": "Κουράστηκα πάρα πολύ σήμερα στη δουλειά και χρειάζομαι επειγόντως ύπνο.",
        "example_en": "I got very tired today at work and urgently need sleep.",
        "example2_el": "Μην κουράζεστε υπερβολικά αν αισθάνεστε ακόμα αδιαθεσία.",
        "example2_en": "Do not exhaust yourself excessively if you still feel indisposed."
    },
    {
        "id": "A2-U10-026",
        "greek": "τραυματίζομαι",
        "english": "to get injured / to be wounded",
        "notes": "Mediopassive verb. Simple past: 'τραυματίστηκα'.",
        "gender_or_pos": "verb (mediopassive)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "τραυματίστηκα",
            "simple_future": "θα τραυματιστώ",
            "noun_derivative": "το τραύμα"
        },
        "keg_communicative_function": "Explaining sports injuries or workplace accidents in past narratives",
        "example_el": "Τραυματίστηκε στο γόνατο ενώ έπαιζε ποδόσφαιρο και πήγε στο νοσοκομείο.",
        "example_en": "He got injured in the knee while playing football and went to the hospital.",
        "example2_el": "Κανένας επιβάτης δεν τραυματίστηκε κατά την απότομη στάση του λεωφορείου.",
        "example2_en": "No passenger was injured during the sudden stop of the bus."
    },
    {
        "id": "A2-U10-027",
        "greek": "χτύπησα",
        "english": "I hit / I knocked / I bumped (part of body)",
        "notes": "Simple past of 'χτυπάω' (χτύπησα, χτύπησες, χτύπησε). Also used mediopassively: 'χτύπησα το χέρι μου'.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "present_stem": "χτυπάω / χτυπώ",
            "collocation": "χτύπησα το κεφάλι μου (I bumped my head)"
        },
        "keg_communicative_function": "Describing domestic mishaps, falls, and bruised limbs to examiners or triage nurses",
        "example_el": "Έπεσα από το ποδήλατο και χτύπησα τον ώμο μου.",
        "example_en": "I fell off the bicycle and hit my shoulder.",
        "example2_el": "Χτύπησε το κουδούνι του ιατρείου και μπήκε ο επόμενος ασθενής.",
        "example2_en": "The clinic doorbell rang and the next patient entered."
    },
    {
        "id": "A2-U10-028",
        "greek": "το κεφάλι",
        "english": "head",
        "notes": "Neuter noun in -ι (-ια). Plural: 'τα κεφάλια'.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κεφάλια",
            "genitive_singular": "του κεφαλιού"
        },
        "keg_communicative_function": "Pinpointing bodily areas of pain or symptoms",
        "example_el": "Γύρισε το κεφάλι του δεξιά και ένιωσε έναν οξύ πόνο στον σβέρκο.",
        "example_en": "He turned his head to the right and felt a sharp pain in his neck.",
        "example2_el": "Φορέστε καπέλο για να προστατεύσετε το κεφάλι σας από τον καυτό ήλιο.",
        "example2_en": "Wear a hat to protect your head from the hot sun."
    },
    {
        "id": "A2-U10-029",
        "greek": "ο λαιμός",
        "english": "throat / neck",
        "notes": "Masculine noun in -ός (-οί). Covers both external neck and internal throat.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι λαιμοί",
            "genitive_singular": "του λαιμού"
        },
        "keg_communicative_function": "Describing throat inflammation and ENT symptoms",
        "example_el": "Ο λαιμός μου είναι κόκκινος και πρησμένος, μάλλον έχω αμυγδαλίτιδα.",
        "example_en": "My throat is red and swollen; I probably have tonsillitis.",
        "example2_el": "Τύλιξε ένα ζεστό κασκόλ γύρω από τον λαιμό του για το κρύο.",
        "example2_en": "He wrapped a warm scarf around his neck for the cold."
    },
    {
        "id": "A2-U10-030",
        "greek": "το στομάχι",
        "english": "stomach",
        "notes": "Neuter noun in -ι (-ια). Plural: 'τα στομάχια'. Collocates with 'στομαχόπονος' (stomach ache).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα στομάχια",
            "genitive_singular": "του στομαχιού"
        },
        "keg_communicative_function": "Describing digestive issues or indigestion to medical staff",
        "example_el": "Έφαγα κάτι βαρύ χθες το βράδυ και με πειράζει το στομάχι μου.",
        "example_en": "I ate something heavy yesterday evening and my stomach is bothering me.",
        "example2_el": "Πάρτε αυτά τα χάπια με γεμάτο στομάχι για να μην έχετε ενοχλήσεις.",
        "example2_en": "Take these pills on a full stomach so that you don't have discomfort."
    },
    {
        "id": "A2-U10-031",
        "greek": "η πλάτη",
        "english": "back (anatomy)",
        "notes": "Feminine noun in -η (-ες). Collocates with 'πονάει η πλάτη μου'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πλάτες",
            "genitive_singular": "της πλάτης"
        },
        "keg_communicative_function": "Describing back strain and physical therapy needs",
        "example_el": "Σήκωσα ένα βαρύ κιβώτιο και με έπιασε δυνατός πόνος στην πλάτη.",
        "example_en": "I lifted a heavy box and was seized by severe back pain.",
        "example2_el": "Η κολύμβηση βοηθάει πολύ στην ενδυνάμωση των μυών της πλάτης.",
        "example2_en": "Swimming helps very much in strengthening the muscles of the back."
    },
    {
        "id": "A2-U10-032",
        "greek": "το πόδι",
        "english": "leg / foot",
        "notes": "Neuter noun in -ι (-ια). Covers entire lower limb or foot. 'Με τα πόδια' = on foot.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πόδια",
            "collocation": "με τα πόδια (on foot)"
        },
        "keg_communicative_function": "Describing foot/leg sprains or walking mobility issues",
        "example_el": "Γλίστρησα στις σκάλες και γύρισα το πόδι μου, δεν μπορώ να το πατήσω.",
        "example_en": "I slipped on the stairs and twisted my foot; I cannot put weight on it.",
        "example2_el": "Περπατήσαμε όλη την ημέρα και στο τέλος δεν αισθανόμασταν τα πόδια μας.",
        "example2_en": "We walked all day and at the end we couldn't feel our legs."
    },
    {
        "id": "A2-U10-033",
        "greek": "το χέρι",
        "english": "arm / hand",
        "notes": "Neuter noun in -ι (-ια). Covers hand and arm. Collocates with 'πλένω τα χέρια μου'.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα χέρια",
            "collocation": "δίνω το χέρι (to shake hands)"
        },
        "keg_communicative_function": "Describing hand/arm injuries, hygiene instructions, or gestures",
        "example_el": "Πλύνετε καλά τα χέρια σας με σαπούνι και νερό πριν από το φαγητό.",
        "example_en": "Wash your hands thoroughly with soap and water before eating.",
        "example2_el": "Έσπασε το χέρι του στο σκι και του έβαλαν γύψο για έναν μήνα.",
        "example2_en": "He broke his arm skiing and they put it in a cast for a month."
    },
    {
        "id": "A2-U10-034",
        "greek": "αρρωσταίνω",
        "english": "to get sick / to fall ill",
        "notes": "Active verb. Simple past: 'αρρώστησα'. Simple future: 'θα αρρωστήσω'. Adjective: 'άρρωστος'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "αρρώστησα",
            "simple_future": "θα αρρωστήσω",
            "adjective": "άρρωστος, -η, -ο"
        },
        "keg_communicative_function": "Stating illness onsets and explaining absences from courses or exam sessions",
        "example_el": "Αρρώστησα ξαφνικά το Σαββατοκύριακο και δεν μπόρεσα να έρθω στο μάθημα.",
        "example_en": "I fell sick suddenly over the weekend and was not able to come to class.",
        "example2_el": "Ντυθείτε ζεστά για να μην αρρωστήσετε από το κρύο.",
        "example2_en": "Dress warmly so as not to get sick from the cold."
    },
    {
        "id": "A2-U10-035",
        "greek": "η υγεία",
        "english": "health",
        "notes": "Feminine noun in -α. Core wish: 'στην υγειά σας!' (cheers / to your health) or 'γεια και υγεία'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "adjective": "υγιεινός (healthy)",
            "collocation": "στην υγειά σας! (cheers / to your health)"
        },
        "keg_communicative_function": "Proposing toasts and emphasizing wellness as life's greatest value in essays",
        "example_el": "Το πολυτιμότερο αγαθό στη ζωή του ανθρώπου είναι αναμφίβολα η υγεία.",
        "example_en": "The most valuable asset in human life is undoubtedly health.",
        "example2_el": "Σηκώσαμε τα ποτήρια μας και ευχηθήκαμε υγεία και ευημερία σε όλους.",
        "example2_en": "We raised our glasses and wished health and prosperity to everyone."
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
    
    batch5_entries = [
        {
            "id": "unit-a2-09",
            "title": "Μάθημα 9: Εργασία, Επαγγέλματα & Αγγελίες (Workplaces, CVs & Classified Ads)",
            "description": "Navigating job advertisements, employment contracts, working conditions, and interview questions using Type 1 Conditionals (αν + ενεστώτας -> μέλλοντας) and temporal connectives (μόλις, αφού, πριν).",
            "order": "KEG-A2-09-A",
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2-09/lesson-01.yaml",
                    "title": "Μάθημα 9: Εργασία, Επαγγέλματα & Αγγελίες (Workplaces, CVs & Classified Ads)"
                }
            ]
        },
        {
            "id": "unit-a2-10",
            "title": "Μάθημα 10: Υγεία, Ατυχήματα & Φαρμακείο (Health, Accidents & Medical Consultation)",
            "description": "Explaining bodily symptoms, consulting doctors and pharmacists, following medical prescriptions, and reporting emergencies using mediopassive verbs (αισθάνομαι, κουράζομαι, τραυματίζομαι) and anatomy vocabulary.",
            "order": "KEG-A2-10-A",
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2-10/lesson-01.yaml",
                    "title": "Μάθημα 10: Υγεία, Ατυχήματα & Φαρμακείο (Health, Accidents & Medical Consultation)"
                }
            ]
        }
    ]
    
    added = 0
    for entry in batch5_entries:
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
    print("--- Starting KEG-A2 Batch 5 Generation & Parallel Synthesis ---")
    
    # 1. Unit A2-09
    u9_notes = """Unit A2-09 Core Notes: Εργασία & Επαγγέλματα (Employment & CV Vocabulary)
• Employment Terminology:
  - αγγελία εργασίας (job vacancy ad), μισθός (salary), προϋπηρεσία (previous experience), προσόντα (qualifications).
  - Types of employment: πλήρης απασχόληση (full-time) vs. μερική απασχόληση (part-time).
  - Contract & Rights: σύμβαση (contract), υπερωρίες (overtime), ασφάλιση (social insurance), ένσημα (contribution stamps).

• Type 1 Conditional Sentences (Υποθετικοί λόγοι 1ου είδους - Real / Possible):
  - Structure: Αν / Εάν + Ενεστώτας -> Θα + Συνοπτικός Μέλλοντας (ή Προστακτική).
  - Example: 'Αν περάσετε τη συνέντευξη, θα υπογράψετε τη σύμβαση.'
  - Example: 'Αν έχετε απορίες, ρωτήστε τον υπεύθυνο.'

• Temporal Connectors:
  - μόλις (as soon as), αφού (after / since), πριν (before)."""

    synthesize_audio_threaded(CARDS_U09, "unit-a2-09")
    save_unit_yaml(
        unit_id="unit-a2-09",
        lesson_id="lesson-01",
        title="Μάθημα 9: Εργασία, Επαγγέλματα & Αγγελίες (Workplaces, CVs & Classified Ads)",
        description="Navigating job advertisements, employment contracts, working conditions, and interview questions using Type 1 Conditionals (αν + ενεστώτας -> μέλλοντας) and temporal connectives (μόλις, αφού, πριν).",
        lesson_notes=u9_notes,
        cards=CARDS_U09
    )

    # 2. Unit A2-10
    u10_notes = """Unit A2-10 Core Notes: Υγεία, Ατυχήματα & Φαρμακείο (Health & Medicine)
• Medical Consultation & Clinical Symptoms:
  - Verbal usage: με πονάει το... / πονάω στο... (it hurts / I ache).
  - aισθάνομαι (to feel) + adjective/adverb (αισθάνομαι άρρωστος / αδυναμία).
  - Common ailments: πυρετός (fever), πονοκέφαλος (headache), πονόλαιμος (sore throat), βήχας (cough), κρυολόγημα (cold), γρίπη (flu).

• Pharmacy & Emergency Services:
  - φαρμακείο (pharmacy), φάρμακο (medicine), συνταγή (prescription), παυσίπονο (painkiller), αντιβιοτικό (antibiotic).
  - Emergencies: ατύχημα (accident), τραύμα (wound), επίδεσμος (bandage), ασθενοφόρο (ambulance - 166).

• Human Anatomy:
  - το κεφάλι (head), ο λαιμός (throat/neck), το στομάχι (stomach), η πλάτη (back), το πόδι (leg/foot), το χέρι (arm/hand)."""

    synthesize_audio_threaded(CARDS_U10, "unit-a2-10")
    save_unit_yaml(
        unit_id="unit-a2-10",
        lesson_id="lesson-01",
        title="Μάθημα 10: Υγεία, Ατυχήματα & Φαρμακείο (Health, Accidents & Medical Consultation)",
        description="Explaining bodily symptoms, consulting doctors and pharmacists, following medical prescriptions, and reporting emergencies using mediopassive verbs (αισθάνομαι, κουράζομαι, τραυματίζομαι) and anatomy vocabulary.",
        lesson_notes=u10_notes,
        cards=CARDS_U10
    )

    # 3. Update manifest
    update_manifest()
    print("\n[OK] Batch 5 generation and parallel synthesis finished successfully!")

if __name__ == "__main__":
    main()

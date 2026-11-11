# -*- coding: utf-8 -*-
"""
Generate KEG-A2 Batch 1:
- Unit A2-01: KEG-A2-01-A (35 cards) - Personal Biography & Simple Past (Αόριστος)
- Unit A2-02: KEG-A2-02-A (35 cards) - Past Habits, Duration & Continuity (Παρατατικός vs Αόριστος)
Includes dual exam-style example sentences and Google Cloud Chirp-3 HD TTS.
"""
import sys
import os
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from server.tts_service import synthesize_greek_chirp, generate_audio_filename

AUDIO_DIR = BASE_DIR / "audio"
CONTENT_DIR = BASE_DIR / "content"

# -------------------------------------------------------------
# UNIT A2-01 CARDS (35 cards)
# Theme: Personal Biography, Life Milestones & Simple Past (Αόριστος)
# -------------------------------------------------------------
CARDS_U01 = [
    {
        "id": "A2-U01-001",
        "greek": "γεννήθηκα",
        "english": "I was born",
        "notes": "First person singular simple past of deponent/mediopassive 'γεννιέμαι'. Essential for Speaking Stage 1 & Writing Task 2.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "voice": "mediopassive",
            "second_person_singular": "γεννήθηκες",
            "third_person_singular": "γεννήθηκε",
            "first_person_plural": "γεννηθήκαμε"
        },
        "keg_communicative_function": "Stating place and date of birth in personal interviews and CVs",
        "example_el": "Γεννήθηκα στην Αθήνα το 1995 και έζησα εκεί μέχρι τα δεκαοκτώ μου χρόνια.",
        "example_en": "I was born in Athens in 1995 and lived there until I was eighteen years old.",
        "example2_el": "Πού γεννηθήκατε και πότε ήρθατε για πρώτη φορά στην Ελλάδα;",
        "example2_en": "Where were you born and when did you come to Greece for the first time?"
    },
    {
        "id": "A2-U01-002",
        "greek": "μεγάλωσα",
        "english": "I grew up",
        "notes": "Simple past of 'μεγαλώνω'. Used to describe childhood locations and family upbringing.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "μεγαλώνω",
            "third_person_singular": "μεγάλωσε",
            "first_person_plural": "μεγαλώσαμε"
        },
        "keg_communicative_function": "Describing where and how one spent childhood years",
        "example_el": "Μεγάλωσα σε ένα μικρό χωριό κοντά στη θάλασσα.",
        "example_en": "I grew up in a small village near the sea.",
        "example2_el": "Τα παιδιά μεγάλωσαν με τους παππούδες τους στην επαρχία.",
        "example2_en": "The children grew up with their grandparents in the countryside."
    },
    {
        "id": "A2-U01-003",
        "greek": "σπούδασα",
        "english": "I studied (at university / college)",
        "notes": "Simple past of 'σπουδάζω'. Distinct from 'διαβάζω' (to study a book/read). Essential for education history.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "σπουδάζω",
            "third_person_singular": "σπούδασε",
            "first_person_plural": "σπουδάσαμε"
        },
        "keg_communicative_function": "Detailing academic background and degrees in personal interviews",
        "example_el": "Σπούδασα ελληνική φιλολογία στο Πανεπιστήμιο Θεσσαλονίκης.",
        "example_en": "I studied Greek philology at the University of Thessaloniki.",
        "example2_el": "Αφού τελείωσε το σχολείο, σπούδασε πληροφορική και οικονομικά.",
        "example2_en": "After finishing school, he studied computer science and economics."
    },
    {
        "id": "A2-U01-004",
        "greek": "αποφοίτησα",
        "english": "I graduated",
        "notes": "Simple past of Type B2 verb 'αποφοιτώ' (-είς / -εί). Formal verb common in biographies and applications.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "αποφοιτώ",
            "third_person_singular": "αποφοίτησε",
            "noun_derivative": "η αποφοίτηση"
        },
        "keg_communicative_function": "Stating graduation year and academic milestones",
        "example_el": "Αποφοίτησα από το τμήμα διοίκησης επιχειρήσεων πριν από τρία χρόνια.",
        "example_en": "I graduated from the department of business administration three years ago.",
        "example2_el": "Η αδελφή μου αποφοίτησε με άριστα από την ιατρική σχολή.",
        "example2_en": "My sister graduated with honors from the medical school."
    },
    {
        "id": "A2-U01-005",
        "greek": "το πτυχίο",
        "english": "university degree / diploma",
        "notes": "Neuter noun in -ο (-α). Collocates with 'παίρνω πτυχίο' (to graduate/obtain degree).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πτυχία",
            "genitive_singular": "του πτυχίου",
            "common_collocation": "παίρνω πτυχίο"
        },
        "keg_communicative_function": "Describing qualifications and educational credentials",
        "example_el": "Πήρα το πτυχίο μου το καλοκαίρι και αμέσως άρχισα να ψάχνω δουλειά.",
        "example_en": "I received my degree in the summer and immediately started looking for a job.",
        "example2_el": "Για τη θέση αυτή είναι απαραίτητο το πτυχίο ξένης γλώσσας.",
        "example2_en": "For this position a foreign language degree is required."
    },
    {
        "id": "A2-U01-006",
        "greek": "πήρα",
        "english": "I took / I got / I received",
        "notes": "Highly irregular simple past of 'παίρνω' (πήρα, πήρες, πήρε, πήραμε, πήρατε, πήραν).",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "παίρνω",
            "second_person_singular": "πήρες",
            "third_person_singular": "πήρε",
            "first_person_plural": "πήραμε"
        },
        "keg_communicative_function": "Reporting past actions: receiving messages, obtaining credentials, taking transport",
        "example_el": "Πήρα το πρωινό λεωφορείο για να φτάσω εγκαίρως στις εξετάσεις.",
        "example_en": "I took the morning bus to arrive in time for the exams.",
        "example2_el": "Πήραμε την απόφαση να μετακομίσουμε σε μεγαλύτερο σπίτι.",
        "example2_en": "We made the decision to move to a larger house."
    },
    {
        "id": "A2-U01-007",
        "greek": "δούλεψα",
        "english": "I worked",
        "notes": "Simple past of 'δουλεύω' (-εψα stem). Standard regular aorist pattern for -εύω verbs.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "δουλεύω",
            "third_person_singular": "δούλεψε",
            "first_person_plural": "δουλέψαμε"
        },
        "keg_communicative_function": "Recounting work history and employment experience in CVs and interviews",
        "example_el": "Δούλεψα ως υπάλληλος υποδοχής σε ξενοδοχείο της Ρόδου για δύο σεζόν.",
        "example_en": "I worked as a front desk receptionist at a hotel in Rhodes for two seasons.",
        "example2_el": "Ο Νίκος δούλεψε σκληρά για να ολοκληρώσει το πρόγραμμα.",
        "example2_en": "Nikos worked hard to complete the project."
    },
    {
        "id": "A2-U01-008",
        "greek": "μετακόμισα",
        "english": "I moved / I relocated",
        "notes": "Simple past of 'μετακομίζω' (-ισα stem). Vital for discussing life changes and residential moves.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "μετακομίζω",
            "third_person_singular": "μετακόμισε",
            "noun_derivative": "η μετακόμιση"
        },
        "keg_communicative_function": "Explaining past residential changes and relocations",
        "example_el": "Πέρυσι μετακόμισα από την Πάτρα στην Αθήνα λόγω δουλειάς.",
        "example_en": "Last year I moved from Patras to Athens due to work.",
        "example2_el": "Πότε μετακομίσατε στην καινούρια σας γειτονιά;",
        "example2_en": "When did you move to your new neighborhood?"
    },
    {
        "id": "A2-U01-009",
        "greek": "η παιδική ηλικία",
        "english": "childhood",
        "notes": "Feminine noun phrase. Collocates with 'στα χρόνια της παιδικής ηλικίας' or 'από την παιδική μου ηλικία'.",
        "gender_or_pos": "noun phrase (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "head_noun": "η ηλικία",
            "adjective": "παιδική",
            "genitive": "της παιδικής ηλικίας"
        },
        "keg_communicative_function": "Discussing early life memories in oral interviews and personal essays",
        "example_el": "Πέρασα την παιδική μου ηλικία κοντά στη φύση και στα ζώα.",
        "example_en": "I spent my childhood close to nature and animals.",
        "example2_el": "Οι φιλίες της παιδικής ηλικίας κρατούν συχνά για μια ζωή.",
        "example2_en": "Childhood friendships often last for a lifetime."
    },
    {
        "id": "A2-U01-010",
        "greek": "η ανάμνηση",
        "english": "memory / recollection",
        "notes": "Feminine noun in -η (-εις). High-utility noun for reflective and narrative writing tasks.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι αναμνήσεις",
            "accusative_singular": "την ανάμνηση",
            "genitive_singular": "της ανάμνησης"
        },
        "keg_communicative_function": "Expressing nostalgia and recalling past events in narrative tasks",
        "example_el": "Έχω πολλές όμορφες αναμνήσεις από τις καλοκαιρινές διακοπές στο νησί.",
        "example_en": "I have many beautiful memories from summer vacations on the island.",
        "example2_el": "Αυτή η φωτογραφία μού φέρνει στο μυαλό μία γλυκιά ανάμνηση.",
        "example2_en": "This photograph brings a sweet memory to my mind."
    },
    {
        "id": "A2-U01-011",
        "greek": "το παρελθόν",
        "english": "the past",
        "notes": "Neuter noun in -όν (-όντος). Contrast with 'το παρόν' (present) and 'το μέλλον' (future).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "genitive_singular": "του παρελθόντος",
            "adverbial_phrase": "στο παρελθόν"
        },
        "keg_communicative_function": "Situating events chronologically and comparing past eras with today",
        "example_el": "Στο παρελθόν οι άνθρωποι επικοινωνούσαν κυρίως με γράμματα.",
        "example_en": "In the past people communicated mainly with letters.",
        "example2_el": "Δεν πρέπει να ξεχνάμε τα μαθήματα του παρελθόντος.",
        "example2_en": "We must not forget the lessons of the past."
    },
    {
        "id": "A2-U01-012",
        "greek": "η καταγωγή",
        "english": "origin / ancestry",
        "notes": "Feminine noun in -η (-ες). Essential question in KEG A2 Speaking Stage 1 ('Ποια είναι η καταγωγή σας;').",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι καταγωγές",
            "collocation": "είμαι ελληνικής καταγωγής / έχω καταγωγή από"
        },
        "keg_communicative_function": "Explaining ethnic or regional background during initial examiner questions",
        "example_el": "Έχω καταγωγή από την Κρήτη, αλλά μεγάλωσα στην Καβάλα.",
        "example_en": "I am of Cretan origin, but I grew up in Kavala.",
        "example2_el": "Ποια είναι η καταγωγή της οικογένειάς σας;",
        "example2_en": "What is the origin of your family?"
    },
    {
        "id": "A2-U01-013",
        "greek": "πήγα",
        "english": "I went",
        "notes": "Irregular simple past of 'πηγαίνω' (πήγα, πήγες, πήγε, πήγαμε, πήγατε, πήγαν). High-frequency narrative core.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "πηγαίνω",
            "second_person_singular": "πήγες",
            "third_person_singular": "πήγε",
            "first_person_plural": "πήγαμε"
        },
        "keg_communicative_function": "Describing past trips, excursions, and visits in essays and dialogues",
        "example_el": "Το προηγούμενο Σαββατοκύριακο πήγα με τους φίλους μου στο Ναύπλιο.",
        "example_en": "Last weekend I went with my friends to Nafplio.",
        "example2_el": "Πήγατε ποτέ σε αρχαιολογικό μουσείο στην Αθήνα;",
        "example2_en": "Have you ever gone to an archaeological museum in Athens?"
    },
    {
        "id": "A2-U01-014",
        "greek": "ήρθα",
        "english": "I came",
        "notes": "Irregular simple past of 'έρχομαι' (ήρθα, ήρθες, ήρθε, ήρθαμε, ήρθατε, ήρθαν).",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "έρχομαι",
            "second_person_singular": "ήρθες",
            "third_person_singular": "ήρθε",
            "first_person_plural": "ήρθαμε"
        },
        "keg_communicative_function": "Stating arrival dates and reasons for moving to Greece",
        "example_el": "Ήρθα στην Ελλάδα πριν από πέντε χρόνια για να μάθω τη γλώσσα.",
        "example_en": "I came to Greece five years ago to learn the language.",
        "example2_el": "Χθες το βράδυ ήρθαν επισκέπτες στο σπίτι μας από τη Γαλλία.",
        "example2_en": "Yesterday evening visitors came to our house from France."
    },
    {
        "id": "A2-U01-015",
        "greek": "έφυγα",
        "english": "I left / I departed",
        "notes": "Simple past of 'φεύγω' (έφυγα, έφυγες, έφυγε, φύγαμε, φύγατε, έφυγαν). Note stress shift in plural.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "φεύγω",
            "third_person_singular": "έφυγε",
            "first_person_plural": "φύγαμε"
        },
        "keg_communicative_function": "Describing departures from jobs, countries, or social events",
        "example_el": "Έφυγα από το γραφείο αργά το απόγευμα γιατί είχα πολλή δουλειά.",
        "example_en": "I left the office late in the afternoon because I had a lot of work.",
        "example2_el": "Το πλοίο έφυγε στην ώρα του από το λιμάνι του Πειραιά.",
        "example2_en": "The ship departed on time from the port of Piraeus."
    },
    {
        "id": "A2-U01-016",
        "greek": "έφτασα",
        "english": "I arrived",
        "notes": "Simple past of 'φτάνω' (έφτασα, έφτασες, έφτασε, φτάσαμε, φτάσατε, έφτασαν).",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "φτάνω",
            "third_person_singular": "έφτασε",
            "first_person_plural": "φτάσαμε"
        },
        "keg_communicative_function": "Reporting arrival times in travel scenarios and listening dialogues",
        "example_el": "Φτάσαμε στο αεροδρόμιο δύο ώρες πριν από την πτήση.",
        "example_en": "We arrived at the airport two hours before the flight.",
        "example2_el": "Το δέμα έφτασε στο ταχυδρομείο σήμερα το πρωί.",
        "example2_en": "The parcel arrived at the post office this morning."
    },
    {
        "id": "A2-U01-017",
        "greek": "είδα",
        "english": "I saw",
        "notes": "Irregular simple past of 'βλέπω' (είδα, είδες, είδε, είδαμε, είδατε, είδαν).",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "βλέπω",
            "second_person_singular": "είδες",
            "third_person_singular": "είδε",
            "first_person_plural": "είδαμε"
        },
        "keg_communicative_function": "Narrating sights, performances, and encounters in personal emails",
        "example_el": "Χθες είδα μια πολύ ενδιαφέρουσα παράσταση στο θέατρο.",
        "example_en": "Yesterday I saw a very interesting performance at the theater.",
        "example2_el": "Είδατε την ανακοίνωση για το πρόγραμμα των μαθημάτων;",
        "example2_en": "Did you see the announcement regarding the course schedule?"
    },
    {
        "id": "A2-U01-018",
        "greek": "άκουσα",
        "english": "I heard / I listened to",
        "notes": "Simple past of 'ακούω' (άκουσα, άκουσες, άκουσε, ακούσαμε, ακούσατε, άκουσαν).",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "ακούω",
            "third_person_singular": "άκουσε",
            "first_person_plural": "ακούσαμε"
        },
        "keg_communicative_function": "Reporting heard announcements, news, or advice in listening & writing tasks",
        "example_el": "Άκουσα τις ειδήσεις στο ραδιόφωνο καθώς οδηγούσα.",
        "example_en": "I heard the news on the radio as I was driving.",
        "example2_el": "Δεν άκουσα καλά τι είπε ο καθηγητής στην τάξη.",
        "example2_en": "I did not hear well what the professor said in class."
    },
    {
        "id": "A2-U01-019",
        "greek": "είπα",
        "english": "I said / I told",
        "notes": "Irregular simple past of 'λέω' (είπα, είπες, είπε, είπαμε, είπατε, είπαν).",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "λέω",
            "second_person_singular": "είπες",
            "third_person_singular": "είπε",
            "first_person_plural": "είπαμε"
        },
        "keg_communicative_function": "Reporting dialogue, opinions, and statements in past narratives",
        "example_el": "Της είπα την αλήθεια για το τι συνέβη χθες στο γραφείο.",
        "example_en": "I told her the truth about what happened yesterday at the office.",
        "example2_el": "Τι σας είπε ο υπάλληλος για την ανανέωση της κάρτας;",
        "example2_en": "What did the clerk tell you about the renewal of the card?"
    },
    {
        "id": "A2-U01-020",
        "greek": "έφαγα",
        "english": "I ate",
        "notes": "Irregular simple past of 'τρώω' (έφαγα, έφαγες, έφαγε, φάγαμε, φάγατε, έφαγαν).",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "τρώω",
            "second_person_singular": "έφαγες",
            "third_person_singular": "έφαγε",
            "first_person_plural": "φάγαμε"
        },
        "keg_communicative_function": "Describing dining experiences, meals, and social gatherings",
        "example_el": "Χθες το μεσημέρι φάγαμε παραδοσιακή χωριάτικη σαλάτα και ψάρι.",
        "example_en": "Yesterday at noon we ate traditional Greek salad and fish.",
        "example2_el": "Δεν έφαγα πρωινό επειδή βιαζόμουν να προλάβω το μετρό.",
        "example2_en": "I didn't eat breakfast because I was in a rush to catch the metro."
    },
    {
        "id": "A2-U01-021",
        "greek": "ήπια",
        "english": "I drank",
        "notes": "Irregular simple past of 'πίνω' (ήπια, ήπιες, ήπιε, ήπιαμε, ήπιατε, ήπιαν).",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "πίνω",
            "second_person_singular": "ήπιες",
            "third_person_singular": "ήπιε",
            "first_person_plural": "ήπιαμε"
        },
        "keg_communicative_function": "Recounting social cafe outings and past daily routines",
        "example_el": "Ήπιαμε έναν ελληνικό καφέ στην πλατεία και συζητήσαμε για τα νέα μας.",
        "example_en": "We drank a Greek coffee in the square and talked about our news.",
        "example2_el": "Ήπιες αρκετό νερό σήμερα μετά τη γυμναστική;",
        "example2_en": "Did you drink enough water today after exercising?"
    },
    {
        "id": "A2-U01-022",
        "greek": "βρήκα",
        "english": "I found",
        "notes": "Irregular simple past of 'βρίσκω' (βρήκα, βρήκες, βρήκε, βρήκαμε, βρήκατε, βρήκαν).",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "βρίσκω",
            "second_person_singular": "βρήκες",
            "third_person_singular": "βρήκε",
            "first_person_plural": "βρήκαμε"
        },
        "keg_communicative_function": "Reporting discovering accommodation, job vacancies, or solutions",
        "example_el": "Τελικά βρήκα ένα πολύ ωραίο διαμέρισμα κοντά στον σταθμό του μετρό.",
        "example_en": "Finally I found a very nice apartment close to the metro station.",
        "example2_el": "Βρήκατε τις πληροφορίες που ζητούσατε στην ιστοσελίδα;",
        "example2_en": "Did you find the information you were requesting on the website?"
    },
    {
        "id": "A2-U01-023",
        "greek": "έχασα",
        "english": "I lost / I missed (transportation)",
        "notes": "Simple past of 'χάνω' (έχασα, έχασες, έχασε, χάσαμε, χάσατε, έχασαν). Used for losing items or missing flights/trains.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "χάνω",
            "third_person_singular": "έχασε",
            "first_person_plural": "χάσαμε"
        },
        "keg_communicative_function": "Reporting travel disruptions or lost items in official inquiries & emails",
        "example_el": "Δυστυχώς έχασα το τρένο των οκτώ και έφτασα με καθυστέρηση.",
        "example_en": "Unfortunately I missed the eight o'clock train and arrived with a delay.",
        "example2_el": "Ο τουρίστας έχασε το διαβατήριό του και πήγε στο αστυνομικό τμήμα.",
        "example2_en": "The tourist lost his passport and went to the police station."
    },
    {
        "id": "A2-U01-024",
        "greek": "έδωσα",
        "english": "I gave / I took (an exam)",
        "notes": "Simple past of 'δίνω' (έδωσα, έδωσες, έδωσε, δώσαμε, δώσατε, έδωσαν). Crucial idiom: 'δίνω εξετάσεις' = to sit exams.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "δίνω",
            "third_person_singular": "έδωσε",
            "collocation": "δίνω εξετάσεις (to sit examinations)"
        },
        "keg_communicative_function": "Discussing exam experiences and exchange of items or money",
        "example_el": "Τον προηγούμενο Μάιο έδωσα εξετάσεις για το πιστοποιητικό επιπέδου Α1.",
        "example_en": "Last May I sat examinations for the level A1 certificate.",
        "example2_el": "Έδωσα στον υπάλληλο όλα τα απαραίτητα δικαιολογητικά.",
        "example2_en": "I gave the clerk all the necessary supporting documents."
    },
    {
        "id": "A2-U01-025",
        "greek": "έμαθα",
        "english": "I learned / I found out",
        "notes": "Irregular simple past of 'μαθαίνω' (έμαθα, έμαθες, έμαθε, μάθαμε, μάθατε, έμαθαν). Dual meaning: acquiring skills vs discovering news.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "μαθαίνω",
            "second_person_singular": "έμαθες",
            "third_person_singular": "έμαθε",
            "first_person_plural": "μάθαμε"
        },
        "keg_communicative_function": "Discussing language acquisition milestones or receiving breaking news",
        "example_el": "Έμαθα ελληνικά επειδή ζω και εργάζομαι στην Ελλάδα.",
        "example_en": "I learned Greek because I live and work in Greece.",
        "example2_el": "Μόλις χθες μάθαμε τα ευχάριστα νέα για την προαγωγή της.",
        "example2_en": "Just yesterday we learned the pleasant news about her promotion."
    },
    {
        "id": "A2-U01-026",
        "greek": "έστειλα",
        "english": "I sent",
        "notes": "Simple past of 'στέλνω' (έστειλα, έστειλες, έστειλε, στείλαμε, στείλατε, έστειλαν). Key verb for correspondence.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "στέλνω",
            "third_person_singular": "έστειλε",
            "first_person_plural": "στείλαμε"
        },
        "keg_communicative_function": "Confirming past correspondence, submission of applications, and messages",
        "example_el": "Έστειλα την αίτηση και το βιογραφικό μου στην εταιρεία μέσω email.",
        "example_en": "I sent my application and CV to the company via email.",
        "example2_el": "Σας στείλαμε την επιβεβαίωση της κράτησης στο κινητό σας.",
        "example2_en": "We sent you the reservation confirmation to your mobile phone."
    },
    {
        "id": "A2-U01-027",
        "greek": "αγόρασα",
        "english": "I bought",
        "notes": "Simple past of 'αγοράζω' (-ασα stem). Basic transaction verb.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "αγοράζω",
            "third_person_singular": "αγόρασε",
            "noun_derivative": "η αγορά"
        },
        "keg_communicative_function": "Describing past shopping, purchases, and gift acquisitions",
        "example_el": "Αγόρασα καινούρια παπούτσια για το γάμο του ξαδέλφου μου.",
        "example_en": "I bought new shoes for my cousin's wedding.",
        "example2_el": "Αγοράσαμε τα εισιτήρια του πλοίου μέσω διαδικτύου.",
        "example2_en": "We bought the ferry tickets via the internet."
    },
    {
        "id": "A2-U01-028",
        "greek": "πλήρωσα",
        "english": "I paid",
        "notes": "Simple past of 'πληρώνω' (-ωσα stem). Core commercial verb.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "πληρώνω",
            "third_person_singular": "πλήρωσε",
            "noun_derivative": "η πληρωμή"
        },
        "keg_communicative_function": "Explaining payment methods and settling bills in dialogues",
        "example_el": "Πλήρωσα τον λογαριασμό του ηλεκτρικού με πιστωτική κάρτα.",
        "example_en": "I paid the electricity bill with a credit card.",
        "example2_el": "Πόσο πληρώσατε για τη διαμονή στο ξενοδοχείο;",
        "example2_en": "How much did you pay for the stay at the hotel?"
    },
    {
        "id": "A2-U01-029",
        "greek": "άλλαξα",
        "english": "I changed / I exchanged",
        "notes": "Simple past of 'αλλάζω' (-αξα stem). Covers changing minds, changing clothes, changing residence or money.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "αλλάζω",
            "third_person_singular": "άλλαξε",
            "noun_derivative": "η αλλαγή"
        },
        "keg_communicative_function": "Explaining modifications in plans, tickets, or personal circumstances",
        "example_el": "Άλλαξα γνώμη και αποφάσισα να μείνω στο σπίτι απόψε.",
        "example_en": "I changed my mind and decided to stay home tonight.",
        "example2_el": "Στο αεροδρόμιο άλλαξα ευρώ σε δολάρια πριν από το ταξίδι.",
        "example2_en": "At the airport I changed euros into dollars before the trip."
    },
    {
        "id": "A2-U01-030",
        "greek": "γνώρισα",
        "english": "I met / I got to know",
        "notes": "Simple past of 'γνωρίζω'. Refers to meeting someone for the first time or discovering a city/culture.",
        "gender_or_pos": "verb (simple past)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "present_stem": "γνωρίζω",
            "third_person_singular": "γνώρισε",
            "noun_derivative": "η γνωριμία"
        },
        "keg_communicative_function": "Narrating interpersonal encounters and discovering new places",
        "example_el": "Στο συνέδριο γνώρισα πολλούς ενδιαφέροντες συναδέλφους από το εξωτερικό.",
        "example_en": "At the conference I met many interesting colleagues from abroad.",
        "example2_el": "Πού γνωρίσατε τον καλύτερό σας φίλο;",
        "example2_en": "Where did you meet your best friend?"
    },
    {
        "id": "A2-U01-031",
        "greek": "παντρεύτηκα",
        "english": "I got married",
        "notes": "Simple past mediopassive of 'παντρεύομαι' (παντρεύτηκα, παντρεύτηκες, παντρεύτηκε, παντρευτήκαμε). Key biographical landmark.",
        "gender_or_pos": "verb (simple past mediopassive)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple past (αόριστος)",
            "voice": "mediopassive",
            "third_person_singular": "παντρεύτηκε",
            "noun_derivative": "ο γάμος"
        },
        "keg_communicative_function": "Stating marital status milestones in biographical tasks",
        "example_el": "Παντρεύτηκα πριν από δέκα χρόνια και έχουμε αποκτήσει δύο παιδιά.",
        "example_en": "I got married ten years ago and we have had two children.",
        "example2_el": "Ο αδελφός μου παντρεύτηκε το περασμένο καλοκαίρι στη Σαντορίνη.",
        "example2_en": "My brother got married last summer in Santorini."
    },
    {
        "id": "A2-U01-032",
        "greek": "πέρυσι",
        "english": "last year",
        "notes": "Temporal adverb. Also written 'πέρσι'. Essential anchor for simple past narratives.",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "temporal adverb",
            "variant": "πέρσι",
            "contrast": "φέτος (this year), του χρόνου (next year)"
        },
        "keg_communicative_function": "Locating past events in preceding calendar year",
        "example_el": "Πέρυσι το καλοκαίρι επισκέφτηκα την Κρήτη για πρώτη φορά.",
        "example_en": "Last year in the summer I visited Crete for the first time.",
        "example2_el": "Πέρυσι δεν μπορέσαμε να ταξιδέψουμε λόγω δουλειάς.",
        "example2_en": "Last year we were not able to travel due to work."
    },
    {
        "id": "A2-U01-033",
        "greek": "πριν από",
        "english": "ago / before",
        "notes": "Prepositional temporal locution taking accusative: 'πριν από δύο μήνες' (two months ago).",
        "gender_or_pos": "prepositional phrase",
        "grammatical_info": {
            "part_of_speech": "prepositional phrase",
            "case_governed": "accusative",
            "examples": "πριν από λίγο, πριν από τρία χρόνια"
        },
        "keg_communicative_function": "Specifying elapsed time since an event occurred",
        "example_el": "Άρχισα να μαθαίνω ελληνικά πριν από δύο χρόνια.",
        "example_en": "I started learning Greek two years ago.",
        "example2_el": "Το αεροπλάνο προσγειώθηκε πριν από δέκα λεπτά.",
        "example2_en": "The airplane landed ten minutes ago."
    },
    {
        "id": "A2-U01-034",
        "greek": "προχθές",
        "english": "the day before yesterday",
        "notes": "Temporal adverb. Also written 'προχτές'. High-frequency anchor in past dialogues.",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "temporal adverb",
            "variant": "προχτές",
            "sequence": "προχθές -> χθες -> σήμερα -> αύριο -> μεθαύριο"
        },
        "keg_communicative_function": "Pinpointing events that happened two days prior",
        "example_el": "Προχθές το απόγευμα συναντήθηκα με τους παλιούς μου συμμαθητές.",
        "example_en": "The day before yesterday in the afternoon I met with my old classmates.",
        "example2_el": "Προχθές παρέλαβα το πιστοποιητικό από τη γραμματεία.",
        "example2_en": "The day before yesterday I received the certificate from the secretariat."
    },
    {
        "id": "A2-U01-035",
        "greek": "το βιογραφικό σημείωμα",
        "english": "curriculum vitae / résumé",
        "notes": "Neuter noun phrase. Frequently referred to simply as 'το βιογραφικό'. Core genre for KEG A2 vocational topics.",
        "gender_or_pos": "noun phrase (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "plural": "τα βιογραφικά σημειώματα",
            "collocation": "συντάσσω / στέλνω βιογραφικό"
        },
        "keg_communicative_function": "Referring to job applications and professional career summaries",
        "example_el": "Ετοίμασα το βιογραφικό μου σημείωμα στα ελληνικά για τη νέα θέση.",
        "example_en": "I prepared my curriculum vitae in Greek for the new position.",
        "example2_el": "Στο βιογραφικό σημείωμα αναφέρετε τις σπουδές και την προϋπηρεσία σας.",
        "example2_en": "In the curriculum vitae mention your studies and previous work experience."
    }
]

# -------------------------------------------------------------
# UNIT A2-02 CARDS (35 cards)
# Theme: Past Habits, Duration & Continuity (Παρατατικός vs Αόριστος)
# -------------------------------------------------------------
CARDS_U02 = [
    {
        "id": "A2-U02-001",
        "greek": "ήμουν",
        "english": "I was",
        "notes": "Imperfect tense of 'είμαι' (ήμουν, ήσουν, ήταν, ήμασταν, ήσασταν, ήταν). Foundation of past descriptive states.",
        "gender_or_pos": "verb (imperfect)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "imperfect (παρατατικός)",
            "second_person_singular": "ήσουν",
            "third_person_singular": "ήταν",
            "first_person_plural": "ήμασταν",
            "second_person_plural": "ήσασταν",
            "third_person_plural": "ήταν / ήσαν"
        },
        "keg_communicative_function": "Describing past states of being, childhood age, emotions, and background settings",
        "example_el": "Όταν ήμουν μικρός, περνούσα όλα τα καλοκαίρια στο σπίτι της γιαγιάς.",
        "example_en": "When I was young, I used to spend all summers at my grandmother's house.",
        "example2_el": "Χθες το απόγευμα ήμασταν όλοι πολύ κουρασμένοι από το ταξίδι.",
        "example2_en": "Yesterday afternoon we were all very tired from the trip."
    },
    {
        "id": "A2-U02-002",
        "greek": "είχα",
        "english": "I had / I used to have",
        "notes": "Imperfect tense of 'έχω' (είχα, είχες, είχε, είχαμε, είχατε, είχαν). Stative and habitual past possession.",
        "gender_or_pos": "verb (imperfect)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "imperfect (παρατατικός)",
            "second_person_singular": "είχες",
            "third_person_singular": "είχε",
            "first_person_plural": "είχαμε"
        },
        "keg_communicative_function": "Describing past possessions, circumstances, or conditions",
        "example_el": "Παλιά είχαμε ένα παλιό αυτοκίνητο που χάλαγε συνέχεια.",
        "example_en": "In the old days we had an old car that kept breaking down.",
        "example2_el": "Είχα την εντύπωση ότι το μάθημα ξεκινούσε στις εννιά.",
        "example2_en": "I had the impression that the class started at nine."
    },
    {
        "id": "A2-U02-003",
        "greek": "συνήθιζα",
        "english": "I used to / I was accustomed to",
        "notes": "Imperfect of 'συνηθίζω'. Followed by 'να + subjunctive' or a noun to express repeated past habits.",
        "gender_or_pos": "verb (imperfect)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "imperfect (παρατατικός)",
            "present_stem": "συνηθίζω",
            "third_person_singular": "συνήθιζε",
            "noun_derivative": "η συνήθεια"
        },
        "keg_communicative_function": "Stating discontinued past routines and habitual actions in speaking and writing",
        "example_el": "Συνήθιζα να ξυπνάω νωρίς και να κάνω βόλτα στην παραλία.",
        "example_en": "I used to wake up early and take a walk on the beach.",
        "example2_el": "Στο σχολείο συνήθιζε να διαβάζει τα μαθήματά του στη βιβλιοθήκη.",
        "example2_en": "At school he used to study his lessons in the library."
    },
    {
        "id": "A2-U02-004",
        "greek": "η συνήθεια",
        "english": "habit / custom",
        "notes": "Feminine noun in -α (-ες). Essential thematic concept when comparing past and modern life.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι συνήθειες",
            "accusative_singular": "τη συνήθεια",
            "genitive_singular": "της συνήθειας"
        },
        "keg_communicative_function": "Comparing old lifestyle habits with contemporary routines",
        "example_el": "Το να πίνουμε καφέ το πρωί είναι μια αγαπημένη ελληνική συνήθεια.",
        "example_en": "Drinking coffee in the morning is a favorite Greek habit.",
        "example2_el": "Με τα χρόνια άλλαξε πολλές από τις παλιές του συνήθειες.",
        "example2_en": "Over the years he changed many of his old habits."
    },
    {
        "id": "A2-U02-005",
        "greek": "ζούσα",
        "english": "I was living / I used to live",
        "notes": "Imperfect of contracted verb 'ζω / ζάω' (ζούσα, ζούσες, ζούσε, ζούσαμε, ζούσατε, ζούσαν). Denotes prolonged residence.",
        "gender_or_pos": "verb (imperfect)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "imperfect (παρατατικός)",
            "present_stem": "ζω",
            "third_person_singular": "ζούσε",
            "first_person_plural": "ζούσαμε"
        },
        "keg_communicative_function": "Narrating long-term past living conditions in biography tasks",
        "example_el": "Εκείνα τα χρόνια ζούσαμε σε ένα ήσυχο προάστιο της πόλης.",
        "example_en": "In those years we were living in a quiet suburb of the city.",
        "example2_el": "Όσο ζούσε στο εξωτερικό, του έλειπε πολύ η ελληνική κουζίνα.",
        "example2_en": "As long as he was living abroad, he missed Greek cuisine very much."
    },
    {
        "id": "A2-U02-006",
        "greek": "έμενα",
        "english": "I was staying / I used to stay",
        "notes": "Imperfect of 'μένω' (έμενα, έμενες, έμενε, μέναμε, μένατε, έμεναν). Continuous past residence.",
        "gender_or_pos": "verb (imperfect)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "imperfect (παρατατικός)",
            "present_stem": "μένω",
            "third_person_singular": "έμενε",
            "first_person_plural": "μέναμε"
        },
        "keg_communicative_function": "Describing past housing arrangements during student or early career years",
        "example_el": "Όταν ήμουν φοιτητής, έμενα σε μια μικρή γκαρσονιέρα στο κέντρο.",
        "example_en": "When I was a student, I used to live in a small studio in the center.",
        "example2_el": "Πού μένατε πριν αποφασίσετε να έρθετε στην πρωτεύουσα;",
        "example2_en": "Where were you living before you decided to come to the capital?"
    },
    {
        "id": "A2-U02-007",
        "greek": "πήγαινα",
        "english": "I was going / I used to go",
        "notes": "Imperfect of 'πηγαίνω' (πήγαινα, πήγαινες, πήγαινε, πηγαίναμε, πηγαίνατε, πήγαιναν). Repetitive or in-progress movement.",
        "gender_or_pos": "verb (imperfect)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "imperfect (παρατατικός)",
            "present_stem": "πηγαίνω",
            "third_person_singular": "πήγαινε",
            "first_person_plural": "πηγαίναμε"
        },
        "keg_communicative_function": "Describing repeated journeys or habits (e.g. walking to school, going to the beach every summer)",
        "example_el": "Κάθε καλοκαίρι πηγαίναμε με την οικογένειά μου στο χωριό των παππούδων.",
        "example_en": "Every summer we used to go with my family to our grandparents' village.",
        "example2_el": "Ενώ πήγαινα στη δουλειά με τα πόδια, συνάντησα έναν παλιό φίλο.",
        "example2_en": "While I was walking to work, I met an old friend."
    },
    {
        "id": "A2-U02-008",
        "greek": "δούλευα",
        "english": "I was working / I used to work",
        "notes": "Imperfect of 'δουλεύω' (δούλευα, δούλευες, δούλευε, δουλεύαμε, δουλεύατε, δούλευαν). Continuous employment background.",
        "gender_or_pos": "verb (imperfect)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "imperfect (παρατατικός)",
            "present_stem": "δουλεύω",
            "third_person_singular": "δούλευε",
            "first_person_plural": "δουλεύαμε"
        },
        "keg_communicative_function": "Setting the workplace background for a past narrative",
        "example_el": "Εκείνη την περίοδο δούλευα πολλές ώρες κάθε μέρα και δεν είχα ελεύθερο χρόνο.",
        "example_en": "During that period I was working many hours every day and had no free time.",
        "example2_el": "Όσο δούλευε στην τράπεζα, παρακολουθούσε παράλληλα μαθήματα γαλλικών.",
        "example2_en": "While she was working at the bank, she was simultaneously attending French classes."
    },
    {
        "id": "A2-U02-009",
        "greek": "διάβαζα",
        "english": "I was reading / I used to study",
        "notes": "Imperfect of 'διαβάζω' (διάβαζα, διάβαζες, διάβαζε, διαβάζαμε, διαβάζατε, διάβαζαν). Extended study periods.",
        "gender_or_pos": "verb (imperfect)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "imperfect (παρατατικός)",
            "present_stem": "διαβάζω",
            "third_person_singular": "διάβαζε",
            "first_person_plural": "διαβάζαμε"
        },
        "keg_communicative_function": "Describing past study habits or actions in progress when interrupted",
        "example_el": "Διάβαζα ένα βιβλίο στο σαλόνι όταν χτύπησε ξαφνικά το κουδούνι.",
        "example_en": "I was reading a book in the living room when suddenly the doorbell rang.",
        "example2_el": "Παλιά διάβαζε καθημερινά εφημερίδα, ενώ τώρα ενημερώνεται από το διαδίκτυο.",
        "example2_en": "In the past he used to read a newspaper daily, whereas now he gets informed online."
    },
    {
        "id": "A2-U02-010",
        "greek": "μιλούσα",
        "english": "I was speaking / I used to talk",
        "notes": "Imperfect of Group B1 verb 'μιλάω / μιλώ' (μιλούσα, μιλούσες, μιλούσε, μιλούσαμε, μιλούσατε, μιλούσαν).",
        "gender_or_pos": "verb (imperfect)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "imperfect (παρατατικός)",
            "present_stem": "μιλάω / μιλώ",
            "third_person_singular": "μιλούσε",
            "first_person_plural": "μιλούσαμε"
        },
        "keg_communicative_function": "Describing ongoing telephone conversations or linguistic abilities in the past",
        "example_el": "Μιλούσα στο τηλέφωνο με τη μητέρα μου όταν κόπηκε το ρεύμα.",
        "example_en": "I was speaking on the phone with my mother when the power went out.",
        "example2_el": "Όταν ήταν παιδί, μιλούσε μόνο ιταλικά στο σπίτι.",
        "example2_en": "When he was a child, he only spoke Italian at home."
    },
    {
        "id": "A2-U02-011",
        "greek": "ξυπνούσα",
        "english": "I used to wake up",
        "notes": "Imperfect of Group B1 verb 'ξυπνάω' (ξυπνούσα, ξυπνούσες, ξυπνούσε, ξυπνούσαμε, ξυπνούσατε, ξυπνούσαν).",
        "gender_or_pos": "verb (imperfect)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "imperfect (παρατατικός)",
            "present_stem": "ξυπνάω",
            "third_person_singular": "ξυπνούσε",
            "first_person_plural": "ξυπνούσαμε"
        },
        "keg_communicative_function": "Describing past morning routines and schedules",
        "example_el": "Στο χωριό ξυπνούσαμε με τον ήλιο και πηγαίναμε στα χωράφια.",
        "example_en": "In the village we used to wake up with the sun and go to the fields.",
        "example2_el": "Τον χειμώνα ξυπνούσε πάντα δύσκολα λόγω του κρύου.",
        "example2_en": "In the winter he always used to wake up with difficulty because of the cold."
    },
    {
        "id": "A2-U02-012",
        "greek": "κοιμόμουν",
        "english": "I was sleeping / I used to sleep",
        "notes": "Imperfect of mediopassive verb 'κοιμάμαι' (κοιμόμουν, κοιμόσουν, κοιμόταν, κοιμόμασταν, κοιμόσασταν, κοιμούνταν).",
        "gender_or_pos": "verb (imperfect mediopassive)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "imperfect (παρατατικός)",
            "voice": "mediopassive",
            "second_person_singular": "κοιμόσουν",
            "third_person_singular": "κοιμόταν",
            "first_person_plural": "κοιμόμασταν"
        },
        "keg_communicative_function": "Describing past sleeping habits or ongoing states during an event",
        "example_el": "Κοιμόμουν βαριά όταν με ξύπνησε ο δυνατός θόρυβος στον δρόμο.",
        "example_en": "I was sleeping heavily when the loud noise in the street woke me up.",
        "example2_el": "Τα καλοκαίρια κοιμόμασταν αργά το βράδυ λόγω της ζέστης.",
        "example2_en": "In the summers we used to sleep late at night due to the heat."
    },
    {
        "id": "A2-U02-013",
        "greek": "φορούσα",
        "english": "I was wearing / I used to wear",
        "notes": "Imperfect of Group B1 verb 'φοράω' (φορούσα, φορούσες, φορούσε, φορούσαμε, φορούσατε, φορούσαν).",
        "gender_or_pos": "verb (imperfect)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "imperfect (παρατατικός)",
            "present_stem": "φοράω",
            "third_person_singular": "φορούσε",
            "first_person_plural": "φορούσαμε"
        },
        "keg_communicative_function": "Describing past appearance, attire, and uniforms",
        "example_el": "Στο σχολείο όλοι οι μαθητές φορούσαν μπλε ποδιές εκείνα τα χρόνια.",
        "example_en": "At school all pupils used to wear blue smocks in those years.",
        "example2_el": "Όταν τον είδα, φορούσε ένα σκούρο παλτό και κρατούσε ομπρέλα.",
        "example2_en": "When I saw him, he was wearing a dark coat and holding an umbrella."
    },
    {
        "id": "A2-U02-014",
        "greek": "οδηγούσα",
        "english": "I was driving / I used to drive",
        "notes": "Imperfect of Group B2 verb 'οδηγώ' (οδηγούσα, οδηγούσες, οδηγούσε, οδηγούσαμε, οδηγούσατε, οδηγούσαν).",
        "gender_or_pos": "verb (imperfect)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "imperfect (παρατατικός)",
            "present_stem": "οδηγώ",
            "third_person_singular": "οδηγούσε",
            "noun_derivative": "ο οδηγός"
        },
        "keg_communicative_function": "Describing ongoing travel actions during incidents or road trips",
        "example_el": "Οδηγούσα προσεκτικά στον αυτοκινητόδρομο επειδή έβρεχε καταρρακτωδώς.",
        "example_en": "I was driving carefully on the highway because it was raining heavily.",
        "example2_el": "Παλιά οδηγούσε μηχανή, αλλά τώρα προτιμάει το αυτοκίνητο.",
        "example2_en": "In the past he used to ride a motorbike, but now he prefers the car."
    },
    {
        "id": "A2-U02-015",
        "greek": "έπαιζα",
        "english": "I was playing / I used to play",
        "notes": "Imperfect of 'παίζω' (έπαιζα, έπαιζες, έπαιζε, παίζαμε, παίζατε, έπαιζαν). Childhood sports and pastimes.",
        "gender_or_pos": "verb (imperfect)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "imperfect (παρατατικός)",
            "present_stem": "παίζω",
            "third_person_singular": "έπαιζε",
            "first_person_plural": "παίζαμε"
        },
        "keg_communicative_function": "Describing childhood games, hobbies, and sports",
        "example_el": "Τα απογεύματα παίζαμε ποδόσφαιρο στην αλάνα μέχρι να νυχτώσει.",
        "example_en": "In the afternoons we used to play football on the vacant lot until it got dark.",
        "example2_el": "Η Μαρία έπαιζε πιάνο για δύο ώρες κάθε μέρα.",
        "example2_en": "Maria used to play the piano for two hours every day."
    },
    {
        "id": "A2-U02-016",
        "greek": "παλιά",
        "english": "in the past / formerly / in the old days",
        "notes": "Temporal adverb. Fundamental signal word for imperfect tense contrasting with present.",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "temporal adverb",
            "comparative": "παλιότερα (formerly)",
            "contrast": "τώρα (now), σήμερα (nowadays)"
        },
        "keg_communicative_function": "Marking historical or generational contrasts in reading and writing essays",
        "example_el": "Παλιά η ζωή ήταν πιο απλή αλλά και πιο δύσκολη σωματικά.",
        "example_en": "In the old days life was simpler but also more physically demanding.",
        "example2_el": "Παλιά δεν υπήρχαν έξυπνα τηλέφωνα και διαδίκτυο.",
        "example2_en": "In the past there were no smartphones and internet."
    },
    {
        "id": "A2-U02-017",
        "greek": "τότε",
        "english": "then / at that time / back then",
        "notes": "Temporal adverb referring to a specific past period. Pairs with 'σήμερα' or 'τώρα'.",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "temporal adverb",
            "common_collocation": "από τότε (since then), μέχρι τότε (until then)"
        },
        "keg_communicative_function": "Anchoring narratives to a previously mentioned point in time",
        "example_el": "Ήμουν δεκαπέντε χρονών τότε και δεν καταλάβαινα τη σημασία του γεγονότος.",
        "example_en": "I was fifteen years old back then and did not understand the importance of the event.",
        "example2_el": "Τότε τα καταστήματα έκλειναν νωρίς το μεσημέρι.",
        "example2_en": "Back then shops used to close early in the afternoon."
    },
    {
        "id": "A2-U02-018",
        "greek": "ενώ",
        "english": "while / whereas",
        "notes": "Subordinating temporal conjunction. Takes imperfect for parallel background actions: 'ενώ έτρωγα, έβλεπα τηλεόραση'.",
        "gender_or_pos": "conjunction",
        "grammatical_info": {
            "part_of_speech": "conjunction",
            "grammatical_usage": "triggers imperfect for ongoing duration or contrast"
        },
        "keg_communicative_function": "Linking simultaneous past actions or contrasting two simultaneous situations",
        "example_el": "Ενώ μαγείρευα στην κουζίνα, τα παιδιά διάβαζαν στο δωμάτιό τους.",
        "example_en": "While I was cooking in the kitchen, the children were studying in their room.",
        "example2_el": "Ενώ περπατούσα στον πεζόδρομο, άκουσα κάποιον να φωνάζει το όνομά μου.",
        "example2_en": "While I was walking on the pedestrian street, I heard someone calling my name."
    },
    {
        "id": "A2-U02-019",
        "greek": "καθώς",
        "english": "as / while",
        "notes": "Formal temporal conjunction synonym of 'ενώ'. Frequent in narrative texts of KEG A2 Reading Section 2.",
        "gender_or_pos": "conjunction",
        "grammatical_info": {
            "part_of_speech": "conjunction",
            "synonym": "την ώρα που, ενώ"
        },
        "keg_communicative_function": "Expressing progressive synchronization between two actions",
        "example_el": "Καθώς πλησίαζε το πλοίο στο λιμάνι, όλοι οι επιβάτες βγήκαν στο κατάστρωμα.",
        "example_en": "As the ship was approaching the port, all passengers came out onto the deck.",
        "example2_el": "Καθώς κοιτούσα τις παλιές φωτογραφίες, ένιωσα μεγάλη συγκίνηση.",
        "example2_en": "As I was looking at the old photographs, I felt great emotion."
    },
    {
        "id": "A2-U02-020",
        "greek": "όταν",
        "english": "when",
        "notes": "Temporal conjunction. Pairs with imperfect for background ('όταν έμενα...') and aorist for main event.",
        "gender_or_pos": "conjunction",
        "grammatical_info": {
            "part_of_speech": "conjunction",
            "tense_combinations": "όταν + παρατατικός (duration/habit) vs όταν + αόριστος (point in time)"
        },
        "keg_communicative_function": "Setting temporal conditions and historical milestones in narratives",
        "example_el": "Όταν έφτασε ο γιατρός, ο ασθενής αισθανόταν ήδη πολύ καλύτερα.",
        "example_en": "When the doctor arrived, the patient was already feeling much better.",
        "example2_el": "Όταν τελειώσουν οι εξετάσεις, θα πάμε όλοι μαζί για φαγητό.",
        "example2_en": "When the examinations finish, we will all go eat together."
    },
    {
        "id": "A2-U02-021",
        "greek": "ξαφνικά",
        "english": "suddenly",
        "notes": "Adverb of manner/time. Characteristic signal word introducing a sudden simple past (αόριστος) into an ongoing imperfect narrative.",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "adverb",
            "narrative_role": "triggers aorist for sudden punctive interruption"
        },
        "keg_communicative_function": "Introducing sudden turns of events in written narrative tasks",
        "example_el": "Καθόμασταν ήσυχα στο μπαλκόνι όταν ξαφνικά άρχισε δυνατή καταιγίδα.",
        "example_en": "We were sitting quietly on the balcony when suddenly a strong storm began.",
        "example2_el": "Ξαφνικά συνειδητοποίησα ότι είχα ξεχάσει τα κλειδιά μου μέσα στο σπίτι.",
        "example2_en": "Suddenly I realized that I had forgotten my keys inside the house."
    },
    {
        "id": "A2-U02-022",
        "greek": "την ώρα που",
        "english": "at the moment that / while",
        "notes": "Temporal prepositional locution synonymous with 'ενώ'. Emphasizes precise coincidence of actions.",
        "gender_or_pos": "conjunctional phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "synonym": "τη στιγμή που"
        },
        "keg_communicative_function": "Pinpointing exact moments when concurrent actions intersect",
        "example_el": "Την ώρα που έμπαινα στο γραφείο, χτύπησε το τηλέφωνο.",
        "example_en": "At the moment that I was entering the office, the telephone rang.",
        "example2_el": "Έφυγε βιαστικά την ώρα που άρχιζε η ομιλία.",
        "example2_en": "He left hurriedly at the time that the speech was beginning."
    },
    {
        "id": "A2-U02-023",
        "greek": "κάθε μέρα",
        "english": "every day",
        "notes": "Adverbial temporal phrase. Distinctive trigger for imperfect (repetitive action in past) or present.",
        "gender_or_pos": "adverbial phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "aspectual_trigger": "habitual imperfect or continuous present"
        },
        "keg_communicative_function": "Describing repeated daily schedules and habitual routines",
        "example_el": "Εκείνο το καλοκαίρι πήγαινα κάθε μέρα για κολύμπι νωρίς το πρωί.",
        "example_en": "That summer I used to go swimming every day early in the morning.",
        "example2_el": "Πρέπει να εξασκείστε στα ελληνικά κάθε μέρα για να πετύχετε στις εξετάσεις.",
        "example2_en": "You must practice Greek every day to succeed in the examinations."
    },
    {
        "id": "A2-U02-024",
        "greek": "συχνά",
        "english": "often / frequently",
        "notes": "Adverb of frequency. Triggers continuous/imperfect aspect when situated in past contexts.",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "frequency adverb",
            "contrast": "σπάνια (rarely), ποτέ (never)"
        },
        "keg_communicative_function": "Expressing frequency of activities and social habits",
        "example_el": "Στο πανεπιστήμιο βγαίναμε πολύ συχνά με τους συμφοιτητές μου.",
        "example_en": "At university we used to go out very often with my fellow students.",
        "example2_el": "Πόσο συχνά επισκέπτεστε τους γονείς σας στο χωριό;",
        "example2_en": "How often do you visit your parents in the village?"
    },
    {
        "id": "A2-U02-025",
        "greek": "σπάνια",
        "english": "rarely / seldom",
        "notes": "Adverb of frequency. Antonym of 'συχνά'.",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "frequency adverb",
            "antonym": "συχνά"
        },
        "keg_communicative_function": "Describing infrequency of habits and unusual occurrences",
        "example_el": "Παλιά ταξίδευα πολύ σπάνια στο εξωτερικό λόγω υψηλού κόστους.",
        "example_en": "In the past I traveled very rarely abroad due to high costs.",
        "example2_el": "Σπάνια χάνει μάθημα, είναι πάντα συνεπής στις υποχρεώσεις του.",
        "example2_en": "He rarely misses a class; he is always punctual in his obligations."
    },
    {
        "id": "A2-U02-026",
        "greek": "σιγά σιγά",
        "english": "gradually / step by step / slowly",
        "notes": "Reduplicated adverbial locution. Denotes progressive gradual development over time.",
        "gender_or_pos": "adverbial phrase",
        "grammatical_info": {
            "part_of_speech": "idiomatic phrase",
            "synonym": "βαθμιαία, σταδιακά"
        },
        "keg_communicative_function": "Expressing gradual progress, adaptation, and linguistic improvement",
        "example_el": "Σιγά σιγά έμαθα τη γλώσσα και συνήθισα τη ζωή στην Ελλάδα.",
        "example_en": "Gradually I learned the language and got used to life in Greece.",
        "example2_el": "Ο καιρός άρχισε σιγά σιγά να ζεσταίνει καθώς ερχόταν η άνοιξη.",
        "example2_en": "The weather gradually began to warm up as spring was arriving."
    },
    {
        "id": "A2-U02-027",
        "greek": "ο τρόπος ζωής",
        "english": "lifestyle / way of life",
        "notes": "Masculine noun phrase. 'ο τρόπος' + genitive 'της ζωής'. Core sociological theme in A2 tests.",
        "gender_or_pos": "noun phrase (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "plural": "οι τρόποι ζωής",
            "genitive": "του τρόπου ζωής"
        },
        "keg_communicative_function": "Comparing urban vs rural lifestyles and modern vs traditional living",
        "example_el": "Ο σύγχρονος τρόπος ζωής στις μεγαλουπόλεις προκαλεί συχνά άγχος.",
        "example_en": "The modern lifestyle in big cities often causes stress.",
        "example2_el": "Πολλοί νέοι αναζητούν έναν πιο υγιεινό τρόπο ζωής κοντά στη φύση.",
        "example2_en": "Many young people are seeking a healthier lifestyle close to nature."
    },
    {
        "id": "A2-U02-028",
        "greek": "η καθημερινότητα",
        "english": "daily life / routine",
        "notes": "Feminine noun in -ότητα (-ότητες). High-frequency term in descriptive and comparative essays.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι καθημερινότητες",
            "accusative_singular": "την καθημερινότητα",
            "genitive_singular": "της καθημερινότητας"
        },
        "keg_communicative_function": "Describing day-to-day existence and recurring routines in Greece",
        "example_el": "Η καθημερινότητα στην Αθήνα είναι γεμάτη δραστηριότητες αλλά και κίνηση.",
        "example_en": "Daily life in Athens is full of activities but also traffic.",
        "example2_el": "Οι διακοπές μάς βοηθούν να ξεφύγουμε από τη ρουτίνα της καθημερινότητας.",
        "example2_en": "Vacations help us escape the routine of daily life."
    },
    {
        "id": "A2-U02-029",
        "greek": "η γειτονιά",
        "english": "neighborhood",
        "notes": "Feminine noun in -ά (-ές). Central cultural concept in Greek community living.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι γειτονιές",
            "accusative_singular": "τη γειτονιά",
            "genitive_singular": "της γειτονιάς"
        },
        "keg_communicative_function": "Describing local community life, neighborhood stores, and changes over time",
        "example_el": "Παλιά στη γειτονιά όλοι οι κάτοικοι γνωρίζονταν μεταξύ τους.",
        "example_en": "In the old days in the neighborhood all residents knew each other.",
        "example2_el": "Μένω σε μια ήσυχη γειτονιά με πολλά πάρκα και καταστήματα.",
        "example2_en": "I live in a quiet neighborhood with many parks and shops."
    },
    {
        "id": "A2-U02-030",
        "greek": "το χωριό",
        "english": "village / rural hometown",
        "notes": "Neuter noun in -ό (-ά). Core cultural topic in contrast with 'η πόλη' (the city).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα χωριά",
            "genitive_singular": "του χωριού"
        },
        "keg_communicative_function": "Describing holidays, traditions, and family roots in the Greek countryside",
        "example_el": "Το Πάσχα όλη η οικογένεια συγκεντρώνεται στο χωριό για να γιορτάσει.",
        "example_en": "At Easter the whole family gathers in the village to celebrate.",
        "example2_el": "Στο χωριό ο ρυθμός της ζωής ήταν πολύ πιο αργός και ήρεμος.",
        "example2_en": "In the village the pace of life was much slower and calmer."
    },
    {
        "id": "A2-U02-031",
        "greek": "οι παραδόσεις",
        "english": "traditions / customs",
        "notes": "Feminine noun plural (singular: 'η παράδοση'). Frequent subject in cultural reading passages.",
        "gender_or_pos": "noun (feminine plural)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "singular": "η παράδοση",
            "genitive_plural": "των παραδόσεων",
            "adjective": "παραδοσιακός"
        },
        "keg_communicative_function": "Discussing cultural heritage, festivities, and seasonal customs in Greece",
        "example_el": "Στην Ελλάδα διατηρούνται ακόμα πολλές παλιές παραδόσεις και έθιμα.",
        "example_en": "In Greece many old traditions and customs are still preserved.",
        "example2_el": "Είναι σημαντικό να γνωρίζουμε τις παραδόσεις του τόπου που επισκεπτόμαστε.",
        "example2_en": "It is important to know the traditions of the place we visit."
    },
    {
        "id": "A2-U02-032",
        "greek": "θυμάμαι",
        "english": "to remember / I remember",
        "notes": "Deponent/mediopassive verb in -άμαι (θυμάμαι, θυμάσαι, θυμάται, θυμόμαστε, θυμάστε, θυμούνται). Past: 'θυμήθηκα'.",
        "gender_or_pos": "verb (deponent)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "present_conjugation": "θυμάμαι, θυμάσαι, θυμάται",
            "simple_past": "θυμήθηκα",
            "antonym": "ξεχνάω"
        },
        "keg_communicative_function": "Recalling past events and expressing childhood memories",
        "example_el": "Θυμάμαι ακόμα με νοσταλγία την πρώτη μέρα που πήγα στο δημοτικό σχολείο.",
        "example_en": "I still remember with nostalgia the first day I went to primary school.",
        "example2_el": "Θυμάστε τι ώρα είχαμε κανονίσει το ραντεβού με τον δικηγόρο;",
        "example2_en": "Do you remember what time we had arranged the appointment with the lawyer?"
    },
    {
        "id": "A2-U02-033",
        "greek": "ξεχνάω",
        "english": "to forget",
        "notes": "Group B1 verb (ξεχνάω / ξεχνώ). Simple past: 'ξέχασα'. Key contrast with 'θυμάμαι'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "ξέχασα",
            "third_person_past": "ξέχασε",
            "antonym": "θυμάμαι"
        },
        "keg_communicative_function": "Expressing lapses in memory, forgetting belongings, or unforgettable moments",
        "example_el": "Δεν θα ξεχάσω ποτέ τη ζεστή φιλοξενία των ανθρώπων στο νησί.",
        "example_en": "I will never forget the warm hospitality of the people on the island.",
        "example2_el": "Συγγνώμη, ξέχασα να σας φέρω τα έγγραφα που μου ζητήσατε.",
        "example2_en": "I am sorry, I forgot to bring you the documents that you asked me for."
    },
    {
        "id": "A2-U02-034",
        "greek": "διαρκώ",
        "english": "to last / to endure",
        "notes": "Type B2 verb (διαρκεί, διαρκούν). Simple past: 'διήρκεσε' or 'διάρκεσε'. Used for duration of events, films, exams.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "third_person_present": "διαρκεί",
            "simple_past": "διήρκεσε / διάρκεσε",
            "noun_derivative": "η διάρκεια"
        },
        "keg_communicative_function": "Discussing length of time, course duration, and exam schedules",
        "example_el": "Η γραπτή εξέταση των ελληνικών διαρκεί περίπου δύο ώρες.",
        "example_en": "The written Greek examination lasts approximately two hours.",
        "example2_el": "Η καλοκαιρινή συναυλία διήρκεσε μέχρι τα μεσάνυχτα.",
        "example2_en": "The summer concert lasted until midnight."
    },
    {
        "id": "A2-U02-035",
        "greek": "η διάρκεια",
        "english": "duration / period",
        "notes": "Feminine noun in -α (-ες). Collocates with 'κατά τη διάρκεια' (during). Essential prepositional phrase.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "collocation": "κατά τη διάρκεια (+ genitive: during)",
            "genitive_singular": "της διάρκειας"
        },
        "keg_communicative_function": "Specifying time periods and describing occurrences during an event",
        "example_el": "Κατά τη διάρκεια των διακοπών επισκεφτήκαμε πολλά μουσεία και αρχαία μνημεία.",
        "example_en": "During the holidays we visited many museums and ancient monuments.",
        "example2_el": "Ποια είναι η διάρκεια του εκπαιδευτικού προγράμματος;",
        "example2_en": "What is the duration of the educational program?"
    }
]

def synthesize_and_save_unit(unit_id, lesson_id, title, description, lesson_notes, cards):
    print(f"\n==================================================")
    print(f"Processing {unit_id} ({len(cards)} cards)")
    print(f"==================================================")
    
    unit_dir = CONTENT_DIR / unit_id
    unit_dir.mkdir(parents=True, exist_ok=True)
    yaml_file = unit_dir / f"{lesson_id}.yaml"
    
    total_audio = 0
    for c in cards:
        cid = c["id"]
        grk = c["greek"]
        
        # 1. Headword audio
        h_fn = generate_audio_filename(grk)
        h_path = AUDIO_DIR / h_fn
        if not h_path.exists() or h_path.stat().st_size == 0:
            print(f"  [TTS Headword] {cid}: '{grk}' -> {h_fn} ...", end=" ", flush=True)
            b = synthesize_greek_chirp(grk)
            with open(h_path, "wb") as f_out:
                f_out.write(b)
            total_audio += 1
            print("OK")
        c["audio"] = h_fn
        c["status"] = "verified"
        
        # 2. Ex 1
        ex1 = c["example_el"]
        fn1 = generate_audio_filename(ex1)
        p1 = AUDIO_DIR / fn1
        if not p1.exists() or p1.stat().st_size == 0:
            print(f"  [TTS Ex1] {cid}: '{ex1}' -> {fn1} ...", end=" ", flush=True)
            b = synthesize_greek_chirp(ex1)
            with open(p1, "wb") as f_out:
                f_out.write(b)
            total_audio += 1
            print("OK")
        c["example_audio"] = fn1
        
        # 3. Ex 2
        ex2 = c["example2_el"]
        fn2 = generate_audio_filename(ex2)
        p2 = AUDIO_DIR / fn2
        if not p2.exists() or p2.stat().st_size == 0:
            print(f"  [TTS Ex2] {cid}: '{ex2}' -> {fn2} ...", end=" ", flush=True)
            b = synthesize_greek_chirp(ex2)
            with open(p2, "wb") as f_out:
                f_out.write(b)
            total_audio += 1
            print("OK")
        c["example2_audio"] = fn2

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
        
    print(f"\n[OK] Successfully wrote {len(cards)} cards to {yaml_file}")
    print(f"[OK] Total new audio files synthesized for {unit_id}: {total_audio}")
    return total_audio

def update_manifest():
    manifest_path = CONTENT_DIR / "manifest.yaml"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)
        
    units = manifest.get("units", [])
    existing_ids = {u["id"] for u in units}
    
    batch1_entries = [
        {
            "id": "unit-a2-01",
            "title": "Μάθημα 1: Βιογραφία, Αναμνήσεις & Το Παρελθόν μου (Personal Biography & Past Experiences)",
            "description": "Recounting life milestones, childhood memories, educational history, and past journeys using the Simple Past (Αόριστος) active voice and essential irregular stems.",
            "order": "KEG-A2-01-A",
            "total_lessons": 1
        },
        {
            "id": "unit-a2-02",
            "title": "Μάθημα 2: Καθημερινές Συνήθειες στο Παρελθόν & Χρόνος (Past Habits, Duration & Continuity)",
            "description": "Describing past routines, enduring habits, and lifestyle transformations using the Imperfect tense (Παρατατικός), temporal connectors (ενώ, καθώς, όταν), and narrative contrast with the Simple Past.",
            "order": "KEG-A2-02-A",
            "total_lessons": 1
        }
    ]
    
    added = 0
    for entry in batch1_entries:
        if entry["id"] not in existing_ids:
            units.append(entry)
            existing_ids.add(entry["id"])
            added += 1
            print(f"[Manifest] Appended {entry['id']} ({entry['order']})")
        else:
            print(f"[Manifest] {entry['id']} already exists, skipping append")
            
    manifest["units"] = units
    with open(manifest_path, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"[Manifest] Manifest saved with {len(units)} units total ({added} new).")

def main():
    print("--- Starting KEG-A2 Batch 1 Generation & Synthesis ---")
    
    # 1. Synthesize Unit A2-01
    u1_notes = """Unit A2-01 Core Notes: Βιογραφία & Αόριστος (Personal Biography & Simple Past)
• Simple Past (Αόριστος) Active Formation:
  - Regular -ω verbs form past in -σα, -ξα, -ψα (δούλεψα, άνοιξα, έγραψα).
  - Regular -άω / -ώ verbs form past in -ησα (μίλησα, ζήτησα) or -εσα / -ασα (φόρεσα, πέρασα).
  - Crucial High-Yield Irregulars: πήγα (πηγαίνω), είδα (βλέπω), είπα (λέω), ήπια (πίνω), έφαγα (τρώω), πήρα (παίρνω), βρήκα (βρίσκω), έδωσα (δίνω), έμαθα (μαθαίνω), έστειλα (στέλνω), έφυγα (φεύγω), ήρθα (έρχομαι).
  - Essential Biography Deponents: γεννήθηκα (γεννιέμαι), παντρεύτηκα (παντρεύομαι).

• Examination Relevance:
  - Writing Task 2 (Letter/Email): Recounting a past trip, describing personal background or explaining past events.
  - Speaking Stage 1: Personal interview regarding studies, career background, and origins."""

    t1 = synthesize_and_save_unit(
        unit_id="unit-a2-01",
        lesson_id="lesson-01",
        title="Μάθημα 1: Βιογραφία, Αναμνήσεις & Το Παρελθόν μου (Personal Biography & Past Experiences)",
        description="Recounting life milestones, childhood memories, educational history, and past journeys using the Simple Past (Αόριστος) active voice and essential irregular stems.",
        lesson_notes=u1_notes,
        cards=CARDS_U01
    )
    
    # 2. Synthesize Unit A2-02
    u2_notes = """Unit A2-02 Core Notes: Παρατατικός & Χρονική Σύνδεση (Imperfect & Temporal Aspect)
• Imperfect (Παρατατικός) Functions:
  - Expresses ongoing duration, past habit/repetition, or background atmosphere in narratives.
  - Forms: έμενα, διάβαζα, δούλευα, μιλούσα, ξυπνούσα, κοιμόμουν, οδηγούσα.
  - Irregular foundations: ήμουν (I was), είχα (I had).

• Aspectual Contrast: Παρατατικός vs. Αόριστος:
  - Background duration interrupted by a punctive event: 'Ενώ μαγείρευα (παρατατικός), χτύπησε (αόριστος) το κουδούνι.'
  - Habitual routine vs. single event: 'Παλιά πήγαινα (παρατατικός) κάθε μέρα, αλλά χθες δεν πήγα (αόριστος).'

• Key Connectors:
  - ενώ (while), καθώς (as/while), όταν (when), ξαφνικά (suddenly), την ώρα που (at the time that)."""

    t2 = synthesize_and_save_unit(
        unit_id="unit-a2-02",
        lesson_id="lesson-01",
        title="Μάθημα 2: Καθημερινές Συνήθειες στο Παρελθόν & Χρόνος (Past Habits, Duration & Continuity)",
        description="Describing past routines, enduring habits, and lifestyle transformations using the Imperfect tense (Παρατατικός), temporal connectors (ενώ, καθώς, όταν), and narrative contrast with the Simple Past.",
        lesson_notes=u2_notes,
        cards=CARDS_U02
    )
    
    # 3. Update manifest
    update_manifest()
    
    print(f"\n==================================================")
    print(f"Batch 1 Complete! Total audio synthesized: {t1 + t2}")
    print(f"==================================================")

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Generate KEG-A2 Batch 2:
- Unit A2-03: KEG-A2-03-A (35 cards) - Future Plans, Intentions & Predictions (Continuous & Simple Future)
- Unit A2-04: KEG-A2-04-A (35 cards) - Wishes, Obligations & Subjunctive Mood (Υποτακτική, Modality & Regulations)
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
# UNIT A2-03 CARDS (35 cards)
# Theme: Future Plans, Intentions & Predictions (Σχέδια & Μέλλοντας)
# -------------------------------------------------------------
CARDS_U03 = [
    {
        "id": "A2-U03-001",
        "greek": "θα πάω",
        "english": "I will go",
        "notes": "Simple future (συνοπτικός μέλλοντας) of 'πηγαίνω' (θα πάω, θα πας, θα πάει, θα πάμε, θα πάτε, θα πάνε). High-frequency anchor for future travel and appointments.",
        "gender_or_pos": "verb (simple future)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple future (συνοπτικός μέλλοντας)",
            "present_stem": "πηγαίνω",
            "second_person_singular": "θα πας",
            "third_person_singular": "θα πάει",
            "first_person_plural": "θα πάμε"
        },
        "keg_communicative_function": "Stating future destinations and travel intentions in speaking and writing tasks",
        "example_el": "Τον επόμενο μήνα θα πάω στην Αθήνα για επαγγελματικό σεμινάριο.",
        "example_en": "Next month I will go to Athens for a professional seminar.",
        "example2_el": "Θα πάτε στο θέατρο το Σάββατο ή προτιμάτε τον κινηματογράφο;",
        "example2_en": "Will you go to the theater on Saturday or do you prefer the cinema?"
    },
    {
        "id": "A2-U03-002",
        "greek": "θα δω",
        "english": "I will see / I will visit",
        "notes": "Simple future of 'βλέπω' (θα δω, θα δεις, θα δει, θα δούμε, θα δείτε, θα δουν). Often used for visiting friends or sights.",
        "gender_or_pos": "verb (simple future)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple future (συνοπτικός μέλλοντας)",
            "present_stem": "βλέπω",
            "second_person_singular": "θα δεις",
            "third_person_singular": "θα δει",
            "first_person_plural": "θα δούμε"
        },
        "keg_communicative_function": "Planning social visits and sightseeing in travel scenarios",
        "example_el": "Μόλις φτάσω στη Θεσσαλονίκη, θα δω τους παλιούς μου φίλους.",
        "example_en": "As soon as I arrive in Thessaloniki, I will see my old friends.",
        "example2_el": "Αύριο θα δούμε τα αποτελέσματα των εξετάσεων στον πίνακα ανακοινώσεων.",
        "example2_en": "Tomorrow we will see the examination results on the notice board."
    },
    {
        "id": "A2-U03-003",
        "greek": "θα κάνω",
        "english": "I will do / I will make",
        "notes": "Simple future of 'κάνω' (θα κάνω, θα κάνεις, θα κάνει, θα κάνουμε, θα κάνετε, θα κάνουν).",
        "gender_or_pos": "verb (simple future)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple future (συνοπτικός μέλλοντας)",
            "present_stem": "κάνω",
            "third_person_singular": "θα κάνει",
            "first_person_plural": "θα κάνουμε"
        },
        "keg_communicative_function": "Describing planned activities and future commitments",
        "example_el": "Το καλοκαίρι θα κάνουμε διακοπές σε ένα ήσυχο νησί των Κυκλάδων.",
        "example_en": "In the summer we will take holidays on a quiet Cycladic island.",
        "example2_el": "Τι θα κάνετε αν αλλάξει το πρόγραμμα των δρομολογίων;",
        "example2_en": "What will you do if the route schedule changes?"
    },
    {
        "id": "A2-U03-004",
        "greek": "θα μείνω",
        "english": "I will stay",
        "notes": "Simple future of 'μένω' (θα μείνω, θα μείνεις, θα μείνει, θα μείνουμε, θα μείνετε, θα μείνουν). Core verb for hotel reservations.",
        "gender_or_pos": "verb (simple future)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple future (συνοπτικός μέλλοντας)",
            "present_stem": "μένω",
            "third_person_singular": "θα μείνει",
            "first_person_plural": "θα μείνουμε"
        },
        "keg_communicative_function": "Specifying future lodging and duration of stay in booking inquiries",
        "example_el": "Θα μείνω σε ένα ξενοδοχείο στο κέντρο της πόλης για τρεις διανυκτερεύσεις.",
        "example_en": "I will stay at a hotel in the city center for three nights.",
        "example2_el": "Πόσες μέρες θα μείνετε στην Κρήτη;",
        "example2_en": "How many days will you stay in Crete?"
    },
    {
        "id": "A2-U03-005",
        "greek": "θα ταξιδέψω",
        "english": "I will travel",
        "notes": "Simple future of 'ταξιδεύω' (-εψω stem: θα ταξιδέψω, θα ταξιδέψεις, θα ταξιδέψει).",
        "gender_or_pos": "verb (simple future)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple future (συνοπτικός μέλλοντας)",
            "present_stem": "ταξιδεύω",
            "third_person_singular": "θα ταξιδέψει",
            "noun_derivative": "το ταξίδι"
        },
        "keg_communicative_function": "Discussing upcoming travel arrangements and itineraries",
        "example_el": "Τον επόμενο χειμώνα θα ταξιδέψω στην Ιταλία με το τρένο.",
        "example_en": "Next winter I will travel to Italy by train.",
        "example2_el": "Θα ταξιδέψετε αεροπορικώς ή με το πλοίο;",
        "example2_en": "Will you travel by plane or by ship?"
    },
    {
        "id": "A2-U03-006",
        "greek": "θα δουλεύω",
        "english": "I will be working",
        "notes": "Continuous future (εξακολουθητικός μέλλοντας) of 'δουλεύω'. Denotes continuous action or routine in future.",
        "gender_or_pos": "verb (continuous future)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "continuous future (εξακολουθητικός μέλλοντας)",
            "aspect": "continuous/imperfective",
            "third_person_singular": "θα δουλεύει",
            "first_person_plural": "θα δουλεύουμε"
        },
        "keg_communicative_function": "Describing continuous future occupation or background activities",
        "example_el": "Όλο το πρωί του Σαββάτου θα δουλεύω στο γραφείο, οπότε δεν θα μπορώ να έρθω.",
        "example_en": "All Saturday morning I will be working at the office, so I will not be able to come.",
        "example2_el": "Του χρόνου θα δουλεύει ως καθηγητής σε ιδιωτικό σχολείο.",
        "example2_en": "Next year he will be working as a teacher at a private school."
    },
    {
        "id": "A2-U03-007",
        "greek": "θα διαβάζω",
        "english": "I will be studying / I will be reading",
        "notes": "Continuous future of 'διαβάζω'. Indicates prolonged study or preparation.",
        "gender_or_pos": "verb (continuous future)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "continuous future (εξακολουθητικός μέλλοντας)",
            "aspect": "continuous/imperfective",
            "third_person_singular": "θα διαβάζει",
            "contrast": "θα διαβάσω (punctual / single completion)"
        },
        "keg_communicative_function": "Describing ongoing preparation for examinations in student interviews",
        "example_el": "Τις επόμενες εβδομάδες θα διαβάζω καθημερινά για τις εξετάσεις του Μαΐου.",
        "example_en": "In the coming weeks I will be studying daily for the May exams.",
        "example2_el": "Μην κάνετε θόρυβο, τα παιδιά θα διαβάζουν για το σχολείο.",
        "example2_en": "Do not make noise, the children will be studying for school."
    },
    {
        "id": "A2-U03-008",
        "greek": "θα πάρω",
        "english": "I will take / I will receive",
        "notes": "Simple future of 'παίρνω' (θα πάρω, θα πάρεις, θα πάρει, θα πάρουμε, θα πάρετε, θα πάρουν).",
        "gender_or_pos": "verb (simple future)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple future (συνοπτικός μέλλοντας)",
            "present_stem": "παίρνω",
            "second_person_singular": "θα πάρεις",
            "third_person_singular": "θα πάρει",
            "first_person_plural": "θα πάρουμε"
        },
        "keg_communicative_function": "Planning transport decisions or taking official exams/degrees",
        "example_el": "Αύριο το πρωί θα πάρω το μετρό για να αποφύγω την κίνηση.",
        "example_en": "Tomorrow morning I will take the metro to avoid traffic.",
        "example2_el": "Σε δύο χρόνια ελπίζει ότι θα πάρει το πτυχίο του.",
        "example2_en": "In two years he hopes that he will receive his degree."
    },
    {
        "id": "A2-U03-009",
        "greek": "θα δώσω",
        "english": "I will give / I will sit (an exam)",
        "notes": "Simple future of 'δίνω' (θα δώσω, θα δώσεις, θα δώσει, θα δώσουμε, θα δώσετε, θα δώσουν). High-frequency idiom: 'θα δώσω εξετάσεις'.",
        "gender_or_pos": "verb (simple future)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple future (συνοπτικός μέλλοντας)",
            "present_stem": "δίνω",
            "third_person_singular": "θα δώσει",
            "collocation": "θα δώσω εξετάσεις (I will sit exams)"
        },
        "keg_communicative_function": "Declaring intent to sit exams and deliver items",
        "example_el": "Τον Μάιο θα δώσω εξετάσεις για το πιστοποιητικό ελληνομάθειας Α2.",
        "example_en": "In May I will sit examinations for the A2 certificate of attainment in Greek.",
        "example2_el": "Θα σας δώσω όλες τις πληροφορίες μόλις λάβω το μήνυμα.",
        "example2_en": "I will give you all the information as soon as I receive the message."
    },
    {
        "id": "A2-U03-010",
        "greek": "θα έρθω",
        "english": "I will come",
        "notes": "Simple future of 'έρχομαι' (θα έρθω, θα έρθεις, θα έρθει, θα έρθουμε, θα έρθετε, θα έρθουν). Key verb for accepting invitations.",
        "gender_or_pos": "verb (simple future)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple future (συνοπτικός μέλλοντας)",
            "present_stem": "έρχομαι",
            "second_person_singular": "θα έρθεις",
            "third_person_singular": "θα έρθει",
            "first_person_plural": "θα έρθουμε"
        },
        "keg_communicative_function": "Accepting invitations and confirming arrival times in Writing Task 1",
        "example_el": "Ευχαριστώ για την πρόσκληση! Θα έρθω στο πάρτι σας μετά τις οκτώ.",
        "example_en": "Thank you for the invitation! I will come to your party after eight.",
        "example2_el": "Θα έρθετε μαζί μας στην εκδρομή την Κυριακή;",
        "example2_en": "Will you come with us on the excursion on Sunday?"
    },
    {
        "id": "A2-U03-011",
        "greek": "θα φύγω",
        "english": "I will leave / I will depart",
        "notes": "Simple future of 'φεύγω' (θα φύγω, θα φύγεις, θα φύγει, θα φύγουμε, θα φύγετε, θα φύγουν).",
        "gender_or_pos": "verb (simple future)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple future (συνοπτικός μέλλοντας)",
            "present_stem": "φεύγω",
            "third_person_singular": "θα φύγει",
            "first_person_plural": "θα φύγουμε"
        },
        "keg_communicative_function": "Stating departure times in travel bookings and formal inquiries",
        "example_el": "Θα φύγω από το σπίτι νωρίς για να μη χάσω το λεωφορείο.",
        "example_en": "I will leave the house early so as not to miss the bus.",
        "example2_el": "Το αεροπλάνο θα φύγει με μικρή καθυστέρηση λόγω καιρού.",
        "example2_en": "The airplane will depart with a slight delay due to weather."
    },
    {
        "id": "A2-U03-012",
        "greek": "θα βρω",
        "english": "I will find",
        "notes": "Simple future of 'βρίσκω' (θα βρω, θα βρεις, θα βρει, θα βρούμε, θα βρείτε, θα βρουν).",
        "gender_or_pos": "verb (simple future)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple future (συνοπτικός μέλλοντας)",
            "present_stem": "βρίσκω",
            "second_person_singular": "θα βρεις",
            "third_person_singular": "θα βρει",
            "first_person_plural": "θα βρούμε"
        },
        "keg_communicative_function": "Expressing optimism about finding employment, lodging, or solutions",
        "example_el": "Είμαι σίγουρος ότι θα βρω μια καλή δουλειά στην Ελλάδα.",
        "example_en": "I am certain that I will find a good job in Greece.",
        "example2_el": "Πού θα βρούμε φθηνά εισιτήρια για το ταξίδι;",
        "example2_en": "Where will we find cheap tickets for the trip?"
    },
    {
        "id": "A2-U03-013",
        "greek": "θα στείλω",
        "english": "I will send",
        "notes": "Simple future of 'στέλνω' (θα στείλω, θα στείλεις, θα στείλει, θα στείλουμε, θα στείλετε, θα στείλουν).",
        "gender_or_pos": "verb (simple future)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "tense": "simple future (συνοπτικός μέλλοντας)",
            "present_stem": "στέλνω",
            "third_person_singular": "θα στείλει",
            "first_person_plural": "θα στείλουμε"
        },
        "keg_communicative_function": "Promising to send emails, documents, or postcards in correspondence",
        "example_el": "Αύριο θα σας στείλω όλα τα απαραίτητα δικαιολογητικά με μήνυμα.",
        "example_en": "Tomorrow I will send you all the necessary documents by email.",
        "example2_el": "Θα στείλουμε κάρτες στους φίλους μας από τις διακοπές.",
        "example2_en": "We will send cards to our friends from the vacation."
    },
    {
        "id": "A2-U03-014",
        "greek": "σκοπεύω",
        "english": "I intend to / I plan to",
        "notes": "Active verb followed by 'να + subjunctive'. Direct indicator of intent in candidate interviews.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "syntax": "σκοπεύω να + υποτακτική",
            "third_person_singular": "σκοπεύει",
            "noun_derivative": "ο σκοπός"
        },
        "keg_communicative_function": "Articulating future career and personal intentions in oral interviews",
        "example_el": "Σκοπεύω να ανοίξω τη δική μου επιχείρηση τα επόμενα χρόνια.",
        "example_en": "I intend to open my own business in the coming years.",
        "example2_el": "Τι σκοπεύετε να κάνετε μετά την ολοκλήρωση του προγράμματος;",
        "example2_en": "What do you intend to do after the completion of the program?"
    },
    {
        "id": "A2-U03-015",
        "greek": "σχεδιάζω",
        "english": "to plan / to design",
        "notes": "Verb taking direct object or 'να + subjunctive'. Related to 'το σχέδιο' (plan/design).",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_future": "θα σχεδιάσω",
            "third_person_singular": "σχεδιάζει",
            "noun_derivative": "το σχέδιο"
        },
        "keg_communicative_function": "Discussing planning of trips, events, or projects",
        "example_el": "Σχεδιάζουμε ένα ταξίδι στη βόρεια Ελλάδα για την άνοιξη.",
        "example_en": "We are planning a trip to northern Greece for the spring.",
        "example2_el": "Η επιτροπή σχεδιάζει νέες εκδηλώσεις για το κοινό.",
        "example2_en": "The committee is planning new events for the public."
    },
    {
        "id": "A2-U03-016",
        "greek": "το σχέδιο",
        "english": "plan / design / blueprint",
        "notes": "Neuter noun in -ο (-α). Plural 'τα σχέδια' means plans / future intentions.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα σχέδια",
            "genitive_singular": "του σχεδίου",
            "collocation": "κάνω σχέδια (to make plans)"
        },
        "keg_communicative_function": "Discussing plans for the holidays or career in personal dialogues",
        "example_el": "Ποια είναι τα σχέδιά σας για το επόμενο καλοκαίρι;",
        "example_en": "What are your plans for next summer?",
        "example2_el": "Έχουμε πολλά σχέδια για τη βελτίωση του χώρου εργασίας.",
        "example2_en": "We have many plans for the improvement of the workplace."
    },
    {
        "id": "A2-U03-017",
        "greek": "ελπίζω",
        "english": "to hope / I hope",
        "notes": "Verb usually followed by 'να + subjunctive' or 'ότι + future'. Expresses optimistic anticipation.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "syntax": "ελπίζω να + υποτακτική / ελπίζω ότι + οριστική",
            "noun_derivative": "η ελπίδα"
        },
        "keg_communicative_function": "Expressing hopes and good wishes in informal emails and interviews",
        "example_el": "Ελπίζω να περάσω με επιτυχία τις εξετάσεις του Μαΐου.",
        "example_en": "I hope to successfully pass the May examinations.",
        "example2_el": "Ελπίζουμε ότι ο καιρός θα είναι καλός το Σαββατοκύριακο.",
        "example2_en": "We hope that the weather will be good over the weekend."
    },
    {
        "id": "A2-U03-018",
        "greek": "το όνειρο",
        "english": "dream",
        "notes": "Neuter noun in -ο (-α). Refers both to sleep dreams and life aspirations.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα όνειρα",
            "genitive_singular": "του ονείρου",
            "collocation": "το όνειρό μου είναι να..."
        },
        "keg_communicative_function": "Describing life aspirations and ideal future goals in oral Stage 1",
        "example_el": "Το όνειρό μου είναι να ζήσω και να εργαστώ μόνιμα σε ένα ελληνικό νησί.",
        "example_en": "My dream is to live and work permanently on a Greek island.",
        "example2_el": "Ποτέ μην εγκαταλείπετε τα όνειρά σας για το μέλλον.",
        "example2_en": "Never abandon your dreams for the future."
    },
    {
        "id": "A2-U03-019",
        "greek": "το μέλλον",
        "english": "the future",
        "notes": "Neuter noun in -ον (-οντος). Temporal anchor: 'στο μέλλον' (in the future).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "genitive_singular": "του μέλλοντος",
            "adverbial_phrase": "στο μέλλον (in the future)"
        },
        "keg_communicative_function": "Speculating about future prospects and career trajectories",
        "example_el": "Στο μέλλον οι περισσότερες συναλλαγές θα γίνονται ψηφιακά.",
        "example_en": "In the future most transactions will be conducted digitally.",
        "example2_el": "Εύχομαι κάθε επιτυχία στο επαγγελματικό σας μέλλον.",
        "example2_en": "I wish every success in your professional future."
    },
    {
        "id": "A2-U03-020",
        "greek": "του χρόνου",
        "english": "next year",
        "notes": "Fixed genitive temporal phrase used adverbially. Antonym: 'πέρυσι' (last year).",
        "gender_or_pos": "adverbial phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "grammatical_origin": "genitive of time",
            "contrast": "πέρυσι (last year), φέτος (this year)"
        },
        "keg_communicative_function": "Setting future calendar milestones in personal plans",
        "example_el": "Του χρόνου θα ξεκινήσω μαθήματα επιπέδου Β1.",
        "example_en": "Next year I will start level B1 courses.",
        "example2_el": "Σκοπεύουν να αγοράσουν δικό τους σπίτι του χρόνου.",
        "example2_en": "They plan to buy their own house next year."
    },
    {
        "id": "A2-U03-021",
        "greek": "τον επόμενο μήνα",
        "english": "next month",
        "notes": "Temporal accusative phrase. Collocates with simple or continuous future.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "case": "accusative of time",
            "related": "την επόμενη εβδομάδα (next week)"
        },
        "keg_communicative_function": "Scheduling medium-term appointments and travel in correspondence",
        "example_el": "Τον επόμενο μήνα θα διεξαχθούν οι ετήσιες εξετάσεις πιστοποίησης.",
        "example_en": "Next month the annual certification exams will be held.",
        "example2_el": "Θα λάβετε την τελική απάντηση τον επόμενο μήνα.",
        "example2_en": "You will receive the final answer next month."
    },
    {
        "id": "A2-U03-022",
        "greek": "σύντομα",
        "english": "soon / shortly",
        "notes": "Adverb of time. Standard closing element in Greek letters: 'θα τα πούμε σύντομα'.",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "adverb",
            "synonym": "σε λίγο, γρήγορα",
            "collocation": "θα τα πούμε σύντομα (see you soon)"
        },
        "keg_communicative_function": "Concluding communicative letters/emails with anticipation of prompt reunion",
        "example_el": "Ελπίζω να έχω νέα σας πολύ σύντομα.",
        "example_en": "I hope to have news from you very soon.",
        "example2_el": "Το καινούριο κατάστημα θα ανοίξει σύντομα στο εμπορικό κέντρο.",
        "example2_en": "The new store will open soon in the shopping mall."
    },
    {
        "id": "A2-U03-023",
        "greek": "σε λίγο",
        "english": "in a little while / shortly",
        "notes": "Temporal prepositional phrase indicating imminent immediate future.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "synonym": "σε λίγα λεπτά"
        },
        "keg_communicative_function": "Announcing imminent departures or arrivals in listening exercises",
        "example_el": "Σε λίγο θα αρχίσει η προβολή της ταινίας, παρακαλώ κλείστε τα κινητά σας.",
        "example_en": "In a little while the film screening will begin; please turn off your mobile phones.",
        "example2_el": "Ο εκφωνητής ανακοίνωσε ότι το τρένο θα φτάσει σε λίγο.",
        "example2_en": "The announcer stated that the train will arrive shortly."
    },
    {
        "id": "A2-U03-024",
        "greek": "μεθαύριο",
        "english": "the day after tomorrow",
        "notes": "Temporal adverb. Forms sequence: χθες -> σήμερα -> αύριο -> μεθαύριο.",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "temporal adverb",
            "sequence": "σήμερα -> αύριο -> μεθαύριο"
        },
        "keg_communicative_function": "Scheduling short-term appointments and meetings in dialogues",
        "example_el": "Μεθαύριο το πρωί έχω ραντεβού με τον γιατρό για εξετάσεις.",
        "example_en": "The day after tomorrow in the morning I have an appointment with the doctor for tests.",
        "example2_el": "Τα μαθήματα θα επαναληφθούν μεθαύριο.",
        "example2_en": "Classes will resume the day after tomorrow."
    },
    {
        "id": "A2-U03-025",
        "greek": "σίγουρα",
        "english": "certainly / definitely",
        "notes": "Adverb of degree/certainty. Expresses high confidence in future predictions.",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "adverb",
            "adjective": "σίγουρος, -η, -ο",
            "synonym": "οπωσδήποτε"
        },
        "keg_communicative_function": "Expressing firm conviction or reassurance in conversations",
        "example_el": "Θα έρθω σίγουρα στη γιορτή σας αν δεν δουλεύω.",
        "example_en": "I will definitely come to your celebration if I am not working.",
        "example2_el": "Με καλή προετοιμασία θα πετύχετε σίγουρα τον στόχο σας.",
        "example2_en": "With good preparation you will definitely achieve your goal."
    },
    {
        "id": "A2-U03-026",
        "greek": "ίσως",
        "english": "perhaps / maybe",
        "notes": "Modal adverb followed by subjunctive or future indicative to express possibility.",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "modal adverb",
            "synonym": "μπορεί να, πιθανόν",
            "syntax": "ίσως + οριστική μέλλοντα ή ίσως + υποτακτική"
        },
        "keg_communicative_function": "Expressing uncertainty or tentative proposals in oral Stage 3",
        "example_el": "Ίσως ταξιδέψουμε στα Χανιά το τριήμερο, αν βρούμε οικονομικά εισιτήρια.",
        "example_en": "Perhaps we will travel to Chania for the three-day weekend if we find budget tickets.",
        "example2_el": "Ίσως χρειαστεί να περιμένετε λίγα λεπτά στη γραμματεία.",
        "example2_en": "Perhaps you will need to wait a few minutes at the secretariat."
    },
    {
        "id": "A2-U03-027",
        "greek": "πιθανόν",
        "english": "probably / likely",
        "notes": "Modal adverb / neuter adjective functioning adverbially. Indicates high probability.",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "modal adverb",
            "variant": "πιθανώς",
            "phrase": "είναι πιθανό να (it is likely that)"
        },
        "keg_communicative_function": "Estimating likelihood and making cautious predictions",
        "example_el": "Πιθανόν να βρέξει το απόγευμα, γι' αυτό πάρτε ομπρέλα μαζί σας.",
        "example_en": "It will probably rain in the afternoon, so take an umbrella with you.",
        "example2_el": "Είναι πολύ πιθανό να αλλάξει η ημερομηνία της συνάντησης.",
        "example2_en": "It is very likely that the meeting date will change."
    },
    {
        "id": "A2-U03-028",
        "greek": "αποκλείεται",
        "english": "it's impossible / out of the question",
        "notes": "Impersonal mediopassive verb. Followed by 'να + subjunctive'. Expresses absolute denial/impossibility.",
        "gender_or_pos": "verb (impersonal)",
        "grammatical_info": {
            "part_of_speech": "impersonal verb",
            "syntax": "αποκλείεται να + υποτακτική",
            "antonym": "είναι σίγουρο"
        },
        "keg_communicative_function": "Rejecting options emphatically or dismissing unlikely possibilities",
        "example_el": "Αποκλείεται να προλάβουμε το τρένο αν δεν πάρουμε ταξί.",
        "example_en": "It's out of the question that we catch the train unless we take a taxi.",
        "example2_el": "Αποκλείεται να κάνει τόση ζέστη τον Μάιο.",
        "example2_en": "It's impossible for it to be that hot in May."
    },
    {
        "id": "A2-U03-029",
        "greek": "αποφασίζω",
        "english": "to decide",
        "notes": "Verb followed by 'να + subjunctive'. Simple past: 'αποφάσισα', simple future: 'θα αποφασίσω'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "αποφάσισα",
            "simple_future": "θα αποφασίσω",
            "noun_derivative": "η απόφαση"
        },
        "keg_communicative_function": "Reporting decisions taken or deliberating options in candidate discussions",
        "example_el": "Αποφάσισα να γραφτώ σε εντατικό τμήμα εκμάθησης ελληνικών.",
        "example_en": "I decided to enroll in an intensive Greek learning course.",
        "example2_el": "Πότε θα αποφασίσετε ποιο αυτοκίνητο θα αγοράσετε;",
        "example2_en": "When will you decide which car you will buy?"
    },
    {
        "id": "A2-U03-030",
        "greek": "η απόφαση",
        "english": "decision",
        "notes": "Feminine noun in -η (-εις). Collocates with 'παίρνω απόφαση' (to make a decision).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι αποφάσεις",
            "accusative_singular": "την απόφαση",
            "collocation": "παίρνω απόφαση"
        },
        "keg_communicative_function": "Discussing life decisions, career steps, and joint conclusions in Stage 3",
        "example_el": "Ήταν μια δύσκολη αλλά απαραίτητη απόφαση για το μέλλον της οικογένειας.",
        "example_en": "It was a difficult but necessary decision for the family's future.",
        "example2_el": "Πήραμε την οριστική απόφαση να μετακομίσουμε στην εξοχή.",
        "example2_en": "We made the definitive decision to move to the countryside."
    },
    {
        "id": "A2-U03-031",
        "greek": "κανονίζω",
        "english": "to arrange / to organize / to settle",
        "notes": "Common conversational verb in Greek life: 'θα το κανονίσω' (I will arrange it). Simple past: 'κανόνισα'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "κανόνισα",
            "simple_future": "θα κανονίσω",
            "collocation": "κανονίζω ραντεβού / συνάντηση"
        },
        "keg_communicative_function": "Arranging social meetings, outings, and schedules with friends",
        "example_el": "Κανονίσαμε να συναντηθούμε έξω από τον σταθμό του μετρό στις επτά.",
        "example_en": "We arranged to meet outside the metro station at seven.",
        "example2_el": "Θα κανονίσω εγώ τα εισιτήρια για όλους μας.",
        "example2_en": "I will arrange the tickets for all of us."
    },
    {
        "id": "A2-U03-032",
        "greek": "ο στόχος",
        "english": "goal / objective / target",
        "notes": "Masculine noun in -ος (-οι). Collocates with 'πετυχαίνω τον στόχο' (to achieve the goal).",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι στόχοι",
            "genitive_singular": "του στόχου",
            "collocation": "βάζω στόχο, πετυχαίνω τον στόχο"
        },
        "keg_communicative_function": "Setting personal and educational objectives in oral interviews",
        "example_el": "Ο βασικός μου στόχος είναι να μιλάω άπταιστα ελληνικά μέχρι το τέλος της χρονιάς.",
        "example_en": "My primary goal is to speak fluent Greek by the end of the year.",
        "example2_el": "Έθεσε υψηλούς στόχους για την επαγγελματική του πορεία.",
        "example2_en": "He set high goals for his professional career."
    },
    {
        "id": "A2-U03-033",
        "greek": "η πρόβλεψη",
        "english": "forecast / prediction",
        "notes": "Feminine noun in -η (-εις). Frequently used for weather forecasts ('η πρόβλεψη του καιρού').",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι προβλέψεις",
            "genitive_singular": "της πρόβλεψης",
            "collocation": "πρόβλεψη καιρού (weather forecast)"
        },
        "keg_communicative_function": "Interpreting weather bulletins and listening forecasts in Section 1",
        "example_el": "Σύμφωνα με την πρόβλεψη της μετεωρολογικής υπηρεσίας, αύριο θα έχουμε ηλιοφάνεια.",
        "example_en": "According to the meteorological service forecast, tomorrow we will have sunshine.",
        "example2_el": "Οι οικονομικές προβλέψεις για το επόμενο έτος είναι ενθαρρυντικές.",
        "example2_en": "The economic forecasts for next year are encouraging."
    },
    {
        "id": "A2-U03-034",
        "greek": "υπόσχομαι",
        "english": "to promise / I promise",
        "notes": "Deponent verb (υπόσχομαι, υπόσχεσαι, υπόσχεται). Simple past: 'υποσχέθηκα'. Simple future: 'θα υποσχεθώ'.",
        "gender_or_pos": "verb (deponent)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "υποσχέθηκα",
            "simple_future": "θα υποσχεθώ",
            "noun_derivative": "η υπόσχεση"
        },
        "keg_communicative_function": "Making commitments and reassuring interlocutors in communicative tasks",
        "example_el": "Σου υπόσχομαι ότι θα κάνω ό,τι καλύτερο μπορώ στις εξετάσεις.",
        "example_en": "I promise you that I will do my absolute best in the exams.",
        "example2_el": "Υποσχέθηκε να τηλεφωνήσει μόλις φτάσει στον προορισμό του.",
        "example2_en": "He promised to call as soon as he arrives at his destination."
    },
    {
        "id": "A2-U03-035",
        "greek": "η υπόσχεση",
        "english": "promise",
        "notes": "Feminine noun in -η (-εις). Collocates with 'κρατάω / τηρώ την υπόσχεση' (to keep a promise).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι υποσχέσεις",
            "accusative_singular": "την υπόσχεση",
            "collocation": "δίνω υπόσχεση, κρατάω την υπόσχεση"
        },
        "keg_communicative_function": "Holding interlocutors to their word in role-plays and letter exchanges",
        "example_el": "Είναι σημαντικό να κρατάμε πάντα τις υποσχέσεις που δίνουμε.",
        "example_en": "It is important to always keep the promises we make.",
        "example2_el": "Μου έδωσε την υπόσχεση ότι θα με επισκεφτεί το καλοκαίρι.",
        "example2_en": "He gave me the promise that he will visit me in the summer."
    }
]

# -------------------------------------------------------------
# UNIT A2-04 CARDS (35 cards)
# Theme: Wishes, Obligations & Subjunctive Mood (Επιθυμίες, Ανάγκες & Υποτακτική)
# -------------------------------------------------------------
CARDS_U04 = [
    {
        "id": "A2-U04-001",
        "greek": "πρέπει να",
        "english": "must / ought to / have to",
        "notes": "Impersonal modal phrase taking subjunctive. Fundamental for rules, obligations, and instructions across all exam papers.",
        "gender_or_pos": "modal phrase (impersonal)",
        "grammatical_info": {
            "part_of_speech": "modal phrase",
            "syntax": "πρέπει να + υποτακτική",
            "past_form": "έπρεπε να (should have / had to)",
            "future_form": "θα πρέπει να (will have to)"
        },
        "keg_communicative_function": "Expressing necessity and stating examination rules",
        "example_el": "Πρέπει να έχετε μαζί σας την αστυνομική ταυτότητα και το δελτίο εξεταζομένου.",
        "example_en": "You must have with you your police identity card and candidate card.",
        "example2_el": "Πρέπει να συμπληρώσετε όλες τις απαντήσεις μέσα σε σαράντα λεπτά.",
        "example2_en": "You must fill in all answers within forty minutes."
    },
    {
        "id": "A2-U04-002",
        "greek": "χρειάζεται να",
        "english": "it is necessary to / one needs to",
        "notes": "Impersonal verb phrase followed by subjunctive. Expresses practical necessity or lack thereof ('δεν χρειάζεται να').",
        "gender_or_pos": "modal phrase (impersonal)",
        "grammatical_info": {
            "part_of_speech": "modal phrase",
            "syntax": "χρειάζεται να + υποτακτική",
            "negative": "δεν χρειάζεται να (there is no need to)"
        },
        "keg_communicative_function": "Explaining requirements or clarifying that an action is unnecessary",
        "example_el": "Δεν χρειάζεται να γράψετε πρόχειρο, μπορείτε να γράψετε απευθείας στο έντυπο.",
        "example_en": "There is no need to write a rough draft; you can write directly on the form.",
        "example2_el": "Χρειάζεται να πληρώσετε τα εξέταστρα πριν από τη λήξη της προθεσμίας.",
        "example2_en": "It is necessary to pay the exam fees before the deadline expires."
    },
    {
        "id": "A2-U04-003",
        "greek": "απαγορεύεται να",
        "english": "it is forbidden to / you must not",
        "notes": "Impersonal passive phrase taking subjunctive. Core regulatory formula seen on signs, official notices, and test instructions.",
        "gender_or_pos": "regulatory phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "syntax": "απαγορεύεται να + υποτακτική / απαγορεύεται + ουσιαστικό",
            "noun_derivative": "η απαγόρευση",
            "antonym": "επιτρέπεται να"
        },
        "keg_communicative_function": "Understanding regulatory prohibitions in notices and rules",
        "example_el": "Απαγορεύεται αυστηρά να χρησιμοποιείτε κινητά τηλέφωνα κατά τη διάρκεια των εξετάσεων.",
        "example_en": "It is strictly forbidden to use mobile phones during examinations.",
        "example2_el": "Στην αίθουσα απαγορεύεται να καπνίζετε και να καταναλώνετε τρόφιμα.",
        "example2_en": "In the hall it is forbidden to smoke and consume food."
    },
    {
        "id": "A2-U04-004",
        "greek": "επιτρέπεται να",
        "english": "it is permitted to / you may",
        "notes": "Impersonal passive phrase taking subjunctive. Contrasts with 'απαγορεύεται'.",
        "gender_or_pos": "regulatory phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "syntax": "επιτρέπεται να + υποτακτική",
            "noun_derivative": "η άδεια",
            "antonym": "απαγορεύεται να"
        },
        "keg_communicative_function": "Understanding permitted actions in official regulations and reading brochures",
        "example_el": "Στο μουσείο επιτρέπεται να βγάζετε φωτογραφίες χωρίς φλας.",
        "example_en": "In the museum it is permitted to take photographs without a flash.",
        "example2_el": "Επιτρέπεται να έχετε μαζί σας ένα μπουκάλι νερό.",
        "example2_en": "You are permitted to have a bottle of water with you."
    },
    {
        "id": "A2-U04-005",
        "greek": "μπορώ να",
        "english": "I can / may I / am I able to",
        "notes": "Modal verb 'μπορώ' followed by subjunctive. Expresses ability, possibility, or polite requests ('μπορώ να ρωτήσω κάτι;').",
        "gender_or_pos": "modal phrase",
        "grammatical_info": {
            "part_of_speech": "verb phrase",
            "syntax": "μπορώ να + υποτακτική",
            "past": "μπόρεσα να (I was able to)",
            "polite_conditional": "θα μπορούσα να (could I / I could)"
        },
        "keg_communicative_function": "Formulating polite inquiries and asking permission in Speaking Stage 2",
        "example_el": "Μπορώ να ρωτήσω πού βρίσκεται το γραφείο του διευθυντή;",
        "example_en": "May I ask where the director's office is located?",
        "example2_el": "Τώρα που έμαθα γραμματική, μπορώ να διαβάζω απλά άρθρα στα ελληνικά.",
        "example2_en": "Now that I learned grammar, I can read simple articles in Greek."
    },
    {
        "id": "A2-U04-006",
        "greek": "θέλω να",
        "english": "I want to",
        "notes": "Verb 'θέλω' followed by subjunctive. Basic formula for expressing intentions and desires.",
        "gender_or_pos": "verb phrase",
        "grammatical_info": {
            "part_of_speech": "verb phrase",
            "syntax": "θέλω να + υποτακτική",
            "polite_form": "θα ήθελα να (I would like to)"
        },
        "keg_communicative_function": "Expressing personal desires, career aims, and ordering in commercial dialogues",
        "example_el": "Θέλω να βελτιώσω την προφορά μου για να μιλάω με μεγαλύτερη άνεση.",
        "example_en": "I want to improve my pronunciation in order to speak with greater ease.",
        "example2_el": "Θέλετε να πάμε μαζί για καφέ μετά το πέρας των μαθημάτων;",
        "example2_en": "Do you want us to go together for coffee after classes finish?"
    },
    {
        "id": "A2-U04-007",
        "greek": "θα ήθελα να",
        "english": "I would like to",
        "notes": "Polite conditional formula with 'ήθελα' + subjunctive. Essential for polite customer requests and formal emails.",
        "gender_or_pos": "polite phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "syntax": "θα ήθελα να + υποτακτική",
            "register": "formal / polite"
        },
        "keg_communicative_function": "Making polite service requests and initiating formal correspondence",
        "example_el": "Θα ήθελα να ζητήσω πληροφορίες σχετικά με τα δίδακτρα του προγράμματος.",
        "example_en": "I would like to request information regarding the program's tuition fees.",
        "example2_el": "Θα ήθελα να κλείσω ένα δίκλινο δωμάτιο για το πρώτο δεκαήμερο του Αυγούστου.",
        "example2_en": "I would like to book a double room for the first ten days of August."
    },
    {
        "id": "A2-U04-008",
        "greek": "προτιμώ να",
        "english": "I prefer to",
        "notes": "Group B1 verb 'προτιμάω / προτιμώ' followed by subjunctive. Essential in pair debates (Speaking Stage 3).",
        "gender_or_pos": "verb phrase",
        "grammatical_info": {
            "part_of_speech": "verb phrase",
            "syntax": "προτιμώ να + υποτακτική / προτιμώ + ουσιαστικό",
            "noun_derivative": "η προτίμηση"
        },
        "keg_communicative_function": "Stating preferences and comparing options during candidate joint negotiations",
        "example_el": "Προτιμώ να ταξιδεύω με πλοίο επειδή μπορώ να απολαμβάνω τη διαδρομή.",
        "example_en": "I prefer to travel by ship because I can enjoy the journey.",
        "example2_el": "Προτιμάτε να μείνουμε σε ξενοδοχείο ή να νοικιάσουμε διαμέρισμα;",
        "example2_en": "Do you prefer that we stay at a hotel or rent an apartment?"
    },
    {
        "id": "A2-U04-009",
        "greek": "για να",
        "english": "in order to / so that",
        "notes": "Final subordinating conjunction expressing purpose. Followed strictly by subjunctive.",
        "gender_or_pos": "conjunction",
        "grammatical_info": {
            "part_of_speech": "final conjunction",
            "syntax": "για να + υποτακτική",
            "meaning": "expresses purpose or objective"
        },
        "keg_communicative_function": "Explaining motivations, causes, and intentions in written essays",
        "example_el": "Ήρθα νωρίς στο εξεταστικό κέντρο για να βρω εύκολα την αίθουσα.",
        "example_en": "I came early to the examination center in order to easily find the room.",
        "example2_el": "Μελετάει κάθε βράδυ για να αποκτήσει το πτυχίο.",
        "example2_en": "She studies every evening so that she can obtain the degree."
    },
    {
        "id": "A2-U04-010",
        "greek": "εύχομαι να",
        "english": "I wish that / I wish you",
        "notes": "Deponent verb 'εύχομαι' followed by subjunctive or accusative. Vital for social pleasantries.",
        "gender_or_pos": "verb phrase",
        "grammatical_info": {
            "part_of_speech": "verb phrase",
            "syntax": "εύχομαι να + υποτακτική / εύχομαι + αιτιατική (εύχομαι καλή επιτυχία)",
            "noun_derivative": "η ευχή"
        },
        "keg_communicative_function": "Offering best wishes for exams, holidays, and milestones in emails",
        "example_el": "Σας εύχομαι καλή επιτυχία στις εξετάσεις της ελληνομάθειας!",
        "example_en": "I wish you good luck in the examinations of Greek language attainment!",
        "example2_el": "Εύχομαι να περάσετε υπέροχα στις καλοκαιρινές σας διακοπές.",
        "example2_en": "I wish that you have a wonderful time on your summer holidays."
    },
    {
        "id": "A2-U04-011",
        "greek": "παρακαλώ να",
        "english": "I kindly request that / please",
        "notes": "Formal verb phrase 'παρακαλώ να' + subjunctive. Typical in administrative requests and polite notices.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "syntax": "παρακαλώ να + υποτακτική / παρακαλείστε να (passive: you are requested to)",
            "register": "polite / formal"
        },
        "keg_communicative_function": "Formulating polite administrative inquiries and understanding official notices",
        "example_el": "Παρακαλώ να μου στείλετε την επιβεβαίωση της εγγραφής μου.",
        "example_en": "I kindly request that you send me the confirmation of my registration.",
        "example2_el": "Παρακαλείστε να παραμείνετε στις θέσεις σας μέχρι τη λήξη της εξέτασης.",
        "example2_en": "You are requested to remain in your seats until the end of the examination."
    },
    {
        "id": "A2-U04-012",
        "greek": "φοβάμαι μήπως",
        "english": "I fear that / I am afraid lest",
        "notes": "Deponent verb 'φοβάμαι' followed by 'μήπως / να'. Expresses anxiety or potential negative outcome.",
        "gender_or_pos": "verb phrase",
        "grammatical_info": {
            "part_of_speech": "verb phrase",
            "syntax": "φοβάμαι μήπως + υποτακτική",
            "noun_derivative": "ο φόβος"
        },
        "keg_communicative_function": "Expressing apprehension about exam results, weather, or travel delays",
        "example_el": "Φοβάμαι μήπως χάσουμε την πτήση αν έχει πολλή κίνηση στον δρόμο.",
        "example_en": "I am afraid lest we miss the flight if there is heavy traffic on the road.",
        "example2_el": "Φοβάται να μιλήσει μπροστά σε κοινό επειδή ντρέπεται.",
        "example2_en": "He is afraid to speak in front of an audience because he is shy."
    },
    {
        "id": "A2-U04-013",
        "greek": "είναι απαραίτητο να",
        "english": "it is essential to / it is necessary to",
        "notes": "Impersonal evaluative structure taking subjunctive. Standard in formal instructions.",
        "gender_or_pos": "impersonal phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "syntax": "είναι απαραίτητο να + υποτακτική",
            "adjective": "απαραίτητος, -η, -ο"
        },
        "keg_communicative_function": "Stating indispensable conditions and prerequisite qualifications",
        "example_el": "Είναι απαραίτητο να γνωρίζετε καλά γραμματική για το επίπεδο Α2.",
        "example_en": "It is essential to know grammar well for level A2.",
        "example2_el": "Είναι απαραίτητο να προσκομίσετε φωτοτυπία του διαβατηρίου σας.",
        "example2_en": "It is essential to provide a photocopy of your passport."
    },
    {
        "id": "A2-U04-014",
        "greek": "είναι σημαντικό να",
        "english": "it is important to",
        "notes": "Evaluative impersonal expression followed by subjunctive.",
        "gender_or_pos": "impersonal phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "syntax": "είναι σημαντικό να + υποτακτική",
            "adjective": "σημαντικός, -ή, -ό"
        },
        "keg_communicative_function": "Highlighting crucial advice and recommendations in essays and presentations",
        "example_el": "Είναι σημαντικό να κοιμηθείτε καλά το βράδυ πριν από τις εξετάσεις.",
        "example_en": "It is important to sleep well the night before the examinations.",
        "example2_el": "Είναι σημαντικό να ακούτε προσεκτικά τις οδηγίες των επιτηρητών.",
        "example2_en": "It is important to listen carefully to the invigilators' instructions."
    },
    {
        "id": "A2-U04-015",
        "greek": "αξίζει να",
        "english": "it is worth doing / it pays to",
        "notes": "Impersonal phrase with 'αξίζει' + subjunctive. Core expression when recommending sights and experiences.",
        "gender_or_pos": "impersonal phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "syntax": "αξίζει να + υποτακτική",
            "noun_derivative": "η αξία"
        },
        "keg_communicative_function": "Recommending attractions, museums, and activities to tourists and friends",
        "example_el": "Αξίζει να επισκεφτείτε το Μουσείο της Ακρόπολης όταν έρθετε στην Αθήνα.",
        "example_en": "It is worth visiting the Acropolis Museum when you come to Athens.",
        "example2_el": "Αξίζει να προσπαθήσετε, ακόμα κι αν η δοκιμασία φαίνεται δύσκολη.",
        "example2_en": "It is worth trying, even if the test seems difficult."
    },
    {
        "id": "A2-U04-016",
        "greek": "είναι δύσκολο να",
        "english": "it is difficult to",
        "notes": "Evaluative impersonal structure with subjunctive. Antonym: 'είναι εύκολο να'.",
        "gender_or_pos": "impersonal phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "syntax": "είναι δύσκολο να + υποτακτική",
            "antonym": "είναι εύκολο να"
        },
        "keg_communicative_function": "Discussing learning difficulties and obstacles in oral interviews",
        "example_el": "Στην αρχή ήταν δύσκολο να καταλάβω τους φυσικούς ομιλητές όταν μιλούσαν γρήγορα.",
        "example_en": "At first it was difficult to understand native speakers when they spoke quickly.",
        "example2_el": "Είναι δύσκολο να βρεις θέση στάθμευσης στο κέντρο της πόλης.",
        "example2_en": "It is difficult to find a parking space in the city center."
    },
    {
        "id": "A2-U04-017",
        "greek": "είναι εύκολο να",
        "english": "it is easy to",
        "notes": "Evaluative impersonal structure with subjunctive. Antonym: 'είναι δύσκολο να'.",
        "gender_or_pos": "impersonal phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "syntax": "είναι εύκολο να + υποτακτική",
            "adjective": "εύκολος, -η, -ο"
        },
        "keg_communicative_function": "Expressing ease of navigation, learning, or communication",
        "example_el": "Είναι εύκολο να μετακινηθείτε στην Αθήνα χρησιμοποιώντας το μετρό.",
        "example_en": "It is easy to get around Athens using the metro.",
        "example2_el": "Μετά από συνεχή εξάσκηση, είναι εύκολο να θυμάσαι τις καταλήξεις των ρημάτων.",
        "example2_en": "After continuous practice, it is easy to remember verb endings."
    },
    {
        "id": "A2-U04-018",
        "greek": "έχω ανάγκη να",
        "english": "I need to / I have a need to",
        "notes": "Idiomatic locution expressing pressing necessity: 'έχω ανάγκη να' + subjunctive.",
        "gender_or_pos": "idiomatic phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "syntax": "έχω ανάγκη να + υποτακτική / έχω ανάγκη από + αιτιατική",
            "noun": "η ανάγκη"
        },
        "keg_communicative_function": "Stating urgent personal requirements and seeking assistance",
        "example_el": "Έχω μεγάλη ανάγκη να ξεκουραστώ μετά από μια εξαντλητική εβδομάδα εργασίας.",
        "example_en": "I really need to rest after an exhausting week of work.",
        "example2_el": "Έχουμε ανάγκη από περισσότερες πληροφορίες πριν πάρουμε την τελική απόφαση.",
        "example2_en": "We need more information before we make the final decision."
    },
    {
        "id": "A2-U04-019",
        "greek": "η ανάγκη",
        "english": "need / necessity / emergency",
        "notes": "Feminine noun in -η (-ες). In plural 'σε περίπτωση ανάγκης' means 'in case of emergency'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ανάγκες",
            "collocation": "σε περίπτωση ανάγκης (in case of emergency)"
        },
        "keg_communicative_function": "Identifying safety signs, urgent requirements, and personal necessities",
        "example_el": "Σε περίπτωση ανάγκης καλέστε αμέσως τον ευρωπαϊκό αριθμό 112.",
        "example_en": "In case of emergency immediately call the European number 112.",
        "example2_el": "Το πρόγραμμα προσαρμόζεται στις ανάγκες κάθε υποψηφίου.",
        "example2_en": "The program is adapted to the needs of each candidate."
    },
    {
        "id": "A2-U04-020",
        "greek": "η επιθυμία",
        "english": "desire / wish",
        "notes": "Feminine noun in -α (-ες). Relates to 'επιθυμώ' (to desire/wish).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι επιθυμίες",
            "verb": "επιθυμώ (-είς)",
            "genitive_singular": "της επιθυμίας"
        },
        "keg_communicative_function": "Expressing personal aspirations and customer preferences",
        "example_el": "Εξέφρασε την επιθυμία να συνεχίσει τις σπουδές του στην Ελλάδα.",
        "example_en": "He expressed the desire to continue his studies in Greece.",
        "example2_el": "Σεβόμαστε τις επιθυμίες και τις επιλογές των πελατών μας.",
        "example2_en": "We respect the desires and choices of our clients."
    },
    {
        "id": "A2-U04-021",
        "greek": "η υποχρέωση",
        "english": "obligation / duty",
        "notes": "Feminine noun in -η (-εις). Essential concept in contracts, employment, and examination rubrics.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι υποχρεώσεις",
            "adjective": "υποχρεωτικός, -ή, -ό (mandatory)",
            "genitive_singular": "της υποχρέωσης"
        },
        "keg_communicative_function": "Understanding duties, responsibilities, and compulsory regulations",
        "example_el": "Είναι υποχρέωση κάθε υποψηφίου να προσέλθει εγκαίρως στις εξετάσεις.",
        "example_en": "It is every candidate's duty to arrive on time for the examinations.",
        "example2_el": "Λόγω πολλών επαγγελματικών υποχρεώσεων δεν μπόρεσα να παρευρεθώ.",
        "example2_en": "Due to many professional obligations I was not able to attend."
    },
    {
        "id": "A2-U04-022",
        "greek": "η άδεια",
        "english": "permission / leave / permit / license",
        "notes": "Feminine noun in -α (-ες). Multiple meanings: annual leave ('άδεια διακοπών'), driving license ('άδεια οδήγησης'), residence permit ('άδεια διαμονής').",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι άδειες",
            "collocations": "άδεια διαμονής, άδεια οδήγησης, κανονική άδεια"
        },
        "keg_communicative_function": "Discussing official permits, workplace vacation leave, and driving licenses",
        "example_el": "Χρειάζεται να ανανεώσω την άδεια διαμονής μου στην αρμόδια υπηρεσία.",
        "example_en": "I need to renew my residence permit at the competent service office.",
        "example2_el": "Τον Αύγουστο θα πάρω δύο εβδομάδες άδεια από τη δουλειά μου.",
        "example2_en": "In August I will take two weeks leave from my job."
    },
    {
        "id": "A2-U04-023",
        "greek": "ο κανονισμός",
        "english": "regulation / rulebook",
        "notes": "Masculine noun in -ος (-οι). Frequently appears in reading tasks concerning school, exam, or building regulations.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι κανονισμοί",
            "genitive_singular": "του κανονισμού"
        },
        "keg_communicative_function": "Comprehending official exam, school, or community rules in Reading Part 1",
        "example_el": "Ο κανονισμός των εξετάσεων ορίζει ότι τα γραπτά παραδίδονται μετά από μία ώρα.",
        "example_en": "The examination regulations stipulate that test papers are submitted after one hour.",
        "example2_el": "Όλοι οι ένοικοι της πολυκατοικίας οφείλουν να τηρούν τον κανονισμό.",
        "example2_en": "All building residents are obliged to observe the regulations."
    },
    {
        "id": "A2-U04-024",
        "greek": "ο κανόνας",
        "english": "rule / standard",
        "notes": "Masculine noun in -ας (-ες). Collocates with 'κανόνες ασφαλείας' (safety rules) or 'γραμματικός κανόνας'.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι κανόνες",
            "genitive_singular": "του κανόνα",
            "genitive_plural": "των κανόνων"
        },
        "keg_communicative_function": "Referring to safety rules, grammatical principles, and behavioral norms",
        "example_el": "Πρέπει να τηρούμε προσεκτικά τους κανόνες οδικής κυκλοφορίας.",
        "example_en": "We must carefully observe road traffic rules.",
        "example2_el": "Ο γραμματικός αυτός κανόνας έχει μερικές σημαντικές εξαιρέσεις.",
        "example2_en": "This grammar rule has some important exceptions."
    },
    {
        "id": "A2-U04-025",
        "greek": "η συμβουλή",
        "english": "advice / tip",
        "notes": "Feminine noun in -ή (-ές). Often used in plural 'οι συμβουλές' (advice/tips).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι συμβουλές",
            "verb": "συμβουλεύω (to advise)"
        },
        "keg_communicative_function": "Giving and asking for advice in personal correspondence and oral situations",
        "example_el": "Σας δίνω μία χρήσιμη συμβουλή: διαβάστε προσεκτικά όλες τις εκφωνήσεις.",
        "example_en": "I give you a useful piece of advice: read all problem rubrics carefully.",
        "example2_el": "Ζήτησε τη συμβουλή του καθηγητή του πριν επιλέξει κατεύθυνση σπουδών.",
        "example2_en": "He sought his teacher's advice before selecting a field of study."
    },
    {
        "id": "A2-U04-026",
        "greek": "συμβουλεύω",
        "english": "to advise / I advise",
        "notes": "Verb taking accusative of person + 'να + subjunctive'. Simple past: 'συμβούλεψα'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "syntax": "συμβουλεύω κάποιον να + υποτακτική",
            "simple_past": "συμβούλεψα",
            "noun_derivative": "η συμβουλή"
        },
        "keg_communicative_function": "Advising a friend in informal emails (Writing Task 1 & 2)",
        "example_el": "Σε συμβουλεύω να ξεκινήσεις την επανάληψη τουλάχιστον έναν μήνα νωρίτερα.",
        "example_en": "I advise you to start revision at least one month earlier.",
        "example2_el": "Ο γιατρός τον συμβούλεψε να κόψει το κάπνισμα και να περπατάει καθημερινά.",
        "example2_en": "The doctor advised him to quit smoking and walk daily."
    },
    {
        "id": "A2-U04-027",
        "greek": "προτείνω",
        "english": "to propose / to suggest / I recommend",
        "notes": "Verb followed by 'να + subjunctive' or noun. Simple past: 'πρότεινα'. Key verb for pair collaboration (Stage 3).",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "syntax": "προτείνω να + υποτακτική / προτείνω + ουσιαστικό",
            "simple_past": "πρότεινα",
            "noun_derivative": "η πρόταση"
        },
        "keg_communicative_function": "Making collaborative suggestions during joint candidate discussions",
        "example_el": "Προτείνω να πάμε το απόγευμα στο μουσείο και μετά να φάμε σε μια παραδοσιακή ταβέρνα.",
        "example_en": "I suggest that we go to the museum in the afternoon and then eat at a traditional tavern.",
        "example2_el": "Τι μου προτείνετε να επισκεφτώ κατά τη διαμονή μου στα Χανιά;",
        "example2_en": "What do you recommend I visit during my stay in Chania?"
    },
    {
        "id": "A2-U04-028",
        "greek": "η πρόταση",
        "english": "proposal / suggestion / sentence (grammar)",
        "notes": "Feminine noun in -η (-εις). Means both a constructive proposal and a linguistic sentence.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι προτάσεις",
            "collocation": "κάνω μια πρόταση (to make a suggestion)"
        },
        "keg_communicative_function": "Evaluating proposals in role-plays and analyzing linguistic sentences in test rubrics",
        "example_el": "Η πρότασή σου είναι εξαιρετική, συμφωνώ απόλυτα να το κάνουμε έτσι.",
        "example_en": "Your proposal is excellent; I completely agree to do it that way.",
        "example2_el": "Συμπληρώστε τις παρακάτω προτάσεις επιλέγοντας τη σωστή λέξη.",
        "example2_en": "Complete the following sentences by choosing the correct word."
    },
    {
        "id": "A2-U04-029",
        "greek": "προσπαθώ",
        "english": "to try / to attempt",
        "notes": "Group B2 verb (-είς / -εί). Followed by 'να + subjunctive'. Simple past: 'προσπάθησα'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "syntax": "προσπαθώ να + υποτακτική",
            "simple_past": "προσπάθησα",
            "noun_derivative": "η προσπάθεια"
        },
        "keg_communicative_function": "Describing effort, study persistence, and problem-solving in interviews",
        "example_el": "Προσπαθώ να μιλάω ελληνικά καθημερινά με τους γείτονες και τους συναδέλφους μου.",
        "example_en": "I try to speak Greek every day with my neighbors and colleagues.",
        "example2_el": "Προσπάθησε να λύσει την άσκηση χωρίς να κοιτάξει τις σημειώσεις του.",
        "example2_en": "He tried to solve the exercise without looking at his notes."
    },
    {
        "id": "A2-U04-030",
        "greek": "καταφέρνω",
        "english": "to manage / to succeed in / to achieve",
        "notes": "Verb followed by 'να + subjunctive'. Simple past: 'κατάφερα'. Synonym: 'κατορθώνω'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "syntax": "καταφέρνω να + υποτακτική",
            "simple_past": "κατάφερα",
            "third_person_past": "κατάφερε"
        },
        "keg_communicative_function": "Reporting successful achievements and overcoming difficulties in past narratives",
        "example_el": "Μετά από πολύ κόπο κατάφερα να πάρω το πιστοποιητικό ελληνομάθειας.",
        "example_en": "After much effort I managed to get the certificate of attainment in Greek.",
        "example2_el": "Καταφέρατε να βρείτε έγκαιρα εισιτήρια για την παράσταση;",
        "example2_en": "Did you manage to find tickets in time for the performance?"
    },
    {
        "id": "A2-U04-031",
        "greek": "φροντίζω",
        "english": "to take care of / to make sure that",
        "notes": "Verb followed by 'να + subjunctive' or 'για + noun'. Simple past: 'φρόντισα'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "syntax": "φροντίζω να + υποτακτική / φροντίζω για",
            "simple_past": "φρόντισα",
            "noun_derivative": "η φροντίδα"
        },
        "keg_communicative_function": "Taking responsibility for arrangements and ensuring conditions are met",
        "example_el": "Φροντίστε να βρίσκεστε στην αίθουσα δεκαπέντε λεπτά πριν από την έναρξη.",
        "example_en": "Make sure to be in the hall fifteen minutes before the start.",
        "example2_el": "Η μητέρα φροντίζει πάντα για τις ανάγκες των παιδιών της.",
        "example2_en": "The mother always takes care of her children's needs."
    },
    {
        "id": "A2-U04-032",
        "greek": "αποφεύγω",
        "english": "to avoid",
        "notes": "Verb followed by 'να + subjunctive' or noun in accusative. Simple past: 'απέφυγα'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "syntax": "αποφεύγω να + υποτακτική / αποφεύγω + αιτιατική",
            "simple_past": "απέφυγα",
            "third_person_past": "απέφυγε"
        },
        "keg_communicative_function": "Giving safety tips, dietary advice, or warning interlocutors",
        "example_el": "Τις μεσημεριανές ώρες του καλοκαιριού καλό είναι να αποφεύγετε την έκθεση στον ήλιο.",
        "example_en": "During summer noon hours it is wise to avoid sun exposure.",
        "example2_el": "Προσπαθεί να αποφεύγει τα λάθη ελέγχοντας προσεκτικά το γραπτό του.",
        "example2_en": "He tries to avoid mistakes by checking his paper carefully."
    },
    {
        "id": "A2-U04-033",
        "greek": "ζητάω",
        "english": "to ask for / to request",
        "notes": "Group B1 verb (ζητάω / ζητώ). Followed by accusative or 'να + subjunctive'. Simple past: 'ζήτησα'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "syntax": "ζητάω από κάποιον να + υποτακτική / ζητάω πληροφορίες",
            "simple_past": "ζήτησα",
            "noun_derivative": "η ζήτηση"
        },
        "keg_communicative_function": "Requesting help, information, or clarification in communicative tasks",
        "example_el": "Ζήτησα από τον καθηγητή να μου εξηγήσει ξανά τη γραμματική.",
        "example_en": "I asked the professor to explain the grammar to me again.",
        "example2_el": "Στην επιστολή ζητάτε πληροφορίες σχετικά με την ημερομηνία έναρξης των μαθημάτων.",
        "example2_en": "In the letter you request information regarding the start date of classes."
    },
    {
        "id": "A2-U04-034",
        "greek": "απαιτώ",
        "english": "to demand / to require",
        "notes": "Group B2 verb (-είς / -εί). Simple past: 'απαίτησα'. Used in formal situations or to express prerequisites.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "syntax": "απαιτώ να + υποτακτική",
            "simple_past": "απαίτησα",
            "noun_derivative": "η απαίτηση"
        },
        "keg_communicative_function": "Formulating assertive claims in complaint letters or stating mandatory prerequisites",
        "example_el": "Η θέση εργασίας απαιτεί άριστη γνώση της ελληνικής και της αγγλικής γλώσσας.",
        "example_en": "The job position requires excellent knowledge of Greek and English.",
        "example2_el": "Απαιτώ να μου επιστραφεί το αντίτιμο του ακυρωμένου εισιτηρίου.",
        "example2_en": "I demand that the price of the cancelled ticket be refunded to me."
    },
    {
        "id": "A2-U04-035",
        "greek": "η απαίτηση",
        "english": "requirement / demand",
        "notes": "Feminine noun in -η (-εις). Often encountered in job vacancy advertisements.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι απαιτήσεις",
            "verb": "απαιτώ",
            "genitive_singular": "της απαίτησης"
        },
        "keg_communicative_function": "Analyzing job requirements, university prerequisites, and exam criteria",
        "example_el": "Η γνώση υπολογιστή αποτελεί βασική απαίτηση για τη συγκεκριμένη θέση.",
        "example_en": "Computer literacy constitutes a basic requirement for this specific position.",
        "example2_el": "Οι απαιτήσεις του επιπέδου Α2 περιλαμβάνουν κατανόηση και παραγωγή απλού λόγου.",
        "example2_en": "The requirements of level A2 include comprehension and production of simple speech."
    }
]

def synthesize_audio_threaded(cards, unit_id):
    """
    Synthesize all audio files for cards using ThreadPoolExecutor for high parallelism.
    """
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
    
    batch2_entries = [
        {
            "id": "unit-a2-03",
            "title": "Μάθημα 3: Σχέδια, Όνειρα & Ο Μέλλοντας (Future Plans, Intentions & Forecasts)",
            "description": "Formulating future plans, intentions, and predictions using Simple and Continuous Future (Συνοπτικός & Εξακολουθητικός Μέλλοντας), temporal adverbials (του χρόνου, σύντομα, σε λίγο), and verbs of intention (σκοπεύω, σχεδιάζω, ελπίζω).",
            "order": "KEG-A2-03-A",
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2-03/lesson-01.yaml",
                    "title": "Μάθημα 3: Σχέδια, Όνειρα & Ο Μέλλοντας (Future Plans, Intentions & Forecasts)"
                }
            ]
        },
        {
            "id": "unit-a2-04",
            "title": "Μάθημα 4: Επιθυμίες, Ανάγκες & Υποτακτική (Wishes, Obligations & Subjunctive Mood)",
            "description": "Expressing wishes, necessity, prohibitions, and polite requests using the Subjunctive mood (Υποτακτική) with modal operators (πρέπει να, απαγορεύεται να, επιτρέπεται να, μπορώ να, θέλω να, για να, αξίζει να).",
            "order": "KEG-A2-04-A",
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2-04/lesson-01.yaml",
                    "title": "Μάθημα 4: Επιθυμίες, Ανάγκες & Υποτακτική (Wishes, Obligations & Subjunctive Mood)"
                }
            ]
        }
    ]
    
    added = 0
    for entry in batch2_entries:
        if entry["id"] not in existing_ids:
            units.append(entry)
            existing_ids.add(entry["id"])
            added += 1
            print(f"[Manifest] Appended {entry['id']} ({entry['order']})")
        else:
            # Update lessons array if missing
            for u in units:
                if u["id"] == entry["id"]:
                    u["lessons"] = entry["lessons"]
            print(f"[Manifest] {entry['id']} already exists, verified lessons array")
            
    manifest["units"] = units
    with open(manifest_path, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"[Manifest] Manifest saved with {len(units)} units total ({added} new).")

def main():
    print("--- Starting KEG-A2 Batch 2 Generation & Parallel Synthesis ---")
    
    # 1. Unit A2-03
    u3_notes = """Unit A2-03 Core Notes: Σχέδια, Όνειρα & Ο Μέλλοντας (Future Plans & Predictions)
• Simple Future (Συνοπτικός Μέλλοντας):
  - Formed with 'θα' + aorist dependent stem (θα πάω, θα δω, θα κάνω, θα μείνω, θα ταξιδέψω, θα πάρω, θα δώσω, θα έρθω, θα φύγω, θα βρω, θα στείλω).
  - Used for single, completed future events at a specific time.

• Continuous Future (Εξακολουθητικός Μέλλοντας):
  - Formed with 'θα' + present stem (θα δουλεύω, θα διαβάζω, θα μένω).
  - Used for duration, repetition, or background state in the future.

• Expressions of Intention & Probability:
  - σκοπεύω να (I intend to), σχεδιάζω να (I plan to), ελπίζω να (I hope to), υπόσχομαι να (I promise to).
  - σίγουρα (definitely), ίσως (perhaps), πιθανόν (probably), αποκλείεται να (it is impossible to).

• Temporal Markers:
  - του χρόνου (next year), τον επόμενο μήνα (next month), σύντομα (soon), σε λίγο (shortly), μεθαύριο (day after tomorrow)."""

    synthesize_audio_threaded(CARDS_U03, "unit-a2-03")
    save_unit_yaml(
        unit_id="unit-a2-03",
        lesson_id="lesson-01",
        title="Μάθημα 3: Σχέδια, Όνειρα & Ο Μέλλοντας (Future Plans, Intentions & Forecasts)",
        description="Formulating future plans, intentions, and predictions using Simple and Continuous Future (Συνοπτικός & Εξακολουθητικός Μέλλοντας), temporal adverbials (του χρόνου, σύντομα, σε λίγο), and verbs of intention (σκοπεύω, σχεδιάζω, ελπίζω).",
        lesson_notes=u3_notes,
        cards=CARDS_U03
    )

    # 2. Unit A2-04
    u4_notes = """Unit A2-04 Core Notes: Επιθυμίες, Ανάγκες & Υποτακτική (Wishes, Obligations & Subjunctive Mood)
• Dependent Subjunctive (Υποτακτική) Structure:
  - Introduced by particles: να, για να (purpose), μήπως (fear/lest).
  - Continuous Subjunctive (present stem): να διαβάζω (habit/duration).
  - Simple Subjunctive (aorist stem): να διαβάσω (single completion).

• Core Impersonal & Modal Operators at A2:
  - πρέπει να (must / ought to) / δεν πρέπει να (must not).
  - χρειάζεται να (needs to) / δεν χρειάζεται να (no need to).
  - απαγορεύεται να (forbidden to) vs. επιτρέπεται να (permitted to).
  - μπορώ να (I can / may I) / θα ήθελα να (polite: I would like to).
  - προτιμώ να (I prefer to) / αξίζει να (it is worth doing).
  - είναι απαραίτητο / σημαντικό / δύσκολο / εύκολο να.

• Regulatory & Communicative Register:
  - High frequency in official public signs, exam rubrics, rules of conduct, and polite administrative correspondence."""

    synthesize_audio_threaded(CARDS_U04, "unit-a2-04")
    save_unit_yaml(
        unit_id="unit-a2-04",
        lesson_id="lesson-01",
        title="Μάθημα 4: Επιθυμίες, Ανάγκες & Υποτακτική (Wishes, Obligations & Subjunctive Mood)",
        description="Expressing wishes, necessity, prohibitions, and polite requests using the Subjunctive mood (Υποτακτική) with modal operators (πρέπει να, απαγορεύεται να, επιτρέπεται να, μπορώ να, θέλω να, για να, αξίζει να).",
        lesson_notes=u4_notes,
        cards=CARDS_U04
    )

    # 3. Update manifest
    update_manifest()
    print("\n[OK] Batch 2 generation and parallel synthesis finished successfully!")

if __name__ == "__main__":
    main()

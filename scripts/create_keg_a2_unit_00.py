# -*- coding: utf-8 -*-
"""
Generate Unit A2-00: KEG A2 Exam Instructions & Rubrics (30 cards)
with dual example sentences and synthesize Chirp-3 HD TTS for headwords and sentences.
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

CARDS = [
    {
        "id": "A2-U00-001",
        "greek": "αιτιολογώ",
        "english": "to justify / explain one's reasoning",
        "notes": "Key rubric verb in A2 reading and listening. Imperative plural: 'αιτιολογήστε'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type B2 (-ώ / -είς)",
            "third_person_singular": "αιτιολογεί",
            "first_person_plural": "αιτιολογούμε",
            "imperative_formal": "αιτιολογήστε"
        },
        "keg_communicative_function": "Justifying answers and decisions in reading & listening tasks",
        "example_el": "Αιτιολογήστε την απάντησή σας με μία πρόταση από το κείμενο.",
        "example_en": "Justify your answer with one sentence from the text.",
        "example2_el": "Πρέπει να αιτιολογήσετε γιατί επιλέξατε τη δήλωση αυτή.",
        "example2_en": "You must justify why you chose this statement."
    },
    {
        "id": "A2-U00-002",
        "greek": "η περίληψη",
        "english": "summary / synopsis",
        "notes": "Feminine noun in -η (-εις). Essential in reading comprehension synthesis.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι περιλήψεις",
            "accusative_singular": "την περίληψη",
            "genitive_singular": "της περίληψης"
        },
        "keg_communicative_function": "Understanding and writing text summaries",
        "example_el": "Γράψτε μία σύντομη περίληψη των κύριων σημείων του άρθρου.",
        "example_en": "Write a short summary of the main points of the article.",
        "example2_el": "Η περίληψη δεν πρέπει να ξεπερνά τις σαράντα λέξεις.",
        "example2_en": "The summary must not exceed forty words."
    },
    {
        "id": "A2-U00-003",
        "greek": "η επιστολή",
        "english": "letter (formal)",
        "notes": "Feminine noun in -η (-ες). Core genre required in KEG A2 Writing Task 2.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι επιστολές",
            "accusative_singular": "την επιστολή",
            "genitive_singular": "της επιστολής"
        },
        "keg_communicative_function": "Composing formal letters and inquiries in Writing Task 2",
        "example_el": "Συντάξτε μία επίσημη επιστολή προς τον διευθυντή της σχολής.",
        "example_en": "Draft a formal letter to the director of the school.",
        "example2_el": "Στην επιστολή αναφέρετε τον λόγο για τον οποίο ζητάτε πληροφορίες.",
        "example2_en": "In the letter state the reason for which you are requesting information."
    },
    {
        "id": "A2-U00-004",
        "greek": "το μήνυμα ηλεκτρονικού ταχυδρομείου",
        "english": "email message",
        "notes": "Neuter compound noun. Also frequently referred to simply as 'το email'.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μηνύματα ηλεκτρονικού ταχυδρομείου",
            "accusative_singular": "το μήνυμα ηλεκτρονικού ταχυδρομείου"
        },
        "keg_communicative_function": "Writing communicative emails to friends, colleagues, or services",
        "example_el": "Στείλτε ένα μήνυμα ηλεκτρονικού ταχυδρομείου στον φίλο σας για τις διακοπές.",
        "example_en": "Send an email message to your friend about vacations.",
        "example2_el": "Απαντήστε στο email επιβεβαιώνοντας την κράτηση του δωματίου.",
        "example2_en": "Reply to the email confirming the booking of the room."
    },
    {
        "id": "A2-U00-005",
        "greek": "η αγγελία",
        "english": "advertisement / classified ad / notice",
        "notes": "Feminine noun in -α (-ες). Frequent authentic genre in A2 Reading Part 1 & 2.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι αγγελίες",
            "accusative_singular": "την αγγελία"
        },
        "keg_communicative_function": "Reading job postings, rentals, and commercial notices",
        "example_el": "Διαβάστε την παρακάτω αγγελία εργασίας και απαντήστε στις ερωτήσεις.",
        "example_en": "Read the following job advertisement and answer the questions.",
        "example2_el": "Η αγγελία ζητά έναν υπάλληλο γραφείου με γνώση αγγλικών.",
        "example2_en": "The classified ad seeks an office clerk with knowledge of English."
    },
    {
        "id": "A2-U00-006",
        "greek": "η συνέντευξη",
        "english": "interview",
        "notes": "Feminine noun in -η (-εις). Appears in both Listening and Speaking tasks.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι συνεντεύξεις",
            "accusative_singular": "τη συνέντευξη"
        },
        "keg_communicative_function": "Listening to recorded interviews and participating in oral test interviews",
        "example_el": "Ακούστε τη συνέντευξη του συγγραφέα στο ραδιόφωνο.",
        "example_en": "Listen to the interview of the author on the radio.",
        "example2_el": "Στη συνέντευξη μιλάει για τη ζωή του στο εξωτερικό.",
        "example2_en": "In the interview he speaks about his life abroad."
    },
    {
        "id": "A2-U00-007",
        "greek": "το φυλλάδιο",
        "english": "booklet / leaflet / exam booklet",
        "notes": "Neuter noun in -ο (-α). Used for examination test booklets and brochures.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα φυλλάδια",
            "accusative_singular": "το φυλλάδιο"
        },
        "keg_communicative_function": "Handling the official May examination booklet and promotional flyers",
        "example_el": "Συμπληρώστε τις απαντήσεις σας στο ειδικό εξεταστικό φυλλάδιο.",
        "example_en": "Fill in your answers in the special examination booklet.",
        "example2_el": "Κοιτάξτε το ενημερωτικό φυλλάδιο του μουσείου.",
        "example2_en": "Look at the informative brochure of the museum."
    },
    {
        "id": "A2-U00-008",
        "greek": "το ακουστικό κείμενο",
        "english": "listening text / audio passage",
        "notes": "Collocation in KEG Listening exam directions. Heard twice with a pause.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ακουστικά κείμενα",
            "accusative_singular": "το ακουστικό κείμενο"
        },
        "keg_communicative_function": "Following official May listening test instructions",
        "example_el": "Θα ακούσετε το ακουστικό κείμενο δύο φορές με μικρό διάλειμμα.",
        "example_en": "You will hear the listening text twice with a short pause.",
        "example2_el": "Πριν από κάθε ακουστικό κείμενο έχετε ένα λεπτό για να διαβάσετε τις ερωτήσεις.",
        "example2_en": "Before each listening text you have one minute to read the questions."
    },
    {
        "id": "A2-U00-009",
        "greek": "το φύλλο απαντήσεων",
        "english": "answer sheet",
        "notes": "Collocation: 'το φύλλο απαντήσεων'. Must be filled in pen by candidates.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα φύλλα απαντήσεων",
            "accusative_singular": "το φύλλο απαντήσεων"
        },
        "keg_communicative_function": "Official answer transfer protocol during exams",
        "example_el": "Μεταφέρετε προσεκτικά όλες τις απαντήσεις σας στο φύλλο απαντήσεων.",
        "example_en": "Transfer all your answers carefully to the answer sheet.",
        "example2_el": "Μην σημειώνετε με μολύβι στο τελικό φύλλο απαντήσεων.",
        "example2_en": "Do not mark with pencil on the final answer sheet."
    },
    {
        "id": "A2-U00-010",
        "greek": "ο εξεταστής",
        "english": "examiner (male)",
        "notes": "Masculine noun in -ης (-ές). Feminine is 'η εξετάστρια'.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι εξεταστές",
            "accusative_singular": "τον εξεταστή",
            "feminine_counterpart": "η εξετάστρια"
        },
        "keg_communicative_function": "Interacting with the official exam jury during oral testing",
        "example_el": "Ο εξεταστής σάς κάνει ερωτήσεις σχετικά με την καθημερινή σας ζωή.",
        "example_en": "The examiner asks you questions regarding your daily life.",
        "example2_el": "Απευθυνθείτε στην εξετάστρια αν δεν ακούτε καθαρά.",
        "example2_en": "Address the examiner if you cannot hear clearly."
    },
    {
        "id": "A2-U00-011",
        "greek": "ο υποψήφιος",
        "english": "candidate / examinee (male)",
        "notes": "Masculine in -ος (-οι). Feminine is 'η υποψήφια' (-ες).",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι υποψήφιοι",
            "accusative_singular": "τον υποψήφιο",
            "feminine_counterpart": "η υποψήφια"
        },
        "keg_communicative_function": "Candidate role identification and registration",
        "example_el": "Κάθε υποψήφιος πρέπει να έχει μαζί του την ταυτότητά του.",
        "example_en": "Every candidate must have their identity card with them.",
        "example2_el": "Η υποψήφια ολοκλήρωσε το γραπτό μέρος της εξέτασης στην ώρα της.",
        "example2_en": "The candidate completed the written portion of the exam on time."
    },
    {
        "id": "A2-U00-012",
        "greek": "το πιστοποιητικό επάρκειας",
        "english": "certificate of attainment / proficiency",
        "notes": "Official credential issued by the Centre for the Greek Language (ΚΕΓ).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πιστοποιητικά επάρκειας",
            "accusative_singular": "το πιστοποιητικό επάρκειας"
        },
        "keg_communicative_function": "Referencing the official KEG certification goals",
        "example_el": "Το πιστοποιητικό επάρκειας της ελληνομάθειας αναγνωρίζεται διεθνώς.",
        "example_en": "The certificate of attainment in Greek is recognized internationally.",
        "example2_el": "Οι εξετάσεις για το πιστοποιητικό επάρκειας γίνονται κάθε Μάιο.",
        "example2_en": "The exams for the certificate of attainment take place every May."
    },
    {
        "id": "A2-U00-013",
        "greek": "η προφορική δοκιμασία",
        "english": "oral examination / speaking test",
        "notes": "Official term for Part 4 (Παραγωγή προφορικού λόγου).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι προφορικές δοκιμασίες",
            "accusative_singular": "την προφορική δοκιμασία"
        },
        "keg_communicative_function": "Understanding the oral speaking evaluation format",
        "example_el": "Η προφορική δοκιμασία επιπέδου Α2 διαρκεί περίπου δέκα με δεκαπέντε λεπτά.",
        "example_en": "The level A2 oral examination lasts approximately ten to fifteen minutes.",
        "example2_el": "Στην προφορική δοκιμασία συμμετέχετε σε διάλογο με έναν άλλο υποψήφιο.",
        "example2_en": "In the oral examination you participate in a dialogue with another candidate."
    },
    {
        "id": "A2-U00-014",
        "greek": "η γραπτή δοκιμασία",
        "english": "written examination",
        "notes": "Official term encompassing Reading, Listening, and Writing papers.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι γραπτές δοκιμασίες",
            "accusative_singular": "τη γραπτή δοκιμασία"
        },
        "keg_communicative_function": "Navigating the written exam schedule",
        "example_el": "Η γραπτή δοκιμασία περιλαμβάνει κατανόηση κειμένου και παραγωγή λόγου.",
        "example_en": "The written examination includes reading comprehension and written production.",
        "example2_el": "Η γραπτή δοκιμασία αρχίζει στις εννέα το πρωί.",
        "example2_en": "The written examination begins at nine in the morning."
    },
    {
        "id": "A2-U00-015",
        "greek": "η κάρτα ρόλου",
        "english": "role-play cue card",
        "notes": "Used in Speaking Task 2: each candidate receives distinct prompts to role-play.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι κάρτες ρόλου",
            "accusative_singular": "την κάρτα ρόλου"
        },
        "keg_communicative_function": "Conducting pair interactions based on cue card prompts",
        "example_el": "Διαβάστε την κάρτα ρόλου και προετοιμάστε τον διάλογο με τον συμμαθητή σας.",
        "example_en": "Read the role card and prepare the dialogue with your classmate.",
        "example2_el": "Στην κάρτα ρόλου αναφέρονται οι πληροφορίες που πρέπει να ζητήσετε.",
        "example2_en": "On the role card the information that you must request is mentioned."
    },
    {
        "id": "A2-U00-016",
        "greek": "η σύγκριση",
        "english": "comparison",
        "notes": "Feminine noun in -η (-εις). Essential communicative function at A2.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι συγκρίσεις",
            "accusative_singular": "τη σύγκριση"
        },
        "keg_communicative_function": "Comparing options, photos, routines, and experiences",
        "example_el": "Κάντε μία σύγκριση ανάμεσα στη ζωή στην πόλη και στο χωριό.",
        "example_en": "Make a comparison between life in the city and in the village.",
        "example2_el": "Από τη σύγκριση των δύο εικόνων προκύπτουν σημαντικές διαφορές.",
        "example2_en": "From the comparison of the two images significant differences emerge."
    },
    {
        "id": "A2-U00-017",
        "greek": "η άποψη",
        "english": "view / opinion",
        "notes": "Feminine in -η (-εις). Commonly used in: 'κατά την άποψή μου' (in my view).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι απόψεις",
            "accusative_singular": "την άποψη",
            "genitive_singular": "της άποψης"
        },
        "keg_communicative_function": "Expressing and substantiating opinions in speaking and writing",
        "example_el": "Εκφράστε την άποψή σας για τα πλεονεκτήματα των μέσων μαζικής μεταφοράς.",
        "example_en": "Express your opinion about the advantages of public transport.",
        "example2_el": "Κατά την άποψή μου, η εκμάθηση μιας γλώσσας ανοίγει νέους δρόμους.",
        "example2_en": "In my view, learning a language opens new avenues."
    },
    {
        "id": "A2-U00-018",
        "greek": "η περιγραφή",
        "english": "description",
        "notes": "Feminine in -η (-ες). Core task directive in speaking and writing.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι περιγραφές",
            "accusative_singular": "την περιγραφή"
        },
        "keg_communicative_function": "Describing objects, people, apartments, and vacation spots",
        "example_el": "Δώστε μία λεπτομερή περιγραφή ενός πρόσφατου ταξιδιού σας.",
        "example_en": "Provide a detailed description of a recent trip of yours.",
        "example2_el": "Η περιγραφή του διαμερίσματος περιλαμβάνει τρία υπνοδωμάτια και μπαλκόνι.",
        "example2_en": "The description of the apartment includes three bedrooms and a balcony."
    },
    {
        "id": "A2-U00-019",
        "greek": "η αφήγηση",
        "english": "narrative / narration of past events",
        "notes": "Feminine in -η (-εις). Writing Task 2 tests personal narration in the past.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι αφηγήσεις",
            "accusative_singular": "την αφήγηση"
        },
        "keg_communicative_function": "Narrating past events chronologically using Aorist and Imperfect",
        "example_el": "Στην αφήγησή σας χρησιμοποιήστε παρελθοντικούς χρόνους, όπως ο αόριστος.",
        "example_en": "In your narrative use past tenses, such as the aorist.",
        "example2_el": "Ακολουθεί μία σύντομη αφήγηση των γεγονότων της περασμένης εβδομάδας.",
        "example2_en": "A short narration of the events of the past week follows."
    },
    {
        "id": "A2-U00-020",
        "greek": "η ανακοίνωση",
        "english": "announcement / public notice",
        "notes": "Feminine in -η (-εις). Key audio genre heard in metro stations, airports, shops.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ανακοινώσεις",
            "accusative_singular": "την ανακοίνωση"
        },
        "keg_communicative_function": "Extracting key details from transit and municipal announcements",
        "example_el": "Ακούστε την ανακοίνωση στο αεροδρόμιο για την αλλαγή της πύλης επιβίβασης.",
        "example_en": "Listen to the announcement at the airport regarding the boarding gate change.",
        "example2_el": "Η ανακοίνωση του δήμου ενημερώνει για τη διακοπή νερού.",
        "example2_en": "The announcement of the municipality informs about the water cut."
    },
    {
        "id": "A2-U00-021",
        "greek": "η πρόσκληση",
        "english": "invitation",
        "notes": "Feminine in -η (-εις). Genre for Writing Task 1 (writing or answering invitations).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι προσκλήσεις",
            "accusative_singular": "την πρόσκληση"
        },
        "keg_communicative_function": "Formulating and responding to invitations",
        "example_el": "Γράψτε μία πρόσκληση σε έναν συνάδελφο για τα γενέθλιά σας.",
        "example_en": "Write an invitation to a colleague for your birthday.",
        "example2_el": "Δεχτήκατε μία πρόσκληση σε γάμο και απαντάτε ευγενικά.",
        "example2_en": "You received an invitation to a wedding and you reply politely."
    },
    {
        "id": "A2-U00-022",
        "greek": "η αποδοχή",
        "english": "acceptance",
        "notes": "Feminine in -η (-ες). Used when accepting invitations, offers, or terms.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι αποδοχές",
            "accusative_singular": "την αποδοχή"
        },
        "keg_communicative_function": "Accepting invitations and agreements formally or informally",
        "example_el": "Δηλώστε την αποδοχή της πρόσκλησης μέσω ηλεκτρονικού μηνύματος.",
        "example_en": "State the acceptance of the invitation via email message.",
        "example2_el": "Η αποδοχή των όρων του συμβολαίου είναι υποχρεωτική.",
        "example2_en": "The acceptance of the terms of the contract is mandatory."
    },
    {
        "id": "A2-U00-023",
        "greek": "η άρνηση",
        "english": "refusal / declining",
        "notes": "Feminine in -η (-εις). Essential polite formula: 'δυστυχώς δεν μπορώ να...' .",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι αρνήσεις",
            "accusative_singular": "την άρνηση"
        },
        "keg_communicative_function": "Declining invitations or proposals politely with justification",
        "example_el": "Γράψτε ένα ευγενικό μήνυμα άρνησης εξηγώντας γιατί δεν μπορείτε να πάτε.",
        "example_en": "Write a polite note of decline explaining why you cannot go.",
        "example2_el": "Η άρνηση της πρότασης έγινε με πολύ διακριτικό τρόπο.",
        "example2_en": "The refusal of the proposal was done in a very discreet manner."
    },
    {
        "id": "A2-U00-024",
        "greek": "το αίτημα",
        "english": "request / formal petition",
        "notes": "Neuter in -μα (-ματα). Key term in administrative writing tasks.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα αιτήματα",
            "accusative_singular": "το αίτημα"
        },
        "keg_communicative_function": "Making formal requests and inquiries to public or private bodies",
        "example_el": "Διατυπώστε το αίτημά σας ευγενικά χρησιμοποιώντας πληθυντικό ευγενείας.",
        "example_en": "Formulate your request politely using the polite plural.",
        "example2_el": "Το αίτημα για παράταση της προθεσμίας έγινε δεκτό.",
        "example2_en": "The request for an extension of the deadline was accepted."
    },
    {
        "id": "A2-U00-025",
        "greek": "η διαμαρτυρία",
        "english": "complaint / protest / grievance",
        "notes": "Feminine in -α (-ες). Common genre in customer service and hotel scenarios.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι διαμαρτυρίες",
            "accusative_singular": "τη διαμαρτυρία"
        },
        "keg_communicative_function": "Expressing complaints and dissatisfaction constructively",
        "example_el": "Συντάξτε μία επιστολή διαμαρτυρίας για την κακή εξυπηρέτηση στο ξενοδοχείο.",
        "example_en": "Draft a letter of complaint regarding the poor service at the hotel.",
        "example2_el": "Εκφράζω τη διαμαρτυρία μου για την καθυστέρηση της πτήσης.",
        "example2_en": "I express my complaint regarding the delay of the flight."
    },
    {
        "id": "A2-U00-026",
        "greek": "το παράπονο",
        "english": "complaint / grievance",
        "notes": "Neuter in -ο (-α). Used interchangeably with 'διαμαρτυρία' in daily Greek.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα παράπονα",
            "accusative_singular": "το παράπονο"
        },
        "keg_communicative_function": "Communicating customer service issues in shops and hotels",
        "example_el": "Έχετε κάποιο παράπονο από τις υπηρεσίες του καταστήματος;",
        "example_en": "Do you have any complaint about the services of the store?",
        "example2_el": "Διατυπώστε τα παράπονά σας στη διεύθυνση του εστιατορίου.",
        "example2_en": "Address your complaints to the management of the restaurant."
    },
    {
        "id": "A2-U00-027",
        "greek": "η προθεσμία",
        "english": "deadline / time limit",
        "notes": "Feminine in -α (-ες). Crucial for registration and course schedules.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι προθεσμίες",
            "accusative_singular": "την προθεσμία"
        },
        "keg_communicative_function": "Observing deadlines and enrollment schedules",
        "example_el": "Η προθεσμία υποβολής των αιτήσεων λήγει στα τέλη Μαρτίου.",
        "example_en": "The deadline for submission of applications expires at the end of March.",
        "example2_el": "Προσέξτε την προθεσμία για να μην χάσετε την εγγραφή σας.",
        "example2_en": "Pay attention to the deadline so that you do not miss your registration."
    },
    {
        "id": "A2-U00-028",
        "greek": "τα εξέταστρα",
        "english": "examination fees",
        "notes": "Neuter plural noun (μόνο πληθυντικός / plurale tantum).",
        "gender_or_pos": "noun (neuter plural)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter plural)",
            "nominative_plural": "τα εξέταστρα",
            "accusative_plural": "τα εξέταστρα",
            "genitive_plural": "των εξετάστρων"
        },
        "keg_communicative_function": "Administrative inquiries regarding examination enrollment fees",
        "example_el": "Η καταβολή των εξετάστρων είναι απαραίτητη για την οριστικοποίηση της αίτησης.",
        "example_en": "The payment of examination fees is necessary for finalizing the application.",
        "example2_el": "Πληρώστε το αντίτιμο των εξετάστρων μέσω τραπεζικής κατάθεσης.",
        "example2_en": "Pay the amount of the examination fees via bank transfer."
    },
    {
        "id": "A2-U00-029",
        "greek": "το εξεταστικό κέντρο",
        "english": "examination center",
        "notes": "Official venue where the May examinations take place globally.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα εξεταστικά κέντρα",
            "accusative_singular": "το εξεταστικό κέντρο"
        },
        "keg_communicative_function": "Exam logistics and arrival procedures",
        "example_el": "Ενημερωθείτε για τη διεύθυνση του εξεταστικού κέντρου πριν από την ημέρα της δοκιμασίας.",
        "example_en": "Inquire about the address of the examination center before the day of the test.",
        "example2_el": "Πρέπει να βρίσκεστε στο εξεταστικό κέντρο μισή ώρα νωρίτερα.",
        "example2_en": "You must be at the examination center half an hour earlier."
    },
    {
        "id": "A2-U00-030",
        "greek": "το αποτέλεσμα",
        "english": "result / outcome",
        "notes": "Neuter in -μα (-ματα). Refers to the official scoring published by KEG.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα αποτελέσματα",
            "accusative_singular": "το αποτέλεσμα"
        },
        "keg_communicative_function": "Checking and discussing examination results",
        "example_el": "Τα αποτελέσματα των εξετάσεων ανακοινώνονται συνήθως στα τέλη Ιουλίου.",
        "example_en": "The examination results are usually announced at the end of July.",
        "example2_el": "Το αποτέλεσμα της προσπάθειάς σας εξαρτάται από τη συστηματική μελέτη.",
        "example2_en": "The result of your effort depends on systematic study."
    }
]

def main():
    u_dir = CONTENT_DIR / "unit-a2-00"
    u_dir.mkdir(parents=True, exist_ok=True)
    yaml_file = u_dir / "lesson-01.yaml"
    
    total_audio = 0
    print(f"=== Synthesizing Audio & Generating {yaml_file.name} ===")
    
    for c in CARDS:
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
        "unit_id": "unit-a2-00",
        "lesson_id": "lesson-01",
        "title": "Μάθημα 0: Οδηγίες Εξετάσεων Α2 & Γλώσσα Rubrics (KEG A2 Exam Instructions & Rubrics)",
        "description": "Essential exam instructions, task rubrics, official test terminology, and evaluation guidelines for the Centre for the Greek Language (ΚΕΓ / KEG) Level A2 May certification examinations.",
        "lesson_status": "not_started",
        "lesson_notes": """Unit A2-00 Core Notes: Γλώσσα Εξετάσεων & Οδηγίες Επιπέδου Α2 (KEG A2 Exam Specifications)

• Overview of the Official May Examination (Πιστοποιητικό Επάρκειας της Ελληνομάθειας - Επίπεδο Α2):
  Conducted annually in May by the Centre for the Greek Language (ΚΕΓ) under the Hellenic Ministry of Education.
  Comprises four mandatory evaluation sections:
  1. Κατανόηση Προφορικού Λόγου (Listening Comprehension - 30 mins): 3 parts covering recorded announcements, public notices, and dialogic interviews.
  2. Κατανόηση Γραπτού Λόγου (Reading Comprehension - 45 mins): 3 parts covering brochures, advertisements, articles, and short authentic texts.
  3. Παραγωγή Γραπτού Λόγου (Written Production - 45 mins): 2 tasks. Task 1: Short communicative email/postcard (40-50 words). Task 2: Narrative or descriptive letter/email (70-80 words).
  4. Παραγωγή Προφορικού Λόγου (Oral Production - 10-15 mins): 3 tasks in candidate pairs. Task 1: Personal interview & biography. Task 2: Role-play using cue cards (κάρτες ρόλου). Task 3: Joint problem-solving or discussion.

• Key Advanced Rubric Imperatives at Level A2:
  - αιτιολογήστε (justify/substantiate your answer with evidence from the text)
  - συγκρίνετε (compare the two options or situations)
  - συντάξτε (draft a formal letter or email)
  - διατυπώστε (formulate a polite request or complaint)
  - περιγράψτε (describe an event, place, or person in detail)
  - αφηγηθείτε (narrate a past experience using chronological past tenses)

• Scoring & Success Threshold:
  Success requires passing each individual skill with at least 60% (12/20 marks).""",
        "entries": CARDS
    }
    
    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(lesson_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        
    print(f"\n[OK] Successfully wrote {len(CARDS)} cards to {yaml_file}")
    print(f"[OK] Total audio files synthesized: {total_audio}")

if __name__ == "__main__":
    main()

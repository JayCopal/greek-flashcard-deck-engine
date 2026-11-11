# -*- coding: utf-8 -*-
"""
Generate KEG-A2 Part 2 Batch 1:
- Unit A2P2-01: KEG-A2-P2-01-A (30 cards) - Everyday Dialogues & Conversational Exchanges
- Unit A2P2-02: KEG-A2-P2-02-A (30 cards) - Personal Identity, Family & Social Circle
Includes dual exam example sentences and multi-threaded Google Cloud Chirp-3 HD TTS.
"""
import sys
import os
import yaml
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from server.tts_service import synthesize_greek_chirp, generate_audio_filename

AUDIO_DIR = BASE_DIR / "audio"
CONTENT_DIR = BASE_DIR / "content"

# -------------------------------------------------------------
# UNIT A2P2-01 CARDS (30 cards)
# Theme: Καθημερινός Διάλογος & Προφορική Επικοινωνία
# -------------------------------------------------------------
CARDS_U01 = [
    {
        "id": "A2P2-U01-001",
        "greek": "μπορώ να σας ρωτήσω κάτι;",
        "english": "may I ask you something?",
        "notes": "Polite conversational opening formula. Essential for Speaking Stages 1 and 2.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "components": "modal verb 'μπορώ' + weak clitic accusative 'σας' + subjunctive 'να ρωτήσω'",
            "register": "polite / formal"
        },
        "keg_communicative_function": "Initiating a polite enquiry or request in spoken interaction",
        "example_el": "Συγγνώμη, μπορώ να σας ρωτήσω κάτι σχετικά με το πρόγραμμα των εξετάσεων;",
        "example_en": "Excuse me, may I ask you something regarding the exam schedule?",
        "example2_el": "Μπορώ να σας ρωτήσω πώς μπορώ να φτάσω στο κέντρο της πόλης;",
        "example2_en": "May I ask you how I can get to the city center?"
    },
    {
        "id": "A2P2-U01-002",
        "greek": "τι εννοείτε ακριβώς;",
        "english": "what exactly do you mean?",
        "notes": "Essential clarification phrase for Speaking and Listening comprehension.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "εννοώ (contracted verb in -ώ)",
            "person": "second person plural (formal / plural)",
            "adverb": "ακριβώς"
        },
        "keg_communicative_function": "Requesting clarification when a statement is unclear",
        "example_el": "Δεν κατάλαβα την τελευταία οδηγία, τι εννοείτε ακριβώς;",
        "example_en": "I did not understand the last instruction, what exactly do you mean?",
        "example2_el": "Όταν λέτε ότι η εγγραφή είναι υποχρεωτική, τι εννοείτε ακριβώς;",
        "example2_en": "When you say registration is mandatory, what exactly do you mean?"
    },
    {
        "id": "A2P2-U01-003",
        "greek": "μήπως μπορείτε να το επαναλάβετε;",
        "english": "could you perhaps repeat that?",
        "notes": "High-yield polite repair formula when audio or examiner is misunderstood.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "particle": "μήπως (polite tentative question)",
            "verb": "επαναλαμβάνω -> να επαναλάβετε (aorist subjunctive)"
        },
        "keg_communicative_function": "Asking an interlocutor to repeat a phrase or question",
        "example_el": "Με συγχωρείτε, είχε θόρυβο στην αίθουσα, μήπως μπορείτε να το επαναλάβετε;",
        "example_en": "Excuse me, there was noise in the room, could you perhaps repeat that?",
        "example2_el": "Δεν άκουσα το όνομα του δρόμου, μήπως μπορείτε να το επαναλάβετε;",
        "example2_en": "I didn't hear the name of the street, could you perhaps repeat that?"
    },
    {
        "id": "A2P2-U01-004",
        "greek": "μιλάτε λίγο πιο αργά, παρακαλώ;",
        "english": "could you speak a little slower, please?",
        "notes": "Crucial speaking management strategy for A2 candidates during examination dialogue.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "comparative_adverb": "πιο αργά",
            "politeness_marker": "παρακαλώ"
        },
        "keg_communicative_function": "Regulating the speech rate of an interlocutor",
        "example_el": "Μιλάτε λίγο πιο αργά, παρακαλώ, γιατί ακόμα μαθαίνω ελληνικά.",
        "example_en": "Could you speak a little slower, please, because I am still learning Greek.",
        "example2_el": "Αν θέλετε, μιλάτε λίγο πιο αργά για να καταγράψω τις διευθύνσεις;",
        "example2_en": "If you would, could you speak a little slower so I can note down the addresses?"
    },
    {
        "id": "A2P2-U01-005",
        "greek": "έχετε απόλυτο δίκιο",
        "english": "you are absolutely right",
        "notes": "Expressing emphatic agreement in Speaking Stage 3 (pair conversation).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "idiom": "έχω δίκιο (to be right)",
            "adjective": "απόλυτο (neuter accusative)"
        },
        "keg_communicative_function": "Expressing strong agreement with a conversation partner",
        "example_el": "Έχετε απόλυτο δίκιο, τα μέσα μαζικής μεταφοράς είναι πολύ πιο οικονομικά.",
        "example_en": "You are absolutely right, public transit is much more economical.",
        "example2_el": "Σε αυτό το σημείο έχετε απόλυτο δίκιο, πρέπει να ξεκινήσουμε νωρίτερα.",
        "example2_en": "On this point you are absolutely right, we must start earlier."
    },
    {
        "id": "A2P2-U01-006",
        "greek": "δεν είμαι σίγουρος / σίγουρη",
        "english": "I am not sure",
        "notes": "Polite hedging formula indicating uncertainty or hesitation.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "copula": "είμαι",
            "gender_forms": "σίγουρος (masc) / σίγουρη (fem)"
        },
        "keg_communicative_function": "Indicating hesitation or lack of certainty in conversation",
        "example_el": "Δεν είμαι σίγουρος για την ώρα της αναχώρησης, ας κοιτάξουμε τον πίνακα.",
        "example_en": "I am not sure about the departure time, let us look at the board.",
        "example2_el": "Δεν είμαι σίγουρη αν το κατάστημα είναι ανοιχτό τα απογεύματα.",
        "example2_en": "I am not sure if the shop is open in the afternoons."
    },
    {
        "id": "A2P2-U01-007",
        "greek": "κατά τη γνώμη μου",
        "english": "in my opinion",
        "notes": "High-yield discourse marker for Speaking Stage 3 and Writing Task 2.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "prepositional phrase",
            "preposition": "κατά + accusative",
            "noun": "η γνώμη (opinion)"
        },
        "keg_communicative_function": "Introducing personal viewpoint or argumentative stance",
        "example_el": "Κατά τη γνώμη μου, η ζωή στην επαρχία προσφέρει περισσότερη ηρεμία.",
        "example_en": "In my opinion, life in the province offers more peace and quiet.",
        "example2_el": "Κατά τη γνώμη μου, αξίζει να επισκεφτούμε το καινούριο μουσείο της πόλης.",
        "example2_en": "In my opinion, it is well worth visiting the city's new museum."
    },
    {
        "id": "A2P2-U01-008",
        "greek": "από ό,τι ξέρω",
        "english": "as far as I know",
        "notes": "Expressing qualified knowledge or provisional information.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "pronoun": "ό,τι (relative with comma)",
            "verb": "ξέρω (present tense)"
        },
        "keg_communicative_function": "Sharing provisional information without absolute certainty",
        "example_el": "Από ό,τι ξέρω, η γραμματεία κλείνει στις δύο το μεσημέρι.",
        "example_en": "As far as I know, the administration office closes at two in the afternoon.",
        "example2_el": "Από ό,τι ξέρω, τα εισιτήρια του πλοίου είναι φθηνότερα τις καθημερινές.",
        "example2_en": "As far as I know, ferry tickets are cheaper on weekdays."
    },
    {
        "id": "A2P2-U01-009",
        "greek": "τι γνώμη έχετε για...;",
        "english": "what is your opinion about...?",
        "notes": "Inquiring about someone's opinion; standard prompt in pair dialogue.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "interrogative phrase",
            "preposition": "για + accusative",
            "register": "formal (έχετε) or plural"
        },
        "keg_communicative_function": "Asking an interlocutor for their perspective on an issue",
        "example_el": "Τι γνώμη έχετε για την εξ αποστάσεως εργασία από το σπίτι;",
        "example_en": "What is your opinion about working remotely from home?",
        "example2_el": "Τι γνώμη έχεις για το καινούριο εστιατόριο που άνοιξε στη γειτονιά;",
        "example2_en": "What do you think about the new restaurant that opened in the neighborhood?"
    },
    {
        "id": "A2P2-U01-010",
        "greek": "συμφωνώ απόλυτα μαζί σας",
        "english": "I completely agree with you",
        "notes": "Formal agreement formula used in conversational negotiation.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "συμφωνώ",
            "preposition": "μαζί + genitive clitic (μαζί σας / μαζί σου)"
        },
        "keg_communicative_function": "Affirming consensus with an interlocutor",
        "example_el": "Συμφωνώ απόλυτα μαζί σας, η προστασία του περιβάλλοντος αφορά όλους μας.",
        "example_en": "I completely agree with you, environmental protection concerns all of us.",
        "example2_el": "Συμφωνώ απόλυτα μαζί σου, αυτή η πρόταση είναι η καλύτερη λύση.",
        "example2_en": "I completely agree with you, this proposal is the best solution."
    },
    {
        "id": "A2P2-U01-011",
        "greek": "φοβάμαι πως διαφωνώ",
        "english": "I am afraid I disagree",
        "notes": "Diplomatic polite disagreement phrase avoiding blunt confrontation.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "φοβάμαι (mediopassive)",
            "conjunction": "πως / ότι"
        },
        "keg_communicative_function": "Expressing courteous disagreement in discussions",
        "example_el": "Φοβάμαι πως διαφωνώ με αυτή την επιλογή, καθώς έχει μεγάλο κόστος.",
        "example_en": "I am afraid I disagree with this option, as it carries a high cost.",
        "example2_el": "Σε αυτό το θέμα φοβάμαι πως διαφωνώ, πιστεύω ότι υπάρχει άλλος τρόπος.",
        "example2_en": "On this topic I am afraid I disagree, I believe there is another way."
    },
    {
        "id": "A2P2-U01-012",
        "greek": "δεν το κατάλαβα καλά",
        "english": "I did not understand it well",
        "notes": "Aorist of καταλαβαίνω with neutral object clitic. Fundamental repair phrase.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "tense": "simple past (αόριστος)",
            "verb": "κατάλαβα (καταλαβαίνω)"
        },
        "keg_communicative_function": "Signaling comprehension breakdown during conversation",
        "example_el": "Συγγνώμη, δεν το κατάλαβα καλά, μπορείτε να μου το εξηγήσετε ξανά;",
        "example_en": "Excuse me, I didn't understand it well, can you explain it to me again?",
        "example2_el": "Δεν το κατάλαβα καλά αυτό το σημείο του κειμένου.",
        "example2_en": "I didn't understand this point in the text very well."
    },
    {
        "id": "A2P2-U01-013",
        "greek": "θέλετε να πείτε ότι...;",
        "english": "do you mean to say that...?",
        "notes": "Checking understanding and summarizing interlocutor statements.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "interrogative phrase",
            "verbs": "θέλετε (present) + να πείτε (subjunctive of λέω)"
        },
        "keg_communicative_function": "Paraphrasing interlocutor input to verify comprehension",
        "example_el": "Θέλετε να πείτε ότι δεν υπάρχουν άλλα διαθέσιμα εισιτήρια για απόψε;",
        "example_en": "Do you mean to say that there are no other tickets available for tonight?",
        "example2_el": "Θέλεις να πεις ότι θα αλλάξουμε το πρόγραμμα της εκδρομής;",
        "example2_en": "Do you mean to say that we will change the excursion schedule?"
    },
    {
        "id": "A2P2-U01-014",
        "greek": "ποια είναι η άποψή σας;",
        "english": "what is your view / opinion?",
        "notes": "Synonym of 'τι γνώμη έχετε'. Key question for interactive oral tasks.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "interrogative phrase",
            "pronoun": "ποια (feminine nominative)",
            "noun": "η άποψη (view, opinion, 3rd declension feminine)"
        },
        "keg_communicative_function": "Inviting someone to express their standpoint",
        "example_el": "Ποια είναι η άποψή σας για τη χρήση των κινητών τηλεφώνων στο σχολείο;",
        "example_en": "What is your view on the use of mobile phones in schools?",
        "example2_el": "Ποια είναι η δική σου άποψη για τις καλοκαιρινές διακοπές;",
        "example2_en": "What is your own view regarding summer vacations?"
    },
    {
        "id": "A2P2-U01-015",
        "greek": "κλείνω ραντεβού",
        "english": "I make / book an appointment",
        "notes": "Collocation: κλείνω + ραντεβού. Standard A2 dialogue task with doctor/services.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "collocation",
            "verb": "κλείνω (aorist: έκλεισα)",
            "noun": "το ραντεβού (indeclinable neuter)"
        },
        "keg_communicative_function": "Scheduling medical, professional or personal appointments",
        "example_el": "Θέλω να κλείσω ένα ραντεβού με τον οδοντίατρο για την επόμενη Τρίτη.",
        "example_en": "I want to make an appointment with the dentist for next Tuesday.",
        "example2_el": "Έκλεισα ραντεβού στην τράπεζα για να ανοίξω έναν λογαριασμό.",
        "example2_en": "I booked an appointment at the bank to open an account."
    },
    {
        "id": "A2P2-U01-016",
        "greek": "αναβάλλω το ραντεβού",
        "english": "I postpone / reschedule the appointment",
        "notes": "Compound verb: ανα- + βάλλω. Common in email rescheduling requests (Writing Task 1).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "collocation",
            "verb": "αναβάλλω (aorist: ανέβαλα, future: θα αναβάλω)",
            "prefix": "ανά-"
        },
        "keg_communicative_function": "Requesting postponement of scheduled commitments",
        "example_el": "Δυστυχώς προέκυψε κάτι έκτακτο και πρέπει να αναβάλω το ραντεβού μας.",
        "example_en": "Unfortunately an emergency arose and I must postpone our appointment.",
        "example2_el": "Ανέβαλαν τη συνάντηση εργασίας για την επόμενη εβδομάδα.",
        "example2_en": "They postponed the work meeting for next week."
    },
    {
        "id": "A2P2-U01-017",
        "greek": "ακυρώνω τη συνάντηση",
        "english": "I cancel the meeting",
        "notes": "Regular -ώνω verb. Essential in cancellation notices and phone calls.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "collocation",
            "verb": "ακυρώνω (aorist: ακύρωσα)",
            "noun": "η συνάντηση"
        },
        "keg_communicative_function": "Notifying interlocutor of cancellation",
        "example_el": "Σας γράφω για να ακυρώσω τη συνάντησή μας, επειδή είμαι άρρωστος.",
        "example_en": "I am writing to cancel our meeting because I am sick.",
        "example2_el": "Ακύρωσαν την πτήση λόγω της κακοκαιρίας.",
        "example2_en": "They cancelled the flight due to bad weather."
    },
    {
        "id": "A2P2-U01-018",
        "greek": "σας τηλεφωνώ σχετικά με...",
        "english": "I am calling you regarding...",
        "notes": "Standard telephone opening phrase for inquiries and booking.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "τηλεφωνώ (-είς, -εί)",
            "preposition": "σχετικά με + accusative"
        },
        "keg_communicative_function": "Stating the purpose of a telephone call",
        "example_el": "Γεια σας, σας τηλεφωνώ σχετικά με την αγγελία για το διαμέρισμα.",
        "example_en": "Hello, I am calling you regarding the advertisement for the apartment.",
        "example2_el": "Σας τηλεφωνώ σχετικά με την αίτηση εργασίας που έστειλα χθες.",
        "example2_en": "I am calling you regarding the job application I sent yesterday."
    },
    {
        "id": "A2P2-U01-019",
        "greek": "ποιος είναι στο τηλέφωνο;",
        "english": "who is on the phone? / who is calling?",
        "notes": "Common telephone phrase for identifying the caller.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "interrogative phrase",
            "pronoun": "ποιος (nominative masculine)"
        },
        "keg_communicative_function": "Inquiring about caller identity",
        "example_el": "Παρακαλώ, ποιος είναι στο τηλέφωνο; Δεν άκουσα καλά το όνομά σας.",
        "example_en": "Excuse me, who is on the phone? I did not hear your name clearly.",
        "example2_el": "Ποιος είναι στο τηλέφωνο τέτοια ώρα;",
        "example2_en": "Who is on the phone at this hour?"
    },
    {
        "id": "A2P2-U01-020",
        "greek": "αφήνω μήνυμα",
        "english": "I leave a message",
        "notes": "Telephone scenario: leaving a voice message or voicemail.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "collocation",
            "verb": "αφήνω (aorist: άφησα, subjunctive: να αφήσω)",
            "noun": "το μήνυμα"
        },
        "keg_communicative_function": "Leaving voice or written messages for third parties",
        "example_el": "Αν ο κύριος Παπαδόπουλος λείπει, μπορώ να αφήσω ένα μήνυμα;",
        "example_en": "If Mr. Papadopoulos is away, can I leave a message?",
        "example2_el": "Άφησα μήνυμα στον τηλεφωνητή αλλά δεν μου απάντησε ακόμα.",
        "example2_en": "I left a message on the answering machine but he hasn't answered yet."
    },
    {
        "id": "A2P2-U01-021",
        "greek": "θα σας καλέσω αργότερα",
        "english": "I will call you later",
        "notes": "Polite telephone closure when unable to speak immediately.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "tense": "simple future (συνοπτικός μέλλοντας)",
            "verb": "καλώ -> θα καλέσω"
        },
        "keg_communicative_function": "Promising a return phone call",
        "example_el": "Τώρα βρίσκομαι σε σύσκεψη, θα σας καλέσω αργότερα.",
        "example_en": "Right now I am in a meeting, I will call you later.",
        "example2_el": "Μην ανησυχείς, θα σε καλέσω μόλις φτάσω στο σπίτι.",
        "example2_en": "Don't worry, I will call you as soon as I arrive home."
    },
    {
        "id": "A2P2-U01-022",
        "greek": "μου επιτρέπετε να προσθέσω κάτι;",
        "english": "allow me to add something? / may I add something?",
        "notes": "Courteous turn-taking intervention during discussions.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "επιτρέπω (present) + προσθέτω -> να προσθέσω (subjunctive)"
        },
        "keg_communicative_function": "Intervening politely in an ongoing discussion",
        "example_el": "Μου επιτρέπετε να προσθέσω κάτι σχετικά με το κόστος του έργου;",
        "example_en": "May I add something regarding the cost of the project?",
        "example2_el": "Αν μου επιτρέπετε, θα ήθελα να προσθέσω μια σημαντική λεπτομέρεια.",
        "example2_en": "If you allow me, I would like to add an important detail."
    },
    {
        "id": "A2P2-U01-023",
        "greek": "ας αλλάξουμε θέμα",
        "english": "let us change the topic",
        "notes": "Hortative particle 'ας' + aorist subjunctive. Topic shift marker.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "particle": "ας (hortative)",
            "verb": "αλλάζω -> αλλάξουμε (1st person plural subjunctive)"
        },
        "keg_communicative_function": "Directing conversation toward a new topic",
        "example_el": "Μιλήσαμε αρκετά για τη δουλειά, ας αλλάξουμε θέμα τώρα.",
        "example_en": "We talked enough about work, let's change the topic now.",
        "example2_el": "Ας αλλάξουμε θέμα και ας σχεδιάσουμε τις διακοπές μας.",
        "example2_en": "Let's change the topic and plan our vacations."
    },
    {
        "id": "A2P2-U01-024",
        "greek": "τι προτείνετε να κάνουμε;",
        "english": "what do you suggest we do?",
        "notes": "Soliciting proposals and joint planning in Speaking Stage 3.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "interrogative phrase",
            "verbs": "προτείνετε (present) + να κάνουμε (subjunctive)"
        },
        "keg_communicative_function": "Asking for suggestions in collaborative decision making",
        "example_el": "Ο καιρός αύριο θα είναι βροχερός, τι προτείνετε να κάνουμε;",
        "example_en": "The weather tomorrow will be rainy, what do you suggest we do?",
        "example2_el": "Τι προτείνεις να κάνουμε για τα γενέθλια της Ελένης;",
        "example2_en": "What do you suggest we do for Eleni's birthday?"
    },
    {
        "id": "A2P2-U01-025",
        "greek": "μου φαίνεται καλή ιδέα",
        "english": "it seems like a good idea to me",
        "notes": "Accepting a proposal enthusiastically.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "φαίνομαι (impersonal mediopassive) + weak clitic μου",
            "noun": "η ιδέα (feminine nominative)"
        },
        "keg_communicative_function": "Endorsing a suggestion made by a partner",
        "example_el": "Να πάμε για φαγητό στην ταβέρνα δίπλα στο λιμάνι; Μου φαίνεται καλή ιδέα!",
        "example_en": "Shall we go eat at the tavern by the harbor? It seems like a good idea to me!",
        "example2_el": "Το να ταξιδέψουμε με το τρένο μου φαίνεται εξαιρετική ιδέα.",
        "example2_en": "Traveling by train seems like an excellent idea to me."
    },
    {
        "id": "A2P2-U01-026",
        "greek": "δυστυχώς δεν μπορώ",
        "english": "unfortunately I cannot",
        "notes": "Polite declination of invitation or request.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "adverb": "δυστυχώς",
            "verb": "δεν μπορώ (negative modal)"
        },
        "keg_communicative_function": "Declining an invitation or offer with regret",
        "example_el": "Σας ευχαριστώ για την πρόσκληση, αλλά δυστυχώς δεν μπορώ να έρθω απόψε.",
        "example_en": "Thank you for the invitation, but unfortunately I cannot come tonight.",
        "example2_el": "Δυστυχώς δεν μπορώ να σε βοηθήσω το πρωί, γιατί έχω μάθημα.",
        "example2_en": "Unfortunately I cannot help you in the morning because I have class."
    },
    {
        "id": "A2P2-U01-027",
        "greek": "σας ευχαριστώ για τον χρόνο σας",
        "english": "thank you for your time",
        "notes": "Formal closing courtesy for interviews and professional emails.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "register": "formal",
            "preposition": "για + accusative 'τον χρόνο σας'"
        },
        "keg_communicative_function": "Expressing gratitude at the conclusion of an encounter",
        "example_el": "Σας ευχαριστώ πολύ για τον χρόνο σας και τις πολύτιμες πληροφορίες.",
        "example_en": "Thank you very much for your time and the valuable information.",
        "example2_el": "Σας ευχαριστώ για τον χρόνο σας, περιμένω νέα σας σύντομα.",
        "example2_en": "Thank you for your time, I look forward to hearing from you soon."
    },
    {
        "id": "A2P2-U01-028",
        "greek": "μη στενοχωριέστε, δεν πειράζει",
        "english": "don't worry, it doesn't matter",
        "notes": "Reassuring formula minimizing inconveniences.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "negative_imperative": "μη στενοχωριέστε (deponent present)",
            "impersonal_verb": "δεν πειράζει"
        },
        "keg_communicative_function": "Reassuring an interlocutor when an apology is made",
        "example_el": "Αργήσατε λίγο αλλά μη στενοχωριέστε, δεν πειράζει καθόλου.",
        "example_en": "You were a little late, but don't worry, it doesn't matter at all.",
        "example2_el": "Έχασες το λεωφορείο; Μη στενοχωριέσαι, έρχεται άλλο σε πέντε λεπτά.",
        "example2_en": "Did you miss the bus? Don't worry, another one comes in five minutes."
    },
    {
        "id": "A2P2-U01-029",
        "greek": "ευχαρίστως να βοηθήσω",
        "english": "I'd be glad to help / with pleasure",
        "notes": "Willingness formula in collaborative tasks.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "adverb": "ευχαρίστως (with pleasure)",
            "verb": "να βοηθήσω (subjunctive of βοηθάω)"
        },
        "keg_communicative_function": "Offering or agreeing to render assistance readily",
        "example_el": "Αν χρειάζεστε οδηγίες για το κέντρο, ευχαρίστως να βοηθήσω.",
        "example_en": "If you need directions to the center, I'd be glad to help.",
        "example2_el": "Ευχαρίστως να σε βοηθήσω με τη μετακόμιση το Σάββατο.",
        "example2_en": "I'd be glad to help you with moving on Saturday."
    },
    {
        "id": "A2P2-U01-030",
        "greek": "τα λέμε σύντομα",
        "english": "talk to you soon / see you soon",
        "notes": "Very common informal conversational and written valediction.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "λέμε (mediopassive reciprocal sense: we talk / see each other)",
            "adverb": "σύντομα"
        },
        "keg_communicative_function": "Informal parting phrase in spoken or written messages",
        "example_el": "Χάρηκα πολύ που σε είδα, τα λέμε σύντομα για καφέ!",
        "example_en": "So glad to see you, talk to you soon for coffee!",
        "example2_el": "Πρέπει να φύγω τώρα, καλή συνέχεια και τα λέμε σύντομα.",
        "example2_en": "I have to leave now, have a good rest of the day and see you soon."
    }
]

# -------------------------------------------------------------
# UNIT A2P2-02 CARDS (30 cards)
# Theme: Προσωπική Ταυτότητα, Οικογένεια & Κοινωνικό Περιβάλλον
# -------------------------------------------------------------
CARDS_U02 = [
    {
        "id": "A2P2-U02-001",
        "greek": "ο συγγενής / οι συγγενείς",
        "english": "relative / relatives",
        "notes": "Third-declension masculine adjective/noun in -ης, -εις. Essential for family topics.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "masculine",
            "nominative_singular": "ο συγγενής",
            "genitive_singular": "του συγγενούς",
            "nominative_plural": "οι συγγενείς",
            "genitive_plural": "των συγγενών"
        },
        "keg_communicative_function": "Talking about extended family and kinship relations",
        "example_el": "Όλοι οι στενοί συγγενείς συγκεντρώθηκαν για το πασχαλινό τραπέζι.",
        "example_en": "All the close relatives gathered for the Easter table.",
        "example2_el": "Έχω πολλούς συγγενείς που ζουν στη Θεσσαλονίκη και στην Κρήτη.",
        "example2_en": "I have many relatives living in Thessaloniki and Crete."
    },
    {
        "id": "A2P2-U02-002",
        "greek": "ο ανιψιός / η ανιψιά",
        "english": "nephew / niece",
        "notes": "Kinship terms. Common in personal biography descriptions.",
        "gender_or_pos": "noun (masculine / feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "masculine": "ο ανιψιός (gen: του ανιψιού)",
            "feminine": "η ανιψιά (gen: της ανιψιάς)",
            "neuter_diminutive": "το ανίψι"
        },
        "keg_communicative_function": "Describing family members and generational relations",
        "example_el": "Ο ανιψιός μου ξεκίνησε φέτος το δημοτικό σχολείο.",
        "example_en": "My nephew started elementary school this year.",
        "example2_el": "Η ανιψιά μου σπουδάζει αρχιτεκτονική στην Πάτρα.",
        "example2_en": "My niece studies architecture in Patras."
    },
    {
        "id": "A2P2-U02-003",
        "greek": "ο πεθερός / η πεθερά",
        "english": "father-in-law / mother-in-law",
        "notes": "In-law kinship terms. Collective neuter: τα πεθερικά.",
        "gender_or_pos": "noun (masculine / feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "masculine": "ο πεθερός",
            "feminine": "η πεθερά",
            "collective_plural": "τα πεθερικά (the in-laws)"
        },
        "keg_communicative_function": "Discussing marital relations and extended family gatherings",
        "example_el": "Την Κυριακή θα επισκεφτούμε τα πεθερικά μου στο χωριό.",
        "example_en": "On Sunday we will visit my in-laws in the village.",
        "example2_el": "Η πεθερά μου μαγειρεύει την καλύτερη παραδοσιακή σπανακόπιτα.",
        "example2_en": "My mother-in-law cooks the best traditional spinach pie."
    },
    {
        "id": "A2P2-U02-004",
        "greek": "ο γαμπρός / η νύφη",
        "english": "son-in-law / groom, daughter-in-law / bride",
        "notes": "Dual meanings: wedding couple and in-law relations.",
        "gender_or_pos": "noun (masculine / feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "masculine": "ο γαμπρός (groom / son-in-law)",
            "feminine": "η νύφη (bride / daughter-in-law)"
        },
        "keg_communicative_function": "Talking about weddings, marriage, and family ties",
        "example_el": "Ο γαμπρός και η νύφη υποδέχτηκαν τους καλεσμένους στη δεξίωση.",
        "example_en": "The groom and bride welcomed the guests at the reception.",
        "example2_el": "Ο γαμπρός τους είναι γιατρός και δουλεύει στο πανεπιστημιακό νοσοκομείο.",
        "example2_en": "Their son-in-law is a doctor and works at the university hospital."
    },
    {
        "id": "A2P2-U02-005",
        "greek": "το μοναχοπαίδι",
        "english": "only child",
        "notes": "Compound noun: μόνος + παιδί. Plural: τα μοναχοπαίδια.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "neuter",
            "genitive_singular": "του μοναχοπαιδιού",
            "nominative_plural": "τα μοναχοπαίδια"
        },
        "keg_communicative_function": "Describing family structure and personal upbringing",
        "example_el": "Είμαι μοναχοπαίδι και δεν έχω αδέρφια, αλλά έχω πολλά ξαδέρφια.",
        "example_en": "I am an only child and have no siblings, but I have many cousins.",
        "example2_el": "Το μοναχοπαίδι της οικογένειας πήρε όλη την προσοχή των γονιών του.",
        "example2_en": "The family's only child received all of their parents' attention."
    },
    {
        "id": "A2P2-U02-006",
        "greek": "ο χαρακτήρας",
        "english": "character / personality",
        "notes": "Third-declension masculine noun in -ας, -ες. Genitive: του χαρακτήρα.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "masculine",
            "genitive": "του χαρακτήρα",
            "plural": "οι χαρακτήρες"
        },
        "keg_communicative_function": "Discussing personal qualities and temperaments",
        "example_el": "Έχει πολύ δυναμικό χαρακτήρα και παίρνει πάντα πρωτοβουλίες στη δουλειά.",
        "example_en": "She has a very dynamic character and always takes initiative at work.",
        "example2_el": "Παρά τις διαφορές στον χαρακτήρα τους, είναι οι καλύτεροι φίλοι.",
        "example2_en": "Despite differences in character, they are the best of friends."
    },
    {
        "id": "A2P2-U02-007",
        "greek": "κοινωνικός, -ή, -ό",
        "english": "sociable / outgoing",
        "notes": "Standard adjective in -ος, -η, -ο. Frequently used in personal description.",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine": "κοινωνικός",
            "feminine": "κοινωνική",
            "neuter": "κοινωνικό"
        },
        "keg_communicative_function": "Describing someone's social nature and interpersonal traits",
        "example_el": "Ο Νίκος είναι πολύ κοινωνικός άνθρωπος και κάνει εύκολα νέους φίλους.",
        "example_en": "Nikos is a very sociable person and makes new friends easily.",
        "example2_el": "Χρειαζόμαστε έναν κοινωνικό υπάλληλο για το τμήμα εξυπηρέτησης πελατών.",
        "example2_en": "We need a sociable employee for the customer service department."
    },
    {
        "id": "A2P2-U02-008",
        "greek": "εσωστρεφής, -ής, -ές",
        "english": "introverted / reserved",
        "notes": "Two-termination adjective in -ης (masc/fem), -ες (neuter).",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine_feminine": "εσωστρεφής",
            "neuter": "εσωστρεφές",
            "plural": "οι εσωστρεφείς / τα εσωστρεφή"
        },
        "keg_communicative_function": "Characterizing reserved or quiet personality types",
        "example_el": "Είναι λίγο εσωστρεφής και προτιμάει να διαβάζει μόνη της στο σπίτι.",
        "example_en": "She is a bit introverted and prefers reading by herself at home.",
        "example2_el": "Οι εσωστρεφείς άνθρωποι συχνά σκέφτονται πολύ πριν μιλήσουν.",
        "example2_en": "Introverted people often think carefully before speaking."
    },
    {
        "id": "A2P2-U02-009",
        "greek": "υπομονετικός, -ή, -ό",
        "english": "patient",
        "notes": "Derived from η υπομονή (patience). Opposite: ανυπόμονος.",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine": "υπομονετικός",
            "feminine": "υπομονετική",
            "neuter": "υπομονετικό",
            "adverb": "υπομονετικά"
        },
        "keg_communicative_function": "Commending patience in relationships or professional settings",
        "example_el": "Ο δάσκαλος είναι πολύ υπομονετικός με τα μικρά παιδιά.",
        "example_en": "The teacher is very patient with young children.",
        "example2_el": "Πρέπει να είμαστε υπομονετικοί όταν μαθαίνουμε μια ξένη γλώσσα.",
        "example2_en": "We must be patient when learning a foreign language."
    },
    {
        "id": "A2P2-U02-010",
        "greek": "ανυπόμονος, -η, -ο",
        "english": "impatient",
        "notes": "Negative prefix αν- + υπομονή. Stress moves to antepenult.",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine": "ανυπόμονος",
            "feminine": "ανυπόμονη",
            "neuter": "ανυπόμονο"
        },
        "keg_communicative_function": "Expressing impatience or eager anticipation",
        "example_el": "Είμαι ανυπόμονος να δω τα αποτελέσματα των εξετάσεων.",
        "example_en": "I am impatient to see the exam results.",
        "example2_el": "Μην είσαι τόσο ανυπόμονη, το λεωφορείο θα φτάσει σε λίγα λεπτά.",
        "example2_en": "Don't be so impatient, the bus will arrive in a few minutes."
    },
    {
        "id": "A2P2-U02-011",
        "greek": "ειλικρινής, -ής, -ές",
        "english": "honest / sincere",
        "notes": "High-register two-ending adjective in -ης, -ες. Noun: η ειλικρίνεια.",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine_feminine": "ειλικρινής",
            "neuter": "ειλικρινές",
            "adverb": "ειλικρινά (honestly)"
        },
        "keg_communicative_function": "Describing truthfulness and sincerity in friendship",
        "example_el": "Εκτιμώ πολύ τους ειλικρινείς φίλους που μου λένε πάντα την αλήθεια.",
        "example_en": "I really appreciate honest friends who always tell me the truth.",
        "example2_el": "Για να είμαι ειλικρινής μαζί σας, αυτή η λύση δεν μου αρέσει πολύ.",
        "example2_en": "To be honest with you, I don't really like this solution."
    },
    {
        "id": "A2P2-U02-012",
        "greek": "γενναιόδωρος, -η, -ο",
        "english": "generous",
        "notes": "Adjective describing kindness with money or time. Noun: η γενναιοδωρία.",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine": "γενναιόδωρος",
            "feminine": "γενναιόδωρη",
            "neuter": "γενναιόδωρο"
        },
        "keg_communicative_function": "Praising generosity in friends and family members",
        "example_el": "Ο παππούς ήταν πάντα γενναιόδωρος και μας έφερνε δώρα από τα ταξίδια του.",
        "example_en": "Grandfather was always generous and brought us gifts from his travels.",
        "example2_el": "Έκαναν μια πολύ γενναιόδωρη δωρεά στο τοπικό νοσοκομείο.",
        "example2_en": "They made a very generous donation to the local hospital."
    },
    {
        "id": "A2P2-U02-013",
        "greek": "πεισματάρης, -α, -ικο",
        "english": "stubborn / obstinate",
        "notes": "Colloquial descriptive adjective in -ης, -α, -ικο. From το πείσμα.",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine": "πεισματάρης",
            "feminine": "πεισματάρα",
            "neuter": "πεισματάρικο"
        },
        "keg_communicative_function": "Describing stubborn or determined personality traits",
        "example_el": "Είναι τόσο πεισματάρης που δεν αλλάζει γνώμη με τίποτα.",
        "example_en": "He is so stubborn that he doesn't change his mind for anything.",
        "example2_el": "Το μικρό παιδί ήταν πεισματάρικο και δεν ήθελε να φάει το φαγητό του.",
        "example2_en": "The toddler was stubborn and didn't want to eat his food."
    },
    {
        "id": "A2P2-U02-014",
        "greek": "ευγενικός, -ή, -ό",
        "english": "polite / courteous / kind",
        "notes": "Crucial civic trait. Adverb: ευγενικά (politely).",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine": "ευγενικός",
            "feminine": "ευγενική",
            "neuter": "ευγενικό",
            "noun": "η ευγένεια"
        },
        "keg_communicative_function": "Evaluating customer service and interpersonal encounters",
        "example_el": "Η υπάλληλος στο ταχυδρομείο ήταν εξαιρετικά ευγενική και εξυπηρετική.",
        "example_en": "The clerk at the post office was exceptionally polite and helpful.",
        "example2_el": "Είναι σημαντικό να μιλάμε ευγενικά στους μεγαλύτερους ανθρώπους.",
        "example2_en": "It is important to speak politely to older people."
    },
    {
        "id": "A2P2-U02-015",
        "greek": "αγενής, -ής, -ές",
        "english": "rude / impolite",
        "notes": "Negative of ευγενής. Two-termination adjective in -ης, -ες.",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine_feminine": "αγενής",
            "neuter": "αγενές",
            "noun": "η αγένεια"
        },
        "keg_communicative_function": "Reporting impolite behavior or complaints",
        "example_el": "Δεν μου άρεσε ο τρόπος του οδηγού, ήταν πολύ αγενής με τους επιβάτες.",
        "example_en": "I did not like the driver's manner, he was very rude to the passengers.",
        "example2_el": "Η αγενής συμπεριφορά δεν γίνεται αποδεκτή στον χώρο εργασίας.",
        "example2_en": "Rude behavior is not accepted in the workplace."
    },
    {
        "id": "A2P2-U02-016",
        "greek": "συμπαθητικός, -ή, -ό",
        "english": "likeable / pleasant / charming",
        "notes": "False friend with English sympathetic; means likeable/friendly.",
        "gender_or_pos": "adjective",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "masculine": "συμπαθητικός",
            "feminine": "συμπαθητική",
            "neuter": "συμπαθητικό",
            "noun": "η συμπάθεια"
        },
        "keg_communicative_function": "Expressing favorable impressions about people",
        "example_el": "Οι νέοι μας γείτονες είναι πολύ συμπαθητικοί και ήσυχοι άνθρωποι.",
        "example_en": "Our new neighbors are very likeable and quiet people.",
        "example2_el": "Μου έκανε πολύ συμπαθητική εντύπωση από την πρώτη στιγμή.",
        "example2_en": "She made a very likeable impression on me from the first moment."
    },
    {
        "id": "A2P2-U02-017",
        "greek": "τα πάω καλά με...",
        "english": "I get along well with...",
        "notes": "High-frequency Greek idiom for interpersonal compatibility.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "idiomatic phrase",
            "verb": "πηγαίνω / πάω (3rd neuter plural 'τα πάω')",
            "preposition": "με + accusative"
        },
        "keg_communicative_function": "Describing harmonious relationships with colleagues or family",
        "example_el": "Τα πάω πολύ καλά με τους συναδέλφους μου στο γραφείο.",
        "example_en": "I get along very well with my colleagues at the office.",
        "example2_el": "Πώς τα πας με τον καινούριο σου συγκάτοικο;",
        "example2_en": "How are you getting along with your new roommate?"
    },
    {
        "id": "A2P2-U02-018",
        "greek": "μαλώνω με...",
        "english": "I quarrel / argue with...",
        "notes": "Regular -ώνω verb. Aorist: μάλωσα. Governs με + accusative.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "present": "μαλώνω",
            "aorist": "μάλωσα",
            "subjunctive": "να μαλώσω"
        },
        "keg_communicative_function": "Describing domestic arguments or sibling quarrels",
        "example_el": "Όταν ήμασταν μικροί, μαλώναμε συχνά με τον αδερφό μου για τα παιχνίδια.",
        "example_en": "When we were little, my brother and I often quarreled over toys.",
        "example2_el": "Μάλωσαν χθες για ασήμαντη αφορμή αλλά σήμερα μιλάνε κανονικά.",
        "example2_en": "They argued yesterday over a trivial excuse, but today they are talking normally."
    },
    {
        "id": "A2P2-U02-019",
        "greek": "συμφιλιώνομαι",
        "english": "I reconcile / make up (with someone)",
        "notes": "Mediopassive verb. Aorist: συμφιλιώθηκα. Noun: η συμφιλίωση.",
        "gender_or_pos": "verb (mediopassive)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "voice": "mediopassive",
            "present": "συμφιλιώνομαι",
            "aorist": "συμφιλιώθηκα"
        },
        "keg_communicative_function": "Narrating reconciliation after a disagreement",
        "example_el": "Μετά από μια μακρά συζήτηση, οι δύο φίλοι συμφιλιώθηκαν.",
        "example_en": "After a long discussion, the two friends reconciled.",
        "example2_el": "Είναι καλύτερα να συμφιλιωθούμε παρά να κρατάμε κακία.",
        "example2_en": "It is better for us to reconcile rather than hold a grudge."
    },
    {
        "id": "A2P2-U02-020",
        "greek": "εμπιστεύομαι",
        "english": "I trust / rely on",
        "notes": "Deponent verb. Aorist: εμπιστεύτηκα. Noun: η εμπιστοσύνη.",
        "gender_or_pos": "verb (deponent)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "voice": "mediopassive / deponent",
            "present": "εμπιστεύομαι",
            "aorist": "εμπιστεύτηκα"
        },
        "keg_communicative_function": "Expressing trust and reliance in interpersonal relations",
        "example_el": "Εμπιστεύομαι την καλύτερή μου φίλη γιατί δεν λέει ποτέ τα μυστικά μου.",
        "example_en": "I trust my best friend because she never tells my secrets.",
        "example2_el": "Χρειάζεται χρόνος για να εμπιστευτείς έναν άγνωστο άνθρωπο.",
        "example2_en": "It takes time to trust a person you don't know."
    },
    {
        "id": "A2P2-U02-021",
        "greek": "η παιδική ηλικία",
        "english": "childhood",
        "notes": "Collocation: παιδικός (adjective) + ηλικία (age). Key for Speaking Stage 1.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "collocation",
            "noun": "η ηλικία (feminine)",
            "adjective": "παιδική"
        },
        "keg_communicative_function": "Recounting childhood years and early life memories",
        "example_el": "Πέρασα την παιδική μου ηλικία σε ένα παραθαλάσσιο χωριό της Πελοποννήσου.",
        "example_en": "I spent my childhood in a coastal village of the Peloponnese.",
        "example2_el": "Έχω πολύ όμορφες αναμνήσεις από την παιδική μου ηλικία.",
        "example2_en": "I have very beautiful memories from my childhood."
    },
    {
        "id": "A2P2-U02-022",
        "greek": "η εφηβεία",
        "english": "adolescence / teenage years",
        "notes": "Feminine noun in -εια. Adjective: ο έφηβος / η έφηβη (teenager).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της εφηβείας"
        },
        "keg_communicative_function": "Discussing the challenges and experiences of teenage life",
        "example_el": "Η εφηβεία είναι μια περίοδος γεμάτη αλλαγές και καινούρια όνειρα.",
        "example_en": "Adolescence is a period full of changes and new dreams.",
        "example2_el": "Στην εφηβεία άρχισα να ενδιαφέρομαι για τη μουσική και τη φωτογραφία.",
        "example2_en": "In adolescence I began to be interested in music and photography."
    },
    {
        "id": "A2P2-U02-023",
        "greek": "η ενηλικίωση",
        "english": "adulthood / coming of age",
        "notes": "Derived from ο ενήλικας (adult). Third-declension feminine in -ση, -σεως/-σης.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της ενηλικίωσης"
        },
        "keg_communicative_function": "Discussing legal age, responsibilities, and adult independence",
        "example_el": "Με την ενηλικίωση στα δεκαοκτώ, οι νέοι αποκτούν δικαίωμα ψήφου.",
        "example_en": "With coming of age at eighteen, young people acquire the right to vote.",
        "example2_el": "Η ενηλικίωση φέρνει μαζί της πολλές ευθύνες αλλά και ανεξαρτησία.",
        "example2_en": "Adulthood brings along many responsibilities as well as independence."
    },
    {
        "id": "A2P2-U02-024",
        "greek": "η σχέση",
        "english": "relationship / connection",
        "notes": "Third-declension feminine noun. Plural: οι σχέσεις, των σχέσεων.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive_singular": "της σχέσης",
            "nominative_plural": "οι σχέσεις",
            "genitive_plural": "των σχέσεων"
        },
        "keg_communicative_function": "Discussing personal or professional relationships",
        "example_el": "Έχουν μια πολύ στενή σχέση βασισμένη στην αμοιβαία κατανόηση.",
        "example_en": "They have a very close relationship based on mutual understanding.",
        "example2_el": "Ποιες είναι οι σχέσεις σας με τους κατοίκους της περιοχής;",
        "example2_en": "What are your relations with the local residents of the area?"
    },
    {
        "id": "A2P2-U02-025",
        "greek": "χωρίζω",
        "english": "I separate / break up / divide",
        "notes": "Regular -ίζω verb. Aorist: χώρισα. Used both for couples and divisions.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "present": "χωρίζω",
            "aorist": "χώρισα",
            "passive": "χωρίζομαι"
        },
        "keg_communicative_function": "Describing breakups or dividing items into portions",
        "example_el": "Μετά από πέντε χρόνια γάμου, αποφάσισαν να χωρίσουν φιλικά.",
        "example_en": "After five years of marriage, they decided to separate amicably.",
        "example2_el": "Χωρίσαμε τα έξοδα του ταξιδιού στα δύο.",
        "example2_en": "We divided the travel expenses in two."
    },
    {
        "id": "A2P2-U02-026",
        "greek": "συγκατοικώ",
        "english": "I live together / cohabit / share a flat",
        "notes": "Compound verb: συν- + κατοικώ. Present: -είς, -εί. Aorist: συγκατοίκησα.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "present": "συγκατοικώ (-είς, -εί)",
            "aorist": "συγκατοίκησα",
            "noun": "η συγκατοίκηση"
        },
        "keg_communicative_function": "Discussing shared housing arrangements with flatmates",
        "example_el": "Συγκατοικώ με δύο συμφοιτητές μου σε ένα διαμέρισμα κοντά στο πανεπιστήμιο.",
        "example_en": "I share a flat with two university classmates in an apartment near campus.",
        "example2_el": "Η συγκατοίκηση βοηθάει πολύ στη μείωση των μηνιαίων εξόδων.",
        "example2_en": "Flatsharing helps a lot in reducing monthly expenses."
    },
    {
        "id": "A2P2-U02-027",
        "greek": "ο/η συγκάτοικος",
        "english": "flatmate / roommate",
        "notes": "Common-gender noun: ο συγκάτοικος (masc), η συγκάτοικος (fem).",
        "gender_or_pos": "noun (masculine / feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "masculine": "ο συγκάτοικος",
            "feminine": "η συγκάτοικος",
            "plural": "οι συγκάτοικοι"
        },
        "keg_communicative_function": "Introducing or describing a roommate in daily life narratives",
        "example_el": "Ο συγκάτοικός μου μαγειρεύει υπέροχα και μοιραζόμαστε όλες τις δουλειές.",
        "example_en": "My roommate cooks wonderfully and we share all the chores.",
        "example2_el": "Ψάχνω για καινούρια συγκάτοικο για το δεύτερο υπνοδωμάτιο.",
        "example2_en": "I am looking for a new female flatmate for the second bedroom."
    },
    {
        "id": "A2P2-U02-028",
        "greek": "η παρέα",
        "english": "group of friends / company",
        "notes": "Quintessential Greek social concept. Noun feminine in -α.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "gender": "feminine",
            "genitive": "της παρέας",
            "plural": "οι παρέες"
        },
        "keg_communicative_function": "Talking about socializing with friendship circles",
        "example_el": "Κάθε Παρασκευή βράδυ βγαίνουμε έξω με την παρέα για φαγητό.",
        "example_en": "Every Friday evening we go out with our group of friends for dinner.",
        "example2_el": "Έχει πολύ καλή παρέα και περνάει ευχάριστα τον ελεύθερο χρόνο του.",
        "example2_en": "He has very good company and spends his free time pleasantly."
    },
    {
        "id": "A2P2-U02-029",
        "greek": "κρατάω επαφή",
        "english": "I keep in touch",
        "notes": "Collocation: κρατάω (κρατώ) + επαφή. Essential for writing friendly letters.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "collocation",
            "verb": "κρατάω / κρατώ (aorist: κράτησα)",
            "noun": "η επαφή (contact)"
        },
        "keg_communicative_function": "Promising or maintaining communication across distances",
        "example_el": "Παρόλο που μετακόμισε στο εξωτερικό, κρατάμε επαφή μέσω διαδικτύου.",
        "example_en": "Even though he moved abroad, we keep in touch via the internet.",
        "example2_el": "Ελπίζω να κρατήσουμε επαφή μετά το τέλος των μαθημάτων.",
        "example2_en": "I hope we keep in touch after the end of classes."
    },
    {
        "id": "A2P2-U02-030",
        "greek": "χάνω επαφή",
        "english": "I lose touch",
        "notes": "Antonym of κρατάω επαφή. Aorist: έχασα επαφή.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "collocation",
            "verb": "χάνω (aorist: έχασα)",
            "noun": "η επαφή"
        },
        "keg_communicative_function": "Explaining past estrangement or drifting apart from old friends",
        "example_el": "Δυστυχώς χάσαμε επαφή μετά το σχολείο αλλά ξαναβρεθήκαμε πρόσφατα.",
        "example_en": "Unfortunately we lost touch after school, but we met up again recently.",
        "example2_el": "Δεν θέλω να χάσουμε επαφή τώρα που αλλάζεις πόλη.",
        "example2_en": "I don't want us to lose touch now that you are changing cities."
    }
]

def synthesize_item(text: str, filename: str) -> bool:
    """Helper to synthesize a single audio string if missing."""
    p = AUDIO_DIR / filename
    if p.exists() and p.stat().st_size > 0:
        return False
    try:
        b = synthesize_greek_chirp(text)
        with open(p, "wb") as f_out:
            f_out.write(b)
        return True
    except Exception as e:
        print(f"  [ERROR] {filename} ('{text}'): {e}")
        return False

def process_unit(unit_id: str, lesson_id: str, title: str, description: str, lesson_notes: str, cards: list, order_code: str):
    print(f"\n>>> Processing {unit_id} ({order_code}) - {len(cards)} cards ...")
    unit_dir = CONTENT_DIR / unit_id
    unit_dir.mkdir(parents=True, exist_ok=True)
    yaml_file = unit_dir / f"{lesson_id}.yaml"
    
    tasks = []
    for c in cards:
        # Greek headword
        fn_greek = generate_audio_filename(c["greek"])
        c["audio"] = fn_greek
        c["status"] = "verified"
        tasks.append((c["greek"], fn_greek))
        
        # Ex 1
        fn_ex1 = generate_audio_filename(c["example_el"])
        c["example_audio"] = fn_ex1
        tasks.append((c["example_el"], fn_ex1))
        
        # Ex 2
        fn_ex2 = generate_audio_filename(c["example2_el"])
        c["example2_audio"] = fn_ex2
        tasks.append((c["example2_el"], fn_ex2))

    print(f"  Synthesizing audio for {len(tasks)} items using ThreadPoolExecutor(max_workers=8)...")
    synthesized_count = 0
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(synthesize_item, text, fn): fn for text, fn in tasks}
        for future in as_completed(futures):
            if future.result():
                synthesized_count += 1

    print(f"  [TTS] Synthesized {synthesized_count} new audio files for {unit_id}.")
    
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
        
    print(f"  [YAML] Saved {yaml_file}")

def update_manifest(new_units: list):
    manifest_path = CONTENT_DIR / "manifest.yaml"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)
        
    units = manifest.get("units", [])
    existing_ids = {u["id"] for u in units}
    
    added = 0
    for entry in new_units:
        if entry["id"] not in existing_ids:
            units.append(entry)
            existing_ids.add(entry["id"])
            added += 1
            print(f"  [Manifest] Appended {entry['id']} ({entry['order']})")
        else:
            print(f"  [Manifest] {entry['id']} already exists, skipping")
            
    manifest["units"] = units
    with open(manifest_path, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"  [Manifest] Manifest updated ({added} new entries). Total: {len(units)} units.")

def main():
    print("==================================================")
    print("Generating KEG-A2 Part 2: Batch 1 (Units 01 & 02)")
    print("==================================================")
    
    u01_notes = """Unit A2P2-01 Core Notes: Καθημερινός Διάλογος & Προφορική Επικοινωνία (Everyday Dialogues & Conversational Exchanges)
• Official KEG A2 Exam Alignment:
  - Speaking Stage 1 & 2: Asking polite questions, requesting repetitions (Μήπως μπορείτε να το επαναλάβετε;), and conversational pacing.
  - Speaking Stage 3 (Pair Interaction): Agreeing/disagreeing diplomatically (Έχετε απόλυτο δίκιο vs. Φοβάμαι πως διαφωνώ), seeking partner's opinion (Ποια είναι η άποψή σας;), and making collaborative plans (Τι προτείνετε να κάνουμε;).
  - Listening & Telephone: Scheduling, postponing, and cancelling appointments (κλείνω / αναβάλλω / ακυρώνω ραντεβού)."""

    process_unit(
        unit_id="unit-a2p2-01",
        lesson_id="lesson-01",
        title="Μάθημα 1: Καθημερινός Διάλογος & Προφορική Επικοινωνία (Everyday Dialogues & Conversational Exchanges)",
        description="Mastering oral repair formulas, turn-taking strategies, polite agreements/disagreements, and telephone booking conversations for the KEG A2 Speaking and Listening sections.",
        lesson_notes=u01_notes,
        cards=CARDS_U01,
        order_code="KEG-A2-P2-01-A"
    )

    u02_notes = """Unit A2P2-02 Core Notes: Προσωπική Ταυτότητα & Κοινωνικό Περιβάλλον (Personal Identity, Family & Social Circle)
• Official KEG A2 Exam Alignment:
  - Speaking Stage 1 (Personal Interview): Describing extended family (συγγενείς, πεθερικά, ανίψια) and life stages (παιδική ηλικία, εφηβεία, ενηλικίωση).
  - Character Descriptions: Adjectives of personality (κοινωνικός, εσωστρεφής, υπομονετικός, ειλικρινής, πεισματάρης).
  - Writing Task 1 & 2: Social relationship idioms (τα πάω καλά με, κρατάω επαφή, συγκατοικώ με)."""

    process_unit(
        unit_id="unit-a2p2-02",
        lesson_id="lesson-01",
        title="Μάθημα 2: Προσωπική Ταυτότητα & Κοινωνικό Περιβάλλον (Personal Identity, Family & Social Circle)",
        description="Describing extended family structures, character traits, interpersonal relationships, and life stages for the personal interview (Speaking Stage 1) and narrative writing tasks.",
        lesson_notes=u02_notes,
        cards=CARDS_U02,
        order_code="KEG-A2-P2-02-A"
    )

    manifest_entries = [
        {
            "id": "unit-a2p2-01",
            "title": "Μάθημα 1: Καθημερινός Διάλογος & Προφορική Επικοινωνία (Everyday Dialogues & Conversational Exchanges)",
            "description": "Mastering oral repair formulas, turn-taking strategies, polite agreements/disagreements, and telephone booking conversations for the KEG A2 Speaking and Listening sections.",
            "order": "KEG-A2-P2-01-A",
            "total_lessons": 1,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2p2-01/lesson-01.yaml",
                    "title": "Μάθημα 1: Καθημερινός Διάλογος & Προφορική Επικοινωνία (Everyday Dialogues & Conversational Exchanges)"
                }
            ]
        },
        {
            "id": "unit-a2p2-02",
            "title": "Μάθημα 2: Προσωπική Ταυτότητα & Κοινωνικό Περιβάλλον (Personal Identity, Family & Social Circle)",
            "description": "Describing extended family structures, character traits, interpersonal relationships, and life stages for the personal interview (Speaking Stage 1) and narrative writing tasks.",
            "order": "KEG-A2-P2-02-A",
            "total_lessons": 1,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2p2-02/lesson-01.yaml",
                    "title": "Μάθημα 2: Προσωπική Ταυτότητα & Κοινωνικό Περιβάλλον (Personal Identity, Family & Social Circle)"
                }
            ]
        }
    ]

    update_manifest(manifest_entries)
    print("\n[OK] Batch 1 finished successfully!")

if __name__ == "__main__":
    main()

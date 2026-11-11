# -*- coding: utf-8 -*-
"""
Generate KEG-A2 Speaking Curriculum Batch 1:
- Unit SP-01: SP-01-A (40 cards) - Προσωπική Συνέντευξη & Ζέσταμα (Stage 1 Examiner Q&A Drills)
- Unit SP-02: SP-02-A (40 cards) - Συνδετικές Εκφράσεις & Διαχείριση Ροής (Conversational Connectors & Fluency Boosters)
Includes dual exam model responses and multi-threaded Google Cloud Chirp-3 HD TTS.
Note: Does NOT modify content/manifest.yaml (handled by parent agent after all batches complete).
"""
import sys
import time
import unicodedata
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


def nfc(text: str) -> str:
    return unicodedata.normalize("NFC", text.strip())


# -------------------------------------------------------------
# UNIT SP-01 CARDS (40 cards: SP-U01-001 .. SP-U01-040)
# Theme: Προσωπική Συνέντευξη & Ζέσταμα (Stage 1 Examiner Q&A Drills)
# -------------------------------------------------------------
CARDS_U01 = [
    # 001-008: Personal identity, origins, family background, and marital/social circle questions
    {
        "id": "SP-U01-001",
        "greek": "Πώς σας λένε και από πού είστε;",
        "english": "What is your name and where are you from? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Personal introduction, origin prepositions (από + accusative), present tense of είμαι and μένω"
        },
        "notes": "Examiner Objective: Warm-up check on basic self-introduction, nationality/origin, and current residence.\nStrategy: State full name, city/country of origin, and add how long you have lived in your current city.",
        "example_el": "Με λένε Μαρία Σμιθ και είμαι από το Λονδίνο της Αγγλίας, αλλά τα τελευταία τρία χρόνια μένω μόνιμα στην Αθήνα μαζί με τον σύζυγό μου.",
        "example_en": "My name is Maria Smith and I am from London, England, but for the last three years I have been living permanently in Athens with my husband.",
        "example2_el": "Ονομάζομαι Νίκος Μπράουν, κατάγομαι από τον Καναδά και ζω στη Θεσσαλονίκη εδώ και δύο χρόνια επειδή εργάζομαι σε μια ελληνική εταιρεία.",
        "example2_en": "My name is Nikos Brown, I come from Canada and I have been living in Thessaloniki for two years because I work at a Greek company.",
        "keg_communicative_function": "Introducing oneself, stating origin and current place of residence"
    },
    {
        "id": "SP-U01-002",
        "greek": "Σε ποια πόλη μένετε τώρα και πόσο καιρό ζείτε εκεί;",
        "english": "Which city do you live in now and how long have you been living there? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Duration expressions (εδώ και + accusative / τα τελευταία + time), locative prepositions (σε + accusative)"
        },
        "notes": "Examiner Objective: Tests ability to express duration of an ongoing state using Present Tense in Greek.\nStrategy: Never use English-style perfect tense here; use Present Tense + 'εδώ και' or 'τα τελευταία χρόνια'.",
        "example_el": "Τώρα μένω στη Λεμεσό της Κύπρου και ζω εκεί εδώ και τέσσερα χρόνια, γιατί μου αρέσει πολύ το ζεστό κλίμα και η θάλασσα.",
        "example_en": "Now I live in Limassol, Cyprus, and I have been living there for four years because I really like the warm climate and the sea.",
        "example2_el": "Αυτή την περίοδο μένω στο Ηράκλειο της Κρήτης τα τελευταία δύο χρόνια και είμαι πολύ ευχαριστημένος με την καθημερινότητά μου εκεί.",
        "example2_en": "During this period I have been living in Heraklion, Crete for the last two years and I am very pleased with my daily life there.",
        "keg_communicative_function": "Expressing place of residence and duration of stay using present tense time markers"
    },
    {
        "id": "SP-U01-003",
        "greek": "Πείτε μου λίγα λόγια για την οικογένειά σας.",
        "english": "Tell me a few words about your family. (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Family kinship nouns, possessive clitics (μου, μας), cardinal numbers and professions"
        },
        "notes": "Examiner Objective: Evaluates vocabulary of family members, basic age/profession descriptors, and relational cohesion.\nStrategy: Mention family size, immediate relatives, and one brief detail about what they do or where they live.",
        "example_el": "Έχω μια μικρή αλλά πολύ δεμένη οικογένεια. Είμαι παντρεμένος, έχω δύο μικρά παιδιά που πηγαίνουν στο δημοτικό σχολείο και οι γονείς μου ζουν κοντά μας.",
        "example_en": "I have a small but very close-knit family. I am married, I have two young children who go to primary school, and my parents live near us.",
        "example2_el": "Στην οικογένειά μου είμαστε τέσσερα άτομα, οι γονείς μου, η μεγαλύτερη αδελφή μου που είναι γιατρός και εγώ, και μιλάμε στο τηλέφωνο κάθε μέρα.",
        "example2_en": "In my family there are four of us—my parents, my older sister who is a doctor, and me—and we talk on the phone every day.",
        "keg_communicative_function": "Describing immediate family structure and family members' occupations"
    },
    {
        "id": "SP-U01-004",
        "greek": "Έχετε αδέλφια ή άλλα κοντινά πρόσωπα στην οικογένειά σας;",
        "english": "Do you have siblings or other close people in your family? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Comparative adjectives (μεγαλύτερος, μικρότερος), accusative object forms, interpersonal expressions"
        },
        "notes": "Examiner Objective: Checks comparison of ages and personality/relationship descriptions.\nStrategy: Even if you are an only child (μοναχοπαίδι), expand by talking about cousins or close relatives.",
        "example_el": "Ναι, έχω έναν μεγαλύτερο αδελφό που μένει στη Γερμανία και μια μικρότερη αδελφή που σπουδάζει ακόμα, και τα πηγαίνουμε εξαιρετικά μεταξύ μας.",
        "example_en": "Yes, I have an older brother who lives in Germany and a younger sister who is still studying, and we get along excellently with each other.",
        "example2_el": "Όχι, είμαι μοναχοπαίδι και δεν έχω αδέλφια, αλλά έχω δύο πρώτα ξαδέλφια στην ίδια ηλικία με εμένα και είμαστε σαν αδέλφια από παιδιά.",
        "example2_en": "No, I am an only child and do not have siblings, but I have two first cousins the same age as me and we have been like siblings since childhood.",
        "keg_communicative_function": "Describing siblings, age comparisons, and family closeness"
    },
    {
        "id": "SP-U01-005",
        "greek": "Πώς είναι ο χαρακτήρας του καλύτερού σας φίλου ή της καλύτερής σας φίλης;",
        "english": "What is the personality of your best friend like? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Personality adjectives (κοινωνικός, ευγενικός, υπομονετικός, ειλικρινής), causal clauses with γιατί/επειδή"
        },
        "notes": "Examiner Objective: Tests descriptive adjectives of character and ability to justify why you value someone.\nStrategy: Use 2-3 character adjectives and give a concrete example of how they support you.",
        "example_el": "Η καλύτερή μου φίλη λέγεται Ελένη και είναι πολύ ευγενική, ειλικρινής και αισιόδοξη κοπέλα, γιατί πάντα με ακούει με υπομονή όταν έχω κάποιο πρόβλημα.",
        "example_en": "My best friend is called Eleni and she is a very polite, honest, and optimistic girl, because she always listens to me patiently when I have a problem.",
        "example2_el": "Ο καλύτερός μου φίλος είναι ο Κώστας, ένας πολύ κοινωνικός και γενναιόδωρος άνθρωπος με υπέροχο χιούμορ, που με κάνει πάντα να γελάω όταν βρισκόμαστε.",
        "example2_en": "My best friend is Kostas, a very sociable and generous person with a wonderful sense of humor, who always makes me laugh when we meet up.",
        "keg_communicative_function": "Describing character traits and explaining personal friendships"
    },
    {
        "id": "SP-U01-006",
        "greek": "Πόσο συχνά βλέπετε τους συγγενείς και τους φίλους σας;",
        "english": "How often do you see your relatives and friends? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Frequency expressions (μία φορά την εβδομάδα, κάθε σαββατοκύριακο, σπάνια), plural accusative nouns"
        },
        "notes": "Examiner Objective: Assesses mastery of frequency adverbs and contrast between nearby friends vs. distant relatives.\nStrategy: Contrast how often you meet local friends in person versus speaking with distant relatives online.",
        "example_el": "Τους φίλους μου τους βλέπω σχεδόν κάθε σαββατοκύριακο για καφέ ή φαγητό, ενώ τους συγγενείς μου τους επισκέπτομαι δύο φορές τον χρόνο στις γιορτές.",
        "example_en": "I see my friends almost every weekend for coffee or food, whereas I visit my relatives twice a year during the holidays.",
        "example2_el": "Επειδή δουλεύω αρκετές ώρες τις καθημερινές, συναντώ τους φίλους μου μία φορά την εβδομάδα, αλλά μιλάω με τους γονείς μου μέσω βιντεοκλήσης κάθε Κυριακή.",
        "example2_en": "Because I work quite a few hours on weekdays, I meet my friends once a week, but I speak with my parents via video call every Sunday.",
        "keg_communicative_function": "Stating frequency of social and family contact"
    },
    {
        "id": "SP-U01-007",
        "greek": "Ποια είναι η οικογενειακή σας κατάσταση και με ποιον μένετε;",
        "english": "What is your marital status and who do you live with? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Marital status adjectives (ελεύθερος/η, παντρεμένος/η), accompaniment (μαζί με + accusative), verb συγκατοικώ"
        },
        "notes": "Examiner Objective: Checks accurate gender agreement on status adjectives (παντρεμένος/παντρεμένη, ελεύθερος/ελεύθερη).\nStrategy: Make sure adjective endings match your grammatical gender and mention household dynamics.",
        "example_el": "Είμαι παντρεμένη εδώ και πέντε χρόνια και μένω σε ένα φωτεινό διαμέρισμα με τον άντρα μου, την κόρη μας και έναν μικρό σκύλο.",
        "example_en": "I have been married for five years and I live in a bright apartment with my husband, our daughter, and a small dog.",
        "example2_el": "Αυτή τη στιγμή είμαι ελεύθερος και συγκατοικώ με έναν καλό μου φίλο από το πανεπιστήμιο, ώστε να μοιραζόμαστε τα έξοδα του σπιτιού.",
        "example2_en": "Right now I am single and share an apartment with a good friend of mine from university so that we split the household expenses.",
        "keg_communicative_function": "Describing marital status and household living arrangements"
    },
    {
        "id": "SP-U01-008",
        "greek": "Τι σας αρέσει να κάνετε όταν περνάτε χρόνο με την οικογένειά σας;",
        "english": "What do you like to do when you spend time with your family? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Impersonal construction (μας αρέσει να + first plural subjunctive), temporal clauses with όταν"
        },
        "notes": "Examiner Objective: Tests first-person plural verb forms (-ουμε / -όμαστε) and shared family routines.\nStrategy: Describe both an indoor habit (cooking, board games) and an outdoor activity (excursions).",
        "example_el": "Όταν είμαστε όλοι μαζί, μας αρέσει να μαγειρεύουμε παραδοσιακά φαγητά την Κυριακή το μεσημέρι και να συζητάμε γύρω από το τραπέζι για τα νέα μας.",
        "example_en": "When we are all together, we like to cook traditional dishes on Sunday afternoon and chat around the table about our news.",
        "example2_el": "Μας αρέσει πολύ να πηγαίνουμε ημερήσιες εκδρομές στη φύση με το αυτοκίνητο ή να βλέπουμε όλοι μαζί μια ωραία ταινία το βράδυ στο σαλόνι.",
        "example2_en": "We really like going on day trips to nature by car or watching a nice movie all together in the evening in the living room.",
        "keg_communicative_function": "Expressing shared family activities and preferences"
    },

    # 009-016: Daily routine, workplace, profession, and university/school studies
    {
        "id": "SP-U01-009",
        "greek": "Τι δουλειά κάνετε και πώς είναι το ωράριό σας;",
        "english": "What job do you do and what are your working hours like? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Professions without indefinite article (είμαι/εργάζομαι ως), time expressions (από τις... μέχρι τις...)"
        },
        "notes": "Examiner Objective: Tests profession vocabulary and telling time in the accusative plural (από τις εννέα ως τις πέντε).\nStrategy: State your occupation, workplace type, and whether your schedule is fixed or flexible.",
        "example_el": "Εργάζομαι ως λογιστής σε μια ιδιωτική εταιρεία και έχω σταθερό ωράριο, από τις εννέα το πρωί μέχρι τις πέντε το απόγευμα, από Δευτέρα έως Παρασκευή.",
        "example_en": "I work as an accountant at a private company and I have fixed hours, from nine in the morning until five in the afternoon, Monday through Friday.",
        "example2_el": "Είμαι γραφίστρια και δουλεύω από το σπίτι μου με ευέλικτο ωράριο, αλλά συνήθως ξεκινάω στις οκτώμισι το πρωί και τελειώνω νωρίς το απόγευμα.",
        "example2_en": "I am a graphic designer and I work from home with a flexible schedule, but I usually start at eight-thirty in the morning and finish early in the afternoon.",
        "keg_communicative_function": "Describing occupation, workplace, and working hours"
    },
    {
        "id": "SP-U01-010",
        "greek": "Πώς είναι μια τυπική μέρα σας από το πρωί ως το βράδυ;",
        "english": "What is a typical day of yours like from morning to night? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Reflexive/middle voice routine verbs (ξυπνάω, ετοιμάζομαι, ξεκουράζομαι, κοιμάμαι), chronological connectors (πρώτα, μετά, τέλος)"
        },
        "notes": "Examiner Objective: Core A2 check on daily routine verbs and chronological sequencing.\nStrategy: Structure into Morning (πρωί), Afternoon (μεσημέρι/απόγευμα), and Evening (βράδυ) using connectors.",
        "example_el": "Ξυπνάω στις επτά το πρωί, πίνω έναν καφέ και πηγαίνω στη δουλειά μου. Το απόγευμα γυρίζω στο σπίτι, μαγειρεύω κάτι ελαφρύ και το βράδυ διαβάζω ελληνικά.",
        "example_en": "I wake up at seven in the morning, drink a coffee, and go to work. In the afternoon I return home, cook something light, and in the evening I study Greek.",
        "example2_el": "Κάθε πρωί ετοιμάζομαι γρήγορα, παίρνω το μετρό για το γραφείο και μετά τη δουλειά πηγαίνω στο γυμναστήριο πριν επιστρέψω στο σπίτι για δείπνο και ξεκούραση.",
        "example2_en": "Every morning I get ready quickly, take the metro to the office, and after work I go to the gym before returning home for dinner and rest.",
        "keg_communicative_function": "Narrating daily routines in chronological sequence"
    },
    {
        "id": "SP-U01-011",
        "greek": "Σας αρέσει η δουλειά σας ή οι σπουδές σας; Γιατί;",
        "english": "Do you like your job or your studies? Why? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Causal subordination (επειδή, γιατί), evaluative adjectives (δημιουργικός, ενδιαφέρων, κουραστικός), concession (παρόλο που)"
        },
        "notes": "Examiner Objective: Tests ability to express job/study satisfaction with balanced pros and cons.\nStrategy: Give a positive reason first, then add a realistic minor challenge using 'παρόλο που' or 'αλλά'.",
        "example_el": "Ναι, μου αρέσει πάρα πολύ η δουλειά μου επειδή είναι δημιουργική και συνεργάζομαι με ευγενικούς συναδέλφους, παρόλο που μερικές φορές έχει αρκετό άγχος.",
        "example_en": "Yes, I like my job very much because it is creative and I work with polite colleagues, even though sometimes it has quite a bit of stress.",
        "example2_el": "Οι σπουδές μου στην πληροφορική μού αρέσουν πολύ γιατί μαθαίνω συνέχεια καινούργια πράγματα και πιστεύω ότι θα βρω εύκολα μια καλή εργασία στο μέλλον.",
        "example2_en": "I like my studies in computer science very much because I am constantly learning new things and I believe I will easily find a good job in the future.",
        "keg_communicative_function": "Expressing and justifying satisfaction with work or studies"
    },
    {
        "id": "SP-U01-012",
        "greek": "Πώς πηγαίνετε συνήθως στη δουλειά σας και πόση ώρα διαρκεί η διαδρομή;",
        "english": "How do you usually get to work and how long does the commute take? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Means of transport (με το λεωφορείο, με το μετρό, με τα πόδια), duration verb (διαρκεί / μου παίρνει + minutes)"
        },
        "notes": "Examiner Objective: Assesses transport vocabulary and commuting duration descriptions.\nStrategy: Mention the vehicle you take, traffic conditions (κίνηση), and what you do during the commute.",
        "example_el": "Συνήθως πηγαίνω στη δουλειά μου με τον ηλεκτρικό σιδηρόδρομο γιατί έχει πολλή κίνηση στους δρόμους, και η διαδρομή διαρκεί περίπου τριάντα λεπτά.",
        "example_en": "I usually go to work by electric train because there is a lot of traffic on the roads, and the commute lasts about thirty minutes.",
        "example2_el": "Επειδή το γραφείο μου βρίσκεται αρκετά κοντά στο σπίτι μου, προτιμώ να πηγαίνω με τα πόδια κάθε πρωί και κάνω μόνο δεκαπέντε λεπτά.",
        "example2_en": "Because my office is located quite close to my home, I prefer to go on foot every morning and it only takes me fifteen minutes.",
        "keg_communicative_function": "Describing daily commuting means and travel duration"
    },
    {
        "id": "SP-U01-013",
        "greek": "Τι σπουδάσατε στο πανεπιστήμιο ή τι επάγγελμα θα θέλατε να κάνετε;",
        "english": "What did you study at university or what profession would you like to do? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Simple Past (Αόριστος: σπούδασα, τελείωσα) and Conditional desire (θα ήθελα να + subjunctive)"
        },
        "notes": "Examiner Objective: Tests shift from Present to Simple Past (Αόριστος) for educational background or Conditional for career goals.\nStrategy: Combine past studies ('σπούδασα...') with present work or future aspirations ('θα ήθελα να...').",
        "example_el": "Σπούδασα οικονομικά στο πανεπιστήμιο της πόλης μου πριν από δέκα χρόνια και στο μέλλον θα ήθελα πολύ να ανοίξω το δικό μου λογιστικό γραφείο.",
        "example_en": "I studied economics at my city's university ten years ago, and in the future I would really like to open my own accounting office.",
        "example2_el": "Τελείωσα τη σχολή ιστορίας και αρχαιολογίας γιατί αγαπώ τον αρχαίο πολιτισμό, και τώρα θα ήθελα να εργαστώ ως ξεναγός σε μουσεία της Ελλάδας.",
        "example2_en": "I graduated from the school of history and archaeology because I love ancient civilization, and now I would like to work as a tour guide in museums in Greece.",
        "keg_communicative_function": "Recounting educational background and stating future career ambitions"
    },
    {
        "id": "SP-U01-014",
        "greek": "Προτιμάτε να δουλεύετε από το σπίτι ή στο γραφείο με συναδέλφους;",
        "english": "Do you prefer working from home or at the office with colleagues? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Preference structures (προτιμώ να + subjunctive), comparative justification, workplace lexicon"
        },
        "notes": "Examiner Objective: Evaluates ability to express preferences and weigh two options.\nStrategy: State your preference clearly and mention both efficiency/comfort and social contact.",
        "example_el": "Προτιμώ να δουλεύω στο γραφείο τρεις μέρες την εβδομάδα για να βλέπω τους συναδέλφους μου, και τις υπόλοιπες δύο μέρες από το σπίτι με ησυχία.",
        "example_en": "I prefer to work at the office three days a week so I can see my colleagues, and the remaining two days from home in peace and quiet.",
        "example2_el": "Προσωπικά προτιμώ να εργάζομαι από το σπίτι μου, επειδή δεν χάνω καθόλου χρόνο στις μετακινήσεις το πρωί και μπορώ να συγκεντρώνομαι πολύ καλύτερα.",
        "example2_en": "Personally I prefer working from home because I do not waste any time commuting in the morning and I can concentrate much better.",
        "keg_communicative_function": "Comparing work environments and justifying personal preference"
    },
    {
        "id": "SP-U01-015",
        "greek": "Τι κάνετε συνήθως στο διάλειμμά σας το μεσημέρι στη δουλειά;",
        "english": "What do you usually do during your lunch break at work? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Present tense habitual actions, food and refreshment vocabulary, prepositions of place"
        },
        "notes": "Examiner Objective: Tests everyday midday routine and food/socializing vocabulary.\nStrategy: Mention how long your break is, what you eat, and whether you step outside for fresh air.",
        "example_el": "Στο μεσημεριανό μου διάλειμμα, που κρατάει μία ώρα, τρώω συνήθως το φαγητό που έχω φέρει από το σπίτι και μετά κάνω έναν σύντομο περίπατο.",
        "example_en": "During my lunch break, which lasts one hour, I usually eat the food I brought from home and afterwards take a short walk.",
        "example2_el": "Το μεσημέρι βγαίνω μαζί με τους συναδέλφους μου σε ένα μικρό εστιατόριο κοντά στο γραφείο μας, όπου τρώμε μια σαλάτα και πίνουμε καφέ.",
        "example2_en": "At noon I go out with my colleagues to a small restaurant near our office, where we eat a salad and drink coffee.",
        "keg_communicative_function": "Describing midday breaks and workplace meal habits"
    },
    {
        "id": "SP-U01-016",
        "greek": "Πότε έχετε τις περισσότερες υποχρεώσεις μέσα στην εβδομάδα;",
        "english": "When do you have the most obligations during the week? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Days of the week in accusative (τη Δευτέρα, την Τετάρτη), superlative quantifier (τις περισσότερες υποχρεώσεις)"
        },
        "notes": "Examiner Objective: Tests days of the week with proper feminine articles and workload explanation.\nStrategy: Name specific days (e.g., Monday/Wednesday) and list the obligations (meetings, lessons, errands).",
        "example_el": "Έχω τις περισσότερες υποχρεώσεις τη Δευτέρα και την Τετάρτη, γιατί εκτός από τη δουλειά μου έχω απογευματινά μαθήματα ελληνικών και προπόνηση στο κολυμβητήριο.",
        "example_en": "I have the most obligations on Monday and Wednesday, because besides my job I have afternoon Greek lessons and training at the swimming pool.",
        "example2_el": "Οι πιο δύσκολες μέρες της εβδομάδας για εμένα είναι η Τρίτη και η Πέμπτη, επειδή έχουμε πολλές συναντήσεις στο γραφείο και γυρίζω αργά στο σπίτι.",
        "example2_en": "The hardest days of the week for me are Tuesday and Thursday, because we have many meetings at the office and I return home late.",
        "keg_communicative_function": "Identifying busy days of the week and explaining weekly obligations"
    },

    # 017-024: Free time, weekend habits, sports, entertainment, and hobbies
    {
        "id": "SP-U01-017",
        "greek": "Πώς περνάτε συνήθως τα σαββατοκύριακά σας;",
        "english": "How do you usually spend your weekends? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Habitual aspect, leisure vocabulary, frequency adverbs and weather conditions (όταν ο καιρός είναι καλός)"
        },
        "notes": "Examiner Objective: Tests present tense fluency and connector usage (συνήθως, μερικές φορές, όταν).\nStrategy: Avoid one-word answers. Follow the Rule of Three: Saturday activity + Sunday activity + weather condition.",
        "example_el": "Τα σαββατοκύριακα συνήθως ξεκουράζομαι στο σπίτι, αλλά όταν ο καιρός είναι καλός, μου αρέσει να πηγαίνω μεγάλες βόλτες δίπλα στη θάλασσα με τους φίλους μου.",
        "example_en": "On weekends I usually rest at home, but when the weather is fine, I enjoy taking long walks by the sea with my friends.",
        "example2_el": "Το Σάββατο το πρωί κάνω τα ψώνια της εβδομάδας στη λαϊκή αγορά και την Κυριακή μαγειρεύω για όλη την οικογένεια και βλέπουμε ταινίες.",
        "example2_en": "On Saturday morning I do the week's shopping at the farmers' market, and on Sunday I cook for the whole family and we watch movies.",
        "keg_communicative_function": "Describing weekend routines and habitual leisure activities"
    },
    {
        "id": "SP-U01-018",
        "greek": "Έχετε κάποιο αγαπημένο χόμπι ή ασχολείστε με κάποιο άθλημα;",
        "english": "Do you have a favorite hobby or do you play any sport? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Deponent verb ασχολούμαι με + accusative, sports/hobby collocations (παίζω τένις, κάνω γιόγκα/ποδήλατο)"
        },
        "notes": "Examiner Objective: Checks accurate use of 'ασχολούμαι με' and 'κάνω/παίζω' with sports and hobbies.\nStrategy: State the hobby/sport, how often you practice it, and how it makes you feel (με βοηθάει να χαλαρώνω).",
        "example_el": "Ναι, στον ελεύθερό μου χρόνο ασχολούμαι με τη φωτογραφία και τρεις φορές την εβδομάδα κάνω τρέξιμο στο πάρκο, γιατί με βοηθάει να διώχνω το άγχος.",
        "example_en": "Yes, in my free time I do photography and three times a week I go running in the park, because it helps me relieve stress.",
        "example2_el": "Το αγαπημένο μου άθλημα είναι η κολύμβηση και πηγαίνω στη θάλασσα ή στο κολυμβητήριο κάθε Σάββατο, ενώ στο σπίτι μου αρέσει να παίζω κιθάρα.",
        "example2_en": "My favorite sport is swimming and I go to the sea or the pool every Saturday, while at home I like playing the guitar.",
        "keg_communicative_function": "Discussing hobbies, sports, and their benefits for well-being"
    },
    {
        "id": "SP-U01-019",
        "greek": "Τι είδους μουσική ακούτε και τι βιβλία προτιμάτε να διαβάζετε;",
        "english": "What kind of music do you listen to and what books do you prefer to read? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Cultural genre adjectives (έντεχνη μουσική, αστυνομικά μυθιστορήματα, ιστορικά βιβλία), temporal clauses"
        },
        "notes": "Examiner Objective: Tests cultural/artistic vocabulary and ability to connect habits to specific moments of the day.\nStrategy: Mention Greek music if applicable (έντεχνα/λαϊκά) to show cultural engagement, plus your preferred book genre.",
        "example_el": "Μου αρέσει πολύ να ακούω ελληνική έντεχνη μουσική όταν οδηγώ, και το βράδυ πριν κοιμηθώ προτιμώ να διαβάζω αστυνομικά μυθιστορήματα ή ιστορικά βιβλία.",
        "example_en": "I really like listening to Greek art-folk music when I drive, and at night before sleeping I prefer reading detective novels or history books.",
        "example2_el": "Ακούω κυρίως κλασική μουσική και τζαζ όταν θέλω να συγκεντρωθώ, ενώ τον τελευταίο καιρό διαβάζω εύκολα ελληνικά διηγήματα για να εμπλουτίσω το λεξιλόγιό μου.",
        "example2_en": "I mainly listen to classical music and jazz when I want to concentrate, while lately I have been reading easy Greek short stories to enrich my vocabulary.",
        "keg_communicative_function": "Expressing tastes in music and reading material"
    },
    {
        "id": "SP-U01-020",
        "greek": "Προτιμάτε να βλέπετε ταινίες στον κινηματογράφο ή στο σπίτι σας;",
        "english": "Do you prefer watching movies at the cinema or at home? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Comparative adjectives (πιο άνετα, πιο οικονομικά), seasonal vocabulary (θερινός κινηματογράφος)"
        },
        "notes": "Examiner Objective: Assesses entertainment vocabulary and comparison of two leisure venues.\nStrategy: Mention Greek open-air summer cinemas (θερινό σινεμά) for an authentic cultural touch!",
        "example_el": "Τον χειμώνα προτιμώ να βλέπω ταινίες στο σπίτι μου στον καναπέ, αλλά το καλοκαίρι μου αρέσει πάρα πολύ να πηγαίνω σε θερινό κινηματογράφο με φίλους.",
        "example_en": "In winter I prefer watching movies at home on the couch, but in summer I really love going to an open-air cinema with friends.",
        "example2_el": "Προτιμώ τον κινηματογράφο γιατί η μεγάλη οθόνη και ο ήχος είναι εντυπωσιακά, και μετά την ταινία μπορούμε να πάμε για ένα ποτό και να τη σχολιάσουμε.",
        "example2_en": "I prefer the cinema because the big screen and sound are impressive, and after the movie we can go for a drink and discuss it.",
        "keg_communicative_function": "Comparing entertainment venues and explaining seasonal preferences"
    },
    {
        "id": "SP-U01-021",
        "greek": "Σας αρέσει να μαγειρεύετε ή προτιμάτε να τρώτε έξω σε εστιατόρια;",
        "english": "Do you like cooking or do you prefer eating out at restaurants? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Food & nutrition adjectives (υγιεινό, σπιτικό, νόστιμο), contrast connectors (τις καθημερινές... ενώ το Σάββατο...)"
        },
        "notes": "Examiner Objective: Tests culinary vocabulary and ability to distinguish weekday routines from weekend outings.\nStrategy: Explain that you cook healthy homemade food on weekdays and go to a taverna on weekends.",
        "example_el": "Τις καθημερινές προτιμώ να μαγειρεύω στο σπίτι γιατί το σπιτικό φαγητό είναι πιο υγιεινό και οικονομικό, αλλά το Σάββατο το βράδυ βγαίνουμε σε κάποια ταβέρνα.",
        "example_en": "On weekdays I prefer cooking at home because homemade food is healthier and more economical, but on Saturday night we go out to a taverna.",
        "example2_el": "Μου αρέσει πολύ η μαγειρική και δοκιμάζω συχνά ελληνικές συνταγές, όπως γεμιστά και μουσακά, όμως μία φορά την εβδομάδα τρώω έξω με την παρέα μου.",
        "example2_en": "I really like cooking and often try Greek recipes like gemista and moussaka, however once a week I eat out with my group of friends.",
        "keg_communicative_function": "Discussing cooking habits versus dining out"
    },
    {
        "id": "SP-U01-022",
        "greek": "Πώς χρησιμοποιείτε το διαδίκτυο στον ελεύθερό σας χρόνο;",
        "english": "How do you use the internet in your free time? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Purpose clauses (για να + subjunctive), digital/media vocabulary (ενημερώνομαι, επικοινωνώ, βίντεο)"
        },
        "notes": "Examiner Objective: Tests digital technology vocabulary in Greek and purpose clauses.\nStrategy: Mention practical uses (news, Greek learning videos, keeping in touch with family abroad).",
        "example_el": "Χρησιμοποιώ το διαδίκτυο καθημερινά για να διαβάζω τις ειδήσεις, να επικοινωνώ με τους φίλους μου στο εξωτερικό και να παρακολουθώ εκπαιδευτικά βίντεο στα ελληνικά.",
        "example_en": "I use the internet daily to read the news, communicate with my friends abroad, and watch educational videos in Greek.",
        "example2_el": "Στον ελεύθερό μου χρόνο μπαίνω στο διαδίκτυο για να ακούω μουσική, να βρίσκω ιδέες για ταξίδια και μερικές φορές να κάνω ηλεκτρονικές αγορές.",
        "example2_en": "In my free time I go on the internet to listen to music, find travel ideas, and sometimes do online shopping.",
        "keg_communicative_function": "Describing everyday internet use and digital habits"
    },
    {
        "id": "SP-U01-023",
        "greek": "Πού σας αρέσει να βγαίνετε το βράδυ με την παρέα σας;",
        "english": "Where do you like going out in the evening with your friends? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Entertainment venues (ταβέρνα, καφετέρια, θέατρο, μπαρ), plural verbs of socializing (συζητάμε, διασκεδάζουμε)"
        },
        "notes": "Examiner Objective: Checks vocabulary for social venues and atmosphere adjectives (ήσυχος, ζωντανός).\nStrategy: Describe the type of venue and why you prefer that atmosphere (e.g., quiet place where we can talk).",
        "example_el": "Όταν βγαίνω το βράδυ με την παρέα μου, προτιμάμε να πηγαίνουμε σε ήσυχες ταβέρνες με ζωντανή μουσική, όπου μπορούμε να φάμε μεζέδες και να συζητήσουμε.",
        "example_en": "When I go out in the evening with my friends, we prefer going to quiet tavernas with live music, where we can eat meze and chat.",
        "example2_el": "Μας αρέσει να πηγαίνουμε πρώτα στο θέατρο ή στον κινηματογράφο στο κέντρο της πόλης και μετά να καθόμαστε σε ένα όμορφο μαγαζί για ένα ποτήρι κρασί.",
        "example2_en": "We like going first to the theater or cinema in the city center and afterwards sitting at a nice place for a glass of wine.",
        "keg_communicative_function": "Describing evening social outings and preferred venues"
    },
    {
        "id": "SP-U01-024",
        "greek": "Πώς γιορτάζετε συνήθως τα γενέθλιά σας ή τις μεγάλες γιορτές;",
        "english": "How do you usually celebrate your birthday or major holidays? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Celebration verbs (γιορτάζω, καλώ, προσφέρω), festive vocabulary (γενέθλια, τούρτα, δώρα)"
        },
        "notes": "Examiner Objective: Evaluates vocabulary related to celebrations, hospitality, and social customs.\nStrategy: Mention who you invite, whether you celebrate at home or outside, and a special detail.",
        "example_el": "Στα γενέθλιά μου συνήθως καλώ τους πιο στενούς μου φίλους στο σπίτι, ετοιμάζω διάφορα φαγητά και γλυκά, και περνάμε ένα πολύ ευχάριστο βράδυ μαζί.",
        "example_en": "On my birthday I usually invite my closest friends to my home, prepare various dishes and sweets, and we spend a very pleasant evening together.",
        "example2_el": "Προτιμώ να γιορτάζω τα γενέθλιά μου σε ένα ωραίο εστιατόριο δίπλα στη θάλασσα μαζί με την οικογένειά μου, όπου κόβουμε την τούρτα και ανταλλάσσουμε ευχές.",
        "example2_en": "I prefer celebrating my birthday at a nice restaurant by the sea with my family, where we cut the cake and exchange wishes.",
        "keg_communicative_function": "Describing personal celebrations and festive customs"
    },

    # 025-032: Living quarters, apartment/house description, and neighborhood life
    {
        "id": "SP-U01-025",
        "greek": "Σε τι είδους σπίτι μένετε τώρα; Περιγράψτε το μας λίγο.",
        "english": "What kind of home do you live in now? Describe it to us a little. (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Housing lexicon (διαμέρισμα, μονοκατοικία, όροφος, δωμάτια), descriptive adjectives (φωτεινό, άνετο, ευρύχωρο)"
        },
        "notes": "Examiner Objective: Core A2 topic testing rooms of the house, floor numbers, and descriptive adjectives.\nStrategy: Mention housing type, floor, number of rooms, and one standout feature (e.g., a big balcony).",
        "example_el": "Μένω σε ένα φωτεινό και άνετο διαμέρισμα στον τρίτο όροφο μιας πολυκατοικίας, το οποίο έχει δύο υπνοδωμάτια, μεγάλο σαλόνι, κουζίνα και ένα υπέροχο μπαλκόνι.",
        "example_en": "I live in a bright and comfortable apartment on the third floor of an apartment building, which has two bedrooms, a large living room, a kitchen, and a wonderful balcony.",
        "example2_el": "Ζούμε σε μια μικρή μονοκατοικία λίγο έξω από το κέντρο της πόλης, που διαθέτει έναν όμορφο κήπο με δέντρα και λουλούδια όπου παίζουν τα παιδιά μας.",
        "example2_en": "We live in a small detached house just outside the city center, which has a beautiful garden with trees and flowers where our children play.",
        "keg_communicative_function": "Describing one's home, rooms, and layout"
    },
    {
        "id": "SP-U01-026",
        "greek": "Ποιο είναι το αγαπημένο σας δωμάτιο στο σπίτι και γιατί;",
        "english": "Which is your favorite room in the house and why? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Neuter nouns and adjectives (το αγαπημένο μου δωμάτιο, το σαλόνι), furniture vocabulary, relative pronoun όπου"
        },
        "notes": "Examiner Objective: Checks furniture/interior vocabulary and explanation of personal comfort.\nStrategy: Pick the living room, kitchen, or balcony, describe 2 pieces of furniture, and say what you do there.",
        "example_el": "Το αγαπημένο μου μέρος στο σπίτι είναι το σαλόνι, γιατί έχει μεγάλα παράθυρα με πολύ ήλιο, έναν αναπαυτικό καναπέ και τη βιβλιοθήκη μου όπου διαβάζω.",
        "example_en": "My favorite place in the house is the living room, because it has large windows with lots of sun, a comfortable sofa, and my bookcase where I read.",
        "example2_el": "Προτιμώ την κουζίνα και το μεγάλο μπαλκόνι μας, επειδή εκεί πίνω τον πρωινό μου καφέ βλέποντας τη θέα και το βράδυ μαγειρεύω ακούγοντας μουσική.",
        "example2_en": "I prefer the kitchen and our big balcony, because that is where I drink my morning coffee looking at the view and in the evening I cook while listening to music.",
        "keg_communicative_function": "Describing a specific room and explaining personal attachment"
    },
    {
        "id": "SP-U01-027",
        "greek": "Πώς είναι η γειτονιά σας; Έχει καταστήματα και συγκοινωνίες;",
        "english": "What is your neighborhood like? Does it have shops and public transport? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Existential verbs (έχει / υπάρχουν), urban infrastructure nouns (σούπερ μάρκετ, φαρμακείο, στάση λεωφορείου)"
        },
        "notes": "Examiner Objective: Tests neighborhood amenities vocabulary and existential plural structures ('υπάρχουν...').\nStrategy: Describe the general vibe (ήσυχη και ασφαλής) and list 3-4 practical shops/transport links nearby.",
        "example_el": "Η γειτονιά μου είναι πολύ ήσυχη και φιλική, αλλά ταυτόχρονα έχει τα πάντα κοντά, όπως σούπερ μάρκετ, φούρνο, φαρμακείο και σταθμό του μετρό σε πέντε λεπτά.",
        "example_en": "My neighborhood is very quiet and friendly, yet at the same time it has everything nearby, such as a supermarket, bakery, pharmacy, and a metro station five minutes away.",
        "example2_el": "Μένω σε μια ζωντανή γειτονιά κοντά στο κέντρο, όπου υπάρχουν πολλά μικρά μαγαζιά, ένα μεγάλο πάρκο με πράσινο και πολύ συχνές συγκοινωνίες με λεωφορεία.",
        "example2_en": "I live in a lively neighborhood near the center, where there are many small shops, a large green park, and very frequent bus connections.",
        "keg_communicative_function": "Describing neighborhood amenities, shops, and transport access"
    },
    {
        "id": "SP-U01-028",
        "greek": "Τι σας αρέσει περισσότερο στη γειτονιά σας και τι θα θέλατε να αλλάξει;",
        "english": "What do you like most about your neighborhood and what would you like to change? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Contrastive evaluation (μου αρέσει ότι... αλλά θα ήθελα να...), urban issues (πάρκινγκ, θόρυβος, καθαριότητα)"
        },
        "notes": "Examiner Objective: Assesses ability to evaluate local living conditions positively and critically.\nStrategy: Praise one feature (trees, safety, proximity to sea) and suggest one realistic urban improvement (parking, wider pavements).",
        "example_el": "Μου αρέσει περισσότερο ότι η γειτονιά μας έχει πολλά δέντρα και καλούς γείτονες, αλλά θα ήθελα να υπάρχουν περισσότερες θέσεις στάθμευσης για τα αυτοκίνητα.",
        "example_en": "What I like most is that our neighborhood has many trees and good neighbors, but I would like there to be more parking spaces for cars.",
        "example2_el": "Αυτό που αγαπώ στη γειτονιά μου είναι ότι βρίσκεται δίπλα στη θάλασσα, όμως θα ήθελα ο δήμος να φτιάξει καλύτερα πεζοδρόμια και λιγότερο θόρυβο το βράδυ.",
        "example2_en": "What I love about my neighborhood is that it is right by the sea, however I would like the municipality to build better sidewalks and have less noise at night.",
        "keg_communicative_function": "Evaluating neighborhood advantages and suggesting urban improvements"
    },
    {
        "id": "SP-U01-029",
        "greek": "Προτιμάτε τη ζωή σε μια μεγάλη πόλη ή σε ένα μικρό χωριό στην εξοχή;",
        "english": "Do you prefer life in a big city or in a small village in the countryside? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Comparative arguments, urban vs. rural lexicon (επιλογές διασκέδασης, καθαρός αέρας, ρυθμοί ζωής)"
        },
        "notes": "Examiner Objective: Classic KEG A2 comparison question testing city vs. countryside vocabulary.\nStrategy: Acknowledge the benefits of both before stating which suits your current stage of life.",
        "example_el": "Αυτή τη στιγμή προτιμώ τη ζωή στην πόλη γιατί βρίσκω πιο εύκολα δουλειά, νοσοκομεία και θέατρα, αλλά το καλοκαίρι λατρεύω την ηρεμία του χωριού.",
        "example_en": "Right now I prefer city life because I find work, hospitals, and theaters more easily, but in the summer I adore the tranquility of the village.",
        "example2_el": "Προτιμώ να ζω σε μια μικρή πόλη ή σε ένα χωριό κοντά στη φύση, επειδή ο αέρας είναι καθαρός και οι ρυθμοί της ζωής είναι πιο ανθρώπινοι.",
        "example2_en": "I prefer living in a small town or a village close to nature, because the air is clean and the pace of life is more humane.",
        "keg_communicative_function": "Comparing urban and rural lifestyles and justifying preferences"
    },
    {
        "id": "SP-U01-030",
        "greek": "Πώς είναι οι σχέσεις σας με τους γείτονές σας;",
        "english": "What are your relations with your neighbors like? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Reciprocal/social verbs (χαιρετιόμαστε, βοηθάμε ο ένας τον άλλον), adjectives of politeness (εξυπηρετικός, διακριτικός)"
        },
        "notes": "Examiner Objective: Tests social interaction vocabulary within an apartment building or neighborhood.\nStrategy: Describe friendly everyday gestures (saying good morning, watering plants when away, sharing sweets).",
        "example_el": "Έχω εξαιρετικές σχέσεις με τους γείτονές μου στην πολυκατοικία, χαιρετιόμαστε πάντα με χαμόγελο και βοηθάμε ο ένας τον άλλον όταν λείπουμε σε ταξίδι.",
        "example_en": "I have excellent relations with my neighbors in the apartment building; we always greet each other with a smile and help one another when we are away on a trip.",
        "example2_el": "Οι γείτονές μου είναι πολύ ευγενικοί και διακριτικοί άνθρωποι, και μάλιστα η κυρία που μένει στον κάτω όροφο μού φέρνει συχνά σπιτικά γλυκά.",
        "example2_en": "My neighbors are very polite and discreet people, and in fact the lady who lives on the floor below often brings me homemade sweets.",
        "keg_communicative_function": "Describing neighborly relations and community interaction"
    },
    {
        "id": "SP-U01-031",
        "greek": "Πού κάνετε συνήθως τα ψώνια σας για το σπίτι;",
        "english": "Where do you usually do your household shopping? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Shopping nouns (λαϊκή αγορά, σούπερ μάρκετ, κρεοπωλείο, φούρνος), comparative quality/price adjectives (φρέσκα, φθηνά)"
        },
        "notes": "Examiner Objective: Tests everyday consumer vocabulary and distinction between specialty shops and supermarkets.\nStrategy: Contrast buying fresh produce at the 'λαϊκή αγορά' with buying dry goods at the supermarket.",
        "example_el": "Κάθε Σάββατο πηγαίνω στη λαϊκή αγορά της γειτονιάς μου για να αγοράσω φρέσκα φρούτα και λαχανικά σε καλές τιμές, και τα υπόλοιπα τα παίρνω από το σούπερ μάρκετ.",
        "example_en": "Every Saturday I go to my neighborhood farmers' market to buy fresh fruit and vegetables at good prices, and I get the rest from the supermarket.",
        "example2_el": "Προτιμώ να ψωνίζω από τα μικρά καταστήματα της περιοχής μου, όπως τον φούρνο και το μανάβικο, γιατί η ποιότητα των προϊόντων είναι εξαιρετική.",
        "example2_en": "I prefer shopping at the small local stores in my area, like the bakery and the greengrocer's, because the quality of the products is excellent.",
        "keg_communicative_function": "Describing shopping habits and preferred local markets"
    },
    {
        "id": "SP-U01-032",
        "greek": "Πώς μοιράζεστε τις δουλειές του σπιτιού στην οικογένειά σας;",
        "english": "How do you share the household chores in your family? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Household chore verbs (σκουπίζω, πλένω τα πιάτα, σιδερώνω, μαγειρεύω), distributive structure (εγώ... ενώ ο/η...)"
        },
        "notes": "Examiner Objective: Evaluates vocabulary of domestic chores and cooperative action.\nStrategy: Use 'εγώ αναλαμβάνω...' and 'ενώ ο/η σύντροφός μου...' to show clear sentence contrast.",
        "example_el": "Στο σπίτι μας μοιραζόμαστε όλες τις δουλειές δίκαια. Εγώ συνήθως μαγειρεύω και βάζω πλυντήριο, ενώ ο σύζυγός μου κάνει τα ψώνια και καθαρίζει το σπίτι.",
        "example_en": "In our home we share all the chores fairly. I usually cook and do the laundry, while my husband does the shopping and cleans the house.",
        "example2_el": "Επειδή μένω μόνος μου, κάνω όλες τις δουλειές του σπιτιού το Σάββατο το πρωί, δηλαδή σκουπίζω, τακτοποιώ τα δωμάτια και σιδερώνω τα ρούχα της εβδομάδας.",
        "example2_en": "Because I live alone, I do all the housework on Saturday morning, meaning I vacuum, tidy the rooms, and iron the week's clothes.",
        "keg_communicative_function": "Describing domestic chores and division of household labor"
    },

    # 033-040: Why Greek?, experience visiting Greece/Cyprus, learning methods, and future goals
    {
        "id": "SP-U01-033",
        "greek": "Γιατί αποφασίσατε να μάθετε ελληνικά;",
        "english": "Why did you decide to learn Greek? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Simple Past + Subjunctive (αποφάσισα να μάθω), causal & purpose clauses (επειδή, για να μπορώ να...)"
        },
        "notes": "Examiner Objective: High-frequency Stage 1 question testing personal motivation and connection to Greek culture/life.\nStrategy: Combine a practical reason (work, living in Greece/Cyprus, family) with an emotional/cultural appreciation.",
        "example_el": "Αποφάσισα να μάθω ελληνικά επειδή ζω και εργάζομαι στην Ελλάδα, και θέλω να επικοινωνώ άνετα στην καθημερινότητά μου με τους Έλληνες φίλους και συναδέλφους μου.",
        "example_en": "I decided to learn Greek because I live and work in Greece, and I want to communicate comfortably in my daily life with my Greek friends and colleagues.",
        "example2_el": "Αγαπώ πάρα πολύ την ελληνική ιστορία και τον πολιτισμό, επισκέπτομαι την Ελλάδα κάθε χρόνο και ήθελα να μιλάω με τους κατοίκους στη δική τους γλώσσα.",
        "example2_en": "I love Greek history and culture very much, I visit Greece every year, and I wanted to speak with the locals in their own language.",
        "keg_communicative_function": "Explaining personal and practical motivations for learning Greek"
    },
    {
        "id": "SP-U01-034",
        "greek": "Πόσο καιρό μαθαίνετε ελληνικά και πώς κάνετε εξάσκηση;",
        "english": "How long have you been learning Greek and how do you practice? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Duration in present tense (μαθαίνω ελληνικά εδώ και...), instrumental phrases (με δάσκαλο, ακούγοντας ραδιόφωνο)"
        },
        "notes": "Examiner Objective: Tests language-learning vocabulary and active study strategies.\nStrategy: Mention how long you have taken lessons and 2 ways you practice outside class (Greek radio, flashcards, chatting).",
        "example_el": "Μαθαίνω ελληνικά εδώ και ενάμιση χρόνο με μια πολύ καλή δασκάλα, και κάθε μέρα κάνω εξάσκηση ακούγοντας ελληνικό ραδιόφωνο και μιλώντας με τους γείτονές μου.",
        "example_en": "I have been learning Greek for a year and a half with a very good teacher, and every day I practice by listening to Greek radio and speaking with my neighbors.",
        "example2_el": "Παρακολουθώ μαθήματα ελληνικών δύο φορές την εβδομάδα τους τελευταίους δέκα μήνες και μελετάω καθημερινά λεξιλόγιο και διαλόγους στον υπολογιστή μου.",
        "example2_en": "I have been attending Greek lessons twice a week for the last ten months and I study vocabulary and dialogues daily on my computer.",
        "keg_communicative_function": "Describing duration of language study and practice methods"
    },
    {
        "id": "SP-U01-035",
        "greek": "Τι σας δυσκολεύει περισσότερο στην ελληνική γλώσσα και τι σας φαίνεται πιο εύκολο;",
        "english": "What do you find most difficult in the Greek language and what seems easier to you? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Psychological/experiential verbs with clitics (με δυσκολεύει, μου φαίνεται), grammatical terminology (τα ρήματα, η ορθογραφία, η προφορά)"
        },
        "notes": "Examiner Objective: Checks meta-linguistic vocabulary and accurate singular/plural agreement with 'με δυσκολεύει / με δυσκολεύουν'.\nStrategy: Note that if the subject is plural (e.g., οι καταλήξεις), use plural verb 'με δυσκολεύουν'.",
        "example_el": "Με δυσκολεύουν περισσότερο η ορθογραφία και οι χρόνοι των ρημάτων, αλλά η προφορά και η καθημερινή προφορική επικοινωνία μού φαίνονται αρκετά πιο εύκολες.",
        "example_en": "Spelling and verb tenses give me the most difficulty, but pronunciation and everyday spoken communication seem much easier to me.",
        "example2_el": "Στην αρχή με δυσκόλευαν τα τρία γένη των ουσιαστικών, όμως τώρα καταλαβαίνω πολύ εύκολα τους Έλληνες όταν μιλούν καθαρά και μαθαίνω γρήγορα νέες λέξεις.",
        "example2_en": "At the beginning the three genders of nouns were difficult for me, however now I understand Greeks very easily when they speak clearly and I learn new words quickly.",
        "keg_communicative_function": "Identifying linguistic challenges and strengths in learning Greek"
    },
    {
        "id": "SP-U01-036",
        "greek": "Έχετε ταξιδέψει σε διάφορα μέρη στην Ελλάδα ή στην Κύπρο; Πού πήγατε;",
        "english": "Have you traveled to various places in Greece or Cyprus? Where did you go? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Simple Past (Αόριστος) of travel verbs (ταξίδεψα, πήγα, επισκέφθηκα, έμεινα, είδα), geographical place names"
        },
        "notes": "Examiner Objective: Tests past narrative skills (Αόριστος) and geographical names in the accusative case.\nStrategy: Name 2-3 specific islands or cities you visited and mention one memorable sight or impression.",
        "example_el": "Ναι, πέρυσι το καλοκαίρι ταξίδεψα στη Νάξο και στη Σαντορίνη, όπου είδα υπέροχες παραλίες, δοκίμασα παραδοσιακά φαγητά και εντυπωσιάστηκα από τη φιλοξενία των κατοίκων.",
        "example_en": "Yes, last summer I traveled to Naxos and Santorini, where I saw wonderful beaches, tried traditional food, and was impressed by the hospitality of the locals.",
        "example2_el": "Έχω επισκεφθεί την Αθήνα, το Ναύπλιο και την Πάφο στην Κύπρο, και μου άρεσαν πάρα πολύ οι αρχαιολογικοί χώροι και τα γραφικά σοκάκια δίπλα στη θάλασσα.",
        "example2_en": "I have visited Athens, Nafplio, and Paphos in Cyprus, and I really liked the archaeological sites and the picturesque alleys by the sea.",
        "keg_communicative_function": "Narrating past travel experiences in Greece and Cyprus"
    },
    {
        "id": "SP-U01-037",
        "greek": "Ποιο είναι το αγαπημένο σας ελληνικό φαγητό ή έθιμο;",
        "english": "What is your favorite Greek dish or custom? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Gastronomy and cultural traditions lexicon (παραδοσιακή κουζίνα, το Πάσχα, η ονομαστική γιορτή), descriptive clauses"
        },
        "notes": "Examiner Objective: Assesses cultural appreciation and descriptive vocabulary for food or Greek traditions.\nStrategy: Name a specific dish (e.g., παστίτσιο, χωριάτικη σαλάτα) or custom (e.g., Easter in the village) and explain why you love it.",
        "example_el": "Το αγαπημένο μου ελληνικό φαγητό είναι ο μουσακάς και η χωριάτικη σαλάτα με φέτα και ελαιόλαδο, γιατί τα υλικά είναι πάντα φρέσκα και πολύ νόστιμα.",
        "example_en": "My favorite Greek food is moussaka and Greek village salad with feta and olive oil, because the ingredients are always fresh and very tasty.",
        "example2_el": "Μου αρέσει πάρα πολύ το ελληνικό Πάσχα στην εξοχή, επειδή όλη η οικογένεια και οι φίλοι μαζεύονται έξω στη φύση, ψήνουν, τραγουδούν και γιορτάζουν μαζί.",
        "example2_en": "I really love Greek Easter in the countryside, because the whole family and friends gather outside in nature, roast food, sing, and celebrate together.",
        "keg_communicative_function": "Expressing appreciation for Greek cuisine and cultural traditions"
    },
    {
        "id": "SP-U01-038",
        "greek": "Ποια εποχή του χρόνου προτιμάτε και γιατί;",
        "english": "Which season of the year do you prefer and why? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Seasons with definite article (η άνοιξη, το καλοκαίρι, το φθινόπωρο, ο χειμώνας), weather expressions (κάνει ζέστη, έχει ήλιο)"
        },
        "notes": "Examiner Objective: Tests weather/climate vocabulary and seasonal activities.\nStrategy: State the season, describe the weather ('η φύση ανθίζει' / 'η μέρα είναι μεγάλη'), and mention what you do then.",
        "example_el": "Η αγαπημένη μου εποχή είναι η άνοιξη, επειδή ο καιρός είναι γλυκός χωρίς υπερβολική ζέστη, η φύση είναι καταπράσινη και μπορώ να κάνω εκδρομές.",
        "example_en": "My favorite season is spring, because the weather is mild without excessive heat, nature is lush green, and I can go on excursions.",
        "example2_el": "Προτιμώ το καλοκαίρι γιατί οι μέρες είναι μεγάλες και φωτεινές, παίρνω την άδειά μου από τη δουλειά και κολυμπάω στη θάλασσα κάθε απόγευμα.",
        "example2_en": "I prefer summer because the days are long and bright, I take my leave from work, and I swim in the sea every afternoon.",
        "keg_communicative_function": "Describing seasonal preferences, weather conditions, and outdoor activities"
    },
    {
        "id": "SP-U01-039",
        "greek": "Ποια είναι τα σχέδιά σας για το επόμενο καλοκαίρι;",
        "english": "What are your plans for next summer? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Simple Future (Συνοπτικός Μέλλοντας: θα πάω, θα μείνω, θα ξεκουραστώ) and intention verbs (σκοπεύω να, σκέφτομαι να)"
        },
        "notes": "Examiner Objective: Crucial test of Future Tense ('θα + συνοπτικός μέλλοντας') and planning verbs ('σκοπεύω να').\nStrategy: Use at least two future verbs ('θα ταξιδέψουμε', 'θα επισκεφθούμε') and mention destination and companions.",
        "example_el": "Το επόμενο καλοκαίρι σκοπεύω να πάρω δύο εβδομάδες άδεια τον Αύγουστο και θα ταξιδέψω με την οικογένειά μου στην Κρήτη για να ξεκουραστούμε.",
        "example_en": "Next summer I plan to take two weeks' vacation in August and I will travel with my family to Crete to rest.",
        "example2_el": "Σκέφτομαι να επισκεφθώ τους γονείς μου για λίγες μέρες τον Ιούλιο και στη συνέχεια θα πάω με τους φίλους μου διακοπές σε ένα ελληνικό νησί.",
        "example2_en": "I am thinking of visiting my parents for a few days in July and afterwards I will go on vacation with my friends to a Greek island.",
        "keg_communicative_function": "Expressing future vacation plans and intentions"
    },
    {
        "id": "SP-U01-040",
        "greek": "Ποιος είναι ο επόμενος στόχος σας αφού πάρετε το πτυχίο ελληνικών Α2;",
        "english": "What is your next goal after you get the A2 Greek certificate? (Examiner Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 (Personal Interview)",
            "focus": "Temporal clause with future reference (αφού πάρω / μόλις πάρω + subjunctive), future aspirations (θα συνεχίσω)"
        },
        "notes": "Examiner Objective: Tests temporal-conditional clauses ('αφού πάρω') and long-term personal/linguistic goals.\nStrategy: Express enthusiasm for continuing to level B1 and applying Greek in your daily/professional life.",
        "example_el": "Αφού πάρω το πτυχίο του επιπέδου Α2, θα συνεχίσω αμέσως τα μαθήματα για το επίπεδο Β1, γιατί θέλω να μιλάω ελληνικά με ακόμα μεγαλύτερη άνεση.",
        "example_en": "After I get the A2 level certificate, I will immediately continue lessons for the B1 level, because I want to speak Greek with even greater fluency.",
        "example2_el": "Μόλις ολοκληρώσω με επιτυχία αυτές τις εξετάσεις, σκοπεύω να χρησιμοποιώ τα ελληνικά καθημερινά στη δουλειά μου και να διαβάζω ελληνική λογοτεχνία χωρίς λεξικό.",
        "example2_en": "As soon as I successfully complete these exams, I plan to use Greek daily in my job and read Greek literature without a dictionary.",
        "keg_communicative_function": "Stating future language-learning and personal development goals"
    },
]


# -------------------------------------------------------------
# UNIT SP-02 CARDS (40 cards: SP-U02-001 .. SP-U02-040)
# Theme: Συνδετικές Εκφράσεις & Διαχείριση Ροής (Conversational Connectors & Fluency Boosters)
# -------------------------------------------------------------
CARDS_U02 = [
    # 001-008: Buying thinking time & managing hesitation
    {
        "id": "SP-U02-001",
        "greek": "Για να σκεφτώ λίγο...",
        "english": "Let me think for a moment... (Spoken Connector / Hesitation Filler)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Spoken Fluency & Interaction)",
            "focus": "Subjunctive particle για να + first-person singular aorist subjunctive (σκεφτώ), adverbial quantifier (λίγο)"
        },
        "notes": "Examiner Objective: Tests interactive competence and natural hesitation management instead of dead silence.\nStrategy: Use immediately when an examiner question catches you off guard to buy 3–4 seconds of thinking time.",
        "example_el": "Για να σκεφτώ λίγο... Νομίζω ότι το πιο όμορφο ταξίδι που έκανα τα τελευταία χρόνια ήταν πέρυσι την άνοιξη στην Κέρκυρα με την οικογένειά μου.",
        "example_en": "Let me think for a moment... I think that the most beautiful trip I took in recent years was last spring to Corfu with my family.",
        "example2_el": "Για να σκεφτώ λίγο... Αν είχα περισσότερο ελεύθερο χρόνο τις καθημερινές, θα ήθελα σίγουρα να μάθω να παίζω ένα μουσικό όργανο.",
        "example2_en": "Let me think for a moment... If I had more free time on weekdays, I would definitely like to learn to play a musical instrument.",
        "keg_communicative_function": "Buying thinking time naturally without breaking conversational flow"
    },
    {
        "id": "SP-U02-002",
        "greek": "Κοιτάξτε, η αλήθεια είναι ότι...",
        "english": "Look, the truth is that... (Spoken Connector / Hesitation Filler)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Spoken Fluency & Interaction)",
            "focus": "Polite imperative discourse marker (κοιτάξτε) + declarative complement clause (η αλήθεια είναι ότι)"
        },
        "notes": "Examiner Objective: Rewards authentic Greek conversational framing when giving an honest or nuanced answer.\nStrategy: Use when your real answer differs from the cliché expectation (e.g., admitting you don't like cooking).",
        "example_el": "Κοιτάξτε, η αλήθεια είναι ότι δεν έχω πολύ ελεύθερο χρόνο τις καθημερινές, γι' αυτό προτιμώ να ξεκουράζομαι στο σπίτι μου το βράδυ.",
        "example_en": "Look, the truth is that I do not have much free time on weekdays, which is why I prefer to rest at home in the evening.",
        "example2_el": "Κοιτάξτε, η αλήθεια είναι ότι στην αρχή φοβόμουν να μιλήσω ελληνικά, αλλά τώρα νιώθω πολύ μεγαλύτερη αυτοπεποίθηση στην καθημερινή μου επικοινωνία.",
        "example2_en": "Look, the truth is that at first I was afraid to speak Greek, but now I feel much greater confidence in my daily communication.",
        "keg_communicative_function": "Introducing a candid personal statement while maintaining spoken fluency"
    },
    {
        "id": "SP-U02-003",
        "greek": "Είναι μια πολύ καλή ερώτηση...",
        "english": "That is a very good question... (Spoken Connector / Hesitation Filler)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Spoken Fluency & Interaction)",
            "focus": "Evaluative noun phrase (μια πολύ καλή ερώτηση) used as a conversational staller in Stage 1 and Stage 3"
        },
        "notes": "Examiner Objective: Demonstrates high communicative poise when responding to abstract Stage 3 follow-up questions.\nStrategy: Pair with 'δεν το είχα σκεφτεί ποτέ έτσι, αλλά...' to transition smoothly into your opinion.",
        "example_el": "Είναι μια πολύ καλή ερώτηση... Δεν το είχα σκεφτεί ποτέ έτσι, αλλά πιστεύω πως η ζωή στην εξοχή είναι πιο υγιεινή για τα παιδιά.",
        "example_en": "That is a very good question... I had never thought about it like that, but I believe life in the countryside is healthier for children.",
        "example2_el": "Είναι μια πολύ καλή ερώτηση... Αν έπρεπε να διαλέξω μόνο μία πόλη στην Ελλάδα για να ζήσω, θα διάλεγα σίγουρα τα Χανιά.",
        "example2_en": "That is a very good question... If I had to choose only one city in Greece to live in, I would definitely choose Chania.",
        "keg_communicative_function": "Acknowledging an examiner question while organizing a thoughtful response"
    },
    {
        "id": "SP-U02-004",
        "greek": "Λοιπόν, εξαρτάται από την περίπτωση...",
        "english": "Well, it depends on the situation... (Spoken Connector / Hesitation Filler)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Spoken Fluency & Interaction)",
            "focus": "Discourse particle (λοιπόν) + deponent verb (εξαρτάται από + accusative) + conditional branching (αν... τότε...)"
        },
        "notes": "Examiner Objective: Shows ability to avoid simplistic yes/no answers by distinguishing two different contexts.\nStrategy: Follow immediately with two contrasting 'όταν' or 'αν' clauses (e.g., winter vs. summer, alone vs. with friends).",
        "example_el": "Λοιπόν, εξαρτάται από την περίπτωση. Όταν είμαι κουρασμένος από τη δουλειά προτιμώ να μένω μέσα, αλλά αν έχω ενέργεια βγαίνω έξω με φίλους.",
        "example_en": "Well, it depends on the situation. When I am tired from work I prefer staying in, but if I have energy I go out with friends.",
        "example2_el": "Λοιπόν, εξαρτάται από την περίπτωση και τον καιρό, γιατί το καλοκαίρι μου αρέσει να ταξιδεύω με πλοίο, ενώ τον χειμώνα προτιμώ το αεροπλάνο.",
        "example2_en": "Well, it depends on the situation and the weather, because in summer I like traveling by ship, whereas in winter I prefer the airplane.",
        "keg_communicative_function": "Nuancing a response by explaining how choices depend on circumstances"
    },
    {
        "id": "SP-U02-005",
        "greek": "Πώς να το πω τώρα με απλά λόγια...",
        "english": "How can I put it now in simple words... (Spoken Connector / Hesitation Filler)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Spoken Fluency & Interaction)",
            "focus": "Deliberative subjunctive question (πώς να το πω) + prepositional manner phrase (με απλά λόγια)"
        },
        "notes": "Examiner Objective: Rewards strategic circumlocution when you cannot recall a difficult word.\nStrategy: Instead of switching to English when stuck on vocabulary, say this phrase and explain the concept using simple A2 words.",
        "example_el": "Πώς να το πω τώρα με απλά λόγια... Είναι ένα μικρό παραδοσιακό μαγαζί στη γειτονιά μου όπου πουλάνε φρέσκο ψωμί, κουλούρια και γλυκά.",
        "example_en": "How can I put it now in simple words... It is a small traditional shop in my neighborhood where they sell fresh bread, koulouria, and sweets.",
        "example2_el": "Πώς να το πω τώρα με απλά λόγια... Νιώθω πολύ μεγάλη χαρά και συγκίνηση κάθε φορά που καταφέρνω να συνεννοηθώ στα ελληνικά χωρίς βοήθεια.",
        "example2_en": "How can I put it now in simple words... I feel great joy and emotion every time I manage to communicate in Greek without help.",
        "keg_communicative_function": "Managing lexical gaps through natural circumlocution"
    },
    {
        "id": "SP-U02-006",
        "greek": "Για να είμαι απόλυτα ειλικρινής...",
        "english": "To be completely honest... (Spoken Connector / Hesitation Filler)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Spoken Fluency & Interaction)",
            "focus": "Purpose/stance clause (για να είμαι) + adverb (απόλυτα) + adjective (ειλικρινής -ής/-ής/-ές)"
        },
        "notes": "Examiner Objective: Demonstrates idiomatic spoken register and grammatical accuracy with '-ής' adjectives.\nStrategy: Note that 'ειλικρινής' is identical for masculine and feminine speakers!",
        "example_el": "Για να είμαι απόλυτα ειλικρινής, δεν ασχολούμαι καθόλου με τον αθλητισμό, αλλά προσπαθώ να περπατάω τουλάχιστον μισή ώρα κάθε μέρα μετά το γραφείο.",
        "example_en": "To be completely honest, I am not involved in sports at all, but I try to walk at least half an hour every day after the office.",
        "example2_el": "Για να είμαι απόλυτα ειλικρινής μαζί σας, προτιμώ τα μικρά ελληνικά νησιά από τις μεγάλες τουριστικές πόλεις, γιατί εκεί ξεκουράζομαι πραγματικά.",
        "example2_en": "To be completely honest with you, I prefer small Greek islands to big tourist cities, because there I truly rest.",
        "keg_communicative_function": "Framing an honest personal admission or preference"
    },
    {
        "id": "SP-U02-007",
        "greek": "Δεν είμαι εντελώς σίγουρος, αλλά νομίζω ότι...",
        "english": "I am not completely sure, but I think that... (Spoken Connector / Hesitation Filler)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Spoken Fluency & Interaction)",
            "focus": "Epistemic hedging (δεν είμαι σίγουρος/σίγουρη) + adversative (αλλά) + cognitive verb (νομίζω ότι)"
        },
        "notes": "Examiner Objective: Essential for Stage 3 (Picture Description) when speculating about where the people are or what is happening.\nStrategy: Feminine speakers should adjust to 'Δεν είμαι εντελώς σίγουρη, αλλά νομίζω ότι...'.",
        "example_el": "Δεν είμαι εντελώς σίγουρος, αλλά νομίζω ότι οι άνθρωποι στη φωτογραφία βρίσκονται σε έναν σταθμό τρένου και περιμένουν να ταξιδέψουν.",
        "example_en": "I am not completely sure, but I think that the people in the photograph are at a train station waiting to travel.",
        "example2_el": "Δεν είμαι εντελώς σίγουρος για την ακριβή τιμή του εισιτηρίου, αλλά νομίζω ότι κοστίζει γύρω στα είκοσι ευρώ με την έκπτωση.",
        "example2_en": "I am not completely sure about the exact ticket price, but I think it costs around twenty euros with the discount.",
        "keg_communicative_function": "Expressing polite uncertainty and making a reasonable guess"
    },
    {
        "id": "SP-U02-008",
        "greek": "Ας δούμε πρώτα τι έχουμε εδώ...",
        "english": "Let's first see what we have here... (Spoken Connector / Hesitation Filler)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 & Stage 3 (Roleplay & Picture Monologue)",
            "focus": "Hortative particle (ας + first plural subjunctive δούμε), temporal adverb (πρώτα)"
        },
        "notes": "Examiner Objective: Perfect opening filler when handed a Stage 2 Roleplay card or Stage 3 Photograph.\nStrategy: Say this aloud with natural intonation while scanning the visual prompt for 2 seconds before launching your description.",
        "example_el": "Ας δούμε πρώτα τι έχουμε εδώ... Στην εικόνα βλέπουμε μια χαρούμενη οικογένεια που τρώει μεσημεριανό φαγητό στον κήπο του σπιτιού της.",
        "example_en": "Let's first see what we have here... In the picture we see a happy family eating lunch in the garden of their house.",
        "example2_el": "Ας δούμε πρώτα τι έχουμε εδώ στην κάρτα... Βλέπω ότι το ταξιδιωτικό γραφείο οργανώνει μια τριήμερη εκδρομή στο Πήλιο αυτό το σαββατοκύριακο.",
        "example2_en": "Let's first see what we have here on the card... I see that the travel agency is organizing a three-day excursion to Pelion this weekend.",
        "keg_communicative_function": "Initiating examination of a cue card or visual prompt aloud"
    },

    # 009-016: Expressing personal views & preferences
    {
        "id": "SP-U02-009",
        "greek": "Κατά τη γνώμη μου...",
        "english": "In my opinion... (Spoken Opinion Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Spoken Fluency & Interaction)",
            "focus": "Prepositional phrase (κατά + accusative: τη γνώμη μου / την άποψή μου)"
        },
        "notes": "Examiner Objective: Tests ability to mark personal viewpoints clearly in Stage 1, 2, and 3.\nStrategy: Rotate 'Κατά τη γνώμη μου' with 'Κατά την άποψή μου' so you do not repeat 'νομίζω' in every sentence.",
        "example_el": "Κατά τη γνώμη μου, ο καλύτερος τρόπος για να μάθει κανείς μια ξένη γλώσσα είναι να μιλάει καθημερινά με τους κατοίκους της χώρας.",
        "example_en": "In my opinion, the best way for someone to learn a foreign language is to speak daily with the residents of the country.",
        "example2_el": "Κατά τη γνώμη μου, τα μέσα μαζικής συγκοινωνίας στην πόλη μας είναι αρκετά καλά, αλλά χρειάζονται περισσότερα δρομολόγια το βράδυ.",
        "example2_en": "In my opinion, public transport in our city is quite good, but more routes are needed at night.",
        "keg_communicative_function": "Introducing a personal opinion on an everyday topic"
    },
    {
        "id": "SP-U02-010",
        "greek": "Προσωπικά πιστεύω πως...",
        "english": "Personally I believe that... (Spoken Opinion Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Spoken Fluency & Interaction)",
            "focus": "Stance adverb (προσωπικά) + verb of belief (πιστεύω) + complementizer (πως / ότι)"
        },
        "notes": "Examiner Objective: Evaluates use of 'πως' as an authentic spoken alternative to 'ότι' after verbs of thinking/believing.\nStrategy: Use 'Προσωπικά πιστεύω πως...' when answering Stage 3 personal extension questions.",
        "example_el": "Προσωπικά πιστεύω πως η υγιεινή διατροφή και ο καλός ύπνος είναι απαραίτητα για να έχουμε ενέργεια και καλή διάθεση όλη την ημέρα.",
        "example_en": "Personally I believe that a healthy diet and good sleep are essential for us to have energy and a good mood all day long.",
        "example2_el": "Προσωπικά πιστεύω πως οι καλοκαιρινές διακοπές σε ένα ήσυχο νησί είναι πολύ πιο ξεκούραστες από ένα ταξίδι σε μια μεγάλη ευρωπαϊκή πρωτεύουσα.",
        "example2_en": "Personally I believe that summer holidays on a quiet island are much more relaxing than a trip to a big European capital.",
        "keg_communicative_function": "Stating a strong personal belief using natural spoken complementizers"
    },
    {
        "id": "SP-U02-011",
        "greek": "Από τη δική μου εμπειρία...",
        "english": "From my own experience... (Spoken Opinion Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 & Stage 3 (Personal Interview & Extension)",
            "focus": "Preposition από + emphatic possessive (τη δική μου εμπειρία), experiential justification"
        },
        "notes": "Examiner Objective: Bridges general exam prompts to concrete personal storytelling (a top KEG A2 rubric booster).\nStrategy: Use this phrase to pivot from an abstract question into a short personal example.",
        "example_el": "Από τη δική μου εμπειρία, όταν μετακομίζεις σε μια καινούργια χώρα, οι γείτονες και οι συνάδελφοι σε βοηθούν πάρα πολύ να προσαρμοστείς.",
        "example_en": "From my own experience, when you move to a new country, neighbors and colleagues help you a great deal to adapt.",
        "example2_el": "Από τη δική μου εμπειρία, τα ψώνια στη λαϊκή αγορά είναι όχι μόνο πιο οικονομικά, αλλά και μια ωραία ευκαιρία για κουβέντα με τους παραγωγούς.",
        "example2_en": "From my own experience, shopping at the farmers' market is not only more economical, but also a nice opportunity to chat with the producers.",
        "keg_communicative_function": "Supporting an opinion with personal life experience"
    },
    {
        "id": "SP-U02-012",
        "greek": "Προτιμώ χίλιες φορές να... παρά να...",
        "english": "I prefer a thousand times to... rather than to... (Spoken Preference Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Spoken Fluency & Interaction)",
            "focus": "Emphatic preference idiom (προτιμώ χίλιες φορές να + subjunctive) + contrastive conjunction (παρά να + subjunctive)"
        },
        "notes": "Examiner Objective: High-scoring idiomatic structure showing natural spoken emphasis and parallel subjunctive clauses.\nStrategy: Keep both verbs in the same aspect (e.g., present subjunctive for general habits).",
        "example_el": "Προτιμώ χίλιες φορές να πηγαίνω στη δουλειά μου με τα πόδια ή με το ποδήλατο, παρά να περιμένω μία ώρα μέσα στην κίνηση με το αυτοκίνητο.",
        "example_en": "I prefer a thousand times to go to work on foot or by bicycle, rather than wait for an hour in traffic by car.",
        "example2_el": "Το καλοκαίρι προτιμώ χίλιες φορές να κολυμπάω στη θάλασσα νωρίς το πρωί, παρά να πηγαίνω στην παραλία το μεσημέρι που έχει πολλή ζέστη.",
        "example2_en": "In summer I prefer a thousand times to swim in the sea early in the morning, rather than go to the beach at noon when it is very hot.",
        "keg_communicative_function": "Expressing strong emphatic preference between two actions"
    },
    {
        "id": "SP-U02-013",
        "greek": "Για εμένα, το πιο σημαντικό πράγμα είναι...",
        "english": "For me, the most important thing is... (Spoken Opinion Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Spoken Fluency & Interaction)",
            "focus": "Prepositional topic front-loading (για εμένα) + superlative neuter phrase (το πιο σημαντικό πράγμα) + noun/clause"
        },
        "notes": "Examiner Objective: Tests superlative adjective structures and prioritization of values/criteria.\nStrategy: Useful in Stage 2 (choosing an apartment/hotel) and Stage 1 (work/neighborhood priorities).",
        "example_el": "Για εμένα, το πιο σημαντικό πράγμα όταν νοικιάζω ένα σπίτι είναι να βρίσκεται κοντά σε σταθμό του μετρό και να έχει καλή θέρμανση.",
        "example_en": "For me, the most important thing when renting a home is that it is located near a metro station and has good heating.",
        "example2_el": "Για εμένα, το πιο σημαντικό πράγμα στη δουλειά δεν είναι μόνο ο καλός μισθός, αλλά και το ευχάριστο κλίμα συνεργασίας με τους συναδέλφους.",
        "example2_en": "For me, the most important thing at work is not only a good salary, but also a pleasant atmosphere of cooperation with colleagues.",
        "keg_communicative_function": "Highlighting personal priorities and evaluation criteria"
    },
    {
        "id": "SP-U02-014",
        "greek": "Μου φαίνεται ότι...",
        "english": "It seems to me that... (Spoken Speculation / Opinion Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Description & Speculation)",
            "focus": "Indirect object clitic (μου) + third-person singular deponent verb (φαίνεται) + declarative clause (ότι / πως)"
        },
        "notes": "Examiner Objective: Key Stage 3 rubric requirement for making hypotheses about people's feelings or situations in a photo.\nStrategy: Use 'Μου φαίνεται ότι...' to interpret facial expressions, weather, or relationships in the picture.",
        "example_el": "Μου φαίνεται ότι η κοπέλα στη φωτογραφία είναι πολύ χαρούμενη, επειδή χαμογελάει πλατιά και κρατάει ένα μεγάλο μπουκέτο με λουλούδια στα χέρια της.",
        "example_en": "It seems to me that the young woman in the photo is very happy, because she is smiling broadly and holding a large bouquet of flowers in her hands.",
        "example2_el": "Μου φαίνεται ότι αυτή η ταβέρνα έχει πολύ καλό φαγητό, γιατί όλα τα τραπέζια είναι γεμάτα με κόσμο και οι πελάτες τρώνε με όρεξη.",
        "example2_en": "It seems to me that this taverna has very good food, because all the tables are full of people and the customers are eating with appetite.",
        "keg_communicative_function": "Expressing impressions and visual hypotheses based on evidence"
    },
    {
        "id": "SP-U02-015",
        "greek": "Από όσο ξέρω...",
        "english": "As far as I know... (Spoken Knowledge Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Spoken Fluency & Interaction)",
            "focus": "Prepositional relative idiom (από όσο ξέρω / από όσο γνωρίζω) for hedging factual statements"
        },
        "notes": "Examiner Objective: Shows natural hedging when sharing factual or practical information in Stage 1 and Stage 2.\nStrategy: Use in Stage 2 roleplays when answering questions about schedules, rules, or local customs.",
        "example_el": "Από όσο ξέρω, τα καταστήματα στην Ελλάδα είναι κλειστά την Κυριακή, εκτός από τα καφέ, τα εστιατόρια και μερικά μικρά μίνι μάρκετ.",
        "example_en": "As far as I know, shops in Greece are closed on Sunday, except for cafes, restaurants, and some small mini-markets.",
        "example2_el": "Από όσο ξέρω, το πλοίο για το νησί αναχωρεί στις επτάμισι το πρωί από το λιμάνι του Πειραιά και το ταξίδι διαρκεί τέσσερις ώρες.",
        "example2_en": "As far as I know, the ferry to the island departs at seven-thirty in the morning from the port of Piraeus and the trip lasts four hours.",
        "keg_communicative_function": "Qualifying factual statements according to one's current knowledge"
    },
    {
        "id": "SP-U02-016",
        "greek": "Δεν έχω ιδιαίτερη προτίμηση, αλλά...",
        "english": "I don't have a strong preference, but... (Spoken Preference Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay & Negotiation)",
            "focus": "Negated verb (δεν έχω) + feminine noun phrase (ιδιαίτερη προτίμηση) + adversative suggestion (αλλά)"
        },
        "notes": "Examiner Objective: Demonstrates cooperative flexibility during Stage 2 partner negotiations.\nStrategy: Show that you are easygoing first ('Δεν έχω ιδιαίτερη προτίμηση'), then gently propose a practical option.",
        "example_el": "Δεν έχω ιδιαίτερη προτίμηση για το εστιατόριο που θα πάμε, αλλά καλό είναι να διαλέξουμε ένα μαγαζί στο κέντρο για να έρθουν όλοι εύκολα.",
        "example_en": "I don't have a strong preference for the restaurant we will go to, but it is good to choose a place in the center so everyone can get there easily.",
        "example2_el": "Δεν έχω ιδιαίτερη προτίμηση ανάμεσα στο Σάββατο και την Κυριακή, αλλά νομίζω ότι την Κυριακή το πρωί θα έχει λιγότερη κίνηση στους δρόμους.",
        "example2_en": "I don't have a strong preference between Saturday and Sunday, but I think that on Sunday morning there will be less traffic on the roads.",
        "keg_communicative_function": "Expressing flexibility while offering a practical suggestion"
    },

    # 017-024: Structuring, contrasting & polishing spoken answers
    {
        "id": "SP-U02-017",
        "greek": "Πρώτα απ' όλα... και δεύτερον...",
        "english": "First of all... and secondly... (Spoken Discourse Organizer)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Spoken Fluency & Interaction)",
            "focus": "Sequential discourse markers (πρώτα απ' όλα / πρώτον ... και δεύτερον / επίσης)"
        },
        "notes": "Examiner Objective: Directly boosts the Discourse Cohesion rubric by organizing multi-reason answers clearly.\nStrategy: Whenever asked 'Γιατί;' (Why?), give two structured reasons using 'Πρώτα απ' όλα...' and 'και δεύτερον...'.",
        "example_el": "Μου αρέσει να ζω σε αυτή τη γειτονιά για δύο λόγους. Πρώτα απ' όλα είναι πολύ ήσυχη και ασφαλής, και δεύτερον βρίσκεται κοντά στη δουλειά μου.",
        "example_en": "I like living in this neighborhood for two reasons. First of all it is very quiet and safe, and secondly it is close to my job.",
        "example2_el": "Προτιμώ να ταξιδεύω με τρένο γιατί, πρώτα απ' όλα, μπορώ να βλέπω το τοπίο από το παράθυρο και, δεύτερον, τα εισιτήρια είναι πιο φθηνά.",
        "example2_en": "I prefer traveling by train because, first of all, I can look at the scenery from the window and, secondly, the tickets are cheaper.",
        "keg_communicative_function": "Structuring spoken arguments in clear sequential order"
    },
    {
        "id": "SP-U02-018",
        "greek": "Από τη μία πλευρά... από την άλλη όμως...",
        "english": "On the one hand... on the other hand, however... (Spoken Contrast Connector)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 & Stage 3 (Balanced Evaluation)",
            "focus": "Correlative contrast markers (από τη μία πλευρά ... από την άλλη όμως)"
        },
        "notes": "Examiner Objective: Shows mature communicative balance by weighing advantages and disadvantages.\nStrategy: Ideal for questions about city vs. village, working from home vs. office, or online vs. in-store shopping.",
        "example_el": "Από τη μία πλευρά η ζωή στη μεγάλη πόλη προσφέρει πολλές ευκαιρίες εργασίας, από την άλλη όμως έχει πολύ θόρυβο, άγχος και ακριβά ενοίκια.",
        "example_en": "On the one hand life in the big city offers many job opportunities, on the other hand, however, it has a lot of noise, stress, and expensive rents.",
        "example2_el": "Από τη μία πλευρά τα ηλεκτρονικά ψώνια είναι πολύ γρήγορα και άνετα, από την άλλη όμως στα ρούχα προτιμώ να τα δοκιμάζω στο κατάστημα.",
        "example2_en": "On the one hand online shopping is very fast and convenient, on the other hand, however, for clothes I prefer trying them on in the store.",
        "keg_communicative_function": "Weighing pros and cons with correlative contrast connectors"
    },
    {
        "id": "SP-U02-019",
        "greek": "Όπως ανέφερα και πριν...",
        "english": "As I mentioned before... (Spoken Cohesion Connector)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Spoken Fluency & Interaction)",
            "focus": "Comparative manner conjunction (όπως) + first-person singular aorist (ανέφερα / είπα) + temporal adverb (πριν)"
        },
        "notes": "Examiner Objective: Demonstrates high-level discourse cohesion by linking later answers back to earlier turns.\nStrategy: Use when an examiner question touches on a detail you already mentioned earlier in the interview.",
        "example_el": "Όπως ανέφερα και πριν, δουλεύω αρκετές ώρες μπροστά στον υπολογιστή, οπότε το απόγευμα χρειάζομαι οπωσδήποτε λίγη κίνηση και καθαρό αέρα στο πάρκο.",
        "example_en": "As I mentioned before, I work quite a few hours in front of the computer, so in the afternoon I definitely need some exercise and fresh air in the park.",
        "example2_el": "Όπως ανέφερα και πριν, τα παιδιά μου είναι ακόμα μικρά, γι' αυτό στις διακοπές μας διαλέγουμε πάντα ξενοδοχεία που βρίσκονται ακριβώς μπροστά στην παραλία.",
        "example2_en": "As I mentioned before, my children are still young, which is why on our vacations we always choose hotels located right in front of the beach.",
        "keg_communicative_function": "Maintaining cohesive links across different parts of a conversation"
    },
    {
        "id": "SP-U02-020",
        "greek": "Εκτός από αυτό, πρέπει να πω ότι...",
        "english": "Besides that, I must say that... (Spoken Additive Connector)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Spoken Fluency & Interaction)",
            "focus": "Prepositional additive phrase (εκτός από αυτό) + modal obligation (πρέπει να πω ότι)"
        },
        "notes": "Examiner Objective: Helps extend short answers into full 25–35 word responses without repeating 'και... και...'.\nStrategy: When you finish your first sentence and realize it was too brief, attach 'Εκτός από αυτό, πρέπει να πω ότι...'.",
        "example_el": "Το διαμέρισμά μας είναι πολύ φωτεινό και ήσυχο. Εκτός από αυτό, πρέπει να πω ότι έχει εξαιρετική θέα στη θάλασσα από το μεγάλο μπαλκόνι.",
        "example_en": "Our apartment is very bright and quiet. Besides that, I must say that it has an excellent view of the sea from the large balcony.",
        "example2_el": "Τα μαθήματα ελληνικών με βοηθούν πολύ στη δουλειά μου. Εκτός από αυτό, πρέπει να πω ότι γνώρισα θαυμάσιους ανθρώπους μέσα στην τάξη μας.",
        "example2_en": "The Greek lessons help me a lot in my job. Besides that, I must say that I met wonderful people in our class.",
        "keg_communicative_function": "Adding supplementary points to expand a spoken response"
    },
    {
        "id": "SP-U02-021",
        "greek": "Με άλλα λόγια...",
        "english": "In other words... (Spoken Reformulation Connector)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Spoken Fluency & Interaction)",
            "focus": "Preposition με + neuter plural noun phrase (άλλα λόγια) used for summarizing or paraphrasing"
        },
        "notes": "Examiner Objective: Evaluates ability to summarize or clarify a point concisely.\nStrategy: Use near the end of your turn to wrap up your main message cleanly.",
        "example_el": "Δουλεύω από το πρωί ως το απόγευμα και το βράδυ έχω μαθήματα. Με άλλα λόγια, το πρόγραμμά μου τις καθημερινές είναι πάρα πολύ γεμάτο.",
        "example_en": "I work from morning till afternoon and in the evening I have lessons. In other words, my schedule on weekdays is very full.",
        "example2_el": "Το ξενοδοχείο είναι καθαρό, οικονομικό και δίπλα στο λιμάνι. Με άλλα λόγια, είναι η καλύτερη επιλογή για τις καλοκαιρινές μας διακοπές.",
        "example2_en": "The hotel is clean, affordable, and right next to the port. In other words, it is the best choice for our summer vacation.",
        "keg_communicative_function": "Reformulating and summarizing a point for clarity"
    },
    {
        "id": "SP-U02-022",
        "greek": "Παρόλο που... εντούτοις...",
        "english": "Even though... nevertheless... (Spoken Concession Connector)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Spoken Fluency & Interaction)",
            "focus": "Concessive conjunction (παρόλο που + indicative) paired with contrastive adverb (εντούτοις / ωστόσο)"
        },
        "notes": "Examiner Objective: Demonstrates upper-A2 syntactic control by subordinating a concession clause.\nStrategy: Remember that 'παρόλο που' takes factual Indicative verbs (not Subjunctive!).",
        "example_el": "Παρόλο που η ελληνική γραμματική έχει αρκετές δυσκολίες, εντούτοις η γλώσσα είναι τόσο όμορφη και μελωδική που μου αρέσει να τη μελετάω κάθε μέρα.",
        "example_en": "Even though Greek grammar has quite a few difficulties, nevertheless the language is so beautiful and melodic that I enjoy studying it every day.",
        "example2_el": "Παρόλο που χθες έβρεχε δυνατά όλο το απόγευμα, εντούτοις πήγαμε κανονικά στο θέατρο με τους φίλους μας και περάσαμε υπέροχα.",
        "example2_en": "Even though it was raining heavily all afternoon yesterday, nevertheless we went to the theater as planned with our friends and had a wonderful time.",
        "keg_communicative_function": "Expressing concession and unexpected contrast in spoken Greek"
    },
    {
        "id": "SP-U02-023",
        "greek": "Για παράδειγμα, πριν από λίγο καιρό...",
        "english": "For example, a little while ago... (Spoken Exemplification Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 1 & Stage 3 (Personal Interview & Narrative Extension)",
            "focus": "Exemplification phrase (για παράδειγμα) + temporal past marker (πριν από λίγο καιρό) + Simple Past (Αόριστος)"
        },
        "notes": "Examiner Objective: Rewards candidates who back up general statements with a short real-life anecdote in the Aorist.\nStrategy: After stating a general habit or opinion, launch a 1-sentence past story with 'Για παράδειγμα, πριν από λίγο καιρό...'.",
        "example_el": "Οι Έλληνες είναι πολύ εξυπηρετικοί με τους ξένους. Για παράδειγμα, πριν από λίγο καιρό χάθηκα σε μια γειτονιά και ένας κύριος με συνόδευσε ως τη στάση.",
        "example_en": "Greeks are very helpful with foreigners. For example, a little while ago I got lost in a neighborhood and a gentleman walked me to the bus stop.",
        "example2_el": "Μου αρέσει να δοκιμάζω καινούργιες δραστηριότητες. Για παράδειγμα, πριν από λίγο καιρό γράφτηκα σε έναν σύλλογο παραδοσιακών ελληνικών χορών στη γειτονιά μου.",
        "example2_en": "I like trying new activities. For example, a little while ago I joined a traditional Greek dance club in my neighborhood.",
        "keg_communicative_function": "Illustrating a general statement with a concrete past example"
    },
    {
        "id": "SP-U02-024",
        "greek": "Συνοψίζοντας λοιπόν, θα έλεγα ότι...",
        "english": "Summarizing then, I would say that... (Spoken Closing Frame)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Picture Monologue & Extended Response)",
            "focus": "Active participle (συνοψίζοντας) + conditional of politeness/moderation (θα έλεγα ότι)"
        },
        "notes": "Examiner Objective: Gives your Stage 3 monologue a polished, unmistakable conclusion instead of trailing off awkwardly.\nStrategy: Use as your final sentence in Stage 3 to sum up the overall mood or message of the photograph.",
        "example_el": "Συνοψίζοντας λοιπόν, θα έλεγα ότι η φωτογραφία μάς δείχνει μια όμορφη οικογενειακή στιγμή γεμάτη αγάπη, χαμόγελα και ηρεμία δίπλα στη θάλασσα.",
        "example_en": "Summarizing then, I would say that the photograph shows us a beautiful family moment full of love, smiles, and tranquility by the sea.",
        "example2_el": "Συνοψίζοντας λοιπόν, θα έλεγα ότι η ζωή στην πόλη μας έχει μεν κάποιες δυσκολίες, αλλά προσφέρει εξαιρετική ποιότητα ζωής και καλό κλίμα.",
        "example2_en": "Summarizing then, I would say that life in our city does have some difficulties, but it offers an excellent quality of life and a good climate.",
        "keg_communicative_function": "Bringing an extended spoken turn or monologue to a structured conclusion"
    },

    # 025-032: Active listening, turn-taking & collaborative agreement/disagreement
    {
        "id": "SP-U02-025",
        "greek": "Συμφωνώ απόλυτα μαζί σας, αλλά...",
        "english": "I completely agree with you, but... (Spoken Interactive Turn-Taking)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay & Negotiation)",
            "focus": "Present tense verb (συμφωνώ) + intensifying adverb (απόλυτα) + comitative phrase (μαζί σας / μαζί σου) + adversative (αλλά)"
        },
        "notes": "Examiner Objective: Core Stage 2 interactive skill—validating your partner's point before introducing a constraint or counter-proposal.\nStrategy: Use 'μαζί σας' in formal roleplays (with an examiner/shopkeeper) or 'μαζί σου' with a peer/friend.",
        "example_el": "Συμφωνώ απόλυτα μαζί σας ότι το ξενοδοχείο στο κέντρο είναι πολύ όμορφο, αλλά νομίζω ότι η τιμή του είναι λίγο ακριβή για εμάς.",
        "example_en": "I completely agree with you that the hotel in the center is very nice, but I think its price is a bit expensive for us.",
        "example2_el": "Συμφωνώ απόλυτα μαζί σας πως η εκδρομή με το πλοίο είναι ωραία ιδέα, αλλά πρέπει πρώτα να ελέγξουμε αν ο καιρός θα είναι καλός.",
        "example2_en": "I completely agree with you that the boat trip is a nice idea, but we must first check whether the weather will be good.",
        "keg_communicative_function": "Expressing partial agreement before introducing a practical reservation"
    },
    {
        "id": "SP-U02-026",
        "greek": "Έχετε απόλυτο δίκιο σε αυτό που λέτε.",
        "english": "You are completely right about what you are saying. (Spoken Agreement Formula)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 & Stage 3 (Interactive Dialogue)",
            "focus": "Idiom έχω δίκιο (έχετε απόλυτο δίκιο) + relative clause (σε αυτό που λέτε)"
        },
        "notes": "Examiner Objective: Rewards natural active listening and enthusiastic agreement during collaborative tasks.\nStrategy: Follow up by adding one extra supporting detail so you advance the dialogue rather than stopping at 'yes'.",
        "example_el": "Έχετε απόλυτο δίκιο σε αυτό που λέτε. Αν κλείσουμε τα εισιτήριά μας ηλεκτρονικά από σήμερα, θα κερδίσουμε και είκοσι τοις εκατό έκπτωση.",
        "example_en": "You are completely right about what you are saying. If we book our tickets online starting today, we will also get a twenty percent discount.",
        "example2_el": "Έχετε απόλυτο δίκιο σε αυτό που λέτε, γιατί το Σάββατο το βράδυ το εστιατόριο έχει πάντα πολύ κόσμο και χρειάζεται οπωσδήποτε κράτηση.",
        "example2_en": "You are completely right about what you are saying, because on Saturday night the restaurant is always very crowded and definitely requires a reservation.",
        "keg_communicative_function": "Validating an interlocutor's point warmly and building upon it"
    },
    {
        "id": "SP-U02-027",
        "greek": "Καταλαβαίνω τι εννοείτε, όμως εγώ νομίζω ότι...",
        "english": "I understand what you mean, however I think that... (Spoken Polite Disagreement)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay & Negotiation)",
            "focus": "Cognitive verb (καταλαβαίνω) + indirect question (τι εννοείτε) + contrastive conjunction (όμως) + emphatic pronoun (εγώ)"
        },
        "notes": "Examiner Objective: Tests polite, non-confrontational disagreement during Stage 2 problem-solving.\nStrategy: Never say a blunt 'Όχι, κάνετε λάθος'; use this cushioned formula to propose an alternative.",
        "example_el": "Καταλαβαίνω τι εννοείτε για το κόστος, όμως εγώ νομίζω ότι αξίζει να πληρώσουμε λίγο παραπάνω για να έχουμε ένα διαμέρισμα με αυτόνομη θέρμανση.",
        "example_en": "I understand what you mean about the cost, however I think that it is worth paying a little extra so we have an apartment with independent heating.",
        "example2_el": "Καταλαβαίνω τι εννοείτε, όμως εγώ νομίζω ότι είναι καλύτερα να αγοράσουμε ένα πρακτικό δώρο για το σπίτι τους παρά απλώς λουλούδια.",
        "example2_en": "I understand what you mean, however I think that it is better to buy a practical gift for their home rather than just flowers.",
        "keg_communicative_function": "Disagreeing diplomatically and offering an alternative viewpoint"
    },
    {
        "id": "SP-U02-028",
        "greek": "Εσείς τι γνώμη έχετε γι' αυτό; Συμφωνείτε;",
        "english": "What is your opinion on this? Do you agree? (Spoken Turn-Giving Formula)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay & Collaborative Planning)",
            "focus": "Emphatic second-person pronoun (εσείς / εσύ) + interrogative phrase (τι γνώμη έχετε γι' αυτό)"
        },
        "notes": "Examiner Objective: Criterion 5 (Interactive Competence) specifically rewards candidates who actively invite their partner to speak.\nStrategy: End your proposal in Stage 2 with this question to pass the turn smoothly to your partner.",
        "example_el": "Εγώ προτείνω να πάμε στην παράσταση του Σαββάτου στις εννέα το βράδυ και μετά να φάμε σε μια ταβέρνα. Εσείς τι γνώμη έχετε γι' αυτό; Συμφωνείτε;",
        "example_en": "I suggest we go to Saturday's performance at nine in the evening and eat at a taverna afterwards. What is your opinion on this? Do you agree?",
        "example2_el": "Νομίζω ότι το μπλε πουκάμισο είναι πιο κομψό και ταιριάζει καλύτερα για τη γιορτή. Εσείς τι γνώμη έχετε γι' αυτό; Συμφωνείτε;",
        "example2_en": "I think that the blue shirt is more elegant and suits the celebration better. What is your opinion on this? Do you agree?",
        "keg_communicative_function": "Inviting the interlocutor's opinion and managing turn-taking"
    },
    {
        "id": "SP-U02-029",
        "greek": "Αυτή είναι μια εξαιρετική ιδέα! Ας το κάνουμε έτσι.",
        "english": "That is an excellent idea! Let's do it that way. (Spoken Consensus Formula)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay Resolution)",
            "focus": "Demonstrative (αυτή) + evaluative noun phrase (μια εξαιρετική ιδέα) + hortative subjunctive (ας το κάνουμε έτσι)"
        },
        "notes": "Examiner Objective: Every Stage 2 roleplay must reach a clear agreement or resolution before the 5 minutes end.\nStrategy: Use this phrase at the end of the roleplay to seal the deal and summarize the final plan.",
        "example_el": "Αυτή είναι μια εξαιρετική ιδέα! Ας το κάνουμε έτσι λοιπόν, θα κλείσω εγώ το τραπέζι στην ταβέρνα και εσείς θα αγοράσετε την τούρτα.",
        "example_en": "That is an excellent idea! Let's do it that way then: I will book the table at the taverna and you will buy the cake.",
        "example2_el": "Αυτή είναι μια εξαιρετική ιδέα! Ας το κάνουμε έτσι και ας συναντηθούμε αύριο στις δέκα το πρωί έξω από τον σταθμό του μετρό.",
        "example2_en": "That is an excellent idea! Let's do it that way and let's meet tomorrow at ten in the morning outside the metro station.",
        "keg_communicative_function": "Confirming mutual agreement and finalizing a shared plan"
    },
    {
        "id": "SP-U02-030",
        "greek": "Μήπως θα ήταν καλύτερα να...;",
        "english": "Perhaps it would be better if we...? (Spoken Polite Counter-Proposal)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay & Problem Solving)",
            "focus": "Polite interrogative particle (μήπως) + conditional comparative (θα ήταν καλύτερα να + plural subjunctive)"
        },
        "notes": "Examiner Objective: Tests polite modal/conditional structures when proposing an alternative date, time, or solution.\nStrategy: Much more polite and higher-scoring than saying 'Πρέπει να...' during a negotiation.",
        "example_el": "Επειδή την Παρασκευή το απόγευμα έχω μάθημα ελληνικών, μήπως θα ήταν καλύτερα να κανονίσουμε τη συνάντησή μας για το Σάββατο το πρωί;",
        "example_en": "Because on Friday afternoon I have a Greek lesson, perhaps it would be better if we arranged our meeting for Saturday morning?",
        "example2_el": "Μήπως θα ήταν καλύτερα να πάρουμε το μετρό αντί για το αυτοκίνητο, ώστε να μη χάσουμε χρόνο ψάχνοντας για θέση στάθμευσης στο κέντρο;",
        "example2_en": "Perhaps it would be better if we took the metro instead of the car, so that we do not waste time looking for a parking space in the center?",
        "keg_communicative_function": "Making a tentative, polite counter-proposal in dialogue"
    },
    {
        "id": "SP-U02-031",
        "greek": "Φοβάμαι πως αυτό είναι λίγο δύσκολο, γιατί...",
        "english": "I am afraid that this is a bit difficult, because... (Spoken Polite Refusal)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay & Scheduling)",
            "focus": "Polite hedging verb (φοβάμαι πως / ότι) + softened adjective (λίγο δύσκολο) + causal justification (γιατί)"
        },
        "notes": "Examiner Objective: Evaluates diplomatic refusal when your roleplay cue card says you are busy at a certain time.\nStrategy: State the polite refusal ('Φοβάμαι πως...'), give the reason from your card, and immediately offer another slot.",
        "example_el": "Φοβάμαι πως αυτό είναι λίγο δύσκολο για εμένα την Τρίτη το πρωί, γιατί εργάζομαι στο γραφείο μέχρι τις τέσσερις το απόγευμα.",
        "example_en": "I am afraid that this is a bit difficult for me on Tuesday morning, because I work at the office until four in the afternoon.",
        "example2_el": "Φοβάμαι πως αυτό είναι λίγο δύσκολο, γιατί το διαμέρισμα στον πρώτο όροφο νοικιάστηκε χθες, αλλά έχουμε ένα άλλο στον τρίτο όροφο.",
        "example2_en": "I am afraid that this is a bit difficult, because the apartment on the first floor was rented yesterday, but we have another one on the third floor.",
        "keg_communicative_function": "Declining a proposal politely and explaining the constraint"
    },
    {
        "id": "SP-U02-032",
        "greek": "Αν δεν έχετε αντίρρηση, προτείνω να...",
        "english": "If you have no objection, I suggest that we... (Spoken Polite Proposal)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay & Service Encounters)",
            "focus": "Conditional politeness formula (αν δεν έχετε αντίρρηση) + verb of proposal (προτείνω να + subjunctive)"
        },
        "notes": "Examiner Objective: Demonstrates formal courtesy and collaborative initiative in Stage 2 roleplays.\nStrategy: Use when proposing how to split tasks or resolve a customer service issue.",
        "example_el": "Αν δεν έχετε αντίρρηση, προτείνω να μοιράσουμε τις δουλειές για τη γιορτή, ώστε να ετοιμάσουμε τα πάντα γρήγορα και χωρίς καθόλου άγχος.",
        "example_en": "If you have no objection, I suggest that we divide the tasks for the party so that we prepare everything quickly and without any stress.",
        "example2_el": "Αν δεν έχετε αντίρρηση, προτείνω να έρθω στο γραφείο σας αύριο στις έντεκα το πρωί για να υπογράψουμε το συμβόλαιο του σπιτιού.",
        "example2_en": "If you have no objection, I suggest that I come to your office tomorrow at eleven in the morning to sign the house contract.",
        "keg_communicative_function": "Proposing a course of action with formal politeness"
    },

    # 033-040: Asking for clarification, repetition & self-correction
    {
        "id": "SP-U02-033",
        "greek": "Με συγχωρείτε, τι εννοείτε με αυτό;",
        "english": "Excuse me, what do you mean by that? (Spoken Clarification Request)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Interactive Repair & Clarification)",
            "focus": "Polite apology formula (με συγχωρείτε) + interrogative clarification (τι εννοείτε με αυτό)"
        },
        "notes": "Examiner Objective: Criterion 5 explicitly rewards candidates who ask for clarification instead of guessing blindly when they miss a word.\nStrategy: Never freeze or answer the wrong question—politely ask the examiner what they mean!",
        "example_el": "Με συγχωρείτε, τι εννοείτε με αυτό; Ρωτάτε για τις καθημερινές μου συνήθειες στη δουλειά ή για το τι κάνω στον ελεύθερό μου χρόνο;",
        "example_en": "Excuse me, what do you mean by that? Are you asking about my daily habits at work or about what I do in my free time?",
        "example2_el": "Με συγχωρείτε, τι εννοείτε με αυτό όταν λέτε ότι η τιμή περιλαμβάνει ημιδιατροφή; Περιλαμβάνει δηλαδή και το πρωινό και το βραδινό γεύμα;",
        "example2_en": "Excuse me, what do you mean by that when you say the price includes half-board? Does that mean it includes both breakfast and dinner?",
        "keg_communicative_function": "Requesting clarification of an unfamiliar term or ambiguous question"
    },
    {
        "id": "SP-U02-034",
        "greek": "Μπορείτε να μου το εξηγήσετε λίγο διαφορετικά, παρακαλώ;",
        "english": "Can you explain it to me a little differently, please? (Spoken Clarification Request)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Interactive Repair & Clarification)",
            "focus": "Modal verb (μπορείτε να) + double clitic pronouns (μου το) + aorist subjunctive (εξηγήσετε) + manner adverb (διαφορετικά)"
        },
        "notes": "Examiner Objective: Shows command of double clitic pronoun order (indirect 'μου' + direct 'το' before the verb).\nStrategy: If the examiner uses a word you don't know, ask them to rephrase it ('να μου το εξηγήσετε λίγο διαφορετικά') rather than just repeating the same word.",
        "example_el": "Συγγνώμη, δεν κατάλαβα την τελευταία λέξη που είπατε. Μπορείτε να μου το εξηγήσετε λίγο διαφορετικά, παρακαλώ, για να σας απαντήσω σωστά;",
        "example_en": "Sorry, I did not understand the last word you said. Can you explain it to me a little differently, please, so I can answer you correctly?",
        "example2_el": "Δεν είμαι σίγουρος ότι κατάλαβα καλά την ερώτηση. Μπορείτε να μου το εξηγήσετε λίγο διαφορετικά ή με πιο απλά λόγια, παρακαλώ;",
        "example2_en": "I am not sure I understood the question well. Can you explain it to me a little differently or in simpler words, please?",
        "keg_communicative_function": "Asking an interlocutor to paraphrase or simplify a question"
    },
    {
        "id": "SP-U02-035",
        "greek": "Μήπως μπορείτε να το επαναλάβετε λίγο πιο αργά;",
        "english": "Could you perhaps repeat it a little more slowly? (Spoken Repetition Request)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Interactive Repair & Clarification)",
            "focus": "Polite interrogative (μήπως μπορείτε να) + object clitic (το) + aorist subjunctive (επαναλάβετε) + comparative adverb (πιο αργά)"
        },
        "notes": "Examiner Objective: Essential survival formula when the interlocutor speaks too fast.\nStrategy: Notice the irregular Aorist Subjunctive 'να το επαναλάβετε' (from επαναλαμβάνω) with stress on '-λά-'.",
        "example_el": "Με συγχωρείτε, δεν σας άκουσα πολύ καλά. Μήπως μπορείτε να το επαναλάβετε λίγο πιο αργά, παρακαλώ, ιδιαίτερα το πρώτο μέρος της ερώτησης;",
        "example_en": "Excuse me, I did not hear you very well. Could you perhaps repeat it a little more slowly, please, especially the first part of the question?",
        "example2_el": "Μήπως μπορείτε να το επαναλάβετε λίγο πιο αργά, παρακαλώ, για να σημειώσω σωστά την ώρα αναχώρησης και τον αριθμό του τηλεφώνου σας;",
        "example2_en": "Could you perhaps repeat it a little more slowly, please, so that I can write down the departure time and your phone number correctly?",
        "keg_communicative_function": "Requesting slower repetition when speech is too rapid"
    },
    {
        "id": "SP-U02-036",
        "greek": "Μάλλον δεν το είπα σωστά, εννοούσα ότι...",
        "english": "I probably didn't say that right, I meant that... (Spoken Self-Correction Formula)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Self-Repair & Accuracy)",
            "focus": "Probability adverb (μάλλον) + negated Aorist (δεν το είπα σωστά) + Imperfect of εννοώ (εννοούσα ότι)"
        },
        "notes": "Examiner Objective: Self-correction counts positively toward Grammatical & Lexical Accuracy if done smoothly.\nStrategy: When you realize you used the wrong tense or word, don't panic—use this bridge and state the corrected version.",
        "example_el": "Πήγαμε στην Κρήτη τον επόμενο μήνα... Μάλλον δεν το είπα σωστά, εννοούσα ότι θα πάμε στην Κρήτη τον επόμενο μήνα για διακοπές.",
        "example_en": "We went to Crete next month... I probably didn't say that right, I meant that we will go to Crete next month for vacation.",
        "example2_el": "Μάλλον δεν το είπα σωστά πριν, εννοούσα ότι το διαμέρισμα βρίσκεται στον δεύτερο όροφο της πολυκατοικίας και όχι στο ισόγειο.",
        "example2_en": "I probably didn't say that right earlier; I meant that the apartment is on the second floor of the apartment building and not on the ground floor.",
        "keg_communicative_function": "Performing smooth self-correction of a grammatical or factual slip"
    },
    {
        "id": "SP-U02-037",
        "greek": "Δεν θυμάμαι την ακριβή λέξη στα ελληνικά, αλλά είναι...",
        "english": "I don't remember the exact word in Greek, but it is... (Spoken Circumlocution Formula)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Lexical Repair & Circumlocution)",
            "focus": "Negated cognitive verb (δεν θυμάμαι) + accusative object (την ακριβή λέξη) + relative definition (ένα αντικείμενο που / ένας άνθρωπος που)"
        },
        "notes": "Examiner Objective: Directly prevents code-switching into English during Stage 3 picture description when you forget a specific noun.\nStrategy: Describe the object's function ('είναι αυτό που χρησιμοποιούμε για να...') or person's role.",
        "example_el": "Δεν θυμάμαι την ακριβή λέξη στα ελληνικά, αλλά είναι αυτό το μεγάλο όχημα που μεταφέρει τα έπιπλα όταν μετακομίζουμε σε καινούργιο σπίτι.",
        "example_en": "I don't remember the exact word in Greek, but it is that large vehicle that transports furniture when we move to a new house.",
        "example2_el": "Δεν θυμάμαι την ακριβή λέξη στα ελληνικά, αλλά είναι το κατάστημα στη γειτονιά όπου πηγαίνουμε για να αγοράσουμε φρέσκα λουλούδια και φυτά.",
        "example2_en": "I don't remember the exact word in Greek, but it is the shop in the neighborhood where we go to buy fresh flowers and plants.",
        "keg_communicative_function": "Overcoming a forgotten vocabulary item through functional description"
    },
    {
        "id": "SP-U02-038",
        "greek": "Αν κατάλαβα καλά, με ρωτάτε αν...",
        "english": "If I understood correctly, you are asking me whether... (Spoken Comprehension Check)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "All Stages (Interactive Comprehension Verification)",
            "focus": "Conditional clause in Aorist (αν κατάλαβα καλά) + reporting verb (με ρωτάτε) + indirect question particle (αν / πώς / γιατί)"
        },
        "notes": "Examiner Objective: Shows active listening and confirms comprehension before launching into a long answer.\nStrategy: Also buys you extra time to structure your grammar while echoing the examiner's question.",
        "example_el": "Αν κατάλαβα καλά, με ρωτάτε αν προτιμώ να διαβάζω έντυπες εφημερίδες ή να ενημερώνομαι από το διαδίκτυο. Εγώ προτιμώ σίγουρα το διαδίκτυο.",
        "example_en": "If I understood correctly, you are asking me whether I prefer reading printed newspapers or getting news from the internet. I definitely prefer the internet.",
        "example2_el": "Αν κατάλαβα καλά, θέλετε να μάθετε ποιες είναι οι τιμές των δωματίων μας για τον μήνα Αύγουστο και αν υπάρχει ελεύθερο πάρκινγκ.",
        "example2_en": "If I understood correctly, you want to find out what our room rates are for the month of August and whether there is free parking.",
        "keg_communicative_function": "Verifying comprehension of an interlocutor's question before answering"
    },
    {
        "id": "SP-U02-039",
        "greek": "Δηλαδή, θέλετε να πείτε ότι...",
        "english": "That is to say, do you mean that...? (Spoken Confirmation & Paraphrase)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 (Bilateral Roleplay & Information Exchange)",
            "focus": "Explanatory adverb (δηλαδή) + modal phrase (θέλετε να πείτε ότι) for checking details"
        },
        "notes": "Examiner Objective: Useful in Stage 2 when confirming conditions, schedules, or prices stated by your partner.\nStrategy: Use with rising question intonation to verify a crucial detail on the cue card.",
        "example_el": "Δηλαδή, θέλετε να πείτε ότι το γυμναστήριο είναι ανοιχτό μόνο τις καθημερινές και ότι το σαββατοκύριακο δεν γίνονται καθόλου ομαδικά μαθήματα;",
        "example_en": "That is to say, do you mean that the gym is open only on weekdays and that on the weekend no group classes take place at all?",
        "example2_el": "Δηλαδή, θέλετε να πείτε ότι αν πληρώσω όλο το ποσό σήμερα με κάρτα, η παράδοση των επίπλων στο σπίτι μου θα είναι δωρεάν;",
        "example2_en": "That is to say, do you mean that if I pay the full amount today by card, the delivery of the furniture to my home will be free?",
        "keg_communicative_function": "Confirming the implications of information received in dialogue"
    },
    {
        "id": "SP-U02-040",
        "greek": "Σας ευχαριστώ πολύ για τη βοήθεια και τις πληροφορίες!",
        "english": "Thank you very much for the help and the information! (Spoken Polite Closing)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 & Exam Conclusion (Polite Social Closing)",
            "focus": "Formal gratitude verb (σας ευχαριστώ πολύ) + causal preposition (για + accusative: τη βοήθεια και τις πληροφορίες)"
        },
        "notes": "Examiner Objective: Every Stage 2 service roleplay (travel agency, pharmacy, real estate, shop) should end with a polite closing formula.\nStrategy: Pair with 'Καλή συνέχεια και καλή σας μέρα!' to end your roleplay with natural Greek courtesy.",
        "example_el": "Σας ευχαριστώ πολύ για τη βοήθεια και τις πληροφορίες! Θα το συζητήσω το βράδυ με τη σύζυγό μου και θα σας τηλεφωνήσω αύριο το πρωί.",
        "example_en": "Thank you very much for the help and the information! I will discuss it tonight with my wife and call you tomorrow morning.",
        "example2_el": "Σας ευχαριστώ πολύ για τη βοήθεια και τις πληροφορίες σχετικά με τα δρομολόγια! Να είστε καλά και σας εύχομαι μια όμορφη συνέχεια!",
        "example2_en": "Thank you very much for the help and the information regarding the routes! Be well and I wish you a pleasant rest of your day!",
        "keg_communicative_function": "Closing a service encounter or formal dialogue with polite gratitude"
    },
]


def synthesize_item(text: str, filename: str) -> bool:
    """Helper to synthesize a single audio string if missing, with retry on 429."""
    p = AUDIO_DIR / filename
    if p.exists() and p.stat().st_size > 0:
        return False
    for attempt in range(5):
        try:
            b = synthesize_greek_chirp(text)
            with open(p, "wb") as f_out:
                f_out.write(b)
            return True
        except Exception as e:
            if "429" in str(e) and attempt < 4:
                time.sleep(3.0 * (attempt + 1))
                continue
            print(f"  [ERROR] {filename} ('{text}'): {e}")
            return False
    return False


def process_unit(
    unit_id: str,
    lesson_id: str,
    title: str,
    description: str,
    lesson_notes: str,
    cards: list,
    order_code: str,
):
    print(f"\n>>> Processing {unit_id} ({order_code}) - {len(cards)} cards ...")
    unit_dir = CONTENT_DIR / unit_id
    unit_dir.mkdir(parents=True, exist_ok=True)
    yaml_file = unit_dir / f"{lesson_id}.yaml"
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)

    tasks = []
    for c in cards:
        c["greek"] = nfc(c["greek"])
        c["example_el"] = nfc(c["example_el"])
        c["example2_el"] = nfc(c["example2_el"])
        c["gender_or_pos"] = "speaking-drill"
        c["status"] = "verified"

        # Greek headword
        fn_greek = generate_audio_filename(c["greek"])
        c["audio"] = fn_greek
        tasks.append((c["greek"], fn_greek))

        # Ex 1
        fn_ex1 = generate_audio_filename(c["example_el"])
        c["example_audio"] = fn_ex1
        tasks.append((c["example_el"], fn_ex1))

        # Ex 2
        fn_ex2 = generate_audio_filename(c["example2_el"])
        c["example2_audio"] = fn_ex2
        tasks.append((c["example2_el"], fn_ex2))

    print(
        f"  Synthesizing audio for {len(tasks)} items using ThreadPoolExecutor(max_workers=6)..."
    )
    synthesized_count = 0
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = {
            executor.submit(synthesize_item, text, fn): fn for text, fn in tasks
        }
        for future in as_completed(futures):
            if future.result():
                synthesized_count += 1

    print(f"  [TTS] Synthesized {synthesized_count} new audio files for {unit_id}.")

    lesson_data = {
        "unit_id": unit_id,
        "lesson_id": lesson_id,
        "title": nfc(title),
        "description": description,
        "lesson_status": "not_started",
        "lesson_notes": nfc(lesson_notes),
        "entries": cards,
    }

    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(
            lesson_data,
            f,
            allow_unicode=True,
            sort_keys=False,
            default_flow_style=False,
        )

    print(f"  [YAML] Saved {yaml_file}")


def main():
    print("=========================================================")
    print("Generating KEG-A2 Speaking Curriculum: Batch 1 (SP-01/02)")
    print("=========================================================")

    u01_notes = """Module SP-01 Core Notes: Προσωπική Συνέντευξη & Ζέσταμα (Stage 1 Examiner Q&A Drills)
• Official KEG A2 Exam Alignment (Stage 1 — ~2–3 minutes):
  - Covers all 5 personal interview domains: Personal identity & family (001–008), Daily routine & work/studies (009–016), Free time & weekend habits (017–024), Home & neighborhood life (025–032), and Why Greek? / Travel / Future goals (033–040).
  - High-Score Strategy: Avoid one-word or bare 3-word replies. Answer using the Rule of Three: Direct Answer + Reason/Connector (γιατί, επειδή, όταν, αλλά) + Concrete Detail."""

    process_unit(
        unit_id="unit-sp-01",
        lesson_id="lesson-01",
        title="Προφορικά SP-01: Προσωπική Συνέντευξη & Ζέσταμα (Stage 1 Examiner Q&A Drills)",
        description="40 rapid examiner question-and-answer drills for Stage 1 of the KEG A2 Speaking exam: personal identity, family, daily routine, work/studies, weekend habits, hobbies, neighborhood, and motivation for learning Greek.",
        lesson_notes=u01_notes,
        cards=CARDS_U01,
        order_code="SP-01-A",
    )

    u02_notes = """Module SP-02 Core Notes: Συνδετικές Εκφράσεις & Διαχείριση Ροής (Conversational Connectors & Fluency Boosters)
• Official KEG A2 Exam Alignment (All 3 Stages — Criterion 1 & Criterion 5):
  - Eliminates silent freezes with automatic Greek hesitation fillers (001–008), personal opinion frames (009–016), discourse structuring & contrast connectors (017–024), collaborative turn-taking & polite agreement/disagreement (025–032), and repair/clarification formulas (033–040).
  - High-Score Strategy: Use natural spoken Greek repair formulas instead of switching to English when you need a moment to think or need a question repeated."""

    process_unit(
        unit_id="unit-sp-02",
        lesson_id="lesson-01",
        title="Προφορικά SP-02: Συνδετικές Εκφράσεις & Διαχείριση Ροής (Conversational Connectors & Fluency Boosters)",
        description="40 high-frequency spoken connectors, hesitation managers, opinion frames, active listening tokens, and polite clarification formulas to eliminate silent freezes across all 3 stages of the KEG A2 Speaking exam.",
        lesson_notes=u02_notes,
        cards=CARDS_U02,
        order_code="SP-02-A",
    )

    print("\n[OK] Speaking Batch 1 (unit-sp-01 & unit-sp-02) finished successfully!")


if __name__ == "__main__":
    main()

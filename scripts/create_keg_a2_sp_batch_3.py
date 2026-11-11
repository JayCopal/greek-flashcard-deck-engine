# -*- coding: utf-8 -*-
"""
Generate KEG-A2 Speaking Examination Curriculum — Batch 3:
- Unit SP-05 (SP-05-A): 40 cards — Stage 3 Examiner Extension Questions & Multi-Tense Storytelling
- Unit SP-06 (SP-06-A): 40 cards — Spoken Phonology, Intonation & Morphological Trap Drills
Includes dual spoken model responses and multi-threaded Google Cloud Chirp-3 HD TTS synthesis.
Note: Does NOT modify content/manifest.yaml (managed by parent coordinator).
"""
import sys
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

# ---------------------------------------------------------------------------
# UNIT SP-05 CARDS (40 cards: SP-U05-001 .. SP-U05-040)
# Theme: Ερωτήσεις Επέκτασης & Προσωπική Εμπειρία (Stage 3 Extension Questions)
# ---------------------------------------------------------------------------
CARDS_SP_05 = [
    # --- 001–008: Holidays, Travel & Island/Summer Experiences ---
    {
        "id": "SP-U05-001",
        "greek": "Εσείς πώς περνάτε συνήθως τις καλοκαιρινές διακοπές σας;",
        "english": "How do you usually spend your summer holidays? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Habitual Present tense, summer leisure collocations, time connectors (συνήθως, κάθε καλοκαίρι)"
        },
        "notes": "Examiner Objective: Bridges a summer/island photograph to candidate's personal holiday habits.\nStrategy: Combine location + daily activities + social companions.",
        "keg_communicative_function": "Describing habitual summer holiday routines and leisure activities",
        "example_el": "Κάθε καλοκαίρι πηγαίνω για δέκα μέρες σε ένα ελληνικό νησί με την οικογένειά μου, όπου κολυμπάμε στη θάλασσα και τρώμε φρέσκο ψάρι.",
        "example_en": "Every summer I go for ten days to a Greek island with my family, where we swim in the sea and eat fresh fish.",
        "example2_el": "Συνήθως προτιμώ να περνάω τις διακοπές μου σε ένα ήσυχο παραθαλάσσιο χωριό, γιατί θέλω να ξεκουράζομαι μακριά από τη φασαρία της πόλης.",
        "example2_en": "Usually I prefer to spend my holidays in a quiet seaside village, because I want to rest far from the noise of the city."
    },
    {
        "id": "SP-U05-002",
        "greek": "Ποιο είναι το πιο ωραίο ταξίδι που κάνατε τα τελευταία χρόνια;",
        "english": "What is the nicest trip you have taken in recent years? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Superlative adjectives (το πιο ωραίο) + Aorist narrative (πήγα, είδα, δοκίμασα, πέρασα)"
        },
        "notes": "Examiner Objective: Tests ability to narrate a specific past experience using Aorist verbs.\nStrategy: State when and where you went, what you saw, and why it was memorable.",
        "keg_communicative_function": "Narrating a memorable past travel experience with descriptive detail",
        "example_el": "Το πιο ωραίο ταξίδι που έκανα ήταν πέρσι την άνοιξη στην Κρήτη, όπου επισκέφτηκα παραδοσιακά χωριά και δοκίμασα υπέροχα τοπικά φαγητά.",
        "example_en": "The nicest trip I took was last spring to Crete, where I visited traditional villages and tried wonderful local foods.",
        "example2_el": "Πριν από δύο χρόνια πήγα στη Θεσσαλονίκη με τους φίλους μου, περπατήσαμε στην παραλία και περάσαμε αξέχαστα.",
        "example2_en": "Two years ago I went to Thessaloniki with my friends, we walked along the waterfront and had an unforgettable time."
    },
    {
        "id": "SP-U05-003",
        "greek": "Προτιμάτε να ταξιδεύετε με πλοίο ή με αεροπλάνο; Γιατί;",
        "english": "Do you prefer to travel by ship or by airplane? Why? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Preference verbs (προτιμώ να + imperfective subjunctive), causal clauses (επειδή, γιατί) and comparisons"
        },
        "notes": "Examiner Objective: Evaluates comparative reasoning after describing a ferry port or airport picture.\nStrategy: State clear preference and give two concrete reasons (speed vs. relaxation/view).",
        "keg_communicative_function": "Expressing and justifying transport preferences with comparative structures",
        "example_el": "Προτιμώ να ταξιδεύω με πλοίο όταν έχω ελεύθερο χρόνο, επειδή μου αρέσει να κάθομαι στο κατάστρωμα και να βλέπω τη θάλασσα.",
        "example_en": "I prefer to travel by ship when I have free time, because I like sitting on the deck and looking at the sea.",
        "example2_el": "Για μακρινά ταξίδια επιλέγω πάντα το αεροπλάνο, γιατί είναι πολύ πιο γρήγορο και άνετο από τα άλλα μέσα μεταφοράς.",
        "example2_en": "For long trips I always choose the airplane, because it is much faster and more comfortable than other means of transport."
    },
    {
        "id": "SP-U05-004",
        "greek": "Όταν πηγαίνετε διακοπές, προτιμάτε να μένετε σε ξενοδοχείο ή σε ενοικιαζόμενο δωμάτιο;",
        "english": "When you go on holiday, do you prefer staying in a hotel or a rented room? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Accommodation vocabulary, temporal/conditional clauses (όταν πηγαίνω, αν ταξιδεύω)"
        },
        "notes": "Examiner Objective: Tests accommodation vocabulary and practical justification.\nStrategy: Mention amenities like breakfast (`πρωινό`), kitchen (`κουζίνα`), or cost (`οικονομικό`).",
        "keg_communicative_function": "Comparing holiday accommodation options and explaining practical advantages",
        "example_el": "Συνήθως προτιμώ να μένω σε ένα μικρό ξενοδοχείο που προσφέρει πρωινό, για να μη χρειάζεται να μαγειρεύω στις διακοπές μου.",
        "example_en": "Usually I prefer to stay in a small hotel that offers breakfast, so that I don't need to cook on my holidays.",
        "example2_el": "Όταν ταξιδεύω με όλη την οικογένεια, νοικιάζουμε ένα διαμέρισμα με κουζίνα, γιατί είναι πιο οικονομικό και έχουμε περισσότερο χώρο.",
        "example2_en": "When I travel with the whole family, we rent an apartment with a kitchen, because it is more economical and we have more space."
    },
    {
        "id": "SP-U05-005",
        "greek": "Σας αρέσει περισσότερο το βουνό ή η θάλασσα για εκδρομές; Γιατί;",
        "english": "Do you like the mountains or the sea more for excursions? Why? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Impersonal verb αρέσει (μου αρέσει περισσότερο), seasonal contrast (το καλοκαίρι vs. τον χειμώνα)"
        },
        "notes": "Examiner Objective: Assesses nature/landscape vocabulary and seasonal linking.\nStrategy: Contrast summer seaside activities with winter mountain trips.",
        "keg_communicative_function": "Comparing natural environments and seasonal excursion preferences",
        "example_el": "Το καλοκαίρι μου αρέσει περισσότερο η θάλασσα για κολύμπι, αλλά τον χειμώνα προτιμώ το βουνό για πεζοπορία στη φύση και καθαρό αέρα.",
        "example_en": "In summer I like the sea more for swimming, but in winter I prefer the mountains for hiking in nature and fresh air.",
        "example2_el": "Αγαπώ πολύ τη θάλασσα σε όλες τις εποχές του χρόνου, γιατί με ηρεμεί να περπατάω στην παραλία όταν έχει ήλιο.",
        "example2_en": "I love the sea very much in all seasons of the year, because it calms me to walk on the beach when it is sunny."
    },
    {
        "id": "SP-U05-006",
        "greek": "Πώς προετοιμάζεστε συνήθως πριν φύγετε για ένα ταξίδι;",
        "english": "How do you usually prepare before leaving for a trip? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Sequential discourse markers (πρώτα, μετά, τέλος) and travel preparation verbs (κλείνω εισιτήρια, ετοιμάζω βαλίτσα)"
        },
        "notes": "Examiner Objective: Checks chronological sequencing in Present tense.\nStrategy: Use `πρώτα`, `στη συνέχεια`, and `την τελευταία μέρα`.",
        "keg_communicative_function": "Explaining a sequence of preparatory steps before travelling",
        "example_el": "Πρώτα κλείνω τα εισιτήρια και το ξενοδοχείο στο διαδίκτυο, και δύο μέρες πριν φύγω φτιάχνω μια λίστα και ετοιμάζω τη βαλίτσα μου.",
        "example_en": "First I book the tickets and the hotel online, and two days before leaving I make a list and pack my suitcase.",
        "example2_el": "Διαβάζω πληροφορίες για το μέρος που θα επισκεφτώ, ελέγχω τον καιρό και αγοράζω ό,τι χρειάζομαι για το ταξίδι.",
        "example2_en": "I read information about the place I will visit, check the weather, and buy whatever I need for the trip."
    },
    {
        "id": "SP-U05-007",
        "greek": "Με ποιους προτιμάτε να πηγαίνετε διακοπές, με την οικογένεια ή με φίλους;",
        "english": "Who do you prefer to go on holiday with, family or friends? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Preposition με + Accusative, balancing two options (από τη μία... από την άλλη...)"
        },
        "notes": "Examiner Objective: Tests interpersonal vocabulary and balanced argumentation.\nStrategy: Explain how both types of holidays offer different benefits.",
        "keg_communicative_function": "Discussing social companions and contrasting types of leisure experiences",
        "example_el": "Μου αρέσουν και τα δύο, γιατί με την οικογένειά μου ξεκουράζομαι ήρεμα, ενώ με τους φίλους μου διασκεδάζουμε και βγαίνουμε το βράδυ.",
        "example_en": "I like both, because with my family I rest quietly, whereas with my friends we have fun and go out in the evening.",
        "example2_el": "Τα τελευταία χρόνια προτιμώ να ταξιδεύω με δύο καλούς φίλους, επειδή έχουμε τα ίδια ενδιαφέροντα και συμφωνούμε εύκολα στο πρόγραμμα.",
        "example2_en": "In recent years I prefer travelling with two good friends, because we have the same interests and agree easily on the schedule."
    },
    {
        "id": "SP-U05-008",
        "greek": "Ποιο μέρος στην Ελλάδα θα θέλατε πολύ να επισκεφτείτε στο μέλλον;",
        "english": "Which place in Greece would you really like to visit in the future? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Polite/hypothetical desire (θα ήθελα να + Aorist subjunctive επισκεφτώ/δω/πάω)"
        },
        "notes": "Examiner Objective: Tests future aspirations and cultural/geographical knowledge of Greece.\nStrategy: Name a specific Greek island or region and say what attracts you there.",
        "keg_communicative_function": "Expressing future travel wishes and cultural interest in Greece",
        "example_el": "Στο μέλλον θα ήθελα πολύ να επισκεφτώ τη Σαντορίνη και τη Νάξο, γιατί έχω δει υπέροχες φωτογραφίες και θέλω να δω το ηλιοβασίλεμα.",
        "example_en": "In the future I would really like to visit Santorini and Naxos, because I have seen wonderful photos and want to see the sunset.",
        "example2_el": "Θα ήθελα να κάνω ένα ταξίδι στην Πελοπόννησο το επόμενο καλοκαίρι, για να δω τους αρχαίους χώρους και τις όμορφες παραλίες.",
        "example2_en": "I would like to take a trip to the Peloponnese next summer, to see the ancient sites and the beautiful beaches."
    },

    # --- 009–016: Shopping, Markets & Consumer Habits ---
    {
        "id": "SP-U05-009",
        "greek": "Προτιμάτε τα μεγάλα σούπερ μάρκετ ή τις λαϊκές αγορές; Γιατί;",
        "english": "Do you prefer large supermarkets or open-air farmers' markets? Why? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Plural noun-adjective agreement in Accusative (φρέσκα φρούτα, χαμηλές τιμές), contrastive conjunction ενώ"
        },
        "notes": "Examiner Objective: Classic follow-up to the 'Laiki Agora' or 'Supermarket' Stage 3 picture.\nStrategy: Contrast fresh produce at the `λαϊκή αγορά` with convenience at the `σούπερ μάρκετ`.",
        "keg_communicative_function": "Comparing traditional open-air markets with modern supermarkets",
        "example_el": "Για φρούτα και λαχανικά προτιμώ τη λαϊκή αγορά της γειτονιάς μου, επειδή τα προϊόντα είναι πιο φρέσκα και οι τιμές πιο οικονομικές.",
        "example_en": "For fruits and vegetables I prefer my neighborhood open-air market, because the products are fresher and the prices more economical.",
        "example2_el": "Πηγαίνω συνήθως στο μεγάλο σούπερ μάρκετ μία φορά την εβδομάδα, γιατί εκεί βρίσκω τα πάντα σε ένα μέρος και κερδίζω χρόνο.",
        "example2_en": "I usually go to the large supermarket once a week, because there I find everything in one place and save time."
    },
    {
        "id": "SP-U05-010",
        "greek": "Σας αρέσει να κάνετε ψώνια από το διαδίκτυο ή από τα μαγαζιά της γειτονιάς;",
        "english": "Do you like shopping online or from neighborhood shops? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Shopping collocations (κάνω ψώνια, δοκιμάζω ρούχα, συγκρίνω τιμές)"
        },
        "notes": "Examiner Objective: Tests ability to discuss modern vs. traditional consumer habits.\nStrategy: Distinguish between buying books/electronics online vs. trying on clothes in person.",
        "keg_communicative_function": "Evaluating online shopping versus local retail stores",
        "example_el": "Όταν αγοράζω ρούχα και παπούτσια, προτιμώ τα μαγαζιά της γειτονιάς, γιατί θέλω να τα δοκιμάζω και να βλέπω την ποιότητα από κοντά.",
        "example_en": "When I buy clothes and shoes, I prefer neighborhood shops, because I want to try them on and see the quality up close.",
        "example2_el": "Αγοράζω συχνά βιβλία και ηλεκτρονικά είδη από το διαδίκτυο, επειδή μπορώ να συγκρίνω εύκολα τις τιμές και να βρω καλές προσφορές.",
        "example2_en": "I often buy books and electronics online, because I can easily compare prices and find good offers."
    },
    {
        "id": "SP-U05-011",
        "greek": "Πόσο συχνά πηγαίνετε για ψώνια και τι αγοράζετε συνήθως;",
        "english": "How often do you go shopping and what do you usually buy? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Frequency expressions (δύο φορές την εβδομάδα, κάθε Σάββατο) + everyday grocery vocabulary"
        },
        "notes": "Examiner Objective: Evaluates routine frequency adverbs and household food/item vocabulary.\nStrategy: Separate weekly grocery shopping from occasional clothing purchases.",
        "keg_communicative_function": "Describing shopping frequency and everyday household purchases",
        "example_el": "Πηγαίνω στο σούπερ μάρκετ δύο φορές την εβδομάδα και αγοράζω γάλα, ψωμί, τυρί, ζυμαρικά και όλα τα απαραίτητα τρόφιμα για το σπίτι.",
        "example_en": "I go to the supermarket twice a week and buy milk, bread, cheese, pasta, and all the necessary groceries for the house.",
        "example2_el": "Για ρούχα πηγαίνω στα μαγαζιά μόνο όταν υπάρχουν εκπτώσεις, αλλά για τρόφιμα ψωνίζω σχεδόν κάθε δύο μέρες από τη γειτονιά μου.",
        "example2_en": "For clothes I go to the shops only when there are sales, but for food I shop almost every two days in my neighborhood."
    },
    {
        "id": "SP-U05-012",
        "greek": "Προσέχετε περισσότερο την τιμή ή την ποιότητα όταν αγοράζετε κάτι;",
        "english": "Do you pay more attention to price or quality when you buy something? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Comparative adverbs (περισσότερο), abstract nouns (η τιμή, η ποιότητα), conditional/relative clauses"
        },
        "notes": "Examiner Objective: Tests decision-making explanation and consumer vocabulary.\nStrategy: Explain that for food and shoes quality comes first, while still looking for reasonable prices.",
        "keg_communicative_function": "Weighing price against quality in consumer decision-making",
        "example_el": "Κοιτάζω πάντα και τα δύο, αλλά στα τρόφιμα και στα παπούτσια προσέχω περισσότερο την ποιότητα, ακόμα κι αν είναι λίγο πιο ακριβά.",
        "example_en": "I always look at both, but for food and shoes I pay more attention to quality, even if they are a bit more expensive.",
        "example2_el": "Προσπαθώ να βρίσκω καλή ποιότητα σε λογική τιμή, γι' αυτό περιμένω συχνά την περίοδο των εκπτώσεων για μεγάλες αγορές.",
        "example2_en": "I try to find good quality at a reasonable price, which is why I often wait for the sales period for big purchases."
    },
    {
        "id": "SP-U05-013",
        "greek": "Προτιμάτε να πληρώνετε με μετρητά ή με κάρτα στα καταστήματα;",
        "english": "Do you prefer to pay with cash or by card in shops? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Instrumental με + Accusative (με μετρητά, με κάρτα), practical justification"
        },
        "notes": "Examiner Objective: Bridges checkout/transaction scenes in Stage 3 photos to daily payment habits.\nStrategy: Mention convenience of cards vs. keeping small cash for coffee/bakeries.",
        "keg_communicative_function": "Explaining payment preferences in everyday transactions",
        "example_el": "Σχεδόν παντού πληρώνω με κάρτα, γιατί είναι πολύ εύκολο και γρήγορο, και δεν χρειάζεται να έχω πολλά κέρματα μαζί μου.",
        "example_en": "Almost everywhere I pay by card, because it is very easy and fast, and I don't need to carry many coins with me.",
        "example2_el": "Στα μεγάλα καταστήματα χρησιμοποιώ πάντα την κάρτα μου, αλλά στον φούρνο και στη λαϊκή αγορά προτιμώ να πληρώνω με μετρητά.",
        "example2_en": "In large stores I always use my card, but at the bakery and the farmers' market I prefer to pay with cash."
    },
    {
        "id": "SP-U05-014",
        "greek": "Σας αρέσει να πηγαίνετε για ψώνια μόνοι σας ή με παρέα;",
        "english": "Do you like going shopping alone or with company? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Reflexive/intensive adjective μόνος μου/μόνη μου vs. με παρέα"
        },
        "notes": "Examiner Objective: Tests social vs. solo activity description.\nStrategy: Combine shopping with having a coffee afterwards (`πίνουμε έναν καφέ`).",
        "keg_communicative_function": "Expressing preferences regarding social versus solo shopping",
        "example_el": "Όταν θέλω να αγοράσω ρούχα, μου αρέσει να πηγαίνω με έναν καλό φίλο για να μου λέει τη γνώμη του και μετά να πίνουμε καφέ.",
        "example_en": "When I want to buy clothes, I like going with a good friend so they can tell me their opinion and afterwards we drink coffee.",
        "example2_el": "Συνήθως προτιμώ να πηγαίνω για ψώνια μόνος μου, γιατί έτσι τελειώνω πιο γρήγορα και δεν κουράζομαι στα μαγαζιά.",
        "example2_en": "Usually I prefer to go shopping by myself, because that way I finish faster and don't get tired in the shops."
    },
    {
        "id": "SP-U05-015",
        "greek": "Τι δώρα σας αρέσει να αγοράζετε για τους φίλους και την οικογένειά σας;",
        "english": "What gifts do you like buying for your friends and family? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Indirect object prepositional phrases (για τους φίλους μου) and gift vocabulary (βιβλία, αρώματα, ρούχα)"
        },
        "notes": "Examiner Objective: Connects celebration or shop-window photos to gift-giving customs.\nStrategy: Give specific examples of gifts based on what the person likes.",
        "keg_communicative_function": "Describing gift-giving habits and personalizing choices for others",
        "example_el": "Μου αρέσει να αγοράζω χρήσιμα δώρα, όπως ένα ωραίο βιβλίο, ένα πουκάμισο ή εισιτήρια για μια θεατρική παράσταση που θέλουν να δουν.",
        "example_en": "I like buying useful gifts, such as a nice book, a shirt, or tickets for a theater performance they want to see.",
        "example2_el": "Όταν πηγαίνω σε μια γιορτή στο σπίτι φίλων, παίρνω συνήθως ένα κουτί γλυκά από το ζαχαροπλαστείο ή ένα καλό μπουκάλι κρασί.",
        "example2_en": "When I go to a celebration at friends' house, I usually bring a box of sweets from the pastry shop or a good bottle of wine."
    },
    {
        "id": "SP-U05-016",
        "greek": "Περιμένετε τις εκπτώσεις για να αγοράσετε ρούχα και παπούτσια;",
        "english": "Do you wait for the sales to buy clothes and shoes? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Purpose clauses with για να + Aorist subjunctive (για να αγοράσω, για να βρω)"
        },
        "notes": "Examiner Objective: Tests purpose clauses (`για να`) and seasonal shopping vocabulary (`χειμερινές / καλοκαιρινές εκπτώσεις`).\nStrategy: Mention saving money on expensive items like winter coats or shoes.",
        "keg_communicative_function": "Explaining budgeting habits and seasonal sales shopping",
        "example_el": "Ναι, περιμένω σχεδόν πάντα τις χειμερινές και τις καλοκαιρινές εκπτώσεις για να αγοράσω ακριβά πράγματα, όπως μπουφάν και καλά παπούτσια.",
        "example_en": "Yes, I almost always wait for the winter and summer sales to buy expensive things, such as jackets and good shoes.",
        "example2_el": "Αν χρειάζομαι κάτι άμεσα το αγοράζω αμέσως, αλλά τις περισσότερες φορές προτιμώ τις εκπτώσεις γιατί οι τιμές είναι πολύ καλύτερες.",
        "example2_en": "If I need something urgently I buy it immediately, but most of the time I prefer the sales because the prices are much better."
    },

    # --- 017–024: Gastronomy, Family Gatherings & Celebrations ---
    {
        "id": "SP-U05-017",
        "greek": "Πόσο συχνά τρώτε έξω σε εστιατόριο ή ταβέρνα με την παρέα σας;",
        "english": "How often do you eat out at a restaurant or taverna with your friends? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Present tense of τρώω (τρώω, τρως, τρώει, τρώμε), dining out vocabulary (ταβέρνα, μεζέδες, παρέα)"
        },
        "notes": "Examiner Objective: Connects a taverna/restaurant photo to the candidate's social dining life.\nStrategy: Mention frequency (e.g., once a week on Saturday night) and what you order.",
        "keg_communicative_function": "Describing social dining habits and favorite Greek tavern dishes",
        "example_el": "Βγαίνουμε με την παρέα μου σε μια παραδοσιακή ταβέρνα σχεδόν κάθε Σάββατο βράδυ, όπου παραγγέλνουμε διάφορους μεζέδες και συζητάμε τα νέα μας.",
        "example_en": "We go out with my group of friends to a traditional taverna almost every Saturday night, where we order various meze dishes and discuss our news.",
        "example2_el": "Τις καθημερινές τρώω πάντα στο σπίτι, αλλά δύο φορές τον μήνα πηγαίνω με την οικογένειά μου σε ένα ωραίο εστιατόριο δίπλα στη θάλασσα.",
        "example2_en": "On weekdays I always eat at home, but twice a month I go with my family to a nice restaurant by the sea."
    },
    {
        "id": "SP-U05-018",
        "greek": "Σας αρέσει να μαγειρεύετε στο σπίτι ή προτιμάτε το έτοιμο φαγητό;",
        "english": "Do you like cooking at home or do you prefer ready-made food? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Comparative adjectives (πιο υγιεινό, πιο νόστιμο, πιο οικονομικό) and kitchen/cooking verbs"
        },
        "notes": "Examiner Objective: Evaluates health/cost comparisons in daily nutrition.\nStrategy: Emphasize that home-cooked food (`το σπιτικό φαγητό`) is healthier, while delivery is only for busy days.",
        "keg_communicative_function": "Comparing home cooking with takeaway food in terms of health and time",
        "example_el": "Μου αρέσει πολύ να μαγειρεύω στο σπίτι με φρέσκα υλικά, γιατί το σπιτικό φαγητό είναι πολύ πιο υγιεινό και οικονομικό από το έτοιμο.",
        "example2_el": "Συνήθως μαγειρεύω εγώ κάθε μέρα, αλλά όταν γυρίζω πολύ κουρασμένος από τη δουλειά το βράδυ, παραγγέλνω κάτι απλό από έξω.",
        "example_en": "I really like cooking at home with fresh ingredients, because homemade food is much healthier and more economical than ready-made food.",
        "example2_en": "Usually I cook every day, but when I return very tired from work in the evening, I order something simple from outside."
    },
    {
        "id": "SP-U05-019",
        "greek": "Ποιο είναι το αγαπημένο σας ελληνικό φαγητό και πώς το τρώτε;",
        "english": "What is your favorite Greek dish and how do you eat it? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Gastronomy vocabulary (μουσακάς, παστίτσιο, χωριάτικη σαλάτα, ψητό ψάρι, ελαιόλαδο)"
        },
        "notes": "Examiner Objective: Tests culinary vocabulary and descriptive enthusiasm.\nStrategy: Name a classic dish, mention its main ingredients, and when you enjoy eating it.",
        "keg_communicative_function": "Describing favorite dishes and culinary ingredients",
        "example_el": "Το αγαπημένο μου ελληνικό φαγητό είναι ο μουσακάς και τα γεμιστά με ρύζι, ειδικά όταν τα συνοδεύω με δροσερή χωριάτικη σαλάτα και φέτα.",
        "example_en": "My favorite Greek dish is moussaka and stuffed vegetables with rice, especially when I accompany them with a cool Greek salad and feta.",
        "example2_el": "Μου αρέσει πάρα πολύ το φρέσκο ψητό ψάρι με λεμόνι και ελαιόλαδο το καλοκαίρι, σε μια ήσυχη ταβέρνα δίπλα στο κύμα.",
        "example2_en": "I really love fresh grilled fish with lemon and olive oil in the summer, at a quiet taverna right by the waves."
    },
    {
        "id": "SP-U05-020",
        "greek": "Ποια είναι η αγαπημένη σας γιορτή του χρόνου και πώς τη γιορτάζετε;",
        "english": "What is your favorite holiday of the year and how do you celebrate it? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Festive vocabulary (Χριστούγεννα, Πάσχα, Πρωτοχρονιά, οικογενειακό τραπέζι, ανταλλάσσω δώρα)"
        },
        "notes": "Examiner Objective: Follow-up to family dinner or celebration pictures.\nStrategy: Describe atmosphere, family gathering, festive meal, and traditions.",
        "keg_communicative_function": "Describing annual holidays, traditions, and family celebrations",
        "example_el": "Η αγαπημένη μου γιορτή είναι τα Χριστούγεννα, γιατί στολίζουμε το σπίτι, μαζευόμαστε όλη η οικογένεια γύρω από το τραπέζι και ανταλλάσσουμε δώρα.",
        "example_en": "My favorite holiday is Christmas, because we decorate the house, the whole family gathers around the table, and we exchange gifts.",
        "example2_el": "Μου αρέσει περισσότερο το Πάσχα την άνοιξη, επειδή πηγαίνουμε στο χωριό, ψήνουμε στον κήπο και γιορτάζουμε έξω στη φύση.",
        "example2_en": "I like Easter in the spring the most, because we go to the village, roast food in the garden, and celebrate outside in nature."
    },
    {
        "id": "SP-U05-021",
        "greek": "Πώς γιορτάσατε τα τελευταία σας γενέθλια;",
        "english": "How did you celebrate your last birthday? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Aorist tense narration (κάλεσα, μαγείρεψα, πήγαμε, σβήσαμε τα κεράκια, περάσαμε)"
        },
        "notes": "Examiner Objective: Tests shift from Present habits to a specific Past event (`πέρσι στα γενέθλιά μου`).\nStrategy: Use 3–4 Aorist verbs to recount who came and what you did.",
        "keg_communicative_function": "Recounting a specific past celebration in the Aorist tense",
        "example_el": "Στα τελευταία μου γενέθλια κάλεσα τους πιο καλούς μου φίλους στο σπίτι, ετοιμάσαμε φαγητό, βάλαμε μουσική και κόψαμε μια μεγάλη τούρτα σοκολάτας.",
        "example_en": "On my last birthday I invited my closest friends to the house, we prepared food, put on music, and cut a big chocolate cake.",
        "example2_el": "Πέρσι στα γενέθλιά μου πήγαμε με την οικογένειά μου σε ένα ωραίο εστιατόριο στο κέντρο της πόλης και περάσαμε ένα υπέροχο βράδυ.",
        "example2_en": "Last year on my birthday I went with my family to a nice restaurant in the city center and we spent a wonderful evening."
    },
    {
        "id": "SP-U05-022",
        "greek": "Συνηθίζετε να καλείτε φίλους για φαγητό ή καφέ στο σπίτι σας;",
        "english": "Are you in the habit of inviting friends for food or coffee at your home? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Habitual verb συνηθίζω να + Present subjunctive (καλώ, φτιάχνω, συζητάω)"
        },
        "notes": "Examiner Objective: Assesses hospitality vocabulary (`φιλοξενία`) and social home routines.\nStrategy: Mention weekend afternoon coffee or Sunday lunch.",
        "keg_communicative_function": "Discussing home hospitality and socializing with friends",
        "example_el": "Ναι, συνηθίζω να καλώ φίλους στο σπίτι τις Κυριακές το μεσημέρι, όπου μαγειρεύω κάτι νόστιμο και καθόμαστε με τις ώρες στο μπαλκόνι.",
        "example_en": "Yes, I am in the habit of inviting friends to the house on Sunday afternoons, where I cook something tasty and we sit for hours on the balcony.",
        "example2_el": "Μου αρέσει πολύ να έρχονται φίλοι το απόγευμα για καφέ και γλυκό, γιατί στο σπίτι υπάρχει ησυχία και μπορούμε να μιλήσουμε άνετα.",
        "example2_en": "I really like having friends come over in the afternoon for coffee and dessert, because at home it is quiet and we can talk comfortably."
    },
    {
        "id": "SP-U05-023",
        "greek": "Τι τρώτε συνήθως για πρωινό πριν ξεκινήσετε τη μέρα σας;",
        "english": "What do you usually eat for breakfast before starting your day? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Temporal conjunction πριν + Aorist subjunctive (πριν ξεκινήσω, πριν φύγω) and breakfast items"
        },
        "notes": "Examiner Objective: Tests daily nutrition vocabulary and weekday vs. weekend contrast.\nStrategy: Contrast a quick weekday breakfast with a relaxed Sunday breakfast.",
        "keg_communicative_function": "Describing daily morning routines and breakfast habits",
        "example_el": "Τις καθημερινές πίνω έναν ζεστό καφέ και τρώω γιαούρτι με μέλι και φρούτα, πριν φύγω το πρωί για τη δουλειά μου.",
        "example_en": "On weekdays I drink a hot coffee and eat yogurt with honey and fruit, before leaving in the morning for my job.",
        "example2_el": "Από Δευτέρα έως Παρασκευή τρώω μόνο ένα τοστ, αλλά την Κυριακή που έχω χρόνο φτιάχνω αυγά, φρέσκο χυμό πορτοκάλι και καφέ.",
        "example2_en": "From Monday to Friday I only eat a toasted sandwich, but on Sunday when I have time I make eggs, fresh orange juice, and coffee."
    },
    {
        "id": "SP-U05-024",
        "greek": "Πόσο σημαντικό είναι για εσάς το οικογενειακό τραπέζι την Κυριακή;",
        "english": "How important is the Sunday family meal for you? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Expressing personal importance (είναι πολύ σημαντικό γιατί...), family cohesion vocabulary"
        },
        "notes": "Examiner Objective: Directly extends a Stage 3 family dinner photograph.\nStrategy: Explain that during the week everyone is busy, so Sunday brings the family together.",
        "keg_communicative_function": "Explaining the emotional and social value of family traditions",
        "example_el": "Για μένα το κυριακάτικο τραπέζι είναι πολύ σημαντικό, επειδή όλη την εβδομάδα δουλεύουμε πολλές ώρες και είναι η μόνη ευκαιρία να βρεθούμε όλοι μαζί.",
        "example_en": "For me the Sunday table is very important, because all week we work long hours and it is the only opportunity for us all to get together.",
        "example2_el": "Μου αρέσει αυτή η παράδοση, γιατί μαζευόμαστε με τους γονείς και τους συγγενείς μας, τρώμε σπιτικό φαγητό και μαθαίνουμε τα νέα ο ένας του άλλου.",
        "example2_en": "I like this tradition, because we gather with our parents and relatives, eat homemade food, and learn each other's news."
    },

    # --- 025–032: Health, Fitness, City vs. Countryside & Environment ---
    {
        "id": "SP-U05-025",
        "greek": "Τι κάνετε στην καθημερινότητά σας για να προσέχετε την υγεία σας;",
        "english": "What do you do in your daily life to look after your health? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Purpose clause για να + subjunctive, health and lifestyle collocations (υγιεινή διατροφή, γυμναστική, ύπνος)"
        },
        "notes": "Examiner Objective: Bridges a doctor's office, pharmacy, or park exercise photo to personal health habits.\nStrategy: Mention diet, physical activity, and adequate sleep.",
        "keg_communicative_function": "Describing healthy lifestyle habits and preventive self-care",
        "example_el": "Προσπαθώ να τρώω πολλά φρούτα και λαχανικά, πίνω αρκετό νερό κάθε μέρα και περπατάω τουλάχιστον μισή ώρα στο πάρκο της γειτονιάς μου.",
        "example_en": "I try to eat plenty of fruits and vegetables, drink enough water every day, and walk at least half an hour in my neighborhood park.",
        "example2_el": "Για να προσέχω την υγεία μου, πηγαίνω στο γυμναστήριο τρεις φορές την εβδομάδα, αποφεύγω τα γλυκά και κοιμάμαι οκτώ ώρες κάθε βράδυ.",
        "example2_en": "To look after my health, I go to the gym three times a week, avoid sweets, and sleep eight hours every night."
    },
    {
        "id": "SP-U05-026",
        "greek": "Αθλείστε στον ελεύθερο χρόνο σας; Ποιο είναι το αγαπημένο σας σπορ;",
        "english": "Do you exercise in your free time? What is your favorite sport? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Middle/passive verb αθλούμαι / γυμνάζομαι, sports nouns (κολύμβηση, τρέξιμο, ποδήλατο, τένις)"
        },
        "notes": "Examiner Objective: Tests sports/exercise vocabulary and stress-relief explanations.\nStrategy: State the activity, how often you do it, and how it makes you feel.",
        "keg_communicative_function": "Discussing sports participation and physical exercise routines",
        "example_el": "Ναι, στον ελεύθερο χρόνο μου κάνω ποδήλατο και κολύμβηση, γιατί με βοηθούν να κρατάω καλή φυσική κατάσταση και να ξεχνάω το άγχος.",
        "example_en": "Yes, in my free time I cycle and swim, because they help me maintain good physical fitness and forget about stress.",
        "example2_el": "Δεν κάνω κάποιο ομαδικό άθλημα, αλλά μου αρέσει πολύ το γρήγορο περπάτημα και το τρέξιμο δίπλα στη θάλασσα τα απογεύματα.",
        "example2_en": "I don't play any team sport, but I really like brisk walking and running by the sea in the afternoons."
    },
    {
        "id": "SP-U05-027",
        "greek": "Τι κάνετε συνήθως όταν νιώθετε κουρασμένοι ή έχετε άγχος από τη δουλειά;",
        "english": "What do you usually do when you feel tired or stressed from work? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Temporal/conditional clause όταν νιώθω + relaxation verbs (χαλαρώνω, ξεκουράζομαι, ακούω μουσική)"
        },
        "notes": "Examiner Objective: Evaluates emotional state adjectives (`κουρασμένος`, `αγχωμένος`) and coping habits.\nStrategy: Mention relaxing activities at home or going for a quiet walk.",
        "keg_communicative_function": "Explaining ways of relaxing and managing everyday stress",
        "example_el": "Όταν νιώθω κουρασμένος ή έχω άγχος, κλείνω το κινητό μου, κάνω ένα ζεστό μπάνιο και ακούω ήρεμη μουσική στο σαλόνι.",
        "example_en": "When I feel tired or stressed, I turn off my mobile phone, take a warm bath, and listen to calm music in the living room.",
        "example2_el": "Για να χαλαρώσω μετά από μια δύσκολη μέρα στη δουλειά, βγαίνω μια βόλτα με τον σκύλο μου ή συναντάω έναν καλό φίλο.",
        "example2_en": "To relax after a difficult day at work, I go for a walk with my dog or meet a good friend."
    },
    {
        "id": "SP-U05-028",
        "greek": "Θα προτιμούσατε να ζείτε σε μια μεγάλη πόλη ή σε ένα ήσυχο χωριό;",
        "english": "Would you prefer to live in a big city or in a quiet village? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Conditional tense (θα προτιμούσα να ζω), urban vs. rural pros and cons"
        },
        "notes": "Examiner Objective: High-frequency KEG A2 extension topic comparing urban vs. countryside life.\nStrategy: Weigh jobs and entertainment in the city against peace and nature in the village.",
        "keg_communicative_function": "Comparing urban and rural living conditions and personal preferences",
        "example_el": "Τώρα προτιμώ να ζω στην πόλη επειδή υπάρχουν περισσότερες ευκαιρίες για δουλειά, αλλά στο μέλλον θα ήθελα να μείνω σε ένα ήσυχο χωριό.",
        "example_en": "Right now I prefer living in the city because there are more job opportunities, but in the future I would like to live in a quiet village.",
        "example2_el": "Θα προτιμούσα να ζω σε μια μικρή πόλη κοντά στη θάλασσα, για να έχω καθαρό αέρα και λιγότερη κίνηση στους δρόμους.",
        "example2_en": "I would prefer to live in a small town near the sea, so as to have clean air and less traffic on the streets."
    },
    {
        "id": "SP-U05-029",
        "greek": "Ποια είναι τα μεγαλύτερα προβλήματα που έχει σήμερα μια μεγάλη πόλη;",
        "english": "What are the biggest problems that a big city has today? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Superlative neuter plural (τα μεγαλύτερα προβλήματα), urban issue nouns (η κίνηση, ο θόρυβος, η ρύπανση)"
        },
        "notes": "Examiner Objective: Connects street traffic or city scenes in Stage 3 to civic awareness.\nStrategy: Mention traffic (`κίνηση`), lack of parking (`πάρκινγκ`), noise (`θόρυβος`), and lack of green spaces (`πάρκα`).",
        "keg_communicative_function": "Identifying and discussing everyday urban problems",
        "example_el": "Τα μεγαλύτερα προβλήματα σε μια μεγάλη πόλη είναι η πολλή κίνηση στους δρόμους, ο θόρυβος, η έλλειψη πάρκινγκ και τα λίγα πάρκα.",
        "example_en": "The biggest problems in a big city are the heavy traffic on the streets, the noise, the lack of parking, and the few parks.",
        "example2_el": "Στις μεγάλες πόλεις ο αέρας δεν είναι καθαρός, τα ενοίκια είναι πολύ ακριβά και οι άνθρωποι τρέχουν συνέχεια με πολύ άγχος.",
        "example2_en": "In big cities the air is not clean, rents are very expensive, and people are constantly rushing around with a lot of stress."
    },
    {
        "id": "SP-U05-030",
        "greek": "Χρησιμοποιείτε τα μέσα μαζικής μεταφοράς ή το αυτοκίνητό σας στις μετακινήσεις σας;",
        "english": "Do you use public transport or your car for your daily commutes? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Public transport vocabulary (μετρό, λεωφορείο, ηλεκτρικός, κίνηση, θέση στάθμευσης)"
        },
        "notes": "Examiner Objective: Tests transport vocabulary and practical commuting arguments.\nStrategy: Explain why the metro/bus is convenient for the city center.",
        "keg_communicative_function": "Discussing daily commuting habits and public transport usage",
        "example_el": "Καθημερινά χρησιμοποιώ το μετρό και το λεωφορείο για να πηγαίνω στη δουλειά μου, γιατί στο κέντρο έχει πολλή κίνηση και δεν βρίσκω πάρκινγκ.",
        "example_en": "Every day I use the metro and the bus to go to my work, because in the center there is heavy traffic and I cannot find parking.",
        "example2_el": "Παίρνω το αυτοκίνητό μου μόνο τα σαββατοκύριακα για εκδρομές, ενώ τις καθημερινές προτιμώ να περπατάω ή να παίρνω το τρένο.",
        "example2_en": "I take my car only on weekends for excursions, whereas on weekdays I prefer to walk or take the train."
    },
    {
        "id": "SP-U05-031",
        "greek": "Τι μπορούμε να κάνουμε εμείς στην καθημερινότητά μας για να προστατεύσουμε το περιβάλλον;",
        "english": "What can we do in our daily lives to protect the environment? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "First person plural modal (μπορούμε να κάνουμε), ecological vocabulary (ανακύκλωση, πλαστικές σακούλες, ενέργεια)"
        },
        "notes": "Examiner Objective: Follows up on beach/park cleanup or nature photographs in Stage 3.\nStrategy: List 3 concrete habits: recycling (`ανακύκλωση`), saving water/electricity, and avoiding plastic.",
        "keg_communicative_function": "Proposing everyday environmental protection actions",
        "example_el": "Μπορούμε να κάνουμε ανακύκλωση στο σπίτι, να μη χρησιμοποιούμε πλαστικές σακούλες στα ψώνια και να κλείνουμε τα φώτα όταν δεν τα χρειαζόμαστε.",
        "example_en": "We can recycle at home, not use plastic bags when shopping, and turn off the lights when we don't need them.",
        "example2_el": "Είναι σημαντικό να κρατάμε τις παραλίες και τα πάρκα καθαρά, να μην πετάμε σκουπίδια κάτω και να χρησιμοποιούμε περισσότερο τα μέσα μεταφοράς.",
        "example2_en": "It is important to keep beaches and parks clean, not throw rubbish on the ground, and use public transport more."
    },
    {
        "id": "SP-U05-032",
        "greek": "Ποια είναι η αγαπημένη σας εποχή του χρόνου και γιατί;",
        "english": "What is your favorite season of the year and why? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Seasons and weather expressions (η άνοιξη, το καλοκαίρι, το φθινόπωρο, ο χειμώνας, ο καιρός είναι γλυκός)"
        },
        "notes": "Examiner Objective: Connects weather/seasonal elements in the visual prompt to candidate preferences.\nStrategy: Describe the weather, nature, and outdoor activities typical of that season.",
        "keg_communicative_function": "Describing seasonal preferences, weather conditions, and outdoor activities",
        "example_el": "Η αγαπημένη μου εποχή είναι η άνοιξη, επειδή ο καιρός είναι ζεστός και ευχάριστος, η φύση είναι καταπράσινη και η μέρα μεγαλώνει.",
        "example_en": "My favorite season is spring, because the weather is warm and pleasant, nature is lush green, and the day gets longer.",
        "example2_el": "Αγαπώ περισσότερο το καλοκαίρι στην Ελλάδα, γιατί έχει πάντα ήλιο, πηγαίνουμε στη θάλασσα και καθόμαστε έξω τα βράδια με φίλους.",
        "example2_en": "I love summer in Greece the most, because it is always sunny, we go to the sea, and we sit outside in the evenings with friends."
    },

    # --- 033–040: Multi-Tense Storytelling (Past vs. Present vs. Future) & Technology ---
    {
        "id": "SP-U05-033",
        "greek": "Πώς ήταν η ζωή σας πριν από πέντε χρόνια σε σχέση με σήμερα;",
        "english": "How was your life five years ago compared to today? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Multi-tense contrast: Imperfect/Aorist (πριν από πέντε χρόνια ζούσα/δούλευα) vs. Present (σήμερα ζω/δουλεύω)"
        },
        "notes": "Examiner Objective: Core KEG A2 test of tense switching between past state (`Παρατατικός`) and current reality (`Ενεστώτας`).\nStrategy: Use explicit time anchors: `Πριν από πέντε χρόνια... ενώ σήμερα...`.",
        "keg_communicative_function": "Contrasting past life circumstances with present routines using Imperfect and Present tenses",
        "example_el": "Πριν από πέντε χρόνια ζούσα σε άλλη πόλη και σπούδαζα στο πανεπιστήμιο, ενώ σήμερα έχω τη δική μου δουλειά και μαθαίνω ελληνικά.",
        "example_en": "Five years ago I was living in another city and studying at university, whereas today I have my own job and am learning Greek.",
        "example2_el": "Τότε είχα περισσότερο ελεύθερο χρόνο για βόλτες με φίλους, αλλά σήμερα η ζωή μου είναι πιο οργανωμένη και έχω περισσότερες ευθύνες.",
        "example2_en": "Back then I had more free time for walks with friends, but today my life is more organized and I have more responsibilities."
    },
    {
        "id": "SP-U05-034",
        "greek": "Τι συνηθίζατε να κάνετε τα καλοκαίρια όταν ήσασταν παιδί;",
        "english": "What did you use to do in the summers when you were a child? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Imperfect tense (Παρατατικός) for childhood habits (όταν ήμουν παιδί, πήγαινα, έπαιζα, έμενα)"
        },
        "notes": "Examiner Objective: Tests accurate formation of Imperfect (`Παρατατικός`) for repeated past actions.\nStrategy: Keep every verb in the Imperfect (`πήγαινα`, `έπαιζα`, `κολυμπούσα`).",
        "keg_communicative_function": "Narrating habitual childhood memories using the Imperfect tense",
        "example_el": "Όταν ήμουν παιδί, κάθε καλοκαίρι πήγαινα στο χωριό των παππούδων μου, έπαιζα όλη μέρα έξω με τα άλλα παιδιά και έτρωγα παγωτό.",
        "example_en": "When I was a child, every summer I used to go to my grandparents' village, play outside all day with the other children, and eat ice cream.",
        "example2_el": "Τα καλοκαίρια ξυπνούσα αργά το πρωί, διάβαζα παιδικά βιβλία, έκανα ποδήλατο στη γειτονιά και πήγαινα στη θάλασσα με τους γονείς μου.",
        "example2_en": "In the summers I used to wake up late in the morning, read children's books, ride my bike in the neighborhood, and go to the sea with my parents."
    },
    {
        "id": "SP-U05-035",
        "greek": "Πώς χρησιμοποιείτε το κινητό τηλέφωνο και το διαδίκτυο στην καθημερινή σας ζωή;",
        "english": "How do you use your mobile phone and the internet in your daily life? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Digital communication vocabulary (στέλνω μηνύματα, διαβάζω ειδήσεις, πληρώνω λογαριασμούς, μαθαίνω γλώσσες)"
        },
        "notes": "Examiner Objective: Connects workplace, café, or youth photos showing smartphones/laptops to candidate's daily use.\nStrategy: Mention communication, work/study, and practical tasks.",
        "keg_communicative_function": "Describing everyday technology and internet usage",
        "example_el": "Χρησιμοποιώ το κινητό και το διαδίκτυο κάθε μέρα για τη δουλειά μου, για να μιλάω με φίλους, να διαβάζω ειδήσεις και να κάνω μαθήματα ελληνικών.",
        "example_en": "I use my mobile phone and the internet every day for my work, to talk with friends, read the news, and take Greek lessons.",
        "example2_el": "Με το διαδίκτυο πληρώνω εύκολα τους λογαριασμούς μου, κλείνω εισιτήρια για ταξίδια και βρίσκω γρήγορα πληροφορίες για ό,τι χρειάζομαι.",
        "example2_en": "With the internet I easily pay my bills, book tickets for trips, and quickly find information for whatever I need."
    },
    {
        "id": "SP-U05-036",
        "greek": "Πιστεύετε ότι η τεχνολογία μάς φέρνει πιο κοντά ή μας απομακρύνει από τους άλλους;",
        "english": "Do you believe technology brings us closer together or distances us from others? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Opinion framing (πιστεύω ότι..., από τη μία πλευρά... από την άλλη...) and balanced A2 evaluation"
        },
        "notes": "Examiner Objective: Tests ability to express a nuanced opinion at CEFR A2 level.\nStrategy: Acknowledge that it helps talk to people far away, but shouldn't replace face-to-face (`από κοντά`) contact.",
        "keg_communicative_function": "Expressing a balanced opinion on the social impact of technology",
        "example_el": "Πιστεύω ότι η τεχνολογία μάς βοηθάει πολύ να επικοινωνούμε με φίλους που ζουν μακριά, αλλά πρέπει να βρισκόμαστε και από κοντά.",
        "example_en": "I believe technology helps us a lot to communicate with friends who live far away, but we must also meet in person.",
        "example2_el": "Όταν χρησιμοποιούμε σωστά το κινητό είναι πολύ χρήσιμο, όμως μερικές φορές οι άνθρωποι κάθονται μαζί στον καφέ και κοιτάζουν μόνο την οθόνη τους.",
        "example2_en": "When we use the mobile phone properly it is very useful, however sometimes people sit together at a café and only look at their screen."
    },
    {
        "id": "SP-U05-037",
        "greek": "Προτιμάτε να διαβάζετε τυπωμένα βιβλία ή να βλέπετε ταινίες στον ελεύθερο χρόνο σας;",
        "english": "Do you prefer reading printed books or watching movies in your free time? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Cultural leisure vocabulary (μυθιστόρημα, κινηματογράφος, ταινία, ξεκουράζω το μυαλό μου)"
        },
        "notes": "Examiner Objective: Extends Stage 3 photos of people reading in a park/metro or relaxing at home.\nStrategy: Explain when you prefer reading (e.g., before sleep or on holiday) vs. watching a film.",
        "keg_communicative_function": "Discussing cultural hobbies and entertainment preferences",
        "example_el": "Μου αρέσει πολύ να διαβάζω ένα ωραίο βιβλίο το βράδυ πριν κοιμηθώ, ενώ το σαββατοκύριακο προτιμώ να βλέπω μια καλή ταινία στον κινηματογράφο.",
        "example_en": "I really like reading a nice book at night before going to sleep, whereas on the weekend I prefer watching a good movie at the cinema.",
        "example2_el": "Τον χειμώνα βλέπω συχνά ταινίες στο σπίτι με την οικογένειά μου, αλλά στις καλοκαιρινές διακοπές παίρνω πάντα μαζί μου δύο βιβλία.",
        "example2_en": "In winter I often watch movies at home with my family, but on summer holidays I always take two books with me."
    },
    {
        "id": "SP-U05-038",
        "greek": "Πώς μαθαίνατε ξένες γλώσσες παλιότερα και πώς μαθαίνετε ελληνικά σήμερα;",
        "english": "How did you use to learn foreign languages in the past and how do you learn Greek today? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Imperfect (παλιότερα μάθαινα, είχαμε) vs. Present (σήμερα μαθαίνω, ακούω, χρησιμοποιώ)"
        },
        "notes": "Examiner Objective: Combines multi-tense contrast with the candidate's personal Greek-learning journey.\nStrategy: Contrast school textbooks in the past with modern audio/apps and speaking practice today.",
        "keg_communicative_function": "Comparing past educational methods with current language-learning practices",
        "example_el": "Παλιότερα στο σχολείο διαβάζαμε μόνο από το βιβλίο της γραμματικής, ενώ σήμερα μαθαίνω ελληνικά με διαδραστικές κάρτες, ακούω ελληνικά τραγούδια και μιλάω με Έλληνες.",
        "example_en": "In the past at school we only read from the grammar book, whereas today I learn Greek with interactive flashcards, listen to Greek songs, and speak with Greeks.",
        "example2_el": "Όταν ήμουν μαθητής δεν είχαμε διαδίκτυο, αλλά τώρα μπορώ να κάνω μάθημα από το σπίτι μου και να ακούω τη σωστή προφορά κάθε μέρα.",
        "example2_en": "When I was a student we didn't have the internet, but now I can take lessons from my home and listen to the correct pronunciation every day."
    },
    {
        "id": "SP-U05-039",
        "greek": "Ποια είναι τα σχέδιά σας για το επόμενο καλοκαίρι ή τον επόμενο χρόνο;",
        "english": "What are your plans for next summer or next year? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Future tense (Συνοπτικός Μέλλοντας: θα δώσω εξετάσεις, θα ταξιδέψω, θα ξεκουραστώ) & intention verbs (σκοπεύω να)"
        },
        "notes": "Examiner Objective: Tests Future tense (`Θα + Συνοπτικός Μέλλοντας`) and future planning verbs (`σκοπεύω να`, `ελπίζω να`).\nStrategy: Connect passing the A2 Greek exam with a celebratory trip to Greece.",
        "keg_communicative_function": "Stating concrete future plans and upcoming personal goals",
        "example_el": "Αυτή την εποχή ετοιμάζομαι για τις εξετάσεις των ελληνικών και το επόμενο καλοκαίρι σκοπεύω να ταξιδέψω στην Ελλάδα για να γιορτάσω με φίλους.",
        "example_en": "Right now I am preparing for the Greek exams and next summer I intend to travel to Greece to celebrate with friends.",
        "example2_el": "Τον επόμενο χρόνο θα συνεχίσω τα μαθήματα ελληνικών στο επόμενο επίπεδο και ελπίζω να επισκεφτώ την Αθήνα και την Κρήτη.",
        "example2_en": "Next year I will continue my Greek lessons at the next level and I hope to visit Athens and Crete."
    },
    {
        "id": "SP-U05-040",
        "greek": "Πού φαντάζεστε τον εαυτό σας σε τρία χρόνια από τώρα;",
        "english": "Where do you imagine yourself three years from now? (Stage 3 Extension Question)",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 (Personal Extension)",
            "focus": "Future continuous & perfective expectations (ελπίζω ότι θα μιλάω, θα έχω, θα περνάω περισσότερο χρόνο)"
        },
        "notes": "Examiner Objective: Concluding Stage 3 prompt testing aspirational future narration.\nStrategy: Combine language fluency goal, career/family happiness, and connection to Greece.",
        "keg_communicative_function": "Expressing long-term personal aspirations and future lifestyle visions",
        "example_el": "Σε τρία χρόνια από τώρα ελπίζω ότι θα μιλάω πολύ καλά ελληνικά, θα έχω μια όμορφη καθημερινότητα και θα περνάω κάθε καλοκαίρι στην Ελλάδα.",
        "example_en": "Three years from now I hope that I will speak Greek very well, have a lovely daily life, and spend every summer in Greece.",
        "example2_el": "Φαντάζομαι τον εαυτό μου σε ένα πιο ήσυχο σπίτι κοντά στη φύση, με καλή υγεία και περισσότερο ελεύθερο χρόνο για ταξίδια και φίλους.",
        "example2_en": "I imagine myself in a quieter house near nature, with good health and more free time for travel and friends."
    },
]

# ---------------------------------------------------------------------------
# UNIT SP-06 CARDS (40 cards: SP-U06-001 .. SP-U06-040)
# Theme: Προφορά, Επιτονισμός & Παγίδες Προφορικού Λόγου (Spoken Phonology & Trap Drills)
# ---------------------------------------------------------------------------
CARDS_SP_06 = [
    # --- 001–010: Voiced vs. Unvoiced Nasal Stops (μπ/π, ντ/τ, γκ/γ/κ, τζ/τσ) ---
    {
        "id": "SP-U06-001",
        "greek": "Ο μπαμπάς μου πήγε στο περίπτερο για να πάρει εφημερίδα.",
        "english": "My dad went to the kiosk to get a newspaper. (Phonology & Nasal Stop Drill)",
        "phonetic_hint": "[o baˈbas mu ˈpije sto peˈriptero ja na ˈpari efimeˈriða] — Contrast voiced bilabial [b] in 'μπαμπάς' with unaspirated voiceless [p] in 'πήγε / περίπτερο / πάρει'.",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Voiced bilabial stop μπ [b/mb] vs. voiceless unaspirated stop π [p]"
        },
        "notes": "Examiner Objective: English speakers often aspirate Greek /p/ ([pʰ]) or confuse initial μπ [b] with π [p].\nStrategy: Keep π crisp and unaspirated (like Spanish/French p), and voice μπ fully from the vocal cords.",
        "keg_communicative_function": "Articulating voiced and voiceless bilabial stops clearly in everyday narrative",
        "example_el": "Το πρωί ο μπαμπάς μου πίνει πάντα έναν ελληνικό καφέ στο μπαλκόνι πριν πάει με τα πόδια στο περίπτερο της γειτονιάς.",
        "example_en": "In the morning my dad always drinks a Greek coffee on the balcony before going on foot to the neighborhood kiosk.",
        "example2_el": "Μπορείς να περάσεις από το περίπτερο και να πάρεις δύο μπουκάλια παγωμένο νερό για την παραλία;",
        "example2_en": "Can you pass by the kiosk and get two bottles of ice-cold water for the beach?"
    },
    {
        "id": "SP-U06-002",
        "greek": "Μπαίνω στο μπάνιο, πλένω τα χέρια μου και πιάνω μια καθαρή πετσέτα.",
        "english": "I go into the bathroom, wash my hands, and grab a clean towel. (Phonology & Nasal Stop Drill)",
        "phonetic_hint": "[ˈbeno sto ˈbaɲo, ˈpleno ta ˈçerja mu ce ˈpjano mɲa kaθaˈri peˈtseta] — Initial μπ [b] ('μπαίνω', 'μπάνιο') vs. cluster πλ [pl] and π+ι [pj] ('πλένω', 'πιάνω').",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Word-initial μπ [b] vs. voiceless bilabial clusters πλ [pl] and πι [pj]"
        },
        "notes": "Examiner Objective: Tests rapid alternation between [b] and [p] in household routine verbs.\nStrategy: Practice the transition `στο μπάνιο [sto ˈbaɲo]` -> `πλένω [ˈpleno]` without puffing air on `π`.",
        "keg_communicative_function": "Describing daily hygiene routines with accurate bilabial articulation",
        "example_el": "Μόλις μπαίνω στο σπίτι, πηγαίνω κατευθείαν στο μπάνιο, πλένω καλά τα χέρια μου με σαπούνι και παίρνω μια μικρή πετσέτα.",
        "example_en": "As soon as I enter the house, I go straight to the bathroom, wash my hands well with soap, and take a small towel.",
        "example2_el": "Στο μπάνιο του ξενοδοχείου υπάρχουν πάντα καθαρές πετσέτες, σαμπουάν και ζεστό νερό όλη την ημέρα.",
        "example2_en": "In the hotel bathroom there are always clean towels, shampoo, and hot water all day long."
    },
    {
        "id": "SP-U06-003",
        "greek": "Ντύνομαι γρήγορα γιατί έχω ραντεβού στις πέντε το απόγευμα.",
        "english": "I get dressed quickly because I have an appointment at five in the afternoon. (Phonology & Nasal Stop Drill)",
        "phonetic_hint": "[ˈdinome ˈɣriɣora jaˈti ˈexo radeˈvu stis ˈpende to aˈpojevma] — Initial ντ [d] in 'ντύνομαι' and word-internal ντ [nd/d] in 'ραντεβού' and 'πέντε'.",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Voiced alveolar stop ντ [d/nd] vs. voiceless dental/alveolar stop τ [t]"
        },
        "notes": "Examiner Objective: Evaluates clarity of `ντ` in core time and scheduling words (`πέντε`, `έντεκα`, `ραντεβού`, `ντύνομαι`).\nStrategy: Never pronounce `πέντε` as `[pente]` with a voiceless `[t]`; soften the dental stop to `[ˈpende]` or `[ˈpede]`.",
        "keg_communicative_function": "Stating appointment times and preparation routines with natural nasal-stop voicing",
        "example_el": "Κάθε απόγευμα στις πέντε και τέταρτο ντύνομαι, παίρνω την τσάντα μου και φεύγω για το ραντεβού μου στο κέντρο.",
        "example_en": "Every afternoon at five fifteen I get dressed, take my bag, and leave for my appointment in the center.",
        "example2_el": "Έκλεισα ραντεβού με τον οδοντίατρο την Τετάρτη στις έντεκα το πρωί, επειδή με πονάει πολύ το δόντι μου.",
        "example2_en": "I booked an appointment with the dentist on Wednesday at eleven in the morning, because my tooth hurts a lot."
    },
    {
        "id": "SP-U06-004",
        "greek": "Στο εστιατόριο παραγγείλαμε ντοματοσαλάτα, πατάτες τηγανητές και τυρί.",
        "english": "At the restaurant we ordered tomato salad, fried potatoes, and cheese. (Phonology & Nasal Stop Drill)",
        "phonetic_hint": "[sto estiaˈtorio paraˈɟilame domatosaˈlata, paˈtates tiɣaniˈtes ce tiˈri] — Contrast initial ντ [d] ('ντοματοσαλάτα') with crisp dental τ [t] ('πατάτες τηγανητές', 'τυρί').",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Contrastive articulation of ντ [d], γγ [ɟ], and dental τ [t] in food ordering"
        },
        "notes": "Examiner Objective: Tests pronunciation of high-frequency taverna items in Stage 2/3.\nStrategy: Keep the tongue against the upper teeth for unaspirated `τ` in `πατάτες τηγανητές`.",
        "keg_communicative_function": "Ordering food and describing meals with clear dental and palatal stops",
        "example_el": "Όταν τρώμε στην ταβέρνα, παίρνουμε πάντα μια φρέσκια ντοματοσαλάτα με φέτα, ζεστές πατάτες τηγανητές και ψητό κοτόπουλο.",
        "example_en": "When we eat at the taverna, we always get a fresh tomato salad with feta, hot fried potatoes, and grilled chicken.",
        "example2_el": "Μου αρέσουν πολύ οι κόκκινες ντομάτες το καλοκαίρι, ειδικά όταν τις κόβω σε σαλάτα με ελαιόλαδο και ρίγανη.",
        "example2_en": "I really like red tomatoes in the summer, especially when I cut them into a salad with olive oil and oregano."
    },
    {
        "id": "SP-U06-005",
        "greek": "Έχω ανάγκη από λίγο ελεύθερο χρόνο για να ξεκουραστώ στον κήπο.",
        "english": "I need a little free time to rest in the garden. (Phonology & Nasal Stop Drill)",
        "phonetic_hint": "[ˈexo aˈnaɟi aˈpo ˈliɣo eˈlefθero ˈxrono ja na ksekuraˈsto ston ˈcipo] — Palatalized γκ [ɟ/ɲɟ] before front vowel [i] in 'ανάγκη' and sandhi 'στον κήπο' [ston ˈɟipo / ston ˈcipo].",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Palatal vs. velar nasal stops γκ/γγ ([ɟ/g]) andvoiceless velar/palatal κ ([k/c])"
        },
        "notes": "Examiner Objective: Candidates frequently mispronounce `ανάγκη` as `[anagi]` with a hard velar instead of palatal `[aˈnaɟi / aˈnaɲɟi]`.\nStrategy: Before `ε/ι` (`ανάγκη`, `άγγελος`, `αγκινάρα`), soften `γκ/γγ` toward the hard palate.",
        "keg_communicative_function": "Expressing personal need for rest with accurate palatal and velar consonants",
        "example_el": "Μετά από τόσες ώρες δουλειάς στο γραφείο, έχω πραγματικά ανάγκη να καθίσω ήσυχα στον κήπο και να πιω έναν καφέ.",
        "example_en": "After so many hours of work at the office, I really need to sit quietly in the garden and drink a coffee.",
        "example2_el": "Ο παππούς μου περνάει όλο το πρωί στον κήπο του σπιτιού, γιατί του αρέσει να ποτίζει τις τριανταφυλλιές και τα λαχανικά.",
        "example2_en": "My grandfather spends the whole morning in the house garden, because he likes watering the rosebushes and the vegetables."
    },
    {
        "id": "SP-U06-006",
        "greek": "Το γκαράζ της πολυκατοικίας βρίσκεται ακριβώς στη γωνία του δρόμου.",
        "english": "The apartment building's garage is located right on the corner of the street. (Phonology & Nasal Stop Drill)",
        "phonetic_hint": "[to gaˈraz tis polikatiˈcias ˈvriscete akriˈvos sti ɣoˈnia tu ˈðromu] — Hard voiced velar stop γκ [g] in 'γκαράζ' vs. voiced velar fricative γ [ɣ] in 'γωνία'.",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Distinguishing voiced velar stop γκ [g] ('γκαράζ', 'γκρι') from voiced velar fricative γ [ɣ] ('γωνία', 'γάλα')"
        },
        "notes": "Examiner Objective: L2 speakers often replace the Greek fricative `γ [ɣ]` (`γωνία`) with the English hard stop `[g]` (`γκαράζ`).\nStrategy: Let air flow smoothly through the back of the throat for `γωνία [ɣoˈnia]`, and make a full stop only on `γκαράζ [gaˈraz]`.",
        "keg_communicative_function": "Giving spatial directions and describing building facilities with clear velar contrasts",
        "example_el": "Αφήνω πάντα το γκρι αυτοκίνητό μου στο υπόγειο γκαράζ, που βρίσκεται ακριβώς στη γωνία δίπλα στον φούρνο της γειτονιάς.",
        "example_en": "I always leave my grey car in the underground garage, which is located right on the corner next to the neighborhood bakery.",
        "example2_el": "Στη γωνία του δρόμου μας άνοιξε ένα καινούργιο γαλακτοπωλείο που πουλάει φρέσκο γάλα, γιαούρτι και παραδοσιακά γλυκά.",
        "example2_en": "On the corner of our street a new dairy shop opened that sells fresh milk, yogurt, and traditional sweets."
    },
    {
        "id": "SP-U06-007",
        "greek": "Ήπια ένα φλιτζάνι ζεστό τσάι με λεμόνι γιατί είχα έντονο βήχα.",
        "english": "I drank a cup of hot tea with lemon because I had a bad cough. (Phonology & Affricate Drill)",
        "phonetic_hint": "[ˈipja ˈena fliˈdzani zeˈsto ˈtsai me leˈmoni jaˈti ˈixa ˈendono ˈvixa] — Voiced alveolar affricate τζ [dz] ('φλιτζάνι') vs. voiceless affricate τσ [ts] ('τσάι').",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Alveolar affricates τζ [dz] vs. τσ [ts] (avoiding postalveolar English [dʒ]/[tʃ])"
        },
        "notes": "Examiner Objective: Greek `τσ/τζ` are crisp dental-alveolar `[ts/dz]`, never thick English `ch/j` (`[tʃ/dʒ]`).\nStrategy: Keep the tongue tip behind the front teeth when saying `φλιτζάνι`, `τζάκι`, `τσάι`, and `τσάντα`.",
        "keg_communicative_function": "Describing remedies for minor illnesses using accurate dental-alveolar affricates",
        "example_el": "Τον χειμώνα μου αρέσει να κάθομαι δίπλα στο τζάκι και να πίνω ένα μεγάλο φλιτζάνι ζεστό τσάι του βουνού με μέλι.",
        "example_en": "In winter I like sitting next to the fireplace and drinking a large cup of hot mountain tea with honey.",
        "example2_el": "Ξέχασα την καινούργια μου τσάντα και το πορτοφόλι μου πάνω στο τραπεζάκι της καφετέριας, δίπλα στο τζάμι.",
        "example2_en": "I forgot my new bag and my wallet on the small table of the café, next to the windowpane."
    },
    {
        "id": "SP-U06-008",
        "greek": "Δεν μπορώ να καταλάβω γιατί το λεωφορείο αργεί πάντα στον σταθμό.",
        "english": "I cannot understand why the bus is always late at the station. (Phonology & Sandhi Assimilation Drill)",
        "phonetic_hint": "[ðem boˈro na kataˈlavo jaˈti to leofoˈrio arˈji ˈpanda ston staˈθmo] — Cross-word nasal assimilation: 'δεν μπορώ' -> [ðem boˈro], 'στον σταθμό' -> [sto(n) staˈθmo].",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Connected speech nasal sandhi (δεν + π/μπ -> [mb], την + π -> [mb], τον + κ -> [ŋg])"
        },
        "notes": "Examiner Objective: Natural spoken Greek links `δεν/μην/τον/την/στον/στην` smoothly into the following stop without an artificial pause.\nStrategy: Pronounce `δεν μπορώ` as a single rhythmic unit `[ðemboˈro]` and `δεν πειράζει` as `[ðembiˈrazi]`.",
        "keg_communicative_function": "Using natural connected-speech sandhi in everyday complaints and observations",
        "example_el": "Δεν πειράζει αν αργήσεις πέντε λεπτά στο ραντεβού μας, γιατί κι εγώ περιμένω ακόμα στην πόρτα του σταθμού.",
        "example_en": "It doesn't matter if you are five minutes late to our appointment, because I too am still waiting at the station door.",
        "example2_el": "Την Παρασκευή το απόγευμα δεν μπορώ να έρθω μαζί σας στον κινηματογράφο, επειδή έχω μάθημα ελληνικών.",
        "example2_en": "On Friday afternoon I cannot come with you to the cinema, because I have a Greek lesson."
    },
    {
        "id": "SP-U06-009",
        "greek": "Την Κυριακή το πρωί πήγαμε μια μεγάλη εκδρομή στην εξοχή με τους γονείς μας.",
        "english": "On Sunday morning we went on a big excursion to the countryside with our parents. (Phonology & Sandhi Drill)",
        "phonetic_hint": "[tiŋ ɟirjaˈci to proˈi ˈpiɣame mɲa meˈɣali ekðroˈmi stin eksoˈçi me tuz ɣoˈniz mas] — Connected speech voicing: 'Την Κυριακή' [tiŋ ɟirjaˈci], 'με τους γονείς' [me tuz ɣoˈnis].",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Cross-word assimilation: την Κυριακή [tiŋ ɟirjaˈci] and final -ς voicing before voiced consonants (τους γονείς [tuz ɣoˈnis])"
        },
        "notes": "Examiner Objective: Trains smooth phrase-level prosody instead of choppy word-by-word reading.\nStrategy: Link article + noun (`την Κυριακή`, `τους γονείς`) without breaking airflow.",
        "keg_communicative_function": "Narrating weekend outings with smooth phrase-level prosody and consonant linking",
        "example_el": "Την Κυριακή που μας πέρασε, πήραμε το αυτοκίνητο και πήγαμε με τους φίλους μας σε ένα όμορφο χωριό κοντά στη θάλασσα.",
        "example_en": "Last Sunday, we took the car and went with our friends to a beautiful village near the sea.",
        "example2_el": "Μου αρέσει να περνάω την Κυριακή μου ήρεμα στο σπίτι με τους γονείς μου και να τρώμε όλοι μαζί το μεσημέρι.",
        "example2_en": "I like spending my Sunday quietly at home with my parents and eating all together at noon."
    },
    {
        "id": "SP-U06-010",
        "greek": "Ο άντρας της αδερφής μου δουλεύει σε μια μεγάλη τράπεζα στην Αθήνα.",
        "english": "My sister's husband works at a big bank in Athens. (Phonology & Cluster Drill)",
        "phonetic_hint": "[o ˈandras tis aðerˈfiz mu ðuˈlevi se mɲa meˈɣali ˈtrapeza stin aˈθina] — Contrast voiced cluster ντρ [ndr/dr] ('άντρας') with voiceless τρ [tr] ('τράπεζα').",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Cluster contrast ντρ [ndr/dr] ('άντρας', 'δέντρο') vs. τρ [tr] ('τράπεζα', 'τρεις')"
        },
        "notes": "Examiner Objective: Ensures clear distinction between `ντρ` and `τρ` with a single alveolar tap `[ɾ]`.\nStrategy: Use a quick, light tap of the tongue tip for `ρ` right after `[d]` or `[t]`.",
        "keg_communicative_function": "Describing family members and professions with accurate consonant clusters",
        "example_el": "Κάτω από τα μεγάλα δέντρα της πλατείας υπάρχει μια τράπεζα, ένα ταχυδρομείο και τρία μικρά καφέ.",
        "example_en": "Under the big trees of the square there is a bank, a post office, and three small cafés.",
        "example2_el": "Ο άντρας που στέκεται μπροστά στην είσοδο της τράπεζας κρατάει μια μαύρη ομπρέλα και περιμένει το ταξί.",
        "example2_en": "The man standing in front of the bank entrance is holding a black umbrella and waiting for the taxi."
    },

    # --- 011–018: Diphthongs αυ ([av] vs. [af]) and ευ ([ev] vs. [ef]) & Fricatives (χ/γ, θ/δ) ---
    {
        "id": "SP-U06-011",
        "greek": "Αύριο το πρωί θα ταξιδέψω με αυτό το πλοίο για τα νησιά.",
        "english": "Tomorrow morning I will travel on this ship to the islands. (Phonology & Diphthong Drill)",
        "phonetic_hint": "[ˈavrio to proˈi θa taksiˈðepso me afˈto to ˈplio ja ta niˈsça] — Diphthong αυ = [av] before voiced ρ ('αύριο') vs. [af] before voiceless τ ('αυτό').",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Phonological rule for αυ: [av] before vowels and voiced consonants (β, γ, δ, ζ, λ, μ, ν, ρ) vs. [af] before voiceless (κ, π, τ, χ, φ, θ, σ, ξ, ψ)"
        },
        "notes": "Examiner Objective: High-frequency pronunciation criterion in KEG A2.\nStrategy: Hear the instant switch in the same sentence: `αύριο [ˈavrio]` (voiced [v] before ρ) vs. `αυτό [afˈto]` (voiceless [f] before τ).",
        "keg_communicative_function": "Applying thevoiced/voiceless assimilation rule for the digraph αυ in travel statements",
        "example_el": "Αύριο θα ξυπνήσω πολύ νωρίς, γιατί αυτό το λεωφορείο φεύγει στις επτά ακριβώς από την κεντρική αυλή του σταθμού.",
        "example_en": "Tomorrow I will wake up very early, because this bus leaves at seven sharp from the central courtyard of the station.",
        "example2_el": "Σε αυτό το μικρό μαγαζί αγόρασα χθες φρέσκα αυγά, βούτυρο και ωραίο ψωμί για το αυριανό μας πρωινό.",
        "example2_en": "At this small shop yesterday I bought fresh eggs, butter, and nice bread for our breakfast tomorrow."
    },
    {
        "id": "SP-U06-012",
        "greek": "Το αυτοκίνητο είναι παρκαρισμένο στη μικρή αυλή πίσω από το σπίτι.",
        "english": "The car is parked in the small courtyard behind the house. (Phonology & Diphthong Drill)",
        "phonetic_hint": "[to aftoˈcinito ˈine parkarizˈmeno sti miˈkri avˈli ˈpiso aˈpo to ˈspiti] — 'αυτοκίνητο' [aftoˈcinito] ([af] before τ) vs. 'αυλή' [avˈli] ([av] before λ).",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Contrastive αυ in noun pairs: αυτοκίνητο / αυτόματος [af] vs. αυλή / αυγό / Αύγουστος [av]"
        },
        "notes": "Examiner Objective: Tests automatic `[af]` vs. `[av]` production in Stage 3 house/street descriptions.\nStrategy: Remember that `λ`, `γ`, `ρ` are voiced so `αυλή`, `αυγό`, `Αύγουστος` always take `[av]`.",
        "keg_communicative_function": "Describing residential spaces and vehicles with accurate diphthong voicing",
        "example_el": "Τον Αύγουστο καθόμαστε κάθε βράδυ στη δροσερή αυλή του σπιτιού μας, μακριά από τον θόρυβο που κάνουν τα αυτοκίνητα.",
        "example_en": "In August we sit every evening in the cool courtyard of our house, far from the noise that the cars make.",
        "example2_el": "Αφήσαμε το αυτοκίνητό μας έξω από την αυλή και μπήκαμε στο σπίτι για να φτιάξουμε καφέ και τηγανητά αυγά.",
        "example2_en": "We left our car outside the courtyard and went into the house to make coffee and fried eggs."
    },
    {
        "id": "SP-U06-013",
        "greek": "Σας ευχαριστώ πολύ για την ευγενική σας βοήθεια και τη συμβουλή.",
        "english": "Thank you very much for your kind help and advice. (Phonology & Diphthong Drill)",
        "phonetic_hint": "[sas efxariˈsto poˈli ja tin evjeniˈci sas voˈiθja ce ti simvuˈli] — Diphthong ευ = [ef] before voiceless χ ('ευχαριστώ') vs. [ev] before voiced γ ('ευγενική').",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Phonological rule for ευ: [ef] before voiceless consonants ('ευχαριστώ', 'εύκολος', 'ελεύθερος') vs. [ev] before voiced ('ευγενικός', 'εβδομάδα', 'ταξιδεύω')"
        },
        "notes": "Examiner Objective: `Ευχαριστώ` and `ευγενικός` are essential politeness words in Stage 2 roleplays.\nStrategy: Pronounce `ευχαριστώ` with a clear `[efx-]` and `ευγενική` with a smooth voiced `[evj-]`. Note also `συμβουλή [simvuˈli]`.",
        "keg_communicative_function": "Expressing polite gratitude with accurate articulation of the digraph ευ",
        "example_el": "Ο υπάλληλος στο ξενοδοχείο ήταν πάρα πολύ ευγενικός και τον ευχαρίστησα θερμά γιατί μας βρήκε εύκολα ένα ήσυχο δωμάτιο.",
        "example_en": "The clerk at the hotel was very polite and I thanked him warmly because he easily found us a quiet room.",
        "example2_el": "Την Παρασκευή έχω ελεύθερο χρόνο το απόγευμα, οπότε είναι ευκαιρία να μαγειρέψω κάτι ωραίο για τους φίλους μου.",
        "example2_en": "On Friday I have free time in the afternoon, so it is an opportunity to cook something nice for my friends."
    },
    {
        "id": "SP-U06-014",
        "greek": "Την Παρασκευή το βράδυ μαγειρεύω πάντα κάτι εύκολο και νόστιμο.",
        "english": "On Friday evening I always cook something easy and tasty. (Phonology & Diphthong Drill)",
        "phonetic_hint": "[tim paraskeˈvi to ˈvraði majiˈrevo ˈpanda ˈkati ˈefkolo ce ˈnostimo] — Contrast [ev] before vowels ('Παρασκευή', 'μαγειρεύω') with [ef] before κ ('εύκολο').",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Productive verb suffix -εύω [ˈevo] (Present) vs. -έψω [ˈepso] (Aorist subjunctive) and adjective εύκολος [ˈefkolos]"
        },
        "notes": "Examiner Objective: Verbs in `-εύω` (`δουλεύω`, `μαγειρεύω`, `ταξιδεύω`, `χορεύω`) always have `[ev]` in the Present tense because a vowel follows.\nStrategy: Practice `μαγειρεύω [majiˈrevo]` vs. `εύκολο [ˈefkolo]`.",
        "keg_communicative_function": "Describing end-of-week cooking habits while contrasting [ev] and [ef]",
        "example_el": "Κάθε Παρασκευή τελειώνω τη δουλειά μου στις τέσσερις, ξεκουράζομαι λίγο και μετά μαγειρεύω μια εύκολη μακαρονάδα για την οικογένεια.",
        "example_en": "Every Friday I finish my work at four, rest a bit, and afterwards cook an easy pasta dish for the family.",
        "example2_el": "Είναι πολύ εύκολο να ταξιδεύεις με το τρένο στην Ευρώπη, γιατί τα δρομολόγια είναι συχνά και άνετα.",
        "example2_en": "It is very easy to travel by train in Europe, because the routes are frequent and comfortable."
    },
    {
        "id": "SP-U06-015",
        "greek": "Δεν θέλω να δω τηλεόραση απόψε, προτιμώ να διαβάσω ένα βιβλίο.",
        "english": "I don't want to watch television tonight, I prefer to read a book. (Phonology & Dental Fricative Drill)",
        "phonetic_hint": "[ðen ˈθelo na ðo tileˈorasi aˈpopse, protiˈmo na ðjaˈvaso ˈena viˈvlio] — Alternating voiced interdental δ [ð] ('δεν', 'δω', 'διαβάσω') and voiceless θ [θ] ('θέλω').",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Interdental fricatives δ [ð] (as in 'this') vs. θ [θ] (as in 'think') without stopping to [d] or [t]"
        },
        "notes": "Examiner Objective: Rapid `δ - θ - δ` sequences (`δεν θέλω να δω`) often cause learners to slip into `[d]` or confuse voicing.\nStrategy: Keep the tip of the tongue lightly between the teeth for the entire opening phrase `Δεν θέλω να δω [ðen ˈθelo na ðo]`.",
        "keg_communicative_function": "Stating evening leisure preferences with clear interdental fricative articulation",
        "example_el": "Δεν θέλω να βγω έξω απόψε γιατί κάνει κρύο, γι' αυτό θα καθίσω στο δωμάτιό μου να διαβάσω δύο κεφάλαια από το βιβλίο μου.",
        "example_en": "I don't want to go out tonight because it is cold, so I will sit in my room to read two chapters from my book.",
        "example2_el": "Τηλεφώνησα στον Δημήτρη και του είπα ότι θα τον δω την Πέμπτη το βράδυ στο θέατρο της γειτονιάς μας.",
        "example2_en": "I phoned Dimitris and told him that I will see him on Thursday evening at our neighborhood theater."
    },
    {
        "id": "SP-U06-016",
        "greek": "Ο θείος μου μένει σε έναν ήσυχο δρόμο δίπλα στη θάλασσα.",
        "english": "My uncle lives on a quiet street next to the sea. (Phonology & Dental Fricative Drill)",
        "phonetic_hint": "[o ˈθios mu ˈmeni se ˈenan ˈisixo ˈðromo ˈðipla sti ˈθalassa] — Symmetric alternation: θ [θ] ('θείος') -> δ [ð] ('δρόμο', 'δίπλα') -> θ [θ] ('θάλασσα').",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Interdental fricative minimal-pair environments (θείος/θάλασσα [θ] vs. δρόμος/δίπλα/δωμάτιο [ð])"
        },
        "notes": "Examiner Objective: Evaluates continuous fricative airflow in spatial and family descriptions.\nStrategy: Ensure `δρόμος` starts with a smooth `[ðr-]`, not `[dr-]`. ",
        "keg_communicative_function": "Describing residential locations using accurate voiceless and voiced dental fricatives",
        "example_el": "Κάθε καλοκαίρι πηγαίνω στο σπίτι του θείου μου, που έχει μεγάλη βεράντα με υπέροχη θέα στη γαλάζια θάλασσα.",
        "example_en": "Every summer I go to my uncle's house, which has a big veranda with a wonderful view of the blue sea.",
        "example2_el": "Ο δρόμος μπροστά από την παραλία έχει πολλά δέντρα και είναι ιδανικός για απογευματινό περίπατο δίπλα στη θάλασσα.",
        "example2_en": "The street in front of the beach has many trees and is ideal for an afternoon walk next to the sea."
    },
    {
        "id": "SP-U06-017",
        "greek": "Χθες το βράδυ είχε πολλή ομίχλη και ψυχρό αέρα στον δρόμο.",
        "english": "Last night there was heavy fog and cold air on the road. (Phonology & Velar/Palatal Fricative Drill)",
        "phonetic_hint": "[xθes to ˈvraði ˈiçe poˈli oˈmixli ce psiˈxro aˈera ston ˈðromo] — Voiceless velar fricative χ [x] ('χθες', 'ομίχλη', 'ψυχρό') vs. palatal allophone [ç] before front vowel ('είχε').",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Allophones of χ: velar [x] before a/o/u and consonants ('χθες', 'χρόνος') vs. palatal [ç] before e/i ('είχε', 'όχι', 'χέρι')"
        },
        "notes": "Examiner Objective: English speakers often replace Greek `χ` with a weak glottal `[h]` or hard `[k]`.\nStrategy: Differentiate back-of-mouth `[x]` in `χθες / χρόνος` from forward palatal `[ç]` (like German *ich* or English *huge*) in `είχε / όχι`.",
        "keg_communicative_function": "Describing past weather conditions with accurate velar and palatal fricatives",
        "example_el": "Χθες τον χειμώνα έκανε πολύ κρύο, είχε δυνατό αέρα και χιόνισε στα ψηλά βουνά έξω από την πόλη μας.",
        "example_en": "Yesterday in winter it was very cold, there was a strong wind, and it snowed on the high mountains outside our city.",
        "example2_el": "Ευτυχώς σήμερα ο καιρός είναι πολύ καλύτερος, έχει ζεστό ήλιο και δεν έχει καθόλου ομίχλη στους δρόμους.",
        "example2_en": "Fortunately today the weather is much better, there is warm sunshine and there is no fog at all on the roads."
    },
    {
        "id": "SP-U06-018",
        "greek": "Η γιαγιά μου μαγειρεύει γρήγορα ένα γευστικό γεύμα για τα εγγόνια της.",
        "english": "My grandmother quickly cooks a tasty meal for her grandchildren. (Phonology & Palatal/Velar Fricative Drill)",
        "phonetic_hint": "[i jaˈja mu majiˈrevi ˈɣriɣora ˈena jefstiˈko ˈjevma ja ta eˈgoɲa tis] — Palatal glide γ [j] before front vowels ('γιαγιά', 'μαγειρεύει', 'γεύμα') vs. velar fricative [ɣ] ('γρήγορα') and stop εγγ [g] ('εγγόνια').",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Pronunciation & Intonation)",
            "focus": "Three-way realization of gamma: palatal [j] ('γιαγιά', 'γεύμα'), velar fricative [ɣ] ('γρήγορα', 'γάλα'), and nasal stop εγγ [g/ŋg] ('εγγόνια')"
        },
        "notes": "Examiner Objective: Showcases all three sounds of `γ` in a single natural sentence.\nStrategy: Make `γιαγιά / γεύμα` glide like English *y* `[j]`, keep `γρήγορα` a soft throat fricative `[ɣ]`, and make `εγγόνια` a clear stop `[eˈgoɲa]`.",
        "keg_communicative_function": "Describing family meals while mastering all three phonological realizations of gamma",
        "example_el": "Κάθε Κυριακή η γιαγιά μας ετοιμάζει στην κουζίνα της ένα μεγάλο οικογενειακό γεύμα και φτιάχνει γλυκό με φρέσκο γάλα.",
        "example_en": "Every Sunday our grandmother prepares a big family meal in her kitchen and makes dessert with fresh milk.",
        "example2_el": "Τα εγγόνια αγαπούν πολύ τις ιστορίες που τους λέει η γιαγιά τους, όταν κάθονται μαζί το απόγευμα στο σαλόνι.",
        "example2_en": "The grandchildren really love the stories their grandmother tells them when they sit together in the afternoon in the living room."
    },

    # --- 019–028: Stress-Placement & Aspect Traps Under Exam Pressure ---
    {
        "id": "SP-U06-019",
        "greek": "Τώρα μένω στην Αθήνα, αλλά πέρσι έμεινα για έξι μήνες στη Θεσσαλονίκη.",
        "english": "Now I live in Athens, but last year I stayed for six months in Thessaloniki. (Stress Shift & Aspect Drill)",
        "phonetic_hint": "[ˈtora ˈmeno stin aˈθina, aˈla ˈpersi ˈemina ja ˈeksi ˈmines sti θesaloˈnici] — Antepenultimate Aorist stress shift: Present 'μένω' [ˈmeno] -> Aorist 'έμεινα' [ˈemina] -> Subjunctive 'να μείνω' [na ˈmino].",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 2 & 4 (Morphological Accuracy & Stress Placement)",
            "focus": "Contrastive stress and vowel/aspect shift: μένω (Present) vs. έμεινα (Aorist) vs. θα μείνω (Future/Subjunctive)"
        },
        "notes": "Examiner Objective: Note that `μένω` (`-ε-`) and `να μείνω` (`-ει-`) sound identical `[ˈmeno]` vs. `[ˈmino]` in vowel change, while Aorist pulls stress back to the augment `έμεινα [ˈemina]`.\nStrategy: Anchor `τώρα μένω`, `πέρσι έμεινα`, and `του χρόνου θα μείνω`.",
        "keg_communicative_function": "Contrasting current residence with past stays using accurate Aorist stress retraction",
        "example_el": "Σήμερα μένω σε ένα μικρό διαμέρισμα στο κέντρο, αλλά το επόμενο καλοκαίρι θα μείνω για έναν μήνα στο σπίτι μας στο νησί.",
        "example_en": "Today I live in a small apartment in the center, but next summer I will stay for a month at our house on the island.",
        "example2_el": "Όταν πήγαμε εκδρομή στο Ναύπλιο, μείναμε σε ένα παραδοσιακό ξενοδοχείο κοντά στο λιμάνι και περάσαμε υπέροχα.",
        "example2_en": "When we went on an excursion to Nafplio, we stayed in a traditional hotel near the port and had a wonderful time."
    },
    {
        "id": "SP-U06-020",
        "greek": "Συνήθως δουλεύω μέχρι τις πέντε, αλλά χθες δούλεψα μέχρι τις οκτώ το βράδυ.",
        "english": "Usually I work until five, but yesterday I worked until eight in the evening. (Stress Shift & Aspect Drill)",
        "phonetic_hint": "[siˈniθos ðuˈlevo ˈmexri tis ˈpende, aˈla xθes ˈðulepsa ˈmexri tis oˈkto to ˈvraði] — Stress shift & [ev]->[eps] change: 'δουλεύω' [ðuˈlevo] -> 'δούλεψα' [ˈðulepsa] -> 'να δουλέψω' [na ðuˈlepso].",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 2 & 4 (Morphological Accuracy & Stress Placement)",
            "focus": "Paroxytone Present δουλεύω [ðuˈlevo] vs. proparoxytone Aorist δούλεψα [ˈðulepsa] vs. Aorist subjunctive να δουλέψω [ðuˈlepso]"
        },
        "notes": "Examiner Objective: Under exam pressure, candidates often misstress the Aorist as `*δουλέψα` instead of `δούλεψα`.\nStrategy: Pull the stress back to the first syllable (`δού-λε-ψα`) in the singular Aorist, and return it to `-λέ-` in the plural (`δουλέψαμε`) and subjunctive (`να δουλέψω`).",
        "keg_communicative_function": "Comparing regular working hours with past overtime using accurate verb stress",
        "example_el": "Αυτή την εβδομάδα δουλεύω από το πρωί, αλλά το Σάββατο δεν θα δουλέψω καθόλου γιατί θέλω να ξεκουραστώ.",
        "example_en": "This week I am working from the morning, but on Saturday I will not work at all because I want to rest.",
        "example2_el": "Πέρσι το καλοκαίρι δούλεψα σε ένα τουριστικό γραφείο στο νησί και γνώρισα πολλούς ανθρώπους από όλο τον κόσμο.",
        "example2_en": "Last summer I worked at a tourist office on the island and met many people from all over the world."
    },
    {
        "id": "SP-U06-021",
        "greek": "Κάθε βράδυ πλένω τα πιάτα, αλλά χθες τα έπλυνα αμέσως μετά το μεσημεριανό.",
        "english": "Every evening I wash the dishes, but yesterday I washed them right after lunch. (Stress Shift & Aspect Drill)",
        "phonetic_hint": "[ˈkaθe ˈvraði ˈpleno ta ˈpjata, aˈla xθes ta ˈeplina aˈmesos meˈta to mesimerjaˈno] — Vowel & stress shift: 'πλένω' [ˈpleno] -> 'έπλυνα' [ˈeplina] -> 'να πλύνω' [na ˈplino].",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 2 & 4 (Morphological Accuracy & Stress Placement)",
            "focus": "Stem vowel raising (-ε- to -υ- [i]) and Aorist stress shift: πλένω -> έπλυνα -> θα πλύνω"
        },
        "notes": "Examiner Objective: Tests household chore verbs where `-ε-` raises to `-υ- [i]` in the Aorist/Subjunctive (`πλένω -> έπλυνα / να πλύνω`).\nStrategy: Notice the vowel change `[e] -> [i]` between `πλένω` (habitual) and `να πλύνω` (single action).",
        "keg_communicative_function": "Describing daily household chores across Present, Aorist, and Subjunctive",
        "example_el": "Πρέπει να πλύνω τα φρούτα με άφθονο νερό πριν τα βάλω στο τραπέζι για να φάμε όλοι μαζί.",
        "example_en": "I must wash the fruit with plenty of water before putting them on the table for us all to eat together.",
        "example2_el": "Το Σάββατο το πρωί πλύναμε το αυτοκίνητο στην αυλή και βάλαμε πλυντήριο όλα τα ρούχα της εβδομάδας.",
        "example2_en": "On Saturday morning we washed the car in the courtyard and put all the week's clothes in the washing machine."
    },
    {
        "id": "SP-U06-022",
        "greek": "Παίρνω το λεωφορείο κάθε πρωί και περνάω μπροστά από το μεγάλο πάρκο.",
        "english": "I take the bus every morning and pass in front of the big park. (Minimal Pair & Aspect Trap Drill)",
        "phonetic_hint": "[ˈperno to leofoˈrio ˈkaθe proˈi ce perˈnao broˈsta aˈpo to meˈɣalo ˈparko] — Crucial minimal pair: 'παίρνω / πήρα' (take) vs. 'περνάω / πέρασα' (pass/spend time).",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 2 & 4 (Lexical-Phonological Minimal Pair & Stress)",
            "focus": "Distinguishing παίρνω [ˈperno] -> πήρα [ˈpira] (take) from περνώ/περνάω [perˈnao] -> πέρασα [ˈperasa] (pass/spend time)"
        },
        "notes": "Examiner Objective: One of the most common A2 speaking traps is confusing `παίρνω` (stress on 1st syllable: *take*) with `περνώ/περνάω` (stress on 2nd syllable: *pass/spend time*).\nStrategy: Memorize the pair in one breath: `πήρα το τρένο` (I took the train) vs. `πέρασα ωραία` (I had a nice time).",
        "keg_communicative_function": "Distinguishing between 'taking transport/items' (παίρνω) and 'passing by/spending time' (περνάω)",
        "example_el": "Χθες πήρα τηλέφωνο τον φίλο μου, πέρασα από το σπίτι του με το αυτοκίνητο και περάσαμε ένα πολύ όμορφο απόγευμα.",
        "example_en": "Yesterday I called my friend on the phone, passed by his house by car, and we spent a very lovely afternoon.",
        "example2_el": "Όταν γυρίζω από τη δουλειά, περνάω πάντα από τον φούρνο για να πάρω φρέσκο ψωμί για το βραδινό μας.",
        "example2_en": "When I return from work, I always pass by the bakery to get fresh bread for our dinner."
    },
    {
        "id": "SP-U06-023",
        "greek": "Τις καθημερινές γυρίζω στο σπίτι στις έξι, αλλά χθες γύρισα στις εννέα.",
        "english": "On weekdays I return home at six, but yesterday I returned at nine. (Stress Shift Drill)",
        "phonetic_hint": "[tis kaθimeriˈnes jiˈrizo sto ˈspiti stis ˈeksi, aˈla xθes ˈjirisa stis eˈnea] — Stress shift: Present 'γυρίζω' [jiˈrizo] -> Aorist 'γύρισα' [ˈjirisa] -> Subjunctive 'να γυρίσω' [na jiˈriso].",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 2 & 4 (Morphological Accuracy & Stress Placement)",
            "focus": "Verbs in -ίζω: paroxytone Present γυρίζω [jiˈrizo] vs. proparoxytone Aorist γύρισα [ˈjirisa]"
        },
        "notes": "Examiner Objective: Spoken Greek relies heavily on `-ίζω` verbs (`γυρίζω`, `αρχίζω`, `νομίζω`, `ψωνίζω`), all of which shift stress to the antepenult in the Aorist.\nStrategy: Contrast `γυρίζω [jiˈrizo]` with `γύρισα [ˈjirisa]`, and remember 1st plural shifts back to `γυρίσαμε [jiˈrisame]`.",
        "keg_communicative_function": "Reporting daily return times versus past exceptions with accurate -ίζω stress patterns",
        "example_el": "Αύριο θα γυρίσω νωρίς από το γραφείο, γιατί θέλω να ψωνίσω στη λαϊκή αγορά πριν κλείσουν οι πάγκοι.",
        "example_en": "Tomorrow I will return early from the office, because I want to shop at the farmers' market before the stalls close.",
        "example2_el": "Όταν γυρίσαμε από τις διακοπές μας στο νησί, ξεκουραστήκαμε όλη την Κυριακή και δείξαμε τις φωτογραφίες στους φίλους μας.",
        "example2_en": "When we returned from our holidays on the island, we rested all Sunday and showed the photos to our friends."
    },
    {
        "id": "SP-U06-024",
        "greek": "Το μάθημα αρχίζει στις δέκα ακριβώς, αλλά σήμερα άρχισε δέκα λεπτά πιο αργά.",
        "english": "The lesson starts at ten sharp, but today it started ten minutes later. (Stress Shift Drill)",
        "phonetic_hint": "[to ˈmaθima arˈçizi stis ˈðeka akriˈvos, aˈla ˈsimera ˈarçise ˈðeka leˈpta pço arˈɣa] — Stress retraction: 'αρχίζει' [arˈçizi] -> 'άρχισε' [ˈarçise] -> 'να αρχίσει' [na arˈçisi].",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 2 & 4 (Morphological Accuracy & Stress Placement)",
            "focus": "Contrastive stress on αρχίζω [arˈçizo] vs. άρχισα [ˈarçisa] and palatal [ç] before [i]"
        },
        "notes": "Examiner Objective: Tests both the stress shift (`αρχίζει` vs. `άρχισε`) and the soft palatal `[ç]` before `ι`.\nStrategy: Emphasize the initial `ΑΡ-` in `άρχισε [ˈarçise]`.",
        "keg_communicative_function": "Stating schedules and timing changes with accurate stress placement",
        "example_el": "Πότε άρχισες να μαθαίνεις ελληνικά και πόσες ώρες την εβδομάδα κάνεις μάθημα με τον δάσκαλό σου;",
        "example_en": "When did you start learning Greek and how many hours a week do you have lessons with your teacher?",
        "example2_el": "Η ταινία στον κινηματογράφο θα αρχίσει στις εννέα το βράδυ, οπότε πρέπει να είμαστε εκεί είκοσι λεπτά νωρίτερα.",
        "example2_en": "The movie at the cinema will start at nine in the evening, so we must be there twenty minutes earlier."
    },
    {
        "id": "SP-U06-025",
        "greek": "Συνήθως πληρώνω με κάρτα, αλλά στον φούρνο σήμερα πλήρωσα με μετρητά.",
        "english": "Usually I pay by card, but at the bakery today I paid with cash. (Stress Shift Drill)",
        "phonetic_hint": "[siˈniθos pliˈrono me ˈkarta, aˈla ston ˈfurno ˈsimera ˈplirosa me metriˈta] — Verbs in -ώνω: 'πληρώνω' [pliˈrono] -> 'πλήρωσα' [ˈplirosa] -> 'να πληρώσω' [na pliˈroso].",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 2 & 4 (Morphological Accuracy & Stress Placement)",
            "focus": "Verbs in -ώνω: paroxytone Present πληρώνω [pliˈrono] vs. proparoxytone Aorist πλήρωσα [ˈplirosa]"
        },
        "notes": "Examiner Objective: Essential for Stage 2 shopping/service roleplays (`πληρώνω`, `πλήρωσα`, `να πληρώσω`).\nStrategy: Notice that `πληρώνω` and `να πληρώσω` share the exact same stress position (`-ρώ-`), while only the past `πλήρωσα` moves stress to `πλή-`.",
        "keg_communicative_function": "Discussing payments and transactions across tenses with accurate stress",
        "example_el": "Μπορώ να πληρώσω τον λογαριασμό με την πιστωτική μου κάρτα ή δέχεστε μόνο μετρητά στο κατάστημά σας;",
        "example_en": "Can I pay the bill with my credit card or do you only accept cash at your shop?",
        "example2_el": "Χθες πλήρωσα το ενοίκιο του σπιτιού και τους λογαριασμούς του ρεύματος και του νερού μέσω διαδικτύου.",
        "example2_en": "Yesterday I paid the house rent and the electricity and water bills online."
    },
    {
        "id": "SP-U06-026",
        "greek": "Τελειώνω τη δουλειά μου στις τέσσερις, αλλά χθες τελείωσα στις τρεις και μισή.",
        "english": "I finish my work at four, but yesterday I finished at three thirty. (Stress Shift Drill)",
        "phonetic_hint": "[teˈljono ti ðuˈlja mu stis ˈteseris, aˈla xθes teˈliosa stis tris ce miˈsi] — Synizesis in Present 'τελειώνω' [teˈljono] vs. full vowel stress in Aorist 'τελείωσα' [teˈliosa].",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 2 & 4 (Morphological Accuracy & Stress Placement)",
            "focus": "Syllable count and stress shift in τελειώνω [teˈljono] vs. τελείωσα [teˈliosa] vs. θα τελειώσω [θa teˈljoso]"
        },
        "notes": "Examiner Objective: `Τελειώνω` has palatalized `[lj]` before stressed `-ώ-`, whereas Aorist `τελείωσα` stresses `-λεί- [ˈli]` before `-ωσα`.\nStrategy: Practice the rhythm `[te-ˈljo-no]` -> `[te-ˈli-o-sa]` -> `[θa te-ˈljo-so]`.",
        "keg_communicative_function": "Stating work and study completion times across Present, Past, and Future",
        "example_el": "Μόλις τελειώσω τα μαθήματά μου το απόγευμα, θα σε πάρω τηλέφωνο για να πάμε μαζί μια βόλτα στην παραλία.",
        "example_en": "As soon as I finish my lessons in the afternoon, I will call you so we can go together for a walk on the beach.",
        "example2_el": "Πέρσι τελείωσα το πρώτο επίπεδο των ελληνικών και φέτος ετοιμάζομαι με χαρά για τις εξετάσεις του δευτέρου επιπέδου.",
        "example2_en": "Last year I finished the first level of Greek and this year I am happily preparing for the second-level exams."
    },
    {
        "id": "SP-U06-027",
        "greek": "Το δωμάτιο του ξενοδοχείου μας είναι πολύ φωτεινό και έχει μεγάλο μπαλκόνι.",
        "english": "Our hotel room is very bright and has a large balcony. (Internal Clitic Stress Shift Drill)",
        "phonetic_hint": "[to ðoˈmatio tu ksenoðoˈçiu mas ˈine poˈli fotiˈno ce ˈeçi meˈɣalo balˈkoni] — Genitive stress shift: Nominative 'το ξενοδοχείο' -> Genitive 'του ξενοδοχείου' + enclitic 'μας'.",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 2 & 4 (Nominal Stress & Enclitic Accentuation)",
            "focus": "Enclitic stress rule (ο δάσκαλός μου, το δωμάτιό μας, του αυτοκινήτου μου)"
        },
        "notes": "Examiner Objective: Proparoxytone nouns (`το δωμάτιο`, `ο δάσκαλος`, `το αυτοκίνητο`) gain a secondary spoken stress on the final syllable when followed by a possessive clitic (`το δωμάτιό μας [to ðoˌmatiˈo mas]`).\nStrategy: Put clear vocal energy on the syllable right before `μου/σου/του/μας/σας/τους` in 3+ syllable proparoxytone words.",
        "keg_communicative_function": "Applying the Greek enclitic stress rule naturally when describing personal possessions",
        "example_el": "Ο δάσκαλός μας στο σχολείο είναι πολύ υπομονετικός και μας εξηγεί πάντα τους κανόνες με απλά παραδείγματα.",
        "example_en": "Our teacher at school is very patient and always explains the rules to us with simple examples.",
        "example2_el": "Τα παράθυρα του διαμερίσματός μου βλέπουν σε ένα ήσυχο πάρκο με πολλά πράσινα δέντρα και λουλούδια.",
        "example2_en": "The windows of my apartment look out onto a quiet park with many green trees and flowers."
    },
    {
        "id": "SP-U06-028",
        "greek": "Κάθε μέρα τρώω φρούτα, αλλά χθες έφαγα ένα γλυκό μετά το φαγητό.",
        "english": "Every day I eat fruit, but yesterday I ate a sweet after the meal. (Suppletive Stem & Stress Drill)",
        "phonetic_hint": "[ˈkaθe ˈmera ˈtroo ˈfruta, aˈla xθes ˈefaɣa ˈena ɣliˈko meˈta to fajiˈto] — Irregular suppletive verb: Present 'τρώω' [ˈtroo] -> Aorist 'έφαγα' [ˈefaɣa] -> Subjunctive 'να φάω' [na ˈfao].",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 2 & 4 (High-Frequency Irregular Verb & Stress)",
            "focus": "Suppletive stems and stress shift: τρώω (Present) -> έφαγα / φάγαμε (Aorist) -> θα φάω (Future)"
        },
        "notes": "Examiner Objective: High-frequency irregular verbs (`τρώω -> έφαγα`, `βλέπω -> είδα`, `πίνω -> ήπια`, `λέω -> είπα`) are tested constantly in Stage 1 and Stage 3.\nStrategy: Drill the triad `τρώω - έφαγα - θα φάω` until automatic.",
        "keg_communicative_function": "Narrating daily diet versus past meals using high-frequency irregular verb stems",
        "example_el": "Σήμερα το μεσημέρι θα φάω μια ελαφριά σαλάτα στο γραφείο, γιατί το βράδυ θα βγούμε για φαγητό με φίλους.",
        "example_en": "Today at noon I will eat a light salad at the office, because in the evening we will go out for food with friends.",
        "example2_el": "Την Κυριακή φάγαμε φρέσκο ψάρι σε μια όμορφη ταβέρνα δίπλα στη θάλασσα και ήπιαμε λευκό κρασί.",
        "example2_en": "On Sunday we ate fresh fish at a lovely taverna by the sea and drank white wine."
    },

    # --- 029–040: Polite Conditional Tone Modulation, Rising Question Intonation & Agreement Traps ---
    {
        "id": "SP-U06-029",
        "greek": "Θα ήθελα να σας ζητήσω μια πληροφορία, αν έχετε λίγο χρόνο.",
        "english": "I would like to ask you for a piece of information, if you have a little time. (Polite Conditional Tone Drill)",
        "phonetic_hint": "[θa ˈiθela na sas ziˈtiso mɲa plirofoˈria, an ˈeçete ˈliɣo ˈxrono] — Softened polite pitch contour on 'Θα ήθελα να σας ζητήσω' + conditional 'αν έχετε'.",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 & Criterion 4 (Polite Register & Tone Modulation)",
            "focus": "Replacing blunt imperatives (Πείτε μου / Δώστε μου) with polite conditional Θα ήθελα να + Aorist subjunctive"
        },
        "notes": "Examiner Objective: In Stage 2 roleplays, blunt imperatives (`Δώστε μου ένα εισιτήριο`) lower scores on Appropriateness and Intonation.\nStrategy: Always open service requests with a warm, mid-high pitch on `Θα ήθελα να...`.",
        "keg_communicative_function": "Initiating a polite service enquiry using conditional mitigation",
        "example_el": "Καλημέρα σας, θα ήθελα να κλείσω ένα δίκλινο δωμάτιο με πρωινό για τρία βράδια τον επόμενο μήνα, παρακαλώ.",
        "example_en": "Good morning, I would like to book a double room with breakfast for three nights next month, please.",
        "example2_el": "Με συγχωρείτε, θα ήθελα να μάθω τι ώρα φεύγει το τελευταίο λεωφορείο για το αεροδρόμιο απόψε.",
        "example2_en": "Excuse me, I would like to find out what time the last bus for the airport leaves tonight."
    },
    {
        "id": "SP-U06-030",
        "greek": "Θα μπορούσατε να μου πείτε τι ώρα ανοίγει το φαρμακείο το απόγευμα;",
        "english": "Could you tell me what time the pharmacy opens in the afternoon? (Polite Conditional Question Drill)",
        "phonetic_hint": "[θa boˈrusate na mu ˈpite ti ˈora aˈniji to farmaˈcio to aˈpojevma↗] — Polite conditional 'Θα μπορούσατε να μου πείτε' + indirect question intonation.",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 & Criterion 4 (Polite Inquiry & Question Intonation)",
            "focus": "Conditional modal Θα μπορούσατε να + indirect question clause (τι ώρα ανοίγει)"
        },
        "notes": "Examiner Objective: Trains polite indirect questions for Stage 2 cue cards (pharmacy, post office, ticket counter).\nStrategy: Stress `μπο-ΡΟΥ-σα-τε` gently and let the voice rise slightly at the end of the request.",
        "keg_communicative_function": "Formulating polite indirect questions about opening hours and services",
        "example_el": "Θα μπορούσατε, σας παρακαλώ, να μου δείξετε αυτό το μπλε πουκάμισο σε λίγο μεγαλύτερο μέγεθος;",
        "example_en": "Could you please show me this blue shirt in a slightly larger size?",
        "example2_el": "Θα μπορούσατε να μου εξηγήσετε πώς πρέπει να παίρνω αυτό το σιρόπι για τον λαιμό κάθε μέρα;",
        "example2_en": "Could you explain to me how I should take this throat syrup every day?"
    },
    {
        "id": "SP-U06-031",
        "greek": "Μήπως υπάρχει διαθέσιμο δωμάτιο με θέα στη θάλασσα για δύο βράδια;",
        "english": "Is there perhaps an available room with a sea view for two nights? (Polite Tentative Intonation Drill)",
        "phonetic_hint": "[ˈmipos iˈparçi ðjaˈθesimo ðoˈmatio me ˈθea sti ˈθalasa ja ˈðio ˈvraðja↗] — Tentative politeness marker 'Μήπως' + rising polar question boundary tone [↗].",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 & Criterion 4 (Polite Tentative Questions & Rising Intonation)",
            "focus": "Polite particle Μήπως + rising terminal pitch contour in yes/no questions"
        },
        "notes": "Examiner Objective: Starting a yes/no question with `Μήπως...;` immediately signals high spoken politeness in Greek.\nStrategy: Keep a gentle rising intonation on the final word (`για δύο βράδια; ↗`).",
        "keg_communicative_function": "Asking polite availability questions in hotel and travel roleplays",
        "example_el": "Μήπως γνωρίζετε αν υπάρχει κάποια έκπτωση στα εισιτήρια του πλοίου για τους φοιτητές και τις οικογένειες;",
        "example_en": "Do you perhaps know if there is any discount on the ferry tickets for students and families?",
        "example2_el": "Με συγχωρείτε, μήπως έχετε λίγο χρόνο να με βοηθήσετε με αυτή την αίτηση εγγραφής;",
        "example2_en": "Excuse me, do you perhaps have a little time to help me with this registration form?"
    },
    {
        "id": "SP-U06-032",
        "greek": "Το εισιτήριο περιλαμβάνει και τις αποσκευές; Ναι, το εισιτήριο περιλαμβάνει και τις αποσκευές.",
        "english": "Does the ticket include luggage too? Yes, the ticket includes luggage too. (Statement vs. Polar Question Intonation Drill)",
        "phonetic_hint": "[to isiˈtirio perilaˈmvani ce tis aposceˈves↗] vs. [ne, to isiˈtirio perilaˈmvani ce tis aposceˈves↘] — Identical syntax distinguished purely by rising [↗] vs. falling [↘] intonation.",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 4 (Sentence Prosody: Polar Question vs. Declarative Statement)",
            "focus": "Distinguishing Greek yes/no questions from statements solely via pitch contour (no auxiliary 'do/does')"
        },
        "notes": "Examiner Objective: Because Greek has no question auxiliary (*do/does*), a flat intonation makes a question sound like a statement.\nStrategy: Raise pitch sharply on the stressed syllable of the final word (`αποσκευ-ΕΣ; ↗`) for the question, and drop pitch (`↘`) for the answer.",
        "keg_communicative_function": "Using rising and falling pitch contours to distinguish polar questions from statements",
        "example_el": "Στην τιμή του δωματίου περιλαμβάνεται και το πρωινό; Ναι, φυσικά, το πρωινό σερβίρεται από τις επτά έως τις δέκα.",
        "example_en": "Is breakfast also included in the price of the room? Yes, of course, breakfast is served from seven to ten.",
        "example2_el": "Μπορώ να αλλάξω αυτό το παντελόνι αν δεν μου κάνει; Βεβαίως, αρκεί να έχετε μαζί σας την απόδειξη αγοράς.",
        "example2_en": "Can I exchange these trousers if they don't fit me? Certainly, provided you have the purchase receipt with you."
    },
    {
        "id": "SP-U06-033",
        "greek": "Σας πειράζει αν ανοίξω λίγο το παράθυρο επειδή κάνει ζέστη στην αίθουσα;",
        "english": "Do you mind if I open the window a little because it is hot in the room? (Polite Permission & Tone Drill)",
        "phonetic_hint": "[sas piˈrazi an aˈnikso ˈliɣo to paˈraθiro epiˈði ˈkani ˈzesti stin ˈeθusa↗] — Polite permission formula 'Σας πειράζει αν + Aorist subjunctive' with rising question tone.",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 & Criterion 5 (Interactive Politeness & Permission)",
            "focus": "Polite permission request Σας πειράζει αν / Μπορώ να + Aorist subjunctive"
        },
        "notes": "Examiner Objective: Tests polite negotiation with a partner or interlocutor in Stage 2.\nStrategy: Pair `Σας πειράζει αν...;` with a courteous reason (`επειδή...`).",
        "keg_communicative_function": "Asking polite permission and negotiating comfort or schedule adjustments",
        "example_el": "Σας πειράζει αν αλλάξουμε την ώρα του ραντεβού μας από τις πέντε στις έξι το απόγευμα, γιατί έχω μια υποχρέωση;",
        "example_en": "Do you mind if we change the time of our appointment from five to six in the afternoon, because I have an obligation?",
        "example2_el": "Μήπως σας πειράζει να καθίσουμε στο τραπέζι έξω στον κήπο, όπου έχει περισσότερη δροσιά και ησυχία;",
        "example2_en": "Do you perhaps mind if we sit at the table outside in the garden, where it is cooler and quieter?"
    },
    {
        "id": "SP-U06-034",
        "greek": "Φοβάμαι πως δεν θα μπορέσω να έρθω το Σάββατο, αλλά μήπως βολεύει την Κυριακή;",
        "english": "I'm afraid I won't be able to come on Saturday, but does Sunday perhaps suit you? (Polite Refusal & Counter-Proposal Drill)",
        "phonetic_hint": "[foˈvame pos ðen θa boˈreso na ˈerθo to ˈsavato↘, aˈla ˈmipos voˈlevi tiŋ ɟirjaˈci↗] — Falling apologetic tone on refusal followed by rising cooperative tone on counter-proposal.",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 2 & Criterion 5 (Polite Disagreement & Counter-Proposal)",
            "focus": "Diplomatic softener Φοβάμαι πως / Δυστυχώς + counter-proposal μήπως βολεύει / προτιμάτε"
        },
        "notes": "Examiner Objective: Stage 2 cue cards always require candidates to decline one inconvenient time/option and propose an alternative.\nStrategy: Never just say `Όχι, δεν μπορώ`. Use `Φοβάμαι πως...` + `μήπως βολεύει...;`.",
        "keg_communicative_function": "Declining a suggestion politely and proposing a practical alternative",
        "example_el": "Δυστυχώς την Παρασκευή το βράδυ δουλεύω μέχρι αργά, αλλά αν θέλεις μπορούμε να βγούμε για φαγητό το Σάββατο το μεσημέρι.",
        "example_en": "Unfortunately on Friday evening I work until late, but if you want we can go out for food on Saturday at noon.",
        "example2_el": "Η ιδέα σου για το θέατρο είναι πολύ ωραία, όμως τα εισιτήρια είναι λίγο ακριβά· μήπως προτιμάς να πάμε σινεμά;",
        "example2_en": "Your idea for the theater is very nice, however the tickets are a bit expensive; do you perhaps prefer to go to the cinema?"
    },
    {
        "id": "SP-U06-035",
        "greek": "Σήμερα έχει πολύ κόσμο στον δρόμο, έχω πολλή δουλειά, αλλά κάνει πολύ ωραίο καιρό.",
        "english": "Today there are many people on the street, I have a lot of work, but the weather is very nice. (Morphological Trap Drill: πολύς / πολλή / πολύ)",
        "phonetic_hint": "[ˈsimera ˈeçi poˈli ˈkozmo ston ˈðromo, ˈexo poˈli ðuˈlja, aˈla ˈkani poˈli oˈreo ceˈro] — Homophonous [poˈli] in Accusative/Adverb vs. Nominative masculine 'πολύς κόσμος' [poˈlis ˈkozmos].",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 2 (Morphological Trap: πολύς / πολλή / πολύ)",
            "focus": "Distinguishing Nominative masculine πολύς (πολύς κόσμος) from Accusative/Feminine/Neuter/Adverb [poˈli] and plural πολλοί/πολλές/πολλά"
        },
        "notes": "Examiner Objective: Candidates often say `*πολύ κόσμος` (dropping `-ς` in Nominative) or `*πολλοί δουλειά`.\nStrategy: In Nominative masculine subject position use `πολύς κόσμος` (`Υπάρχει πολύς κόσμος`), in Accusative object position use `πολύ κόσμο` (`Βλέπω πολύ κόσμο`).",
        "keg_communicative_function": "Using the quantifier πολύς/πολλή/πολύ accurately across gender, number, and case",
        "example_el": "Στην κεντρική πλατεία της πόλης υπάρχει πάντα πολύς κόσμος, πολλά μαγαζιά και πολλές όμορφες καφετέριες.",
        "example_en": "In the central square of the city there are always many people, many shops, and many lovely cafés.",
        "example2_el": "Αυτό το καλοκαίρι γνώρισα πολλούς καλούς φίλους στο νησί και περάσαμε πολύ ωραία στις διακοπές μας.",
        "example2_en": "This summer I met many good friends on the island and we had a very nice time on our holidays."
    },
    {
        "id": "SP-U06-036",
        "greek": "Πήγα στον γιατρό το πρωί και έδωσα τις εξετάσεις μου στη γραμματεία της γιατρού.",
        "english": "I went to the doctor in the morning and gave my test results to the (female) doctor's reception. (Morphological Trap Drill)",
        "phonetic_hint": "[ˈpiɣa ston jaˈtro to proˈi ce ˈeðosa tis ekseˈtasis mu sti ɣramaˈtia tis jaˈtru] — Epicene masculine/feminine nouns in -ός: 'ο/η γιατρός' -> Acc. 'τον/την γιατρό', Gen. 'του/της γιατρού'.",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 2 (Morphological Trap: Feminine Nouns in -ος & Accusative/Genitive Articles)",
            "focus": "Common-gender professions (ο/η γιατρός, ο/η δικηγόρος, ο/η υπάλληλος) and feminine nouns in -ος (η οδός, η είσοδος, η έξοδος)"
        },
        "notes": "Examiner Objective: Feminine nouns ending in `-ος` (`η είσοδος`, `η οδός`, `η γιατρός`) trap learners into using masculine articles (`*τον είσοδο`).\nStrategy: Always match the feminine article: `στην κεντρική είσοδο`, `στην οδό Ερμού`, `μίλησα με την ευγενική υπάλληλο`.",
        "keg_communicative_function": "Maintaining accurate article-noun gender agreement with feminine nouns in -ος",
        "example_el": "Το φαρμακείο βρίσκεται στην κεντρική οδό της γειτονιάς μας, ακριβώς απέναντι από την είσοδο του σταθμού του μετρό.",
        "example_en": "The pharmacy is located on the main street of our neighborhood, right across from the entrance of the metro station.",
        "example2_el": "Ρώτησα την ευγενική υπάλληλο στο γκισέ τι ώρα αναχωρεί το επόμενο πλοίο για το νησί της Ρόδου.",
        "example2_en": "I asked the polite female clerk at the counter what time the next ship departs for the island of Rhodes."
    },
    {
        "id": "SP-U06-037",
        "greek": "Στην εικόνα βλέπω τρεις άντρες, τέσσερις γυναίκες και τρία μικρά παιδιά.",
        "english": "In the picture I see three men, four women, and three small children. (Morphological Trap Drill: Numerals 3 & 4)",
        "phonetic_hint": "[stin iˈkona ˈvlepo tris ˈandres, ˈteseris jiˈneces ce ˈtria miˈkra peˈðja] — Gender agreement on numerals: Masc./Fem. 'τρεις / τέσσερις' [tris / ˈteseris] vs. Neuter 'τρία / τέσσερα'.",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 & Criterion 2 (Morphological Trap: Declension of Numerals 3 and 4)",
            "focus": "Masculine/Feminine τρεις & τέσσερις (τρεις μέρες, τέσσερις φίλοι) vs. Neuter τρία & τέσσερα (τρία χρόνια, τέσσερα παιδιά)"
        },
        "notes": "Examiner Objective: In Stage 3 picture descriptions, saying `*τρία γυναίκες` or `*τρεις παιδιά` is a glaring grammatical error.\nStrategy: Use `τρεις / τέσσερις` for masculine and feminine (`τρεις ώρες`, `τέσσερις εβδομάδες`) and `τρία / τέσσερα` only for neuter (`τρία άτομα`, `τέσσερα δωμάτια`).",
        "keg_communicative_function": "Counting people, objects, and time durations accurately in Stage 3 descriptions",
        "example_el": "Μένω στην Ελλάδα εδώ και τρία χρόνια και κάνω μάθημα ελληνικών τέσσερις ώρες κάθε εβδομάδα με την τάξη μου.",
        "example_en": "I have been living in Greece for three years now and I take Greek lessons four hours every week with my class.",
        "example2_el": "Θα ήθελα να αγοράσω τρεις μπλούζες, τέσσερις καφέδες και τρία μπουκάλια νερό για την εκδρομή μας.",
        "example2_en": "I would like to buy three shirts, four coffees, and three bottles of water for our excursion."
    },
    {
        "id": "SP-U06-038",
        "greek": "Τα καλοκαίρια της αρέσει να ταξιδεύει με την οικογένειά της στα ελληνικά νησιά.",
        "english": "In the summers she likes travelling with her family to the Greek islands. (Morphological Trap Drill: αρέσει Construction)",
        "phonetic_hint": "[ta kaloˈcerja tis aˈresi na taksiˈðevi me tin ikoˈjeɲa tis sta eliniˈka niˈsça] — Genitive weak pronoun 'μου / σου / του / της / μας / σας / τους' + 'αρέσει / αρέσουν'.",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 2 (Morphological & Syntactic Trap: Μου αρέσει / Μου αρέσουν)",
            "focus": "Genitive experiencer pronoun (μου/του/της/μας/τους) + singular αρέσει (with singular noun or να-clause) vs. plural αρέσουν (with plural noun)"
        },
        "notes": "Examiner Objective: Two classic exam errors are using `*με αρέσει` instead of `μου αρέσει`, or failing to pluralize `μου αρέσουν τα ταξίδια`.\nStrategy: Use singular `μου αρέσει το καλοκαίρι / μου αρέσει να κολυμπάω`, and plural `μου αρέσουν οι ελληνικές παραλίες`.",
        "keg_communicative_function": "Expressing likes and preferences with accurate Genitive pronouns and verb number agreement",
        "example_el": "Στους γονείς μου αρέσουν πολύ τα παραδοσιακά χωριά, ενώ στον αδερφό μου αρέσει να μένει κοντά στη θάλασσα.",
        "example_en": "My parents really like traditional villages, whereas my brother likes staying near the sea.",
        "example2_el": "Μας αρέσουν πάρα πολύ οι ελληνικοί χοροί και η μουσική, γι' αυτό πηγαίνουμε συχνά σε γιορτές με την παρέα μας.",
        "example2_en": "We really like Greek dances and music, which is why we often go to celebrations with our group of friends."
    },
    {
        "id": "SP-U06-039",
        "greek": "Έδωσα του φίλου μου το βιβλίο και μου είπε ότι θα μου το επιστρέψει την Τρίτη.",
        "english": "I gave my friend the book and he told me that he will return it to me on Tuesday. (Morphological Trap Drill: Clitic Pronoun Order)",
        "phonetic_hint": "[ˈeðosa tu ˈfilu mu to viˈvlio ce mu ˈipe ˈoti θa mu to epiˈstrepsi tin ˈtriti] — Double clitic pronoun order before the verb: Indirect (Genitive 'μου') + Direct (Accusative 'το') + Verb.",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Criterion 2 & 4 (Clitic Pronoun Phonology & Word Order)",
            "focus": "Proclitic weak pronoun cluster (θα μου το δώσει, μου το είπε) as a single phonological word with main verb"
        },
        "notes": "Examiner Objective: Weak object pronouns (`μου το έδωσε`, `θα σας το στείλω`) must precede indicative/subjunctive verbs without pause.\nStrategy: Pronounce `θα μου το επιστρέψει` smoothly as one prosodic unit `[θamutoepiˈstrepsi]`.",
        "keg_communicative_function": "Using weak indirect and direct object pronouns fluently in spoken exchanges",
        "example_el": "Αν χρειάζεσαι το λεξικό για το μάθημα, μπορώ να σου το δώσω σήμερα και να μου το φέρεις την επόμενη εβδομάδα.",
        "example_en": "If you need the dictionary for the lesson, I can give it to you today and you can bring it back to me next week.",
        "example2_el": "Ζήτησα από τον υπάλληλο το πρόγραμμα των δρομολογίων και μου το έστειλε αμέσως στο ηλεκτρονικό μου ταχυδρομείο.",
        "example2_en": "I asked the clerk for the timetable of routes and he sent it to me immediately at my email address."
    },
    {
        "id": "SP-U06-040",
        "greek": "Σας ευχαριστώ θερμά για τη συζήτηση, χάρηκα πολύ που τα είπαμε και σας εύχομαι καλή συνέχεια!",
        "english": "Thank you warmly for the conversation, I was very glad we spoke, and I wish you all the best! (Exam Closing Prosody Drill)",
        "phonetic_hint": "[sas efxariˈsto θerˈma ja ti siˈzitisi, ˈxarika poˈli pu ta ˈipame ce sas ˈefxome kaˈli siˈneçia] — Warm, confident closing cadence combining [efx] ('ευχαριστώ', 'εύχομαι') and palatal [ç] ('συνέχεια').",
        "gender_or_pos": "speaking-drill",
        "status": "verified",
        "grammatical_info": {
            "stage": "Stage 3 Closing & Criterion 4/5 (Polite Farewell & Prosodic Confidence)",
            "focus": "Formal/polite closing formulas (Σας ευχαριστώ θερμά, χάρηκα πολύ, καλή συνέχεια)"
        },
        "notes": "Examiner Objective: Leaving a warm, natural, phonologically crisp final impression at the end of the 12-minute KEG A2 speaking exam.\nStrategy: Deliver with a smile, clear articulation of `ευχαριστώ / εύχομαι [efx-]`, and natural falling-warm intonation.",
        "keg_communicative_function": "Concluding the oral examination politely with natural farewell formulas",
        "example_el": "Ήταν μεγάλη μου χαρά που συζητήσαμε σήμερα μαζί· σας ευχαριστώ πολύ για τον χρόνο σας και εύχομαι να έχετε μια όμορφη μέρα.",
        "example_en": "It was my great pleasure that we talked together today; thank you very much for your time and I wish you a lovely day.",
        "example2_el": "Σας ευχαριστώ πολύ για την ευχάριστη συζήτηση, χάρηκα για τη γνωριμία και ελπίζω να τα ξαναπούμε σύντομα.",
        "example2_en": "Thank you very much for the pleasant conversation, I was glad to meet you, and I hope we speak again soon."
    },
]


def normalize_nfc(text: str) -> str:
    return unicodedata.normalize("NFC", text)


def synthesize_item(text: str, filename: str) -> bool:
    """Synthesize a single Greek string via Google Cloud Chirp-3 HD if not already cached."""
    import time
    p = AUDIO_DIR / filename
    if p.exists() and p.stat().st_size > 0:
        return False
    for attempt in range(5):
        try:
            audio_bytes = synthesize_greek_chirp(text)
            with open(p, "wb") as f_out:
                f_out.write(audio_bytes)
            return True
        except Exception as e:
            if "429" in str(e) and attempt < 4:
                time.sleep(3 * (attempt + 1))
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
    AUDIO_DIR.mkdir(parents=True, exist_ok=True)
    unit_dir = CONTENT_DIR / unit_id
    unit_dir.mkdir(parents=True, exist_ok=True)
    yaml_file = unit_dir / f"{lesson_id}.yaml"

    tasks = []
    for c in cards:
        c["greek"] = normalize_nfc(c["greek"])
        c["example_el"] = normalize_nfc(c["example_el"])
        c["example2_el"] = normalize_nfc(c["example2_el"])
        c["status"] = "verified"

        fn_greek = generate_audio_filename(c["greek"])
        c["audio"] = fn_greek
        tasks.append((c["greek"], fn_greek))

        fn_ex1 = generate_audio_filename(c["example_el"])
        c["example_audio"] = fn_ex1
        tasks.append((c["example_el"], fn_ex1))

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
        "title": title,
        "description": description,
        "lesson_status": "not_started",
        "lesson_notes": lesson_notes,
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
    print("==================================================================")
    print("Generating KEG-A2 Speaking Curriculum: Batch 3 (Units SP-05 & SP-06)")
    print("==================================================================")

    sp05_notes = """Unit SP-05 Core Notes: Ερωτήσεις Επέκτασης & Προσωπική Εμπειρία (Stage 3 Examiner Extension Questions)
• Official KEG A2 Exam Alignment:
  - Stage 3 Follow-Up Phase: After the candidate describes the visual prompt, the examiner asks 3–4 personal extension questions bridging the topic of the photograph to the candidate's own habits, experiences, and opinions.
  - Multi-Tense Control: Candidates must smoothly transition between habitual Present (Ενεστώτας), specific past experiences in Aorist (Αόριστος), childhood/past habits in Imperfect (Παρατατικός), and future plans/aspirations (Συνοπτικός & Εξακολουθητικός Μέλλοντας).
  - Thematic Coverage: Holidays & Travel (001–008), Shopping & Consumer Habits (009–016), Gastronomy & Celebrations (017–024), Health, Urban vs. Rural Life & Environment (025–032), and Past vs. Present vs. Future & Technology (033–040)."""

    process_unit(
        unit_id="unit-sp-05",
        lesson_id="lesson-01",
        title="Προφορικά SP-05: Ερωτήσεις Επέκτασης & Προσωπική Εμπειρία (Stage 3 Examiner Extension Questions)",
        description="40 examiner follow-up prompts bridging the Stage 3 visual stimulus to the candidate’s personal life, multi-tense storytelling (comparing past habits in Imperfect/Aorist with Present routines and Future plans), and lifestyle preferences.",
        lesson_notes=sp05_notes,
        cards=CARDS_SP_05,
        order_code="SP-05-A",
    )

    sp06_notes = """Unit SP-06 Core Notes: Προφορά, Επιτονισμός & Παγίδες Προφορικού Λόγου (Spoken Phonology & Trap Drills)
• Official KEG A2 Exam Alignment:
  - Criterion 4 (Προφορά & Επιτονισμός) & Criterion 2 (Γραμματική & Συντακτική Ορθότητα):
  - Nasal Stops & Connected Speech Sandhi (001–010): Voiced vs. unvoiced stops (μπ/π, ντ/τ, γκ/γ/κ, τζ/τσ) and cross-word nasal assimilation (δεν μπορώ, την Κυριακή).
  - Diphthongs & Fricatives (011–018): Assimilation of αυ ([av]/[af]) and ευ ([ev]/[ef]), plus dental (θ/δ) and velar/palatal (χ/γ) fricative contrasts.
  - Stress-Placement & Aspect Traps (019–028): Antepenultimate Aorist stress retraction (μένω/έμεινα, δουλεύω/δούλεψα, γυρίζω/γύρισα, πληρώνω/πλήρωσα), lexical minimal pairs (παίρνω/πήρα vs. περνάω/πέρασα), and enclitic stress (ο δάσκαλός μας).
  - Polite Conditional Tone & Morphological Traps (029–040): Replacing imperatives with Θα ήθελα / Θα μπορούσατε / Μήπως, rising polar question intonation, πολύς/πολλή/πολύ, feminine nouns in -ος, and τρεις/τρία."""

    process_unit(
        unit_id="unit-sp-06",
        lesson_id="lesson-01",
        title="Προφορικά SP-06: Προφορά, Επιτονισμός & Παγίδες Προφορικού Λόγου (Spoken Phonology & Trap Drills)",
        description="40 orthoepic and morphological trap drills targeting Criterion 4 (Pronunciation & Intonation) and Criterion 2 (Accuracy): nasal stops (μπ/π, ντ/τ, γκ/κ), diphthongs (αυ/ευ), stress shifts across tenses, and polite conditional tone modulation.",
        lesson_notes=sp06_notes,
        cards=CARDS_SP_06,
        order_code="SP-06-A",
    )

    print("\n[OK] KEG-A2 Speaking Batch 3 (unit-sp-05 & unit-sp-06) finished successfully!")


if __name__ == "__main__":
    main()

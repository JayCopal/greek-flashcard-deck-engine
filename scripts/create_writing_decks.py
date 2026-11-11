import os
import sys
import yaml
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from server.tts_service import synthesize_greek_chirp, generate_audio_filename

AUDIO_DIR = BASE_DIR / "audio"
CONTENT_DIR = BASE_DIR / "content"

def ensure_audio(text):
    if not text:
        return None
    fn = generate_audio_filename(text)
    fp = AUDIO_DIR / fn
    if not fp.exists():
        try:
            raw = synthesize_greek_chirp(text)
            if raw:
                with open(fp, "wb") as f:
                    f.write(raw)
                print(f"  [TTS] Synthesized {fn} for: {text[:35]}...")
        except Exception as e:
            print(f"  [TTS Error] {e} for: {text[:35]}")
    return fn

def process_cards(cards):
    for c in cards:
        c['audio'] = ensure_audio(c['greek'])
        c['status'] = 'verified' if (AUDIO_DIR / c['audio']).exists() else 'pending_tts'
        if c.get('example_el'):
            c['example_audio'] = ensure_audio(c['example_el'])
        if c.get('example2_el'):
            c['example2_audio'] = ensure_audio(c['example2_el'])
    return cards

def save_unit(uid, title, description, notes, cards):
    target_dir = CONTENT_DIR / uid
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / "lesson-01.yaml"
    
    processed = process_cards(cards)
    data = {
        "unit_id": uid,
        "lesson_id": "lesson-01",
        "title": title,
        "description": description,
        "lesson_status": "not_started",
        "lesson_notes": notes,
        "entries": processed
    }
    with open(target_file, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"[Saved] {uid} with {len(processed)} cards.")

# --------------------------------------------------------------------
# UNIT WR1-01: Prompt Decoders & Examiner Directives
# --------------------------------------------------------------------
CARDS_WR1_01 = [
    {
        "id": "WR1-U01-001",
        "greek": "περιγράψτε",
        "english": "describe (examiner directive)",
        "notes": "Imperative of περιγράφω. Directs candidate to use descriptive adjectives, location markers, and sensory details.",
        "gender_or_pos": "verb (imperative)",
        "example_el": "Περιγράψτε το νέο σας διαμέρισμα και τη γειτονιά όπου μένετε.",
        "example_en": "Describe your new apartment and the neighborhood where you live.",
        "example2_el": "Περιγράψτε ένα ταξίδι που κάνατε το περασμένο καλοκαίρι.",
        "example2_en": "Describe a trip that you took last summer."
    },
    {
        "id": "WR1-U01-002",
        "greek": "εξηγήστε γιατί",
        "english": "explain why (causal directive)",
        "notes": "Imperative of εξηγώ. Triggers causal connectors: γιατί, επειδή, γι' αυτό.",
        "example_el": "Εξηγήστε γιατί δεν μπορείτε να έρθετε στη σημερινή συνάντηση.",
        "example_en": "Explain why you cannot come to today's meeting.",
        "example2_el": "Εξηγήστε γιατί σας αρέσει τόσο πολύ αυτή η πόλη.",
        "example2_en": "Explain why you like this city so much."
    },
    {
        "id": "WR1-U01-003",
        "greek": "προτείνετε",
        "english": "suggest / recommend",
        "notes": "Imperative of προτείνω. Triggers modal expressions: σου προτείνω να, μπορούμε να.",
        "example_el": "Προτείνετε μια παραδοσιακή ταβέρνα για το δείπνο του Σαββάτου.",
        "example_en": "Suggest a traditional taverna for Saturday dinner.",
        "example2_el": "Προτείνετε ένα καλό μέρος για διακοπές στον φίλο σας.",
        "example2_en": "Recommend a good vacation spot to your friend."
    },
    {
        "id": "WR1-U01-004",
        "greek": "ζητήστε πληροφορίες",
        "english": "ask for information / inquire",
        "notes": "Imperative of ζητώ. Directs candidate to write polite inquiry questions (πού, πότε, πόσο, υπάρχει).",
        "example_el": "Ζητήστε πληροφορίες για τις τιμές και τα δρομολόγια των πλοίων.",
        "example_en": "Ask for information about ferry ticket prices and schedules.",
        "example2_el": "Ζητήστε πληροφορίες για τα δωμάτια του ξενοδοχείου.",
        "example2_en": "Ask for information about the hotel rooms."
    },
    {
        "id": "WR1-U01-005",
        "greek": "ενημερώστε",
        "english": "inform / notify",
        "notes": "Imperative of ενημερώνω. Directs candidate to state factual circumstances or updates clearly.",
        "example_el": "Ενημερώστε τον συνάδελφό σας για τη νέα ώρα της συνεδρίασης.",
        "example_en": "Inform your colleague about the new meeting time.",
        "example2_el": "Ενημερώστε τον δάσκαλο ότι θα απουσιάσετε από το μάθημα.",
        "example2_en": "Inform the teacher that you will be absent from class."
    },
    {
        "id": "WR1-U01-006",
        "greek": "προσκαλέστε",
        "english": "invite",
        "notes": "Imperative of προσκαλώ. Essential for Task 1: state occasion, date, time, and address.",
        "example_el": "Προσκαλέστε τους φίλους σας στα γενέθλιά σας αυτό το Σάββατο.",
        "example_en": "Invite your friends to your birthday party this Saturday.",
        "example2_el": "Προσκαλέστε τους γείτονες στα εγκαίνια του νέου σας σπιτιού.",
        "example2_en": "Invite the neighbors to your housewarming party."
    },
    {
        "id": "WR1-U01-007",
        "greek": "δικαιολογήστε",
        "english": "justify / provide reasons",
        "notes": "Imperative of δικαιολογώ. Required when declining invitations or defending personal preferences.",
        "example_el": "Δικαιολογήστε την άρνησή σας να παρευρεθείτε στην εκδήλωση.",
        "example_en": "Justify your refusal to attend the event.",
        "example2_el": "Δικαιολογήστε γιατί προτιμάτε να ταξιδέψετε με τρένο.",
        "example2_en": "Justify why you prefer to travel by train."
    },
    {
        "id": "WR1-U01-008",
        "greek": "ευχαριστήστε",
        "english": "thank / express gratitude",
        "notes": "Imperative of ευχαριστώ. Essential in social notes and polite follow-up messages.",
        "example_el": "Ευχαριστήστε τον οικοδεσπότη για την υπέροχη φιλοξενία στο νησί.",
        "example_en": "Thank the host for the wonderful hospitality on the island.",
        "example2_el": "Ευχαριστήστε τη φίλη σας για το όμορφο δώρο που σας έκανε.",
        "example2_en": "Thank your friend for the lovely gift she gave you."
    },
    {
        "id": "WR1-U01-009",
        "greek": "επιβεβαιώστε",
        "english": "confirm",
        "notes": "Imperative of επιβεβαιώνω. Common in booking and appointment confirmations.",
        "example_el": "Επιβεβαιώστε την κράτηση του δωματίου μέχρι αύριο το μεσημέρι.",
        "example_en": "Confirm the room reservation by tomorrow noon.",
        "example2_el": "Επιβεβαιώστε την παρουσία σας στο πάρτι γενεθλίων.",
        "example2_en": "Confirm your attendance at the birthday party."
    },
    {
        "id": "WR1-U01-010",
        "greek": "συγκρίνετε",
        "english": "compare",
        "notes": "Imperative of συγκρίνω. Directs candidate to use comparative forms (πιο, καλύτερος, φθηνότερος).",
        "example_el": "Συγκρίνετε τις δύο πόλεις και πείτε ποια σας αρέσει πιο πολύ.",
        "example_en": "Compare the two cities and say which one you like more.",
        "example2_el": "Συγκρίνετε το παλιό με το καινούργιο σας σπίτι.",
        "example2_en": "Compare your old and your new house."
    }
]

# --------------------------------------------------------------------
# UNIT WR1-02: Formulaic Openers, Transitions & Closers
# --------------------------------------------------------------------
CARDS_WR1_02 = [
    {
        "id": "WR1-U02-001",
        "greek": "Αγαπητέ μου...",
        "english": "Dear (masculine singular)...",
        "notes": "Formal/informal letter opener for a male recipient. E.g. Αγαπητέ μου Γιώργο,",
        "gender_or_pos": "phrase (salutation)",
        "example_el": "Αγαπητέ μου Νίκο, σου γράφω για να σου πω τα ευχάριστα νέα μου.",
        "example_en": "Dear Nikos, I am writing to tell you my pleasant news.",
        "example2_el": "Αγαπητέ μου φίλε, ελπίζω να είσαι καλά εσύ και η οικογένειά σου.",
        "example2_en": "My dear friend, I hope you and your family are well."
    },
    {
        "id": "WR1-U02-002",
        "greek": "Αγαπητή μου...",
        "english": "Dear (feminine singular)...",
        "notes": "Formal/informal letter opener for a female recipient. E.g. Αγαπητή μου Μαρία,",
        "gender_or_pos": "phrase (salutation)",
        "example_el": "Αγαπητή μου Ελένη, πώς είσαι; Χάθηκα αυτές τις μέρες.",
        "example_en": "Dear Eleni, how are you? I've been lost these days.",
        "example2_el": "Αγαπητή μου γιαγιά, σου στέλνω αυτή την κάρτα από τη Ρόδο.",
        "example2_en": "My dear grandmother, I am sending you this postcard from Rhodes."
    },
    {
        "id": "WR1-U02-003",
        "greek": "Γεια σου! Πώς είσαι;",
        "english": "Hello! How are you?",
        "notes": "Standard friendly informal email and note opener.",
        "gender_or_pos": "phrase (greeting)",
        "example_el": "Γεια σου Κώστα! Πώς είσαι; Ελπίζω όλα να πηγαίνουν περίφημα.",
        "example_en": "Hello Kostas! How are you? I hope everything is going wonderfully.",
        "example2_el": "Γεια σου Άννα! Πώς είσαι; Σου γράφω από το νέο μου γραφείο.",
        "example2_en": "Hello Anna! How are you? I am writing to you from my new office."
    },
    {
        "id": "WR1-U02-004",
        "greek": "Συγγνώμη που άργησα να σου γράψω",
        "english": "Sorry for being late in writing to you",
        "notes": "Standard apology transitional chunk. Fulfills politeness conventions.",
        "gender_or_pos": "phrase",
        "example_el": "Συγγνώμη που άργησα να σου γράψω, αλλά είχα πάρα πολλή δουλειά.",
        "example_en": "Sorry for the delay in writing to you, but I had too much work.",
        "example2_el": "Συγγνώμη που άργησα να σου απαντήσω, έλειπα σε ταξίδι.",
        "example2_en": "Sorry for being late in answering you; I was away on a trip."
    },
    {
        "id": "WR1-U02-005",
        "greek": "Σου γράφω για να σου πω τα νέα μου",
        "english": "I am writing to tell you my news",
        "notes": "Standard communicative intent formula opening Task 2 letters.",
        "gender_or_pos": "phrase",
        "example_el": "Σου γράφω για να σου πω τα νέα μου από τη νέα μου δουλειά.",
        "example_en": "I am writing to tell you my news from my new job.",
        "example2_el": "Σου γράφω για να σου πω ότι τελικά μετακομίζω στην Αθήνα.",
        "example2_en": "I am writing to tell you that I am finally moving to Athens."
    },
    {
        "id": "WR1-U02-006",
        "greek": "Ελπίζω να τα πούμε σύντομα",
        "english": "I hope we talk / see each other soon",
        "notes": "Pre-closing formula expressing future contact.",
        "gender_or_pos": "phrase",
        "example_el": "Αυτά είναι τα νέα μου. Ελπίζω να τα πούμε σύντομα από κοντά!",
        "example_en": "That is my news. I hope we see each other soon in person!",
        "example2_el": "Ελπίζω να τα πούμε σύντομα και να κανονίσουμε να βγούμε.",
        "example2_en": "I hope we talk soon and arrange to go out."
    },
    {
        "id": "WR1-U02-007",
        "greek": "Περιμένω νέα σου",
        "english": "I await your news / looking forward to hearing from you",
        "notes": "Closing prompt expecting recipient reply.",
        "gender_or_pos": "phrase",
        "example_el": "Γράψε μου όταν μπορέσεις, περιμένω νέα σου με ανυπομονησία.",
        "example_en": "Write to me when you can; I look forward to your news with anticipation.",
        "example2_el": "Περιμένω νέα σου σχετικά με το πρόγραμμα των διακοπών.",
        "example2_en": "I await your news regarding the holiday schedule."
    },
    {
        "id": "WR1-U02-008",
        "greek": "Πάρε με τηλέφωνο όταν μπορέσεις",
        "english": "Call me when you can",
        "notes": "Action directive closing in Task 1 notes.",
        "gender_or_pos": "phrase",
        "example_el": "Πάρε με τηλέφωνο όταν μπορέσεις για να κλείσουμε τα εισιτήρια.",
        "example_en": "Call me when you can so we can book the tickets.",
        "example2_el": "Αν έχεις κάποια απορία, πάρε με τηλέφωνο όταν μπορέσεις.",
        "example2_en": "If you have any question, call me when you can."
    },
    {
        "id": "WR1-U02-009",
        "greek": "Σε φιλώ",
        "english": "Kisses (warm informal letter closer)",
        "notes": "Most frequent closer in KEG A2 informal writing.",
        "gender_or_pos": "phrase (valediction)",
        "example_el": "Χαιρέτησε όλους από μένα. Σε φιλώ, Δημήτρης.",
        "example_en": "Say hi to everyone from me. Kisses, Dimitris.",
        "example2_el": "Ανυπομονώ να σε δω το Σάββατο. Σε φιλώ πολύ, Σοφία.",
        "example2_en": "I look forward to seeing you Saturday. Many kisses, Sofia."
    },
    {
        "id": "WR1-U02-010",
        "greek": "Με πολλή αγάπη",
        "english": "With much love",
        "notes": "Affectionate closer for close family and friends. Spells: πολλή (feminine with double lambda and eta).",
        "gender_or_pos": "phrase (valediction)",
        "example_el": "Σου εύχομαι κάθε καλό και καλή επιτυχία. Με πολλή αγάπη, Μαρία.",
        "example_en": "I wish you all the best and great success. With much love, Maria.",
        "example2_el": "Να προσέχεις τον εαυτό σου. Με πολλή αγάπη, η μητέρα σου.",
        "example2_en": "Take care of yourself. With much love, your mother."
    }
]

# --------------------------------------------------------------------
# UNIT WR1-03: Discourse Connectors & Syntactic Linkers
# --------------------------------------------------------------------
CARDS_WR1_03 = [
    {
        "id": "WR1-U03-001",
        "greek": "επίσης",
        "english": "also / additionally",
        "notes": "Adverb of addition. Adds secondary facts without repeating 'και'.",
        "gender_or_pos": "adverb",
        "example_el": "Το σπίτι είναι μεγάλο και επίσης είναι πολύ κοντά στη δουλειά μου.",
        "example_en": "The house is big and also very close to my work.",
        "example2_el": "Επίσης, μην ξεχάσεις να φέρεις τη φωτογραφική σου μηχανή.",
        "example2_en": "Additionally, don't forget to bring your camera."
    },
    {
        "id": "WR1-U03-002",
        "greek": "πρώτα... μετά... στο τέλος",
        "english": "first... then... in the end",
        "notes": "Temporal narrative chain. Indispensable for chronological flow in Task 2.",
        "gender_or_pos": "phrase (temporal sequence)",
        "example_el": "Πρώτα κάναμε μπάνιο στη θάλασσα, μετά φάγαμε και στο τέλος ήπιαμε καφέ.",
        "example_en": "First we swam in the sea, then we ate, and in the end we drank coffee.",
        "example2_el": "Πρώτα πήγαμε στο μουσείο, μετά κάναμε βόλτα και στο τέλος γυρίσαμε στο ξενοδοχείο.",
        "example2_en": "First we went to the museum, then we strolled, and in the end we returned to the hotel."
    },
    {
        "id": "WR1-U03-003",
        "greek": "όμως",
        "english": "however / nevertheless",
        "notes": "Adversative connector. Introduces a contrast or unexpected obstacle.",
        "gender_or_pos": "conjunction",
        "example_el": "Το ξενοδοχείο ήταν παλιό, όμως το δωμάτιο ήταν πεντακάθαρο.",
        "example_en": "The hotel was old; however, the room was spotless.",
        "example2_el": "Ήθελα να έρθω στο πάρτι, όμως είχα πάρα πολλή δουλειά.",
        "example2_en": "I wanted to come to the party; however, I had too much work."
    },
    {
        "id": "WR1-U03-004",
        "greek": "αν και",
        "english": "although / even though",
        "notes": "Concessive conjunction introducing dependent clauses of concession.",
        "gender_or_pos": "conjunction",
        "example_el": "Αν και ο καιρός ήταν βροχερός, περάσαμε υπέροχα στην εκδρομή.",
        "example_en": "Even though the weather was rainy, we had a wonderful time on the trip.",
        "example2_el": "Αν και ήμουν κουρασμένος, πήγα στη γιορτή του φίλου μου.",
        "example2_en": "Although I was tired, I went to my friend's celebration."
    },
    {
        "id": "WR1-U03-005",
        "greek": "επειδή",
        "english": "because / since",
        "notes": "Causal conjunction placed at clause start. Synonymous with γιατί.",
        "gender_or_pos": "conjunction",
        "example_el": "Επειδή είχα υψηλό πυρετό, δεν πήγα σήμερα στο γραφείο.",
        "example_en": "Because I had a high fever, I did not go to the office today.",
        "example2_el": "Επειδή μου αρέσει η θάλασσα, προτιμώ να κάνω διακοπές σε νησί.",
        "example2_en": "Since I like the sea, I prefer vacationing on an island."
    },
    {
        "id": "WR1-U03-006",
        "greek": "γι' αυτό (το λόγο)",
        "english": "for this reason / therefore",
        "notes": "Consecutive connector indicating result or logical conclusion.",
        "gender_or_pos": "phrase",
        "example_el": "Αισθάνομαι άρρωστος, γι' αυτό θα μείνω σήμερα στο σπίτι.",
        "example_en": "I feel sick; for this reason I will stay at home today.",
        "example2_el": "Χάλασε το αυτοκίνητο, γι' αυτό πήραμε το τρένο.",
        "example2_en": "The car broke down; therefore, we took the train."
    },
    {
        "id": "WR1-U03-007",
        "greek": "όταν",
        "english": "when / whenever",
        "notes": "Temporal conjunction connecting dependent time clauses with main clause.",
        "gender_or_pos": "conjunction",
        "example_el": "Όταν φτάσαμε στο νησί, ενθουσιαστήκαμε με το τοπίο.",
        "example_en": "When we arrived on the island, we were thrilled with the landscape.",
        "example2_el": "Όταν έχεις ελεύθερο χρόνο, πάρε με ένα τηλέφωνο.",
        "example2_en": "When you have free time, give me a call."
    },
    {
        "id": "WR1-U03-008",
        "greek": "πριν από",
        "english": "before",
        "notes": "Preposition of time. Followed by noun or dependent clause (πριν + να).",
        "gender_or_pos": "preposition",
        "example_el": "Πριν από τις διακοπές, πρέπει να κλείσουμε τα εισιτήρια του πλοίου.",
        "example_en": "Before the holidays, we must book the ferry tickets.",
        "example2_el": "Φάγαμε πρωινό πριν από την αναχώρηση του λεωφορείου.",
        "example2_en": "We ate breakfast before the bus's departure."
    },
    {
        "id": "WR1-U03-009",
        "greek": "αφού",
        "english": "after / since",
        "notes": "Temporal/causal connector. Expresses sequence or completed condition.",
        "gender_or_pos": "conjunction",
        "example_el": "Αφού τελείωσα τη δουλειά μου, πήγα κατευθείαν στην παραλία.",
        "example_en": "After I finished my work, I went straight to the beach.",
        "example2_el": "Αφού σου αρέσει το ελληνικό φαγητό, πρέπει να δοκιμάσεις μουσακά.",
        "example2_en": "Since you like Greek food, you must try moussaka."
    },
    {
        "id": "WR1-U03-010",
        "greek": "λοιπόν",
        "english": "well then / so",
        "notes": "Discourse marker used to open proposals, summaries, or conclusions.",
        "gender_or_pos": "particle",
        "example_el": "Λοιπόν, τι ώρα θα συναντηθούμε το Σάββατο στην πλατεία;",
        "example_en": "Well then, what time shall we meet on Saturday in the square?",
        "example2_el": "Λοιπόν, αποφάσισα να νοικιάσω αυτό το διαμέρισμα.",
        "example2_en": "So, I decided to rent this apartment."
    }
]

# --------------------------------------------------------------------
# UNIT WR1-05: Error Hunter & Orthography Traps (Format C)
# --------------------------------------------------------------------
CARDS_WR1_05 = [
    {
        "id": "WR1-U05-001",
        "greek": "πολύ vs πολλή",
        "english": "much/very: adverb/neuter (πολύ) vs feminine noun modifier (πολλή)",
        "notes": "Top spelling trap. Adverb: 'πολύ καλά'. Feminine noun: 'πολλή δουλειά', 'πολλή ζέστη'.",
        "gender_or_pos": "grammar trap",
        "example_el": "Είχα πολλή δουλειά σήμερα στο γραφείο και κουράστηκα πολύ.",
        "example_en": "I had a lot of work today at the office and got very tired.",
        "example2_el": "Έκανε πολλή ζέστη, αλλά περάσαμε πολύ όμορφα.",
        "example2_en": "It was very hot, but we had a very nice time."
    },
    {
        "id": "WR1-U05-002",
        "greek": "τον / την (τελικό ν)",
        "english": "final nu rule before vowels and stops (κ, π, τ, μπ, ντ, γκ, τσ, τζ, ξ, ψ)",
        "notes": "Retention of final ν is mandatory before vowels and plosives (τον φίλο vs τον πατέρα).",
        "gender_or_pos": "orthography rule",
        "example_el": "Είδα τον πατέρα μου και την καθηγήτριά μου στο δρόμο.",
        "example_en": "I saw my father and my teacher on the street.",
        "example2_el": "Άκουσα το τραγούδι και τη μουσική από μακριά.",
        "example2_en": "I heard the song and the music from afar."
    },
    {
        "id": "WR1-U05-003",
        "greek": "-τε vs -ται",
        "english": "second person plural active (-τε) vs third person singular mediopassive (-ται)",
        "notes": "Top morphological trap: εσείς κάνετε (active -τε) vs αυτός κοιμάται (passive -ται).",
        "gender_or_pos": "morphology trap",
        "example_el": "Εσείς τι κάνετε το απόγευμα όταν εκείνος ξεκουράζεται;",
        "example_en": "What are you doing in the afternoon when he is resting?",
        "example2_el": "Περιμένετε λίγο παρακαλώ, γιατί ο γιατρός ετοιμάζεται.",
        "example2_en": "Wait a little, please, because the doctor is getting ready."
    },
    {
        "id": "WR1-U05-004",
        "greek": "πέρυσι / πέρσι",
        "english": "last year (spelling with υ and ι)",
        "notes": "Spelling safe harbor: π-έ-ρ-υ-σ-ι. Common error is spelling with ι or η.",
        "gender_or_pos": "adverb (spelling)",
        "example_el": "Πέρυσι το καλοκαίρι πήγαμε διακοπές στη Νάξο.",
        "example_en": "Last year in the summer we went on vacation to Naxos.",
        "example2_el": "Πέρυσι τέτοια εποχή έμενα ακόμα στη Θεσσαλονίκη.",
        "example2_en": "Last year at this time I was still living in Thessaloniki."
    },
    {
        "id": "WR1-U05-005",
        "greek": "περασμένος, -η, -ο",
        "english": "past / previous (spelling with double sigma: -σσ-)",
        "notes": "Spelled with double sigma: περασμένος (from περνάω). E.g. την περασμένη εβδομάδα.",
        "gender_or_pos": "adjective (spelling)",
        "example_el": "Τον περασμένο μήνα άλλαξα διαμέρισμα και γειτονιά.",
        "example_en": "Last month I changed apartment and neighborhood.",
        "example2_el": "Την περασμένη Κυριακή πήγαμε εκδρομή στο βουνό.",
        "example2_en": "Last Sunday we went on an excursion to the mountain."
    },
    {
        "id": "WR1-U05-006",
        "greek": "είμαι vs είχα vs ήμουν",
        "english": "tense distinction: I am (είμαι) vs I had (είχα) vs I was (ήμουν)",
        "notes": "Crucial distinction between present auxiliary, past possession, and past existence.",
        "gender_or_pos": "verb distinction",
        "example_el": "Χθες ήμουν άρρωστος και είχα πυρετό, αλλά σήμερα είμαι πολύ καλύτερα.",
        "example_en": "Yesterday I was sick and had a fever, but today I am much better.",
        "example2_el": "Όταν ήμουν μικρός, είχα έναν σκύλο.",
        "example2_en": "When I was young, I had a dog."
    },
    {
        "id": "WR1-U05-007",
        "greek": "μου / σου / του (θέση κλιτικών)",
        "english": "weak clitic pronouns position before finite verbs and after imperatives",
        "notes": "Placement rule: 'μου είπε' (before verb) vs 'πες μου' (after imperative).",
        "gender_or_pos": "syntax rule",
        "example_el": "Μου έδωσε τα κλειδιά και μου είπε να προσέχω.",
        "example_en": "He gave me the keys and told me to be careful.",
        "example2_el": "Δώσε μου σε παρακαλώ το τηλέφωνο του γιατρού.",
        "example2_en": "Give me, please, the doctor's phone number."
    },
    {
        "id": "WR1-U05-008",
        "greek": "στο / στη(ν) / στο / στους / στις / στα",
        "english": "preposition 'σε' + definite article contractions",
        "notes": "Mandatory contraction in Greek: σε + τον -> στον, σε + την -> στην, σε + το -> στο.",
        "gender_or_pos": "contraction rule",
        "example_el": "Πήγαμε στο νησί, μείναμε στο ξενοδοχείο και φάγαμε στην ταβέρνα.",
        "example_en": "We went to the island, stayed at the hotel, and ate at the taverna.",
        "example2_el": "Συναντηθήκαμε στις οκτώ το βράδυ στον σταθμό του μετρό.",
        "example2_en": "We met at eight in the evening at the metro station."
    },
    {
        "id": "WR1-U05-009",
        "greek": "ανυπομονώ να...",
        "english": "I look forward to... (+ subjunctive)",
        "notes": "Fixed collocation followed by subjunctive 'να'. Great closing formula in Task 1/2.",
        "gender_or_pos": "phrase",
        "example_el": "Ανυπομονώ να σε δω το Σαββατοκύριακο και να τα πούμε.",
        "example_en": "I look forward to seeing you over the weekend and catching up.",
        "example2_el": "Ανυπομονούμε να έρθουμε στο πάρτι των γενεθλίων σου.",
        "example2_en": "We look forward to coming to your birthday party."
    },
    {
        "id": "WR1-U05-010",
        "greek": "περνάω υπέροχα / πέρασα αξέχαστα",
        "english": "I am having a wonderful time / I had an unforgettable time",
        "notes": "Fixed idiomatic formula for holiday and party descriptions in Task 2.",
        "gender_or_pos": "idiom",
        "example_el": "Περάσαμε αξέχαστα στην Κρήτη και θέλουμε να ξαναπάμε του χρόνου.",
        "example_en": "We had an unforgettable time in Crete and want to go back next year.",
        "example2_el": "Περνάω υπέροχα στις διακοπές μου και ξεκουράζομαι πολύ.",
        "example2_en": "I am having a wonderful time on my holidays and resting a lot."
    }
]

# --------------------------------------------------------------------
# UNIT WR1-06: Lego Sentence Builders — Task 1 Functional Notes
# --------------------------------------------------------------------
CARDS_WR1_06 = [
    {
        "id": "WR1-U06-001",
        "greek": "Σου γράφω αυτό το σημείωμα για να σου πω...",
        "english": "I am writing you this note to tell you...",
        "notes": "[Lego Builder] Standard opening sentence for functional Task 1 notes (30-45 words).",
        "gender_or_pos": "sentence frame",
        "example_el": "Σου γράφω αυτό το σημείωμα για να σου πω ότι σήμερα θα αργήσω να γυρίσω.",
        "example_en": "I am writing you this note to tell you that today I will be late returning.",
        "example2_el": "Σου γράφω αυτό το σύντομο σημείωμα για να σου αφήσω τα κλειδιά.",
        "example2_en": "I am writing you this brief note to leave you the keys."
    },
    {
        "id": "WR1-U06-002",
        "greek": "Έχω αφήσει τα κλειδιά στο γραφείο σου.",
        "english": "I have left the keys on your desk.",
        "notes": "[Lego Builder] Perfect tense (έχω αφήσει) stating key location for roommates/colleagues.",
        "gender_or_pos": "sentence",
        "example_el": "Έχω αφήσει τα κλειδιά του σπιτιού στο πάνω συρτάρι του γραφείου σου.",
        "example_en": "I have left the house keys in the top drawer of your desk.",
        "example2_el": "Έχω αφήσει τα κλειδιά στον γείτονα του πρώτου ορόφου.",
        "example2_en": "I have left the keys with the first-floor neighbor."
    },
    {
        "id": "WR1-U06-003",
        "greek": "Μπορείς σε παρακαλώ να ποτίσεις τα φυτά;",
        "english": "Could you please water the plants?",
        "notes": "[Lego Builder] Modal polite request in neighbor notes during absence.",
        "gender_or_pos": "question",
        "example_el": "Μπορείς σε παρακαλώ να ποτίσεις τα φυτά στο μπαλκόνι δύο φορές την εβδομάδα;",
        "example_en": "Could you please water the plants on the balcony twice a week?",
        "example2_el": "Μπορείς σε παρακαλώ να ταΐσεις τη γάτα όσο θα λείπω;",
        "example2_en": "Could you please feed the cat while I will be away?"
    },
    {
        "id": "WR1-U06-004",
        "greek": "Θέλεις να πάμε μαζί για καφέ το απόγευμα;",
        "english": "Do you want to go together for coffee this afternoon?",
        "notes": "[Lego Builder] Informal invitation sentence frame.",
        "gender_or_pos": "question",
        "example_el": "Θέλεις να πάμε μαζί για καφέ το απόγευμα στην πλατεία;",
        "example_en": "Do you want to go together for coffee this afternoon in the square?",
        "example2_el": "Θέλεις να πάμε για φαγητό μετά το μάθημα των ελληνικών;",
        "example2_en": "Do you want to go for food after the Greek lesson?"
    },
    {
        "id": "WR1-U06-005",
        "greek": "Δυστυχώς δεν θα μπορέσω να έρθω στο ραντεβού.",
        "english": "Unfortunately I won't be able to come to the appointment.",
        "notes": "[Lego Builder] Polite cancellation/decline frame with modal future.",
        "gender_or_pos": "sentence",
        "example_el": "Δυστυχώς δεν θα μπορέσω να έρθω στο ραντεβού μας γιατί προέκυψε κάτι επείγον.",
        "example_en": "Unfortunately I won't be able to come to our appointment because something urgent came up.",
        "example2_el": "Δυστυχώς δεν θα μπορέσω να παρευρεθώ στη συνάντηση λόγω ασθένειας.",
        "example2_en": "Unfortunately I won't be able to attend the meeting due to illness."
    },
    {
        "id": "WR1-U06-006",
        "greek": "Τι λες να το κανονίσουμε για την επόμενη εβδομάδα;",
        "english": "What do you say we arrange it for next week?",
        "notes": "[Lego Builder] Alternative date proposal after declining.",
        "gender_or_pos": "question",
        "example_el": "Τι λες να το κανονίσουμε για την επόμενη εβδομάδα που θα έχω περισσότερο χρόνο;",
        "example_en": "What do you say we arrange it for next week when I will have more time?",
        "example2_el": "Τι λες να βρεθούμε την Τετάρτη αντί για τη Δευτέρα;",
        "example2_en": "What do you say we meet on Wednesday instead of Monday?"
    },
    {
        "id": "WR1-U06-007",
        "greek": "Σε παρακαλώ, διάβασε τα επείγοντα μηνύματα.",
        "english": "Please read the urgent messages.",
        "notes": "[Lego Builder] Workplace handover imperative in absence notes.",
        "gender_or_pos": "imperative sentence",
        "example_el": "Σε παρακαλώ, διάβασε τα επείγοντα μηνύματα και απάντησε στους πελάτες.",
        "example_en": "Please read the urgent messages and reply to the clients.",
        "example2_el": "Σε παρακαλώ, ενημέρωσε τον διευθυντή για την απουσία μου.",
        "example2_en": "Please inform the manager about my absence."
    },
    {
        "id": "WR1-U06-008",
        "greek": "Σου αφήνω τα χρήματα πάνω στο τραπέζι.",
        "english": "I am leaving you the money on the table.",
        "notes": "[Lego Builder] Shared flat / utility bill note statement.",
        "gender_or_pos": "sentence",
        "example_el": "Σου αφήνω τα χρήματα για τον λογαριασμό του ρεύματος πάνω στο τραπέζι.",
        "example_en": "I am leaving you the money for the electricity bill on the table.",
        "example2_el": "Σου αφήνω το μερίδιό μου για τα κοινόχρηστα στο σαλόνι.",
        "example2_en": "I am leaving you my share for the building maintenance in the living room."
    },
    {
        "id": "WR1-U06-009",
        "greek": "Μην ξεχάσεις να κλειδώσεις την εξώπορτα.",
        "english": "Don't forget to lock the front door.",
        "notes": "[Lego Builder] Negative imperative reminder: μην + subjunctive (μην ξεχάσεις).",
        "gender_or_pos": "imperative sentence",
        "example_el": "Όταν φύγεις από το σπίτι, μην ξεχάσεις να κλειδώσεις την εξώπορτα.",
        "example_en": "When you leave the house, don't forget to lock the front door.",
        "example2_el": "Μην ξεχάσεις να σβήσεις τα φώτα και το κλιματιστικό.",
        "example2_en": "Don't forget to turn off the lights and the air conditioner."
    },
    {
        "id": "WR1-U06-010",
        "greek": "Θα επιστρέψω το βράδυ γύρω στις εννέα.",
        "english": "I will return tonight around nine.",
        "notes": "[Lego Builder] Stating anticipated return time in daily notes.",
        "gender_or_pos": "sentence",
        "example_el": "Έχω πολλές δουλειές στην πόλη, οπότε θα επιστρέψω το βράδυ γύρω στις εννέα.",
        "example_en": "I have many errands in the city, so I will return tonight around nine.",
        "example2_el": "Θα επιστρέψω από το γραφείο νωρίς το απόγευμα.",
        "example2_en": "I will return from the office early in the afternoon."
    }
]

# --------------------------------------------------------------------
# UNIT WR2-01: Thematic Playbook 1 — Social Invitations, Birthdays & RSVP
# --------------------------------------------------------------------
CARDS_WR2_01 = [
    {
        "id": "WR2-U01-001",
        "greek": "Το Σάββατο έχω τα γενέθλιά μου και κάνω πάρτι.",
        "english": "On Saturday it's my birthday and I am throwing a party.",
        "notes": "[Playbook 1] Core anchor sentence opening birthday invitations in Task 1.",
        "gender_or_pos": "sentence",
        "example_el": "Αυτό το Σάββατο έχω τα γενέθλιά μου και κάνω ένα μεγάλο πάρτι στο σπίτι μου.",
        "example_en": "This Saturday it's my birthday and I am throwing a big party at my house.",
        "example2_el": "Την επόμενη εβδομάδα έχω τα γενέθλιά μου και θέλω να το γιορτάσουμε μαζί.",
        "example2_en": "Next week is my birthday and I want us to celebrate it together."
    },
    {
        "id": "WR2-U01-002",
        "greek": "Θα χαρώ πολύ αν έρθεις στη γιορτή μου.",
        "english": "I will be very glad if you come to my celebration.",
        "notes": "[Playbook 1] Polite conditional welcome formula.",
        "gender_or_pos": "sentence",
        "example_el": "Θα χαρώ πάρα πολύ αν έρθεις στη γιορτή μου με την παρέα σου.",
        "example_en": "I will be very glad if you come to my celebration with your friends.",
        "example2_el": "Θα χαρούμε πολύ αν μπορέσετε να παρευρεθείτε στο δείπνο.",
        "example2_en": "We will be very glad if you can attend the dinner."
    },
    {
        "id": "WR2-U01-003",
        "greek": "Το πάρτι θα αρχίσει στις οκτώ το βράδυ.",
        "english": "The party will start at eight in the evening.",
        "notes": "[Playbook 1] Time specification essential for exam task fulfillment.",
        "gender_or_pos": "sentence",
        "example_el": "Το πάρτι θα αρχίσει στις οκτώ το βράδυ και θα έχει πολλή μουσική και φαγητό.",
        "example_en": "The party will start at eight in the evening and will have lots of music and food.",
        "example2_el": "Η εκδήλωση θα ξεκινήσει στις εννέα ακριβώς στην ταράτσα.",
        "example2_en": "The event will start at nine sharp on the terrace."
    },
    {
        "id": "WR2-U01-004",
        "greek": "Μην φέρεις τίποτα, θα έχω φαγητό και ποτά.",
        "english": "Don't bring anything; I will have food and drinks.",
        "notes": "[Playbook 1] Friendly hospitality note in invitations.",
        "gender_or_pos": "sentence",
        "example_el": "Μην φέρεις τίποτα απολύτως, θα έχω ετοιμάσει φαγητό, γλυκά και ποτά για όλους.",
        "example_en": "Don't bring anything at all; I will have prepared food, sweets, and drinks for everyone.",
        "example2_el": "Μην ανησυχείς για τίποτα, έχουμε κανονίσει όλο το φαγητό.",
        "example2_en": "Don't worry about anything; we have arranged all the food."
    },
    {
        "id": "WR2-U01-005",
        "greek": "Πες μου μέχρι την Παρασκευή αν θα έρθεις.",
        "english": "Tell me by Friday if you will come (RSVP deadline).",
        "notes": "[Playbook 1] Essential confirmation deadline requested by exam prompts.",
        "gender_or_pos": "sentence",
        "example_el": "Σε παρακαλώ, πες μου μέχρι την Παρασκευή αν θα έρθεις για να ξέρω πόσα άτομα θα είμαστε.",
        "example_en": "Please tell me by Friday if you will come so I know how many people we will be.",
        "example2_el": "Ενημέρωσέ με μέχρι την Πέμπτη αν μπορείς να έρθεις.",
        "example2_en": "Let me know by Thursday if you can make it."
    },
    {
        "id": "WR2-U01-006",
        "greek": "Σε ευχαριστώ πολύ για την πρόσκληση!",
        "english": "Thank you very much for the invitation!",
        "notes": "[Playbook 1] Mandatory opener when replying to invitations.",
        "gender_or_pos": "phrase",
        "example_el": "Σε ευχαριστώ πάρα πολύ για την όμορφη πρόσκληση στα γενέθλιά σου!",
        "example_en": "Thank you so much for the lovely invitation to your birthday!",
        "example2_el": "Σας ευχαριστούμε θερμά για την πρόσκληση στον γάμο σας.",
        "example2_en": "We thank you warmly for the invitation to your wedding."
    },
    {
        "id": "WR2-U01-007",
        "greek": "Με μεγάλη μου χαρά δέχομαι να έρθω.",
        "english": "With great pleasure I accept to come.",
        "notes": "[Playbook 1] Positive RSVP acceptance formula.",
        "gender_or_pos": "sentence",
        "example_el": "Με μεγάλη μου χαρά δέχομαι να έρθω στο πάρτι και ανυπομονώ να σε δω!",
        "example_en": "With great pleasure I accept to come to the party and look forward to seeing you!",
        "example2_el": "Φυσικά και θα έρθω, δεν θα έχανα με τίποτα τη γιορτή σου.",
        "example2_en": "Of course I will come; I wouldn't miss your celebration for anything."
    },
    {
        "id": "WR2-U01-008",
        "greek": "Δυστυχώς δεν μπορώ να έρθω γιατί θα λείπω.",
        "english": "Unfortunately I cannot come because I will be away.",
        "notes": "[Playbook 1] Negative RSVP with polite travel excuse.",
        "gender_or_pos": "sentence",
        "example_el": "Δυστυχώς δεν μπορώ να έρθω στο πάρτι γιατί εκείνο το Σαββατοκύριακο θα λείπω σε ταξίδι.",
        "example_en": "Unfortunately I cannot come to the party because that weekend I will be away on a trip.",
        "example2_el": "Λυπάμαι πολύ αλλά δεν θα μπορέσω να παρευρεθώ λόγω επαγγελματικού ταξιδιού.",
        "example2_en": "I am very sorry but I will not be able to attend due to a business trip."
    },
    {
        "id": "WR2-U01-009",
        "greek": "Σου εύχομαι ολόψυχα χρόνια πολλά και καλή χρονιά!",
        "english": "I wish you from my heart many happy years and a good year!",
        "notes": "[Playbook 1] Warm birthday/nameday wish formula.",
        "gender_or_pos": "sentence",
        "example_el": "Σου εύχομαι ολόψυχα χρόνια πολλά, υγεία, ευτυχία και κάθε επιτυχία στη ζωή σου!",
        "example_en": "I wish you from my heart many happy years, health, happiness, and every success in your life!",
        "example2_el": "Χρόνια πολλά για την ονομαστική σου γιορτή, να είσαι πάντα χαρούμενος!",
        "example2_en": "Happy name day, may you always be joyful!"
    },
    {
        "id": "WR2-U01-010",
        "greek": "Ελπίζω να βρεθούμε μια άλλη μέρα να κεράσω.",
        "english": "I hope we meet another day so I can treat you.",
        "notes": "[Playbook 1] Polite restorative closing after declining an invite.",
        "gender_or_pos": "sentence",
        "example_el": "Λυπάμαι που δεν θα είμαι εκεί, αλλά ελπίζω να βρεθούμε μια άλλη μέρα να σε κεράσω καφέ.",
        "example_en": "I am sorry I won't be there, but I hope we meet another day so I can treat you to coffee.",
        "example2_el": "Υπόσχομαι να βρεθούμε μόλις επιστρέψω για να γιορτάσουμε μαζί.",
        "example2_en": "I promise we'll meet as soon as I return to celebrate together."
    }
]

def main():
    print("--- Building KEG-A2-WR-P1 & KEG-A2-WR-P2 ---")
    
    # 1. Save WR1 units
    save_unit(
        "unit-wr1-01",
        "Μάθημα 1: Αποκωδικοποίηση Οδηγιών & Ρήματα Εξεταστή (Prompt Decoders & Examiner Directives)",
        "Mastering authentic Greek exam instructions: action verbs (περιγράψτε, εξηγήστε, προτείνετε, ζητήστε, ενημερώστε, προσκαλέστε) and tense cues.",
        "Unit WR1-01 Core Notes: Prompt Decoders & Action Verbs\n• Examiner Action Verbs:\n  - Περιγράψτε: describe (adjectives & details)\n  - Εξηγήστε γιατί: explain why (causal connectors)\n  - Προτείνετε: suggest / recommend\n  - Ζητήστε πληροφορίες: ask for details (questions)\n  - Ενημερώστε: notify / inform\n  - Προσκαλέστε: invite (occasion, time, venue).",
        CARDS_WR1_01
    )
    
    save_unit(
        "unit-wr1-02",
        "Μάθημα 2: Φόρμουλες Έναρξης, Μετάβασης & Κλεισίματος (Formulaic Openers, Transitions & Closers)",
        "Standard letter and email frameworks: friendly salutations, transition chunks, apologies for late replies, call-to-action closers, and sign-offs.",
        "Unit WR1-02 Core Notes: Openers, Transitions & Closers\n• Openers: Αγαπητέ μου / Αγαπητή μου..., Γεια σου! Πώς είσαι;\n• Transitions: Συγγνώμη που άργησα να σου γράψω..., Σου γράφω για να σου πω...\n• Closers: Περιμένω νέα σου, Πάρε με τηλέφωνο, Σε φιλώ, Με πολλή αγάπη.",
        CARDS_WR1_02
    )
    
    save_unit(
        "unit-wr1-03",
        "Μάθημα 3: Συνδετικές Λέξεις & Συντακτική Συνοχή (Discourse Connectors & Logical Flow)",
        "High-scoring sentence linkers: sequence (πρώτα... μετά... στο τέλος), contrast (όμως, αν και), cause/effect (επειδή, γι' αυτό), and condition (όταν, πριν από, αφού).",
        "Unit WR1-03 Core Notes: Connectors & Syntax\n• Sequence: πρώτα, μετά, έπειτα, στο τέλος\n• Contrast: αλλά, όμως, αν και\n• Cause & Effect: γιατί, επειδή, γι' αυτό το λόγο\n• Condition & Time: όταν, πριν από, αφού, λοιπόν.",
        CARDS_WR1_03
    )
    
    # Save WR1-04 (Safe harbors from existing writing cards)
    import subprocess
    res = subprocess.run(["git", "show", "1cf0e0d:content/unit-a2-10/lesson-01.yaml"], capture_output=True, text=True, encoding="utf-8")
    if res.returncode == 0:
        sh_data = yaml.safe_load(res.stdout)
        sh_cards = sh_data.get("entries", [])
        save_unit(
            "unit-wr1-04",
            "Μάθημα 4: Γραμματικοί Ασφαλείς Λιμένες & Ανώμαλοι Αόριστοι (Grammar Safe Harbors)",
            sh_data.get("description", "Eliminating high-penalty errors in A2 written exams: irregular past stems, clitic pronoun positions, and modal subjunctive rules."),
            sh_data.get("lesson_notes", ""),
            sh_cards
        )
    save_unit(
        "unit-wr1-05",
        "Μάθημα 5: Παγίδες Ορθογραφίας, Τόνοι & Συμφωνία (Error Hunter & Orthography Traps)",
        "Eliminating high-penalty errors in written production: πολύ vs πολλή, final nu rules, -τε vs -ται verb endings, stress marks (τόνος), and clitic pronoun placement.",
        "Unit WR1-05 Core Notes: Orthography & Morphology Traps\n• πολύ (adverb/neuter) vs πολλή (feminine noun modifier: πολλή δουλειά)\n• -τε (active 2nd plural: κάνετε) vs -ται (mediopassive 3rd singular: κοιμάται)\n• Τόνος: mandatory on EVERY word of 2+ syllables\n• Final nu: preserved before vowels and stops (κ, π, τ, μπ, ντ, γκ, τσ, τζ, ξ, ψ).",
        CARDS_WR1_05
    )
    
    save_unit(
        "unit-wr1-06",
        "Μάθημα 6: Lego Sentence Builders — Task 1 Σημειώματα & Μηνύματα (Task 1 Functional Notes)",
        "Modular sentence building blocks for Task 1 functional notes (30-45 words): arrangements, leaving keys, watering plants, excusing absence, and reminders.",
        "Unit WR1-06 Core Notes: Task 1 Functional Notes (30–45 words)\n• Structure:\n  1. Greeting (Γεια σου [Όνομα])\n  2. Purpose (Σου γράφω για να σου πω... / Έχω αφήσει...)\n  3. Instructions or polite request (Μπορείς σε παρακαλώ να...)\n  4. Action closer (Πάρε με τηλέφωνο / Σε φιλώ).",
        CARDS_WR1_06
    )

    # Save WR2-01 (Playbook 1)
    save_unit(
        "unit-wr2-01",
        "Μάθημα 1: Προσκλήσεις, Γενέθλια & RSVP (Thematic Playbook 1: Social Invitations & Parties)",
        "Mastering Task 1 notes: composing and replying to party, birthday, and celebration invitations, accepting or politely declining with justifications.",
        "Unit WR2-01 Core Notes: Social Invitations (Task 1)\n• Key elements:\n  - Αφορμή: Έχω τα γενέθλιά μου / Κάνω πάρτι.\n  - Χρόνος & Τόπος: Το Σάββατο στις 8:00 στο σπίτι μου.\n  - Φιλοξενία: Μην φέρεις τίποτα, θα έχω φαγητό και ποτά.\n  - RSVP: Πες μου μέχρι την Παρασκευή αν θα έρθεις.\n  - Αποδοχή / Άρνηση: Με μεγάλη χαρά δέχομαι vs Δυστυχώς θα λείπω.",
        CARDS_WR2_01
    )

if __name__ == '__main__':
    main()

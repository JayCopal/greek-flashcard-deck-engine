# -*- coding: utf-8 -*-
"""
Curriculum Synchronizer (JSON Batch -> YAML SSOT)
Converts raw CEFR A1 curriculum batches into the project's single source of truth:
  - content/manifest.yaml
  - content/unit-XX/lesson-YY.yaml
Preserves all verified audio assets and existing lesson statuses.
"""
import sys
import glob
import json
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
AUDIO_DIR = BASE_DIR / "audio"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

UNIT_METADATA = {
    1: {
        "title": "Χαιρετισμοί & Γνωριμία (Greetings & Introductions)",
        "description": "CEFR A1: Formal & informal greetings, polite addresses, personal pronouns, and core verbs (είμαι, λέω, γράφω).",
        "lesson_notes": (
            "Unit 1 Core Grammar Notes:\n"
            "• Vocative Singular: Masculine nouns in -ος end in -ε (κύριε Παπαδόπουλε). Feminine nouns in -α/-η remain unchanged (κυρία, δεσποινίς).\n"
            "• Copular Verb 'είμαι' (Present): εγώ είμαι, εσύ είσαι, αυτός/αυτή/αυτό είναι, εμείς είμαστε, εσείς είστε, αυτοί/αυτές/αυτά είναι.\n"
            "• Stating Names: 'Με λένε + Accusative' (e.g. Με λένε Κώστα) or 'Είμαι ο/η + Nominative'."
        ),
    },
    2: {
        "title": "Καταγωγή, Εθνικότητες & Γλώσσες (Origins, Nationalities & Languages)",
        "description": "CEFR A1: Countries, nationalities, spoken languages, and verbs of residence & communication (μένω, μιλάω, μαθαίνω).",
        "lesson_notes": (
            "Unit 2 Core Grammar Notes:\n"
            "• Expressing Origin: 'από + Accusative' (e.g., Από πού είσαι; — Είμαι από την Ελλάδα).\n"
            "• Expressing Residence: 'σε + Accusative' contracts with article: σε + την = στην, σε + το = στο, σε + τον = στον (e.g., Μένω στην Αθήνα).\n"
            "• Nationalities: Masculine in -ος/-ας/-ης, Feminine in -ίδα/-α (ο Έλληνας / η Ελληνίδα, ο Άγγλος / η Αγγλίδα).\n"
            "• Languages: Neuter plural with definite article (τα ελληνικά, τα αγγλικά, τα γαλλικά)."
        ),
    },
    3: {
        "title": "Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας (Professions & Contact Details)",
        "description": "CEFR A1: Occupations, workplaces, phone numbers, addresses, digits 0-10, and verbs (δουλεύω, σπουδάζω, διδάσκω).",
        "lesson_notes": (
            "Unit 3 Core Grammar Notes:\n"
            "• Inquiring about Profession: 'Τι δουλειά κάνεις;' (informal) or 'Ποιο είναι το επάγγελμά σας;' (formal).\n"
            "• Stating Profession: Copula 'είμαι' + Profession noun WITHOUT indefinite article (e.g., Είμαι γιατρός / Είμαι φοιτητής).\n"
            "• Workplaces with Preposition 'σε': δουλεύω σε γραφείο (in an office), δουλεύω στο νοσοκομείο (at the hospital).\n"
            "• Digits 0–10: μηδέν, ένα, δύο, τρία, τέσσερα, πέντε, έξι, επτά, οκτώ, εννέα, δέκα.\n"
            "• Stating Phone & Address: 'Το τηλέφωνό μου είναι...' / 'Μένω στην οδό... αριθμός...'."
        ),
    },
    4: {
        "title": "Οικογένεια, Πρόσωπα & Περιγραφή (Family & Physical/Personal Traits)",
        "description": "CEFR A1: Family relations, marital status, physical descriptions, the verb 'έχω', and possessive enclitics (μου, σου, του, της).",
        "lesson_notes": (
            "Unit 4 Core Grammar Notes:\n"
            "• Possessive Enclitic Clitics: Placed directly AFTER the noun with definite article: ο πατέρας μου (my father), η μητέρα σου (your mother), το παιδί της (her child).\n"
            "• Double Accent Rule: Proparoxytone nouns (accented on 3rd syllable from end) take an additional accent on the last syllable before a possessive clitic (e.g., το αυτοκίνητό μου).\n"
            "• Describing People: Verb 'είμαι' + Adjective (e.g., Είναι ψηλός, αδύνατος και πολύ συμπαθητικός). Adjectives agree in gender, number, and case with the noun.\n"
            "• The Verb 'έχω' (to have): εγώ έχω, εσύ έχεις, αυτός/αυτή/αυτό έχει, εμείς έχουμε, εσείς έχετε, αυτοί/αυτές/αυτά έχουν."
        ),
    },
    5: {
        "title": "Στο Καφέ & Στην Ταβέρνα (Ordering Food & Drinks)",
        "description": "CEFR A1: Reading Greek menus, ordering food and drinks, coffee preparation styles, taverna etiquette, and consumption verbs (θέλω, πίνω, παίρνω, τρώω).",
        "lesson_notes": (
            "Unit 5 Core Grammar Notes:\n"
            "• Verbs of Consumption & Preference (Present Active Indicative):\n"
            "  - θέλω (Type A): θέλω, θέλεις, θέλει, θέλουμε, θέλετε, θέλουν.\n"
            "  - πίνω (Type A): πίνω, πίνεις, πίνει, πίνουμε, πίνετε, πίνουν.\n"
            "  - παίρνω (Type A): παίρνω, παίρνεις, παίρνει, παίρνουμε, παίρνετε, παίρνουν.\n"
            "  - τρώω (Type A irregular): τρώω, τρως, τρώει, τρώμε, τρώτε, τρώνε.\n"
            "• Direct Object in Accusative with Indefinite Article:\n"
            "  - Masculine: έναν καφέ, έναν χυμό\n"
            "  - Feminine: μία μπίρα (μπύρα), μία σαλάτα\n"
            "  - Neuter: ένα νερό, ένα τοστ, ένα σουβλάκι\n"
            "• Greek Coffee Sweetness Degrees:\n"
            "  - σκέτος (plain / zero sugar)\n"
            "  - μέτριος (medium / 1 spoon sugar)\n"
            "  - γλυκός (sweet / 2 spoons sugar)\n"
            "• Common Ordering Formulas:\n"
            "  - 'Τι θα πάρετε;' (What will you have?)\n"
            "  - 'Για μένα... παρακαλώ.' (For me... please.)\n"
            "  - 'Τον λογαριασμό, παρακαλώ.' (The bill, please.)\n"
            "  - 'Ορίστε!' (Here you are! / Certainly!)\n"
            "  - 'Καλή όρεξη!' (Enjoy your meal!) / 'Στην υγειά μας!' (Cheers!)"
        ),
    },
    6: {
        "title": "Στην Αγορά, Ψώνια & Τιμές (Shopping, Supermarket & Prices)",
        "description": "CEFR A1: Supermarket shopping, farmers' market transactions, buying groceries and clothes, asking for prices and weights, and payment methods.",
        "lesson_notes": (
            "Unit 6 Core Grammar Notes:\n"
            "• Inquiring about Prices:\n"
            "  - Singular: 'Πόσο κάνει;' / 'Πόσο κοστίζει;' (e.g. Πόσο κάνει το γάλα;)\n"
            "  - Plural: 'Πόσο έχουν;' / 'Πόσο κάνουν;' (e.g. Πόσο έχουν τα πορτοκάλια;)\n"
            "• Units of Measurement & Packaging:\n"
            "  - το κιλό (kilo) / μισό κιλό (half kilo)\n"
            "  - το γραμμάριο (gram) / διακόσια γραμμάρια (200g)\n"
            "  - το λίτρο (liter) / το μπουκάλι (bottle) / το πακέτο (packet)\n"
            "• Neuter Nouns in -ο, -ι, -μα:\n"
            "  - In -ο: το κιλό -> τα κιλά, το λίτρο -> τα λίτρα, το μήλο -> τα μήλα.\n"
            "  - In -ι: το ψωμί -> τα ψωμιά, το τυρί -> τα τυριά, το μαγαζί -> τα μαγαζιά.\n"
            "  - In -μα: το χρώμα -> τα χρώματα, το πράγμα -> τα πράγματα.\n"
            "• Payment Methods:\n"
            "  - με μετρητά (with cash)\n"
            "  - με κάρτα (by card)\n"
            "• Key Commercial Expressions:\n"
            "  - 'Ορίστε τα ρέστα σας.' (Here is your change.)\n"
            "  - 'Χρειάζεστε απόδειξη;' (Do you need a receipt?)\n"
            "  - 'Ψάχνω ένα...' (I am looking for a...)"
        ),
    },
    7: {
        "title": "Το Σπίτι, Έπιπλα & Διαμονή (House, Furniture & Accommodation)",
        "description": "CEFR A1: Describing an apartment, rooms of the house, core furniture, spatial prepositions, and understanding classified accommodation listings.",
        "lesson_notes": (
            "Unit 7 Core Grammar Notes:\n"
            "• Existential Construction 'υπάρχει / υπάρχουν':\n"
            "  - Singular: 'Υπάρχει ένα μεγάλο σαλόνι.' (There is a large living room.)\n"
            "  - Plural: 'Υπάρχουν δύο κρεβατοκάμαρες.' (There are two bedrooms.)\n"
            "  - Negative: 'Δεν υπάρχει ασανσέρ.' (There is no elevator.)\n"
            "• Spatial Prepositions & Adverbs (Governing Accusative):\n"
            "  - Governed by 'σε + άρθρο' (contracted): μέσα σε (inside), πάνω σε (on top of), δίπλα σε (next to), ανάμεσα σε (between).\n"
            "  - Governed by 'από + άρθρο': έξω από (outside of), κάτω από (under), απέναντι από (across from), μπροστά από (in front of), πίσω από (behind).\n"
            "• Definite Article Grid (Nominative & Accusative):\n"
            "  - Masculine: Nom: ο / οι — Acc: τον / τους\n"
            "  - Feminine:  Nom: η / οι — Acc: τη(ν) / τις\n"
            "  - Neuter:    Nom: το / τα — Acc: το / τα\n"
            "• Reading Housing Classified Ads (Αγγελίες Κατοικιών):\n"
            "  - ενοικιάζεται (for rent) / πωλείται (for sale)\n"
            "  - γκαρσονιέρα (studio flat), δυάρι (2-room flat), τριάρι (3-room flat)\n"
            "  - όροφος: 1ος (πρώτος), 2ος (δεύτερος), ισόγειο (ground floor)\n"
            "  - επιπλωμένο (furnished) / αυτόνομη θέρμανση (independent heating)"
        ),
    },
    8: {
        "title": "Καθημερινό Πρόγραμμα & Συνήθειες (Daily Routines & Habits)",
        "description": "CEFR A1: Describing daily routines, work and study schedule, frequency adverbs (πάντα, συχνά, ποτέ), Type A, B1, and B2 active verbs, and modal connectors (θέλω να).",
        "lesson_notes": (
            "Unit 8 Core Grammar Notes:\n"
            "• Daily Routine Active Verbs:\n"
            "  - Type A (-ω, -εις, -ει, -ουμε, -ετε, -ουν): αρχίζω, τελειώνω, διαβάζω, γράφω, ακούω, βλέπω, μαγειρεύω, φεύγω, γυρίζω, ψωνίζω.\n"
            "  - Type B1 (-άω/-ώ, -άς, -άει/-ά, -άμε, -άτε, -άνε/-ούν): ξυπνάω/ξυπνώ, περπατάω/περπατώ, τραγουδάω/τραγουδώ.\n"
            "  - Type B2 (-ώ, -είς, -εί, -ούμε, -είτε, -ούν): οδηγώ, μπορώ, ζω.\n"
            "• Strict A1 Active Routine Phrases (Avoiding Mediopassive):\n"
            "  - παίρνω πρωινό (have breakfast)\n"
            "  - κάνω μπάνιο / κάνω ντους (take a bath / shower)\n"
            "  - κάνω γυμναστική (work out / exercise)\n"
            "  - πάω για ύπνο (go to bed / sleep)\n"
            "• Adverbs of Frequency & Scale:\n"
            "  - πάντα (100%) > συνήθως (80%) > συχνά (60%) > μερικές φορές (40%) > σπάνια (10%) > ποτέ (0%).\n"
            "  - Double Negative Rule with ποτέ: 'Δεν' + verb + 'ποτέ' (e.g. Δεν πίνω ποτέ καφέ το βράδυ).\n"
            "• Times of the Day & Temporal Markers:\n"
            "  - το πρωί, το μεσημέρι, το απόγευμα, το βράδυ, τη νύχτα.\n"
            "  - νωρίς (early) vs. αργά (late).\n"
            "• Modal Connective Syntax:\n"
            "  - θέλω να + Present Active Indicative (θέλω να μάθω...)\n"
            "  - μπορώ να + Present Active Indicative (μπορώ να μιλήσω...)"
        ),
    },
    9: {
        "title": "Ώρα, Ημερολόγιο & Ραντεβού (Telling Time, Calendar & Appointments)",
        "description": "CEFR A1: Asking for and stating the time, days of the week, months, seasons, arranging appointments, and understanding timetable announcements.",
        "lesson_notes": (
            "Unit 9 Core Grammar Notes:\n"
            "• Telling Time (Ώρα):\n"
            "  - Inquiring: 'Τι ώρα είναι;' (What time is it?) / 'Σε τι ώρα;' (At what time?).\n"
            "  - Exact hour: 'Είναι μία ακριβώς' (1:00) / 'Είναι δύο ακριβώς' (2:00).\n"
            "  - Minutes past: 'Είναι τρεις και τέταρτο' (3:15) / 'Είναι τέσσερις και είκοσι' (4:20).\n"
            "  - Half past: 'Είναι πέντε και μισή' (5:30).\n"
            "  - Minutes to: 'Είναι έξι παρά είκοσι' (5:40) / 'Είναι επτά παρά τέταρτο' (6:45).\n"
            "  - Specifying when: 'Στη μία' (at 1:00) vs 'Στις τρεις, στις τέσσερις...' (all other hours).\n"
            "• Days of the Week (Ημέρες της Εβδομάδας):\n"
            "  - Feminine (all except Saturday): η Δευτέρα, η Τρίτη, η Τετάρτη, η Πέμπτη, η Παρασκευή, η Κυριακή.\n"
            "  - Neuter: το Σάββατο, το σαββατοκύριακο.\n"
            "  - Temporal Accusative (no preposition): 'τη Δευτέρα' (on Monday), 'το Σάββατο' (on Saturday).\n"
            "• The Four Seasons (Εποχές):\n"
            "  - η άνοιξη (spring), το καλοκαίρι (summer), το φθινόπωρο (autumn), ο χειμώνας (winter).\n"
            "  - Temporal Accusative: 'την άνοιξη', 'το καλοκαίρι', 'το φθινόπωρο', 'τον χειμώνα'.\n"
            "• Months (Μήνες):\n"
            "  - All months in Modern Greek are masculine (ο Ιανουάριος, ο Απρίλιος, ο Αύγουστος...).\n"
            "  - Temporal Accusative: 'τον Ιανουάριο' (in January), 'τον Αύγουστο' (in August).\n"
            "• Time Spans & Scheduling Connectives:\n"
            "  - από... μέχρι... (from... until...): 'από τις εννέα μέχρι τις πέντε'.\n"
            "  - πριν από / μετά από + Accusative.\n"
            "  - κλείνω ραντεβού (make an appointment) / περιμένω (wait for)."
        ),
    },
    10: {
        "title": "Στην Πόλη, Μετακινήσεις & Οδηγίες (City Navigation, Transport & Directions)",
        "description": "CEFR A1: Asking for and giving directions in town, public transportation (metro, bus, train), ticket purchases, and spatial prepositions.",
        "lesson_notes": (
            "Unit 10 Core Grammar Notes:\n"
            "• Asking for Directions in Town:\n"
            "  - Inquiring politely: 'Συγγνώμη, πού είναι το/η/ο...;' (Excuse me, where is the...?).\n"
            "  - 'Πώς πάω στο/στη/στον...;' (How do I get to...?).\n"
            "  - 'Ψάχνω τον σταθμό / το φαρμακείο...' (I am looking for the station / pharmacy...).\n"
            "• Giving Directions (Indicative / Polite 2nd Person Plural -ετε):\n"
            "  - Πηγαίνετε όλο ευθεία. (Go straight ahead.)\n"
            "  - Στρίβετε δεξιά / αριστερά στο πρώτο φανάρι. (Turn right / left at the first traffic light.)\n"
            "  - Περνάτε τη διάβαση / τον δρόμο. (Cross the crosswalk / street.)\n"
            "• Spatial Prepositions & Adverbs (Governing Accusative):\n"
            "  - κοντά σε + Accusative: 'κοντά στον σταθμό' (near the station).\n"
            "  - μακριά από + Accusative: 'μακριά από το κέντρο' (far from downtown).\n"
            "  - απέναντι από + Accusative: 'απέναντι από την τράπεζα' (across from the bank).\n"
            "  - δίπλα σε + Accusative: 'δίπλα στο ταχυδρομείο' (next to the post office).\n"
            "• Public Transportation Formulas:\n"
            "  - Mode of transit with 'με + Definite Accusative': με το μετρό, με το λεωφορείο, με το τρένο, με το ταξί.\n"
            "  - Walking: 'με τα πόδια' (on foot).\n"
            "  - Boarding / Alighting: ανεβαίνω στο λεωφορείο (board) / κατεβαίνω στη στάση (get off).\n"
            "  - Purchasing tickets: ένα απλό εισιτήριο (single) / ένα εισιτήριο μετ' επιστροφής (round-trip)."
        ),
    },
    11: {
        "title": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "description": "CEFR A1: Talking about hobbies, sports, cinema, beach and island vacations, describing the weather, and using direct-object clitic pronouns.",
        "lesson_notes": (
            "Unit 11 Core Grammar Notes:\n"
            "• Weather Idioms & Impersonal Expressions:\n"
            "  - 'Τι καιρό κάνει σήμερα;' (What's the weather like today?).\n"
            "  - 'Κάνει ζέστη / κάνει κρύο' (It is hot / cold).\n"
            "  - 'Έχει ήλιο / έχει συννεφιά / έχει αέρα' (It is sunny / cloudy / windy).\n"
            "  - Impersonal verbs: βρέχει (it rains), χιονίζει (it snows), φυσάει (the wind blows).\n"
            "  - Degrees of temperature: 'Η θερμοκρασία είναι 28 βαθμοί.'\n"
            "• Expressing Likes & Preferences ('Μου αρέσει / Μου αρέσουν'):\n"
            "  - 'Μου αρέσει' + Singular noun or verb: 'Μου αρέσει η θάλασσα' / 'Μου αρέσει να ταξιδεύω'.\n"
            "  - 'Μου αρέσουν' + Plural noun: 'Μου αρέσουν τα νησιά'.\n"
            "  - Verb 'προτιμάω / προτιμώ': 'Προτιμώ τη θάλασσα από το βουνό.'\n"
            "• Weak Direct-Object Clitic Pronouns (Αιτιατική Προσωπικών Αντωνυμιών):\n"
            "  - Singular: με (me), σε (you), τον (him/it), την (her/it), το (it).\n"
            "  - Plural: μας (us), σας (you all), τους (them masc), τις (them fem), τα (them neut).\n"
            "  - Syntactic position: Placed immediately BEFORE the conjugated verb in active indicative:\n"
            "    * 'Τον βλέπω' (I see him).\n"
            "    * 'Τις ξέρεις;' (Do you know them?).\n"
            "    * 'Δεν το θέλω' (I don't want it)."
        ),
    },
}


def build_card_entry(c, existing_entry=None):
    audio_file = c.get("audio") or (existing_entry.get("audio") if existing_entry else None)
    
    if audio_file and (AUDIO_DIR / audio_file).exists():
        status = "verified"
    else:
        status = existing_entry.get("status", "pending_tts") if existing_entry else "pending_tts"
        if status == "verified" and not (audio_file and (AUDIO_DIR / audio_file).exists()):
            status = "pending_tts"

    entry = {
        "id": c["id"],
        "greek": c["front"],
        "phonetic_hint": c.get("phonetic_hint", "") or (existing_entry.get("phonetic_hint", "") if existing_entry else ""),
        "english": c["back_primary"],
        "notes": c.get("notes_or_mnemonics", ""),
        "gender_or_pos": c.get("grammatical_info", {}).get("part_of_speech", "phrase"),
        "audio": audio_file,
        "status": status,
        "example_el": c.get("example_el", ""),
        "example_en": c.get("example_en", ""),
        "grammatical_info": c.get("grammatical_info", {}),
        "keg_communicative_function": c.get("keg_communicative_function", ""),
    }
    return entry


def sync_all():
    print("=" * 70)
    print("Curriculum Sync: Aggregating JSON Batches into YAML SSOT")
    print("=" * 70)

    # Find all batch json files
    json_files = sorted(glob.glob(str(CONTENT_DIR / "keg_a1_units_*.json")))
    print(f"Found {len(json_files)} batch JSON files: {[Path(p).name for p in json_files]}")

    all_cards_by_unit = {}
    for jf in json_files:
        with open(jf, "r", encoding="utf-8") as f:
            batch = json.load(f)
            for card in batch:
                u_num = card["unit_number"]
                all_cards_by_unit.setdefault(u_num, []).append(card)

    total_cards = sum(len(cards) for cards in all_cards_by_unit.values())
    print(f"Total aggregated cards: {total_cards} across {len(all_cards_by_unit)} units.")

    # Manifest units container
    manifest_units = []

    for u_num in sorted(all_cards_by_unit.keys()):
        cards = all_cards_by_unit[u_num]
        unit_id = f"unit-{u_num:02d}"
        lesson_id = "lesson-01"
        rel_file = f"{unit_id}/{lesson_id}.yaml"
        yaml_file = CONTENT_DIR / rel_file
        yaml_file.parent.mkdir(parents=True, exist_ok=True)

        meta = UNIT_METADATA.get(u_num, {
            "title": cards[0].get("unit_theme", f"Unit {u_num}"),
            "description": f"CEFR A1 Unit {u_num} curriculum.",
            "lesson_notes": "",
        })

        # Load existing YAML if exists to preserve existing lesson_status/notes
        existing_data = {}
        existing_entries_map = {}
        if yaml_file.exists():
            with open(yaml_file, "r", encoding="utf-8") as f:
                existing_data = yaml.safe_load(f) or {}
                for e in existing_data.get("entries", []):
                    existing_entries_map[e["id"]] = e

        lesson_entries = [
            build_card_entry(c, existing_entries_map.get(c["id"]))
            for c in cards
        ]

        verified_in_unit = sum(1 for e in lesson_entries if e["status"] == "verified")

        lesson_data = {
            "unit_id": unit_id,
            "lesson_id": lesson_id,
            "title": meta["title"],
            "description": meta["description"],
            "lesson_status": existing_data.get("lesson_status", "not_started"),
            "lesson_notes": existing_data.get("lesson_notes") or meta["lesson_notes"],
            "entries": lesson_entries,
        }

        with open(yaml_file, "w", encoding="utf-8") as f:
            yaml.dump(lesson_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

        print(f"-> Unit {u_num}: {len(lesson_entries)} cards written to {rel_file} ({verified_in_unit} verified)")

        manifest_units.append({
            "id": unit_id,
            "title": meta["title"],
            "order": u_num,
            "lessons": [
                {
                    "id": lesson_id,
                    "file": rel_file,
                    "title": meta["title"],
                }
            ],
        })

    # Write Manifest
    manifest_data = {
        "deck_title": "Modern Greek Mastery (CEFR A1)",
        "source_language": "en",
        "target_language": "el",
        "created_at": "2026-10-25",
        "units": manifest_units,
    }

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)

    print("-" * 70)
    print(f"Manifest updated at {MANIFEST_PATH.name} with {len(manifest_units)} units.")
    print("Curriculum successfully synced to YAML Single Source of Truth!")


if __name__ == "__main__":
    sync_all()

# -*- coding: utf-8 -*-
"""
Script to create Unit 101 from Klik A1 (Pages 25-41):
Εισαγωγική Ενότητα - Ήχοι, Γράμματα & Πρώτες Λέξεις
Strictly conforming to docs/LESSON_CREATION_GUIDE.md and the klik-a1-deck-builder skill.
"""
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
UNIT_DIR = CONTENT_DIR / "unit-101"
UNIT_DIR.mkdir(parents=True, exist_ok=True)
YAML_PATH = UNIT_DIR / "lesson-01.yaml"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

cards_u101 = [
    # --- Page 25: First Words & Alphabet Foundations ---
    {
        "id": "A1-U101-001",
        "greek": "το αεροπλάνο",
        "phonetic_hint": "",
        "english": "airplane / plane",
        "notes": "Klik A1 p. 25. Neuter noun in -ο with plural in -α. Compound word: αέρας (air) + πλάνο.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το αεροπλάνο φτάνει στην Αθήνα στις πέντε.",
        "example_en": "The airplane arrives in Athens at five o'clock.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα αεροπλάνα",
            "accusative_singular": "το αεροπλάνο"
        },
        "keg_communicative_function": "Identifying modes of transport and travel vocabulary"
    },
    {
        "id": "A1-U101-002",
        "greek": "το βάζο",
        "phonetic_hint": "",
        "english": "vase",
        "notes": "Klik A1 p. 25. Common household neuter noun. Practicing voiced fricative [v] (β).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Έχει όμορφα λουλούδια στο βάζο.",
        "example_en": "There are beautiful flowers in the vase.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα βάζα",
            "accusative_singular": "το βάζο"
        },
        "keg_communicative_function": "Describing home decor and everyday objects"
    },
    {
        "id": "A1-U101-003",
        "greek": "η βάρκα",
        "phonetic_hint": "",
        "english": "small boat / rowboat",
        "notes": "Klik A1 p. 25. Feminine noun in -α with stress on the first syllable.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η βάρκα είναι στο μικρό λιμάνι.",
        "example_en": "The boat is in the small harbor.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι βάρκες",
            "accusative_singular": "τη βάρκα"
        },
        "keg_communicative_function": "Describing sea transport and maritime settings"
    },
    {
        "id": "A1-U101-004",
        "greek": "το ζάρι",
        "phonetic_hint": "",
        "english": "die / dice",
        "notes": "Klik A1 p. 25. Neuter noun in -ι with plural in -ια. Practicing voiced dental fricative [z] (ζ).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ρίχνω το ζάρι στο παιχνίδι.",
        "example_en": "I roll the die in the game.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ζάρια",
            "accusative_singular": "το ζάρι"
        },
        "keg_communicative_function": "Discussing board games and recreation"
    },
    {
        "id": "A1-U101-005",
        "greek": "το λεμόνι",
        "phonetic_hint": "",
        "english": "lemon",
        "notes": "Klik A1 p. 25. Neuter noun in -ι with plural in -ια. Core staple fruit in Greek cooking.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Θέλω λίγο λεμόνι στη σαλάτα.",
        "example_en": "I want a little lemon on the salad.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα λεμόνια",
            "accusative_singular": "το λεμόνι"
        },
        "keg_communicative_function": "Ordering and describing fresh foods"
    },
    {
        "id": "A1-U101-006",
        "greek": "το μαγαζί",
        "phonetic_hint": "",
        "english": "shop / store",
        "notes": "Klik A1 p. 25. Neuter noun in -ί with oxytone stress (plural: τα μαγαζιά).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το μαγαζί είναι ανοιχτό σήμερα.",
        "example_en": "The store is open today.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μαγαζιά",
            "accusative_singular": "το μαγαζί"
        },
        "keg_communicative_function": "Navigating commercial shops and town facilities"
    },
    {
        "id": "A1-U101-007",
        "greek": "η μπίρα",
        "phonetic_hint": "",
        "english": "beer",
        "notes": "Klik A1 p. 25. Also spelled μπύρα. Practicing the initial voiced stop [b] (μπ).",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μία κρύα μπίρα, παρακαλώ.",
        "example_en": "One cold beer, please.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι μπίρες",
            "accusative_singular": "την μπίρα"
        },
        "keg_communicative_function": "Ordering drinks at a cafe or taverna"
    },
    {
        "id": "A1-U101-008",
        "greek": "η κιθάρα",
        "phonetic_hint": "",
        "english": "guitar",
        "notes": "Klik A1 p. 25. Feminine noun in -α with stress on the penult.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο Νίκος παίζει κιθάρα πολύ καλά.",
        "example_en": "Nikos plays guitar very well.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι κιθάρες",
            "accusative_singular": "την κιθάρα"
        },
        "keg_communicative_function": "Discussing hobbies and musical instruments"
    },
    {
        "id": "A1-U101-009",
        "greek": "ο καναπές",
        "phonetic_hint": "",
        "english": "sofa / couch",
        "notes": "Klik A1 p. 25. Masculine noun in -ές with plural adding -δες (οι καναπέδες).",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο καναπές στο σαλόνι είναι άνετος.",
        "example_en": "The sofa in the living room is comfortable.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι καναπέδες",
            "accusative_singular": "τον καναπέ"
        },
        "keg_communicative_function": "Describing home furniture"
    },
    {
        "id": "A1-U101-010",
        "greek": "το κασκόλ",
        "phonetic_hint": "",
        "english": "scarf",
        "notes": "Klik A1 p. 25. Neuter indeclinable loanword (το κασκόλ, τα κασκόλ).",
        "gender_or_pos": "noun (neuter indeclinable)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Φοράω ζεστό κασκόλ τον χειμώνα.",
        "example_en": "I wear a warm scarf in the winter.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter indeclinable)",
            "plural": "τα κασκόλ",
            "accusative_singular": "το κασκόλ"
        },
        "keg_communicative_function": "Describing clothing and winter accessories"
    },
    {
        "id": "A1-U101-011",
        "greek": "το ντουλάπι",
        "phonetic_hint": "",
        "english": "cupboard / cabinet",
        "notes": "Klik A1 p. 25. Practicing the initial voiced dental stop [d] (ντ).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τα ποτήρια είναι μέσα στο ντουλάπι.",
        "example_en": "The glasses are inside the cupboard.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ντουλάπια",
            "accusative_singular": "το ντουλάπι"
        },
        "keg_communicative_function": "Locating objects in the kitchen or house"
    },
    {
        "id": "A1-U101-012",
        "greek": "το πιάνο",
        "phonetic_hint": "",
        "english": "piano",
        "notes": "Klik A1 p. 25. Neuter noun in -ο with plural in -α.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η Μαρία μαθαίνει πιάνο.",
        "example_en": "Maria is learning piano.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πιάνα",
            "accusative_singular": "το πιάνο"
        },
        "keg_communicative_function": "Talking about musical skills and hobbies"
    },
    {
        "id": "A1-U101-013",
        "greek": "το θέατρο",
        "phonetic_hint": "",
        "english": "theater / theatre",
        "notes": "Klik A1 p. 25. Neuter noun in -ο with initial voiceless dental fricative [θ].",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πάμε στο θέατρο απόψε;",
        "example_en": "Shall we go to the theater tonight?",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα θέατρα",
            "accusative_singular": "το θέατρο"
        },
        "keg_communicative_function": "Suggesting cultural outings and leisure activities"
    },
    {
        "id": "A1-U101-014",
        "greek": "η τσάντα",
        "phonetic_hint": "",
        "english": "bag / handbag",
        "notes": "Klik A1 p. 25. Practicing the affricate [ts] (τσ). Feminine in -α.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η τσάντα μου είναι πάνω στο τραπέζι.",
        "example_en": "My bag is on the table.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι τσάντες",
            "accusative_singular": "την τσάντα"
        },
        "keg_communicative_function": "Identifying personal belongings"
    },
    {
        "id": "A1-U101-015",
        "greek": "ο μανάβης",
        "phonetic_hint": "",
        "english": "greengrocer",
        "notes": "Klik A1 p. 25. Masculine profession noun in -ης (plural: οι μανάβηδες).",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αγοράζω φρούτα από τον μανάβη της γειτονιάς.",
        "example_en": "I buy fruit from the neighborhood greengrocer.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι μανάβηδες",
            "accusative_singular": "τον μανάβη"
        },
        "keg_communicative_function": "Identifying local vendors and professions"
    },

    # --- Page 26: Uppercase/Lowercase & Everyday Vocabulary ---
    {
        "id": "A1-U101-016",
        "greek": "το δελφίνι",
        "phonetic_hint": "",
        "english": "dolphin",
        "notes": "Klik A1 p. 26. Neuter noun in -ι with plural in -ια. Practicing [δ] and [f] (φ).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Είδαμε ένα δελφίνι στο Αιγαίο.",
        "example_en": "We saw a dolphin in the Aegean.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα δελφίνια",
            "accusative_singular": "το δελφίνι"
        },
        "keg_communicative_function": "Describing wildlife and sea animals"
    },
    {
        "id": "A1-U101-017",
        "greek": "η ετικέτα",
        "phonetic_hint": "",
        "english": "label / price tag",
        "notes": "Klik A1 p. 26. Feminine noun in -α with stress on the penult.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κοίταξε την τιμή στην ετικέτα.",
        "example_en": "Check the price on the label.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ετικέτες",
            "accusative_singular": "την ετικέτα"
        },
        "keg_communicative_function": "Checking product information while shopping"
    },
    {
        "id": "A1-U101-018",
        "greek": "η σαλάτα",
        "phonetic_hint": "",
        "english": "salad",
        "notes": "Klik A1 p. 26. Core food vocabulary. Greek salad is 'η χωριάτικη σαλάτα'.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Παραγγέλνουμε μια ελληνική σαλάτα.",
        "example_en": "We are ordering a Greek salad.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι σαλάτες",
            "accusative_singular": "τη σαλάτα"
        },
        "keg_communicative_function": "Ordering traditional dishes at restaurants"
    },
    {
        "id": "A1-U101-019",
        "greek": "το ταξί",
        "phonetic_hint": "",
        "english": "taxi / cab",
        "notes": "Klik A1 p. 26. Neuter indeclinable loanword with oxytone stress (ταξί).",
        "gender_or_pos": "noun (neuter indeclinable)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Παίρνουμε ταξί για το αεροδρόμιο.",
        "example_en": "We take a taxi to the airport.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter indeclinable)",
            "plural": "τα ταξί",
            "accusative_singular": "το ταξί"
        },
        "keg_communicative_function": "Arranging transportation around the city"
    },
    {
        "id": "A1-U101-020",
        "greek": "το τρένο",
        "phonetic_hint": "",
        "english": "train",
        "notes": "Klik A1 p. 26. Neuter noun in -ο with plural in -α. Also spelled τραίνο.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το τρένο φεύγει στις δέκα το πρωί.",
        "example_en": "The train leaves at ten in the morning.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα τρένα",
            "accusative_singular": "το τρένο"
        },
        "keg_communicative_function": "Talking about train travel and schedules"
    },
    {
        "id": "A1-U101-021",
        "greek": "η φωτογραφία",
        "phonetic_hint": "",
        "english": "photograph / photo",
        "notes": "Klik A1 p. 26. Feminine noun in -ία with plural in -ίες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βγάζω μια φωτογραφία στο μουσείο.",
        "example_en": "I take a photograph at the museum.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι φωτογραφίες",
            "accusative_singular": "τη φωτογραφία"
        },
        "keg_communicative_function": "Talking about sightseeing and memories"
    },
    {
        "id": "A1-U101-022",
        "greek": "το βερίκοκο",
        "phonetic_hint": "",
        "english": "apricot",
        "notes": "Klik A1 p. 26. Neuter proparoxytone in -ο with stress shifting in genitive: του βερίκοκου.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το καλοκαίρι τρώμε γλυκά βερίκοκα.",
        "example_en": "In the summer we eat sweet apricots.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα βερίκοκα",
            "accusative_singular": "το βερίκοκο"
        },
        "keg_communicative_function": "Naming seasonal fruits"
    },
    {
        "id": "A1-U101-023",
        "greek": "το ασανσέρ",
        "phonetic_hint": "",
        "english": "elevator / lift",
        "notes": "Klik A1 p. 26. Neuter indeclinable French loanword.",
        "gender_or_pos": "noun (neuter indeclinable)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το ασανσέρ ανεβαίνει στον πέμπτο όροφο.",
        "example_en": "The elevator goes up to the fifth floor.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter indeclinable)",
            "plural": "τα ασανσέρ",
            "accusative_singular": "το ασανσέρ"
        },
        "keg_communicative_function": "Navigating buildings and hotels"
    },
    {
        "id": "A1-U101-024",
        "greek": "η αφίσα",
        "phonetic_hint": "",
        "english": "poster",
        "notes": "Klik A1 p. 26. Feminine noun in -α with stress on the penult.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Έχει μια αφίσα της συναυλίας στον τοίχο.",
        "example_en": "There is a concert poster on the wall.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι αφίσες",
            "accusative_singular": "την αφίσα"
        },
        "keg_communicative_function": "Identifying announcements and cultural posters"
    },
    {
        "id": "A1-U101-025",
        "greek": "το κρουασάν",
        "phonetic_hint": "",
        "english": "croissant",
        "notes": "Klik A1 p. 26. Neuter indeclinable bakery item.",
        "gender_or_pos": "noun (neuter indeclinable)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Θέλω έναν καφέ και ένα κρουασάν σοκολάτας.",
        "example_en": "I want a coffee and a chocolate croissant.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter indeclinable)",
            "plural": "τα κρουασάν",
            "accusative_singular": "το κρουασάν"
        },
        "keg_communicative_function": "Ordering breakfast items at bakeries and cafes"
    },
    {
        "id": "A1-U101-026",
        "greek": "το μαγιό",
        "phonetic_hint": "",
        "english": "swimsuit / bathing suit",
        "notes": "Klik A1 p. 26. Neuter indeclinable loanword (το μαγιό, τα μαγιό).",
        "gender_or_pos": "noun (neuter indeclinable)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βάζω το μαγιό μου στην τσάντα για τη θάλασσα.",
        "example_en": "I put my swimsuit in the bag for the beach.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter indeclinable)",
            "plural": "τα μαγιό",
            "accusative_singular": "το μαγιό"
        },
        "keg_communicative_function": "Talking about summer holidays and beachwear"
    },

    # --- Page 27: Phonemes [α] & [ε] - Foods, Hobbies & Pastimes ---
    {
        "id": "A1-U101-027",
        "greek": "η ντομάτα",
        "phonetic_hint": "",
        "english": "tomato",
        "notes": "Klik A1 p. 27. Practicing [d] (ντ) and [α]. Essential Greek grocery staple.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αγοράζω ένα κιλό κόκκινες ντομάτες.",
        "example_en": "I buy one kilo of red tomatoes.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ντομάτες",
            "accusative_singular": "την ντομάτα"
        },
        "keg_communicative_function": "Buying groceries at the market"
    },
    {
        "id": "A1-U101-028",
        "greek": "η ελιά",
        "phonetic_hint": "",
        "english": "olive / olive tree",
        "notes": "Klik A1 p. 27. Feminine oxytone in -ιά (plural: οι ελιές). Symbol of Greece.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μου αρέσουν πολύ οι μαύρες ελιές Καλαμάτας.",
        "example_en": "I really like black Kalamata olives.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ελιές",
            "accusative_singular": "την ελιά"
        },
        "keg_communicative_function": "Discussing traditional Greek foods and appetizers"
    },
    {
        "id": "A1-U101-029",
        "greek": "το κρεμμύδι",
        "phonetic_hint": "",
        "english": "onion",
        "notes": "Klik A1 p. 27. Neuter noun in -ι with plural in -ια. Double μμ pronounced as single [m].",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βάζουμε ψιλοκομμένο κρεμμύδι στη σαλάτα.",
        "example_en": "We put finely chopped onion in the salad.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κρεμμύδια",
            "accusative_singular": "το κρεμμύδι"
        },
        "keg_communicative_function": "Describing cooking ingredients"
    },
    {
        "id": "A1-U101-030",
        "greek": "το αγγούρι",
        "phonetic_hint": "",
        "english": "cucumber",
        "notes": "Klik A1 p. 27. Practicing the voiced velar nasal combination γγ [ŋg]/[g].",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κόβω το φρέσκο αγγούρι σε φέτες.",
        "example_en": "I slice the fresh cucumber into pieces.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα αγγούρια",
            "accusative_singular": "το αγγούρι"
        },
        "keg_communicative_function": "Describing fresh produce"
    },
    {
        "id": "A1-U101-031",
        "greek": "το λάδι",
        "phonetic_hint": "",
        "english": "olive oil / oil",
        "notes": "Klik A1 p. 27 (corrected from OCR 'γάδι'). Essential Greek culinary foundation.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το ελληνικό παρθένο ελαιόλαδο είναι εξαιρετικό.",
        "example_en": "Greek virgin olive oil is outstanding.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα λάδια",
            "accusative_singular": "το λάδι"
        },
        "keg_communicative_function": "Describing culinary staples"
    },
    {
        "id": "A1-U101-032",
        "greek": "το τυρί",
        "phonetic_hint": "",
        "english": "cheese",
        "notes": "Klik A1 p. 27. Oxytone neuter in -ί (plural: τα τυριά).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η φέτα είναι το πιο διάσημο ελληνικό τυρί.",
        "example_en": "Feta is the most famous Greek cheese.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα τυριά",
            "accusative_singular": "το τυρί"
        },
        "keg_communicative_function": "Ordering dairy and cheeses"
    },
    {
        "id": "A1-U101-033",
        "greek": "η πιπεριά",
        "phonetic_hint": "",
        "english": "pepper / bell pepper",
        "notes": "Klik A1 p. 27. Oxytone feminine in -ιά (plural: οι πιπεριές).",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Προσθέτω μια πράσινη πιπεριά στο φαγητό.",
        "example_en": "I add a green bell pepper to the dish.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πιπεριές",
            "accusative_singular": "την πιπεριά"
        },
        "keg_communicative_function": "Selecting produce at the grocery store"
    },
    {
        "id": "A1-U101-034",
        "greek": "το λάχανο",
        "phonetic_hint": "",
        "english": "cabbage",
        "notes": "Klik A1 p. 27. Neuter proparoxytone in -ο with stress on the antepenult.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Φτιάχνουμε σαλάτα με λάχανο και καρότο.",
        "example_en": "We make a salad with cabbage and carrot.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα λάχανα",
            "accusative_singular": "το λάχανο"
        },
        "keg_communicative_function": "Describing vegetables and winter salads"
    },
    {
        "id": "A1-U101-035",
        "greek": "το παιχνίδι",
        "phonetic_hint": "",
        "english": "game / toy",
        "notes": "Klik A1 p. 27. Practicing digraph αι [e] and neuter ending -ίδι.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τα παιδιά παίζουν ένα διασκεδαστικό παιχνίδι.",
        "example_en": "The children are playing an entertaining game.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα παιχνίδια",
            "accusative_singular": "το παιχνίδι"
        },
        "keg_communicative_function": "Discussing leisure, games, and play"
    },
    {
        "id": "A1-U101-036",
        "greek": "το διάβασμα",
        "phonetic_hint": "",
        "english": "reading / studying",
        "notes": "Klik A1 p. 27. Neuter noun in -μα (plural: τα διαβάσματα). Verbal noun from διαβάζω.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Έχω πολύ διάβασμα για το μάθημα των ελληνικών.",
        "example_en": "I have a lot of studying for the Greek lesson.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα διαβάσματα",
            "accusative_singular": "το διάβασμα"
        },
        "keg_communicative_function": "Talking about daily study habits and education"
    },
    {
        "id": "A1-U101-037",
        "greek": "η ταινία",
        "phonetic_hint": "",
        "english": "movie / film",
        "notes": "Klik A1 p. 27. Feminine in -ία with digraph αι [e].",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βλέπουμε μια ενδιαφέρουσα ταινία στον κινηματογράφο.",
        "example_en": "We are watching an interesting movie at the cinema.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ταινίες",
            "accusative_singular": "την ταινία"
        },
        "keg_communicative_function": "Discussing entertainment and films"
    },
    {
        "id": "A1-U101-038",
        "greek": "το ποδόσφαιρο",
        "phonetic_hint": "",
        "english": "soccer / football",
        "notes": "Klik A1 p. 27. Compound noun: πόδι (foot) + σφαίρα (sphere/ball). Digraph αι [e].",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο γιος μου παίζει ποδόσφαιρο κάθε Σάββατο.",
        "example_en": "My son plays soccer every Saturday.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ποδόσφαιρα",
            "accusative_singular": "το ποδόσφαιρο"
        },
        "keg_communicative_function": "Talking about sports and team games"
    },
    {
        "id": "A1-U101-039",
        "greek": "η βόλτα",
        "phonetic_hint": "",
        "english": "walk / stroll",
        "notes": "Klik A1 p. 27. Essential Greek social activity: 'πάω βόλτα' (I go for a stroll).",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πάμε μια βόλτα στην παραλία;",
        "example_en": "Shall we go for a walk along the beach?",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι βόλτες",
            "accusative_singular": "τη βόλτα"
        },
        "keg_communicative_function": "Suggesting recreational walks and outdoor meetups"
    },
    {
        "id": "A1-U101-040",
        "greek": "η τηλεόραση",
        "phonetic_hint": "",
        "english": "television / TV",
        "notes": "Klik A1 p. 27. Feminine noun in -ση with plural in -σεις (οι τηλεοράσεις).",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βλέπω τις ειδήσεις στην τηλεόραση.",
        "example_en": "I watch the news on television.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι τηλεοράσεις",
            "accusative_singular": "την τηλεόραση"
        },
        "keg_communicative_function": "Describing home media and daily habits"
    },
    {
        "id": "A1-U101-041",
        "greek": "το ταξίδι",
        "phonetic_hint": "",
        "english": "trip / journey / travel",
        "notes": "Klik A1 p. 27. Neuter noun in -ι with plural in -ια. Related to ταξιδεύω.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Καλό ταξίδι και καλή διασκέδαση!",
        "example_en": "Have a good trip and have fun!",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ταξίδια",
            "accusative_singular": "το ταξίδι"
        },
        "keg_communicative_function": "Wishing someone a good trip and discussing travel"
    },

    # --- Page 28: Sounds [ι] & [ο] - Days, Seasons & Food ---
    {
        "id": "A1-U101-042",
        "greek": "η Δευτέρα",
        "phonetic_hint": "",
        "english": "Monday",
        "notes": "Klik A1 p. 28. Diphthong ευ pronounced [ev] before dental τ [t].",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τη Δευτέρα αρχίζει η νέα σχολική χρονιά.",
        "example_en": "On Monday the new school year begins.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι Δευτέρες",
            "accusative_singular": "τη Δευτέρα"
        },
        "keg_communicative_function": "Specifying days and scheduling weekly routines"
    },
    {
        "id": "A1-U101-043",
        "greek": "το φθινόπωρο",
        "phonetic_hint": "",
        "english": "autumn / fall",
        "notes": "Klik A1 p. 28. Practicing consonant cluster φθ [fθ] and letter combinations for [i] (ι, οι).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το φθινόπωρο τα φύλλα των δέντρων πέφτουν.",
        "example_en": "In autumn the leaves of the trees fall.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα φθινόπωρα",
            "accusative_singular": "το φθινόπωρο"
        },
        "keg_communicative_function": "Talking about the four seasons and weather"
    },
    {
        "id": "A1-U101-044",
        "greek": "το Σάββατο",
        "phonetic_hint": "",
        "english": "Saturday",
        "notes": "Klik A1 p. 28. Neuter noun in -ο with proparoxytone stress (τα Σάββατα).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το Σάββατο πηγαίνουμε για ψώνια στη λαϊκή.",
        "example_en": "On Saturday we go shopping at the farmers' market.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Σάββατα",
            "accusative_singular": "το Σάββατο"
        },
        "keg_communicative_function": "Arranging weekend appointments"
    },
    {
        "id": "A1-U101-045",
        "greek": "ο χειμώνας",
        "phonetic_hint": "",
        "english": "winter",
        "notes": "Klik A1 p. 28. Digraph ει [i]. Masculine noun in -ας (οι χειμώνες).",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τον χειμώνα κάνει κρύο και χιονίζει στα βουνά.",
        "example_en": "In winter it is cold and snows in the mountains.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι χειμώνες",
            "accusative_singular": "τον χειμώνα"
        },
        "keg_communicative_function": "Discussing winter climate and seasonal changes"
    },
    {
        "id": "A1-U101-046",
        "greek": "το καλοκαίρι",
        "phonetic_hint": "",
        "english": "summer",
        "notes": "Klik A1 p. 28. Digraph αι [e]. Neuter in -ι with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το καλοκαίρι πάμε διακοπές στα νησιά.",
        "example_en": "In summer we go on vacation to the islands.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα καλοκαίρια",
            "accusative_singular": "το καλοκαίρι"
        },
        "keg_communicative_function": "Talking about summer holidays and beach activities"
    },
    {
        "id": "A1-U101-047",
        "greek": "η άνοιξη",
        "phonetic_hint": "",
        "english": "spring",
        "notes": "Klik A1 p. 28. Feminine noun with digraph οι [i] and proparoxytone stress.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Την άνοιξη ο καιρός είναι ζεστός και ανθίζουν τα λουλούδια.",
        "example_en": "In spring the weather is warm and the flowers bloom.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ανοίξεις",
            "accusative_singular": "την άνοιξη"
        },
        "keg_communicative_function": "Describing springtime weather"
    },
    {
        "id": "A1-U101-048",
        "greek": "το γάλα",
        "phonetic_hint": "",
        "english": "milk",
        "notes": "Klik A1 p. 28. Irregular neuter noun: το γάλα, του γάλακτος, τα γάλατα.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πίνω ένα ποτήρι γάλα κάθε πρωί.",
        "example_en": "I drink a glass of milk every morning.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα γάλατα",
            "accusative_singular": "το γάλα"
        },
        "keg_communicative_function": "Ordering breakfast beverages"
    },
    {
        "id": "A1-U101-049",
        "greek": "το παγωτό",
        "phonetic_hint": "",
        "english": "ice cream",
        "notes": "Klik A1 p. 28. Oxytone neuter in -ό (plural: τα παγωτά).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τα παιδιά θέλουν παγωτό σοκολάτα.",
        "example_en": "The children want chocolate ice cream.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα παγωτά",
            "accusative_singular": "το παγωτό"
        },
        "keg_communicative_function": "Ordering desserts and snacks"
    },
    {
        "id": "A1-U101-050",
        "greek": "το μέλι",
        "phonetic_hint": "",
        "english": "honey",
        "notes": "Klik A1 p. 28. Neuter noun in -ι. Famous Greek thyme honey is 'μέλι θυμαρίσιο'.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τρώω γιαούρτι με μέλι και καρύδια.",
        "example_en": "I eat yogurt with honey and walnuts.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μέλια",
            "accusative_singular": "το μέλι"
        },
        "keg_communicative_function": "Describing traditional breakfast sweets"
    },
    {
        "id": "A1-U101-051",
        "greek": "το νερό",
        "phonetic_hint": "",
        "english": "water",
        "notes": "Klik A1 p. 28. Essential noun: 'ένα ποτήρι νερό' (a glass of water).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μπορώ να έχω ένα μπουκάλι νερό, παρακαλώ;",
        "example_en": "May I have a bottle of water, please?",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα νερά",
            "accusative_singular": "το νερό"
        },
        "keg_communicative_function": "Requesting drinking water at any venue"
    },
    {
        "id": "A1-U101-052",
        "greek": "το ψωμί",
        "phonetic_hint": "",
        "english": "bread",
        "notes": "Klik A1 p. 28. Oxytone neuter in -ί (plural: τα ψωμιά).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αγοράζουμε φρέσκο ψωμί από τον φούρνο.",
        "example_en": "We buy fresh bread from the bakery.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ψωμιά",
            "accusative_singular": "το ψωμί"
        },
        "keg_communicative_function": "Buying bread and ordering table settings"
    },
    {
        "id": "A1-U101-053",
        "greek": "το μήλο",
        "phonetic_hint": "",
        "english": "apple",
        "notes": "Klik A1 p. 28. Neuter noun in -ο with plural in -α.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ένα μήλο την ημέρα τον γιατρό τον κάνει πέρα.",
        "example_en": "An apple a day keeps the doctor away.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μήλα",
            "accusative_singular": "το μήλο"
        },
        "keg_communicative_function": "Naming common fruits"
    },
    {
        "id": "A1-U101-054",
        "greek": "το πορτοκάλι",
        "phonetic_hint": "",
        "english": "orange",
        "notes": "Klik A1 p. 28. Neuter noun in -ι with plural in -ια. Related to η πορτοκαλάδα.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πίνω φρέσκο χυμό πορτοκάλι κάθε πρωί.",
        "example_en": "I drink fresh orange juice every morning.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πορτοκάλια",
            "accusative_singular": "το πορτοκάλι"
        },
        "keg_communicative_function": "Ordering fresh juices and fruit"
    },
    {
        "id": "A1-U101-055",
        "greek": "τα μακαρόνια",
        "phonetic_hint": "",
        "english": "pasta / spaghetti",
        "notes": "Klik A1 p. 28. Usually encountered in the plural: τα μακαρόνια.",
        "gender_or_pos": "noun (neuter plural)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μαγειρεύουμε μακαρόνια με σάλτσα ντομάτας.",
        "example_en": "We are cooking pasta with tomato sauce.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter plural)",
            "plural": "τα μακαρόνια",
            "accusative_singular": "τα μακαρόνια"
        },
        "keg_communicative_function": "Ordering staple main courses"
    },

    # --- Page 29 & 30: Digraphs [ου], [αυ/ευ], Dialytika ϊ/ϋ, Consonant [β] ---
    {
        "id": "A1-U101-056",
        "greek": "το ούζο",
        "phonetic_hint": "",
        "english": "ouzo",
        "notes": "Klik A1 p. 29. Practicing digraph ου [u]. Iconic Greek aniseed spirit.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πίνουμε ούζο με μεζέ δίπλα στο κύμα.",
        "example_en": "We drink ouzo with meze by the waves.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ούζα",
            "accusative_singular": "το ούζο"
        },
        "keg_communicative_function": "Ordering traditional beverages and appetizers"
    },
    {
        "id": "A1-U101-057",
        "greek": "το σπανάκι",
        "phonetic_hint": "",
        "english": "spinach",
        "notes": "Klik A1 p. 29. Key ingredient in traditional σπανακόπιτα.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αγοράζω φρέσκο σπανάκι για την πίτα.",
        "example_en": "I buy fresh spinach for the pie.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα σπανάκια",
            "accusative_singular": "το σπανάκι"
        },
        "keg_communicative_function": "Buying greens and vegetables"
    },
    {
        "id": "A1-U101-058",
        "greek": "το καρπούζι",
        "phonetic_hint": "",
        "english": "watermelon",
        "notes": "Klik A1 p. 29. Digraph ου [u]. Quintessential Greek summer fruit.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το δροσερό καρπούζι είναι υπέροχο το καλοκαίρι.",
        "example_en": "Chilled watermelon is wonderful in summer.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα καρπούζια",
            "accusative_singular": "το καρπούζι"
        },
        "keg_communicative_function": "Ordering seasonal desserts"
    },
    {
        "id": "A1-U101-059",
        "greek": "το φρούτο",
        "phonetic_hint": "",
        "english": "fruit",
        "notes": "Klik A1 p. 29. Digraph ου [u]. Plural: τα φρούτα.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τρώω φρέσκα φρούτα εποχής κάθε μέρα.",
        "example_en": "I eat fresh seasonal fruit every day.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα φρούτα",
            "accusative_singular": "το φρούτο"
        },
        "keg_communicative_function": "Talking about healthy diet and fruits"
    },
    {
        "id": "A1-U101-060",
        "greek": "ο καιρός",
        "phonetic_hint": "",
        "english": "weather / time",
        "notes": "Klik A1 p. 30. Digraph αι [e]. 'Τι καιρό κάνει;' (What is the weather like?).",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Σήμερα ο καιρός είναι πολύ ζεστός και ηλιόλουστος.",
        "example_en": "Today the weather is very warm and sunny.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι καιροί",
            "accusative_singular": "τον καιρό"
        },
        "keg_communicative_function": "Inquiring about and describing the weather"
    },
    {
        "id": "A1-U101-061",
        "greek": "το προϊόν",
        "phonetic_hint": "",
        "english": "product",
        "notes": "Klik A1 p. 30. Demonstrates dialytika (ϊ): separates vowels ο and ϊ, avoiding diphthong.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αυτό είναι ένα παραδοσιακό ελληνικό προϊόν.",
        "example_en": "This is a traditional Greek product.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα προϊόντα",
            "accusative_singular": "το προϊόν"
        },
        "keg_communicative_function": "Discussing local products and commerce"
    },
    {
        "id": "A1-U101-062",
        "greek": "το καΐκι",
        "phonetic_hint": "",
        "english": "traditional boat / caique",
        "notes": "Klik A1 p. 30. Dialytika with tonos (ΐ): separates vowels and carries word stress.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το ξύλινο καΐκι φεύγει για το νησάκι.",
        "example_en": "The wooden caique is departing for the small islet.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα καΐκια",
            "accusative_singular": "το καΐκι"
        },
        "keg_communicative_function": "Describing traditional island boats"
    },

    # --- Page 31 & 32: Sounds [b] (μπ), [p] (π), [f] (φ), [θ] (θ) - Clothing & Details ---
    {
        "id": "A1-U101-063",
        "greek": "το φόρεμα",
        "phonetic_hint": "",
        "english": "dress",
        "notes": "Klik A1 p. 31. Neuter in -μα with plural adding -τα: τα φορέματα.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η Άννα φοράει ένα κομψό καλοκαιρινό φόρεμα.",
        "example_en": "Anna is wearing an elegant summer dress.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα φορέματα",
            "accusative_singular": "το φόρεμα"
        },
        "keg_communicative_function": "Describing outfits and clothing"
    },
    {
        "id": "A1-U101-064",
        "greek": "η μπλούζα",
        "phonetic_hint": "",
        "english": "blouse / top / t-shirt",
        "notes": "Klik A1 p. 31. Practicing voiced bilabial stop [b] (μπ).",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αυτή η άσπρη μπλούζα σου πάει πολύ.",
        "example_en": "This white top suits you very well.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι μπλούζες",
            "accusative_singular": "την μπλούζα"
        },
        "keg_communicative_function": "Complimenting and choosing clothes"
    },
    {
        "id": "A1-U101-065",
        "greek": "το μπουφάν",
        "phonetic_hint": "",
        "english": "jacket / winter jacket",
        "notes": "Klik A1 p. 31. Digraphs μπ [b] and ου [u]. Neuter indeclinable loanword.",
        "gender_or_pos": "noun (neuter indeclinable)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πάρε το μπουφάν σου, έχει κρύο έξω.",
        "example_en": "Take your jacket, it is cold outside.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter indeclinable)",
            "plural": "τα μπουφάν",
            "accusative_singular": "το μπουφάν"
        },
        "keg_communicative_function": "Advising someone on weather and outer clothing"
    },
    {
        "id": "A1-U101-066",
        "greek": "το πουκάμισο",
        "phonetic_hint": "",
        "english": "shirt (button-up)",
        "notes": "Klik A1 p. 31. Practicing voiceless bilabial stop [p] (π).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο Νίκος φοράει καθαρό γαλάζιο πουκάμισο.",
        "example_en": "Nikos is wearing a clean light-blue shirt.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πουκάμισα",
            "accusative_singular": "το πουκάμισο"
        },
        "keg_communicative_function": "Describing formal or daily attire"
    },
    {
        "id": "A1-U101-067",
        "greek": "το παπούτσι",
        "phonetic_hint": "",
        "english": "shoe",
        "notes": "Klik A1 p. 31. Commonly used in plural: τα παπούτσια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αυτά τα καινούρια παπούτσια είναι πολύ άνετα.",
        "example_en": "These new shoes are very comfortable.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα παπούτσια",
            "accusative_singular": "το παπούτσι"
        },
        "keg_communicative_function": "Shopping for footwear"
    },
    {
        "id": "A1-U101-068",
        "greek": "η ομπρέλα",
        "phonetic_hint": "",
        "english": "umbrella",
        "notes": "Klik A1 p. 31. Internal μπ pronounced [mb] or [b].",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βρέχει καταρρακτωδώς, άνοιξε την ομπρέλα σου.",
        "example_en": "It is pouring rain, open your umbrella.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ομπρέλες",
            "accusative_singular": "την ομπρέλα"
        },
        "keg_communicative_function": "Dealing with rainy weather"
    },
    {
        "id": "A1-U101-069",
        "greek": "το παντελόνι",
        "phonetic_hint": "",
        "english": "trousers / pants",
        "notes": "Klik A1 p. 31. Neuter noun in -ι (plural: τα παντελόνια).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αγοράζω ένα μαύρο παντελόνι για τη δουλειά.",
        "example_en": "I buy black trousers for work.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα παντελόνια",
            "accusative_singular": "το παντελόνι"
        },
        "keg_communicative_function": "Shopping for clothing"
    },
    {
        "id": "A1-U101-070",
        "greek": "η πετσέτα",
        "phonetic_hint": "",
        "english": "towel / napkin",
        "notes": "Klik A1 p. 31. Feminine noun in -α (plural: οι πετσέτες).",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Παίρνω μια καθαρή πετσέτα για το μπάνιο.",
        "example_en": "I take a clean towel for the bath.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πετσέτες",
            "accusative_singular": "την πετσέτα"
        },
        "keg_communicative_function": "Talking about bathroom and beach items"
    },
    {
        "id": "A1-U101-071",
        "greek": "το παλτό",
        "phonetic_hint": "",
        "english": "coat / overcoat",
        "notes": "Klik A1 p. 32. Neuter indeclinable loanword (το παλτό, τα παλτό).",
        "gender_or_pos": "noun (neuter indeclinable)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Φοράει βαρύ παλτό γιατί κάνει πολύ κρύο.",
        "example_en": "She wears a heavy coat because it is very cold.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter indeclinable)",
            "plural": "τα παλτό",
            "accusative_singular": "το παλτό"
        },
        "keg_communicative_function": "Selecting winter clothing"
    },
    {
        "id": "A1-U101-072",
        "greek": "το πορτοφόλι",
        "phonetic_hint": "",
        "english": "wallet / purse",
        "notes": "Klik A1 p. 32. Neuter noun in -ι (plural: τα πορτοφόλια).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ξέχασα το πορτοφόλι μου στο σπίτι.",
        "example_en": "I forgot my wallet at home.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πορτοφόλια",
            "accusative_singular": "το πορτοφόλι"
        },
        "keg_communicative_function": "Managing personal belongings and money"
    },
    {
        "id": "A1-U101-073",
        "greek": "η φούστα",
        "phonetic_hint": "",
        "english": "skirt",
        "notes": "Klik A1 p. 32. Feminine noun in -α with stress on the first syllable.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αυτή η μπλε φούστα είναι πολύ ωραία.",
        "example_en": "This blue skirt is very pretty.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι φούστες",
            "accusative_singular": "τη φούστα"
        },
        "keg_communicative_function": "Describing clothing styles"
    },
    {
        "id": "A1-U101-074",
        "greek": "το τηλέφωνο",
        "phonetic_hint": "",
        "english": "telephone / phone number",
        "notes": "Klik A1 p. 32. Neuter proparoxytone in -ο with initial τ and voiceless fricative φ [f].",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ποιο είναι το τηλέφωνό σου;",
        "example_en": "What is your telephone number?",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα τηλέφωνα",
            "accusative_singular": "το τηλέφωνο"
        },
        "keg_communicative_function": "Exchanging telephone contact details"
    },
    {
        "id": "A1-U101-075",
        "greek": "τα γενέθλια",
        "phonetic_hint": "",
        "english": "birthday",
        "notes": "Klik A1 p. 32. Practicing voiceless dental fricative θ [θ]. Neuter plural noun.",
        "gender_or_pos": "noun (neuter plural)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Χρόνια πολλά για τα γενέθλιά σου!",
        "example_en": "Happy birthday! (Many years to you!)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter plural)",
            "plural": "τα γενέθλια",
            "accusative_singular": "τα γενέθλια"
        },
        "keg_communicative_function": "Wishing happy birthday and celebrating milestones"
    },

    # --- Page 33 & 34: Sounds [δ], [t], [d] (ντ), [γ] - Landscapes, Food & Music ---
    {
        "id": "A1-U101-076",
        "greek": "η εφημερίδα",
        "phonetic_hint": "",
        "english": "newspaper",
        "notes": "Klik A1 p. 33. Feminine noun in -α with voiced dental fricative δ [ð].",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Διαβάζω την πρωινή εφημερίδα με τον καφέ μου.",
        "example_en": "I read the morning newspaper with my coffee.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι εφημερίδες",
            "accusative_singular": "την εφημερίδα"
        },
        "keg_communicative_function": "Buying reading material at the kiosk (περίπτερο)"
    },
    {
        "id": "A1-U101-077",
        "greek": "η πορτοκαλάδα",
        "phonetic_hint": "",
        "english": "orangeade / orange soda",
        "notes": "Klik A1 p. 33. Classic Greek beverage: 'με ανθρακικό' (fizzy) or 'χωρίς' (still).",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Θα ήθελα μία δροσερή πορτοκαλάδα, παρακαλώ.",
        "example_en": "I would like a chilled orangeade, please.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πορτοκαλάδες",
            "accusative_singular": "την πορτοκαλάδα"
        },
        "keg_communicative_function": "Ordering beverages at a cafe or kiosk"
    },
    {
        "id": "A1-U101-078",
        "greek": "η σοκολάτα",
        "phonetic_hint": "",
        "english": "chocolate",
        "notes": "Klik A1 p. 33. Feminine in -α. Plural: οι σοκολάτες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μου αρέσει η μαύρη σοκολάτα με αμύγδαλα.",
        "example_en": "I like dark chocolate with almonds.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι σοκολάτες",
            "accusative_singular": "τη σοκολάτα"
        },
        "keg_communicative_function": "Buying sweets and confectioneries"
    },
    {
        "id": "A1-U101-079",
        "greek": "το περιοδικό",
        "phonetic_hint": "",
        "english": "magazine",
        "notes": "Klik A1 p. 33. Oxytone neuter in -ό (plural: τα περιοδικά).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αγοράζω ένα εβδομαδιαίο περιοδικό από το περίπτερο.",
        "example_en": "I buy a weekly magazine from the kiosk.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα περιοδικά",
            "accusative_singular": "το περιοδικό"
        },
        "keg_communicative_function": "Buying reading materials"
    },
    {
        "id": "A1-U101-080",
        "greek": "η θάλασσα",
        "phonetic_hint": "",
        "english": "sea",
        "notes": "Klik A1 p. 33. Feminine proparoxytone in -α (plural: οι θάλασσες).",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κολυμπάμε στην καθαρή θάλασσα το πρωί.",
        "example_en": "We swim in the clear sea in the morning.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι θάλασσες",
            "accusative_singular": "τη θάλασσα"
        },
        "keg_communicative_function": "Describing nature and coastal destinations"
    },
    {
        "id": "A1-U101-081",
        "greek": "το βουνό",
        "phonetic_hint": "",
        "english": "mountain",
        "notes": "Klik A1 p. 33. Oxytone neuter in -ό (plural: τα βουνά).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο Όλυμπος είναι το ψηλότερο βουνό της Ελλάδας.",
        "example_en": "Mount Olympus is the highest mountain in Greece.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα βουνά",
            "accusative_singular": "το βουνό"
        },
        "keg_communicative_function": "Describing geographical landscapes"
    },
    {
        "id": "A1-U101-082",
        "greek": "ο κινηματογράφος",
        "phonetic_hint": "",
        "english": "cinema / movie theater",
        "notes": "Klik A1 p. 33. Often abbreviated informally as 'το σινεμά'.",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο θερινός κινηματογράφος είναι μαγικός το καλοκαίρι.",
        "example_en": "The open-air cinema is magical in summer.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι κινηματογράφοι",
            "accusative_singular": "τον κινηματογράφο"
        },
        "keg_communicative_function": "Planning evening entertainment"
    },
    {
        "id": "A1-U101-083",
        "greek": "το χωριό",
        "phonetic_hint": "",
        "english": "village",
        "notes": "Klik A1 p. 33. Oxytone neuter in -ό (plural: τα χωριά).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το καλοκαίρι πάμε στο χωριό του παππού.",
        "example_en": "In summer we go to my grandfather's village.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα χωριά",
            "accusative_singular": "το χωριό"
        },
        "keg_communicative_function": "Talking about origin and rural Greece"
    },
    {
        "id": "A1-U101-084",
        "greek": "η ταβέρνα",
        "phonetic_hint": "",
        "english": "taverna / traditional restaurant",
        "notes": "Klik A1 p. 33. Core Greek dining establishment.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τρώμε φρέσκο ψάρι στην παραδοσιακή ταβέρνα.",
        "example_en": "We eat fresh fish at the traditional taverna.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ταβέρνες",
            "accusative_singular": "την ταβέρνα"
        },
        "keg_communicative_function": "Eating out and cultural dining"
    },
    {
        "id": "A1-U101-085",
        "greek": "το βιολί",
        "phonetic_hint": "",
        "english": "violin",
        "notes": "Klik A1 p. 34. Oxytone neuter in -ί (plural: τα βιολιά).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο μουσικός παίζει παραδοσιακό νησιώτικο βιολί.",
        "example_en": "The musician plays traditional island violin.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα βιολιά",
            "accusative_singular": "το βιολί"
        },
        "keg_communicative_function": "Talking about traditional Greek music"
    },
    {
        "id": "A1-U101-086",
        "greek": "η γάτα",
        "phonetic_hint": "",
        "english": "cat",
        "notes": "Klik A1 p. 34. Practicing voiced velar fricative γ [ɣ]. Plural: οι γάτες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η άσπρη γάτα κοιμάται στον ήλιο.",
        "example_en": "The white cat is sleeping in the sun.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι γάτες",
            "accusative_singular": "τη γάτα"
        },
        "keg_communicative_function": "Talking about domestic pets"
    },

    # --- Page 35, 36, 37: Sounds [x], [k], [g] (γκ/γγ), [s], [ts/dz] ---
    {
        "id": "A1-U101-087",
        "greek": "η καρέκλα",
        "phonetic_hint": "",
        "english": "chair",
        "notes": "Klik A1 p. 35. Feminine noun in -α with stress on the penult.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κάθισε σε αυτή την άνετη καρέκλα.",
        "example_en": "Sit down in this comfortable chair.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι καρέκλες",
            "accusative_singular": "την καρέκλα"
        },
        "keg_communicative_function": "Classroom and household furniture"
    },
    {
        "id": "A1-U101-088",
        "greek": "το μολύβι",
        "phonetic_hint": "",
        "english": "pencil",
        "notes": "Klik A1 p. 35. Neuter noun in -ι with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Γράφω την άσκηση με μολύβι.",
        "example_en": "I write the exercise in pencil.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μολύβια",
            "accusative_singular": "το μολύβι"
        },
        "keg_communicative_function": "Classroom instructions and stationery"
    },
    {
        "id": "A1-U101-089",
        "greek": "ο χάρτης",
        "phonetic_hint": "",
        "english": "map",
        "notes": "Klik A1 p. 35. Practicing voiceless velar fricative χ [x]. Masculine in -ης.",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κοιτάζουμε τον χάρτη της Ελλάδας.",
        "example_en": "We look at the map of Greece.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι χάρτες",
            "accusative_singular": "τον χάρτη"
        },
        "keg_communicative_function": "Reading geographical maps and directions"
    },
    {
        "id": "A1-U101-090",
        "greek": "το χιόνι",
        "phonetic_hint": "",
        "english": "snow",
        "notes": "Klik A1 p. 35. Neuter noun in -ι. Pronounced with palatal [ç].",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το χιόνι καλύπτει τις στέγες των σπιτιών.",
        "example_en": "The snow covers the roofs of the houses.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα χιόνια",
            "accusative_singular": "το χιόνι"
        },
        "keg_communicative_function": "Describing winter weather conditions"
    },
    {
        "id": "A1-U101-091",
        "greek": "το αβγό",
        "phonetic_hint": "",
        "english": "egg",
        "notes": "Klik A1 p. 35. Also spelled αυγό. Oxytone neuter in -ό (τα αβγά).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τρώω ένα βραστό αβγό για πρωινό.",
        "example_en": "I eat a boiled egg for breakfast.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα αβγά",
            "accusative_singular": "το αβγό"
        },
        "keg_communicative_function": "Ordering breakfast foods"
    },
    {
        "id": "A1-U101-092",
        "greek": "ο σκύλος",
        "phonetic_hint": "",
        "english": "dog",
        "notes": "Klik A1 p. 35. Practicing voiceless velar stop κ [k]. Plural: οι σκύλοι / τα σκυλιά.",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο σκύλος τρέχει χαρούμενος στο πάρκο.",
        "example_en": "The dog is running happily in the park.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι σκύλοι",
            "accusative_singular": "τον σκύλο"
        },
        "keg_communicative_function": "Talking about pets and animals"
    },
    {
        "id": "A1-U101-093",
        "greek": "το μαρούλι",
        "phonetic_hint": "",
        "english": "lettuce",
        "notes": "Klik A1 p. 36. Neuter noun in -ι with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Φτιάχνω μια πράσινη σαλάτα με τραγανό μαρούλι.",
        "example_en": "I make a green salad with crisp lettuce.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μαρούλια",
            "accusative_singular": "το μαρούλι"
        },
        "keg_communicative_function": "Selecting salad greens at market"
    },
    {
        "id": "A1-U101-094",
        "greek": "το γιαούρτι",
        "phonetic_hint": "",
        "english": "yogurt / Greek strained yogurt",
        "notes": "Klik A1 p. 37. Practicing voiceless alveolar fricative [s] (σ).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το στραγγιστό ελληνικό γιαούρτι είναι πεντανόστιμο.",
        "example_en": "Strained Greek yogurt is delicious.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα γιαούρτια",
            "accusative_singular": "το γιαούρτι"
        },
        "keg_communicative_function": "Ordering dairy and desserts"
    },
    {
        "id": "A1-U101-095",
        "greek": "το σουβλάκι",
        "phonetic_hint": "",
        "english": "souvlaki / skewer",
        "notes": "Klik A1 p. 37. Practicing σ [s] and diminutive neuter suffix -άκι.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Παραγγέλνουμε δύο σουβλάκια με πίτα και τζατζίκι.",
        "example_en": "We order two souvlakia with pita and tzatziki.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα σουβλάκια",
            "accusative_singular": "το σουβλάκι"
        },
        "keg_communicative_function": "Ordering Greek fast food and street food"
    },

    # --- Page 38, 39, 40, 41: Nature, Communication & Core Action Verbs ---
    {
        "id": "A1-U101-096",
        "greek": "το λιμάνι",
        "phonetic_hint": "",
        "english": "port / harbor",
        "notes": "Klik A1 p. 38. Practicing lateral alveolar [l] (λ). Plural: τα λιμάνια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το πλοίο φτάνει στο λιμάνι του Πειραιά.",
        "example_en": "The ship arrives at the port of Piraeus.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα λιμάνια",
            "accusative_singular": "το λιμάνι"
        },
        "keg_communicative_function": "Navigating ferry ports and seaside terminals"
    },
    {
        "id": "A1-U101-097",
        "greek": "το δέντρο",
        "phonetic_hint": "",
        "english": "tree",
        "notes": "Klik A1 p. 38. Digraph ντ internally [nd]/[d]. Plural: τα δέντρα.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Καθόμαστε κάτω από τη σκιά του μεγάλου δέντρου.",
        "example_en": "We sit under the shade of the big tree.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα δέντρα",
            "accusative_singular": "το δέντρο"
        },
        "keg_communicative_function": "Describing outdoor environments and nature"
    },
    {
        "id": "A1-U101-098",
        "greek": "η λίμνη",
        "phonetic_hint": "",
        "english": "lake",
        "notes": "Klik A1 p. 38. Feminine noun in -η with plural in -ες (οι λίμνες).",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κάνουμε βόλτα γύρω από την όμορφη λίμνη.",
        "example_en": "We take a walk around the beautiful lake.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι λίμνες",
            "accusative_singular": "τη λίμνη"
        },
        "keg_communicative_function": "Describing natural landmarks"
    },
    {
        "id": "A1-U101-099",
        "greek": "το πάρκο",
        "phonetic_hint": "",
        "english": "park",
        "notes": "Klik A1 p. 38. Neuter noun in -ο with plural in -α.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τα παιδιά παίζουν στο πάρκο της γειτονιάς.",
        "example_en": "The children are playing in the neighborhood park.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πάρκα",
            "accusative_singular": "το πάρκο"
        },
        "keg_communicative_function": "Leisure activities in public town spaces"
    },
    {
        "id": "A1-U101-100",
        "greek": "η γλώσσα",
        "phonetic_hint": "",
        "english": "language / tongue",
        "notes": "Klik A1 p. 39. Feminine noun in -α with double σσ: οι γλώσσες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μαθαίνω την ελληνική γλώσσα με ενθουσιασμό.",
        "example_en": "I am learning the Greek language with enthusiasm.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι γλώσσες",
            "accusative_singular": "τη γλώσσα"
        },
        "keg_communicative_function": "Talking about languages and communication"
    },
    {
        "id": "A1-U101-101",
        "greek": "η διεύθυνση",
        "phonetic_hint": "",
        "english": "address (street / email)",
        "notes": "Klik A1 p. 39. Feminine noun in -ση with plural in -σεις.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ποια είναι η διεύθυνση του ξενοδοχείου σας;",
        "example_en": "What is the address of your hotel?",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι διευθύνσεις",
            "accusative_singular": "τη διεύθυνση"
        },
        "keg_communicative_function": "Asking for and providing address information"
    },
    {
        "id": "A1-U101-102",
        "greek": "το ψάρι",
        "phonetic_hint": "",
        "english": "fish",
        "notes": "Klik A1 p. 40. Practicing voiceless affricate/cluster [ps] (ψ).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τρώμε ψητό ψάρι στην ψαροταβέρνα.",
        "example_en": "We eat grilled fish at the fish taverna.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ψάρια",
            "accusative_singular": "το ψάρι"
        },
        "keg_communicative_function": "Ordering seafood and fresh fish"
    },
    {
        "id": "A1-U101-103",
        "greek": "το αναψυκτικό",
        "phonetic_hint": "",
        "english": "soft drink / soda",
        "notes": "Klik A1 p. 40. Practicing cluster [ps] (ψ). Plural: τα αναψυκτικά.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Προτιμώ ένα κρύο αναψυκτικό χωρίς ζάχαρη.",
        "example_en": "I prefer a cold sugar-free soft drink.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα αναψυκτικά",
            "accusative_singular": "το αναψυκτικό"
        },
        "keg_communicative_function": "Ordering non-alcoholic drinks"
    },
    {
        "id": "A1-U101-104",
        "greek": "ταξιδεύω",
        "phonetic_hint": "",
        "english": "to travel",
        "notes": "Klik A1 p. 40. Type A regular active verb. Practicing ξ [ks] and ευ [ev].",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ταξιδεύω συχνά στην Ελλάδα για διακοπές.",
        "example_en": "I travel often to Greece for vacation.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A (active regular)",
            "third_person_singular": "ταξιδεύει",
            "first_person_plural": "ταξιδεύουμε"
        },
        "keg_communicative_function": "Describing travel habits and journeys"
    },
    {
        "id": "A1-U101-105",
        "greek": "ξυπνάω",
        "phonetic_hint": "",
        "english": "to wake up",
        "notes": "Klik A1 p. 40. Type B1 contract verb (ξυπνάω / ξυπνώ). Practicing ξ [ks].",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κάθε μέρα ξυπνάω στις επτά το πρωί.",
        "example_en": "Every day I wake up at seven in the morning.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type B1",
            "third_person_singular": "ξυπνάει",
            "first_person_plural": "ξυπνάμε"
        },
        "keg_communicative_function": "Describing morning routines"
    },
    {
        "id": "A1-U101-106",
        "greek": "τρώω",
        "phonetic_hint": "",
        "english": "to eat",
        "notes": "Klik A1 p. 40. Common irregular verb: τρώω, τρως, τρώει, τρώμε, τρώτε, τρώνε.",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τρώμε μεσημεριανό με την οικογένεια στις δύο.",
        "example_en": "We eat lunch with the family at two o'clock.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "irregular",
            "third_person_singular": "τρώει",
            "first_person_plural": "τρώμε"
        },
        "keg_communicative_function": "Talking about meals and daily dining habits"
    },
    {
        "id": "A1-U101-107",
        "greek": "δουλεύω",
        "phonetic_hint": "",
        "english": "to work",
        "notes": "Klik A1 p. 40. Type A active regular verb: δουλεύω, δουλεύεις, δουλεύει.",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Δουλεύω σε μια εταιρεία στο κέντρο της πόλης.",
        "example_en": "I work at a company in the city center.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A (active regular)",
            "third_person_singular": "δουλεύει",
            "first_person_plural": "δουλεύουμε"
        },
        "keg_communicative_function": "Stating professional occupation and workplace"
    },
    {
        "id": "A1-U101-108",
        "greek": "ξοδεύω",
        "phonetic_hint": "",
        "english": "to spend (money / energy)",
        "notes": "Klik A1 p. 40. Type A active regular verb. Practicing cluster ξ [ks] and ευ [ev].",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Δεν ξοδεύω πολλά χρήματα όταν κάνω ψώνια.",
        "example_en": "I do not spend a lot of money when I shop.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A (active regular)",
            "third_person_singular": "ξοδεύει",
            "first_person_plural": "ξοδεύουμε"
        },
        "keg_communicative_function": "Discussing spending habits and shopping"
    },
    {
        "id": "A1-U101-109",
        "greek": "τα χρήματα",
        "phonetic_hint": "",
        "english": "money",
        "notes": "Klik A1 p. 40. Neuter plural noun (το χρήμα, τα χρήματα). Often colloquial 'τα λεφτά'.",
        "gender_or_pos": "noun (neuter plural)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πόσα χρήματα χρειάζεσαι για το ταξίδι;",
        "example_en": "How much money do you need for the trip?",
        "grammatical_info": {
            "part_of_speech": "noun (neuter plural)",
            "plural": "τα χρήματα",
            "accusative_singular": "τα χρήματα"
        },
        "keg_communicative_function": "Managing finances and purchasing goods"
    },
    {
        "id": "A1-U101-110",
        "greek": "η χελώνα",
        "phonetic_hint": "",
        "english": "turtle / tortoise",
        "notes": "Klik A1 p. 41. Practicing voiceless velar fricative χ [x]. Plural: οι χελώνες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η θαλάσσια χελώνα Καρέτα-Καρέτα ζει στην Ελλάδα.",
        "example_en": "The loggerhead sea turtle Caretta-Caretta lives in Greece.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι χελώνες",
            "accusative_singular": "τη χελώνα"
        },
        "keg_communicative_function": "Naming native animals and wildlife"
    },
    {
        "id": "A1-U101-111",
        "greek": "το μπουκάλι",
        "phonetic_hint": "",
        "english": "bottle",
        "notes": "Klik A1 p. 41. Neuter noun in -ι with plural in -ια. Digraphs μπ [b] and ου [u].",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ανοίγουμε ένα μπουκάλι καλό κρασί στο δείπνο.",
        "example_en": "We open a bottle of good wine at dinner.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μπουκάλια",
            "accusative_singular": "το μπουκάλι"
        },
        "keg_communicative_function": "Ordering bottled drinks and table service"
    },
    {
        "id": "A1-U101-112",
        "greek": "το τραπέζι",
        "phonetic_hint": "",
        "english": "table",
        "notes": "Klik A1 p. 41. Neuter noun in -ι with plural in -ια. Related to 'κάνω τραπέζι' (host a meal).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ένα τραπέζι για τέσσερα άτομα έξω, παρακαλώ.",
        "example_en": "A table for four outside, please.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα τραπέζια",
            "accusative_singular": "το τραπέζι"
        },
        "keg_communicative_function": "Reserving or asking for a table at a taverna"
    }
]

lesson_u101 = {
    "unit_id": "unit-101",
    "lesson_id": "lesson-01",
    "title": "Εισαγωγική Ενότητα: Ήχοι, Αλφάβητο & Βασικό Λεξιλόγιο (Pages 25-41)",
    "description": "CEFR A1: Phonetic patterns, alphabet letter combinations, and foundational vocabulary from Klik A1 (pages 25-41).",
    "lesson_status": "not_started",
    "lesson_notes": """Κλικ στα Ελληνικά Α1 — Εισαγωγική Ενότητα (Σελίδες 25-41):
• Φωνηεντικά δίψηφα (Vowel Digraphs):
  - ει, οι, υι, η, ι, υ → [i]
  - αι, ε → [e]
  - ου → [u]
• Συνδυασμοί αυ, ευ (Combinations with υ):
  - Pronounced [af], [ef] before voiceless consonants (θ, κ, ξ, π, σ, τ, φ, χ, ψ).
  - Pronounced [av], [ev] before vowels and voiced consonants (β, γ, δ, ζ, λ, μ, ν, ρ).
• Σύμφωνα & συμφωνικά δίψηφα (Consonants & Consonant Digraphs):
  - μπ → [b] at the start of a word, [mb]/[b] internally.
  - ντ → [d] at the start of a word, [nd]/[d] internally.
  - γκ / γγ → [g] at the start of a word, [ŋg]/[g] internally.
  - τσ → [ts], τζ → [dz].
• Διακριτικά σημεία (Diacritics):
  - Διαλυτικά (dialytika ¨): Separate vowels in digraphs (π.χ. το προϊόν, το καΐκι).""",
    "entries": cards_u101
}

def main():
    print(f"Writing {len(cards_u101)} cards to {YAML_PATH}...")
    with open(YAML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(lesson_u101, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("YAML successfully written.")

    # Update manifest.yaml
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    units = manifest.get("units", [])
    # Check if unit-101 already exists
    existing = next((u for u in units if u.get("id") == "unit-101"), None)
    unit_101_entry = {
        "id": "unit-101",
        "title": "Κλικ στα Ελληνικά Α1: Σελίδες 25-41 (Εισαγωγική Ενότητα - Ήχοι, Γράμματα & Πρώτες Λέξεις)",
        "order": 101,
        "lessons": [
            {
                "id": "lesson-01",
                "file": "unit-101/lesson-01.yaml",
                "title": "Εισαγωγική Ενότητα: Ήχοι, Αλφάβητο & Βασικό Λεξιλόγιο (Pages 25-41)"
            }
        ]
    }

    if existing:
        print("Updating existing unit-101 in manifest.yaml...")
        idx = units.index(existing)
        units[idx] = unit_101_entry
    else:
        print("Appending unit-101 to manifest.yaml...")
        units.append(unit_101_entry)

    manifest["units"] = units

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("Manifest successfully updated with unit-101!")

if __name__ == "__main__":
    main()

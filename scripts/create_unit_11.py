# -*- coding: utf-8 -*-
"""
Script to create Unit 11: Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)
Strictly conforming to docs/LESSON_CREATION_GUIDE.md and KEG A1 Standards.
"""
import sys
import json
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
UNIT_DIR = CONTENT_DIR / "unit-11"
UNIT_DIR.mkdir(parents=True, exist_ok=True)
YAML_PATH = UNIT_DIR / "lesson-01.yaml"
JSON_PATH = CONTENT_DIR / "keg_a1_units_11.json"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

cards_u11 = [
    # 1. Weather & Meteorological Phenomena
    {
        "id": "A1-U11-001",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "ο καιρός",
        "back_primary": "weather / time",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι καιροί",
            "accusative_singular": "τον καιρό"
        },
        "keg_communicative_function": "Inquiring about and describing the weather",
        "example_el": "Πώς είναι ο καιρός σήμερα στην Αθήνα;",
        "example_en": "How is the weather today in Athens?",
        "notes_or_mnemonics": "Masculine in -ος with plural in -οι (οι καιροί). Key question: 'Τι καιρό κάνει;' (What is the weather like?)."
    },
    {
        "id": "A1-U11-002",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "ο ήλιος",
        "back_primary": "sun",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι ήλιοι",
            "accusative_singular": "τον ήλιο"
        },
        "keg_communicative_function": "Describing sunny atmospheric conditions",
        "example_el": "Ο ήλιος λάμπει στον ουρανό.",
        "example_en": "The sun shines in the sky.",
        "notes_or_mnemonics": "Masculine in -ος with plural in -οι (οι ήλιοι)."
    },
    {
        "id": "A1-U11-003",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "η βροχή",
        "back_primary": "rain",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι βροχές",
            "accusative_singular": "τη βροχή"
        },
        "keg_communicative_function": "Discussing rainfall and rainy weather",
        "example_el": "Η βροχή είναι πολύ δυνατή σήμερα.",
        "example_en": "The rain is very heavy today.",
        "notes_or_mnemonics": "Feminine oxytone in -ή with plural in -ές (οι βροχές)."
    },
    {
        "id": "A1-U11-004",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "το χιόνι",
        "back_primary": "snow",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα χιόνια",
            "accusative_singular": "το χιόνι"
        },
        "keg_communicative_function": "Discussing snowfall and winter conditions",
        "example_el": "Υπάρχει πολύ χιόνι πάνω στα βουνά.",
        "example_en": "There is a lot of snow up on the mountains.",
        "notes_or_mnemonics": "Neuter in -ι with plural in -ια (τα χιόνια)."
    },
    {
        "id": "A1-U11-005",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "ο αέρας / ο άνεμος",
        "back_primary": "wind / air",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι αέρηδες / οι άνεμοι",
            "accusative_singular": "τον αέρα / τον άνεμο"
        },
        "keg_communicative_function": "Describing windy weather conditions",
        "example_el": "Σήμερα έχει πολύ δυνατό αέρα στο νησί.",
        "example_en": "Today there is very strong wind on the island.",
        "notes_or_mnemonics": "Common usage: 'ο αέρας'. Weather forecasts often use 'ο άνεμος'."
    },
    {
        "id": "A1-U11-006",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "το σύννεφο",
        "back_primary": "cloud",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα σύννεφα",
            "accusative_singular": "το σύννεφο"
        },
        "keg_communicative_function": "Describing sky conditions",
        "example_el": "Βλέπω μαύρα σύννεφα στον ουρανό.",
        "example_en": "I see dark clouds in the sky.",
        "notes_or_mnemonics": "Proparoxytone neuter in -ο with plural in -α (τα σύννεφα)."
    },
    {
        "id": "A1-U11-007",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "η συννεφιά",
        "back_primary": "cloudiness / overcast sky",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι συννεφιές",
            "accusative_singular": "τη συννεφιά"
        },
        "keg_communicative_function": "Reporting cloudy weather",
        "example_el": "Έχει συννεφιά αλλά δεν βρέχει.",
        "example_en": "It is overcast, but it is not raining.",
        "notes_or_mnemonics": "Feminine oxytone in -ιά. Frequently paired with verb: 'έχει συννεφιά'."
    },
    {
        "id": "A1-U11-008",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "η θερμοκρασία",
        "back_primary": "temperature",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι θερμοκρασίες",
            "accusative_singular": "τη θερμοκρασία"
        },
        "keg_communicative_function": "Reading and discussing temperature forecasts",
        "example_el": "Η θερμοκρασία είναι είκοσι πέντε βαθμοί Κελσίου.",
        "example_en": "The temperature is twenty-five degrees Celsius.",
        "notes_or_mnemonics": "Feminine in -α with plural in -ες (οι θερμοκρασίες)."
    },
    {
        "id": "A1-U11-009",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "ο βαθμός",
        "back_primary": "degree (temperature) / grade",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι βαθμοί",
            "accusative_singular": "τον βαθμό"
        },
        "keg_communicative_function": "Expressing degrees of temperature",
        "example_el": "Το καλοκαίρι έχουμε σαράντα βαθμούς.",
        "example_en": "In the summer we have forty degrees.",
        "notes_or_mnemonics": "Masculine oxytone in -ός with plural in -οί (οι βαθμοί)."
    },
    {
        "id": "A1-U11-010",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "phrase",
        "front": "κάνει ζέστη",
        "back_primary": "it is hot / it is warm (weather)",
        "grammatical_info": {
            "part_of_speech": "phrase (impersonal weather idiom)"
        },
        "keg_communicative_function": "Expressing that the weather is warm or hot",
        "example_el": "Σήμερα κάνει πολλή ζέστη στην Αθήνα.",
        "example_en": "Today it is very hot in Athens.",
        "notes_or_mnemonics": "Impersonal idiom: κάνει + noun ζέστη (heat)."
    },
    {
        "id": "A1-U11-011",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "phrase",
        "front": "κάνει κρύο",
        "back_primary": "it is cold (weather)",
        "grammatical_info": {
            "part_of_speech": "phrase (impersonal weather idiom)"
        },
        "keg_communicative_function": "Expressing cold weather conditions",
        "example_el": "Τον χειμώνα κάνει αρκετό κρύο.",
        "example_en": "In the winter it is quite cold.",
        "notes_or_mnemonics": "Impersonal idiom: κάνει + noun/adjective κρύο (cold)."
    },
    {
        "id": "A1-U11-012",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "phrase",
        "front": "έχει ήλιο",
        "back_primary": "it is sunny / the sun is out",
        "grammatical_info": {
            "part_of_speech": "phrase (impersonal weather idiom)"
        },
        "keg_communicative_function": "Describing sunny days",
        "example_el": "Έχει ωραίο ήλιο σήμερα, πάμε βόλτα;",
        "example_en": "It is nice and sunny today, shall we go for a walk?",
        "notes_or_mnemonics": "Impersonal construction: έχει + noun ήλιο."
    },
    {
        "id": "A1-U11-013",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "verb",
        "front": "βρέχει",
        "back_primary": "it rains / it is raining",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A (impersonal 3rd singular)",
            "third_person_singular": "βρέχει",
            "first_person_plural": "βρέχουμε (as personal transitive: we wet)"
        },
        "keg_communicative_function": "Reporting rainy conditions",
        "example_el": "Πάρε ομπρέλα γιατί βρέχει έξω.",
        "example_en": "Take an umbrella because it is raining outside.",
        "notes_or_mnemonics": "Used almost exclusively in the 3rd person singular for weather: βρέχει."
    },
    {
        "id": "A1-U11-014",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "verb",
        "front": "χιονίζει",
        "back_primary": "it snows / it is snowing",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A (impersonal 3rd singular)",
            "third_person_singular": "χιονίζει",
            "first_person_plural": "χιονίζουμε"
        },
        "keg_communicative_function": "Reporting snow conditions",
        "example_el": "Χιονίζει στα βουνά της βόρειας Ελλάδας.",
        "example_en": "It is snowing in the mountains of northern Greece.",
        "notes_or_mnemonics": "Impersonal weather verb from το χιόνι (snow)."
    },
    {
        "id": "A1-U11-015",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "verb",
        "front": "φυσάει / φυσά",
        "back_primary": "the wind blows / it is windy",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "B1 (impersonal 3rd singular)",
            "third_person_singular": "φυσάει / φυσά",
            "first_person_plural": "φυσάμε"
        },
        "keg_communicative_function": "Reporting windy atmospheric phenomena",
        "example_el": "Φυσάει πολύ δυνατά κοντά στη θάλασσα.",
        "example_en": "The wind is blowing very strongly near the sea.",
        "notes_or_mnemonics": "Type B1 active verb: φυσάει."
    },

    # 2. Leisure, Travel & Vacation Vocabulary
    {
        "id": "A1-U11-016",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "ο ελεύθερος χρόνος",
        "back_primary": "free time / leisure time",
        "grammatical_info": {
            "part_of_speech": "phrase (noun expression)",
            "plural": "οι ελεύθεροι χρόνοι",
            "accusative_singular": "τον ελεύθερο χρόνο"
        },
        "keg_communicative_function": "Talking about leisure availability and hobbies",
        "example_el": "Τι κάνεις στον ελεύθερο χρόνο σου;",
        "example_en": "What do you do in your free time?",
        "notes_or_mnemonics": "Adjective ελεύθερος (free) + χρόνος (time)."
    },
    {
        "id": "A1-U11-017",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "οι διακοπές",
        "back_primary": "vacation / holidays",
        "grammatical_info": {
            "part_of_speech": "noun (feminine plural)",
            "plural": "οι διακοπές",
            "accusative_singular": "τη διακοπή (break / interruption)"
        },
        "keg_communicative_function": "Discussing vacation plans and holiday periods",
        "example_el": "Το καλοκαίρι πάμε διακοπές στην Κρήτη.",
        "example_en": "In the summer we go on vacation to Crete.",
        "notes_or_mnemonics": "Commonly plural: οι διακοπές (the holidays). Phrase: 'πάω διακοπές'."
    },
    {
        "id": "A1-U11-018",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "η παραλία",
        "back_primary": "beach / seashore",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι παραλίες",
            "accusative_singular": "την παραλία"
        },
        "keg_communicative_function": "Talking about seaside outings and summer recreation",
        "example_el": "Πηγαίνουμε στην παραλία για μπάνιο.",
        "example_en": "We go to the beach for a swim.",
        "notes_or_mnemonics": "Feminine in -α with plural in -ες (οι παραλίες)."
    },
    {
        "id": "A1-U11-019",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "η θάλασσα",
        "back_primary": "sea",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι θάλασσες",
            "accusative_singular": "τη θάλασσα"
        },
        "keg_communicative_function": "Talking about marine geography and swimming",
        "example_el": "Το νερό στη θάλασσα είναι πολύ ζεστό.",
        "example_en": "The water in the sea is very warm.",
        "notes_or_mnemonics": "Feminine proparoxytone in -α with plural in -ες (οι θάλασσες)."
    },
    {
        "id": "A1-U11-020",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "το βουνό",
        "back_primary": "mountain",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα βουνά",
            "accusative_singular": "το βουνό"
        },
        "keg_communicative_function": "Talking about mountain hiking and nature excursions",
        "example_el": "Μου αρέσει να περπατάω στο βουνό.",
        "example_en": "I like walking on the mountain.",
        "notes_or_mnemonics": "Neuter oxytone in -ό with plural in -ά (τα βουνά)."
    },
    {
        "id": "A1-U11-021",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "το νησί",
        "back_primary": "island",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα νησιά",
            "accusative_singular": "το νησί"
        },
        "keg_communicative_function": "Talking about Greek islands and travel destinations",
        "example_el": "Η Σαντορίνη είναι ένα διάσημο ελληνικό νησί.",
        "example_en": "Santorini is a famous Greek island.",
        "notes_or_mnemonics": "Neuter oxytone in -ί with plural in -ιά (τα νησιά)."
    },
    {
        "id": "A1-U11-022",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "το ταξίδι",
        "back_primary": "trip / journey / travel",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ταξίδια",
            "accusative_singular": "το ταξίδι"
        },
        "keg_communicative_function": "Discussing journeys and wishing good travels",
        "example_el": "Καλό ταξίδι και καλή διασκέδαση!",
        "example_en": "Have a good trip and have fun!",
        "notes_or_mnemonics": "Neuter in -ι with plural in -ια (τα ταξίδια). Well-known wish: 'Καλό ταξίδι!'."
    },
    {
        "id": "A1-U11-023",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "η βόλτα",
        "back_primary": "walk / stroll / ride",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι βόλτες",
            "accusative_singular": "τη βόλτα"
        },
        "keg_communicative_function": "Arranging casual walks and outings",
        "example_el": "Πάμε μια βόλτα στην παραλία το απόγευμα;",
        "example_en": "Shall we go for a walk on the beach this afternoon?",
        "notes_or_mnemonics": "Feminine in -α with plural in -ες (οι βόλτες). Idiom: 'πάω βόλτα / κάνω βόλτα'."
    },
    {
        "id": "A1-U11-024",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "το ποδόσφαιρο",
        "back_primary": "football / soccer",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ποδόσφαιρα (rare)",
            "accusative_singular": "το ποδόσφαιρο"
        },
        "keg_communicative_function": "Discussing team sports and athletic hobbies",
        "example_el": "Τα παιδιά παίζουν ποδόσφαιρο στο πάρκο.",
        "example_en": "The children are playing soccer in the park.",
        "notes_or_mnemonics": "Compound neuter: πόδι (foot) + σφαίρα (ball/sphere)."
    },
    {
        "id": "A1-U11-025",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "το μπάσκετ",
        "back_primary": "basketball",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μπάσκετ",
            "accusative_singular": "το μπάσκετ"
        },
        "keg_communicative_function": "Discussing basketball games and hobbies",
        "example_el": "Παίζω μπάσκετ με τους φίλους μου κάθε Σάββατο.",
        "example_en": "I play basketball with my friends every Saturday.",
        "notes_or_mnemonics": "Indeclinable neuter loanword (το μπάσκετ)."
    },
    {
        "id": "A1-U11-026",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "το σινεμά",
        "back_primary": "cinema / movies / movie theater",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα σινεμά",
            "accusative_singular": "το σινεμά"
        },
        "keg_communicative_function": "Going to movie screenings and entertainment",
        "example_el": "Πάμε σινεμά απόψε να δούμε μια ελληνική ταινία;",
        "example_en": "Shall we go to the cinema tonight to see a Greek movie?",
        "notes_or_mnemonics": "Indeclinable neuter loanword (το σινεμά). Synonymous with 'ο κινηματογράφος'."
    },
    {
        "id": "A1-U11-027",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "το θέατρο",
        "back_primary": "theater / theatre",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα θέατρα",
            "accusative_singular": "το θέατρο"
        },
        "keg_communicative_function": "Attending theatrical performances",
        "example_el": "Μου αρέσει πολύ το αρχαίο ελληνικό θέατρο.",
        "example_en": "I really like ancient Greek theater.",
        "notes_or_mnemonics": "Neuter in -ο with plural in -α (τα θέατρα)."
    },
    {
        "id": "A1-U11-028",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "η συναυλία",
        "back_primary": "concert",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι συναυλίες",
            "accusative_singular": "τη συναυλία"
        },
        "keg_communicative_function": "Attending musical performances and live shows",
        "example_el": "Έχουμε εισιτήρια για τη συναυλία της Παρασκευής.",
        "example_en": "We have tickets for Friday's concert.",
        "notes_or_mnemonics": "Feminine in -α with plural in -ες (οι συναυλίες)."
    },
    {
        "id": "A1-U11-029",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "η μουσική",
        "back_primary": "music",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι μουσικές",
            "accusative_singular": "τη μουσική"
        },
        "keg_communicative_function": "Expressing musical taste and listening habits",
        "example_el": "Ακούω παραδοσιακή ελληνική μουσική.",
        "example_en": "I listen to traditional Greek music.",
        "notes_or_mnemonics": "Feminine oxytone in -ή with plural in -ές (οι μουσικές)."
    },
    {
        "id": "A1-U11-030",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "η φωτογραφία",
        "back_primary": "photograph / photography",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι φωτογραφίες",
            "accusative_singular": "τη φωτογραφία"
        },
        "keg_communicative_function": "Taking vacation photos and discussing visual hobbies",
        "example_el": "Βγάζω πολλές φωτογραφίες στις διακοπές μου.",
        "example_en": "I take lots of photos on my vacation.",
        "notes_or_mnemonics": "Feminine in -α with plural in -ες (οι φωτογραφίες). Phrase: 'βγάζω φωτογραφία' (to take a photo)."
    },

    # 3. Verbs of Leisure, Preference & Direct Object Clitics
    {
        "id": "A1-U11-031",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "verb",
        "front": "παίζω",
        "back_primary": "to play (sports/games/instruments) / I play",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό παίζει",
            "first_person_plural": "εμείς παίζουμε"
        },
        "keg_communicative_function": "Talking about playing games, sports, and musical instruments",
        "example_el": "Παίζω κιθάρα και τραγουδάω.",
        "example_en": "I play guitar and sing.",
        "notes_or_mnemonics": "Type A regular verb: παίζω, παίζεις, παίζει, παίζουμε, παίζετε, παίζουν."
    },
    {
        "id": "A1-U11-032",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "verb",
        "front": "ταξιδεύω",
        "back_primary": "to travel / I travel",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό ταξιδεύει",
            "first_person_plural": "εμείς ταξιδεύουμε"
        },
        "keg_communicative_function": "Describing travel habits and destinations",
        "example_el": "Ταξιδεύουμε συχνά στο εξωτερικό.",
        "example_en": "We often travel abroad.",
        "notes_or_mnemonics": "Type A regular verb in -εύω: ταξιδεύω, ταξιδεύεις, ταξιδεύει, ταξιδεύουμε, ταξιδεύετε, ταξιδεύουν."
    },
    {
        "id": "A1-U11-033",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "verb",
        "front": "κολυμπάω / κολυμπώ",
        "back_primary": "to swim / I swim",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "B1",
            "third_person_singular": "αυτός / αυτή / αυτό κολυμπάει (κολυμπά)",
            "first_person_plural": "εμείς κολυμπάμε"
        },
        "keg_communicative_function": "Describing swimming and aquatic recreation",
        "example_el": "Κολυμπάω στη θάλασσα κάθε καλοκαίρι.",
        "example_en": "I swim in the sea every summer.",
        "notes_or_mnemonics": "Type B1 active verb: κολυμπάω, κολυμπάς, κολυμπάει, κολυμπάμε, κολυμπάτε, κολυμπάνε."
    },
    {
        "id": "A1-U11-034",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "verb",
        "front": "χορεύω",
        "back_primary": "to dance / I dance",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό χορεύει",
            "first_person_plural": "εμείς χορεύουμε"
        },
        "keg_communicative_function": "Talking about dancing and festive social gatherings",
        "example_el": "Χορεύουμε συρτάκι στις γιορτές.",
        "example_en": "We dance syrtaki at celebrations.",
        "notes_or_mnemonics": "Type A regular verb in -εύω: χορεύω, χορεύεις, χορεύει, χορεύουμε, χορεύετε, χορεύουν."
    },
    {
        "id": "A1-U11-035",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "verb",
        "front": "ακούω",
        "back_primary": "to listen / to hear / I listen",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό ακούει",
            "first_person_plural": "εμείς ακούμε"
        },
        "keg_communicative_function": "Expressing auditory perception and music consumption",
        "example_el": "Ακούω ραδιόφωνο όταν οδηγώ.",
        "example_en": "I listen to the radio when I drive.",
        "notes_or_mnemonics": "Type A vowel-stem verb: ακούω, ακούς, ακούει, ακούμε, ακούτε, ακούν(ε)."
    },
    {
        "id": "A1-U11-036",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "verb",
        "front": "προτιμάω / προτιμώ",
        "back_primary": "to prefer / I prefer",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "B1",
            "third_person_singular": "αυτός / αυτή / αυτό προτιμάει (προτιμά)",
            "first_person_plural": "εμείς προτιμάμε"
        },
        "keg_communicative_function": "Stating preferences between leisure options or choices",
        "example_el": "Προτιμώ τη θάλασσα από το βουνό.",
        "example_en": "I prefer the sea over the mountain.",
        "notes_or_mnemonics": "Type B1 active verb: προτιμάω, προτιμάς, προτιμάει, προτιμάμε, προτιμάτε, προτιμούν."
    },
    {
        "id": "A1-U11-037",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "phrase",
        "front": "μου αρέσει",
        "back_primary": "I like (singular noun or verb infinitive)",
        "grammatical_info": {
            "part_of_speech": "phrase (preference construction)"
        },
        "keg_communicative_function": "Expressing likes and personal tastes with singular objects or actions",
        "example_el": "Μου αρέσει πολύ το ελληνικό καλοκαίρι.",
        "example_en": "I like the Greek summer very much.",
        "notes_or_mnemonics": "Weak indirect object clitic (μου) + 3rd person singular 'αρέσει' + Nominative singular or verb."
    },
    {
        "id": "A1-U11-038",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "phrase",
        "front": "μου αρέσουν",
        "back_primary": "I like (plural nouns)",
        "grammatical_info": {
            "part_of_speech": "phrase (preference construction)"
        },
        "keg_communicative_function": "Expressing likes and personal tastes with plural objects",
        "example_el": "Μου αρέσουν τα παλιά ελληνικά τραγούδια.",
        "example_en": "I like old Greek songs.",
        "notes_or_mnemonics": "Used exclusively when the liked entity is Nominative plural: 'μου αρέσουν τα νησιά'."
    },
    {
        "id": "A1-U11-039",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "verb",
        "front": "διασκεδάζω",
        "back_primary": "to have fun / to party / to enjoy oneself / I have fun",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό διασκεδάζει",
            "first_person_plural": "εμείς διασκεδάζουμε"
        },
        "keg_communicative_function": "Talking about having a good time at outings and events",
        "example_el": "Διασκεδάζουμε πολύ στις διακοπές μας.",
        "example_en": "We have a lot of fun on our vacation.",
        "notes_or_mnemonics": "Type A regular verb in -άζω: διασκεδάζω, διασκεδάζεις, διασκεδάζει, διασκεδάζουμε, διασκεδάζετε, διασκεδάζουν."
    },
    {
        "id": "A1-U11-040",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "verb",
        "front": "χαλαρώνω",
        "back_primary": "to relax / to unwind / I relax",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "A",
            "third_person_singular": "αυτός / αυτή / αυτό χαλαρώνει",
            "first_person_plural": "εμείς χαλαρώνουμε"
        },
        "keg_communicative_function": "Expressing unwinding and resting during free time",
        "example_el": "Το σαββατοκύριακο μένω σπίτι και χαλαρώνω.",
        "example_en": "On the weekend I stay home and relax.",
        "notes_or_mnemonics": "Type A active verb: χαλαρώνω, χαλαρώνεις, χαλαρώνει, χαλαρώνουμε, χαλαρώνετε, χαλαρώνουν."
    },
    {
        "id": "A1-U11-041",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "τον / την / το",
        "back_primary": "him / her / it (weak direct-object clitics)",
        "grammatical_info": {
            "part_of_speech": "pronoun (personal direct-object singular)",
            "clitic_forms": "τον (masc), την (fem), το (neut)"
        },
        "keg_communicative_function": "Referring to persons or objects as direct objects without repeating nouns",
        "example_el": "Βλέπεις τον Νίκο; — Ναι, τον βλέπω.",
        "example_en": "Do you see Nikos? — Yes, I see him.",
        "notes_or_mnemonics": "Placed directly BEFORE the conjugated verb in indicative sentences (τον βλέπω, την ξέρω, το ακούω)."
    },
    {
        "id": "A1-U11-042",
        "unit_number": 11,
        "unit_theme": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "card_type": "vocabulary",
        "front": "τους / τις / τα",
        "back_primary": "them (weak direct-object clitics plural)",
        "grammatical_info": {
            "part_of_speech": "pronoun (personal direct-object plural)",
            "clitic_forms": "τους (masc), τις (fem), τα (neut)"
        },
        "keg_communicative_function": "Referring to plural persons or objects as direct objects",
        "example_el": "Ξέρεις τους καθηγητές; — Ναι, τους ξέρω καλά.",
        "example_en": "Do you know the professors? — Yes, I know them well.",
        "notes_or_mnemonics": "Placed directly BEFORE the conjugated verb in indicative sentences (τους ξέρω, τις βλέπω, τα θέλω)."
    }
]

# 1. Write content/keg_a1_units_11.json
with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(cards_u11, f, ensure_ascii=False, indent=2)
print(f"[OK] Wrote {len(cards_u11)} cards to {JSON_PATH.name}")

# 2. Build entries for content/unit-11/lesson-01.yaml
lesson_entries = []
for c in cards_u11:
    entry = {
        "id": c["id"],
        "greek": c["front"],
        "phonetic_hint": "",
        "english": c["back_primary"],
        "notes": c.get("notes_or_mnemonics", ""),
        "gender_or_pos": c["grammatical_info"].get("part_of_speech", "phrase"),
        "audio": None,
        "status": "pending_tts",
        "example_el": c.get("example_el", ""),
        "example_en": c.get("example_en", ""),
        "grammatical_info": c.get("grammatical_info", {}),
        "keg_communicative_function": c.get("keg_communicative_function", "")
    }
    lesson_entries.append(entry)

lesson_notes_u11 = (
    "Unit 11 Core Grammar Notes:\n\n"
    "• Weather Idioms & Impersonal Expressions:\n"
    "  - 'Τι καιρό κάνει σήμερα;' (What's the weather like today?).\n"
    "  - 'Κάνει ζέστη / κάνει κρύο' (It is hot / cold).\n"
    "  - 'Έχει ήλιο / έχει συννεφιά / έχει αέρα' (It is sunny / cloudy / windy).\n"
    "  - Impersonal verbs: βρέχει (it rains), χιονίζει (it snows), φυσάει (the wind blows).\n"
    "  - Degrees of temperature: 'Η θερμοκρασία είναι 28 βαθμοί.'\n\n"
    "• Expressing Likes & Preferences ('Μου αρέσει / Μου αρέσουν'):\n"
    "  - 'Μου αρέσει' + Singular noun or verb: 'Μου αρέσει η θάλασσα' / 'Μου αρέσει να ταξιδεύω'.\n"
    "  - 'Μου αρέσουν' + Plural noun: 'Μου αρέσουν τα νησιά'.\n"
    "  - Verb 'προτιμάω / προτιμώ': 'Προτιμώ τη θάλασσα από το βουνό.'\n\n"
    "• Weak Direct-Object Clitic Pronouns (Αιτιατική Προσωπικών Αντωνυμιών):\n"
    "  - Singular: με (me), σε (you), τον (him/it), την (her/it), το (it).\n"
    "  - Plural: μας (us), σας (you all), τους (them masc), τις (them fem), τα (them neut).\n"
    "  - Syntactic position: Placed immediately BEFORE the conjugated verb in active indicative:\n"
    "    * 'Τον βλέπω' (I see him).\n"
    "    * 'Τις ξέρεις;' (Do you know them?).\n"
    "    * 'Δεν το θέλω' (I don't want it)."
)

yaml_payload = {
    "unit_id": "unit-11",
    "lesson_id": "lesson-01",
    "title": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
    "description": "CEFR A1: Talking about hobbies, sports, cinema, beach and island vacations, describing the weather, and using direct-object clitic pronouns.",
    "lesson_status": "not_started",
    "lesson_notes": lesson_notes_u11,
    "entries": lesson_entries
}

with open(YAML_PATH, "w", encoding="utf-8") as f:
    yaml.dump(yaml_payload, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
print(f"[OK] Wrote {len(lesson_entries)} entries to {YAML_PATH.relative_to(BASE_DIR)}")

# 3. Update content/manifest.yaml if unit-11 is not already in manifest
with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = yaml.safe_load(f) or {}

existing_unit_ids = [u["id"] for u in manifest.get("units", [])]
if "unit-11" not in existing_unit_ids:
    units = manifest.get("units", [])
    insert_idx = len(units)
    for idx, u in enumerate(units):
        if u["id"] == "unit-10":
            insert_idx = idx + 1
            break
    units.insert(insert_idx, {
        "id": "unit-11",
        "title": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)",
        "order": "OG-11-A",
        "lessons": [
            {
                "id": "lesson-01",
                "file": "unit-11/lesson-01.yaml",
                "title": "Ελεύθερος Χρόνος, Καιρός & Διακοπές (Leisure, Weather & Holidays)"
            }
        ]
    })
    manifest["units"] = units
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"[OK] Added unit-11 to {MANIFEST_PATH.name} right after unit-10 (order: OG-11-A)")
else:
    print(f"[INFO] unit-11 already exists in {MANIFEST_PATH.name}")

print("\nUnit 11 creation complete!")

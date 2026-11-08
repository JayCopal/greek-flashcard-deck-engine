# -*- coding: utf-8 -*-
"""
Script to create Unit 108c from Klik A1 (Pages 175-194):
Ενότητα 8: Διάλογοι & Εξετάσεις — Φαγητό, Ταβέρνα, Αγορά & Συνταγές (A1 Synthesis)
Strictly conforming to docs/LESSON_CREATION_GUIDE.md and the klik-a1-deck-builder skill.
50 conversational and dialogue cards with 100% vocabulary compliance.
"""
import sys
import re
import unicodedata
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
UNIT_DIR = CONTENT_DIR / "unit-108c"
UNIT_DIR.mkdir(parents=True, exist_ok=True)
YAML_PATH = UNIT_DIR / "lesson-01.yaml"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

allowed_fillers = {
    "λοιπόν", "εντάξει", "βέβαια", "φυσικά", "συγγνώμη", "ορίστε",
    "αμέσως", "μήπως", "βεβαίως", "ναι", "όχι"
}

units_108 = [
    "unit-100", "unit-101", "unit-102", "unit-102b", "unit-103", "unit-103b",
    "unit-104", "unit-104b", "unit-105", "unit-105b", "unit-105c",
    "unit-106", "unit-106b", "unit-106c", "unit-107", "unit-107b", "unit-107c",
    "unit-108", "unit-108b"
]

cards_u108c = [
    # --- 1. Greengrocer & Open-Air Market (001-010) ---
    {
        "id": "A1-U108C-001",
        "greek": "— Καλημέρα σας, τι θα πάρετε σήμερα; — Καλημέρα, θέλω ένα κιλό ντομάτες και μισό κιλό αγγούρια.",
        "phonetic_hint": "— Kah-lee-MEH-rah sahs, tee thah PAH-reh-teh SEE-meh-rah? — Kah-lee-MEH-rah, THEH-loh EH-nah kee-LOH doh-MAH-tes keh mee-SOH kee-LOH ahng-GOO-ryah.",
        "english": "— Good morning, what will you have today? — Good morning, I want one kilo of tomatoes and half a kilo of cucumbers.",
        "notes": "Review Unit 108. Produce market transaction with quantities 'ένα κιλό' and 'μισό κιλό'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι άλλο θέλετε από τον μανάβη; — Θέλω δύο κιλά πατάτες και ένα κιλό κρεμμύδια.",
        "example_en": "— What else do you want from the greengrocer? — I want two kilos of potatoes and one kilo of onions.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Purchasing produce and stating quantities at the greengrocer"
    },
    {
        "id": "A1-U108C-002",
        "greek": "— Πόσο κάνουν οι ντομάτες το κιλό; — Κάνουν δύο ευρώ το κιλό, είναι πολύ φρέσκες.",
        "phonetic_hint": "— POH-soh KAH-noon ee doh-MAH-tes toh kee-LOH? — KAH-noon THEE-oh ev-ROH toh kee-LOH, EE-neh poh-LEE FREH-skes.",
        "english": "— How much are the tomatoes per kilo? — They are two euros per kilo, they are very fresh.",
        "notes": "Review Unit 108. Inquiring about price per kilogram ('το κιλό').",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πόσο κάνουν τα πορτοκάλια; — Κάνουν ένα ευρώ και πενήντα λεπτά το κιλό.",
        "example_en": "— How much are the oranges? — They are one euro and fifty cents per kilo.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Asking and answering about food item unit prices"
    },
    {
        "id": "A1-U108C-003",
        "greek": "— Θέλετε και μερικά φρέσκα φρούτα; — Ναι, βάλτε μου μερικές μπανάνες και τέσσερα μήλα.",
        "phonetic_hint": "— THEH-leh-teh keh meh-ree-KAH FREH-skah FROO-tah? — Neh, VAHL-teh moo meh-ree-KES bah-NAH-nes keh TEH-seh-rah MEE-lah.",
        "english": "— Would you also like some fresh fruit? — Yes, put a few bananas and four apples for me.",
        "notes": "Review Unit 108. Indefinite adjective 'μερικοί, μερικές, μερικά' with fruit nouns.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Έχετε μήλα σήμερα; — Ναι, έχουμε πολύ νόστιμα μήλα.",
        "example_en": "— Do you have apples today? — Yes, we have very tasty apples.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Requesting fruit quantities using indefinite determiners"
    },
    {
        "id": "A1-U108C-004",
        "greek": "— Είναι γλυκά τα ροδάκινα και τα σταφύλια; — Ναι, είναι πολύ γλυκά και νόστιμα!",
        "phonetic_hint": "— EE-neh glee-KAH tah roh-THAH-kee-nah keh tah stah-FEE-lyah? — Neh, EE-neh poh-LEE glee-KAH keh NOH-stee-mah!",
        "english": "— Are the peaches and grapes sweet? — Yes, they are very sweet and tasty!",
        "notes": "Review Unit 108. Adjectives 'γλυκός' and 'νόστιμος'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Θέλεις ένα ροδάκινο ή ένα αχλάδι; — Θέλω ένα γλυκό ροδάκινο, ευχαριστώ.",
        "example_en": "— Do you want a peach or a pear? — I want a sweet peach, thank you.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Inquiring about produce ripeness and taste quality"
    },
    {
        "id": "A1-U108C-005",
        "greek": "— Χρειάζεστε λεμόνια για τη σαλάτα; — Ναι, παρακαλώ, βάλτε μου ένα κιλό φρέσκα λεμόνια.",
        "phonetic_hint": "— Khree-AH-zeh-steh leh-MOH-nyah yah tee sah-LAH-tah? — Neh, pah-rah-kah-LOH, VAHL-teh moo EH-nah kee-LOH FREH-skah leh-MOH-nyah.",
        "english": "— Do you need lemons for the salad? — Yes, please, put one kilo of fresh lemons for me.",
        "notes": "Review Unit 108. Verb 'χρειάζομαι' with salad ingredients.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Έχουμε λεμόνια στο σπίτι; — Όχι, δεν έχουμε κανένα λεμόνι στο ψυγείο.",
        "example_en": "— Do we have lemons at home? — No, we do not have a single lemon in the fridge.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Confirming grocery needs and specifying ingredients"
    },
    {
        "id": "A1-U108C-006",
        "greek": "— Πού είναι η λαϊκή αγορά σήμερα; — Είναι στον δρόμο κοντά στην πλατεία.",
        "phonetic_hint": "— POO EE-neh ee lah-ee-KEE ah-goh-RAH SEE-meh-rah? — EE-neh ston THROH-moh kon-DAH steen plah-TEE-ah.",
        "english": "— Where is the open-air market today? — It is on the street near the square.",
        "notes": "Review Units 102 & 108. Locating the weekly farmer's market ('λαϊκή αγορά').",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πότε έχει λαϊκή αγορά στη γειτονιά σας; — Έχει κάθε Δευτέρα πρωί.",
        "example_en": "— When is there an open-air market in your neighborhood? — There is one every Monday morning.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Inquiring about location and schedule of local open-air markets"
    },
    {
        "id": "A1-U108C-007",
        "greek": "— Έχετε φρέσκο μαρούλι και καρότα; — Βεβαίως, ορίστε ένα πολύ φρέσκο μαρούλι και μισό κιλό καρότα.",
        "phonetic_hint": "— EH-kheh-teh FREH-skoh mah-ROO-lee keh kah-ROH-tah? — Veh-VEH-ohs, oh-REES-teh EH-nah poh-LEE FREH-skoh mah-ROO-lee keh mee-SOH kee-LOH kah-ROH-tah.",
        "english": "— Do you have fresh lettuce and carrots? — Certainly, here is a very fresh lettuce and half a kilo of carrots.",
        "notes": "Review Unit 108. Polite vendor response with 'βεβαίως' and 'ορίστε'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Θα πάρετε και λάχανο σήμερα; — Όχι, σήμερα δεν θέλω λάχανο, ευχαριστώ.",
        "example_en": "— Will you take cabbage today as well? — No, today I do not want cabbage, thank you.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Checking produce availability and accepting vendor selections"
    },
    {
        "id": "A1-U108C-008",
        "greek": "— Θέλετε πράσινες ή κόκκινες πιπεριές; — Θέλω δύο πράσινες πιπεριές και ένα κεφάλι σκόρδο.",
        "phonetic_hint": "— THEH-leh-teh PRAH-see-nes ee KOH-kee-nes pee-peh-RYES? — THEH-loh THEE-oh PRAH-see-nes pee-peh-RYES keh EH-nah keh-FAH-lee SKOR-thoh.",
        "english": "— Do you want green or red peppers? — I want two green peppers and a bulb of garlic.",
        "notes": "Review Unit 108. Selecting vegetables by color with 'πιπεριά' and 'σκόρδο'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Βάζεις σκόρδο στη σάλτσα; — Ναι, βάζω πάντα λίγο σκόρδο για γεύση.",
        "example_en": "— Do you put garlic in the sauce? — Yes, I always add a little garlic for flavor.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Specifying color and variety preferences for vegetables"
    },
    {
        "id": "A1-U108C-009",
        "greek": "— Πόσο θέλετε να σας βάλω από τις μαύρες ελιές; — Βάλτε μου μισό κιλό, παρακαλώ.",
        "phonetic_hint": "— POH-soh THEH-leh-teh nah sahs VAH-loh ah-POH tees MAH-vres eh-LYES? — VAHL-teh moo mee-SOH kee-LOH, pah-rah-kah-LOH.",
        "english": "— How much do you want me to put for you of the black olives? — Put half a kilo for me, please.",
        "notes": "Review Unit 108. Inquiring quantity with 'πόσο' and specifying 'μισό κιλό'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Σου αρέσουν οι πράσινες ελιές; — Μου αρέσουν πολύ οι πράσινες και οι μαύρες ελιές.",
        "example_en": "— Do you like green olives? — I like green and black olives very much.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Specifying weight quantities for olives at the produce market"
    },
    {
        "id": "A1-U108C-010",
        "greek": "— Θέλετε τίποτα άλλο από τη λαϊκή; — Όχι, εντάξει, αυτά είναι όλα για σήμερα.",
        "phonetic_hint": "— THEH-leh-teh TEE-poh-tah AH-loh ah-POH tee lah-ee-KEE? — OH-khee, en-DAHK-see, ahf-TAH EE-neh OH-lah yah SEE-meh-rah.",
        "english": "— Do you want anything else from the market? — No, alright, that is everything for today.",
        "notes": "Review Unit 108. Closing a vendor transaction with 'τίποτα άλλο' and 'εντάξει'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Είναι εντάξει τα πράγματα στη σακούλα; — Ναι, είναι όλα μια χαρά.",
        "example_en": "— Are the items in the bag alright? — Yes, everything is just fine.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Concluding retail purchasing dialogues with vendors"
    },

    # --- 2. Bakery, Butcher & Supermarket (011-020) ---
    {
        "id": "A1-U108C-011",
        "greek": "— Καλημέρα σας, ένα ζεστό ψωμί και μία τυρόπιτα, παρακαλώ. — Ορίστε, είναι μόλις από τον φούρνο!",
        "phonetic_hint": "— Kah-lee-MEH-rah sahs, EH-nah zeh-STOH psoh-MEE keh MEE-ah tee-ROH-pee-tah, pah-rah-kah-LOH. — Oh-REES-teh, EE-neh MOH-lees ah-POH ton FOOR-noh!",
        "english": "— Good morning, a warm bread and a cheese pie, please. — Here you are, they are fresh out of the oven!",
        "notes": "Review Unit 108. Bakery transaction for daily bread and savory pastry.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Είναι ζεστό το ψωμί; — Ναι, είναι πολύ φρέσκο και πολύ ζεστό.",
        "example_en": "— Is the bread warm? — Yes, it is very fresh and very warm.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Purchasing bread and traditional pastries at the bakery"
    },
    {
        "id": "A1-U108C-012",
        "greek": "— Μου δίνετε και δύο κουλούρια; — Βεβαίως, ορίστε δύο πολύ νόστιμα κουλούρια.",
        "phonetic_hint": "— Moo THEE-neh-teh keh THEE-oh koo-LOO-ryah? — Veh-VEH-ohs, oh-REES-teh THEE-oh poh-LEE NOH-stee-mah koo-LOO-ryah.",
        "english": "— Could you also give me two bread rings? — Certainly, here are two very tasty bread rings.",
        "notes": "Review Unit 108. Traditional Greek street bread ring ('κουλούρι').",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Παίρνεις κουλούρι κάθε πρωί; — Ναι, παίρνω πάντα ένα κουλούρι για πρωινό.",
        "example_en": "— Do you get a koulouri every morning? — Yes, I always get a koulouri for breakfast.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Requesting bakery snack items with polite imperative"
    },
    {
        "id": "A1-U108C-013",
        "greek": "— Γεια σας, τι κρέας έχετε σήμερα στο κρεοπωλείο; — Έχουμε πολύ καλό μοσχάρι, αρνί και φρέσκο κοτόπουλο.",
        "phonetic_hint": "— YAH sahs, tee KREH-ahs EH-kheh-teh SEE-meh-rah stoh kreh-oh-poh-LEE-oh? — EH-khoo-meh poh-LEE kah-LOH moh-SKHAH-ree, ahr-NEE keh FREH-skoh koh-TOH-poo-loh.",
        "english": "— Hello, what meat do you have today at the butcher shop? — We have very good beef, lamb, and fresh chicken.",
        "notes": "Review Unit 108. Inquiring about meat selections at the butcher shop.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Θα πάρετε κοτόπουλο ή μοσχάρι; — Θα πάρω ένα μεγάλο κοτόπουλο για τον φούρνο.",
        "example_en": "— Will you take chicken or beef? — I will take a large chicken for the oven.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Inquiring about meat varieties at the butcher shop"
    },
    {
        "id": "A1-U108C-014",
        "greek": "— Κόψτε μου, παρακαλώ, ένα κιλό μοσχαρίσιο κιμά. — Αμέσως, ορίστε ο κιμάς για τα μπιφτέκια σας.",
        "phonetic_hint": "— KOH-mpsteh moo, pah-rah-kah-LOH, EH-nah kee-LOH moh-skhah-REE-syoh kee-MAH. — Ah-MEH-sohs, oh-REES-teh oh kee-MAHS yah tah beef-TEH-kyah sahs.",
        "english": "— Grind one kilo of minced beef for me, please. — Right away, here is the ground meat for your patties.",
        "notes": "Review Unit 108. Ordering ground beef with preparation instructions.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι θα κάνετε με τον κιμά; — Θα κάνω νόστιμα μπιφτέκια με πατάτες.",
        "example_en": "— What will you do with the minced meat? — I will make tasty patties with potatoes.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Ordering custom meat cuts and ground meat at the butcher"
    },
    {
        "id": "A1-U108C-015",
        "greek": "— Θα ήθελα τέσσερις μπριζόλες. — Ορίστε, είναι περίπου ένα κιλό.",
        "phonetic_hint": "— Thah EE-theh-lah TEH-seh-rees bree-ZOH-les. — Oh-REES-teh, EE-neh peh-REE-poo EH-nah kee-LOH.",
        "english": "— I would like four chops. — Here you are, they are about one kilo.",
        "notes": "Review Unit 108. Ordering meat cuts by piece count with weight confirmation.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πόσο κάνουν οι μπριζόλες; — Κάνουν δέκα ευρώ συνολικά.",
        "example_en": "— How much are the chops? — They are ten euros in total.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Ordering specific meat cut portions and verifying final weight"
    },
    {
        "id": "A1-U108C-016",
        "greek": "— Είναι φρέσκα τα ψάρια σήμερα; — Ναι, είναι ολόφρεσκα από τη θάλασσα!",
        "phonetic_hint": "— EE-neh FREH-skah tah PSAH-ryah SEE-meh-rah? — Neh, EE-neh oh-LOH-freh-skah ah-POH tee THAH-lah-sah!",
        "english": "— Is the fish fresh today? — Yes, it is completely fresh from the sea!",
        "notes": "Review Unit 108. Freshness inquiry at the fish market with 'ολόφρεσκος'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι ψάρι θέλετε να πάρετε; — Θέλω ένα μεγάλο ψάρι για τον φούρνο.",
        "example_en": "— What fish do you want to get? — I want a large fish for the oven.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Checking fish freshness and selecting seafood"
    },
    {
        "id": "A1-U108C-017",
        "greek": "— Πού είναι το γάλα και τα τυριά στο σούπερ μάρκετ; — Είναι στο βάθος, δίπλα στα ψυγεία με τα τυριά.",
        "phonetic_hint": "— POO EE-neh toh GHAH-lah keh tah tee-RYAH stoh SOO-pehr MAHR-ket? — EE-neh stoh VAH-thos, THEEP-lah stah psee-YEE-ah meh tah tee-RYAH.",
        "english": "— Where are the milk and cheeses in the supermarket? — They are in the back, next to the refrigerated cheese cases.",
        "notes": "Review Units 106 & 108. Supermarket aisle navigation for dairy products.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Χρειαζόμαστε γάλα και γιαούρτι; — Ναι, πάρε δύο γάλατα και ένα γιαούρτι.",
        "example_en": "— Do we need milk and yogurt? — Yes, get two cartons of milk and one yogurt.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Navigating supermarket aisles and locating dairy sections"
    },
    {
        "id": "A1-U108C-018",
        "greek": "— Θα ήθελα μισό κιλό τυρί φέτα σε άλμη. — Βεβαίως, ορίστε η φέτα, είναι πεντανόστιμο τυρί.",
        "phonetic_hint": "— Thah EE-theh-lah mee-SOH kee-LOH tee-REE FEH-tah seh AHL-mee. — Veh-VEH-ohs, oh-REES-teh ee FEH-tah, EE-neh pen-dah-NOH-stee-moh tee-REE.",
        "english": "— I would like half a kilo of feta cheese in brine. — Certainly, here is the feta, it is delicious cheese.",
        "notes": "Review Unit 108. Traditional Greek cheese counter consultation.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Σου αρέσει η φέτα; — Μου αρέσει πολύ η φέτα σε άλμη.",
        "example_en": "— Do you like feta? — I like feta in brine very much.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Ordering cheese at the deli counter by texture and brine"
    },
    {
        "id": "A1-U108C-019",
        "greek": "— Έχουμε ελαιόλαδο, ρύζι και μακαρόνια στο σπίτι; — Έχουμε ρύζι, αλλά χρειαζόμαστε ένα μπουκάλι λάδι και αλεύρι.",
        "phonetic_hint": "— EH-khoo-meh eh-leh-OH-lah-thoh, REE-zee keh mah-kah-ROH-nyah stoh SPEE-tee? — EH-khoo-meh REE-zee, ah-LAH khree-ah-ZOH-mah-steh EH-nah boo-KAH-lee LAH-thee keh ah-LEF-ree.",
        "english": "— Do we have olive oil, rice, and pasta at home? — We have rice, but we need a bottle of oil and flour.",
        "notes": "Review Unit 108. Pantry essentials inventory dialogue.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πάρε και ένα πακέτο μακαρόνια, σε παρακαλώ. — Εντάξει, θα πάρω ένα πακέτο μακαρόνια.",
        "example_en": "— Get a packet of pasta too, please. — Alright, I will get a packet of pasta.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Coordinating essential pantry grocery purchases"
    },
    {
        "id": "A1-U108C-020",
        "greek": "— Μου δίνετε και μία σακούλα, παρακαλώ; — Βεβαίως, ορίστε η σακούλα. Είναι είκοσι τρία ευρώ συνολικά.",
        "phonetic_hint": "— Moo THEE-neh-teh keh MEE-ah sah-KOO-lah, pah-rah-kah-LOH? — Veh-VEH-ohs, oh-REES-teh ee sah-KOO-lah. EE-neh EE-koh-see THREE-ah ev-ROH see-noh-lee-KAH.",
        "english": "— Could you give me a shopping bag too, please? — Certainly, here is the bag. It is twenty-three euros in total.",
        "notes": "Review Unit 108. Checkout interaction requesting shopping bag ('σακούλα').",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ορίστε είκοσι πέντε ευρώ, κρατήστε τα ρέστα. — Ευχαριστώ πολύ, καλή σας μέρα!",
        "example_en": "— Here is twenty-five euros, keep the change. — Thank you very much, have a nice day!",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Completing supermarket checkout transactions and tipping"
    },

    # --- 3. Taverna, Souvlaki & Cafe (021-035) ---
    {
        "id": "A1-U108C-021",
        "greek": "— Καλησπέρα σας, έχετε ένα ελεύθερο τραπέζι για δύο άτομα; — Βεβαίως, περάστε μέσα, ορίστε ένα ωραίο τραπέζι.",
        "phonetic_hint": "— Kah-lee-SPEH-rah sahs, EH-kheh-teh EH-nah eh-LEF-theh-roh trah-PEH-zee yah THEE-oh AH-toh-mah? — Veh-VEH-ohs, peh-RAH-steh MEH-sah, oh-REES-teh EH-nah oh-REH-oh trah-PEH-zee.",
        "english": "— Good evening, do you have an available table for two people? — Certainly, come inside, here is a nice table.",
        "notes": "Review Unit 108. Arriving at a tavern and asking for a table.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Θέλετε τραπέζι μέσα ή έξω; — Θέλουμε έξω στην αυλή, είναι πολύ όμορφα.",
        "example_en": "— Do you want a table inside or outside? — We want outside in the courtyard, it is very beautiful.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Requesting table seating at a tavern or restaurant"
    },
    {
        "id": "A1-U108C-022",
        "greek": "— Συγγνώμη, μπορούμε να παραγγείλουμε, παρακαλώ; — Βεβαίως, τι θα πάρετε για ορεκτικό;",
        "phonetic_hint": "— Seeg-NOH-mee, boh-ROO-meh nah pah-rahng-GEE-loo-meh, pah-rah-kah-LOH? — Veh-VEH-ohs, tee thah PAH-reh-teh yah oh-rek-tee-KOH?",
        "english": "— Excuse me, may we order, please? — Certainly, what will you have for an appetizer?",
        "notes": "Review Unit 108. Calling the waiter and initiating the food order.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Μπορούμε να παραγγείλουμε τώρα; — Αμέσως, τι θέλετε να πάρετε;",
        "example_en": "— Can we order now? — Right away, what would you like to have?",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Requesting restaurant menus and indicating readiness to order"
    },
    {
        "id": "A1-U108C-023",
        "greek": "— Τι θα πάρετε για ορεκτικό; — Για ορεκτικό θα πάρουμε μία χωριάτικη σαλάτα και ένα τζατζίκι.",
        "phonetic_hint": "— Tee thah PAH-reh-teh yah oh-rek-tee-KOH? — Yah oh-rek-tee-KOH thah PAH-roo-meh MEE-ah khoh-RYAH-tee-kee sah-LAH-tah keh EH-nah dzah-DZEE-kee.",
        "english": "— What will you have for an appetizer? — For an appetizer we will take a Greek salad and a tzatziki.",
        "notes": "Review Unit 108. Ordering traditional Greek starters.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Θέλετε τη σαλάτα με φέτα και ελιές; — Ναι, με πολλή φέτα και ελαιόλαδο.",
        "example_en": "— Do you want the salad with feta and olives? — Yes, with plenty of feta and olive oil.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Ordering appetizers and traditional dips at a taverna"
    },
    {
        "id": "A1-U108C-024",
        "greek": "— Μας φέρνετε λίγο ψωμί ακόμα και ένα μπουκάλι νερό; — Βεβαίως, αμέσως σας τα φέρω.",
        "phonetic_hint": "— Mahs FEHR-neh-teh LEE-goh psoh-MEE ah-KOH-mah keh EH-nah boo-KAH-lee neh-ROH? — Veh-VEH-ohs, ah-MEH-sohs sahs tah FEH-roh.",
        "english": "— Could you bring us a little more bread and a bottle of water? — Certainly, I will bring them to you right away.",
        "notes": "Review Unit 108. Requesting extra table bread and water.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Θέλετε το νερό παγωμένο ή δροσερό; — Θέλουμε ένα μπουκάλι παγωμένο νερό.",
        "example_en": "— Do you want the water ice-cold or chilled? — We want a bottle of ice-cold water.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Requesting additional bread and water from waiting staff"
    },
    {
        "id": "A1-U108C-025",
        "greek": "— Και για κυρίως πιάτο, τι θα πάρετε; — Εγώ θα πάρω δύο σουβλάκια με πατάτες τηγανητές.",
        "phonetic_hint": "— Keh yah kee-REE-os PYAH-toh, tee thah PAH-reh-teh? — Eh-GHOH thah PAH-roh THEE-oh soov-LAH-kyah meh pah-TAH-tes tee-ghah-nee-TES.",
        "english": "— And for the main course, what will you have? — I will have two souvlakia with fried potatoes.",
        "notes": "Review Unit 108. Ordering main dish ('κυρίως πιάτο') and sides.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Θέλεις πίτα με σουβλάκι; — Ναι, θέλω ένα σουβλάκι σε πίτα με ντομάτα και τζατζίκι.",
        "example_en": "— Do you want pita with souvlaki? — Yes, I want a souvlaki in pita with tomato and tzatziki.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Ordering main meat dishes and street food combinations"
    },
    {
        "id": "A1-U108C-026",
        "greek": "— Για μένα, μία μερίδα ψητό κοτόπουλο με ρύζι, παρακαλώ. — Πολύ ωραία, και για τη φίλη σας;",
        "phonetic_hint": "— Yah MEH-nah, MEE-ah meh-REE-thah psee-TOH koh-TOH-poo-loh meh REE-zee, pah-rah-kah-LOH. — Poh-LEE oh-REH-ah, keh yah tee FEE-lee sahs?",
        "english": "— For me, a portion of roast chicken with rice, please. — Very nice, and for your friend?",
        "notes": "Review Unit 108. Specifying meal portion ('μερίδα') with sides.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι φαγητό έχει σήμερα; — Έχει νόστιμο ψητό κοτόπουλο και μπιφτέκια.",
        "example_en": "— What food is there today? — There is tasty roast chicken and patties.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Specifying portion sizes and companion orders"
    },
    {
        "id": "A1-U108C-027",
        "greek": "— Έχετε φρέσκο ψάρι ψητό; — Ναι, έχουμε πολύ καλό ψάρι ψητό στα κάρβουνα.",
        "phonetic_hint": "— EH-kheh-teh FREH-skoh PSAH-ree psee-TOH? — Neh, EH-khoo-meh poh-LEE kah-LOH PSAH-ree psee-TOH stah KAHR-voo-nah.",
        "english": "— Do you have fresh grilled fish? — Yes, we have very good fish grilled over charcoal.",
        "notes": "Review Unit 108. Grilled fish inquiry in tavernas.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Σου αρέσει το ψάρι; — Ναι, μου αρέσει πάρα πολύ το ψητό ψάρι με λεμόνι.",
        "example_en": "— Do you like fish? — Yes, I really love grilled fish with lemon.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Ordering seafood and grilled fish specialties"
    },
    {
        "id": "A1-U108C-028",
        "greek": "— Τι θα πιείτε με το φαγητό; — Θα πιούμε μισό κιλό κόκκινο κρασί και μία μπύρα.",
        "phonetic_hint": "— Tee thah PYEH-teh meh toh fah-yee-TOH? — Thah PYOO-meh mee-SOH kee-LOH KOH-kee-noh krah-SEE keh MEE-ah MPEE-rah.",
        "english": "— What will you drink with the meal? — We will drink half a kilo of red wine and a beer.",
        "notes": "Review Unit 108. Ordering bulk tavern wine ('μισό κιλό κρασί') and beer.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Προτιμάτε λευκό ή κόκκινο κρασί; — Προτιμάμε ένα δροσερό λευκό κρασί.",
        "example_en": "— Do you prefer white or red wine? — We prefer a chilled white wine.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Ordering beverages and house wine by volume at a taverna"
    },
    {
        "id": "A1-U108C-029",
        "greek": "— Θέλετε και ένα ούζο; — Ναι, θέλουμε ένα ούζο με κρύο νερό για αρχή.",
        "phonetic_hint": "— THEH-leh-teh keh EH-nah OO-zoh? — Neh, THEH-loo-meh EH-nah OO-zoh meh KREE-oh neh-ROH yah ahr-KHEE.",
        "english": "— Would you also like an ouzo? — Yes, we want an ouzo with cold water to start.",
        "notes": "Review Unit 108. Ordering traditional Greek aperitif with water.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πίνεις ούζο το καλοκαίρι; — Ναι, πίνω πάντα ούζο δίπλα στη θάλασσα.",
        "example_en": "— Do you drink ouzo in the summer? — Yes, I always drink ouzo beside the sea.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Ordering traditional Greek aperitifs and iced drinks"
    },
    {
        "id": "A1-U108C-030",
        "greek": "— Πώς σας φαίνεται το φαγητό; — Είναι πεντανόστιμο, συγχαρητήρια στον μάγειρα!",
        "phonetic_hint": "— POHS sahs FEH-neh-teh toh fah-yee-TOH? — EE-neh pen-dah-NOH-stee-moh, see-khah-ree-TEE-ryah ston MAH-yee-rah!",
        "english": "— How do you find the food? — It is absolutely delicious, congratulations to the chef!",
        "notes": "Review Unit 108. Expressing meal satisfaction and compliments.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Σου αρέσει το φαγητό; — Ναι, είναι πολύ νόστιμο φαγητό.",
        "example_en": "— Do you like the food? — Yes, it is very tasty food.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Complimenting food taste and chef preparation in a restaurant"
    },
    {
        "id": "A1-U108C-031",
        "greek": "— Θέλετε κάποιο γλυκό για το τέλος; — Ναι, θα πάρουμε ένα γιαούρτι με μέλι και ένα παγωτό.",
        "phonetic_hint": "— THEH-leh-teh KAH-pyoh glee-KOH yah toh TEH-los? — Neh, thah PAH-roo-meh EH-nah yah-OOR-tee meh MEH-lee keh EH-nah pah-ghoh-TOH.",
        "english": "— Would you like some dessert for the end? — Yes, we will take a yogurt with honey and an ice cream.",
        "notes": "Review Unit 108. Ordering traditional desserts ('γιαούρτι με μέλι').",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Έχετε γλυκό σοκολάτα; — Ναι, έχουμε πολύ νόστιμη σοκολάτα και φρούτα.",
        "example_en": "— Do you have chocolate dessert? — Yes, we have very tasty chocolate and fruit.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Ordering desserts and post-meal refreshments"
    },
    {
        "id": "A1-U108C-032",
        "greek": "— Μας φέρνετε τον λογαριασμό, παρακαλώ; — Βεβαίως, αμέσως σας φέρω τον λογαριασμό.",
        "phonetic_hint": "— Mahs FEHR-neh-teh ton loh-ghah-ryahz-MOH, pah-rah-kah-LOH? — Veh-VEH-ohs, ah-MEH-sohs sahs FEH-roh ton loh-ghah-ryahz-MOH.",
        "english": "— Could you bring us the bill, please? — Certainly, I will bring you the bill right away.",
        "notes": "Review Unit 108. Asking for the check in a restaurant or cafe.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πόσο είναι ο λογαριασμός; — Είναι τριάντα δύο ευρώ για όλα.",
        "example_en": "— How much is the bill? — It is thirty-two euros for everything.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Requesting the bill and settling restaurant charges"
    },
    {
        "id": "A1-U108C-033",
        "greek": "— Μπορώ να πληρώσω με πιστωτική κάρτα; — Ναι, φυσικά, με κάρτα ή με μετρητά.",
        "phonetic_hint": "— Boh-ROH nah plee-ROH-soh meh pees-toh-tee-KEE KAHR-tah? — Neh, fee-see-KAH, meh KAHR-tah ee meh meh-tree-TAH.",
        "english": "— Can I pay by credit card? — Yes, of course, by card or with cash.",
        "notes": "Review Unit 108. Asking about payment methods in dining establishments.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πληρώνουμε μαζί; — Ναι, πληρώνουμε μαζί, παρακαλώ.",
        "example_en": "— Are we paying together? — Yes, we are paying together, please.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Inquiring about payment methods and split payment options"
    },
    {
        "id": "A1-U108C-034",
        "greek": "— Ορίστε σαράντα ευρώ, κρατήστε τα ρέστα. — Σας ευχαριστούμε πάρα πολύ, καλό σας βράδυ!",
        "phonetic_hint": "— Oh-REES-teh sah-RAHN-dah ev-ROH, krah-TEE-steh tah REH-stah. — Sahs ef-khah-ree-STOO-meh PAH-rah poh-LEE, kah-LOH sahs VRAH-thee!",
        "english": "— Here is forty euros, keep the change. — Thank you very much, have a pleasant evening!",
        "notes": "Review Unit 108. Polite tipping formula 'κρατήστε τα ρέστα'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Έχει ρέστα; — Όχι, είναι ακριβώς τα χρήματα.",
        "example_en": "— Is there change? — No, it is the exact amount.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Offering tips and polite closing greetings to service staff"
    },
    {
        "id": "A1-U108C-035",
        "greek": "— Θέλεις έναν καφέ μετά το φαγητό; — Ναι, θα ήθελα έναν ζεστό ελληνικό καφέ με λίγη ζάχαρη.",
        "phonetic_hint": "— THEH-lees EH-nahn kah-FEH meh-TAH toh fah-yee-TOH? — Neh, thah EE-theh-lah EH-nahn zeh-STOH eh-lee-nee-KOH kah-FEH meh LEE-yee ZAH-khah-ree.",
        "english": "— Do you want a coffee after the meal? — Yes, I would like a hot Greek coffee with a little sugar.",
        "notes": "Review Unit 108. Ordering coffee post-meal ('ελληνικός καφές').",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πώς πίνεις τον καφέ σου; — Τον πίνω μέτριο, με λίγη ζάχαρη.",
        "example_en": "— How do you drink your coffee? — I drink it medium-sweet, with a little sugar.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Specifying coffee preparation preferences after dining"
    },

    # --- 4. Cooking & Recipes (036-042) ---
    {
        "id": "A1-U108C-036",
        "greek": "— Πώς κάνεις την ελληνική χωριάτικη σαλάτα; — Κόψτε τις ντομάτες, το αγγούρι και το κρεμμύδι σε λεπτές φέτες.",
        "phonetic_hint": "— POHS KAH-nees teen eh-lee-nee-KEE khoh-RYAH-tee-kee sah-LAH-tah? — KOH-mpsteh tees doh-MAH-tes, toh ahng-GOO-ree keh toh kreh-MEE-thee seh lep-TES FEH-tes.",
        "english": "— How do you make Greek country salad? — Cut the tomatoes, cucumber, and onion into thin slices.",
        "notes": "Review Unit 108. Recipe instructions using imperative plural 'κόψτε'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι άλλο βάζεις στη σαλάτα; — Βάζω ελιές, φέτα και λίγη ρίγανη.",
        "example_en": "— What else do you put in the salad? — I add olives, feta, and a little oregano.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Explaining recipe preparation steps and ingredient chopping"
    },
    {
        "id": "A1-U108C-037",
        "greek": "— Πόσο λάδι και αλάτι να βάλω; — Βάλτε λίγο ελαιόλαδο, αλάτι και ρίγανη στη σαλάτα.",
        "phonetic_hint": "— POH-soh LAH-thee keh ah-LAH-tee nah VAH-loh? — VAHL-teh LEE-goh eh-leh-OH-lah-thoh, ah-LAH-tee keh REE-ghah-nee steen sah-LAH-tah.",
        "english": "— How much oil and salt should I add? — Add a little olive oil, salt, and oregano to the salad.",
        "notes": "Review Unit 108. Recipe measurements with imperative 'βάλτε'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Μην ρίχνεις πολύ αλάτι στο φαγητό. — Εντάξει, δεν ρίχνω άλλο αλάτι.",
        "example_en": "— Do not throw too much salt into the food. — Alright, I will not add any more salt.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Giving measuring instructions for culinary seasonings"
    },
    {
        "id": "A1-U108C-038",
        "greek": "— Και μετά τι κάνουμε; — Ανακατέψτε καλά όλα τα υλικά μέσα στο μεγάλο μπολ.",
        "phonetic_hint": "— Keh meh-TAH tee KAH-noo-meh? — Ah-nah-kah-TEHP-steh kah-LAH OH-lah tah ee-lee-KAH MEH-sah stoh meh-GHAH-loh bohl.",
        "english": "— And what do we do after that? — Mix all the ingredients well inside the large bowl.",
        "notes": "Review Unit 108. Cooking procedural step with imperative 'ανακατέψτε'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Είναι καλή η σαλάτα; — Ναι, είναι πολύ καλή και νόστιμη.",
        "example_en": "— Is the salad good? — Yes, it is very good and tasty.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Instructing how to combine and mix recipe ingredients"
    },
    {
        "id": "A1-U108C-039",
        "greek": "— Πώς ψήνουμε το κοτόπουλο με τις πατάτες; — Βάλτε το στον φούρνο για σαράντα λεπτά στους εκατόν ογδόντα βαθμούς.",
        "phonetic_hint": "— POHS PSEE-noo-meh toh koh-TOH-poo-loh meh tees pah-TAH-tes? — VAHL-teh toh ston FOOR-noh yah sah-RAHN-dah lep-TAH stoos eh-kah-TON ohg-THOHN-dah vahth-MOOS.",
        "english": "— How do we bake the chicken with potatoes? — Put it in the oven for forty minutes at one hundred eighty degrees.",
        "notes": "Review Unit 108. Oven temperature and baking time instructions.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ψήστε το κρέας στον φούρνο. — Εντάξει, το βάζω στον φούρνο τώρα.",
        "example_en": "— Bake the meat in the oven. — Alright, I am putting it in the oven now.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Giving oven temperature and cooking time directions"
    },
    {
        "id": "A1-U108C-040",
        "greek": "— Θέλετε πατάτες τηγανητές; — Ναι, θέλω πατάτες τηγανητές με λίγο αλάτι.",
        "phonetic_hint": "— THEH-leh-teh pah-TAH-tes tee-ghah-nee-TES? — Neh, THEH-loh pah-TAH-tes tee-ghah-nee-TES meh LEE-goh ah-LAH-tee.",
        "english": "— Would you like fried potatoes? — Yes, I want fried potatoes with a little salt.",
        "notes": "Review Unit 108. Frying preference and side dish selection.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Σου αρέσουν οι τηγανητές πατάτες; — Μου αρέσουν πάρα πολύ, είναι πολύ νόστιμο φαγητό.",
        "example_en": "— Do you like french fries? — I like them very much, they are very tasty food.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Describing frying methods and side dish preferences"
    },
    {
        "id": "A1-U108C-041",
        "greek": "— Είναι πολύ αλμυρή αυτή η σούπα; — Ναι, έχει πολύ αλάτι, μην ρίχνεις άλλο αλάτι.",
        "phonetic_hint": "— EE-neh poh-LEE ahl-mee-REE ahf-TEE ee SOO-pah? — Neh, EH-khee poh-LEE ah-LAH-tee, meen REEKH-nees AH-loh ah-LAH-tee.",
        "english": "— Is this soup very salty? — Yes, it has too much salt, do not add any more salt.",
        "notes": "Review Unit 108. Taste adjective 'αλμυρός' and seasoning warning.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πώς είναι η γεύση; — Είναι πολύ καλή, αλλά έχει πολύ λεμόνι.",
        "example_en": "— How is the taste? — It is very good, but it has a lot of lemon.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Evaluating seasoning levels and advising on taste adjustments"
    },
    {
        "id": "A1-U108C-042",
        "greek": "— Πώς πίνεις τον ελληνικό καφέ; — Τον πίνω με λίγη ζάχαρη, χωρίς γάλα.",
        "phonetic_hint": "— POHS PEE-nees ton eh-lee-nee-KOH kah-FEH? — Ton PEE-noh meh LEE-yee ZAH-khah-ree, khoh-REES GHAH-lah.",
        "english": "— How do you drink Greek coffee? — I drink it with a little sugar, without milk.",
        "notes": "Review Unit 108. Coffee preparation preference formula.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Μην βάζεις πολλή ζάχαρη στον ελληνικό καφέ. — Εντάξει, πίνω πάντα μέτριο καφέ.",
        "example_en": "— Do not put much sugar in Greek coffee. — Alright, I always drink medium coffee.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Explaining traditional coffee preparation procedures"
    },

    # --- 5. Dietary Habits & CEFR A1 Oral Exam Tasks (043-050) ---
    {
        "id": "A1-U108C-043",
        "greek": "— Τι τρως συνήθως για πρωινό; — Συνήθως τρώω ψωμί με μέλι ή βούτυρο και πίνω έναν ζεστό καφέ.",
        "phonetic_hint": "— Tee TROHS see-NEE-thohs yah proh-ee-NOH? — See-NEE-thohs TROH-oh psoh-MEE meh MEH-lee ee VOO-tee-roh keh PEE-noh EH-nahn zeh-STOH kah-FEH.",
        "english": "— What do you usually eat for breakfast? — Usually I eat bread with honey or butter and drink a hot coffee.",
        "notes": "Review Unit 108. CEFR A1 oral exam inquiry about daily morning dietary habits.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τρως αυγά το πρωί; — Μερικές φορές τρώω ένα βραστό αυγό με φρέσκο ψωμί.",
        "example_en": "— Do you eat eggs in the morning? — Sometimes I eat a boiled egg with fresh bread.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Describing regular morning dietary routines in oral exams"
    },
    {
        "id": "A1-U108C-044",
        "greek": "— Τι περιλαμβάνει η υγιεινή μεσογειακή διατροφή; — Περιλαμβάνει πολλά φρέσκα λαχανικά, φρούτα, ψάρια και ελαιόλαδο.",
        "phonetic_hint": "— Tee peh-ree-lahm-VAH-nee ee ee-yee-ee-NEE meh-soh-yee-ah-KEE thee-ah-troh-FEE? — Peh-ree-lahm-VAH-nee poh-LAH FREH-skah lah-khah-nee-KAH, FROO-tah, PSAH-ryah keh eh-leh-OH-lah-thoh.",
        "english": "— What does the healthy Mediterranean diet include? — It includes plenty of fresh vegetables, fruit, fish, and olive oil.",
        "notes": "Review Unit 108. Describing the Mediterranean diet components.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Κάνεις δίαιτα αυτό τον καιρό; — Ναι, κάνω δίαιτα και τρώω μόνο σαλάτα και φρούτα.",
        "example_en": "— Are you on a diet lately? — Yes, I am on a diet and eat only salad and fruit.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Discussing healthy nutrition and dietary components"
    },
    {
        "id": "A1-U108C-045",
        "greek": "— Τρως κρέας στο μεσημεριανό; — Όχι, δεν τρώω κρέας, τρώω μόνο λαχανικά και φρούτα.",
        "phonetic_hint": "— TROHS KREH-ahs stoh meh-see-meh-ryah-NOH? — OH-khee, then TROH-oh KREH-ahs, TROH-oh MOH-noh lah-khah-nee-KAH keh FROO-tah.",
        "english": "— Do you eat meat at lunch? — No, I do not eat meat, I only eat vegetables and fruit.",
        "notes": "Review Unit 108. Declaring dietary food exclusions.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Έχετε φαγητά χωρίς κρέας στην ταβέρνα; — Ναι, έχουμε πολλές σαλάτες και λαχανικά.",
        "example_en": "— Do you have dishes without meat at the tavern? — Yes, we have many salads and vegetables.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Declaring dietary restrictions and vegetarian preferences"
    },
    {
        "id": "A1-U108C-046",
        "greek": "— Υπάρχει κανένα περίπτερο ανοιχτό εδώ κοντά; — Ναι, υπάρχει ένα περίπτερο απέναντι από την εκκλησία.",
        "phonetic_hint": "— Ee-PAHR-khee kah-NEH-nah peh-REE-pteh-roh ah-neekh-TOH eh-THOH kon-DAH? — Neh, ee-PAHR-khee EH-nah peh-REE-pteh-roh ah-PEH-nahn-dee ah-POH teen ek-klee-SEE-ah.",
        "english": "— Is there any open kiosk nearby? — Yes, there is a kiosk opposite the church.",
        "notes": "Review Unit 108. Indefinite pronoun 'κανένας, καμία, κανένα' in neighborhood inquiries.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι έχει το περίπτερο; — Έχει νερό, αναψυκτικά, εφημερίδες και σοκολάτες.",
        "example_en": "— What does the kiosk have? — It has water, soft drinks, newspapers, and chocolates.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Inquiring about kiosks and neighborhood retail convenience"
    },
    {
        "id": "A1-U108C-047",
        "greek": "— Είναι κανείς στην κουζίνα τώρα; — Όχι, δεν είναι κανείς μέσα, όλοι είναι στο σαλόνι.",
        "phonetic_hint": "— EE-neh kah-NEES steen koo-ZEE-nah TOH-rah? — OH-khee, then EE-neh kah-NEES MEH-sah, OH-lee EE-neh stoh sah-LOH-nee.",
        "english": "— Is anyone in the kitchen right now? — No, no one is inside, everyone is in the living room.",
        "notes": "Review Unit 108. Indefinite pronoun 'κανείς' (anyone / no one).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ήρθε κανείς για το μεσημεριανό φαγητό; — Όχι ακόμα, δεν ήρθε κανένας.",
        "example_en": "— Did anyone come for lunch? — Not yet, nobody has arrived.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Inquiring and stating absence of persons using 'κανείς'"
    },
    {
        "id": "A1-U108C-048",
        "greek": "— Θέλεις κάτι ελαφρύ και νόστιμο για βραδινό; — Ναι, θέλω μόνο ένα γιαούρτι με μέλι και καρύδια.",
        "phonetic_hint": "— THEH-lees KAH-tee eh-lah-FREE keh NOH-stee-moh yah vrah-thee-NOH? — Neh, THEH-loh MOH-noh EH-nah yah-OOR-tee meh MEH-lee keh kah-REE-thyah.",
        "english": "— Do you want something light and tasty for dinner? — Yes, I only want a yogurt with honey and walnuts.",
        "notes": "Review Unit 108. Indefinite pronoun 'κάτι' with taste adjectives.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Έχεις τίποτα άλλο στο ψυγείο; — Όχι, δεν έχω τίποτα άλλο, πρέπει να πάμε για ψώνια.",
        "example_en": "— Do you have anything else in the fridge? — No, I don't have anything else, we must go shopping.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Expressing desire for light meals using indefinite pronouns"
    },
    {
        "id": "A1-U108C-049",
        "greek": "— Ποιο είναι το αγαπημένο σου ελληνικό φαγητό; — Το αγαπημένο μου φαγητό είναι το σουβλάκι και η χωριάτικη σαλάτα.",
        "phonetic_hint": "— PYO EE-neh toh ah-ghah-pee-MEH-noh soo eh-lee-nee-KOH fah-yee-TOH? — Toh ah-ghah-pee-MEH-noh moo fah-yee-TOH EE-neh toh soov-LAH-kee keh ee khoh-RYAH-tee-kee sah-LAH-tah.",
        "english": "— What is your favorite Greek dish? — My favorite dish is souvlaki and Greek salad.",
        "notes": "Review Unit 108. CEFR A1 standard exam personal preference question.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Σου αρέσει η ελληνική κουζίνα; — Ναι, μου αρέσει πάρα πολύ γιατί έχει φρέσκα υλικά.",
        "example_en": "— Do you like Greek cuisine? — Yes, I like it very much because it has fresh ingredients.",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Stating personal culinary preferences in A1 oral interviews"
    },
    {
        "id": "A1-U108C-050",
        "greek": "— Στην υγεία μας, παιδιά! — Στην υγεία σου, να είμαστε πάντα καλά!",
        "phonetic_hint": "— Steen ee-YEE-ah mahs, peh-THYAH! — Steen ee-YEE-ah soo, nah EE-mah-steh PAHN-dah kah-LAH!",
        "english": "— Cheers to our health, everyone! — Cheers to your health, may we always be well!",
        "notes": "Review Unit 108. Traditional table toast ('στην υγεία μας').",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Να είμαστε πάντα καλά στο τραπέζι! — Ευχαριστούμε πολύ, επίσης σε όλους!",
        "example_en": "— May we always be well at the table! — Thank you very much, likewise to everyone!",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Making traditional table toasts and dining wishes at social meals"
    }
]

lesson_u108c = {
    "unit_id": "unit-108c",
    "lesson_id": "lesson-01",
    "title": "Ενότητα 8: Διάλογοι & Εξετάσεις — Φαγητό, Ταβέρνα, Αγορά & Συνταγές (A1 Synthesis)",
    "description": "Conversational, dialogue, and CEFR A1 oral exam practice focusing on food markets, grocery shopping, ordering in tavernas and cafes, recipes and cooking instructions, dietary preferences, and expressing quantities using vocabulary from Lessons 100 to 108.",
    "lesson_status": "not_started",
    "entries": cards_u108c
}

def verify_vocabulary():
    print(f"Loading vocabulary from {len(units_108)} prerequisite units...")
    known = set()
    for u in units_108:
        p = CONTENT_DIR / u / "lesson-01.yaml"
        if p.exists():
            data = yaml.safe_load(p.read_text(encoding="utf-8"))
            for entry in data.get("entries", []):
                texts = [entry.get("greek", ""), entry.get("example_el", "")]
                ginfo = entry.get("grammatical_info", {})
                if isinstance(ginfo, dict):
                    for val in ginfo.values():
                        if isinstance(val, str):
                            texts.append(val)
                for t in texts:
                    for w in re.findall(r"[\u0370-\u03ff\u1f00-\u1fff]+", t):
                        nw = unicodedata.normalize("NFC", w.strip().lower())
                        nw = re.sub(r"[^\w]", "", nw, flags=re.UNICODE)
                        if nw:
                            known.add(nw)

    errs = []
    for c in cards_u108c:
        cid = c["id"]
        for f in ["greek", "example_el"]:
            t = c[f]
            words = re.findall(r"[\u0370-\u03ff\u1f00-\u1fff]+", t)
            un = []
            for w in words:
                nw = unicodedata.normalize("NFC", w.strip().lower())
                nw = re.sub(r"[^\w]", "", nw, flags=re.UNICODE)
                if nw and nw not in known and nw not in allowed_fillers:
                    un.append(w)
            if un:
                errs.append((cid, f, un))
    return errs

def main():
    print("=== Validating Unit 108c Vocabulary Compliance ===")
    errs = verify_vocabulary()
    if errs:
        print(f"CRITICAL: Found {len(errs)} vocabulary errors:")
        for cid, f, un in errs:
            print(f"  {cid} {f}: {un}")
        sys.exit(1)
    print(f"SUCCESS: All {len(cards_u108c)} cards are 100% compliant with vocabulary from Lessons 100-108!")

    print(f"Writing {len(cards_u108c)} cards to {YAML_PATH}...")
    with open(YAML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(lesson_u108c, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("YAML successfully saved!")

    # Update manifest.yaml
    print(f"Checking {MANIFEST_PATH} for unit-108c entry...")
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    units = manifest.get("units", [])
    existing = next((u for u in units if u.get("id") == "unit-108c"), None)

    unit_108c_entry = {
        "id": "unit-108c",
        "title": "Κλικ στα Ελληνικά Α1: Σελίδες 175-194 (Ενότητα 8: Από τον μανάβη στο πιάτο μας! - Διάλογοι, Εξετάσεις & Συνομιλίες)",
        "order": "KlikA1-08-C",
        "is_expansion": True,
        "expansion_of": "KlikA1-08-A",
        "lessons": [
            {
                "id": "lesson-01",
                "file": "unit-108c/lesson-01.yaml",
                "title": "Ενότητα 8: Διάλογοι & Εξετάσεις — Φαγητό, Ταβέρνα, Αγορά & Συνταγές (A1 Synthesis)",
                "description": "Conversational, dialogue, and CEFR A1 oral exam practice focusing on food markets, grocery shopping, ordering in tavernas and cafes, recipes and cooking instructions, dietary preferences, and expressing quantities using vocabulary from Lessons 100 to 108."
            }
        ]
    }

    if existing:
        print("Updating existing unit-108c in manifest.yaml...")
        idx = units.index(existing)
        units[idx] = unit_108c_entry
    else:
        # Find unit-108b
        u108b_idx = next((i for i, u in enumerate(units) if u.get("id") == "unit-108b"), None)
        if u108b_idx is not None:
            print(f"Inserting unit-108c directly after unit-108b (index {u108b_idx + 1})...")
            units.insert(u108b_idx + 1, unit_108c_entry)
        else:
            print("Appending unit-108c to manifest.yaml...")
            units.append(unit_108c_entry)

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("Manifest successfully updated with unit-108c!")

if __name__ == "__main__":
    main()

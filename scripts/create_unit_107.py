# -*- coding: utf-8 -*-
"""
Script to create Unit 107 from Klik A1 (Pages 133-150):
Ενότητα 6: Σπίτι μου, σπιτάκι μου - Βασικό Λεξιλόγιο
Strictly conforming to docs/LESSON_CREATION_GUIDE.md and the klik-a1-deck-builder skill.
"""
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
UNIT_DIR = CONTENT_DIR / "unit-107"
UNIT_DIR.mkdir(parents=True, exist_ok=True)
YAML_PATH = UNIT_DIR / "lesson-01.yaml"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

cards_u107 = [
    # =========================================================================
    # 1. House & Property Types (pp. 133-134, 137)
    # =========================================================================
    {
        "id": "A1-U107-001",
        "greek": "το σπίτι",
        "phonetic_hint": "to SPEE-tee",
        "english": "house / home",
        "notes": "Klik A1 p. 133. Neuter noun in -ι with plural in -ια. Core thematic noun of Unit 6.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το σπίτι μας έχει τέσσερα δωμάτια και μεγάλο κήπο.",
        "example_en": "Our house has four rooms and a large garden.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα σπίτια",
            "accusative_singular": "το σπίτι"
        },
        "keg_communicative_function": "Identifying residential houses"
    },
    {
        "id": "A1-U107-002",
        "greek": "το διαμέρισμα",
        "phonetic_hint": "to thee-ah-MEH-ree-zmah",
        "english": "apartment / flat",
        "notes": "Klik A1 p. 133. Neuter noun in -μα with plural in -ματα.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Νοικιάζω ένα φωτεινό διαμέρισμα στον τρίτο όροφο.",
        "example_en": "I rent a bright apartment on the third floor.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα διαμερίσματα",
            "accusative_singular": "το διαμέρισμα"
        },
        "keg_communicative_function": "Discussing apartment living"
    },
    {
        "id": "A1-U107-003",
        "greek": "η πολυκατοικία",
        "phonetic_hint": "ee po-lee-kah-tee-KEE-ah",
        "english": "apartment building / block of flats",
        "notes": "Klik A1 p. 133. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η πολυκατοικία μας έχει έξι ορόφους και καινούργιο ασανσέρ.",
        "example_en": "Our apartment building has six floors and a new elevator.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πολυκατοικίες",
            "accusative_singular": "την πολυκατοικία"
        },
        "keg_communicative_function": "Describing apartment buildings"
    },
    {
        "id": "A1-U107-004",
        "greek": "η μονοκατοικία",
        "phonetic_hint": "ee mo-no-kah-tee-KEE-ah",
        "english": "detached house / single-family house",
        "notes": "Klik A1 p. 133. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Προτιμούν να μένουν σε μονοκατοικία έξω από την πόλη.",
        "example_en": "They prefer to live in a detached house outside the city.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι μονοκατοικίες",
            "accusative_singular": "τη μονοκατοικία"
        },
        "keg_communicative_function": "Contrasting detached houses with apartments"
    },
    {
        "id": "A1-U107-005",
        "greek": "το κτίριο",
        "phonetic_hint": "to KTEE-ree-o",
        "english": "building",
        "notes": "Klik A1 p. 133, 137. Neuter noun in -ιο with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αυτό το κτίριο είναι πολύ παλιό αλλά διατηρητέο.",
        "example_en": "This building is very old but listed as historic.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κτίρια",
            "accusative_singular": "το κτίριο"
        },
        "keg_communicative_function": "Identifying buildings and architectural structures"
    },

    # =========================================================================
    # 2. Rooms & Spaces within the Home (pp. 133-135, 141)
    # =========================================================================
    {
        "id": "A1-U107-006",
        "greek": "το δωμάτιο",
        "phonetic_hint": "to tho-MAH-tee-o",
        "english": "room",
        "notes": "Klik A1 p. 133, 135. Neuter noun in -ιο with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το σπίτι έχει τρία υπνοδωμάτια και ένα μεγάλο δωμάτιο για γραφείο.",
        "example_en": "The house has three bedrooms and a large room for an office.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα δωμάτια",
            "accusative_singular": "το δωμάτιο"
        },
        "keg_communicative_function": "Counting and specifying rooms in a house"
    },
    {
        "id": "A1-U107-007",
        "greek": "το υπνοδωμάτιο",
        "phonetic_hint": "to eep-no-tho-MAH-tee-o",
        "english": "bedroom",
        "notes": "Klik A1 p. 133, 141. Compound neuter noun: ύπνος + δωμάτιο.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το κύριο υπνοδωμάτιο έχει δικό του μπαλκόνι.",
        "example_en": "The master bedroom has its own balcony.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα υπνοδωμάτια",
            "accusative_singular": "το υπνοδωμάτιο"
        },
        "keg_communicative_function": "Specifying bedrooms in floorplans"
    },
    {
        "id": "A1-U107-008",
        "greek": "το σαλόνι",
        "phonetic_hint": "to sah-LO-nee",
        "english": "living room",
        "notes": "Klik A1 p. 133, 134, 141. Neuter noun in -ι with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πίνουμε τον καφέ μας στο σαλόνι με τους φίλους μας.",
        "example_en": "We drink our coffee in the living room with our friends.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα σαλόνια",
            "accusative_singular": "το σαλόνι"
        },
        "keg_communicative_function": "Describing the living room area"
    },
    {
        "id": "A1-U107-009",
        "greek": "το καθιστικό",
        "phonetic_hint": "to kah-thee-stee-KO",
        "english": "sitting room / lounge",
        "notes": "Klik A1 p. 133, 142. Neuter noun in -ο with plural in -α.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το καθιστικό είναι φωτεινό και έχει τζάκι.",
        "example_en": "The sitting room is bright and has a fireplace.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα καθιστικά",
            "accusative_singular": "το καθιστικό"
        },
        "keg_communicative_function": "Naming family sitting areas"
    },
    {
        "id": "A1-U107-010",
        "greek": "η κουζίνα",
        "phonetic_hint": "ee koo-ZEE-nah",
        "english": "kitchen",
        "notes": "Klik A1 p. 133, 134, 141. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μαγειρεύω καθημερινά στην κουζίνα νόστιμα φαγητά.",
        "example_en": "I cook delicious meals daily in the kitchen.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι κουζίνες",
            "accusative_singular": "την κουζίνα"
        },
        "keg_communicative_function": "Identifying kitchen spaces"
    },
    {
        "id": "A1-U107-011",
        "greek": "το μπάνιο",
        "phonetic_hint": "to BAH-nyo",
        "english": "bathroom",
        "notes": "Klik A1 p. 133, 134, 141. Neuter noun in -ιο with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το διαμέρισμα έχει δύο μπάνια, ένα μεγάλο και ένα μικρό.",
        "example_en": "The apartment has two bathrooms, a large one and a small one.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μπάνια",
            "accusative_singular": "το μπάνιο"
        },
        "keg_communicative_function": "Describing bathroom facilities"
    },
    {
        "id": "A1-U107-012",
        "greek": "ο διάδρομος",
        "phonetic_hint": "o thee-AH-thro-mos",
        "english": "corridor / hallway",
        "notes": "Klik A1 p. 141. Masculine noun in -ος with plural in -οι.",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο διάδρομος ενώνει το σαλόνι με τα υπνοδωμάτια.",
        "example_en": "The corridor connects the living room to the bedrooms.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι διάδρομοι",
            "accusative_singular": "τον διάδρομο"
        },
        "keg_communicative_function": "Locating hallways and corridors"
    },
    {
        "id": "A1-U107-013",
        "greek": "το χολ",
        "phonetic_hint": "to khol",
        "english": "entrance hall / foyer / hall",
        "notes": "Klik A1 p. 141. Indeclinable neuter loan noun.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αφήνουμε τα παλτά μας στην κρεμάστρα στο χολ.",
        "example_en": "We leave our coats on the rack in the entrance hall.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα χολ",
            "accusative_singular": "το χολ"
        },
        "keg_communicative_function": "Identifying home entrance hallways"
    },
    {
        "id": "A1-U107-014",
        "greek": "το μπαλκόνι",
        "phonetic_hint": "to bahl-KO-nee",
        "english": "balcony",
        "notes": "Klik A1 p. 134, 142. Neuter noun in -ι with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Καθόμαστε στο μπαλκόνι τα καλοκαιρινά βράδια.",
        "example_en": "We sit on the balcony on summer evenings.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μπαλκόνια",
            "accusative_singular": "το μπαλκόνι"
        },
        "keg_communicative_function": "Describing outdoor balcony spaces"
    },
    {
        "id": "A1-U107-015",
        "greek": "η αυλή",
        "phonetic_hint": "ee ahv-LEE",
        "english": "courtyard / yard",
        "notes": "Klik A1 p. 133, 137, 139. Feminine noun in -η with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η μονοκατοικία έχει μια μεγάλη πλακόστρωτη αυλή.",
        "example_en": "The detached house has a large paved courtyard.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι αυλές",
            "accusative_singular": "την αυλή"
        },
        "keg_communicative_function": "Describing courtyards and enclosed outdoor areas"
    },
    {
        "id": "A1-U107-016",
        "greek": "ο κήπος",
        "phonetic_hint": "o KEE-pos",
        "english": "garden",
        "notes": "Klik A1 p. 133, 134, 137, 142. Masculine noun in -ος with plural in -οι.",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Φυτεύουμε όμορφα λουλούδια και δέντρα στον κήπο.",
        "example_en": "We plant beautiful flowers and trees in the garden.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι κήποι",
            "accusative_singular": "τον κήπο"
        },
        "keg_communicative_function": "Describing house gardens and yards"
    },
    {
        "id": "A1-U107-017",
        "greek": "το πάρκινγκ",
        "phonetic_hint": "to PAHR-keeng",
        "english": "parking space / car park",
        "notes": "Klik A1 p. 134. Indeclinable neuter loan noun.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το διαμέρισμα διαθέτει ιδιωτικό πάρκινγκ στην πιλοτή.",
        "example_en": "The apartment features private parking in the covered ground area.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πάρκινγκ",
            "accusative_singular": "το πάρκινγκ"
        },
        "keg_communicative_function": "Specifying vehicle parking facilities"
    },

    # =========================================================================
    # 3. Structural & Building Components (pp. 133, 137, 140-142)
    # =========================================================================
    {
        "id": "A1-U107-018",
        "greek": "ο όροφος",
        "phonetic_hint": "o O-ro-fos",
        "english": "floor / story",
        "notes": "Klik A1 p. 133, 138, 141. Masculine noun in -ος with plural in -οι.",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το διαμέρισμα βρίσκεται στον δεύτερο όροφο.",
        "example_en": "The apartment is located on the second floor.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι όροφοι",
            "accusative_singular": "τον όροφο"
        },
        "keg_communicative_function": "Indicating building storeys"
    },
    {
        "id": "A1-U107-019",
        "greek": "το ισόγειο",
        "phonetic_hint": "to ee-SO-yee-o",
        "english": "ground floor",
        "notes": "Klik A1 p. 133. Neuter noun in -ο with plural in -α.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Στο ισόγειο της πολυκατοικίας υπάρχει ένα φαρμακείο.",
        "example_en": "On the ground floor of the apartment building there is a pharmacy.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ισόγεια",
            "accusative_singular": "το ισόγειο"
        },
        "keg_communicative_function": "Identifying ground floor levels"
    },
    {
        "id": "A1-U107-020",
        "greek": "η είσοδος",
        "phonetic_hint": "ee EE-so-thos",
        "english": "entrance",
        "notes": "Klik A1 p. 134, 142, 145. Feminine noun in -ος with plural in -οι.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η κεντρική είσοδος της πολυκατοικίας είναι πάντα κλειδωμένη.",
        "example_en": "The main entrance of the apartment building is always locked.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι είσοδοι",
            "accusative_singular": "την είσοδο"
        },
        "keg_communicative_function": "Locating entrances"
    },
    {
        "id": "A1-U107-021",
        "greek": "το ασανσέρ",
        "phonetic_hint": "to ah-sahn-SEHR",
        "english": "elevator / lift",
        "notes": "Klik A1 p. 134. Indeclinable neuter loan noun.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Παίρνουμε το ασανσέρ για να ανέβουμε στον πέμπτο όροφο.",
        "example_en": "We take the elevator to go up to the fifth floor.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ασανσέρ",
            "accusative_singular": "το ασανσέρ"
        },
        "keg_communicative_function": "Navigating elevators"
    },
    {
        "id": "A1-U107-022",
        "greek": "η σκάλα",
        "phonetic_hint": "ee SKAH-lah",
        "english": "stairs / staircase",
        "notes": "Klik A1 p. 133, 145. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ανεβαίνω με τις σκάλες για να γυμνάζομαι.",
        "example_en": "I go up by the stairs to exercise.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι σκάλες",
            "accusative_singular": "τη σκάλα"
        },
        "keg_communicative_function": "Describing stairways"
    },
    {
        "id": "A1-U107-023",
        "greek": "η πόρτα",
        "phonetic_hint": "ee POR-tah",
        "english": "door",
        "notes": "Klik A1 p. 141, 142, 146. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κλείσε την πόρτα του δωματίου, σε παρακαλώ.",
        "example_en": "Close the room door, please.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πόρτες",
            "accusative_singular": "την πόρτα"
        },
        "keg_communicative_function": "Identifying and operating doors"
    },
    {
        "id": "A1-U107-024",
        "greek": "το παράθυρο",
        "phonetic_hint": "to pah-RAH-thee-ro",
        "english": "window",
        "notes": "Klik A1 p. 141, 142, 146. Neuter noun in -ο with plural in -α.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ανοίγω το παράθυρο για να μπει καθαρός αέρας.",
        "example_en": "I open the window to let fresh air in.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα παράθυρα",
            "accusative_singular": "το παράθυρο"
        },
        "keg_communicative_function": "Operating windows"
    },
    {
        "id": "A1-U107-025",
        "greek": "ο τοίχος",
        "phonetic_hint": "o TEE-khos",
        "english": "wall",
        "notes": "Klik A1 p. 141, 145. Masculine noun in -ος with plural in -οι.",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κρεμάμε έναν ωραίο πίνακα στον τοίχο του σαλονιού.",
        "example_en": "We hang a nice painting on the living room wall.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι τοίχοι",
            "accusative_singular": "τον τοίχο"
        },
        "keg_communicative_function": "Describing walls and wall hangings"
    },
    {
        "id": "A1-U107-026",
        "greek": "το πάτωμα",
        "phonetic_hint": "to PAH-to-mah",
        "english": "floor / flooring",
        "notes": "Klik A1 p. 141. Neuter noun in -μα with plural in -ματα.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το ξύλινο πάτωμα στο υπνοδωμάτιο είναι ζεστό.",
        "example_en": "The wooden floor in the bedroom is warm.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πατώματα",
            "accusative_singular": "το πάτωμα"
        },
        "keg_communicative_function": "Referring to floors and floor surfaces"
    },
    {
        "id": "A1-U107-027",
        "greek": "το ταβάνι",
        "phonetic_hint": "to tah-VAH-nee",
        "english": "ceiling",
        "notes": "Klik A1 p. 141. Neuter noun in -ι with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το ταβάνι του παλιού σπιτιού είναι πολύ ψηλό.",
        "example_en": "The ceiling of the old house is very high.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ταβάνια",
            "accusative_singular": "το ταβάνι"
        },
        "keg_communicative_function": "Describing ceilings"
    },
    {
        "id": "A1-U107-028",
        "greek": "το τζάκι",
        "phonetic_hint": "to DZAH-kee",
        "english": "fireplace",
        "notes": "Klik A1 p. 134, 140. Neuter noun in -ι with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ανάβουμε το τζάκι τα κρύα βράδια του χειμώνα.",
        "example_en": "We light the fireplace on cold winter evenings.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα τζάκια",
            "accusative_singular": "το τζάκι"
        },
        "keg_communicative_function": "Talking about fireplaces"
    },

    # =========================================================================
    # 4. Furniture & Home Furnishings (pp. 141-143)
    # =========================================================================
    {
        "id": "A1-U107-029",
        "greek": "το έπιπλο",
        "phonetic_hint": "to EH-pee-plo",
        "english": "piece of furniture / furniture",
        "notes": "Klik A1 p. 141, 149. Neuter noun in -ο with plural in -α.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αγοράσαμε καινούργια έπιπλα για το καινούριο μας σπίτι.",
        "example_en": "We bought new furniture for our new home.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα έπιπλα",
            "accusative_singular": "το έπιπλο"
        },
        "keg_communicative_function": "Discussing furniture generally"
    },
    {
        "id": "A1-U107-030",
        "greek": "ο καναπές",
        "phonetic_hint": "o kah-nah-PES",
        "english": "sofa / couch",
        "notes": "Klik A1 p. 141, 142. Masculine noun in -ές with plural in -έδες.",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο καναπές στο σαλόνι είναι μεγάλος και άνετος.",
        "example_en": "The sofa in the living room is large and comfortable.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι καναπέδες",
            "accusative_singular": "τον καναπέ"
        },
        "keg_communicative_function": "Identifying sofas and seating"
    },
    {
        "id": "A1-U107-031",
        "greek": "η πολυθρόνα",
        "phonetic_hint": "ee po-lee-THRO-nah",
        "english": "armchair",
        "notes": "Klik A1 p. 141, 142. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κάθομαι στην αναπαυτική πολυθρόνα και διαβάζω εφημερίδα.",
        "example_en": "I sit in the comfortable armchair and read a newspaper.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πολυθρόνες",
            "accusative_singular": "την πολυθρόνα"
        },
        "keg_communicative_function": "Describing armchairs"
    },
    {
        "id": "A1-U107-032",
        "greek": "το τραπέζι",
        "phonetic_hint": "to trah-PEH-zee",
        "english": "table",
        "notes": "Klik A1 p. 141, 142. Neuter noun in -ι with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Όλη η οικογένεια τρώει μαζί γύρω από το μεγάλο τραπέζι.",
        "example_en": "The whole family eats together around the large table.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα τραπέζια",
            "accusative_singular": "το τραπέζι"
        },
        "keg_communicative_function": "Describing dining and work tables"
    },
    {
        "id": "A1-U107-033",
        "greek": "το τραπεζάκι",
        "phonetic_hint": "to trah-peh-ZAH-kee",
        "english": "coffee table / small table",
        "notes": "Klik A1 p. 141, 143. Diminutive neuter noun in -άκι.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Έχουμε ένα χαμηλό τραπεζάκι σαλονιού μπροστά από τον καναπέ.",
        "example_en": "We have a low coffee table in front of the sofa.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα τραπεζάκια",
            "accusative_singular": "το τραπεζάκι"
        },
        "keg_communicative_function": "Identifying coffee tables and small side tables"
    },
    {
        "id": "A1-U107-034",
        "greek": "η καρέκλα",
        "phonetic_hint": "ee kah-REH-klah",
        "english": "chair",
        "notes": "Klik A1 p. 138, 141, 142. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η τραπεζαρία διαθέτει έξι ξύλινες καρέκλες.",
        "example_en": "The dining area features six wooden chairs.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι καρέκλες",
            "accusative_singular": "την καρέκλα"
        },
        "keg_communicative_function": "Counting and describing chairs"
    },
    {
        "id": "A1-U107-035",
        "greek": "το γραφείο",
        "phonetic_hint": "to grah-FEE-o",
        "english": "desk / study",
        "notes": "Klik A1 p. 141, 142. Neuter noun in -ιο with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μελετάω τα μαθήματά μου πάνω στο γραφείο.",
        "example_en": "I study my lessons at the desk.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα γραφεία",
            "accusative_singular": "το γραφείο"
        },
        "keg_communicative_function": "Identifying study desks"
    },
    {
        "id": "A1-U107-036",
        "greek": "η βιβλιοθήκη",
        "phonetic_hint": "ee veev-lee-o-THEE-kee",
        "english": "bookcase / bookshelf / library",
        "notes": "Klik A1 p. 141, 142, 144. Feminine noun in -η with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η βιβλιοθήκη στο σαλόνι είναι γεμάτη με ελληνικά βιβλία.",
        "example_en": "The bookcase in the living room is full of Greek books.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι βιβλιοθήκες",
            "accusative_singular": "τη βιβλιοθήκη"
        },
        "keg_communicative_function": "Describing bookshelves and storage for books"
    },
    {
        "id": "A1-U107-037",
        "greek": "το κρεβάτι",
        "phonetic_hint": "to kreh-VAH-tee",
        "english": "bed",
        "notes": "Klik A1 p. 141, 142. Neuter noun in -ι with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το υπνοδωμάτιο έχει ένα άνετο διπλό κρεβάτι.",
        "example_en": "The bedroom has a comfortable double bed.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κρεβάτια",
            "accusative_singular": "το κρεβάτι"
        },
        "keg_communicative_function": "Describing beds in bedrooms"
    },
    {
        "id": "A1-U107-038",
        "greek": "το κομοδίνο",
        "phonetic_hint": "to ko-mo-THEE-no",
        "english": "bedside table / nightstand",
        "notes": "Klik A1 p. 141. Neuter noun in -ο with plural in -α.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Έχω ένα μικρό φωτιστικό πάνω στο κομοδίνο μου.",
        "example_en": "I have a small lamp on my bedside table.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κομοδίνα",
            "accusative_singular": "το κομοδίνο"
        },
        "keg_communicative_function": "Identifying nightstands"
    },
    {
        "id": "A1-U107-039",
        "greek": "η ντουλάπα",
        "phonetic_hint": "ee doo-LAH-pah",
        "english": "wardrobe / closet",
        "notes": "Klik A1 p. 134, 141, 143. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κρεμάω όλα τα ρούχα μου μέσα στη ντουλάπα.",
        "example_en": "I hang all my clothes inside the wardrobe.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ντουλάπες",
            "accusative_singular": "τη ντουλάπα"
        },
        "keg_communicative_function": "Describing clothing closets and wardrobes"
    },
    {
        "id": "A1-U107-040",
        "greek": "το συρτάρι",
        "phonetic_hint": "to seer-TAH-ree",
        "english": "drawer",
        "notes": "Klik A1 p. 142. Neuter noun in -ι with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βάζω τα κλειδιά και τα έγγραφα μέσα στο συρτάρι.",
        "example_en": "I put the keys and the documents inside the drawer.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα συρτάρια",
            "accusative_singular": "το συρτάρι"
        },
        "keg_communicative_function": "Locating items in drawers"
    },

    # =========================================================================
    # 5. Appliances, Utilities & Fixtures (pp. 140-142)
    # =========================================================================
    {
        "id": "A1-U107-041",
        "greek": "το ψυγείο",
        "phonetic_hint": "to psee-YEE-o",
        "english": "refrigerator / fridge",
        "notes": "Klik A1 p. 141, 142. Neuter noun in -ιο with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βάζω το γάλα και τα φρούτα μέσα στο ψυγείο.",
        "example_en": "I put the milk and the fruit inside the fridge.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ψυγεία",
            "accusative_singular": "το ψυγείο"
        },
        "keg_communicative_function": "Naming kitchen refrigeration appliances"
    },
    {
        "id": "A1-U107-042",
        "greek": "η ηλεκτρική κουζίνα",
        "phonetic_hint": "ee ee-lek-tree-KEE koo-ZEE-nah",
        "english": "electric stove / cooker",
        "notes": "Klik A1 p. 141, 142. Feminine noun phrase: επίθετο + ουσιαστικό.",
        "gender_or_pos": "noun phrase (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η καινούργια ηλεκτρική κουζίνα έχει κεραμικές εστίες.",
        "example_en": "The new electric cooker has ceramic hobs.",
        "grammatical_info": {
            "part_of_speech": "noun phrase (feminine)",
            "plural": "οι ηλεκτρικές κουζίνες",
            "accusative_singular": "την ηλεκτρική κουζίνα"
        },
        "keg_communicative_function": "Identifying kitchen stoves and cooking ranges"
    },
    {
        "id": "A1-U107-043",
        "greek": "το πλυντήριο ρούχων",
        "phonetic_hint": "to pleen-TEE-ree-o ROO-khon",
        "english": "washing machine",
        "notes": "Klik A1 p. 141, 142. Neuter noun phrase: ουσιαστικό + γενική πληθυντικού.",
        "gender_or_pos": "noun phrase (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βάζω τα άπλυτα ρούχα στο πλυντήριο ρούχων κάθε Σάββατο.",
        "example_en": "I put the dirty clothes into the washing machine every Saturday.",
        "grammatical_info": {
            "part_of_speech": "noun phrase (neuter)",
            "plural": "τα πλυντήρια ρούχων",
            "accusative_singular": "το πλυντήριο ρούχων"
        },
        "keg_communicative_function": "Naming clothes washing appliances"
    },
    {
        "id": "A1-U107-044",
        "greek": "ο νιπτήρας",
        "phonetic_hint": "o neep-TEE-rahs",
        "english": "washbasin / bathroom sink",
        "notes": "Klik A1 p. 141. Masculine noun in -ας with plural in -ες.",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πλένω τα χέρια μου και το πρόσωπό μου στον νιπτήρα.",
        "example_en": "I wash my hands and face in the washbasin.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι νιπτήρες",
            "accusative_singular": "τον νιπτήρα"
        },
        "keg_communicative_function": "Describing bathroom basins"
    },
    {
        "id": "A1-U107-045",
        "greek": "η μπανιέρα",
        "phonetic_hint": "ee bah-NYEH-rah",
        "english": "bathtub",
        "notes": "Klik A1 p. 141, 142. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κάνω ένα ζεστό χαλαρωτικό αφρόλουτρο στην μπανιέρα.",
        "example_en": "I take a warm relaxing bubble bath in the bathtub.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι μπανιέρες",
            "accusative_singular": "την μπανιέρα"
        },
        "keg_communicative_function": "Describing bathtubs in bathrooms"
    },
    {
        "id": "A1-U107-046",
        "greek": "η βρύση",
        "phonetic_hint": "ee VREE-see",
        "english": "tap / faucet",
        "notes": "Klik A1 p. 141, 142. Feminine noun in -η with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κλείσε καλά τη βρύση για να μην τρέχει νερό.",
        "example_en": "Turn off the tap tightly so water doesn't drip.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι βρύσες",
            "accusative_singular": "τη βρύση"
        },
        "keg_communicative_function": "Operating water faucets"
    },
    {
        "id": "A1-U107-047",
        "greek": "το καλοριφέρ",
        "phonetic_hint": "to kah-lo-ree-FEHR",
        "english": "radiator / central heating",
        "notes": "Klik A1 p. 140. Indeclinable neuter loan noun.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τον χειμώνα ανάβουμε το καλοριφέρ για να ζεσταθεί το σπίτι.",
        "example_en": "In winter we turn on the radiator to warm up the house.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα καλοριφέρ",
            "accusative_singular": "το καλοριφέρ"
        },
        "keg_communicative_function": "Operating radiators and central heating"
    },
    {
        "id": "A1-U107-048",
        "greek": "το κλιματιστικό",
        "phonetic_hint": "to klee-mah-tee-stee-KO",
        "english": "air conditioner / A/C",
        "notes": "Klik A1 p. 140. Neuter noun in -ο with plural in -α.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ανάβω το κλιματιστικό γιατί έχει αφόρητη ζέστη.",
        "example_en": "I turn on the air conditioner because it is unbearably hot.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κλιματιστικά",
            "accusative_singular": "το κλιματιστικό"
        },
        "keg_communicative_function": "Operating climate control and air conditioning"
    },
    {
        "id": "A1-U107-049",
        "greek": "ο θερμοσίφωνας",
        "phonetic_hint": "o ther-mo-SEE-fo-nahs",
        "english": "water heater / boiler",
        "notes": "Klik A1 p. 140. Masculine noun in -ας with plural in -ες.",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ανάβω τον θερμοσίφωνα για να έχουμε ζεστό νερό.",
        "example_en": "I turn on the water heater so we have hot water.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι θερμοσίφωνες",
            "accusative_singular": "τον θερμοσίφωνα"
        },
        "keg_communicative_function": "Managing water heating"
    },
    {
        "id": "A1-U107-050",
        "greek": "η τηλεόραση",
        "phonetic_hint": "ee tee-leh-O-rah-see",
        "english": "television / TV",
        "notes": "Klik A1 p. 141, 143. Feminine noun in -ση with plural in -σεις.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βλέπουμε μια ταινία στην τηλεόραση μετά το βραδινό.",
        "example_en": "We watch a movie on the television after dinner.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι τηλεοράσεις",
            "accusative_singular": "την τηλεόραση"
        },
        "keg_communicative_function": "Naming television sets"
    },
    {
        "id": "A1-U107-051",
        "greek": "το φωτιστικό",
        "phonetic_hint": "to foh-tee-stee-KO",
        "english": "light fixture / lamp",
        "notes": "Klik A1 p. 143. Neuter noun in -ο with plural in -α.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το μοντέρνο φωτιστικό δίνει ζεστό φως στο σαλόνι.",
        "example_en": "The modern light fixture casts a warm light in the living room.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα φωτιστικά",
            "accusative_singular": "το φωτιστικό"
        },
        "keg_communicative_function": "Describing lamps and light fixtures"
    },
    {
        "id": "A1-U107-052",
        "greek": "το χαλί",
        "phonetic_hint": "to khah-LEE",
        "english": "carpet / rug",
        "notes": "Klik A1 p. 144. Neuter noun in -ι with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Στρώνουμε ζεστά χαλιά στο σπίτι το φθινόπωρο.",
        "example_en": "We lay warm carpets in the house in the autumn.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα χαλιά",
            "accusative_singular": "το χαλί"
        },
        "keg_communicative_function": "Talking about carpets and rugs"
    },
    {
        "id": "A1-U107-053",
        "greek": "η κουρτίνα",
        "phonetic_hint": "ee koor-TEE-nah",
        "english": "curtain",
        "notes": "Klik A1 p. 141. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ανοίγω τις κουρτίνες για να μπει το πρωινό φως.",
        "example_en": "I open the curtains to let the morning light in.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι κουρτίνες",
            "accusative_singular": "την κουρτίνα"
        },
        "keg_communicative_function": "Operating window curtains"
    },
    {
        "id": "A1-U107-054",
        "greek": "ο καθρέφτης",
        "phonetic_hint": "o kah-THREHF-tees",
        "english": "mirror",
        "notes": "Klik A1 p. 144. Masculine noun in -ης with plural in -ες.",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Υπάρχει ένας μεγάλος καθρέφτης πάνω από τον νιπτήρα στο μπάνιο.",
        "example_en": "There is a large mirror above the sink in the bathroom.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι καθρέφτες",
            "accusative_singular": "τον καθρέφτη"
        },
        "keg_communicative_function": "Describing mirrors in home decor"
    },

    # =========================================================================
    # 6. Real Estate, Leasing & Neighborhood (pp. 133-136, 140)
    # =========================================================================
    {
        "id": "A1-U107-055",
        "greek": "το ενοίκιο",
        "phonetic_hint": "to eh-NEE-kee-o",
        "english": "rent",
        "notes": "Klik A1 p. 133, 140. Neuter noun in -ιο with plural in -ια.",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πληρώνω το ενοίκιο του διαμερίσματος στην αρχή κάθε μήνα.",
        "example_en": "I pay the apartment rent at the beginning of each month.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ενοίκια",
            "accusative_singular": "το ενοίκιο"
        },
        "keg_communicative_function": "Discussing rental payments"
    },
    {
        "id": "A1-U107-056",
        "greek": "τα κοινόχρηστα",
        "phonetic_hint": "tah kee-NO-khree-stah",
        "english": "building maintenance fees / shared expenses",
        "notes": "Klik A1 p. 140, 141. Neuter noun used only in plural (plurale tantum).",
        "gender_or_pos": "noun (neuter)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τα κοινόχρηστα της πολυκατοικίας περιλαμβάνουν τη θέρμανση και τον καθαρισμό.",
        "example_en": "Building maintenance fees include heating and cleaning.",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κοινόχρηστα",
            "accusative_singular": "τα κοινόχρηστα"
        },
        "keg_communicative_function": "Inquiring about building shared expenses"
    },
    {
        "id": "A1-U107-057",
        "greek": "η αγγελία",
        "phonetic_hint": "ee ahg-yeh-LEE-ah",
        "english": "advertisement / classified ad",
        "notes": "Klik A1 p. 133, 134, 136. Feminine noun in -α with plural in -ες.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Διαβάζω τις μικρές αγγελίες στην εφημερίδα για να βρω σπίτι.",
        "example_en": "I read the classified ads in the newspaper to find a house.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι αγγελίες",
            "accusative_singular": "την αγγελία"
        },
        "keg_communicative_function": "Reading and placing property classified ads"
    },
    {
        "id": "A1-U107-058",
        "greek": "η γειτονιά",
        "phonetic_hint": "ee yee-to-NYAH",
        "english": "neighborhood",
        "notes": "Klik A1 p. 133, 137, 140. Feminine noun in -ιά with plural in -ιές.",
        "gender_or_pos": "noun (feminine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η γειτονιά μας είναι πολύ ήσυχη και έχει πολλά δέντρα.",
        "example_en": "Our neighborhood is very quiet and has many trees.",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι γειτονιές",
            "accusative_singular": "τη γειτονιά"
        },
        "keg_communicative_function": "Describing local neighborhoods"
    },
    {
        "id": "A1-U107-059",
        "greek": "ο γείτονας",
        "phonetic_hint": "o YEE-to-nahs",
        "english": "neighbor",
        "notes": "Klik A1 p. 137, 139. Masculine noun in -ας with plural in -ες. Fem: η γειτόνισσα.",
        "gender_or_pos": "noun (masculine)",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο διπλανός γείτονας είναι πολύ ευγενικός και εξυπηρετικός.",
        "example_en": "The next-door neighbor is very polite and helpful.",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι γείτονες",
            "accusative_singular": "τον γείτονα"
        },
        "keg_communicative_function": "Talking about neighbors"
    },

    # =========================================================================
    # 7. Descriptive Adjectives & Housekeeping Verbs (pp. 133, 137, 144, 146)
    # =========================================================================
    {
        "id": "A1-U107-060",
        "greek": "φωτεινός",
        "phonetic_hint": "foh-tee-NOS",
        "english": "bright / luminous",
        "notes": "Klik A1 p. 133, 137. Adjective in -ός, -ή, -ό.",
        "gender_or_pos": "adjective",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το σαλόνι είναι ιδιαίτερα φωτεινό χάρη στα μεγάλα παράθυρα.",
        "example_en": "The living room is especially bright thanks to the large windows.",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "forms": "φωτεινός, -ή, -ό"
        },
        "keg_communicative_function": "Describing lighting qualities of rooms"
    },
    {
        "id": "A1-U107-061",
        "greek": "ήσυχος",
        "phonetic_hint": "EE-see-khos",
        "english": "quiet / peaceful",
        "notes": "Klik A1 p. 133, 137. Adjective in -ος, -η, -ο.",
        "gender_or_pos": "adjective",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ψάχνουμε ένα ήσυχο διαμέρισμα μακριά από τον θόρυβο των δρόμων.",
        "example_en": "We are looking for a quiet apartment away from street noise.",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "forms": "ήσυχος, -η, -ο"
        },
        "keg_communicative_function": "Evaluating residential tranquility"
    },
    {
        "id": "A1-U107-062",
        "greek": "καθαρίζω",
        "phonetic_hint": "kah-thah-REE-zo",
        "english": "I clean",
        "notes": "Klik A1 p. 144, 146. Type A regular verb. Imperative: καθάρισε! / καθαρίστε!",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Καθαρίζω το σπίτι κάθε Σάββατο πρωί.",
        "example_en": "I clean the house every Saturday morning.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A (active regular)",
            "third_person_singular": "καθαρίζει",
            "first_person_plural": "καθαρίζουμε"
        },
        "keg_communicative_function": "Talking about home cleaning routines"
    },
    {
        "id": "A1-U107-063",
        "greek": "τακτοποιώ",
        "phonetic_hint": "tahk-to-pee-O",
        "english": "I tidy up / arrange / organize",
        "notes": "Klik A1 p. 146, 148. Type B2 contract verb (-ώ, -είς, -εί). Imperative: τακτοποίησε! / τακτοποιήστε!",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τακτοποιώ τα ρούχα και τα βιβλία στο δωμάτιό μου.",
        "example_en": "I tidy up the clothes and the books in my room.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type B2 (contract)",
            "third_person_singular": "τακτοποιεί",
            "first_person_plural": "τακτοποιούμε"
        },
        "keg_communicative_function": "Tidying up rooms and belongings"
    },
    {
        "id": "A1-U107-064",
        "greek": "ανάβω",
        "phonetic_hint": "ah-NAH-vo",
        "english": "I turn on / switch on / light",
        "notes": "Klik A1 p. 146. Type A verb. Dependent/Imperative stem: άναψε! / ανάψτε!",
        "gender_or_pos": "verb",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ανάβω το φως μόλις μπαίνω στο σπίτι.",
        "example_en": "I turn on the light as soon as I enter the house.",
        "grammatical_info": {
            "part_of_speech": "verb",
            "verb_type": "Type A (active regular)",
            "third_person_singular": "ανάβει",
            "first_person_plural": "ανάβουμε"
        },
        "keg_communicative_function": "Operating household lights and appliances"
    }
]

lesson_u107 = {
    "unit_id": "unit-107",
    "lesson_id": "lesson-01",
    "title": "Ενότητα 6: Σπίτι μου, σπιτάκι μου — Βασικό Λεξιλόγιο (Pages 133-150)",
    "description": "CEFR A1: Housing and property types, rooms and structural components, furniture and appliances, real estate terminology, and housekeeping verbs from Klik A1 (Pages 133-150).",
    "lesson_status": "not_started",
    "lesson_notes": (
        "Κλικ στα Ελληνικά Α1 — Ενότητα 6: Σπίτι μου, σπιτάκι μου (Σελίδες 133-150):\n"
        "• Τύποι Κατοικίας & Κτίρια (Housing & Property Types):\n"
        "  - το σπίτι, το διαμέρισμα, η πολυκατοικία, η μονοκατοικία, το κτίριο.\n"
        "• Χώροι & Δωμάτια του Σπιτιού (Rooms & Spaces):\n"
        "  - το δωμάτιο, το υπνοδωμάτιο, το σαλόνι, το καθιστικό, η κουζίνα, το μπάνιο.\n"
        "  - ο διάδρομος, το χολ, το μπαλκόνι, η αυλή, ο κήπος, το πάρκινγκ.\n"
        "• Δομικά Στοιχεία & Υποδομές (Building Components):\n"
        "  - ο όροφος, το ισόγειο, η είσοδος, το ασανσέρ, η σκάλα, η πόρτα, το παράθυρο.\n"
        "  - ο τοίχος, το πάτωμα, το ταβάνι, το τζάκι.\n"
        "• Έπιπλα & Οικιακός Εξοπλισμός (Furniture & Furnishings):\n"
        "  - το έπιπλο, ο καναπές, η πολυθρόνα, το τραπέζι, το τραπεζάκι, η καρέκλα.\n"
        "  - το γραφείο, η βιβλιοθήκη, το κρεβάτι, το κομοδίνο, η ντουλάπα, το συρτάρι.\n"
        "• Ηλεκτρικές Συσκευές & Εγκαταστάσεις (Appliances & Utilities):\n"
        "  - το ψυγείο, η ηλεκτρική κουζίνα, το πλυντήριο ρούχων, ο νιπτήρας, η μπανιέρα, η βρύση.\n"
        "  - το καλοριφέρ, το κλιματιστικό, ο θερμοσίφωνας, η τηλεόραση, το φωτιστικό, το χαλί, η κουρτίνα, ο καθρέφτης.\n"
        "• Ενοικίαση & Γειτονιά (Real Estate & Neighborhood):\n"
        "  - το ενοίκιο, τα κοινόχρηστα, η αγγελία, η γειτονιά, ο γείτονας.\n"
        "• Επίθετα & Ρήματα Κατοικίας (Adjectives & Housekeeping Verbs):\n"
        "  - φωτεινός, ήσυχος, καθαρίζω, τακτοποιώ, ανάβω."
    ),
    "entries": cards_u107
}

def main():
    print(f"Writing {len(cards_u107)} cards to {YAML_PATH}...")
    with open(YAML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(lesson_u107, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("YAML successfully written.")

    # Update manifest.yaml
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    units = manifest.get("units", [])
    existing = next((u for u in units if u.get("id") == "unit-107"), None)
    unit_107_entry = {
        "id": "unit-107",
        "title": "Κλικ στα Ελληνικά Α1: Σελίδες 133-150 (Ενότητα 6: Σπίτι μου, σπιτάκι μου - Λεξιλόγιο)",
        "order": "KlikA1-07-A",
        "lessons": [
            {
                "id": "lesson-01",
                "file": "unit-107/lesson-01.yaml",
                "title": "Ενότητα 6: Σπίτι μου, σπιτάκι μου — Βασικό Λεξιλόγιο (Pages 133-150)"
            }
        ]
    }

    if existing:
        print("Updating existing unit-107 in manifest.yaml...")
        idx = units.index(existing)
        units[idx] = unit_107_entry
    else:
        print("Appending unit-107 to manifest.yaml...")
        units.append(unit_107_entry)

    manifest["units"] = units

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("Manifest successfully updated with unit-107!")

if __name__ == "__main__":
    main()

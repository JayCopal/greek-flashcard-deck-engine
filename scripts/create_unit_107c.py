# -*- coding: utf-8 -*-
"""
Script to create Unit 107 C from Klik A1 (Pages 133-150):
Ενότητα 6: Σπίτι μου, σπιτάκι μου - Διάλογοι, Εξετάσεις & Συνομιλίες
Focuses on conversational dialogues, apartment hunting, rental inquiries and costs,
roommate life, household instructions (imperative mood), prohibitions, and
home life exchanges using exclusively vocabulary from Lessons 101 to 107.
"""
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
UNIT_DIR = CONTENT_DIR / "unit-107c"
UNIT_DIR.mkdir(parents=True, exist_ok=True)
YAML_PATH = UNIT_DIR / "lesson-01.yaml"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

cards_u107c = [
    # =========================================================================
    # Part 1: Real Estate Ads & Apartment Search (Cards 001 - 010)
    # =========================================================================
    {
        "id": "A1-U107C-001",
        "greek": "— Γεια σας, είναι για την αγγελία του σπιτιού. — Ναι, μάλιστα, είναι ελεύθερο το διαμέρισμα.",
        "phonetic_hint": "YAH sahs, EE-neh yah teen ahng-geh-LEE-ah too spee-TYOO. — Neh, MAH-lee-stah, EE-neh eh-LEF-the-ro to thee-ah-MEH-ree-zmah.",
        "english": "— Hello, this is regarding the house advertisement. — Yes, certainly, the apartment is available.",
        "notes": "Review Unit 107. Real estate telephone inquiry responding to a classified ad ('αγγελία').",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Είδα την αγγελία σας. Είναι ελεύθερο το σπίτι; — Ναι, είναι ελεύθερο.",
        "example_en": "— I saw your advertisement. Is the house available? — Yes, it is available.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about classified housing advertisements and property availability"
    },
    {
        "id": "A1-U107C-002",
        "greek": "— Σε ποιον όροφο βρίσκεται το διαμέρισμα; — Βρίσκεται στον δεύτερο όροφο.",
        "phonetic_hint": "seh PYO-n OH-ro-fo VREES-keh-teh to thee-ah-MEH-ree-zmah? — VREES-keh-teh ston THEHF-teh-ro OH-ro-fo.",
        "english": "— On which floor is the apartment located? — It is located on the second floor.",
        "notes": "Review Units 103 & 107. Specifying building floors using masculine accusative ordinal numbers.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Σε ποιον όροφο μένετε; — Μένουμε στον τρίτο όροφο της πολυκατοικίας.",
        "example_en": "— On which floor do you live? — We live on the third floor of the apartment building.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking and answering about apartment floor levels in multi-story buildings"
    },
    {
        "id": "A1-U107C-003",
        "greek": "— Πόσα δωμάτια έχει το σπίτι; — Έχει δύο υπνοδωμάτια, σαλόνι, κουζίνα και δύο μπάνια.",
        "phonetic_hint": "POH-sah tho-MAH-tyah EH-khee to SPEE-tee? — EH-khee THEE-o eep-no-tho-MAH-tyah, sah-LOH-nee, koo-ZEE-nah keh THEE-o MPAH-nyah.",
        "english": "— How many rooms does the house have? — It has two bedrooms, a living room, a kitchen, and two bathrooms.",
        "notes": "Review Unit 107. Inquiring about room layout and internal house distribution.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Είναι μεγάλο το σπίτι; — Ναι, είναι εκατό τετραγωνικών μέτρων με μεγάλα δωμάτια.",
        "example_en": "— Is the house large? — Yes, it is one hundred square meters with large rooms.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing apartment layout, room counts, and surface area"
    },
    {
        "id": "A1-U107C-004",
        "greek": "— Είναι φωτεινό και ήσυχο το διαμέρισμα; — Ναι, είναι πολύ φωτεινό και ήσυχο.",
        "phonetic_hint": "EE-neh fo-tee-NOH keh EE-see-kho to thee-ah-MEH-ree-zmah? — Neh, EE-neh po-LEE fo-tee-NOH keh EE-see-kho.",
        "english": "— Is the apartment bright and quiet? — Yes, it is very bright and quiet.",
        "notes": "Review Unit 107. Key housing adjectives 'φωτεινός' and 'ήσυχος' in the neuter nominative.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Μένεις σε ήσυχη γειτονιά; — Ναι, η γειτονιά μας είναι πολύ ήσυχη.",
        "example_en": "— Do you live in a quiet neighborhood? — Yes, our neighborhood is very quiet.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Assessing living comfort, natural daylight, and acoustic tranquility"
    },
    {
        "id": "A1-U107C-005",
        "greek": "— Έχει μπαλκόνι το σπίτι; — Ναι, το μπαλκόνι είναι πολύ μεγάλο με θέα στο πάρκο.",
        "phonetic_hint": "EH-khee mpal-KOH-nee to SPEE-tee? — Neh, to mpal-KOH-nee EE-neh po-LEE meh-GHAH-lo meh THEH-ah sto PAHR-ko.",
        "english": "— Does the house have a balcony? — Yes, the balcony is very large with a view of the park.",
        "notes": "Review Unit 107. Inquiring about outdoor spaces and park views.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Βλέπει στον κήπο το μπαλκόνι; — Ναι, βλέπει στην αυλή και στον κήπο.",
        "example_en": "— Does the balcony face the garden? — Yes, it overlooks the courtyard and the garden.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about balconies, outdoor views, and exterior spaces"
    },
    {
        "id": "A1-U107C-006",
        "greek": "— Πού είναι η πολυκατοικία; — Είναι κοντά στο πανεπιστήμιο και στον σταθμό του μετρό.",
        "phonetic_hint": "poo EE-neh ee po-lee-kah-tee-KEE-ah? — EE-neh kon-DAH sto pah-neh-pee-STEE-mee-o keh ston stahth-MOH too meh-TROH.",
        "english": "— Where is the apartment building? — It is near the university and the metro station.",
        "notes": "Review Units 103 & 107. Locating residential properties relative to public transport and campus.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Υπάρχει στάση λεωφορείου μπροστά από την πολυκατοικία; — Ναι, υπάρχει στάση.",
        "example_en": "— Is there a bus stop in front of the apartment building? — Yes, there is a stop.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing property location and access to urban transit"
    },
    {
        "id": "A1-U107C-007",
        "greek": "— Το διαμέρισμα είναι επιπλωμένο; — Ναι, είναι πλήρως επιπλωμένο και έχει όλες τις ηλεκτρικές συσκευές.",
        "phonetic_hint": "to thee-ah-MEH-ree-zmah EE-neh eh-pee-plo-MEH-no? — Neh, EE-neh PLEE-ros eh-pee-plo-MEH-no keh EH-khee OH-lehs tees ee-lek-tree-KEHS see-skeh-VEHS.",
        "english": "— Is the apartment furnished? — Yes, it is fully furnished and has all electrical appliances.",
        "notes": "Review Unit 107. Property condition: 'πλήρως επιπλωμένο' with modern household appliances.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Έχει ψυγείο και πλυντήριο; — Ναι, έχει ψυγείο, πλυντήριο ρούχων και ηλεκτρική κουζίνα.",
        "example_en": "— Does it have a fridge and a washing machine? — Yes, it has a fridge, washing machine, and electric cooker.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Checking furnishing status and included household appliances"
    },
    {
        "id": "A1-U107C-008",
        "greek": "— Μπορείτε να δείτε το διαμέρισμα σήμερα; — Βεβαίως, ελάτε το απόγευμα στις έξι.",
        "phonetic_hint": "bo-REE-teh nah THEE-teh to thee-ah-MEH-ree-zmah SEE-meh-rah? — veh-VEH-os, eh-LAH-teh to ah-POH-yev-mah stees EH-ksee.",
        "english": "— Can you view the apartment today? — Certainly, come this afternoon at six.",
        "notes": "Review Units 106 & 107. Arranging property viewings with polite imperative 'ελάτε'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Περάστε μέσα στο σπίτι να το δείτε! — Ευχαριστώ, περνάμε αμέσως.",
        "example_en": "— Step inside the house to see it! — Thank you, we are coming right in.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Scheduling and attending property inspection appointments"
    },
    {
        "id": "A1-U107C-009",
        "greek": "— Η πολυκατοικία έχει ασανσέρ; — Ναι, η πολυκατοικία είναι καινούργια και διαθέτει σύγχρονο ασανσέρ.",
        "phonetic_hint": "ee po-lee-kah-tee-KEE-ah EH-khee ah-sahn-SEHR? — Neh, ee po-lee-kah-tee-KEE-ah EE-neh keh-NOOR-gyah keh thee-ah-THEH-tee SEEN-khro-no ah-sahn-SEHR.",
        "english": "— Does the apartment building have an elevator? — Yes, the building is new and features a modern elevator.",
        "notes": "Review Unit 107. Inquiring about building infrastructure and elevator facilities.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πού είναι η σκάλα; — Η σκάλα είναι δίπλα στην είσοδο.",
        "example_en": "— Where are the stairs? — The staircase is next to the entrance.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Verifying elevator availability and building accessibility"
    },
    {
        "id": "A1-U107C-010",
        "greek": "— Υπάρχει πάρκινγκ στην πολυκατοικία; — Ναι, το σπίτι διαθέτει πάρκινγκ για το αυτοκίνητο.",
        "phonetic_hint": "ee-PAHR-khee PAHR-keengk steen po-lee-kah-tee-KEE-ah? — Neh, to SPEE-tee thee-ah-THEH-tee PAHR-keengk yah to af-to-KEE-nee-to.",
        "english": "— Is there parking in the apartment building? — Yes, the house features parking for the car.",
        "notes": "Review Unit 107. Asking about dedicated vehicle parking spots in apartment blocks.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Έχει χώρο για το αυτοκίνητο; — Ναι, έχει πάρκινγκ.",
        "example_en": "— Does it have space for the car? — Yes, it has parking.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Confirming parking space availability for tenant vehicles"
    },

    # =========================================================================
    # Part 2: Rent, Utilities, Heating & Living Costs (Cards 011 - 018)
    # =========================================================================
    {
        "id": "A1-U107C-011",
        "greek": "— Πόσο είναι το μηνιαίο ενοίκιο; — Το ενοίκιο είναι τετρακόσια πενήντα ευρώ τον μήνα.",
        "phonetic_hint": "POH-so EE-neh to mee-nee-EH-o eh-NEE-kee-o? — To eh-NEE-kee-o EE-neh teh-trah-KOH-syah peh-NEEN-dah ev-ROH ton MEE-nah.",
        "english": "— How much is the monthly rent? — The rent is four hundred fifty euros per month.",
        "notes": "Review Unit 107. Inquiring about rental rates using compound numbers and time accusative 'τον μήνα'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πόσο είναι το ενοίκιο για το διαμέρισμα; — Είναι τετρακόσια ευρώ χωρίς τα κοινόχρηστα.",
        "example_en": "— How much is the rent for the apartment? — It is four hundred euros without building fees.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about monthly rental costs and lease conditions"
    },
    {
        "id": "A1-U107C-012",
        "greek": "— Πόσο είναι τα κοινόχρηστα τον μήνα; — Είναι περίπου είκοσι πέντε ευρώ.",
        "phonetic_hint": "POH-so EE-neh tah kee-NOH-khree-stah ton MEE-nah? — EE-neh peh-REE-poo EE-ko-see PEN-deh ev-ROH.",
        "english": "— How much are the building fees per month? — They are approximately twenty-five euros.",
        "notes": "Review Unit 107. Shared building maintenance expenses ('κοινόχρηστα').",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πόσο πληρώνετε για τα κοινόχρηστα τον χειμώνα; — Πληρώνουμε σαράντα ευρώ.",
        "example_en": "— How much do you pay for building fees in the winter? — We pay forty euros.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Calculating shared residential maintenance and utility charges"
    },
    {
        "id": "A1-U107C-013",
        "greek": "— Τι είδους θέρμανση έχει το σπίτι; — Έχει αυτόνομη θέρμανση με φυσικό αέριο.",
        "phonetic_hint": "tee EE-thoos THEHR-mahn-see EH-khee to SPEE-tee? — EH-khee ahf-TOH-no-mee THEHR-mahn-see meh fee-see-KOH ah-EH-ree-o.",
        "english": "— What kind of heating does the house have? — It has autonomous natural gas heating.",
        "notes": "Review Unit 107. Inquiring about home heating systems and natural gas connections.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ανάβει το καλοριφέρ τον χειμώνα; — Ναι, έχουμε ζέστη με αυτόνομη θέρμανση.",
        "example_en": "— Does the radiator turn on in the winter? — Yes, we have heat with autonomous heating.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about home heating types and autonomous climate control"
    },
    {
        "id": "A1-U107C-014",
        "greek": "— Έχει κλιματιστικό στο σαλόνι; — Ναι, έχει κλιματιστικό για το καλοκαίρι.",
        "phonetic_hint": "EH-khee klee-mah-tee-stee-KOH sto sah-LOH-nee? — Neh, EH-khee klee-mah-tee-stee-KOH yah to kah-lo-KEH-ree.",
        "english": "— Is there an air conditioner in the living room? — Yes, there is an air conditioner for the summer.",
        "notes": "Review Unit 107. Air conditioning facilities for cooling during summer heatwaves.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ανάβουμε το κλιματιστικό όταν έχει ζέστη; — Ναι, το ανάβουμε κάθε μεσημέρι.",
        "example_en": "— Do we turn on the air conditioner when it's hot? — Yes, we turn it on every afternoon.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Checking air conditioning availability for summer climate control"
    },
    {
        "id": "A1-U107C-015",
        "greek": "— Πού είναι ο θερμοσίφωνας; — Ο θερμοσίφωνας είναι μέσα στο μπάνιο.",
        "phonetic_hint": "poo EE-neh o thehr-mo-SEE-fo-nahs? — O thehr-mo-SEE-fo-nahs EE-neh MEH-sah sto MPAH-nyo.",
        "english": "— Where is the water heater? — The water heater is inside the bathroom.",
        "notes": "Review Unit 107. Hot water boiler placement in residential bathrooms.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Άναψε τον θερμοσίφωνα, σε παρακαλώ! — Τον ανάβω αμέσως για να κάνεις μπάνιο.",
        "example_en": "— Turn on the water heater, please! — I'll turn it on right away so you can bathe.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Locating hot water boilers and operating domestic water heating"
    },
    {
        "id": "A1-U107C-016",
        "greek": "— Είναι ακριβό το ενοίκιο; — Όχι, είναι πολύ οικονομικό για αυτή τη γειτονιά.",
        "phonetic_hint": "EE-neh ah-kree-VOH to eh-NEE-kee-o? — OH-khee, EE-neh po-LEE ee-ko-no-mee-KOH yah ahf-TEE tee yee-to-NYAH.",
        "english": "— Is the rent expensive? — No, it is very economical for this neighborhood.",
        "notes": "Review Units 106 & 107. Comparing rent affordability within a specific city area.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πόσα χρήματα πληρώνετε κάθε μήνα; — Πληρώνουμε τετρακόσια ευρώ.",
        "example_en": "— How much money do you pay each month? — We pay four hundred euros.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Evaluating rental affordability and monthly housing budget"
    },
    {
        "id": "A1-U107C-017",
        "greek": "— Πότε είναι ελεύθερο το σπίτι; — Είναι ελεύθερο από την επόμενη εβδομάδα.",
        "phonetic_hint": "POH-teh EE-neh eh-LEF-the-ro to SPEE-tee? — EE-neh eh-LEF-the-ro ah-POH teen eh-POH-meh-nee ehv-tho-MAH-thah.",
        "english": "— When is the house available? — It is available starting next week.",
        "notes": "Review Units 103 & 107. Availability dates and move-in timeline.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Μπορούμε να μείνουμε από τη Δευτέρα; — Ναι, είναι καθαρό και έτοιμο.",
        "example_en": "— Can we stay starting Monday? — Yes, it is clean and ready.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Confirming lease commencement dates and move-in readiness"
    },
    {
        "id": "A1-U107C-018",
        "greek": "— Πώς είναι οι γείτονες στην πολυκατοικία; — Είναι πολύ καλοί γείτονες.",
        "phonetic_hint": "POS EE-neh ee YEE-to-nehs steen po-lee-kah-tee-KEE-ah? — EE-neh po-LEE kah-LEE YEE-to-nehs.",
        "english": "— What are the neighbors in the building like? — They are very good neighbors.",
        "notes": "Review Unit 107. Inquiring about building co-residents ('γείτονες').",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Μένει ο ιδιοκτήτης στην πολυκατοικία; — Ναι, μένει στον πρώτο όροφο.",
        "example_en": "— Does the landlord live in the apartment building? — Yes, he lives on the first floor.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking about neighbors, building community, and landlord presence"
    },

    # =========================================================================
    # Part 3: Apartment Viewing & Furniture Placement (Cards 019 - 028)
    # =========================================================================
    {
        "id": "A1-U107C-019",
        "greek": "— Περάστε μέσα στο σαλόνι, παρακαλώ! — Ευχαριστώ πολύ, το σπίτι σας είναι όμορφο!",
        "phonetic_hint": "peh-RAH-steh MEH-sah sto sah-LOH-nee, pah-rah-kah-LOH! — Ef-khah-ree-STOH po-LEE, to SPEE-tee sahs EE-neh OH-mor-fo!",
        "english": "— Step inside into the living room, please! — Thank you very much, your home is beautiful!",
        "notes": "Review Unit 107. Welcoming guests with polite imperative 'περάστε' and expressing appreciation.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Περάστε μέσα στο καθιστικό και καθίστε στην πολυθρόνα! — Ευχαριστώ!",
        "example_en": "— Step into the lounge and sit in the armchair! — Thank you!",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Welcoming visitors hospitably into residential living areas"
    },
    {
        "id": "A1-U107C-020",
        "greek": "— Πού είναι το καθιστικό; — Είναι εδώ δεξιά, δίπλα στο μεγάλο μπαλκόνι.",
        "phonetic_hint": "poo EE-neh to kah-thee-stee-KOH? — EE-neh eh-THOH thehk-SYAH, THEEP-lah sto meh-GHAH-lo mpal-KOH-nee.",
        "english": "— Where is the sitting room? — It is right here on the right, next to the big balcony.",
        "notes": "Review Unit 107. Locating sitting spaces relative to balconies with spatial adverb 'δεξιά'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Το καθιστικό είναι πολύ φωτεινό! — Ναι, έχει μεγάλο παράθυρο.",
        "example_en": "— The sitting room is very bright! — Yes, it has a large window.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Directing guests to sitting areas and highlighting natural light"
    },
    {
        "id": "A1-U107C-021",
        "greek": "— Πού βρίσκεται ο καναπές; — Ο καναπές βρίσκεται απέναντι από την τηλεόραση.",
        "phonetic_hint": "poo VREES-keh-teh o kah-nah-PEHS? — O kah-nah-PEHS VREES-keh-teh ah-PEH-nahn-dee ah-POH teen tee-leh-OH-rah-see.",
        "english": "— Where is the sofa located? — The sofa is located across from the television.",
        "notes": "Review Unit 107. Locating living room furniture with spatial preposition 'απέναντι από'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Στη μέση του σαλονιού υπάρχει ένα χαμηλό ξύλινο τραπεζάκι. — Και ένα όμορφο χαλί.",
        "example_en": "— In the middle of the living room there is a low wooden coffee table. — And a beautiful rug.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing living room furniture arrangements and interior layout"
    },
    {
        "id": "A1-U107C-022",
        "greek": "— Πού είναι η κουζίνα; — Η κουζίνα είναι δίπλα στην είσοδο, αριστερά.",
        "phonetic_hint": "poo EE-neh ee koo-ZEE-nah? — Ee koo-ZEE-nah EE-neh THEEP-lah steen EE-so-tho, ah-ree-steh-RAH.",
        "english": "— Where is the kitchen? — The kitchen is next to the entrance, on the left.",
        "notes": "Review Unit 107. Locating kitchen facilities relative to the apartment entrance.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Οι κουρτίνες στην κουζίνα είναι κίτρινες; — Ναι, και τα ντουλάπια είναι λευκά.",
        "example_en": "— Are the curtains in the kitchen yellow? — Yes, and the cabinets are white.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing kitchen location, cabinets, and decorative colors"
    },
    {
        "id": "A1-U107C-023",
        "greek": "— Πού είναι το υπνοδωμάτιο; — Είναι δίπλα στο μπάνιο.",
        "phonetic_hint": "poo EE-neh to eep-no-tho-MAH-tee-o? — EE-neh THEEP-lah sto MPAH-nyo.",
        "english": "— Where is the bedroom? — It is next to the bathroom.",
        "notes": "Review Unit 107. Locating resting rooms using preposition 'δίπλα σε'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι χρώμα είναι οι τοίχοι στο υπνοδωμάτιο; — Είναι ανοιχτό πράσινο.",
        "example_en": "— What color are the walls in the bedroom? — They are light green.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Identifying bedroom locations and wall paint color schemes"
    },
    {
        "id": "A1-U107C-024",
        "greek": "— Τι έχει δίπλα στο κρεβάτι; — Έχει δύο κομοδίνα με φωτιστικά.",
        "phonetic_hint": "tee EH-khee THEEP-lah sto kreh-VAH-tee? — EH-khee THEE-o ko-mo-THEE-nah meh fo-tee-stee-KAH.",
        "english": "— What is next to the bed? — There are two nightstands with bedside lamps.",
        "notes": "Review Unit 107. Bedroom furniture: 'κομοδίνα' and 'φωτιστικά'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Βάλε το βιβλίο σου πάνω στο κομοδίνο. — Το βάζω εκεί τώρα.",
        "example_en": "— Put your book on top of the nightstand. — I am putting it there now.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing bedside furniture items and small bedroom fixtures"
    },
    {
        "id": "A1-U107C-025",
        "greek": "— Το μπάνιο έχει μπανιέρα; — Ναι, έχει μια μεγάλη μπανιέρα και έναν νιπτήρα.",
        "phonetic_hint": "to MPAH-nyo EH-khee mpah-NYEH-rah? — Neh, EH-khee myah meh-GHAH-lee mpah-NYEH-rah keh EH-nahn neep-TEE-rah.",
        "english": "— Does the bathroom have a bathtub? — Yes, it has a large bathtub and a washbasin.",
        "notes": "Review Unit 107. Sanitary fixtures: 'μπανιέρα', 'νιπτήρας', 'βρύση'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ο καθρέφτης είναι πάνω από τον νιπτήρα; — Ναι, ακριβώς πάνω από τη βρύση.",
        "example_en": "— Is the mirror above the washbasin? — Yes, right above the faucet.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing bathroom fixtures, bathtubs, mirrors, and washbasins"
    },
    {
        "id": "A1-U107C-026",
        "greek": "— Πού είναι το πλυντήριο ρούχων; — Είναι μέσα στο μπάνιο, πίσω από την πόρτα.",
        "phonetic_hint": "poo EE-neh to pleen-TEE-ree-o ROO-khohn? — EE-neh MEH-sah sto MPAH-nyo, PEE-so ah-POH teen POHR-tah.",
        "english": "— Where is the washing machine? — It is inside the bathroom, behind the door.",
        "notes": "Review Unit 107. Laundry appliance location using spatial preposition 'πίσω από'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πλύνε τα ρούχα σου σήμερα στο πλυντήριο! — Ναι, τα πλένω αμέσως.",
        "example_en": "— Wash your clothes in the washing machine today! — Yes, I am washing them right away.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Locating laundry appliances and organizing washing chores"
    },
    {
        "id": "A1-U107C-027",
        "greek": "— Έχει τζάκι το σαλόνι; — Ναι, το τζάκι είναι δεξιά από τον γωνιακό καναπέ.",
        "phonetic_hint": "EH-khee TZAH-kee to sah-LOH-nee? — Neh, to TZAH-kee EE-neh thehk-SYAH ah-POH ton gho-nee-ah-KOH kah-nah-PEH.",
        "english": "— Does the living room have a fireplace? — Yes, the fireplace is to the right of the corner sofa.",
        "notes": "Review Unit 107. Fireplace fixture: 'το τζάκι' with corner furniture.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ανάβουμε το τζάκι όταν κάνει κρύο; — Ναι, ανάβουμε το τζάκι τον χειμώνα.",
        "example_en": "— Do we light the fireplace when it's cold? — Yes, we light the fireplace in the winter.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing fireplace features and heating coziness in living rooms"
    },
    {
        "id": "A1-U107C-028",
        "greek": "— Πού είναι η βιβλιοθήκη; — Η μεγάλη βιβλιοθήκη είναι δίπλα στην πόρτα του γραφείου.",
        "phonetic_hint": "poo EE-neh ee veev-lee-o-THEE-kee? — Ee meh-GHAH-lee veev-lee-o-THEE-kee EE-neh THEEP-lah steen POHR-tah too ghrah-FEE-oo.",
        "english": "— Where is the bookcase? — The large bookcase is beside the door of the study.",
        "notes": "Review Unit 107. Study furniture: 'βιβλιοθήκη', 'γραφείο', 'πόρτα'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Το λεξικό είναι πάνω στο γραφείο; — Ναι, είναι πάνω στο γραφείο.",
        "example_en": "— Is the dictionary on top of the desk? — Yes, it is on the desk.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Locating bookcases, study desks, and reading materials"
    },

    # =========================================================================
    # Part 4: Roommate Life & Imperative Instructions (Cards 029 - 038)
    # =========================================================================
    {
        "id": "A1-U107C-029",
        "greek": "— Άνοιξε το παράθυρο, σε παρακαλώ, γιατί έχει πολλή ζέστη. — Αμέσως, το ανοίγω τώρα.",
        "phonetic_hint": "AH-neek-seh to pah-RAH-thee-ro, seh pah-rah-kah-LOH, yah-TEE EH-khee po-LEE ZEHS-tee. — ah-MEH-sos, to ah-NEE-gho TOH-rah.",
        "english": "— Open the window, please, because it is very hot. — Right away, I am opening it now.",
        "notes": "Review Unit 107b. Singular Aorist Imperative 'άνοιξε' for immediate room ventilation.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Κάνει πολλή ζέστη εδώ μέσα! — Άνοιξε και την πόρτα να μπει αέρας.",
        "example_en": "— It is very hot in here! — Open the door too to let in fresh air.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Giving polite imperative instructions to ventilate rooms"
    },
    {
        "id": "A1-U107C-030",
        "greek": "— Κλείσε την πόρτα όταν βγεις έξω! — Εντάξει, την κλείνω αμέσως.",
        "phonetic_hint": "KLEE-seh teen POHR-tah OH-tahn vyees EH-kso! — ehn-DAHK-see, teen KLEE-no ah-MEH-sos.",
        "english": "— Close the door when you go outside! — Alright, I am closing it immediately.",
        "notes": "Review Unit 107b. Singular Aorist Imperative 'κλείσε' upon departing.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Κλείσε τα παράθυρα το βράδυ! — Ναι, τα κλείνω πάντα.",
        "example_en": "— Close the windows at night! — Yes, I always close them.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Instructing housemates to shut doors and windows for safety"
    },
    {
        "id": "A1-U107C-031",
        "greek": "— Άναψε το φως στο διάδρομο, γιατί είναι σκοτεινά. — Το ανάβω αμέσως.",
        "phonetic_hint": "AH-nahp-seh to fos sto thee-AH-thro-mo, yah-TEE EE-neh sko-tee-NAH. — To ah-NAH-vo ah-MEH-sos.",
        "english": "— Turn on the light in the hallway, because it is dark. — I am turning it on right away.",
        "notes": "Review Unit 107b. Imperative 'άναψε' for illumination.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Άναψε το φωτιστικό δαπέδου, σε παρακαλώ. — Ναι, το ανάβω για το διάβασμα.",
        "example_en": "— Turn on the floor lamp, please. — Yes, I am turning it on for studying.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Requesting hallway lighting and room illumination"
    },
    {
        "id": "A1-U107C-032",
        "greek": "— Σβήσε το καλοριφέρ πριν φύγεις από το σπίτι! — Μην ανησυχείς, το κλείνω τώρα.",
        "phonetic_hint": "ZVEE-seh to kah-lo-ree-FEHR PREEN FEE-yees ah-POH to SPEE-tee! — Meen ah-nee-see-KHEES, to KLEE-no TOH-rah.",
        "english": "— Turn off the radiator before you leave the house! — Don't worry, I am shutting it off now.",
        "notes": "Review Unit 107b. Imperative 'σβήσε' to save heating energy.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Κλείσε τα φώτα πριν φύγεις! — Ναι, τα κλείνουμε όλα.",
        "example_en": "— Turn off the lights before you leave! — Yes, we turn them all off.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Instructing housemates to shut down heating and save electricity"
    },
    {
        "id": "A1-U107C-033",
        "greek": "— Κάθισε αναπαυτικά στον καναπέ και ξεκουράσου! — Ευχαριστώ, είμαι πολύ κουρασμένος.",
        "phonetic_hint": "KAH-thee-seh ah-nah-pahf-tee-KAH ston kah-nah-PEH keh kseh-koo-RAH-soo! — Ef-khah-ree-STOH, EE-meh po-LEE koo-rahz-MEH-nos.",
        "english": "— Sit down comfortably on the sofa and relax! — Thank you, I am very tired.",
        "notes": "Review Unit 107b. Hospitality imperatives 'κάθισε' and reflexive 'ξεκουράσου'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Καθίστε στην πολυθρόνα, παρακαλώ! — Ευχαριστώ πάρα πολύ.",
        "example_en": "— Please sit in the armchair! — Thank you very much.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Offering comfortable seating and inviting guests to unwind"
    },
    {
        "id": "A1-U107C-034",
        "greek": "— Φέρε μου ένα ποτήρι δροσερό νερό από την κουζίνα! — Ορίστε, κρύο νερό από το ψυγείο.",
        "phonetic_hint": "FEH-reh moo EH-nah po-TEE-ree thro-seh-ROH neh-ROH ah-POH teen koo-ZEE-nah! — o-REES-teh, KREE-o neh-ROH ah-POH to psee-YEE-o.",
        "english": "— Bring me a glass of cool water from the kitchen! — Here you are, cold water from the fridge.",
        "notes": "Review Unit 107b. Irregular imperative 'φέρε' for bringing items.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Φέρε μου ένα ποτήρι νερό, σε παρακαλώ. — Ορίστε το νερό σου.",
        "example_en": "— Bring me a glass of water, please. — Here is your water.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Requesting and serving water from the refrigerator"
    },
    {
        "id": "A1-U107C-035",
        "greek": "— Πλύνε τα πιάτα μετά το μεσημεριανό φαγητό! — Ναι, πλένω τα πιάτα και τα ποτήρια τώρα.",
        "phonetic_hint": "PLEE-neh tah PYA-tah meh-TAH to meh-see-meh-ree-ah-NOH fah-yee-TOH! — Neh, PLEH-no tah PYA-tah keh tah po-TEE-ryah TOH-rah.",
        "english": "— Wash the dishes after lunch! — Yes, I am washing the plates and glasses now.",
        "notes": "Review Unit 107b. Domestic chore imperative 'πλύνε τα πιάτα'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πλύνε τα πιάτα στην κουζίνα! — Τα πλένω αμέσως.",
        "example_en": "— Wash the dishes in the kitchen! — I am washing them right away.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Delegating and confirming kitchen dishwashing responsibilities"
    },
    {
        "id": "A1-U107C-036",
        "greek": "— Καθάρισε το δωμάτιό σου πριν έρθουν οι καλεσμένοι! — Ναι, καθαρίζω και τακτοποιώ τα ρούχα μου.",
        "phonetic_hint": "kah-THAH-ree-seh to tho-MAH-tee-OH soo PREEN EHR-thoon ee kah-leh-ZMEH-nee! — Neh, kah-thah-REE-zo keh tak-to-py-OH tah ROO-khah moo.",
        "english": "— Clean your room before the guests arrive! — Yes, I am cleaning and tidying my clothes.",
        "notes": "Review Unit 107b. Domestic imperatives 'καθάρισε' and 'τακτοποιώ' prior to guest visits.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τακτοποιώ τα ρούχα μου στην ντουλάπα. — Πολύ ωραία.",
        "example_en": "— I am organizing my clothes in the wardrobe. — Very good.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Directing domestic tidying and wardrobe organization before visits"
    },
    {
        "id": "A1-U107C-037",
        "greek": "— Βάλε τα ρούχα σου μέσα στην ντουλάπα! — Τα βάζω αμέσως στο συρτάρι.",
        "phonetic_hint": "VAH-leh tah ROO-khah soo MEH-sah steen noo-LAH-pah! — Tah VAH-zo ah-MEH-sos sto seer-TAH-ree.",
        "english": "— Put your clothes inside the wardrobe! — I am putting them into the drawer right away.",
        "notes": "Review Unit 107b. Irregular imperative 'βάλε' with internal preposition 'μέσα σε'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Βάλε τα παπούτσια σου στην είσοδο. — Εντάξει, τα βάζω εκεί.",
        "example_en": "— Put your shoes at the entrance. — Alright, I am putting them there.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Instructing housemates to store clothing in wardrobes and drawers"
    },
    {
        "id": "A1-U107C-038",
        "greek": "— Βάλε τις παντόφλες σου, γιατί το πάτωμα είναι κρύο! — Ναι, τις φοράω αμέσως.",
        "phonetic_hint": "VAH-leh tees pahn-TOH-flehs soo, yah-TEE to PAH-to-mah EE-neh KREE-o! — Neh, tees fo-RAH-o ah-MEH-sos.",
        "english": "— Put on your slippers, because the floor is cold! — Yes, I am putting them on right away.",
        "notes": "Review Unit 107b. Home footwear etiquette: 'παντόφλες' and 'πάτωμα'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Οι παντόφλες σου είναι κάτω από το κρεβάτι. — Ευχαριστώ, τις φοράω.",
        "example_en": "— Your slippers are under the bed. — Thank you, I am putting them on.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Reminding family members to wear indoor slippers on cold floors"
    },

    # =========================================================================
    # Part 5: Prohibitions & Household Rules (Cards 039 - 044)
    # =========================================================================
    {
        "id": "A1-U107C-039",
        "greek": "— Μη μιλάτε τόσο δυνατά, γιατί κοιμάται το παιδί! — Συγγνώμη, κάνουμε ησυχία αμέσως.",
        "phonetic_hint": "mee mee-LAH-teh TOH-so thee-nah-TAH, yah-TEE kee-MAH-teh to peh-THEE! — seeg-NOH-mee, KAH-noo-meh ee-see-KHEE-ah ah-MEH-sos.",
        "english": "— Don't speak so loudly, because the child is sleeping! — Sorry, we'll be quiet immediately.",
        "notes": "Review Unit 107b. Negative prohibition 'μη μιλάτε' and keeping quiet ('κάνουμε ησυχία').",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Κοιμάται το μωρό στο δωμάτιο; — Ναι, κάνουμε ησυχία.",
        "example_en": "— Is the baby sleeping in the room? — Yes, we are keeping quiet.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Enforcing household quiet hours and requesting lower speaking volume"
    },
    {
        "id": "A1-U107C-040",
        "greek": "— Μην ανοίγεις το παράθυρο, γιατί κάνει κρύο έξω! — Εντάξει, το κλείνω αμέσως.",
        "phonetic_hint": "meen ah-NEE-yees to pah-RAH-thee-ro, yah-TEE KAH-nee KREE-o EH-kso! — ehn-DAHK-see, to KLEE-no ah-MEH-sos.",
        "english": "— Don't open the window, because it's cold outside! — Alright, I am closing it immediately.",
        "notes": "Review Unit 107b. Prohibition with 'μην ανοίγεις' during cold weather.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Βρέχει έξω; — Ναι, κλείσε καλά τα παράθυρα.",
        "example_en": "— Is it raining outside? — Yes, close the windows tightly.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Prohibiting open windows during low outdoor temperatures"
    },
    {
        "id": "A1-U107C-041",
        "greek": "— Μη βάζεις τα βρεγμένα παπούτσια πάνω στο χαλί! — Συγγνώμη, τα βγάζω στην είσοδο.",
        "phonetic_hint": "mee VAH-zees tah vrehg-MEH-nah pah-POO-tsyah PAH-no sto khah-LEE! — seeg-NOH-mee, tah VGAH-zo steen EE-so-tho.",
        "english": "— Don't put wet shoes on the carpet! — Sorry, I am taking them off at the entrance.",
        "notes": "Review Unit 107b. Domestic rule prohibiting wet footwear on rugs.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Το χαλί είναι καινούργιο και καθαρό; — Ναι, είναι καθαρό.",
        "example_en": "— Is the rug new and clean? — Yes, it is clean.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Enforcing cleanliness rules regarding wet shoes on carpets"
    },
    {
        "id": "A1-U107C-042",
        "greek": "— Μην πετάς τα σκουπίδια κάτω, βάλε τα στον κάδο! — Ναι, τα βάζω μέσα στον κάδο.",
        "phonetic_hint": "meen peh-TAHS tah skoo-PEE-thyah KAH-to, VAH-leh tah ston KAH-tho! — Neh, tah VAH-zo MEH-sah ston KAH-tho.",
        "english": "— Don't throw rubbish on the floor, put it in the bin! — Yes, I am putting it inside the bin.",
        "notes": "Review Unit 107b. Waste disposal rule with 'μην πετάς' and 'βάλε στον κάδο'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πού βάζουμε τα σκουπίδια; — Έξω στην αυλή, μέσα στον κάδο.",
        "example_en": "— Where do we put the garbage? — Outside in the yard, inside the bin.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Directing proper household waste disposal into rubbish bins"
    },
    {
        "id": "A1-U107C-043",
        "greek": "— Μη φεύγεις ακόμα, κάθισε να πιούμε έναν καφέ! — Ευχαριστώ, μένω για λίγο.",
        "phonetic_hint": "mee FEHV-yees ah-KOH-mah, KAH-thee-seh nah PYOOH-meh EH-nahn kah-FEH! — Ef-khah-ree-STOH, MEH-no yah LEE-gho.",
        "english": "— Don't leave yet, sit down so we can drink a coffee! — Thank you, I will stay for a while.",
        "notes": "Review Unit 107b. Friendly persuasion with negative imperative 'μη φεύγεις'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Έχεις χρόνο για έναν καφέ; — Ναι, έχω ελεύθερο χρόνο.",
        "example_en": "— Do you have time for a coffee? — Yes, I have free time.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Persuading guests to prolong their stay and share coffee"
    },
    {
        "id": "A1-U107C-044",
        "greek": "— Μην ανησυχείς για τα κοινόχρηστα, τα πληρώνω εγώ! — Σε ευχαριστώ πάρα πολύ.",
        "phonetic_hint": "meen ah-nee-see-KHEES yah tah kee-NOH-khree-stah, tah plee-ROH-no eh-GHOH! — Seh ef-khah-ree-STOH PAH-rah po-LEE.",
        "english": "— Don't worry about the building fees, I will pay them! — Thank you very much.",
        "notes": "Review Unit 107b. Reassuring phrase 'μην ανησυχείς' regarding shared utility payments.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πληρώνετε τα κοινόχρηστα κάθε μήνα; — Ναι, τα πληρώνουμε μαζί.",
        "example_en": "— Do you pay the building fees every month? — Yes, we pay them together.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Reassuring roommates and settling shared maintenance expenses"
    },

    # =========================================================================
    # Part 6: Home Life & Communicative Synthesis (Cards 045 - 050)
    # =========================================================================
    {
        "id": "A1-U107C-045",
        "greek": "— Πώς σου φαίνεται το καινούργιο μας σπίτι; — Μου αρέσει πάρα πολύ, είναι ζεστό και άνετο.",
        "phonetic_hint": "POS soo FEH-neh-teh to keh-NOOR-gyo mahs SPEE-tee? — Moo ah-REH-see PAH-rah po-LEE, EE-neh zeh-STOH keh AH-neh-to.",
        "english": "— How do you like our new home? — I like it very much, it is warm and comfortable.",
        "notes": "Review Units 104 & 107. Asking for and offering an impression of a newly occupied residence.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Είναι όμορφο το διαμέρισμα; — Ναι, είναι ένα πολύ όμορφο σπίτι.",
        "example_en": "— Is the apartment beautiful? — Yes, it is a very beautiful house.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking for impressions and evaluating the comfort of a new residence"
    },
    {
        "id": "A1-U107C-046",
        "greek": "— Πρόσεξε τα σκαλοπάτια, γιατί είναι βρεγμένα! — Ευχαριστώ, προσέχεις κι εσύ;",
        "phonetic_hint": "PROH-sek-seh tah skah-lo-PAH-tyah, yah-TEE EE-neh vrehg-MEH-nah! — Ef-khah-ree-STOH, pro-SEH-khees kee eh-SEE?",
        "english": "— Watch the stairs, because they are wet! — Thank you, are you watching out too?",
        "notes": "Review Unit 107b. Cautionary imperative 'πρόσεξε' on wet building steps.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πρόσεξε στην είσοδο! — Ναι, ευχαριστώ, πρόσεξε κι εσύ!",
        "example_en": "— Watch out at the entrance! — Yes, thank you, you watch out too!",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Warning housemates about slippery steps and physical hazards"
    },
    {
        "id": "A1-U107C-047",
        "greek": "— Στείλε μου τη διεύθυνση και τον όροφο του σπιτιού! — Σου στέλνω μήνυμα στο κινητό σου τώρα.",
        "phonetic_hint": "STEE-leh moo tee thee-EH-fthin-see keh ton OH-ro-fo too spee-TYOO! — Soo STEHL-no MEE-nee-mah sto kee-nee-TOH soo TOH-rah.",
        "english": "— Send me the address and the floor of the house! — I am sending you a text on your mobile now.",
        "notes": "Review Units 103 & 107. Imperative 'στείλε' to exchange address and floor details.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ποια είναι η διεύθυνσή σας; — Οδός Ερμού δέκα, στον δεύτερο όροφο.",
        "example_en": "— What is your address? — Ten Ermou Street, on the second floor.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Requesting and sending residence address details via mobile message"
    },
    {
        "id": "A1-U107C-048",
        "greek": "— Ποιο δωμάτιο σου αρέσει πιο πολύ; — Το σαλόνι, επειδή έχει μεγάλο μπαλκόνι και ήλιο.",
        "phonetic_hint": "PYO tho-MAH-tee-o soo ah-REH-see PYO po-LEE? — To sah-LOH-nee, eh-pee-THEE EH-khee meh-GHAH-lo mpal-KOH-nee keh EE-lyo.",
        "english": "— Which room do you like the most? — The living room, because it has a large balcony and sunlight.",
        "notes": "Review Units 105 & 107. Stating room preferences with comparative 'πιο πολύ'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πού πίνετε τον καφέ σας το πρωί; — Στο μπαλκόνι, κάθε πρωί.",
        "example_en": "— Where do you drink your coffee in the morning? — On the balcony, every morning.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Explaining preferred rooms in a home and describing sunny spaces"
    },
    {
        "id": "A1-U107C-049",
        "greek": "— Τα παιδιά παίζουν έξω στην αυλή με τον σκύλο; — Ναι, παίζουν έξω στον κήπο.",
        "phonetic_hint": "tah peh-THYAH PEH-zoon EH-kso steen ahv-LEE meh ton SKEE-lo? — Neh, PEH-zoon EH-kso ston KEE-po.",
        "english": "— Are the children playing outside in the yard with the dog? — Yes, they are playing outside in the garden.",
        "notes": "Review Unit 107. Describing outdoor play in courtyards ('αυλή') and gardens ('κήπος').",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Έχει μεγάλο κήπο η μονοκατοικία; — Ναι, έχει έναν όμορφο κήπο πίσω από το σπίτι.",
        "example_en": "— Does the detached house have a large garden? — Yes, it has a beautiful garden behind the house.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing outdoor family activities in yards and gardens"
    },
    {
        "id": "A1-U107C-050",
        "greek": "— Σπίτι μου, σπιτάκι μου και σπιτοκαλυβάκι μου! — Ναι, είναι το πιο όμορφο σπίτι!",
        "phonetic_hint": "SPEE-tee moo, spee-TAH-kee moo keh spee-to-kah-lee-VAH-kee moo! — Neh, EE-neh to PYO OH-mor-fo SPEE-tee!",
        "english": "— Home sweet home, my little house and little haven! — Yes, it is the most beautiful home!",
        "notes": "Review Unit 107b. Traditional Greek cultural proverb celebrating the joy and comfort of one's home.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Χάρηκα πολύ για το νέο μας σπίτι! — Καλωσόρισες στο σπίτι μας!",
        "example_en": "— I am very glad about our new house! — Welcome to our home!",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Reciting cultural home proverbs and expressing contentment in one's abode"
    }
]

lesson_u107c = {
    "unit_id": "unit-107c",
    "lesson_id": "lesson-01",
    "title": "Ενότητα 6: Διάλογοι & Εξετάσεις — Σπίτι, Ενοικίαση & Οδηγίες (A1 Synthesis 101-107)",
    "description": "Conversational, dialogue, and CEFR A1 oral exam practice focusing on home life, apartment search, rental negotiations, giving polite instructions and household commands (imperative), and neighborhood living using vocabulary from Lessons 101 to 107.",
    "lesson_status": "not_started",
    "entries": cards_u107c
}

def main():
    print(f"Writing {len(cards_u107c)} cards to {YAML_PATH}...")
    with open(YAML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(lesson_u107c, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("YAML successfully written.")

    # Update manifest.yaml
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    units = manifest.get("units", [])
    existing = next((u for u in units if u.get("id") == "unit-107c"), None)
    unit_107c_entry = {
        "id": "unit-107c",
        "title": "Κλικ στα Ελληνικά Α1: Σελίδες 133-150 (Ενότητα 6: Σπίτι μου, σπιτάκι μου - Διάλογοι, Εξετάσεις & Συνομιλίες)",
        "order": "KlikA1-07-C",
        "is_expansion": True,
        "expansion_of": "KlikA1-07-A",
        "lessons": [
            {
                "id": "lesson-01",
                "file": "unit-107c/lesson-01.yaml",
                "title": "Ενότητα 6: Διάλογοι & Εξετάσεις — Σπίτι, Ενοικίαση & Οδηγίες (A1 Synthesis 101-107)",
                "description": "Conversational, dialogue, and CEFR A1 oral exam practice focusing on home life, apartment search, rental negotiations, giving polite instructions and household commands (imperative), and neighborhood living using vocabulary from Lessons 101 to 107."
            }
        ]
    }

    if existing:
        print("Updating existing unit-107c in manifest.yaml...")
        idx = units.index(existing)
        units[idx] = unit_107c_entry
    else:
        u107b_idx = next((i for i, u in enumerate(units) if u.get("id") == "unit-107b"), None)
        if u107b_idx is not None:
            print(f"Inserting unit-107c immediately after unit-107b (index {u107b_idx + 1})...")
            units.insert(u107b_idx + 1, unit_107c_entry)
        else:
            print("Appending unit-107c to manifest.yaml...")
            units.append(unit_107c_entry)

    manifest["units"] = units

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("Manifest successfully updated with unit-107c!")

if __name__ == "__main__":
    main()

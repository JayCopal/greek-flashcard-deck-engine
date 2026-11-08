# -*- coding: utf-8 -*-
"""
Script to create Unit 103 B from Klik A1 (Pages 55-68):
Ενότητα 2: Πού μένεις; - Γραμματική & Προτάσεις
Focuses on full sentences, syntax patterns, prepositions 'σε' and 'από'
with accusative definite articles (στον/στη/στο, από τον/τη/το),
spatial expressions (κοντά σε, μακριά από, απέναντι από, δίπλα σε, μπροστά από, πίσω από),
Type A verb conjugations in -ω (μένω, σπουδάζω, αρχίζω, πίνω, κάνω, ξέρω, καταλαβαίνω),
address and telephone formulation, and everyday conversational formulas.
"""
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
UNIT_DIR = CONTENT_DIR / "unit-103b"
UNIT_DIR.mkdir(parents=True, exist_ok=True)
YAML_PATH = UNIT_DIR / "lesson-01.yaml"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

cards_u103b = [
    # =========================================================================
    # 1. Prepositions "σε" & "από" with Accusative Articles (pp. 58-59)
    # =========================================================================
    {
        "id": "A1-U103B-001",
        "greek": "Ο Άρης είναι από τη Θεσσαλονίκη, αλλά μένει στην Αθήνα.",
        "phonetic_hint": "o AH-rees EE-neh ah-POH tee the-sah-lo-NEE-kee, ah-LAH MEH-nee steen ah-THEE-nah",
        "english": "Aris is from Thessaloniki, but lives in Athens.",
        "notes": "Klik A1 p. 58. Grammar: contrast of origin ('από τη' + feminine accusative) and residence ('στην' + feminine accusative).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Από πού είναι ο Άρης και πού μένει τώρα; — Ο Άρης είναι από τη Θεσσαλονίκη, αλλά μένει στην Αθήνα.",
        "example_en": "— Where is Aris from and where does he live now? — Aris is from Thessaloniki, but lives in Athens.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Contrasting geographical origin with current place of residence"
    },
    {
        "id": "A1-U103B-002",
        "greek": "Η Κάλη είναι από τον Βόλο και μένει στον Βόλο.",
        "phonetic_hint": "ee KAH-lee EE-neh ah-POH ton VOH-lo keh MEH-nee ston VOH-lo",
        "english": "Kali is from Volos and lives in Volos.",
        "notes": "Klik A1 p. 58. Grammar: masculine singular accusative with prepositions 'από τον' and 'στον' (< ο Βόλος).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η Κάλη δεν θέλει να φύγει: είναι από τον Βόλο και μένει στον Βόλο.",
        "example_en": "Kali does not want to leave: she is from Volos and lives in Volos.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Stating masculine city origin and residence"
    },
    {
        "id": "A1-U103B-003",
        "greek": "Ο φοιτητής είναι από το Βερολίνο και τώρα μένει στο Ηράκλειο.",
        "phonetic_hint": "o fee-tee-TEES EE-neh ah-POH to veh-ro-LEE-no keh TOH-rah MEH-nee sto ee-RAH-klee-o",
        "english": "The student is from Berlin and now lives in Heraklion.",
        "notes": "Klik A1 p. 58, 59. Grammar: neuter singular accusative with prepositions 'από το' and 'στο'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ήρθε με πρόγραμμα Erasmus: ο φοιτητής είναι από το Βερολίνο και τώρα μένει στο Ηράκλειο.",
        "example_en": "He came with an Erasmus program: the student is from Berlin and now lives in Heraklion.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing international student mobility and neuter city names"
    },
    {
        "id": "A1-U103B-004",
        "greek": "Πού μένει η οικογένειά σου; — Μένει στον Πειραιά.",
        "phonetic_hint": "poo MEH-nee ee ee-ko-YEH-nee-AH soo? — MEH-nee ston pee-reh-AH",
        "english": "Where does your family live? — It lives in Piraeus.",
        "notes": "Klik A1 p. 58. Grammar: masculine noun in -ας (ο Πειραιάς) in the accusative with preposition: 'στον Πειραιά'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πού μένει η οικογένειά σου; — Μένει στον Πειραιά, κοντά στο λιμάνι.",
        "example_en": "— Where does your family live? — It lives in Piraeus, near the port.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about family residence in port cities"
    },
    {
        "id": "A1-U103B-005",
        "greek": "Είμαι από την Πάτρα, αλλά σπουδάζω στη Θεσσαλονίκη.",
        "phonetic_hint": "EE-meh ah-POH teen PAH-trah, ah-LAH spoo-THAH-zo stee the-sah-lo-NEE-kee",
        "english": "I am from Patras, but study in Thessaloniki.",
        "notes": "Klik A1 p. 58, 64. Grammar: feminine accusative rule: 'στην Πάτρα' (keeps ν before π) vs 'στη Θεσσαλονίκη' (drops ν before θ).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Από πού είσαι; — Είμαι από την Πάτρα, αλλά σπουδάζω στη Θεσσαλονίκη.",
        "example_en": "— Where are you from? — I am from Patras, but study in Thessaloniki.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Explaining student relocation between major cities"
    },
    {
        "id": "A1-U103B-006",
        "greek": "Μένουμε στο κέντρο της πόλης, κοντά στην πλατεία.",
        "phonetic_hint": "MEH-noo-meh sto KEN-dro tees POH-lees, kon-DAH steen plah-TEE-ah",
        "english": "We live in the city center, near the square.",
        "notes": "Klik A1 p. 58, 63. Grammar: 1st person plural verb 'μένουμε' + prepositional locatives 'στο κέντρο' and 'στην πλατεία'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Είναι πολύ βολικά, επειδή μένουμε στο κέντρο της πόλης, κοντά στην πλατεία.",
        "example_en": "It is very convenient, because we live in the city center, near the square.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing central downtown living"
    },
    {
        "id": "A1-U103B-007",
        "greek": "Από πού είστε; — Είμαστε από την Κρήτη.",
        "phonetic_hint": "ah-POH poo EE-steh? — EE-mah-steh ah-POH teen KREE-tee",
        "english": "Where are you from? — We are from Crete.",
        "notes": "Klik A1 p. 58. Grammar: plural question 'από πού είστε' + feminine island name with 'από την'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Από πού είστε; — Είμαστε από την Κρήτη, από τα Χανιά.",
        "example_en": "— Where are you from? — We are from Crete, from Chania.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring and answering about regional/island origins"
    },
    {
        "id": "A1-U103B-008",
        "greek": "Η μητέρα μου μένει στη Λάρισα με την αδερφή μου.",
        "phonetic_hint": "ee mee-TEH-rah moo MEH-nee stee LAH-ree-sah meh teen ah-thel-FEE moo",
        "english": "My mother lives in Larissa with my sister.",
        "notes": "Klik A1 p. 58. Grammar: feminine accusative without final nu ('στη Λάρισα') before liquid consonant λ.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Εγώ μένω στην Αθήνα, αλλά η μητέρα μου μένει στη Λάρισα με την αδερφή μου.",
        "example_en": "I live in Athens, but my mother lives in Larissa with my sister.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Explaining maternal living situation in provincial cities"
    },
    {
        "id": "A1-U103B-009",
        "greek": "Το ξενοδοχείο είναι στο Σύνταγμα ή στην Ομόνοια;",
        "phonetic_hint": "to kseh-no-tho-KHEE-o EE-neh sto SEEN-dag-mah ee steen oh-MOH-nee-ah",
        "english": "Is the hotel in Syntagma or in Omonoia?",
        "notes": "Klik A1 p. 58, 65. Contrast of neuter neighborhood 'στο Σύνταγμα' and feminine neighborhood 'στην Ομόνοια'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ψάχνω το ξενοδοχείο. Είναι στο Σύνταγμα ή στην Ομόνοια; — Είναι στο Σύνταγμα.",
        "example_en": "— I am looking for the hotel. Is it in Syntagma or in Omonoia? — It is in Syntagma.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking for neighborhood clarification for tourist accommodation"
    },
    {
        "id": "A1-U103B-010",
        "greek": "Πηγαίνω από το σπίτι στη δουλειά με τα πόδια.",
        "phonetic_hint": "pee-YEH-no ah-POH to SPEE-tee stee thoo-LYAH meh tah POH-thyah",
        "english": "I go from home to work on foot.",
        "notes": "Klik A1 p. 58, 64. Grammar: correlated prepositions 'από το... στη...' indicating departure and destination.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Είναι πολύ κοντά, γι' αυτό πηγαίνω από το σπίτι στη δουλειά με τα πόδια.",
        "example_en": "It is very close, so I go from home to work on foot.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing foot commuting routine from home to office"
    },
    {
        "id": "A1-U103B-011",
        "greek": "Ο Νίκος μένει στον τρίτο όροφο της πολυκατοικίας.",
        "phonetic_hint": "o NEE-kos MEH-nee ston TREE-to OH-ro-fo tees po-lee-kah-tee-KEE-as",
        "english": "Nikos lives on the third floor of the apartment building.",
        "notes": "Klik A1 p. 56, 58. Grammar: masculine ordinal accusative 'στον τρίτο όροφο'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αν έρθεις στην πολυκατοικία, ο Νίκος μένει στον τρίτο όροφο.",
        "example_en": "If you come to the apartment building, Nikos lives on the third floor.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Specifying apartment floor level"
    },
    {
        "id": "A1-U103B-012",
        "greek": "Το ιατρείο του είναι στον δεύτερο όροφο.",
        "phonetic_hint": "to yah-TREE-o too EE-neh ston THEHF-teh-ro OH-ro-fo",
        "english": "His doctor's office is on the second floor.",
        "notes": "Klik A1 p. 58, 63. Grammar: ordinal numbers in accusative locative: 'στον δεύτερο όροφο'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πάρτε το ασανσέρ, το ιατρείο του είναι στον δεύτερο όροφο.",
        "example_en": "Take the elevator, his office is on the second floor.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Directing visitors to medical offices by floor"
    },

    # =========================================================================
    # 2. Spatial Expressions & Urban Landmarks (pp. 63-64, 67)
    # =========================================================================
    {
        "id": "A1-U103B-013",
        "greek": "Το σπίτι μου είναι κοντά στον σταθμό του μετρό.",
        "phonetic_hint": "to SPEE-tee moo EE-neh kon-DAH ston stahth-MOH too meh-TROH",
        "english": "My house is near the metro station.",
        "notes": "Klik A1 p. 63, 67. Grammar: spatial phrase 'κοντά σε' + masculine accusative 'στον σταθμό'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Είναι πολύ εύκολο να έρθεις, γιατί το σπίτι μου είναι κοντά στον σταθμό του μετρό.",
        "example_en": "It is very easy to come, because my house is near the metro station.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing home proximity to public transit"
    },
    {
        "id": "A1-U103B-014",
        "greek": "Το αεροδρόμιο είναι πολύ μακριά από το κέντρο.",
        "phonetic_hint": "to ah-eh-ro-DHROH-mee-o EE-neh po-LEE mah-kree-AH ah-POH to KEN-dro",
        "english": "The airport is very far from the center.",
        "notes": "Klik A1 p. 63, 67. Grammar: antonym spatial expression 'μακριά από' + neuter accusative 'το κέντρο'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πρέπει να πάρουμε ταξί, επειδή το αεροδρόμιο είναι πολύ μακριά από το κέντρο.",
        "example_en": "We need to take a taxi, because the airport is very far from the center.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing long urban distance and transit necessity"
    },
    {
        "id": "A1-U103B-015",
        "greek": "Η καφετέρια είναι δίπλα στο φαρμακείο.",
        "phonetic_hint": "ee kah-feh-TEH-ree-ah EE-neh THEEP-lah sto fahr-mah-KEE-o",
        "english": "The cafe is next to the pharmacy.",
        "notes": "Klik A1 p. 63. Grammar: spatial expression 'δίπλα σε' + neuter accusative 'στο φαρμακείο'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Σε περιμένω έξω: η καφετέρια είναι δίπλα στο φαρμακείο.",
        "example_en": "I am waiting for you outside: the cafe is next to the pharmacy.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing immediate adjacent location of urban shops"
    },
    {
        "id": "A1-U103B-016",
        "greek": "Η στάση του λεωφορείου είναι δίπλα στην είσοδο.",
        "phonetic_hint": "ee STAH-see too leh-o-fo-REE-oo EE-neh THEEP-lah steen EE-so-tho",
        "english": "The bus stop is next to the entrance.",
        "notes": "Klik A1 p. 63, 67. Grammar: 'δίπλα στην' + feminine accusative 'είσοδο'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Δεν θα περπατήσεις πολύ, η στάση του λεωφορείου είναι δίπλα στην είσοδο.",
        "example_en": "You won't walk far, the bus stop is right next to the entrance.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Locating bus stops relative to building entrances"
    },
    {
        "id": "A1-U103B-017",
        "greek": "Ο κινηματογράφος είναι ακριβώς απέναντι από το πάρκο.",
        "phonetic_hint": "o kee-nee-mah-to-GRAH-fos EE-neh ah-kree-VOHS ah-PEH-nahn-dee ah-POH to PAHR-ko",
        "english": "The cinema is right across from the park.",
        "notes": "Klik A1 p. 63. Grammar: spatial expression 'απέναντι από' + neuter accusative 'το πάρκο'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Θα σε δω στις οκτώ: ο κινηματογράφος είναι ακριβώς απέναντι από το πάρκο.",
        "example_en": "I'll see you at eight: the cinema is right across from the park.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Giving cinema meeting points across public parks"
    },
    {
        "id": "A1-U103B-018",
        "greek": "Το μουσείο βρίσκεται απέναντι από τη βιβλιοθήκη.",
        "phonetic_hint": "to moo-SEE-o VREE-skeh-teh ah-PEH-nahn-dee ah-POH tee veev-lee-o-THEE-kee",
        "english": "The museum is located across from the library.",
        "notes": "Klik A1 p. 63. Grammar: positional mediopassive verb 'βρίσκεται' + 'απέναντι από τη' + feminine accusative.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Στην παλιά πόλη, το μουσείο βρίσκεται απέναντι από τη βιβλιοθήκη.",
        "example_en": "In the old town, the museum is located across from the library.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Giving cultural landmark coordinates"
    },
    {
        "id": "A1-U103B-019",
        "greek": "Υπάρχει ένα μεγάλο πάρκο μπροστά από το νοσοκομείο.",
        "phonetic_hint": "ee-PAHR-khee EH-nah meh-GHAH-lo PAHR-ko bro-STAH ah-POH to no-so-ko-MEE-o",
        "english": "There is a large park in front of the hospital.",
        "notes": "Klik A1 p. 63. Grammar: existential impersonal verb 'υπάρχει' + 'μπροστά από το'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μπορείς να ξεκουραστείς εκεί, υπάρχει ένα μεγάλο πάρκο μπροστά από το νοσοκομείο.",
        "example_en": "You can rest there, there is a large park in front of the hospital.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Stating existence of green spaces in front of landmarks"
    },
    {
        "id": "A1-U103B-020",
        "greek": "Το γυμναστήριο είναι ακριβώς πίσω από το σχολείο.",
        "phonetic_hint": "to yeem-nah-STEE-ree-o EE-neh ah-kree-VOHS PEE-so ah-POH to sko-LEE-o",
        "english": "The gym is right behind the school.",
        "notes": "Klik A1 p. 63, 64. Grammar: spatial phrase 'πίσω από το' + neuter accusative.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Για να παίξεις μπάσκετ, το γυμναστήριο είναι ακριβώς πίσω από το σχολείο.",
        "example_en": "To play basketball, the gym is right behind the school.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Locating sports facilities behind educational buildings"
    },
    {
        "id": "A1-U103B-021",
        "greek": "Τι έχει πίσω από την εκκλησία; — Έχει ένα μικρό πάρκο.",
        "phonetic_hint": "tee EH-khee PEE-so ah-POH teen ek-lee-SEE-ah? — EH-khee EH-nah mee-KROH PAHR-ko",
        "english": "What is behind the church? — There is a small park.",
        "notes": "Klik A1 p. 64. Grammar: interrogative structure with 'έχει' (impersonal 'there is') + 'πίσω από την'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι έχει πίσω από την εκκλησία; — Έχει ένα μικρό πάρκο με παγκάκια.",
        "example_en": "— What is behind the church? — There is a small park with benches.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about and describing urban backspaces"
    },
    {
        "id": "A1-U103B-022",
        "greek": "Το ξενοδοχείο είναι πάνω στην πλατεία Αριστοτέλους.",
        "phonetic_hint": "to kseh-no-tho-KHEE-o EE-neh PAH-no steen plah-TEE-ah ah-ree-sto-TEH-loos",
        "english": "The hotel is right on Aristotelous Square.",
        "notes": "Klik A1 p. 65. Grammar: spatial expression 'πάνω στην' indicating prime location right on a square.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η θέα είναι υπέροχη επειδή το ξενοδοχείο είναι πάνω στην πλατεία Αριστοτέλους.",
        "example_en": "The view is wonderful because the hotel is right on Aristotelous Square.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Highlighting prime hotel location on main civic plazas"
    },
    {
        "id": "A1-U103B-023",
        "greek": "Το σούπερ μάρκετ είναι ανάμεσα στην τράπεζα και στο φαρμακείο.",
        "phonetic_hint": "to SOO-pehr MAHR-ket EE-neh ah-NAH-meh-sah steen TRAH-peh-zah keh sto fahr-mah-KEE-o",
        "english": "The supermarket is between the bank and the pharmacy.",
        "notes": "Klik A1 p. 63. Grammar: spatial correlative 'ανάμεσα σε... και σε...' with feminine and neuter articles.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Θα το βρεις εύκολα: το σούπερ μάρκετ είναι ανάμεσα στην τράπεζα και στο φαρμακείο.",
        "example_en": "You will find it easily: the supermarket is between the bank and the pharmacy.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Providing precise relative positioning between two businesses"
    },
    {
        "id": "A1-U103B-024",
        "greek": "Η σχολή είναι πολύ κοντά και πηγαίνω πάντα με τα πόδια.",
        "phonetic_hint": "ee sko-LEE EE-neh po-LEE kon-DAH keh pee-YEH-no PAHN-dah meh tah POH-thyah",
        "english": "The school is very close and I always go on foot.",
        "notes": "Klik A1 p. 65. Grammar: adverbial phrase of proximity 'πολύ κοντά' linked to habitual motion.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Δεν παίρνω λεωφορείο: η σχολή είναι πολύ κοντά και πηγαίνω πάντα με τα πόδια.",
        "example_en": "I don't take a bus: the school is very close and I always go on foot.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing pedestrian commuting based on close proximity"
    },

    # =========================================================================
    # 3. Present Tense Type A Verbs in Context (pp. 65-66)
    # =========================================================================
    {
        "id": "A1-U103B-025",
        "greek": "Εγώ μένω στην Αθήνα, αλλά οι γονείς μου μένουν στο χωριό.",
        "phonetic_hint": "eh-GHOH MEH-no steen ah-THEE-nah, ah-LAH ee gho-NEES moo MEH-noon sto kho-RYOH",
        "english": "I live in Athens, but my parents live in the village.",
        "notes": "Klik A1 p. 66. Grammar: 1st person singular 'μένω' vs 3rd person plural 'μένουν' of verb μένω.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Εγώ μένω στην Αθήνα λόγω δουλειάς, αλλά οι γονείς μου μένουν στο χωριό.",
        "example_en": "I live in Athens due to work, but my parents live in the village.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Contrasting individual urban residence with parental rural living"
    },
    {
        "id": "A1-U103B-026",
        "greek": "Εσύ πού μένεις; — Μένω με δύο φίλους μου.",
        "phonetic_hint": "eh-SEE poo MEH-nees? — MEH-no meh THEE-o FEE-loos moo",
        "english": "Where do you live? — I live with two friends of mine.",
        "notes": "Klik A1 p. 55, 66. Grammar: 2nd person singular question 'πού μένεις' + accommodation response with 'με'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Εσύ πού μένεις; — Μένω με δύο φίλους μου σε ένα μεγάλο διαμέρισμα.",
        "example_en": "— Where do you live? — I live with two friends of mine in a big apartment.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking and answering about shared living arrangements"
    },
    {
        "id": "A1-U103B-027",
        "greek": "Η Βίβιαν και η Άννα σπουδάζουν νομική στην Ελλάδα.",
        "phonetic_hint": "ee VEE-vee-ahn keh ee AH-nah spoo-THAH-zoon no-mee-KEE steen eh-LAH-thah",
        "english": "Vivian and Anna study law in Greece.",
        "notes": "Klik A1 p. 65, 66. Grammar: 3rd person plural 'σπουδάζουν' (< σπουδάζω) + direct object of discipline.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Είναι συμφοιτήτριες: η Βίβιαν και η Άννα σπουδάζουν νομική στην Ελλάδα.",
        "example_en": "They are fellow students: Vivian and Anna study law in Greece.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing university studies of third persons"
    },
    {
        "id": "A1-U103B-028",
        "greek": "Τι σπουδάζεις στο πανεπιστήμιο; — Σπουδάζω ιατρική.",
        "phonetic_hint": "tee spoo-THAH-zees sto pah-neh-pee-STEE-mee-o? — spoo-THAH-zo yah-tree-KEE",
        "english": "What do you study at university? — I study medicine.",
        "notes": "Klik A1 p. 65, 66. Grammar: 2nd person singular 'σπουδάζεις' and 1st person singular 'σπουδάζω'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι σπουδάζεις στο πανεπιστήμιο; — Σπουδάζω ιατρική και είμαι στο δεύτερο έτος.",
        "example_en": "— What do you study at university? — I study medicine and I am in the second year.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about and stating one's field of study"
    },
    {
        "id": "A1-U103B-029",
        "greek": "Ο Χρήστος αρχίζει φέτος τα μαθήματα στη σχολή.",
        "phonetic_hint": "o KHREE-stos ahr-KHEE-zee FEH-tos tah mah-THEE-mah-tah stee sko-LEE",
        "english": "Christos starts classes at the university school this year.",
        "notes": "Klik A1 p. 66. Grammar: 3rd person singular verb 'αρχίζει' (< αρχίζω) + temporal adverb 'φέτος'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Είναι πρωτοετής: ο Χρήστος αρχίζει φέτος τα μαθήματα στη σχολή.",
        "example_en": "He is a freshman: Christos starts classes at university this year.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Announcing commencement of university academic year"
    },
    {
        "id": "A1-U103B-030",
        "greek": "Το μάθημα αρχίζει στις εννέα το πρωί.",
        "phonetic_hint": "to MAH-thee-mah ahr-KHEE-zee stees eh-NEH-ah to proh-EE",
        "english": "The lesson starts at nine in the morning.",
        "notes": "Klik A1 p. 60, 66. Grammar: intransitive 3rd person singular 'αρχίζει' with exact clock time.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πρέπει να ξυπνήσεις νωρίς, γιατί το μάθημα αρχίζει στις εννέα το πρωί.",
        "example_en": "You need to wake up early, because the class starts at nine in the morning.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Stating class start time with numbers"
    },
    {
        "id": "A1-U103B-031",
        "greek": "Πίνουμε έναν ελληνικό καφέ στην καφετέρια της πλατείας.",
        "phonetic_hint": "PEE-noo-meh EH-nahn eh-lee-nee-KOH kah-FEH steen kah-feh-TEH-ree-ah tees plah-TEE-as",
        "english": "We are drinking a Greek coffee at the cafe on the square.",
        "notes": "Klik A1 p. 62, 66. Grammar: 1st person plural 'πίνουμε' (< πίνω) + accusative direct object.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Έλα μαζί μας: πίνουμε έναν ελληνικό καφέ στην καφετέρια της πλατείας.",
        "example_en": "Come join us: we are drinking a Greek coffee at the cafe on the square.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing shared social coffee habits"
    },
    {
        "id": "A1-U103B-032",
        "greek": "Τι πίνετε; — Πίνω ένα παγωμένο τσάι.",
        "phonetic_hint": "tee PEE-neh-teh? — PEE-no EH-nah pah-gho-MEH-no TSAH-ee",
        "english": "What are you drinking? — I am drinking an iced tea.",
        "notes": "Klik A1 p. 66. Grammar: 2nd plural/polite question 'τι πίνετε' + 1st singular response 'πίνω'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Καλώς ήρθατε, τι πίνετε; — Πίνω ένα παγωμένο τσάι με λεμόνι.",
        "example_en": "— Welcome, what are you having to drink? — I am drinking an iced tea with lemon.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Ordering and stating beverage choices"
    },
    {
        "id": "A1-U103B-033",
        "greek": "Τι κάνουν τα παιδιά τώρα; — Διαβάζουν στο δωμάτιό τους.",
        "phonetic_hint": "tee KAH-noon tah peh-THYAH TOH-rah? — thyah-VAH-zoon sto tho-MAH-tee-OH toos",
        "english": "What are the children doing now? — They are studying in their room.",
        "notes": "Klik A1 p. 65, 66. Grammar: 3rd person plural verb pair 'κάνουν' and 'διαβάζουν'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι κάνουν τα παιδιά τώρα; — Διαβάζουν στο δωμάτιό τους για το σχολείο.",
        "example_en": "— What are the children doing now? — They are studying in their room for school.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about ongoing activities of family members"
    },
    {
        "id": "A1-U103B-034",
        "greek": "Ξέρεις πού είναι το ταχυδρομείο; — Ναι, είναι στην επόμενη γωνία.",
        "phonetic_hint": "KSEH-rees poo EE-neh to tah-khee-thro-MEE-o? — neh, EE-neh steen eh-POH-meh-nee gho-NEE-ah",
        "english": "Do you know where the post office is? — Yes, it is on the next corner.",
        "notes": "Klik A1 p. 64, 66. Grammar: verb 'ξέρω' (2nd person singular 'ξέρεις') introducing an indirect question.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Συγγνώμη, ξέρεις πού είναι το ταχυδρομείο; — Ναι, είναι στην επόμενη γωνία, δίπλα στην τράπεζα.",
        "example_en": "— Excuse me, do you know where the post office is? — Yes, it is on the next corner, next to the bank.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking for and receiving directions on street corners"
    },
    {
        "id": "A1-U103B-035",
        "greek": "Δεν καταλαβαίνω αυτή τη λέξη, τι σημαίνει στα ελληνικά;",
        "phonetic_hint": "then kah-tah-lah-VEH-no ahf-TEEN tee LEH-ksee, tee see-MEH-nee stah eh-lee-nee-KAH",
        "english": "I don't understand this word, what does it mean in Greek?",
        "notes": "Klik A1 p. 56. Grammar: negated Type A verb 'δεν καταλαβαίνω' + definition question 'τι σημαίνει'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Είμαι αρχάριος: δεν καταλαβαίνω αυτή τη λέξη, τι σημαίνει στα ελληνικά;",
        "example_en": "I am a beginner: I don't understand this word, what does it mean in Greek?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Requesting clarification of unfamiliar Greek vocabulary"
    },
    {
        "id": "A1-U103B-036",
        "greek": "Καταλαβαίνετε τι λέει ο καθηγητής; — Ναι, μιλάει πολύ καθαρά.",
        "phonetic_hint": "kah-tah-lah-VEH-neh-teh tee LEH-ee o kah-thee-yee-TEES? — neh, mee-LAH-ee po-LEE kah-thah-RAH",
        "english": "Do you understand what the professor is saying? — Yes, he speaks very clearly.",
        "notes": "Klik A1 p. 56, 66. Grammar: 2nd person plural 'καταλαβαίνετε' + 3rd person singular 'μιλάει'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Καταλαβαίνετε τι λέει ο καθηγητής; — Ναι, μιλάει πολύ καθαρά και αργά.",
        "example_en": "— Do you understand what the teacher is saying? — Yes, he speaks very clearly and slowly.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Evaluating academic speech comprehension in class"
    },

    # =========================================================================
    # 4. Inquiring & Giving Address Details, Street, Number & Telephone (pp. 56-57, 60, 68)
    # =========================================================================
    {
        "id": "A1-U103B-037",
        "greek": "Ποια είναι η διεύθυνσή σου; — Μένω στην οδό Ερμού, αριθμός δέκα.",
        "phonetic_hint": "PYAH EE-neh ee dhyEH-fteen-SEE soo? — MEH-no steen oh-THOH ehr-MOO, ah-reeth-MOHS THEH-kah",
        "english": "What is your address? — I live on Ermou Street, number ten.",
        "notes": "Klik A1 p. 56, 57. Grammar: feminine interrogative 'ποια' + address formula 'οδός... αριθμός...'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Για την εγγραφή, ποια είναι η διεύθυνσή σου; — Μένω στην οδό Ερμού, αριθμός δέκα.",
        "example_en": "— For registration, what is your address? — I live on Ermou Street, number ten.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about and stating official home address"
    },
    {
        "id": "A1-U103B-038",
        "greek": "Ποιο είναι το τηλέφωνό σου; — Το τηλέφωνό μου είναι δύο, ένα, μηδέν...",
        "phonetic_hint": "PYOH EE-neh to tee-LEH-fo-NOH soo? — to tee-LEH-fo-NOH moo EE-neh THEE-o, EH-nah, mee-THEN...",
        "english": "What is your telephone number? — My telephone number is two, one, zero...",
        "notes": "Klik A1 p. 56, 57, 60. Grammar: neuter interrogative 'ποιο' + digit-by-digit cardinal numbers recitation.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ποιο είναι το τηλέφωνό σου; — Το τηλέφωνό μου είναι 210-7654321.",
        "example_en": "— What is your phone number? — My telephone number is 210-7654321.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking for and reciting landline telephone digits"
    },
    {
        "id": "A1-U103B-039",
        "greek": "Έχεις κινητό; — Ναι, το κινητό μου είναι 697-1234567.",
        "phonetic_hint": "EH-khees kee-nee-TOH? — neh, to kee-nee-TOH moo EE-neh...",
        "english": "Do you have a mobile phone? — Yes, my mobile is 697-1234567.",
        "notes": "Klik A1 p. 57, 68. Grammar: Greek mobile telephone standard prefix '69' (έξι, εννέα...).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Έχεις κινητό για να σου στείλω μήνυμα; — Ναι, το κινητό μου είναι 697-1234567.",
        "example_en": "— Do you have a cell phone so I can text you? — Yes, my cell is 697-1234567.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Exchanging mobile phone numbers for text messaging"
    },
    {
        "id": "A1-U103B-040",
        "greek": "Ποιος είναι ο ταχυδρομικός κώδικας της περιοχής;",
        "phonetic_hint": "PYOHS EE-neh o tah-khee-thro-mee-KOHS KOH-thee-kahs tees peh-ree-o-KHEES",
        "english": "What is the postal code of the area?",
        "notes": "Klik A1 p. 56, 57. Grammar: masculine noun phrase 'ο ταχυδρομικός κώδικας' (Τ.Κ.).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Γράφω το γράμμα. Ποιος είναι ο ταχυδρομικός κώδικας της περιοχής; — Είναι 54250.",
        "example_en": "— I am writing the letter. What is the postal code of the area? — It is 54250.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about Greek postal codes for mailing"
    },
    {
        "id": "A1-U103B-041",
        "greek": "Συμπληρώνω την αίτηση με το όνομα και το επώνυμό μου.",
        "phonetic_hint": "seem-blee-ROH-no teen EH-tee-see meh to OH-no-mah keh to eh-POH-nee-MOH moo",
        "english": "I am filling out the application form with my first name and surname.",
        "notes": "Klik A1 p. 56, 57. Grammar: administrative action verb 'συμπληρώνω' + double accent 'επώνυμό μου'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Στη γραμματεία της σχολής, συμπληρώνω την αίτηση με το όνομα και το επώνυμό μου.",
        "example_en": "At the school secretariat, I fill out the application with my first name and surname.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing the process of completing official Greek forms"
    },
    {
        "id": "A1-U103B-042",
        "greek": "Ποια είναι η πόλη καταγωγής σου; — Η καταγωγή μου είναι από τα Χανιά.",
        "phonetic_hint": "PYAH EE-neh ee POH-lee kah-tah-gho-YEES soo? — ee kah-tah-gho-YEE moo EE-neh ah-POH tah khah-NYAH",
        "english": "What is your city of origin? — My origin is from Chania.",
        "notes": "Klik A1 p. 55, 57. Grammar: genitive attribute 'πόλη καταγωγής' and noun 'η καταγωγή μου'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ποια είναι η πόλη καταγωγής σου; — Η καταγωγή μου είναι από τα Χανιά της Κρήτης.",
        "example_en": "— What is your city of origin? — My origin is from Chania in Crete.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Stating ancestral roots and hometown origin"
    },
    {
        "id": "A1-U103B-043",
        "greek": "Πόσο κάνει δύο συν τρία; — Δύο συν τρία κάνει πέντε.",
        "phonetic_hint": "POH-so KAH-nee THEE-o seen TREE-ah? — THEE-o seen TREE-ah KAH-nee PEN-deh",
        "english": "How much is two plus three? — Two plus three equals five.",
        "notes": "Klik A1 p. 60. Grammar: arithmetical calculation question 'πόσο κάνει' with addition preposition 'συν'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Στο μάθημα των μαθηματικών: πόσο κάνει δύο συν τρία; — Δύο συν τρία κάνει πέντε.",
        "example_en": "In math class: how much is two plus three? — Two plus three makes five.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Doing basic addition with Greek cardinal numbers 0-10"
    },
    {
        "id": "A1-U103B-044",
        "greek": "Έχω τρία βιβλία και τέσσερα τετράδια στο σακίδιό μου.",
        "phonetic_hint": "EH-kho TREE-ah veev-LEE-ah keh TEH-seh-rah teh-TRAH-thyah sto sah-KEE-dhyOH moo",
        "english": "I have three books and four notebooks in my backpack.",
        "notes": "Klik A1 p. 60. Grammar: agreement of inflected numbers: neuter nominative/accusative 'τρία' and 'τέσσερα'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Για το μάθημα έχω τρία βιβλία και τέσσερα τετράδια στο σακίδιό μου.",
        "example_en": "For class I have three books and four notebooks in my backpack.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Counting school supplies with inflected numerals 3 and 4"
    },

    # =========================================================================
    # 5. Conversational Dialogue Formulas & Living Arrangements (pp. 55, 62, 65, 67)
    # =========================================================================
    {
        "id": "A1-U103B-045",
        "greek": "Πώς είσαι; — Είμαι πολύ καλά, ευχαριστώ. Εσύ τι κάνεις;",
        "phonetic_hint": "pos EE-seh? — EE-meh po-LEE kah-LAH, ef-khah-ree-STOH. eh-SEE tee KAH-nees",
        "english": "How are you? — I am very well, thank you. How are you doing?",
        "notes": "Klik A1 p. 56, 67. Standard everyday Greek greeting and reciprocation exchange.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Γεια σου, Δήμητρα! Πώς είσαι; — Είμαι πολύ καλά, ευχαριστώ. Εσύ τι κάνεις;",
        "example_en": "— Hello, Dimitra! How are you? — I am very well, thank you. How are you doing?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Greeting friends and politely reciprocating inquiries about health"
    },
    {
        "id": "A1-U103B-046",
        "greek": "Μένεις μόνος σου ή έχεις συγκάτοικο; — Μένω με έναν φίλο μου.",
        "phonetic_hint": "MEH-nees MOH-nos soo ee EH-khees seen-GAH-tee-ko? — MEH-no meh EH-nahn FEE-lo moo",
        "english": "Do you live alone or do you have a roommate? — I live with a friend of mine.",
        "notes": "Klik A1 p. 62, 67. Idiom 'μόνος σου' (alone/by yourself) vs 'συγκάτοικος' (roommate).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Στο καινούριο σπίτι μένεις μόνος σου ή έχεις συγκάτοικο; — Μένω με έναν φίλο μου.",
        "example_en": "— In the new house do you live alone or do you have a roommate? — I live with a friend of mine.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Discussing independent living vs living with roommates"
    },
    {
        "id": "A1-U103B-047",
        "greek": "Το διαμέρισμά μου είναι πολύ φωτεινό, ήσυχο και άνετο.",
        "phonetic_hint": "to dhyah-MEH-ree-ZMAH moo EE-neh po-LEE fo-tee-NOH, EE-see-kho keh AH-neh-to",
        "english": "My apartment is very bright, quiet, and comfortable.",
        "notes": "Klik A1 p. 62, 67. Grammar: neuter descriptive adjectives modifying 'το διαμέρισμα'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μου αρέσει πολύ η νέα γειτονιά, γιατί το διαμέρισμά μου είναι πολύ φωτεινό, ήσυχο και άνετο.",
        "example_en": "I really like the new neighborhood, because my apartment is very bright, quiet, and comfortable.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Praising the qualities of one's apartment"
    },
    {
        "id": "A1-U103B-048",
        "greek": "Κάνουμε συχνά παρέα τα απογεύματα μετά τη σχολή.",
        "phonetic_hint": "KAH-noo-meh see-KHNAH pah-REH-ah tah ah-po-YEV-mah-tah meh-TAH tee sko-LEE",
        "english": "We often hang out in the afternoons after university.",
        "notes": "Klik A1 p. 56, 65, 68. Greek cultural idiom 'κάνω παρέα' (hang out / spend time with friends).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Είμαστε καλοί φίλοι και κάνουμε συχνά παρέα τα απογεύματα μετά τη σχολή.",
        "example_en": "We are good friends and we often hang out in the afternoons after school.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing recurring social gatherings with classmates"
    },
    {
        "id": "A1-U103B-049",
        "greek": "Συγγνώμη, μήπως ξέρετε πού είναι το πλησιέστερο φαρμακείο;",
        "phonetic_hint": "see-GNOH-mee, MEE-pos KSEH-reh-teh poo EE-neh to plee-see-EH-steh-ro fahr-mah-KEE-o",
        "english": "Excuse me, do you happen to know where the nearest pharmacy is?",
        "notes": "Klik A1 p. 63, 67. Polite inquiry formula: 'συγγνώμη' + 'μήπως' + 2nd plural 'ξέρετε'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Συγγνώμη, μήπως ξέρετε πού είναι το πλησιέστερο φαρμακείο; — Ναι, απέναντι από την τράπεζα.",
        "example_en": "— Excuse me, do you happen to know where the nearest pharmacy is? — Yes, across from the bank.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Politely requesting directions to urgent neighborhood services"
    },
    {
        "id": "A1-U103B-050",
        "greek": "Περνάμε πάρα πολύ καλά στη νέα μας γειτονιά.",
        "phonetic_hint": "per-NAH-meh PAH-rah po-LEE kah-LAH stee NEH-ah mahs yee-to-NYAH",
        "english": "We are having a very good time in our new neighborhood.",
        "notes": "Klik A1 p. 56, 68. Verbal idiom 'περνάω καλά' in 1st plural 'περνάμε πάρα πολύ καλά'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Όλοι οι γείτονες είναι ευγενικοί και περνάμε πάρα πολύ καλά στη νέα μας γειτονιά.",
        "example_en": "All the neighbors are polite and we are having a very good time in our new neighborhood.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing collective contentment with community environment"
    }
]

lesson_u103b = {
    "unit_id": "unit-103b",
    "lesson_id": "lesson-01",
    "title": "Ενότητα 2: Προτάσεις & Γραμματική — Κατοικία, Προθέσεις (σε/από), Ρήματα σε -ω & Τοπικοί Προσδιορισμοί (Pages 55-68)",
    "description": "Expansion & Complementary to Lesson 103: Sentence structures, syntax patterns, locative prepositions merged with accusative articles (στον/στη/στο, από τον/τη/το), Type A verb conjugations (-ω), and spatial expressions (κοντά, δίπλα, απέναντι).",
    "entries": cards_u103b
}

def main():
    print(f"Writing {len(cards_u103b)} cards to {YAML_PATH}...")
    with open(YAML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(lesson_u103b, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("YAML successfully written.")

    # Update manifest.yaml
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    units = manifest.get("units", [])
    existing = next((u for u in units if u.get("id") == "unit-103b"), None)
    unit_103b_entry = {
        "id": "unit-103b",
        "title": "Κλικ στα Ελληνικά Α1: Σελίδες 55-68 (Ενότητα 2: Πού μένεις; - Γραμματική & Προτάσεις)",
        "order": "KlikA1-03-B",
        "is_expansion": True,
        "expansion_of": "KlikA1-03-A",
        "lessons": [
            {
                "id": "lesson-01",
                "file": "unit-103b/lesson-01.yaml",
                "title": "Ενότητα 2: Προτάσεις & Γραμματική — Κατοικία, Προθέσεις (σε/από), Ρήματα σε -ω & Τοπικοί Προσδιορισμοί (Pages 55-68)",
                "description": "Expansion & Complementary to Lesson 103: Sentence structures, syntax patterns, locative prepositions merged with accusative articles (στον/στη/στο, από τον/τη/το), Type A verb conjugations (-ω), and spatial expressions (κοντά, δίπλα, απέναντι)."
            }
        ]
    }

    if existing:
        print("Updating existing unit-103b in manifest.yaml...")
        idx = units.index(existing)
        units[idx] = unit_103b_entry
    else:
        # Insert immediately after unit-103 if found, otherwise append
        u103_idx = next((i for i, u in enumerate(units) if u.get("id") == "unit-103"), None)
        if u103_idx is not None:
            print(f"Inserting unit-103b immediately after unit-103 (at index {u103_idx + 1})...")
            units.insert(u103_idx + 1, unit_103b_entry)
        else:
            print("Appending unit-103b to manifest.yaml...")
            units.append(unit_103b_entry)

    manifest["units"] = units

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("Manifest successfully updated with unit-103b!")

if __name__ == "__main__":
    main()

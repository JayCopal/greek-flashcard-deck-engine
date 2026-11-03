# -*- coding: utf-8 -*-
"""
Script to create Unit 105 B from Klik A1 (Pages 87-110):
Ενότητα 4: Από το πρωί μέχρι το βράδυ - Γραμματική & Προτάσεις
Focuses on full sentences, grammar structures, accusative case transforms,
verb conjugations (πάω, ακούω, λέω, τρώω, κοιμάμαι, έρχομαι), time telling,
and daily routine expressions.
"""
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
UNIT_DIR = CONTENT_DIR / "unit-105b"
UNIT_DIR.mkdir(parents=True, exist_ok=True)
YAML_PATH = UNIT_DIR / "lesson-01.yaml"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

cards_u105b = [
    # =========================================================================
    # 1. Preferences: "Μου αρέσει / Μου αρέσουν / Δεν μου αρέσει να..." (pp. 88-89)
    # =========================================================================
    {
        "id": "A1-U105B-001",
        "greek": "Μου αρέσει πολύ η κλασική μουσική.",
        "phonetic_hint": "moo ah-REH-see poh-LEE ee klah-see-KEE moo-see-KEE",
        "english": "I really like classical music.",
        "notes": "Klik A1 p. 88-89. Grammar: 'μου αρέσει' + singular nominative subject (η κλασική μουσική).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Σου αρέσει η όπερα; — Ναι, μου αρέσει πολύ η κλασική μουσική.",
        "example_en": "— Do you like opera? — Yes, I really like classical music.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing personal taste and musical preferences"
    },
    {
        "id": "A1-U105B-002",
        "greek": "Σου αρέσει ο κινηματογράφος;",
        "phonetic_hint": "soo ah-REH-see oh kee-nee-mah-toh-GRAH-fos",
        "english": "Do you like the cinema / movies?",
        "notes": "Klik A1 p. 88-89. Grammar: question with second person pronoun 'σου' + 'αρέσει' + singular noun.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Σου αρέσει ο κινηματογράφος; — Ναι, πάω κάθε Παρασκευή.",
        "example_en": "— Do you like cinema? — Yes, I go every Friday.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about someone's hobbies and leisure preferences"
    },
    {
        "id": "A1-U105B-003",
        "greek": "Μου αρέσουν τα παλιά βιβλία και τα μουσεία.",
        "phonetic_hint": "moo ah-REH-soon tah pah-LYAH veev-LEE-ah keh tah moo-SEE-ah",
        "english": "I like old books and museums.",
        "notes": "Klik A1 p. 89. Grammar: 'μου αρέσουν' (plural verb form) with plural subjects (τα βιβλία, τα μουσεία).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Στην Αθήνα επισκέπτομαι συχνά την Πλάκα γιατί μου αρέσουν τα παλιά βιβλία και τα μουσεία.",
        "example_en": "In Athens I often visit Plaka because I like old books and museums.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing likes with plural direct subjects"
    },
    {
        "id": "A1-U105B-004",
        "greek": "Δεν μου αρέσουν οι ταινίες τρόμου.",
        "phonetic_hint": "then moo ah-REH-soon ee teh-NEE-es TROH-moo",
        "english": "I don't like horror movies.",
        "notes": "Klik A1 p. 89. Grammar: negation 'δεν' + 'μου αρέσουν' + feminine plural noun phrase 'οι ταινίες τρόμου'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Προτιμώ τις κωμωδίες επειδή δεν μου αρέσουν οι ταινίες τρόμου.",
        "example_en": "I prefer comedies because I do not like horror movies.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing dislikes and movie genre preferences"
    },
    {
        "id": "A1-U105B-005",
        "greek": "Μου αρέσει να κάνω βόλτες στην πόλη.",
        "phonetic_hint": "moo ah-REH-see nah KAH-noh VOHL-tes steen POH-lee",
        "english": "I like taking walks in the city.",
        "notes": "Klik A1 p. 89. Grammar: 'μου αρέσει να' + present subjunctive verb (κάνω) for ongoing/habitual action.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Όταν έχει καλό καιρό, μου αρέσει να κάνω βόλτες στην πόλη.",
        "example_en": "When the weather is good, I like taking walks in the city.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing enjoyment of activities using subjunctive 'να'"
    },
    {
        "id": "A1-U105B-006",
        "greek": "Της αρέσει να μαγειρεύει για τους φίλους της.",
        "phonetic_hint": "tees ah-REH-see nah mah-yee-REH-vee yah toos FEE-loos tees",
        "english": "She likes cooking for her friends.",
        "notes": "Klik A1 p. 89. Grammar: weak indirect pronoun 'της' (her) + 'αρέσει να' + third person singular verb (μαγειρεύει).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η Ελένη είναι εξαιρετική μαγείρισσα και της αρέσει να μαγειρεύει για τους φίλους της.",
        "example_en": "Eleni is an excellent cook and she likes cooking for her friends.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing someone else's hobbies and leisure activities"
    },
    {
        "id": "A1-U105B-007",
        "greek": "Δεν μου αρέσει να ξυπνάω πολύ νωρίς.",
        "phonetic_hint": "then moo ah-REH-see nah ksee-PNAH-oh poh-LEE noh-REES",
        "english": "I don't like waking up very early.",
        "notes": "Klik A1 p. 89, 98. Grammar: negative 'δεν' + 'μου αρέσει να' + contract verb (ξυπνάω) + adverb (νωρίς).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τις καθημερινές ξυπνάω στις έξι, αλλά δεν μου αρέσει να ξυπνάω πολύ νωρίς.",
        "example_en": "On weekdays I wake up at six, but I don't like waking up very early.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing reluctance regarding morning habits"
    },
    {
        "id": "A1-U105B-008",
        "greek": "Μας αρέσει να ταξιδεύουμε το καλοκαίρι.",
        "phonetic_hint": "mahs ah-REH-see nah tah-ksee-THEHV-oo-meh toh kah-loh-KEH-ree",
        "english": "We like traveling in the summer.",
        "notes": "Klik A1 p. 89. Grammar: plural weak pronoun 'μας' (us) + 'αρέσει να' + first-person plural verb (ταξιδεύουμε).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κάθε χρόνο παίρνουμε άδεια τον Αύγουστο επειδή μας αρέσει να ταξιδεύουμε το καλοκαίρι.",
        "example_en": "Every year we take leave in August because we like traveling in the summer.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing shared group preferences and vacation habits"
    },

    # =========================================================================
    # 2. Accusative Direct Objects: Singular & Plural Pairs (pp. 93-96)
    # =========================================================================
    {
        "id": "A1-U105B-009",
        "greek": "Βλέπω τον αγώνα ποδοσφαίρου στην τηλεόραση.",
        "phonetic_hint": "VLEH-poh ton ah-GHO-nah poh-thos-FEH-roo steen tee-leh-OH-rah-see",
        "english": "I am watching the football match on television.",
        "notes": "Klik A1 p. 93-94. Grammar: masculine accusative singular 'τον αγώνα' (< ο αγώνας).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι κάνεις τώρα; — Βλέπω τον αγώνα ποδοσφαίρου στην τηλεόραση.",
        "example_en": "— What are you doing now? — I am watching the football match on TV.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Using masculine accusative singular direct objects"
    },
    {
        "id": "A1-U105B-010",
        "greek": "Παρακολουθούμε όλους τους αγώνες της ομάδας.",
        "phonetic_hint": "pah-rah-koh-loo-THOO-meh OH-loos toos ah-GHOH-nes tees oh-MAH-thas",
        "english": "We watch all the matches of the team.",
        "notes": "Klik A1 p. 94. Grammar: masculine accusative plural 'τους αγώνες' (< οι αγώνες).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Είμαστε μεγάλοι φίλαθλοι και παρακολουθούμε όλους τους αγώνες της ομάδας.",
        "example_en": "We are big sports fans and we watch all the matches of the team.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Using masculine accusative plural direct objects"
    },
    {
        "id": "A1-U105B-011",
        "greek": "Περιμένω τον φίλο μου στον σταθμό.",
        "phonetic_hint": "peh-ree-MEH-noh ton FEE-loh moo ston stahth-MOH",
        "english": "I am waiting for my friend at the station.",
        "notes": "Klik A1 p. 93-94. Grammar: masculine accusative singular 'τον φίλο' (< ο φίλος).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Είμαι έξω από το μετρό και περιμένω τον φίλο μου στον σταθμό.",
        "example_en": "I am outside the metro and waiting for my friend at the station.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Indicating meeting locations with accusative singular direct objects"
    },
    {
        "id": "A1-U105B-012",
        "greek": "Περιμένουμε τους φίλους μας για δείπνο.",
        "phonetic_hint": "peh-ree-MEH-noo-meh toos FEE-loos mahs yah THEEP-noh",
        "english": "We are waiting for our friends for dinner.",
        "notes": "Klik A1 p. 94. Grammar: masculine accusative plural 'τους φίλους' (< οι φίλοι).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το τραπέζι είναι έτοιμο και περιμένουμε τους φίλους μας για δείπνο.",
        "example_en": "The table is ready and we are waiting for our friends for dinner.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing hospitality with accusative plural direct objects"
    },
    {
        "id": "A1-U105B-013",
        "greek": "Ο παππούς καθαρίζει τον κήπο κάθε πρωί.",
        "phonetic_hint": "oh pah-POOS kah-thah-REE-zee ton KEE-poh KAH-theh proh-EE",
        "english": "Grandfather cleans the garden every morning.",
        "notes": "Klik A1 p. 93-94. Grammar: masculine accusative singular 'τον κήπο' (< ο κήπος).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο παππούς αγαπάει τα λουλούδια και καθαρίζει τον κήπο κάθε πρωί.",
        "example_en": "Grandfather loves flowers and cleans the garden every morning.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing outdoor chores with accusative nouns"
    },
    {
        "id": "A1-U105B-014",
        "greek": "Οι γείτονες καθαρίζουν τους κήπους τους την άνοιξη.",
        "phonetic_hint": "ee YEE-toh-nes kah-thah-REE-zoon toos KEE-poos toos teen AH-neek-see",
        "english": "The neighbors clean their gardens in spring.",
        "notes": "Klik A1 p. 94. Grammar: masculine accusative plural 'τους κήπους' (< οι κήποι).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Όταν ανοίγει ο καιρός, οι γείτονες καθαρίζουν τους κήπους τους την άνοιξη.",
        "example_en": "When the weather warms up, the neighbors clean their gardens in the spring.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing seasonal activities with masculine plural accusative"
    },
    {
        "id": "A1-U105B-015",
        "greek": "Διαβάζω την πρωινή εφημερίδα με τον καφέ μου.",
        "phonetic_hint": "thyah-VAH-zoh teen proh-ee-NEE eh-fee-meh-REE-thah meh ton kah-FEH moo",
        "english": "I read the morning newspaper with my coffee.",
        "notes": "Klik A1 p. 93, 95. Grammar: feminine accusative singular 'την πρωινή εφημερίδα' (< η εφημερίδα).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κάθε μέρα πριν από τη δουλειά διαβάζω την πρωινή εφημερίδα με τον καφέ μου.",
        "example_en": "Every day before work I read the morning newspaper with my coffee.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Talking about reading habits with feminine accusative singular"
    },
    {
        "id": "A1-U105B-016",
        "greek": "Αγοράζει όλες τις εφημερίδες την Κυριακή.",
        "phonetic_hint": "ah-ghoh-RAH-zee OH-les tees eh-fee-meh-REE-thes teen kee-ryah-KEE",
        "english": "He buys all the newspapers on Sunday.",
        "notes": "Klik A1 p. 95. Grammar: feminine accusative plural 'τις εφημερίδες' (< οι εφημερίδες).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Του αρέσει η ενημέρωση και αγοράζει όλες τις εφημερίδες την Κυριακή.",
        "example_en": "He likes keeping informed and buys all the newspapers on Sunday.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing habitual purchases using feminine accusative plural"
    },
    {
        "id": "A1-U105B-017",
        "greek": "Ανοίγω την πόρτα του σπιτιού.",
        "phonetic_hint": "ah-NEE-ghoh teen POHR-tah too spee-TYOO",
        "english": "I open the door of the house.",
        "notes": "Klik A1 p. 95, 102. Grammar: feminine accusative singular 'την πόρτα' (< η πόρτα).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Γυρίζω από τη δουλειά και ανοίγω την πόρτα του σπιτιού.",
        "example_en": "I return from work and open the door of the house.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing immediate household actions with feminine accusative"
    },
    {
        "id": "A1-U105B-018",
        "greek": "Κλείνει τις πόρτες και τα παράθυρα πριν φύγει.",
        "phonetic_hint": "KLEE-nee tees POHR-tes keh tah pah-RAH-thee-rah preen FEE-yee",
        "english": "She closes the doors and the windows before leaving.",
        "notes": "Klik A1 p. 95. Grammar: feminine accusative plural 'τις πόρτες' + neuter plural 'τα παράθυρα'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Για ασφάλεια κλείνει τις πόρτες και τα παράθυρα πριν φύγει.",
        "example_en": "For safety she closes the doors and the windows before leaving.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing domestic safety measures with mixed plural accusative objects"
    },
    {
        "id": "A1-U105B-019",
        "greek": "Πλένω το πιάτο μετά το μεσημεριανό.",
        "phonetic_hint": "PLEH-noh toh PYAH-toh meh-TAH toh meh-see-meh-ryah-NOH",
        "english": "I wash the plate after lunch.",
        "notes": "Klik A1 p. 95, 98. Grammar: neuter accusative singular 'το πιάτο' (< το πιάτο).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μόλις τελειώνω το φαγητό, πλένω το πιάτο μετά το μεσημεριανό.",
        "example_en": "As soon as I finish eating, I wash the plate after lunch.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing after-meal chores with neuter accusative singular"
    },
    {
        "id": "A1-U105B-020",
        "greek": "Πλένουμε τα πιάτα και τα ποτήρια μαζί.",
        "phonetic_hint": "PLEH-noo-meh tah PYAH-tah keh tah poh-TEE-ryah mah-ZEE",
        "english": "We wash the dishes and the glasses together.",
        "notes": "Klik A1 p. 95. Grammar: neuter accusative plural 'τα πιάτα', 'τα ποτήρια'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μετά το οικογενειακό τραπέζι, πλένουμε τα πιάτα και τα ποτήρια μαζί.",
        "example_en": "After the family dinner, we wash the dishes and glasses together.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing shared household chores with neuter plural accusative"
    },
    {
        "id": "A1-U105B-021",
        "greek": "Αγοράζω ένα νέο βιβλίο κάθε μήνα.",
        "phonetic_hint": "ah-ghoh-RAH-zoh EH-nah NEH-oh veev-LEE-oh KAH-theh MEE-nah",
        "english": "I buy a new book every month.",
        "notes": "Klik A1 p. 95. Grammar: neuter indefinite accusative 'ένα νέο βιβλίο' + frequency expression.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μου αρέσει πολύ το διάβασμα και αγοράζω ένα νέο βιβλίο κάθε μήνα.",
        "example_en": "I love reading and I buy a new book every month.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing monthly routines and purchasing habits"
    },
    {
        "id": "A1-U105B-022",
        "greek": "Διαβάζει πολλά βιβλία τον ελεύθερο χρόνο της.",
        "phonetic_hint": "thyah-VAH-zee poh-LAH veev-LEE-ah ton eh-LEF-theh-roh KHROH-noh tees",
        "english": "She reads many books in her free time.",
        "notes": "Klik A1 p. 87, 95. Grammar: neuter accusative plural 'πολλά βιβλία' + adverbial accusative of time.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η Άννα δεν βλέπει τηλεόραση, αλλά διαβάζει πολλά βιβλία τον ελεύθερο χρόνο της.",
        "example_en": "Anna doesn't watch TV, but reads many books in her free time.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Discussing reading habits and leisure duration"
    },

    # =========================================================================
    # 3. High-Frequency Irregular & Contract Verbs in Context (pp. 93, 107-108)
    # =========================================================================
    {
        "id": "A1-U105B-023",
        "greek": "Πού πας τώρα; — Πάω στο σούπερ μάρκετ.",
        "phonetic_hint": "poo pahs TOH-rah? — PAH-oh stoh SOO-pehr MAHR-ket",
        "english": "Where are you going now? — I am going to the supermarket.",
        "notes": "Klik A1 p. 93, 107. Grammar: verb 'πάω' (πας 2nd sg. / πάω 1st sg.).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πού πας τώρα; — Πάω στο σούπερ μάρκετ για ψώνια.",
        "example_en": "— Where are you going now? — I am going to the supermarket for groceries.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking and answering about current destination"
    },
    {
        "id": "A1-U105B-024",
        "greek": "Πάμε μια βόλτα στην πλατεία;",
        "phonetic_hint": "PAH-meh myah VOHL-tah steen plah-TEE-ah",
        "english": "Shall we go for a walk in the square?",
        "notes": "Klik A1 p. 88, 107. Grammar: verb 'πάμε' (1st person plural) used as a friendly proposal.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Έχει ωραίο απόγευμα. Πάμε μια βόλτα στην πλατεία;",
        "example_en": "It's a nice afternoon. Shall we go for a walk in the square?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Making social invitations and casual suggestions"
    },
    {
        "id": "A1-U105B-025",
        "greek": "Τα παιδιά πάνε στο σχολείο με τα πόδια.",
        "phonetic_hint": "tah peh-THYAH PAH-neh stoh skhoh-LEE-oh meh tah POH-thyah",
        "english": "The children go to school on foot.",
        "notes": "Klik A1 p. 107. Grammar: verb 'πάνε' (3rd person plural) + mode of transport 'με τα πόδια'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το σχολείο είναι κοντά, γι' αυτό τα παιδιά πάνε στο σχολείο με τα πόδια.",
        "example_en": "The school is near, so the children go to school on foot.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing school commuting routines"
    },
    {
        "id": "A1-U105B-026",
        "greek": "Ακούω το ραδιόφωνο στο αυτοκίνητο κάθε πρωί.",
        "phonetic_hint": "ah-KOO-oh toh rah-thyOH-foh-noh stoh ahf-toh-KEE-nee-toh KAH-theh proh-EE",
        "english": "I listen to the radio in the car every morning.",
        "notes": "Klik A1 p. 93, 107. Grammar: verb 'ακούω' (1st sg.) + direct object 'το ραδιόφωνο'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Όταν οδηγώ για το γραφείο, ακούω το ραδιόφωνο στο αυτοκίνητο κάθε πρωί.",
        "example_en": "When I drive to the office, I listen to the radio in the car every morning.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing morning commute habits and media consumption"
    },
    {
        "id": "A1-U105B-027",
        "greek": "Ακούς τις ειδήσεις στις οκτώ το βράδυ;",
        "phonetic_hint": "ah-KOOS tees ee-THEE-sees stees ohk-TOH toh VRAH-thee",
        "english": "Do you listen to the news at eight in the evening?",
        "notes": "Klik A1 p. 107. Grammar: verb 'ακούς' (2nd sg.) + feminine accusative plural 'τις ειδήσεις'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ακούς τις ειδήσεις στις οκτώ το βράδυ; — Ναι, πάντα.",
        "example_en": "— Do you listen to the news at eight in the evening? — Yes, always.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about news habits and evening schedule"
    },
    {
        "id": "A1-U105B-028",
        "greek": "Ακούμε ελληνική μουσική όταν μαγειρεύουμε.",
        "phonetic_hint": "ah-KOO-meh eh-lee-nee-KEE moo-see-KEE OH-tahn mah-yee-REHV-oo-meh",
        "english": "We listen to Greek music when we cook.",
        "notes": "Klik A1 p. 107. Grammar: verb 'ακούμε' (1st pl.) + temporal conjunction 'όταν' + verb 'μαγειρεύουμε'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μας αρέσει η παρέα στην κουζίνα και ακούμε ελληνική μουσική όταν μαγειρεύουμε.",
        "example_en": "We like company in the kitchen and listen to Greek music when we cook.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Relating concurrent leisure activities in the home"
    },
    {
        "id": "A1-U105B-029",
        "greek": "Τι λες; — Λέω ότι έχεις απόλυτο δίκιο.",
        "phonetic_hint": "tee LEHS? — LEH-oh OH-tee EH-khees ah-POH-lee-toh THEE-kyoh",
        "english": "What do you say? / What do you mean? — I say that you are totally right.",
        "notes": "Klik A1 p. 93, 107. Grammar: verb 'λέω' (λες 2nd sg. / λέω 1st sg.) + subordinate conjunction 'ότι'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι λες για το σχέδιο; — Λέω ότι έχεις απόλυτο δίκιο.",
        "example_en": "— What do you think about the plan? — I say you are completely right.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing opinions, agreement, and verbal interaction"
    },
    {
        "id": "A1-U105B-030",
        "greek": "Πώς το λένε αυτό στα ελληνικά;",
        "phonetic_hint": "pohs toh LEH-neh ahf-TOH stah eh-lee-nee-KAH",
        "english": "How do you say this in Greek? / What do they call this in Greek?",
        "notes": "Klik A1 p. 107. Essential communicative phrase with 3rd plural impersonal 'λένε' + object pronoun 'το'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Δεν ξέρω τη λέξη. Πώς το λένε αυτό στα ελληνικά;",
        "example_en": "I don't know the word. How do you say this in Greek?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking for vocabulary clarification and meta-linguistic support"
    },
    {
        "id": "A1-U105B-031",
        "greek": "Τι λέει η μητέρα σου για το ταξίδι;",
        "phonetic_hint": "tee LEH-ee ee mee-TEH-rah soo yah toh tahk-SEE-thee",
        "english": "What is your mother saying about the trip?",
        "notes": "Klik A1 p. 107. Grammar: verb 'λέει' (3rd sg.) + preposition 'για' + neuter noun.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Μίλησες μαζί της; Τι λέει η μητέρα σου για το ταξίδι; — Χάρηκε πάρα πολύ.",
        "example_en": "— Did you speak with her? What does your mother say about the trip? — She was delighted.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Reporting family opinions and reactions"
    },
    {
        "id": "A1-U105B-032",
        "greek": "Τι τρως για πρωινό; — Τρώω ψωμί με μέλι.",
        "phonetic_hint": "tee TROHS yah proh-ee-NOH? — TROH-oh psoh-MEE meh MEH-lee",
        "english": "What do you eat for breakfast? — I eat bread with honey.",
        "notes": "Klik A1 p. 93, 107. Grammar: irregular verb 'τρώω' (τρως 2nd sg. / τρώω 1st sg.).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι τρως για πρωινό; — Τρώω ψωμί με μέλι και πίνω ένα ποτήρι γάλα.",
        "example_en": "— What do you eat for breakfast? — I eat bread with honey and drink a glass of milk.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Discussing breakfast foods and morning eating habits"
    },
    {
        "id": "A1-U105B-033",
        "greek": "Το μεσημέρι τρώμε όλοι μαζί στο σπίτι.",
        "phonetic_hint": "toh meh-see-MEH-ree TROH-meh OH-lee mah-ZEE stoh SPEE-tee",
        "english": "At noon we all eat together at home.",
        "notes": "Klik A1 p. 98, 107. Grammar: verb 'τρώμε' (1st person plural) + adverb of manner 'μαζί'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τις Κυριακές το μεσημέρι τρώμε όλοι μαζί στο σπίτι της γιαγιάς.",
        "example_en": "On Sunday afternoons we all eat together at grandmother's house.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing family mealtime traditions"
    },
    {
        "id": "A1-U105B-034",
        "greek": "Τα παιδιά τρώνε φρούτα μετά το σχολείο.",
        "phonetic_hint": "tah peh-THYAH TROH-neh FROO-tah meh-TAH toh skhoh-LEE-oh",
        "english": "The children eat fruit after school.",
        "notes": "Klik A1 p. 107. Grammar: verb 'τρώνε' (3rd person plural) + neuter plural 'φρούτα'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Για κολατσιό τα παιδιά τρώνε φρούτα μετά το σχολείο.",
        "example_en": "For a snack, the children eat fruit after school.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing children's dietary and snacking routines"
    },
    {
        "id": "A1-U105B-035",
        "greek": "Τι ώρα κοιμάσαι συνήθως το βράδυ;",
        "phonetic_hint": "tee OH-rah kee-MAH-seh see-NEE-thos toh VRAH-thee",
        "english": "What time do you usually sleep at night?",
        "notes": "Klik A1 p. 93, 107. Grammar: mediopassive verb 'κοιμάμαι' (κοιμάσαι 2nd person singular).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι ώρα κοιμάσαι συνήθως το βράδυ; — Συνήθως κοιμάμαι στις έντεκα.",
        "example_en": "— What time do you usually go to bed at night? — I usually sleep at eleven.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about bedtime routines and sleep habits"
    },
    {
        "id": "A1-U105B-036",
        "greek": "Ο πατέρας κοιμάται νωρίς επειδή ξυπνάει στις πέντε.",
        "phonetic_hint": "oh pah-TEH-rahs kee-MAH-teh noh-REES eh-pee-THEE ksee-PNAH-ee stees PEN-deh",
        "english": "Father goes to sleep early because he wakes up at five.",
        "notes": "Klik A1 p. 98, 107. Grammar: mediopassive 3rd sg. 'κοιμάται' + causal conjunction 'επειδή'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Λόγω της δουλειάς του, ο πατέρας κοιμάται νωρίς επειδή ξυπνάει στις πέντε.",
        "example_en": "Due to his job, father sleeps early because he wakes up at five.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Explaining the cause behind daily schedules"
    },
    {
        "id": "A1-U105B-037",
        "greek": "Τις Κυριακές κοιμόμαστε μέχρι αργά το πρωί.",
        "phonetic_hint": "tees kee-ryah-KEHS kee-MOH-mah-steh MEHKH-ree ahr-GHAH toh proh-EE",
        "english": "On Sundays we sleep until late in the morning.",
        "notes": "Klik A1 p. 107. Grammar: mediopassive 1st pl. 'κοιμόμαστε' + preposition 'μέχρι' + adverb 'αργά'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Δεν έχουμε δουλειά, γι' αυτό τις Κυριακές κοιμόμαστε μέχρι αργά το πρωί.",
        "example_en": "We don't have work, so on Sundays we sleep until late in the morning.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing weekend rest habits and late rising"
    },
    {
        "id": "A1-U105B-038",
        "greek": "Έρχεσαι μαζί μας στην ταβέρνα το βράδυ;",
        "phonetic_hint": "EHR-kheh-seh mah-ZEE mahs steen tah-VEHR-nah toh VRAH-thee",
        "english": "Are you coming with us to the tavern tonight?",
        "notes": "Klik A1 p. 107. Grammar: mediopassive verb 'έρχομαι' (έρχεσαι 2nd person singular invitation).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Θα πάμε για φαγητό. Έρχεσαι μαζί μας στην ταβέρνα το βράδυ;",
        "example_en": "We are going for food. Are you coming with us to the tavern tonight?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inviting someone out for dinner using 'έρχομαι'"
    },
    {
        "id": "A1-U105B-039",
        "greek": "Ο Νίκος έρχεται στη δουλειά με το μετρό.",
        "phonetic_hint": "oh NEE-kohs EHR-kheh-teh stee thoo-LYAH meh toh meh-TROH",
        "english": "Nikos comes to work by metro.",
        "notes": "Klik A1 p. 107. Grammar: mediopassive 3rd sg. 'έρχεται' + prepositional phrase of transport.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Δεν οδηγεί αυτοκίνητο. Ο Νίκος έρχεται στη δουλειά με το μετρό.",
        "example_en": "He does not drive a car. Nikos comes to work by metro.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing daily commute methods using 'έρχομαι'"
    },
    {
        "id": "A1-U105B-040",
        "greek": "Οι φίλοι μας έρχονται για φαγητό απόψε.",
        "phonetic_hint": "ee FEE-lee mahs EHR-khon-deh yah fah-yee-TOH ah-POH-pseh",
        "english": "Our friends are coming over for food tonight.",
        "notes": "Klik A1 p. 107. Grammar: mediopassive 3rd pl. 'έρχονται' + temporal adverb 'απόψε'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πρέπει να καθαρίσω το σπίτι γιατί οι φίλοι μας έρχονται για φαγητό απόψε.",
        "example_en": "I must clean the house because our friends are coming for food tonight.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Announcing evening social gatherings and visits"
    },

    # =========================================================================
    # 4. Telling Time & Schedule Collocations (pp. 100-103)
    # =========================================================================
    {
        "id": "A1-U105B-041",
        "greek": "Τι ώρα είναι; — Είναι οκτώ και τέταρτο.",
        "phonetic_hint": "tee OH-rah EE-neh? — EE-neh ohk-TOH keh TEH-tahr-toh",
        "english": "What time is it? — It is a quarter past eight.",
        "notes": "Klik A1 p. 100-101. Standard time expression with 'και τέταρτο' (:15).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Συγγνώμη, τι ώρα είναι; — Είναι οκτώ και τέταρτο.",
        "example_en": "— Excuse me, what time is it? — It is a quarter past eight.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about and stating the exact hour and quarter past"
    },
    {
        "id": "A1-U105B-042",
        "greek": "Είναι εννέα και μισή το βράδυ.",
        "phonetic_hint": "EE-neh eh-NEH-ah keh mee-SEE toh VRAH-thee",
        "english": "It is nine thirty in the evening.",
        "notes": "Klik A1 p. 100-101. Standard time expression with 'και μισή' (:30) and time-of-day clarification.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Είναι εννέα και μισή το βράδυ και η πόλη είναι ακόμα γεμάτη κόσμο.",
        "example_en": "It is half past nine in the evening and the city is still full of people.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Stating half-past hours in context"
    },
    {
        "id": "A1-U105B-043",
        "greek": "Είναι δέκα παρά είκοσι.",
        "phonetic_hint": "EE-neh THEH-kah pah-RAH EE-koh-see",
        "english": "It is twenty to ten.",
        "notes": "Klik A1 p. 100-101. Prepositional time subtraction with 'παρά' (:40 = 'δέκα παρά είκοσι').",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βιάσου, είναι δέκα παρά είκοσι και το λεωφορείο περνάει στις δέκα.",
        "example_en": "Hurry up, it is twenty to ten and the bus passes at ten.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Stating time before the hour using 'παρά'"
    },
    {
        "id": "A1-U105B-044",
        "greek": "Είναι τρεις ακριβώς το μεσημέρι.",
        "phonetic_hint": "EE-neh trees ah-kree-VOHS toh meh-see-MEH-ree",
        "english": "It is exactly three in the afternoon.",
        "notes": "Klik A1 p. 100-101. Precision time indicator 'ακριβώς' (on the dot / sharp).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Το ρολόι χτυπάει, είναι τρεις ακριβώς το μεσημέρι.",
        "example_en": "The clock is chiming, it is exactly three in the afternoon.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing precise on-the-hour time"
    },
    {
        "id": "A1-U105B-045",
        "greek": "Τι ώρα αρχίζει η ταινία; — Αρχίζει στις εννέα.",
        "phonetic_hint": "tee OH-rah ahr-KHEE-zee ee teh-NEE-ah? — ahr-KHEE-zee stees eh-NEH-ah",
        "english": "What time does the movie start? — It starts at nine.",
        "notes": "Klik A1 p. 100, 102. Grammar: verb 'αρχίζει' (it starts) + prepositional time 'στις εννέα'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι ώρα αρχίζει η ταινία; — Αρχίζει στις εννέα, ας πάρουμε εισιτήρια.",
        "example_en": "— What time does the film start? — It starts at nine, let's buy tickets.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about cinema and event start times"
    },
    {
        "id": "A1-U105B-046",
        "greek": "Το μάθημα τελειώνει στις δύο και τέταρτο.",
        "phonetic_hint": "toh MAH-thee-mah teh-lyOH-nee stees THEE-oh keh TEH-tahr-toh",
        "english": "The lesson finishes at a quarter past two.",
        "notes": "Klik A1 p. 102. Grammar: verb 'τελειώνει' (it ends / finishes) + time structure.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μην ανησυχείς, το μάθημα τελειώνει στις δύο και τέταρτο και μετά είμαι ελεύθερος.",
        "example_en": "Don't worry, the lesson finishes at a quarter past two and then I am free.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Communicating end times and academic schedules"
    },
    {
        "id": "A1-U105B-047",
        "greek": "Η τράπεζα ανοίγει στις οκτώ και κλείνει στις δύο.",
        "phonetic_hint": "ee TRAH-peh-zah ah-NEE-yee stees ohk-TOH keh KLEE-nee stees THEE-oh",
        "english": "The bank opens at eight and closes at two.",
        "notes": "Klik A1 p. 102. Grammar: contrast verbs 'ανοίγει' (opens) and 'κλείνει' (closes) with opening hours.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πρέπει να πας νωρίς, επειδή η τράπεζα ανοίγει στις οκτώ και κλείνει στις δύο.",
        "example_en": "You must go early, because the bank opens at eight and closes at two.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing business hours and administrative operational schedules"
    },

    # =========================================================================
    # 5. Daily Routine & Frequency Expressions (pp. 98-99, 109-110)
    # =========================================================================
    {
        "id": "A1-U105B-048",
        "greek": "Ξυπνάω νωρίς, πλένομαι και πίνω έναν ζεστό καφέ.",
        "phonetic_hint": "ksee-PNAH-oh noh-REES, PLEH-noh-meh keh PEE-noh EH-nahn zehs-TOH kah-FEH",
        "english": "I wake up early, wash myself, and drink a hot coffee.",
        "notes": "Klik A1 p. 98-99. Sequence of morning routine actions with mediopassive reflexive 'πλένομαι'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κάθε εργάσιμη μέρα ξυπνάω νωρίς, πλένομαι και πίνω έναν ζεστό καφέ.",
        "example_en": "Every working day I wake up early, wash, and drink a hot coffee.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Narrating chronological morning routines"
    },
    {
        "id": "A1-U105B-049",
        "greek": "Φεύγω από το σπίτι στις οκτώ και μισή και γυρίζω στις έξι.",
        "phonetic_hint": "FEHV-ghoh ah-POH toh SPEE-tee stees ohk-TOH keh mee-SEE keh yee-REE-zoh stees EHK-see",
        "english": "I leave the house at eight-thirty and return at six.",
        "notes": "Klik A1 p. 98-99. Pair verbs 'φεύγω από' (leave from) and 'γυρίζω' (return).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Έχω πολλή δουλειά σήμερα: φεύγω από το σπίτι στις οκτώ και μισή και γυρίζω στις έξι.",
        "example_en": "I have lots of work today: I leave home at eight-thirty and return at six.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing departure and return times for work"
    },
    {
        "id": "A1-U105B-050",
        "greek": "Πάντα πίνω καφέ το πρωί, αλλά ποτέ δεν πίνω καφέ το βράδυ.",
        "phonetic_hint": "PAHN-dah PEE-noh kah-FEH toh proh-EE, ah-LAH poh-TEH then PEE-noh kah-FEH toh VRAH-thee",
        "english": "I always drink coffee in the morning, but I never drink coffee at night.",
        "notes": "Klik A1 p. 98, 109-110. Frequency contrast: 'πάντα' (always) versus 'ποτέ δεν' (never).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Για να κοιμάμαι εύκολα, πάντα πίνω καφέ το πρωί, αλλά ποτέ δεν πίνω καφέ το βράδυ.",
        "example_en": "In order to sleep easily, I always drink coffee in the morning, but never drink coffee at night.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing frequency contrasts with 'πάντα' and 'ποτέ'"
    },
    {
        "id": "A1-U105B-051",
        "greek": "Πηγαίνω στο γυμναστήριο τρεις φορές την εβδομάδα.",
        "phonetic_hint": "pee-YEH-noh stoh yeem-nahs-TEE-ree-oh trees foh-REHS teen ehv-thoh-MAH-thah",
        "english": "I go to the gym three times a week.",
        "notes": "Klik A1 p. 98, 109. Frequency expression: 'τρεις φορές την εβδομάδα' (three times a week).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Για να διατηρούμαι σε φόρμα, πηγαίνω στο γυμναστήριο τρεις φορές την εβδομάδα.",
        "example_en": "To stay in shape, I go to the gym three times a week.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Stating regular frequency of exercise and sporting habits"
    },
    {
        "id": "A1-U105B-052",
        "greek": "Συνήθως τρώμε βραδινό στις εννέα, αλλά σπάνια βλέπουμε τηλεόραση.",
        "phonetic_hint": "see-NEE-thos TROH-meh vrah-thee-NOH stees eh-NEH-ah, ah-LAH SPAH-nyah VLEH-poo-meh tee-leh-OH-rah-see",
        "english": "We usually eat dinner at nine, but we rarely watch television.",
        "notes": "Klik A1 p. 109-110. Frequency contrast: 'συνήθως' (usually) versus 'σπάνια' (rarely).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Στην οικογένειά μας συνήθως τρώμε βραδινό στις εννέα, αλλά σπάνια βλέπουμε τηλεόραση.",
        "example_en": "In our family we usually have dinner at nine, but we rarely watch television.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing recurring lifestyle habits with 'συνήθως' and 'σπάνια'"
    }
]

lesson_u105b = {
    "unit_id": "unit-105b",
    "lesson_id": "lesson-01",
    "title": "Ενότητα 4: Προτάσεις & Γραμματική — Καθημερινότητα, Αιτιατική, Ώρα & Συζυγίες (Pages 87-110)",
    "entries": cards_u105b
}

def main():
    print(f"Writing {len(cards_u105b)} cards to {YAML_PATH}...")
    with open(YAML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(lesson_u105b, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("YAML successfully written.")

    # Update manifest.yaml
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    units = manifest.get("units", [])
    existing = next((u for u in units if u.get("id") == "unit-105b"), None)
    unit_105b_entry = {
        "id": "unit-105b",
        "title": "Κλικ στα Ελληνικά Α1: Σελίδες 87-110 (Ενότητα 4: Από το πρωί μέχρι το βράδυ - Γραμματική & Προτάσεις)",
        "order": "105B",
        "is_expansion": True,
        "expansion_of": "105",
        "lessons": [
            {
                "id": "lesson-01",
                "file": "unit-105b/lesson-01.yaml",
                "title": "Ενότητα 4: Προτάσεις & Γραμματική — Καθημερινότητα, Αιτιατική, Ώρα & Συζυγίες (Pages 87-110)",
                "description": "Expansion & Complementary to Lesson 105: Sentence structures, syntax patterns, accusative direct objects, irregular verbs, and time-telling."
            }
        ]
    }

    if existing:
        print("Updating existing unit-105b in manifest.yaml...")
        idx = units.index(existing)
        units[idx] = unit_105b_entry
    else:
        print("Appending unit-105b to manifest.yaml...")
        units.append(unit_105b_entry)

    manifest["units"] = units

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("Manifest successfully updated with unit-105b!")

if __name__ == "__main__":
    main()

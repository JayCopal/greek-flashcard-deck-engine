# -*- coding: utf-8 -*-
"""
Script to create Unit 108 B from Klik A1 (Pages 151-174):
Ενότητα 7: Γιορτές! Ώρα για ψώνια - Γραμματική & Προτάσεις
Focuses on:
1. Simple Future Tense (θα + στιγμιαίος κορμός / αόριστος υποτακτικής: θα πάω, θα αγοράσω, θα φάμε, θα μείνουμε).
2. Weak Direct Object Pronouns in Accusative (με, σε, τον, την, το, μας, σας, τους, τις, τα) and their word order.
3. Demonstrative Pronouns & Contrast (αυτός/αυτή/αυτό vs εκείνος/εκείνη/εκείνο).
4. Shopping, sizing, trying on clothes, discounts, payment and cashier interactions.
5. Holiday traditions, invitations, accepting/declining, and cultural celebration wishes (Χριστούγεννα, Πρωτοχρονιά, Πάσχα, ονομαστική γιορτή).
"""
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
UNIT_DIR = CONTENT_DIR / "unit-108b"
UNIT_DIR.mkdir(parents=True, exist_ok=True)
YAML_PATH = UNIT_DIR / "lesson-01.yaml"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

cards_u108b = [
    # =========================================================================
    # 1. Simple Future Tense — Regular & Irregular Stems (pp. 158-161, 168-171)
    # =========================================================================
    {
        "id": "A1-U108B-001",
        "greek": "Αύριο θα πάω στην αγορά για ψώνια.",
        "phonetic_hint": "AV-ree-o thah PAH-o steen ah-go-RAH yah PSON-yah",
        "english": "Tomorrow I will go to the market for shopping.",
        "notes": "Klik A1 p. 158, 160. Grammar: Simple Future (θα πάω) formed with future particle θα + dependent stem of verb πηγαίνω / πάω.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι θα κάνεις αύριο το πρωί; — Αύριο θα πάω στην αγορά για ψώνια.",
        "example_en": "— What will you do tomorrow morning? — Tomorrow I will go to the market for shopping.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Stating future shopping plans using the simple future"
    },
    {
        "id": "A1-U108B-002",
        "greek": "Τι θα κάνεις το Σαββατοκύριακο;",
        "phonetic_hint": "tee thah KAH-nees to sah-vah-to-KEE-ree-ah-ko",
        "english": "What will you do over the weekend?",
        "notes": "Klik A1 p. 158, 168. Grammar: Simple Future 2nd person singular (θα κάνεις) of verb κάνω.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι θα κάνεις το Σαββατοκύριακο; — Θα πάω μια εκδρομή στο βουνό.",
        "example_en": "— What will you do over the weekend? — I will go on an excursion to the mountain.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about weekend plans using the future tense"
    },
    {
        "id": "A1-U108B-003",
        "greek": "Το βράδυ θα φάμε σε μια παραδοσιακή ταβέρνα.",
        "phonetic_hint": "to VRAH-thee thah FAH-meh seh mee-ah pah-rah-tho-see-ah-KEE tah-VER-nah",
        "english": "In the evening we will eat at a traditional tavern.",
        "notes": "Klik A1 p. 158, 160. Grammar: Simple Future 1st person plural (θα φάμε) of irregular verb τρώω (dependent stem φα-).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πού θα πάτε για δείπνο; — Το βράδυ θα φάμε σε μια παραδοσιακή ταβέρνα.",
        "example_en": "— Where will you go for dinner? — In the evening we will eat at a traditional tavern.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing shared evening dining intentions in the future"
    },
    {
        "id": "A1-U108B-004",
        "greek": "Την επόμενη εβδομάδα θα αγοράσω καινούρια παπούτσια.",
        "phonetic_hint": "teen eh-PO-meh-nee ev-tho-MAH-thah thah ah-go-RAH-so keh-NOO-ryah pah-POO-tsyah",
        "english": "Next week I will buy new shoes.",
        "notes": "Klik A1 p. 158, 162. Grammar: Simple Future 1st person singular (θα αγοράσω) of Type A verb αγοράζω (stem in -ασ-).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Χρειάζεσαι μπότες για τον χειμώνα; — Ναι, την επόμενη εβδομάδα θα αγοράσω καινούρια παπούτσια.",
        "example_en": "— Do you need boots for winter? — Yes, next week I will buy new shoes.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Planning future retail purchases with temporal markers"
    },
    {
        "id": "A1-U108B-005",
        "greek": "Θα μείνουμε στο σπίτι γιατί κάνει πολύ κρύο.",
        "phonetic_hint": "thah MEE-noo-meh sto SPEE-tee yah-TEE KAH-nee po-LEE KREE-o",
        "english": "We will stay home because it is very cold.",
        "notes": "Klik A1 p. 158, 160. Grammar: Simple Future 1st person plural (θα μείνουμε) of verb μένω (dependent stem μειν-).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Θα βγείτε μια βόλτα έξω; — Όχι, θα μείνουμε στο σπίτι γιατί κάνει πολύ κρύο.",
        "example_en": "— Will you go for a walk outside? — No, we will stay home because it is very cold.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Explaining homebound plans due to winter weather conditions"
    },
    {
        "id": "A1-U108B-006",
        "greek": "Σε λίγο θα πιούμε έναν ζεστό καφέ.",
        "phonetic_hint": "seh LEE-go thah PYOO-meh EH-nahn zeh-STO kah-FEH",
        "english": "Shortly we will drink a hot coffee.",
        "notes": "Klik A1 p. 158, 160. Grammar: Simple Future 1st person plural (θα πιούμε) of irregular verb πίνω (stem πι-).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Κρυώνεις; — Ναι, σε λίγο θα πιούμε έναν ζεστό καφέ για να ζεσταθούμε.",
        "example_en": "— Are you cold? — Yes, shortly we will drink a hot coffee to warm up.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Suggesting imminent warm beverage consumption"
    },
    {
        "id": "A1-U108B-007",
        "greek": "Αύριο το πρωί θα δω τη φίλη μου στο κέντρο.",
        "phonetic_hint": "AV-ree-o to pro-EE thah THO tee FEE-lee moo sto KEN-tro",
        "english": "Tomorrow morning I will see my friend downtown.",
        "notes": "Klik A1 p. 158, 160. Grammar: Simple Future 1st person singular (θα δω) of irregular verb βλέπω (stem δ-).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Έχεις κάποιο ραντεβού; — Ναι, αύριο το πρωί θα δω τη φίλη μου στο κέντρο.",
        "example_en": "— Do you have an appointment? — Yes, tomorrow morning I will see my friend downtown.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Scheduling a future meeting with a friend"
    },
    {
        "id": "A1-U108B-008",
        "greek": "Θα έρθεις μαζί μας στο πάρτι των γενεθλίων;",
        "phonetic_hint": "thah ER-thees mah-ZEE mahs sto PAR-tee ton yeh-neh-THLEE-on",
        "english": "Will you come with us to the birthday party?",
        "notes": "Klik A1 p. 158, 168. Grammar: Simple Future 2nd person singular (θα έρθεις) of irregular verb έρχομαι (stem ερθ-).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Θα έρθεις μαζί μας στο πάρτι των γενεθλίων; — Ναι, ευχαρίστως!",
        "example_en": "— Will you come with us to the birthday party? — Yes, gladly!",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Extending an invitation to a birthday party"
    },
    {
        "id": "A1-U108B-009",
        "greek": "Του χρόνου θα ταξιδέψουμε στην Ελλάδα για διακοπές.",
        "phonetic_hint": "too KHRO-noo thah tah-ksee-THEH-psoo-meh steen eh-LAH-thah yah thee-ah-ko-PES",
        "english": "Next year we will travel to Greece for holidays.",
        "notes": "Klik A1 p. 158, 160. Grammar: Simple Future 1st person plural (θα ταξιδέψουμε) of verb ταξιδεύω (stem in -εψ-).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ποια είναι τα σχέδιά σας; — Του χρόνου θα ταξιδέψουμε στην Ελλάδα για διακοπές.",
        "example_en": "— What are your plans? — Next year we will travel to Greece for holidays.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing long-term holiday travel intentions"
    },
    {
        "id": "A1-U108B-010",
        "greek": "Δεν θα βγω απόψε γιατί είμαι πολύ κουρασμένος.",
        "phonetic_hint": "then thah VGO ah-PO-pseh yah-TEE EE-meh po-LEE koo-rah-ZMEH-nos",
        "english": "I will not go out tonight because I am very tired.",
        "notes": "Klik A1 p. 158, 160. Grammar: Negation of Simple Future with δεν (δεν θα βγω) of irregular verb βγαίνω (stem βγ-).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Θα πάμε σε ένα μπαρ; — Όχι, δεν θα βγω απόψε γιατί είμαι πολύ κουρασμένος.",
        "example_en": "— Shall we go to a bar? — No, I will not go out tonight because I am very tired.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Declining an outing using negative future tense"
    },

    # =========================================================================
    # 2. Weak Accusative Pronouns & Word Order (pp. 162-167)
    # =========================================================================
    {
        "id": "A1-U108B-011",
        "greek": "Αυτό το φόρεμα είναι πολύ όμορφο, θα το αγοράσω.",
        "phonetic_hint": "af-TO to FO-reh-mah EE-neh po-LEE O-mor-fo, thah to ah-go-RAH-so",
        "english": "This dress is very beautiful, I will buy it.",
        "notes": "Klik A1 p. 162, 164. Grammar: Weak direct object pronoun neuter singular (το) placed between θα and the verb (θα το αγοράσω).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πώς σου φαίνεται; — Αυτό το φόρεμα είναι πολύ όμορφο, θα το αγοράσω.",
        "example_en": "— How does it look to you? — This dress is very beautiful, I will buy it.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Deciding on a clothing purchase using an object pronoun"
    },
    {
        "id": "A1-U108B-012",
        "greek": "Βλέπεις εκείνον τον άντρα; Τον ξέρεις;",
        "phonetic_hint": "VLEH-pees eh-KEE-non ton AHN-drah? ton KSEH-rees?",
        "english": "Do you see that man? Do you know him?",
        "notes": "Klik A1 p. 164. Grammar: Weak direct object pronoun masculine singular accusative (τον) placed directly before verb (τον ξέρεις).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Βλέπεις εκείνον τον άντρα; Τον ξέρεις; — Ναι, είναι ο καθηγητής μας.",
        "example_en": "— Do you see that man? Do you know him? — Yes, he is our teacher.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking about acquaintance recognition using masculine accusative pronoun"
    },
    {
        "id": "A1-U108B-013",
        "greek": "Ψάχνω την τσάντα μου αλλά δεν την βρίσκω πουθενά.",
        "phonetic_hint": "PSAH-khno teen TSAHN-dah moo ah-LAH then teen VREE-sko poo-theh-NAH",
        "english": "I am looking for my bag but I cannot find it anywhere.",
        "notes": "Klik A1 p. 164. Grammar: Weak direct object pronoun feminine singular accusative (την) placed between negation and verb (δεν την βρίσκω).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι έχασες; — Ψάχνω την τσάντα μου αλλά δεν την βρίσκω πουθενά.",
        "example_en": "— What did you lose? — I am looking for my bag but I cannot find it anywhere.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Reporting a misplaced accessory with feminine object pronoun"
    },
    {
        "id": "A1-U108B-014",
        "greek": "Με ακούς καλά ή να μιλήσω πιο δυνατά;",
        "phonetic_hint": "meh ah-KOOS kah-LAH ee nah mee-LEE-so pyo thee-nah-TAH",
        "english": "Do you hear me well or should I speak louder?",
        "notes": "Klik A1 p. 164. Grammar: Weak direct object pronoun 1st person singular (με) placed before verb.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Με ακούς καλά ή να μιλήσω πιο δυνατά; — Σε ακούω μια χαρά, μην ανησυχείς.",
        "example_en": "— Do you hear me well or should I speak louder? — I hear you just fine, do not worry.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Verifying audio clarity using first-person object pronoun"
    },
    {
        "id": "A1-U108B-015",
        "greek": "Σε περιμένω έξω από τον σταθμό του μετρό.",
        "phonetic_hint": "seh peh-ree-MEH-no EH-kso ah-PO ton stahth-MO too meh-TRO",
        "english": "I am waiting for you outside the metro station.",
        "notes": "Klik A1 p. 164. Grammar: Weak direct object pronoun 2nd person singular (σε) preceding verb περιμένω.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πού είσαι τώρα; — Σε περιμένω έξω από τον σταθμό του μετρό.",
        "example_en": "— Where are you now? — I am waiting for you outside the metro station.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Specifying a meeting location using second-person object pronoun"
    },
    {
        "id": "A1-U108B-016",
        "greek": "Μας βλέπετε από εκεί που κάθεστε;",
        "phonetic_hint": "mahs VLEH-peh-teh ah-PO eh-KEE poo KAH-theh-steh",
        "english": "Can you see us from where you are sitting?",
        "notes": "Klik A1 p. 164. Grammar: Weak direct object pronoun 1st person plural (μας) before verb.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Μας βλέπετε από εκεί που κάθεστε; — Ναι, σας βλέπουμε πολύ καθαρά.",
        "example_en": "— Can you see us from where you are sitting? — Yes, we see you very clearly.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Confirming visual visibility using plural object pronouns"
    },
    {
        "id": "A1-U108B-017",
        "greek": "Σας ευχαριστούμε πολύ για την ευγενική πρόσκληση.",
        "phonetic_hint": "sahs ef-khah-ree-STOO-meh po-LEE yah teen ef-yeh-nee-KEE PRO-sklee-see",
        "english": "We thank you very much for the kind invitation.",
        "notes": "Klik A1 p. 164, 168. Grammar: Weak direct object pronoun 2nd person plural / formal (σας).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Χαρήκαμε που ήρθατε στο πάρτι μας! — Εμείς σας ευχαριστούμε πολύ για την ευγενική πρόσκληση.",
        "example_en": "— We were glad you came to our party! — We thank you very much for the kind invitation.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing formal gratitude for a social invitation"
    },
    {
        "id": "A1-U108B-018",
        "greek": "Έχουμε πολλούς φίλους και θα τους καλέσουμε όλους.",
        "phonetic_hint": "EH-khoo-meh po-LEES FEE-loos keh thah toos kah-LEH-soo-meh O-loos",
        "english": "We have many friends and we will invite them all.",
        "notes": "Klik A1 p. 164, 168. Grammar: Weak direct object pronoun masculine plural accusative (τους) between θα and verb (θα τους καλέσουμε).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πόσους καλεσμένους θα έχετε; — Έχουμε πολλούς φίλους και θα τους καλέσουμε όλους.",
        "example_en": "— How many guests will you have? — We have many friends and we will invite them all.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing party guest invitations using masculine plural object pronoun"
    },
    {
        "id": "A1-U108B-019",
        "greek": "Σου αρέσουν αυτές οι μπότες; Θα τις δοκιμάσω αμέσως.",
        "phonetic_hint": "soo ah-REH-soon af-TES ee BO-tes? thah tees tho-kee-MAH-so ah-MEH-sos",
        "english": "Do you like these boots? I will try them on immediately.",
        "notes": "Klik A1 p. 162, 164. Grammar: Weak direct object pronoun feminine plural accusative (τις) in future construction (θα τις δοκιμάσω).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Σου αρέσουν αυτές οι μπότες; Θα τις δοκιμάσω αμέσως. — Είναι υπέροχες, ζήτα το νούμερό σου.",
        "example_en": "— Do you like these boots? I will try them on immediately. — They are wonderful, ask for your size.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Announcing intention to try footwear using feminine plural object pronoun"
    },
    {
        "id": "A1-U108B-020",
        "greek": "Αγόρασα πολλά δώρα και θα τα τυλίξω το βράδυ.",
        "phonetic_hint": "ah-GO-rah-sah po-LAH THO-rah keh thah tah tee-LEE-kso to VRAH-thee",
        "english": "I bought many gifts and I will wrap them in the evening.",
        "notes": "Klik A1 p. 156, 164. Grammar: Weak direct object pronoun neuter plural accusative (τα) positioned between θα and verb (θα τα τυλίξω).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι έχεις μέσα στις σακούλες; — Αγόρασα πολλά δώρα και θα τα τυλίξω το βράδυ.",
        "example_en": "— What do you have inside the bags? — I bought many gifts and I will wrap them in the evening.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Discussing gift preparation using neuter plural object pronoun"
    },

    # =========================================================================
    # 3. Demonstratives & Contrast: αυτός vs εκείνος (pp. 162-167)
    # =========================================================================
    {
        "id": "A1-U108B-021",
        "greek": "Αυτό το παλτό είναι καλό, αλλά εκείνο είναι πιο ζεστό.",
        "phonetic_hint": "af-TO to pahl-TO EE-neh kah-LO, ah-LAH eh-KEE-no EE-neh pyo zeh-STO",
        "english": "This coat is good, but that one over there is warmer.",
        "notes": "Klik A1 p. 162, 166. Grammar: Contrast between proximate demonstrative αυτό and distant demonstrative εκείνο.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ποιο πανωφόρι προτιμάς; — Αυτό το παλτό είναι καλό, αλλά εκείνο είναι πιο ζεστό.",
        "example_en": "— Which outerwear do you prefer? — This coat is good, but that one over there is warmer.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Comparing clothing qualities using demonstrative contrast"
    },
    {
        "id": "A1-U108B-022",
        "greek": "Αυτή η φούστα μου αρέσει, αλλά εκείνη έχει καλύτερο χρώμα.",
        "phonetic_hint": "af-TEE ee FOO-stah moo ah-REH-see, ah-LAH eh-KEE-nee EH-khee kah-LEE-teh-ro KHRO-mah",
        "english": "I like this skirt, but that one has a better color.",
        "notes": "Klik A1 p. 162, 166. Grammar: Feminine demonstrative contrast (αυτή vs εκείνη).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ποια φούστα θα δοκιμάσεις; — Αυτή η φούστα μου αρέσει, αλλά εκείνη έχει καλύτερο χρώμα.",
        "example_en": "— Which skirt will you try? — I like this skirt, but that one has a better color.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Evaluating skirt choices based on color and style"
    },
    {
        "id": "A1-U108B-023",
        "greek": "Ποιο πουκάμισο προτιμάς, αυτό εδώ ή εκείνο στη βιτρίνα;",
        "phonetic_hint": "PYO poo-KAH-mee-so pro-tee-MAHS, af-TO eh-THO ee eh-KEE-no stee vee-TREE-nah",
        "english": "Which shirt do you prefer, this one here or that one in the display window?",
        "notes": "Klik A1 p. 162, 166. Grammar: Demonstrative contrast (αυτό εδώ vs εκείνο στη βιτρίνα).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ποιο πουκάμισο προτιμάς, αυτό εδώ ή εκείνο στη βιτρίνα; — Προτιμώ εκείνο στη βιτρίνα, είναι πιο κομψό.",
        "example_en": "— Which shirt do you prefer, this one here or that one in the shop window? — I prefer that one in the window, it is more elegant.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking for preferences between proximal and distal items"
    },
    {
        "id": "A1-U108B-024",
        "greek": "Αυτά τα γάντια είναι από δέρμα, ενώ εκείνα είναι μάλλινα.",
        "phonetic_hint": "af-TAH tah GHAHN-dyah EE-neh ah-PO THAYR-mah, eh-NO eh-KEE-nah EE-neh MAH-lee-nah",
        "english": "These gloves are made of leather, whereas those are woolen.",
        "notes": "Klik A1 p. 162, 166. Grammar: Neuter plural demonstrative contrast (αυτά vs εκείνα) with materials (δέρμα, μάλλινα).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ποια γάντια κρατάνε περισσότερη ζέστη; — Αυτά τα γάντια είναι από δέρμα, ενώ εκείνα είναι μάλλινα.",
        "example_en": "— Which gloves keep more warmth? — These gloves are made of leather, whereas those are woolen.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Distinguishing materials and garments using plural demonstratives"
    },
    {
        "id": "A1-U108B-025",
        "greek": "Εκείνο το κατάστημα στον πεζόδρομο έχει πολύ καλές τιμές.",
        "phonetic_hint": "eh-KEE-no to kah-TAH-stee-mah ston peh-ZO-thro-mo EH-khee po-LEE kah-LES tee-MES",
        "english": "That shop on the pedestrian street has very good prices.",
        "notes": "Klik A1 p. 162, 166. Grammar: Distant demonstrative (εκείνο) pointing to a physical storefront.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πού να πάμε για ρούχα; — Εκείνο το κατάστημα στον πεζόδρομο έχει πολύ καλές τιμές.",
        "example_en": "— Where should we go for clothes? — That shop on the pedestrian walkway has very good prices.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Recommending an urban retail venue using distant demonstrative"
    },
    {
        "id": "A1-U108B-026",
        "greek": "Εκείνοι οι πελάτες περιμένουν στην ουρά για το ταμείο.",
        "phonetic_hint": "eh-KEE-nee ee peh-LAH-tes peh-ree-MEH-noon steen oo-RAH yah to tah-MEE-o",
        "english": "Those customers are waiting in line for the cash register.",
        "notes": "Klik A1 p. 164, 166. Grammar: Masculine plural distant demonstrative (εκείνοι) modifying noun πελάτες.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πού πληρώνουμε; — Πίσω από εκείνους τους κυρίους, εκείνοι οι πελάτες περιμένουν στην ουρά για το ταμείο.",
        "example_en": "— Where do we pay? — Behind those gentlemen, those customers are waiting in line for the cashier.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Directing customers to queue lines at cashier stations"
    },

    # =========================================================================
    # 4. Retail Sizing, Trying On & Fitting Room Dialogues (pp. 162-165)
    # =========================================================================
    {
        "id": "A1-U108B-027",
        "greek": "Παρακαλώ, μπορώ να δοκιμάσω αυτό το σακάκι;",
        "phonetic_hint": "pah-rah-kah-LO, bo-RO nah tho-kee-MAH-so af-TO to sah-KAH-kee",
        "english": "Please, may I try on this jacket?",
        "notes": "Klik A1 p. 162, 164. Grammar: Modal construction μπορώ να + dependent subjunctive (δοκιμάσω). Standard polite retail question.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Παρακαλώ, μπορώ να δοκιμάσω αυτό το σακάκι; — Φυσικά, περάστε στα δοκιμαστήρια.",
        "example_en": "— Please, may I try on this jacket? — Of course, proceed to the fitting rooms.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Politely requesting to try on apparel in a clothing shop"
    },
    {
        "id": "A1-U108B-028",
        "greek": "Συγγνώμη, πού είναι το δοκιμαστήριο;",
        "phonetic_hint": "seeg-NO-mee, poo EE-neh to tho-kee-mah-STEE-ree-o",
        "english": "Excuse me, where is the fitting room?",
        "notes": "Klik A1 p. 162. Vocabulary & syntax: Inquiring about store amenities with polite opening (συγγνώμη).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Συγγνώμη, πού είναι το δοκιμαστήριο; — Στο βάθος δεξιά, δίπλα στο ταμείο.",
        "example_en": "— Excuse me, where is the fitting room? — Straight at the back on the right, next to the cashier.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Locating customer dressing rooms within a store"
    },
    {
        "id": "A1-U108B-029",
        "greek": "Τι νούμερο φοράτε σε παντελόνι;",
        "phonetic_hint": "tee NOO-meh-ro fo-RAH-teh seh pahn-deh-LO-nee",
        "english": "What size do you wear in trousers?",
        "notes": "Klik A1 p. 162, 163. Grammar: Polite plural (φοράτε) used by sales assistants to ask for garment sizes.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι νούμερο φοράτε σε παντελόνι; — Φοράω συνήθως το τριάντα οκτώ.",
        "example_en": "— What size do you wear in trousers? — I usually wear size thirty-eight.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking customer sizing as a retail salesperson"
    },
    {
        "id": "A1-U108B-030",
        "greek": "Φοράω συνήθως το μεσαίο μέγεθος ή το σαράντα.",
        "phonetic_hint": "fo-RAH-o see-NEE-thos to meh-SEH-o MEH-yeh-thos ee to sah-RAHN-dah",
        "english": "I usually wear medium size or size forty.",
        "notes": "Klik A1 p. 162, 163. Vocabulary: μέγεθος (size descriptor) and numerical clothing size (σαράντα).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Τι νούμερο θέλετε να σας φέρω; — Φοράω συνήθως το μεσαίο μέγεθος ή το σαράντα.",
        "example_en": "— What size do you want me to bring you? — I usually wear medium size or size forty.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Specifying personal clothing size to store staff"
    },
    {
        "id": "A1-U108B-031",
        "greek": "Αυτό το τζιν μου είναι πολύ στενό στη μέση.",
        "phonetic_hint": "af-TO to dzeen moo EE-neh po-LEE steh-NO stee MEH-see",
        "english": "These jeans are too tight on me around the waist.",
        "notes": "Klik A1 p. 162, 163. Grammar: Indirect object / dative relation with weak pronoun (μου είναι) + adjective στενό (tight).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πώς σας φαίνεται το παντελόνι; — Αυτό το τζιν μου είναι πολύ στενό στη μέση, έχετε ένα νούμερο μεγαλύτερο;",
        "example_en": "— How do the pants seem to you? — These jeans are too tight on me around the waist, do you have a size larger?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Explaining garment fit defect (too tight) to a salesperson"
    },
    {
        "id": "A1-U108B-032",
        "greek": "Αυτή η μπλούζα σας είναι πολύ φαρδιά, δοκιμάστε ένα μικρότερο νούμερο.",
        "phonetic_hint": "af-TEE ee BLOO-zah sahs EE-neh po-LEE fahr-THYAH, tho-kee-MAH-steh EH-nah mee-KRO-teh-ro NOO-meh-ro",
        "english": "This blouse is too loose on you, try a smaller size.",
        "notes": "Klik A1 p. 162, 163. Grammar: Polite imperative plural (δοκιμάστε) + comparative adjective (μικρότερο).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Νομίζω ότι μου πέφτει μεγάλη. — Ναι, αυτή η μπλούζα σας είναι πολύ φαρδιά, δοκιμάστε ένα μικρότερο νούμερο.",
        "example_en": "— I think it falls too large on me. — Yes, this blouse is too loose on you, try a smaller size.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Advising a customer to downsize a loose-fitting garment"
    },
    {
        "id": "A1-U108B-033",
        "greek": "Το μήκος είναι καλό, αλλά τα μανίκια είναι πολύ μακριά.",
        "phonetic_hint": "to MEE-kos EE-neh kah-LO, ah-LAH tah mah-NEE-kyah EE-neh po-LEE mah-KRYAH",
        "english": "The length is good, but the sleeves are too long.",
        "notes": "Klik A1 p. 162, 163. Vocabulary & agreement: το μήκος (length), τα μανίκια (sleeves), neuter plural adjective μακριά.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Σου κάνει το πουκάμισο; — Το μήκος είναι καλό, αλλά τα μανίκια είναι πολύ μακριά.",
        "example_en": "— Does the shirt fit you? — The length is good, but the sleeves are too long.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing specific garment dimension mismatches"
    },
    {
        "id": "A1-U108B-034",
        "greek": "Αυτό το χρώμα σάς πηγαίνει πάρα πολύ!",
        "phonetic_hint": "af-TO to KHRO-mah sahs pee-YEH-nee PAH-rah po-LEE",
        "english": "This color suits you very much!",
        "notes": "Klik A1 p. 162, 164. Idiom: πηγαίνει σε κάποιον = suits / flatters someone. Polite pronoun σάς.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Να πάρω το πράσινο ή το μαύρο; — Πάρε το πράσινο! Αυτό το χρώμα σάς πηγαίνει πάρα πολύ!",
        "example_en": "— Should I take the green or the black? — Take the green! This color suits you very much!",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Complimenting someone on flattering clothing color"
    },
    {
        "id": "A1-U108B-035",
        "greek": "Σας κάνει το φόρεμα ή θέλετε να δείτε άλλο σχέδιο;",
        "phonetic_hint": "sahs KAH-nee to FO-reh-mah ee THEH-leh-teh nah THEE-teh AH-lo SKHEH-thee-o",
        "english": "Does the dress fit you or would you like to see another design?",
        "notes": "Klik A1 p. 162, 164. Idiom: μου κάνει = it fits me. Polite plural σας κάνει.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Σας κάνει το φόρεμα ή θέλετε να δείτε άλλο σχέδιο; — Μου κάνει πολύ καλά, ευχαριστώ.",
        "example_en": "— Does the dress fit you or would you like to see another design? — It fits me very well, thank you.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about garment fit and proposing design alternatives"
    },
    {
        "id": "A1-U108B-036",
        "greek": "Μου κάνει τέλεια και είναι πάρα πολύ άνετο.",
        "phonetic_hint": "moo KAH-nee TEH-lyah keh EE-neh PAH-rah po-LEE AH-neh-to",
        "english": "It fits me perfectly and it is extremely comfortable.",
        "notes": "Klik A1 p. 162, 163. Idiom: μου κάνει τέλεια (it fits me perfectly). Adjective άνετος/άνετη/άνετο.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πώς αισθάνεσαι με το κουστούμι; — Μου κάνει τέλεια και είναι πάρα πολύ άνετο.",
        "example_en": "— How do you feel in the suit? — It fits me perfectly and it is extremely comfortable.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing complete satisfaction with clothing fit and comfort"
    },

    # =========================================================================
    # 5. Prices, Discounts, Cashier & Payment Dialogues (pp. 162-167)
    # =========================================================================
    {
        "id": "A1-U108B-037",
        "greek": "Πόσο κοστίζει αυτό το ζευγάρι παπούτσια;",
        "phonetic_hint": "PO-so ko-STEE-zee af-TO to zev-GHAH-ree pah-POO-tsyah",
        "english": "How much does this pair of shoes cost?",
        "notes": "Klik A1 p. 162, 164. Vocabulary: κοστίζω (to cost), το ζευγάρι (pair).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πόσο κοστίζει αυτό το ζευγάρι παπούτσια; — Κοστίζει εβδομήντα πέντε ευρώ.",
        "example_en": "— How much does this pair of shoes cost? — It costs seventy-five euros.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about the retail price of footwear"
    },
    {
        "id": "A1-U108B-038",
        "greek": "Στις εκπτώσεις όλα τα είδη έχουν έκπτωση είκοσι τοις εκατό.",
        "phonetic_hint": "stees ek-PTO-sees O-lah tah EE-thee EH-khoon EK-pto-see EE-ko-see tees eh-kah-TO",
        "english": "During the sales, all items have a twenty percent discount.",
        "notes": "Klik A1 p. 162, 164. Formula: έκπτωση είκοσι τοις εκατό (twenty percent discount).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Έχει κάποια προσφορά σήμερα; — Ναι, στις εκπτώσεις όλα τα είδη έχουν έκπτωση είκοσι τοις εκατό.",
        "example_en": "— Is there any special offer today? — Yes, during sales all items have a twenty percent discount.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Stating percentage discounts during retail sale periods"
    },
    {
        "id": "A1-U108B-039",
        "greek": "Πληρώνετε με μετρητά ή προτιμάτε κάρτα;",
        "phonetic_hint": "plee-RO-neh-teh meh meh-tree-TAH ee pro-tee-MAH-teh KAHR-tah",
        "english": "Are you paying in cash or do you prefer card?",
        "notes": "Klik A1 p. 162, 164. Retail cashier standard question: με μετρητά (cash) ή με κάρτα (card).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πληρώνετε με μετρητά ή προτιμάτε κάρτα; — Με κάρτα, παρακαλώ.",
        "example_en": "— Are you paying in cash or do you prefer card? — By card, please.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Offering payment method choices at the cash register"
    },
    {
        "id": "A1-U108B-040",
        "greek": "Θα πληρώσω με πιστωτική κάρτα χωρίς επαφή.",
        "phonetic_hint": "thah plee-RO-so meh pee-sto-tee-KEE KAHR-tah kho-REES eh-pah-FEE",
        "english": "I will pay with a contactless credit card.",
        "notes": "Klik A1 p. 162, 164. Modern commercial phrase: πιστωτική κάρτα χωρίς επαφή (contactless credit card).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πώς θα πληρώσετε; — Θα πληρώσω με πιστωτική κάρτα χωρίς επαφή.",
        "example_en": "— How will you pay? — I will pay with a contactless credit card.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Selecting electronic card payment at checkout"
    },
    {
        "id": "A1-U108B-041",
        "greek": "Ορίστε τα ρέστα σας και η απόδειξη αγοράς.",
        "phonetic_hint": "o-REE-steh tah REH-stah sahs keh ee ah-PO-theek-see ah-go-RAHS",
        "english": "Here is your change and the purchase receipt.",
        "notes": "Klik A1 p. 162, 164. Vocabulary: τα ρέστα (change), η απόδειξη (receipt). Concluding cashier turn.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ορίστε τα ρέστα σας και η απόδειξη αγοράς. — Ευχαριστώ πολύ, καλή σας μέρα!",
        "example_en": "— Here is your change and the purchase receipt. — Thank you very much, have a nice day!",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Delivering monetary change and receipt to a shopper"
    },
    {
        "id": "A1-U108B-042",
        "greek": "Κρατήστε την απόδειξη σε περίπτωση που θέλετε να κάνετε αλλαγή.",
        "phonetic_hint": "krah-TEE-steh teen ah-PO-theek-see seh peh-REE-pto-see poo THEH-leh-teh nah KAH-neh-teh ah-lah-YEE",
        "english": "Keep the receipt in case you want to make an exchange.",
        "notes": "Klik A1 p. 162, 164. Imperative κρατήστε + phrase σε περίπτωση που (in case) + αλλαγή (exchange/return).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Μπορώ να αλλάξω το νούμερο αν δεν κάνει; — Ναι, κρατήστε την απόδειξη σε περίπτωση που θέλετε να κάνετε αλλαγή.",
        "example_en": "— Can I exchange the size if it does not fit? — Yes, keep the receipt in case you want to make an exchange.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Explaining exchange policy conditions requiring a receipt"
    },

    # =========================================================================
    # 6. Holiday Greetings, Invitations & Celebrations (pp. 155-157, 168-174)
    # =========================================================================
    {
        "id": "A1-U108B-043",
        "greek": "Καλά Χριστούγεννα και καλή χρονιά σε όλη την οικογένεια!",
        "phonetic_hint": "kah-LAH khree-STOO-yeh-nah keh kah-LEE khro-NYAH seh O-lee teen ee-ko-YEH-nyah",
        "english": "Merry Christmas and a Happy New Year to the whole family!",
        "notes": "Klik A1 p. 155, 172. Essential seasonal holiday wish pairing Christmas and the New Year.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Φεύγουμε για τις διακοπές των γιορτών! — Καλά Χριστούγεννα και καλή χρονιά σε όλη την οικογένεια!",
        "example_en": "— We are leaving for the festive holidays! — Merry Christmas and a Happy New Year to the whole family!",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Exchanging traditional Christmas and New Year wishes"
    },
    {
        "id": "A1-U108B-044",
        "greek": "Χρόνια πολλά για την ονομαστική σου γιορτή, να χαίρεσαι το όνομά σου!",
        "phonetic_hint": "KHRO-nyah po-LAH yah teen o-no-mah-stee-KEE soo yor-TEE, nah KHEH-reh-seh to O-no-MAH soo",
        "english": "Happy name day, may you rejoice in your name!",
        "notes": "Klik A1 p. 155, 172. Cultural tradition: In Greece, name days (ονομαστική γιορτή) are widely celebrated with this formulaic wish.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Σήμερα γιορτάζει ο Γιώργος! — Χρόνια πολλά για την ονομαστική σου γιορτή, να χαίρεσαι το όνομά σου!",
        "example_en": "— Today Giorgos is celebrating his name day! — Happy name day, may you rejoice in your name!",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Wishing someone well on their Greek Orthodox name day"
    },
    {
        "id": "A1-U108B-045",
        "greek": "Καλό Πάσχα και καλή Ανάσταση με υγεία και αγάπη!",
        "phonetic_hint": "kah-LO PAH-skhah keh kah-LEE ah-NAH-stah-see meh ee-YEE-ah keh ah-GHAH-pee",
        "english": "Happy Easter and good Resurrection with health and love!",
        "notes": "Klik A1 p. 155, 172. Traditional Greek Easter wish preceding Holy Saturday / Easter Sunday.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Θα τα πούμε μετά τις γιορτές. — Καλό Πάσχα και καλή Ανάσταση με υγεία και αγάπη!",
        "example_en": "— We will talk after the holidays. — Happy Easter and good Resurrection with health and love!",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Offering traditional Greek Easter holiday greetings"
    },
    {
        "id": "A1-U108B-046",
        "greek": "Το Σάββατο έχω τα γενέθλιά μου και κάνω πάρτι στο σπίτι.",
        "phonetic_hint": "to SAH-vah-to EH-kho tah yeh-NEH-thlee-ah moo keh KAH-no PAR-tee sto SPEE-tee",
        "english": "On Saturday it is my birthday and I am throwing a party at home.",
        "notes": "Klik A1 p. 168, 170. Social invitations: τα γενέθλιά μου (my birthday) + κάνω πάρτι (to throw a party).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Το Σάββατο έχω τα γενέθλιά μου και κάνω πάρτι στο σπίτι. Θα έρθεις; — Εννοείται! Χρόνια πολλά από τώρα!",
        "example_en": "— On Saturday it is my birthday and I am throwing a party at home. Will you come? — Absolutely! Happy birthday in advance!",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Announcing a home birthday party celebration"
    },
    {
        "id": "A1-U108B-047",
        "greek": "Θέλεις να έρθεις μαζί με την παρέα σου στη γιορτή μας;",
        "phonetic_hint": "THEH-lees nah ER-thees mah-ZEE meh teen pah-REH-ah soo stee yor-TEE mahs",
        "english": "Do you want to come along with your friends to our celebration?",
        "notes": "Klik A1 p. 168, 170. Invitation formula: θέλεις να έρθεις + μαζί με (together with) + η παρέα (group of friends).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Θέλεις να έρθεις μαζί με την παρέα σου στη γιορτή μας; — Ευχαριστούμε πολύ, θα έρθουμε με μεγάλη χαρά!",
        "example_en": "— Do you want to come along with your group to our celebration? — Thank you very much, we will come with great joy!",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inviting a friend and their group of companions to a party"
    },
    {
        "id": "A1-U108B-048",
        "greek": "Με μεγάλη μου χαρά να έρθω! Τι ώρα αρχίζει η μουσική;",
        "phonetic_hint": "meh meh-GHAH-lee moo khah-RAH nah ER-tho! tee O-rah ahr-KHEE-zee ee moo-see-KEE",
        "english": "With great pleasure I'll come! What time does the music start?",
        "notes": "Klik A1 p. 168, 170. Social acceptance phrase: Με μεγάλη μου χαρά (with great pleasure) + question about party schedule.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Σε περιμένουμε στο πάρτι απόψε! — Με μεγάλη μου χαρά να έρθω! Τι ώρα αρχίζει η μουσική;",
        "example_en": "— We are expecting you at the party tonight! — With great pleasure I'll come! What time does the music start?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Accepting an invitation enthusiastically and asking event timing"
    },
    {
        "id": "A1-U108B-049",
        "greek": "Στολίζουμε το χριστουγεννιάτικο δέντρο με πολύχρωμα λαμπάκια και μπάλες.",
        "phonetic_hint": "sto-LEE-zoo-meh to khree-stoo-yeh-NYAH-tee-ko THEN-dro meh po-LEE-khro-mah lahm-BAH-kyah keh BAH-les",
        "english": "We decorate the Christmas tree with colorful lights and ornaments.",
        "notes": "Klik A1 p. 156, 172. Cultural holiday action: στολίζω (to decorate) + χριστουγεννιάτικο δέντρο (Christmas tree) + λαμπάκια (fairy lights) + μπάλες (baubles).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Πότε στολίζετε για τις γιορτές; — Κάθε Δεκέμβριο στολίζουμε το χριστουγεννιάτικο δέντρο με πολύχρωμα λαμπάκια και μπάλες.",
        "example_en": "— When do you decorate for the holidays? — Every December we decorate the Christmas tree with colorful lights and ornaments.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing Christmas holiday decorating traditions"
    },
    {
        "id": "A1-U108B-050",
        "greek": "Και του χρόνου με υγεία, να είμαστε πάντα όλοι καλά!",
        "phonetic_hint": "keh too KHRO-noo meh ee-YEE-ah, nah EE-mah-steh PAHN-dah O-lee kah-LAH",
        "english": "And next year with good health, may we always all be well!",
        "notes": "Klik A1 p. 155, 172. Quintessential recurring Greek celebratory toast/wish: Και του χρόνου (may we celebrate again next year).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "— Ήταν μια υπέροχη γιορτή! — Και του χρόνου με υγεία, να είμαστε πάντα όλοι καλά!",
        "example_en": "— It was a wonderful celebration! — And next year with good health, may we always all be well!",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing traditional annual recurring celebratory wishes"
    }
]

lesson_u108b = {
    "unit_id": "unit-108b",
    "lesson_id": "lesson-01",
    "title": "Ενότητα 7: Προτάσεις & Γραμματική — Γιορτές! Ώρα για ψώνια (Pages 151-174)",
    "description": (
        "Expansion & Complementary to Lesson 108: Sentence structures, syntax patterns, "
        "Simple Future tense (θα + στιγμιαίος κορμός), weak direct object pronouns in accusative "
        "(με, σε, τον, την, το, μας, σας, τους, τις, τα), demonstrative contrast (αυτός vs εκείνος), "
        "retail shopping, sizing, fitting rooms, discounts, cashier transactions, and holiday wishes."
    ),
    "lesson_status": "not_started",
    "entries": cards_u108b
}

def main():
    print(f"Writing {len(cards_u108b)} cards to {YAML_PATH}...")
    with open(YAML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(lesson_u108b, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("YAML successfully written.")

    # Update manifest.yaml
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    units = manifest.get("units", [])
    existing = next((u for u in units if u.get("id") == "unit-108b"), None)
    unit_108b_entry = {
        "id": "unit-108b",
        "title": "Κλικ στα Ελληνικά Α1: Σελίδες 151-174 (Ενότητα 7: Γιορτές! Ώρα για ψώνια - Γραμματική & Προτάσεις)",
        "order": "KlikA1-08-B",
        "is_expansion": True,
        "expansion_of": "KlikA1-08-A",
        "lessons": [
            {
                "id": "lesson-01",
                "file": "unit-108b/lesson-01.yaml",
                "title": "Ενότητα 7: Προτάσεις & Γραμματική — Γιορτές! Ώρα για ψώνια (Pages 151-174)",
                "description": (
                    "Expansion & Complementary to Lesson 108: Sentence structures, syntax patterns, "
                    "Simple Future tense (θα + στιγμιαίος κορμός), weak direct object pronouns in accusative "
                    "(με, σε, τον, την, το, μας, σας, τους, τις, τα), demonstrative contrast (αυτός vs εκείνος), "
                    "retail shopping, sizing, fitting rooms, discounts, cashier transactions, and holiday wishes."
                )
            }
        ]
    }

    if existing:
        print("Updating existing unit-108b in manifest.yaml...")
        idx = units.index(existing)
        units[idx] = unit_108b_entry
    else:
        print("Appending unit-108b to manifest.yaml...")
        units.append(unit_108b_entry)

    manifest["units"] = units

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("Manifest successfully updated with unit-108b!")

if __name__ == "__main__":
    main()

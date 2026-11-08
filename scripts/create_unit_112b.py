# -*- coding: utf-8 -*-
"""
Script to create Unit 112b from Klik A1 (Pages 233-255):
Ενότητα 11: Στη σειρά σας παρακαλώ! & Τελική Επανάληψη - Γραμματική & Εκφράσεις
Strictly conforming to docs/LESSON_CREATION_GUIDE.md and the klik-a1-deck-builder skill.
Covers ditransitive verbs with indirect objects (σε ποιον / σε ποια / σε ποιους),
weak indirect pronouns (μου, σου, του, της, μας, σας, τους), direct speech reporting
(λέει/είπε, ρωτάει/ρώτησε, απαντάει/απάντησε), bank/ATM dialogues, post office procedures,
utility bills & queue management, and CEFR A1 capstone review dialogues.
"""
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
UNIT_DIR = CONTENT_DIR / "unit-112b"
UNIT_DIR.mkdir(parents=True, exist_ok=True)
YAML_PATH = UNIT_DIR / "lesson-01.yaml"
MANIFEST_PATH = CONTENT_DIR / "manifest.yaml"

cards_u112b = [
    # =========================================================================
    # 1. Ditransitive Verbs with Indirect Objects: σε ποιον / σε ποια (pp. 236-237)
    # =========================================================================
    {
        "id": "A1-U112B-001",
        "greek": "Σε ποιον στέλνεις αυτό το ηλεκτρονικό μήνυμα; — Στον διευθυντή μου.",
        "phonetic_hint": "seh pyon STEL-nees ahf-TO to ee-lek-tro-nee-KO MEE-nee-mah — ston dhyef-theen-DEE moo",
        "english": "To whom are you sending this email? — To my manager.",
        "notes": "Klik A1 p. 236, 237. Prepositional phrase 'σε ποιον' inquiring about the indirect object recipient (masculine singular).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Σε ποιον στέλνεις αυτό το ηλεκτρονικό μήνυμα; — Στον διευθυντή μου για να εγκρίνει την άδεια.",
        "example_en": "To whom are you sending this email? — To my manager so that he approves the leave.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about recipient with 'σε ποιον'"
    },
    {
        "id": "A1-U112B-002",
        "greek": "Σε ποιον δίνεις τα χρήματα για τον λογαριασμό; — Στον ταμία.",
        "phonetic_hint": "seh pyon DHEE-nees tah KHREE-mah-tah yah ton lo-ghah-ree-ahz-MO — ston tah-MEE-ah",
        "english": "To whom are you giving the money for the bill? — To the teller.",
        "notes": "Klik A1 p. 236, 237. Verb 'δίνω' taking direct object (τα χρήματα) and indirect object (στον ταμία).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Σε ποιον δίνεις τα χρήματα για τον λογαριασμό; — Στον ταμία στο γκισέ της τράπεζας.",
        "example_en": "To whom are you giving the money for the bill? — To the teller at the bank counter.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Indicating payment recipient"
    },
    {
        "id": "A1-U112B-003",
        "greek": "Σε ποια αγοράζεις αυτό το ωραίο δώρο; — Στην αδερφή μου.",
        "phonetic_hint": "seh pyah ah-yo-RAH-zees ahf-TO to o-REH-o DHO-ro — steen ah-dher-FEE moo",
        "english": "For whom are you buying this nice gift? — For my sister.",
        "notes": "Klik A1 p. 236, 237. Prepositional phrase 'σε ποια' asking for feminine recipient with 'αγοράζω'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Σε ποια αγοράζεις αυτό το ωραίο δώρο; — Στην αδερφή μου που έχει γενέθλια αύριο.",
        "example_en": "For whom are you buying this nice gift? — For my sister whose birthday is tomorrow.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Asking for feminine gift recipient"
    },
    {
        "id": "A1-U112B-004",
        "greek": "Σε ποιους είπες τα ευχάριστα νέα για τη δουλειά; — Στους φίλους μου.",
        "phonetic_hint": "seh pyoos EE-pes tah ef-KHAH-ree-stah NEH-ah yah tee dhoo-LYAH — stoos FEE-loos moo",
        "english": "To whom did you tell the pleasant news about the job? — To my friends.",
        "notes": "Klik A1 p. 236, 237. Plural interrogative 'σε ποιους' answered with masculine plural 'στους φίλους μου'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Σε ποιους είπες τα ευχάριστα νέα για τη δουλειά; — Στους φίλους μου και στους συγγενείς μου.",
        "example_en": "To whom did you tell the great news about the job? — To my friends and relatives.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Relaying news to plural recipients"
    },
    {
        "id": "A1-U112B-005",
        "greek": "Γράφω μια επίσημη επιστολή στην τράπεζα για το δάνειο.",
        "phonetic_hint": "GHRAH-fo myah eh-PEE-see-mee eh-pee-sto-LEE steen TRAH-peh-zah yah to DHAH-nee-o",
        "english": "I am writing an official letter to the bank about the loan.",
        "notes": "Klik A1 p. 236, 237. Verb 'γράφω' followed by feminine direct object and prepositional recipient 'στην τράπεζα'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Γράφω μια επίσημη επιστολή στην τράπεζα για το στεγαστικό δάνειο.",
        "example_en": "I am writing an official letter to the bank regarding the home mortgage loan.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Addressing written requests to organizations"
    },
    {
        "id": "A1-U112B-006",
        "greek": "Στέλνω ένα συστημένο δέμα στους γονείς μου στην Κρήτη.",
        "phonetic_hint": "STEL-no EH-nah see-stee-MEH-no DHEH-mah stoos gho-NEES moo steen KREE-tee",
        "english": "I am sending a registered parcel to my parents in Crete.",
        "notes": "Klik A1 p. 236, 238. Ditransitive construction combining postal terminology with indirect object.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Στέλνω ένα συστημένο δέμα στους γονείς μου στην Κρήτη με το ταχυδρομείο.",
        "example_en": "I am sending a registered package to my parents in Crete via the post office.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing postal shipments"
    },
    {
        "id": "A1-U112B-007",
        "greek": "Τι έδωσες στον ταχυδρόμο; — Του έδωσα την υπογραφή μου.",
        "phonetic_hint": "tee EH-dho-ses ston tah-khee-DHRO-mo — too EH-dho-sah teen ee-po-ghrah-FEE moo",
        "english": "What did you give to the mailman? — I gave him my signature.",
        "notes": "Klik A1 p. 237. Alternation between full prepositional phrase ('στον ταχυδρόμο') and weak clitic ('του έδωσα').",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τι έδωσες στον ταχυδρόμο; — Του έδωσα την υπογραφή μου για το πακέτο.",
        "example_en": "What did you give to the postman? — I gave him my signature for the package.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Answering what was given to service workers"
    },
    {
        "id": "A1-U112B-008",
        "greek": "Δείχνω την αστυνομική ταυτότητά μου στον υπάλληλο.",
        "phonetic_hint": "DHEEKH-no teen ah-stee-no-mee-KEE taf-TO-tee-tah moo ston ee-PAH-lee-lo",
        "english": "I show my police ID card to the employee.",
        "notes": "Klik A1 p. 236, 240. Verb 'δείχνω' (I show) + accusative item + prepositional recipient.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Δείχνω την αστυνομική ταυτότητά μου στον υπάλληλο για να επαληθεύσει τα στοιχεία μου.",
        "example_en": "I show my police ID card to the clerk to verify my details.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Presenting ID documents to officials"
    },

    # =========================================================================
    # 2. Weak Indirect Object Pronouns (μου, σου, του, της, μας, σας, τους) (p. 237)
    # =========================================================================
    {
        "id": "A1-U112B-009",
        "greek": "Μου δίνετε το στιλό σας για ένα λεπτό, παρακαλώ;",
        "phonetic_hint": "moo DHEE-neh-teh to stee-LO sahs yah EH-nah lep-TO pah-rah-kah-LO",
        "english": "Could you give me your pen for a minute, please?",
        "notes": "Klik A1 p. 237. First-person weak indirect clitic 'μου' placed immediately before the finite verb.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μου δίνετε το στιλό σας για ένα λεπτό, παρακαλώ, να υπογράψω;",
        "example_en": "Could you please give me your pen for a minute so I can sign?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Politely borrowing writing materials"
    },
    {
        "id": "A1-U112B-010",
        "greek": "Σου στέλνω τον σύνδεσμο της ιστοσελίδας στο κινητό σου.",
        "phonetic_hint": "soo STEL-no ton SEEN-dhez-mo tees ees-to-seh-LEE-dhahs sto kee-nee-TO soo",
        "english": "I am sending you the website link to your mobile phone.",
        "notes": "Klik A1 p. 233, 237. Second-person informal clitic 'σου'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Σου στέλνω τον σύνδεσμο της ιστοσελίδας στο κινητό σου για να δεις την αίτηση.",
        "example_en": "I am sending you the link to the website on your mobile to see the form.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Sharing links with friends"
    },
    {
        "id": "A1-U112B-011",
        "greek": "Του έδωσα τον κωδικό για να μπει στον λογαριασμό.",
        "phonetic_hint": "too EH-dho-sah ton ko-dhee-KO yah nah bee ston lo-ghah-ree-ahz-MO",
        "english": "I gave him the code to log into the account.",
        "notes": "Klik A1 p. 233, 237. Third-person masculine weak pronoun 'του' (to him).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Του έδωσα τον κωδικό για να μπει στον λογαριασμό και να κάνει την πληρωμή.",
        "example_en": "I gave him the code to enter the account and make the payment.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Giving credentials to a third person"
    },
    {
        "id": "A1-U112B-012",
        "greek": "Της είπα ότι η τράπεζα κλείνει στις δύο και μισή.",
        "phonetic_hint": "tees EE-pah O-tee ee TRAH-peh-zah KLEE-nee stees DHEE-o keh mee-SEE",
        "english": "I told her that the bank closes at two thirty.",
        "notes": "Klik A1 p. 237. Third-person feminine weak pronoun 'της' (to her) before 'είπα'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Της είπα ότι η τράπεζα κλείνει στις δύο και μισή και πρέπει να βιαστούμε.",
        "example_en": "I told her that the bank closes at two thirty and we need to hurry.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Informing a female acquaintance"
    },
    {
        "id": "A1-U112B-013",
        "greek": "Μας έστειλαν την απόδειξη πληρωμής με ηλεκτρονικό μήνυμα.",
        "phonetic_hint": "mahs EH-stee-lahn teen ah-PO-dheek-see plee-ro-MEES meh ee-lek-tro-nee-KO MEE-nee-mah",
        "english": "They sent us the payment receipt by email.",
        "notes": "Klik A1 p. 234, 237. First-person plural clitic 'μας' (to us).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μας έστειλαν την απόδειξη πληρωμής με ηλεκτρονικό μήνυμα αμέσως μετά την αγορά.",
        "example_en": "They sent us the payment receipt by email immediately after the purchase.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Confirming receipt of confirmation"
    },
    {
        "id": "A1-U112B-014",
        "greek": "Σας παραδίδω το διαβατήριό σας ανανεωμένο.",
        "phonetic_hint": "sahs pah-rah-DHEE-dho to dhyah-vah-TEE-ree-o sahs ah-nah-neh-o-MEH-no",
        "english": "I hand you your renewed passport.",
        "notes": "Klik A1 p. 237, 240. Polite second-person plural clitic 'σας' (to you).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ορίστε, κύριε Παπαδόπουλε, σας παραδίδω το διαβατήριό σας ανανεωμένο.",
        "example_en": "Here you are, Mr. Papadopoulos, I hand you your renewed passport.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Handing official documents to clients"
    },
    {
        "id": "A1-U112B-015",
        "greek": "Τους εξήγησα πώς να συμπληρώσουν την αίτηση.",
        "phonetic_hint": "toos ek-SEE-yee-sah pos nah seem-blee-RO-soon teen EH-tee-see",
        "english": "I explained to them how to fill out the application.",
        "notes": "Klik A1 p. 234, 237. Third-person plural clitic 'τους' (to them).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τους εξήγησα προσεκτικά πώς να συμπληρώσουν την αίτηση στα ελληνικά.",
        "example_en": "I explained to them carefully how to fill out the application in Greek.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Helping others with administrative paperwork"
    },
    {
        "id": "A1-U112B-016",
        "greek": "Μου είπε ο ταμίας ότι δεν έχω αρκετό υπόλοιπο.",
        "phonetic_hint": "moo EE-peh o tah-MEE-ahs O-tee dhen EH-kho ahr-keh-TO ee-PO-lee-po",
        "english": "The cashier told me that I do not have sufficient balance.",
        "notes": "Klik A1 p. 234, 237. Clitic pronoun 'μου' preceding verb with post-verbal subject 'ο ταμίας'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μου είπε ο ταμίας ότι δεν έχω αρκετό υπόλοιπο για να κάνω ανάληψη.",
        "example_en": "The teller told me that I don't have enough balance to make a withdrawal.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Reporting account balance feedback"
    },

    # =========================================================================
    # 3. Direct Speech Reporting: λέει / είπε, ρωτάει / ρώτησε (pp. 241-242)
    # =========================================================================
    {
        "id": "A1-U112B-017",
        "greek": "Ο υπάλληλος είπε: «Για τα γράμματα θα περιμένετε εδώ».",
        "phonetic_hint": "o ee-PAH-lee-los EE-peh «yah tah GHRAH-mah-tah thah peh-ree-MEH-neh-teh eh-DHO»",
        "english": "The clerk said: 'For letters you will wait here.'",
        "notes": "Klik A1 p. 241, 242. Greek quotation marks («...») framing direct speech after 'είπε:'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο υπάλληλος είπε: «Για τα γράμματα θα περιμένετε εδώ στη σειρά σας».",
        "example_en": "The employee said: 'For letters you will wait here in your line.'",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Reporting employee instructions directly"
    },
    {
        "id": "A1-U112B-018",
        "greek": "Η πελάτισσα ρώτησε: «Πόσο κοστίζουν τα γραμματόσημα;».",
        "phonetic_hint": "ee peh-LAH-tees-sah RO-tee-seh «PO-so ko-STEE-zoon tah ghrah-mah-TO-see-mah»",
        "english": "The customer asked: 'How much do the stamps cost?'",
        "notes": "Klik A1 p. 241, 242. Reporting questions directly with 'ρώτησε: «...;»'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η πελάτισσα ρώτησε: «Πόσο κοστίζουν τα γραμματόσημα για την Ευρώπη;».",
        "example_en": "The customer asked: 'How much do stamps for Europe cost?'",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Quoting customer questions directly"
    },
    {
        "id": "A1-U112B-019",
        "greek": "Ο αστυνομικός ρώτησε: «Ποιο είναι το όχημα που ενεπλάκη;».",
        "phonetic_hint": "o ah-stee-no-mee-KOS RO-tee-seh «pyo EE-neh to O-khee-mah poo eh-neh-PLAH-kee»",
        "english": "The police officer asked: 'Which is the vehicle that was involved?'",
        "notes": "Klik A1 p. 241. Quoting formal police questioning.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο αστυνομικός ρώτησε: «Ποιο είναι το όχημα που ενεπλάκη στο τροχαίο;».",
        "example_en": "The police officer asked: 'Which is the vehicle involved in the crash?'",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Reporting police inquiries"
    },
    {
        "id": "A1-U112B-020",
        "greek": "Ο οδηγός απάντησε: «Δεν είδα το κόκκινο φανάρι».",
        "phonetic_hint": "o o-dhee-GHOS ah-PAHN-dee-seh «dhen EE-dhah to KOK-kee-no fah-NAH-ree»",
        "english": "The driver answered: 'I did not see the red light.'",
        "notes": "Klik A1 p. 241, 242. Direct speech reporting with 'απάντησε'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο οδηγός απάντησε: «Δεν είδα το κόκκινο φανάρι γιατί είχε ομίχλη».",
        "example_en": "The driver answered: 'I didn't see the red light because it was foggy.'",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Reporting testimony directly"
    },
    {
        "id": "A1-U112B-021",
        "greek": "Η ταμίας είπε: «Περάστε στο ταμείο νούμερο δύο, παρακαλώ».",
        "phonetic_hint": "ee tah-MEE-ahs EE-peh «peh-RAHS-teh sto tah-MEE-o NOO-meh-ro DHEE-o pah-rah-kah-LO»",
        "english": "The teller said: 'Proceed to counter number two, please.'",
        "notes": "Klik A1 p. 235, 241. Quoting bank staff calling the next client.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η ταμίας είπε: «Περάστε στο ταμείο νούμερο δύο, παρακαλώ, για την ανάληψη».",
        "example_en": "The teller said: 'Proceed to counter number two, please, for the withdrawal.'",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Calling next customer to counter"
    },
    {
        "id": "A1-U112B-022",
        "greek": "Ο Νίκος ρώτησε: «Μπορώ να ανοίξω λογαριασμό από το διαδίκτυο;».",
        "phonetic_hint": "o NEE-kos RO-tee-seh «bo-RO nah ah-NEEK-so lo-ghah-ree-ahz-MO ah-PO to dhyah-DHEEK-tee-o»",
        "english": "Nikos asked: 'Can I open an account from the internet?'",
        "notes": "Klik A1 p. 233, 241. Quoting an online banking eligibility question.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο Νίκος ρώτησε: «Μπορώ να ανοίξω λογαριασμό από το διαδίκτυο χωρίς να πάω στο κατάστημα;».",
        "example_en": "Nikos asked: 'Can I open an account online without going to the branch?'",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Quoting digital service inquiries"
    },
    {
        "id": "A1-U112B-023",
        "greek": "Ο διευθυντής είπε: «Η αίτησή σας εγκρίθηκε σήμερα το πρωί».",
        "phonetic_hint": "o dhyef-theen-DEES EE-peh «ee EH-tee-see sahs eng-GREE-thee-keh SEE-meh-rah to pro-EE»",
        "english": "The manager said: 'Your application was approved this morning.'",
        "notes": "Klik A1 p. 241. Reporting administrative approval.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο διευθυντής είπε: «Η αίτησή σας εγκρίθηκε σήμερα το πρωί και μπορείτε να υπογράψετε».",
        "example_en": "The manager said: 'Your application was approved this morning and you can sign.'",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Reporting administrative status"
    },
    {
        "id": "A1-U112B-024",
        "greek": "Η κυρία Ελένη είπε: «Θέλω να στείλω αυτό το δέμα επείγον».",
        "phonetic_hint": "ee kee-REE-ah eh-LEH-nee EE-peh «THEH-lo nah STEE-lo ahf-TO to DHEH-mah eh-PEE-ghon»",
        "english": "Mrs. Eleni said: 'I want to send this parcel express.'",
        "notes": "Klik A1 p. 238, 241. Direct postal instruction quote.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Η κυρία Ελένη είπε: «Θέλω να στείλω αυτό το δέμα επείγον στην Αγγλία».",
        "example_en": "Mrs. Eleni said: 'I want to send this parcel express to England.'",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Quoting customer shipping choice"
    },

    # =========================================================================
    # 4. Bank & ATM Transactions Dialogues (pp. 233-236, 245)
    # =========================================================================
    {
        "id": "A1-U112B-025",
        "greek": "Καλημέρα σας, θα ήθελα να ανοίξω έναν λογαριασμό ταμιευτηρίου.",
        "phonetic_hint": "kah-lee-MEH-rah sahs thah EE-theh-lah nah ah-NEEK-so EH-nahn lo-ghah-ree-ahz-MO tah-mee-ef-tee-REE-oo",
        "english": "Good morning, I would like to open a savings account.",
        "notes": "Klik A1 p. 234. Polite conditional formula 'θα ήθελα να + subjunctive'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Καλημέρα σας, θα ήθελα να ανοίξω έναν λογαριασμό ταμιευτηρίου στην τράπεζά σας.",
        "example_en": "Good morning, I would like to open a savings account in your bank.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Polite bank account opening request"
    },
    {
        "id": "A1-U112B-026",
        "greek": "Συμπληρώστε αυτή την αίτηση και υπογράψτε στο κάτω μέρος.",
        "phonetic_hint": "seem-blee-RO-steh ahf-TEEN teen EH-tee-see keh ee-po-GHRAHP-steh sto KAH-to MEH-ros",
        "english": "Fill out this application and sign at the bottom.",
        "notes": "Klik A1 p. 234, 235. Formal imperative forms: 'συμπληρώστε' and 'υπογράψτε'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Συμπληρώστε αυτή την αίτηση με τα στοιχεία σας και υπογράψτε στο κάτω μέρος.",
        "example_en": "Fill out this application with your details and sign at the bottom.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Giving administrative completion instructions"
    },
    {
        "id": "A1-U112B-027",
        "greek": "Χρειάζομαι την ταυτότητά σας και ένα αποδεικτικό του ΑΦΜ σας.",
        "phonetic_hint": "khree-AH-zo-meh teen taf-TO-tee-tah sahs keh EH-nah ah-po-dheek-tee-KO too ah-fee-MEE sahs",
        "english": "I need your ID card and a proof of your tax identification number.",
        "notes": "Klik A1 p. 234, 236. Standard customer due diligence requirements in Greek banks.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Χρειάζομαι την ταυτότητά σας και ένα αποδεικτικό του ΑΦΜ σας για να ολοκληρώσω την εγγραφή.",
        "example_en": "I need your ID card and proof of your tax number to complete registration.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Requesting official identification documents"
    },
    {
        "id": "A1-U112B-028",
        "greek": "Θέλω να κάνω μια κατάθεση τριακοσίων ευρώ στον λογαριασμό μου.",
        "phonetic_hint": "THEH-lo nah KAH-no myah kah-TAH-theh-see tree-ah-ko-SEE-on ev-RO ston lo-ghah-ree-ahz-MO moo",
        "english": "I want to make a deposit of three hundred euros into my account.",
        "notes": "Klik A1 p. 234, 235, 245. High-frequency banking counter transaction statement.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Θέλω να κάνω μια κατάθεση τριακοσίων ευρώ στον λογαριασμό μου με μετρητά.",
        "example_en": "I want to make a cash deposit of three hundred euros into my account.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Depositing funds at bank counter"
    },
    {
        "id": "A1-U112B-029",
        "greek": "Θέλω να κάνω μια ανάληψη εκατόν πενήντα ευρώ από το ταμείο.",
        "phonetic_hint": "THEH-lo nah KAH-no myah ah-NAH-leep-see eh-kah-TON peh-NEEN-dah ev-RO ah-PO to tah-MEE-o",
        "english": "I want to make a withdrawal of one hundred fifty euros from the counter.",
        "notes": "Klik A1 p. 235, 245. Specifying cash withdrawal sum.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Θέλω να κάνω μια ανάληψη εκατόν πενήντα ευρώ από το ταμείο, ορίστε το βιβλιάριό μου.",
        "example_en": "I want to withdraw 150 euros from the counter, here is my passbook.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Withdrawing cash at bank desk"
    },
    {
        "id": "A1-U112B-030",
        "greek": "Βάλτε την κάρτα σας στη σχισμή και πληκτρολογήστε το PIN σας.",
        "phonetic_hint": "VAHL-teh teen KAHR-tah sahs stee skheez-MEE keh pleek-tro-lo-YEE-steh to peen sahs",
        "english": "Insert your card into the slot and type in your PIN.",
        "notes": "Klik A1 p. 235. Step-by-step instructions for ATM operation.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Βάλτε την κάρτα σας στη σχισμή και πληκτρολογήστε το PIN σας προσεκτικά.",
        "example_en": "Insert your card into the slot and key in your PIN carefully.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Following ATM step-by-step instructions"
    },
    {
        "id": "A1-U112B-031",
        "greek": "Επιλέξτε το ποσό που θέλετε και μην ξεχάσετε την κάρτα σας.",
        "phonetic_hint": "eh-pee-LEHK-steh to po-SO poo THEH-leh-teh keh meen kseh-KHAH-seh-teh teen KAHR-tah sahs",
        "english": "Select the amount you want and do not forget your card.",
        "notes": "Klik A1 p. 235. ATM final safety reminder.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Επιλέξτε το ποσό που θέλετε στην οθόνη και μην ξεχάσετε την κάρτα σας.",
        "example_en": "Select the amount you want on screen and don't forget your card.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Completing cash withdrawal at ATM"
    },
    {
        "id": "A1-U112B-032",
        "greek": "Ποιο είναι το διαθέσιμο υπόλοιπο του τραπεζικού λογαριασμού μου;",
        "phonetic_hint": "pyo EE-neh to dhyah-THEH-see-mo ee-PO-lee-po too trah-peh-zee-KOO lo-ghah-ree-ahz-MOO moo",
        "english": "What is the available balance of my bank account?",
        "notes": "Klik A1 p. 234. Inquiring about funds available for withdrawal.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Μπορείτε να μου πείτε ποιο είναι το διαθέσιμο υπόλοιπο του τραπεζικού λογαριασμού μου;",
        "example_en": "Could you tell me what the available balance of my bank account is?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about available funds"
    },

    # =========================================================================
    # 5. Post Office Services & Mailing Procedures (pp. 238-239, 242)
    # =========================================================================
    {
        "id": "A1-U112B-033",
        "greek": "Θέλω να στείλω αυτό το γράμμα στην Ισπανία.",
        "phonetic_hint": "THEH-lo nah STEE-lo ahf-TO to GHRAH-mah steen ees-pah-NEE-ah",
        "english": "I want to send this letter to Spain.",
        "notes": "Klik A1 p. 238. Standard opening request at the post office desk.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Γεια σας, θέλω να στείλω αυτό το γράμμα στην Ισπανία αεροπορικώς.",
        "example_en": "Hello, I want to send this letter to Spain by airmail.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Requesting international mail service"
    },
    {
        "id": "A1-U112B-034",
        "greek": "Θέλετε να το στείλετε απλό ή συστημένο;",
        "phonetic_hint": "THEH-leh-teh nah to STEE-leh-teh ah-PLO ee see-stee-MEH-no",
        "english": "Do you want to send it regular or registered?",
        "notes": "Klik A1 p. 238, 239. Classic postal option: 'απλό' (standard) vs 'συστημένο' (tracked).",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Θέλετε να το στείλετε απλό ή συστημένο με αριθμό παρακολούθησης;",
        "example_en": "Do you want to send it regular or registered with a tracking number?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Clarifying postal shipping options"
    },
    {
        "id": "A1-U112B-035",
        "greek": "Πόσο κοστίζει για να πάει επείγον με ταχυμεταφορά;",
        "phonetic_hint": "PO-so ko-STEE-zee yah nah PAH-ee eh-PEE-ghon meh tah-khee-meh-tah-fo-RAH",
        "english": "How much does it cost to go express by courier?",
        "notes": "Klik A1 p. 238. Question on priority delivery tariff.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πόσο κοστίζει για να πάει επείγον με ταχυμεταφορά ώστε να φτάσει αύριο;",
        "example_en": "How much does it cost for express courier delivery so that it arrives tomorrow?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about express postal shipping"
    },
    {
        "id": "A1-U112B-036",
        "greek": "Κολλήστε αυτό το γραμματόσημο επάνω δεξιά στον φάκελο.",
        "phonetic_hint": "ko-LEE-steh ahf-TO to ghrah-mah-TO-see-mo eh-PAH-no dhehk-see-AH ston FAH-keh-lo",
        "english": "Stick this stamp on the top right of the envelope.",
        "notes": "Klik A1 p. 238, 239. Imperative 'κολλήστε' with spatial prepositional phrase.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κολλήστε αυτό το γραμματόσημο επάνω δεξιά στον φάκελο και ρίξτε τον στο κουτί.",
        "example_en": "Stick this stamp on the top right of the envelope and drop it in the box.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Instructing where to affix postage stamps"
    },
    {
        "id": "A1-U112B-037",
        "greek": "Έχω ένα ειδοποιητήριο για ένα δέμα από το εξωτερικό.",
        "phonetic_hint": "EH-kho EH-nah ee-dho-pee-ee-TEE-ree-o yah EH-nah DHEH-mah ah-PO to ek-so-teh-ree-KO",
        "english": "I have a notification slip for a parcel from abroad.",
        "notes": "Klik A1 p. 238, 239. Collecting undelivered mail using the courier/postal notice.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Έχω ένα ειδοποιητήριο για ένα δέμα από το εξωτερικό, ορίστε το χαρτί.",
        "example_en": "I have a collection notice for a parcel from abroad, here is the slip.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Presenting package delivery notifications"
    },
    {
        "id": "A1-U112B-038",
        "greek": "Υπογράψτε εδώ στην οθόνη για να παραλάβετε το πακέτο.",
        "phonetic_hint": "ee-po-GHRAHP-steh eh-DHO steen o-THO-nee yah nah pah-rah-LAH-veh-teh to pah-KEH-to",
        "english": "Sign here on the screen to receive the package.",
        "notes": "Klik A1 p. 238. Modern digital signature directive during parcel delivery.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Υπογράψτε εδώ στην οθόνη με το ηλεκτρονικό στιλό για να παραλάβετε το πακέτο.",
        "example_en": "Sign here on the screen with the stylus to receive the parcel.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Signing for package delivery"
    },
    {
        "id": "A1-U112B-039",
        "greek": "Σε πόσες μέρες θα φτάσει η επιστολή στον προορισμό της;",
        "phonetic_hint": "seh PO-ses MEH-res thah FTAH-see ee eh-pee-sto-LEE ston pro-o-reez-MO tees",
        "english": "In how many days will the letter reach its destination?",
        "notes": "Klik A1 p. 238. Future duration inquiry: 'σε πόσες μέρες...'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Σε πόσες μέρες θα φτάσει η επιστολή στον προορισμό της στην Αμερική;",
        "example_en": "In how many days will the letter reach its destination in America?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inquiring about postal delivery timeframe"
    },

    # =========================================================================
    # 6. Paying Utility Bills & Managing Public Queues (pp. 240, 242)
    # =========================================================================
    {
        "id": "A1-U112B-040",
        "greek": "Ήρθα να πληρώσω τον λογαριασμό της ΔΕΗ και του ΟΤΕ.",
        "phonetic_hint": "EER-thah nah plee-RO-so ton lo-ghah-ree-ahz-MO tees dheh-EE keh too oh-teh-EH",
        "english": "I came to pay the electricity and phone bills.",
        "notes": "Klik A1 p. 240. Stating purpose of visit to bank or post office counter.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ήρθα να πληρώσω τον λογαριασμό της ΔΕΗ και του ΟΤΕ προτού λήξουν.",
        "example_en": "I came to pay the electricity and telephone bills before they expire.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Paying public utility accounts"
    },
    {
        "id": "A1-U112B-041",
        "greek": "Ο λογαριασμός είναι εμπρόθεσμος ή έχει λήξει η προθεσμία;",
        "phonetic_hint": "o lo-ghah-ree-ahz-MOS EE-neh em-BRO-thez-mos ee EH-khee LEEK-see ee pro-thez-MEE-ah",
        "english": "Is the bill on time or has the due date expired?",
        "notes": "Klik A1 p. 240. Distinguishing on-time payment ('εμπρόθεσμος') from overdue ('ληξιπρόθεσμος').",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ο λογαριασμός είναι εμπρόθεσμος ή έχει λήξει η προθεσμία πληρωμής;",
        "example_en": "Is the bill within due date or has the payment deadline expired?",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Checking bill due date status"
    },
    {
        "id": "A1-U112B-042",
        "greek": "Πάρτε ένα νούμερο προτεραιότητας και περιμένετε τη σειρά σας.",
        "phonetic_hint": "PAHR-teh EH-nah NOO-meh-ro pro-teh-reh-O-tee-tahs keh peh-ree-MEH-neh-teh tee seh-RAH sahs",
        "english": "Take a priority ticket number and wait for your turn.",
        "notes": "Klik A1 p. 233, 240. Universal procedure in Greek banks and public agencies.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Πάρτε ένα νούμερο προτεραιότητας από την είσοδο και περιμένετε τη σειρά σας στην αίθουσα.",
        "example_en": "Take a queue ticket from the entrance and wait for your turn in the hall.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Managing queue sequence"
    },
    {
        "id": "A1-U112B-043",
        "greek": "Με συγχωρείτε, είστε στην ουρά ή περιμένετε κάποιον;",
        "phonetic_hint": "meh seen-kho-REE-teh EE-steh steen oo-RAH ee peh-ree-MEH-neh-teh KAH-pyon",
        "english": "Excuse me, are you in the line or waiting for someone?",
        "notes": "Klik A1 p. 233, 242. Essential polite line inquiry in Greek queues.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Με συγχωρείτε, είστε στην ουρά ή περιμένετε κάποιον; — Όχι, είμαι στην ουρά.",
        "example_en": "Excuse me, are you in the line or waiting for someone? — No, I am in line.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Confirming queue position politely"
    },
    {
        "id": "A1-U112B-044",
        "greek": "Ορίστε τα χρήματα ακριβώς, δεν χρειάζομαι ρέστα.",
        "phonetic_hint": "o-REE-steh tah KHREE-mah-tah ah-kree-VOS dhen khree-AH-zo-meh REH-stah",
        "english": "Here is the exact amount, I do not need change.",
        "notes": "Klik A1 p. 235. Phrase for paying with exact change: 'τα χρήματα ακριβώς'.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Ορίστε τα χρήματα ακριβώς, είκοσι πέντε ευρώ, δεν χρειάζομαι ρέστα.",
        "example_en": "Here is the exact money, twenty-five euros, I don't need change.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Paying exact cash without change"
    },
    {
        "id": "A1-U112B-045",
        "greek": "Κρατήστε το απόκομμα της πληρωμής ως επίσημη απόδειξη.",
        "phonetic_hint": "krah-TEES-teh to ah-PO-ko-mah tees plee-ro-MEES os eh-PEE-see-mee ah-PO-dheek-see",
        "english": "Keep the payment stub as an official receipt.",
        "notes": "Klik A1 p. 240. Clerk advice on keeping utility payment proof.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Κρατήστε το απόκομμα της πληρωμής ως επίσημη απόδειξη για το αρχείο σας.",
        "example_en": "Keep the payment receipt stub as proof for your records.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Retaining official transaction proof"
    },

    # =========================================================================
    # 7. CEFR A1 Capstone Comprehensive Review Dialogues (pp. 249-254)
    # =========================================================================
    {
        "id": "A1-U112B-046",
        "greek": "Σε προσκαλώ στο πάρτι των γενεθλίων μου το Σάββατο στις επτά.",
        "phonetic_hint": "seh pros-kah-LO sto PAHR-tee ton yeh-neh-THLEE-on moo to SAH-vah-to stees ep-TAH",
        "english": "I invite you to my birthday party on Saturday at seven.",
        "notes": "Klik A1 p. 249. Official A1 exam prompt on social invitations.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Σε προσκαλώ στο πάρτι των γενεθλίων μου το Σάββατο στις επτά στο σπίτι μου στο κέντρο.",
        "example_en": "I invite you to my birthday party on Saturday at seven at my home in the center.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Inviting friends to social events"
    },
    {
        "id": "A1-U112B-047",
        "greek": "Αν δεν μπορείς να έρθεις, τηλεφώνησέ μου ή στείλε μου μήνυμα.",
        "phonetic_hint": "ahn dhen bo-REES nah ER-thees tee-leh-FO-nee-SEH moo ee STEE-leh moo MEE-nee-mah",
        "english": "If you cannot come, call me or send me a text message.",
        "notes": "Klik A1 p. 249. Real condition with 'αν' followed by imperatives with clitics.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Αν δεν μπορείς να έρθεις, τηλεφώνησέ μου εγκαίρως ή στείλε μου μήνυμα.",
        "example_en": "If you cannot come, call me in good time or send me a message.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Giving RSVP conditional instructions"
    },
    {
        "id": "A1-U112B-048",
        "greek": "Τι καιρό κάνει στην Ελλάδα το καλοκαίρι; — Κάνει πολλή ζέστη και έχει ήλιο.",
        "phonetic_hint": "tee keh-RO KAH-nee steen eh-LAH-dhah to kah-lo-KEH-ree — KAH-nee po-LEE ZES-tee keh EH-khee EE-lyo",
        "english": "What is the weather like in Greece in the summer? — It is very hot and sunny.",
        "notes": "Klik A1 p. 251, 252. A1 oral synthesis question describing climate.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Τι καιρό κάνει στην Ελλάδα το καλοκαίρι; — Κάνει πολλή ζέστη και έχει ήλιο όλη μέρα.",
        "example_en": "What is the weather like in Greece during summer? — It is very hot and sunny all day.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Describing summer weather patterns"
    },
    {
        "id": "A1-U112B-049",
        "greek": "Θα ήθελα να κλείσω ένα τραπέζι για δύο άτομα για απόψε το βράδυ.",
        "phonetic_hint": "thah EE-theh-lah nah KLEE-so EH-nah trah-PEH-zee yah DHEE-o AH-to-mah yah ah-PO-bseh to VRAH-dhee",
        "english": "I would like to book a table for two people for tonight.",
        "notes": "Klik A1 p. 252, 254. Core communicative task for reserving at a restaurant.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Καλησπέρα σας, θα ήθελα να κλείσω ένα τραπέζι για δύο άτομα για απόψε το βράδυ στις εννέα.",
        "example_en": "Good evening, I would like to book a table for two people for tonight at nine.",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Booking a restaurant table"
    },
    {
        "id": "A1-U112B-050",
        "greek": "Χαίρομαι πολύ που σε ξαναβλέπω μετά από τόσα χρόνια!",
        "phonetic_hint": "KHEH-ro-meh po-LEE poo seh ksah-nah-VLEH-po meh-TAH ah-PO TO-sah KHRO-nyah",
        "english": "I am so glad to see you again after so many years!",
        "notes": "Klik A1 p. 254. Capstone social dialogue roleplay celebrating reunion.",
        "gender_or_pos": "phrase",
        "audio": None,
        "status": "pending_tts",
        "example_el": "Χαίρομαι πάρα πολύ που σε ξαναβλέπω μετά από τόσα χρόνια, είσαι μια χαρά!",
        "example_en": "I am so glad to see you again after so many years, you look great!",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Expressing joy at meeting an old acquaintance"
    }
]

lesson_u112b = {
    "unit_id": "unit-112b",
    "lesson_id": "lesson-01",
    "title": "Ενότητα 11: Στη σειρά σας παρακαλώ! & Τελική Επανάληψη — Γραμματική & Εκφράσεις (Pages 233-255)",
    "description": (
        "Grammar paradigms, administrative syntax, and capstone exam dialogues from Unit 11 and the final review of Klik sta Ellinika A1: "
        "ditransitive verbs with indirect objects (σε ποιον / σε ποια / σε ποιους), "
        "weak indirect pronouns (μου, σου, του, της, μας, σας, τους), "
        "direct speech quotation reporting (λέει/είπε, ρωτάει/ρώτησε, απαντάει/απάντησε), "
        "bank counter consultations and ATM transaction dialogues, "
        "post office shipping options (απλό vs συστημένο, επείγον), "
        "utility bill settlement and public queuing etiquette (ΔΕΗ, ΟΤΕ, νούμερο προτεραιότητας), "
        "and CEFR A1 certification capstone oral and written communicative tasks."
    ),
    "lesson_status": "not_started",
    "entries": cards_u112b
}

def main():
    print(f"Writing {len(cards_u112b)} cards to {YAML_PATH}...")
    with open(YAML_PATH, "w", encoding="utf-8") as f:
        yaml.dump(lesson_u112b, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("YAML successfully written.")

    # Update manifest.yaml
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)

    units = manifest.get("units", [])
    existing = next((u for u in units if u.get("id") == "unit-112b"), None)
    unit_112b_entry = {
        "id": "unit-112b",
        "title": "Κλικ στα Ελληνικά Α1: Σελίδες 233-255 (Ενότητα 11: Στη σειρά σας παρακαλώ! & Τελική Επανάληψη - Γραμματική & Εκφράσεις)",
        "order": "KlikA1-12-B",
        "is_expansion": True,
        "expansion_of": "KlikA1-12-A",
        "lessons": [
            {
                "id": "lesson-01",
                "file": "unit-112b/lesson-01.yaml",
                "title": "Ενότητα 11: Στη σειρά σας παρακαλώ! & Τελική Επανάληψη — Γραμματική & Εκφράσεις (Pages 233-255)"
            }
        ]
    }

    if existing:
        print("Updating existing unit-112b in manifest.yaml...")
        idx = units.index(existing)
        units[idx] = unit_112b_entry
    else:
        print("Appending unit-112b to manifest.yaml...")
        units.append(unit_112b_entry)

    manifest["units"] = units

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print("Manifest successfully updated with unit-112b!")

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Generate KEG-A2 Batch 6:
- Unit A2-11: KEG-A2-11-A (35 cards) - Culture, Entertainment & Digital Media (Πολιτισμός, ΜΜΕ & Ψηφιακή Ζωή)
- Unit A2-12: KEG-A2-12-A (35 cards) - Exam Workshop & Simulation (Εξεταστικό Εργαστήριο & Προσομοίωση)
Includes dual exam-style example sentences and multi-threaded Google Cloud Chirp-3 HD TTS.
"""
import sys
import os
import yaml
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from server.tts_service import synthesize_greek_chirp, generate_audio_filename

AUDIO_DIR = BASE_DIR / "audio"
CONTENT_DIR = BASE_DIR / "content"

# -------------------------------------------------------------
# UNIT A2-11 CARDS (35 cards)
# Theme: Culture, Entertainment & Digital Media (Πολιτισμός & ΜΜΕ)
# -------------------------------------------------------------
CARDS_U11 = [
    {
        "id": "A2-U11-001",
        "greek": "ο πολιτισμός",
        "english": "culture / civilization",
        "notes": "Masculine noun in -ός (-οί). Covers arts, cultural heritage, and historical civilization.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι πολιτισμοί",
            "adjective": "πολιτιστικός, -ή, -ό",
            "collocation": "υπουργείο πολιτισμού (ministry of culture)"
        },
        "keg_communicative_function": "Discussing cultural events, festivals, and Greek heritage in Reading Part 2",
        "example_el": "Η Ελλάδα έχει πλούσιο πολιτισμό και μακραίωνη ιστορία που προσελκύει εκατομμύρια επισκέπτες.",
        "example_en": "Greece has a rich culture and long history that attracts millions of visitors.",
        "example2_el": "Ο δήμος διοργανώνει πολιτιστικές εκδηλώσεις για μικρούς και μεγάλους.",
        "example2_en": "The municipality organizes cultural events for young and old."
    },
    {
        "id": "A2-U11-002",
        "greek": "η τέχνη",
        "english": "art",
        "notes": "Feminine noun in -η (-ες). Covers fine arts, painting, music, and theater.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι τέχνες",
            "adjective": "καλλιτεχνικός, -ή, -ό",
            "collocation": "έργο τέχνης (work of art)"
        },
        "keg_communicative_function": "Appreciating exhibitions and discussing creative hobbies",
        "example_el": "Η μοντέρνα τέχνη εκφράζει τις αγωνίες και τις ιδέες της σύγχρονης κοινωνίας.",
        "example_en": "Modern art expresses the anxieties and ideas of contemporary society.",
        "example2_el": "Στην πινακοθήκη εκτίθενται αριστουργήματα της νεοελληνικής τέχνης.",
        "example2_en": "Masterpieces of modern Greek art are exhibited in the art gallery."
    },
    {
        "id": "A2-U11-003",
        "greek": "η παράσταση",
        "english": "performance / theatrical show",
        "notes": "Feminine noun in -η (-εις). Relates to theater, dance, or musical concerts.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι παραστάσεις",
            "genitive_singular": "της παράστασης",
            "collocation": "θεατρική παράσταση"
        },
        "keg_communicative_function": "Booking tickets and reviewing theater performances in personal letters",
        "example_el": "Η θεατρική παράσταση ξεκινάει ακριβώς στις εννιά το βράδυ.",
        "example_en": "The theatrical performance begins at exactly nine in the evening.",
        "example2_el": "Παρακολουθήσαμε μια εξαιρετική αρχαία τραγωδία στην Επίδαυρο.",
        "example2_en": "We attended an extraordinary ancient tragedy at Epidaurus."
    },
    {
        "id": "A2-U11-004",
        "greek": "η συναυλία",
        "english": "concert / live music show",
        "notes": "Feminine noun in -α (-ες). Key cultural pastime in Greek summer open-air theaters.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι συναυλίες",
            "collocation": "εισιτήριο συναυλίας"
        },
        "keg_communicative_function": "Inviting friends to concerts and arranging meeting points",
        "example_el": "Θέλεις να πάμε μαζί στη συναυλία του αγαπημένου μας συγκροτήματος;",
        "example_en": "Do you want us to go together to the concert of our favorite band?",
        "example2_el": "Η συναυλία δόθηκε στο Ηρώδειο κάτω από τη φωτισμένη Ακρόπολη.",
        "example2_en": "The concert took place at the Odeon of Herodes Atticus beneath the illuminated Acropolis."
    },
    {
        "id": "A2-U11-005",
        "greek": "η ταινία",
        "english": "movie / film",
        "notes": "Feminine noun in -α (-ες). Collocates with 'βλέπω ταινία' and film genres ('κωμωδία, δράμα').",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ταινίες",
            "collocation": "ελληνική ταινία, θερινός κινηματογράφος"
        },
        "keg_communicative_function": "Expressing film preferences and recommending movies in candidate dialogues",
        "example_el": "Είδαμε μια πολύ συγκινητική ταινία στον θερινό κινηματογράφο της γειτονιάς.",
        "example_en": "We saw a very moving movie at the neighborhood's open-air cinema.",
        "example2_el": "Η νέα ταινία του σκηνοθέτη κέρδισε το πρώτο βραβείο στο φεστιβάλ.",
        "example2_en": "The director's new movie won first prize at the festival."
    },
    {
        "id": "A2-U11-006",
        "greek": "ο ηθοποιός",
        "english": "actor / actress",
        "notes": "Masculine / feminine noun (ο/η ηθοποιός). Compound: ήθος (character) + ποιώ (to create).",
        "gender_or_pos": "noun (common gender)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "plural": "οι ηθοποιοί",
            "genitive_singular": "του/της ηθοποιού"
        },
        "keg_communicative_function": "Commenting on acting performances in theater and cinema reviews",
        "example_el": "Οι ηθοποιοί ερμήνευσαν τους ρόλους τους με εξαιρετική πειστικότητα.",
        "example_en": "The actors performed their roles with extraordinary conviction.",
        "example2_el": "Είναι ένας από τους πιο ταλαντούχους νέους ηθοποιούς του ελληνικού θεάτρου.",
        "example2_en": "He is one of the most talented young actors in Greek theater."
    },
    {
        "id": "A2-U11-007",
        "greek": "ο σκηνοθέτης",
        "english": "director (film / theater)",
        "notes": "Masculine noun in -ης (-ες). Feminine: 'η σκηνοθέτιδα'.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι σκηνοθέτες",
            "feminine": "η σκηνοθέτιδα",
            "noun_activity": "η σκηνοθεσία"
        },
        "keg_communicative_function": "Identifying film and stage creators in cultural articles",
        "example_el": "Ο διάσημος σκηνοθέτης έδωσε συνέντευξη τύπου για τη νέα του ταινία.",
        "example_en": "The famous director gave a press conference about his new film.",
        "example2_el": "Η σκηνοθεσία της παράστασης ήταν πρωτοποριακή και εντυπωσιακή.",
        "example2_en": "The staging of the performance was innovative and impressive."
    },
    {
        "id": "A2-U11-008",
        "greek": "η κριτική",
        "english": "review / critique",
        "notes": "Feminine noun in -ή (-ές). Collocates with 'γράφω κριτική' or 'θετική / αρνητική κριτική'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι κριτικές",
            "collocation": "θετική κριτική (positive review)"
        },
        "keg_communicative_function": "Reading cultural reviews to choose books, films, or plays",
        "example_el": "Το βιβλίο απέσπασε διθυραμβικές κριτικές από τους ειδικούς της λογοτεχνίας.",
        "example_en": "The book received rave reviews from literature experts.",
        "example2_el": "Διάβασα μια ενδιαφέρουσα κριτική για την έκθεση στην εφημερίδα.",
        "example2_en": "I read an interesting review about the exhibition in the newspaper."
    },
    {
        "id": "A2-U11-009",
        "greek": "το φεστιβάλ",
        "english": "festival",
        "notes": "Neuter indeclinable noun. Examples: Φεστιβάλ Αθηνών, Φεστιβάλ Κινηματογράφου Θεσσαλονίκης.",
        "gender_or_pos": "noun (neuter indeclinable)",
        "grammatical_info": {
            "part_of_speech": "noun (indeclinable)",
            "plural": "τα φεστιβάλ"
        },
        "keg_communicative_function": "Participating in seasonal arts, music, and film festivals",
        "example_el": "Κάθε Νοέμβριο διεξάγεται το Διεθνές Φεστιβάλ Κινηματογράφου στη Θεσσαλονίκη.",
        "example_en": "Every November the International Film Festival takes place in Thessaloniki.",
        "example2_el": "Το καλοκαιρινό φεστιβάλ περιλαμβάνει συναυλίες και παραστάσεις χορού.",
        "example2_en": "The summer festival includes concerts and dance performances."
    },
    {
        "id": "A2-U11-010",
        "greek": "η έκθεση",
        "english": "exhibition / essay",
        "notes": "Feminine noun in -η (-εις). Means both art exhibition ('έκθεση ζωγραφικής') and essay/composition.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι εκθέσεις",
            "genitive_singular": "της έκθεσης",
            "verb": "εκθέτω"
        },
        "keg_communicative_function": "Visiting art and museum exhibitions; writing test compositions",
        "example_el": "Επισκεφτήκαμε μια φωτογραφική έκθεση αφιερωμένη στα ελληνικά νησιά.",
        "example_en": "We visited a photography exhibition dedicated to the Greek islands.",
        "example2_el": "Στην έκθεση ιδεών πρέπει να αναπτύξετε τα επιχειρήματά σας με σαφήνεια.",
        "example2_en": "In the essay composition you must develop your arguments with clarity."
    },
    {
        "id": "A2-U11-011",
        "greek": "τα ΜΜΕ",
        "english": "mass media (press, TV, radio, digital)",
        "notes": "Neuter plural acronym: Μέσα Μαζικής Ενημέρωσης. Pronounced 'μι-μι-έ'.",
        "gender_or_pos": "noun phrase (neuter acronym)",
        "grammatical_info": {
            "part_of_speech": "noun phrase (acronym)",
            "full_form": "Μέσα Μαζικής Ενημέρωσης"
        },
        "keg_communicative_function": "Discussing the role of news, television, and journalism in modern life",
        "example_el": "Τα ΜΜΕ διαδραματίζουν καθοριστικό ρόλο στην ενημέρωση των πολιτών.",
        "example_en": "The mass media play a decisive role in informing citizens.",
        "example2_el": "Πολλά παραδοσιακά ΜΜΕ στρέφονται πλέον στις ψηφιακές πλατφόρμες.",
        "example2_en": "Many traditional media outlets are now turning to digital platforms."
    },
    {
        "id": "A2-U11-012",
        "greek": "η είδηση",
        "english": "news item / piece of news",
        "notes": "Feminine noun in -η (-εις). Plural 'οι ειδήσεις' means the news broadcast or headlines.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ειδήσεις",
            "collocation": "δελτίο ειδήσεων (news bulletin)"
        },
        "keg_communicative_function": "Following television news broadcasts and discussing daily headlines",
        "example_el": "Ακούσατε τις ειδήσεις των οκτώ στην τηλεόραση;",
        "example_en": "Did you listen to the eight o'clock news on television?",
        "example2_el": "Η ευχάριστη είδηση μεταδόθηκε γρήγορα σε όλη τη χώρα.",
        "example2_en": "The pleasant news was broadcast quickly across the country."
    },
    {
        "id": "A2-U11-013",
        "greek": "η εφημερίδα",
        "english": "newspaper",
        "notes": "Feminine noun in -α (-ες). Relates to 'ο εφημεριδοπώλης' (newsagent) and 'το περίπτερο'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι εφημερίδες",
            "genitive_singular": "της εφημερίδας"
        },
        "keg_communicative_function": "Reading authentic newspaper headlines and articles in Reading Part 2",
        "example_el": "Αγοράζω καθημερινά την πρωινή εφημερίδα από το περίπτερο της γειτονιάς.",
        "example_en": "I buy the morning newspaper daily from the neighborhood kiosk.",
        "example2_el": "Το άρθρο δημοσιεύτηκε στο πρωτοσέλιδο της κυριακάτικης εφημερίδας.",
        "example2_en": "The article was published on the front page of the Sunday newspaper."
    },
    {
        "id": "A2-U11-014",
        "greek": "το διαδίκτυο",
        "english": "the internet",
        "notes": "Neuter compound noun: διά + δίκτυο (net). Prepositional: 'στο διαδίκτυο' (online/on the internet).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "genitive_singular": "του διαδικτύου",
            "synonym": "το ίντερνετ",
            "adjective": "διαδικτυακός, -ή, -ό"
        },
        "keg_communicative_function": "Discussing digital connectivity, online courses, and internet safety",
        "example_el": "Σήμερα μπορούμε να βρούμε αμέτρητες πληροφορίες και μαθήματα στο διαδίκτυο.",
        "example_en": "Today we can find countless pieces of information and lessons on the internet.",
        "example2_el": "Η διαδικτυακή επικοινωνία μάς επιτρέπει να μένουμε σε επαφή με φίλους στο εξωτερικό.",
        "example2_en": "Online communication allows us to stay in touch with friends abroad."
    },
    {
        "id": "A2-U11-015",
        "greek": "η ιστοσελίδα",
        "english": "webpage / website",
        "notes": "Feminine compound noun: ιστός (web) + σελίδα (page). Plural: 'οι ιστοσελίδες'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ιστοσελίδες",
            "synonym": "ο ιστότοπος"
        },
        "keg_communicative_function": "Navigating institutional web portals and checking online guidelines",
        "example_el": "Επισκεφτείτε την επίσημη ιστοσελίδα του Κέντρου Ελληνικής Γλώσσας για παλιά θέματα εξετάσεων.",
        "example_en": "Visit the official website of the Centre for the Greek Language for past exam papers.",
        "example2_el": "Η ιστοσελίδα ανανεώνεται τακτικά με νέες ανακοινώσεις και άρθρα.",
        "example2_en": "The website is updated regularly with new announcements and articles."
    },
    {
        "id": "A2-U11-016",
        "greek": "η εφαρμογή",
        "english": "mobile application / app / implementation",
        "notes": "Feminine noun in -η (-εις). Means both software mobile app and practical application.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι εφαρμογές",
            "collocation": "εφαρμογή για κινητά (mobile app)"
        },
        "keg_communicative_function": "Using language learning applications and mobile banking",
        "example_el": "Κατέβασα μια εξαιρετική εφαρμογή στο κινητό μου για την εκμάθηση ελληνικού λεξιλογίου.",
        "example_en": "I downloaded an excellent app on my mobile phone for learning Greek vocabulary.",
        "example2_el": "Μπορείτε να πληρώσετε τον λογαριασμό εύκολα μέσω της τραπεζικής εφαρμογής.",
        "example2_en": "You can pay the bill easily via the banking application."
    },
    {
        "id": "A2-U11-017",
        "greek": "το μέσο κοινωνικής δικτύωσης",
        "english": "social media platform",
        "notes": "Neuter noun phrase. Often in plural: 'τα μέσα κοινωνικής δικτύωσης' (social networks).",
        "gender_or_pos": "noun phrase (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "plural": "τα μέσα κοινωνικής δικτύωσης",
            "abbreviation": "social media"
        },
        "keg_communicative_function": "Debating advantages and disadvantages of social networks in Speaking Stage 3",
        "example_el": "Τα μέσα κοινωνικής δικτύωσης διευκολύνουν την επικοινωνία, αλλά απαιτούν προσοχή.",
        "example_en": "Social media facilitate communication, but require caution.",
        "example2_el": "Πολλοί νέοι περνούν αρκετές ώρες την ημέρα στα μέσα κοινωνικής δικτύωσης.",
        "example2_en": "Many young people spend several hours a day on social media."
    },
    {
        "id": "A2-U11-018",
        "greek": "ο χρήστης",
        "english": "user (computer / internet / transport)",
        "notes": "Masculine noun in -ης (-ες). Relates to 'χρησιμοποιώ' (to use).",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι χρήστες",
            "feminine": "η χρήστης / χρήστρια",
            "collocation": "όνομα χρήστη (username)"
        },
        "keg_communicative_function": "Logging into digital portals and handling authentication details",
        "example_el": "Πληκτρολογήστε το όνομα χρήστη και τον κωδικό πρόσβασης για να συνδεθείτε.",
        "example_en": "Type your username and password to log in.",
        "example2_el": "Η πλατφόρμα έχει πάνω από ένα εκατομμύριο ενεργούς χρήστες.",
        "example2_en": "The platform has over one million active users."
    },
    {
        "id": "A2-U11-019",
        "greek": "το λάθος",
        "english": "mistake / error",
        "notes": "Neuter noun in -ος (-η). Genitive singular: 'του λάθους', plural: 'τα λάθη', genitive plural: 'των λαθών'. Core A2 grammar milestone.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα λάθη",
            "genitive_singular": "του λάθους",
            "genitive_plural": "των λαθών",
            "collocation": "κάνω λάθος (to make a mistake)"
        },
        "keg_communicative_function": "Recognizing and correcting language errors; apologising for misunderstandings",
        "example_el": "Μη φοβάστε να κάνετε λάθη όταν μιλάτε, από τα λάθη μαθαίνουμε.",
        "example_en": "Do not be afraid to make mistakes when you speak; from mistakes we learn.",
        "example2_el": "Διόρθωσε όλα τα ορθογραφικά λάθη πριν παραδώσει το γραπτό του.",
        "example2_en": "He corrected all spelling mistakes before submitting his paper."
    },
    {
        "id": "A2-U11-020",
        "greek": "το μέρος",
        "english": "place / part",
        "notes": "Neuter noun in -ος (-η). Genitive: 'του μέρους', plural: 'τα μέρη'. 'Από το ένα μέρος... από το άλλο μέρος' (on one part... on the other).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μέρη",
            "genitive_singular": "του μέρους",
            "genitive_plural": "των μερών"
        },
        "keg_communicative_function": "Describing geographical locations and structural parts of an exam",
        "example_el": "Η εξέταση χωρίζεται σε τέσσερα ισότιμα μέρη: κατανόηση και παραγωγή λόγου.",
        "example_en": "The examination is divided into four equal parts: comprehension and production of speech.",
        "example2_el": "Η Ελλάδα είναι γεμάτη μαγευτικά μέρη που αξίζει να ανακαλύψετε.",
        "example2_en": "Greece is full of enchanting places that are worth discovering."
    },
    {
        "id": "A2-U11-021",
        "greek": "το κόστος",
        "english": "cost / expense",
        "notes": "Neuter noun in -ος. Genitive: 'του κόστους'. Collocates with 'κόστος ζωής' (cost of living).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "genitive_singular": "του κόστους",
            "collocation": "κόστος συμμετοχής (participation fee)"
        },
        "keg_communicative_function": "Inquiring about program fees, living costs, and travel budgets",
        "example_el": "Το συνολικό κόστος των εξετάσεων περιλαμβάνει τη συμμετοχή και το πιστοποιητικό.",
        "example_en": "The total cost of examinations includes participation and the certificate.",
        "example2_el": "Το κόστος ζωής στην επαρχία είναι αισθητά χαμηλότερο από ό,τι στην πρωτεύουσα.",
        "example2_en": "The cost of living in the provinces is noticeably lower than in the capital."
    },
    {
        "id": "A2-U11-022",
        "greek": "το είδος",
        "english": "type / kind / genre",
        "notes": "Neuter noun in -ος (-η). Genitive: 'του είδους', plural: 'τα είδη'. Plural 'είδη' also means goods/articles.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα είδη",
            "genitive_singular": "του είδους",
            "collocation": "είδη πρώτης ανάγκης (basic necessities)"
        },
        "keg_communicative_function": "Categorizing text genres, musical types, and consumer commodities",
        "example_el": "Ποιο είδος μουσικής προτιμάτε να ακούτε όταν χαλαρώνετε;",
        "example_en": "What kind of music do you prefer to listen to when relaxing?",
        "example2_el": "Στο σούπερ μάρκετ θα βρείτε όλα τα απαραίτητα είδη διατροφής.",
        "example2_en": "At the supermarket you will find all necessary food items."
    },
    {
        "id": "A2-U11-023",
        "greek": "το μέγεθος",
        "english": "size / magnitude",
        "notes": "Neuter noun in -ος (-η). Genitive: 'του μεγέθους', plural: 'τα μεγέθη'. Used for clothing, files, or dimensions.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μεγέθη",
            "genitive_singular": "του μεγέθους"
        },
        "keg_communicative_function": "Specifying clothing sizes in shopping or digital attachment sizes in emails",
        "example_el": "Έχετε αυτό το πουκάμισο σε μεγαλύτερο μέγεθος;",
        "example_en": "Do you have this shirt in a larger size?",
        "example2_el": "Το μέγεθος του αρχείου δεν πρέπει να υπερβαίνει τα δέκα megabytes.",
        "example2_en": "The file size must not exceed ten megabytes."
    },
    {
        "id": "A2-U11-024",
        "greek": "το κράτος",
        "english": "state / nation-state / government",
        "notes": "Neuter noun in -ος (-η). Genitive: 'του κράτους', plural: 'τα κράτη'. Adjective: 'κρατικός' (state/public).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κράτη",
            "genitive_singular": "του κράτους",
            "adjective": "κρατικός, -ή, -ό"
        },
        "keg_communicative_function": "Discussing European states, public services, and governmental regulations",
        "example_el": "Το ελληνικό κράτος χορηγεί υποτροφίες σε ξένους φοιτητές για εκμάθηση της γλώσσας.",
        "example_en": "The Greek state awards scholarships to foreign students for learning the language.",
        "example2_el": "Η Ελλάδα είναι μέλος της Ευρωπαϊκής Ένωσης και του χώρου Σένγκεν.",
        "example2_en": "Greece is a member of the European Union and the Schengen area."
    },
    {
        "id": "A2-U11-025",
        "greek": "που",
        "english": "who / which / that (invariable relative pronoun)",
        "notes": "Invariable relative pronoun (unaccented). Refers to persons or things regardless of gender, number, or case.",
        "gender_or_pos": "relative pronoun (invariable)",
        "grammatical_info": {
            "part_of_speech": "relative pronoun",
            "accentuation": "always unaccented (distinguish from interrogative πού;)",
            "agreement": "invariable"
        },
        "keg_communicative_function": "Linking clauses smoothly to describe people, objects, and places",
        "example_el": "Ο καθηγητής που μας διδάσκει ελληνικά είναι εξαιρετικά υπομονετικός.",
        "example_en": "The teacher who teaches us Greek is extremely patient.",
        "example2_el": "Αυτό είναι το βιβλίο που μου πρότεινες να διαβάσω.",
        "example2_en": "This is the book that you recommended I read."
    },
    {
        "id": "A2-U11-026",
        "greek": "ο οποίος",
        "english": "who / which (variable relative pronoun)",
        "notes": "Declinable relative pronoun (ο οποίος, η οποία, το οποίο / οι οποίοι, οι οποίες, τα οποία). Used for clarity and formal register.",
        "gender_or_pos": "relative pronoun (declinable)",
        "grammatical_info": {
            "part_of_speech": "relative pronoun",
            "feminine": "η οποία",
            "neuter": "το οποίο",
            "plural_masculine": "οι οποίοι",
            "plural_feminine": "οι οποίες",
            "plural_neuter": "τα οποία"
        },
        "keg_communicative_function": "Formulating precise relative clauses in formal writing and exam compositions",
        "example_el": "Συναντήθηκα με τη διευθύντρια, η οποία μου εξήγησε τη διαδικασία της εγγραφής.",
        "example_en": "I met with the director, who explained to me the registration process.",
        "example2_el": "Τα πιστοποιητικά, τα οποία εκδίδονται στα ελληνικά, αναγνωρίζονται διεθνώς.",
        "example2_en": "The certificates, which are issued in Greek, are internationally recognized."
    },
    {
        "id": "A2-U11-027",
        "greek": "δημοσιεύω",
        "english": "to publish / to post online",
        "notes": "Active verb. Simple past: 'δημοσίευσα'. Used for articles, posts, and exam announcements.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "δημοσίευσα",
            "noun_derivative": "η δημοσίευση"
        },
        "keg_communicative_function": "Reporting published news, forum posts, or announcement of results",
        "example_el": "Τα τελικά αποτελέσματα των εξετάσεων θα δημοσιευτούν στο διαδίκτυο στα τέλη Ιουνίου.",
        "example_en": "The final results of the exams will be published online in late June.",
        "example2_el": "Δημοσίευσε ένα ενδιαφέρον σχόλιο στο ιστολόγιο της τάξης.",
        "example2_en": "She posted an interesting comment on the class blog."
    },
    {
        "id": "A2-U11-028",
        "greek": "η σύνδεση",
        "english": "connection / internet link / log-in",
        "notes": "Feminine noun in -η (-εις). Collocates with 'σύνδεση στο διαδίκτυο' (internet connection).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι συνδέσεις",
            "verb": "συνδέομαι (to log in / connect)"
        },
        "keg_communicative_function": "Resolving network connectivity problems and logging into exam platforms",
        "example_el": "Η ασύρματη σύνδεση στο διαδίκτυο είναι γρήγορη και σταθερή σε όλο το κτίριο.",
        "example_en": "The wireless internet connection is fast and stable throughout the building.",
        "example2_el": "Πραγματοποιήστε σύνδεση στον λογαριασμό σας για να δείτε τη βαθμολογία σας.",
        "example2_en": "Log in to your account to view your grades."
    },
    {
        "id": "A2-U11-029",
        "greek": "κατεβάζω",
        "english": "to download / to bring down",
        "notes": "Active verb. Simple past: 'κατέβασα'. Compound: κάτω + βάζω. Antonym: 'ανεβάζω' (to upload).",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "κατέβασα",
            "antonym": "ανεβάζω (to upload)"
        },
        "keg_communicative_function": "Downloading practice exam files, audio samples, or application forms",
        "example_el": "Κατέβασα τα υποδειγματικά θέματα των εξετάσεων στον υπολογιστή μου για εξάσκηση.",
        "example_en": "I downloaded the sample exam papers onto my computer for practice.",
        "example2_el": "Μπορείτε να κατεβάσετε την εφαρμογή δωρεάν από το ηλεκτρονικό κατάστημα.",
        "example2_en": "You can download the app for free from the app store."
    },
    {
        "id": "A2-U11-030",
        "greek": "ανεβάζω",
        "english": "to upload / to stage a play / to raise",
        "notes": "Active verb. Simple past: 'ανέβασα'. Antonym: 'κατεβάζω'. Multiple uses: upload files or stage a performance.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "ανέβασα",
            "antonym": "κατεβάζω"
        },
        "keg_communicative_function": "Uploading documents to official portals or sharing photos",
        "example_el": "Ανέβασα όλα τα δικαιολογητικά στην πλατφόρμα των αιτήσεων σε μορφή PDF.",
        "example_en": "I uploaded all supporting documents onto the application platform in PDF format.",
        "example2_el": "Η θεατρική ομάδα ανέβασε μια κλασική ελληνική κωμωδία.",
        "example2_en": "The theater troupe staged a classic Greek comedy."
    },
    {
        "id": "A2-U11-031",
        "greek": "ο υπολογιστής",
        "english": "computer",
        "notes": "Masculine noun in -ής (-ές). Collocates with 'φορητός υπολογιστής' (laptop).",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι υπολογιστές",
            "collocation": "φορητός υπολογιστής (laptop)"
        },
        "keg_communicative_function": "Discussing computer literacy and digital tools in education",
        "example_el": "Χρησιμοποιώ τον φορητό υπολογιστή καθημερινά για τη μελέτη και την εργασία μου.",
        "example_en": "I use the laptop computer daily for my study and work.",
        "example2_el": "Η εξέταση πραγματοποιείται σε αίθουσα υπολογιστών με σύγχρονο εξοπλισμό.",
        "example2_en": "The examination takes place in a computer lab with modern equipment."
    },
    {
        "id": "A2-U11-032",
        "greek": "το κινητό τηλέφωνο",
        "english": "mobile phone / smartphone",
        "notes": "Neuter noun phrase. Often simply called 'το κινητό'. Key exam rule: must be switched off.",
        "gender_or_pos": "noun phrase (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "plural": "τα κινητά τηλέφωνα",
            "short_form": "το κινητό"
        },
        "keg_communicative_function": "Observing test instructions regarding electronic mobile devices",
        "example_el": "Απενεργοποιήστε τα κινητά σας τηλέφωνα πριν εισέλθετε στον χώρο της εξέτασης.",
        "example_en": "Turn off your mobile phones before entering the examination area.",
        "example2_el": "Μου έστειλε μήνυμα στο κινητό για να επιβεβαιώσει το απογευματινό μας ραντεβού.",
        "example2_en": "He sent me a text on the mobile phone to confirm our afternoon appointment."
    },
    {
        "id": "A2-U11-033",
        "greek": "το μήνυμα",
        "english": "message / text message",
        "notes": "Neuter noun in -μα (-ματα). Plural: 'τα μηνύματα'. SMS: γραπτό μήνυμα.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μηνύματα",
            "collocation": "στέλνω μήνυμα (to send a text)"
        },
        "keg_communicative_function": "Reading and writing short communicative messages in Writing Task 1",
        "example_el": "Σου άφησα ένα φωνητικό μήνυμα επειδή δεν απάντησες στο τηλέφωνο.",
        "example_en": "I left you a voice message because you did not answer the phone.",
        "example2_el": "Έλαβα ένα ενημερωτικό μήνυμα σχετικά με την αλλαγή της ώρας του μαθήματος.",
        "example2_en": "I received an informative text message regarding the change in class time."
    },
    {
        "id": "A2-U11-034",
        "greek": "το περιοδικό",
        "english": "magazine / journal",
        "notes": "Neuter noun in -ό (-ά). Plural: 'τα περιοδικά'. Source of authentic short articles in tests.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα περιοδικά",
            "genitive_singular": "του περιοδικού"
        },
        "keg_communicative_function": "Comprehending lifestyle and cultural articles from Greek magazines",
        "example_el": "Διάβασα μια πολύ ενδιαφέρουσα συνέντευξη σε ένα εβδομαδιαίο περιοδικό.",
        "example_en": "I read a very interesting interview in a weekly magazine.",
        "example2_el": "Το περιοδικό δημοσιεύει άρθρα για τη διατροφή, την υγεία και τα ταξίδια.",
        "example2_en": "The magazine publishes articles about nutrition, health, and travel."
    },
    {
        "id": "A2-U11-035",
        "greek": "η οθόνη",
        "english": "screen / display",
        "notes": "Feminine noun in -η (-ες). Used for cinema screen, computer monitor, or phone display.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι οθόνες",
            "genitive_singular": "της οθόνης"
        },
        "keg_communicative_function": "Following electronic departure boards and digital display monitors",
        "example_el": "Κοιτάξτε την οθόνη για να δείτε ποιος αριθμός εξυπηρετείται αυτή τη στιγμή.",
        "example_en": "Look at the screen to see which number is being served right now.",
        "example2_el": "Η οθόνη αφής διευκολύνει την πλοήγηση στην εφαρμογή.",
        "example2_en": "The touchscreen facilitates navigation in the application."
    }
]

# -------------------------------------------------------------
# UNIT A2-12 CARDS (35 cards)
# Theme: Exam Workshop & Simulation (Εξεταστικό Εργαστήριο & Προσομοίωση)
# -------------------------------------------------------------
CARDS_U12 = [
    {
        "id": "A2-U12-001",
        "greek": "επομένως",
        "english": "therefore / consequently",
        "notes": "Formal cohesive conjunction/adverb. Marks logical deduction. Elevates candidate writing in Task 2.",
        "gender_or_pos": "conjunction / adverb",
        "grammatical_info": {
            "part_of_speech": "cohesive conjunction",
            "synonym": "άρα, συνεπώς"
        },
        "keg_communicative_function": "Drawing conclusions and connecting arguments in written compositions",
        "example_el": "Έχουμε ολοκληρώσει όλη την ύλη, επομένως είμαστε έτοιμοι για τις εξετάσεις.",
        "example_en": "We have completed all the material; therefore, we are ready for the exams.",
        "example2_el": "Δεν υπάρχουν άλλα διαθέσιμα εισιτήρια, επομένως πρέπει να αλλάξουμε ημερομηνία.",
        "example2_en": "There are no other tickets available; consequently, we must change date."
    },
    {
        "id": "A2-U12-002",
        "greek": "ωστόσο",
        "english": "however / nevertheless / yet",
        "notes": "Adversative connector. Contrasts two balanced propositions in argumentative speech and writing.",
        "gender_or_pos": "conjunction / adverb",
        "grammatical_info": {
            "part_of_speech": "adversative conjunction",
            "synonym": "όμως, παρ' όλα αυτά"
        },
        "keg_communicative_function": "Introducing counter-arguments and nuanced qualifications in essays and debates",
        "example_el": "Η δοκιμασία ήταν απαιτητική, ωστόσο όλοι οι υποψήφιοι κατέβαλαν μεγάλη προσπάθεια.",
        "example_en": "The test was demanding; however, all candidates made a great effort.",
        "example2_el": "Ο καιρός ήταν βροχερός, ωστόσο η συναυλία πραγματοποιήθηκε κανονικά.",
        "example2_en": "The weather was rainy; nevertheless, the concert took place as scheduled."
    },
    {
        "id": "A2-U12-003",
        "greek": "εξάλλου",
        "english": "besides / moreover / after all",
        "notes": "Additive connective adverb. Reinforces a previous point with additional justification.",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "connector",
            "synonym": "άλλωστε, επιπλέον"
        },
        "keg_communicative_function": "Adding persuasive points during candidate discussions (Speaking Stage 3)",
        "example_el": "Προτείνω να πάμε με το μετρό, εξάλλου είναι πολύ πιο γρήγορο και οικονομικό.",
        "example_en": "I suggest we go by metro; besides, it is much faster and more economical.",
        "example2_el": "Δεν χρειάζεται να ανησυχείτε, εξάλλου έχετε προετοιμαστεί εξαιρετικά.",
        "example2_en": "There is no need to worry; after all, you have prepared extraordinarily well."
    },
    {
        "id": "A2-U12-004",
        "greek": "επιπλέον",
        "english": "furthermore / in addition",
        "notes": "Additive adverb. Used to introduce supplementary arguments in structured paragraphs.",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "connector",
            "synonym": "επιπροσθέτως, επίσης"
        },
        "keg_communicative_function": "Expanding essays with secondary supporting reasons in Writing Task 2",
        "example_el": "Το ξενοδοχείο είναι κεντρικό και, επιπλέον, προσφέρει δωρεάν χώρο στάθμευσης.",
        "example_en": "The hotel is central and, in addition, offers free parking space.",
        "example2_el": "Επιπλέον, η εκμάθηση μιας ξένης γλώσσας ανοίγει νέους επαγγελματικούς ορίζοντες.",
        "example2_en": "Furthermore, learning a foreign language opens new professional horizons."
    },
    {
        "id": "A2-U12-005",
        "greek": "κατά τη γνώμη μου",
        "english": "in my opinion",
        "notes": "Fixed prepositional formula. Essential for stating personal viewpoints in oral and written tasks.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "synonym": "κατά την άποψή μου, πιστεύω ότι"
        },
        "keg_communicative_function": "Expressing stance and personal perspective during examiner questioning",
        "example_el": "Κατά τη γνώμη μου, η συνεχής εξάσκηση είναι το κλειδί για την κατάκτηση της γλώσσας.",
        "example_en": "In my opinion, continuous practice is the key to mastering the language.",
        "example2_el": "Κατά τη γνώμη μου, η δεύτερη επιλογή είναι σαφώς πιο συμφέρουσα.",
        "example2_en": "In my opinion, the second option is clearly more advantageous."
    },
    {
        "id": "A2-U12-006",
        "greek": "συμφωνώ απόλυτα",
        "english": "I completely agree",
        "notes": "Verbal collocation. Core communicative move in candidate pair interactions (Stage 3).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "συμφωνώ",
            "antonym": "διαφωνώ"
        },
        "keg_communicative_function": "Validating candidate peer proposals enthusiastically during joint problem-solving",
        "example_el": "Συμφωνώ απόλυτα μαζί σου, αυτή είναι η καλύτερη λύση για το πρόβλημα.",
        "example_en": "I completely agree with you; that is the best solution to the problem.",
        "example2_el": "Συμφωνώ απόλυτα με την άποψη ότι η προστασία του περιβάλλοντος προέχει.",
        "example2_en": "I completely agree with the view that environmental protection takes precedence."
    },
    {
        "id": "A2-U12-007",
        "greek": "διαφωνώ",
        "english": "to disagree / I disagree",
        "notes": "Contracted verb (διαφωνώ, διαφωνείς). Followed by 'με + accusative' (I disagree with).",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "antonym": "συμφωνώ",
            "noun_derivative": "η διαφωνία"
        },
        "keg_communicative_function": "Expressing polite dissent and offering alternative ideas in candidate debates",
        "example_el": "Διαφωνώ ευγενικά με αυτή την πρόταση επειδή το κόστος είναι υπερβολικά υψηλό.",
        "example_en": "I politely disagree with this proposal because the cost is excessively high.",
        "example2_el": "Δεν διαφωνώ με την ιδέα, αλλά θεωρώ ότι χρειάζεται περισσότερος χρόνος.",
        "example2_en": "I do not disagree with the idea, but I consider that more time is needed."
    },
    {
        "id": "A2-U12-008",
        "greek": "από τη μία πλευρά",
        "english": "on the one hand",
        "notes": "Correlative discourse formula. Pairs with 'από την άλλη πλευρά' (on the other hand).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "discourse connector",
            "correlative_pair": "από τη μία... από την άλλη..."
        },
        "keg_communicative_function": "Balancing pros and cons in written essays and spoken debates",
        "example_el": "Από τη μία πλευρά η ζωή στην πόλη προσφέρει ευκαιρίες, από την άλλη όμως έχει πολύ άγχος.",
        "example_en": "On the one hand city life offers opportunities, but on the other it has much stress.",
        "example2_el": "Από τη μία πλευρά κατανοώ τη δυσκολία, από την άλλη όμως πρέπει να προσπαθήσουμε.",
        "example2_en": "On the one hand I understand the difficulty, but on the other we must try."
    },
    {
        "id": "A2-U12-009",
        "greek": "από την άλλη πλευρά",
        "english": "on the other hand",
        "notes": "Correlative discourse formula pairing with 'από τη μία πλευρά'.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "discourse connector",
            "correlative_pair": "από τη μία πλευρά..."
        },
        "keg_communicative_function": "Introducing the opposing perspective in structured argumentative texts",
        "example_el": "Από την άλλη πλευρά, το διαδίκτυο κρύβει κινδύνους που δεν πρέπει να αγνοούμε.",
        "example_en": "On the other hand, the internet conceals risks that we must not ignore.",
        "example2_el": "Από την άλλη πλευρά, η επαρχία προσφέρει πολύ καλύτερη ποιότητα ζωής.",
        "example2_en": "On the other hand, the countryside offers a much better quality of life."
    },
    {
        "id": "A2-U12-010",
        "greek": "για παράδειγμα",
        "english": "for example / for instance",
        "notes": "Exemplifying phrase. Often abbreviated as 'π.χ.' (παραδείγματος χάριν).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "abbreviation": "π.χ."
        },
        "keg_communicative_function": "Illustrating general statements with concrete evidence in compositions",
        "example_el": "Στην Ελλάδα υπάρχουν πολλά όμορφα νησιά, για παράδειγμα η Νάξος και η Μήλος.",
        "example_en": "In Greece there are many beautiful islands, for example Naxos and Milos.",
        "example2_el": "Μπορείτε να εξασκηθείτε με διάφορους τρόπους, για παράδειγμα βλέποντας ελληνικές σειρές.",
        "example2_en": "You can practice in various ways, for instance by watching Greek series."
    },
    {
        "id": "A2-U12-011",
        "greek": "δηλαδή",
        "english": "that is to say / namely / in other words",
        "notes": "Clarifying connector. Used to explain, rephrase, or specify meaning.",
        "gender_or_pos": "conjunction / adverb",
        "grammatical_info": {
            "part_of_speech": "connector",
            "usage": "clarification or reformulation"
        },
        "keg_communicative_function": "Reformulating thoughts and clarifying statements when speaking to examiners",
        "example_el": "Το μάθημα είναι καθημερινό, δηλαδή από Δευτέρα έως και Παρασκευή.",
        "example_en": "The course is daily, that is to say from Monday through Friday.",
        "example2_el": "Πρέπει να πετύχετε εξήντα τοις εκατό, δηλαδή τουλάχιστον δώδεκα στα είκοσι.",
        "example2_en": "You must achieve sixty percent, in other words at least twelve out of twenty."
    },
    {
        "id": "A2-U12-012",
        "greek": "πρώτον",
        "english": "firstly / in the first place",
        "notes": "Ordinal discourse connector. Pairs with 'δεύτερον' (secondly) and 'τέλος' (finally).",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "ordinal connector",
            "sequence": "πρώτον -> δεύτερον -> τρίτον -> τέλος"
        },
        "keg_communicative_function": "Structuring multi-point arguments sequentially in essays and oral presentations",
        "example_el": "Πρώτον, πρέπει να διαβάσουμε προσεκτικά όλες τις ερωτήσεις του φυλλαδίου.",
        "example_en": "Firstly, we must carefully read all the questions in the booklet.",
        "example2_el": "Πρώτον, η τιμή είναι πολύ προσιτή και, δεύτερον, η ποιότητα είναι άριστη.",
        "example2_en": "Firstly, the price is very affordable and, secondly, the quality is excellent."
    },
    {
        "id": "A2-U12-013",
        "greek": "δεύτερον",
        "english": "secondly",
        "notes": "Ordinal discourse connector following 'πρώτον'.",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "ordinal connector",
            "sequence": "πρώτον -> δεύτερον"
        },
        "keg_communicative_function": "Adding the second point in a structured oral or written argument",
        "example_el": "Δεύτερον, έχουμε αρκετό χρόνο για να οργανώσουμε την εκδρομή μας.",
        "example_en": "Secondly, we have enough time to organize our excursion.",
        "example2_el": "Δεύτερον, η τοποθεσία του ξενοδοχείου είναι εξαιρετικά βολική για τις μετακινήσεις μας.",
        "example2_en": "Secondly, the hotel's location is extremely convenient for our travels."
    },
    {
        "id": "A2-U12-014",
        "greek": "τελικά",
        "english": "finally / in the end / after all",
        "notes": "Adverb of time and discourse conclusion. Indicates final outcome.",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "adverb",
            "synonym": "στο τέλος, εν τέλει"
        },
        "keg_communicative_function": "Concluding narratives and describing the final resolution of an event",
        "example_el": "Τελικά καταφέραμε να φτάσουμε στον προορισμό μας πριν πέσει η νύχτα.",
        "example_en": "In the end we managed to arrive at our destination before night fell.",
        "example2_el": "Τελικά ποια απόφαση πήρατε για τις καλοκαιρινές διακοπές;",
        "example2_en": "In the end what decision did you make regarding the summer vacation?"
    },
    {
        "id": "A2-U12-015",
        "greek": "συμπερασματικά",
        "english": "in conclusion / to sum up",
        "notes": "Discourse concluding adverb. Standard transitional marker for closing paragraphs.",
        "gender_or_pos": "adverb",
        "grammatical_info": {
            "part_of_speech": "concluding adverb",
            "noun": "το συμπέρασμα (conclusion)",
            "synonym": "εν κατακλείδι"
        },
        "keg_communicative_function": "Signaling the final concluding paragraph of written essays",
        "example_el": "Συμπερασματικά, η προετοιμασία και η ψυχραιμία εξασφαλίζουν την επιτυχία στις εξετάσεις.",
        "example_en": "In conclusion, preparation and composure ensure success in examinations.",
        "example2_el": "Συμπερασματικά, τα οφέλη του προγράμματος υπερτερούν σαφώς των δυσκολιών.",
        "example2_en": "To sum up, the benefits of the program clearly outweigh the difficulties."
    },
    {
        "id": "A2-U12-016",
        "greek": "το πλεονέκτημα",
        "english": "advantage / asset",
        "notes": "Neuter noun in -μα (-ματα). Antonym: 'το μειονέκτημα' (disadvantage). Core argumentative pair.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πλεονεκτήματα",
            "antonym": "το μειονέκτημα"
        },
        "keg_communicative_function": "Comparing positive features of two competing options in Speaking Stage 3",
        "example_el": "Το βασικό πλεονέκτημα της δημόσιας συγκοινωνίας είναι το χαμηλό κόστος και η προστασία του περιβάλλοντος.",
        "example_en": "The main advantage of public transport is low cost and environmental protection.",
        "example2_el": "Ποια είναι τα πλεονεκτήματα της εργασίας από το σπίτι;",
        "example2_en": "What are the advantages of working from home?"
    },
    {
        "id": "A2-U12-017",
        "greek": "το μειονέκτημα",
        "english": "disadvantage / drawback",
        "notes": "Neuter noun in -μα (-ματα). Antonym: 'το πλεονέκτημα'.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μειονεκτήματα",
            "antonym": "το πλεονέκτημα"
        },
        "keg_communicative_function": "Pointing out drawbacks or limitations during candidate negotiations",
        "example_el": "Ένα σοβαρό μειονέκτημα του αυτοκινήτου στην πόλη είναι η δυσκολία εύρεσης στάθμευσης.",
        "example_en": "A serious disadvantage of the car in the city is the difficulty in finding parking.",
        "example2_el": "Πρέπει να εξετάσουμε τόσο τα πλεονεκτήματα όσο και τα μειονεκτήματα κάθε επιλογής.",
        "example2_en": "We must examine both the advantages and the disadvantages of each option."
    },
    {
        "id": "A2-U12-018",
        "greek": "η προσομοίωση",
        "english": "simulation / mock exam",
        "notes": "Feminine noun in -η (-εις). Verb: 'προσομοιώνω'. Essential pedagogical rehearsal.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι προσομοιώσεις",
            "collocation": "προσομοίωση εξετάσεων (mock exam)"
        },
        "keg_communicative_function": "Participating in timed practice mock tests under real exam conditions",
        "example_el": "Κάναμε μια πλήρη προσομοίωση της γραπτής εξέτασης με αυστηρή τήρηση του χρόνου.",
        "example_en": "We did a full simulation of the written examination with strict adherence to time.",
        "example2_el": "Η προσομοίωση βοηθά τους υποψηφίους να αποβάλουν το περιττό άγχος.",
        "example2_en": "Simulation helps candidates eliminate unnecessary stress."
    },
    {
        "id": "A2-U12-019",
        "greek": "ο υποψήφιος",
        "english": "candidate / examinee",
        "notes": "Masculine noun in -ος (-οι). Feminine: 'η υποψήφια'.",
        "gender_or_pos": "noun (masculine / feminine)",
        "grammatical_info": {
            "part_of_speech": "noun",
            "feminine": "η υποψήφια",
            "plural": "οι υποψήφιοι",
            "genitive_singular": "του υποψηφίου"
        },
        "keg_communicative_function": "Identifying test candidates and understanding examinee rights and duties",
        "example_el": "Κάθε υποψήφιος λαμβάνει ένα ατομικό δελτίο με τον κωδικό αριθμό του.",
        "example_en": "Each candidate receives an individual card with his/her identification code.",
        "example2_el": "Οι υποψήφιοι εξετάζονται ανά ζεύγη στην παραγωγή προφορικού λόγου.",
        "example2_en": "Candidates are examined in pairs in oral speech production."
    },
    {
        "id": "A2-U12-020",
        "greek": "ο εξεταστής",
        "english": "examiner",
        "notes": "Masculine noun in -ής (-ές). Feminine: 'η εξετάστρια'.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι εξεταστές",
            "feminine": "η εξετάστρια",
            "verb": "εξετάζω"
        },
        "keg_communicative_function": "Interacting respectfully with test evaluators during oral tests",
        "example_el": "Ο εξεταστής έκανε φιλικές ερωτήσεις για να βοηθήσει τους υποψηφίους να χαλαρώσουν.",
        "example_en": "The examiner asked friendly questions to help the candidates relax.",
        "example2_el": "Απευθυνθείτε στην εξετάστρια αν χρειάζεστε διευκρίνιση για την εκφώνηση.",
        "example2_en": "Address the examiner if you need clarification regarding the prompt."
    },
    {
        "id": "A2-U12-021",
        "greek": "η βαθμολογία",
        "english": "grading / scoring / marks",
        "notes": "Feminine noun in -α. Minimum passing mark: 60% per individual skill (12/20 marks).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "verb": "βαθμολογώ",
            "collocation": "τελική βαθμολογία (final score)"
        },
        "keg_communicative_function": "Understanding evaluation criteria and score thresholds",
        "example_el": "Η βάση για την απόκτηση του πιστοποιητικού είναι το εξήντα τοις εκατό σε κάθε δεξιότητα.",
        "example_en": "The threshold for obtaining the certificate is sixty percent in each skill.",
        "example2_el": "Πέτυχε υψηλή βαθμολογία στην κατανόηση προφορικού και γραπτού λόγου.",
        "example2_en": "She achieved a high score in oral and written comprehension."
    },
    {
        "id": "A2-U12-022",
        "greek": "η λύση",
        "english": "solution / resolution",
        "notes": "Feminine noun in -η (-εις). Verb: 'λύνω' (to solve). Collocates with 'βρίσκω λύση'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι λύσεις",
            "verb": "λύνω",
            "collocation": "προτείνω λύση (to propose a solution)"
        },
        "keg_communicative_function": "Proposing mutually agreeable solutions in pair role-plays (Speaking Stage 3)",
        "example_el": "Πρέπει να βρούμε μια κοινά αποδεκτή λύση που να εξυπηρετεί και τους δυο μας.",
        "example_en": "We must find a mutually acceptable solution that serves both of us.",
        "example2_el": "Αυτή η λύση είναι πρακτική, οικονομική και άμεσα εφαρμόσιμη.",
        "example2_en": "This solution is practical, economical, and immediately applicable."
    },
    {
        "id": "A2-U12-023",
        "greek": "το επιχείρημα",
        "english": "argument / reasoning point",
        "notes": "Neuter noun in -μα (-ματα). Essential in presenting and defending a viewpoint.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα επιχειρήματα",
            "collocation": "ισχυρό επιχείρημα (strong argument)"
        },
        "keg_communicative_function": "Supporting opinions with cogent arguments in oral tests and essays",
        "example_el": "Υποστήριξε την άποψή του με λογικά και πειστικά επιχειρήματα.",
        "example_en": "He supported his viewpoint with logical and persuasive arguments.",
        "example2_el": "Ποιο είναι το κύριο επιχείρημά σας υπέρ αυτής της επιλογής;",
        "example2_en": "What is your main argument in favor of this choice?"
    },
    {
        "id": "A2-U12-024",
        "greek": "κατά συνέπεια",
        "english": "as a result / consequently",
        "notes": "Formal cohesive phrase. Connects cause with resulting consequence.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "synonym": "επομένως, ως αποτέλεσμα"
        },
        "keg_communicative_function": "Linking causes to consequences in analytical reading and writing tasks",
        "example_el": "Δεν υπήρχαν διαθέσιμα δρομολόγια και, κατά συνέπεια, αναγκαστήκαμε να διανυκτερεύσουμε εκεί.",
        "example_en": "There were no available routes and, consequently, we were forced to spend the night there.",
        "example2_el": "Μελέτησε εντατικά όλη τη χρονιά και, κατά συνέπεια, πέρασε με άριστα.",
        "example2_en": "She studied intensively all year and, as a result, passed with distinction."
    },
    {
        "id": "A2-U12-025",
        "greek": "συνοψίζοντας",
        "english": "summarizing / in brief",
        "notes": "Present active participle of 'συνοψίζω'. Used formulaically at conclusion of oral monologue.",
        "gender_or_pos": "participle (discourse)",
        "grammatical_info": {
            "part_of_speech": "participle",
            "verb": "συνοψίζω (to summarize)"
        },
        "keg_communicative_function": "Summarizing personal thoughts before ending an oral response",
        "example_el": "Συνοψίζοντας, θεωρώ ότι η εκμάθηση της ελληνικής γλώσσας αποτελεί μια σπουδαία εμπειρία.",
        "example_en": "Summarizing, I consider that learning the Greek language constitutes a great experience.",
        "example2_el": "Συνοψίζοντας τα κύρια σημεία, καταλήγουμε στην ανάγκη άμεσης δράσης.",
        "example2_en": "Summarizing the main points, we conclude on the necessity for immediate action."
    },
    {
        "id": "A2-U12-026",
        "greek": "ο χρόνος εξέτασης",
        "english": "exam time / allotted duration",
        "notes": "Masculine noun phrase. Critical parameter for managing pace across test papers.",
        "gender_or_pos": "noun phrase (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "collocation": "διαχείριση χρόνου (time management)"
        },
        "keg_communicative_function": "Managing test pacing and respecting allotted section time limits",
        "example_el": "Η σωστή διαχείριση του χρόνου εξέτασης είναι κρίσιμη για να προλάβετε όλες τις ερωτήσεις.",
        "example_en": "Proper management of exam time is critical in order to get to all questions.",
        "example2_el": "Ο χρόνος εξέτασης για την παραγωγή γραπτού λόγου είναι σαράντα πέντε λεπτά.",
        "example2_en": "The exam time for written production is forty-five minutes."
    },
    {
        "id": "A2-U12-027",
        "greek": "η πιστοποίηση",
        "english": "certification / attainment credential",
        "notes": "Feminine noun in -η (-εις). Official term: 'Πιστοποίηση Επάρκειας της Ελληνομάθειας'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "verb": "πιστοποιώ",
            "collocation": "πιστοποίηση ελληνομάθειας"
        },
        "keg_communicative_function": "Discussing certification goals and official language credentials",
        "example_el": "Η πιστοποίηση επιπέδου Α2 αποτελεί πολύτιμο εφόδιο για την αγορά εργασίας στην Ελλάδα.",
        "example_en": "The level A2 certification constitutes a valuable asset for the job market in Greece.",
        "example2_el": "Ο φορέας πιστοποίησης ανακοίνωσε το επίσημο πρόγραμμα των εξετάσεων.",
        "example2_en": "The certification body announced the official exam schedule."
    },
    {
        "id": "A2-U12-028",
        "greek": "η στρατηγική",
        "english": "strategy / technique",
        "notes": "Feminine noun in -ή (-ές). Covers test-taking skills and preparation methods.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι στρατηγικές",
            "adjective": "στρατηγικός, -ή, -ό"
        },
        "keg_communicative_function": "Applying effective exam techniques (skimming, scanning, eliminating wrong options)",
        "example_el": "Μια καλή στρατηγική είναι να ξεκινήσετε από τις ασκήσεις που σας φαίνονται πιο εύκολες.",
        "example_en": "A good strategy is to begin from the exercises that appear easiest to you.",
        "example2_el": "Εφαρμόστε τις στρατηγικές κατανόησης που διδαχτήκατε στην τάξη.",
        "example2_en": "Apply the comprehension strategies that you were taught in class."
    },
    {
        "id": "A2-U12-029",
        "greek": "η προσοχή",
        "english": "attention / caution / care",
        "notes": "Feminine noun in -ή. Collocates with 'προσέχω' (to pay attention) or 'με προσοχή' (carefully).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "verb": "προσέχω",
            "collocation": "με μεγάλη προσοχή (with great care)"
        },
        "keg_communicative_function": "Focusing carefully on exam instructions, rubric details, and listening texts",
        "example_el": "Ακούστε το ηχητικό απόσπασμα με μεγάλη προσοχή κατά τη δεύτερη μετάδοση.",
        "example_en": "Listen to the audio excerpt with great attention during the second broadcast.",
        "example2_el": "Δώστε ιδιαίτερη προσοχή στην ορθογραφία και στα σημεία στίξης.",
        "example2_en": "Pay special attention to spelling and punctuation marks."
    },
    {
        "id": "A2-U12-030",
        "greek": "η ψυχραιμία",
        "english": "composure / calmness / presence of mind",
        "notes": "Feminine compound noun: ψυχρός (cool) + αίμα (blood). Collocates with 'διατηρώ την ψυχραιμία μου'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "adjective": "ψύχραιμος, -η, -ο",
            "collocation": "κρατάω την ψυχραιμία μου (to keep my cool)"
        },
        "keg_communicative_function": "Maintaining calm and confidence during testing conditions",
        "example_el": "Διατηρήστε την ψυχραιμία σας ακόμα κι αν συναντήσετε μια άγνωστη λέξη στο κείμενο.",
        "example_en": "Maintain your composure even if you encounter an unfamiliar word in the text.",
        "example2_el": "Η ψυχραιμία βοηθά στη συγκέντρωση και στην αποφυγή βιαστικών λαθών.",
        "example2_en": "Composure helps concentration and avoids hasty mistakes."
    },
    {
        "id": "A2-U12-031",
        "greek": "το επίτευγμα",
        "english": "achievement / accomplishment",
        "notes": "Neuter noun in -μα (-ματα). Relates to 'επιτυγχάνω' (to achieve/succeed).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα επιτεύγματα",
            "verb": "επιτυγχάνω"
        },
        "keg_communicative_function": "Celebrating the milestone of passing the Greek proficiency examination",
        "example_el": "Η απόκτηση του πιστοποιητικού Α2 είναι ένα σπουδαίο επίτευγμα για κάθε σπουδαστή.",
        "example_en": "Obtaining the A2 certificate is a great achievement for every student.",
        "example2_el": "Είμαστε υπερήφανοι για τα μαθησιακά επιτεύγματα όλων των υποψηφίων.",
        "example2_en": "We are proud of the learning achievements of all candidates."
    },
    {
        "id": "A2-U12-032",
        "greek": "η αυτοπεποίθηση",
        "english": "self-confidence",
        "notes": "Feminine compound noun: αυτός + πεποίθηση (conviction/trust).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "collocation": "με αυτοπεποίθηση (with confidence)"
        },
        "keg_communicative_function": "Speaking fluently and assertively during the candidate pair interview",
        "example_el": "Μιλήστε καθαρά και με αυτοπεποίθηση στους εξεταστές κατά την προφορική δοκιμασία.",
        "example_en": "Speak clearly and with self-confidence to the examiners during the oral test.",
        "example2_el": "Η καλή προετοιμασία ενισχύει την αυτοπεποίθηση του υποψηφίου.",
        "example2_en": "Good preparation enhances the candidate's self-confidence."
    },
    {
        "id": "A2-U12-033",
        "greek": "η επανάληψη",
        "english": "revision / review / repetition",
        "notes": "Feminine noun in -η (-εις). Relates to 'επαναλαμβάνω' (to repeat / revise).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι επαναλήψεις",
            "verb": "επαναλαμβάνω",
            "collocation": "τελική επανάληψη (final revision)"
        },
        "keg_communicative_function": "Scheduling systematic vocabulary and grammar revisions prior to test day",
        "example_el": "Κάντε μια τελική επανάληψη των βασικών γραμματικών κανόνων λίγες μέρες πριν από τις εξετάσεις.",
        "example_en": "Do a final revision of basic grammar rules a few days before the examinations.",
        "example2_el": "Η επανάληψη είναι η μητέρα της μαθήσεως.",
        "example2_en": "Repetition is the mother of learning."
    },
    {
        "id": "A2-U12-034",
        "greek": "η συνεργασία των υποψηφίων",
        "english": "candidate collaboration (pair work)",
        "notes": "Feminine noun phrase. Specifically evaluated in Speaking Stage 3 (joint interaction).",
        "gender_or_pos": "noun phrase (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "evaluative_criterion": "evaluated in Speaking Stage 3"
        },
        "keg_communicative_function": "Demonstrating cooperative turn-taking and active listening with a peer partner",
        "example_el": "Στο τρίτο μέρος της προφορικής εξέτασης αξιολογείται η ουσιαστική συνεργασία των δύο υποψηφίων.",
        "example_en": "In the third part of the oral exam the substantive collaboration of the two candidates is evaluated.",
        "example2_el": "Ακούστε προσεκτικά τον συνομιλητή σας και ανταποκριθείτε στα επιχειρήματά του.",
        "example2_en": "Listen carefully to your partner and respond to their arguments."
    },
    {
        "id": "A2-U12-035",
        "greek": "η επιτυχία",
        "english": "success",
        "notes": "Feminine noun in -α (-ες). Relates to 'πετυχαίνω' (to succeed / to pass). Standard test blessing.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι επιτυχίες",
            "verb": "πετυχαίνω",
            "collocation": "καλή επιτυχία (good luck / every success)"
        },
        "keg_communicative_function": "Wishing success and celebrating the completion of the CEFR A2 curriculum",
        "example_el": "Σας συγχαίρω θερμά για την επιτυχία σας και την απόκτηση του Πιστοποιητικού Ελληνομάθειας Α2!",
        "example_en": "I warmly congratulate you on your success and on obtaining the A2 Certificate of Attainment in Greek!",
        "example2_el": "Η συνέπεια και η αγάπη για τη γλώσσα αποτελούν τη μεγαλύτερη εγγύηση για την επιτυχία.",
        "example2_en": "Consistency and love for the language constitute the greatest guarantee of success."
    }
]

def synthesize_audio_threaded(cards, unit_id):
    tasks = []
    for c in cards:
        cid = c["id"]
        # Headword
        grk = c["greek"]
        h_fn = generate_audio_filename(grk)
        h_path = AUDIO_DIR / h_fn
        c["audio"] = h_fn
        c["status"] = "verified"
        if not h_path.exists() or h_path.stat().st_size == 0:
            tasks.append((cid, "Headword", grk, h_fn, h_path))

        # Ex 1
        ex1 = c["example_el"]
        fn1 = generate_audio_filename(ex1)
        p1 = AUDIO_DIR / fn1
        c["example_audio"] = fn1
        if not p1.exists() or p1.stat().st_size == 0:
            tasks.append((cid, "Ex1", ex1, fn1, p1))

        # Ex 2
        ex2 = c["example2_el"]
        fn2 = generate_audio_filename(ex2)
        p2 = AUDIO_DIR / fn2
        c["example2_audio"] = fn2
        if not p2.exists() or p2.stat().st_size == 0:
            tasks.append((cid, "Ex2", ex2, fn2, p2))

    total_needed = len(tasks)
    print(f"[{unit_id}] Synthesizing {total_needed} missing audio files using 8 parallel worker threads...")

    completed = 0
    t0 = time.time()

    def worker(task):
        cid, label, text, fn, path = task
        try:
            b = synthesize_greek_chirp(text)
            with open(path, "wb") as f_out:
                f_out.write(b)
            return True, cid, label, fn
        except Exception as e:
            return False, cid, label, str(e)

    with ThreadPoolExecutor(max_workers=8) as executor:
        for ok, cid, label, res in executor.map(worker, tasks):
            completed += 1
            if ok:
                if completed % 10 == 0 or completed == total_needed:
                    print(f"  [{unit_id}] {completed}/{total_needed} done ({time.time()-t0:.1f}s)")
            else:
                print(f"  [ERROR] {cid} {label}: {res}")

    print(f"[{unit_id}] Parallel audio synthesis complete in {time.time()-t0:.2f}s ({completed} files).")
    return total_needed

def save_unit_yaml(unit_id, lesson_id, title, description, lesson_notes, cards):
    unit_dir = CONTENT_DIR / unit_id
    unit_dir.mkdir(parents=True, exist_ok=True)
    yaml_file = unit_dir / f"{lesson_id}.yaml"
    
    lesson_data = {
        "unit_id": unit_id,
        "lesson_id": lesson_id,
        "title": title,
        "description": description,
        "lesson_status": "not_started",
        "lesson_notes": lesson_notes,
        "entries": cards
    }
    
    with open(yaml_file, "w", encoding="utf-8") as f:
        yaml.dump(lesson_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"[{unit_id}] Saved {len(cards)} cards to {yaml_file}")

def update_manifest():
    manifest_path = CONTENT_DIR / "manifest.yaml"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)
        
    units = manifest.get("units", [])
    existing_ids = {u["id"] for u in units}
    
    batch6_entries = [
        {
            "id": "unit-a2-11",
            "title": "Μάθημα 11: Πολιτισμός, ΜΜΕ & Ψηφιακή Ζωή (Culture, Media & Digital Life)",
            "description": "Engaging with Greek cinema, theater, news, digital platforms, and internet communication, using neuter third-declension nouns in -ος / -ους (το λάθος, το μέρος, το κόστος) and relative pronouns (που, ο οποίος).",
            "order": "KEG-A2-11-A",
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2-11/lesson-01.yaml",
                    "title": "Μάθημα 11: Πολιτισμός, ΜΜΕ & Ψηφιακή Ζωή (Culture, Media & Digital Life)"
                }
            ]
        },
        {
            "id": "unit-a2-12",
            "title": "Μάθημα 12: Εξεταστικό Εργαστήριο & Προσομοίωση (KEG A2 Exam Workshop & Simulation)",
            "description": "Mastering discourse connectors (επομένως, ωστόσο, εξάλλου, κατά τη γνώμη μου, από τη μία... από την άλλη), argumentation tactics, and pair interaction protocols for full simulation of the official May KEG A2 certification paper.",
            "order": "KEG-A2-12-A",
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2-12/lesson-01.yaml",
                    "title": "Μάθημα 12: Εξεταστικό Εργαστήριο & Προσομοίωση (KEG A2 Exam Workshop & Simulation)"
                }
            ]
        }
    ]
    
    added = 0
    for entry in batch6_entries:
        if entry["id"] not in existing_ids:
            units.append(entry)
            existing_ids.add(entry["id"])
            added += 1
            print(f"[Manifest] Appended {entry['id']} ({entry['order']})")
        else:
            for u in units:
                if u["id"] == entry["id"]:
                    u["lessons"] = entry["lessons"]
            print(f"[Manifest] {entry['id']} already exists, verified lessons array")
            
    manifest["units"] = units
    with open(manifest_path, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"[Manifest] Manifest saved with {len(units)} units total ({added} new).")

def main():
    print("--- Starting KEG-A2 Batch 6 Generation & Parallel Synthesis ---")
    
    # 1. Unit A2-11
    u11_notes = """Unit A2-11 Core Notes: Πολιτισμός, ΜΜΕ & Ψηφιακή Ζωή (Culture, Media & Digital Life)
• Arts & Cultural Activities:
  - πολιτισμός (culture), τέχνη (art), παράσταση (performance), συναυλία (concert), ταινία (movie), ηθοποιός (actor), σκηνοθέτης (director).
  - Digital & Media: ΜΜΕ (mass media), είδηση (news item), διαδίκτυο (internet), ιστοσελίδα (website), εφαρμογή (app), μέσα κοινωνικής δικτύωσης (social networks).

• Neuter Nouns in -ος / -ους (Third Declension):
  - Singular: το λάθος, του λάθους, το λάθος.
  - Plural: τα λάθη, των λαθών, τα λάθη.
  - Core paradigms: το μέρος (place/part), το κόστος (cost), το είδος (type), το μέγεθος (size), το κράτος (state), το δάσος (forest).

• Relative Pronouns:
  - Invariable 'που' (who, which, that): easy, unaccented, universally applicable.
  - Variable 'ο οποίος, η οποία, το οποίο': formal, agrees in gender, number, and case with antecedent."""

    synthesize_audio_threaded(CARDS_U11, "unit-a2-11")
    save_unit_yaml(
        unit_id="unit-a2-11",
        lesson_id="lesson-01",
        title="Μάθημα 11: Πολιτισμός, ΜΜΕ & Ψηφιακή Ζωή (Culture, Media & Digital Life)",
        description="Engaging with Greek cinema, theater, news, digital platforms, and internet communication, using neuter third-declension nouns in -ος / -ους (το λάθος, το μέρος, το κόστος) and relative pronouns (που, ο οποίος).",
        lesson_notes=u11_notes,
        cards=CARDS_U11
    )

    # 2. Unit A2-12
    u12_notes = """Unit A2-12 Core Notes: Εξεταστικό Εργαστήριο & Προσομοίωση (KEG A2 Exam Workshop)
• Discourse Connectors & Cohesion (Συνδετικές λέξεις):
  - Consequence: επομένως (therefore), κατά συνέπεια (as a result).
  - Contrast: ωστόσο (however), από τη μία πλευρά... από την άλλη πλευρά (on the one hand... on the other).
  - Addition: εξάλλου (moreover / besides), επιπλέον (furthermore).
  - Structuring: πρώτον (firstly), δεύτερον (secondly), τελικά (finally), συμπερασματικά (in conclusion).
  - Opinion: κατά τη γνώμη μου (in my opinion), συμφωνώ απόλυτα (I completely agree), διαφωνώ (I disagree).

• Exam Simulation Strategy across the 4 Papers:
  - Listening (30 mins): Focus on keywords during first playback; verify during second.
  - Reading (45 mins): Skim headline/subheads; match exact factual evidence.
  - Writing (45 mins): Task 1 (note/invitation, 40-50 words); Task 2 (narrative/letter, 70-80 words).
  - Speaking (10-12 mins): Stage 1 (personal interview); Stage 2 (cue-card role-play); Stage 3 (collaborative negotiation)."""

    synthesize_audio_threaded(CARDS_U12, "unit-a2-12")
    save_unit_yaml(
        unit_id="unit-a2-12",
        lesson_id="lesson-01",
        title="Μάθημα 12: Εξεταστικό Εργαστήριο & Προσομοίωση (KEG A2 Exam Workshop & Simulation)",
        description="Mastering discourse connectors (επομένως, ωστόσο, εξάλλου, κατά τη γνώμη μου, από τη μία... από την άλλη), argumentation tactics, and pair interaction protocols for full simulation of the official May KEG A2 certification paper.",
        lesson_notes=u12_notes,
        cards=CARDS_U12
    )

    # 3. Update manifest
    update_manifest()
    print("\n[OK] Batch 6 generation and parallel synthesis finished successfully!")

if __name__ == "__main__":
    main()

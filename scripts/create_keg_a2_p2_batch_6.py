# -*- coding: utf-8 -*-
"""
Generate KEG-A2 Part 2 Batch 6:
- Unit A2P2-11: KEG-A2-P2-11-A (30 cards) - Culture, Arts, Media & Digital Communication
- Unit A2P2-12: KEG-A2-P2-12-A (30 cards) - Exam Writing Mastery, Advanced Orthography Traps & Full Exam Synthesis
Includes dual exam example sentences and multi-threaded Google Cloud Chirp-3 HD TTS with rate limit retries.
"""
import sys
import os
import time
import yaml
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from server.tts_service import synthesize_greek_chirp, generate_audio_filename

AUDIO_DIR = BASE_DIR / "audio"
CONTENT_DIR = BASE_DIR / "content"

# -------------------------------------------------------------
# UNIT A2P2-11 CARDS (30 cards)
# Theme: Πολιτισμός, Τέχνες, Μέσα Μαζικής Ενημέρωσης & Ψηφιακή Επικοινωνία
# -------------------------------------------------------------
CARDS_U11 = [
    {
        "id": "A2P2-U11-001",
        "greek": "η θεατρική παράσταση",
        "english": "theatrical performance / play",
        "notes": "Collocation: η παράσταση (performance) + adjective θεατρικός, -ή, -ό.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Discussing cultural events, theater attendance, and leisure activities",
        "example_el": "Κλείσαμε εισιτήρια για μια εξαιρετική θεατρική παράσταση το Σάββατο.",
        "example_en": "We booked tickets for an excellent theater performance on Saturday.",
        "example2_el": "Η θεατρική παράσταση ξεκινάει ακριβώς στις εννέα το βράδυ.",
        "example2_en": "The theater performance starts punctually at nine in the evening."
    },
    {
        "id": "A2P2-U11-002",
        "greek": "η έκθεση ζωγραφικής",
        "english": "painting exhibition / art exhibition",
        "notes": "Noun η έκθεση + γενική της ζωγραφικής (painting).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Inviting someone to visit an exhibition and discussing artworks",
        "example_el": "Στην πινακοθήκη φιλοξενείται μια νέα έκθεση ζωγραφικής γνωστών Ελλήνων δημιουργών.",
        "example_en": "The art gallery is hosting a new painting exhibition by well-known Greek artists.",
        "example2_el": "Θέλεις να πάμε μαζί στην έκθεση ζωγραφικής την Κυριακή το πρωί;",
        "example2_en": "Do you want us to go together to the painting exhibition on Sunday morning?"
    },
    {
        "id": "A2P2-U11-003",
        "greek": "το μουσείο σύγχρονης τέχνης",
        "english": "museum of contemporary art",
        "notes": "Genitive: σύγχρονης (contemporary/modern) + τέχνης (art).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Recommending sightseeing landmarks and cultural venues",
        "example_el": "Το μουσείο σύγχρονης τέχνης έχει δωρεάν είσοδο κάθε πρώτη Πέμπτη του μήνα.",
        "example_en": "The contemporary art museum has free entrance every first Thursday of the month.",
        "example2_el": "Περάσαμε τρεις ώρες στο μουσείο σύγχρονης τέχνης θαυμάζοντας τα γλυπτά.",
        "example2_en": "We spent three hours at the contemporary art museum admiring the sculptures."
    },
    {
        "id": "A2P2-U11-004",
        "greek": "το μουσικό φεστιβάλ",
        "english": "music festival",
        "notes": "Neuter noun φεστιβάλ (indeclinable) + adjective μουσικός, -ή, -ό.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Describing summer music events and booking tickets",
        "example_el": "Κάθε καλοκαίρι διοργανώνεται ένα διεθνές μουσικό φεστιβάλ στο αρχαίο θέατρο.",
        "example_en": "Every summer an international music festival is organized at the ancient theater.",
        "example2_el": "Αγοράσαμε κάρτα διαρκείας για όλες τις συναυλίες του μουσικού φεστιβάλ.",
        "example2_en": "We bought a season pass for all the concerts of the music festival."
    },
    {
        "id": "A2P2-U11-005",
        "greek": "η κριτική ταινίας",
        "english": "film / movie review",
        "notes": "Noun η κριτική + γενική ταινίας. Essential for discussing cultural opinions.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Reading and writing short reviews of movies and plays",
        "example_el": "Διάβασα μια θετική κριτική ταινίας και αποφάσισα να πάω στον κινηματογράφο.",
        "example_en": "I read a positive movie review and decided to go to the cinema.",
        "example2_el": "Ο δημοσιογράφος έγραψε μια αυστηρή κριτική ταινίας για τη νέα παραγωγή.",
        "example2_en": "The journalist wrote a strict film review about the new production."
    },
    {
        "id": "A2P2-U11-006",
        "greek": "η αίθουσα κινηματογράφου",
        "english": "cinema auditorium / movie theater hall",
        "notes": "Noun η αίθουσα (hall/room) + γενική κινηματογράφου.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Giving directions inside an entertainment complex or arranging meetup spots",
        "example_el": "Παρακαλούμε απενεργοποιήστε τα κινητά σας τηλέφωνα μέσα στην αίθουσα κινηματογράφου.",
        "example_en": "Please turn off your mobile phones inside the cinema auditorium.",
        "example2_el": "Συναντηθήκαμε έξω από την αίθουσα κινηματογράφου δέκα λεπτά πριν την προβολή.",
        "example2_en": "We met outside the cinema auditorium ten minutes before the screening."
    },
    {
        "id": "A2P2-U11-007",
        "greek": "η ξενάγηση",
        "english": "guided tour",
        "notes": "Noun derived from ξεναγώ (to guide tourists).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Asking for and booking guided tours in archaeological and historical sites",
        "example_el": "Η ξενάγηση στον αρχαιολογικό χώρο γίνεται στα ελληνικά και στα αγγλικά.",
        "example_en": "The guided tour at the archaeological site is conducted in Greek and in English.",
        "example2_el": "Συμμετείχαμε σε μια δίωρη ξενάγηση στην παλιά πόλη.",
        "example2_en": "We participated in a two-hour guided tour of the old town."
    },
    {
        "id": "A2P2-U11-008",
        "greek": "ο / η ξεναγός",
        "english": "tour guide",
        "notes": "Common gender noun: ο ξεναγός / η ξεναγός.",
        "gender_or_pos": "noun (masculine/feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "common"},
        "keg_communicative_function": "Interacting with tourist professionals and following explanations",
        "example_el": "Η ξεναγός μάς εξήγησε την ιστορία του μνημείου με πολύ κατανοητό τρόπο.",
        "example_en": "The tour guide explained the history of the monument to us in a very clear way.",
        "example2_el": "Ακολουθήσαμε τον ξεναγό μέσα από τα στενά σοκάκια του νησιού.",
        "example2_en": "We followed the tour guide through the narrow alleyways of the island."
    },
    {
        "id": "A2P2-U11-009",
        "greek": "το δελτίο ειδήσεων",
        "english": "news broadcast / news bulletin",
        "notes": "Collocation: το δελτίο + γενική πληθυντικού των ειδήσεων.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Talking about current affairs, television programming, and daily news updates",
        "example_el": "Κάθε βράδυ στις οκτώ παρακολουθώ το κεντρικό δελτίο ειδήσεων στην τηλεόραση.",
        "example_en": "Every evening at eight I watch the main news bulletin on television.",
        "example2_el": "Στο δελτίο ειδήσεων ανακοίνωσαν σημαντικές αλλαγές στον καιρό.",
        "example2_en": "On the news broadcast they announced significant changes in the weather."
    },
    {
        "id": "A2P2-U11-010",
        "greek": "η εφημερίδα",
        "english": "newspaper",
        "notes": "Feminine noun (-α, -ες). Related: ο/η εφημεριδοπώλης.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Discussing news sources and purchasing reading material at the kiosk",
        "example_el": "Αγοράζω την κυριακάτικη εφημερίδα για να διαβάσω τα πολιτιστικά νέα.",
        "example_en": "I buy the Sunday newspaper to read the cultural news.",
        "example2_el": "Το άρθρο δημοσιεύτηκε στην πρώτη σελίδα της τοπικής εφημερίδας.",
        "example2_en": "The article was published on the front page of the local newspaper."
    },
    {
        "id": "A2P2-U11-011",
        "greek": "το ενημερωτικό άρθρο",
        "english": "informative article / news article",
        "notes": "Adjective ενημερωτικός, -ή, -ό + noun το άρθρο.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Referring to informational texts and quoting journalistic sources",
        "example_el": "Διάβασα ένα ενδιαφέρον ενημερωτικό άρθρο για την προστασία του περιβάλλοντος.",
        "example_en": "I read an interesting informative article about environmental protection.",
        "example2_el": "Το ενημερωτικό άρθρο περιλαμβάνει χρήσιμες συμβουλές για τους καταναλωτές.",
        "example2_en": "The informative article includes useful advice for consumers."
    },
    {
        "id": "A2P2-U11-012",
        "greek": "ο / η δημοσιογράφος",
        "english": "journalist / reporter",
        "notes": "Two-gender noun: ο δημοσιογράφος / η δημοσιογράφος.",
        "gender_or_pos": "noun (masculine/feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "common"},
        "keg_communicative_function": "Identifying professions in media and communications",
        "example_el": "Η δημοσιογράφος έκανε συνέντευξη με τον σκηνοθέτη της νέας ταινίας.",
        "example_en": "The journalist interviewed the director of the new movie.",
        "example2_el": "Πολλοί δημοσιογράφοι συγκεντρώθηκαν στην αίθουσα για τη συνέντευξη τύπου.",
        "example2_en": "Many journalists gathered in the hall for the press conference."
    },
    {
        "id": "A2P2-U11-013",
        "greek": "η ηλεκτρονική συνδρομή",
        "english": "digital / online subscription",
        "notes": "Adjective ηλεκτρονικός, -ή, -ό + noun συνδρομή (subscription).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Managing digital services, newspaper paywalls, and streaming accounts",
        "example_el": "Ανανέωσα την ετήσια ηλεκτρονική συνδρομή μου στο περιοδικό τέχνης.",
        "example_en": "I renewed my annual online subscription to the art magazine.",
        "example2_el": "Με την ηλεκτρονική συνδρομή έχεις πρόσβαση σε όλα τα άρθρα του ιστότοπου.",
        "example2_en": "With the digital subscription you have access to all website articles."
    },
    {
        "id": "A2P2-U11-014",
        "greek": "τα μέσα κοινωνικής δικτύωσης",
        "english": "social media platforms / social networks",
        "notes": "Fixed expression: τα μέσα (media) + κοινωνικής δικτύωσης (social networking).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Discussing online communication, habits, and digital lifestyle",
        "example_el": "Πολλοί νέοι ενημερώνονται καθημερινά κυρίως από τα μέσα κοινωνικής δικτύωσης.",
        "example_en": "Many young people get their daily updates mainly from social media.",
        "example2_el": "Αποφάσισα να περιορίσω τον χρόνο που περνάω στα μέσα κοινωνικής δικτύωσης.",
        "example2_en": "I decided to limit the time I spend on social networks."
    },
    {
        "id": "A2P2-U11-015",
        "greek": "η ανάρτηση",
        "english": "post / publication (on social media or forum)",
        "notes": "From αναρτώ (to post/upload). Plural: οι αναρτήσεις.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Describing social media interactions, photos, and status updates",
        "example_el": "Έκανε μια πολύ όμορφη ανάρτηση με φωτογραφίες από το ταξίδι του στα Χανιά.",
        "example_en": "He made a very beautiful post with photos from his trip to Chania.",
        "example2_el": "Είδα την ανάρτησή σου για το σεμινάριο και τη βρήκα πολύ ενδιαφέρουσα.",
        "example2_en": "I saw your post about the seminar and found it very interesting."
    },
    {
        "id": "A2P2-U11-016",
        "greek": "ο λογαριασμός χρήστη",
        "english": "user account",
        "notes": "Collocation: ο λογαριασμός (account) + γενική του χρήστη (user).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "masculine"},
        "keg_communicative_function": "Handling website registration, login prompts, and account management",
        "example_el": "Για να υποβάλετε την αίτηση, πρέπει πρώτα να δημιουργήσετε λογαριασμό χρήστη.",
        "example_en": "To submit the application, you must first create a user account.",
        "example2_el": "Συνδέθηκα στον λογαριασμό χρήστη μου για να ελέγξω τα στοιχεία πληρωμής.",
        "example2_en": "I logged into my user account to verify the payment details."
    },
    {
        "id": "A2P2-U11-017",
        "greek": "ο κωδικός πρόσβασης",
        "english": "password / access code",
        "notes": "Collocation: ο κωδικός + γενική πρόσβασης (access).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "masculine"},
        "keg_communicative_function": "Resetting passwords and describing cybersecurity procedures",
        "example_el": "Ξέχασα τον κωδικό πρόσβασης και ζήτησα επαναφορά μέσω email.",
        "example_en": "I forgot my password and requested a reset via email.",
        "example2_el": "Πρέπει να επιλέξετε έναν ισχυρό κωδικό πρόσβασης με γράμματα και αριθμούς.",
        "example2_en": "You must choose a strong password with letters and numbers."
    },
    {
        "id": "A2P2-U11-018",
        "greek": "η ψηφιακή εφαρμογή",
        "english": "digital application / mobile app",
        "notes": "Adjective ψηφιακός, -ή, -ό + noun η εφαρμογή (app/application).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Referring to smartphone apps for transit, tickets, and communication",
        "example_el": "Κατέβασα στο κινητό μου τη νέα ψηφιακή εφαρμογή για τα δρομολόγια των λεωφορείων.",
        "example_en": "I downloaded onto my mobile the new digital app for bus schedules.",
        "example2_el": "Αυτή η ψηφιακή εφαρμογή με βοηθάει καθημερινά στην εκμάθηση νέων ελληνικών λέξεων.",
        "example2_en": "This digital app helps me daily in learning new Greek words."
    },
    {
        "id": "A2P2-U11-019",
        "greek": "το μήνυμα ηλεκτρονικού ταχυδρομείου",
        "english": "email message",
        "notes": "Formal Greek term for email. Colloquially also: το μέιλ.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Referring to email correspondence in administrative and exam writing prompts",
        "example_el": "Σας στέλνω αυτό το μήνυμα ηλεκτρονικού ταχυδρομείου για να επιβεβαιώσω την κράτησή μου.",
        "example_en": "I am sending you this email message to confirm my reservation.",
        "example2_el": "Έλαβα ένα μήνυμα ηλεκτρονικού ταχυδρομείου με όλα τα απαραίτητα έγγραφα.",
        "example2_en": "I received an email message with all the required documents."
    },
    {
        "id": "A2P2-U11-020",
        "greek": "η κοινοποίηση συνδέσμου",
        "english": "link sharing / sharing a link",
        "notes": "Noun κοινοποίηση (sharing/notification) + γενική συνδέσμου (link).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Sharing articles, invitations, and web links with friends and classmates",
        "example_el": "Η κοινοποίηση συνδέσμου στην ομάδα βοήθησε όλους τους φοιτητές να βρουν τις σημειώσεις.",
        "example_en": "Sharing the link in the group helped all students find the notes.",
        "example2_el": "Σου έκανα κοινοποίηση συνδέσμου για τη συναυλία που συζητούσαμε.",
        "example2_en": "I shared a link with you for the concert we were discussing."
    },
    {
        "id": "A2P2-U11-021",
        "greek": "το σχόλιο",
        "english": "comment / feedback note",
        "notes": "Neuter noun (-ιο, -ια). Verb: σχολιάζω (to comment).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "neuter"},
        "keg_communicative_function": "Leaving comments on blogs, posts, and class forums",
        "example_el": "Άφησα ένα θετικό σχόλιο κάτω από τη φωτογραφία της παράστασης.",
        "example_en": "I left a positive comment under the photo of the performance.",
        "example2_el": "Διάβασα με προσοχή όλα τα σχόλια των αναγνωστών στο ιστολόγιο.",
        "example2_en": "I carefully read all reader comments on the blog."
    },
    {
        "id": "A2P2-U11-022",
        "greek": "ο / η θεατής",
        "english": "spectator / viewer / audience member",
        "notes": "Masculine: ο θεατής (-ής, -ές). Feminine: η θεατής or η θεάτρια. Plural: οι θεατές.",
        "gender_or_pos": "noun (masculine/feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "masculine"},
        "keg_communicative_function": "Describing audience reaction in arts and cinema",
        "example_el": "Οι θεατές χειροκρότησαν θερμά τους ηθοποιούς στο τέλος του έργου.",
        "example_en": "The spectators warmly applauded the actors at the end of the play.",
        "example2_el": "Χιλιάδες θεατές παρακολούθησαν τη συναυλία στο ανοιχτό γήπεδο.",
        "example2_en": "Thousands of spectators attended the concert at the open stadium."
    },
    {
        "id": "A2P2-U11-023",
        "greek": "η συναυλία κλασικής μουσικής",
        "english": "classical music concert",
        "notes": "Noun η συναυλία + γενική κλασικής μουσικής.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Describing musical outings and personal taste in art",
        "example_el": "Πήγαμε στο Μέγαρο Μουσικής για μια μαγευτική συναυλία κλασικής μουσικής.",
        "example_en": "We went to the Concert Hall for an enchanting classical music concert.",
        "example2_el": "Η συναυλία κλασικής μουσικής περιλάμβανε έργα του Μότσαρτ και του Μπετόβεν.",
        "example2_en": "The classical music concert featured works by Mozart and Beethoven."
    },
    {
        "id": "A2P2-U11-024",
        "greek": "η πολιτιστική εκδήλωση",
        "english": "cultural event",
        "notes": "Adjective πολιτιστικός, -ή, -ό + noun η εκδήλωση (-η, -εις).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Participating in community events and writing cultural invitations",
        "example_el": "Ο δήμος οργανώνει μια μεγάλη πολιτιστική εκδήλωση στην κεντρική πλατεία.",
        "example_en": "The municipality is organizing a major cultural event in the central square.",
        "example2_el": "Η πολιτιστική εκδήλωση συγκέντρωσε καλλιτέχνες από όλη τη χώρα.",
        "example2_en": "The cultural event gathered artists from all across the country."
    },
    {
        "id": "A2P2-U11-025",
        "greek": "η πρεμιέρα",
        "english": "premiere / opening night",
        "notes": "Feminine loanword (-α, -ες). Used for films and theater.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Discussing first screenings and debut theater nights",
        "example_el": "Η πρεμιέρα της ταινίας προσέλκυσε πλήθος κόσμου και διάσημους καλλιτέχνες.",
        "example_en": "The movie premiere attracted crowds of people and famous artists.",
        "example2_el": "Καταφέραμε να βρούμε θέσεις στην πρεμιέρα της όπερας.",
        "example2_en": "We managed to get seats for the opera premiere."
    },
    {
        "id": "A2P2-U11-026",
        "greek": "η είσοδος ελεύθερη",
        "english": "free admission / free entrance",
        "notes": "Collocation on posters: είσοδος (entrance) + ελεύθερη (free). Often: Είσοδος ελεύθερη.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Noting and communicating free admission to cultural venues",
        "example_el": "Για τη συναυλία στο πάρκο η είσοδος είναι ελεύθερη για το κοινό.",
        "example_en": "For the concert in the park, admission is free for the public.",
        "example2_el": "Η αφίσα έγραφε: 'Είσοδος ελεύθερη για όλους τους μαθητές και φοιτητές'.",
        "example2_en": "The poster stated: 'Free admission for all pupils and students'."
    },
    {
        "id": "A2P2-U11-027",
        "greek": "προτείνω ανεπιφύλακτα",
        "english": "I wholeheartedly recommend / I recommend without reservation",
        "notes": "Verb προτείνω + adverb ανεπιφύλακτα (without reservation). Premium KEG A2 review expression.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Writing glowing recommendations in reviews and personal letters",
        "example_el": "Σας προτείνω ανεπιφύλακτα αυτό το βιβλίο, είναι πραγματικά συναρπαστικό.",
        "example_en": "I wholeheartedly recommend this book to you; it is truly fascinating.",
        "example2_el": "Προτείνω ανεπιφύλακτα το εστιατόριο για το εξαιρετικό φαγητό και τη ζεστή ατμόσφαιρα.",
        "example2_en": "I recommend the restaurant without reservation for its excellent food and warm ambiance."
    },
    {
        "id": "A2P2-U11-028",
        "greek": "παρακολουθώ τα πολιτιστικά δρώμενα",
        "english": "I follow cultural events and happenings",
        "notes": "Verb παρακολουθώ + phrase τα πολιτιστικά δρώμενα (cultural happenings).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Expressing engagement with arts and cultural life in oral/written tasks",
        "example_el": "Παρακολουθώ τα πολιτιστικά δρώμενα της Αθήνας κάθε σαββατοκύριακο.",
        "example_en": "I follow the cultural happenings of Athens every weekend.",
        "example2_el": "Μου αρέσει να παρακολουθώ τα πολιτιστικά δρώμενα και να επισκέπτομαι νέες εκθέσεις.",
        "example2_en": "I enjoy following cultural events and visiting new exhibitions."
    },
    {
        "id": "A2P2-U11-029",
        "greek": "εντυπωσιάστηκα από την παράσταση",
        "english": "I was impressed by the performance",
        "notes": "Aorist passive εντυπωσιάστηκα (from εντυπωσιάζω) + preposition από.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Expressing emotional reaction and critical praise for events",
        "example_el": "Εντυπωσιάστηκα από την παράσταση και τη συγκλονιστική ερμηνεία των ηθοποιών.",
        "example_en": "I was impressed by the performance and the gripping acting of the cast.",
        "example2_el": "Όλοι οι φίλοι μου εντυπωσιάστηκαν από την παράσταση χορού.",
        "example2_en": "All my friends were impressed by the dance performance."
    },
    {
        "id": "A2P2-U11-030",
        "greek": "περνάω ευχάριστα τον ελεύθερο χρόνο μου",
        "english": "I spend my free time pleasantly",
        "notes": "Verb περνάω + adverb ευχάριστα + direct object τον ελεύθερο χρόνο μου.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Writing about hobbies, leisure activities, and weekend relaxation",
        "example_el": "Περνάω ευχάριστα τον ελεύθερο χρόνο μου διαβάζοντας βιβλία και κάνοντας ποδήλατο.",
        "example_en": "I spend my free time pleasantly reading books and cycling.",
        "example2_el": "Στο χωριό περνάμε πάντα ευχάριστα τον ελεύθερο χρόνο μας κοντά στη φύση.",
        "example2_en": "In the village we always spend our free time pleasantly close to nature."
    }
]

# -------------------------------------------------------------
# UNIT A2P2-12 CARDS (30 cards)
# Theme: Εξεταστική Δεξιότητα, Ορθογραφικές Παγίδες & Ολοκληρωμένη Σύνθεση
# -------------------------------------------------------------
CARDS_U12 = [
    {
        "id": "A2P2-U12-001",
        "greek": "πολύ vs πολλή (πολλή δουλειά / πολύ κουρασμένος)",
        "english": "much / a lot of (feminine adjective πολλή) vs. very (adverb πολύ)",
        "notes": "Major KEG A2 spelling trap: πολλή (adjective modifying feminine noun with double λ and η) vs πολύ (adverb modifying verb or adjective, ending in υ).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Avoiding fundamental spelling errors in written production essays",
        "example_el": "Είχα πολλή δουλειά σήμερα στο γραφείο και γύρισα στο σπίτι πολύ κουρασμένος.",
        "example_en": "I had a lot of work today at the office and returned home very tired.",
        "example2_el": "Χρειάζεται πολλή υπομονή γιατί η διαδικασία είναι πολύ χρονοβόρα.",
        "example2_en": "It takes a lot of patience because the process is very time-consuming."
    },
    {
        "id": "A2P2-U12-002",
        "greek": "-ειτε vs -είται (σκέφτεστε vs σκέφτεται)",
        "english": "passive 2nd person plural ending (-εστε/-ειτε) vs 3rd person singular (-εται/-είται)",
        "notes": "Endings trap: 2nd plural imperative/subjunctive (-είτε / -εστε) vs 3rd singular present (-εται / -είται). E.g. εσείς σκέφτεστε / αυτός σκέφτεται.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Correctly inflecting passive verbs in formal and plural addressing",
        "example_el": "Σας παρακαλώ, σκεφτείτε καλά την πρότασή μας πριν αποφασίσετε.",
        "example_en": "Please consider our proposal carefully before you decide.",
        "example2_el": "Ο διευθυντής σκέφτεται να προσλάβει δύο νέους υπαλλήλους.",
        "example2_en": "The manager is considering hiring two new employees."
    },
    {
        "id": "A2P2-U12-003",
        "greek": "-τε vs -ται (γράφετε vs γράφεται)",
        "english": "active 2nd plural ending (-τε) vs passive 3rd singular ending (-ται)",
        "notes": "Classic Greek spelling trap: -τε is active 2nd plural (εσείς γράφετε), while -ται is passive 3rd singular (αυτό γράφεται).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Distinguishing active you-plural addressing from passive statements in writing",
        "example_el": "Όταν γράφετε μια επίσημη επιστολή, προσέχετε την ορθογραφία των λέξεων.",
        "example_en": "When you write a formal letter, pay attention to the spelling of the words.",
        "example2_el": "Αυτή η λέξη γράφεται με δύο λάμδα και υπογεγραμμένη.",
        "example2_en": "This word is written with two lambdas and an iota."
    },
    {
        "id": "A2P2-U12-004",
        "greek": "ο βαθύς, η βαθιά, το βαθύ",
        "english": "deep (masc / fem / neuter - adjectives in -ύς, -ιά, -ύ)",
        "notes": "Irregular adjective declension: masc βαθύς/βαθιού, fem βαθιά/βαθιάς, neut βαθύ/βαθιού. Plural: βαθιοί, βαθιές, βαθιά. Same as βαρύς, ελαφρύς, μακρύς.",
        "gender_or_pos": "adjective",
        "grammatical_info": {"part_of_speech": "adjective"},
        "keg_communicative_function": "Using physical descriptive adjectives accurately across gender forms",
        "example_el": "Η θάλασσα σε εκείνο το σημείο έχει πολύ βαθιά νερά και χρειάζεται προσοχή.",
        "example_en": "The sea at that spot has very deep waters and caution is needed.",
        "example2_el": "Πήρα μια βαθιά ανάσα πριν μπω στην αίθουσα των εξετάσεων.",
        "example2_en": "I took a deep breath before entering the examination room."
    },
    {
        "id": "A2P2-U12-005",
        "greek": "ο / η / το ίδιος, ίδια, ίδιο",
        "english": "the same / identical (or emphatic: myself, yourself)",
        "notes": "Used with article: ο ίδιος / η ίδια / το ίδιο = 'the same'. Without article / emphatic: εγώ ο ίδιος = 'I myself'.",
        "gender_or_pos": "adjective",
        "grammatical_info": {"part_of_speech": "adjective"},
        "keg_communicative_function": "Comparing similarities and emphasizing personal agency",
        "example_el": "Έχουμε ακριβώς το ίδιο πρόγραμμα μαθημάτων κάθε Δευτέρα και Τετάρτη.",
        "example_en": "We have the exact same class schedule every Monday and Wednesday.",
        "example2_el": "Μίλησα με τον ίδιο τον υπεύθυνο και μου εξήγησε τη διαδικασία.",
        "example2_en": "I spoke with the person in charge himself and he explained the procedure to me."
    },
    {
        "id": "A2P2-U12-006",
        "greek": "ο / η / το δικός, δική, δικό μου",
        "english": "my own (emphatic possessive pronoun)",
        "notes": "Emphatic possessive: ο δικός μου / η δική μου / το δικό μου. Declines like an adjective.",
        "gender_or_pos": "pronoun",
        "grammatical_info": {"part_of_speech": "pronoun"},
        "keg_communicative_function": "Emphasizing ownership and personal perspective in written compositions",
        "example_el": "Το δικό μου διαμέρισμα είναι πιο φωτεινό από το παλιό μου σπίτι.",
        "example_en": "My own apartment is brighter than my old home.",
        "example2_el": "Αυτή είναι η δική μου άποψη για το θέμα της δημόσιας συγκοινωνίας.",
        "example2_en": "This is my own view on the issue of public transit."
    },
    {
        "id": "A2P2-U12-007",
        "greek": "Αξιότιμε κύριε / Αξιότιμη κυρία",
        "english": "Dear Sir / Dear Madam (Formal salutation formula)",
        "notes": "Vocative singular of αξιότιμος (esteemed/honorable): Αξιότιμε κύριε / Αξιότιμη κυρία. Mandatory opening for formal letters.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Opening formal letters, official emails, and administrative requests in exam tasks",
        "example_el": "Αξιότιμε κύριε Διευθυντή, σας γράφω για να υποβάλω αίτηση συμμετοχής στο πρόγραμμα.",
        "example_en": "Dear Mr. Director, I am writing to submit an application to participate in the program.",
        "example2_el": "Αξιότιμη κυρία Παπαδοπούλου, σας ευχαριστώ θερμά για την άμεση απάντησή σας.",
        "example2_en": "Dear Ms. Papadopoulou, thank you warmly for your prompt reply."
    },
    {
        "id": "A2P2-U12-008",
        "greek": "Με εκτίμηση",
        "english": "Yours sincerely / With respect (Formal closing formula)",
        "notes": "Preposition με + accusative εκτίμηση (esteem/respect). Standard formal closing formula before candidate signature.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Closing formal letters and emails according to KEG scoring standards",
        "example_el": "Σας ευχαριστώ εκ των προτέρων για τον χρόνο σας. Με εκτίμηση, Γιώργος Παπαδόπουλος.",
        "example_en": "Thank you in advance for your time. Yours sincerely, Giorgos Papadopoulos.",
        "example2_el": "Με εκτίμηση και σεβασμό προς το έργο του ιδρύματος.",
        "example2_en": "Yours sincerely and with respect toward the foundation's work."
    },
    {
        "id": "A2P2-U12-009",
        "greek": "Σας γράφω για να σας ενημερώσω",
        "english": "I am writing to inform you (Formal introductory purpose statement)",
        "notes": "Fixed formal opening sentence: Σας γράφω (I write to you) + για να σας ενημερώσω (in order to inform you).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Stating the purpose of writing in Task 2 exam scenarios",
        "example_el": "Σας γράφω για να σας ενημερώσω σχετικά με την αλλαγή της ημερομηνίας άφιξής μου.",
        "example_en": "I am writing to inform you regarding the change in my arrival date.",
        "example2_el": "Σας γράφω για να σας ενημερώσω ότι παρέλαβα επιτυχώς τα έγγραφα.",
        "example2_en": "I am writing to inform you that I successfully received the documents."
    },
    {
        "id": "A2P2-U12-010",
        "greek": "Θα ήθελα να εκφράσω τα παράπονά μου",
        "english": "I would like to express my complaints / I wish to file a complaint",
        "notes": "Conditional polite opener: Θα ήθελα να + εκφράσω τα παράπονά μου (my complaints).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Writing formal complaint letters regarding service defects, noise, or broken amenities",
        "example_el": "Θα ήθελα να εκφράσω τα παράπονά μου για την κακή εξυπηρέτηση στο ξενοδοχείο σας.",
        "example_en": "I would like to express my complaints regarding the poor service at your hotel.",
        "example2_el": "Θα ήθελα να εκφράσω τα έντονα παράπονά μου για τη συνεχή καθυστέρηση των δρομολογίων.",
        "example2_en": "I would like to express my strong complaints regarding the constant schedule delays."
    },
    {
        "id": "A2P2-U12-011",
        "greek": "Ζητώ συγγνώμη για την αναστάτωση",
        "english": "I apologize for the inconvenience",
        "notes": "Verb ζητώ συγγνώμη (I ask forgiveness) + preposition για + noun αναστάτωση (disruption/inconvenience).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Writing polite apologies for missed appointments or delays in exam correspondence",
        "example_el": "Ζητώ συγγνώμη για την αναστάτωση που προκάλεσε η ακύρωση του ραντεβού μου.",
        "example_en": "I apologize for the inconvenience caused by the cancellation of my appointment.",
        "example2_el": "Ζητώ συγγνώμη για την καθυστέρηση και ευχαριστώ για την κατανόησή σας.",
        "example2_en": "I apologize for the delay and thank you for your understanding."
    },
    {
        "id": "A2P2-U12-012",
        "greek": "Σας προτείνω να επισκεφθείτε",
        "english": "I suggest that you visit",
        "notes": "Polite plural/formal: Σας προτείνω + να + aorist subjunctive επισκεφθείτε (from επισκέπτομαι).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Making travel and leisure recommendations in tourist guide/email tasks",
        "example_el": "Σας προτείνω να επισκεφθείτε το νέο αρχαιολογικό μουσείο νωρίς το πρωί.",
        "example_en": "I suggest that you visit the new archaeological museum early in the morning.",
        "example2_el": "Αν βρεθείτε στην πόλη, σας προτείνω να επισκεφθείτε τις παραδοσιακές ταβέρνες.",
        "example2_en": "If you find yourself in the city, I suggest that you visit the traditional tavernas."
    },
    {
        "id": "A2P2-U12-013",
        "greek": "Κατά τη γνώμη μου",
        "english": "In my opinion",
        "notes": "Preposition κατά + accusative τη γνώμη μου. High-scoring essay discursive marker.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Stating personal viewpoints and argumentative positions in written essays",
        "example_el": "Κατά τη γνώμη μου, η χρήση των ποδηλάτων στην πόλη πρέπει να ενθαρρυνθεί περισσότερο.",
        "example_en": "In my opinion, the use of bicycles in the city should be encouraged more.",
        "example2_el": "Κατά τη γνώμη μου, τα διαδικτυακά μαθήματα προσφέρουν μεγάλη ευελιξία.",
        "example2_en": "In my opinion, online classes offer great flexibility."
    },
    {
        "id": "A2P2-U12-014",
        "greek": "Από τη μία πλευρά ... από την άλλη πλευρά",
        "english": "On the one hand ... on the other hand",
        "notes": "Balanced connective pair for presenting contrasting arguments: από τη μία πλευρά ... από την άλλη πλευρά.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Balancing advantages and disadvantages in A2 discursive writing",
        "example_el": "Από τη μία πλευρά η ζωή στην πρωτεύουσα προσφέρει ευκαιρίες, από την άλλη πλευρά όμως έχει πολύ άγχος.",
        "example_en": "On the one hand life in the capital offers opportunities, but on the other hand it has a lot of stress.",
        "example2_el": "Από τη μία πλευρά είναι ακριβό, από την άλλη πλευρά όμως η ποιότητα είναι ασύγκριτη.",
        "example2_en": "On the one hand it is expensive, but on the other hand the quality is incomparable."
    },
    {
        "id": "A2P2-U12-015",
        "greek": "Όχι μόνο ... αλλά και",
        "english": "Not only ... but also",
        "notes": "Additive correlative conjunction: Όχι μόνο [clause A] ... αλλά και [clause B].",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Linking compound positive elements with rhetorical emphasis",
        "example_el": "Το ξενοδοχείο ήταν όχι μόνο πεντακάθαρο αλλά και πολύ κοντά στην παραλία.",
        "example_en": "The hotel was not only spotless but also very close to the beach.",
        "example2_el": "Έμαθε όχι μόνο να μιλάει ελληνικά αλλά και να γράφει άπταιστα.",
        "example2_en": "She learned not only to speak Greek but also to write fluently."
    },
    {
        "id": "A2P2-U12-016",
        "greek": "Σύμφωνα με",
        "english": "According to",
        "notes": "Prepositional connector: σύμφωνα με + accusative. Used to cite sources or official instructions.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Referencing notices, regulations, and third-party statements in written exams",
        "example_el": "Σύμφωνα με τις οδηγίες του υπουργείου, οι εγγραφές ξεκινούν την πρώτη Σεπτεμβρίου.",
        "example_en": "According to the ministry's instructions, registrations begin on September first.",
        "example2_el": "Σύμφωνα με την πρόγνωση του καιρού, το σαββατοκύριακο θα έχει καταιγίδες.",
        "example2_en": "According to the weather forecast, there will be thunderstorms over the weekend."
    },
    {
        "id": "A2P2-U12-017",
        "greek": "Σε περίπτωση που",
        "english": "In case / In the event that",
        "notes": "Compound conditional conjunction: Σε περίπτωση που + verb (subjunctive or indicative).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Outlining contingencies, backup plans, and conditions in letters",
        "example_el": "Σε περίπτωση που χρειαστείτε περισσότερες πληροφορίες, μη διστάσετε να επικοινωνήσετε μαζί μου.",
        "example_en": "In case you need more information, do not hesitate to contact me.",
        "example2_el": "Σε περίπτωση που βρέχει, η συναυλία θα πραγματοποιηθεί στην κλειστή αίθουσα.",
        "example2_en": "In case it rains, the concert will take place in the indoor hall."
    },
    {
        "id": "A2P2-U12-018",
        "greek": "Παρόλο που",
        "english": "Even though / Although",
        "notes": "Concessive conjunction: Παρόλο που + indicative. Concedes a fact while affirming main clause.",
        "gender_or_pos": "conjunction",
        "grammatical_info": {"part_of_speech": "conjunction"},
        "keg_communicative_function": "Formulating complex concessive sentences in exam compositions",
        "example_el": "Παρόλο που έφτασα αργά στο αεροδρόμιο, πρόλαβα την πτήση μου στην ώρα της.",
        "example_en": "Even though I arrived late at the airport, I caught my flight on time.",
        "example2_el": "Παρόλο που το θέμα ήταν δύσκολο, όλοι οι μαθητές έγραψαν καλά στις εξετάσεις.",
        "example2_en": "Although the topic was difficult, all students wrote well in the exams."
    },
    {
        "id": "A2P2-U12-019",
        "greek": "Επομένως / Συνεπώς",
        "english": "Therefore / Consequently",
        "notes": "Cohesive adverbs of logical deduction: Επομένως / Συνεπώς.",
        "gender_or_pos": "adverb",
        "grammatical_info": {"part_of_speech": "adverb"},
        "keg_communicative_function": "Connecting cause and effect in essay development and problem solving",
        "example_el": "Δεν υπήρχαν διαθέσιμα εισιτήρια, επομένως αποφασίσαμε να ταξιδέψουμε την επόμενη μέρα.",
        "example_en": "There were no available tickets; therefore, we decided to travel the next day.",
        "example2_el": "Η προθεσμία έληξε, συνεπώς δεν γίνονται δεκτές άλλες αιτήσεις.",
        "example2_en": "The deadline expired; consequently, no further applications are accepted."
    },
    {
        "id": "A2P2-U12-020",
        "greek": "Επιπλέον / Επίσης",
        "english": "Furthermore / Moreover / In addition",
        "notes": "Additive connectors for building cumulative arguments: Επιπλέον / Επίσης.",
        "gender_or_pos": "adverb",
        "grammatical_info": {"part_of_speech": "adverb"},
        "keg_communicative_function": "Adding secondary points and supplementary reasons in written production",
        "example_el": "Το σπίτι είναι ευρύχωρο και επιπλέον βρίσκεται πολύ κοντά στο μετρό.",
        "example_en": "The house is spacious and furthermore is located very close to the metro.",
        "example2_el": "Επιπλέον, θα ήθελα να ρωτήσω αν περιλαμβάνεται το πρωινό στην τιμή του δωματίου.",
        "example2_en": "In addition, I would like to ask whether breakfast is included in the room price."
    },
    {
        "id": "A2P2-U12-021",
        "greek": "Συνοψίζοντας",
        "english": "In summary / Summarizing",
        "notes": "Active present participle (-οντας) of συνοψίζω. Standard academic summing-up connector.",
        "gender_or_pos": "participle",
        "grammatical_info": {"part_of_speech": "participle"},
        "keg_communicative_function": "Transitioning smoothly into the final paragraph of an exam essay",
        "example_el": "Συνοψίζοντας, θεωρώ ότι η εμπειρία των σπουδών στο εξωτερικό είναι πολύτιμη για κάθε νέο.",
        "example_en": "Summarizing, I consider the experience of studying abroad invaluable for every young person.",
        "example2_el": "Συνοψίζοντας τα παραπάνω σημεία, προτείνω να ξεκινήσουμε άμεσα το σχέδιο.",
        "example2_en": "Summarizing the above points, I suggest that we initiate the plan immediately."
    },
    {
        "id": "A2P2-U12-022",
        "greek": "Εν κατακλείδι",
        "english": "In conclusion / Finally",
        "notes": "Formal fixed prepositional phrase (Katharevousa relic) used in modern writing: εν κατακλείδι.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Concluding formal compositions and essays with high linguistic register",
        "example_el": "Εν κατακλείδι, πιστεύω ακράδαντα ότι η εκμάθηση μιας ξένης γλώσσας ανοίγει νέους ορίζοντες.",
        "example_en": "In conclusion, I firmly believe that learning a foreign language opens new horizons.",
        "example2_el": "Εν κατακλείδι, σας ευχαριστώ θερμά για την προσοχή σας και παραμένω στη διάθεσή σας.",
        "example2_en": "In conclusion, I thank you warmly for your attention and remain at your disposal."
    },
    {
        "id": "A2P2-U12-023",
        "greek": "Ελπίζω να λάβετε υπόψη σας το αίτημά μου",
        "english": "I hope you will consider my request",
        "notes": "Idiom λαμβάνω υπόψη (to take into consideration) + direct object το αίτημά μου.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Closing formal request or complaint letters with professional politeness",
        "example_el": "Ελπίζω να λάβετε υπόψη σας το αίτημά μου και να μου απαντήσετε σύντομα.",
        "example_en": "I hope you will take my request into consideration and reply to me soon.",
        "example2_el": "Ελπίζω να λάβετε σοβαρά υπόψη σας τις παρατηρήσεις των περιοίκων.",
        "example2_en": "I hope you will seriously consider the observations of the local residents."
    },
    {
        "id": "A2P2-U12-024",
        "greek": "Ανυπομονώ να λάβω την απάντησή σας",
        "english": "I look forward to receiving your reply",
        "notes": "Verb ανυπομονώ (I look forward to / am impatient) + να λάβω (to receive) + την απάντησή σας.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Expressing courteous expectation of response in business/formal correspondence",
        "example_el": "Ανυπομονώ να λάβω την απάντησή σας σχετικά με την αίτηση υποτροφίας.",
        "example_en": "I look forward to receiving your reply regarding the scholarship application.",
        "example2_el": "Ανυπομονώ να λάβω νέα σας και ελπίζω να συναντηθούμε από κοντά σύντομα.",
        "example2_en": "I look forward to hearing your news and hope we meet in person soon."
    },
    {
        "id": "A2P2-U12-025",
        "greek": "Με μεγάλη μου χαρά αποδέχομαι την πρόσκληση",
        "english": "With great pleasure I accept the invitation",
        "notes": "Phrase με μεγάλη μου χαρά + αποδέχομαι (I accept) + την πρόσκληση.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Accepting invitations to parties, dinners, or ceremonies in Task 1 writing",
        "example_el": "Με μεγάλη μου χαρά αποδέχομαι την πρόσκληση στον γάμο σας και ανυπομονώ να γιορτάσουμε μαζί.",
        "example_en": "With great pleasure I accept the invitation to your wedding and look forward to celebrating together.",
        "example2_el": "Με μεγάλη μου χαρά αποδέχομαι την πρόσκλησή σας να μιλήσω στη φοιτητική εκδήλωση.",
        "example2_en": "With great pleasure I accept your invitation to speak at the student event."
    },
    {
        "id": "A2P2-U12-026",
        "greek": "Δυστυχώς δεν θα μπορέσω να παρευρεθώ",
        "english": "Unfortunately I will not be able to attend",
        "notes": "Adverb δυστυχώς + δεν θα μπορέσω + aorist subjunctive παρευρεθώ (from παρευρίσκομαι).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Politely declining social invitations with regret and justification in exam tasks",
        "example_el": "Δυστυχώς δεν θα μπορέσω να παρευρεθώ στα γενέθλιά σου λόγω ανειλημμένων επαγγελματικών υποχρεώσεων.",
        "example_en": "Unfortunately I will not be able to attend your birthday due to prior professional commitments.",
        "example2_el": "Δυστυχώς δεν θα μπορέσω να παρευρεθώ στην εκδήλωση, αλλά σας εύχομαι καλή επιτυχία.",
        "example2_en": "Unfortunately I will not be able to attend the event, but I wish you every success."
    },
    {
        "id": "A2P2-U12-027",
        "greek": "Σας ευχαριστώ εκ των προτέρων για τη βοήθεια",
        "english": "Thank you in advance for your assistance",
        "notes": "Prepositional idiom εκ των προτέρων (in advance / beforehand) + για τη βοήθεια.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Concluding requests for information, favors, or assistance gracefully",
        "example_el": "Σας ευχαριστώ εκ των προτέρων για τη βοήθεια και την άμεση εξυπηρέτηση.",
        "example_en": "Thank you in advance for your assistance and prompt service.",
        "example2_el": "Σας ευχαριστώ εκ των προτέρων για τη βοήθεια που θα μου προσφέρετε στη μετακόμιση.",
        "example2_en": "Thank you in advance for the help you will offer me with moving."
    },
    {
        "id": "A2P2-U12-028",
        "greek": "Είναι απαραίτητο να γνωρίζετε ότι",
        "english": "It is necessary that you know that",
        "notes": "Impersonal phrase είναι απαραίτητο (it is essential/necessary) + να γνωρίζετε ότι.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Emphasizing critical requirements, prerequisites, and instructions in letters",
        "example_el": "Είναι απαραίτητο να γνωρίζετε ότι τα γραφεία της υπηρεσίας είναι κλειστά τα σαββατοκύριακα.",
        "example_en": "It is necessary that you know that the service offices are closed on weekends.",
        "example2_el": "Είναι απαραίτητο να γνωρίζετε ότι απαιτείται προηγούμενη επικύρωση των δικαιολογητικών.",
        "example2_en": "It is necessary that you know that prior verification of supporting documents is required."
    },
    {
        "id": "A2P2-U12-029",
        "greek": "Δεν υπάρχει αμφιβολία ότι",
        "english": "There is no doubt that",
        "notes": "Impersonal expression: Δεν υπάρχει αμφιβολία (there is no doubt) + ότι clause.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Asserting strong conviction and certainty in argumentative writing",
        "example_el": "Δεν υπάρχει αμφιβολία ότι η γνώση των ελληνικών θα με βοηθήσει να βρω καλύτερη δουλειά.",
        "example_en": "There is no doubt that knowledge of Greek will help me find a better job.",
        "example2_el": "Δεν υπάρχει αμφιβολία ότι η συστηματική εξάσκηση οδηγεί στην επιτυχία στις εξετάσεις.",
        "example2_en": "There is no doubt that systematic practice leads to success in the exams."
    },
    {
        "id": "A2P2-U12-030",
        "greek": "Ευελπιστώ σε μια θετική απάντηση",
        "english": "I look forward to / anticipate a positive response",
        "notes": "Verb ευελπιστώ (I hope/aspire with optimism) + preposition σε + accusative.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Polite high-register closing formula for job or scholarship applications",
        "example_el": "Ευελπιστώ σε μια θετική απάντηση και είμαι έτοιμος για μια προσωπική συνέντευξη.",
        "example_en": "I anticipate a positive response and am ready for an in-person interview.",
        "example2_el": "Ευελπιστώ σε μια θετική απάντηση στο αίτημά μου για ανανέωση της συνεργασίας μας.",
        "example2_en": "I look forward to a positive response to my request for renewal of our collaboration."
    }
]

def synthesize_item(text: str, filename: str) -> bool:
    if not text:
        return False
    out_file = AUDIO_DIR / filename
    if out_file.exists() and out_file.stat().st_size > 0:
        return False
    for attempt in range(4):
        try:
            audio_bytes = synthesize_greek_chirp(text)
            with open(out_file, "wb") as f:
                f.write(audio_bytes)
            return True
        except Exception as e:
            err_str = str(e)
            if "429" in err_str:
                time.sleep(2 * (attempt + 1))
                continue
            print(f"    [ERR] {text[:30]}: {e}")
            return False
    return False

def process_and_save_unit(unit_id: str, lesson_id: str, title: str, description: str, lesson_notes: str, cards: list, order_code: str):
    unit_dir = CONTENT_DIR / unit_id
    unit_dir.mkdir(parents=True, exist_ok=True)
    yaml_file = unit_dir / f"{lesson_id}.yaml"
    
    print(f"\nProcessing {unit_id} ({len(cards)} cards)...")
    tasks = []
    for c in cards:
        c["status"] = "verified"
        fn_main = generate_audio_filename(c["greek"])
        c["audio"] = fn_main
        tasks.append((c["greek"], fn_main))
        
        if "example_el" in c and c["example_el"]:
            fn_ex1 = generate_audio_filename(c["example_el"])
            c["example_audio"] = fn_ex1
            tasks.append((c["example_el"], fn_ex1))
            
        if "example2_el" in c and c["example2_el"]:
            fn_ex2 = generate_audio_filename(c["example2_el"])
            c["example2_audio"] = fn_ex2
            tasks.append((c["example2_el"], fn_ex2))

    print(f"  Synthesizing audio for {len(tasks)} items using ThreadPoolExecutor(max_workers=6)...")
    synthesized_count = 0
    with ThreadPoolExecutor(max_workers=6) as executor:
        futures = {executor.submit(synthesize_item, text, fn): fn for text, fn in tasks}
        for future in as_completed(futures):
            if future.result():
                synthesized_count += 1

    print(f"  [TTS] Synthesized {synthesized_count} new audio files for {unit_id}.")
    
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
        
    print(f"  [YAML] Saved {yaml_file}")

def update_manifest(entries):
    manifest_path = CONTENT_DIR / "manifest.yaml"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f) or {}
        
    units = manifest.get("units", [])
    existing_ids = {u["id"] for u in units}
    added = 0
    for entry in entries:
        if entry["id"] not in existing_ids:
            units.append(entry)
            existing_ids.add(entry["id"])
            added += 1
            print(f"  [Manifest] Appended {entry['id']} ({entry['order']})")
        else:
            print(f"  [Manifest] {entry['id']} already exists, skipping")
            
    manifest["units"] = units
    with open(manifest_path, "w", encoding="utf-8") as f:
        yaml.dump(manifest, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"  [Manifest] Manifest updated ({added} new entries). Total: {len(units)} units.")

def main():
    print("==================================================")
    print("Generating KEG-A2 Part 2: Batch 6 (Units 11 & 12)")
    print("==================================================")
    
    u11_notes = """Unit A2P2-11 Core Notes: Πολιτισμός, Τέχνες, ΜΜΕ & Ψηφιακή Επικοινωνία
• Cultural Life & Entertainment Vocabulary:
  - Performing Arts & Exhibitions (η θεατρική παράσταση, η έκθεση ζωγραφικής, το μουσείο σύγχρονης τέχνης, το μουσικό φεστιβάλ, η πρεμιέρα, ο/η θεατής).
  - Media & Press (το δελτίο ειδήσεων, η εφημερίδα, το ενημερωτικό άρθρο, ο/η δημοσιογράφος, η ηλεκτρονική συνδρομή).
  - Digital Media & Networking (τα μέσα κοινωνικής δικτύωσης, η ανάρτηση, ο λογαριασμός χρήστη, ο κωδικός πρόσβασης, η ψηφιακή εφαρμογή, η κοινοποίηση συνδέσμου, το σχόλιο).
  - Critical Review & Personal Opinions (προτείνω ανεπιφύλακτα, εντυπωσιάστηκα από την παράσταση, παρακολουθώ τα πολιτιστικά δρώμενα)."""

    process_and_save_unit(
        unit_id="unit-a2p2-11",
        lesson_id="lesson-01",
        title="Μάθημα 11: Πολιτισμός, Τέχνες, ΜΜΕ & Ψηφιακή Επικοινωνία (Culture, Arts & Digital Media)",
        description="Mastering theater, exhibitions, cinema, news media, social networking, and expressing cultural recommendations for the KEG A2 exam.",
        lesson_notes=u11_notes,
        cards=CARDS_U11,
        order_code="KEG-A2-P2-11-A"
    )

    u12_notes = """Unit A2P2-12 Core Notes: Εξεταστική Δεξιότητα, Ορθογραφικές Παγίδες & Ολοκληρωμένη Σύνθεση
• Essential Orthography Traps & High-Scoring Writing Formulas:
  - High-frequency spelling traps: πολύ (adverb) vs πολλή (feminine adjective), -ειτε vs -είται, -τε vs -ται, irregular adjectives in -ύς/-ιά/-ύ.
  - Formal letter/email salutations & sign-offs: Αξιότιμε κύριε / Αξιότιμη κυρία, Με εκτίμηση.
  - Strategic communicative formulas: Σας γράφω για να σας ενημερώσω, Θα ήθελα να εκφράσω τα παράπονά μου, Ζητώ συγγνώμη για την αναστάτωση, Σας προτείνω να επισκεφθείτε.
  - Cohesive connectors & discourse markers: Κατά τη γνώμη μου, από τη μία πλευρά... από την άλλη πλευρά, όχι μόνο... αλλά και, σύμφωνα με, σε περίπτωση που, παρόλο που, επομένως, συνοψίζοντας, εν κατακλείδι."""

    process_and_save_unit(
        unit_id="unit-a2p2-12",
        lesson_id="lesson-01",
        title="Μάθημα 12: Εξεταστική Δεξιότητα, Ορθογραφικές Παγίδες & Ολοκληρωμένη Σύνθεση (Exam Writing Mastery & Orthography)",
        description="Conquering common spelling traps, formal letter formulas, cohesive argumentative connectors, and capstone exam synthesis for the KEG A2 certification.",
        lesson_notes=u12_notes,
        cards=CARDS_U12,
        order_code="KEG-A2-P2-12-A"
    )

    manifest_entries = [
        {
            "id": "unit-a2p2-11",
            "title": "Μάθημα 11: Πολιτισμός, Τέχνες, ΜΜΕ & Ψηφιακή Επικοινωνία (Culture, Arts & Digital Media)",
            "description": "Mastering theater, exhibitions, cinema, news media, social networking, and expressing cultural recommendations for the KEG A2 exam.",
            "order": "KEG-A2-P2-11-A",
            "total_lessons": 1,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2p2-11/lesson-01.yaml",
                    "title": "Μάθημα 11: Πολιτισμός, Τέχνες, ΜΜΕ & Ψηφιακή Επικοινωνία (Culture, Arts & Digital Media)"
                }
            ]
        },
        {
            "id": "unit-a2p2-12",
            "title": "Μάθημα 12: Εξεταστική Δεξιότητα, Ορθογραφικές Παγίδες & Ολοκληρωμένη Σύνθεση (Exam Writing Mastery & Orthography)",
            "description": "Conquering common spelling traps, formal letter formulas, cohesive argumentative connectors, and capstone exam synthesis for the KEG A2 certification.",
            "order": "KEG-A2-P2-12-A",
            "total_lessons": 1,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2p2-12/lesson-01.yaml",
                    "title": "Μάθημα 12: Εξεταστική Δεξιότητα, Ορθογραφικές Παγίδες & Ολοκληρωμένη Σύνθεση (Exam Writing Mastery & Orthography)"
                }
            ]
        }
    ]

    update_manifest(manifest_entries)
    print("\n[OK] Batch 6 finished successfully! Part 2 is 100% complete!")

if __name__ == "__main__":
    main()

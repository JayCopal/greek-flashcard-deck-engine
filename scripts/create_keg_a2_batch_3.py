# -*- coding: utf-8 -*-
"""
Generate KEG-A2 Batch 3:
- Unit A2-05: KEG-A2-05-A (35 cards) - Social Life, Invitations & Wishes (Κοινωνική Ζωή, Προσκλήσεις & Ευχές)
- Unit A2-06: KEG-A2-06-A (35 cards) - Banking, Post Office & Public Services (Συναλλαγές, Τράπεζα & ΚΕΠ)
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
# UNIT A2-05 CARDS (35 cards)
# Theme: Social Events, Invitations & Wishes (Κοινωνική Ζωή)
# -------------------------------------------------------------
CARDS_U05 = [
    {
        "id": "A2-U05-001",
        "greek": "η πρόσκληση",
        "english": "invitation",
        "notes": "Feminine noun in -η (-εις). Core text type in KEG A2 Writing Task 1 (40-50 words invitation or response).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι προσκλήσεις",
            "accusative_singular": "την πρόσκληση",
            "genitive_singular": "της πρόσκλησης",
            "verb": "προσκαλώ"
        },
        "keg_communicative_function": "Reading and writing formal and informal invitations for celebrations",
        "example_el": "Σας στέλνω αυτή την πρόσκληση για τα εγκαίνια της νέας μας έκθεσης.",
        "example_en": "I am sending you this invitation for the opening of our new exhibition.",
        "example2_el": "Λάβαμε μια όμορφη πρόσκληση για τον γάμο της Ελένης και του Γιώργου.",
        "example2_en": "We received a lovely invitation to Eleni and Giorgos's wedding."
    },
    {
        "id": "A2-U05-002",
        "greek": "προσκαλώ",
        "english": "to invite",
        "notes": "Contracted verb (προσκαλώ, προσκαλείς, προσκαλεί). Simple past: 'προσκάλεσα'. Simple future: 'θα προσκαλέσω'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "προσκάλεσα",
            "simple_future": "θα προσκαλέσω",
            "noun_derivative": "η πρόσκληση"
        },
        "keg_communicative_function": "Inviting friends, colleagues, or neighbors to social gatherings",
        "example_el": "Θα ήθελα να σας προσκαλέσω στο σπίτι μου για φαγητό το βράδυ του Σαββάτου.",
        "example_en": "I would like to invite you to my house for dinner on Saturday evening.",
        "example2_el": "Μας προσκάλεσαν σε μια μουσική εκδήλωση στο αρχαίο θέατρο.",
        "example2_en": "They invited us to a musical event at the ancient theater."
    },
    {
        "id": "A2-U05-003",
        "greek": "δέχομαι",
        "english": "to accept",
        "notes": "Deponent verb (δέχομαι, δέχεσαι, δέχεται). Simple past: 'δέχτηκα' / 'δέχθηκα'. Antonym: 'αρνούμαι'.",
        "gender_or_pos": "verb (deponent)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "δέχτηκα",
            "simple_future": "θα δεχτώ",
            "antonym": "αρνούμαι",
            "noun_derivative": "η αποδοχή"
        },
        "keg_communicative_function": "Accepting invitations gladly in Writing Task 1 responses",
        "example_el": "Δέχομαι με μεγάλη χαρά την πρόσκλησή σας και ανυπομονώ να σας δω.",
        "example_en": "I accept your invitation with great joy and look forward to seeing you.",
        "example2_el": "Ο διευθυντής δέχτηκε να συναντηθεί μαζί μας αύριο το πρωί.",
        "example2_en": "The director agreed to meet with us tomorrow morning."
    },
    {
        "id": "A2-U05-004",
        "greek": "αρνούμαι",
        "english": "to refuse / to decline",
        "notes": "Deponent verb (αρνούμαι, αρνείσαι, αρνείται). Simple past: 'αρνήθηκα'. Must be accompanied by polite apology in A2 letters.",
        "gender_or_pos": "verb (deponent)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "αρνήθηκα",
            "simple_future": "θα αρνηθώ",
            "noun_derivative": "η άρνηση"
        },
        "keg_communicative_function": "Declining an invitation politely and stating reasons in Writing Task 1",
        "example_el": "Δυστυχώς αναγκάζομαι να αρνηθώ την πρόσκληση λόγω ανειλημμένων υποχρεώσεων.",
        "example_en": "Unfortunately I am forced to decline the invitation due to prior commitments.",
        "example2_el": "Δεν μπορώ να αρνηθώ τη βοήθεια που μου προσφέρει ο φίλος μου.",
        "example2_en": "I cannot refuse the help that my friend offers me."
    },
    {
        "id": "A2-U05-005",
        "greek": "με χαρά",
        "english": "with pleasure / gladly",
        "notes": "Prepositional adverbial formula expressing enthusiastic acceptance.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "collocation": "με μεγάλη χαρά (with great pleasure)",
            "synonym": "ευχαρίστως"
        },
        "keg_communicative_function": "Accepting social invitations enthusiastically in email correspondence",
        "example_el": "Θα έρθω με χαρά στα γενέθλιά σου την επόμενη Παρασκευή!",
        "example_en": "I will come with pleasure to your birthday next Friday!",
        "example2_el": "Με μεγάλη χαρά σάς ανακοινώνουμε τη γέννηση της κόρης μας.",
        "example2_en": "With great pleasure we announce to you the birth of our daughter."
    },
    {
        "id": "A2-U05-006",
        "greek": "δυστυχώς δεν μπορώ",
        "english": "unfortunately I cannot",
        "notes": "Fixed formula for declining invitations politely before giving an excuse.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "usage": "polite refusal followed by excuse (γιατί, επειδή)"
        },
        "keg_communicative_function": "Softening refusals in formal and informal written responses",
        "example_el": "Σας ευχαριστώ πολύ για το κάλεσμα, αλλά δυστυχώς δεν μπορώ να παρευρεθώ.",
        "example_en": "Thank you very much for the invite, but unfortunately I cannot attend.",
        "example2_el": "Δυστυχώς δεν μπορώ να έρθω μαζί σας επειδή δουλεύω μέχρι αργά.",
        "example2_en": "Unfortunately I cannot come with you because I work until late."
    },
    {
        "id": "A2-U05-007",
        "greek": "η ευχή",
        "english": "wish / blessing",
        "notes": "Feminine noun in -ή (-ές). Core concept in Greek cultural etiquette.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ευχές",
            "accusative_singular": "την ευχή",
            "verb": "εύχομαι"
        },
        "keg_communicative_function": "Exchanging wishes for holidays, birthdays, and name days",
        "example_el": "Σας στέλνω τις θερμότερες ευχές μου για υγεία και ευτυχία.",
        "example_en": "I send you my warmest wishes for health and happiness.",
        "example2_el": "Τις ημέρες των εορτών ανταλλάσσουμε παραδοσιακές ευχές με φίλους και συγγενείς.",
        "example2_en": "During the holidays we exchange traditional wishes with friends and relatives."
    },
    {
        "id": "A2-U05-008",
        "greek": "χρόνια πολλά",
        "english": "happy birthday / many happy returns / happy name day",
        "notes": "Universal Greek festive greeting used on birthdays, name days, New Year, Christmas, and national holidays.",
        "gender_or_pos": "phrase (greeting)",
        "grammatical_info": {
            "part_of_speech": "formulaic greeting",
            "literal": "many years",
            "usage": "birthdays, namedays, Easter, Christmas"
        },
        "keg_communicative_function": "Congratulating celebrants on festive occasions",
        "example_el": "Χρόνια πολλά για τη γιορτή σου! Να είσαι πάντα γερός και ευτυχισμένος.",
        "example_en": "Many happy returns for your name day! May you always be healthy and happy.",
        "example2_el": "Της τηλεφώνησα για να της ευχηθώ χρόνια πολλά για τα γενέθλιά της.",
        "example2_en": "I phoned her to wish her happy birthday for her birthday."
    },
    {
        "id": "A2-U05-009",
        "greek": "καλή επιτυχία",
        "english": "good luck / every success",
        "notes": "Formulaic greeting used before tests, job interviews, or new ventures.",
        "gender_or_pos": "phrase (greeting)",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η επιτυχία",
            "adjective": "καλή"
        },
        "keg_communicative_function": "Wishing success to peers before exams or challenging tasks",
        "example_el": "Καλή επιτυχία σε όλους τους υποψηφίους στις αυριανές εξετάσεις!",
        "example_en": "Good luck to all candidates in tomorrow's examinations!",
        "example2_el": "Σου εύχομαι καλή επιτυχία στη νέα σου δουλειά.",
        "example2_en": "I wish you good luck in your new job."
    },
    {
        "id": "A2-U05-010",
        "greek": "περαστικά",
        "english": "get well soon / may it pass quickly",
        "notes": "Neuter plural adjective used as formulaic greeting to someone sick or recovering from illness/injury.",
        "gender_or_pos": "phrase (greeting)",
        "grammatical_info": {
            "part_of_speech": "formulaic greeting",
            "origin": "περαστικός (transitory)",
            "usage": "when someone is unwell or injured"
        },
        "keg_communicative_function": "Expressing sympathy and wishing prompt recovery to friends or colleagues",
        "example_el": "Έμαθα ότι είσαι άρρωστος με γρίπη. Περαστικά και γρήγορη ανάρρωση!",
        "example_en": "I heard that you are ill with the flu. Get well soon and a speedy recovery!",
        "example2_el": "Περαστικά στην αδελφή σου, ελπίζω να βγει σύντομα από το νοσοκομείο.",
        "example2_en": "Get well wishes to your sister; I hope she is discharged from the hospital soon."
    },
    {
        "id": "A2-U05-011",
        "greek": "συγχαρητήρια",
        "english": "congratulations",
        "notes": "Neuter plural noun used as exclamation. High-utility response to graduations, promotions, or passing exams.",
        "gender_or_pos": "noun (neuter plural)",
        "grammatical_info": {
            "part_of_speech": "noun (plural) / exclamation",
            "collocation": "θερμά συγχαρητήρια (warm congratulations)"
        },
        "keg_communicative_function": "Congratulating friends on academic diplomas or career advancements",
        "example_el": "Θερμά συγχαρητήρια για την επιτυχία σου στις εξετάσεις ελληνομάθειας!",
        "example_en": "Warm congratulations on your success in the Greek language examinations!",
        "example2_el": "Όλοι οι συνάδελφοι έδωσαν συγχαρητήρια στον Νίκο για την προαγωγή του.",
        "example2_en": "All colleagues offered congratulations to Nikos on his promotion."
    },
    {
        "id": "A2-U05-012",
        "greek": "να ζήσετε",
        "english": "may you live long and happily (wedding wish to the newlyweds)",
        "notes": "Fixed subjunctive formula addressed to bride and groom at Greek weddings.",
        "gender_or_pos": "phrase (wish)",
        "grammatical_info": {
            "part_of_speech": "formulaic wish",
            "syntax": "να + ζήσετε (aorist subjunctive plural of ζω)"
        },
        "keg_communicative_function": "Offering appropriate wedding congratulations in letters and conversations",
        "example_el": "Να ζήσετε και να είστε πάντα αγαπημένοι και ευτυχισμένοι!",
        "example_en": "May you live long together and always be loving and happy!",
        "example2_el": "Γράψαμε στην κάρτα του γάμου: «Να ζήσετε με υγεία και χαρά».",
        "example2_en": "We wrote on the wedding card: 'May you live long with health and joy.'"
    },
    {
        "id": "A2-U05-013",
        "greek": "να σας ζήσει",
        "english": "may your newborn live long (wish to new parents)",
        "notes": "Fixed formula addressed to parents on the birth or baptism of a child.",
        "gender_or_pos": "phrase (wish)",
        "grammatical_info": {
            "part_of_speech": "formulaic wish",
            "syntax": "να + σας (indirect clitic) + ζήσει (third person)"
        },
        "keg_communicative_function": "Congratulating parents on the arrival or christening of a child",
        "example_el": "Να σας ζήσει ο νεογέννητος γιος σας και να τον καμαρώσετε όπως επιθυμείτε!",
        "example_en": "May your newborn son live long and may you be proud of him as you desire!",
        "example2_el": "Στείλαμε λουλούδια στους νέους γονείς με την ευχή: «Να σας ζήσει!».",
        "example2_en": "We sent flowers to the new parents with the wish: 'May he/she live long!'"
    },
    {
        "id": "A2-U05-014",
        "greek": "καλή διασκέδαση",
        "english": "have fun / have a great time",
        "notes": "Formulaic farewell wish before someone goes to a party, concert, cinema, or weekend outing.",
        "gender_or_pos": "phrase (greeting)",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "noun": "η διασκέδαση",
            "verb": "διασκεδάζω"
        },
        "keg_communicative_function": "Wishing an enjoyable evening or outing to companions",
        "example_el": "Καλή διασκέδαση στη συναυλία απόψε, τα λέμε αύριο!",
        "example_en": "Have a great time at the concert tonight, see you tomorrow!",
        "example2_el": "Εύχομαι καλή διασκέδαση σε όλους σας στην αποψινή έξοδο.",
        "example2_en": "I wish everyone a wonderful time on tonight's night out."
    },
    {
        "id": "A2-U05-015",
        "greek": "τα γενέθλια",
        "english": "birthday",
        "notes": "Neuter plural noun (always plural in Greek). Collocates with 'γιορτάζω τα γενέθλιά μου'.",
        "gender_or_pos": "noun (neuter plural)",
        "grammatical_info": {
            "part_of_speech": "noun (plural only)",
            "genitive": "των γενεθλίων",
            "collocation": "τούρτα γενεθλίων (birthday cake)"
        },
        "keg_communicative_function": "Writing birthday party invitations and scheduling parties in Task 1",
        "example_el": "Το Σάββατο γιορτάζω τα γενέθλιά μου και οργανώνω ένα πάρτι στο σπίτι.",
        "example_en": "On Saturday I am celebrating my birthday and organizing a party at home.",
        "example2_el": "Σου εύχομαι ολόψυχα χρόνια πολλά για τα τριακοστά σου γενέθλια!",
        "example2_en": "I wholeheartedly wish you many happy returns for your thirtieth birthday!"
    },
    {
        "id": "A2-U05-016",
        "greek": "η ονομαστική γιορτή",
        "english": "name day celebration",
        "notes": "Feminine noun phrase. Highly celebrated social tradition in Greek culture.",
        "gender_or_pos": "noun phrase (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "plural": "οι ονομαστικές γιορτές",
            "cultural_note": "celebrated on the saint's feast day"
        },
        "keg_communicative_function": "Discussing cultural customs and congratulating friends on their name day",
        "example_el": "Στην Ελλάδα η ονομαστική γιορτή είναι συχνά πιο σημαντική από τα γενέθλια.",
        "example_en": "In Greece the name day celebration is often more important than birthdays.",
        "example2_el": "Σήμερα είναι η ονομαστική γιορτή του Γιώργου και το σπίτι είναι γεμάτο επισκέπτες.",
        "example2_en": "Today is Giorgos's name day and the house is full of visitors."
    },
    {
        "id": "A2-U05-017",
        "greek": "ο γάμος",
        "english": "wedding / marriage",
        "notes": "Masculine noun in -ος (-οι). Covers wedding ceremony and marital institution.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι γάμοι",
            "genitive_singular": "του γάμου",
            "verb": "παντρεύομαι"
        },
        "keg_communicative_function": "Interpreting wedding announcements and composing congratulatory messages",
        "example_el": "Ο γάμος θα πραγματοποιηθεί σε ένα γραφικό εκκλησάκι δίπλα στη θάλασσα.",
        "example_en": "The wedding will take place in a picturesque chapel by the sea.",
        "example2_el": "Ετοιμάζουμε τα ρούχα μας για τον γάμο των φίλων μας στην Κέρκυρα.",
        "example2_en": "We are preparing our clothes for our friends' wedding in Corfu."
    },
    {
        "id": "A2-U05-018",
        "greek": "η βάφτιση",
        "english": "christening / baptism",
        "notes": "Feminine noun in -η (-εις). Third major Greek life-cycle milestone celebration alongside wedding and birthday.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι βαφτίσεις",
            "verb": "βαφτίζω"
        },
        "keg_communicative_function": "Recognizing family event invitations and social gathering protocols",
        "example_el": "Μας κάλεσαν στη βάφτιση της ανιψιάς μου την επόμενη Κυριακή.",
        "example_en": "They invited us to my niece's christening next Sunday.",
        "example2_el": "Μετά τη βάφτιση ακολούθησε δεξίωση με φαγητό και παραδοσιακή μουσική.",
        "example2_en": "After the christening a reception followed with food and traditional music."
    },
    {
        "id": "A2-U05-019",
        "greek": "το δώρο",
        "english": "gift / present",
        "notes": "Neuter noun in -ο (-α). Collocates with 'κάνω δώρο' (to give a gift) or 'παίρνω δώρο' (to buy a gift).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα δώρα",
            "genitive_singular": "του δώρου"
        },
        "keg_communicative_function": "Discussing gifts in joint shopping negotiations (Speaking Stage 3)",
        "example_el": "Τι δώρο προτείνεις να αγοράσουμε για τα γενέθλια της Μαρίας;",
        "example_en": "What gift do you suggest we buy for Maria's birthday?",
        "example2_el": "Τους πήγαμε ένα όμορφο αναμνηστικό δώρο για το νέο τους σπίτι.",
        "example2_en": "We brought them a beautiful souvenir gift for their new home."
    },
    {
        "id": "A2-U05-020",
        "greek": "διασκεδάζω",
        "english": "to have fun / to amuse oneself",
        "notes": "Active verb. Simple past: 'διασκέδασα'. Simple future: 'θα διασκεδάσω'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "διασκέδασα",
            "simple_future": "θα διασκεδάσω",
            "noun_derivative": "η διασκέδαση"
        },
        "keg_communicative_function": "Describing party experiences and recreational outings in past narratives",
        "example_el": "Χθες το βράδυ διασκεδάσαμε πάρα πολύ με τη ζωντανή μουσική.",
        "example_en": "Yesterday evening we had a great time with the live music.",
        "example2_el": "Στην εκδρομή τα παιδιά έπαιξαν και διασκέδασαν με την ψυχή τους.",
        "example2_en": "On the excursion the children played and had fun to their heart's content."
    },
    {
        "id": "A2-U05-021",
        "greek": "περνάω καλά",
        "english": "to have a good time / to spend time nicely",
        "notes": "Idiomatic verbal locution. Past: 'πέρασα καλά'. Future: 'θα περάσω καλά'.",
        "gender_or_pos": "idiomatic phrase",
        "grammatical_info": {
            "part_of_speech": "verbal phrase",
            "past": "πέρασα καλά (I had a good time)",
            "antonym": "περνάω άσχημα"
        },
        "keg_communicative_function": "Reporting on holiday quality and social gatherings in personal letters",
        "example_el": "Περάσαμε υπέροχα στο νησί, ο καιρός ήταν θαυμάσιος και το φαγητό εξαιρετικό.",
        "example_en": "We had a wonderful time on the island; the weather was magnificent and the food superb.",
        "example2_el": "Ελπίζω να περάσετε πολύ καλά στο ταξίδι σας!",
        "example2_en": "I hope you have a very good time on your trip!"
    },
    {
        "id": "A2-U05-022",
        "greek": "κερνάω",
        "english": "to treat / to pay for someone's drink or meal",
        "notes": "Group B1 verb (κερνάω / κερνώ). Simple past: 'κέρασα'. Quintessential Greek cultural hospitality gesture.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "κέρασα",
            "simple_future": "θα κεράσω",
            "noun_derivative": "το κέρασμα"
        },
        "keg_communicative_function": "Offering to treat someone in cafe or tavern situations",
        "example_el": "Σήμερα γιορτάζω, οπότε σας κερνάω όλους καφέ και γλυκό!",
        "example_en": "Today is my name day, so I am treating you all to coffee and dessert!",
        "example2_el": "Άσε με να πληρώσω εγώ τον λογαριασμό, θέλω να σε κεράσω.",
        "example2_en": "Let me pay the bill; I want to treat you."
    },
    {
        "id": "A2-U05-023",
        "greek": "η φιλοξενία",
        "english": "hospitality",
        "notes": "Feminine noun in -α (-ες). Celebrated Greek value. Collocates with 'ευχαριστώ για τη φιλοξενία'.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "adjective": "φιλόξενος, -η, -ο",
            "genitive_singular": "της φιλοξενίας"
        },
        "keg_communicative_function": "Expressing gratitude to hosts in thank-you notes after a stay",
        "example_el": "Σας ευχαριστώ από καρδιάς για τη θερμή φιλοξενία στο σπίτι σας.",
        "example_en": "I thank you from the bottom of my heart for the warm hospitality at your home.",
        "example2_el": "Οι κάτοικοι του χωριού μάς υποδέχτηκαν με εξαιρετική φιλοξενία.",
        "example2_en": "The villagers welcomed us with extraordinary hospitality."
    },
    {
        "id": "A2-U05-024",
        "greek": "μου",
        "english": "to me (indirect weak clitic pronoun)",
        "notes": "Genitive weak personal pronoun. Placed immediately before finite verbs ('μου αρέσει', 'μου είπε') and after imperatives ('πες μου').",
        "gender_or_pos": "pronoun (clitic genitive)",
        "grammatical_info": {
            "part_of_speech": "weak personal pronoun",
            "person": "1st singular",
            "case": "genitive (indirect object)",
            "placement": "before finite verb / after imperative"
        },
        "keg_communicative_function": "Signaling recipient of information, invitations, or gifts",
        "example_el": "Μου έστειλε μήνυμα για να μου ανακοινώσει τα ευχάριστα νέα.",
        "example_en": "He sent me a message to announce the pleasant news to me.",
        "example2_el": "Πες μου σε παρακαλώ τι ώρα αρχίζει η εκδήλωση.",
        "example2_en": "Tell me please what time the event begins."
    },
    {
        "id": "A2-U05-025",
        "greek": "σου",
        "english": "to you (informal singular indirect clitic)",
        "notes": "Genitive weak personal pronoun for 2nd person singular ('σου δίνω', 'σου εύχομαι').",
        "gender_or_pos": "pronoun (clitic genitive)",
        "grammatical_info": {
            "part_of_speech": "weak personal pronoun",
            "person": "2nd singular",
            "case": "genitive (indirect object)"
        },
        "keg_communicative_function": "Addressing friends directly with wishes, news, or advice",
        "example_el": "Σου εύχομαι ολόψυχα καλή επιτυχία στις εξετάσεις σου!",
        "example_en": "I wish you wholeheartedly good luck in your examinations!",
        "example2_el": "Σου έφερα ένα μικρό δώρο από το ταξίδι μου στην Κρήτη.",
        "example2_en": "I brought you a small gift from my trip to Crete."
    },
    {
        "id": "A2-U05-026",
        "greek": "του",
        "english": "to him / to it (masculine / neuter indirect clitic)",
        "notes": "Genitive weak personal pronoun for 3rd person singular masculine and neuter.",
        "gender_or_pos": "pronoun (clitic genitive)",
        "grammatical_info": {
            "part_of_speech": "weak personal pronoun",
            "person": "3rd singular masculine/neuter",
            "case": "genitive (indirect object)"
        },
        "keg_communicative_function": "Referring to male third parties or neuter entities in social interactions",
        "example_el": "Του τηλεφώνησα χθες για να τον προσκαλέσω στο δείπνο.",
        "example_en": "I phoned him yesterday to invite him to dinner.",
        "example2_el": "Του αρέσει πολύ να δοκιμάζει παραδοσιακά ελληνικά φαγητά.",
        "example2_en": "He likes trying traditional Greek dishes very much."
    },
    {
        "id": "A2-U05-027",
        "greek": "της",
        "english": "to her (feminine indirect clitic)",
        "notes": "Genitive weak personal pronoun for 3rd person singular feminine.",
        "gender_or_pos": "pronoun (clitic genitive)",
        "grammatical_info": {
            "part_of_speech": "weak personal pronoun",
            "person": "3rd singular feminine",
            "case": "genitive (indirect object)"
        },
        "keg_communicative_function": "Directing actions and wishes to a female friend or colleague",
        "example_el": "Της έδωσα τα κλειδιά του διαμερίσματος πριν φύγω για τη δουλειά.",
        "example_en": "I gave her the keys to the apartment before leaving for work.",
        "example2_el": "Της ευχηθήκαμε όλοι χρόνια πολλά για τη γιορτή της.",
        "example2_en": "We all wished her many happy returns for her name day."
    },
    {
        "id": "A2-U05-028",
        "greek": "μας",
        "english": "to us / our",
        "notes": "Weak pronoun for 1st person plural. Can function as indirect object ('μας είπε') or possessive ('το σπίτι μας').",
        "gender_or_pos": "pronoun (clitic genitive)",
        "grammatical_info": {
            "part_of_speech": "weak personal pronoun",
            "person": "1st plural",
            "case": "genitive"
        },
        "keg_communicative_function": "Reporting communications received by a group or family",
        "example_el": "Μας εξήγησαν αναλυτικά τις λεπτομέρειες του προγράμματος.",
        "example_en": "They explained the details of the program to us comprehensively.",
        "example2_el": "Ελάτε να μας επισκεφτείτε στο νέο μας σπίτι το Σαββατοκύριακο.",
        "example2_en": "Come visit us at our new house over the weekend."
    },
    {
        "id": "A2-U05-029",
        "greek": "σας",
        "english": "to you (plural / formal singular indirect clitic)",
        "notes": "Weak pronoun for 2nd person plural or polite singular address ('σας ευχαριστώ').",
        "gender_or_pos": "pronoun (clitic genitive)",
        "grammatical_info": {
            "part_of_speech": "weak personal pronoun",
            "person": "2nd plural / polite singular",
            "case": "genitive (indirect object)"
        },
        "keg_communicative_function": "Addressing examiners, officials, or groups politely in spoken and written Greek",
        "example_el": "Σας ευχαριστώ πολύ για τη βοήθεια και την άμεση ανταπόκριση.",
        "example_en": "I thank you very much for your assistance and prompt response.",
        "example2_el": "Σας στέλνω συνημμένα τα έγγραφα που μου ζητήσατε.",
        "example2_en": "I send you attached the documents you requested from me."
    },
    {
        "id": "A2-U05-030",
        "greek": "τους",
        "english": "to them (indirect clitic pronoun)",
        "notes": "Weak pronoun for 3rd person plural indirect object ('τους είπα', 'τους έδωσα'). Distinct from accusative plural 'τους' (masculine direct).",
        "gender_or_pos": "pronoun (clitic genitive)",
        "grammatical_info": {
            "part_of_speech": "weak personal pronoun",
            "person": "3rd plural",
            "case": "genitive (indirect object)"
        },
        "keg_communicative_function": "Referring to multiple third parties in narratives and social situations",
        "example_el": "Τους είπαμε ότι θα φτάσουμε με μικρή καθυστέρηση λόγω κίνησης.",
        "example_en": "We told them that we will arrive with a slight delay due to traffic.",
        "example2_el": "Τους αρέσει να περνούν τα Σαββατοκύριακα στην εξοχή.",
        "example2_en": "They like spending weekends in the countryside."
    },
    {
        "id": "A2-U05-031",
        "greek": "το κάλεσμα",
        "english": "invitation / call",
        "notes": "Neuter noun in -μα (-ματα). Conversational synonym of 'η πρόσκληση'.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα καλέσματα",
            "synonym": "η πρόσκληση",
            "verb": "καλώ"
        },
        "keg_communicative_function": "Thanking a host warmly for a casual party invite",
        "example_el": "Σε ευχαριστώ θερμά για το κάλεσμα, θα είμαι σίγουρα εκεί!",
        "example_en": "I thank you warmly for the invite; I will definitely be there!",
        "example2_el": "Ανταποκρίθηκαν αμέσως στο κάλεσμα της γειτονιάς για τον καθαρισμό του πάρκου.",
        "example2_en": "They responded immediately to the neighborhood's call for park cleaning."
    },
    {
        "id": "A2-U05-032",
        "greek": "η αφορμή",
        "english": "occasion / pretext / reason",
        "notes": "Feminine noun in -ή (-ές). Collocates with 'με αφορμή' (on the occasion of). Standard opening formula in invitations.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι αφορμές",
            "collocation": "με αφορμή (+ αιτιατική: on the occasion of)"
        },
        "keg_communicative_function": "Stating the festive occasion of an event in Writing Task 1",
        "example_el": "Με αφορμή τα γενέθλιά μου, θα χαρώ πολύ να πιούμε ένα ποτό μαζί.",
        "example_en": "On the occasion of my birthday, I will be very glad to have a drink together.",
        "example2_el": "Η γιορτή ήταν μια εξαιρετική αφορμή για να βρεθούμε ξανά όλοι οι φίλοι.",
        "example2_en": "The celebration was an excellent occasion for all of us friends to meet again."
    },
    {
        "id": "A2-U05-033",
        "greek": "δικαιολογώ",
        "english": "to justify / to explain one's absence",
        "notes": "Group B2 verb (-ώ / -είς). In social contexts means explaining an inability to attend.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "δικαιολόγησα",
            "simple_future": "θα δικαιολογήσω",
            "noun_derivative": "η δικαιολογία"
        },
        "keg_communicative_function": "Justifying an unavoidable absence in letters of regret",
        "example_el": "Σας γράφω για να δικαιολογήσω την απουσία μου από τη χθεσινή συνάντηση.",
        "example_en": "I am writing to you to explain my absence from yesterday's meeting.",
        "example2_el": "Δικαιολόγησε την αργοπορία του αναφέροντας το μποτιλιάρισμα στους δρόμους.",
        "example2_en": "He justified his delay mentioning the traffic jam on the roads."
    },
    {
        "id": "A2-U05-034",
        "greek": "η δεξίωση",
        "english": "reception / banquet",
        "notes": "Feminine noun in -η (-εις). Formal celebratory dinner after a wedding, graduation, or official ceremony.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι δεξιώσεις",
            "genitive_singular": "της δεξίωσης"
        },
        "keg_communicative_function": "Understanding formal reception invitations and RSVP requirements",
        "example_el": "Η δεξίωση του γάμου θα πραγματοποιηθεί σε παραθαλάσσιο εστιατόριο στις εννέα.",
        "example_en": "The wedding reception will take place at a seaside restaurant at nine.",
        "example2_el": "Παρακαλούμε να επιβεβαιώσετε την παρουσία σας στη δεξίωση μέχρι το τέλος του μήνα.",
        "example2_en": "Please confirm your presence at the reception by the end of the month."
    },
    {
        "id": "A2-U05-035",
        "greek": "τα λέμε",
        "english": "see you / talk to you soon",
        "notes": "Idiomatic formulaic farewell. Variants: 'τα λέμε σύντομα', 'τα λέμε αύριο'.",
        "gender_or_pos": "phrase (farewell)",
        "grammatical_info": {
            "part_of_speech": "idiomatic phrase",
            "literal": "we say them",
            "variants": "τα λέμε σύντομα, τα λέμε από κοντά"
        },
        "keg_communicative_function": "Closing friendly notes and emails informally",
        "example_el": "Ανυπομονώ να συναντηθούμε την Κυριακή, τα λέμε!",
        "example_en": "I look forward to meeting on Sunday; see you!",
        "example2_el": "Καλή συνέχεια στη μέρα σου και τα λέμε το βράδυ στο τηλέφωνο.",
        "example2_en": "Have a good rest of your day and talk to you tonight on the phone."
    }
]

# -------------------------------------------------------------
# UNIT A2-06 CARDS (35 cards)
# Theme: Banking, Post Office & Public Services (Συναλλαγές & ΚΕΠ)
# -------------------------------------------------------------
CARDS_U06 = [
    {
        "id": "A2-U06-001",
        "greek": "ο λογαριασμός",
        "english": "bill / bank account",
        "notes": "Masculine noun in -ος (-οι). Dual meaning: utility/restaurant bill ('πληρώνω τον λογαριασμό') or bank account ('τραπεζικός λογαριασμός').",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι λογαριασμοί",
            "genitive_singular": "του λογαριασμού",
            "collocations": "λογαριασμός ρεύματος, τραπεζικός λογαριασμός"
        },
        "keg_communicative_function": "Settling utility bills and handling bank accounts in Speaking Stage 2 role-plays",
        "example_el": "Θα ήθελα να ανοίξω έναν τραπεζικό λογαριασμό ταμιευτηρίου.",
        "example_en": "I would like to open a savings bank account.",
        "example2_el": "Πήγα στο ταχυδρομείο για να πληρώσω τον λογαριασμό του νερού.",
        "example2_en": "I went to the post office to pay the water bill."
    },
    {
        "id": "A2-U06-002",
        "greek": "η κατάθεση",
        "english": "bank deposit",
        "notes": "Feminine noun in -η (-εις). Verb: 'καταθέτω' (to deposit). Antonym: 'η ανάληψη' (withdrawal).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι καταθέσεις",
            "verb": "καταθέτω",
            "antonym": "η ανάληψη"
        },
        "keg_communicative_function": "Depositing funds at bank counters and filling out deposit slips",
        "example_el": "Θέλω να κάνω μια κατάθεση χρημάτων στον λογαριασμό του ενοικίου.",
        "example_en": "I want to make a cash deposit into the rent account.",
        "example2_el": "Συμπληρώστε το έντυπο κατάθεσης με το ακριβές ποσό και την υπογραφή σας.",
        "example2_en": "Fill in the deposit form with the exact amount and your signature."
    },
    {
        "id": "A2-U06-003",
        "greek": "η ανάληψη",
        "english": "cash withdrawal",
        "notes": "Feminine noun in -η (-εις). Collocates with 'κάνω ανάληψη' (to withdraw money).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι αναλήψεις",
            "verb": "κάνω ανάληψη / σηκώνω χρήματα",
            "antonym": "η κατάθεση"
        },
        "keg_communicative_function": "Withdrawing money from bank tellers and ATM machines",
        "example_el": "Έκανα ανάληψη διακοσίων ευρώ από το μηχάνημα της τράπεζας.",
        "example_en": "I made a withdrawal of two hundred euros from the bank machine.",
        "example2_el": "Υπάρχει ημερήσιο όριο για ανάληψη μετρητών με την κάρτα σας.",
        "example2_en": "There is a daily limit for cash withdrawal with your card."
    },
    {
        "id": "A2-U06-004",
        "greek": "το ΑΤΜ",
        "english": "ATM / cash dispenser",
        "notes": "Neuter indeclinable acronym. Pronounced 'ά-τα-μα'. Essential in city navigation dialogues.",
        "gender_or_pos": "noun (neuter indeclinable)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ΑΤΜ",
            "synonym": "μηχάνημα αυτόματων συναλλαγών"
        },
        "keg_communicative_function": "Asking for and giving directions to the nearest cash dispenser",
        "example_el": "Μήπως γνωρίζετε πού βρίσκεται το κοντινότερο ΑΤΜ για ανάληψη μετρητών;",
        "example_en": "Do you happen to know where the nearest ATM is located for cash withdrawal?",
        "example2_el": "Το ΑΤΜ έξω από την τράπεζα είναι εκτός λειτουργίας αυτή τη στιγμή.",
        "example2_en": "The ATM outside the bank is out of order at the moment."
    },
    {
        "id": "A2-U06-005",
        "greek": "το υπόλοιπο",
        "english": "account balance / remainder",
        "notes": "Neuter noun in -ο (-α). Collocates with 'υπόλοιπο λογαριασμού' (account balance).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα υπόλοιπα",
            "genitive_singular": "του υπολοίπου",
            "collocation": "υπόλοιπο λογαριασμού"
        },
        "keg_communicative_function": "Inquiring about account balances at banks or over telephone banking",
        "example_el": "Θα ήθελα να ελέγξω το υπόλοιπο του τραπεζικού μου λογαριασμού.",
        "example_en": "I would like to check the balance of my bank account.",
        "example2_el": "Στην οθόνη του ΑΤΜ εμφανίστηκε το διαθέσιμο υπόλοιπο.",
        "example2_en": "On the ATM screen the available balance was displayed."
    },
    {
        "id": "A2-U06-006",
        "greek": "η συναλλαγή",
        "english": "transaction",
        "notes": "Feminine noun in -η (-ες). Core formal noun covering banking, shopping, and postal operations.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι συναλλαγές",
            "genitive_singular": "της συναλλαγής"
        },
        "keg_communicative_function": "Conducting administrative and commercial operations",
        "example_el": "Για λόγους ασφαλείας, κρατήστε την απόδειξη της συναλλαγής σας.",
        "example_en": "For security reasons, retain the receipt of your transaction.",
        "example2_el": "Η συναλλαγή ολοκληρώθηκε με επιτυχία.",
        "example2_en": "The transaction was completed successfully."
    },
    {
        "id": "A2-U06-007",
        "greek": "το ταχυδρομείο",
        "english": "post office",
        "notes": "Neuter noun in -ο (-α). Often abbreviated as 'ΕΛΤΑ' (Hellenic Post).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα ταχυδρομεία",
            "genitive_singular": "του ταχυδρομείου",
            "acronym": "ΕΛΤΑ"
        },
        "keg_communicative_function": "Seeking postal services and navigating postal branch hours",
        "example_el": "Πρέπει να πάω στο κεντρικό ταχυδρομείο για να παραλάβω ένα δέμα.",
        "example_en": "I must go to the central post office to collect a parcel.",
        "example2_el": "Μέχρι τι ώρα μένει ανοιχτό το ταχυδρομείο τις καθημερινές;",
        "example2_en": "Until what time does the post office stay open on weekdays?"
    },
    {
        "id": "A2-U06-008",
        "greek": "το δέμα",
        "english": "parcel / package",
        "notes": "Neuter noun in -μα (-ματα). Central subject in post office counter dialogues.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα δέματα",
            "genitive_singular": "του δέματος",
            "genitive_plural": "των δεμάτων"
        },
        "keg_communicative_function": "Mailing or collecting packages in service counter dialogues",
        "example_el": "Θέλω να στείλω αυτό το δέμα στην οικογένειά μου στο εξωτερικό.",
        "example_en": "I want to send this parcel to my family abroad.",
        "example2_el": "Ήρθε ειδοποίηση ότι το δέμα σας έφτασε και είναι έτοιμο για παραλαβή.",
        "example2_en": "A notification arrived that your parcel arrived and is ready for collection."
    },
    {
        "id": "A2-U06-009",
        "greek": "το γραμματόσημο",
        "english": "postage stamp",
        "notes": "Neuter noun in -ο (-α). Compound: γράμμα + σήμα.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα γραμματόσημα",
            "genitive_singular": "του γραμματοσήμου"
        },
        "keg_communicative_function": "Purchasing stamps for letters and postcards",
        "example_el": "Χρειάζομαι δύο γραμματόσημα για απλή επιστολή εσωτερικού.",
        "example_en": "I need two postage stamps for a simple domestic letter.",
        "example2_el": "Πόσο κοστίζει το γραμματόσημο για αποστολή κάρτας στη Γαλλία;",
        "example2_en": "How much does the stamp cost for sending a card to France?"
    },
    {
        "id": "A2-U06-010",
        "greek": "συστημένο",
        "english": "registered (mail)",
        "notes": "Adjective / substantivized neuter 'συστημένο'. Ensures tracked delivery.",
        "gender_or_pos": "adjective / noun",
        "grammatical_info": {
            "part_of_speech": "adjective",
            "collocation": "συστημένη επιστολή / συστημένο δέμα"
        },
        "keg_communicative_function": "Specifying tracked postal dispatch methods at service counters",
        "example_el": "Θα ήθελα να στείλω αυτό το επίσημο έγγραφο ως συστημένο.",
        "example_en": "I would like to send this official document as registered mail.",
        "example2_el": "Τα συστημένα γράμματα παραδίδονται μόνο με επίδειξη ταυτότητας και υπογραφή.",
        "example2_en": "Registered letters are delivered only upon presentation of identity and signature."
    },
    {
        "id": "A2-U06-011",
        "greek": "το ΚΕΠ",
        "english": "Citizens' Service Center (KEP)",
        "notes": "Neuter indeclinable acronym (Κέντρο Εξυπηρέτησης Πολιτών). Core Greek civic institution for certificates and legalizations.",
        "gender_or_pos": "noun (neuter indeclinable)",
        "grammatical_info": {
            "part_of_speech": "noun (acronym)",
            "full_name": "Κέντρο Εξυπηρέτησης Πολιτών"
        },
        "keg_communicative_function": "Navigating administrative paperwork at civic service centers in Greece",
        "example_el": "Μπορείτε να πάτε στο πλησιέστερο ΚΕΠ για να βγάλετε βεβαίωση κατοικίας.",
        "example_en": "You can go to the nearest KEP to obtain a certificate of residence.",
        "example2_el": "Τα ΚΕΠ εξυπηρετούν τους πολίτες με ταχύτητα και χωρίς ταλαιπωρία.",
        "example2_en": "Citizens' Service Centers serve citizens quickly and hassle-free."
    },
    {
        "id": "A2-U06-012",
        "greek": "η αίτηση",
        "english": "formal application / petition",
        "notes": "Feminine noun in -η (-εις). Core document required across public services and exam registrations.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι αιτήσεις",
            "collocation": "υποβάλλω / συμπληρώνω αίτηση",
            "genitive_singular": "της αίτησης"
        },
        "keg_communicative_function": "Submitting applications and filling administrative forms",
        "example_el": "Συμπλήρωσα την αίτηση συμμετοχής στις εξετάσεις ελληνομάθειας.",
        "example_en": "I filled in the application to participate in the Greek language examinations.",
        "example2_el": "Η προθεσμία για την υποβολή των αιτήσεων λήγει στο τέλος της εβδομάδας.",
        "example2_en": "The deadline for the submission of applications expires at the end of the week."
    },
    {
        "id": "A2-U06-013",
        "greek": "το πιστοποιητικό",
        "english": "certificate",
        "notes": "Neuter noun in -ο (-α). Essential term for the exam credential itself ('πιστοποιητικό ελληνομάθειας').",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πιστοποιητικά",
            "genitive_singular": "του πιστοποιητικού"
        },
        "keg_communicative_function": "Requesting official certifications and language credentials",
        "example_el": "Χρειάζομαι ένα πιστοποιητικό γεννήσεως μεταφρασμένο στα ελληνικά.",
        "example_en": "I need a birth certificate translated into Greek.",
        "example2_el": "Το πιστοποιητικό ελληνομάθειας αποτελεί επίσημη αναγνώριση των γλωσσικών σας δεξιοτήτων.",
        "example2_en": "The certificate of attainment in Greek constitutes official recognition of your language skills."
    },
    {
        "id": "A2-U06-014",
        "greek": "η βεβαίωση",
        "english": "attestation / statement / confirmation certificate",
        "notes": "Feminine noun in -η (-εις). Official paper attesting to attendance, residence, or employment.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι βεβαιώσεις",
            "genitive_singular": "της βεβαίωσης",
            "verb": "βεβαιώνω"
        },
        "keg_communicative_function": "Asking for proof of enrollment, employment, or residence at KEP or school",
        "example_el": "Ζήτησα από τη γραμματεία μια βεβαίωση σπουδών για την ανανέωση της κάρτας.",
        "example_en": "I asked the secretariat for a study attestation for the card renewal.",
        "example2_el": "Η βεβαίωση εργασίας αναφέρει τον μισθό και τα έτη προϋπηρεσίας.",
        "example2_en": "The employment attestation states the salary and years of previous service."
    },
    {
        "id": "A2-U06-015",
        "greek": "η ουρά",
        "english": "queue / line / wait-line",
        "notes": "Feminine noun in -ά (-ές). Collocates with 'περιμένω στην ουρά' (to wait in line).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ουρές",
            "collocation": "περιμένω στην ουρά"
        },
        "keg_communicative_function": "Waiting in service queues and asking who is last in line",
        "example_el": "Είχε μεγάλη ουρά στην τράπεζα και περίμενα σχεδόν μισή ώρα.",
        "example_en": "There was a long line at the bank and I waited nearly half an hour.",
        "example2_el": "Συγγνώμη, ποιος είναι ο τελευταίος στην ουρά;",
        "example2_en": "Excuse me, who is the last person in the line?"
    },
    {
        "id": "A2-U06-016",
        "greek": "ο αριθμός προτεραιότητας",
        "english": "queue number / priority ticket",
        "notes": "Masculine noun phrase. Taken from electronic ticket dispensers at banks, post offices, and KEP.",
        "gender_or_pos": "noun phrase (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "plural": "οι αριθμοί προτεραιότητας",
            "collocation": "παίρνω αριθμό προτεραιότητας"
        },
        "keg_communicative_function": "Understanding electronic ticketing procedures in Greek public services",
        "example_el": "Παρακαλώ πάρτε αριθμό προτεραιότητας από το μηχάνημα στην είσοδο.",
        "example_en": "Please take a priority number from the machine at the entrance.",
        "example2_el": "Όταν εμφανιστεί ο αριθμός προτεραιότητάς σας στην οθόνη, περάστε στο αντίστοιχο γκισέ.",
        "example2_en": "When your priority number appears on the screen, proceed to the corresponding counter."
    },
    {
        "id": "A2-U06-017",
        "greek": "το γκισέ",
        "english": "service counter / teller window",
        "notes": "Neuter indeclinable noun of French origin. Plural 'τα γκισέ'.",
        "gender_or_pos": "noun (neuter indeclinable)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα γκισέ",
            "synonym": "το ταμείο, η θυρίδα"
        },
        "keg_communicative_function": "Locating service desks and approaching tellers",
        "example_el": "Περάστε παρακαλώ στο γκισέ νούμερο τέσσερα για την εξυπηρέτησή σας.",
        "example_en": "Please proceed to counter number four for your assistance.",
        "example2_el": "Ο υπάλληλος πίσω από το γκισέ έλεγξε τα δικαιολογητικά μου.",
        "example2_en": "The clerk behind the counter inspected my supporting documents."
    },
    {
        "id": "A2-U06-018",
        "greek": "η εξυπηρέτηση",
        "english": "service / customer assistance",
        "notes": "Feminine noun in -η (-εις). Collocates with 'εξυπηρέτηση πελατών' (customer service).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "verb": "εξυπηρετώ",
            "collocation": "εξυπηρέτηση πολιτών / πελατών"
        },
        "keg_communicative_function": "Evaluating service quality or expressing compliments/complaints",
        "example_el": "Η εξυπηρέτηση στο συγκεκριμένο κατάστημα ήταν άψογη και ευγενική.",
        "example_en": "The service at this specific store was impeccable and polite.",
        "example2_el": "Για οποιαδήποτε απορία απευθυνθείτε στο τμήμα εξυπηρέτησης.",
        "example2_en": "For any query please contact the customer service department."
    },
    {
        "id": "A2-U06-019",
        "greek": "εξυπηρετώ",
        "english": "to serve / to assist (customers/citizens)",
        "notes": "Contracted verb (εξυπηρετώ, εξυπηρετείς, εξυπηρετεί). Passive: 'εξυπηρετούμαι'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "εξυπηρέτησα",
            "simple_future": "θα εξυπηρετήσω",
            "passive_present": "εξυπηρετούμαι"
        },
        "keg_communicative_function": "Interacting with service clerks and understanding turn announcements",
        "example_el": "Ο επόμενος παρακαλώ! Πώς μπορώ να σας εξυπηρετήσω;",
        "example_en": "Next please! How may I assist you?",
        "example2_el": "Οι πολίτες εξυπηρετούνται κατά σειρά προτεραιότητας.",
        "example2_en": "Citizens are served in order of priority."
    },
    {
        "id": "A2-U06-020",
        "greek": "ο υπάλληλος",
        "english": "clerk / employee / official",
        "notes": "Masculine noun in -ος (-οι). Feminine: 'η υπάλληλος'.",
        "gender_or_pos": "noun (masculine / feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (common gender)",
            "plural": "οι υπάλληλοι",
            "genitive_singular": "του/της υπαλλήλου",
            "genitive_plural": "των υπαλλήλων"
        },
        "keg_communicative_function": "Identifying service representatives and consulting officials",
        "example_el": "Ο υπάλληλος της τράπεζας μου εξήγησε πώς λειτουργεί η νέα εφαρμογή.",
        "example_en": "The bank clerk explained to me how the new application works.",
        "example2_el": "Ρωτήστε την αρμόδια υπάλληλο στο γραφείο πληροφοριών.",
        "example2_en": "Ask the competent employee at the information desk."
    },
    {
        "id": "A2-U06-021",
        "greek": "υπογράφω",
        "english": "to sign",
        "notes": "Verb taking direct object. Simple past: 'υπέγραψα'. Imperative: 'υπογράψτε εδώ'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "υπέγραψα",
            "simple_future": "θα υπογράψω",
            "imperative_formal": "υπογράψτε",
            "noun_derivative": "η υπογραφή"
        },
        "keg_communicative_function": "Signing contracts, forms, and receipts in administrative workflows",
        "example_el": "Παρακαλώ υπογράψτε στο κάτω μέρος της σελίδας δίπλα στην ημερομηνία.",
        "example_en": "Please sign at the bottom of the page next to the date.",
        "example2_el": "Υπέγραψα το συμβόλαιο ενοικίασης του διαμερίσματος χθες.",
        "example2_en": "I signed the rental contract for the apartment yesterday."
    },
    {
        "id": "A2-U06-022",
        "greek": "η υπογραφή",
        "english": "signature",
        "notes": "Feminine noun in -ή (-ές). Collocates with 'βάζω υπογραφή' (to put a signature).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι υπογραφές",
            "verb": "υπογράφω"
        },
        "keg_communicative_function": "Verifying required signatures on applications and test cover sheets",
        "example_el": "Χωρίς τη δική σας υπογραφή, το έγγραφο δεν θεωρείται έγκυρο.",
        "example_en": "Without your signature, the document is not considered valid.",
        "example2_el": "Βάλτε την υπογραφή σας στην απόδειξη παραλαβής του δέματος.",
        "example2_en": "Put your signature on the parcel delivery receipt."
    },
    {
        "id": "A2-U06-023",
        "greek": "το γνήσιο της υπογραφής",
        "english": "legalization / authentication of signature",
        "notes": "Fixed legal phrase in Greek public administration. Done at KEP or police stations.",
        "gender_or_pos": "noun phrase (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "institution": "performed at KEP or Police Station"
        },
        "keg_communicative_function": "Requesting official signature legalization for declarations",
        "example_el": "Χρειάζομαι το γνήσιο της υπογραφής για αυτή την υπεύθυνη δήλωση.",
        "example_en": "I need the authentication of my signature for this solemn declaration.",
        "example2_el": "Στο ΚΕΠ κάνουν το γνήσιο της υπογραφής δωρεάν με επίδειξη ταυτότητας.",
        "example2_en": "At KEP they authenticate signatures free of charge upon presentation of ID."
    },
    {
        "id": "A2-U06-024",
        "greek": "το αντίγραφο",
        "english": "copy / duplicate / photocopy",
        "notes": "Neuter noun in -ο (-α). Collocates with 'επικυρωμένο αντίγραφο' (certified copy).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα αντίγραφα",
            "collocation": "επικυρωμένο αντίγραφο"
        },
        "keg_communicative_function": "Providing required document copies in paperwork submissions",
        "example_el": "Παρακαλώ κρατήστε ένα αντίγραφο της αίτησης για το προσωπικό σας αρχείο.",
        "example_en": "Please keep a copy of the application for your personal archive.",
        "example2_el": "Χρειάζεται να καταθέσετε ένα απλό αντίγραφο του διαβατηρίου σας.",
        "example2_en": "You need to submit a simple copy of your passport."
    },
    {
        "id": "A2-U06-025",
        "greek": "παραλαμβάνω",
        "english": "to receive / to collect / to pick up",
        "notes": "Compound verb: παρά + λαμβάνω. Simple past: 'παρέλαβα'. Simple future: 'θα παραλάβω'.",
        "gender_or_pos": "verb",
        "grammatical_info": {
            "part_of_speech": "verb",
            "simple_past": "παρέλαβα",
            "simple_future": "θα παραλάβω",
            "noun_derivative": "η παραλαβή"
        },
        "keg_communicative_function": "Collecting parcels, cards, or certificates from public services",
        "example_el": "Πότε μπορώ να έρθω για να παραλάβω το νέο μου διαβατήριο;",
        "example_en": "When can I come to pick up my new passport?",
        "example2_el": "Παρέλαβα το πιστοποιητικό από τη γραμματεία σήμερα το πρωί.",
        "example2_en": "I collected the certificate from the secretariat this morning."
    },
    {
        "id": "A2-U06-026",
        "greek": "περάστε",
        "english": "come in / step forward / please proceed",
        "notes": "Imperative plural / formal polite of 'περνάω'. Standard greeting invitation from officials.",
        "gender_or_pos": "verb (imperative)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "mood": "imperative (προστακτική)",
            "register": "polite / formal",
            "singular_informal": "πέρασε"
        },
        "keg_communicative_function": "Understanding polite verbal instructions from bank tellers or examiners",
        "example_el": "Περάστε παρακαλώ, καθίστε απέναντι και δείξτε μου τα έγγραφά σας.",
        "example_en": "Please come in, sit across, and show me your documents.",
        "example2_el": "Περάστε στο ταμείο για να πληρώσετε το παράβολο.",
        "example2_en": "Proceed to the cashier to pay the administrative fee."
    },
    {
        "id": "A2-U06-027",
        "greek": "περιμένετε",
        "english": "wait / please wait",
        "notes": "Imperative plural / formal polite of 'περιμένω'. Singular: 'περίμενε'.",
        "gender_or_pos": "verb (imperative)",
        "grammatical_info": {
            "part_of_speech": "verb",
            "mood": "imperative (προστακτική)",
            "register": "polite / formal",
            "singular_informal": "περίμενε"
        },
        "keg_communicative_function": "Following staff instructions in waiting rooms and telephone queues",
        "example_el": "Περιμένετε ένα λεπτό παρακαλώ στη γραμμή μέχρι να ελέγξω τα στοιχεία σας.",
        "example_en": "Please wait a minute on the line while I check your details.",
        "example2_el": "Περιμένετε στην αίθουσα αναμονής μέχρι να φωνάξουν το όνομά σας.",
        "example2_en": "Wait in the waiting room until they call your name."
    },
    {
        "id": "A2-U06-028",
        "greek": "δείξτε μου",
        "english": "show me",
        "notes": "Imperative of 'δείχνω' + weak pronoun 'μου'. Routine demand from public officials and police.",
        "gender_or_pos": "imperative phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "δείχνω",
            "mood": "imperative",
            "clitic": "μου (indirect object placed after imperative)"
        },
        "keg_communicative_function": "Responding to requests for identity verification at gates or counters",
        "example_el": "Δείξτε μου παρακαλώ την ταυτότητα ή το διαβατήριό σας.",
        "example_en": "Show me please your identity card or your passport.",
        "example2_el": "Δείξτε μου στην οθόνη πού ακριβώς εμφανίζεται το σφάλμα.",
        "example2_en": "Show me on the screen where exactly the error appears."
    },
    {
        "id": "A2-U06-029",
        "greek": "δώστε μου",
        "english": "give me / please hand me",
        "notes": "Imperative of 'δίνω' + weak pronoun 'μου'. Polite customer request: 'δώστε μου ένα λεπτό'.",
        "gender_or_pos": "imperative phrase",
        "grammatical_info": {
            "part_of_speech": "phrase",
            "verb": "δίνω",
            "mood": "imperative",
            "register": "polite / formal"
        },
        "keg_communicative_function": "Requesting documents, time, or receipts in administrative transactions",
        "example_el": "Δώστε μου παρακαλώ τον αριθμό φορολογικού σας μητρώου.",
        "example_en": "Please give me your tax registration number (AFM).",
        "example2_el": "Δώστε μου λίγο χρόνο να συγκεντρώσω τα απαιτούμενα δικαιολογητικά.",
        "example2_en": "Give me a little time to gather the required supporting documents."
    },
    {
        "id": "A2-U06-030",
        "greek": "το παράβολο",
        "english": "administrative fee / official receipt voucher",
        "notes": "Neuter noun in -ο (-α). Fee paid for state certificates, permits, or exam participation.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα παράβολα",
            "collocation": "ηλεκτρονικό παράβολο (e-paravolo)"
        },
        "keg_communicative_function": "Paying official state administrative fees for registrations and permits",
        "example_el": "Πρέπει να πληρώσετε το ηλεκτρονικό παράβολο μέσω της τράπεζας για να ολοκληρωθεί η αίτηση.",
        "example_en": "You must pay the electronic administrative fee through the bank for the application to be completed.",
        "example2_el": "Εκδώστε το παράβολο από την ιστοσελίδα και προσκομίστε τον κωδικό πληρωμής.",
        "example2_en": "Issue the fee voucher from the website and provide the payment code."
    },
    {
        "id": "A2-U06-031",
        "greek": "τα μετρητά",
        "english": "cash",
        "notes": "Neuter plural noun (always plural). Collocates with 'πληρώνω με μετρητά' (to pay in cash).",
        "gender_or_pos": "noun (neuter plural)",
        "grammatical_info": {
            "part_of_speech": "noun (plural)",
            "contrast": "με κάρτα (by card)",
            "collocation": "πληρωμή σε μετρητά"
        },
        "keg_communicative_function": "Specifying payment by cash vs card at cash desks",
        "example_el": "Προτιμάτε να πληρώσετε με μετρητά ή με πιστωτική κάρτα;",
        "example_en": "Do you prefer to pay in cash or with a credit card?",
        "example2_el": "Δεν έχω αρκετά μετρητά μαζί μου, οπότε θα πληρώσω με την κάρτα.",
        "example2_en": "I do not have enough cash with me, so I will pay with the card."
    },
    {
        "id": "A2-U06-032",
        "greek": "η απόδειξη",
        "english": "receipt / proof",
        "notes": "Feminine noun in -η (-εις). Always provided after commercial transactions in Greece.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι αποδείξεις",
            "collocation": "απόδειξη πληρωμής / αγοράς"
        },
        "keg_communicative_function": "Requesting and checking transaction receipts in commercial dialogues",
        "example_el": "Ορίστε η απόδειξη πληρωμής και τα ρέστα σας.",
        "example_en": "Here is the payment receipt and your change.",
        "example2_el": "Κρατήστε την απόδειξη σε περίπτωση που χρειαστεί να αλλάξετε το προϊόν.",
        "example2_en": "Keep the receipt in case you need to exchange the product."
    },
    {
        "id": "A2-U06-033",
        "greek": "τα ρέστα",
        "english": "change (monetary balance returned)",
        "notes": "Neuter plural noun (always plural). Collocates with 'πάρτε τα ρέστα σας' (take your change).",
        "gender_or_pos": "noun (neuter plural)",
        "grammatical_info": {
            "part_of_speech": "noun (plural only)",
            "collocation": "κρατήστε τα ρέστα (keep the change)"
        },
        "keg_communicative_function": "Collecting monetary change in shops, taxis, and public offices",
        "example_el": "Ξεχάσατε τα ρέστα σας πάνω στο ταμείο!",
        "example_en": "You forgot your change on the counter!",
        "example2_el": "Σας έδωσα είκοσι ευρώ, οπότε περιμένω πέντε ευρώ ρέστα.",
        "example2_en": "I gave you twenty euros, so I expect five euros change."
    },
    {
        "id": "A2-U06-034",
        "greek": "η χρέωση",
        "english": "charge / fee / debit",
        "notes": "Feminine noun in -η (-εις). Relates to 'χρεώνω' (to charge). Antonym: 'η πίστωση' (credit).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι χρεώσεις",
            "verb": "χρεώνω",
            "antonym": "η πίστωση"
        },
        "keg_communicative_function": "Questioning service charges or verifying commission fees on bank transfers",
        "example_el": "Υπάρχει επιπλέον χρέωση για την άμεση μεταφορά χρημάτων σε άλλη τράπεζα;",
        "example_en": "Is there an additional charge for the immediate money transfer to another bank?",
        "example2_el": "Είδα μια άγνωστη χρέωση στον λογαριασμό μου και τηλεφώνησα στην εξυπηρέτηση.",
        "example2_en": "I saw an unknown charge on my account and phoned customer service."
    },
    {
        "id": "A2-U06-035",
        "greek": "το ωράριο λειτουργίας",
        "english": "operating hours / opening schedule",
        "notes": "Neuter noun phrase. Always posted outside Greek stores, banks, post offices, and clinics.",
        "gender_or_pos": "noun phrase (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun phrase",
            "head_noun": "το ωράριο",
            "genitive": "της λειτουργίας"
        },
        "keg_communicative_function": "Reading and understanding opening hours on public notices in Reading Part 1",
        "example_el": "Το ωράριο λειτουργίας της τράπεζας είναι από τις οκτώ το πρωί έως τις δύο το μεσημέρι.",
        "example_en": "The bank's operating hours are from eight in the morning until two in the afternoon.",
        "example2_el": "Ποιο είναι το ωράριο λειτουργίας του ταχυδρομείου το Σάββατο;",
        "example2_en": "What is the post office operating schedule on Saturday?"
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
    
    batch3_entries = [
        {
            "id": "unit-a2-05",
            "title": "Μάθημα 5: Κοινωνική Ζωή, Προσκλήσεις & Ευχές (Social Events, Invitations & Wishes)",
            "description": "Composing and replying to invitations, expressing wishes for birthdays, weddings, name days, and using weak indirect object clitic pronouns (μου, σου, του, της, μας, σας, τους) in formal and informal social interactions.",
            "order": "KEG-A2-05-A",
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2-05/lesson-01.yaml",
                    "title": "Μάθημα 5: Κοινωνική Ζωή, Προσκλήσεις & Ευχές (Social Events, Invitations & Wishes)"
                }
            ]
        },
        {
            "id": "unit-a2-06",
            "title": "Μάθημα 6: Συναλλαγές, Τράπεζα, Ταχυδρομείο & Δημόσιες Υπηρεσίες (Banking, Post Office & Public Services)",
            "description": "Navigating banking counters, ATM withdrawals, postal package dispatches, utility bills, and Citizens' Service Centers (ΚΕΠ) using polite imperatives (περάστε, περιμένετε, δείξτε μου, δώστε μου) and administrative formulas.",
            "order": "KEG-A2-06-A",
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2-06/lesson-01.yaml",
                    "title": "Μάθημα 6: Συναλλαγές, Τράπεζα, Ταχυδρομείο & Δημόσιες Υπηρεσίες (Banking, Post Office & Public Services)"
                }
            ]
        }
    ]
    
    added = 0
    for entry in batch3_entries:
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
    print("--- Starting KEG-A2 Batch 3 Generation & Parallel Synthesis ---")
    
    # 1. Unit A2-05
    u5_notes = """Unit A2-05 Core Notes: Κοινωνική Ζωή, Προσκλήσεις & Ευχές (Social Life & Etiquette)
• Indirect Object Weak Clitic Pronouns (Γενική αδύνατων αντωνυμιών):
  - Singular: μου (to me), σου (to you), του (to him/it), της (to her).
  - Plural: μας (to us), σας (to you / formal singular), τους (to them).
  - Position: immediately preceding conjugated verbs (μου στέλνει, σου εύχομαι) and immediately following imperatives (πες μου, δώστε μας).

• Formulaic Social Wishes:
  - Χρόνια πολλά (birthdays, namedays, holidays).
  - Καλή επιτυχία (exams, interviews, trials).
  - Περαστικά (illness, recovery).
  - Συγχαρητήρια (diplomas, achievements, promotions).
  - Να ζήσετε (wedding wish to newlyweds).
  - Να σας ζήσει (birth/baptism wish to parents).

• Writing Task 1 Protocol (40-50 words):
  - Polite invitation: αφορμή (occasion) + τόπος (place) + χρόνος (time).
  - Acceptance: με χαρά (with pleasure) + ανυπομονώ (look forward to).
  - Polite decline: δυστυχώς δεν μπορώ (unfortunately cannot) + δικαιολόγηση (justification)."""

    synthesize_audio_threaded(CARDS_U05, "unit-a2-05")
    save_unit_yaml(
        unit_id="unit-a2-05",
        lesson_id="lesson-01",
        title="Μάθημα 5: Κοινωνική Ζωή, Προσκλήσεις & Ευχές (Social Events, Invitations & Wishes)",
        description="Composing and replying to invitations, expressing wishes for birthdays, weddings, name days, and using weak indirect object clitic pronouns (μου, σου, του, της, μας, σας, τους) in formal and informal social interactions.",
        lesson_notes=u5_notes,
        cards=CARDS_U05
    )

    # 2. Unit A2-06
    u6_notes = """Unit A2-06 Core Notes: Συναλλαγές, Τράπεζα & Δημόσιες Υπηρεσίες (Public Services & Transactions)
• Civic & Administrative Environments:
  - Η τράπεζα: λογαριασμός (account), κατάθεση (deposit), ανάληψη (withdrawal), ΑΤΜ, υπόλοιπο (balance).
  - Το ταχυδρομείο (ΕΛΤΑ): δέμα (parcel), γραμματόσημο (stamp), συστημένο (registered mail).
  - Το ΚΕΠ (Κέντρο Εξυπηρέτησης Πολιτών): αίτηση (application), πιστοποιητικό (certificate), βεβαίωση (attestation), γνήσιο υπογραφής (signature legalization).

• Imperative Directives in Public Counters:
  - Περάστε (step forward / come in).
  - Περιμένετε (wait).
  - Δείξτε μου (show me).
  - Δώστε μου (give me).
  - Υπογράψτε (sign).

• Speaking Stage 2 Role-Play Alignment:
  - Candidate acts as customer/citizen requesting services, inquiring about costs, explaining requirements, and thanking staff."""

    synthesize_audio_threaded(CARDS_U06, "unit-a2-06")
    save_unit_yaml(
        unit_id="unit-a2-06",
        lesson_id="lesson-01",
        title="Μάθημα 6: Συναλλαγές, Τράπεζα, Ταχυδρομείο & Δημόσιες Υπηρεσίες (Banking, Post Office & Public Services)",
        description="Navigating banking counters, ATM withdrawals, postal package dispatches, utility bills, and Citizens' Service Centers (ΚΕΠ) using polite imperatives (περάστε, περιμένετε, δείξτε μου, δώστε μου) and administrative formulas.",
        lesson_notes=u6_notes,
        cards=CARDS_U06
    )

    # 3. Update manifest
    update_manifest()
    print("\n[OK] Batch 3 generation and parallel synthesis finished successfully!")

if __name__ == "__main__":
    main()

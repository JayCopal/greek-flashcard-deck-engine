# -*- coding: utf-8 -*-
"""
Generate KEG-A2 Part 2 Batch 4:
- Unit A2P2-07: KEG-A2-P2-07-A (30 cards) - Health, Emergency Notes, Medical Care & Absence Letters
- Unit A2P2-08: KEG-A2-P2-08-A (30 cards) - Weather, Environment, Holiday Excursions & Reports
Includes dual exam example sentences and multi-threaded Google Cloud Chirp-3 HD TTS.
"""
import sys
import os
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
# UNIT A2P2-07 CARDS (30 cards)
# Theme: Υγεία, Συμπτώματα, Ιατρική Φροντίδα & Επιστολές Απουσίας
# -------------------------------------------------------------
CARDS_U07 = [
    {
        "id": "A2P2-U07-001",
        "greek": "ο έντονος πονοκέφαλος",
        "english": "severe headache",
        "notes": "Adjective έντονος + compound noun πονοκέφαλος (πόνος + κεφάλι). Genitive: του έντονου πονοκεφάλου.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "masculine"},
        "keg_communicative_function": "Describing acute medical symptoms in doctor consultations and absence notes",
        "example_el": "Από το πρωί έχω έναν έντονο πονοκέφαλο και δεν μπορώ να συγκεντρωθώ.",
        "example_en": "Since morning I have a severe headache and I cannot concentrate.",
        "example2_el": "Ο γιατρός μού συνέστησε παυσίπονα για τον έντονο πονοκέφαλο.",
        "example2_en": "The doctor recommended painkillers for the severe headache."
    },
    {
        "id": "A2P2-U07-002",
        "greek": "έχω ρίγη και δέκατα",
        "english": "I have chills and low-grade fever",
        "notes": "Ρίγη (chills, neuter plural) + δέκατα (low fever 37.1 - 37.9°C). High-frequency medical idiom.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "register": "informal / conversational"},
        "keg_communicative_function": "Reporting onset of fever and chills to a physician or nurse",
        "example_el": "Αισθάνομαι αδυναμία, έχω ρίγη και δέκατα από χθες το απόγευμα.",
        "example_en": "I feel weakness, I have chills and a low-grade fever since yesterday afternoon.",
        "example2_el": "Αν έχετε ρίγη και δέκατα, καλό είναι να μετρήσετε τη θερμοκρασία σας.",
        "example2_en": "If you have chills and a low-grade fever, it is good to measure your temperature."
    },
    {
        "id": "A2P2-U07-003",
        "greek": "η ιατρική βεβαίωση",
        "english": "medical certificate / doctor's sick note",
        "notes": "Essential administrative term for excusing workplace or school absences. Genitive: της ιατρικής βεβαίωσης.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Requesting official sick leave documentation from a clinic",
        "example_el": "Χρειάζομαι μια ιατρική βεβαίωση για τη δουλειά μου επειδή έλειψα τρεις μέρες.",
        "example_en": "I need a medical certificate for my job because I was absent for three days.",
        "example2_el": "Ο γιατρός υπέγραψε την ιατρική βεβαίωση και μου την έδωσε στη γραμματεία.",
        "example2_en": "The doctor signed the medical certificate and gave it to me at the reception."
    },
    {
        "id": "A2P2-U07-004",
        "greek": "η αναρρωτική άδεια",
        "english": "sick leave / convalescence leave",
        "notes": "Adjective αναρρωτικός (convalescent) + άδεια (leave/permit). Crucial for formal work notes.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Applying for or reporting authorized sick leave to human resources",
        "example_el": "Ο γιατρός μού έδωσε πενθήμερη αναρρωτική άδεια λόγω βαριάς γρίπης.",
        "example_en": "The doctor gave me a five-day sick leave due to a severe flu.",
        "example2_el": "Έστειλα την αναρρωτική άδεια στο τμήμα προσωπικού με email.",
        "example2_en": "I sent the sick leave to the HR department by email."
    },
    {
        "id": "A2P2-U07-005",
        "greek": "παίρνω τη θεραπεία",
        "english": "to take medication / undergo prescribed therapy",
        "notes": "Collocation: παίρνω + αιτιατική θεραπεία. Regular treatment compliance.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Describing compliance with a physician's treatment plan",
        "example_el": "Πρέπει να παίρνετε τη θεραπεία σας καθημερινά μετά το πρωινό φαγητό.",
        "example_en": "You must take your treatment daily after breakfast.",
        "example2_el": "Άρχισα να παίρνω τη θεραπεία και ήδη νιώθω πολύ καλύτερα.",
        "example2_en": "I started taking the treatment and already feel much better."
    },
    {
        "id": "A2P2-U07-006",
        "greek": "το ασθενοφόρο",
        "english": "ambulance",
        "notes": "Emergency noun: ασθενής (patient) + φέρω (carry). Call 166 in Greece.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "neuter", "plural": "τα ασθενοφόρα"},
        "keg_communicative_function": "Calling emergency medical services in urgent accident dialogues",
        "example_el": "Καλέστε αμέσως το ασθενοφόρο, ο κύριος έχασε τις αισθήσεις του!",
        "example_en": "Call the ambulance immediately, the gentleman lost consciousness!",
        "example2_el": "Το ασθενοφόρο έφτασε στον τόπο του ατυχήματος μέσα σε δέκα λεπτά.",
        "example2_en": "The ambulance arrived at the accident scene within ten minutes."
    },
    {
        "id": "A2P2-U07-007",
        "greek": "οι πρώτες βοήθειες",
        "english": "first aid",
        "notes": "Always feminine plural: οι πρώτες βοήθειες (accusative: τις πρώτες βοήθειες).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine plural"},
        "keg_communicative_function": "Requesting immediate first aid or emergency hospital intake",
        "example_el": "Του πρόσφεραν τις πρώτες βοήθειες μέχρι να φτάσει ο γιατρός.",
        "example_en": "They offered him first aid until the doctor arrived.",
        "example2_el": "Πήγαμε στο τμήμα επειγόντων περιστατικών για τις πρώτες βοήθειες.",
        "example2_en": "We went to the emergency department for first aid."
    },
    {
        "id": "A2P2-U07-008",
        "greek": "η αλλεργική αντίδραση",
        "english": "allergic reaction",
        "notes": "Compound medical concept: αλλεργικός, -ή, -ό + αντίδραση. Crucial for food/pharmacy.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Reporting food or drug allergies in dining and medical environments",
        "example_el": "Έπαθε αλλεργική αντίδραση επειδή το φαγητό περιείχε ξηρούς καρπούς.",
        "example_en": "He suffered an allergic reaction because the food contained nuts.",
        "example2_el": "Έχετε κάποια αλλεργική αντίδραση σε αντιβιοτικά ή άλλα φάρμακα;",
        "example2_en": "Do you have any allergic reaction to antibiotics or other medications?"
    },
    {
        "id": "A2P2-U07-009",
        "greek": "πονάει η μέση μου",
        "english": "my lower back hurts",
        "notes": "Common orthopedic complaint: η μέση (waist/lower back). Impersonal verb πονάει.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Describing musculoskeletal pain and workplace strain",
        "example_el": "Σήκωσα ένα βαρύ κιβώτιο και από τότε πονάει αφόρητα η μέση μου.",
        "example_en": "I lifted a heavy box and since then my lower back hurts unbearably.",
        "example2_el": "Αν πονάει η μέση σας, πρέπει να αποφεύγετε την ορθοστασία.",
        "example2_en": "If your lower back hurts, you must avoid standing for long periods."
    },
    {
        "id": "A2P2-U07-010",
        "greek": "το διάστρεμμα",
        "english": "sprain / twisted ankle",
        "notes": "Neuter noun in -μα: genitive του διαστρέμματος, plural τα διαστρέμματα.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "neuter"},
        "keg_communicative_function": "Reporting minor sports or walking injuries",
        "example_el": "Έπεσα στα σκαλιά και έπαθα ένα ελαφρύ διάστρεμμα στον αστράγαλο.",
        "example_en": "I fell on the stairs and suffered a mild sprain in my ankle.",
        "example2_el": "Ο γιατρός είπε ότι είναι απλό διάστρεμμα και χρειάζεται πάγο και ξεκούραση.",
        "example2_en": "The doctor said it is a simple sprain and needs ice and rest."
    },
    {
        "id": "A2P2-U07-011",
        "greek": "η πίεση του αίματος",
        "english": "blood pressure",
        "notes": "Medical measurement: η πίεση (pressure) + γενική αίματος. Normal: κανονική πίεση.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Discussing cardiovascular health and routine pharmacy checkups",
        "example_el": "Πήγα στο φαρμακείο για να μετρήσω την πίεση του αίματός μου.",
        "example_en": "I went to the pharmacy to measure my blood pressure.",
        "example2_el": "Η πίεσή σας είναι απολύτως φυσιολογική: δώδεκα με οκτώ.",
        "example2_en": "Your blood pressure is completely normal: twelve over eight."
    },
    {
        "id": "A2P2-U07-012",
        "greek": "κάνω εξετάσεις αίματος",
        "english": "to have blood tests done",
        "notes": "Collocation: κάνω + αιτιατική πληθυντικού εξετάσεις + γενική αίματος.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Arranging or reporting laboratory blood tests",
        "example_el": "Ο παθολόγος μού ζήτησε να κάνω γενικές εξετάσεις αίματος.",
        "example_en": "The general practitioner asked me to have routine blood tests done.",
        "example2_el": "Τα αποτελέσματα από τις εξετάσεις αίματος θα βγουν αύριο το μεσημέρι.",
        "example2_en": "The results from the blood tests will come out tomorrow noon."
    },
    {
        "id": "A2P2-U07-013",
        "greek": "η συνταγή του γιατρού",
        "english": "doctor's prescription",
        "notes": "Distinguish between συνταγή μαγειρικής (recipe) and ιατρική συνταγή (prescription).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Presenting prescriptions at Greek community pharmacies",
        "example_el": "Έχετε τη συνταγή του γιατρού για να εκτελέσω τα φάρμακα;",
        "example_en": "Do you have the doctor's prescription so I can fill the medicines?",
        "example2_el": "Χωρίς ιατρική συνταγή δεν επιτρέπεται η χορήγηση αντιβίωσης.",
        "example2_en": "Without a medical prescription, dispensing antibiotics is not permitted."
    },
    {
        "id": "A2P2-U07-014",
        "greek": "το παυσίπονο χάπι",
        "english": "painkiller pill",
        "notes": "Compound adjective παυσίπονος (ending pain: παύω + πόνος) + χάπι.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "neuter"},
        "keg_communicative_function": "Purchasing over-the-counter pain medication",
        "example_el": "Πήρα ένα παυσίπονο χάπι επειδή με πονούσε τρομερά το δόντι μου.",
        "example_en": "I took a painkiller pill because my tooth was hurting terribly.",
        "example2_el": "Μην παίρνετε παυσίπονα χάπια με άδειο στομάχι.",
        "example2_en": "Do not take painkiller pills on an empty stomach."
    },
    {
        "id": "A2P2-U07-015",
        "greek": "ο επίδεσμος και το τσιρότο",
        "english": "bandage and adhesive plaster (band-aid)",
        "notes": "Pharmacy staples: ο επίδεσμος (bandage) and το τσιρότο (band-aid).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Requesting wound-dressing supplies at a pharmacy",
        "example_el": "Έκοψα το δάχτυλό μου και χρειάζομαι απολυμαντικό και ένα τσιρότο.",
        "example_en": "I cut my finger and I need antiseptic and a band-aid.",
        "example2_el": "Ο νοσοκόμος τύλιξε το τραύμα με έναν αποστειρωμένο επίδεσμο.",
        "example2_en": "The nurse wrapped the wound with a sterile bandage."
    },
    {
        "id": "A2P2-U07-016",
        "greek": "έχω στομαχικές διαταραχές",
        "english": "I have an upset stomach / stomach disturbances",
        "notes": "Adjective στομαχικός, -ή, -ό + plural noun διαταραχές (disturbances).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Describing digestive symptoms and food-related illnesses",
        "example_el": "Μάλλον έφαγα κάτι χαλασμένο και έχω έντονες στομαχικές διαταραχές.",
        "example_en": "I probably ate something spoiled and have severe stomach disturbances.",
        "example2_el": "Πιείτε ένα ζεστό χαμομήλι αν έχετε στομαχικές διαταραχές.",
        "example2_en": "Drink a warm chamomile tea if you have stomach disturbances."
    },
    {
        "id": "A2P2-U07-017",
        "greek": "η χρόνια πάθηση",
        "english": "chronic condition / chronic illness",
        "notes": "Medical history concept: χρόνιος, -α, -ο + πάθηση (illness/affection).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Providing personal medical history in hospital intake forms",
        "example_el": "Πάσχετε από κάποια χρόνια πάθηση, όπως διαβήτη ή υπέρταση;",
        "example_en": "Do you suffer from any chronic condition, such as diabetes or hypertension?",
        "example2_el": "Δεν έχω καμία χρόνια πάθηση και δεν παίρνω τακτική φαρμακευτική αγωγή.",
        "example2_en": "I do not have any chronic condition and do not take regular medication."
    },
    {
        "id": "A2P2-U07-018",
        "greek": "το βιβλιάριο υγείας",
        "english": "health insurance booklet / social security book",
        "notes": "Administrative health record: το βιβλιάριο (small book/booklet).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "neuter"},
        "keg_communicative_function": "Presenting health insurance proof at state clinics and hospitals",
        "example_el": "Πρέπει να έχετε μαζί σας την ταυτότητα και το βιβλιάριο υγείας σας.",
        "example_en": "You must have your ID and health insurance booklet with you.",
        "example2_el": "Σφράγισαν το βιβλιάριο υγείας μου στο ταμείο του νοσοκομείου.",
        "example2_en": "They stamped my health insurance booklet at the hospital cashier."
    },
    {
        "id": "A2P2-U07-019",
        "greek": "κάνω εμβόλιο",
        "english": "to get vaccinated",
        "notes": "Collocation: κάνω + εμβόλιο (vaccine). Passive: εμβολιάζομαι.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Discussing preventative vaccinations with healthcare providers",
        "example_el": "Κάθε φθινόπωρο κάνω το αντιγριπικό εμβόλιο για προστασία.",
        "example_en": "Every autumn I get the flu vaccine for protection.",
        "example2_el": "Έχετε κάνει όλα τα απαραίτητα εμβόλια για το ταξίδι σας στην Ασία;",
        "example2_en": "Have you had all the necessary vaccinations for your trip to Asia?"
    },
    {
        "id": "A2P2-U07-020",
        "greek": "το τραύμα επουλώνεται",
        "english": "the wound is healing",
        "notes": "Verb επουλώνομαι (to heal/scar over). Formal medical progression.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Describing recovery and wound healing in follow-up visits",
        "example_el": "Ο γιατρός είπε ότι το τραύμα επουλώνεται πολύ καλά και δεν έχει μόλυνση.",
        "example_en": "The doctor said that the wound is healing very well and has no infection.",
        "example2_el": "Χρειάζεται μερικές μέρες ακόμα για να επουλωθεί πλήρως το τραύμα.",
        "example2_en": "It needs a few more days for the wound to heal completely."
    },
    {
        "id": "A2P2-U07-021",
        "greek": "έχω ναυτία και ζαλάδα",
        "english": "I have nausea and dizziness",
        "notes": "Frequent travel and illness pair: η ναυτία (nausea) + η ζαλάδα (dizziness).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Describing motion sickness or sudden vertigo to travel attendants or doctors",
        "example_el": "Στο πλοίο ένιωσα έντονη ναυτία και ζαλάδα λόγω των κυμάτων.",
        "example_en": "On the ship I felt intense nausea and dizziness due to the waves.",
        "example2_el": "Αν έχετε ζαλάδα, καθίστε αμέσως κάτω και πιείτε λίγο δροσερό νερό.",
        "example2_en": "If you have dizziness, sit down immediately and drink a little cool water."
    },
    {
        "id": "A2P2-U07-022",
        "greek": "η αποχή από την εργασία",
        "english": "abstention from work / sick leave absence",
        "notes": "Formal administrative noun: η αποχή (abstention, genitive της αποχής).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Formal phrase used in official medical certificates for employment",
        "example_el": "Η γνωμάτευση του γιατρού συνιστά τριήμερη αποχή από την εργασία.",
        "example_en": "The doctor's diagnosis recommends three days' absence from work.",
        "example2_el": "Η αποχή από την εργασία κρίθηκε απαραίτητη για την πλήρη ανάρρωση του ασθενούς.",
        "example2_en": "Absence from work was deemed necessary for the patient's full recovery."
    },
    {
        "id": "A2P2-U07-023",
        "greek": "ειδοποιώ εγκαίρως",
        "english": "to notify in good time / promptly",
        "notes": "Adverb εγκαίρως (in timely fashion, on time). Polite professional expectation.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Assuring prompt notification of absence to superiors",
        "example_el": "Σας ειδοποιώ εγκαίρως ότι δεν θα μπορέσω να παραστώ στη συνάντηση.",
        "example_en": "I notify you in good time that I will not be able to attend the meeting.",
        "example2_el": "Παρακαλώ ειδοποιήστε μας εγκαίρως σε περίπτωση που ακυρώσετε το ραντεβού σας.",
        "example2_en": "Please notify us in good time in case you cancel your appointment."
    },
    {
        "id": "A2P2-U07-024",
        "greek": "η επείγουσα ανάγκη",
        "english": "urgent need / emergency situation",
        "notes": "Adjective επείγων, επείγουσα, επείγον + ανάγκη. High-stakes correspondence.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Justifying sudden departure or immediate request for assistance",
        "example_el": "Λόγω επείγουσας οικογενειακής ανάγκης, πρέπει να αναχωρήσω άμεσα.",
        "example_en": "Due to an urgent family need, I must depart immediately.",
        "example2_el": "Σε περίπτωση επείγουσας ανάγκης, μπορείτε να επικοινωνήσετε μαζί μου στο κινητό.",
        "example2_en": "In case of urgent need, you can contact me on my mobile."
    },
    {
        "id": "A2P2-U07-025",
        "greek": "αναθέτω τα καθήκοντά μου",
        "english": "to delegate / assign my duties",
        "notes": "Compound verb αναθέτω (Aorist: ανέθεσα) + τα καθήκοντα (duties/tasks).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Explaining workplace duty handover during absence in formal emails",
        "example_el": "Κατά τη διάρκεια της άδειάς μου, ανέθεσα τα καθήκοντά μου στον κύριο Παπαδόπουλο.",
        "example_en": "During my leave, I delegated my duties to Mr. Papadopoulos.",
        "example2_el": "Έχω αναθέσει τα επείγοντα καθήκοντά μου στη συνάδελφό μου, την κυρία Γεωργίου.",
        "example2_en": "I have delegated my urgent duties to my colleague, Ms. Georgiou."
    },
    {
        "id": "A2P2-U07-026",
        "greek": "η πλήρης ανάρρωση",
        "english": "full recovery / complete convalescence",
        "notes": "Adjective πλήρης, -ης, -ες + noun ανάρρωση. Standard conclusion in sick notes.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Stating prognosis and conditions for returning to normal activities",
        "example_el": "Χρειάζεται μία εβδομάδα ξεκούρασης για την πλήρη ανάρρωση από τη λοίμωξη.",
        "example_en": "It takes one week of rest for full recovery from the infection.",
        "example2_el": "Σας εύχομαι ολόψυχα γρήγορη και πλήρη ανάρρωση!",
        "example2_en": "I wish you from my heart a quick and complete recovery!"
    },
    {
        "id": "A2P2-U07-027",
        "greek": "αισθάνομαι εξαντλημένος",
        "english": "I feel exhausted",
        "notes": "Mediopassive verb αισθάνομαι + passive participle εξαντλημένος, -η, -ο.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Describing severe physical exhaustion and burnout symptoms",
        "example_el": "Δούλεψα δώδεκα ώρες συνεχόμενα και αισθάνομαι εντελώς εξαντλημένος.",
        "example_en": "I worked twelve hours continuously and feel completely exhausted.",
        "example2_el": "Ο ασθενής αισθάνεται εξαντλημένος μετά τον υψηλό πυρετό.",
        "example2_en": "The patient feels exhausted following the high fever."
    },
    {
        "id": "A2P2-U07-028",
        "greek": "η προληπτική ιατρική",
        "english": "preventative medicine",
        "notes": "Adjective προληπτικός, -ή, -ό + ιατρική. Essential public health theme in A2 texts.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Discussing health prevention, annual check-ups, and healthy lifestyle habits",
        "example_el": "Η προληπτική ιατρική και οι τακτικοί έλεγχοι σώζουν ζωές.",
        "example_en": "Preventative medicine and regular check-ups save lives.",
        "example2_el": "Στο πλαίσιο της προληπτικής ιατρικής, κάνω τσεκ-απ κάθε χρόνο.",
        "example2_en": "In the framework of preventative medicine, I do a check-up every year."
    },
    {
        "id": "A2P2-U07-029",
        "greek": "το θερμόμετρο δείχνει",
        "english": "the thermometer shows",
        "notes": "Instrumental noun το θερμόμετρο + verb δείχνει (shows/indicates).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Reporting exact fever temperature in telephone and written consultations",
        "example_el": "Το θερμόμετρο δείχνει τριάντα οκτώ και πέντε (38.5), οπότε πήρα αντιπυρετικό.",
        "example_en": "The thermometer shows thirty-eight point five (38.5), so I took an antipyretic.",
        "example2_el": "Αν το θερμόμετρο δείχνει πάνω από τριάντα εννιά, καλέστε αμέσως γιατρό.",
        "example2_en": "If the thermometer shows above thirty-nine, call a doctor immediately."
    },
    {
        "id": "A2P2-U07-030",
        "greek": "επιστρέφω στα καθήκοντά μου",
        "english": "to return to my duties / resume work",
        "notes": "Formal re-entry formula: επιστρέφω + σε + τα καθήκοντά μου. Closing sick leave notes.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Announcing official return to workplace duties after illness",
        "example_el": "Αισθάνομαι πλέον υγιής και επιστρέφω στα καθήκοντά μου τη Δευτέρα το πρωί.",
        "example_en": "I feel healthy now and return to my duties on Monday morning.",
        "example2_el": "Ανυπομονώ να επιστρέψω στα καθήκοντά μου και να συνεχίσω τη συνεργασία μας.",
        "example2_en": "I look forward to returning to my duties and continuing our collaboration."
    }
]

# -------------------------------------------------------------
# UNIT A2P2-08 CARDS (30 cards)
# Theme: Καιρός, Περιβάλλον, Εξορμήσεις & Γραπτές Αναφορές
# -------------------------------------------------------------
CARDS_U08 = [
    {
        "id": "A2P2-U08-001",
        "greek": "το δελτίο καιρού",
        "english": "weather forecast / weather bulletin",
        "notes": "Collocation: το δελτίο (bulletin) + γενική καιρού. Standard trigger in listening and writing.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Referring to official meteorological reports when planning outdoor events",
        "example_el": "Σύμφωνα με το δελτίο καιρού, το Σαββατοκύριακο θα έχει έντονες βροχές.",
        "example_en": "According to the weather forecast, on the weekend there will be heavy rains.",
        "example2_el": "Ακούσατε το δελτίο καιρού για να ξέρουμε αν θα πάμε για πεζοπορία;",
        "example2_en": "Did you listen to the weather report so we know if we will go hiking?"
    },
    {
        "id": "A2P2-U08-002",
        "greek": "η κακοκαιρία",
        "english": "bad weather / severe storm",
        "notes": "Antonym: η καλοκαιρία (fine weather). Genitive: της κακοκαιρίας.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Explaining trip cancellations or event disruptions due to severe weather",
        "example_el": "Λόγω της ξαφνικής κακοκαιρίας, όλα τα δρομολόγια των πλοίων ακυρώθηκαν.",
        "example_en": "Due to the sudden bad weather, all ferry sailings were cancelled.",
        "example2_el": "Η κακοκαιρία έπληξε τις ορεινές περιοχές με χιονοπτώσεις και κρύο.",
        "example2_en": "The bad weather hit the mountainous areas with snowfalls and cold."
    },
    {
        "id": "A2P2-U08-003",
        "greek": "η θερμοκρασία θα φτάσει",
        "english": "the temperature will reach",
        "notes": "Predictive future: θα φτάσει (from φτάνω) + degrees in accusative (τους... βαθμούς).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Stating forecast temperature peaks in letters and emails",
        "example_el": "Αύριο η θερμοκρασία θα φτάσει τους τριάντα πέντε βαθμούς Κελσίου.",
        "example_en": "Tomorrow the temperature will reach thirty-five degrees Celsius.",
        "example2_el": "Τον Ιούλιο η θερμοκρασία συχνά φτάνει σε πολύ υψηλά επίπεδα στην Αθήνα.",
        "example2_en": "In July the temperature often reaches very high levels in Athens."
    },
    {
        "id": "A2P2-U08-004",
        "greek": "πνέουν ισχυροί άνεμοι",
        "english": "strong winds are blowing",
        "notes": "Formal verb πνέω (blow) + adjective ισχυρός. Common maritime bulletin phrase.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Describing wind conditions and maritime travel safety",
        "example_el": "Στο Αιγαίο πνέουν ισχυροί άνεμοι επτά με οκτώ μποφόρ.",
        "example_en": "In the Aegean, strong winds of seven to eight Beaufort are blowing.",
        "example2_el": "Επειδή πνέουν ισχυροί άνεμοι, απαγορεύεται το άναμμα φωτιάς στο δάσος.",
        "example2_en": "Because strong winds are blowing, lighting fires in the forest is prohibited."
    },
    {
        "id": "A2P2-U08-005",
        "greek": "η ηλιοφάνεια",
        "english": "sunshine / sunny weather",
        "notes": "Compound noun: ήλιος (sun) + φαίνομαι (appear). Genitive: της ηλιοφάνειας.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Describing pleasant, sunny climate in holiday correspondence",
        "example_el": "Στην Ελλάδα έχουμε σχεδόν όλο τον χρόνο άφθονη ηλιοφάνεια.",
        "example_en": "In Greece we have abundant sunshine almost all year round.",
        "example2_el": "Η πρόγνωση προβλέπει γενικά ηλιοφάνεια με λίγες αραιές νεφώσεις.",
        "example2_en": "The forecast predicts general sunshine with a few sparse clouds."
    },
    {
        "id": "A2P2-U08-006",
        "greek": "η καταιγίδα και οι κεραυνοί",
        "english": "thunderstorm and lightning bolts",
        "notes": "Η καταιγίδα (storm) + ο κεραυνός (lightning bolt / thunderbolt, plural οι κεραυνοί).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Narrating dramatic weather incidents during outdoor activities",
        "example_el": "Μας έπιασε μια δυνατή καταιγίδα στο δρόμο και οι κεραυνοί ήταν τρομακτικοί.",
        "example_en": "A heavy thunderstorm caught us on the road and the lightning bolts were terrifying.",
        "example2_el": "Κατά τη διάρκεια της καταιγίδας μείναμε ασφαλείς μέσα στο αυτοκίνητο.",
        "example2_en": "During the thunderstorm we remained safe inside the car."
    },
    {
        "id": "A2P2-U08-007",
        "greek": "ο καύσωνας",
        "english": "heatwave",
        "notes": "Masculine noun in -ας: genitive του καύσωνα. Major recurring summer topic in Greece.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "masculine"},
        "keg_communicative_function": "Discussing summer heatwaves and health precautions in emails",
        "example_el": "Τις μέρες του καύσωνα πρέπει να πίνουμε άφθονο νερό και να μένουμε στη σκιά.",
        "example_en": "During heatwave days we must drink plenty of water and stay in the shade.",
        "example2_el": "Ο καύσωνας στην πόλη ήταν ανυπόφορος, γι' αυτό φύγαμε για τη θάλασσα.",
        "example2_en": "The heatwave in the city was unbearable, that's why we left for the sea."
    },
    {
        "id": "A2P2-U08-008",
        "greek": "η χιονόπτωση",
        "english": "snowfall",
        "notes": "Compound noun: χιόνι (snow) + πέφτω/πτώση (fall). Genitive: της χιονόπτωσης.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Describing winter mountain excursions and ski conditions",
        "example_el": "Η πυκνή χιονόπτωση κάλυψε τις στέγες όλων των σπιτιών στο χωριό.",
        "example_en": "The dense snowfall covered the roofs of all houses in the village.",
        "example2_el": "Λόγω της χιονόπτωσης, τα αυτοκίνητα χρειάζονται αντιολισθητικές αλυσίδες.",
        "example2_en": "Due to the snowfall, cars require anti-skid chains."
    },
    {
        "id": "A2P2-U08-009",
        "greek": "το φυσικό τοπίο",
        "english": "natural landscape / natural scenery",
        "notes": "Adjective φυσικός, -ή, -ό + noun τοπίο (scenery/landscape).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Praising the beauty of natural scenery in vacation narratives",
        "example_el": "Το φυσικό τοπίο στα Μετέωρα είναι πραγματικά μοναδικό στον κόσμο.",
        "example_en": "The natural landscape in Meteora is truly unique in the world.",
        "example2_el": "Μείναμε έκπληκτοι από την άγρια ομορφιά του φυσικού τοπίου.",
        "example2_en": "We were amazed by the wild beauty of the natural landscape."
    },
    {
        "id": "A2P2-U08-010",
        "greek": "ο εθνικός δρυμός",
        "english": "national park / protected forest reserve",
        "notes": "Ecological term: ο δρυμός (oak forest/national reserve). E.g. Εθνικός Δρυμός Ολύμπου.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "masculine"},
        "keg_communicative_function": "Describing eco-tourism, hiking trips, and environmental protection",
        "example_el": "Κάναμε πεζοπορία στον Εθνικό Δρυμό της Πάρνηθας και είδαμε ελάφια.",
        "example_en": "We hiked in the National Park of Parnitha and saw deer.",
        "example2_el": "Απαγορεύεται το κάμπινγκ και το άναμμα φωτιάς μέσα στον εθνικό δρυμό.",
        "example2_en": "Camping and lighting fires inside the national park are prohibited."
    },
    {
        "id": "A2P2-U08-011",
        "greek": "η προστασία του περιβάλλοντος",
        "english": "environmental protection",
        "notes": "Noun η προστασία + γενική ουδετέρου του περιβάλλοντος. Frequent discursive theme.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Discussing recycling, sustainability, and nature preservation in exams",
        "example_el": "Η προστασία του περιβάλλοντος είναι ευθύνη όλων των πολιτών.",
        "example_en": "Environmental protection is the responsibility of all citizens.",
        "example2_el": "Στο σχολείο οργανώνουμε δράσεις για την προστασία του θαλάσσιου περιβάλλοντος.",
        "example2_en": "At school we organize actions for the protection of the marine environment."
    },
    {
        "id": "A2P2-U08-012",
        "greek": "η ανακύκλωση σκουπιδιών",
        "english": "waste recycling / garbage recycling",
        "notes": "Noun η ανακύκλωση + γενική πληθυντικού σκουπιδιών (των σκουπιδιών).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Describing green habits and civic recycling responsibilities",
        "example_el": "Στη γειτονιά μας έχουμε μπλε κάδους για την ανακύκλωση χαρτιού και γυαλιού.",
        "example_en": "In our neighborhood we have blue bins for recycling paper and glass.",
        "example2_el": "Πρέπει να μάθουμε στα παιδιά τη σημασία της ανακύκλωσης σκουπιδιών.",
        "example2_en": "We must teach children the importance of waste recycling."
    },
    {
        "id": "A2P2-U08-013",
        "greek": "οι ανανεώσιμες πηγές ενέργειας",
        "english": "renewable energy sources",
        "notes": "Modern green term: ανανεώσιμος, -η, -ο (renewable) + πηγές (sources) + ενέργειας.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine plural"},
        "keg_communicative_function": "Referring to solar panels and wind energy in A2 reading texts",
        "example_el": "Η Ελλάδα επενδύει στις ανανεώσιμες πηγές ενέργειας, όπως η ηλιακή και η αιολική.",
        "example_en": "Greece invests in renewable energy sources, such as solar and wind.",
        "example2_el": "Τα φωτοβολταϊκά πάνελ είναι μια σημαντική ανανεώσιμη πηγή ενέργειας.",
        "example2_en": "Photovoltaic panels are an important renewable source of energy."
    },
    {
        "id": "A2P2-U08-014",
        "greek": "η αμμουδερή ακτή",
        "english": "sandy coast / sandy shoreline",
        "notes": "Adjective αμμουδερός, -ή, -ό (sandy, from άμμος) + ακτή (coastline).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Describing beach terrain and swimming destinations in travel writing",
        "example_el": "Το ξενοδοχείο βρισκόταν ακριβώς μπροστά σε μια απέραντη αμμουδερή ακτή.",
        "example_en": "The hotel was located right in front of an endless sandy coast.",
        "example2_el": "Περπατήσαμε κατά μήκος της αμμουδερής ακτής την ώρα του ηλιοβασιλέματος.",
        "example2_en": "We walked along the sandy coast at sunset."
    },
    {
        "id": "A2P2-U08-015",
        "greek": "τα κρυστάλλινα νερά",
        "english": "crystal-clear waters",
        "notes": "Classic Greek sea collocation: κρυστάλλινος, -η, -ο + νερά (waters).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter plural"},
        "keg_communicative_function": "Praising sea quality and pristine swimming spots in holiday letters",
        "example_el": "Η παραλία είχε κρυστάλλινα νερά και λευκό βότσαλο.",
        "example_en": "The beach had crystal-clear waters and white pebbles.",
        "example2_el": "Όλοι ενθουσιάστηκαν με τα πεντακάθαρα, κρυστάλλινα νερά του όρμου.",
        "example2_en": "Everyone was thrilled with the spotless, crystal-clear waters of the cove."
    },
    {
        "id": "A2P2-U08-016",
        "greek": "το φαράγγι",
        "english": "gorge / canyon",
        "notes": "Neuter noun: το φαράγγι (plural: τα φαράγγια). Famous example: Φαράγγι της Σαμαριάς.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "neuter"},
        "keg_communicative_function": "Recounting hiking and trekking adventures through gorges",
        "example_el": "Διασχίσαμε το περίφημο φαράγγι της Σαμαριάς σε έξι ώρες.",
        "example_en": "We crossed the famous Samaria gorge in six hours.",
        "example2_el": "Το μονοπάτι μέσα στο φαράγγι ήταν απαιτητικό αλλά εντυπωσιακό.",
        "example2_en": "The path through the gorge was demanding but impressive."
    },
    {
        "id": "A2P2-U08-017",
        "greek": "η ορεινή πεζοπορία",
        "english": "mountain hiking / mountain trekking",
        "notes": "Adjective ορεινός, -ή, -ό (mountainous, from όρος) + πεζοπορία (hiking, from πεζός + πορεία).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Describing outdoor leisure hobbies and mountain expeditions",
        "example_el": "Η ορεινή πεζοπορία είναι ο καλύτερος τρόπος για να απολαύσεις τη φύση.",
        "example_en": "Mountain hiking is the best way to enjoy nature.",
        "example2_el": "Χρειαζόμαστε ειδικά παπούτσια και σακίδιο για την ορεινή πεζοπορία.",
        "example2_en": "We need special shoes and a backpack for mountain hiking."
    },
    {
        "id": "A2P2-U08-018",
        "greek": "η χερσόνησος",
        "english": "peninsula",
        "notes": "Feminine noun ending in -ος (second declension feminine): η χερσόνησος, της χερσονήσου.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Referring to Greek geography (e.g. Πελοπόννησος, Χαλκιδική)",
        "example_el": "Η Πελοπόννησος είναι μια ιστορική χερσόνησος με αμέτρητα αξιοθέατα.",
        "example_en": "The Peloponnese is a historic peninsula with countless sights.",
        "example2_el": "Επισκεφτήκαμε τις τρεις χερσονήσους της Χαλκιδικής το περασμένο καλοκαίρι.",
        "example2_en": "We visited the three peninsulas of Chalkidiki last summer."
    },
    {
        "id": "A2P2-U08-019",
        "greek": "ο αρχαιολογικός χώρος",
        "english": "archaeological site",
        "notes": "Adjective αρχαιολογικός, -ή, -ό + χώρος. Plural: οι αρχαιολογικοί χώροι.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "masculine"},
        "keg_communicative_function": "Describing visits to historical landmarks and ancient ruins",
        "example_el": "Ο αρχαιολογικός χώρος των Δελφών ήταν γεμάτος τουρίστες από όλο τον κόσμο.",
        "example_en": "The archaeological site of Delphi was full of tourists from all over the world.",
        "example2_el": "Το εισιτήριο για τον αρχαιολογικό χώρο περιλαμβάνει και την είσοδο στο μουσείο.",
        "example2_en": "The ticket for the archaeological site also includes admission to the museum."
    },
    {
        "id": "A2P2-U08-020",
        "greek": "το γραφικό λιμανάκι",
        "english": "picturesque small harbor",
        "notes": "Diminutive neuter: το λιμάνι -> το λιμανάκι + adjective γραφικός, -ή, -ό.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Describing romantic, authentic island settings in letters and postcards",
        "example_el": "Καθίσαμε για ουζομεζέδες σε μια ταβερνούλα στο γραφικό λιμανάκι του νησιού.",
        "example_en": "We sat for ouzo and meze at a small tavern in the picturesque harbor of the island.",
        "example2_el": "Τα ψαροκάικα ήταν αραγμένα στο ήσυχο, γραφικό λιμανάκι.",
        "example2_en": "The fishing boats were moored in the quiet, picturesque small harbor."
    },
    {
        "id": "A2P2-U08-021",
        "greek": "η πυρκαγιά στο δάσος",
        "english": "forest fire / wildfire",
        "notes": "Noun η πυρκαγιά (wildfire, from πυρ + καίω). Major summer natural hazard.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Reporting emergency environmental news and fire prevention precautions",
        "example_el": "Η πυροσβεστική υπηρεσία έσβησε την πυρκαγιά στο δάσος πριν φτάσει στα σπίτια.",
        "example_en": "The fire service extinguished the forest fire before it reached the houses.",
        "example2_el": "Το καλοκαίρι ο κίνδυνος για πυρκαγιά στο δάσος είναι ιδιαίτερα υψηλός.",
        "example2_en": "In summer the risk of a forest fire is particularly high."
    },
    {
        "id": "A2P2-U08-022",
        "greek": "η ξηρασία και η λειψυδρία",
        "english": "drought and water shortage",
        "notes": "Environmental pairing: η ξηρασία (drought, from ξηρός) + η λειψυδρία (lack of water).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Discussing climatic challenges and water conservation on Greek islands",
        "example_el": "Η παρατεταμένη ξηρασία προκάλεσε σοβαρή λειψυδρία σε πολλά μικρά νησιά.",
        "example_en": "The prolonged drought caused severe water shortages on many small islands.",
        "example2_el": "Πρέπει να κάνουμε οικονομία στο νερό για να αποφύγουμε τη λειψυδρία.",
        "example2_en": "We must conserve water to avoid water shortages."
    },
    {
        "id": "A2P2-U08-023",
        "greek": "το ηλιοβασίλεμα στη θάλασσα",
        "english": "sunset over the sea",
        "notes": "Compound noun: ήλιος + βασίλεμα (setting). Quintessential Greek postcard phrase.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Evoking romantic aesthetic impressions in personal vacation writing",
        "example_el": "Θαυμάσαμε το μαγευτικό ηλιοβασίλεμα στη θάλασσα από την καλντέρα της Σαντορίνης.",
        "example_en": "We admired the magical sunset over the sea from the caldera of Santorini.",
        "example2_el": "Τραβήξαμε υπέροχες φωτογραφίες καθώς το ηλιοβασίλεμα στη θάλασσα έβαφε τον ουρανό κόκκινο.",
        "example2_en": "We took wonderful photos as the sunset over the sea dyed the sky red."
    },
    {
        "id": "A2P2-U08-024",
        "greek": "η χλωρίδα και η πανίδα",
        "english": "flora and fauna",
        "notes": "Scientific and environmental pair: η χλωρίδα (plant life) + η πανίδα (animal life).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Describing biodiversity and ecosystem riches in environmental articles",
        "example_el": "Η πλούσια χλωρίδα και πανίδα του βουνού προστατεύεται από ευρωπαϊκούς νόμους.",
        "example_en": "The rich flora and fauna of the mountain are protected by European laws.",
        "example2_el": "Στην περιοχή συναντάμε σπάνια είδη της ελληνικής χλωρίδας και πανίδας.",
        "example2_en": "In the area we encounter rare species of Greek flora and fauna."
    },
    {
        "id": "A2P2-U08-025",
        "greek": "η καλοκαιρινή μπόρα",
        "english": "summer downpour / sudden shower",
        "notes": "Noun η μπόρα (sudden heavy rain shower, genitive της μπόρας).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Describing brief weather disruptions during summer travels",
        "example_el": "Μια ξαφνική καλοκαιρινή μπόρα δρόσισε την ατμόσφαιρα αλλά κράτησε μόνο δέκα λεπτά.",
        "example_en": "A sudden summer downpour cooled the atmosphere but lasted only ten minutes.",
        "example2_el": "Μπήκαμε σε ένα υπόστεγο για να προστατευτούμε από τη δυνατή μπόρα.",
        "example2_en": "We stepped under an awning to protect ourselves from the heavy downpour."
    },
    {
        "id": "A2P2-U08-026",
        "greek": "το ορεινό καταφύγιο",
        "english": "mountain refuge / alpine shelter",
        "notes": "Adjective ορεινός + noun το καταφύγιο (refuge/shelter). Overnight hiking base.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Narrating overnight hiking stops and alpine accommodation",
        "example_el": "Διανυκτερεύσαμε στο ορεινό καταφύγιο του Ολύμπου σε υψόμετρο δύο χιλιάδων μέτρων.",
        "example_en": "We stayed overnight at the mountain refuge of Olympus at an altitude of two thousand meters.",
        "example2_el": "Το ορεινό καταφύγιο πρόσφερε ζεστή σούπα και τζάκι στους κουρασμένους ορειβάτες.",
        "example2_en": "The mountain refuge offered hot soup and a fireplace to the tired climbers."
    },
    {
        "id": "A2P2-U08-027",
        "greek": "η θαλάσσια ρύπανση",
        "english": "marine pollution",
        "notes": "Adjective θαλάσσιος, -α, -ο + noun η ρύπανση (pollution, genitive της ρύπανσης).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Addressing plastic waste and coastal cleanliness in exam prompts",
        "example_el": "Τα πλαστικά απορρίμματα αποτελούν τη μεγαλύτερη απειλή για τη θαλάσσια ρύπανση.",
        "example_en": "Plastic waste constitutes the greatest threat regarding marine pollution.",
        "example2_el": "Εθελοντές καθάρισαν την ακτή στο πλαίσιο δράσης κατά της θαλάσσιας ρύπανσης.",
        "example2_en": "Volunteers cleaned the coast as part of an initiative against marine pollution."
    },
    {
        "id": "A2P2-U08-028",
        "greek": "το αγροτουριστικό κατάλυμα",
        "english": "agritourism lodging / rural farm stay",
        "notes": "Modern travel trend: αγροτουριστικός, -ή, -ό + κατάλυμα (lodging/accommodation).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Describing authentic rural farm stays and local organic gastronomy",
        "example_el": "Μείναμε σε ένα παραδοσιακό αγροτουριστικό κατάλυμα όπου μαζεύαμε μόνοι μας φρούτα.",
        "example_en": "We stayed at a traditional agritourism lodging where we picked fruits ourselves.",
        "example2_el": "Ο αγροτουρισμός προσφέρει αυθεντική επαφή με τον παραδοσιακό τρόπο ζωής του χωριού.",
        "example2_en": "Agritourism offers authentic contact with the traditional village way of life."
    },
    {
        "id": "A2P2-U08-029",
        "greek": "η ομίχλη περιόρισε την ορατότητα",
        "english": "the fog reduced visibility",
        "notes": "Aorist of περιορίζω (περιόρισε) + noun η ορατότητα (visibility). Transportation alert.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Reporting road or flight transit conditions in weather narratives",
        "example_el": "Η πυκνή πρωινή ομίχλη περιόρισε την ορατότητα στον αυτοκινητόδρομο στα πενήντα μέτρα.",
        "example_en": "The dense morning fog reduced visibility on the highway to fifty meters.",
        "example2_el": "Οδηγούσαμε εξαιρετικά αργά επειδή η ομίχλη περιόρισε την ορατότητα.",
        "example2_en": "We were driving extremely slowly because the fog reduced visibility."
    },
    {
        "id": "A2P2-U08-030",
        "greek": "οι κλιματικές αλλαγές",
        "english": "climate changes / global climate shifts",
        "notes": "Adjective κλιματικός, -ή, -ό + plural noun αλλαγές. Dominant CEFR A2 reading topic.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine plural"},
        "keg_communicative_function": "Discussing global warming and extreme weather patterns in tests",
        "example_el": "Οι κλιματικές αλλαγές προκαλούν συχνότερα ακραία καιρικά φαινόμενα παγκοσμίως.",
        "example_en": "Climate changes cause more frequent extreme weather events worldwide.",
        "example2_el": "Πρέπει να λάβουμε άμεσα μέτρα για να αντιμετωπίσουμε τις κλιματικές αλλαγές.",
        "example2_en": "We must take immediate measures to tackle climate changes."
    }
]

def synthesize_item(text: str, filename: str) -> bool:
    if not text:
        return False
    out_file = AUDIO_DIR / filename
    if out_file.exists() and out_file.stat().st_size > 0:
        return False
    try:
        audio_bytes = synthesize_greek_chirp(text)
        with open(out_file, "wb") as f:
            f.write(audio_bytes)
        return True
    except Exception as e:
        print(f"    [ERR] {text[:30]}: {e}")
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
        
        fn_ex1 = generate_audio_filename(c["example_el"])
        c["example_audio"] = fn_ex1
        tasks.append((c["example_el"], fn_ex1))
        
        fn_ex2 = generate_audio_filename(c["example2_el"])
        c["example2_audio"] = fn_ex2
        tasks.append((c["example2_el"], fn_ex2))

    print(f"  Synthesizing audio for {len(tasks)} items using ThreadPoolExecutor(max_workers=8)...")
    synthesized_count = 0
    with ThreadPoolExecutor(max_workers=8) as executor:
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

def update_manifest(new_units: list):
    manifest_path = CONTENT_DIR / "manifest.yaml"
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)
        
    units = manifest.get("units", [])
    existing_ids = {u["id"] for u in units}
    
    added = 0
    for entry in new_units:
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
    print("Generating KEG-A2 Part 2: Batch 4 (Units 07 & 08)")
    print("==================================================")
    
    u07_notes = """Unit A2P2-07 Core Notes: Υγεία, Συμπτώματα & Επιστολές Απουσίας
• Medical Emergency & Workplace Absence Framework:
  - Explaining acute symptoms to doctors (έχω ρίγη και δέκατα, πονάει η μέση μου, έντονος πονοκέφαλος).
  - Formal administrative sick leave (η ιατρική βεβαίωση, η αναρρωτική άδεια, η αποχή από την εργασία).
  - Workplace delegation & emergency contacts (αναθέτω τα καθήκοντά μου, ειδοποιώ εγκαίρως)."""

    process_and_save_unit(
        unit_id="unit-a2p2-07",
        lesson_id="lesson-01",
        title="Μάθημα 7: Υγεία, Συμπτώματα & Ιατρική Φροντίδα (Health, Symptoms & Medical Care)",
        description="Describing acute medical symptoms, doctor consultations, prescription handling, and writing official workplace or school absence notes.",
        lesson_notes=u07_notes,
        cards=CARDS_U07,
        order_code="KEG-A2-P2-07-A"
    )

    u08_notes = """Unit A2P2-08 Core Notes: Καιρός, Περιβάλλον & Εξορμήσεις
• Environmental & Meteorological Framework:
  - Weather bulletins and trip logistics (το δελτίο καιρού, η κακοκαιρία, η θερμοκρασία θα φτάσει).
  - Landscape and outdoor recreation descriptions (το φυσικό τοπίο, τα κρυστάλλινα νερά, η αμμουδερή ακτή, το φαράγγι).
  - Ecological awareness in A2 texts (η προστασία του περιβάλλοντος, η ανακύκλωση, οι ανανεώσιμες πηγές)."""

    process_and_save_unit(
        unit_id="unit-a2p2-08",
        lesson_id="lesson-01",
        title="Μάθημα 8: Καιρός, Περιβάλλον & Γεωγραφία (Weather, Environment & Nature)",
        description="Understanding weather bulletins, seasonal forecasts, environmental protection concepts, and describing Greek geography and outdoor excursions.",
        lesson_notes=u08_notes,
        cards=CARDS_U08,
        order_code="KEG-A2-P2-08-A"
    )

    manifest_entries = [
        {
            "id": "unit-a2p2-07",
            "title": "Μάθημα 7: Υγεία, Συμπτώματα & Ιατρική Φροντίδα (Health, Symptoms & Medical Care)",
            "description": "Describing acute medical symptoms, doctor consultations, prescription handling, and writing official workplace or school absence notes.",
            "order": "KEG-A2-P2-07-A",
            "total_lessons": 1,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2p2-07/lesson-01.yaml",
                    "title": "Μάθημα 7: Υγεία, Συμπτώματα & Ιατρική Φροντίδα (Health, Symptoms & Medical Care)"
                }
            ]
        },
        {
            "id": "unit-a2p2-08",
            "title": "Μάθημα 8: Καιρός, Περιβάλλον & Γεωγραφία (Weather, Environment & Nature)",
            "description": "Understanding weather bulletins, seasonal forecasts, environmental protection concepts, and describing Greek geography and outdoor excursions.",
            "order": "KEG-A2-P2-08-A",
            "total_lessons": 1,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2p2-08/lesson-01.yaml",
                    "title": "Μάθημα 8: Καιρός, Περιβάλλον & Γεωγραφία (Weather, Environment & Nature)"
                }
            ]
        }
    ]

    update_manifest(manifest_entries)
    print("\n[OK] Batch 4 finished successfully!")

if __name__ == "__main__":
    main()

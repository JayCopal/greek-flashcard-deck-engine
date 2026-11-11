# -*- coding: utf-8 -*-
"""
Generate KEG-A2 Part 2 Batch 5:
- Unit A2P2-09: KEG-A2-P2-09-A (30 cards) - Workplace Communication, Job Seeking & Professional Duties
- Unit A2P2-10: KEG-A2-P2-10-A (30 cards) - Education, Language Learning & Academic Applications
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
# UNIT A2P2-09 CARDS (30 cards)
# Theme: Εργασία, Επαγγελματικές Σχέσεις & Καριέρα
# -------------------------------------------------------------
CARDS_U09 = [
    {
        "id": "A2P2-U09-001",
        "greek": "η συνέντευξη εργασίας",
        "english": "job interview",
        "notes": "Compound collocation: η συνέντευξη + γενική εργασίας. Core professional milestone.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Discussing job interviews and candidate selection in spoken/written contexts",
        "example_el": "Αύριο το πρωί έχω μια κρίσιμη συνέντευξη εργασίας για τη θέση του γραμματέα.",
        "example_en": "Tomorrow morning I have a crucial job interview for the secretary position.",
        "example2_el": "Στη συνέντευξη εργασίας μού ζήτησαν να περιγράψω την επαγγελματική μου εμπειρία.",
        "example2_en": "In the job interview they asked me to describe my professional experience."
    },
    {
        "id": "A2P2-U09-002",
        "greek": "η αγγελία πρόσληψης",
        "english": "job hiring advertisement / recruitment ad",
        "notes": "Noun η αγγελία + γενική της πρόσληψης (from προσλαμβάνω).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Reading and responding to employment classified ads in newspapers and portals",
        "example_el": "Είδα την αγγελία πρόσληψης στην εφημερίδα και έστειλα αμέσως το βιογραφικό μου.",
        "example_en": "I saw the hiring ad in the newspaper and sent my CV immediately.",
        "example2_el": "Η αγγελία πρόσληψης αναφέρει ότι απαιτείται πολύ καλή γνώση ελληνικών.",
        "example2_en": "The hiring ad states that very good knowledge of Greek is required."
    },
    {
        "id": "A2P2-U09-003",
        "greek": "η σύμβαση ορισμένου χρόνου",
        "english": "fixed-term employment contract",
        "notes": "Legal contract type: ορισμένος χρόνος (fixed/determinate term). Opposite: αορίστου χρόνου.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Discussing contract duration and employment conditions",
        "example_el": "Υπέγραψα εξάμηνη σύμβαση ορισμένου χρόνου με δυνατότητα ανανέωσης.",
        "example_en": "I signed a six-month fixed-term contract with possibility of renewal.",
        "example2_el": "Οι εργαζόμενοι με σύμβαση ορισμένου χρόνου έχουν τα ίδια δικαιώματα άδειας.",
        "example2_en": "Workers on fixed-term contracts have the same leave entitlements."
    },
    {
        "id": "A2P2-U09-004",
        "greek": "η σύμβαση αορίστου χρόνου",
        "english": "permanent / indefinite-term employment contract",
        "notes": "Noun η σύμβαση + γενική αορίστου χρόνου. Indicates permanent tenure.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Stating permanent job status and career stability",
        "example_el": "Μετά από δύο χρόνια δουλειάς, μου πρόσφεραν σύμβαση αορίστου χρόνου.",
        "example_en": "After two years of work, they offered me a permanent contract.",
        "example2_el": "Η σύμβαση αορίστου χρόνου προσφέρει μεγαλύτερη ασφάλεια στον εργαζόμενο.",
        "example2_en": "The permanent contract offers greater security to the employee."
    },
    {
        "id": "A2P2-U09-005",
        "greek": "το ωράριο πλήρους απασχόλησης",
        "english": "full-time working hours",
        "notes": "Genitive: πλήρους (full) + απασχόλησης (employment). Opposite: μερικής απασχόλησης.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Specifying full-time vs. part-time work schedules",
        "example_el": "Εργάζομαι με ωράριο πλήρους απασχόλησης, σαράντα ώρες την εβδομάδα.",
        "example_en": "I work on a full-time schedule, forty hours per week.",
        "example2_el": "Η θέση αφορά ωράριο πλήρους απασχόλησης με πρωινές βάρδιες.",
        "example2_en": "The position concerns full-time hours with morning shifts."
    },
    {
        "id": "A2P2-U09-006",
        "greek": "η μερική απασχόληση",
        "english": "part-time employment",
        "notes": "Adjective μερικός, -ή, -ό (partial/part) + noun απασχόληση.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Applying for or describing student or part-time work arrangements",
        "example_el": "Ως φοιτητής, αναζητώ εργασία μερικής απασχόλησης για τα απογεύματα.",
        "example_en": "As a student, I am looking for part-time work for the afternoons.",
        "example2_el": "Η μερική απασχόληση μού επιτρέπει να συνδυάζω τις σπουδές με τη δουλειά.",
        "example2_en": "Part-time employment allows me to combine studies with work."
    },
    {
        "id": "A2P2-U09-007",
        "greek": "οι υπερωρίες πληρώνονται",
        "english": "overtime hours are paid",
        "notes": "Plural feminine noun: οι υπερωρίες (overtime: υπέρ + ώρα). Verb πληρώνονται (passive).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Inquiring about overtime compensation in employment negotiations",
        "example_el": "Στην εταιρεία μας όλες οι υπερωρίες πληρώνονται με επιπλέον ποσοστό.",
        "example_en": "In our company all overtime hours are paid with an extra percentage.",
        "example2_el": "Έκανα δέκα ώρες υπερωρίες αυτό τον μήνα για να ολοκληρώσω το έργο.",
        "example2_en": "I did ten hours of overtime this month to complete the project."
    },
    {
        "id": "A2P2-U09-008",
        "greek": "ο μηνιαίος μισθός",
        "english": "monthly salary",
        "notes": "Adjective μηνιαίος, -α, -ο (monthly) + masculine noun μισθός.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "masculine"},
        "keg_communicative_function": "Stating salary expectations and compensation packages",
        "example_el": "Ο μηνιαίος μισθός κατατίθεται στον τραπεζικό λογαριασμό την πρώτη κάθε μήνα.",
        "example_en": "The monthly salary is deposited in the bank account on the first of each month.",
        "example2_el": "Ποιος είναι ο καθαρός μηνιαίος μισθός μετά την αφαίρεση των φόρων;",
        "example2_en": "What is the net monthly salary after deducting taxes?"
    },
    {
        "id": "A2P2-U09-009",
        "greek": "η κανονική άδεια",
        "english": "annual paid leave / regular vacation leave",
        "notes": "Workplace entitlement: κανονική άδεια (distinguished from αναρρωτική άδεια).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Requesting annual vacation time in written requests to management",
        "example_el": "Θα ήθελα να πάρω δύο εβδομάδες από την κανονική μου άδεια τον Αύγουστο.",
        "example_en": "I would like to take two weeks of my annual leave in August.",
        "example2_el": "Ο διευθυντής ενέκρινε την κανονική άδεια όλων των υπαλλήλων του τμήματος.",
        "example2_en": "The manager approved the annual leave of all department employees."
    },
    {
        "id": "A2P2-U09-010",
        "greek": "η συστατική επιστολή",
        "english": "letter of recommendation / reference letter",
        "notes": "Adjective συστατικός (recommending) + επιστολή (letter). Critical for applications.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Requesting and submitting letters of recommendation for job applications",
        "example_el": "Ο προηγούμενος εργοδότης μου μού έγραψε μια εξαιρετική συστατική επιστολή.",
        "example_en": "My previous employer wrote me an excellent letter of recommendation.",
        "example2_el": "Επισυνάπτω το βιογραφικό μου σημείωμα και δύο συστατικές επιστολές.",
        "example2_en": "I attach my curriculum vitae and two letters of recommendation."
    },
    {
        "id": "A2P2-U09-011",
        "greek": "η επαγγελματική εμπειρία",
        "english": "professional work experience",
        "notes": "Adjective επαγγελματικός + εμπειρία. Major CV heading in A2 exams.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Summarizing work history and career background in interviews and forms",
        "example_el": "Έχω πενταετή επαγγελματική εμπειρία στον τομέα των πωλήσεων και του μάρκετινγκ.",
        "example_en": "I have five years of professional experience in sales and marketing.",
        "example2_el": "Η θέση είναι κατάλληλη και για νέους πτυχιούχους χωρίς προηγούμενη επαγγελματική εμπειρία.",
        "example2_en": "The position is also suitable for recent graduates without prior professional experience."
    },
    {
        "id": "A2P2-U09-012",
        "greek": "τα προσόντα του υποψηφίου",
        "english": "candidate's qualifications",
        "notes": "Neuter plural προσόντα (qualifications/assets) + γενική υποψηφίου (applicant).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Matching qualifications to job requirements in recruitment texts",
        "example_el": "Τα προσόντα του υποψηφίου ανταποκρίνονται πλήρως στις απαιτήσεις της εταιρείας.",
        "example_en": "The candidate's qualifications fully meet the company's requirements.",
        "example2_el": "Βασικό προσόν για τη θέση είναι το πτυχίο πανεπιστημίου και η γνώση ξένων γλωσσών.",
        "example2_en": "A key qualification for the position is a university degree and knowledge of foreign languages."
    },
    {
        "id": "A2P2-U09-013",
        "greek": "υποβάλλω αίτηση",
        "english": "to submit an application",
        "notes": "Formal compound verb: υποβάλλω (Aorist: υπέβαλα) + αιτιατική αίτηση.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Describing the official submission of job or university application forms",
        "example_el": "Υπέβαλα ηλεκτρονική αίτηση για τη θέση εργασίας μέσω της ιστοσελίδας.",
        "example_en": "I submitted an online application for the job position via the website.",
        "example2_el": "Η προθεσμία για να υποβάλετε αίτηση λήγει την ερχόμενη Παρασκευή.",
        "example2_en": "The deadline to submit an application expires next Friday."
    },
    {
        "id": "A2P2-U09-014",
        "greek": "το συνάδελφος και ο προϊστάμενος",
        "english": "colleague and supervisor / manager",
        "notes": "Workplace hierarchy pair: ο συνάδελφος (peer colleague) + ο προϊστάμενος (boss/supervisor).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Distinguishing communication registers between coworkers and superiors",
        "example_el": "Συνεργάζομαι άριστα με τους συναδέλφους μου και ενημερώνω τακτικά τον προϊστάμενό μου.",
        "example_en": "I cooperate excellently with my colleagues and regularly inform my supervisor.",
        "example2_el": "Ο προϊστάμενος συγκάλεσε έκτακτη συνάντηση με όλους τους συναδέλφους του γραφείου.",
        "example2_en": "The supervisor called an emergency meeting with all office colleagues."
    },
    {
        "id": "A2P2-U09-015",
        "greek": "το επαγγελματικό ταξίδι",
        "english": "business trip",
        "notes": "Collocation: επαγγελματικός, -ή, -ό + ταξίδι. Distinguish from διακοπές (vacation).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Explaining workplace travel and out-of-office duties",
        "example_el": "Την επόμενη εβδομάδα θα βρίσκομαι στην Κύπρο για επαγγελματικό ταξίδι.",
        "example_en": "Next week I will be in Cyprus for a business trip.",
        "example2_el": "Η εταιρεία καλύπτει όλα τα έξοδα διαμονής και μετακίνησης για το επαγγελματικό ταξίδι.",
        "example2_en": "The company covers all lodging and transport expenses for the business trip."
    },
    {
        "id": "A2P2-U09-016",
        "greek": "η τηλεργασία από το σπίτι",
        "english": "remote telework from home",
        "notes": "Modern term: η τηλεργασία (telework/remote work: τηλε + εργασία).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Discussing hybrid work schedules and work-from-home options",
        "example_el": "Δύο μέρες την εβδομάδα δουλεύω με τηλεργασία από το σπίτι μου.",
        "example_en": "Two days a week I work remotely via telework from my home.",
        "example2_el": "Η τηλεργασία εξοικονομεί πολύτιμο χρόνο από τις καθημερινές μετακινήσεις.",
        "example2_en": "Telework saves valuable time from daily commuting."
    },
    {
        "id": "A2P2-U09-017",
        "greek": "η ανακοίνωση της διεύθυνσης",
        "english": "management announcement / company memo",
        "notes": "Administrative communication: η ανακοίνωση + γενική της διεύθυνσης.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Reading and following internal company directives and staff notices",
        "example_el": "Διαβάστε την ανακοίνωση της διεύθυνσης στον πίνακα ανακοινώσεων του προσωπικού.",
        "example_en": "Read the management announcement on the staff bulletin board.",
        "example2_el": "Σύμφωνα με την επίσημη ανακοίνωση της διεύθυνσης, τα γραφεία θα ανακαινιστούν σύντομα.",
        "example2_en": "According to the official management memo, the offices will be renovated soon."
    },
    {
        "id": "A2P2-U09-018",
        "greek": "υπογράφω τη σύμβαση",
        "english": "to sign the contract",
        "notes": "Verb υπογράφω (Aorist: υπέγραψα) + accusative σύμβαση. Critical legal action.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Confirming the formal signing of an employment agreement",
        "example_el": "Πήγα στα κεντρικά γραφεία και υπέγραψα τη νέα σύμβαση εργασίας μου.",
        "example_en": "I went to the headquarters and signed my new employment contract.",
        "example2_el": "Διαβάστε προσεκτικά όλους τους όρους πριν υπογράψετε τη σύμβαση.",
        "example2_en": "Read all terms carefully before you sign the contract."
    },
    {
        "id": "A2P2-U09-019",
        "greek": "η προθεσμία υποβολής",
        "english": "submission deadline",
        "notes": "Fixed administrative phrase: η προθεσμία (deadline) + γενική υποβολής (submission).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Checking and meeting strict application deadlines in exam contexts",
        "example_el": "Μην καθυστερείτε: η προθεσμία υποβολής των δικαιολογητικών λήγει σήμερα στις τρεις.",
        "example_en": "Do not delay: the submission deadline for supporting documents expires today at three.",
        "example2_el": "Δόθηκε παράταση στην προθεσμία υποβολής των αιτήσεων μέχρι το τέλος του μήνα.",
        "example2_en": "An extension was granted to the application submission deadline until the end of the month."
    },
    {
        "id": "A2P2-U09-020",
        "greek": "η επαγγελματική κατάρτιση",
        "english": "vocational training / professional skilling",
        "notes": "Education-employment link: η κατάρτιση (training/preparation). Genitive: της κατάρτισης.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Describing professional development courses and technical training seminars",
        "example_el": "Παρακολουθώ σεμινάρια επαγγελματικής κατάρτισης στις ψηφιακές τεχνολογίες.",
        "example_en": "I attend professional training seminars in digital technologies.",
        "example2_el": "Η διαρκής επαγγελματική κατάρτιση είναι απαραίτητη στη σύγχρονη αγορά εργασίας.",
        "example2_en": "Continuous professional training is necessary in the modern job market."
    },
    {
        "id": "A2P2-U09-021",
        "greek": "το τμήμα προσωπικού",
        "english": "human resources department (HR)",
        "notes": "Corporate division: το τμήμα + γενική προσωπικού (staff/personnel).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Addressing inquiries regarding contracts, leave, and payroll to HR",
        "example_el": "Απευθυνθείτε στο τμήμα προσωπικού για πληροφορίες σχετικά με την ασφάλισή σας.",
        "example_en": "Address the HR department for information regarding your insurance.",
        "example2_el": "Το τμήμα προσωπικού μού ζήτησε φωτοτυπία του πτυχίου και της ταυτότητάς μου.",
        "example2_en": "The HR department asked me for a photocopy of my degree and my ID."
    },
    {
        "id": "A2P2-U09-022",
        "greek": "η παραίτηση από τη θέση",
        "english": "resignation from the post / quitting",
        "notes": "Noun η παραίτηση (resignation) + preposition από. Verb: παραιτούμαι.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Announcing career transitions or resignation from a position",
        "example_el": "Υπέβαλε την παραίτησή του επειδή βρήκε καλύτερη δουλειά στο εξωτερικό.",
        "example_en": "He submitted his resignation because he found a better job abroad.",
        "example2_el": "Η παραίτηση από τη θέση εργασίας έγινε δεκτή από το διοικητικό συμβούλιο.",
        "example2_en": "The resignation from the job position was accepted by the board of directors."
    },
    {
        "id": "A2P2-U09-023",
        "greek": "η άδεια μητρότητας",
        "english": "maternity leave",
        "notes": "Social benefit: άδεια + γενική μητρότητας (motherhood). Paternity: πατρότητας.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Discussing parental leave entitlements and family benefits",
        "example_el": "Η συνάδελφός μας βρίσκεται σε άδεια μητρότητας και θα επιστρέψει σε έξι μήνες.",
        "example_en": "Our colleague is on maternity leave and will return in six months.",
        "example2_el": "Ο νόμος προστατεύει πλήρως τις εργαζόμενες μητέρες κατά την άδεια μητρότητας.",
        "example2_en": "The law fully protects working mothers during maternity leave."
    },
    {
        "id": "A2P2-U09-024",
        "greek": "η επαγγελματική εξέλιξη",
        "english": "career advancement / professional growth",
        "notes": "Noun η εξέλιξη (evolution/advancement, genitive της εξέλιξης).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Stating career goals and promotion aspirations in personal interviews",
        "example_el": "Αυτή η θέση προσφέρει εξαιρετικές προοπτικές για επαγγελματική εξέλιξη.",
        "example_en": "This position offers excellent prospects for career advancement.",
        "example2_el": "Επιθυμώ να εργαστώ σε ένα περιβάλλον που υποστηρίζει την επαγγελματική εξέλιξη.",
        "example2_en": "I desire to work in an environment that supports professional growth."
    },
    {
        "id": "A2P2-U09-025",
        "greek": "η απόδειξη πληρωμής",
        "english": "payment receipt / pay slip",
        "notes": "Financial voucher: η απόδειξη + γενική πληρωμής. Plural: οι αποδείξεις πληρωμής.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Requesting and retaining payment receipts and salary slips",
        "example_el": "Κρατήστε την απόδειξη πληρωμής σε περίπτωση που χρειαστείτε αλλαγή προϊόντος.",
        "example_en": "Keep the payment receipt in case you need a product exchange.",
        "example2_el": "Κάθε μήνα λαμβάνουμε ηλεκτρονικά την απόδειξη πληρωμής του μισθού μας.",
        "example2_en": "Every month we receive our salary payment slip electronically."
    },
    {
        "id": "A2P2-U09-026",
        "greek": "το συνδικαλιστικό σωματείο",
        "english": "trade union / labor union",
        "notes": "Workplace civic institution: το σωματείο (association/union).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Referring to workers' unions and collective agreements in A2 texts",
        "example_el": "Το σωματείο των εργαζομένων διαπραγματεύεται τη νέα συλλογική σύμβαση.",
        "example_en": "The workers' union is negotiating the new collective agreement.",
        "example2_el": "Έγινα μέλος στο συνδικαλιστικό σωματείο για να προστατεύσω τα δικαιώματά μου.",
        "example2_en": "I became a member in the trade union to protect my rights."
    },
    {
        "id": "A2P2-U09-027",
        "greek": "οργανώνω το γραφείο μου",
        "english": "to organize my office / workspace",
        "notes": "Verb οργανώνω (Aorist: οργάνωσα) + accusative το γραφείο μου.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Describing daily workplace habits and administrative tidy-up",
        "example_el": "Κάθε πρωί οργανώνω το γραφείο μου και ταξινομώ τα έγγραφα της ημέρας.",
        "example_en": "Every morning I organize my desk and classify the documents of the day.",
        "example2_el": "Χρειάζομαι λίγο χρόνο για να οργανώσω το γραφείο μου μετά τη μετακόμιση.",
        "example2_en": "I need a little time to organize my office after the move."
    },
    {
        "id": "A2P2-U09-028",
        "greek": "η επαγγελματική επιτυχία",
        "english": "professional success",
        "notes": "Noun η επιτυχία (success, genitive της επιτυχίας). Antonym: η αποτυχία.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Congratulating colleagues or expressing wishes for career milestones",
        "example_el": "Σου εύχομαι από καρδιάς κάθε επαγγελματική επιτυχία στη νέα σου δουλειά!",
        "example_en": "I wish you from my heart every professional success in your new job!",
        "example2_el": "Η σκληρή δουλειά και η αφοσίωση είναι τα θεμέλια για την επαγγελματική επιτυχία.",
        "example2_en": "Hard work and dedication are the foundations for professional success."
    },
    {
        "id": "A2P2-U09-029",
        "greek": "το επαγγελματικό ραντεβού",
        "english": "business appointment / professional meeting",
        "notes": "Collocation: επαγγελματικός + ραντεβού (indeclinable neuter).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Scheduling, confirming, or postponing business meetings via email",
        "example_el": "Έχω ένα σημαντικό επαγγελματικό ραντεβού με έναν πελάτη στις έντεκα το πρωί.",
        "example_en": "I have an important business appointment with a client at eleven in the morning.",
        "example2_el": "Θα ήθελα να αλλάξουμε την ώρα για το επαγγελματικό ραντεβού μας αν είναι δυνατόν.",
        "example2_en": "I would like us to change the time for our business appointment if possible."
    },
    {
        "id": "A2P2-U09-030",
        "greek": "η επίσημη πρόσκληση σε δείπνο",
        "english": "formal dinner invitation",
        "notes": "Register contrast: επίσημη πρόσκληση (formal invitation) vs φιλική πρόσκληση.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Replying to formal corporate and diplomatic dinner invitations",
        "example_el": "Λάβαμε μια επίσημη πρόσκληση σε δείπνο από το Εμπορικό Επιμελητήριο.",
        "example_en": "We received a formal dinner invitation from the Chamber of Commerce.",
        "example2_el": "Παρακαλώ επιβεβαιώστε την παρουσία σας στην επίσημη πρόσκληση σε δείπνο μέχρι αύριο.",
        "example2_en": "Please confirm your attendance to the formal dinner invitation by tomorrow."
    }
]

# -------------------------------------------------------------
# UNIT A2P2-10 CARDS (30 cards)
# Theme: Εκπαίδευση, Σπουδές, Βιβλιοθήκες & Εκμάθηση Γλωσσών
# -------------------------------------------------------------
CARDS_U10 = [
    {
        "id": "A2P2-U10-001",
        "greek": "το πανεπιστημιακό πτυχίο",
        "english": "university degree",
        "notes": "Collocation: πανεπιστημιακός, -ή, -ό + το πτυχίο (degree). Essential biography credential.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Stating academic qualifications in personal interviews and CV applications",
        "example_el": "Έλαβα το πανεπιστημιακό πτυχίο μου στα οικονομικά με βαθμό άριστα.",
        "example_en": "I received my university degree in economics with honors.",
        "example2_el": "Για τη θέση απαιτείται πανεπιστημιακό πτυχίο ή ισότιμος αναγνωρισμένος τίτλος.",
        "example2_en": "For the position, a university degree or equivalent recognized qualification is required."
    },
    {
        "id": "A2P2-U10-002",
        "greek": "το μεταπτυχιακό πρόγραμμα",
        "english": "postgraduate master's program",
        "notes": "Compound adjective μεταπτυχιακός (meta + ptychio: post-degree) + πρόγραμμα.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Describing postgraduate studies and master's degree specializations",
        "example_el": "Έκανα αίτηση για ένα διετές μεταπτυχιακό πρόγραμμα στην ευρωπαϊκή ιστορία.",
        "example_en": "I applied for a two-year master's program in European history.",
        "example2_el": "Το μεταπτυχιακό πρόγραμμα περιλαμβάνει παρακολούθηση μαθημάτων και διπλωματική εργασία.",
        "example2_en": "The postgraduate program includes course attendance and a master's thesis."
    },
    {
        "id": "A2P2-U10-003",
        "greek": "η φοιτητική εστία",
        "english": "student dormitory / student residence hall",
        "notes": "Noun η εστία (hearth/dormitory, genitive της εστίας) + adjective φοιτητικός.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Discussing student accommodation, dorm life, and university campus services",
        "example_el": "Κατά τα πρώτα δύο χρόνια των σπουδών μου έμενα στη φοιτητική εστία.",
        "example_en": "During the first two years of my studies I lived in the student dormitory.",
        "example2_el": "Η φοιτητική εστία παρέχει δωρεάν στέγαση και σίτιση σε δικαιούχους φοιτητές.",
        "example2_en": "The student residence provides free housing and meals to eligible students."
    },
    {
        "id": "A2P2-U10-004",
        "greek": "η υποτροφία σπουδών",
        "english": "academic scholarship / study grant",
        "notes": "Noun η υποτροφία + γενική πληθυντικού σπουδών. Prestigious achievement.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Applying for and receiving academic merit scholarships",
        "example_el": "Κέρδισε υποτροφία σπουδών χάρη στις εξαιρετικές ακαδημαϊκές της επιδόσεις.",
        "example_en": "She won an academic scholarship thanks to her outstanding academic performance.",
        "example2_el": "Το ίδρυμα προσφέρει υποτροφίες σπουδών σε νέους επιστήμονες για έρευνα.",
        "example2_en": "The foundation offers study scholarships to young scientists for research."
    },
    {
        "id": "A2P2-U10-005",
        "greek": "η δανειστική βιβλιοθήκη",
        "english": "lending library / public library",
        "notes": "Adjective δανειστικός (from δανείζω: to lend) + βιβλιοθήκη. Genitive: της δανειστικής βιβλιοθήκης.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Navigating public library card rules, borrowing books, and quiet study rooms",
        "example_el": "Έβγαλα κάρτα μέλους στη δημοτική δανειστική βιβλιοθήκη για να δανείζομαι βιβλία.",
        "example_en": "I got a membership card at the municipal lending library to borrow books.",
        "example2_el": "Μπορείτε να κρατήσετε τα βιβλία από τη δανειστική βιβλιοθήκη για δεκαπέντε μέρες.",
        "example2_en": "You can keep the books from the lending library for fifteen days."
    },
    {
        "id": "A2P2-U10-006",
        "greek": "η εξεταστική περίοδος",
        "english": "exam period / exam session",
        "notes": "University calendar: η εξεταστική (short for εξεταστική περίοδος). E.g. εξεταστική Ιουνίου.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Describing intense study routines and schedules during university exam sessions",
        "example_el": "Κατά την εξεταστική περίοδο διαβάζω στη βιβλιοθήκη από το πρωί μέχρι το βράδυ.",
        "example_en": "During the exam period I study in the library from morning until evening.",
        "example2_el": "Η χειμερινή εξεταστική περίοδος ξεκινά στα τέλη Ιανουαρίου.",
        "example2_en": "The winter examination period begins in late January."
    },
    {
        "id": "A2P2-U10-007",
        "greek": "η εκμάθηση της ελληνικής",
        "english": "learning Modern Greek / acquisition of Greek",
        "notes": "Noun η εκμάθηση (acquisition/learning, from εκμανθάνω) + γενική της ελληνικής.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Expressing motivation and goals for studying Modern Greek in exams",
        "example_el": "Η εκμάθηση της ελληνικής γλώσσας είναι μια συναρπαστική και όμορφη εμπειρία.",
        "example_en": "Learning the Greek language is a fascinating and beautiful experience.",
        "example2_el": "Αφιερώνω δύο ώρες καθημερινά στην εκμάθηση της ελληνικής γραμματικής και λεξιλογίου.",
        "example2_en": "I dedicate two hours daily to the learning of Greek grammar and vocabulary."
    },
    {
        "id": "A2P2-U10-008",
        "greek": "το δίγλωσσο λεξικό",
        "english": "bilingual dictionary",
        "notes": "Compound adjective: δίγλωσσος, -η, -ο (two languages) + το λεξικό.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Referring to language study tools, dictionaries, and vocabulary apps",
        "example_el": "Χρησιμοποιώ ένα δίγλωσσο λεξικό για να μεταφράζω τις άγνωστες λέξεις.",
        "example_en": "I use a bilingual dictionary to translate unfamiliar words.",
        "example2_el": "Το ηλεκτρονικό δίγλωσσο λεξικό παρέχει παραδείγματα και φωνητική προφορά.",
        "example2_en": "The electronic bilingual dictionary provides examples and audio pronunciation."
    },
    {
        "id": "A2P2-U10-009",
        "greek": "η γραμματική και το συντακτικό",
        "english": "grammar and syntax",
        "notes": "Linguistic fundamentals: η γραμματική (morphology) + το συντακτικό (sentence structure).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Discussing language structure, rules, and syntax hurdles in student dialogues",
        "example_el": "Η ελληνική γραμματική έχει πολλούς κανόνες, αλλά το συντακτικό είναι πολύ λογικό.",
        "example_en": "Greek grammar has many rules, but the syntax is very logical.",
        "example2_el": "Κάνουμε πολλές ασκήσεις για να κατανοήσουμε τη γραμματική και το συντακτικό.",
        "example2_en": "We do many exercises to understand grammar and syntax."
    },
    {
        "id": "A2P2-U10-010",
        "greek": "η σωστή προφορά",
        "english": "correct pronunciation",
        "notes": "Adjective σωστός, -ή, -ό + noun η προφορά (pronunciation, from προφέρω).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Focusing on phonetics, accentuation, and clear oral articulation",
        "example_el": "Η σωστή προφορά και ο σωστός τονισμός βοηθούν στην καλή επικοινωνία.",
        "example_en": "Correct pronunciation and correct stress placement help in good communication.",
        "example2_el": "Ακούω ελληνικά τραγούδια και podcast για να βελτιώσω τη σωστή προφορά μου.",
        "example2_en": "I listen to Greek songs and podcasts to improve my correct pronunciation."
    },
    {
        "id": "A2P2-U10-011",
        "greek": "το φροντιστήριο γλωσσών",
        "english": "foreign language cram school / language institute",
        "notes": "Greek educational institution: το φροντιστήριο (private tuition center).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Enrolling in private language courses and group tuition centers",
        "example_el": "Κάνω εντατικά μαθήματα ελληνικών σε ένα φροντιστήριο γλωσσών στο κέντρο.",
        "example_en": "I do intensive Greek lessons at a language institute in the center.",
        "example2_el": "Το φροντιστήριο γλωσσών οργανώνει τμήματα προετοιμασίας για τις εξετάσεις του Μαΐου.",
        "example2_en": "The language center organizes preparatory classes for the May exams."
    },
    {
        "id": "A2P2-U10-012",
        "greek": "παραδίδω την εργασία",
        "english": "to submit / hand in the assignment",
        "notes": "Verb παραδίδω (Aorist: παρέδωσα) + accusative εργασία (homework/essay).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Reporting completion and timely submission of coursework to teachers",
        "example_el": "Παρέδωσα την τελική γραπτή εργασία μου στον καθηγητή πριν από τη λήξη της προθεσμίας.",
        "example_en": "I submitted my final written assignment to the professor before the deadline expired.",
        "example2_el": "Πρέπει να παραδώσουμε την εργασία μας μέσω της ηλεκτρονικής πλατφόρμας του μαθήματος.",
        "example2_en": "We must hand in our assignment via the course's electronic platform."
    },
    {
        "id": "A2P2-U10-013",
        "greek": "η βαθμολογία των εξετάσεων",
        "english": "exam marks / grades",
        "notes": "Compound noun: βαθμός (grade) + λόγος -> η βαθμολογία. Scale in Greece: 1–20 or 1–10.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Discussing exam scores, grades, and pass thresholds (βάση)",
        "example_el": "Η βαθμολογία των εξετάσεων αναρτήθηκε στην ιστοσελίδα της σχολής.",
        "example_en": "The exam marks were posted on the faculty's website.",
        "example2_el": "Πέτυχε υψηλή βαθμολογία και συγκέντρωσε δεκαεννιά στα είκοσι στην έκθεση.",
        "example2_en": "He achieved a high grade and scored nineteen out of twenty in the essay."
    },
    {
        "id": "A2P2-U10-014",
        "greek": "το σχολικό έτος",
        "english": "school year / academic year",
        "notes": "Academic calendar: το σχολικό έτος (from September to June in Greece).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Referencing school terms, vacations, and annual educational calendars",
        "example_el": "Το νέο σχολικό έτος ξεκινά στις έντεκα Σεπτεμβρίου με τον καθιερωμένο αγιασμό.",
        "example_en": "The new school year starts on September eleventh with the traditional blessing.",
        "example2_el": "Κατά τη διάρκεια του σχολικού έτους οι μαθητές έχουν διακοπές Χριστουγέννων και Πάσχα.",
        "example2_en": "During the school year students have Christmas and Easter vacations."
    },
    {
        "id": "A2P2-U10-015",
        "greek": "η προφορική παρουσίαση",
        "english": "oral presentation",
        "notes": "Classroom requirement: προφορικός, -ή, -ό + παρουσίαση. Plural: οι παρουσιάσεις.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Preparing and delivering oral presentations in front of classmates",
        "example_el": "Ετοίμασα μια δεκάλεπτη προφορική παρουσίαση με διαφάνειες για τον ελληνικό τουρισμό.",
        "example_en": "I prepared a ten-minute oral presentation with slides on Greek tourism.",
        "example2_el": "Η προφορική παρουσίαση βαθμολογείται για την καθαρότητα και τη δομή των επιχειρημάτων.",
        "example2_en": "The oral presentation is graded for clarity and argument structure."
    },
    {
        "id": "A2P2-U10-016",
        "greek": "η ομαδική εργασία",
        "english": "group work / team project",
        "notes": "Pedagogical format: ομαδικός, -ή, -ό + εργασία. Opposite: ατομική εργασία.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Collaborating on team projects and dividing tasks with fellow students",
        "example_el": "Στο μάθημα της ιστορίας κάναμε μια ομαδική εργασία τριών ατόμων.",
        "example_en": "In the history class we did a group project of three people.",
        "example2_el": "Η ομαδική εργασία καλλιεργεί τη συνεργασία και την ανταλλαγή απόψεων.",
        "example2_en": "Teamwork cultivates cooperation and the exchange of views."
    },
    {
        "id": "A2P2-U10-017",
        "greek": "η πανεπιστημιούπολη",
        "english": "university campus",
        "notes": "Compound noun: πανεπιστήμιο + πόλη (university city/campus). Feminine third declension.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "feminine"},
        "keg_communicative_function": "Describing university campus facilities, libraries, and grounds",
        "example_el": "Η πανεπιστημιούπολη στα Ιωάννινα είναι καταπράσινη και διαθέτει σύγχρονες εγκαταστάσεις.",
        "example_en": "The university campus in Ioannina is very green and features modern facilities.",
        "example2_el": "Το λεωφορείο συνδέει το κέντρο της πόλης απευθείας με την πανεπιστημιούπολη.",
        "example2_en": "The bus connects the city center directly with the university campus."
    },
    {
        "id": "A2P2-U10-018",
        "greek": "το εκπαιδευτικό σύστημα",
        "english": "educational system",
        "notes": "Adjective εκπαιδευτικός, -ή, -ό + noun το σύστημα (genitive του συστήματος).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Comparing educational structures and school levels across countries",
        "example_el": "Το ελληνικό εκπαιδευτικό σύστημα περιλαμβάνει πρωτοβάθμια, δευτεροβάθμια και τριτοβάθμια εκπαίδευση.",
        "example_en": "The Greek educational system includes primary, secondary, and tertiary education.",
        "example2_el": "Υπάρχουν αρκετές διαφορές ανάμεσα στο εκπαιδευτικό σύστημα της Ελλάδας και της χώρας μου.",
        "example2_en": "There are several differences between the educational system of Greece and of my country."
    },
    {
        "id": "A2P2-U10-019",
        "greek": "το πιστοποιητικό γλωσσομάθειας",
        "english": "language proficiency certificate",
        "notes": "Official credential: το πιστοποιητικό + γενική γλωσσομάθειας (language knowledge).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Targeting the official Certificate of Attainment in Greek examinations",
        "example_el": "Στόχος μου είναι να αποκτήσω το επίσημο πιστοποιητικό γλωσσομάθειας επιπέδου Α2.",
        "example_en": "My goal is to obtain the official language proficiency certificate of level A2.",
        "example2_el": "Το πιστοποιητικό γλωσσομάθειας του ΚΕΓ αναγνωρίζεται διεθνώς και από το ελληνικό δημόσιο.",
        "example2_en": "The KEG language proficiency certificate is recognized internationally and by the Greek state."
    },
    {
        "id": "A2P2-U10-020",
        "greek": "η πτυχιακή εργασία",
        "english": "graduation thesis / bachelor's dissertation",
        "notes": "Adjective πτυχιακός (degree-related) + εργασία. Capstone academic paper.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Describing undergraduate thesis research and oral defense",
        "example_el": "Ολοκλήρωσα την πτυχιακή εργασία μου με θέμα τη διδασκαλία της ελληνικής ως ξένης γλώσσας.",
        "example_en": "I completed my bachelor's thesis on teaching Greek as a foreign language.",
        "example2_el": "Υποστήριξε με επιτυχία την πτυχιακή εργασία του μπροστά στην τριμελή επιτροπή καθηγητών.",
        "example2_en": "He successfully defended his thesis before the three-member committee of professors."
    },
    {
        "id": "A2P2-U10-021",
        "greek": "η διά ζώσης εκπαίδευση",
        "english": "in-person / face-to-face education",
        "notes": "Archaic fixed expression: διά ζώσης (in person, physically present). Opposite: εξ αποστάσεως.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Contrasting classroom-based physical study with online remote learning",
        "example_el": "Προτιμώ τη διά ζώσης εκπαίδευση επειδή η επαφή με τον δάσκαλο είναι πιο άμεση.",
        "example_en": "I prefer in-person education because contact with the teacher is more direct.",
        "example2_el": "Τα πανεπιστήμια επέστρεψαν πλήρως στη διά ζώσης εκπαίδευση και διδασκαλία.",
        "example2_en": "Universities returned fully to in-person education and teaching."
    },
    {
        "id": "A2P2-U10-022",
        "greek": "η εξ αποστάσεως διδασκαλία",
        "english": "distance learning / online teaching",
        "notes": "Adverbial phrase: εξ αποστάσεως (from a distance) + διδασκαλία (teaching/instruction).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Describing video conference classes, e-learning platforms, and digital tutoring",
        "example_el": "Η εξ αποστάσεως διδασκαλία προσφέρει μεγάλη ευελιξία σε εργαζόμενους φοιτητές.",
        "example_en": "Distance learning offers great flexibility to working students.",
        "example2_el": "Παρακολουθώ μαθήματα ελληνικών μέσω εξ αποστάσεως διδασκαλίας δύο φορές την εβδομάδα.",
        "example2_en": "I attend Greek lessons via distance learning twice a week."
    },
    {
        "id": "A2P2-U10-023",
        "greek": "η εγγραφή στο πανεπιστήμιο",
        "english": "university enrollment / registration",
        "notes": "Administrative milestone: η εγγραφή (enrollment/registration, genitive της εγγραφής).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Completing student registration and course enrollment procedures",
        "example_el": "Ολοκλήρωσα την εγγραφή μου στο πανεπιστήμιο και παρέλαβα τη φοιτητική μου ταυτότητα.",
        "example_en": "I completed my enrollment at the university and received my student ID card.",
        "example2_el": "Οι εγγραφές στο πανεπιστήμιο πραγματοποιούνται ηλεκτρονικά τον Σεπτέμβριο.",
        "example2_en": "University enrollments take place electronically in September."
    },
    {
        "id": "A2P2-U10-024",
        "greek": "το αναγνωστήριο",
        "english": "study hall / reading room",
        "notes": "Dedicated quiet space: το αναγνωστήριο (from αναγιγνώσκω / αναγνώστης).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {"part_of_speech": "noun", "gender": "neuter"},
        "keg_communicative_function": "Meeting study partners in library quiet zones and silent reading rooms",
        "example_el": "Συναντηθήκαμε στο κεντρικό αναγνωστήριο της βιβλιοθήκης για να μελετήσουμε μαζί.",
        "example_en": "We met in the central reading room of the library to study together.",
        "example2_el": "Στο αναγνωστήριο επιβάλλεται απόλυτη ησυχία για να μην ενοχλούνται οι φοιτητές.",
        "example2_en": "In the reading room absolute silence is required so students are not disturbed."
    },
    {
        "id": "A2P2-U10-025",
        "greek": "η επαναληπτική άσκηση",
        "english": "revision exercise / review drill",
        "notes": "Adjective επαναληπτικός, -ή, -ό (revision/review, from επανάληψη) + άσκηση.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Doing practice drills, grammar tests, and test-prep review tasks",
        "example_el": "Κάναμε πολλές επαναληπτικές ασκήσεις στον αόριστο και στον μέλλοντα.",
        "example_en": "We did many revision exercises in the simple past and future tense.",
        "example2_el": "Οι επαναληπτικές ασκήσεις στο τέλος κάθε ενότητας βοηθούν στην εμπέδωση της ύλης.",
        "example2_en": "The review exercises at the end of each unit help in consolidating the material."
    },
    {
        "id": "A2P2-U10-026",
        "greek": "η διπλωματική επιτροπή",
        "english": "examination committee / jury panel",
        "notes": "Evaluation panel: διπλωματικός (degree-evaluating) + επιτροπή (committee).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Describing formal academic evaluation and oral degree defenses",
        "example_el": "Η διπλωματική επιτροπή βαθμολόγησε την εργασία με βαθμό εννιάμισι.",
        "example_en": "The examination committee graded the thesis with a mark of nine and a half.",
        "example2_el": "Απάντησε με σιγουριά σε όλες τις ερωτήσεις που έθεσε η διπλωματική επιτροπή.",
        "example2_en": "He answered with confidence all the questions posed by the examination committee."
    },
    {
        "id": "A2P2-U10-027",
        "greek": "οι ξένες γλώσσες",
        "english": "foreign languages",
        "notes": "Essential skill: ξένος, -η, -ο + γλώσσα. Plural: οι ξένες γλώσσες.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine plural"},
        "keg_communicative_function": "Listing spoken languages and multilingual capabilities in resumes",
        "example_el": "Μιλάω άπταιστα δύο ξένες γλώσσες, αγγλικά και γαλλικά, και μαθαίνω ελληνικά.",
        "example_en": "I speak two foreign languages fluently, English and French, and I am learning Greek.",
        "example2_el": "Η γνώση ξένων γλωσσών ανοίγει πόρτες για σπουδές και εργασία στο εξωτερικό.",
        "example2_en": "Knowledge of foreign languages opens doors for studies and work abroad."
    },
    {
        "id": "A2P2-U10-028",
        "greek": "το εκπαιδευτικό πρόγραμμα",
        "english": "educational program / curriculum course",
        "notes": "Adjective εκπαιδευτικός + πρόγραμμα. E.g. εκπαιδευτικό πρόγραμμα Erasmus.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "neuter"},
        "keg_communicative_function": "Participating in academic exchange programs like Erasmus in Greece",
        "example_el": "Συμμετέχω σε ένα ευρωπαϊκό εκπαιδευτικό πρόγραμμα ανταλλαγής φοιτητών.",
        "example_en": "I am participating in a European educational student exchange program.",
        "example2_el": "Το εκπαιδευτικό πρόγραμμα περιλαμβάνει μαθήματα γλώσσας και πολιτιστικές επισκέψεις.",
        "example2_en": "The educational program includes language lessons and cultural visits."
    },
    {
        "id": "A2P2-U10-029",
        "greek": "η ακαδημαϊκή ταυτότητα",
        "english": "student ID card / academic pass (πάσο)",
        "notes": "Student credential: η ακαδημαϊκή ταυτότητα (colloquially called το πάσο).",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Showing student ID for discounts on public transit, museums, and bookstores",
        "example_el": "Δείξτε την ακαδημαϊκή ταυτότητά σας για να πάρετε μειωμένο εισιτήριο στο μετρό.",
        "example_en": "Show your student ID card to get a discounted ticket on the metro.",
        "example2_el": "Η ακαδημαϊκή ταυτότητα ισχύει για όλα τα χρόνια των προπτυχιακών σπουδών.",
        "example2_en": "The student ID card is valid for all years of undergraduate studies."
    },
    {
        "id": "A2P2-U10-030",
        "greek": "η ορκωμοσία των αποφοίτων",
        "english": "graduation commencement / oath ceremony",
        "notes": "Commencement ritual: η ορκωμοσία (oath-taking, from ορκίζομαι) + γενική αποφοίτων.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase", "gender": "feminine"},
        "keg_communicative_function": "Inviting family and friends to university graduation commencement ceremonies",
        "example_el": "Η επίσημη ορκωμοσία των αποφοίτων της σχολής θα γίνει στην κεντρική αίθουσα τελετών.",
        "example_en": "The official graduation commencement of the faculty will take place in the central hall of ceremonies.",
        "example2_el": "Σας προσκαλώ με χαρά στην ορκωμοσία μου την ερχόμενη Τετάρτη στις δώδεκα το μεσημέρι.",
        "example2_en": "I invite you with joy to my graduation ceremony next Wednesday at twelve noon."
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
    print("Generating KEG-A2 Part 2: Batch 5 (Units 09 & 10)")
    print("==================================================")
    
    u09_notes = """Unit A2P2-09 Core Notes: Εργασία, Επαγγελματικές Σχέσεις & Καριέρα
• Workplace Communication & Recruitment Protocol:
  - Applying for positions and classified ads (η αγγελία πρόσληψης, υποβάλλω αίτηση, η συστατική επιστολή).
  - Contracts & Working Hours (η σύμβαση ορισμένου/αορίστου χρόνου, πλήρης/μερική απασχόληση, οι υπερωρίες).
  - Workplace hierarchy and team communication (ο συνάδελφος, ο προϊστάμενος, το τμήμα προσωπικού)."""

    process_and_save_unit(
        unit_id="unit-a2p2-09",
        lesson_id="lesson-01",
        title="Μάθημα 9: Εργασία, Επαγγελματικές Σχέσεις & Καριέρα (Workplace & Career Development)",
        description="Mastering employment contracts, recruitment interviews, job applications, workplace relations, and professional duties for the KEG A2 exam.",
        lesson_notes=u09_notes,
        cards=CARDS_U09,
        order_code="KEG-A2-P2-09-A"
    )

    u10_notes = """Unit A2P2-10 Core Notes: Εκπαίδευση, Σπουδές & Γλώσσες
• Academic & Language Acquisition Terminology:
  - University milestones and qualifications (το πανεπιστημιακό πτυχίο, το μεταπτυχιακό, η υποτροφία, η ορκωμοσία).
  - Libraries and study spaces (η δανειστική βιβλιοθήκη, το αναγνωστήριο, η εξεταστική περίοδος).
  - Language learning tools and terminology (η εκμάθηση της ελληνικής, το δίγλωσσο λεξικό, η σωστή προφορά)."""

    process_and_save_unit(
        unit_id="unit-a2p2-10",
        lesson_id="lesson-01",
        title="Μάθημα 10: Εκπαίδευση, Σπουδές & Γλώσσες (Education & Language Learning)",
        description="Understanding university courses, degrees, scholarships, library facilities, and language learning strategies for the KEG A2 exams.",
        lesson_notes=u10_notes,
        cards=CARDS_U10,
        order_code="KEG-A2-P2-10-A"
    )

    manifest_entries = [
        {
            "id": "unit-a2p2-09",
            "title": "Μάθημα 9: Εργασία, Επαγγελματικές Σχέσεις & Καριέρα (Workplace & Career Development)",
            "description": "Mastering employment contracts, recruitment interviews, job applications, workplace relations, and professional duties for the KEG A2 exam.",
            "order": "KEG-A2-P2-09-A",
            "total_lessons": 1,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2p2-09/lesson-01.yaml",
                    "title": "Μάθημα 9: Εργασία, Επαγγελματικές Σχέσεις & Καριέρα (Workplace & Career Development)"
                }
            ]
        },
        {
            "id": "unit-a2p2-10",
            "title": "Μάθημα 10: Εκπαίδευση, Σπουδές & Γλώσσες (Education & Language Learning)",
            "description": "Understanding university courses, degrees, scholarships, library facilities, and language learning strategies for the KEG A2 exams.",
            "order": "KEG-A2-P2-10-A",
            "total_lessons": 1,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": "unit-a2p2-10/lesson-01.yaml",
                    "title": "Μάθημα 10: Εκπαίδευση, Σπουδές & Γλώσσες (Education & Language Learning)"
                }
            ]
        }
    ]

    update_manifest(manifest_entries)
    print("\n[OK] Batch 5 finished successfully!")

if __name__ == "__main__":
    main()

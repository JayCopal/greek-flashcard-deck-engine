# -*- coding: utf-8 -*-
"""
Enrich Units 1, 2, and 3 with authentic second example sentences (KEG A1 Exam)
and synthesize Chirp-3 HD TTS for both Sentence 1 and Sentence 2.
"""
import sys
import os
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from server.tts_service import synthesize_greek_chirp, generate_audio_filename

AUDIO_DIR = BASE_DIR / "audio"
CONTENT_DIR = BASE_DIR / "content"

U01_EXAMPLES_2 = {
    "A1-U01-001": ("Ποιος είναι αυτός ο κύριος εκεί;", "Who is that gentleman over there?"),
    "A1-U01-002": ("Η κυρία Παπαδάκη είναι καθηγήτρια ελληνικών.", "Mrs. Papadaki is a Greek teacher."),
    "A1-U01-003": ("Η δεσποινίς Μαρία είναι γραμματέας στο σχολείο.", "Miss Maria is a secretary at the school."),
    "A1-U01-004": ("Γράψτε το όνομά σας στο έντυπο, παρακαλώ.", "Write your name on the form, please."),
    "A1-U01-005": ("Πώς γράφετε το επώνυμό σας;", "How do you spell your last name?"),
    "A1-U01-006": ("Έχω ένα γράμμα από τον φίλο μου στην Ιταλία.", "I have a letter from my friend in Italy."),
    "A1-U01-007": ("Ο φίλος μου μιλάει πολύ καλά ελληνικά.", "My friend speaks Greek very well."),
    "A1-U01-008": ("Η φίλη μου μένει στη Θεσσαλονίκη.", "My friend lives in Thessaloniki."),
    "A1-U01-009": ("Είστε έτοιμοι για τις εξετάσεις;", "Are you ready for the exams?"),
    "A1-U01-010": ("Τι λέει ο διάλογος στο κείμενο;", "What does the dialogue in the text say?"),
    "A1-U01-011": ("Γράφω μια σύντομη κάρτα στη μητέρα μου.", "I am writing a short card to my mother."),
    "A1-U01-012": ("Εγώ μένω στην Αθήνα και σπουδάζω.", "I live in Athens and I study."),
    "A1-U01-013": ("Εσύ τι γλώσσες μιλάς;", "What languages do you speak?"),
    "A1-U01-014": ("Αυτός είναι ο νέος γιατρός του νοσοκομείου.", "He is the new doctor of the hospital."),
    "A1-U01-015": ("Αυτή δουλεύει σε μία μεγάλη τράπεζα.", "She works in a big bank."),
    "A1-U01-016": ("Αυτό το βιβλίο είναι για το επίπεδο Α1.", "This book is for level A1."),
    "A1-U01-017": ("Εμείς μαθαίνουμε ελληνικά κάθε μέρα.", "We learn Greek every day."),
    "A1-U01-018": ("Εσείς τι δουλειά κάνετε;", "What kind of work do you do?"),
    "A1-U01-019": ("Αυτά τα μαθήματα είναι πολύ χρήσιμα.", "These lessons are very useful."),
    "A1-U01-020": ("Πώς πάτε στο πανεπιστήμιο;", "How do you go to the university?"),
    "A1-U01-021": ("Ποιο είναι το τηλέφωνό σας;", "What is your phone number?"),
    "A1-U01-022": ("Τι ώρα αρχίζει η εξέταση;", "What time does the exam begin?"),
    "A1-U01-023": ("Γεια σου, Νίκο! Τα λέμε αύριο.", "Hello, Nikos! See you tomorrow."),
    "A1-U01-024": ("Γεια σας, παιδιά! Είστε καλά;", "Hello, guys! Are you well?"),
    "A1-U01-025": ("Καλημέρα, θέλω ένα εισιτήριο παρακαλώ.", "Good morning, I want a ticket please."),
    "A1-U01-026": ("Καλησπέρα, ένα τραπέζι για δύο άτομα παρακαλώ.", "Good evening, a table for two please."),
    "A1-U01-027": ("Είμαι κουρασμένος, καληνύχτα!", "I am tired, good night!"),
    "A1-U01-028": ("Αντίο και καλό ταξίδι!", "Goodbye and have a good trip!"),
    "A1-U01-029": ("Τα λέμε το απόγευμα στην πλατεία.", "See you this afternoon in the square."),
    "A1-U01-030": ("Σας ευχαριστώ πολύ, κύριε καθηγητά.", "Thank you very much, Professor."),
    "A1-U01-031": ("— Ευχαριστώ πολύ! — Παρακαλώ, τίποτα!", "— Thank you very much! — You're welcome, not at all!"),
    "A1-U01-032": ("Ζητώ συγγνώμη για την καθυστέρηση.", "I apologize for the delay."),
    "A1-U01-033": ("Χάρηκα πολύ για τη γνωριμία.", "Very pleased to meet you."),
    "A1-U01-034": ("Μου αρέσει πολύ η ελληνική μουσική.", "I like Greek music very much."),
    "A1-U01-035": ("Όλα πάνε πολύ καλά στη δουλειά.", "Everything goes very well at work.")
}

U02_EXAMPLES_2 = {
    "A1-U02-001": ("Η Ισπανία είναι μία όμορφη ευρωπαϊκή χώρα.", "Spain is a beautiful European country."),
    "A1-U02-002": ("Ποια είναι η πρωτεύουσα της χώρας σου;", "What is the capital city of your country?"),
    "A1-U02-003": ("Πολλά κράτη συμμετέχουν στον διαγωνισμό.", "Many states participate in the competition."),
    "A1-U02-004": ("Έχω ελληνική και καναδική εθνικότητα.", "I have Greek and Canadian nationality."),
    "A1-U02-005": ("Από πού είναι η καταγωγή της οικογένειάς σου;", "Where is your family's origin from?"),
    "A1-U02-006": ("Η ελληνική γλώσσα έχει μακρά ιστορία.", "The Greek language has a long history."),
    "A1-U02-007": ("Μιλάω τη μητρική μου γλώσσα στο σπίτι.", "I speak my mother tongue at home."),
    "A1-U02-008": ("Κάθε καλοκαίρι ταξιδεύω στην Ελλάδα.", "Every summer I travel to Greece."),
    "A1-U02-009": ("Το Λονδίνο είναι η πρωτεύουσα της Αγγλίας.", "London is the capital of England."),
    "A1-U02-010": ("Η Κύπρος έχει υπέροχες παραλίες.", "Cyprus has wonderful beaches."),
    "A1-U02-011": ("Μαθαίνω γαλλικά γιατί θέλω να πάω στη Γαλλία.", "I learn French because I want to go to France."),
    "A1-U02-012": ("Ο αδελφός μου σπουδάζει στη Γερμανία.", "My brother studies in Germany."),
    "A1-U02-013": ("Η Ρώμη είναι μεγάλη πόλη στην Ιταλία.", "Rome is a big city in Italy."),
    "A1-U02-014": ("Η Μαδρίτη και η Βαρκελώνη είναι στην Ισπανία.", "Madrid and Barcelona are in Spain."),
    "A1-U02-015": ("Έχω συγγενείς στις Ηνωμένες Πολιτείες.", "I have relatives in the United States."),
    "A1-U02-016": ("Πολλοί Έλληνες ζουν στην Αυστραλία.", "Many Greeks live in Australia."),
    "A1-U02-017": ("Ο κύριος Γιώργος είναι Έλληνας από την Κρήτη.", "Mr. Giorgos is a Greek man from Crete."),
    "A1-U02-018": ("Η Μαρία είναι Ελληνίδα και μένει στην Πάτρα.", "Maria is a Greek woman and lives in Patras."),
    "A1-U02-019": ("Ο Άγγλος καθηγητής διδάσκει στο κολέγιο.", "The English teacher teaches at the college."),
    "A1-U02-020": ("Η κυρία Σμιθ είναι Αγγλίδα τουρίστρια.", "Mrs. Smith is an English tourist."),
    "A1-U02-021": ("Ο Γάλλος μάγειρας φτιάχνει υπέροχα γλυκά.", "The French chef makes wonderful desserts."),
    "A1-U02-022": ("Η Γαλλίδα φοιτήτρια μαθαίνει νέα ελληνικά.", "The French student learns Modern Greek."),
    "A1-U02-023": ("Ο Γερμανός μηχανικός εργάζεται στην Αθήνα.", "The German engineer works in Athens."),
    "A1-U02-024": ("Η Γερμανίδα φίλη μου μιλάει τρεις γλώσσες.", "My German friend speaks three languages."),
    "A1-U02-025": ("Ο Ιταλός οδηγός γνωρίζει καλά τους δρόμους.", "The Italian driver knows the streets well."),
    "A1-U02-026": ("Η Ιταλίδα τραγουδίστρια έχει ωραία φωνή.", "The Italian singer has a nice voice."),
    "A1-U02-027": ("Ο Ισπανός συμμαθητής μου είναι πολύ φιλικός.", "My Spanish classmate is very friendly."),
    "A1-U02-028": ("Η Ισπανίδα δασκάλα διδάσκει ισπανικά.", "The Spanish teacher teaches Spanish."),
    "A1-U02-029": ("Μου αρέσει το ελληνικό γιαούρτι με μέλι.", "I like Greek yogurt with honey."),
    "A1-U02-030": ("Καταλαβαίνω τα ελληνικά αλλά μιλάω λίγο.", "I understand Greek but I speak a little."),
    "A1-U02-031": ("Διαβάζω ένα βιβλίο στα αγγλικά.", "I am reading a book in English."),
    "A1-U02-032": ("Τα γαλλικά είναι μία όμορφη γλώσσα.", "French is a beautiful language."),
    "A1-U02-033": ("Πού μένεις τώρα στην Αθήνα;", "Where do you live now in Athens?"),
    "A1-U02-034": ("Μιλάτε αργά παρακαλώ, είμαι ξένος.", "Please speak slowly, I am a foreigner."),
    "A1-U02-035": ("Μαθαίνω ελληνικά για τις εξετάσεις του ΚΕΓ.", "I am learning Greek for the KEG exams."),
    "A1-U02-036": ("Δεν καταλαβαίνω αυτή τη λέξη, τι σημαίνει;", "I don't understand this word, what does it mean?"),
    "A1-U02-037": ("Ξέρετε πού είναι η στάση του λεωφορείου;", "Do you know where the bus stop is?"),
    "A1-U02-038": ("Είμαι από την Κύπρο, εσύ από πού είσαι;", "I am from Cyprus, where are you from?"),
    "A1-U02-039": ("Μένουμε σε ένα ξενοδοχείο στο κέντρο.", "We are staying at a hotel in the center."),
    "A1-U02-040": ("Μιλάω λίγο ελληνικά, είμαι αρχάριος.", "I speak a little Greek, I am a beginner.")
}

U03_EXAMPLES_2 = {
    "A1-U03-001": ("Συμπληρώστε το επάγγελμά σας στην αίτηση.", "Fill in your profession on the application form."),
    "A1-U03-002": ("Ο δάσκαλος εξηγεί τον κανόνα στα παιδιά.", "The teacher explains the rule to the children."),
    "A1-U03-003": ("Η δασκάλα διαβάζει το παραμύθι στην τάξη.", "The teacher reads the fairy tale in the classroom."),
    "A1-U03-004": ("Ο καθηγητής απαντάει στις ερωτήσεις μας.", "The professor answers our questions."),
    "A1-U03-005": ("Η καθηγήτρια γράφει στον πίνακα.", "The professor writes on the board."),
    "A1-U03-006": ("Ο μαθητής γράφει την άσκηση στο τετράδιο.", "The pupil writes the exercise in the notebook."),
    "A1-U03-007": ("Η μαθήτρια ρωτάει τη δασκάλα για το μάθημα.", "The pupil asks the teacher about the lesson."),
    "A1-U03-008": ("Ο φοιτητής διαβάζει στη βιβλιοθήκη.", "The university student studies in the library."),
    "A1-U03-009": ("Η φοιτήτρια περνάει όλες τις εξετάσεις.", "The university student passes all the exams."),
    "A1-U03-010": ("Πρέπει να πάω στον γιατρό σήμερα.", "I must go to the doctor today."),
    "A1-U03-011": ("Η νοσοκόμα βοηθάει τον ασθενή στο κρεβάτι.", "The nurse helps the patient in bed."),
    "A1-U03-012": ("Ο δικηγόρος διαβάζει τα επίσημα έγγραφα.", "The lawyer reads the official documents."),
    "A1-U03-013": ("Ο γραμματέας στέλνει ένα email στον πελάτη.", "The secretary sends an email to the client."),
    "A1-U03-014": ("Ο υπάλληλος δίνει πληροφορίες στο γκισέ.", "The employee gives information at the counter."),
    "A1-U03-015": ("Ο πωλητής λέει την τιμή στον πελάτη.", "The salesman tells the price to the customer."),
    "A1-U03-016": ("Η πωλήτρια δείχνει τα ρούχα στη βιτρίνα.", "The saleswoman shows the clothes in the display window."),
    "A1-U03-017": ("Ο σερβιτόρος ρωτάει: 'Τι θα πιείτε;'.", "The waiter asks: 'What will you drink?'."),
    "A1-U03-018": ("Η σερβιτόρα φέρνει τον λογαριασμό στο τραπέζι.", "The waitress brings the bill to the table."),
    "A1-U03-019": ("Ο οδηγός ταξί σταματάει στο φανάρι.", "The taxi driver stops at the traffic light."),
    "A1-U03-020": ("Ο μάγειρας μαγειρεύει φρέσκο ψάρι.", "The chef cooks fresh fish."),
    "A1-U03-021": ("Το γραφείο μου είναι στον τρίτο όροφο.", "My office is on the third floor."),
    "A1-U03-022": ("Το σχολείο είναι κλειστό το Σάββατο.", "The school is closed on Saturday."),
    "A1-U03-023": ("Το πανεπιστήμιο έχει πολλούς ξένους φοιτητές.", "The university has many foreign students."),
    "A1-U03-024": ("Το νοσοκομείο είναι κοντά στον σταθμό.", "The hospital is near the station."),
    "A1-U03-025": ("Η εταιρεία ανοίγει νέο γραφείο στη Θεσσαλονίκη.", "The company opens a new office in Thessaloniki."),
    "A1-U03-026": ("Γράψτε τη διεύθυνση κατοικίας σας εδώ.", "Write your home address here."),
    "A1-U03-027": ("Η οδός Πανεπιστημίου είναι πολύ γνωστή.", "Panepistimiou Street is very well known."),
    "A1-U03-028": ("Σε ποιον αριθμό μένετε;", "At which number do you live?"),
    "A1-U03-029": ("Ποιο είναι το τηλέφωνο του φαρμακείου;", "What is the pharmacy's phone number?"),
    "A1-U03-030": ("Στείλε μου μήνυμα στο κινητό μου.", "Send me a message on my mobile phone."),
    "A1-U03-031": ("Πού είναι το ταχυδρομείο της γειτονιάς;", "Where is the neighborhood post office?"),
    "A1-U03-032": ("Συμπληρώστε τον ταχυδρομικό κώδικα στο γράμμα.", "Fill in the postal code on the letter."),
    "A1-U03-033": ("Δουλεύω από τις εννέα μέχρι τις πέντε.", "I work from nine to five."),
    "A1-U03-034": ("Τι σπουδάζεις στο πανεπιστήμιο;", "What do you study at university?"),
    "A1-U03-035": ("Δύο μείον δύο κάνει μηδέν.", "Two minus two makes zero."),
    "A1-U03-036": ("Θέλω ένα ποτήρι νερό, παρακαλώ.", "I want a glass of water, please."),
    "A1-U03-037": ("Το λεωφορείο περνάει σε δέκα λεπτά.", "The bus passes in ten minutes."),
    "A1-U03-038": ("Ένα κιλό πορτοκάλια κοστίζει ένα ευρώ και είκοσι λεπτά.", "One kilo of oranges costs one euro and twenty cents."),
    "A1-U03-039": ("Το ξενοδοχείο έχει εκατό δωμάτια.", "The hotel has one hundred rooms."),
    "A1-U03-040": ("Πού είναι η στάση του μετρό;", "Where is the metro stop?")
}

ALL_BATCH_A = [
    ("unit-01", U01_EXAMPLES_2),
    ("unit-02", U02_EXAMPLES_2),
    ("unit-03", U03_EXAMPLES_2),
]

def process_batch_a():
    total_new_sentences = 0
    total_audio_synthesized = 0
    
    for uid, ex2_map in ALL_BATCH_A:
        yaml_path = CONTENT_DIR / uid / "lesson-01.yaml"
        with open(yaml_path, "r", encoding="utf-8") as f:
            ydata = yaml.safe_load(f)
            
        entries = ydata.get("entries", [])
        print(f"\n=== Processing {uid} ({len(entries)} cards) ===")
        
        for e in entries:
            cid = e["id"]
            
            # Sentence 1: Ensure example_audio exists
            ex1_el = e.get("example_el", "").strip()
            if ex1_el:
                fn1 = generate_audio_filename(ex1_el)
                out_path1 = AUDIO_DIR / fn1
                if not out_path1.exists() or out_path1.stat().st_size == 0:
                    print(f"  [TTS Ex1] {cid}: '{ex1_el}' -> {fn1} ...", end=" ", flush=True)
                    try:
                        b = synthesize_greek_chirp(ex1_el)
                        with open(out_path1, "wb") as f_out:
                            f_out.write(b)
                        total_audio_synthesized += 1
                        print("OK")
                    except Exception as err:
                        print(f"FAILED: {err}")
                        raise err
                e["example_audio"] = fn1
                
            # Sentence 2: Add if present in ex2_map
            if cid in ex2_map:
                ex2_el, ex2_en = ex2_map[cid]
                e["example2_el"] = ex2_el
                e["example2_en"] = ex2_en
                total_new_sentences += 1
                
                fn2 = generate_audio_filename(ex2_el)
                out_path2 = AUDIO_DIR / fn2
                if not out_path2.exists() or out_path2.stat().st_size == 0:
                    print(f"  [TTS Ex2] {cid}: '{ex2_el}' -> {fn2} ...", end=" ", flush=True)
                    try:
                        b = synthesize_greek_chirp(ex2_el)
                        with open(out_path2, "wb") as f_out:
                            f_out.write(b)
                        total_audio_synthesized += 1
                        print("OK")
                    except Exception as err:
                        print(f"FAILED: {err}")
                        raise err
                e["example2_audio"] = fn2
                
        with open(yaml_path, "w", encoding="utf-8") as f:
            yaml.dump(ydata, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
        print(f"[OK] Saved {uid} with 2 example sentences and audio references.")

    print(f"\nBatch A Complete! Added {total_new_sentences} sentences, synthesized {total_audio_synthesized} audio files.")

if __name__ == "__main__":
    process_batch_a()

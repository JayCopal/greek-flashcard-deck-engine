# -*- coding: utf-8 -*-
"""
Enrich Unit 00 (Exam Rubrics & Instructions) with authentic second example sentences (KEG A1 Exam)
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

U00_EXAMPLES_2 = {
    "A1-U00-001": ("Διαβάζουμε τις ερωτήσεις πριν ακούσουμε το κείμενο.", "We read the questions before we listen to the text."),
    "A1-U00-002": ("Γράψτε ένα μήνυμα στον φίλο σας για το πάρτι.", "Write a message to your friend about the party."),
    "A1-U00-003": ("Ακούστε την ανακοίνωση στον σταθμό και απαντήστε.", "Listen to the announcement at the station and answer."),
    "A1-U00-004": ("Κοιτάξτε τις φωτογραφίες και βρείτε το σωστό πρόσωπο.", "Look at the photos and find the correct person."),
    "A1-U00-005": ("Βλέπετε το παράδειγμα στη σελίδα δέκα.", "You see the example on page ten."),
    "A1-U00-006": ("Αντιστοιχίστε κάθε εικόνα με τη σωστή λέξη.", "Match each picture with the correct word."),
    "A1-U00-007": ("Συμπληρώστε τα στοιχεία σας στην αίτηση.", "Fill in your details on the application form."),
    "A1-U00-008": ("Επιλέξτε τη σωστή πρόταση για κάθε εικόνα.", "Choose the correct sentence for each image."),
    "A1-U00-009": ("Διαλέξτε τη σωστή απάντηση από τις επιλογές.", "Pick the correct answer from the choices."),
    "A1-U00-010": ("Κυκλώστε τον αριθμό που ακούτε στον διάλογο.", "Circle the number you hear in the dialogue."),
    "A1-U00-011": ("Υπογραμμίστε τη σωστή λέξη μέσα στην παρένθεση.", "Underline the correct word inside the parentheses."),
    "A1-U00-012": ("Σημειώστε ένα [X] δίπλα στη σωστή πρόταση.", "Mark an [X] next to the correct sentence."),
    "A1-U00-013": ("Απαντήστε σύντομα σε κάθε ερώτηση.", "Answer briefly to each question."),
    "A1-U00-014": ("Βρείτε τις διαφορές ανάμεσα στις δύο εικόνες.", "Find the differences between the two images."),
    "A1-U00-015": ("Βάλτε ένα [X] στο τετραγωνάκι δίπλα στο όνομα.", "Put an [X] in the little box next to the name."),
    "A1-U00-016": ("Διαγράψτε το λάθος και γράψτε το σωστό.", "Cross out the mistake and write the correct one."),
    "A1-U00-017": ("Διορθώστε την πρόταση σύμφωνα με το παράδειγμα.", "Correct the sentence according to the example."),
    "A1-U00-018": ("Ξαναδιαβάζω το κείμενο για να καταλάβω καλύτερα.", "I re-read the text to understand better."),
    "A1-U00-019": ("Συνεχίζουμε με το δεύτερο μέρος της εξέτασης.", "We continue with the second part of the exam."),
    "A1-U00-020": ("Ο καθηγητής εξηγεί τον κανόνα στους μαθητές.", "The professor explains the rule to the students."),
    "A1-U00-021": ("Σημειώστε μόνο το σωστό στο φύλλο απαντήσεων.", "Mark only the correct one on the answer sheet."),
    "A1-U00-022": ("Αν κάνετε λάθος, διαγράψτε τη λέξη καθαρά.", "If you make a mistake, cross out the word clearly."),
    "A1-U00-023": ("Διαβάστε τις προτάσεις και γράψτε Σωστό ή Λάθος.", "Read the sentences and write True or False."),
    "A1-U00-024": ("Στην πολλαπλή επιλογή επιλέγουμε μία μόνο σωστή απάντηση.", "In multiple choice we choose only one correct answer."),
    "A1-U00-025": ("Συμπληρώστε τα κενά με τα κατάλληλα άρθρα.", "Fill in the blanks with the appropriate articles."),
    "A1-U00-026": ("Αντιστοιχίστε κάθε επάγγελμα με τον κατάλληλο χώρο εργασίας.", "Match each profession with the appropriate workplace."),
    "A1-U00-027": ("Κυκλώστε το σωστό για κάθε αριθμημένη ερώτηση.", "Circle the correct one for each numbered question."),
    "A1-U00-028": ("Βάλτε στη σωστή σειρά τις ημέρες της εβδομάδας.", "Put the days of the week in the correct order."),
    "A1-U00-029": ("Απαντήστε στις ερωτήσεις με δύο ή τρεις λέξεις.", "Answer the questions with two or three words."),
    "A1-U00-030": ("Διαλέξτε τη σωστή απάντηση μετά από κάθε διάλογο.", "Pick the correct answer after each dialogue."),
    "A1-U00-031": ("Σημειώστε με ένα τικ αν η δήλωση είναι σωστή.", "Mark with a checkmark if the statement is correct."),
    "A1-U00-032": ("Η εξέταση επιπέδου Α1 περιλαμβάνει τέσσερις δεξιότητες.", "The level A1 examination includes four skills."),
    "A1-U00-033": ("Το τεστ αρχίζει ακριβώς στις εννέα το πρωί.", "The test starts at nine sharp in the morning."),
    "A1-U00-034": ("Ακολουθήστε τις οδηγίες του επιτηρητή της αίθουσας.", "Follow the instructions of the room proctor."),
    "A1-U00-035": ("Αν έχετε κάποια ερώτηση, σηκώστε το χέρι σας.", "If you have any question, raise your hand."),
    "A1-U00-036": ("Κάθε απάντηση πρέπει να είναι καθαρά γραμμένη.", "Each answer must be clearly written."),
    "A1-U00-037": ("Στο θέμα δύο γράφουμε μία πρόσκληση σε φίλο.", "In task two we write an invitation to a friend."),
    "A1-U00-038": ("Το παράδειγμα σας δείχνει πώς να απαντήσετε.", "The example shows you how to answer."),
    "A1-U00-039": ("Διαβάζουμε το κείμενο δύο φορές με προσοχή.", "We read the text twice with attention."),
    "A1-U00-040": ("Ο διάλογος γίνεται σε ένα εστιατόριο.", "The dialogue takes place in a restaurant."),
    "A1-U00-041": ("Κάθε πρόταση αρχίζει με κεφαλαίο γράμμα.", "Every sentence starts with a capital letter."),
    "A1-U00-042": ("Γράψτε τη σωστή λέξη κάτω από την εικόνα.", "Write the correct word under the picture."),
    "A1-U00-043": ("Μην αφήνετε κανένα κενό χωρίς απάντηση.", "Do not leave any blank without an answer."),
    "A1-U00-044": ("Κοιτάξτε την εικόνα και απαντήστε στις ερωτήσεις.", "Look at the picture and answer the questions."),
    "A1-U00-045": ("Περιγράψτε τη φωτογραφία στον εξεταστή.", "Describe the photograph to the examiner."),
    "A1-U00-046": ("Κοιτάξτε τον πίνακα με τις ώρες των δρομολογίων.", "Look at the table with the timetable of itineraries."),
    "A1-U00-047": ("Συμπληρώστε τη σωστή λέξη στην τρίτη στήλη.", "Fill in the correct word in the third column."),
    "A1-U00-048": ("Μην γράφετε έξω από τη γραμμή.", "Do not write outside the line."),
    "A1-U00-049": ("Η βάση για την επιτυχία είναι ο βαθμός δέκα.", "The passing mark for success is grade ten."),
    "A1-U00-050": ("Η βαθμολογία ανακοινώνεται στην ιστοσελίδα του ΚΕΓ.", "The grades are announced on the KEG website."),
    "A1-U00-051": ("Έχετε αρκετό χρόνο για να απαντήσετε σε όλα.", "You have enough time to answer everything."),
    "A1-U00-052": ("Γυρίστε στη σελίδα πέντε του φυλλαδίου.", "Turn to page five of the booklet."),
    "A1-U00-053": ("Αυτή η άσκηση έχει πέντε ερωτήσεις.", "This exercise has five questions."),
    "A1-U00-054": ("Η κατανόηση γραπτού λόγου περιλαμβάνει σύντομες αγγελίες και σημειώματα.", "Reading comprehension includes short classified ads and notes."),
    "A1-U00-055": ("Στην κατανόηση προφορικού λόγου ακούτε κάθε ηχογράφηση δύο φορές.", "In listening comprehension you hear each recording twice."),
    "A1-U00-056": ("Στην παραγωγή γραπτού λόγου προσέχετε την ορθογραφία και τους τόνους.", "In written production pay attention to spelling and stress accents."),
    "A1-U00-057": ("Στην παραγωγή προφορικού λόγου μιλάτε για την οικογένεια και τα χόμπι σας.", "In oral production you talk about your family and your hobbies."),
    "A1-U00-058": ("Οι εξετάσεις πολιτογράφησης απαιτούν βασική γνώση ελληνικών.", "Citizenship examinations require basic knowledge of Greek."),
    "A1-U00-059": ("Μαθαίνουμε τους βασικούς κανόνες γραμματικής στο επίπεδο Α1.", "We learn the basic grammar rules at level A1."),
    "A1-U00-060": ("Βάλτε το ουσιαστικό στη σωστή πτώση.", "Put the noun in the correct case."),
    "A1-U00-061": ("Κλίνουμε το ρήμα στον ενεστώτα.", "We conjugate the verb in the present tense."),
    "A1-U00-062": ("Το επίθετο μπαίνει συνήθως πριν από το ουσιαστικό.", "The adjective usually comes before the noun."),
    "A1-U00-063": ("Μην ξεχνάτε το άρθρο μπροστά από το ουσιαστικό.", "Do not forget the article in front of the noun."),
    "A1-U00-064": ("Η λέξη 'το παιδί' είναι στον ενικό αριθμό.", "The word 'το παιδί' is in the singular number."),
    "A1-U00-065": ("Ποιος είναι ο πληθυντικός αριθμός της λέξης 'ο καφές';", "What is the plural number of the word 'ο καφές'?")
}

def process_unit_00():
    yaml_path = CONTENT_DIR / "unit-00" / "lesson-01.yaml"
    if not yaml_path.exists():
        print(f"[ERROR] {yaml_path} does not exist.")
        return
        
    with open(yaml_path, "r", encoding="utf-8") as f:
        ydata = yaml.safe_load(f)
        
    entries = ydata.get("entries", [])
    print(f"\n=== Processing unit-00 ({len(entries)} cards) ===")
    
    total_new_sentences = 0
    total_audio_synthesized = 0
    
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
        if cid in U00_EXAMPLES_2:
            ex2_el, ex2_en = U00_EXAMPLES_2[cid]
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
    print(f"[OK] Saved unit-00 with 2 example sentences and audio references.")
    print(f"\nUnit 00 Complete! Added {total_new_sentences} sentences, synthesized {total_audio_synthesized} audio files.")

if __name__ == "__main__":
    process_unit_00()

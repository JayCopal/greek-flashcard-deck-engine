# -*- coding: utf-8 -*-
"""
Enrich Units 7, 8, and 9 with authentic second example sentences (KEG A1 Exam)
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

U07_EXAMPLES_2 = {
    "A1-U07-001": ("Το σπίτι μας έχει τρία υπνοδωμάτια και κήπο.", "Our house has three bedrooms and a garden."),
    "A1-U07-002": ("Το διαμέρισμα είναι στον τρίτο όροφο.", "The apartment is on the third floor."),
    "A1-U07-003": ("Η πολυκατοικία έχει καινούριο ασανσέρ.", "The apartment building has a new elevator."),
    "A1-U07-004": ("Το δωμάτιό μου είναι πάντα καθαρό και τακτοποιημένο.", "My room is always clean and tidy."),
    "A1-U07-005": ("Πόσο κοστίζει το δωμάτιο στο ξενοδοχείο;", "How much does the room in the hotel cost?"),
    "A1-U07-006": ("Σε ποιον όροφο είναι το γραφείο σας;", "On which floor is your office?"),
    "A1-U07-007": ("Το διαμέρισμα στο ισόγειο έχει μικρή αυλή.", "The ground floor apartment has a small courtyard."),
    "A1-U07-008": ("Πίνουμε καφέ στο μπαλκόνι κάθε πρωί.", "We drink coffee on the balcony every morning."),
    "A1-U07-009": ("Το σπίτι έχει έναν μεγάλο κήπο με δέντρα.", "The house has a large garden with trees."),
    "A1-U07-010": ("Έχουμε έναν άνετο καναπέ στο σαλόνι.", "We have a comfortable couch in the living room."),
    "A1-U07-011": ("Η κουζίνα έχει ψυγείο, φούρνο και τραπέζι.", "The kitchen has a fridge, oven, and table."),
    "A1-U07-012": ("Η κρεβατοκάμαρα έχει μία μεγάλη ντουλάπα.", "The bedroom has a large wardrobe."),
    "A1-U07-013": ("Το σπίτι έχει δύο μπάνια.", "The house has two bathrooms."),
    "A1-U07-014": ("Ο διάδρομος είναι μακρύς και φωτεινός.", "The corridor is long and bright."),
    "A1-U07-015": ("Η εξώπορτα της πολυκατοικίας είναι κλειστή.", "The building's front door is closed."),
    "A1-U07-016": ("Κλείνω το παράθυρο γιατί κάνει κρύο.", "I close the window because it is cold."),
    "A1-U07-017": ("Το διαμέρισμα νοικιάζεται χωρίς έπιπλα.", "The apartment is rented without furniture."),
    "A1-U07-018": ("Στρώνω το κρεβάτι μου κάθε πρωί.", "I make my bed every morning."),
    "A1-U07-019": ("Ο καναπές στο σαλόνι γίνεται κρεβάτι.", "The couch in the living room turns into a bed."),
    "A1-U07-020": ("Κάθομαι στην αναπαυτική πολυθρόνα.", "I sit in the comfortable armchair."),
    "A1-U07-021": ("Βάζω την καρέκλα δίπλα στο γραφείο.", "I put the chair next to the desk."),
    "A1-U07-022": ("Η ντουλάπα στην κρεβατοκάμαρα είναι μεγάλη.", "The wardrobe in the bedroom is large."),
    "A1-U07-023": ("Το ψυγείο είναι γεμάτο φρέσκα τρόφιμα.", "The fridge is full of fresh food."),
    "A1-U07-024": ("Βάζω τα ρούχα στο πλυντήριο.", "I put the clothes in the washing machine."),
    "A1-U07-025": ("Δεν ανοίγω την τηλεόραση όταν διαβάζω.", "I do not turn on the television when I study."),
    "A1-U07-026": ("Ανάβω το φωτιστικό γιατί σκοτεινιάζει.", "I turn on the lamp because it gets dark."),
    "A1-U07-027": ("Καθαρίζω το χαλί με την ηλεκτρική σκούπα.", "I clean the rug with the vacuum cleaner."),
    "A1-U07-028": ("Βάζω τα ρούχα μέσα στη βαλίτσα.", "I put the clothes inside the suitcase."),
    "A1-U07-029": ("Συναντιόμαστε έξω από τον κινηματογράφο.", "We meet outside the cinema."),
    "A1-U07-030": ("Τα κλειδιά είναι πάνω στο κομοδίνο.", "The keys are on the nightstand."),
    "A1-U07-031": ("Τα παπούτσια είναι κάτω από την καρέκλα.", "The shoes are under the chair."),
    "A1-U07-032": ("Το φαρμακείο είναι δίπλα στον φούρνο.", "The pharmacy is next to the bakery."),
    "A1-U07-033": ("Μένω ακριβώς απέναντι από το σχολείο.", "I live right across from the school."),
    "A1-U07-034": ("Σταματάω μπροστά από την είσοδο.", "I stop in front of the entrance."),
    "A1-U07-035": ("Το πάρκινγκ είναι πίσω από το κτίριο.", "The parking is behind the building."),
    "A1-U07-036": ("Η τράπεζα είναι ανάμεσα στο καφέ και το σούπερ μάρκετ.", "The bank is between the cafe and the supermarket."),
    "A1-U07-037": ("Πληρώνω το ενοίκιο την πρώτη μέρα του μήνα.", "I pay the rent on the first day of the month."),
    "A1-U07-038": ("Παίρνω το ασανσέρ για τον πέμπτο όροφο.", "I take the elevator to the fifth floor."),
    "A1-U07-039": ("Το χειμώνα ανάβουμε τη θέρμανση.", "In winter we turn on the heating."),
    "A1-U07-040": ("Ο φίλος μου νοικιάζει ένα μικρό στούντιο.", "My friend is renting a small studio."),
    "A1-U07-041": ("Υπάρχει ελεύθερο δωμάτιο για απόψε;", "Is there a vacant room for tonight?"),
    "A1-U07-042": ("Το σαλόνι είναι πολύ φωτεινό το πρωί.", "The living room is very bright in the morning."),
    "A1-U07-043": ("Ψάχνω ένα επιπλωμένο διαμέρισμα με δύο δωμάτια.", "I am looking for a furnished two-room apartment."),
    "A1-U07-044": ("Ενοικιάζεται γκαρσονιέρα πλήρως ανακαινισμένη.", "Studio apartment for rent, fully renovated."),
    "A1-U07-045": ("Πωλείται διαμέρισμα εκατό τετραγωνικών μέτρων.", "Apartment of one hundred square meters for sale.")
}

U08_EXAMPLES_2 = {
    "A1-U08-001": ("Τι πρόγραμμα έχεις για το σαββατοκύριακο;", "What schedule do you have for the weekend?"),
    "A1-U08-002": ("Είναι καλή συνήθεια να περπατάμε κάθε μέρα.", "It is a good habit to walk every day."),
    "A1-U08-003": ("Κάθε πρωί πίνω έναν ζεστό καφέ.", "Every morning I drink a hot coffee."),
    "A1-U08-004": ("Το μεσημέρι γυρίζω στο σπίτι για φαγητό.", "At noon I return home for food."),
    "A1-U08-005": ("Το απόγευμα πηγαίνω στο γυμναστήριο.", "In the afternoon I go to the gym."),
    "A1-U08-006": ("Το βράδυ μαγειρεύω κάτι απλό και βλέπω τηλεόραση.", "In the evening I cook something simple and watch television."),
    "A1-U08-007": ("Καληνύχτα και καλό ξημέρωμα!", "Good night and have a good dawn!"),
    "A1-U08-008": ("Τι τρως συνήθως για πρωινό;", "What do you usually eat for breakfast?"),
    "A1-U08-009": ("Ετοιμάζω μεσημεριανό για όλη την οικογένεια.", "I prepare lunch for the whole family."),
    "A1-U08-010": ("Μετά το βραδινό πίνω ένα ζεστό τσάι.", "After dinner I drink a hot tea."),
    "A1-U08-011": ("Κάνουμε διάλειμμα δεκαπέντε λεπτών.", "We take a fifteen-minute break."),
    "A1-U08-012": ("Πότε τελειώνει το σημερινό μάθημα;", "When does today's lesson end?"),
    "A1-U08-013": ("Η ταινία αρχίζει στις εννέα το βράδυ.", "The film begins at nine in the evening."),
    "A1-U08-014": ("Τελειώνω τη δουλειά στις πέντε το απόγευμα.", "I finish work at five in the afternoon."),
    "A1-U08-015": ("Διαβάζω τα νέα στο διαδίκτυο.", "I read the news on the internet."),
    "A1-U08-016": ("Ακούω την καθηγήτρια με προσοχή.", "I listen to the teacher with attention."),
    "A1-U08-017": ("Βλέπω έναν φίλο μου στον δρόμο.", "I see a friend of mine on the street."),
    "A1-U08-018": ("Ποιος μαγειρεύει σήμερα το μεσημέρι;", "Who is cooking this afternoon?"),
    "A1-U08-019": ("Φεύγετε τώρα για το αεροδρόμιο;", "Are you leaving now for the airport?"),
    "A1-U08-020": ("Γυρίζουμε στο σπίτι με τα πόδια.", "We return home on foot."),
    "A1-U08-021": ("Ψωνίζω φρούτα και λαχανικά από το σούπερ μάρκετ.", "I shop for fruits and vegetables from the supermarket."),
    "A1-U08-022": ("Τι ώρα ξυπνάς τα σαββατοκύριακα;", "What time do you wake up on weekends?"),
    "A1-U08-023": ("Περπατάμε μέχρι την πλατεία για έναν καφέ.", "We walk up to the square for a coffee."),
    "A1-U08-024": ("Η Άννα τραγουδάει πολύ ωραία.", "Anna sings very beautifully."),
    "A1-U08-025": ("Δεν οδηγώ αυτοκίνητο στην Αθήνα, παίρνω το μετρό.", "I do not drive a car in Athens, I take the metro."),
    "A1-U08-026": ("Ζείτε μόνιμα στην Ελλάδα;", "Do you live permanently in Greece?"),
    "A1-U08-027": ("Μπορείτε να επαναλάβετε την ερώτηση, παρακαλώ;", "Can you repeat the question, please?"),
    "A1-U08-028": ("Παίρνουμε πρωινό μαζί στο μπαλκόνι.", "We have breakfast together on the balcony."),
    "A1-U08-029": ("Κάνω ένα ζεστό μπάνιο το βράδυ.", "I take a warm bath in the evening."),
    "A1-U08-030": ("Κάνει γυμναστική κάθε μέρα πριν τη δουλειά.", "He exercises every day before work."),
    "A1-U08-031": ("Στις δώδεκα κάνουμε διάλειμμα για φαγητό.", "At twelve we take a break for food."),
    "A1-U08-032": ("Είμαι κουρασμένος και πάω για ύπνο νωρίς.", "I am tired and I am going to bed early."),
    "A1-U08-033": ("Λέω πάντα την αλήθεια στους φίλους μου.", "I always tell the truth to my friends."),
    "A1-U08-034": ("Τι κάνετε συνήθως τις Κυριακές;", "What do you usually do on Sundays?"),
    "A1-U08-035": ("Επισκέπτομαι συχνά τους γονείς μου.", "I frequently visit my parents."),
    "A1-U08-036": ("Μερικές φορές πηγαίνουμε σε ελληνικές ταβέρνες.", "Sometimes we go to Greek tavernas."),
    "A1-U08-037": ("Βλέπω σπάνια τηλεόραση τις καθημερινές.", "I rarely watch TV on weekdays."),
    "A1-U08-038": ("Δεν τρώω ποτέ κρέας το βράδυ.", "I never eat meat in the evening."),
    "A1-U08-039": ("Πίνω δύο λίτρα νερό κάθε μέρα.", "I drink two liters of water every day."),
    "A1-U08-040": ("Φτάνω νωρίς στο μάθημα για να βρω θέση.", "I arrive early to class to find a seat."),
    "A1-U08-041": ("Είναι πολύ αργά, πρέπει να φύγω.", "It is very late, I must leave."),
    "A1-U08-042": ("Θέλουμε να ταξιδέψουμε στην Ελλάδα το καλοκαίρι.", "We want to travel to Greece in the summer.")
}

U09_EXAMPLES_2 = {
    "A1-U09-001": ("Είναι μία η ώρα το μεσημέρι.", "It is one o'clock in the afternoon."),
    "A1-U09-002": ("Περιμένετε ένα λεπτό, παρακαλώ.", "Wait a minute, please."),
    "A1-U09-003": ("Η πτήση αναχωρεί στις έξι και τέταρτο.", "The flight departs at a quarter past six."),
    "A1-U09-004": ("Το μάθημα αρχίζει στις εννέα και μισή.", "The class starts at half past nine."),
    "A1-U09-005": ("Είναι δέκα παρά δέκα το πρωί.", "It is ten to ten in the morning."),
    "A1-U09-006": ("Συναντιόμαστε στις επτά ακριβώς έξω από το θέατρο.", "We meet at seven sharp outside the theater."),
    "A1-U09-007": ("Το ραντεβού μας είναι στις δύο το μεσημέρι.", "Our appointment is at two in the afternoon."),
    "A1-U09-008": ("Έχετε ραντεβού με τη γραμματέα;", "Do you have an appointment with the secretary?"),
    "A1-U09-009": ("Αυτό το ρολόι τοίχου είναι παλιό.", "This wall clock is old."),
    "A1-U09-010": ("Πόσες ώρες δουλεύεις την εβδομάδα;", "How many hours do you work a week?"),
    "A1-U09-011": ("Τι κάνεις συνήθως το σαββατοκύριακο;", "What do you usually do on the weekend?"),
    "A1-U09-012": ("Τη Δευτέρα έχουμε πολλή δουλειά στο γραφείο.", "On Monday we have a lot of work at the office."),
    "A1-U09-013": ("Την Τρίτη το απόγευμα πηγαίνω για τρέξιμο.", "On Tuesday afternoon I go for a run."),
    "A1-U09-014": ("Την Τετάρτη έχω συνάντηση με τον καθηγητή.", "On Wednesday I have a meeting with the professor."),
    "A1-U09-015": ("Την Πέμπτη το βράδυ τρώμε μαζί με φίλους.", "On Thursday evening we eat together with friends."),
    "A1-U09-016": ("Η Παρασκευή είναι η αγαπημένη μου μέρα.", "Friday is my favorite day."),
    "A1-U09-017": ("Το Σάββατο το βράδυ πάμε σε μία συναυλία.", "On Saturday evening we go to a concert."),
    "A1-U09-018": ("Την Κυριακή το πρωί πίνουμε καφέ με την οικογένεια.", "On Sunday morning we drink coffee with the family."),
    "A1-U09-019": ("Στην Ελλάδα κάθε εποχή έχει τις ομορφιές της.", "In Greece every season has its beauties."),
    "A1-U09-020": ("Την άνοιξη ανθίζουν τα λουλούδια στους κήπους.", "In spring the flowers bloom in the gardens."),
    "A1-U09-021": ("Το καλοκαίρι κάνει πολλή ζέστη στην Αθήνα.", "In summer it is very hot in Athens."),
    "A1-U09-022": ("Το φθινόπωρο πέφτουν τα φύλλα από τα δέντρα.", "In autumn the leaves fall from the trees."),
    "A1-U09-023": ("Τον χειμώνα φοράμε ζεστά παλτά και σκούφους.", "In winter we wear warm coats and beanies."),
    "A1-U09-024": ("Ποιος μήνας είναι ο πιο ζεστός;", "Which month is the warmest?"),
    "A1-U09-025": ("Πόσων χρονών είσαι φέτος;", "How old are you this year?"),
    "A1-U09-026": ("Σημειώνω την ημερομηνία στο ημερολόγιό μου.", "I note the date in my calendar."),
    "A1-U09-027": ("Ο Ιανουάριος είναι ο πρώτος μήνας του χρόνου.", "January is the first month of the year."),
    "A1-U09-028": ("Τον Απρίλιο ο καιρός είναι συνήθως ήπιος.", "In April the weather is usually mild."),
    "A1-U09-029": ("Τον Ιούλιο κλείνουν τα σχολεία για καλοκαίρι.", "In July the schools close for summer."),
    "A1-U09-030": ("Ο Αύγουστος είναι ο μήνας των διακοπών.", "August is the vacation month."),
    "A1-U09-031": ("Τον Δεκέμβριο στολίζουμε το χριστουγεννιάτικο δέντρο.", "In December we decorate the Christmas tree."),
    "A1-U09-032": ("Πρέπει να φύγω πριν από το μεσημέρι.", "I must leave before noon."),
    "A1-U09-033": ("Τι κάνεις μετά από τη δουλειά;", "What do you do after work?"),
    "A1-U09-034": ("Δουλεύω από τη Δευτέρα μέχρι την Παρασκευή.", "I work from Monday until Friday."),
    "A1-U09-035": ("Τι μέρα είναι σήμερα;", "What day is today?"),
    "A1-U09-036": ("Αύριο είναι αργία και τα καταστήματα είναι κλειστά.", "Tomorrow is a public holiday and the shops are closed."),
    "A1-U09-037": ("Χθες είναι Κυριακή και μένω στο σπίτι.", "Yesterday is Sunday and I stay at home."),
    "A1-U09-038": ("Τώρα διαβάζουμε για τις εξετάσεις ελληνικών.", "Now we are studying for the Greek exams."),
    "A1-U09-039": ("Κλείνω ραντεβού στον οδοντίατρο για την επόμενη εβδομάδα.", "I make an appointment at the dentist for next week."),
    "A1-U09-040": ("Περιμένω το λεωφορείο στη στάση.", "I am waiting for the bus at the stop."),
    "A1-U09-041": ("Συναντώ έναν παλιό μου συμμαθητή στον δρόμο.", "I meet an old classmate of mine on the street."),
    "A1-U09-042": ("Δεν προλαβαίνω να πάρω πρωινό σήμερα.", "I don't have time to have breakfast today.")
}

BATCH_C_MAPS = {
    "unit-07": U07_EXAMPLES_2,
    "unit-08": U08_EXAMPLES_2,
    "unit-09": U09_EXAMPLES_2,
}

def process_batch_c():
    total_new_sentences = 0
    total_audio_synthesized = 0

    for uid, ex2_map in BATCH_C_MAPS.items():
        yaml_path = CONTENT_DIR / uid / "lesson-01.yaml"
        if not yaml_path.exists():
            print(f"[WARN] {yaml_path} does not exist, skipping.")
            continue
            
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

    print(f"\nBatch C Complete! Added {total_new_sentences} sentences, synthesized {total_audio_synthesized} audio files.")

if __name__ == "__main__":
    process_batch_c()

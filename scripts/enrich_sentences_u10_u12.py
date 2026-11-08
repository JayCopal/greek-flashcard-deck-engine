# -*- coding: utf-8 -*-
"""
Enrich Units 10, 11, and 12 with authentic second example sentences (KEG A1 Exam)
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

U10_EXAMPLES_2 = {
    "A1-U10-001": ("Περνάμε τον δρόμο προσεκτικά.", "We cross the street carefully."),
    "A1-U10-002": ("Πού βρίσκεται η οδός Ακαδημίας;", "Where is Akadimias Street located?"),
    "A1-U10-003": ("Τα παιδιά παίζουν στην κεντρική πλατεία.", "The children play in the central square."),
    "A1-U10-004": ("Στρίβουμε δεξιά στην επόμενη γωνία.", "We turn right at the next corner."),
    "A1-U10-005": ("Σταματάμε στο κόκκινο φανάρι.", "We stop at the red light."),
    "A1-U10-006": ("Περπατάμε στο φαρδύ πεζοδρόμιο.", "We walk on the wide sidewalk."),
    "A1-U10-007": ("Σταματήστε στη διάβαση πεζών, παρακαλώ.", "Stop at the pedestrian crossing, please."),
    "A1-U10-008": ("Πάμε για ψώνια στο κέντρο της Αθήνας.", "We go shopping in downtown Athens."),
    "A1-U10-009": ("Πρέπει να πάω στην τράπεζα για μία συναλλαγή.", "I must go to the bank for a transaction."),
    "A1-U10-010": ("Στέλνω ένα δέμα από το ταχυδρομείο.", "I send a parcel from the post office."),
    "A1-U10-011": ("Αγοράζω παυσίπονα από το φαρμακείο.", "I buy painkillers from the pharmacy."),
    "A1-U10-012": ("Η αδελφή μου εργάζεται ως νοσοκόμα στο νοσοκομείο.", "My sister works as a nurse in the hospital."),
    "A1-U10-013": ("Επισκεπτόμαστε το Μουσείο της Ακρόπολης.", "We visit the Acropolis Museum."),
    "A1-U10-014": ("Το ξενοδοχείο περιλαμβάνει πρωινό στην τιμή.", "The hotel includes breakfast in the price."),
    "A1-U10-015": ("Αγοράζω εφημερίδα και τσίχλες από το περίπτερο.", "I buy a newspaper and gum from the kiosk."),
    "A1-U10-016": ("Πού είναι το πλησιέστερο αστυνομικό τμήμα;", "Where is the nearest police station?"),
    "A1-U10-017": ("Το μετρό της Αθήνας είναι γρήγορο και καθαρό.", "The Athens metro is fast and clean."),
    "A1-U10-018": ("Ποιο λεωφορείο πάει στο αεροδρόμιο;", "Which bus goes to the airport?"),
    "A1-U10-019": ("Το τρένο φτάνει στην ώρα του.", "The train arrives on time."),
    "A1-U10-020": ("Το τραμ περνάει δίπλα από τη θάλασσα.", "The tram passes next to the sea."),
    "A1-U10-021": ("Βρίσκουμε εύκολα ταξί στην πιάτσα.", "We easily find a taxi at the taxi rank."),
    "A1-U10-022": ("Το πλοίο αναχωρεί στις οκτώ το πρωί.", "The ship departs at eight in the morning."),
    "A1-U10-023": ("Φοβάμαι να ταξιδέψω με το αεροπλάνο.", "I am afraid of traveling by plane."),
    "A1-U10-024": ("Συναντιόμαστε στον κεντρικό σιδηροδρομικό σταθμό.", "We meet at the central railway station."),
    "A1-U10-025": ("Κατεβαίνω στην τρίτη στάση μετά την πλατεία.", "I get off at the third stop after the square."),
    "A1-U10-026": ("Πόσο κοστίζει το εισιτήριο για το μουσείο;", "How much does the ticket to the museum cost?"),
    "A1-U10-027": ("Ένα απλό εισιτήριο κοστίζει ένα ευρώ και είκοσι λεπτά.", "A single ticket costs one euro and twenty cents."),
    "A1-U10-028": ("Είναι φθηνότερο να βγάλετε εισιτήριο μετ' επιστροφής.", "It is cheaper to get a return ticket."),
    "A1-U10-029": ("Αλλάζουμε γραμμή στον σταθμό Σύνταγμα.", "We change lines at Syntagma station."),
    "A1-U10-030": ("Περιμένουμε το τρένο στην αποβάθρα ένα.", "We are waiting for the train at platform one."),
    "A1-U10-031": ("Συνεχίζετε ευθεία μέχρι να δείτε την εκκλησία.", "Continue straight until you see the church."),
    "A1-U10-032": ("Το κατάστημα είναι στο δεξί σας χέρι.", "The shop is on your right-hand side."),
    "A1-U10-033": ("Στρίβω αριστερά στο φανάρι.", "I turn left at the traffic light."),
    "A1-U10-034": ("Μένω πολύ κοντά στη δουλειά μου.", "I live very close to my work."),
    "A1-U10-035": ("Το σπίτι μου είναι μακριά από τη θάλασσα.", "My house is far from the sea."),
    "A1-U10-036": ("Το καφέ είναι απέναντι από το πάρκο.", "The cafe is across from the park."),
    "A1-U10-037": ("Είναι κοντά, πάμε με τα πόδια;", "It's close, shall we go on foot?"),
    "A1-U10-038": ("Στρίβετε δεξιά στην οδό Πανεπιστημίου.", "Turn right onto Panepistimiou Street."),
    "A1-U10-039": ("Περνάω κάθε μέρα έξω από το σχολείο σας.", "I pass by outside your school every day."),
    "A1-U10-040": ("Κατεβαίνω στο κέντρο για δουλειές.", "I go down to the city center for errands."),
    "A1-U10-041": ("Ανεβαίνω τις σκάλες με τα πόδια.", "I climb the stairs on foot."),
    "A1-U10-042": ("Ψάχνω ένα καλό εστιατόριο στην περιοχή.", "I am looking for a good restaurant in the area.")
}

U11_EXAMPLES_2 = {
    "A1-U11-001": ("Τι καιρό κάνει σήμερα στη Θεσσαλονίκη;", "What is the weather like today in Thessaloniki?"),
    "A1-U11-002": ("Φοράω γυαλιά ηλίου όταν έχει δυνατό ήλιο.", "I wear sunglasses when there is strong sun."),
    "A1-U11-003": ("Μετά τη βροχή ο αέρας είναι καθαρός.", "After the rain the air is clean."),
    "A1-U11-004": ("Τα παιδιά φτιάχνουν έναν χιονάνθρωπο στο χιόνι.", "The children are making a snowman in the snow."),
    "A1-U11-005": ("Έχει πολύ δυνατό αέρα σήμερα στην παραλία.", "There is very strong wind today at the beach."),
    "A1-U11-006": ("Ο ουρανός είναι γεμάτος άσπρα σύννεφα.", "The sky is full of white clouds."),
    "A1-U11-007": ("Δεν μου αρέσει η συννεφιά, προτιμώ τον ήλιο.", "I do not like cloudy weather, I prefer the sun."),
    "A1-U11-008": ("Η θερμοκρασία πέφτει το βράδυ.", "The temperature drops at night."),
    "A1-U11-009": ("Σήμερα η θερμοκρασία είναι τριάντα βαθμοί.", "Today the temperature is thirty degrees."),
    "A1-U11-010": ("Το καλοκαίρι κάνει υπερβολική ζέστη.", "In the summer it is excessively hot."),
    "A1-U11-011": ("Κλείστε την πόρτα γιατί κάνει κρύο.", "Close the door because it is cold."),
    "A1-U11-012": ("Σήμερα έχει λαμπερό ήλιο και καθαρό ουρανό.", "Today there is bright sun and clear sky."),
    "A1-U11-013": ("Βρέχει ασταμάτητα από το πρωί.", "It has been raining non-stop since morning."),
    "A1-U11-014": ("Τον χειμώνα χιονίζει συχνά στα βουνά.", "In the winter it snows frequently in the mountains."),
    "A1-U11-015": ("Σήμερα δεν φυσάει καθόλου.", "Today there is no wind at all."),
    "A1-U11-016": ("Έχω λίγο ελεύθερο χρόνο τα απογεύματα.", "I have a little free time in the afternoons."),
    "A1-U11-017": ("Πότε αρχίζουν οι καλοκαιρινές διακοπές;", "When do summer vacations begin?"),
    "A1-U11-018": ("Η παραλία είναι γεμάτη ομπρέλες και ξαπλώστρες.", "The beach is full of umbrellas and sunbeds."),
    "A1-U11-019": ("Μου αρέσει να κοιτάζω τη γαλάζια θάλασσα.", "I like looking at the blue sea."),
    "A1-U11-020": ("Το σαββατοκύριακο πάμε εκδρομή στο βουνό.", "On the weekend we go on an excursion to the mountain."),
    "A1-U11-021": ("Πολλά ελληνικά νησιά έχουν γραφικά χωριά.", "Many Greek islands have picturesque villages."),
    "A1-U11-022": ("Ετοιμάζω τις βαλίτσες για το ταξίδι.", "I prepare the suitcases for the trip."),
    "A1-U11-023": ("Κάνουμε μία βόλτα στα σοκάκια του νησιού.", "We take a stroll in the alleys of the island."),
    "A1-U11-024": ("Βλέπουμε ποδόσφαιρο στην τηλεόραση με φίλους.", "We watch soccer on television with friends."),
    "A1-U11-025": ("Η ελληνική ομάδα μπάσκετ είναι πολύ καλή.", "The Greek basketball team is very good."),
    "A1-U11-026": ("Πάμε συχνά στο θερινό σινεμά το καλοκαίρι.", "We often go to the open-air cinema in the summer."),
    "A1-U11-027": ("Απόψε έχουμε εισιτήρια για το θέατρο.", "Tonight we have tickets for the theater."),
    "A1-U11-028": ("Η συναυλία αρχίζει στις εννέα το βράδυ.", "The concert starts at nine in the evening."),
    "A1-U11-029": ("Μου αρέσει να ακούω χαλαρωτική μουσική.", "I like listening to relaxing music."),
    "A1-U11-030": ("Μπορείτε να μας βγάλετε μία φωτογραφία, παρακαλώ;", "Could you take a photo of us, please?"),
    "A1-U11-031": ("Τα παιδιά παίζουν επιτραπέζια παιχνίδια στο σπίτι.", "The children play board games at home."),
    "A1-U11-032": ("Ταξιδεύω με πλοίο στις Κυκλάδες κάθε χρόνο.", "I travel by ferry to the Cyclades every year."),
    "A1-U11-033": ("Κολυμπάμε κάθε πρωί πριν από τη δουλειά.", "We swim every morning before work."),
    "A1-U11-034": ("Χορεύεις ελληνικούς χορούς;", "Do you dance Greek dances?"),
    "A1-U11-035": ("Ακούω τα αγαπημένα μου τραγούδια στο τηλέφωνο.", "I listen to my favorite songs on the phone."),
    "A1-U11-036": ("Προτιμάτε καφέ ή τσάι;", "Do you prefer coffee or tea?"),
    "A1-U11-037": ("Μου αρέσει πολύ να διαβάζω βιβλία.", "I like reading books very much."),
    "A1-U11-038": ("Μου αρέσουν οι παραδοσιακοί χοροί της Ελλάδας.", "I like traditional dances of Greece."),
    "A1-U11-039": ("Διασκεδάζουμε στα γενέθλια του φίλου μας.", "We have fun at our friend's birthday."),
    "A1-U11-040": ("Ακούω απαλή μουσική για να χαλαρώσω.", "I listen to soft music in order to relax."),
    "A1-U11-041": ("Έχεις το βιβλίο μου; — Ναι, το έχω.", "Do you have my book? — Yes, I have it."),
    "A1-U11-042": ("Βλέπεις τις φωτογραφίες; — Ναι, τις βλέπω.", "Do you see the photos? — Yes, I see them.")
}

U12_EXAMPLES_2 = {
    "A1-U12-001": ("Το ανθρώπινο σώμα χρειάζεται νερό και άσκηση.", "The human body needs water and exercise."),
    "A1-U12-002": ("Φοράω καπέλο για να προστατεύω το κεφάλι μου.", "I wear a hat to protect my head."),
    "A1-U12-003": ("Πίνω ζεστό τσάι με μέλι για τον λαιμό.", "I drink warm tea with honey for my throat."),
    "A1-U12-004": ("Με πονάει το στομάχι όταν πίνω πολύ καφέ.", "My stomach hurts when I drink a lot of coffee."),
    "A1-U12-005": ("Ξαπλώνω γιατί με πονάει η κοιλιά μου.", "I lie down because my belly hurts."),
    "A1-U12-006": ("Πλύνετε τα μάτια σας με καθαρό νερό.", "Wash your eyes with clean water."),
    "A1-U12-007": ("Ο γιατρός εξετάζει το αυτί του παιδιού.", "The doctor examines the child's ear."),
    "A1-U12-008": ("Βάζω σταγόνες στη μύτη για το συνάχι.", "I put drops in my nose for the cold."),
    "A1-U12-009": ("Βουρτσίζω τα δόντια μου και καθαρίζω το στόμα μου.", "I brush my teeth and clean my mouth."),
    "A1-U12-010": ("Πλένω τα δόντια μου δύο φορές την ημέρα.", "I brush my teeth twice a day."),
    "A1-U12-011": ("Δώσε μου το χέρι σου.", "Give me your hand."),
    "A1-U12-012": ("Με πονούν τα πόδια μου μετά από πολλή ορθοστασία.", "My legs hurt after a lot of standing."),
    "A1-U12-013": ("Κάθομαι ίσια για να μην πονάει η πλάτη μου.", "I sit straight so that my back doesn't hurt."),
    "A1-U12-014": ("Το περπάτημα είναι πολύ καλό για την καρδιά.", "Walking is very good for the heart."),
    "A1-U12-015": ("Βάζω το θερμόμετρο για να μετρήσω τον πυρετό.", "I put on the thermometer to measure the fever."),
    "A1-U12-016": ("Παίρνω ένα χάπι για τον δυνατό πονοκέφαλο.", "I take a pill for the severe headache."),
    "A1-U12-017": ("Έχω πονόλαιμο και δεν μπορώ να φάω.", "I have a sore throat and I cannot eat."),
    "A1-U12-018": ("Ο πονόδοντος είναι ανυπόφορος, πάω στον οδοντίατρο.", "The toothache is unbearable, I go to the dentist."),
    "A1-U12-019": ("Έχω συνάχι και χρειάζομαι χαρτομάντιλα.", "I have a runny nose and I need tissues."),
    "A1-U12-020": ("Πολλοί μαθητές έχουν γρίπη αυτόν τον μήνα.", "Many students have the flu this month."),
    "A1-U12-021": ("Πίνω σιρόπι για να σταματήσει ο βήχας.", "I drink syrup to stop the cough."),
    "A1-U12-022": ("Την άνοιξη έχω έντονη αλλεργία στη γύρη.", "In spring I have severe allergy to pollen."),
    "A1-U12-023": ("Το παιδί είναι άρρωστο και μένει στο σπίτι.", "The child is sick and stays home."),
    "A1-U12-024": ("Είμαστε κουρασμένοι μετά από το ταξίδι.", "We are tired after the trip."),
    "A1-U12-025": ("Αγοράζω τα φάρμακά μου από το κοντινό φαρμακείο.", "I buy my medications from the nearby pharmacy."),
    "A1-U12-026": ("Πίνω ένα χάπι με ένα ποτήρι νερό.", "I drink a pill with a glass of water."),
    "A1-U12-027": ("Παίρνω μία ασπιρίνη για τον πυρετό.", "I take an aspirin for the fever."),
    "A1-U12-028": ("Πάρτε μία κουταλιά σιρόπι τρεις φορές την ημέρα.", "Take a spoonful of syrup three times a day."),
    "A1-U12-029": ("Βάζω ένα τσιρότο στο μικρό κόψιμο.", "I put a band-aid on the small cut."),
    "A1-U12-030": ("Χρειαζόμαστε αποστειρωμένη γάζα και επίδεσμο.", "We need sterile gauze and a bandage."),
    "A1-U12-031": ("Το οινόπνευμα καθαρίζει και απολυμαίνει.", "Alcohol cleans and disinfects."),
    "A1-U12-032": ("Ο γιατρός μού γράφει μία συνταγή για αντιβίωση.", "The doctor writes me a prescription for antibiotics."),
    "A1-U12-033": ("Ρωτάω τον φαρμακοποιό πώς να παίρνω το φάρμακο.", "I ask the pharmacist how to take the medicine."),
    "A1-U12-034": ("Το ασθενοφόρο φτάνει σε πέντε λεπτά.", "The ambulance arrives in five minutes."),
    "A1-U12-035": ("Πού πονάτε ακριβώς, κύριε Παπαδόπουλε;", "Where do you hurt exactly, Mr. Papadopoulos?"),
    "A1-U12-036": ("Με πονάει το αυτί μου από το πρωί.", "My ear hurts since morning."),
    "A1-U12-037": ("Πρέπει να μείνετε στο κρεβάτι για τρεις μέρες.", "You must stay in bed for three days."),
    "A1-U12-038": ("Δεν νιώθω καλά σήμερα, ζαλίζομαι.", "I don't feel well today, I am dizzy."),
    "A1-U12-039": ("Βοήθεια, παρακαλώ! Καλέστε έναν γιατρό!", "Help, please! Call a doctor!"),
    "A1-U12-040": ("Είναι επείγον, χρειάζομαι γιατρό αμέσως!", "It is urgent, I need a doctor immediately!"),
    "A1-U12-041": ("Εύχομαι γρήγορη ανάρρωση και περαστικά σου!", "I wish you a speedy recovery and get well soon!"),
    "A1-U12-042": ("Η σωστή διατροφή είναι απαραίτητη για την υγεία.", "Proper nutrition is essential for health.")
}

BATCH_D_MAPS = {
    "unit-10": U10_EXAMPLES_2,
    "unit-11": U11_EXAMPLES_2,
    "unit-12": U12_EXAMPLES_2,
}

def process_batch_d():
    total_new_sentences = 0
    total_audio_synthesized = 0

    for uid, ex2_map in BATCH_D_MAPS.items():
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

    print(f"\nBatch D Complete! Added {total_new_sentences} sentences, synthesized {total_audio_synthesized} audio files.")

if __name__ == "__main__":
    process_batch_d()

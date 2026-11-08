# -*- coding: utf-8 -*-
"""
Enrich Units 4, 5, and 6 with authentic second example sentences (KEG A1 Exam)
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

U04_EXAMPLES_2 = {
    "A1-U04-001": ("Η οικογένειά μου είναι από την Κρήτη.", "My family is from Crete."),
    "A1-U04-002": ("Οι γονείς του μένουν σε ένα όμορφο χωριό.", "His parents live in a beautiful village."),
    "A1-U04-003": ("Πώς λένε τον πατέρα σου;", "What is your father's name?"),
    "A1-U04-004": ("Η μητέρα της δουλεύει σε νοσοκομείο.", "Her mother works in a hospital."),
    "A1-U04-005": ("Ο μπαμπάς μου διαβάζει την εφημερίδα κάθε πρωί.", "My dad reads the newspaper every morning."),
    "A1-U04-006": ("Η μαμά μου μού ετοιμάζει το πρωινό.", "My mom prepares breakfast for me."),
    "A1-U04-007": ("Ο γιος τους πηγαίνει στο δημοτικό σχολείο.", "Their son goes to primary school."),
    "A1-U04-008": ("Πόσο χρονών είναι η κόρη σας;", "How old is your daughter?"),
    "A1-U04-009": ("Έχεις αδελφό ή αδελφή;", "Do you have a brother or sister?"),
    "A1-U04-010": ("Η αδελφή μου είναι φοιτήτρια στην Πάτρα.", "My sister is a university student in Patras."),
    "A1-U04-011": ("Ο παππούς κάθεται στον καναπέ και ξεκουράζεται.", "Grandfather sits on the couch and rests."),
    "A1-U04-012": ("Η γιαγιά μένει μαζί μας στο σπίτι.", "Grandmother lives with us at home."),
    "A1-U04-013": ("Τα παιδιά παίζουν στην αυλή του σχολείου.", "The children play in the schoolyard."),
    "A1-U04-014": ("Το μωρό πίνει γάλα από το μπουκάλι.", "The baby drinks milk from the bottle."),
    "A1-U04-015": ("Ποιος είναι αυτός ο ψηλός άντρας;", "Who is that tall man?"),
    "A1-U04-016": ("Αυτή η γυναίκα είναι δικηγόρος.", "This woman is a lawyer."),
    "A1-U04-017": ("Ο θείος μου έχει ένα μικρό μαγαζί.", "My uncle has a small shop."),
    "A1-U04-018": ("Η θεία Μαρία μαγειρεύει νόστιμα φαγητά.", "Aunt Maria cooks delicious meals."),
    "A1-U04-019": ("Ο ξάδελφός μου είναι πολύ συμπαθητικός.", "My cousin is very likeable."),
    "A1-U04-020": ("Πηγαίνω σινεμά με την ξαδέλφη μου.", "I go to the cinema with my cousin."),
    "A1-U04-021": ("Πόσοι άνθρωποι μένουν σε αυτό το κτίριο;", "How many people live in this building?"),
    "A1-U04-022": ("Είναι παντρεμένος και έχει δύο παιδιά.", "He is married and has two children."),
    "A1-U04-023": ("Είμαι ελεύθερη και μένω μόνη μου.", "I am single and I live alone."),
    "A1-U04-024": ("Πλύνετε το πρόσωπό σας με κρύο νερό.", "Wash your face with cold water."),
    "A1-U04-025": ("Ο αδελφός μου έχει κοντά μαύρα μαλλιά.", "My brother has short black hair."),
    "A1-U04-026": ("Έχει μεγάλα καστανά μάτια.", "She has big brown eyes."),
    "A1-U04-027": ("Ο αδελφός μου είναι πιο ψηλός από μένα.", "My brother is taller than me."),
    "A1-U04-028": ("Φοράει ένα κοντό παντελόνι.", "He is wearing short trousers."),
    "A1-U04-029": ("Η κοπέλα είναι αδύνατη και φοράει γυαλιά.", "The girl is slim and wears glasses."),
    "A1-U04-030": ("Αυτό το βιβλίο είναι πολύ χοντρό.", "This book is very thick."),
    "A1-U04-031": ("Η πόλη της Θεσσαλονίκης είναι πολύ όμορφη.", "The city of Thessaloniki is very beautiful."),
    "A1-U04-032": ("Πολλοί νέοι άνθρωποι ψάχνουν δουλειά.", "Many young people are looking for work."),
    "A1-U04-033": ("Το σπίτι μας έχει ένα μεγάλο σαλόνι.", "Our house has a large living room."),
    "A1-U04-034": ("Ο κύριος Νίκος είναι πολύ καλός γείτονας.", "Mr. Nikos is a very good neighbor."),
    "A1-U04-035": ("Ο νέος καθηγητής είναι ευγενικός και συμπαθητικός.", "The new professor is polite and pleasant."),
    "A1-U04-036": ("Έχεις λίγο χρόνο να μιλήσουμε;", "Do you have a little time for us to talk?"),
    "A1-U04-037": ("Το τηλέφωνό μου είναι στο γραφείο.", "My telephone is in the office."),
    "A1-U04-038": ("Ποιο είναι το όνομά σου;", "What is your name?"),
    "A1-U04-039": ("Το σπίτι της είναι κοντά στον σταθμό.", "Her house is near the station."),
    "A1-U04-040": ("Το διαμέρισμά μας είναι στον δεύτερο όροφο.", "Our apartment is on the second floor.")
}

U05_EXAMPLES_2 = {
    "A1-U05-001": ("Πίνετε ελληνικό καφέ ή φραπέ;", "Do you drink Greek coffee or frappé?"),
    "A1-U05-002": ("Ένα μπουκάλι εμφιαλωμένο νερό, παρακαλώ.", "A bottle of bottled water, please."),
    "A1-U05-003": ("Θέλω ένα ζεστό τσάι με λεμόνι.", "I want a hot tea with lemon."),
    "A1-U05-004": ("Έναν φυσικό χυμό πορτοκάλι, παρακαλώ.", "A fresh orange juice, please."),
    "A1-U05-005": ("Θέλετε πορτοκαλάδα με ανθρακικό ή χωρίς;", "Do you want orangeade with carbonation or without?"),
    "A1-U05-006": ("Μία δροσερή λεμονάδα για μένα, παρακαλώ.", "A cool lemonade for me, please."),
    "A1-U05-007": ("Πίνω έναν καφέ με λίγο γάλα.", "I drink a coffee with a little milk."),
    "A1-U05-008": ("Δύο παγωμένες μπύρες, παρακαλώ.", "Two cold beers, please."),
    "A1-U05-009": ("Προτιμάτε λευκό ή κόκκινο κρασί;", "Do you prefer white or red wine?"),
    "A1-U05-010": ("Πόση ζάχαρη βάζετε στον καφέ σας;", "How much sugar do you put in your coffee?"),
    "A1-U05-011": ("Το φαγητό σε αυτή την ταβέρνα είναι πεντανόστιμο.", "The food in this tavern is delicious."),
    "A1-U05-012": ("Μας φέρνετε λίγο ψωμί ακόμα, παρακαλώ;", "Could you bring us a little more bread, please?"),
    "A1-U05-013": ("Μία πράσινη σαλάτα με ελαιόλαδο, παρακαλώ.", "A green salad with olive oil, please."),
    "A1-U05-014": ("Η χωριάτικη σαλάτα έχει ντομάτα, αγγούρι και φέτα.", "The Greek village salad has tomato, cucumber, and feta."),
    "A1-U05-015": ("Τρώω ψωμί με τυρί και ντομάτα για πρωινό.", "I eat bread with cheese and tomato for breakfast."),
    "A1-U05-016": ("Ένα κομμάτι φέτα με ρίγανη και λάδι, παρακαλώ.", "A piece of feta with oregano and olive oil, please."),
    "A1-U05-017": ("Δεν τρώω κρέας, είμαι χορτοφάγος.", "I don't eat meat, I am a vegetarian."),
    "A1-U05-018": ("Θέλω ψητό κοτόπουλο με πατάτες τηγανητές.", "I want grilled chicken with french fries."),
    "A1-U05-019": ("Το ψάρι είναι φρέσκο σήμερα;", "Is the fish fresh today?"),
    "A1-U05-020": ("Δύο σουβλάκια με πίτα και τζατζίκι, παρακαλώ.", "Two souvlakia with pita and tzatziki, please."),
    "A1-U05-021": ("Μία τυρόπιτα και μία σπανακόπιτα από τον φούρνο.", "One cheese pie and one spinach pie from the bakery."),
    "A1-U05-022": ("Μία μερίδα πατάτες τηγανητές για τα παιδιά.", "One portion of french fries for the children."),
    "A1-U05-023": ("Ένα τοστ με γαλοπούλα και τυρί, παρακαλώ.", "A toast with turkey and cheese, please."),
    "A1-U05-024": ("Τι γλυκό έχετε σήμερα;", "What dessert do you have today?"),
    "A1-U05-025": ("Ένα παγωτό σοκολάτα σε κυπελλάκι, παρακαλώ.", "A chocolate ice cream in a cup, please."),
    "A1-U05-026": ("Οι ηλικιωμένοι παίζουν τάβλι στο καφενείο.", "The elderly men play backgammon at the traditional cafe."),
    "A1-U05-027": ("Συναντιόμαστε στην καφετέρια στην πλατεία.", "We meet at the coffee shop in the square."),
    "A1-U05-028": ("Πάμε σε μία παραδοσιακή ταβέρνα δίπλα στη θάλασσα;", "Shall we go to a traditional taverna next to the sea?"),
    "A1-U05-029": ("Το εστιατόριο ανοίγει στις επτά το απόγευμα.", "The restaurant opens at seven in the evening."),
    "A1-U05-030": ("Ένα τραπέζι έξω στην αυλή, παρακαλώ.", "A table outside in the yard, please."),
    "A1-U05-031": ("Μας φέρνετε τον κατάλογο να παραγγείλουμε;", "Could you bring us the menu so we can order?"),
    "A1-U05-032": ("Μαζί ή χωριστά ο λογαριασμός;", "Together or separate is the bill?"),
    "A1-U05-033": ("Αφήνουμε ένα μικρό φιλοδώρημα στον σερβιτόρο.", "We leave a small tip for the waiter."),
    "A1-U05-034": ("Τι θέλετε να πιείτε;", "What do you want to drink?"),
    "A1-U05-035": ("Πίνω πολύ νερό το καλοκαίρι.", "I drink lots of water in the summer."),
    "A1-U05-036": ("Τι παίρνετε για πρωινό;", "What do you have for breakfast?"),
    "A1-U05-037": ("Τρώμε μεσημεριανό στις δύο το μεσημέρι.", "We eat lunch at two in the afternoon."),
    "A1-U05-038": ("Είστε έτοιμοι να παραγγείλετε;", "Are you ready to order?"),
    "A1-U05-039": ("Ορίστε ο καφές και το νερό σας.", "Here is your coffee and your water."),
    "A1-U05-040": ("Για μένα μία χωριάτικη σαλάτα και ένα νερό.", "For me a Greek salad and a water."),
    "A1-U05-041": ("Καλησπέρα σας, τι θα πάρετε για φαγητό;", "Good evening, what will you have to eat?"),
    "A1-U05-042": ("Σας εύχομαι καλή όρεξη!", "I wish you bon appétit!"),
    "A1-U05-043": ("Στην υγειά σας και καλή διασκέδαση!", "Cheers to your health and have fun!"),
    "A1-U05-044": ("Έναν ελληνικό καφέ μέτριο, παρακαλώ.", "A medium-sweet Greek coffee, please."),
    "A1-U05-045": ("Πίνω πάντα τον καφέ μου σκέτο, χωρίς ζάχαρη.", "I always drink my coffee plain, without sugar.")
}

U06_EXAMPLES_2 = {
    "A1-U06-001": ("Η κεντρική αγορά της πόλης έχει τα πάντα.", "The central market of the city has everything."),
    "A1-U06-002": ("Η λαϊκή αγορά γίνεται κάθε Τετάρτη στη γειτονιά μας.", "The open-air market takes place every Wednesday in our neighborhood."),
    "A1-U06-003": ("Πάω στο σούπερ μάρκετ για τα ψώνια της εβδομάδας.", "I am going to the supermarket for the weekly groceries."),
    "A1-U06-004": ("Παίρνω φρέσκο ψωμί κάθε πρωί από τον φούρνο.", "I get fresh bread every morning from the bakery."),
    "A1-U06-005": ("Ο κρεοπώλης κόβει το κρέας στο κρεοπωλείο.", "The butcher cuts the meat at the butcher shop."),
    "A1-U06-006": ("Αυτό το μαγαζί πουλάει παραδοσιακά προϊόντα.", "This shop sells traditional products."),
    "A1-U06-007": ("Το ελληνικό ελαιόλαδο είναι εξαιρετικής ποιότητας.", "Greek olive oil is of excellent quality."),
    "A1-U06-008": ("Μαγειρεύω κοτόπουλο με ρύζι και λαχανικά.", "I cook chicken with rice and vegetables."),
    "A1-U06-009": ("Τα παιδιά θέλουν μακαρόνια με κιμά και τυρί.", "The children want pasta with minced meat and cheese."),
    "A1-U06-010": ("Ποια φρούτα είναι εποχής το καλοκαίρι;", "Which fruits are in season in the summer?"),
    "A1-U06-011": ("Αγοράζω φρέσκα λαχανικά από τη λαϊκή.", "I buy fresh vegetables from the farmers' market."),
    "A1-U06-012": ("Πόσο κάνουν οι ντομάτες το κιλό;", "How much are tomatoes per kilo?"),
    "A1-U06-013": ("Βάζω αγγούρι και ντομάτα στη σαλάτα.", "I put cucumber and tomato in the salad."),
    "A1-U06-014": ("Κόβω ένα κρεμμύδι για τη σάλτσα.", "I chop an onion for the sauce."),
    "A1-U06-015": ("Τρώω ένα πράσινο μήλο κάθε απόγευμα.", "I eat a green apple every afternoon."),
    "A1-U06-016": ("Αυτά τα πορτοκάλια είναι πολύ γλυκά.", "These oranges are very sweet."),
    "A1-U06-017": ("Θέλω δύο κιλά πατάτες και ένα κιλό μήλα.", "I want two kilos of potatoes and one kilo of apples."),
    "A1-U06-018": ("Βάλτε μου τριακόσια γραμμάρια φέτα, παρακαλώ.", "Give me three hundred grams of feta, please."),
    "A1-U06-019": ("Πόσο κάνει ένα λίτρο γάλα στο σούπερ μάρκετ;", "How much is a liter of milk at the supermarket?"),
    "A1-U06-020": ("Ανοίγω ένα μπουκάλι κόκκινο κρασί.", "I open a bottle of red wine."),
    "A1-U06-021": ("Πόσο κάνει αυτό το πακέτο καφέ;", "How much is this packet of coffee?"),
    "A1-U06-022": ("Πόσο κάνει το κομμάτι;", "How much does each piece cost?"),
    "A1-U06-023": ("Βάζω τα καθαρά ρούχα στη ντουλάπα.", "I put the clean clothes in the wardrobe."),
    "A1-U06-024": ("Ψάχνω ένα τζιν παντελόνι στο νούμερό μου.", "I am looking for a pair of jeans in my size."),
    "A1-U06-025": ("Αυτή η άσπρη μπλούζα είναι από βαμβάκι.", "This white T-shirt is made of cotton."),
    "A1-U06-026": ("Σιδερώνω το πουκάμισό μου για τη δουλειά.", "I iron my shirt for work."),
    "A1-U06-027": ("Χρειάζομαι ένα ζευγάρι αθλητικά παπούτσια.", "I need a pair of athletic shoes."),
    "A1-U06-028": ("Αυτό το πουκάμισο είναι σε μεγάλο μέγεθος;", "Is this shirt available in a large size?"),
    "A1-U06-029": ("Ποιο χρώμα προτιμάτε, το μπλε ή το μαύρο;", "Which color do you prefer, blue or black?"),
    "A1-U06-030": ("Ποια είναι η τελική τιμή με την έκπτωση;", "What is the final price with the discount?"),
    "A1-U06-031": ("Κρατήστε τα ρέστα, ευχαριστώ πολύ.", "Keep the change, thank you very much."),
    "A1-U06-032": ("Κρατάω την απόδειξη για την εγγύηση.", "I keep the receipt for the guarantee."),
    "A1-U06-033": ("Έχω μόνο μετρητά μαζί μου σήμερα.", "I only have cash with me today."),
    "A1-U06-034": ("Δέχεστε πιστωτική κάρτα;", "Do you accept a credit card?"),
    "A1-U06-035": ("Τι αγοράζετε συνήθως από τον φούρνο;", "What do you usually buy from the bakery?"),
    "A1-U06-036": ("Αυτό το βιβλίο κοστίζει δέκα ευρώ.", "This book costs ten euros."),
    "A1-U06-037": ("Ποιος πληρώνει τον λογαριασμό σήμερα;", "Who pays the bill today?"),
    "A1-U06-038": ("Ψάχνω ένα δώρο για τα γενέθλια του φίλου μου.", "I am looking for a present for my friend's birthday."),
    "A1-U06-039": ("Πόσο κάνει αυτό το σακάκι;", "How much is this jacket?"),
    "A1-U06-040": ("Αυτό το εστιατόριο είναι πολύ ακριβό για μας.", "This restaurant is too expensive for us."),
    "A1-U06-041": ("Ψάχνω ένα φθηνό δωμάτιο κοντά στο κέντρο.", "I am looking for an inexpensive room near the center."),
    "A1-U06-042": ("Έχετε ρέστα από είκοσι ευρώ;", "Do you have change for twenty euros?")
}

ALL_BATCH_B = [
    ("unit-04", U04_EXAMPLES_2),
    ("unit-05", U05_EXAMPLES_2),
    ("unit-06", U06_EXAMPLES_2),
]

def process_batch_b():
    total_new_sentences = 0
    total_audio_synthesized = 0
    
    for uid, ex2_map in ALL_BATCH_B:
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

    print(f"\nBatch B Complete! Added {total_new_sentences} sentences, synthesized {total_audio_synthesized} audio files.")

if __name__ == "__main__":
    process_batch_b()

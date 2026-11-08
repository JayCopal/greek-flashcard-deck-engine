# -*- coding: utf-8 -*-
"""
KEG A1 Exam Syllabus Comprehensive Coverage Mapping Tool
Verifies alignment with official Examination Specifications of the Centre for the Greek Language.
"""
import sys
import yaml
from pathlib import Path
from collections import defaultdict

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
MANIFEST_PATH = BASE_DIR / "content" / "manifest.yaml"

with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
    manifest = yaml.safe_load(f)

# The 4 Exam Components & Core Competencies defined by the Greek Language Center (ΚΕΓ)
KEG_EXAM_SPECIFICATIONS = {
    "1. Exam Rubrics & Metalanguage (Γλώσσα Εξετάσεων & Οδηγίες)": {
        "unit": "unit-00",
        "description": "Understanding imperative prompts, question formats, and scoring terms",
        "key_lexis": [
            "διαβάζω", "γράφω", "ακούω", "κοιτάζω", "αντιστοιχίζω", "συμπληρώνω", "επιλέγω",
            "κυκλώνω", "υπογραμμίζω", "σημειώνω", "απαντώ", "διαγράφω", "το σωστό", "το λάθος",
            "Σωστό ή Λάθος (Σ/Λ)", "η πολλαπλή επιλογή", "συμπληρώστε τα κενά", "κυκλώστε το σωστό",
            "η εξέταση", "η οδηγία", "η ερώτηση", "η απάντηση", "το θέμα", "το κείμενο", "ο διάλογος",
            "η κατανόηση γραπτού λόγου", "η κατανόηση προφορικού λόγου", "η παραγωγή γραπτού λόγου",
            "η παραγωγή προφορικού λόγου", "ο βαθμός", "η βαθμολογία"
        ]
    },
    "2. Personal Identification & Social Formulas (Προσωπικά Στοιχεία & Χαιρετισμοί)": {
        "unit": "unit-01",
        "description": "Greetings, introducing self/others, polite formulas, personal pronouns, copula είμαι",
        "key_lexis": [
            "ο κύριος", "η κυρία", "η δεσποινίδα", "το όνομα", "το επώνυμο", "το γράμμα",
            "είμαι", "λέω", "γράφω", "εγώ", "εσύ", "αυτός", "αυτή", "αυτό", "εμείς", "εσείς",
            "πώς", "ποιος, ποια, ποιο", "τι", "γεια σου", "γεια σας", "καλημέρα", "καλησπέρα",
            "καληνύχτα", "αντίο", "ευχαριστώ", "παρακαλώ", "η συγγνώμη", "χάρηκα"
        ]
    },
    "3. Origin, Nationalities & Languages (Καταγωγή, Εθνικότητες & Γλώσσες)": {
        "unit": "unit-02",
        "description": "Countries, nationalities, spoken languages, prepositions από and σε + article",
        "key_lexis": [
            "η χώρα", "η πόλη", "η εθνικότητα", "η καταγωγή", "η γλώσσα", "η μητρική γλώσσα",
            "η Ελλάδα", "η Κύπρος", "ο Έλληνας", "η Ελληνίδα", "τα ελληνικά", "τα αγγλικά",
            "μένω", "μιλάω / μιλώ", "μαθαίνω", "καταλαβαίνω", "ξέρω", "από", "σε"
        ]
    },
    "4. Professions, Studies & Contact Forms (Επαγγέλματα, Σπουδές & Στοιχεία Επικοινωνίας)": {
        "unit": "unit-03",
        "description": "Occupations, workplaces, phone, address, numerals 0-100, official registration form filling",
        "key_lexis": [
            "το επάγγελμα", "ο δάσκαλος", "η δασκάλα", "ο καθηγητής", "η καθηγήτρια",
            "ο μαθητής", "η μαθήτρια", "ο φοιτητής", "η φοιτήτρια", "ο γιατρός", "η νοσοκόμα",
            "το γραφείο", "το σχολείο", "το πανεπιστήμιο", "το νοσοκομείο", "η διεύθυνση",
            "η οδός", "ο αριθμός", "το τηλέφωνο", "το κινητό", "το ταχυδρομείο", "ο ταχυδρομικός κώδικας",
            "δουλεύω", "σπουδάζω", "μηδέν", "ένας, μία / μια, ένα", "δέκα", "είκοσι", "εκατό"
        ]
    },
    "5. Family, Physical Appearance & Character (Οικογένεια, Πρόσωπα & Περιγραφή)": {
        "unit": "unit-04",
        "description": "Kinship, marital status, physical description, verb έχω, possessive enclitics",
        "key_lexis": [
            "η οικογένεια", "οι γονείς", "ο πατέρας", "η μητέρα", "ο γιος", "η κόρη", "ο αδελφός / ο αδερφός",
            "η αδελφή / η αδερφή", "ο παππούς", "η γιαγιά", "το παιδί", "ο άντρας", "η γυναίκα",
            "παντρεμένος, -η, -ο", "ελεύθερος, -η, -ο", "τα μαλλιά", "τα μάτια", "ψηλός, -ή, -ό",
            "κοντός, -ή, -ό", "αδύνατος, -η, -ο", "χοντρός, -ή, -ό", "όμορφος, -η, -ο", "νέος, -α, -ο",
            "μεγάλος, -η, -ο", "καλός, -ή, -ό", "έχω", "μου", "σου", "του / της / του"
        ]
    },
    "6. Food & Drink: Ordering & Paying (Στο Καφέ & Στην Ταβέρνα)": {
        "unit": "unit-05",
        "description": "Tavern/cafe menus, ordering, dietary preferences, the bill, verbs θέλω, πίνω, τρώω",
        "key_lexis": [
            "ο καφές", "το νερό", "το τσάι", "ο χυμός", "η μπύρα", "το κρασί", "το ψωμί",
            "η σαλάτα", "το τυρί", "η φέτα", "το κρέας", "το κοτόπουλο", "το ψάρι", "τα μακαρόνια",
            "το γλυκό", "ο κατάλογος / το μενού", "ο λογαριασμός", "θέλω", "πίνω", "τρώω", "παίρνω",
            "ορίστε", "για μένα", "τον λογαριασμό, παρακαλώ"
        ]
    },
    "7. Shopping, Supermarket & Prices (Στην Αγορά, Ψώνια & Τιμές)": {
        "unit": "unit-06",
        "description": "Grocery shopping, weights/measures, clothing, price inquiries, payment methods",
        "key_lexis": [
            "το σούπερ μάρκετ", "η λαϊκή αγορά", "το μαγαζί / το κατάστημα", "το ταμείο", "η απόδειξη",
            "τα ρέστα", "τα μετρητά", "η κάρτα", "το κιλό", "το γραμμάριο", "το λίτρο", "το ευρώ",
            "το λεπτό (χρήματα)", "πόσο κάνει;", "πόσο έχουν;", "ακριβός, -ή, -ό", "φθηνός, -ή, -ό",
            "το χρώμα", "το μέγεθος", "αγοράζω", "πληρώνω", "κοστίζει"
        ]
    },
    "8. Housing, Furniture & Classified Ads (Το Σπίτι, Έπιπλα & Διαμονή)": {
        "unit": "unit-07",
        "description": "Rooms, furniture, floor numbers, rental advertisements, spatial prepositions, υπάρχει/υπάρχουν",
        "key_lexis": [
            "το σπίτι", "το διαμέρισμα", "η πολυκατοικία", "το δωμάτιο", "το σαλόνι", "η κουζίνα",
            "το μπάνιο", "η κρεβατοκάμαρα", "το μπαλκόνι", "ο όροφος", "το ισόγειο", "το ασανσέρ",
            "το ενοίκιο", "το έπιπλο", "το κρεβάτι", "ο καναπές", "το τραπέζι", "η καρέκλα",
            "η ντουλάπα", "το ψυγείο", "υπάρχει / υπάρχουν", "ενοικιάζεται", "πωλείται", "επιπλωμένος, -η, -ο"
        ]
    },
    "9. Daily Routines, Habits & Frequency (Καθημερινό Πρόγραμμα & Συνήθειες)": {
        "unit": "unit-08",
        "description": "Daily actions, frequency adverbs, times of day, Type A/B1/B2 active verbs, active routine idioms",
        "key_lexis": [
            "το πρόγραμμα", "η συνήθεια", "το πρωί", "το μεσημέρι", "το απόγευμα", "το βράδυ",
            "η νύχτα", "νωρίς", "αργά", "πάντα", "συνήθως", "συχνά", "μερικές φορές", "σπάνια",
            "ποτέ", "ξυπνάω / ξυπνώ", "σηκώνομαι (παίρνω πρωινό)", "κάνω ντους / κάνω μπάνιο",
            "φεύγω", "γυρίζω", "διαβάζω", "μαγειρεύω", "πάω για ύπνο"
        ]
    },
    "10. Time, Calendar & Appointments (Ώρα, Ημερολόγιο & Ραντεβού)": {
        "unit": "unit-09",
        "description": "Telling time, fractions, days of week, months, seasons, arranging appointments, connectives",
        "key_lexis": [
            "η ώρα", "το λεπτό", "το τέταρτο", "και μισή", "παρά", "στις μία / στις δύο / στις τρεις",
            "το ραντεβού", "η εβδομάδα", "η Δευτέρα", "η Τρίτη", "η Τετάρτη", "η Πέμπτη", "η Παρασκευή",
            "το Σάββατο", "η Κυριακή", "το σαββατοκύριακο", "η εποχή", "η άνοιξη", "το καλοκαίρι",
            "το φθινόπωρο", "ο χειμώνας", "ο μήνας", "πριν από", "μετά από", "από... μέχρι...",
            "σήμερα", "αύριο", "χθες", "τώρα", "κλείνω ραντεβού", "περιμένω", "συναντάω / συναντώ"
        ]
    },
    "11. City Navigation, Transport & Directions (Στην Πόλη, Μετακινήσεις & Οδηγίες)": {
        "unit": "unit-10",
        "description": "Urban landmarks, public transit, ticket types, asking/giving directions, movement verbs",
        "key_lexis": [
            "ο δρόμος", "η οδός", "η πλατεία", "η γωνία", "το φανάρι", "το πεζοδρόμιο", "η διάβαση",
            "το κέντρο", "η τράπεζα", "το ταχυδρομείο", "το φαρμακείο", "το νοσοκομείο", "το μουσείο",
            "το ξενοδοχείο", "το περίπτερο", "το μετρό", "το λεωφορείο", "το τρένο", "το ταξί",
            "ο σταθμός", "η στάση", "το εισιτήριο", "το απλό εισιτήριο", "το εισιτήριο μετ' επιστροφής",
            "ευθεία", "δεξιά", "αριστερά", "κοντά σε", "μακριά από", "απέναντι από", "με τα πόδια",
            "στρίβω", "περνάω / περνώ", "κατεβαίνω", "ανεβαίνω", "ψάχνω"
        ]
    },
    "12. Leisure, Weather & Direct Clitics (Ελεύθερος Χρόνος, Καιρός & Διακοπές)": {
        "unit": "unit-11",
        "description": "Weather conditions, hobbies, sports, vacations, expressing likes, weak direct-object clitics",
        "key_lexis": [
            "ο καιρός", "ο ήλιος", "η βροχή", "το χιόνι", "ο αέρας / ο άνεμος", "η θερμοκρασία",
            "ο βαθμός", "κάνει ζέστη", "κάνει κρύο", "έχει ήλιο", "βρέχει", "χιονίζει", "φυσάει / φυσά",
            "ο ελεύθερος χρόνος", "οι διακοπές", "η παραλία", "η θάλασσα", "το βουνό", "το νησί",
            "το ταξίδι", "η βόλτα", "το ποδόσφαιρο", "το μπάσκετ", "το σινεμά", "το θέατρο", "η μουσική",
            "παίζω", "ταξιδεύω", "κολυμπάω / κολυμπώ", "χορεύω", "ακούω", "προτιμάω / προτιμώ",
            "μου αρέσει", "μου αρέσουν", "διασκεδάζω", "χαλαρώνω", "τον / την / το", "τους / τις / τα"
        ]
    },
    "13. Health, Pharmacy & Emergencies (Υγεία, Φαρμακείο & Έκτακτη Ανάγκη)": {
        "unit": "unit-12",
        "description": "Anatomy, symptoms, illness, pharmacy purchases, modal 'πρέπει να', emergency cries, wishes",
        "key_lexis": [
            "το σώμα", "το κεφάλι", "ο λαιμός", "το στομάχι", "η κοιλιά", "το μάτι", "το αυτί",
            "η μύτη", "το στόμα", "το δόντι", "το χέρι", "το πόδι", "η πλάτη", "η καρδιά",
            "ο πυρετός", "ο πονοκέφαλος", "ο πονόλαιμος", "ο πονόδοντος", "το συνάχι", "η γρίπη",
            "ο βήχας", "η αλλεργία", "άρρωστος, άρρωστη, άρρωστο", "κουρασμένος, κουρασμένη, κουρασμένο",
            "το φάρμακο", "το χάπι", "η ασπιρίνη", "το σιρόπι", "το τσιρότο", "η συνταγή",
            "ο φαρμακοποιός", "το ασθενοφόρο", "πονάω / πονώ", "πονάει... / πονάνε...", "πρέπει να",
            "νιώθω", "βοήθεια!", "χρειάζομαι γιατρό!", "περαστικά!", "η υγεία"
        ]
    }
}

# Load all cards from YAML into an indexed lookup
deck_by_unit = {}
all_greek_terms = defaultdict(list)

for u_spec in manifest.get("units", []):
    u_id = u_spec["id"]
    rel_path = u_spec["lessons"][0]["file"]
    yp = BASE_DIR / "content" / rel_path
    if yp.exists():
        with open(yp, "r", encoding="utf-8") as f:
            ydata = yaml.safe_load(f)
            deck_by_unit[u_id] = ydata.get("entries", [])
            for e in deck_by_unit[u_id]:
                all_greek_terms[e["greek"].lower()].append((u_id, e["id"]))

print("=" * 80)
print("EVALUATION: OFFICIAL KEG A1 SYLLABUS COVERAGE")
print("=" * 80)

total_target_lexis = 0
total_found_lexis = 0

for section_name, sec_data in KEG_EXAM_SPECIFICATIONS.items():
    u_id = sec_data["unit"]
    key_lexis = sec_data["key_lexis"]
    unit_cards = deck_by_unit.get(u_id, [])
    unit_greeks = {e["greek"].lower(): e for e in unit_cards}

    found = []
    missing = []
    for item in key_lexis:
        item_lower = item.lower()
        if item_lower in unit_greeks or item_lower in all_greek_terms:
            found.append(item)
        else:
            # Check partial match
            partial = any(item_lower in g or g in item_lower for g in unit_greeks)
            if partial:
                found.append(item)
            else:
                missing.append(item)

    total_target_lexis += len(key_lexis)
    total_found_lexis += len(found)
    pct = (len(found) / len(key_lexis)) * 100

    print(f"\n{section_name} [{u_id}]")
    print(f"  Target Items: {len(key_lexis)} | Covered: {len(found)} ({pct:5.1f}%)")
    if missing:
        print(f"  Missing or unmapped: {missing}")
    else:
        print("  Status: 100% Full Lexical & Functional Alignment!")

print("\n" + "=" * 80)
print(f"OVERALL KEG A1 SYLLABUS COVERAGE: {total_found_lexis}/{total_target_lexis} ({total_found_lexis/total_target_lexis*100:5.1f}%)")
print("=" * 80)

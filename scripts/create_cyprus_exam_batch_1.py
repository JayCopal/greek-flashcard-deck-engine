# -*- coding: utf-8 -*-
"""
Generate Cyprus Culture and Political/Social Reality Exam Curriculum — Batch 1 (Units 1-3):
- unit-cyp-01 (CYP-01-A): Πολίτευμα, Θεσμοί & Κράτος της Κύπρου (Polity, State Institutions & Governance) - 30 cards
- unit-cyp-02 (CYP-02-A): Σύγχρονη Ιστορία της Κύπρου (Modern History of Cyprus: 1955–Present) - 30 cards
- unit-cyp-03 (CYP-03-A): Γεωγραφία, Επαρχίες, Πόλεις & Φύση (Geography, Districts, Cities & Nature) - 30 cards
Hybrid format: Core terminology cards + Direct past-exam Q&A cards.
"""
import sys
import unicodedata
from pathlib import Path
import yaml

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"

# ==============================================================================
# UNIT CYP-01: Πολίτευμα, Θεσμοί & Κράτος της Κύπρου (30 Cards)
# ==============================================================================
NOTES_CYP_01 = """Unit CYP-01 Core Exam Notes: Πολίτευμα, Θεσμοί & Κράτος της Κύπρου (Polity, State Institutions & Governance)

• Το Πολίτευμα της Κυπριακής Δημοκρατίας (System of Government):
  - Η Κύπρος είναι ανεξάρτητη και κυρίαρχη Προεδρική Δημοκρατία (Presidential Republic) σύμφωνα με το Σύνταγμα του 1960.
  - Ο Πρόεδρος της Δημοκρατίας είναι ταυτόχρονα Αρχηγός του Κράτους (Head of State) και Αρχηγός της Κυβέρνησης (Head of Government).
  - Εκλέγεται άμεσα από τον λαό με καθολική ψηφοφορία για πενταετή θητεία (5-year term). Σημερινός Πρόεδρος (από το 2023): Νίκος Χριστοδουλίδης.

• Διάκριση των Εξουσιών (Separation of Powers):
  1. Εκτελεστική Εξουσία (Executive Power): Ασκείται από τον Πρόεδρο της Δημοκρατίας και το Υπουργικό Συμβούλιο (Council of Ministers).
  2. Νομοθετική Εξουσία (Legislative Power): Ασκείται από τη Βουλή των Αντιπροσώπων (House of Representatives).
     - Συνταγματική σύνθεση: 80 έδρες συνολικά (56 Ελληνοκύπριοι βουλευτές + 24 Τουρκοκύπριοι βουλευτές, οι οποίοι απέχουν από το 1964).
     - Επιπλέον 3 εκπρόσωποι των Θρησκευτικών Ομάδων (Μαρωνίτες, Αρμένιοι, Λατίνοι) με συμβουλευτικό χαρακτήρα.
     - Οι βουλευτικές εκλογές διεξάγονται κάθε 5 χρόνια. Πρόεδρος της Βουλής: Αννίτα Δημητρίου.
  3. Δικαστική Εξουσία (Judicial Power): Ανεξάρτητη εξουσία που ασκείται από το Ανώτατο Συνταγματικό Δικαστήριο, το Ανώτατο Δικαστήριο και τα Επαρχιακά Δικαστήρια.

• Ανεξάρτητοι Αξιωματούχοι & Εθνικά Σύμβολα:
  - Ανεξάρτητοι Θεσμοί: Γενικός Εισαγγελέας (Attorney General), Γενικός Ελεγκτής (Auditor General), Επίτροπος Διοικήσεως (Ombudsman).
  - Επίσημες Γλώσσες (Άρθρο 3 Συντάγματος): Ελληνική και Τουρκική.
  - Σημαία της Κύπρου: Σχεδιάστηκε το 1960 από τον Τουρκοκύπριο ζωγράφο Ισμέτ Γκιουνέι (λευκό φόντο, χαλκόχρωμος χάρτης του νησιού, δύο κλαδιά ελιάς).
  - Εθνικός Ύμνος: «Ύμνος εις την Ελευθερίαν» (στίχοι Διονυσίου Σολωμού, μουσική Νικολάου Μάντζαρου, υιοθετήθηκε το 1966)."""

CARDS_CYP_01 = [
    {
        "id": "CYP-U01-001",
        "greek": "η Κυπριακή Δημοκρατία",
        "phonetic_hint": "ee kee-pree-ah-KEE theem-oh-krah-TEE-ah",
        "english": "the Republic of Cyprus",
        "notes": "Official constitutional name of the state established on 16 August 1960.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι Κυπριακές Δημοκρατίες",
            "accusative_singular": "την Κυπριακή Δημοκρατία",
            "genitive_singular": "της Κυπριακής Δημοκρατίας"
        },
        "keg_communicative_function": "Polity & Institutions — Official state terminology",
        "example_el": "Η Κυπριακή Δημοκρατία ανακηρύχθηκε επίσημα ανεξάρτητο κράτος το 1960.",
        "example_en": "The Republic of Cyprus was officially proclaimed an independent state in 1960.",
        "example2_el": "Η Κυπριακή Δημοκρατία είναι πλήρες κράτος μέλος της Ευρωπαϊκής Ένωσης.",
        "example2_en": "The Republic of Cyprus is a full member state of the European Union."
    },
    {
        "id": "CYP-U01-002",
        "greek": "— Ποιο είναι το πολίτευμα της Κυπριακής Δημοκρατίας; — Προεδρική Δημοκρατία.",
        "phonetic_hint": "PEE-oh EE-neh toh poh-LEE-tev-mah tees kee-pree-ah-KEES theem-oh-krah-TEE-ahs? proh-eth-ree-KEE theem-oh-krah-TEE-ah",
        "english": "— What is the system of government of the Republic of Cyprus? — Presidential Republic.",
        "notes": "Frequent past exam question! Distractors often include 'Προεδρευόμενη Κοινοβουλευτική Δημοκρατία' (Greece's system) or 'Βασιλευόμενη Δημοκρατία'.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Constitutional regime of Cyprus",
        "example_el": "Στην Προεδρική Δημοκρατία ο Πρόεδρος είναι αρχηγός και του κράτους και της κυβέρνησης.",
        "example_en": "In a Presidential Republic, the President is head of both the state and the government.",
        "example2_el": "Το πολίτευμα της Κύπρου καθορίζεται από το Σύνταγμα του 1960.",
        "example2_en": "The system of government of Cyprus is defined by the Constitution of 1960."
    },
    {
        "id": "CYP-U01-003",
        "greek": "το Σύνταγμα",
        "phonetic_hint": "toh SEEN-dahg-mah",
        "english": "the Constitution",
        "notes": "Neuter noun in -μα (-ματα). The Constitution of Cyprus is the supreme law of the Republic (ο υπέρτατος νόμος).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Συντάγματα",
            "accusative_singular": "το Σύνταγμα",
            "genitive_singular": "του Συντάγματος"
        },
        "keg_communicative_function": "Polity & Institutions — Constitutional law",
        "example_el": "Το Σύνταγμα της Κυπριακής Δημοκρατίας τέθηκε σε ισχύ στις 16 Αυγούστου 1960.",
        "example_en": "The Constitution of the Republic of Cyprus entered into force on 16 August 1960.",
        "example2_el": "Το Σύνταγμα κατοχυρώνει τα θεμελιώδη δικαιώματα και τις ελευθερίες των πολιτών.",
        "example2_en": "The Constitution safeguards the fundamental rights and freedoms of citizens."
    },
    {
        "id": "CYP-U01-004",
        "greek": "— Ποιες είναι οι επίσημες γλώσσες της Κυπριακής Δημοκρατίας; — Η ελληνική και η τουρκική.",
        "phonetic_hint": "pyehs EE-neh ee eh-PEE-see-mehs GHLOH-sehs tees kee-pree-ah-KEES theem-oh-krah-TEE-ahs? ee eh-lee-nee-KEE keh ee toor-kee-KEE",
        "english": "— What are the official languages of the Republic of Cyprus? — Greek and Turkish.",
        "notes": "Classic past exam question! Under Article 3 of the Constitution, Greek and Turkish are the two official languages (English is widely spoken but NOT an official constitutional language).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Official languages under the Constitution",
        "example_el": "Σύμφωνα με το Άρθρο 3 του Συντάγματος, οι επίσημες γλώσσες είναι η ελληνική και η τουρκική.",
        "example_en": "According to Article 3 of the Constitution, the official languages are Greek and Turkish.",
        "example2_el": "Η αγγλική γλώσσα χρησιμοποιείται ευρέως αλλά δεν είναι επίσημη γλώσσα του κράτους.",
        "example2_en": "The English language is widely used but is not an official language of the state."
    },
    {
        "id": "CYP-U01-005",
        "greek": "η διάκριση των εξουσιών",
        "phonetic_hint": "ee thee-AH-kree-see ton ehk-soo-see-ON",
        "english": "the separation of powers",
        "notes": "Core constitutional principle dividing state authority into Executive (Εκτελεστική), Legislative (Νομοθετική), and Judicial (Δικαστική).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι διακρίσεις των εξουσιών",
            "accusative_singular": "τη διάκριση των εξουσιών"
        },
        "keg_communicative_function": "Polity & Institutions — Democratic principles",
        "example_el": "Η διάκριση των εξουσιών αποτελεί θεμελιώδη αρχή της δημοκρατίας στην Κύπρο.",
        "example_en": "The separation of powers is a fundamental principle of democracy in Cyprus.",
        "example2_el": "Οι τρεις εξουσίες είναι η εκτελεστική, η νομοθετική και η δικαστική.",
        "example2_en": "The three powers are the executive, the legislative, and the judicial."
    },
    {
        "id": "CYP-U01-006",
        "greek": "η εκτελεστική εξουσία",
        "phonetic_hint": "ee ehk-teh-leh-stee-KEE ehk-soo-SEE-ah",
        "english": "the executive power / branch",
        "notes": "Exercised by the President of the Republic and the Council of Ministers (το Υπουργικό Συμβούλιο).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι εκτελεστικές εξουσίες",
            "accusative_singular": "την εκτελεστική εξουσία"
        },
        "keg_communicative_function": "Polity & Institutions — Branches of government",
        "example_el": "Στην Κύπρο η εκτελεστική εξουσία ασκείται από τον Πρόεδρο της Δημοκρατίας και το Υπουργικό Συμβούλιο.",
        "example_en": "In Cyprus, executive power is exercised by the President of the Republic and the Council of Ministers.",
        "example2_el": "Τα μέλη της εκτελεστικής εξουσίας δεν μπορούν να είναι ταυτόχρονα και βουλευτές.",
        "example2_en": "Members of the executive branch cannot simultaneously be members of parliament."
    },
    {
        "id": "CYP-U01-007",
        "greek": "— Πόσα χρόνια διαρκεί η θητεία του Προέδρου της Κυπριακής Δημοκρατίας; — Πέντε χρόνια.",
        "phonetic_hint": "POH-sah KHROH-nyah theeahr-KEE ee thee-TEE-ah too proh-ETH-roo tees kee-pree-ah-KEES theem-oh-krah-TEE-ahs? PEHN-deh KHROH-nyah",
        "english": "— How many years does the term of the President of the Republic of Cyprus last? — Five years.",
        "notes": "Past exam question! Both Presidential elections and Parliamentary elections in Cyprus take place every 5 years.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Presidential term of office",
        "example_el": "Οι προεδρικές εκλογές στην Κύπρο διεξάγονται κάθε πέντε χρόνια με καθολική ψηφοφορία.",
        "example_en": "Presidential elections in Cyprus are held every five years by universal suffrage.",
        "example2_el": "Αν κανένας υποψήφιος δεν λάβει πάνω από 50%, διεξάγεται δεύτερος γύρος την επόμενη Κυριακή.",
        "example2_en": "If no candidate receives over 50%, a second round is held the following Sunday."
    },
    {
        "id": "CYP-U01-008",
        "greek": "— Ποιος είναι ο σημερινός Πρόεδρος της Κυπριακής Δημοκρατίας; — Ο Νίκος Χριστοδουλίδης.",
        "phonetic_hint": "pyos EE-neh oh see-meh-ree-NOHS PROH-eth-ros tees kee-pree-ah-KEES theem-oh-krah-TEE-ahs? oh NEE-kos khree-stoh-thoo-LEE-thees",
        "english": "— Who is the current President of the Republic of Cyprus? — Nikos Christodoulides.",
        "notes": "Elected in February 2023 as the 8th President of the Republic of Cyprus, succeeding Nicos Anastasiades.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Current Head of State",
        "example_el": "Ο Νίκος Χριστοδουλίδης εξελέγη Πρόεδρος της Κυπριακής Δημοκρατίας τον Φεβρουάριο του 2023.",
        "example_en": "Nikos Christodoulides was elected President of the Republic of Cyprus in February 2023.",
        "example2_el": "Πριν εκλεγεί Πρόεδρος, ο Νίκος Χριστοδουλίδης είχε διατελέσει Υπουργός Εξωτερικών.",
        "example2_en": "Before being elected President, Nikos Christodoulides had served as Minister of Foreign Affairs."
    },
    {
        "id": "CYP-U01-009",
        "greek": "το Υπουργικό Συμβούλιο",
        "phonetic_hint": "toh ee-poor-yee-KOH seem-VOO-lee-oh",
        "english": "the Council of Ministers / Cabinet",
        "notes": "Appointed by the President of the Republic. Cyprus has 11 Ministries (Υπουργεία) and 6 Deputy Ministries (Υφυπουργεία).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Υπουργικά Συμβούλια",
            "accusative_singular": "το Υπουργικό Συμβούλιο",
            "genitive_singular": "του Υπουργικού Συμβουλίου"
        },
        "keg_communicative_function": "Polity & Institutions — Executive Cabinet",
        "example_el": "Το Υπουργικό Συμβούλιο διορίζεται από τον Πρόεδρο της Δημοκρατίας και χαράσσει την κυβερνητική πολιτική.",
        "example_en": "The Council of Ministers is appointed by the President of the Republic and formulates government policy.",
        "example2_el": "Οι συνεδριάσεις του Υπουργικού Συμβουλίου πραγματοποιούνται στο Προεδρικό Μέγαρο στη Λευκωσία.",
        "example2_en": "The meetings of the Council of Ministers take place at the Presidential Palace in Nicosia."
    },
    {
        "id": "CYP-U01-010",
        "greek": "η νομοθετική εξουσία",
        "phonetic_hint": "ee noh-moh-theh-tee-KEE ehk-soo-SEE-ah",
        "english": "the legislative power / branch",
        "notes": "Exercised by the House of Representatives (η Βουλή των Αντιπροσώπων), which votes on laws and approves the state budget.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι νομοθετικές εξουσίες",
            "accusative_singular": "τη νομοθετική εξουσία"
        },
        "keg_communicative_function": "Polity & Institutions — Legislative branch",
        "example_el": "Ποιο όργανο ασκεί τη νομοθετική εξουσία στην Κύπρο; Η Βουλή των Αντιπροσώπων.",
        "example_en": "Which body exercises legislative power in Cyprus? The House of Representatives.",
        "example2_el": "Η νομοθετική εξουσία ψηφίζει τους νόμους και τον κρατικό προϋπολογισμό.",
        "example2_en": "The legislative branch votes on laws and the state budget."
    },
    {
        "id": "CYP-U01-011",
        "greek": "η Βουλή των Αντιπροσώπων",
        "phonetic_hint": "ee voo-LEE ton ahn-dee-proh-SOH-pon",
        "english": "the House of Representatives (Parliament of Cyprus)",
        "notes": "Unicameral parliament of Cyprus. Elected for a 5-year term by proportional representation.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι Βουλές των Αντιπροσώπων",
            "accusative_singular": "τη Βουλή των Αντιπροσώπων",
            "genitive_singular": "της Βουλής των Αντιπροσώπων"
        },
        "keg_communicative_function": "Polity & Institutions — Parliament of Cyprus",
        "example_el": "Η Βουλή των Αντιπροσώπων εδρεύει στην πρωτεύουσα Λευκωσία.",
        "example_en": "The House of Representatives is based in the capital Nicosia.",
        "example2_el": "Ο Πρόεδρος της Βουλής αναπληρώνει τον Πρόεδρο της Δημοκρατίας όταν απουσιάζει στο εξωτερικό.",
        "example2_en": "The President of the House deputizes for the President of the Republic when he is abroad."
    },
    {
        "id": "CYP-U01-012",
        "greek": "— Πόσοι Ελληνοκύπριοι βουλευτές εκλέγονται στη Βουλή των Αντιπροσώπων; — Πενήντα έξι (56) βουλευτές.",
        "phonetic_hint": "POH-see eh-lee-noh-KEE-pree-ee voo-lehf-TEHS ehk-LEH-ghon-deh stee voo-LEE ton ahn-dee-proh-SOH-pon? peh-NEEN-dah EHK-see voo-lehf-TEHS",
        "english": "— How many Greek Cypriot MPs are elected to the House of Representatives? — Fifty-six (56) MPs.",
        "notes": "High-frequency exam question! Total constitutional seats Since 1985: 80 (56 Greek Cypriot + 24 Turkish Cypriot seats, which remain vacant). Plus 3 observers from Religious Groups.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Composition of Parliament",
        "example_el": "Συνολικά οι βουλευτικές έδρες είναι 80: 56 για την ελληνοκυπριακή κοινότητα και 24 για την τουρκοκυπριακή.",
        "example_en": "In total there are 80 parliamentary seats: 56 for the Greek Cypriot community and 24 for the Turkish Cypriot community.",
        "example2_el": "Οι 24 έδρες των Τουρκοκυπρίων βουλευτών παραμένουν κενές από το 1964.",
        "example2_en": "The 24 seats of the Turkish Cypriot MPs have remained vacant since 1964."
    },
    {
        "id": "CYP-U01-013",
        "greek": "— Ποιες είναι οι τρεις αναγνωρισμένες θρησκευτικές ομάδες στη Βουλή; — Οι Μαρωνίτες, οι Αρμένιοι και οι Λατίνοι.",
        "phonetic_hint": "pyehs EE-neh ee trees ah-nah-ghnoh-ree-ZMEH-nehs three-skef-tee-KEHS oh-MAH-thehs stee voo-LEE? ee mah-roh-NEE-tehs, ee ahr-MEH-nee-ee keh ee lah-TEE-nee",
        "english": "— Which are the three recognized religious groups in Parliament? — The Maronites, the Armenians, and the Latins.",
        "notes": "Past exam question! Under the Constitution, the Maronites, Armenians, and Latins (Roman Catholics) are recognized religious groups that each elect 1 representative to the House.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Constitutional Religious Groups",
        "example_el": "Οι Μαρωνίτες, οι Αρμένιοι και οι Λατίνοι εκλέγουν από έναν εκπρόσωπο στη Βουλή των Αντιπροσώπων.",
        "example_en": "The Maronites, the Armenians, and the Latins each elect one representative to the House of Representatives.",
        "example2_el": "Μετά το δημοψήφισμα του 1960, οι τρεις θρησκευτικές ομάδες επέλεξαν να ανήκουν στην ελληνοκυπριακή κοινότητα.",
        "example2_en": "Following the 1960 referendum, the three religious groups chose to belong to the Greek Cypriot community."
    },
    {
        "id": "CYP-U01-014",
        "greek": "— Ποια είναι η Πρόεδρος της Βουλής των Αντιπροσώπων; — Η Αννίτα Δημητρίου.",
        "phonetic_hint": "pyah EE-neh ee PROH-eth-ros tees voo-LEES ton ahn-dee-proh-SOH-pon? ee ah-NEE-tah theem-ee-TREE-oo",
        "english": "— Who is the President (Speaker) of the House of Representatives? — Annita Demetriou.",
        "notes": "Elected in June 2021 as the first female Speaker of the House of Representatives in Cyprus, and also President of DISY since 2023.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Head of the Legislative Branch",
        "example_el": "Η Αννίτα Δημητρίου είναι η πρώτη γυναίκα που εξελέγη Πρόεδρος της Βουλής των Αντιπροσώπων.",
        "example_en": "Annita Demetriou is the first woman elected President of the House of Representatives.",
        "example2_el": "Ο Πρόεδρος της Βουλής είναι ο δεύτερος τη τάξει πολιτειακός αξιωματούχος της Κυπριακής Δημοκρατίας.",
        "example2_en": "The President of the House is the second highest state official of the Republic of Cyprus."
    },
    {
        "id": "CYP-U01-015",
        "greek": "η δικαστική εξουσία",
        "phonetic_hint": "ee thee-kah-stee-KEE ehk-soo-SEE-ah",
        "english": "the judicial power / judiciary",
        "notes": "Completely independent from the executive and legislative branches. Following the 2023 judicial reform, headed by the Supreme Constitutional Court and the Supreme Court.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι δικαστικές εξουσίες",
            "accusative_singular": "τη δικαστική εξουσία"
        },
        "keg_communicative_function": "Polity & Institutions — Judiciary",
        "example_el": "Η δικαστική εξουσία στην Κύπρο είναι ανεξάρτητη και απονέμει τη δικαιοσύνη.",
        "example_en": "The judicial power in Cyprus is independent and administers justice.",
        "example2_el": "Στην κορυφή της δικαστικής εξουσίας βρίσκονται το Ανώτατο Συνταγματικό Δικαστήριο και το Ανώτατο Δικαστήριο.",
        "example2_en": "At the top of the judiciary are the Supreme Constitutional Court and the Supreme Court."
    },
    {
        "id": "CYP-U01-016",
        "greek": "το Ανώτατο Δικαστήριο",
        "phonetic_hint": "toh ah-NOH-tah-toh thee-kah-STEE-ree-oh",
        "english": "the Supreme Court",
        "notes": "Highest appellate court of the Republic, alongside the Supreme Constitutional Court (το Ανώτατο Συνταγματικό Δικαστήριο) and the Court of Appeal (το Εφετείο).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Ανώτατα Δικαστήρια",
            "accusative_singular": "το Ανώτατο Δικαστήριο",
            "genitive_singular": "του Ανωτάτου Δικαστηρίου"
        },
        "keg_communicative_function": "Polity & Institutions — Courts of Cyprus",
        "example_el": "Οι δικαστές του Ανωτάτου Δικαστηρίου διορίζονται από τον Πρόεδρο της Δημοκρατίας.",
        "example_en": "The judges of the Supreme Court are appointed by the President of the Republic.",
        "example2_el": "Κάθε επαρχία της Κύπρου διαθέτει το δικό της Επαρχιακό Δικαστήριο.",
        "example2_en": "Each district of Cyprus has its own District Court."
    },
    {
        "id": "CYP-U01-017",
        "greek": "ο Γενικός Εισαγγελέας",
        "phonetic_hint": "oh yeh-nee-KOHS ee-sahng-gheh-LEH-ahs",
        "english": "the Attorney General",
        "notes": "Independent officer of the Republic (head of the Law Office — η Νομική Υπηρεσία) serving as legal adviser to the state and director of public prosecutions.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι Γενικοί Εισαγγελείς",
            "accusative_singular": "τον Γενικό Εισαγγελέα",
            "genitive_singular": "του Γενικού Εισαγγελέα"
        },
        "keg_communicative_function": "Polity & Institutions — Independent state officials",
        "example_el": "Ο Γενικός Εισαγγελέας είναι ο νομικός σύμβουλος της Κυπριακής Δημοκρατίας και προΐσταται της Νομικής Υπηρεσίας.",
        "example_en": "The Attorney General is the legal adviser of the Republic of Cyprus and heads the Law Office.",
        "example2_el": "Ο Γενικός Εισαγγελέας της Δημοκρατίας είναι ο Γιώργος Σαββίδης.",
        "example2_en": "The Attorney General of the Republic is George Savvides."
    },
    {
        "id": "CYP-U01-018",
        "greek": "ο Γενικός Ελεγκτής",
        "phonetic_hint": "oh yeh-nee-KOHS eh-lehng-KTEES",
        "english": "the Auditor General",
        "notes": "Head of the Audit Office of the Republic (η Ελεγκτική Υπηρεσία), constitutionally responsible for auditing all public revenues and expenditures.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι Γενικοί Ελεγκτές",
            "accusative_singular": "τον Γενικό Ελεγκτή",
            "genitive_singular": "του Γενικού Ελεγκτή"
        },
        "keg_communicative_function": "Polity & Institutions — Financial oversight",
        "example_el": "Ο Γενικός Ελεγκτής ελέγχει τις δαπάνες και τα έσοδα του κράτους.",
        "example_en": "The Auditor General audits the expenditures and revenues of the state.",
        "example2_el": "Η Ελεγκτική Υπηρεσία είναι ανεξάρτητος θεσμός της Κυπριακής Δημοκρατίας.",
        "example2_en": "The Audit Office is an independent institution of the Republic of Cyprus."
    },
    {
        "id": "CYP-U01-019",
        "greek": "ο Επίτροπος Διοικήσεως",
        "phonetic_hint": "oh eh-PEE-troh-pos thee-ee-KEE-seh-os",
        "english": "the Commissioner for Administration (Ombudsman)",
        "notes": "Full title: Επίτροπος Διοικήσεως και Προστασίας Ανθρώπινων Δικαιωμάτων. Investigates citizen complaints against public administration.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι Επίτροποι Διοικήσεως",
            "accusative_singular": "τον Επίτροπο Διοικήσεως"
        },
        "keg_communicative_function": "Polity & Institutions — Citizen rights & Ombudsman",
        "example_el": "Οι πολίτες μπορούν να υποβάλουν παράπονο στον Επίτροπο Διοικήσεως για πράξεις της δημόσιας υπηρεσίας.",
        "example_en": "Citizens can submit a complaint to the Ombudsman regarding actions of the public service.",
        "example2_el": "Η Επίτροπος Διοικήσεως και Προστασίας Ανθρώπινων Δικαιωμάτων είναι η Μαρία Στυλιανού-Λοττίδη.",
        "example2_en": "The Commissioner for Administration and the Protection of Human Rights is Maria Stylianou-Lottides."
    },
    {
        "id": "CYP-U01-020",
        "greek": "η σημαία της Κύπρου",
        "phonetic_hint": "ee see-MEH-ah tees KEE-proo",
        "english": "the flag of Cyprus",
        "notes": "Features a white background, the copper-orange silhouette of the island (symbolizing copper deposits), and two crossed olive branches (symbolizing peace between the two communities).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι σημαίες της Κύπρου",
            "accusative_singular": "τη σημαία της Κύπρου"
        },
        "keg_communicative_function": "Polity & Institutions — National symbols",
        "example_el": "Τι απεικονίζει η σημαία της Κύπρου; Τον χάρτη του νησιού σε χρώμα χαλκού και δύο κλαδιά ελιάς σε λευκό φόντο.",
        "example_en": "What does the flag of Cyprus depict? The map of the island in copper color and two olive branches on a white background.",
        "example2_el": "Τα δύο κλαδιά ελιάς στη σημαία συμβολίζουν την ειρήνη μεταξύ Ελληνοκυπρίων και Τουρκοκυπρίων.",
        "example2_en": "The two olive branches on the flag symbolize peace between Greek Cypriots and Turkish Cypriots."
    },
    {
        "id": "CYP-U01-021",
        "greek": "— Ποιος σχεδίασε τη σημαία της Κυπριακής Δημοκρατίας; — Ο Τουρκοκύπριος ζωγράφος Ισμέτ Γκιουνέι.",
        "phonetic_hint": "pyos skheh-THEE-ah-seh tee see-MEH-ah tees kee-pree-ah-KEES theem-oh-krah-TEE-ahs? oh toor-koh-KEE-pree-os zoh-GHRAH-fos ee-SMEHT gyoo-NEH-ee",
        "english": "— Who designed the flag of the Republic of Cyprus? — The Turkish Cypriot painter Ismet Guney.",
        "notes": "Classic past exam question! Chosen in 1960 by President Makarios III and Vice-President Fazıl Küçük; blue and red colors were intentionally avoided.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Designer of the Cyprus flag",
        "example_el": "Η σημαία της Κύπρου σχεδιάστηκε το 1960 από τον Τουρκοκύπριο καλλιτέχνη Ισμέτ Γκιουνέι.",
        "example_en": "The flag of Cyprus was designed in 1960 by the Turkish Cypriot artist Ismet Guney.",
        "example2_el": "Η Κύπρος και το Κόσοβο είναι οι μόνες χώρες που απεικονίζουν τον χάρτη τους στη σημαία τους.",
        "example2_en": "Cyprus and Kosovo are the only countries that depict their map on their flag."
    },
    {
        "id": "CYP-U01-022",
        "greek": "— Ποιος είναι ο Εθνικός Ύμνος της Κύπρου; — Ο «Ύμνος εις την Ελευθερίαν» του Διονυσίου Σολωμού.",
        "phonetic_hint": "pyos EE-neh oh eth-nee-KOHS EEM-nos tees KEE-proo? oh EEM-nos ees teen eh-lef-theh-REE-ahn too thee-oh-nee-SEE-oo soh-loh-MOO",
        "english": "— What is the National Anthem of Cyprus? — The 'Hymn to Liberty' by Dionysios Solomos.",
        "notes": "Past exam question! Lyrics by Dionysios Solomos (1823), music composed by Nikolaos Mantzaros; officially adopted by the Republic of Cyprus in November 1966.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — National Anthem of Cyprus",
        "example_el": "Ο Εθνικός Ύμνος της Κύπρου είναι κοινός με της Ελλάδας, σε στίχους Διονυσίου Σολωμού και μουσική Νικολάου Μάντζαρου.",
        "example_en": "The National Anthem of Cyprus is shared with Greece, with lyrics by Dionysios Solomos and music by Nikolaos Mantzaros.",
        "example2_el": "Το Υπουργικό Συμβούλιο καθιέρωσε επίσημα τον Εθνικό Ύμνο στην Κύπρο το 1966.",
        "example2_en": "The Council of Ministers officially established the National Anthem in Cyprus in 1966."
    },
    {
        "id": "CYP-U01-023",
        "greek": "ο Δημοκρατικός Συναγερμός (ΔΗΣΥ)",
        "phonetic_hint": "oh theem-oh-krah-tee-KOHS see-nah-yer-MOHS (THEE-SEE)",
        "english": "the Democratic Rally (DISY)",
        "notes": "Major center-right political party in Cyprus, founded in 1976 by Glafcos Clerides (Γλαύκος Κληρίδης). Affiliated with the European People's Party (ΕΛΚ).",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι Δημοκρατικοί Συναγερμοί",
            "accusative_singular": "τον Δημοκρατικό Συναγερμό"
        },
        "keg_communicative_function": "Polity & Institutions — Major political parties",
        "example_el": "Ο Δημοκρατικός Συναγερμός (ΔΗΣΥ) ιδρύθηκε το 1976 από τον πρώην Πρόεδρο Γλαύκο Κληρίδη.",
        "example_en": "The Democratic Rally (DISY) was founded in 1976 by former President Glafcos Clerides.",
        "example2_el": "Πρόεδρος του Δημοκρατικού Συναγερμού είναι η Αννίτα Δημητρίου.",
        "example2_en": "The President of the Democratic Rally is Annita Demetriou."
    },
    {
        "id": "CYP-U01-024",
        "greek": "το Ανορθωτικό Κόμμα Εργαζόμενου Λαού (ΑΚΕΛ)",
        "phonetic_hint": "toh ah-nor-thoh-tee-KOH KOH-mah ehr-ghah-ZOH-meh-noo lah-OO (ah-KEHL)",
        "english": "the Progressive Party of Working People (AKEL)",
        "notes": "Major left-wing political party in Cyprus, founded in 1941 (succeeding the Communist Party of Cyprus of 1926). General Secretary: Stefanos Stefanou (Στέφανος Στεφάνου).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Ανορθωτικά Κόμματα",
            "accusative_singular": "το Ανορθωτικό Κόμμα Εργαζόμενου Λαού"
        },
        "keg_communicative_function": "Polity & Institutions — Major political parties",
        "example_el": "Το ΑΚΕΛ είναι το μεγαλύτερο κόμμα της Αριστεράς στην Κύπρο και ιδρύθηκε το 1941.",
        "example_en": "AKEL is the largest party of the Left in Cyprus and was founded in 1941.",
        "example2_el": "Γενικός Γραμματέας της Κεντρικής Επιτροπής του ΑΚΕΛ είναι ο Στέφανος Στεφάνου.",
        "example2_en": "The General Secretary of the Central Committee of AKEL is Stefanos Stefanou."
    },
    {
        "id": "CYP-U01-025",
        "greek": "το Δημοκρατικό Κόμμα (ΔΗΚΟ)",
        "phonetic_hint": "toh theem-oh-krah-tee-KOH KOH-mah (THEE-KOH)",
        "english": "the Democratic Party (DIKO)",
        "notes": "Centrist political party in Cyprus, founded in 1976 by Spyros Kyprianou (Σπύρος Κυπριανού). Current President: Nikolas Papadopoulos (Νικόλας Παπαδόπουλος).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Δημοκρατικά Κόμματα",
            "accusative_singular": "το Δημοκρατικό Κόμμα"
        },
        "keg_communicative_function": "Polity & Institutions — Major political parties",
        "example_el": "Το Δημοκρατικό Κόμμα (ΔΗΚΟ) ιδρύθηκε το 1976 από τον Σπύρο Κυπριανού και ανήκει στον χώρο του Κέντρου.",
        "example_en": "The Democratic Party (DIKO) was founded in 1976 by Spyros Kyprianou and belongs to the political Center.",
        "example2_el": "Πρόεδρος του Δημοκρατικού Κόμματος είναι ο Νικόλας Παπαδόπουλος.",
        "example2_en": "The President of the Democratic Party is Nikolas Papadopoulos."
    },
    {
        "id": "CYP-U01-026",
        "greek": "η ΕΔΕΚ (Κίνημα Σοσιαλδημοκρατών)",
        "phonetic_hint": "ee eh-THEHK (KEE-nee-mah soh-syahl-theem-oh-krah-TON)",
        "english": "EDEK (Movement for Social Democracy)",
        "notes": "Social-democratic party founded in 1969 by Vassos Lyssarides (Βάσος Λυσσαρίδης).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "τα Κινήματα Σοσιαλδημοκρατών",
            "accusative_singular": "την ΕΔΕΚ"
        },
        "keg_communicative_function": "Polity & Institutions — Political parties",
        "example_el": "Η ΕΔΕΚ ιδρύθηκε το 1969 από τον γιατρό και πολιτικό Βάσο Λυσσαρίδη.",
        "example_en": "EDEK was founded in 1969 by the physician and politician Vassos Lyssarides.",
        "example2_el": "Η ΕΔΕΚ εκπροσωπεί τον χώρο της σοσιαλδημοκρατίας στην Κυπριακή Βουλή.",
        "example2_en": "EDEK represents the space of social democracy in the Cypriot Parliament."
    },
    {
        "id": "CYP-U01-027",
        "greek": "η καθολική ψηφοφορία",
        "phonetic_hint": "ee kah-thoh-lee-KEE psee-foh-foh-REE-ah",
        "english": "universal suffrage / voting",
        "notes": "In Cyprus, the right to vote (το δικαίωμα του εκλέγειν) is granted to citizens aged 18 and over.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι καθολικές ψηφοφορίες",
            "accusative_singular": "την καθολική ψηφοφορία"
        },
        "keg_communicative_function": "Polity & Institutions — Electoral rights",
        "example_el": "Το δικαίωμα ψήφου στην Κύπρο αποκτάται με τη συμπλήρωση του δέκατου όγδοου (18ου) έτους της ηλικίας.",
        "example_en": "The right to vote in Cyprus is acquired upon reaching eighteen (18) years of age.",
        "example2_el": "Η ψηφοφορία στις εκλογές είναι άμεση, καθολική και μυστική.",
        "example2_en": "Voting in elections is direct, universal, and secret."
    },
    {
        "id": "CYP-U01-028",
        "greek": "το Προεδρικό Μέγαρο",
        "phonetic_hint": "toh proh-eth-ree-KOH MEH-ghah-roh",
        "english": "the Presidential Palace",
        "notes": "Official residence and office of the President of the Republic of Cyprus in Nicosia (rebuilt after burning during the July 1974 coup).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Προεδρικά Μέγαρα",
            "accusative_singular": "το Προεδρικό Μέγαρο",
            "genitive_singular": "του Προεδρικού Μεγάρου"
        },
        "keg_communicative_function": "Polity & Institutions — State buildings",
        "example_el": "Το Προεδρικό Μέγαρο βρίσκεται στη Λευκωσία και αποτελεί την επίσημη έδρα του Προέδρου της Δημοκρατίας.",
        "example_en": "The Presidential Palace is located in Nicosia and is the official seat of the President of the Republic.",
        "example2_el": "Το κτίριο καταστράφηκε κατά το πραξικόπημα του 1974 και ανοικοδομήθηκε στη συνέχεια.",
        "example2_en": "The building was destroyed during the 1974 coup and was subsequently rebuilt."
    },
    {
        "id": "CYP-U01-029",
        "greek": "— Ποιος αναπληρώνει τον Πρόεδρο της Δημοκρατίας όταν απουσιάζει ή κωλύεται; — Ο Πρόεδρος της Βουλής των Αντιπροσώπων.",
        "phonetic_hint": "pyos ah-nah-plee-ROH-nee ton PROH-eth-roh tees theem-oh-krah-TEE-ahs OH-tahn ah-poo-see-AH-zee? oh PROH-eth-ros tees voo-LEES ton ahn-dee-proh-SOH-pon",
        "english": "— Who deputizes for the President of the Republic when absent or incapacitated? — The President of the House of Representatives.",
        "notes": "Past exam question! Because there is no Vice-President currently participating in government, the Speaker of the House serves as Acting President (Προεδρεύων της Δημοκρατίας).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Constitutional succession",
        "example_el": "Όταν ο Πρόεδρος της Δημοκρατίας ταξιδεύει στο εξωτερικό, καθήκοντα Προεδρεύοντα ασκεί ο Πρόεδρος της Βουλής.",
        "example_en": "When the President of the Republic travels abroad, the President of the House serves as Acting President.",
        "example2_el": "Η θέση του Αντιπροέδρου της Δημοκρατίας, που προοριζόταν για Τουρκοκύπριο, παραμένει κενή από το 1963.",
        "example2_en": "The post of Vice-President of the Republic, reserved for a Turkish Cypriot, has remained vacant since 1963."
    },
    {
        "id": "CYP-U01-030",
        "greek": "η Κεντρική Τράπεζα της Κύπρου",
        "phonetic_hint": "ee kehn-dree-KEE TRAH-peh-zah tees KEE-proo",
        "english": "the Central Bank of Cyprus",
        "notes": "Established in 1963; member of the Eurosystem since 2008. Current Governor (Διοικητής): Christodoulos Patsalides (Χριστόδουλος Πατσαλίδης, appointed 2024).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι Κεντρικές Τράπεζες",
            "accusative_singular": "την Κεντρική Τράπεζα της Κύπρου"
        },
        "keg_communicative_function": "Polity & Institutions — Monetary authority",
        "example_el": "Η Κεντρική Τράπεζα της Κύπρου ιδρύθηκε το 1963 και αποτελεί μέλος του Ευρωσυστήματος από το 2008.",
        "example_en": "The Central Bank of Cyprus was founded in 1963 and has been a member of the Eurosystem since 2008.",
        "example2_el": "Διοικητής της Κεντρικής Τράπεζας της Κύπρου είναι ο Χριστόδουλος Πατσαλίδης.",
        "example2_en": "The Governor of the Central Bank of Cyprus is Christodoulos Patsalides."
    }
]

# ==============================================================================
# UNIT CYP-02: Σύγχρονη Ιστορία της Κύπρου (1955–Σήμερα) (30 Cards)
# ==============================================================================
NOTES_CYP_02 = """Unit CYP-02 Core Exam Notes: Σύγχρονη Ιστορία της Κύπρου (Modern History of Cyprus: 1955–Present)

• Αγώνας της ΕΟΚΑ & Ίδρυση της Κυπριακής Δημοκρατίας (1955–1960):
  - 1878–1960: Περίοδος Αγγλοκρατίας (Βρετανική αποικιοκρατία).
  - 1 Απριλίου 1955 – 1959: Απελευθερωτικός Αγώνας της ΕΟΚΑ (Εθνική Οργάνωση Κυπρίων Αγωνιστών) κατά της βρετανικής αποικιοκρατίας, με στρατιωτικό αρχηγό τον Γεώργιο Γρίβα (Διγενή) και πολιτικό ηγέτη τον Αρχιεπίσκοπο Μακάριο Γ΄.
  - Φεβρουάριος 1959: Υπογραφή των Συμφωνιών Ζυρίχης-Λονδίνου. Τρεις Εγγυήτριες Δυνάμεις: Ελλάδα, Τουρκία, Ηνωμένο Βασίλειο.
  - 16 Αυγούστου 1960: Επίσημη ανακήρυξη της ανεξαρτησίας της Κυπριακής Δημοκρατίας. (Εορτάζεται την 1η Οκτωβρίου).

• Οι Πρόεδροι της Κυπριακής Δημοκρατίας (Chronological List — High Exam Frequency!):
  1. Αρχιεπίσκοπος Μακάριος Γ΄ (1960–1977) — Πρώτος Πρόεδρος
  2. Σπύρος Κυπριανού (1977–1988)
  3. Γιώργος Βασιλείου (1988–1993)
  4. Γλαύκος Κληρίδης (1993–2003)
  5. Τάσσος Παπαδόπουλος (2003–2008) — Επί προεδρίας του έγινε το δημοψήφισμα για το Σχέδιο Ανάν & η ένταξη στην ΕΕ (2004)
  6. Δημήτρης Χριστόφιας (2008–2013)
  7. Νίκος Αναστασιάδης (2013–2023)
  8. Νίκος Χριστοδουλίδης (2023–σήμερα)

• Γεγονότα 1963–1974 & Το Κυπριακό Πρόβλημα:
  - 1963–1964: Διακοινοτικές ταραχές, χάραξη της Πράσινης Γραμμής στη Λευκωσία και άφιξη της Ειρηνευτικής Δύναμης του ΟΗΕ (ΟΥΝΦΙΚΥΠ / UNFICYP) το 1964.
  - 15 Ιουλίου 1974: Στρατιωτικό πραξικόπημα της ελληνικής χούντας και της ΕΟΚΑ Β΄ κατά του Προέδρου Μακαρίου.
  - 20 Ιουλίου 1974: Τουρκική στρατιωτική εισβολή («Αττίλας Ι» τον Ιούλιο και «Αττίλας ΙΙ» στις 14 Αυγούστου 1974).
  - Συνέπειες: Κατοχή περίπου του 36,2%–37% του εδάφους της Κυπριακής Δημοκρατίας, ~200.000 πρόσφυγες, αγνοούμενοι, εγκλωβισμένοι στην Καρπασία.
  - 15 Νοεμβρίου 1983: Παράνομη ανακήρυξη του «ψευδοκράτους» στα κατεχόμενα, η οποία καταδικάστηκε από το Ψήφισμα 541 του Συμβουλίου Ασφαλείας του ΟΗΕ (αναγνωρίζεται μόνο από την Τουρκία).
  - 24 Απριλίου 2004: Δημοψήφισμα για το Σχέδιο Ανάν (απορρίφθηκε από το 76% των Ελληνοκυπρίων, εγκρίθηκε από το 65% των Τουρκοκυπρίων).
  - 1 Μαΐου 2004: Επίσημη ένταξη της Κυπριακής Δημοκρατίας στην Ευρωπαϊκή Ένωση."""

CARDS_CYP_02 = [
    {
        "id": "CYP-U02-001",
        "greek": "— Πότε ανακηρύχθηκε επίσημα η Κυπριακή Δημοκρατία ως ανεξάρτητο κράτος; — Στις 16 Αυγούστου 1960.",
        "phonetic_hint": "POH-teh ah-nah-kee-REEK-thee-keh eh-PEE-see-mah ee kee-pree-ah-KEE theem-oh-krah-TEE-ah? stees theh-kah-EHK-see ahv-GHOO-stoo 1960",
        "english": "— When was the Republic of Cyprus officially proclaimed an independent state? — On 16 August 1960.",
        "notes": "Crucial exam distinction: Independence was actually proclaimed on 16 August 1960, whereas Independence Day is celebrated on 1 October (to avoid the summer heat and holidays).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Date of proclamation of Independence",
        "example_el": "Η Κυπριακή Δημοκρατία ιδρύθηκε στις 16 Αυγούστου 1960 μετά το τέλος της βρετανικής αποικιοκρατίας.",
        "example_en": "The Republic of Cyprus was founded on 16 August 1960 after the end of British colonial rule.",
        "example2_el": "Αν και η ανεξαρτησία ανακηρύχθηκε στις 16 Αυγούστου, η επίσημη εθνική επέτειος γιορτάζεται την 1η Οκτωβρίου.",
        "example2_en": "Although independence was proclaimed on 16 August, the official national anniversary is celebrated on 1 October."
    },
    {
        "id": "CYP-U02-002",
        "greek": "— Πότε γιορτάζεται η Ημέρα Ανεξαρτησίας της Κυπριακής Δημοκρατίας; — Την 1η Οκτωβρίου.",
        "phonetic_hint": "POH-teh yor-TAH-zeh-teh ee ee-MEH-rah ah-nehk-sahr-tee-SEE-ahs tees kee-pree-ah-KEES theem-oh-krah-TEE-ahs? teen PROH-tee ohk-toh-VREE-oo",
        "english": "— When is the Independence Day of the Republic of Cyprus celebrated? — On 1 October.",
        "notes": "Past exam question! Decided by the Council of Ministers in 1963 so that schools, diplomatic missions, and the public could participate after summer.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Celebration of Cyprus Independence Day",
        "example_el": "Την 1η Οκτωβρίου είναι επίσημη αργία και πραγματοποιείται μεγάλη στρατιωτική παρέλαση στη Λευκωσία.",
        "example_en": "October 1st is a public holiday and a grand military parade takes place in Nicosia.",
        "example2_el": "Η Ημέρα Ανεξαρτησίας της Κύπρου μεταφέρθηκε από τον Αύγουστο στην 1η Οκτωβρίου λόγω των υψηλών θερμοκρασιών του καλοκαιριού.",
        "example2_en": "Cyprus Independence Day was moved from August to 1 October due to the high summer temperatures."
    },
    {
        "id": "CYP-U02-003",
        "greek": "ο απελευθερωτικός αγώνας της ΕΟΚΑ",
        "phonetic_hint": "oh ah-peh-lef-theh-roh-tee-KOHS ah-GHOH-nahs tees eh-OH-kah",
        "english": "the EOKA liberation struggle (1955–1959)",
        "notes": "EOKA = Εθνική Οργάνωση Κυπρίων Αγωνιστών (National Organisation of Cypriot Fighters). Began on 1 April 1955 against British colonial rule.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι απελευθερωτικοί αγώνες",
            "accusative_singular": "τον απελευθερωτικό αγώνα της ΕΟΚΑ"
        },
        "keg_communicative_function": "Modern History — Anti-colonial struggle 1955–1959",
        "example_el": "Ο απελευθερωτικός αγώνας της ΕΟΚΑ ξεκίνησε την 1η Απριλίου 1955 και έληξε το 1959.",
        "example_en": "The EOKA liberation struggle began on 1 April 1955 and ended in 1959.",
        "example2_el": "Η 1η Απριλίου είναι επίσημη εθνική επέτειος και αργία στην Κύπρο.",
        "example2_en": "April 1st is an official national anniversary and public holiday in Cyprus."
    },
    {
        "id": "CYP-U02-004",
        "greek": "οι Συμφωνίες Ζυρίχης-Λονδίνου",
        "phonetic_hint": "ee seem-foh-NEE-ehs zee-REE-khees lohn-THEE-noo",
        "english": "the Zurich and London Agreements (1959)",
        "notes": "Signed in February 1959 by Britain, Greece, Turkey, and representatives of the Greek Cypriot (Makarios III) and Turkish Cypriot (Fazıl Küçük) communities, establishing the Republic of Cyprus.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι Συμφωνίες Ζυρίχης-Λονδίνου",
            "accusative_plural": "τις Συμφωνίες Ζυρίχης-Λονδίνου"
        },
        "keg_communicative_function": "Modern History — Founding treaties of 1959",
        "example_el": "Οι Συμφωνίες Ζυρίχης-Λονδίνου υπογράφηκαν τον Φεβρουάριο του 1959 και οδήγησαν στην ανεξαρτησία της Κύπρου.",
        "example_en": "The Zurich and London Agreements were signed in February 1959 and led to the independence of Cyprus.",
        "example2_el": "Με τις συμφωνίες αυτές το Ηνωμένο Βασίλειο διατήρησε δύο κυρίαρχες στρατιωτικές βάσεις στο Ακρωτήρι και στη Δεκέλεια.",
        "example2_en": "Under these agreements, the United Kingdom retained two Sovereign Base Areas at Akrotiri and Dhekelia."
    },
    {
        "id": "CYP-U02-005",
        "greek": "— Ποιος ήταν ο πρώτος Πρόεδρος της Κυπριακής Δημοκρατίας; — Ο Αρχιεπίσκοπος Μακάριος Γ΄.",
        "phonetic_hint": "pyos EE-tahn oh PROH-tos PROH-eth-ros tees kee-pree-ah-KEES theem-oh-krah-TEE-ahs? oh ahr-khee-eh-PEE-skoh-pos mah-KAH-ree-os oh TREE-tos",
        "english": "— Who was the first President of the Republic of Cyprus? — Archbishop Makarios III.",
        "notes": "Past exam question! Archbishop Makarios III (Μιχαήλ Χριστοδούλου Μούσκος) served as the first President from 1960 until his death on 3 August 1977.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — First President of Cyprus",
        "example_el": "Ο Αρχιεπίσκοπος Μακάριος Γ΄ υπήρξε ο πρώτος Πρόεδρος της Κυπριακής Δημοκρατίας από το 1960 έως το 1977.",
        "example_en": "Archbishop Makarios III was the first President of the Republic of Cyprus from 1960 to 1977.",
        "example2_el": "Πρώτος Αντιπρόεδρος της Κυπριακής Δημοκρατίας το 1960 εξελέγη ο Τουρκοκύπριος Φαζίλ Κουτσιούκ.",
        "example2_en": "The Turkish Cypriot Fazil Kucuk was elected first Vice-President of the Republic of Cyprus in 1960."
    },
    {
        "id": "CYP-U02-006",
        "greek": "οι εγγυήτριες δυνάμεις",
        "phonetic_hint": "ee ehng-ghee-EE-tree-ehs thee-NAH-mees",
        "english": "the Guarantor Powers (Greece, Turkey, United Kingdom)",
        "notes": "Under the 1960 Treaty of Guarantee (Συνθήκη Εγγυήσεως), Greece, Turkey, and the UK became guarantors of the independence, territorial integrity, and Constitution of Cyprus.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι εγγυήτριες δυνάμεις",
            "accusative_plural": "τις εγγυήτριες δυνάμεις"
        },
        "keg_communicative_function": "Modern History — 1960 Treaty of Guarantee",
        "example_el": "Ποιες ήταν οι τρεις εγγυήτριες δυνάμεις της Κυπριακής Δημοκρατίας το 1960; Η Ελλάδα, η Τουρκία και το Ηνωμένο Βασίλειο.",
        "example_en": "Which were the three guarantor powers of the Republic of Cyprus in 1960? Greece, Turkey, and the United Kingdom.",
        "example2_el": "Οι εγγυήτριες δυνάμεις ανέλαβαν την υποχρέωση να προστατεύουν την ανεξαρτησία και την εδαφική ακεραιότητα της Κύπρου.",
        "example2_en": "The guarantor powers undertook the obligation to protect the independence and territorial integrity of Cyprus."
    },
    {
        "id": "CYP-U02-007",
        "greek": "η Πράσινη Γραμμή (η Νεκρή Ζώνη)",
        "phonetic_hint": "ee PRAH-see-nee ghrah-MEE (ee neh-KREE ZOH-nee)",
        "english": "the Green Line (the UN Buffer Zone)",
        "notes": "First drawn in December 1963 in Nicosia with a green chinagraph pencil by British General Peter Young; extended across the island (180 km) after the 1974 Turkish invasion.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι Πράσινες Γραμμές",
            "accusative_singular": "την Πράσινη Γραμμή"
        },
        "keg_communicative_function": "Modern History — Division of Cyprus & UN Buffer Zone",
        "example_el": "Η Πράσινη Γραμμή χωρίζει τις ελεύθερες περιοχές της Κυπριακής Δημοκρατίας από τις κατεχόμενες περιοχές.",
        "example_en": "The Green Line separates the government-controlled areas of the Republic of Cyprus from the occupied areas.",
        "example2_el": "Η Νεκρή Ζώνη ελέγχεται από την Ειρηνευτική Δύναμη των Ηνωμένων Εθνών στην Κύπρο (ΟΥΝΦΙΚΥΠ).",
        "example2_en": "The Buffer Zone is controlled by the United Nations Peacekeeping Force in Cyprus (UNFICYP)."
    },
    {
        "id": "CYP-U02-008",
        "greek": "η ΟΥΝΦΙΚΥΠ (Ειρηνευτική Δύναμη του ΟΗΕ)",
        "phonetic_hint": "ee OON-fee-keep (ee-ree-nef-tee-KEE THEE-nah-mee too oh-ee-EH)",
        "english": "UNFICYP (United Nations Peacekeeping Force in Cyprus)",
        "notes": "Established in March 1964 by UN Security Council Resolution 186 to prevent recurrence of fighting and supervise the ceasefire lines.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι Ειρηνευτικές Δυνάμεις",
            "accusative_singular": "την ΟΥΝΦΙΚΥΠ"
        },
        "keg_communicative_function": "Modern History — UN peacekeeping in Cyprus",
        "example_el": "Η Ειρηνευτική Δύναμη του ΟΗΕ (ΟΥΝΦΙΚΥΠ) βρίσκεται στην Κύπρο από το 1964.",
        "example_en": "The UN Peacekeeping Force (UNFICYP) has been in Cyprus since 1964.",
        "example2_el": "Αποστολή της ΟΥΝΦΙΚΥΠ είναι η επιτήρηση της Νεκρής Ζώνης και η διατήρηση της ειρήνης.",
        "example2_en": "The mission of UNFICYP is the supervision of the Buffer Zone and the maintenance of peace."
    },
    {
        "id": "CYP-U02-009",
        "greek": "το πραξικόπημα της 15ης Ιουλίου 1974",
        "phonetic_hint": "toh prahk-see-KOH-pee-mah tees theh-kah-PEHN-dees ee-oo-LEE-oo 1974",
        "english": "the coup d'état of 15 July 1974",
        "notes": "Staged on 15 July 1974 by the military junta in Athens and EOKA B to overthrow President Makarios III, giving Turkey the pretext to invade five days later.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα πραξικοπήματα",
            "accusative_singular": "το πραξικόπημα της 15ης Ιουλίου 1974"
        },
        "keg_communicative_function": "Modern History — Events of July 1974",
        "example_el": "Στις 15 Ιουλίου 1974 εκδηλώθηκε στρατιωτικό πραξικόπημα για την ανατροπή του Προέδρου Μακαρίου.",
        "example_en": "On 15 July 1974, a military coup was staged to overthrow President Makarios.",
        "example2_el": "Το πραξικόπημα της 15ης Ιουλίου 1974 έδωσε την αφορμή στην Τουρκία να εισβάλει στην Κύπρο πέντε ημέρες αργότερα.",
        "example2_en": "The coup of 15 July 1974 gave Turkey the pretext to invade Cyprus five days later."
    },
    {
        "id": "CYP-U02-010",
        "greek": "— Πότε έγινε η τουρκική εισβολή στην Κύπρο; — Στις 20 Ιουλίου 1974.",
        "phonetic_hint": "POH-teh EH-yee-neh ee toor-kee-KEE ees-voh-LEE steen KEE-proh? stees EE-koh-see ee-oo-LEE-oo 1974",
        "english": "— When did the Turkish invasion of Cyprus take place? — On 20 July 1974.",
        "notes": "Essential exam question! The invasion occurred in two phases: Phase 1 on 20 July 1974 (landing at Pentemili, Kyrenia) and Phase 2 on 14 August 1974 (occupying Morphou, Famagusta, and Karpasia).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Date of the Turkish invasion",
        "example_el": "Η τουρκική εισβολή στην Κύπρο ξεκίνησε τα ξημερώματα της 20ής Ιουλίου 1974 από τις ακτές της Κερύνειας.",
        "example_en": "The Turkish invasion of Cyprus began at dawn on 20 July 1974 on the coast of Kyrenia.",
        "example2_el": "Η δεύτερη φάση της τουρκικής εισβολής εκδηλώθηκε στις 14 Αυγούστου 1974.",
        "example2_en": "The second phase of the Turkish invasion took place on 14 August 1974."
    },
    {
        "id": "CYP-U02-011",
        "greek": "τα κατεχόμενα εδάφη",
        "phonetic_hint": "tah kah-teh-KHOH-meh-nah eh-THAH-fee",
        "english": "the occupied territories",
        "notes": "Since August 1974, approximately 36.2%–37% of the territory of the Republic of Cyprus remains under illegal Turkish military occupation.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κατεχόμενα εδάφη",
            "accusative_plural": "τα κατεχόμενα εδάφη"
        },
        "keg_communicative_function": "Modern History — Consequences of 1974",
        "example_el": "Περίπου το 37% του εδάφους της Κυπριακής Δημοκρατίας παραμένει υπό τουρκική στρατιωτική κατοχή από το 1974.",
        "example_en": "Approximately 37% of the territory of the Republic of Cyprus remains under Turkish military occupation since 1974.",
        "example2_el": "Η επαρχία της Κερύνειας βρίσκεται εξ ολοκλήρου στα κατεχόμενα εδάφη.",
        "example2_en": "The district of Kyrenia is located entirely within the occupied territories."
    },
    {
        "id": "CYP-U02-012",
        "greek": "οι πρόσφυγες",
        "phonetic_hint": "ee PROH-sfee-yehs",
        "english": "the refugees / internally displaced persons",
        "notes": "Approximately 200,000 Greek Cypriots (one-third of the population) were forcibly displaced from their homes in 1974.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "singular": "ο πρόσφυγας / η πρόσφυγας",
            "plural": "οι πρόσφυγες",
            "accusative_singular": "τον πρόσφυγα"
        },
        "keg_communicative_function": "Modern History — Displacement & humanitarian impact",
        "example_el": "Το 1974 περίπου διακόσιες χιλιάδες (200.000) Ελληνοκύπριοι έγιναν πρόσφυγες στην ίδια τους την πατρίδα.",
        "example_en": "In 1974, approximately two hundred thousand (200,000) Greek Cypriots became refugees in their own homeland.",
        "example2_el": "Το κράτος δημιούργησε προσφυγικούς συνοικισμούς για τη στέγαση των εκτοπισθέντων πολιτών.",
        "example2_en": "The state created refugee housing estates to house the displaced citizens."
    },
    {
        "id": "CYP-U02-013",
        "greek": "οι αγνοούμενοι",
        "phonetic_hint": "ee ah-ghnoh-OO-meh-nee",
        "english": "the missing persons",
        "notes": "Humanitarian tragedy of the 1963–64 and 1974 events. Investigated by the bi-communal Committee on Missing Persons in Cyprus (Διερευνητική Επιτροπή για τους Αγνοουμένους - ΔΕΑ).",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "singular": "ο αγνοούμενος",
            "plural": "οι αγνοούμενοι",
            "accusative_singular": "τον αγνοούμενο"
        },
        "keg_communicative_function": "Modern History — Humanitarian issues of the Cyprus Problem",
        "example_el": "Η Διερευνητική Επιτροπή για τους Αγνοουμένους (ΔΕΑ) εργάζεται για τον εντοπισμό και την ταυτοποίηση των αγνοουμένων.",
        "example_en": "The Committee on Missing Persons (CMP) works to locate and identify the missing persons.",
        "example2_el": "Το ζήτημα των αγνοουμένων αποτελεί μία από τις πιο τραγικές ανθρωπιστικές πτυχές της τουρκικής εισβολής.",
        "example2_en": "The issue of missing persons constitutes one of the most tragic humanitarian aspects of the Turkish invasion."
    },
    {
        "id": "CYP-U02-014",
        "greek": "οι εγκλωβισμένοι",
        "phonetic_hint": "ee ehng-gloh-veez-MEH-nee",
        "english": "the enclaved persons",
        "notes": "Greek Cypriots and Maronites who remained in their ancestral villages in the occupied Karpasia peninsula (π.χ. Ριζοκάρπασο) and Maronite villages (π.χ. Κορμακίτης) after 1974.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "singular": "ο εγκλωβισμένος",
            "plural": "οι εγκλωβισμένοι",
            "accusative_singular": "τον εγκλωβισμένο"
        },
        "keg_communicative_function": "Modern History — Enclaved population in Karpasia",
        "example_el": "Οι εγκλωβισμένοι παρέμειναν στα χωριά τους στη χερσόνησο της Καρπασίας και στα μαρωνίτικα χωριά μετά το 1974.",
        "example_en": "The enclaved remained in their villages on the Karpasia peninsula and in the Maronite villages after 1974.",
        "example2_el": "Στο Ριζοκάρπασο λειτουργούν ελληνικό δημοτικό σχολείο και γυμνάσιο για τα παιδιά των εγκλωβισμένων.",
        "example2_en": "In Rizokarpaso, a Greek primary school and high school operate for the children of the enclaved."
    },
    {
        "id": "CYP-U02-015",
        "greek": "— Πότε έγινε η παράνομη ανακήρυξη του «ψευδοκράτους» στα κατεχόμενα; — Στις 15 Νοεμβρίου 1983.",
        "phonetic_hint": "POH-teh EH-yee-neh ee pah-RAH-noh-mee ah-nah-KEE-reek-see too psef-thoh-KRAH-toos? stees theh-kah-PEHN-deh noh-ehm-VREE-oo 1983",
        "english": "— When did the illegal declaration of the 'pseudo-state' in the occupied areas take place? — On 15 November 1983.",
        "notes": "Past exam question! Unilaterally declared by Rauf Denktaş on 15 Nov 1983; condemned as legally invalid by UN Security Council Resolutions 541 (1983) and 550 (1984). Recognized only by Turkey.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Illegal 1983 UDI & UN Resolutions",
        "example_el": "Στις 15 Νοεμβρίου 1983 η τουρκοκυπριακή ηγεσία προχώρησε στην παράνομη ανακήρυξη του λεγόμενου «ψευδοκράτους».",
        "example_en": "On 15 November 1983, the Turkish Cypriot leadership proceeded with the illegal declaration of the so-called 'pseudo-state'.",
        "example2_el": "Το Συμβούλιο Ασφαλείας του ΟΗΕ καταδίκασε την ενέργεια αυτή με το Ψήφισμα 541 και κάλεσε όλα τα κράτη να μην το αναγνωρίσουν.",
        "example2_en": "The UN Security Council condemned this action with Resolution 541 and called on all states not to recognize it."
    },
    {
        "id": "CYP-U02-016",
        "greek": "— Ποιος διετέλεσε Πρόεδρος της Κυπριακής Δημοκρατίας αμέσως μετά τον θάνατο του Μακαρίου Γ΄ (1977–1988); — Ο Σπύρος Κυπριανού.",
        "phonetic_hint": "pyos theeh-TEH-leh-seh PROH-eth-ros tees kee-pree-ah-KEES theem-oh-krah-TEE-ahs ah-MEH-sos meh-TAH ton THAH-nah-toh too mah-kah-REE-oo? oh SPEE-ros kee-pree-ah-NOO",
        "english": "— Who served as President of the Republic of Cyprus immediately after the death of Makarios III (1977–1988)? — Spyros Kyprianou.",
        "notes": "Past exam question on Presidential chronology! Spyros Kyprianou was the 2nd President of the Republic (1977–1988).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Presidents of the Republic of Cyprus",
        "example_el": "Ο Σπύρος Κυπριανού υπήρξε ο δεύτερος Πρόεδρος της Κυπριακής Δημοκρατίας από το 1977 έως το 1988.",
        "example_en": "Spyros Kyprianou was the second President of the Republic of Cyprus from 1977 to 1988.",
        "example2_el": "Μετά τον Σπύρο Κυπριανού, τρίτος Πρόεδρος εξελέγη ο Γιώργος Βασιλείου (1988–1993).",
        "example2_en": "After Spyros Kyprianou, George Vasiliou was elected third President (1988–1993)."
    },
    {
        "id": "CYP-U02-017",
        "greek": "ο Γιώργος Βασιλείου (Πρόεδρος 1988–1993)",
        "phonetic_hint": "oh YOR-ghos vah-see-LEE-oo",
        "english": "George Vasiliou (3rd President of Cyprus, 1988–1993)",
        "notes": "During his presidency, Cyprus submitted its formal application for membership in the European Communities (July 1990) and founded the University of Cyprus (1989).",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "accusative_singular": "τον Γιώργο Βασιλείου"
        },
        "keg_communicative_function": "Modern History — Presidents of Cyprus",
        "example_el": "Επί προεδρίας του Γιώργου Βασιλείου το 1990, η Κύπρος υπέβαλε αίτηση ένταξης στην Ευρωπαϊκή Οικονομική Κοινότητα.",
        "example_en": "During the presidency of George Vasiliou in 1990, Cyprus submitted an application to join the European Economic Community.",
        "example2_el": "Κατά τη θητεία του Γιώργου Βασιλείου ιδρύθηκε και το Πανεπιστήμιο Κύπρου το 1989.",
        "example2_en": "During George Vasiliou's term, the University of Cyprus was also founded in 1989."
    },
    {
        "id": "CYP-U02-018",
        "greek": "ο Γλαύκος Κληρίδης (Πρόεδρος 1993–2003)",
        "phonetic_hint": "oh GHLAHF-kos klee-REE-thees",
        "english": "Glafcos Clerides (4th President of Cyprus, 1993–2003)",
        "notes": "Served two consecutive five-year terms (1993–1998 and 1998–2003), completing Cyprus's EU accession negotiations.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "accusative_singular": "τον Γλαύκο Κληρίδη"
        },
        "keg_communicative_function": "Modern History — Presidents of Cyprus",
        "example_el": "Ο Γλαύκος Κληρίδης διετέλεσε τέταρτος Πρόεδρος της Κυπριακής Δημοκρατίας για δύο θητείες, από το 1993 έως το 2003.",
        "example_en": "Glafcos Clerides served as the fourth President of the Republic of Cyprus for two terms, from 1993 to 2003.",
        "example2_el": "Κατά τη διακυβέρνηση του Γλαύκου Κληρίδη ολοκληρώθηκαν οι ενταξιακές διαπραγματεύσεις της Κύπρου με την Ευρωπαϊκή Ένωση.",
        "example2_en": "During Glafcos Clerides's administration, Cyprus's accession negotiations with the European Union were completed."
    },
    {
        "id": "CYP-U02-019",
        "greek": "— Ποιος ήταν Πρόεδρος της Κυπριακής Δημοκρατίας το 2004 κατά την ένταξη στην Ευρωπαϊκή Ένωση; — Ο Τάσσος Παπαδόπουλος.",
        "phonetic_hint": "pyos EE-tahn PROH-eth-ros tees kee-pree-ah-KEES theem-oh-krah-TEE-ahs toh 2004 kah-TAH teen EHN-dahk-see steen ev-roh-pah-ee-KEE EH-noh-see? oh TAH-sos pah-pah-THOH-poo-los",
        "english": "— Who was President of the Republic of Cyprus in 2004 during accession to the European Union? — Tassos Papadopoulos.",
        "notes": "Frequent past exam question! Tassos Papadopoulos served as the 5th President (2003–2008). He signed the Accession Treaty in Athens (April 2003) and presided over the 2004 Annan Plan referendum and EU entry.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Presidency during 2004 EU Accession",
        "example_el": "Ο Τάσσος Παπαδόπουλος διετέλεσε πέμπτος Πρόεδρος της Κυπριακής Δημοκρατίας από το 2003 έως το 2008.",
        "example_en": "Tassos Papadopoulos served as the fifth President of the Republic of Cyprus from 2003 to 2008.",
        "example2_el": "Επί προεδρίας Τάσσου Παπαδόπουλου η Κύπρος εντάχθηκε στην Ευρωπαϊκή Ένωση (2004) και στην Ευρωζώνη (2008).",
        "example2_en": "During Tassos Papadopoulos's presidency, Cyprus joined the European Union (2004) and the Eurozone (2008)."
    },
    {
        "id": "CYP-U02-020",
        "greek": "το δημοψήφισμα για το Σχέδιο Ανάν (24 Απριλίου 2004)",
        "phonetic_hint": "toh theem-oh-PSEE-feez-mah yah toh SKHEH-thee-oh ah-NAHN",
        "english": "the referendum on the Annan Plan (24 April 2004)",
        "notes": "UN Secretary-General Kofi Annan's plan for a solution to the Cyprus Problem. Rejected by 76% of Greek Cypriots and approved by 65% of Turkish Cypriots in simultaneous referendums on 24 April 2004.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα δημοψηφίσματα",
            "accusative_singular": "το δημοψήφισμα για το Σχέδιο Ανάν"
        },
        "keg_communicative_function": "Modern History — 2004 Annan Plan Referendum",
        "example_el": "Στις 24 Απριλίου 2004 διεξήχθησαν χωριστά δημοψηφίσματα στις δύο κοινότητες για το Σχέδιο Ανάν του ΟΗΕ.",
        "example_en": "On 24 April 2004, separate referendums were held in the two communities on the UN's Annan Plan.",
        "example2_el": "Το Σχέδιο Ανάν απορρίφθηκε από την πλειοψηφία (76%) των Ελληνοκυπρίων και εγκρίθηκε από το 65% των Τουρκοκυπρίων.",
        "example2_en": "The Annan Plan was rejected by the majority (76%) of Greek Cypriots and approved by 65% of Turkish Cypriots."
    },
    {
        "id": "CYP-U02-021",
        "greek": "— Πότε εντάχθηκε επίσημα η Κυπριακή Δημοκρατία στην Ευρωπαϊκή Ένωση; — Την 1η Μαΐου 2004.",
        "phonetic_hint": "POH-teh ehn-DAHKH-thee-keh eh-PEE-see-mah ee kee-pree-ah-KEE theem-oh-krah-TEE-ah steen ev-roh-pah-ee-KEE EH-noh-see? teen PROH-tee mah-EE-oo 2004",
        "english": "— When did the Republic of Cyprus officially join the European Union? — On 1 May 2004.",
        "notes": "One of the most frequently asked questions in the exam! Cyprus joined the EU on 1 May 2004 alongside 9 other countries; the European acquis (κοινοτικό κεκτημένο) is suspended in the occupied areas under Protocol 10.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Date of EU Accession",
        "example_el": "Η Κυπριακή Δημοκρατία έγινε πλήρες μέλος της Ευρωπαϊκής Ένωσης την 1η Μαΐου 2004.",
        "example_en": "The Republic of Cyprus became a full member of the European Union on 1 May 2004.",
        "example2_el": "Ενώ ολόκληρη η Κύπρος εντάχθηκε στην ΕΕ, η εφαρμογή του ευρωπαϊκού κεκτημένου αναστέλλεται στις κατεχόμενες περιοχές.",
        "example2_en": "While the whole of Cyprus joined the EU, the application of the European acquis is suspended in the occupied areas."
    },
    {
        "id": "CYP-U02-022",
        "greek": "ο Δημήτρης Χριστόφιας (Πρόεδρος 2008–2013)",
        "phonetic_hint": "oh theem-EE-trees khree-STOH-fyahs",
        "english": "Demetris Christofias (6th President of Cyprus, 2008–2013)",
        "notes": "Sixth President of the Republic (2008–2013) and former Speaker of the House (2001–2008) and General Secretary of AKEL. During his term Cyprus held its first Presidency of the Council of the EU (2nd half of 2012).",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "accusative_singular": "τον Δημήτρη Χριστόφια"
        },
        "keg_communicative_function": "Modern History — Presidents of Cyprus",
        "example_el": "Ο Δημήτρης Χριστόφιας διετέλεσε έκτος Πρόεδρος της Κυπριακής Δημοκρατίας από το 2008 έως το 2013.",
        "example_en": "Demetris Christofias served as the sixth President of the Republic of Cyprus from 2008 to 2013.",
        "example2_el": "Το δεύτερο εξάμηνο του 2012 η Κύπρος ανέλαβε για πρώτη φορά την Προεδρία του Συμβουλίου της Ευρωπαϊκής Ένωσης.",
        "example2_en": "In the second half of 2012, Cyprus assumed the Presidency of the Council of the European Union for the first time."
    },
    {
        "id": "CYP-U02-023",
        "greek": "ο Νίκος Αναστασιάδης (Πρόεδρος 2013–2023)",
        "phonetic_hint": "oh NEE-kos ah-nah-stah-see-AH-thees",
        "english": "Nicos Anastasiades (7th President of Cyprus, 2013–2023)",
        "notes": "Seventh President of the Republic, elected for two terms (2013–2018 and 2018–2023). During his presidency, the General Healthcare System (ΓεΣΥ) was implemented and the Crans-Montana talks (2017) took place.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "accusative_singular": "τον Νίκο Αναστασιάδη"
        },
        "keg_communicative_function": "Modern History — Presidents of Cyprus",
        "example_el": "Ο Νίκος Αναστασιάδης υπήρξε ο έβδομος Πρόεδρος της Κυπριακής Δημοκρατίας από το 2013 έως το 2023.",
        "example_en": "Nicos Anastasiades was the seventh President of the Republic of Cyprus from 2013 to 2023.",
        "example2_el": "Εξελέγη Πρόεδρος για δύο συνεχόμενες πενταετείς θητείες, το 2013 και το 2018.",
        "example2_en": "He was elected President for two consecutive five-year terms, in 2013 and 2018."
    },
    {
        "id": "CYP-U02-024",
        "greek": "η Διζωνική Δικοινοτική Ομοσπονδία (ΔΔΟ)",
        "phonetic_hint": "ee thee-zoh-nee-KEE thee-kee-noh-tee-KEE oh-moh-spon-THEE-ah",
        "english": "Bi-zonal, Bi-communal Federation (BBF)",
        "notes": "The agreed framework under United Nations Security Council resolutions and the High-Level Agreements (Makarios-Denktaş 1977 & Kyprianou-Denktaş 1979) for a comprehensive settlement of the Cyprus problem.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι Διζωνικές Δικοινοτικές Ομοσπονδίες",
            "accusative_singular": "τη Διζωνική Δικοινοτική Ομοσπονδία"
        },
        "keg_communicative_function": "Modern History — Framework for solving the Cyprus problem",
        "example_el": "Τα ψηφίσματα του ΟΗΕ προβλέπουν λύση Διζωνικής Δικοινοτικής Ομοσπονδίας με πολιτική ισότητα.",
        "example_en": "UN resolutions provide for a solution of a Bi-zonal, Bi-communal Federation with political equality.",
        "example2_el": "Η λύση προνοεί ένα κράτος με μία κυριαρχία, μία διεθνή προσωπικότητα και μία ιθαγένεια.",
        "example2_en": "The solution provides for one state with a single sovereignty, a single international personality, and a single citizenship."
    },
    {
        "id": "CYP-U02-025",
        "greek": "τα Βαρώσια (η περίκλειστη πόλη της Αμμοχώστου)",
        "phonetic_hint": "tah vah-ROH-syah (ee peh-REE-klee-stee POH-lee tees ah-moh-KHOH-stoo)",
        "english": "Varosha (the fenced-off quarter of Famagusta)",
        "notes": "Once Cyprus's premier tourist resort, abandoned and fenced off by the Turkish army in August 1974. UN Security Council Resolution 550 (1984) calls for its return to its lawful inhabitants under UN administration.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Βαρώσια",
            "accusative_plural": "τα Βαρώσια",
            "genitive_plural": "των Βαρωσίων"
        },
        "keg_communicative_function": "Modern History — Famagusta & UN Resolution 550",
        "example_el": "Τα Βαρώσια είναι η περίκλειστη συνοικία της Αμμοχώστου που εκκενώθηκε κατά την τουρκική εισβολή του 1974.",
        "example_en": "Varosha is the fenced-off quarter of Famagusta that was evacuated during the Turkish invasion of 1974.",
        "example2_el": "Το Ψήφισμα 550 του ΟΗΕ ζητά την επιστροφή των Βαρωσίων στους νόμιμους κατοίκους τους υπό τη διοίκηση του ΟΗΕ.",
        "example2_en": "UN Resolution 550 calls for the return of Varosha to its lawful inhabitants under UN administration."
    },
    {
        "id": "CYP-U02-026",
        "greek": "οι Κυρίαρχες Βρετανικές Βάσεις (Ακρωτήρι & Δεκέλεια)",
        "phonetic_hint": "ee kee-REE-ahr-khehs vreh-tah-nee-KEHS VAH-sees (ah-kroh-TEE-ree keh theh-KEH-lee-ah)",
        "english": "the British Sovereign Base Areas (Akrotiri & Dhekelia)",
        "notes": "Two areas (Akrotiri near Limassol and Dhekelia near Larnaca/Famagusta, totaling ~3% of the island's area) retained by the UK under the 1960 Treaty of Establishment.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι Κυρίαρχες Βρετανικές Βάσεις",
            "accusative_plural": "τις Κυρίαρχες Βρετανικές Βάσεις"
        },
        "keg_communicative_function": "Modern History — 1960 Treaty of Establishment",
        "example_el": "Πού βρίσκονται οι δύο βρετανικές στρατιωτικές βάσεις στην Κύπρο; Στο Ακρωτήρι και στη Δεκέλεια.",
        "example_en": "Where are the two British military bases in Cyprus located? At Akrotiri and Dhekelia.",
        "example2_el": "Οι Βρετανικές Βάσεις καλύπτουν περίπου το 3% της συνολικής έκτασης του νησιού.",
        "example2_en": "The British Bases cover approximately 3% of the total area of the island."
    },
    {
        "id": "CYP-U02-027",
        "greek": "η διάνοιξη των οδοφραγμάτων (2003)",
        "phonetic_hint": "ee thee-AH-neek-see ton oh-thoh-frahgh-MAH-ton",
        "english": "the opening of the crossing points / checkpoints (2003)",
        "notes": "In April 2003, partial movement across the Green Line began for the first time since 1974 (starting with Ledra Palace, and later Ledra Street / οδός Λήδρας in 2008).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι διανοίξεις των οδοφραγμάτων",
            "accusative_singular": "τη διάνοιξη των οδοφραγμάτων"
        },
        "keg_communicative_function": "Modern History — Green Line crossing points",
        "example_el": "Τον Απρίλιο του 2003 άνοιξαν για πρώτη φορά από το 1974 οδοφράγματα κατά μήκος της Πράσινης Γραμμής.",
        "example_en": "In April 2003, crossing points along the Green Line opened for the first time since 1974.",
        "example2_el": "Το οδόφραγμα της οδού Λήδρας στο κέντρο της Λευκωσίας άνοιξε το 2008.",
        "example2_en": "The Ledra Street crossing point in the center of Nicosia opened in 2008."
    },
    {
        "id": "CYP-U02-028",
        "greek": "τα Φυλακισμένα Μνήματα",
        "phonetic_hint": "tah fee-lah-keez-MEH-nah MNEE-mah-tah",
        "english": "the Imprisoned Graves (Central Prisons of Nicosia)",
        "notes": "Historic monument in the Central Prisons of Nicosia where 13 EOKA fighters (including Evagoras Pallikarides and Karaolis & Demetriou) are buried.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Φυλακισμένα Μνήματα",
            "accusative_plural": "τα Φυλακισμένα Μνήματα"
        },
        "keg_communicative_function": "Modern History — National memorials in Nicosia",
        "example_el": "Τα Φυλακισμένα Μνήματα βρίσκονται στις Κεντρικές Φυλακές Λευκωσίας και αποτελούν ιερό μνημείο του αγώνα του 1955–1959.",
        "example_en": "The Imprisoned Graves are located in the Central Prisons of Nicosia and constitute a sacred memorial of the 1955–1959 struggle.",
        "example2_el": "Εκεί είναι θαμμένοι δεκατρείς αγωνιστές της ΕΟΚΑ, μεταξύ των οποίων ο Μιχαλάκης Καραολής και ο Ευαγόρας Παλληκαρίδης.",
        "example2_en": "Thirteen EOKA fighters are buried there, including Michalakis Karaolis and Evagoras Pallikarides."
    },
    {
        "id": "CYP-U02-029",
        "greek": "ο Τύμβος της Μακεδονίτισσας",
        "phonetic_hint": "oh TEEM-vos tees mah-keh-thoh-NEE-tee-sahs",
        "english": "the Makedonitissa Tomb (Military Cemetery in Nicosia)",
        "notes": "Military cemetery and memorial in Engomi, Nicosia, honoring Greek Cypriot and Greek soldiers who fell defending Cyprus during the 1974 Turkish invasion.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι Τύμβοι",
            "accusative_singular": "τον Τύμβο της Μακεδονίτισσας"
        },
        "keg_communicative_function": "Modern History — 1974 memorials",
        "example_el": "Ο Τύμβος της Μακεδονίτισσας στη Λευκωσία είναι στρατιωτικό κοιμητήριο και μνημείο των πεσόντων του 1974.",
        "example_en": "The Makedonitissa Tomb in Nicosia is a military cemetery and memorial to the fallen of 1974.",
        "example2_el": "Κάθε χρόνο στις 20 Ιουλίου τελείται στον Τύμβο της Μακεδονίτισσας επίσημο μνημόσυνο παρουσία του Προέδρου της Δημοκρατίας.",
        "example2_en": "Every year on 20 July, an official memorial service is held at the Makedonitissa Tomb in the presence of the President of the Republic."
    },
    {
        "id": "CYP-U02-030",
        "greek": "η έκρηξη στη ναυτική βάση στο Μαρί (11 Ιουλίου 2011)",
        "phonetic_hint": "ee EH-kreek-see stee nahf-tee-KEE VAH-see stoh mah-REE",
        "english": "the Mari naval base explosion (11 July 2011)",
        "notes": "Major modern tragic event: on 11 July 2011, confiscated munitions exploded at the 'Evangelos Florakis' Naval Base at Mari, killing 13 people (firefighters, sailors, officers) and destroying the adjacent Vassilikos power station.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι εκρήξεις",
            "accusative_singular": "την έκρηξη στη ναυτική βάση στο Μαρί"
        },
        "keg_communicative_function": "Modern History — Major post-2000 events",
        "example_el": "Στις 11 Ιουλίου 2011 σημειώθηκε φονική έκρηξη στη ναυτική βάση «Ευάγγελος Φλωράκης» στο Μαρί, με 13 νεκρούς.",
        "example_en": "On 11 July 2011, a deadly explosion occurred at the 'Evangelos Florakis' naval base in Mari, resulting in 13 deaths.",
        "example2_el": "Από την έκρηξη στο Μαρί καταστράφηκε και ο γειτονικός ηλεκτροπαραγωγός σταθμός του Βασιλικού.",
        "example2_en": "The explosion at Mari also destroyed the neighboring Vassilikos power station."
    }
]

# ==============================================================================
# UNIT CYP-03: Γεωγραφία, Επαρχίες, Πόλεις & Φύση (30 Cards)
# ==============================================================================
NOTES_CYP_03 = """Unit CYP-03 Core Exam Notes: Γεωγραφία, Επαρχίες, Πόλεις & Φύση της Κύπρου (Geography, Districts, Cities & Nature)

• Γεωγραφική Θέση & Μέγεθος:
  - Η Κύπρος βρίσκεται στη βορειοανατολική Μεσόγειο (Northeastern Mediterranean), στο σταυροδρόμι Ευρώπης, Ασίας και Αφρικής.
  - Είναι το τρίτο μεγαλύτερο νησί της Μεσογείου (μετά τη Σικελία και τη Σαρδηνία), με έκταση 9.251 τετραγωνικά χιλιόμετρα (τ.χλμ.).

• Οι 6 Επαρχίες της Κύπρου (The 6 Administrative Districts — High Exam Frequency!):
  1. Λευκωσία (Nicosia): Πρωτεύουσα και μεγαλύτερη σε πληθυσμό πόλη, στο κέντρο του νησιού. Η τελευταία διαιρεμένη πρωτεύουσα της Ευρώπης.
  2. Λεμεσός (Limassol): Δεύτερη μεγαλύτερη πόλη, στη νότια ακτή. Διαθέτει το μεγαλύτερο εμπορικό λιμάνι της Κύπρου και αποτελεί κέντρο ναυτιλίας.
  3. Λάρνακα (Larnaca): Στη νοτιοανατολική ακτή. Διαθέτει το κύριο διεθνές αεροδρόμιο, την Αλυκή Λάρνακας (με τα φλαμίνγκο) και το τέμενος Χαλά Σουλτάν Τεκκέ.
  4. Πάφος (Paphos): Στη νοτιοδυτική Κύπρο. Διαθέτει το δεύτερο διεθνές αεροδρόμιο, την Πόλη Χρυσοχούς, τη χερσόνησο του Ακάμα και μνημεία UNESCO.
  5. Αμμόχωστος (Famagusta): Στα ανατολικά. Η πόλη της Αμμοχώστου είναι κατεχόμενη από το 1974. Στην ελεύθερη επαρχία Αμμοχώστου ανήκουν το Παραλίμνι (προσωρινή διοικητική έδρα), η Αγία Νάπα, ο Πρωταράς και η Δερύνεια.
  6. Κερύνεια (Kyrenia): Στη βόρεια ακτή. Είναι η μικρότερη επαρχία και η μόνη που βρίσκεται εξ ολοκλήρου υπό τουρκική κατοχή από το 1974.

• Βουνά, Πεδιάδες, Ποτάμια & Φύση:
  - Οροσειρά του Τροόδους: Η μεγαλύτερη οροσειρά (κεντρική/νοτιοδυτική Κύπρος). Ψηλότερη κορυφή: ο Όλυμπος (Χιονίστρα) στα 1.952 μέτρα. Άλλες κορυφές Τροόδους: Μαδαρή, Παπούτσα.
  - Οροσειρά του Πενταδακτύλου (Βόρεια): Κατεχόμενη ασβεστολιθική οροσειρά. Κορυφές & κάστρα: Κυπαρισσόβουνο (1.024 μ.), Άγιος Ιλαρίωνας, Βουφαβέντο, Καντάρα.
  - Πεδιάδα της Μεσαορίας: Η μεγαλύτερη εύφορη πεδιάδα, ανάμεσα στο Τρόοδος και τον Πενταδάκτυλο.
  - Ποταμοί & Φράγματα: Μεγαλύτερος ποταμός ο Πεδιαίος (ή Πηδιάς, ~100 χλμ.). Μεγαλύτερο φράγμα: το φράγμα του Κούρη (στην επαρχία Λεμεσού).
  - Χλωρίδα & Πανίδα: Εθνικό ζώο το κυπριακό αγρινό (Ovis orientalis ophion), θαλάσσιες χελώνες Καρέτα-Καρέτα και Πράσινη Χελώνα (στον Ακάμα/Λάρα), εθνικό δέντρο η λατζιά (χρυσή δρυς της Κύπρου)."""

CARDS_CYP_03 = [
    {
        "id": "CYP-U03-001",
        "greek": "— Σε ποιο μέρος της Μεσογείου βρίσκεται η Κύπρος; — Στη βορειοανατολική Μεσόγειο.",
        "phonetic_hint": "seh pyoh MEH-ros tees meh-soh-YEE-oo VREE-skeh-teh ee KEE-pros? stee voh-ree-oh-ah-nah-toh-lee-KEE meh-SOH-yee-oh",
        "english": "— In which part of the Mediterranean is Cyprus located? — In the northeastern Mediterranean.",
        "notes": "Actual past exam question! Watch out for distractors like 'νοτιοδυτική' or 'βορειοδυτική'. Cyprus is in the northeastern corner of the Mediterranean (βορειοανατολική Μεσόγειος).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Geographical location of Cyprus",
        "example_el": "Η Κύπρος βρίσκεται στη βορειοανατολική λεκάνη της Μεσογείου, στο σταυροδρόμι τριών ηπείρων.",
        "example_en": "Cyprus is located in the northeastern basin of the Mediterranean, at the crossroads of three continents.",
        "example2_el": "Με έκταση 9.251 τετραγωνικά χιλιόμετρα, η Κύπρος είναι το τρίτο μεγαλύτερο νησί της Μεσογείου μετά τη Σικελία και τη Σαρδηνία.",
        "example2_en": "With an area of 9,251 square kilometers, Cyprus is the third largest island in the Mediterranean after Sicily and Sardinia."
    },
    {
        "id": "CYP-U03-002",
        "greek": "— Ποιες είναι οι έξι (6) επαρχίες της Κυπριακής Δημοκρατίας; — Λευκωσία, Λεμεσός, Λάρνακα, Πάφος, Αμμόχωστος και Κερύνεια.",
        "phonetic_hint": "pyehs EE-neh ee EHK-see eh-pahr-KHEE-ehs tees kee-pree-ah-KEES theem-oh-krah-TEE-ahs? lef-koh-SEE-ah, leh-meh-SOHS, LAHR-nah-kah, PAH-fos, ah-MOH-khoh-stos keh keh-REE-nyah",
        "english": "— What are the six (6) districts of the Republic of Cyprus? — Nicosia, Limassol, Larnaca, Paphos, Famagusta, and Kyrenia.",
        "notes": "Essential exam question! Cyprus is administratively divided into 6 districts (έξι επαρχίες).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Six administrative districts of Cyprus",
        "example_el": "Η Κυπριακή Δημοκρατία διαιρείται διοικητικά σε έξι επαρχίες.",
        "example_en": "The Republic of Cyprus is administratively divided into six districts.",
        "example2_el": "Η επαρχία Λευκωσίας είναι η μεγαλύτερη σε πληθυσμό, ενώ η επαρχία Κερύνειας είναι η μικρότερη σε έκταση.",
        "example2_en": "The Nicosia district is the largest in population, while the Kyrenia district is the smallest in area."
    },
    {
        "id": "CYP-U03-003",
        "greek": "η Λευκωσία (η πρωτεύουσα)",
        "phonetic_hint": "ee lef-koh-SEE-ah (ee proh-TEH-voo-sah)",
        "english": "Nicosia (the capital city)",
        "notes": "Capital and largest city of Cyprus, located inland near the center of the island; surrounded in its historic core by the 16th-century Venetian Walls (τα Ενετικά Τείχη).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "accusative_singular": "τη Λευκωσία",
            "genitive_singular": "της Λευκωσίας"
        },
        "keg_communicative_function": "Geography — Capital of Cyprus",
        "example_el": "Η Λευκωσία είναι η πρωτεύουσα της Κύπρου και η τελευταία διαιρεμένη πρωτεύουσα της Ευρώπης.",
        "example_en": "Nicosia is the capital of Cyprus and the last divided capital of Europe.",
        "example2_el": "Η παλιά πόλη της Λευκωσίας περιβάλλεται από τα κυκλικά Ενετικά Τείχη του 16ου αιώνα.",
        "example2_en": "The old city of Nicosia is surrounded by the circular Venetian Walls of the 16th century."
    },
    {
        "id": "CYP-U03-004",
        "greek": "η Λεμεσός",
        "phonetic_hint": "ee leh-meh-SOHS",
        "english": "Limassol",
        "notes": "Second largest urban area in Cyprus, located on the southern coast between the ancient cities of Amathus (Αμαθούντα) and Kourion (Κούριο); hosts Cyprus's largest commercial port.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "accusative_singular": "τη Λεμεσό",
            "genitive_singular": "της Λεμεσού"
        },
        "keg_communicative_function": "Geography — Major cities of Cyprus",
        "example_el": "Η Λεμεσός διαθέτει το μεγαλύτερο εμπορικό λιμάνι της Κύπρου και αποτελεί διεθνές ναυτιλιακό κέντρο.",
        "example_en": "Limassol has the largest commercial port in Cyprus and is an international shipping center.",
        "example2_el": "Στη Λεμεσό διοργανώνονται κάθε χρόνο το μεγάλο Καρναβάλι και η παραδοσιακή Γιορτή του Κρασιού.",
        "example2_en": "In Limassol, the grand Carnival and the traditional Wine Festival are organized every year."
    },
    {
        "id": "CYP-U03-005",
        "greek": "η Λάρνακα",
        "phonetic_hint": "ee LAHR-nah-kah",
        "english": "Larnaca",
        "notes": "Built over ancient Kition (το αρχαίο Κίτιο), birthplace of the Stoic philosopher Zeno (Ζήνωνας ο Κιτιεύς). Home to Cyprus's largest international airport, Finikoudes promenade, Saint Lazarus Church, and the Salt Lake.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "accusative_singular": "τη Λάρνακα",
            "genitive_singular": "της Λάρνακας"
        },
        "keg_communicative_function": "Geography — Major cities of Cyprus",
        "example_el": "Η Λάρνακα είναι χτισμένη στη θέση του αρχαίου βασιλείου του Κιτίου και διαθέτει το μεγαλύτερο αεροδρόμιο της χώρας.",
        "example_en": "Larnaca is built on the site of the ancient kingdom of Kition and has the country's largest airport.",
        "example2_el": "Τον χειμώνα χιλιάδες ροζ φλαμίνγκο φιλοξενούνται στον υγροβιότοπο της Αλυκής Λάρνακας.",
        "example2_en": "In winter, thousands of pink flamingos are hosted at the Larnaca Salt Lake wetland."
    },
    {
        "id": "CYP-U03-006",
        "greek": "η Πάφος",
        "phonetic_hint": "ee PAH-fos",
        "english": "Paphos",
        "notes": "Located in southwestern Cyprus; mythical birthplace of Aphrodite, capital of Cyprus in Hellenistic and Roman times, and European Capital of Culture in 2017 (Πολιτιστική Πρωτεύουσα της Ευρώπης 2017).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "accusative_singular": "την Πάφο",
            "genitive_singular": "της Πάφου"
        },
        "keg_communicative_function": "Geography — Major cities of Cyprus",
        "example_el": "Η Πάφος υπήρξε Πολιτιστική Πρωτεύουσα της Ευρώπης το 2017 και φημίζεται για τα ρωμαϊκά ψηφιδωτά της.",
        "example_en": "Paphos was European Capital of Culture in 2017 and is famous for its Roman mosaics.",
        "example2_el": "Στην επαρχία Πάφου βρίσκεται η Πέτρα του Ρωμιού, η οποία συνδέεται με τον μύθο της γέννησης της θεάς Αφροδίτης.",
        "example2_en": "In the Paphos district lies Petra tou Romiou, which is linked to the myth of the birth of the goddess Aphrodite."
    },
    {
        "id": "CYP-U03-007",
        "greek": "— Σε ποια επαρχία ανήκει η Πόλη Χρυσοχούς; — Στην επαρχία Πάφου.",
        "phonetic_hint": "seh pyah eh-pahr-KHEE-ah ah-NEE-kee ee POH-lee khree-soh-KHOOS? steen eh-pahr-KHEE-ah PAH-foo",
        "english": "— To which district does Polis Chrysochous belong? — To the Paphos district.",
        "notes": "Actual past exam question! Polis Chrysochous (with the fishing port of Latchi / Λατσί and the Baths of Aphrodite) is in the northwestern part of the Paphos district.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — District of Polis Chrysochous",
        "example_el": "Η Πόλη Χρυσοχούς βρίσκεται στα βορειοδυτικά της επαρχίας Πάφου, κοντά στη χερσόνησο του Ακάμα.",
        "example_en": "Polis Chrysochous is located in the northwest of the Paphos district, near the Akamas peninsula.",
        "example2_el": "Κοντά στην Πόλη Χρυσοχούς βρίσκονται το λιμανάκι στο Λατσί και τα Λουτρά της Αφροδίτης.",
        "example2_en": "Near Polis Chrysochous are the small harbor of Latchi and the Baths of Aphrodite."
    },
    {
        "id": "CYP-U03-008",
        "greek": "— Σε ποια επαρχία ανήκουν η Αγία Νάπα, το Παραλίμνι και ο Πρωταράς; — Στην επαρχία Αμμοχώστου.",
        "phonetic_hint": "seh pyah eh-pahr-KHEE-ah ah-NEE-koon ee ah-YEE-ah NAH-pah, toh pah-rah-LEEM-nee keh oh proh-tah-RAHS? steen eh-pahr-KHEE-ah ah-moh-KHOH-stoo",
        "english": "— To which district do Ayia Napa, Paralimni, and Protaras belong? — To the Famagusta district.",
        "notes": "Frequent past exam question! Candidates often mistakenly guess Larnaca because they fly into Larnaca airport; Ayia Napa, Paralimni, Protaras, Deryneia, and Sotira make up the free Famagusta area (ελεύθερη επαρχία Αμμοχώστου).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Free Famagusta District towns",
        "example_el": "Το Παραλίμνι αποτελεί την προσωρινή διοικητική έδρα της ελεύθερης επαρχίας Αμμοχώστου.",
        "example_en": "Paralimni serves as the temporary administrative center of the free Famagusta district.",
        "example2_el": "Το εθνικό δασικό πάρκο του Κάβο Γκρέκο βρίσκεται ανάμεσα στην Αγία Νάπα και τον Πρωταρά στην επαρχία Αμμοχώστου.",
        "example2_en": "The Cape Greco National Forest Park is located between Ayia Napa and Protaras in the Famagusta district."
    },
    {
        "id": "CYP-U03-009",
        "greek": "— Ποια επαρχία της Κύπρου βρίσκεται ολόκληρη υπό τουρκική κατοχή από το 1974; — Η επαρχία Κερύνειας.",
        "phonetic_hint": "pyah eh-pahr-KHEE-ah tees KEE-proo VREE-skeh-teh oh-LOH-klee-ree ee-POH toor-kee-KEE kah-toh-KHEE? ee eh-pahr-KHEE-ah keh-REE-nyahs",
        "english": "— Which district of Cyprus has been entirely under Turkish occupation since 1974? — The Kyrenia district.",
        "notes": "Past exam question! While parts of Nicosia, Famagusta, and Larnaca districts are also occupied, Kyrenia (η Κερύνεια) is the only district that is 100% occupied.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Occupied districts of Cyprus",
        "example_el": "Η επαρχία Κερύνειας είναι η μόνη από τις έξι επαρχίες που είναι εξ ολοκλήρου κατεχόμενη από το 1974.",
        "example_en": "The Kyrenia district is the only one of the six districts that has been wholly occupied since 1974.",
        "example2_el": "Στην πόλη της Κερύνειας βρίσκεται το μεσαιωνικό κάστρο όπου εκτίθεται το αρχαίο καράβι της Κερύνειας.",
        "example2_en": "In the city of Kyrenia stands the medieval castle where the ancient Kyrenia ship is exhibited."
    },
    {
        "id": "CYP-U03-010",
        "greek": "η οροσειρά του Τροόδους",
        "phonetic_hint": "ee oh-roh-see-RAH too troh-OH-thoos",
        "english": "the Troodos mountain range",
        "notes": "Largest mountain range in Cyprus, covering much of the western and central parts of the island; rich in pine forests, copper ore (οφιολιθικό σύμπλεγμα), and UNESCO-listed Byzantine churches.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι οροσειρές",
            "accusative_singular": "την οροσειρά του Τροόδους"
        },
        "keg_communicative_function": "Geography — Mountain ranges of Cyprus",
        "example_el": "Η οροσειρά του Τροόδους είναι ο σημαντικότερος φυσικός πνεύμονας πρασίνου και κύρια πηγή νερού της Κύπρου.",
        "example_en": "The Troodos mountain range is the most important natural green lung and main water source of Cyprus.",
        "example2_el": "Οι κορυφές Μαδαρή και Παπούτσα ανήκουν στην οροσειρά του Τροόδους.",
        "example2_en": "The peaks Madari and Papoutsa belong to the Troodos mountain range."
    },
    {
        "id": "CYP-U03-011",
        "greek": "— Ποια είναι η ψηλότερη κορυφή της Κύπρου; — Ο Όλυμπος (Χιονίστρα) στο Τρόοδος, με ύψος 1.952 μέτρα.",
        "phonetic_hint": "pyah EE-neh ee psee-LOH-teh-ree koh-ree-FEE tees KEE-proo? oh OH-leem-bos (khyoh-NEE-strah) stoh TROH-oh-thos",
        "english": "— What is the highest peak in Cyprus? — Mount Olympus (Chionistra) in Troodos, at 1,952 meters.",
        "notes": "Past exam question! Mount Olympus (also called Chionistra / Χιονίστρα) in the Troodos range reaches 1,952 meters above sea level.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Highest mountain peak of Cyprus",
        "example_el": "Ο Όλυμπος, γνωστός και ως Χιονίστρα, έχει υψόμετρο 1.952 μέτρα και χιονίζεται κάθε χειμώνα.",
        "example_en": "Mount Olympus, also known as Chionistra, has an elevation of 1,952 meters and receives snow every winter.",
        "example2_el": "Ο Πρόδρομος, σε υψόμετρο 1.380 μέτρων στο Τρόοδος, είναι το ψηλότερο κατοικημένο χωριό της Κύπρου.",
        "example2_en": "Prodromos, at an altitude of 1,380 meters in Troodos, is the highest inhabited village in Cyprus."
    },
    {
        "id": "CYP-U03-012",
        "greek": "η οροσειρά του Πενταδακτύλου",
        "phonetic_hint": "ee oh-roh-see-RAH too pehn-dah-thahk-TEE-loo",
        "english": "the Pentadaktylos (Kyrenia) mountain range",
        "notes": "Past exam question often asks to distinguish Pentadaktylos peaks/castles (Κυπαρισσόβουνο 1.024 μ., Άγιος Ιλαρίωνας, Βουφαβέντο, Καντάρα) from Troodos peaks (Όλυμπος, Μαδαρή, Παπούτσα).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι οροσειρές",
            "accusative_singular": "την οροσειρά του Πενταδακτύλου"
        },
        "keg_communicative_function": "Geography — Mountain ranges & castles of Cyprus",
        "example_el": "Στην οροσειρά του Πενταδακτύλου βρίσκονται τα τρία βυζαντινά κάστρα: του Αγίου Ιλαρίωνα, του Βουφαβέντο και της Καντάρας.",
        "example_en": "In the Pentadaktylos range stand the three Byzantine castles: Saint Hilarion, Buffavento, and Kantara.",
        "example2_el": "Η ψηλότερη κορυφή του Πενταδακτύλου είναι το Κυπαρισσόβουνο με ύψος 1.024 μέτρα.",
        "example2_en": "The highest peak of Pentadaktylos is Kyparissovouno with a height of 1,024 meters."
    },
    {
        "id": "CYP-U03-013",
        "greek": "η πεδιάδα της Μεσαορίας",
        "phonetic_hint": "ee peh-thee-AH-thah tees meh-sah-oh-REE-ahs",
        "english": "the Mesaoria plain",
        "notes": "Meaning 'between the mountains' (μεταξύ των ορέων): the central agricultural plain stretching across the island from Morphou Bay in the west to Famagusta Bay in the east, between Troodos and Pentadaktylos.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι πεδιάδες",
            "accusative_singular": "την πεδιάδα της Μεσαορίας"
        },
        "keg_communicative_function": "Geography — Plains and agriculture",
        "example_el": "Η πεδιάδα της Μεσαορίας εκτείνεται ανάμεσα στην οροσειρά του Τροόδους και την οροσειρά του Πενταδακτύλου.",
        "example_en": "The Mesaoria plain stretches between the Troodos mountain range and the Pentadaktylos mountain range.",
        "example2_el": "Η Μεσαορία αποτελεί τον κύριο σιτοβολώνα της Κύπρου, όπου καλλιεργούνται δημητριακά και πατάτες.",
        "example2_en": "Mesaoria is the main breadbasket of Cyprus, where cereals and potatoes are cultivated."
    },
    {
        "id": "CYP-U03-014",
        "greek": "— Ποιος είναι ο μεγαλύτερος ποταμός της Κύπρου; — Ο Πεδιαίος (ή Πηδιάς).",
        "phonetic_hint": "pyos EE-neh oh meh-ghah-LEE-teh-ros poh-tah-MOHS tees KEE-proo? oh peh-thee-EH-os (ee pee-THYAHS)",
        "english": "— Which is the longest river in Cyprus? — The Pedieos (or Pidias) river.",
        "notes": "Past exam question! The Pedieos river originates in Troodos near Machairas Monastery, flows through Nicosia and the Mesaoria plain, and empties into Famagusta Bay (~100 km long).",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Longest river in Cyprus",
        "example_el": "Ο Πεδιαίος ποταμός έχει μήκος περίπου 100 χιλιόμετρα, πηγάζει από το Τρόοδος και διασχίζει τη Λευκωσία.",
        "example_en": "The Pedieos river is about 100 kilometers long, originates in Troodos, and flows through Nicosia.",
        "example2_el": "Όλοι οι ποταμοί της Κύπρου είναι χείμαρροι που τροφοδοτούνται από τις βροχές του χειμώνα και το λιώσιμο του χιονιού.",
        "example2_en": "All rivers in Cyprus are seasonal streams fed by winter rains and melting snow."
    },
    {
        "id": "CYP-U03-015",
        "greek": "— Ποιο είναι το μεγαλύτερο φράγμα της Κύπρου; — Το φράγμα του Κούρη στην επαρχία Λεμεσού.",
        "phonetic_hint": "pyoh EE-neh toh meh-ghah-LEE-teh-roh FRAHGH-mah tees KEE-proo? toh FRAHGH-mah too KOO-ree steen eh-pahr-KHEE-ah leh-meh-SOO",
        "english": "— Which is the largest dam/reservoir in Cyprus? — The Kouris Dam in the Limassol district.",
        "notes": "Past exam question! Completed in 1988 with a capacity of 115 million cubic meters; the old village of Alassa was submerged and its Church of Saint Nicholas roof can be seen when water levels drop.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Largest dam in Cyprus",
        "example_el": "Το φράγμα του Κούρη στην επαρχία Λεμεσού έχει χωρητικότητα 115 εκατομμύρια κυβικά μέτρα νερού.",
        "example_en": "The Kouris Dam in the Limassol district has a capacity of 115 million cubic meters of water.",
        "example2_el": "Άλλα μεγάλα φράγματα της Κύπρου είναι του Ασπρόκρεμμου στην Πάφο και της Ευρέτου στην Πόλη Χρυσοχούς.",
        "example2_en": "Other large dams in Cyprus are Asprokremmos in Paphos and Evretou in Polis Chrysochous."
    },
    {
        "id": "CYP-U03-016",
        "greek": "η χερσόνησος του Ακάμα",
        "phonetic_hint": "ee kher-SOH-nee-sos too ah-KAH-mah",
        "english": "the Akamas Peninsula",
        "notes": "Protected national forest park at the northwestern tip of Cyprus (Paphos district), famous for the Avakas Gorge (Φαράγγι του Άβακα), Blue Lagoon, and Lara Beach turtle nesting ground.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι χερσόνησοι",
            "accusative_singular": "τη χερσόνησο του Ακάμα"
        },
        "keg_communicative_function": "Geography — Peninsulas & natural parks",
        "example_el": "Η χερσόνησος του Ακάμα στην επαρχία Πάφου είναι προστατευόμενος βιότοπος με σπάνια χλωρίδα και πανίδα.",
        "example_en": "The Akamas Peninsula in the Paphos district is a protected habitat with rare flora and fauna.",
        "example2_el": "Στην παραλία της Λάρας στον Ακάμα γεννούν τα αυγά τους οι προστατευόμενες θαλάσσιες χελώνες Καρέτα-Καρέτα και Πράσινη Χελώνα.",
        "example2_en": "On Lara Beach in Akamas, the protected Loggerhead (Caretta caretta) and Green sea turtles lay their eggs."
    },
    {
        "id": "CYP-U03-017",
        "greek": "η χερσόνησος της Καρπασίας",
        "phonetic_hint": "ee kher-SOH-nee-sos tees kahr-pah-SEE-ahs",
        "english": "the Karpasia (Karpass) Peninsula",
        "notes": "Long narrow peninsula in the northeastern tip of Cyprus (Famagusta district), ending at Cape Apostolos Andreas (το Ακρωτήριο του Αποστόλου Ανδρέα). Occupied since August 1974.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι χερσόνησοι",
            "accusative_singular": "τη χερσόνησο της Καρπασίας"
        },
        "keg_communicative_function": "Geography — Peninsulas of Cyprus",
        "example_el": "Στο βορειοανατολικό άκρο της χερσονήσου της Καρπασίας βρίσκεται το Μοναστήρι του Αποστόλου Ανδρέα.",
        "example_en": "At the northeastern tip of the Karpasia peninsula lies the Apostolos Andreas Monastery.",
        "example2_el": "Στην Καρπασία ζουν ελεύθερα τα άγρια γαϊδουράκια και βρίσκονται τα χωριά των Ελληνοκυπρίων εγκλωβισμένων.",
        "example2_en": "In Karpasia, wild donkeys live freely and the villages of the enclaved Greek Cypriots are located."
    },
    {
        "id": "CYP-U03-018",
        "greek": "το κυπριακό αγρινό",
        "phonetic_hint": "toh kee-pree-ah-KOH ah-ghree-NOH",
        "english": "the Cyprus mouflon (wild sheep)",
        "notes": "Endemic wild sheep subspecies (Ovis orientalis ophion) living in the Paphos Forest (το Δάσος της Πάφου / Κοιλάδα των Κέδρων). National animal symbol featured on Cyprus euro coins (1, 2, and 5 cent coins) and Cyprus Airways.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα κυπριακά αγρινά",
            "accusative_singular": "το κυπριακό αγρινό",
            "genitive_singular": "του κυπριακού αγρινού"
        },
        "keg_communicative_function": "Geography & Nature — Endemic fauna of Cyprus",
        "example_el": "Ποιο είναι το μεγαλύτερο ενδημικό άγριο θηλαστικό της Κύπρου και εθνικό της σύμβολο; Το κυπριακό αγρινό.",
        "example_en": "Which is the largest endemic wild mammal of Cyprus and its national symbol? The Cyprus mouflon.",
        "example2_el": "Το αγρινό ζει προστατευμένο στο Δάσος της Πάφου και απεικονίζεται στα κυπριακά κέρματα του ευρώ.",
        "example2_en": "The mouflon lives protected in the Paphos Forest and is depicted on Cypriot euro coins."
    },
    {
        "id": "CYP-U03-019",
        "greek": "η λατζιά (η χρυσή δρυς της Κύπρου)",
        "phonetic_hint": "ee lah-TZAH (ee khree-SEE threes tees KEE-proo)",
        "english": "the golden oak of Cyprus (national tree)",
        "notes": "Endemic evergreen oak species (Quercus alnifolia) growing exclusively in the Troodos mountains; designated in 2006 as the National Tree of Cyprus (το εθνικό δέντρο της Κύπρου).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι λατζιές",
            "accusative_singular": "τη λατζιά"
        },
        "keg_communicative_function": "Geography & Nature — Endemic flora of Cyprus",
        "example_el": "Ποιο είναι το εθνικό δέντρο της Κύπρου που φύεται αποκλειστικά στην οροσειρά του Τροόδους; Η λατζιά.",
        "example_en": "What is the national tree of Cyprus that grows exclusively in the Troodos mountain range? The golden oak (latzia).",
        "example2_el": "Εκτός από τη λατζιά, στην Κοιλάδα των Κέδρων στο Δάσος της Πάφου φύεται ο ενδημικός κυπριακός κέδρος.",
        "example2_en": "Besides the golden oak, the endemic Cyprus cedar grows in Cedar Valley in the Paphos Forest."
    },
    {
        "id": "CYP-U03-020",
        "greek": "οι αλυκές (Λάρνακας και Ακρωτηρίου)",
        "phonetic_hint": "ee ah-lee-KEHS (LAHR-nah-kahs keh ah-kroh-tee-REE-oo)",
        "english": "the Salt Lakes (of Larnaca and Akrotiri)",
        "notes": "Major Ramsar-protected wetlands in Cyprus where migratory birds, especially greater flamingos (τα φλαμίνγκο), spend the winter months.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "singular": "η αλυκή",
            "plural": "οι αλυκές",
            "accusative_plural": "τις αλυκές"
        },
        "keg_communicative_function": "Geography & Nature — Wetlands of Cyprus",
        "example_el": "Οι δύο σημαντικότεροι υγροβιότοποι της Κύπρου είναι η Αλυκή Λάρνακας και η Αλυκή Ακρωτηρίου στη Λεμεσό.",
        "example_en": "The two most important wetlands of Cyprus are the Larnaca Salt Lake and the Akrotiri Salt Lake in Limassol.",
        "example2_el": "Το καλοκαίρι το νερό στις αλυκές εξατμίζεται, αφήνοντας ένα παχύ στρώμα αλατιού.",
        "example2_en": "In summer, the water in the salt lakes evaporates, leaving a thick layer of salt."
    },
    {
        "id": "CYP-U03-021",
        "greek": "το μεσογειακό κλίμα",
        "phonetic_hint": "toh meh-soh-yee-ah-KOH KLEE-mah",
        "english": "the Mediterranean climate",
        "notes": "Cyprus has a warm Mediterranean climate with over 300 days of sunshine per year, hot dry summers (May–October) and mild rainy winters (November–March).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα μεσογειακά κλίματα",
            "accusative_singular": "το μεσογειακό κλίμα"
        },
        "keg_communicative_function": "Geography — Climate of Cyprus",
        "example_el": "Η Κύπρος έχει μεσογειακό κλίμα με θερμά, ξηρά καλοκαίρια και ήπιους χειμώνες.",
        "example_en": "Cyprus has a Mediterranean climate with hot, dry summers and mild winters.",
        "example2_el": "Το νησί απολαμβάνει περισσότερες από τριακόσιες (300) ημέρες ηλιοφάνειας τον χρόνο.",
        "example2_en": "The island enjoys more than three hundred (300) days of sunshine a year."
    },
    {
        "id": "CYP-U03-022",
        "greek": "τα Κρασοχώρια της Λεμεσού (π.χ. το Όμοδος)",
        "phonetic_hint": "tah krah-soh-KHOH-ryah tees leh-meh-SOO (toh OH-moh-thos)",
        "english": "the Wine Villages of Limassol (e.g., Omodos)",
        "notes": "Past exam question on famous Cypriot villages! Omodos (το Όμοδος, famous for Timios Stavros Monastery and wine), Arsos, Vouni, and Koilani are in the Limassol district.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Κρασοχώρια",
            "accusative_plural": "τα Κρασοχώρια"
        },
        "keg_communicative_function": "Geography — Traditional villages of Cyprus",
        "example_el": "Σε ποια επαρχία βρίσκεται το γραφικό κρασοχώρι Όμοδος με το Μοναστήρι του Τιμίου Σταυρού; Στην επαρχία Λεμεσού.",
        "example_en": "In which district is the picturesque wine village of Omodos with the Monastery of the Holy Cross located? In the Limassol district.",
        "example2_el": "Στην επαρχία Λεμεσού βρίσκονται επίσης τα ορεινά θέρετρα Πλάτρες και Αγρός, καθώς και το παραλιακό Πισσούρι.",
        "example2_en": "Also located in the Limassol district are the mountain resorts of Platres and Agros, as well as coastal Pissouri."
    },
    {
        "id": "CYP-U03-023",
        "greek": "τα Λεύκαρα (επαρχία Λάρνακας)",
        "phonetic_hint": "tah LEHF-kah-rah (eh-pahr-KHEE-ah LAHR-nah-kahs)",
        "english": "Lefkara village (Larnaca district)",
        "notes": "Famous mountain village in the Larnaca district, renowned worldwide for traditional Lefkara lace embroidery (τα λευκαρίτικα κεντήματα) and filigree silversmithing (η αργυροχοΐα).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Λεύκαρα",
            "accusative_plural": "τα Λεύκαρα",
            "genitive_plural": "των Λευκάρων"
        },
        "keg_communicative_function": "Geography & Culture — Villages of Larnaca district",
        "example_el": "Σε ποια επαρχία βρίσκονται τα Λεύκαρα, που φημίζονται για τα κεντήματα και την αργυροχοΐα τους; Στην επαρχία Λάρνακας.",
        "example_en": "In which district is Lefkara, famous for its embroidery and silversmithing, located? In the Larnaca district.",
        "example2_el": "Σύμφωνα με την παράδοση, ο Λεονάρντο ντα Βίντσι επισκέφθηκε τα Λεύκαρα το 1481 και αγόρασε κέντημα για τον καθεδρικό ναό του Μιλάνου.",
        "example2_en": "According to tradition, Leonardo da Vinci visited Lefkara in 1481 and bought embroidery for the Milan Cathedral."
    },
    {
        "id": "CYP-U03-024",
        "greek": "η Κακοπετριά και το Φικάρδου (επαρχία Λευκωσίας)",
        "phonetic_hint": "ee kah-koh-peh-tree-AH keh toh fee-KAHR-thoo",
        "english": "Kakopetria and Fikardou villages (Nicosia district)",
        "notes": "Past exam village questions! Kakopetria (in the Solea valley) and the medieval preserved stone village of Fikardou (winner of the Europa Nostra award) are in the Nicosia district.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "accusative_singular": "την Κακοπετριά"
        },
        "keg_communicative_function": "Geography — Mountain villages of Nicosia district",
        "example_el": "Το παραδοσιακό χωριό Φικάρδου και η Κακοπετριά στην κοιλάδα της Σολέας ανήκουν στην επαρχία Λευκωσίας.",
        "example_en": "The traditional village of Fikardou and Kakopetria in the Solea valley belong to the Nicosia district.",
        "example2_el": "Ολόκληρο το χωριό Φικάρδου έχει κηρυχθεί αρχαίο μνημείο και έχει τιμηθεί με το βραβείο Europa Nostra.",
        "example2_en": "The entire village of Fikardou has been declared an ancient monument and honored with the Europa Nostra award."
    },
    {
        "id": "CYP-U03-025",
        "greek": "τα Κοκκινοχώρια",
        "phonetic_hint": "tah koh-kee-noh-KHOH-ryah",
        "english": "the Kokkinochoria ('Red Soil Villages')",
        "notes": "Group of villages in southeastern Cyprus (spanning the Famagusta and Larnaca districts, such as Xylofagou, Liopetri, Frenaros, Avgorou, Deryneia) famous for their fertile mineral-rich red soil and Cyprus potato cultivation (η κυπριακή πατάτα).",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Κοκκινοχώρια",
            "accusative_plural": "τα Κοκκινοχώρια"
        },
        "keg_communicative_function": "Geography & Agriculture — Regions of Cyprus",
        "example_el": "Τα Κοκκινοχώρια στη νοτιοανατολική Κύπρο ονομάζονται έτσι από το εύφορο κόκκινο χώμα τους.",
        "example_en": "The Kokkinochoria in southeastern Cyprus are named after their fertile red soil.",
        "example2_el": "Η περιοχή των Κοκκινοχωρίων φημίζεται ιδιαίτερα για την παραγωγή της κυπριακής πατάτας και του κολοκασιού.",
        "example2_en": "The Kokkinochoria region is particularly famous for the production of Cyprus potatoes and taro (kolokasi)."
    },
    {
        "id": "CYP-U03-026",
        "greek": "η Μόρφου",
        "phonetic_hint": "ee MOR-foo",
        "english": "Morphou",
        "notes": "Major town in northwestern Cyprus (in the Nicosia district), famous for its citrus groves (πορτοκάλια της Μόρφου) and the Church of Saint Mamas (ο Άγιος Μάμας). Occupied by Turkish forces since August 1974.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "accusative_singular": "τη Μόρφου",
            "genitive_singular": "της Μόρφου"
        },
        "keg_communicative_function": "Geography — Occupied towns of Nicosia district",
        "example_el": "Η κωμόπολη της Μόρφου ανήκει διοικητικά στην επαρχία Λευκωσίας και βρίσκεται υπό τουρκική κατοχή από το 1974.",
        "example_en": "The town of Morphou belongs administratively to the Nicosia district and has been under Turkish occupation since 1974.",
        "example2_el": "Η Μόρφου είναι γνωστή για τα εσπεριδοειδή της και τον βυζαντινό ναό του Αγίου Μάμαντος.",
        "example2_en": "Morphou is known for its citrus fruits and the Byzantine church of Saint Mamas."
    },
    {
        "id": "CYP-U03-027",
        "greek": "ο χαλκός (το μέταλλο της Κύπρου)",
        "phonetic_hint": "oh khahl-KOHS (toh MEH-tah-loh tees KEE-proo)",
        "english": "copper (the metal linked to the name of Cyprus)",
        "notes": "Since antiquity, Cyprus was famous across the Mediterranean for its rich copper mines (π.χ. Σκουριώτισσα, Ταμασός); the Latin word for copper (aes Cyprium -> cuprum) derives from Cyprus.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "accusative_singular": "τον χαλκό",
            "genitive_singular": "του χαλκού"
        },
        "keg_communicative_function": "Geography & History — Copper heritage of Cyprus",
        "example_el": "Ποιο μέταλλο συνδέθηκε ιστορικά με το όνομα και τον πλούτο της Κύπρου από την αρχαιότητα; Ο χαλκός.",
        "example_en": "Which metal has been historically linked with the name and wealth of Cyprus since antiquity? Copper.",
        "example2_el": "Το χρώμα του χάρτη στη σημαία της Κυπριακής Δημοκρατίας συμβολίζει τα πλούσια κοιτάσματα χαλκού του νησιού.",
        "example2_en": "The color of the map on the flag of the Republic of Cyprus symbolizes the island's rich copper deposits."
    },
    {
        "id": "CYP-U03-028",
        "greek": "η Πέτρα του Ρωμιού",
        "phonetic_hint": "ee PEH-trah too roh-MYOO",
        "english": "Petra tou Romiou (Aphrodite's Rock)",
        "notes": "Famous sea stack on the coast between Paphos and Limassol (near Kouklia / Palaipafos). Associated with both the mythical birth of Aphrodite from the sea foam and the Byzantine border warrior Digenis Akritas ('ο Ρωμιός').",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "accusative_singular": "την Πέτρα του Ρωμιού",
            "genitive_singular": "της Πέτρας του Ρωμιού"
        },
        "keg_communicative_function": "Geography & Mythology — Coastal landmarks",
        "example_el": "Η Πέτρα του Ρωμιού βρίσκεται στην ακτή της επαρχίας Πάφου και συνδέεται με τον μύθο της Αφροδίτης και τον Διγενή Ακρίτα.",
        "example_en": "Petra tou Romiou is located on the coast of the Paphos district and is linked with the myth of Aphrodite and Digenis Akritas.",
        "example2_el": "Λόγω της λατρείας της Αφροδίτης στην αρχαιότητα, η Κύπρος ονομάζεται συχνά «το νησί της Αφροδίτης».",
        "example2_en": "Because of the worship of Aphrodite in antiquity, Cyprus is often called 'the island of Aphrodite'."
    },
    {
        "id": "CYP-U03-029",
        "greek": "το Κάβο Γκρέκο (το Ακρωτήριο Πηδάλιο)",
        "phonetic_hint": "toh KAH-voh GREH-koh (toh ah-kroh-TEE-ree-oh pee-THAH-lee-oh)",
        "english": "Cape Greco (southeastern cape of Cyprus)",
        "notes": "Protected National Forest Park (Εθνικό Δασικό Πάρκο) at the southeastern tip of Cyprus between Ayia Napa and Protaras in the free Famagusta district.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "accusative_singular": "το Κάβο Γκρέκο"
        },
        "keg_communicative_function": "Geography — Capes and National Forest Parks",
        "example_el": "Το Κάβο Γκρέκο βρίσκεται στο νοτιοανατολικό άκρο της Κύπρου, ανάμεσα στην Αγία Νάπα και τον Πρωταρά.",
        "example_en": "Cape Greco is located at the southeastern tip of Cyprus, between Ayia Napa and Protaras.",
        "example2_el": "Η περιοχή είναι κηρυγμένο Εθνικό Δασικό Πάρκο, γνωστό για τις θαλασσινές σπηλιές και τα κρυστάλλινα νερά της.",
        "example2_en": "The area is a designated National Forest Park, known for its sea caves and crystal-clear waters."
    },
    {
        "id": "CYP-U03-030",
        "greek": "— Ποιες χώρες βρίσκονται γεωγραφικά πιο κοντά στην Κύπρο; — Η Τουρκία, η Συρία, ο Λίβανος, το Ισραήλ, η Αίγυπτος και η Ελλάδα.",
        "phonetic_hint": "pyehs KHOH-rehs VREE-skohn-deh yeh-oh-ghrah-fee-KAH pyoh kohn-DAH steen KEE-proh? ee toor-KEE-ah, ee see-REE-ah, oh LEE-vah-nos, toh ee-srah-EEL, ee EH-yeep-tos keh ee eh-LAH-thah",
        "english": "— Which countries are geographically closest to Cyprus? — Turkey, Syria, Lebanon, Israel, Egypt, and Greece.",
        "notes": "Past exam geography question! Turkey lies ~75 km to the north, Syria and Lebanon ~105–180 km to the east, Israel and Egypt to the south/southeast, and the Greek island of Kastellorizo / Rhodes to the west.",
        "gender_or_pos": "phrase",
        "grammatical_info": {
            "part_of_speech": "phrase"
        },
        "keg_communicative_function": "Past Exam Q&A — Neighboring countries in the Eastern Mediterranean",
        "example_el": "Ανατολικά της Κύπρου βρίσκονται η Συρία και ο Λίβανος, ενώ νότια βρίσκονται η Αίγυπτος και το Ισραήλ.",
        "example_en": "East of Cyprus lie Syria and Lebanon, while to the south lie Egypt and Israel.",
        "example2_el": "Το ελληνικό νησί που βρίσκεται γεωγραφικά πιο κοντά στην Κύπρο είναι το Καστελλόριζο (Μεγίστη).",
        "example2_en": "The Greek island located geographically closest to Cyprus is Kastellorizo (Megisti)."
    }
]


def normalize_card(card: dict) -> dict:
    out = {}
    for k, v in card.items():
        if isinstance(v, str):
            out[k] = unicodedata.normalize("NFC", v.strip())
        else:
            out[k] = v
    out["audio"] = None
    out["status"] = "pending_tts"
    return out


def write_unit(unit_id: str, title: str, description: str, notes: str, cards: list):
    unit_dir = CONTENT_DIR / unit_id
    unit_dir.mkdir(parents=True, exist_ok=True)
    lesson_path = unit_dir / "lesson-01.yaml"

    normalized_cards = [normalize_card(c) for c in cards]
    lesson_data = {
        "unit_id": unit_id,
        "lesson_id": "lesson-01",
        "title": unicodedata.normalize("NFC", title),
        "description": unicodedata.normalize("NFC", description),
        "lesson_status": "not_started",
        "lesson_notes": unicodedata.normalize("NFC", notes),
        "entries": normalized_cards,
    }

    with open(lesson_path, "w", encoding="utf-8") as f:
        yaml.dump(lesson_data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"[OK] Wrote {lesson_path} ({len(normalized_cards)} cards)")


def main():
    write_unit(
        unit_id="unit-cyp-01",
        title="Μάθημα 1: Πολίτευμα, Θεσμοί & Κράτος της Κύπρου (Polity, State Institutions & Governance)",
        description="Constitutional regime of the Republic of Cyprus (Presidential Republic), separation of powers, the President and Council of Ministers, the House of Representatives (56+24 seats & 3 religious groups), independent officials, national symbols, and political parties.",
        notes=NOTES_CYP_01,
        cards=CARDS_CYP_01,
    )
    write_unit(
        unit_id="unit-cyp-02",
        title="Μάθημα 2: Σύγχρονη Ιστορία της Κύπρου 1955–Σήμερα (Modern History of Cyprus)",
        description="The 1955–1959 EOKA liberation struggle, Zurich-London Agreements, proclamation of independence (1960), chronological succession of Presidents of the Republic, the 1974 coup and Turkish invasion, the Green Line, the 2004 Annan Plan referendum, and EU accession.",
        notes=NOTES_CYP_02,
        cards=CARDS_CYP_02,
    )
    write_unit(
        unit_id="unit-cyp-03",
        title="Μάθημα 3: Γεωγραφία, Επαρχίες, Πόλεις & Φύση της Κύπρου (Geography, Districts, Cities & Nature)",
        description="Geographical position in the northeastern Mediterranean, the 6 administrative districts, major cities and traditional villages (Omodos, Lefkara, Kakopetria, Fikardou), Troodos and Pentadaktylos mountain ranges, Pedieos river, Kouris dam, and endemic flora and fauna (mouflon, golden oak).",
        notes=NOTES_CYP_03,
        cards=CARDS_CYP_03,
    )


if __name__ == "__main__":
    main()

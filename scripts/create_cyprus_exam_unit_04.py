# -*- coding: utf-8 -*-
"""
Generate Cyprus Culture and Political/Social Reality Exam Curriculum — Unit 4:
- unit-cyp-04 (CYP-04-A): Πολιτισμός, Παράδοση, Ήθη, Έθιμα & Προϊόντα (Culture, Traditions & Products) - 30 cards
"""
import sys
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from scripts.create_cyprus_exam_batch_1 import write_unit

NOTES_CYP_04 = """Unit CYP-04 Core Exam Notes: Πολιτισμός, Παράδοση, Ήθη, Έθιμα & Προϊόντα (Culture, Traditions, Customs & Products)

• Μνημεία Παγκόσμιας Κληρονομιάς της UNESCO στην Κύπρο:
  1. Η Πάφος (Νέα Πάφος, Τάφοι των Βασιλέων & Παλαίπαφος στα Κούκλια) — από το 1980.
  2. Οι δέκα Τοιχογραφημένοι Βυζαντινοί Ναοί στην περιοχή του Τροόδους — από το 1985.
  3. Ο Νεολιθικός Οικισμός της Χοιροκοιτίας (επαρχία Λάρνακας) — από το 1998.
• Άυλη Πολιτιστική Κληρονομιά της UNESCO:
  - Τα Λευκαρίτικα κεντήματα (2009), τα Τσιαττιστά — ποιητικοί αυτοσχεδιασμοί (2011), η Μεσογειακή Διατροφή, η τέχνη της ξερολιθιάς, η Βυζαντινή Ψαλτική.

• Παραδοσιακά Προϊόντα (ΠΟΠ / ΠΓΕ) & Γαστρονομία:
  - Το χαλλούμι (ΠΟΠ από το 2021): Παραδοσιακό τυρί από αιγοπρόβειο (και αγελαδινό) γάλα με δυόσμο.
  - Η κουμανδαρία: Γλυκό κρασί από λιαστές λευκές (Ξυνιστέρι) και μαύρες (Μαύρο) σταφυλές στα Κουμανδαροχώρια του Τροόδους· το αρχαιότερο ονομαστό κρασί στον κόσμο.
  - Η ζιβανία (παραδοσιακό απόσταγμα σταφυλιών), το χαρουπόμελο («ο μαύρος χρυσός της Κύπρου»), ο παλουζές και ο σουτζιούκος, η φλαούνα (πασχαλινό έδεσμα), η σεφταλιά, το οφτό κλέφτικο, τα κουπέπια, το λουκούμι Γεροσκήπου (ΠΓΕ).

• Μεγάλες Γιορτές, Έθιμα & Θρησκεία:
  - Ο Κατακλυσμός (Δευτέρα του Αγίου Πνεύματος, ιδιαίτερα στη Λάρνακα), το Καρναβάλι Λεμεσού, η Γιορτή του Κρασιού στη Λεμεσό, τα Ανθεστήρια (Μάιος), η Λαμπρατζιά το Πάσχα.
  - Η Αυτοκέφαλη Εκκλησία της Κύπρου: Ιδρύθηκε το 45 μ.Χ. από τους Αποστόλους Βαρνάβα και Παύλο. Προκαθήμενος: Αρχιεπίσκοπος Νέας Ιουστινιανής και πάσης Κύπρου Γεώργιος."""

CARDS_CYP_04 = [
    {
        "id": "CYP-U04-001",
        "greek": "το χαλλούμι (προϊόν ΠΟΠ)",
        "phonetic_hint": "toh khah-LOO-mee (proh-ee-OHN POHP)",
        "english": "halloumi cheese (PDO product)",
        "notes": "Cyprus's most famous traditional dairy product, registered as a Protected Designation of Origin (Προστατευόμενη Ονομασία Προέλευσης - ΠΟΠ) in the European Union in 2021.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα χαλλούμια",
            "accusative_singular": "το χαλλούμι",
            "genitive_singular": "του χαλλουμιού"
        },
        "keg_communicative_function": "Culture & Products — Protected traditional products",
        "example_el": "Το χαλλούμι είναι το παραδοσιακό τυρί της Κύπρου και έχει κατοχυρωθεί ως προϊόν ΠΟΠ στην Ευρωπαϊκή Ένωση.",
        "example_en": "Halloumi is the traditional cheese of Cyprus and has been registered as a PDO product in the European Union.",
        "example2_el": "Κατά την παρασκευή του χαλλουμιού προστίθεται φρέσκος ή ξηρός δυόσμος.",
        "example2_en": "During the preparation of halloumi, fresh or dried mint is added."
    },
    {
        "id": "CYP-U04-002",
        "greek": "— Ποιο είναι το φημισμένο παραδοσιακό γλυκό κρασί της Κύπρου; — Η Κουμανδαρία.",
        "phonetic_hint": "pyoh EE-neh toh fee-meez-MEH-noh pah-rah-thoh-see-ah-KOH ghlee-KOH krah-SEE tees KEE-proo? ee koo-mahn-dah-REE-ah",
        "english": "— What is the famous traditional sweet wine of Cyprus? — Commandaria.",
        "notes": "Frequent past exam question! Commandaria took its name in the 12th century from the Knights Hospitaller 'Grande Commanderie' at Kolossi Castle in Limassol.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Past Exam Q&A — Traditional Cypriot wine",
        "example_el": "Η κουμανδαρία παράγεται από λιαστά σταφύλια στα χωριά της οροσειράς του Τροόδους.",
        "example_en": "Commandaria is produced from sun-dried grapes in the villages of the Troodos mountain range.",
        "example2_el": "Είναι το αρχαιότερο ονομαστό κρασί στον κόσμο που παραμένει σε συνεχή παραγωγή.",
        "example2_en": "It is the oldest named wine in the world that remains in continuous production."
    },
    {
        "id": "CYP-U04-003",
        "greek": "τα λευκαρίτικα κεντήματα",
        "phonetic_hint": "tah lef-kah-REE-tee-kah kehn-DEE-mah-tah",
        "english": "Lefkara lace / embroidery",
        "notes": "Past exam question! Handwritten linen embroidery from the village of Lefkara (Larnaca district), inscribed on the UNESCO Intangible Cultural Heritage list in 2009.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "singular": "το λευκαρίτικο κέντημα",
            "plural": "τα λευκαρίτικα κεντήματα",
            "accusative_plural": "τα λευκαρίτικα κεντήματα"
        },
        "keg_communicative_function": "Culture & Products — UNESCO Intangible Heritage",
        "example_el": "Τα λευκαρίτικα κεντήματα έχουν εγγραφεί στον κατάλογο της Άυλης Πολιτιστικής Κληρονομιάς της UNESCO.",
        "example_en": "Lefkara embroideries have been inscribed on the UNESCO Intangible Cultural Heritage list.",
        "example2_el": "Εκτός από το κέντημα, τα Λεύκαρα φημίζονται και για την παραδοσιακή τέχνη της αργυροχοΐας.",
        "example2_en": "Besides embroidery, Lefkara is also famous for the traditional art of silversmithing."
    },
    {
        "id": "CYP-U04-004",
        "greek": "η ζιβανία",
        "phonetic_hint": "ee zee-vah-NEE-ah",
        "english": "zivania (traditional Cypriot pomace brandy)",
        "notes": "Traditional Cypriot alcoholic spirit distilled from grape pomace (τα στέμφυλα / τζίβανα) and local dry wine. Protected Geographical Indication (ΠΓΕ).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι ζιβανίες",
            "accusative_singular": "τη ζιβανία"
        },
        "keg_communicative_function": "Culture & Products — Traditional spirits",
        "example_el": "Η ζιβανία είναι το παραδοσιακό αλκοολούχο απόσταγμα από στέμφυλα σταφυλιών της Κύπρου.",
        "example_en": "Zivania is the traditional alcoholic spirit made from grape pomace in Cyprus.",
        "example2_el": "Στην Ιερά Μονή Κύκκου παρασκευάζεται και η γνωστή κόκκινη ζιβανία με βότανα και κανέλα.",
        "example2_en": "At Kykkos Monastery, the well-known red zivania with herbs and cinnamon is also produced."
    },
    {
        "id": "CYP-U04-005",
        "greek": "η φλαούνα",
        "phonetic_hint": "ee flah-OO-nah",
        "english": "flaouna (traditional Cypriot Easter cheese pastry)",
        "notes": "Savory-sweet pastry filled with special cheese, eggs, raisins, mint, and mahleb (μαχλέπι), baked in every Cypriot household on Holy Thursday/Saturday for Easter Sunday.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι φλαούνες",
            "accusative_singular": "τη φλαούνα"
        },
        "keg_communicative_function": "Culture & Customs — Easter culinary traditions",
        "example_el": "Ποιο είναι το κατεξοχήν παραδοσιακό έδεσμα που ζυμώνουν στην Κύπρο το Πάσχα; Η φλαούνα.",
        "example_en": "What is the quintessential traditional pastry baked in Cyprus at Easter? The flaouna.",
        "example2_el": "Οι φλαούνες αλείφονται με αυγό και πασπαλίζονται με σουσάμι πριν ψηθούν στον φούρνο.",
        "example2_en": "Flaounes are brushed with egg and sprinkled with sesame seeds before being baked in the oven."
    },
    {
        "id": "CYP-U04-006",
        "greek": "ο σουτζιούκος και ο παλουζές",
        "phonetic_hint": "oh soo-TZYOO-kos keh oh pah-loo-ZEHS",
        "english": "soutzioukos and palouzes (traditional grape-must sweets)",
        "notes": "Made in autumn during the grape harvest (ο τρύγος) in the wine villages: palouzes is thick grape-must pudding, and soutzioukos is made by dipping strings of almonds/walnuts into palouzes.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι σουτζιούκοι",
            "accusative_singular": "τον σουτζιούκο"
        },
        "keg_communicative_function": "Culture & Products — Grape harvest delicacies",
        "example_el": "Ο παλουζές και ο σουτζιούκος παρασκευάζονται το φθινόπωρο από μούστο σταφυλιού στα κρασοχώρια.",
        "example_en": "Palouzes and soutzioukos are prepared in autumn from grape must in the wine villages.",
        "example2_el": "Για την παρασκευή του σουτζιούκου βουτούν κλωστές με αμύγδαλα ή καρύδια μέσα στον ζεστό παλουζέ.",
        "example2_en": "To make soutzioukos, strings of almonds or walnuts are dipped into warm palouzes."
    },
    {
        "id": "CYP-U04-007",
        "greek": "το χαρουπόμελο (ο «μαύρος χρυσός» της Κύπρου)",
        "phonetic_hint": "toh khah-roo-POH-meh-loh (oh MAHV-ros khree-SOHS tees KEE-proo)",
        "english": "carob syrup (the 'black gold' of Cyprus)",
        "notes": "Carobs (τα χαρούπια / τα τεράτσια) were historically Cyprus's largest agricultural export, earning the nickname 'black gold of Cyprus' (ο μαύρος χρυσός της Κύπρου); main festival in Anogyra.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα χαρουπόμελα",
            "accusative_singular": "το χαρουπόμελο"
        },
        "keg_communicative_function": "Culture & Products — Carob heritage",
        "example_el": "Τα χαρούπια ονομάστηκαν «ο μαύρος χρυσός της Κύπρου» λόγω της μεγάλης οικονομικής τους σημασίας.",
        "example_en": "Carobs were called 'the black gold of Cyprus' due to their great economic importance.",
        "example2_el": "Από τα χαρούπια παράγεται το θρεπτικό χαρουπόμελο και τα παραδοσιακά παστέλλια στην Ανώγυρα.",
        "example2_en": "From carobs, nutritious carob syrup and traditional pastelli bars are produced in Anogyra."
    },
    {
        "id": "CYP-U04-008",
        "greek": "το λουκούμι Γεροσκήπου",
        "phonetic_hint": "toh loo-KOO-mee yeh-roh-SKEE-poo",
        "english": "Geroskipou Loukoumi (Cyprus Delight)",
        "notes": "First Cypriot product to receive Protected Geographical Indication (ΠΓΕ) status in the EU; produced in Geroskipou in the Paphos district since 1895.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα λουκούμια Γεροσκήπου",
            "accusative_singular": "το λουκούμι Γεροσκήπου"
        },
        "keg_communicative_function": "Culture & Products — Paphos traditional sweets",
        "example_el": "Το λουκούμι Γεροσκήπου στην επαρχία Πάφου είναι κατοχυρωμένο προϊόν Προστατευόμενης Γεωγραφικής Ένδειξης.",
        "example_en": "Geroskipou Loukoumi in the Paphos district is a registered Protected Geographical Indication product.",
        "example2_el": "Ο Αγρός στην επαρχία Λεμεσού φημίζεται αντίστοιχα για το ροδόσταγμα από τριαντάφυλλα και τα γλυκά του κουταλιού.",
        "example2_en": "Agros in the Limassol district is correspondingly famous for its rosewater and spoon sweets."
    },
    {
        "id": "CYP-U04-009",
        "greek": "η σεφταλιά και το οφτό κλέφτικο",
        "phonetic_hint": "ee sehf-tah-LYAH keh toh ohf-TOH KLEHF-tee-koh",
        "english": "sheftalia and ofto kleftiko (traditional meat dishes)",
        "notes": "Classic Cypriot dishes: sheftalia is minced pork/lamb seasoned with onion and parsley wrapped in caul fat (μπόλια / πάνα) and grilled; ofto kleftiko is lamb/goat slow-baked in a sealed clay oven (ταβέ / κλέφτικος φούρνος).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι σεφταλιές",
            "accusative_singular": "τη σεφταλιά"
        },
        "keg_communicative_function": "Culture & Gastronomy — Traditional Cypriot cuisine",
        "example_el": "Στην κυπριακή πίτα σερβίρονται συνήθως σουβλάκια μαζί με παραδοσιακές σεφταλιές.",
        "example_en": "In Cypriot pita bread, souvlaki is usually served together with traditional sheftalia.",
        "example2_el": "Το οφτό κλέφτικο ψήνεται για πολλές ώρες σε παραδοσιακό πυρωμένο χωμάτινο φούρνο.",
        "example2_en": "Ofto kleftiko is slow-roasted for many hours in a traditional heated clay oven."
    },
    {
        "id": "CYP-U04-010",
        "greek": "— Ποια μεγάλη παραδοσιακή γιορτή γιορτάζεται την Πεντηκοστή στις παραλιακές πόλεις και ιδιαίτερα στη Λάρνακα; — Η Γιορτή του Κατακλυσμού.",
        "phonetic_hint": "pyah meh-GHAH-lee pah-rah-thoh-see-ah-KEE yor-TEE yor-TAH-zeh-teh teen pehn-dee-koh-STEE? ee yor-TEE too kah-tah-klee-ZMOO",
        "english": "— Which major traditional festival is celebrated at Pentecost in coastal towns and especially in Larnaca? — The Festival of the Flood (Kataklysmos).",
        "notes": "High-frequency past exam question! Celebrated 50 days after Orthodox Easter (Monday of the Holy Spirit / Δευτέρα του Αγίου Πνεύματος), uniquely preserved in Cyprus, with sea games, folk dance, and tsiattista.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Past Exam Q&A — Kataklysmos festival",
        "example_el": "Η Γιορτή του Κατακλυσμού γιορτάζεται πενήντα ημέρες μετά το Πάσχα, με επίκεντρο τις Φοινικούδες στη Λάρνακα.",
        "example_en": "The Festival of Kataklysmos is celebrated fifty days after Easter, centered at Finikoudes in Larnaca.",
        "example2_el": "Κατά τον Κατακλυσμό διοργανώνονται διαγωνισμοί τσιαττιστών, κυπριακοί χοροί και θαλάσσια αγωνίσματα.",
        "example2_en": "During Kataklysmos, competitions of tsiattista, Cypriot dances, and water sports are organized."
    },
    {
        "id": "CYP-U04-011",
        "greek": "τα τσιαττιστά (ποιητικοί αυτοσχεδιασμοί)",
        "phonetic_hint": "tah tsyah-tee-STAH (pee-ee-tee-KEE ahf-toh-skheh-thee-ah-ZMEE)",
        "english": "tsiattista (improvised oral poetic duelling)",
        "notes": "Improvised rhyming couplets in the Cypriot Greek dialect (15-syllable iambic verse / ιαμβικός δεκαπεντασύλλαβος), often accompanied by violin and lute; inscribed by UNESCO in 2011.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα τσιαττιστά",
            "accusative_plural": "τα τσιαττιστά"
        },
        "keg_communicative_function": "Culture & Traditions — Oral folk poetry",
        "example_el": "Τα τσιαττιστά είναι αυτοσχέδια ομοιοκατάληκτα δίστιχα στην κυπριακή διάλεκτο και προστατεύονται από την UNESCO.",
        "example_en": "Tsiattista are improvised rhyming couplets in the Cypriot dialect and are protected by UNESCO.",
        "example2_el": "Οι ποιητάρηδες διαγωνίζονται στα τσιαττιστά με τη συνοδεία βιολιού και λαούτου.",
        "example2_en": "The folk poets compete in tsiattista accompanied by violin and lute."
    },
    {
        "id": "CYP-U04-012",
        "greek": "— Σε ποια πόλη της Κύπρου διοργανώνονται κάθε χρόνο το μεγαλύτερο Καρναβάλι και η Γιορτή του Κρασιού; — Στη Λεμεσό.",
        "phonetic_hint": "seh pyah POH-lee tees KEE-proo thee-or-ghah-NOH-nohn-deh toh meh-ghah-LEE-teh-roh kahr-nah-VAH-lee keh ee yor-TEE too krah-SYOO? stee leh-meh-SOH",
        "english": "— In which city of Cyprus are the largest Carnival and the Wine Festival organized every year? — In Limassol.",
        "notes": "Actual past exam question! Both the famous Carnival parade (before Clean Monday) and the Wine Festival (late August/September in the Limassol Municipal Garden) take place in Limassol.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Past Exam Q&A — Major cultural festivals of Limassol",
        "example_el": "Η Γιορτή του Κρασιού πραγματοποιείται κάθε χρόνο στον Δημόσιο Κήπο της Λεμεσού από το 1961.",
        "example_en": "The Wine Festival takes place every year in the Municipal Garden of Limassol since 1961.",
        "example2_el": "Το Καρναβάλι Λεμεσού κορυφώνεται με τη μεγάλη καρναβαλίστικη παρέλαση την Κυριακή πριν από την Καθαρά Δευτέρα.",
        "example2_en": "The Limassol Carnival culminates with the grand carnival parade on the Sunday before Clean Monday."
    },
    {
        "id": "CYP-U04-013",
        "greek": "η Καθαρά Δευτέρα («το κόψιμο της μουττής της Σαρακοστής»)",
        "phonetic_hint": "ee kah-thah-RAH thef-TEH-rah",
        "english": "Clean Monday / Green Monday (start of Lent in the countryside)",
        "notes": "In Cyprus, going out to the fields on Clean Monday to eat fasting food (λαγάνα, ταχίνι, χαλβάς, ελιές, λαχανικά) and fly kites is traditionally called «κόβω τη μουττή (μύτη) της Σαρακοστής».",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "accusative_singular": "την Καθαρά Δευτέρα"
        },
        "keg_communicative_function": "Culture & Customs — Clean Monday traditions",
        "example_el": "Την Καθαρά Δευτέρα οι Κύπριοι βγαίνουν στους αγρούς με νηστίσιμα φαγητά και πετούν χαρταετό.",
        "example_en": "On Clean Monday, Cypriots go out to the fields with Lenten foods and fly kites.",
        "example2_el": "Το έθιμο της εξόδου στη φύση την Καθαρά Δευτέρα λέγεται στην Κύπρο «κόψιμο της μουττής της Σαρακοστής».",
        "example2_en": "The custom of going out into nature on Clean Monday is called in Cyprus 'cutting the nose of Lent'."
    },
    {
        "id": "CYP-U04-014",
        "greek": "η λαμπρατζιά (το έθιμο του Μεγάλου Σαββάτου)",
        "phonetic_hint": "ee lahm-brah-TZAH (toh EH-thee-moh too meh-GHAH-loo sah-VAH-too)",
        "english": "lambratzia (the Easter bonfire on Holy Saturday night)",
        "notes": "Traditional Cypriot Easter bonfire lit in churchyards on Holy Saturday night at the Resurrection service, symbolically burning the effigy of Judas (ο Ιούδας).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι λαμπρατζιές",
            "accusative_singular": "τη λαμπρατζιά"
        },
        "keg_communicative_function": "Culture & Customs — Cypriot Easter traditions",
        "example_el": "Η λαμπρατζιά είναι η μεγάλη φωτιά που ανάβει έξω από τις εκκλησίες το βράδυ της Ανάστασης στην Κύπρο.",
        "example_en": "The lambratzia is the large bonfire lit outside churches on the night of the Resurrection in Cyprus.",
        "example2_el": "Την Κυριακή και τη Δευτέρα του Πάσχα στα χωριά της Κύπρου διοργανώνονται παραδοσιακά πασχαλινά παιχνίδια, όπως οι σακκουλοδρομίες και το σχοινί.",
        "example2_en": "On Easter Sunday and Monday in the villages of Cyprus, traditional Easter games such as sack races and tug-of-war are organized."
    },
    {
        "id": "CYP-U04-015",
        "greek": "τα Ανθεστήρια (η γιορτή των λουλουδιών)",
        "phonetic_hint": "tah ahn-theh-STEE-ree-ah (ee yor-TEE ton loo-loo-THYON)",
        "english": "the Anthestiria (Spring Flower Festival)",
        "notes": "Celebrated every May in cities such as Larnaca, Paphos, and Limassol with flower-decorated floats celebrating spring and rebirth, tracing its roots to ancient Greek festivals in honor of Dionysus.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Ανθεστήρια",
            "accusative_plural": "τα Ανθεστήρια"
        },
        "keg_communicative_function": "Culture & Customs — Spring festivals",
        "example_el": "Τα Ανθεστήρια είναι η γιορτή των λουλουδιών και της άνοιξης που γιορτάζεται τον Μάιο με παρελάσεις ανθοστόλιστων αρμάτων.",
        "example_en": "The Anthestiria is the festival of flowers and spring celebrated in May with parades of flower-decorated floats.",
        "example2_el": "Η γιορτή των Ανθεστηρίων έχει τις ρίζες της στην αρχαία Ελλάδα.",
        "example2_en": "The festival of Anthestiria has its roots in ancient Greece."
    },
    {
        "id": "CYP-U04-016",
        "greek": "η Χοιροκοιτία (ο νεολιθικός οικισμός)",
        "phonetic_hint": "ee khee-roh-kee-TEE-ah (oh neh-oh-lee-thee-KOHS ee-keez-MOHS)",
        "english": "Choirokoitia (UNESCO Neolithic settlement)",
        "notes": "Prehistoric Neolithic settlement in the Larnaca district dating back to the 7th millennium BC, famous for its circular stone houses (θόλοι); UNESCO World Heritage Site since 1998.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "accusative_singular": "τη Χοιροκοιτία",
            "genitive_singular": "της Χοιροκοιτίας"
        },
        "keg_communicative_function": "Culture & Archaeology — UNESCO World Heritage Sites",
        "example_el": "Ο νεολιθικός οικισμός της Χοιροκοιτίας βρίσκεται στην επαρχία Λάρνακας και αποτελεί Μνημείο Παγκόσμιας Κληρονομιάς της UNESCO.",
        "example_en": "The Neolithic settlement of Choirokoitia is located in the Larnaca district and is a UNESCO World Heritage Site.",
        "example2_el": "Ο οικισμός χαρακτηρίζεται από τις κυκλικές λιθόκτιστες κατοικίες του που χρονολογούνται από την 7η χιλιετία π.Χ.",
        "example2_en": "The settlement is characterized by its circular stone-built dwellings dating from the 7th millennium BC."
    },
    {
        "id": "CYP-U04-017",
        "greek": "οι Τάφοι των Βασιλέων και τα Ψηφιδωτά της Πάφου",
        "phonetic_hint": "ee TAH-fee ton vah-see-LEH-on keh tah psee-fee-thoh-TAH tees PAH-foo",
        "english": "the Tombs of the Kings and the Paphos Mosaics",
        "notes": "Inscribed on the UNESCO World Heritage list in 1980. The Hellenistic/Roman underground peristyle tombs in Kato Paphos housed high officials and Ptolemaic aristocrats (not actual kings).",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι Τάφοι των Βασιλέων",
            "accusative_plural": "τους Τάφους των Βασιλέων"
        },
        "keg_communicative_function": "Culture & Archaeology — UNESCO sites in Paphos",
        "example_el": "Οι Τάφοι των Βασιλέων και τα περίφημα ρωμαϊκά ψηφιδωτά βρίσκονται στην Κάτω Πάφο.",
        "example_en": "The Tombs of the Kings and the famous Roman mosaics are located in Kato Paphos.",
        "example2_el": "Ο αρχαιολογικός χώρος της Πάφου εντάχθηκε στον κατάλογο Παγκόσμιας Κληρονομιάς της UNESCO το 1980.",
        "example2_en": "The archaeological site of Paphos was inscribed on the UNESCO World Heritage list in 1980."
    },
    {
        "id": "CYP-U04-018",
        "greek": "οι τοιχογραφημένοι βυζαντινοί ναοί του Τροόδους",
        "phonetic_hint": "ee tee-khoh-ghrah-fee-MEH-nee vee-zahn-dee-NEE nah-EE too troh-OH-thoos",
        "english": "the Painted Byzantine Churches in the Troodos Region (UNESCO)",
        "notes": "Ten timber-roofed Byzantine and post-Byzantine churches in Troodos (such as Panagia tis Asinou, Agios Nikolaos tis Stegis in Kakopetria, Panagia tou Araka in Lagoudera) listed by UNESCO since 1985.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "plural": "οι τοιχογραφημένοι ναοί",
            "accusative_plural": "τους τοιχογραφημένους ναούς"
        },
        "keg_communicative_function": "Culture & Heritage — UNESCO churches of Troodos",
        "example_el": "Δέκα τοιχογραφημένοι βυζαντινοί ναοί στην οροσειρά του Τροόδους προστατεύονται ως Μνημεία Παγκόσμιας Κληρονομιάς της UNESCO.",
        "example_en": "Ten painted Byzantine churches in the Troodos mountain range are protected as UNESCO World Heritage Sites.",
        "example2_el": "Μεταξύ αυτών είναι η Παναγία της Ασίνου, ο Άγιος Νικόλαος της Στέγης στην Κακοπετριά και η Παναγία του Άρακα στα Λαγουδερά.",
        "example2_en": "Among them are Panagia tis Asinou, Agios Nikolaos tis Stegis in Kakopetria, and Panagia tou Araka in Lagoudera."
    },
    {
        "id": "CYP-U04-019",
        "greek": "το αρχαίο θέατρο του Κουρίου",
        "phonetic_hint": "toh ahr-KHEH-oh THEH-ah-troh too koo-REE-oo",
        "english": "the ancient Greco-Roman theater of Kourion",
        "notes": "Located on a cliff overlooking Episkopi Bay in the Limassol district; built in the 2nd century BC and still used today for international ancient Greek drama festivals and concerts.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα αρχαία θέατρα",
            "accusative_singular": "το αρχαίο θέατρο του Κουρίου"
        },
        "keg_communicative_function": "Culture & Archaeology — Ancient city-kingdoms of Cyprus",
        "example_el": "Το αρχαίο θέατρο του Κουρίου βρίσκεται στην επαρχία Λεμεσού και φιλοξενεί παραστάσεις αρχαίου δράματος.",
        "example_en": "The ancient theater of Kourion is located in the Limassol district and hosts performances of ancient drama.",
        "example2_el": "Στα κατεχόμενα εδάφη, κοντά στην Αμμόχωστο, βρίσκονται επίσης η αρχαία πόλη και το θέατρο της Σαλαμίνας.",
        "example2_en": "In the occupied territories, near Famagusta, also lie the ancient city and theater of Salamis."
    },
    {
        "id": "CYP-U04-020",
        "greek": "η Αυτοκέφαλη Εκκλησία της Κύπρου",
        "phonetic_hint": "ee ahf-toh-KEH-fah-lee eh-klee-SEE-ah tees KEE-proo",
        "english": "the Autocephalous Orthodox Church of Cyprus",
        "notes": "One of the oldest autocephalous Eastern Orthodox churches (autocephaly recognized by the Third Ecumenical Council of Ephesus in 431 AD). Founded by Apostles Barnabas and Paul in 45 AD.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "accusative_singular": "την Αυτοκέφαλη Εκκλησία της Κύπρου"
        },
        "keg_communicative_function": "Culture & Religion — Church of Cyprus",
        "example_el": "Η Εκκλησία της Κύπρου ιδρύθηκε το 45 μ.Χ. από τους Αποστόλους Παύλο και Βαρνάβα.",
        "example_en": "The Church of Cyprus was founded in 45 AD by the Apostles Paul and Barnabas.",
        "example2_el": "Προκαθήμενος της Εκκλησίας της Κύπρου είναι ο Αρχιεπίσκοπος Γεώργιος.",
        "example2_en": "The Primate of the Church of Cyprus is Archbishop Georgios."
    },
    {
        "id": "CYP-U04-021",
        "greek": "— Ποιος είναι ο προστάτης άγιος και ιδρυτής της Εκκλησίας της Κύπρου; — Ο Απόστολος Βαρνάβας.",
        "phonetic_hint": "pyos EE-neh oh proh-STAH-tees AH-yee-os keh ee-three-TEES tees eh-klee-SEE-ahs tees KEE-proo? oh ah-POH-stoh-los vahr-NAH-vahs",
        "english": "— Who is the patron saint and founder of the Church of Cyprus? — Apostle Barnabas.",
        "notes": "Past exam question! Apostle Barnabas, a native of Salamis in Cyprus, preached Christianity on the island with Apostle Paul in 45 AD; his tomb and monastery are near occupied Salamis/Famagusta. Feast day: 11 June.",
        "gender_or_pos": "phrase",
        "grammatical_info": {"part_of_speech": "phrase"},
        "keg_communicative_function": "Past Exam Q&A — Patron saint of Cyprus",
        "example_el": "Ο Απόστολος Βαρνάβας καταγόταν από τη Σαλαμίνα της Κύπρου και είναι ο ιδρυτής και προστάτης της Εκκλησίας της Κύπρου.",
        "example_en": "Apostle Barnabas hailed from Salamis in Cyprus and is the founder and patron saint of the Church of Cyprus.",
        "example2_el": "Η μνήμη του Αποστόλου Βαρνάβα γιορτάζεται στις 11 Ιουνίου.",
        "example2_en": "The feast day of Apostle Barnabas is celebrated on 11 June."
    },
    {
        "id": "CYP-U04-022",
        "greek": "η Ιερά Μονή Κύκκου",
        "phonetic_hint": "ee ee-eh-RAH moh-NEE KEE-koo",
        "english": "the Holy Monastery of Kykkos",
        "notes": "The wealthiest and best-known monastery in Cyprus, founded at the end of the 11th century under Byzantine Emperor Alexios I Komnenos in the Troodos mountains; houses the sacred icon of the Virgin Mary attributed to Evangelist Luke. Tomb of Archbishop Makarios III is nearby at Throni (στο Θρονί).",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι Ιερές Μονές",
            "accusative_singular": "την Ιερά Μονή Κύκκου"
        },
        "keg_communicative_function": "Culture & Religion — Major monasteries of Cyprus",
        "example_el": "Η Ιερά Μονή Κύκκου βρίσκεται στην οροσειρά του Τροόδους και ιδρύθηκε στα τέλη του 11ου αιώνα.",
        "example_en": "The Holy Monastery of Kykkos is located in the Troodos mountain range and was founded at the end of the 11th century.",
        "example2_el": "Πολύ κοντά στη Μονή Κύκκου, στην τοποθεσία «Θρονί», βρίσκεται ο τάφος του πρώτου Προέδρου της Κύπρου, Αρχιεπισκόπου Μακαρίου Γ΄.",
        "example2_en": "Very close to Kykkos Monastery, at the site of 'Throni', lies the tomb of the first President of Cyprus, Archbishop Makarios III."
    },
    {
        "id": "CYP-U04-023",
        "greek": "η Ιερά Μονή Μαχαιρά και η Μονή Σταυροβουνίου",
        "phonetic_hint": "ee ee-eh-RAH moh-NEE mah-kheh-RAH keh ee moh-NEE stahv-roh-voo-NEE-oo",
        "english": "Machairas Monastery and Stavrovouni Monastery",
        "notes": "Machairas Monastery (Nicosia district) hides the lair where EOKA hero Grigoris Afxentiou fell on 3 March 1957; Stavrovouni Monastery (Larnaca district) was founded by Saint Helena in the 4th century AD.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "accusative_singular": "την Ιερά Μονή Μαχαιρά"
        },
        "keg_communicative_function": "Culture & Religion — Historic monasteries",
        "example_el": "Κοντά στη Μονή Μαχαιρά βρίσκεται το κρησφύγετο όπου έπεσε ηρωικά μαχόμενος ο υπαρχηγός της ΕΟΚΑ Γρηγόρης Αυξεντίου το 1957.",
        "example_en": "Near Machairas Monastery lies the hideout where EOKA deputy leader Grigoris Afxentiou fell heroically fighting in 1957.",
        "example2_el": "Η Μονή Σταυροβουνίου στην επαρχία Λάρνακας ιδρύθηκε κατά την παράδοση από την Αγία Ελένη τον 4ο αιώνα μ.Χ.",
        "example2_en": "Stavrovouni Monastery in the Larnaca district was founded according to tradition by Saint Helena in the 4th century AD."
    },
    {
        "id": "CYP-U04-024",
        "greek": "το Τέμενος Χαλά Σουλτάν Τεκκέ (Αλυκή Λάρνακας)",
        "phonetic_hint": "toh TEH-meh-nos khah-LAH sool-TAHN teh-KEH",
        "english": " the Hala Sultan Tekke Mosque (Larnaca Salt Lake)",
        "notes": "Important Muslim shrine on the banks of the Larnaca Salt Lake, protected as a cultural monument in the government-controlled areas.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Τεμένη",
            "accusative_singular": "το Τέμενος Χαλά Σουλτάν Τεκκέ"
        },
        "keg_communicative_function": "Culture & Religion — Religious monuments in Cyprus",
        "example_el": "Το Τέμενος Χαλά Σουλτάν Τεκκέ βρίσκεται στις όχθες της Αλυκής Λάρνακας και αποτελεί σημαντικό μουσουλμανικό μνημείο.",
        "example_en": "The Hala Sultan Tekke Mosque is located on the banks of the Larnaca Salt Lake and is an important Muslim monument.",
        "example2_el": "Η Κυπριακή Δημοκρατία προστατεύει τα θρησκευτικά μνημεία όλων των κοινοτήτων και θρησκειών του νησιού.",
        "example2_en": "The Republic of Cyprus protects the religious monuments of all communities and religions of the island."
    },
    {
        "id": "CYP-U04-025",
        "greek": "ο Ναός του Αγίου Λαζάρου στη Λάρνακα",
        "phonetic_hint": "oh nah-OHS too ah-YEE-oo lah-ZAH-roo stee LAHR-nah-kah",
        "english": "the Church of Saint Lazarus in Larnaca",
        "notes": "Late 9th-century Byzantine stone church in Larnaca built over the second tomb of Lazarus of Bethany, who according to tradition became the first Bishop of Kition (Larnaca) and lived there for 30 years.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "accusative_singular": "τον Ναό του Αγίου Λαζάρου"
        },
        "keg_communicative_function": "Culture & Religion — Patron saint of Larnaca",
        "example_el": "Ο Άγιος Λάζαρος είναι ο πολιούχος της Λάρνακας (αρχαίο Κίτιο), όπου έζησε και διετέλεσε πρώτος επίσκοπος.",
        "example_en": "Saint Lazarus is the patron saint of Larnaca (ancient Kition), where he lived and served as the first bishop.",
        "example2_el": "Ο βυζαντινός ναός του Αγίου Λαζάρου στο κέντρο της Λάρνακας χτίστηκε τον 9ο αιώνα μ.Χ.",
        "example2_en": "The Byzantine church of Saint Lazarus in the center of Larnaca was built in the 9th century AD."
    },
    {
        "id": "CYP-U04-026",
        "greek": "η Κυπριακή Διάλεκτος",
        "phonetic_hint": "ee kee-pree-ah-KEE thee-AH-lehk-tos",
        "english": "the Cypriot Greek Dialect",
        "notes": "Spoken variety of Greek used in everyday life in Cyprus alongside Standard Modern Greek (η Κοινή Νεοελληνική), preserving medieval and ancient Greek vocabulary and phonological traits. Famous dialect poets: Vasilis Michaelides (Βασίλης Μιχαηλίδης, national poet of Cyprus, author of «Η 9η Ιουλίου του 1821») and Dimitris Lipertis.",
        "gender_or_pos": "noun (feminine)",
        "grammatical_info": {
            "part_of_speech": "noun (feminine)",
            "plural": "οι διάλεκτοι",
            "accusative_singular": "την Κυπριακή Διάλεκτο"
        },
        "keg_communicative_function": "Culture & Literature — Language and national poets",
        "example_el": "Ο Βασίλης Μιχαηλίδης θεωρείται ο εθνικός ποιητής της Κύπρου και έγραψε στην κυπριακή διάλεκτο το ποίημα «Η 9η Ιουλίου του 1821».",
        "example_en": "Vasilis Michaelides is considered the national poet of Cyprus and wrote the poem 'The 9th of July 1821' in the Cypriot dialect.",
        "example2_el": "Στην επίσημη διοίκηση και στην εκπαίδευση χρησιμοποιείται η Κοινή Νεοελληνική, ενώ στην καθημερινή προφορική επικοινωνία η κυπριακή διάλεκτος.",
        "example2_en": "In official administration and education Standard Modern Greek is used, while in daily oral communication the Cypriot dialect is used."
    },
    {
        "id": "CYP-U04-027",
        "greek": "το Κάστρο του Κολοσσίου και το Κάστρο της Λεμεσού",
        "phonetic_hint": "toh KAH-stroh too koh-loh-SEE-oo keh toh KAH-stroh tees leh-meh-SOO",
        "english": "Kolossi Castle and Limassol Medieval Castle",
        "notes": "Kolossi Castle (west of Limassol) was the Crusader headquarters for Commandaria wine and sugar cane production; Limassol Castle is where Richard the Lionheart married Berengaria of Navarre in 1191.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Κάστρα",
            "accusative_singular": "το Κάστρο του Κολοσσίου"
        },
        "keg_communicative_function": "Culture & History — Medieval castles of Cyprus",
        "example_el": "Το μεσαιωνικό Κάστρο του Κολοσσίου στη Λεμεσό συνδέεται ιστορικά με την παραγωγή του γλυκού κρασιού Κουμανδαρία.",
        "example_en": "The medieval Kolossi Castle in Limassol is historically linked with the production of the sweet wine Commandaria.",
        "example2_el": "Στο μεσαιωνικό Κάστρο της Λεμεσού στεγάζεται σήμερα το Μεσαιωνικό Μουσείο Κύπρου.",
        "example2_en": "The Medieval Castle of Limassol today houses the Cyprus Medieval Museum."
    },
    {
        "id": "CYP-U04-028",
        "greek": "το Κυπριακό Μουσείο στη Λευκωσία",
        "phonetic_hint": "toh kee-pree-ah-KOH moo-SEE-oh stee lef-koh-SEE-ah",
        "english": "the Cyprus Museum (Archaeological Museum in Nicosia)",
        "notes": "Oldest and largest archaeological museum in Cyprus (founded 1882), located in Nicosia; houses treasures such as the Horned God of Enkomi, the Idol of Pomos (το ειδώλιο του Πωμού), and the Salamis statues.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα Κυπριακά Μουσεία",
            "accusative_singular": "το Κυπριακό Μουσείο"
        },
        "keg_communicative_function": "Culture & Archaeology — National museum & artifacts",
        "example_el": "Το Κυπριακό Μουσείο στη Λευκωσία είναι το μεγαλύτερο και παλαιότερο αρχαιολογικό μουσείο της Κύπρου.",
        "example_en": "The Cyprus Museum in Nicosia is the largest and oldest archaeological museum in Cyprus.",
        "example2_el": "Το προϊστορικό σταυρόσχημο ειδώλιο του Πωμού απεικονίζεται στα κυπριακά κέρματα του ενός και των δύο ευρώ.",
        "example2_en": "The prehistoric cruciform idol of Pomos is depicted on the Cypriot one-euro and two-euro coins."
    },
    {
        "id": "CYP-U04-029",
        "greek": "ο ΘΟΚ (Θεατρικός Οργανισμός Κύπρου)",
        "phonetic_hint": "oh THOHK (theh-ah-tree-KOHS or-ghah-nee-ZMOHS KEE-proo)",
        "english": "THOC (Cyprus Theatre Organisation)",
        "notes": "State theater organization of Cyprus, founded in 1971 and headquartered in Nicosia.",
        "gender_or_pos": "noun (masculine)",
        "grammatical_info": {
            "part_of_speech": "noun (masculine)",
            "accusative_singular": "τον Θεατρικό Οργανισμό Κύπρου"
        },
        "keg_communicative_function": "Culture & Arts — State cultural institutions",
        "example_el": "Ο Θεατρικός Οργανισμός Κύπρου (ΘΟΚ) ιδρύθηκε το 1971 και αποτελεί τον κρατικό θεατρικό φορέα της χώρας.",
        "example_en": "The Cyprus Theatre Organisation (THOC) was founded in 1971 and is the state theatrical institution of the country.",
        "example2_el": "Το κεντρικό κτίριο και οι σκηνές του ΘΟΚ βρίσκονται στη Λευκωσία.",
        "example2_en": "The main building and stages of THOC are located in Nicosia."
    },
    {
        "id": "CYP-U04-030",
        "greek": "το καπνιστό της Πιτσιλιάς (τα παραδοσιακά αλλαντικά: λούντζα, χοιρομέρι, λουκάνικα)",
        "phonetic_hint": "toh kah-pnee-STOH tees pee-tsee-LYAHS (LOON-dzah, khee-roh-MEH-ree, loo-KAH-nee-kah)",
        "english": "smoked meats of Pitsilia (lountza, chiromeri, sausages)",
        "notes": "Traditional Cypriot cured and smoked pork delicacies from the mountainous Pitsilia region (Αγρός, Πελένδρι, Κυπερούντα) marinated in red wine and coriander seeds, certified with EU PGI status.",
        "gender_or_pos": "noun (neuter)",
        "grammatical_info": {
            "part_of_speech": "noun (neuter)",
            "plural": "τα καπνιστά αλλαντικά",
            "accusative_singular": "το καπνιστό της Πιτσιλιάς"
        },
        "keg_communicative_function": "Culture & Products — Traditional PGI delicacies",
        "example_el": "Η ορεινή περιοχή της Πιτσιλιάς φημίζεται για τα παραδοσιακά αλλαντικά της, όπως η λούντζα, το χοιρομέρι και τα κρασάτα λουκάνικα.",
        "example_en": "The mountainous region of Pitsilia is famous for its traditional cured meats, such as lountza, chiromeri, and wine-marinated sausages.",
        "example2_el": "Τα αλλαντικά της Πιτσιλιάς ωριμάζουν σε κόκκινο κρασί με κόλιανδρο και καπνίζονται με ξύλα.",
        "example2_en": "The cured meats of Pitsilia are matured in red wine with coriander and wood-smoked."
    }
]


def main():
    write_unit(
        unit_id="unit-cyp-04",
        title="Μάθημα 4: Πολιτισμός, Παράδοση, Ήθη, Έθιμα & Προϊόντα (Culture, Traditions & Products)",
        description="UNESCO World Heritage and Intangible Heritage in Cyprus (Paphos, Choirokoitia, Painted Churches of Troodos, Lefkara lace, Tsiattista), PDO/PGI products (Halloumi, Commandaria, Zivania, Geroskipou Loukoumi), festivals (Kataklysmos, Limassol Carnival & Wine Festival), and the Church of Cyprus.",
        notes=NOTES_CYP_04,
        cards=CARDS_CYP_04,
    )


if __name__ == "__main__":
    main()

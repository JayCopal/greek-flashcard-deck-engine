import os
import sys
import yaml
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = Path(__file__).resolve().parent.parent

def update_manifest():
    manifest_path = BASE_DIR / "content" / "manifest.yaml"
    with open(manifest_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)

    units = data.get('units', [])
    
    # 1. Update unit-a2-00 to 12 in manifest to ensure clean KEG-A2-P1-XX-A order
    for u in units:
        uid = u['id']
        if uid.startswith('unit-a2-'):
            num = int(uid.split('-')[2])
            u['order'] = f"KEG-A2-P1-{num:02d}-A"
        elif uid.startswith('unit-a2p2-'):
            num = int(uid.split('-')[2])
            u['order'] = f"KEG-A2-P2-{num:02d}-A"

    # Remove any old wr1/wr2 units if they existed
    units = [u for u in units if not (u['id'].startswith('unit-wr1-') or u['id'].startswith('unit-wr2-'))]

    # 2. Add unit-wr1-01 to 06
    wr1_specs = [
        ("unit-wr1-01", "KEG-A2-WR-P1-01-A", "Μάθημα 1: Αποκωδικοποίηση Οδηγιών & Ρήματα Εξεταστή (Prompt Decoders & Examiner Directives)", "Mastering authentic Greek exam instructions: action verbs and tense cues."),
        ("unit-wr1-02", "KEG-A2-WR-P1-02-A", "Μάθημα 2: Φόρμουλες Έναρξης, Μετάβασης & Κλεισίματος (Formulaic Openers, Transitions & Closers)", "Standard letter and email frameworks: friendly salutations, transition chunks, apologies for late replies, and sign-offs."),
        ("unit-wr1-03", "KEG-A2-WR-P1-03-A", "Μάθημα 3: Συνδετικές Λέξεις & Συντακτική Συνοχή (Discourse Connectors & Logical Flow)", "High-scoring sentence linkers: sequence, contrast, cause/effect, and condition."),
        ("unit-wr1-04", "KEG-A2-WR-P1-04-A", "Μάθημα 4: Γραμματικοί Ασφαλείς Λιμένες & Ανώμαλοι Αόριστοι (Grammar Safe Harbors)", "Eliminating high-penalty errors in A2 written exams: irregular past stems, clitic pronoun positions, and modal subjunctive rules."),
        ("unit-wr1-05", "KEG-A2-WR-P1-05-A", "Μάθημα 5: Παγίδες Ορθογραφίας, Τόνοι & Συμφωνία (Error Hunter & Orthography Traps)", "Eliminating high-penalty errors in written production: πολύ vs πολλή, final nu rules, -τε vs -ται verb endings, stress marks (τόνος), and clitic placement."),
        ("unit-wr1-06", "KEG-A2-WR-P1-06-A", "Μάθημα 6: Lego Sentence Builders — Task 1 Σημειώματα & Μηνύματα (Task 1 Functional Notes)", "Modular sentence building blocks for Task 1 functional notes (30-45 words): arrangements, leaving keys, watering plants, and reminders.")
    ]

    for uid, order, title, desc in wr1_specs:
        units.append({
            "id": uid,
            "title": title,
            "description": desc,
            "order": order,
            "total_lessons": 1,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": f"{uid}/lesson-01.yaml",
                    "title": title
                }
            ]
        })

    # 3. Add unit-wr2-01 to 06
    wr2_specs = [
        ("unit-wr2-01", "KEG-A2-WR-P2-01-A", "Μάθημα 1: Προσκλήσεις, Γενέθλια & RSVP (Thematic Playbook 1: Social Invitations & Parties)", "Mastering Task 1 notes: composing and replying to party, birthday, and celebration invitations, accepting or politely declining with justifications."),
        ("unit-wr2-02", "KEG-A2-WR-P2-02-A", "Μάθημα 2: Γραπτός Λόγος — Το Σπίτι, η Γειτονιά & Μετακόμιση (A2 Writing: Housing & Moving)", "Describing apartments, rooms, locations, and neighborhood facilities, handling housewarming invitations and practical rental inquiries."),
        ("unit-wr2-03", "KEG-A2-WR-P2-03-A", "Μάθημα 3: Γραπτός Λόγος — Υγεία, Συμπτώματα & Απουσία (A2 Writing: Health & Absences)", "Describing illness symptoms, doctor diagnoses, and writing polite notes to employers, teachers, or colleagues excusing absences."),
        ("unit-wr2-04", "KEG-A2-WR-P2-04-A", "Μάθημα 4: Γραπτός Λόγος — Ταξίδια, Διακοπές & Εκδρομές (A2 Writing: Travel & Holidays)", "Mastering the narrative past in Task 2 compositions: setting the scene, describing places, expressing impressions, and using chronological Aorist chains."),
        ("unit-wr2-05", "KEG-A2-WR-P2-05-A", "Μάθημα 5: Γραπτός Λόγος — Φαγητό, Αγορά & Προτάσεις στην Πόλη (A2 Writing: Dining & City Life)", "Writing restaurant reviews and recommendations, making table reservations, and detailing city shopping excursions."),
        ("unit-wr2-06", "KEG-A2-WR-P2-06-A", "Μάθημα 6: Γραπτός Λόγος — Προσομοιώσεις Εξετάσεων ΚΕΓ Α2 (A2 Writing: Mock Exam Capstone)", "Full-scale integrated exam simulations replicating authentic KEG past papers: paired Task 1 (30-45 words) and Task 2 (65-80 words) prompts with model scripts and scoring rubrics.")
    ]

    for uid, order, title, desc in wr2_specs:
        units.append({
            "id": uid,
            "title": title,
            "description": desc,
            "order": order,
            "total_lessons": 1,
            "lessons": [
                {
                    "id": "lesson-01",
                    "file": f"{uid}/lesson-01.yaml",
                    "title": title
                }
            ]
        })

    data['units'] = units
    with open(manifest_path, 'w', encoding='utf-8') as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    print(f"Successfully updated content/manifest.yaml with {len(units)} units total!")

if __name__ == '__main__':
    update_manifest()

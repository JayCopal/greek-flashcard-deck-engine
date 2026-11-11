---
name: keg-a2-speaking-builder
description: Design, build, and expand CEFR A2 Modern Greek Speaking Examination (Παραγωγή και Διάδραση Προφορικού Λόγου) preparation modules (SP-01 to SP-06) aligned with the Centre for the Greek Language (ΚΕΓ) evaluation rubrics, dual model responses, and Google Cloud Chirp-3 HD audio synthesis.
---

# KEG A2 Modern Greek Speaking Examination Builder (`keg-a2-speaking-builder`)

Use this skill when generating, expanding, or auditing flashcards and interactive speaking drills for the **Centre for the Greek Language (ΚΕΓ / KEG) Level A2 Speaking Examination (Παραγωγή και Διάδραση Προφορικού Λόγου)**.

Full specification: [docs/KEG_A2_SPEAKING_CURRICULUM_SPEC.md](file:///c:/jay-programs/greek-flashcard-deck-engine/docs/KEG_A2_SPEAKING_CURRICULUM_SPEC.md)

## Core Curriculum Modules (`unit-sp-01` to `unit-sp-06`)

1. **`unit-sp-01` (`SP-01-A`)**: Rapid Examiner Q&A Drills (Stage 1 Warm-up & Personal Interview)
2. **`unit-sp-02` (`SP-02-A`)**: Conversational Connectors & Hesitation Managers (Spoken Fluency Boosters)
3. **`unit-sp-03` (`SP-03-A`)**: Stage 2 Cue Card Scenarios & Bilateral Roleplays (Information Exchange)
4. **`unit-sp-04` (`SP-04-A`)**: Stage 3 Visual Description Lego Framework (Image Monologues)
5. **`unit-sp-05` (`SP-05-A`)**: Examiner Personal Extension Questions (Stage 3 Follow-up & Multi-Tense Narrative)
6. **`unit-sp-06` (`SP-06-A`)**: Spoken Phonology & High-Frequency Trap Drills (Orthoepy, Stress Shifts & Polite Tone)

## Card Schema Requirements

- **`id`**: `SP-U01-001` through `SP-U06-040`
- **`gender_or_pos`**: `"speaking-drill"`
- **`grammatical_info`**: Must include `stage` and `focus`
- **`example_el` / `example_en`**: Primary high-scoring spoken model response (`example_audio` via Chirp-3 HD)
- **`example2_el` / `example2_en`**: Alternative/creative spoken response (`example2_audio` via Chirp-3 HD)
- **`keg_communicative_function`**: Official CEFR A2 communicative descriptor

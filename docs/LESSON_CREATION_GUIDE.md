# Lesson & Curriculum Creation Guide (Single Source of Truth)

This guide defines the standards, schemas, validation rules, and workflows for creating and expanding lessons in the **Greek Flashcard Deck Engine**.

---

## 1. Architectural Principle: Single Source of Truth (SSOT)

The **only source of truth** for card data, units, and lessons in this application is the local YAML structure inside `content/`:

```
content/
├── manifest.yaml             # Master index of units, lesson order, and deck metadata
├── unit-01/
│   └── lesson-01.yaml        # All cards, grammar notes, and metadata for Unit 1
├── unit-02/
│   └── lesson-01.yaml        # Unit 2
├── unit-03/
│   └── lesson-01.yaml        # Unit 3
├── unit-04/
│   └── lesson-01.yaml        # Unit 4
└── unit-05/
    └── lesson-01.yaml        # Unit 5
```

> [!IMPORTANT]
> The web application (`FastAPI`, `React/Vite`, and the PWA builder) **only reads `content/manifest.yaml` and the referenced lesson YAML files**.
> Intermediate JSON batch files (e.g. `keg_a1_units_*.json`) are **not** read directly by the application runtime. Any card defined in a JSON file is completely invisible until synced into the YAML files.

---

## 2. YAML File Schemas

### 2.1 Manifest Schema (`content/manifest.yaml`)

Every unit and lesson must be registered in `content/manifest.yaml`:

```yaml
deck_title: "Modern Greek Mastery (CEFR A1)"
source_language: "en"
target_language: "el"
created_at: "2026-10-25"
units:
  - id: "unit-01"
    title: "Χαιρετισμοί & Γνωριμία (Greetings & Introductions)"
    order: 1
    lessons:
      - id: "lesson-01"
        file: "unit-01/lesson-01.yaml"
        title: "Χαιρετισμοί & Γνωριμία (Greetings & Introductions)"
  - id: "unit-02"
    title: "Καταγωγή, Εθνικότητες & Γλώσσες (Origins, Nationalities & Languages)"
    order: 2
    lessons:
      - id: "lesson-01"
        file: "unit-02/lesson-01.yaml"
        title: "Καταγωγή, Εθνικότητες & Γλώσσες (Origins, Nationalities & Languages)"
```

### 2.2 Lesson Schema (`content/unit-XX/lesson-YY.yaml`)

```yaml
unit_id: "unit-01"
lesson_id: "lesson-01"
title: "Χαιρετισμοί & Γνωριμία (Greetings & Introductions)"
description: "CEFR A1: Formal & informal greetings, polite addresses, personal pronouns, and core verbs."
lesson_status: "not_started"   # 'not_started' | 'in_progress' | 'learned'
lesson_notes: |
  Unit 1 Core Grammar Notes:
  • Vocative Singular: Masculine nouns in -ος end in -ε (κύριε Παπαδόπουλε).
  • Copular Verb 'είμαι' (Present): είμαι, είσαι, είναι, είμαστε, είστε, είναι.
entries:
  - id: "A1-U01-001"
    greek: "ο κύριος"
    phonetic_hint: ""
    english: "Mr. / sir / gentleman"
    notes: "Vocative singular drops final -ς and changes to -ε (κύριε)."
    gender_or_pos: "noun (masculine)"
    audio: "o-kyrios-022974.mp3"
    status: "verified"          # 'pending_tts' | 'needs_review' | 'verified'
    example_el: "Γεια σας, κύριε Παπαδόπουλε."
    example_en: "Hello, Mr. Papadopoulos."
    grammatical_info:
      part_of_speech: "noun (masculine)"
      plural: "οι κύριοι"
      accusative_singular: "τον κύριο"
    keg_communicative_function: "Addressing individuals politely and formal introductions"
```

---

## 3. Card Entry Field Definitions & Validation Rules

| Field | Type | Required | Description & Validation Rules |
|---|---|---|---|
| `id` | `string` | **Yes** | Unique identifier (e.g. `A1-U05-001`). Must follow `A1-U{Unit}-{Number:03d}` pattern. |
| `greek` | `string` | **Yes** | Modern Greek text. **Must include valid tonos accents** (normalized NFC). Nouns **must** include the definite article (`ο `, `η `, `το `, `οι `, `τα `). |
| `english` | `string` | **Yes** | Primary English translation. |
| `gender_or_pos` | `string` | **Yes** | Part of speech (`noun (masculine)`, `noun (feminine)`, `noun (neuter)`, `verb`, `phrase`, `adverb`, `preposition`, `adjective`, `numeral`). |
| `audio` | `string \| null` | **Yes** | Deterministic filename in `audio/` (e.g. `o-kyrios-022974.mp3`), or `null` if ungenerated. |
| `status` | `string` | **Yes** | `"pending_tts"`, `"needs_review"`, or `"verified"`. A card is only `"verified"` if the physical `.mp3` file exists and is non-empty. |
| `notes` | `string` | No | Grammar tips, declension notes, or mnemonics shown on card flip. |
| `phonetic_hint` | `string` | No | Optional phonetic pronunciation guide. |
| `example_el` | `string` | No | Natural Greek example sentence illustrating usage. |
| `example_en` | `string` | No | English translation of the example sentence. |
| `grammatical_info` | `object` | No | Structured grammar data (see section 3.1 below). |
| `keg_communicative_function` | `string` | No | CEFR A1 communicative function descriptor. |

### 3.1 Grammatical Info Sub-Rules

To maintain high linguistic standards matching the Centre for the Greek Language (ΚΕΓ / KEG):
1. **Nouns:**
   - Must include `plural` (e.g., `οι καφέδες`, `τα νερά`).
   - Must include `accusative_singular` (e.g., `τον καφέ`, `το νερό`).
2. **Verbs:**
   - Must include `verb_type` (e.g., `Type A (active regular)`, `Type B1`, `irregular`).
   - Must include `third_person_singular` (e.g., `θέλει`, `πίνει`).
   - Must include `first_person_plural` (e.g., `θέλουμε`, `πίνουμε`).
3. **Adjectives:**
   - Must list the three gender endings or feminine and neuter forms (e.g., `ψηλός, -ή, -ό`).

---

## 4. How to Create or Expand Lessons

There are **three supported workflows** depending on how you author content:

### Workflow A: Visual In-App Deck Editor (Interactive GUI)
1. Start the server and frontend:
   ```powershell
   npm run server
   npm run dev
   ```
2. Open `http://localhost:5173` and click the **Deck Editor** tab.
3. Select your Unit and Lesson from the dropdown.
4. Click **Add Card to YAML**, fill in the fields, and click **Save Entry to YAML**.
5. Click **Generate Chirp-3 Audio**:
   - The audio synthesizes in memory and automatically previews.
   - Click **Accept** (green) to write the `.mp3` into `audio/` and mark `status: verified`.

---

### Workflow B: Direct YAML Authoring (Fast Manual Addition)
1. Create a new folder and file in `content/`, for example `content/unit-06/lesson-01.yaml`.
2. Add your card entries using the template above. Leave `audio: null` and `status: "pending_tts"`.
3. Register the unit and lesson in `content/manifest.yaml`.
4. Generate the Chirp-3 audio assets:
   ```powershell
   npm run audio:generate
   ```
   *The script will automatically detect all ungenerated cards, call Google Cloud TTS Chirp-3 HD, write the MP3s to `audio/`, and update the YAML entries in place with `status: verified`.*

---

### Workflow C: Automated Script Generation (Curriculum Generators / AI Agents)
If using an automated python script to generate large curriculum batches:
1. Ensure your script writes directly to `content/unit-XX/lesson-01.yaml` and updates `content/manifest.yaml` (see `scripts/create_unit_05.py` for a reference implementation).
2. If you generate an intermediate JSON batch (`content/keg_a1_units_XX.json`), immediately run the curriculum synchronizer:
   ```powershell
   npm run sync:curriculum
   ```
3. Generate the audio assets:
   ```powershell
   npm run audio:generate
   ```

---

## 5. Audio Generation & Verification

Audio generation is strictly managed by **Google Cloud Text-to-Speech Chirp 3 HD**. 
For full t
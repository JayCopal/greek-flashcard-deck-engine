import os
import shutil
import base64
import yaml
import unicodedata
from pathlib import Path
from typing import Optional, List, Dict, Any
from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from .tts_service import (
    VOICE_CATALOG,
    DEFAULT_VOICE,
    create_preview_session,
    get_preview_session,
    remove_preview_session,
    generate_audio_filename,
)

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / os.getenv("CONTENT_DIR", "content")
AUDIO_DIR = BASE_DIR / os.getenv("AUDIO_OUTPUT_DIR", "audio")
AUDIO_DIR.mkdir(parents=True, exist_ok=True)

app = FastAPI(title="Greek Flashcard Deck Engine API")

# Enable CORS for local dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount audio directory to serve permanent MP3s
app.mount("/audio", StaticFiles(directory=str(AUDIO_DIR)), name="audio")


class NewEntryPayload(BaseModel):
    unit_id: str
    lesson_id: str
    greek: str
    phonetic_hint: Optional[str] = ""
    english: str
    notes: Optional[str] = ""
    gender_or_pos: Optional[str] = "phrase"


class UpdateEntryPayload(BaseModel):
    unit_id: str
    lesson_id: str
    greek: Optional[str] = None
    phonetic_hint: Optional[str] = None
    english: Optional[str] = None
    notes: Optional[str] = None
    gender_or_pos: Optional[str] = None
    status: Optional[str] = None
    audio: Optional[str] = None


class UpdateLessonPayload(BaseModel):
    lesson_notes: Optional[str] = None
    lesson_status: Optional[str] = None  # 'not_started' | 'in_progress' | 'learned'
    title: Optional[str] = None
    description: Optional[str] = None


class TTSPreviewRequest(BaseModel):
    text: str
    voice: Optional[str] = None
    speaking_rate: Optional[float] = 0.9


class TTSAcceptRequest(BaseModel):
    sessionId: str
    entryId: str
    unitId: str
    lessonId: str


class TTSRejectRequest(BaseModel):
    sessionId: Optional[str] = None
    entryId: str
    unitId: str
    lessonId: str


def load_yaml(file_path: Path) -> Dict[str, Any]:
    if not file_path.exists():
        raise HTTPException(status_code=404, detail=f"File not found: {file_path.name}")
    with open(file_path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def save_yaml(file_path: Path, data: Dict[str, Any]) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        yaml.dump(data, f, allow_unicode=True, sort_keys=False, default_flow_style=False)


@app.get("/api/voices")
def get_voices():
    return {
        "voices": VOICE_CATALOG,
        "default": DEFAULT_VOICE,
    }


@app.get("/api/deck")
def get_deck():
    manifest_path = CONTENT_DIR / "manifest.yaml"
    manifest = load_yaml(manifest_path)

    total_entries = 0
    verified_count = 0
    pending_count = 0
    needs_review_count = 0

    units = manifest.get("units", [])
    full_units = []

    for unit in units:
        unit_copy = dict(unit)
        lessons = unit.get("lessons", [])
        full_lessons = []

        unit_entries = 0
        unit_verified = 0

        for lesson_meta in lessons:
            rel_file = lesson_meta.get("file")
            lesson_path = CONTENT_DIR / rel_file
            lesson_data = load_yaml(lesson_path)
            lesson_data.setdefault("lesson_status", "not_started")
            lesson_data.setdefault("lesson_notes", "")

            entries = lesson_data.get("entries", [])
            lesson_entries_count = len(entries)
            lesson_verified_count = 0

            for entry in entries:
                status = entry.get("status", "pending_tts")
                if status == "verified" and entry.get("audio"):
                    # Verify audio file actually exists
                    if (AUDIO_DIR / entry["audio"]).exists():
                        verified_count += 1
                        lesson_verified_count += 1
                    else:
                        entry["status"] = "pending_tts"
                        pending_count += 1
                elif status == "needs_review":
                    needs_review_count += 1
                else:
                    pending_count += 1

            total_entries += lesson_entries_count
            unit_entries += lesson_entries_count
            unit_verified += lesson_verified_count

            lesson_data["total_entries"] = lesson_entries_count
            lesson_data["verified_entries"] = lesson_verified_count
            lesson_data["coverage_percentage"] = (
                round((lesson_verified_count / lesson_entries_count) * 100, 1)
                if lesson_entries_count > 0 else 0.0
            )
            full_lessons.append(lesson_data)

        unit_copy["lessons"] = full_lessons
        unit_copy["total_entries"] = unit_entries
        unit_copy["verified_entries"] = unit_verified
        unit_copy["coverage_percentage"] = (
            round((unit_verified / unit_entries) * 100, 1)
            if unit_entries > 0 else 0.0
        )
        full_units.append(unit_copy)

    coverage = (
        round((verified_count / total_entries) * 100, 1)
        if total_entries > 0 else 0.0
    )

    return {
        "manifest": {
            "deck_title": manifest.get("deck_title", "Modern Greek Deck"),
            "source_language": manifest.get("source_language", "en"),
            "target_language": manifest.get("target_language", "el"),
            "created_at": manifest.get("created_at"),
        },
        "stats": {
            "total_units": len(units),
            "total_lessons": sum(len(u.get("lessons", [])) for u in units),
            "total_entries": total_entries,
            "verified_count": verified_count,
            "pending_count": pending_count,
            "needs_review_count": needs_review_count,
            "coverage_percentage": coverage,
        },
        "units": full_units,
    }


@app.post("/api/entry")
def create_entry(payload: NewEntryPayload):
    manifest = load_yaml(CONTENT_DIR / "manifest.yaml")
    lesson_rel = None
    for unit in manifest.get("units", []):
        if unit.get("id") == payload.unit_id:
            for les in unit.get("lessons", []):
                if les.get("id") == payload.lesson_id:
                    lesson_rel = les.get("file")
                    break

    if not lesson_rel:
        raise HTTPException(status_code=404, detail="Unit or Lesson not found in manifest")

    lesson_path = CONTENT_DIR / lesson_rel
    lesson_data = load_yaml(lesson_path)
    entries = lesson_data.setdefault("entries", [])

    new_id = f"grk-{len(entries) + 1:03d}"
    normalized_greek = unicodedata.normalize("NFC", payload.greek.strip())

    new_entry = {
        "id": new_id,
        "greek": normalized_greek,
        "phonetic_hint": payload.phonetic_hint.strip() if payload.phonetic_hint else "",
        "english": payload.english.strip(),
        "notes": payload.notes.strip() if payload.notes else "",
        "gender_or_pos": payload.gender_or_pos or "phrase",
        "audio": None,
        "status": "pending_tts",
    }
    entries.append(new_entry)
    save_yaml(lesson_path, lesson_data)
    return {"success": True, "entry": new_entry}


@app.put("/api/entry/{entry_id}")
def update_entry(entry_id: str, payload: UpdateEntryPayload):
    manifest = load_yaml(CONTENT_DIR / "manifest.yaml")
    lesson_rel = None
    for unit in manifest.get("units", []):
        if unit.get("id") == payload.unit_id:
            for les in unit.get("lessons", []):
                if les.get("id") == payload.lesson_id:
                    lesson_rel = les.get("file")
                    break

    if not lesson_rel:
        raise HTTPException(status_code=404, detail="Unit or Lesson not found in manifest")

    lesson_path = CONTENT_DIR / lesson_rel
    lesson_data = load_yaml(lesson_path)
    entries = lesson_data.get("entries", [])

    matched = None
    for e in entries:
        if e.get("id") == entry_id:
            matched = e
            break

    if not matched:
        raise HTTPException(status_code=404, detail="Entry ID not found in lesson")

    if payload.greek is not None:
        matched["greek"] = unicodedata.normalize("NFC", payload.greek.strip())
    if payload.phonetic_hint is not None:
        matched["phonetic_hint"] = payload.phonetic_hint.strip()
    if payload.english is not None:
        matched["english"] = payload.english.strip()
    if payload.notes is not None:
        matched["notes"] = payload.notes.strip()
    if payload.gender_or_pos is not None:
        matched["gender_or_pos"] = payload.gender_or_pos
    if payload.status is not None:
        matched["status"] = payload.status
    if payload.audio is not None:
        matched["audio"] = payload.audio

    save_yaml(lesson_path, lesson_data)
    return {"success": True, "entry": matched}


@app.put("/api/lesson/{unit_id}/{lesson_id}")
def update_lesson(unit_id: str, lesson_id: str, payload: UpdateLessonPayload):
    manifest = load_yaml(CONTENT_DIR / "manifest.yaml")
    lesson_rel = None
    for unit in manifest.get("units", []):
        if unit.get("id") == unit_id:
            for les in unit.get("lessons", []):
                if les.get("id") == lesson_id:
                    lesson_rel = les.get("file")
                    break

    if not lesson_rel:
        raise HTTPException(status_code=404, detail="Lesson not found in manifest")

    lesson_path = CONTENT_DIR / lesson_rel
    lesson_data = load_yaml(lesson_path)

    if payload.lesson_notes is not None:
        lesson_data["lesson_notes"] = payload.lesson_notes.strip()
    if payload.lesson_status is not None:
        if payload.lesson_status not in ["not_started", "in_progress", "learned"]:
            raise HTTPException(status_code=400, detail="Invalid lesson status")
        lesson_data["lesson_status"] = payload.lesson_status
    if payload.title is not None:
        lesson_data["title"] = payload.title.strip()
    if payload.description is not None:
        lesson_data["description"] = payload.description.strip()

    save_yaml(lesson_path, lesson_data)
    return {"success": True, "lesson": lesson_data}


@app.post("/api/tts/preview")
def tts_preview(payload: TTSPreviewRequest):
    if not payload.text or not payload.text.strip():
        raise HTTPException(status_code=400, detail="Text cannot be empty")

    try:
        session = create_preview_session(
            text=payload.text,
            voice_name=payload.voice,
            speaking_rate=payload.speaking_rate or 0.9
        )
        audio_b64 = base64.b64encode(session["audioBytes"]).decode("ascii")
        return {
            "sessionId": session["sessionId"],
            "filename": session["filename"],
            "audioBase64": f"data:audio/mp3;base64,{audio_b64}",
        }
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"TTS synthesis failed: {str(exc)}")


@app.post("/api/tts/accept")
def tts_accept(payload: TTSAcceptRequest):
    session = get_preview_session(payload.sessionId)
    if not session:
        raise HTTPException(status_code=404, detail="Preview session expired or not found")

    filename = session["filename"]
    audio_path = AUDIO_DIR / filename

    # Atomically write file
    temp_path = AUDIO_DIR / f"{filename}.tmp"
    with open(temp_path, "wb") as f:
        f.write(session["audio_bytes"])
    temp_path.replace(audio_path)

    # Clean up preview session
    remove_preview_session(payload.sessionId)

    # Update YAML
    manifest = load_yaml(CONTENT_DIR / "manifest.yaml")
    lesson_rel = None
    for unit in manifest.get("units", []):
        if unit.get("id") == payload.unitId:
            for les in unit.get("lessons", []):
                if les.get("id") == payload.lessonId:
                    lesson_rel = les.get("file")
                    break

    if not lesson_rel:
        raise HTTPException(status_code=404, detail="Lesson file not found in manifest")

    lesson_path = CONTENT_DIR / lesson_rel
    lesson_data = load_yaml(lesson_path)
    entries = lesson_data.get("entries", [])

    updated_entry = None
    for e in entries:
        if e.get("id") == payload.entryId:
            e["audio"] = filename
            e["status"] = "verified"
            updated_entry = e
            break

    if not updated_entry:
        raise HTTPException(status_code=404, detail="Entry ID not found in lesson")

    save_yaml(lesson_path, lesson_data)
    return {"success": True, "audio": filename, "entry": updated_entry}


@app.post("/api/tts/reject")
def tts_reject(payload: TTSRejectRequest):
    if payload.sessionId:
        remove_preview_session(payload.sessionId)

    manifest = load_yaml(CONTENT_DIR / "manifest.yaml")
    lesson_rel = None
    for unit in manifest.get("units", []):
        if unit.get("id") == payload.unitId:
            for les in unit.get("lessons", []):
                if les.get("id") == payload.lessonId:
                    lesson_rel = les.get("file")
                    break

    if lesson_rel:
        lesson_path = CONTENT_DIR / lesson_rel
        lesson_data = load_yaml(lesson_path)
        for e in lesson_data.get("entries", []):
            if e.get("id") == payload.entryId:
                e["status"] = "needs_review"
                break
        save_yaml(lesson_path, lesson_data)

    return {"success": True, "status": "needs_review"}


@app.post("/api/export")
def export_pwa():
    """
    Export routine:
    1. Reads manifest & all lessons
    2. Builds dist-pwa/data/deck.json
    3. Copies all referenced verified audio to dist-pwa/audio/
    """
    export_dir = BASE_DIR / "dist-pwa"
    data_dir = export_dir / "data"
    audio_export_dir = export_dir / "audio"

    data_dir.mkdir(parents=True, exist_ok=True)
    audio_export_dir.mkdir(parents=True, exist_ok=True)

    manifest = load_yaml(CONTENT_DIR / "manifest.yaml")
    full_deck = get_deck()

    # Save compiled deck JSON
    import json
    with open(data_dir / "deck.json", "w", encoding="utf-8") as f:
        json.dump(full_deck, f, ensure_ascii=False, indent=2)

    # Copy verified audio
    copied_count = 0
    for unit in full_deck.get("units", []):
        for lesson in unit.get("lessons", []):
            for entry in lesson.get("entries", []):
                audio_name = entry.get("audio")
                if audio_name:
                    src_audio = AUDIO_DIR / audio_name
                    if src_audio.exists():
                        shutil.copy2(src_audio, audio_export_dir / audio_name)
                        copied_count += 1

    return {
        "success": True,
        "message": f"Successfully compiled deck.json and copied {copied_count} audio files to dist-pwa.",
        "exportPath": str(export_dir),
    }

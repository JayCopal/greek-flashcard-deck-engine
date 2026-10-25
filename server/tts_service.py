import os
import re
import uuid
import time
import hashlib
import unicodedata
from pathlib import Path
from typing import Dict, Any, Optional
from dotenv import load_dotenv

load_dotenv()

# Ensure GOOGLE_APPLICATION_CREDENTIALS is set
BASE_DIR = Path(__file__).resolve().parent.parent
creds_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "gcp_credentials.json")
if not os.path.isabs(creds_path):
    creds_path = str(BASE_DIR / creds_path)
if os.path.exists(creds_path):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = creds_path

try:
    from google.cloud import texttospeech
    GCP_TTS_AVAILABLE = True
except ImportError:
    GCP_TTS_AVAILABLE = False

VOICE_CATALOG = [
    {
        "id": "el-GR-Chirp3-HD-Leda",
        "name": "Leda (Female - Default)",
        "gender": "FEMALE",
        "description": "Clear, natural Greek examiner voice. Excellent articulation for learners.",
        "isDefault": True,
    },
    {
        "id": "el-GR-Chirp3-HD-Charon",
        "name": "Charon (Male)",
        "gender": "MALE",
        "description": "Deep, articulate, natural Greek male voice with authentic native cadence.",
        "isDefault": False,
    },
    {
        "id": "el-GR-Chirp3-HD-Puck",
        "name": "Puck (Male)",
        "gender": "MALE",
        "description": "Energetic, conversational Greek male voice.",
        "isDefault": False,
    },
    {
        "id": "el-GR-Chirp3-HD-Aoede",
        "name": "Aoede (Female)",
        "gender": "FEMALE",
        "description": "Melodic, gentle Greek female voice.",
        "isDefault": False,
    },
]

DEFAULT_VOICE = os.getenv("DEFAULT_VOICE", "el-GR-Chirp3-HD-Leda")
DEFAULT_SPEAKING_RATE = 0.9

# In-memory preview buffer (sessionId -> { audio_bytes, greek_text, voice, created_at })
preview_sessions: Dict[str, Dict[str, Any]] = {}


GREEK_TRANSLIT = {
    'α': 'a', 'β': 'v', 'γ': 'g', 'δ': 'd', 'ε': 'e', 'ζ': 'z', 'η': 'i', 'θ': 'th',
    'ι': 'i', 'κ': 'k', 'λ': 'l', 'μ': 'm', 'ν': 'n', 'ξ': 'x', 'ο': 'o', 'π': 'p',
    'ρ': 'r', 'σ': 's', 'ς': 's', 'τ': 't', 'υ': 'y', 'φ': 'f', 'χ': 'ch', 'ψ': 'ps',
    'ω': 'o',
}


def generate_audio_filename(greek_text: str) -> str:
    """
    Deterministic audio naming:
    - Normalizes to NFC
    - Strips diacritics and transliterates to Latin for cross-platform safe filesystem slug (e.g. kalimera-3a7f8e.mp3)
    - Preserves NFC text for SHA256 hash
    """
    text_nfc = unicodedata.normalize("NFC", greek_text.strip())
    
    # Remove diacritics for the slug
    nfd = unicodedata.normalize("NFD", text_nfc)
    without_accents = "".join(c for c in nfd if unicodedata.category(c) != "Mn").lower()
    
    # Transliterate Greek characters to Latin
    latin_chars = [GREEK_TRANSLIT.get(c, c) for c in without_accents]
    latin_str = "".join(latin_chars)
    
    slug = re.sub(r'[^a-z0-9]', '-', latin_str)
    slug = re.sub(r'-+', '-', slug).strip('-')[:20]
    if not slug:
        slug = "greek"

    # Hash original Unicode text with accents
    hash_code = hashlib.sha256(text_nfc.encode("utf-8")).hexdigest()[:6]
    return f"{slug}-{hash_code}.mp3"


def synthesize_greek_chirp(
    text: str,
    voice_name: Optional[str] = None,
    speaking_rate: float = DEFAULT_SPEAKING_RATE
) -> bytes:
    """
    Synthesize speech using Google Cloud TTS Chirp 3 HD Greek voices.
    """
    if not GCP_TTS_AVAILABLE:
        raise RuntimeError("google-cloud-texttospeech library is not available.")

    selected_voice = voice_name or DEFAULT_VOICE

    client = texttospeech.TextToSpeechClient()

    # Greek text must always be NFC normalized
    normalized_text = unicodedata.normalize("NFC", text.strip())

    synthesis_input = texttospeech.SynthesisInput(text=normalized_text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="el-GR",
        name=selected_voice,
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=speaking_rate,
        sample_rate_hertz=24000,
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config,
    )

    return response.audio_content


def create_preview_session(text: str, voice_name: Optional[str] = None, speaking_rate: float = DEFAULT_SPEAKING_RATE) -> Dict[str, Any]:
    # Prune sessions older than 30 minutes
    now = time.time()
    stale_keys = [k for k, v in preview_sessions.items() if now - v["created_at"] > 1800]
    for k in stale_keys:
        preview_sessions.pop(k, None)

    audio_bytes = synthesize_greek_chirp(text, voice_name, speaking_rate)
    session_id = str(uuid.uuid4())
    filename = generate_audio_filename(text)

    preview_sessions[session_id] = {
        "audio_bytes": audio_bytes,
        "greek_text": text,
        "voice": voice_name or DEFAULT_VOICE,
        "filename": filename,
        "created_at": now,
    }

    return {
        "sessionId": session_id,
        "filename": filename,
        "audioBytes": audio_bytes,
    }


def get_preview_session(session_id: str) -> Optional[Dict[str, Any]]:
    return preview_sessions.get(session_id)


def remove_preview_session(session_id: str) -> None:
    preview_sessions.pop(session_id, None)

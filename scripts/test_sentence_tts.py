# -*- coding: utf-8 -*-
"""
Test Chirp-3 HD audio synthesis on an example sentence.
"""
import sys
import os
import hashlib
import unicodedata
import re
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

from server.tts_service import synthesize_greek_chirp, generate_audio_filename

sample_sentence = "Γεια σας, κύριε Παπαδόπουλε. Πώς είστε σήμερα;"
fn = generate_audio_filename(sample_sentence)
print(f"Generated filename: {fn}")

print("Synthesizing test sentence with Chirp-3 HD...")
audio_bytes = synthesize_greek_chirp(sample_sentence)
print(f"Successfully synthesized {len(audio_bytes)} bytes!")

test_out = BASE_DIR / "audio" / fn
with open(test_out, "wb") as f:
    f.write(audio_bytes)
print(f"Saved to {test_out.name}")

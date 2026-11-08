# -*- coding: utf-8 -*-
"""
Full Verification Script for KEG A1 Flashcards:
Verifies that 100% of cards in Units 00-12 have two valid example sentences
with accompanying, non-empty Chirp-3 HD audio files on disk.
"""
import sys
import yaml
from pathlib import Path

if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(__file__).resolve().parent.parent
CONTENT_DIR = BASE_DIR / "content"
AUDIO_DIR = BASE_DIR / "audio"

UNITS = [f"unit-{i:02d}" for i in range(13)]

def verify():
    total_cards = 0
    missing_ex1 = []
    missing_ex2 = []
    missing_audio_head = []
    missing_audio_ex1 = []
    missing_audio_ex2 = []
    
    print("=" * 60)
    print("KEG A1 COMPREHENSIVE CARD & AUDIO AUDIT")
    print("=" * 60)
    
    for uid in UNITS:
        yp = CONTENT_DIR / uid / "lesson-01.yaml"
        if not yp.exists():
            print(f"[MISSING UNIT] {yp}")
            continue
            
        with open(yp, "r", encoding="utf-8") as f:
            yd = yaml.safe_load(f)
            
        entries = yd.get("entries", [])
        u_count = len(entries)
        total_cards += u_count
        
        u_ex1_ok = 0
        u_ex2_ok = 0
        u_aud_ex1_ok = 0
        u_aud_ex2_ok = 0
        
        for e in entries:
            cid = e["id"]
            
            # Headword audio
            h_aud = e.get("audio")
            if not h_aud or not (AUDIO_DIR / h_aud).exists() or (AUDIO_DIR / h_aud).stat().st_size == 0:
                missing_audio_head.append((cid, h_aud))
                
            # Ex 1
            ex1_el = e.get("example_el", "").strip()
            ex1_en = e.get("example_en", "").strip()
            ex1_aud = e.get("example_audio")
            if ex1_el and ex1_en:
                u_ex1_ok += 1
            else:
                missing_ex1.append(cid)
                
            if ex1_aud and (AUDIO_DIR / ex1_aud).exists() and (AUDIO_DIR / ex1_aud).stat().st_size > 0:
                u_aud_ex1_ok += 1
            else:
                missing_audio_ex1.append((cid, ex1_aud))
                
            # Ex 2
            ex2_el = e.get("example2_el", "").strip()
            ex2_en = e.get("example2_en", "").strip()
            ex2_aud = e.get("example2_audio")
            if ex2_el and ex2_en:
                u_ex2_ok += 1
            else:
                missing_ex2.append(cid)
                
            if ex2_aud and (AUDIO_DIR / ex2_aud).exists() and (AUDIO_DIR / ex2_aud).stat().st_size > 0:
                u_aud_ex2_ok += 1
            else:
                missing_audio_ex2.append((cid, ex2_aud))
                
        print(f"{uid:8} | Cards: {u_count:3} | Ex1: {u_ex1_ok:3}/{u_count:3} | Ex2: {u_ex2_ok:3}/{u_count:3} | AudioEx1: {u_aud_ex1_ok:3}/{u_count:3} | AudioEx2: {u_aud_ex2_ok:3}/{u_count:3}")

    print("=" * 60)
    print(f"Total Cards Audited: {total_cards}")
    print(f"Missing Sentence 1: {len(missing_ex1)}")
    print(f"Missing Sentence 2: {len(missing_ex2)}")
    print(f"Missing Headword Audio: {len(missing_audio_head)}")
    print(f"Missing Ex1 Audio: {len(missing_audio_ex1)}")
    print(f"Missing Ex2 Audio: {len(missing_audio_ex2)}")
    print("=" * 60)
    
    if not (missing_ex1 or missing_ex2 or missing_audio_head or missing_audio_ex1 or missing_audio_ex2):
        print("ALL CHECKS PASSED: 100% of cards have 2 valid example sentences and full audio coverage!")
        return 0
    else:
        print("[WARN] Some cards require attention.")
        return 1

if __name__ == "__main__":
    sys.exit(verify())

#!/usr/bin/env python3
"""
Static Mobile PWA Export Script
- Reads content/manifest.yaml & lesson YAML files
- Compiles unified dist-pwa/data/deck.json
- Copies all verified audio from audio/ to dist-pwa/audio/
- Runs Vite build to generate the production PWA bundle in dist-pwa/
"""
import os
import sys
import json
import shutil
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))
CONTENT_DIR = BASE_DIR / "content"
AUDIO_DIR = BASE_DIR / "audio"
DIST_PWA = BASE_DIR / "dist-pwa"


def export():
    print("==> Starting Static Mobile PWA Export...")
    
    # 1. First run vite build if package.json has build script
    if (BASE_DIR / "package.json").exists():
        print("==> Building Vite production assets...")
        res = subprocess.run("npm run build", cwd=str(BASE_DIR), shell=True)
        if res.returncode != 0:
            print("Error: npm run build failed.")
            sys.exit(res.returncode)

    # 2. Prepare dist-pwa directory
    # Copy from dist to dist-pwa if dist exists
    dist_dir = BASE_DIR / "dist"
    if dist_dir.exists():
        if DIST_PWA.exists():
            shutil.rmtree(DIST_PWA)
        shutil.copytree(dist_dir, DIST_PWA)
    else:
        DIST_PWA.mkdir(parents=True, exist_ok=True)

    data_dir = DIST_PWA / "data"
    audio_dir = DIST_PWA / "audio"
    data_dir.mkdir(parents=True, exist_ok=True)
    audio_dir.mkdir(parents=True, exist_ok=True)

    # 3. Compile deck.json
    from server.main import get_deck
    deck_data = get_deck()
    with open(data_dir / "deck.json", "w", encoding="utf-8") as f:
        json.dump(deck_data, f, ensure_ascii=False, indent=2)
    print(f"==> Wrote compiled deck data to {data_dir / 'deck.json'}")

    # 4. Copy verified audio
    copied = 0
    for unit in deck_data.get("units", []):
        for lesson in unit.get("lessons", []):
            for entry in lesson.get("entries", []):
                audio_file = entry.get("audio")
                if audio_file:
                    src = AUDIO_DIR / audio_file
                    if src.exists():
                        shutil.copy2(src, audio_dir / audio_file)
                        copied += 1

    print(f"==> Copied {copied} verified audio files into {audio_dir}")
    print("\n[OK] PWA Export Complete! Folder is ready in: dist-pwa/")
    print("   To test locally: npx serve dist-pwa")
    print("   Deploy dist-pwa/ to Cloudflare Pages, GitHub Pages, or any static host.")


if __name__ == "__main__":
    export()

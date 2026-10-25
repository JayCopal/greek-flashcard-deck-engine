"""
Script to generate standard and maskable PWA icons for GreekDeck.
Generates:
- public/pwa-192x192.png
- public/pwa-512x512.png
- public/pwa-maskable-512x512.png
- public/apple-touch-icon.png
- public/favicon.ico
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

PUBLIC_DIR = Path(__file__).resolve().parent.parent / "public"
PUBLIC_DIR.mkdir(parents=True, exist_ok=True)

def create_base_icon(size: int, is_maskable: bool = False) -> Image.Image:
    # 512 base canvas
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(canvas)

    bg_color = (2, 132, 199, 255)  # #0284c7 (Sky-600)
    
    if is_maskable:
        # Full edge-to-edge background for adaptive masking
        draw.rectangle([0, 0, size, size], fill=bg_color)
        font_size = int(size * 0.45) # safe zone is central 60-80%
    else:
        # Rounded rectangle for standard icon
        radius = int(size * 0.22)
        draw.rounded_rectangle([0, 0, size, size], radius=radius, fill=bg_color)
        font_size = int(size * 0.55)

    try:
        font = ImageFont.truetype("times.ttf", font_size)
    except Exception:
        font = ImageFont.load_default()

    text = "Ω"
    bbox = draw.textbbox((0, 0), text, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    # Center text perfectly
    x = (size - text_w) / 2 - bbox[0]
    y = (size - text_h) / 2 - bbox[1] - (size * 0.02) # slight optical adjustment

    # Draw subtle shadow for depth
    draw.text((x, y + (size * 0.015)), text, font=font, fill=(3, 105, 161, 160))
    # Draw primary glyph
    draw.text((x, y), text, font=font, fill=(255, 255, 255, 255))

    return canvas

def generate_all():
    print("Generating PWA icons...")
    
    # 512 standard
    icon_512 = create_base_icon(512, is_maskable=False)
    icon_512.save(PUBLIC_DIR / "pwa-512x512.png", "PNG")
    print(f"Saved {PUBLIC_DIR / 'pwa-512x512.png'}")

    # 192 standard
    icon_192 = icon_512.resize((192, 192), Image.Resampling.LANCZOS)
    icon_192.save(PUBLIC_DIR / "pwa-192x192.png", "PNG")
    print(f"Saved {PUBLIC_DIR / 'pwa-192x192.png'}")

    # 512 maskable (edge to edge background, safe-zone symbol)
    icon_maskable = create_base_icon(512, is_maskable=True)
    icon_maskable.save(PUBLIC_DIR / "pwa-maskable-512x512.png", "PNG")
    print(f"Saved {PUBLIC_DIR / 'pwa-maskable-512x512.png'}")

    # Apple touch icon 180x180 (no transparent corners, iOS handles rounding)
    apple_icon = create_base_icon(180, is_maskable=True)
    apple_icon.save(PUBLIC_DIR / "apple-touch-icon.png", "PNG")
    print(f"Saved {PUBLIC_DIR / 'apple-touch-icon.png'}")

    # Favicon.ico (contains 16, 32, 48)
    icon_48 = icon_512.resize((48, 48), Image.Resampling.LANCZOS)
    icon_48.save(PUBLIC_DIR / "favicon.ico", format="ICO", sizes=[(16, 16), (32, 32), (48, 48)])
    print(f"Saved {PUBLIC_DIR / 'favicon.ico'}")

if __name__ == "__main__":
    generate_all()

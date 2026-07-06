from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "img" / "research-map.png"


def draw_visual():
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    w, h = 980, 760
    img = Image.new("RGB", (w, h), "#f8faf9")
    draw = ImageDraw.Draw(img)

    # Soft background bands.
    for i, color in enumerate(["#dce9e5", "#efe4d9", "#e5eee7", "#edf2f0"]):
        y0 = 70 + i * 145
        draw.rounded_rectangle((80, y0, w - 80, y0 + 92), radius=34, fill=color)

    nodes = [
        ("#14665f", 230, 170, 64),
        ("#a35c2a", 710, 205, 58),
        ("#477a5b", 315, 510, 54),
        ("#213b3a", 675, 545, 66),
        ("#6b7f7a", 500, 360, 78),
    ]

    lines = [
        ((230, 170), (500, 360), "#14665f"),
        ((710, 205), (500, 360), "#a35c2a"),
        ((315, 510), (500, 360), "#477a5b"),
        ((675, 545), (500, 360), "#213b3a"),
        ((230, 170), (315, 510), "#879994"),
        ((710, 205), (675, 545), "#879994"),
    ]

    overlay = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    for (x1, y1), (x2, y2), color in lines:
        od.line((x1, y1, x2, y2), fill=color + "88", width=12)
        od.line((x1, y1, x2, y2), fill="#ffffffcc", width=4)
    overlay = overlay.filter(ImageFilter.GaussianBlur(0.2))
    img = Image.alpha_composite(img.convert("RGBA"), overlay)
    draw = ImageDraw.Draw(img)

    for color, x, y, r in nodes:
        draw.ellipse((x - r - 11, y - r - 11, x + r + 11, y + r + 11), fill="#ffffffcc")
        draw.ellipse((x - r, y - r, x + r, y + r), fill=color)
        draw.ellipse((x - r + 16, y - r + 16, x + r - 16, y + r - 16), fill="#ffffff22", outline="#ffffff99", width=3)

    for x, y, r in [(155, 430, 8), (820, 390, 10), (510, 120, 7), (455, 615, 9), (820, 600, 6)]:
        draw.ellipse((x - r, y - r, x + r, y + r), fill="#a35c2a")

    img = img.convert("RGB")
    img.save(OUTPUT, optimize=True, quality=95)


if __name__ == "__main__":
    draw_visual()

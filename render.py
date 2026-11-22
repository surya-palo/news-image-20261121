#!/usr/bin/env python3
"""Render the news-image-20261121 poster: a 1024x1024 newspaper-style
summary of the world news of Saturday 21 November 2026.

Build-time tool only (uses Pillow, which is NOT part of the entry
program). The entry itself is entry.png plus main.py, which copies it.
Run:  python3 render.py   (writes entry.png next to this file)
"""
import textwrap
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (246, 241, 231)
INK = (26, 26, 26)
RED = (163, 22, 33)
GREY = (90, 86, 78)
RULE = (26, 26, 26)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap returning a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, leading):
    for ln in lines:
        draw.text((x, y), ln, font=fnt, fill=fill)
        y += leading
    return y


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # Frame
    d.rectangle([8, 8, W - 9, H - 9], outline=INK, width=3)
    d.rectangle([16, 16, W - 17, H - 17], outline=INK, width=1)

    mx = 40                      # left/right margin
    cw = W - 2 * mx              # content width = 944

    # ---- Masthead -------------------------------------------------
    y = 28
    f_title = font(SERIF_B, 54)
    title = "THE WORLD IN ONE DAY"
    d.text(((W - d.textlength(title, font=f_title)) / 2, y),
           title, font=f_title, fill=INK)
    y += 64
    f_date = font(SANS_B, 28)
    date = "SATURDAY, 21 NOVEMBER 2026"
    d.text(((W - d.textlength(date, font=f_date)) / 2, y),
           date, font=f_date, fill=RED)
    y += 38
    d.line([(mx, y), (W - mx, y)], fill=RULE, width=3)
    d.line([(mx, y + 5), (W - mx, y + 5)], fill=RULE, width=1)
    y += 16

    # ---- Lead story ----------------------------------------------
    f_kick = font(SANS_B, 19)
    d.text((mx, y), "LEAD STORY  ·  KYIV AND WARSAW",
           font=f_kick, fill=RED)
    y += 26
    f_head = font(SERIF_B, 42)
    head = "Russian missiles strike Kyiv — and land in Poland"
    lines = wrap(d, head, f_head, cw)
    assert len(lines) == 2, f"lead headline wrapped to {len(lines)} lines"
    y = draw_lines(d, lines, mx, y, f_head, INK, 50)
    y += 4
    f_body = font(SANS, 22)
    body = ("Russia fired more than 400 drones and 110 missiles at Ukraine "
            "overnight, killing at least eight people in Kyiv. Two Russian "
            "missiles and a suspected drone came down in Poland; Prime "
            "Minister Tusk called it a deliberate provocation.")
    lines = wrap(d, body, f_body, cw)
    assert len(lines) <= 4, f"lead body wrapped to {len(lines)} lines"
    y = draw_lines(d, lines, mx, y, f_body, INK, 28)
    y += 10
    d.line([(mx, y), (W - mx, y)], fill=RULE, width=2)
    y += 12

    # ---- Story cards, 2 columns x 3 rows -------------------------
    gap = 20
    col_w = (cw - gap) // 2
    row_h = 164
    row_gap = 12
    cards = [
        ("MARKETS",
         "AI sell-off drags S&P 500 into correction",
         "US stocks fell sharply on Friday: the S&P 500 dropped 3.7% and "
         "the Nasdaq lost 5.3%, wiping out its gains for 2026."),
        ("BRITAIN & EUROPE",
         "UK and EU sign three deals in biggest step since Brexit",
         "Trade, emissions and youth-mobility deals: 100,000 young "
         "Britons gain the right to live, work and study in the EU."),
        ("SUMMIT FALLOUT",
         "Trump calls Putin \u201cmy friend\u201d; Zelenskyy answers: \u201ckiller\u201d",
         "After the Shenzhen summit with Putin and Xi, Trump defended his "
         "ties to both; Kyiv warned against a deal on Moscow\u2019s terms."),
        ("CLIMATE",
         "COP31 deadlocked over fossil fuels; talks extended",
         "Negotiators failed to agree on phasing out fossil fuels, and the "
         "summit was extended as a preliminary deal was discussed."),
        ("MIDDLE EAST",
         "Houthi missiles aimed at Riyadh shot down",
         "The Saudi-led coalition intercepted three ballistic missiles "
         "headed for the capital, the third night of alerts in a row."),
        ("PERU",
         "Magnitude 6.9 earthquake shakes Peru\u2019s Andes",
         "The quake struck near Ondores at 00:09 UTC and was felt in Lima; "
         "no casualties or damage were immediately reported."),
    ]
    f_tag = font(SANS_B, 17)
    f_chead = font(SERIF_B, 25)
    f_cbody = font(SANS, 19)
    for i, (tag, chead, cbody) in enumerate(cards):
        cx = mx + (i % 2) * (col_w + gap)
        cy = y + (i // 2) * (row_h + row_gap)
        d.rectangle([cx, cy, cx + col_w, cy + row_h],
                    outline=GREY, width=1)
        ix, iy = cx + 14, cy + 11
        iw = col_w - 28
        d.text((ix, iy), tag, font=f_tag, fill=RED)
        iy += 24
        hlines = wrap(d, chead, f_chead, iw)
        assert len(hlines) <= 2, f"card {i} headline: {len(hlines)} lines"
        iy = draw_lines(d, hlines, ix, iy, f_chead, INK, 28)
        iy += 3
        blines = wrap(d, cbody, f_cbody, iw)
        assert len(blines) <= 3, f"card {i} body: {len(blines)} lines"
        draw_lines(d, blines, ix, iy, f_cbody, INK, 22)
    y += 3 * row_h + 2 * row_gap
    y += 10
    d.line([(mx, y), (W - mx, y)], fill=RULE, width=2)
    y += 10

    # ---- Also today ----------------------------------------------
    f_also = font(SANS_B, 18)
    f_also_b = font(SANS, 18)
    also = ("ALSO TODAY:  Pancreatic-cancer pill trial: tumours undetectable "
            "in 1 in 12 patients  ·  Fire at a Basra power plant kills at "
            "least four.")
    lines = wrap(d, also, f_also_b, cw)
    assert len(lines) <= 2, f"also-today wrapped to {len(lines)} lines"
    y = draw_lines(d, lines, mx, y, f_also_b, INK, 23)
    y += 7

    # ---- Footer ----------------------------------------------------
    f_foot = font(SANS, 15)
    foot = ("Stories happened or were first reported on 21 Nov 2026  ·  "
            "Sources: BBC, AP, Al Jazeera, Reuters, FT, Guardian")
    flines = wrap(d, foot, f_foot, cw)
    assert len(flines) <= 2, f"footer wrapped to {len(flines)} lines"
    y = draw_lines(d, flines, mx, y, f_foot, GREY, 20)
    assert y <= H - 26, f"content overflows: y={y}"

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()

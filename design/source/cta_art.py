# -*- coding: utf-8 -*-
"""Call-to-action illustrations, direction AB: the campus drawing used for the three things a reader can ask for.
Visit: the Corelith kombi at the admin block, two of us walking in with a laptop, the Head at the door.
Price: the bursar's desk, the laptop showing US$1,140 and the printed price sheet.
Training: the staffroom, teachers round the table, the trainer at the screen."""
import iso_campus as ISO
from iso_campus import I, P, poly, line, box, fl, fr, top, shadow, person, kid, WALL, PALE, ROOF, GLASS, HAIR, BLUE
from portal_art import setup, slab, DEFS, FLOOR, BOARD, GROUND
from common import ic, SANS

PAVED = ("#f6f7f9", "#e6e9ee", "#d8dce3")
DESK = ("#f7f3ea", "#e6dccb", "#d8ccb7")


def laptop(x, y, z, w=0.5, d=0.34):
    out = box(x, y, w, d, 0.03, z, ("#d4d9e0", "#bcc3cf", "#aab1bd"), lip=False)
    out += poly(fl(x + 0.02, x + w - 0.02, y + 0.04, z + 0.03, z + 0.36), "#3a404c", HAIR, 0.4)
    out += poly(fl(x + 0.05, x + w - 0.05, y + 0.04, z + 0.06, z + 0.33), BLUE, "none")
    return out


def cutaway(x0, y0, x1, y1, h, floor=FLOOR):
    out = poly(top(x0, y0, x1 - x0, y1 - y0, 0.02), floor[0], HAIR, 0.5)
    out += box(x0 - 0.15, y0 - 0.15, x1 - x0 + 0.15, 0.15, h, 0, WALL)
    out += box(x0 - 0.15, y0, 0.15, y1 - y0, h, 0, WALL)
    return out


def scene_visit():
    W, D = 9.0, 5.5
    out = slab(W, D, PAVED)
    out += poly(top(0, 3.4, W, 1.1, 0.003), "#eceef2", "none")                            # the drive
    svg, anc = ISO.admin(3.2, 0.6, 2.8, 1.6, 1.5)
    out += svg
    out += person(4.55, 2.6, "#3a404c")                                                   # the Head at the door
    out += person(3.7, 3.15, BLUE) + person(4.0, 3.35, BLUE)                              # two of us, one with the laptop
    out += box(3.8, 3.2, 0.16, 0.05, 0.12, 0.28, ("#3a404c", "#3a404c", "#2e333d"), lip=False)
    out += ISO.kombi(0.7, 3.55)
    out += ISO.jtree(7.4, 1.4, 0.95, ISO.JAC) + ISO.jtree(8.2, 3.9, 0.8, "green") + ISO.jtree(1.4, 1.2, 0.8, "green")
    labels = [("calendar", "Demo at your school", ("Your forms", "Your fee structure"), *P(*anc))]
    return out, labels


def scene_price():
    W, D = 6.6, 4.4
    out = slab(W, D, GROUND["Administration"])
    x0, y0, x1, y1, h = 0.7, 0.5, 6.0, 3.8, 1.05
    out += cutaway(x0, y0, x1, y1, h, ("#f1f2f5", "#e3e6eb", "#d6dae1"))
    out += poly(fl(x0 + 0.7, x0 + 2.1, y0, 0.32, 0.82), GLASS, HAIR, 0.5)                 # the counter window
    out += box(x0 + 0.6, y0, 1.6, 0.25, 0.05, 0.3, PALE, lip=False)
    out += poly(fl(x0 + 2.6, x0 + 3.6, y0, 0.4, 0.82), "#f7f3ea", HAIR, 0.5)             # fees notice
    for r in range(3):
        out += line((x0 + 2.7, y0, 0.74 - r * 0.11), (x0 + 3.5, y0, 0.74 - r * 0.11), "rgba(20,24,36,0.2)", 0.6)
    out += box(x0 + 0.1, y0 + 0.6, 0.5, 0.9, 0.6, 0, ("#e9ecf0", "#d4d9e0", "#c3c9d3"))  # filing cabinet
    dx, dy = x0 + 1.6, y0 + 1.2
    out += box(dx, dy, 2.4, 1.1, 0.36, 0, DESK)                                          # the bursar's desk
    out += laptop(dx + 0.35, dy + 0.3, 0.36, 0.62, 0.4)
    out += box(dx + 1.3, dy + 0.35, 0.42, 0.55, 0.012, 0.36, ("#ffffff", "#e5e8ed", "#d4d9e0"), lip=False)   # price sheet
    for r in range(4):
        out += line((dx + 1.36, dy + 0.42 + r * 0.11, 0.375), (dx + 1.66, dy + 0.42 + r * 0.11, 0.375), "rgba(20,24,36,0.25)", 0.5)
    out += person(dx + 1.0, dy + 1.35, "#6f7a8c")                                        # the bursar
    labels = [("download-2", "Price sheet (PDF)", ("1,140 active pupils", "US$1,140 a month"), *P(x0 + 1.4, y0, 0.92))]
    return out, labels


def scene_training():
    W, D = 8.0, 5.0
    out = slab(W, D, GROUND["Teacher"])
    x0, y0, x1, y1, h = 1.2, 0.6, 6.8, 4.2, 1.05
    out += cutaway(x0, y0, x1, y1, h)
    out += poly(fl(x0 + 1.4, x0 + 3.6, y0, 0.34, 0.9), "#3a404c", HAIR, 0.6)             # the screen
    out += poly(fl(x0 + 1.5, x0 + 3.5, y0, 0.4, 0.84), "#ffffff", "none")
    out += poly(fl(x0 + 1.6, x0 + 2.2, y0, 0.48, 0.78), "#e8effd", "none")
    out += poly(fl(x0 + 2.35, x0 + 3.4, y0, 0.66, 0.76), BLUE, "none")
    out += line((x0 + 2.35, y0, 0.58), (x0 + 3.2, y0, 0.58), "#c3c9d3", 1.2)
    out += line((x0 + 2.35, y0, 0.5), (x0 + 3.0, y0, 0.5), "#c3c9d3", 1.2)
    for k in range(4):                                                                   # pigeonholes on the left wall
        out += poly(fr(x0, y0 + 0.5 + k * 0.32, y0 + 0.78 + k * 0.32, 0.4, 0.62), "#e9dcc6", HAIR, 0.4)
    out += person(x0 + 4.0, y0 + 0.9, BLUE)                                             # the trainer
    tx, ty = x0 + 1.4, y0 + 1.8
    seats = [(tx + 0.4, ty - 0.15), (tx + 1.2, ty - 0.15), (tx + 2.0, ty - 0.15), (tx + 0.4, ty + 1.35), (tx + 1.2, ty + 1.35), (tx + 2.0, ty + 1.35), (tx + 2.95, ty + 0.6)]
    tones = ("#6f7a8c", "#8f98a8", "#3a404c", "#6f7a8c", "#8f98a8", "#6f7a8c", "#3a404c")
    for (sx, sy), t in zip(seats[:3], tones):
        out += person(sx, sy, t)
    out += box(tx, ty, 2.6, 1.1, 0.34, 0, DESK)                                          # staffroom table
    out += laptop(tx + 0.3, ty + 0.3, 0.34, 0.5, 0.32) + laptop(tx + 1.6, ty + 0.3, 0.34, 0.5, 0.32)
    for (sx, sy), t in zip(seats[3:], tones[3:]):
        out += person(sx, sy, t)
    labels = [("presentation-2", "Training at your school", ("Weeks 1–2 setup", "Weeks 3–4 training"), *P(x0 + 2.5, y0, 1.0))]
    return out, labels


SCENES = {"visit": scene_visit, "price": scene_price, "training": scene_training}
PLATES = {"visit": (9.0, 5.5), "price": (6.6, 4.4), "training": (8.0, 5.0)}
USCALE = {"visit": 1.0, "price": 1.18, "training": 1.0}


def pills(labels):
    PILL = ("display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 11px 0 4px;border:1px solid #e7e9ef;border-radius:999px;background:#fff;"
            "box-shadow:0 6px 14px -8px rgba(15,20,35,.35);font:500 12.5px 'Atkinson Hyperlegible Next',sans-serif;color:#0b0c14;white-space:nowrap")
    CHIP = ("display:inline-flex;align-items:center;height:22px;padding:0 8px;border-radius:999px;background:#f1f3f6;border:1px solid #e3e6eb;"
            "font:500 11.5px 'Atkinson Hyperlegible Next',sans-serif;color:#3b3d47;white-space:nowrap")
    out = ""
    for icon, text, chips, ax, ay in labels:
        stem = 22
        tile = f'<span style="width:22px;height:22px;border-radius:11px;background:#2563eb;display:flex;align-items:center;justify-content:center">{ic(icon, 12, "#fff")}</span>'
        out += (f'<span style="position:absolute;left:{ax - 0.5:.1f}px;top:{ay - stem:.0f}px;width:1px;height:{stem}px;background:#9aa1ad"></span>'
                f'<span style="position:absolute;left:{ax - 3:.1f}px;top:{ay - 3:.1f}px;width:6px;height:6px;border-radius:3px;background:#fff;border:1.5px solid #0b0c14;box-sizing:border-box"></span>'
                f'<span style="position:absolute;left:{ax:.0f}px;top:{ay - stem - 30:.0f}px;transform:translateX(-50%);display:flex;gap:5px;align-items:center">'
                f'<span style="{PILL}">{tile}{text}</span>' + "".join(f'<span style="{CHIP}">{c}</span>' for c in chips) + '</span>')
    return out


def cta_scene(kind, w=560, h=400, U=40, cx=None, cy=None, labels=True):
    W, D = PLATES[kind]
    U = U * USCALE[kind]
    setup(W, D, U, cx if cx is not None else w / 2, cy if cy is not None else h * 0.6)
    svg, lab = SCENES[kind]()
    out = (f'<div style="position:relative;width:{w}px;height:{h}px">'
           f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="position:absolute;left:0;top:0" aria-hidden="true">{DEFS}{svg}</svg>')
    if labels:
        out += pills(lab)
    return out + '</div>'

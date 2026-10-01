# -*- coding: utf-8 -*-
"""Department and school-type drawings, direction AB revised (type-led plus illustration).
Each department of Campus is one small place in the school on its own plate, in the campus projection,
with one blue thing in it. School types are the building that tells them apart."""
import iso_campus as ISO
from iso_campus import I, P, poly, line, box, fl, fr, top, sign, shadow, win_f, win_s, gable, person, kid, WALL, PALE, DARK, ROOF, GLASS, HAIR, BLUE
from portal_art import setup, slab, DEFS, FLOOR, BOARD, ROOF_GREY
from cta_art import laptop, DESK

PLATE = ("#f6f7f9", "#e6e9ee", "#d8dce3")
GRASS = ("#eef3e9", "#dde7d4", "#cfdbc4")
PAPER = ("#ffffff", "#e5e8ed", "#d4d9e0")
TRUNK = ("#5b8cf3", "#3469e0", "#2853c2")
W0, D0 = 4.4, 3.0


def desk(x, y, w=0.7, d=0.42, h=0.3):
    return box(x, y, w, d, h, 0, DESK, lip=False)


def books(x, y, z, n=3, w=0.32, d=0.24, blue=1):
    out = ""
    for i in range(n):
        f = TRUNK if i == blue else PAPER
        out += box(x + (i % 2) * 0.02, y, w, d, 0.05, z + i * 0.05, f, lip=False)
    return out


# ---- departments -----------------------------------------------------------------------------------
def d_academics():
    out = slab(W0, D0, PLATE)
    out += poly(top(0.4, 0.3, 3.6, 2.4, 0.01), FLOOR[0], HAIR, 0.4)
    out += box(1.0, 0.35, 2.0, 0.06, 0.85, 0.22, ("#2b3631", BOARD, "#26302b"), lip=False)    # chalkboard on its frame
    out += box(0.95, 0.38, 0.06, 0.06, 1.1, 0, DARK, lip=False) + box(2.99, 0.38, 0.06, 0.06, 1.1, 0, DARK, lip=False)
    for k in range(3):
        out += line((1.15, 0.41, 0.85 - k * 0.15), (1.15 + 0.9 - k * 0.2, 0.41, 0.85 - k * 0.15), "rgba(255,255,255,.55)", 0.9)
    out += person(3.4, 0.95, BLUE)                                                       # the teacher with her tablet
    for r, yy in enumerate((1.25, 1.95)):
        for c, xx in enumerate((0.9, 1.9)):
            out += desk(xx, yy)
            out += books(xx + 0.18, yy + 0.08, 0.3, 2, 0.28, 0.2, blue=(1 if (r + c) % 3 == 0 else 9))
            out += kid(xx + 0.35, yy + 0.62, ("#6f7a8c", "#8f98a8", "#3a404c", "#6f7a8c")[r * 2 + c])
    return out


def d_admissions():
    out = slab(W0, D0, PLATE)
    out += box(1.0, 0.7, 2.2, 0.6, 0.36, 0, DESK)                                       # the admissions desk
    out += person(2.0, 0.55, BLUE)                                                       # the clerk behind it
    out += box(1.25, 0.82, 0.42, 0.32, 0.06, 0.36, PAPER, lip=False)                     # forms
    out += box(1.8, 0.85, 0.46, 0.3, 0.05, 0.36, TRUNK, lip=False)                       # the blue application file
    out += box(2.5, 0.8, 0.36, 0.3, 0.02, 0.36, PAPER, lip=False)
    out += person(1.7, 1.85, "#6f7a8c") + kid(2.15, 1.95, "#8f98a8")                     # a mother and her child
    out += box(3.5, 0.5, 0.5, 0.06, 1.0, 0, PAPER, lip=False)                             # the notice board
    out += poly(fl(3.55, 3.95, 0.56, 0.55, 0.9), "#e8effd", "none")
    return out


def d_fees():
    out = slab(W0, D0, PLATE)
    out += box(0.6, 0.4, 2.2, 1.2, 1.15)                                                # the bursary
    out += box(0.55, 0.35, 2.3, 1.3, 0.08, 1.15, PALE)
    out += poly(fl(1.0, 2.2, 1.6, 0.4, 0.85), GLASS, HAIR, 0.5)                          # counter window
    out += box(0.95, 1.6, 1.3, 0.22, 0.04, 0.38, PALE, lip=False)
    out += poly(fl(1.05, 1.5, 1.6, 0.42, 0.78), "#9fb3d9", "none")
    out += sign(1.0, 2.4, 1.6, 0.92, 1.08, "Bursary")
    for k, (px, py, t) in enumerate(((1.6, 2.15, BLUE), (2.25, 2.35, "#6f7a8c"), (2.9, 2.5, "#8f98a8"), (3.55, 2.6, "#6f7a8c"))):
        out += person(px, py, t)
    return out


def d_accounting():
    out = slab(W0, D0, PLATE)
    out += box(0.5, 0.4, 0.5, 0.9, 0.75, 0, ("#e9ecf0", "#d4d9e0", "#c3c9d3"))           # filing cabinet
    for z in (0.22, 0.47):
        out += line((1.0, 0.55, z), (1.0, 1.15, z), "rgba(20,24,36,.25)", 0.7)
    out += box(1.3, 0.7, 2.3, 1.0, 0.36, 0, DESK)                                       # the desk
    out += laptop(1.55, 0.95, 0.36, 0.62, 0.4)
    out += books(2.45, 0.95, 0.36, 3, 0.36, 0.26, blue=9)                                # ledgers
    out += box(3.05, 1.0, 0.34, 0.3, 0.14, 0.36, ("#3a404c", "#2e333d", "#262a33"), lip=False)   # the fiscal receipt printer
    out += box(3.12, 1.3, 0.2, 0.14, 0.01, 0.36, PAPER, lip=False)
    out += person(2.2, 2.15, "#6f7a8c")
    return out


def d_hr():
    out = slab(W0, D0, PLATE)
    out += box(0.6, 0.45, 2.0, 0.45, 1.2, 0, ("#e9dcc6", "#d9c8aa", "#c9b594"))          # pigeonholes
    for r in range(4):
        for c in range(5):
            x0, z0 = 0.7 + c * 0.38, 0.1 + r * 0.28
            fill = "#ffffff" if (r + c) % 2 == 0 else "#efe6d6"
            if (r, c) == (2, 3):
                fill = BLUE
            out += poly(fl(x0, x0 + 0.3, 0.9, z0, z0 + 0.2), fill, HAIR, 0.4)
    out += box(2.9, 0.6, 1.0, 0.7, 0.34, 0, DESK)                                       # payslip table
    for k in range(3):
        out += box(3.0 + k * 0.28, 0.75 + k * 0.06, 0.24, 0.34, 0.012, 0.34, PAPER, lip=False)
    out += person(1.6, 1.6, "#6f7a8c") + person(3.4, 1.75, BLUE)
    return out


def d_boarding():
    out = slab(W0, D0, PLATE)
    out += poly(top(0.4, 0.3, 3.6, 2.4, 0.01), "#eef0f3", HAIR, 0.4)
    for bx in (0.7, 2.3):                                                               # two bunks
        for z in (0.25, 0.85):
            out += box(bx, 0.5, 1.2, 0.55, 0.12, z, ("#ffffff", "#e5e8ed", "#d4d9e0"), lip=False)
            out += box(bx + 0.05, 0.55, 0.3, 0.45, 0.06, z + 0.12, ("#e8effd", "#d5e1fb", "#c3d3f8"), lip=False)
        for px in (bx, bx + 1.15):
            out += box(px, 1.0, 0.05, 0.05, 1.15, 0, DARK, lip=False)
    out += box(0.9, 1.45, 0.7, 0.4, 0.3, 0, TRUNK, lip=False)                             # the trunk
    out += line((0.9, 1.85, 0.2), (1.6, 1.85, 0.2), "#1f4fb8", 0.9)
    out += kid(2.3, 1.95, "#6f7a8c") + person(3.3, 1.85, "#8f98a8")                      # a boarder and the matron
    return out


def d_stock():
    out = slab(W0, D0, PLATE)
    svg, _ = ISO.stores(0.5, 0.4, 2.2, 1.2, 0.95)
    out += svg
    for i, (dx, dy, dz, f) in enumerate(((3.0, 1.0, 0, PAPER), (3.45, 1.0, 0, ("#efe6d6", "#e3d6bf", "#d6c6aa")), (3.2, 1.0, 0.32, TRUNK),
                                         (3.0, 1.5, 0, ("#efe6d6", "#e3d6bf", "#d6c6aa")))):
        out += box(dx, dy, 0.4, 0.4, 0.32, dz, f, lip=False)                              # boxes: textbooks, uniforms
    out += person(2.6, 2.3, "#6f7a8c")
    return out


def d_comms():
    out = slab(W0, D0, GRASS)
    x, y, w, d, h = 1.2, 1.0, 1.25, 0.14, 2.1                                           # a phone standing on the plate
    out += box(x, y, w, d, h, 0.02, ("#3a404c", "#2e333d", "#262a33"), lip=False)
    out += poly(fl(x + 0.07, x + w - 0.07, y + d, 0.14, h - 0.08), "#ffffff", "none")
    out += poly(fl(x + 0.12, x + 0.95, y + d, 1.55, 1.85), "#f1f3f6", "none")             # message in
    out += poly(fl(x + 0.3, x + 1.13, y + d, 1.1, 1.4), BLUE, "none")                     # reply out
    out += poly(fl(x + 0.12, x + 0.8, y + d, 0.65, 0.95), "#f1f3f6", "none")
    for k, z in enumerate((1.75, 1.65)):
        out += line((x + 0.2, y + d, z), (x + 0.8 - k * 0.2, y + d, z), "#9aa1ad", 0.8)
    out += person(3.1, 1.6, "#6f7a8c") + kid(3.45, 1.75, "#8f98a8")
    return out


def d_insights():
    out = slab(W0, D0, PLATE)
    for i, (hh, f) in enumerate(((0.55, PALE), (0.8, PALE), (0.7, PALE), (1.25, ROOF))):   # the figures, as bars
        out += box(0.8 + i * 0.62, 0.7, 0.42, 0.42, hh, 0, f, lip=False)
    out += line((0.6, 1.3, 0.01), (3.4, 1.3, 0.01), "#c3c9d3", 1)
    out += person(3.6, 1.6, "#3a404c")                                                   # the Head
    out += box(1.2, 1.8, 1.4, 0.7, 0.32, 0, DESK)
    out += laptop(1.5, 1.95, 0.32, 0.55, 0.36)
    return out


DEPT_SCENES = {"academics": d_academics, "admissions": d_admissions, "fees": d_fees, "accounting": d_accounting, "hr": d_hr,
               "boarding": d_boarding, "stock": d_stock, "comms": d_comms, "insights": d_insights}


# ---- school types ----------------------------------------------------------------------------------
def s_day():
    out = slab(W0, D0, PLATE)
    svg, _ = ISO.classroom(0.4, 0.3, "Form 2", 3.2, 1.0, 0.85)
    out += svg
    out += kid(1.6, 2.5, "#6f7a8c") + kid(2.0, 2.6, BLUE) + kid(2.4, 2.5, "#8f98a8")      # pupils arriving with bags
    return out


def s_boarding():
    out = slab(W0, D0, PLATE)
    svg, _ = ISO.hostel(0.4, 0.3, "Tsavo House", 3.4, 1.1, 1.5)
    out += svg
    out += box(1.2, 2.3, 0.6, 0.35, 0.26, 0, TRUNK, lip=False) + kid(2.1, 2.5, "#6f7a8c")
    return out


def s_government():
    out = slab(W0, D0, PLATE)
    svg, _ = ISO.admin(0.9, 0.4, 2.4, 1.3, 1.35)
    out += svg
    out += kid(2.6, 2.4, "#6f7a8c") + person(3.1, 2.3, "#8f98a8")
    return out


def s_private():
    out = slab(W0, D0, PLATE)
    out += box(0.8, 0.3, 2.8, 1.1, 1.3) + box(0.75, 0.25, 2.9, 1.2, 0.08, 1.3, PALE)
    for z in (0.25, 0.8):
        out += win_f(1.0, 1.4, z, 5, 0.32, 0.32, 0.18)
    out += sign(1.4, 3.0, 1.4, 1.08, 1.24, "Senior School")
    out += box(0.95, 2.1, 0.22, 0.22, 0.75, 0, DARK, lip=False) + box(3.25, 2.1, 0.22, 0.22, 0.75, 0, DARK, lip=False)   # gate pillars
    out += poly(fl(1.17, 3.25, 2.32, 0.45, 0.7), BLUE, "none")                            # the blue name board
    out += line((1.17, 2.32, 0.2), (3.25, 2.32, 0.2), "#9aa1ad", 1.2)
    return out


def s_mission():
    out = slab(W0, D0, GRASS)
    out += box(1.2, 0.4, 1.4, 2.0, 1.0)                                                 # the chapel
    out += gable(1.12, 0.32, 1.56, 2.16, 1.0, 0.9, ROOF_GREY)
    out += poly(fl(1.65, 2.15, 2.4, 0, 0.7), "#8f98a8", HAIR, 0.5)
    out += win_s(2.6, 0.7, 0.35, 3, 0.25, 0.4, 0.3)
    cx = 1.9
    out += line((cx, 2.48, 1.45), (cx, 2.48, 2.05), BLUE, 2.2) + line((cx - 0.17, 2.48, 1.85), (cx + 0.17, 2.48, 1.85), BLUE, 2.2)   # the cross
    out += ISO.jtree(3.5, 1.2, 0.8, ISO.JAC) + kid(3.1, 2.6, "#6f7a8c")
    return out


TYPE_SCENES = {"t-day": s_day, "t-boarding": s_boarding, "t-government": s_government, "t-private": s_private, "t-mission": s_mission}


def art(kind, w=360, h=230, U=None):
    """one department or school type on its plate, fitted to w x h"""
    fn = DEPT_SCENES.get(kind) or TYPE_SCENES[kind]
    U = U or min(w / 7.6, h / 4.6)
    setup(W0, D0, U, w / 2, h * 0.62)
    return (f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="display:block" aria-hidden="true">{DEFS}{fn()}</svg>')


# ---- the five kinds of K-12 school on one campus plate (the Who we serve call to action) -----------------
def schools_campus(w=600, h=420, U=28):
    """one plate, one projection: the chapel and Tsavo House and the admin block along the back, a path, the Form 2 block and
    the private senior school with its gate along the front. Labels on stems name each kind of school."""
    import nav_icons
    W, D = 12.0, 7.4
    setup(W, D, U, w / 2 + 6, h * 0.6)
    out = slab(W, D, PLATE)
    out += poly(top(0.3, 0.3, 2.6, 2.4, 0.004), GRASS[0], "none")                       # the mission's lawn
    out += poly(top(0, 3.05, W, 0.75, 0.003), "#eceef2", "none")                         # the inner path
    out += line((0, 3.05, 0.005), (W, 3.05, 0.005), "rgba(20,24,36,0.08)", 0.8) + line((0, 3.8, 0.005), (W, 3.8, 0.005), "rgba(20,24,36,0.08)", 0.8)
    anchors = {}
    # back row, drawn first
    ch = box(0.8, 0.5, 1.3, 1.9, 0.95) + gable(0.72, 0.42, 1.46, 2.06, 0.95, 0.85, ROOF_GREY)
    ch += poly(fl(1.2, 1.7, 2.4, 0, 0.65), "#8f98a8", HAIR, 0.5) + win_s(2.1, 0.8, 0.32, 3, 0.26, 0.36, 0.2)
    cx = 1.45
    ch += line((cx, 2.48, 1.35), (cx, 2.48, 2.0), BLUE, max(1.6, 0.09 * I.U)) + line((cx - 0.18, 2.48, 1.78), (cx + 0.18, 2.48, 1.78), BLUE, max(1.6, 0.09 * I.U))
    out += ch
    anchors["t-mission"] = (1.45, 1.45, 1.8)
    svg, a = ISO.hostel(3.3, 0.5, "Tsavo House", 3.6, 1.1, 1.45)
    out += svg; anchors["t-boarding"] = a
    svg, a = ISO.admin(8.5, 0.5, 2.4, 1.3, 1.35)
    out += svg; anchors["t-government"] = a
    out += ISO.jtree(11.4, 2.4, 0.75, ISO.JAC) + ISO.jtree(2.6, 2.3, 0.6, "green") + ISO.jtree(7.6, 1.2, 0.7, "green")
    out += kid(4.4, 3.4, "#6f7a8c") + kid(4.8, 3.5, BLUE) + kid(9.6, 3.45, "#8f98a8")
    # front row
    svg, a = ISO.classroom(0.6, 4.3, "Form 2", 3.2, 1.0, 0.85)
    out += svg; anchors["t-day"] = a
    px = 6.0
    pb = poly(top(px + 0.9, 5.4, 1.0, 1.05, 0.004), "#eceef2", "none")                   # the drive to the gate
    pb += shadow(px, 4.3, 2.8, 1.1, 0.6) + box(px, 4.3, 2.8, 1.1, 1.25) + box(px - 0.05, 4.25, 2.9, 1.2, 0.08, 1.25, PALE)
    for z in (0.22, 0.75):
        pb += win_f(px + 0.2, 5.4, z, 5, 0.3, 0.32, 0.18)
    pb += sign(px + 0.6, px + 2.2, 5.4, 1.0, 1.16, "Senior School")
    pb += box(px, 6.45, 0.2, 0.2, 0.7, 0, DARK, lip=False) + box(px + 2.6, 6.45, 0.2, 0.2, 0.7, 0, DARK, lip=False)
    pb += poly(fl(px + 0.2, px + 2.6, 6.65, 0.42, 0.66), BLUE, "none")
    out += pb; anchors["t-private"] = (px + 1.4, 4.85, 1.35)
    out += ISO.jtree(4.9, 5.9, 0.7, ISO.JAC) + ISO.jtree(10.6, 5.4, 0.75, "green") + ISO.jtree(11.2, 4.4, 0.6, ISO.JAC) + kid(2.6, 6.2, BLUE) + kid(3.0, 6.3, "#6f7a8c")
    pts = {k: P(*v) for k, v in anchors.items()}
    names = {k: n.replace(" schools", "") for n, k, d in __import__("words").SCHOOL_TYPES}
    svg = f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="position:absolute;left:0;top:0" aria-hidden="true">{DEFS}{out}</svg>'
    PILL = ("display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 11px 0 4px;border:1px solid #e7e9ef;border-radius:999px;background:#fff;"
            "box-shadow:0 6px 14px -8px rgba(15,20,35,.35);font:500 12.5px 'Atkinson Hyperlegible Next',sans-serif;color:#0b0c14;white-space:nowrap")
    lab = ""
    for k, (ax, ay) in pts.items():
        stem = 22
        lab += (f'<span style="position:absolute;left:{ax - 0.5:.1f}px;top:{ay - stem:.0f}px;width:1px;height:{stem}px;background:#9aa1ad"></span>'
                f'<span style="position:absolute;left:{ax - 3:.1f}px;top:{ay - 3:.1f}px;width:6px;height:6px;border-radius:3px;background:#fff;border:1.5px solid #0b0c14;box-sizing:border-box"></span>'
                f'<span style="position:absolute;left:{ax:.0f}px;top:{ay - stem - 30:.0f}px;transform:translateX(-50%)"><span style="{PILL}">{nav_icons.nav_icon(k, 22)}{names[k]}</span></span>')
    return f'<div style="position:relative;width:{w}px;height:{h}px">{svg}{lab}</div>'

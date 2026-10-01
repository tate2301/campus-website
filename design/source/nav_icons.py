# -*- coding: utf-8 -*-
"""Navigation icons, drawn in the campus projection like the portal icons: one object per page, one blue part,
centred on a pale tile. Used in the site map, the reach table and the menus."""
import iso_campus as ISO
from iso_campus import I, P, poly, line, box, fl, fr, top, win_f, win_s, gable, WALL, PALE, DARK, ROOF, GLASS, HAIR, BLUE
import portal_art

PAPER = ("#ffffff", "#e5e8ed", "#d4d9e0")
BLUEF = ("#5b8cf3", "#3469e0", "#2853c2")
INKF = ("#4b5363", "#3a404c", "#2e333d")
WOOD = ("#efe6d6", "#e3d6bf", "#d6c6aa")
BOARD = ("#2b3631", "#34433d", "#26302b")
GREYR = ("#cfd4dc", "#b8bfca", "#a7afbc")


def txt(x, y, z, s, t, fill="#ffffff", w=600):
    size = s * I.U
    return (f'<text transform="{I.fmat(x, y, z)}" text-anchor="middle" dominant-baseline="central" font-family="{I.FONT}" '
            f'font-size="{size:.1f}" font-weight="{w}" fill="{fill}">{t}</text>')


def ring(cx, cy, z, r, fill, stroke="none", sw=0):
    c = P(cx, cy, z)
    return f'<ellipse cx="{c[0]:.1f}" cy="{c[1]:.1f}" rx="{r * I.U * 0.866:.1f}" ry="{r * I.U * 0.5:.1f}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def coin(cx, cy, z, r=0.55, h=0.16, f=PAPER):
    return I.cyl(cx, cy, r, h, z, f)


def sheet(x, y, w, d, z=0.0, f=PAPER):
    return box(x, y, w, d, 0.06, z, f, lip=False)


def standing(x, y, w, h, z=0.0, d=0.08, f=PAPER):
    """a panel standing up, its face towards the viewer's left (the +y plane)"""
    return box(x, y, w, d, h, z, f, lip=False)


# ---- top level --------------------------------------------------------------------------------------
def i_solutions():
    out = ""
    for r in range(3):
        for c in range(3):
            f = BLUEF if (r, c) == (0, 2) else WALL
            h = 0.5 if (r, c) == (0, 2) else 0.32
            out += box(c * 0.82, r * 0.82, 0.66, 0.66, h, 0, f, lip=False)
    return out, (2.3, 2.3, 0.5)


def i_who():
    out = box(0, 0, 2.6, 1.2, 0.9)
    for i in range(3):
        out += poly(fl(0.2 + i * 0.82, 0.48 + i * 0.82, 1.2, 0, 0.62), "#8f98a8", "none")
        out += poly(fl(0.55 + i * 0.82, 0.86 + i * 0.82, 1.2, 0.28, 0.62), GLASS, "none")
    out += gable(-0.1, -0.1, 2.8, 1.4, 0.9, 0.6, ROOF)
    return out, (2.6, 1.2, 1.5)


def i_platform():
    out = box(0, 0, 2.2, 2.2, 0.28, 0, PALE, lip=False)
    out += box(0.12, 0.12, 1.96, 1.96, 0.28, 0.42, WALL, lip=False)
    out += box(0.24, 0.24, 1.72, 1.72, 0.28, 0.84, BLUEF, lip=False)
    return out, (2.2, 2.2, 1.12)


def i_pricing():
    out = coin(0.7, 0.7, 0) + coin(0.7, 0.7, 0.18) + coin(0.7, 0.7, 0.36, f=BLUEF)
    out += coin(1.75, 1.3, 0) + coin(1.75, 1.3, 0.18)
    return out, (2.3, 1.85, 0.52)


def i_demo():
    out = box(0, 0, 2.0, 1.8, 0.5, 0, WALL)
    out += box(0, 0, 2.0, 1.8, 0.18, 0.5, BLUEF, lip=False)
    for r in range(3):
        for c in range(4):
            out += poly(top(0.2 + c * 0.42, 0.25 + r * 0.45, 0.28, 0.28, 0.505), "#dfe3ea", "none") if False else ""
    for c in range(4):
        out += poly(fl(0.15 + c * 0.45, 0.45 + c * 0.45, 1.8, 0.12, 0.38), "#e8ecf2", "none")
    out += line((0.5, 0.6, 0.68), (0.5, 0.6, 0.95), INKF[1], 2) + line((1.5, 0.6, 0.68), (1.5, 0.6, 0.95), INKF[1], 2)
    return out, (2.0, 1.8, 0.95)


def i_signin():
    out = box(0, 0, 1.6, 0.25, 2.1, 0, PALE, lip=False)                      # door frame
    out += poly(fl(0.22, 1.38, 0.25, 0, 1.85), BLUE, "none")                 # the door
    c = P(1.18, 0.25, 0.95)
    out += f'<circle cx="{c[0]:.1f}" cy="{c[1]:.1f}" r="{0.07 * I.U:.1f}" fill="#ffffff"/>'
    out += box(0.05, 0.25, 1.5, 0.35, 0.04, 0, PAPER, lip=False)              # the step
    return out, (1.6, 0.6, 2.1)


def i_footer():
    out = sheet(0, 0, 2.4, 1.7)
    out += box(0, 1.25, 2.4, 0.45, 0.07, 0, BLUEF, lip=False)
    for k in range(3):
        out += line((0.25, 0.3 + k * 0.28, 0.065), (1.7 - k * 0.3, 0.3 + k * 0.28, 0.065), "#c3c9d3", 1.2)
    return out, (2.4, 1.7, 0.1)


# ---- departments ------------------------------------------------------------------------------------
def i_academics():
    out = box(0, 0.5, 2.2, 0.08, 1.3, 0.25, BOARD, lip=False)
    out += box(0.05, 0.58, 0.08, 0.08, 1.6, 0, DARK, lip=False) + box(2.07, 0.58, 0.08, 0.08, 1.6, 0, DARK, lip=False)
    for k in range(3):
        out += line((0.25, 0.58, 1.3 - k * 0.25), (1.4 - k * 0.25, 0.58, 1.3 - k * 0.25), "rgba(255,255,255,.6)", 1.1)
    out += box(0.6, 1.0, 0.7, 0.5, 0.1, 0, PAPER, lip=False) + box(0.62, 1.02, 0.66, 0.46, 0.1, 0.1, BLUEF, lip=False)
    return out, (2.2, 1.5, 1.6)


def i_admissions():
    out = sheet(0, 0, 1.6, 2.0)
    out += box(0.45, -0.1, 0.7, 0.25, 0.14, 0.06, INKF, lip=False)            # the clip
    for k in range(4):
        out += line((0.25, 0.45 + k * 0.32, 0.065), (1.35 - (k % 2) * 0.35, 0.45 + k * 0.32, 0.065), "#c3c9d3", 1.3)
    out += box(1.0, 1.2, 1.0, 0.8, 0.12, 0.06, BLUEF, lip=False)              # the application file
    return out, (2.0, 2.0, 0.2)


def i_fees():
    out = ""
    for k in range(3):                                                          # a stack of bank notes
        out += box(0, 0.2, 2.0, 1.2, 0.1, k * 0.1, ("#e7f2ea", "#cfe3d5", "#bdd7c4"), lip=False)
    out += ring(1.0, 0.8, 0.31, 0.3, "none", "#9cc4a8", 1.2)
    out += coin(1.9, 1.75, 0, 0.45) + coin(1.9, 1.75, 0.16, 0.45) + coin(1.9, 1.75, 0.32, 0.45, f=BLUEF)
    return out, (2.4, 2.2, 0.48)


def i_accounting():
    out = ""
    for k, f in enumerate((PAPER, PAPER, BLUEF)):
        out += box(0, 0, 1.4, 1.9, 0.18, k * 0.2, f, lip=False)
    out += box(1.65, 0.6, 0.85, 1.3, 0.2, 0, INKF, lip=False)                 # calculator
    out += poly(top(1.75, 0.7, 0.65, 0.3, 0.205), "#b8f0c8", "none")
    for r in range(3):
        for c in range(3):
            out += poly(top(1.75 + c * 0.22, 1.1 + r * 0.24, 0.15, 0.16, 0.205), "#8f98a8", "none")
    return out, (2.5, 1.9, 0.6)


def i_hr():
    out = box(0, 0, 2.2, 0.6, 1.6, 0, WOOD)
    for r in range(3):
        for c in range(4):
            x0, z0 = 0.15 + c * 0.5, 0.15 + r * 0.48
            fill = BLUE if (r, c) == (1, 2) else ("#ffffff" if (r + c) % 2 == 0 else "#f3ece0")
            out += poly(fl(x0, x0 + 0.4, 0.6, z0, z0 + 0.36), fill, HAIR, 0.4)
    return out, (2.2, 0.6, 1.6)


def i_boarding():
    out = ""
    for z in (0.25, 1.0):
        out += box(0, 0, 2.2, 1.0, 0.16, z, PAPER, lip=False)
        out += box(0.08, 0.1, 0.55, 0.8, 0.08, z + 0.16, ("#e8effd", "#d5e1fb", "#c3d3f8"), lip=False)
    for px, py in ((0, 0.92), (2.12, 0.92), (2.12, 0)):
        out += box(px, py, 0.08, 0.08, 1.45, 0, DARK, lip=False)
    out += box(0.5, 1.25, 1.1, 0.6, 0.45, 0, BLUEF, lip=False)                 # the trunk
    return out, (2.2, 1.85, 1.45)


def i_stock():
    out = box(0, 0, 1.0, 1.0, 0.8, 0, WOOD) + box(1.15, 0, 1.0, 1.0, 0.8, 0, WOOD) + box(0.55, 0.1, 1.0, 0.9, 0.7, 0.8, BLUEF)
    out += box(0.3, 1.2, 0.9, 0.8, 0.6, 0, WOOD)
    for x0 in (0.45, 1.6):
        out += line((x0, 1.0, 0.55), (x0 + 0.3, 1.0, 0.55), "rgba(20,24,36,.25)", 0.8)
    return out, (2.15, 2.0, 1.5)


def i_comms():
    out = box(0, 0, 1.3, 0.16, 2.2, 0, INKF, lip=False)
    out += poly(fl(0.08, 1.22, 0.16, 0.12, 2.08), "#ffffff", "none")
    out += poly(fl(0.15, 0.95, 0.16, 1.55, 1.85), "#eef0f3", "none")
    out += poly(fl(0.35, 1.15, 0.16, 1.05, 1.38), BLUE, "none")
    out += poly(fl(0.15, 0.8, 0.16, 0.6, 0.88), "#eef0f3", "none")
    return out, (1.3, 0.16, 2.2)


def i_insights():
    out = ""
    for i, (h, f) in enumerate(((0.6, PALE), (0.95, PALE), (0.75, PALE), (1.55, BLUEF))):
        out += box(i * 0.6, 0, 0.44, 0.44, h, 0, f, lip=False)
    out += box(-0.15, -0.15, 2.5, 0.8, 0.04, -0.04, PAPER, lip=False)
    return out, (2.4, 0.65, 1.55)


# ---- school types -----------------------------------------------------------------------------------
def i_day():
    return i_who()


def i_boarding_school():
    out = box(0, 0, 2.6, 1.1, 1.5) + box(-0.05, -0.05, 2.7, 1.2, 0.1, 1.5, PALE)
    for z in (0.25, 0.9):
        out += win_f(0.2, 1.1, z, 5, 0.3, 0.36, 0.18)
    out += box(0.9, 1.25, 0.8, 0.45, 0.35, 0, BLUEF, lip=False)
    return out, (2.6, 1.7, 1.6)


def i_government():
    out = box(0, 0, 2.2, 1.3, 1.4) + box(-0.05, -0.05, 2.3, 1.4, 0.1, 1.4, PALE)
    for z in (0.25, 0.85):
        out += win_f(0.2, 1.3, z, 4, 0.32, 0.34, 0.18)
    fx, fy = -0.3, 1.5
    out += line((fx, fy, 0), (fx, fy, 2.2), "#8f97a5", 1.6)
    out += poly([P(fx, fy, 2.2), P(fx + 0.7, fy, 2.1), P(fx + 0.7, fy, 1.75), P(fx, fy, 1.85)], BLUE, "none")
    return out, (2.2, 1.6, 2.2)


def i_private():
    out = box(0.3, 0, 2.0, 1.0, 1.1) + box(0.25, -0.05, 2.1, 1.1, 0.08, 1.1, PALE)
    out += win_f(0.5, 1.0, 0.3, 4, 0.3, 0.4, 0.18)
    out += box(0, 1.5, 0.22, 0.22, 0.85, 0, DARK, lip=False) + box(2.4, 1.5, 0.22, 0.22, 0.85, 0, DARK, lip=False)
    out += poly(fl(0.22, 2.4, 1.72, 0.5, 0.8), BLUE, "none")
    return out, (2.62, 1.72, 1.18)


def i_mission():
    out = box(0, 0, 1.4, 2.0, 1.0)
    out += gable(-0.08, -0.08, 1.56, 2.16, 1.0, 0.9, GREYR)
    out += poly(fl(0.45, 0.95, 2.0, 0, 0.7), "#8f98a8", HAIR, 0.5)
    cx = 0.7
    out += line((cx, 2.08, 1.45), (cx, 2.08, 2.15), BLUE, 2.4) + line((cx - 0.2, 2.08, 1.9), (cx + 0.2, 2.08, 1.9), BLUE, 2.4)
    return out, (1.4, 2.1, 2.1)


# ---- platform ---------------------------------------------------------------------------------------
def i_record():
    out = box(0, 0, 1.8, 0.14, 2.2, 0, PAPER, lip=False)                      # a record card standing
    out += box(0, 0, 0.7, 0.14, 0.3, 2.2, BLUEF, lip=False)                   # its tab
    c = P(0.5, 0.14, 1.6)
    out += f'<circle cx="{c[0] + 2:.1f}" cy="{c[1]:.1f}" r="{0.22 * I.U:.1f}" fill="#d5e1fb"/>'
    for k in range(3):
        out += line((0.95, 0.14, 1.75 - k * 0.25), (1.6, 0.14, 1.75 - k * 0.25), "#c3c9d3", 1.1)
    out += line((0.2, 0.14, 0.8), (1.6, 0.14, 0.8), "#c3c9d3", 1.1) + line((0.2, 0.14, 0.55), (1.3, 0.14, 0.55), "#c3c9d3", 1.1)
    return out, (1.8, 0.14, 2.5)


def i_offline():
    out = box(0, 0, 2.0, 0.14, 1.5, 0, INKF, lip=False)                       # a tablet on its stand
    out += poly(fl(0.08, 1.92, 0.14, 0.08, 1.42), "#ffffff", "none")
    out += poly(fl(0.18, 1.82, 0.14, 1.12, 1.3), "#fdf1dc", "none")           # "saved on this tablet"
    for k in range(3):
        out += line((0.2, 0.14, 0.9 - k * 0.22), (1.5, 0.14, 0.9 - k * 0.22), "#d4d9e0", 1.1)
        out += poly(fl(1.58, 1.8, 0.14, 0.82 - k * 0.22, 0.96 - k * 0.22), BLUE if k == 0 else "#dbe7d9", "none")
    out += box(0.3, 0.14, 1.4, 0.7, 0.06, 0, PALE, lip=False)
    return out, (2.0, 0.84, 1.5)


def i_portals():
    out = ""
    for i, (x, y, f) in enumerate(((0, 0, WALL), (1.1, 0, WALL), (0, 1.1, WALL), (1.1, 1.1, WALL))):
        out += box(x, y, 0.85, 0.85, 0.55, 0, f)
        out += box(x - 0.04, y - 0.04, 0.93, 0.93, 0.12, 0.55, BLUEF if i == 1 else GREYR, lip=False)
    return out, (1.95, 1.95, 0.67)


def i_security():
    out = box(0, 0, 1.8, 1.6, 1.6, 0, ("#e9ecf0", "#d4d9e0", "#c3c9d3"))      # a safe
    c = P(0.9, 1.6, 0.85)
    out += (f'<ellipse cx="{c[0]:.1f}" cy="{c[1]:.1f}" rx="{0.36 * I.U * 0.87:.1f}" ry="{0.36 * I.U:.1f}" transform="rotate(-30 {c[0]:.1f} {c[1]:.1f})" fill="{BLUE}"/>'
            f'<ellipse cx="{c[0]:.1f}" cy="{c[1]:.1f}" rx="{0.12 * I.U * 0.87:.1f}" ry="{0.12 * I.U:.1f}" transform="rotate(-30 {c[0]:.1f} {c[1]:.1f})" fill="#ffffff"/>')
    out += box(1.8, 0.3, 0.06, 0.25, 0.3, 1.1, INKF, lip=False) + box(1.8, 1.0, 0.06, 0.25, 0.3, 1.1, INKF, lip=False)
    return out, (1.86, 1.6, 1.6)


def i_ai():
    out = box(0, 0, 1.7, 0.12, 2.1, 0, PAPER, lip=False)
    for k in range(4):
        out += line((0.2, 0.12, 1.7 - k * 0.3), (1.45 - (k % 2) * 0.4, 0.12, 1.7 - k * 0.3), "#c3c9d3", 1.1)
    cx, z = 1.15, 0.5                                                          # a four-point spark in blue
    pts_ = [P(cx, 0.12, z + 0.42), P(cx + 0.1, 0.12, z + 0.1), P(cx + 0.38, 0.12, z), P(cx + 0.1, 0.12, z - 0.1),
            P(cx, 0.12, z - 0.42), P(cx - 0.1, 0.12, z - 0.1), P(cx - 0.38, 0.12, z), P(cx - 0.1, 0.12, z + 0.1)]
    out += poly(pts_, BLUE, "none")
    return out, (1.7, 0.12, 2.1)


def i_integrations():
    out = box(0.9, 0.9, 0.8, 0.8, 0.8, 0, BLUEF)
    out += line((0.45, 1.3, 0.3), (0.9, 1.3, 0.3), "#9aa1ad", 2) + line((1.3, 0.45, 0.3), (1.3, 0.9, 0.3), "#9aa1ad", 2)
    out += box(0, 1.0, 0.6, 0.6, 0.55, 0, WALL) + box(1.0, 0, 0.6, 0.6, 0.55, 0, WALL)
    return out, (1.7, 1.7, 0.8)


def i_moving():
    out = ISO.kombi(0, 0)
    return out, (1.75, 0.62, 0.82)


# ---- pricing, demo, company, legal ------------------------------------------------------------------
def i_calculator():
    out = box(0, 0, 1.5, 2.0, 0.25, 0, INKF, lip=False)
    out += poly(top(0.12, 0.12, 1.26, 0.45, 0.255), "#b8f0c8", "none")
    for r in range(4):
        for c in range(3):
            f = BLUE if (r, c) == (3, 2) else "#8f98a8"
            out += poly(top(0.15 + c * 0.42, 0.72 + r * 0.31, 0.3, 0.22, 0.255), f, "none")
    return out, (1.5, 2.0, 0.25)


def i_included():
    out = sheet(0, 0, 1.6, 2.1)
    for k in range(4):
        y = 0.35 + k * 0.42
        out += poly(top(0.2, y, 0.22, 0.22, 0.065), BLUE if k < 3 else "#d4d9e0", "none")
        out += line((0.55, y + 0.11, 0.065), (1.35, y + 0.11, 0.065), "#c3c9d3", 1.3)
    return out, (1.6, 2.1, 0.1)


def i_training():
    out = box(0, 0, 2.3, 0.1, 1.4, 0.4, PAPER, lip=False)                    # a screen on its stand
    out += box(1.1, 0.0, 0.1, 0.1, 0.4, 0, DARK, lip=False)
    for i, h in enumerate((0.35, 0.55, 0.8)):
        out += poly(fl(0.3 + i * 0.45, 0.6 + i * 0.45, 0.1, 0.6, 0.6 + h), BLUE if i == 2 else "#d4d9e0", "none")
    return out, (2.3, 0.1, 1.8)


def i_questions():
    out = box(0, 0, 1.9, 0.5, 1.3, 0.3, WALL)
    out += poly([P(0.35, 0.5, 0.3), P(0.75, 0.5, 0.3), P(0.35, 0.5, 0.0)], WALL[1], "rgba(20,24,36,0.16)")
    out += txt(0.95, 0.5, 0.95, 0.75, "?", BLUE)
    return out, (1.9, 0.5, 1.6)


def i_pricesheet():
    out = box(0, 0, 1.6, 0.12, 2.1, 0, PAPER, lip=False)
    out += poly(fl(0.0, 1.6, 0.12, 1.65, 2.1), BLUE, "none")
    for k in range(4):
        out += line((0.2, 0.12, 1.4 - k * 0.25), (1.4 - (k % 2) * 0.35, 0.12, 1.4 - k * 0.25), "#c3c9d3", 1.1)
    out += box(1.1, 0.4, 0.7, 0.7, 0.2, 0, BLUEF, lip=False)                  # the download tile
    a, b = P(1.45, 0.75, 0.21), P(1.45, 0.75, 0.21)
    return out, (1.8, 1.1, 2.1)


def i_sent():
    out = box(0, 0, 2.2, 1.5, 0.12, 0, PAPER, lip=False)                     # an envelope
    out += poly([P(0, 0, 0.125), P(1.1, 0.75, 0.125), P(2.2, 0, 0.125)], "#e8effd", HAIR, 0.5)
    out += line((0, 1.5, 0.125), (1.1, 0.75, 0.125), "#c3c9d3", 1) + line((2.2, 1.5, 0.125), (1.1, 0.75, 0.125), "#c3c9d3", 1)
    out += I.cyl(1.75, 1.35, 0.32, 0.08, 0.12, BLUEF)                          # the tick seal
    return out, (2.2, 1.6, 0.25)


def i_contact():
    out = box(0, 0, 1.0, 0.12, 1.8, 0, INKF, lip=False)
    out += poly(fl(0.07, 0.93, 0.12, 0.12, 1.68), "#ffffff", "none")
    out += poly(fl(0.17, 0.83, 0.12, 0.25, 0.55), BLUE, "none")
    for r in range(3):
        out += poly(fl(0.2, 0.8, 0.12, 0.75 + r * 0.25, 0.9 + r * 0.25), "#eef0f3", "none")
    return out, (1.0, 0.12, 1.8)


def i_support():
    out = ""
    for k in range(8):
        a0, a1 = k * 45, (k + 1) * 45
        import math
        pts_ = []
        for a in range(a0, a1 + 1, 9):
            r = math.radians(a)
            pts_.append(P(1 + 1.0 * math.cos(r), 1 + 1.0 * math.sin(r), 0.2))
        for a in range(a1, a0 - 1, -9):
            r = math.radians(a)
            pts_.append(P(1 + 0.55 * math.cos(r), 1 + 0.55 * math.sin(r), 0.2))
        out += poly(pts_, BLUE if k % 2 == 0 else "#ffffff", HAIR, 0.5)
    return out, (2.0, 2.0, 0.2)


def i_privacy():
    a, b = P(0.3, 0.3, 1.0), P(1.1, 0.3, 1.0)                                   # the shackle, then the body of the padlock
    r = (b[0] - a[0]) / 2
    out = f'<path d="M{a[0]:.1f} {a[1]:.1f} V{a[1] - r * 0.9:.1f} A{r:.1f} {r:.1f} 0 0 1 {b[0]:.1f} {b[1] - r * 0.9:.1f} V{b[1]:.1f}" fill="none" stroke="#9aa1ad" stroke-width="{0.18 * I.U:.1f}" stroke-linecap="round"/>'
    out += box(0, 0, 1.4, 0.6, 1.1, 0, BLUEF)
    c = P(0.7, 0.6, 0.55)
    out += f'<circle cx="{c[0]:.1f}" cy="{c[1]:.1f}" r="{0.1 * I.U:.1f}" fill="#ffffff"/>'
    return out, (1.4, 0.6, 1.9)


def i_data():
    out = I.cyl(0.8, 0.8, 0.8, 0.45, 0, WALL) + I.cyl(0.8, 0.8, 0.8, 0.45, 0.5, WALL) + I.cyl(0.8, 0.8, 0.8, 0.45, 1.0, BLUEF)
    return out, (1.6, 1.6, 1.45)


def i_terms():
    out = box(0, 0, 1.6, 0.12, 2.1, 0, PAPER, lip=False)
    for k in range(5):
        out += line((0.2, 0.12, 1.85 - k * 0.25), (1.4 - (k % 3) * 0.25, 0.12, 1.85 - k * 0.25), "#c3c9d3", 1.1)
    c = P(1.15, 0.12, 0.4)
    out += f'<circle cx="{c[0]:.1f}" cy="{c[1]:.1f}" r="{0.24 * I.U:.1f}" fill="{BLUE}"/>'
    return out, (1.6, 0.12, 2.1)


def i_nointernet():
    out = box(0, 0, 2.0, 1.2, 0.42, 0, WALL)                                   # a router
    for x0 in (0.35, 1.55):
        out += line((x0, 0.25, 0.42), (x0 - 0.1, 0.25, 1.25), "#8f98a8", 1.8)
    for k in range(3):
        out += poly(fl(0.3 + k * 0.32, 0.5 + k * 0.32, 1.2, 0.17, 0.27), "#8f98a8" if k else "#d4d9e0", "none")
    c = P(1.0, 0.6, 1.6)                                                         # the signal, crossed out
    out += "".join(f'<path d="M{c[0] - r:.1f} {c[1]:.1f} A{r:.1f} {r * 0.8:.1f} 0 0 1 {c[0] + r:.1f} {c[1]:.1f}" fill="none" stroke="#c3c9d3" stroke-width="{0.13 * I.U:.1f}" stroke-linecap="round"/>'
                   for r in (0.35 * I.U, 0.7 * I.U, 1.05 * I.U))
    out += f'<line x1="{c[0] - 0.95 * I.U:.1f}" y1="{c[1] - 0.95 * I.U:.1f}" x2="{c[0] + 0.95 * I.U:.1f}" y2="{c[1] + 0.35 * I.U:.1f}" stroke="{BLUE}" stroke-width="{0.16 * I.U:.1f}" stroke-linecap="round"/>'
    return out, (2.0, 1.2, 2.6)


def i_calendar_t():
    out = box(0, 0, 2.0, 0.12, 1.8, 0, PAPER, lip=False)                    # a timetable on the wall
    for r in range(4):
        for c in range(4):
            f = BLUE if (r, c) in ((1, 2), (3, 0)) else ("#e8ecf2" if (r + c) % 2 else "#f3f4f7")
            out += poly(fl(0.12 + c * 0.45, 0.5 + c * 0.45, 0.12, 0.12 + r * 0.38, 0.44 + r * 0.38), f, "none")
    out += poly(fl(0.0, 2.0, 0.12, 1.6, 1.8), INKF[1], "none")
    return out, (2.0, 0.12, 1.8)


ICONS = {"solutions": i_solutions, "who": i_who, "platform": i_platform, "pricing": i_pricing, "demo": i_demo, "signin": i_signin, "footer": i_footer,
         "academics": i_academics, "admissions": i_admissions, "fees": i_fees, "accounting": i_accounting, "hr-payroll": i_hr, "boarding": i_boarding,
         "stock": i_stock, "communication": i_comms, "insights": i_insights,
         "t-day": i_day, "t-boarding": i_boarding_school, "t-government": i_government, "t-private": i_private, "t-mission": i_mission,
         "record": i_record, "offline": i_offline, "portals": i_portals, "security": i_security, "ai": i_ai, "integrations": i_integrations, "moving": i_moving,
         "calculator": i_calculator, "included": i_included, "training": i_training, "questions": i_questions, "pricesheet": i_pricesheet,
         "sent": i_sent, "nointernet": i_nointernet, "calendar-t": i_calendar_t, "contact": i_contact, "support": i_support, "privacy": i_privacy, "data": i_data, "terms": i_terms}


def nav_icon(key, size=40, tile=True):
    """a page's icon: its object drawn small and centred on a pale tile, as portal_art.portal_icon"""
    if key in portal_art.SCENES:
        return portal_art.portal_icon(key, size, tile)
    fn = ICONS[key]
    U = size / 64 * 9.5
    I.U = U
    I.OX, I.OY = 0, 0
    svg0, ext = fn()
    xs, ys = [], []
    for x in (0, ext[0]):
        for y in (0, ext[1]):
            for z in (0, ext[2]):
                px, py = P(x, y, z)
                xs.append(px); ys.append(py)
    span = max(max(xs) - min(xs), (max(ys) - min(ys)) * 1.08)
    k = size * 0.7 / span                                                      # fill the tile to the same margin as the portal icons
    U *= k
    I.U = U
    xs = [v * k for v in xs]
    ys = [v * k for v in ys]
    I.OX = size / 2 - (min(xs) + max(xs)) / 2
    I.OY = size / 2 - (min(ys) + max(ys)) / 2 + size * 0.02
    svg, _ = fn()
    defs = '<defs><filter id="sh" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="1.5"/></filter></defs>'
    inner = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" style="display:block;flex:none" aria-hidden="true">{defs}{svg}</svg>'
    if not tile:
        return inner
    r = round(size * 0.24)
    return (f'<span style="width:{size}px;height:{size}px;border-radius:{r}px;background:#f4f5f7;box-shadow:inset 0 0 0 1px #e7e9ef;'
            f'display:flex;align-items:center;justify-content:center;flex:none;overflow:hidden">{inner}</span>')


# ==== v2, 1 Oct 2026: optimised set ===================================================================
# Every object now has thickness (no flat sheets), one clear blue part covering a fifth to a third of it,
# a soft contact shadow, the same light (top lightest, the +y face lit, the +x face in shade), and a
# reduced drawing below 28px where hairline details are dropped so the silhouette carries the icon.
import math
GREYF = ("#9aa3b2", "#7d8696", "#69717f")
NOTE = ("#e2f1e6", "#c3dfcb", "#adcfb8")
DETAIL = ("#c3c9d3", "#d4d9e0", "rgba(255,255,255,.6)", "#9aa1ad")       # hairline colours dropped at small sizes


def fig(x, y, h=1.3, f=GREYF):
    """a person at icon scale: a body block and a head, sized by the projection, not in pixels"""
    out = box(x - 0.2, y - 0.16, 0.4, 0.32, h * 0.66, 0, f, lip=False)
    c = P(x, y, h * 0.66 + 0.26)
    return out + f'<circle cx="{c[0]:.2f}" cy="{c[1]:.2f}" r="{0.21 * I.U:.2f}" fill="#3a404c"/>'


def i_solutions():
    out = ""
    for r in range(3):
        for c in range(3):
            hot = (r, c) == (0, 2)
            out += box(c * 0.8, r * 0.8, 0.62, 0.62, 0.95 if hot else 0.42, 0, BLUEF if hot else WALL, lip=False)
    return out, (2.22, 2.22, 0.95)


def i_who():
    """the people Campus serves: a teacher, a pupil in blue, a parent"""
    out = fig(0.35, 0.35, 1.55) + fig(1.55, 0.25, 1.45) + fig(0.95, 0.95, 1.1, BLUEF)
    return out, (1.9, 1.25, 1.85)


def i_pricing():
    """a price tag standing up, blue, with its string"""
    y0, y1 = 0.0, 0.16
    shape = [(0.5, 1.7), (2.0, 1.7), (2.0, 0.25), (0.5, 0.25), (0.0, 0.97)]
    out = poly([P(x, y0, z) for x, z in shape], BLUEF[2], "none")                     # back face, in shade
    out += poly([P(0.5, y0, 1.7), P(2.0, y0, 1.7), P(2.0, y1, 1.7), P(0.5, y1, 1.7)], BLUEF[0], "none")   # top edge
    out += poly([P(2.0, y0, 1.7), P(2.0, y1, 1.7), P(2.0, y1, 0.25), P(2.0, y0, 0.25)], BLUEF[2], "none")  # right edge
    out += poly([P(x, y1, z) for x, z in shape], BLUEF[1], "rgba(20,24,36,.16)")           # front face
    h = P(0.42, y1, 0.97)
    out += f'<circle cx="{h[0]:.2f}" cy="{h[1]:.2f}" r="{0.12 * I.U:.2f}" fill="#ffffff"/>'
    s0, s1 = P(0.42, y1, 0.97), P(-0.35, y1, 1.75)
    out += f'<path d="M{s0[0]:.2f} {s0[1]:.2f} Q{s0[0] - 0.4 * I.U:.2f} {s0[1] - 0.2 * I.U:.2f} {s1[0]:.2f} {s1[1]:.2f}" fill="none" stroke="#9aa1ad" stroke-width="{max(0.8, 0.07 * I.U):.2f}" stroke-linecap="round"/>'
    out += txt(1.28, y1, 0.97, 0.42, "US$1")
    return out, (2.0, 0.16, 1.75)


def i_demo():
    """a desk calendar standing up: blue header, rings, one day marked"""
    out = box(0, 0, 2.0, 0.34, 1.9, 0, PAPER, lip=False)
    out += poly(fl(0, 2.0, 0.34, 1.42, 1.9), BLUE, "none")
    for r in range(3):
        for c in range(4):
            x0, z0 = 0.18 + c * 0.44, 0.18 + r * 0.38
            out += poly(fl(x0, x0 + 0.32, 0.34, z0, z0 + 0.26), "#cfdcfb" if (r, c) == (1, 2) else "#eef0f3", "none")
    for rx in (0.45, 1.45):
        out += box(rx, 0.1, 0.1, 0.12, 0.3, 1.78, INKF, lip=False)
    return out, (2.0, 0.34, 2.08)


def i_signin():
    out = box(0, 0, 1.8, 0.3, 2.2, 0, PALE, lip=False)                                  # the frame
    out += poly(fl(0.22, 1.58, 0.3, 0.05, 1.98), BLUE, "none")                          # the door
    out += poly(fl(0.22, 0.4, 0.3, 0.05, 1.98), "#3469e0", "none")                       # its hinge edge
    k = P(1.35, 0.3, 1.0)
    out += f'<circle cx="{k[0]:.2f}" cy="{k[1]:.2f}" r="{0.09 * I.U:.2f}" fill="#ffffff"/>'
    out += box(-0.1, 0.3, 2.0, 0.5, 0.08, 0, PAPER, lip=False)                           # the step
    return out, (1.9, 0.8, 2.2)


def i_footer():
    """a page standing up: browser bar on top, the blue footer band at the bottom"""
    out = box(0, 0, 2.4, 0.16, 1.8, 0, PAPER, lip=False)
    out += poly(fl(0, 2.4, 0.16, 1.5, 1.8), "#eef0f3", "none")
    for i in range(3):
        c = P(0.18 + i * 0.16, 0.16, 1.65)
        out += f'<circle cx="{c[0]:.2f}" cy="{c[1]:.2f}" r="{0.05 * I.U:.2f}" fill="#c3c9d3"/>'
    for k in range(3):
        out += line((0.25, 0.16, 1.25 - k * 0.22), (1.9 - k * 0.35, 0.16, 1.25 - k * 0.22), "#c3c9d3", 1.1)
    out += poly(fl(0, 2.4, 0.16, 0.0, 0.42), BLUE, "none")
    return out, (2.4, 0.16, 1.8)


def i_admissions():
    """a clipboard standing up: the form, two boxes ticked in blue"""
    out = box(0, 0, 1.7, 0.14, 2.25, 0, WOOD, lip=False)
    out += poly(fl(0.14, 1.56, 0.14, 0.14, 1.95), "#ffffff", "none")
    out += box(0.5, 0.0, 0.7, 0.24, 0.24, 2.0, INKF, lip=False)                           # the clip
    for k in range(3):
        z = 1.6 - k * 0.45
        out += poly(fl(0.3, 0.55, 0.14, z - 0.12, z + 0.12), BLUE if k < 2 else "#d4d9e0", "none")
        out += line((0.7, 0.14, z), (1.38 - (k % 2) * 0.25, 0.14, z), "#c3c9d3", 1.2)
    return out, (1.7, 0.24, 2.25)


def i_fees():
    out = ""
    for k in range(3):
        out += box(0, 0.2, 2.0, 1.2, 0.12, k * 0.12, NOTE, lip=False)
    out += ring(1.0, 0.8, 0.365, 0.3, "none", "#8fbf9d", max(0.8, 0.06 * I.U))
    for k in range(3):
        out += coin(1.95, 1.75, k * 0.18, 0.46, 0.18, BLUEF if k == 2 else PAPER)
    return out, (2.4, 2.2, 0.54)


def i_hr():
    out = box(0, 0, 2.1, 0.62, 1.7, 0, WOOD)
    for r in range(3):
        for c in range(3):
            x0, z0 = 0.15 + c * 0.66, 0.15 + r * 0.52
            out += poly(fl(x0, x0 + 0.56, 0.62, z0, z0 + 0.42), "#ffffff" if (r + c) % 2 == 0 else "#f3ece0", HAIR, 0.4)
    out += box(0.86, 0.62, 0.44, 0.22, 0.3, 0.68, BLUEF, lip=False)                      # a payslip envelope sticking out
    return out, (2.1, 0.84, 1.7)


def i_record():
    out = box(0, 0, 1.9, 0.18, 2.2, 0, PAPER, lip=False)                                  # a pupil's record card
    out += box(0, 0, 0.75, 0.18, 0.3, 2.2, BLUEF, lip=False)                              # its tab
    c = P(0.55, 0.18, 1.55)
    out += f'<circle cx="{c[0]:.2f}" cy="{c[1]:.2f}" r="{0.3 * I.U:.2f}" fill="{BLUE}"/>'
    for k in range(3):
        out += line((1.0, 0.18, 1.75 - k * 0.27), (1.7 - (k % 2) * 0.25, 0.18, 1.75 - k * 0.27), "#c3c9d3", 1.2)
    for k in range(2):
        out += line((0.22, 0.18, 0.8 - k * 0.27), (1.65 - k * 0.4, 0.18, 0.8 - k * 0.27), "#c3c9d3", 1.2)
    return out, (1.9, 0.18, 2.5)


def i_ai():
    out = box(0, 0, 1.7, 0.16, 2.1, 0, PAPER, lip=False)
    for k in range(3):
        out += line((0.2, 0.16, 1.8 - k * 0.27), (1.45 - (k % 2) * 0.4, 0.16, 1.8 - k * 0.27), "#c3c9d3", 1.2)

    def spark(cx, z, r):
        return poly([P(cx, 0.16, z + r), P(cx + r * 0.22, 0.16, z + r * 0.22), P(cx + r, 0.16, z), P(cx + r * 0.22, 0.16, z - r * 0.22),
                     P(cx, 0.16, z - r), P(cx - r * 0.22, 0.16, z - r * 0.22), P(cx - r, 0.16, z), P(cx - r * 0.22, 0.16, z + r * 0.22)], BLUE, "none")
    out += spark(0.95, 0.6, 0.5) + spark(1.42, 1.05, 0.2)
    return out, (1.7, 0.16, 2.1)


def i_included():
    """an open box with what comes in it: a blue binder and a sheet"""
    out = poly(top(0, 0, 1.9, 1.4, 0.9), "#c3c9d3", "rgba(20,24,36,.16)")               # the opening
    out += box(0.35, 0.35, 0.3, 0.75, 1.15, 0.15, BLUEF, lip=False)                       # binder
    out += box(0.9, 0.45, 0.8, 0.08, 1.05, 0.2, PAPER, lip=False)                         # sheet
    out += poly(fl(0, 1.9, 1.4, 0, 0.9), WOOD[1], "rgba(20,24,36,.16)") + poly(fr(1.9, 0, 1.4, 0, 0.9), WOOD[2], "rgba(20,24,36,.16)")
    out += poly([P(0, 1.4, 0.9), P(1.9, 1.4, 0.9), P(1.9, 1.4, 0.82), P(0, 1.4, 0.82)], WOOD[0], "none")
    out += poly([P(0.0, 1.4, 0.9), P(-0.1, 1.9, 1.15), P(1.8, 1.9, 1.15), P(1.9, 1.4, 0.9)], WOOD[0], "rgba(20,24,36,.16)")   # front flap open
    return out, (1.9, 1.9, 1.35)


def i_training():
    out = box(0, 0, 2.4, 0.14, 1.5, 0.45, INKF, lip=False)                               # the screen
    out += poly(fl(0.1, 2.3, 0.14, 0.55, 1.85), "#ffffff", "none")
    for i, h in enumerate((0.35, 0.6, 0.95)):
        out += poly(fl(0.35 + i * 0.6, 0.75 + i * 0.6, 0.14, 0.65, 0.65 + h), BLUE if i == 2 else "#d4d9e0", "none")
    out += box(1.15, 0.0, 0.1, 0.1, 0.45, 0, DARK, lip=False) + box(0.75, -0.2, 0.9, 0.5, 0.05, 0, DARK, lip=False)
    return out, (2.4, 0.3, 1.95)


def i_questions():
    out = box(0, 0, 1.9, 0.5, 1.35, 0.35, WALL)
    out += poly([P(0.35, 0.5, 0.35), P(0.8, 0.5, 0.35), P(0.3, 0.5, 0.0)], WALL[1], "rgba(20,24,36,0.16)")
    out += txt(0.95, 0.5, 1.03, 1.0, "?", BLUE)
    return out, (1.9, 0.5, 1.7)


def i_sent():
    out = box(0, 0, 2.2, 1.5, 0.18, 0, PAPER, lip=False)
    out += poly([P(0, 0, 0.185), P(1.1, 0.8, 0.185), P(2.2, 0, 0.185)], "#e8effd", HAIR, 0.5)
    out += line((0, 1.5, 0.185), (1.1, 0.8, 0.185), "#c3c9d3", 1) + line((2.2, 1.5, 0.185), (1.1, 0.8, 0.185), "#c3c9d3", 1)
    out += I.cyl(1.75, 1.35, 0.42, 0.1, 0.18, BLUEF)
    a, b, c = P(1.58, 1.35, 0.29), P(1.72, 1.46, 0.29), P(1.95, 1.2, 0.29)
    out += f'<polyline points="{a[0]:.2f},{a[1]:.2f} {b[0]:.2f},{b[1]:.2f} {c[0]:.2f},{c[1]:.2f}" fill="none" stroke="#ffffff" stroke-width="{max(1, 0.09 * I.U):.2f}" stroke-linecap="round" stroke-linejoin="round"/>'
    return out, (2.2, 1.77, 0.3)


def i_contact():
    """a desk telephone, the handset in blue"""
    out = box(0, 0, 1.9, 1.4, 0.5, 0, WALL)
    for r in range(3):
        for c in range(3):
            out += poly(top(0.95 + c * 0.28, 0.6 + r * 0.24, 0.2, 0.16, 0.505), "#c9ced7", "none")
    out += box(0.12, 0.15, 0.55, 1.1, 0.12, 0.5, BLUEF, lip=False)                        # the handset
    out += box(0.12, 0.15, 0.55, 0.28, 0.22, 0.62, BLUEF, lip=False) + box(0.12, 0.97, 0.55, 0.28, 0.22, 0.62, BLUEF, lip=False)
    return out, (1.9, 1.4, 0.84)


def i_support():
    """a lifebuoy: a white ring with blue bands"""
    R, r, h = 1.0, 0.5, 0.3
    cx = cy = 1.0
    out = I.cyl(cx, cy, R, h, 0, PAPER, lid=False)
    pts = lambda rr, a0, a1, z: [P(cx + rr * math.cos(math.radians(a)), cy + rr * math.sin(math.radians(a)), z) for a in range(a0, a1 + 1, 6)]
    for k in range(4):
        a0 = k * 90
        out += poly(pts(R, a0, a0 + 45, h) + pts(r, a0 + 45, a0, h)[::1][::-1][::-1], "#ffffff", "none")
    for k in range(8):
        a0, a1 = k * 45, k * 45 + 45
        out += poly(pts(R, a0, a1, h) + list(reversed(pts(r, a0, a1, h))), BLUE if k % 2 == 0 else "#ffffff", "rgba(20,24,36,.12)", 0.5)
    c = P(cx, cy, h)
    out += f'<ellipse cx="{c[0]:.2f}" cy="{c[1]:.2f}" rx="{r * I.U * 0.866 * 1.414:.2f}" ry="{r * I.U * 0.5 * 1.414:.2f}" fill="#f4f5f7" stroke="rgba(20,24,36,.16)" stroke-width="0.6"/>'
    return out, (2.0, 2.0, 0.3)


def i_privacy():
    a, b = P(0.32, 0.3, 1.0), P(1.08, 0.3, 1.0)
    r = (b[0] - a[0]) / 2
    out = (f'<path d="M{a[0]:.2f} {a[1]:.2f} V{a[1] - r * 0.95:.2f} A{r:.2f} {r:.2f} 0 0 1 {b[0]:.2f} {b[1] - r * 0.95:.2f} V{b[1]:.2f}" fill="none" '
           f'stroke="#8f98a8" stroke-width="{0.2 * I.U:.2f}" stroke-linecap="round"/>')
    out += box(0, 0, 1.4, 0.6, 1.15, 0, BLUEF)
    k = P(0.7, 0.6, 0.62)
    out += f'<circle cx="{k[0]:.2f}" cy="{k[1]:.2f}" r="{0.12 * I.U:.2f}" fill="#ffffff"/>'
    out += poly(fl(0.66, 0.74, 0.6, 0.3, 0.6), "#ffffff", "none")
    return out, (1.4, 0.6, 2.0)


def i_terms():
    out = box(0, 0, 1.6, 0.16, 2.1, 0, PAPER, lip=False)
    for k in range(5):
        out += line((0.2, 0.16, 1.85 - k * 0.25), (1.4 - (k % 3) * 0.25, 0.16, 1.85 - k * 0.25), "#c3c9d3", 1.2)
    out += poly([P(0.98, 0.16, 0.45), P(0.9, 0.16, 0.02), P(1.05, 0.16, 0.12), P(1.15, 0.16, 0.0), P(1.2, 0.16, 0.45)], "#2853c2", "none")   # ribbon
    c = P(1.1, 0.16, 0.5)
    out += f'<circle cx="{c[0]:.2f}" cy="{c[1]:.2f}" r="{0.3 * I.U:.2f}" fill="{BLUE}"/><circle cx="{c[0]:.2f}" cy="{c[1]:.2f}" r="{0.18 * I.U:.2f}" fill="none" stroke="#ffffff" stroke-width="{max(0.7, 0.05 * I.U):.2f}"/>'
    return out, (1.6, 0.16, 2.1)


_nointernet_v1 = i_nointernet


def i_nointernet():
    svg, ext = _nointernet_v1()
    return svg.replace(f'stroke-width="{0.16 * I.U:.1f}"', f'stroke-width="{0.24 * I.U:.1f}"').replace(f'stroke-width="{0.13 * I.U:.1f}"', f'stroke-width="{0.17 * I.U:.1f}"'), ext


def i_government():
    out = box(0, 0, 2.2, 1.3, 1.4) + box(-0.05, -0.05, 2.3, 1.4, 0.1, 1.4, PALE)
    for z in (0.25, 0.85):
        out += win_f(0.2, 1.3, z, 4, 0.32, 0.34, 0.18)
    out += poly(fl(0.85, 1.35, 1.3, 0, 0.6), "#8f98a8", "none")
    fx, fy = -0.35, 1.5
    out += line((fx, fy, 0), (fx, fy, 2.3), "#8f97a5", max(1, 0.1 * I.U))
    out += poly([P(fx, fy, 2.3), P(fx + 0.95, fy, 2.18), P(fx + 0.95, fy, 1.7), P(fx, fy, 1.82)], BLUE, "none")
    return out, (2.2, 1.6, 2.3)


def i_mission():
    out = box(0, 0, 1.4, 2.0, 1.0)
    out += gable(-0.08, -0.08, 1.56, 2.16, 1.0, 0.9, GREYR)
    out += poly(fl(0.45, 0.95, 2.0, 0, 0.7), "#8f98a8", HAIR, 0.5)
    out += win_s(1.4, 0.35, 0.35, 3, 0.3, 0.4, 0.22)
    cx, w = 0.7, max(1.4, 0.14 * I.U)
    out += line((cx, 2.08, 1.4), (cx, 2.08, 2.3), BLUE, w) + line((cx - 0.26, 2.08, 2.0), (cx + 0.26, 2.08, 2.0), BLUE, w)
    return out, (1.4, 2.1, 2.3)


def i_day():
    out = box(0, 0, 2.6, 1.2, 0.9)
    for i in range(3):
        out += poly(fl(0.2 + i * 0.82, 0.48 + i * 0.82, 1.2, 0, 0.62), "#8f98a8", "none")
        out += poly(fl(0.55 + i * 0.82, 0.86 + i * 0.82, 1.2, 0.28, 0.62), GLASS, "none")
    out += gable(-0.1, -0.1, 2.8, 1.4, 0.9, 0.6, ROOF)
    return out, (2.6, 1.2, 1.5)


ICONS.update({"t-day": i_day, "solutions": i_solutions, "who": i_who, "pricing": i_pricing, "demo": i_demo, "signin": i_signin, "footer": i_footer,
              "admissions": i_admissions, "fees": i_fees, "hr-payroll": i_hr, "record": i_record, "ai": i_ai, "included": i_included,
              "training": i_training, "questions": i_questions, "sent": i_sent, "contact": i_contact, "support": i_support,
              "privacy": i_privacy, "terms": i_terms, "nointernet": i_nointernet, "t-government": i_government, "t-mission": i_mission})


def nav_icon(key, size=40, tile=True):
    """a page's icon: its object drawn in the campus projection, centred on a pale tile with a soft contact shadow.
    Below 28px the hairline details and text drop out so the silhouette and the blue part carry it."""
    import re
    if key in portal_art.SCENES:
        return portal_art.portal_icon(key, size, tile)
    fn = ICONS[key]
    U = size / 64 * 9.5
    I.U = U
    I.OX, I.OY = 0, 0
    svg0, ext = fn()
    xs, ys = [], []
    for x in (0, ext[0]):
        for y in (0, ext[1]):
            for z in (0, ext[2]):
                px, py = P(x, y, z)
                xs.append(px); ys.append(py)
    span = max(max(xs) - min(xs), (max(ys) - min(ys)) * 1.06)
    k = size * (0.66 if size >= 32 else 0.72) / span
    I.U = U * k
    xs = [v * k for v in xs]
    ys = [v * k for v in ys]
    I.OX = size / 2 - (min(xs) + max(xs)) / 2
    I.OY = size / 2 - (min(ys) + max(ys)) / 2 + size * 0.015
    svg, _ = fn()
    c = P(ext[0] / 2, ext[1] / 2, 0)
    rx = max(ext[0], ext[1], 0.9) * I.U * 0.62
    shadow = f'<ellipse cx="{c[0]:.2f}" cy="{c[1] + size * 0.02:.2f}" rx="{rx:.2f}" ry="{rx * 0.38:.2f}" fill="rgba(15,20,35,.10)" filter="url(#nsh{size})"/>'
    if size < 28:
        for col in DETAIL:
            svg = re.sub(r'<line [^>]*stroke="' + re.escape(col) + r'"[^>]*/>', "", svg)
        svg = re.sub(r"<text [^>]*>[^<]*</text>", "", svg)
        svg = svg.replace('stroke-width="0.7"', 'stroke-width="0.45"')
    defs = (f'<defs><filter id="nsh{size}" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="{max(0.6, size / 40):.2f}"/></filter>'
            '<filter id="sh" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="1.5"/></filter></defs>')
    inner = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" style="display:block;flex:none" aria-hidden="true">{defs}{shadow}{svg}</svg>'
    if not tile:
        return inner
    r = round(size * 0.24)
    return (f'<span style="width:{size}px;height:{size}px;border-radius:{r}px;background:#f4f5f7;box-shadow:inset 0 0 0 1px #e7e9ef;'
            f'display:flex;align-items:center;justify-content:center;flex:none;overflow:hidden">{inner}</span>')

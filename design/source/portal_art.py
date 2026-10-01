# -*- coding: utf-8 -*-
"""Portal illustrations and portal icons, direction AB.
Each portal has its own place in the school, drawn with the campus parts on its own plate:
Administration = the admin block and bursary queue; Teacher = a Form 3B classroom, cut away;
Parent = a guardian's home behind its durawall; Student = the library, a bench of readers and Tsavo House.
Icons are the same places reduced to one object each, drawn in the same projection."""
import iso_campus as ISO
from iso_campus import I, P, poly, line, box, fl, fr, top, sign, shadow, win_f, win_s, gable, person, kid, WALL, PALE, DARK, ROOF, GLASS, HAIR, BLUE

DEFS = ('<defs><filter id="sh" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3"/></filter>'
        '<filter id="floor" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="12"/></filter></defs>')
GROUND = {"Administration": ("#f6f7f9", "#e6e9ee", "#d8dce3"), "Teacher": ("#f6f7f9", "#e6e9ee", "#d8dce3"),
          "Parent": ("#eef3e9", "#dde7d4", "#cfdbc4"), "Student": ("#f6f7f9", "#e6e9ee", "#d8dce3")}
FLOOR = ("#efe7d9", "#e2d7c4", "#d6c8b1")
BOARD = "#34433d"
ROOF_GREY = ("#cfd4dc", "#b8bfca", "#a7afbc")


def setup(W, D, U, cx, cy):
    I.U = U
    I.OX = cx - (W - D) / 2 * U * I.C30
    I.OY = cy - (W + D) / 2 * U * I.S30


def slab(W, D, faces, th=0.35):
    foot = [P(0, 0, -th), P(W, 0, -th), P(W, D, -th), P(0, D, -th)]
    out = f'<g filter="url(#floor)" transform="translate(0 12)"><polygon points="{I.pts(foot)}" fill="rgba(15,20,35,0.12)"/></g>'
    out += box(0, 0, W, D, th, -th, faces, lip=False, edge=HAIR)
    a, b, c = P(0, D, 0), P(W, D, 0), P(W, 0, 0)
    return out + f'<polyline points="{I.pts([a, b, c])}" fill="none" stroke="#ffffff" stroke-width="1.1"/>'


def phone_in_hand(x, y, z=0.32):
    a = P(x, y, z)
    return f'<rect x="{a[0] - 1.6:.1f}" y="{a[1] - 3:.1f}" width="3.4" height="5.6" rx="0.9" fill="{BLUE}"/>'


# ---- the four scenes -----------------------------------------------------------------------------
def scene_admin():
    W, D = 8.0, 5.0
    out = slab(W, D, GROUND["Administration"])
    for i in range(int(W)):                                        # paving joints
        out += line((i + 0.5, 0, 0.003), (i + 0.5, D, 0.003), "rgba(20,24,36,0.05)", 0.7)
    svg, anc = ISO.admin(1.0, 0.7, 2.8, 1.6, 1.5)
    out += svg
    for k, (px, py, t) in enumerate(((4.25, 1.55, "#6f7a8c"), (4.6, 1.75, BLUE), (4.95, 1.95, "#8f98a8"), (5.3, 2.15, "#6f7a8c"))):
        out += person(px, py, t)                                   # the queue at the bursary window
    st, st_anc = ISO.stores(5.4, 0.4, 2.0, 1.1, 0.9)
    out += st
    out += ISO.jtree(7.3, 3.6, 0.8, "green") + ISO.jtree(0.6, 4.2, 0.75, ISO.JAC)
    labels = [("Administration", ("Fees", "Payroll", "HR"), *P(*anc)), (None, ("Stock",), *P(*st_anc))]
    return out, labels


def scene_teacher():
    W, D = 8.0, 5.0
    out = slab(W, D, GROUND["Teacher"])
    x0, y0, x1, y1, h = 1.2, 0.6, 6.8, 4.2, 1.05
    out += poly(top(x0, y0, x1 - x0, y1 - y0, 0.02), FLOOR[0], HAIR, 0.5)
    for i in range(1, 7):                                         # floor boards
        out += line((x0, y0 + i * (y1 - y0) / 7, 0.025), (x1, y0 + i * (y1 - y0) / 7, 0.025), "rgba(120,96,60,0.10)", 0.6)
    out += box(x0 - 0.15, y0 - 0.15, x1 - x0 + 0.15, 0.15, h, 0, WALL)          # back wall
    out += box(x0 - 0.15, y0, 0.15, y1 - y0, h, 0, WALL)                        # left wall
    out += poly(fl(x0 + 1.0, x0 + 3.6, y0, 0.36, 0.86), BOARD, HAIR, 0.6)       # chalkboard
    out += line((x0 + 1.25, y0, 0.74), (x0 + 2.4, y0, 0.74), "rgba(255,255,255,0.75)", 0.9)
    out += line((x0 + 1.25, y0, 0.62), (x0 + 2.0, y0, 0.62), "rgba(255,255,255,0.6)", 0.9)
    out += line((x0 + 2.6, y0, 0.5), (x0 + 3.3, y0, 0.5), "rgba(255,255,255,0.6)", 0.9)
    out += poly(fl(x0 + 4.0, x0 + 5.2, y0, 0.32, 0.86), "#f7f3ea", HAIR, 0.5)   # timetable on the wall
    for r in range(4):
        out += line((x0 + 4.1, y0, 0.78 - r * 0.12), (x0 + 5.1, y0, 0.78 - r * 0.12), "rgba(20,24,36,0.18)", 0.6)
    for k in range(3):                                            # windows on the left wall
        out += poly(fr(x0, y0 + 0.5 + k * 1.1, y0 + 1.1 + k * 1.1, 0.42, 0.86), GLASS, HAIR, 0.5)
    tones = ("#6f7a8c", BLUE, "#8f98a8", "#6f7a8c", "#8f98a8", BLUE)
    n = 0
    for r in range(3):                                            # desks in rows, a pupil at each
        for c_ in range(4):
            dx, dy = x0 + 0.7 + c_ * 1.25, y0 + 1.25 + r * 0.95
            out += box(dx, dy, 0.6, 0.36, 0.3, 0, ("#f7f3ea", "#e6dccb", "#d8ccb7"), lip=False)
            out += kid(dx + 0.3, dy + 0.52, tones[n % 6])
            n += 1
    out += person(x0 + 4.6, y0 + 0.75, "#3a404c") + phone_in_hand(x0 + 4.75, y0 + 0.78, 0.3)   # Ms Sibanda with the tablet
    labels = [("Teacher", ("Register", "Marks", "Schemes of work"), *P(x0 + 2.3, y0, 1.0))]
    return out, labels


def house(x, y, w=2.6, d=1.7, h=1.0):
    yy = y + d
    out = shadow(x, y, w, d + 0.5, 0.6) + box(x, y, w, d, h)
    out += box(x + 0.2, yy, w - 0.4, 0.5, 0.06, 0, PALE, lip=False)                      # veranda slab
    for px in (x + 0.25, x + w - 0.3):
        out += box(px, yy + 0.4, 0.07, 0.07, h - 0.06, 0.06, WALL, lip=False)
    out += poly(fl(x + 1.1, x + 1.5, yy, 0, 0.66), BLUE, HAIR, 0.5)                       # the blue door
    out += poly(fl(x + 0.35, x + 0.85, yy, 0.32, 0.66), GLASS, HAIR, 0.5) + poly(fl(x + 1.8, x + 2.3, yy, 0.32, 0.66), GLASS, HAIR, 0.5)
    out += win_s(x + w, y + 0.4, 0.32, 1, 0.6, 0.34, 0.2)
    out += gable(x - 0.12, y - 0.12, w + 0.24, d + 0.62, h, 0.6, ROOF_GREY)
    return out, (x + w / 2, y + d / 2, h + 0.6)


def durawall(x0, x1, y, h=0.42, gap=None):
    out = ""
    segs = [(x0, x1)] if not gap else [(x0, gap[0]), (gap[1], x1)]
    for a, b in segs:
        out += box(a, y, b - a, 0.12, h, 0, ("#eceef2", "#dfe2e8", "#cfd4dc"), lip=False)
        n = max(1, int((b - a) / 0.5))
        for k in range(1, n):
            out += line((a + k * (b - a) / n, y + 0.12, 0), (a + k * (b - a) / n, y + 0.12, h), "rgba(20,24,36,0.10)", 0.6)
    return out


def scene_parent():
    W, D = 8.0, 5.0
    out = slab(W, D, GROUND["Parent"])
    out += durawall(0.3, 7.7, 0.25)                                           # back and side walls
    svg, anc = house(2.2, 0.9, 2.8, 1.7, 1.0)
    out += svg
    out += ISO.jtree(6.6, 1.3, 1.0, "green") + ISO.jtree(1.0, 1.6, 0.8, "green")
    out += poly(top(3.3, 3.1, 0.5, 1.6, 0.004), "#e4e7ec", "none")                     # path to the gate
    out += person(3.6, 2.95, "#6f7a8c") + phone_in_hand(3.75, 2.98, 0.3)             # Rudo Moyo with her phone
    out += kid(4.1, 3.05, BLUE)
    out += durawall(0.3, 7.7, 4.55, 0.42, gap=(3.2, 3.9))                          # front durawall with the gate
    labels = [("Parent", ("Attendance", "Fees", "Reports"), *P(*anc))]
    return out, labels


def scene_student():
    W, D = 8.0, 5.0
    out = slab(W, D, GROUND["Student"])
    lib, lib_anc = ISO.library(0.8, 0.6, 2.6, 1.4, 1.0)
    hos, hos_anc = ISO.hostel(4.3, 0.5, "Tsavo House", 3.2, 1.3, 1.5)
    out += lib + hos
    out += ISO.jtree(3.75, 2.6, 0.85, ISO.JAC) + ISO.jtree(7.4, 3.4, 0.8, ISO.JAC)
    out += box(1.2, 3.25, 1.6, 0.35, 0.2, 0, ("#e9dcc6", "#d9c8aa", "#c9b594"), lip=False)   # bench
    out += kid(1.45, 3.2, BLUE) + kid(1.9, 3.2, "#6f7a8c") + kid(2.35, 3.2, "#8f98a8")
    out += box(5.0, 3.6, 0.45, 0.3, 0.12, 0, ("#ffffff", "#e5e8ed", "#d4d9e0"), lip=False)    # a pile of books
    out += box(5.03, 3.62, 0.4, 0.27, 0.1, 0.12, ROOF, lip=False)
    out += kid(5.7, 3.7, BLUE) + kid(6.1, 3.85, "#6f7a8c")
    labels = [("Student", ("Timetable", "Homework", "E-library"), *P(*lib_anc)), (None, ("Hostel",), *P(*hos_anc))]
    return out, labels


SCENES = {"Administration": scene_admin, "Teacher": scene_teacher, "Parent": scene_parent, "Student": scene_student}


def portal_scene(name, w=560, h=400, U=40, cx=None, cy=None, labels=True):
    """one portal's place on its plate; labels=False for thumbnails"""
    setup(8.0, 5.0, U, cx if cx is not None else w / 2, cy if cy is not None else h * 0.6)
    svg, lab = SCENES[name]()
    out = (f'<div style="position:relative;width:{w}px;height:{h}px">'
           f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="position:absolute;left:0;top:0" aria-hidden="true">{DEFS}{svg}</svg>')
    if labels:
        out += pills(lab)
    return out + '</div>'


# ---- icons: one object per portal, same projection -----------------------------------------------
def _icon_svg(name):
    if name == "Administration":
        out = box(0, 0, 2.4, 1.7, 2.1) + box(-0.08, -0.08, 2.56, 1.86, 0.22, 2.1, ROOF, lip=False)
        for z in (0.35, 1.15):
            out += win_f(0.25, 1.7, z, 3, 0.45, 0.45, 0.28)
            out += win_s(2.4, 0.25, z, 2, 0.5, 0.45, 0.25)
        return out, (2.4, 1.7, 2.32)
    if name == "Teacher":
        out = box(0, 0, 3.0, 1.3, 1.1)
        for i in range(3):
            out += poly(fl(0.25 + i * 0.95, 0.55 + i * 0.95, 1.3, 0, 0.75), "#8f98a8", "none")
            out += poly(fl(0.62 + i * 0.95, 0.98 + i * 0.95, 1.3, 0.35, 0.75), GLASS, "none")
        out += gable(-0.12, -0.12, 3.24, 1.54, 1.1, 0.7, ROOF)
        return out, (3.0, 1.3, 1.8)
    if name == "Parent":
        out = box(0, 0, 2.3, 1.8, 1.15)
        out += poly(fl(0.9, 1.4, 1.8, 0, 0.8), BLUE, "none")
        out += poly(fl(0.2, 0.7, 1.8, 0.4, 0.8), GLASS, "none") + poly(fl(1.6, 2.1, 1.8, 0.4, 0.8), GLASS, "none")
        out += gable(-0.12, -0.12, 2.54, 2.04, 1.15, 0.85, ROOF_GREY)
        return out, (2.3, 1.8, 2.0)
    out = box(0, 0, 2.6, 1.9, 0.42, 0, ("#ffffff", "#e5e8ed", "#d4d9e0"))
    out += box(0.12, 0.08, 2.36, 1.74, 0.42, 0.42, PALE)
    out += box(0.0, 0.02, 2.56, 1.84, 0.42, 0.84, ROOF)
    for z in (0.14, 0.28, 0.56, 0.7):
        out += line((0.15 if z > 0.42 else 0.05, 1.9 if z < 0.42 else 1.82, z), (2.5, 1.9 if z < 0.42 else 1.82, z), "rgba(20,24,36,0.18)", 0.6)
    return out, (2.6, 1.9, 1.26)


def portal_icon(name, size=48, tile=True):
    """the portal's icon: its object drawn small, centred on a white tile"""
    U = size / 64 * 9.5
    I.U = U
    svg0, ext = _icon_svg(name)
    # centre the object's bounding box in the square
    xs, ys = [], []
    for x in (0, ext[0]):
        for y in (0, ext[1]):
            for z in (0, ext[2]):
                I.OX, I.OY = 0, 0
                px, py = P(x, y, z)
                xs.append(px); ys.append(py)
    I.OX = size / 2 - (min(xs) + max(xs)) / 2
    I.OY = size / 2 - (min(ys) + max(ys)) / 2 + size * 0.02
    svg, _ = _icon_svg(name)
    inner = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" style="display:block;flex:none" aria-hidden="true">{svg}</svg>'
    if not tile:
        return inner
    r = round(size * 0.24)
    return (f'<span style="width:{size}px;height:{size}px;border-radius:{r}px;background:#f4f5f7;box-shadow:inset 0 0 0 1px #e7e9ef;'
            f'display:flex;align-items:center;justify-content:center;flex:none;overflow:hidden">{inner}</span>')


def pills(labels):
    """labels on stems: the portal pill carries the portal's own icon; modules are grey chips"""
    PILL = ("display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 11px 0 4px;border:1px solid #e7e9ef;border-radius:999px;background:#fff;"
            "box-shadow:0 6px 14px -8px rgba(15,20,35,.35);font:500 12.5px 'Atkinson Hyperlegible Next',sans-serif;color:#0b0c14;white-space:nowrap")
    CHIP = ("display:inline-flex;align-items:center;height:22px;padding:0 8px;border-radius:999px;background:#f1f3f6;border:1px solid #e3e6eb;"
            "font:500 11.5px 'Atkinson Hyperlegible Next',sans-serif;color:#3b3d47;white-space:nowrap")
    out = ""
    for portal, chips, ax, ay in labels:
        stem = 22 if portal else 16
        out += (f'<span style="position:absolute;left:{ax - 0.5:.1f}px;top:{ay - stem:.0f}px;width:1px;height:{stem}px;background:#9aa1ad"></span>'
                f'<span style="position:absolute;left:{ax - 3:.1f}px;top:{ay - 3:.1f}px;width:6px;height:6px;border-radius:3px;background:#fff;border:1.5px solid #0b0c14;box-sizing:border-box"></span>')
        inner = (f'<span style="{PILL}">{portal_icon(portal, 22)}{portal} portal</span>' if portal else "") + "".join(f'<span style="{CHIP}">{c}</span>' for c in chips)
        top_ = ay - stem - (30 if portal else 22)
        out += f'<span style="position:absolute;left:{ax:.0f}px;top:{top_:.0f}px;transform:translateX(-50%);display:flex;gap:5px;align-items:center">{inner}</span>'
    return out

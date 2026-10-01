# -*- coding: utf-8 -*-
"""Direction A: Mukuvisi High School drawn as one isometric campus with the Corelith street's parts.
Every building faces a path the viewer can see. Labels sit on stems: the four portals in blue-bordered
pills where each one is used, the modules as small grey chips on the building they run."""
import sys
PP = "/tmp/claude-0/-home-claude/bcef0de9-d748-5cac-a3e6-27f5c8608e47/scratchpad/pp"
sys.path[:0] = [PP, PP + "/../flare"]
import iso5 as I  # noqa: E402
from iso5 import P, poly, line, box, fl, fr, top, sign, shadow, win_f, win_s, roller, gable, tree, person, kid, kombi, WALL, PALE, DARK, ROOF, GLASS, HAIR, BLUE  # noqa

GREY_ROOF = ("#d9dde4", "#c3c9d3", "#b3bac6")
FIELD = ("#dfe9d6", "#cfdcc4")
JAC = "jacaranda"


def jtree(x, y, s=1.0, kind="green"):
    if kind == JAC:
        a = P(x, y, 0)
        out = f'<ellipse cx="{a[0] + 5:.1f}" cy="{a[1] + 2:.1f}" rx="{0.55 * s * I.U:.1f}" ry="{0.24 * s * I.U:.1f}" fill="rgba(15,20,35,0.08)" filter="url(#sh)"/>'
        out += line((x, y, 0), (x, y, 0.72 * s), "#8a8f99", 1.8)
        for dz, rx, ry, f in ((0.7, 0.62, 0.28, "#c9bdf0"), (0.9, 0.46, 0.2, "#ddd5f7")):
            c = P(x, y, dz * s)
            out += f'<ellipse cx="{c[0]:.1f}" cy="{c[1]:.1f}" rx="{rx * s * I.U:.1f}" ry="{ry * s * I.U:.1f}" fill="{f}" stroke="rgba(20,24,36,0.10)" stroke-width="0.7"/>'
        return out
    return tree(x, y, s, kind)


def classroom(x, y, name, w=3.6, d=1.25, h=0.9):
    """a classroom block: veranda on pillars, a door and a window per classroom, blue roof"""
    yy, V = y + d, 0.42
    out = shadow(x, y, w, d + V, 0.6) + box(x, y, w, d, h)
    n = int(w / 0.8)
    for i in range(n):
        cx = x + 0.2 + i * 0.8
        out += poly(fl(cx, cx + 0.24, yy, 0, 0.6), "#8f98a8", HAIR, 0.5)
        out += poly(fl(cx + 0.36, cx + 0.68, yy, 0.24, 0.56), GLASS, HAIR, 0.5)
    out += win_s(x + w, y + 0.25, 0.3, 2, 0.32, 0.32, 0.25)
    out += box(x, yy, w, V, 0.05, 0, PALE, lip=False)
    for i in range(7):
        px = x + 0.06 + i * (w - 0.18) / 6
        out += box(px, yy + V - 0.12, 0.08, 0.08, h - 0.05, 0.05, WALL, lip=False)
    out += gable(x - 0.1, y - 0.1, w + 0.2, d + V + 0.12, h, 0.55)
    out += sign(x + w - 1.0, x + w - 0.1, yy + V + 0.02, 0.62, 0.84, name)
    return out, (x + w / 2, y + (d + V) / 2, h + 0.55)


def admin(x, y, w=2.6, d=1.5, h=1.5):
    yy = y + d
    out = shadow(x, y, w, d, 0.8) + box(x, y, w, d, h)
    out += box(x - 0.05, y - 0.05, w + 0.1, d + 0.1, 0.1, h, PALE)
    for z in (0.28, 0.9):
        out += win_f(x + 0.2, yy, z, 4, 0.36, 0.34, 0.24, lit=((2,) if z > 0.5 else ()))
        out += win_s(x + w, y + 0.22, z, 2, 0.4, 0.34, 0.3)
    out += poly(fl(x + 1.0, x + 1.5, yy, 0, 0.62), "#8f98a8", HAIR, 0.5)             # door
    out += box(x + 0.85, yy, 0.8, 0.32, 0.05, 0.66, PALE)                               # canopy
    out += sign(x + 0.35, x + w - 0.35, yy, h - 0.2, h + 0.06, "Administration")
    # bursary counter window on the side, with its own small sign
    out += poly(fr(x + w, y + 0.9, y + 1.35, 0.3, 0.62), "#9fb3d9", HAIR, 0.5)
    # flagpole
    fx, fy = x - 0.25, yy + 0.35
    out += line((fx, fy, 0), (fx, fy, 2.2), "#8f97a5", 1.3)
    out += poly([P(fx, fy, 2.2), P(fx + 0.5, fy, 2.12), P(fx + 0.5, fy, 1.87), P(fx, fy, 1.95)], "#12805c", "none")
    return out, (x + w / 2, y + d / 2, h + 0.1)


def library(x, y, w=2.4, d=1.4, h=1.0):
    yy = y + d
    out = shadow(x, y, w, d, 0.6) + box(x, y, w, d, h)
    out += win_f(x + 0.18, yy, 0.18, 4, 0.34, 0.62, 0.2)
    out += win_s(x + w, y + 0.2, 0.25, 2, 0.4, 0.5, 0.2)
    out += gable(x - 0.08, y - 0.08, w + 0.16, d + 0.16, h, 0.45, GREY_ROOF)
    out += sign(x + 0.5, x + w - 0.5, yy + 0.09, h + 0.06, h + 0.3, "Library")
    return out, (x + w / 2, y + d / 2, h + 0.45)


def hostel(x, y, name, w=4.2, d=1.35, h=1.6):
    yy = y + d
    out = shadow(x, y, w, d, 0.8) + box(x, y, w, d, h)
    out += box(x - 0.05, y - 0.05, w + 0.1, d + 0.1, 0.1, h, PALE)
    for z in (0.28, 0.98):
        out += win_f(x + 0.2, yy, z, 8, 0.3, 0.36, 0.2)
        out += win_s(x + w, y + 0.22, z, 2, 0.36, 0.36, 0.3)
    out += box(x, yy, w, 0.36, 0.05, 0.74, PALE, lip=False)                           # walkway on the first floor
    out += line((x, yy + 0.36, 0.95), (x + w, yy + 0.36, 0.95), "#aab1bd", 1)
    out += poly(fl(x + w / 2 - 0.2, x + w / 2 + 0.2, yy, 0, 0.62), "#8f98a8", HAIR, 0.5)
    out += sign(x + 0.3, x + 1.9, yy, h - 0.3, h - 0.06, name)
    return out, (x + w / 2, y + d / 2, h + 0.1)


def stores(x, y, w=2.2, d=1.3, h=0.95):
    yy = y + d
    out = shadow(x, y, w, d) + box(x, y, w, d, h)
    out += box(x - 0.05, y - 0.05, w + 0.1, d + 0.1, 0.1, h, PALE)
    out += roller(x + 0.2, x + 1.1, yy, 0.66)
    out += win_f(x + 1.35, yy, 0.3, 2, 0.26, 0.26, 0.14)
    out += sign(x + 1.25, x + w - 0.12, yy, h - 0.3, h - 0.06, "Stores")
    # sacks by the door
    for i, (dx, dz) in enumerate(((0.0, 0), (0.22, 0), (0.11, 0.14))):
        out += box(x + 1.2 + dx, yy + 0.15, 0.2, 0.28, 0.14, dz, ("#efe6d6", "#e3d6bf", "#d6c6aa"), lip=False)
    return out, (x + w / 2, y + d / 2, h + 0.1)


def field(x, y, w, d):
    out = poly(top(x, y, w, d, 0.004), FIELD[0], "none")
    m = 0.2
    out += poly(top(x + m, y + m, w - 2 * m, d - 2 * m, 0.006), "none", "rgba(255,255,255,0.95)", 1.1)
    out += line((x + w / 2, y + m, 0.006), (x + w / 2, y + d - m, 0.006), "rgba(255,255,255,0.95)", 1.1)
    c = P(x + w / 2, y + d / 2, 0.006)
    out += f'<ellipse cx="{c[0]:.1f}" cy="{c[1]:.1f}" rx="{0.62 * I.U:.1f}" ry="{0.36 * I.U:.1f}" fill="none" stroke="rgba(255,255,255,0.95)" stroke-width="1.1"/>'
    for gx in (x + m + 0.02, x + w - m - 0.02):                                               # goalposts
        y0, y1 = y + d / 2 - 0.45, y + d / 2 + 0.45
        out += line((gx, y0, 0), (gx, y0, 0.34), "#ffffff", 1.8) + line((gx, y1, 0), (gx, y1, 0.34), "#ffffff", 1.8)
        out += line((gx, y0, 0.34), (gx, y1, 0.34), "#ffffff", 1.8)
    return out


def gate(x, y, w=3.2):
    """the school gate on the front road: two pillars carrying the name board, a guard hut and a boom"""
    out = ""
    # guard hut inside the gate
    out += shadow(x + w - 0.95, y - 1.05, 0.7, 0.7) + box(x + w - 0.95, y - 1.05, 0.7, 0.7, 0.62)
    out += box(x + w - 1.0, y - 1.1, 0.8, 0.8, 0.06, 0.62, PALE)
    out += poly(fl(x + w - 0.85, x + w - 0.45, y - 0.35, 0.3, 0.52), GLASS, "none")
    for px in (x, x + w):
        out += box(px - 0.12, y - 0.12, 0.24, 0.24, 0.9, 0, DARK, lip=False)
    out += poly(fl(x + 0.1, x + w - 0.1, y, 0.62, 0.9), "#ffffff", HAIR, 0.6)
    size = 0.28 * I.U * 0.62
    out += (f'<text transform="{I.fmat(x + w / 2, y, 0.76)}" text-anchor="middle" dominant-baseline="central" font-family="{I.FONT}" '
            f'font-size="{size:.1f}" font-weight="600" fill="{I.INKG}">Mukuvisi High School</text>')
    for i in range(6):                                                                       # the boom, red and white
        a0, a1 = x + 0.2 + i * 0.28, x + 0.2 + (i + 1) * 0.28
        out += line((a0, y - 0.02, 0.36), (a1, y - 0.02, 0.36), "#e0533f" if i % 2 == 0 else "#ffffff", 2.4)
    return out


def path_(y0, y1, W):
    out = poly(top(0, y0, W, y1 - y0, 0.002), "#eceef2", "none")
    out += line((0, y0, 0.004), (W, y0, 0.004), "rgba(20,24,36,0.08)", 0.8) + line((0, y1, 0.004), (W, y1, 0.004), "rgba(20,24,36,0.08)", 0.8)
    return out


def scene(width=1280, height=720, U=45, cx=640, cy=404):
    W, D = 16.0, 7.8
    I.U, I.W, I.D = U, W, D
    I.OX = cx - (W - D) / 2 * U * I.C30
    I.OY = cy - (W + D) / 2 * U * I.S30
    parts = [I.base(), path_(2.5, 3.1, W), I.road(6.6, 7.45)]
    labels = []
    back, front = [], []

    def put(lst, key, res, portal=None, chips=()):
        svg, anc = res
        lst.append((key, svg))
        sx, sy = P(*anc)
        labels.append((portal, chips, sx, sy))

    # back row faces the inner path
    put(back, 0.4, classroom(0.4, 0.35, "Block A", 3.4), "Teacher", ("Registers", "Marks"))
    put(back, 4.4, admin(4.4, 0.5), "Administration", ("Fees", "Payroll", "HR"))
    put(back, 7.7, library(7.7, 0.7, 2.3), "Student", ("E-library",))
    put(back, 10.6, hostel(10.6, 0.75, "Tsavo House", 4.0), None, ("Boarding",))
    for tx, ty, s_, k in ((15.2, 0.9, 1.0, JAC), (15.5, 2.0, 0.75, "green"), (7.3, 0.5, 0.7, "green"), (10.25, 0.55, 0.8, JAC)):
        back.append((tx, jtree(tx, ty, s_, k)))
    back.append((3.0, "".join(kid(px, py, t) for px, py, t in ((1.2, 2.72, "#6f7a8c"), (1.5, 2.86, BLUE), (2.3, 2.78, "#8f98a8"), (5.9, 2.82, "#6f7a8c"), (9.2, 2.8, BLUE)))))
    # front row faces the front road
    put(front, 0.4, classroom(0.4, 3.55, "Block C", 3.4), None, ())
    front.append((4.3, field(4.4, 3.5, 5.3, 2.75)))
    front.append((5.5, "".join(kid(px, py, t) for px, py, t in ((5.6, 4.4, BLUE), (6.7, 5.2, "#6f7a8c"), (7.8, 4.7, "#8f98a8"), (8.8, 5.5, BLUE), (7.1, 4.1, "#6f7a8c")))))
    put(front, 10.3, stores(10.3, 3.85, 2.2, 1.3), None, ("Stock",))
    front.append((12.6, gate(12.3, 6.35, 2.5)))
    for tx, ty, s_, k in ((3.95, 5.9, 0.7, JAC), (10.0, 6.0, 0.72, "green"), (15.4, 4.3, 0.9, JAC), (12.8, 4.6, 0.6, "green")):
        front.append((tx + 0.01, jtree(tx, ty, s_, k)))
    front.append((9.0, kombi(8.6, 6.7)))
    front.append((15.9, person(15.75, 6.72, "#6f7a8c") + person(15.5, 6.92, BLUE)))
    for lst in (back, front):
        lst.sort(key=lambda t: t[0])
        parts += [s for _, s in lst]
    # the parent portal is used at home: its label sits on the parent at the gate
    sx, sy = P(15.5, 6.92, 0.5)
    labels.append(("Parent", (), sx, sy, "right"))
    defs = ('<defs><filter id="sh" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3"/></filter>'
            '<filter id="floor" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="16"/></filter></defs>')
    svg = f'<svg width="{width}" height="{height}" viewBox="0 0 {width} {height}" style="position:absolute;left:0;top:0" aria-hidden="true">{defs}{"".join(parts)}</svg>'
    return svg, labels


PORTAL_ICON = {"Administration": "building-2", "Teacher": "book-6", "Parent": "home-3", "Student": "school"}


def pills(labels, ic):
    PILL = ("display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 11px 0 4px;border:1px solid #e7e9ef;border-radius:999px;background:#fff;"
            "box-shadow:0 6px 14px -8px rgba(15,20,35,.35);font:500 12.5px 'Atkinson Hyperlegible Next',sans-serif;color:#0b0c14;white-space:nowrap")
    CHIP = ("display:inline-flex;align-items:center;height:22px;padding:0 8px;border-radius:999px;background:#f1f3f6;border:1px solid #e3e6eb;"
            "font:500 11.5px 'Atkinson Hyperlegible Next',sans-serif;color:#3b3d47;white-space:nowrap")
    out = ""
    for lb in labels:
        portal, chips, ax, ay = lb[:4]
        side = lb[4] if len(lb) > 4 else "centre"
        stem = (22 if portal else 16) if side == "centre" else 34
        out += (f'<span style="position:absolute;left:{ax - 0.5:.1f}px;top:{ay - stem:.0f}px;width:1px;height:{stem}px;background:#9aa1ad"></span>'
                f'<span style="position:absolute;left:{ax - 3:.1f}px;top:{ay - 3:.1f}px;width:6px;height:6px;border-radius:3px;background:#fff;border:1.5px solid #0b0c14;box-sizing:border-box"></span>')
        inner = ""
        if portal:
            import portal_art
            tile = portal_art.portal_icon(portal, 22)
            inner += f'<span style="{PILL}">{tile}{portal} portal</span>'
        if chips:
            inner += "".join(f'<span style="{CHIP}">{c}</span>' for c in chips)
        top_ = ay - stem - (30 if portal else 22)
        tf = "translateX(-50%)" if side == "centre" else "translateX(-14px)"
        out += f'<span style="position:absolute;left:{ax:.0f}px;top:{top_:.0f}px;transform:{tf};display:flex;gap:5px;align-items:center">{inner}</span>'
    return out

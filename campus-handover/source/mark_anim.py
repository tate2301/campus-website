# -*- coding: utf-8 -*-
"""One mark, recorded once, arriving everywhere: Ms Sibanda submits Tanaka's 71% and it travels across the campus drawing
to the staffroom, the Head's view, Tanaka's portal and his mother's phone. Animated with CSS; an 8 second loop."""
from ds import *
import iso_campus as ISO
import portal_art

DUR = 8
CSS = ""          # keyframes, collected as the pieces are built; canvasio puts them in the helmet


def _kf(name, frames):
    global CSS
    body = " ".join(f"{p}%{{{v}}}" for p, v in frames)
    rule = f"@keyframes {name}{{{body}}}"
    if rule not in CSS:
        CSS += rule + "\n"
    return name


def entry_card(w=260):
    """the marks entry: three pupils, Tanaka's mark typed, the submit button that turns to submitted"""
    rows = [("Tanaka Moyo", "71", True), ("Tendai Chirwa", "58", False), ("Ruvimbo Gumbo", "77", False)]
    r = "".join(f'<div style="display:flex;align-items:center;justify-content:space-between;padding:7px 0;border-top:1px solid {LINE};font:400 13px {SANS}">{n}'
                f'<span style="width:46px;height:26px;border-radius:7px;box-shadow:inset 0 0 0 {"1.5px " + BLUE if hot else "1px " + LINE};display:flex;align-items:center;justify-content:center;'
                f'font:600 13px {SANS};color:{INK}">{v}</span></div>' for n, v, hot in rows)
    press = _kf("cmk-press", [(0, "opacity:1"), (16, "opacity:1"), (19, "opacity:0"), (96, "opacity:0"), (100, "opacity:1")])
    done = _kf("cmk-done", [(0, "opacity:0"), (16, "opacity:0"), (19, "opacity:1"), (96, "opacity:1"), (100, "opacity:0")])
    tap = _kf("cmk-tap", [(0, "transform:scale(1)"), (13, "transform:scale(1)"), (15, "transform:scale(.94)"), (18, "transform:scale(1)"), (100, "transform:scale(1)")])
    btn = (f'<div style="position:relative;height:38px;margin-top:10px;animation:{tap} {DUR}s infinite">'
           f'<span style="position:absolute;inset:0;border-radius:10px;background:{BLUE};color:#fff;display:flex;align-items:center;justify-content:center;gap:8px;font:600 13.5px {SANS};animation:{press} {DUR}s infinite">'
           f'{ic("send-plane", 14, "#fff")}Submit marks</span>'
           f'<span style="position:absolute;inset:0;border-radius:10px;background:{OKS};color:{OK};display:flex;align-items:center;justify-content:center;gap:8px;font:600 13.5px {SANS};opacity:0;animation:{done} {DUR}s infinite">'
           f'{ic("check-circle", 14, OK)}Recorded once · 4 places</span></div>')
    return (f'<div style="width:{w}px;border-radius:16px;background:#fff;box-shadow:0 0 0 1px {LINE},0 18px 30px -18px rgba(11,12,20,.35);padding:14px 14px 14px;box-sizing:border-box">'
            f'<div style="display:flex;align-items:center;gap:8px;margin-bottom:8px">{portal_art.portal_icon("Teacher", 24)}'
            f'<div><div style="font:600 13.5px {SANS}">Mathematics · test 2</div><div style="font:400 11.5px {SANS};color:{MUTED}">Form 3B · Ms Sibanda</div></div></div>{r}{btn}</div>')


# the route the mark walks, in campus units on the ground: out of Form 3B onto the inner path, along it to the admin
# block's door, on to the library, then east past the stores, south through the school gate to Rudo Moyo on the road
ROUTE = [("Teacher", (2.1, 2.05)), (None, (2.1, 2.8)), (None, (5.65, 2.8)), ("Administration", (5.65, 2.05)), (None, (5.65, 2.8)),
         (None, (8.85, 2.8)), ("Student", (8.85, 2.18)), (None, (8.85, 2.8)), (None, (13.55, 2.8)), (None, (13.55, 7.02)),
         ("Parent", (15.25, 7.02))]
STOPS = {"Teacher": ("Marks", "Ms Sibanda's class list"), "Administration": ("Head's view", "class average 64%"),
         "Student": ("Tanaka's portal", "Mathematics 71%"), "Parent": ("Rudo Moyo's phone", "Tanaka scored 71%")}


def _rounded(pts, r=9):
    """an SVG path through the points with each corner rounded, so the walk turns like a person on a path"""
    import math
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(1, len(pts) - 1):
        (x0, y0), (x1, y1), (x2, y2) = pts[i - 1], pts[i], pts[i + 1]
        l1, l2 = math.dist((x0, y0), (x1, y1)), math.dist((x1, y1), (x2, y2))
        if l1 < 1 or l2 < 1:
            continue
        k1, k2 = min(r, l1 / 2) / l1, min(r, l2 / 2) / l2
        a = (x1 - (x1 - x0) * k1, y1 - (y1 - y0) * k1)
        b = (x1 + (x2 - x1) * k2, y1 + (y2 - y1) * k2)
        d += f" L{a[0]:.1f} {a[1]:.1f} Q{x1:.1f} {y1:.1f} {b[0]:.1f} {b[1]:.1f}"
    d += f" L{pts[-1][0]:.1f} {pts[-1][1]:.1f}"
    return d


def scene(w=620, h=460):
    """the campus with the mark walking the school's own paths to every portal"""
    import math
    svg, labels = ISO.scene(w, h, U=23, cx=330, cy=246)
    anc = {l[0]: (l[2], l[3]) for l in labels if l[0]}
    pts = [ISO.P(x, y, 0.02) for _, (x, y) in ROUTE]                                # world to screen, after the scene set the projection
    stop_xy = {p: pts[i] for i, (p, _) in enumerate(ROUTE) if p}                     # before any icon resets the projection
    d = _rounded(pts)
    seg = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    L = sum(seg)
    # timeline: appear at 19%, walk to 80%, pausing 3% at each stop; the trail draws as it walks
    t0, t1, hold = 20.0, 82.0, 3.0
    n_hold = sum(1 for p, _ in ROUTE[1:] if p)
    walk = (t1 - t0 - hold * n_hold) / L
    t, acc, go, trail, arrive = t0, 0.0, [(0, "offset-distance:0%;opacity:0"), (t0 - 1, "offset-distance:0%;opacity:0"), (t0, "offset-distance:0%;opacity:1")], \
        [(0, f"stroke-dashoffset:{L:.0f}"), (t0, f"stroke-dashoffset:{L:.0f}")], {ROUTE[0][0]: t0}
    for i, ln in enumerate(seg):
        t += ln * walk
        acc += ln
        f = acc / L * 100
        go.append((round(t, 2), f"offset-distance:{f:.2f}%;opacity:1"))
        trail.append((round(t, 2), f"stroke-dashoffset:{L - acc:.0f}"))
        p = ROUTE[i + 1][0]
        if p:
            arrive[p] = t
            t += hold
            go.append((round(t, 2), f"offset-distance:{f:.2f}%;opacity:1"))
            trail.append((round(t, 2), f"stroke-dashoffset:{L - acc:.0f}"))
    go += [(round(t + 3, 2), "offset-distance:100%;opacity:0"), (100, "offset-distance:100%;opacity:0")]
    trail += [(94, "stroke-dashoffset:0"), (100, f"stroke-dashoffset:{L:.0f}")]
    gk, tk = _kf("cmk-go2", go), _kf("cmk-trail2", trail)
    out = (f'<div style="position:relative;width:{w}px;height:{h}px">{svg}'
           f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="position:absolute;left:0;top:0;overflow:visible" aria-hidden="true">'
           f'<path d="{d}" fill="none" stroke="#ffffff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" opacity=".9" stroke-dasharray="{L:.0f}" style="animation:{tk} {DUR}s infinite"/>'
           f'<path d="{d}" fill="none" stroke="{BLUE}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" stroke-dasharray="{L:.0f}" style="animation:{tk} {DUR}s infinite"/></svg>'
           f'<span style="position:absolute;left:0;top:0;offset-path:path(\'{d}\');offset-rotate:0deg;offset-anchor:50% 85%;animation:{gk} {DUR}s infinite;'
           f'display:inline-flex;align-items:center;height:24px;padding:0 9px;border-radius:12px;background:{BLUE};color:#fff;font:600 12px {SANS};'
           f'box-shadow:0 0 0 2px #fff,0 8px 16px -6px rgba(37,99,235,.7)">71%</span>')
    for i, p in enumerate(("Teacher", "Administration", "Student", "Parent")):
        ta = arrive[p]
        a, b = STOPS[p]
        name = _kf(f"cmk-pop2{i}", [(0, "opacity:0;transform:translate(-50%,-100%) translateY(6px) scale(.9)"), (round(ta, 1), "opacity:0;transform:translate(-50%,-100%) translateY(6px) scale(.9)"),
                                     (round(ta + 2.5, 1), "opacity:1;transform:translate(-50%,-100%) translateY(0) scale(1)"), (94, "opacity:1;transform:translate(-50%,-100%) translateY(0) scale(1)"),
                                     (98, "opacity:0;transform:translate(-50%,-100%) translateY(0) scale(1)"), (100, "opacity:0")])
        x, y = anc[p]
        dx, dy = {"Teacher": (-30, -6), "Administration": (70, -10), "Student": (110, 10), "Parent": (40, -4)}[p]
        gx, gy = stop_xy[p]
        out += (f'<span style="position:absolute;left:{x + dx:.0f}px;top:{y - 10 + dy:.0f}px;opacity:0;animation:{name} {DUR}s infinite;display:flex;align-items:center;gap:7px;'
                f'padding:5px 10px 5px 5px;border-radius:12px;background:#fff;box-shadow:0 0 0 1px {LINE},0 10px 18px -10px rgba(11,12,20,.4);white-space:nowrap">'
                f'{portal_art.portal_icon(p, 24)}<span><span style="display:block;font:600 12px {SANS};color:{INK}">{a}</span>'
                f'<span style="display:block;font:400 11px {SANS};color:{MUTED}">{b}</span></span></span>')
        out += f'<span style="position:absolute;left:{gx - 4:.0f}px;top:{gy - 4:.0f}px;width:8px;height:8px;border-radius:4px;background:#fff;border:2px solid {BLUE};box-sizing:border-box"></span>'
    return out + '</div>'


def mark_journey(w=620, h=460):
    """the row picture: the campus on its plate, the entry card in the corner it starts from"""
    return (f'<div style="position:relative;width:{w}px;height:{h}px;border-radius:28px;{DOTS};box-shadow:inset 0 0 0 1px #eceef2;overflow:hidden">'
            f'{scene(w, h)}<div style="position:absolute;left:20px;top:{h - 236}px">{entry_card(250)}</div></div>')

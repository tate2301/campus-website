# -*- coding: utf-8 -*-
"""Corelith Campus design system, direction AB. Components are functions so the site build uses the same ones."""
from brandkit import *

T = {  # tokens
    "ink": INK, "ink-2": INK2, "muted": MUTED, "faint": FAINT, "line": LINE, "plate": PLATE, "ground": GROUND, "white": "#ffffff",
    "accent": BLUE, "accent-hover": "#1d4ed8", "accent-tint": "#e8effd", "accent-ring": "#bfd3fb",
    "campus": CAMPUS, "campus-tint": "#efeaff",
    "ok": OK, "ok-tint": OKS, "warn": WARN, "warn-tint": WARNS, "bad": BAD, "bad-tint": BADS,
}
SPACE = [4, 8, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96, 112]
RADII = [("input", 12), ("card", 16), ("photo, plate", 24), ("pill, button", 999)]
SHADOWS = [("none", "none"), ("card", "0 1px 2px rgba(11,12,20,.06), 0 16px 36px -18px rgba(11,12,20,.30)"),
           ("raised", "0 2px 4px rgba(11,12,20,.06), 0 28px 56px -24px rgba(11,12,20,.38)"), ("outline", f"0 0 0 1px {LINE}")]
SH_CARD = SHADOWS[1][1]


# ---- components ----------------------------------------------------------------------------------
def cbtn(label, icon="right-line", kind="primary", size="md", state="default"):
    h, fs, ics = {"sm": (36, 14, 14), "md": (44, 15, 16), "lg": (52, 16, 18)}[size]
    if kind == "link":
        c = T["accent"] if state == "hover" else INK
        return (f'<span style="display:inline-flex;align-items:center;gap:6px;font:500 {fs}px {SANS};color:{c};text-decoration:underline;text-underline-offset:4px;'
                f'{"opacity:.45;" if state == "disabled" else ""}{"outline:3px solid " + T["accent-ring"] + ";outline-offset:3px;border-radius:4px;" if state == "focus" else ""}">{label}{ic("right-line", ics - 2, c)}</span>')
    bg, fg, bd = {"primary": (T["accent"], "#fff", "none"), "secondary": ("#fff", INK, f"inset 0 0 0 1px {LINE}"), "dark": (INK, "#fff", "none"),
                  "tint": (T["accent-tint"], T["accent"], "none")}[kind]
    if state == "hover":
        bg = {"primary": T["accent-hover"], "secondary": PLATE, "dark": "#23252f", "tint": "#dbe6fc"}[kind]
    if state == "disabled":
        bg, fg, bd = ("#eef0f3", FAINT, "none")
    ring = f",0 0 0 3px #fff,0 0 0 6px {T['accent-ring']}" if state == "focus" else ""
    sh = (bd if bd != "none" else "0 0 0 0 transparent") + ring
    return (f'<span style="display:inline-flex;align-items:center;gap:8px;height:{h}px;padding:0 {round(h * 0.38)}px 0 {round(h * 0.46)}px;border-radius:{h // 2}px;'
            f'background:{bg};color:{fg};box-shadow:{sh};font:500 {fs}px/1 {SANS};white-space:nowrap">{label}{ic(icon, ics, fg) if icon else ""}</span>')


PORTAL_NAMES = ("Administration", "Teacher", "Parent", "Student")


def portal_tag(t):
    """a tag naming where something comes from; when it names a portal it carries that portal's icon"""
    import portal_art
    name = next((n for n in PORTAL_NAMES if t.startswith(n + " portal")), None)
    icon = portal_art.portal_icon(name, 20, tile=False) if name else ""
    pad = "0 10px 0 4px" if name else "0 10px"
    return (f'<span style="display:inline-flex;align-items:center;gap:4px;height:26px;padding:{pad};border-radius:13px;background:{T["campus-tint"]};'
            f'font:500 13px {SANS};color:{CAMPUS};white-space:nowrap">{icon}{t}</span>')


def module_chip(code, name, icon):
    return (f'<span style="display:inline-flex;align-items:center;gap:8px;height:36px;padding:0 14px 0 10px;border-radius:18px;background:#fff;box-shadow:0 0 0 1px {LINE};font:500 14px {SANS};color:{INK2};white-space:nowrap">'
            f'{ic(icon, 16, MUTED)}<span style="font:400 12px {MONO};color:{FAINT}">{code}</span>{name}</span>')


def filter_pill(t, on=False):
    return (f'<span style="display:inline-flex;align-items:center;gap:7px;height:40px;padding:0 16px;border-radius:20px;'
            f'{"background:" + INK + ";color:#fff" if on else "background:#fff;color:" + INK2 + ";box-shadow:0 0 0 1px " + LINE};font:500 14.5px {SANS};white-space:nowrap">{t}</span>')


def field(label, value="", ph_="", help_="", error="", w=360, kind="text", focus=False):
    bd = T["bad"] if error else (T["accent"] if focus else LINE)
    ring = f",0 0 0 4px {T['accent-ring']}" if focus else ""
    val = f'<span style="color:{INK}">{value}</span>' if value else f'<span style="color:{FAINT}">{ph_}</span>'
    tail = ic("down-line", 16, MUTED) if kind == "select" else ""
    hh = 104 if kind == "area" else 48
    box = (f'<div style="height:{hh}px;border-radius:12px;background:#fff;box-shadow:inset 0 0 0 {1.5 if (error or focus) else 1}px {bd}{ring};display:flex;align-items:{"flex-start" if kind == "area" else "center"};'
           f'justify-content:space-between;padding:{"14px" if kind == "area" else "0"} 16px;box-sizing:border-box;font:400 16px {SANS}">{val}{tail}</div>')
    note = (f'<div style="display:flex;gap:6px;align-items:center;font:400 13.5px {SANS};color:{T["bad"]};margin-top:8px">{ic("alert", 14, T["bad"])}{error}</div>' if error
            else (f'<div style="font:400 13.5px {SANS};color:{MUTED};margin-top:8px">{help_}</div>' if help_ else ""))
    return f'<div style="width:{w}px"><div style="font:500 14px {SANS};color:{INK};margin-bottom:8px">{label}</div>{box}{note}</div>'


def check(label, on=True, radio=False):
    r = 10 if radio else 6
    inner = (f'<span style="width:8px;height:8px;border-radius:4px;background:#fff"></span>' if radio else ic("check-line", 14, "#fff")) if on else ""
    return (f'<span style="display:inline-flex;align-items:center;gap:10px;font:400 15px {SANS};color:{INK}">'
            f'<span style="width:20px;height:20px;border-radius:{r}px;display:flex;align-items:center;justify-content:center;{"background:" + BLUE if on else "background:#fff;box-shadow:inset 0 0 0 1.5px #c3c8d1"}">{inner}</span>{label}</span>')


def segmented(opts, on=0):
    return (f'<div style="display:inline-flex;padding:4px;border-radius:24px;background:#eef0f3">'
            + "".join(f'<span style="height:36px;padding:0 16px;border-radius:18px;display:flex;align-items:center;font:500 14px {SANS};'
                      f'{"background:#fff;color:" + INK + ";box-shadow:0 1px 2px rgba(11,12,20,.12)" if i == on else "color:" + MUTED}">{o}</span>' for i, o in enumerate(opts)) + '</div>')


def sec_head(a, b, body="", centre=False, w=1280):
    """a section head is the headline alone (1 Oct 2026: "lose these descriptions for sections")"""
    if centre:
        return f'<div style="width:{w}px;text-align:center">{h2(a, b, 44, centre=True)}</div>'
    return f'<div style="width:{w}px">{h2(a, b, 44)}</div>'


def portal_thumb(n, w=272, h=168):
    import portal_art
    k = w / 560
    sc = portal_art.portal_scene(n, 560, round(h / k), 40, 280, round(h / k) * 0.6, labels=False)
    return (f'<div style="width:{w}px;height:{h}px;border-radius:12px;overflow:hidden;{DOTS};box-shadow:inset 0 0 0 1px #eceef2;flex:none">'
            f'{scaled(sc, w, h, k)}</div>')


def portal_tile(n, icn, where, d, w=304):
    import portal_art
    return (f'<div style="width:{w}px;box-sizing:border-box;background:#fff;border-radius:16px;box-shadow:0 0 0 1px {LINE};padding:16px 16px 24px;display:flex;flex-direction:column;gap:14px">'
            f'{portal_thumb(n, w - 32, 168)}'
            f'<div style="display:flex;gap:12px;align-items:center;padding:4px 10px 0">{portal_art.portal_icon(n, 40)}<div><div style="font:600 19px {SANS}">{n} portal</div><div style="font:400 14px {SANS};color:{MUTED};margin-top:2px">{where}</div></div></div>'
            f'<div style="font:400 15px/1.55 {SANS};color:{INK2};padding:0 10px">{d}</div><div style="padding:0 10px">{cbtn("See the " + n.lower() + " portal", kind="link", size="sm")}</div></div>')


def story_row(s, pic, flip=False, w=1280):
    text = (f'<div style="width:500px;display:flex;flex-direction:column;gap:18px">{"<div style=&quot;display:flex&quot;>" + portal_tag(s["tag"]) + "</div>"}'
            f'{h2(s["h"], "", 38)}{para(s["b"], 17, INK2, 500)}<div>{ticks(s["pts"])}</div></div>').replace("&quot;", '"')
    return f'<div style="width:{w}px;display:flex;justify-content:space-between;align-items:center;{"flex-direction:row-reverse;" if flip else ""}">{text}{pic}</div>'


def photo_story(n, pos, cards, w=640, h=480):
    """a photo with cards on its edge: cards is a list of (x, y, html)"""
    return (f'<div style="position:relative;width:{w}px;height:{h}px;flex:none"><div style="position:absolute;right:0;top:0">{ph(n, w - 110, h, pos, 24)}</div>'
            + "".join(at(x, y, c_, i + 2) for i, (x, y, c_) in enumerate(cards)) + '</div>')


def plate_story(cards, w=640, h=480):
    return (f'<div style="position:relative;width:{w}px;height:{h}px;border-radius:24px;{DOTS};box-shadow:inset 0 0 0 1px #eceef2;flex:none;overflow:hidden">'
            + "".join(at(x, y, c_, i + 2) for i, (x, y, c_) in enumerate(cards)) + '</div>')


def figure_tile(v, t, d):
    return (f'<div style="flex:1;padding:28px;border-radius:16px;background:#fff;box-shadow:0 0 0 1px {LINE}"><div style="font:600 44px/1 {SANS};letter-spacing:-0.03em;{NUM}">{v}</div>'
            f'<div style="font:500 16px {SANS};margin-top:12px">{t}</div><div style="font:400 14px {SANS};color:{MUTED};margin-top:4px">{d}</div></div>')


def commit_item(icn, t, d):
    return (f'<div style="display:flex;gap:14px"><span style="width:40px;height:40px;border-radius:20px;background:{T["accent-tint"]};display:flex;align-items:center;justify-content:center;flex:none">{ic(icn, 18, BLUE)}</span>'
            f'<div><div style="font:600 16px {SANS}">{t}</div><div style="font:400 14.5px/1.55 {SANS};color:{INK2};margin-top:4px">{d}</div></div></div>')


def nav_bar(open_=None, w=1440):
    items = "".join(f'<span style="display:inline-flex;align-items:center;gap:4px;height:36px;padding:0 12px;border-radius:18px;{"background:" + PLATE + ";" if t == open_ else ""}font:500 15px {SANS};color:{INK if t == open_ else INK2}">'
                    f'{t}{ic("down-line" if t != open_ else "up-line", 14, FAINT) if t in MENUS else ""}</span>' for t in CP.NAV)
    return (f'<div style="width:{w}px;height:76px;display:flex;align-items:center;gap:28px;padding:0 {120 if w >= 1280 else 40}px;box-sizing:border-box;border-bottom:1px solid {LINE};background:#fff">'
            f'{lockup(24)}<div style="display:flex;gap:6px;margin-left:12px">{items}</div><span style="flex:1"></span>'
            f'<span style="font:500 15px {SANS};color:{INK2}">Sign in</span>{cbtn("Book a demo", "calendar", size="sm")}</div>')


MENUS = ("Solutions", "Who we serve", "Platform")


def dept_thumb(kind, w=64, h=46):
    import dept_art
    return (f'<span style="width:{w}px;height:{h}px;border-radius:10px;background:#f4f5f7;box-shadow:inset 0 0 0 1px #e7e9ef;overflow:hidden;flex:none;display:block">'
            f'{dept_art.art(kind, w, h, U=w / 6.4)}</span>')


def mega_departments(w=1440):
    """Solutions: the nine departments, each with its drawing, and Moving to Campus"""
    items = "".join(f'<div style="display:flex;gap:12px;align-items:center;padding:10px;border-radius:14px;{"background:" + PLATE if i == 0 else ""}">'
                    f'{__import__("nav_icons").nav_icon(sl, 44)}<div style="min-width:0"><div style="font:600 15px {SANS}">{n}</div>'
                    f'<div style="font:400 13px/1.4 {SANS};color:{MUTED};margin-top:2px">{CP.MENU_LINE[k]}</div></div></div>'
                    for i, (n, sl, d, p_, k) in enumerate(CP.DEPARTMENTS))
    side = (f'<div style="width:300px;border-radius:20px;{DOTS};padding:20px;box-sizing:border-box;flex:none">'
            f'<div style="font:500 13px {SANS};color:{MUTED}">Moving to Campus</div>'
            f'<div style="font:600 20px/1.2 {SANS};letter-spacing:-0.01em;margin-top:8px">Move your school in four weeks.</div>'
            f'<div style="font:400 13.5px/1.5 {SANS};color:{INK2};margin-top:8px">From another system, Excel or paper registers. Data capture is included.</div>'
            f'<div style="margin-top:14px">{cbtn("How we move your records", kind="link", size="sm")}</div></div>')
    return (f'<div style="width:{w}px;height:440px;background:#fff;box-shadow:0 1px 0 {LINE},0 30px 50px -30px rgba(11,12,20,.25)">{nav_bar("Solutions", w)}'
            f'<div style="display:flex;gap:40px;padding:24px 120px 32px"><div style="flex:1"><div style="font:500 13px {SANS};color:{MUTED};margin:0 0 8px 10px">Departments</div>'
            f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:4px 8px">{items}</div></div>{side}</div></div>')


def mega_who(w=1440):
    """Who we serve: school types with their building, and the people, each with their portal's icon"""
    import portal_art
    types = "".join(f'<div style="display:flex;gap:12px;align-items:center;padding:8px 10px;border-radius:14px">{__import__("nav_icons").nav_icon(k, 44)}'
                    f'<div><div style="font:600 15px {SANS}">{n}</div><div style="font:400 13px/1.4 {SANS};color:{MUTED};margin-top:2px">{d}</div></div></div>'
                    for n, k, d in CP.SCHOOL_TYPES)
    roles = "".join(f'<div style="display:flex;gap:12px;align-items:center;padding:8px 10px">{portal_art.portal_icon(p_, 44)}'
                    f'<div><div style="font:600 15px {SANS}">{n}</div><div style="font:400 13px/1.4 {SANS};color:{MUTED};margin-top:2px">{d}</div></div></div>'
                    for n, p_, d, k_ in CP.ROLES)
    return (f'<div style="width:{w}px;height:490px;background:#fff;box-shadow:0 1px 0 {LINE},0 30px 50px -30px rgba(11,12,20,.25)">{nav_bar("Who we serve", w)}'
            f'<div style="display:flex;gap:48px;padding:24px 120px 32px">'
            f'<div style="flex:1"><div style="font:500 13px {SANS};color:{MUTED};margin:0 0 6px 10px">By type of school · K-12</div>{types}</div>'
            f'<div style="flex:1"><div style="font:500 13px {SANS};color:{MUTED};margin:0 0 6px 10px">By role</div>{roles}</div></div></div>')


def ISO_SC():
    svg, labels = ISO.scene()
    return f'<div style="position:relative;width:1280px;height:720px">{svg}</div>'


def mobile_nav(open_=False):
    bar = (f'<div style="height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 20px;border-bottom:1px solid {LINE}">{lockup(20, by=False)}'
           f'<span style="display:flex;gap:10px;align-items:center">{cbtn("Demo", "calendar", size="sm")}'
           f'<span style="width:40px;height:40px;border-radius:20px;box-shadow:inset 0 0 0 1px {LINE};display:flex;align-items:center;justify-content:center">{__import__("campus_mark").menu_icon(20, open_)}</span></span></div>')
    if not open_:
        body = (f'<div style="padding:28px 20px"><div style="font:600 34px/1.08 {SANS};letter-spacing:-0.03em">{CP.HERO["h1a"]}</div>'
                f'<div style="font:400 16px/1.55 {SANS};color:{INK2};margin-top:14px">{CP.HERO["body_phone"]}</div>'
                f'<div style="margin-top:22px">{ph("boys-reading-2.jpg", 350, 230, "58% 40%", 20)}</div></div>')
    else:
        rows = "".join(f'<div style="display:flex;align-items:center;justify-content:space-between;height:56px;border-bottom:1px solid {LINE};font:500 18px {SANS}">{t}{ic("down-line" if t in MENUS else "right-line", 16, MUTED)}</div>' for t in CP.NAV)
        body = (f'<div style="padding:12px 20px">{rows}<div style="display:flex;flex-direction:column;gap:12px;margin-top:28px">'
                f'<div style="display:flex">{cbtn("Book a demo", "calendar", size="lg")}</div><div style="display:flex">{cbtn("Sign in", "user-3", "secondary", "lg")}</div></div></div>')
    return f'<div style="width:390px;height:640px;background:#fff;border-radius:28px;box-shadow:0 0 0 1px {LINE},{SH_CARD};overflow:hidden">{bar}{body}</div>'


def pricing_card(p, primary=True, w=413):
    return (f'<div style="width:{w}px;box-sizing:border-box;background:#fff;border-radius:24px;box-shadow:0 0 0 {2 if primary else 1}px {BLUE if primary else LINE};padding:32px;display:flex;flex-direction:column;gap:18px">'
            f'<div style="display:flex;justify-content:space-between;align-items:center"><span style="font:600 18px {SANS}">{p["name"]}</span>{status(SB, "Current offer", "info") if primary else ""}</div>'
            f'<div><span style="font:600 56px/1 {SANS};letter-spacing:-0.03em">{p["price"]}</span><div style="font:400 15px {SANS};color:{MUTED};margin-top:10px">{p["per"]}</div></div>'
            f'<div style="display:flex;gap:8px;padding:12px 0 0;border-top:1px solid {LINE}">'
            + "".join(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:6px">{__import__("portal_art").portal_icon(n, 40)}'
                      f'<span style="font:500 11.5px {SANS};color:{MUTED}">{n}</span></div>' for n in PORTAL_NAMES)
            + f'</div><div>{ticks(p["items"], INK2, "check-circle", BLUE, 15)}</div>'
            f'<div style="display:flex">{cbtn("Book a demo", "calendar", "primary" if primary else "secondary")}</div></div>')


def calculator(pupils="1,140", lms=False, w=520):
    rate = "8.99" if lms else "1.00"
    total = "US$10,248.60" if lms else "US$1,140.00"
    return (f'<div style="width:{w}px;box-sizing:border-box;background:#fff;border-radius:24px;box-shadow:0 0 0 1px {LINE},{SH_CARD};padding:32px">'
            f'<div style="font:600 18px {SANS}">Work out your school</div>'
            f'<div style="display:flex;gap:16px;margin-top:22px;align-items:flex-end">{field("Active pupils", pupils, w=200)}'
            f'<div><div style="font:500 14px {SANS};margin-bottom:8px">Package</div>{segmented(["Campus", "With LMS"], 1 if lms else 0)}</div></div>'
            f'<div style="margin-top:26px;padding:22px;border-radius:16px;background:{PLATE}">'
            f'<div style="display:flex;justify-content:space-between;font:400 15px {SANS};color:{INK2}"><span>{pupils} active pupils × US${rate}</span><span>a month</span></div>'
            f'<div style="font:600 44px/1 {SANS};letter-spacing:-0.03em;margin-top:12px;{NUM}">{total}</div>'
            f'<div style="display:flex;gap:8px;margin-top:14px">{status(SB, "First month free", "ok")}{status(SB, "Holidays US$0", "mute")}</div></div></div>')


FAQ = [("What counts as an active pupil?", "A learner on the roll in the month we bill. Pupils who leave stop counting the next month."),
       ("Do we pay in the holidays?", "No. Billing stops when the term closes and starts again when it opens."),
       ("Can we keep our data if we leave?", "Yes. The school can export everything, at any time, in full."),
       ("Does it work without internet?", "Yes. The whole system works without internet. Changes save on the device and sync when the connection returns.")]


def faq(w=760, open_=0):
    out = ""
    for i, (q, a) in enumerate(FAQ):
        o = i == open_
        out += (f'<div style="padding:20px 0;border-top:1px solid {LINE}"><div style="display:flex;justify-content:space-between;align-items:center;font:600 17px {SANS}">{q}{ic("up-line" if o else "down-line", 18, MUTED)}</div>'
                + (f'<div style="font:400 15.5px/1.6 {SANS};color:{INK2};margin-top:10px;max-width:640px">{a}</div>' if o else "") + '</div>')
    return f'<div style="width:{w}px">{out}<div style="border-top:1px solid {LINE}"></div></div>'


def timeline(w=1280):
    tl = "".join(f'<div style="flex:1;padding-top:14px;border-top:3px solid {BLUE if i < 2 else LINE}"><div style="font:500 13px {SANS};color:{MUTED}">{a}</div>'
                 f'<div style="font:600 16px {SANS};margin-top:6px">{b}</div><div style="font:400 14px {SANS};color:{INK2};margin-top:2px">{c}</div></div>' for i, (a, b, c) in enumerate(CP.PRICING["timeline"]))
    return f'<div style="width:{w}px;display:flex;gap:18px">{tl}</div>'


# ---- boards --------------------------------------------------------------------------------------
def label(t):
    return f'<div style="font:500 13px {SANS};color:{MUTED};margin-bottom:14px">{t}</div>'


def block(t, inner, mt=56):
    return f'<div style="margin-top:{mt}px"><div style="font:600 18px {SANS};padding-bottom:14px;border-bottom:1px solid {LINE};margin-bottom:24px">{t}</div>{inner}</div>'


def ds_tokens():
    groups = [("Text and surface", ["ink", "ink-2", "muted", "faint", "line", "plate", "ground", "white"]),
              ("Accent and product", ["accent", "accent-hover", "accent-tint", "accent-ring", "campus", "campus-tint"]),
              ("Status", ["ok", "ok-tint", "warn", "warn-tint", "bad", "bad-tint"])]
    col = ""
    for g, keys in groups:
        rows = "".join(f'<div style="display:flex;align-items:center;gap:12px;padding:9px 0;border-top:1px solid {LINE}"><span style="width:28px;height:28px;border-radius:8px;background:{T[k]};box-shadow:inset 0 0 0 1px rgba(11,12,20,.08)"></span>'
                       f'<span style="font:400 13px {MONO};color:{INK}">--cc-{k}</span><span style="flex:1"></span><span style="font:400 12px {MONO};color:{MUTED}">{T[k].upper()}</span></div>' for k in keys)
        col += f'<div style="flex:1">{label(g)}{rows}</div>'
    sp = "".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px"><div style="width:{s_}px;height:{s_}px;background:{T["accent-tint"]};box-shadow:inset 0 0 0 1px {T["accent-ring"]}"></div>'
                 f'<span style="font:400 12px {MONO};color:{MUTED}">{s_}</span></div>' for s_ in SPACE)
    rd = "".join(f'<div style="display:flex;flex-direction:column;gap:10px;align-items:flex-start"><div style="width:120px;height:80px;border-radius:{min(r_, 40)}px;background:{PLATE};box-shadow:inset 0 0 0 1px {LINE}"></div>'
                 f'<span style="font:500 14px {SANS}">{n}</span><span style="font:400 12px {MONO};color:{MUTED}">--cc-radius-{n.split(",")[0]}: {r_}px</span></div>' for n, r_ in RADII)
    sh = "".join(f'<div style="display:flex;flex-direction:column;gap:10px"><div style="width:180px;height:100px;border-radius:16px;background:#fff;box-shadow:{v};{"border:1.5px dashed #c3c8d1;box-sizing:border-box" if v == "none" else ""}"></div>'
                 f'<span style="font:500 14px {SANS}">{n}</span></div>' for n, v in SHADOWS)
    ty = [("display", "62/1.06 · 600 · -0.035em"), ("h1", "48/1.08 · 600 · -0.03em"), ("h2", "38/1.12 · 600 · -0.025em"), ("h3", "24/1.25 · 600"),
          ("lead", "19/1.6 · 400"), ("body", "17/1.6 · 400"), ("small", "15/1.5 · 400"), ("label", "13/1.3 · 500"), ("code", "12 · Plex Mono 400")]
    tyr = "".join(f'<div style="display:flex;justify-content:space-between;padding:9px 0;border-top:1px solid {LINE}"><span style="font:400 13px {MONO}">--cc-type-{n}</span><span style="font:400 12px {MONO};color:{MUTED}">{v}</span></div>' for n, v in ty)
    grid = "".join(f'<div style="flex:1;height:120px;background:#fde7ec;opacity:.8"></div>' for _ in range(12))
    grids = [("Desktop 1440", "12 columns · 120 margin · 24 gutter · content 1200"), ("Tablet 1024", "8 columns · 48 margin · 20 gutter"), ("Phone 390", "4 columns · 20 margin · 16 gutter")]
    gl = "".join(f'<div style="flex:1"><div style="font:600 15px {SANS}">{a}</div><div style="font:400 14px {SANS};color:{MUTED};margin-top:4px">{b}</div></div>' for a, b in grids)
    body = (f'<div style="display:flex;gap:48px">{col}</div>'
            + block("Type", f'<div style="width:760px">{tyr}</div>')
            + block("Spacing", f'<div style="display:flex;gap:26px;align-items:flex-end">{sp}</div>')
            + block("Radius", f'<div style="display:flex;gap:56px">{rd}</div>')
            + block("Shadow", f'<div style="display:flex;gap:40px">{sh}</div>')
            + block("Layout", f'<div style="position:relative;height:120px;display:flex;gap:24px;padding:0 60px;border-radius:12px;background:{PLATE}">{grid}</div><div style="display:flex;gap:40px;margin-top:18px">{gl}</div>'))
    return frame("Design system · 01", "Tokens", "Colour, type, space, radius, shadow.",
                 "Every value on the site comes from this list. Names start with --cc- so they never clash with the Corelith company site.", body)


def ds_actions():
    kinds = [("Primary", "primary"), ("Secondary", "secondary"), ("Dark", "dark"), ("Tint", "tint")]
    states = ["default", "hover", "focus", "disabled"]
    head = "".join(f'<span style="font:500 13px {SANS};color:{MUTED}">{s_}</span>' for s_ in ["", "Default", "Hover", "Focus", "Disabled"])
    rows = "".join(f'<span style="font:500 15px {SANS}">{n}</span>' + "".join(f'<div>{cbtn("Book a demo", "calendar", k, "md", s_)}</div>' for s_ in states) for n, k in kinds)
    rows += '<span style="font:500 15px ' + SANS + '">Link</span>' + "".join(f'<div>{cbtn("See pricing", kind="link", state=s_)}</div>' for s_ in states)
    grid = f'<div style="display:grid;grid-template-columns:140px repeat(4,1fr);gap:22px 20px;align-items:center">{head}{rows}</div>'
    sizes = "".join(f'<div style="display:flex;flex-direction:column;gap:10px;align-items:flex-start">{cbtn("Book a demo", "calendar", "primary", s_)}<span style="font:400 12px {MONO};color:{MUTED}">{s_} · {h_}px</span></div>'
                    for s_, h_ in (("sm", 36), ("md", 44), ("lg", 52)))
    tags = (f'<div style="display:flex;flex-wrap:wrap;gap:12px;align-items:center">{status(SB, "Present", "ok")}{status(SB, "Late", "warn")}{status(SB, "Absent", "bad")}'
            f'{status(SB, "Current offer", "info")}{status(SB, "Draft", "mute")}{portal_tag("Teacher portal · offline")}{portal_tag("Parent portal")}</div>')
    chips = f'<div style="display:flex;flex-wrap:wrap;gap:10px">' + "".join(module_chip(c, n, i) for c, n, i in MODULES[:5]) + '</div>'
    filt = f'<div style="display:flex;gap:10px">' + "".join(filter_pill(t, i == 0) for i, t in enumerate(["All", "Administration", "Teacher", "Parent", "Student"])) + '</div>'
    rules = ["Every button carries an icon, after the label.", "Labels say what happens: Book a demo, Download the price sheet (PDF). Never Submit or Learn more.",
             "One primary button per view. Links are underlined and end in a chevron."]
    body = (grid + block("Sizes", f'<div style="display:flex;gap:40px">{sizes}</div>')
            + block("Status pills and portal tags", tags) + block("Module chips", chips) + block("Filter pills", filt)
            + block("Rules", "".join(f'<div style="font:400 15.5px/1.55 {SANS};color:{INK2};padding:6px 0">{r_}</div>' for r_ in rules)))
    return frame("Design system · 02", "Actions and tags", "Buttons, links, pills, chips.",
                 "Buttons are pills with an icon after the label. Tags are round and carry a dot when they report a status.", body)


def ds_forms():
    r1 = (f'<div style="display:flex;gap:28px;align-items:flex-start">{field("School name", "Mukuvisi High School")}'
          f'{field("Your role", "Head", kind="select")}{field("Phone", "", "+263 77 000 0000", help_="We call to arrange a visit. No sales lists.", focus=True)}</div>')
    r2 = (f'<div style="display:flex;gap:28px;align-items:flex-start;margin-top:28px">{field("Email", "head@mukuvisi", error="Enter a full email address, like head@mukuvisi.ac.zw")}'
          f'{field("Active pupils", "1,140", help_="Roughly is fine.")}{field("Anything we should know", "", "Boarding, two campuses, a system you use now", kind="area")}</div>')
    ctl = (f'<div style="display:flex;gap:56px;align-items:center">{check("Boarding school")}{check("Day school", False)}'
           f'{check("Visit the school", True, True)}{check("Video call", False, True)}{segmented(["Term time", "All year"])}</div>')
    demo = (f'<div style="width:620px;box-sizing:border-box;padding:36px;border-radius:24px;background:#fff;box-shadow:0 0 0 1px {LINE},{SH_CARD}">'
            f'<div style="font:600 24px {SANS};letter-spacing:-0.015em">Book a demo</div><div style="font:400 15px {SANS};color:{MUTED};margin-top:6px">We call you to arrange a visit.</div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:26px">{field("Your name", "Chipo Mutasa", w=264)}{field("Your role", "Head", kind="select", w=264)}'
            f'{field("School", "Mukuvisi High School", w=264)}{field("Phone", "+263 77 000 0000", w=264)}</div>'
            f'<div style="display:flex;justify-content:space-between;align-items:center;margin-top:28px">{check("Visit the school", True, True)}{cbtn("Book a demo", "calendar")}</div></div>')
    import cta_art
    done = (f'<div style="width:560px;box-sizing:border-box;padding:20px 36px 36px;border-radius:24px;background:#fff;box-shadow:0 0 0 1px {LINE}">'
            f'<div style="margin:0 -16px 8px;border-radius:16px;overflow:hidden;{DOTS}">{scaled(cta_art.cta_scene("visit", 560, 300, 40, 280, 175, labels=False), 520, 279, 520 / 560)}</div>'
            f'<span style="width:44px;height:44px;border-radius:22px;background:{OKS};display:flex;align-items:center;justify-content:center">{ic("check-line", 22, OK)}</span>'
            f'<div style="font:600 22px {SANS};margin-top:18px">Request sent</div><div style="font:400 15.5px/1.6 {SANS};color:{INK2};margin-top:8px">We will call +263 77 000 0000 to arrange a visit to Mukuvisi High School.</div>'
            f'<div style="margin-top:20px">{cbtn("See pricing", kind="link")}</div></div>')
    body = (r1 + r2 + block("Choices", ctl) + block("Demo form and its sent state", f'<div style="display:flex;gap:40px;align-items:flex-start">{demo}{done}</div>'))
    return frame("Design system · 03", "Forms", "Labels above, help before the mistake.",
                 "Fields are 48px with the label always visible above. Help text says why we ask. Errors say how to fix it, in words and in red.", body)


def ds_nav():
    import pages
    ft = pages.site_footer()
    body = (block("Desktop nav", nav_bar(w=1280), 0)
            + block("Solutions menu", scaled(mega_departments(), 1280, round(1280 / 1440 * 440), 1280 / 1440))
            + block("Who we serve menu", scaled(mega_who(), 1280, round(1280 / 1440 * 490), 1280 / 1440))
            + block("Phone", f'<div style="display:flex;gap:40px">{mobile_nav(False)}{mobile_nav(True)}</div>')
            + block("Footer", scaled(f'<div style="width:1440px">{ft}</div>', 1280, round(1280 / 1440 * 820), 1280 / 1440)))
    return frame("Design system · 04", "Navigation", "Nav, menus, phone, footer.",
                 "Four items and one button. Solutions opens on the nine departments, Who we serve on the types of school and the people who use Campus.", body)


def ds_sections():
    tiles = "".join(portal_tile(*p_) for p_ in PORTALS)
    mods = "".join(module_chip(c, n, i) for c, n, i in MODULES)
    s = CP.STORIES
    import pages
    row1 = pages.row(*CP.ROWS[1], pages.pic_offline(560, 420))
    dtiles = "".join(pages.dept_tile(*d) for d in CP.DEPARTMENTS[:3])
    row2 = story_row(s[2], plate_story([(36, 40, fee_card(SB, 330)), (300, 220, receipts_card(SB, 300))]), flip=True)
    figs = "".join(figure_tile(*f_) for f_ in CP.FIGURES)
    comm = "".join(commit_item(*c_) for c_ in COMMIT)
    body = (block("Section head", sec_head(*CP.PORTALS_H, CP.PORTALS_B), 0)
            + block("Section head, centred", sec_head("What the school can count on.", "", "Six things written down, so the SDC can hold us to them.", True))
            + block("Portal tiles", f'<div style="display:flex;justify-content:space-between">{tiles}</div>')
            + block("Department tiles", f'<div style="display:flex;justify-content:space-between">{dtiles}</div>')
            + block("Row: eyebrow, claim, paragraph, photograph", row1)
            + block("Story row, plate", row2)
            + block("Figures", f'<div style="display:flex;gap:16px">{figs}</div>')
            + block("Commitments", f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:36px 48px">{comm}</div>')
            + block("The drawing, full width", tile(scaled(iso_scene(), 1280, 720, 1), 1280, 720, GROUND)))
    return frame("Design system · 05", "Sections", "Heads, tiles, story rows, figures.",
                 "Pages are stacks of these. Every section opens with type; a row takes a photograph, the drawing or a plate of cards and alternates sides down the page.", body.replace("Six things written down, so the SDC can hold us to them.", "Six commitments the SDC can hold us to."))


def ds_cards():
    items = [("Register", register_card(SB, 300)), ("Sync", sync_card(SB, 280)), ("Marks", marks_card(SB, 300)), ("Report", report_card(SB, 300)),
             ("Fees", fee_card(SB, 300)), ("Receipts", receipts_card(SB, 280)), ("The Head's view", head_card(SB, 300)), ("Parent's week", week_card(SB, 300)),
             ("Message", message_card(SB, 280)), ("Same mark, four places", same_card(SB, 300))]
    cells = "".join(f'<div>{label(n)}{c_}</div>' for n, c_ in items)
    anat = (f'<div style="display:flex;gap:40px;align-items:flex-start"><div style="position:relative">{fee_card(SB, 330)}'
            f'<span style="position:absolute;left:342px;top:18px;white-space:nowrap;font:400 12px {MONO};color:{MUTED}">header: tile, title, meta</span>'
            f'<span style="position:absolute;left:342px;top:70px;white-space:nowrap;font:400 12px {MONO};color:{MUTED}">rows: label, figure</span>'
            f'<span style="position:absolute;left:342px;top:196px;white-space:nowrap;font:400 12px {MONO};color:{MUTED}">pills: status, code</span></div>'
            f'<div style="margin-left:220px;width:420px">'
            + "".join(f'<div style="padding:12px 0;border-top:1px solid {LINE};font:400 15px/1.55 {SANS};color:{INK2}">{t}</div>' for t in (
                "Radius 16, padding 16, the card shadow.", "Figures come from world.md: US$420.00 is Tanaka's balance on every card that shows it.",
                "Money carries the currency and two decimals. Times are 24-hour.", "The tile colour says what the card is about: violet for Campus, green for money in, blue for the Head's view."))
            + '</div></div>')
    body = (f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:36px 24px;align-items:start">{cells}</div>' + block("Anatomy", anat))
    return frame("Design system · 06", "Product cards", "Ten cards, one school's figures.",
                 "These cards sit on photographs, on plates and in the Head's view. Each shows real figures from the one school.", body)


def ds_pricing():
    P_ = CP.PRICING
    ex = P_["example"]
    example = (f'<div style="width:414px;align-self:flex-start;box-sizing:border-box;background:{PLATE};border-radius:24px;padding:32px">'
               f'<div style="font:500 14px {SANS};color:{MUTED}">Worked example</div><div style="font:600 17px {SANS};margin-top:10px">{ex["t"]}</div>'
               f'<div style="font:600 44px/1 {SANS};letter-spacing:-0.03em;margin-top:14px">{ex["v"]}</div><div style="font:400 15px/1.5 {SANS};color:{INK2};margin-top:8px">{ex["s"]}</div>'
               f'<div style="margin-top:18px;padding-top:16px;border-top:1px solid {LINE};display:flex;justify-content:space-between;font:400 14px {SANS};color:{MUTED}"><span>Holidays</span><span style="color:{INK};font-weight:500">US$0</span></div><div style="margin-top:16px">{cbtn("Work out your school", kind="link", size="sm")}</div></div>')
    comp = [("Registers, marks and reports", True, True), ("Fees in US$ and ZiG, receipts", True, True), ("Boarding, payroll, HR, stock", True, True),
            ("Parent and student portals", True, True), ("Lessons, homework, e-library", False, True), ("AI help from the school's material", False, True)]
    ct = (f'<div style="display:grid;grid-template-columns:1fr 200px 200px;padding:12px 0;border-bottom:1px solid {INK};font:600 15px {SANS}"><span></span><span>Campus</span><span>With LMS</span></div>'
          + "".join(f'<div style="display:grid;grid-template-columns:1fr 200px 200px;padding:14px 0;border-bottom:1px solid {LINE};font:400 15px {SANS};color:{INK2}"><span>{n}</span>'
                    f'<span>{ic("check-line", 18, BLUE) if a else "<span style=&quot;color:#9a9ea9&quot;>—</span>"}</span><span>{ic("check-line", 18, BLUE) if b else "—"}</span></div>' for n, a, b in comp))
    body = (f'<div style="display:flex;gap:20px;align-items:stretch">{pricing_card(P_["main"])}{pricing_card(P_["lms"], False)}{example}</div>'
            + block("Calculator", f'<div style="display:flex;gap:40px">{calculator()}{calculator(lms=True)}</div>')
            + block("Comparison", f'<div style="width:900px">{ct}</div>'.replace("&quot;", '"'))
            + block("From signing to running", timeline())
            + block("Questions", faq()))
    return frame("Design system · 07", "Pricing", "Per active pupil, per month.",
                 "The price, a worked example at a real school size, and a calculator the bursar can check. No plan names to decode.", body)


def ds_media():
    import pages, dept_art
    spec = (f'<div style="position:relative;width:620px;margin-top:8px">{pages.pic_record()}'
            f'<span style="position:absolute;left:470px;top:430px;font:400 12px {MONO};color:{MUTED}">radius 28 · dotted plate</span></div>')
    specr = "".join(f'<div style="padding:12px 0;border-top:1px solid {LINE};font:400 15px/1.55 {SANS};color:{INK2}">{t}</div>' for t in (
        "Cards sit on the dotted plate, never on the drawing or loose on white.", "One to four cards, from one school: Mukuvisi High, Tanaka Moyo, Form 3B.",
        "The plate matches the height of the text beside it.", "On phones the plate crops to the first card."))
    depts = "".join(f'<div style="width:240px">{tile(dept_art.art(k, 240, 160, U=34), 240, 160, PLATE)}<div style="font:500 13.5px {SANS};margin-top:8px">{n}</div></div>'
                    for n, sl, d, p_, k in CP.DEPARTMENTS[:5])
    frame_d = (f'<div style="display:flex;gap:40px;align-items:flex-start">{tile(scaled(iso_scene(), 640, 360, 0.5), 640, 360, GROUND)}'
               f'<div style="flex:1">' + "".join(f'<div style="padding:12px 0;border-top:1px solid {LINE};font:400 15px/1.55 {SANS};color:{INK2}">{t}</div>' for t in (
                   "The drawing sits on the dotted ground, radius 24 to 32; in a hero it runs off the right edge of the page.", "Labels stay at 12.5px whatever the drawing's scale; on phones the drawing crops to one building and its label.",
                   "Each department and school type has its own small place on a plate (DS11).", "Exported at 4K for the site, light only.")) + '</div></div>')
    ph_ = (f'<div style="display:flex;gap:20px;align-items:center">{dashed(240, 80, "School logo", 16)}{dashed(240, 80, "School logo", 16)}'
           f'{dashed(560, 160, "A quote from a Head, with their written permission", 24)}</div>')
    pspec = (f'<div style="position:relative;width:640px;height:480px;margin-top:44px">{photo_story("classroom-zambia.jpg", "center 40%", [(0, 70, register_card(SB, 300))])}'
             f'<div style="position:absolute;left:110px;top:-22px;width:190px;border-top:1px dashed {BAD}"></div>'
             f'<span style="position:absolute;left:150px;top:-40px;font:400 12px {MONO};color:{BAD}">overlap 40–190px</span>'
             f'<span style="position:absolute;left:470px;top:490px;font:400 12px {MONO};color:{MUTED}">radius 24</span></div>')
    pspecr = "".join(f'<div style="padding:12px 0;border-top:1px solid {LINE};font:400 15px/1.55 {SANS};color:{INK2}">{t}</div>' for t in (
        "Photographs show people: pupils, teachers, a parent at home. Campus is a platform for people.", "The photo is right-aligned; cards start at the column's left edge.",
        "Cards overlap the photo by 40 to 190px and stay clear of faces.", "On phones the cards stack under the photo, overlapping its bottom edge by 40px."))
    body = (block("Photograph with cards", f'<div style="display:flex;gap:60px;align-items:flex-start">{pspec}<div style="flex:1">{pspecr}</div></div>', 16)
            + block("Cards on a plate", f'<div style="display:flex;gap:60px;align-items:flex-start">{spec}<div style="flex:1">{specr}</div></div>')
            + block("The drawing", frame_d) + block("Department drawings", f'<div style="display:flex;justify-content:space-between">{depts}</div>')
            + block("Placeholders", ph_ + f'<div style="font:400 15px {SANS};color:{MUTED};margin-top:14px">Logo and quote slots stay dashed until a school agrees in writing.</div>'))
    return frame("Design system · 08", "Media", "Photographs, cards, the drawing.",
                 "How pictures sit beside the type: people in photographs, the school in the drawing, the product in cards.", body)


DS = [("DS01-tokens", "Tokens", ds_tokens), ("DS02-actions", "Actions and tags", ds_actions), ("DS03-forms", "Forms", ds_forms),
      ("DS04-navigation", "Navigation", ds_nav), ("DS05-sections", "Sections", ds_sections), ("DS06-cards", "Product cards", ds_cards),
      ("DS07-pricing", "Pricing", ds_pricing), ("DS08-media", "Media", ds_media)]


# ---- 09 portals: one place and one icon per portal -------------------------------------------------
PORTAL_DIR = [("Administration", "The admin block", "The bursary window with a queue, the Head's office, the stores and the flag.", "The bursar and parents paying.", "Fees, Payroll, HR, Stock"),
              ("Teacher", "Form 3B, cut away", "Desks in rows, the chalkboard, the timetable on the wall.", "Ms Sibanda with her tablet, pupils at their desks.", "Register, Marks, Schemes of work"),
              ("Parent", "A guardian's home", "The house behind its durawall, the blue door, the veranda, the path to the gate.", "Rudo Moyo with her phone, Rufaro beside her.", "Attendance, Fees, Reports"),
              ("Student", "The library and Tsavo House", "A bench of readers, a pile of books, jacaranda trees.", "Pupils reading and walking to the hostel.", "Timetable, Homework, E-library, Hostel")]


def ds_portals():
    import portal_art
    cells = ""
    for n, place, things, people, mods in PORTAL_DIR:
        rows = "".join(f'<div style="display:grid;grid-template-columns:110px 1fr;gap:12px;padding:9px 0;border-top:1px solid {LINE};font:400 14.5px/1.5 {SANS};color:{INK2}">'
                       f'<span style="font:500 13px {SANS};color:{MUTED}">{a}</span><span>{b}</span></div>' for a, b in (("Drawn", things), ("People", people), ("Chips", mods)))
        cells += (f'<div style="width:620px"><div style="border-radius:24px;{DOTS};box-shadow:inset 0 0 0 1px #eceef2;overflow:hidden">{portal_art.portal_scene(n, 620, 430, 46, 310, 246)}</div>'
                  f'<div style="display:flex;align-items:center;gap:12px;margin-top:18px">{portal_art.portal_icon(n, 48)}<div><div style="font:600 19px {SANS}">{n} portal</div>'
                  f'<div style="font:400 14px {SANS};color:{MUTED};margin-top:2px">{place}</div></div></div><div style="margin-top:14px">{rows}</div></div>')
    sheet = ""
    for n in PORTAL_NAMES:
        sheet += (f'<div style="display:grid;grid-template-columns:150px 64px 40px 24px 1fr 1fr;gap:24px;align-items:center;padding:16px 0;border-top:1px solid {LINE}">'
                  f'<span style="font:600 15px {SANS}">{n}</span>{portal_art.portal_icon(n, 64)}{portal_art.portal_icon(n, 40)}{portal_art.portal_icon(n, 24)}'
                  f'<div>{portal_tag(n + " portal")}</div>'
                  f'<div style="position:relative;height:34px"><span style="display:inline-flex;align-items:center;gap:6px;height:30px;padding:0 11px 0 4px;border:1px solid #e7e9ef;border-radius:999px;background:#fff;'
                  f'box-shadow:0 6px 14px -8px rgba(15,20,35,.35);font:500 12.5px {SANS};white-space:nowrap">{portal_art.portal_icon(n, 22)}{n} portal</span></div></div>')
    head = (f'<div style="display:grid;grid-template-columns:150px 64px 40px 24px 1fr 1fr;gap:24px;padding:0 0 10px;font:500 13px {SANS};color:{MUTED}">'
            f'<span>Portal</span><span>64</span><span>40</span><span>24</span><span>Tag, wherever it is named</span><span>Label on a drawing</span></div>')
    rules = [("One place per portal", "A portal's page uses only its own place: the admin block for Administration, the classroom for Teacher, the home for Parent, the library and hostel for Student."),
             ("The place follows the portal", "When another page shows a feature from a portal, its picture comes from that portal's place, and its tag and label carry that portal's icon."),
             ("Same drawing, same rules", "The campus projection, greys, one blue and the same parts. Only the whole-campus drawing shows all four places together."),
             ("Icons replace generic ones", "Wherever a portal is named, in the nav, the menu, pricing, tags and labels on drawings, its icon is used instead of a MingCute glyph.")]
    rl = "".join(f'<div style="padding:16px 0;border-top:1px solid {LINE}"><div style="font:600 16px {SANS}">{t}</div><div style="font:400 14.5px/1.55 {SANS};color:{INK2};margin-top:4px">{d}</div></div>' for t, d in rules)
    body = (f'<div style="display:grid;grid-template-columns:620px 620px;justify-content:space-between;row-gap:56px">{cells}</div>'
            + block("Icons", head + sheet)
            + block("Rules", f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 56px">{rl}</div>'))
    return frame("Design system · 09", "Portals", "One place and one icon for each.",
                 "Each portal has its own place in the school and its own icon, drawn like the campus. On a portal's page every picture uses its place; wherever the portal is named, its icon goes with it.", body)


DS.append(("DS09-portals", "Portals", ds_portals))



# ---- 10 calls to action ---------------------------------------------------------------------------
CTAS = {"visit": ("See Campus at your school.", CP.CTA["b"], [("Book a demo", "calendar", "primary"), ("Download the price sheet (PDF)", "download-2", "secondary")]),
        "price": ("Work out your school's monthly cost.", "Enter your number of active pupils to see the figure, or download the price sheet to take to your SDC.",
                  [("Work out your school", "wallet-3", "primary"), ("Download the price sheet (PDF)", "download-2", "secondary")]),
        "training": ("Running in four weeks.", "Two weeks to set up and two weeks of training at your school. Then we support you through the rest of the term.",
                     [("Book a demo", "calendar", "primary")])}


def cta_block(kind, w=1280):
    import cta_art
    h_, b_, btns = CTAS[kind]
    bt = "".join(cbtn(t, i, k, "lg") for t, i, k in btns)
    return (f'<div style="width:{w}px;box-sizing:border-box;display:flex;align-items:center;gap:48px;border-radius:32px;background:{PLATE};padding:24px 24px 24px 64px">'
            f'<div style="flex:1;display:flex;flex-direction:column;gap:20px">{h2(h_, "", 44)}{para(b_, 18, INK2, 520)}<div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:6px">{bt}</div></div>'
            f'<div style="width:600px;height:430px;border-radius:24px;overflow:hidden;{DOTS};box-shadow:inset 0 0 0 1px #e3e6eb;flex:none">{cta_art.cta_scene(kind, 600, 430, 42, 300, 255)}</div></div>')


def cta_phone(kind="visit"):
    import cta_art
    h_, b_, btns = CTAS[kind]
    return (f'<div style="width:390px;background:#fff;border-radius:28px;box-shadow:0 0 0 1px {LINE};overflow:hidden;padding:20px;box-sizing:border-box">'
            f'<div style="border-radius:20px;background:{PLATE};padding:12px 12px 28px">'
            f'<div style="border-radius:16px;overflow:hidden;{DOTS}">{scaled(cta_art.cta_scene(kind, 560, 420, 40, 280, 250), 326, 245, 326 / 560)}</div>'
            f'<div style="padding:20px 10px 0;display:flex;flex-direction:column;gap:14px"><div style="font:600 30px/1.1 {SANS};letter-spacing:-0.03em">{h_}</div>'
            f'<div style="font:400 16px/1.55 {SANS};color:{INK2}">{b_}</div><div style="display:flex">{cbtn(btns[0][0], btns[0][1], "primary", "lg")}</div></div></div></div>')


def ds_ctas():
    rules = [("Show what the button does", "The drawing shows what happens next: we arrive at the school, the bursar has the price sheet, the staffroom is being trained."),
             ("The drawing, never a photograph", "Calls to action use the campus drawing so no stock person stands in for Corelith."),
             ("One primary button", "The first button is the action the picture shows; a second, if any, is secondary."),
             ("Where each one goes", "Visit closes Home, Features, Solutions and Platform. Price closes Pricing. Training closes the implementation section and the demo page.")]
    rl = "".join(f'<div style="padding:16px 0;border-top:1px solid {LINE}"><div style="font:600 16px {SANS}">{t}</div><div style="font:400 14.5px/1.55 {SANS};color:{INK2};margin-top:4px">{d}</div></div>' for t, d in rules)
    body = (block("Visit", cta_block("visit"), 0) + block("Price", cta_block("price")) + block("Training", cta_block("training"))
            + block("On a phone", f'<div style="display:flex;gap:40px;align-items:flex-start">{cta_phone("visit")}{cta_phone("price")}{cta_phone("training")}</div>')
            + block("Rules", f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 56px">{rl}</div>'))
    return frame("Design system · 10", "Calls to action", "Drawn as what happens next.",
                 "Three calls to action, each with its own drawing in the campus style: we visit the school, you get the price sheet, we train your staff.", body)


DS.append(("DS10-ctas", "Calls to action", ds_ctas))


# ---- 11 departments and school types -------------------------------------------------------------
def ds_departments():
    import pages, dept_art
    tiles = "".join(pages.dept_tile(*d) for d in CP.DEPARTMENTS)
    types = "".join(f'<div style="width:232px">{tile(dept_art.art(k, 232, 170, U=32), 232, 170, PLATE)}<div style="font:600 16px {SANS};margin-top:12px">{n}</div>'
                    f'<div style="font:400 13.5px/1.5 {SANS};color:{INK2};margin-top:4px">{d}</div></div>' for n, k, d in CP.SCHOOL_TYPES)
    own = "".join(f'<div style="display:flex;align-items:center;gap:10px;padding:10px 0;border-top:1px solid {LINE};font:400 14.5px {SANS};color:{INK2}">'
                  f'{__import__("portal_art").portal_icon(p_, 28)}<span style="font-weight:600;color:{INK};width:240px">{n}</span>{p_} portal</div>' for n, sl, d, p_, k in CP.DEPARTMENTS)
    body = (block("Department tiles", f'<div style="display:grid;grid-template-columns:repeat(3,389px);gap:24px">{tiles}</div>', 0)
            + block("Which portal draws each department", f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 48px">{own}</div>')
            + block("School types · K-12", f'<div style="display:flex;justify-content:space-between">{types}</div>'))
    return frame("Design system · 11", "Departments", "Nine departments, five kinds of school.",
                 "The Veracross split in our words. Each department is a small place in the school, drawn in the style of the portal it belongs to; each type of school is the building that tells it apart.", body)


DS.append(("DS11-departments", "Departments", ds_departments))

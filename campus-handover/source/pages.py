# -*- coding: utf-8 -*-
"""Campus site pages after the positioning round (1 Oct 2026): type leads, the drawing carries the pictures,
cards show the product. Home, a department page (Academics and student life) and Moving to Campus."""
from ds import *
import dept_art, portal_art, cta_art
import iso_campus as ISO

SDK = "/root/.claude/plugins/synced/f83d1a09-511c-45a3-835c-21ea18df88cf_b7d94d8a-a046-4159-ad33-19d70dd8e185/saas-design~g2/lib"
import sys
sys.path.insert(0, SDK)
from sdkit import icons as SI  # noqa: E402

EYE = BLUE
X = 120          # page gutter


def eyebrow(t, key=None, c=EYE):
    """the eyebrow: blue, sentence case, with the page's drawn icon when it has one"""
    import nav_icons
    lead = nav_icons.nav_icon(key, 30) if key else ""
    return f'<div style="display:flex;align-items:center;gap:10px;font:500 15px {SANS};color:{c};letter-spacing:0.005em">{lead}{t}</div>'


def head(t, size=52, w=720, c=INK):
    return f'<h2 style="margin:0;font:600 {size}px/1.08 {SANS};letter-spacing:-0.034em;color:{c};max-width:{w}px;text-wrap:balance">{t}</h2>'


def explore(t="Explore"):
    return (f'<span style="display:inline-flex;align-items:center;gap:6px;font:600 15px {SANS};color:{INK}">{t}'
            f'{ic("arrow-right-line", 15, BLUE)}</span>')


GAP = 160       # space between sections, so each one is read before the next


def band(inner, bg="#fff", pad=f"{GAP}px {X}px"):
    return f'<section style="background:{bg};padding:{pad}">{inner}</section>'


ROW_ICON = {"Single record": "record", "Works without internet": "nointernet", "Integrations": "integrations", "Training and support": "training",
            "Data and security": "security", "Registers": "academics", "Marks and reports": "record", "Timetables": "calendar-t", "Family communication": "communication"}


def row(eye, h, b, pic, flip=False, extra=""):
    """the Veracross row: eyebrow, a verb-led headline, a paragraph; the picture beside it at the same height"""
    txt = (f'<div style="flex:1;display:flex;flex-direction:column;gap:18px;justify-content:center;max-width:500px">{eyebrow(eye, ROW_ICON.get(eye))}{head(h, 42, 500)}'
           f'{para(b, 18, INK2, 480)}{extra}</div>')
    pic_ = f'<div style="flex:none">{pic}</div>'
    return f'<div style="display:flex;gap:96px;align-items:center;justify-content:space-between">{pic_ + txt if flip else txt + pic_}</div>'


def on_plate(inner, w=620, h=420):
    return f'<div style="position:relative;width:{w}px;height:{h}px;border-radius:28px;{DOTS};box-shadow:inset 0 0 0 1px #eceef2;overflow:hidden">{inner}</div>'


def logo_of(ref, color, size=28):
    return SI.svg(ref, size, color)


# ---- pictures for the rows --------------------------------------------------------------------------
def pic_record(w=620, h=420):
    return on_plate(f'<div style="position:absolute;left:-30px;top:-10px">{scaled(cards_plate(), 680, 383, 680 / 1280)}</div>'
                    f'<div style="position:absolute;left:24px;bottom:22px;display:flex;gap:8px">'
                    + "".join(f'<span style="display:inline-flex;align-items:center;gap:6px;height:28px;padding:0 10px 0 4px;border-radius:14px;background:#fff;box-shadow:inset 0 0 0 1px {LINE};font:500 12.5px {SANS}">'
                              f'{portal_art.portal_icon(p_, 20)}{n}</span>' for n, p_ in (("Fees", "Administration"), ("Marks", "Teacher"), ("Receipts", "Administration"), ("Head's view", "Administration")))
                    + '</div>', w, h)


def pic_offline(w=620, h=420):
    from ui import register_card
    return photo_story("classroom-zambia.jpg", "center 40%", [(0, 60, register_card(SB, 300, offline=True))], w, h)


def pic_integrations(w=620, h=420):
    core = (f'<div style="position:absolute;left:48px;top:140px;width:200px;height:140px;border-radius:20px;background:#fff;box-shadow:0 0 0 1px {LINE},0 18px 30px -20px rgba(11,12,20,.35);'
            f'display:flex;flex-direction:column;justify-content:center;align-items:flex-start;gap:14px;padding:0 24px;box-sizing:border-box">{lockup(24, by=False)}'
            f'<div style="font:400 13px {SANS};color:{MUTED}">One record per pupil</div></div>')
    items = [(logo_of("simple-icons:sage", "#00D639", 30), "Sage Pastel", "Journals, the ledger"),
             (logo_of("simple-icons:quickbooks", "#2CA01C", 30), "QuickBooks", "Invoices, payments"),
             (__import__("brands").logo("ZIMRA", 30), "ZIMRA fiscalisation", "Fiscal receipts (FDMS)")]
    out, ys = "", (58, 175, 292)
    for (lg, n, d), y in zip(items, ys):
        out += (f'<div style="position:absolute;left:340px;top:{y}px;width:240px;height:72px;border-radius:16px;background:#fff;box-shadow:0 0 0 1px {LINE},0 14px 24px -18px rgba(11,12,20,.3);'
                f'display:flex;align-items:center;gap:12px;padding:0 16px;box-sizing:border-box">{lg}<div><div style="font:600 15px {SANS}">{n}</div>'
                f'<div style="font:400 12.5px {SANS};color:{MUTED};margin-top:2px">{d}</div></div></div>')
    # connectors: from the record's right edge to each tile's left edge, drawn as an elbow
    lines = (f'<span style="position:absolute;left:248px;top:210px;width:46px;height:1.5px;background:#9aa1ad"></span>'
             f'<span style="position:absolute;left:294px;top:94px;width:1.5px;height:234px;background:#9aa1ad"></span>'
             + "".join(f'<span style="position:absolute;left:294px;top:{y + 36}px;width:46px;height:1.5px;background:#9aa1ad"></span>'
                       f'<span style="position:absolute;left:336px;top:{y + 33}px;width:7px;height:7px;border-radius:4px;background:#fff;border:1.5px solid {INK};box-sizing:border-box"></span>' for y in ys))
    return on_plate(lines + core + out, w, h)


def pic_training(w=620, h=420):
    return on_plate(f'<div style="position:absolute;left:10px;top:0">{cta_art.cta_scene("training", 600, 430, 46, 300, 262)}</div>', w, h)


def pic_security(w=620, h=420):
    rows = [("Mrs Ncube", "Bursar", "Fees, payroll, the books"), ("Ms Sibanda", "Class teacher", "Form 3B registers and marks"),
            ("Rudo Moyo", "Guardian", "Tanaka only"), ("Mr Dube", "Head", "Every department")]
    r = "".join(f'<div style="display:flex;align-items:center;gap:12px;padding:11px 0;border-top:1px solid {LINE}"><div style="flex:1"><div style="font:600 14px {SANS}">{n}</div>'
                f'<div style="font:400 12.5px {SANS};color:{MUTED}">{role}</div></div><div style="font:400 13px {SANS};color:{INK2};width:170px">{acc}</div></div>' for n, role, acc in rows)
    card_ = (f'<div style="position:absolute;left:60px;top:44px;width:420px;border-radius:18px;background:#fff;box-shadow:0 0 0 1px {LINE},0 18px 30px -20px rgba(11,12,20,.35);padding:16px 18px 6px;box-sizing:border-box">'
             f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:10px">{pmark("Campus", 28, 8)}<div style="font:600 15px {SANS}">Who sees what</div>'
             f'<span style="flex:1"></span><span style="font:400 12px {MONO};color:{MUTED}">Mukuvisi High</span></div>{r}</div>')
    chip = (f'<div style="position:absolute;left:300px;top:322px;display:flex;flex-direction:column;gap:8px">'
            f'<span style="display:inline-flex;align-items:center;gap:8px;height:34px;padding:0 14px 0 10px;border-radius:17px;background:#fff;box-shadow:0 0 0 1px {LINE};font:500 13px {SANS}">{ic("safe-lock", 15, OK)}Backed up at 02:00 today</span>'
            f'<span style="display:inline-flex;align-items:center;gap:8px;height:34px;padding:0 14px 0 10px;border-radius:17px;background:#fff;box-shadow:0 0 0 1px {LINE};font:500 13px {SANS}">{ic("download-2", 15, BLUE)}Export everything (.zip)</span></div>')
    return on_plate(card_ + chip, w, h)


# ---- sections ---------------------------------------------------------------------------------------
def hero(w=1440):
    H = CP.HERO
    import hero as HR
    tick = "".join(f'<span style="display:inline-flex;align-items:center;gap:7px;font:500 14.5px {SANS};color:{INK2}">{ic("check-circle", 15, OK)}{t}</span>'
                   for t in ("Setup and training free", "First month free", "US$1 per active pupil per month"))
    txt = (f'<div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:24px;padding:88px {X}px 0">'
           f'<h1 style="margin:0;font:600 64px/1.04 {SANS};letter-spacing:-0.04em;max-width:960px;text-wrap:balance">{H["h1a"]}</h1>{para(H["body"], 20, INK2, 640, True)}'
           f'<div style="display:flex;gap:12px;margin-top:6px">{cbtn(H["cta"], "calendar", "primary", "lg")}{cbtn(H["cta2"], "arrow-down-line", "secondary", "lg")}</div>'
           f'<div style="display:flex;gap:22px">{tick}</div></div>')
    pic = f'<div style="display:flex;justify-content:center;padding:56px {X}px 0">{HR.hero_picture()}</div>'
    return f'<section>{txt}{pic}</section>'


def dept_tile(n, sl, d, p_, k, w=389, h=400):
    return (f'<div style="position:relative;width:{w}px;height:{h}px;border-radius:24px;background:{PLATE};overflow:hidden;box-sizing:border-box;padding:28px 28px 0">'
            f'<div style="font:600 28px/1.12 {SANS};letter-spacing:-0.025em;max-width:300px">{n}</div>'
            f'<div style="font:400 15px/1.5 {SANS};color:{INK2};margin-top:10px;max-width:320px">{d}</div>'
            f'<div style="position:absolute;left:28px;bottom:26px">{explore()}</div>'
            f'<div style="position:absolute;right:-26px;bottom:-30px">{dept_art.art(k, 330, 228, U=42)}</div></div>')


def departments(w=1440):
    a, b = CP.DEPTS_H
    tiles = "".join(dept_tile(*d) for d in CP.DEPARTMENTS)
    return band(f'<div style="display:flex;flex-direction:column;gap:16px;margin-bottom:48px">{eyebrow("Solutions", "solutions")}{head(a, 52, 640)}</div>'
                f'<div style="display:grid;grid-template-columns:repeat(3,389px);gap:24px">{tiles}</div>')


def schools_plate(w=600, h=420):
    """the five kinds of K-12 school, each drawn as its building, gathered on one plate"""
    return on_plate(dept_art.schools_campus(w, h), w, h)


def focus(w=1440):
    h_, b_ = CP.FOCUS
    txt = (f'<div style="flex:1;display:flex;flex-direction:column;gap:20px">{eyebrow("Who we serve · K-12", "who")}{head(h_, 44, 560)}{para(b_, 18, INK2, 520)}'
           f'<div style="display:flex;gap:12px;margin-top:6px">{cbtn("Book a demo", "calendar", "primary", "lg")}{cbtn("See who we serve", "arrow-right-line", "secondary", "lg")}</div></div>')
    return (f'<div style="padding:0 {X - 40}px"><div style="display:flex;align-items:center;gap:48px;border-radius:32px;background:{PLATE};padding:24px 24px 24px 64px">'
            f'{txt}<div style="flex:none;border-radius:24px;overflow:hidden">{schools_plate()}</div></div></div>')


def rows(w=1440):
    import mark_anim
    pics = [mark_anim.mark_journey(620, 460), pic_offline(), pic_integrations(), pic_training(), pic_security()]
    out = "".join(f'<div style="margin-top:{0 if i == 0 else GAP}px">{row(e, h_, b_, p, flip=i % 2 == 1)}</div>' for i, ((e, h_, b_), p) in enumerate(zip(CP.ROWS, pics)))
    return band(out)


TYPE_PHOTO = {"t-day": ("girls-classroom.jpg", "center 35%"), "t-boarding": ("boys-reading.jpg", "center 40%"), "t-government": ("classroom-uniforms.jpg", "center"),
              "t-private": ("seniors-lecture.jpg", "center 30%"), "t-mission": ("teacher-garden.jpg", "center 30%")}


def who(w=1440):
    import nav_icons
    a, b = CP.WHO_H
    types = "".join(f'<div style="width:232px;display:flex;flex-direction:column"><div style="position:relative;width:232px;height:250px">{ph(TYPE_PHOTO[k][0], 232, 250, TYPE_PHOTO[k][1], 20)}'
                    f'<div style="position:absolute;left:12px;bottom:12px;border-radius:12px;box-shadow:0 8px 18px -10px rgba(11,12,20,.5)">{nav_icons.nav_icon(k, 44)}</div></div>'
                    f'<div style="font:600 19px {SANS};margin-top:16px">{n}</div><div style="font:400 14.5px/1.5 {SANS};color:{INK2};margin-top:6px">{d}</div>'
                    f'<div style="margin-top:auto;padding-top:16px">{explore()}</div></div>' for n, k, d in CP.SCHOOL_TYPES)
    return band(f'<div style="display:flex;flex-direction:column;gap:16px;margin-bottom:48px">{eyebrow("Who we serve · K-12", "who")}{head(a, 52, 640)}</div>'
                f'<div style="display:flex;justify-content:space-between;align-items:stretch">{types}</div>')


def site_footer():
    """the footer opens with Who we serve: the five kinds of K-12 school, people photographed at each, the building as its icon"""
    import nav_icons
    types = "".join(f'<div style="width:232px;display:flex;flex-direction:column"><div style="position:relative;width:232px;height:150px">{ph(TYPE_PHOTO[k][0], 232, 150, TYPE_PHOTO[k][1], 16)}'
                    f'<div style="position:absolute;left:10px;bottom:10px;border-radius:10px;box-shadow:0 8px 18px -10px rgba(11,12,20,.5)">{nav_icons.nav_icon(k, 36)}</div></div>'
                    f'<div style="font:600 16px {SANS};margin-top:12px">{n}</div></div>'
                    for n, k, d in CP.SCHOOL_TYPES)
    who_ = (f'<div style="padding:72px {X}px 64px;border-top:1px solid {LINE}"><div style="display:flex;align-items:baseline;justify-content:space-between;margin-bottom:28px">'
            f'{eyebrow("Who we serve · K-12", "who")}</div>'
            f'<div style="display:flex;justify-content:space-between;align-items:stretch">{types}</div></div>')
    return who_ + footer("a").replace("padding:72px", "padding:56px", 1)


def role_tile(n, p_, d, k, w=389, h=400):
    """a role, set like a department tile: the name big, one line, its portal, and the place it works drawn in the corner"""
    art = (portal_art.portal_scene("Student", 330, 228, 30, 175, 140, labels=False) if k == "pupils" else dept_art.art(k, 330, 228, U=42))
    return (f'<div style="position:relative;width:{w}px;height:{h}px;border-radius:24px;background:{PLATE};overflow:hidden;box-sizing:border-box;padding:28px 28px 0">'
            f'<div style="display:inline-flex;align-items:center;gap:6px;height:28px;padding:0 10px 0 4px;border-radius:14px;background:#fff;box-shadow:inset 0 0 0 1px {LINE};font:500 12.5px {SANS};color:{INK2}">'
            f'{portal_art.portal_icon(p_, 20)}{p_} portal</div>'
            f'<div style="font:600 28px/1.12 {SANS};letter-spacing:-0.025em;margin-top:16px;text-wrap:balance">{n}</div>'
            f'<div style="font:400 15px/1.5 {SANS};color:{INK2};margin-top:10px;max-width:320px">{d}</div>'
            f'<div style="position:absolute;left:28px;bottom:26px">{explore()}</div>'
            f'<div style="position:absolute;right:-26px;bottom:-30px">{art}</div></div>')


def roles(w=1440):
    tiles = "".join(role_tile(*r) for r in CP.ROLES)
    return band(f'<div style="display:flex;flex-direction:column;gap:16px;margin-bottom:48px">{eyebrow("Who uses Campus", "portals")}{head(CP.ROLES_H, 52, 640)}</div>'
                f'<div style="display:grid;grid-template-columns:repeat(3,389px);gap:24px">{tiles}</div>', pad=f"0 {X}px")


def steps(items, w=600):
    out = ""
    for i, (wk, t, d) in enumerate(items):
        last = i == len(items) - 1
        out += (f'<div style="position:relative;display:flex;gap:20px;padding-bottom:{0 if last else 26}px">'
                + ("" if last else f'<span style="position:absolute;left:19px;top:40px;bottom:0;width:1.5px;background:#c3c9d3"></span>')
                + f'<span style="width:40px;height:40px;border-radius:20px;background:{"#fff" if not last else BLUE};box-shadow:inset 0 0 0 1.5px {BLUE if not last else BLUE};'
                f'display:flex;align-items:center;justify-content:center;font:600 15px {SANS};color:{BLUE if not last else "#fff"};flex:none">{i + 1}</span>'
                f'<div style="padding-top:2px"><div style="display:flex;gap:10px;align-items:baseline"><span style="font:600 18px {SANS}">{t}</span>'
                f'<span style="font:400 13px {MONO};color:{MUTED}">{wk}</span></div><div style="font:400 15px/1.55 {SANS};color:{INK2};margin-top:4px;max-width:{w - 60}px">{d}</div></div></div>')
    return out


def switching(w=1440):
    S = CP.SWITCH
    left = (f'<div style="width:520px;display:flex;flex-direction:column;gap:20px">{eyebrow(S["eyebrow"], "moving")}{head(S["h_home"], 46, 520)}{para(S["b"], 18, INK2, 500)}'
            f'<div style="display:flex;flex-wrap:wrap;gap:8px;margin-top:4px">'
            + "".join(f'<span style="display:inline-flex;align-items:center;height:32px;padding:0 12px;border-radius:16px;background:#fff;box-shadow:inset 0 0 0 1px {LINE};font:500 13.5px {SANS};color:{INK2}">{m}</span>' for m in S["moves"])
            + f'</div><div style="margin-top:8px">{explore("How we move your records")}</div></div>')
    right = f'<div style="width:600px;border-radius:28px;background:#fff;box-shadow:0 0 0 1px {LINE};padding:36px 36px 32px;box-sizing:border-box">{steps(S["steps"])}</div>'
    return band(f'<div style="display:flex;justify-content:space-between;align-items:center">{left}{right}</div>', bg=PLATE)


def price_card(w=300):
    from ui import card, lab, fig
    P_ = CP.PRICING
    return card(SB, f'{lab(SB, P_["example"]["t"])}<div style="margin-top:8px">{fig(SB, P_["example"]["v"], 34)}</div>'
                    f'<div style="font:400 13.5px {SANS};color:{MUTED};margin-top:6px">{P_["example"]["s"]}</div>'
                    f'<div style="margin-top:12px;padding-top:10px;border-top:1px solid {LINE};font:400 13px {SANS};color:{INK2}">1,140 × US$1 per active pupil</div>', w, pad=18)


def price_band(w=1440):
    P_ = CP.PRICING
    txt = (f'<div style="flex:1;display:flex;flex-direction:column;gap:18px;max-width:500px">{eyebrow("Pricing", "pricing")}{head(P_["h"], 42, 500)}{para(P_["b"], 18, INK2, 480)}'
           f'<div>{ticks(["Setup, data capture and training free", "First month free", "Every department and portal included"])}</div>'
           f'<div>{cbtn("See pricing", "arrow-right-line", "secondary", "md")}</div></div>')
    pic = ph("seniors-lecture.jpg", 620, 440, "center 30%", 24)          # the worked-example card was taken off in the canvas (1 Oct)
    return band(f'<div style="display:flex;gap:96px;align-items:center;justify-content:space-between">{pic}{txt}</div>', pad=f"{GAP}px {X}px 0")


def home(w=1440):
    return (f'<div style="width:{w}px;background:#fff;font-family:{SANS};color:{INK}">{nav_bar(w=w)}{hero()}{departments()}{focus()}{rows()}<div style="height:0"></div>{roles()}'
            f'<div style="height:{GAP}px"></div>{switching()}{price_band()}<div style="padding:{GAP}px {X - 40}px">{cta_block("visit", w=w - 2 * (X - 40))}</div>{site_footer()}</div>')


# ---- department page: Academics and student life ----------------------------------------------------
def timetable_card(w=520):
    """the Form 3B timetable in edit mode: week switcher, a lesson being moved, undo and publish"""
    days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    periods = [("07:30", ["Maths", "English", "Maths", "Shona", "Science"]), ("08:40", ["Science", "Maths", "History", "Maths", "English"]),
               ("10:10", ["Shona", "Geography", "English", "Science", "Maths"]), ("11:20", ["English", "Science", "Shona", "Geography", "Sport"])]
    head_ = "".join(f'<div style="font:500 12px {SANS};color:{MUTED};padding:0 0 8px">{d}</div>' for d in days)
    grip = ('<span style="display:inline-grid;grid-template-columns:repeat(2,3px);gap:2px;margin-right:5px;vertical-align:middle">'
            + "".join(f'<i style="width:3px;height:3px;border-radius:2px;background:{BLUE}"></i>' for _ in range(6)) + '</span>')
    cells = ""
    for t, subs in periods:
        cells += f'<div style="font:400 12px {MONO};color:{MUTED};padding-top:10px">{t}</div>'
        for j, s_ in enumerate(subs):
            hot = (t, j) == ("10:10", 2)
            drop = (t, j) == ("11:20", 2)
            bg = "#ffffff" if hot else ("#f6f7f9" if not drop else "#f8faff")
            sh = (f"0 0 0 1.5px {BLUE},0 10px 18px -8px rgba(37,99,235,.45)" if hot else (f"inset 0 0 0 1.5px #9db8f5" if drop else "inset 0 0 0 1px #eceef2"))
            style = f"transform:translate(4px,-3px) rotate(-1.5deg);" if hot else ""
            border = "border:1.5px dashed #9db8f5;" if drop else ""
            label = (f'{grip}{s_}' if hot else s_)
            sub = "Room 12 now" if hot else ("Swap here" if drop else ("Lab" if s_ == "Science" else "3B"))
            cells += (f'<div style="position:relative;height:44px;border-radius:9px;padding:6px 8px;box-sizing:border-box;background:{bg};box-shadow:{sh};{border}{style}'
                      f'font:500 12.5px {SANS};color:{INK};white-space:nowrap">{label}'
                      f'<div style="font:400 10.5px {SANS};color:{BLUE if (hot or drop) else MUTED};margin-top:1px">{sub}</div></div>')
    sw = (f'<div style="display:inline-flex;align-items:center;height:30px;border-radius:9px;box-shadow:inset 0 0 0 1px {LINE}">'
          f'<span style="width:28px;display:flex;justify-content:center">{ic("left-line", 13, INK2)}</span>'
          f'<span style="font:500 12.5px {SANS};padding:0 4px">Week 4</span>'
          f'<span style="width:28px;display:flex;justify-content:center">{ic("right-line", 13, INK2)}</span></div>')
    seg = (f'<div style="display:inline-flex;height:30px;padding:3px;border-radius:9px;background:#f1f3f6;box-sizing:border-box">'
           f'<span style="padding:0 10px;border-radius:7px;background:#fff;box-shadow:0 1px 2px rgba(11,12,20,.12);font:500 12px {SANS};display:flex;align-items:center">Form 3B</span>'
           f'<span style="padding:0 10px;font:500 12px {SANS};color:{MUTED};display:flex;align-items:center">Teachers</span>'
           f'<span style="padding:0 10px;font:500 12px {SANS};color:{MUTED};display:flex;align-items:center">Rooms</span></div>')
    foot = (f'<div style="display:flex;align-items:center;gap:8px;margin-top:14px;padding-top:12px;border-top:1px solid {LINE}">'
            f'<span style="font:400 12.5px {SANS};color:{MUTED};flex:1">1 unpublished change</span>'
            f'<span style="height:32px;padding:0 12px;border-radius:9px;box-shadow:inset 0 0 0 1px {LINE};display:inline-flex;align-items:center;gap:6px;font:500 12.5px {SANS}">{ic("back-2-line", 13, INK2)}Undo</span>'
            f'<span style="height:32px;padding:0 12px;border-radius:9px;background:{BLUE};color:#fff;display:inline-flex;align-items:center;gap:6px;font:600 12.5px {SANS}">{ic("check-line", 13, "#fff")}Publish changes</span></div>')
    return card(SB, f'<div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">{pmark("Campus", 26, 7)}<div style="flex:1"><div style="font:600 14.5px {SANS}">Timetable</div>'
                    f'<div style="font:400 12px {SANS};color:{MUTED}">Term 3 · editing</div></div>{sw}</div>'
                    f'<div style="margin-bottom:12px">{seg}</div>'
                    f'<div style="display:grid;grid-template-columns:44px repeat(5,1fr);gap:6px">{"<div></div>" + head_}{cells}</div>{foot}', w, pad=18)


# ---- a phone at true size: a 393 x 852 point screen, system sizes as on the device, scaled down only when placed ----
SCR_W, SCR_H, BEZ = 393, 852, 12


def status_bar(t="16:10", dark=False):
    """the iOS status bar on a 393 pt iPhone 15 Pro, measured from Apple's HIG status-bar figure and its UI kit:
    a 393 x 54 bar; the time (semibold 17, tight tracking) centred in a 16-129 pt box; cellular 19.2 x 12.2,
    wi-fi 17.1 x 12.3 and battery 27.3 x 13 centred as one group in a 264-377 pt box, 5.8 and 7 pt apart;
    everything centred on y = 31, the line of the Dynamic Island's middle"""
    c = "#ffffff" if dark else "#000000"
    cy = 31.0
    # cellular: four bars 3.2 wide, 2.13 apart, rounded 1.1
    hs = (4.4, 6.9, 9.5, 12.2)
    cell = "".join(f'<rect x="{i * 5.33:.2f}" y="{12.2 - hgt:.2f}" width="3.2" height="{hgt}" rx="1.1" fill="{c}"/>' for i, hgt in enumerate(hs))
    # wi-fi: three filled annular sectors and a dot, a 90 degree fan pointing up from (8.57, 12.3)
    import math
    def sector(r0, r1, a0=225, a1=315, ox=8.57, oy=12.3):
        p = lambda r, a: (ox + r * math.cos(math.radians(a)), oy + r * math.sin(math.radians(a)))
        (x0, y0), (x1, y1), (x2, y2), (x3, y3) = p(r1, a0), p(r1, a1), p(r0, a1), p(r0, a0)
        return (f'<path d="M{x0:.2f} {y0:.2f} A{r1} {r1} 0 0 1 {x1:.2f} {y1:.2f} L{x2:.2f} {y2:.2f} A{r0} {r0} 0 0 0 {x3:.2f} {y3:.2f} Z" '
                f'fill="{c}" stroke="{c}" stroke-width="0.9" stroke-linejoin="round"/>')
    wifi = sector(0.01, 3.2) + sector(5.0, 7.6) + sector(9.4, 11.9)
    batt = (f'<rect x="0.5" y="0.5" width="24" height="12" rx="3.8" fill="none" stroke="{c}" stroke-opacity=".35"/>'
            f'<rect x="2" y="2" width="21" height="9" rx="2.5" fill="{c}"/>'
            f'<path d="M26 4.5c0.75 0.25 1.33 1 1.33 2s-0.58 1.75-1.33 2z" fill="{c}" fill-opacity=".4"/>')
    group = (f'<div style="position:absolute;left:264.3px;width:113px;top:{cy - 6.5:.1f}px;height:13px;display:flex;align-items:center;justify-content:center;gap:0">'
             f'<svg width="19.2" height="12.2" viewBox="0 0 19.2 12.2" style="display:block">{cell}</svg>'
             f'<svg width="17.14" height="12.33" viewBox="0 0 17.14 12.33" style="display:block;margin-left:5.8px">{wifi}</svg>'
             f'<svg width="27.33" height="13" viewBox="0 0 27.33 13" style="display:block;margin-left:7px">{batt}</svg></div>')
    time_ = (f'<div style="position:absolute;left:16px;width:113px;top:{cy - 11:.1f}px;height:22px;display:flex;align-items:center;justify-content:center;'
             f"font:600 17px/22px 'Inter',sans-serif;letter-spacing:-0.4px;color:{c};font-feature-settings:'tnum' 0,'cv11' 1\">{t}</div>")
    return f'<div style="position:relative;height:54px">{time_}{group}</div>'


def device(screen):
    """iPhone 15 Pro proportions: a 393 x 852 pt screen with 55 pt corners, a thin black border inside a titanium band,
    the Dynamic Island (126 x 37 pt, the front camera in its right end), the Action button and volume buttons on the
    left, the side button on the right, antenna breaks in the band, the home indicator"""
    w, h = SCR_W + 2 * BEZ, SCR_H + 2 * BEZ
    ti = "linear-gradient(90deg,#3d4045 0%,#8a8d93 6%,#55585e 14%,#3a3d42 50%,#55585e 86%,#8f9298 94%,#3d4045 100%)"
    btn = lambda side, top, hgt: (f'<span style="position:absolute;{side}:-3px;top:{top}px;width:4px;height:{hgt}px;border-radius:{"2px 0 0 2px" if side == "left" else "0 2px 2px 0"};'
                                  f'background:linear-gradient(90deg,#55585e,#9a9da3 50%,#55585e);box-shadow:0 0 0 0.5px rgba(0,0,0,.35)"></span>')
    breaks = "".join(f'<span style="position:absolute;{s}:0;top:{t}px;width:3px;height:5px;background:#9a9da3;opacity:.7"></span>' for s, t in (("left", 92), ("right", 92), ("left", h - 98), ("right", h - 98)))
    island = (f'<span style="position:absolute;left:50%;top:11px;transform:translateX(-50%);width:126px;height:37px;border-radius:19px;background:#000">'
              f'<i style="position:absolute;right:13px;top:11.5px;width:14px;height:14px;border-radius:7px;background:radial-gradient(circle at 40% 38%,#3b4b6e 0 18%,#151b2b 34%,#06080d 70%);'
              f'box-shadow:0 0 0 1px #0d1018"></i></span>')
    return (f'<div style="position:relative;width:{w}px;height:{h}px;flex:none">'
            + btn("left", 168, 30) + btn("left", 230, 60) + btn("left", 302, 60) + btn("right", 252, 96)
            + f'<div style="position:absolute;inset:0;border-radius:66px;background:{ti};box-shadow:inset 0 0 0 1px rgba(255,255,255,.25)"></div>'
            + breaks
            + f'<div style="position:absolute;inset:4px;border-radius:62px;background:#050506"></div>'
            f'<div style="position:absolute;left:{BEZ}px;top:{BEZ}px;width:{SCR_W}px;height:{SCR_H}px;border-radius:55px;overflow:hidden;background:#f2f3f6">{screen}{island}'
            f'<span style="position:absolute;left:50%;bottom:8px;transform:translateX(-50%);width:139px;height:5px;border-radius:3px;background:#000"></span></div></div>')


def parent_app():
    """the Parent portal on Rudo Moyo's phone at 16:10 on Thursday 1 October, at system sizes, in Inter (the closest open face to the system font)"""
    F = "'Inter',sans-serif"

    def card_(inner, pad="14px 16px"):
        return f'<div style="background:#fff;border-radius:16px;padding:{pad}">{inner}</div>'

    def lead(icn, bg, fg, s=34):
        return f'<span style="width:{s}px;height:{s}px;border-radius:10px;background:{bg};display:flex;align-items:center;justify-content:center;flex:none">{ic(icn, 18, fg)}</span>'

    sec = lambda t, r="": (f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin:22px 4px 8px">'
                           f'<span style="font:600 15px {F};color:{INK}">{t}</span><span style="font:400 15px {F};color:{BLUE}">{r}</span></div>')
    days = [("M", "ok"), ("T", "ok"), ("W", "late"), ("T", "ok"), ("F", "today")]
    strip = "".join(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:6px"><span style="font:400 12px {F};color:{MUTED}">{d}</span>'
                    f'<span style="width:28px;height:28px;border-radius:14px;display:flex;align-items:center;justify-content:center;'
                    f'background:{OKS if s_ == "ok" else (WARNS if s_ == "late" else "#e8effd")};box-shadow:{"inset 0 0 0 1.5px " + BLUE if s_ == "today" else "none"}">'
                    f'{ic("check-line" if s_ != "late" else "time-line", 14, OK if s_ == "ok" else (WARN if s_ == "late" else BLUE))}</span></div>' for d, s_ in days)
    att = card_(f'<div style="display:flex;align-items:center;gap:12px">{lead("check-circle", OKS, OK)}'
                f'<div style="flex:1"><div style="font:600 15px {F}">Present today</div><div style="font:400 13px {F};color:{MUTED};margin-top:1px">Marked at 07:42 by Ms Sibanda</div></div></div>'
                f'<div style="display:flex;margin-top:14px;padding-top:12px;border-top:1px solid #f0f1f4">{strip}</div>')
    marks = [("Mathematics", "Test 2", "71%", True), ("English", "Essay", "68%", False), ("Combined Science", "Practical", "74%", False)]
    mk = "".join(f'<div style="display:flex;align-items:center;gap:12px;padding:11px 0;{"border-top:1px solid #f0f1f4;" if i else ""}">'
                 f'<div style="flex:1"><div style="font:500 15px {F};color:{INK}">{n}</div><div style="font:400 13px {F};color:{MUTED};margin-top:1px">{t}{" · class average 64%" if new else ""}</div></div>'
                 + (f'<span style="height:20px;padding:0 7px;border-radius:10px;background:{BLUE};color:#fff;font:600 11px {F};display:inline-flex;align-items:center">New</span>' if new else "")
                 + f'<span style="font:600 15px {F};color:{INK};width:40px;text-align:right">{v}</span></div>' for i, (n, t, v, new) in enumerate(marks))
    fees = card_(f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font:400 13px {F};color:{MUTED}">Term 3 balance</span>'
                 f'<span style="font:500 13px {F};color:{WARN}">Due Fri 16 Oct</span></div>'
                 f'<div style="font:600 28px {F};letter-spacing:-0.02em;margin-top:2px">US$420.00</div>'
                 f'<div style="height:6px;border-radius:3px;background:#eef0f3;margin-top:10px;overflow:hidden"><div style="width:66%;height:100%;background:{OK}"></div></div>'
                 f'<div style="font:400 12px {F};color:{MUTED};margin-top:6px">US$830 of US$1,250 paid</div>'
                 f'<div style="margin-top:14px;height:46px;border-radius:12px;background:{BLUE};color:#fff;display:flex;align-items:center;justify-content:center;gap:8px;font:600 16px {F}">'
                 f'{ic("wallet-3", 17, "#ffffff")}Pay with EcoCash</div>')
    msg = card_(f'<div style="display:flex;gap:12px">{lead("message-3", "#efeaff", CAMPUS)}'
                f'<div style="flex:1;min-width:0"><div style="display:flex;justify-content:space-between"><span style="font:600 15px {F}">Ms Sibanda</span>'
                f'<span style="font:400 13px {F};color:{MUTED}">14:05</span></div>'
                f'<div style="font:400 14px/1.4 {F};color:{INK2};margin-top:2px">Tanaka did well on test 2. Keep up the practice on algebra this week.</div></div></div>')
    badge = (f'<span style="position:absolute;left:15px;top:-5px;min-width:18px;height:18px;padding:0 5px;box-sizing:border-box;border-radius:9px;background:#ff3b30;'
             f"color:#fff;font:600 12px/18px 'Inter',sans-serif;text-align:center\">2</span>")
    tabs = "".join(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:4px;font:500 10px {F};color:{BLUE if i == 0 else "#8e8e93"}">'
                   f'<span style="position:relative;display:block;width:24px;height:24px">{ic(n, 24, BLUE if i == 0 else "#8e8e93")}{badge if n == "message-3" else ""}</span>{t}</div>'
                   for i, (n, t) in enumerate((("home-3", "Home"), ("chart-bar", "Marks"), ("wallet-3", "Fees"), ("message-3", "Messages"), ("user-3", "Account"))))
    body = (f'<div style="padding:4px 16px 0">'
            f'<div style="display:flex;align-items:center;justify-content:space-between;height:44px">'
            f'<div style="display:flex;align-items:center;gap:9px">{pmark("Campus", 28, 8)}<span style="font:600 17px {F}">Parent portal</span></div>'
            f'<span style="position:relative;width:36px;height:36px;border-radius:18px;background:#fff;display:flex;align-items:center;justify-content:center">{ic("notification", 18, INK)}'
            f'<i style="position:absolute;right:8px;top:8px;width:8px;height:8px;border-radius:4px;background:{BAD};box-shadow:0 0 0 2px #fff"></i></span></div>'
            f'<div style="font:600 28px {F};letter-spacing:-0.025em;margin:10px 4px 12px">Good afternoon, Rudo</div>'
            f'<div style="display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:16px;background:#fff">'
            f'<span style="width:40px;height:40px;border-radius:20px;background:#e8effd;color:{BLUE};display:flex;align-items:center;justify-content:center;font:600 15px {F}">TM</span>'
            f'<div style="flex:1"><div style="font:600 16px {F}">Tanaka Moyo</div><div style="font:400 13px {F};color:{MUTED};margin-top:1px">Form 3B · Tsavo House</div></div>'
            f'<span style="font:400 15px {F};color:{BLUE};display:flex;align-items:center;gap:2px">Switch{ic("down-line", 13, BLUE)}</span></div>'
            + sec("Today", "Thu 1 Oct") + att
            + sec("Marks", "See all") + card_(mk, "4px 16px")
            + sec("Fees", "Statement") + fees
            + sec("Messages", "") + msg + '</div>')
    tabbar = (f'<div style="position:absolute;left:0;right:0;bottom:0;height:83px;background:#f9f9fb;box-shadow:0 -0.5px 0 rgba(0,0,0,.18);'
              f'display:flex;align-items:flex-start;padding:7px 4px 0;box-sizing:border-box">{tabs}</div>')
    return f'<div style="position:relative;width:{SCR_W}px;height:{SCR_H}px;background:#f2f3f6;font-family:{SANS};color:{INK};overflow:hidden">{status_bar()}{body}{tabbar}</div>'


def parent_phone(k=0.5):
    w, h = SCR_W + 2 * BEZ, SCR_H + 2 * BEZ
    inner = f'<div style="padding:0 6px">{device(parent_app())}</div>'                      # room for the side buttons
    return f'<div style="filter:drop-shadow(0 16px 22px rgba(11,12,20,.32))">{scaled(inner, round((w + 12) * k), round(h * k), k)}</div>'


def page_hero(eye, key, h, b, buttons, pic):
    """a page's hero: centred type, the picture below it at full column width"""
    return (f'<section><div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:22px;padding:88px {X}px 0">{eyebrow(eye, key)}'
            f'<h1 style="margin:0;font:600 60px/1.05 {SANS};letter-spacing:-0.04em;max-width:900px;text-wrap:balance">{h}</h1>{para(b, 20, INK2, 640, True)}'
            f'<div style="display:flex;gap:12px;margin-top:6px">{buttons}</div></div>'
            f'<div style="display:flex;justify-content:center;padding:56px {X}px 0">{pic}</div></section>')


def dept_page(w=1440):
    import hero as HR
    from ui import register_card, marks_card, report_card, parent_screen
    A = CP.ACADEMICS
    pic = (f'<div style="position:relative;width:1200px;height:600px">'
           f'<div style="position:absolute;left:90px;top:30px">{ph("teacher-maths.jpg", 1020, 570, "center 30%", 24)}</div>'
           + at(0, 120, HR.tagged("Teacher portal", register_card(SB, 300, offline=True)), 3)
           + at(880, 0, HR.tagged("Teacher portal", marks_card(SB, 320)), 2) + '</div>')
    top_ = page_hero(A["eyebrow"], "academics", A["h"], A["b"], cbtn("Book a demo", "calendar", "primary", "lg"), pic)
    bh, bb = A["band"]
    band_ = band(f'<div style="display:flex;align-items:center;justify-content:space-between;gap:96px">'
                 f'<div style="flex:1;display:flex;flex-direction:column;gap:20px;max-width:520px">{eyebrow("One record", "record")}{head(bh, 44, 520)}{para(bb, 19, INK2, 500)}</div>'
                 f'{ph("girls-classroom.jpg", 600, 420, "center 35%", 24)}</div>', bg=PLATE, pad=f"{GAP - 40}px {X}px")
    import mark_anim
    pics = [photo_story("classroom-zambia.jpg", "center 40%", [(0, 60, register_card(SB, 300, offline=True))], 620, 420),
            mark_anim.mark_journey(620, 460),
            on_plate(f'<div style="position:absolute;left:40px;top:28px">{timetable_card(540)}</div>', 620, 460),
            photo_story("mother-phone.jpg", "65% center", [(0, 8, parent_phone(0.52))], 620, 470)]
    rws = "".join(f'<div style="margin-top:{0 if i == 0 else GAP}px">{row(e, h_, b_, p, flip=i % 2 == 1)}</div>' for i, ((e, h_, b_), p) in enumerate(zip(A["rows"], pics)))
    tools = "".join(f'<div style="display:flex;align-items:center;gap:10px;padding:14px 0;border-top:1px solid {LINE};font:500 16px {SANS}">{ic("check-circle", 16, BLUE)}{t}</div>' for t in A["tools"])
    tools_ = band(f'<div style="display:flex;gap:96px"><div style="width:420px">{eyebrow("Features", "included")}<div style="margin-top:14px">{head(A["tools_h"], 40, 420)}</div></div>'
                  f'<div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:0 48px">{tools}</div></div>', pad=f"0 {X}px")
    return (f'<div style="width:{w}px;background:#fff;font-family:{SANS};color:{INK}">{nav_bar("Solutions", w)}{top_}<div style="height:{GAP}px"></div>{band_}{band(rws)}'
            f'{tools_}<div style="padding:{GAP}px {X - 40}px">{cta_block("visit", w=w - 2 * (X - 40))}</div>{site_footer()}</div>')


# ---- Moving to Campus -------------------------------------------------------------------------------
def switch_page(w=1440):
    S = CP.SWITCH
    pic = (f'<div style="width:1200px;height:520px;border-radius:32px;{DOTS};box-shadow:inset 0 0 0 1px #eceef2;overflow:hidden;display:flex;gap:0">'
           f'{cta_art.cta_scene("visit", 600, 520, 50, 300, 300)}{cta_art.cta_scene("training", 600, 520, 50, 300, 300)}</div>')
    top_ = page_hero(S["eyebrow"], "moving", S["h"], S["b"],
                     cbtn("Book a demo", "calendar", "primary", "lg") + cbtn("Download the price sheet (PDF)", "download-2", "secondary", "lg"), pic)
    cols = "".join(f'<div style="flex:1;border-radius:24px;background:#fff;box-shadow:inset 0 0 0 1px {LINE};padding:28px 26px;box-sizing:border-box;display:flex;flex-direction:column;gap:10px">'
                   f'<div style="font:600 22px {SANS};letter-spacing:-0.015em">{i + 1}. {t}</div><div style="font:400 15px/1.55 {SANS};color:{INK2}">{d}</div></div>'
                   for i, (wk, t, d) in enumerate(S["steps"]))
    plan = band(f'<div style="display:flex;flex-direction:column;gap:16px;margin-bottom:44px">{eyebrow("The four weeks", "demo")}{head("From your old system to your first term on Campus.", 46, 820)}</div>'
                f'<div style="display:flex;gap:20px;align-items:stretch">{cols}</div>', bg=PLATE)
    import nav_icons
    lines = ["Every pupil's record with their guardians, class and house.", "Contracts, leave balances and the details payroll needs.",
             "Each family's balance in US dollars and ZiG, signed off by the bursar.", "This year's marks and the reports already sent home.",
             "Forms, subjects, rooms and the timetable for the term.", "Stores, uniforms and textbooks, with what is issued to whom."]
    keys = ("Parent", "hr-payroll", "fees", "record", "calendar-t", "stock")
    shots = [("mother-phone.jpg", "65% center"), ("teacher-notebook.jpg", "center 25%"), ("classroom-uniforms.jpg", "center"),
             ("teacher-maths.jpg", "center 30%"), ("classroom-zambia.jpg", "center 40%"), ("boys-laptop.jpg", "center")]
    cards = "".join(f'<div class="cmp-hov" style="height:300px;border-radius:24px;background:{PLATE};box-sizing:border-box;padding:28px;display:flex;flex-direction:column">'
                    f'<div class="cmp-img">{ph(sh[0], 389, 300, sh[1], 0)}</div>'
                    f'<div class="cmp-txt" style="display:flex;flex-direction:column;height:100%">{nav_icons.nav_icon(k, 48)}'
                    f'<div style="margin-top:auto;font:600 24px/1.15 {SANS};letter-spacing:-0.02em;color:{INK};text-wrap:balance">{m}</div>'
                    f'<div style="font:400 15px/1.5 {SANS};color:{INK2};margin-top:8px">{ln}</div></div></div>'
                    for m, ln, k, sh in zip(S["moves"], lines, keys, shots))
    what = band(f'<div style="display:flex;flex-direction:column;gap:14px;margin-bottom:44px">{eyebrow("What moves", "stock")}{head("Everything the school keeps, on one record.", 46, 820)}</div>'
                f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px">{cards}</div>')
    qs = "".join(f'<div style="padding:22px 0;border-top:1px solid {LINE}"><div style="font:600 18px {SANS}">{q}</div><div style="font:400 16px/1.6 {SANS};color:{INK2};margin-top:6px;max-width:720px">{a}</div></div>' for q, a in S["faq"])
    faq_ = band(f'<div style="display:flex;gap:96px"><div style="width:420px">{eyebrow("Questions", "questions")}<div style="margin-top:14px">{head("What schools ask before they move.", 40, 420)}</div></div>'
                f'<div style="flex:1">{qs}</div></div>', pad=f"0 {X}px")
    return (f'<div style="width:{w}px;background:#fff;font-family:{SANS};color:{INK}">{nav_bar("Platform", w)}{top_}<div style="height:{GAP}px"></div>{plan}{what}{faq_}'
            f'<div style="padding:{GAP}px {X - 40}px">{cta_block("training", w=w - 2 * (X - 40))}</div>{site_footer()}</div>')


# the canvas caps an artboard at 8,000px, so Home is shown in two consecutive boards, split between sections
def home_a(w=1440):
    return f'<div style="width:{w}px;background:#fff;font-family:{SANS};color:{INK}">{nav_bar(w=w)}{hero()}{departments()}{focus()}{rows()}</div>'


def home_b(w=1440):
    return (f'<div style="width:{w}px;background:#fff;font-family:{SANS};color:{INK}">{roles()}'
            f'<div style="height:{GAP}px"></div>{switching()}{price_band()}<div style="padding:{GAP}px {X - 40}px">{cta_block("visit", w=w - 2 * (X - 40))}</div>{site_footer()}</div>')

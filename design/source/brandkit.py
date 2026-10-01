# -*- coding: utf-8 -*-
"""Corelith Campus brand kit, direction AB: people in photographs, the school as a drawing, the product as cards.
Each board is a 1440-wide page; the same HTML is rendered here for review and written out as a canvas artboard."""
from landing import *
import iso5 as I

SB = SIGS["b"]
GROUND = "#f7f8fa"
DOTS = f"background:{GROUND} radial-gradient(#dfe2e8 1px,transparent 1.2px) 0 0/22px 22px"


def lum(h):
    h = h.lstrip("#")
    c = [int(h[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    c = [x / 12.92 if x <= 0.03928 else ((x + 0.055) / 1.055) ** 2.4 for x in c]
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2]


def contrast(a, b="#ffffff"):
    la, lb = sorted((lum(a), lum(b)), reverse=True)
    return (la + 0.05) / (lb + 0.05)


def frame(num, title, sub, intro, body, pad_bottom=96):
    return (f'<div style="width:1440px;background:#fff;padding:72px 80px {pad_bottom}px;box-sizing:border-box;font-family:{SANS};color:{INK}">'
            f'<div style="display:flex;align-items:center;justify-content:space-between;padding-bottom:18px;border-bottom:1px solid {LINE}">'
            f'<span style="display:flex;align-items:center;gap:14px">{lockup(20)}</span>'
            f'<span style="font:500 14px {SANS};color:{MUTED}">{num}</span></div>'
            f'<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:64px;margin-top:48px">'
            f'{h2(title, sub, 44)}<div style="width:480px;flex:none">{para(intro, 17, INK2, 480)}</div></div>'
            f'<div style="margin-top:48px">{body}</div></div>')


def tile(inner, w, h, bg="#fff", extra=""):
    return (f'<div style="position:relative;width:{w}px;height:{h}px;border-radius:24px;background:{bg};box-shadow:inset 0 0 0 1px {LINE};'
            f'overflow:hidden;flex:none;{extra}">{inner}</div>')


def cap(t, d="", c=INK):
    return (f'<div style="margin-top:14px"><div style="font:600 15px {SANS};color:{c}">{t}</div>'
            + (f'<div style="font:400 14px/1.5 {SANS};color:{MUTED};margin-top:3px">{d}</div>' if d else "") + '</div>')


def dodont(ok, t):
    c, icn = (OK, "check-circle") if ok else (BAD, "close-circle")
    return f'<div style="display:flex;gap:8px;align-items:flex-start;margin-top:14px;font:500 14.5px/1.45 {SANS};color:{c}"><span style="padding-top:2px">{ic(icn, 16, c)}</span>{t}</div>'


def scaled(html, w, h, k):
    """a fixed-size piece shown at scale k inside a w x h box"""
    return (f'<div style="width:{w}px;height:{h}px;overflow:hidden;position:relative;flex:none">'
            f'<div style="position:absolute;left:0;top:0;width:{w / k:.0f}px;height:{h / k:.0f}px;transform:scale({k});transform-origin:0 0">{html}</div></div>')


def iso_scene(w=1280, h=720):
    svg, labels = ISO.scene()
    return f'<div style="position:relative;width:1280px;height:720px;{DOTS}">{svg}{ISO.pills(labels, ic)}</div>'


def photo_collage():
    """the hero composite: a photo with product cards on its edge"""
    return (f'<div style="position:relative;width:1280px;height:720px;background:#fff">'
            f'<div style="position:absolute;left:250px;top:40px">{ph("boys-reading-2.jpg", 980, 640, "58% 40%", 24)}</div>'
            + at(60, 250, register_card(SB, 320, offline=True), 2)
            + at(1000, 80, card(SB, f'{lab(SB, "Attendance today")}<div style="margin-top:8px">{fig(SB, "96.4%", 32)}</div><div style="margin-top:10px">{status(SB, "1,099 of 1,140", "ok")}</div>', pad=20), 2)
            + at(860, 580, card(SB, f'<div style="display:flex;align-items:center;gap:10px">{ic("message-3", 18, BLUE)}<span style="font:500 15px {SANS};white-space:nowrap">To Rudo Moyo: Tanaka scored 71% in test 2</span></div>', pad=16), 3)
            + '</div>')


def type_sample(w=1280, h=720):
    """a section as type alone: the eyebrow, the claim, the paragraph"""
    return (f'<div style="width:{w}px;height:{h}px;background:#fff;display:flex;flex-direction:column;justify-content:center;gap:28px;padding:0 120px;box-sizing:border-box">'
            f'<div style="font:500 26px {SANS};color:{BLUE}">School management for K-12</div>'
            f'<div style="font:600 92px/1.02 {SANS};letter-spacing:-0.04em;max-width:1000px">A school management platform that puts people first.</div>'
            f'<div style="font:400 30px/1.5 {SANS};color:{INK2};max-width:900px">Software for every department in your school, with one record at the centre.</div></div>')


def cards_plate(w=1280, h=720):
    return (f'<div style="position:relative;width:{w}px;height:{h}px;{DOTS}">'
            + at(120, 90, fee_card(SB, 380)) + at(540, 60, marks_card(SB, 340), 2) + at(420, 330, receipts_card(SB, 300), 3)
            + at(800, 300, head_card(SB, 340), 3) + '</div>')


# ---- 01 cover -------------------------------------------------------------------------------------
def bk_cover():
    k = 1260 / 1280 * 0.5
    trio = [("Type", "Plain headlines lead every section: an eyebrow, one claim, one paragraph.", type_sample()),
            ("Photographs", "People at school: pupils, teachers, a parent at home. Campus is a platform for people.", photo_collage()),
            ("The drawing", "The school as one campus, each portal labelled on the building where it is used.", iso_scene()),
            ("Cards", "The product as staff and parents see it: registers, marks, fees and receipts, with one school's figures.", cards_plate())]
    cols = "".join(f'<div style="width:305px">{tile(scaled(html, 305, 172, 305 / 1280), 305, 172)}{cap(t, d)}</div>' for t, d, html in trio)
    import pages
    body = (f'<div style="display:flex;gap:20px">{tile(scaled(pages.hero(), 630, 354, 630 / 1440), 630, 354)}{tile(scaled(iso_scene(), 630, 354, 630 / 1280), 630, 354)}</div>'
            f'<div style="display:flex;justify-content:space-between;margin-top:56px">{cols}</div>'
            f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-top:64px;padding-top:28px;border-top:1px solid {LINE}">'
            + "".join(f'<div><div style="font:500 13px {SANS};color:{MUTED}">{a}</div><div style="font:500 16px {SANS};margin-top:6px">{b}</div></div>'
                      for a, b in (("Product", "Corelith Campus, school management"), ("Made by", "Corelith Labs, Harare"), ("Readers", "Heads, SDCs, bursars, teachers, parents"), ("Launched", "Thursday 1 October 2026")))
            + '</div>')
    head = (f'<div style="width:1440px;background:#fff;padding:72px 80px 96px;box-sizing:border-box;font-family:{SANS};color:{INK}">'
            f'<div style="display:flex;align-items:center;justify-content:space-between;padding-bottom:18px;border-bottom:1px solid {LINE}">{lockup(20)}'
            f'<span style="font:500 14px {SANS};color:{MUTED}">Brand kit · 01</span></div>'
            f'<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-top:56px;gap:64px">'
            f'<h1 style="margin:0;font:600 76px/1.02 {SANS};letter-spacing:-0.04em">Corelith Campus<br><span style="color:{FAINT}">Brand kit</span></h1>'
            f'<div style="width:520px">{para("Campus is a platform for people. Plain headlines lead each section; photographs show the people at school; the drawing shows the school, its departments and what happens next; cards show the product as staff and parents see it.", 18, INK2, 520)}</div></div>'
            f'<div style="margin-top:56px">{body}</div></div>')
    return head


# ---- 02 logo --------------------------------------------------------------------------------------
def bk_logo():
    big = lockup(64)
    clear = (f'<div style="position:relative;padding:32px;border:1.5px dashed #c3c8d1;border-radius:8px">{big}'
             f'<span style="position:absolute;left:-1px;top:-24px;font:500 12px {MONO};color:{MUTED}">x = tile ÷ 2</span></div>')
    main = tile(f'<div style="height:100%;display:flex;align-items:center;justify-content:center">{clear}</div>', 880, 360)
    comp = tile(f'<div style="height:100%;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:14px">{lockup(40, by=False)}'
                f'<span style="font:400 13px {SANS};color:{MUTED}">Compact: product nav, app bar</span></div>', 380, 170, PLATE)
    onph = (f'<div style="position:relative;width:380px;height:170px;border-radius:24px;overflow:hidden">{ph("girls-classroom.jpg", 380, 170, "center 35%", 24)}'
            f'<div style="position:absolute;left:20px;bottom:20px;padding:10px 14px;border-radius:12px;background:#fff">{lockup(20)}</div></div>')
    right = f'<div style="display:flex;flex-direction:column;gap:20px">{comp}{onph}</div>'
    sizes = "".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:10px;justify-content:flex-end">{pmark("Campus", s_, round(s_ * 0.26))}'
                    f'<span style="font:400 12px {MONO};color:{MUTED}">{s_}</span></div>' for s_ in (128, 64, 40, 24, 16))
    app = (f'<div style="display:flex;gap:28px;align-items:flex-end">{sizes}'
           f'<div style="width:1px;height:120px;background:{LINE};margin:0 12px"></div>'
           f'<div style="display:flex;flex-direction:column;align-items:center;gap:10px"><div style="width:128px;height:128px;border-radius:28px;background:#fff;box-shadow:0 0 0 1px {LINE},0 12px 30px -18px rgba(11,12,20,.35);display:flex;align-items:center;justify-content:center">{pmark("Campus", 84, 22)}</div>'
           f'<span style="font:400 12px {MONO};color:{MUTED}">app icon</span></div></div>')
    rel = (f'<div style="display:flex;flex-direction:column;gap:18px;justify-content:center;height:100%;padding:0 36px">'
           f'<div style="display:flex;flex-direction:column;gap:12px"><div style="display:flex;align-items:center;justify-content:space-between"><span style="font:500 12px {SANS};color:{MUTED}">Nav</span>{lockup(20)}</div>'
           f'<div style="display:flex;align-items:center;justify-content:space-between;padding-top:12px;border-top:1px solid {LINE}"><span style="font:500 12px {SANS};color:{MUTED}">Footer</span>{logo(18, INK)}</div></div>'
           f'<div style="font:400 14.5px/1.55 {SANS};color:{INK2}">"by Corelith" sits beside the product name in the nav. The full Corelith logo goes in the footer. The Corelith mark keeps its own blue, #0F62FE, and is never recoloured or split.</div></div>')
    bad = [(f'<span style="display:inline-flex;align-items:center;gap:10px"><span style="width:34px;height:34px;border-radius:9px;background:{BLUE};display:flex;align-items:center;justify-content:center">{ic("school", 18, "#fff")}</span>'
            f'<span style="font:600 30px {SANS};letter-spacing:-0.03em">campus</span></span>', "Recolour the product tile"),
           (f'<span style="display:inline-flex;align-items:center;gap:10px">{pmark("Campus", 34, 9)}<span style="font:600 26px {SANS};letter-spacing:0.08em">CAMPUS</span></span>', "Set the name in capitals"),
           (f'<div style="position:relative;width:260px;height:110px;border-radius:14px;overflow:hidden">{ph("classroom-uniforms.jpg", 260, 110, "center", 14)}'
            f'<div style="position:absolute;left:16px;top:36px">{lockup(24, "#fff", False)}</div></div>', "Put the lockup straight on a photo"),
           (f'<span style="display:inline-flex;align-items:center;gap:10px">{pmark("Campus", 34, 9)}<span style="font:600 30px {SERIF};letter-spacing:-0.01em">Campus</span></span>', "Change the typeface")]
    bads = "".join(f'<div style="width:295px">{tile(f"<div style=&quot;height:100%;display:flex;align-items:center;justify-content:center&quot;>{x}</div>", 295, 150)}{dodont(False, t)}</div>' for x, t in bad)
    body = (f'<div style="display:flex;gap:20px">{main}{right}</div>'
            f'<div style="display:flex;gap:20px;margin-top:20px">{tile(f"<div style=&quot;height:100%;display:flex;align-items:center;padding:0 48px&quot;>{app}</div>", 880, 230)}{tile(rel, 380, 230)}</div>'
            f'<div style="font:600 17px {SANS};margin-top:56px">Don\'t</div><div style="display:flex;justify-content:space-between;margin-top:16px">{bads}</div>')
    return frame("Brand kit · 02", "Logo", "The lockup and its parent logo.",
                 "The mark is the school drawn in the campus projection: one block, its gable roof and the flag, white on the Campus tile. The lockup is the mark, the name in lower case, and \"by Corelith\" in the nav. Keep clear space of half the tile's height on every side.",
                 body.replace("&quot;", '"'))


# ---- 03 colour ------------------------------------------------------------------------------------
def bk_colour():
    main = [("Ink", INK, "#fff", "Headings, body, the dark button"), ("Accent", BLUE, "#fff", "Buttons, active states, roofs and portal tiles"),
            ("Campus", CAMPUS, "#fff", "The product tile and portal tags, nothing else"), ("Plate", PLATE, INK, "Section bands, trays, dotted plates"),
            ("Line", LINE, INK, "Rules, card outlines, input borders")]
    sw = "".join(f'<div style="flex:1"><div style="height:200px;border-radius:20px;background:{c};box-shadow:inset 0 0 0 1px rgba(11,12,20,.06);padding:20px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:space-between;color:{t}">'
                 f'<span style="font:600 20px {SANS}">{n}</span><span style="font:400 13px {MONO}">{c.upper()}</span></div>'
                 f'<div style="font:400 14px/1.5 {SANS};color:{INK2};margin-top:12px">{d}</div>'
                 f'<div style="font:400 12px {MONO};color:{MUTED};margin-top:6px">{contrast(c):.1f}:1 on white</div></div>' for n, c, t, d in main)
    greys = [("Ink 2", INK2, "Body text"), ("Muted", MUTED, "Secondary text"), ("Faint", FAINT, "Heading second line, disabled"), ("Ground", GROUND, "Illustration ground")]
    gs = "".join(f'<div style="display:flex;align-items:center;gap:14px;padding:12px 0;border-top:1px solid {LINE}"><span style="width:36px;height:36px;border-radius:10px;background:{c};box-shadow:inset 0 0 0 1px rgba(11,12,20,.06)"></span>'
                 f'<div style="flex:1"><div style="font:500 15px {SANS}">{n}</div><div style="font:400 13px {SANS};color:{MUTED}">{d}</div></div><span style="font:400 12px {MONO};color:{MUTED}">{c.upper()}</span></div>' for n, c, d in greys)
    drops = [("Roof blue", "#2563eb", "classroom roofs"), ("Jacaranda", "#c9bdf0", "three trees at most"), ("Field", "#dfe9d6", "the sports field"), ("Boom red", "#e0533f", "the gate boom only"), ("Flag green", "#12805c", "the flag")]
    ds = "".join(f'<div style="display:flex;align-items:center;gap:14px;padding:12px 0;border-top:1px solid {LINE}"><span style="width:36px;height:36px;border-radius:18px;background:{c}"></span>'
                 f'<div style="flex:1"><div style="font:500 15px {SANS}">{n}</div><div style="font:400 13px {SANS};color:{MUTED}">{d}</div></div><span style="font:400 12px {MONO};color:{MUTED}">{c.upper()}</span></div>' for n, c, d in drops)
    st = "".join(f'<div style="display:flex;align-items:center;justify-content:space-between;padding:12px 0;border-top:1px solid {LINE}">{status(SB, t, k)}<span style="font:400 12px {MONO};color:{MUTED}">{c.upper()} on {bg.upper()}</span></div>'
                 for t, k, c, bg in (("Present · paid", "ok", OK, OKS), ("Late · due soon", "warn", WARN, WARNS), ("Absent · overdue", "bad", BAD, BADS), ("Information", "info", BLUE, "#e8effd")))
    prop = [(64, "#ffffff", "White"), (18, PLATE, "Plate"), (10, INK, "Ink"), (6, BLUE, "Accent"), (1, CAMPUS, "Campus"), (1, OK, "Status")]
    bar = "".join(f'<div style="flex:{p};background:{c};height:56px;box-shadow:inset 0 0 0 1px rgba(11,12,20,.06)"></div>' for p, c, n in prop)
    leg = "".join(f'<span style="font:400 13px {SANS};color:{MUTED}">{n} {p}%</span>' for p, c, n in prop)
    col = lambda h, inner: f'<div style="flex:1"><div style="font:600 17px {SANS};margin-bottom:10px">{h}</div>{inner}</div>'
    body = (f'<div style="display:flex;gap:16px">{sw}</div>'
            f'<div style="font:600 17px {SANS};margin-top:56px">How much of each, on a page</div>'
            f'<div style="display:flex;border-radius:14px;overflow:hidden;margin-top:14px">{bar}</div><div style="display:flex;gap:22px;margin-top:10px">{leg}</div>'
            f'<div style="display:flex;gap:48px;margin-top:56px">{col("Greys", gs)}{col("In the drawing only", ds)}{col("Status, in data only", st)}</div>')
    return frame("Brand kit · 03", "Colour", "One accent. Violet marks the product.",
                 "Pages are white and plate grey with ink type. Blue is the one accent. Violet belongs to the product tile and the portal tags. Status colours appear only where the data means it.", body)


# ---- 04 type --------------------------------------------------------------------------------------
def bk_type():
    spec = (f'<div style="display:flex;gap:48px;align-items:flex-end"><span style="font:600 220px/0.8 {SANS};letter-spacing:-0.05em">Aa</span>'
            f'<div style="display:flex;flex-direction:column;gap:10px;padding-bottom:10px">'
            + "".join(f'<span style="font:{w_} 30px {SANS};letter-spacing:-0.02em">{n} {w_} · Form 3B register</span>' for n, w_ in (("Semibold", 600), ("Medium", 500), ("Regular", 400)))
            + f'<span style="font:400 16px {SANS};color:{MUTED};margin-top:6px">Atkinson Hyperlegible Next. Made for readers with low vision; every letter is distinct.</span></div></div>')
    scale = [("Display", 62, 600, "1.06", "-0.035em", "One system for the whole school."), ("Heading 1", 48, 600, "1.08", "-0.03em", "Four portals."),
             ("Heading 2", 38, 600, "1.12", "-0.025em", "Campus works without internet."), ("Heading 3", 24, 600, "1.25", "-0.015em", "Administration portal"),
             ("Lead", 19, 400, "1.6", "0", "Registers, marks and fees share one record."), ("Body", 17, 400, "1.6", "0", "Ms Sibanda marks Form 3B on the classroom tablet at 07:42."),
             ("Small", 15, 400, "1.5", "0", "Setup and training free."), ("Label", 13, 500, "1.3", "0", "Attendance today")]
    rows = "".join(f'<div style="display:grid;grid-template-columns:160px 150px 1fr;gap:20px;align-items:baseline;padding:16px 0;border-top:1px solid {LINE}">'
                   f'<span style="font:500 14px {SANS}">{n}</span><span style="font:400 12px {MONO};color:{MUTED}">{s_} / {lh} · {w_}</span>'
                   f'<span style="font:{w_} {s_}px/{lh} {SANS};letter-spacing:{ls};white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{t}</span></div>' for n, s_, w_, lh, ls, t in scale)
    two = (f'<div style="padding:36px;border-radius:24px;background:{PLATE}">{h2("Record a mark once.", "Everyone sees the same one.", 44)}'
           f'<div style="font:400 14px/1.5 {SANS};color:{MUTED};margin-top:18px">Two-tone headings: the claim in ink, the consequence in #9A9EA9.</div></div>')
    nums = (f'<div style="padding:36px;border-radius:24px;box-shadow:inset 0 0 0 1px {LINE}"><div style="font:600 56px/1 {SANS};letter-spacing:-0.03em;{NUM}">US$612,400</div>'
            f'<div style="display:flex;gap:18px;margin-top:22px;align-items:baseline"><span style="font:400 13px {MONO};color:{INK2}">R-2026-18824</span><span style="font:400 13px {MONO};color:{INK2}">M·02</span><span style="font:400 13px {MONO};color:{INK2}">07:42</span></div>'
            f'<div style="font:400 14px/1.5 {SANS};color:{MUTED};margin-top:18px">Figures use tabular numbers. IBM Plex Mono is for codes only: receipts, module numbers, times in tables.</div></div>')
    body = (f'{spec}<div style="margin-top:56px">{rows}</div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:48px">{two}{nums}</div>')
    return frame("Brand kit · 04", "Type", "One family, three weights.",
                 "Atkinson Hyperlegible Next is the only typeface, at 400, 500 and 600. Nothing is set above 600 and nothing in capitals.", body)


# ---- 05 photography -------------------------------------------------------------------------------
PHOTOS = [("boys-reading-2.jpg", "58% 40%", "Home hero", "Pupils at a boarding school, Form 3 age"), ("classroom-zambia.jpg", "center 40%", "Works without internet", "A classroom with a teacher at the front"),
          ("teacher-maths.jpg", "center 30%", "Academics and student life", "A teacher at the board"), ("mother-phone.jpg", "65% center", "Parents and guardians", "A parent at home, a pupil at the table"),
          ("girls-classroom.jpg", "center 35%", "Who we serve · day schools", "Pupils arriving in class"), ("seniors-lecture.jpg", "center 30%", "Who we serve · private schools", "Upper Sixth in a lecture")]


def bk_photo():
    grid = "".join(f'<div style="width:400px">{ph(n, 400, 280, pos, 24)}{cap(t, d)}</div>' for n, pos, t, d in PHOTOS)
    do1 = (f'<div style="position:relative;width:400px;height:300px"><div style="position:absolute;right:0;top:0">{ph("teacher-maths.jpg", 260, 300, "center 30%", 24)}</div>'
           + at(0, 56, marks_card(SB, 232), 2) + '</div>')
    dn1 = (f'<div style="position:relative;width:400px;height:300px">{ph("boys-reading-2.jpg", 400, 300, "58% 40%", 24)}'
           + at(150, 30, register_card(SB, 230, offline=False), 2) + '</div>')
    dn2 = (f'<div style="position:relative;width:400px;height:300px">{ph("classroom-uniforms.jpg", 400, 300, "center", 24)}'
           f'<div style="position:absolute;left:28px;top:90px;font:600 34px/1.1 {SANS};color:#fff;letter-spacing:-0.02em">Every pupil,<br>every term.</div></div>')
    dn3 = (f'<div style="position:relative;width:400px;height:300px;border-radius:24px;box-shadow:inset 0 0 0 1px {LINE};display:flex;align-items:center;gap:18px;padding:0 28px;box-sizing:border-box">'
           f'{ph("teacher-notebook.jpg", 120, 150, "center 25%", 60)}<div><div style="font:600 18px {SANS}">Your implementation lead</div>'
           f'<div style="font:400 14px {SANS};color:{MUTED};margin-top:4px">Corelith Labs, Harare</div></div></div>')
    dd = [(do1, True, "Cards overlap the photo's edge and leave faces clear"), (dn1, False, "Cards over faces"),
          (dn2, False, "Text set on a photo"), (dn3, False, "A stock person captioned as Corelith staff")]
    row = "".join(f'<div style="width:295px">{scaled(x, 295, 221, 295 / 400)}{dodont(o, t)}</div>' for x, o, t in dd)
    rules = [("Real schools", "Zimbabwean or regional schools, pupils in uniform. Licensed Pexels stock until Corelith photographs a school, then our own."),
             ("Crop to people", "Radius 24. Portrait 4:5 for single people, 3:2 or 16:10 for groups. Keep heads clear of the top edge."),
             ("Untouched", "No filters, duotones, overlays or text on the photo.")]
    rl = "".join(f'<div style="flex:1;padding-top:16px;border-top:2px solid {INK}"><div style="font:600 17px {SANS}">{t}</div><div style="font:400 15px/1.55 {SANS};color:{INK2};margin-top:8px">{d}</div></div>' for t, d in rules)
    body = (f'<div style="display:grid;grid-template-columns:repeat(3,400px);justify-content:space-between;row-gap:36px">{grid}</div>'
            f'<div style="display:flex;gap:40px;margin-top:64px">{rl}</div>'
            f'<div style="display:flex;justify-content:space-between;margin-top:56px">{row}</div>')
    return frame("Brand kit · 05", "Photography", "Real schools, pupils in uniform.",
                 "Campus is a platform for people, so people are photographed: pupils, teachers, a parent at home. Photographs lead the Home hero, Who we serve and the department pages.", body.replace("&quot;", '"'))


def bk_layout():
    import pages
    scale = [("Hero · 68 / 600", f'<div style="font:600 68px/1.03 {SANS};letter-spacing:-0.04em;max-width:1000px">A school management platform that puts people first.</div>'),
             ("Section · 52 / 600", f'<div style="font:600 52px/1.08 {SANS};letter-spacing:-0.034em">One system for the whole school.</div>'),
             ("Row · 42 / 600", f'<div style="font:600 42px/1.08 {SANS};letter-spacing:-0.034em">Keep working when the internet goes.</div>'),
             ("Tile · 28 / 600", f'<div style="font:600 28px/1.12 {SANS};letter-spacing:-0.025em">Academics and student life</div>'),
             ("Eyebrow · 15 / 500, blue", f'<div style="font:500 15px {SANS};color:{BLUE}">Single record</div>'),
             ("Body · 18–20 / 400", f'<div style="font:400 19px/1.6 {SANS};color:{INK2};max-width:720px">Each pupil, guardian and member of staff has one record. Admissions starts it, teachers add marks, the bursary adds payments, and the Head reads the same figures.</div>')]
    sc = "".join(f'<div style="display:flex;gap:40px;align-items:baseline;padding:22px 0;border-top:1px solid {LINE}"><span style="width:200px;flex:none;font:400 13px {MONO};color:{MUTED}">{k}</span>{v}</div>' for k, v in scale)
    rw = pages.row(*CP.ROWS[1], pages.pic_offline())
    rwt = tile(scaled(f'<div style="width:1200px;padding:40px 0;background:#fff">{rw}</div>', 820, 340, 820 / 1200), 820, 340)
    d0 = CP.DEPARTMENTS[0]
    dt = tile(f'<div style="padding:20px 0 0 20px">{scaled(pages.dept_tile(*d0), 284, 292, 284 / 389)}</div>', 420, 340, "#fff")
    rules = [("Words first", "Every section opens with an eyebrow, one headline and one paragraph. The picture follows and shows what the words say."),
             ("One claim per headline", "The headline makes one claim in the reader's words. The paragraph proves it with a name, a figure or a screen."),
             ("Eyebrows in sentence case", "Blue, 15px, never capitals: Single record, Works without internet, Moving to Campus."),
             ("People in photographs, places in drawings", "A photograph shows the people a section is about; the drawing shows the school, a department or what happens next; cards show the product.")]
    rl = "".join(f'<div style="padding:16px 0;border-top:1px solid {LINE}"><div style="font:600 16px {SANS}">{t}</div><div style="font:400 14.5px/1.55 {SANS};color:{INK2};margin-top:4px">{d}</div></div>' for t, d in rules)
    body = (sc + f'<div style="display:flex;gap:20px;margin-top:56px"><div>{rwt}{cap("A row", "Eyebrow, headline, paragraph; the picture at the same height, sides alternating down the page.")}</div>'
            f'<div>{dt}{cap("A department tile", "The name big, one line, the department drawn in the corner.")}</div></div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 60px;margin-top:56px">{rl}</div>')
    return frame("Brand kit · 10", "Type-led layout", "Headlines carry the page.",
                 "Campus reads like Veracross: big plain type, a department grid, rows of eyebrow, claim and proof. Under the type, photographs carry the people and the drawing carries the school.", body)


# ---- 06 illustration ------------------------------------------------------------------------------
def part(fn, w, h, U=40, ox=None, oy=None, label=None):
    """draw one isometric part alone in a w x h box"""
    I.U = U
    I.OX = ox if ox is not None else w * 0.42
    I.OY = oy if oy is not None else h * 0.34
    res = fn()
    svg = res[0] if isinstance(res, tuple) else res
    defs = '<defs><filter id="sh" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="3"/></filter></defs>'
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="display:block">{defs}{svg}</svg>'


PARTS = [("Classroom block", "Verandas on pillars, a door and window per room. Teacher portal.", lambda: ISO.classroom(0, 0, "Block C", 3.4), 44, 150, 70),
         ("Administration", "Two storeys, the bursary window on the side, the flag. Administration portal.", lambda: ISO.admin(0, 0), 44, 150, 90),
         ("Library", "Tall windows, a grey pitched roof. Student portal, e-library.", lambda: ISO.library(0, 0, 2.3), 48, 140, 70),
         ("Tsavo House", "The hostel: two floors of dormitory windows, a walkway. Boarding.", lambda: ISO.hostel(0, 0, "Tsavo House", 4.0), 38, 120, 90),
         ("Stores", "Roller door, sacks of mealie meal. Stock.", lambda: ISO.stores(0, 0, 2.2, 1.3), 52, 150, 70),
         ("The gate", "Name board, guard hut, the red and white boom.", lambda: ISO.gate(0, 1.2, 2.5), 50, 130, 60),
         ("The field", "Lines, goalposts, pupils at break.", lambda: ISO.field(0, 0, 4.2, 2.3) + "".join(ISO.kid(px, py, t) for px, py, t in ((1.2, 0.8, BLUE), (2.4, 1.4, "#6f7a8c"), (3.1, 0.9, "#8f98a8"))), 44, 120, 50),
         ("Trees and people", "Jacaranda, msasa green, pupils and parents at the scale of the doors.",
          lambda: ISO.jtree(0.6, 0.6, 1.0, ISO.JAC) + ISO.jtree(1.8, 1.1, 0.9, "green") + ISO.jtree(3.0, 0.5, 0.8, ISO.JAC) + ISO.person(3.9, 1.3, "#6f7a8c") + ISO.person(4.2, 1.5, BLUE) + ISO.kid(4.5, 1.2, "#8f98a8"), 50, 120, 70),
         ("The kombi", "At the gate at 16:30, with the Corelith mark on its side.", lambda: ISO.kombi(0, 0), 70, 110, 80)]


def bk_illustration():
    tiles = ""
    for n, d, fn, U, ox, oy in PARTS:
        svg = part(fn, 400, 250, U, ox, oy)
        tiles += f'<div style="width:400px">{tile(svg, 400, 250, GROUND)}{cap(n, d)}</div>'
    pill_demo = ISO.pills([("Teacher", ("Registers", "Marks"), 250, 140)], ic)
    label_box = (f'<div style="position:relative;width:560px;height:200px;{DOTS};border-radius:24px;box-shadow:inset 0 0 0 1px {LINE}">'
                 f'{pill_demo}'
                 f'<span style="position:absolute;left:262px;top:152px;font:400 12px {MONO};color:{MUTED}">dot on the building</span>'
                 f'<span style="position:absolute;left:340px;top:117px;font:400 12px {MONO};color:{MUTED}">22px stem</span></div>')
    lrules = [("Portal pill", "Blue icon tile and the portal's name, on a stem to the building where the portal is used."),
              ("Module chip", "Grey chip beside the portal pill, or on its own stem: Fees, Boarding, Stock."),
              ("Every label touches its object", "No floating labels. A stem ends in a dot on the roof or wall.")]
    lr = "".join(f'<div style="padding:14px 0;border-top:1px solid {LINE}"><div style="font:600 16px {SANS}">{t}</div><div style="font:400 14.5px/1.55 {SANS};color:{INK2};margin-top:4px">{d}</div></div>' for t, d in lrules)
    body = (f'<div style="display:grid;grid-template-columns:repeat(3,400px);justify-content:space-between;row-gap:36px">{tiles}</div>'
            f'<div style="display:flex;gap:60px;margin-top:64px;align-items:flex-start">{label_box}<div style="flex:1">{lr}</div></div>')
    return frame("Brand kit · 06", "Illustration", "The school as one campus.",
                 "The drawing uses the Corelith street's isometric parts, built as a school. Grey buildings, blue roofs on the classrooms, a few trees. Each part is drawn once here and reused on every page.", body)


# ---- 07 composition -------------------------------------------------------------------------------
def bk_composition():
    import pages
    W_ = lambda html, h: f'<div style="width:1440px;height:{h}px;overflow:hidden;background:#fff">{html}</div>'
    seq = [("Hero", "Type + photograph", W_(pages.hero(), 810)), ("Departments", "Type + the drawing", W_(pages.departments(), 810)),
           ("Works without internet", "Type + photograph", W_(pages.band(pages.row(*CP.ROWS[1], pages.pic_offline()), pad="160px 120px"), 810)),
           ("Who we serve", "Type + photographs", W_(pages.who(), 810)), ("Moving to Campus", "Type", W_(pages.switching(), 810)),
           ("Call to action", "Type + the drawing", _cta_drawing())]
    tag = lambda t: {"Type + the drawing": ("#efeaff", CAMPUS), "Type + cards": ("#eef0f3", INK2), "Type": ("#eef0f3", INK2),
                     "Type + photograph": ("#e8effd", BLUE), "Type + photographs": ("#e8effd", BLUE)}[t]
    items = ""
    for i, (n, t, html) in enumerate(seq):
        bg, c = tag(t)
        k_ = 400 / (1440 if "width:1440px" in html[:60] else 1280)
        items += (f'<div style="width:400px">{tile(scaled(html, 400, 225, k_), 400, 225)}'
                  f'<div style="display:flex;align-items:center;gap:10px;margin-top:14px"><span style="font:400 12px {MONO};color:{MUTED}">{i + 1:02d}</span>'
                  f'<span style="font:600 15px {SANS}">{n}</span><span style="flex:1"></span>'
                  f'<span style="height:24px;padding:0 10px;border-radius:12px;background:{bg};color:{c};font:500 12.5px {SANS};display:inline-flex;align-items:center">{t}</span></div></div>')
    rules = [("Type opens every section", "Then one picture: a photograph, the drawing or a plate of cards. Down a page they alternate."),
             ("People in photographs, places in drawings", "Cards may sit on a photo's edge or on the dotted plate, never on the drawing."),
             ("Every call to action is drawn", "Visit, Price or Training, each showing what happens next."),
             ("Same school everywhere", "Mukuvisi High, Tanaka Moyo, Form 3B and the same figures in every picture.")]
    rl = "".join(f'<div style="padding:16px 0;border-top:1px solid {LINE}"><div style="font:600 16px {SANS}">{t}</div><div style="font:400 14.5px/1.55 {SANS};color:{INK2};margin-top:4px">{d}</div></div>' for t, d in rules)
    body = (f'<div style="display:grid;grid-template-columns:repeat(3,400px);justify-content:space-between;row-gap:36px">{items}</div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 60px;margin-top:56px">{rl}</div>')
    return frame("Brand kit · 07", "Putting them together", "Home, section by section.",
                 "Type opens every section. Photographs show the people, the drawing shows the school and its departments and closes the page with the call to action, and cards show the product. Here is the order on Home.", body)


def _parents():
    return (f'<div style="position:relative;width:1280px;height:720px;background:#fff">'
            f'<div style="position:absolute;left:60px;top:40px">{ph("mother-phone.jpg", 820, 640, "65% center", 24)}</div>'
            + at(760, 120, week_card(SB, 400), 2) + at(700, 420, message_card(SB, 380), 3) + '</div>')


def _cta_drawing():
    import ds
    return f'<div style="width:1280px;height:720px;display:flex;align-items:center;background:#fff">{ds.cta_block("visit", w=1280)}</div>'


# ---- 08 applications ------------------------------------------------------------------------------
def social_photo():
    return (f'<div style="width:1080px;height:1080px;background:#fff;position:relative;font-family:{SANS}">'
            f'<div style="position:absolute;left:0;top:0">{ph("classroom-zambia.jpg", 1080, 640, "center 40%", 0)}</div>'
            + at(560, 330, register_card(SB, 440), 2)
            + f'<div style="position:absolute;left:72px;top:700px;width:560px"><div style="font:600 58px/1.05 {SANS};letter-spacing:-0.035em;text-wrap:balance">Campus works without internet.</div></div>'
              f'<div style="position:absolute;left:72px;bottom:64px;display:flex;align-items:center;justify-content:space-between;width:936px">{lockup(34)}'
              f'<span style="font:500 24px {SANS};color:{MUTED}">campus.corelith.co.zw</span></div></div>')


def social_iso():
    svg, labels = ISO.scene()
    sc = f'<div style="position:relative;width:1280px;height:720px">{svg}{ISO.pills(labels, ic)}</div>'
    return (f'<div style="width:1080px;height:1080px;{DOTS};position:relative;font-family:{SANS};overflow:hidden">'
            f'<div style="position:absolute;left:72px;top:72px"><div style="font:600 58px/1.05 {SANS};letter-spacing:-0.035em">Four portals.<br><span style="color:{FAINT}">One record behind them.</span></div></div>'
            f'<div style="position:absolute;left:-130px;top:250px;transform:scale(1.04);transform-origin:0 0">{sc}</div>'
            f'<div style="position:absolute;left:72px;bottom:64px;display:flex;align-items:center;justify-content:space-between;width:936px;padding:18px 24px;border-radius:20px;background:#fff;box-sizing:border-box">{lockup(30)}'
            f'<span style="font:500 22px {SANS};color:{INK2}">campus.corelith.co.zw</span></div></div>')


def email_header():
    I_ = part(lambda: ISO.classroom(0, 0, "Block A", 3.4), 300, 200, 30, 90, 60)
    return (f'<div style="width:1200px;height:400px;background:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 80px;box-sizing:border-box;font-family:{SANS};box-shadow:inset 0 -1px 0 {LINE}">'
            f'<div><div>{lockup(34)}</div><div style="font:600 48px/1.1 {SANS};letter-spacing:-0.03em;margin-top:36px">October at Campus</div>'
            f'<div style="font:400 22px {SANS};color:{MUTED};margin-top:10px">What changed this month, for Heads and bursars</div></div>'
            f'<div style="width:420px;height:300px;border-radius:24px;{DOTS};display:flex;align-items:center;justify-content:center">{scaled(I_, 420, 280, 1.4)}</div></div>')


def bk_applications():
    sq1 = tile(scaled(social_photo(), 630, 630, 630 / 1080), 630, 630)
    sq2 = tile(scaled(social_iso(), 630, 630, 630 / 1080), 630, 630)
    em = tile(scaled(email_header(), 1280, 427, 1280 / 1200), 1280, 427)
    body = (f'<div style="display:flex;gap:20px"><div>{sq1}{cap("Social post, 1080 × 1080", "A story led by a photograph: the photo on top, the words on white below it.")}</div>'
            f'<div>{sq2}{cap("Social post, 1080 × 1080", "The drawing, for posts about the portals and modules.")}</div></div>'
            f'<div style="margin-top:48px">{em}{cap("Email header, 1200 × 400", "Monthly note to schools. Single parts of the drawing work at small sizes.")}</div>')
    return frame("Brand kit · 08", "In use", "Posts and email.",
                 "Type, photographs, the drawing and cards, sized for social and email. Words never sit on a photo; they sit on white or on the dotted ground.", body)


BOARDS = [("BK01-cover", "01 · Cover", bk_cover), ("BK02-logo", "02 · Logo", bk_logo), ("BK03-colour", "03 · Colour", bk_colour), ("BK04-type", "04 · Type", bk_type),
          ("BK05-photography", "05 · Photography", bk_photo), ("BK06-illustration", "06 · Illustration", bk_illustration),
          ("BK07-composition", "07 · Putting them together", bk_composition), ("BK08-in-use", "08 · In use", bk_applications)]


# ---- 09 voice -------------------------------------------------------------------------------------
VOICE_RULES = [("Prove local fit with detail", "Say EcoCash, ZiG, Form 3B, exeat and the end-of-term report. Never write \"built for Zimbabwe\", \"local\" or \"homegrown\".",
                "Built for how Zimbabwean schools run.", "Fees in US dollars and ZiG, matched to each pupil."),
               ("Start from the school day", "Open with what happens at school, then say what Campus does about it.",
                "A unified platform for school operations.", "Campus works without internet."),
               ("One claim, one detail", "Follow each claim with something a Head can check in a demo: a name, a figure, a screen.",
                "Save hours every week.", "You record a mark once and it appears on the report."),
               ("Talk like a colleague", "Plain words and contractions. Speak to the person doing the job as \"you\"; \"we\" is Corelith.",
                "Empower your educators with seamless workflows.", "You enter each mark once."),
               ("Be exact about money", "The currency and both decimals, every time. Say what isn't charged.",
                "Affordable pricing for every school.", "US$1 per active pupil per month.")]
TONES = [("The Head", "calm, accountable", "Attendance, fees and open jobs are on one screen before assembly."),
         ("SDC and bursar", "exact", "1,140 active pupils × US$1 = US$1,140 a month. The first month is free."),
         ("Teachers", "time and fewer forms", "You record a mark once. It shows on the report and on the parent's phone."),
         ("Parents", "warm, about their child", "Tanaka was in school all week and scored 71% in Mathematics.")]
USE = ["internet", "Head", "pupil", "parent or guardian", "term", "Form 3B", "bursar", "exeat", "SDC", "register", "report", "portal", "department", "single record", "cloud-based", "active pupil", "EcoCash", "ZiG"]
AVOID = ["signal", "principal", "stakeholder", "our solution", "seamless", "empower", "unlock", "transform", "best-in-class", "cutting-edge",
         "AI-powered", "magic", "journey", "built for Zimbabwe", "homegrown"]
REFS = [("PowerSchool", "Opens each block on the reader's real problem, in short sentences.", "Power puns and stakeholder language."),
        ("Basecamp", "Plain, first person, with a view of its own.", "The jokes. A Head buying for 1,140 pupils wants calm."),
        ("Veracross", "\"A school management platform that puts people first.\" The department split; rows of eyebrow, claim and proof.", "Capitalised eyebrows; \"industry-leading\"."),
        ("iSAMS", "Cloud-based, one integrated record; migration and training named as services.", "Screenshot collages; four-colour tabs."),
        ("Seesaw", "A teacher's own words describe the benefit, once a school agrees.", "The \"most platforms do X, we do Y\" frame."),
        ("Zeraki, ClassDojo, Interfolio", "Zeraki names real fee tasks: receipts, pledges.", "Slogans, emoji, \"empowers\", \"best-in-class\".")]


def bk_voice():
    rows = ""
    for i, (t, d, no, yes) in enumerate(VOICE_RULES):
        rows += (f'<div style="display:grid;grid-template-columns:48px 360px 1fr 1fr;gap:28px;align-items:start;padding:24px 0;border-top:1px solid {LINE}">'
                 f'<span style="font:500 15px {SANS};color:{FAINT}">0{i + 1}</span>'
                 f'<div><div style="font:600 20px {SANS};letter-spacing:-0.01em">{t}</div><div style="font:400 15px/1.55 {SANS};color:{INK2};margin-top:8px">{d}</div></div>'
                 f'<div style="padding:18px 20px;border-radius:16px;background:{BADS}"><div style="display:flex;gap:6px;align-items:center;font:500 13px {SANS};color:{BAD}">{ic("close-circle", 14, BAD)}Not this</div>'
                 f'<div style="font:500 17px/1.4 {SANS};color:{INK2};margin-top:8px">{no}</div></div>'
                 f'<div style="padding:18px 20px;border-radius:16px;background:{OKS}"><div style="display:flex;gap:6px;align-items:center;font:500 13px {SANS};color:{OK}">{ic("check-circle", 14, OK)}This</div>'
                 f'<div style="font:600 17px/1.4 {SANS};color:{INK};margin-top:8px">{yes}</div></div></div>')
    tones = "".join(f'<div style="flex:1;padding:24px;border-radius:20px;box-shadow:inset 0 0 0 1px {LINE}"><div style="font:600 16px {SANS}">{r}</div>'
                    f'<div style="font:400 13.5px {SANS};color:{MUTED};margin-top:2px">{t}</div>'
                    f'<div style="font:500 17px/1.45 {SANS};color:{INK};margin-top:18px">{e}</div></div>' for r, t, e in TONES)
    heads = "".join(f'<div style="flex:1;padding:26px;border-radius:20px;background:{PLATE}">{h2(a, b, 28)}</div>' for a, b in (
        ("A school management platform that puts people first.", ""), ("One system for the whole school.", ""), ("Four portals.", "One record behind them.")))
    chip = lambda t, ok: (f'<span style="display:inline-flex;align-items:center;height:32px;padding:0 13px;border-radius:16px;font:500 14px {SANS};'
                          f'{"background:#fff;box-shadow:inset 0 0 0 1px " + LINE + ";color:" + INK if ok else "background:" + PLATE + ";color:" + MUTED + ";text-decoration:line-through"}">{t}</span>')
    use_chips = "".join(chip(w, True) for w in USE)
    avoid_chips = "".join(chip(w, False) for w in AVOID)
    words = (f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:48px"><div><div style="font:500 13px {SANS};color:{MUTED};margin-bottom:14px">Use</div><div style="display:flex;flex-wrap:wrap;gap:8px">{use_chips}</div></div>'
             f'<div><div style="font:500 13px {SANS};color:{MUTED};margin-bottom:14px">Avoid</div><div style="display:flex;flex-wrap:wrap;gap:8px">{avoid_chips}</div></div></div>')
    refs = (f'<div style="display:grid;grid-template-columns:240px 1fr 1fr;gap:20px;padding:0 0 10px;font:500 13px {SANS};color:{MUTED}"><span>Site</span><span>Take</span><span>Leave</span></div>'
            + "".join(f'<div style="display:grid;grid-template-columns:240px 1fr 1fr;gap:20px;padding:14px 0;border-top:1px solid {LINE};font:400 15px/1.5 {SANS};color:{INK2}">'
                      f'<span style="font-weight:600;color:{INK}">{s_}</span><span>{a}</span><span>{b}</span></div>' for s_, a, b in REFS))
    sub = lambda t: f'<div style="font:600 18px {SANS};margin:64px 0 20px">{t}</div>'
    body = (f'{rows}<div style="border-top:1px solid {LINE}"></div>'
            + sub("Tone by reader") + f'<div style="display:flex;gap:16px">{tones}</div>'
            + sub("Headlines: one claim, and a second line only when it adds a fact") + f'<div style="display:flex;gap:16px">{heads}</div>'
            + sub("Words") + words
            + sub("What we took from the reference sites") + refs)
    return frame("Brand kit · 09", "Voice", "A colleague from the school office.",
                 "Plain, calm, exact about money and specific about the school day. Campus shows it fits Zimbabwean schools through the detail it names, never by saying so.", body)


BOARDS.append(("BK09-voice", "09 · Voice", bk_voice))
BOARDS.append(("BK10-layout", "10 · Type-led layout", bk_layout))

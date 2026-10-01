# -*- coding: utf-8 -*-
"""Three whole landing pages, one per direction, from the same copy and world.
A: product-site template, centred, isometric campus, fragments on plates.
B: split hero, photographs with UI cards over them, pills.
C: editorial and numbered, documents as the objects, serif figures and mono labels."""
from common import *
from ui import *
import words as CP
import iso_campus as ISO

PAD = 120


def sec(inner, bg="#fff", pad="112px 120px", extra=""):
    return f'<section style="background:{bg};padding:{pad};box-sizing:border-box;{extra}">{inner}</section>'


def h2(a, b="", size=44, font=SANS, w=600, ls="-0.03em", centre=False, grey=True):
    al = "text-align:center;" if centre else ""
    tail = f'<br><span style="color:{FAINT if grey else INK}">{b}</span>' if b else ""
    return f'<h2 style="margin:0;font:{w} {size}px/1.1 {font};letter-spacing:{ls};color:{INK};text-wrap:balance;{al}">{a}{tail}</h2>'


def para(t, size=18, c=INK2, mw=560, centre=False):
    al = "text-align:center;margin-left:auto;margin-right:auto;" if centre else ""
    return f'<p style="margin:0;font:400 {size}px/1.6 {SANS};color:{c};max-width:{mw}px;{al}">{t}</p>'


def ticks(items, c=INK2, icon="check-circle", ic_c=BLUE, size=15.5):
    return "".join(f'<div style="display:flex;gap:10px;align-items:flex-start;font:400 {size}px/1.5 {SANS};color:{c};padding:5px 0">'
                   f'<span style="padding-top:3px">{ic(icon, 16, ic_c)}</span>{t}</div>' for t in items)


def navbar(kind="a"):
    links = "".join(f'<span style="display:inline-flex;align-items:center;gap:4px;font:500 15px {SANS};color:{INK2}">{t}{ic("down-line", 14, FAINT) if t in ("Solutions", "Who we serve", "Platform") else ""}</span>' for t in CP.NAV)
    r = 20 if kind == "b" else (8 if kind == "a" else 3)
    demo = btn(CP.HERO["cta"], "calendar", "primary", 40, 14.5).replace("border-radius:8px", f"border-radius:{r}px")
    return (f'<div style="height:76px;display:flex;align-items:center;gap:40px;padding:0 {PAD}px;border-bottom:1px solid {LINE if kind != "c" else INK};background:#fff">'
            f'{lockup(24)}<div style="display:flex;gap:30px;margin-left:16px">{links}</div><span style="flex:1"></span>'
            f'<span style="font:500 15px {SANS};color:{INK2}">Sign in</span>{demo}</div>')


def footer(kind="a"):
    cols = "".join(f'<div style="display:flex;flex-direction:column;gap:12px"><span style="font:600 14px {SANS};color:{INK}">{h}</span>'
                   + "".join(f'<span style="font:400 14px {SANS};color:{MUTED}">{x}</span>' for x in xs) + '</div>' for h, xs in CP.FOOT)
    return (f'<footer style="padding:72px {PAD}px 48px;border-top:1px solid {LINE if kind != "c" else INK};background:#fff">'
            f'<div style="display:flex;justify-content:space-between;gap:60px"><div style="display:flex;flex-direction:column;gap:18px;max-width:320px">{lockup(24, by=False)}'
            f'<span style="font:400 14px/1.6 {SANS};color:{MUTED}">{CP.FOOT_LINE}</span><span style="margin-top:6px">{logo(20, INK)}</span></div>'
            f'<div style="display:grid;grid-template-columns:repeat(4,150px);gap:36px">{cols}</div></div>'
            f'<div style="display:flex;justify-content:space-between;margin-top:56px;padding-top:22px;border-top:1px solid {LINE};font:400 13px {SANS};color:{MUTED}">'
            f'<span>© 2026 Corelith Labs</span><span>Harare, Zimbabwe</span></div></footer>')


def logo_row(kind="a", n=5):
    r = {"a": 12, "b": 999, "c": 2}[kind]
    boxes = "".join(dashed(196, 64, "School logo", r if r < 100 else 32) for _ in range(n))
    cap = f'<div style="font:{"400 13px " + MONO if kind == "c" else "500 14px " + SANS};color:{MUTED};text-align:center;margin-bottom:22px">{CP.LOGOS}</div>'
    return f'<div style="padding:56px {PAD}px">{cap}<div style="display:flex;justify-content:space-between">{boxes}</div></div>'


# ---- A: product-site template --------------------------------------------------------------------
SA = SIGS["a"]


def plate(inner, w, h, extra=""):
    return (f'<div style="position:relative;width:{w}px;height:{h}px;border-radius:20px;background:{PLATE} radial-gradient(#dfe2e8 1px,transparent 1.2px) 0 0/20px 20px;'
            f'box-shadow:inset 0 0 0 1px #eceef2;overflow:hidden;flex:none;{extra}">{inner}</div>')


def at(x, y, inner, z=1):
    return f'<div style="position:absolute;left:{x}px;top:{y}px;z-index:{z}">{inner}</div>'


def pic_a(k, w=560, h=480):
    if k == "register":
        inner = at(28, 34, register_card(SA, 292)) + at(332, 190, sync_card(SA, 204), 2)
    elif k == "record":
        inner = (at(30, 32, marks_card(SA, 250)) + at(300, 52, report_card(SA, 230), 2)
                 + at(56, 290, head_card(SA, 252), 3) + at(356, 262, phone(SA, _mini_parent(SA), 150, 176), 3))
    elif k == "fees":
        inner = at(40, 40, fee_card(SA, 320)) + at(286, 226, receipts_card(SA, 240), 2)
    else:
        inner = at(48, 14, parent_screen(SA, 220)) + at(312, 150, message_card(SA, 218), 2)
    return plate(inner, w, h)


def _mini_parent(S):
    return (f'<div style="padding:30px 12px 10px;font-family:{S["font"]}"><div style="font:600 11px {S["font"]}">Tanaka · this week</div>'
            f'<div style="margin-top:8px;font-size:10px;color:{MUTED}">Mathematics test 2</div><div style="margin-top:2px">{fig(S, "71%", 18)}</div>'
            f'<div style="margin-top:6px;font-size:10px;color:{MUTED}">Class average 64%</div></div>')


def receipts_card(S, w=240):
    return card(S, chead(S, "bill", "Receipts", "Today", OK)
                + rowl(S, "EcoCash · 9", "US$3,410.00", top=False) + rowl(S, "Bank · 2", "US$1,410.00") + rowl(S, "Cash · 1", "ZiG 2,600.00")
                + f'<div style="margin-top:8px">{status(S, "Matched to pupils", "ok")}</div>', w)


def message_card(S, w=220):
    return card(S, chead(S, "message-3", "Ms Sibanda", "16:10", BLUE)
                + f'<div style="font-size:13px;line-height:1.5;color:{INK2}">Tanaka did well on test 2. Keep up the algebra practice at home.</div>'
                + f'<div style="margin-top:10px;display:flex;justify-content:flex-end">{status(S, "Reply", "info")}</div>', w)


def landing_a():
    H = CP.HERO
    svg, labels = ISO.scene(1200, 676, 42, 600, 372)
    hero = (f'<div style="padding:88px {PAD}px 0;text-align:center">'
            f'<div style="display:inline-flex;align-items:center;gap:8px;height:30px;padding:0 12px 0 6px;border-radius:15px;background:#fff;box-shadow:0 0 0 1px {LINE};font:500 13.5px {SANS};color:{INK2}">'
            f'{pmark("Campus", 18, 5)}Opens with Corelith 1.0 on 1 October{ic("right-line", 13, MUTED)}</div>'
            f'<h1 style="margin:24px auto 0;font:600 62px/1.06 {SANS};letter-spacing:-0.035em;max-width:1200px">{H["h1a"]}</h1>'
            f'<div style="margin-top:24px">{para(H["body"], 19, INK2, 720, True)}</div>'
            f'<div style="display:flex;gap:18px;justify-content:center;align-items:center;margin-top:32px">{btn(H["cta"], "calendar", "primary", 50, 16)}{link(H["cta2"], INK, 16)}</div>'
            f'<div style="margin-top:16px;font:400 14px {SANS};color:{MUTED}">{H["note"]}</div>'
            f'<div style="position:relative;width:1200px;height:676px;margin:24px auto 0;text-align:left">{svg}{ISO.pills(labels, ic)}</div></div>')
    # portals feature block: four tiles
    tiles = "".join(f'<div style="background:#fff;border-radius:16px;box-shadow:0 0 0 1px {LINE};padding:26px;display:flex;flex-direction:column;gap:14px">'
                    f'<span style="width:40px;height:40px;border-radius:10px;background:#e8effd;display:flex;align-items:center;justify-content:center">{ic(i, 20, BLUE)}</span>'
                    f'<div><div style="font:600 19px {SANS}">{n} portal</div><div style="font:400 14px {SANS};color:{MUTED};margin-top:4px">{w_}</div></div>'
                    f'<div style="font:400 15px/1.55 {SANS};color:{INK2}">{d}</div><span style="flex:1"></span>{link("See the " + n.lower() + " portal", INK, 14.5)}</div>'
                    for n, i, w_, d in PORTALS)
    mods = "".join(f'<span style="display:inline-flex;align-items:center;gap:8px;height:36px;padding:0 14px 0 10px;border-radius:10px;background:#fff;box-shadow:0 0 0 1px {LINE};font:500 14px {SANS};color:{INK2}">'
                   f'{ic(i, 16, MUTED)}<span style="font:400 12px {MONO};color:{FAINT}">{c}</span>{n}</span>' for c, n, i in MODULES)
    portals = sec(f'<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:60px">{h2(*CP.PORTALS_H)}{para(CP.PORTALS_B, 17, INK2, 470)}</div>'
                  f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-top:48px">{tiles}</div>'
                  f'<div style="display:flex;flex-wrap:wrap;gap:10px;margin-top:22px;align-items:center"><span style="font:500 14px {SANS};color:{MUTED};margin-right:6px">Eight modules underneath</span>{mods}</div>',
                  PLATE)
    # four stories, alternating
    st = ""
    for i, s in enumerate(CP.STORIES):
        text = (f'<div style="width:500px;display:flex;flex-direction:column;gap:20px">'
                f'<span style="display:inline-flex;align-self:flex-start;align-items:center;gap:6px;height:26px;padding:0 10px;border-radius:13px;background:#efeaff;font:500 13px {SANS};color:{CAMPUS}">{s["tag"]}</span>'
                f'{h2(s["h"], "", 38)}{para(s["b"], 17, INK2, 500)}<div>{ticks(s["pts"])}</div></div>')
        pic = pic_a(s["k"])
        row = f'{text}{pic}' if i % 2 == 0 else f'{pic}{text}'
        st += f'<div style="display:flex;justify-content:space-between;align-items:center;padding:56px 0;{"border-top:1px solid " + LINE if i else ""}">{row}</div>'
    stories = sec(st, "#fff", "64px 120px")
    figs = "".join(f'<div style="padding:28px;border-radius:16px;background:#fff;box-shadow:0 0 0 1px {LINE}"><div style="font:600 44px/1 {SANS};letter-spacing:-0.03em">{v}</div>'
                   f'<div style="font:500 16px {SANS};margin-top:12px">{t}</div><div style="font:400 14px {SANS};color:{MUTED};margin-top:4px">{d}</div></div>' for v, t, d in CP.FIGURES)
    comm = "".join(f'<div style="display:flex;gap:14px"><span style="width:36px;height:36px;border-radius:9px;background:#fff;box-shadow:0 0 0 1px {LINE};display:flex;align-items:center;justify-content:center;flex:none">{ic(i, 18, BLUE)}</span>'
                   f'<div><div style="font:600 16px {SANS}">{t}</div><div style="font:400 14.5px/1.55 {SANS};color:{INK2};margin-top:4px">{d}</div></div></div>' for i, t, d in COMMIT)
    band = sec(f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px">{figs}</div>'
               f'<div style="margin-top:88px">{h2("What the school can count on.", "", 40)}</div>'
               f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:40px 48px;margin-top:44px">{comm}</div>', PLATE)
    pricing = sec(pricing_block("a"), "#fff")
    cta = sec(f'<div style="border-radius:24px;background:{PLATE};box-shadow:inset 0 0 0 1px #eceef2;padding:72px;text-align:center">'
              f'{h2(CP.CTA["h"], "", 44, centre=True)}<div style="margin-top:18px">{para(CP.CTA["b"], 18, INK2, 620, True)}</div>'
              f'<div style="display:flex;gap:14px;justify-content:center;margin-top:30px">{btn(CP.CTA["cta"], "calendar", "primary", 50, 16)}{btn(CP.CTA["cta2"], "download-2", "ghost", 50, 16)}</div></div>',
              "#fff", "24px 120px 112px")
    return navbar("a") + hero + logo_row("a") + portals + stories + band + pricing + cta + footer("a")


def pricing_block(kind):
    P_ = CP.PRICING
    r = {"a": 18, "b": 24, "c": 3}[kind]
    fnum = f"600 56px/1 {SANS}" if kind != "c" else f"500 64px/1 {SERIF}"

    def plan(p, primary):
        bd = f"box-shadow:0 0 0 2px {BLUE};" if primary and kind != "c" else (f"box-shadow:0 0 0 1px {LINE};" if kind != "c" else f"border-top:2px solid {INK};")
        return (f'<div style="flex:1;background:#fff;border-radius:{r}px;{bd}padding:34px;display:flex;flex-direction:column;gap:18px">'
                f'<div style="display:flex;justify-content:space-between;align-items:center"><span style="font:600 18px {SANS}">{p["name"]}</span>'
                f'{status(SIGS[kind], "Current offer", "info") if primary else ""}</div>'
                f'<div><span style="font:{fnum};letter-spacing:-0.03em">{p["price"]}</span><div style="font:400 15px {SANS};color:{MUTED};margin-top:10px">{p["per"]}</div></div>'
                f'<div style="border-top:1px solid {LINE};padding-top:12px">{ticks(p["items"], INK2, "check-circle", BLUE if kind != "c" else INK, 15)}</div><span style="flex:1"></span>'
                f'{btn("Book a demo", "calendar", "primary" if primary else "ghost", 46, 15).replace("border-radius:8px", "border-radius:" + str(min(r, 23)) + "px")}</div>')
    ex = P_["example"]
    tl = "".join(f'<div style="flex:1;padding-top:14px;border-top:3px solid {BLUE if i < 2 else LINE}"><div style="font:{"500 13px " + SANS if kind != "c" else "400 12px " + MONO};color:{MUTED}">{a}</div>'
                 f'<div style="font:600 16px {SANS};margin-top:6px">{b}</div><div style="font:400 14px {SANS};color:{INK2};margin-top:2px">{c}</div></div>' for i, (a, b, c) in enumerate(P_["timeline"]))
    side = (f'<div style="width:360px;display:flex;flex-direction:column;gap:16px">'
            f'<div style="background:{PLATE if kind != "c" else "#fff"};border-radius:{r}px;padding:28px;{"border:1px solid " + INK if kind == "c" else ""}">'
            f'<div style="font:500 14px {SANS};color:{MUTED}">Worked example</div><div style="font:600 17px {SANS};margin-top:10px">{ex["t"]}</div>'
            f'<div style="font:{fnum};font-size:44px;letter-spacing:-0.03em;margin-top:14px">{ex["v"]}</div><div style="font:400 15px/1.5 {SANS};color:{INK2};margin-top:8px">{ex["s"]}</div>'
            f'<div style="margin-top:18px;padding-top:16px;border-top:1px solid {LINE};display:flex;justify-content:space-between;font:400 14px {SANS};color:{MUTED}"><span>Holidays</span><span style="color:{INK};font-weight:500">US$0</span></div>'
            f'<div style="margin-top:14px">{link("Work out your school", INK, 14.5)}</div></div></div>')
    return (f'<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:60px">{h2(P_["h"], "", 44)}{para(P_["b"], 17, INK2, 440)}</div>'
            f'<div style="display:flex;gap:16px;margin-top:48px;align-items:stretch">{plan(P_["main"], True)}{plan(P_["lms"], False)}{side}</div>'
            f'<div style="margin-top:48px;display:flex;gap:18px;align-items:flex-start"><div style="width:240px;font:600 17px {SANS}">From signing to running</div>{tl}</div>')


# ---- B: photographs with UI cards over them --------------------------------------------------------
SB = SIGS["b"]


def pill(t, c=INK2, bg="#fff", icon=None, h=32, size=14):
    return (f'<span style="align-self:flex-start;display:inline-flex;align-items:center;gap:7px;height:{h}px;padding:0 14px {"" if not icon else ""};border-radius:{h // 2}px;background:{bg};'
            f'box-shadow:0 0 0 1px {LINE};font:500 {size}px {SANS};color:{c};white-space:nowrap">{ic(icon, 15, c) if icon else ""}{t}</span>')


def rbtn(label, icon, kind="primary", h=50, size=16):
    return btn(label, icon, kind, h, size).replace("border-radius:8px", f"border-radius:{h // 2}px")


def ph(n, w, h, pos="center", r=24):
    return photo(n, w, h, pos, r)


def week_card(S, w=262):
    return card(S, chead(S, "home-3", "Tanaka · this week", "Fri", CAMPUS)
                + rowl(S, "Present", "5 of 5 days", top=False) + rowl(S, "Mathematics test 2", "71%") + rowl(S, "Balance, due 16 Oct", "US$420.00", WARN), w)


def same_card(S, w=300):
    tags = "".join(status(S, t, "mute") for t in ("Term report", "Rudo's phone", "Head's view", "Tanaka's portal"))
    return card(S, chead(S, "check-circle", "The same 71% in four places", "", OK) + f'<div style="display:flex;flex-wrap:wrap;gap:6px">{tags}</div>', w)


def pic_b(k, w=600, h=460):
    if k == "register":
        return (f'<div style="position:relative;width:{w}px;height:{h}px;flex:none">{ph("classroom-zambia.jpg", w - 90, h, "center 40%")}'
                + at(w - 300, 40, register_card(SB, 300), 2) + '</div>')
    if k == "record":
        return (f'<div style="position:relative;width:{w}px;height:{h}px;flex:none"><div style="position:absolute;right:0;top:0">{ph("teacher-maths.jpg", 330, h, "center 30%")}</div>'
                + at(0, 36, marks_card(SB, 290), 2) + at(30, 280, same_card(SB, 300), 3) + '</div>')
    if k == "fees":
        return (f'<div style="position:relative;width:{w}px;height:{h}px;flex:none;border-radius:24px;background:{PLATE}">'
                + at(20, 28, fee_card(SB, 292), 2) + at(300, 150, receipts_card(SB, 214), 3) + '</div>')
    return (f'<div style="position:relative;width:{w}px;height:{h}px;flex:none">{ph("mother-phone.jpg", w - 110, h, "65% center")}'
            + at(w - 262, 36, week_card(SB, 262), 2) + at(w - 300, 236, message_card(SB, 250), 3) + '</div>')


def landing_b():
    H = CP.HERO
    hero_pic = (f'<div style="position:relative;width:640px;height:600px;flex:none">'
                f'<div style="position:absolute;right:0;top:0">{ph("boys-reading-2.jpg", 560, 600, "58% center", 28)}</div>'
                + at(0, 300, register_card(SB, 290, offline=False), 2)
                + at(380, 36, card(SB, f'{lab(SB, "Attendance today")}<div style="margin-top:8px">{fig(SB, "96.4%", 30)}</div><div style="margin-top:8px">{status(SB, "1,099 of 1,140", "ok")}</div>', pad=18), 2)
                + at(330, 470, card(SB, f'<div style="display:flex;align-items:center;gap:10px">{ic("message-3", 18, BLUE)}<span style="font:500 14px {SANS}">Tanaka scored 71% in test 2</span></div>', pad=14), 3)
                + '</div>')
    hero = (f'<div style="display:flex;align-items:center;justify-content:space-between;padding:72px {PAD}px 40px;gap:40px">'
            f'<div style="width:540px;display:flex;flex-direction:column;gap:24px">{pill("Opens with Corelith 1.0 on 1 October", CAMPUS, "#f6f3ff", "calendar")}'
            f'<h1 style="margin:0;font:600 58px/1.06 {SANS};letter-spacing:-0.035em">{H["h1a"]}</h1>'
            f'{para(H["body"], 18.5, INK2, 520)}'
            f'<div style="display:flex;gap:14px;align-items:center">{rbtn(H["cta"], "calendar")}{rbtn(H["cta2"], "right-line", "ghost")}</div>'
            f'<div style="display:flex;gap:8px;flex-wrap:wrap">{pill("Setup free", INK2, "#fff", "check-circle", 30, 13.5)}{pill("First month free", INK2, "#fff", "check-circle", 30, 13.5)}{pill("US$1 per active pupil per month", INK2, "#fff", "check-circle", 30, 13.5)}</div></div>'
            f'{hero_pic}</div>')
    # feature block: the product itself, framed, with portal pills above
    tabs = "".join(f'<span style="display:inline-flex;align-items:center;gap:8px;height:42px;padding:0 18px 0 14px;border-radius:21px;'
                   f'{"background:" + INK + ";color:#fff" if i == 0 else "background:#fff;color:" + INK2 + ";box-shadow:0 0 0 1px " + LINE};font:500 15px {SANS}">'
                   f'{ic(ic_, 16, "#fff" if i == 0 else MUTED)}{n}</span>' for i, (n, ic_, w_, d) in enumerate(PORTALS))
    shot = f'<div style="transform:scale(0.9);transform-origin:top left;width:1280px;height:800px">{head_view(SB)}</div>'
    feat = sec(f'<div style="text-align:center">{h2(*CP.PORTALS_H, centre=True)}<div style="margin-top:18px">{para(CP.PORTALS_B, 18, INK2, 640, True)}</div>'
               f'<div style="display:flex;gap:10px;justify-content:center;margin-top:32px">{tabs}</div></div>'
               f'<div style="margin:40px auto 0;width:1200px;height:760px;border-radius:32px;background:#e9ecf1;padding:24px;box-sizing:border-box;overflow:hidden">{shot}</div>',
               PLATE, "104px 120px")
    # stories: a 2 x 2 grid of cards, picture on top, text below
    cards = ""
    for s in CP.STORIES:
        cards += (f'<div style="background:#fff;border-radius:28px;box-shadow:0 0 0 1px {LINE};padding:28px;display:flex;flex-direction:column;gap:22px">'
                  f'{pic_b(s["k"], 532, 402)}<div style="display:flex;flex-direction:column;gap:14px;padding:0 6px 6px">'
                  f'<div style="display:flex">{status(SB, s["tag"], "campus")}</div>{h2(s["h"], "", 30)}{para(s["b"], 16.5, INK2, 520)}</div></div>')
    stories = sec(f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px">{cards}</div>', "#fff", "104px 120px")
    figs = "".join(f'<div style="flex:1;padding:26px 28px;border-radius:24px;background:#fff">{fig(SB, v, 40)}<div style="font:500 16px {SANS};margin-top:12px">{t}</div>'
                   f'<div style="font:400 14px {SANS};color:{MUTED};margin-top:4px">{d}</div></div>' for v, t, d in CP.FIGURES)
    comm = "".join(f'<div style="background:#fff;border-radius:24px;padding:26px;display:flex;flex-direction:column;gap:14px">'
                   f'<span style="width:44px;height:44px;border-radius:22px;background:#e8effd;display:flex;align-items:center;justify-content:center">{ic(i, 20, BLUE)}</span>'
                   f'<div style="font:600 17px {SANS}">{t}</div><div style="font:400 15px/1.55 {SANS};color:{INK2}">{d}</div></div>' for i, t, d in COMMIT)
    band = sec(f'<div style="display:flex;gap:16px">{figs}</div><div style="margin-top:80px;text-align:center">{h2("What the school can count on.", "", 42, centre=True)}</div>'
               f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:40px">{comm}</div>', PLATE, "96px 120px")
    pricing = sec(pricing_block("b"), "#fff")
    cta = sec(f'<div style="display:flex;align-items:center;gap:56px;border-radius:32px;background:{PLATE};padding:28px 28px 28px 64px">'
              f'<div style="flex:1;display:flex;flex-direction:column;gap:18px">{h2(CP.CTA["h"], "", 44)}{para(CP.CTA["b"], 18, INK2, 520)}'
              f'<div style="display:flex;gap:12px;margin-top:8px">{rbtn(CP.CTA["cta"], "calendar")}{rbtn(CP.CTA["cta2"], "download-2", "ghost")}</div></div>'
              f'{ph("boys-laptop.jpg", 460, 420, "30% center", 24)}</div>', "#fff", "0 120px 104px")
    return navbar("b") + hero + logo_row("b") + feat + stories + band + pricing + cta + footer("b")


# ---- C: documents, numbered, serif figures ---------------------------------------------------------
SC_ = SIGS["c"]
RULE = "#e3e6eb"


def mono(t, c=MUTED, size=12):
    return f'<span style="font:400 {size}px {MONO};color:{c}">{t}</span>'


def paper(inner, w, extra=""):
    return (f'<div style="width:{w}px;box-sizing:border-box;background:#fff;box-shadow:0 0 0 1px #dfe2e8,0 24px 50px -32px rgba(11,12,20,.35);'
            f'padding:32px 34px;font-family:{SANS};color:{INK};{extra}">{inner}</div>')


REPORT_ROWS = [("Mathematics", 71, 64, "Strong in algebra; practise geometry.", "NS"), ("English", 68, 61, "Reads widely; essays need planning.", "TC"),
               ("Combined Science", 74, 66, "Careful in practicals.", "KM"), ("Geography", 62, 59, "Map work improving.", "RM"),
               ("Shona", 80, 72, "Excellent oral work.", "FN"), ("History", 66, 63, "Good use of sources.", "AD")]


def report_doc(w=600):
    """Tanaka's Term 3 report: every line is written by one portal. Returns (html, row_y) where row_y maps a key to its y in px."""
    RH = 36
    head = (f'<div style="display:flex;align-items:center;gap:14px;padding-bottom:18px;border-bottom:1px solid {INK}">'
            f'<span style="width:44px;height:44px;border-radius:22px;border:1px solid {INK};display:flex;align-items:center;justify-content:center;font:500 15px {SERIF}">MH</span>'
            f'<div style="flex:1"><div style="font:500 20px {SERIF}">{SCHOOL}</div>{mono("Harare · Term 3 report · 2026")}</div>{mono("Page 1 of 1")}</div>')
    det = (f'<div style="display:grid;grid-template-columns:1.3fr 1fr 1fr;gap:10px;padding:14px 0;border-bottom:1px solid {RULE}">'
           + "".join(f'<div>{mono(a, MUTED, 11)}<div style="font:500 14.5px {SANS};margin-top:4px">{b}</div></div>' for a, b in (("Pupil", "Tanaka Moyo"), ("Form", "3B · Tsavo House"), ("Admission", "2024-0387")))
           + '</div>')
    th = (f'<div style="display:grid;grid-template-columns:150px 54px 60px 1fr;gap:10px;height:30px;align-items:end;padding-bottom:6px;border-bottom:1px solid {RULE}">'
          + "".join(mono(t, MUTED, 11) for t in ("Subject", "Mark", "Class", "Comment")) + '</div>')
    rows = "".join(f'<div style="display:grid;grid-template-columns:150px 54px 60px 1fr;gap:10px;height:{RH}px;align-items:center;border-bottom:1px solid {RULE};font-size:13.5px">'
                   f'<span>{s}</span><span style="font:500 17px {SERIF};{NUM}">{m}</span><span style="font:400 15px {SERIF};color:{MUTED};{NUM}">{a}</span>'
                   f'<span style="color:{INK2};font-size:12.5px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{c}</span></div>' for s, m, a, c, t in REPORT_ROWS)
    att = (f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;padding:14px 0;border-bottom:1px solid {RULE}">'
           f'<div>{mono("Attendance, term 3", MUTED, 11)}<div style="font:500 17px {SERIF};margin-top:4px">97% · 2 days absent</div></div>'
           f'<div>{mono("Fees, term 3", MUTED, 11)}<div style="font:500 17px {SERIF};margin-top:4px">US$420.00 due 16 Oct</div></div></div>')
    headr = (f'<div style="padding:14px 0 0">{mono("The Head", MUTED, 11)}<div style="font:italic 400 15px/1.5 {SERIF};margin-top:4px;color:{INK2}">A steady term with real progress in Mathematics. Well done, Tanaka.</div>'
             f'<div style="display:flex;justify-content:space-between;align-items:flex-end;margin-top:10px"><span style="font:400 13px {SANS};color:{MUTED}">Mrs Chipo Mutasa, Head</span>{mono("Closes Thu 3 Dec")}</div></div>')
    html = paper(head + det + th + rows + att + headr, w)
    # y positions (from the paper's top) for the annotations
    y0 = 32 + 64 + 1 + 70 + 30
    ys = {"pupil": 32 + 64 + 36, "marks": y0 + RH * 0.5, "att": y0 + RH * 6 + 34, "fees": y0 + RH * 6 + 34, "head": y0 + RH * 6 + 70 + 34}
    return html, ys


def notes(items, x0, w=250):
    """annotations: (y, label, text); each a mono label, a sentence, and a dotted leader back to the document"""
    out = ""
    for y, lbl, t in items:
        out += (f'<div style="position:absolute;left:{x0 - 64}px;top:{y:.0f}px;width:56px;border-top:1px dashed #9aa1ad"></div>'
                f'<div style="position:absolute;left:{x0 - 68}px;top:{y - 3:.0f}px;width:7px;height:7px;background:{INK}"></div>'
                f'<div style="position:absolute;left:{x0}px;top:{y - 10:.0f}px;width:{w}px">{mono(lbl, BLUE, 12)}'
                f'<div style="font:400 14px/1.5 {SANS};color:{INK2};margin-top:4px">{t}</div></div>')
    return out


def report_object(w=1200, h=700, doc_w=580, left=0):
    doc, ys = report_doc(doc_w)
    x0 = left + doc_w + 72
    items = [(ys["pupil"], "Student portal", "Tanaka sees this report, and each mark the day it is entered."),
             (ys["marks"] + 10, "Teacher portal", "Each subject teacher records a mark once. Ms Sibanda recorded hers on 24 September."),
             (ys["att"] + 10, "Administration portal", "Attendance from the daily register. The balance from the bursary."),
             (ys["head"] + 20, "Parent portal", "Sent to Rudo Moyo's phone the day the term closes.")]
    return (f'<div style="position:relative;width:{w}px;height:{h}px"><div style="position:absolute;left:{left}px;top:0">{doc}</div>'
            f'{notes(items, x0, w - x0 - 10)}</div>')


def reg_sheet(w=520):
    rows = "".join(f'<div style="display:grid;grid-template-columns:28px 1fr 32px;gap:10px;height:32px;align-items:center;border-bottom:1px solid {RULE};font-size:13.5px">'
                   f'{mono(f"{i + 1:02d}", FAINT, 11)}<span>{n}</span><span style="font:500 13px {MONO};color:{ {"P": OK, "A": BAD, "L": WARN}[m] }">{m}</span></div>' for i, (n, m) in enumerate(FORM3B[:7]))
    inner = (f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding-bottom:12px;border-bottom:1px solid {INK}">'
             f'<span style="font:500 20px {SERIF}">Form 3B register</span>{mono("Wed 30 Sep · 07:42")}</div>'
             f'<div style="display:flex;align-items:center;gap:8px;margin:12px 0;font:400 12px {MONO};color:{WARN}"><i style="width:7px;height:7px;background:{WARN}"></i>No internet · saved on this tablet</div>'
             f'{rows}<div style="display:flex;justify-content:space-between;padding-top:12px">{mono("36 P · 1 L · 1 A · 38 on roll")}'
             f'<span style="font:400 12px {MONO};color:{OK}">■ synced 08:05</span></div>')
    return paper(inner, w)


def statement_doc(w=520):
    inner = (f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding-bottom:12px;border-bottom:1px solid {INK}">'
             f'<span style="font:500 20px {SERIF}">Fee statement · Term 3</span>{mono("INV-T3-0387")}</div>'
             f'<div style="padding:10px 0;font:400 13.5px {SANS};color:{INK2}">Tanaka Moyo · Form 3B · boarder</div>'
             + "".join(f'<div style="display:grid;grid-template-columns:70px 1fr 120px;gap:10px;height:36px;align-items:center;border-top:1px solid {RULE};font-size:13.5px">'
                       f'{mono(d)}<span>{t}</span><span style="text-align:right;font:500 16px {SERIF};{NUM};color:{c}">{v}</span></div>'
                       for d, t, v, c in (("08 Sep", "Term fee, boarding", "US$1,250.00", INK), ("14 Sep", "EcoCash · R-2026-18511", "−US$500.00", OK),
                                          ("22 Sep", "Bank transfer · R-2026-18824", "−US$330.00", OK)))
             + f'<div style="display:grid;grid-template-columns:70px 1fr 120px;gap:10px;height:44px;align-items:center;border-top:1px solid {INK}">'
               f'<span></span><span style="font:500 14px {SANS}">Balance due Friday 16 October</span><span style="text-align:right;font:500 20px {SERIF}">US$420.00</span></div>'
               f'<div style="margin-top:12px;padding-top:12px;border-top:1px dashed {RULE};display:flex;justify-content:space-between">{mono("Bursary receipts today")}{mono("US$4,820.00 · ZiG 2,600.00", INK)}</div>')
    return paper(inner, w)


def sms(w=320):
    bub = lambda t, me=False: (f'<div style="align-self:{"flex-end" if me else "flex-start"};max-width:78%;padding:10px 12px;border-radius:3px;'
                               f'background:{"#e8effd" if me else PLATE};font:400 13.5px/1.45 {SANS};color:{INK}">{t}</div>')
    inner = (f'<div style="padding:44px 16px 16px;display:flex;flex-direction:column;gap:10px">'
             f'<div style="text-align:center">{mono("Mukuvisi High School · Campus")}</div>'
             + bub("Tanaka was present all five days this week. Mathematics test 2: 71% (class average 64%).")
             + bub("Term 3 balance US$420.00, due Friday 16 October. Pay by EcoCash or at the bursary.")
             + bub("Thank you. I'll pay on Friday.", True)
             + bub("Ms Sibanda: Tanaka did well. Please keep up the algebra practice at home.") + '</div>')
    return phone(SC_, inner, w, round(w * 1.72))


def pic_c(k):
    if k == "register":
        return f'<div style="position:relative;width:560px;height:440px">{at(20, 0, reg_sheet(500))}</div>'
    if k == "record":
        spokes = [("Teacher portal", "enters the mark"), ("Parent portal", "sees it that evening"), ("Student portal", "sees it the same day"), ("Administration portal", "the Head's view")]
        rows = "".join(f'<div style="display:grid;grid-template-columns:24px 1fr 1fr;gap:12px;height:62px;align-items:center;border-bottom:1px solid {RULE}">'
                       f'{mono(f"P{i + 1}", FAINT)}<span style="font:500 15px {SANS}">{a}</span><span style="font:400 14px {SANS};color:{MUTED}">{b}</span></div>' for i, (a, b) in enumerate(spokes))
        inner = (f'<div style="padding:22px 24px;border:1px solid {INK};display:flex;justify-content:space-between;align-items:baseline">'
                 f'<div>{mono("One record · 2024-0387")}<div style="font:500 22px {SERIF};margin-top:6px">Tanaka Moyo · Mathematics test 2</div></div>'
                 f'<span style="font:500 44px {SERIF}">71%</span></div><div style="margin-left:40px;border-left:1px solid {INK};padding-left:24px">{rows}</div>')
        return f'<div style="width:560px">{inner}</div>'
    if k == "fees":
        return f'<div style="position:relative;width:560px;height:440px">{at(20, 0, statement_doc(520))}</div>'
    return f'<div style="position:relative;width:560px;height:620px;display:flex;justify-content:center">{sms(300)}</div>'


def landing_c():
    H = CP.HERO
    hero = (f'<div style="padding:72px {PAD}px 40px">'
            f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding-bottom:14px;border-bottom:1px solid {INK}">'
            f'{mono("Corelith Campus · school management for Zimbabwe", INK)}{mono("Opens with Corelith 1.0 · Thursday 1 October 2026")}</div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:64px;margin-top:48px">'
            f'<h1 style="margin:0;font:500 76px/1.02 {SERIF};letter-spacing:-0.02em">{H["h1a"]}</h1>'
            f'<div style="display:flex;flex-direction:column;gap:24px;padding-top:12px">{para(H["body"], 19, INK2, 520)}'
            f'<div style="display:flex;gap:18px;align-items:center">{btn(H["cta"], "calendar", "primary", 50, 16).replace("border-radius:8px", "border-radius:3px")}{link(H["cta2"], INK, 16)}</div>'
            f'{mono(H["note"])}</div></div>'
            f'<div style="margin-top:64px;padding-top:40px;border-top:1px solid {RULE}">{report_object(1200, 700, 600, 0)}</div></div>')
    # feature block: the portals as a contents page, modules as an index
    prt = "".join(f'<div style="padding:22px 0;border-top:1px solid {INK if i == 0 else RULE};display:grid;grid-template-columns:60px 260px 1fr;gap:20px;align-items:baseline">'
                  f'{mono(f"P{i + 1}", MUTED, 13)}<div><div style="font:500 26px {SERIF}">{n} portal</div>{mono(w_)}</div>'
                  f'<div style="font:400 16px/1.55 {SANS};color:{INK2}">{d}</div></div>' for i, (n, ic_, w_, d) in enumerate(PORTALS))
    idx = "".join(f'<div style="display:flex;justify-content:space-between;align-items:baseline;padding:12px 0;border-bottom:1px solid {RULE}">'
                  f'<span style="font:400 16px {SANS}">{n}</span>{mono(c)}</div>' for c, n, i in MODULES)
    feat = sec(f'<div style="display:grid;grid-template-columns:1fr 340px;gap:80px"><div>{h2(CP.PORTALS_H[0] + " " + CP.PORTALS_H[1], "", 48, SERIF, 500, "-0.015em")}'
               f'<div style="margin:18px 0 36px">{para(CP.PORTALS_B, 17, INK2, 600)}</div>{prt}</div>'
               f'<div style="padding-top:8px">{mono("Modules", INK)}<div style="margin-top:14px;border-top:1px solid {INK}">{idx}</div>'
               f'<div style="margin-top:18px;font:400 14px/1.55 {SANS};color:{MUTED}">The Head\'s view sits above all eight.</div></div></div>', "#fff", "96px 120px")
    st = ""
    for i, s in enumerate(CP.STORIES):
        text = (f'<div style="width:520px;display:flex;flex-direction:column;gap:18px">'
                f'<div style="display:flex;gap:14px;align-items:baseline"><span style="font:500 56px/1 {SERIF};color:{BLUE}">{s["n"]}</span>{mono(s["tag"])}</div>'
                f'{h2(s["h"], "", 38, SERIF, 500, "-0.01em")}{para(s["b"], 17, INK2, 520)}'
                + "".join(f'<div style="display:flex;gap:12px;padding:10px 0;border-top:1px solid {RULE};font:400 15px {SANS};color:{INK2}">{mono("—", FAINT)}{p}</div>' for p in s["pts"])
                + '</div>')
        st += (f'<div style="display:flex;justify-content:space-between;align-items:flex-start;padding:72px 0;border-top:1px solid {INK if i == 0 else RULE}">'
               f'{text}{pic_c(s["k"])}</div>')
    stories = sec(st, "#fff", "24px 120px 40px")
    figs = "".join(f'<div style="padding:26px 24px 0 0;border-top:1px solid {INK}"><div style="font:500 60px/1 {SERIF};letter-spacing:-0.01em">{v}</div>'
                   f'<div style="font:500 16px {SANS};margin-top:14px">{t}</div><div style="margin-top:4px">{mono(d)}</div></div>' for v, t, d in CP.FIGURES)
    comm = "".join(f'<div style="display:grid;grid-template-columns:44px 1fr;gap:10px;padding:20px 0;border-top:1px solid {RULE}">{mono(f"{i + 1:02d}", MUTED, 13)}'
                   f'<div><div style="font:500 20px {SERIF}">{t}</div><div style="font:400 15px/1.55 {SANS};color:{INK2};margin-top:6px">{d}</div></div></div>' for i, (ic_, t, d) in enumerate(COMMIT))
    band = sec(f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px">{figs}</div>'
               f'<div style="display:grid;grid-template-columns:360px 1fr;gap:80px;margin-top:96px">{h2("What the school can count on.", "", 40, SERIF, 500, "-0.01em")}'
               f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 48px">{comm}</div></div>', PLATE, "96px 120px")
    pricing = sec(pricing_block("c").replace(f"font:600 44px/1.1 {SANS};letter-spacing:-0.03em", f"font:500 44px/1.1 {SERIF};letter-spacing:-0.01em"), "#fff")
    cta = sec(f'<div style="border-top:1px solid {INK};padding-top:48px;display:grid;grid-template-columns:1fr 1fr;gap:64px;align-items:end">'
              f'{h2(CP.CTA["h"], "", 60, SERIF, 500, "-0.02em")}<div style="display:flex;flex-direction:column;gap:22px">{para(CP.CTA["b"], 18, INK2, 520)}'
              f'<div style="display:flex;gap:12px">{btn(CP.CTA["cta"], "calendar", "primary", 50, 16).replace("border-radius:8px", "border-radius:3px")}'
              f'{btn(CP.CTA["cta2"], "download-2", "ghost", 50, 16).replace("border-radius:8px", "border-radius:3px")}</div></div></div>', "#fff", "40px 120px 104px")
    return navbar("c") + hero + logo_row("c") + feat + stories + band + pricing + cta + footer("c")

# -*- coding: utf-8 -*-
"""The website at phone width (390). Same copy, same cards, same photographs as the desktop boards, laid out the
way a phone reads: one column, text first, then one picture; cards at their own size over the photo's lower edge,
never shrunk. Sections 96px apart. Every desktop page has its phone board beside it on the canvas."""
from ds import *
import pages as PG
import site_words as SW
import site_cards as SC
import hero as HR
import webpages as WP
import dept_art, portal_art, cta_art, nav_icons
import campus_mark

MW = 390
MX = 20                 # side gutter
CW = MW - 2 * MX        # 350, the content column
MGAP = 96


# ---- frame ---------------------------------------------------------------------------------------------
def mpage(secs):
    return f'<div style="width:{MW}px;background:#fff;font-family:{SANS};color:{INK};overflow:hidden">{"".join(secs)}</div>'


def gap(h=MGAP):
    return f'<div style="height:{h}px"></div>'


def pad(inner, p=f"0 {MX}px"):
    return f'<div style="padding:{p}">{inner}</div>'


def nav():
    return (f'<div style="height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 {MX}px;border-bottom:1px solid {LINE};background:#fff">'
            f'{lockup(20, by=False)}<span style="display:flex;gap:10px;align-items:center">{cbtn("Demo", "calendar", size="sm")}'
            f'<span style="width:40px;height:40px;border-radius:20px;box-shadow:inset 0 0 0 1px {LINE};display:flex;align-items:center;justify-content:center">{campus_mark.menu_icon(20)}</span></span></div>')


def eyebrow(t, key=None):
    lead = nav_icons.nav_icon(key, 26) if key else ""
    return f'<div style="display:flex;align-items:center;gap:8px;font:500 14px {SANS};color:{BLUE}">{lead}{t}</div>'


def h1(t):
    return f'<h1 style="margin:0;font:600 36px/1.08 {SANS};letter-spacing:-0.035em;text-wrap:balance">{t}</h1>'


def h2(t, size=30):
    return f'<h2 style="margin:0;font:600 {size}px/1.12 {SANS};letter-spacing:-0.03em;text-wrap:balance">{t}</h2>'


def p(t, size=16.5, c=INK2):
    return f'<p style="margin:0;font:400 {size}px/1.55 {SANS};color:{c}">{t}</p>'


def btn_full(label, icon="calendar", kind="primary"):
    return f'<div style="display:flex">{cbtn(label, icon, kind, "lg").replace("display:inline-flex", "display:flex;flex:1;justify-content:center", 1)}</div>'


def head(eye, key, h, mb=28):
    return f'<div style="display:flex;flex-direction:column;gap:12px;margin-bottom:{mb}px">{eyebrow(eye, key)}{h2(h)}</div>'


def scale_to(html, w, h, tw=CW):
    """a desktop picture fitted to the phone column"""
    k = tw / w
    return scaled(html, tw, round(h * k), k)


# ---- pictures ----------------------------------------------------------------------------------------
def tcard(name, w=310, **kw):
    return WP.tcard(name, w=w, **kw)


def photo_card(photo, pos, card_html=None, h=240):
    """the phone's photo story: the photograph, then a card over its lower edge at the card's own size"""
    out = ph(photo, CW, h, pos, 20)
    if card_html:
        out += f'<div style="margin:-64px 12px 0;position:relative;z-index:2">{card_html}</div>'
    return f'<div>{out}</div>'


def plate_card(card_html, art=None):
    a = f'<div style="display:flex;justify-content:flex-end;margin:-30px -20px -10px 0">{dept_art.art(art, 300, 200, U=40)}</div>' if art else ""
    return (f'<div style="border-radius:24px;{DOTS};box-shadow:inset 0 0 0 1px #eceef2;padding:24px 20px {0 if art else 24}px;overflow:hidden;display:flex;flex-direction:column;align-items:center">'
            f'<div style="position:relative;z-index:2">{card_html}</div>{a}</div>')


def pic_of(spec):
    kind = spec[0]
    if kind == "plate":
        n = spec[1][0][0]
        return plate_card(tcard(n), spec[2])
    if kind == "photo":
        return photo_card(spec[1], spec[2], tcard(spec[3][0][0]))
    if kind == "integrations":
        return scale_to(PG.pic_integrations(620, 420), 620, 420)
    if kind == "phone":
        return phone_on(PG.parent_phone(0.6), "mother-phone.jpg", "65% center")
    raise ValueError(kind)


def phone_on(phone_html, photo, pos, h=520):
    """a phone mock standing over a photograph, centred"""
    return (f'<div style="position:relative;width:{CW}px;height:{h}px;border-radius:24px;overflow:hidden">'
            f'<div style="position:absolute;inset:0">{ph(photo, CW, h, pos, 24)}</div>'
            f'<div style="position:absolute;left:0;right:0;top:24px;display:flex;justify-content:center">{phone_html}</div></div>')


# ---- sections ------------------------------------------------------------------------------------------
def hero(eye, key, h, b, pic="", buttons=None):
    buttons = buttons if buttons is not None else btn_full("Book a demo")
    return (f'<section style="padding:36px {MX}px 0;display:flex;flex-direction:column;gap:18px">{eyebrow(eye, key) if eye else ""}{h1(h)}{p(b, 17)}'
            f'{buttons}{f"<div style=margin-top:14px>{pic}</div>" if pic else ""}</section>')


def row(eye, key, h, b, pic):
    return pad(f'<div style="display:flex;flex-direction:column;gap:14px">{eyebrow(eye, key)}{h2(h)}{p(b)}<div style="margin-top:14px">{pic}</div></div>')


def rows(items):
    return "".join((gap() if i else "") + row(*it) for i, it in enumerate(items))


def band(eye, key, h, b, photo, pos):
    return (f'<section style="background:{PLATE};padding:64px {MX}px;display:flex;flex-direction:column;gap:14px">{eyebrow(eye, key)}{h2(h)}{p(b)}'
            f'<div style="margin-top:14px">{ph(photo, CW, 240, pos, 20)}</div></section>')


def dtile(n, sl, d, p_, k):
    return (f'<div style="position:relative;height:264px;border-radius:22px;background:{PLATE};overflow:hidden;padding:24px 22px 0;box-sizing:border-box">'
            f'<div style="font:600 24px/1.15 {SANS};letter-spacing:-0.02em;max-width:280px;text-wrap:balance">{n}</div>'
            f'<div style="font:400 14.5px/1.5 {SANS};color:{INK2};margin-top:8px;max-width:290px">{d}</div>'
            f'<div style="position:absolute;left:22px;bottom:22px">{PG.explore()}</div>'
            f'<div style="position:absolute;right:-30px;bottom:-34px">{dept_art.art(k, 236, 160, U=30)}</div></div>')


def tiles(slugs):
    return '<div style="display:flex;flex-direction:column;gap:14px">' + "".join(dtile(*WP.DEPT[s]) for s in slugs) + '</div>'


def tools(title, items):
    t = "".join(f'<div style="display:flex;align-items:center;gap:10px;padding:13px 0;border-top:1px solid {LINE};font:500 15.5px {SANS}">{ic("check-circle", 16, BLUE)}{x}</div>' for x in items)
    return pad(head("Features", "included", title, 18) + t)


def faq(eye, key, h, qa):
    qs = "".join(f'<div style="padding:18px 0;border-top:1px solid {LINE}"><div style="display:flex;justify-content:space-between;gap:12px;font:600 16.5px/1.35 {SANS}">{q}'
                 f'{ic("up-line" if i == 0 else "down-line", 18, MUTED)}</div>'
                 + (f'<div style="font:400 15px/1.6 {SANS};color:{INK2};margin-top:8px">{a}</div>' if i == 0 else "") + '</div>' for i, (q, a) in enumerate(qa))
    return pad(head(eye, key, h, 14) + qs + f'<div style="border-top:1px solid {LINE}"></div>')


def cta(kind="visit"):
    h_, b_, btns = CTAS[kind]
    second = btns[1] if len(btns) > 1 else None
    return pad(f'<div style="border-radius:24px;background:{PLATE};padding:12px 12px 26px">'
               f'<div style="border-radius:18px;overflow:hidden;{DOTS};box-shadow:inset 0 0 0 1px #e3e6eb">{scaled(cta_art.cta_scene(kind, 560, 420, 40, 280, 250), 326, 245, 326 / 560)}</div>'
               f'<div style="padding:20px 10px 0;display:flex;flex-direction:column;gap:14px">{h2(h_, 28)}{p(b_, 16)}{btn_full(btns[0][0], btns[0][1])}'
               + (btn_full(second[0], second[1], "secondary") if second else "") + '</div></div>')


def footer():
    types = "".join(f'<div style="flex:none;width:150px"><div style="position:relative;width:150px;height:110px">{ph(PG.TYPE_PHOTO[k][0], 150, 110, PG.TYPE_PHOTO[k][1], 14)}'
                    f'<div style="position:absolute;left:8px;bottom:8px;border-radius:9px;box-shadow:0 6px 14px -8px rgba(11,12,20,.5)">{nav_icons.nav_icon(k, 30)}</div></div>'
                    f'<div style="font:600 14.5px {SANS};margin-top:10px">{n}</div></div>' for n, k, d in CP.SCHOOL_TYPES)
    who = (f'<div style="padding:48px 0 40px {MX}px;border-top:1px solid {LINE}">{eyebrow("Who we serve · K-12", "who")}'
           f'<div style="display:flex;gap:12px;margin-top:20px;overflow:hidden">{types}</div></div>')
    cols = "".join(f'<div style="display:flex;flex-direction:column;gap:11px"><span style="font:600 14px {SANS}">{h}</span>'
                   + "".join(f'<span style="font:400 14px {SANS};color:{MUTED}">{x}</span>' for x in xs) + '</div>' for h, xs in CP.FOOT)
    foot = (f'<footer style="padding:40px {MX}px 36px;border-top:1px solid {LINE}">{lockup(22, by=False)}'
            f'<div style="font:400 14px/1.6 {SANS};color:{MUTED};margin-top:14px">{CP.FOOT_LINE}</div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:32px 20px;margin-top:32px">{cols}</div>'
            f'<div style="display:flex;justify-content:space-between;margin-top:36px;padding-top:18px;border-top:1px solid {LINE};font:400 13px {SANS};color:{MUTED}">'
            f'<span>© 2026 Corelith Labs</span><span>Harare, Zimbabwe</span></div></footer>')
    return who + foot


def end(kind="visit"):
    return [gap() + cta(kind) + gap(), footer()]


# ---- page templates --------------------------------------------------------------------------------------
def dept(slug):
    n, sl, d, p_, k = WP.DEPT[slug]
    D = SW.DEPTS[slug]
    photo, pos, a, b = D["hero"]
    top = nav() + hero(n, slug, D["h"], D["b"], photo_card(photo, pos, tcard(a)))
    bh, bb, bp, bpos = D["band"]
    return [top, gap() + band("One record", "record", bh, bb, bp, bpos), gap() + rows([(e, key, h_, b_, pic_of(sp)) for e, key, h_, b_, sp in D["rows"]]),
            gap() + tools(SW.DEPT_TOOLS_H, D["tools"])] + end()


def academics():
    from ui import register_card, marks_card
    A = CP.ACADEMICS
    top = nav() + hero(A["eyebrow"], "academics", A["h"], A["b"], photo_card("teacher-maths.jpg", "center 30%", HR.tagged("Teacher portal", register_card(SB, 310, offline=True))))
    bh, bb = A["band"]
    import mark_anim
    pics = [photo_card("classroom-zambia.jpg", "center 40%", HR.tagged("Teacher portal", register_card(SB, 310, offline=True))),
            scale_to(mark_anim.mark_journey(620, 460), 620, 460),
            plate_card(scale_to(PG.timetable_card(540), 540, 470, 310)),
            phone_on(PG.parent_phone(0.6), "mother-phone.jpg", "65% center")]
    rws = rows([(e, PG.ROW_ICON.get(e), h_, b_, pc) for (e, h_, b_), pc in zip(A["rows"], pics)])
    return [top, gap() + band("One record", "record", bh, bb, "girls-classroom.jpg", "center 35%"), gap() + rws, gap() + tools(A["tools_h"], A["tools"])] + end()


def type_page(key):
    import who_sections as WS
    T = SW.TYPES[key]
    photo, pos, a, b = T["hero"]
    top = nav() + hero(T["name"], key, T["h"], T["b"], photo_card(photo, pos, tcard(a)))
    secs = [gap() + s for s in TYPE_M[key]()]
    depts = pad(head("Departments", "solutions", SW.TYPE_DEPTS_H) + tiles(T["depts"]))
    return [top] + secs + [gap() + depts] + end()


def role(slug):
    R = SW.ROLE_PAGES[slug]
    photo, pos, a, b = R["hero"]
    eye = (f'<div style="display:flex;align-items:center;gap:8px;font:500 14px {SANS};color:{BLUE}">{portal_art.portal_icon(R["portal"], 26)}{R["name"]}'
           f'<span style="color:{FAINT}">·</span><span style="color:{INK2}">{R["portal"]} portal</span></div>')
    top = nav() + hero("", None, R["h"], R["b"], photo_card(photo, pos, tcard(a))).replace('gap:18px">', f'gap:18px">{eye}', 1)
    rws = rows([(e, k, h_, b_, pic_of(sp)) for e, k, h_, b_, sp in R["rows"]])
    depts = pad(head("Departments", "solutions", SW.ROLE_DEPTS_H) + tiles(R["depts"]))
    return [top, gap() + rws, gap() + depts] + end()


# ---- the bespoke Who we serve sections, at phone width ------------------------------------------------------
def m_day():
    import who_sections as WS
    steps = [("06:50", "On the bus"), ("07:30", "Register"), ("08:06", "Absences home"), ("12:40", "Marks in"), ("16:10", "Home time")]
    chips = "".join(f'<span style="flex:none;display:inline-flex;flex-direction:column;gap:2px;padding:10px 14px;border-radius:14px;'
                    f'{"background:" + INK + ";color:#fff" if i == 1 else "background:" + PLATE + ";color:" + INK2}">'
                    f'<b style="font:500 12px {MONO};color:{"#bfd3fb" if i == 1 else BLUE}">{t}</b><span style="font:600 14.5px {SANS}">{h}</span></span>' for i, (t, h) in enumerate(steps))
    day = pad(head("The school day", "t-day", "From the bus stop to home time, on one record.", 20)
              + f'<div style="display:flex;gap:8px;overflow:hidden;margin-right:-{MX}px">{chips}</div>'
              + f'<div style="margin-top:18px">{p("Ms Sibanda marks Form 3B on a tablet before the first lesson, with or without internet. The office sees it by 08:05.")}</div>'
              + f'<div style="margin-top:22px">{photo_card("teacher-tablet.jpg", "center 25%", HR.tagged("Teacher portal", WS.SC_card("register_card", 310)))}</div>')
    fam = row("Fees by family", "fees", "One statement for every family.",
              "Brothers and sisters bill to one family account, with the sibling discount applied. Parents pay once, by EcoCash or at the bursary, and the payment lands on each child's account.",
              photo_card("child-doorway.jpg", "center 30%", HR.tagged("Parent portal", WS.family_card(326))))
    lv = ""
    for ph_, pos, t, d, pts in [("ecd-class.jpg", "center 40%", "ECD to Grade 7", "The class teacher marks one register and writes the report comment for each child.",
                                 ["Class registers", "A class teacher's comment on every report", "Parents of the youngest see each day"]),
                                ("exam-blue.jpg", "center 40%", "Form 1 to Upper Sixth", "You mark registers by lesson, enter marks by subject, and every subject teacher adds a line to the report.",
                                 ["Registers by lesson", "Mark sheets by subject", "Exam classes in the holidays"])]:
        lv += (f'<div style="border-radius:22px;background:{PLATE};overflow:hidden">{ph(ph_, CW, 200, pos, 0)}<div style="padding:20px 22px 24px">'
               f'<div style="font:600 22px/1.15 {SANS};letter-spacing:-0.02em">{t}</div><div style="font:400 15px/1.55 {SANS};color:{INK2};margin-top:8px">{d}</div>'
               f'<div style="margin-top:12px">{ticks(pts, INK2, size=14.5)}</div></div></div>')
    levels = pad(head("Primary and secondary", "academics", "Run ECD and Upper Sixth from the same record.") + f'<div style="display:flex;flex-direction:column;gap:14px">{lv}</div>')
    return [day, gap() + fam, gap() + levels]


def m_boarding():
    import who_sections as WS
    rc = row("Roll call", "boarding", "Take roll call on your phone, house by house.",
             "Open your house at prep or lights out and tap each boarder in. Exeats and the sick bay are already marked, and anyone missing comes to the top. It works without internet.",
             phone_on(WS.rollcall_phone(0.6), "girls-smiling.jpg", "center 35%", 560))
    steps = [("1", "The guardian asks", "From the Parent portal, with who is collecting.", HR.tagged("Parent portal", WS.request_card(300))),
             ("2", "The housemaster approves", "The guardian and the fee account are checked on the record.", HR.tagged("Administration portal", WS.approve_card(300))),
             ("3", "Signed out", "The boarder leaves the house list until they are back.", HR.tagged("Administration portal", WS.signout_card(300)))]
    st = "".join(f'<div style="display:flex;gap:14px;{"padding-top:26px" if i else ""}"><div style="display:flex;flex-direction:column;align-items:center">'
                 f'<span style="width:30px;height:30px;border-radius:15px;background:{BLUE};color:#fff;display:flex;align-items:center;justify-content:center;font:600 14px {SANS};flex:none">{n}</span>'
                 + (f'<span style="flex:1;width:1.5px;background:#c3c9d3;margin-top:6px"></span>' if i < 2 else "") +
                 f'</div><div style="flex:1;padding-bottom:4px"><div style="font:600 18px {SANS}">{t}</div><div style="font:400 14.5px/1.5 {SANS};color:{INK2};margin-top:4px">{d}</div>'
                 f'<div style="margin-top:14px">{c}</div></div></div>' for i, (n, t, d, c) in enumerate(steps))
    exeat = f'<section style="background:{PLATE};padding:64px {MX}px">{head("Exeats", "sent", "An exeat in three steps, and nobody unaccounted for.")}{st}</section>'
    fees = row("Boarding fees", "fees", "Boarding and tuition on one account.",
               "Boarding, tuck and outings bill to the family's account with tuition, in US dollars and ZiG. Guardians pay by EcoCash or bank transfer and see the balance in the portal.",
               photo_card("boys-reading-2.jpg", "47% 42%", HR.tagged("Parent portal", WS.SC_card("fee_card", 320))))
    return [rc, gap() + exeat, gap() + fees]


def m_government():
    import who_sections as WS
    tile = lambda t, d, c: (f'<div style="border-radius:22px;background:{PLATE};padding:24px 20px 24px;display:flex;flex-direction:column;gap:10px">'
                            f'<div style="font:600 22px/1.15 {SANS};letter-spacing:-0.02em">{t}</div><div style="font:400 15px/1.55 {SANS};color:{INK2}">{d}</div>'
                            f'<div style="margin-top:12px">{c}</div></div>')
    split = pad(head("Staff", "hr-payroll", "Who pays whom, kept straight.") + '<div style="display:flex;flex-direction:column;gap:14px">'
                + tile("Teachers the government pays", "Their contracts, postings, leave and timetables live on Campus. Their pay does not.", HR.tagged("Administration portal", WS.gov_staff_card(310)))
                + tile("Staff your SDC employs", "Groundsmen, security, the office, the kitchen and any extra teachers are paid through Campus payroll.", HR.tagged("Administration portal", WS.sdc_payrun_card(310)))
                + '</div>')
    big = row("Big classes", "academics", "A register for 52 pupils in under a minute.",
              "Mark everyone present, then tap the three who are not. It saves on the phone without internet and reaches the office when the connection returns.",
              photo_card("class-desks.jpg", "center 40%", HR.tagged("Teacher portal", WS.bigclass_card(310))))
    levy = row("Fees and levies", "fees", "Bill tuition and levies the way your SDC sets them.",
               "Tuition, building and sports levies by form, in US dollars or ZiG. Every payment gets a receipt, and the SDC sees what has come in against what was billed.",
               plate_card(HR.tagged("Parent portal", SC.levy_card(300))))
    return [split, gap() + big, gap() + levy]


def m_private():
    import who_sections as WS
    stages = [("Enquiries", 214), ("School tours", 176), ("Applications", 168), ("Entrance test", 142), ("Offers", 132), ("Accepted", 96)]
    bars = "".join(f'<div style="padding:6px 0"><div style="font:500 13.5px {SANS};color:{INK2};margin-bottom:5px">{n}</div>'
                   f'<span style="display:block;height:30px;border-radius:9px;background:#e7ebf1;position:relative;overflow:hidden">'
                   f'<i style="position:absolute;left:0;top:0;bottom:0;width:{v / 214 * 100:.1f}%;background:{BLUE if n == "Accepted" else "#8fb0f6"};border-radius:9px"></i>'
                   f'<b style="position:absolute;left:12px;top:0;bottom:0;display:flex;align-items:center;font:600 13.5px {SANS};color:#fff;{NUM}">{v}</b></span></div>' for n, v in stages)
    funnel = (f'<section style="background:{PLATE};padding:64px {MX}px">{head("Admissions", "admissions", "Fill 120 places from one list.", 20)}{bars}'
              f'<div style="display:flex;gap:8px;margin-top:14px">{status(SB, "24 places left", "info")}{status(SB, "Deposits due 30 Oct", "warn")}</div>'
              f'<div style="margin-top:24px;display:flex;justify-content:center">{HR.tagged("Administration portal", SC.application_card(320))}</div></section>')
    board = row("The board", "insights", "Take the board a report it can read in five minutes.",
                "Enrolment, fees, results and staffing for the term, from the records the school already keeps. Download it as a PDF for the meeting.",
                photo_card("seniors-lecture.jpg", "center 30%", HR.tagged("Administration portal", WS.board_card(320))))
    phone = row("Parent portal", "Parent", "A portal for every family.",
                "Attendance, marks, fees and reports reach each family's phone that week, with a line to the class teacher.",
                phone_on(PG.parent_phone(0.6), "mother-phone.jpg", "65% center", 560))
    return [funnel, gap() + board, gap() + phone]


def m_mission():
    import who_sections as WS
    reg = row("Day and boarding", "t-mission", "Day scholars and boarders on one register.",
              "One class register shows who goes home and who boards. Boarders also appear on their house's roll call, and fees bill by the type of place.",
              plate_card(HR.tagged("Teacher portal", WS.mixed_register_card(310))))
    auth = row("Responsible authority", "insights", "The report your church asks for, without retyping.",
               "Enrolment, results, finance and staffing for the responsible authority, built from the records the school keeps every day.",
               f'<div style="position:relative">{ph("girls-desks.jpg", CW, 220, "center 35%", 20)}<div style="margin:-80px 10px 0;position:relative">{WS.authority_doc(330)}</div></div>')
    return [reg, gap() + auth]


TYPE_M = {"t-day": m_day, "t-boarding": m_boarding, "t-government": m_government, "t-private": m_private, "t-mission": m_mission}


# ---- unique pages ----------------------------------------------------------------------------------------
def home():
    H = CP.HERO
    import mark_anim
    tick = "".join(f'<div style="display:flex;align-items:center;gap:8px;font:500 14.5px {SANS};color:{INK2}">{ic("check-circle", 15, OK)}{t}</div>'
                   for t in ("Setup and training free", "First month free", "US$1 per active pupil per month"))
    pic = photo_card("boys-reading-2.jpg", "58% 40%", HR.tagged("Teacher portal", __import__("ui").register_card(SB, 310, offline=True)), 250)
    top = nav() + hero("", None, H["h1a"], H["body_phone"], pic, btn_full(H["cta"]) + f'<div style="display:flex;flex-direction:column;gap:6px">{tick}</div>')
    a, b = CP.DEPTS_H
    depts = pad(head("Solutions", "solutions", a) + tiles([d[1] for d in CP.DEPARTMENTS]))
    h_, b_ = CP.FOCUS
    focus = pad(f'<div style="border-radius:24px;background:{PLATE};padding:12px 12px 26px"><div style="border-radius:18px;overflow:hidden">{scale_to(PG.schools_plate(), 600, 420, 326)}</div>'
                f'<div style="padding:20px 10px 0;display:flex;flex-direction:column;gap:14px">{eyebrow("Who we serve · K-12", "who")}{h2(h_, 28)}{p(b_, 16)}'
                f'{btn_full("Book a demo")}{btn_full("See who we serve", "arrow-right-line", "secondary")}</div></div>')
    pics = [scale_to(mark_anim.mark_journey(620, 460), 620, 460), photo_card("classroom-zambia.jpg", "center 40%", HR.tagged("Teacher portal", __import__("ui").register_card(SB, 310, offline=True))),
            scale_to(PG.pic_integrations(620, 420), 620, 420), scale_to(PG.pic_training(620, 420), 620, 420), scale_to(PG.pic_security(620, 420), 620, 420)]
    rws = rows([(e, PG.ROW_ICON[e], h__, b__, pc) for (e, h__, b__), pc in zip(CP.ROWS, pics)])
    roles = pad(head("Who uses Campus", "portals", CP.ROLES_H) + '<div style="display:flex;flex-direction:column;gap:14px">'
                + "".join(role_tile(*r) for r in CP.ROLES) + '</div>')
    return [top, gap() + depts, gap() + focus, gap() + rws, gap() + roles, gap() + moving_band(), gap() + price_band()] + end()


def role_tile(n, p_, d, k):
    art = (portal_art.portal_scene("Student", 270, 186, 25, 140, 115, labels=False) if k == "pupils" else dept_art.art(k, 270, 186, U=34))
    return (f'<div style="position:relative;height:300px;border-radius:22px;background:{PLATE};overflow:hidden;padding:22px 22px 0;box-sizing:border-box">'
            f'<div style="display:inline-flex;align-items:center;gap:6px;height:26px;padding:0 10px 0 4px;border-radius:13px;background:#fff;box-shadow:inset 0 0 0 1px {LINE};font:500 12px {SANS};color:{INK2}">'
            f'{portal_art.portal_icon(p_, 18)}{p_} portal</div>'
            f'<div style="font:600 24px/1.15 {SANS};letter-spacing:-0.02em;margin-top:14px">{n}</div>'
            f'<div style="font:400 14.5px/1.5 {SANS};color:{INK2};margin-top:8px;max-width:290px">{d}</div>'
            f'<div style="position:absolute;left:22px;bottom:22px">{PG.explore()}</div>'
            f'<div style="position:absolute;right:-30px;bottom:-34px">{art}</div></div>')


def moving_band():
    S = CP.SWITCH
    chips = "".join(f'<span style="display:inline-flex;align-items:center;height:30px;padding:0 12px;border-radius:15px;background:#fff;box-shadow:inset 0 0 0 1px {LINE};font:500 13px {SANS};color:{INK2}">{m}</span>' for m in S["moves"])
    return (f'<section style="background:{PLATE};padding:64px {MX}px;display:flex;flex-direction:column;gap:14px">{eyebrow(S["eyebrow"], "moving")}{h2(S["h_home"])}{p(S["b"])}'
            f'<div style="display:flex;flex-wrap:wrap;gap:8px">{chips}</div>'
            f'<div style="margin-top:12px;border-radius:22px;background:#fff;box-shadow:0 0 0 1px {LINE};padding:24px 20px">{PG.steps(S["steps"], 310)}</div>'
            f'<div>{PG.explore("How we move your records")}</div></section>')


def price_band():
    P_ = CP.PRICING
    return pad(f'<div style="display:flex;flex-direction:column;gap:14px">{eyebrow("Pricing", "pricing")}{h2(P_["h"])}{p(P_["b"])}'
               f'<div>{ticks(["Setup, data capture and training free", "First month free", "Every department and portal included"], size=15)}</div>'
               f'<div style="margin-top:6px">{ph("girl-beret.jpg", CW, 300, "center 20%", 20)}</div>{btn_full("See pricing", "arrow-right-line", "secondary")}</div>')


def solutions():
    S = SW.SOLUTIONS
    import mark_anim
    top = nav() + hero(S["eyebrow"], "solutions", S["h"], S["b"])
    rws = rows([(e, PG.ROW_ICON[e], h_, b_, pc) for (e, h_, b_), pc in zip(CP.ROWS[:3], [scale_to(mark_anim.mark_journey(620, 460), 620, 460),
                photo_card("classroom-zambia.jpg", "center 40%", HR.tagged("Teacher portal", __import__("ui").register_card(SB, 310, offline=True))), scale_to(PG.pic_integrations(620, 420), 620, 420)])])
    return [top, gap(40) + pad(tiles([d[1] for d in CP.DEPARTMENTS])), gap() + rws, gap() + moving_band()] + end()


def who():
    S = SW.WHO
    top = nav() + hero(S["eyebrow"], "who", S["h"], S["b"], f'<div style="border-radius:22px;overflow:hidden">{scale_to(PG.on_plate(dept_art.schools_campus(600, 420), 600, 420), 600, 420)}</div>')
    ty = "".join(f'<div><div style="position:relative">{ph(PG.TYPE_PHOTO[k][0], CW, 200, PG.TYPE_PHOTO[k][1], 20)}'
                 f'<div style="position:absolute;left:12px;bottom:12px;border-radius:12px;box-shadow:0 8px 18px -10px rgba(11,12,20,.5)">{nav_icons.nav_icon(k, 40)}</div></div>'
                 f'<div style="font:600 19px {SANS};margin-top:14px">{n}</div><div style="font:400 15px/1.5 {SANS};color:{INK2};margin-top:4px">{d}</div>'
                 f'<div style="margin-top:12px">{PG.explore()}</div></div>' for n, k, d in CP.SCHOOL_TYPES)
    types = pad(head("Who we serve · K-12", "who", S["types_h"]) + f'<div style="display:flex;flex-direction:column;gap:32px">{ty}</div>')
    roles = pad(head("Who uses Campus", "portals", CP.ROLES_H) + '<div style="display:flex;flex-direction:column;gap:14px">' + "".join(role_tile(*r) for r in CP.ROLES) + '</div>')
    return [top, gap() + types, gap() + roles] + end()


def platform():
    P = SW.PLATFORM
    import mark_anim
    top = nav() + hero(P["eyebrow"], "platform", P["h"], P["b"], photo_card("pupils-writing.jpg", "center 40%", tcard("student_card")))
    r1 = rows([(e, PG.ROW_ICON[e], h_, b_, pc) for (e, h_, b_), pc in zip(CP.ROWS[:2], [scale_to(mark_anim.mark_journey(620, 460), 620, 460),
               photo_card("classroom-zambia.jpg", "center 40%", HR.tagged("Teacher portal", __import__("ui").register_card(SB, 310, offline=True)))])])
    pt = "".join(f'<div style="position:relative;height:280px;border-radius:22px;background:{PLATE};overflow:hidden;padding:22px 22px 0;box-sizing:border-box">'
                 f'<div style="font:600 22px {SANS};letter-spacing:-0.02em">{n} portal</div><div style="font:400 14.5px/1.5 {SANS};color:{INK2};margin-top:6px">{w_}</div>'
                 f'<div style="font:400 14px/1.5 {SANS};color:{MUTED};margin-top:2px">{wh}</div>'
                 f'<div style="position:absolute;right:-20px;bottom:-30px">{portal_art.portal_scene(n, 280, 190, 24, 140, 118, labels=False)}</div></div>' for n, w_, wh in P["portals"])
    portals = pad(head("Four portals", "portals", P["portals_h"]) + f'<div style="display:flex;flex-direction:column;gap:14px">{pt}</div>')
    e, h_, b_ = CP.ROWS[4]
    ae, ah, ab = P["ai"]
    r2 = rows([(e, "security", h_, b_, scale_to(PG.pic_security(), 620, 420)), (ae, "ai", ah, ab, plate_card(tcard("ai_card", 310)))])
    more = pad(head("Platform", "platform", P["more_h"]) + '<div style="display:flex;flex-direction:column;gap:14px">'
               + WP.link_card("integrations", "Integrations", "Sage Pastel, QuickBooks, ZIMRA fiscalisation and payments.", "See the integrations")
               + WP.link_card("moving", "Moving to Campus", "From your old system to your first term on Campus, in four weeks.", "How we move your records") + '</div>')
    return [top, gap() + r1, gap() + portals, gap() + r2, gap() + more] + end()


def marketplace():
    import brands
    cats = ["All"] + [c for c, _ in SC.MARKET]
    chips = "".join(f'<span style="flex:none;height:34px;padding:0 14px;border-radius:17px;display:inline-flex;align-items:center;font:500 13.5px {SANS};'
                    f'{"background:" + INK + ";color:#fff" if i == 0 else "background:#fff;color:" + INK2 + ";box-shadow:inset 0 0 0 1px " + LINE}">{c}</span>' for i, c in enumerate(cats))
    items = ""
    for cat, its in SC.MARKET:
        for n, d, st in its:
            act = (f'<span style="display:inline-flex;align-items:center;gap:4px;height:28px;padding:0 10px;border-radius:14px;background:{OKS};color:{OK};font:500 12px {SANS}">{ic("check-line", 12, OK)}Connected</span>'
                   if st else f'<span style="display:inline-flex;align-items:center;height:28px;padding:0 12px;border-radius:14px;box-shadow:inset 0 0 0 1px {LINE};font:500 12px {SANS}">Add</span>')
            items += (f'<div style="display:flex;align-items:center;gap:12px;padding:12px 14px;border-top:1px solid {LINE}">{brands.logo(n, 34)}'
                      f'<div style="flex:1;min-width:0"><div style="font:600 14.5px {SANS}">{n}</div><div style="font:400 12.5px {SANS};color:{MUTED}">{d}</div></div>{act}</div>')
    return (f'<div style="border-radius:20px;background:#fff;box-shadow:0 0 0 1px {LINE},0 24px 40px -28px rgba(11,12,20,.35);overflow:hidden">'
            f'<div style="display:flex;align-items:center;gap:10px;padding:14px">{pmark("Campus", 26, 7)}<span style="font:600 15px {SANS}">Integrations</span></div>'
            f'<div style="padding:0 14px 12px"><div style="display:flex;align-items:center;gap:8px;height:38px;padding:0 12px;border-radius:19px;background:#f2f4f7;font:400 13.5px {SANS};color:{FAINT}">{ic("search", 15, MUTED)}Search integrations</div></div>'
            f'<div style="display:flex;gap:8px;padding:0 14px 14px;overflow:hidden">{chips}</div>{items}</div>')


def integrations():
    I_ = SW.INTEG
    top = nav() + hero(I_["eyebrow"], "integrations", I_["h"], I_["b"], photo_card("girls-papers.jpg", "center 40%", tcard("payments_card")))
    items = []
    for i, (e, k, h_, b_, cn, to) in enumerate(I_["rows"]):
        kw = {"to": to} if to else {}
        c = HR.tagged("Administration portal", WP.card_html(cn, 310, **kw))
        pic = photo_card("accountant-man.jpg", "center 30%", c) if i == 1 else photo_card("mother-phone.jpg", "65% center", c) if i == 3 else plate_card(c)
        items.append((e, k, h_, b_, pic))
    mk = f'<section style="background:{PLATE};padding:64px {MX}px">{head(I_["market_eye"], "integrations", I_["market_h"])}{marketplace()}</section>'
    return [top, gap() + rows(items), gap() + mk, gap() + faq("Questions", "questions", "What bursars ask about the links.", I_["faq"])] + end()


def moving():
    S = CP.SWITCH
    top = nav() + hero(S["eyebrow"], "moving", S["h"], S["b"], f'<div style="border-radius:22px;overflow:hidden;{DOTS}">{scaled(cta_art.cta_scene("visit", 600, 520, 50, 300, 300), CW, round(520 * CW / 600), CW / 600)}</div>',
                       btn_full("Book a demo") + btn_full("Download the price sheet (PDF)", "download-2", "secondary"))
    cols = "".join(f'<div style="border-radius:20px;background:#fff;box-shadow:inset 0 0 0 1px {LINE};padding:22px 20px"><div style="font:600 19px {SANS}">{i + 1}. {t}</div>'
                   f'<div style="font:400 15px/1.55 {SANS};color:{INK2};margin-top:6px">{d}</div></div>' for i, (wk, t, d) in enumerate(S["steps"]))
    plan = f'<section style="background:{PLATE};padding:64px {MX}px">{head("The four weeks", "demo", "From your old system to your first term on Campus.")}<div style="display:flex;flex-direction:column;gap:12px">{cols}</div></section>'
    keys = ("Parent", "hr-payroll", "fees", "record", "calendar-t", "stock")
    lines = ["Every pupil's record with their guardians, class and house.", "Contracts, leave balances and the details payroll needs.",
             "Each family's balance in US dollars and ZiG, signed off by the bursar.", "This year's marks and the reports already sent home.",
             "Forms, subjects, rooms and the timetable for the term.", "Stores, uniforms and textbooks, with what is issued to whom."]
    cards = "".join(f'<div style="border-radius:20px;background:{PLATE};padding:22px;display:flex;gap:14px">{nav_icons.nav_icon(k, 40)}<div><div style="font:600 18px/1.2 {SANS}">{m}</div>'
                    f'<div style="font:400 14.5px/1.5 {SANS};color:{INK2};margin-top:4px">{ln}</div></div></div>' for m, ln, k in zip(S["moves"], lines, keys))
    what = pad(head("What moves", "stock", "Everything the school keeps, on one record.") + f'<div style="display:flex;flex-direction:column;gap:12px">{cards}</div>')
    return [top, gap() + plan, gap() + what, gap() + faq("Questions", "questions", "What schools ask before they move.", S["faq"])] + end("training")


def pricing():
    P = SW.PRICE
    top = nav() + hero(P["eyebrow"], "pricing", P["h"], P["b"], f'<div style="display:flex;flex-direction:column;gap:14px">{pricing_card(CP.PRICING["main"], True, CW)}{pricing_card(CP.PRICING["lms"], False, CW)}</div>',
                       btn_full("Book a demo") + btn_full("Download the price sheet (PDF)", "download-2", "secondary"))
    calc = row(P["calc_h"], "calculator", "Your school's figure, before you call us.", P["calc_b"], calculator("1,140", False, CW))
    inc = "".join(f'<div style="display:flex;flex-direction:column;gap:8px;padding:18px;border-radius:18px;background:{PLATE}">{nav_icons.nav_icon(k, 40)}'
                  f'<div style="font:600 15.5px/1.25 {SANS};margin-top:4px">{t}</div><div style="font:400 13.5px/1.45 {SANS};color:{INK2}">{d}</div></div>' for k, t, d in P["included"])
    included = pad(head(P["incl_h"], "included", "Everything, at US$1 per active pupil per month.") + f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px">{inc}</div>')
    setup = (f'<section style="background:{PLATE};padding:64px {MX}px;display:flex;flex-direction:column;gap:14px">{eyebrow(P["setup_h"], "training")}{h2("Running in four weeks, with us at the school.")}{p(P["setup_b"])}'
             f'<div style="border-radius:20px;overflow:hidden;{DOTS};box-shadow:inset 0 0 0 1px #e3e6eb;margin-top:8px">{scaled(cta_art.cta_scene("training", 600, 460, 46, 300, 270), CW, round(460 * CW / 600), CW / 600)}</div>'
             f'<div style="margin-top:8px">{PG.steps(CP.SWITCH["steps"], CW)}</div></section>')
    qa = FAQ + [("What does setup cost?", "Nothing. Setup, data capture and training are free."), ("Is there a charge per user?", "No. Staff, guardians and pupils sign in at no extra cost.")]
    return [top, gap() + calc, gap() + included, gap() + setup, gap() + faq(P["faq_h"], "questions", "What schools ask about the price.", qa)] + end()


def demo():
    D = SW.DEMO
    st = "".join(f'<div style="display:flex;gap:14px;padding:14px 0;border-top:1px solid {LINE}"><span style="width:30px;height:30px;border-radius:15px;background:#e8effd;color:{BLUE};'
                 f'display:flex;align-items:center;justify-content:center;font:600 13.5px {SANS};flex:none">{n}</span><div><div style="font:600 16px {SANS}">{t}</div>'
                 f'<div style="font:400 14.5px/1.5 {SANS};color:{INK2};margin-top:3px">{d}</div></div></div>' for n, t, d in D["steps"])
    form = (f'<div style="border-radius:22px;background:#fff;box-shadow:0 0 0 1px {LINE},{SH_CARD};padding:24px 20px;display:flex;flex-direction:column;gap:16px">'
            f'<div style="font:600 22px {SANS}">Book a demo</div>'
            + "".join(field(l, v, ph_, help_=hp, w=310, kind=kd) for l, v, ph_, hp, kd in [("Your name", "Chipo Mutasa", "", "", "text"), ("Your role", "Head", "", "", "select"),
                      ("School", "Mukuvisi High School", "", "", "text"), ("Active pupils", "1,140", "", "Roughly is fine.", "text"), ("Phone", "+263 77 000 0000", "", "", "text"),
                      ("Email", "", "head@yourschool.ac.zw", "", "text")])
            + f'<div><div style="font:500 14px {SANS};margin-bottom:10px">How should we show you?</div><div style="display:flex;gap:24px">{check("Visit the school", True, True)}{check("Video call", False, True)}</div></div>'
            + f'{btn_full("Book a demo")}<div style="font:400 13px/1.5 {SANS};color:{MUTED}">We use these details only to arrange the demo.</div></div>')
    top = nav() + (f'<section style="padding:36px {MX}px 0;display:flex;flex-direction:column;gap:18px">{eyebrow(D["eyebrow"], "demo")}{h1(D["h"])}{p(D["b"], 17)}'
                   f'<div><div style="font:600 17px {SANS};margin-bottom:4px">{D["next_h"]}</div>{st}</div><div style="margin-top:8px">{form}</div></section>')
    ag = "".join(f'<div style="border-radius:22px;background:{PLATE};padding:22px 18px 22px">'
                 f'<span style="display:inline-flex;align-items:center;gap:6px;height:28px;padding:0 11px;border-radius:14px;background:#fff;box-shadow:inset 0 0 0 1px {LINE};'
                 f'font:500 13px {SANS};color:{INK2}"><b style="font:500 12.5px {MONO};color:{BLUE}">{t}</b>{room}</span>'
                 f'<div style="font:600 21px/1.2 {SANS};letter-spacing:-0.02em;margin-top:12px">{h_}</div><div style="font:400 15px/1.5 {SANS};color:{INK2};margin-top:6px">{d}</div>'
                 f'<div style="margin-top:16px;display:flex;justify-content:center">{tcard(cn, 310)}</div></div>' for t, room, h_, d, cn in D["agenda"])
    agenda = pad(head("Your demo", "demo", D["agenda_h"]) + f'<div style="display:flex;flex-direction:column;gap:14px">{ag}</div>')
    e, k, h_, b_ = D["who"]
    who_ = row(e, k, h_, b_, photo_card("woman-files.jpg", "center 30%", tcard("visitors_card", 326)))
    return [top, gap() + agenda, gap() + who_, gap() + faq("Questions", "questions", D["faq_h"], D["faq"]), gap(), footer()]


def sent():
    S = SW.SENT
    top = nav() + (f'<section style="padding:32px {MX}px 0;display:flex;flex-direction:column;align-items:center;text-align:center">'
                   f'<div style="border-radius:22px;overflow:hidden;{DOTS};box-shadow:inset 0 0 0 1px #e3e6eb">{scaled(cta_art.cta_scene("visit", 700, 420, 42, 350, 245), CW, 210, CW / 700)}</div>'
                   f'<span style="width:48px;height:48px;border-radius:24px;background:{OKS};display:flex;align-items:center;justify-content:center;margin-top:32px">{ic("check-line", 24, OK)}</span>'
                   f'<div style="margin-top:18px">{h1(S["h"])}</div><div style="margin-top:12px">{p(S["b"], 17)}</div></section>')
    cards = ('<div style="display:flex;flex-direction:column;gap:14px">'
             + WP.link_card("pricing", "Pricing", "US$1 per active pupil per month, with setup and training free.", "See pricing")
             + WP.link_card("moving", "Moving to Campus", "How we move your records in four weeks.", "How we move your records")
             + WP.link_card("pricesheet", "The price sheet", "One page to take to your SDC or board.", "Download the price sheet (PDF)") + '</div>')
    return [top, gap(64) + pad(f'<div style="font:600 20px {SANS};margin-bottom:18px;text-align:center">{S["next_h"]}</div>{cards}'), gap(), footer()]


def signin():
    S = SW.SIGNIN
    pw = field("Password", "••••••••••", w=CW).replace("••••••••••</span>", f'••••••••••</span><span style="font:500 13px {SANS};color:{BLUE}">Show</span>', 1)
    portals = "".join(f'<span style="display:inline-flex;align-items:center;gap:5px;height:30px;padding:0 10px 0 4px;border-radius:15px;background:rgba(255,255,255,.94);font:500 12.5px {SANS}">'
                      f'{portal_art.portal_icon(n, 22)}{n}</span>' for n in PORTAL_NAMES)
    return (f'<div style="width:{MW}px;height:844px;background:#fff;font-family:{SANS};color:{INK};position:relative;overflow:hidden">'
            f'<div style="position:relative;height:250px"><img src="{PH("boys-reading-2.jpg")}" alt="" style="width:100%;height:100%;object-fit:cover;object-position:47% 42%">'
            f'<div style="position:absolute;left:{MX}px;right:{MX}px;bottom:14px;display:flex;flex-wrap:wrap;gap:6px">{portals}</div></div>'
            f'<div style="padding:28px {MX}px">{lockup(22, by=False)}<div style="font:600 30px/1.1 {SANS};letter-spacing:-0.03em;margin-top:22px">{S["h"]}</div>'
            f'<div style="margin-top:24px">{field("Email or phone number", "rudo.moyo@gmail.com", w=CW)}</div><div style="margin-top:16px">{pw}</div>'
            f'<div style="display:flex;justify-content:space-between;align-items:center;margin-top:14px">{check("Keep me signed in", True)}<span style="font:500 14px {SANS};color:{BLUE}">Forgot password?</span></div>'
            f'<div style="margin-top:22px">{btn_full("Sign in", "arrow-right-line")}</div></div>'
            f'<div style="position:absolute;left:{MX}px;right:{MX}px;bottom:24px;display:flex;gap:18px;font:400 13px {SANS};color:{MUTED}"><span>Privacy</span><span>Terms</span><span>Support</span></div></div>')


def contact():
    C = SW.CONTACT
    top = nav() + hero(C["eyebrow"], "contact", C["h"], C["b"])
    routes = pad('<div style="display:flex;flex-direction:column;gap:14px">' + "".join(WP.link_card(k, t, d, a) for k, t, d, a in C["routes"]) + '</div>')
    topics = "".join(filter_pill(t, i == 0) for i, t in enumerate(C["topics"]))
    form = (f'<section style="background:{PLATE};padding:64px {MX}px;display:flex;flex-direction:column;gap:16px">{eyebrow(C["form_h"], "contact")}{h2(C["form_hh"])}{p(C["form_b"])}'
            f'<div style="display:flex;flex-wrap:wrap;gap:8px">{topics}</div>'
            f'{field("Your name", "Chipo Mutasa", w=CW)}{field("Email", "head@mukuvisi.ac.zw", w=CW)}{field("Organisation", "Mukuvisi High School", w=CW)}'
            f'{field("Message", "", "What would you like to ask?", kind="area", w=CW)}{btn_full("Send message", "send-plane")}'
            f'<div style="margin-top:24px">{photo_card("office-documents.jpg", "center 30%", HR.tagged("Campus team", SC.thread_card(326)))}</div></section>')
    return [top, gap(40) + routes, gap() + form] + end()


def support():
    S = SW.SUPPORT
    search = (f'<div style="height:52px;border-radius:26px;background:#fff;box-shadow:0 0 0 1px {LINE},{SH_CARD};display:flex;align-items:center;gap:10px;padding:0 18px">'
              f'{ic("search", 18, MUTED)}<span style="font:400 15px {SANS};color:{FAINT}">Search the guides</span></div>')
    top = nav() + hero(S["eyebrow"], "support", S["h"], S["b"], "", search)
    tp = "".join(f'<div style="border-radius:22px;background:{PLATE};padding:22px">{nav_icons.nav_icon(k, 40)}<div style="font:600 20px {SANS};margin-top:14px">{t}</div><div style="margin-top:8px">'
                 + "".join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:11px 0;border-top:1px solid #e3e6eb;font:400 15px {SANS};color:{INK2}">{g}{ic("right-line", 14, FAINT)}</div>' for g in gs)
                 + '</div></div>' for k, t, gs in S["topics"])
    topics = pad(head("Guides", "support", "Find the guide for your job.") + f'<div style="display:flex;flex-direction:column;gap:14px">{tp}</div>')
    reach = pad(head("Support", "support", S["reach_h"]) + '<div style="display:flex;flex-direction:column;gap:14px">'
                + "".join(WP.link_card(k, t, d, a) for k, t, d, a in S["reach"]) + '</div>')
    return [top, gap() + topics, gap() + reach] + end()


def legal(key):
    L = SW.LEGAL[key]
    top = nav() + (f'<section style="padding:36px {MX}px 28px;border-bottom:1px solid {LINE};margin:0 0 0;display:flex;flex-direction:column;gap:14px">{eyebrow(L["title"], key)}{h1(L["h"])}'
                   f'<div style="font:400 14px {SANS};color:{MUTED}">{SW.LEGAL_UPDATED}</div></section>')
    body = "".join(f'<div style="padding-top:{28 if i else 0}px"><h3 style="margin:0;font:600 21px/1.25 {SANS};letter-spacing:-0.015em">{t}</h3>'
                   f'<p style="margin:10px 0 0;font:400 16.5px/1.65 {SANS};color:{INK2}">{pp}</p></div>' for i, (t, pp) in enumerate(L["sections"]))
    oth = "".join(f'<div style="display:flex;align-items:center;gap:12px;padding:16px 18px;border-radius:18px;background:{PLATE}">{nav_icons.nav_icon(k, 34)}'
                  f'<span style="font:600 16px {SANS};flex:1">{v["title"]}</span>{ic("arrow-right-line", 16, BLUE)}</div>' for k, v in SW.LEGAL.items() if k != key)
    return [top, gap(32) + pad(body + f'<div style="display:flex;flex-direction:column;gap:12px;margin-top:48px">{oth}</div>'), gap(), footer()]

# -*- coding: utf-8 -*-
"""Sections made for each kind of school on the Who we serve pages. Each type shows what is particular to it:
the day school's day, the boarding house at lights out, who pays whom at a government school, a private school's
admissions and board, and a mission school's day scholars and boarders side by side."""
from ds import *
import pages as PG
import site_cards as SC
import hero as HR
import nav_icons, portal_art
from ui import card, chead, rowl, status, lab, fig

S = SB
X, GAP = PG.X, PG.GAP


def _tc(portal, inner):
    return HR.tagged(f"{portal} portal", inner)


def _pills(*p):
    return '<div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:10px">' + "".join(status(S, t, k) for t, k in p) + '</div>'


def head(eye, key, h, w=820, mb=44):
    return f'<div style="display:flex;flex-direction:column;gap:16px;margin-bottom:{mb}px">{PG.eyebrow(eye, key)}{PG.head(h, 46, w)}</div>'


def wrap(inner):
    return f'<div style="padding:0 {X}px">{inner}</div>'


def plate_band(inner):
    return f'<section style="background:{PLATE};padding:{GAP - 40}px {X}px">{inner}</section>'


def row(eye, key, h, b, pic, flip=False):
    txt = (f'<div style="flex:1;display:flex;flex-direction:column;gap:18px;justify-content:center;max-width:500px">{PG.eyebrow(eye, key)}{PG.head(h, 42, 500)}'
           f'{para(b, 18, INK2, 480)}</div>')
    pic_ = f'<div style="flex:none">{pic}</div>'
    return wrap(f'<div style="display:flex;gap:96px;align-items:center;justify-content:space-between">{pic_ + txt if flip else txt + pic_}</div>')


# ---- cards only these pages use ----------------------------------------------------------------------
def absence_card(w=230):
    return card(S, chead(S, "send-plane", "Absent today", "08:06")
                + rowl(S, "Farai Nyathi", "Form 3B", top=False)
                + f'<div style="margin-top:6px;padding:8px 10px;border-radius:12px;background:#f2f4f7;font:400 12.5px/1.45 {SANS};color:{INK2}">'
                  f'Farai is marked absent today. Reply to Ms Sibanda if you know why.</div>' + _pills(("Sent to Mr Nyathi", "ok")), w)


def family_card(w=330):
    return card(S, chead(S, "home-3", "Moyo family · Term 3", "One statement")
                + rowl(S, "Tanaka · Form 3B", "US$1,250.00", top=False) + rowl(S, "Rufaro · Grade 5", "US$980.00") + rowl(S, "Transport, both", "US$180.00")
                + rowl(S, "Sibling discount, 5%", "−US$49.00", OK) + rowl(S, "Paid, EcoCash 14 Sep", "−US$500.00", OK) + rowl(S, "Balance", "US$1,861.00", INK, True)
                + _pills(("Due Fri 16 Oct", "warn")), w)


def request_card(w=250):
    return card(S, chead(S, "door", "Exeat request", "", CAMPUS)
                + rowl(S, "Kudzai Mhlanga", "Form 4", top=False) + rowl(S, "Out", "Fri 16:00") + rowl(S, "Back", "Sun 17:00") + rowl(S, "Collecting", "Mr T. Mhlanga")
                + f'<div style="margin-top:10px">{cbtn("Send request", "send-plane", "primary", "sm")}</div>', w)


def approve_card(w=250):
    return card(S, chead(S, "check-circle", "Waiting for you", "Mr Chari", BLUE)
                + rowl(S, "Kudzai Mhlanga · exeat", "Fri–Sun", top=False) + rowl(S, "Guardian on record", "Mr T. Mhlanga", OK)
                + rowl(S, "Fees", "Up to date", OK)
                + f'<div style="display:flex;gap:8px;margin-top:10px">{cbtn("Approve", "check-line", "primary", "sm")}{cbtn("Decline", "", "secondary", "sm")}</div>', w)


def signout_card(w=250):
    return card(S, chead(S, "time", "Signed out", "16:12", OK)
                + rowl(S, "Kudzai Mhlanga", "Tsavo House", top=False) + rowl(S, "Collected by", "Mr T. Mhlanga") + rowl(S, "Due back", "Sun 17:00")
                + _pills(("Off the house list", "campus")), w)


def gov_staff_card(w=320):
    return card(S, chead(S, "user-3", "Mr Tendai Chari", "Mathematics")
                + rowl(S, "Paid by", "Government", top=False) + rowl(S, "Contract and posting", "On file") + rowl(S, "Leave this year", "3 of 22 days")
                + rowl(S, "Timetable", "26 lessons a week") + _pills(("Not on the school payroll", "mute")), w)


def sdc_payrun_card(w=320):
    return card(S, chead(S, "wallet-3", "SDC payroll · September", "14 staff")
                + rowl(S, "Groundsmen", "4", top=False) + rowl(S, "Security", "3") + rowl(S, "Office and kitchen", "5") + rowl(S, "Extra teachers", "2")
                + rowl(S, "Net pay", "US$3,940.00", INK, True)
                + f'<div style="margin-top:10px">{cbtn("Approve payroll", "check-circle", "primary", "sm")}</div>', w)


def bigclass_card(w=320):
    dots = "".join(f'<i style="width:14px;height:14px;border-radius:4px;background:{BAD if i in (7, 23, 41) else OK};opacity:{1 if i in (7, 23, 41) else .75}"></i>' for i in range(52))
    return card(S, chead(S, "book-6", "Form 2C register", "07:35")
                + f'<div style="display:grid;grid-template-columns:repeat(13,14px);gap:5px;margin:4px 0 10px">{dots}</div>'
                + rowl(S, "Present", "49") + rowl(S, "Absent", "3", BAD)
                + f'<div style="display:flex;gap:8px;margin-top:10px">{cbtn("Mark all present", "check-line", "secondary", "sm")}{cbtn("Save", "", "primary", "sm")}</div>', w)


def board_card(w=320):
    return card(S, chead(S, "chart-bar", "Board report · Term 3", "Draft", BLUE)
                + rowl(S, "Pupils on the roll", "1,140 (+38)", top=False) + rowl(S, "Fees collected", "70.3%") + rowl(S, "Form 4 average", "64% (+3)")
                + rowl(S, "Staff", "86 · 2 vacancies") + rowl(S, "Places for 2027", "96 of 120 accepted")
                + f'<div style="margin-top:10px">{cbtn("Download the report (PDF)", "download-2", "secondary", "sm")}</div>', w)


def mixed_register_card(w=320):
    rows = [("Tanaka Moyo", "Boarder", "P"), ("Tendai Chirwa", "Day", "P"), ("Ruvimbo Gumbo", "Boarder", "P"), ("Farai Nyathi", "Day", "A"), ("Chiedza Banda", "Day", "P")]
    r = "".join(f'<div style="display:flex;align-items:center;gap:10px;padding:7px 0;border-top:1px solid #edeff2;font-size:13px"><span style="flex:1">{n}</span>'
                f'<span style="font:500 11.5px {SANS};color:{CAMPUS if t == "Boarder" else INK2};background:{"#efeaff" if t == "Boarder" else "#eef0f3"};padding:2px 8px;border-radius:10px">{t}</span>'
                f'{status(S, "Present" if m == "P" else "Absent", "ok" if m == "P" else "bad")}</div>' for n, t, m in rows)
    return card(S, chead(S, "book-6", "Form 3B register", "07:42") + r
                + f'<div style="display:flex;justify-content:space-between;padding-top:10px;border-top:1px solid #edeff2;font-size:12.5px;color:{MUTED}"><span>22 day · 16 boarders</span><span>38</span></div>', w)


def authority_doc(w=400):
    sec = lambda t, rows: (f'<div style="margin-top:14px"><div style="font:600 12.5px {SANS};color:{INK}">{t}</div>'
                           + "".join(f'<div style="display:flex;justify-content:space-between;padding:5px 0;border-bottom:1px solid #eef0f3;font:400 12px {SANS};color:{INK2}"><span>{a}</span><span style="{NUM}">{b}</span></div>' for a, b in rows) + '</div>')
    return (f'<div style="width:{w}px;box-sizing:border-box;background:#fff;border-radius:6px;box-shadow:0 0 0 1px {LINE},0 24px 40px -24px rgba(11,12,20,.4);padding:28px 30px 30px">'
            f'<div style="display:flex;justify-content:space-between;align-items:center">{pmark("Campus", 26, 7)}<span style="font:400 11px {MONO};color:{MUTED}">Term 3 · 2026</span></div>'
            f'<div style="font:500 20px/1.2 {SERIF};margin-top:18px">Report to the responsible authority</div>'
            + sec("Enrolment", [("Day scholars", "412"), ("Boarders", "288"), ("New this year", "64")])
            + sec("Results", [("Form 4 average", "62%"), ("Upper Sixth average", "68%")])
            + sec("Finance", [("Fees and levies billed", "US$486,200"), ("Collected", "US$341,900 · 70.3%")])
            + sec("Staff", [("Paid by government", "31"), ("Paid by the school", "18")])
            + '</div>')


# ---- sections by type -----------------------------------------------------------------------------------
def day_sections():
    # one moment at a time: a short list of the day on the left, one picture for the selected moment on the right.
    # On a phone the list becomes a row of time chips above the picture, so nothing has to shrink.
    steps = [("06:50", "On the bus"), ("07:30", "Register"), ("08:06", "Absences home"), ("12:40", "Marks in"), ("16:10", "Home time")]
    on = 1
    lst = "".join(
        (f'<div style="display:flex;gap:18px;padding:20px 0;border-top:1px solid {LINE}">'
         f'<span style="width:58px;flex:none;font:500 14px {MONO};color:{BLUE if i == on else MUTED};padding-top:3px">{t}</span>'
         f'<div><div style="font:600 {24 if i == on else 20}px/1.2 {SANS};letter-spacing:-0.015em;color:{INK if i == on else MUTED}">{h}</div>'
         + (f'<div style="font:400 16px/1.55 {SANS};color:{INK2};margin-top:8px;max-width:360px">Ms Sibanda marks Form 3B on a tablet before the first lesson, '
            f'with or without internet. The office sees it by 08:05.</div>' if i == on else '') + '</div></div>')
        for i, (t, h) in enumerate(steps)) + f'<div style="border-top:1px solid {LINE}"></div>'
    pic = photo_story("teacher-tablet.jpg", "center 25%", [(0, 90, _tc("Teacher", SC_card("register_card", 300)))], 620, 520)
    day = row_html = wrap(head("The school day", "t-day", "From the bus stop to home time, on one record.")
                          + f'<div style="display:flex;gap:96px;align-items:center;justify-content:space-between"><div style="flex:1;max-width:460px">{lst}</div>{pic}</div>')
    fam = row("Fees by family", "fees", "One statement for every family.",
              "Brothers and sisters bill to one family account, with the sibling discount applied. Parents pay once, by EcoCash or at the bursary, and the payment lands on each child's account.",
              photo_story("child-doorway.jpg", "center 30%", [(0, 70, _tc("Parent", family_card(330)))], 620, 480), flip=True)
    tiles = ""
    for ph_, pos, t, d, pts in [("ecd-class.jpg", "center 40%", "ECD to Grade 7", "The class teacher marks one register and writes the report comment for each child.",
                                 ["Class registers", "A class teacher's comment on every report", "Parents of the youngest see each day"]),
                                ("exam-blue.jpg", "center 40%", "Form 1 to Upper Sixth", "You mark registers by lesson, enter marks by subject, and every subject teacher adds a line to the report.",
                                 ["Registers by lesson", "Mark sheets by subject", "Exam classes in the holidays"])]:
        tiles += (f'<div style="flex:1;border-radius:24px;background:{PLATE};overflow:hidden">{ph(ph_, 588, 300, pos, 0)}'
                  f'<div style="padding:26px 28px 30px"><div style="font:600 26px/1.15 {SANS};letter-spacing:-0.02em">{t}</div>'
                  f'<div style="font:400 15.5px/1.55 {SANS};color:{INK2};margin-top:8px">{d}</div><div style="margin-top:14px">{ticks(pts, INK2)}</div></div></div>')
    levels = wrap(head("Primary and secondary", "academics", "Run ECD and Upper Sixth from the same record.") + f'<div style="display:flex;gap:24px">{tiles}</div>')
    return [day, fam, levels]


def boarding_sections():
    houses = [("Tsavo House", "Mr Chari", 64, 58, 4, 1, 1), ("Kariba House", "Mrs Dube", 60, 57, 3, 0, 0),
              ("Zambezi House", "Mr Ncube", 72, 66, 5, 1, 0), ("Hwange House", "Mrs Sithole", 56, 54, 2, 0, 0)]
    cols = ""
    for n, hm, tot, inn, ex, sick, miss in houses:
        seg = lambda v, c: f'<i style="width:{v / tot * 100:.1f}%;background:{c}"></i>'
        cols += (f'<div style="flex:1;padding:20px;border-radius:16px;background:#fff;box-shadow:0 0 0 1px {LINE}">'
                 f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font:600 16px {SANS}">{n}</span>'
                 f'<span style="font:400 12.5px {SANS};color:{MUTED}">{hm}</span></div>'
                 f'<div style="display:flex;align-items:baseline;gap:6px;margin-top:14px">{fig(S, f"{inn}", 30)}<span style="font:400 13px {SANS};color:{MUTED}">of {tot} in the house</span></div>'
                 f'<div style="display:flex;height:8px;border-radius:4px;overflow:hidden;background:#eef0f3;margin:12px 0 8px">{seg(inn, BLUE)}{seg(ex, CAMPUS)}{seg(sick, WARN)}{seg(miss, BAD)}</div>'
                 + rowl(S, "On exeat", str(ex), top=False) + rowl(S, "Sick bay", str(sick)) + rowl(S, "Not marked", str(miss), BAD if miss else MUTED, bool(miss))
                 + '</div>')
    panel = (f'<div style="border-radius:20px;background:#fafbfc;box-shadow:0 0 0 1px {LINE},0 30px 60px -30px rgba(11,12,20,.35);overflow:hidden">'
             f'<div style="display:flex;align-items:center;gap:12px;padding:16px 22px;border-bottom:1px solid {LINE};background:#fff">{portal_art.portal_icon("Administration", 28)}'
             f'<span style="font:600 15px {SANS}">Houses · lights out</span><span style="font:400 13px {SANS};color:{MUTED}">Thursday 21:00 · 252 boarders</span><span style="flex:1"></span>'
             f'{status(S, "1 not marked", "bad")}</div><div style="display:flex;gap:16px;padding:20px">{cols}</div></div>')
    board = row("Roll call", "boarding", "Take roll call on your phone, house by house.",
                "Open your house at prep or lights out and tap each boarder in. Exeats and the sick bay are already marked, and anyone missing comes to the top. It works without internet.",
                photo_story("girls-smiling.jpg", "center 35%", [(0, 10, rollcall_phone(0.52))], 620, 480), flip=True)
    arrow = f'<div style="flex:none;align-self:center;width:40px;display:flex;justify-content:center">{ic("arrow-right-line", 22, FAINT)}</div>'
    steps = [("1", "The guardian asks", "From the Parent portal, with who is collecting.", _tc("Parent", request_card())),
             ("2", "The housemaster approves", "The guardian and the fee account are checked on the record.", _tc("Administration", approve_card())),
             ("3", "Signed out", "The boarder leaves the house list until they are back.", _tc("Administration", signout_card()))]
    strip = arrow.join(f'<div style="width:330px;display:flex;flex-direction:column;gap:16px">'
                       f'<div style="display:flex;gap:12px;align-items:flex-start"><span style="width:30px;height:30px;border-radius:15px;background:{BLUE};color:#fff;display:flex;align-items:center;justify-content:center;font:600 14px {SANS};flex:none">{n}</span>'
                       f'<div><div style="font:600 19px {SANS}">{t}</div><div style="font:400 14.5px/1.5 {SANS};color:{INK2};margin-top:4px">{d}</div></div></div>'
                       f'<div style="padding-left:42px">{c}</div></div>' for n, t, d, c in steps)
    exeat = plate_band(head("Exeats", "sent", "An exeat in three steps, and nobody unaccounted for.") + f'<div style="display:flex;justify-content:space-between">{strip}</div>')
    fees = row("Boarding fees", "fees", "Boarding and tuition on one account.",
               "Boarding, tuck and outings bill to the family's account with tuition, in US dollars and ZiG. Guardians pay by EcoCash or bank transfer and see the balance in the portal.",
               photo_story("boys-reading-2.jpg", "47% 42%", [(0, 80, _tc("Parent", SC_card("fee_card", 320)))], 620, 460))
    return [board, exeat, fees]


def government_sections():
    tile = lambda t, d, c: (f'<div style="flex:1;border-radius:24px;background:{PLATE};padding:34px 34px 0;overflow:hidden;display:flex;flex-direction:column;gap:12px;min-height:520px">'
                            f'<div style="font:600 26px/1.15 {SANS};letter-spacing:-0.02em">{t}</div><div style="font:400 16px/1.55 {SANS};color:{INK2};max-width:440px">{d}</div>'
                            f'<div style="margin-top:20px">{c}</div></div>')
    split = wrap(head("Staff", "hr-payroll", "Who pays whom, kept straight.")
                 + '<div style="display:flex;gap:24px">'
                 + tile("Teachers the government pays", "Their contracts, postings, leave and timetables live on Campus. Their pay does not.", _tc("Administration", gov_staff_card()))
                 + tile("Staff your SDC employs", "Groundsmen, security, the office, the kitchen and any extra teachers are paid through Campus payroll.", _tc("Administration", sdc_payrun_card()))
                 + '</div>')
    big = row("Big classes", "academics", "A register for 52 pupils in under a minute.",
              "Mark everyone present, then tap the three who are not. It saves on the phone without internet and reaches the office when the connection returns.",
              photo_story("class-desks.jpg", "center 40%", [(0, 60, _tc("Teacher", bigclass_card()))], 620, 470), flip=True)
    levy = row("Fees and levies", "fees", "Bill tuition and levies the way your SDC sets them.",
               "Tuition, building and sports levies by form, in US dollars or ZiG. Every payment gets a receipt, and the SDC sees what has come in against what was billed.",
               PG.on_plate(at(30, 30, _tc("Parent", SC.levy_card(280))) + at(326, 196, _tc("Administration", SC.collected_card(270))), 620, 470))
    return [split, big, levy]


def private_sections():
    stages = [("Enquiries", 214), ("School tours", 176), ("Applications", 168), ("Entrance test", 142), ("Offers", 132), ("Accepted", 96)]
    bars = "".join(f'<div style="display:flex;align-items:center;gap:16px;padding:8px 0"><span style="width:130px;font:500 14.5px {SANS};color:{INK2}">{n}</span>'
                   f'<span style="flex:1;height:34px;border-radius:10px;background:#e7ebf1;position:relative;overflow:hidden">'
                   f'<i style="position:absolute;left:0;top:0;bottom:0;width:{v / 214 * 100:.1f}%;background:{BLUE if n == "Accepted" else "#8fb0f6"};border-radius:10px"></i>'
                   f'<b style="position:absolute;left:14px;top:0;bottom:0;display:flex;align-items:center;font:600 14px {SANS};color:#fff;{NUM}">{v}</b></span></div>' for n, v in stages)
    funnel = plate_band(head("Admissions", "admissions", "Fill 120 places from one list.")
                        + f'<div style="display:flex;gap:56px;align-items:center"><div style="flex:1">{bars}'
                          f'<div style="display:flex;gap:10px;margin-top:16px">{status(S, "24 places left", "info")}{status(S, "Deposits due 30 Oct", "warn")}</div></div>'
                          f'<div style="flex:none">{_tc("Administration", SC.application_card(320))}</div></div>')
    board = row("The board", "insights", "Take the board a report it can read in five minutes.",
                "Enrolment, fees, results and staffing for the term, from the records the school already keeps. Download it as a PDF for the meeting.",
                photo_story("seniors-lecture.jpg", "center 30%", [(0, 60, _tc("Administration", board_card()))], 620, 480))
    phone = row("Parent portal", "Parent", "A portal for every family.",
                "Attendance, marks, fees and reports reach each family's phone that week, with a line to the class teacher.",
                photo_story("mother-phone.jpg", "65% center", [(0, 8, PG.parent_phone(0.52))], 620, 470), flip=True)
    return [funnel, board, phone]


def mission_sections():
    reg = row("Day and boarding", "t-mission", "Day scholars and boarders on one register.",
              "One class register shows who goes home and who boards. Boarders also appear on their house's roll call, and fees bill by the type of place.",
              PG.on_plate(at(24, 30, _tc("Teacher", mixed_register_card(300))) + at(336, 240, _tc("Administration", SC.rollcall_card(260))), 620, 520))
    doc = (f'<div style="position:relative;width:620px;height:560px">{ph("girls-desks.jpg", 500, 560, "center 35%", 24).replace("flex:none", "flex:none;margin-left:120px")}'
           f'<div style="position:absolute;left:0;top:70px">{authority_doc(380)}</div></div>')
    auth = row("Responsible authority", "insights", "The report your church asks for, without retyping.",
               "Enrolment, results, finance and staffing for the responsible authority, built from the records the school keeps every day.", doc, flip=True)
    return [reg, auth]


def SC_card(name, w):
    import ui
    return getattr(ui, name)(S, w)


SECTIONS = {"t-day": day_sections, "t-boarding": boarding_sections, "t-government": government_sections,
            "t-private": private_sections, "t-mission": mission_sections}


# ---- roll call on the housemaster's phone, at true device size --------------------------------------------
def rollcall_app():
    F = "'Inter',sans-serif"
    W_, H_ = PG.SCR_W, PG.SCR_H
    pill = lambda t, fg, bg, icn=None: (f'<span style="display:inline-flex;align-items:center;gap:4px;height:30px;padding:0 11px;border-radius:15px;background:{bg};color:{fg};font:600 13px {F};white-space:nowrap">'
                                        f'{ic(icn, 14, fg) if icn else ""}{t}</span>')
    boarders = [("TZ", "Tafadzwa Zhou", "Room 6 · last seen at prep 19:40", "miss"), ("KM", "Kudzai Mhlanga", "Room 2 · back Sun 17:00", "exeat"),
                ("TM", "Tanaka Moyo", "Room 4", "in"), ("NC", "Nyasha Chari", "Room 4", "in"), ("RG", "Rufaro Gumbo", "Sick bay since 15:20", "sick"),
                ("TS", "Tinashe Sithole", "Room 5", "in"), ("BM", "Blessing Mutasa", "Room 5", "in")]
    rows = ""
    for i, (ini, n, sub, st) in enumerate(boarders):
        right = {"in": pill("In", OK, OKS, "check-line"), "exeat": pill("Exeat", CAMPUS, "#efeaff"), "sick": pill("Sick bay", WARN, WARNS),
                 "miss": pill("Mark in", "#fff", BAD), "todo": pill("Tap to mark", BLUE, "#e8effd")}[st]
        av_bg, av_fg = (BADS, BAD) if st == "miss" else ("#eef0f3", INK2)
        rows += (f'<div style="display:flex;align-items:center;gap:12px;padding:11px 16px;{"border-top:1px solid #f0f1f4;" if i else ""}">'
                 f'<span style="width:38px;height:38px;border-radius:19px;background:{av_bg};color:{av_fg};display:flex;align-items:center;justify-content:center;font:600 13px {F};flex:none">{ini}</span>'
                 f'<div style="flex:1;min-width:0"><div style="font:500 16px {F};color:{INK}">{n}</div><div style="font:400 13px {F};color:{BAD if st == "miss" else MUTED};margin-top:1px">{sub}</div></div>{right}</div>')
    seg = lambda v, c: f'<i style="width:{v / 64 * 100:.2f}%;background:{c}"></i>'
    summary = (f'<div style="background:#fff;border-radius:16px;padding:14px 16px">'
               f'<div style="display:flex;align-items:baseline;gap:6px"><span style="font:600 32px {F};letter-spacing:-0.02em">63</span>'
               f'<span style="font:400 15px {F};color:{MUTED}">of 64 accounted for</span></div>'
               f'<div style="display:flex;height:8px;border-radius:4px;overflow:hidden;background:#eef0f3;margin:10px 0 12px">{seg(58, BLUE)}{seg(4, CAMPUS)}{seg(1, WARN)}{seg(1, BAD)}</div>'
               f'<div style="display:flex;justify-content:space-between;font:400 13px {F};color:{INK2}">'
               + "".join(f'<span style="display:flex;align-items:center;gap:6px"><i style="width:8px;height:8px;border-radius:4px;background:{c}"></i>{t}</span>'
                         for t, c in (("58 in", BLUE), ("4 exeat", CAMPUS), ("1 sick bay", WARN), ("1 missing", BAD)))
               + '</div></div>')
    segctl = (f'<div style="display:flex;background:#e4e6eb;border-radius:9px;padding:2px;margin:16px 0 10px">'
              + "".join(f'<span style="flex:1;height:30px;border-radius:7px;display:flex;align-items:center;justify-content:center;font:{"600" if i == 0 else "500"} 13px {F};'
                        f'{"background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.12);" if i == 0 else ""}color:{INK}">{t}</span>' for i, t in enumerate(("All 64", "Not marked 1", "Away 5")))
              + '</div>')
    body = (f'<div style="padding:0 16px">'
            f'<div style="display:flex;align-items:center;justify-content:space-between;height:44px">'
            f'<span style="display:flex;align-items:center;gap:2px;font:400 17px {F};color:{BLUE}">{ic("left-line", 20, BLUE)}Houses</span>'
            f'<span style="font:600 17px {F}">Tsavo House</span><span style="font:400 17px {F};color:{BLUE}">Search</span></div>'
            f'<div style="font:600 28px {F};letter-spacing:-0.025em;margin:8px 4px 2px">Lights out</div>'
            f'<div style="font:400 15px {F};color:{MUTED};margin:0 4px 14px">Thursday 21:00 · Mr Chari</div>'
            f'{summary}{segctl}<div style="background:#fff;border-radius:16px;overflow:hidden">{rows}</div></div>')
    foot = (f'<div style="position:absolute;left:0;right:0;bottom:0;padding:12px 16px 34px;background:#f9f9fb;box-shadow:0 -0.5px 0 rgba(0,0,0,.18)">'
            f'<div style="display:flex;align-items:center;gap:6px;justify-content:center;font:400 13px {F};color:{MUTED};margin-bottom:10px">{ic("wifi-off", 14, MUTED)}Saved on this phone · syncs when online</div>'
            f'<div style="height:50px;border-radius:14px;background:{BLUE};color:#fff;display:flex;align-items:center;justify-content:center;font:600 17px {F}">Finish roll call</div></div>')
    return f'<div style="position:relative;width:{W_}px;height:{H_}px;background:#f2f3f6;color:{INK};overflow:hidden">{PG.status_bar("21:04")}{body}{foot}</div>'


def rollcall_phone(k=0.52):
    w, h = PG.SCR_W + 2 * PG.BEZ, PG.SCR_H + 2 * PG.BEZ
    inner = f'<div style="padding:0 6px">{PG.device(rollcall_app())}</div>'
    return f'<div style="filter:drop-shadow(0 16px 22px rgba(11,12,20,.32))">{scaled(inner, round((w + 12) * k), round(h * k), k)}</div>'

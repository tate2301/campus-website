# -*- coding: utf-8 -*-
"""Small product cards for the website pages, one world: Mukuvisi High School, Form 3B, Tanaka and Rudo Moyo,
Ms Sibanda, Mr Dube the Head, Tsavo House. Figures add up across cards."""
from ds import *
from ui import card, chead, rowl, status, lab, fig

S = SB


def _btns(*b):
    return '<div style="display:flex;gap:8px;margin-top:12px">' + "".join(cbtn(t, i, k, "sm") for t, i, k in b) + '</div>'


def _foot(t):
    return f'<div style="margin-top:8px;font-size:12px;color:{MUTED}">{t}</div>'


def _pills(*p):
    return '<div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:10px">' + "".join(status(S, t, k) for t, k in p) + '</div>'


# ---- admissions ---------------------------------------------------------------------------------------
def intake_card(w=300):
    return card(S, chead(S, "user-add", "Form 1 · 2027 intake", "120 places")
                + rowl(S, "Enquiries", "214", top=False) + rowl(S, "Applications", "168") + rowl(S, "Sat the entrance test", "142")
                + rowl(S, "Offers sent", "132") + rowl(S, "Accepted", "96", INK, True) + _pills(("Deposits due 30 Oct", "warn")), w)


def application_card(w=300):
    return card(S, chead(S, "file-check", "Application · Nyasha Banda", "A-0142")
                + rowl(S, "Guardian", "Grace Banda", top=False) + rowl(S, "Grade 7 results", "6 units") + rowl(S, "Entrance test", "68%")
                + rowl(S, "Documents", "3 of 3") + _pills(("Offer sent", "campus"), ("Deposit due 30 Oct", "warn")), w)


def offer_card(w=300):
    return card(S, chead(S, "send-plane", "Offer letters · Form 1", "Today")
                + rowl(S, "Sent to guardians", "132", top=False) + rowl(S, "Deposit paid", "96", OK) + rowl(S, "Waiting list", "18")
                + _btns(("Move to class lists", "arrow-right-line", "primary")), w)


# ---- fees ---------------------------------------------------------------------------------------------
def lhead(name, title, meta=""):
    """a card head that leads with the named service's own mark"""
    import brands
    return (f'<div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;white-space:nowrap">{brands.logo(name, 22)}'
            f'<span style="font:600 13.5px {SANS};color:{INK};overflow:hidden;text-overflow:ellipsis">{title}</span><span style="flex:1"></span>{lab(S, meta)}</div>')


def lrow(name, a, b, top=True):
    import brands
    bt = "border-top:1px solid #e3e6eb;" if top else ""
    return (f'<div style="display:flex;align-items:center;gap:10px;padding:7px 0;{bt}font-size:13px">{brands.logo(name, 20)}'
            f'<span style="flex:1">{a}</span><span style="font-weight:500;{NUM}">{b}</span></div>')


def payments_card(w=320):
    return card(S, chead(S, "bank-card", "Payments today", "Bursary")
                + lrow("EcoCash", "Tanaka Moyo", "US$500.00", top=False) + lrow("Bank transfer", "Chipo Ncube", "US$330.00")
                + lrow("Cash", "Farai Nyathi", "ZiG 2,400.00") + _pills(("3 matched to pupils", "ok"), ("R-2026-18824", "mute")), w)


def billing_card(w=320):
    return card(S, chead(S, "wallet-3", "Term 3 billing", "Ready to send")
                + rowl(S, "Tuition, Forms 1–4", "US$1,250.00", top=False) + rowl(S, "Boarding", "US$900.00") + rowl(S, "Transport", "US$180.00")
                + rowl(S, "Pupils billed", "1,140", INK, True) + _pills(("Sibling discount on 214", "campus"))
                + _btns(("Send statements", "send-plane", "primary")), w)


def arrears_card(w=320):
    rows = [("Form 1", 4120, .46), ("Form 2", 6380, .71), ("Form 3", 8950, 1.0), ("Form 4", 5210, .58)]
    r = "".join(f'<div style="display:flex;align-items:center;gap:10px;padding:7px 0;border-top:1px solid #edeff2;font-size:13px">'
                f'<span style="width:52px">{n}</span><span style="flex:1;height:8px;border-radius:4px;background:#eef0f3;position:relative">'
                f'<i style="position:absolute;left:0;top:0;bottom:0;width:{k * 100:.0f}%;border-radius:4px;background:{WARN}"></i></span>'
                f'<span style="width:84px;text-align:right;font-weight:500;{NUM}">US${v:,}</span></div>' for n, v, k in rows)
    return card(S, chead(S, "chart-bar", "Arrears by form", "Today") + r + _btns(("Send reminders", "send-plane", "secondary")), w)


# ---- accounting ---------------------------------------------------------------------------------------
def ledger_card(w=320):
    return card(S, chead(S, "book-2", "General ledger", "Sep 2026")
                + rowl(S, "Fees income", "US$412,300.00", top=False) + rowl(S, "Payroll", "−US$186,420.00") + rowl(S, "Stores and supplies", "−US$22,910.00")
                + rowl(S, "Repairs", "−US$4,180.00") + rowl(S, "Net for the month", "US$198,790.00", INK, True) + _pills(("Up to date at 18:00", "ok")), w)


def journal_card(w=320, to="Sage Pastel"):
    return card(S, lhead(to, f"Journal to {to}", "30 Sep")
                + rowl(S, "Bank", "Dr US$12,840.00", top=False) + rowl(S, "Fees income", "Cr US$11,920.00") + rowl(S, "Uniform sales", "Cr US$920.00")
                + _pills((f"Posted to {to}", "ok"), ("J-0930", "mute")), w)


def qr(n=21, s=4, seed=7):
    import random
    rnd = random.Random(seed)
    cells = ""
    for y in range(n):
        for x in range(n):
            finder = any(fx <= x < fx + 7 and fy <= y < fy + 7 for fx, fy in ((0, 0), (n - 7, 0), (0, n - 7)))
            if finder:
                lx, ly = (x % (n - 7) if x >= n - 7 else x), (y % (n - 7) if y >= n - 7 else y)
                on = lx in (0, 6) or ly in (0, 6) or (2 <= lx <= 4 and 2 <= ly <= 4)
            else:
                on = rnd.random() < .48
            if on:
                cells += f'<rect x="{x * s}" y="{y * s}" width="{s}" height="{s}"/>'
    return f'<svg width="{n * s}" height="{n * s}" viewBox="0 0 {n * s} {n * s}" fill="{INK}">{cells}</svg>'


def fiscal_card(w=280):
    m = f"font:400 11.5px {MONO};color:{INK2}"
    rows = "".join(f'<div style="display:flex;justify-content:space-between;{m};padding:3px 0"><span>{a}</span><span>{b}</span></div>'
                   for a, b in [("Receipt", "R-2026-18824"), ("Pupil", "Tanaka Moyo"), ("Term 3 fees", "US$500.00"), ("Fiscal day", "214"), ("Device", "0412")])
    return card(S, f'<div style="text-align:center;font:600 13.5px {SANS}">Mukuvisi High School</div><div style="text-align:center;font:400 11.5px {MONO};color:{MUTED};margin-top:2px">Fiscal tax invoice</div>'
                   f'<div style="border-top:1px dashed #cfd4dc;margin:10px 0 6px"></div>{rows}<div style="border-top:1px dashed #cfd4dc;margin:6px 0 10px"></div>'
                   f'<div style="display:flex;gap:12px;align-items:center">{qr()}<div style="flex:1"><div style="{m}">Verification code</div>'
                   f'<div style="font:500 12.5px {MONO};margin-top:2px">4F2A-9C1B-77D0</div><div style="margin-top:8px;display:flex;align-items:center;gap:6px">{__import__("brands").logo("ZIMRA", 20)}{status(S, "Sent to FDMS", "ok")}</div></div></div>', w)


# ---- HR and payroll -----------------------------------------------------------------------------------
def payslip_card(w=300):
    return card(S, chead(S, "file-check", "Payslip · September 2026", "Mrs T. Ncube")
                + rowl(S, "Basic salary", "US$620.00", top=False) + rowl(S, "Allowances", "US$80.00") + rowl(S, "PAYE", "−US$41.30", MUTED)
                + rowl(S, "AIDS levy", "−US$1.24", MUTED) + rowl(S, "NSSA", "−US$31.50", MUTED) + rowl(S, "Net pay", "US$625.96", INK, True), w)


def payrun_card(w=300):
    return card(S, chead(S, "wallet-3", "September payroll", "86 staff")
                + rowl(S, "Gross pay", "US$58,240.00", top=False) + rowl(S, "Deductions", "−US$7,180.00") + rowl(S, "Net pay", "US$51,060.00", INK, True)
                + _pills(("Payday 25 Sep", "info")) + _btns(("Approve payroll", "check-circle", "primary")), w)


def staff_card(w=300):
    return card(S, chead(S, "user-3", "Mrs Tariro Ncube", "Science")
                + rowl(S, "Contract", "Fixed term to Dec 2026", top=False) + rowl(S, "Qualifications", "BEd, Science") + rowl(S, "Leave left", "14 of 22 days")
                + rowl(S, "Bank details", "On file") + _pills(("Renewal due this term", "warn")), w)


def leave_card(w=300):
    r = "".join(f'<div style="display:flex;align-items:center;gap:10px;padding:8px 0;border-top:{"1px solid #edeff2" if i else "0"};font-size:13px">'
                f'<div style="flex:1"><div style="font-weight:600">{n}</div><div style="color:{MUTED};font-size:12px">{d}</div></div>'
                f'<span style="height:28px;padding:0 10px;border-radius:14px;background:{BLUE};color:#fff;display:inline-flex;align-items:center;font:500 12px {SANS}">Approve</span></div>'
                for i, (n, d) in enumerate([("Mrs Ncube", "2 days · 6–7 Oct"), ("Mr Chari", "1 day · 9 Oct"), ("Ms Sibanda", "Half day · 14 Oct")]))
    return card(S, chead(S, "calendar", "Leave requests", "3 waiting") + r + _foot("Cover goes on the timetable when you approve"), w)


# ---- boarding -----------------------------------------------------------------------------------------
def rollcall_card(w=300):
    return card(S, chead(S, "moon", "Tsavo House · lights out", "21:00")
                + rowl(S, "In the house", "58", top=False) + rowl(S, "On exeat", "4") + rowl(S, "Sick bay", "1")
                + rowl(S, "Not marked", "1", BAD, True)
                + f'<div style="display:flex;align-items:center;gap:8px;margin-top:8px;padding:8px 10px;border-radius:12px;background:{BADS};font-size:12.5px;color:{BAD}">'
                  f'{ic("alert", 14, BAD)}Tafadzwa Zhou · last seen at prep</div>', w)


def exeat_card(w=300):
    return card(S, chead(S, "door", "Exeat · Kudzai Mhlanga", "Form 4")
                + rowl(S, "Out", "Fri 16:00", top=False) + rowl(S, "Back", "Sun 17:00") + rowl(S, "Collected by", "Mr T. Mhlanga")
                + rowl(S, "Approved by", "Mr Chari, housemaster") + _pills(("Signed out 16:12", "campus")), w)


def sickbay_card(w=300):
    return card(S, chead(S, "first-aid-kit", "Sick bay · today", "Matron")
                + rowl(S, "Seen", "5", top=False) + rowl(S, "Back to lessons", "4") + rowl(S, "Resting", "1")
                + _pills(("Guardians told", "ok"), ("Class teachers told", "ok")), w)


# ---- stock --------------------------------------------------------------------------------------------
def stock_card(w=320):
    return card(S, chead(S, "box-3", "Stores", "Today")
                + rowl(S, "Blazer, size 34", "12 · reorder at 10", WARN, top=False) + rowl(S, "School tie", "84")
                + rowl(S, "Exercise books, A4", "1,260") + rowl(S, "Science textbook, Form 3", "36 of 120 issued")
                + _pills(("PO-0391 sent to supplier", "info")), w)


def issue_card(w=300):
    return card(S, chead(S, "book-2", "Issued to Tanaka Moyo", "Form 3B")
                + rowl(S, "Mathematics, Form 3", "Due back Nov", top=False) + rowl(S, "Combined Science, Form 3", "Due back Nov")
                + rowl(S, "Blazer, size 34", "US$45.00 to fees") + _pills(("Signed for 12 Jan", "ok")), w)


def repairs_card(w=300):
    r = "".join(f'<div style="display:flex;align-items:center;justify-content:space-between;gap:10px;padding:8px 0;border-top:{"1px solid #edeff2" if i else "0"};font-size:13px">'
                f'<span>{n}</span>{status(S, t, k)}</div>'
                for i, (n, t, k) in enumerate([("Window, Room 12", "Assigned", "info"), ("Tap, Tsavo House", "Done · US$18", "ok"), ("Projector, Lab 2", "Waiting for part", "warn")]))
    return card(S, chead(S, "tool", "Repairs", "3 open this week") + r, w)


# ---- communication ------------------------------------------------------------------------------------
def compose_card(w=340):
    chip = f'<span style="display:inline-flex;align-items:center;gap:6px;height:26px;padding:0 10px;border-radius:13px;background:#e8effd;color:{BLUE};font:500 12.5px {SANS}">{ic("group", 13, BLUE)}Form 3B guardians · 38</span>'
    return card(S, chead(S, "send-plane", "New message", "Ms Sibanda")
                + f'<div style="display:flex;align-items:center;gap:8px;font-size:12.5px;color:{MUTED}">To {chip}</div>'
                + f'<div style="margin-top:10px;padding:10px 12px;border-radius:12px;box-shadow:inset 0 0 0 1px {LINE};font:400 13.5px/1.5 {SANS};color:{INK2}">'
                  f'Sports day is on Friday 9 October. Pupils come in sports kit and bring water.</div>'
                + f'<div style="display:flex;align-items:center;justify-content:space-between;margin-top:12px"><span style="font-size:12px;color:{MUTED}">Replies go to Ms Sibanda</span>'
                  f'{cbtn("Send", "send-plane", "primary", "sm")}</div>', w)


def events_card(w=300):
    return card(S, chead(S, "calendar", "Term 3 dates", "Parent portal")
                + rowl(S, "Sports day", "Fri 9 Oct", top=False) + rowl(S, "Half term", "16–19 Oct") + rowl(S, "Form 4 exams start", "Mon 26 Oct")
                + rowl(S, "Term closes", "Thu 3 Dec") + _pills(("Reminder the day before", "campus")), w)


def read_card(w=300):
    r = "".join(f'<div style="display:flex;justify-content:space-between;padding:7px 0;border-top:1px solid #edeff2;font-size:13px"><span>{n}</span><span style="color:{MUTED}">Not opened</span></div>'
                for n in ("Mr Nyathi", "Mrs Gumbo", "Mr Zhou", "Mrs Chirwa"))
    return card(S, chead(S, "chat-3", "Sports day notice", "Form 3B")
                + f'<div style="display:flex;align-items:baseline;gap:8px">{fig(S, "34 of 38", 26)}<span style="font-size:13px;color:{MUTED}">guardians read it</span></div>'
                + f'<div style="margin-top:10px">{r}</div>' + _btns(("Remind the 4", "send-plane", "secondary")), w)


# ---- insights -----------------------------------------------------------------------------------------
def attendance_card(w=320):
    vals = [("F1", 97.1), ("F2", 96.2), ("F3", 95.4), ("F4", 94.8), ("F5", 91.6), ("F6", 97.9)]
    bars = "".join(f'<div style="flex:1;display:flex;flex-direction:column;align-items:center;gap:6px"><span style="font:500 11px {SANS};color:{INK2};{NUM}">{v:.1f}</span>'
                   f'<span style="width:22px;height:{(v - 86) * 8:.0f}px;border-radius:6px 6px 2px 2px;background:{WARN if v < 93 else BLUE}"></span>'
                   f'<span style="font:500 11.5px {SANS};color:{MUTED}">{n}</span></div>' for n, v in vals)
    return card(S, chead(S, "chart-bar", "Attendance by form", "This week", BLUE)
                + f'<div style="display:flex;align-items:flex-end;gap:6px;height:130px;padding-top:6px">{bars}</div>'
                + _pills(("Form 5 down 3 points", "warn")), w)


def collected_card(w=320):
    return card(S, chead(S, "wallet-3", "Fees collected", "Term 3", BLUE)
                + f'<div style="display:flex;align-items:baseline;gap:8px">{fig(S, "70.3%", 30)}<span style="font-size:13px;color:{MUTED}">of US$1,425,000.00 billed</span></div>'
                + f'<div style="display:flex;height:10px;border-radius:5px;overflow:hidden;margin:12px 0 4px;background:#eef0f3"><i style="width:58%;background:{BLUE}"></i><i style="width:12.3%;background:#8fb0f6"></i></div>'
                + rowl(S, "Paid in US dollars", "58.0%", top=False) + rowl(S, "Paid in ZiG", "12.3%") + rowl(S, "Outstanding", "29.7%", WARN), w)


def results_card(w=300):
    from common import MARKS
    r = "".join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:7px 0;border-top:{"1px solid #edeff2" if i else "0"};font-size:13px">'
                f'<span>{n}</span><span style="display:flex;gap:10px;align-items:center"><b style="font-weight:600;{NUM}">{avg}%</b>'
                f'{status(S, d.replace("-", "−"), "ok" if d.startswith("+") else "bad")}</span></div>' for i, (n, m, avg, d) in enumerate(MARKS[:4]))
    return card(S, chead(S, "file-check", "Results · Form 3", "Term 3", BLUE) + r + _foot("Class averages, against Term 2"), w)


# ---- school types and roles ---------------------------------------------------------------------------
def transport_card(w=300):
    return card(S, chead(S, "bus-2", "Route 4 · Mabelreign", "06:50")
                + rowl(S, "Stop 1 · Ashdown Park", "9 pupils", top=False) + rowl(S, "Stop 2 · Meyrick Park", "14 pupils") + rowl(S, "Stop 3 · Mabelreign shops", "11 pupils")
                + _pills(("Tanaka Moyo · stop 3", "campus"), ("Billed with fees", "mute")), w)


def levy_card(w=300):
    return card(S, chead(S, "wallet-3", "Fees and levies · Form 2", "Term 3")
                + rowl(S, "Tuition", "US$120.00", top=False) + rowl(S, "Building levy", "US$15.00") + rowl(S, "Sports levy", "US$5.00")
                + rowl(S, "Total", "US$140.00", INK, True) + _pills(("Set by the SDC", "mute"), ("US$ or ZiG", "info")), w)


def ai_card(w=340):
    bub = lambda t, me: (f'<div style="display:flex;justify-content:{"flex-end" if me else "flex-start"};margin-top:8px"><div style="max-width:84%;padding:9px 12px;border-radius:14px;'
                         f'background:{BLUE if me else "#f2f4f7"};color:{"#fff" if me else INK};font:400 13px/1.45 {SANS}">{t}</div></div>')
    src = (f'<span style="display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 9px;border-radius:12px;box-shadow:inset 0 0 0 1px {LINE};'
           f'font:500 11.5px {SANS};color:{INK2};margin-top:8px">{ic("book-2", 12, MUTED)}Form 2 Science notes · Mr Chari</span>')
    return card(S, chead(S, "sparkles", "Ask the library", "Student portal")
                + bub("Why does a plant cell have a cell wall?", True)
                + bub("The cell wall keeps the cell's shape and stops it bursting when it takes in water. See page 14 of your notes.", False)
                + src + _foot("Logged · the school can switch AI off"), w)


def student_card(w=300):
    return card(S, chead(S, "calendar", "Tanaka · Tuesday", "Student portal")
                + rowl(S, "07:30 · Mathematics", "Room 12", top=False) + rowl(S, "08:40 · Combined Science", "Lab 2") + rowl(S, "10:10 · English", "Room 7")
                + rowl(S, "English essay", "Due Thu", WARN) + _pills(("3 library books on loan", "campus")), w)


def approvals_card(w=300):
    r = "".join(f'<div style="display:flex;align-items:center;gap:10px;padding:8px 0;border-top:{"1px solid #edeff2" if i else "0"};font-size:13px">'
                f'{ic(icn, 15, MUTED)}<span style="flex:1">{t}</span><span style="height:26px;padding:0 10px;border-radius:13px;background:{BLUE};color:#fff;display:inline-flex;align-items:center;font:500 12px {SANS}">Approve</span></div>'
                for i, (icn, t) in enumerate([("wallet-3", "September payroll"), ("calendar", "Leave · Mrs Ncube"), ("send-plane", "Form 1 offers · 12")]))
    return card(S, chead(S, "check-circle", "Waiting for you", "Mr Dube", BLUE) + r, w)


def signin_card(w=300):
    return card(S, chead(S, "user-3", "Sign-ins", "Parent portal")
                + rowl(S, "Guardians with a sign-in", "1,804", top=False) + rowl(S, "Signed in this week", "1,377") + rowl(S, "Sent this morning", "12 new families")
                + _pills(("Works on any phone", "ok")), w)


# ---- the demo visit -----------------------------------------------------------------------------------
def plan_card(w=300):
    return card(S, chead(S, "task", "Your plan · Mukuvisi High", "Draft", BLUE)
                + rowl(S, "Setup and data capture", "Weeks 1–2", top=False) + rowl(S, "Training at the school", "Weeks 3–4")
                + rowl(S, "Active pupils", "1,140") + rowl(S, "Each month", "US$1,140.00", INK, True)
                + _pills(("First month free", "ok"), ("Setup free", "ok")), w)


def visitors_card(w=320):
    import portal_art
    ppl = [("Mr Dube", "Head", "Administration"), ("Mrs Gumbo", "Bursar", "Administration"), ("Ms Sibanda", "Form 3B teacher", "Teacher"),
           ("Mr Chari", "Housemaster, Tsavo House", "Administration")]
    r = "".join(f'<div style="display:flex;align-items:center;gap:10px;padding:8px 0;border-top:{"1px solid #edeff2" if i else "0"}">{portal_art.portal_icon(p, 28)}'
                f'<div style="flex:1;min-width:0"><div style="font:600 13px {SANS}">{n}</div><div style="font:400 12px {SANS};color:{MUTED}">{role}</div></div>'
                f'{status(S, "Coming", "ok")}</div>' for i, (n, role, p) in enumerate(ppl))
    return card(S, chead(S, "calendar", "Demo · Thu 8 Oct, 14:00", "Mukuvisi High") + r
                + f'<div style="margin-top:8px;padding:8px 10px;border-radius:12px;background:#f2f4f7;font-size:12.5px;color:{INK2}">Forms, fee structure and staff list loaded</div>', w)


def thread_card(w=340):
    bub = lambda who, t, me: (f'<div style="margin-top:10px;display:flex;flex-direction:column;align-items:{"flex-end" if me else "flex-start"}">'
                              f'<span style="font:500 11.5px {SANS};color:{MUTED};margin-bottom:4px">{who}</span>'
                              f'<div style="max-width:88%;padding:9px 12px;border-radius:14px;background:{"#f2f4f7" if me else BLUE};color:{INK if me else "#fff"};font:400 13px/1.45 {SANS}">{t}</div></div>')
    return card(S, chead(S, "mail", "Two campuses", "Pricing")
                + bub("Chipo Mutasa · Mukuvisi High", "We run a junior and a senior campus. Is that one school on Campus, or two?", True)
                + bub("Campus team", "One school and one record, with both campuses in it, at US$1 per active pupil per month.", False)
                + _pills(("Replied by email", "ok")), w)


# ---- the integrations marketplace, as the Administration portal shows it -----------------------------
MARKET = [("Accounting", [("Sage Pastel", "Journals and the ledger", "on"), ("QuickBooks", "Invoices, payments and journals", ""), ("Xero", "Journals and bank feeds", "")]),
          ("Tax", [("ZIMRA fiscalisation", "Fiscal receipts through FDMS", "on")]),
          ("Payments", [("EcoCash", "Fees paid from a phone", "on")]),
          ("Messaging", [("WhatsApp", "Notices and receipts to guardians", ""), ("Gmail", "School email from Campus", "")]),
          ("Work and learning", [("Google Workspace", "Sign in with the school's Google accounts", ""), ("Microsoft 365", "Sign in with the school's Microsoft accounts", ""),
                                 ("Google Meet", "Online lessons from the timetable", ""), ("Microsoft Teams", "Online lessons from the timetable", ""),
                                 ("Google Drive", "Files on the pupil's record", ""), ("Excel", "Export any list", "on")])]


def marketplace(w=1200):
    import brands
    cats = ["All"] + [c for c, _ in MARKET]
    side = "".join(f'<div style="display:flex;justify-content:space-between;align-items:center;height:36px;padding:0 12px;border-radius:10px;{"background:#fff;box-shadow:0 0 0 1px " + LINE + ";" if i == 0 else ""}'
                   f'font:{"600" if i == 0 else "500"} 13.5px {SANS};color:{INK if i == 0 else INK2}">{c}<span style="font:400 12px {SANS};color:{MUTED}">'
                   f'{sum(len(x) for _, x in MARKET) if i == 0 else len(MARKET[i - 1][1])}</span></div>' for i, c in enumerate(cats))
    tiles = ""
    for cat, items in MARKET:
        for n, d, st in items:
            act = (f'<span style="display:inline-flex;align-items:center;gap:5px;height:28px;padding:0 10px;border-radius:14px;background:{OKS};color:{OK};font:500 12px {SANS}">{ic("check-line", 12, OK)}Connected</span>'
                   if st else f'<span style="display:inline-flex;align-items:center;height:28px;padding:0 12px;border-radius:14px;box-shadow:inset 0 0 0 1px {LINE};font:500 12px {SANS};color:{INK}">Add</span>')
            tiles += (f'<div style="display:flex;flex-direction:column;gap:10px;padding:16px;border-radius:14px;background:#fff;box-shadow:0 0 0 1px {LINE}">'
                      f'<div style="display:flex;justify-content:space-between;align-items:flex-start">{brands.logo(n, 34)}{act}</div>'
                      f'<div><div style="font:600 14px {SANS}">{n}</div><div style="font:400 12.5px/1.45 {SANS};color:{MUTED};margin-top:3px">{d}</div></div>'
                      f'<div style="margin-top:auto;font:400 11.5px {SANS};color:{FAINT}">{cat}</div></div>')
    tiles += (f'<div style="display:flex;flex-direction:column;align-items:flex-start;gap:10px;padding:16px;border-radius:14px;border:1.5px dashed #c9ced6">'
              f'<span style="width:34px;height:34px;border-radius:10px;background:#e8effd;display:flex;align-items:center;justify-content:center">{ic("add-line", 18, BLUE)}</span>'
              f'<div><div style="font:600 14px {SANS}">Ask for an integration</div><div style="font:400 12.5px/1.45 {SANS};color:{MUTED};margin-top:3px">Tell us what your school uses</div></div></div>')
    top = (f'<div style="display:flex;align-items:center;gap:14px;padding:16px 22px;border-bottom:1px solid {LINE}">{pmark("Campus", 28, 8)}'
           f'<span style="font:600 15px {SANS}">Integrations</span><span style="flex:1"></span>'
           f'<span style="display:flex;align-items:center;gap:8px;width:280px;height:36px;padding:0 12px;border-radius:18px;background:#f2f4f7;font:400 13px {SANS};color:{FAINT}">{ic("search", 15, MUTED)}Search integrations</span></div>')
    body = (f'<div style="display:flex"><div style="width:200px;padding:18px 14px;border-right:1px solid {LINE};background:#fafbfc;display:flex;flex-direction:column;gap:4px">{side}</div>'
            f'<div style="flex:1;padding:20px;display:grid;grid-template-columns:repeat(4,1fr);gap:14px;background:#fafbfc">{tiles}</div></div>')
    return f'<div style="width:{w}px;border-radius:20px;overflow:hidden;background:#fff;box-shadow:0 0 0 1px {LINE},0 30px 60px -30px rgba(11,12,20,.35)">{top}{body}</div>'

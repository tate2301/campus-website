# -*- coding: utf-8 -*-
"""Campus product UI, drawn from one world in three signatures:
A trays (Inter, white cards in grey trays), B pills (Atkinson, big figures, round status pills),
C ledger (serif figures, mono labels, hairline rules, no fills)."""
from common import *

SIGS = {
    "a": dict(key="a", font=UI, fig=f"600 {{s}}px/1 {UI}", figk=1.0, card="#fff", tray=TRAY, r=10, bd=f"box-shadow:0 0 0 1px {LINE};",
              sh="box-shadow:0 0 0 1px #e3e6eb,0 18px 40px -24px rgba(11,12,20,.28);", lab=f"500 12px {UI}", labc=MUTED, gap=10),
    "b": dict(key="b", font=SANS, fig=f"600 {{s}}px/1 {SANS}", figk=1.2, card="#fff", tray="#f4f5f7", r=16, bd="",
              sh="box-shadow:0 1px 2px rgba(11,12,20,.06),0 16px 36px -18px rgba(11,12,20,.30);", lab=f"500 13px {SANS}", labc=MUTED, gap=12),
    "c": dict(key="c", font=SANS, fig=f"500 {{s}}px/1 {SERIF}", figk=1.25, card="#fff", tray="#fff", r=3, bd=f"box-shadow:0 0 0 1px #d9dce3;",
              sh="box-shadow:0 0 0 1px #d4d8df;", lab=f"400 11px {MONO}", labc=MUTED, gap=0),
}


def lab(S, t, c=None):
    return f'<span style="font:{S["lab"]};color:{c or S["labc"]}">{t}</span>'


def fig(S, v, s=28, c=INK):
    return f'<span style="font:{S["fig"].format(s=round(s * S["figk"]))};color:{c};letter-spacing:{"-0.02em" if S["key"] != "c" else "0"};{NUM}">{v}</span>'


def status(S, t, kind="ok"):
    c, bg = {"ok": (OK, OKS), "warn": (WARN, WARNS), "bad": (BAD, BADS), "info": (BLUE, "#e8effd"), "mute": (INK2, "#eef0f3"), "campus": (CAMPUS, "#efeaff")}[kind]
    if S["key"] == "a":
        return f'<span style="display:inline-flex;align-items:center;height:20px;padding:0 7px;border-radius:5px;background:{bg};font:500 11.5px {UI};color:{c};white-space:nowrap">{t}</span>'
    if S["key"] == "b":
        return (f'<span style="display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 10px 0 8px;border-radius:999px;background:{bg};font:500 12.5px {SANS};color:{c};white-space:nowrap">'
                f'<i style="width:6px;height:6px;border-radius:3px;background:{c}"></i>{t}</span>')
    return f'<span style="display:inline-flex;align-items:center;gap:6px;font:400 11px {MONO};color:{c};white-space:nowrap"><i style="width:7px;height:7px;background:{c}"></i>{t}</span>'


def card(S, inner, w=None, pad=16, extra="", shadow=True):
    ww = f"width:{w}px;" if w else ""
    return (f'<div style="{ww}box-sizing:border-box;background:{S["card"]};border-radius:{S["r"]}px;{S["sh"] if shadow else S["bd"]}padding:{pad}px;'
            f'font-family:{S["font"]};color:{INK};{extra}">{inner}</div>')


def rowl(S, a, b, c=INK, bold=False, top=True):
    bt = f"border-top:1px solid {'#e3e6eb' if S['key'] != 'c' else '#e6e8ec'};" if top else ""
    bf = f"font-family:{SERIF};font-size:{15 if bold else 14}px;" if S["key"] == "c" else ""
    return (f'<div style="display:flex;justify-content:space-between;align-items:center;gap:12px;padding:8px 0;{bt}font-size:13px;color:{c}">'
            f'<span>{a}</span><span style="font-weight:{600 if bold else 500};{NUM}{bf}">{b}</span></div>')


def chead(S, icon, title, meta="", hue=CAMPUS):
    tile = (f'<span style="width:22px;height:22px;border-radius:{6 if S["key"] != "c" else 2}px;background:{hue};display:flex;align-items:center;justify-content:center">{ic(icon, 13, "#fff")}</span>'
            if S["key"] != "c" else ic(icon, 16, INK))
    return (f'<div style="display:flex;align-items:center;gap:8px;margin-bottom:10px;white-space:nowrap">{tile}<span style="font:600 13.5px {S["font"]};color:{INK};overflow:hidden;text-overflow:ellipsis">{title}</span>'
            f'<span style="flex:1"></span>{lab(S, meta)}</div>')


# ---- small cards for the section pictures ------------------------------------------------------
def register_card(S, w=300, offline=True):
    rows = "".join(f'<div style="display:flex;align-items:center;gap:10px;padding:7px 0;border-top:1px solid #edeff2;font-size:13px">'
                   f'<span style="flex:1">{n}</span>{status(S, {"P": "Present", "A": "Absent", "L": "Late"}[m], {"P": "ok", "A": "bad", "L": "warn"}[m])}</div>'
                   for n, m in FORM3B[:5])
    band = (f'<div style="display:flex;align-items:center;gap:8px;margin:0 0 10px;padding:8px 10px;border-radius:{max(2, S["r"] - 4)}px;background:{WARNS};font-size:12px;color:{WARN}">'
            f'{ic("wifi-off", 14, WARN)}Saved on this tablet · syncs when online</div>') if offline else ""
    return card(S, chead(S, "book-6", "Form 3B register", "07:42") + band + rows
                + f'<div style="display:flex;justify-content:space-between;padding-top:10px;border-top:1px solid #edeff2;font-size:12.5px;color:{MUTED}"><span>36 present · 1 late · 1 absent</span><span>38</span></div>', w)


def sync_card(S, w=280):
    return card(S, chead(S, "refresh-2", "Synced to the school", "08:05", OK)
                + rowl(S, "Registers", "3 from Block C", top=False) + rowl(S, "Marks", "38 entries") + rowl(S, "Receipts", "2 from the bursary")
                + f'<div style="margin-top:8px">{status(S, "The office has the same figures now", "ok")}</div>', w)


def marks_card(S, w=300):
    return card(S, chead(S, "file-check", "Mathematics · test 2", "24 Sep")
                + rowl(S, "Tanaka Moyo", "71%", top=False, bold=True) + rowl(S, "Tendai Chirwa", "58%") + rowl(S, "Ruvimbo Gumbo", "77%")
                + rowl(S, "Class average", "64%", MUTED)
                + f'<div style="margin-top:8px;font-size:12px;color:{MUTED}">Recorded once by Ms Sibanda</div>', w)


def fee_card(S, w=320):
    return card(S, chead(S, "wallet-3", "Tanaka Moyo · fees", "Term 3")
                + rowl(S, "Term fee", "US$1,250.00", top=False) + rowl(S, "EcoCash, 14 Sep", "−US$500.00", OK) + rowl(S, "Bank transfer, 22 Sep", "−US$330.00", OK)
                + rowl(S, "Balance", "US$420.00", INK, True)
                + f'<div style="display:flex;gap:8px;margin-top:8px">{status(S, "Due Fri 16 Oct", "warn")}{status(S, "R-2026-18824", "mute")}</div>', w)


def report_card(S, w=300):
    return card(S, chead(S, "file-check", "Term 3 report · Tanaka", "Draft")
                + "".join(rowl(S, n, f"{m}%", top=(i > 0)) for i, (n, m, a, d) in enumerate(MARKS[:4]))
                + f'<div style="margin-top:8px">{status(S, "Ready when the term closes", "campus")}</div>', w)


def head_card(S, w=300):
    return card(S, chead(S, "chart-bar", "The Head's view", "07:58", BLUE)
                + f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">'
                + f'<div>{lab(S, "Attendance")}<div style="margin-top:6px">{fig(S, "96.4%", 22)}</div></div>'
                + f'<div>{lab(S, "Fees collected")}<div style="margin-top:6px">{fig(S, "70.3%", 22)}</div></div></div>'
                + f'<div style="margin-top:10px;font-size:12px;color:{MUTED}">Mathematics, Form 3: average up 6 points</div>', w)


def phone(S, inner, w=260, h=520, dark=False):
    frame = "#16181d"
    return (f'<div style="width:{w}px;height:{h}px;border-radius:{round(w * 0.16)}px;background:{frame};padding:9px;box-sizing:border-box;'
            f'box-shadow:0 30px 60px -30px rgba(11,12,20,.5)"><div style="width:100%;height:100%;border-radius:{round(w * 0.13)}px;overflow:hidden;background:#fff;position:relative;font-family:{S["font"]}">'
            f'<div style="position:absolute;top:8px;left:50%;transform:translateX(-50%);width:{round(w * 0.28)}px;height:{round(w * 0.075)}px;border-radius:99px;background:{frame}"></div>'
            f'{inner}</div></div>')


def parent_screen(S, w=260):
    s = w / 260
    inner = (f'<div style="padding:{round(40 * s)}px 16px 16px;display:flex;flex-direction:column;gap:12px">'
             f'<div style="display:flex;align-items:center;gap:10px"><div style="width:34px;height:34px;border-radius:17px;background:#efeaff;display:flex;align-items:center;justify-content:center;font:600 13px {SANS};color:{CAMPUS}">TM</div>'
             f'<div style="white-space:nowrap"><div style="font:600 15px {S["font"]}">Tanaka Moyo</div><div style="font-size:12px;color:{MUTED}">Form 3B · Tsavo House</div></div></div>'
             f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">'
             f'<div style="background:{PLATE};border-radius:{max(3, S["r"] - 4)}px;padding:10px;white-space:nowrap">{lab(S, "This week")}<div style="margin-top:6px">{fig(S, "5 of 5", round(18 * s))}</div><div style="font-size:11px;color:{MUTED};margin-top:4px">days present</div></div>'
             f'<div style="background:{PLATE};border-radius:{max(3, S["r"] - 4)}px;padding:10px;white-space:nowrap">{lab(S, "Balance")}<div style="margin-top:6px">{fig(S, "US$420", round(18 * s))}</div><div style="font-size:11px;color:{MUTED};margin-top:4px">due 16 Oct</div></div></div>'
             f'<div style="font:600 13px {S["font"]};margin-top:4px">Latest marks</div>'
             + "".join(f'<div style="display:flex;justify-content:space-between;font-size:12.5px;padding:6px 0;border-top:1px solid #eef0f3"><span>{n}</span><span style="font-weight:600;{NUM}">{m}%</span></div>' for n, m, a, d in MARKS[:3])
             + f'<div style="padding:10px;border-radius:{max(3, S["r"] - 4)}px;background:#e8effd;font-size:12px;color:#1d4ed8">Ms Sibanda: Tanaka did well on test 2. Keep up the practice on algebra.</div></div>')
    return phone(S, inner, w, round(w * 2.05))


# ---- the in-use pieces (busiest screen, phone task, message) ------------------------------------
NAV = [("chart-bar", "Head's view"), ("user-3", "Pupils"), ("wallet-3", "Fees and accounting"), ("moon", "Boarding"), ("bank-card", "Payroll"),
       ("contacts-2", "Staff"), ("box-3", "Stock"), ("tool", "Maintenance"), ("message-3", "Communication")]


def head_view(S, w=1280, h=800):
    k = S["key"]
    if k == "b":
        return head_view_b(S, w, h)
    SC = f'<span style="flex:1"></span><span style="font:400 11px {MONO};color:{MUTED}">1</span>'
    side_bg = {"a": "#f6f7f9", "b": "#fff", "c": "#fff"}[k]
    nav = "".join(f'<div style="display:flex;align-items:center;gap:10px;height:34px;padding:0 10px;border-radius:{min(8, S["r"])}px;'
                  f'{"background:" + ("#fff;box-shadow:0 0 0 1px " + LINE if k == "a" else ("#eef3fe" if k == "b" else "none")) + ";" if i == 0 else ""}'
                  f'font:{"600" if i == 0 else "400"} 13.5px {S["font"]};color:{BLUE if (i == 0 and k == "b") else (INK if i == 0 else INK2)}">'
                  f'{ic(icn, 16, BLUE if (i == 0 and k != "c") else INK2)}{t}</div>'
                  for i, (icn, t) in enumerate(NAV))
    side = (f'<div style="width:232px;flex:none;background:{side_bg};border-right:1px solid {LINE};padding:18px 14px;box-sizing:border-box;display:flex;flex-direction:column;gap:18px">'
            f'{lockup(20, by=False)}'
            f'<div style="display:flex;align-items:center;gap:8px;padding:8px 10px;border-radius:8px;box-shadow:0 0 0 1px {LINE};background:#fff;font:500 13px {S["font"]}">'
            f'<span style="width:22px;height:22px;border-radius:6px;background:#0b0c14;color:#fff;display:flex;align-items:center;justify-content:center;font:600 10px {SANS}">MH</span>{SCHOOL}</div>'
            f'<div style="display:flex;flex-direction:column;gap:2px">{nav}</div><span style="flex:1"></span>'
            f'<div style="display:flex;align-items:center;gap:8px;font-size:12px;color:{MUTED}">{ic("refresh-2", 14, OK)}Synced at 07:58</div></div>')

    kpis = [("Attendance today", "96.4%", "1,099 of 1,140 pupils", ("ok", "+0.8 on last week")),
            ("Fees collected", "US$612,400", "70.3% of US$871,500 due", ("info", "Term 3, week 4")),
            ("Boarders on roll", "212", "4 on exeat this weekend", ("mute", "Tsavo and Kariba")),
            ("Maintenance", "3 open", "oldest open 9 days", ("warn", "1 overdue"))]

    def kpi(t, v, sub, st):
        inner = (f'{lab(S, t)}<div style="margin:10px 0 6px">{fig(S, v, 26)}</div><div style="font-size:12.5px;color:{MUTED}">{sub}</div>'
                 f'<div style="margin-top:10px">{status(S, st[1], st[0])}</div>')
        if k == "c":
            return f'<div style="padding:16px 18px;border-right:1px solid #e3e6eb">{inner}</div>'
        return card(S, inner, pad=16)
    krow = "".join(kpi(*x) for x in kpis)
    krow = (f'<div style="display:grid;grid-template-columns:repeat(4,1fr);{"gap:14px" if k != "c" else "border-top:1px solid " + INK + ";border-bottom:1px solid #e3e6eb"}">{krow}</div>')

    # fees collected by week, cumulative, against the amount due
    weeks = [("Wk 1", 214800), ("Wk 2", 389600), ("Wk 3", 521300), ("Wk 4", 612400)]
    due = 871500
    bars = ""
    for i, (wl, v) in enumerate(weeks):
        hh = round(150 * v / due)
        col = BLUE if i == 3 else ("#c7d5f8" if k != "c" else "#b9bec8")
        bars += (f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px;flex:1">'
                 f'<span style="font:500 12px {S["font"]};color:{INK2};{NUM}">{v / 1000:.0f}k</span>'
                 f'<div style="width:46px;height:150px;display:flex;align-items:flex-end;background:{"#f1f3f6" if k != "c" else "none"};border-radius:{min(6, S["r"])}px;{"border-bottom:1px solid " + INK if k == "c" else ""}">'
                 f'<div style="width:100%;height:{hh}px;background:{col};border-radius:{min(6, S["r"])}px {min(6, S["r"])}px 0 0"></div></div>'
                 f'<span style="font:{S["lab"]};color:{MUTED}">{wl}</span></div>')
    chart_inner = (f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font:600 14px {S["font"]}">Fees collected this term</span>{lab(S, "cumulative · US$")}</div>'
                   f'<div style="display:flex;gap:10px;margin-top:18px;align-items:flex-end">{bars}'
                   f'<div style="flex:1.4;display:flex;flex-direction:column;gap:10px;padding-left:14px;border-left:1px solid #e6e8ec">'
                   f'{lab(S, "Due this term")}{fig(S, "US$871,500", 18)}{lab(S, "Still to collect")}{fig(S, "US$259,100", 18, WARN)}</div></div>')
    forms = [("Form 1", 97.1), ("Form 2", 94.2), ("Form 3", 96.8), ("Form 4", 97.5), ("Lower 6", 96.0), ("Upper 6", 98.3)]
    att_inner = (f'<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="font:600 14px {S["font"]}">Attendance by form</span>{lab(S, "today")}</div>'
                 + "".join(f'<div style="display:flex;align-items:center;gap:12px;padding:{7 if k == "a" else 9}px 0;border-top:{"1px solid #eef0f3" if i else "none"};font-size:13px">'
                           f'<span style="width:70px">{f}</span><div style="flex:1;height:6px;border-radius:3px;background:#eef0f3;overflow:hidden">'
                           f'<div style="width:{(p - 85) / 15 * 100:.0f}%;height:6px;background:{WARN if p < 95 else (BLUE if k != "c" else INK)}"></div></div>'
                           f'<span style="width:44px;text-align:right;font-weight:500;{NUM}">{p}%</span></div>' for i, (f, p) in enumerate(forms)))
    attn = [("warn", "Form 2C attendance is 88% this week", "Class teacher Mr Dube has been asked to call three families"),
            ("bad", "46 accounts over 60 days in arrears", "US$38,900 outstanding · reminders go out Friday"),
            ("warn", "Science lab extractor fan", "Job MJ-0142, open 9 days, parts ordered from Msasa"),
            ("info", "Form 4 mock timetable ready for approval", "Sent by Mr Ncube, deputy head, at 07:40")]
    att_list = "".join(f'<div style="display:flex;gap:10px;padding:11px 0;border-top:{"1px solid #eef0f3" if i else "none"}">'
                       f'<i style="width:8px;height:8px;border-radius:{4 if k != "c" else 0}px;margin-top:5px;flex:none;background:{ {"warn": WARN, "bad": BAD, "info": BLUE}[kd] }"></i>'
                       f'<div><div style="font:500 13.5px {S["font"]};color:{INK}">{t}</div><div style="font-size:12.5px;color:{MUTED};margin-top:2px">{s}</div></div></div>'
                       for i, (kd, t, s) in enumerate(attn))
    attn_inner = f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px"><span style="font:600 14px {S["font"]}">Needs your attention</span>{lab(S, "4")}</div>{att_list}'
    today = [("07:30", "Registers closed", "62 of 64 classes marked; Form 5A and 6B late"), ("08:05", "Fees received since 06:00", "12 payments, 9 by EcoCash, 1 in ZiG"),
             ("14:30", "SDC finance meeting", "Term 3 collections pack attached")]
    today_inner = (f'<div style="display:flex;justify-content:space-between;align-items:baseline;margin-bottom:6px"><span style="font:600 14px {S["font"]}">Today</span>{lab(S, "Wed 30 Sep")}</div>'
                   + "".join(f'<div style="display:flex;gap:12px;padding:10px 0;border-top:{"1px solid #eef0f3" if i else "none"}">'
                             f'<span style="width:40px;flex:none;font:{S["lab"]};color:{MUTED};padding-top:2px">{t}</span>'
                             f'<div><div style="font:500 13.5px {S["font"]}">{a}</div><div style="font-size:12.5px;color:{MUTED};margin-top:2px">{b}</div></div></div>'
                             for i, (t, a, b) in enumerate(today)))

    def panel(inner, extra=""):
        if k == "c":
            return f'<div style="padding:18px 0;border-bottom:1px solid #e3e6eb;{extra}">{inner}</div>'
        return card(S, inner, pad=18, extra=extra)

    title = ("Good morning, Mrs Mutasa" if k != "c" else "The Head's view")
    sub = f"{TODAY} · Term 3, week 4 · {SCHOOL}"
    top = (f'<div style="display:flex;align-items:flex-end;justify-content:space-between;gap:20px">'
           f'<div><div style="font:{"600 24px" if k != "c" else "500 30px"} {S["font"] if k != "c" else SERIF};letter-spacing:{"-0.02em" if k != "c" else "-0.01em"}">{title}</div>'
           f'<div style="margin-top:6px;font:{S["lab"] if k == "c" else "400 13.5px " + S["font"]};color:{MUTED}">{sub}</div></div>'
           f'<div style="display:flex;gap:10px">{btn("Export for the SDC", "download-2", "ghost", 38, 13.5)}{btn("Send a circular", "message-3", "primary", 38, 13.5)}</div></div>')
    main = (f'<div style="flex:1;min-width:0;background:{S["tray"] if k == "a" else "#fff"};padding:26px 30px;box-sizing:border-box;display:flex;flex-direction:column;gap:{18 if k != "c" else 6}px">'
            f'{top}{krow}<div style="display:grid;grid-template-columns:1.25fr 1fr;gap:{16 if k != "c" else 36}px">'
            f'<div style="display:flex;flex-direction:column;gap:{16 if k != "c" else 0}px">{panel(chart_inner)}{panel(att_inner)}</div>'
            f'<div style="display:flex;flex-direction:column;gap:{16 if k != "c" else 0}px">{panel(attn_inner)}{panel(today_inner)}</div></div></div>')
    return (f'<div style="width:{w}px;height:{h}px;display:flex;background:#fff;border-radius:{14 if k != "c" else 4}px;overflow:hidden;'
            f'box-shadow:0 0 0 1px {LINE};font-family:{S["font"]};color:{INK}">{side}{main}</div>')


def register_phone(S, w=390, h=844):
    k = S["key"]
    marks = {"P": ("P", OK, OKS), "A": ("A", BAD, BADS), "L": ("L", WARN, WARNS)}

    def toggle(m):
        out = ""
        for o in "PLA":
            on = o == m
            c, bg = marks[o][1], marks[o][2]
            if k == "c":
                out += f'<span style="width:30px;height:30px;display:flex;align-items:center;justify-content:center;font:500 13px {MONO};border:1px solid {c if on else "#dfe2e7"};color:{c if on else FAINT};background:{bg if on else "#fff"}">{o}</span>'
            elif k == "b":
                out += (f'<span style="height:30px;padding:0 11px;border-radius:15px;display:flex;align-items:center;font:600 12.5px {SANS};'
                        f'background:{c if on else "transparent"};color:{"#fff" if on else FAINT}">{ {"P": "Here", "L": "Late", "A": "Away"}[o] }</span>')
            else:
                out += (f'<span style="width:34px;height:34px;border-radius:{17 if k == "b" else 8}px;display:flex;align-items:center;justify-content:center;'
                        f'font:600 13px {S["font"]};background:{c if on else "#f1f3f6"};color:{"#fff" if on else FAINT}">{o}</span>')
        if k == "b":
            return f'<div style="display:flex;padding:3px;border-radius:18px;background:#f1f3f6">{out}</div>'
        return f'<div style="display:flex;gap:6px">{out}</div>'
    rows = "".join(f'<div style="display:flex;align-items:center;gap:12px;padding:10px 20px;border-top:1px solid #eef0f3">'
                   f'<span style="width:32px;height:32px;border-radius:{16 if k != "c" else 2}px;background:#eef0f3;display:flex;align-items:center;justify-content:center;font:600 11px {SANS};color:{INK2}">{"".join(p[0] for p in n.split())}</span>'
                   f'<span style="flex:1;font:500 15px {S["font"]}">{n}</span>{toggle(m)}</div>' for n, m in FORM3B)
    counts = [("Present", "36", OK), ("Late", "1", WARN), ("Absent", "1", BAD)]
    cbar = "".join(f'<div style="flex:1;padding:10px 12px;{"border-radius:12px;background:#f6f7f9;" if k != "c" else "border-right:1px solid #e3e6eb;"}">'
                   f'{lab(S, t)}<div style="margin-top:4px">{fig(S, v, 22, c)}</div></div>' for t, v, c in counts)
    inner = (f'<div style="padding:54px 20px 12px;display:flex;flex-direction:column;gap:14px">'
             f'<div style="display:flex;align-items:center;gap:10px">{ic("left-line", 20, INK)}<div style="flex:1"><div style="font:600 19px {S["font"]}">Form 3B register</div>'
             f'<div style="font-size:13px;color:{MUTED};margin-top:2px">Wednesday 30 Sep · Period 1 · Ms Sibanda</div></div></div>'
             f'<div style="display:flex;align-items:center;gap:8px;padding:10px 12px;border-radius:{12 if k != "c" else 2}px;background:{WARNS};color:{WARN};font-size:13px">'
             f'{ic("wifi-off", 16, WARN)}No internet. Saved on this phone; it syncs when you are back online.</div>'
             f'<div style="display:flex;gap:8px">{cbar}</div></div>'
             f'<div>{rows}</div>'
             f'<div style="padding:10px 20px;font-size:13px;color:{MUTED}">28 more pupils</div>'
             f'<div style="position:absolute;left:0;right:0;bottom:0;padding:14px 20px 26px;background:#fff;border-top:1px solid {LINE}">'
             f'<div style="height:50px;border-radius:{12 if k != "c" else 3}px;background:{BLUE};color:#fff;display:flex;align-items:center;justify-content:center;gap:8px;font:600 16px {S["font"]}">'
             f'Submit register{ic("check-line", 18, "#fff")}</div></div>')
    return phone(S, inner, w, h)


def parent_message(S, w=620, h=None):
    k = S["key"]
    body = (f'<div style="padding:26px 30px;display:flex;flex-direction:column;gap:16px;font-family:{S["font"]}">'
            f'<div style="display:flex;align-items:center;gap:12px">{pmark("Campus", 36, 9)}<div style="flex:1"><div style="font:600 14px {S["font"]}">{SCHOOL}</div>'
            f'<div style="font-size:12.5px;color:{MUTED}">via Corelith Campus · to Rudo Moyo</div></div><span style="font:{S["lab"]};color:{MUTED}">16:10</span></div>'
            f'<div style="font:{"600 22px " + S["font"] if k != "c" else "500 26px " + SERIF};letter-spacing:-0.015em">Tanaka scored 71% in Mathematics test 2</div>'
            f'<div style="font-size:15px;line-height:1.55;color:{INK2}">Ms Sibanda marked Form 3B\'s second Mathematics test on 24 September. The class average was 64%. '
            f'Tanaka\'s strongest section was algebra.</div>'
            f'<div style="display:grid;grid-template-columns:repeat(3,1fr);{"gap:10px" if k != "c" else "border-top:1px solid #e3e6eb;border-bottom:1px solid #e3e6eb"}">'
            + "".join(f'<div style="padding:12px 14px;{"border-radius:" + str(max(4, S["r"] - 4)) + "px;background:" + PLATE if k != "c" else ("border-right:1px solid #e3e6eb" if i < 2 else "")}">'
                      f'{lab(S, t)}<div style="margin-top:6px">{fig(S, v, 20)}</div></div>'
                      for i, (t, v) in enumerate([("Test 2", "71%"), ("Class average", "64%"), ("Attendance, term", "97%")]))
            + f'</div><div style="display:flex;align-items:center;gap:10px;padding:12px 14px;border-radius:{max(3, S["r"] - 4)}px;background:{WARNS};font-size:13.5px;color:{WARN}">'
            f'{ic("wallet-3", 16, WARN)}Term 3 balance US$420.00, due Friday 16 October</div>'
            f'<div style="display:flex;gap:10px">{btn("Open the parent portal", "right-line", "primary", 42, 14)}{btn("Message Ms Sibanda", "message-3", "ghost", 42, 14)}</div></div>')
    return (f'<div style="width:{w}px;background:#fff;border-radius:{14 if k != "c" else 4}px;box-shadow:0 0 0 1px {LINE},0 24px 50px -30px rgba(11,12,20,.3);overflow:hidden;color:{INK}">'
            f'<div style="height:40px;background:#f6f7f9;border-bottom:1px solid {LINE};display:flex;align-items:center;gap:8px;padding:0 16px">'
            + "".join(f'<i style="width:10px;height:10px;border-radius:5px;background:#dfe2e7"></i>' for _ in range(3))
            + f'<span style="margin-left:10px;font:400 12.5px {S["font"]};color:{MUTED}">Inbox</span></div>{body}</div>')


def head_view_b(S, w=1280, h=800):
    """B: top navigation, two large figure cards, pills everywhere, a two-column attention list"""
    F = SANS
    navs = "".join(f'<span style="display:inline-flex;align-items:center;gap:7px;height:34px;padding:0 14px;border-radius:17px;'
                   f'{"background:#eef3fe;color:" + BLUE if i == 0 else "color:" + INK2};font:{"600" if i == 0 else "500"} 13.5px {F}">'
                   f'{ic(icn, 15, BLUE if i == 0 else MUTED) if i == 0 else ""}{t}</span>'
                   for i, (icn, t) in enumerate(NAV[:7]))
    topbar = (f'<div style="height:64px;display:flex;align-items:center;gap:22px;padding:0 28px;border-bottom:1px solid {LINE};background:#fff">'
              f'{lockup(20, by=False)}<div style="display:flex;gap:2px">{navs}<span style="display:inline-flex;align-items:center;gap:4px;height:34px;padding:0 12px;color:{INK2};font:500 13.5px {F}">More{ic("down-line", 14, MUTED)}</span></div>'
              f'<span style="flex:1"></span>{status(S, "Synced 07:58", "ok")}'
              f'<span style="width:34px;height:34px;border-radius:17px;background:#efeaff;color:{CAMPUS};display:flex;align-items:center;justify-content:center;font:600 12px {F}">CM</span></div>')
    greet = (f'<div style="display:flex;align-items:flex-end;justify-content:space-between">'
             f'<div><div style="font:600 30px/1.1 {F};letter-spacing:-0.025em">Good morning, Mrs Mutasa</div>'
             f'<div style="margin-top:8px;font:400 14px {F};color:{MUTED}">{TODAY} · Term 3, week 4 · {SCHOOL}</div></div>'
             f'<div style="display:flex;gap:10px">{btn("Export for the SDC", "download-2", "ghost", 40, 14).replace("border-radius:8px", "border-radius:20px")}'
             f'{btn("Send a circular", "message-3", "primary", 40, 14).replace("border-radius:8px", "border-radius:20px")}</div></div>')
    # attendance: big figure + a pill column per form
    forms = [("F1", 97.1), ("F2", 94.2), ("F3", 96.8), ("F4", 97.5), ("L6", 96.0), ("U6", 98.3)]
    cols = "".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px">'
                   f'<span style="font:500 11.5px {F};color:{INK2};{NUM}">{p:.0f}%</span>'
                   f'<div style="width:22px;height:92px;border-radius:11px;background:#f1f3f6;display:flex;align-items:flex-end;overflow:hidden">'
                   f'<div style="width:22px;height:{round(92 * (p - 88) / 12)}px;border-radius:11px;background:{WARN if p < 95 else BLUE}"></div></div>'
                   f'<span style="font:500 11.5px {F};color:{MUTED}">{f}</span></div>' for f, p in forms)
    att = card(S, f'<div style="display:flex;justify-content:space-between">{lab(S, "Attendance today")}{status(S, "+0.8 on last week", "ok")}</div>'
                  f'<div style="display:flex;align-items:flex-end;justify-content:space-between;margin-top:14px">'
                  f'<div>{fig(S, "96.4%", 46)}<div style="margin-top:10px;font-size:14px;color:{MUTED}">1,099 of 1,140 pupils</div>'
                  f'<div style="margin-top:14px">{status(S, "Form 2 below 95%", "warn")}</div></div>'
                  f'<div style="display:flex;gap:12px">{cols}</div></div>'
                  f'<div style="display:flex;gap:10px;padding-top:16px;border-top:1px solid #eef0f3">{status(S, "41 absent", "mute")}{status(S, "29 with a reason from home", "mute")}</div>', pad=22,
               extra="display:flex;flex-direction:column;justify-content:space-between")
    # fees: big figure + a pill progress bar in weeks
    wk = [214800, 389600, 521300, 612400]
    seg = "".join(f'<div style="position:absolute;left:0;top:0;bottom:0;width:{v / 871500 * 100:.1f}%;border-radius:10px;background:{BLUE if i == 3 else ("#c7d5f8" if i == 2 else ("#dbe5fb" if i == 1 else "#e8effd"))};z-index:{4 - i}"></div>'
                  for i, v in enumerate(wk))
    fees = card(S, f'<div style="display:flex;justify-content:space-between">{lab(S, "Fees collected this term")}{status(S, "70.3% of US$871,500", "info")}</div>'
                   f'<div style="margin-top:14px">{fig(S, "US$612,400", 46)}</div>'
                   f'<div style="position:relative;height:20px;border-radius:10px;background:#f1f3f6;margin-top:22px;overflow:hidden">{seg}</div>'
                   f'<div style="display:flex;justify-content:space-between;margin-top:8px;font:500 12px {F};color:{MUTED}"><span>Wk 1 · 215k</span><span>Wk 2 · 390k</span><span>Wk 3 · 521k</span><span style="color:{BLUE}">Wk 4 · 612k</span><span>Due 871.5k</span></div>'
                   f'<div style="display:flex;gap:10px;margin-top:18px">{status(S, "Still to collect US$259,100", "warn")}{status(S, "12 payments today", "mute")}</div>', pad=22,
                extra="display:flex;flex-direction:column;justify-content:space-between")
    small = lambda t, v, sub, st: card(S, f'{lab(S, t)}<div style="margin:10px 0 6px">{fig(S, v, 30)}</div><div style="font-size:13px;color:{MUTED}">{sub}</div><div style="margin-top:12px">{status(S, st[1], st[0])}</div>', pad=20)
    side = (f'<div style="display:flex;flex-direction:column;gap:14px">{small("Boarders on roll", "212", "4 on exeat this weekend", ("mute", "Tsavo and Kariba"))}'
            f'{small("Maintenance", "3 open", "oldest open 9 days", ("warn", "1 overdue"))}</div>')
    attn = [("warn", "Form 2C attendance is 88% this week", "Mr Dube is calling three families"),
            ("bad", "46 accounts over 60 days in arrears", "US$38,900 · reminders go out Friday"),
            ("warn", "Science lab extractor fan", "Job MJ-0142 · parts ordered from Msasa"),
            ("info", "Form 4 mock timetable ready", "From Mr Ncube, deputy head, 07:40")]
    items = "".join(f'<div style="display:flex;gap:12px;align-items:flex-start;padding:14px;border-radius:14px;background:#f6f7f9">'
                    f'<span style="width:32px;height:32px;border-radius:16px;flex:none;display:flex;align-items:center;justify-content:center;background:{ {"warn": WARNS, "bad": BADS, "info": "#e8effd"}[kd] }">'
                    f'{ic({"warn": "alert", "bad": "wallet-3", "info": "calendar"}[kd] if i != 2 else "tool", 16, {"warn": WARN, "bad": BAD, "info": BLUE}[kd])}</span>'
                    f'<div style="flex:1;min-width:0"><div style="font:600 14px {F}">{t}</div><div style="font-size:13px;color:{MUTED};margin-top:3px">{s}</div></div>'
                    f'{ic("right-line", 16, FAINT)}</div>' for i, (kd, t, s) in enumerate(attn))
    attn_card = card(S, f'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px"><span style="font:600 16px {F}">Needs your attention</span>{status(S, "4 items", "mute")}</div>'
                        f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px">{items}</div>', pad=22)
    today = [("07:30", "Registers closed", "62 of 64 marked"), ("08:05", "Fees since 06:00", "US$4,820.00 and ZiG 2,600.00"), ("14:30", "SDC finance meeting", "Pack attached")]
    tl = "".join(f'<div style="display:flex;gap:12px;align-items:center;padding:10px 0;border-top:{"1px solid #eef0f3" if i else "none"}">'
                 f'<span style="height:24px;padding:0 9px;border-radius:12px;background:#f1f3f6;display:flex;align-items:center;font:500 12px {F};color:{INK2};{NUM}">{t}</span>'
                 f'<div><div style="font:500 14px {F}">{a}</div><div style="font-size:12.5px;color:{MUTED};margin-top:2px">{b}</div></div></div>' for i, (t, a, b) in enumerate(today))
    today_card = card(S, f'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px"><span style="font:600 16px {F}">Today</span>{lab(S, "Wed 30 Sep")}</div>{tl}', pad=22)
    main = (f'<div style="padding:28px;display:flex;flex-direction:column;gap:18px;background:#f4f5f7;flex:1">{greet}'
            f'<div style="display:grid;grid-template-columns:1fr 1.15fr 250px;gap:14px">{att}{fees}{side}</div>'
            f'<div style="display:grid;grid-template-columns:1fr 340px;gap:14px">{attn_card}{today_card}</div></div>')
    return (f'<div style="width:{w}px;height:{h}px;display:flex;flex-direction:column;background:#fff;border-radius:16px;overflow:hidden;'
            f'box-shadow:0 0 0 1px {LINE};font-family:{F};color:{INK}">{topbar}{main}</div>')

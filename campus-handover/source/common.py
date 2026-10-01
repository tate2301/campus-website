# -*- coding: utf-8 -*-
"""Corelith Campus: shared world, tokens and primitives. Reuses the Corelith company kit for the logo,
icons and product marks, so Campus stays one family with the company and product sites."""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, "/home/claude/corelith-co/kit")
from base import logo, mark, ic, pmark as _base_pmark, PBY, icons  # noqa: E402,F401
from campus_mark import campus_mark  # noqa: E402


def pmark(name, size=40, r=None):
    """product marks; Campus has its own, drawn in the illustration style (1 Oct 2026)"""
    if name == "Campus":
        return campus_mark(size, r)
    return _base_pmark(name, size, r)

PH = lambda n: "file://" + os.path.join(ROOT, "assets", "photos", n)
ART = lambda n: "file:///home/claude/corelith-co/assets/art/" + n

INK, INK2, MUTED, FAINT, LINE = "#0b0c14", "#3b3d47", "#6b6d78", "#9a9ea9", "#e7e9ef"
BLUE, MARK, CAMPUS = "#2563eb", "#0F62FE", "#7c5cff"
PLATE, TRAY, WHITE = "#f4f5f7", "#eceef2", "#ffffff"
OK, OKS, WARN, WARNS, BAD, BADS = "#12805c", "#e5f4ec", "#a15c07", "#fdf1dc", "#be123c", "#fde7ec"
SANS, SERIF, MONO, UI = "'Atkinson Hyperlegible Next',sans-serif", "'Newsreader',serif", "'IBM Plex Mono',monospace", "'Inter',sans-serif"
NUM = "font-variant-numeric:tabular-nums;"

# ---- the world (one set of names and figures for every picture) ---------------------------------
SCHOOL = "Mukuvisi High School"
TODAY = "Wednesday 30 September"
PUPIL = dict(name="Tanaka Moyo", form="Form 3B", house="Tsavo House", adm="2024-0387", guardian="Rudo Moyo",
             fee="1,250.00", paid="830.00", bal="420.00", due="Friday 16 October")
FORM3B = [("Tanaka Moyo", "P"), ("Tendai Chirwa", "P"), ("Ruvimbo Gumbo", "P"), ("Farai Nyathi", "A"), ("Chiedza Banda", "P"),
          ("Kundai Marufu", "L"), ("Anesu Dube", "P"), ("Nyasha Mlambo", "P"), ("Takudzwa Shumba", "P"), ("Rutendo Phiri", "P")]
MARKS = [("Mathematics", 71, 64, "+6"), ("English", 68, 61, "+2"), ("Combined Science", 74, 66, "+9"), ("Geography", 62, 59, "-3"),
         ("Shona", 80, 72, "+4"), ("History", 66, 63, "+1")]

PORTALS = [("Administration", "building-2", "Office, bursary, stores",
            "Run the school from enrolment to the last payslip of the year: fees in two currencies, payroll, stock and the Head's view."),
           ("Teacher", "book-6", "Staffroom and classroom",
            "The register on a tablet, marks recorded once, schemes of work reused, and parents told without a phone call."),
           ("Parent", "home-3", "Home, on any phone",
            "Attendance, marks, fees and reports in the week they happen, and a line to the class teacher."),
           ("Student", "school", "Class, hostel and home",
            "What is due, how I am doing, the timetable, and the library on my own phone.")]

MODULES = [("M·01", "Students and academics", "user-3"), ("M·02", "Fees and accounting", "wallet-3"), ("M·03", "Boarding", "moon"),
           ("M·04", "Payroll", "bank-card"), ("M·05", "Human resources", "contacts-2"), ("M·06", "Stock", "box-3"),
           ("M·07", "Maintenance", "tool"), ("M·08", "Communication", "message-3")]

COMMIT = [("wifi-off", "Works offline", "Every portal and module works without internet. Changes sync when the connection returns."),
          ("safe-lock", "The school owns its data", "Backed up every day and exportable in full. Never sold, shared or used to train AI models."),
          ("shield", "Role-based access", "Each person sees what their role needs. Every change records who made it and when."),
          ("cellphone", "Any device you have", "Office desktops, classroom tablets and a parent's phone. No server room."),
          ("map-pin", "Support from Harare", "Training and support from people who can come to the school."),
          ("sparkles", "AI that assists", "It drafts and explains; a teacher decides. Every use is logged and the school can switch it off.")]


def lockup(h=24, ink=INK, by=True):
    """the Campus product lockup, as on the product sites: the mark tile, lowercase name, 'by Corelith'"""
    t = (f'<span style="display:inline-flex;align-items:center;gap:{round(h * 0.36)}px">{pmark("Campus", h, round(h * 0.28))}'
         f'<span style="font:600 {round(h * 0.92)}px/1 {SANS};letter-spacing:-0.03em;color:{ink}">campus</span></span>')
    if by:
        t += f'<span style="font:400 {max(11, round(h * 0.5))}px {SANS};color:{MUTED};padding-left:12px;border-left:1px solid {LINE}">by Corelith</span>'
    return f'<span style="display:inline-flex;align-items:center;gap:12px">{t}</span>'


def btn(label, icon="calendar", kind="primary", h=44, size=15):
    s = {"primary": f"background:{BLUE};color:#fff;", "ghost": f"background:#fff;color:{INK};box-shadow:inset 0 0 0 1px {LINE};",
         "ink": f"background:#fff;color:{INK};", "dark": f"background:{INK};color:#fff;"}[kind]
    c = "#fff" if kind in ("primary", "dark") else INK
    return (f'<span style="display:inline-flex;align-items:center;gap:8px;height:{h}px;padding:0 {round(h * 0.36)}px 0 {round(h * 0.42)}px;border-radius:8px;'
            f'{s}font:500 {size}px/1 {SANS};white-space:nowrap">{label}{ic(icon, 16, c) if icon else ""}</span>')


def link(label, c=INK, size=15):
    return (f'<span style="display:inline-flex;align-items:center;gap:6px;font:500 {size}px {SANS};color:{c};text-decoration:underline;text-underline-offset:3px">{label}'
            f'{ic("right-line", 14, c)}</span>')


def photo(n, w, h, pos="center", r=14, extra=""):
    return (f'<div style="width:{w}px;height:{h}px;border-radius:{r}px;overflow:hidden;background:#dfe2e7;flex:none;{extra}">'
            f'<img src="{PH(n)}" alt="" style="display:block;width:100%;height:100%;object-fit:cover;object-position:{pos}"></div>')


def dashed(w, h, text, r=14):
    return (f'<div style="width:{w}px;height:{h}px;border:1.5px dashed #c3c8d1;border-radius:{r}px;display:flex;align-items:center;justify-content:center;'
            f'text-align:center;padding:0 20px;box-sizing:border-box;font:400 14px/1.5 {SANS};color:{MUTED}">{text}</div>')


def page(html, w=1440, h=None, bg=WHITE):
    hh = f"height:{h}px;" if h else ""
    return {"html": f'<div style="width:{w}px;{hh}background:{bg};position:relative;overflow:hidden;font-family:{SANS};color:{INK}">{html}</div>', "w": w}

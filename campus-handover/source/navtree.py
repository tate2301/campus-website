# -*- coding: utf-8 -*-
"""The Campus site map and how each page is reached. Built from placed boxes and lines, so every node can be moved on the canvas."""
from ds import *
import portal_art

W = 2880
DOMAIN = "campus.corelith.co.zw"
CTA_IC = {"visit": ("calendar", "Visit"), "price": ("download-2", "Price"), "training": ("presentation-2", "Training")}
PI = lambda n, s=22: portal_art.portal_icon(n, s)

# kind: page, section (an anchor on its parent), file, out (outside the site)
TREE = [
    ("Solutions", "/solutions", "layout-4", "visit", [
        ("Departments", [(n, "/solutions/" + sl, p_, "visit") for n, sl, d, p_, k in CP.DEPARTMENTS])]),
    ("Who we serve", "/who-we-serve", "school", "visit", [
        ("Types of school · K-12", [(n, "/who-we-serve/" + k[2:], "page", "visit") for n, k, d in CP.SCHOOL_TYPES]),
        ("Roles", [("School leadership", "/who-we-serve/leadership", "Administration", "visit"), ("The bursary", "/who-we-serve/bursary", "Administration", "visit"),
                   ("Teachers", "/who-we-serve/teachers", "Teacher", "visit"), ("Boarding staff", "/who-we-serve/boarding-staff", "Administration", "visit"),
                   ("Parents and guardians", "/who-we-serve/parents", "Parent", "visit"),
                   ("Pupils", "/who-we-serve/pupils", "Student", "visit")])]),
    ("Platform", "/platform", "layers", "visit", [
        ("Sections", [("One record", "#single-record", "section", None),
                      ("Works without internet", "#offline", "section", None),
                      ("Four portals", "#portals", "section", None),
                      ("Data and security", "#security", "section", None),
                      ("AI that assists", "#ai", "section", None)]),
        ("Pages", [("Integrations", "/platform/integrations", "page", "visit"),
                   ("Moving to Campus", "/moving-to-campus", "page", "training")])]),
    ("Pricing", "/pricing", "wallet-3", "price", [
        ("Sections", [("Work out your school", "#calculator", "section", None),
                      ("What is included", "#included", "section", None),
                      ("Setup and training", "#implementation", "section", "training"),
                      ("Questions", "#faq", "section", None)]),
        ("Files", [("Price sheet (PDF)", "/pricing/price-sheet.pdf", "file", None)])]),
    ("Book a demo", "/demo", "calendar", "training", [
        ("After the form", [("Request sent", "/demo/sent", "page", None)])]),
    ("Sign in", "app." + DOMAIN, "user-3", None, [
        ("Opens the app", [("One sign-in for all four portals", "Role decides the portal", "out", None)])]),
    ("Footer only", "", "menu-line", None, [
        ("Company", [("Corelith", "corelith.co.zw", "out", None), ("Contact", "/contact", "page", None), ("Support", "/support", "page", None)]),
        ("Legal", [("Privacy", "/legal/privacy", "page", None), ("Data ownership", "/legal/data-ownership", "page", None), ("Terms", "/legal/terms", "page", None)])]),
]

LN = "#c3c9d3"
CW = 300          # one column
GAP = 48
SUB = 24          # gap between two sub-columns under one parent


def cta_chip(k):
    if not k:
        return ""
    i, t = CTA_IC[k]
    return (f'<span style="display:inline-flex;align-items:center;gap:4px;height:22px;padding:0 8px 0 6px;border-radius:11px;background:#e8effd;color:{BLUE};font:500 12px {SANS};flex:none">'
            f'{ic(i, 12, BLUE)}{t}</span>')


NAV_KEY = {n: sl for n, sl, d, p_, k in CP.DEPARTMENTS}
NAV_KEY.update({n: k for n, k, d in CP.SCHOOL_TYPES})
NAV_KEY.update({"One record": "record", "Works without internet": "nointernet", "Four portals": "portals", "Data and security": "security", "AI that assists": "ai",
                "Integrations": "integrations", "Moving to Campus": "moving", "Work out your school": "calculator", "What is included": "included",
                "Setup and training": "training", "Questions": "questions", "Price sheet (PDF)": "pricesheet", "Request sent": "sent",
                "One sign-in for all four portals": "signin", "Contact": "contact", "Support": "support", "Privacy": "privacy", "Data ownership": "data", "Terms": "terms",
                "Solutions": "solutions", "Who we serve": "who", "Platform": "platform", "Pricing": "pricing", "Book a demo": "demo", "Sign in": "signin", "Footer only": "footer",
                "Nine department pages": "solutions", "Five school-type pages": "t-day", "Six role pages": "portals", "Company and legal": "terms"})


def lead_icon(name, kind, size=34):
    import nav_icons
    if name == "Home":
        return pmark("Campus", size, round(size * 0.27))
    if name == "Corelith":
        return (f'<span style="width:{size}px;height:{size}px;border-radius:{round(size * 0.24)}px;background:#f4f5f7;box-shadow:inset 0 0 0 1px #e7e9ef;'
                f'display:flex;align-items:center;justify-content:center;flex:none">{mark(round(size * 0.5))}</span>')
    key = NAV_KEY.get(name)
    if key:
        return nav_icons.nav_icon(key, size)
    if kind in PORTAL_NAMES:
        return PI(kind, size)
    return nav_icons.nav_icon("included", size)


def node(name, url, kind, cta, w=CW - 32):
    """a page card with its drawn icon; kind is a portal name, 'page', 'section', 'file' or 'out'"""
    dashed = kind in ("section", "out")
    border = f"border:1.5px dashed {LN}" if dashed else f"border:1px solid {LINE}"
    lead = f'<span style="flex:none">{lead_icon(name, kind)}</span>'
    if kind in PORTAL_NAMES and NAV_KEY.get(name) and not cta:                # which portal's drawing the page uses
        cta_mark = f'<span style="flex:none" title="{kind} portal">{PI(kind, 20)}</span>'
    else:
        cta_mark = ""
    bg = "#fff" if not dashed else "rgba(255,255,255,.6)"
    return (f'<div style="width:{w}px;min-height:58px;box-sizing:border-box;display:flex;align-items:center;gap:10px;padding:10px 10px 10px 12px;border-radius:14px;background:{bg};{border}">'
            f'{lead}<div style="flex:1;min-width:0"><div style="font:600 14.5px/1.25 {SANS};color:{INK}">{name}</div>'
            f'<div style="font:400 12px/1.4 {MONO};color:{MUTED};margin-top:2px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis">{url}</div></div>{cta_chip(cta)}{cta_mark}</div>')


def l1(name, url, icn, cta, w):
    foot = name == "Footer only"
    border = f"border:1.5px dashed {LN}" if foot or name == "Sign in" else f"border:1.5px solid {INK}"
    return (f'<div style="width:{w}px;height:76px;box-sizing:border-box;display:flex;align-items:center;gap:12px;padding:0 14px;border-radius:18px;background:#fff;{border};'
            f'box-shadow:0 10px 24px -18px rgba(11,12,20,.4)">'
            f'{lead_icon(name, "page", 44)}'
            f'<div style="flex:1;min-width:0"><div style="font:600 18px/1.2 {SANS}">{name}</div><div style="font:400 12.5px {MONO};color:{MUTED};margin-top:3px">{url or "Linked from the footer"}</div></div>'
            f'{cta_chip(cta)}</div>')


def branch(groups, w, ext=24, pcta=None):
    """labelled lists under one continuous spine; each page hangs off it on a short tick. ext: how far the spine reaches up to its parent"""
    rows = []
    for gi, (g, kids) in enumerate(groups):
        rows.append(("label", g, gi > 0))
        rows += [("node", k, False) for k in kids]
    out = f'<div style="width:{w}px">'
    for i, (t, v, sp) in enumerate(rows):
        last = i == len(rows) - 1
        top = -ext if i == 0 else 0
        if t == "label":
            h = "100%" if not last else "0"
            out += (f'<div style="position:relative;padding:{14 if sp else 0}px 0 10px 32px;font:500 13px {SANS};color:{MUTED}">'
                    f'<span style="position:absolute;left:15px;top:{top}px;bottom:0;width:1.5px;background:{LN}"></span>{v}</div>')
        else:
            n, u, k, c = v
            spine = (f'top:{top}px;height:{29 - top}px' if last else f'top:{top}px;bottom:0')
            out += (f'<div style="position:relative;padding:0 0 {0 if last else 12}px 32px">'
                    f'<span style="position:absolute;left:15px;{spine};width:1.5px;background:{LN}"></span>'
                    f'<span style="position:absolute;left:15px;top:28px;width:17px;height:1.5px;background:{LN}"></span>'
                    f'{node(n, u, k, c if c != pcta else None, w - 32)}</div>')
    return out + '</div>'


def column(item):
    name, url, icn, cta, groups = item
    if name == "Who we serve":
        w = 2 * CW + SUB
        body = (f'<div style="display:flex;gap:{SUB}px;align-items:flex-start;padding-top:34px">'
                + "".join(branch([gk], CW, 0, cta) for gk in groups) + '</div>')
        spines = (f'<span style="position:absolute;left:15px;top:76px;width:1.5px;height:34px;background:{LN}"></span>'
                  f'<span style="position:absolute;left:15px;top:88px;width:{CW + SUB + 1.5}px;height:1.5px;background:{LN}"></span>')
        return w, (f'<div style="position:relative;width:{w}px;flex:none">{l1(name, url, icn, cta, w)}{spines}'
                   f'<div style="position:relative">{body}</div>'
                   f'<span style="position:absolute;left:{CW + SUB + 15}px;top:88px;width:1.5px;height:22px;background:{LN}"></span></div>')
    w = CW
    return w, (f'<div style="position:relative;width:{w}px;flex:none">{l1(name, url, icn, cta, w)}'
               f'<div style="padding-top:24px">{branch(groups, CW, 24, cta)}</div></div>')


def legend():
    def item(lead, t):
        return f'<div style="display:flex;align-items:center;gap:10px;font:400 14.5px {SANS};color:{INK2}">{lead}{t}</div>'
    box = lambda b: f'<span style="width:34px;height:22px;border-radius:6px;background:#fff;{b};flex:none"></span>'
    ports = "".join(PI(n, 24) for n in PORTAL_NAMES)
    ctas = "".join(cta_chip(k) for k in CTA_IC)
    return (f'<div style="display:flex;gap:40px;align-items:center;flex-wrap:wrap;padding:18px 24px;border-radius:18px;background:{PLATE}">'
            + item(box(f"border:1.5px solid {INK}"), "Top level, in the header")
            + item(box(f"border:1px solid {LINE}"), "A page")
            + item(box(f"border:1.5px dashed {LN}"), "A section of its parent, or outside the site")
            + item(f'<span style="display:flex;gap:4px">{"".join(__import__("nav_icons").nav_icon(k, 28) for k in ("academics", "record", "t-mission"))}</span>', "Each page's own drawn icon")
            + item(f'<span style="display:flex;gap:4px">{ports}</span>', "The portal whose drawing a department page uses")
            + item(f'<span style="display:flex;gap:6px">{ctas}</span>', "The call to action that closes the page")
            + '</div>')


def sitemap():
    cols = [column(it) for it in TREE]
    inner_w = sum(w for w, _ in cols) + GAP * (len(cols) - 1)
    x0 = (W - 160 - inner_w) // 2
    # centres of each top-level card, for the bus
    xs, x = [], 0
    for w, _ in cols:
        xs.append(x + w // 2)
        x += w + GAP
    home_x = inner_w // 2
    bus_y = 150
    lines = (f'<span style="position:absolute;left:{home_x - 0.75}px;top:96px;width:1.5px;height:{bus_y - 96}px;background:{LN}"></span>'
             f'<span style="position:absolute;left:{xs[0]}px;top:{bus_y}px;width:{xs[-2] - xs[0]}px;height:1.5px;background:{LN}"></span>'
             + "".join(f'<span style="position:absolute;left:{cx - 0.75}px;top:{bus_y}px;width:1.5px;height:40px;background:{LN}"></span>' for cx in xs[:-1])
             + f'<span style="position:absolute;left:{xs[-2]}px;top:{bus_y}px;width:{xs[-1] - xs[-2]}px;height:0;border-top:1.5px dashed {LN}"></span>'
               f'<span style="position:absolute;left:{xs[-1] - 0.75}px;top:{bus_y}px;width:0;height:40px;border-left:1.5px dashed {LN}"></span>')
    home = (f'<div style="position:absolute;left:{home_x - 170}px;top:0;width:340px;height:96px;box-sizing:border-box;display:flex;align-items:center;gap:14px;padding:0 18px;border-radius:22px;background:#e8effd;box-shadow:inset 0 0 0 1.5px {BLUE}">'
            f'{lead_icon("Home", "page", 46)}<div style="flex:1"><div style="font:600 22px {SANS};color:{INK}">Home</div><div style="font:400 13px {MONO};color:{MUTED};margin-top:3px">{DOMAIN}</div></div>{cta_chip("visit")}</div>')
    tree = (f'<div style="position:relative;width:{inner_w}px;margin:0 auto">{home}{lines}'
            f'<div style="display:flex;gap:{GAP}px;align-items:flex-start;padding-top:190px">' + "".join(h for _, h in cols) + '</div></div>')
    head = (f'<div style="display:flex;align-items:center;justify-content:space-between;padding-bottom:22px;border-bottom:1px solid {LINE}">{lockup(26)}'
            f'<span style="font:500 16px {SANS};color:{MUTED}">Navigation · 1 October 2026</span></div>'
            f'<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:80px;margin-top:56px">'
            f'<h1 style="margin:0;font:600 88px/1 {SANS};letter-spacing:-0.04em">Site map<br><span style="color:{FAINT}">Every page and where it sits</span></h1>'
            f'<div style="width:760px">{para("Four pages in the header, each with its own pages below it. Solutions is split by department, Who we serve by type of school and by role. Department pages use the drawing of the portal they belong to, so Fees and billing is drawn at the admin block. Every page closes with one call to action.", 20, INK2, 760)}</div></div>'
            f'<div style="margin-top:48px">{legend()}</div>')
    return (f'<div style="width:{W}px;background:#fff;padding:80px 80px 120px;box-sizing:border-box;font-family:{SANS};color:{INK}">{head}'
            f'<div style="margin-top:80px;padding:72px 0 64px;border-radius:32px;{DOTS};box-shadow:inset 0 0 0 1px #eceef2">{tree}</div></div>')


# ---- how each page is reached ---------------------------------------------------------------------
REACH_COLS = ["Header", "Header menu", "Phone menu", "Footer", "Calls to action"]
Y = "y"
REACH = [
    ("Home", "/", "page", [Y, "", Y, Y, ""], "The Campus lockup on every page"),
    ("Solutions", "/solutions", "page", [Y, "", Y, Y, ""], "Home: the department tiles under the hero"),
    ("Nine department pages", "/solutions/academics …", "Teacher", ["", Y, Y, "", ""], "Home: each department tile; Pricing: the list of what is included"),
    ("Who we serve", "/who-we-serve", "page", [Y, "", Y, "", ""], ""),
    ("Five school-type pages", "/who-we-serve/day …", "page", ["", Y, Y, Y, ""], "Home: the Who we serve band"),
    ("Six role pages", "/who-we-serve/teachers …", "Parent", ["", Y, Y, "", ""], "Home: the row of portals under the school types"),
    ("Platform", "/platform", "page", [Y, "", Y, Y, ""], "Home: each row links to its section"),
    ("Integrations", "/platform/integrations", "page", ["", Y, Y, "", ""], "Accounting page; Home: the integrations row"),
    ("Moving to Campus", "/moving-to-campus", "page", ["", Y, Y, Y, ""], "Solutions menu: the side card; Home: “How we move your records”"),
    ("Pricing", "/pricing", "page", [Y, "", Y, Y, "Price"], "Home: the pricing band"),
    ("Price sheet (PDF)", "/pricing/price-sheet.pdf", "file", ["", "", "", "", "Visit, Price"], "Pricing: under the calculator"),
    ("Book a demo", "/demo", "page", ["Button", "", "Button", "", "Visit, Training"], "Hero: the first button"),
    ("Request sent", "/demo/sent", "page", ["", "", "", "", ""], "Only after the demo form is sent"),
    ("Sign in", "app." + DOMAIN, "out", [Y, "", Y, "", ""], ""),
    ("Company and legal", "/contact, /legal/…", "page", ["", "", "", Y, ""], "Platform: “Data and security” links to Data ownership"),
]


def reach(W=1920):
    th = f'font:500 13.5px {SANS};color:{MUTED};padding:0 16px 14px;text-align:left;border-bottom:1px solid {LINE}'
    head = (f'<tr><th style="{th};padding-left:0;width:420px">Page</th>' + "".join(f'<th style="{th};width:130px">{c}</th>' for c in REACH_COLS)
            + f'<th style="{th}">Also linked from</th></tr>')
    rows = ""
    for n, u, k, cells, also in REACH:
        tds = ""
        for c in cells:
            if c == Y:
                v = f'<span style="display:inline-block;width:12px;height:12px;border-radius:6px;background:{BLUE}"></span>'
            elif c:
                v = f'<span style="font:500 13.5px {SANS};color:{BLUE}">{c}</span>'
            else:
                v = f'<span style="display:inline-block;width:12px;height:1.5px;background:{LINE};vertical-align:middle"></span>'
            tds += f'<td style="padding:14px 16px;border-bottom:1px solid {LINE};vertical-align:middle">{v}</td>'
        rows += (f'<tr><td style="padding:10px 16px 10px 0;border-bottom:1px solid {LINE}">{node(n, u, k, None, 400)}</td>{tds}'
                 f'<td style="padding:14px 16px;border-bottom:1px solid {LINE};font:400 14.5px/1.5 {SANS};color:{INK2}">{also}</td></tr>')
    table = f'<table style="border-collapse:collapse;width:100%">{head}{rows}</table>'
    rules = [("Four in the header", "Solutions, Who we serve, Platform and Pricing. Sign in and Book a demo sit on the right of the bar."),
             ("Menus open on Solutions, Who we serve and Platform", "Solutions lists the nine departments with their drawings. Who we serve lists the types of school and the roles."),
             ("The phone menu holds the same tree", "Each menu opens in place; Book a demo stays in the bar as “Demo”."),
             ("Nothing is reached only by search", "Every page has at least two ways in. Request sent is the one exception: it follows the form.")]
    rl = "".join(f'<div style="padding:16px 0;border-top:1px solid {LINE}"><div style="font:600 17px {SANS}">{t}</div><div style="font:400 15px/1.55 {SANS};color:{INK2};margin-top:4px">{d}</div></div>' for t, d in rules)
    body = (f'{table}<div style="display:grid;grid-template-columns:1fr 1fr;gap:0 64px;margin-top:64px">{rl}</div>')
    return (f'<div style="width:{W}px;background:#fff;padding:80px 80px 120px;box-sizing:border-box;font-family:{SANS};color:{INK}">'
            f'<div style="display:flex;align-items:center;justify-content:space-between;padding-bottom:22px;border-bottom:1px solid {LINE}">{lockup(26)}'
            f'<span style="font:500 16px {SANS};color:{MUTED}">Navigation · 1 October 2026</span></div>'
            f'<h1 style="margin:56px 0 0;font:600 64px/1.05 {SANS};letter-spacing:-0.035em">How each page is reached<br><span style="color:{FAINT}">Header, menus, footer and links</span></h1>'
            f'<div style="margin-top:56px">{body}</div></div>')

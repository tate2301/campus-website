# -*- coding: utf-8 -*-
"""Every page in the navigation tree, built from the same sections as Home, Academics and Moving.
Each page is a list of sections, so a page taller than an artboard can be split between sections."""
from ds import *
import pages as PG
import site_words as SW
import site_cards as SC
import hero as HR
import dept_art, portal_art, cta_art, nav_icons
import ui

X, GAP = PG.X, PG.GAP
W = 1440
DEPT = {sl: (n, sl, d, p_, k) for n, sl, d, p_, k in CP.DEPARTMENTS}
CARD_PORTAL = {"intake_card": "Administration", "application_card": "Administration", "offer_card": "Administration", "payments_card": "Administration",
               "billing_card": "Administration", "arrears_card": "Administration", "ledger_card": "Administration", "journal_card": "Administration",
               "fiscal_card": "Administration", "payslip_card": "Teacher", "payrun_card": "Administration", "staff_card": "Administration",
               "leave_card": "Teacher", "rollcall_card": "Administration", "exeat_card": "Parent", "sickbay_card": "Administration",
               "stock_card": "Administration", "issue_card": "Administration", "repairs_card": "Teacher", "compose_card": "Teacher",
               "events_card": "Parent", "read_card": "Teacher", "attendance_card": "Administration", "collected_card": "Administration",
               "results_card": "Administration", "transport_card": "Parent", "levy_card": "Parent", "ai_card": "Student", "student_card": "Student",
               "approvals_card": "Administration", "plan_card": "Administration", "visitors_card": "Administration", "register_card": "Teacher", "marks_card": "Teacher", "fee_card": "Parent", "head_card": "Administration",
               "note_card": "Parent", "att_card": "Administration", "signin_card": "Administration"}
WIDE = {"compose_card": 340, "ai_card": 340, "payments_card": 320, "billing_card": 320, "arrears_card": 320, "ledger_card": 320, "journal_card": 320,
        "stock_card": 320, "attendance_card": 320, "collected_card": 320, "fee_card": 320, "note_card": 330, "fiscal_card": 280, "visitors_card": 320}


def card_html(name, w=None, **kw):
    w = w or WIDE.get(name, 300)
    if hasattr(SC, name) and getattr(SC, name).__module__ == "site_cards":
        return getattr(SC, name)(w, **kw)
    if name in ("note_card", "att_card"):
        return getattr(HR, name)(w)
    return getattr(ui, name)(SB, w)


def tcard(name, **kw):
    return HR.tagged(f"{CARD_PORTAL.get(name, 'Administration')} portal", card_html(name, **kw))


# ---- page frame -----------------------------------------------------------------------------------------
def gap(h=GAP):
    return f'<div style="height:{h}px"></div>'


def wrap(inner, pad=f"0 {X}px"):
    return f'<div style="padding:{pad}">{inner}</div>'


def page(secs, w=W):
    return f'<div style="width:{w}px;background:#fff;font-family:{SANS};color:{INK}">{"".join(secs)}</div>'


def footer_secs(cta="visit"):
    return [wrap(cta_block(cta, w=W - 2 * (X - 40)), f"{GAP}px {X - 40}px"), PG.site_footer()]


def sec_head(eye, key, h, size=46, w=820, mb=44):
    return f'<div style="display:flex;flex-direction:column;gap:16px;margin-bottom:{mb}px">{PG.eyebrow(eye, key)}{PG.head(h, size, w)}</div>'


def row(eye, key, h, b, pic, flip=False, extra=""):
    txt = (f'<div style="flex:1;display:flex;flex-direction:column;gap:18px;justify-content:center;max-width:500px">{PG.eyebrow(eye, key)}{PG.head(h, 42, 500)}'
           f'{para(b, 18, INK2, 480)}{extra}</div>')
    pic_ = f'<div style="flex:none">{pic}</div>'
    return f'<div style="display:flex;gap:96px;align-items:center;justify-content:space-between">{pic_ + txt if flip else txt + pic_}</div>'


def rows(items):
    """items: (eye, key, h, b, pic_html). Alternating, GAP apart"""
    return wrap("".join(f'<div style="margin-top:{0 if i == 0 else GAP}px">{row(e, k, h_, b_, p, flip=i % 2 == 1)}</div>' for i, (e, k, h_, b_, p) in enumerate(items)))


def pic_of(spec, w=620, h=440):
    kind = spec[0]
    if kind == "plate":
        cards, art = spec[1], spec[2]
        inner = ""
        if art:
            inner += f'<div style="position:absolute;right:-12px;bottom:-6px">{dept_art.art(art, 420, 290, U=48)}</div>'
        for n, x, y in cards:
            inner += at(x, y, tcard(n), 3)
        return PG.on_plate(inner, w, h)
    if kind == "photo":
        return photo_story(spec[1], spec[2], [(x, y, tcard(n)) for n, x, y in spec[3]], w, h)
    if kind == "integrations":
        return PG.pic_integrations(w, h)
    if kind == "phone":
        return photo_story("mother-phone.jpg", "65% center", [(0, 8, PG.parent_phone(0.52))], w, 470)
    raise ValueError(kind)


def hero_pic(photo, pos, a, b):
    return (f'<div style="position:relative;width:1200px;height:600px">'
            f'<div style="position:absolute;left:90px;top:30px">{ph(photo, 1020, 570, pos, 24)}</div>'
            + at(0, 120, tcard(a), 3) + at(1200 - WIDE.get(b, 300), 0, tcard(b), 2) + '</div>')


def demo_btns(price=False):
    b = cbtn("Book a demo", "calendar", "primary", "lg")
    if price:
        b += cbtn("Download the price sheet (PDF)", "download-2", "secondary", "lg")
    return b


def split_band(eye, key, h, b, photo, pos):
    return (f'<section style="background:{PLATE};padding:{GAP - 40}px {X}px"><div style="display:flex;align-items:center;justify-content:space-between;gap:96px">'
            f'<div style="flex:1;display:flex;flex-direction:column;gap:20px;max-width:520px">{PG.eyebrow(eye, key)}{PG.head(h, 44, 520)}{para(b, 19, INK2, 500)}</div>'
            f'{ph(photo, 600, 420, pos, 24)}</div></section>')


def tools(title, items):
    t = "".join(f'<div style="display:flex;align-items:center;gap:10px;padding:14px 0;border-top:1px solid {LINE};font:500 16px {SANS}">{ic("check-circle", 16, BLUE)}{x}</div>' for x in items)
    return wrap(f'<div style="display:flex;gap:96px"><div style="width:420px">{PG.eyebrow("Features", "included")}<div style="margin-top:14px">{PG.head(title, 40, 420)}</div></div>'
                f'<div style="flex:1;display:grid;grid-template-columns:1fr 1fr;gap:0 48px">{t}</div></div>')


def tiles(slugs, cols=3):
    t = "".join(PG.dept_tile(*DEPT[s], w=384) for s in slugs)
    return f'<div style="display:grid;grid-template-columns:repeat({cols},384px);gap:24px;justify-content:space-between">{t}</div>'


def faq_list(eye, key, h, qa):
    qs = "".join(f'<div style="padding:22px 0;border-top:1px solid {LINE}"><div style="font:600 18px {SANS}">{q}</div>'
                 f'<div style="font:400 16px/1.6 {SANS};color:{INK2};margin-top:6px;max-width:720px">{a}</div></div>' for q, a in qa)
    return wrap(f'<div style="display:flex;gap:96px"><div style="width:420px">{PG.eyebrow(eye, key)}<div style="margin-top:14px">{PG.head(h, 40, 420)}</div></div>'
                f'<div style="flex:1">{qs}</div></div>')


def link_card(key, t, d, act, w=None, h=None, art=None):
    """equal-height card: icon, title, one line, action on the bottom line"""
    ww = f"width:{w}px;" if w else "flex:1;"
    top = (f'<div style="margin:-28px -28px 20px;height:220px;{DOTS};border-bottom:1px solid #eceef2;overflow:hidden">{art}</div>' if art else nav_icons.nav_icon(key, 48))
    return (f'<div style="{ww}box-sizing:border-box;border-radius:24px;background:{PLATE};padding:28px;display:flex;flex-direction:column;overflow:hidden;{"min-height:" + str(h) + "px;" if h else ""}">'
            f'{top}<div style="font:600 24px/1.15 {SANS};letter-spacing:-0.02em;margin-top:{0 if art else 20}px;text-wrap:balance">{t}</div>'
            f'<div style="font:400 15px/1.5 {SANS};color:{INK2};margin-top:8px">{d}</div><div style="margin-top:auto;padding-top:22px">{PG.explore(act)}</div></div>')


# ---- department page --------------------------------------------------------------------------------------
def dept_secs(slug):
    n, sl, d, p_, k = DEPT[slug]
    D = SW.DEPTS[slug]
    photo, pos, a, b = D["hero"]
    top = PG.page_hero(n, slug, D["h"], D["b"], demo_btns(), hero_pic(photo, pos, a, b))
    bh, bb, bp, bpos = D["band"]
    rws = rows([(e, key, h_, b_, pic_of(sp)) for e, key, h_, b_, sp in D["rows"]])
    return [nav_bar("Solutions", W) + top, gap() + split_band("One record", "record", bh, bb, bp, bpos) + gap(), rws, gap() + tools(SW.DEPT_TOOLS_H, D["tools"])] + footer_secs()


# ---- school type page -------------------------------------------------------------------------------------
def type_secs(key):
    import who_sections as WS
    T = SW.TYPES[key]
    photo, pos, a, b = T["hero"]
    top = PG.page_hero(T["name"], key, T["h"], T["b"], demo_btns(), hero_pic(photo, pos, a, b))
    secs = [gap() + x for x in WS.SECTIONS[key]()]
    depts = wrap(sec_head("Departments", "solutions", SW.TYPE_DEPTS_H) + tiles(T["depts"]))
    return [nav_bar("Who we serve", W) + top] + secs + [gap() + depts] + footer_secs()


# ---- role page ------------------------------------------------------------------------------------------
def role_secs(slug):
    R = SW.ROLE_PAGES[slug]
    photo, pos, a, b = R["hero"]
    eye = (f'<div style="display:flex;align-items:center;gap:10px;font:500 15px {SANS};color:{BLUE}">{portal_art.portal_icon(R["portal"], 30)}{R["name"]}'
           f'<span style="color:{FAINT}">·</span><span style="color:{INK2}">{R["portal"]} portal</span></div>')
    top = PG.page_hero("", None, R["h"], R["b"], demo_btns(), hero_pic(photo, pos, a, b)).replace(PG.eyebrow("", None), eye, 1)
    rws = rows([(e, k, h_, b_, pic_of(sp)) for e, k, h_, b_, sp in R["rows"]])
    depts = wrap(sec_head("Departments", "solutions", SW.ROLE_DEPTS_H) + tiles(R["depts"]))
    return [nav_bar("Who we serve", W) + top, gap() + rws, gap() + depts] + footer_secs()


# ---- Solutions index ----------------------------------------------------------------------------------------
def solutions_secs():
    S = SW.SOLUTIONS
    top = PG.page_hero(S["eyebrow"], "solutions", S["h"], S["b"], demo_btns(), "")
    grid = wrap(tiles([d[1] for d in CP.DEPARTMENTS]))
    import mark_anim
    rws = rows([(e, PG.ROW_ICON[e], h_, b_, p) for (e, h_, b_), p in zip(CP.ROWS[:3], [mark_anim.mark_journey(620, 460), PG.pic_offline(), PG.pic_integrations()])])
    return [nav_bar("Solutions", W) + top, grid, gap() + rws, gap() + PG.switching()] + footer_secs()


# ---- Who we serve index ---------------------------------------------------------------------------------------
def who_secs():
    S = SW.WHO
    pic = PG.on_plate(dept_art.schools_campus(1200, 560, 40), 1200, 560)
    top = PG.page_hero(S["eyebrow"], "who", S["h"], S["b"], demo_btns(), pic)
    types = "".join(f'<div style="width:232px;display:flex;flex-direction:column"><div style="position:relative;width:232px;height:250px">{ph(PG.TYPE_PHOTO[k][0], 232, 250, PG.TYPE_PHOTO[k][1], 20)}'
                    f'<div style="position:absolute;left:12px;bottom:12px;border-radius:12px;box-shadow:0 8px 18px -10px rgba(11,12,20,.5)">{nav_icons.nav_icon(k, 44)}</div></div>'
                    f'<div style="font:600 19px {SANS};margin-top:16px">{n}</div><div style="font:400 14.5px/1.5 {SANS};color:{INK2};margin-top:6px">{d}</div>'
                    f'<div style="margin-top:auto;padding-top:16px">{PG.explore()}</div></div>' for n, k, d in CP.SCHOOL_TYPES)
    types_ = wrap(sec_head("Who we serve · K-12", "who", SW.WHO["types_h"]) + f'<div style="display:flex;justify-content:space-between;align-items:stretch">{types}</div>')
    roles = wrap(sec_head("Who uses Campus", "portals", CP.ROLES_H) + f'<div style="display:grid;grid-template-columns:repeat(3,389px);gap:24px;justify-content:space-between">'
                 + "".join(PG.role_tile(*r) for r in CP.ROLES) + '</div>')
    return [nav_bar("Who we serve", W) + top, gap() + types_, gap() + roles] + footer_secs()


# ---- Platform ---------------------------------------------------------------------------------------------
def platform_secs():
    P = SW.PLATFORM
    import mark_anim
    pic = (f'<div style="position:relative;width:1200px;height:600px">'
           f'<div style="position:absolute;left:90px;top:30px">{ph("pupils-writing.jpg", 1020, 570, "center 40%", 24)}</div>'
           + at(0, 90, tcard("register_card"), 3) + at(880, 0, tcard("fee_card"), 2) + at(840, 400, tcard("student_card"), 4) + '</div>')
    top = PG.page_hero(P["eyebrow"], "platform", P["h"], P["b"], demo_btns(), pic)
    r1 = rows([(e, PG.ROW_ICON[e], h_, b_, p) for (e, h_, b_), p in zip(CP.ROWS[:2], [mark_anim.mark_journey(620, 460), PG.pic_offline()])])
    pt = "".join(f'<div style="position:relative;height:420px;border-radius:24px;background:{PLATE};overflow:hidden;padding:26px 24px 0;box-sizing:border-box">'
                 f'<div style="font:600 24px/1.15 {SANS};letter-spacing:-0.02em">{n} portal</div>'
                 f'<div style="font:400 14.5px/1.5 {SANS};color:{INK2};margin-top:8px">{who}</div><div style="font:400 14.5px/1.5 {SANS};color:{MUTED};margin-top:4px">{what}</div>'
                 f'<div style="position:absolute;left:-20px;bottom:-24px">{portal_art.portal_scene(n, 320, 220, 26, 160, 135, labels=False)}</div></div>'
                 for n, who, what in P["portals"])
    portals = wrap(sec_head("Four portals", "portals", P["portals_h"]) + f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px">{pt}</div>')
    e, h_, b_ = CP.ROWS[4]
    ae, ah, ab = P["ai"]
    r2 = rows([(e, "security", h_, b_, PG.pic_security()), (ae, "ai", ah, ab, PG.on_plate(at(140, 40, tcard("ai_card")), 620, 440))])
    more = wrap(sec_head("Platform", "platform", P["more_h"]) + '<div style="display:flex;gap:24px;align-items:stretch">'
                + link_card("integrations", "Integrations", "Sage Pastel, QuickBooks, ZIMRA fiscalisation and payments.", "See the integrations",
                            art=f'<div style="display:flex;justify-content:center">{scaled(PG.pic_integrations(620, 420), 325, 220, 220 / 420)}</div>')
                + link_card("moving", "Moving to Campus", "From your old system to your first term on Campus, in four weeks.", "How we move your records",
                            art=cta_art.cta_scene("training", 588, 220, 26, 294, 150, labels=False)) + '</div>')
    return [nav_bar("Platform", W) + top, gap() + r1, gap() + portals, gap() + r2, gap() + more] + footer_secs()


# ---- Integrations -----------------------------------------------------------------------------------------
def integrations_secs():
    I_ = SW.INTEG
    top = PG.page_hero(I_["eyebrow"], "integrations", I_["h"], I_["b"], demo_btns(), hero_pic("girls-papers.jpg", "center 40%", "payments_card", "fiscal_card"))
    items = []
    for i, (e, k, h_, b_, cn, to) in enumerate(I_["rows"]):
        kw = {"to": to} if to else {}
        c = HR.tagged("Administration portal", card_html(cn, **kw))
        pic = (photo_story("accountant-man.jpg", "center 30%", [(0, 80, c)], 620, 440) if i == 1 else
               photo_story("mother-phone.jpg", "65% center", [(0, 90, c)], 620, 440) if i == 3 else PG.on_plate(at(150, 40, c), 620, 440))
        items.append((e, k, h_, b_, pic))
    mk = (f'<section style="background:{PLATE};padding:{GAP - 40}px {X}px">{sec_head(I_["market_eye"], "integrations", I_["market_h"])}'
          f'{SC.marketplace(1200)}</section>')
    return [nav_bar("Platform", W) + top, gap() + rows(items), gap() + mk, gap() + faq_list("Questions", "questions", "What bursars ask about the links.", I_["faq"])] + footer_secs()


# ---- Pricing --------------------------------------------------------------------------------------------------
def pricing_secs():
    P = SW.PRICE
    cards = (f'<div style="display:flex;gap:24px;align-items:stretch;width:1200px">'
             f'<div style="flex:none;width:340px;border-radius:24px;overflow:hidden;position:relative;background:#dfe2e7">'
             f'<img src="{PH("girl-beret.jpg")}" alt="" style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 20%"></div>'
             f'{pricing_card(CP.PRICING["main"], True, 418)}{pricing_card(CP.PRICING["lms"], False, 418)}</div>')
    top = PG.page_hero(P["eyebrow"], "pricing", P["h"], P["b"], demo_btns(True), cards)
    calc = wrap(row(P["calc_h"], "calculator", "Your school's figure, before you call us.", P["calc_b"], calculator("1,140", False, 560)))
    inc = "".join(f'<div style="display:flex;flex-direction:column;gap:12px;padding:24px;border-radius:20px;background:{PLATE}">{nav_icons.nav_icon(k, 48)}'
                  f'<div style="font:600 18px {SANS};margin-top:6px">{t}</div><div style="font:400 14.5px/1.5 {SANS};color:{INK2}">{d}</div></div>' for k, t, d in P["included"])
    included = wrap(sec_head(P["incl_h"], "included", "Everything, at US$1 per active pupil per month.") + f'<div style="display:grid;grid-template-columns:repeat(4,1fr);gap:24px">{inc}</div>')
    S = CP.SWITCH
    setup = (f'<section style="background:{PLATE};padding:{GAP - 40}px {X}px"><div style="display:flex;justify-content:space-between;align-items:center;gap:72px">'
             f'<div style="width:520px;display:flex;flex-direction:column;gap:20px">{PG.eyebrow(P["setup_h"], "training")}{PG.head("Running in four weeks, with us at the school.", 44, 520)}'
             f'{para(P["setup_b"], 18, INK2, 500)}<div style="margin-top:8px">{PG.steps(S["steps"], 520)}</div></div>'
             f'<div style="width:600px;height:520px;border-radius:24px;overflow:hidden;{DOTS};box-shadow:inset 0 0 0 1px #e3e6eb;flex:none">{cta_art.cta_scene("training", 600, 520, 46, 300, 300)}</div></div></section>')
    qa = FAQ + [("What does setup cost?", "Nothing. Setup, data capture and training are free."),
                ("Is there a charge per user?", "No. Staff, guardians and pupils sign in at no extra cost.")]
    return [nav_bar("Pricing", W) + top, gap() + calc, gap() + included, gap() + setup, gap() + faq_list(P["faq_h"], "questions", "What schools ask about the price.", qa)] + footer_secs()


def price_sheet():
    P = CP.PRICING
    m, lm = P["main"], P["lms"]
    inc = "".join(f'<div style="display:flex;gap:10px;align-items:flex-start;padding:7px 0;border-top:1px solid {LINE};font:400 13.5px/1.45 {SANS};color:{INK2}">'
                  f'<span style="padding-top:2px">{ic("check-circle", 14, BLUE)}</span>{t}</div>' for t in m["items"] + ["Works without internet", "Daily backups and a full export"])
    tl = "".join(f'<div style="flex:1;padding-top:10px;border-top:3px solid {BLUE}"><div style="font:500 11.5px {SANS};color:{MUTED}">{a}</div>'
                 f'<div style="font:600 14px {SANS};margin-top:4px">{b}</div><div style="font:400 12.5px/1.4 {SANS};color:{INK2};margin-top:2px">{c}</div></div>' for a, b, c in P["timeline"])
    return (f'<div style="width:794px;height:1123px;box-sizing:border-box;background:#fff;padding:56px 60px;font-family:{SANS};color:{INK};display:flex;flex-direction:column">'
            f'<div style="display:flex;justify-content:space-between;align-items:center;padding-bottom:18px;border-bottom:1px solid {LINE}">{lockup(22, by=False)}'
            f'<span style="font:400 12px {MONO};color:{MUTED}">Price sheet · October 2026</span></div>'
            f'<div style="margin-top:40px;font:500 14px {SANS};color:{BLUE}">Pricing</div>'
            f'<div style="font:600 46px/1.04 {SANS};letter-spacing:-0.035em;margin-top:10px;text-wrap:balance">US$1 per active pupil per month.</div>'
            f'<div style="font:400 15.5px/1.6 {SANS};color:{INK2};margin-top:14px;max-width:560px">{P["b"]}</div>'
            f'<div style="display:flex;gap:20px;margin-top:32px">'
            f'<div style="flex:1;border-radius:16px;box-shadow:0 0 0 2px {BLUE};padding:22px"><div style="font:600 15px {SANS}">{m["name"]}</div>'
            f'<div style="font:600 38px/1 {SANS};letter-spacing:-0.03em;margin-top:12px">{m["price"]}</div><div style="font:400 13px {SANS};color:{MUTED};margin-top:6px">{m["per"]}</div>'
            f'<div style="margin-top:14px">{inc}</div></div>'
            f'<div style="flex:1;display:flex;flex-direction:column;gap:20px"><div style="border-radius:16px;box-shadow:0 0 0 1px {LINE};padding:22px"><div style="font:600 15px {SANS}">{lm["name"]}</div>'
            f'<div style="font:600 38px/1 {SANS};letter-spacing:-0.03em;margin-top:12px">{lm["price"]}</div><div style="font:400 13px {SANS};color:{MUTED};margin-top:6px">{lm["per"]}</div>'
            f'<div style="font:400 13.5px/1.5 {SANS};color:{INK2};margin-top:12px">{"<br>".join(lm["items"])}</div></div>'
            f'<div style="border-radius:16px;background:{PLATE};padding:22px"><div style="font:500 13px {SANS};color:{MUTED}">{P["example"]["t"]}</div>'
            f'<div style="font:600 32px/1 {SANS};letter-spacing:-0.03em;margin-top:10px;{NUM}">{P["example"]["v"]}</div><div style="font:400 13px {SANS};color:{INK2};margin-top:6px">{P["example"]["s"]}</div></div></div></div>'
            f'<div style="margin-top:34px;font:600 16px {SANS}">Setup and training</div><div style="display:flex;gap:16px;margin-top:14px">{tl}</div>'
            f'<div style="margin-top:34px;font:600 16px {SANS}">Questions</div><div style="display:grid;grid-template-columns:1fr 1fr;gap:4px 28px;margin-top:6px">'
            + "".join(f'<div style="padding:10px 0;border-top:1px solid {LINE}"><div style="font:600 13.5px {SANS}">{q}</div><div style="font:400 12.5px/1.5 {SANS};color:{INK2};margin-top:3px">{a}</div></div>' for q, a in (FAQ[0], FAQ[3]))
            + f'</div><div style="margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;padding-top:20px;border-top:1px solid {LINE}">'
            f'<div style="font:400 12.5px/1.6 {SANS};color:{MUTED}">Book a demo at campus.corelith.co.zw/demo<br>{CP.FOOT_LINE}</div>{pmark("Campus", 40, 11)}</div></div>')


# ---- Book a demo and Request sent -------------------------------------------------------------------------
def demo_form():
    return (f'<div style="width:560px;box-sizing:border-box;padding:36px;border-radius:24px;background:#fff;box-shadow:0 0 0 1px {LINE},{SH_CARD}">'
            f'<div style="font:600 24px {SANS};letter-spacing:-0.015em">Book a demo</div><div style="font:400 15px {SANS};color:{MUTED};margin-top:6px">We call you to arrange a visit.</div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:26px">{field("Your name", "Chipo Mutasa", w=234)}{field("Your role", "Head", kind="select", w=234)}'
            f'{field("School", "Mukuvisi High School", w=234)}{field("Active pupils", "1,140", help_="Roughly is fine.", w=234)}'
            f'{field("Phone", "+263 77 000 0000", w=234)}{field("Email", "", "head@yourschool.ac.zw", w=234)}</div>'
            f'<div style="margin-top:22px"><div style="font:500 14px {SANS};margin-bottom:10px">Your school</div><div style="display:flex;gap:28px">{check("Day", True)}{check("Boarding", True)}{check("Primary", False)}{check("Secondary", True)}</div></div>'
            f'<div style="margin-top:20px"><div style="font:500 14px {SANS};margin-bottom:10px">How should we show you?</div><div style="display:flex;gap:28px">{check("Visit the school", True, True)}{check("Video call", False, True)}</div></div>'
            f'<div style="display:flex;justify-content:space-between;align-items:center;margin-top:30px;padding-top:22px;border-top:1px solid {LINE}">'
            f'<span style="font:400 13px/1.5 {SANS};color:{MUTED};max-width:250px">We use these details only to arrange the demo.</span>{cbtn("Book a demo", "calendar", "primary", "lg")}</div></div>')


def demo_secs():
    D = SW.DEMO
    st = "".join(f'<div style="display:flex;gap:16px;padding:16px 0;border-top:1px solid {LINE}"><span style="width:32px;height:32px;border-radius:16px;background:#e8effd;color:{BLUE};'
                 f'display:flex;align-items:center;justify-content:center;font:600 14px {SANS};flex:none">{n}</span><div><div style="font:600 17px {SANS}">{t}</div>'
                 f'<div style="font:400 15px/1.55 {SANS};color:{INK2};margin-top:4px">{d}</div></div></div>' for n, t, d in D["steps"])
    left = (f'<div style="width:540px;display:flex;flex-direction:column;gap:22px">{PG.eyebrow(D["eyebrow"], "demo")}'
            f'<h1 style="margin:0;font:600 56px/1.05 {SANS};letter-spacing:-0.04em;text-wrap:balance">{D["h"]}</h1>{para(D["b"], 19, INK2, 520)}'
            f'<div style="margin-top:18px"><div style="font:600 18px {SANS};margin-bottom:6px">{D["next_h"]}</div>{st}</div></div>')
    body = wrap(f'<div style="display:flex;justify-content:space-between;align-items:flex-start">{left}{demo_form()}</div>', f"88px {X}px 0")
    # the afternoon, room by room, each with what you will see on the screen
    ag = ""
    for time, room, t, d, cn in D["agenda"]:
        ag += (f'<div style="position:relative;min-height:{ {"head_card": 340, "payments_card": 340, "register_card": 420, "plan_card": 420}[cn]}px;border-radius:24px;background:{PLATE};overflow:hidden;padding:30px;box-sizing:border-box">'
               f'<div style="width:206px;display:flex;flex-direction:column;gap:12px">'
               f'<span style="display:inline-flex;align-self:flex-start;align-items:center;gap:6px;height:28px;padding:0 11px;border-radius:14px;background:#fff;box-shadow:inset 0 0 0 1px {LINE};'
               f'font:500 13px {SANS};color:{INK2}"><b style="font:500 12.5px {MONO};color:{BLUE}">{time}</b>{room}</span>'
               f'<div style="font:600 24px/1.15 {SANS};letter-spacing:-0.02em;text-wrap:balance">{t}</div><div style="font:400 15px/1.55 {SANS};color:{INK2}">{d}</div></div>'
               f'<div style="position:absolute;right:28px;top:30px">{tcard(cn, w=300)}</div></div>')
    agenda = wrap(sec_head("Your demo", "demo", D["agenda_h"]) + f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px">{ag}</div>')
    e, k, h_, b_ = D["who"]
    who = rows([(e, k, h_, b_, photo_story("woman-files.jpg", "center 30%", [(0, 70, tcard("visitors_card"))], 620, 460))])
    return [nav_bar(None, W) + body, gap() + agenda, gap() + who, gap() + faq_list("Questions", "questions", D["faq_h"], D["faq"]), gap()] + [PG.site_footer()]


def sent_secs():
    S = SW.SENT
    top = (f'<section style="display:flex;flex-direction:column;align-items:center;text-align:center;padding:72px {X}px 0">'
           f'<div style="width:760px;height:400px;border-radius:28px;overflow:hidden;{DOTS};box-shadow:inset 0 0 0 1px #e3e6eb">{cta_art.cta_scene("visit", 760, 400, 42, 380, 235)}</div>'
           f'<span style="width:52px;height:52px;border-radius:26px;background:{OKS};display:flex;align-items:center;justify-content:center;margin-top:44px">{ic("check-line", 26, OK)}</span>'
           f'<h1 style="margin:22px 0 0;font:600 56px/1.05 {SANS};letter-spacing:-0.04em">{S["h"]}</h1><div style="margin-top:18px">{para(S["b"], 20, INK2, 620, True)}</div></section>')
    cards = ('<div style="display:flex;gap:24px;align-items:stretch">'
             + link_card("pricing", "Pricing", "US$1 per active pupil per month, with setup and training free.", "See pricing")
             + link_card("moving", "Moving to Campus", "How we move your records in four weeks.", "How we move your records")
             + link_card("pricesheet", "The price sheet", "One page to take to your SDC or board.", "Download the price sheet (PDF)") + '</div>')
    nxt = wrap(f'<div style="font:600 22px {SANS};letter-spacing:-0.015em;margin-bottom:24px;text-align:center">{S["next_h"]}</div>{cards}')
    return [nav_bar(None, W) + top, gap(120) + nxt, gap()] + [PG.site_footer()]


# ---- Sign in (the app) ----------------------------------------------------------------------------------
def signin():
    S = SW.SIGNIN
    school = (f'<div style="display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:14px;background:{PLATE}">{nav_icons.nav_icon("t-day", 36)}'
              f'<div style="flex:1"><div style="font:400 12.5px {SANS};color:{MUTED}">School</div><div style="font:600 15px {SANS}">{S["school"]}</div></div>'
              f'<span style="font:500 14px {SANS};color:{BLUE}">Change</span></div>')
    pw = field("Password", "••••••••••", w=400).replace("••••••••••</span>", f'••••••••••</span><span style="font:500 13px {SANS};color:{BLUE}">Show</span>', 1)
    form = (f'<div style="width:400px"><div style="font:600 34px/1.1 {SANS};letter-spacing:-0.03em">{S["h"]}</div>'
            f'<div style="margin-top:32px">{field("Email or phone number", "rudo.moyo@gmail.com", w=400)}</div>'
            f'<div style="margin-top:18px">{pw}</div>'
            f'<div style="display:flex;justify-content:space-between;align-items:center;margin-top:16px">{check("Keep me signed in on this device", True)}<span style="font:500 14px {SANS};color:{BLUE}">Forgot password?</span></div>'
            f'<div style="display:flex;margin-top:26px">{cbtn("Sign in", "arrow-right-line", "primary", "lg").replace("display:inline-flex", "display:flex;flex:1;justify-content:center", 1)}</div>'
            f'</div>')
    left = (f'<div style="width:640px;height:900px;box-sizing:border-box;padding:48px 120px;display:flex;flex-direction:column">'
            f'<div>{lockup(24, by=False)}</div><div style="flex:1;display:flex;align-items:center">{form}</div>'
            f'<div style="display:flex;gap:20px;font:400 13px {SANS};color:{MUTED}"><span>Privacy</span><span>Terms</span><span>Support</span><span style="margin-left:auto">© 2026 Corelith Labs</span></div></div>')
    portals = "".join(f'<span style="display:inline-flex;align-items:center;gap:6px;height:36px;padding:0 12px 0 5px;border-radius:18px;background:rgba(255,255,255,.94);font:500 13.5px {SANS};color:{INK}">'
                      f'{portal_art.portal_icon(n, 26)}{n}</span>' for n in PORTAL_NAMES)
    right = (f'<div style="position:relative;flex:1;height:900px;padding:24px 24px 24px 0;box-sizing:border-box"><div style="position:relative;width:100%;height:100%;border-radius:28px;overflow:hidden">'
             f'<img src="{PH("boys-reading-2.jpg")}" alt="" style="width:100%;height:100%;object-fit:cover;object-position:47% 42%">'
             f'<div style="position:absolute;left:24px;bottom:24px;display:flex;gap:8px">{portals}</div></div></div>')
    return f'<div style="width:1440px;height:900px;display:flex;background:#fff;font-family:{SANS};color:{INK}">{left}{right}</div>'


# ---- footer pages -------------------------------------------------------------------------------------------
def contact_secs():
    C = SW.CONTACT
    top = PG.page_hero(C["eyebrow"], "contact", C["h"], C["b"], demo_btns(), "")
    routes = wrap('<div style="display:flex;gap:24px;align-items:stretch">' + "".join(link_card(k, t, d, a) for k, t, d, a in C["routes"]) + '</div>')
    topics = "".join(filter_pill(t, i == 0) for i, t in enumerate(C["topics"]))
    form = (f'<div style="width:520px;display:flex;flex-direction:column;gap:20px">{PG.eyebrow(C["form_h"], "contact")}{PG.head(C["form_hh"], 44, 520)}{para(C["form_b"], 18, INK2, 500)}'
            f'<div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:8px">{topics}</div>'
            f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:4px">{field("Your name", "Chipo Mutasa", w=250)}{field("Email", "head@mukuvisi.ac.zw", w=250)}</div>'
            f'{field("Organisation", "Mukuvisi High School", w=520)}'
            f'{field("Message", "", "What would you like to ask?", kind="area", w=520)}'
            f'<div style="display:flex;margin-top:6px">{cbtn("Send message", "send-plane", "primary", "lg")}</div></div>')
    pic = photo_story("office-documents.jpg", "center 30%", [(0, 250, HR.tagged("Campus team", SC.thread_card(340)))], 620, 640)
    body = (f'<section style="background:{PLATE};padding:{GAP - 40}px {X}px"><div style="display:flex;justify-content:space-between;align-items:center">'
            f'{form}{pic}</div></section>')
    return [nav_bar(None, W) + top, routes, gap() + body] + footer_secs()


def support_secs():
    S = SW.SUPPORT
    search = (f'<div style="width:640px;height:60px;border-radius:30px;background:#fff;box-shadow:0 0 0 1px {LINE},{SH_CARD};display:flex;align-items:center;gap:12px;padding:0 24px;box-sizing:border-box">'
              f'{ic("search", 20, MUTED)}<span style="font:400 17px {SANS};color:{FAINT}">Search the guides, for example “match an EcoCash payment”</span></div>')
    top = PG.page_hero(S["eyebrow"], "support", S["h"], S["b"], "", search)
    tp = "".join(f'<div style="border-radius:24px;background:{PLATE};padding:28px;display:flex;flex-direction:column">{nav_icons.nav_icon(k, 48)}'
                 f'<div style="font:600 22px {SANS};letter-spacing:-0.015em;margin-top:20px">{t}</div><div style="margin-top:12px">'
                 + "".join(f'<div style="display:flex;justify-content:space-between;align-items:center;padding:11px 0;border-top:1px solid #e3e6eb;font:400 15px {SANS};color:{INK2}">{g}{ic("right-line", 14, FAINT)}</div>' for g in gs)
                 + '</div></div>' for k, t, gs in S["topics"])
    topics = wrap(sec_head("Guides", "support", "Find the guide for your job.") + f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:24px">{tp}</div>')
    arts = [cta_art.cta_scene("visit", 588, 220, 26, 294, 150, labels=False), cta_art.cta_scene("training", 588, 220, 26, 294, 150, labels=False)]
    reach = wrap(sec_head("Support", "support", S["reach_h"]) + '<div style="display:flex;gap:24px;align-items:stretch">'
                 + "".join(link_card(k, t, d, a, art=ar) for (k, t, d, a), ar in zip(S["reach"], arts)) + '</div>')
    return [nav_bar(None, W) + top, gap() + topics, gap() + reach] + footer_secs()


def legal_secs(key):
    L = SW.LEGAL[key]
    icon = {"privacy": "privacy", "data": "data", "terms": "terms"}[key]
    head_ = wrap(f'<div style="display:flex;flex-direction:column;gap:20px;padding-bottom:48px;border-bottom:1px solid {LINE}">{PG.eyebrow(L["title"], icon)}'
                 f'<h1 style="margin:0;font:600 56px/1.05 {SANS};letter-spacing:-0.04em;text-wrap:balance">{L["h"]}</h1>'
                 f'<div style="font:400 15px {SANS};color:{MUTED}">{SW.LEGAL_UPDATED}</div></div>', f"88px {X}px 0")
    toc = "".join(f'<div style="padding:9px 0 9px 14px;border-left:2px solid {BLUE if i == 0 else LINE};font:{"500" if i == 0 else "400"} 14.5px {SANS};color:{INK if i == 0 else MUTED}">{t}</div>'
                  for i, (t, _) in enumerate(L["sections"]))
    body = "".join(f'<div style="padding:{0 if i == 0 else 40}px 0 0"><h3 style="margin:0;font:600 24px/1.2 {SANS};letter-spacing:-0.015em">{t}</h3>'
                   f'<p style="margin:12px 0 0;font:400 18px/1.65 {SANS};color:{INK2}">{p}</p></div>' for i, (t, p) in enumerate(L["sections"]))
    others = [(k, v["title"]) for k, v in SW.LEGAL.items() if k != key]
    oth = "".join(f'<div style="flex:1;display:flex;align-items:center;gap:14px;padding:20px 22px;border-radius:20px;background:{PLATE}">{nav_icons.nav_icon(k, 40)}'
                  f'<span style="font:600 18px {SANS};flex:1">{t}</span>{ic("arrow-right-line", 16, BLUE)}</div>' for k, t in others)
    main = wrap(f'<div style="display:flex;gap:96px;padding-top:56px"><div style="width:280px;flex:none">{toc}</div>'
                f'<div style="flex:1;max-width:760px">{body}<div style="display:flex;gap:20px;margin-top:64px">{oth}</div></div></div>')
    return [nav_bar(None, W) + head_ + main, gap()] + [PG.site_footer()]

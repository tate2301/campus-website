# -*- coding: utf-8 -*-
"""The Campus moodboard: the reference sites, our own pictures, colour, type and words, on one board."""
from ds import *
import portal_art, cta_art
from canvasio import MOOD

W = 2880
REFS = [("veracross-k12.jpg", "Veracross · K-12", "Eyebrow, claim, proof: the row we use on every page."),
        ("veracross-tiles.jpg", "Veracross · departments", "A tile per department, one database at the centre."),
        ("isams.jpg", "iSAMS by Iris", "Cloud-based, one integrated record: how Campus is built."),
        ("veracross.jpg", "Veracross", "Typography carries the page."),
        ("rippling.jpg", "Rippling · platform", "Shared capabilities as cards under every product."),
        ("ps-connected.jpg", "PowerSchool · Connected OS", "The product organised by the people it serves."),
        ("interfolio.jpg", "Interfolio", "One product, one clear page."),
        ("basecamp.jpg", "Basecamp", "Plain words with a view of their own.")]


def img(src, w, h, r=16, pos="top", fit="cover", bg="#f4f5f7"):
    return (f'<div style="width:{w}px;height:{h}px;border-radius:{r}px;overflow:hidden;box-shadow:0 0 0 1px {LINE};background:{bg};flex:none">'
            f'<img src="{src}" alt="" style="display:block;width:100%;height:100%;object-fit:{fit};object-position:{pos}"></div>')


def note(t, d):
    return (f'<div style="margin-top:12px"><div style="font:600 16px {SANS}">{t}</div>'
            f'<div style="font:400 15px/1.5 {SANS};color:{MUTED};margin-top:2px">{d}</div></div>')


def section(t, sub, inner):
    return (f'<div style="margin-top:88px"><div style="display:flex;align-items:baseline;gap:18px;padding-bottom:18px;border-bottom:1px solid {LINE};margin-bottom:32px">'
            f'<span style="font:600 32px {SANS};letter-spacing:-0.02em">{t}</span><span style="font:400 18px {SANS};color:{MUTED}">{sub}</span></div>{inner}</div>')


def moodboard():
    cw = (W - 160 - 3 * 32) // 4                     # one column of four
    ch = round(cw * 0.72)
    big_w, big_h = 2 * cw + 32, 2 * ch + 32 + 2 * 70
    refs = [f'<div style="grid-column:span 2;grid-row:span 2">{img(MOOD + "corelith-street.jpg", big_w, big_h - 70, 20, "center", "contain", "#f3f4f8")}'
            f'{note("Corelith · platform street", "Our own isometric street. Campus reuses its parts, projection and labels on stems.")}</div>']
    refs += [f'<div>{img(MOOD + f, cw, ch)}{note(t, d)}</div>' for f, t, d in REFS]
    grid1 = f'<div style="display:grid;grid-template-columns:repeat(4,{cw}px);gap:32px;align-items:start">{"".join(refs)}</div>'

    import pages, dept_art
    hero_pic = tile(scaled(f'<div style="width:1440px;height:810px;overflow:hidden;background:#fff">{pages.hero()}</div>', big_w, round(big_w * 810 / 1440), big_w / 1440), big_w, round(big_w * 720 / 1280), "#fff")
    drawing = tile(scaled(iso_scene(), big_w, round(big_w * 720 / 1280), big_w / 1280), big_w, round(big_w * 720 / 1280), GROUND)
    ports = "".join(f'<div>{portal_thumb(n, cw, round(cw * 0.6))}{note(n + " portal", d)}</div>'
                    for n, d in (("Administration", "The admin block and the bursary queue."), ("Teacher", "Form 3B, cut away."),
                                 ("Parent", "A guardian's home behind its durawall."), ("Student", "The library and Tsavo House.")))
    photos = "".join(f'<div>{tile(dept_art.art(k, cw, ch, U=cw / 6.6), cw, ch, PLATE)}{note(n, d.split(". ")[0].rstrip(".") + ".")}</div>'
                     for n, sl, d, p_, k in [CP.DEPARTMENTS[i] for i in (0, 2, 7, 8)])
    people = "".join(f'<div>{ph(n, cw, ch, pos, 16)}{note(t, d)}</div>' for n, pos, t, d in PHOTOS[1:5])
    tw = (W - 160 - 2 * 32) // 3
    th = round(tw * 430 / 600)
    cta_notes = {"visit": ("Visit", "We arrive at the school with your forms and fee structure."),
                 "price": ("Price", "The bursar has the price sheet for 1,140 active pupils."),
                 "training": ("Training", "Your staffroom, trained at the school in weeks 3 and 4.")}
    ctas = "".join(f'<div>{tile(scaled(cta_art.cta_scene(k, 600, 430, 42, 300, 255), tw, th, tw / 600), tw, th, GROUND)}{note(*cta_notes[k])}</div>'
                   for k in ("visit", "price", "training"))
    cards = tile(scaled(cards_plate(), big_w, round(big_w * 720 / 1280), big_w / 1280), big_w, round(big_w * 720 / 1280), GROUND)
    cards_note = note("Cards", "One school's figures: fees, marks, receipts, the Head's view.")
    icons = "".join(f'<div style="display:flex;flex-direction:column;align-items:center;gap:20px">{portal_art.portal_icon(n, 180)}'
                    f'<span style="font:500 18px {SANS}">{n}</span></div>' for n in PORTAL_NAMES)
    icon_tile = tile(f'<div style="display:flex;justify-content:space-around;align-items:center;width:100%">{icons}</div>', big_w, round(big_w * 720 / 1280), GROUND, "display:flex;align-items:center")
    icons_note = note("Portal icons", "Each portal's object drawn small, used in the menu, pricing and tags.")
    grid2 = (f'<div style="display:grid;grid-template-columns:repeat(4,{cw}px);gap:32px;align-items:start">'
             f'<div style="grid-column:span 2">{hero_pic}{note("Type and a photograph", "The claim in big plain type; the people photographed, the product on its edges.")}</div>'
             f'<div style="grid-column:span 2">{drawing}{note("The drawing", "The school as one campus, each portal on its building.")}</div>'
             f'{ports}{photos}{people}'
             f'<div style="grid-column:span 4;display:grid;grid-template-columns:repeat(3,{tw}px);gap:32px">{ctas}</div>'
             f'<div style="grid-column:span 2">{cards}{cards_note}</div>'
             f'<div style="grid-column:span 2">{icon_tile}{icons_note}</div></div>')

    sw = "".join(f'<div style="flex:1"><div style="height:200px;border-radius:20px;background:{c};box-shadow:inset 0 0 0 1px rgba(11,12,20,.06)"></div>'
                 f'<div style="font:600 16px {SANS};margin-top:12px">{n}</div><div style="font:400 13px {MONO};color:{MUTED};margin-top:2px">{c.upper()}</div></div>'
                 for n, c in (("Ink", INK), ("Accent", BLUE), ("Campus", CAMPUS), ("Plate", PLATE), ("Ground", GROUND), ("Jacaranda", "#c9bdf0"), ("Field", "#dfe9d6")))
    type_ = (f'<div style="display:flex;gap:64px;align-items:flex-end"><span style="font:600 200px/0.8 {SANS};letter-spacing:-0.05em">Aa</span>'
             f'<div><div style="font:600 64px/1.05 {SANS};letter-spacing:-0.035em">A school management platform that puts people first.</div>'
             f'<div style="font:400 22px/1.5 {SANS};color:{INK2};margin-top:16px;max-width:900px">Software for every department in your school, with one record at the centre. Campus runs in the cloud and keeps working without internet.</div>'
             f'<div style="font:400 15px {MONO};color:{MUTED};margin-top:16px">Atkinson Hyperlegible Next 400 · 500 · 600 · IBM Plex Mono for codes · R-2026-18824</div></div></div>')
    words = "".join(f'<span style="display:inline-flex;align-items:center;height:44px;padding:0 20px;border-radius:22px;background:#fff;box-shadow:inset 0 0 0 1px {LINE};font:500 18px {SANS}">{w_}</span>'
                    for w_ in ("puts people first", "one record", "every department", "cloud-based", "works without internet", "Head", "Form 3B", "EcoCash", "ZiG", "SDC", "bursar", "US$1 per active pupil per month"))
    grid3 = (f'<div style="display:flex;gap:20px">{sw}</div><div style="margin-top:56px">{type_}</div>'
             f'<div style="display:flex;flex-wrap:wrap;gap:12px;margin-top:56px">{words}</div>')

    head = (f'<div style="display:flex;align-items:center;justify-content:space-between;padding-bottom:22px;border-bottom:1px solid {LINE}">{lockup(26)}'
            f'<span style="font:500 16px {SANS};color:{MUTED}">Moodboard · 1 October 2026</span></div>'
            f'<div style="display:flex;justify-content:space-between;align-items:flex-end;gap:80px;margin-top:56px">'
            f'<h1 style="margin:0;font:600 88px/1 {SANS};letter-spacing:-0.04em">Moodboard<br><span style="color:{FAINT}">Corelith Campus</span></h1>'
            f'<div style="width:760px">{para("The sites we learnt from: iSAMS for how Campus is built on one record, Veracross for the voice, the department split and type that carries the page. Below them, our own type, photographs, drawings, colour and words.", 20, INK2, 760)}</div></div>')
    body = (head + section("Reference sites", "What each one gave us", grid1)
            + section("Campus", "Type, photographs, the drawing, portals, departments, calls to action and cards", grid2)
            + section("Colour, type and words", "One accent, one family, the school's own nouns", grid3))
    return f'<div style="width:{W}px;background:#fff;padding:80px 80px 120px;box-sizing:border-box;font-family:{SANS};color:{INK}">{body}</div>'

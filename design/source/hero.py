# -*- coding: utf-8 -*-
"""The Home hero, direction AB. The photograph carries the people; three cards carry the product, each tagged
with the portal it comes from; the drawing starts just below the fold and names the same portals on the school."""
from ds import *


def tagged(tag, inner):
    """a product card with the portal it comes from on a tag above it"""
    return f'<div style="display:flex;flex-direction:column;align-items:flex-start;gap:8px">{portal_tag(tag)}{inner}</div>'


def att_card(w=230):
    return card(SB, f'{lab(SB, "Attendance today")}<div style="margin-top:8px">{fig(SB, "96.4%", 32)}</div>'
                    f'<div style="font:400 13px {SANS};color:{MUTED};margin-top:6px">1,099 of 1,140 pupils</div>'
                    f'<div style="margin-top:10px">{status(SB, "+0.8 on last week", "ok")}</div>', w, pad=18)


def note_card(w=330):
    return card(SB, f'<div style="display:flex;align-items:center;gap:10px">{pmark("Campus", 30, 8)}'
                    f'<div style="flex:1;min-width:0"><div style="font:600 14px {SANS}">To Rudo Moyo</div><div style="font:400 12.5px {SANS};color:{MUTED}">16:10 · from Ms Sibanda</div></div></div>'
                    f'<div style="font:400 14px/1.45 {SANS};color:{INK2};margin-top:10px">Tanaka scored 71% in Mathematics test 2. The class average was 64%.</div>', w, pad=16)


def hero_picture(w=1200, h=620):
    """the hero picture: a wide photograph, three cards on its edges, each tagged with its portal"""
    return (f'<div style="position:relative;width:{w}px;height:{h}px;flex:none">'
            f'<div style="position:absolute;left:90px;top:30px">{ph("boys-reading-2.jpg", w - 180, h - 30, "47% 42%", 24)}</div>'
            + at(0, 150, tagged("Teacher portal", register_card(SB, 300, offline=True)), 3)
            + at(w - 250, 0, tagged("Administration portal", att_card(250)), 2)
            + at(w - 360, h - 150, tagged("Parent portal", note_card(360)), 4)
            + '</div>')


def hero_section(w=1440, peek=True):
    H = CP.HERO
    top = (f'<div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:24px;padding:72px 120px 0">'
           f'<div style="display:flex">{portal_tag("Corelith 1.0 is open")}</div>'
           f'<h1 style="margin:0;font:600 66px/1.04 {SANS};letter-spacing:-0.038em;max-width:1200px">{H["h1a"]}</h1>'
           f'{para(H["body"], 19, INK2, 720, True)}'
           f'<div style="display:flex;gap:12px;align-items:center;margin-top:6px">{cbtn(H["cta"], "calendar", "primary", "lg")}{cbtn(H["cta2"], "right-line", "secondary", "lg")}</div>'
           f'<div style="display:flex;gap:22px;justify-content:center">'
           + "".join(f'<span style="display:inline-flex;align-items:center;gap:7px;font:500 14px {SANS};color:{INK2}">{ic("check-circle", 15, OK)}{t}</span>'
                     for t in ("Setup and training free", "First month free", "US$1 per active pupil per month"))
           + '</div></div>')
    pic = f'<div style="display:flex;justify-content:center;padding:44px 120px 96px">{hero_picture()}</div>'
    band = ""
    if peek:
        svg, labels = ISO.scene()
        sc = f'<div style="position:relative;width:1280px;height:720px">{svg}{ISO.pills(labels, ic)}</div>'
        band = (f'<div style="margin:0 60px;border-radius:32px 32px 0 0;{DOTS};box-shadow:inset 0 0 0 1px #eceef2;padding:64px 60px 0;height:420px;overflow:hidden;position:relative">'
                f'{sec_head(*CP.PORTALS_H, CP.PORTALS_B, w=1200)}'
                f'<div style="position:absolute;left:20px;top:190px">{sc}</div></div>')
    return f'<div style="width:{w}px;background:#fff;font-family:{SANS};color:{INK}">{nav_bar(w=w)}{top}{pic}{band}</div>'


def hero_phone():
    H = CP.HERO
    pic = (f'<div style="position:relative;width:350px;margin-top:6px">{ph("boys-reading-2.jpg", 350, 250, "60% 40%", 20)}'
           f'<div style="margin:-56px 14px 0;position:relative;z-index:2">{tagged("Teacher portal", register_card(SB, 322, offline=True))}</div></div>')
    body = (f'<div style="padding:32px 20px 32px;display:flex;flex-direction:column;gap:18px">'
            f'<h1 style="margin:0;font:600 38px/1.06 {SANS};letter-spacing:-0.035em;text-wrap:balance">{H["h1a"]}</h1>'
            f'<div style="font:400 16.5px/1.55 {SANS};color:{INK2}">{H["body_phone"]}</div>'
            f'<div style="display:flex;flex-direction:column;gap:10px"><div style="display:flex">{cbtn(H["cta"], "calendar", "primary", "lg")}</div>'
            f'<div style="font:400 14px {SANS};color:{MUTED}">{H["note"]}</div></div>{pic}</div>')
    bar = (f'<div style="height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 20px;border-bottom:1px solid {LINE}">{lockup(20, by=False)}'
           f'<span style="width:40px;height:40px;border-radius:20px;box-shadow:inset 0 0 0 1px {LINE};display:flex;align-items:center;justify-content:center">{__import__("campus_mark").menu_icon(20)}</span></div>')
    return f'<div style="width:390px;background:#fff;font-family:{SANS};color:{INK}">{bar}{body}</div>'


def hero_art():
    """the hero picture alone at 1280 x 720 for export"""
    return f'<div style="position:relative;width:1280px;height:720px;background:#fff;display:flex;align-items:center;justify-content:center">{scaled(hero_picture(), 1240, 641, 1240 / 1200)}</div>'

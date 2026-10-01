# -*- coding: utf-8 -*-
"""Rough heroes, 1280 x 720, one per direction."""
from landing import *


def hero_a():
    svg, labels = ISO.scene()
    return f'<div style="position:relative;width:1280px;height:720px;background:#f7f8fa radial-gradient(#dfe2e8 1px,transparent 1.2px) 0 0/22px 22px">{svg}{ISO.pills(labels, ic)}</div>'


def hero_b():
    return (f'<div style="position:relative;width:1280px;height:720px;background:#fff;overflow:hidden">'
            f'<div style="position:absolute;left:250px;top:40px">{ph("boys-reading-2.jpg", 980, 640, "58% 40%", 32)}</div>'
            + at(60, 250, register_card(SB, 320, offline=True), 2)
            + at(1000, 80, card(SB, f'{lab(SB, "Attendance today")}<div style="margin-top:8px">{fig(SB, "96.4%", 32)}</div><div style="margin-top:10px">{status(SB, "1,099 of 1,140", "ok")}</div>', pad=20), 2)
            + at(880, 560, card(SB, f'<div style="display:flex;align-items:center;gap:10px">{ic("message-3", 18, BLUE)}<span style="font:500 15px {SANS}">Rudo Moyo: Tanaka scored 71% in test 2</span></div>', pad=16), 3)
            + at(430, 590, card(SB, f'<div style="display:flex;align-items:center;gap:10px">{ic("wallet-3", 18, OK)}<span style="font:500 15px {SANS}">EcoCash US$500.00 received · R-2026-18511</span></div>', pad=16), 3)
            + '</div>')


def hero_c():
    return f'<div style="position:relative;width:1280px;height:720px;background:#fff;padding:52px 0 0 60px;box-sizing:border-box">{report_object(1180, 660, 600, 0)}</div>'

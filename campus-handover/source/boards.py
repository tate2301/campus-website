# -*- coding: utf-8 -*-
"""Brand boards for the gate: family, one sentence, the rough hero, the rule sheet's headings, the risk."""
from landing import *

OUT = "file:///home/claude/campus/out/"
D = {
    "a": dict(fam="Isometric scene", line="Mukuvisi High School drawn as one campus with the Corelith street's parts; each portal is labelled on the building where it is used.",
              why="Closest to how Corelith already looks: the street, the product sites.",
              pal=[("#2563eb", "Accent: roofs, portal tiles"), ("#f7f8fa", "Ground, dot grid"), ("#dde1e7", "Wall greys"), ("#c9bdf0", "Jacaranda, a little"), ("#dfe9d6", "Field")],
              type_=("Atkinson Hyperlegible Next", "600 · 500 · 400", SANS), labels="Portal pills with a blue tile on a stem; modules as grey chips",
              risk="It sits so close to the Corelith street that Campus may read as one more Corelith building, not a school system; the school's own detail has to carry it."),
    "b": dict(fam="Photo + UI collage", line="Pupils and teachers photographed at school, with the product's own cards laid over each photo's edge.",
              why="Product-first, and the brief asks for real people in real schools.",
              pal=[("#2563eb", "Accent: buttons, active tab"), ("#ffffff", "Ground"), ("#f4f5f7", "Trays"), ("#12805c", "Status only"), ("#7c5cff", "Portal tag")],
              type_=("Atkinson Hyperlegible Next", "Big figures at 600, round pills", SANS), labels="The cards are the labels; round status pills with a dot",
              risk="Leans on stock photography until Corelith photographs a school, and stock can make it look like every other school site."),
    "c": dict(fam="Editorial, documents", line="Tanaka's term report is the object; the margin says which portal wrote each line.",
              why="The reach: no school-software site in the ledger uses the school's own paperwork as the picture.",
              pal=[("#2563eb", "Accent: numbers, notes"), ("#ffffff", "Paper and ground"), ("#0b0c14", "Ink rules"), ("#e3e6eb", "Hairlines"), ("#a15c07", "Register marks only")],
              type_=("Newsreader with Plex Mono", "Serif figures, mono labels", SERIF), labels="Margin notes: mono label, one sentence, dashed leader",
              risk="Quiet and text-heavy. A Head skimming may not see that this is software, so product screens have to come in early on every page."),
}


LBL = '<div style="font:400 15px/1.55 ' + SANS.replace("{", "{{").replace("}", "}}") + ';color:#3b3d47">{}</div>'


def board(k):
    d = D[k]
    sw = "".join(f'<div style="display:flex;align-items:center;gap:12px;padding:8px 0;border-top:1px solid {LINE}"><span style="width:28px;height:28px;border-radius:6px;background:{c};box-shadow:inset 0 0 0 1px rgba(11,12,20,.08)"></span>'
                 f'<span style="font:400 14px {SANS};color:{INK2}">{t}</span><span style="flex:1"></span>{mono(c.upper() if c.startswith("#") else c)}</div>' for c, t in d["pal"])
    col = lambda h, inner: f'<div style="flex:1;display:flex;flex-direction:column;gap:10px"><div style="font:600 15px {SANS}">{h}</div>{inner}</div>'
    typ = (f'<div style="font:{"500" if k == "c" else "600"} 40px/1.1 {d["type_"][2]};letter-spacing:{"-0.01em" if k == "c" else "-0.03em"}">Form 3B · 71%</div>'
           f'<div style="font:400 14px {SANS};color:{MUTED}">{d["type_"][0]} · {d["type_"][1]}</div>')
    return (f'<div style="width:1440px;background:#fff;padding:64px 80px 72px;box-sizing:border-box">'
            f'<div style="display:flex;align-items:baseline;gap:18px"><span style="font:600 56px/1 {SANS};color:{BLUE}">{k.upper()}</span>'
            f'<span style="font:600 30px {SANS};letter-spacing:-0.02em">{d["fam"]}</span><span style="flex:1"></span>{lockup(22)}</div>'
            f'<div style="margin-top:14px;font:400 20px/1.5 {SANS};color:{INK2};max-width:1000px">{d["line"]}</div>'
            f'<div style="margin-top:6px;font:400 15px {SANS};color:{MUTED}">{d["why"]}</div>'
            f'<img src="{OUT}hero/{k}-rough.png" style="display:block;width:1280px;height:720px;margin-top:32px;border-radius:14px;box-shadow:0 0 0 1px {LINE}">'
            f'<div style="display:flex;gap:48px;margin-top:40px">{col("Palette and tokens", sw)}{col("Type", typ)}{col("Labels", LBL.format(d["labels"]))}</div>'
            f'<div style="margin-top:36px;padding:18px 22px;border-radius:12px;background:{WARNS};display:flex;gap:12px;align-items:flex-start;font:400 15.5px/1.5 {SANS};color:{WARN}">'
            f'{ic("alert", 18, WARN)}<span><b style="font-weight:600">Risk.</b> {d["risk"]}</span></div></div>')

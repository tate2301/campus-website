# -*- coding: utf-8 -*-
"""Place the website boards on the canvas's Website page, one row per top-level item of the navigation tree."""
import json, sys
from ds import CP
import site_words as SW
R = "/tmp/claude-0/-home-claude/bcef0de9-d748-5cac-a3e6-27f5c8608e47/scratchpad/campus-bk/project/"
c = json.load(open(R + "canvas.json"))
b = json.load(open("/home/claude/campus/out/site/built.json"))


def dims(name):
    if name in b:
        return b[name][0], b[name][1], b[name][2]
    v = c["boards"][name]
    return v["w"], v["h"], v["title"]


retitle = {"PG01-home.dc.html": "Website · Home · 1 of 2", "PG01b-home.dc.html": "Website · Home · 2 of 2", "Hero-phone.dc.html": "Website · Home · phone 390",
           "PG02-academics.dc.html": "Website · Solutions · Academics and student life", "PG03-moving.dc.html": "Website · Platform · Moving to Campus"}
f = lambda k: k + ".dc.html"
bands = [
    [["PG01-home.dc.html", "PG01b-home.dc.html"], ["Hero-phone.dc.html"]],
    [[f("WS-solutions")], ["PG02-academics.dc.html"]] + [[f("WS-sol-" + sl)] for n, sl, *_ in CP.DEPARTMENTS if sl != "academics"],
    [[f("WS-who")]] + [[f("WS-who-" + k[2:])] for n, k, d in CP.SCHOOL_TYPES] + [[f("WS-role-" + s)] for s in SW.ROLE_PAGES],
    [[f("WS-platform")], [f("WS-integrations")], ["PG03-moving.dc.html"]],
    [[f("WS-pricing")], [f("WS-price-sheet")]],
    [[f("WS-demo")], [f("WS-demo-sent")]],
    [[f("WS-signin")]],
    [[f("WS-contact")], [f("WS-support")], [f("WS-legal-privacy")], [f("WS-legal-data")], [f("WS-legal-terms")]],
]
mb = json.load(open("/home/claude/campus/out/mobile/built.json"))
PHONE = {"PG01-home.dc.html": "WM-home", "PG02-academics.dc.html": "WM-sol-academics", "PG03-moving.dc.html": "WM-moving"}


def phone_parts(desk):
    base = PHONE.get(desk) or ("WM-" + desk[3:-8] if desk.startswith("WS-") else None)
    return sorted([n for n, v in mb.items() if v[3] == base], key=lambda n: mb[n][4])


c["boards"].pop("Hero-phone.dc.html", None)                      # superseded by the full phone Home
bands[0] = [["PG01-home.dc.html", "PG01b-home.dc.html"]]
y, order = 0, []
for band in bands:
    x, bh = 0, 0
    for ci, col in enumerate(band):
        cy, cw = y, 0
        for name in col:
            w, h, t = dims(name)
            c["boards"][name] = {"w": w, "h": h, "title": retitle.get(name, t), "x": x, "y": cy, "page": "website"}
            order.append(name)
            cy += h + 80
            cw = max(cw, w)
        bh = max(bh, cy - 80 - y)
        phones = phone_parts(col[0])
        if phones:
            py = y
            for pn in phones:
                w, h, t = mb[pn][0], mb[pn][1], mb[pn][2]
                c["boards"][pn] = {"w": w, "h": h, "title": t, "x": x + cw + 80, "y": py, "page": "website"}
                order.append(pn)
                py += h + 80
            bh = max(bh, py - 80 - y)
            cw += 80 + 390
        x += cw + (240 if ci == 0 else 160)
    y += bh + 400
c["order"] = [o for o in c["order"] if o not in order and o != "Hero-phone.dc.html"] + order
json.dump(c, open(R + "canvas.json", "w"), indent=1)
print(len(order), y)

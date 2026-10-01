# -*- coding: utf-8 -*-
"""Build the website boards: render each page, split any page taller than an artboard between sections, write the .dc files."""
import os, sys, json
from PIL import Image
import canvasio
from crender import render
import webpages as ST
import site_words as SW
from ds import CP

OUT = "/home/claude/campus/out/site"
CAP = 7600


def registry():
    """(key, path title, sections fn or html fn, kind) in navigation order; kind 'secs' or 'html'"""
    R = []
    R.append(("WS-solutions", "Solutions", lambda: ST.solutions_secs()))
    for n, sl, d, p_, k in CP.DEPARTMENTS:
        if sl != "academics":
            R.append((f"WS-sol-{sl}", f"Solutions · {n}", (lambda s=sl: ST.dept_secs(s))))
    R.append(("WS-who", "Who we serve", lambda: ST.who_secs()))
    for n, k, d in CP.SCHOOL_TYPES:
        R.append((f"WS-who-{k[2:]}", f"Who we serve · {n}", (lambda k=k: ST.type_secs(k))))
    for sl, r in SW.ROLE_PAGES.items():
        R.append((f"WS-role-{sl}", f"Who we serve · {r['name']}", (lambda s=sl: ST.role_secs(s))))
    R.append(("WS-platform", "Platform", lambda: ST.platform_secs()))
    R.append(("WS-integrations", "Platform · Integrations", lambda: ST.integrations_secs()))
    R.append(("WS-pricing", "Pricing", lambda: ST.pricing_secs()))
    R.append(("WS-price-sheet", "Pricing · Price sheet (PDF, A4)", lambda: ST.price_sheet()))
    R.append(("WS-demo", "Book a demo", lambda: ST.demo_secs()))
    R.append(("WS-demo-sent", "Book a demo · Request sent", lambda: ST.sent_secs()))
    R.append(("WS-signin", "Sign in · app", lambda: ST.signin()))
    R.append(("WS-contact", "Footer · Contact", lambda: ST.contact_secs()))
    R.append(("WS-support", "Footer · Support", lambda: ST.support_secs()))
    for k in ("privacy", "data", "terms"):
        R.append((f"WS-legal-{k}", f"Footer · {SW.LEGAL[k]['title']}", (lambda k=k: ST.legal_secs(k))))
    return R


def heights(htmls, tag):
    pngs = render([(h, f"{OUT}/m/{tag}-{i}.png", 1) for i, h in enumerate(htmls)])
    return [Image.open(p).size[1] for p in pngs]


def build(only=None):
    res = {}
    items = [r for r in registry() if not only or r[0] in only]
    built = [(k, t, f()) for k, t, f in items]
    first = render([((ST.page(x) if isinstance(x, list) else x), f"{OUT}/{k}.png", 1) for k, t, x in built])
    for (k, t, x), png in zip(built, first):
        w, h = Image.open(png).size
        parts = [x]
        if isinstance(x, list) and h > CAP:
            hs = heights([ST.page([s]) for s in x], k)
            parts, cur, ch = [], [], 0
            for s, sh in zip(x, hs):
                if cur and ch + sh > CAP:
                    parts.append(cur); cur, ch = [], 0
                cur.append(s); ch += sh
            parts.append(cur)
        n = len(parts)
        for i, pt in enumerate(parts):
            key = k if n == 1 else f"{k}-{i + 1}"
            title = "Website · " + t + ("" if n == 1 else f" · {i + 1} of {n}")
            html = ST.page(pt) if isinstance(pt, list) else pt
            if n > 1:
                p = render([(html, f"{OUT}/{key}.png", 1)])[0]
                w, h = Image.open(p).size
            name = key + ".dc.html"
            open(os.path.join(canvasio.R, "project", name), "w").write(canvasio.dc(title, html, w, h))
            res[name] = (w, h, title, k, i)
        print(k, n, h, flush=True)
    return res


if __name__ == "__main__":
    only = sys.argv[1:] or None
    r = build(only)
    old = {}
    p = f"{OUT}/built.json"
    if os.path.exists(p):
        old = json.load(open(p))
    old.update(r)
    json.dump(old, open(p, "w"), indent=1)

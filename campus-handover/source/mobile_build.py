# -*- coding: utf-8 -*-
"""Build the phone boards (390 wide), splitting any page taller than an artboard between sections."""
import os, sys, json
from PIL import Image
import canvasio
from crender import render
import mobile as M
import site_words as SW
from ds import CP

OUT = "/home/claude/campus/out/mobile"
CAP = 7990


def registry():
    R = [("WM-home", "Home", M.home), ("WM-solutions", "Solutions", M.solutions), ("WM-sol-academics", "Solutions · Academics and student life", M.academics)]
    for n, sl, d, p_, k in CP.DEPARTMENTS:
        if sl != "academics":
            R.append((f"WM-sol-{sl}", f"Solutions · {n}", (lambda s=sl: M.dept(s))))
    R.append(("WM-who", "Who we serve", M.who))
    for n, k, d in CP.SCHOOL_TYPES:
        R.append((f"WM-who-{k[2:]}", f"Who we serve · {n}", (lambda k=k: M.type_page(k))))
    for sl, r in SW.ROLE_PAGES.items():
        R.append((f"WM-role-{sl}", f"Who we serve · {r['name']}", (lambda s=sl: M.role(s))))
    R += [("WM-platform", "Platform", M.platform), ("WM-integrations", "Platform · Integrations", M.integrations), ("WM-moving", "Platform · Moving to Campus", M.moving),
          ("WM-pricing", "Pricing", M.pricing), ("WM-demo", "Book a demo", M.demo), ("WM-demo-sent", "Book a demo · Request sent", M.sent), ("WM-signin", "Sign in · app", M.signin),
          ("WM-contact", "Footer · Contact", M.contact), ("WM-support", "Footer · Support", M.support)]
    for k in ("privacy", "data", "terms"):
        R.append((f"WM-legal-{k}", f"Footer · {SW.LEGAL[k]['title']}", (lambda k=k: M.legal(k))))
    return R


def build(only=None):
    res = {}
    items = [r for r in registry() if not only or r[0] in only]
    built = [(k, t, f()) for k, t, f in items]
    first = render([((M.mpage(x) if isinstance(x, list) else x), f"{OUT}/{k}.png", 1) for k, t, x in built])
    for (k, t, x), png in zip(built, first):
        w, h = Image.open(png).size
        parts = [x]
        if isinstance(x, list) and h > CAP:
            hs = [Image.open(q).size[1] for q in render([(M.mpage([s]), f"{OUT}/m/{k}-{i}.png", 1) for i, s in enumerate(x)])]
            parts, cur, ch = [], [], 0
            for s, sh in zip(x, hs):
                if cur and ch + sh > CAP:
                    parts.append(cur); cur, ch = [], 0
                cur.append(s); ch += sh
            parts.append(cur)
        n = len(parts)
        for i, pt in enumerate(parts):
            key = k if n == 1 else f"{k}-{i + 1}"
            title = "Website · " + t + " · phone" + ("" if n == 1 else f" · {i + 1} of {n}")
            html = M.mpage(pt) if isinstance(pt, list) else pt
            if n > 1:
                q = render([(html, f"{OUT}/{key}.png", 1)])[0]
                w, h = Image.open(q).size
            name = key + ".dc.html"
            open(os.path.join(canvasio.R, "project", name), "w").write(canvasio.dc(title, html, w, h))
            res[name] = (w, h, title, k, i)
        print(k, n, h, flush=True)
    return res


if __name__ == "__main__":
    r = build(sys.argv[1:] or None)
    p = f"{OUT}/built.json"
    old = json.load(open(p)) if os.path.exists(p) else {}
    if not sys.argv[1:]:
        old = {}
    # drop stale parts of the pages just rebuilt
    ks = {v[3] for v in r.values()}
    old = {n: v for n, v in old.items() if v[3] not in ks}
    old.update(r)
    os.makedirs(OUT, exist_ok=True)
    json.dump(old, open(p, "w"), indent=1)

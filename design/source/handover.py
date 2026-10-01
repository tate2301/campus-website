# -*- coding: utf-8 -*-
"""Build the Campus website handover for Claude Code: the reference renders, the exact HTML per route at both widths,
the content as JSON, tokens, the drawn assets as markup fragments, the photos and logos, the generator source and a
Playwright visual test. Output: /home/claude/campus/exports/campus-handover (and a zip beside it)."""
import os, re, json, shutil, glob
from PIL import Image
from crender import render
import canvasio
from ds import CP, FAQ
import words, site_words as SW
import pages as PG, webpages as WP, mobile as M
import mark_anim, fx
import nav_icons, campus_mark, dept_art, cta_art, portal_art, brands

ROOT = "/home/claude/campus"
OUT = f"{ROOT}/exports/campus-handover"
PHOTOS = f"{ROOT}/assets/photos"


def routes():
    """(route, slug, title, desktop html fn, phone html fn)"""
    full = lambda secs: (lambda: WP.page(secs()))
    mfull = lambda secs: (lambda: M.mpage(secs()))
    R = [("/", "home", "Home", PG.home, mfull(M.home)),
         ("/solutions", "solutions", "Solutions", full(WP.solutions_secs), mfull(M.solutions)),
         ("/solutions/academics", "solutions-academics", "Academics and student life", PG.dept_page, mfull(M.academics))]
    for n, sl, d, p_, k in CP.DEPARTMENTS:
        if sl != "academics":
            R.append((f"/solutions/{sl}", f"solutions-{sl}", n, full(lambda s=sl: WP.dept_secs(s)), mfull(lambda s=sl: M.dept(s))))
    R.append(("/who-we-serve", "who-we-serve", "Who we serve", full(WP.who_secs), mfull(M.who)))
    for n, k, d in CP.SCHOOL_TYPES:
        R.append((f"/who-we-serve/{k[2:]}", f"who-we-serve-{k[2:]}", n, full(lambda k=k: WP.type_secs(k)), mfull(lambda k=k: M.type_page(k))))
    for sl, r in SW.ROLE_PAGES.items():
        R.append((f"/who-we-serve/{sl}", f"who-we-serve-{sl}", r["name"], full(lambda s=sl: WP.role_secs(s)), mfull(lambda s=sl: M.role(s))))
    R += [("/platform", "platform", "Platform", full(WP.platform_secs), mfull(M.platform)),
          ("/platform/integrations", "platform-integrations", "Integrations", full(WP.integrations_secs), mfull(M.integrations)),
          ("/moving-to-campus", "moving-to-campus", "Moving to Campus", PG.switch_page, mfull(M.moving)),
          ("/pricing", "pricing", "Pricing", full(WP.pricing_secs), mfull(M.pricing)),
          ("/pricing/price-sheet.pdf", "price-sheet", "Price sheet (A4 PDF)", WP.price_sheet, None),
          ("/demo", "demo", "Book a demo", full(WP.demo_secs), mfull(M.demo)),
          ("/demo/sent", "demo-sent", "Request sent", full(WP.sent_secs), mfull(M.sent)),
          ("app:/sign-in", "sign-in", "Sign in (app)", WP.signin, M.signin),
          ("/contact", "contact", "Contact", full(WP.contact_secs), mfull(M.contact)),
          ("/support", "support", "Support", full(WP.support_secs), mfull(M.support))]
    for k, path in (("privacy", "privacy"), ("data", "data-ownership"), ("terms", "terms")):
        R.append((f"/legal/{path}", f"legal-{path}", SW.LEGAL[k]["title"], full(lambda k=k: WP.legal_secs(k)), mfull(lambda k=k: M.legal(k))))
    return R


HEAD = ("<!doctype html><html lang='en-GB'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
        "<title>{title}</title>" + canvasio.FONT.replace("&amp;", "&") +
        "<style>body{{margin:0}}*{{box-sizing:border-box;-webkit-font-smoothing:antialiased}}h1,h2,h3{{text-wrap:balance}}{extra}</style></head><body>")


def standalone(html, title, depth=2):
    extra = (mark_anim.CSS if "cmk-" in html else "") + (fx.HOVER if "cmp-hov" in html else "")
    rel = "../" * depth + "assets/photos/"
    html = html.replace("file://" + PHOTOS + "/", rel)
    assert "file://" not in html, "unmapped local file"
    return HEAD.format(title=title, extra=extra) + html + "</body></html>"


def to_jpg(png, jpg, maxh=None):
    im = Image.open(png).convert("RGB")
    im.save(jpg, quality=86, optimize=True)
    os.remove(png)


def build():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    for d in ("reference/desktop", "reference/phone", "html/desktop", "html/phone", "assets/photos", "assets/logos", "components", "content", "spec", "tests", "source"):
        os.makedirs(f"{OUT}/{d}", exist_ok=True)
    os.environ["CMK_FREEZE"] = "*{animation-play-state:paused!important;animation-delay:-3.5s!important}"
    R = routes()
    manifest, jobs = [], []
    for route, slug, title, dfn, mfn in R:
        d = dfn()
        jobs.append((d, f"{OUT}/reference/desktop/{slug}.png", 1))
        open(f"{OUT}/html/desktop/{slug}.html", "w").write(standalone(d, f"{title} · Corelith Campus"))
        entry = {"route": route, "slug": slug, "title": title, "desktop": {"width": 794 if slug == "price-sheet" else 1440, "html": f"html/desktop/{slug}.html", "reference": f"reference/desktop/{slug}.jpg"}}
        if mfn:
            m = mfn()
            jobs.append((m, f"{OUT}/reference/phone/{slug}.png", 2))
            open(f"{OUT}/html/phone/{slug}.html", "w").write(standalone(m, f"{title} · Corelith Campus"))
            entry["phone"] = {"width": 390, "html": f"html/phone/{slug}.html", "reference": f"reference/phone/{slug}.jpg", "reference_scale": 2}
        manifest.append(entry)
        print(slug, flush=True)
    for side in ("/desktop/", "/phone/"):                                   # one batch per width: the renderer keys temp files by name
        for png in render([j for j in jobs if side in j[1]]):
            to_jpg(png, png[:-4] + ".jpg")
    for e in manifest:
        for side in ("desktop", "phone"):
            if side in e:
                w, h = Image.open(f"{OUT}/{e[side]['reference']}").size
                e[side]["reference_px"] = [w, h]
                e[side]["height"] = h // e[side].get("reference_scale", 1)
    json.dump({"site": "Corelith Campus", "domain": "campus.corelith.co.zw", "app_domain": "app.campus.corelith.co.zw", "routes": manifest},
              open(f"{OUT}/spec/routes.json", "w"), indent=1)

    # photos actually used, logos
    used = set()
    for f in glob.glob(f"{OUT}/html/*/*.html"):
        used |= set(re.findall(r"assets/photos/([\w.-]+)", open(f).read()))
    for n in sorted(used):
        shutil.copy(f"{PHOTOS}/{n}", f"{OUT}/assets/photos/{n}")
    for n in ("corelith-logo.svg", "corelith-mark.svg"):
        shutil.copy(f"{ROOT}/assets/{n}", f"{OUT}/assets/logos/{n}")
    for n in ("ecocash-icon.png", "zimra-logo.png", "zimra-mark.png"):
        shutil.copy(f"{PHOTOS}/{n}", f"{OUT}/assets/logos/{n}")

    # drawn pieces as exact markup fragments, with a 2x preview each
    frags = {}
    frags["campus-mark-64"] = campus_mark.campus_mark(64)
    frags["campus-mark-24"] = campus_mark.campus_mark(24)
    frags["menu-icon"] = campus_mark.menu_icon(20)
    frags["menu-icon-open"] = campus_mark.menu_icon(20, True)
    frags["lockup-nav"] = __import__("common").lockup(24)
    frags["lockup"] = __import__("common").lockup(24, by=False)
    for k in sorted(nav_icons.ICONS):
        frags[f"icon-{k}"] = nav_icons.nav_icon(k, 48)
    for n in ("Administration", "Teacher", "Parent", "Student"):
        frags[f"portal-icon-{n.lower()}"] = portal_art.portal_icon(n, 48)
        frags[f"portal-scene-{n.lower()}"] = portal_art.portal_scene(n, 560, 400)
    for k in list(dept_art.DEPT_SCENES) + list(dept_art.TYPE_SCENES):
        frags[f"drawing-{k}"] = dept_art.art(k, 360, 230)
    for k in ("visit", "price", "training"):
        frags[f"cta-scene-{k}"] = cta_art.cta_scene(k, 600, 430, 42, 300, 255)
    frags["schools-campus"] = dept_art.schools_campus(600, 420)
    frags["mark-journey"] = mark_anim.mark_journey(620, 460)
    frags["integrations-sketch"] = PG.pic_integrations(620, 420)
    for n in brands.REF:
        frags[f"logo-{n.lower().replace(' ', '-')}"] = brands.logo(n, 48)
    pj = []
    for k, v in frags.items():
        open(f"{OUT}/components/{k}.html", "w").write(v.replace("file://" + PHOTOS + "/", "../assets/photos/"))
        pj.append((f'<div style="display:inline-block;padding:8px;background:#fff">{v}</div>', f"{OUT}/components/{k}.png", 2))
    render(pj)
    open(f"{OUT}/components/mark-journey.css", "w").write(mark_anim.CSS)
    open(f"{OUT}/components/hover-reveal.css", "w").write(fx.HOVER)

    # content: every string the pages use, from the two copy modules
    def dump(mod):
        out = {}
        for k, v in vars(mod).items():
            if k.isupper() and isinstance(v, (str, list, dict, tuple)):
                out[k] = v
        return out
    json.dump({"words": dump(words), "site_words": dump(SW), "faq_pricing": FAQ, "ctas": __import__("ds").CTAS, "marketplace": __import__("site_cards").MARKET},
              open(f"{OUT}/content/copy.json", "w"), indent=1, ensure_ascii=False, default=list)

    # tokens and direction
    shutil.copy(f"{ROOT}/direction/tokens.json", f"{OUT}/spec/tokens.json")
    for n in ("rules.md", "voice.md", "positioning.md"):
        shutil.copy(f"{ROOT}/direction/{n}", f"{OUT}/spec/{n}")
    shutil.copy(f"{ROOT}/refs/assets.md", f"{OUT}/spec/assets-and-licences.md")
    # generator source, the ground truth for every value
    for f in glob.glob(f"{ROOT}/kit/*.py"):
        shutil.copy(f, f"{OUT}/source/")
    return manifest


if __name__ == "__main__":
    m = build()
    print(len(m), "routes")

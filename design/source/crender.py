"""render a list of (html, out_png, width) with one browser; html is the inner markup"""
import os, json, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
FONTS = open(os.path.join(ROOT, "direction", "fonts.css")).read()
BATCH = "/home/claude/corelith-co/brandkit/batch.mjs"
TMP = os.path.join(ROOT, "tmp"); os.makedirs(TMP, exist_ok=True)


def render(items, scale=1):
    jobs = []
    for html, out, *rest in items:
        p = os.path.join(TMP, os.path.basename(out).replace(".png", ".html"))
        if "cmk-" in html:
            import mark_anim
            html = f"<style>{mark_anim.CSS}{os.environ.get('CMK_FREEZE', '')}</style>" + html
        if "cmp-hov" in html:
            import fx
            html = f"<style>{fx.HOVER}{os.environ.get('CMP_HOVER', '')}</style>" + html
        open(p, "w").write(f"<!doctype html><html><head><meta charset='utf-8'><style>{FONTS}body{{margin:0}}*{{box-sizing:border-box;-webkit-font-smoothing:antialiased}}</style></head>"
                           f"<body><div id='art' style='display:inline-block'>{html}</div></body></html>")
        os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
        jobs.append({"in": p, "out": os.path.abspath(out), "scale": rest[0] if rest else scale})
    jp = os.path.join(TMP, "jobs.json"); json.dump(jobs, open(jp, "w"))
    subprocess.run(["node", BATCH, jp], check=True, capture_output=True)
    return [j["out"] for j in jobs]

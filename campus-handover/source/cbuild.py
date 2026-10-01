# -*- coding: utf-8 -*-
"""Render boards, write them as canvas artboards, return their heights."""
import os, sys
from PIL import Image
import canvasio
from crender import render

OUT = "/home/claude/campus/out/canvas"
FILE = {"BK01-cover": "Main"}


def build(items):
    """items: (key, title, html_fn). Writes project/<key>.dc.html, returns {file: (w, h, title)}"""
    htmls = [(k, t, f()) for k, t, f in items]
    pngs = render([(h, f"{OUT}/{k}.png", 1) for k, t, h in htmls])
    res = {}
    for (k, t, h), p in zip(htmls, pngs):
        w, hh = Image.open(p).size
        name = FILE.get(k, k) + ".dc.html"
        open(os.path.join(canvasio.R, "project", name), "w").write(canvasio.dc(t, h, w, hh))
        res[name] = (w, hh, t)
    return res

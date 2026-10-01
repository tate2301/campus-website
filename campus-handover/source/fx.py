# -*- coding: utf-8 -*-
"""Shared interaction CSS for the canvas pages: hover cards that reveal a photograph behind the text (Veracross tiles)."""
HOVER = (".cmp-hov{position:relative;overflow:hidden;cursor:pointer}"
         ".cmp-hov .cmp-img{position:absolute;inset:0;opacity:0;transition:opacity .35s ease}"
         ".cmp-hov .cmp-img img{width:100%;height:100%;object-fit:cover;display:block}"
         ".cmp-hov .cmp-img::after{content:'';position:absolute;inset:0;background:linear-gradient(180deg,rgba(11,12,20,.15),rgba(11,12,20,.78))}"
         ".cmp-hov .cmp-txt{position:relative;transition:color .35s ease}"
         ".cmp-hov:hover .cmp-img{opacity:1}"
         ".cmp-hov:hover .cmp-txt,.cmp-hov:hover .cmp-txt *{color:#fff !important}")

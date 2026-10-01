# -*- coding: utf-8 -*-
"""Real third-party marks, flat and unaltered: Iconify logo sets where they exist, the EcoCash app icon as an image.
ZIMRA's mark is the emblem from the logo on zimra.co.zw, cropped for small sizes."""
from common import *
import sys
sys.path.insert(0, "/root/.claude/plugins/synced/f83d1a09-511c-45a3-835c-21ea18df88cf_b7d94d8a-a046-4159-ad33-19d70dd8e185/saas-design~g2/lib")
from sdkit import icons as SI  # noqa: E402

REF = {"Sage Pastel": ("simple-icons:sage", "#00D639"), "QuickBooks": ("simple-icons:quickbooks", "#2CA01C"), "Xero": ("logos:xero", None),
       "Visa": ("logos:visa", None), "Mastercard": ("logos:mastercard", None), "WhatsApp": ("logos:whatsapp-icon", None),
       "Gmail": ("logos:google-gmail", None), "Google Workspace": ("logos:google-icon", None), "Microsoft 365": ("logos:microsoft-icon", None),
       "Microsoft Teams": ("logos:microsoft-teams", None), "Google Meet": ("logos:google-meet", None), "Zoom": ("logos:zoom-icon", None),
       "Google Drive": ("logos:google-drive", None), "OneDrive": ("logos:microsoft-onedrive", None), "Excel": ("vscode-icons:file-type-excel", None),
       "Google Calendar": ("logos:google-calendar", None), "Moodle": ("simple-icons:moodle", "#F98012")}


def logo(name, size=28):
    """the brand's mark centred in a size x size box"""
    box = f"width:{size}px;height:{size}px;display:inline-flex;align-items:center;justify-content:center;flex:none"
    if name == "EcoCash":
        return f'<span style="{box}"><img src="{PH("ecocash-icon.png")}" alt="EcoCash" style="width:{size}px;height:{size}px;border-radius:{round(size * .24)}px"></span>'
    if name in ("ZIMRA", "ZIMRA fiscalisation"):
        return f'<span style="{box}"><img src="{PH("zimra-mark.png")}" alt="ZIMRA" style="width:{size}px;height:{size}px;border-radius:{round(size * .24)}px;box-shadow:inset 0 0 0 1px #e7e9ef"></span>'
    if name == "Bank transfer":
        return f'<span style="{box};border-radius:{round(size * .24)}px;background:#eef0f3">{ic("bank-card", round(size * .56), INK2)}</span>'
    if name == "Cash":
        return f'<span style="{box};border-radius:{round(size * .24)}px;background:#eef0f3">{ic("coin-2", round(size * .56), INK2)}</span>'
    ref, col = REF[name]
    s = SI.svg(ref, round(size * (.62 if name in ("Visa", "Xero") else .86)), col)
    return f'<span style="{box}">{s}</span>'

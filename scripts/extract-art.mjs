#!/usr/bin/env node
// Fills src/art/registry.json with the drawn pieces from design/html.
//
// The site must be running with ART_COLLECT=1 (every <Art k="…"> renders as an <art-ph> placeholder):
//   ART_COLLECT=1 npx next dev -p 3100 &  node scripts/extract-art.mjs --base http://localhost:3100 [--only slug,slug]
//
// For each route and width, the placeholder's position (child indices from the page root) is looked up in the design's
// own HTML, parsed by the same browser, and the element there is stored under the placeholder's key. Because the
// position only lines up when the markup around it matches the design, a key that resolves to two different pieces
// (or to nothing) points at a structural difference in the port, and is reported.
import fs from "node:fs";
import path from "node:path";
import { chromium } from "@playwright/test";

const ROOT = path.resolve(import.meta.dirname, "..");
const DESIGN = path.join(ROOT, "design");
const REG = path.join(ROOT, "src/art/registry.json");
const args = Object.fromEntries(process.argv.slice(2).reduce((a, v, i, all) => (v.startsWith("--") ? [...a, [v.slice(2), all[i + 1]?.startsWith("--") ? true : all[i + 1] ?? true]] : a), []));
const BASE = args.base ?? "http://localhost:3100";
const only = typeof args.only === "string" ? args.only.split(",") : null;
const spec = JSON.parse(fs.readFileSync(path.join(DESIGN, "spec/routes.json"), "utf8"));
const registry = JSON.parse(fs.readFileSync(REG, "utf8"));

// in the page: every placeholder with its path from the page root of one layout
const COLLECT = (tree) => {
  const root = document.querySelector(`[data-tree="${tree}"]`)?.firstElementChild;
  if (!root) return null;
  const kids = (el) => [...el.children].filter((c) => !c.hasAttribute("data-extra"));
  const out = [];
  for (const ph of root.querySelectorAll("art-ph")) {
    const p = [];
    for (let el = ph; el !== root; el = el.parentElement) p.unshift(kids(el.parentElement).indexOf(el));
    out.push({ k: ph.dataset.k, path: p });
  }
  return out;
};
// in the design page: the element at each path
const RESOLVE = (paths) => {
  const root = document.body.firstElementChild;
  return paths.map((p) => {
    let el = root;
    for (const i of p) el = el?.children[i];
    return el ? el.outerHTML : null;
  });
};

// Pieces no exported page shows (the open menu icon, some icons at 48) come from design/components, whose
// parameters are known from their names. Scenes and drawings there have no recorded parameters and are not seeded.
const LOGO_NAME = { excel: "Excel", gmail: "Gmail", "google-calendar": "Google Calendar", "google-drive": "Google Drive", "google-meet": "Google Meet",
  "google-workspace": "Google Workspace", mastercard: "Mastercard", "microsoft-365": "Microsoft 365", "microsoft-teams": "Microsoft Teams", moodle: "Moodle",
  onedrive: "OneDrive", quickbooks: "QuickBooks", "sage-pastel": "Sage Pastel", visa: "Visa", whatsapp: "WhatsApp", xero: "Xero", zoom: "Zoom" };
const seedKey = (f) => {
  const n = f.replace(/\.html$/, "");
  if (n === "menu-icon") return "menu:20";
  if (n === "menu-icon-open") return "menu:20:open";
  if (n === "campus-mark-24") return "mark:24:6";
  if (n === "campus-mark-64") return "mark:64:17";
  if (n.startsWith("icon-")) return `nav:${n.slice(5)}:48`;
  if (n.startsWith("portal-icon-")) return `portal:${n[12].toUpperCase()}${n.slice(13)}:48`;
  // the call-to-action scenes in design/components are the CTA block's (600 x 430, U 42, centre 300,255)
  if (n.startsWith("cta-scene-")) return `cta:${n.slice(10)}:600x430:42,300,255`;
  if (n.startsWith("logo-")) return LOGO_NAME[n.slice(5)] ? `logo:${LOGO_NAME[n.slice(5)]}:48` : null;
  return null;
};
const seeded = {};
for (const f of fs.readdirSync(path.join(DESIGN, "components")).filter((f) => f.endsWith(".html"))) {
  const k = seedKey(f);
  if (k) seeded[k] = fs.readFileSync(path.join(DESIGN, "components", f), "utf8").trim();
}

// the price sheet is a PDF on the site; its source page is /print/price-sheet
const sitePath = (route) => (route.endsWith(".pdf") ? "/print/price-sheet" : route.replace(/^app:/, ""));

const browser = await chromium.launch();
const ctx = await browser.newContext();
await ctx.route(/^https?:\/\/(?!localhost)/, (r) => r.abort());  // the design pages need nothing from the network to be parsed
const site = await ctx.newPage();
const design = await ctx.newPage();
const conflicts = [];
const missing = [];
let added = 0;

// Seeds go first: a named fragment is what that drawing is, wherever a page puts it. (Pricing closes with the Price
// call to action, per rules.md, where the design's page draws Visit; matched by position, the page would say Visit.)
// They go through the browser too, so they are serialised exactly as the extracted pieces are.
for (const [k, html] of Object.entries(seeded)) {
  await design.setContent(`<body>${html}</body>`);
  const piece = await design.evaluate(() => document.body.firstElementChild.outerHTML);
  if (registry[k] === undefined) { registry[k] = piece; added++; }
  else if (registry[k] !== piece) conflicts.push(`design/components seed ${k} differs from the registry`);
}

for (const r of spec.routes) {
  if (only && !only.includes(r.slug)) continue;
  await site.goto(BASE + sitePath(r.route), { waitUntil: "domcontentloaded" });
  for (const side of ["desktop", "phone"]) {
    if (!r[side]) continue;
    const found = await site.evaluate(COLLECT, side);
    if (!found) { console.log(`· ${r.slug} ${side}: no layout yet`); continue; }
    const html = fs.readFileSync(path.join(DESIGN, r[side].html), "utf8").replace(/<link[^>]*>/g, "").replace(/<img /g, "<img loading=\"lazy\" ");
    await design.setContent(html, { waitUntil: "domcontentloaded" });
    const pieces = await design.evaluate(RESOLVE, found.map((f) => f.path));
    found.forEach(({ k, path: p }, i) => {
      const piece = pieces[i]?.replace(/ loading="lazy"/g, "");
      if (!piece) return missing.push(`${r.slug} ${side} ${k} at ${p.join(".")}`);
      if (registry[k] === undefined) { registry[k] = piece; added++; }
      else if (registry[k] !== piece) conflicts.push(`${r.slug} ${side} ${k} at ${p.join(".")}: ${piece.slice(0, 140)}`);
    });
    console.log(`· ${r.slug} ${side}: ${found.length} pieces`);
  }
}

await browser.close();

const sorted = Object.fromEntries(Object.keys(registry).sort().map((k) => [k, registry[k]]));
fs.writeFileSync(REG, JSON.stringify(sorted, null, 0).replace(/","/g, '",\n"') + "\n");
console.log(`\n${added} new pieces, ${Object.keys(registry).length} in the registry`);
if (missing.length) console.log(`\nNot found in the design (structure differs above it):\n  ${missing.join("\n  ")}`);
if (conflicts.length) console.log(`\nResolved to a different piece than before (structure differs, or the key needs another parameter):\n  ${conflicts.join("\n  ")}`);
process.exit(missing.length || conflicts.length ? 1 : 0);

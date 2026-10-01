#!/usr/bin/env node
// Prints /print/price-sheet to public/pricing/price-sheet.pdf: one A4 page, as reference/desktop/price-sheet.jpg.
// Needs the site running:  npm run build && npm run start   then   node scripts/price-sheet-pdf.mjs [--base http://localhost:3000]
import fs from "node:fs";
import path from "node:path";
import { chromium } from "@playwright/test";

const ROOT = path.resolve(import.meta.dirname, "..");
const i = process.argv.indexOf("--base");
const BASE = i > 0 ? process.argv[i + 1] : "http://localhost:3000";
const OUT = path.join(ROOT, "public/pricing/price-sheet.pdf");

const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 794, height: 1123 } });
await page.goto(`${BASE}/print/price-sheet`, { waitUntil: "networkidle" });
await page.evaluate(() => document.fonts.ready);
// A4 at 96 dpi is 794 x 1123: the sheet fills the page edge to edge
await page.addStyleTag({ content: "@page{size:A4;margin:0}html,body{margin:0}" });
fs.mkdirSync(path.dirname(OUT), { recursive: true });
await page.pdf({ path: OUT, format: "A4", printBackground: true, preferCSSPageSize: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
await browser.close();
console.log(`wrote ${path.relative(ROOT, OUT)} (${fs.statSync(OUT).size} bytes)`);

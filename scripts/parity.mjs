#!/usr/bin/env node
// Compares each page with the reference JPEG the acceptance test uses, and with the design's own HTML rendered by the
// same browser.
//
//   node scripts/parity.mjs [--base http://localhost:3000] [--only slug,slug] [--side desktop|phone]
//
// The references are JPEGs (quality 86), and JPEG alone moves 0.3-0.6% of a page's pixels past pixelmatch's
// threshold, so each line also reports that floor: the page's own render saved the same way. FLOOR means the page
// is within 0.1 points of it. The design HTML loads Google Fonts' current files, which differ slightly from the
// ones the references (and next/font) use, so "vs design" is a structural check, not a pixel one. See NOTES.md.
// Diffs are written to .parity/.
import fs from "node:fs";
import http from "node:http";
import path from "node:path";
import { chromium } from "@playwright/test";
import sharp from "sharp";
import pixelmatch from "pixelmatch";
import { EnvHttpProxyAgent, fetch as ufetch } from "undici";

const ROOT = path.resolve(import.meta.dirname, "..");
const DESIGN = path.join(ROOT, "design");
const OUT = path.join(ROOT, ".parity");
const args = Object.fromEntries(process.argv.slice(2).reduce((a, v, i, all) => (v.startsWith("--") ? [...a, [v.slice(2), all[i + 1]?.startsWith("--") ? true : all[i + 1] ?? true]] : a), []));
const BASE = args.base ?? "http://localhost:3000";
const only = typeof args.only === "string" ? args.only.split(",") : null;
const sides = args.side ? [args.side] : ["desktop", "phone"];
const spec = JSON.parse(fs.readFileSync(path.join(DESIGN, "spec/routes.json"), "utf8"));
const FREEZE = "*,*::before,*::after{animation-play-state:paused!important;animation-delay:-3.5s!important;transition:none!important;caret-color:transparent!important}";
fs.mkdirSync(path.join(OUT, "fonts"), { recursive: true });

// the design pages, served at their routes, one server per width
function serve(side) {
  const map = Object.fromEntries(spec.routes.filter((r) => r[side]).map((r) => [r.route.replace(/^app:/, ""), r[side].html]));
  const server = http.createServer((q, s) => {
    const u = decodeURIComponent(q.url.split("?")[0]);
    const f = map[u] ? path.join(DESIGN, map[u]) : path.join(DESIGN, u);
    if (!f.startsWith(DESIGN) || !fs.existsSync(f) || !fs.statSync(f).isFile()) { s.writeHead(404); return s.end(); }
    s.writeHead(200, { "content-type": f.endsWith(".html") ? "text/html" : f.endsWith(".png") ? "image/png" : "image/jpeg" });
    fs.createReadStream(f).pipe(s);
  });
  return new Promise((ok) => server.listen(0, () => ok({ server, url: `http://localhost:${server.address().port}` })));
}

// Google Fonts for the design pages, fetched by Node (which honours HTTPS_PROXY) and cached
const agent = process.env.HTTPS_PROXY || process.env.https_proxy ? new EnvHttpProxyAgent() : undefined;
async function fonts(route) {
  const url = route.request().url();
  const file = path.join(OUT, "fonts", Buffer.from(url).toString("base64url").slice(-120));
  if (!fs.existsSync(file)) {
    const res = await ufetch(url, { dispatcher: agent, headers: { "user-agent": route.request().headers()["user-agent"] } });
    fs.writeFileSync(file, Buffer.from(await res.arrayBuffer()));
    fs.writeFileSync(file + ".type", res.headers.get("content-type") ?? "");
  }
  await route.fulfill({ body: fs.readFileSync(file), contentType: fs.readFileSync(file + ".type", "utf8"), headers: { "access-control-allow-origin": "*" } });
}

async function shot(browser, url, width, scale) {
  const page = await browser.newPage({ viewport: { width, height: 900 }, deviceScaleFactor: scale });
  await page.route(/fonts\.(googleapis|gstatic)\.com/, fonts);
  await page.goto(url, { waitUntil: "networkidle" });
  await page.addStyleTag({ content: FREEZE });
  await page.evaluate(() => document.fonts.ready);
  const png = await page.screenshot({ fullPage: true });
  await page.close();
  return png;
}

async function compare(a, b, name) {
  const A = sharp(a).ensureAlpha(), B = sharp(b).ensureAlpha();
  const ma = await A.metadata(), mb = await B.metadata();
  if (ma.width !== mb.width) return { share: NaN, dh: mb.height - ma.height };
  const w = ma.width, h = Math.min(ma.height, mb.height);
  const ra = await A.extract({ left: 0, top: 0, width: w, height: h }).raw().toBuffer();
  const rb = await B.extract({ left: 0, top: 0, width: w, height: h }).raw().toBuffer();
  const diff = Buffer.alloc(w * h * 4);
  const bad = pixelmatch(ra, rb, diff, w, h, { threshold: 0.1 });
  if (name) await sharp(diff, { raw: { width: w, height: h, channels: 4 } }).png().toFile(path.join(OUT, name));
  return { share: bad / (w * h), dh: mb.height - ma.height };
}

const servers = Object.fromEntries(await Promise.all(sides.map(async (s) => [s, await serve(s)])));
const browser = await chromium.launch();
const pct = (x) => (Number.isNaN(x) ? "  width!" : (x * 100).toFixed(2).padStart(6) + "%");
let failed = 0;
for (const r of spec.routes) {
  if (r.route.endsWith(".pdf") || (only && !only.includes(r.slug))) continue;
  for (const side of sides) {
    const s = r[side];
    if (!s) continue;
    const scale = s.reference_scale ?? 1;
    const route = r.route.replace(/^app:/, "");
    const [mine, theirs] = [await shot(browser, BASE + route, s.width, scale), await shot(browser, servers[side].url + route, s.width, scale)];
    fs.writeFileSync(path.join(OUT, `${r.slug}-${side}.png`), mine);
    fs.writeFileSync(path.join(OUT, `${r.slug}-${side}.design.png`), theirs);
    const vsDesign = await compare(theirs, mine, `${r.slug}-${side}.diff.png`);
    const vsRef = await compare(fs.readFileSync(path.join(DESIGN, s.reference)), mine, `${r.slug}-${side}.ref-diff.png`);
    // the floor: the same render saved as the references were (JPEG, quality 86) differs from itself by this much
    const floor = await compare(mine, await sharp(mine).jpeg({ quality: 86, chromaSubsampling: "4:2:0" }).toBuffer());
    // PASS: the acceptance test's limits against the reference. FLOOR: within 0.1 points of what JPEG alone costs.
    const hOk = Math.abs(vsRef.dh / scale) <= 4;
    const verdict = hOk && vsRef.share <= 0.005 ? "PASS " : hOk && vsRef.share - floor.share <= 0.001 ? "FLOOR" : "FAIL ";
    if (verdict === "FAIL ") failed++;
    console.log(`${verdict} ${r.slug.padEnd(28)} ${side.padEnd(7)} vs design ${pct(vsDesign.share)} dh ${String(vsDesign.dh / scale).padStart(5)} | vs reference ${pct(vsRef.share)} dh ${String(vsRef.dh / scale).padStart(5)} (JPEG floor ${pct(floor.share)})`);
  }
}
await browser.close();
Object.values(servers).forEach(({ server }) => server.close());
process.exit(failed ? 1 : 0);

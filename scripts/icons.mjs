// The site's icons, from the drawn Campus mark (design/components/campus-mark-64.html), not redrawn:
//   src/og/mark.svg      the mark tile as a standalone SVG (the fragment's purple tile, 17px corners, clipped)
//   src/app/icon.svg     the same, for browser tabs
//   src/app/favicon.ico  32 and 48 px PNGs of it, for crawlers and older browsers
//   src/app/apple-icon.png  180 px, square (iOS rounds the corners itself)
// Run with `npm run icons` after the mark changes.
import { readFileSync, writeFileSync } from "node:fs";
import { chromium } from "playwright";

const frag = readFileSync("design/components/campus-mark-64.html", "utf8");
const inner = frag.match(/<svg[^>]*>([\s\S]*)<\/svg>/)[1];
const bg = frag.match(/background:(#[0-9a-f]{6})/i)[1];
const r = frag.match(/border-radius:(\d+)px/)[1];

const tile = (round) =>
  `<svg xmlns="http://www.w3.org/2000/svg" width="64" height="64" viewBox="0 0 64 64">` +
  (round ? `<clipPath id="t"><rect width="64" height="64" rx="${r}"/></clipPath><g clip-path="url(#t)">` : `<g>`) +
  `<rect width="64" height="64" fill="${bg}"/>${inner}</g></svg>\n`;

writeFileSync("src/og/mark.svg", tile(true));
writeFileSync("src/app/icon.svg", tile(true));

const browser = await chromium.launch();
const page = await browser.newPage();
async function png(svg, s) {
  await page.setViewportSize({ width: s, height: s });
  await page.setContent(`<style>html,body{margin:0;background:transparent}</style><img style="display:block;width:${s}px;height:${s}px" src="data:image/svg+xml;base64,${Buffer.from(svg).toString("base64")}">`);
  return page.screenshot({ omitBackground: true, type: "png" });
}
writeFileSync("src/app/apple-icon.png", await png(tile(false), 180));

// an ICO that holds PNGs (valid since Windows Vista and in every browser)
const sizes = [32, 48];
const pngs = [];
for (const s of sizes) pngs.push(await png(tile(true), s));
await browser.close();
const head = Buffer.alloc(6 + 16 * sizes.length);
head.writeUInt16LE(0, 0); head.writeUInt16LE(1, 2); head.writeUInt16LE(sizes.length, 4);
let off = head.length;
sizes.forEach((s, i) => {
  const e = 6 + 16 * i;
  head.writeUInt8(s, e); head.writeUInt8(s, e + 1); head.writeUInt16LE(1, e + 4); head.writeUInt16LE(32, e + 6);
  head.writeUInt32LE(pngs[i].length, e + 8); head.writeUInt32LE(off, e + 12);
  off += pngs[i].length;
});
writeFileSync("src/app/favicon.ico", Buffer.concat([head, ...pngs]));
console.log("icons written");

// General Sans (Indian Type Foundry, via Fontshare) for the whole site, fetched before every build and dev run.
//
// The ITF Free Font License (FFL 2.0) lets us self-host the font for our own website, but not hand the files out
// through a public repository, and not subset or convert them. This repository is public, so the files are not
// committed: this script downloads Fontshare's official package and copies the files the site uses, unmodified, into
// src/fonts/general-sans/ (git-ignored), and next/font/local serves them from the site.
//   *.woff2  the webfonts (next/font/local, src/app/fonts.ts)
//   *.ttf    for the shared-link images (Satori reads TTF, not WOFF2; src/og/card.tsx)
//   FFL.txt  the licence, as shipped in the package
// The package's files, not the ones Fontshare's CSS API serves: those are a different build whose small sizes render
// with gaps inside words in Chromium on Linux and Windows ("f ree").
import { existsSync, mkdirSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { inflateRawSync } from "node:zlib";

const DIR = "src/fonts/general-sans";
const ZIP = "https://api.fontshare.com/v2/fonts/download/general-sans";
const NAMES = { 400: "Regular", 500: "Medium", 600: "Semibold" };
const WANT = new Map([
  ...Object.entries(NAMES).flatMap(([w, n]) => [
    [`Fonts/WEB/fonts/GeneralSans-${n}.woff2`, `GeneralSans-${w}.woff2`],
    [`Fonts/WEB/fonts/GeneralSans-${n}.ttf`, `GeneralSans-${w}.ttf`],
  ]),
  ["License/FFL.txt", "FFL.txt"],
]);

if ([...WANT.values()].every((f) => existsSync(join(DIR, f)))) process.exit(0);

async function get(url) {
  for (let i = 1; ; i++) {
    try {
      const r = await fetch(url);
      if (!r.ok) throw new Error(`${r.status} ${r.statusText}`);
      return Buffer.from(await r.arrayBuffer());
    } catch (e) {
      if (i === 4) throw new Error(`fonts: could not fetch ${url}: ${e.message}`);
      await new Promise((ok) => setTimeout(ok, 1000 * 2 ** i));
    }
  }
}

/** the entries of a zip file, by name, read from its central directory (stored or deflated entries) */
function unzip(buf) {
  const eocd = buf.lastIndexOf(Buffer.from([0x50, 0x4b, 0x05, 0x06]));
  if (eocd < 0) throw new Error("fonts: the download is not a zip file");
  const count = buf.readUInt16LE(eocd + 10);
  let p = buf.readUInt32LE(eocd + 16);
  const out = new Map();
  for (let i = 0; i < count; i++) {
    const method = buf.readUInt16LE(p + 10), size = buf.readUInt32LE(p + 20);
    const nameLen = buf.readUInt16LE(p + 28), extraLen = buf.readUInt16LE(p + 30), commentLen = buf.readUInt16LE(p + 32);
    const local = buf.readUInt32LE(p + 42);
    const name = buf.toString("utf8", p + 46, p + 46 + nameLen);
    const start = local + 30 + buf.readUInt16LE(local + 26) + buf.readUInt16LE(local + 28);
    const data = buf.subarray(start, start + size);
    out.set(name, () => (method === 0 ? data : inflateRawSync(data)));
    p += 46 + nameLen + extraLen + commentLen;
  }
  return out;
}

const entries = unzip(await get(ZIP));
mkdirSync(DIR, { recursive: true });
for (const [suffix, file] of WANT) {
  const name = [...entries.keys()].find((n) => n.endsWith(suffix));
  if (!name) throw new Error(`fonts: ${suffix} is not in the General Sans package`);
  writeFileSync(join(DIR, file), entries.get(name)());
}
console.log(`fonts: General Sans ${Object.keys(NAMES).join("/")} in ${DIR}`);

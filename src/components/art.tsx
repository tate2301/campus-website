import "server-only";
import fs from "node:fs";
import path from "node:path";
import { createElement } from "react";
import { htmlToReact } from "@/lib/html-to-react";

/**
 * Every drawn piece on the site (the Campus mark, nav and portal icons, department and school drawings, the
 * call-to-action scenes, the mark journey, brand logos and interface glyphs) is rendered from the exact markup the
 * design was exported with. The pieces are kept in src/art/registry.json, keyed by what was drawn and at which size,
 * e.g. "nav:fees:48" or "cta:visit:600x430:42,300,255". scripts/extract-art.mjs fills the registry from design/html.
 *
 * With ART_COLLECT=1 each piece renders as a placeholder instead, which is how the extraction script finds where
 * every piece sits on a page.
 */
const FILE = path.join(process.cwd(), "src/art/registry.json");
let registry: Record<string, string> = {};
let stamp = 0;

function load() {
  const m = fs.statSync(FILE).mtimeMs;
  if (m !== stamp) {
    registry = JSON.parse(fs.readFileSync(FILE, "utf8"));
    stamp = m;
  }
  return registry;
}

export function hasArt(k: string) {
  return k in load();
}

export function Art({ k }: { k: string }) {
  if (process.env.ART_COLLECT === "1") return createElement("art-ph", { "data-k": k });
  const html = load()[k];
  if (html === undefined) {
    if (process.env.NODE_ENV === "production") throw new Error(`Missing drawing "${k}" in src/art/registry.json; run npm run art`);
    return createElement("art-ph", { "data-k": k, style: { display: "inline-block", outline: "2px dashed red", minWidth: 8, minHeight: 8 } });
  }
  return htmlToReact(html.replaceAll("../../assets/", "/assets/"));
}

import type { CSSProperties } from "react";
import { typeset } from "./type";

/**
 * Inline CSS, written the way design/html/*.html writes it, turned into a React style object.
 * The pages are ported value for value from that markup, so every size, colour and gap stays a literal
 * that can be checked against the source: sx("font:600 52px/1.08 var(--font-sans);letter-spacing:-0.034em").
 * Text in the site's sans is then typeset by src/lib/type.ts: its size is snapped to the type scale and its leading
 * and tracking follow from that size (the example renders as 600 48px/1.08 with -0.025em).
 */
const cache = new Map<string, CSSProperties>();

export function sx(css: string): CSSProperties {
  const hit = cache.get(css);
  if (hit) return hit;
  const out: Record<string, string> = {};
  for (const decl of splitTop(css, ";")) {
    const i = decl.indexOf(":");
    if (i < 0) continue;
    const prop = decl.slice(0, i).trim();
    const value = decl.slice(i + 1).trim();
    if (!prop || !value) continue;
    out[camel(prop)] = value;
  }
  typeset(out);
  cache.set(css, out);
  return out;
}

/** joins style fragments, skipping empty ones, for the places the source builds a style from parts */
export function cx(...parts: (string | false | null | undefined)[]): string {
  return parts.filter(Boolean).join(";");
}

function camel(prop: string): string {
  if (prop.startsWith("--")) return prop;
  const p = prop.startsWith("-ms-") ? prop.slice(1) : prop;
  return p.replace(/-([a-z])/g, (_, c: string) => c.toUpperCase());
}

/** split on a separator outside quotes and parentheses (url(), path('…'), gradients) */
export function splitTop(s: string, sep: string): string[] {
  const parts: string[] = [];
  let depth = 0;
  let quote: string | null = null;
  let start = 0;
  for (let i = 0; i < s.length; i++) {
    const ch = s[i];
    if (quote) {
      if (ch === quote) quote = null;
    } else if (ch === "'" || ch === '"') quote = ch;
    else if (ch === "(") depth++;
    else if (ch === ")") depth--;
    else if (ch === sep && depth === 0) {
      parts.push(s.slice(start, i));
      start = i + 1;
    }
  }
  parts.push(s.slice(start));
  return parts;
}

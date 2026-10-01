import "server-only";
import { createElement, Fragment, type ReactNode } from "react";
import { parse, type HTMLElement, type Node } from "node-html-parser";
import { sx } from "./sx";

/**
 * Turns a markup fragment from the design (a drawing, an icon, a logo) into React elements, element for element,
 * so the page's DOM is the design's DOM with no wrapper around it. Runs on the server only; the result is static HTML.
 */

// SVG and HTML attributes React spells in camelCase
const ATTR: Record<string, string> = {
  class: "className", for: "htmlFor", tabindex: "tabIndex", crossorigin: "crossOrigin",
  "xlink:href": "xlinkHref", "xml:space": "xmlSpace", "xmlns:xlink": "xmlnsXlink",
};
const KEEP = /^(aria-|data-)/;

function attrName(name: string): string {
  if (ATTR[name]) return ATTR[name];
  if (KEEP.test(name) || !name.includes("-")) return name;
  return name.replace(/-([a-z])/g, (_, c: string) => c.toUpperCase());
}

function toReact(node: Node, key: number): ReactNode {
  if (node.nodeType === 3) return (node as unknown as { text: string }).text;
  if (node.nodeType !== 1) return null;
  const el = node as HTMLElement;
  const props: Record<string, unknown> = { key };
  for (const [name, value] of Object.entries(el.attributes)) {
    if (name === "style") props.style = sx(value);
    else props[attrName(name)] = value;
  }
  const kids = el.childNodes.map((c, i) => toReact(c, i)).filter((c) => c !== null && c !== "");
  return createElement(el.rawTagName, props, ...(kids.length ? kids : []));
}

const cache = new Map<string, ReactNode>();

export function htmlToReact(html: string): ReactNode {
  const hit = cache.get(html);
  if (hit !== undefined) return hit;
  const root = parse(html, { lowerCaseTagName: false, comment: false });
  const kids = root.childNodes.map((c, i) => toReact(c, i));
  const out = kids.length === 1 ? kids[0] : createElement(Fragment, null, ...kids);
  cache.set(html, out);
  return out;
}

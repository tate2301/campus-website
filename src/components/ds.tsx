/**
 * The design system's building blocks, ported from design/source (common.py, landing.py, ui.py, ds.py, brandkit.py,
 * pages.py). Each component keeps the name of the function it ports and every value it draws with.
 */
import Image from "next/image";
import Link from "next/link";
import type { ReactNode } from "react";
import { Art } from "./art";
import { Ic } from "./icon";
export { Ic };
import { sx, cx } from "@/lib/sx";
import { BLUE, CAMPUS, DOTS, FAINT, INK, INK2, LINE, MUTED, NUM, OK, OKS, PLATE, SANS, WARN, WARNS, BAD, BADS, pyRound } from "@/lib/design";
import { PHOTO_ALT } from "@/content/photo-alt";

type Kids = { children?: ReactNode };

// ---- drawn pieces (src/art/registry.json) ------------------------------------------------------------
/** a page's drawn icon on its pale tile (nav_icons.nav_icon) */
export const NavIcon = ({ k, s, tile = true }: { k: string; s: number; tile?: boolean }) => <Art k={`nav:${k}:${s}${tile ? "" : ":bare"}`} />;
/** a portal's icon (portal_art.portal_icon) */
export const PortalIcon = ({ n, s, tile = true }: { n: string; s: number; tile?: boolean }) => <Art k={`portal:${n}:${s}${tile ? "" : ":bare"}`} />;
/** the Campus mark on its violet tile (campus_mark.campus_mark) */
export const Pmark = ({ s, r }: { s: number; r?: number }) => <Art k={`mark:${s}:${r ?? pyRound(s * 0.26)}`} />;
/** the Corelith logo (the company kit's logo(size, colour)) */
export const CorelithLogo = ({ s, c }: { s: number; c: string }) => <Art k={`corelith:${s}:${c}`} />;
/** the menu button's drawing, closed or open (campus_mark.menu_icon) */
export const MenuIcon = ({ s, open = false }: { s: number; open?: boolean }) => <Art k={`menu:${s}${open ? ":open" : ""}`} />;
/** a department or school type in its place (dept_art.art) */
export const DeptArt = ({ k, w, h, U }: { k: string; w: number; h: number; U: number }) => <Art k={`dept:${k}:${w}x${h}:U${U}`} />;
/** a call-to-action scene (cta_art.cta_scene) */
export const CtaScene = ({ k, w, h, U, cx: x, cy: y, labels = true }: { k: string; w: number; h: number; U: number; cx: number; cy: number; labels?: boolean }) =>
  <Art k={`cta:${k}:${w}x${h}:${U},${x},${y}${labels ? "" : ":nolabels"}`} />;
/** a portal's place (portal_art.portal_scene) */
export const PortalScene = ({ n, w, h, U, cx: x, cy: y, labels = true }: { n: string; w: number; h: number; U: number; cx: number; cy: number; labels?: boolean }) =>
  <Art k={`scene:${n}:${w}x${h}:${U},${x},${y}${labels ? "" : ":nolabels"}`} />;
/** the five kinds of school on one plate (dept_art.schools_campus) */
export const SchoolsCampus = ({ w, h, U = 28 }: { w: number; h: number; U?: number }) => <Art k={`schools:${w}x${h}:U${U}`} />;
/** a third-party mark (brands.logo) */
export const BrandLogo = ({ n, s }: { n: string; s: number }) => <Art k={`logo:${n}:${s}`} />;
/** an Iconify logo (pages.logo_of) */
export const LogoOf = ({ r, s, c }: { r: string; s: number; c: string }) => <Art k={`si:${r}:${s}:${c}`} />;

// ---- links ------------------------------------------------------------------------------------------------
/** an element drawn as a span in the design that is a link on the site: same box, same style */
export function A({ href, style, children, label }: { href?: string; style?: string; label?: string } & Kids) {
  if (!href) return <span style={style ? sx(style) : undefined}>{children}</span>;
  const s = style ? sx(style) : undefined;
  if (href.startsWith("http") || href.startsWith("#") || href.endsWith(".pdf")) return <a href={href} style={s} aria-label={label}>{children}</a>;
  // no viewport prefetch: a page carries dozens of links, and loading every route on arrival would hold up the page
  return <Link href={href} prefetch={false} style={s} aria-label={label}>{children}</Link>;
}

// ---- type -------------------------------------------------------------------------------------------------
/** landing.h2: a heading with an optional grey second line */
export function H2({ a, b = "", size = 44, font = SANS, w = 600, ls = "-0.03em", centre = false }: { a: ReactNode; b?: ReactNode; size?: number; font?: string; w?: number; ls?: string; centre?: boolean }) {
  return (
    <h2 style={sx(`margin:0;font:${w} ${size}px/1.1 ${font};letter-spacing:${ls};color:${INK};text-wrap:balance;${centre ? "text-align:center;" : ""}`)}>
      {a}{b ? <><br /><span style={sx(`color:${FAINT}`)}>{b}</span></> : null}
    </h2>
  );
}

/** landing.para */
export function Para({ t, size = 18, c = INK2, mw = 560, centre = false }: { t: ReactNode; size?: number; c?: string; mw?: number; centre?: boolean }) {
  return <p style={sx(`margin:0;font:400 ${size}px/1.6 ${SANS};color:${c};max-width:${mw}px;${centre ? "text-align:center;margin-left:auto;margin-right:auto;" : ""}`)}>{t}</p>;
}

/** landing.ticks */
export function Ticks({ items, c = INK2, icon = "check-circle", icC = BLUE, size = 15.5 }: { items: string[]; c?: string; icon?: string; icC?: string; size?: number }) {
  return <>{items.map((t, i) => (
    <div key={i} style={sx(`display:flex;gap:10px;align-items:flex-start;font:400 ${size}px/1.5 ${SANS};color:${c};padding:5px 0`)}>
      <span style={sx("padding-top:3px")}><Ic n={icon} s={16} c={icC} /></span>{t}
    </div>))}</>;
}

/** pages.eyebrow: blue, sentence case, with the page's drawn icon */
export function Eyebrow({ t, k, c = BLUE }: { t: ReactNode; k?: string | null; c?: string }) {
  return <div style={sx(`display:flex;align-items:center;gap:10px;font:500 15px ${SANS};color:${c};letter-spacing:0.005em`)}>{k ? <NavIcon k={k} s={30} /> : null}{t}</div>;
}

/** pages.head */
export function Head({ t, size = 52, w = 720, c = INK }: { t: ReactNode; size?: number; w?: number; c?: string }) {
  return <h2 style={sx(`margin:0;font:600 ${size}px/1.08 ${SANS};letter-spacing:-0.034em;color:${c};max-width:${w}px;text-wrap:balance`)}>{t}</h2>;
}

/** pages.explore: the tile's action, on one line */
export function Explore({ t = "Explore", href }: { t?: string; href?: string }) {
  return (
    <A href={href} style={`display:inline-flex;align-items:center;gap:6px;font:600 15px ${SANS};color:${INK}`}>
      {t}<Ic n="arrow-right-line" s={15} c={BLUE} />
    </A>
  );
}

// ---- layout helpers ---------------------------------------------------------------------------------------
/** landing.at: absolutely placed */
export const At = ({ x, y, z = 1, children }: { x: number; y: number; z?: number } & Kids) =>
  <div style={sx(`position:absolute;left:${x}px;top:${y}px;z-index:${z}`)}>{children}</div>;

/** Python's f"{v:.0f}" */
const f0 = (v: number) => String(pyRound(v));

/** brandkit.scaled: a fixed-size piece shown at scale k inside a w x h box */
export function Scaled({ w, h, k, children }: { w: number; h: number; k: number } & Kids) {
  return (
    <div style={sx(`width:${w}px;height:${h}px;overflow:hidden;position:relative;flex:none`)}>
      <div style={sx(`position:absolute;left:0;top:0;width:${f0(w / k)}px;height:${f0(h / k)}px;transform:scale(${k});transform-origin:0 0`)}>{children}</div>
    </div>
  );
}

/** common.photo / landing.ph: a photograph cropped into a rounded box */
export function Ph({ n, w, h, pos = "center", r = 24, extra = "", alt }: { n: string; w: number | string; h: number; pos?: string; r?: number; extra?: string; alt?: string }) {
  const width = typeof w === "number" ? `${w}px` : w;
  return (
    <div style={sx(`width:${width};height:${h}px;border-radius:${r}px;overflow:hidden;background:#dfe2e7;flex:none;${extra}`)}>
      <Image src={`/assets/photos/${n}`} alt={alt ?? PHOTO_ALT[n] ?? ""} width={typeof w === "number" ? w : 350} height={h} loading="eager" decoding="sync"
        style={sx(`display:block;width:100%;height:100%;object-fit:cover;object-position:${pos}`)} />
    </div>
  );
}

/** pages.on_plate: the dotted plate */
export const OnPlate = ({ w = 620, h = 420, children }: { w?: number; h?: number } & Kids) =>
  <div style={sx(`position:relative;width:${w}px;height:${h}px;border-radius:28px;${DOTS};box-shadow:inset 0 0 0 1px #eceef2;overflow:hidden`)}>{children}</div>;

/** ds.photo_story: a photo with cards on its edge; cards are [x, y, node] */
export function PhotoStory({ n, pos, cards, w = 640, h = 480 }: { n: string; pos: string; cards: [number, number, ReactNode][]; w?: number; h?: number }) {
  return (
    <div style={sx(`position:relative;width:${w}px;height:${h}px;flex:none`)}>
      <div style={sx("position:absolute;right:0;top:0")}><Ph n={n} w={w - 110} h={h} pos={pos} r={24} /></div>
      {cards.map(([x, y, c], i) => <At key={i} x={x} y={y} z={i + 2}>{c}</At>)}
    </div>
  );
}

// ---- product UI, signature B (ui.py) --------------------------------------------------------------------
type StatusKind = "ok" | "warn" | "bad" | "info" | "mute" | "campus";
const STATUS: Record<StatusKind, [string, string]> = { ok: [OK, OKS], warn: [WARN, WARNS], bad: [BAD, BADS], info: [BLUE, "#e8effd"], mute: [INK2, "#eef0f3"], campus: [CAMPUS, "#efeaff"] };

/** ui.status: a round pill with a dot */
export function Status({ t, kind = "ok" }: { t: ReactNode; kind?: StatusKind }) {
  const [c, bg] = STATUS[kind];
  return (
    <span style={sx(`display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 10px 0 8px;border-radius:999px;background:${bg};font:500 12.5px ${SANS};color:${c};white-space:nowrap`)}>
      <i style={sx(`width:6px;height:6px;border-radius:3px;background:${c}`)} />{t}
    </span>
  );
}

/** ui.card */
export function Card({ w, pad = 16, extra = "", children }: { w?: number; pad?: number; extra?: string } & Kids) {
  return (
    <div style={sx(`${w ? `width:${w}px;` : ""}box-sizing:border-box;background:#fff;border-radius:16px;box-shadow:0 1px 2px rgba(11,12,20,.06),0 16px 36px -18px rgba(11,12,20,.30);padding:${pad}px;font-family:${SANS};color:${INK};${extra}`)}>
      {children}
    </div>
  );
}

/** ui.lab */
export const Lab = ({ t, c }: { t: ReactNode; c?: string }) => <span style={sx(`font:500 13px ${SANS};color:${c ?? MUTED}`)}>{t}</span>;

/** ui.fig: a figure, tabular */
export const Fig = ({ v, s = 28, c = INK }: { v: ReactNode; s?: number; c?: string }) =>
  <span style={sx(`font:600 ${pyRound(s * 1.2)}px/1 ${SANS};color:${c};letter-spacing:-0.02em;${NUM}`)}>{v}</span>;

/** ui.chead: the card's header: a tile with its glyph, the title, the meta on the right */
export function Chead({ icon, title, meta = "", hue = CAMPUS }: { icon: string; title: ReactNode; meta?: ReactNode; hue?: string }) {
  return (
    <div style={sx("display:flex;align-items:center;gap:8px;margin-bottom:10px;white-space:nowrap")}>
      <span style={sx(`width:22px;height:22px;border-radius:6px;background:${hue};display:flex;align-items:center;justify-content:center`)}><Ic n={icon} s={13} c="#fff" /></span>
      <span style={sx(`font:600 13.5px ${SANS};color:${INK};overflow:hidden;text-overflow:ellipsis`)}>{title}</span>
      <span style={sx("flex:1")} /><Lab t={meta} />
    </div>
  );
}

/** ui.rowl: a label and its figure */
export function Rowl({ a, b, c = INK, bold = false, top = true }: { a: ReactNode; b: ReactNode; c?: string; bold?: boolean; top?: boolean }) {
  return (
    <div style={sx(`display:flex;justify-content:space-between;align-items:center;gap:12px;padding:8px 0;${top ? "border-top:1px solid #e3e6eb;" : ""}font-size:13px;color:${c}`)}>
      <span>{a}</span><span style={sx(`font-weight:${bold ? 600 : 500};${NUM}`)}>{b}</span>
    </div>
  );
}

// ---- actions (ds.py) ----------------------------------------------------------------------------------------
type BtnKind = "primary" | "secondary" | "dark" | "tint" | "link";
const SIZES = { sm: [36, 14, 14], md: [44, 15, 16], lg: [52, 16, 18] } as const;
const KINDS = { primary: [BLUE, "#fff", "none"], secondary: ["#fff", INK, `inset 0 0 0 1px ${LINE}`], dark: [INK, "#fff", "none"], tint: ["#e8effd", BLUE, "none"] } as const;

export function btnStyle(kind: Exclude<BtnKind, "link">, size: keyof typeof SIZES) {
  const [h, fs] = SIZES[size];
  const [bg, fg, bd] = KINDS[kind];
  const sh = bd !== "none" ? bd : "0 0 0 0 transparent";
  return `display:inline-flex;align-items:center;gap:8px;height:${h}px;padding:0 ${pyRound(h * 0.38)}px 0 ${pyRound(h * 0.46)}px;border-radius:${Math.floor(h / 2)}px;background:${bg};color:${fg};box-shadow:${sh};font:500 ${fs}px/1 ${SANS};white-space:nowrap`;
}

/**
 * ds.cbtn: a pill with its icon after the label. With href it is a link, with type a form button; the box is the same.
 * `style` lets a caller widen it the way the design does (display:flex;flex:1;justify-content:center).
 */
export function Cbtn({ label, icon = "right-line", kind = "primary", size = "md", href, type, full = false }:
  { label: ReactNode; icon?: string | null; kind?: BtnKind; size?: keyof typeof SIZES; href?: string; type?: "submit" | "button"; full?: boolean }) {
  const [, fs, ics] = SIZES[size];
  if (kind === "link") {
    return (
      <A href={href} style={`display:inline-flex;align-items:center;gap:6px;font:500 ${fs}px ${SANS};color:${INK};text-decoration:underline;text-underline-offset:4px;`}>
        {label}<Ic n="right-line" s={ics - 2} c={INK} />
      </A>
    );
  }
  let style = btnStyle(kind, size);
  if (full) style = style.replace("display:inline-flex", "display:flex;flex:1;justify-content:center");
  const fg = KINDS[kind][1];
  const inner = <>{label}{icon ? <Ic n={icon} s={ics} c={fg} /> : null}</>;
  if (type) return <button type={type} style={sx(style)}>{inner}</button>;
  return <A href={href} style={style}>{inner}</A>;
}

export const PORTAL_NAMES = ["Administration", "Teacher", "Parent", "Student"] as const;

/** ds.portal_tag: where something comes from; a portal's tag carries its icon */
export function PortalTag({ t }: { t: string }) {
  const name = PORTAL_NAMES.find((n) => t.startsWith(n + " portal"));
  return (
    <span style={sx(`display:inline-flex;align-items:center;gap:4px;height:26px;padding:${name ? "0 10px 0 4px" : "0 10px"};border-radius:13px;background:#efeaff;font:500 13px ${SANS};color:${CAMPUS};white-space:nowrap`)}>
      {name ? <PortalIcon n={name} s={20} tile={false} /> : null}{t}
    </span>
  );
}

/** hero.tagged: a product card with the portal it comes from on a tag above it */
export const Tagged = ({ tag, children }: { tag: string } & Kids) =>
  <div style={sx("display:flex;flex-direction:column;align-items:flex-start;gap:8px")}><PortalTag t={tag} />{children}</div>;

/** ds.filter_pill */
export const FilterPill = ({ t, on = false }: { t: string; on?: boolean }) =>
  <span style={sx(`display:inline-flex;align-items:center;gap:7px;height:40px;padding:0 16px;border-radius:20px;${on ? `background:${INK};color:#fff` : `background:#fff;color:${INK2};box-shadow:0 0 0 1px ${LINE}`};font:500 14.5px ${SANS};white-space:nowrap`)}>{t}</span>;

/** ds.segmented */
export function Segmented({ opts, on = 0 }: { opts: string[]; on?: number }) {
  return (
    <div style={sx("display:inline-flex;padding:4px;border-radius:24px;background:#eef0f3")}>
      {opts.map((o, i) => <span key={i} style={sx(`height:36px;padding:0 16px;border-radius:18px;display:flex;align-items:center;font:500 14px ${SANS};${i === on ? `background:#fff;color:${INK};box-shadow:0 1px 2px rgba(11,12,20,.12)` : `color:${MUTED}`}`)}>{o}</span>)}
    </div>
  );
}

/** ds.check: a checkbox or radio as drawn */
export function Check({ label, on = true, radio = false }: { label: ReactNode; on?: boolean; radio?: boolean }) {
  const r = radio ? 10 : 6;
  const inner = on ? (radio ? <span style={sx("width:8px;height:8px;border-radius:4px;background:#fff")} /> : <Ic n="check-line" s={14} c="#fff" />) : null;
  return (
    <span style={sx(`display:inline-flex;align-items:center;gap:10px;font:400 15px ${SANS};color:${INK}`)}>
      <span style={sx(`width:20px;height:20px;border-radius:${r}px;display:flex;align-items:center;justify-content:center;${on ? `background:${BLUE}` : "background:#fff;box-shadow:inset 0 0 0 1.5px #c3c8d1"}`)}>{inner}</span>{label}
    </span>
  );
}

/** ds.field: label above a 48px box, help below */
export function Field({ label, value = "", ph = "", help = "", w = 360, kind = "text", tail }: { label: ReactNode; value?: ReactNode; ph?: string; help?: string; w?: number | string; kind?: "text" | "select" | "area"; tail?: ReactNode }) {
  const width = typeof w === "number" ? `${w}px` : w;
  const hh = kind === "area" ? 104 : 48;
  return (
    <div style={sx(`width:${width}`)}>
      <div style={sx(`font:500 14px ${SANS};color:${INK};margin-bottom:8px`)}>{label}</div>
      <div style={sx(`height:${hh}px;border-radius:12px;background:#fff;box-shadow:inset 0 0 0 1px ${LINE};display:flex;align-items:${kind === "area" ? "flex-start" : "center"};justify-content:space-between;padding:${kind === "area" ? "14px" : "0"} 16px;box-sizing:border-box;font:400 16px ${SANS}`)}>
        {value ? <span style={sx(`color:${INK}`)}>{value}</span> : <span style={sx(`color:${FAINT}`)}>{ph}</span>}
        {kind === "select" ? <Ic n="down-line" s={16} c={MUTED} /> : null}{tail}
      </div>
      {help ? <div style={sx(`font:400 13.5px ${SANS};color:${MUTED};margin-top:8px`)}>{help}</div> : null}
    </div>
  );
}

export { sx, cx };

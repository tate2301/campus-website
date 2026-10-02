/**
 * The site's type rules, in one place. sx() (src/lib/sx.ts) applies them to every style set in the site's sans
 * (var(--font-sans), General Sans): it snaps the size to the scale, sets the leading for that size and tracks the
 * letters for that size. Phone mock-ups (Inter), figures (Inter, tabular), the mono and the report serif are not
 * touched. The reasoning and the sources are in docs/typography.md.
 */

/**
 * The sizes text may be set in, px. 1px steps for interface text (labels and cards: emphasis in small steps), then
 * the classical series for reading and display (12 14 16 18 24 36 48 … with 20, 22, 28, 32, 40, 56, 64 between).
 * Body copy is 17–18 (never under 15); each heading level is a clear step up from the one below.
 */
export const SCALE = [12, 13, 14, 15, 16, 17, 18, 20, 22, 24, 28, 32, 36, 40, 48, 56, 64] as const;

/** the scale step a drawn size moves to: the nearest step, except that ties and the drawn 30 and 44 go down */
export function snap(px: number): number {
  if (px === 30) return 28; // phone section heads: a clear step below the 36 page title
  if (px === 44) return 40; // desktop row and card heads: a clear step below the 48 section heads
  let best: number = SCALE[0];
  for (const s of SCALE) if (Math.abs(s - px) < Math.abs(best - px)) best = s;
  return best;
}

/**
 * Leading (line-height, unitless) for a size, for text that runs to more than one line. Display type is set tight
 * (the lines are short and the ascenders don't collide); reading text gets 1.5, interface text a little less.
 */
export function lead(px: number): number {
  if (px >= 48) return 1.08;
  if (px >= 32) return 1.1;
  if (px >= 24) return 1.15;
  if (px >= 20) return 1.3;
  if (px >= 16) return 1.5;
  if (px >= 14) return 1.45;
  return 1.4;
}

/**
 * Tracking (letter-spacing) for a size, for lowercase text. Large type is tightened a little as it grows, text sizes
 * are left as drawn by the font, and the smallest sizes are opened a touch. Capitals would get +0.05 to 0.1em, but the
 * site sets nothing in capitals.
 */
export function track(px: number): string {
  if (px >= 48) return "-0.025em";
  if (px >= 32) return "-0.02em";
  if (px >= 24) return "-0.015em";
  if (px >= 18) return "-0.005em";
  if (px >= 14) return "0em";
  return "0.01em";
}

const SANS_FONT = /^(\d{3}) ([\d.]+)px(?:\/([\d.]+)(px)?)? (var\(--font-sans\).*)$/;

/**
 * Typesets a parsed style (property names in camelCase) in place, when its font shorthand is the site's sans.
 * Single-line settings (a line-height of 1, or none) keep their leading; multi-line ones get lead(size).
 */
export function typeset(style: Record<string, string>): void {
  const m = style.font?.match(SANS_FONT);
  if (!m) return;
  const [, w, size, lh, unit, family] = m;
  const px = snap(Number(size));
  let line = "";
  if (lh !== undefined) {
    const ratio = unit ? Number(lh) / Number(size) : Number(lh);
    line = ratio <= 1.05 ? `/${lh}${unit ?? ""}` : `/${lead(px)}`;
  }
  style.font = `${w} ${px}px${line} ${family}`;
  style.letterSpacing = track(px);
}

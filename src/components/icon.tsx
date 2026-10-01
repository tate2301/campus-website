import "server-only";
import icons from "@iconify-json/mingcute/icons.json";
import { htmlToReact } from "@/lib/html-to-react";

/**
 * A MingCute glyph, as the design kit's ic(name, size, colour) draws it: "-line" names as they are, every other name
 * in its "-fill" form, in a 24-unit box, the colour written into the paths.
 */
const ICONS = (icons as { icons: Record<string, { body: string }> }).icons;

export function Ic({ n, s, c }: { n: string; s: number; c: string }) {
  const name = n.endsWith("-line") ? n : `${n}-fill`;
  const icon = ICONS[name];
  if (!icon) throw new Error(`No MingCute icon "${name}"`);
  return htmlToReact(
    `<svg style="flex:none;display:block" width="${s.toFixed(1)}" height="${s}" viewBox="0 0 24 24" aria-hidden="true">${icon.body.replaceAll("currentColor", c)}</svg>`,
  );
}

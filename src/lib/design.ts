/**
 * The values the design is built from (design/source/common.py, ds.py, brandkit.py), under the names the source
 * uses, so a component can be read side by side with the function it ports. Colours match spec/tokens.css; they are
 * kept as literals here because they also name the drawings in the art registry (e.g. "ic:check-circle:15:#12805c").
 */
export const INK = "#0b0c14", INK2 = "#3b3d47", MUTED = "#6b6d78", FAINT = "#9a9ea9", LINE = "#e7e9ef";
export const BLUE = "#2563eb", MARK = "#0F62FE", CAMPUS = "#7c5cff";
export const PLATE = "#f4f5f7", TRAY = "#eceef2", WHITE = "#ffffff", GROUND = "#f7f8fa";
export const OK = "#12805c", OKS = "#e5f4ec", WARN = "#a15c07", WARNS = "#fdf1dc", BAD = "#be123c", BADS = "#fde7ec";

export const SANS = "var(--font-sans)", SERIF = "var(--font-serif)", MONO = "var(--font-mono)", UI = "var(--font-ui)";
/** figures that line up or change: Inter's tabular figures, because General Sans has proportional figures only */
export const NUM = "font-family:var(--font-ui);font-variant-numeric:tabular-nums;";
export const DOTS = `background:${GROUND} radial-gradient(#dfe2e8 1px,transparent 1.2px) 0 0/22px 22px`;
export const SH_CARD = "0 1px 2px rgba(11,12,20,.06), 0 16px 36px -18px rgba(11,12,20,.30)";

/** desktop: 1440 page, 120 gutter, 160 between sections */
export const X = 120, GAP = 160, W = 1440;
/** phone: 390 page, 20 gutter, 350 column, 96 between sections */
export const MW = 390, MX = 20, CW = 350, MGAP = 96;

/** Python's round(): halves go to the even neighbour */
export function pyRound(x: number): number {
  const r = Math.round(x);
  return Math.abs(x % 1) === 0.5 && r % 2 !== 0 ? r - 1 : r;
}

/** Python's f"{x:.0f}" and friends for the few values the source formats */
export const fmt = (x: number, d = 0) => x.toFixed(d);

/**
 * Desktop gutters, fluid above the design width: 120px at 1440, and the 1200px column centred on wider screens.
 * (Between 1024 and 1439 the desktop layout is zoomed as a whole; see src/app/layout.tsx.)
 */
export const PX = "max(120px, calc(50% - 600px))";
/** the 80px gutter of the call-to-action block and the Who we serve focus plate, which are 1280 wide */
export const PX80 = "max(80px, calc(50% - 640px))";

/** Python's f"{x:.Nf}": like toFixed, but an exact half goes to the even neighbour (6.25 -> "6.2") */
export function pyFixed(x: number, d: number): string {
  const m = 10 ** d, v = x * m;
  const r = Math.abs(v - Math.trunc(v)) === 0.5 ? pyRound(v) : Math.round(v);
  return (r / m).toFixed(d);
}

import { ImageResponse } from "next/og";
import { readFileSync } from "node:fs";
import { join } from "node:path";
import { lead, track } from "@/lib/type";

/**
 * The image a link to the site shows when shared (Open Graph and X), 1200 × 630. It is not drawn in the design, so it
 * is made of the design's own parts, set in General Sans by the rules in src/lib/type.ts: the nav lockup (mark tile, "campus", "by Corelith"), a blue eyebrow and the
 * page's headline as written in content/copy.json, on the page ground, with the address underneath.
 */
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

const dir = join(process.cwd(), "src/og");
// General Sans, as fetched by scripts/fonts.mjs (Satori reads the TTF files, not WOFF2)
const font = (w: 400 | 500 | 600) => ({ name: "General Sans", data: readFileSync(join(process.cwd(), `src/fonts/general-sans/GeneralSans-${w}.ttf`)), weight: w, style: "normal" as const });
const fonts = [font(400), font(500), font(600)];
const mark = `data:image/svg+xml;base64,${readFileSync(join(dir, "mark.svg")).toString("base64")}`;

// spec/tokens.css
const INK = "#0b0c14", MUTED = "#6b6d78", LINE = "#e7e9ef", BLUE = "#2563eb", GROUND = "#f7f8fa";

export function ogImage({ eyebrow, h }: { eyebrow: string; h: string }) {
  return new ImageResponse(
    (
      <div style={{ width: "100%", height: "100%", display: "flex", flexDirection: "column", justifyContent: "space-between", padding: "72px 88px", fontFamily: "General Sans", color: INK, backgroundColor: GROUND }}>
        <div style={{ display: "flex", alignItems: "center", gap: 18 }}>
          {/* eslint-disable-next-line @next/next/no-img-element */}
          <img src={mark} width={56} height={56} alt="" />
          <span style={{ fontSize: 52, fontWeight: 600, letterSpacing: track(52), lineHeight: 1 }}>campus</span>
          <span style={{ fontSize: 28, color: MUTED, paddingLeft: 18, marginLeft: 2, borderLeft: `2px solid ${LINE}` }}>by Corelith</span>
        </div>
        <div style={{ display: "flex", flexDirection: "column", gap: 24, maxWidth: 960 }}>
          <span style={{ fontSize: 30, fontWeight: 500, color: BLUE }}>{eyebrow}</span>
          <span style={{ fontSize: h.length > 48 ? 64 : 72, fontWeight: 600, lineHeight: lead(64), letterSpacing: track(64), textWrap: "balance" }}>{h}</span>
        </div>
        <span style={{ fontSize: 26, color: MUTED }}>campus.corelith.co.zw</span>
      </div>
    ),
    { ...size, fonts },
  );
}

import localFont from "next/font/local";
import { Inter, IBM_Plex_Mono, Newsreader } from "next/font/google";

/**
 * General Sans (Indian Type Foundry, Fontshare, ITF Free Font License) for everything on the site: one family, three
 * weights a step apart (regular 400 for text, medium 500 for labels and buttons, semibold 600 for headings). The files
 * are fetched by scripts/fonts.mjs before every build; they are not in the repository (see that script for why).
 *
 * The overrides centre the cap height in the line box. As drawn, General Sans has 292 units above its capitals and
 * 240 below the baseline (per 1000), so a label in a button or pill sits low. Ascent = cap height + descender
 * (718 + 240) and no line gap puts 240 units on both sides, and line-height:normal becomes 1.2.
 */
export const generalSans = localFont({
  src: [
    { path: "../fonts/general-sans/GeneralSans-400.woff2", weight: "400", style: "normal" },
    { path: "../fonts/general-sans/GeneralSans-500.woff2", weight: "500", style: "normal" },
    { path: "../fonts/general-sans/GeneralSans-600.woff2", weight: "600", style: "normal" },
  ],
  variable: "--font-general-sans",
  display: "swap",
  adjustFontFallback: "Arial",
  declarations: [
    { prop: "ascent-override", value: "95.8%" },
    { prop: "descent-override", value: "24%" },
    { prop: "line-gap-override", value: "0%" },
  ],
});

/**
 * Inter: inside the phone mock-ups (the Campus app's own type), and for figures that must line up or that change,
 * because General Sans has only proportional figures (no tnum feature). See NUM in src/lib/design.ts.
 */
export const inter = Inter({ weight: ["400", "500", "600"], subsets: ["latin"], variable: "--font-inter" });
export const plexMono = IBM_Plex_Mono({ weight: ["400", "500"], subsets: ["latin"], variable: "--font-plex-mono" });
export const newsreader = Newsreader({ weight: ["400", "500"], subsets: ["latin"], variable: "--font-newsreader" });

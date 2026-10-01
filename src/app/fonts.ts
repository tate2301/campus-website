import { Atkinson_Hyperlegible_Next, Inter, IBM_Plex_Mono, Newsreader } from "next/font/google";

// The same families, weights and axes as the Google Fonts request in design/html/*.html.
export const atkinson = Atkinson_Hyperlegible_Next({ weight: ["400", "500", "600"], subsets: ["latin", "latin-ext"], variable: "--font-atkinson" });
export const inter = Inter({ weight: ["400", "500", "600"], subsets: ["latin"], variable: "--font-inter" });
export const plexMono = IBM_Plex_Mono({ weight: ["400", "500"], subsets: ["latin"], variable: "--font-plex-mono" });
export const newsreader = Newsreader({ subsets: ["latin"], axes: ["opsz"], variable: "--font-newsreader" });

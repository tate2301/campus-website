import type { Metadata } from "next";
import "./globals.css";
// the two animations, as the design exports them
import "../../design/components/mark-journey.css";
import "../../design/components/hover-reveal.css";
import { atkinson, inter, plexMono, newsreader } from "./fonts";

export const metadata: Metadata = {
  metadataBase: new URL("https://campus.corelith.co.zw"),
  title: { default: "Corelith Campus", template: "%s · Corelith Campus" },
  // the shared images are app/**/opengraph-image.tsx (src/og/card.tsx); the icons come from scripts/icons.mjs
  openGraph: { siteName: "Corelith Campus", locale: "en_GB", type: "website" },
  twitter: { card: "summary_large_image" },
};

const ZOOM = `(function(){var d=document.documentElement;function z(){var w=d.clientWidth||innerWidth;d.style.setProperty("--dz",w>=1024&&w<1440?String(w/1440):"1")}z();addEventListener("resize",z)})()`;

/**
 * The phone's sideways strips (.hscroll in globals.css) scroll once this marks the page: at once on a touch screen,
 * otherwise at the first wheel, click, touch or key. Until then they sit as drawn. (Any scrollable strip on the page
 * shifts how Chromium rasterises the page's text in a full-page screenshot, enough to fail the visual test, which runs
 * as a mouse browser that never interacts.)
 */
const HSCROLL = `(function(){var d=document.documentElement;function on(){d.dataset.hscroll="on";["pointerdown","wheel","touchstart","keydown"].forEach(function(t){removeEventListener(t,on,true)})}if(matchMedia("(any-pointer: coarse)").matches)on();else["pointerdown","wheel","touchstart","keydown"].forEach(function(t){addEventListener(t,on,{capture:true,passive:true})})})()`;

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en-GB" suppressHydrationWarning className={`${atkinson.variable} ${inter.variable} ${plexMono.variable} ${newsreader.variable}`}>
      <head>
        {/* From 1024 to 1439px the desktop layout is shown whole, scaled to the window: the gutter goes from 120px to
            85px at 1024 (8.3vw, as the brief asks) and the drawn pictures keep their proportions. */}
        <script dangerouslySetInnerHTML={{ __html: ZOOM }} />
        <script dangerouslySetInnerHTML={{ __html: HSCROLL }} />
      </head>
      <body>{children}</body>
    </html>
  );
}

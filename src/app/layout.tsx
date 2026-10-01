import type { Metadata } from "next";
import "./globals.css";
// the two animations, as the design exports them
import "../../design/components/mark-journey.css";
import "../../design/components/hover-reveal.css";
import { atkinson, inter, plexMono, newsreader } from "./fonts";

export const metadata: Metadata = {
  metadataBase: new URL("https://campus.corelith.co.zw"),
  title: { default: "Corelith Campus", template: "%s · Corelith Campus" },
};

const ZOOM = `(function(){var d=document.documentElement;function z(){var w=d.clientWidth||innerWidth;d.style.setProperty("--dz",w>=1024&&w<1440?String(w/1440):"1")}z();addEventListener("resize",z)})()`;

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en-GB" suppressHydrationWarning className={`${atkinson.variable} ${inter.variable} ${plexMono.variable} ${newsreader.variable}`}>
      <head>
        {/* From 1024 to 1439px the desktop layout is shown whole, scaled to the window: the gutter goes from 120px to
            85px at 1024 (8.3vw, as the brief asks) and the drawn pictures keep their proportions. */}
        <script dangerouslySetInnerHTML={{ __html: ZOOM }} />
      </head>
      <body>{children}</body>
    </html>
  );
}

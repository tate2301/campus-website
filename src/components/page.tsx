import type { ReactNode } from "react";
import { sx } from "@/lib/sx";
import { INK, SANS } from "@/lib/design";
import { Tree } from "./photo";

/**
 * A route renders both layouts the design draws: the desktop page (1440) and the phone page (390).
 * CSS shows one of them (globals.css: phone up to 1023px, desktop from 1024px); the other is display:none, so it is
 * out of the accessibility tree, and its photographs are not fetched (photo.tsx).
 */
export function SitePage({ desktop, phone, desktopStyle = "", phoneStyle = "" }: { desktop: ReactNode; phone?: ReactNode; desktopStyle?: string; phoneStyle?: string }) {
  return (
    <>
      <div className="layout-desktop" data-tree="desktop">
        <div style={sx(`width:100%;background:#fff;font-family:${SANS};color:${INK};${desktopStyle}`)}><Tree name="desktop">{desktop}</Tree></div>
      </div>
      {phone ? (
        <div className="layout-phone" data-tree="phone">
          <div style={sx(`width:100%;max-width:560px;margin:0 auto;background:#fff;font-family:${SANS};color:${INK};overflow:hidden;${phoneStyle}`)}><Tree name="phone">{phone}</Tree></div>
        </div>
      ) : null}
    </>
  );
}

/** the design's gap(h) spacer */
export const Gap = ({ h }: { h: number }) => <div style={sx(`height:${h}px`)} />;

/**
 * Site chrome: the nav and the footer, desktop (ds.nav_bar, pages.site_footer, landing.footer) and phone
 * (mobile.nav, mobile.footer, the open menu from ds.mobile_nav).
 */
import { A, Cbtn, CorelithLogo, Eyebrow, Ic, MenuIcon, NavIcon, Ph, Pmark, btnStyle, sx } from "./ds";
import { MobileMenu } from "./mobile-menu";
import { CP } from "@/content/copy";
import { ACTION_HREF, FOOT_HREF, NAV_HREF, typeHref } from "@/content/links";
import { FAINT, INK, INK2, LINE, MUTED, MX, PLATE, PX, SANS, pyRound } from "@/lib/design";

/** common.lockup: the Campus mark tile, the name in lower case and, in the nav only, "by Corelith" */
export function Lockup({ h = 24, ink = INK, by = true, href }: { h?: number; ink?: string; by?: boolean; href?: string }) {
  return (
    <A href={href} label={href ? "Corelith Campus, home" : undefined} style="display:inline-flex;align-items:center;gap:12px">
      <span style={sx(`display:inline-flex;align-items:center;gap:${pyRound(h * 0.36)}px`)}>
        <Pmark s={h} r={pyRound(h * 0.28)} />
        <span style={sx(`font:600 ${pyRound(h * 0.92)}px/1 ${SANS};letter-spacing:-0.03em;color:${ink}`)}>campus</span>
      </span>
      {by ? <span style={sx(`font:400 ${Math.max(11, pyRound(h * 0.5))}px ${SANS};color:${MUTED};padding-left:12px;border-left:1px solid ${LINE}`)}>by Corelith</span> : null}
    </A>
  );
}

const MENUS = ["Solutions", "Who we serve", "Platform"];

/** ds.nav_bar: four items and one button; the section you are in is shown open */
export function NavBar({ open }: { open?: string | null }) {
  return (
    <header style={sx(`width:100%;height:76px;display:flex;align-items:center;gap:28px;padding:0 ${PX};box-sizing:border-box;border-bottom:1px solid ${LINE};background:#fff`)}>
      <Lockup h={24} href="/" />
      <nav aria-label="Main" style={sx("display:flex;gap:6px;margin-left:12px")}>
        {(CP.NAV as string[]).map((t) => {
          const on = t === open;
          return (
            <A key={t} href={NAV_HREF[t]} style={`display:inline-flex;align-items:center;gap:4px;height:36px;padding:0 12px;border-radius:18px;${on ? `background:${PLATE};` : ""}font:500 15px ${SANS};color:${on ? INK : INK2}`}>
              {t}{MENUS.includes(t) ? <Ic n={on ? "up-line" : "down-line"} s={14} c={FAINT} /> : null}
            </A>
          );
        })}
      </nav>
      <span style={sx("flex:1")} />
      <A href="/sign-in" style={`font:500 15px ${SANS};color:${INK2}`}>Sign in</A>
      <Cbtn label="Book a demo" icon="calendar" size="sm" href="/demo" />
    </header>
  );
}

export const TYPE_PHOTO: Record<string, [string, string]> = {
  "t-day": ["girls-classroom.jpg", "center 35%"], "t-boarding": ["boys-reading.jpg", "center 40%"], "t-government": ["classroom-uniforms.jpg", "center"],
  "t-private": ["seniors-lecture.jpg", "center 30%"], "t-mission": ["teacher-garden.jpg", "center 30%"],
};

/** landing.footer columns */
function FootCols({ gap }: { gap: number }) {
  return <>{(CP.FOOT as [string, string[]][]).map(([h, xs]) => (
    <div key={h} style={sx(`display:flex;flex-direction:column;gap:${gap}px`)}>
      <span style={sx(`font:600 14px ${SANS};${gap === 12 ? `color:${INK}` : ""}`)}>{h}</span>
      {xs.map((x) => <A key={x} href={FOOT_HREF[x]} style={`font:400 14px ${SANS};color:${MUTED}`}>{x}</A>)}
    </div>
  ))}</>;
}

/** pages.site_footer: Who we serve, the five kinds of K-12 school, above the link columns */
export function SiteFooter() {
  return (
    <>
      <div style={sx(`padding:72px ${PX} 64px;border-top:1px solid ${LINE}`)}>
        <div style={sx("display:flex;align-items:baseline;justify-content:space-between;margin-bottom:28px")}>
          <Eyebrow t="Who we serve · K-12" k="who" />
        </div>
        <div style={sx("display:flex;justify-content:space-between;align-items:stretch")}>
          {(CP.SCHOOL_TYPES as [string, string, string][]).map(([n, k]) => (
            <A key={k} href={typeHref(k)} style="width:232px;display:flex;flex-direction:column">
              <div style={sx("position:relative;width:232px;height:150px")}>
                <Ph n={TYPE_PHOTO[k][0]} w={232} h={150} pos={TYPE_PHOTO[k][1]} r={16} />
                <div style={sx("position:absolute;left:10px;bottom:10px;border-radius:10px;box-shadow:0 8px 18px -10px rgba(11,12,20,.5)")}><NavIcon k={k} s={36} /></div>
              </div>
              <div style={sx(`font:600 16px ${SANS};margin-top:12px`)}>{n}</div>
            </A>
          ))}
        </div>
      </div>
      <footer style={sx(`padding:56px ${PX} 48px;border-top:1px solid ${LINE};background:#fff`)}>
        <div style={sx("display:flex;justify-content:space-between;gap:60px")}>
          <div style={sx("display:flex;flex-direction:column;gap:18px;max-width:320px")}>
            <Lockup h={24} by={false} href="/" />
            <span style={sx(`font:400 14px/1.6 ${SANS};color:${MUTED}`)}>{CP.FOOT_LINE}</span>
            <span style={sx("margin-top:6px")}><CorelithLogo s={20} c={INK} /></span>
          </div>
          <div style={sx("display:grid;grid-template-columns:repeat(4,150px);gap:36px")}><FootCols gap={12} /></div>
        </div>
        <div style={sx(`display:flex;justify-content:space-between;margin-top:56px;padding-top:22px;border-top:1px solid ${LINE};font:400 13px ${SANS};color:${MUTED}`)}>
          <span>© 2026 Corelith Labs</span><span>Harare, Zimbabwe</span>
        </div>
      </footer>
    </>
  );
}

// ---- phone -------------------------------------------------------------------------------------------------
/** ds.mobile_nav, open: the sections, then Book a demo and Sign in */
function PhoneMenuSheet() {
  return (
    <div style={sx("padding:12px 20px")}>
      {(CP.NAV as string[]).map((t) => (
        <A key={t} href={NAV_HREF[t]} style={`display:flex;align-items:center;justify-content:space-between;height:56px;border-bottom:1px solid ${LINE};font:500 18px ${SANS}`}>
          {t}<Ic n={MENUS.includes(t) ? "down-line" : "right-line"} s={16} c={MUTED} />
        </A>
      ))}
      <div style={sx("display:flex;flex-direction:column;gap:12px;margin-top:28px")}>
        <div style={sx("display:flex")}><Cbtn label="Book a demo" icon="calendar" size="lg" href="/demo" /></div>
        <div style={sx("display:flex")}><Cbtn label="Sign in" icon="user-3" kind="secondary" size="lg" href="/sign-in" /></div>
      </div>
    </div>
  );
}

/** mobile.nav */
export function PhoneNav() {
  return (
    <header style={sx(`height:64px;display:flex;align-items:center;justify-content:space-between;padding:0 ${MX}px;border-bottom:1px solid ${LINE};background:#fff`)}>
      <Lockup h={20} by={false} href="/" />
      <span style={sx("display:flex;gap:10px;align-items:center")}>
        <Cbtn label="Demo" icon="calendar" size="sm" href={ACTION_HREF.Demo} />
        <MobileMenu buttonStyle={sx(`width:40px;height:40px;border-radius:20px;box-shadow:inset 0 0 0 1px ${LINE};display:flex;align-items:center;justify-content:center`)}
          closedIcon={<MenuIcon s={20} />} openIcon={<MenuIcon s={20} open />} sheet={<PhoneMenuSheet />} />
      </span>
    </header>
  );
}

/** mobile.footer */
export function PhoneFooter() {
  return (
    <>
      <div style={sx(`padding:48px 0 40px ${MX}px;border-top:1px solid ${LINE}`)}>
        <PhoneEyebrow t="Who we serve · K-12" k="who" />
        <div style={sx("display:flex;gap:12px;margin-top:20px;overflow:hidden")}>
          {(CP.SCHOOL_TYPES as [string, string, string][]).map(([n, k]) => (
            <A key={k} href={typeHref(k)} style="flex:none;width:150px">
              <div style={sx("position:relative;width:150px;height:110px")}>
                <Ph n={TYPE_PHOTO[k][0]} w={150} h={110} pos={TYPE_PHOTO[k][1]} r={14} />
                <div style={sx("position:absolute;left:8px;bottom:8px;border-radius:9px;box-shadow:0 6px 14px -8px rgba(11,12,20,.5)")}><NavIcon k={k} s={30} /></div>
              </div>
              <div style={sx(`font:600 14.5px ${SANS};margin-top:10px`)}>{n}</div>
            </A>
          ))}
        </div>
      </div>
      <footer style={sx(`padding:40px ${MX}px 36px;border-top:1px solid ${LINE}`)}>
        <Lockup h={22} by={false} href="/" />
        <div style={sx(`font:400 14px/1.6 ${SANS};color:${MUTED};margin-top:14px`)}>{CP.FOOT_LINE}</div>
        <div style={sx("display:grid;grid-template-columns:1fr 1fr;gap:32px 20px;margin-top:32px")}><FootCols gap={11} /></div>
        <div style={sx(`display:flex;justify-content:space-between;margin-top:36px;padding-top:18px;border-top:1px solid ${LINE};font:400 13px ${SANS};color:${MUTED}`)}>
          <span>© 2026 Corelith Labs</span><span>Harare, Zimbabwe</span>
        </div>
      </footer>
    </>
  );
}

/** mobile.eyebrow: 14px, the icon at 26 */
export function PhoneEyebrow({ t, k }: { t: React.ReactNode; k?: string | null }) {
  return <div style={sx(`display:flex;align-items:center;gap:8px;font:500 14px ${SANS};color:#2563eb`)}>{k ? <NavIcon k={k} s={26} /> : null}{t}</div>;
}

export { btnStyle };

import type { Metadata } from "next";
import { SitePage, Gap } from "@/components/page";
import { NavBar, PhoneNav, SiteFooter } from "@/components/chrome";
import { CtaSection, DemoBtns, LinkCard, PageHero, PicIntegrations, PicOffline, PicSecurity, ROW_ICON, Rows, SecHead, Wrap } from "@/components/sections";
import { MarkJourney } from "@/components/mark-journey";
import { RegisterCard } from "@/components/cards";
import { MTCard, TCard } from "@/components/pictures";
import { MEnd, MGap, MHead, MHero, MRows, Pad, PhotoCard, PlateCard, ScaleTo } from "@/components/phone";
import { At, CtaScene, OnPlate, Ph, PortalScene, Scaled, Tagged, sx } from "@/components/ds";
import { CP, SW } from "@/content/copy";
import { GAP, INK2, MUTED, PLATE, SANS } from "@/lib/design";

export const metadata: Metadata = { title: "Platform", description: SW.PLATFORM.b };

const ROWS = CP.ROWS as [string, string, string][];
// the two link cards, as written in webpages.platform_secs and mobile.platform
const INTEG: [string, string, string, string] = ["integrations", "Integrations", "Sage Pastel, QuickBooks, ZIMRA fiscalisation and payments.", "See the integrations"];
const MOVING: [string, string, string, string] = ["moving", "Moving to Campus", "From your old system to your first term on Campus, in four weeks.", "How we move your records"];

/** webpages.platform_secs */
function Desktop() {
  const P = SW.PLATFORM;
  const [e, h, b] = ROWS[4];
  const [ae, ah, ab] = P.ai;
  const pic = (
    <div style={sx("position:relative;width:1200px;height:600px")}>
      <div style={sx("position:absolute;left:90px;top:30px")}><Ph n="pupils-writing.jpg" w={1020} h={570} pos="center 40%" r={24} /></div>
      <At x={0} y={90} z={3}><TCard name="register_card" /></At>
      <At x={880} y={0} z={2}><TCard name="fee_card" /></At>
      <At x={840} y={400} z={4}><TCard name="student_card" /></At>
    </div>
  );
  return (
    <>
      <NavBar open="Platform" />
      <PageHero eye={P.eyebrow} k="platform" h={P.h} b={P.b} buttons={<DemoBtns />} pic={pic} />
      <Gap h={GAP} />
      <Wrap><Rows items={[{ eye: ROWS[0][0], k: ROW_ICON[ROWS[0][0]], h: ROWS[0][1], b: ROWS[0][2], pic: <MarkJourney /> }, { eye: ROWS[1][0], k: ROW_ICON[ROWS[1][0]], h: ROWS[1][1], b: ROWS[1][2], pic: <PicOffline /> }]} /></Wrap>
      <Gap h={GAP} />
      <Wrap>
        <SecHead eye="Four portals" k="portals" h={P.portals_h} />
        <div style={sx("display:grid;grid-template-columns:repeat(4,1fr);gap:24px")}>
          {(P.portals as [string, string, string][]).map(([n, who, what]) => (
            <div key={n} style={sx(`position:relative;height:420px;border-radius:24px;background:${PLATE};overflow:hidden;padding:26px 24px 0;box-sizing:border-box`)}>
              <div style={sx(`font:600 24px/1.15 ${SANS};letter-spacing:-0.02em`)}>{n} portal</div>
              <div style={sx(`font:400 14.5px/1.5 ${SANS};color:${INK2};margin-top:8px`)}>{who}</div>
              <div style={sx(`font:400 14.5px/1.5 ${SANS};color:${MUTED};margin-top:4px`)}>{what}</div>
              <div style={sx("position:absolute;left:-20px;bottom:-24px")}><PortalScene n={n} w={320} h={220} U={26} cx={160} cy={135} labels={false} /></div>
            </div>
          ))}
        </div>
      </Wrap>
      <Gap h={GAP} />
      <Wrap><Rows items={[
        { eye: e, k: "security", h, b, pic: <PicSecurity /> },
        { eye: ae, k: "ai", h: ah, b: ab, pic: <OnPlate w={620} h={440}><At x={140} y={40}><TCard name="ai_card" /></At></OnPlate> },
      ]} /></Wrap>
      <Gap h={GAP} />
      <Wrap>
        <SecHead eye="Platform" k="platform" h={P.more_h} />
        <div style={sx("display:flex;gap:24px;align-items:stretch")}>
          <LinkCard k={INTEG[0]} t={INTEG[1]} d={INTEG[2]} act={INTEG[3]}
            art={<div style={sx("display:flex;justify-content:center")}><Scaled w={325} h={220} k={220 / 420}><PicIntegrations w={620} h={420} /></Scaled></div>} />
          <LinkCard k={MOVING[0]} t={MOVING[1]} d={MOVING[2]} act={MOVING[3]} art={<CtaScene k="training" w={588} h={220} U={26} cx={294} cy={150} labels={false} />} />
        </div>
      </Wrap>
      <CtaSection kind="visit" />
      <SiteFooter />
    </>
  );
}

/** mobile.platform */
function Phone() {
  const P = SW.PLATFORM;
  const [e, h, b] = ROWS[4];
  const [ae, ah, ab] = P.ai;
  return (
    <>
      <PhoneNav />
      <MHero eye={P.eyebrow} k="platform" h={P.h} b={P.b} pic={<PhotoCard photo="pupils-writing.jpg" pos="center 40%" card={<MTCard name="student_card" />} />} />
      <MGap />
      <MRows items={[
        { eye: ROWS[0][0], k: ROW_ICON[ROWS[0][0]], h: ROWS[0][1], b: ROWS[0][2], pic: <ScaleTo w={620} h={460}><MarkJourney /></ScaleTo> },
        { eye: ROWS[1][0], k: ROW_ICON[ROWS[1][0]], h: ROWS[1][1], b: ROWS[1][2], pic: <PhotoCard photo="classroom-zambia.jpg" pos="center 40%" card={<Tagged tag="Teacher portal"><RegisterCard w={310} offline /></Tagged>} /> },
      ]} />
      <MGap />
      <Pad>
        <MHead eye="Four portals" k="portals" h={P.portals_h} />
        <div style={sx("display:flex;flex-direction:column;gap:14px")}>
          {(P.portals as [string, string, string][]).map(([n, w, wh]) => (
            <div key={n} style={sx(`position:relative;height:280px;border-radius:22px;background:${PLATE};overflow:hidden;padding:22px 22px 0;box-sizing:border-box`)}>
              <div style={sx(`font:600 22px ${SANS};letter-spacing:-0.02em`)}>{n} portal</div>
              <div style={sx(`font:400 14.5px/1.5 ${SANS};color:${INK2};margin-top:6px`)}>{w}</div>
              <div style={sx(`font:400 14px/1.5 ${SANS};color:${MUTED};margin-top:2px`)}>{wh}</div>
              <div style={sx("position:absolute;right:-20px;bottom:-30px")}><PortalScene n={n} w={280} h={190} U={24} cx={140} cy={118} labels={false} /></div>
            </div>
          ))}
        </div>
      </Pad>
      <MGap />
      <MRows items={[
        { eye: e, k: "security", h, b, pic: <ScaleTo w={620} h={420}><PicSecurity /></ScaleTo> },
        { eye: ae, k: "ai", h: ah, b: ab, pic: <PlateCard card={<MTCard name="ai_card" w={310} />} /> },
      ]} />
      <MGap />
      <Pad>
        <MHead eye="Platform" k="platform" h={P.more_h} />
        <div style={sx("display:flex;flex-direction:column;gap:14px")}>
          <LinkCard k={INTEG[0]} t={INTEG[1]} d={INTEG[2]} act={INTEG[3]} />
          <LinkCard k={MOVING[0]} t={MOVING[1]} d={MOVING[2]} act={MOVING[3]} />
        </div>
      </Pad>
      <MEnd />
    </>
  );
}

export default function Platform() {
  return <SitePage desktop={<Desktop />} phone={<Phone />} />;
}

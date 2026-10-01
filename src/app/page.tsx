import type { Metadata } from "next";
import { SitePage, Gap } from "@/components/page";
import { NavBar, PhoneNav, SiteFooter } from "@/components/chrome";
import { CtaSection, Departments, Focus, HomeHero, PicIntegrations, PicOffline, PicSecurity, PicTraining, PriceBand, ROW_ICON, Roles, Rows, Band, Switching } from "@/components/sections";
import { MarkJourney } from "@/components/mark-journey";
import { RegisterCard } from "@/components/cards";
import { BtnFull, H2, MEnd, MGap, MHead, MHero, MRoleTile, MRows, MTiles, MovingBand, MPriceBand, P, PEyebrow, Pad, PhotoCard, ScaleTo } from "@/components/phone";
import { Ic, OnPlate, SchoolsCampus, Tagged, sx } from "@/components/ds";
import { CP } from "@/content/copy";
import { GAP, INK2, OK, PLATE, SANS } from "@/lib/design";

export const metadata: Metadata = { title: "Home", description: CP.HERO.body };

/** pages.home */
function Desktop() {
  const pics = [<MarkJourney key="j" />, <PicOffline key="o" />, <PicIntegrations key="i" />, <PicTraining key="t" />, <PicSecurity key="s" />];
  return (
    <>
      <NavBar />
      <HomeHero />
      <Departments />
      <Focus />
      <Band><Rows items={(CP.ROWS as [string, string, string][]).map(([e, h, b], i) => ({ eye: e, k: ROW_ICON[e], h, b, pic: pics[i] }))} /></Band>
      <div style={sx("height:0")} />
      <Roles />
      <Gap h={GAP} />
      <Switching />
      <PriceBand />
      <CtaSection kind="visit" />
      <SiteFooter />
    </>
  );
}

/** mobile.home */
function Phone() {
  const H = CP.HERO;
  const [a] = CP.DEPTS_H;
  const [fh, fb] = CP.FOCUS;
  const register = <Tagged tag="Teacher portal"><RegisterCard w={310} offline /></Tagged>;
  const pics = [
    <ScaleTo key="j" w={620} h={460}><MarkJourney /></ScaleTo>,
    <PhotoCard key="o" photo="classroom-zambia.jpg" pos="center 40%" card={register} />,
    <ScaleTo key="i" w={620} h={420}><PicIntegrations /></ScaleTo>,
    <ScaleTo key="t" w={620} h={420}><PicTraining /></ScaleTo>,
    <ScaleTo key="s" w={620} h={420}><PicSecurity /></ScaleTo>,
  ];
  return (
    <>
      <PhoneNavAndHero />
      <MGap />
      <Pad><MHead eye="Solutions" k="solutions" h={a} /><MTiles slugs={(CP.DEPARTMENTS as string[][]).map((d) => d[1])} /></Pad>
      <MGap />
      <Pad>
        <div style={sx(`border-radius:24px;background:${PLATE};padding:12px 12px 26px`)}>
          <div style={sx("border-radius:18px;overflow:hidden")}><ScaleTo w={600} h={420} tw={326}><OnPlate w={600} h={420}><SchoolsCampus w={600} h={420} /></OnPlate></ScaleTo></div>
          <div style={sx("padding:20px 10px 0;display:flex;flex-direction:column;gap:14px")}>
            <PEyebrow t="Who we serve · K-12" k="who" /><H2 t={fh} size={28} /><P t={fb} size={16} />
            <BtnFull label="Book a demo" /><BtnFull label="See who we serve" icon="arrow-right-line" kind="secondary" />
          </div>
        </div>
      </Pad>
      <MGap />
      <MRows items={(CP.ROWS as [string, string, string][]).map(([e, h, b], i) => ({ eye: e, k: ROW_ICON[e], h, b, pic: pics[i] }))} />
      <MGap />
      <Pad>
        <MHead eye="Who uses Campus" k="portals" h={CP.ROLES_H} />
        <div style={sx("display:flex;flex-direction:column;gap:14px")}>{(CP.ROLES as [string, string, string, string][]).map((r) => <MRoleTile key={r[0]} r={r} />)}</div>
      </Pad>
      <MGap />
      <MovingBand />
      <MGap />
      <MPriceBand />
      <MEnd />
    </>
  );

  function PhoneNavAndHero() {
    return (
      <>
        <PhoneNav />
        <MHero h={H.h1a} b={H.body_phone} pic={<PhotoCard photo="boys-reading-2.jpg" pos="58% 40%" card={register} h={250} />}
          buttons={<>
            <BtnFull label={H.cta} />
            <div style={sx("display:flex;flex-direction:column;gap:6px")}>
              {["Setup and training free", "First month free", "US$1 per active pupil per month"].map((t) => (
                <div key={t} style={sx(`display:flex;align-items:center;gap:8px;font:500 14.5px ${SANS};color:${INK2}`)}><Ic n="check-circle" s={15} c={OK} />{t}</div>
              ))}
            </div>
          </>} />
      </>
    );
  }
}

export default function Home() {
  return <SitePage desktop={<Desktop />} phone={<Phone />} />;
}

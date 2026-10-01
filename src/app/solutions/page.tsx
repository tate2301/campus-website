import type { Metadata } from "next";
import { SitePage, Gap } from "@/components/page";
import { NavBar, PhoneNav, SiteFooter } from "@/components/chrome";
import { CtaSection, DemoBtns, PageHero, PicIntegrations, PicOffline, ROW_ICON, Rows, Switching, Tiles, Wrap } from "@/components/sections";
import { MarkJourney } from "@/components/mark-journey";
import { RegisterCard } from "@/components/cards";
import { MEnd, MGap, MHero, MRows, MTiles, MovingBand, Pad, PhotoCard, ScaleTo } from "@/components/phone";
import { Tagged } from "@/components/ds";
import { CP, SW } from "@/content/copy";
import { GAP } from "@/lib/design";

export const metadata: Metadata = { title: "Solutions", description: SW.SOLUTIONS.b };

const ALL = (CP.DEPARTMENTS as string[][]).map((d) => d[1]);
const ROWS = (CP.ROWS as [string, string, string][]).slice(0, 3);

/** webpages.solutions_secs */
function Desktop() {
  const S = SW.SOLUTIONS;
  const pics = [<MarkJourney key="j" />, <PicOffline key="o" />, <PicIntegrations key="i" />];
  return (
    <>
      <NavBar open="Solutions" />
      <PageHero eye={S.eyebrow} k="solutions" h={S.h} b={S.b} buttons={<DemoBtns />} />
      <Wrap><Tiles slugs={ALL} /></Wrap>
      <Gap h={GAP} />
      <Wrap><Rows items={ROWS.map(([e, h, b], i) => ({ eye: e, k: ROW_ICON[e], h, b, pic: pics[i] }))} /></Wrap>
      <Gap h={GAP} />
      <Switching />
      <CtaSection kind="visit" />
      <SiteFooter />
    </>
  );
}

/** mobile.solutions */
function Phone() {
  const S = SW.SOLUTIONS;
  const pics = [
    <ScaleTo key="j" w={620} h={460}><MarkJourney /></ScaleTo>,
    <PhotoCard key="o" photo="classroom-zambia.jpg" pos="center 40%" card={<Tagged tag="Teacher portal"><RegisterCard w={310} offline /></Tagged>} />,
    <ScaleTo key="i" w={620} h={420}><PicIntegrations /></ScaleTo>,
  ];
  return (
    <>
      <PhoneNav />
      <MHero eye={S.eyebrow} k="solutions" h={S.h} b={S.b} />
      <MGap h={40} />
      <Pad><MTiles slugs={ALL} /></Pad>
      <MGap />
      <MRows items={ROWS.map(([e, h, b], i) => ({ eye: e, k: ROW_ICON[e], h, b, pic: pics[i] }))} />
      <MGap />
      <MovingBand />
      <MEnd />
    </>
  );
}

export default function Solutions() {
  return <SitePage desktop={<Desktop />} phone={<Phone />} />;
}

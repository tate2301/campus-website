import type { Metadata } from "next";
import { SitePage, Gap } from "@/components/page";
import { NavBar, PhoneNav, SiteFooter, TYPE_PHOTO } from "@/components/chrome";
import { CtaSection, DemoBtns, PageHero, RoleTile, SecHead, TypeCard, Wrap } from "@/components/sections";
import { MEnd, MGap, MHead, MHero, MRoleTile, Pad, ScaleTo } from "@/components/phone";
import { A, Explore, NavIcon, OnPlate, Ph, SchoolsCampus, sx } from "@/components/ds";
import { CP, SW } from "@/content/copy";
import { typeHref } from "@/content/links";
import { CW, GAP, INK2, SANS } from "@/lib/design";

export const metadata: Metadata = { title: "Who we serve", description: SW.WHO.b };

type Type = [string, string, string];
type Role = [string, string, string, string];

/** webpages.who_secs */
function Desktop() {
  const S = SW.WHO;
  return (
    <>
      <NavBar open="Who we serve" />
      <PageHero eye={S.eyebrow} k="who" h={S.h} b={S.b} buttons={<DemoBtns />} pic={<OnPlate w={1200} h={560}><SchoolsCampus w={1200} h={560} U={40} /></OnPlate>} />
      <Gap h={GAP} />
      <Wrap>
        <SecHead eye="Who we serve · K-12" k="who" h={S.types_h} />
        <div style={sx("display:flex;justify-content:space-between;align-items:stretch")}>{(CP.SCHOOL_TYPES as Type[]).map((t) => <TypeCard key={t[1]} t={t} />)}</div>
      </Wrap>
      <Gap h={GAP} />
      <Wrap>
        <SecHead eye="Who uses Campus" k="portals" h={CP.ROLES_H} />
        <div style={sx("display:grid;grid-template-columns:repeat(3,389px);gap:24px;justify-content:space-between")}>{(CP.ROLES as Role[]).map((r) => <RoleTile key={r[0]} r={r} />)}</div>
      </Wrap>
      <CtaSection kind="visit" />
      <SiteFooter />
    </>
  );
}

/** mobile.who */
function Phone() {
  const S = SW.WHO;
  return (
    <>
      <PhoneNav />
      <MHero eye={S.eyebrow} k="who" h={S.h} b={S.b} pic={<div style={sx("border-radius:22px;overflow:hidden")}><ScaleTo w={600} h={420}><OnPlate w={600} h={420}><SchoolsCampus w={600} h={420} /></OnPlate></ScaleTo></div>} />
      <MGap />
      <Pad>
        <MHead eye="Who we serve · K-12" k="who" h={S.types_h} />
        <div style={sx("display:flex;flex-direction:column;gap:32px")}>
          {(CP.SCHOOL_TYPES as Type[]).map(([n, k, d]) => (
            <A key={k} href={typeHref(k)} style="display:block">
              <div style={sx("position:relative")}>
                <Ph n={TYPE_PHOTO[k][0]} w={CW} h={200} pos={TYPE_PHOTO[k][1]} r={20} />
                <div style={sx("position:absolute;left:12px;bottom:12px;border-radius:12px;box-shadow:0 8px 18px -10px rgba(11,12,20,.5)")}><NavIcon k={k} s={40} /></div>
              </div>
              <div style={sx(`font:600 19px ${SANS};margin-top:14px`)}>{n}</div>
              <div style={sx(`font:400 15px/1.5 ${SANS};color:${INK2};margin-top:4px`)}>{d}</div>
              <div style={sx("margin-top:12px")}><Explore /></div>
            </A>
          ))}
        </div>
      </Pad>
      <MGap />
      <Pad>
        <MHead eye="Who uses Campus" k="portals" h={CP.ROLES_H} />
        <div style={sx("display:flex;flex-direction:column;gap:14px")}>{(CP.ROLES as Role[]).map((r) => <MRoleTile key={r[0]} r={r} />)}</div>
      </Pad>
      <MEnd />
    </>
  );
}

export default function WhoWeServe() {
  return <SitePage desktop={<Desktop />} phone={<Phone />} />;
}

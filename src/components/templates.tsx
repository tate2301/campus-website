/**
 * Page templates shared by several routes: a department (pages.dept_page for Academics, webpages.dept_secs for the
 * other eight), a kind of school (webpages.type_secs) and a role (webpages.role_secs), desktop and phone.
 */
import type { ReactNode } from "react";
import { Gap, SitePage } from "./page";
import { NavBar, PhoneNav, SiteFooter } from "./chrome";
import { CtaSection, DemoBtns, PageHero, ROW_ICON, Rows, SecHead, SplitBand, Tiles, Tools, Wrap, PicOffline } from "./sections";
import { MBand, MEnd, MGap, MHead, MHero, MRows, MTiles, MTools, Pad, PhoneOn, PhotoCard, PlateCard, ScaleTo } from "./phone";
import { At, OnPlate, Ph, PhotoStory, PortalIcon, Tagged, sx } from "./ds";
import { MarksCard, RegisterCard } from "./cards";
import { MarkJourney } from "./mark-journey";
import { ParentPhone, TimetableCard } from "./phones";
import { HeroPic, MPicOf, MTCard, PicOf, type PicSpec } from "./pictures";
import { SECTIONS } from "./who-sections";
import { M_SECTIONS } from "./who-phone";
import { CP, SW } from "@/content/copy";
import { BLUE, FAINT, GAP, INK2, SANS } from "@/lib/design";

type Row5 = [string, string, string, string, PicSpec];
const dept = (slug: string) => (CP.DEPARTMENTS as [string, string, string, string, string][]).find((d) => d[1] === slug)!;

// ---- Academics and student life ------------------------------------------------------------------------------
/** pages.dept_page */
function AcademicsDesktop() {
  const A = CP.ACADEMICS;
  const [bh, bb] = A.band;
  const pic = (
    <div style={sx("position:relative;width:1200px;height:600px")}>
      <div style={sx("position:absolute;left:90px;top:30px")}><Ph n="teacher-maths.jpg" w={1020} h={570} pos="center 30%" r={24} /></div>
      <At x={0} y={120} z={3}><Tagged tag="Teacher portal"><RegisterCard w={300} offline /></Tagged></At>
      <At x={880} y={0} z={2}><Tagged tag="Teacher portal"><MarksCard w={320} /></Tagged></At>
    </div>
  );
  const pics = [
    <PicOffline key="o" />,
    <MarkJourney key="j" />,
    <OnPlate key="t" w={620} h={460}><div style={sx("position:absolute;left:40px;top:28px")}><TimetableCard w={540} /></div></OnPlate>,
    <PhotoStory key="p" n="mother-phone.jpg" pos="65% center" cards={[[0, 8, <ParentPhone key="pp" k={0.52} />]]} w={620} h={470} />,
  ];
  return (
    <>
      <NavBar open="Solutions" />
      <PageHero eye={A.eyebrow} k="academics" h={A.h} b={A.b} buttons={<DemoBtns />} pic={pic} />
      <Gap h={GAP} />
      <SplitBand eye="One record" k="record" h={bh} b={bb} photo="girls-classroom.jpg" pos="center 35%" />
      <section style={sx(`background:#fff;padding:${GAP}px max(120px, calc(50% - 600px))`)}>
        <Rows items={(A.rows as [string, string, string][]).map(([e, h, b], i) => ({ eye: e, k: ROW_ICON[e], h, b, pic: pics[i] }))} />
      </section>
      <Tools title={A.tools_h} items={A.tools} />
      <CtaSection kind="visit" />
      <SiteFooter />
    </>
  );
}

/** mobile.academics */
function AcademicsPhone() {
  const A = CP.ACADEMICS;
  const [bh, bb] = A.band;
  const register = <Tagged tag="Teacher portal"><RegisterCard w={310} offline /></Tagged>;
  const pics = [
    <PhotoCard key="o" photo="classroom-zambia.jpg" pos="center 40%" card={register} />,
    <ScaleTo key="j" w={620} h={460}><MarkJourney /></ScaleTo>,
    <PlateCard key="t" card={<ScaleTo w={540} h={470} tw={310}><TimetableCard w={540} /></ScaleTo>} />,
    <PhoneOn key="p" phone={<ParentPhone k={0.6} />} photo="mother-phone.jpg" pos="65% center" />,
  ];
  return (
    <>
      <PhoneNav />
      <MHero eye={A.eyebrow} k="academics" h={A.h} b={A.b} pic={<PhotoCard photo="teacher-maths.jpg" pos="center 30%" card={register} />} />
      <MGap />
      <MBand eye="One record" k="record" h={bh} b={bb} photo="girls-classroom.jpg" pos="center 35%" />
      <MGap />
      <MRows items={(A.rows as [string, string, string][]).map(([e, h, b], i) => ({ eye: e, k: ROW_ICON[e], h, b, pic: pics[i] }))} />
      <MGap />
      <MTools title={A.tools_h} items={A.tools} />
      <MEnd />
    </>
  );
}

export const AcademicsPage = () => <SitePage desktop={<AcademicsDesktop />} phone={<AcademicsPhone />} />;

// ---- the other departments --------------------------------------------------------------------------------
/** webpages.dept_secs */
function DeptDesktop({ slug }: { slug: string }) {
  const [n] = dept(slug);
  const D = SW.DEPTS[slug];
  const [photo, pos, a, b] = D.hero;
  const [bh, bb, bp, bpos] = D.band;
  return (
    <>
      <NavBar open="Solutions" />
      <PageHero eye={n} k={slug} h={D.h} b={D.b} buttons={<DemoBtns />} pic={<HeroPic photo={photo} pos={pos} a={a} b={b} />} />
      <Gap h={GAP} />
      <SplitBand eye="One record" k="record" h={bh} b={bb} photo={bp} pos={bpos} />
      <Gap h={GAP} />
      <Wrap><Rows items={(D.rows as Row5[]).map(([e, k, h, b_, sp]) => ({ eye: e, k, h, b: b_, pic: <PicOf spec={sp} /> }))} /></Wrap>
      <Gap h={GAP} />
      <Tools title={SW.DEPT_TOOLS_H} items={D.tools} />
      <CtaSection kind="visit" />
      <SiteFooter />
    </>
  );
}

/** mobile.dept */
function DeptPhone({ slug }: { slug: string }) {
  const [n] = dept(slug);
  const D = SW.DEPTS[slug];
  const [photo, pos, a] = D.hero;
  const [bh, bb, bp, bpos] = D.band;
  return (
    <>
      <PhoneNav />
      <MHero eye={n} k={slug} h={D.h} b={D.b} pic={<PhotoCard photo={photo} pos={pos} card={<MTCard name={a} />} />} />
      <MGap />
      <MBand eye="One record" k="record" h={bh} b={bb} photo={bp} pos={bpos} />
      <MGap />
      <MRows items={(D.rows as Row5[]).map(([e, k, h, b_, sp]) => ({ eye: e, k, h, b: b_, pic: <MPicOf spec={sp} /> }))} />
      <MGap />
      <MTools title={SW.DEPT_TOOLS_H} items={D.tools} />
      <MEnd />
    </>
  );
}

export const DeptPage = ({ slug }: { slug: string }) => <SitePage desktop={<DeptDesktop slug={slug} />} phone={<DeptPhone slug={slug} />} />;

// ---- a kind of school --------------------------------------------------------------------------------------
/** webpages.type_secs */
function TypeDesktop({ k }: { k: string }) {
  const T = SW.TYPES[k];
  const [photo, pos, a, b] = T.hero;
  return (
    <>
      <NavBar open="Who we serve" />
      <PageHero eye={T.name} k={k} h={T.h} b={T.b} buttons={<DemoBtns />} pic={<HeroPic photo={photo} pos={pos} a={a} b={b} />} />
      {SECTIONS[k]().map((s, i) => <Section key={i}><Gap h={GAP} />{s}</Section>)}
      <Gap h={GAP} />
      <Wrap><SecHead eye="Departments" k="solutions" h={SW.TYPE_DEPTS_H} /><Tiles slugs={T.depts} /></Wrap>
      <CtaSection kind="visit" />
      <SiteFooter />
    </>
  );
}
const Section = ({ children }: { children: ReactNode }) => <>{children}</>;

/** mobile.type_page */
function TypePhone({ k }: { k: string }) {
  const T = SW.TYPES[k];
  const [photo, pos, a] = T.hero;
  return (
    <>
      <PhoneNav />
      <MHero eye={T.name} k={k} h={T.h} b={T.b} pic={<PhotoCard photo={photo} pos={pos} card={<MTCard name={a} />} />} />
      {/* mobile.m_day and its siblings put a gap before every section after the first, and type_page puts another
          before each, so those sections are 192px apart on the phone, as drawn (NOTES.md) */}
      {M_SECTIONS[k]().map((s, i) => <Section key={i}><MGap />{i ? <MGap /> : null}{s}</Section>)}
      <MGap />
      <Pad><MHead eye="Departments" k="solutions" h={SW.TYPE_DEPTS_H} /><MTiles slugs={T.depts} /></Pad>
      <MEnd />
    </>
  );
}

export const TypePage = ({ k }: { k: string }) => <SitePage desktop={<TypeDesktop k={k} />} phone={<TypePhone k={k} />} />;

// ---- a role ------------------------------------------------------------------------------------------------
/** the role's eyebrow: its portal icon, the role, and the portal it works in */
function RoleEye({ name, portal, phone = false }: { name: string; portal: string; phone?: boolean }) {
  return (
    <div style={sx(`display:flex;align-items:center;gap:${phone ? 8 : 10}px;font:500 ${phone ? 14 : 15}px ${SANS};color:${BLUE}`)}>
      <PortalIcon n={portal} s={phone ? 26 : 30} />{name}<span style={sx(`color:${FAINT}`)}>·</span><span style={sx(`color:${INK2}`)}>{portal} portal</span>
    </div>
  );
}

/** webpages.role_secs */
function RoleDesktop({ slug }: { slug: string }) {
  const R = SW.ROLE_PAGES[slug];
  const [photo, pos, a, b] = R.hero;
  return (
    <>
      <NavBar open="Who we serve" />
      <PageHero eyeNode={<RoleEye name={R.name} portal={R.portal} />} h={R.h} b={R.b} buttons={<DemoBtns />} pic={<HeroPic photo={photo} pos={pos} a={a} b={b} />} />
      <Gap h={GAP} />
      <Wrap><Rows items={(R.rows as Row5[]).map(([e, k, h, b_, sp]) => ({ eye: e, k, h, b: b_, pic: <PicOf spec={sp} /> }))} /></Wrap>
      <Gap h={GAP} />
      <Wrap><SecHead eye="Departments" k="solutions" h={SW.ROLE_DEPTS_H} /><Tiles slugs={R.depts} /></Wrap>
      <CtaSection kind="visit" />
      <SiteFooter />
    </>
  );
}

/** mobile.role */
function RolePhone({ slug }: { slug: string }) {
  const R = SW.ROLE_PAGES[slug];
  const [photo, pos, a] = R.hero;
  return (
    <>
      <PhoneNav />
      <MHero eyeNode={<RoleEye name={R.name} portal={R.portal} phone />} h={R.h} b={R.b} pic={<PhotoCard photo={photo} pos={pos} card={<MTCard name={a} />} />} />
      <MGap />
      <MRows items={(R.rows as Row5[]).map(([e, k, h, b_, sp]) => ({ eye: e, k, h, b: b_, pic: <MPicOf spec={sp} /> }))} />
      <MGap />
      <Pad><MHead eye="Departments" k="solutions" h={SW.ROLE_DEPTS_H} /><MTiles slugs={R.depts} /></Pad>
      <MEnd />
    </>
  );
}

export const RolePage = ({ slug }: { slug: string }) => <SitePage desktop={<RoleDesktop slug={slug} />} phone={<RolePhone slug={slug} />} />;

import type { Metadata } from "next";
import { SitePage, Gap } from "@/components/page";
import { NavBar, PhoneNav, SiteFooter } from "@/components/chrome";
import { CtaSection, LinkCard, PageHero, SecHead, Wrap } from "@/components/sections";
import { MEnd, MGap, MHead, MHero, Pad } from "@/components/phone";
import { CtaScene, Ic, NavIcon, sx } from "@/components/ds";
import { SW } from "@/content/copy";
import { FAINT, GAP, INK, INK2, LINE, MUTED, PLATE, SANS, SH_CARD } from "@/lib/design";

export const metadata: Metadata = { title: "Support", description: SW.SUPPORT.b };

// the guides live in Help, inside the app; the search sends the question there
const HELP = "https://app.campus.corelith.co.zw/help";
const GUIDES_HEAD = "Find the guide for your job.";
type Topic = [string, string, string[]];
type Reach = [string, string, string, string];
const input = `color:${INK};width:100%;min-width:0;border:0;padding:0;margin:0;background:transparent;outline:none`;

const Guides = ({ gs }: { gs: string[] }) => <>{gs.map((g) => (
  <div key={g} style={sx(`display:flex;justify-content:space-between;align-items:center;padding:11px 0;border-top:1px solid #e3e6eb;font:400 15px ${SANS};color:${INK2}`)}>{g}<Ic n="right-line" s={14} c={FAINT} /></div>
))}</>;

/** webpages.support_secs */
function Desktop() {
  const S = SW.SUPPORT;
  const search = (
    <form role="search" action={HELP} method="get" className="field-box" style={sx(`width:640px;height:60px;border-radius:30px;background:#fff;box-shadow:0 0 0 1px ${LINE},${SH_CARD};display:flex;align-items:center;gap:12px;padding:0 24px;box-sizing:border-box`)}>
      <Ic n="search" s={20} c={MUTED} />
      <input type="search" name="q" aria-label="Search the guides" placeholder="Search the guides, for example “match an EcoCash payment”" style={sx(`font:400 17px ${SANS};${input}`)} />
    </form>
  );
  const arts = [<CtaScene key="v" k="visit" w={588} h={220} U={26} cx={294} cy={150} labels={false} />, <CtaScene key="t" k="training" w={588} h={220} U={26} cx={294} cy={150} labels={false} />];
  return (
    <>
      <NavBar />
      <PageHero eye={S.eyebrow} k="support" h={S.h} b={S.b} pic={search} />
      <Gap h={GAP} />
      <Wrap>
        <SecHead eye="Guides" k="support" h={GUIDES_HEAD} />
        <div style={sx("display:grid;grid-template-columns:repeat(3,1fr);gap:24px")}>
          {(S.topics as Topic[]).map(([k, t, gs]) => (
            <div key={t} style={sx(`border-radius:24px;background:${PLATE};padding:28px;display:flex;flex-direction:column`)}>
              <NavIcon k={k} s={48} /><div style={sx(`font:600 22px ${SANS};letter-spacing:-0.015em;margin-top:20px`)}>{t}</div>
              <div style={sx("margin-top:12px")}><Guides gs={gs} /></div>
            </div>
          ))}
        </div>
      </Wrap>
      <Gap h={GAP} />
      <Wrap>
        <SecHead eye="Support" k="support" h={S.reach_h} />
        <div style={sx("display:flex;gap:24px;align-items:stretch")}>{(S.reach as Reach[]).map(([k, t, d, a], i) => <LinkCard key={k} k={k} t={t} d={d} act={a} art={arts[i]} />)}</div>
      </Wrap>
      <CtaSection kind="visit" />
      <SiteFooter />
    </>
  );
}

/** mobile.support */
function Phone() {
  const S = SW.SUPPORT;
  const search = (
    <form role="search" action={HELP} method="get" className="field-box" style={sx(`height:52px;border-radius:26px;background:#fff;box-shadow:0 0 0 1px ${LINE},${SH_CARD};display:flex;align-items:center;gap:10px;padding:0 18px`)}>
      <Ic n="search" s={18} c={MUTED} />
      <input type="search" name="q" aria-label="Search the guides" placeholder="Search the guides" style={sx(`font:400 15px ${SANS};${input}`)} />
    </form>
  );
  return (
    <>
      <PhoneNav />
      <MHero eye={S.eyebrow} k="support" h={S.h} b={S.b} buttons={search} />
      <MGap />
      <Pad>
        <MHead eye="Guides" k="support" h={GUIDES_HEAD} />
        <div style={sx("display:flex;flex-direction:column;gap:14px")}>
          {(S.topics as Topic[]).map(([k, t, gs]) => (
            <div key={t} style={sx(`border-radius:22px;background:${PLATE};padding:22px`)}>
              <NavIcon k={k} s={40} /><div style={sx(`font:600 20px ${SANS};margin-top:14px`)}>{t}</div>
              <div style={sx("margin-top:8px")}><Guides gs={gs} /></div>
            </div>
          ))}
        </div>
      </Pad>
      <MGap />
      <Pad>
        <MHead eye="Support" k="support" h={S.reach_h} />
        <div style={sx("display:flex;flex-direction:column;gap:14px")}>{(S.reach as Reach[]).map(([k, t, d, a]) => <LinkCard key={k} k={k} t={t} d={d} act={a} />)}</div>
      </Pad>
      <MEnd />
    </>
  );
}

export default function Support() {
  return <SitePage desktop={<Desktop />} phone={<Phone />} />;
}

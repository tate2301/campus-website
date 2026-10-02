import type { Metadata } from "next";
import { SitePage, Gap } from "@/components/page";
import { NavBar, PhoneNav, SiteFooter } from "@/components/chrome";
import { CtaSection, DemoBtns, FaqList, PageHero, Rows, SecHead, Wrap } from "@/components/sections";
import { CardHtml, HeroPic, MTCard } from "@/components/pictures";
import { Marketplace } from "@/components/site-cards";
import { MEnd, MFaq, MGap, MHead, MHero, MRows, PhotoCard, PlateCard } from "@/components/phone";
import { At, BrandLogo, Ic, OnPlate, PhotoStory, CorelithLogo, Tagged, sx } from "@/components/ds";
import { MARKET, SW } from "@/content/copy";
import { FAINT, GAP, INK, INK2, LINE, MUTED, MX, OK, OKS, PLATE, PX, SANS } from "@/lib/design";

export const metadata: Metadata = { title: "Integrations", description: SW.INTEG.b };

type IRow = [string, string, string, string, string, string | null];
const FAQ_H = "What bursars ask about the links.";

/** mobile.marketplace: the Corelith Plugins and Integrations Hub at phone width */
function PhoneMarketplace() {
  const cats = ["All", ...MARKET.map(([c]) => c)];
  return (
    <div style={sx(`border-radius:20px;background:#fff;box-shadow:0 0 0 1px ${LINE},0 24px 40px -28px rgba(11,12,20,.35);overflow:hidden`)}>
      <div style={sx("display:flex;align-items:center;gap:10px;padding:14px")}><CorelithLogo s={20} c={INK} /><span style={sx(`font:600 14px ${SANS};white-space:nowrap;padding-left:10px;border-left:1px solid ${LINE}`)}>Plugins and Integrations Hub</span></div>
      <div style={sx("padding:0 14px 12px")}>
        <div style={sx(`display:flex;align-items:center;gap:8px;height:38px;padding:0 12px;border-radius:19px;background:#f2f4f7;font:400 13.5px ${SANS};color:${FAINT}`)}><Ic n="search" s={15} c={MUTED} />Search integrations</div>
      </div>
      <div className="hscroll" style={sx("display:flex;gap:8px;padding:0 14px 14px;overflow:hidden;scroll-padding-left:14px")}>
        {cats.map((c, i) => (
          <span key={c} style={sx(`flex:none;height:34px;padding:0 14px;border-radius:17px;display:inline-flex;align-items:center;font:500 13.5px ${SANS};${i === 0 ? `background:${INK};color:#fff` : `background:#fff;color:${INK2};box-shadow:inset 0 0 0 1px ${LINE}`}`)}>{c}</span>
        ))}
      </div>
      {MARKET.flatMap(([, its]) => its).map(([n, d, st]) => (
        <div key={n} style={sx(`display:flex;align-items:center;gap:12px;padding:12px 14px;border-top:1px solid ${LINE}`)}>
          <BrandLogo n={n} s={34} />
          <div style={sx("flex:1;min-width:0")}><div style={sx(`font:600 14.5px ${SANS}`)}>{n}</div><div style={sx(`font:400 12.5px ${SANS};color:${MUTED}`)}>{d}</div></div>
          {st
            ? <span style={sx(`display:inline-flex;align-items:center;gap:4px;height:28px;padding:0 10px;border-radius:14px;background:${OKS};color:${OK};font:500 12px ${SANS}`)}><Ic n="check-line" s={12} c={OK} />Connected</span>
            : <span style={sx(`display:inline-flex;align-items:center;height:28px;padding:0 12px;border-radius:14px;box-shadow:inset 0 0 0 1px ${LINE};font:500 12px ${SANS}`)}>Add</span>}
        </div>
      ))}
    </div>
  );
}

/** webpages.integrations_secs */
function Desktop() {
  const I = SW.INTEG;
  const items = (I.rows as IRow[]).map(([e, k, h, b, cn, to], i) => {
    const c = <Tagged tag="Administration portal"><CardHtml name={cn} to={to ?? undefined} /></Tagged>;
    const pic = i === 1 ? <PhotoStory n="accountant-man.jpg" pos="center 30%" cards={[[0, 80, c]]} w={620} h={440} />
      : i === 3 ? <PhotoStory n="mother-phone.jpg" pos="65% center" cards={[[0, 90, c]]} w={620} h={440} />
      : <OnPlate w={620} h={440}><At x={150} y={40}>{c}</At></OnPlate>;
    return { eye: e, k, h, b, pic };
  });
  return (
    <>
      <NavBar open="Platform" />
      <PageHero eye={I.eyebrow} k="integrations" h={I.h} b={I.b} buttons={<DemoBtns />} pic={<HeroPic photo="girls-papers.jpg" pos="center 40%" a="payments_card" b="fiscal_card" />} />
      <Gap h={GAP} />
      <Wrap><Rows items={items} /></Wrap>
      <Gap h={GAP} />
      <section style={sx(`background:${PLATE};padding:${GAP - 40}px ${PX}`)}>
        <SecHead eye={I.market_eye} k="integrations" h={I.market_h} />
        <Marketplace w={1200} />
      </section>
      <Gap h={GAP} />
      <FaqList eye="Questions" k="questions" h={FAQ_H} qa={I.faq} />
      <CtaSection kind="visit" />
      <SiteFooter />
    </>
  );
}

/** mobile.integrations */
function Phone() {
  const I = SW.INTEG;
  const items = (I.rows as IRow[]).map(([e, k, h, b, cn, to], i) => {
    const c = <Tagged tag="Administration portal"><CardHtml name={cn} w={310} to={to ?? undefined} /></Tagged>;
    const pic = i === 1 ? <PhotoCard photo="accountant-man.jpg" pos="center 30%" card={c} /> : i === 3 ? <PhotoCard photo="mother-phone.jpg" pos="65% center" card={c} /> : <PlateCard card={c} />;
    return { eye: e, k, h, b, pic };
  });
  return (
    <>
      <PhoneNav />
      <MHero eye={I.eyebrow} k="integrations" h={I.h} b={I.b} pic={<PhotoCard photo="girls-papers.jpg" pos="center 40%" card={<MTCard name="payments_card" />} />} />
      <MGap />
      <MRows items={items} />
      <MGap />
      <section style={sx(`background:${PLATE};padding:64px ${MX}px`)}>
        <MHead eye={I.market_eye} k="integrations" h={I.market_h} />
        <PhoneMarketplace />
      </section>
      <MGap />
      <MFaq eye="Questions" k="questions" h={FAQ_H} qa={I.faq} />
      <MEnd />
    </>
  );
}

export default function Integrations() {
  return <SitePage desktop={<Desktop />} phone={<Phone />} />;
}

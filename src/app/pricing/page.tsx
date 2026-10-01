import type { Metadata } from "next";
import { Photo } from "@/components/photo";
import { SitePage, Gap } from "@/components/page";
import { NavBar, PhoneNav, SiteFooter } from "@/components/chrome";
import { CtaSection, DemoBtns, FaqList, PageHero, Row, SecHead, Steps, Wrap } from "@/components/sections";
import { BtnFull, H2, MEnd, MFaq, MGap, MHead, MHero, MRow, P, PEyebrow, Pad } from "@/components/phone";
import { PricingCard } from "@/components/pricing";
import { Calculator } from "@/components/calculator";
import { CtaScene, Eyebrow, Head, NavIcon, Para, Scaled, sx } from "@/components/ds";
import { CP, FAQ, SW } from "@/content/copy";
import { PHOTO_ALT } from "@/content/photo-alt";
import { CW, DOTS, GAP, INK2, MX, PLATE, PX, SANS, pyRound } from "@/lib/design";

export const metadata: Metadata = { title: "Pricing", description: SW.PRICE.b };

// written into webpages.pricing_secs and mobile.pricing, not in the copy modules
const CALC_HEAD = "Your school's figure, before you call us.";
const INCL_HEAD = "Everything, at US$1 per active pupil per month.";
const SETUP_HEAD = "Running in four weeks, with us at the school.";
const FAQ_HEAD = "What schools ask about the price.";
const QA: [string, string][] = [...FAQ, ["What does setup cost?", "Nothing. Setup, data capture and training are free."],
  ["Is there a charge per user?", "No. Staff, guardians and pupils sign in at no extra cost."]];

/** webpages.pricing_secs */
function Desktop() {
  const Pr = SW.PRICE;
  const cards = (
    <div style={sx("display:flex;gap:24px;align-items:stretch;width:1200px")}>
      <div style={sx("flex:none;width:340px;border-radius:24px;overflow:hidden;position:relative;background:#dfe2e7")}>
        <Photo src="/assets/photos/girl-beret.jpg" alt={PHOTO_ALT["girl-beret.jpg"]} width={340} height={600} loading="eager" decoding="sync"
          style={sx("position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:center 20%")} />
      </div>
      <PricingCard p={CP.PRICING.main} primary w={418} /><PricingCard p={CP.PRICING.lms} primary={false} w={418} />
    </div>
  );
  return (
    <>
      <NavBar open="Pricing" />
      <PageHero eye={Pr.eyebrow} k="pricing" h={Pr.h} b={Pr.b} buttons={<DemoBtns price />} pic={cards} />
      <Gap h={GAP} />
      <Wrap><Row eye={Pr.calc_h} k="calculator" h={CALC_HEAD} b={Pr.calc_b} pic={<Calculator w={560} id="calculator" />} /></Wrap>
      <Gap h={GAP} />
      <Wrap>
        <SecHead eye={Pr.incl_h} k="included" h={INCL_HEAD} />
        <div style={sx("display:grid;grid-template-columns:repeat(4,1fr);gap:24px")}>
          {(Pr.included as [string, string, string][]).map(([k, t, d]) => (
            <div key={t} style={sx(`display:flex;flex-direction:column;gap:12px;padding:24px;border-radius:20px;background:${PLATE}`)}>
              <NavIcon k={k} s={48} /><div style={sx(`font:600 18px ${SANS};margin-top:6px`)}>{t}</div><div style={sx(`font:400 14.5px/1.5 ${SANS};color:${INK2}`)}>{d}</div>
            </div>
          ))}
        </div>
      </Wrap>
      <Gap h={GAP} />
      <section style={sx(`background:${PLATE};padding:${GAP - 40}px ${PX}`)}>
        <div style={sx("display:flex;justify-content:space-between;align-items:center;gap:72px")}>
          <div style={sx("width:520px;display:flex;flex-direction:column;gap:20px")}>
            <Eyebrow t={Pr.setup_h} k="training" /><Head t={SETUP_HEAD} size={44} w={520} /><Para t={Pr.setup_b} size={18} c={INK2} mw={500} />
            <div style={sx("margin-top:8px")}><Steps items={CP.SWITCH.steps} w={520} /></div>
          </div>
          <div style={sx(`width:600px;height:520px;border-radius:24px;overflow:hidden;${DOTS};box-shadow:inset 0 0 0 1px #e3e6eb;flex:none`)}>
            <CtaScene k="training" w={600} h={520} U={46} cx={300} cy={300} />
          </div>
        </div>
      </section>
      <Gap h={GAP} />
      <FaqList eye={Pr.faq_h} k="questions" h={FAQ_HEAD} qa={QA} />
      {/* rules.md: the Price call to action closes Pricing (the drawn page closes with Visit; NOTES.md) */}
      <CtaSection kind="price" hrefs={{ "Work out your school": "#calculator" }} />
      <SiteFooter />
    </>
  );
}

/** mobile.pricing */
function Phone() {
  const Pr = SW.PRICE;
  return (
    <>
      <PhoneNav />
      <MHero eye={Pr.eyebrow} k="pricing" h={Pr.h} b={Pr.b}
        pic={<div style={sx("display:flex;flex-direction:column;gap:14px")}><PricingCard p={CP.PRICING.main} primary w="100%" /><PricingCard p={CP.PRICING.lms} primary={false} w="100%" /></div>}
        buttons={<><BtnFull label="Book a demo" /><BtnFull label="Download the price sheet (PDF)" icon="download-2" kind="secondary" /></>} />
      <MGap />
      <MRow eye={Pr.calc_h} k="calculator" h={CALC_HEAD} b={Pr.calc_b} pic={<Calculator w="100%" id="calculator-phone" />} />
      <MGap />
      <Pad>
        <MHead eye={Pr.incl_h} k="included" h={INCL_HEAD} />
        <div style={sx("display:grid;grid-template-columns:1fr 1fr;gap:12px")}>
          {(Pr.included as [string, string, string][]).map(([k, t, d]) => (
            <div key={t} style={sx(`display:flex;flex-direction:column;gap:8px;padding:18px;border-radius:18px;background:${PLATE}`)}>
              <NavIcon k={k} s={40} /><div style={sx(`font:600 15.5px/1.25 ${SANS};margin-top:4px`)}>{t}</div><div style={sx(`font:400 13.5px/1.45 ${SANS};color:${INK2}`)}>{d}</div>
            </div>
          ))}
        </div>
      </Pad>
      <MGap />
      <section style={sx(`background:${PLATE};padding:64px ${MX}px;display:flex;flex-direction:column;gap:14px`)}>
        <PEyebrow t={Pr.setup_h} k="training" /><H2 t={SETUP_HEAD} /><P t={Pr.setup_b} />
        <div style={sx(`border-radius:20px;overflow:hidden;${DOTS};box-shadow:inset 0 0 0 1px #e3e6eb;margin-top:8px`)}>
          <Scaled w={CW} h={pyRound(460 * CW / 600)} k={CW / 600}><CtaScene k="training" w={600} h={460} U={46} cx={300} cy={270} /></Scaled>
        </div>
        <div style={sx("margin-top:8px")}><Steps items={CP.SWITCH.steps} w={CW} /></div>
      </section>
      <MGap />
      <MFaq eye={Pr.faq_h} k="questions" h={FAQ_HEAD} qa={QA} />
      <MEnd kind="price" hrefs={{ "Work out your school": "#calculator-phone" }} />
    </>
  );
}

export default function Pricing() {
  return <SitePage desktop={<Desktop />} phone={<Phone />} />;
}

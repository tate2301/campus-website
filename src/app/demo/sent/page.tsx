import type { Metadata } from "next";
import type { ReactNode } from "react";
import { SitePage, Gap } from "@/components/page";
import { NavBar, PhoneNav, PhoneFooter, SiteFooter } from "@/components/chrome";
import { LinkCard, Wrap } from "@/components/sections";
import { H1, MGap, P, Pad } from "@/components/phone";
import { CtaScene, Ic, Para, Scaled, sx } from "@/components/ds";
import { SW } from "@/content/copy";
import { CW, DOTS, GAP, INK2, MX, OK, OKS, PX, SANS } from "@/lib/design";

export const metadata: Metadata = { title: "Request sent", robots: { index: false } };

// the three next steps, as written in webpages.sent_secs and mobile.sent
const NEXT: [string, string, string, string][] = [
  ["pricing", "Pricing", "US$1 per active pupil per month, with setup and training free.", "See pricing"],
  ["moving", "Moving to Campus", "How we move your records in four weeks.", "How we move your records"],
  ["pricesheet", "The price sheet", "One page to take to your SDC or board.", "Download the price sheet (PDF)"],
];
const cards = (): ReactNode[] => NEXT.map(([k, t, d, a]) => <LinkCard key={k} k={k} t={t} d={d} act={a} />);

/** webpages.sent_secs */
function Desktop() {
  const S = SW.SENT;
  return (
    <>
      <NavBar />
      <section style={sx(`display:flex;flex-direction:column;align-items:center;text-align:center;padding:72px ${PX} 0`)}>
        <div style={sx(`width:760px;height:400px;border-radius:28px;overflow:hidden;${DOTS};box-shadow:inset 0 0 0 1px #e3e6eb`)}><CtaScene k="visit" w={760} h={400} U={42} cx={380} cy={235} /></div>
        <span style={sx(`width:52px;height:52px;border-radius:26px;background:${OKS};display:flex;align-items:center;justify-content:center;margin-top:44px`)}><Ic n="check-line" s={26} c={OK} /></span>
        <h1 style={sx(`margin:22px 0 0;font:600 56px/1.05 ${SANS};letter-spacing:-0.04em`)}>{S.h}</h1>
        <div style={sx("margin-top:18px")}><Para t={S.b} size={20} c={INK2} mw={620} centre /></div>
      </section>
      <Gap h={120} />
      <Wrap>
        <div style={sx(`font:600 22px ${SANS};letter-spacing:-0.015em;margin-bottom:24px;text-align:center`)}>{S.next_h}</div>
        <div style={sx("display:flex;gap:24px;align-items:stretch")}>{cards()}</div>
      </Wrap>
      <Gap h={GAP} />
      <SiteFooter />
    </>
  );
}

/** mobile.sent */
function Phone() {
  const S = SW.SENT;
  return (
    <>
      <PhoneNav />
      <section style={sx(`padding:32px ${MX}px 0;display:flex;flex-direction:column;align-items:center;text-align:center`)}>
        <div style={sx(`border-radius:22px;overflow:hidden;${DOTS};box-shadow:inset 0 0 0 1px #e3e6eb`)}>
          <Scaled w={CW} h={210} k={CW / 700}><CtaScene k="visit" w={700} h={420} U={42} cx={350} cy={245} /></Scaled>
        </div>
        <span style={sx(`width:48px;height:48px;border-radius:24px;background:${OKS};display:flex;align-items:center;justify-content:center;margin-top:32px`)}><Ic n="check-line" s={24} c={OK} /></span>
        <div style={sx("margin-top:18px")}><H1 t={S.h} /></div>
        <div style={sx("margin-top:12px")}><P t={S.b} size={17} /></div>
      </section>
      <MGap h={64} />
      <Pad>
        <div style={sx(`font:600 20px ${SANS};margin-bottom:18px;text-align:center`)}>{S.next_h}</div>
        <div style={sx("display:flex;flex-direction:column;gap:14px")}>{cards()}</div>
      </Pad>
      <MGap />
      <PhoneFooter />
    </>
  );
}

export default function Sent() {
  return <SitePage desktop={<Desktop />} phone={<Phone />} />;
}

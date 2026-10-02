import type { Metadata } from "next";
import { SitePage, Gap } from "@/components/page";
import { NavBar, PhoneNav, SiteFooter } from "@/components/chrome";
import { Band, CtaSection, FaqList, PageHero } from "@/components/sections";
import { BtnFull, MEnd, MFaq, MGap, MHead, MHero, Pad } from "@/components/phone";
import { Cbtn, CtaScene, Eyebrow, Head, NavIcon, Ph, Scaled, sx } from "@/components/ds";
import { CP } from "@/content/copy";
import { ACTION_HREF } from "@/content/links";
import { CW, DOTS, GAP, INK, INK2, LINE, MX, PLATE, SANS, pyRound } from "@/lib/design";

export const metadata: Metadata = { title: "Moving to Campus", description: CP.SWITCH.b };

// written into pages.switch_page and mobile.moving in the design source, not in the copy modules
const PLAN_EYE = "The four weeks", PLAN_H = "From your old system to your first term on Campus.";
const WHAT_EYE = "What moves", WHAT_H = "Everything the school keeps, on one record.";
const FAQ_H = "What schools ask before they move.";
const LINES = ["Every pupil’s record with their guardians, class and house.", "Contracts, leave balances and the details payroll needs.",
  "Each family’s balance in US dollars and ZiG, signed off by the bursar.", "This year’s marks and the reports already sent home.",
  "Forms, subjects, rooms and the timetable for the term.", "Stores, uniforms and textbooks, with what is issued to whom."];
const KEYS = ["Parent", "hr-payroll", "fees", "record", "calendar-t", "stock"];
const SHOTS: [string, string][] = [["mother-phone.jpg", "65% center"], ["teacher-notebook.jpg", "center 25%"], ["classroom-uniforms.jpg", "center"],
  ["teacher-maths.jpg", "center 30%"], ["classroom-zambia.jpg", "center 40%"], ["boys-laptop.jpg", "center"]];

/** pages.switch_page */
function Desktop() {
  const S = CP.SWITCH;
  const pic = (
    <div style={sx(`width:1200px;height:520px;border-radius:32px;${DOTS};box-shadow:inset 0 0 0 1px #eceef2;overflow:hidden;display:flex;gap:0`)}>
      <CtaScene k="visit" w={600} h={520} U={50} cx={300} cy={300} /><CtaScene k="training" w={600} h={520} U={50} cx={300} cy={300} />
    </div>
  );
  return (
    <>
      <NavBar open="Platform" />
      <PageHero eye={S.eyebrow} k="moving" h={S.h} b={S.b} pic={pic} buttons={<>
        <Cbtn label="Book a demo" icon="calendar" kind="primary" size="lg" href={ACTION_HREF["Book a demo"]} />
        <Cbtn label="Download the price sheet (PDF)" icon="download-2" kind="secondary" size="lg" href={ACTION_HREF["Download the price sheet (PDF)"]} />
      </>} />
      <Gap h={GAP} />
      <Band bg={PLATE}>
        <div style={sx("display:flex;flex-direction:column;gap:16px;margin-bottom:44px")}><Eyebrow t={PLAN_EYE} k="demo" /><Head t={PLAN_H} size={46} w={820} /></div>
        <div style={sx("display:flex;gap:20px;align-items:stretch")}>
          {(S.steps as [string, string, string][]).map(([, t, d], i) => (
            <div key={t} style={sx(`flex:1;border-radius:24px;background:#fff;box-shadow:inset 0 0 0 1px ${LINE};padding:28px 26px;box-sizing:border-box;display:flex;flex-direction:column;gap:10px`)}>
              <div style={sx(`font:600 22px ${SANS};letter-spacing:-0.015em`)}>{i + 1}. {t}</div>
              <div style={sx(`font:400 15px/1.55 ${SANS};color:${INK2}`)}>{d}</div>
            </div>
          ))}
        </div>
      </Band>
      <Band>
        <div style={sx("display:flex;flex-direction:column;gap:14px;margin-bottom:44px")}><Eyebrow t={WHAT_EYE} k="stock" /><Head t={WHAT_H} size={46} w={820} /></div>
        <div style={sx("display:grid;grid-template-columns:repeat(3,1fr);gap:24px")}>
          {(S.moves as string[]).map((m, i) => (
            <div key={m} className="cmp-hov" style={sx(`height:300px;border-radius:24px;background:${PLATE};box-sizing:border-box;padding:28px;display:flex;flex-direction:column`)}>
              <div className="cmp-img"><Ph n={SHOTS[i][0]} w={389} h={300} pos={SHOTS[i][1]} r={0} alt="" /></div>
              <div className="cmp-txt" style={sx("display:flex;flex-direction:column;height:100%")}>
                <NavIcon k={KEYS[i]} s={48} />
                <div style={sx(`margin-top:auto;font:600 24px/1.15 ${SANS};letter-spacing:-0.02em;color:${INK};text-wrap:balance`)}>{m}</div>
                <div style={sx(`font:400 15px/1.5 ${SANS};color:${INK2};margin-top:8px`)}>{LINES[i]}</div>
              </div>
            </div>
          ))}
        </div>
      </Band>
      <FaqList eye="Questions" k="questions" h={FAQ_H} qa={S.faq} />
      <CtaSection kind="training" />
      <SiteFooter />
    </>
  );
}

/** mobile.moving */
function Phone() {
  const S = CP.SWITCH;
  return (
    <>
      <PhoneNav />
      <MHero eye={S.eyebrow} k="moving" h={S.h} b={S.b}
        pic={<div style={sx(`border-radius:22px;overflow:hidden;${DOTS}`)}><Scaled w={CW} h={pyRound(520 * CW / 600)} k={CW / 600}><CtaScene k="visit" w={600} h={520} U={50} cx={300} cy={300} /></Scaled></div>}
        buttons={<><BtnFull label="Book a demo" /><BtnFull label="Download the price sheet (PDF)" icon="download-2" kind="secondary" /></>} />
      <MGap />
      <section style={sx(`background:${PLATE};padding:64px ${MX}px`)}>
        <MHead eye={PLAN_EYE} k="demo" h={PLAN_H} />
        <div style={sx("display:flex;flex-direction:column;gap:12px")}>
          {(S.steps as [string, string, string][]).map(([, t, d], i) => (
            <div key={t} style={sx(`border-radius:20px;background:#fff;box-shadow:inset 0 0 0 1px ${LINE};padding:22px 20px`)}>
              <div style={sx(`font:600 19px ${SANS}`)}>{i + 1}. {t}</div>
              <div style={sx(`font:400 15px/1.55 ${SANS};color:${INK2};margin-top:6px`)}>{d}</div>
            </div>
          ))}
        </div>
      </section>
      <MGap />
      <Pad>
        <MHead eye={WHAT_EYE} k="stock" h={WHAT_H} />
        <div style={sx("display:flex;flex-direction:column;gap:12px")}>
          {(S.moves as string[]).map((m, i) => (
            <div key={m} style={sx(`border-radius:20px;background:${PLATE};padding:22px;display:flex;gap:14px`)}>
              <NavIcon k={KEYS[i]} s={40} />
              <div><div style={sx(`font:600 18px/1.2 ${SANS}`)}>{m}</div><div style={sx(`font:400 14.5px/1.5 ${SANS};color:${INK2};margin-top:4px`)}>{LINES[i]}</div></div>
            </div>
          ))}
        </div>
      </Pad>
      <MGap />
      <MFaq eye="Questions" k="questions" h={FAQ_H} qa={S.faq} />
      <MEnd kind="training" />
    </>
  );
}

export default function Moving() {
  return <SitePage desktop={<Desktop />} phone={<Phone />} />;
}

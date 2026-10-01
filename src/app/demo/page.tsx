import type { Metadata } from "next";
import { SitePage, Gap } from "@/components/page";
import { NavBar, PhoneNav, SiteFooter } from "@/components/chrome";
import { CtaSection, FaqList, Rows, SecHead, Wrap } from "@/components/sections";
import { TCard } from "@/components/pictures";
import { CheckInput, FieldInput } from "@/components/forms";
import { FormKit } from "@/components/form-kit";
import { H1, MEnd, MFaq, MGap, MHead, MRow, P, PEyebrow, Pad, PhotoCard } from "@/components/phone";
import { Cbtn, Eyebrow, Para, PhotoStory, sx } from "@/components/ds";
import { SW } from "@/content/copy";
import { BLUE, GAP, INK2, LINE, MONO, MUTED, MX, PLATE, PX, SANS, SH_CARD } from "@/lib/design";

export const metadata: Metadata = { title: "Book a demo", description: SW.DEMO.b };

// the role list is not drawn (the design shows "Head" chosen); these are the people who book a demo
const ROLES = ["Head", "Deputy head", "Bursar", "SDC member", "Teacher", "Other"];
const MIN_H: Record<string, number> = { head_card: 340, payments_card: 340, register_card: 420, plan_card: 420 };

/** webpages.demo_form: the form, posting to /api/demo */
function DemoForm({ id }: { id: string }) {
  const f = (n: string) => `${id}-${n}`;
  return (
    <form id={id} action="/api/demo" method="post" style={sx(`width:560px;box-sizing:border-box;padding:36px;border-radius:24px;background:#fff;box-shadow:0 0 0 1px ${LINE},${SH_CARD}`)}>
      <div style={sx(`font:600 24px ${SANS};letter-spacing:-0.015em`)}>Book a demo</div>
      <div style={sx(`font:400 15px ${SANS};color:${MUTED};margin-top:6px`)}>We call you to arrange a visit.</div>
      <div style={sx("display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:26px")}>
        <FieldInput id={f("name")} name="name" label="Your name" ph="Chipo Mutasa" w={234} required autoComplete="name" />
        <FieldInput id={f("role")} name="role" label="Your role" ph="Head" kind="select" options={ROLES} w={234} required />
        <FieldInput id={f("school")} name="school" label="School" ph="Mukuvisi High School" w={234} required autoComplete="organization" />
        <FieldInput id={f("pupils")} name="pupils" label="Active pupils" ph="1,140" help="Roughly is fine." w={234} />
        <FieldInput id={f("phone")} name="phone" label="Phone" ph="+263 77 000 0000" type="tel" w={234} required autoComplete="tel" />
        <FieldInput id={f("email")} name="email" label="Email" ph="head@yourschool.ac.zw" type="email" w={234} autoComplete="email" />
      </div>
      <div role="group" aria-labelledby={f("kind")} style={sx("margin-top:22px")}>
        <div id={f("kind")} style={sx(`font:500 14px ${SANS};margin-bottom:10px`)}>Your school</div>
        <div style={sx("display:flex;gap:28px")}>
          {["Day", "Boarding", "Primary", "Secondary"].map((t) => <CheckInput key={t} label={t} name="school_kind" value={t} />)}
        </div>
      </div>
      <div role="radiogroup" aria-labelledby={f("how")} style={sx("margin-top:20px")}>
        <div id={f("how")} style={sx(`font:500 14px ${SANS};margin-bottom:10px`)}>How should we show you?</div>
        <div style={sx("display:flex;gap:28px")}>
          <CheckInput label="Visit the school" name="how" value="visit" radio checked /><CheckInput label="Video call" name="how" value="video" radio />
        </div>
      </div>
      <div style={sx(`display:flex;justify-content:space-between;align-items:center;margin-top:30px;padding-top:22px;border-top:1px solid ${LINE}`)}>
        <span style={sx(`font:400 13px/1.5 ${SANS};color:${MUTED};max-width:250px`)}>We use these details only to arrange the demo.</span>
        <Cbtn label="Book a demo" icon="calendar" kind="primary" size="lg" type="submit" />
      </div>
      <FormKit font={SANS} />
    </form>
  );
}

/** mobile.demo's form */
function PhoneDemoForm({ id }: { id: string }) {
  const f = (n: string) => `${id}-${n}`;
  return (
    <form id={id} action="/api/demo" method="post" style={sx(`border-radius:22px;background:#fff;box-shadow:0 0 0 1px ${LINE},${SH_CARD};padding:24px 20px;display:flex;flex-direction:column;gap:16px`)}>
      <div style={sx(`font:600 22px ${SANS}`)}>Book a demo</div>
      <FieldInput id={f("name")} name="name" label="Your name" ph="Chipo Mutasa" w={310} required autoComplete="name" />
      <FieldInput id={f("role")} name="role" label="Your role" ph="Head" kind="select" options={ROLES} w={310} required />
      <FieldInput id={f("school")} name="school" label="School" ph="Mukuvisi High School" w={310} required autoComplete="organization" />
      <FieldInput id={f("pupils")} name="pupils" label="Active pupils" ph="1,140" help="Roughly is fine." w={310} />
      <FieldInput id={f("phone")} name="phone" label="Phone" ph="+263 77 000 0000" type="tel" w={310} required autoComplete="tel" />
      <FieldInput id={f("email")} name="email" label="Email" ph="head@yourschool.ac.zw" type="email" w={310} autoComplete="email" />
      <div role="radiogroup" aria-labelledby={f("how")}>
        <div id={f("how")} style={sx(`font:500 14px ${SANS};margin-bottom:10px`)}>How should we show you?</div>
        <div style={sx("display:flex;gap:24px")}><CheckInput label="Visit the school" name="how" value="visit" radio checked /><CheckInput label="Video call" name="how" value="video" radio /></div>
      </div>
      <div style={sx("display:flex")}><Cbtn label="Book a demo" icon="calendar" kind="primary" size="lg" type="submit" full /></div>
      <div style={sx(`font:400 13px/1.5 ${SANS};color:${MUTED}`)}>We use these details only to arrange the demo.</div>
      <FormKit font={SANS} />
    </form>
  );
}

type Agenda = [string, string, string, string, string];

/** webpages.demo_secs */
function Desktop() {
  const D = SW.DEMO;
  const [e, k, h, b] = D.who;
  return (
    <>
      <NavBar />
      <Wrap pad={`88px ${PX} 0`}>
        <div style={sx("display:flex;justify-content:space-between;align-items:flex-start")}>
          <div style={sx("width:540px;display:flex;flex-direction:column;gap:22px")}>
            <Eyebrow t={D.eyebrow} k="demo" />
            <h1 style={sx(`margin:0;font:600 56px/1.05 ${SANS};letter-spacing:-0.04em;text-wrap:balance`)}>{D.h}</h1>
            <Para t={D.b} size={19} c={INK2} mw={520} />
            <div style={sx("margin-top:18px")}>
              <div style={sx(`font:600 18px ${SANS};margin-bottom:6px`)}>{D.next_h}</div>
              {(D.steps as [string, string, string][]).map(([n, t, d]) => (
                <div key={n} style={sx(`display:flex;gap:16px;padding:16px 0;border-top:1px solid ${LINE}`)}>
                  <span style={sx(`width:32px;height:32px;border-radius:16px;background:#e8effd;color:${BLUE};display:flex;align-items:center;justify-content:center;font:600 14px ${SANS};flex:none`)}>{n}</span>
                  <div><div style={sx(`font:600 17px ${SANS}`)}>{t}</div><div style={sx(`font:400 15px/1.55 ${SANS};color:${INK2};margin-top:4px`)}>{d}</div></div>
                </div>
              ))}
            </div>
          </div>
          <DemoForm id="demo-d" />
        </div>
      </Wrap>
      <Gap h={GAP} />
      <Wrap>
        <SecHead eye="Your demo" k="demo" h={D.agenda_h} />
        <div style={sx("display:grid;grid-template-columns:1fr 1fr;gap:24px")}>
          {(D.agenda as Agenda[]).map(([time, room, t, d, cn]) => (
            <div key={time} style={sx(`position:relative;min-height:${MIN_H[cn]}px;border-radius:24px;background:${PLATE};overflow:hidden;padding:30px;box-sizing:border-box`)}>
              <div style={sx("width:206px;display:flex;flex-direction:column;gap:12px")}>
                <span style={sx(`display:inline-flex;align-self:flex-start;align-items:center;gap:6px;height:28px;padding:0 11px;border-radius:14px;background:#fff;box-shadow:inset 0 0 0 1px ${LINE};font:500 13px ${SANS};color:${INK2}`)}>
                  <b style={sx(`font:500 12.5px ${MONO};color:${BLUE}`)}>{time}</b>{room}
                </span>
                <div style={sx(`font:600 24px/1.15 ${SANS};letter-spacing:-0.02em;text-wrap:balance`)}>{t}</div>
                <div style={sx(`font:400 15px/1.55 ${SANS};color:${INK2}`)}>{d}</div>
              </div>
              <div style={sx("position:absolute;right:28px;top:30px")}><TCard name={cn} w={300} /></div>
            </div>
          ))}
        </div>
      </Wrap>
      <Gap h={GAP} />
      <Wrap><Rows items={[{ eye: e, k, h, b, pic: <PhotoStory n="woman-files.jpg" pos="center 30%" cards={[[0, 70, <TCard key="v" name="visitors_card" />]]} w={620} h={460} /> }]} /></Wrap>
      <Gap h={GAP} />
      <FaqList eye="Questions" k="questions" h={D.faq_h} qa={D.faq} />
      {/* rules.md: Training closes the demo page (the drawn page has no call to action; NOTES.md) */}
      <CtaSection kind="training" hrefs={{ "Book a demo": "#demo-d" }} />
      <SiteFooter />
    </>
  );
}

/** mobile.demo */
function Phone() {
  const D = SW.DEMO;
  const [e, k, h, b] = D.who;
  return (
    <>
      <PhoneNav />
      <section style={sx(`padding:36px ${MX}px 0;display:flex;flex-direction:column;gap:18px`)}>
        <PEyebrow t={D.eyebrow} k="demo" /><H1 t={D.h} /><P t={D.b} size={17} />
        <div>
          <div style={sx(`font:600 17px ${SANS};margin-bottom:4px`)}>{D.next_h}</div>
          {(D.steps as [string, string, string][]).map(([n, t, d]) => (
            <div key={n} style={sx(`display:flex;gap:14px;padding:14px 0;border-top:1px solid ${LINE}`)}>
              <span style={sx(`width:30px;height:30px;border-radius:15px;background:#e8effd;color:${BLUE};display:flex;align-items:center;justify-content:center;font:600 13.5px ${SANS};flex:none`)}>{n}</span>
              <div><div style={sx(`font:600 16px ${SANS}`)}>{t}</div><div style={sx(`font:400 14.5px/1.5 ${SANS};color:${INK2};margin-top:3px`)}>{d}</div></div>
            </div>
          ))}
        </div>
        <div style={sx("margin-top:8px")}><PhoneDemoForm id="demo-p" /></div>
      </section>
      <MGap />
      <Pad>
        <MHead eye="Your demo" k="demo" h={D.agenda_h} />
        <div style={sx("display:flex;flex-direction:column;gap:14px")}>
          {(D.agenda as Agenda[]).map(([t, room, h_, d, cn]) => (
            <div key={t} style={sx(`border-radius:22px;background:${PLATE};padding:22px 18px 22px`)}>
              <span style={sx(`display:inline-flex;align-items:center;gap:6px;height:28px;padding:0 11px;border-radius:14px;background:#fff;box-shadow:inset 0 0 0 1px ${LINE};font:500 13px ${SANS};color:${INK2}`)}>
                <b style={sx(`font:500 12.5px ${MONO};color:${BLUE}`)}>{t}</b>{room}
              </span>
              <div style={sx(`font:600 21px/1.2 ${SANS};letter-spacing:-0.02em;margin-top:12px`)}>{h_}</div>
              <div style={sx(`font:400 15px/1.5 ${SANS};color:${INK2};margin-top:6px`)}>{d}</div>
              <div style={sx("margin-top:16px;display:flex;justify-content:center")}><TCard name={cn} w={310} /></div>
            </div>
          ))}
        </div>
      </Pad>
      <MGap />
      <MRow eye={e} k={k} h={h} b={b} pic={<PhotoCard photo="woman-files.jpg" pos="center 30%" card={<TCard name="visitors_card" w={326} />} />} />
      <MGap />
      <MFaq eye="Questions" k="questions" h={D.faq_h} qa={D.faq} />
      <MEnd kind="training" hrefs={{ "Book a demo": "#demo-p" }} />
    </>
  );
}

export default function Demo() {
  return <SitePage desktop={<Desktop />} phone={<Phone />} />;
}

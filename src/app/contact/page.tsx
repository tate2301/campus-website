import type { Metadata } from "next";
import { SitePage, Gap } from "@/components/page";
import { NavBar, PhoneNav, SiteFooter } from "@/components/chrome";
import { CtaSection, DemoBtns, LinkCard, PageHero, Wrap } from "@/components/sections";
import { ThreadCard } from "@/components/site-cards";
import { FieldInput, PillInput } from "@/components/forms";
import { SentNote } from "@/components/sent-note";
import { H2, MEnd, MGap, MHero, P, PEyebrow, Pad, PhotoCard } from "@/components/phone";
import { Cbtn, Eyebrow, Head, Para, PhotoStory, Tagged, sx } from "@/components/ds";
import { SW } from "@/content/copy";
import { CW, GAP, INK2, MUTED, MX, PLATE, PX, SANS } from "@/lib/design";

export const metadata: Metadata = { title: "Contact", description: SW.CONTACT.b };

type Route = [string, string, string, string];
const note = sx(`font:400 15px ${SANS};color:${MUTED};margin-left:16px;align-self:center`);

/** webpages.contact_secs */
function Desktop() {
  const C = SW.CONTACT;
  return (
    <>
      <NavBar />
      <PageHero eye={C.eyebrow} k="contact" h={C.h} b={C.b} buttons={<DemoBtns />} />
      <Wrap><div style={sx("display:flex;gap:24px;align-items:stretch")}>{(C.routes as Route[]).map(([k, t, d, a]) => <LinkCard key={k} k={k} t={t} d={d} act={a} />)}</div></Wrap>
      <Gap h={GAP} />
      <section style={sx(`background:${PLATE};padding:${GAP - 40}px ${PX}`)}>
        <div style={sx("display:flex;justify-content:space-between;align-items:center")}>
          <form id="message" action="/api/contact" method="post" style={sx("width:520px;display:flex;flex-direction:column;gap:20px")}>
            <Eyebrow t={C.form_h} k="contact" /><Head t={C.form_hh} size={44} w={520} /><Para t={C.form_b} size={18} c={INK2} mw={500} />
            <div role="radiogroup" aria-label="Topic" style={sx("display:flex;gap:8px;flex-wrap:wrap;margin-top:8px")}>
              {(C.topics as string[]).map((t, i) => <PillInput key={t} t={t} name="topic" checked={i === 0} />)}
            </div>
            <div style={sx("display:grid;grid-template-columns:1fr 1fr;gap:20px;margin-top:4px")}>
              <FieldInput id="c-d-name" name="name" label="Your name" ph="Chipo Mutasa" w={250} autoComplete="name" />
              <FieldInput id="c-d-email" name="email" type="email" label="Email" ph="head@mukuvisi.ac.zw" w={250} autoComplete="email" required />
            </div>
            <FieldInput id="c-d-org" name="organisation" label="Organisation" ph="Mukuvisi High School" w={520} autoComplete="organization" />
            <FieldInput id="c-d-msg" name="message" label="Message" ph="What would you like to ask?" kind="area" w={520} required />
            <div style={sx("display:flex;margin-top:6px")}><Cbtn label="Send message" icon="send-plane" kind="primary" size="lg" type="submit" /><SentNote style={note} /></div>
          </form>
          <PhotoStory n="office-documents.jpg" pos="center 30%" cards={[[0, 250, <Tagged key="t" tag="Campus team"><ThreadCard w={340} /></Tagged>]]} w={620} h={640} />
        </div>
      </section>
      <CtaSection kind="visit" />
      <SiteFooter />
    </>
  );
}

/** mobile.contact */
function Phone() {
  const C = SW.CONTACT;
  return (
    <>
      <PhoneNav />
      <MHero eye={C.eyebrow} k="contact" h={C.h} b={C.b} />
      <MGap h={40} />
      <Pad><div style={sx("display:flex;flex-direction:column;gap:14px")}>{(C.routes as Route[]).map(([k, t, d, a]) => <LinkCard key={k} k={k} t={t} d={d} act={a} to={a === "Write to us" ? "#message-phone" : undefined} />)}</div></Pad>
      <MGap />
      <form id="message-phone" action="/api/contact" method="post" style={sx(`background:${PLATE};padding:64px ${MX}px;display:flex;flex-direction:column;gap:16px`)}>
        <PEyebrow t={C.form_h} k="contact" /><H2 t={C.form_hh} /><P t={C.form_b} />
        <div role="radiogroup" aria-label="Topic" style={sx("display:flex;flex-wrap:wrap;gap:8px")}>
          {(C.topics as string[]).map((t, i) => <PillInput key={t} t={t} name="topic" checked={i === 0} />)}
        </div>
        <FieldInput id="c-p-name" name="name" label="Your name" ph="Chipo Mutasa" w="100%" autoComplete="name" />
        <FieldInput id="c-p-email" name="email" type="email" label="Email" ph="head@mukuvisi.ac.zw" w="100%" autoComplete="email" required />
        <FieldInput id="c-p-org" name="organisation" label="Organisation" ph="Mukuvisi High School" w="100%" autoComplete="organization" />
        <FieldInput id="c-p-msg" name="message" label="Message" ph="What would you like to ask?" kind="area" w="100%" required />
        <div style={sx("display:flex")}><Cbtn label="Send message" icon="send-plane" kind="primary" size="lg" type="submit" full /><SentNote style={note} /></div>
        <div style={sx("margin-top:24px")}><PhotoCard photo="office-documents.jpg" pos="center 30%" card={<Tagged tag="Campus team"><ThreadCard w={326} /></Tagged>} /></div>
      </form>
      <MEnd />
    </>
  );
}

export default function Contact() {
  return <SitePage desktop={<Desktop />} phone={<Phone />} />;
}

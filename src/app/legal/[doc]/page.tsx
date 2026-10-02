import type { Metadata } from "next";
import { SitePage, Gap } from "@/components/page";
import { NavBar, PhoneFooter, PhoneNav, SiteFooter } from "@/components/chrome";
import { Wrap } from "@/components/sections";
import { H1, MGap, PEyebrow, Pad } from "@/components/phone";
import { A, Eyebrow, Ic, NavIcon, sx } from "@/components/ds";
import { SW } from "@/content/copy";
import { LEGAL_HREF } from "@/content/links";
import { BLUE, GAP, INK, INK2, LINE, MUTED, MX, PLATE, PX, SANS } from "@/lib/design";

const DOCS: Record<string, string> = { privacy: "privacy", "data-ownership": "data", terms: "terms" };
type Doc = { title: string; h: string; sections: [string, string][] };
const anchor = (t: string) => t.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "");

export const dynamicParams = false;
export const generateStaticParams = () => Object.keys(DOCS).map((doc) => ({ doc }));

export async function generateMetadata({ params }: { params: Promise<{ doc: string }> }): Promise<Metadata> {
  const L: Doc = SW.LEGAL[DOCS[(await params).doc]];
  return { title: L.title, description: L.h };
}

/** webpages.legal_secs */
function Desktop({ k }: { k: string }) {
  const L: Doc = SW.LEGAL[k];
  const others = Object.entries(SW.LEGAL as Record<string, Doc>).filter(([o]) => o !== k);
  return (
    <>
      <NavBar />
      <Wrap pad={`88px ${PX} 0`}>
        <div style={sx(`display:flex;flex-direction:column;gap:20px;padding-bottom:48px;border-bottom:1px solid ${LINE}`)}>
          <Eyebrow t={L.title} k={k} />
          <h1 style={sx(`margin:0;font:600 56px/1.05 ${SANS};letter-spacing:-0.04em;text-wrap:balance`)}>{L.h}</h1>
          <div style={sx(`font:400 15px ${SANS};color:${MUTED}`)}>{SW.LEGAL_UPDATED}</div>
        </div>
      </Wrap>
      <Wrap>
        <div style={sx("display:flex;gap:96px;padding-top:56px")}>
          <nav aria-label="On this page" style={sx("width:280px;flex:none")}>
            {L.sections.map(([t], i) => (
              <A key={t} href={`#${anchor(t)}`} style={`display:block;padding:9px 0 9px 14px;border-left:2px solid ${i === 0 ? BLUE : LINE};font:${i === 0 ? "500" : "400"} 14.5px ${SANS};color:${i === 0 ? INK : MUTED}`}>{t}</A>
            ))}
          </nav>
          <div style={sx("flex:1;max-width:640px")}>
            {L.sections.map(([t, p], i) => (
              <div key={t} id={anchor(t)} style={sx(`padding:${i === 0 ? 0 : 40}px 0 0`)}>
                <h3 style={sx(`margin:0;font:600 24px/1.2 ${SANS};letter-spacing:-0.015em`)}>{t}</h3>
                <p style={sx(`margin:12px 0 0;font:400 18px/1.65 ${SANS};color:${INK2}`)}>{p}</p>
              </div>
            ))}
            <div style={sx("display:flex;gap:20px;margin-top:64px")}>
              {others.map(([o, v]) => (
                <A key={o} href={LEGAL_HREF[o]} style={`flex:1;display:flex;align-items:center;gap:14px;padding:20px 22px;border-radius:20px;background:${PLATE}`}>
                  <NavIcon k={o} s={40} /><span style={sx(`font:600 18px ${SANS};flex:1`)}>{v.title}</span><Ic n="arrow-right-line" s={16} c={BLUE} />
                </A>
              ))}
            </div>
          </div>
        </div>
      </Wrap>
      <Gap h={GAP} />
      <SiteFooter />
    </>
  );
}

/** mobile.legal */
function Phone({ k }: { k: string }) {
  const L: Doc = SW.LEGAL[k];
  const others = Object.entries(SW.LEGAL as Record<string, Doc>).filter(([o]) => o !== k);
  return (
    <>
      <PhoneNav />
      <section style={sx(`padding:36px ${MX}px 28px;border-bottom:1px solid ${LINE};margin:0 0 0;display:flex;flex-direction:column;gap:14px`)}>
        <PEyebrow t={L.title} k={k} /><H1 t={L.h} />
        <div style={sx(`font:400 14px ${SANS};color:${MUTED}`)}>{SW.LEGAL_UPDATED}</div>
      </section>
      <MGap h={32} />
      <Pad>
        {L.sections.map(([t, p], i) => (
          <div key={t} style={sx(`padding-top:${i ? 28 : 0}px`)}>
            <h3 style={sx(`margin:0;font:600 21px/1.25 ${SANS};letter-spacing:-0.015em`)}>{t}</h3>
            <p style={sx(`margin:10px 0 0;font:400 16.5px/1.65 ${SANS};color:${INK2}`)}>{p}</p>
          </div>
        ))}
        <div style={sx("display:flex;flex-direction:column;gap:12px;margin-top:48px")}>
          {others.map(([o, v]) => (
            <A key={o} href={LEGAL_HREF[o]} style={`display:flex;align-items:center;gap:12px;padding:16px 18px;border-radius:18px;background:${PLATE}`}>
              <NavIcon k={o} s={34} /><span style={sx(`font:600 16px ${SANS};flex:1`)}>{v.title}</span><Ic n="arrow-right-line" s={16} c={BLUE} />
            </A>
          ))}
        </div>
      </Pad>
      <MGap />
      <PhoneFooter />
    </>
  );
}

export default async function Legal({ params }: { params: Promise<{ doc: string }> }) {
  const k = DOCS[(await params).doc];
  return <SitePage desktop={<Desktop k={k} />} phone={<Phone k={k} />} />;
}

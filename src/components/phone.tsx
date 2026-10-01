/**
 * The phone layout (design/source/mobile.py): one column, text first, then one picture; cards at their own size over
 * the photo's lower edge; sections 96px apart. At 390 this is the design to the pixel; up to 1023 the column widens
 * to 560 (see SitePage).
 */
import type { ReactNode } from "react";
import { A, Cbtn, CtaScene, DeptArt, Explore, Ic, NavIcon, Ph, PortalIcon, PortalScene, Scaled, Tagged, Ticks, btnStyle, sx } from "./ds";
import { PhoneEyebrow, PhoneFooter } from "./chrome";
import { Steps } from "./sections";
import { CP, CTAS } from "@/content/copy";
import { ACTION_HREF, deptHref, roleHref } from "@/content/links";
import { BLUE, CW, DOTS, INK2, LINE, MGAP, MUTED, MX, PLATE, SANS, pyRound } from "@/lib/design";

const href = (label: string) => ACTION_HREF[label];
export const PEyebrow = PhoneEyebrow;

// ---- type ------------------------------------------------------------------------------------------------
export const H1 = ({ t }: { t: ReactNode }) => <h1 style={sx(`margin:0;font:600 36px/1.08 ${SANS};letter-spacing:-0.035em;text-wrap:balance`)}>{t}</h1>;
export const H2 = ({ t, size = 30 }: { t: ReactNode; size?: number }) => <h2 style={sx(`margin:0;font:600 ${size}px/1.12 ${SANS};letter-spacing:-0.03em;text-wrap:balance`)}>{t}</h2>;
export const P = ({ t, size = 16.5, c = INK2 }: { t: ReactNode; size?: number; c?: string }) => <p style={sx(`margin:0;font:400 ${size}px/1.55 ${SANS};color:${c}`)}>{t}</p>;

/** mobile.btn_full: a large button across the column */
export const BtnFull = ({ label, icon = "calendar", kind = "primary", to }: { label: string; icon?: string; kind?: "primary" | "secondary"; to?: string }) =>
  <div style={sx("display:flex")}><Cbtn label={label} icon={icon} kind={kind} size="lg" href={to ?? href(label)} full /></div>;

/** mobile.head: eyebrow and headline */
export const MHead = ({ eye, k, h, mb = 28 }: { eye: ReactNode; k?: string | null; h: ReactNode; mb?: number }) =>
  <div style={sx(`display:flex;flex-direction:column;gap:12px;margin-bottom:${mb}px`)}><PEyebrow t={eye} k={k} /><H2 t={h} /></div>;

// ---- frame -------------------------------------------------------------------------------------------------
export const MGap = ({ h = MGAP }: { h?: number }) => <div style={sx(`height:${h}px`)} />;
export const Pad = ({ p = `0 ${MX}px`, children }: { p?: string; children: ReactNode }) => <div style={sx(`padding:${p}`)}>{children}</div>;

/** mobile.scale_to: a desktop picture fitted to the column */
export const ScaleTo = ({ w, h, tw = CW, children }: { w: number; h: number; tw?: number; children: ReactNode }) => {
  const k = tw / w;
  return <Scaled w={tw} h={pyRound(h * k)} k={k}>{children}</Scaled>;
};

// ---- pictures ------------------------------------------------------------------------------------------------
/** mobile.photo_card: the photograph, then a card over its lower edge at the card's own size */
export const PhotoCard = ({ photo, pos, card, h = 240 }: { photo: string; pos: string; card?: ReactNode; h?: number }) => (
  <div>
    <Ph n={photo} w={CW} h={h} pos={pos} r={20} />
    {card ? <div style={sx("margin:-64px 12px 0;position:relative;z-index:2")}>{card}</div> : null}
  </div>
);

/** mobile.plate_card: a card on the dotted plate, the department's drawing below it */
export const PlateCard = ({ card, art }: { card: ReactNode; art?: string | null }) => (
  <div style={sx(`border-radius:24px;${DOTS};box-shadow:inset 0 0 0 1px #eceef2;padding:24px 20px ${art ? 0 : 24}px;overflow:hidden;display:flex;flex-direction:column;align-items:center`)}>
    <div style={sx("position:relative;z-index:2")}>{card}</div>
    {art ? <div style={sx("display:flex;justify-content:flex-end;margin:-30px -20px -10px 0")}><DeptArt k={art} w={300} h={200} U={40} /></div> : null}
  </div>
);

/** mobile.phone_on: a phone mock standing over a photograph */
export const PhoneOn = ({ phone, photo, pos, h = 520 }: { phone: ReactNode; photo: string; pos: string; h?: number }) => (
  <div style={sx(`position:relative;width:${CW}px;height:${h}px;border-radius:24px;overflow:hidden`)}>
    <div style={sx("position:absolute;inset:0")}><Ph n={photo} w={CW} h={h} pos={pos} r={24} /></div>
    <div style={sx("position:absolute;left:0;right:0;top:24px;display:flex;justify-content:center")}>{phone}</div>
  </div>
);

// ---- sections ----------------------------------------------------------------------------------------------
/** mobile.hero */
export function MHero({ eye, k, h, b, pic, buttons, eyeNode }: { eye?: ReactNode; k?: string | null; h: ReactNode; b: ReactNode; pic?: ReactNode; buttons?: ReactNode; eyeNode?: ReactNode }) {
  return (
    <section style={sx(`padding:36px ${MX}px 0;display:flex;flex-direction:column;gap:18px`)}>
      {eyeNode ?? (eye ? <PEyebrow t={eye} k={k} /> : null)}
      <H1 t={h} /><P t={b} size={17} />
      {buttons ?? <BtnFull label="Book a demo" />}
      {pic ? <div style={sx("margin-top:14px")}>{pic}</div> : null}
    </section>
  );
}

/** mobile.row */
export const MRow = ({ eye, k, h, b, pic }: { eye: ReactNode; k?: string | null; h: ReactNode; b: ReactNode; pic: ReactNode }) => (
  <Pad><div style={sx("display:flex;flex-direction:column;gap:14px")}><PEyebrow t={eye} k={k} /><H2 t={h} /><P t={b} /><div style={sx("margin-top:14px")}>{pic}</div></div></Pad>
);

/** mobile.rows: a section apart */
export const MRows = ({ items }: { items: { eye: ReactNode; k?: string | null; h: ReactNode; b: ReactNode; pic: ReactNode }[] }) =>
  <>{items.map((it, i) => <FragmentRow key={i} first={i === 0} {...it} />)}</>;
const FragmentRow = ({ first, ...it }: { first: boolean; eye: ReactNode; k?: string | null; h: ReactNode; b: ReactNode; pic: ReactNode }) => <>{first ? null : <MGap />}<MRow {...it} /></>;

/** mobile.band: a grey band with a photograph */
export const MBand = ({ eye, k, h, b, photo, pos }: { eye: ReactNode; k: string; h: ReactNode; b: ReactNode; photo: string; pos: string }) => (
  <section style={sx(`background:${PLATE};padding:64px ${MX}px;display:flex;flex-direction:column;gap:14px`)}>
    <PEyebrow t={eye} k={k} /><H2 t={h} /><P t={b} />
    <div style={sx("margin-top:14px")}><Ph n={photo} w={CW} h={240} pos={pos} r={20} /></div>
  </section>
);

type Dept = [string, string, string, string, string];

/** mobile.dtile */
export function DTile({ d }: { d: Dept }) {
  const [n, sl, desc, , k] = d;
  return (
    <A href={deptHref(sl)} style={`position:relative;height:264px;border-radius:22px;background:${PLATE};overflow:hidden;padding:24px 22px 0;box-sizing:border-box;display:block`}>
      <div style={sx(`font:600 24px/1.15 ${SANS};letter-spacing:-0.02em;max-width:280px;text-wrap:balance`)}>{n}</div>
      <div style={sx(`font:400 14.5px/1.5 ${SANS};color:${INK2};margin-top:8px;max-width:290px`)}>{desc}</div>
      <div style={sx("position:absolute;left:22px;bottom:22px")}><Explore /></div>
      <div style={sx("position:absolute;right:-30px;bottom:-34px")}><DeptArt k={k} w={236} h={160} U={30} /></div>
    </A>
  );
}

/** mobile.tiles */
export const MTiles = ({ slugs }: { slugs: string[] }) => (
  <div style={sx("display:flex;flex-direction:column;gap:14px")}>{slugs.map((s) => <DTile key={s} d={(CP.DEPARTMENTS as Dept[]).find((d) => d[1] === s)!} />)}</div>
);

/** mobile.tools */
export const MTools = ({ title, items }: { title: ReactNode; items: string[] }) => (
  <Pad>
    <MHead eye="Features" k="included" h={title} mb={18} />
    {items.map((x) => <div key={x} style={sx(`display:flex;align-items:center;gap:10px;padding:13px 0;border-top:1px solid ${LINE};font:500 15.5px ${SANS}`)}><Ic n="check-circle" s={16} c={BLUE} />{x}</div>)}
  </Pad>
);

/** mobile.faq: an accordion, the first question open */
export function MFaq({ eye, k, h, qa }: { eye: ReactNode; k: string; h: ReactNode; qa: [string, string][] }) {
  return (
    <Pad>
      <MHead eye={eye} k={k} h={h} mb={14} />
      {qa.map(([q, a], i) => (
        <details key={q} className="faq" open={i === 0} style={sx(`padding:18px 0;border-top:1px solid ${LINE}`)}>
          <summary style={sx(`display:flex;justify-content:space-between;gap:12px;font:600 16.5px/1.35 ${SANS}`)}>{q}<Ic n="down-line" s={18} c={MUTED} /></summary>
          <div style={sx(`font:400 15px/1.6 ${SANS};color:${INK2};margin-top:8px`)}>{a}</div>
        </details>
      ))}
      <div style={sx(`border-top:1px solid ${LINE}`)} />
    </Pad>
  );
}

/** mobile.cta: the call to action with its drawing */
export function MCta({ kind = "visit" }: { kind?: "visit" | "price" | "training" }) {
  const [h, b, btns] = CTAS[kind];
  const second = btns[1];
  return (
    <Pad>
      <div style={sx(`border-radius:24px;background:${PLATE};padding:12px 12px 26px`)}>
        <div style={sx(`border-radius:18px;overflow:hidden;${DOTS};box-shadow:inset 0 0 0 1px #e3e6eb`)}>
          <Scaled w={326} h={245} k={326 / 560}><CtaScene k={kind} w={560} h={420} U={40} cx={280} cy={250} /></Scaled>
        </div>
        <div style={sx("padding:20px 10px 0;display:flex;flex-direction:column;gap:14px")}>
          <H2 t={h} size={28} /><P t={b} size={16} />
          <BtnFull label={btns[0][0]} icon={btns[0][1]} />
          {second ? <BtnFull label={second[0]} icon={second[1]} kind="secondary" /> : null}
        </div>
      </div>
    </Pad>
  );
}

/** mobile.end: the call to action and the footer */
export const MEnd = ({ kind = "visit" }: { kind?: "visit" | "price" | "training" }) => <><MGap /><MCta kind={kind} /><MGap /><PhoneFooter /></>;

/** mobile.role_tile */
export function MRoleTile({ r }: { r: [string, string, string, string] }) {
  const [n, p, d, k] = r;
  return (
    <A href={roleHref(n)} style={`position:relative;height:300px;border-radius:22px;background:${PLATE};overflow:hidden;padding:22px 22px 0;box-sizing:border-box;display:block`}>
      <div style={sx(`display:inline-flex;align-items:center;gap:6px;height:26px;padding:0 10px 0 4px;border-radius:13px;background:#fff;box-shadow:inset 0 0 0 1px ${LINE};font:500 12px ${SANS};color:${INK2}`)}>
        <PortalIcon n={p} s={18} />{p} portal
      </div>
      <div style={sx(`font:600 24px/1.15 ${SANS};letter-spacing:-0.02em;margin-top:14px`)}>{n}</div>
      <div style={sx(`font:400 14.5px/1.5 ${SANS};color:${INK2};margin-top:8px;max-width:290px`)}>{d}</div>
      <div style={sx("position:absolute;left:22px;bottom:22px")}><Explore /></div>
      <div style={sx("position:absolute;right:-30px;bottom:-34px")}>
        {k === "pupils" ? <PortalScene n="Student" w={270} h={186} U={25} cx={140} cy={115} labels={false} /> : <DeptArt k={k} w={270} h={186} U={34} />}
      </div>
    </A>
  );
}

/** mobile.moving_band */
export function MovingBand() {
  const S = CP.SWITCH;
  return (
    <section style={sx(`background:${PLATE};padding:64px ${MX}px;display:flex;flex-direction:column;gap:14px`)}>
      <PEyebrow t={S.eyebrow} k="moving" /><H2 t={S.h_home} /><P t={S.b} />
      <div style={sx("display:flex;flex-wrap:wrap;gap:8px")}>
        {(S.moves as string[]).map((m) => <span key={m} style={sx(`display:inline-flex;align-items:center;height:30px;padding:0 12px;border-radius:15px;background:#fff;box-shadow:inset 0 0 0 1px ${LINE};font:500 13px ${SANS};color:${INK2}`)}>{m}</span>)}
      </div>
      <div style={sx(`margin-top:12px;border-radius:22px;background:#fff;box-shadow:0 0 0 1px ${LINE};padding:24px 20px`)}><Steps items={S.steps} w={310} /></div>
      <div><Explore t="How we move your records" href={href("How we move your records")} /></div>
    </section>
  );
}

/** mobile.price_band */
export function MPriceBand() {
  const P_ = CP.PRICING;
  return (
    <Pad>
      <div style={sx("display:flex;flex-direction:column;gap:14px")}>
        <PEyebrow t="Pricing" k="pricing" /><H2 t={P_.h} /><P t={P_.b} />
        <div><Ticks items={["Setup, data capture and training free", "First month free", "Every department and portal included"]} size={15} /></div>
        <div style={sx("margin-top:6px")}><Ph n="girl-beret.jpg" w={CW} h={300} pos="center 20%" r={20} /></div>
        <BtnFull label="See pricing" icon="arrow-right-line" kind="secondary" />
      </div>
    </Pad>
  );
}

export { Tagged, NavIcon, btnStyle, MUTED };

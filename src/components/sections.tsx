/**
 * Desktop sections, ported from design/source/pages.py, webpages.py and ds.py. Section components keep the names of
 * the functions they port. Gutters are fluid above 1440 (PX); everything else is the design's value.
 */
import { Fragment, type ReactNode } from "react";
import { A, At, BrandLogo, Card, Cbtn, CtaScene, DeptArt, Eyebrow, Explore, Fig, H2, Head, Ic, Lab, LogoOf, NavIcon, OnPlate, Para, Ph, PhotoStory, Pmark, PortalIcon, PortalScene, SchoolsCampus, Tagged, Ticks, sx } from "./ds";
import { AttCard, NoteCard, RegisterCard } from "./cards";
import { MarkJourney } from "./mark-journey";
import { Lockup, TYPE_PHOTO } from "./chrome";
import { CP, CTAS } from "@/content/copy";
import { ACTION_HREF, deptHref, roleHref, typeHref } from "@/content/links";
import { BLUE, DOTS, FAINT, GAP, INK, INK2, LINE, MONO, MUTED, OK, PLATE, PX, PX80, SANS } from "@/lib/design";

const href = (label: string) => ACTION_HREF[label];

// ---- frame -------------------------------------------------------------------------------------------------
/** pages.band: a full-width section */
export const Band = ({ bg = "#fff", pad = `${GAP}px ${PX}`, children }: { bg?: string; pad?: string; children: ReactNode }) =>
  <section style={sx(`background:${bg};padding:${pad}`)}>{children}</section>;

/** webpages.wrap: the content column */
export const Wrap = ({ pad = `0 ${PX}`, children, id }: { pad?: string; children: ReactNode; id?: string }) => <div id={id} style={sx(`padding:${pad}`)}>{children}</div>;

/** webpages.sec_head: eyebrow and headline */
export const SecHead = ({ eye, k, h, size = 46, w = 820, mb = 44 }: { eye: ReactNode; k: string; h: ReactNode; size?: number; w?: number; mb?: number }) => (
  <div style={sx(`display:flex;flex-direction:column;gap:16px;margin-bottom:${mb}px`)}><Eyebrow t={eye} k={k} /><Head t={h} size={size} w={w} /></div>
);

// ---- rows ------------------------------------------------------------------------------------------------
export const ROW_ICON: Record<string, string> = {
  "Single record": "record", "Works without internet": "nointernet", Integrations: "integrations", "Training and support": "training",
  "Data and security": "security", Registers: "academics", "Marks and reports": "record", Timetables: "calendar-t", "Family communication": "communication",
};

/** pages.row / webpages.row: eyebrow, a verb-led headline, a paragraph; the picture beside it */
export function Row({ eye, k, h, b, pic, flip = false, extra }: { eye: ReactNode; k?: string | null; h: ReactNode; b: ReactNode; pic: ReactNode; flip?: boolean; extra?: ReactNode }) {
  const txt = (
    <div style={sx("flex:1;display:flex;flex-direction:column;gap:18px;justify-content:center;max-width:500px")}>
      <Eyebrow t={eye} k={k} /><Head t={h} size={42} w={500} /><Para t={b} size={18} c={INK2} mw={480} />{extra}
    </div>
  );
  const p = <div style={sx("flex:none")}>{pic}</div>;
  return <div style={sx("display:flex;gap:96px;align-items:center;justify-content:space-between")}>{flip ? <>{p}{txt}</> : <>{txt}{p}</>}</div>;
}

/** rows, alternating sides, a section apart */
export const Rows = ({ items }: { items: { eye: ReactNode; k?: string | null; h: ReactNode; b: ReactNode; pic: ReactNode; extra?: ReactNode }[] }) => (
  <>{items.map((it, i) => <div key={i} style={sx(`margin-top:${i === 0 ? 0 : GAP}px`)}><Row {...it} flip={i % 2 === 1} /></div>)}</>
);

// ---- row pictures (pages.py) -----------------------------------------------------------------------------
/** pages.pic_offline: the register, saved on the tablet, on the classroom photo */
export const PicOffline = ({ w = 620, h = 420 }: { w?: number; h?: number }) =>
  <PhotoStory n="classroom-zambia.jpg" pos="center 40%" cards={[[0, 60, <RegisterCard key="r" w={300} offline />]]} w={w} h={h} />;

/** pages.pic_integrations: the record and the three links */
export function PicIntegrations({ w = 620, h = 420 }: { w?: number; h?: number }) {
  const items: [ReactNode, string, string][] = [
    [<LogoOf key="s" r="simple-icons:sage" s={30} c="#00D639" />, "Sage Pastel", "Journals, the ledger"],
    [<LogoOf key="q" r="simple-icons:quickbooks" s={30} c="#2CA01C" />, "QuickBooks", "Invoices, payments"],
    [<BrandLogo key="z" n="ZIMRA" s={30} />, "ZIMRA fiscalisation", "Fiscal receipts (FDMS)"],
  ];
  const ys = [58, 175, 292];
  return (
    <OnPlate w={w} h={h}>
      <span style={sx("position:absolute;left:248px;top:210px;width:46px;height:1.5px;background:#9aa1ad")} />
      <span style={sx("position:absolute;left:294px;top:94px;width:1.5px;height:234px;background:#9aa1ad")} />
      {ys.map((y) => (
        <Fragment key={y}>
          <span style={sx(`position:absolute;left:294px;top:${y + 36}px;width:46px;height:1.5px;background:#9aa1ad`)} />
          <span style={sx(`position:absolute;left:336px;top:${y + 33}px;width:7px;height:7px;border-radius:4px;background:#fff;border:1.5px solid ${INK};box-sizing:border-box`)} />
        </Fragment>
      ))}
      <div style={sx(`position:absolute;left:48px;top:140px;width:200px;height:140px;border-radius:20px;background:#fff;box-shadow:0 0 0 1px ${LINE},0 18px 30px -20px rgba(11,12,20,.35);display:flex;flex-direction:column;justify-content:center;align-items:flex-start;gap:14px;padding:0 24px;box-sizing:border-box`)}>
        <Lockup h={24} by={false} />
        <div style={sx(`font:400 13px ${SANS};color:${MUTED}`)}>One record per pupil</div>
      </div>
      {items.map(([lg, n, d], i) => (
        <div key={n} style={sx(`position:absolute;left:340px;top:${ys[i]}px;width:240px;height:72px;border-radius:16px;background:#fff;box-shadow:0 0 0 1px ${LINE},0 14px 24px -18px rgba(11,12,20,.3);display:flex;align-items:center;gap:12px;padding:0 16px;box-sizing:border-box`)}>
          {lg}<div><div style={sx(`font:600 15px ${SANS}`)}>{n}</div><div style={sx(`font:400 12.5px ${SANS};color:${MUTED};margin-top:2px`)}>{d}</div></div>
        </div>
      ))}
    </OnPlate>
  );
}

/** pages.pic_training: the staffroom being trained */
export const PicTraining = ({ w = 620, h = 420 }: { w?: number; h?: number }) =>
  <OnPlate w={w} h={h}><div style={sx("position:absolute;left:10px;top:0")}><CtaScene k="training" w={600} h={430} U={46} cx={300} cy={262} /></div></OnPlate>;

/** pages.pic_security: who sees what, the backup and the export */
export function PicSecurity({ w = 620, h = 420 }: { w?: number; h?: number }) {
  const rows = [["Mrs Ncube", "Bursar", "Fees, payroll, the books"], ["Ms Sibanda", "Class teacher", "Form 3B registers and marks"], ["Rudo Moyo", "Guardian", "Tanaka only"], ["Mr Dube", "Head", "Every department"]];
  return (
    <OnPlate w={w} h={h}>
      <div style={sx(`position:absolute;left:60px;top:44px;width:420px;border-radius:18px;background:#fff;box-shadow:0 0 0 1px ${LINE},0 18px 30px -20px rgba(11,12,20,.35);padding:16px 18px 6px;box-sizing:border-box`)}>
        <div style={sx("display:flex;align-items:center;gap:10px;margin-bottom:10px")}>
          <Pmark s={28} r={8} /><div style={sx(`font:600 15px ${SANS}`)}>Who sees what</div><span style={sx("flex:1")} />
          <span style={sx(`font:400 12px ${MONO};color:${MUTED}`)}>Mukuvisi High</span>
        </div>
        {rows.map(([n, role, acc]) => (
          <div key={n} style={sx(`display:flex;align-items:center;gap:12px;padding:11px 0;border-top:1px solid ${LINE}`)}>
            <div style={sx("flex:1")}><div style={sx(`font:600 14px ${SANS}`)}>{n}</div><div style={sx(`font:400 12.5px ${SANS};color:${MUTED}`)}>{role}</div></div>
            <div style={sx(`font:400 13px ${SANS};color:${INK2};width:170px`)}>{acc}</div>
          </div>
        ))}
      </div>
      <div style={sx("position:absolute;left:300px;top:322px;display:flex;flex-direction:column;gap:8px")}>
        <span style={sx(`display:inline-flex;align-items:center;gap:8px;height:34px;padding:0 14px 0 10px;border-radius:17px;background:#fff;box-shadow:0 0 0 1px ${LINE};font:500 13px ${SANS}`)}><Ic n="safe-lock" s={15} c={OK} />Backed up at 02:00 today</span>
        <span style={sx(`display:inline-flex;align-items:center;gap:8px;height:34px;padding:0 14px 0 10px;border-radius:17px;background:#fff;box-shadow:0 0 0 1px ${LINE};font:500 13px ${SANS}`)}><Ic n="download-2" s={15} c={BLUE} />Export everything (.zip)</span>
      </div>
    </OnPlate>
  );
}

// ---- heroes ------------------------------------------------------------------------------------------------
/** hero.hero_picture: the wide photograph and three cards, each tagged with its portal */
export function HeroPicture({ w = 1200, h = 620 }: { w?: number; h?: number }) {
  return (
    <div style={sx(`position:relative;width:${w}px;height:${h}px;flex:none`)}>
      <div style={sx("position:absolute;left:90px;top:30px")}><Ph n="boys-reading-2.jpg" w={w - 180} h={h - 30} pos="47% 42%" r={24} /></div>
      <At x={0} y={150} z={3}><Tagged tag="Teacher portal"><RegisterCard w={300} offline /></Tagged></At>
      <At x={w - 250} y={0} z={2}><Tagged tag="Administration portal"><AttCard w={250} /></Tagged></At>
      <At x={w - 360} y={h - 150} z={4}><Tagged tag="Parent portal"><NoteCard w={360} /></Tagged></At>
    </div>
  );
}

/** pages.hero: Home's centred type over the wide photograph */
export function HomeHero() {
  const H = CP.HERO;
  return (
    <section>
      <div style={sx(`display:flex;flex-direction:column;align-items:center;text-align:center;gap:24px;padding:88px ${PX} 0`)}>
        <h1 style={sx(`margin:0;font:600 64px/1.04 ${SANS};letter-spacing:-0.04em;max-width:960px;text-wrap:balance`)}>{H.h1a}</h1>
        <Para t={H.body} size={20} c={INK2} mw={640} centre />
        <div style={sx("display:flex;gap:12px;margin-top:6px")}>
          <Cbtn label={H.cta} icon="calendar" kind="primary" size="lg" href={href(H.cta)} />
          <Cbtn label={H.cta2} icon="arrow-down-line" kind="secondary" size="lg" href={href(H.cta2)} />
        </div>
        <div style={sx("display:flex;gap:22px")}>
          {["Setup and training free", "First month free", "US$1 per active pupil per month"].map((t) => (
            <span key={t} style={sx(`display:inline-flex;align-items:center;gap:7px;font:500 14.5px ${SANS};color:${INK2}`)}><Ic n="check-circle" s={15} c={OK} />{t}</span>
          ))}
        </div>
      </div>
      <div style={sx(`display:flex;justify-content:center;padding:56px ${PX} 0`)}><HeroPicture /></div>
    </section>
  );
}

/** pages.page_hero: centred type, the picture below at full column width */
export function PageHero({ eye, k, h, b, buttons, pic, eyeNode }: { eye?: ReactNode; k?: string | null; h: ReactNode; b: ReactNode; buttons?: ReactNode; pic?: ReactNode; eyeNode?: ReactNode }) {
  return (
    <section>
      <div style={sx(`display:flex;flex-direction:column;align-items:center;text-align:center;gap:22px;padding:88px ${PX} 0`)}>
        {eyeNode ?? <Eyebrow t={eye} k={k} />}
        <h1 style={sx(`margin:0;font:600 60px/1.05 ${SANS};letter-spacing:-0.04em;max-width:900px;text-wrap:balance`)}>{h}</h1>
        <Para t={b} size={20} c={INK2} mw={640} centre />
        <div style={sx("display:flex;gap:12px;margin-top:6px")}>{buttons}</div>
      </div>
      <div style={sx(`display:flex;justify-content:center;padding:56px ${PX} 0`)}>{pic}</div>
    </section>
  );
}

/** webpages.demo_btns */
export const DemoBtns = ({ price = false }: { price?: boolean }) => (
  <>
    <Cbtn label="Book a demo" icon="calendar" kind="primary" size="lg" href={href("Book a demo")} />
    {price ? <Cbtn label="Download the price sheet (PDF)" icon="download-2" kind="secondary" size="lg" href={href("Download the price sheet (PDF)")} /> : null}
  </>
);

// ---- tiles --------------------------------------------------------------------------------------------------
type Dept = [string, string, string, string, string];

/** pages.dept_tile: grey tile, name big, one line, the department drawn in the corner */
export function DeptTile({ d, w = 389, h = 400 }: { d: Dept; w?: number; h?: number }) {
  const [n, sl, desc, , k] = d;
  return (
    <A href={deptHref(sl)} style={`position:relative;width:${w}px;height:${h}px;border-radius:24px;background:${PLATE};overflow:hidden;box-sizing:border-box;padding:28px 28px 0;display:block`}>
      <div style={sx(`font:600 28px/1.12 ${SANS};letter-spacing:-0.025em;max-width:300px`)}>{n}</div>
      <div style={sx(`font:400 15px/1.5 ${SANS};color:${INK2};margin-top:10px;max-width:320px`)}>{desc}</div>
      <div style={sx("position:absolute;left:28px;bottom:26px")}><Explore /></div>
      <div style={sx("position:absolute;right:-26px;bottom:-30px")}><DeptArt k={k} w={330} h={228} U={42} /></div>
    </A>
  );
}

/** pages.departments: Home's department grid */
export function Departments() {
  const [a] = CP.DEPTS_H;
  return (
    <Band>
      <div id="departments" style={sx("display:flex;flex-direction:column;gap:16px;margin-bottom:48px")}><Eyebrow t="Solutions" k="solutions" /><Head t={a} size={52} w={640} /></div>
      <div style={sx("display:grid;grid-template-columns:repeat(3,389px);gap:24px")}>{(CP.DEPARTMENTS as Dept[]).map((d) => <DeptTile key={d[1]} d={d} />)}</div>
    </Band>
  );
}

/** webpages.tiles: departments by slug, 384 wide */
export const Tiles = ({ slugs, cols = 3 }: { slugs: string[]; cols?: number }) => (
  <div style={sx(`display:grid;grid-template-columns:repeat(${cols},384px);gap:24px;justify-content:space-between`)}>
    {slugs.map((s) => <DeptTile key={s} d={(CP.DEPARTMENTS as Dept[]).find((d) => d[1] === s)!} w={384} />)}
  </div>
);

/** pages.role_tile: a role set like a department tile, with its portal */
export function RoleTile({ r, w = 389, h = 400 }: { r: [string, string, string, string]; w?: number; h?: number }) {
  const [n, p, d, k] = r;
  return (
    <A href={roleHref(n)} style={`position:relative;width:${w}px;height:${h}px;border-radius:24px;background:${PLATE};overflow:hidden;box-sizing:border-box;padding:28px 28px 0;display:block`}>
      <div style={sx(`display:inline-flex;align-items:center;gap:6px;height:28px;padding:0 10px 0 4px;border-radius:14px;background:#fff;box-shadow:inset 0 0 0 1px ${LINE};font:500 12.5px ${SANS};color:${INK2}`)}>
        <PortalIcon n={p} s={20} />{p} portal
      </div>
      <div style={sx(`font:600 28px/1.12 ${SANS};letter-spacing:-0.025em;margin-top:16px;text-wrap:balance`)}>{n}</div>
      <div style={sx(`font:400 15px/1.5 ${SANS};color:${INK2};margin-top:10px;max-width:320px`)}>{d}</div>
      <div style={sx("position:absolute;left:28px;bottom:26px")}><Explore /></div>
      <div style={sx("position:absolute;right:-26px;bottom:-30px")}>
        {k === "pupils" ? <PortalScene n="Student" w={330} h={228} U={30} cx={175} cy={140} labels={false} /> : <DeptArt k={k} w={330} h={228} U={42} />}
      </div>
    </A>
  );
}

/** pages.roles: Home's role grid */
export const Roles = () => (
  <Band pad={`0 ${PX}`}>
    <div style={sx("display:flex;flex-direction:column;gap:16px;margin-bottom:48px")}><Eyebrow t="Who uses Campus" k="portals" /><Head t={CP.ROLES_H} size={52} w={640} /></div>
    <div style={sx("display:grid;grid-template-columns:repeat(3,389px);gap:24px")}>{(CP.ROLES as [string, string, string, string][]).map((r) => <RoleTile key={r[0]} r={r} />)}</div>
  </Band>
);

/** a kind of school, photographed, with its building as the icon (pages.who, webpages.who_secs) */
export const TypeCard = ({ t }: { t: [string, string, string] }) => {
  const [n, k, d] = t;
  return (
    <A href={typeHref(k)} style="width:232px;display:flex;flex-direction:column">
      <div style={sx("position:relative;width:232px;height:250px")}>
        <Ph n={TYPE_PHOTO[k][0]} w={232} h={250} pos={TYPE_PHOTO[k][1]} r={20} />
        <div style={sx("position:absolute;left:12px;bottom:12px;border-radius:12px;box-shadow:0 8px 18px -10px rgba(11,12,20,.5)")}><NavIcon k={k} s={44} /></div>
      </div>
      <div style={sx(`font:600 19px ${SANS};margin-top:16px`)}>{n}</div>
      <div style={sx(`font:400 14.5px/1.5 ${SANS};color:${INK2};margin-top:6px`)}>{d}</div>
      <div style={sx("margin-top:auto;padding-top:16px")}><Explore /></div>
    </A>
  );
};

// ---- bands ---------------------------------------------------------------------------------------------------
/** pages.focus: K-12, with the five kinds of school on one plate */
export function Focus() {
  const [h, b] = CP.FOCUS;
  return (
    <div style={sx(`padding:0 ${PX80}`)}>
      <div style={sx(`display:flex;align-items:center;gap:48px;border-radius:32px;background:${PLATE};padding:24px 24px 24px 64px`)}>
        <div style={sx("flex:1;display:flex;flex-direction:column;gap:20px")}>
          <Eyebrow t="Who we serve · K-12" k="who" /><Head t={h} size={44} w={560} /><Para t={b} size={18} c={INK2} mw={520} />
          <div style={sx("display:flex;gap:12px;margin-top:6px")}>
            <Cbtn label="Book a demo" icon="calendar" kind="primary" size="lg" href={href("Book a demo")} />
            <Cbtn label="See who we serve" icon="arrow-right-line" kind="secondary" size="lg" href={href("See who we serve")} />
          </div>
        </div>
        <div style={sx("flex:none;border-radius:24px;overflow:hidden")}><OnPlate w={600} h={420}><SchoolsCampus w={600} h={420} /></OnPlate></div>
      </div>
    </div>
  );
}

/** pages.steps: the four weeks, numbered on a line */
export function Steps({ items, w = 600 }: { items: [string, string, string][]; w?: number }) {
  return <>{items.map(([wk, t, d], i) => {
    const last = i === items.length - 1;
    return (
      <div key={t} style={sx(`position:relative;display:flex;gap:20px;padding-bottom:${last ? 0 : 26}px`)}>
        {last ? null : <span style={sx("position:absolute;left:19px;top:40px;bottom:0;width:1.5px;background:#c3c9d3")} />}
        <span style={sx(`width:40px;height:40px;border-radius:20px;background:${last ? BLUE : "#fff"};box-shadow:inset 0 0 0 1.5px ${BLUE};display:flex;align-items:center;justify-content:center;font:600 15px ${SANS};color:${last ? "#fff" : BLUE};flex:none`)}>{i + 1}</span>
        <div style={sx("padding-top:2px")}>
          <div style={sx("display:flex;gap:10px;align-items:baseline")}><span style={sx(`font:600 18px ${SANS}`)}>{t}</span><span style={sx(`font:400 13px ${MONO};color:${MUTED}`)}>{wk}</span></div>
          <div style={sx(`font:400 15px/1.55 ${SANS};color:${INK2};margin-top:4px;max-width:${w - 60}px`)}>{d}</div>
        </div>
      </div>
    );
  })}</>;
}

/** pages.switching: Moving from another system */
export function Switching() {
  const S = CP.SWITCH;
  return (
    <Band bg={PLATE}>
      <div style={sx("display:flex;justify-content:space-between;align-items:center")}>
        <div style={sx("width:520px;display:flex;flex-direction:column;gap:20px")}>
          <Eyebrow t={S.eyebrow} k="moving" /><Head t={S.h_home} size={46} w={520} /><Para t={S.b} size={18} c={INK2} mw={500} />
          <div style={sx("display:flex;flex-wrap:wrap;gap:8px;margin-top:4px")}>
            {(S.moves as string[]).map((m) => <span key={m} style={sx(`display:inline-flex;align-items:center;height:32px;padding:0 12px;border-radius:16px;background:#fff;box-shadow:inset 0 0 0 1px ${LINE};font:500 13.5px ${SANS};color:${INK2}`)}>{m}</span>)}
          </div>
          <div style={sx("margin-top:8px")}><Explore t="How we move your records" href={href("How we move your records")} /></div>
        </div>
        <div style={sx(`width:600px;border-radius:28px;background:#fff;box-shadow:0 0 0 1px ${LINE};padding:36px 36px 32px;box-sizing:border-box`)}><Steps items={S.steps} /></div>
      </div>
    </Band>
  );
}

/** pages.price_band: the price on Home */
export function PriceBand() {
  const P = CP.PRICING;
  return (
    <Band pad={`${GAP}px ${PX} 0`}>
      <div style={sx("display:flex;gap:96px;align-items:center;justify-content:space-between")}>
        <Ph n="seniors-lecture.jpg" w={620} h={440} pos="center 30%" r={24} />
        <div style={sx("flex:1;display:flex;flex-direction:column;gap:18px;max-width:500px")}>
          <Eyebrow t="Pricing" k="pricing" /><Head t={P.h} size={42} w={500} /><Para t={P.b} size={18} c={INK2} mw={480} />
          <div><Ticks items={["Setup, data capture and training free", "First month free", "Every department and portal included"]} /></div>
          <div><Cbtn label="See pricing" icon="arrow-right-line" kind="secondary" size="md" href={href("See pricing")} /></div>
        </div>
      </div>
    </Band>
  );
}

/** ds.cta_block: a call to action, drawn as what happens next */
export function CtaBlock({ kind }: { kind: "visit" | "price" | "training" }) {
  const [h, b, btns] = CTAS[kind];
  return (
    <div style={sx(`width:100%;box-sizing:border-box;display:flex;align-items:center;gap:48px;border-radius:32px;background:${PLATE};padding:24px 24px 24px 64px`)}>
      <div style={sx("flex:1;display:flex;flex-direction:column;gap:20px")}>
        <H2 a={h} size={44} /><Para t={b} size={18} c={INK2} mw={520} />
        <div style={sx("display:flex;gap:12px;flex-wrap:wrap;margin-top:6px")}>
          {btns.map(([t, i, k]) => <Cbtn key={t} label={t} icon={i} kind={k as "primary"} size="lg" href={href(t)} />)}
        </div>
      </div>
      <div style={sx(`width:600px;height:430px;border-radius:24px;overflow:hidden;${DOTS};box-shadow:inset 0 0 0 1px #e3e6eb;flex:none`)}>
        <CtaScene k={kind} w={600} h={430} U={42} cx={300} cy={255} />
      </div>
    </div>
  );
}

/** the call to action, 160 above and below, in the 80px gutter (webpages.footer_secs) */
export const CtaSection = ({ kind = "visit" }: { kind?: "visit" | "price" | "training" }) =>
  <div style={sx(`padding:${GAP}px ${PX80}`)}><CtaBlock kind={kind} /></div>;

/** webpages.split_band: a grey band, text and a photograph */
export function SplitBand({ eye, k, h, b, photo, pos }: { eye: ReactNode; k: string; h: ReactNode; b: ReactNode; photo: string; pos: string }) {
  return (
    <section style={sx(`background:${PLATE};padding:${GAP - 40}px ${PX}`)}>
      <div style={sx("display:flex;align-items:center;justify-content:space-between;gap:96px")}>
        <div style={sx("flex:1;display:flex;flex-direction:column;gap:20px;max-width:520px")}><Eyebrow t={eye} k={k} /><Head t={h} size={44} w={520} /><Para t={b} size={19} c={INK2} mw={500} /></div>
        <Ph n={photo} w={600} h={420} pos={pos} r={24} />
      </div>
    </section>
  );
}

/** webpages.tools: the features list */
export function Tools({ title, items }: { title: ReactNode; items: string[] }) {
  return (
    <Wrap>
      <div style={sx("display:flex;gap:96px")}>
        <div style={sx("width:420px")}><Eyebrow t="Features" k="included" /><div style={sx("margin-top:14px")}><Head t={title} size={40} w={420} /></div></div>
        <div style={sx("flex:1;display:grid;grid-template-columns:1fr 1fr;gap:0 48px")}>
          {items.map((x) => <div key={x} style={sx(`display:flex;align-items:center;gap:10px;padding:14px 0;border-top:1px solid ${LINE};font:500 16px ${SANS}`)}><Ic n="check-circle" s={16} c={BLUE} />{x}</div>)}
        </div>
      </div>
    </Wrap>
  );
}

/** webpages.faq_list: questions, all open */
export function FaqList({ eye, k, h, qa }: { eye: ReactNode; k: string; h: ReactNode; qa: [string, string][] }) {
  return (
    <Wrap>
      <div style={sx("display:flex;gap:96px")}>
        <div style={sx("width:420px")}><Eyebrow t={eye} k={k} /><div style={sx("margin-top:14px")}><Head t={h} size={40} w={420} /></div></div>
        <div style={sx("flex:1")}>
          {qa.map(([q, a]) => (
            <div key={q} style={sx(`padding:22px 0;border-top:1px solid ${LINE}`)}>
              <div style={sx(`font:600 18px ${SANS}`)}>{q}</div>
              <div style={sx(`font:400 16px/1.6 ${SANS};color:${INK2};margin-top:6px;max-width:720px`)}>{a}</div>
            </div>
          ))}
        </div>
      </div>
    </Wrap>
  );
}

/** webpages.link_card: icon or drawing, title, one line, the action on the bottom line */
export function LinkCard({ k, t, d, act, w, h, art, to }: { k: string; t: ReactNode; d: ReactNode; act: string; w?: number; h?: number; art?: ReactNode; to?: string }) {
  const top = art ? <div style={sx(`margin:-28px -28px 20px;height:220px;${DOTS};border-bottom:1px solid #eceef2;overflow:hidden`)}>{art}</div> : <NavIcon k={k} s={48} />;
  return (
    <A href={to ?? href(act)} style={`${w ? `width:${w}px;` : "flex:1;"}box-sizing:border-box;border-radius:24px;background:${PLATE};padding:28px;display:flex;flex-direction:column;overflow:hidden;${h ? `min-height:${h}px;` : ""}`}>
      {top}
      <div style={sx(`font:600 24px/1.15 ${SANS};letter-spacing:-0.02em;margin-top:${art ? 0 : 20}px;text-wrap:balance`)}>{t}</div>
      <div style={sx(`font:400 15px/1.5 ${SANS};color:${INK2};margin-top:8px`)}>{d}</div>
      <div style={sx("margin-top:auto;padding-top:22px")}><Explore t={act} /></div>
    </A>
  );
}

export { Card, Fig, Lab, FAINT, INK };

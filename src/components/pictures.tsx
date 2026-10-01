/**
 * The pictures beside the type on department, school-type, role and platform pages (webpages.card_html, tcard,
 * pic_of, hero_pic, and mobile.pic_of): product cards tagged with their portal, on a photograph or a dotted plate.
 */
import type { ReactElement, ReactNode } from "react";
import { At, DeptArt, OnPlate, Ph, PhotoStory, Tagged, sx } from "./ds";
import { AttCard, FeeCard, HeadCard, MarksCard, MessageCard, NoteCard, ReceiptsCard, RegisterCard, ReportCard, SyncCard, WeekCard } from "./cards";
import { SITE_CARDS } from "./site-cards";
import { ParentPhone } from "./phones";
import { PicIntegrations } from "./sections";
import { PhoneOn, PhotoCard, PlateCard, ScaleTo } from "./phone";

/** which portal each card comes from (webpages.CARD_PORTAL) */
export const CARD_PORTAL: Record<string, string> = {
  intake_card: "Administration", application_card: "Administration", offer_card: "Administration", payments_card: "Administration",
  billing_card: "Administration", arrears_card: "Administration", ledger_card: "Administration", journal_card: "Administration",
  fiscal_card: "Administration", payslip_card: "Teacher", payrun_card: "Administration", staff_card: "Administration",
  leave_card: "Teacher", rollcall_card: "Administration", exeat_card: "Parent", sickbay_card: "Administration",
  stock_card: "Administration", issue_card: "Administration", repairs_card: "Teacher", compose_card: "Teacher",
  events_card: "Parent", read_card: "Teacher", attendance_card: "Administration", collected_card: "Administration",
  results_card: "Administration", transport_card: "Parent", levy_card: "Parent", ai_card: "Student", student_card: "Student",
  approvals_card: "Administration", plan_card: "Administration", visitors_card: "Administration", register_card: "Teacher", marks_card: "Teacher", fee_card: "Parent", head_card: "Administration",
  note_card: "Parent", att_card: "Administration", signin_card: "Administration",
};
/** cards drawn wider than 300 (webpages.WIDE) */
export const WIDE: Record<string, number> = {
  compose_card: 340, ai_card: 340, payments_card: 320, billing_card: 320, arrears_card: 320, ledger_card: 320, journal_card: 320,
  stock_card: 320, attendance_card: 320, collected_card: 320, fee_card: 320, note_card: 330, fiscal_card: 280, visitors_card: 320,
};

const UI_CARDS: Record<string, (p: { w?: number }) => ReactElement> = {
  register_card: ({ w }) => <RegisterCard w={w} />, sync_card: SyncCard, marks_card: MarksCard, fee_card: FeeCard, report_card: ReportCard,
  head_card: HeadCard, receipts_card: ReceiptsCard, message_card: MessageCard, week_card: WeekCard,
};

/** webpages.card_html: a card by its name in the design source, at its width */
export function CardHtml({ name, w, to }: { name: string; w?: number; to?: string }) {
  const width = w ?? WIDE[name] ?? 300;
  const sc = SITE_CARDS[name];
  if (sc) return sc(to ? { w: width, to } : { w: width });
  if (name === "note_card") return <NoteCard w={width} />;
  if (name === "att_card") return <AttCard w={width} />;
  const ui = UI_CARDS[name];
  if (!ui) throw new Error(`No card "${name}"`);
  return ui({ w: width });
}

/** webpages.tcard: a card with its portal's tag above it */
export const TCard = ({ name, w, to }: { name: string; w?: number; to?: string }) =>
  <Tagged tag={`${CARD_PORTAL[name] ?? "Administration"} portal`}><CardHtml name={name} w={w} to={to} /></Tagged>;

export type PicSpec = ["plate", [string, number, number][], string | null] | ["photo", string, string, [string, number, number][]] | ["integrations"] | ["phone"];

/** webpages.pic_of: the picture a row's spec describes */
export function PicOf({ spec, w = 620, h = 440 }: { spec: PicSpec; w?: number; h?: number }) {
  switch (spec[0]) {
    case "plate":
      return (
        <OnPlate w={w} h={h}>
          {spec[2] ? <div style={sx("position:absolute;right:-12px;bottom:-6px")}><DeptArt k={spec[2]} w={420} h={290} U={48} /></div> : null}
          {spec[1].map(([n, x, y]) => <At key={n} x={x} y={y} z={3}><TCard name={n} /></At>)}
        </OnPlate>
      );
    case "photo":
      return <PhotoStory n={spec[1]} pos={spec[2]} cards={spec[3].map(([n, x, y]) => [x, y, <TCard key={n} name={n} />])} w={w} h={h} />;
    case "integrations":
      return <PicIntegrations w={w} h={h} />;
    case "phone":
      return <PhotoStory n="mother-phone.jpg" pos="65% center" cards={[[0, 8, <ParentPhone key="p" k={0.52} />]]} w={w} h={470} />;
  }
}

/** webpages.hero_pic: the wide photograph with a card on each side */
export function HeroPic({ photo, pos, a, b, children }: { photo: string; pos: string; a: string; b: string; children?: ReactNode }) {
  return (
    <div style={sx("position:relative;width:1200px;height:600px")}>
      <div style={sx("position:absolute;left:90px;top:30px")}><Ph n={photo} w={1020} h={570} pos={pos} r={24} /></div>
      <At x={0} y={120} z={3}><TCard name={a} /></At>
      <At x={1200 - (WIDE[b] ?? 300)} y={0} z={2}><TCard name={b} /></At>
      {children}
    </div>
  );
}

// ---- phone -----------------------------------------------------------------------------------------------
/** mobile.tcard: 310 wide unless asked */
export const MTCard = ({ name, w = 310, to }: { name: string; w?: number; to?: string }) => <TCard name={name} w={w} to={to} />;

/** mobile.pic_of: the first card of the spec, at its own size */
export function MPicOf({ spec }: { spec: PicSpec }) {
  switch (spec[0]) {
    case "plate":
      return <PlateCard card={<MTCard name={spec[1][0][0]} />} art={spec[2]} />;
    case "photo":
      return <PhotoCard photo={spec[1]} pos={spec[2]} card={<MTCard name={spec[3][0][0]} />} />;
    case "integrations":
      return <ScaleTo w={620} h={420}><PicIntegrations w={620} h={420} /></ScaleTo>;
    case "phone":
      return <PhoneOn phone={<ParentPhone k={0.6} />} photo="mother-phone.jpg" pos="65% center" />;
  }
}

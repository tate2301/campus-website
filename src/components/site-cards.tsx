/**
 * Small product cards for the website pages (site_cards.py), one world: Mukuvisi High School, Form 3B, Tanaka and
 * Rudo Moyo, Ms Sibanda, Mr Dube the Head, Tsavo House. Figures add up across cards.
 */
import type { ReactElement, ReactNode } from "react";
import { Art } from "./art";
import { BrandLogo, Card, Cbtn, Chead, Fig, Ic, Lab, Pmark, PortalIcon, Rowl, Status, sx } from "./ds";
import { BAD, BADS, BLUE, FAINT, INK, INK2, LINE, MONO, MUTED, NUM, OK, OKS, SANS, WARN, pyRound } from "@/lib/design";
import { MARKS } from "@/content/world";
import { MARKET } from "@/content/copy";

type StatusKind = "ok" | "warn" | "bad" | "info" | "mute" | "campus";
type BtnKind = "primary" | "secondary" | "dark" | "tint";

/** Python's f"{v:,}" for whole numbers */
const comma = (v: number) => String(v).replace(/\B(?=(\d{3})+(?!\d))/g, ",");

// ---- helpers -------------------------------------------------------------------------------------------
/** site_cards._btns */
const Btns = ({ b }: { b: [string, string, BtnKind][] }) => (
  <div style={sx("display:flex;gap:8px;margin-top:12px")}>
    {b.map(([t, i, k]) => <Cbtn key={t} label={t} icon={i} kind={k} size="sm" />)}
  </div>
);

/** site_cards._foot */
const Foot = ({ t }: { t: ReactNode }) => <div style={sx(`margin-top:8px;font-size:12px;color:${MUTED}`)}>{t}</div>;

/** site_cards._pills */
const Pills = ({ p }: { p: [string, StatusKind][] }) => (
  <div style={sx("display:flex;gap:8px;flex-wrap:wrap;margin-top:10px")}>
    {p.map(([t, k]) => <Status key={t} t={t} kind={k} />)}
  </div>
);

/** site_cards.lhead: a card head that leads with the named service's own mark */
const Lhead = ({ name, title, meta = "" }: { name: string; title: ReactNode; meta?: ReactNode }) => (
  <div style={sx("display:flex;align-items:center;gap:8px;margin-bottom:10px;white-space:nowrap")}>
    <BrandLogo n={name} s={22} />
    <span style={sx(`font:600 13.5px ${SANS};color:${INK};overflow:hidden;text-overflow:ellipsis`)}>{title}</span><span style={sx("flex:1")} /><Lab t={meta} />
  </div>
);

/** site_cards.lrow */
const Lrow = ({ name, a, b, top = true }: { name: string; a: ReactNode; b: ReactNode; top?: boolean }) => (
  <div style={sx(`display:flex;align-items:center;gap:10px;padding:7px 0;${top ? "border-top:1px solid #e3e6eb;" : ""}font-size:13px`)}>
    <BrandLogo n={name} s={20} />
    <span style={sx("flex:1")}>{a}</span><span style={sx(`font-weight:500;${NUM}`)}>{b}</span>
  </div>
);

/** site_cards.qr: a drawn QR code */
const Qr = ({ n = 21, s = 4, seed = 7 }: { n?: number; s?: number; seed?: number }) => <Art k={`qr:${n}:${s}:${seed}`} />;

// ---- admissions ----------------------------------------------------------------------------------------
/** site_cards.intake_card */
export const IntakeCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="user-add" title="Form 1 · 2027 intake" meta="120 places" />
    <Rowl a="Enquiries" b="214" top={false} /><Rowl a="Applications" b="168" /><Rowl a="Sat the entrance test" b="142" />
    <Rowl a="Offers sent" b="132" /><Rowl a="Accepted" b="96" c={INK} bold /><Pills p={[["Deposits due 30 Oct", "warn"]]} />
  </Card>
);

/** site_cards.application_card */
export const ApplicationCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="file-check" title="Application · Nyasha Banda" meta="A-0142" />
    <Rowl a="Guardian" b="Grace Banda" top={false} /><Rowl a="Grade 7 results" b="6 units" /><Rowl a="Entrance test" b="68%" />
    <Rowl a="Documents" b="3 of 3" /><Pills p={[["Offer sent", "campus"], ["Deposit due 30 Oct", "warn"]]} />
  </Card>
);

/** site_cards.offer_card */
export const OfferCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="send-plane" title="Offer letters · Form 1" meta="Today" />
    <Rowl a="Sent to guardians" b="132" top={false} /><Rowl a="Deposit paid" b="96" c={OK} /><Rowl a="Waiting list" b="18" />
    <Btns b={[["Move to class lists", "arrow-right-line", "primary"]]} />
  </Card>
);

// ---- fees ----------------------------------------------------------------------------------------------
/** site_cards.payments_card */
export const PaymentsCard = ({ w = 320 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="bank-card" title="Payments today" meta="Bursary" />
    <Lrow name="EcoCash" a="Tanaka Moyo" b="US$500.00" top={false} /><Lrow name="Bank transfer" a="Chipo Ncube" b="US$330.00" />
    <Lrow name="Cash" a="Farai Nyathi" b="ZiG 2,400.00" /><Pills p={[["3 matched to pupils", "ok"], ["R-2026-18824", "mute"]]} />
  </Card>
);

/** site_cards.billing_card */
export const BillingCard = ({ w = 320 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="wallet-3" title="Term 3 billing" meta="Ready to send" />
    <Rowl a="Tuition, Forms 1–4" b="US$1,250.00" top={false} /><Rowl a="Boarding" b="US$900.00" /><Rowl a="Transport" b="US$180.00" />
    <Rowl a="Pupils billed" b="1,140" c={INK} bold /><Pills p={[["Sibling discount on 214", "campus"]]} />
    <Btns b={[["Send statements", "send-plane", "primary"]]} />
  </Card>
);

const ARREARS: [string, number, number][] = [["Form 1", 4120, .46], ["Form 2", 6380, .71], ["Form 3", 8950, 1.0], ["Form 4", 5210, .58]];

/** site_cards.arrears_card */
export const ArrearsCard = ({ w = 320 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="chart-bar" title="Arrears by form" meta="Today" />
    {ARREARS.map(([n, v, k]) => (
      <div key={n} style={sx("display:flex;align-items:center;gap:10px;padding:7px 0;border-top:1px solid #edeff2;font-size:13px")}>
        <span style={sx("width:52px")}>{n}</span><span style={sx("flex:1;height:8px;border-radius:4px;background:#eef0f3;position:relative")}>
          <i style={sx(`position:absolute;left:0;top:0;bottom:0;width:${pyRound(k * 100)}%;border-radius:4px;background:${WARN}`)} /></span>
        <span style={sx(`width:84px;text-align:right;font-weight:500;${NUM}`)}>US${comma(v)}</span>
      </div>
    ))}
    <Btns b={[["Send reminders", "send-plane", "secondary"]]} />
  </Card>
);

// ---- accounting ----------------------------------------------------------------------------------------
/** site_cards.ledger_card */
export const LedgerCard = ({ w = 320 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="book-2" title="General ledger" meta="Sep 2026" />
    <Rowl a="Fees income" b="US$412,300.00" top={false} /><Rowl a="Payroll" b="−US$186,420.00" /><Rowl a="Stores and supplies" b="−US$22,910.00" />
    <Rowl a="Repairs" b="−US$4,180.00" /><Rowl a="Net for the month" b="US$198,790.00" c={INK} bold /><Pills p={[["Up to date at 18:00", "ok"]]} />
  </Card>
);

/** site_cards.journal_card */
export const JournalCard = ({ w = 320, to = "Sage Pastel" }: { w?: number; to?: string }) => (
  <Card w={w}>
    <Lhead name={to} title={`Journal to ${to}`} meta="30 Sep" />
    <Rowl a="Bank" b="Dr US$12,840.00" top={false} /><Rowl a="Fees income" b="Cr US$11,920.00" /><Rowl a="Uniform sales" b="Cr US$920.00" />
    <Pills p={[[`Posted to ${to}`, "ok"], ["J-0930", "mute"]]} />
  </Card>
);

const FISCAL: [string, string][] = [["Receipt", "R-2026-18824"], ["Pupil", "Tanaka Moyo"], ["Term 3 fees", "US$500.00"], ["Fiscal day", "214"], ["Device", "0412"]];

/** site_cards.fiscal_card */
export function FiscalCard({ w = 280 }: { w?: number }) {
  const m = `font:400 11.5px ${MONO};color:${INK2}`;
  return (
    <Card w={w}>
      <div style={sx(`text-align:center;font:600 13.5px ${SANS}`)}>Mukuvisi High School</div>
      <div style={sx(`text-align:center;font:400 11.5px ${MONO};color:${MUTED};margin-top:2px`)}>Fiscal tax invoice</div>
      <div style={sx("border-top:1px dashed #cfd4dc;margin:10px 0 6px")} />
      {FISCAL.map(([a, b]) => (
        <div key={a} style={sx(`display:flex;justify-content:space-between;${m};padding:3px 0`)}><span>{a}</span><span>{b}</span></div>
      ))}
      <div style={sx("border-top:1px dashed #cfd4dc;margin:6px 0 10px")} />
      <div style={sx("display:flex;gap:12px;align-items:center")}>
        <Qr />
        <div style={sx("flex:1")}>
          <div style={sx(m)}>Verification code</div>
          <div style={sx(`font:500 12.5px ${MONO};margin-top:2px`)}>4F2A-9C1B-77D0</div>
          <div style={sx("margin-top:8px;display:flex;align-items:center;gap:6px")}><BrandLogo n="ZIMRA" s={20} /><Status t="Sent to FDMS" kind="ok" /></div>
        </div>
      </div>
    </Card>
  );
}

// ---- HR and payroll ------------------------------------------------------------------------------------
/** site_cards.payslip_card */
export const PayslipCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="file-check" title="Payslip · September 2026" meta="Mrs T. Ncube" />
    <Rowl a="Basic salary" b="US$620.00" top={false} /><Rowl a="Allowances" b="US$80.00" /><Rowl a="PAYE" b="−US$41.30" c={MUTED} />
    <Rowl a="AIDS levy" b="−US$1.24" c={MUTED} /><Rowl a="NSSA" b="−US$31.50" c={MUTED} /><Rowl a="Net pay" b="US$625.96" c={INK} bold />
  </Card>
);

/** site_cards.payrun_card */
export const PayrunCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="wallet-3" title="September payroll" meta="86 staff" />
    <Rowl a="Gross pay" b="US$58,240.00" top={false} /><Rowl a="Deductions" b="−US$7,180.00" /><Rowl a="Net pay" b="US$51,060.00" c={INK} bold />
    <Pills p={[["Payday 25 Sep", "info"]]} /><Btns b={[["Approve payroll", "check-circle", "primary"]]} />
  </Card>
);

/** site_cards.staff_card */
export const StaffCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="user-3" title="Mrs Tariro Ncube" meta="Science" />
    <Rowl a="Contract" b="Fixed term to Dec 2026" top={false} /><Rowl a="Qualifications" b="BEd, Science" /><Rowl a="Leave left" b="14 of 22 days" />
    <Rowl a="Bank details" b="On file" /><Pills p={[["Renewal due this term", "warn"]]} />
  </Card>
);

const LEAVE: [string, string][] = [["Mrs Ncube", "2 days · 6–7 Oct"], ["Mr Chari", "1 day · 9 Oct"], ["Ms Sibanda", "Half day · 14 Oct"]];

/** site_cards.leave_card */
export const LeaveCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="calendar" title="Leave requests" meta="3 waiting" />
    {LEAVE.map(([n, d], i) => (
      <div key={n} style={sx(`display:flex;align-items:center;gap:10px;padding:8px 0;border-top:${i ? "1px solid #edeff2" : "0"};font-size:13px`)}>
        <div style={sx("flex:1")}><div style={sx("font-weight:600")}>{n}</div><div style={sx(`color:${MUTED};font-size:12px`)}>{d}</div></div>
        <span style={sx(`height:28px;padding:0 10px;border-radius:14px;background:${BLUE};color:#fff;display:inline-flex;align-items:center;font:500 12px ${SANS}`)}>Approve</span>
      </div>
    ))}
    <Foot t="Cover goes on the timetable when you approve" />
  </Card>
);

// ---- boarding ------------------------------------------------------------------------------------------
/** site_cards.rollcall_card */
export const RollcallCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="moon" title="Tsavo House · lights out" meta="21:00" />
    <Rowl a="In the house" b="58" top={false} /><Rowl a="On exeat" b="4" /><Rowl a="Sick bay" b="1" />
    <Rowl a="Not marked" b="1" c={BAD} bold />
    <div style={sx(`display:flex;align-items:center;gap:8px;margin-top:8px;padding:8px 10px;border-radius:12px;background:${BADS};font-size:12.5px;color:${BAD}`)}>
      <Ic n="alert" s={14} c={BAD} />Tafadzwa Zhou · last seen at prep
    </div>
  </Card>
);

/** site_cards.exeat_card */
export const ExeatCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="door" title="Exeat · Kudzai Mhlanga" meta="Form 4" />
    <Rowl a="Out" b="Fri 16:00" top={false} /><Rowl a="Back" b="Sun 17:00" /><Rowl a="Collected by" b="Mr T. Mhlanga" />
    <Rowl a="Approved by" b="Mr Chari, housemaster" /><Pills p={[["Signed out 16:12", "campus"]]} />
  </Card>
);

/** site_cards.sickbay_card */
export const SickbayCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="first-aid-kit" title="Sick bay · today" meta="Matron" />
    <Rowl a="Seen" b="5" top={false} /><Rowl a="Back to lessons" b="4" /><Rowl a="Resting" b="1" />
    <Pills p={[["Guardians told", "ok"], ["Class teachers told", "ok"]]} />
  </Card>
);

// ---- stock ---------------------------------------------------------------------------------------------
/** site_cards.stock_card */
export const StockCard = ({ w = 320 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="box-3" title="Stores" meta="Today" />
    <Rowl a="Blazer, size 34" b="12 · reorder at 10" c={WARN} top={false} /><Rowl a="School tie" b="84" />
    <Rowl a="Exercise books, A4" b="1,260" /><Rowl a="Science textbook, Form 3" b="36 of 120 issued" />
    <Pills p={[["PO-0391 sent to supplier", "info"]]} />
  </Card>
);

/** site_cards.issue_card */
export const IssueCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="book-2" title="Issued to Tanaka Moyo" meta="Form 3B" />
    <Rowl a="Mathematics, Form 3" b="Due back Nov" top={false} /><Rowl a="Combined Science, Form 3" b="Due back Nov" />
    <Rowl a="Blazer, size 34" b="US$45.00 to fees" /><Pills p={[["Signed for 12 Jan", "ok"]]} />
  </Card>
);

const REPAIRS: [string, string, StatusKind][] = [["Window, Room 12", "Assigned", "info"], ["Tap, Tsavo House", "Done · US$18", "ok"], ["Projector, Lab 2", "Waiting for part", "warn"]];

/** site_cards.repairs_card */
export const RepairsCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="tool" title="Repairs" meta="3 open this week" />
    {REPAIRS.map(([n, t, k], i) => (
      <div key={n} style={sx(`display:flex;align-items:center;justify-content:space-between;gap:10px;padding:8px 0;border-top:${i ? "1px solid #edeff2" : "0"};font-size:13px`)}>
        <span>{n}</span><Status t={t} kind={k} />
      </div>
    ))}
  </Card>
);

// ---- communication -------------------------------------------------------------------------------------
/** site_cards.compose_card */
export const ComposeCard = ({ w = 340 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="send-plane" title="New message" meta="Ms Sibanda" />
    <div style={sx(`display:flex;align-items:center;gap:8px;font-size:12.5px;color:${MUTED}`)}>
      To <span style={sx(`display:inline-flex;align-items:center;gap:6px;height:26px;padding:0 10px;border-radius:13px;background:#e8effd;color:${BLUE};font:500 12.5px ${SANS}`)}><Ic n="group" s={13} c={BLUE} />Form 3B guardians · 38</span>
    </div>
    <div style={sx(`margin-top:10px;padding:10px 12px;border-radius:12px;box-shadow:inset 0 0 0 1px ${LINE};font:400 13.5px/1.5 ${SANS};color:${INK2}`)}>
      Sports day is on Friday 9 October. Pupils come in sports kit and bring water.
    </div>
    <div style={sx("display:flex;align-items:center;justify-content:space-between;margin-top:12px")}>
      <span style={sx(`font-size:12px;color:${MUTED}`)}>Replies go to Ms Sibanda</span>
      <Cbtn label="Send" icon="send-plane" kind="primary" size="sm" />
    </div>
  </Card>
);

/** site_cards.events_card */
export const EventsCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="calendar" title="Term 3 dates" meta="Parent portal" />
    <Rowl a="Sports day" b="Fri 9 Oct" top={false} /><Rowl a="Half term" b="16–19 Oct" /><Rowl a="Form 4 exams start" b="Mon 26 Oct" />
    <Rowl a="Term closes" b="Thu 3 Dec" /><Pills p={[["Reminder the day before", "campus"]]} />
  </Card>
);

/** site_cards.read_card */
export const ReadCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="chat-3" title="Sports day notice" meta="Form 3B" />
    <div style={sx("display:flex;align-items:baseline;gap:8px")}><Fig v="34 of 38" s={26} /><span style={sx(`font-size:13px;color:${MUTED}`)}>guardians read it</span></div>
    <div style={sx("margin-top:10px")}>
      {["Mr Nyathi", "Mrs Gumbo", "Mr Zhou", "Mrs Chirwa"].map((n) => (
        <div key={n} style={sx("display:flex;justify-content:space-between;padding:7px 0;border-top:1px solid #edeff2;font-size:13px")}><span>{n}</span><span style={sx(`color:${MUTED}`)}>Not opened</span></div>
      ))}
    </div>
    <Btns b={[["Remind the 4", "send-plane", "secondary"]]} />
  </Card>
);

// ---- insights ------------------------------------------------------------------------------------------
const ATT: [string, number][] = [["F1", 97.1], ["F2", 96.2], ["F3", 95.4], ["F4", 94.8], ["F5", 91.6], ["F6", 97.9]];

/** site_cards.attendance_card */
export const AttendanceCard = ({ w = 320 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="chart-bar" title="Attendance by form" meta="This week" hue={BLUE} />
    <div style={sx("display:flex;align-items:flex-end;gap:6px;height:130px;padding-top:6px")}>
      {ATT.map(([n, v]) => (
        <div key={n} style={sx("flex:1;display:flex;flex-direction:column;align-items:center;gap:6px")}>
          <span style={sx(`font:500 11px ${SANS};color:${INK2};${NUM}`)}>{v.toFixed(1)}</span>
          <span style={sx(`width:22px;height:${pyRound((v - 86) * 8)}px;border-radius:6px 6px 2px 2px;background:${v < 93 ? WARN : BLUE}`)} />
          <span style={sx(`font:500 11.5px ${SANS};color:${MUTED}`)}>{n}</span>
        </div>
      ))}
    </div>
    <Pills p={[["Form 5 down 3 points", "warn"]]} />
  </Card>
);

/** site_cards.collected_card */
export const CollectedCard = ({ w = 320 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="wallet-3" title="Fees collected" meta="Term 3" hue={BLUE} />
    <div style={sx("display:flex;align-items:baseline;gap:8px")}><Fig v="70.3%" s={30} /><span style={sx(`font-size:13px;color:${MUTED}`)}>of US$1,425,000.00 billed</span></div>
    <div style={sx("display:flex;height:10px;border-radius:5px;overflow:hidden;margin:12px 0 4px;background:#eef0f3")}>
      <i style={sx(`width:58%;background:${BLUE}`)} /><i style={sx("width:12.3%;background:#8fb0f6")} />
    </div>
    <Rowl a="Paid in US dollars" b="58.0%" top={false} /><Rowl a="Paid in ZiG" b="12.3%" /><Rowl a="Outstanding" b="29.7%" c={WARN} />
  </Card>
);

/** site_cards.results_card */
export const ResultsCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="file-check" title="Results · Form 3" meta="Term 3" hue={BLUE} />
    {MARKS.slice(0, 4).map(([n, , avg, d], i) => (
      <div key={n} style={sx(`display:flex;justify-content:space-between;align-items:center;padding:7px 0;border-top:${i ? "1px solid #edeff2" : "0"};font-size:13px`)}>
        <span>{n}</span>
        <span style={sx("display:flex;gap:10px;align-items:center")}>
          <b style={sx(`font-weight:600;${NUM}`)}>{avg}%</b><Status t={d.replaceAll("-", "−")} kind={d.startsWith("+") ? "ok" : "bad"} />
        </span>
      </div>
    ))}
    <Foot t="Class averages, against Term 2" />
  </Card>
);

// ---- school types and roles ----------------------------------------------------------------------------
/** site_cards.transport_card */
export const TransportCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="bus-2" title="Route 4 · Mabelreign" meta="06:50" />
    <Rowl a="Stop 1 · Ashdown Park" b="9 pupils" top={false} /><Rowl a="Stop 2 · Meyrick Park" b="14 pupils" /><Rowl a="Stop 3 · Mabelreign shops" b="11 pupils" />
    <Pills p={[["Tanaka Moyo · stop 3", "campus"], ["Billed with fees", "mute"]]} />
  </Card>
);

/** site_cards.levy_card */
export const LevyCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="wallet-3" title="Fees and levies · Form 2" meta="Term 3" />
    <Rowl a="Tuition" b="US$120.00" top={false} /><Rowl a="Building levy" b="US$15.00" /><Rowl a="Sports levy" b="US$5.00" />
    <Rowl a="Total" b="US$140.00" c={INK} bold /><Pills p={[["Set by the SDC", "mute"], ["US$ or ZiG", "info"]]} />
  </Card>
);

/** site_cards.ai_card's bubble */
const AiBub = ({ t, me }: { t: ReactNode; me: boolean }) => (
  <div style={sx(`display:flex;justify-content:${me ? "flex-end" : "flex-start"};margin-top:8px`)}>
    <div style={sx(`max-width:84%;padding:9px 12px;border-radius:14px;background:${me ? BLUE : "#f2f4f7"};color:${me ? "#fff" : INK};font:400 13px/1.45 ${SANS}`)}>{t}</div>
  </div>
);

/** site_cards.ai_card */
export const AiCard = ({ w = 340 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="sparkles" title="Ask the library" meta="Student portal" />
    <AiBub t="Why does a plant cell have a cell wall?" me={true} />
    <AiBub t="The cell wall keeps the cell's shape and stops it bursting when it takes in water. See page 14 of your notes." me={false} />
    <span style={sx(`display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 9px;border-radius:12px;box-shadow:inset 0 0 0 1px ${LINE};font:500 11.5px ${SANS};color:${INK2};margin-top:8px`)}>
      <Ic n="book-2" s={12} c={MUTED} />Form 2 Science notes · Mr Chari
    </span>
    <Foot t="Logged · the school can switch AI off" />
  </Card>
);

/** site_cards.student_card */
export const StudentCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="calendar" title="Tanaka · Tuesday" meta="Student portal" />
    <Rowl a="07:30 · Mathematics" b="Room 12" top={false} /><Rowl a="08:40 · Combined Science" b="Lab 2" /><Rowl a="10:10 · English" b="Room 7" />
    <Rowl a="English essay" b="Due Thu" c={WARN} /><Pills p={[["3 library books on loan", "campus"]]} />
  </Card>
);

const APPROVALS: [string, string][] = [["wallet-3", "September payroll"], ["calendar", "Leave · Mrs Ncube"], ["send-plane", "Form 1 offers · 12"]];

/** site_cards.approvals_card */
export const ApprovalsCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="check-circle" title="Waiting for you" meta="Mr Dube" hue={BLUE} />
    {APPROVALS.map(([icn, t], i) => (
      <div key={t} style={sx(`display:flex;align-items:center;gap:10px;padding:8px 0;border-top:${i ? "1px solid #edeff2" : "0"};font-size:13px`)}>
        <Ic n={icn} s={15} c={MUTED} /><span style={sx("flex:1")}>{t}</span>
        <span style={sx(`height:26px;padding:0 10px;border-radius:13px;background:${BLUE};color:#fff;display:inline-flex;align-items:center;font:500 12px ${SANS}`)}>Approve</span>
      </div>
    ))}
  </Card>
);

/** site_cards.signin_card */
export const SigninCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="user-3" title="Sign-ins" meta="Parent portal" />
    <Rowl a="Guardians with a sign-in" b="1,804" top={false} /><Rowl a="Signed in this week" b="1,377" /><Rowl a="Sent this morning" b="12 new families" />
    <Pills p={[["Works on any phone", "ok"]]} />
  </Card>
);

// ---- the demo visit ------------------------------------------------------------------------------------
/** site_cards.plan_card */
export const PlanCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="task" title="Your plan · Mukuvisi High" meta="Draft" hue={BLUE} />
    <Rowl a="Setup and data capture" b="Weeks 1–2" top={false} /><Rowl a="Training at the school" b="Weeks 3–4" />
    <Rowl a="Active pupils" b="1,140" /><Rowl a="Each month" b="US$1,140.00" c={INK} bold />
    <Pills p={[["First month free", "ok"], ["Setup free", "ok"]]} />
  </Card>
);

const VISITORS: [string, string, string][] = [["Mr Dube", "Head", "Administration"], ["Mrs Gumbo", "Bursar", "Administration"], ["Ms Sibanda", "Form 3B teacher", "Teacher"],
  ["Mr Chari", "Housemaster, Tsavo House", "Administration"]];

/** site_cards.visitors_card */
export const VisitorsCard = ({ w = 320 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="calendar" title="Demo · Thu 8 Oct, 14:00" meta="Mukuvisi High" />
    {VISITORS.map(([n, role, p], i) => (
      <div key={n} style={sx(`display:flex;align-items:center;gap:10px;padding:8px 0;border-top:${i ? "1px solid #edeff2" : "0"}`)}>
        <PortalIcon n={p} s={28} />
        <div style={sx("flex:1;min-width:0")}><div style={sx(`font:600 13px ${SANS}`)}>{n}</div><div style={sx(`font:400 12px ${SANS};color:${MUTED}`)}>{role}</div></div>
        <Status t="Coming" kind="ok" />
      </div>
    ))}
    <div style={sx(`margin-top:8px;padding:8px 10px;border-radius:12px;background:#f2f4f7;font-size:12.5px;color:${INK2}`)}>Forms, fee structure and staff list loaded</div>
  </Card>
);

/** site_cards.thread_card's bubble */
const ThreadBub = ({ who, t, me }: { who: string; t: ReactNode; me: boolean }) => (
  <div style={sx(`margin-top:10px;display:flex;flex-direction:column;align-items:${me ? "flex-end" : "flex-start"}`)}>
    <span style={sx(`font:500 11.5px ${SANS};color:${MUTED};margin-bottom:4px`)}>{who}</span>
    <div style={sx(`max-width:88%;padding:9px 12px;border-radius:14px;background:${me ? "#f2f4f7" : BLUE};color:${me ? INK : "#fff"};font:400 13px/1.45 ${SANS}`)}>{t}</div>
  </div>
);

/** site_cards.thread_card */
export const ThreadCard = ({ w = 340 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="mail" title="Two campuses" meta="Pricing" />
    <ThreadBub who="Chipo Mutasa · Mukuvisi High" t="We run a junior and a senior campus. Is that one school on Campus, or two?" me={true} />
    <ThreadBub who="Campus team" t="One school and one record, with both campuses in it, at US$1 per active pupil per month." me={false} />
    <Pills p={[["Replied by email", "ok"]]} />
  </Card>
);

// ---- the integrations marketplace, as the Administration portal shows it -------------------------------
/** site_cards.marketplace */
export function Marketplace({ w = 1200 }: { w?: number }) {
  const cats = ["All", ...MARKET.map(([c]) => c)];
  const total = MARKET.reduce((t, [, x]) => t + x.length, 0);
  return (
    <div style={sx(`width:${w}px;border-radius:20px;overflow:hidden;background:#fff;box-shadow:0 0 0 1px ${LINE},0 30px 60px -30px rgba(11,12,20,.35)`)}>
      <div style={sx(`display:flex;align-items:center;gap:14px;padding:16px 22px;border-bottom:1px solid ${LINE}`)}>
        <Pmark s={28} r={8} />
        <span style={sx(`font:600 15px ${SANS}`)}>Integrations</span><span style={sx("flex:1")} />
        <span style={sx(`display:flex;align-items:center;gap:8px;width:280px;height:36px;padding:0 12px;border-radius:18px;background:#f2f4f7;font:400 13px ${SANS};color:${FAINT}`)}>
          <Ic n="search" s={15} c={MUTED} />Search integrations
        </span>
      </div>
      <div style={sx("display:flex")}>
        <div style={sx(`width:200px;padding:18px 14px;border-right:1px solid ${LINE};background:#fafbfc;display:flex;flex-direction:column;gap:4px`)}>
          {cats.map((c, i) => (
            <div key={c} style={sx(`display:flex;justify-content:space-between;align-items:center;height:36px;padding:0 12px;border-radius:10px;${i === 0 ? `background:#fff;box-shadow:0 0 0 1px ${LINE};` : ""}font:${i === 0 ? "600" : "500"} 13.5px ${SANS};color:${i === 0 ? INK : INK2}`)}>
              {c}<span style={sx(`font:400 12px ${SANS};color:${MUTED}`)}>{i === 0 ? total : MARKET[i - 1][1].length}</span>
            </div>
          ))}
        </div>
        <div style={sx("flex:1;padding:20px;display:grid;grid-template-columns:repeat(4,1fr);gap:14px;background:#fafbfc")}>
          {MARKET.flatMap(([cat, items]) => items.map(([n, d, st]) => (
            <div key={n} style={sx(`display:flex;flex-direction:column;gap:10px;padding:16px;border-radius:14px;background:#fff;box-shadow:0 0 0 1px ${LINE}`)}>
              <div style={sx("display:flex;justify-content:space-between;align-items:flex-start")}>
                <BrandLogo n={n} s={34} />
                {st ? (
                  <span style={sx(`display:inline-flex;align-items:center;gap:5px;height:28px;padding:0 10px;border-radius:14px;background:${OKS};color:${OK};font:500 12px ${SANS}`)}><Ic n="check-line" s={12} c={OK} />Connected</span>
                ) : (
                  <span style={sx(`display:inline-flex;align-items:center;height:28px;padding:0 12px;border-radius:14px;box-shadow:inset 0 0 0 1px ${LINE};font:500 12px ${SANS};color:${INK}`)}>Add</span>
                )}
              </div>
              <div><div style={sx(`font:600 14px ${SANS}`)}>{n}</div><div style={sx(`font:400 12.5px/1.45 ${SANS};color:${MUTED};margin-top:3px`)}>{d}</div></div>
              <div style={sx(`margin-top:auto;font:400 11.5px ${SANS};color:${FAINT}`)}>{cat}</div>
            </div>
          )))}
          <div style={sx("display:flex;flex-direction:column;align-items:flex-start;gap:10px;padding:16px;border-radius:14px;border:1.5px dashed #c9ced6")}>
            <span style={sx("width:34px;height:34px;border-radius:10px;background:#e8effd;display:flex;align-items:center;justify-content:center")}><Ic n="add-line" s={18} c={BLUE} /></span>
            <div><div style={sx(`font:600 14px ${SANS}`)}>Ask for an integration</div><div style={sx(`font:400 12.5px/1.45 ${SANS};color:${MUTED};margin-top:3px`)}>Tell us what your school uses</div></div>
          </div>
        </div>
      </div>
    </div>
  );
}

/** the site cards by their Python names, for the pages that place them by name */
export const SITE_CARDS: Record<string, (p: { w?: number; to?: string }) => ReactElement> = {
  intake_card: IntakeCard, application_card: ApplicationCard, offer_card: OfferCard,
  payments_card: PaymentsCard, billing_card: BillingCard, arrears_card: ArrearsCard,
  ledger_card: LedgerCard, journal_card: JournalCard, fiscal_card: FiscalCard,
  payslip_card: PayslipCard, payrun_card: PayrunCard, staff_card: StaffCard, leave_card: LeaveCard,
  rollcall_card: RollcallCard, exeat_card: ExeatCard, sickbay_card: SickbayCard,
  stock_card: StockCard, issue_card: IssueCard, repairs_card: RepairsCard,
  compose_card: ComposeCard, events_card: EventsCard, read_card: ReadCard,
  attendance_card: AttendanceCard, collected_card: CollectedCard, results_card: ResultsCard,
  transport_card: TransportCard, levy_card: LevyCard, ai_card: AiCard, student_card: StudentCard,
  approvals_card: ApprovalsCard, signin_card: SigninCard,
  plan_card: PlanCard, visitors_card: VisitorsCard, thread_card: ThreadCard,
};

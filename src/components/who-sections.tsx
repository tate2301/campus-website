/**
 * The sections made for each kind of school on the Who we serve pages (who_sections.py): the day school's day, the
 * boarding house at lights out, who pays whom at a government school, a private school's admissions and board, and a
 * mission school's day scholars and boarders side by side.
 */
import { Fragment, type ReactElement, type ReactNode } from "react";
import { At, Card, Cbtn, Chead, Fig, Ic, OnPlate, Ph, PhotoStory, Pmark, PortalIcon, Rowl, Status, Tagged, Ticks, sx } from "./ds";
import { AttCard, FeeCard, HeadCard, MarksCard, MessageCard, NoteCard, ReceiptsCard, RegisterCard, ReportCard, SyncCard, WeekCard } from "./cards";
import { Band, Row, SecHead, Wrap } from "./sections";
import { SITE_CARDS } from "./site-cards";
import { ParentPhone, RollcallPhone } from "./phones";
import { BAD, BLUE, CAMPUS, FAINT, GAP, INK, INK2, LINE, MONO, MUTED, NUM, OK, PLATE, PX, SANS, SERIF, WARN, pyRound } from "@/lib/design";

type StatusKind = "ok" | "warn" | "bad" | "info" | "mute" | "campus";

/** Python's f"{x:.1f}" (halves to even, as Python formats an exact tie) */
const f1 = (x: number) => (pyRound(x * 10) / 10).toFixed(1);

// ---- local helpers ------------------------------------------------------------------------------------------
/** who_sections._tc: a card tagged with its portal */
const Tc = ({ portal, children }: { portal: string; children: ReactNode }) => <Tagged tag={`${portal} portal`}>{children}</Tagged>;

/** who_sections._pills */
const Pills = ({ p }: { p: [string, StatusKind][] }) => (
  <div style={sx("display:flex;gap:8px;flex-wrap:wrap;margin-top:10px")}>{p.map(([t, k]) => <Status key={t} t={t} kind={k} />)}</div>
);

/** who_sections.row: pages.row in the page's column */
const WRow = (p: { eye: ReactNode; k: string; h: ReactNode; b: ReactNode; pic: ReactNode; flip?: boolean }) => <Wrap><Row {...p} /></Wrap>;

/** who_sections.plate_band */
const PlateBand = ({ children }: { children: ReactNode }) => <Band bg={PLATE} pad={`${GAP - 40}px ${PX}`}>{children}</Band>;

/** who_sections.SC_card: a ui.py card by its Python name (site_cards.py cards as a fallback) */
const UI_CARDS: Record<string, (p: { w?: number }) => ReactElement> = {
  register_card: RegisterCard, fee_card: FeeCard, marks_card: MarksCard, report_card: ReportCard, head_card: HeadCard, sync_card: SyncCard,
  receipts_card: ReceiptsCard, message_card: MessageCard, week_card: WeekCard, att_card: AttCard, note_card: NoteCard,
};
function ScCard({ name, w }: { name: string; w?: number }) {
  const C = UI_CARDS[name] ?? SITE_CARDS[name];
  return <C w={w} />;
}

// ---- cards only these pages use ------------------------------------------------------------------------------
/** who_sections.absence_card */
export const AbsenceCard = ({ w = 230 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="send-plane" title="Absent today" meta="08:06" />
    <Rowl a="Farai Nyathi" b="Form 3B" top={false} />
    <div style={sx(`margin-top:6px;padding:8px 10px;border-radius:12px;background:#f2f4f7;font:400 12.5px/1.45 ${SANS};color:${INK2}`)}>
      Farai is marked absent today. Reply to Ms Sibanda if you know why.
    </div>
    <Pills p={[["Sent to Mr Nyathi", "ok"]]} />
  </Card>
);

/** who_sections.family_card */
export const FamilyCard = ({ w = 330 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="home-3" title="Moyo family · Term 3" meta="One statement" />
    <Rowl a="Tanaka · Form 3B" b="US$1,250.00" top={false} /><Rowl a="Rufaro · Grade 5" b="US$980.00" /><Rowl a="Transport, both" b="US$180.00" />
    <Rowl a="Sibling discount, 5%" b="−US$49.00" c={OK} /><Rowl a="Paid, EcoCash 14 Sep" b="−US$500.00" c={OK} /><Rowl a="Balance" b="US$1,861.00" c={INK} bold />
    <Pills p={[["Due Fri 16 Oct", "warn"]]} />
  </Card>
);

/** who_sections.request_card */
export const RequestCard = ({ w = 250 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="door" title="Exeat request" meta="" hue={CAMPUS} />
    <Rowl a="Kudzai Mhlanga" b="Form 4" top={false} /><Rowl a="Out" b="Fri 16:00" /><Rowl a="Back" b="Sun 17:00" /><Rowl a="Collecting" b="Mr T. Mhlanga" />
    <div style={sx("margin-top:10px")}><Cbtn label="Send request" icon="send-plane" kind="primary" size="sm" /></div>
  </Card>
);

/** who_sections.approve_card */
export const ApproveCard = ({ w = 250 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="check-circle" title="Waiting for you" meta="Mr Chari" hue={BLUE} />
    <Rowl a="Kudzai Mhlanga · exeat" b="Fri–Sun" top={false} /><Rowl a="Guardian on record" b="Mr T. Mhlanga" c={OK} />
    <Rowl a="Fees" b="Up to date" c={OK} />
    <div style={sx("display:flex;gap:8px;margin-top:10px")}>
      <Cbtn label="Approve" icon="check-line" kind="primary" size="sm" /><Cbtn label="Decline" icon="" kind="secondary" size="sm" />
    </div>
  </Card>
);

/** who_sections.signout_card */
export const SignoutCard = ({ w = 250 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="time" title="Signed out" meta="16:12" hue={OK} />
    <Rowl a="Kudzai Mhlanga" b="Tsavo House" top={false} /><Rowl a="Collected by" b="Mr T. Mhlanga" /><Rowl a="Due back" b="Sun 17:00" />
    <Pills p={[["Off the house list", "campus"]]} />
  </Card>
);

/** who_sections.gov_staff_card */
export const GovStaffCard = ({ w = 320 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="user-3" title="Mr Tendai Chari" meta="Mathematics" />
    <Rowl a="Paid by" b="Government" top={false} /><Rowl a="Contract and posting" b="On file" /><Rowl a="Leave this year" b="3 of 22 days" />
    <Rowl a="Timetable" b="26 lessons a week" /><Pills p={[["Not on the school payroll", "mute"]]} />
  </Card>
);

/** who_sections.sdc_payrun_card */
export const SdcPayrunCard = ({ w = 320 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="wallet-3" title="SDC payroll · September" meta="14 staff" />
    <Rowl a="Groundsmen" b="4" top={false} /><Rowl a="Security" b="3" /><Rowl a="Office and kitchen" b="5" /><Rowl a="Extra teachers" b="2" />
    <Rowl a="Net pay" b="US$3,940.00" c={INK} bold />
    <div style={sx("margin-top:10px")}><Cbtn label="Approve payroll" icon="check-circle" kind="primary" size="sm" /></div>
  </Card>
);

const ABSENT = [7, 23, 41];

/** who_sections.bigclass_card: 52 pupils, three absent */
export const BigclassCard = ({ w = 320 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="book-6" title="Form 2C register" meta="07:35" />
    <div style={sx("display:grid;grid-template-columns:repeat(13,14px);gap:5px;margin:4px 0 10px")}>
      {Array.from({ length: 52 }, (_, i) => (
        <i key={i} style={sx(`width:14px;height:14px;border-radius:4px;background:${ABSENT.includes(i) ? BAD : OK};opacity:${ABSENT.includes(i) ? 1 : 0.75}`)} />
      ))}
    </div>
    <Rowl a="Present" b="49" /><Rowl a="Absent" b="3" c={BAD} />
    <div style={sx("display:flex;gap:8px;margin-top:10px")}>
      <Cbtn label="Mark all present" icon="check-line" kind="secondary" size="sm" /><Cbtn label="Save" icon="" kind="primary" size="sm" />
    </div>
  </Card>
);

/** who_sections.board_card */
export const BoardCard = ({ w = 320 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="chart-bar" title="Board report · Term 3" meta="Draft" hue={BLUE} />
    <Rowl a="Pupils on the roll" b="1,140 (+38)" top={false} /><Rowl a="Fees collected" b="70.3%" /><Rowl a="Form 4 average" b="64% (+3)" />
    <Rowl a="Staff" b="86 · 2 vacancies" /><Rowl a="Places for 2027" b="96 of 120 accepted" />
    <div style={sx("margin-top:10px")}><Cbtn label="Download the report (PDF)" icon="download-2" kind="secondary" size="sm" /></div>
  </Card>
);

const MIXED: [string, string, string][] = [["Tanaka Moyo", "Boarder", "P"], ["Tendai Chirwa", "Day", "P"], ["Ruvimbo Gumbo", "Boarder", "P"], ["Farai Nyathi", "Day", "A"], ["Chiedza Banda", "Day", "P"]];

/** who_sections.mixed_register_card: day scholars and boarders on one register */
export const MixedRegisterCard = ({ w = 320 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="book-6" title="Form 3B register" meta="07:42" />
    {MIXED.map(([n, t, m]) => (
      <div key={n} style={sx("display:flex;align-items:center;gap:10px;padding:7px 0;border-top:1px solid #edeff2;font-size:13px")}>
        <span style={sx("flex:1")}>{n}</span>
        <span style={sx(`font:500 11.5px ${SANS};color:${t === "Boarder" ? CAMPUS : INK2};background:${t === "Boarder" ? "#efeaff" : "#eef0f3"};padding:2px 8px;border-radius:10px`)}>{t}</span>
        <Status t={m === "P" ? "Present" : "Absent"} kind={m === "P" ? "ok" : "bad"} />
      </div>
    ))}
    <div style={sx(`display:flex;justify-content:space-between;padding-top:10px;border-top:1px solid #edeff2;font-size:12.5px;color:${MUTED}`)}>
      <span>22 day · 16 boarders</span><span>38</span>
    </div>
  </Card>
);

/** who_sections.authority_doc's sec: a heading and its figures */
const DocSec = ({ t, rows }: { t: string; rows: [string, string][] }) => (
  <div style={sx("margin-top:14px")}>
    <div style={sx(`font:600 12.5px ${SANS};color:${INK}`)}>{t}</div>
    {rows.map(([a, b]) => (
      <div key={a} style={sx(`display:flex;justify-content:space-between;padding:5px 0;border-bottom:1px solid #eef0f3;font:400 12px ${SANS};color:${INK2}`)}>
        <span>{a}</span><span style={sx(NUM)}>{b}</span>
      </div>
    ))}
  </div>
);

/** who_sections.authority_doc: the report to the responsible authority, on paper */
export const AuthorityDoc = ({ w = 400 }: { w?: number }) => (
  <div style={sx(`width:${w}px;box-sizing:border-box;background:#fff;border-radius:6px;box-shadow:0 0 0 1px ${LINE},0 24px 40px -24px rgba(11,12,20,.4);padding:28px 30px 30px`)}>
    <div style={sx("display:flex;justify-content:space-between;align-items:center")}>
      <Pmark s={26} r={7} /><span style={sx(`font:400 11px ${MONO};color:${MUTED}`)}>Term 3 · 2026</span>
    </div>
    <div style={sx(`font:500 20px/1.2 ${SERIF};margin-top:18px`)}>Report to the responsible authority</div>
    <DocSec t="Enrolment" rows={[["Day scholars", "412"], ["Boarders", "288"], ["New this year", "64"]]} />
    <DocSec t="Results" rows={[["Form 4 average", "62%"], ["Upper Sixth average", "68%"]]} />
    <DocSec t="Finance" rows={[["Fees and levies billed", "US$486,200"], ["Collected", "US$341,900 · 70.3%"]]} />
    <DocSec t="Staff" rows={[["Paid by government", "31"], ["Paid by the school", "18"]]} />
  </div>
);

// ---- sections by type ------------------------------------------------------------------------------------------
const DAY_STEPS: [string, string][] = [["06:50", "On the bus"], ["07:30", "Register"], ["08:06", "Absences home"], ["12:40", "Marks in"], ["16:10", "Home time"]];
const LEVELS: [string, string, string, string, string[]][] = [
  ["ecd-class.jpg", "center 40%", "ECD to Grade 7", "The class teacher marks one register and writes the report comment for each child.",
    ["Class registers", "A class teacher's comment on every report", "Parents of the youngest see each day"]],
  ["exam-blue.jpg", "center 40%", "Form 1 to Upper Sixth", "You mark registers by lesson, enter marks by subject, and every subject teacher adds a line to the report.",
    ["Registers by lesson", "Mark sheets by subject", "Exam classes in the holidays"]],
];

/** who_sections.day_sections: the school day, fees by family, primary and secondary */
export function daySections(): ReactNode[] {
  // one moment at a time: a short list of the day on the left, one picture for the selected moment on the right
  const on = 1;
  const lst = (
    <>
      {DAY_STEPS.map(([t, h], i) => (
        <div key={t} style={sx(`display:flex;gap:18px;padding:20px 0;border-top:1px solid ${LINE}`)}>
          <span style={sx(`width:58px;flex:none;font:500 14px ${MONO};color:${i === on ? BLUE : MUTED};padding-top:3px`)}>{t}</span>
          <div>
            <div style={sx(`font:600 ${i === on ? 24 : 20}px/1.2 ${SANS};letter-spacing:-0.015em;color:${i === on ? INK : MUTED}`)}>{h}</div>
            {i === on ? (
              <div style={sx(`font:400 16px/1.55 ${SANS};color:${INK2};margin-top:8px;max-width:360px`)}>
                Ms Sibanda marks Form 3B on a tablet before the first lesson, with or without internet. The office sees it by 08:05.
              </div>
            ) : null}
          </div>
        </div>
      ))}
      <div style={sx(`border-top:1px solid ${LINE}`)} />
    </>
  );
  const pic = <PhotoStory n="teacher-tablet.jpg" pos="center 25%" cards={[[0, 90, <Tc portal="Teacher"><ScCard name="register_card" w={300} /></Tc>]]} w={620} h={520} />;
  const day = (
    <Wrap key="day">
      <SecHead eye="The school day" k="t-day" h="From the bus stop to home time, on one record." />
      <div style={sx("display:flex;gap:96px;align-items:center;justify-content:space-between")}><div style={sx("flex:1;max-width:460px")}>{lst}</div>{pic}</div>
    </Wrap>
  );
  const fam = (
    <WRow key="fam" eye="Fees by family" k="fees" h="One statement for every family."
      b="Brothers and sisters bill to one family account, with the sibling discount applied. Parents pay once, by EcoCash or at the bursary, and the payment lands on each child's account."
      pic={<PhotoStory n="child-doorway.jpg" pos="center 30%" cards={[[0, 70, <Tc portal="Parent"><FamilyCard w={330} /></Tc>]]} w={620} h={480} />} flip />
  );
  const levels = (
    <Wrap key="levels">
      <SecHead eye="Primary and secondary" k="academics" h="Run ECD and Upper Sixth from the same record." />
      <div style={sx("display:flex;gap:24px")}>
        {LEVELS.map(([p, pos, t, d, pts]) => (
          <div key={t} style={sx(`flex:1;border-radius:24px;background:${PLATE};overflow:hidden`)}>
            <Ph n={p} w={588} h={300} pos={pos} r={0} />
            <div style={sx("padding:26px 28px 30px")}>
              <div style={sx(`font:600 26px/1.15 ${SANS};letter-spacing:-0.02em`)}>{t}</div>
              <div style={sx(`font:400 15.5px/1.55 ${SANS};color:${INK2};margin-top:8px`)}>{d}</div>
              <div style={sx("margin-top:14px")}><Ticks items={pts} c={INK2} /></div>
            </div>
          </div>
        ))}
      </div>
    </Wrap>
  );
  return [day, fam, levels];
}


/** who_sections.boarding_sections: roll call, exeats, boarding fees */
export function boardingSections(): ReactNode[] {
  const board = (
    <WRow key="board" eye="Roll call" k="boarding" h="Take roll call on your phone, house by house."
      b="Open your house at prep or lights out and tap each boarder in. Exeats and the sick bay are already marked, and anyone missing comes to the top. It works without internet."
      pic={<PhotoStory n="girls-smiling.jpg" pos="center 35%" cards={[[0, 10, <RollcallPhone k={0.52} />]]} w={620} h={480} />} flip />
  );
  const arrow = <div style={sx("flex:none;align-self:center;width:40px;display:flex;justify-content:center")}><Ic n="arrow-right-line" s={22} c={FAINT} /></div>;
  const steps: [string, string, string, ReactNode][] = [
    ["1", "The guardian asks", "From the Parent portal, with who is collecting.", <Tc portal="Parent"><RequestCard /></Tc>],
    ["2", "The housemaster approves", "The guardian and the fee account are checked on the record.", <Tc portal="Administration"><ApproveCard /></Tc>],
    ["3", "Signed out", "The boarder leaves the house list until they are back.", <Tc portal="Administration"><SignoutCard /></Tc>],
  ];
  const strip = steps.map(([n, t, d, c], i) => (
    <Fragment key={n}>
      {i > 0 ? arrow : null}
      <div style={sx("width:330px;display:flex;flex-direction:column;gap:16px")}>
        <div style={sx("display:flex;gap:12px;align-items:flex-start")}>
          <span style={sx(`width:30px;height:30px;border-radius:15px;background:${BLUE};color:#fff;display:flex;align-items:center;justify-content:center;font:600 14px ${SANS};flex:none`)}>{n}</span>
          <div><div style={sx(`font:600 19px ${SANS}`)}>{t}</div><div style={sx(`font:400 14.5px/1.5 ${SANS};color:${INK2};margin-top:4px`)}>{d}</div></div>
        </div>
        <div style={sx("padding-left:42px")}>{c}</div>
      </div>
    </Fragment>
  ));
  const exeat = (
    <PlateBand key="exeat">
      <SecHead eye="Exeats" k="sent" h="An exeat in three steps, and nobody unaccounted for." />
      <div style={sx("display:flex;justify-content:space-between")}>{strip}</div>
    </PlateBand>
  );
  const fees = (
    <WRow key="fees" eye="Boarding fees" k="fees" h="Boarding and tuition on one account."
      b="Boarding, tuck and outings bill to the family's account with tuition, in US dollars and ZiG. Guardians pay by EcoCash or bank transfer and see the balance in the portal."
      pic={<PhotoStory n="boys-reading-2.jpg" pos="47% 42%" cards={[[0, 80, <Tc portal="Parent"><ScCard name="fee_card" w={320} /></Tc>]]} w={620} h={460} />} />
  );
  return [board, exeat, fees];
}

/** government_sections' tile */
const GovTile = ({ t, d, children }: { t: string; d: string; children: ReactNode }) => (
  <div style={sx(`flex:1;border-radius:24px;background:${PLATE};padding:34px 34px 0;overflow:hidden;display:flex;flex-direction:column;gap:12px;min-height:520px`)}>
    <div style={sx(`font:600 26px/1.15 ${SANS};letter-spacing:-0.02em`)}>{t}</div><div style={sx(`font:400 16px/1.55 ${SANS};color:${INK2};max-width:440px`)}>{d}</div>
    <div style={sx("margin-top:20px")}>{children}</div>
  </div>
);

/** who_sections.government_sections: staff, big classes, fees and levies */
export function governmentSections(): ReactNode[] {
  const split = (
    <Wrap key="split">
      <SecHead eye="Staff" k="hr-payroll" h="Who pays whom, kept straight." />
      <div style={sx("display:flex;gap:24px")}>
        <GovTile t="Teachers the government pays" d="Their contracts, postings, leave and timetables live on Campus. Their pay does not.">
          <Tc portal="Administration"><GovStaffCard /></Tc>
        </GovTile>
        <GovTile t="Staff your SDC employs" d="Groundsmen, security, the office, the kitchen and any extra teachers are paid through Campus payroll.">
          <Tc portal="Administration"><SdcPayrunCard /></Tc>
        </GovTile>
      </div>
    </Wrap>
  );
  const big = (
    <WRow key="big" eye="Big classes" k="academics" h="A register for 52 pupils in under a minute."
      b="Mark everyone present, then tap the three who are not. It saves on the phone without internet and reaches the office when the connection returns."
      pic={<PhotoStory n="class-desks.jpg" pos="center 40%" cards={[[0, 60, <Tc portal="Teacher"><BigclassCard /></Tc>]]} w={620} h={470} />} flip />
  );
  const levy = (
    <WRow key="levy" eye="Fees and levies" k="fees" h="Bill tuition and levies the way your SDC sets them."
      b="Tuition, building and sports levies by form, in US dollars or ZiG. Every payment gets a receipt, and the SDC sees what has come in against what was billed."
      pic={
        <OnPlate w={620} h={470}>
          <At x={30} y={30}><Tc portal="Parent"><ScSite name="levy_card" w={280} /></Tc></At>
          <At x={326} y={196}><Tc portal="Administration"><ScSite name="collected_card" w={270} /></Tc></At>
        </OnPlate>
      } />
  );
  return [split, big, levy];
}

/** a site_cards.py card by its Python name (SC.<name>(w)) */
function ScSite({ name, w }: { name: string; w?: number }) {
  const C = SITE_CARDS[name];
  return <C w={w} />;
}

const STAGES: [string, number][] = [["Enquiries", 214], ["School tours", 176], ["Applications", 168], ["Entrance test", 142], ["Offers", 132], ["Accepted", 96]];

/** who_sections.private_sections: admissions, the board, the parent portal */
export function privateSections(): ReactNode[] {
  const bars = STAGES.map(([n, v]) => (
    <div key={n} style={sx("display:flex;align-items:center;gap:16px;padding:8px 0")}>
      <span style={sx(`width:130px;font:500 14.5px ${SANS};color:${INK2}`)}>{n}</span>
      <span style={sx("flex:1;height:34px;border-radius:10px;background:#e7ebf1;position:relative;overflow:hidden")}>
        <i style={sx(`position:absolute;left:0;top:0;bottom:0;width:${f1(v / 214 * 100)}%;background:${n === "Accepted" ? BLUE : "#8fb0f6"};border-radius:10px`)} />
        <b style={sx(`position:absolute;left:14px;top:0;bottom:0;display:flex;align-items:center;font:600 14px ${SANS};color:#fff;${NUM}`)}>{v}</b>
      </span>
    </div>
  ));
  const funnel = (
    <PlateBand key="funnel">
      <SecHead eye="Admissions" k="admissions" h="Fill 120 places from one list." />
      <div style={sx("display:flex;gap:56px;align-items:center")}>
        <div style={sx("flex:1")}>
          {bars}
          <div style={sx("display:flex;gap:10px;margin-top:16px")}><Status t="24 places left" kind="info" /><Status t="Deposits due 30 Oct" kind="warn" /></div>
        </div>
        <div style={sx("flex:none")}><Tc portal="Administration"><ScSite name="application_card" w={320} /></Tc></div>
      </div>
    </PlateBand>
  );
  const board = (
    <WRow key="board" eye="The board" k="insights" h="Take the board a report it can read in five minutes."
      b="Enrolment, fees, results and staffing for the term, from the records the school already keeps. Download it as a PDF for the meeting."
      pic={<PhotoStory n="seniors-lecture.jpg" pos="center 30%" cards={[[0, 60, <Tc portal="Administration"><BoardCard /></Tc>]]} w={620} h={480} />} />
  );
  const phone = (
    <WRow key="phone" eye="Parent portal" k="Parent" h="A portal for every family."
      b="Attendance, marks, fees and reports reach each family's phone that week, with a line to the class teacher."
      pic={<PhotoStory n="mother-phone.jpg" pos="65% center" cards={[[0, 8, <ParentPhone k={0.52} />]]} w={620} h={470} />} flip />
  );
  return [funnel, board, phone];
}

/** who_sections.mission_sections: day and boarding on one register, the report to the responsible authority */
export function missionSections(): ReactNode[] {
  const reg = (
    <WRow key="reg" eye="Day and boarding" k="t-mission" h="Day scholars and boarders on one register."
      b="One class register shows who goes home and who boards. Boarders also appear on their house's roll call, and fees bill by the type of place."
      pic={
        <OnPlate w={620} h={520}>
          <At x={24} y={30}><Tc portal="Teacher"><MixedRegisterCard w={300} /></Tc></At>
          <At x={336} y={240}><Tc portal="Administration"><ScSite name="rollcall_card" w={260} /></Tc></At>
        </OnPlate>
      } />
  );
  const doc = (
    <div style={sx("position:relative;width:620px;height:560px")}>
      <Ph n="girls-desks.jpg" w={500} h={560} pos="center 35%" r={24} extra="margin-left:120px" />
      <div style={sx("position:absolute;left:0;top:70px")}><AuthorityDoc w={380} /></div>
    </div>
  );
  const auth = (
    <WRow key="auth" eye="Responsible authority" k="insights" h="The report your church asks for, without retyping."
      b="Enrolment, results, finance and staffing for the responsible authority, built from the records the school keeps every day." pic={doc} flip />
  );
  return [reg, auth];
}

/** who_sections.SECTIONS: each school type's sections, by the type's key */
export const SECTIONS: Record<string, () => ReactNode[]> = {
  "t-day": daySections, "t-boarding": boardingSections, "t-government": governmentSections, "t-private": privateSections, "t-mission": missionSections,
};

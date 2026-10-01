/**
 * The bespoke Who we serve sections at phone width (mobile.m_day, m_boarding, m_government, m_private, m_mission).
 * Each returns its sections in order; the page puts 96px between them.
 */
import type { ReactNode } from "react";
import { Ph, Status, Tagged, Ticks, sx } from "./ds";
import { FeeCard, RegisterCard } from "./cards";
import { ApplicationCard, LevyCard } from "./site-cards";
import { ApproveCard, AuthorityDoc, BigclassCard, BoardCard, FamilyCard, GovStaffCard, MixedRegisterCard, RequestCard, SdcPayrunCard, SignoutCard } from "./who-sections";
import { ParentPhone, RollcallPhone } from "./phones";
import { MHead, MRow, P, Pad, PhoneOn, PhotoCard, PlateCard } from "./phone";
import { BLUE, CW, INK, INK2, MONO, MX, NUM, PLATE, SANS, pyFixed } from "@/lib/design";

/** mobile.m_day */
function mDay(): ReactNode[] {
  const steps: [string, string][] = [["06:50", "On the bus"], ["07:30", "Register"], ["08:06", "Absences home"], ["12:40", "Marks in"], ["16:10", "Home time"]];
  const levels: [string, string, string, string, string[]][] = [
    ["ecd-class.jpg", "center 40%", "ECD to Grade 7", "The class teacher marks one register and writes the report comment for each child.",
      ["Class registers", "A class teacher's comment on every report", "Parents of the youngest see each day"]],
    ["exam-blue.jpg", "center 40%", "Form 1 to Upper Sixth", "You mark registers by lesson, enter marks by subject, and every subject teacher adds a line to the report.",
      ["Registers by lesson", "Mark sheets by subject", "Exam classes in the holidays"]],
  ];
  return [
    <Pad key="day">
      <MHead eye="The school day" k="t-day" h="From the bus stop to home time, on one record." mb={20} />
      <div style={sx(`display:flex;gap:8px;overflow:hidden;margin-right:-${MX}px`)}>
        {steps.map(([t, h], i) => (
          <span key={t} style={sx(`flex:none;display:inline-flex;flex-direction:column;gap:2px;padding:10px 14px;border-radius:14px;${i === 1 ? `background:${INK};color:#fff` : `background:${PLATE};color:${INK2}`}`)}>
            <b style={sx(`font:500 12px ${MONO};color:${i === 1 ? "#bfd3fb" : BLUE}`)}>{t}</b><span style={sx(`font:600 14.5px ${SANS}`)}>{h}</span>
          </span>
        ))}
      </div>
      <div style={sx("margin-top:18px")}><P t="Ms Sibanda marks Form 3B on a tablet before the first lesson, with or without internet. The office sees it by 08:05." /></div>
      <div style={sx("margin-top:22px")}><PhotoCard photo="teacher-tablet.jpg" pos="center 25%" card={<Tagged tag="Teacher portal"><RegisterCard w={310} /></Tagged>} /></div>
    </Pad>,
    <MRow key="fam" eye="Fees by family" k="fees" h="One statement for every family."
      b="Brothers and sisters bill to one family account, with the sibling discount applied. Parents pay once, by EcoCash or at the bursary, and the payment lands on each child's account."
      pic={<PhotoCard photo="child-doorway.jpg" pos="center 30%" card={<Tagged tag="Parent portal"><FamilyCard w={326} /></Tagged>} />} />,
    <Pad key="levels">
      <MHead eye="Primary and secondary" k="academics" h="Run ECD and Upper Sixth from the same record." />
      <div style={sx("display:flex;flex-direction:column;gap:14px")}>
        {levels.map(([photo, pos, t, d, pts]) => (
          <div key={t} style={sx(`border-radius:22px;background:${PLATE};overflow:hidden`)}>
            <Ph n={photo} w={CW} h={200} pos={pos} r={0} />
            <div style={sx("padding:20px 22px 24px")}>
              <div style={sx(`font:600 22px/1.15 ${SANS};letter-spacing:-0.02em`)}>{t}</div>
              <div style={sx(`font:400 15px/1.55 ${SANS};color:${INK2};margin-top:8px`)}>{d}</div>
              <div style={sx("margin-top:12px")}><Ticks items={pts} c={INK2} size={14.5} /></div>
            </div>
          </div>
        ))}
      </div>
    </Pad>,
  ];
}

/** mobile.m_boarding */
function mBoarding(): ReactNode[] {
  const steps: [string, string, string, ReactNode][] = [
    ["1", "The guardian asks", "From the Parent portal, with who is collecting.", <Tagged key="a" tag="Parent portal"><RequestCard w={300} /></Tagged>],
    ["2", "The housemaster approves", "The guardian and the fee account are checked on the record.", <Tagged key="b" tag="Administration portal"><ApproveCard w={300} /></Tagged>],
    ["3", "Signed out", "The boarder leaves the house list until they are back.", <Tagged key="c" tag="Administration portal"><SignoutCard w={300} /></Tagged>],
  ];
  return [
    <MRow key="rc" eye="Roll call" k="boarding" h="Take roll call on your phone, house by house."
      b="Open your house at prep or lights out and tap each boarder in. Exeats and the sick bay are already marked, and anyone missing comes to the top. It works without internet."
      pic={<PhoneOn phone={<RollcallPhone k={0.6} />} photo="girls-smiling.jpg" pos="center 35%" h={560} />} />,
    <section key="exeat" style={sx(`background:${PLATE};padding:64px ${MX}px`)}>
      <MHead eye="Exeats" k="sent" h="An exeat in three steps, and nobody unaccounted for." />
      {steps.map(([n, t, d, c], i) => (
        <div key={n} style={sx(`display:flex;gap:14px;${i ? "padding-top:26px" : ""}`)}>
          <div style={sx("display:flex;flex-direction:column;align-items:center")}>
            <span style={sx(`width:30px;height:30px;border-radius:15px;background:${BLUE};color:#fff;display:flex;align-items:center;justify-content:center;font:600 14px ${SANS};flex:none`)}>{n}</span>
            {i < 2 ? <span style={sx("flex:1;width:1.5px;background:#c3c9d3;margin-top:6px")} /> : null}
          </div>
          <div style={sx("flex:1;padding-bottom:4px")}>
            <div style={sx(`font:600 18px ${SANS}`)}>{t}</div>
            <div style={sx(`font:400 14.5px/1.5 ${SANS};color:${INK2};margin-top:4px`)}>{d}</div>
            <div style={sx("margin-top:14px")}>{c}</div>
          </div>
        </div>
      ))}
    </section>,
    <MRow key="fees" eye="Boarding fees" k="fees" h="Boarding and tuition on one account."
      b="Boarding, tuck and outings bill to the family's account with tuition, in US dollars and ZiG. Guardians pay by EcoCash or bank transfer and see the balance in the portal."
      pic={<PhotoCard photo="boys-reading-2.jpg" pos="47% 42%" card={<Tagged tag="Parent portal"><FeeCard w={320} /></Tagged>} />} />,
  ];
}

/** mobile.m_government */
function mGovernment(): ReactNode[] {
  const tile = (t: string, d: string, c: ReactNode) => (
    <div key={t} style={sx(`border-radius:22px;background:${PLATE};padding:24px 20px 24px;display:flex;flex-direction:column;gap:10px`)}>
      <div style={sx(`font:600 22px/1.15 ${SANS};letter-spacing:-0.02em`)}>{t}</div>
      <div style={sx(`font:400 15px/1.55 ${SANS};color:${INK2}`)}>{d}</div>
      <div style={sx("margin-top:12px")}>{c}</div>
    </div>
  );
  return [
    <Pad key="split">
      <MHead eye="Staff" k="hr-payroll" h="Who pays whom, kept straight." />
      <div style={sx("display:flex;flex-direction:column;gap:14px")}>
        {tile("Teachers the government pays", "Their contracts, postings, leave and timetables live on Campus. Their pay does not.", <Tagged tag="Administration portal"><GovStaffCard w={310} /></Tagged>)}
        {tile("Staff your SDC employs", "Groundsmen, security, the office, the kitchen and any extra teachers are paid through Campus payroll.", <Tagged tag="Administration portal"><SdcPayrunCard w={310} /></Tagged>)}
      </div>
    </Pad>,
    <MRow key="big" eye="Big classes" k="academics" h="A register for 52 pupils in under a minute."
      b="Mark everyone present, then tap the three who are not. It saves on the phone without internet and reaches the office when the connection returns."
      pic={<PhotoCard photo="class-desks.jpg" pos="center 40%" card={<Tagged tag="Teacher portal"><BigclassCard w={310} /></Tagged>} />} />,
    <MRow key="levy" eye="Fees and levies" k="fees" h="Bill tuition and levies the way your SDC sets them."
      b="Tuition, building and sports levies by form, in US dollars or ZiG. Every payment gets a receipt, and the SDC sees what has come in against what was billed."
      pic={<PlateCard card={<Tagged tag="Parent portal"><LevyCard w={300} /></Tagged>} />} />,
  ];
}

/** mobile.m_private */
function mPrivate(): ReactNode[] {
  const stages: [string, number][] = [["Enquiries", 214], ["School tours", 176], ["Applications", 168], ["Entrance test", 142], ["Offers", 132], ["Accepted", 96]];
  return [
    <section key="funnel" style={sx(`background:${PLATE};padding:64px ${MX}px`)}>
      <MHead eye="Admissions" k="admissions" h="Fill 120 places from one list." mb={20} />
      {stages.map(([n, v]) => (
        <div key={n} style={sx("padding:6px 0")}>
          <div style={sx(`font:500 13.5px ${SANS};color:${INK2};margin-bottom:5px`)}>{n}</div>
          <span style={sx("display:block;height:30px;border-radius:9px;background:#e7ebf1;position:relative;overflow:hidden")}>
            <i style={sx(`position:absolute;left:0;top:0;bottom:0;width:${pyFixed(v / 214 * 100, 1)}%;background:${n === "Accepted" ? BLUE : "#8fb0f6"};border-radius:9px`)} />
            <b style={sx(`position:absolute;left:12px;top:0;bottom:0;display:flex;align-items:center;font:600 13.5px ${SANS};color:#fff;${NUM}`)}>{v}</b>
          </span>
        </div>
      ))}
      <div style={sx("display:flex;gap:8px;margin-top:14px")}><Status t="24 places left" kind="info" /><Status t="Deposits due 30 Oct" kind="warn" /></div>
      <div style={sx("margin-top:24px;display:flex;justify-content:center")}><Tagged tag="Administration portal"><ApplicationCard w={320} /></Tagged></div>
    </section>,
    <MRow key="board" eye="The board" k="insights" h="Take the board a report it can read in five minutes."
      b="Enrolment, fees, results and staffing for the term, from the records the school already keeps. Download it as a PDF for the meeting."
      pic={<PhotoCard photo="seniors-lecture.jpg" pos="center 30%" card={<Tagged tag="Administration portal"><BoardCard w={320} /></Tagged>} />} />,
    <MRow key="phone" eye="Parent portal" k="Parent" h="A portal for every family."
      b="Attendance, marks, fees and reports reach each family's phone that week, with a line to the class teacher."
      pic={<PhoneOn phone={<ParentPhone k={0.6} />} photo="mother-phone.jpg" pos="65% center" h={560} />} />,
  ];
}

/** mobile.m_mission */
function mMission(): ReactNode[] {
  return [
    <MRow key="reg" eye="Day and boarding" k="t-mission" h="Day scholars and boarders on one register."
      b="One class register shows who goes home and who boards. Boarders also appear on their house's roll call, and fees bill by the type of place."
      pic={<PlateCard card={<Tagged tag="Teacher portal"><MixedRegisterCard w={310} /></Tagged>} />} />,
    <MRow key="auth" eye="Responsible authority" k="insights" h="The report your church asks for, without retyping."
      b="Enrolment, results, finance and staffing for the responsible authority, built from the records the school keeps every day."
      pic={<div style={sx("position:relative")}><Ph n="girls-desks.jpg" w={CW} h={220} pos="center 35%" r={20} /><div style={sx("margin:-80px 10px 0;position:relative")}><AuthorityDoc w={330} /></div></div>} />,
  ];
}

export const M_SECTIONS: Record<string, () => ReactNode[]> = { "t-day": mDay, "t-boarding": mBoarding, "t-government": mGovernment, "t-private": mPrivate, "t-mission": mMission };

/**
 * The product cards: static pictures of Campus with the school's fixed figures (ui.py, hero.py, landing.py).
 */
import { Card, Chead, Fig, Ic, Lab, Pmark, Rowl, Status, sx } from "./ds";
import { BLUE, CAMPUS, INK2, MUTED, OK, SANS, WARN, WARNS } from "@/lib/design";
import { FORM3B, MARKS } from "@/content/world";

const MARK = { P: ["Present", "ok"], A: ["Absent", "bad"], L: ["Late", "warn"] } as const;

/** ui.register_card: Form 3B's register at 07:42, saved on the tablet */
export function RegisterCard({ w = 300, offline = true }: { w?: number; offline?: boolean }) {
  return (
    <Card w={w}>
      <Chead icon="book-6" title="Form 3B register" meta="07:42" />
      {offline ? (
        <div style={sx(`display:flex;align-items:center;gap:8px;margin:0 0 10px;padding:8px 10px;border-radius:12px;background:${WARNS};font-size:12px;color:${WARN}`)}>
          <Ic n="wifi-off" s={14} c={WARN} />Saved on this tablet · syncs when online
        </div>
      ) : null}
      {FORM3B.slice(0, 5).map(([n, m]) => (
        <div key={n} style={sx("display:flex;align-items:center;gap:10px;padding:7px 0;border-top:1px solid #edeff2;font-size:13px")}>
          <span style={sx("flex:1")}>{n}</span><Status t={MARK[m][0]} kind={MARK[m][1]} />
        </div>
      ))}
      <div style={sx(`display:flex;justify-content:space-between;padding-top:10px;border-top:1px solid #edeff2;font-size:12.5px;color:${MUTED}`)}>
        <span>36 present · 1 late · 1 absent</span><span>38</span>
      </div>
    </Card>
  );
}

/** ui.sync_card */
export const SyncCard = ({ w = 280 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="refresh-2" title="Synced to the school" meta="08:05" hue={OK} />
    <Rowl a="Registers" b="3 from Block C" top={false} /><Rowl a="Marks" b="38 entries" /><Rowl a="Receipts" b="2 from the bursary" />
    <div style={sx("margin-top:8px")}><Status t="The office has the same figures now" kind="ok" /></div>
  </Card>
);

/** ui.marks_card: Mathematics test 2, recorded once */
export const MarksCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="file-check" title="Mathematics · test 2" meta="24 Sep" />
    <Rowl a="Tanaka Moyo" b="71%" top={false} bold /><Rowl a="Tendai Chirwa" b="58%" /><Rowl a="Ruvimbo Gumbo" b="77%" />
    <Rowl a="Class average" b="64%" c={MUTED} />
    <div style={sx(`margin-top:8px;font-size:12px;color:${MUTED}`)}>Recorded once by Ms Sibanda</div>
  </Card>
);

/** ui.fee_card: Tanaka's Term 3 account */
export const FeeCard = ({ w = 320 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="wallet-3" title="Tanaka Moyo · fees" meta="Term 3" />
    <Rowl a="Term fee" b="US$1,250.00" top={false} /><Rowl a="EcoCash, 14 Sep" b="−US$500.00" c={OK} /><Rowl a="Bank transfer, 22 Sep" b="−US$330.00" c={OK} />
    <Rowl a="Balance" b="US$420.00" bold />
    <div style={sx("display:flex;gap:8px;margin-top:8px")}><Status t="Due Fri 16 Oct" kind="warn" /><Status t="R-2026-18824" kind="mute" /></div>
  </Card>
);

/** ui.report_card */
export const ReportCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="file-check" title="Term 3 report · Tanaka" meta="Draft" />
    {MARKS.slice(0, 4).map(([n, m], i) => <Rowl key={n} a={n} b={`${m}%`} top={i > 0} />)}
    <div style={sx("margin-top:8px")}><Status t="Ready when the term closes" kind="campus" /></div>
  </Card>
);

/** ui.head_card: the Head's view */
export const HeadCard = ({ w = 300 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="chart-bar" title="The Head’s view" meta="07:58" hue={BLUE} />
    <div style={sx("display:grid;grid-template-columns:1fr 1fr;gap:10px")}>
      <div><Lab t="Attendance" /><div style={sx("margin-top:6px")}><Fig v="96.4%" s={22} /></div></div>
      <div><Lab t="Fees collected" /><div style={sx("margin-top:6px")}><Fig v="70.3%" s={22} /></div></div>
    </div>
    <div style={sx(`margin-top:10px;font-size:12px;color:${MUTED}`)}>Mathematics, Form 3: average up 6 points</div>
  </Card>
);

/** landing.receipts_card */
export const ReceiptsCard = ({ w = 240 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="bill" title="Receipts" meta="Today" hue={OK} />
    <Rowl a="EcoCash · 9" b="US$3,410.00" top={false} /><Rowl a="Bank · 2" b="US$1,410.00" /><Rowl a="Cash · 1" b="ZiG 2,600.00" />
    <div style={sx("margin-top:8px")}><Status t="Matched to pupils" kind="ok" /></div>
  </Card>
);

/** landing.message_card */
export const MessageCard = ({ w = 220 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="message-3" title="Ms Sibanda" meta="16:10" hue={BLUE} />
    <div style={sx(`font-size:13px;line-height:1.5;color:${INK2}`)}>Tanaka did well on test 2. Keep up the algebra practice at home.</div>
    <div style={sx("margin-top:10px;display:flex;justify-content:flex-end")}><Status t="Reply" kind="info" /></div>
  </Card>
);

/** landing.week_card */
export const WeekCard = ({ w = 262 }: { w?: number }) => (
  <Card w={w}>
    <Chead icon="home-3" title="Tanaka · this week" meta="Fri" hue={CAMPUS} />
    <Rowl a="Present" b="5 of 5 days" top={false} /><Rowl a="Mathematics test 2" b="71%" /><Rowl a="Balance, due 16 Oct" b="US$420.00" c={WARN} />
  </Card>
);

/** hero.att_card: attendance today */
export const AttCard = ({ w = 230 }: { w?: number }) => (
  <Card w={w} pad={18}>
    <Lab t="Attendance today" /><div style={sx("margin-top:8px")}><Fig v="96.4%" s={32} /></div>
    <div style={sx(`font:400 13px ${SANS};color:${MUTED};margin-top:6px`)}>1,099 of 1,140 pupils</div>
    <div style={sx("margin-top:10px")}><Status t="+0.8 on last week" kind="ok" /></div>
  </Card>
);

/** hero.note_card: the note to Rudo Moyo */
export const NoteCard = ({ w = 330 }: { w?: number }) => (
  <Card w={w} pad={16}>
    <div style={sx("display:flex;align-items:center;gap:10px")}>
      <Pmark s={30} r={8} />
      <div style={sx("flex:1;min-width:0")}>
        <div style={sx(`font:600 14px ${SANS}`)}>To Rudo Moyo</div>
        <div style={sx(`font:400 12.5px ${SANS};color:${MUTED}`)}>16:10 · from Ms Sibanda</div>
      </div>
    </div>
    <div style={sx(`font:400 14px/1.45 ${SANS};color:${INK2};margin-top:10px`)}>Tanaka scored 71% in Mathematics test 2. The class average was 64%.</div>
  </Card>
);

/**
 * The phones at true device size (pages.py status_bar, device, parent_app, parent_phone; who_sections.py rollcall_app,
 * rollcall_phone) and the Form 3B timetable in edit mode (pages.timetable_card). The screens are 393 x 852 points, set
 * in Inter at system sizes, and scaled down only where they are placed.
 */
import type { ReactNode } from "react";
import { Art } from "./art";
import { Card, Ic, Pmark, Scaled, sx } from "./ds";
import { BAD, BADS, BLUE, CAMPUS, INK, INK2, LINE, MONO, MUTED, OK, OKS, SANS, UI, WARN, WARNS, pyRound } from "@/lib/design";

/** pages.SCR_W, SCR_H, BEZ: the screen in points and the band around it */
const SCR_W = 393, SCR_H = 852, BEZ = 12;

/** Python's f"{x:.2f}": an exact half goes to the even neighbour (90.625 -> 90.62), where toFixed rounds up */
const f2 = (x: number) => {
  const s = x * 100;
  return Math.abs(s % 1) === 0.5 ? (pyRound(s) / 100).toFixed(2) : x.toFixed(2);
};

/** pages.status_bar: the iOS status bar on a 393 pt iPhone 15 Pro, the time and the three glyphs centred on y = 31 */
export function StatusBar({ t = "16:10", dark = false }: { t?: string; dark?: boolean }) {
  const c = dark ? "#ffffff" : "#000000";
  const cy = 31.0;
  return (
    <div style={sx("position:relative;height:54px")}>
      <div style={sx(`position:absolute;left:16px;width:113px;top:${(cy - 11).toFixed(1)}px;height:22px;display:flex;align-items:center;justify-content:center;font:600 17px/22px ${UI};letter-spacing:-0.4px;color:${c};font-feature-settings:'tnum' 0,'cv11' 1`)}>{t}</div>
      <div style={sx(`position:absolute;left:264.3px;width:113px;top:${(cy - 6.5).toFixed(1)}px;height:13px;display:flex;align-items:center;justify-content:center;gap:0`)}>
        <Art k={`status:cell:${c}`} /><Art k={`status:wifi:${c}`} /><Art k={`status:batt:${c}`} />
      </div>
    </div>
  );
}

/** pages.device: iPhone 15 Pro proportions, the titanium band, the buttons, the Dynamic Island and the home indicator */
export function Device({ children }: { children?: ReactNode }) {
  const w = SCR_W + 2 * BEZ, h = SCR_H + 2 * BEZ;
  const ti = "linear-gradient(90deg,#3d4045 0%,#8a8d93 6%,#55585e 14%,#3a3d42 50%,#55585e 86%,#8f9298 94%,#3d4045 100%)";
  const btn = (side: "left" | "right", top: number, hgt: number) => (
    <span style={sx(`position:absolute;${side}:-3px;top:${top}px;width:4px;height:${hgt}px;border-radius:${side === "left" ? "2px 0 0 2px" : "0 2px 2px 0"};background:linear-gradient(90deg,#55585e,#9a9da3 50%,#55585e);box-shadow:0 0 0 0.5px rgba(0,0,0,.35)`)} />
  );
  const breaks: [string, number][] = [["left", 92], ["right", 92], ["left", h - 98], ["right", h - 98]];
  return (
    <div style={sx(`position:relative;width:${w}px;height:${h}px;flex:none`)}>
      {btn("left", 168, 30)}{btn("left", 230, 60)}{btn("left", 302, 60)}{btn("right", 252, 96)}
      <div style={sx(`position:absolute;inset:0;border-radius:66px;background:${ti};box-shadow:inset 0 0 0 1px rgba(255,255,255,.25)`)} />
      {breaks.map(([s, t], i) => <span key={i} style={sx(`position:absolute;${s}:0;top:${t}px;width:3px;height:5px;background:#9a9da3;opacity:.7`)} />)}
      <div style={sx("position:absolute;inset:4px;border-radius:62px;background:#050506")} />
      <div style={sx(`position:absolute;left:${BEZ}px;top:${BEZ}px;width:${SCR_W}px;height:${SCR_H}px;border-radius:55px;overflow:hidden;background:#f2f3f6`)}>
        {children}
        <span style={sx("position:absolute;left:50%;top:11px;transform:translateX(-50%);width:126px;height:37px;border-radius:19px;background:#000")}>
          <i style={sx("position:absolute;right:13px;top:11.5px;width:14px;height:14px;border-radius:7px;background:radial-gradient(circle at 40% 38%,#3b4b6e 0 18%,#151b2b 34%,#06080d 70%);box-shadow:0 0 0 1px #0d1018")} />
        </span>
        <span style={sx("position:absolute;left:50%;bottom:8px;transform:translateX(-50%);width:139px;height:5px;border-radius:3px;background:#000")} />
      </div>
    </div>
  );
}

// ---- the Parent portal on Rudo Moyo's phone ------------------------------------------------------------------
const PCard = ({ pad = "14px 16px", children }: { pad?: string; children?: ReactNode }) =>
  <div style={sx(`background:#fff;border-radius:16px;padding:${pad}`)}>{children}</div>;

const Lead = ({ icn, bg, fg, s = 34 }: { icn: string; bg: string; fg: string; s?: number }) => (
  <span style={sx(`width:${s}px;height:${s}px;border-radius:10px;background:${bg};display:flex;align-items:center;justify-content:center;flex:none`)}><Ic n={icn} s={18} c={fg} /></span>
);

const Sec = ({ t, r = "" }: { t: string; r?: string }) => (
  <div style={sx("display:flex;justify-content:space-between;align-items:baseline;margin:22px 4px 8px")}>
    <span style={sx(`font:600 15px ${UI};color:${INK}`)}>{t}</span><span style={sx(`font:400 15px ${UI};color:${BLUE}`)}>{r}</span>
  </div>
);

const DAYS: [string, "ok" | "late" | "today"][] = [["M", "ok"], ["T", "ok"], ["W", "late"], ["T", "ok"], ["F", "today"]];
const PMARKS: [string, string, string, boolean][] = [["Mathematics", "Test 2", "71%", true], ["English", "Essay", "68%", false], ["Combined Science", "Practical", "74%", false]];
const TABS: [string, string][] = [["home-3", "Home"], ["chart-bar", "Marks"], ["wallet-3", "Fees"], ["message-3", "Messages"], ["user-3", "Account"]];

/** pages.parent_app: the Parent portal on Rudo Moyo's phone at 16:10 on Thursday 1 October */
export function ParentApp() {
  const strip = DAYS.map(([d, s_], i) => (
    <div key={i} style={sx("flex:1;display:flex;flex-direction:column;align-items:center;gap:6px")}>
      <span style={sx(`font:400 12px ${UI};color:${MUTED}`)}>{d}</span>
      <span style={sx(`width:28px;height:28px;border-radius:14px;display:flex;align-items:center;justify-content:center;background:${s_ === "ok" ? OKS : (s_ === "late" ? WARNS : "#e8effd")};box-shadow:${s_ === "today" ? "inset 0 0 0 1.5px " + BLUE : "none"}`)}>
        <Ic n={s_ !== "late" ? "check-line" : "time-line"} s={14} c={s_ === "ok" ? OK : (s_ === "late" ? WARN : BLUE)} />
      </span>
    </div>
  ));
  const att = (
    <PCard>
      <div style={sx("display:flex;align-items:center;gap:12px")}>
        <Lead icn="check-circle" bg={OKS} fg={OK} />
        <div style={sx("flex:1")}><div style={sx(`font:600 15px ${UI}`)}>Present today</div><div style={sx(`font:400 13px ${UI};color:${MUTED};margin-top:1px`)}>Marked at 07:42 by Ms Sibanda</div></div>
      </div>
      <div style={sx("display:flex;margin-top:14px;padding-top:12px;border-top:1px solid #f0f1f4")}>{strip}</div>
    </PCard>
  );
  const mk = PMARKS.map(([n, t, v, isNew], i) => (
    <div key={n} style={sx(`display:flex;align-items:center;gap:12px;padding:11px 0;${i ? "border-top:1px solid #f0f1f4;" : ""}`)}>
      <div style={sx("flex:1")}><div style={sx(`font:500 15px ${UI};color:${INK}`)}>{n}</div><div style={sx(`font:400 13px ${UI};color:${MUTED};margin-top:1px`)}>{t}{isNew ? " · class average 64%" : ""}</div></div>
      {isNew ? <span style={sx(`height:20px;padding:0 7px;border-radius:10px;background:${BLUE};color:#fff;font:600 11px ${UI};display:inline-flex;align-items:center`)}>New</span> : null}
      <span style={sx(`font:600 15px ${UI};color:${INK};width:40px;text-align:right`)}>{v}</span>
    </div>
  ));
  const fees = (
    <PCard>
      <div style={sx("display:flex;justify-content:space-between;align-items:baseline")}><span style={sx(`font:400 13px ${UI};color:${MUTED}`)}>Term 3 balance</span>
        <span style={sx(`font:500 13px ${UI};color:${WARN}`)}>Due Fri 16 Oct</span></div>
      <div style={sx(`font:600 28px ${UI};letter-spacing:-0.02em;margin-top:2px`)}>US$420.00</div>
      <div style={sx("height:6px;border-radius:3px;background:#eef0f3;margin-top:10px;overflow:hidden")}><div style={sx(`width:66%;height:100%;background:${OK}`)} /></div>
      <div style={sx(`font:400 12px ${UI};color:${MUTED};margin-top:6px`)}>US$830 of US$1,250 paid</div>
      <div style={sx(`margin-top:14px;height:46px;border-radius:12px;background:${BLUE};color:#fff;display:flex;align-items:center;justify-content:center;gap:8px;font:600 16px ${UI}`)}>
        <Ic n="wallet-3" s={17} c="#ffffff" />Pay with EcoCash
      </div>
    </PCard>
  );
  const msg = (
    <PCard>
      <div style={sx("display:flex;gap:12px")}>
        <Lead icn="message-3" bg="#efeaff" fg={CAMPUS} />
        <div style={sx("flex:1;min-width:0")}>
          <div style={sx("display:flex;justify-content:space-between")}><span style={sx(`font:600 15px ${UI}`)}>Ms Sibanda</span>
            <span style={sx(`font:400 13px ${UI};color:${MUTED}`)}>14:05</span></div>
          <div style={sx(`font:400 14px/1.4 ${UI};color:${INK2};margin-top:2px`)}>Tanaka did well on test 2. Keep up the practice on algebra this week.</div>
        </div>
      </div>
    </PCard>
  );
  const badge = (
    <span style={sx(`position:absolute;left:15px;top:-5px;min-width:18px;height:18px;padding:0 5px;box-sizing:border-box;border-radius:9px;background:#ff3b30;color:#fff;font:600 12px/18px ${UI};text-align:center`)}>2</span>
  );
  const tabs = TABS.map(([n, t], i) => (
    <div key={n} style={sx(`flex:1;display:flex;flex-direction:column;align-items:center;gap:4px;font:500 10px ${UI};color:${i === 0 ? BLUE : "#8e8e93"}`)}>
      <span style={sx("position:relative;display:block;width:24px;height:24px")}><Ic n={n} s={24} c={i === 0 ? BLUE : "#8e8e93"} />{n === "message-3" ? badge : null}</span>{t}
    </div>
  ));
  return (
    <div style={sx(`position:relative;width:${SCR_W}px;height:${SCR_H}px;background:#f2f3f6;font-family:${SANS};color:${INK};overflow:hidden`)}>
      <StatusBar />
      <div style={sx("padding:4px 16px 0")}>
        <div style={sx("display:flex;align-items:center;justify-content:space-between;height:44px")}>
          <div style={sx("display:flex;align-items:center;gap:9px")}><Pmark s={28} r={8} /><span style={sx(`font:600 17px ${UI}`)}>Parent portal</span></div>
          <span style={sx("position:relative;width:36px;height:36px;border-radius:18px;background:#fff;display:flex;align-items:center;justify-content:center")}>
            <Ic n="notification" s={18} c={INK} />
            <i style={sx(`position:absolute;right:8px;top:8px;width:8px;height:8px;border-radius:4px;background:${BAD};box-shadow:0 0 0 2px #fff`)} />
          </span>
        </div>
        <div style={sx(`font:600 28px ${UI};letter-spacing:-0.025em;margin:10px 4px 12px`)}>Good afternoon, Rudo</div>
        <div style={sx("display:flex;align-items:center;gap:12px;padding:12px 14px;border-radius:16px;background:#fff")}>
          <span style={sx(`width:40px;height:40px;border-radius:20px;background:#e8effd;color:${BLUE};display:flex;align-items:center;justify-content:center;font:600 15px ${UI}`)}>TM</span>
          <div style={sx("flex:1")}><div style={sx(`font:600 16px ${UI}`)}>Tanaka Moyo</div><div style={sx(`font:400 13px ${UI};color:${MUTED};margin-top:1px`)}>Form 3B · Tsavo House</div></div>
          <span style={sx(`font:400 15px ${UI};color:${BLUE};display:flex;align-items:center;gap:2px`)}>Switch<Ic n="down-line" s={13} c={BLUE} /></span>
        </div>
        <Sec t="Today" r="Thu 1 Oct" />{att}
        <Sec t="Marks" r="See all" /><PCard pad="4px 16px">{mk}</PCard>
        <Sec t="Fees" r="Statement" />{fees}
        <Sec t="Messages" r="" />{msg}
      </div>
      <div style={sx("position:absolute;left:0;right:0;bottom:0;height:83px;background:#f9f9fb;box-shadow:0 -0.5px 0 rgba(0,0,0,.18);display:flex;align-items:flex-start;padding:7px 4px 0;box-sizing:border-box")}>{tabs}</div>
    </div>
  );
}

/** pages.parent_phone: the Parent portal in the device, scaled, with room for the side buttons */
export function ParentPhone({ k = 0.5 }: { k?: number }) {
  const w = SCR_W + 2 * BEZ, h = SCR_H + 2 * BEZ;
  return (
    <div style={sx("filter:drop-shadow(0 16px 22px rgba(11,12,20,.32))")}>
      <Scaled w={pyRound((w + 12) * k)} h={pyRound(h * k)} k={k}>
        <div style={sx("padding:0 6px")}><Device><ParentApp /></Device></div>
      </Scaled>
    </div>
  );
}

// ---- the Form 3B timetable ----------------------------------------------------------------------------------
const TT_DAYS = ["Mon", "Tue", "Wed", "Thu", "Fri"];
const PERIODS: [string, string[]][] = [["07:30", ["Maths", "English", "Maths", "Shona", "Science"]], ["08:40", ["Science", "Maths", "History", "Maths", "English"]],
  ["10:10", ["Shona", "Geography", "English", "Science", "Maths"]], ["11:20", ["English", "Science", "Shona", "Geography", "Sport"]]];

/** pages.timetable_card: the Form 3B timetable in edit mode: week switcher, a lesson being moved, undo and publish */
export function TimetableCard({ w = 520 }: { w?: number }) {
  const grip = (
    <span style={sx("display:inline-grid;grid-template-columns:repeat(2,3px);gap:2px;margin-right:5px;vertical-align:middle")}>
      {[0, 1, 2, 3, 4, 5].map((i) => <i key={i} style={sx(`width:3px;height:3px;border-radius:2px;background:${BLUE}`)} />)}
    </span>
  );
  const cells = PERIODS.map(([t, subs]) => [
    <div key={t} style={sx(`font:400 12px ${MONO};color:${MUTED};padding-top:10px`)}>{t}</div>,
    ...subs.map((s_, j) => {
      const hot = t === "10:10" && j === 2;
      const drop = t === "11:20" && j === 2;
      const bg = hot ? "#ffffff" : (!drop ? "#f6f7f9" : "#f8faff");
      const sh = hot ? `0 0 0 1.5px ${BLUE},0 10px 18px -8px rgba(37,99,235,.45)` : (drop ? "inset 0 0 0 1.5px #9db8f5" : "inset 0 0 0 1px #eceef2");
      const style = hot ? "transform:translate(4px,-3px) rotate(-1.5deg);" : "";
      const border = drop ? "border:1.5px dashed #9db8f5;" : "";
      const sub = hot ? "Room 12 now" : (drop ? "Swap here" : (s_ === "Science" ? "Lab" : "3B"));
      return (
        <div key={`${t}-${j}`} style={sx(`position:relative;height:44px;border-radius:9px;padding:6px 8px;box-sizing:border-box;background:${bg};box-shadow:${sh};${border}${style}font:500 12.5px ${SANS};color:${INK};white-space:nowrap`)}>
          {hot ? <>{grip}{s_}</> : s_}
          <div style={sx(`font:400 10.5px ${SANS};color:${hot || drop ? BLUE : MUTED};margin-top:1px`)}>{sub}</div>
        </div>
      );
    }),
  ]);
  return (
    <Card w={w} pad={18}>
      <div style={sx("display:flex;align-items:center;gap:10px;margin-bottom:12px")}>
        <Pmark s={26} r={7} />
        <div style={sx("flex:1")}><div style={sx(`font:600 14.5px ${SANS}`)}>Timetable</div>
          <div style={sx(`font:400 12px ${SANS};color:${MUTED}`)}>Term 3 · editing</div></div>
        <div style={sx(`display:inline-flex;align-items:center;height:30px;border-radius:9px;box-shadow:inset 0 0 0 1px ${LINE}`)}>
          <span style={sx("width:28px;display:flex;justify-content:center")}><Ic n="left-line" s={13} c={INK2} /></span>
          <span style={sx(`font:500 12.5px ${SANS};padding:0 4px`)}>Week 4</span>
          <span style={sx("width:28px;display:flex;justify-content:center")}><Ic n="right-line" s={13} c={INK2} /></span>
        </div>
      </div>
      <div style={sx("margin-bottom:12px")}>
        <div style={sx("display:inline-flex;height:30px;padding:3px;border-radius:9px;background:#f1f3f6;box-sizing:border-box")}>
          <span style={sx(`padding:0 10px;border-radius:7px;background:#fff;box-shadow:0 1px 2px rgba(11,12,20,.12);font:500 12px ${SANS};display:flex;align-items:center`)}>Form 3B</span>
          <span style={sx(`padding:0 10px;font:500 12px ${SANS};color:${MUTED};display:flex;align-items:center`)}>Teachers</span>
          <span style={sx(`padding:0 10px;font:500 12px ${SANS};color:${MUTED};display:flex;align-items:center`)}>Rooms</span>
        </div>
      </div>
      <div style={sx("display:grid;grid-template-columns:44px repeat(5,1fr);gap:6px")}>
        <div />
        {TT_DAYS.map((d) => <div key={d} style={sx(`font:500 12px ${SANS};color:${MUTED};padding:0 0 8px`)}>{d}</div>)}
        {cells}
      </div>
      <div style={sx(`display:flex;align-items:center;gap:8px;margin-top:14px;padding-top:12px;border-top:1px solid ${LINE}`)}>
        <span style={sx(`font:400 12.5px ${SANS};color:${MUTED};flex:1`)}>1 unpublished change</span>
        <span style={sx(`height:32px;padding:0 12px;border-radius:9px;box-shadow:inset 0 0 0 1px ${LINE};display:inline-flex;align-items:center;gap:6px;font:500 12.5px ${SANS}`)}><Ic n="back-2-line" s={13} c={INK2} />Undo</span>
        <span style={sx(`height:32px;padding:0 12px;border-radius:9px;background:${BLUE};color:#fff;display:inline-flex;align-items:center;gap:6px;font:600 12.5px ${SANS}`)}><Ic n="check-line" s={13} c="#fff" />Publish changes</span>
      </div>
    </Card>
  );
}

// ---- roll call on the housemaster's phone ---------------------------------------------------------------------
type Board = "in" | "exeat" | "sick" | "miss" | "todo";
const BOARDERS: [string, string, string, Board][] = [["TZ", "Tafadzwa Zhou", "Room 6 · last seen at prep 19:40", "miss"], ["KM", "Kudzai Mhlanga", "Room 2 · back Sun 17:00", "exeat"],
  ["TM", "Tanaka Moyo", "Room 4", "in"], ["NC", "Nyasha Chari", "Room 4", "in"], ["RG", "Rufaro Gumbo", "Sick bay since 15:20", "sick"],
  ["TS", "Tinashe Sithole", "Room 5", "in"], ["BM", "Blessing Mutasa", "Room 5", "in"]];

const Pill = ({ t, fg, bg, icn }: { t: string; fg: string; bg: string; icn?: string }) => (
  <span style={sx(`display:inline-flex;align-items:center;gap:4px;height:30px;padding:0 11px;border-radius:15px;background:${bg};color:${fg};font:600 13px ${UI};white-space:nowrap`)}>
    {icn ? <Ic n={icn} s={14} c={fg} /> : null}{t}
  </span>
);

const RIGHT: Record<Board, ReactNode> = {
  in: <Pill t="In" fg={OK} bg={OKS} icn="check-line" />, exeat: <Pill t="Exeat" fg={CAMPUS} bg="#efeaff" />, sick: <Pill t="Sick bay" fg={WARN} bg={WARNS} />,
  miss: <Pill t="Mark in" fg="#fff" bg={BAD} />, todo: <Pill t="Tap to mark" fg={BLUE} bg="#e8effd" />,
};

/** who_sections.rollcall_app: lights out in Tsavo House at 21:04, on the housemaster's phone */
export function RollcallApp() {
  const rows = BOARDERS.map(([ini, n, sub, st], i) => {
    const [avBg, avFg] = st === "miss" ? [BADS, BAD] : ["#eef0f3", INK2];
    return (
      <div key={ini} style={sx(`display:flex;align-items:center;gap:12px;padding:11px 16px;${i ? "border-top:1px solid #f0f1f4;" : ""}`)}>
        <span style={sx(`width:38px;height:38px;border-radius:19px;background:${avBg};color:${avFg};display:flex;align-items:center;justify-content:center;font:600 13px ${UI};flex:none`)}>{ini}</span>
        <div style={sx("flex:1;min-width:0")}><div style={sx(`font:500 16px ${UI};color:${INK}`)}>{n}</div><div style={sx(`font:400 13px ${UI};color:${st === "miss" ? BAD : MUTED};margin-top:1px`)}>{sub}</div></div>
        {RIGHT[st]}
      </div>
    );
  });
  const seg = (v: number, c: string) => <i key={c} style={sx(`width:${f2(v / 64 * 100)}%;background:${c}`)} />;
  const legend: [string, string][] = [["58 in", BLUE], ["4 exeat", CAMPUS], ["1 sick bay", WARN], ["1 missing", BAD]];
  const summary = (
    <div style={sx("background:#fff;border-radius:16px;padding:14px 16px")}>
      <div style={sx("display:flex;align-items:baseline;gap:6px")}><span style={sx(`font:600 32px ${UI};letter-spacing:-0.02em`)}>63</span>
        <span style={sx(`font:400 15px ${UI};color:${MUTED}`)}>of 64 accounted for</span></div>
      <div style={sx("display:flex;height:8px;border-radius:4px;overflow:hidden;background:#eef0f3;margin:10px 0 12px")}>{seg(58, BLUE)}{seg(4, CAMPUS)}{seg(1, WARN)}{seg(1, BAD)}</div>
      <div style={sx(`display:flex;justify-content:space-between;font:400 13px ${UI};color:${INK2}`)}>
        {legend.map(([t, c]) => <span key={t} style={sx("display:flex;align-items:center;gap:6px")}><i style={sx(`width:8px;height:8px;border-radius:4px;background:${c}`)} />{t}</span>)}
      </div>
    </div>
  );
  const segctl = (
    <div style={sx("display:flex;background:#e4e6eb;border-radius:9px;padding:2px;margin:16px 0 10px")}>
      {["All 64", "Not marked 1", "Away 5"].map((t, i) => (
        <span key={t} style={sx(`flex:1;height:30px;border-radius:7px;display:flex;align-items:center;justify-content:center;font:${i === 0 ? "600" : "500"} 13px ${UI};${i === 0 ? "background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.12);" : ""}color:${INK}`)}>{t}</span>
      ))}
    </div>
  );
  return (
    <div style={sx(`position:relative;width:${SCR_W}px;height:${SCR_H}px;background:#f2f3f6;color:${INK};overflow:hidden`)}>
      <StatusBar t="21:04" />
      <div style={sx("padding:0 16px")}>
        <div style={sx("display:flex;align-items:center;justify-content:space-between;height:44px")}>
          <span style={sx(`display:flex;align-items:center;gap:2px;font:400 17px ${UI};color:${BLUE}`)}><Ic n="left-line" s={20} c={BLUE} />Houses</span>
          <span style={sx(`font:600 17px ${UI}`)}>Tsavo House</span><span style={sx(`font:400 17px ${UI};color:${BLUE}`)}>Search</span>
        </div>
        <div style={sx(`font:600 28px ${UI};letter-spacing:-0.025em;margin:8px 4px 2px`)}>Lights out</div>
        <div style={sx(`font:400 15px ${UI};color:${MUTED};margin:0 4px 14px`)}>Thursday 21:00 · Mr Chari</div>
        {summary}{segctl}<div style={sx("background:#fff;border-radius:16px;overflow:hidden")}>{rows}</div>
      </div>
      <div style={sx("position:absolute;left:0;right:0;bottom:0;padding:12px 16px 34px;background:#f9f9fb;box-shadow:0 -0.5px 0 rgba(0,0,0,.18)")}>
        <div style={sx(`display:flex;align-items:center;gap:6px;justify-content:center;font:400 13px ${UI};color:${MUTED};margin-bottom:10px`)}><Ic n="wifi-off" s={14} c={MUTED} />Saved on this phone · syncs when online</div>
        <div style={sx(`height:50px;border-radius:14px;background:${BLUE};color:#fff;display:flex;align-items:center;justify-content:center;font:600 17px ${UI}`)}>Finish roll call</div>
      </div>
    </div>
  );
}

/** who_sections.rollcall_phone: the roll call in the device, scaled */
export function RollcallPhone({ k = 0.52 }: { k?: number }) {
  const w = SCR_W + 2 * BEZ, h = SCR_H + 2 * BEZ;
  return (
    <div style={sx("filter:drop-shadow(0 16px 22px rgba(11,12,20,.32))")}>
      <Scaled w={pyRound((w + 12) * k)} h={pyRound(h * k)} k={k}>
        <div style={sx("padding:0 6px")}><Device><RollcallApp /></Device></div>
      </Scaled>
    </div>
  );
}

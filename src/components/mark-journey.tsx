/**
 * mark_anim.mark_journey: one mark, recorded once, walking the campus drawing to every portal (8 s loop).
 * The keyframes are design/components/mark-journey.css, imported as they are in the root layout.
 */
import { Art } from "./art";
import { Ic, PortalIcon, sx } from "./ds";
import { BLUE, DOTS, INK, LINE, MUTED, OK, OKS, SANS } from "@/lib/design";

function EntryCard({ w = 250 }: { w?: number }) {
  const rows: [string, string, boolean][] = [["Tanaka Moyo", "71", true], ["Tendai Chirwa", "58", false], ["Ruvimbo Gumbo", "77", false]];
  return (
    <div style={sx(`width:${w}px;border-radius:16px;background:#fff;box-shadow:0 0 0 1px ${LINE},0 18px 30px -18px rgba(11,12,20,.35);padding:14px 14px 14px;box-sizing:border-box`)}>
      <div style={sx("display:flex;align-items:center;gap:8px;margin-bottom:8px")}>
        <PortalIcon n="Teacher" s={24} />
        <div><div style={sx(`font:600 13.5px ${SANS}`)}>Mathematics · test 2</div><div style={sx(`font:400 11.5px ${SANS};color:${MUTED}`)}>Form 3B · Ms Sibanda</div></div>
      </div>
      {rows.map(([n, v, hot]) => (
        <div key={n} style={sx(`display:flex;align-items:center;justify-content:space-between;padding:7px 0;border-top:1px solid ${LINE};font:400 13px ${SANS}`)}>
          {n}<span style={sx(`width:46px;height:26px;border-radius:7px;box-shadow:inset 0 0 0 ${hot ? `1.5px ${BLUE}` : `1px ${LINE}`};display:flex;align-items:center;justify-content:center;font:600 13px ${SANS};color:${INK}`)}>{v}</span>
        </div>
      ))}
      <div style={sx("position:relative;height:38px;margin-top:10px;animation:cmk-tap 8s infinite")}>
        <span style={sx(`position:absolute;inset:0;border-radius:10px;background:${BLUE};color:#fff;display:flex;align-items:center;justify-content:center;gap:8px;font:600 13.5px ${SANS};animation:cmk-press 8s infinite`)}>
          <Ic n="send-plane" s={14} c="#fff" />Submit marks
        </span>
        <span style={sx(`position:absolute;inset:0;border-radius:10px;background:${OKS};color:${OK};display:flex;align-items:center;justify-content:center;gap:8px;font:600 13.5px ${SANS};opacity:0;animation:cmk-done 8s infinite`)}>
          <Ic n="check-circle" s={14} c={OK} />Recorded once · 4 places
        </span>
      </div>
    </div>
  );
}

export function MarkJourney({ w = 620, h = 460 }: { w?: number; h?: number }) {
  return (
    <div className="mark-journey" role="img" aria-label="Ms Sibanda records Tanaka's 71% once; the mark reaches the Head's view, Tanaka's portal and Rudo Moyo's phone."
      style={sx(`position:relative;width:${w}px;height:${h}px;border-radius:28px;${DOTS};box-shadow:inset 0 0 0 1px #eceef2;overflow:hidden`)}>
      <Art k={`journey:${w}x${h}`} />
      <div style={sx(`position:absolute;left:20px;top:${h - 236}px`)}><EntryCard w={250} /></div>
    </div>
  );
}

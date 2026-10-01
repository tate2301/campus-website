import type { Metadata } from "next";
import { Fragment } from "react";
import { Lockup } from "@/components/chrome";
import { Ic, Pmark, sx } from "@/components/ds";
import { CP, FAQ } from "@/content/copy";
import { BLUE, INK, INK2, LINE, MONO, MUTED, NUM, PLATE, SANS } from "@/lib/design";

/**
 * webpages.price_sheet: the one-page price sheet, A4 at 96 dpi (794 x 1123). scripts/price-sheet-pdf.mjs prints this
 * page to public/pricing/price-sheet.pdf, which is what /pricing/price-sheet.pdf serves.
 */
export const metadata: Metadata = { title: "Price sheet", robots: { index: false } };

type Plan = { name: string; price: string; per: string; items: string[] };

export default function PriceSheet() {
  const P = CP.PRICING;
  const m: Plan = P.main, lm: Plan = P.lms;
  return (
    <div data-tree="desktop">
      <div style={sx(`width:794px;height:1123px;box-sizing:border-box;background:#fff;padding:56px 60px;font-family:${SANS};color:${INK};display:flex;flex-direction:column`)}>
        <div style={sx(`display:flex;justify-content:space-between;align-items:center;padding-bottom:18px;border-bottom:1px solid ${LINE}`)}>
          <Lockup h={22} by={false} /><span style={sx(`font:400 12px ${MONO};color:${MUTED}`)}>Price sheet · October 2026</span>
        </div>
        <div style={sx(`margin-top:40px;font:500 14px ${SANS};color:${BLUE}`)}>Pricing</div>
        <h1 style={sx(`margin:10px 0 0;font:600 46px/1.04 ${SANS};letter-spacing:-0.035em;text-wrap:balance`)}>US$1 per active pupil per month.</h1>
        <div style={sx(`font:400 15.5px/1.6 ${SANS};color:${INK2};margin-top:14px;max-width:560px`)}>{P.b}</div>
        <div style={sx("display:flex;gap:20px;margin-top:32px")}>
          <div style={sx(`flex:1;border-radius:16px;box-shadow:0 0 0 2px ${BLUE};padding:22px`)}>
            <div style={sx(`font:600 15px ${SANS}`)}>{m.name}</div>
            <div style={sx(`font:600 38px/1 ${SANS};letter-spacing:-0.03em;margin-top:12px`)}>{m.price}</div>
            <div style={sx(`font:400 13px ${SANS};color:${MUTED};margin-top:6px`)}>{m.per}</div>
            <div style={sx("margin-top:14px")}>
              {[...m.items, "Works without internet", "Daily backups and a full export"].map((t) => (
                <div key={t} style={sx(`display:flex;gap:10px;align-items:flex-start;padding:7px 0;border-top:1px solid ${LINE};font:400 13.5px/1.45 ${SANS};color:${INK2}`)}>
                  <span style={sx("padding-top:2px")}><Ic n="check-circle" s={14} c={BLUE} /></span>{t}
                </div>
              ))}
            </div>
          </div>
          <div style={sx("flex:1;display:flex;flex-direction:column;gap:20px")}>
            <div style={sx(`border-radius:16px;box-shadow:0 0 0 1px ${LINE};padding:22px`)}>
              <div style={sx(`font:600 15px ${SANS}`)}>{lm.name}</div>
              <div style={sx(`font:600 38px/1 ${SANS};letter-spacing:-0.03em;margin-top:12px`)}>{lm.price}</div>
              <div style={sx(`font:400 13px ${SANS};color:${MUTED};margin-top:6px`)}>{lm.per}</div>
              <div style={sx(`font:400 13.5px/1.5 ${SANS};color:${INK2};margin-top:12px`)}>{lm.items.map((t, i) => <Fragment key={t}>{i ? <br /> : null}{t}</Fragment>)}</div>
            </div>
            <div style={sx(`border-radius:16px;background:${PLATE};padding:22px`)}>
              <div style={sx(`font:500 13px ${SANS};color:${MUTED}`)}>{P.example.t}</div>
              <div style={sx(`font:600 32px/1 ${SANS};letter-spacing:-0.03em;margin-top:10px;${NUM}`)}>{P.example.v}</div>
              <div style={sx(`font:400 13px ${SANS};color:${INK2};margin-top:6px`)}>{P.example.s}</div>
            </div>
          </div>
        </div>
        <div style={sx(`margin-top:34px;font:600 16px ${SANS}`)}>Setup and training</div>
        <div style={sx("display:flex;gap:16px;margin-top:14px")}>
          {(P.timeline as [string, string, string][]).map(([a, b, c]) => (
            <div key={a} style={sx(`flex:1;padding-top:10px;border-top:3px solid ${BLUE}`)}>
              <div style={sx(`font:500 11.5px ${SANS};color:${MUTED}`)}>{a}</div>
              <div style={sx(`font:600 14px ${SANS};margin-top:4px`)}>{b}</div>
              <div style={sx(`font:400 12.5px/1.4 ${SANS};color:${INK2};margin-top:2px`)}>{c}</div>
            </div>
          ))}
        </div>
        <div style={sx(`margin-top:34px;font:600 16px ${SANS}`)}>Questions</div>
        <div style={sx("display:grid;grid-template-columns:1fr 1fr;gap:4px 28px;margin-top:6px")}>
          {[FAQ[0], FAQ[3]].map(([q, a]) => (
            <div key={q} style={sx(`padding:10px 0;border-top:1px solid ${LINE}`)}>
              <div style={sx(`font:600 13.5px ${SANS}`)}>{q}</div><div style={sx(`font:400 12.5px/1.5 ${SANS};color:${INK2};margin-top:3px`)}>{a}</div>
            </div>
          ))}
        </div>
        <div style={sx(`margin-top:auto;display:flex;justify-content:space-between;align-items:flex-end;padding-top:20px;border-top:1px solid ${LINE}`)}>
          <div style={sx(`font:400 12.5px/1.6 ${SANS};color:${MUTED}`)}>Book a demo at campus.corelith.co.zw/demo<br />{CP.FOOT_LINE}</div>
          <Pmark s={40} r={11} />
        </div>
      </div>
    </div>
  );
}

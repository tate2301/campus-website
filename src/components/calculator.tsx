"use client";
import { useId, useState } from "react";
import { sx } from "@/lib/sx";

/**
 * ds.calculator, working: the number of active pupils times the package's rate. It opens on the design's example
 * (1,140 pupils, Campus at US$1), drawn exactly as the design draws it; the value is an input and the package a
 * choice of two. The status pills and field are drawn here as in ds.status and ds.field, because this component
 * runs in the browser.
 */
const INK = "#0b0c14", INK2 = "#3b3d47", MUTED = "#6b6d78", LINE = "#e7e9ef", PLATE = "#f4f5f7";
const SANS = "var(--font-sans)";
const SH_CARD = "0 1px 2px rgba(11,12,20,.06), 0 16px 36px -18px rgba(11,12,20,.30)";
const RATES = [["Campus", 1], ["With LMS", 8.99]] as const;

const money = (v: number) => `US$${v.toLocaleString("en-GB", { minimumFractionDigits: 2, maximumFractionDigits: 2 })}`;
const count = (v: number) => v.toLocaleString("en-GB");

function Pill({ t, c, bg }: { t: string; c: string; bg: string }) {
  return (
    <span style={sx(`display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 10px 0 8px;border-radius:999px;background:${bg};font:500 12.5px ${SANS};color:${c};white-space:nowrap`)}>
      <i style={sx(`width:6px;height:6px;border-radius:3px;background:${c}`)} />{t}
    </span>
  );
}

export function Calculator({ w = 520 }: { w?: number }) {
  const id = useId();
  const [text, setText] = useState("1,140");
  const [pkg, setPkg] = useState(0);
  const pupils = Math.max(0, Math.floor(Number(text.replace(/[^\d]/g, "")) || 0));
  const [, rate] = RATES[pkg];
  return (
    <div id="calculator" style={sx(`width:${w}px;box-sizing:border-box;background:#fff;border-radius:24px;box-shadow:0 0 0 1px ${LINE},${SH_CARD};padding:32px`)}>
      <div style={sx(`font:600 18px ${SANS}`)}>Work out your school</div>
      <div style={sx("display:flex;gap:16px;margin-top:22px;align-items:flex-end")}>
        <div style={sx("width:200px")}>
          <label htmlFor={id} style={sx(`display:block;font:500 14px ${SANS};color:${INK};margin-bottom:8px`)}>Active pupils</label>
          <div style={sx(`height:48px;border-radius:12px;background:#fff;box-shadow:inset 0 0 0 1px ${LINE};display:flex;align-items:center;justify-content:space-between;padding:0 16px;box-sizing:border-box;font:400 16px ${SANS}`)}>
            <input id={id} inputMode="numeric" autoComplete="off" value={text}
              onChange={(e) => setText(e.target.value)} onBlur={() => setText(count(pupils))}
              style={sx(`color:${INK};font:inherit;width:100%;min-width:0;border:0;padding:0;margin:0;background:transparent;outline:none`)} />
          </div>
        </div>
        <div>
          <div style={sx(`font:500 14px ${SANS};margin-bottom:8px`)}>Package</div>
          <div role="radiogroup" aria-label="Package" style={sx("display:inline-flex;padding:4px;border-radius:24px;background:#eef0f3")}>
            {RATES.map(([o], i) => (
              <button key={o} type="button" role="radio" aria-checked={i === pkg} onClick={() => setPkg(i)}
                style={sx(`height:36px;padding:0 16px;border-radius:18px;display:flex;align-items:center;font:500 14px ${SANS};${i === pkg ? `background:#fff;color:${INK};box-shadow:0 1px 2px rgba(11,12,20,.12)` : `color:${MUTED}`}`)}>{o}</button>
            ))}
          </div>
        </div>
      </div>
      <div style={sx(`margin-top:26px;padding:22px;border-radius:16px;background:${PLATE}`)} aria-live="polite">
        <div style={sx(`display:flex;justify-content:space-between;font:400 15px ${SANS};color:${INK2}`)}>
          <span>{`${count(pupils)} active pupils × US$${rate.toFixed(2)}`}</span><span>a month</span>
        </div>
        <div style={sx(`font:600 44px/1 ${SANS};letter-spacing:-0.03em;margin-top:12px;font-variant-numeric:tabular-nums;`)}>{money(Math.round(pupils * rate * 100) / 100)}</div>
        <div style={sx("display:flex;gap:8px;margin-top:14px")}><Pill t="First month free" c="#12805c" bg="#e5f4ec" /><Pill t="Holidays US$0" c={INK2} bg="#eef0f3" /></div>
      </div>
    </div>
  );
}

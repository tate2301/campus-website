/**
 * Working form controls drawn exactly as ds.field and ds.check draw them. A text box is the design's 48px box with an
 * input in it; a checkbox or radio is the design's 20px box with a real input beside it, hidden, that the box follows
 * (globals.css: .ctl). No JavaScript: the forms post to /api/*, which redirects.
 */
import type { ReactNode } from "react";
import { Ic, sx } from "./ds";
import { FAINT, INK, INK2, LINE, MUTED, SANS } from "@/lib/design";

type FieldProps = {
  id: string; name: string; label: ReactNode; ph?: string; help?: string; w?: number | string;
  kind?: "text" | "select" | "area"; type?: string; required?: boolean; options?: string[]; autoComplete?: string; tail?: ReactNode;
};

/** ds.field, working */
export function FieldInput({ id, name, label, ph = "", help = "", w = 360, kind = "text", type = "text", required, options = [], autoComplete, tail }: FieldProps) {
  const width = typeof w === "number" ? `${w}px` : w;
  const hh = kind === "area" ? 104 : 48;
  const input = `color:${INK};font:inherit;width:100%;min-width:0;border:0;padding:0;margin:0;background:transparent;outline:none`;
  return (
    <div style={sx(`width:${width}`)}>
      <label htmlFor={id} style={sx(`display:block;font:500 14px ${SANS};color:${INK};margin-bottom:8px`)}>{label}</label>
      <div className="field-box" style={sx(`height:${hh}px;border-radius:12px;background:#fff;box-shadow:inset 0 0 0 1px ${LINE};display:flex;align-items:${kind === "area" ? "flex-start" : "center"};justify-content:space-between;padding:${kind === "area" ? "14px" : "0"} 16px;box-sizing:border-box;font:400 16px ${SANS}`)}>
        {kind === "select" ? (
          <select id={id} name={name} required={required} defaultValue="" style={sx(`${input};appearance:none;cursor:pointer`)}>
            <option value="" disabled>{ph}</option>
            {options.map((o) => <option key={o}>{o}</option>)}
          </select>
        ) : kind === "area" ? (
          <textarea id={id} name={name} placeholder={ph} required={required} style={sx(`${input};height:100%;resize:none;line-height:normal`)} />
        ) : (
          <input id={id} name={name} type={type} placeholder={ph} required={required} autoComplete={autoComplete} style={sx(input)} />
        )}
        {kind === "select" ? <Ic n="down-line" s={16} c={MUTED} /> : null}{tail}
      </div>
      {help ? <div style={sx(`font:400 13.5px ${SANS};color:${MUTED};margin-top:8px`)}>{help}</div> : null}
    </div>
  );
}

/** ds.check, working: a checkbox, or a radio when name groups it */
export function CheckInput({ label, name, value, radio = false, checked = false }: { label: ReactNode; name: string; value: string; radio?: boolean; checked?: boolean }) {
  return (
    <label className="ctl" style={sx(`display:inline-flex;align-items:center;gap:10px;font:400 15px ${SANS};color:${INK}`)}>
      <span className={radio ? "box radio" : "box"} style={sx(`width:20px;height:20px;border-radius:${radio ? 10 : 6}px;display:flex;align-items:center;justify-content:center`)}>
        {radio ? <span style={sx("width:8px;height:8px;border-radius:4px;background:#fff")} /> : <Ic n="check-line" s={14} c="#fff" />}
      </span>
      {label}
      <input data-extra type={radio ? "radio" : "checkbox"} name={name} value={value} defaultChecked={checked} />
    </label>
  );
}

export { FAINT };

/** ds.filter_pill, working: one of a set of topics, as a radio */
export function PillInput({ t, name, checked = false }: { t: string; name: string; checked?: boolean }) {
  return (
    <label className="pill" style={sx(`display:inline-flex;align-items:center;gap:7px;height:40px;padding:0 16px;border-radius:20px;background:#fff;color:${INK2};box-shadow:0 0 0 1px ${LINE};font:500 14.5px ${SANS};white-space:nowrap`)}>
      {t}<input data-extra type="radio" name={name} value={t} defaultChecked={checked} />
    </label>
  );
}

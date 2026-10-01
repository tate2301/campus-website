/** ds.pricing_card: a package, its price, the four portals, what it includes */
import { Cbtn, PortalIcon, PORTAL_NAMES, Status, Ticks, sx } from "./ds";
import { BLUE, INK2, LINE, MUTED, SANS } from "@/lib/design";

type Plan = { name: string; price: string; per: string; items: string[] };

export function PricingCard({ p, primary = true, w = 413 }: { p: Plan; primary?: boolean; w?: number | string }) {
  return (
    <div style={sx(`width:${typeof w === "number" ? `${w}px` : w};box-sizing:border-box;background:#fff;border-radius:24px;box-shadow:0 0 0 ${primary ? 2 : 1}px ${primary ? BLUE : LINE};padding:32px;display:flex;flex-direction:column;gap:18px`)}>
      <div style={sx("display:flex;justify-content:space-between;align-items:center")}>
        <span style={sx(`font:600 18px ${SANS}`)}>{p.name}</span>{primary ? <Status t="Current offer" kind="info" /> : null}
      </div>
      <div><span style={sx(`font:600 56px/1 ${SANS};letter-spacing:-0.03em`)}>{p.price}</span><div style={sx(`font:400 15px ${SANS};color:${MUTED};margin-top:10px`)}>{p.per}</div></div>
      <div style={sx(`display:flex;gap:8px;padding:12px 0 0;border-top:1px solid ${LINE}`)}>
        {PORTAL_NAMES.map((n) => (
          <div key={n} style={sx("flex:1;display:flex;flex-direction:column;align-items:center;gap:6px")}>
            <PortalIcon n={n} s={40} /><span style={sx(`font:500 11.5px ${SANS};color:${MUTED}`)}>{n}</span>
          </div>
        ))}
      </div>
      <div><Ticks items={p.items} c={INK2} icon="check-circle" icC={BLUE} size={15} /></div>
      <div style={sx("display:flex")}><Cbtn label="Book a demo" icon="calendar" kind={primary ? "primary" : "secondary"} href="/demo" /></div>
    </div>
  );
}

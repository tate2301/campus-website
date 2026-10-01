import "server-only";
import { clean, cleanAttribution, deliver, sourceLabel, type Lead } from "./leads";
import { FORM_MESSAGES } from "@/content/form-messages";

/**
 * The request side of the two forms, as corelith.co.zw's /api/leads: validation, a honeypot, a timing trap and a
 * rate limit, then the lead is logged before delivery so a copy always survives.
 *
 * The forms work without JavaScript: a plain post is answered with a redirect (to Request sent, or back to the form
 * with ?error=…). With JavaScript the form kit posts with `accept: application/json` and gets JSON back, so a
 * visitor's answers stay in the form if something needs fixing.
 */

type Kind = "demo" | "contact";
const PAGE: Record<Kind, string> = { demo: "/demo", contact: "/contact" };
const DONE: Record<Kind, string> = { demo: "/demo/sent", contact: "/contact?sent=1" };
const EMAIL = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

// A speed bump, not a wall: the counter lives in this instance's memory. Put the host's rate limiting in front of it.
const WINDOW_MS = 60_000, MAX_PER_WINDOW = 5;
const hits = new Map<string, number[]>();
function rateLimited(key: string): boolean {
  const now = Date.now();
  const recent = (hits.get(key) ?? []).filter((t) => now - t < WINDOW_MS);
  recent.push(now);
  hits.set(key, recent);
  if (hits.size > 5000) for (const [k, times] of hits) if (!times.some((t) => now - t < WINDOW_MS)) hits.delete(k);
  return recent.length > MAX_PER_WINDOW;
}

async function read(request: Request): Promise<Record<string, unknown>> {
  if ((request.headers.get("content-type") ?? "").includes("application/json")) return (await request.json()) as Record<string, unknown>;
  const form = await request.formData();
  const out: Record<string, unknown> = {};
  for (const key of new Set(form.keys())) {
    const all = form.getAll(key).filter((v): v is string => typeof v === "string");
    out[key] = all.length > 1 ? all : all[0];
  }
  return out;
}

const list = (v: unknown) => (Array.isArray(v) ? v.map((x) => clean(x, 60)).filter(Boolean).join(", ") : clean(v, 60));

function build(kind: Kind, p: Record<string, unknown>): Lead | { error: string } {
  const name = clean(p.name, 200), email = clean(p.email, 200), phone = clean(p.phone, 40);
  if (!name) return { error: "name" };
  if (email && !EMAIL.test(email)) return { error: "email" };
  let attribution;
  try { attribution = cleanAttribution(typeof p.attribution === "string" ? JSON.parse(p.attribution) : p.attribution); } catch { /* none */ }
  const base = { name, email, phone, receivedAt: new Date().toISOString(), attribution };
  if (kind === "demo") {
    const school = clean(p.school, 200);
    if (!school) return { error: "school" };
    if (!phone) return { error: "phone" };
    const fields: Record<string, string> = {};
    const role = clean(p.role, 60), pupils = clean(p.pupils, 40), kinds = list(p.school_kind), how = clean(p.how, 20);
    if (role) fields.Role = role;
    if (pupils) fields["Active pupils"] = pupils;
    if (kinds) fields["The school"] = kinds;
    if (how) fields["Show it by"] = how === "video" ? "Video call" : "Visit to the school";
    return { ...base, company: school, message: "", source: "campus-demo", fields };
  }
  const message = clean(p.message, 4000);
  if (!email) return { error: "email" };
  if (!message) return { error: "message" };
  const fields: Record<string, string> = {};
  const topic = clean(p.topic, 60);
  if (topic) fields.Topic = topic;
  return { ...base, company: clean(p.organisation, 200), message, source: "campus-contact", fields };
}

export async function handleLead(request: Request, kind: Kind): Promise<Response> {
  const json = (request.headers.get("accept") ?? "").includes("application/json");
  const done = () => (json ? Response.json({ ok: true, redirect: DONE[kind] }, { status: 201 }) : Response.redirect(new URL(DONE[kind], request.url), 303));
  const fail = (code: string, status: number) => json
    ? Response.json({ error: FORM_MESSAGES[code], code }, { status })
    : Response.redirect(new URL(`${PAGE[kind]}?error=${code}`, request.url), 303);

  let payload: Record<string, unknown>;
  try { payload = await read(request); } catch { return fail("failed", 400); }

  // Honeypot: a field people never see. Bots that fill it are told it worked, so they don't learn.
  if (clean(payload.website)) return done();
  // Timing trap: the form kit stamps when the form appeared; faster than a person can read it is scripted.
  const renderedAt = Number(payload.renderedAt);
  if (Number.isFinite(renderedAt) && renderedAt > 0 && Date.now() - renderedAt < 2500) return done();

  const ip = request.headers.get("cf-connecting-ip") || request.headers.get("x-real-ip") || request.headers.get("x-forwarded-for")?.split(",")[0].trim() || "unknown";
  if (rateLimited(ip)) return fail("busy", 429);

  const lead = build(kind, payload);
  if ("error" in lead) return fail(lead.error, 400);

  // Log first and always, so the lead survives whatever happens to delivery.
  console.log("[lead]", JSON.stringify(lead));
  const result = await deliver(lead);
  if (!result.configured) {
    if (process.env.NODE_ENV !== "production") console.warn(`[lead] CORELITH_CRM_API_KEY is not set — ${sourceLabel(lead.source)} from ${lead.name} exists only in this log.`);
    return done();
  }
  if (result.error) {
    console.error("[lead] delivery failed —", result.error);
    return fail("failed", 500);
  }
  return done();
}

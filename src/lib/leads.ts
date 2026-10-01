import "server-only";

/**
 * What happens to a demo request or a contact message after someone presses send.
 *
 * Both go to Corelith's own CRM, the same intake corelith.co.zw uses (its lib/leads.ts and docs/FORMS.md): the
 * tenant's public lead webhook finds or creates a deduplicated client, opens a lead at stage NEW, writes the
 * submission onto the lead's timeline and notifies whoever the API key routes to.
 *
 * Setup: set CORELITH_CRM_API_KEY (minted in the tenant under CRM → Settings → API keys; it begins with `crm_`). Leave
 * the key's default channel unset, so the CRM derives the channel from the campaign fields. CORELITH_CRM_URL overrides
 * the host, for pointing a staging build elsewhere. Until the key is set, a submission exists only in the server log.
 */

const DELIVERY_TIMEOUT_MS = 8000;
/** The webhook's own ceiling on `message`; any overflow rejects the whole submission. */
const CRM_MESSAGE_MAX = 4000;
/** Corelith's tenant, as corelith.co.zw's forms use it. */
const CRM_HOST = "https://hurudza-creative.apps.corelith.co.zw";
const SITE = "campus.corelith.co.zw";

export type Attribution = {
  utmSource?: string; utmMedium?: string; utmCampaign?: string; utmTerm?: string; utmContent?: string;
  /** an external referrer only */
  referrer?: string;
  /** the page the form was sent from, path and query */
  landingPage?: string;
};

export type Lead = {
  name: string;
  email: string;
  phone: string;
  /** the school, or the organisation for a contact message */
  company: string;
  message: string;
  /** which form: campus-demo, campus-contact */
  source: string;
  receivedAt: string;
  /** the form's own questions, label → answer, folded into the CRM note */
  fields: Record<string, string>;
  attribution?: Attribution;
};

export function clean(value: unknown, max = 500): string {
  return typeof value === "string" ? value.trim().slice(0, max) : "";
}

export function cleanAttribution(value: unknown): Attribution | undefined {
  if (!value || typeof value !== "object" || Array.isArray(value)) return undefined;
  const source = value as Record<string, unknown>;
  const out: Attribution = {};
  for (const key of ["utmSource", "utmMedium", "utmCampaign", "utmTerm", "utmContent", "referrer", "landingPage"] as const) {
    const text = clean(source[key], 300);
    if (text) out[key] = text;
  }
  return Object.keys(out).length ? out : undefined;
}

export function sourceLabel(source: string): string {
  return ({ "campus-demo": "Campus demo request", "campus-contact": "Campus enquiry" } as Record<string, string>)[source] ?? source;
}

function attributionLines(lead: Lead): string[] {
  const a = lead.attribution;
  if (!a) return [];
  const campaign = [a.utmSource, a.utmMedium, a.utmCampaign].filter(Boolean).join(" / ");
  return [
    campaign && `Campaign: ${campaign}`,
    a.utmTerm && `Campaign term: ${a.utmTerm}`,
    a.utmContent && `Campaign content: ${a.utmContent}`,
    a.referrer && `Referred by: ${a.referrer}`,
    a.landingPage && `Sent from: ${a.landingPage}`,
  ].filter(Boolean) as string[];
}

/**
 * The CRM note. The webhook has no custom fields, so everything the form asked that has no column of its own (the
 * school, the role, the number of pupils, how to show it) is folded in here rather than dropped. The visitor's own
 * words go last, so they are what is cut if the note runs long.
 */
function crmMessage(lead: Lead): string {
  const context = [
    lead.company && `School: ${lead.company}`,
    ...Object.entries(lead.fields).map(([label, value]) => `${label}: ${value}`),
    ...attributionLines(lead),
  ].filter(Boolean);
  const head = [`${sourceLabel(lead.source)} — ${SITE}`, context.join("\n")].filter(Boolean).join("\n\n");
  const body = lead.message ? `${head}\n\n${lead.message}` : head;
  return body.length <= CRM_MESSAGE_MAX ? body : `${body.slice(0, CRM_MESSAGE_MAX - 1).trimEnd()}…`;
}

/** clamp to the webhook's limit: it validates strictly and rejects the whole lead on any overflow */
function cap(value: string | undefined, max: number): string | undefined {
  const text = (value ?? "").trim().slice(0, max);
  return text || undefined;
}

async function postCrm(lead: Lead, host: string, apiKey: string): Promise<void> {
  const a = lead.attribution;
  const response = await fetch(`${host.replace(/\/+$/, "")}/api/public/crm/webhook/leads`, {
    method: "POST",
    headers: { "content-type": "application/json", "x-api-key": apiKey },
    // The schema mixes camelCase (`phoneCountry`) and snake case (`utm_*`). Unknown keys are dropped silently, so the
    // body is built field by field. `channel` is not sent: the CRM derives it from the campaign fields.
    body: JSON.stringify({
      name: cap(lead.name, 200),
      email: cap(lead.email, 200),
      phone: cap(lead.phone, 40),
      // the numbers this form collects are Zimbabwean; the hint lets the CRM normalise to E.164 and deduplicate
      phoneCountry: lead.phone ? "ZW" : undefined,
      message: crmMessage(lead),
      services: ["Campus"],
      source: cap(sourceLabel(lead.source), 120),
      utm_source: cap(a?.utmSource, 120),
      utm_medium: cap(a?.utmMedium, 120),
      utm_campaign: cap(a?.utmCampaign, 120),
      utm_term: cap(a?.utmTerm, 120),
      utm_content: cap(a?.utmContent, 120),
      referrer: cap(a?.referrer, 500),
      landing_page: cap(a?.landingPage, 500),
    }),
    signal: AbortSignal.timeout(DELIVERY_TIMEOUT_MS),
  });
  if (!response.ok) throw new Error(`crm responded ${response.status}: ${(await response.text()).slice(0, 200)}`);
  const created = (await response.json().catch(() => null)) as { leadNo?: string } | null;
  if (created?.leadNo) console.log(`[lead] crm accepted — ${created.leadNo}`);
}

/** `configured: false` is the pre-launch state: the log is the only copy. */
export async function deliver(lead: Lead): Promise<{ configured: boolean; error?: string }> {
  const key = process.env.CORELITH_CRM_API_KEY;
  if (!key) return { configured: false };
  try {
    await postCrm(lead, process.env.CORELITH_CRM_URL || CRM_HOST, key);
    return { configured: true };
  } catch (e) {
    return { configured: true, error: String(e).slice(0, 300) };
  }
}

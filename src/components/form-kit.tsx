"use client";
import { useEffect, useRef, useState } from "react";
import { FORM_MESSAGES } from "@/content/form-messages";

/**
 * The working parts of a lead form, as on corelith.co.zw: a honeypot field, the time the form appeared (the server
 * ignores sends faster than a person can read), this visit's campaign tags, and a line that says what went wrong or
 * that a message was sent. It also sends the form without leaving the page, so nothing typed is lost if a field
 * needs fixing. Without JavaScript the form still posts, and the server redirects.
 *
 * Campaign tags are read from this page only, and nothing is stored: keeping a visit's first page across pages needs
 * the consent corelith.co.zw asks for, and the Campus design has no consent banner (NOTES.md).
 *
 * Renders one element, display:none until there is something to say, at the end of the form.
 */
const EXTERNAL = (ref: string) => { try { return ref && new URL(ref).host !== location.host ? ref : undefined; } catch { return undefined; } };

function attribution(): string {
  const p = new URLSearchParams(location.search);
  const a = {
    utmSource: p.get("utm_source") ?? undefined, utmMedium: p.get("utm_medium") ?? undefined, utmCampaign: p.get("utm_campaign") ?? undefined,
    utmTerm: p.get("utm_term") ?? undefined, utmContent: p.get("utm_content") ?? undefined,
    referrer: EXTERNAL(document.referrer), landingPage: location.pathname + location.search,
  };
  return JSON.stringify(a);
}

export function FormKit({ font }: { font: string }) {
  const ref = useRef<HTMLDivElement>(null);
  const [note, setNote] = useState<{ text: string; ok: boolean } | null>(null);
  const [busy, setBusy] = useState(false);

  useEffect(() => {
    const box = ref.current!;
    const form = box.closest("form")!;
    (box.querySelector("[name=renderedAt]") as HTMLInputElement).value = String(Date.now());
    (box.querySelector("[name=attribution]") as HTMLInputElement).value = attribution();
    // after a plain post came back (no JavaScript at the time), say what happened
    const q = new URLSearchParams(location.search);
    const code = q.get("error");
    if (code && FORM_MESSAGES[code]) setNote({ text: FORM_MESSAGES[code], ok: false });
    else if (q.has("sent")) setNote({ text: FORM_MESSAGES.sent, ok: true });

    const submit = async (e: SubmitEvent) => {
      e.preventDefault();
      setBusy(true);
      setNote(null);
      try {
        const res = await fetch(form.action, { method: "POST", body: new FormData(form), headers: { accept: "application/json" } });
        const body = (await res.json().catch(() => ({}))) as { ok?: boolean; redirect?: string; error?: string };
        if (res.ok && body.redirect?.startsWith("/demo/sent")) return location.assign(body.redirect);
        if (res.ok) { form.reset(); setNote({ text: FORM_MESSAGES.sent, ok: true }); return; }
        setNote({ text: body.error ?? FORM_MESSAGES.failed, ok: false });
      } catch {
        setNote({ text: FORM_MESSAGES.failed, ok: false });
      } finally {
        setBusy(false);
      }
    };
    form.addEventListener("submit", submit);
    return () => form.removeEventListener("submit", submit);
  }, []);

  useEffect(() => { ref.current!.closest("form")!.setAttribute("aria-busy", String(busy)); }, [busy]);

  return (
    <div ref={ref} data-extra style={{ display: note ? "block" : "none", marginTop: 16 }}>
      {/* honeypot: hidden from people and from assistive technology */}
      <input type="text" name="website" tabIndex={-1} autoComplete="off" aria-hidden="true" style={{ position: "absolute", left: -10000, width: 1, height: 1, opacity: 0 }} />
      <input type="hidden" name="renderedAt" />
      <input type="hidden" name="attribution" />
      <p role={note?.ok ? "status" : "alert"} style={{ margin: 0, font: `400 15px/1.5 ${font}`, color: note?.ok ? "#12805c" : "#be123c" }}>{note?.text}</p>
    </div>
  );
}

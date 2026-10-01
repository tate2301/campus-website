import { NextResponse } from "next/server";

/**
 * Book a demo. A stub: it checks the request has what the call needs, then shows "Request sent". Replace the TODO
 * with the real hand-off (CRM, email to the Harare team) when there is one.
 */
export async function POST(req: Request) {
  const form = await req.formData();
  const name = String(form.get("name") ?? "").trim();
  const school = String(form.get("school") ?? "").trim();
  const phone = String(form.get("phone") ?? "").trim();
  if (!name || !school || !phone) return NextResponse.json({ error: "Name, school and phone are needed to arrange the demo." }, { status: 400 });
  // TODO: send the request to the team
  return NextResponse.redirect(new URL("/demo/sent", req.url), 303);
}

import { NextResponse } from "next/server";

/** Contact. A stub like /api/demo: checks the message has a reply address, then returns to the page. */
export async function POST(req: Request) {
  const form = await req.formData();
  const email = String(form.get("email") ?? "").trim();
  const message = String(form.get("message") ?? "").trim();
  if (!email || !message) return NextResponse.json({ error: "An email address and a message are needed." }, { status: 400 });
  // TODO: send the message to the team
  return NextResponse.redirect(new URL("/contact?sent=1", req.url), 303);
}

"use client";
import { useEffect, useState } from "react";

/** After the contact form posts (/api/contact redirects back with ?sent=1), say so beside the button. */
export function SentNote({ style }: { style: React.CSSProperties }) {
  const [sent, setSent] = useState(false);
  useEffect(() => setSent(new URLSearchParams(location.search).has("sent")), []);
  return <span data-extra role="status" style={{ ...style, display: sent ? undefined : "none" }}>{sent ? "Sent. We read every message and reply by email." : ""}</span>;
}

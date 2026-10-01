"use client";
import { useId, useState, type CSSProperties, type ReactNode } from "react";

/**
 * "Forgot password?" on the sign-in screen. Campus has no self-service reset: the school's own administrator resets a
 * password from the Administration portal (the guides list "Reset a guardian's password"). So the link opens a line
 * that says so, under the row it sits in. The design has no words for it (NOTES.md).
 */
export const FORGOT_NOTE = "Your school's Campus administrator resets passwords. Ask them to reset yours.";

export function ForgotPasswordRow({ rowStyle, linkStyle, noteStyle, children }: { rowStyle: CSSProperties; linkStyle: CSSProperties; noteStyle: CSSProperties; children: ReactNode }) {
  const [open, setOpen] = useState(false);
  const id = useId();
  return (
    <>
      <div style={rowStyle}>
        {children}
        <button type="button" style={linkStyle} aria-expanded={open} aria-controls={id} onClick={() => setOpen(!open)}>Forgot password?</button>
      </div>
      <p id={id} data-extra hidden={!open} style={noteStyle}>{FORGOT_NOTE}</p>
    </>
  );
}

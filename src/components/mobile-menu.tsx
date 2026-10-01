"use client";
import { useEffect, useState, type ReactNode } from "react";

/**
 * The phone menu button and its full-height sheet (ds.mobile_nav, open state). The drawings are rendered on the
 * server and passed in; this only switches between them.
 */
export function MobileMenu({ closedIcon, openIcon, sheet, buttonStyle }: { closedIcon: ReactNode; openIcon: ReactNode; sheet: ReactNode; buttonStyle: React.CSSProperties }) {
  const [open, setOpen] = useState(false);
  useEffect(() => {
    document.documentElement.style.overflow = open ? "hidden" : "";
    if (!open) return;
    const close = (e: KeyboardEvent) => e.key === "Escape" && setOpen(false);
    window.addEventListener("keydown", close);
    return () => window.removeEventListener("keydown", close);
  }, [open]);
  return (
    <>
      <button type="button" style={buttonStyle} aria-expanded={open} aria-controls="phone-menu" aria-label={open ? "Close menu" : "Open menu"} onClick={() => setOpen(!open)}>
        {open ? openIcon : closedIcon}
      </button>
      {open ? (
        <nav id="phone-menu" data-extra aria-label="Menu" onClick={(e) => (e.target as HTMLElement).closest("a") && setOpen(false)}
          style={{ position: "fixed", left: 0, right: 0, top: 64, bottom: 0, zIndex: 50, background: "#fff", overflowY: "auto" }}>
          {sheet}
        </nav>
      ) : null}
    </>
  );
}

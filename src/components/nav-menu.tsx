"use client";
import { useEffect, useRef, useState, type CSSProperties, type ReactNode } from "react";

/**
 * A nav item that opens its menu (ds.mega_departments, ds.mega_who): on hover, on click, and from the keyboard.
 * Escape, a click elsewhere, choosing a link or moving off the item closes it; opening one menu closes the other. The
 * menu and the chevrons are drawn on the server and passed in; the menu opens under the whole header.
 */
const OPENED = "campus:nav-menu";

export function NavMenu({ label, buttonStyle, down, up, menu, id }: { label: string; buttonStyle: CSSProperties; down: ReactNode; up: ReactNode; menu: ReactNode; id: string }) {
  const [open, setOpen] = useState(false);
  const wrap = useRef<HTMLSpanElement>(null);
  const timer = useRef<ReturnType<typeof setTimeout> | null>(null);
  /** when hover opened it: a click that follows straight after should not close it again */
  const hoverAt = useRef(0);
  const cancel = () => { if (timer.current) clearTimeout(timer.current); timer.current = null; };
  const later = (v: boolean, ms: number) => { cancel(); timer.current = setTimeout(() => { timer.current = null; if (v) hoverAt.current = Date.now(); setOpen(v); }, ms); };

  useEffect(() => {
    if (open) window.dispatchEvent(new CustomEvent(OPENED, { detail: id }));
    const other = (e: Event) => { if ((e as CustomEvent).detail !== id) { cancel(); setOpen(false); } };
    window.addEventListener(OPENED, other);
    return () => window.removeEventListener(OPENED, other);
  }, [open, id]);

  useEffect(() => {
    if (!open) return;
    const box = wrap.current!;
    const header = box.closest("header")!;
    const away = (e: Event) => { if (!header.contains(e.target as Node)) setOpen(false); };
    const esc = (e: KeyboardEvent) => { if (e.key === "Escape") { setOpen(false); (box.firstElementChild as HTMLElement).focus(); } };
    // anywhere in the header but this item and its menu: close, unless the pointer comes back
    const over = (e: MouseEvent) => { if (!box.contains(e.target as Node) && !timer.current) later(false, 160); };
    const leave = () => later(false, 160);
    document.addEventListener("mousedown", away);
    document.addEventListener("focusin", away);
    document.addEventListener("keydown", esc);
    header.addEventListener("mouseover", over);
    header.addEventListener("mouseleave", leave);
    return () => {
      document.removeEventListener("mousedown", away);
      document.removeEventListener("focusin", away);
      document.removeEventListener("keydown", esc);
      header.removeEventListener("mouseover", over);
      header.removeEventListener("mouseleave", leave);
    };
  }, [open]);
  useEffect(() => cancel, []);

  const toggle = () => {
    cancel();
    if (open && Date.now() - hoverAt.current < 400) return;
    hoverAt.current = 0;
    setOpen(!open);
  };

  return (
    <span ref={wrap} style={{ display: "contents" }} onMouseEnter={() => later(true, open ? 0 : 80)}>
      <button type="button" style={buttonStyle} aria-expanded={open} aria-controls={open ? id : undefined} onClick={toggle}>
        {label}{open ? up : down}
      </button>
      {open ? <div id={id} data-extra onClick={(e) => { if ((e.target as Element).closest("a")) setOpen(false); }}
        style={{ position: "absolute", left: 0, right: 0, top: 76, zIndex: 40, background: "#fff", boxShadow: "0 1px 0 #e7e9ef,0 30px 50px -30px rgba(11,12,20,.25)", cursor: "auto" }}>
        {menu}
      </div> : null}
    </span>
  );
}

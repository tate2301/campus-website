"use client";
import Image, { type ImageProps } from "next/image";
import { createContext, useContext, type ReactNode } from "react";

/**
 * Every route carries both layouts and CSS shows one (globals.css). A photograph in the hidden layout must not be
 * downloaded, but the photographs stay eager so a full-page screenshot never catches one half loaded. So each photo
 * sits in a <picture> whose <source> answers the hidden layout's media query with a blank pixel: the browser picks
 * that and never fetches the photo. Crossing 1024 px swaps them, as the layouts swap.
 */
type TreeName = "desktop" | "phone";
const TreeContext = createContext<TreeName | null>(null);

/** the media query under which this layout is hidden: the same breakpoint as .layout-desktop / .layout-phone */
const HIDDEN: Record<TreeName, string> = { desktop: "(max-width: 1023.98px)", phone: "(min-width: 1024px)" };
const BLANK = "data:image/gif;base64,R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7";

export function Tree({ name, children }: { name: TreeName; children: ReactNode }) {
  return <TreeContext.Provider value={name}>{children}</TreeContext.Provider>;
}

export function Photo(props: ImageProps) {
  const tree = useContext(TreeContext);
  const img = <Image {...props} />;
  if (!tree) return img;
  return (
    <picture style={{ display: "contents" }}>
      <source media={HIDDEN[tree]} srcSet={BLANK} />
      {img}
    </picture>
  );
}

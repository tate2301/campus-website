import { ogImage } from "@/og/card";
import { SW } from "@/content/copy";

const eyebrow = "Who we serve", h = SW.WHO.h as string;
export const alt = `${eyebrow}: ${h}`;
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";
export default function Image() {
  return ogImage({ eyebrow, h });
}

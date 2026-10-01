import { ogImage } from "@/og/card";
import { CP } from "@/content/copy";

const eyebrow = "Academics and student life", h = CP.ACADEMICS.h as string;
export const alt = `${eyebrow}: ${h}`;
export const size = { width: 1200, height: 630 };
export const contentType = "image/png";
export default function Image() {
  return ogImage({ eyebrow, h });
}

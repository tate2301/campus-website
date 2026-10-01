import { ogImage } from "@/og/card";
import { SW } from "@/content/copy";

export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

const DOCS: Record<string, string> = { privacy: "privacy", "data-ownership": "data", terms: "terms" };
export const generateStaticParams = () => Object.keys(DOCS).map((doc) => ({ doc }));

export default async function Image({ params }: { params: Promise<{ doc: string }> }) {
  const L: { title: string; h: string } = SW.LEGAL[DOCS[(await params).doc]];
  return ogImage({ eyebrow: L.title, h: L.h });
}

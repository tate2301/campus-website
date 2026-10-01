import { ogImage } from "@/og/card";
import { SW } from "@/content/copy";

export const size = { width: 1200, height: 630 };
export const contentType = "image/png";

const TYPES = Object.keys(SW.TYPES).map((k) => k.slice(2));
const ROLES = Object.keys(SW.ROLE_PAGES);
export const generateStaticParams = () => [...TYPES, ...ROLES].map((slug) => ({ slug }));

export default async function Image({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  const page = TYPES.includes(slug) ? SW.TYPES[`t-${slug}`] : SW.ROLE_PAGES[slug];
  return ogImage({ eyebrow: page.name, h: page.h });
}

import type { Metadata } from "next";
import { RolePage, TypePage } from "@/components/templates";
import { SW } from "@/content/copy";

/** the five kinds of school (t-day → /who-we-serve/day) and the six roles */
const TYPES = Object.keys(SW.TYPES).map((k) => k.slice(2));
const ROLES = Object.keys(SW.ROLE_PAGES);

export const dynamicParams = false;
export const generateStaticParams = () => [...TYPES, ...ROLES].map((slug) => ({ slug }));

export async function generateMetadata({ params }: { params: Promise<{ slug: string }> }): Promise<Metadata> {
  const { slug } = await params;
  const page = TYPES.includes(slug) ? SW.TYPES[`t-${slug}`] : SW.ROLE_PAGES[slug];
  return { title: page.name, description: page.b };
}

export default async function WhoWeServePage({ params }: { params: Promise<{ slug: string }> }) {
  const { slug } = await params;
  return TYPES.includes(slug) ? <TypePage k={`t-${slug}`} /> : <RolePage slug={slug} />;
}

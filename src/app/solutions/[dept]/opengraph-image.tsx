import { ogImage } from "@/og/card";
import { CP, SW } from "@/content/copy";

export const size = { width: 1200, height: 630 };
export const contentType = "image/png";
export const generateStaticParams = () => Object.keys(SW.DEPTS).map((dept) => ({ dept }));

const name = (slug: string) => (CP.DEPARTMENTS as string[][]).find((d) => d[1] === slug)![0];

export default async function Image({ params }: { params: Promise<{ dept: string }> }) {
  const { dept } = await params;
  return ogImage({ eyebrow: name(dept), h: SW.DEPTS[dept].h });
}

import type { Metadata } from "next";
import { DeptPage } from "@/components/templates";
import { CP, SW } from "@/content/copy";

/** the eight departments with a page of their own (Academics has its own route) */
export const dynamicParams = false;
export const generateStaticParams = () => Object.keys(SW.DEPTS).map((dept) => ({ dept }));

const name = (slug: string) => (CP.DEPARTMENTS as string[][]).find((d) => d[1] === slug)![0];

export async function generateMetadata({ params }: { params: Promise<{ dept: string }> }): Promise<Metadata> {
  const { dept } = await params;
  return { title: name(dept), description: SW.DEPTS[dept].b };
}

export default async function Department({ params }: { params: Promise<{ dept: string }> }) {
  const { dept } = await params;
  return <DeptPage slug={dept} />;
}

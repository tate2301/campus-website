import type { Metadata } from "next";
import { AcademicsPage } from "@/components/templates";
import { CP } from "@/content/copy";

export const metadata: Metadata = { title: "Academics and student life", description: CP.ACADEMICS.b };

export default function Academics() {
  return <AcademicsPage />;
}

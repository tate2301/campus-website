import { handleLead } from "@/lib/lead-route";

/** Book a demo: to the Corelith CRM, then Request sent. See src/lib/leads.ts. */
export async function POST(request: Request) {
  return handleLead(request, "demo");
}

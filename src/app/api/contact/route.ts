import { handleLead } from "@/lib/lead-route";

/** A message from the contact page: to the Corelith CRM, then back to the page with a confirmation. See src/lib/leads.ts. */
export async function POST(request: Request) {
  return handleLead(request, "contact");
}

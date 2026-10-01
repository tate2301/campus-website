import { CP, SW } from "./copy";

/** Where every navigation item, footer link, tile and card goes (spec/routes.json). */
export const NAV_HREF: Record<string, string> = { Solutions: "/solutions", "Who we serve": "/who-we-serve", Platform: "/platform", Pricing: "/pricing" };

export const FOOT_HREF: Record<string, string> = {
  Solutions: "/solutions", Platform: "/platform", Pricing: "/pricing", "Moving to Campus": "/moving-to-campus",
  Day: "/who-we-serve/day", Boarding: "/who-we-serve/boarding", Government: "/who-we-serve/government", Private: "/who-we-serve/private", Mission: "/who-we-serve/mission",
  // the company site is not part of this repo
  Corelith: "https://corelith.co.zw", Contact: "/contact", Support: "/support",
  Privacy: "/legal/privacy", "Data ownership": "/legal/data-ownership", Terms: "/legal/terms",
};

/** a department by its slug (CP.DEPARTMENTS[i][1]) */
export const deptHref = (slug: string) => `/solutions/${slug}`;
/** a school type by its key ("t-day") */
export const typeHref = (key: string) => `/who-we-serve/${key.slice(2)}`;
/** a role by its name (CP.ROLES[i][0]), in the order of SW.ROLE_PAGES */
export const roleHref = (name: string) => {
  const slug = Object.entries(SW.ROLE_PAGES as Record<string, { name: string }>).find(([, r]) => r.name === name)?.[0]
    ?? Object.keys(SW.ROLE_PAGES)[(CP.ROLES as string[][]).findIndex((r) => r[0] === name)];
  return `/who-we-serve/${slug}`;
};

export const LEGAL_HREF: Record<string, string> = { privacy: "/legal/privacy", data: "/legal/data-ownership", terms: "/legal/terms" };

/** actions, by the label the design gives them */
export const ACTION_HREF: Record<string, string> = {
  "Book a demo": "/demo", Demo: "/demo", "See pricing": "/pricing", "Download the price sheet (PDF)": "/pricing/price-sheet.pdf",
  "See who we serve": "/who-we-serve", "How we move your records": "/moving-to-campus", "See the integrations": "/platform/integrations",
  "Work out your school": "/pricing#calculator", "Go to support": "/support", "Write to us": "#message",
  "Open Help": "https://app.campus.corelith.co.zw", "Book a visit": "/contact#message", "Sign in": "/sign-in", "See the departments": "#departments",
};

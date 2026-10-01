/* eslint-disable @typescript-eslint/no-explicit-any */
import copy from "../../design/content/copy.json";

/**
 * All site copy, from design/content/copy.json (the two copy modules of the design, words.py and site_words.py,
 * plus the pricing FAQ, the three calls to action and the integrations marketplace). Nothing here is reworded.
 * CP and SW are the names the design source uses for the two modules.
 */
export const CP = copy.words as any;
export const SW = copy.site_words as any;
export const FAQ = copy.faq_pricing as [string, string][];
export const CTAS = copy.ctas as unknown as Record<"visit" | "price" | "training", [string, string, [string, string, string][]]>;
export const MARKET = copy.marketplace as [string, [string, string, string][]][];

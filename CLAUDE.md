# Corelith Campus website: build brief

You are building the marketing site for Corelith Campus, cloud-based school management software for K-12 schools. The design is finished and signed off on a canvas. Your job is to make the site match it pixel for pixel at both design widths, as a real, responsive, accessible Next.js site. Don't redesign, reword or "improve" anything. If something in the design looks wrong, list it in `NOTES.md` and build it as drawn.

## What is in this folder

| Path | What it is | How to use it |
|---|---|---|
| `spec/routes.json` | Every page: route, title, design widths and heights, and the reference and HTML files for each width | Your page list and your test list |
| `reference/desktop/*.jpg` | Each page rendered at 1440 px, 1x | What "done" looks like on desktop |
| `reference/phone/*.jpg` | Each page rendered at 390 px, 2x | What "done" looks like on a phone |
| `html/desktop/*.html`, `html/phone/*.html` | The exact markup and inline CSS each reference was rendered from. They open in a browser on their own. | Your source of truth for every size, colour, gap and radius. Read these, don't guess from the JPEGs. |
| `components/*.html` + `*.png` | The drawn pieces as exact markup fragments: the Campus mark, the menu icon, the 40-odd drawn icons, portal icons and scenes, the isometric department and school drawings, the call-to-action scenes, the schools campus, the animated mark journey, the integrations sketch and brand logos | Port each to a React component that outputs the same SVG. Never redraw them. |
| `components/mark-journey.css`, `components/hover-reveal.css` | The two animations: the mark travelling the campus (8 s loop) and the cards that reveal a photo on hover | Use them as they are |
| `content/copy.json` | Every string on the site, from the two copy modules | All copy comes from here. Don't rewrite it. |
| `spec/tokens.css`, `spec/tokens.json` | Colours, fonts, radii, shadows, layout | Map them into your Tailwind theme as CSS variables |
| `spec/rules.md`, `spec/voice.md`, `spec/positioning.md` | The art direction, voice and positioning the design follows | Read before you start. They explain why things are the way they are. |
| `spec/assets-and-licences.md` | Source and licence for every photo and logo | Keep it in the repo |
| `assets/photos`, `assets/logos` | Every photograph and third-party logo the pages use | Serve them with `next/image` using the `object-position` given in the HTML |
| `source/*.py` | The Python that generated every board | The ground truth when the HTML leaves a value unclear |
| `tests/` | A Playwright visual test against the references | Your acceptance test (below) |

## Stack

- Next.js (App Router), TypeScript, React Server Components by default, static generation for every marketing route.
- Tailwind CSS with the tokens from `spec/tokens.css` as CSS variables. No component library.
- Fonts: General Sans (400, 500, 600) for everything, through `next/font/local` from files `scripts/fonts.mjs` fetches (the licence forbids committing them; see `docs/typography.md`, which replaces Atkinson Hyperlegible Next and sets the type rules), and through `next/font/google`: Inter only inside the phone mock-ups, IBM Plex Mono (400, 500), and Newsreader for the one report document.
- `next/image` for photographs. Logos and drawings stay inline SVG.
- The price sheet at `/pricing/price-sheet.pdf` is a generated A4 PDF that matches `reference/desktop/price-sheet.jpg`.
- Sign-in lives on the app domain (`app.campus.corelith.co.zw`). Build it as `/sign-in` in this repo as a static screen; each school reaches it on its own address, so there is no school picker.

## Layout

- Desktop design: 1440 wide, 120 px gutters, a 1200 px content column, 160 px between sections.
- Phone design: 390 wide, 20 px gutters, 96 px between sections, one column, text first and then one picture.
- Between the two: use the phone layout up to 1023 px with the column capped at 560 px and centred. Use the desktop layout from 1024 px, with the gutter `clamp(40px, 8.3vw, 120px)` and the content column capped at 1200 px.
- Product cards in phone pictures are never scaled down. They sit at their own size over the lower edge of the photo.
- Headings use `text-wrap: balance`.
- Section heads are an eyebrow (blue, with its drawn icon) and a headline only. There are no descriptions beside section heads.
- Cards in a row are equal height, with the action on the bottom line.
- "by Corelith" appears only in the nav lockup.

## Components to build first

Build these as shared components, each matched against its fragment or a page in the reference, before you assemble any page:

1. Nav (desktop, and phone with the menu icon and open state), and the footer with the "Who we serve" photo strip.
2. Eyebrow, headline, paragraph, buttons (`cbtn` in `source/ds.py`: pill, icon after the label, three sizes), explore link.
3. Page hero (centred type, picture below), the photo-with-tagged-cards picture, the dotted plate, and the alternating row (text 500 px, picture 620 px, 96 px apart).
4. Department tile, role tile, link card, features list, FAQ list, the call-to-action block with its drawing.
5. The product cards in `source/site_cards.py`, `source/ui.py` and `source/who_sections.py`. They are static mock-ups with fixed world data (Mukuvisi High School, Tanaka Moyo, Form 3B, Tsavo House). Keep every figure exactly as drawn; they add up across pages.
6. The two phone mock-ups (`parent_app` in `source/pages.py`, `rollcall_app` in `source/who_sections.py`). Build them at 393 × 852 and scale them as a whole.

Then build the pages in the order of `spec/routes.json`.

## Accessibility and behaviour

- Real `<a href>` and `<button>`. Every link in the nav, footer, tiles and cards goes to its route in `spec/routes.json`.
- Alt text on every photograph: describe the people and the place, not "stock photo".
- Respect `prefers-reduced-motion`: freeze the mark journey on its final frame.
- The phone menu opens a full-height sheet, as drawn in the design system (the `menu-icon-open` fragment shows the open state).
- Forms (book a demo, contact) post to an API route that you stub. Show the "Request sent" page after a successful demo request.

## Acceptance: pixel for pixel

`tests/visual.spec.ts` loads every route at 1440 (1x) and 390 (2x), takes a full-page screenshot and compares it with the reference, after freezing animations at the same frame the references used (`animation-delay: -3.5s`, paused).

- Each route must differ from its reference by at most 0.5% of pixels (pixelmatch threshold 0.1).
- The page height must be within 4 px of the reference.
- Run it with `BASE_URL=http://localhost:3000 npx playwright test`.
- When a route fails, open its `html/` file next to your page in the browser and fix the difference. Don't change the test or the references.

## Working rules

- Copy comes only from `content/copy.json`, in British English. The price is always written "US$1 per active pupil per month".
- Every value comes from the HTML or the source. Don't round anything to a Tailwind default if the design says 13.5 px or 18 px.
- Don't add sections, testimonials, statistics, logos or features that are not in the design.
- Commit page by page, with the route in the message.

<!-- BEGIN:nextjs-agent-rules -->

# This is NOT the Next.js you know

This version has breaking changes — APIs, conventions, and file structure may all differ from your training data. Read the relevant guide in `node_modules/next/dist/docs/` (resolved from this file's directory; in monorepos the `next` package may not be visible from the repo root) before writing any code. Heed deprecation notices.

This block is written and re-added by `next dev` — verify at `node_modules/next/dist/server/lib/generate-agent-files.js`. Removing it from a diff only re-creates the uncommitted change; committing it with your work keeps the tree clean.

<!-- END:nextjs-agent-rules -->

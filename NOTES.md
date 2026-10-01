# Notes: what could not be matched, and why

Status on 1 October 2026, from `npm run test:visual` (the acceptance test, unchanged) and `npm run parity`.

## The result

**50 of 70 checks pass the acceptance test.** Of the other 20:

- 9 are the pages now built to `rules.md` rather than as drawn, at the client's request: Pricing and Book a demo, both
  widths, and the five school-type pages on a phone. Their references show the drawn version (see "Where the drawn
  pages disagree with `rules.md`").
- 10 are within 0.1 points of what the reference's own JPEG compression costs that page.
- 1, sign-in on a phone, matches its reference's pixels (0.45%) but not its height, which the test can't measure as
  drawn.

| | Checks |
|---|---|
| Pass (≤ 0.5% of pixels, height within 4 px) | 50 |
| Built to `rules.md`, so different from the drawn reference | 9 |
| Over 0.5%, but within 0.1 points of the JPEG floor (see below) | 10 |
| Height cannot match the reference (sign-in, phone) | 1 |

Before the `rules.md` changes, 56 passed and the demo page and desktop Pricing were at the floor. The drop-down menus
and the photo loading change no page's pixels.

The full table is at the end of this file.

## Why some pages can't get under 0.5%

### 1. The references are JPEGs, and JPEG alone moves 0.2–1.6% of a page's pixels

`design/source/handover.py` saves every reference as a JPEG at quality 86. Around text, JPEG's 8×8 blocks and halved
colour resolution shift enough pixels past pixelmatch's threshold (0.1) to count as different. Taking a page's own
render and saving it the same way already gives:

- 0.18–0.40% for photo-heavy pages
- 0.45–0.68% for text-heavy pages (the legal pages, pricing, the demo page, Home)
- 1.56% for the price sheet

Above 0.5% that floor makes the test impossible to pass, however exact the page is. `npm run parity` prints each page's
floor next to its result; every route that fails the test, apart from the rules.md pages and phone sign-in, is within 0.1
points of its floor, i.e. its remaining differences are the JPEG's, not the build's. (The floor uses a different JPEG encoder from the one that made the
references, so it is an estimate; a few pages that pass sit up to 0.09 above it.)

### 2. Sign in, phone: the screen is 844 px tall, the test's window is 900

The phone sign-in is a full phone screen (390 × 844). The test opens a 390 × 900 window and takes a full-page
screenshot, which is never shorter than the window, so it measures 900 against the reference's 844. The page itself
matches its reference to 0.45%. The design's own HTML fails the same way.

### 3. The demo and contact forms have no example person in them

The design shows the forms filled in for "Chipo Mutasa" at Mukuvisi High School. A working form shouldn't arrive
filled with someone else's details, so the fields are empty and the design's values are their placeholders (faint
grey rather than ink). The checkboxes for the kind of school start unticked; "Visit the school" stays chosen. This
cost the demo page about 0.05–0.08 points over its floor before it gained the Training section; contact and sign-in
still pass.

## Things found in the handover

### The design HTML is not what the references were rendered from

`design/html/*.html` loads fonts from Google Fonts. The references were rendered by `source/crender.py` with a local
`direction/fonts.css` that is not in the handover. Today Google Fonts serves a browser slightly different files from
the ones that rendered the references (Atkinson Hyperlegible Next v7 differs by a few bytes), so the design HTML,
opened as it is, misses its own references by 1–3% on desktop and up to 17% on phone (lines rewrap and push the page
by up to 90 px). `next/font` downloads the files that match the references, so the site matches them more closely than
the design HTML does. Newsreader had to be requested at its two static weights to match (the authority report on
Mission schools).

`npm run parity` still compares every page with the design HTML too: the structure and every drawn piece are taken
from it, so that comparison catches structural mistakes even though its pixel figure includes the font difference.

### The generator code is incomplete

`design/source/*.py` imports the Corelith company kit (`/home/claude/corelith-co/kit`: the logo, MingCute icons, the
`iso5` isometric drawing library) and an `sdkit` icon set, none of which are in the handover. So the drawings could not
be regenerated. Instead:

- Interface glyphs (`ic(name, size, colour)`) are MingCute from `@iconify-json/mingcute`: `-line` names as they are,
  every other name in its `-fill` form. Every glyph on every page matches this rule exactly.
- Every other drawn piece is the exact markup exported in `design/html`, kept in `src/art/registry.json` and rendered as
  React elements. `scripts/extract-art.mjs` fills it by matching positions in the page, and `design/components` seeds the
  pieces no exported page shows (the open menu icon). The drawings are generated per size, so the same department at
  two sizes is two pieces.

### Copy that is not in copy.json

`content/copy.json` holds the two copy modules, but the Python writes more text inline: card figures and labels, the
interface text ("Explore", "Forgot password?", "© 2026 Corelith Labs", "Harare, Zimbabwe"), section headlines on some
pages ("Everything the school keeps, on one record.", "What schools ask about the price.") and the three next steps on
Request sent. These are copied verbatim from `design/source` into the components that draw them, and marked there.

Added because the design has no words for them:

- The role list on Book a demo. The design shows "Head" chosen; the options are Head, Deputy head, Bursar, SDC member,
  Teacher, Other.
- What the forms say (`src/content/form-messages.ts`), worded after corelith.co.zw's own forms: one line per field that
  needs fixing, "That's a few submissions in a row…", "We couldn't save your request just now. Please email
  hello@corelith.co.zw…", and, after a contact message is sent, "Sent. We read every message and reply by email." (the
  second sentence is the form's own copy).
- Under "Forgot password?": "Your school's Campus administrator resets passwords. Ask them to reset yours." The site's
  copy never says "workspace"; the people who run a school's Campus work in the Administration portal.
- Accessible names: "Open menu", "Close menu", "Topic", "Package", "Search the guides", and the mark journey's
  description.

### Where the drawn pages disagree with `rules.md`: built to `rules.md`, as asked

These were first built as drawn and flagged; the client asked for the `rules.md` version. Each costs its page the
acceptance test, because the references show the drawn version.

- **Pricing closes with the Price call to action** (the drawn page has Visit). "Work out your school" goes to the
  calculator on the same page. The phone has no Price drawing of its own, so it shows the 600 × 430 drawing scaled to
  the column, as the phone does with other wide pictures. Desktop now differs from its reference by 1.20%; the phone page
  is 36 px taller.
- **The demo page closes with the Training call to action** (the drawn page has none). "Book a demo" goes back up to the
  form. The page is 637 px taller on desktop and 585 px on the phone.
- **Phone school-type pages have 96 px between sections** (the drawn pages have 192 between some, because `mobile.m_day`
  and the others add a gap and `type_page` adds another). Four of the five pages are 192 px shorter than their
  references, Mission 96.

### Other inconsistencies, built as drawn

- **The nav marks the section you are in by drawing its menu open** (grey pill, chevron up) on every page in that
  section. Now that the menus open, the chevron shows whether the menu is open; the section you are in keeps the grey
  pill.
- `who_sections.boarding_sections` builds a "houses at lights out" panel that no page uses. It isn't built.
- The school types' `rows` in `site_words.py` (copy.json `site_words.TYPES.*.rows`) are not used: the type pages are
  built from `who_sections` instead. So `transport_card`, used only there, appears on no page, and neither does
  `signin_card`. Both cards are ported; the rows' copy is not on the site.

## Decisions to check

- **Both layouts are in every page.** The design draws the phone pages separately (different order, sizes and pictures),
  so each route renders both and CSS shows one: phone up to 1023 px, desktop from 1024 px. The hidden layout is out of
  the accessibility tree, and its photographs are not downloaded: each photograph is a `<picture>` whose `<source>`
  answers the hidden layout's media query with a blank pixel (`src/components/photo.tsx`), so the browser fetches only
  the visible layout's photos (Home: 8 at 1440, 9 at 390, of 17). Photographs stay eager, so full-page screenshots never
  catch one half loaded. Crossing 1024 px loads the other layout's photos as it appears.
- **Between 1024 and 1439 px the desktop layout is zoomed as a whole** to the window's width. That gives exactly the
  brief's `clamp(40px, 8.3vw, 120px)` gutter and 1200 px column at every width, and the drawn pictures (cards placed
  over photographs) keep their proportions. Above 1440 the gutters grow and the column stays 1200, centred. The gutter
  uses `8.334vw` rather than `8.3vw` so the design width gets exactly 120 px (8.3vw is 119.5 px at 1440).
- **Photographs are served unoptimised** (`images.unoptimized`). `next/image` is used for them, but Next's re-encoding
  changes every pixel of every photo, which the visual test counts.
- **Inline styles.** Components carry the design's values as inline CSS strings (`sx("font:600 52px/1.08 …")`), copied
  from the source, rather than Tailwind classes, so each can be checked against the function it ports. Tailwind provides
  the theme (tokens as CSS variables) without its preflight reset, which would change line heights the design depends on.
- **Links the design doesn't specify:** "Corelith" in the footer goes to https://corelith.co.zw (confirmed: Corelith's
  own site). "Forgot password?" links nowhere: passwords are reset by the school's own administrator (confirmed), so it
  opens a line under the row that says so. "Open Help" and the guide search go to the app, at
  app.campus.corelith.co.zw as the brief names it; corelith.co.zw has no Campus app links to confirm those paths
  against, so **they still need confirming**, as does the address the sign-in form posts to. "Book a visit" goes to the contact form.
- **The drop-down menus** are built from the design-system board (`ds.mega_departments`, `ds.mega_who`): Solutions opens
  the nine departments and the Moving to Campus panel, Who we serve opens the school types and the roles. They open on
  hover or click and work from the keyboard (Enter or Space opens, Tab moves through, Escape closes and returns to the
  button). Only one is open at a time. They close when you click elsewhere, move off the nav or choose a link. The board
  draws the first department highlighted; that is the hover and focus state. The design exported the school buildings at
  44 px but not the department or portal drawings, so those are the 48 px drawing scaled to 44. The menus are desktop
  only; the phone has its own menu sheet.
- The guide titles on Support are not links (the guides live in the app).
- **The phone FAQ is an accordion**, as drawn (first question open): `<details>`, with the chevron turned when open.
- **Reduced motion** stops the mark journey at 90% of its loop, with the mark delivered to all four places (the loop's
  last frame is empty).

## The forms

Book a demo and Contact send to Corelith's own CRM, the same intake corelith.co.zw's forms use (its `lib/leads.ts` and
`docs/FORMS.md`): `POST {host}/api/public/crm/webhook/leads` with the key in `x-api-key`. The CRM finds or creates the
client, opens a lead at stage New and notifies whoever the key routes to.

- **Setup:** set `CORELITH_CRM_API_KEY` (a `crm_` key minted in the tenant under CRM → Settings → API keys, with no
  default channel). `CORELITH_CRM_URL` points a staging build at another host; it defaults to Corelith's tenant. Until
  the key is set, a submission is only written to the server log, and the visitor still sees it as sent.
- **What arrives:** name, email, phone (with `phoneCountry: ZW`), `services: ["Campus"]`, the source ("Campus demo
  request" or "Campus enquiry") and the campaign tags. The webhook has no custom fields, so the school, role, number of
  pupils, kind of school, how to show it and the contact topic are written at the top of the lead's note, with the
  visitor's own message last.
- **Spam:** a hidden field, a minimum time on the page (2.5 s), and five sends a minute per address. The last one counts
  per server instance, so it's only a speed bump; put the host's rate limiting in front of it.
- **Failure:** if the CRM refuses or doesn't answer within 8 s, the visitor is asked to email hello@corelith.co.zw, and
  the submission is still in the server log.
- **Without JavaScript** the forms still post; the server redirects to Request sent, or back with the message.
- **Campaign tags:** corelith.co.zw remembers the page a visit started on, but only with cookie consent, and the Campus
  design has no consent banner. So Campus stores nothing: it sends the tags on the page the form is on, and an external
  referrer. Ads should point at the form's page, or a consent banner should be added first.

Checked end to end against a stand-in CRM, at both widths in a browser and with plain posts. Both forms arrived with the
right fields and campaign tags. The demo went on to Request sent; the contact form showed its line and cleared.

## Results by route

Percentages are pixels differing from the reference (the acceptance test's figure); floor is what JPEG alone costs that
page; height is the difference from the reference in CSS pixels.

| Route | Desktop | Phone |
|---|---|---|
| `/` | 0.53% (floor 0.53%), at floor | 0.36% (floor 0.35%), passes |
| `/solutions` | 0.56% (floor 0.56%), at floor | 0.42% (floor 0.40%), passes |
| `/solutions/academics` | 0.45% (floor 0.45%), passes | 0.31% (floor 0.30%), passes |
| `/solutions/admissions` | 0.44% (floor 0.44%), passes | 0.33% (floor 0.33%), passes |
| `/solutions/fees` | 0.45% (floor 0.45%), passes | 0.34% (floor 0.34%), passes |
| `/solutions/accounting` | 0.45% (floor 0.45%), passes | 0.36% (floor 0.36%), passes |
| `/solutions/hr-payroll` | 0.42% (floor 0.42%), passes | 0.33% (floor 0.33%), passes |
| `/solutions/boarding` | 0.41% (floor 0.41%), passes | 0.30% (floor 0.30%), passes |
| `/solutions/stock` | 0.42% (floor 0.42%), passes | 0.32% (floor 0.32%), passes |
| `/solutions/communication` | 0.39% (floor 0.39%), passes | 0.31% (floor 0.31%), passes |
| `/solutions/insights` | 0.40% (floor 0.40%), passes | 0.29% (floor 0.29%), passes |
| `/who-we-serve` | 0.40% (floor 0.40%), passes | 0.28% (floor 0.28%), passes |
| `/who-we-serve/day` | 0.47% (floor 0.47%), passes | 19.98% (floor 0.36%, −192 px), rules.md version |
| `/who-we-serve/boarding` | 0.48% (floor 0.48%), passes | 13.72% (floor 0.35%, −192 px), rules.md version |
| `/who-we-serve/government` | 0.51% (floor 0.51%), at floor | 12.76% (floor 0.37%, −193 px), rules.md version |
| `/who-we-serve/private` | 0.43% (floor 0.43%), passes | 15.12% (floor 0.31%, −192 px), rules.md version |
| `/who-we-serve/mission` | 0.48% (floor 0.48%), passes | 12.09% (floor 0.36%, −96 px), rules.md version |
| `/who-we-serve/leadership` | 0.41% (floor 0.41%), passes | 0.30% (floor 0.30%), passes |
| `/who-we-serve/bursary` | 0.45% (floor 0.45%), passes | 0.34% (floor 0.34%), passes |
| `/who-we-serve/teachers` | 0.44% (floor 0.44%), passes | 0.33% (floor 0.33%), passes |
| `/who-we-serve/boarding-staff` | 0.43% (floor 0.43%), passes | 0.32% (floor 0.32%), passes |
| `/who-we-serve/parents` | 0.43% (floor 0.43%), passes | 0.32% (floor 0.32%), passes |
| `/who-we-serve/pupils` | 0.43% (floor 0.43%), passes | 0.34% (floor 0.34%), passes |
| `/platform` | 0.50% (floor 0.50%), at floor | 0.35% (floor 0.33%), passes |
| `/platform/integrations` | 0.49% (floor 0.49%), passes | 0.48% (floor 0.39%), passes |
| `/moving-to-campus` | 0.49% (floor 0.49%), passes | 0.40% (floor 0.40%), passes |
| `/pricing` | 1.20% (floor 0.59%), rules.md version | 3.89% (floor 0.38%, −36 px), rules.md version |
| `/pricing/price-sheet.pdf` | 1.56% (floor 1.56%), at floor | — |
| `/demo` | 3.78% (floor 0.63%, +637 px), rules.md version | 4.54% (floor 0.43%, +585 px), rules.md version |
| `/demo/sent` | 0.32% (floor 0.32%), passes | 0.26% (floor 0.26%), passes |
| `/sign-in` | 0.30% (floor 0.22%), passes | 0.45% (floor 0.18%, +56 px), height |
| `/contact` | 0.41% (floor 0.37%), passes | 0.34% (floor 0.25%), passes |
| `/support` | 0.37% (floor 0.37%), passes | 0.26% (floor 0.26%), passes |
| `/legal/privacy` | 0.67% (floor 0.67%), at floor | 0.68% (floor 0.67%), at floor |
| `/legal/data-ownership` | 0.52% (floor 0.52%), at floor | 0.53% (floor 0.53%), at floor |
| `/legal/terms` | 0.53% (floor 0.53%), at floor | 0.54% (floor 0.53%), at floor |

"Passes": within the acceptance test's limits. "At floor": over 0.5%, but within 0.1 points of the JPEG floor.
"rules.md version": the page now follows `rules.md` where the drawn page doesn't (see above), so it differs from its
reference by design; heights are the difference from the reference.
The price sheet is not in the acceptance test (it is checked as a PDF, by eye); its source page is compared here.

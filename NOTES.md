# Notes: what could not be matched, and why

Status on 1 October 2026, from `npm run test:visual` (the acceptance test, unchanged) and `npm run parity`.

## The result

**56 of 70 checks pass the acceptance test. Of the other 14, 13 are within 0.1 points of what the reference's own JPEG
compression costs that page, and the last (sign-in on a phone) matches its pixels (0.45%) but not its height, which the
test cannot measure as drawn.**

| | Checks |
|---|---|
| Pass (≤ 0.5% of pixels, height within 4 px) | 56 |
| Over 0.5%, but within 0.1 points of the JPEG floor (see below) | 13 |
| Height cannot match the reference (sign-in, phone) | 1 |

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
floor next to its result; every route that fails the test is within 0.1 points of its floor, i.e. its remaining
differences are the JPEG's, not the build's. (The floor uses a different JPEG encoder from the one that made the
references, so it is an estimate; a few pages that pass sit up to 0.09 above it.)

### 2. Sign in, phone: the screen is 844 px tall, the test's window is 900

The phone sign-in is a full phone screen (390 × 844). The test opens a 390 × 900 window and takes a full-page
screenshot, which is never shorter than the window, so it measures 900 against the reference's 844. The page itself
matches its reference to 0.45%. The design's own HTML fails the same way.

### 3. The demo and contact forms have no example person in them

The design shows the forms filled in for "Chipo Mutasa" at Mukuvisi High School. A working form shouldn't arrive
filled with someone else's details, so the fields are empty and the design's values are their placeholders (faint
grey rather than ink). The checkboxes for the kind of school start unticked; "Visit the school" stays chosen. This
costs the demo page about 0.05–0.08 points over its floor; contact and sign-in still pass.

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
- After a contact message is sent: "Sent. We read every message and reply by email." (the second sentence is the
  form's own copy).
- Accessible names: "Open menu", "Close menu", "Topic", "Package", "Search the guides", and the mark journey's
  description.

### Inconsistencies, built as drawn

- **Pricing closes with the Visit call to action**, though `rules.md` says the Price one closes Pricing.
- **The demo page has no call to action**, though `rules.md` says Training closes it.
- **Phone school-type pages put 192 px between their own sections** (`mobile.m_day` and the others add a gap, and
  `type_page` adds another); desktop uses 160.
- **The nav marks the section you are in by drawing its menu open** (grey pill, chevron up) on every page in that
  section.
- `who_sections.boarding_sections` builds a "houses at lights out" panel that no page uses. It isn't built.
- The school types' `rows` in `site_words.py` (copy.json `site_words.TYPES.*.rows`) are not used: the type pages are
  built from `who_sections` instead. So `transport_card`, used only there, appears on no page, and neither does
  `signin_card`. Both cards are ported; the rows' copy is not on the site.

## Decisions to check

- **Both layouts are in every page.** The design draws the phone pages separately (different order, sizes and pictures),
  so each route renders both and CSS shows one: phone up to 1023 px, desktop from 1024 px. The hidden layout is out of
  the accessibility tree, but its photographs are still fetched, because they load eagerly (lazy images below the fold
  would be missing from a full-page screenshot). Once the pixel gate is retired, switching the photographs to
  `loading="lazy"` stops that.
- **Between 1024 and 1439 px the desktop layout is zoomed as a whole** to the window's width. That gives exactly the
  brief's `clamp(40px, 8.3vw, 120px)` gutter and 1200 px column at every width, and the drawn pictures (cards placed
  over photographs) keep their proportions. Above 1440 the gutters grow and the column stays 1200, centred. The gutter
  uses `8.334vw` rather than `8.3vw` so the design width gets exactly 120 px (8.3vw is 119.5 px at 1440).
- **Photographs are served unoptimised** (`images.unoptimized`). `next/image` is used for them, but Next's re-encoding
  changes every pixel of every photo, which the visual test counts.
- **Inline styles.** Components carry the design's values as inline CSS strings (`sx("font:600 52px/1.08 …")`), copied
  from the source, rather than Tailwind classes, so each can be checked against the function it ports. Tailwind provides
  the theme (tokens as CSS variables) without its preflight reset, which would change line heights the design depends on.
- **Links the design doesn't specify:** "Corelith" in the footer goes to https://corelith.co.zw; "Open Help",
  "Forgot password?" and the guide search go to the app (app.campus.corelith.co.zw); "Book a visit" goes to the contact
  form.
- **Not built:** the Solutions and Who we serve drop-down menus drawn on the design-system board (DS04). The nav items
  link to their section pages. The guide titles on Support are not links (the guides live in the app).
- **The phone FAQ is an accordion**, as drawn (first question open): `<details>`, with the chevron turned when open.
- **Reduced motion** stops the mark journey at 90% of its loop, with the mark delivered to all four places (the loop's
  last frame is empty).

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
| `/who-we-serve/day` | 0.47% (floor 0.47%), passes | 0.35% (floor 0.35%), passes |
| `/who-we-serve/boarding` | 0.48% (floor 0.48%), passes | 0.34% (floor 0.34%), passes |
| `/who-we-serve/government` | 0.51% (floor 0.51%), at floor | 0.36% (floor 0.36%), passes |
| `/who-we-serve/private` | 0.43% (floor 0.43%), passes | 0.30% (floor 0.30%), passes |
| `/who-we-serve/mission` | 0.48% (floor 0.48%), passes | 0.36% (floor 0.36%), passes |
| `/who-we-serve/leadership` | 0.41% (floor 0.41%), passes | 0.30% (floor 0.30%), passes |
| `/who-we-serve/bursary` | 0.45% (floor 0.45%), passes | 0.34% (floor 0.34%), passes |
| `/who-we-serve/teachers` | 0.44% (floor 0.44%), passes | 0.33% (floor 0.33%), passes |
| `/who-we-serve/boarding-staff` | 0.43% (floor 0.43%), passes | 0.32% (floor 0.32%), passes |
| `/who-we-serve/parents` | 0.43% (floor 0.43%), passes | 0.32% (floor 0.32%), passes |
| `/who-we-serve/pupils` | 0.43% (floor 0.43%), passes | 0.34% (floor 0.34%), passes |
| `/platform` | 0.50% (floor 0.50%), at floor | 0.35% (floor 0.33%), passes |
| `/platform/integrations` | 0.49% (floor 0.49%), passes | 0.48% (floor 0.39%), passes |
| `/moving-to-campus` | 0.49% (floor 0.49%), passes | 0.40% (floor 0.40%), passes |
| `/pricing` | 0.59% (floor 0.59%), at floor | 0.39% (floor 0.39%), passes |
| `/pricing/price-sheet.pdf` | 1.56% (floor 1.56%), at floor | — |
| `/demo` | 0.73% (floor 0.68%), at floor | 0.54% (floor 0.46%), at floor |
| `/demo/sent` | 0.32% (floor 0.32%), passes | 0.26% (floor 0.26%), passes |
| `/sign-in` | 0.30% (floor 0.22%), passes | 0.45% (floor 0.18%, +56 px), height |
| `/contact` | 0.41% (floor 0.37%), passes | 0.34% (floor 0.25%), passes |
| `/support` | 0.37% (floor 0.37%), passes | 0.26% (floor 0.26%), passes |
| `/legal/privacy` | 0.67% (floor 0.67%), at floor | 0.68% (floor 0.67%), at floor |
| `/legal/data-ownership` | 0.52% (floor 0.52%), at floor | 0.53% (floor 0.53%), at floor |
| `/legal/terms` | 0.53% (floor 0.53%), at floor | 0.54% (floor 0.53%), at floor |

"Passes": within the acceptance test's limits. "At floor": over 0.5%, but within 0.1 points of the JPEG floor.
The price sheet is not in the acceptance test (it is checked as a PDF, by eye); its source page is compared here.

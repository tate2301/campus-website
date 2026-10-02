# Typography: sources, rules and how this site applies them

October 2026. Written for two uses: the record of why the Corelith Campus site is set the way it is, and the material
for the typography section of the saas-design plugin. Part 1 is the rule set, ready to lift into the plugin. Part 2 is
how this site applies it. Part 3 lists every source, who wrote it and what it says.

Everything in the sources is paraphrased; the few quotations are short and attributed. Where sources disagree, the
disagreement is stated and the choice made here is named.

---

## Part 1. The rules (for the plugin)

Each rule cites its sources by key: **PC** Pierrick Calvez, **PT** Practical Typography (Butterick), **ETS** Elements
of Typographic Style Applied to the Web (Rutter, after Bringhurst), **TH** Typography Handbook, **IF** Interface
Cheat Sheet (Krehel), **JK** Details that make interfaces feel better (Krehel), **YT** Yep! Type on UI fonts,
**RS** The Concept of Taste (Salaja).

### 1. Choosing the typeface

1. **Pick one family and stop.** One family with at least four weights covers a marketing site and its product
   cards (PC: "Don't nerd over typefaces, just pick one"). A second family needs a fixed job of its own (PT: mixing
   fonts is optional; most documents take two, few take three).
2. **Test a UI face on two numbers before liking its look (YT).**
   - x-height at least 70% of cap height, ideally 75%. Below 70% a label looks like it sits low and padding can't
     fix it.
   - Cap-centred vertical metrics: the space above the capitals equals the space below the baseline, so a label
     centres in a button or pill with one padding value at every size. If a font fails this, fix it in the
     `@font-face` with `ascent-override`/`descent-override` (or `text-box: trim-both cap alphabetic` where
     supported), never with per-size padding nudges.
3. **Check the features you rely on.** Tabular figures (`tnum`), real small caps (`smcp`) and kerning (`kern`) must be
   in the font; CSS can't make them (PT, ETS). If the text face has no tabular figures, set changing or aligned figures
   in a second face that has them.
4. **Licence first.** Free on Google Fonts (OFL) can be committed and subset. Fontshare's ITF Free Font License
   allows self-hosting for your own site but not redistribution through a public repository, subsetting or format
   conversion. Commercial faces need a web licence. Never copy another site's webfont files.
5. **Serve WOFF2**, `font-display: swap`, preload only the one or two faces above the fold, and match the fallback's
   metrics to limit layout shift (IF, TH). `next/font` does all of this.
6. **Taste is the fundamentals.** Composition, hierarchy and clarity outlast trends. Type sets the tone before a word
   is read, so the face is a brand decision, not a default. Usability first, character on top (RS).

### 2. Size and scale

1. **Body text 15–25 px on screens** (PT), 14–25 px (PC). 12 px is too small for anything people read (PC). Interface
   labels in dense cards can go to 12–14 px.
2. **Use a short list of sizes, not ad-hoc ones.**
   - Classical series: 12 14 16 18 21 24 36 48 60 72 (ETS).
   - A modular scale, e.g. 1.25 on a 16 px base, made fluid with `clamp()` and a rem minimum (TH).
   - "In doubt, multiply by two" between levels: 100 / 50 / 25 (PC).
   - PT disagrees with fixed scales ("if headings look right, they are right") and warns against huge web headings.
   - **Synthesis:** allowed sizes, 1 px apart for interface text (emphasis in small steps, PT), wider apart for reading
     and display sizes (ETS); each heading level a clear step from the next (PC); headings no bigger than they need to
     be (PT).
3. **Hierarchy through contrast.** Big differences, not small ones: size, weight, space and colour together (PC, TH).
   "In doubt, skip a weight": e.g. 600 / 400, not 500 / 400 (PC).
4. **At most three heading levels; two is better** (PT).

### 3. Leading (line-height)

1. Unitless `line-height` (PT, ETS, TH).
2. **Reading text 1.4–1.5.** PT says 1.2–1.45; ETS 1.3 and up, using 1.5; PC 1.5 for long text and 1.2 for a short
   paragraph; TH's specimen 1.55. Add about 0.1 for every 10 characters past 65 per line (TH).
3. **Display type tighter.** Large headings 1.0–1.15. Below 1 is fine for short display lines if ascenders and
   descenders don't collide (ETS).
4. Smaller text (captions, card text) 1.4–1.45.

### 4. Measure (line length)

1. **45–75 characters per line; about 66 is ideal** (ETS, TH). PT allows 45–90, PC 40–70, IF 60–75.
2. Interface text, captions and notes: 35–50 (TH).
3. Cap the width of text containers (`max-width`) rather than letting text run the width of the window. In px or em,
   not `ch`: `ch` is the width of a zero, not of an average letter (PT; TH uses `65ch` anyway). Roughly 0.5 em per
   character: 66 characters ≈ 33 em (ETS).
4. Let the measure shrink on phones rather than shrinking the type (TH). Check line length first in responsive
   layouts (PT).

### 5. Tracking, kerning and ligatures

1. **Never letter-space lowercase body text** (PT, ETS).
2. **Tighten large type a little as it grows**; PT allows removing space from large lowercase headlines. Don't
   overdo it: ETS warns that heavy negative tracking hurts legibility. TH's specimen tracks its H1 at −0.025 em.
3. **Open very small text a touch** (PT: below about 9 pt).
4. **Capitals and small caps +5–12%** (`0.05em`–`0.12em`), built into the caps style itself (PT, ETS). Set capitals
   with `text-transform`, not by typing them (IF, PT). All caps for less than one line only (PT).
5. **Kerning always on** (`font-kerning: normal`) (PT, TH); kern display type by eye where pairs still gap (PC, ETS).
   Common and contextual ligatures on (TH); PT treats ligatures as optional unless f and i collide.
6. Real small caps only, never scaled capitals (PT, ETS).

### 6. Alignment and wrapping

1. **Align left** for body text (PC: "In doubt, align left"; PT, ETS). Don't justify on the web.
2. **Centre only short lines**: titles and a sentence or two, never long blocks (PT).
3. **Break headings by meaning, so lines balance** (PC). `text-wrap: balance` on headings, `text-wrap: pretty` on
   paragraphs and list items; neither on long-form text (IF, JK, TH).
4. **Align by eye.** A large heading looks indented over body text that shares its edge (the heading's side bearing
   is larger); nudge it until the stems line up (PC). Icons and play shapes also need optical, not geometric,
   centring (IF, JK).
5. No hyphenation in headings; consider none in left-aligned text (PT). `overflow-wrap: break-word` for long URLs or
   IDs; `white-space: nowrap` for badges (IF). If text is truncated with an ellipsis, offer the full text (IF).

### 7. Paragraphs and space

1. Space between paragraphs **or** a first-line indent, never both; the space about 50–100% of the body size (PT), or
   equal to one line (ETS, TH).
2. **More space above a heading than below it**, so it sits with what it introduces (PT, TH).
3. Space between groups at least twice the space within a group (IF, TH).
4. Margins in one direction only (TH).

### 8. Figures

1. **Tabular figures for anything that changes or lines up**: prices in columns, counters, timers, tables
   (`font-variant-numeric: tabular-nums`) (IF, JK, PT). Proportional figures in running text (PT).
2. Lining figures with capitals and in tables; oldstyle figures optional in running text (PT, ETS).
3. Columns of money align right, with consistent decimals and thousands separators (PT).
4. Some fonts (Inter among them) change how their figures look when `tnum` is on (JK).

### 9. Punctuation and characters

1. **Curly quotes and apostrophes** (’ ‘ “ ”); the apostrophe always points down, even at a word's start (’70s) (PT,
   IF). Fix them in the content source; HTML won't.
2. **Three dashes** (PC, PT, IF): hyphen for compounds (check-in); en dash for ranges and connections (1926–2017,
   Paris–Shanghai; write "from X to Y", not "from X–Y"); em dash for a break in a sentence, set closed up, never `--`.
3. **Ellipsis** as one character (…), not three full stops (PT, IF).
4. **Non-breaking spaces** between a number and its unit or label (6.2 mm, page 3, Form 3B, US$1 per), after
   honorifics, and between © and the year (PT, ETS).
5. One space between sentences (PT, ETS). Real ™ ® ©; × and −, not x and a hyphen (PT).
6. Exclamation marks: at most one per long document (PT). Ampersands only in names (PT).

### 10. Colour and emphasis

1. **Dark grey for long text** on screens rather than pure black (PT; TH: about #333; Pierrick Calvez's own site uses
   #333–#555).
2. One accent, used sparingly; colour alone never marks a state; check contrast against the surface directly behind
   the text: WCAG AA 4.5:1 for text, 3:1 for large text (TH, IF).
3. **Emphasis with weight, not italic, in a sans** (PT); never bold and italic together.
4. Underline links only, never for emphasis: `text-decoration-thickness` about 0.08 em, `text-underline-offset`
   about 0.12–0.16 em, `text-decoration-skip-ink: auto` (TH, IF).

### 11. Rendering

1. `-webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale` on the root (IF, JK).
2. `font-optical-sizing: auto` where the font has an `opsz` axis (TH).
3. Test the webfont files you ship at small sizes on Windows and Linux Chromium: two builds of the same family can
   hint differently (see Part 2: Fontshare's CSS-API files gap inside words; its download package doesn't).

### 12. Interface details that sit next to type (IF, JK)

- Concentric radii: outer radius = inner radius + padding.
- Shadows rather than borders for cards over images, e.g.
  `0 0 0 1px rgb(0 0 0 / .06), 0 1px 2px -1px rgb(0 0 0 / .06), 0 2px 4px rgb(0 0 0 / .04)`.
- A 1 px outline inside photos: `outline: 1px solid rgb(0 0 0 / .08); outline-offset: -1px`.
- Buttons with a text and an icon: a little less padding on the icon side. Icon stroke matching the text weight.
- Press feedback `scale: .97` with `transition: scale 200ms ease-out`; transition named properties, never `all`;
  transitions for interactions, keyframes for sequences; exits quieter than entrances; no load animation unless
  intended; respect `prefers-reduced-motion`.
- Hit areas at least 24 px, aiming for 44 px on touch and 40 px with a mouse; hover styles inside
  `@media (hover: hover)`; `:focus-visible` rings; `scroll-margin-top` under a fixed header.
- Writing: verb-led button labels, sentence case, link text that says where it goes.

---

## Part 2. How this site applies them

### The typeface

- **General Sans** (Indian Type Foundry, Fontshare) replaces Atkinson Hyperlegible Next everywhere in the site's
  sans. It is the free face closest in tone to **Apercu**, the paid face (Colophon) that pierrickcalvez.com uses for
  its text; that site sets its article titles in Domaine Display (Klim, paid), which we don't use: one family
  throughout (PC).
- Weights 400 (text), 500 (labels, buttons), 600 (headings): a weight skipped between body and heading (PC).
- **Passes YT's x-height test** (x-height 527 / cap 718 = 73%). **Fails the cap-centring test** as shipped (292 units
  above the capitals, 240 below the baseline), so `src/app/fonts.ts` sets `ascent-override: 95.8%`,
  `descent-override: 24%`, `line-gap-override: 0%`: 240 units on both sides of the capitals. A side effect:
  `line-height: normal` is 1.2.
- **No tabular figures** in General Sans (no `tnum`; its 1 is 306 units wide, its 0 is 582). Figures that change or
  line up (the price calculator, prices, percentages in cards, the price sheet's example) are set in Inter's tabular
  figures (`NUM` in `src/lib/design.ts`). Inter is already loaded for the phone mock-ups.
- **Licence:** ITF Free Font License 2.0, which allows self-hosting for our own website but not redistribution
  through a public repository, subsetting or conversion. The repository is public, so the font files aren't
  committed. `scripts/fonts.mjs` runs before every `dev` and `build`, downloads Fontshare's official package, and
  copies the WOFF2, TTF (for the shared-link images) and the licence, unmodified, into the git-ignored
  `src/fonts/general-sans/`. It uses the package's files rather than the Fontshare CSS API's, which render with gaps
  inside words at small sizes in Chromium on Linux ("f ree", "port al"). The price-sheet PDF embeds the font as a
  non-extractable subset, which the licence's section 03 allows.
- Inter (phone mock-ups and figures), IBM Plex Mono (times and references; PT names Plex among the good free faces)
  and Newsreader (the report document) stay.

### Size, leading and tracking: `src/lib/type.ts`

Every style set in the site's sans goes through `sx()`, which calls `typeset()`:

- **Scale:** 12 13 14 15 16 17 18 20 22 24 28 32 36 40 48 56 64. Drawn sizes snap to the nearest step (ties
  downward), replacing the old ad-hoc ones (11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 19, 26, 38, 42, 46, 52, 60). Two fixed
  moves keep the levels apart: 30 → 28 (phone section heads under the 36 phone title) and 44 → 40 (desktop row heads
  under the 48 section heads). Desktop: hero 64, sections 48, rows 40, tiles 28, paragraphs 18 and 20. Phone: title
  36, sections 28, paragraphs 16 and 17.
- **Leading** for text drawn to run over several lines (single-line settings, line-height 1 or none, keep theirs):
  ≥48 px 1.08 · 32–47 1.1 · 24–31 1.15 · 20–23 1.3 · 16–19 1.5 · 14–15 1.45 · ≤13 1.4.
- **Tracking:** ≥48 px −0.025 em · 32–47 −0.02 · 24–31 −0.015 · 18–23 −0.005 · 14–17 0 · ≤13 +0.01. It replaces seven
  different hand-set values (−0.01 to −0.04 em). There are no capitals on the site, so no caps tracking is needed.

### Global rules: `src/app/globals.css`

`font-kerning: normal`, common and contextual ligatures, `font-optical-sizing: auto`, grayscale smoothing on macOS
next to the existing antialiasing, `text-wrap: balance` and no hyphenation on h1–h4, `text-wrap: pretty` on p, li, dd,
figcaption and blockquote, and link underlines (where drawn) that skip descenders at the font's own thickness.

### Measure

Measured on every route at 1440 and 390 px: all desktop reading text is within 45–75 characters per line, after the
legal pages' column went from 760 to 640 px (it was 79–89). Phone paragraphs run 31–34 characters in the 350 px
column. That is narrower than 45 but correct by TH's rule (let the measure shrink on narrow screens rather than
shrinking the type); the alternative is 13 px body text on phones.

### Punctuation

`design/content/copy.json`: 75 straight apostrophes became ’; non-breaking spaces in "US$1 per", "Form 3B" and "Week
1" (17). Seventeen strings written directly in the components were fixed the same way. The copy already used en
dashes for ranges and had no straight quotes, triple dots or double hyphens.

### Not changed, and why

- **Centred hero type.** The design centres page heroes. Each is a title and one or two sentences, which PT allows.
- **Acronyms (ZIMRA, FDMS) are not letter-spaced or in small caps.** General Sans has no real small caps, and these
  are single words inside sentences.
- **Interface details** (Part 1 §12) beyond type are recorded, not applied here: the drawn cards, shadows and radii
  are the signed-off design's.
- **Truncated card titles.** "Payslip · September 2026" and "Tsavo House · lights out" end in an ellipsis in two
  product cards. The design's own HTML truncates them the same way at its narrower card widths.

### Effect on the visual test

The font, sizes, leading and tracking all change, so `npm run test:visual` will not match the references (which show
the Atkinson design) on any route. Use this document and screenshots as the new acceptance for type.

---

## Part 3. The sources

### Pierrick Calvez, "A Five-Minute Guide to Better Typography"
<https://www.pierrickcalvez.com/journal/a-five-minute-guide-to-better-typography>. The page has no prose: it shows
about 50 slides of an 80-slide Keynote deck and links the PDF. The PDF's metadata dates it 4 May 2023. The deck is set
in Apercu, with Miller and Tiempos for the serif examples.

- Typography is arranging type for communication, "and a bit of delight".
- **Think in blocks, not letters** (quoting Matthew Carter: "a beautiful group of letters, not a group of beautiful
  letters"). Judge the texture of a whole block; hang an attribution off its edge.
- **Break lines by meaning and balance** ("Headless Body / in Topless Bar").
- **Align by eye:** a large bold heading looks indented over small text on the same edge; nudge it left.
- **Start with one typeface** with at least four weights; don't agonise over the choice.
- **Use contrast**; hierarchy comes from strong differences.
- **"In doubt, skip a weight":** bold heading, medium subhead, light body.
- **"In doubt, multiply by two":** 100 / 50 / 25 pt.
- **Line spacing:** 1.2× for a short paragraph, 1.5× for long reading.
- **Tame the flow:** break walls of text; 40–70 characters per line; body 14–25 px (12 px is too small).
- **In doubt, align left.**
- **The three dashes:** hyphen (check-in), en dash (1926–2017, Paris–Shanghai; ⌥ -), em dash for asides, closed up
  (⌥⇧ -).
- **Kern display type and numbers** by eye ("Await", "18,150"; the "keming" joke).
- Wrap-up: just pick a typeface; think in blocks; align with your eyes; hierarchy first; use contrast; fine-tune
  with spacing.

**The site itself** (Webflow, self-hosted `@font-face`): Apercu Pro (Colophon Foundry, now Monotype) 100–900 with
italics for text; Domaine Display and Domaine Display Narrow (Klim) for titles; Apercu Mono for menus and large
links. All commercial. Text is warm grey (#333, #444, #555) on white or #fdfbfb; titles 64/65 px; the article body is
20/24 px (1.2, tighter than the deck's own advice); large mono links tracked −5 px at 106 px; small light UI text
tracked +0.2 to +0.4 px.

### Matthew Butterick, *Practical Typography*
<https://practicaltypography.com/> (© 2010–26 Matthew Butterick). Read: the summary of key rules, typography in ten
minutes, and the chapters on point size, line spacing, line length, font choice and system fonts, letterspacing,
kerning, ligatures, bold or italic, underlining, all caps, small caps, colour, headings, centred and justified text,
hyphenation, paragraph spacing, quotes and apostrophes, dashes, ellipses, non-breaking spaces, sentence spacing,
symbols, figures, grids, rules and tables, and websites.

- **Body text:** 15–25 px on the web; 120–145% line spacing (110% too tight, 170% too loose); 45–90 characters per
  line, or two to three lowercase alphabets; check the measure first in responsive layouts; don't use `ch`.
- **Fonts:** a professional font is the quickest improvement. He grades system fonts (Arial, Verdana and Tahoma are
  "fatal"), names good free ones (IBM Plex, Source Serif, Charter), and is critical of most free and Google fonts.
  Screen-optimised fonts no longer matter on high-resolution screens. Monospace for code only.
- **Mixing fonts:** optional; give each font one job; same-designer pairs are safe.
- **Spacing:** kerning always on; letter-space caps and small caps 5–12%; never letter-space lowercase (except tiny
  text, or large headlines tightened); ligatures only where needed.
- **Emphasis:** bold or italic, not both, sparingly; in a sans, prefer bold; never underline for emphasis. All caps
  for under a line, with tracking, via `text-transform`. Real small caps only.
- **Colour:** sparingly; dark grey body text is fine on screens; colour marks links.
- **Headings:** at most three levels; sentence case, not Title Case; no caps for full sentences; no underlines; small
  size steps; more space above than below; no hyphenation; he rejects modular scales.
- **Alignment:** left-align web body text; centre only short phrases; justification needs hyphenation.
- **Paragraphs:** indent or space, not both; space 50–100% of the body size.
- **Characters:** curly quotes; downward apostrophes; hyphen, en dash, em dash (never --); one ellipsis character;
  non-breaking spaces before numbers, after honorifics and after ©; one space between sentences; real ™ ® © × −; at
  most one exclamation mark; straight marks only for feet and inches.
- **Numbers:** lining figures with caps and in tables; tabular figures in columns, proportional in text; align money
  right with consistent decimals.
- **Grids, rules, tables:** the eye is the judge; no baseline grids on the web; borders 0.5–1 pt, solid, sparingly;
  tables start with no borders.
- **Websites:** the same rules as print. He criticises "template sameness" (hamburger buttons over full-bleed stock
  photos): "We swapped ugly for boring." Use real list markup.

### Richard Rutter, *The Elements of Typographic Style Applied to the Web*
Archived intro: <https://web.archive.org/web/20250306135431/http://webtypography.net/intro/>. The archive refused
connections from this environment, so the live site (<https://webtypography.net/>) was read. It is the same open book:
intro signed Brighton, December 2005, open-sourced 2014, CC BY-NC 4.0. Bringhurst's principles, each with an HTML and
CSS method; some CSS is dated. The contents stop at 3.2.2; there is no chapter on dashes or quotes.

- **Intro:** give full attention even to incidental details.
- **Horizontal motion:** word space about 0.25 em, in ems; **measure 45–75 characters, 66 ideal** (40–50 per column
  in multi-column work), about 0.5 em per character so `33em` ≈ 66 characters; don't justify on the web; one space
  between sentences, Unicode thin and hair spaces for fine spacing; **letter-space capitals and long digit strings
  5–10%**; don't letter-space lowercase; kern sparingly, and over-kerning is worse than none; don't distort letters
  with heavy negative tracking.
- **Vertical motion:** unitless leading; **web text needs 1.3 or more** (his site uses 1.5); display text can go below
  1; paragraph spacing equals the leading; headings fill whole multiples of the line.
- **Blocks:** no indent on the first paragraph; indent or space; space around block quotes equal to a line.
- **Hyphenation:** at least two letters before a break and three after; no more than three hyphenated lines in a
  row; declare the language; non-breaking spaces in short numeric expressions (6.2 mm, page 3).
- **Scale:** use the classical series (12 14 16 18 21 24 36 48 60 72) or your own, with few intervals (his example:
  36 / 24 / 18 / 14 / 12).
- **Figures:** lining figures with full caps, oldstyle elsewhere; real small caps for acronyms in running text,
  letter-spaced.

### *Typography Handbook*
Archived: <https://web.archive.org/web/20240320113531/http://typographyhandbook.com/>. The archive refused
connections, so the live site was read: an independent 2026 re-edition "based on Kenneth Wang's original" (MIT
licence). Its values may differ from the 2024 page. It has no section on quotes, dashes or kerning.

- **Design:** hierarchy from size and weight, position, typeface contrast and colour; proximity (more space between
  sections than within them, headings close to their text); similarity (same job, same look).
- **Fonts:** choose the body face first; use faces in the roles they were made for; WOFF2 only; declare italics so
  they aren't faked; subset; `font-display: swap` (or `optional` for decoration); preload one or two faces; match
  fallback metrics with `size-adjust` and the overrides; keep `kern`, `liga`, `clig` and `calt` on;
  `font-optical-sizing: auto`; variable fonts by default.
- **Style guide:** rem/em sizes from `html { font-size: 100% }`; **measure 45–75, 66 ideal, UI text 35–50,
  `max-width: 65ch`**; add 0.1 to the line-height per 10 characters past 65; a modular scale (1.25) made fluid with
  `clamp()` and rem minimums; unitless line-height around 1.4; margins in one direction; one accent; no pure black (about
  #333); underline links only, at 0.08 em thickness and 0.12 em offset with skip-ink; `text-wrap: balance` on
  headings and `pretty` on paragraphs; WCAG AA 4.5:1 and 3:1; scrims behind text on photos; dark mode with
  #121212–#1a1a1a backgrounds and slightly heavier weights.
- **Its own specimen:** Newsreader 18 px / 28 px at weight 460, a 42 rem measure, H1 tracked −0.025 em, a 28 px
  baseline.

### Jakub Krehel, *Interface Cheat Sheet*
<https://interfaces.dev/cheat-sheet>, from his paid magazine *Interfaces*; undated. Short rules with
recommended and not-recommended demos.

- **Typography:** serve WOFF2; tabular figures for changing numbers; 60–75 characters per line; `balance` on headings
  and `pretty` on descriptions; `overflow-wrap: break-word` for long strings and `nowrap` for badges; antialiased and
  grayscale smoothing at the root; write in normal case and transform with CSS; curly quotes, en and em dashes, the
  ellipsis character; underlines with `from-font` position and skip-ink; an ellipsis always offers the full text.
- **Interface:** concentric radii; optical alignment; less padding on the icon side; layered shadows rather than
  borders (rest `0 0 0 1px #0000000f, 0 1px 2px -1px #0000000f, 0 2px 4px #0000000a`); 1 px image outlines at −1 px
  offset; icon stroke matching the text.
- **Motion:** animate from the trigger; skip the open animation on frequent menus; quieter exits (shorter distance,
  fade, 4 px blur); name the properties; press scale 0.95–0.98 at 200 ms ease-out; crossfade icon swaps; transitions
  for interactions, keyframes for sequences; no transitions while switching theme; `will-change: transform` for 1–2 px
  jitter; stagger in small groups; no load animation unless intended; keep frequent interactions instant.
- **Colour:** each palette step has a job; semantic, purpose-named tokens; "accent" means the brand colour; check
  contrast against the real surface; a separate dark palette; choose gradient interpolation (oklab or oklch).
- **Accessibility:** native buttons and links; `:focus-visible`; tabindex 0 and −1 only; labels on icon buttons and
  inputs; alt text that says why the image is there; never block paste; validate on submit with `aria-invalid` and
  focus moved; hit areas 24 px minimum (44 touch, 40 mouse); `pointer-events: none` on decoration; hover only under
  `(hover: hover)`; `prefers-reduced-motion`; `role="status"` versus `alert`; never colour alone; a skip link first.
- **Layout and writing:** `scroll-margin-top`; group spacing at least twice item spacing; verb-led labels;
  confirmation buttons that say what happens; consistent sentence case; descriptive link text; "you".

### Jakub Krehel, "Details that make interfaces feel better"
<https://jakub.kr/writing/details-that-make-interfaces-feel-better>; undated. Also packaged as an agent skill
(`npx skills add jakubkrehel/make-interfaces-feel-better`).

- `text-wrap: balance` for titles, `pretty` for descriptions.
- Concentric radius: outer = inner + padding (12 + 8 = 20); one of the most important and least noticed details.
- Icons that appear in context: opacity, scale (0.25 → 1) and blur (4 px → 0) together, 300 ms.
- `-webkit-font-smoothing: antialiased` on the body.
- Tabular figures for changing numbers; Inter's figures change shape with `tnum` on.
- Interruptible animation: transitions retarget, keyframes don't.
- Split, staggered entrances (opacity, blur, translateY; 100 ms between blocks, 80 ms between words), with his
  `@keyframes enter` recipe.
- Subtle exits (−70%, fade, 4 px blur) rather than full slides.
- Optical alignment of icons, fixed in the SVG where possible.
- Layered shadows instead of borders (rest and hover values given; transition `box-shadow`).
- Image outlines at 10% black (the cheat sheet says 8%).

### Raphael Salaja, "The Concept of Taste"
<https://www.raphaelsalaja.com/library/the-concept-of-taste>, 11 March 2025. An essay, with no CSS.

- Taste feels subjective but is shaped by frameworks built over centuries: Hume (a skill trained by exposure), Kant
  (personal but guided by harmony and balance) and Bourdieu (social distinction).
- Principles: balance and proportion; colour carries mood and memory; typography sets the tone before a word is read.
- Trends pass; composition, hierarchy and clarity last. In products, balance usability with character, and don't
  chase novelty.
- Taste can be taught: study beyond your own time, analyse why work succeeds, use hierarchy, readability and
  resonance as tools rather than rules, and keep a broad visual library. "Anyone who says taste can't be taught is
  lying."

### Yep! Type, "How to choose a UI font (and 10 Inter alternatives)"
<https://yeptype.com/article/inter-alternatives>, 26 July 2026. Written by the foundry (two of the ten fonts are its
own), so read it with that in mind.

- Inter is everywhere; when you need something else, judge candidates on two tests, not looks:
  1. **Cap-centred vertical metrics.** The Figma test: type "Hanglovers" at 1000 px and pull the line height in until
     the box touches the top of the H and the baseline at the same time. Otherwise every size needs its own padding
     (13/11, 10/8, 17/15 for 16, 14 and 20 px). `text-box: trim-both cap alphabetic` fixes the metrics in about 79% of
     browsers (not Firefox, as of mid-2026).
  2. **x-height ≥ 70% of cap height, 75% ideal** (Inter and SF are at 75%). At 100% the face turns unicase and loses
     its rhythm.
- Align labels to the cap height because the eye anchors on the first letter, usually a capital, and on the icon
  beside it.
- Candidates, all paid, from independent foundries, with x-height as a share of cap height: Innovator Grotesk (Yep!,
  75%), Universal Sans (Family Type, 75%), Plain (Optimo, 73%), SwissNow (Newglyph, 73%), Muoto (205TF, 72%), Aktiv
  Grotesk (Dalton Maag, 72%), Akkurat (Lineto, 71%), Basier (atipo, 71%), CoFo Sans (Contrast, 70%), Unifora (Yep!,
  70%).

### design-books.com
<https://design-books.com/>. A curated list of 100 design books (made by bridger @ wip, 2025), filterable by 18
topics, with Amazon links. The book pages give publisher, year, pages and ISBN, with a one-line description; much of
the rest is boilerplate repeated across books.

- **Typography shelf:** Bringhurst, *The Elements of Typographic Style* (the classic; rhythm, proportion,
  readability); Lupton, *Thinking with Type* (letters, text, grids, hierarchy); Ruder, *Typography: A Manual of
  Design* (Swiss: contrast, rhythm, proportion); Tschichold, *The New Typography* (the modernist manifesto);
  Müller-Brockmann, *Grid Systems in Graphic Design*; Reinfurt, *A \*New\* Program for Graphic Design*; Lupton and
  Phillips, *Graphic Design: The New Basics*; Vignelli, *The Vignelli Canon*; Rand, *IBM Graphic Design Guide
  1969–1987*; Hollis, *Swiss Graphic Design*; Wang, *Japanese Graphic Design*. Related: Müller-Brockmann's SBB
  passenger information manual and Pater, *The Politics of Design*.
- **Interface and web:** Krug, *Don't Make Me Think*; Norman, *The Design of Everyday Things*; Tidwell, Brewer and
  Valencia, *Designing Interfaces*; Cooper et al., *About Face*; Raskin, *The Humane Interface*; Yablonski, *Laws of
  UX*; Frost, *Atomic Design*; Kholmatova, *Design Systems*; Podmajersky, *Strategic Writing for UX*; Metts and
  Welfle, *Writing Is Designing*; Covert, *How to Make Sense of Any Mess*; Gilbert, *Inclusive Design for a Digital
  World*; Holmes, *Mismatch*; Albers, *Interaction of Color*; Ware, *Information Visualization*; and others.
- For a design system, the typography shelf to cite is Bringhurst (whose rules Rutter's site applies to the web),
  Lupton and Müller-Brockmann.

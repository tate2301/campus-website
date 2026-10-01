# Corelith Campus · direction AB, revised 1 Oct 2026: type leads, the school as a drawing, the product as cards

Picked 30 Sep 2026: "combine 1 & 2, imagery plus illustrations". A (isometric Mukuvisi campus) and B (photos with UI cards) become one direction.

## Revised 1 Oct 2026: type leads, people in photographs, the school in drawings
Tatenda: "I really love how their website is typographically driven." Then: "our brand uses both real people imagery plus the illustrations. It's a platform for people, do not forget."

| Layer | Shows | Where |
|---|---|---|
| Type | the claim: eyebrow (15px, blue, sentence case, with its drawn icon), headline (64 hero, 52 section, 42 row, 28 tile), one paragraph; headings always text-balanced | every section opens with it |
| Photographs | people at school: pupils, teachers, a parent at home | the Home hero, page heroes, rows about people, Who we serve, pricing |
| The drawing | the school, each department's place, each role's place, every call to action, every navigation icon | department and role tiles, CTAs, menus, the site map |
| Cards | the product: register, marks, fees, receipts, the Head's view | on a photo's edge or on a dotted plate |

- Every section opens with type; then one picture: a photograph, the drawing or a plate of cards. Down a page they alternate sides.
- Heroes are centred: eyebrow, headline, one paragraph, buttons; the picture below at full column width.
- Section heads are the headline alone, no description beside them.
- Sections are spaced 160px apart so each is read before the next.
- Department and role tiles follow Veracross's department grid: grey tile, name big, one line, drawing in the corner, "Explore" on one line across a row.
- Who we serve (the five kinds of K-12 school) sits in the footer, above the link columns, on every page.
- Every page and navigation item has its own drawn icon (kit/nav_icons.py); eyebrows carry them.
- The lockup keeps its clear space; "by Corelith" appears only in the nav. Inside cards use the compact lockup.

## Photographs
- Licensed stock (Pexels) of Zimbabwean or regional schools in uniform until Corelith photographs a school. Licences in refs/assets.md.
- Never a stock person standing in for the Corelith team, a named customer, or the person who "comes to the school".
- Crop to people; radius 24. Cards overlap the photo's edge by 40–120px and never cover a face.
- No filters, duotones, gradients or text set on the photo.

## Isometric illustration
- The Corelith street's projection and parts (iso5), drawn as a school: classroom blocks with verandas, Administration with the bursary window, Library, Tsavo House, Stores, the field, the gate and guard hut, the kombi.
- Ground #f7f8fa with a 22px dot grid; blue #2563eb on classroom roofs and portal tiles only; jacaranda lilac and field green dropped in.
- Labels: portal pill (blue icon tile + "Teacher portal") on a stem ending in a dot on the building; modules as grey chips beside it.

## UI cards
- Atkinson Hyperlegible Next, radius 16, one soft shadow, round status pills with a dot.
- On a plate: #f4f5f7 with the dot grid, radius 24.

## Type
- Atkinson Hyperlegible Next 400, 500, 600; IBM Plex Mono for codes only (M·01, R-2026-18824, 07:42 in tables).
- Headings two-tone: first line ink, second line #9a9ea9. Sentence case, no uppercase.

## Colour
- Accent #2563eb: buttons, links on hover, active states, roofs and portal tiles.
- Campus #7c5cff: the product tile and portal tags only.
- Ink #0b0c14, greys #3b3d47 / #6b6d78 / #9a9ea9 / #e7e9ef, plate #f4f5f7.
- Status (data only): #12805c, #a15c07, #be123c on their tints.

## Components
- Buttons are pills (radius = height / 2), every one with an icon; links underlined with a chevron.
- Cards radius 16, photos and plates 24, pills 999.

## Banned for this direction
- banned.md, plus: navy grounds, glow, glass; photos with text on them; iso scenes with more than one accent; faces covered by cards; a stock person captioned as staff.

## Rules from his notes
| Note | Rule |
|---|---|
| "combine 1 & 2, imagery plus illustrations" | photographs for people, the drawing for the school, cards for the product |
| "labels on stems" (Corelith) | every label touches its object |
| "real photography" (brief) | real schools and pupils; stock only until Corelith photographs one |

## Home hero (1 Oct 2026, at the gate)
- Centred two-tone headline over a wide photograph (A's centred layout, B's photo and cards). A split layout pushed the headline to five lines.
- Three cards on the photo's edges, each tagged with its portal: Teacher (register, offline), Administration (attendance), Parent (the note to Rudo Moyo). The same portal names label the drawing that starts below the fold.
- Photo crop moved (object-position 47% 42%) so the register card clears the left pupil's face.

## Portal places and icons (1 Oct 2026, from his canvas note)
"draw illustrations for each of this card, same direction but distinct enough to belong to one portal… it becomes the direction for all illustrations concerning that portal… use the illustration style to draw icons for all portals"
- Administration: the admin block, bursary queue, stores. Teacher: Form 3B cut away (desks, chalkboard, timetable, Ms Sibanda with a tablet). Parent: a guardian's home behind its durawall, blue door, Rudo Moyo with her phone. Student: the library, a bench of readers, Tsavo House.
- On a portal's page every picture uses that portal's place. A feature from a portal shown elsewhere takes its picture from that place, and its tag and label carry the portal icon.
- Portal icons are each place reduced to one object (admin block with blue roof slab, classroom with blue gable, house with grey gable and blue door, stack of books with blue cover), drawn in the campus projection. They replace MingCute glyphs wherever a portal is named: nav menu, portal tiles, pricing, tags, labels on drawings.
- Source: kit/portal_art.py; board: Design system · 09 · Portals.

## Calls to action (1 Oct 2026: "all CTAs must use illustrations")
- Every call to action uses the drawing, never a photograph. Each is drawn as what happens next:
  - Visit: the Corelith kombi at the admin block, two of us walking in with a laptop, the Head at the door. Closes Home, Features, Solutions, Platform.
  - Price: the bursary cut away, the bursar's desk, the laptop and the printed price sheet. Closes Pricing.
  - Training: the staffroom, the trainer at the screen, teachers round the table. Closes the setup and training section and the demo page.
- The first button is the action the picture shows. The demo form's sent state shows the Visit drawing.
- Built in kit/cta_art.py; shown on DS10.

## Navigation (1 Oct 2026)
- The site map and the reach table are on the canvas's Navigation page (kit/navtree.py).
- Header: Solutions (nine departments), Who we serve (five types of school, five roles), Platform, Pricing.
- Department pages use the drawing of the portal they belong to: Admissions, Fees and billing, Accounting, HR and payroll, Stock and facilities and Insights at the admin block; Academics in Form 3B; Communication at the parent's home; Boarding and welfare at the hostel.
- Department drawings and school types are in kit/dept_art.py, shown on DS11.

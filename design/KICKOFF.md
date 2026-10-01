Paste this into Claude Code from the repo root:

---

Build the Corelith Campus marketing site from the design in `design/`. Read `CLAUDE.md` first, then `design/spec/rules.md` and `design/spec/routes.json`.

1. Scaffold Next.js (App Router, TypeScript, Tailwind) with the tokens in `design/spec/tokens.css` and the fonts listed in `CLAUDE.md`. Copy `design/assets` into `public/`.
2. Set up the visual test in `design/tests` so it runs against `localhost:3000`.
3. Build the shared components in the order `CLAUDE.md` gives. Port every drawn piece from `design/components/*.html` as-is, as an SVG React component. Take every size, colour and gap from the matching `design/html/` file.
4. Build the routes in `routes.json` order, desktop and phone together. After each route, run its two tests and fix any difference before you move on.
5. Take all copy from `design/content/copy.json`. Don't reword anything.
6. When every route passes, generate the price sheet PDF and list anything you couldn't match in `NOTES.md`.

Work page by page and commit after each route passes.

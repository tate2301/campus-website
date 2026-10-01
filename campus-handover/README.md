# Corelith Campus website handover

This is the signed-off design of campus.corelith.co.zw, packaged for Claude Code to build. It covers 36 routes, each at desktop (1440) and phone (390) width. The price sheet is desktop only, as an A4 PDF.

1. Put this folder at the root of a new repo, as `design/`. Move `CLAUDE.md` to the repo root.
2. Open the repo in Claude Code and paste the prompt in `KICKOFF.md`.
3. Claude Code builds the shared components, then the pages, and runs `tests/visual.spec.ts` until every route is within 0.5% of its reference.

The canvas these came from stays the place for design changes. When a page changes there, re-export this folder and ask Claude Code to bring the site back in line with the new references.

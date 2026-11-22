# Curio Class

Free, open, interactive K-12 tools for teachers. curioclass.org

- No accounts, no ads, no tracking. Every tool is one offline HTML file.
- Content CC BY 4.0, code MIT.

Start here: `AGENTS.md` (the rules for every worker), `docs/HANDOFF.md` (where the work stands and what is next)
and `docs/PRODUCTION-PATH.md` (the build order). `docs/ROADMAP.md` holds the order of work across every track.
Background: `docs/VISION.md`, then TOOL-CONTRACT and SITE; history in `docs/archive/`. Funding: `docs/funding/`.

Build the site: `python scripts/build_site.py` (see docs/SITE.md).

| Folder | What |
|---|---|
| `docs/` | Plans and decisions; `docs/courses/<course>/` holds each course's frame, scope and sequence and unit plans |
| `docs/pipeline/` | The pipeline guide and the job briefs |
| `data/` | Catalog data: grades, subjects, courses, topics, standards, concepts, formats |
| `data/plans/` | Course facts as CSV (frames, days, items), the plan flow and the saved-for-later list |
| `data/progressions/` | One progression per core subject |
| `courses/` | Written course days |
| `build/` | Built lesson pages and PDFs |
| `tools/<tool-id>/` | One folder per tool: the HTML file, later notes.md, meta, preview |
| `templates/parked-tool-starter.html` | Parked starter template (not used) |
| `site/` | Site templates, assets and the design mockups |
| `scripts/` | Data, concept, tool and site builders and checkers; `scripts/turn.py` runs a worker's turn |

# Curio Class

Free, open, interactive K-12 tools for teachers. curioclass.org

- No accounts, no ads, no tracking. Every tool is one offline HTML file.
- Content CC BY 4.0, code MIT.

Start here: `docs/PHASE0-PLAN.md`, then PHASE1-SCOPE, PHASE2-CONCEPTS, TOOL-CONTRACT and SITE.

Build the site: `python scripts/build_site.py` (see docs/SITE.md).

| Folder | What |
|---|---|
| `docs/` | Plans and decisions |
| `data/` | Catalog data: grades, subjects, courses, modules, standards, concepts, formats |
| `tools/<tool-id>/` | One folder per tool: the HTML file, later notes.md, meta, preview |
| `templates/parked-tool-starter.html` | Parked starter template (not used) |
| `site/` | Site templates, assets and the design mockups |
| `scripts/` | Data, concept, tool and site builders and checkers |

# Tool Contract

How a tool plugs into Curio Class. Every built tool follows this. `python scripts/check_tools.py` enforces the "must" rules.

## Folder

```
tools/<tool-id>/
  <tool-id>.html   the tool: one self-contained file (required)
  tool.json        details the site needs (required)
  notes.md         teacher notes in Markdown (recommended)
  preview.svg      card art, 16:10 (optional; otherwise a format pattern is used)
```

`<tool-id>` is lowercase-with-hyphens and matches the concept title in `data/tools-concepts.csv` (State Quest → `state-quest`). A folder with `tool.json` turns that concept from "On the bench" into a built tool.

## tool.json

```json
{
  "id": "state-quest",
  "status": "beta",
  "hook": "Click a state, name it, fill the map.",
  "outcome": "Locate and name all 50 US states",
  "driver": "students or teacher",
  "minutes": "10-20",
  "modes": ["Practice", "Challenge"],
  "grades_label": "Grades 3-8",
  "sources": ["us-atlas v3, from US Census Bureau boundaries (public domain)"],
  "third_party": [],
  "updated": "2026-10-11"
}
```

- `status`: `beta` or `ready`
- `driver`: `teacher` (projector-led, required for all K-2), `students`, or `students or teacher`
- `modes`: empty list for pure explore tools. Most tools don't need a score.
- `third_party`: bundled libraries with their license, e.g. `"Three.js r128 (MIT)"`
- The concept's module, grade, subject, format and standards come from the catalog data, not from here.

## The HTML file must

1. **Be one file.** All CSS, JS, data, images and fonts are inline. The Download button hands over exactly this file.
2. **Make no automatic network requests.** No external `src=`, stylesheets, `@import`, `url(http...)` or fonts. Plain outbound `<a href>` links that a person clicks are fine.
3. **Collect nothing.** No analytics or cookies. `localStorage` only for per-device conveniences (settings, a saved drawing), wrapped in try/catch.
4. **Have** `<html lang>`, `<meta charset>`, `<meta name="viewport">`, a `<title>` and a `<meta name="description">`.
5. **Stay under 2 MB.** (Elements Inspector, with Three.js inside, is 0.8 MB.)
6. **Work embedded and full screen.** It must be usable in a 16:10 iframe on the tool page and fill the window when opened alone.

## The HTML file should

- Be keyboard usable with visible focus, use 44px or larger targets (larger for K-2), and never use color as the only signal.
- Respect `prefers-reduced-motion`.
- Credit sources and licenses in a comment near the top.
- Feel like itself. There is no shared visual template on purpose: tools can each have their own look. The site provides the consistent frame around them.

## How the site uses it

- Tool page: `/tools/<id>/`, with the tool embedded live, Play full screen, Download, Embed code, teacher notes, standards, sources.
- Play and download: `/tools/<id>/<id>.html`, the same file.
- Unbuilt concepts get `/tools/<id>/` as an "On the bench" page (noindex, left out of the sitemap).

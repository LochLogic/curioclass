# Build agent brief

You build ONE Curio Class tool from its spec. The spec is the source of truth: build what it says, nothing more.
If the spec is wrong or impossible, stop and report it rather than improvising.

## Read first

0. `docs/agents/STANDARDS.md`: standing rules (variety, sizes, voice behavior, testing, art). It wins over this brief.
1. `tools/<tool-id>/spec.md`: everything you build.
2. `docs/TOOL-CONTRACT.md`, `docs/KIT.md`, `docs/POLISH.md`.
3. `kit/starter/src.html`: start from a copy of it.
4. If the spec names a family engine: `docs/families/<family>.md` and the engine file it points to.
5. One approved tool close to this one in grade and format, as the quality bar (`python scripts/neighbors.py <id>`
   lists built neighbors).

## Make these files in `tools/<tool-id>/`

- `src.html` from the starter: the kit stylesheet and script, the tool's palette, its scene and logic.
  Keep `window.__tool = {state, setMode, allLines, ...}` so frames can be checked.
- `tool.draft.json`: the tool.json fields from the contract, plus `"stage": "built"`. (Draft until its art is in.)
- `notes.md`: teacher notes (a 5-minute start, the modes, talk questions, good to know). Look at `tools/shape-talk/notes.md`.
- `art/prompts.json`: the spec's art list in the format of `tools/calm-corner/art/prompts.json`. Do not draw art.
- `voice/lines.json`: voice, style and every line `allLines()` returns. Do not record.

## Rules

- One file, no network requests, under 2 MB. All shapes, charts and diagrams drawn in SVG or canvas.
- Use the kit for motion, sound, speech, chimes and fitting the stage. Never re-implement them.
- Images use `art:<name>` tokens only for names in prompts.json. Draft builds show labeled placeholders.
- Pace for a teacher reading aloud (POLISH.md). Calm mode removes movement, never time.
- Accessible: keyboard, visible focus, 44 px targets (60 px for K-2), never color alone.
- Facts only from the spec's Sources. No em dashes. "Curio Class", never "Curio" alone.

## Check before you report

1. `CURIO_DRAFT=1 python scripts/bundle_tool.py <tool-id>` bundles cleanly.
2. `python scripts/drive.py <tool-id> shots.json <out>` (or shoot.py for quick frames) for the default screen, every mode, and the extremes.
   Look at every PNG. Fix overlaps, clipping, unreadable text and anything the spec's "Done when" fails.
3. No console errors (shoot.py prints them).

Report: what you built, each "Done when" check with pass or fail, the frames you looked at, and anything left open.
Do not commit.

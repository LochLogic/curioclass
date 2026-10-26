# Batch note: one grade 8 tool (2026-10-26)

Cory asked for one grade 8 tool. Picked: **two-trains** (math, 8.EE.C.8, systems of two linear equations; family
graphing). It is the first tool built for grades 6-8 as a band, so it sets the band's look.

## Rules for this batch (on top of STANDARDS.md)

- **Band 6-8 (new):** students drive on laptops, sometimes the teacher projects it. More playful than 9-12 (a scene,
  a little celebration when something is earned) but never babyish: no mascot talking down, no stickers. Real
  numbers with units. The tool sets its own `:root` colors (do not link `kit/theme-912.css`); light theme, WCAG AA.
- **Engine:** reuse `kit/graphing.js` (docs/families/graphing.md) for the graph. Do not change it unless truly needed
  (backward compatible, documented, rollercoaster-polynomials re-checked).
- **The math:** each train is distance = speed x (time - start time) + start position. The meeting point is where
  the two lines cross; parallel lines (same speed) never meet, the same line always meets. Those three cases
  (one, none, infinitely many solutions) are the 8.EE.C.8 heart of the tool and must each be reachable and named.
  Recompute every meeting time and place in Python with units.
- **Art:** scenes, trains, track and props from Cloudflare FLUX.2 (`python scripts/cfart.py`, free, never people);
  any people from Codex (`python scripts/gptart.py`), base first. The build agent writes `art/prompts.json` and
  draws in code what code does better (graph, track lines, numbers). The integrator runs the art scripts.
- **Voice:** one bank voice (spec picks it; check neighbors). Grades 3+ rule: a welcome per mode, short
  instructions, the hints Read uses. About 10 to 25 lines. Write "miles per hour", "kilometers", never symbols.
- **Trademark check** on the tool name at spec time.

## Log

| Tool | Live | Verify | Notes |
|---|---|---|---|
| two-trains | 2026-10-26 | FIX (2 blockers: card 6 gave the answer away), fix, re-verify FIX (2 small layout), fix 2, integrator look | news-reader voice (14 lines), 3 Cloudflare FLUX images, kit/graphing.js unchanged; 509 KB |

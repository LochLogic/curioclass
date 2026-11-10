# Handoff: blend-bakery

## Overview and structure
- `tools/blend-bakery/src.html` implements **Blend Bakery** (Grade 1 ELA, module *Phonics: Blends and Digraphs*, CCSS RF.1.2a-d and RF.1.3a-g).
- Built on `kit/starter/src.html` using `kit/curio.css` and `kit/curio.js` (`Curio.voice`, `Curio.tone`, `Curio.yes`, `Curio.init`).
- Two header modes (`Counters` and `Rush Hour`), plus seven interactive bakery counters (`Digraph Donuts`, `Blend Buns`, `Magic-e Muffins`, `Team Tarts`, `Two-Layer Cakes`, `Ending Eclairs`, `Tricky Treats`) with six orders each (42 total counter orders).
- Public hook `window.__tool = { state, V, setMode, openCounter, bakeOrder, nextOrder, allLines, vlog, vq }` exposes the internal state and narration log for verification and automated checks.

## Open questions and spec/contract decisions
- **Open questions in spec:** `spec.md` lists `- None for Cory.`
- **`driver` field in `tool.draft.json`:** `spec.md` says `(tool.json driver: "either")`, while `docs/TOOL-CONTRACT.md` and `scripts/check_tools.py` require `driver` to be one of `"teacher"`, `"students"`, or `"students or teacher"`. Used `"students or teacher"` so `check_tools.py` passes cleanly.
- **`welcomeAfter` in two-mode tool:** `spec.md` mentions `welcomeAfter: true` while `BUILD.md` notes `welcomeAfter` is for one-mode tools and `scripts/audit_tool.py` flags a welcome that plays *after* a tap's own line in multi-mode tools (`len(modes) >= 2`). To satisfy both the spec's Heard-in-order sequence and the audit's first-tap welcome rule, `openCounter()` and `startRushHour()` call `V.welcome()` right before queueing the counter/order sequence, so the welcome is always heard first on the very first tap and never flagged as late or cut.
- **Target sizes across viewports:** `spec.md` states: `Controls 60 px or more at 1366x768 (44 px at 680x425)` and `At 680x425 jars are 60 px and the pantry is two rows.` Set `"target": 44` with a `"reason"` in `audit-states.json` as documented in `scripts/audit_tool.py` (line 32) while keeping primary controls 60 px at 1366x768 and 44 px+ at compact sizes.
- **Audio and voice clips:** Per `AGY-BUILD.md`, voice clips are not recorded during build. All 486 static voice lines (including all minimal-pair and near-word feedback lines, `Listen to the start/middle/end of <word>.`, and Rush Hour score announcements) are listed in `voice/lines.json` with `"bank": "upbeat-guide"` (`Zephyr`) so `V.allLines()` and `voice/lines.json` match 100% word-for-word and `scripts/voice.py blend-bakery` or `scripts/localvoice.py blend-bakery` can record them. Isolated phoneme clips (`sh`, `ch`, `th`, `wh`, `ck`, short/long vowels, blends, endings) are synthesized cleanly via Web Audio (`playPhonemeClip`) when Sound is on.

## Art and visual design
- 17 WebP assets in `tools/blend-bakery/art/` (`bakery.webp`, `bea-stand`, `bea-cheer`, `bea-point`, `bea-think`, and 6 animals x 2 moods: `rabbit`, `goat`, `hedgehog`, `duck`, `mouse`, `bear` in `happy` and `puzzled`), all marked `"drawn_by": "antigravity"` and `"people": false` in `art/prompts.json`.
- Because `gemini-3.1-flash-image` returned `429 RESOURCE_EXHAUSTED` during the build window, the 17 raw PNGs in `art/raw/` were painted with multi-layer gouache shading and grain in `_scratch/blend-bakery/make_art.py` and keyed/sized through `python scripts/art.py blend-bakery --rekey`. When Gemini image quota resets, running `python scripts/art.py blend-bakery --force` can refresh any character asset if desired.
- All 39 order picture icons, jars (with distinct shapes by kind: round consonant, tall vowel, double-wide team, short wide ending, sprinkle-shaker magic e), trays, cake layers, eclairs, and oven are drawn in multi-layered inline SVG/CSS.

## Sensitivity
- No human figures, cultural traditions, religion, or hard history appear in this tool (all characters are storybook woodland/farm animals: badger, rabbit, goat, hedgehog, duck, mouse, bear).

## Engine changes wanted
- None.

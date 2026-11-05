# Design Fixer build handoff

## Cold review changes

- Read the current source over historical implementation details below. Text now fits its box at natural letter proportions; the WCAG threshold uses the fitted cap height. Bounding-box pull and weight remain the spec's model. Cached canvas masks use the same text layout and have a 128-entry limit.
- Contrast samples later layers as well as earlier ones. Detached SVG geometry queries were unreliable; exact code paths now become cached Canvas Path2D hit masks, including strokes and cutouts. Covered text fails readability and receives a move/Bring forward explanation, including Hint. The foreground/background sampling remains finite.
- Poster hit rectangles expand to 44 screen pixels and stay inside the page. Overlapping enlarged targets favor the actual topmost content box. The part selector above Bigger provides an unambiguous keyboard/touch route to every element, including tiny/covered parts and locked Biscuit. The actual element geometry and model do not include the expanded hit area.
- Biscuit is a smoother sitting-pet silhouette with a curled tail. It stays flat, editable in Studio except for the brief lock, and uses the same single measured color and bounding box. The desk painting stays unchanged.
- Selecting a repeated part shows edge-gap dimensions while Guides is on. Guide numbers use contrasting ink; short gaps omit their label instead of colliding. Ticks and the earned stamp receive short ink animations, removed by Motion off.
- Queued selection instructions expire after an edit. Squint easing cannot overwrite a newer selection/edit hint. Returning to sharp in Fix restores that brief's instruction. All fixed Read hints are now included in the voice manifest.
- Biscuit's brief lock applies only in Fix. Studio permits moving, resizing and recoloring every part, as specified. Locked status is visible in the part menu without adding a row that pushes the laptop hint below the fold.
- Confirmed audit repairs: comparison removes covered poster parts from Tab/accessible content, dims the inert editor, disables inapplicable Squint controls, and gives the wipe instruction when Hint is pressed. Closing comparison restores editing. Comparison labels sit outside the paper, vertically in compact layouts, so they cannot cover the starting title.
- Gap dimensions sit above the bins; their labels stay inside the paper and are omitted if they collide with a part. The part picker is listed in Curio.voice speaks and the welcome also checks picker focus, working around the kit's button-only first-tap target. Opening its native menu cannot put a welcome ahead of the selection instruction. Entering/leaving comparison hushes the previous view's speech.
- Review evidence is in `_scratch/design-fixer/review-*`. The final audit outcome will be recorded in codex-review.md. No shared source or spec changed.
- The cold-review audit completed once in 29.7 minutes: 329 raw leads, 75 frames inspected, no runtime exceptions or controls stuck after resize. Confirmed comparison, annotation and picker-voice repairs received targeted rechecks afterward, including a hosted 375-pixel phone. No second full audit was run. Final bundle: 274,158 bytes (267.7 KiB). Owned Chrome/server processes were closed and host.html removed.

## Built

Two modes, ten broken posters, five live meters, Squint and eye-path badges, selection and keyboard editing, drag/corner resizing, snapping guides, layers, locked Biscuit, goal ticks, a persistent completion list and the before-and-after wipe. One generated desk painting is bundled; the measured poster parts remain flat editable vector art.

`src.html` starts with responsive desk/panel styles and markup, then poster data and lines, the numerical model, icon geometry and glyph masks, stable poster nodes, rendering, pointer/keyboard controls and mode/persistence wiring. `window.__tool` exposes the model and read-only diagnostics for checks. Only poster changes rebuild poster nodes; editing keeps the interactive nodes stable.

## Model and tricky parts

- Model coordinates are 1000 by 1414. Pull and weight use element bounding-box area, D65 sRGB CIELAB lightness and chroma. Text cap height is block height divided by its number of lines. The model notice is always under the meters.
- Contrast checks WCAG sRGB luminance. For overlaps, a 48 by 12 grid samples foreground glyphs against prior painted text and icon geometry. Canvas glyph masks cache normalized text and SVG paths provide icon masks. This is finite sampling; tiny overlaps can fall between samples. It is a teaching model, not a substitute for an accessibility checker.
- Icon cutouts paint the paper color, and the overlap model treats them that way. Color changes preserve these cutouts even after an icon has been white.
- The blurred poster is a separate SVG copy with CSS blur/grayscale. It explicitly toggles the SVG `hidden` attribute; setting an SVG `.hidden` property alone leaves the copy hidden. The transparent live SVG keeps receiving input.
- Corner dragging changes width and height independently. Bigger, Smaller, plus and minus resize proportionally. All movement is clamped. Snapping uses four screen pixels; unity edges and star-row alignment use four poster units.
- Tab skips the root SVG and visits poster parts in current top-to-bottom order, independently of the visual layer order. Programmatic focus always uses preventScroll.
- Every goal is recomputed on each rendered edit. Un-ticks are silent. The current attempt keeps its earned stamp after further edits; Start over or loading a poster starts a fresh broken attempt. Previously earned completions remain checkmarked in the menu.
- Clear progress removes `design-fixer-solved` and will not immediately re-award a still-met goal. Progress is a map of earned completions, not stored poster layouts. Studio work is intentionally temporary.
- Clearing hushes stale narration, closes the comparison and keeps focus on Clear progress. If all goals still tick after clearing, Hint names Start over instead of the hidden Before and after control.
- Active mode taps preserve edits. Reset on an already pristine poster is a no-op, so quick repeated taps do not cut the welcome. Sound reserves its label width to keep the header steady.
- Curio.voice owns narration scheduling; the tool owns the hint. How lines use V.heard and state validity; goal, fixed, locked and hint lines are events. Voice is big-sister, Leda, in the manifest. No audio was recorded in this build, as instructed; browser speech is the fallback.

## Art

`art/prompts.json` stores the house style and full desk prompt. The built-in image tool made `art/raw/df-desk.png`; the only art.py invocation was `--rekey df-desk`. Finished art is 1500 by 938, about 130 KB. The usable center is approximately x 18-84 percent, y 2-97 percent. The poster is centered inside this region after cover crop, with a width guard in tall narrow stages. No people occur in the image.

## Decisions and open questions

The spec contains no open-question section. These implementation interpretations are explicit:

- Keep all ten posters as listed: one unity brief and the final mixed brief, despite the introductory shorthand about two per principle.
- Use the stated 3 percent and 2.4 percent cap-height thresholds. Their 0.8 ratio is not exactly the source example's 18.7 divided by 24, which is about 0.779.
- Use flat measured vector parts and one rich painted desk, as the Art section leans toward. Do not add non-editable paintings inside posters.
- Add the small orange block to Biscuit's broken inventory so it can be enlarged and moved; there is no Add element control. This supplies the asymmetric repair described by the Sources example without extending the feature set.
- Honor the explicit "Nothing plays on its own" rule: no decorative idle animation. Squint easing and immediate edit/goal feedback provide motion when requested.
- At short preview sizes, the meters and hint remain together while the editor can scroll. At 375 wide, the stage and Squint appear first and the panel follows below, as specified. Small actual poster parts can be smaller than a 44-pixel tap target; their keyboard path remains available.

## Evidence

Scratch contains independent Python formula checks and reference fixes, browser/Python comparisons, real pointer repairs of all ten briefs, all required sizes, hosted 375-pixel phone frames, Motion off, grayscale, min/max resize, overlap regression, keyboard and voice logs. The full audit runs last and its findings are summarized in codex-report.md.

The full audit completed in about 29 minutes with 356 raw leads. No runtime errors, stuck controls, infinite animations or repeated how-to failures were found. Read width, compact hint placement and rapid mode/reset welcome cuts were repaired and checked with targeted follow-ups. Phone below-fold leads follow the specified stacked layout; small poster-part targets remain open. Transparent hit rectangles account for the reported hidden title text; the frames show the lettering clearly. The full audit was not repeated after those local fixes.

The final comparison and stamp checks include 680x425, 1280x720, 1366x768 and the hosted phone. The stamp sits slightly across the paper's lower edge so Science Night's footer stays visible. The finished bundle is approximately 260 KiB, including 130.14 KiB of painted art. All 36 runtime lines match the voice manifest.

## Engine changes wanted

`kit/curio.js`, `Curio.voice`, first-tap pointer/key listener: change the `closest('button')` target lookup to include native `select` and `input` controls before matching `opts.speaks`. The documented option currently cannot suppress a welcome for a native picker whose own instruction arrives on change. Design Fixer works around this using welcome validity while its part picker has focus. No shared file was changed.

## Audit harness note

The audit's `steps` method wraps a drag string in a function body. It needs a body with a top-level return, whereas drive.py needs a returning expression. The first audit recipe used the latter format, so that one audit state did not reach its wipe. The stored recipe was corrected for cold review and the missing comparison coverage was checked separately with real pointer input. A helpful shared documentation change would name this distinction in `scripts/audit_tool.py`, function `Audit.steps`; no shared file was edited here.

## Next

Cold review only. No commit, deployment or polish round was performed. Inspect small-poster hit targets and finite contrast sampling in the cold review. The 1280 by 720 editor and hint fit; the less-used Clear progress row can require a small panel scroll for the longest briefs. The specified stacked phone flow necessarily puts the editing panel below the first screen, so the general no-scroll rule cannot also be met there.

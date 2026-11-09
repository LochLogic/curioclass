# Packaging Challenge handoff

## Cold review changes, 2026-11-07
The single cold review played the bundle before reading this handoff or src.html. Full evidence and scripts are in `_scratch/packaging-challenge/`.

Lid cost rejects nonfinite input and restores its last valid price. Its event now follows price direction, interrupts stale price speech, and distinguishes cost from actual material. The sampled minimum is explicitly descriptive; near-minimum events report geometry rather than achievement, and are suppressed after Reveal best so copying the reference earns no praise.

Show curve describes a model curve even with zero or repeated dots. Reveal best keeps the best dimensions and objective on the bench, outside the scrolling detail panel, and gives its marker a brief Motion-aware arrival. Shelf describes model area rather than claiming measured real metal usage, and its Best label is separated from the point.

The drink illustration was redrawn with the built-in imagegen tool using the prompt in `art/prompts.json`. All keyed cutouts except the already-clean soup were reprocessed with art.py's despill option; the painted bench, shelf, metal cans and kraft style remain. No people are needed in this object-scale workbench or pantry scene.

The spec's four-can Shelf is retained. Its stated centimeter inputs remain the model's inputs; numerical results are recomputed from them. The spec's beverage height is an approximate specimen size, not a universal manufacturing dimension. Narration still uses the browser; no recordings were made.

Case labels its planned ratio Full-case fill, separate from the packed count. Small graph margins allow four-digit y values. The invalid-lid audit state keeps the permanent bench readout rather than a duplicate inside the scrolling detail panel, and purposeful fixture focus uses preventScroll.

Focused review evidence: `post-copy.json` has zero best-event credit after copying; `post-math.json` passes all 11 formula checks and all six case comparisons; `keyboard-final.json` reaches O2 at 3.84 with 17 keyboard trials and Reveal best focused. `voice-events.json` has five factual events, `voice-how.json` one how-to over five taps, `voice-main-post.json` all three mode instructions, and `read-off.json` Read with Sound off. The settled calm case has 24 packages and no running animations.

The cold review's single final audit completed within 40 minutes at `_scratch/packaging-challenge/review-audit/audit.md`: four leads, with all 91 frames inspected. One fixture selector was corrected to the bench's live readout; three first-tap welcome omissions are permitted by BASELINE 16 and the spec. All other size, state, Motion off, focus, runtime, repeat, quick-tap and resize checks passed. No second audit was run.

Build only, 2026-11-03. No commits, shared engines or other tools changed.

## Implementation
`src.html` uses the starter's kit header and control structure, the 9-12 theme, Curio.voice, Curio.tone and Plane. It lays out at actual pixel dimensions with ResizeObserver rather than scaling a fixed scene. The package SVG redraws while its stable handle retains focus and pointer capture. All buttons, sliders and number fields remain stable DOM nodes.

Orders store their shape, price rule, trial dots and personal minimum for this page session. Release records a trial; five dots reveal the curve. Reveal best leaves the student's shape in place and adds the exact analytic minimum. O6 reprices previous dots when the lid cost changes. Actual mass always uses unweighted material area.

Shelf cutouts are cropped through art.py and stretched to the published outside height and diameter on one shared scale. Their transparent button targets may be wider than a small can; the painted can itself retains the exact scale. Selection lifts a can by 10 pixels. Each graph uses that can's own outside-size cylinder volume.

Case uses 24 packages in a 4 by 6 grid. Six arrive immediately, with another six at 0.5, 1.0 and 1.5 seconds. A second tap, order change, mode switch, slider input or Motion change finishes a running drop immediately. Switching to a new order clears the packed count for that order. Resizing carries the current packing count forward.

`window.__tool` exposes state, setMode, order, set, best, shelf, lidCost, pack, model, optimum, allLines, vlog and vq. Modes accept title case or lower case. `set(value)` records a trial; `set(value, false)` updates without a release.

## Numbers and modeling decisions
- Compute from listed centimeter dimensions, not the rounded Shelf example results. No. 303 therefore has volume 572.5 cm³, material 385.8 cm² and best 381.7 cm²; No. 2½ has 996.2, 553.4 and 552.2; No. 10 has 3450.9, 1266.3 and 1264.2. Drink remains 420.8, 323.5 and 310.9. Percentage comparisons retain full precision, giving 4.1%, 1.1%, 0.2% and 0.2%.
- The exact O2 minimum is r = 3.837215..., h = 7.674430..., area 277.545024.... At the entered radius 3.84, h = 7.663304..., displayed 7.66. Reveal best correctly displays its own 7.67 height. The same distinction applies to entering 2.66 in O6 versus the exact 2.660576... minimum.
- Case mass uses 24 × actual area × 0.03 g/cm², explicitly a practice number. Box and tray readouts label it a practice metal equivalent, not real cardboard mass.
- No personal work is saved. Only the kit's shared Motion preference persists on this device.

## Open question settled
Keep four real, unbranded cans. This is the option the spec leans toward. Do not add an invented cereal box with brand-dependent dimensions.

## Art and narration
Twelve new OpenAI gpt-image illustrations plus the existing kraft texture, all in `art/`. Prompts and provenance are in `art/prompts.json`; original generated PNGs are in ignored `art/raw/`. Soup was redrawn twice to make neutral steam; the soda was redrawn once to remove key-color reflections. Final soup also uses art.py's despill option. No people were generated.

Voice bank: hero-coach / Puck. `voice/lines.json` lists nine lines. No recordings were made, as this build forbids recording. Browser speech is the active fallback, so the intended bank voice is not yet audible. Tests use muted Chrome and inspect the kit's narration log; no listening review was performed.

## Layout and verification
Main controls remain visible at the standard sizes and 375x812 iframe. Short landscape keeps stage and panel beside one another. Portrait stacks controls beneath the stage. The live material is also printed on the stage so dense secondary readouts can scroll within their own panel. On the shortest landscape screens O6 omits its decorative order card to make room for both sliders and the hint. Net occupies a strip below the package, with no overlay on the graph, and starts open at 900 pixels tall or above unless the user has chosen its visibility.

Evidence lives only in `_scratch/packaging-challenge/`: independent numbers, math assertions, real jittered drag, held-click student path, keyboard completion, all-size frames, extreme shapes, Motion off, grayscale and final audit. The keyboard run uses native closed-select arrows followed by Tab; Enter on a closed select opens its menu and is not needed to confirm an arrow-key change.

The first phone host requested its own missing favicon. The host and tool now use an inline empty icon; subsequent phone shots were clean. A screenshot batch also overlapped a previous Chrome process; only the interrupted shots were retried with an isolated allowed port. Neither was a tool runtime failure.

## Engine changes wanted
None. All workarounds remain in this tool.

## Next review
Read `codex-report.md` and the audit leads before making changes. This is the end of the build, not a polish round. A classroom trial, headphone review and recorded narration remain outside this run.

## Audit closure
The single full mechanical audit completed with 24 leads in `_scratch/packaging-challenge/audit/audit.md`. Its 89 frames were inspected. Post-audit changes fixed 21 leads: the Case target, every height-label overlap category, O6 hint clipping, the curve crossing BEST on a phone, and welcome speech cut by repeated mode or Clear taps. Targeted checks cover these repairs; the full audit was not repeated.

Three first-tap welcome omissions are intentional. The spec makes the Orders welcome stale after the first release; Show curve and Reveal best have their own first-tap instruction. STANDARDS says a tap's own speech skips the welcome. The fixed-volume premise remains visible, and Read speaks the current next action.

Repeated clicks on the selected mode now finish any visual motion without stopping valid speech. Clear preserves an active Orders welcome, which still fits the unchanged order. Height labels are to the left of the package, outside the right-side handle's transparent target. BEST is below the minimum, where the material curve cannot cross it.

# Living Pond build handoff

`src.html` contains the instrument CSS and markup, the conservative model, and the display and interaction controller in that order. `living-pond.html` is the generated offline bundle. No shared file was edited. There is no lesson sequence or achievement layer.

## Model

The model uses sixteen matter pools plus fixed adult turtle mass. Seven daily substeps share a proportional outflow limiter. Minnow shade is eight matter pools. All population rates are deterministic. The tracer alone uses a seeded linear congruential draw to choose among actual transfers. Visual positions are deterministic seeded functions.

Habitat changes are applied immediately and recorded with the current week. A 104-week counterfactual is computed from the pre-change state. Saved ponds store the starting choice, action log and week. Open reconstructs silently; Replay applies the same marks at Fast. Storage calls are guarded.

Energy resets at the calendar boundary. `lastEnergy` supplies the last-year column beside the current year, including at week 0.

Decomposers Off freezes their activity and body pool; this hypothetical switch matches the brief's dormant specks and ensures that turning it back on can recover an early collapse. If algae have actually gone extinct, decomposers cannot create new algae; restocking is needed.

## Art

One 6 × 6 atlas holds the 36 requested painted objects and places. Canvas crops its cells, and all live water, positions, tint, ice thickness, charts, dots, arrows, ledgers and gauges remain code. Raw generation is preserved in `art/raw/`. Prompts are in `art/prompts.json`.

The prescribed `scripts/art.py --rekey` command failed because the available Python lacks NumPy. `_scratch/living-pond/prepare_art.py` creates a browser canvas packing page; the assigned-port drive produces a keyed WebP data URI, and `assemble.py` saves it and assembles the source. This is deterministic packing, with no paid service or software installation.

## Evidence

All build scripts, the historical specification, raw check results and frames are under `_scratch/living-pond/`. `model-results.json` records the ten-winter and intervention runs. `verify-model.js` checks conservation and finite values through every step; `verify_numbers.py` independently checks scenario thresholds and the seasonal calendar.

Browser evidence covers immediate input, tracer transfers, save/open, Replay equality, blocked storage, voice ordering, extreme populations, motion, grayscale and responsive layouts. The final mechanical audit is under `audit/`. Its leads are answered in `codex-report.md`.

## Engine changes wanted

- `scripts/art.py` imports NumPy and SciPy for rekeying. Document or supply a supported interpreter for the build environment, so the normal art packing command works without installation.
- `scripts/drive.py`, key map in `main`: add arbitrary letter/digit shortcuts. Its current map raises KeyError for `l`, `n`, and `3`. This build's live-walk harness sends proper CDP key events without changing the shared script.
- No ecosystem engine promotion requested; this remains a tool-local model as the spec directs.

## Known limits

The historical specification provides formulas and claimed outputs, but no executable reference implementation. The explicit simultaneous conservative flows do not reproduce every historical range exactly. The report gives actual outcomes rather than repeating unverified historical numbers. The first ghost can take more than the requested 5 ms. Desktop headless timings do not establish Chromebook performance.

The selected gravel-ranger recording is not bundled. The kit uses browser speech. The first hint speaks once after a touch unless that touch stocked or fed the pond. Per the settled Refine call, plain event readings describe ice, low oxygen, winterkill, departures and vanished snails. Each has a 20-second cooldown, a four-second expiry and a current-state validity check. Read speaks the live instrument.

OpenStax's current page licence differs from the old spec. It and EPA/DNR are references only, with no source text, figures or data copied into the instrument. The Manual records current terms and original model provenance. No measured ecological dataset is represented.

## Cold review changes

Review evidence uses review-prefixed files in Scratch. The model coefficients and conservative transfer order are unchanged. Energy labels now distinguish net production and use of stores. Open reconstructs the final chart snapshot after actions at the saved week. New/Open clear transient selection and movement accumulators. Shortcuts respect the open drawer and native confirmation dialog.

Specimen cells are trimmed to alpha bounds in the browser and fitted without changing their aspect ratio. Food-web arrows anchor to current hitboxes, with missing kinds labelled absent; Life inspection is also available with Enter on the tank. The heron stands clear of the calendar. The new generated shore atlas has four full-width seasonal strips, drawn as a background, never as model data.

New shore prompt and original PNG are in art/prompts.json and art/raw/pond-shores-v2.png. The built-in imagegen skill produced it. scripts/art.py --rekey still fails at its NumPy import in the supplied interpreter; bounded browser canvas encoding supplies the WebP without touching shared code.

The review also dates the latest log entry in Read, animates model-driven heron departures using the existing flight pose (stationary with Motion off), and fits all Net controls at compact landscape widths without removing icons. This last layout correction was confirmed by the single review audit and re-shot at affected widths.

Ghost traces retain long dashes. The Refine fix uses 0.35 alpha to distinguish these projections from the actual pond. Actual traces keep their original colours and dash patterns, with separate stem algae and optional shade histories.

Hidden chart chips keep full label contrast and use strike-through to indicate hidden traces. In Net mode the decomposer key reads Specks and explains that they cannot be netted, rather than promising a Net 1 action. The bundled source includes its MIT notice and links the original content licence. Final save-control verification covered Rename, cancelled/confirmed Delete, the eight-save cap and all New choices, and restored the review-profile fixtures.

## Refine fix implementation

Seven dropdowns were replaced locally by detented rotary switches and a decomposer lever. Their values, defaults and existing shortcuts are preserved. Arrow keys and Home/End operate the switches; accessible value text follows the printed value. No shared kit code changed.

Snapshots now record separate floating and stem algae counts and average minnow shade. The optional shade trace uses its own 0 to 7 scale. Matter Enter and pointer taps both choose the nearest visible dot. The trip records weeks in the current pool and names decomposers on the direct muck-to-water transfer. Transfer weights and population equations are unchanged.

Flow records carry the existing transfer kind and an eater attribution solely to label Energy heat at the breathing eater, including digestion by ordinary eaters and fixed adult turtles and herons. Decomposers have their own heat arrow. These metadata do not change transfer amounts. Charts and the oxygen meter redraw on state changes, rather than every animation frame. Motion off also suspends idle tank drawing. A swipe computes its unchanged ghost once on release or cancellation.

At phone width the seven recorder keys use short names in two rows, keeping Stems, Shade and Whole run visible. Their full values remain accessible. The tray retains its specified scrolling row. The final mechanical audit is run once; any corrections from its leads have scoped follow-up frames instead of another full audit.

Fix evidence is under `_scratch/living-pond/fix-before`, `fix-after`, `fix-targeted`, `fix-voice` and `fix-audit`. `fix-model-parity.json` compares 27 habitat combinations for 520 weeks each against the pre-fix source, with zero population or oxygen drift.

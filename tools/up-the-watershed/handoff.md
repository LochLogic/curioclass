# Up the Watershed build handoff

Build only, 2026-10-31. No commits, branch changes, deployment or polish round. Writes are confined to this tool and `_scratch/up-the-watershed/`.

## Structure
`src.html` began with the kit starter. It contains the responsive CSS, semantic controls, SVG watershed, load model, evidence validator, session controller and persistence layer. Kit CSS, the grade 9-12 theme and Curio.voice are bundled without changes. There is no family engine.

The major pure functions are `model(weather, plan)`, `evaluate(plan)`, `share(source, weather)`, `cost(plan)` and `validEvidence(source, sampleIndices)`. Display values come from the unrounded load model, then round for samples; cleanup calculations retain full precision. `renderGauges` presents concentration and load changes separately. The source table's beach has only E. coli; other beach tests explicitly say Not modeled.

Controls are built once. State updates change values and attributes rather than replacing active controls. A plan-version token invalidates the 400 ms test beat and subsequent 400 ms gauge fill when any fix changes. Motion off keeps the test beat and removes the fill motion. Progress is under localStorage key `up-the-watershed`, guarded with try/catch. Saved plan explanations live only in the in-memory reasons object.

There is one actual `#hint`, moved into the appropriate Sample/Claim or Fix-it container. Read always speaks the current visible hint. Same-mode taps preserve narration; distinct event occurrence keys keep repeated solved, last-kit and out-of-kits lines in the queue. Mode changes and dialogs stop lines whose context has passed.

## Art
All 22 specified images are present and used. Eight existing scene WebPs and their prompts were retained. Fourteen missing assets were generated with the built-in OpenAI image tool: two case scenes, seven miniatures and five aerial textures. Full prompts and provenance are in `art/prompts.json`; originals are in `art/raw/`. The mandated free `art.py --rekey <name>` path produced WebPs. The active names retain the eight existing short names instead of renaming files.

The map clips tiled 256 px textures to code shapes and darkens them with palette layers. Labels, sample flags, brackets, results and flowing water stay in code. Icons are full illustrations rather than generic pictograms. No person appears in any image.

## Spec open questions resolved
- Title: use **Up the Watershed**, the option the spec favors.
- Rain advisory: retain it as an honest protection option. It can meet the beach goal through storm closure while explicitly showing water still over 410. It never reduces the modeled pollutant.
- Costs, flows and loads: retain the fictional, scaled teaching model. Say so on screen and in notes; do not imply real cost estimates or universal field efficiencies.

## Important presentation choices
- The EPA 410 statistical threshold is called the fictional case action line, not a universal legal closure rule. The 126 geometric mean is not treated as a single-sample test.
- Compact cleanup cards show art, name, price and Add/Remove. Fix details exposes every effect and who-pays note to touch and keyboard users. Larger laptop cards also show it inline.
- A pinned result allows pointer input through its noninteractive body so it does not block the next sample spot. Its Close control remains interactive with a reserved 44 px header area. Resize repositions the existing result without rebuilding its control.
- Evidence buttons appear for checked suspects. Unchecked rows reserve their space without presenting a disabled action.
- Whole-creek revelation supplies all results and source shares, but does not invent sampled evidence for claims. Source shares replace the checkbox area's reserved footprint; all 22 map flags remain unobscured. Hide whole creek restores the choices without moving Submit.
- Responsive source positions use the icon image centers to redraw map evidence brackets. Compact flags move beside or above crowded sites. Dry stays before storm, and letters preserve the distinction in grayscale.
- B1 and B2 combine multiplicatively on the remaining field nitrate load.
- Voice uses the specified casual-peer bank identity in `voice/lines.json`. No audio was recorded; the kit currently uses browser speech fallback, so the actual bank timbre awaits recordings.

## Evidence map
`_scratch/up-the-watershed/watershed_numbers.py` independently computes samples, worked plans and all 512 combinations. `browser-model-results.json` compares the JavaScript model against 4,174 independent numeric comparisons. `display-results.json` checks all 88 displayed sample cells. `final-paths/` holds the final real-click case routes. `responsive/` holds the full size/mode sweep. `bars/` contains isolated copies and bundled reference tools, keeping their original tool folders untouched.

The single mechanical audit is under `audit/`; it completed with 549 original leads. `audit-dispositions.csv` responds to each original lead. Focused post-fix checks are under `focused/`, `last/`, `result-finish/` and `voice-finish/`. The full audit was not repeated. `frame-sheet-manifest.json` maps inspected contact sheets to their original screenshots. `validation-manifest.json` points to the main final evidence.

## Engine changes wanted
None. The iframe test host requests a favicon by default; the scratch harness adds a data favicon to the temporary host page rather than editing drive.py.

## Remaining validation
The cold review is recorded in codex-review.md. Recorded voice timbre and classroom duration remain unmeasured. This tool uses browser speech fallback; no recordings were made during build or review.

Precision nit retained from the spec: E alone gives exactly 0.0475 mg/L dry inlet phosphorus. The three-decimal display is 0.047, as in the spec, because of binary rounding. Raw goal checks are unaffected.

## Cold review changes, 2026-11-03
- Fixed `share`: the treatment plant lies below S7, so it contributes zero to the Muddy creek target. Background shares now sum correctly.
- Added a visible Fix details disclosure of all effects and social costs, usable by touch and keyboard at compact sizes. Kept the nine-card choice set.
- Kept dry, storm and change row labels in phone gauges. Added the 20 percent culprit criterion to the initial Claim instruction.
- Isolated claim feedback by case and invalidated feedback when attached evidence changes. Selecting a map spot with no accusation restores the actionable Claim hint.
- Lifted sampling with a brief shaded vial fill plus the existing ripple. A dry Pipe keeps the vial empty; Motion off preserves the result and removes movement.
- Redrew `uw-i-cattle` using built-in OpenAI image generation, processed through `art.py --rekey uw-i-cattle`; prompt and provenance are in prompts.json.
- Expanded audit states with compact Fix details, over-budget and exhausted-kit states. Review evidence stays in `_scratch/up-the-watershed/`.
- Cancels a pending cleanup test on mode exit, so its late result cannot replace another mode's hint. Logbook distinguishes no flow and unmodeled tests without attaching measurement units.
- Speech remains browser fallback. No recordings were made. No shared kit, scripts, docs, other tools or git history were changed.
- The single review audit completed in 2,302 seconds with 285 leads. The 285-row disposition file and all 67 audit frames are in Scratch. Confirmed layout and voice leads received scoped rechecks; no second full audit was run.
- Compact header layout keeps the map, kits, Take sample and Make claim inside the phone viewport. Flags have explicit gaps from circles and labels at every checked size.
- Exhaustion and budget-threshold events preempt obsolete welcomes. Empty evidence and empty portfolio instructions name reachable controls.
- Native dialogs now include their own Read button because the page header becomes inert while a dialog is open. Field photos use contain and a viewport-based height cap to preserve the whole scene.
- Three actual saved alternatives were tested together, including the advisory plan, the $1,595,000 alternative and E alone. Plans survive reload; Why notes remain session-only.

# Model Mechanic handoff

Build only, 2026-11-02. No commits. Start with src.html, the spec and codex-report.md for checks and limitations.

## Structure

src.html starts from the kit starter. Its CSS lays out an instrument bench, with the toolbox before the stage in DOM keyboard order. Data generation uses MLLab.rng, uni and r2. Training uses the family knn model; evaluation and confusion rendering use the family engine. No kit files were edited.

Work Orders keep their current index, labels and edits across Garage switches. Garage resets when left, so its edited labels last until Reset or a mode change. evaluate computes results; run updates goals and starts a 400 ms count tween. snapTween finalizes that tween before student input. Photo inspectors are native modal dialogs with focus restoration. Fixed training order is animal, day, night. WO3 wrong label indices differ by day and night because the specification counts all thirty deer together.

revision changes when the configuration changes. Each score event has a unique run key, so repeated identical scores are not collapsed at a two-second tap pace. Do not replace those keys with one shared score key. Completed orders can still be inspected, and closing the drawer restores their repair note. Test photos keep the model's answer tag when enlarged and show the true animal in a separate caption.

Responsive controls move the hint above the phone stage and put Run and Reset in the phone header. Desktop toolbox hints and Run are sticky during scrolling. The short landscape photo inspector uses two columns so all four label choices stay visible. The smallest landscape matrices place their time tabs on the right to preserve 44 px cells. Narrow matrices use letter labels with an explicit species key.

## Open question decision

Took the spec's painted-cutout direction: seven animal/grass assets sized by Size, four measured values shown as bars when enlarged. The scene explicitly says the paintings do not encode every feature. Exact classification uses all selected numeric clues. No code silhouettes substituted.

## Art

Preserved both existing FLUX clearings. Seven new assets made with the built-in imagegen tool and copied to art/raw, then processed only with art.py --rekey. Full subject prompts and house style are in art/prompts.json. No people.

Final cutout options are holes=true and despill=false. The shared magenta despill pass left blue edge pixels; the hole-aware rekey removes that blue fringe. Fine key-colored specks can still be found at full asset resolution, but the final in-scene frames were inspected after processing.

## Engine changes wanted

- `kit/ml-lab.js`, `view.confusion` / its `host` redraw: capture the focused cell's row and column before clearing the SVG, then focus the replacement with preventScroll after resize. The tool restores focus during its own updates; pure engine resize redraws remain an engine responsibility.
- `kit/ml-lab.js`, `view.confusion`: allow distinct rowClasses and colClasses. The zero-training workaround currently uses a fifth No answer column plus an unused zero truth row. Four truth rows and a separate abstention column would express this edge case more cleanly. No kit file was edited.
- `scripts/art.py`, `cut_out`, magenta despill branch: compute the spill mask before changing either red or blue, then apply it to both channels. Recomputing the condition after red changes can leave blue edges. This build uses the existing holes option instead; the shared script was not edited.

## Follow-up

The single mechanical audit reached its 40-minute cap without writing audit.md. All 54 generated audit frames were inspected. Targeted checks passed after repairs, but this is not a completed full audit. Evidence and profiles are in _scratch/model-mechanic. No Chrome or server should remain running, and host.html is removed.

Narration is browser fallback, with science-narrator and all 53 fixed lines prepared in voice/lines.json. Do not record automatically. Browser voice identity and offline speech depend on the browser's installed voices.

## Specification edge cases

- Kept Size height exact and clamped the seeded horizontal position to keep animals inside their frames. The unclamped 10-to-60-percent left positions can crop wide fox and raccoon cutouts.
- A zero-count animal can still be predicted if the student gives its label to another animal. This is correct nearest-neighbor behavior and an exception to the spec's blanket zero-count prediction statement.
- All eight wrong labels are reachable using Size only and k=9. Restore all clues and k=1 for the reference 37/40 result.

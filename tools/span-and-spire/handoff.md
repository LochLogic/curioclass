# Span and Spire: current review handoff
Cold review, 2026-10-30. No commit, deployment or voice recording. The original build handoff is preserved below
as historical evidence; its missing-art and layout statements have been superseded.

## Current files and behavior
The readable source is src.html. The kit owns Motion, Sound, Read, narration queues and basic tones.
The direct-stiffness solver, modal solver and explicit collapse engine remain local to the tool.
All 27 paintings are now present in art/, with original PNGs in art/raw/ and provenance in art/prompts.json.
They were generated individually with the built-in imagegen tool and packed only through art.py --rekey.
Seven assets were redrawn for subject accuracy, axle counts, a tank without extra support legs and full soil texture.
Cutout edge spill was removed through the existing pipeline. No images contain people.

## Review repairs
- Nonlinear cable shakes render and score the actual explicit forces and displacements, track peak sway,
  classify failure as a shake and use simulated time when the 600-step cap slows the model.
- Design edits reset wind qualification. Shake edits restart a full qualification window and clear prior explicit state.
- Borrow replaces a matching member's material, so borrowing stronger tower legs works. Ghosts stay with their mode.
- Top loads remain with Go and materials before scrolling settings. Primary shelves stay available while scrolling.
- Compact Promises opens all choices in a native dialog; reasons are inline for touch users. Focus returns without scrolling.
- Old farm bridge is always present, including first Yard entry. Card thumbnails are larger.
  Truck results in a tower column say not applicable.
- Cable mechanisms trigger bSlack. The tFold line no longer claims that every loose structure has no triangles.
  Worst spots updates its hint immediately. Crossing narration captures the actual truck and design revision.
  The road-gap event is short enough for repeated two-second input; its hint retains the full building instruction.
- Vehicle proportions use actual cutout dimensions. Turning hub marks no longer paint a second set of tires.

## Verification and open reference questions
Evidence: C:/Users/Cory/AppData/Local/Temp/curio-codex/span-and-spire.
Independent NumPy/SciPy calculations confirm the full-member-weight and plate-mass disagreements in the historical
table below. Pratt 4 m / semi is 101.6595%, Warren / semi 57.5738%, and narrow tank sway 0.762857/s.
No solver values were fitted to the reference examples. Nonlinear cable slack was exercised live:
current forces matched the explicit engine exactly while the shake continued.
All 24 mode/size frames were inspected, including a real 375-wide iframe. The host favicon 404 is a harness
request, not a request made by the tool. Keyboard-only construction, Motion off, grayscale, a full 15 s shake,
material borrowing, a fresh wind window, member 61 refusal and minimum settings were checked.
Recorded narration remains absent and browser audio was muted; voice timing is assessed from the kit log.
The cold review audit reached its 1,800-second limit without producing audit.md. All 82 captured frames were inspected.
Its owned Chrome and host were closed. No second audit was run. See codex-review.md for the verification limits. Actual Chromebook performance and exact spec reference
numbers remain open. The local frame-time measurements are not a hardware certification.

## Historical build handoff

# Span and Spire: build handoff

Build only, 2026-10-30. No commit, deployment, art generation, voice recording or polish round.

## Files and structure

`src.html` is the readable source, adapted from the kit starter. The palette, responsive layout and controls come first.
The script contains material and truck data, kit voice lines, direct stiffness algebra, cable active-set iteration,
mass-normalized modal analysis, the explicit collapse integrator, session state, canvas rendering, Yard and input handlers.
The generated `span-and-spire.html` is the offline draft bundle, not an alternate source.

The kit owns Motion, Sound, Read, narration queuing and basic tones. Ambient engine and wind synthesis is gesture-gated
Web Audio, follows the kit Sound state, and makes no files or requests. `voice/lines.json` uses firm-captain / Alnilam.
No recordings were made. `art/prompts.json` lists the 27 specified assets; nothing was painted, downloaded or drawn as
replacement art. The bundler supplies labeled draft placeholders. Source, notes and JSON have no em dashes.

## Settled choices

- Prices are game prices. The material shelf, cost display, tooltips and notes say so.
- Old farm bridge appears only after the first save. It cannot be renamed or deleted; Open makes an editable copy.
- Steady sine shakes only. No historical earthquake record was fetched or invented.
- `shakeInput.acceleration(t, settings)` is the extension point for a future verified record. Its companion
  `displacement(t, settings)` drives the true-size table drawing. Add a record only with provenance, units, time-step
  and integration checks; keep the existing two-second ramp and fifteen-second steady test distinct from that record.

## Physics

All calculations use SI units. Each side gets half the axle loads and a 2.0 kN/m slab load. Each member gets its full
stated self-weight, split between its ends. Bridge supports are a pin and roller; extra terrain footings are pins.
Truck axles use lever-rule interpolation between road joints. Stiffness matrices, factorizations and loose modes are
cached by design object and active cable mask. The smallest stiffness eigenvalue is checked against 1e-9 of the largest.
Cables drop the most squeezed active member and re-add a stretched inactive member, bounded by twice the cable count.

Towers use six mass-normalized modes, 20 kg plates, the chosen top mass, 5% damping and 1 ms integration steps. Tower
cables include 100 kN installation pull and geometric stiffness. Slack switches to nonlinear central differences.
Collapse recomputes axial forces from lengths and directions, removes failed members, includes ground contact and
uses centered Rayleigh damping. The damping increment is solved with a cached factorization, avoiding numerical
explosion from a separate high-frequency damping restriction. At most 600 explicit steps run per frame; excess demand
shows slow motion. A failed bridge member is removed and the remaining structure is re-solved before a full collapse.
The slab contributes inertial mass in bridge collapse. The truck rides its road segment until a twenty-degree tilt,
then slides and falls; its axle mass detaches from the deck. Water contact triggers the splash before crane recovery.

Motion off keeps physical time and integration. The failed tower is shown as still poses rather than a motion loop.
Pluck input accounts for displayed magnification, so the top follows the pointer instead of moving twenty times
farther than it. The load body and highest joints are pluck targets. Shift with an arrow provides a keyboard pluck.

## Editing and persistence

Drag from a joint to add a member. Shift drag moves a free joint, resolving the spec's two competing uses of a drag
from a joint. Tap a member to change its material. Keyboard arrows / Enter build; Delete erases; 1 to 5 choose material;
Space runs or stops; R rebuilds after failure. Undo and Redo retain fifty edits. Crossings never become joints by accident.

Changing a truck or design re-solves immediately. A saved design is a snapshot. Yard Open edits a copy; Borrow maps
joint coordinates and overlays selectable pink member ghosts. Save stores designs, promises, test results and resonance
dots. Tags and the first-save flag also persist in `curio-span-and-spire`; every storage access is guarded. Session
storage fallback is visible in the panel. No transfer code, upload, account or network service exists.
Mode changes pause and retain each mode's current test. Changing shake or wind settings during a shake starts a new
fifteen-second qualification window while motion responds immediately. Valley quake results are stored separately
from other shake speeds, so the comparison table never relabels a different shake as the Valley quake.

## Numbers check and spec disagreements

Scratch evidence: `S:/CurioClass-codex-scratch/span-and-spire/reference_check.py`, `numbers.json`, `more-numbers.json`,
`comparison.json` and the `*-browser.json` files. Python uses NumPy / SciPy independently of the browser implementation.
No reference percentage is fitted into the product. Keep the spec unchanged until its reference calculations are resolved.

Full stated member self-weight produces these whole-crossing worst uses, in percent:

| Design | Game price | Pickup | Bus | Fire | Grain | Semi |
|---|---:|---:|---:|---:|---:|---:|
| Bare deck | 3,300 | loose | loose | loose | loose | loose |
| Pratt 2 m | 7,442 | 39.60 | 80.56 | 102.63 | 116.64 | 114.29 |
| Pratt 4 m | 8,297 | 32.46 | 67.46 | 85.37 | 97.09 | 101.66 |
| Pratt 5 m | 8,771 | 38.16 | 78.78 | 99.55 | 113.15 | 118.45 |
| Pratt 6 m | 9,263 | 46.04 | 94.39 | 119.12 | 135.30 | 141.61 |
| Old farm Howe 2 m | 7,442 | 35.64 | 74.05 | 93.45 | 105.76 | 109.05 |
| Pratt cable diagonals | 8,071 | 31.93 | loose | loose | loose | loose |
| Crossed cables | 8,976 | 32.54 | 67.54 | 85.45 | 97.17 | 101.74 |
| Warren 4 m | 8,783 | 20.23 | 40.71 | 51.74 | 58.75 | 57.57 |
| Warren shoestring | 8,364 | 19.75 | 40.23 | 51.26 | 58.27 | 57.10 |
| Pratt 2 m with pier | 9,992 | 22.99 | 44.71 | 58.16 | 64.94 | 66.53 |
| Pratt 6 m with braces | 10,224 | 13.97 | 27.63 | 34.98 | 39.66 | 38.87 |
| Pratt 6 m, big end posts | 10,273 | 14.06 | 27.72 | 35.07 | 39.74 | 38.96 |

The browser agrees with the independently rounded Python bridge values within 0.005 percentage points. In particular,
the spec's Pratt 4 m semi 99.6% pass and crossed-cable semi pass are not reproduced: both slightly exceed 100% using
the stated loads. Warren and shoestring still pass comfortably, and shoestring keeps all six promises. The cable bus
mechanism begins at front 5.15 m rather than 4.7 m. A 55-member, 24-joint, twelve-panel crossed-cable interpretation
costs $16,295 and reaches semi 55.05%; the source's $14,656 shape does not fully specify its cable assignments.

Tank tower, 20 m: 2 m timber sway 0.76286/s; shake 0.30 g at 0.8 reaches about 426% and first fails near 1.88 s;
1.4 holds at about 36.24%. Width 4 m: 1.42140/s; 1.4 fails near 2.07 s. Steel: 1.35554/s and fails near 2.49 s.
Empty top gives 3.57909/s, not the spec's 4.32; bell gives 1.43343/s, not 1.47. These use the specified joint plate
and full member masses. The qualitative stiffness / resonance and lighter-top discoveries remain reproducible.

Wind checks reproduce the supplied main comparisons: narrow tank tower wind 50 at 72.31%, wind 70 at 132.35%; the
30 m stepped spire wind 70 at 97.81%. The 26 m 4-then-2 m town tower reaches wind 61.04% and Valley quake 51.28%.
The guyed tower is 1.89996/s; it survives 0.8 and fails 1.4 after the cable/slack explicit transition. Its exact peak
and failure time differ from the reference. The nonlinear cable transition deserves further independent calibration.

Tap pressure recomputes as 127.53, 225.63, 284.49 and 323.73 kPa at heights 10, 20, 26 and 30 m. Bridge Formula
results are about 52,732 and 85,525 lb before the semi's 80,000 lb cap. Euler timber squeeze limits are 312.28,
156.14 and 78.07 kN at 4 m, square root of 32 m, and 8 m. Contrast ratios reproduce the spec: ink/panel 14.29,
muted/panel 7.69, pink button text 7.17, pull/paper 9.15, squeeze/paper 9.31 and focus/paper 7.07.

## Play and graphics checks

A fresh agent played for 10 minutes 22 seconds through real held clicks, whole-pixel drags and keys, with no fixtures
or builder hooks. It chose another tower experiment at the end and explained resonance using its own runs. The
original hint blocked Tower's starting joints; that was repaired mid-session and verified by the fresh player.
Later builder checks verified the Motion-off collapse, tank pluck target and redraw invalidation repairs.

Graphics use lit material layers, wood grain / steel highlights, gusset bolts, force arrows, double squeeze lines,
slack waves, bowing failure, nonlinear falling geometry, creek ripples, recovery hook and inspection stamps. The
painted places, trucks and props remain labeled placeholders. Their finish is not equivalent to the painted bar
tools; art and recorded voice remain explicit draft dependencies, not a reason to make replacement art in this run.

All STANDARDS sizes were shot once in every mode, including the real 375-wide iframe on host 8775. Only sizes touched
by a repair were re-shot. Scratch contains frames, test plans, browser profiles, logs and the side-by-side bar frame.
The single full audit stopped at its 30-minute limit. It saved 79 frames but never produced `audit.md`.
All 79 frames were inspected. A focused repair check then verified the phone Go / Rebuild targets, actual Tower
drags, slider endpoints, modal welcome suppression and still recovery poses. It saved ten additional frames.
The overlap checker includes intentional canvas overlays and descendants of closed Promises details; those are
not visible collisions. The complete voice / input audit remains unfinished. See the final `codex-report.md`.

## Engine changes wanted

None in the kit. Both structural engines live inside this tool as specified. Do not patch shared kit files to resolve
the reference-number discrepancies.

## Still to verify or resolve

- Resolve the reference self-weight / mass calculations before accepting Done when 2 to 4 at their exact figures.
- Independently calibrate nonlinear prestressed cable transitions and large-motion ground contact.
- Benchmark on an actual school Chromebook. Windows frame timing is useful evidence, not that hardware test.
- Painted art and recorded narration remain absent by instruction. Review their integration in the later authorized phase.
- The fresh play check was an agent play check, not a human usability study. Sound was muted in browser automation.
- Complete the interrupted voice / input audit and a clean final ten-minute play check in the later authorized round.
- At 680x425, Tower's top-mass choices require scrolling the control panel. The main action and material row stay visible,
  but the broader short-choice visibility rule is not fully met. Resolve without reducing the scene to a thumbnail.

# Hallway Art Museum build handoff

Built 2026-11-01, Build only. No commit and no polish round.

## Layout and code

`src.html` starts from the kit starter and uses the shared kit CSS, controls, tones, and `Curio.voice`.
The three views share one live wall element, moved into the Opening day view without duplicating its state.
Controls are created once. `render()` updates their attributes and artwork interiors while preserving button focus.
The content table, home rules, center calculations, checking, narration, rendering, and pointer handling are separate
sections in the script. `window.__tool` exposes state, calculations, actions, and voice logs for review.

Choose has a real 4 by 3 grid over the painted cart. Compact landscapes retain a side height panel and a full-width
home tray and bar. The phone uses a three-row header, a wall above the height controls, and a two-row home tray.
The wall uses real pixel layout with a centimeter-to-position mapping; it is not a scaled fixed desktop canvas.
Artwork has a minimum drawn size to keep little clay and rock pieces recognizable in previews. Center calculations
always use the spec's actual artwork sizes, including fractional centimeter centers on cases.
The painted support meets the displayed artwork's bottom after that visual size adjustment. Do not measure the
illustrated object or pedestal against the ruler to infer its physical dimensions; the center value is authoritative.

## Important behavior

- Reasons belong to pieces. A theme change keeps the collection and recomputes literal matches.
- Only colors and story reasons justify a nonmatching piece. The theme reason does not falsely make it match.
- A selected tray piece can be placed by tap or drag. A displayed piece swaps with the destination bay.
- Window homes clear for every piece moved outside bay 3, including the other half of a swap.
- Wall height clamps to 40 through 200 in 5 cm steps. Stand and case centers derive from level and half the piece size.
- Kid eyes is view state only and remains on through dragging. It evaluates centers in the inclusive 70 through 140 band.
- A change invalidates the ribbon. A successful check earns and speaks it again. A repeated unchanged check opens the rows.
- Opening day accepts unfinished work and has no score or win gate. Next piece wraps through all five bays.
- Start over confirms and clears the collection and hallway. Nothing is saved between visits.

## Narration and motion

The bank is upbeat-guide, Zephyr, with the specified bright tour-guide style. `voice/lines.json` contains the complete
fixed narration inventory. No audio was recorded, as required for this build, so actual playback uses browser speech.
How-to lines use `V.how`; piece descriptions, role prompts, check notes, and ribbon results use events.
Checks and mode changes hush obsolete speech. Queued notes are tied to the hallway revision and open check dialog.
Read takes its content from the card, check notes, role prompt, or current next-action hint.
The Stand and Glass case have their own Low/Middle/Tall instruction so their hint names the controls actually present.
Tap or key input finishes running finite animations immediately. Motion off explicitly removes all tool loops and transitions.

## Art

All 22 specified assets were generated with the built-in image tool in one gouache and colored-pencil house style.
Full prompts, size budgets, provenance, and keying options are in `art/prompts.json`. Raw originals are in `art/raw/`.
The free `scripts/art.py hallway-art-museum --rekey <name>` path made every finished WebP.
The art cart and snowman received edge despill. No people were generated and no art remains to paint.
The tree is translucent tissue collage; the glass case, ruler, band, badges, ribbon, and labels are code.

## Checks and evidence

Scratch is `_scratch/hallway-art-museum/`. It contains numeric recomputation, image provenance paths, art and frame
contact sheets, the two bar-tool bundles and frames, real-input shots and logs, functional checks, and the one audit.
`audit-states.json` uses real inputs for the picked card, kid view, lower height limit, check rows, ready opening, and reset.
The report is the final record of audit leads and any remaining limits. The full audit is not rerun after targeted repairs.

The single mechanical audit reached its 40-minute cap without writing audit.md. It left 67 frames, all inspected.
Its completed state images are evidence, but its full repeated-input and resize suite is not certified complete.
Afterward, targeted checks passed for 60 px pedestal controls, the longest selected name, alternative-home notes,
keyboard return focus, the upper limit, ribbon interruption, Kid eyes dragging, and the oversized robot's case.
A separate real-input CDP check resized during the ribbon, height movement, and kid fade with no exceptions.
The final support-alignment change was re-shot at 680, 760, and 1366. The upper-limit audit state was added for
the next reviewer, and the lower-limit phone-size filter corrected, after the timed audit; those edits were not re-audited.
Final reset checks confirmed that Keep it preserves the work, Yes clears picks and bays, the role prompt resets,
and Put back removes only its piece and bay. The shipped bundle is 1,029,267 bytes with 48 browser-narration lines.
All launched Chrome and host processes were closed; ports 9970, 9971, and 8775 were confirmed no longer listening.

The functional matrix covered all 60 piece/home pairs, band boundaries, fractional case centers, swaps, the window reset,
height clamping, and argued themes. Separate input runs covered real dragging, keyboard height movement, all eight role
prompts, a sixth pick, theme changes, and two earned ribbon speech events. Frames cover every required size and all modes.

## Spec questions and implementation choices

The spec lists no open questions. No subject matter, modes, or export/save features were added.
The favorable Stand options for the two clay pieces are accepted with their safety note, following the explicit piece table.
On the first successful check the ribbon appears directly over the wall. A subsequent unchanged check opens the fifteen
badge rows, so the success moment is visible instead of being covered immediately by a dialog.

## Engine changes wanted

None. No kit, engine, shared script, documentation, or other tool was edited.

## Next review

Use the cold review in a separate chat. Check browser narration by listening on the intended classroom device, and
assess the small-art minimum sizing and classroom pacing with a real K-2 group. No polish round was started here.

## Cold review repairs, 2026-11-04

The cold reviewer played the full student path before reading this handoff. Source changes keep the cart, original
collection, hallway, Kid eyes reveal, support art, and check rules. The pointer prop was redrawn with a slender
shaft and modest grip; its full prompt and cutout settings are in art/prompts.json, using the built-in image tool.

Set up now uses CSS grid so DOM order is tray, bays, homes, height controls, then the bar. The worktop contains
only the wall. Mode switching returns the wall to that worktop. Reopened cards always show a next action, Read
uses individual registered lines, and the fifth-pick event waits until the look-closer card closes. Five picks
keep the Set up instruction when returning to Choose or cancelling Start over. Limits name the enabled arrow.
Each native dialog has its own Read control because the header is inert while a dialog is open. Card and check
Read use individual registered narration parts. Boundary arrows transfer keyboard focus to the enabled direction.

Low pedestal warnings name Tall or Middle. Opening day names the glowing artwork, responds visibly to Next piece,
and supplies a useful action instead of an art-looking prompt when its bay is empty. The existing eight prompts
remain unchanged for occupied bays. The role label is informational; the class still supplies every explanation.

Review evidence lives in Scratch: cold-frames, review-sizes, review-special, review-voice, mechanics-final.json,
numbers-review.json, and review-audit. The final audit result is recorded in codex-review.md. Recordings remain
absent under the no-recording rule. No shared kit edits or git commits were made.
The 63-line inventory matches allLines(). Held-click counts: reason guidance 1/1, repeated piece descriptions 5/5,
repeated role events 5/5, re-earned ribbon events 2/2, fifth-pick event 1/1. Read works during speech and with Sound
off. The keyboard-only path chose five pieces, placed and framed one, changed height, checked, and returned focus.

The review audit hit its 40-minute limit with 77 frames and 71 aggregate leads. Its stress suite did not finish.
The partial report's clean stress rows do not establish coverage. All saved frames were inspected. Confirmed
repairs: compact ruler callouts/ticks no longer collide; tick marks remain, with only colliding numbers suppressed.
The ribbon is click-through, clears the ruler, and stays above the art in compact views. The checklist header
stays visible while scrolling. The child-eye estimate note stays visible on phones. Active-mode re-entry leaves
its current welcome running. Reset opening/dismissal hushes obsolete speech. Empty-gallery guidance is a how-to
spoken once; moving between an empty and occupied bay stops stale guidance and restores the relevant prompt.
Removed the global #hint keep-region because native dialogs intentionally cover that underlying hint.

Remaining audit leads were expected pointer-transparent/behind-dialog hit-test results and first-tap welcome
suppression required by STANDARDS. The two real rapid-mode welcome cuts were fixed and directly re-tested.
Post-audit evidence is in post-audit-frames/ and its JSON results. Nine direct resizes during the ribbon, height
motion, and Kid eyes fade passed without runtime errors; resize-recheck.json records their scope. This targeted
check is not a completion or rerun of the full stress audit. All review Chrome and host processes were closed.

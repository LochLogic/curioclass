# Shadow Measure build handoff

## Structure
src.html starts from the kit starter, uses the kit frame and 9-12 theme, and owns the pixel-sized canvas simulation, persistent HTML controls and session notebook. The script separates geometry, transitions, voice, painting and pointer input. __tool exposes the required state and methods plus setup helpers and narration logs.

## Tricky parts
All tapes round to 0.01 m before calculating. Percent error uses the full recorded ratio. Images are cut out by scripts/art.py --rekey only. Each cutout's normalized measured point is listed in art/prompts.json. Scratch landmarks.py derives landmarks.json, which src.html loads with a bundler token. A hoop's base is the vertical ground projection of its rim, not its offset support post. The tripod base means the projection under the eyepiece.

Sun shadow footprints preserve the cutout alpha silhouette, flattened across the measuring strip. Their longitudinal coordinate is projected from image height, so a top's shadow lands at the exact physical endpoint. The hoop backboard casts past the rim's chalk tick. The wall's broad painted facade continues off the left of the view so the measured right edge and reflection path remain central.

## Decisions and conflicts
- No open questions are listed in the spec.
- The user and CODEX-BUILD require the built-in image tool. They override the spec's local FLUX and white-background requests. All nine cutouts use flat keyed backgrounds, with magenta for the tree. No people appear.
- The spec stacks the panel below the scene under 1000 px. STANDARDS wins in short landscape boxes: below 900 px tall, keep them side by side when at least 600 px wide. Phones and the tall 760 px view stack.
- CODEX-BUILD says to start the report as soon as the first bundle works, then stop when it is written. An in-progress report is created at first bundle; the final report is completed after the mandated checks, then the run stops.
- The two reference tools were copied and bundled in Scratch because bundling them in their own directories would violate the user's write boundary.
- A reason-card pair is evaluated together. On failure both choices and tape readings clear, and the refused notebook row stays unfinished. Remeasure before another attempt to prevent free option enumeration. There are no scores or rewards to farm.
- A fabricated pair of very short readings can accidentally produce the correct ratio. Percent error still reports the mathematical result, but close praise requires both endpoints to be within max(0.06 m, 3 percent of the real span). Otherwise feedback asks for a fresh measurement. This implements the user's explicit request to close passing cheats without hiding honest numerical error.
- Dilation controls sit over the stage to preserve the notebook's working space in compact views. Bars have wide/thin labels and an upward marker when an estimate exceeds the view.
- The 3.05 m hoop model is the spec's rounded version of exactly 3.048 m for ten feet.
- The opening premise hides real height until Reveal, while the required Hoop setup line explicitly publishes 3.05 m. The specific required hoop rule line wins; other real heights stay unknown until Reveal.

## Sensitivity
No people, bodies, culture, religion or hard history. The schoolyard is invented.

## Engine changes wanted
None. No shared kit edits.

## Art still to paint
None. Eleven images generated during Build, with full prompts and raw originals in art/raw.

## Next
The separate cold review is recorded in codex-review.md. No git commits were made.

## Cold review changes
- Fixed Streetlight's welcome to name Measure before asking for tape movement.
- Split Mirror's crosshair narration by step, stopped setup speech on Measure, and restored the once-only tape how-to on entry.
- Put all fixed Read hints into the voice inventory, now 25 strings. No audio was recorded.
- Separated setup welcomes from tape instructions, so entering Measure or enabling Sound there never names the hidden setup button.
- Made the dilation sample point keyboard accessible with visible focus, arrow keys and Home. Its position survives resize.
- Blocked the confirmed k=0.21 shortcut by showing numeric scale only after Reveal. The spec's hidden-height premise wins over an unspecified readout timing; the full dilation layer remains usable before Reveal.
- Added post-Reveal dotted gaps from the student's tape ends to their physical targets. These introduce no pre-Reveal correctness clue.
- Redrew the clipped basketball hoop in the same painted style, recalibrated its rim, and rekeyed five other cutouts with edge despill.
- Added cold-review extremes and failed-trial audit fixtures. Source facts and independent calculations are in the cold review evidence.

## Cold review verification
The single review audit completed with 36 leads. Twelve are hidden header words replaced by accessible 17 px glyphs;
fourteen are expected overlays on the focusable canvas or their text containers; three are first-tap welcome skips;
five are current-step or unmoved-handle clicks; two are the failed phone audit host. Repeated taps, Motion off and
resize stress reported no exceptions or stuck controls. All 71 audit frames were inspected.

The phone audit host was affected by surviving test-server children from the LibreOffice Python launcher. Independent
375 px drive.py iframe runs verified setup, measuring, refusal and Reveal, including the final dilation and tape-gap
repairs. The three exact owned server processes were identified by command line and closed. All assigned ports are
closed, and host.html is absent. Scratch now has an in-process bounded runner and server lifecycle.

After the audit, the final instruction correction was rechecked with the complete main voice walk, repeat-event
counts, phone frames and Sound-on-during-Measure. Leaving the crosshair also hushes its now-stale event. Voice
inventory and allLines match all 25 strings. The review audit is not claimed to cover those later narrow voice changes.
The audit fixture's phone size keys now use the auditor's exact 375x812 label for future runs.

## Audit snapshot and repairs
The single complete audit is in _scratch/shadow-measure/audit/audit.md. It has 41 leads and 67 frames. Its original state drags omitted the outer return required by the audit's step wrapper, so its Why, Reveal and populated-notebook state replays did not reach those states. The corrected audit-states.json is ready for the cold reviewer. Separate real-input replays validate the repaired states without rerunning the full audit.

Audited layout repairs use two compact setup columns, two measurement readouts side by side in short notebook panels, extra clearance below the night tapes, and a right-aligned dilation control with a shorter readout. A rapid New trial tap on an untouched setup preserves the still-valid welcome instead of cutting it. The full audit predates these focused repairs; the build report identifies the follow-up evidence.

The 15 zero-font leads are the intentionally hidden words behind visible 17 px header glyphs, each with a 44 px target and an accessible name. Selecting the current Set up tab is a no-op. Clicking a drag handle without moving it is also a no-op; real drags and arrow keys are tested separately. A first action that speaks its own instruction skips the welcome, as STANDARDS requires.

## Verification left open
Twenty-five corrected real-input replays passed, including Why and Reveal at all eight required sizes, populated notebooks at three sizes, and the repaired near-mirror and dilation layouts. Later Chrome CDP connections closed before further checks, including with the standard drive.py runner. Do not describe the final full audit as clean.

Recheck the final 680x425 Sun, Hoop, Mirror and Streetlight setup layouts; the shortened refusal feedback at 680 and 375 wide; the rapid New trial welcome repair; and the hint when returning to an already-proved Why step. These repairs are implemented and the final bundled scripts pass Node syntax checking, but their last browser retests did not run. Full main paths and keyboard-only Sun passed before these focused changes.
The final anti-cheat presentation also marks mismatched-endpoint notebook rows "remeasure" and withholds the positive headline. The earlier fabricated-ratio test passed the numerical and narration guard; these added labels need the next browser check too.

All assigned ports are closed, no owned Chrome remained in the final process inventory, and host.html was removed. No recordings, git commits or polish round were made.

# Codex report: which-way-is-down

## Built

Build only. Four schoolyards, three objects, arrow recording, the X-ray reveal, argument/evidence checking,
one-attempt predictions, and Earth/Moon/Mars drops. The tool is one offline file using the shared kit.
Source, draft metadata, notes, voice manifest, art, audit states and handoff are in this tool folder.
No commits, deployment, paid image service, recordings or polish round. All scratch evidence is in
`_scratch/which-way-is-down/`. The final report is written last because the owner required work to stop upon its creation.

## Numbers check

`recomputed.json`, `prepare.py` and `plan_checks.py` preserve calculations.
From 1.5 m, sqrt(2h/g) gives Earth 0.553001 s, Moon 1.360828 s, Mars 0.899236 s.
The rounded table is 9.8/1.6/3.7; physics uses 9.81/1.62/3.71. Slow motion integrates elapsed time divided by ten.
Measured browser landings: 584 ms and 5,541 ms; a restarted world drop has elapsed time zero.
School true arrows: 298.8, 179.8, 33.9 and 116.6 degrees. Untouched errors: 28.8, 90.2, 123.9 and 153.4 degrees.
Anchorage's supplied view longitude and the parenthetical side signs conflict with the specified sides; the implementation uses the computed view.
South Pole gaps are 14.4, 45.1, 61.95 and 76.7 degrees. Sydney displays 62.0 rather than the spec's 61.9.
Cairo permits 17 integer settings inside the inclusive tolerance; the other seven test places permit 16.
Claim lengths are not all within the spec's stated range; their exact text is preserved with equal-sized, shuffled cards.
Contrast: ink/paper 13.78:1, muted/paper 5.50:1, white/copper 5.71:1, copper/paper 5.07:1,
gold/space 12.56:1, miss/space 7.80:1, light text/space 15.52:1.

## Facts checked

- Down toward the spherical Earth's center: [NGSS 5-PS2-1](https://www.nextgenscience.org/pe/5-ps2-1-motion-and-stability-forces-and-interactions).
- Mean Earth radius and Mars gravity: [NASA/JPL physical parameters](https://ssd.jpl.nasa.gov/planets/phys_par.html).
- Moon gravity: [NASA Moon fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html).
- Rounded Earth/Moon/Mars table: [NASA planetary fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/).
- Feather and heavy object fall together without air resistance: [NASA Apollo 15 demonstration](https://science.nasa.gov/resource/the-apollo-15-hammer-feather-drop/).
- Plumb lines and the real vertical: [NOAA NGS](https://www.ngs.noaa.gov/GEOID/GSVS/deflection-vertical.shtml).
  Notes distinguish the ideal sphere from flattening, rotation and local deflections.
- Esperanza has a school and families: [official school registry](https://mapa.educacion.gob.ar/legajo/940011700)
  and [Argentina government](https://www.argentina.gob.ar/node/460649). No territorial claim is made.
- School-town and test-place coordinates: transcribed from the spec's GeoNames/Wikipedia values and checked in the projection/math.
  Per-city source pages were not independently reopened. Children and yards are explicitly illustrative, not actual pupil portraits or school-site surveys.
- Claims B, C and D are hypotheses to reject, not factual assertions. Their angular consequences are checked against recorded evidence.

## Break it

- Record: untouched arrows miss at all four places. Real handle drags hit all four. A miss gives a scaffold and grants no record.
- Pointer shortcut: center-click aiming initially worked. Fixed by requiring a drag to start within the 48 px handle target.
  Final real-input proof: a center tap leaves 270 degrees and misses; a handle drag hits.
- Claim elimination: all four choices tested. Only A fits all attached places. Elimination alone never earns Strong.
- Evidence: only place records count. Feather tube and Other worlds concern speed and never replace the third place.
- Predictions: untouched arrows miss at all eight pool places. Repeated Predict taps cannot add a second attempt.
  Three real aimed hits earned Strong; the badge stays unavailable during the pending result sequence.
- Mode-switch skipping: an unfinished test resumes at the same place and angle. Twelve switches preserve the same index and cannot earn Strong.
- Reasoning: punctuation-only input now counts as zero words. Eight filler words remain a teacher-review issue, as the spec explicitly requires.
- Changing evidence clears Fits and the streak. Historical saved rows cannot restore a streak or a saved Strong badge.
- Reset: clears records, reasoning, tests, X-ray and reveal state, while retaining Globe kids.
- Test artifacts: `functional/results.json`, `voice-walk/results.json`, the focused `*-proof.json` files and `handle-frames/`.
  The first functional run exposed the Esperanza handle clipping; its downstream Zoom failures were consequences of that defect.
  The voice run's world-restart assertion sampled after its deliberate two-second pause; the immediate timing proof passes.

## Voice walk

The main run used held 120 ms clicks at a two-second pace, with the actual queue log in `voice-walk/voice-log.json`.
Heard: fellA, hMark, recOk, fellQ, recMiss, fellS, recMiss, fellE, recMiss, rv1, rv2, rv3,
wArgue, hCheck, noFit, fits, hTest, miss, hit, hit, hit, strong, wWorlds, worlds, hMarkBtn.
The reveal's three lines start in the required order. Tests wait for the whole result before Next place.
The side path uses Feather tube, two misses and Read. Both miss events start; Read speaks the current measured-error hint.
Record feedback now starts immediately, preventing it from waiting behind an obsolete how-to line.
PARTIAL: hNext and hZoom were dropped by subsequent actions before starting in the rapid browser-speech run.
Their current instructions remain in the hint and Read. This is an explicit review item, not a clean voice claim.
The Anchorage welcome is now valid only at Anchorage; Sound toggling at Quito cannot announce Anchorage.
No recordings were made. The 27-line upbeat-guide manifest is ready for the separate recording workflow.

## Feel check

Best moment: the four colored lines stretch through Earth and converge on the glowing center, with Ruby standing correctly on her upside-down edge.
The student earns a specific argument card, with their evidence, reasoning and tested predictions.
Flattest moment 1 was an apple floating below the hand. The art placement now follows each child's actual cutout proportions.
Flattest moment 2 was a miss that felt stuck because a handle was clipped or covered. The handle is now reachable;
the yard turns onto the tangent, while predictions play out along the true plumb line.
The reveal turns the view, fades to X-ray and extends each line. Motion off preserves drop timing without moving the objects.
Both bar tools were bundled into Scratch and opened. `feel-comparison.jpg` places the reveal beside Snowy Mail Route.
The tool has richer painted setting and a clear visual payoff; later play changes from observing to recording, arguing and unaided predicting.

## Done when

1. PASS, with final focused layout proofs: yard is the main Drop scene; Mark/Test foreground the globe and arrow. Laptop controls fit; compact hints remain visible.
2. PASS: four real drops, plumb trails and right-angle marks. Measured normal/slow timings are above.
3. PASS: all four untouched misses and corrected real drags, including Esperanza at 680x425.
4. PASS for ordered reveal and tap cancellation; full voice log and final skip proof. The final turn/fade preserves the same sequence.
5. PASS for radial line convergence in spun X-ray views and added-kid lines. Rotation uses yaw/pitch; free roll is not implemented.
6. PASS with the documented Sydney rounding difference: A fits, B/C/D miss with computed degree gaps.
7. PASS: one attempt, unchanged-arrow misses, real aimed hits, result wait and earned Strong.
8. PASS: restart paths and elapsed-time integration; immediate world restart proof passes. Speed changes apply continuously.
9. PASS: Earth/Mars/Moon landing order and 0.55/0.90/1.36 readouts; viewing speed does not alter the displayed real time.
10. FAIL (partial): repeated results and Read work; rapid speech can lose hNext/hZoom. Result lines name Next while it waits
    for speech to end, following Heard in order rather than the conflicting no-disabled-control rule. See Voice walk.
11. PASS for the assessed direction skill: repeated clicks alone cannot earn Strong, and evidence is derived from the notebook records.

## Wave lessons

- FAIL (partial), Hint and voice: hints update synchronously and name current controls; Read verified. Voice pacing remains PARTIAL as stated above.
- PASS, Focus and layout: stable controls are retained; Mark and Test move focus to the canvas with preventScroll. Back restores Drop focus.
- PASS, Sizes: all standard desktop sizes captured; narrow iframe and final focused checks are listed below. Mode tabs have at least 44 px width.
- PASS, Targets: the visible checkbox is 23 px, inside a clickable full-width 44 px label row. Audit counts the native square, not the full target.
- PASS, No giveaways: equal claim cards, shuffled order, no live angle verdict, no kid or center dot in Test. Center-click aiming was closed.
- PASS, Honest numbers: rounded gravity, real-time readouts, model assumptions and the 8-degree tolerance are explicit.
- PASS, Standards: solo students record, compare claims and predict unfamiliar directions for 5-PS2-1. No family engine is specified.
- PASS, Motion off: no CSS loops; the bob/twinkle stop and landing timing stays the same.
- PASS, Short choices: all claim and place choices remain visible. Notebook/Start over may fold below in short boxes, as permitted.
- PASS, Resize during animation: the actual fall finished after a mid-fall resize with no exception.
- PASS, Welcome: no welcomeAfter; first-action cuts follow BASELINE 16. The place-specific welcome now has a matching validity guard.
- PASS, Unknown states: unrecorded places and unattempted predictions remain explicitly unknown.
- PASS, One meaning per style: solid colored evidence, dashed white claim, named Hit/Miss with degree gaps.
- PASS, Honest badges: Strong requires all four gates and waits for the result; changing evidence invalidates it.
- PASS, Reversible hints: returning modes sets the hint immediately; a paused test resumes with its test instruction.
- PASS, No copying words: claim elimination is permitted, but independent spatial predictions remain required.

## Audit leads

Completed once within the 40-minute limit: 188 mechanical leads. The 233-entry ledger covers every printed
lead/control row, including repeat/quick-tap pass rows; no entry remains unclassified. No full audit rerun was made.

Every lead is listed with its disposition in `audit-lead-ledger.md` in Scratch.
The full audit froze its own HTML. Subsequent focused fixes are documented in handoff.md and verified separately;
the audit is a snapshot, not final certification. Its first drag fixture returned no points, so evidence/test states were not reached.
The checked-in fixture is repaired. Separate real-input runs reached all four records and Strong.
Canvas/HTML overlays and modal coverage are intentional. The notebook fold is permitted. Actual target, focus, naming and layout defects were fixed.
The audit's missing-premise welcome lead is superseded by BASELINE 16; the premise remains in the hint and Read.

## Frames looked at

Default, all modes, four records, wrong claim, reveal, Strong, three-world landings, compact Mark/Argue, keyboard,
grayscale, Motion off, overlay, all standard sizes and 375-wide iframe views. Art and people contact sheets inspected.
Audit frames were inspected in numbered contact sheets, with suspected layout defects opened separately at native size.
63 audit frames and 52 other frames inspected in audit-contact-1 through 8 and extra-contact-1 through 7,
plus native-size views. Final phone Globe/Test/landed and final reveal sequence checks pass.
Earlier 404 fixture images remain as failed-test evidence; the corrected final host checks have no console errors.

## Art made

22 images, 1,435,494 bytes (1,401.8 KiB). Recorded voice: 0 KB. Final bundle: 2,064,316 bytes
(2,015.9 KiB), approximately the 2 MB goal. validation-manifest.json records the final source/bundle hashes
and passing static checks. cleanup.json confirms no listeners remain on the assigned host/Chrome ports.

The built-in image tool made all art during this build. Prompts and provenance are in art/prompts.json; finished WebPs are in art/.
Redrawn/edited: four empty space/ground assets that initially included people, Sofia's rejected point pose, Quito's skyline and the feather tube.
The final Quito edit passed the fresh agent's follow-up review. Minor outfit/accessory continuity differences remain in two pose pairs.

## Art still to paint

None. All 22 final assets are present, including eight people poses. The owner people contact sheet is in Scratch for pre-ship review.

## Engine changes wanted

None. Shared kit, docs and scripts were not edited.

## Left open

- Rapid browser-speech how-to ordering for hNext/hZoom needs the cold voice review; fixed recordings are absent by build instruction.
- Saved test rows are historical on reload; Strong is not restored. Free-roll globe rotation is not implemented.
- Full audit limitations and post-snapshot fixes are explicit above. Per-city coordinate source pages were not independently reopened.
- Minor Jonah/Valentina accessory continuity differences remain; representation and anatomy passed fresh review.

# Which Way Is Down?: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: which-way-is-down

#### Built

Build only. Four schoolyards, three objects, arrow recording, the X-ray reveal, argument/evidence checking,
one-attempt predictions, and Earth/Moon/Mars drops. The tool is one offline file using the shared kit.
Source, draft metadata, notes, voice manifest, art, audit states and handoff are in this tool folder.
No commits, deployment, paid image service, recordings or polish round. All scratch evidence is in
`_scratch/which-way-is-down/`. The final report is written last because the owner required work to stop upon its creation.

#### Numbers check

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

#### Facts checked

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

#### Break it

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

#### Voice walk

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

#### Feel check

Best moment: the four colored lines stretch through Earth and converge on the glowing center, with Ruby standing correctly on her upside-down edge.
The student earns a specific argument card, with their evidence, reasoning and tested predictions.
Flattest moment 1 was an apple floating below the hand. The art placement now follows each child's actual cutout proportions.
Flattest moment 2 was a miss that felt stuck because a handle was clipped or covered. The handle is now reachable;
the yard turns onto the tangent, while predictions play out along the true plumb line.
The reveal turns the view, fades to X-ray and extends each line. Motion off preserves drop timing without moving the objects.
Both bar tools were bundled into Scratch and opened. `feel-comparison.jpg` places the reveal beside Snowy Mail Route.
The tool has richer painted setting and a clear visual payoff; later play changes from observing to recording, arguing and unaided predicting.

#### Done when

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

#### Wave lessons

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

#### Audit leads

Completed once within the 40-minute limit: 188 mechanical leads. The 233-entry ledger covers every printed
lead/control row, including repeat/quick-tap pass rows; no entry remains unclassified. No full audit rerun was made.

Every lead is listed with its disposition in `audit-lead-ledger.md` in Scratch.
The full audit froze its own HTML. Subsequent focused fixes are documented in handoff.md and verified separately;
the audit is a snapshot, not final certification. Its first drag fixture returned no points, so evidence/test states were not reached.
The checked-in fixture is repaired. Separate real-input runs reached all four records and Strong.
Canvas/HTML overlays and modal coverage are intentional. The notebook fold is permitted. Actual target, focus, naming and layout defects were fixed.
The audit's missing-premise welcome lead is superseded by BASELINE 16; the premise remains in the hint and Read.

#### Frames looked at

Default, all modes, four records, wrong claim, reveal, Strong, three-world landings, compact Mark/Argue, keyboard,
grayscale, Motion off, overlay, all standard sizes and 375-wide iframe views. Art and people contact sheets inspected.
Audit frames were inspected in numbered contact sheets, with suspected layout defects opened separately at native size.
63 audit frames and 52 other frames inspected in audit-contact-1 through 8 and extra-contact-1 through 7,
plus native-size views. Final phone Globe/Test/landed and final reveal sequence checks pass.
Earlier 404 fixture images remain as failed-test evidence; the corrected final host checks have no console errors.

#### Art made

22 images, 1,435,494 bytes (1,401.8 KiB). Recorded voice: 0 KB. Final bundle: 2,064,316 bytes
(2,015.9 KiB), approximately the 2 MB goal. validation-manifest.json records the final source/bundle hashes
and passing static checks. cleanup.json confirms no listeners remain on the assigned host/Chrome ports.

The built-in image tool made all art during this build. Prompts and provenance are in art/prompts.json; finished WebPs are in art/.
Redrawn/edited: four empty space/ground assets that initially included people, Sofia's rejected point pose, Quito's skyline and the feather tube.
The final Quito edit passed the fresh agent's follow-up review. Minor outfit/accessory continuity differences remain in two pose pairs.

#### Art still to paint

None. All 22 final assets are present, including eight people poses. The owner people contact sheet is in Scratch for pre-ship review.

#### Engine changes wanted

None. Shared kit, docs and scripts were not edited.

#### Left open

- Rapid browser-speech how-to ordering for hNext/hZoom needs the cold voice review; fixed recordings are absent by build instruction.
- Saved test rows are historical on reload; Strong is not restored. Free-roll globe rotation is not implemented.
- Full audit limitations and post-snapshot fixes are explicit above. Per-city coordinate source pages were not independently reopened.
- Minor Jonah/Valentina accessory continuity differences remain; representation and anatomy passed fresh review.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: which-way-is-down

#### Played

Cold Grade 5 solo play, before the builder's report, handoff, notes or source: four records, reveal, argument, prediction miss and Other worlds. Then a teacher/projector voice walk and focused repair checks. The schoolyards and the converging-arrow reveal are strong; retained their detail and character.

#### Findings fixed

- **blocker, general, Argue voice:** three hits announced a strong argument with zero reasoning words. Confirmed in `review-probe/hit-no-reason-2.json`. Speech now obeys the reasoning gate, completing reasoning afterward can announce the newly earned result, and removing words reverses the hint/status and interrupts a stale Strong announcement.
- **should fix, general, Argue entry:** four available records still produced "Record at least three places" because attached cards were counted. Entry now checks available records and names the usable next action. Unavailable-card prompts speak once per Argue entry, not on every tap; the discussion prompt no longer assumes a pupil made a miss.
- **should fix, general, voice:** Zoom out skipped the Globe how-to; long confirmations lost navigation cues at a two-second pace. Shortened the first landing and Record confirmation, synchronized Zoom before its visibility check, and queued the Globe cue after the reveal.
- **should fix, general, predictions:** results named Next place while it was disabled. Result and next-action speech are now separate; Next is named only once enabled. Predict also preserves a useful keyboard focus path. Obsolete claim/evidence headings hide during predictions.
- **should fix, general, keyboard/access:** Go to Drop hid the focused control; it now focuses Drop with preventScroll. Passive pictures use image semantics and leave the tab order; interactive globe/arrow views keep their keyboard surface.
- **should fix, general, vacuum demonstration:** the sealed tube fell with its contents fixed inside. Its shell now stays still while the painted feather and apple fall together inside it.
- **should fix, general, narrow Argue:** six evidence choices pushed the hint below the phone frame. Compact claims and a three-column evidence grid keep every choice, Check/Test and the complete hint visible at 375x812 and 680x425.
- **should fix, general, phone yard:** the school badge covered the child's face. It now occupies clear upper-right sky. The white ruler also gained a dark backing so Antarctic snow cannot hide it. Landed-state bubbles were moved into clear margins after the audit frame exposed a face overlap at 1000x625; rechecked at 1000, 680 and 375 widths.
- **should fix, general, Motion off/reveal:** canvas arrows still grew in calm mode despite the default CSS audit being clean. They now hold still through each 800 ms beat and extend at its end. Rendered pixels remain identical during an active calm reveal.
- **polish, general, Other worlds:** lifted the flattest scene with shaded lane frames, height ticks, contact shadows and brief landing rings; retained the painted surfaces, planets and timing.
- **polish, general, art/facts:** redrew the weakest cutout, the feather tube; qualified 6,371 km as this model's radius; added individually checked geography sources to notes. Updated voice, audit states and handoff.

#### Findings left

- **nit, general, people art:** small backpack/hat/accessory continuity differences remain between a few holding and pointing poses; anatomy, weather clothing and the overall illustration style are sound.
- All blocker/should-fix findings identified in this pass are repaired. The narrow argument paper deliberately scrolls for reasoning/history; the main action choices remain visible. Audit coverage limitations and spec boundaries are explicit below.

#### Break it

- **Record:** untouched arrows missed all four schools, by 28.8, 90.2, 123.9 and 153.4 degrees. Repeated Record cannot rotate an arrow. A miss supplies the specified teaching scaffold; recording is evidence collection, not independent proof. Real, whole-pixel handle drags hit.
- **Claim check:** tried every claim; only A fitted. Elimination unlocks testing but never earns Strong. Two place cards plus both speed cards left Check disabled. Only three actual place records satisfy the evidence gate.
- **Predictions:** tried unchanged arrows at all eight pool places on both alternating sides, repeated Predict taps and a center tap. All unchanged guesses missed; a center tap left 270 degrees; repeated taps spent exactly one attempt. Switching modes retained the unspent place and index.
- **Strong/reasoning:** three hits with zero words and punctuation stayed below Strong and no longer spoke Strong. Eight filler words can satisfy the explicit word-count gate only after the independent direction hits; scientific reasoning remains teacher-read, as the spec requires. A subsequent miss removed Strong. Native keyboard deletion of earned reasoning cleared both status and hint; deleting again during the award voice cut that obsolete announcement.
- **Reset/storage:** Clear erased records, reasoning and tests. Reloaded test rows remain historical; no saved score restores a streak. No extra award, best score or hidden percentage was added.
- **Timing:** restarted Drop all returned elapsed time to zero; Earth/Mars/Moon landed in that order. Slow-to-normal changed the integrated speed immediately. Motion off preserved the Earth landing time, measured at 574.9 ms, rather than skipping time.
- Proofs: `review-break-results.json`, `review-side-results.json`, `review-main-voice/`, all under `_scratch/which-way-is-down/`.

#### Voice walk

Sound on, default settings, held 120 ms clicks at a two-second pace: Drop/Mark/Record at all four schools, Zoom out through the whole reveal, Argue/claim/three place cards/reasoning/Check/Test, three aimed predictions, then Other worlds/Drop all.
Actually started, in order: fellA, hMarkBtn, hMark, recOk, fellQ, recOk, hNext, fellS, recOk, fellE, recOk, hZoom, rv1, rv2, rv3, wGlobe, wArgue, hCheck, fits, hTest, hit, nextReady, hit, nextReady, hit, strong, nextReady, wWorlds, worlds.
The first Drop tap legitimately skips the Anchorage welcome under BASELINE 16; its instruction remains in the hint and Read. Actions can cut speech whose moment they leave. No stale instruction played over a different mode.

| Line(s) | Kind | Expected | Actually started |
|---|---|---|---|
| hMarkBtn, hMark, hNext, hZoom, wGlobe, wArgue, hCheck, hTest, wWorlds | how | once each on main path | once each |
| recOk, recMiss | event, five repeated submissions | five each | five each |
| hMark, hNext | how, repeat side path | once each | once each |
| hit, strong | event, three successful main tests | three, one | three, one |

Read interrupted speech, worked with Sound off and released promptly on a mode change. All 28 manifest lines match `allLines()`. The post-audit empty-record side path spoke once for five taps, then once more on re-entry. No recordings were made: the build brief forbids recording; these checks used browser fallback. Logs: `review-evidence-summary.json` and `review-side/`.

#### Facts checked

- **Earth's down points toward the spherical center; support an argument with evidence:** [NGSS 5-PS2-1](https://www.nextgenscience.org/pe/5-ps2-1-motion-and-stability-forces-and-interactions). The student records, compares a claim and tests new directions; the standard is practiced, not merely named.
- **Plumb lines follow local gravity; real Earth departs from an ideal sphere:** [NOAA NGS vertical deflection](https://www.ngs.noaa.gov/GEOID/GSVS/deflection-vertical.shtml). Notes distinguish flattening, rotation and local deflections; the diagram is explicitly a model.
- **Mean radius 6,371 km:** [NASA Earth fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/earthfact.html). Changed the screen's exact "below every school" claim to "in this model".
- **Rounded gravity 9.8, 1.6, 3.7 meters per second each second:** [NASA planetary fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/), [Moon](https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html), [JPL parameters](https://ssd.jpl.nasa.gov/planets/phys_par.html). Physics uses 9.81/1.62/3.71; Moon/Earth 0.165 and Mars/Earth 0.378 round to 0.17 and 0.38.
- **1.5 m drops:** independently recomputed sqrt(2h/g): 0.553001, 1.360828 and 0.899236 seconds, hence Earth 0.55, Moon 1.36, Mars 0.90. Constant gravity/no air resistance is stated; numeric proof is `review-numbers.json`.
- **Feather and heavier object fall together without air resistance:** [NASA Apollo 15 hammer-feather demonstration](https://nssdc.gsfc.nasa.gov/planetary/lunar/apollo_15_feather_drop.html). Repaired the picture so it demonstrates the intended result.
- **Esperanza has families and Escuela Provincial 38:** [Argentina government family arrival](https://www.argentina.gob.ar/node/460649); **63.4 S, approximately 57.0 W:** [official base description](https://www.argentina.gob.ar/node/82609). No claim of Antarctic territorial ownership or "only school" is made.
- **School-town locations/latitude notes:** [Anchorage](https://www.geonames.org/5879400/anchorage.html), [Quito](https://www.geonames.org/3652462/quito.html), [Sydney](https://www.geonames.org/2147714/sydney.html), plus the official Esperanza source above. Notes distinguish city/base points and fictional illustrated pupils from verified school-site surveys.
- **Test coordinates:** checked [Tokyo](https://www.geonames.org/1850147/tokyo.html), [Cairo](https://www.geonames.org/360630/cairo.html), [Oslo](https://www.geonames.org/3143244/oslo.html), [Honolulu](https://www.geonames.org/5856195/honolulu.html), [Nairobi](https://www.geonames.org/184745/nairobi.html), [Cape Town](https://www.geonames.org/3369157/cape-town.html), [Ushuaia](https://www.geonames.org/3833367/ushuaia.html), [Buenos Aires](https://www.geonames.org/3435910/buenos-aires.html). Cairo/Oslo reference points differ within about 0.1 degree from the spec; documented rather than falsely claiming identical rounding.
- **Direction calculations:** recomputed school arrows 298.8/179.8/33.9/116.6; South-Pole gaps 14.4/45.1/61.95/76.7; parallel-axis gaps 28.8/90.2/123.9/153.4. Sydney correctly displays 62.0. Integer hit windows contain 16 settings except Cairo's 17; no probability claim is shown to students.

#### Sensitivity

The four fictional children and illustrated Alaska/Ecuador/Australia/Antarctica settings need the fresh sensitivity lens for representation and the small pose continuity differences. None is assigned an Indigenous identity from appearance. A child is an individual, not a stand-in for an entire population. Esperanza is named as an Argentine research base without a territorial claim. All eight people assets are marked `people: true`; no frightening, mocking or stereotyped depiction was found in this pass.

#### Flattest moment left

After its first informative comparison, repeating Other worlds has limited depth. The new landing treatment improves that payoff; the four-location evidence sequence and the later unaided predictions remain the session's progression. No new topic or game was added.

#### Graphics

Checked all 22 assets, every yard at final laptop size, the eight people poses, the space/ground/world art and the repaired tube in laptop, preview and phone scenes. One built-in OpenAI image redraw; final `art/wwd-feather-tube.webp`, exact prompt in `art/prompts.json`, source in `art/raw/wwd-feather-tube.png`, processed with `art.py --rekey`.
Other worlds and the globe retain the original painted texture and precise code geometry. Motion off stops new landing rings and existing bob/star motion. Grayscale retains named places, solid/dashed meanings, Hit/Miss text and measured gaps.
Compared with existing Snowy Mail Route and Beat Lab frames; retained this tool's richer painted field-trip identity. Art: 1,441,494 bytes; bundle: 2,077,358 bytes (about 2,028.7 KiB), below 2 MiB. Static checks and contrast: ink/paper 13.78:1, muted/paper 5.50:1, white/copper 5.71:1, gold/space 12.56:1, miss/space 7.80:1.

#### Audit

Completed once within the 40-minute limit, Chrome 9941 and host 8745: 195 mechanical leads; all 237 printed lead/control rows classified in `review-audit-ledger.md` and `.json`. No unclassified row remains. Resize stress reported no exceptions or controls left disabled; repeat and quick-tap sections were clean.
Reviewed all 67 audit frames in 12 contact sheets and opened affected frames at native size. Intentional canvas/HTML layering, 23 px checkbox squares inside 44 px labels, secondary Start over folding, modal coverage and a Check cue made obsolete by the fixture were distinguished from real faults.
The audit could not discover its 375 px iframe context. Separate hosted 375x812 captures cover all four modes, all six evidence cards, the prediction view and affected yard states. This is a declared harness gap, not a claim that the audit checked phones. Multiple surviving HTTP listeners on the assigned port were identified during cleanup; an older served directory likely explains the missing iframe page.
The audit snapshot preceded the final bubble/focus/passive-surface fixes. Scoped post-audit captures also verify empty-card narration, prediction headings, reveal skip and calm pixel stability; no full audit or second full review was run. These confirmations, including the reasoning-removal reversal, had zero console errors. Chrome attachment failures were retried within bounds; successful paths are preserved.

#### Left open

- Eight words are a length check, not a scientific-reasoning evaluator; teacher review is explicitly required by the spec. Filler alone cannot bypass the independent direction predictions.
- Recorded upbeat-guide narration remains for the separate recording workflow; no recording or shared engine change was made here.
- The existing globe uses longitude/latitude rotation without free roll. A new rotation interaction was not added in this one-pass repair.
- The spec names cities/base rather than four identifiable surveyed schools; notes state the illustration boundary. No identities or school names were invented.
- Unattended choices followed the spec/baseline. No commits, deployment, shared-file edits or outreach. Writes are confined to this tool and its Scratch folder. Chrome ports are closed and temporary host.html is removed. **Host cleanup remains blocked by Windows permissions:** six verified Python HTTP listeners on 8745, PIDs 6524, 44320, 44824, 47396, 49844 and 50820, returned Access denied on termination. No elevation or policy change was attempted. `review-host-cleanup.json` preserves the ownership proof and errors; these hosts need closing outside this permission profile before port reuse.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Which Way Is Down? Build handoff

#### Source map

src.html starts with the kit frame, responsive control desk and argument card. The script contains the school and test
place tables, line manifest, local save/restore, actions, responsive canvas renderer, orthographic projection and pointer/keyboard input.
land.json is loaded through the bundler's json token. It contains longitude/latitude rings recovered by inverting the
repository's Natural Earth Equal Earth map. All pictures use art tokens. The bundle works offline.

#### Tricky parts

The angle convention is counterclockwise from screen right, with screen-down 270 degrees. Edge views preserve a school's
latitude and requested side. Claim gaps are three-dimensional analytic vector angles. Displayed dashed arrows are the
projection of each rule; the degree verdict is computed in three dimensions.

Physics integrates real elapsed time and changes speed continuously when Slow motion changes. Motion off holds the object
until its landing time. Test attempts are spent before animation or narration; another Predict cannot add another row.
The Strong status waits until the result sequence completes. Changing any evidence invalidates Fits and the current streak.
Restored test rows are historical and cannot restore a streak. An unfinished test resumes after mode changes, so students
cannot skip hard places to preserve a streak. Punctuation does not count as reasoning words. Start over preserves Globe kids.

#### Spec decisions and contradictions

- The open people/sensitivity question takes the brief's permitted people option. All eight child assets have people:true.
  A fresh agent inspected the people sheet and yards. Representation, clothing and anatomy passed. Minor pose differences
  in Jonah's undershirt/backpack and Valentina's hat/scarf/backpack remain. The contact sheet is in Scratch for owner review.
- The initial Quito skyline added a statue and church spires outside the requested backdrop. An image edit removes them.
- Anchorage's numeric view longitude 120.1 E places it on the right under the usual orthographic convention.
  Use 59.9 W for its specified left edge. The parenthetical left/right longitude signs are also reversed.
  The other three numeric view longitudes and all four listed true arrow angles are preserved.
- The table rounds Moon/Mars gravity to 1.6/3.7, while its fall times use 1.62/3.71. Physics uses the precise values,
  shows the requested rounded table and states this in notes. Earth 9.81 follows Interactions; 9.8 is the rounded table.
- Inclusive 8-degree integer tolerance admits 16 settings for fractional true angles and 17 for integer true angles.
  Cairo admits 17; the other seven test places admit 16. The spec's 0.0088 percent three-guess figure is a close
  approximation, not an exact value for this mixed pool. No probability claim is shown to students.
- The rounded Sydney latitude gives a South Pole gap of 61.95 degrees, displayed as 62.0, rather than 61.9 in Sources.
- Claim texts are preserved exactly, despite the stated equal-length range. Cards have equal size and color and shuffled order.
- The model treats every school as mean radius 6,371 km. Real elevations, flattening and local gravity variations are in notes.
- The review resolves the result/Next place wording conflict with separate lines. The result finishes before Next
  enables; nextReady then names the enabled control. No result line now tells a student to press a disabled Next.
- The supplied four school locations represent towns/base, not verified individual school coordinates. The yards and pupils
  are explicitly described in notes as illustrations. No school names or pupil identities are invented.

#### Sensitivity

Four fictional pupils represent Alaska, Ecuador, Australia and an Argentine research base in Antarctica. No claim about
Antarctic territory is made. No Indigenous identity is assigned from appearance or location. Fresh representation review
passed, with the minor pose consistency notes above. This is Build only; owner contact-sheet review remains before shipping.

#### Engine changes wanted

None. The tool uses Curio.voice, Curio.init, Curio.wait, Curio.tone and Curio.yes without changing shared kit files.

#### Build boundary

No commits, shared-file edits, deployment, paid art service or narration recording. Evidence, raw test scripts, frames,
art and people contact sheets and the mechanical audit are under _scratch/which-way-is-down/.
The full audit froze its own HTML before the final mode-resume, punctuation-count, minimum tab-width, partial-record
title, focus, 760-wide layout, reset-reveal and handle-only drag fixes. Focused final proofs cover those changes;
the full audit is a documented snapshot, not final certification.
The first audit-state drag fixture evaluated a point array without returning it. The published audit-states.json now
returns real drag points. The frozen audit did not reach its intended evidence/test states. The separate functional
runner did reach all four records and Strong using real pointer drags.

#### Next review priorities

##### Cold review repairs, 2026-11-06 to 2026-11-07

The short Record confirmation now leaves time for hNext/hZoom to start at a two-second action pace; sync runs before
the newly visible Zoom control is tested. A completed reveal queues the Globe how-to once. Argue entry checks the
number of available records, rather than the number already attached, before asking for more observations.
The first landing says "Straight down." so hMarkBtn can start before the next two-second tap. The plumb-line term
remains on the landing tag, in the diagram, the marking instruction and the teacher notes.
Test result speech does not name Next place while disabled; nextReady speaks after it enables. Strong speech uses
the reasoning gate too, and entering reasoning after the third hit can announce the newly completed card.
Predict moves keyboard focus onto the canvas, then to Next place only if the student has not moved focus elsewhere.

The feather tube was redrawn with the built-in OpenAI image tool. Its source prompt and content band are in prompts.json;
raw/wwd-feather-tube.png is processed with art.py --rekey. vacuumTube keeps the brass shell stationary and moves the
painted feather/apple band together inside it. Other worlds retains all its painted surfaces and gains shaded lane
frames, height ticks, contact shadows and brief landing rings. All moving additions stop with Motion off.
The radius label now says it belongs to the model. Notes link the independently checked geography sources.
At narrow widths six evidence choices use three columns; compact claim cards keep the hint in view. On phones the
school badge sits in the upper-right sky rather than over the child's face. The one-meter ruler has a dark backing
so the Antarctic snow cannot hide its white scale or label. These were checked at the actual affected sizes.
The review audit confirmed a landed-state speech bubble crossing the face at 1000x625. Bubbles now stay in the
left margin, with a separate phone height, and were rechecked in the landed states rather than only the opening yard.
The empty-notebook request uses the same how-to key for its welcome and card taps, once per Argue entry. Repeated
unrecorded-card taps therefore keep the hint available without nagging the same instruction as a fresh event.
The audit also found Go to Drop losing focus as its button disappeared. It now focuses Drop with preventScroll.
Passive yard/world/evidence pictures use role img and stay out of the tab order; only the interactive globe and
Mark/Test arrow expose an application keyboard surface. The label describes the actual mode.
The reveal's canvas arrows had escaped the default-screen calm audit. With Motion off they now hold their short
length through each 800 ms beat and appear extended at its end. Timing and narration order are retained; a pixel
stability check during an active reveal verifies that this is not merely the absence of CSS animation.
The old Pick a claim / Attach evidence headings now hide with their choices during Test, so the prediction controls
are not introduced by obsolete instructions. Laptop and phone prediction frames verify the resulting layout.
Removing reasoning after Strong also reverses the hint and interrupts an obsolete award announcement with the
missing-reasoning event. This is transition feedback, not a repeated how-to on every keystroke.

##### Review cleanup limitation

The temporary host.html is removed and Chrome ports 9940 through 9947 are closed. Six verified Python HTTP listeners
remain on the assigned host port 8745: PIDs 6524, 44320, 44824, 47396, 49844 and 50820. Native process termination
returned Access denied under this permission profile. The server was verified by matching its served tool bytes to
the reviewed bundle before attempting termination. No elevation or policy change was attempted. Close these hosts
outside this permission profile before reusing 8745; see _scratch/which-way-is-down/review-host-cleanup.json.

The build's rapid browser-speech navigation concern was resolved in the cold review. The final two-second main path
heard hMarkBtn, hMark, hNext, hZoom, the three reveal lines, wGlobe, wArgue, hCheck, hTest and wWorlds.
Fixed recordings are not present and recording is outside this brief. Recorded takes will need their own timing check.
The test view resumes after mode changes. Start over clears the argument; it also resets X-ray/reveal state while
preserving added Globe kids. Reloaded test rows are deliberately historical, so a saved card must earn a fresh streak.
Globe rotation uses yaw and pitch, with pitch limited near the poles; it does not offer free roll.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)

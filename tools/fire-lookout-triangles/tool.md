# Fire Lookout Triangles: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: fire-lookout-triangles

#### Built
Built all four specified modes in a self-contained HTML bundle, using the kit starter, 9-12 theme, Curio.voice, and the specified red-orange accent. The SVG map uses equal distance scales and real pixel layout. No family engine applies.
Delivered src.html, tool.draft.json with stage built, notes.md, voice/lines.json, audit-states.json, handoff.md, eight finished images with prompts, and preview.svg. No commit or polish round.
Workspace was S:\CurioClass-codex. Tool work and evidence stay in the two authorized folders. Existing bar bundles were opened read-only because rebundling them would write outside this boundary.
Evidence root: ../../_scratch/fire-lookout-triangles/. Separate checks: 41 functional, 8 keyboard/focus, 4 voice, and 9 edge assertions passed. The mechanical audit did not finish.
Computed contrast ratios: accent on panel 5.83:1, accent on section 5.53:1, dark ink on accent 6.12:1, map ink on its halo 15.42:1.

#### Numbers check
Independent Python computation: ../../_scratch/fire-lookout-triangles/setup.py and numbers.json. All supplied worked answers agree at their stated precision.
B = (13.15569669, 4.78828201); C = (6.00000000, -10.39230485) miles. Baselines are 14 and 12 miles.

| Smoke | A, B, F degrees | AF mi | BF mi | CAF degrees | CF mi |
|---|---|---|---|---|---|
| 1 | 35, 95, 50 | 18.20615749 | 10.48251205 | 115 | 25.69292279 |
| 2 | 30, 80, 70 | 14.67214729 | 7.44924441 | 50 | 11.52935898 |
| 3 | 60, 50, 70 | 11.41290457 | 12.90246979 | 140 | 22.00184996 |
| 4 | 50, 50, 80 | 10.89006679 | 10.89006679 | 30 | 6.02061184 |

Radio: perpendicular height 7 mi; Call 1 distances 6.46750140 and 17.78120990 mi, angles 128.94 and 51.06 degrees; Call 2 distance 12.12435565 mi; Call 3 no intersection.
Burns: 0.40129821, 1.40953893, 0.32000000 square miles; 256.83085168, 902.10491595, 204.80000000 acres.
C's exact smoke readings are 9.9572, 47.1255, 349.4771, 34.7424 degrees. Its tags round to three-digit whole azimuths.
Burn 2 cannot fit a two-mile square: its width is 2.513 mi before margins. It receives a 2.993 mi view; other burns use two-mile views. Data stay unchanged.

#### Facts checked
- Sine law, opposite-side pairing, SSA alternatives, and half-ab-sine-C area: [OpenStax 10.1](https://openstax.org/books/algebra-and-trigonometry-2e/pages/10-1-non-right-triangles-law-of-sines).
- Cosine law and its included angle: [OpenStax 10.2](https://openstax.org/books/algebra-and-trigonometry-2e/pages/10-2-non-right-triangles-law-of-cosines).
- Clockwise azimuths and locating a fire by crossing tower readings: USDA Forest Service, Firefighter Math, [Chapter 6, Location](https://www.fs.usda.gov/t-d/pubs/pdf/00511802.pdf). No inventor or invention date is claimed.
- One square mile equals 640 acres: [NIST conversion table, square-mile row](https://www.nist.gov/pml/us-surveyfoot/revised-unit-conversion-factors), also referenced by Handbook 44 Appendix C.
- Triangle angles sum to 180; opposite azimuths differ by 180 degrees; all preset positions, distances, readouts, scale bars, and radio intersections follow the independent geometry computation.
- Blue Lake's north shore is y = 11.5; the farther radio point is y = 13.6212. The approximately two-mile south clue fits the farther point.
- Forest, named towers, roads, lake, creek, smoke locations, engine calls, and burn surveys are fictional content from spec.md. Arrival and completion labels describe verified program state.
- Privacy: only check marks are saved locally. Clear marks was tested; network instrumentation found no tool HTTP requests.
- Coverage caveat: [CCSS G-SRT.D.9 and D.10](https://www.thecorestandards.org/Math/Content/HSG/SRT/) require derivation and proofs. The spec supplies application activities only. Those parts are not claimed as taught; notes and handoff state the gap.

#### Break it
- Sight gate: used whole-pixel, timing-jittered real drags and keyboard turns. A single locked sight never unlocks calculations; both must point at the smoke.
- Angles: empty and incorrect boxes do not advance. The checker requires the exact three whole-degree values, including the third angle.
- Distance: 18.0 fails for Smoke 1; 18.2 mi and 18.21 fit tolerance. Blank, NaN, Infinity, exponent overflow, trailing garbage, and arithmetic expressions fail.
- Show me: deliberately missed twice and copied its filled answers through the remaining steps. The run reaches the crew as guided and earns no saved check mark. This closes the cheap saved-completion cheat.
- Marks: none are written at calculation completion or during a drive. Replacing a smoke stops the drive; no ghost arrival or mark appears later. Clear marks removes saved marks.
- Radio: tried 0, 1, and 2 in sequence, wrong map points, and the same true point twice. Counts alone do not finish; Call 1 needs two distinct intersections. Call 3 requires the separate No spot confirmation.
- Burn: 0.41 fails for Burn 2; all three correct area/acres pairs pass. Both units are checked. Its worked solution is teaching assistance, with no score or mastery badge.
- No best score or competitive meter exists. Repeating checks cannot create an achievement total. Completion marks are explicitly a local convenience, not assessment.
- Sampled 1,200 random smokes independently for bounds, tower clearance, angle F range, and reconstruction from rounded readings. All passed.
- Edge probes: painted tower taps do nothing; six points near map boundaries remain on the map. Neighboring whole-degree readings resolve rounding that would otherwise place a fix just outside the boundary.
Evidence: checks/functional.json, keyboard.json, edges.json, plus numbers.json.

#### Voice walk
Held clicks used a 120 ms press and a 2 s pace. The main path crossed all modes; the side path used a wrong count, Read, Sound off, a mode change, Sound on, and Read again.
Main lines started in this order:
spot, spotC, dispatch, sight, angles, right, af, right, cf, right, crew, onScene, radio, radioPin, two, burn, right.
All four correct checks spoke their event. No how-to repeated. Read used the currently displayed hint. Inventory matches the 21 runtime lines.
Fixed a dropped radioPin line: choosing the count now interrupts the obsolete welcome using the kit's now option. Step changes similarly replace obsolete instructions; Read keeps priority.
The first custom keyboard test used an incomplete DevTools Enter event. Correcting the harness to send Enter text produced the real keyboard path; no tool workaround was added for that harness fault.
Narration is browser fallback, not an Algenib recording or a listening verification of gravel-ranger. No audio was recorded.
Evidence: checks/voice-walk.json and voice.json.

#### Feel check
Played the complete sequence through all four fixed smokes, the radio alternatives, and all burns, with real aiming and typed answers.
Best moment: the engine follows the dirt road, turns toward the located fire, and leaves an earned field-log entry with the student's distances.
Flattest moment 1: the short preview clipped smoke and hid part of Check area. The plume now rises above the map frame; compact given-data text and panel spacing keep the main action visible.
Flattest moment 2: a radio count initially led to a long wait for its next spoken instruction, and the near pin label collided with B. The instruction changes immediately and the pin label now sits on the other side.
Compared the built frame beside Beat Lab in ../../_scratch/fire-lookout-triangles/bar-comparison.jpg, and inspected Snowy Mail Route separately. The painted terrain, detailed objects, disciplined map overlays, and engine arrival give this tool comparable visual care with a different mood.
The later math still asks for deliberate calculation. The random cases and three radio geometries provide variation without adding unrelated rewards.

#### Done when
1. PASS: real Spot taps swing both sights; Smoke 1 reads 35 + 95 + 50 = 180. Collinear placement reports no triangle.
2. PASS: Smoke 1 locks at 035 and 345; angles, AF 18.2, and CF 25.69 pass; AF 18.0 fails. C radius equals the independent distance to the fire.
3. PASS: fixed answers for Smokes 2, 3, and 4 pass; Smoke 4 AF equals BF.
4. PASS: 1,200 random cases satisfy bounds, clearance, valid crossing, and rounded-angle reconstruction.
5. PASS: Call 1 needs two distinct pins; Call 2 has the tangent point; Call 3 has none.
6. PASS: Burn 1 accepts 0.40 and 257; Burn 2 rejects 0.41 and accepts 1.41 and 902.
7. PASS: keyboard 1-degree and 10-degree turns, slider value text, and a complete Dispatch path without pointer input.
8. PASS for queue behavior: every required main-path instruction started once; all four correct checks spoke. Recorded-voice timbre remains open.
9. PASS by inspected frames: map is the largest scene at 1366x768 and 1000x625; detailed forest and instrument art remain visible; map labels are at least 11 px.
10. PASS: replacement during sight motion, drive cancellation, burn replacement, and mode changes keep the newest state. A resize during the truck drive leaves arrival and marks correct.
11. PASS by frames: main controls fit 1366x768 and 1280x720; compact preview and phone fixes preserve the main controls and readable labels. Extended worked text and secondary logs can scroll.
12. PASS: network trace has no tool HTTP requests; source and notes have no em dashes; all eight assets show no people.

#### Wave lessons
- Hint and voice: PASS. Immediate state hints, kit how/event distinction, Read priority, and tested 2 s pace.
- Focus and layout: PASS. Static controls, reserved hint space, preventScroll focus, next-smoke focus after arrival, visible-call focus after No spot.
- Sizes: PASS by inspected manual frames at every required size, with 44 px controls and handles. Full mechanical audit is unfinished.
- No giveaways: PASS. Dispatch keeps unknown distances hidden; worked answers label the run guided and block its saved mark.
- Honest numbers: PASS. Fictional setting and rounded-azimuth convention are explicit; tolerance checks use unrounded computations.
- Standards: PARTIAL. Solo applications cover the planned math, including ambiguous SSA. D.9 derivation and D.10 proofs are absent from the spec and build.
- Motion off: PASS. No looping signal animation; sights, zoom, and drive resolve instantly as this spec requests.
- Short choice sets: PASS by frames. Four smokes, three calls, three counts, and three burns remain available together.
- Resize during animation: PASS. Real truck drive resized to 760x900 and back with no exception or stuck state.
- Late welcome: PASS. Current-mode taps do nothing; mode/state validity drops obsolete welcomes. No welcomeAfter workaround.
- Unknown stays unknown: PASS. Initial triangle values use question marks; Dispatch does not reveal unsolved distances.
- One look, one meaning: PASS. A solid, B dashed, and C dotted, supported by letter labels and azimuth tags.
- Truthful badges: PASS. Guided runs are labeled and not marked as independently completed; arrival marks follow actual arrival.
- Hints change back: PASS. Mode and reset hints update immediately; returning to empty Spot resets its status text.
- No answer by word matching: PASS. Numeric geometry and spatial intersections are required; no answer-card wording shortcut exists.

#### Audit leads
AUDIT NOT FINISHED. The single invocation exited on a 60 s DevTools protocol timeout while enabling a fresh page, before the first size frame or incremental report save. No mechanical leads were produced. The outer command cap was 40 minutes.
Exact invocation and trace endpoint are in ../../_scratch/fire-lookout-triangles/audit-failure.md. Shared audit/driver files were unchanged; no workaround or second full audit was run.
Manual frames and the separate real-input checks are evidence for the specific passes above, not a substitute clean-audit claim.
The initial drive.py phone host requested a missing favicon. The final scratch host uses a data icon and all final target shots report zero console warnings, errors, or exceptions. Server connection resets occurred only when Chrome closed idle HTTP connections during shutdown.
After the failed audit, only targeted label/focus/edge checks were run; the entire size set was not repeated.

#### Frames looked at
Opened every captured PNG, including superseded frames:
- references/: both bar tools.
- initial/: default, worked Spot, Dispatch preview, Burn preview.
- sizes/: all seven standard desktop/tall sizes, compact Dispatch and Burn, grayscale Radio, Motion-off Burn.
- phone/: all four modes through a 375x812 iframe.
- checks/: crew arrival, solved Radio, solved Burn, keyboard arrival, voice side path, map-edge smoke.
- final/: Radio label fix, tall stacked layout, creek label, three phone label fixes, and final edge label.
Also inspected art-contact.jpg and bar-comparison.jpg. The final focused frames supersede the earlier clipped-label versions. No audit PNG existed.

#### Art made
Seven missing assets generated using the built-in image tool, plus one smoke redraw; one existing dusk image preserved. Eight final images total, about 256.7 KB. Voice files: 0 KB. Bundle: about 582 KB, comfortably below the 2 MB goal.
The prompt set is art/prompts.json; originals are in art/raw/; final WebPs are in art/. Credit is in tool.draft.json. People is false on every asset.
The original magenta-keyed smoke had a colored fringe. It was redrawn as opaque gray on green and processed through scripts/art.py --rekey, as were the other new assets. No paid art.py generation or audio service was called.
The existing dusk image is used in the welcome and preview.svg; all other planned images are used at useful scene sizes.

#### Art still to paint
None.

#### Engine changes wanted
None.

#### Left open
- Mechanical audit is unfinished because of the DevTools timeout. A later cold review must run it.
- The requested gravel-ranger recording is absent under the no-recording instruction; browser narration is available.
- D.9 derivation and D.10 proofs need a curriculum decision. No extra activity was improvised.
- Burn 2's viewport and Spot's rounded boundary convention differ from a literal reading of the spec; both are documented in handoff.md.
- All test Chrome profiles and servers belonging to this build were closed. Cleanup found no remaining owned process; host.html is absent. No shared source file was edited. No git operation, publication, or polish round was performed.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: fire-lookout-triangles

#### Played
Cold, as a grade 12 student: Spot exploration, a full Smoke 1 dispatch, all three Radio calls, and Burn 1, with held clicks and Sound on, before reading codex-report.md, handoff.md, notes.md or src.html. The map and crew arrival are strong. Then checked the Teaching, Play and Craft lenses, projection sizes, keyboard-only dispatch, cheap paths and errors. One review pass; fixes received focused re-checks.

#### Findings fixed
- **blocker, general, Dispatch checks:** 624 blind numerical trials, copying Spot answers, and restarting a worked example each earned an independent saved mark. Two rejected checks or exposed answers now keep that triangle guided for the page session, including restarts; it can finish but earns no mark. All three exact attacks now yield marks `[]`, with guided labels in the step and log.
- **blocker, general, Burn:** copying Show me received ordinary success; changing that answer to 999 square miles and 0 acres left success and its answer visible. Guided work now has distinct feedback/voice. Editing a checked answer clears its result, worked card and map answer immediately. Error hints update immediately and Read names Check area.
- **should fix, general, Radio:** count enumeration led to unqualified result feedback. A wrong count or two missed pins now labels the comparison guided; distinct intersections remain mandatory.
- **should fix, general, compact Radio:** the painting covered call text because compact section padding overrode its reserved space. Restored image padding and fitted the quote. Zero-spot confirmation now replaces the answered count row, keeping No spot visible and focused at 680x425.
- **should fix, general, map labels:** Cedar Creek overlapped C at small scales; phone Radio pin distances were clipped by the map frame. Moved these labels into clear side margins. North-facing sight aria readings now wrap to 0, matching 000 degrees on screen.
- **should fix, general, art:** colored cutout fringes, weakest on the radio. Redrew the radio with the built-in image tool; re-keyed all five cutouts with hole detection and spill removal using the required free pipeline.
- **polish, general, opening:** tighter preview readouts expose the full welcome painting and copy at 680x425.
- **polish, general, Radio payoff:** the old ending was a paragraph that supplied the lake answer. Its existing clue now also marks the farther pin and the southward lake connection on the map. Both mathematical solutions remain visible.
- **should fix, general, Read:** fixed hints were absent from the narration inventory, and Show me left its earlier error hint behind. All 44 narration/Read lines are now inventoried; Show me immediately names Check as the next action. The main voice walk and Read were re-run. Corrected voice token quoting for future recordings.
- **should fix, general, audit-confirmed craft:** raised covered B/F labels, separated phone AC/BT labels and the lake/handle, set Spot to at least 44 px, and made input names explicit. Expired sight handles now disappear immediately when the angle step opens. Reserved Sound width to prevent header shifts.
- **should fix, general, audit-states.json:** eight drag expressions omitted the required outer return, so named states were never reached. Corrected them; real-input replays now reach angles, guided readiness, crew arrival and both Radio pins.

#### Findings left
- **should fix, spec-level scope:** G-SRT.D.9 requires deriving the area formula; D.10 includes proofs. The spec supplies applications. Notes disclose this; no new activity or shared curriculum mapping was invented. Owner must resolve the coverage claim.
- **polish:** the requested gravel-ranger timbre has no recording. Browser speech works; the build rules prohibit recording audio in this run.

#### Break it
- **Sight gate:** swept keyboard bearings until each instrument locked; one sight alone does not open the angle form. The valid directions are still required, and bearings/lock status do not reveal the later distances.
- **Angles, AF, CF:** exact angle checks and separate distance checks remain. The 624-check sweep is guided with no mark. All four independent preset solutions still pass and earn their marks. Empty/nonfinite/arithmetic/trailing-garbage inputs fail parsing. Smoke 1 AF 18.0 fails; 18.2 mi passes; CF 25.69 passes.
- **Show me and marks:** copied work can reach the crew as guided practice. No mark is awarded, including after restarting and re-entering the copied answers. Copying the exact visible Spot triangle also stays guided. An independent path still earns Smoke 1's mark only at arrival. Keyboard-only arrival also earns its mark and moves focus to Smoke 2.
- **Radio:** tried 0, 1 and 2 in turn; count-only never finishes. A repeated pin leaves exactly one location and cannot satisfy the two-location case. Wrong locations fail. Count guessing plus the true pins is labeled guided. Calls 2 and 3 finish only at their tangent point and No spot confirmation respectively.
- **Burn:** both units are required: correct square miles with zero acres fails. Burn 2 rejects 0.41 and accepts 1.41/902; Burn 3 accepts 0.32/205. Show me and repeated checks stay guided. A post-success edit removes success before another check; incorrect replacement values fail with no lingering answer overlay. Repeated correct checks create no score or saved achievement.
- **Random smoke:** 1,200 new cases passed bounds, two-mile tower clearance, 25 to 155 degree fire angle, and reconstruction from the rounded sightings. Collinear smoke reports no triangle. Replacing a smoke during its swing and a burn during zoom settles on the latest case. A canceled independent drive earns no mark; a resize during arrival still completes correctly. There is no best score, reflection gate, or competitive meter.
- Evidence: `../../_scratch/fire-lookout-triangles/pre-*.json`, `post-*.json`, `recomputed-review.json`, `review-post/`, `review-focused/`.

#### Voice walk
120 ms held clicks, two-second gaps, default student path first; repeated with Sound and Motion on after repairs. Main sequence heard: spotC, dispatch, sight, angles, right, af, right, cf, right, crew, onScene, radio, radioPin, two, right, radioNone, right, burn, right.
Spot's first map tap skips its welcome under BASELINE rule 16; the current hint still tells the student to tap another clearing. Each later mode/how-to starts once, in context. Read interrupts speech, works with Sound off, and releases on a mode change. No stale-mode speech or console exception was found in the captured walks.

| Line | Kind | Expected | Spoken |
|---|---|---:|---:|
| Each main-path how-to above | how | 1 | 1 |
| miss, five side-path failed checks | event | 5 | 5 |
| right, five side-path correct checks | event | 5 | 5 |

Evidence: `review-voice-summary-final.json`, `review-voice-after-audit/`, earlier five-repeat counts in `review-voice-final/side-voice.json`, and its separate `keyboard-only.json`. This verifies browser narration behavior, not a recorded Algenib performance.

#### Facts checked
- Laws of sines/cosines, opposite-side pairing, the 180 degree angle sum, positive SSA alternatives, and half-ab-sine-C area: [OpenStax 10.1](https://openstax.org/books/algebra-and-trigonometry-2e/pages/10-1-non-right-triangles-law-of-sines) and [10.2](https://openstax.org/books/algebra-and-trigonometry-2e/pages/10-2-non-right-triangles-law-of-cosines), checked live. All example numbers independently recomputed in `recompute-review.py`.
- Towers B (13.15569669, 4.78828201), C (6, -10.39230485), baselines 14/12 mi, reverse azimuths 250/330 degrees: independent coordinates from the fictional spec, with the same trigonometry sources.

| Smoke | A/B/F degrees | AF/BF/CF miles, independently rounded |
|---|---|---|
| 1 | 35/95/50 | 18.21 / 10.48 / 25.69 |
| 2 | 30/80/70 | 14.67 / 7.45 / 11.53 |
| 3 | 60/50/70 | 11.41 / 12.90 / 22.00 |
| 4 | 50/50/80 | 10.89 / 10.89 / 6.02 |

- Radio's perpendicular height is 7 mi. Radii 9/7/6 give two/one/zero solutions; AT is 6.46750140 or 17.78120990, then 12.12435565 mi; T is 128.94 or 51.06, then 90 degrees. Independent ray-circle and sine-law calculations agree with OpenStax 10.1. The far point's north coordinate 13.6212 minus the specified lake shore 11.5 is 2.1212 mi, so the approximately two-mile south clue fits.
- Burn areas: 0.40129821, 1.40953893, 0.32000000 square miles; 256.83085, 902.10492, 204.8 acres. Formula: OpenStax 10.1. Conversion 1 square mile = 640 acres: [NIST Handbook 44, 2026 Appendix C](https://www.nist.gov/system/files/documents/2025/12/30/appc-26-HB44-20251222.pdf), checked live.
- Azimuth clockwise from north and crossing lookout sightings: USDA Forest Service/NWCG, [Firefighter Math 6.2, Azimuths](https://www.nwcg.gov/course/ffm/location/firefighter-math-62-azimuths) and [6.8, Intersection](https://www-nwcg.fs2c.usda.gov/course/ffm/location/firefighter-math-68-intersection). No inventor or date is claimed.
- Derivation/proof/application coverage: [CCSS G-SRT.D.9 to D.11](https://www.thecorestandards.org/Math/Content/HSG/SRT/), checked live. Fictional geography and crews are clearly identified; this is a geometry model, not operational dispatch guidance. Local storage and no-request claims checked against source and the embedded bundle, not an external authority.

#### Sensitivity
None: fictional forest and crews, no real community, culture, religion, hard history, body or people image. The scene needs no identifiable figure at this map scale. All eight assets were inspected; people flags are false. Fire depiction is quiet, with no injury.

#### Flattest moment left
Repeated calculation forms remain deliberate calculator work. That is the specified grade 12 task. The formerly flat Radio ending now has a visible, case-specific lake-clue payoff; the forest scene and earned truck arrival were retained.

#### Graphics
Inspected all eight assets at display scale: dusk lookout, forest canopy, tower, smoke, flame, truck, radio and burn scar. Radio redrawn once; five keyed assets cleaned. No missing art or added topic. Art 257.2 KiB; bundle 588.5 KiB, below 2 MB. Computed palette contrasts: accent/panel 5.83:1, accent/section base 5.53:1, dark ink/accent 6.12:1, map ink/halo 15.42:1. Compared fresh read-only Snowy Mail Route and Beat Lab frames, with `review-bar-comparison.jpg` side by side; preserved this tool's richer forest and restrained instrument style.
Opened all manual captures in `review-cold`, `review-play`, `review-break`, `review-post`, `review-sizes`, `review-changed`, `review-focused` and `review-voice-final`, plus the focused audit, current voice, copy/restart, fixture and edge re-check folders. Covered all STANDARDS sizes, all four phone modes through the 375x812 host, grayscale, Motion off, visible focus and keyboard-only completion. Secondary worked cards scroll; main input controls remain available.

#### Audit
Completed once, last, within the 40-minute command cap: `review-audit/audit.md`, 109 mechanical leads and 66 frames. Confirmed target, text-layer and label collisions were repaired and re-shot at their affected sizes. Explicit input names were added. The broken drag-state definitions explain the hidden-step and lost-focus leads; corrected real-input replays reach the promised states, including a resized drive. The audit was not run again.
Intentional map/field-sheet/handle layering stays. Clear marks is secondary log maintenance; all actual smoke choices remain available. The clipped duplicate Burn card error has its complete copy and next action in the visible hint. Passive map clicks are not promised actions. First-tap welcome leads are covered by BASELINE 16 and the independently verified current-mode instructions. Calm, repeated-click and rapid-tap checks were clean. Full dispositions: [review-audit-disposition.md](../../_scratch/fire-lookout-triangles/review-audit-disposition.md).
Wave lessons were checked through the cold play, all sizes, real input and the scoped repairs: immediate state hints/Read, preserved focus, 44 px controls, non-color sight styles, honest numbers/marks, visible choice sets and Motion off. The standards coverage exception remains named above.

#### Left open
- Curriculum coverage and requested recorded timbre above need a later scope decision; no kit changes, spec edits, recording, commit or deployment was made.
- Unattended choices: two rejected checks use the spec's two-miss assistance threshold; already exposed or guided triangles remain guided for this page session; preserve both SSA solutions; retain the unnamed fire finder; retain Burn 2's documented larger viewport because its exact geometry cannot fit a two-mile square.
- Process deviation: initial workspace/brief reads and memory search completed without an explicit command wrapper in under one second each. All subsequent commands used explicit deadlines. Review notes stayed in Scratch until this final report, honoring the stop-on-write instruction.
- Host file removed. All assigned Chrome and host ports verified closed; only the named tool and Scratch hold authored project changes. No git operation was made.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Fire Lookout Triangles handoff

Build only, 2026-11-05. No commit or polish round. Source and evidence are confined to this tool and `_scratch/fire-lookout-triangles/`.

#### Structure
`src.html` follows the kit starter, with the 9-12 theme, a tool palette, four static panel panes, and a responsive SVG map. The panel appears first in DOM order for keyboard navigation, while CSS places the map on the left. SVG coordinates are recomputed in real pixels on resize, with one common scale for miles east and north.

The script is organized as geometry and number parsing; narration; cancelable animations; Spot; Dispatch; Radio; Burn area; SVG drawing; and input wiring. The test hook exposes state, geometry, drawing transforms, and the kit voice log. It exposes no score-setting or completion shortcut. The only stored data are fixed-smoke completion marks in `curio-flt-done`, guarded by try/catch.

Sight handles are persistent HTML slider buttons above the SVG, with pointer capture, 44-pixel targets, and keyboard azimuth controls. Map crosshair input makes Spot and Radio usable with a keyboard. The open Dispatch form moves focus only when its predecessor becomes hidden. Other controls keep their DOM identities.

All animations share a cancellation handle. Replacing a smoke, restarting, changing modes, or replacing a burn cancels the old operation. Draws never replace the handle buttons or the form controls. Reduced motion finishes the geometry and arrival instantly, as the spec explicitly asks.

#### Decisions and contradictions
- Open question: leave the instrument unnamed. No inventor, date, or Osborne Firefinder claim was added. This follows the option the spec leans toward.
- Art method: the current build brief and direct request require the image tool, which supersedes the spec's older local-FLUX instruction. Seven missing assets were generated with the built-in image tool, plus one smoke redraw. The existing dusk painting is preserved. All assets have `people: false`.
- Burn viewport: Burn 2 cannot fit in a two-mile square. In the chosen orientation its horizontal extent is 2.513 miles before label margins. The tool fits its exact geometry in a 2.993-mile square; Burns 1 and 3 use two-mile views. This is a viewport correction, not a change to its data or learning goal.
- Layout: STANDARDS takes precedence over the spec's unconditional stacking below 1000 pixels. Short landscape previews keep the panel beside the map. Tall narrow screens stack; phones use a shorter map so the main controls and hint remain visible.
- Spot precision: a tap snaps slightly to the intersection of rounded azimuths. At a boundary, the nearest valid intersection from neighboring whole-degree readings is used to keep smoke on the map. The point, readouts, worked law, and C circle agree exactly. Collinear smoke stays at its tapped position and reports no triangle. This convention is explained in teacher notes.
- Worked examples: Show me is available after two misses, as specified. Any Dispatch run using it is labeled guided and earns no saved check mark. The field log identifies guided runs. There is no best score or Radio/Burn mastery claim to farm by enumerating answers.
- Voice: no audio was recorded, as the brief prohibits it. `voice/lines.json` requests gravel-ranger / Algenib; the runtime uses the kit's browser speech fallback. This does not reproduce the requested timbre. Stale how-to speech can be cut as the task changes; Read retains kit priority.
- Standards: the spec's solo activities apply both laws and the area formula. CCSS G-SRT.D.9 requires deriving the area formula, and D.10 requires proving the laws. Neither derivation is specified or added. These are curriculum scope gaps for the owner to resolve, not claims that proofs are taught.
- Report timing: the direct instruction says to stop when codex-report.md is written. The report is finalized last, rather than creating an early partial report and continuing after that trigger.
- Reference tools: their existing self-contained bundles were opened read-only. Rebundling another tool would violate this run's write boundary. The nearest math neighbor has no handoff or refine file; existing Biased Bot handoff and refine notes supplied additional focus and voice lessons.

#### Evidence
Scratch holds `numbers.json`, the source computation script, generated-image path mapping, art contact sheet, reference frames, initial and final size frames, real-input functional/voice/keyboard checks, phone frames, and the mechanical audit. Functional cases independently check the fixed answers and 1,200 randomly generated smokes. Audit states use actual clicks and drags, including guided progress through the locked steps.

Teacher notes distinguish completion marks from assessment, explain rounding and the fictional map, give keyboard instructions, and name sources. Review should retain the painted scene and the subdued instrument style.

#### Art still to paint
None. The original magenta-keyed smoke had a colored fringe and was redrawn in opaque gray on green, then processed through the required free rekey pipeline. All other cutouts and textures were inspected together at final display scale.

#### Sensitivity
No people, cultures, Indigenous communities, religion, hard history, or bodies appear. The forest and incidents are fictional. This is a classroom geometry model, not operational fire advice. Review the quiet fire depiction for age suitability; no injury or destructive spectacle is shown.

#### Engine changes wanted
None. Kit files are unchanged. The built-in queue's `now` option already provides state-change interruption while preserving Read priority.

#### Next review
Confirm the proof and area-derivation requirements with the curriculum owner, and decide whether the requested ranger recording should be produced in a separately authorized audio pass. The mechanical audit stopped before its first stage on a DevTools timeout. The build report records that unfinished check and the separate successful checks.

#### Cold review repairs, 2026-11-08
The cold playthrough preceded reading builder notes/source. A numerical sweep earned a false independent Dispatch mark. Two rejected checks across a run now set assisted, which survives step transitions; Show me still opens after two misses within a step. The guided event has separate narration and never earns a saved mark. Resetting or choosing a new smoke starts a fresh attempt.

Burn now identifies guided work after repeated checks or Show me. Editing a completed answer immediately clears burnDone, its worked result and map answer, and keeps subsequent work guided because the solution was exposed. Failure hints now name the error and Check area at once. Radio count enumeration is labeled guided; distinct spatial intersections are still required. Its completed two-spot map highlights the farther pin and the southward lake clue, retaining both mathematical solutions.

Radio art was redrawn with the built-in image tool. All five cutouts were re-keyed with holes and despill options through scripts/art.py --rekey. Original radio is preserved in Scratch. The original forest, tower design, textures and restrained palette are retained. No shared kit changes or audio recordings.

Review evidence uses review-* files in Scratch, separate from builder evidence. See codex-review.md for the final audit disposition and remaining spec-level coverage limits.

Compact layout repairs keep the creek label clear of C and preserve the radio image's padding. At the smallest preview, tighter Spot readouts leave the welcome painting readable. Radio pin distances move into clear side margins on phones. In the zero-spot confirmation step, No spot replaces the already answered count choices in the same space and receives focus without scrolling; the count choices return after confirmation. Sight aria values wrap at north just like the visible three-digit azimuth.

The one review audit completed with 109 mechanical leads. Its drag snippets lacked outer returns, so several named states had never been reached by that replay. Eight snippets now return their coordinates; focused real-input replays verify the actual states, including a resize during arrival. Map labels now paint above plumes, and cramped AC/BT annotations use clear phone margins. The Spot button is at least 44 pixels wide, Sound has stable width, and all numeric inputs have explicit accessible names. Completed aiming redraws immediately to remove inactive handles.

The narration-only inventory omitted fixed Read hints. All 44 narration/Read strings now belong to Curio.voice's line inventory and voice/lines.json. Show me updates its hint to the actual next Check action. The main voice walk was repeated afterward. No recording was made.

An in-memory set remembers exact rounded triangles viewed in Spot or given guided status during this page session. Reusing their answers in Dispatch, including restarting a completed guided example, stays guided and earns no new saved mark. This closes cross-mode and restart answer-copy routes while preserving free exploration. It adds no persisted data. Detailed audit dispositions and final evidence are linked from codex-review.md.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)

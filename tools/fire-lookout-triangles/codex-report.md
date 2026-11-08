# Codex report: fire-lookout-triangles

## Built
Built all four specified modes in a self-contained HTML bundle, using the kit starter, 9-12 theme, Curio.voice, and the specified red-orange accent. The SVG map uses equal distance scales and real pixel layout. No family engine applies.
Delivered src.html, tool.draft.json with stage built, notes.md, voice/lines.json, audit-states.json, handoff.md, eight finished images with prompts, and preview.svg. No commit or polish round.
Workspace was S:\CurioClass-codex. Tool work and evidence stay in the two authorized folders. Existing bar bundles were opened read-only because rebundling them would write outside this boundary.
Evidence root: ../../_scratch/fire-lookout-triangles/. Separate checks: 41 functional, 8 keyboard/focus, 4 voice, and 9 edge assertions passed. The mechanical audit did not finish.
Computed contrast ratios: accent on panel 5.83:1, accent on section 5.53:1, dark ink on accent 6.12:1, map ink on its halo 15.42:1.

## Numbers check
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

## Facts checked
- Sine law, opposite-side pairing, SSA alternatives, and half-ab-sine-C area: [OpenStax 10.1](https://openstax.org/books/algebra-and-trigonometry-2e/pages/10-1-non-right-triangles-law-of-sines).
- Cosine law and its included angle: [OpenStax 10.2](https://openstax.org/books/algebra-and-trigonometry-2e/pages/10-2-non-right-triangles-law-of-cosines).
- Clockwise azimuths and locating a fire by crossing tower readings: USDA Forest Service, Firefighter Math, [Chapter 6, Location](https://www.fs.usda.gov/t-d/pubs/pdf/00511802.pdf). No inventor or invention date is claimed.
- One square mile equals 640 acres: [NIST conversion table, square-mile row](https://www.nist.gov/pml/us-surveyfoot/revised-unit-conversion-factors), also referenced by Handbook 44 Appendix C.
- Triangle angles sum to 180; opposite azimuths differ by 180 degrees; all preset positions, distances, readouts, scale bars, and radio intersections follow the independent geometry computation.
- Blue Lake's north shore is y = 11.5; the farther radio point is y = 13.6212. The approximately two-mile south clue fits the farther point.
- Forest, named towers, roads, lake, creek, smoke locations, engine calls, and burn surveys are fictional content from spec.md. Arrival and completion labels describe verified program state.
- Privacy: only check marks are saved locally. Clear marks was tested; network instrumentation found no tool HTTP requests.
- Coverage caveat: [CCSS G-SRT.D.9 and D.10](https://www.thecorestandards.org/Math/Content/HSG/SRT/) require derivation and proofs. The spec supplies application activities only. Those parts are not claimed as taught; notes and handoff state the gap.

## Break it
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

## Voice walk
Held clicks used a 120 ms press and a 2 s pace. The main path crossed all modes; the side path used a wrong count, Read, Sound off, a mode change, Sound on, and Read again.
Main lines started in this order:
spot, spotC, dispatch, sight, angles, right, af, right, cf, right, crew, onScene, radio, radioPin, two, burn, right.
All four correct checks spoke their event. No how-to repeated. Read used the currently displayed hint. Inventory matches the 21 runtime lines.
Fixed a dropped radioPin line: choosing the count now interrupts the obsolete welcome using the kit's now option. Step changes similarly replace obsolete instructions; Read keeps priority.
The first custom keyboard test used an incomplete DevTools Enter event. Correcting the harness to send Enter text produced the real keyboard path; no tool workaround was added for that harness fault.
Narration is browser fallback, not an Algenib recording or a listening verification of gravel-ranger. No audio was recorded.
Evidence: checks/voice-walk.json and voice.json.

## Feel check
Played the complete sequence through all four fixed smokes, the radio alternatives, and all burns, with real aiming and typed answers.
Best moment: the engine follows the dirt road, turns toward the located fire, and leaves an earned field-log entry with the student's distances.
Flattest moment 1: the short preview clipped smoke and hid part of Check area. The plume now rises above the map frame; compact given-data text and panel spacing keep the main action visible.
Flattest moment 2: a radio count initially led to a long wait for its next spoken instruction, and the near pin label collided with B. The instruction changes immediately and the pin label now sits on the other side.
Compared the built frame beside Beat Lab in ../../_scratch/fire-lookout-triangles/bar-comparison.jpg, and inspected Snowy Mail Route separately. The painted terrain, detailed objects, disciplined map overlays, and engine arrival give this tool comparable visual care with a different mood.
The later math still asks for deliberate calculation. The random cases and three radio geometries provide variation without adding unrelated rewards.

## Done when
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

## Wave lessons
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

## Audit leads
AUDIT NOT FINISHED. The single invocation exited on a 60 s DevTools protocol timeout while enabling a fresh page, before the first size frame or incremental report save. No mechanical leads were produced. The outer command cap was 40 minutes.
Exact invocation and trace endpoint are in ../../_scratch/fire-lookout-triangles/audit-failure.md. Shared audit/driver files were unchanged; no workaround or second full audit was run.
Manual frames and the separate real-input checks are evidence for the specific passes above, not a substitute clean-audit claim.
The initial drive.py phone host requested a missing favicon. The final scratch host uses a data icon and all final target shots report zero console warnings, errors, or exceptions. Server connection resets occurred only when Chrome closed idle HTTP connections during shutdown.
After the failed audit, only targeted label/focus/edge checks were run; the entire size set was not repeated.

## Frames looked at
Opened every captured PNG, including superseded frames:
- references/: both bar tools.
- initial/: default, worked Spot, Dispatch preview, Burn preview.
- sizes/: all seven standard desktop/tall sizes, compact Dispatch and Burn, grayscale Radio, Motion-off Burn.
- phone/: all four modes through a 375x812 iframe.
- checks/: crew arrival, solved Radio, solved Burn, keyboard arrival, voice side path, map-edge smoke.
- final/: Radio label fix, tall stacked layout, creek label, three phone label fixes, and final edge label.
Also inspected art-contact.jpg and bar-comparison.jpg. The final focused frames supersede the earlier clipped-label versions. No audit PNG existed.

## Art made
Seven missing assets generated using the built-in image tool, plus one smoke redraw; one existing dusk image preserved. Eight final images total, about 256.7 KB. Voice files: 0 KB. Bundle: about 582 KB, comfortably below the 2 MB goal.
The prompt set is art/prompts.json; originals are in art/raw/; final WebPs are in art/. Credit is in tool.draft.json. People is false on every asset.
The original magenta-keyed smoke had a colored fringe. It was redrawn as opaque gray on green and processed through scripts/art.py --rekey, as were the other new assets. No paid art.py generation or audio service was called.
The existing dusk image is used in the welcome and preview.svg; all other planned images are used at useful scene sizes.

## Art still to paint
None.

## Engine changes wanted
None.

## Left open
- Mechanical audit is unfinished because of the DevTools timeout. A later cold review must run it.
- The requested gravel-ranger recording is absent under the no-recording instruction; browser narration is available.
- D.9 derivation and D.10 proofs need a curriculum decision. No extra activity was improvised.
- Burn 2's viewport and Spot's rounded boundary convention differ from a literal reading of the spec; both are documented in handoff.md.
- All test Chrome profiles and servers belonging to this build were closed. Cleanup found no remaining owned process; host.html is absent. No shared source file was edited. No git operation, publication, or polish round was performed.

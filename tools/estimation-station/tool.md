# Estimation Station: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: estimation-station

#### Built
Offline Grade 2 Freight and Yard, using the kit starter, CSS, voice, chimes and motion preferences. Eight Freight jobs build from estimates and tool choice to curves, standing lengths, two units, ribbon differences and order slips. The finish is a personal eight-card delivery ledger, a train race and six first-choice tool stamps.
44 original paintings make the station, table, objects, train and Mr. Hollis. Responsive SVG supplies accurate tools, paths, ticks and equations. Source is readable, with a maximum line length of 148 characters. Draft stage is built.
Only tools/estimation-station/ and _scratch/estimation-station/ were written. No commits, recordings, publication or polish round. No family engine is specified. Temporary host pages were removed.
Process deviation: the restart's first read-only location/brief command lacked an explicit timeout. Subsequent commands use the bounded Scratch runner. No command was left hanging intentionally.

#### Numbers check
Evidence: Scratch verify_numbers.py, numbers.txt, regression-break.json and the final browser band check.
- Maximum: four ordinary jobs at 6, one two-unit job at 11, ribbons at 5 and two slips at 2 = 44. Starter ghost = 32.
- Slip answers: 63, 83, 63, 87, 72, 72, 55, 46, 45, 18, 27, 34, 25, 22, 54. All are within 100; all 15 regroup.
- Ribbon gaps: 12, 9, 16, 28, 27, 27. An inclusive 0 to 100 tape has 101 ticks.
- Explicit estimate bands win in order. At length 10, guesses 10, 11, 12, 13 and 15 give 3, 3, 2, 1 and 0 stars.
- The blanket claim that unit swaps always score zero is false under those bands: 3 for 1 inch earns 1 star; 1 for 2 centimeters earns 3. Numeric input cannot identify a child's intended unit. Formula retained and discrepancy handed off.
- Ordinary inch pools, uniform items and lengths: random 1 to 100 = 0.1143 stars; best fixed 5 = 1.1389; fixed 50 = 0. Centimeter pools: 0.1731, best fixed 8 = 0.8175, fixed 50 = 0. These restricted pools do not establish the spec's whole-run averages or its claimed no-skill run total.
- Recomputed contrast: white/brand 7.134, brand/paper 6.390, ink/paper 14.668, muted/paper 6.384, ink/gold 7.891, ink/tape 9.775, ink/wood 9.745, ink/table 8.112, white/blue 5.668, blue/paper 5.077. Ghost/paper 3.160 is for the secondary graphical ghost.

#### Facts checked
These are the complete factual claims; item and story lengths are fictional values, not physical benchmarks.
- 1 foot = 12 inches and 1 yard = 3 feet = 36 inches: NIST Handbook 44, Appendix C; NIST SP 811, Appendix B. Foot marks and yardstick use these relations.
- 1 meter = 100 centimeters: BIPM SI Brochure, prefixes; NIST SP 330. Meter ticks and two-unit measurements use this relation.
- The same length takes fewer larger units: CCSS 2.MD.2 and Common Core Standards Writing Team, Geometric Measurement K-5 Progressions (2012), Grade 2 section.
- Equally spaced ruler/number-line positions model sums and differences: CCSS 2.MD.6 and the same Progressions. Orders require a physical layout and a matching answer.
- CCSS 2.MD.1: student chooses, aligns, traces and repeats tools. 2.MD.2: measures the same object in two units. 2.MD.3: estimates before measuring. 2.MD.4: measures and subtracts ribbon lengths. 2.MD.5 and 2.MD.6: places pieces and solves within-100 stories on a marked tape. Wording follows the spec's named CCSS and Progressions sources.
- Tape endpoints of 60 inches and 150 centimeters are the specified model values. They are not exact physical equivalents. No cross-system conversion question or body-size benchmark was added.

#### Break it
Evidence: gameplay-results.json, keyboard-results.json, regression-break.json and regression-run.json. Browser fixtures inject cases but call the production controls and checks.
- Empty Check does nothing. Input caps at three digits. A correct typed length without aligned zero or completed trace fails; two attempts exhaust reading points.
- Edge/tick-count answer length + 1 fails. Wrong first tool followed by every tool cannot regain its stamp. Repeated Check after a result cannot farm points. Score commits once per result.
- 495 item/length suitability cases have a best working tool; no single tool wins all kinds. Curves reject sticks; standing objects reject tape; unsupported units reject a tool. Wrong choices show a recoiling stick or flopping tape and specific feedback.
- 30 two-unit lengths/directions pass at 11 points with chalk positions rescaled and preserved. Both big-to-small and small-to-big orders are tested.
- All 18 ribbon/tool combinations finish with readable shorter ends. Short rulers now rewind to an existing chalk mark for the blue reading. Difference checks reject both the sum and the longer length. The difference arc stays absent until checked.
- All 15 slips reject a self-consistent answer for the wrong layout. A correct story answer with the wrong layout also fails. Correct second attempts earn 1; correct first attempts earn 2. The layout gate was tightened after the answer-only bypass was found.
- A full mouse run and a real Tab/Enter/arrow-key run each earned 44, six stamps, Tool sense and eight saved job scores. Actual curve tracing and piece dragging were exercised. A final handler regression again earned 44.
- Abandoning a run never saves. A finished run becomes the next opponent; the active ghost is frozen so saving cannot change it retroactively. Tool sense requires six first-pick stamps. Tiny-object estimation remains easier under the required bands, as disclosed above.
- Yard has no points. Show me now demonstrates aligned zero, the asked tape face, completed tracing and the final measured piece; it cannot present a misaligned End reading as the answer.

#### Voice walk
The final default-settings walk completed eight jobs, 44 points and the Yard side path using real held clicks (0.12 s), two seconds between taps, actual curve tracing and tool dragging. Evidence: full-voice-walk.json and full-voice-walk.png. No runtime errors or warnings.
Spoken order: welcome began but was cut; Tape and trace instructions; readHow; correct first reading; later crate names/questions and tools; second-unit question/action; red reading, blue reading and difference question; order introductions and equations; delivered total, Starter comparison and endHow. Yard welcome, Inch ruler, alignment/Show me instruction, revealed length and Read followed.
The log exposes failures: guessHow was initially dropped and later cut; markHow was dropped as newer work arrived; both placeHow lines became stale. The full order stories were not heard before the placement inputs. Successful gameplay with a test harness that knows the answers is not evidence of independent pre-reader access.
First-crate held-click evidence remains in voice-walk.json: welcome began, then was cut by the student's Check; guessed number began and was cut by tool selection; Tape, trace instructions, readHow, correct reading, guess, stars and nextHow were heard in that order. Yard welcome, Show me and Read were heard on the side path. Sound off and back on were exercised.
Read now speaks the current hint and includes an unsolved order's story and current equation, plus the first reading before a second-unit guess. Yard has its own tool instructions and no longer queues a how line requiring its disabled Check.
The expanded recording inventory was reduced from an erroneous Cartesian catalogue to 6,583 reachable utterances/fragments. It no longer invents impossible item measurements or false filled story equations. Voice identity is gravel-ranger / Algenib. No audio was recorded; Chrome remained muted, so audible voice quality is unverified.
Known limitation: rapid progress can hush opening guessHow before it is heard. The complete pre-reader guarantee and exactly-once how-line guarantee are not claimed.

#### Feel check
Best moment: tracing a curved rope, bringing zero into place, then seeing the object load and the red train pull past the ghost. The final ledger shows the student's actual guesses, readings, equations and tool choices.
Flattest moment 1: an unsuitable tool only explained failure. Added a visible stiff-stick recoil or sagging tape, a low tone and Mr. Hollis pointing.
Flattest moment 2: the finish cramped its payoff. Freed the ending's unused controls and laid out eight recap cards with the earned badge and device-only line visible at 1366x768.
Compared Scratch bar-comparison.png: Estimation Station beside Snowy Mail Route and Beat Lab. The station's painted wood, lit platform, objects and train meet their visual finish without copying their scene or palette. The bars were bundled before implementation; browser opening succeeded later after launch retries, so the requested opening order was not fully met.
Later jobs introduce curves, repeated pieces, another unit, subtraction and story modeling. They require different actions rather than a longer sequence of identical guesses. Freight is untimed; Yard supports repeated free measuring.

#### Done when
1. PASS: work table dominates 1366x768; pad, Check, rack and active controls fit. Preview 680x425 has no page scroll and uses at least 10 px text. See sizes and final targeted frames.
2. FAIL against the literal universal wording: the five estimate jobs and second-unit guess show the correct bands and card, but explicit ribbon/slip flows have no guess. A true-size segment replaces a square when the square cannot fit. Both conflicts are recorded in handoff.md.
3. PASS: first-pick stamps, tool rejection and six-stamp badge verified by the tool cases and complete runs. Rack dimensions stay reserved.
4. FAIL in part: exact-reading, alignment, tracing and mark gates work, but standing tools intentionally start at the specified floor zero. A 150 px lens at 4x cannot show zero two large on-screen units away. It shows local graduations while approaching zero; no false rescaling was added.
5. PASS: all 30 two-unit cases pass in both directions, with correct replacement tool/face, preserved marks, big arcs, small ticks and both readings.
6. PASS with disclosed short-tool handling: the aligned origin stays fixed; shorter tools return to existing marks to read blue. All 18 cases pass; no premature difference arc.
7. PASS: all 15 stories and both layout families tested, including a real piece drag. Each equation has an unknown until checked and fills it afterward.
8. PASS: digit input responds during narration; tool and mode changes act immediately and hush older work. Audit rapid-tap and five-tap checks are clean. Generation guards prevent rejected-tool timers leaking into another crate.
9. FAIL / not established: pictures and words support every control and Read includes the current problem, but opening instructions can be hushed. No claim that a pre-reader completed eight jobs without reading.
10. PASS: Starter 32, completed per-job ghost, comparisons, end-only persistence, eight saved jobs and the device-only message verified.
11. FAIL literally: two attempts prevent five wrong Checks within one job. Extra Checks cannot score or replay stale feedback. readHow was heard; the complete once-each how requirement has remaining gaps.
12. PASS: calm train, load and arcs settle to their correct states. Audit finds no infinite motion. All resources are embedded; no tool network references or requests were observed.

#### Wave lessons
BR1 checks:
- Hint and voice: FAIL in part. Hint updates immediately and Read includes the task; kit heard/queue behavior is used. Opening how lines can still be hushed at a 2 s pace.
- Focus and layout: PASS for the tested controls. Check transfers focus when it becomes unavailable; Next transfers when hidden. No focus on load. Hint space is reserved; choices stay in place. Whole keyboard run passed.
- Sizes: PASS. All seven standard sizes, real 375 px host, both modes and targeted measuring/slip states inspected. Full laptop controls are 60 px; compact controls use the spec's 44 px exception.
- No giveaways: PASS for checks and stamps. Physical readiness and layout are required, attempts are limited and a first-tool stamp is irreversible. Estimation's stated tiny-length tolerance is retained.
- Honest numbers: PASS with disclosed scoring conflict. Asked units, nominal model scale, two-attempt points, star bands, device storage and Starter ghost are explicit. No unsupported mastery label.
- Standards: PASS. Each 2.MD.1 through 2.MD.6 code maps to student action above; no family engine was specified.
- Motion off: PASS. Calm frames checked; audit finds no infinite animation. All final art is present.
Network-help-desk lessons:
- Short choices visible: PASS. Five tools always visible; Yard's 36 objects use explicit pages, not a hidden short answer set.
- Resize mid-animation: PASS for the exercised states. Load animation retains its start time; audit found no exceptions. The final real 1366 to 760 to 1366 resizes retained the tape, face and visible Flip on two tool selections. The original audit lead was not reproduced.
- Late welcome: PASS for ordering, with a limitation. No welcomeAfter. New run deliberately interrupts the old welcome; it gives the new crate action, so the original premise can be missed.
- Unknown shown unknown: PASS. No measured length before Check or Show me, no filled answer before a result and no ribbon arc before difference checking.
- One look, one meaning: PASS. Red ribbon stripes, blue ribbon dots, grey dashed ghost and checked tool stamp remain distinct in grayscale.
- Badge says what is true: PASS. Tool sense means six first-choice stamps; a wrong first tool cannot recover one.
- Hint changes back: PASS. Mode/item/tool changes reset contextual hints and errors; Read uses the current hint.
- No copying words: PASS for score gates. Stories require layout and arithmetic; reading requires a physical instrument action. No answer word is printed in a selectable answer list.

#### Audit leads
Ran audit_tool.py exactly once, last after the full size pass. It finished with 164 mechanical leads; all 41 audit PNGs were inspected. Full evidence: Scratch audit/audit.md. Post-audit fixes received targeted checks, not another audit or size sweep.
- All size/state board-versus-step/card/bold-name overlap rows: intentional overlay of noninteractive labels on the keyboard-operable SVG board. They do not cover another button or hidden choice. Keyboard focus and actual targets remain usable.
- All hint keep-region rows: the portrait floats within the hint region's rectangle. Text wraps alongside it; sampled points hitting the portrait do not mean covered text. Frames at each flagged size were inspected.
- Rack-open card coverage at all sizes: false positive from the noninteractive card's pointer-events: none. Hit testing reaches the SVG underneath although the card is visibly on top. The card, reserved rack and hint remain visible in the actual frames.
- Measuring board keep-region sample at 680: a foreground crate and scene labels sit on the SVG. Actual controls remain outside the scene, usable and visible.
- Clipped ruler numerals and foot labels: true-proportion long tools extend beyond the work surface, by design. The local lens supplies the needed area. Labels at circle edges were genuinely clipped; fixed with circle-aware placement and spacing. Checked final preview lenses and short-ruler frame.
- Start label versus step tag at 375: fixed by lowering the compact Start lens; final phone/preview frames inspected.
- Yard numeral versus duplicate measured text: genuine overlap. Removed the redundant bottom readout; the card retains the answer. Both compact Yard frames rechecked.
- Yard readHow dropped with no input, and the three tool-choice variants requiring disabled Check: fixed with Yard-specific tool instructions and no Freight readHow scheduling in Yard. Show me remains the named action.
- Resize left Flip disabled: not reproduced in the final real viewport test. Two tape selections retained tool=tape, face=inches and hidden=false at 760x900 and back at 1366x768, with no exceptions. No source mutation disables Flip. The audit's randomized before/after trace may choose different working tools; retain the lead for independent review if it recurs.
- New run first-tap welcome not heard: retained action-first interruption. New crate and next action are spoken; full premise may be missed. Listed under voice limitations rather than marked clean.
- Board click in Yard changes nothing: it is the keyboard/pointer measuring surface, not a standalone action. With a selected tool or piece it accepts dragging and arrow keys. Kept focusable for access.
- Held-click row saying "A eraser": corrected to "An eraser" and updated inventory.
- Mode movement counts are expected mode reflow. Single controls settled with Enter twice; five held clicks and 0.7 s double taps were clean. Motion-off stage was clean. No other actionable lead remains unaccounted for.

#### Frames looked at
Scratch: all final-art-0 through 3 sheets and the people sheet; gameplay and keyboard runs; every sizes and modes output; phone freight/Yard and real slip drag; final's seven targeted frames; all seven audit contact sheets covering 41 audit PNGs; bar-comparison.png; voice-walk.png; all six regression PNGs; both yard-final PNGs; notebook-phone-verified.png and notebook-public-path.png.
The first notebook injected fixture updated the SVG but left a stale card, a fixture limitation. The public-path frame uses shelf paging and selection, shows Notebook with its centimeter reading, and confirms the paint is present at 375 px. Phone retry and final batches report zero console errors/warnings. Earlier driver failures are preserved in Scratch; they are not counted as passes.
The final full-voice-walk.png was also opened and inspected. Its JSON records eight jobs, 44 points, clean runtime logs and the real resize results. All Chrome instances owned by the test commands and all host servers were closed.

#### Art made
44 original generated paintings, all drawn_by: codex, each processed using art.py --rekey. Finished WebP art totals 1,423,334 bytes, about 1,390 KiB. Quality is 72. Raw originals and complete prompts remain in art/raw and art/prompts.json.
Three Mr. Hollis poses are marked people: true. The snake head was redrawn once because the first version included an unwanted coiled body. All specified art is referenced; exact tools and diagrams use SVG.
Final bundle: 2,101,402 bytes, about 2,052 KiB, just above the 2 MiB goal. Voice recordings: 0 KB. Text inventory: about 309 KiB, 6,583 entries. Images were retained because they teach and give the scene its character; the bundle is far below 6 MB.

#### Art still to paint
None. Independent representation review of the three people poses remains for the separate cold review; this Build does not claim it occurred. Contact sheet is in Scratch.

#### Engine changes wanted
None. No kit, docs, shared scripts or other tool was intentionally changed. A digit-key limitation in the shot helper was handled in a Scratch keyboard harness, not by changing the engine.

#### Left open
- The literal square/fill/lens requirements conflict geometrically at tiny lengths; standing zero, ribbon/slip guesses and two-unit direction wording conflict elsewhere. Exact choices are in handoff.md.
- Guessing averages and the no-skill whole-run score claim lack a disclosed weighting; only the computations stated here are claimed. Tiny unit swaps can earn stars under the required formula.
- Opening how-line interruption and the complete pre-reader guarantee remain unproven. The five-wrong-Checks requirement conflicts with two tries. Audible browser voice quality is unverified; no recordings were authorized.
- The audit's original Flip availability lead did not recur during the final same-tool resize test; retain it for independent review if it recurs.
- Fresh people representation review belongs to the later cold review. No print-and-carry feature was added. No unresolved owner question was listed in the spec; the options it leans toward were taken and documented.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: estimation-station

#### Played
Before reading the builder's account, completed a cold Grade 2 eight-job poor run and Yard. Later played carefully to 44 points as a solo learner and projector operator. Rich, tactile and varied; curve tracing and the loaded-train race are strongest. Checks covered both modes at every required size, real tool/piece drags, keyboard play, grayscale and Motion off.

#### Findings fixed
- **Blocker, general, estimate input:** zero-only taps could earn maximum stars on a one-unit object. Positive guesses are now required; zero keeps the guess open without points. Accepted-guess bands are unchanged.
- **Blocker, general, second estimate:** the first tool could expose the next unit's answer through smaller-unit numerals or foot labels. Those secondary-unit answers now stay hidden until the second guess is checked, in both directions.
- **Should fix, general, narration:** opening, placement and Next cues could disappear behind longer lines. Short cues receive priority; a story survives placement; timers are canceled across jobs/modes and restricted to reading steps. Old results stop when Next changes the scene.
- **Should fix, general, Yard events:** five Show me taps produced only three spoken reveals behind the welcome. Reveal events now take priority while Read retains the kit's priority. Five reveals now start five events; five tool selections speak five names and one how-to.
- **Should fix, general, measurement:** long rulers could have only zero numbered. Labels thin with scale while every tick and longer fifth marks remain; standing-tool chalk labels sit beside the ruler. A skipped measured piece receives Mark and move feedback instead of an incorrect zero warning.
- **Should fix, general, score feedback:** the two-unit card showed only the first estimate's stars. It now distinguishes First and Then, checked with zero versus three stars and an eight-point job.
- **Should fix, general, focus:** Next and the final Mark could hide the focused button; responsive Yard rebuilding could lose the selected item. Focus now transfers before those controls disappear and follows the same shelf item across resizing.
- **Should fix, general, compact graphics:** the End lens could touch the crate card, the ribbon gap label clipped, and unit-comparison text/arcs crossed other content. Lenses, arcs and the compact comparison placard now have separate room.
- **Should fix, audit, Yard/layout:** choosing another tool left the previous checked answer visible; it now clears. The compact order paper hid the first ribbon number; the bars now fit below it (5 px clear at 680).
- **Should fix, wave lesson, resize:** an active drag reused its old pixel anchor after scale changed. A stationary pointer could move the measurement. Resize now ends the gesture and preserves its unit position; the identical physical test fails on the audit snapshot and passes on the final bundle.
- **Polish, general, payoff/art:** a successful ribbon animated its teaching arc away. Both patterned ribbons and the labeled difference now stay visible. Redrew the flat tool icons and lens rims with grain, shading, metal tips and readable capacity captions.
- **Polish, general:** corrected scissors grammar and Back's invalid tone frequency. Notes, narration inventory, handoff and audit states were updated.

#### Findings left
- **Polish, spec constraint:** short-object tolerances remain generous, and a numerically close estimate cannot reveal which unit the child intended. A small-object star is not proof of estimation mastery.
- **Polish, spec constraint:** eight Right nudges align the specified fixed lying-tool start. This shortcut was exercised; the reading still needs the correct number, face and completed pieces. No separate alignment-mastery badge is claimed.
- **Nit, art:** a faint keyed edge remains around parts of Mr. Hollis's hair. Keep the strong portraits; the representation review should also inspect their cutouts.

#### Break it
- **Guess stars:** tested exact, one-unit, 20/30/50-percent errors, repeated digits and zero. Three-digit limit and empty Check hold; held zero/Check and public-handler zero probes earn nothing. Positive bands at length ten give 3, 3, 2, 1, 0 stars for 10, 11, 12, 13, 15.
- **First-tool stamp / Tool sense:** tried wrong-first then every tool, repeated selections, all 25 representative physical tool choices and 495 suitability cases. A lost stamp never returns; no single tool wins every kind. Six first-pick stamps were earned in the legitimate keyboard run.
- **Reading points:** copied the correct value before alignment/tracing, entered length plus one twice, changed tools between attempts, skipped a measured piece, used the wrong tape face and mashed Check after completion. These fail or lose the intended attempt; changing tools cannot reset attempts and results cannot farm points.
- **Second unit:** copied the first number into the second estimate/read and tried copying smaller-unit tool numerals. These fail. All 30 lengths/directions complete correctly at eleven points; marks remain in matching physical positions.
- **Ribbon:** tried the sum and the longer ribbon as the difference; both fail. No answer arc appears before the check; reading points remain separate and limited.
- **Order slips:** all 15 correct story answers fail in the wrong layout. A self-consistent answer to the wrong equation also fails. Correcting layout on try two earns one point. A real drag to zero was accepted.
- **Race / saved best:** repeated completed Checks cannot increase the score; abandoned runs do not replace the ghost. Proper mouse and keyboard runs earned 44. A deliberately weak completed opponent can be beaten easily; the comparison is personal, not a mastery certificate.
- **Yard:** Show me is intentionally an unscored reveal, not a gate. There is no reflection gate.
Evidence: Scratch review-cheats-post-audit.json (26 passing probes), review-keyboard.json, review-zero-held.json and review-main-voice.json.

#### Voice walk
Held 0.12-second clicks, two-second tap spacing, default Sound/Motion, physical curve/tool drags: guess, rack, align/trace, read, Next; both units; red, blue, difference; two stories and placements; delivery; Yard, tool, Show me, Read. Let each story narration reach its question before answering.
Final run: eight jobs, 44 points, no runtime errors. The welcome may be skipped by the first action, as BASELINE 16 allows.

| Cue | Kind | Expected | Started |
|---|---|---:|---:|
| guessHow | how | 1 | 1 |
| toolAlign | how | 1 | 1 |
| nextHow | how | 1 | 1 |
| markHow | how | 1 | 1 |
| readHow | how | 1 | 1 |
| trace | how | 1 | 1 |
| placeHow | how | 1 | 1 |
| endHow | how | 1 | 1 |
| yardWelcome | welcome | 1 | 1 |
| yardMeasure | how | 1 | 1 |
| Yard reveal | event | 5 | 5 |
| Tool name | event | 5 | 5 |

Read interrupts speech, works with Sound off, and releases on a mode change. Rapid transitions do not replay older work. The table follows first-spoken order; readHow was dropped on the first fast reading and heard after Mark on the next job. Counts measure starts, not uncut completions: advancing can interrupt result detail. Muted testing does not establish audible narrator quality or a child's independent comprehension. Every observed spoken line is in the inventory.

#### Facts checked
- **12 inches per foot, 3 feet / 36 inches per yard; inch/centimeter and foot/centimeter factors:** [NIST SP 811, Appendix B](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors), cross-checked against NIST Handbook 44 Appendix C.
- **100 centimeters per meter:** [BIPM SI prefixes](https://www.bipm.org/en/measurement-units/si-prefixes), centi factor 0.01; agrees with NIST SP 330.
- **Larger units give fewer counts:** derived from those NIST/BIPM ratios, matching the relationship required by CCSS 2.MD.2.
- **Selecting rulers, yardsticks, meter sticks and tapes; estimating the four units; length differences; within-100 stories and equally spaced number lines:** [CCSS Grade 2 Measurement and Data, 2.MD.1 through 2.MD.6](https://www.thecorestandards.org/Math/Content/2/MD/). Each has an activity in the played run.
- **Scenario arithmetic:** independently recomputed all 15 answers (63, 83, 63, 87, 72, 72, 55, 46, 45, 18, 27, 34, 25, 22, 54), six ribbon gaps (12, 9, 16, 28, 27, 27), 101 tape ticks, maximum 44 and Starter 32 against spec Content. Object lengths and nominal tape endpoints are model givens, not physical benchmarks.

#### Sensitivity
Mr. Hollis is the knowledgeable older Black station master, portrayed warmly and consistently. All three poses are marked people: true. A fresh representation lens should inspect hands, expressions, cutout edges and the generic rug decoration; no named cultural tradition, body, religion or historical claim is taught.

#### Flattest moment left
Yard's reveal is a static answer rather than a dramatic payoff. It remains appropriate for untimed free measuring; Freight supplies the earned train and personal ledger. The formerly flat ribbon finish is now a persistent comparison.

#### Graphics
Checked all 44 paintings through the art/people sheets and in-tool frames, plus tools, lenses, curves, ribbons, slips and end cards. Preserved the warm station, objects, three portraits and train. Redrew code art only; no missing painted assets or unmarked people were found. Final bundle: 2,106 KB (2,105,724 bytes); 44 paintings, 3 people assets. Compared the station with the existing Snowy Mail Route bar frame without simplifying its look.

#### Audit
Ran scripts/audit_tool.py once, on Chrome 9961 / host 8765, with a 40-minute cap; finished in about 30 minutes with 209 mechanical leads. Viewed all 44 captured frames. Confirmed and repaired the compact order overlap, crowded standing-ruler labels and stale Yard reveal, then re-shot affected sizes. Other leads were board/panel layering, the intentionally covered crate card during rack choice, offscreen portions of a long ruler, recap scrolling over the background tape, and action-first welcome interruptions allowed by BASELINE 16. Held-click, five-click, double-tap and mid-action resize exception/disabled-control checks were clean. The dedicated drag check found the additional unit-position defect described above.
Wave lessons were checked directly: current hints/Read, once-only cues, stable focus, all five rack choices in view, accurate feedback, no answer-copy shortcut, every standard practiced, grayscale meanings, Motion off, state restoration and resizing during actual tool use. The audit could not obtain its phone iframe context because an earlier review host still owned port 8765. Identified and terminated that exact owned process, then manually re-shot all seven omitted phone states on the correct host. Phone verification is a targeted replacement, not a successful automated phone audit. The bundled tool has no external resources or network calls.

#### Left open
Unattended choices follow the brief: positive guess domain, explicit scoring bands, ribbon/slip flows without added guesses, both two-unit directions, a truthful unit segment when a square cannot fit, the spec's compact 44-pixel exception, and action-first narration. Very large on-screen units cannot both fit inside a 150-pixel lens at true 4x; standing tools start at the specified floor zero. These spec tensions were not hidden by changing scale or adding features. No engine changes or commits.
The first location/brief read lacked an explicit command timeout; subsequent commands were bounded. An initial play-driver choice loop and the keyboard driver's Enter encoding were corrected; failed harness attempts remain in Scratch. The audit was run once, last. No second full review or polish round was started.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Estimation Station handoff

#### Build
One offline HTML tool, Freight and Yard. Source starts from the kit starter, uses kit CSS, Curio.voice, Curio.init and kit chimes. No family engine is specified. No commits, publication, recordings or polish round.

#### Source map
The source contains responsive station CSS, a persistent header/panel, content and art maps, the Freight state machine, tool suitability and scoring, SVG drawing, and pointer/keyboard input. content.json is loaded through the bundler's json token. Art uses art tokens only. voice/lines.json holds expanded utterances and the requested gravel-ranger / Algenib recording identity; current audio uses browser fallback.

state.offset and state.moved are in the asked unit, so resizing preserves a placement. The native ruler ticks stay in inches or centimeters even when the question asks for feet or meters. Curves use sampled arc length. The first choice fixes a stamp once. Checks require physical readiness as well as a typed reading. A result is committed once; abandoned runs never write storage. The ghost is frozen at run start so saving a finished run cannot change its opponent retroactively.

Short tools on a ribbon pair return to an existing chalk mark when needed to read the shorter ribbon. The initial zero alignment is preserved. The two-unit turn rescales existing mark positions and labels rather than erasing the marks. Yard's Show me demonstrates aligned zero, the asked face and the final measured piece. Read includes the current question and, for an unsolved order, the story and current equation.

#### Spec choices and discrepancies
- No unanswered owner questions are listed. No print-and-carry feature was added.
- Two-unit descriptions list fixed directions but Done when asks for both directions. Each chosen two-unit item randomizes direction.
- Under the disclosed uniform-item, uniform-length weighting, ordinary inch and centimeter pools give different guessing averages from the Sources commentary. See Scratch numbers.txt; those narrow pools do not establish the whole-run average. The explicit bands win; very short objects remain intentionally easy.
- Its blanket unit-swap-zero claim conflicts with those bands on tiny lengths. A guess of 3 for a 1-inch item earns 1 star; a guess of 1 for 2 centimeters earns 3. Numeric guesses cannot reveal which unit a child had in mind. The explicit scoring formula is preserved.
- The cold review accepts positive guesses only. All content lengths and the spec's random-guess domain are positive. A zero-only tap shortcut now stays at the guess step without points; the explicit bands are unchanged for accepted guesses. This is the unattended interpretation of the input domain.
- All 15 slips regroup. All answers and ribbon gaps recompute correctly.
- A one-unit square beside a 1-inch object filling most of the scene cannot also fit at that scale. Such cases use an accurate one-unit segment, with no misleading rescaled square. Broad objects keep their aspect ratio, which can reduce the requested 55 to 80 percent width fill.
- A 150-pixel lens at 4 times magnification cannot show both points when zero starts 2 large on-screen units away. It shows local graduations as zero approaches. Exact magnification and placement are preserved; Nudge remains available.
- Ribbon and order jobs follow their explicit flows without an estimate; the generic instruction that every crate begins with a guess applies to the first five jobs and the second-unit estimate.
- Check requires a matching order layout as well as the story answer. Otherwise typing the correct story answer without modeling the story bypasses the number-line action.
- The scene reflows recap cards into rows. Small recap panels scroll while New run and Yard remain available.
- The preview and phone use 44-pixel pad/control targets as the explicit spec permits. The full laptop controls use 60 pixels.
- The five-wrong-Checks voice instruction conflicts with the two-attempt limit within one job. Extra Checks after a result do nothing and cannot add points.
- The tape's nominal end marks are 60 inches and 150 centimeters as specified. Those marks are not exact physical equivalents. Cross-system conversions are not taught.
- BUILD.md's older "Do not draw art" line and the spec's Gemini routing conflict with the user's image-tool request and CODEX-BUILD.md. The user request and CODEX-BUILD.md win: OpenAI gpt-image was used, including for people, as ART.md permits.

#### Sensitivity
Mr. Hollis is a friendly older Black station master. All three people assets are marked people: true. He is shown as the knowledgeable guide, with consistent attire and dignified expressions. There are no claims about culture, bodies, religion or history. The three poses are on _scratch/estimation-station/people-contact-sheet.png for the owner and the fresh representation check in the later cold review. This Build does not claim that independent review has happened.

#### Art
44 original generated paintings, processed only with art.py --rekey. Snake head was redrawn once to remove an unwanted whole coiled body. All specified images are referenced. Raw originals remain in art/raw as the build brief requests. Final art sheets and the people contact sheet are in Scratch. Art credit is in tool.draft.json and the source comment.

#### Engine changes wanted
None. No kit, docs, scripts or other tool was intentionally edited.

#### Remaining voice limits
The cold review gives the first number tap its short guess instruction and gives the first result its Next cue before optional result detail. How lines use the kit's heard set; tool names remain repeatable events. Order introduction and placement share a scope so placing a piece does not discard its story. Read still includes the current story and equation. Next interrupts obsolete narration as its new crate appears. The first welcome can be skipped, consistent with BASELINE 16.

See codex-review.md and Scratch review-main-voice.json for the final held-click walk and observed counts. Recorded speech is still absent. Muted Chrome establishes queue behavior, not audible narrator quality or an independently observed child's comprehension. A student listening to an order must have time to hear its story before answering; the review waits for that question while keeping taps two seconds apart.

#### Cold review repairs

The second estimate keeps the first unit's markings and hides secondary-unit numerals in both directions. Correct ribbon results retain the ribbons and their comparison arc. Tool icons now have shaded wood, metal, grain and readable capacity captions. Ruler labels thin with scale while every tick remains; standing-tool chalk labels stay beside the ruler. Skipping an outstanding measured piece receives Mark and move feedback instead of a false zero-alignment warning. Yard preserves the focused item across responsive shelf rebuilding and clears its previous answer when another tool is selected. Compact order bars sit below their paper. Resizing ends an active drag while preserving its unit position. Scissors grammar and Back's feedback tone were corrected.

Audit states now include a deterministic measuring fixture, a placed order, a ribbon result and a complete delivery. Test setup uses the existing content and production handlers; the separate voice walk uses held physical input through all eight jobs. No shared engine was changed.

#### Next review
See codex-report.md for the builder's checks and codex-review.md for the separate cold review, repairs, evidence and remaining limitations. Keep this at Build until Refine.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-07)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-07)
- 2026-11-25: handoff.md folded in (last changed 2026-11-07)

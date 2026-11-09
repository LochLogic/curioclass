# Codex report: estimation-station

## Built
Offline Grade 2 Freight and Yard, using the kit starter, CSS, voice, chimes and motion preferences. Eight Freight jobs build from estimates and tool choice to curves, standing lengths, two units, ribbon differences and order slips. The finish is a personal eight-card delivery ledger, a train race and six first-choice tool stamps.
44 original paintings make the station, table, objects, train and Mr. Hollis. Responsive SVG supplies accurate tools, paths, ticks and equations. Source is readable, with a maximum line length of 148 characters. Draft stage is built.
Only tools/estimation-station/ and _scratch/estimation-station/ were written. No commits, recordings, publication or polish round. No family engine is specified. Temporary host pages were removed.
Process deviation: the restart's first read-only location/brief command lacked an explicit timeout. Subsequent commands use the bounded Scratch runner. No command was left hanging intentionally.

## Numbers check
Evidence: Scratch verify_numbers.py, numbers.txt, regression-break.json and the final browser band check.
- Maximum: four ordinary jobs at 6, one two-unit job at 11, ribbons at 5 and two slips at 2 = 44. Starter ghost = 32.
- Slip answers: 63, 83, 63, 87, 72, 72, 55, 46, 45, 18, 27, 34, 25, 22, 54. All are within 100; all 15 regroup.
- Ribbon gaps: 12, 9, 16, 28, 27, 27. An inclusive 0 to 100 tape has 101 ticks.
- Explicit estimate bands win in order. At length 10, guesses 10, 11, 12, 13 and 15 give 3, 3, 2, 1 and 0 stars.
- The blanket claim that unit swaps always score zero is false under those bands: 3 for 1 inch earns 1 star; 1 for 2 centimeters earns 3. Numeric input cannot identify a child's intended unit. Formula retained and discrepancy handed off.
- Ordinary inch pools, uniform items and lengths: random 1 to 100 = 0.1143 stars; best fixed 5 = 1.1389; fixed 50 = 0. Centimeter pools: 0.1731, best fixed 8 = 0.8175, fixed 50 = 0. These restricted pools do not establish the spec's whole-run averages or its claimed no-skill run total.
- Recomputed contrast: white/brand 7.134, brand/paper 6.390, ink/paper 14.668, muted/paper 6.384, ink/gold 7.891, ink/tape 9.775, ink/wood 9.745, ink/table 8.112, white/blue 5.668, blue/paper 5.077. Ghost/paper 3.160 is for the secondary graphical ghost.

## Facts checked
These are the complete factual claims; item and story lengths are fictional values, not physical benchmarks.
- 1 foot = 12 inches and 1 yard = 3 feet = 36 inches: NIST Handbook 44, Appendix C; NIST SP 811, Appendix B. Foot marks and yardstick use these relations.
- 1 meter = 100 centimeters: BIPM SI Brochure, prefixes; NIST SP 330. Meter ticks and two-unit measurements use this relation.
- The same length takes fewer larger units: CCSS 2.MD.2 and Common Core Standards Writing Team, Geometric Measurement K-5 Progressions (2012), Grade 2 section.
- Equally spaced ruler/number-line positions model sums and differences: CCSS 2.MD.6 and the same Progressions. Orders require a physical layout and a matching answer.
- CCSS 2.MD.1: student chooses, aligns, traces and repeats tools. 2.MD.2: measures the same object in two units. 2.MD.3: estimates before measuring. 2.MD.4: measures and subtracts ribbon lengths. 2.MD.5 and 2.MD.6: places pieces and solves within-100 stories on a marked tape. Wording follows the spec's named CCSS and Progressions sources.
- Tape endpoints of 60 inches and 150 centimeters are the specified model values. They are not exact physical equivalents. No cross-system conversion question or body-size benchmark was added.

## Break it
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

## Voice walk
The final default-settings walk completed eight jobs, 44 points and the Yard side path using real held clicks (0.12 s), two seconds between taps, actual curve tracing and tool dragging. Evidence: full-voice-walk.json and full-voice-walk.png. No runtime errors or warnings.
Spoken order: welcome began but was cut; Tape and trace instructions; readHow; correct first reading; later crate names/questions and tools; second-unit question/action; red reading, blue reading and difference question; order introductions and equations; delivered total, Starter comparison and endHow. Yard welcome, Inch ruler, alignment/Show me instruction, revealed length and Read followed.
The log exposes failures: guessHow was initially dropped and later cut; markHow was dropped as newer work arrived; both placeHow lines became stale. The full order stories were not heard before the placement inputs. Successful gameplay with a test harness that knows the answers is not evidence of independent pre-reader access.
First-crate held-click evidence remains in voice-walk.json: welcome began, then was cut by the student's Check; guessed number began and was cut by tool selection; Tape, trace instructions, readHow, correct reading, guess, stars and nextHow were heard in that order. Yard welcome, Show me and Read were heard on the side path. Sound off and back on were exercised.
Read now speaks the current hint and includes an unsolved order's story and current equation, plus the first reading before a second-unit guess. Yard has its own tool instructions and no longer queues a how line requiring its disabled Check.
The expanded recording inventory was reduced from an erroneous Cartesian catalogue to 6,583 reachable utterances/fragments. It no longer invents impossible item measurements or false filled story equations. Voice identity is gravel-ranger / Algenib. No audio was recorded; Chrome remained muted, so audible voice quality is unverified.
Known limitation: rapid progress can hush opening guessHow before it is heard. The complete pre-reader guarantee and exactly-once how-line guarantee are not claimed.

## Feel check
Best moment: tracing a curved rope, bringing zero into place, then seeing the object load and the red train pull past the ghost. The final ledger shows the student's actual guesses, readings, equations and tool choices.
Flattest moment 1: an unsuitable tool only explained failure. Added a visible stiff-stick recoil or sagging tape, a low tone and Mr. Hollis pointing.
Flattest moment 2: the finish cramped its payoff. Freed the ending's unused controls and laid out eight recap cards with the earned badge and device-only line visible at 1366x768.
Compared Scratch bar-comparison.png: Estimation Station beside Snowy Mail Route and Beat Lab. The station's painted wood, lit platform, objects and train meet their visual finish without copying their scene or palette. The bars were bundled before implementation; browser opening succeeded later after launch retries, so the requested opening order was not fully met.
Later jobs introduce curves, repeated pieces, another unit, subtraction and story modeling. They require different actions rather than a longer sequence of identical guesses. Freight is untimed; Yard supports repeated free measuring.

## Done when
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

## Wave lessons
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

## Audit leads
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

## Frames looked at
Scratch: all final-art-0 through 3 sheets and the people sheet; gameplay and keyboard runs; every sizes and modes output; phone freight/Yard and real slip drag; final's seven targeted frames; all seven audit contact sheets covering 41 audit PNGs; bar-comparison.png; voice-walk.png; all six regression PNGs; both yard-final PNGs; notebook-phone-verified.png and notebook-public-path.png.
The first notebook injected fixture updated the SVG but left a stale card, a fixture limitation. The public-path frame uses shelf paging and selection, shows Notebook with its centimeter reading, and confirms the paint is present at 375 px. Phone retry and final batches report zero console errors/warnings. Earlier driver failures are preserved in Scratch; they are not counted as passes.
The final full-voice-walk.png was also opened and inspected. Its JSON records eight jobs, 44 points, clean runtime logs and the real resize results. All Chrome instances owned by the test commands and all host servers were closed.

## Art made
44 original generated paintings, all drawn_by: codex, each processed using art.py --rekey. Finished WebP art totals 1,423,334 bytes, about 1,390 KiB. Quality is 72. Raw originals and complete prompts remain in art/raw and art/prompts.json.
Three Mr. Hollis poses are marked people: true. The snake head was redrawn once because the first version included an unwanted coiled body. All specified art is referenced; exact tools and diagrams use SVG.
Final bundle: 2,101,402 bytes, about 2,052 KiB, just above the 2 MiB goal. Voice recordings: 0 KB. Text inventory: about 309 KiB, 6,583 entries. Images were retained because they teach and give the scene its character; the bundle is far below 6 MB.

## Art still to paint
None. Independent representation review of the three people poses remains for the separate cold review; this Build does not claim it occurred. Contact sheet is in Scratch.

## Engine changes wanted
None. No kit, docs, shared scripts or other tool was intentionally changed. A digit-key limitation in the shot helper was handled in a Scratch keyboard harness, not by changing the engine.

## Left open
- The literal square/fill/lens requirements conflict geometrically at tiny lengths; standing zero, ribbon/slip guesses and two-unit direction wording conflict elsewhere. Exact choices are in handoff.md.
- Guessing averages and the no-skill whole-run score claim lack a disclosed weighting; only the computations stated here are claimed. Tiny unit swaps can earn stars under the required formula.
- Opening how-line interruption and the complete pre-reader guarantee remain unproven. The five-wrong-Checks requirement conflicts with two tries. Audible browser voice quality is unverified; no recordings were authorized.
- The audit's original Flip availability lead did not recur during the final same-tool resize test; retain it for independent review if it recurs.
- Fresh people representation review belongs to the later cold review. No print-and-carry feature was added. No unresolved owner question was listed in the spec; the options it leans toward were taken and documented.

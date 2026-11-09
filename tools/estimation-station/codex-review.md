# Codex review: estimation-station

## Played
Before reading the builder's account, completed a cold Grade 2 eight-job poor run and Yard. Later played carefully to 44 points as a solo learner and projector operator. Rich, tactile and varied; curve tracing and the loaded-train race are strongest. Checks covered both modes at every required size, real tool/piece drags, keyboard play, grayscale and Motion off.

## Findings fixed
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

## Findings left
- **Polish, spec constraint:** short-object tolerances remain generous, and a numerically close estimate cannot reveal which unit the child intended. A small-object star is not proof of estimation mastery.
- **Polish, spec constraint:** eight Right nudges align the specified fixed lying-tool start. This shortcut was exercised; the reading still needs the correct number, face and completed pieces. No separate alignment-mastery badge is claimed.
- **Nit, art:** a faint keyed edge remains around parts of Mr. Hollis's hair. Keep the strong portraits; the representation review should also inspect their cutouts.

## Break it
- **Guess stars:** tested exact, one-unit, 20/30/50-percent errors, repeated digits and zero. Three-digit limit and empty Check hold; held zero/Check and public-handler zero probes earn nothing. Positive bands at length ten give 3, 3, 2, 1, 0 stars for 10, 11, 12, 13, 15.
- **First-tool stamp / Tool sense:** tried wrong-first then every tool, repeated selections, all 25 representative physical tool choices and 495 suitability cases. A lost stamp never returns; no single tool wins every kind. Six first-pick stamps were earned in the legitimate keyboard run.
- **Reading points:** copied the correct value before alignment/tracing, entered length plus one twice, changed tools between attempts, skipped a measured piece, used the wrong tape face and mashed Check after completion. These fail or lose the intended attempt; changing tools cannot reset attempts and results cannot farm points.
- **Second unit:** copied the first number into the second estimate/read and tried copying smaller-unit tool numerals. These fail. All 30 lengths/directions complete correctly at eleven points; marks remain in matching physical positions.
- **Ribbon:** tried the sum and the longer ribbon as the difference; both fail. No answer arc appears before the check; reading points remain separate and limited.
- **Order slips:** all 15 correct story answers fail in the wrong layout. A self-consistent answer to the wrong equation also fails. Correcting layout on try two earns one point. A real drag to zero was accepted.
- **Race / saved best:** repeated completed Checks cannot increase the score; abandoned runs do not replace the ghost. Proper mouse and keyboard runs earned 44. A deliberately weak completed opponent can be beaten easily; the comparison is personal, not a mastery certificate.
- **Yard:** Show me is intentionally an unscored reveal, not a gate. There is no reflection gate.
Evidence: Scratch review-cheats-post-audit.json (26 passing probes), review-keyboard.json, review-zero-held.json and review-main-voice.json.

## Voice walk
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

## Facts checked
- **12 inches per foot, 3 feet / 36 inches per yard; inch/centimeter and foot/centimeter factors:** [NIST SP 811, Appendix B](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors), cross-checked against NIST Handbook 44 Appendix C.
- **100 centimeters per meter:** [BIPM SI prefixes](https://www.bipm.org/en/measurement-units/si-prefixes), centi factor 0.01; agrees with NIST SP 330.
- **Larger units give fewer counts:** derived from those NIST/BIPM ratios, matching the relationship required by CCSS 2.MD.2.
- **Selecting rulers, yardsticks, meter sticks and tapes; estimating the four units; length differences; within-100 stories and equally spaced number lines:** [CCSS Grade 2 Measurement and Data, 2.MD.1 through 2.MD.6](https://www.thecorestandards.org/Math/Content/2/MD/). Each has an activity in the played run.
- **Scenario arithmetic:** independently recomputed all 15 answers (63, 83, 63, 87, 72, 72, 55, 46, 45, 18, 27, 34, 25, 22, 54), six ribbon gaps (12, 9, 16, 28, 27, 27), 101 tape ticks, maximum 44 and Starter 32 against spec Content. Object lengths and nominal tape endpoints are model givens, not physical benchmarks.

## Sensitivity
Mr. Hollis is the knowledgeable older Black station master, portrayed warmly and consistently. All three poses are marked people: true. A fresh representation lens should inspect hands, expressions, cutout edges and the generic rug decoration; no named cultural tradition, body, religion or historical claim is taught.

## Flattest moment left
Yard's reveal is a static answer rather than a dramatic payoff. It remains appropriate for untimed free measuring; Freight supplies the earned train and personal ledger. The formerly flat ribbon finish is now a persistent comparison.

## Graphics
Checked all 44 paintings through the art/people sheets and in-tool frames, plus tools, lenses, curves, ribbons, slips and end cards. Preserved the warm station, objects, three portraits and train. Redrew code art only; no missing painted assets or unmarked people were found. Final bundle: 2,106 KB (2,105,724 bytes); 44 paintings, 3 people assets. Compared the station with the existing Snowy Mail Route bar frame without simplifying its look.

## Audit
Ran scripts/audit_tool.py once, on Chrome 9961 / host 8765, with a 40-minute cap; finished in about 30 minutes with 209 mechanical leads. Viewed all 44 captured frames. Confirmed and repaired the compact order overlap, crowded standing-ruler labels and stale Yard reveal, then re-shot affected sizes. Other leads were board/panel layering, the intentionally covered crate card during rack choice, offscreen portions of a long ruler, recap scrolling over the background tape, and action-first welcome interruptions allowed by BASELINE 16. Held-click, five-click, double-tap and mid-action resize exception/disabled-control checks were clean. The dedicated drag check found the additional unit-position defect described above.
Wave lessons were checked directly: current hints/Read, once-only cues, stable focus, all five rack choices in view, accurate feedback, no answer-copy shortcut, every standard practiced, grayscale meanings, Motion off, state restoration and resizing during actual tool use. The audit could not obtain its phone iframe context because an earlier review host still owned port 8765. Identified and terminated that exact owned process, then manually re-shot all seven omitted phone states on the correct host. Phone verification is a targeted replacement, not a successful automated phone audit. The bundled tool has no external resources or network calls.

## Left open
Unattended choices follow the brief: positive guess domain, explicit scoring bands, ribbon/slip flows without added guesses, both two-unit directions, a truthful unit segment when a square cannot fit, the spec's compact 44-pixel exception, and action-first narration. Very large on-screen units cannot both fit inside a 150-pixel lens at true 4x; standing tools start at the specified floor zero. These spec tensions were not hidden by changing scale or adding features. No engine changes or commits.
The first location/brief read lacked an explicit command timeout; subsequent commands were bounded. An initial play-driver choice loop and the keyboard driver's Enter encoding were corrected; failed harness attempts remain in Scratch. The audit was run once, last. No second full review or polish round was started.

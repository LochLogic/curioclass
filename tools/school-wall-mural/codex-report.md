# Codex report: school-wall-mural

## Built

Build only completed on 2026-11-01. No commits and no polish round.
The self-contained `school-wall-mural.html` is 1471.7 KiB, below 2 MB.
Delivered source, draft metadata (stage built), teacher notes, 23 voice lines, audit states, handoff, art prompts, fifteen WebP paintings and the bundle.
Listen, Judge, Street test and Board are connected. Rubric, choice, banner and revisions save locally.
No recordings were made. Curio.voice uses browser speech, with clear-teacher / Iapetus specified for later recording.
No network requests are made by the tool.

## Numbers check

PASS: recomputed all 16,383 nonzero weightings in `_scratch/school-wall-mural/prepare.py`.
Unique wins A/B/C/D: 328 / 7753 / 2210 / 4245; ties: 1847. These match the spec.
Correction: Equal weights sets weights to 2, so B/D/C/A total 40 / 38 / 36 / 30. The spec's 20 / 19 / 18 / 15 are weight-1 sums.
All twelve original visual angles match to 0.1 arcminute. Enlarged A across the street is 57.3 arcminutes.
A 12 m wall at 25 km/h gives 1.728 seconds, rounded to the specified 1.7-second ride.
Year-five losses I/II/III: 4.9 / 18.5 / 55.6 percent. All intermediate compound values match.
Contrast ratios: ink/paper 14.03, ink/white 15.83, muted/paper 5.62, muted/white 6.35, brand/paper 5.71, white/brand 6.44.
Zero-weight labels use the muted color instead of reduced opacity.
Pigment grades are explicitly the fictional sketch model's paint grades. Primary sources show product variation; universal pigment-only grade verification is not claimed.

## Feel check

Played the connected path: listen, build criteria, change a leader, inspect and pin a sketch, test the wall, revise, undo and present evidence.
Best moment: enlarging River Timeline makes the factory visibly readable while removing the bridge, and its History/Readable tradeoff updates everywhere.
Flattest moment 1: the first factory revision was a flat vector study beside rich paintings. Replaced it with a fifteenth generated painting.
Flattest moment 2: the original bus scene pushed recall buttons and paint swatches below the laptop frame. Reduced scene height so the next action stays with its result.
Compared the gallery frame beside Beat Lab in `_scratch/school-wall-mural/bar-comparison.png`; also opened Snowy Mail Route.
This is a quieter decision tool than Beat Lab, but its paintings, material surfaces, live ranking, street placement and earned evidence reply are not plainer.

## Done when

1. PASS: Judge's ranked proposals and score bars are central at 1366x768 and 680x425; the leader strip is visible. Frames: `full-frames/judge-1366.png`, `full-frames/judge-680.png`.
2. PASS: History alone selects A, Nature B, Cost C, Students D; all zero ties all four. Functional assertions and real-input audit states cover the limits.
3. PASS: weights synchronously update totals, rank and the strip; the reorder uses a 400 ms FLIP animation. Motion off skips it. Keyboard changes retained focus.
4. PASS: all original angles and enlarged A match the calculation; the 5/15 arcminute branches and the mural-only blur implement the stated rule.
5. PASS: measured rides were 1703-1707 ms with motion on/off. Mode and view interruption tests stop rides immediately.
6. PASS: C's III swatches show 55.6% loss at five. Both C swaps raise Lasts to 3; Undo restores 1. B's two swaps raise Lasts to 3 and its equal-weight total to 42; Undo restores 2.
7. PASS: an unseen Across test stays locked and unlocks after it is opened. Replies correctly count 0/3 and 3/3. The year-five comparison now requires both actual year-five views.
8. PASS on the targeted held-click paths: newLeader started three times, busAsk three times, boardDone twice; busHow once. A neighbor quote then Add instruction both started, in order. Rapid same-mode and Reset taps no longer cut the welcome.
9. PASS: reload restored choice, weights and revision before Reset. Reset cleared the save and returned to Listen. A blocked-storage check displayed the local-tab fallback without an exception.

Evidence: `logic-results.json` has an empty failure list; `reload-results.json` reports ok; `focus-evidence-results.json` passes year-five locks, B swaps/Undo and storage fallback.
The final functional run after the behavior fixes also has an empty failure list.

## Wave lessons

- Hint and voice: PASS on tested laptop paths. Hints update immediately; Read uses the current hint; quote/instruction sequences stay together. A/D summer hints now name available controls.
- Focus and layout: FAIL for the complete every-size standard. Lost focus on view/navigation/Present controls was fixed, and initial focus is not taken. Compact and long-page scrolling remains.
- Sizes: FAIL for every control above the fold at every size. The laptop rubric and ranking fit; 680/800 previews and stacked 760/375 pages can need scrolling. Phone horizontal overflow was fixed.
- No giveaways: PASS. This is an open evaluation model, with no hidden correct mural, answer meter or approval score.
- Honest numbers: PASS. Weighted totals, glimpse guide, angular guide and fade model are labeled. Actual paint durability is not predicted.
- Standards: PASS. Solo actions select work, prepare it for a setting, present evidence, evaluate criteria and connect community wishes.
- Motion off: PASS. The audit found no infinite animation; ride timing remains 1.7 seconds.
- Short choice sets: FAIL across all sizes. All seven criterion options now fit on the laptop; compact panels and the long custodian quote can still scroll.
- Resize mid-animation: PASS in the audit, with no exceptions or controls left disabled.
- Delayed welcome after a first action: PASS by design. The action's own quote/instruction replaces the welcome, following STANDARDS. No welcomeAfter queue is used.
- Unknown shown as unknown: PASS. Untested Board evidence is locked and names the missing action.
- One look, one meaning: PASS. Criterion colors, labels and bars share one mapping; grayscale also retains ranks, names, scores and weights.
- Badge truth: PASS. The leader, ties and pinned choice are distinct; revised scores and artwork use the same state.
- Hint changes back: PASS on mode/view/revision changes; unavailable paint swaps are no longer named for A/D.
- No answer by copying words: PASS within this spec. Board cards cite evidence; a proposed timeline panel is marked as a weak proposal rather than verified work.

## Audit leads

Ran the full audit once on Chrome 9971 and host 8775. It completed with 202 original leads.
Motion off and resize stress were clean. The audit reported no runtime exceptions in its control walk.
The audit describes the bundle before the targeted corrections. It was not rerun, so 202 is not a current unresolved-bug count.

Every original lead is individually mapped in `_scratch/school-wall-mural/audit-dispositions.md` (202 parsed entries, matching the audit).
Raw audit: `_scratch/school-wall-mural/audit/audit.md`.

| Original entries | Disposition |
|---:|---|
| 103 | Vertical fold, hint, keep-region and short-panel concerns retained for review. Responsive street heights improved some cases; no clean all-size claim. |
| 58 | Phone width/clipping addressed by minmax grid sizing. All four street views now measure width 375 and scrollWidth 375. |
| 11 | Focus addressed by restoring rebuilt view/Present controls and moving removed navigation controls to the destination mode. |
| 10 | Ranking banner minimum increased to 10 px. |
| 8 | Phone proposal text is visibly replaced by 11 px A/B/C/D pseudo-elements; the cards retain complete accessible names. |
| 6 | Own first-tap lines intentionally skip the welcome, as STANDARDS requires. Neighbor quote sequencing was corrected. |
| 5 | Rapid active-mode/Reset welcome cuts addressed; targeted logs show no cut. |
| 1 | Criterion selector replaces weight rows and fits seven choices on laptops; compact scrolling remains. |

Targeted checks after corrections: 0 console errors/warnings. The final phone host check also has 0 warnings.
The initial phone host favicon 404 was a harness request; a data favicon in the temporary host removed it.
Additional corrections: board reply priority, actual year-five evidence, readable zero-weight labels, miniature nameplate spacing and scroll access for long quotes.

## Frames looked at

- Both reference tool frames and the side-by-side comparison.
- All five early frames, twelve full-run frames, grayscale/keyboard and calm frames, zero ties, saved/reloaded state, and both functional-result frames.
- All targeted, post-audit, final quote/reset, revised factory, five-summer swatch, bus recall, criterion selector and phone frames.
- All 86 audit PNGs reviewed through fifteen labeled contact sheets in `_scratch/school-wall-mural/audit-sheets/`.
- Final phone Sidewalk and Five summers frames show the corrected width; all four view widths were measured.
- Every final screenshot was inspected. These observations do not imply every strict fold requirement passed.

## Art made

15 generated paintings, 1041.1 KiB total WebP art. Final bundle 1471.7 KiB.
Six places, four original mural sketches, two wall views, a bus window, boardroom and enlarged-factory revision.
All were made with the built-in image tool during this build, copied into art/raw and processed with art.py --rekey only.
Prompts and provenance are in art/prompts.json. No people, faces, body parts or image lettering.
Fourteen base paintings were accepted; the additional painted factory revision replaced the weaker code study.

## Art still to paint

None. No people assets are required.

## Engine changes wanted

None. No kit, family engine, scripts or documentation source was changed.

## Left open

- Short previews and long stacked pages do not meet the complete every-control-above-fold standard. Some quotes, revisions and selectors require scrolling.
- Miniature banner lettering on the Board easel is artwork-scale text.
- A full product-specific confirmation of all pigment grades needs actual paint formulations. The current screen explicitly labels these as sketch-model grades and warns that products vary.
- The single audit was not rerun after targeted corrections. Its original results and every disposition remain available for the cold review.
- Recorded narration is intentionally absent under the Build-only instruction.
- Process deviations: the required reference-tool bundling regenerated two ignored reference HTML files outside the allowed folders, and the initial guide-read command lacked an explicit timeout. No outside source files were edited. Details are in handoff.md.
- Report created last to honor the user's instruction to stop when it is written.

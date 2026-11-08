# Fair Dice Investigation build handoff

## Structure
`src.html` uses the starter's kit frame, Curio.voice and the 9-12 theme. Static controls stay mounted. One script owns the seeded dice, numerical tails, case progression, device storage and responsive canvas charts. Canvas dimensions use actual CSS pixels. A first-case briefing sits over the empty chart and yields on the first roll.

## Tricky parts
- Mulberry32 chooses the hidden die and supplies independent weighted rolls. `?seed=n` and `__tool.seed(n)` reproduce investigations. Roll animations generate only the rolls already drawn; interruption cancels the rest without spending them.
- Gamma Q supplies chi-square upper tails. Incomplete beta supplies two-sided t tails. The slope interval uses t* for df 10. Statistics are computed from the supplied data, not copied constants.
- Case 2 supports pointer capture drags and a keyboard equivalent: row total, column total, matching cell. Both margins must match. Fill the rest requires three different cells.
- Case 2 uses the spec's fixed alpha 0.05. Only Case 1 and Dice lab show the alpha selector. Its result cannot inherit a different lab cutoff.
- Case 3 requires both tests, a link decision and a citation. The first filed citation is final: students enter the p-value or interval endpoints and its comparison. Unsupported first conclusions are retained as Evidence reviewed, never silently promoted to Case closed. Shuffles use Fisher-Yates, calculate 1,000 slopes immediately, and draw over 1.3 seconds.
- Dice lab computes all tests before drawing. Filled versus outlined dots distinguish flags without relying on color. Settings cancel pending drawings and invalidate the current result. Historical rows retain their n, alpha and normalized weights.
- Solved cases and the first case's evidence snapshot save with try/catch under `curio-dice-cases`. Clear confirms, removes the key, and reloads. Settings and all records stay on the device.
- Revealed face probabilities also appear in the main paper test card, so the payoff remains visible when the compact notebook hides its long log.
- Fixed narration uses curious-librarian / Aoede in the manifest, with Curio.voice's browser fallback. No audio was recorded.

## Open questions resolved
1. Keep the board game café tournament setting. There is no casino or gambling mechanic.
2. Keep Case 2 as homogeneity. Test help explains the sampling distinction from independence and their shared formula.
3. Keep the 1,200-roll budget. The limited power is intentional. No accusation is presented as statistical certainty.
4. The cold review supplied both spec portraits using the built-in image tool, marked people true, keyed with art.py --rekey, and inspected in context. The owner contact sheet is in Scratch. The librarian and tournament player are fictional characters.

## Art
Seven images were generated during this build with the built-in image tool: felt-table, die-red, die-blue, die-green, die-white, case2-file and case3-file. Source prompts are in `art/prompts.json`, raw PNGs in `art/raw`, final WebPs in `art`. The café image was redrawn in the cold review to match the painted set. All charts, pips, stamps and preview art are code.

## Engine changes wanted
None. No kit files were changed.

## Review handoff
The cold review is complete. See codex-review.md for findings, source checks, cheat replays and final voice results. Scratch contains the complete audit, rendered evidence and scoped repair checks.

The one full mechanical audit reported 26 leads. Focused repairs followed it, with targeted screenshots and real-input checks. The full audit was not rerun. Same-mode/case taps preserve narration; dialog focus returns only to a focusable control; disabling Fill the rest moves focus to Point to the cell. Long dialogs keep Back to evidence visible and their text is keyboard focusable.

## Cold review repairs
- While rolls remain, Accuse requires a current test. At zero budget an unsupported guess remains possible, without earning Case closed, so a poor allocation cannot trap the student in Case 1. Correct hidden identity with p at or above alpha earns Loaded, not established, preserving uncertainty without rewarding a lucky guess as statistical success.
- Case 2 uses the existing Point control for a selection followed by File finding. No correctness feedback occurs while selecting. The first wrong filing is retained, with correction evidence and onward access.
- Case 3 requires a numerical evidence citation and interpretation, within the spec's p-value/interval choice. File evidence commits the first conclusion. Both successful and unsupported filings persist with their actual evidence.
- Reviewed files remain accessible and unlock onward investigation; only supported conclusions say Case closed. Clear starts a fresh investigation, with confirmation.
- Lab completion is an event, so five runs produce five completion lines. The shuffle distribution now owns its slope axis rather than borrowing the residual plot's x axis.
- Portraits replace the silhouette placeholders. Existing felt, resin dice, evidence still lifes and noir palette are retained.

## Sensitivity
Fictional cafe, no cultural or historical representation claims, bodies instruction, religion or gambling. Two adult portraits: a medium-brown-skinned older woman as the competent librarian, and a light-skinned middle-aged tournament player. A fresh image reviewer should check respectful age and gender presentation, natural anatomy, and that the mildly self-assured player is not read as a caricature. Contact sheet: `_scratch/fair-dice-investigation/review-art-contact.png`.

## Left open after cold review
- The source spec and shared module catalog retain legacy AP U8/U9 labels despite College Board's revised 2026-27 five-unit framework. Shared catalog/spec changes need the curriculum owner and are outside this scoped review.
- Curious-librarian recordings are absent. Browser fallback was exercised with real held input and inspected via the voice log; a listening review of recorded takes remains for the audio stage. No audio was recorded here.

The cold review also redrew cafe-after-hours in the shared painted gouache style; no FLUX image remains in the final bundle. All three new review assets were generated through the built-in image tool. Exact prompts are recorded in art/prompts.json.

Further review checks: Mulberry32 now wraps its state to unsigned 32 bits on every draw, avoiding floating-point drift in long lab sessions. Six million fair-die rolls were exercised. History rows show each weighted die's actual six relative weights, so changing the sliders cannot make unrelated power estimates look like one sample-size experiment. The slope card leaves the zero comparison to the student before filing. Point and File narration use distinct current-state instructions.


Focused closing checks also name the filed die or explanatory variable on the main paper verdict, keep empty-die instructions valid at zero budget, and explicitly name the citation inputs for accessibility.

## Cold review validation
The single cold-review audit completed on Chrome 9941 and host 8745 with a 40-minute cap. Its 51 leads were classified in codex-review.md; citation names and the confirmed rapid-Accuse speech cut were addressed. Focused checks verified zero-budget fail-forward without unearned closure, named verdicts, all four mode introductions in a clean profile, and exact saved records. Windows process-termination denials affected harness shutdown after results were saved; owned browser-debug and host listeners were verified absent with netstat. No second full audit was run.

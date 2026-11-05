# Fair Dice Investigation build handoff

## Structure
`src.html` uses the starter's kit frame, Curio.voice and the 9-12 theme. Static controls stay mounted. One script owns the seeded dice, numerical tails, case progression, device storage and responsive canvas charts. Canvas dimensions use actual CSS pixels. A first-case briefing sits over the empty chart and yields on the first roll.

## Tricky parts
- Mulberry32 chooses the hidden die and supplies independent weighted rolls. `?seed=n` and `__tool.seed(n)` reproduce investigations. Roll animations generate only the rolls already drawn; interruption cancels the rest without spending them.
- Gamma Q supplies chi-square upper tails. Incomplete beta supplies two-sided t tails. The slope interval uses t* for df 10. Statistics are computed from the supplied data, not copied constants.
- Case 2 supports pointer capture drags and a keyboard equivalent: row total, column total, matching cell. Both margins must match. Fill the rest requires three different cells.
- Case 2 uses the spec's fixed alpha 0.05. Only Case 1 and Dice lab show the alpha selector. Its result cannot inherit a different lab cutoff.
- Case 3 requires both tests, a link decision and a citation. A temperature citation rejects the decoy without closing the case. Shuffles use Fisher-Yates, calculate 1,000 slopes immediately, and draw over 1.3 seconds.
- Dice lab computes all tests before drawing. Filled versus outlined dots distinguish flags without relying on color. Settings cancel pending drawings and invalidate the current result. Historical rows retain their n, alpha and normalized weights.
- Solved cases and the first case's evidence snapshot save with try/catch under `curio-dice-cases`. Clear confirms, removes the key, and reloads. Settings and all records stay on the device.
- Revealed face probabilities also appear in the main paper test card, so the payoff remains visible when the compact notebook hides its long log.
- Fixed narration uses curious-librarian / Aoede in the manifest, with Curio.voice's browser fallback. No audio was recorded.

## Open questions resolved
1. Keep the board game café tournament setting. There is no casino or gambling mechanic.
2. Keep Case 2 as homogeneity. Test help explains the sampling distinction from independence and their shared formula.
3. Keep the 1,200-roll budget. The limited power is intentional. No accusation is presented as statistical certainty.
4. Defer the librarian and suspect portraits for owner review. Both assets remain listed with people true and art tokens; tasteful faceless code silhouettes serve their briefing cards. No people were generated.

## Art
Seven images were generated during this build with the built-in image tool: felt-table, die-red, die-blue, die-green, die-white, case2-file and case3-file. Source prompts are in `art/prompts.json`, raw PNGs in `art/raw`, final WebPs in `art`. The original café image remains in use behind the picker and briefing dialogs. All charts, pips, stamps and preview art are code.

## Engine changes wanted
None. No kit files were changed.

## Next review
Build only. No commits or polish round. Use codex-report.md for the build checks and any remaining audit leads. Review the small-screen density, classroom pacing and browser-speech listening quality in the cold review.

The one full mechanical audit reported 26 leads. Focused repairs followed it, with targeted screenshots and real-input checks. The full audit was not rerun. Same-mode/case taps preserve narration; dialog focus returns only to a focusable control; disabling Fill the rest moves focus to Point to the cell. Long dialogs keep Back to evidence visible and their text is keyboard focusable.

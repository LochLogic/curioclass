# Paycheck Decoder handoff

Build only, November 7, 2026. No commit and no polish round.

## Cold review repairs, November 8, 2026

Preserved the desk, workplace paintings, apricot paper hierarchy, prediction guards and payroll formulas. Redrew the highlighter with the built-in image tool, keyed its magenta backdrop using `art.py --rekey`, and inspected the final 240-pixel asset and its 100-pixel scene placement. Prompt and raw image are in `art/`; the old asset is preserved in Scratch.

Employer-paid amounts now flash and show signed deltas, matching employee lines. Salary/worker and mode changes recompute the validation note so a rejected hourly rate cannot leave an hourly warning on Avery's salary form. Motion-off reveal keeps employer-card buttons disabled until the result beat, and `showCard` also guards the reveal, preventing a result from arriving over a newly opened card. The take-home bar names the tax/benefit gap and explicitly describes underfunded setups. Ohio's card names its omitted $332 base tax. Compact Change it hides a redundant heading and an empty validation note to keep hours and pay rate nearer the top.

No curriculum, formula, score, shared engine, voice recording or bank voice change. The annualized federal estimate, simplified location taxes, missing money engine and incompatible whole-stub/44-pixel preview requirements remain the spec decisions below. Review evidence is under `_scratch/paycheck-decoder/`, with `review-` or `-review` names; the builder's evidence is retained.

Compact Change it now scrolls the paper to the gross line on entry, so an hours edit has visible earnings beside it rather than just an employer header. Hour readouts keep their unit together and the two week sliders align. The phone timecard gets enough height for the hours and pay-rate controls together; secondary settings still scroll.

An underfunded setup also pauses Guess first before any attempt: Check/slider are disabled and the hint/Read/once-per-load how-to name Change it. This prevents the nonnegative slider from asking for an impossible negative deposit. Its fixed `underfundedGuess` line is included in the voice manifest and `allLines()`; healthy and zero-pay practice paths retain their original behavior.

The single review audit completed with 84 leads in about 32 minutes. Its old snapshot and all 51 frames are preserved in `review-audit/`. The confirmed card fix keeps Plain words, Close card, Show me and the hint outside a separate keyboard-focusable explanation scroller. Phone cards expose a named nonmodal dialog and focus Close without scrolling. The unopened list is retained. `drawLinks()` restores outlines after Plain words redraws the stub. Inner-paper scrolling brings a list-selected or returned focus line into view while preventScroll keeps the page still. The desk scene, signed feedback and full math steps are retained.

Try again is disabled until there is something to reset; after a retry the guess slider gets focus with preventScroll. The biggest-mover calculation now includes net, so Sam's OH-to-TX net gain of $56.20 is correctly larger than either individual removed tax. Zero-gross readouts avoid a false 0% of zero, with a zero-pay how-to and result event. There are seven fixed how-to lines and one fixed zero-result line in the manifest, plus the two dynamic event keys. No recording was made.

Spec correction wanted: the Massachusetts formula includes pre-tax retirement contributions even though eligible 401(k) deferrals are generally excluded under current MA DOR guidance. Do not silently rewrite the mandated formula. The card and notes now distinguish that model from the actual rule; return the formula to the spec owner. This is separate from the intentionally simplified Ohio base tax and Denver earnings-threshold omissions.

## Structure

`src.html` starts from the kit starter's metadata, header, main/panel structure and kit initialization. It includes the 9-12 theme, then tool CSS, a document renderer, pure payroll functions, line cards and mode handlers. `window.__tool` exposes state, config, current amounts and pure calculations for testing. The bundle is generated, not hand edited.

The panel precedes the paper in DOM tab order. Workplace tabs stay selected across modes. Paper and panel have independent scrolling; the phone paper uses one column and a line card becomes a bottom sheet. Stable inputs are never replaced during slider changes. Paper rows are redrawn to show signed current-check deltas in reserved space. Tapping an amount while editing returns to Stub with that card open and preserves the edited values. Speech is routed through Curio.voice, and effects through Curio.tone.

## Open question resolved

Keep the spec's annualized bracket estimate rather than implementing the full Publication 15-T tables. The federal card explains the distinction and assumes a single filer with no credits or extra withholding.

## Spec conflicts and decisions

- The prompt requires the image tool; older spec text names local FLUX. Used built-in OpenAI image generation for all five paintings, each `drawn_by: codex` and `people: false`.
- All rows cannot remain 44 px while a complete four-box stub, employer strip, header and tabs fit in 680x425. Preserve target size and real pixels, with an internal paper scrollbar. The whole-stub preview requirement is left open, not claimed passed.
- YTD multiplication conflicts with capped Social Security, additional Medicare and once-monthly Denver charges. Sum the actual model checks for affected lines. Cards show the simple multiplication and then the corrected accumulated total.
- KFF's $9,325 is the total premium. Use it as total and explicitly model 84% as the employer portion. The $1,440 employee example remains the spec's chosen amount.
- The spec has no low-pay benefit shortfall rule. Limit the health deduction to gross minus retirement and label the rule in its card; show a form note if remaining taxes still exceed available pay. All-zero hourly stubs suppress benefits and taxes.
- Preserve both weeks when converting Sam's pay schedule. A later edit to the average hours deliberately replaces the alternating pattern, stated beside the slider.
- Denver's once-monthly tax uses the displayed dates, not an independent fractional-month counter. Weekly and biweekly checks begin January 2; semimonthly checks are the 15th and last day. This fixes a possible tax/date mismatch when schedules change.
- The nearest-guess tally could be set by copying an already revealed result, reading Stub first, or using zero-hour pay. Only the first check on an original unchanged positive-gross stub whose pay has not already been available in Stub or Change it enters the tally. Jordan starts as practice because the opening screen exposes it. Switching to an unseen worker in Guess first enables a first prediction. Retries are practice. Remembering a value from a previous visit is ordinary learning; no visit's tally persists.
- CODEX-BUILD asks for an early report, but the owner's direct prompt says stop when that file is written. The final report is created after checks; interim evidence stays in Scratch.
- The spec's instant Motion-off reveal is visual: amounts appear at once, while the result/voice beat keeps the same deadline as the animated reveal. This also honors STANDARDS' instruction to preserve timing. A mid-reveal Motion toggle preserves the remaining deadline.

## Voice

Declared bank voice: calm-professor, Schedar. Seven fixed how-to lines, one fixed zero-result line, and two dynamic event keys, deltaBig and guessResult. No recording was made. Browser speech is the runtime fallback and cannot guarantee Schedar. Read speaks the current card's text when open. Mode changes, card changes and new edits hush stale speech. A still-valid Plain words how-to continues across successive line selections, then stays heard.

## Engine changes wanted

`docs/families/money.md` and `kit/money.js` do not exist in this checkout. Proposed future shared API: `r2`, `money`, `fedTax`, `fica`, `stateTax`, `paycheck`. The tool-local `paycheck` returns integer cents, preserves week-specific overtime, applies partial Social Security cap crossing, and excludes additional Medicare from the employer match. Promote only after three finished tools actually share the implementation, per BASELINE rule 13. No shared file was edited.

## Sensitivity

Financial learning model only. No culture, religion, hard history, bodily depiction or people artwork. Review that the fictional young workers are treated respectfully and that low earnings are never framed as personal failure. No household income is requested.

## Evidence

`_scratch/paycheck-decoder/` holds independent Decimal calculations, 6,000 fixture results, browser shots, voice logs, adversarial checks, audit output and comparison frames. Five original PNGs are in `art/raw`; five resized WebPs are used in the offline bundle. No host.html is required for normal use.

The single full audit completed with 90 leads against its preserved pre-fix bundle. Compact targets, card hints, edit-mode line actions, prediction actions and resize interruptions have targeted repair evidence. The audit's 375 host checks were blocked by a stale owned test server, which was stopped. Separate final 375 checks pass. All used browser ports and the host port were verified closed before the report. Compact forms and the 680 whole-stub requirement remain the documented layout constraint.

Windows test note: this machine's LibreOffice `python.exe` launches a separate runtime. Stopping its launcher did not stop the first HTTP server. The final host helper records the runtime PID, has a time limit and exits through a stop flag; its supervisor waits for shutdown. No test service remains on the assigned ports.

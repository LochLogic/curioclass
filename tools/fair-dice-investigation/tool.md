# Fair Dice Investigation: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: fair-dice-investigation

#### Built

- Offline Grade 12 statistics mystery: three ordered cases and Dice lab. Uses the kit frame, 9-12 theme and Curio.voice.
- Seven new painted assets, the retained café backdrop, adaptive canvas charts, interruptible seeded rolls, expected-cell dragging, slope inference, shuffles and simulation history.
- All files are inside the tool and its Scratch folder. No commits, branch changes, kit edits, audio recording or polish round.

#### Numbers check

- Scratch setup.py, numbers.json and strategies.py independently recompute the supplied arithmetic with NumPy/SciPy.
- Worked counts: χ² 17.16, p 0.00420614; contributions 8.41, .16, .16, .01, .01, 8.41. Fair-looking 60: χ² 1, p .96256577.
- Case 2: columns 115, 88, 81, 76; expected 38.3333, 29.3333, 27, 25.3333; χ² 14.39680828, df 6, p .02550441. Largest contribution 6.40289855, Castle seat 1.
- Weight: slope .28496503, SE .05620169, t 5.07039939, p .000484545, interval (.159739857, .410190213). Temperature: slope .00118881, p .780529823, interval (-.008064795, .010442417).
- Critical values, normalized weights, noncentral power, multiple testing rates, binomial spreads, residual summaries and contrasts match the spec's rounded arithmetic.
- Independent 20,000-run estimates vary from the spec's particular simulation: fair rates ranged .0443 to .0539, not its .047 to .052. Loaded power ranged .07665 at n 30 to .9615 at n 1,000. No fixed result is substituted for simulation.
- Independent 10,000-case strategies: equal allocation .435; 150 then leader .4702; 100 then fixed leader .410; adaptive 1,200 .5762, 1,500 .6528, 2,000 .7196. The 5,000-shuffle extreme fraction was .0008, versus the spec's .0006. Both are stochastic variation.
- Contrast: brand/panel 5.62:1, brand/section 5.33:1, brand/paper 6.38:1, dark ink/brand 5.89:1, card/felt 10.54:1.

#### Feel check

- Played the full real-input path through all three cases, including wrong-cell and temperature-decoy feedback, then compared fair and loaded simulations.
- Best moment: the 1,000-dot field changes from a few false alarms to roughly four fifths flagged, and the student's case closes with their evidence filed.
- Flattest moment 1: native drag did not register reliably. Replaced it with a moving total chip and pointer-capture drop handling. Real drags now build the expected count.
- Flattest moment 2: compact plots compressed into almost flat strips. Reclaimed readout space, reduced tick density and reserved scatter/residual height. Also gave a six-row lab history an adaptive dot strip.
- Opened and bundled both bar tools in Scratch. feel-comparison.png places the 1366x768 evidence view beside Beat Lab. The painted felt, resin dice and paper readout have comparable visual weight without mimicking its palette or interaction.

#### Done when

1. PASS: goodness API reproduces the worked example, exact contributions and displayed p .0042; functional.json.
2. PASS: real-input expected cells build, Fill the rest unlocks after three, only Castle seat 1 closes the case; verification.json and table frames.
3. PASS: actual regressions reproduce slope .2850, t 5.07, p ≈ .00048 and (.160,.410); decoy p ≈ .781. Four-place p readouts retain a separate precision note for the tiny slope p.
4. PASS: checked 1,000-run fair share .048 and loaded share .797; a separate UI loaded run .796. These satisfy the requested bands.
5. PASS: tests below 30 refused; 13 requests for Roll 100 stop at exactly 1,200; Accuse stays live. Two wrong accusations reveal four true distributions and open Case 2.
6. PASS: at 1366x768 and 1000x625, face bars, winning-seat table, scatter/residual chart and share-flagged chart dominate their stages; full sweep and targeted frames.
7. PASS: interrupted roll kept 28 completed rolls, then exactly 10 on the other die. Shuffle tab changes and lab slider changes cancel the draw immediately; no delayed stale result.
8. PASS: the complete real-input path saved all three cases and the first evidence snapshot through reload. Clear restored no solved cases and a 1,200-roll budget.
9. PASS with focused post-audit checks: all required sizes shot once, affected sizes rechecked. Held clicks, keyboard activation, grayscale and Motion off checked. A host fixture favicon 404 was removed from the subsequent phone checks; the actual offline tool made no HTTP requests.

#### Wave lessons

- PASS, Hint and voice: current hints update before narration; Read read the exact live hint; first roll acts immediately. How lines use Curio.voice and stale checks. The audit found no errors or lost repeated events in its 2-second tap checks.
- PASS, Focus and layout: static controls stay mounted, no focus taken on load, dialog focus returns with preventScroll, hint space reserved. The final focus checks return to pick2 after closing Case 2, point-cell after filling, and next-case or m-lab on closure.
- PASS, Sizes: full eight-size sweep, including 375x812 iframe, then targeted compact/table/plot/lab corrections. The repaired phone Cases button and all six sliders measure at least 44 pixels in each target dimension.
- PASS, No giveaways: hidden die index stays in the closure until a case closes; names and artwork do not signal loading. True probabilities appear only after accusation.
- PASS, Honest numbers: each test names H₀, df, expected counts and α; simulation results identify false alarm rate or power and their assumptions.
- PASS, Standards: students perform goodness of fit and homogeneity for U8, and both slope tests and intervals for U9. No family engine applies.
- PASS, Motion off: tumble and idle-light loops explicitly stop. Roll accounting and 650 ms roll duration remain the same.
- PASS, Short choices: dice, decision/citation buttons, totals and lab settings are visible; long help and logs may scroll. Full-size and targeted phone frames were inspected.
- PASS, Resize mid-animation: charts redraw from state; controls are not rebuilt and pending animation state is retained or canceled by its owner.
- PASS, Welcome timing: no welcomeAfter. The first Roll is declared as speaking later and skips a stale welcome. Case briefings delay the welcome until the student returns to evidence.
- PASS, Unknown as unknown: untested statistics, unbuilt expected counts and the initial lab share show question marks.
- PASS, One look, one meaning: dashed line always means expected counts; filled versus outlined lab dots mean flagged versus not flagged.
- PASS, Badge truth: case stamps reflect either a solved file or the two-error evidence limit; non-rejection never claims the die is proven fair.
- PASS, Reversible hints: mode, plot, n, α and weight changes replace the hint immediately.
- PASS, No answer by copying: students compare contributions and inferential results; briefing text does not identify the loaded die or largest cell.

#### Audit leads

One full audit completed on port 9981 with host 8785: 26 leads. It found no exceptions, no stuck disabled controls on resize, no infinite animation with Motion off, and clean five-click, 2-second narration checks. The full audit predates the final repairs and was not rerun.
- FIXED, 5 alpha-label leads: replaced font-size zero text with a hidden redundant span and a visible alpha symbol. The select retains its accessible name.
- FIXED, 1 phone target lead: Cases is at least 44 by 44 pixels. All six phone sliders now have 44-pixel hit heights too.
- FIXED, 4 dialog-return focus leads: reject a saved body or nonfocusable opener, then return on the next frame to a visible control or the active case card. Real clicks and Enter twice now end on pick2.
- FIXED, 3 Fill the rest focus leads: capture focus before disabling the button, then move it to Point to the cell. Verified active id point-cell.
- FIXED, 2 phone table-heading overlap leads: recovered header room and tightened the formula row. The measured briefing bottom is 140 and table top is 143, with zero overlap.
- INTENTIONAL, 2 briefing hint/keep leads: the modal covers the background hint and makes the background inert. The dialog has its own readable, focusable text and an always-visible Back to evidence control.
- INTENTIONAL, 4 first-welcome leads on Roll 1/10/100 and Test: STANDARDS requires the first action's own line or animation to skip a stale welcome. The premise is visible in the opening briefing; Test gives its own under-30 instruction.
- FIXED, 1 late Accuse welcome: the welcome becomes invalid on accusation or closure, and the action hushes stale speech. Seed 7's first Accuse logs only the closed event.
- FIXED, 1 Enter-twice focus lead: capture the active button before it disables and focus Next case or Dice lab afterward. Enter twice through the next briefing now leaves focus on pick2.
- FIXED, 3 quick-tap welcome-cut leads: tapping the current mode or current case no longer hushes it. Real repeated Cases, case-card and Dice lab taps log one welcome without a cut.
- Additional focused repairs: honest-die reaccusation is refused without spending the second attempt; wrong cell selection stays in pointing mode; closed Case 3 never names a hidden Next case; Case 2 uses its specified fixed alpha 0.05; compact dot stacks and six-row history fit their boxes.

#### Frames looked at

- Scratch bar-frames: Snowy Mail Route and Beat Lab, 1366x768.
- All 3 check frames and 10 journey frames, including interruption, exhausted budget, wrong accusation, table drag, both slopes, shuffle, lab cancel and keyboard activation.
- All 32 full-sweep frames: four evidence views at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812.
- All 14 targeted frames, including affected compact/phone states, grayscale, Motion off and briefing.
- All 7 final frames: opening, compact opening, n/α extremes, zero weights, second wrong accusation and six-row history.
- All 59 audit frames, reviewed in labeled contact sheets.
- Two last compact/phone truth-reveal frames: every revealed probability is visible on the main card, whose bottom stays inside the viewport.
- All 9 final-source preview repair frames, then 13 finished-bundle frames plus the focus diagnostic and 2 final keyboard/welcome frames. Phone target measurements, zero table overlap, and the Enter-twice path are in finish.log and the final tool output.

#### Art made

- Seven new images through the built-in image tool. Existing café retained. Eight final WebPs total 164.5 KB. Final bundled file is 519.9 KB, below 2 MB.
- Raw PNGs copied into art/raw, prompts and drawn_by recorded. Processed only with art.py --rekey. Each finished asset reviewed on a dark contact sheet and in context. No redraw needed.

#### Art still to paint

- Librarian and suspect portraits: people true, deferred for owner review. Faceless code silhouettes remain. No people or body parts were generated.

#### Engine changes wanted

None.

#### Left open

- Recorded curious-librarian narration is absent by the build-only no-recording instruction. Browser speech remains the fallback and has not had a listening review.
- No live classroom session or cold review has occurred. Small-screen density remains a useful cold-review focus.
- The full audit was run once before the final focused repairs. Its original 26 leads and the targeted repair evidence remain in Scratch for the cold reviewer.
- No final full audit or second complete size sweep was run after the focused repairs. The affected header layouts were rechecked at every required size, with additional phone table/lab, focus, keyboard and welcome checks.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: fair-dice-investigation

#### Played
Cold Grade 12 solo play of all three cases, both slope plots, shuffles and Dice lab preceded reading the builder's report, handoff, notes or source. Replayed the repaired journey with voice on and checked projector legibility. The resin dice, felt table and fair-versus-loaded dot field were strong and remain.

#### Findings fixed
- blocker, general, Case 1: a lucky zero-roll accusation earned Case closed. While rolls remain, a current test is required. A correct identity without significant evidence is Loaded, not established.
- blocker, general, Case 1 budget edge: the evidence guard could strand a student after spending every roll on one honest die. Zero-budget guesses now allow a reviewed resolution, never statistical closure without a supporting test. Two wrong accusations still open Case 2.
- blocker, general, Case 2: trying cells in turn earned closure. Select without correctness feedback, then File finding; the first wrong filing stays Evidence reviewed and cannot become a solved stamp by sweeping options.
- blocker, general, Case 3: both links plus either citation could be tried freely. Filing now requires the selected plot's numerical evidence and its null comparison. An unsupported first conclusion remains in the record; answer cycling cannot earn closure.
- blocker, general, random generator: unbounded state lost integer precision after about 4.92 million draws. State now wraps to unsigned 32 bits; six million fair-die rolls were exercised.
- should fix, general, teaching: the slope card supplied the zero-comparison answer. It now gives the numbers and asks students to make the comparison before filing. Display-rounded p-values are accepted.
- should fix, general, simulation history: different custom dice were all called Weighted. Each row now identifies its six relative weights, preserving honest comparisons across settings.
- should fix, general, shuffle: explanatory-variable ticks and a residual label remained under shuffled slopes. The distribution now owns its slope scale and units.
- should fix, general, voice: simulation completion was a once-only how-to. It is a short event on every run. Point/File instructions match the current button label; dialog speech stops when its dialog closes.
- should fix, general, rapid Accuse: repeated invalid taps hushed their own instruction. Invalid taps now leave it playing, without spending attempts.
- should fix, general, state wording: filed verdicts name the accused die or explanatory variable while another evidence view is selected. Empty-die instructions no longer recommend disabled Roll controls.
- should fix, general, access: phone Read was 41.6 px wide; it is at least 44 px. Compact storage disclosure is visible. Citation inputs have explicit accessible names, retaining their native labels.
- should fix, general, graphics: two silhouette placeholders became painted adult portraits; the flat cafe backdrop was redrawn to match the existing painted set. The palette, dice, felt and evidence still lifes were retained.

#### Findings left
- should fix, shared catalog/spec: AP U8/U9 labels are legacy mappings. Current College Board guidance uses a revised five-unit framework. Notes and handoff identify this; changing shared curriculum mappings or the source spec is outside this review's scope.
- Recorded curious-librarian clips remain absent under CODEX-BUILD.md's no-recording rule. Browser fallback was exercised; recorded-take listening belongs to the audio stage.

#### Break it
- Case 1: zero-work and repeated Accuse taps cannot earn closure or spend attempts while budget remains. At 29 rolls Test refuses; at 30 it accepts, with expected count 5.
- A tested loaded die with p 0.8323 stays Loaded, not established. At zero budget, an untested correct guess also remains unsupported; no fabricated p-value is shown.
- Spending all 1,200 rolls on one honest die, accusing it, then an unsampled honest die advances to Case 2 as evidence ran out. Reaccusing a cleared die does not spend another attempt.
- Case 2: rebuilding the same cell three times builds only one and leaves Fill the rest disabled. Sweeping all cells then filing a wrong cell records failure; later taps cannot promote it. The correct first largest-cell filing succeeds.
- Case 3: blank evidence refuses filing; wrong numbers or the wrong null comparison cannot earn closure. Correct interval endpoints and rounded p 0.0005 work. Unsupported filings retain the chosen variable and evidence.
- Lab: sweeping weights changes the actual distribution, not a score. Zero weights visibly use Fair; n 30/1,000, alpha .10/.05/.01, maximum weights and six-row history were checked. Fair/loaded n 600 rates of .043/.780 met the spec's bands; six later fair n 1,000 runs ranged .038 to .055.
- Interrupted rolling retained 25 rolls, then exactly 10 on the next die; total stopped at 1,200 and budget 0. Slider and plot changes canceled pending lab/shuffle drawings without stale results.
- Reviewed outcomes survived a fresh page load without becoming Case closed. Clear restored no saved cases and 1,200 rolls. A whole-pixel jittered row-total and column-total drag built the expected cell.

#### Voice walk
Final clean-profile walk: select each die, Roll 100 and Test; allocate the remaining rolls, test and accuse; Next case and Back to evidence; build three expected cells, Fill the rest, choose and file the cell; open Case 3, test both slopes, choose Weight depth and file an interval citation; open Dice lab and run investigations. Held clicks were 120 ms, 2 seconds apart.
Spoken starts, in order: wCases, budget, exhausted, closed, wCase2, fill, pointCell, fileCell, closed, wCase3, chooseLink, citation, fileEvidence, closed, wLab, labDone. All four mode introductions started once on the final clean-profile path; the log is in Scratch main-voice-walk.json.
| Line | Kind | Expected starts | Observed |
|---|---|---:|---:|
| Each of wCases, wCase2, wCase3, wLab | welcome | 1 | 1 each |
| budget, repeated eligible rolls | how | 1 | 1 |
| under30, five repeated tests | how | 1 | 1 |
| labDone, five runs | event | 5 | 5 |
| testedFirst, two rapid invalid accusations | how | 1, uncut | 1, uncut |
Read spoke the live hint with Sound off. Obsolete pointing/citation instructions give way after the student advances; current File instructions remain. First-tap welcome skips/cuts follow BASELINE rule 16.

#### Facts checked
- All cafe, dice and game records are explicitly invented. Computation evidence: Scratch `review-math.py`, `review-numbers.py` and `review-numbers.json`.
- Goodness-of-fit formula, upper tail, df 5 and expected-count minimum 5: [OpenStax 11.2](https://openstax.org/books/introductory-statistics-2e/pages/11-2-goodness-of-fit-test). Recomputed invented examples: 17.16, p .00420614, parts 8.41/.16/.16/.01/.01/8.41; fair 60 gives 1.00, p .96256577.
- Row/column expected counts, df (r-1)(c-1), separate-sample homogeneity and its sampling distinction: [OpenStax 11.3](https://openstax.org/books/introductory-statistics-2e/pages/11-3-test-of-independence) and [11.4](https://openstax.org/books/introductory-statistics-2e/pages/11-4-test-for-homogeneity). Invented table recomputed: totals 115/88/81/76; expected 38.3333/29.3333/27/25.3333; chi-square 14.3968083, df 6, p .0255044; largest contribution 6.402899, Castle seat 1.
- Slope test, standard error, 95% interval, residual/design conditions and association limits: [OpenIntro Statistics 4e, 8.4](https://www.openintro.org/book/os/). Invented weight data recomputed: b .2849650, SE .0562017, t 5.070399, df 10, p .000484545, interval (.159740,.410190), r .848503, r squared .719958. Temperature: b .00118881, t .286249, p .780529823, interval (-.0080648,.0104424).
- The spec's critical values 9.236/11.070/15.086, normalized loaded weights and noncentral power estimates .079/.112/.189/.450/.788/.960 were independently reproduced with SciPy. They remain labeled approximate where appropriate.
- Fixed-sample, independent-test family false alarms recompute to 14.2625% for three and 18.5494% for four. Multiple-comparison context: [OpenIntro 4e, 7.5](https://www.openintro.org/book/os/). Notes distinguish adaptive/repeated testing from this fixed-sample calculation.
- Curriculum revision verified live against [College Board AP Statistics](https://apcentral.collegeboard.org/courses/ap-statistics), 2026-11-08; legacy mapping is left with the curriculum owner.

#### Sensitivity
No cultural, historical, religious or bodies lesson; this is a fictional cafe with no gambling mechanic. Both portraits carry people true. A fresh art reviewer should check respectful age/gender presentation and natural anatomy: a competent older medium-brown-skinned librarian and a light-skinned middle-aged tournament player, without caricature. Contact sheet: Scratch `review-art-contact.png`.

#### Flattest moment left
Building three expected cells still repeats one formula, as the spec requires. The closing slope conclusion now requires numerical evidence and a committed interpretation, giving the final file more weight.

#### Graphics
Generated with the built-in image tool: `art/raw/librarian.png`, `suspect.png`, and replacement `cafe-after-hours.png`; full prompts in `art/prompts.json`. Processed only with art.py --rekey. Finished WebPs and their final on-screen sizes were inspected.
Retained color pairs independently recomputed with the [W3C contrast method](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html): brand/panel 5.62:1, ink/brand 5.89:1, card/felt 10.54:1.
Ten WebPs total 224.2 KiB; final bundle 647.1 KiB. All 32 evidence-size frames, extremes, grayscale, Motion off, keyboard navigation, eight citation-name frames, affected phone/compact verdict frames and all 65 audit frames were inspected. Beat Lab and Snowy Mail Route frames were compared with this tool.

#### Audit
One full audit completed in about 28 minutes, with a 40-minute cap, Chrome 9941 and host 8745; report: Scratch `review-audit/audit.md`. No exceptions or stuck controls in resize stress; first-screen sizes and Motion off were clean.
51 leads: 36 repeated slider hitbox/caption overlaps were visually intentional within the same label, below the visible thumb/track; four background-hint leads were modal coverage with the background inert; eight welcome skips/cuts follow BASELINE rule 16. Two field-name leads were addressed with explicit names. The one confirmed rapid-Accuse speech cut was fixed and replayed.
The audit predates those focused closing repairs; affected states and the main voice path were rechecked, without a second full audit. Two recheck harnesses saved their frames/results, then hit shutdown caps with Windows process-termination denials. The owned browser was closed through its debug connection; the voice walk was retried smaller in a clean profile and passed. The final metadata snapshot reported zero app errors, and its saved record and voice manifest were read back successfully.

#### Left open
Legacy shared curriculum mapping and recorded audio, as above. No live classroom observation is claimed. No questions were asked: kept the spec's cafe, homogeneity case and 1,200-roll budget. No commits; repository writes stayed in this tool and its Scratch folder. Temporary tool host removed; owned browser-debug and host listeners verified absent with netstat.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Fair Dice Investigation build handoff

#### Structure
`src.html` uses the starter's kit frame, Curio.voice and the 9-12 theme. Static controls stay mounted. One script owns the seeded dice, numerical tails, case progression, device storage and responsive canvas charts. Canvas dimensions use actual CSS pixels. A first-case briefing sits over the empty chart and yields on the first roll.

#### Tricky parts
- Mulberry32 chooses the hidden die and supplies independent weighted rolls. `?seed=n` and `__tool.seed(n)` reproduce investigations. Roll animations generate only the rolls already drawn; interruption cancels the rest without spending them.
- Gamma Q supplies chi-square upper tails. Incomplete beta supplies two-sided t tails. The slope interval uses t* for df 10. Statistics are computed from the supplied data, not copied constants.
- Case 2 supports pointer capture drags and a keyboard equivalent: row total, column total, matching cell. Both margins must match. Fill the rest requires three different cells.
- Case 2 uses the spec's fixed alpha 0.05. Only Case 1 and Dice lab show the alpha selector. Its result cannot inherit a different lab cutoff.
- Case 3 requires both tests, a link decision and a citation. The first filed citation is final: students enter the p-value or interval endpoints and its comparison. Unsupported first conclusions are retained as Evidence reviewed, never silently promoted to Case closed. Shuffles use Fisher-Yates, calculate 1,000 slopes immediately, and draw over 1.3 seconds.
- Dice lab computes all tests before drawing. Filled versus outlined dots distinguish flags without relying on color. Settings cancel pending drawings and invalidate the current result. Historical rows retain their n, alpha and normalized weights.
- Solved cases and the first case's evidence snapshot save with try/catch under `curio-dice-cases`. Clear confirms, removes the key, and reloads. Settings and all records stay on the device.
- Revealed face probabilities also appear in the main paper test card, so the payoff remains visible when the compact notebook hides its long log.
- Fixed narration uses curious-librarian / Aoede in the manifest, with Curio.voice's browser fallback. No audio was recorded.

#### Open questions resolved
1. Keep the board game café tournament setting. There is no casino or gambling mechanic.
2. Keep Case 2 as homogeneity. Test help explains the sampling distinction from independence and their shared formula.
3. Keep the 1,200-roll budget. The limited power is intentional. No accusation is presented as statistical certainty.
4. The cold review supplied both spec portraits using the built-in image tool, marked people true, keyed with art.py --rekey, and inspected in context. The owner contact sheet is in Scratch. The librarian and tournament player are fictional characters.

#### Art
Seven images were generated during this build with the built-in image tool: felt-table, die-red, die-blue, die-green, die-white, case2-file and case3-file. Source prompts are in `art/prompts.json`, raw PNGs in `art/raw`, final WebPs in `art`. The café image was redrawn in the cold review to match the painted set. All charts, pips, stamps and preview art are code.

#### Engine changes wanted
None. No kit files were changed.

#### Review handoff
The cold review is complete. See codex-review.md for findings, source checks, cheat replays and final voice results. Scratch contains the complete audit, rendered evidence and scoped repair checks.

The one full mechanical audit reported 26 leads. Focused repairs followed it, with targeted screenshots and real-input checks. The full audit was not rerun. Same-mode/case taps preserve narration; dialog focus returns only to a focusable control; disabling Fill the rest moves focus to Point to the cell. Long dialogs keep Back to evidence visible and their text is keyboard focusable.

#### Cold review repairs
- While rolls remain, Accuse requires a current test. At zero budget an unsupported guess remains possible, without earning Case closed, so a poor allocation cannot trap the student in Case 1. Correct hidden identity with p at or above alpha earns Loaded, not established, preserving uncertainty without rewarding a lucky guess as statistical success.
- Case 2 uses the existing Point control for a selection followed by File finding. No correctness feedback occurs while selecting. The first wrong filing is retained, with correction evidence and onward access.
- Case 3 requires a numerical evidence citation and interpretation, within the spec's p-value/interval choice. File evidence commits the first conclusion. Both successful and unsupported filings persist with their actual evidence.
- Reviewed files remain accessible and unlock onward investigation; only supported conclusions say Case closed. Clear starts a fresh investigation, with confirmation.
- Lab completion is an event, so five runs produce five completion lines. The shuffle distribution now owns its slope axis rather than borrowing the residual plot's x axis.
- Portraits replace the silhouette placeholders. Existing felt, resin dice, evidence still lifes and noir palette are retained.

#### Sensitivity
Fictional cafe, no cultural or historical representation claims, bodies instruction, religion or gambling. Two adult portraits: a medium-brown-skinned older woman as the competent librarian, and a light-skinned middle-aged tournament player. A fresh image reviewer should check respectful age and gender presentation, natural anatomy, and that the mildly self-assured player is not read as a caricature. Contact sheet: `_scratch/fair-dice-investigation/review-art-contact.png`.

#### Left open after cold review
- The source spec and shared module catalog retain legacy AP U8/U9 labels despite College Board's revised 2026-27 five-unit framework. Shared catalog/spec changes need the curriculum owner and are outside this scoped review.
- Curious-librarian recordings are absent. Browser fallback was exercised with real held input and inspected via the voice log; a listening review of recorded takes remains for the audio stage. No audio was recorded here.

The cold review also redrew cafe-after-hours in the shared painted gouache style; no FLUX image remains in the final bundle. All three new review assets were generated through the built-in image tool. Exact prompts are recorded in art/prompts.json.

Further review checks: Mulberry32 now wraps its state to unsigned 32 bits on every draw, avoiding floating-point drift in long lab sessions. Six million fair-die rolls were exercised. History rows show each weighted die's actual six relative weights, so changing the sliders cannot make unrelated power estimates look like one sample-size experiment. The slope card leaves the zero comparison to the student before filing. Point and File narration use distinct current-state instructions.


Focused closing checks also name the filed die or explanatory variable on the main paper verdict, keep empty-die instructions valid at zero budget, and explicitly name the citation inputs for accessibility.

#### Cold review validation
The single cold-review audit completed on Chrome 9941 and host 8745 with a 40-minute cap. Its 51 leads were classified in codex-review.md; citation names and the confirmed rapid-Accuse speech cut were addressed. Focused checks verified zero-budget fail-forward without unearned closure, named verdicts, all four mode introductions in a clean profile, and exact saved records. Windows process-termination denials affected harness shutdown after results were saved; owned browser-debug and host listeners were verified absent with netstat. No second full audit was run.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)

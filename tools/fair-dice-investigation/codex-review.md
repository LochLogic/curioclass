# Codex review: fair-dice-investigation

## Played
Cold Grade 12 solo play of all three cases, both slope plots, shuffles and Dice lab preceded reading the builder's report, handoff, notes or source. Replayed the repaired journey with voice on and checked projector legibility. The resin dice, felt table and fair-versus-loaded dot field were strong and remain.

## Findings fixed
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

## Findings left
- should fix, shared catalog/spec: AP U8/U9 labels are legacy mappings. Current College Board guidance uses a revised five-unit framework. Notes and handoff identify this; changing shared curriculum mappings or the source spec is outside this review's scope.
- Recorded curious-librarian clips remain absent under CODEX-BUILD.md's no-recording rule. Browser fallback was exercised; recorded-take listening belongs to the audio stage.

## Break it
- Case 1: zero-work and repeated Accuse taps cannot earn closure or spend attempts while budget remains. At 29 rolls Test refuses; at 30 it accepts, with expected count 5.
- A tested loaded die with p 0.8323 stays Loaded, not established. At zero budget, an untested correct guess also remains unsupported; no fabricated p-value is shown.
- Spending all 1,200 rolls on one honest die, accusing it, then an unsampled honest die advances to Case 2 as evidence ran out. Reaccusing a cleared die does not spend another attempt.
- Case 2: rebuilding the same cell three times builds only one and leaves Fill the rest disabled. Sweeping all cells then filing a wrong cell records failure; later taps cannot promote it. The correct first largest-cell filing succeeds.
- Case 3: blank evidence refuses filing; wrong numbers or the wrong null comparison cannot earn closure. Correct interval endpoints and rounded p 0.0005 work. Unsupported filings retain the chosen variable and evidence.
- Lab: sweeping weights changes the actual distribution, not a score. Zero weights visibly use Fair; n 30/1,000, alpha .10/.05/.01, maximum weights and six-row history were checked. Fair/loaded n 600 rates of .043/.780 met the spec's bands; six later fair n 1,000 runs ranged .038 to .055.
- Interrupted rolling retained 25 rolls, then exactly 10 on the next die; total stopped at 1,200 and budget 0. Slider and plot changes canceled pending lab/shuffle drawings without stale results.
- Reviewed outcomes survived a fresh page load without becoming Case closed. Clear restored no saved cases and 1,200 rolls. A whole-pixel jittered row-total and column-total drag built the expected cell.

## Voice walk
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

## Facts checked
- All cafe, dice and game records are explicitly invented. Computation evidence: Scratch `review-math.py`, `review-numbers.py` and `review-numbers.json`.
- Goodness-of-fit formula, upper tail, df 5 and expected-count minimum 5: [OpenStax 11.2](https://openstax.org/books/introductory-statistics-2e/pages/11-2-goodness-of-fit-test). Recomputed invented examples: 17.16, p .00420614, parts 8.41/.16/.16/.01/.01/8.41; fair 60 gives 1.00, p .96256577.
- Row/column expected counts, df (r-1)(c-1), separate-sample homogeneity and its sampling distinction: [OpenStax 11.3](https://openstax.org/books/introductory-statistics-2e/pages/11-3-test-of-independence) and [11.4](https://openstax.org/books/introductory-statistics-2e/pages/11-4-test-for-homogeneity). Invented table recomputed: totals 115/88/81/76; expected 38.3333/29.3333/27/25.3333; chi-square 14.3968083, df 6, p .0255044; largest contribution 6.402899, Castle seat 1.
- Slope test, standard error, 95% interval, residual/design conditions and association limits: [OpenIntro Statistics 4e, 8.4](https://www.openintro.org/book/os/). Invented weight data recomputed: b .2849650, SE .0562017, t 5.070399, df 10, p .000484545, interval (.159740,.410190), r .848503, r squared .719958. Temperature: b .00118881, t .286249, p .780529823, interval (-.0080648,.0104424).
- The spec's critical values 9.236/11.070/15.086, normalized loaded weights and noncentral power estimates .079/.112/.189/.450/.788/.960 were independently reproduced with SciPy. They remain labeled approximate where appropriate.
- Fixed-sample, independent-test family false alarms recompute to 14.2625% for three and 18.5494% for four. Multiple-comparison context: [OpenIntro 4e, 7.5](https://www.openintro.org/book/os/). Notes distinguish adaptive/repeated testing from this fixed-sample calculation.
- Curriculum revision verified live against [College Board AP Statistics](https://apcentral.collegeboard.org/courses/ap-statistics), 2026-11-08; legacy mapping is left with the curriculum owner.

## Sensitivity
No cultural, historical, religious or bodies lesson; this is a fictional cafe with no gambling mechanic. Both portraits carry people true. A fresh art reviewer should check respectful age/gender presentation and natural anatomy: a competent older medium-brown-skinned librarian and a light-skinned middle-aged tournament player, without caricature. Contact sheet: Scratch `review-art-contact.png`.

## Flattest moment left
Building three expected cells still repeats one formula, as the spec requires. The closing slope conclusion now requires numerical evidence and a committed interpretation, giving the final file more weight.

## Graphics
Generated with the built-in image tool: `art/raw/librarian.png`, `suspect.png`, and replacement `cafe-after-hours.png`; full prompts in `art/prompts.json`. Processed only with art.py --rekey. Finished WebPs and their final on-screen sizes were inspected.
Retained color pairs independently recomputed with the [W3C contrast method](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html): brand/panel 5.62:1, ink/brand 5.89:1, card/felt 10.54:1.
Ten WebPs total 224.2 KiB; final bundle 647.1 KiB. All 32 evidence-size frames, extremes, grayscale, Motion off, keyboard navigation, eight citation-name frames, affected phone/compact verdict frames and all 65 audit frames were inspected. Beat Lab and Snowy Mail Route frames were compared with this tool.

## Audit
One full audit completed in about 28 minutes, with a 40-minute cap, Chrome 9941 and host 8745; report: Scratch `review-audit/audit.md`. No exceptions or stuck controls in resize stress; first-screen sizes and Motion off were clean.
51 leads: 36 repeated slider hitbox/caption overlaps were visually intentional within the same label, below the visible thumb/track; four background-hint leads were modal coverage with the background inert; eight welcome skips/cuts follow BASELINE rule 16. Two field-name leads were addressed with explicit names. The one confirmed rapid-Accuse speech cut was fixed and replayed.
The audit predates those focused closing repairs; affected states and the main voice path were rechecked, without a second full audit. Two recheck harnesses saved their frames/results, then hit shutdown caps with Windows process-termination denials. The owned browser was closed through its debug connection; the voice walk was retried smaller in a clean profile and passed. The final metadata snapshot reported zero app errors, and its saved record and voice manifest were read back successfully.

## Left open
Legacy shared curriculum mapping and recorded audio, as above. No live classroom observation is claimed. No questions were asked: kept the spec's cafe, homogeneity case and 1,200-roll budget. No commits; repository writes stayed in this tool and its Scratch folder. Temporary tool host removed; owned browser-debug and host listeners verified absent with netstat.

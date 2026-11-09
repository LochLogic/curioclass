# Codex review: courtroom-statistics

## Played

- Cold Grade 12 play: Seeds from folder to interval, then Lineup and Docket, before reading the builder's report, handoff, notes or source. Strong setting and restrained verdict; condition and approval loopholes weakened the reasoning.
- Played the main path with held clicks at 2-second intervals, plus keyboard-only to Sentencing. Checked all eight required sizes, Motion off, grayscale, the seven case types and Docket extremes.

## Findings fixed

- Blocker, general, Trial: a filed conclusion stayed approved after editing or submitting a wrong replacement. Changes now revoke filing and later tabs immediately.
- Blocker, general, Trial: wrong revised conditions and charges retained later unlocks and stale session verdicts. They now clear dependent approvals and replace the result with Review pending.
- Should fix, general, poll follow-through: answering the other conditions after dismissal could overwrite Dismissed and name the disabled Admit evidence button. Dismissal now remains decisive while random selection is false; the saved before/after replay confirms the instruction, session record and disabled control agree.
- Blocker, general, Trial: option sweeps and three Yes taps could produce an unqualified completion. Questions now vary logically between Yes and No; corrections stay visible in the session record and cannot be erased by reopening.
- Blocker, general, standards: revisiting a case or peeking in Lineup could escape evidence-exposure and late-alpha tracking. Exposure, chosen standards and warning flags now survive both paths for this page session. A pre-evidence change also survives reopening; the replay retains 0.01 instead of resetting to 0.05, without a false late-change flag.
- Should fix, general, Docket: at true p = 0.50 the unshaded null region was called beta. Both bars now explicitly measure Type I error there; beta is explained only under a false null.
- Should fix, general, voice: result events queued behind obsolete speech and disappeared on repeated actions. Results now start with their action; state changes drop stale speech; the paired teaching explanation speaks once.
- Should fix, general, phone: privacy text was hidden. A compact header line now states session-only handling and that no data leaves the device.
- Should fix, general, Lineup at 680x425: the confidence bracket crossed the axis labels despite a mechanically clean audit row. A compact title/control row and inline slider label now reserve a taller number line. Re-shot at 680x425 and 800x500; no crossing remains.
- Should fix, general, Docket minimum at 680x425: the cutoff and right endpoint labels collided. A small paper label above the axis separates the cutoff when horizontal space is tight. Re-shot at 680x425, 800x500 and the 375-wide host; labels are separate.
- Should fix, general, art: the cereal box was beside the weighing scale. Redrew it on the tray in the existing style and moved its code label.
- Polish, general, proof stage: three bare alpha buttons were the flattest step. Added restrained proof marks and error-risk cues without exposing evidence.
- Should fix, general, assumptions/voice manifest: stated no-extreme-outlier assumptions for summary-only cases; replaced the elementary-teacher recording style with a high school court clerk style; synchronized lines and audit paths.

## Findings left

- Should fix, spec/catalog: AP unit labels use the older U6/U7 numbering. Current College Board labels are U3/U4. Notes identify the migration; external catalog and spec remain unchanged under this review's scope rule.
- Should fix, spec/mapping: S-IC.B.4 requires developing margin of error with simulation; B.5 requires simulation of treatment differences. The prescribed analytical cases and coin-power simulation do not fully cover those clauses. Corrected notes to say partial coverage; adding a new simulation or changing the external mapping exceeds scope.
- Production limitation, voice: native speech remains the fallback. Recording and ear review of Iapetus were outside the authorized build workflow.

## Break it

- Charges: tried all signs, including a wrong sign after a filed result. Wrong revisions lock later stages; corrected attempts remain identified.
- Conditions: ran all-Yes, repeated toggles, a wrong revision after filing, the paired trap and voluntary-response poll. All-Yes stays at Admissibility; a bad revision cannot reach Sentencing; the poll never reaches inference.
- Verdicts: tried Innocent, both decisions in succession and a changed alpha after filing. Old verdicts and filed results are cleared; Innocent never counts as a verdict.
- Context: enumerated all six strength/direction pairs and edited a correct filed sentence to a wrong one. Only the current correct pair files; revisions revoke prior filing. Corrections are retained rather than presented as first-attempt mastery.
- Standard: tried a Lineup peek, mode return and reopening. Evidence exposure and late-standard warnings persist. An early 0.01 change survives reopening without a late-change flag. Default-alpha selection is an open modeling choice, not a scored task.
- Lineup: swept the slider endpoints and compared bands with intervals. This is labeled exploration, with no score or mastery gate to farm.
- Docket: repeated runs, changed controls during bar growth and used both parameter extremes. Old simulations clear at once; exact and sampled shares remain distinct. No best score or reflection gate exists.

## Voice walk

- Main path: bench, Seeds, charge, standard, three condition questions, Evidence, Verdict, context, Sentencing, Explore in Lineup, claim drag, Docket, Hold 1,000 trials.
- Heard in order: wTrial, charge, rightCharge, proof, checks, admit, evidence, verdict, rightVerdict, filed, sentencing, wLineup, wDocket, simulation. Every mode how-to started once in the matching mode.
- Final repeat check, 120 ms held clicks at a 2-second pace:

| Lines | Kind | Expected / spoken |
|---|---|---|
| wrongCharge, rightCharge, wrongCheck, wrongVerdict, rightVerdict | event, each | 5 / 5 |
| innocent, wrongSentence, filed, filedGuided, dismissed, simulation | event, each | 5 / 5 |
| alphaLate | event | 5 / 5 |
| charge; paired | how, each | 1 / 1 |
| wTrial, wLineup, wDocket on main path | welcome, each | 1 / 1 |

- Read interrupted current speech, worked with Sound off and released the queue on mode change. Later actions stop obsolete lines; rapid repeated result taps intentionally restart their current event. All 23 fixed lines match the manifest. Native speech was logged, not ear-reviewed.

## Facts checked

- All case values are explicitly fictional. Independently recomputed six estimates/SEs/statistics/p-values, 30 intervals and 75 Docket combinations against SciPy; all agree at displayed precision. Evidence: review-number-results.json and browser-numbers.json in Scratch.
- Seeds: z -2.376, p 0.0087, 90% interval [0.743, 0.837]; null versus estimated SE: [OpenStax 8.3](https://openstax.org/books/introductory-statistics-2e/pages/8-3-a-population-proportion).
- Cereal: mean 365.9, SD 5.2450, t -2.002, df 24, p 0.0284; 98% interval includes 368. Bus: t 1.224, df 39, p 0.1141. [OpenStax 8.2](https://openstax.org/books/introductory-statistics-2e/pages/8-2-a-single-population-mean-using-the-student-t-distribution).
- Reminder texts: pooled p 0.78, z 2.365, p 0.0090; interval SE 0.033665. [OpenStax 10.3](https://openstax.org/books/introductory-statistics-2e/pages/10-3-comparing-two-independent-population-proportions).
- Shoes: paired mean -1.05, SD 0.9060, t -4.015, df 11, p 0.0010; pairs are not independent old/new groups. [OpenStax 10.4](https://openstax.org/books/introductory-statistics-2e/pages/10-4-matched-or-paired-samples).
- Desks: SE 9.4322, Welch df 57.6121, t 2.1204, p 0.0383; 95% excludes zero and 99% includes it. [OpenStax 10.1](https://openstax.org/books/introductory-statistics-2e/pages/10-1-two-population-means-with-unknown-standard-deviations).
- Preset alpha, directional tails, p-value under H0 and failure to reject rather than proof: [OpenStax 9.4](https://openstax.org/books/introductory-statistics-2e/pages/9-4-rare-events-the-sample-decision-and-conclusion), [9.5](https://openstax.org/books/introductory-statistics-2e/pages/9-5-additional-information-and-full-hypothesis-test-examples).
- Docket k = 59, Type I 0.0443 and power 0.6225 at n 100, alpha 0.05, true p 0.60. Type I/II and power definitions: [OpenStax 9.2](https://openstax.org/books/introductory-statistics-2e/pages/9-2-outcomes-and-the-type-i-and-type-ii-errors); exact binomial sums independently verified.
- Score-test inversion versus Wald interval: [NIST/SEMATECH 7.2.4.1](https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm), plus the spec's [OpenIntro reference](https://www.openintro.org/book/os/). Mean test/interval duality checked numerically.
- Selection bias and the call-in dismissal: [OpenStax 1.2](https://openstax.org/books/introductory-statistics-2e/pages/1-2-data-sampling-and-variation-in-data-and-sampling). [Common Core S-IC.B](https://www.thecorestandards.org/Math/Content/HSS/IC/) confirms the simulation clauses missing from the spec's coverage claim. The [current AP course](https://apcentral.collegeboard.org/courses/ap-statistics) confirms revised Units 3 and 4 for 2026-27.

## Sensitivity

- No cultural, Indigenous, religious or hard-history content. Seven fictional cases concern data, including clinic attendance and adult workers/runners; no medical advice or actual legal defendants. Notes explain that the courtroom is a teaching analogy, not legal guidance. No depicted people or stereotypes; all assets checked.

## Flattest moment left

- The interval page is deliberately quiet and still mostly interpretation. Its payoff is the student's verdict beside the claim and interval; preserved the strong Lineup transition instead of adding celebration.

## Graphics

- Inspected all 11 finished assets, their styles and case mappings. Preserved courtroom, folders, gavel, coin and six other evidence paintings. Redrew only cereal with built-in imagegen; prompt and raw PNG saved in the tool, previous art preserved in Scratch.
- New WebP is 680 x 510, about 37 KB. All art totals 377,260 bytes; bundle 600,853 bytes (about 587 KiB). Paintings now fit full frames, with more height on large screens and a label positioned from the actual painted rectangle. No missing art tokens; no people assets requiring people:true.
- Computed contrast: ink/panel 14.01, muted/panel 5.88, green/panel 5.76, header 10.46, focus/panel 6.38. The spec's muted ratio 6.35 is inaccurate; actual contrast remains strong. Compared the retained court finish with the existing Beat Lab comparison frame without rebuilding another tool.

## Audit

- Ran scripts/audit_tool.py once on Chrome 9941, host 8745, with a 40-minute limit. It finished: 145 frames, all visually inspected, 18 leads. Motion off, mid-action resize, keyboard focus, five held clicks and quick double taps passed.
- One real lead was the compact Docket cutoff collision, repaired and re-shot. Independently caught and repaired the compact Lineup bracket crossing. Targeted scans and frames at 680x425 and 800x500, plus Docket at 375-wide, are clear of overlap, clipping and disabled-control instructions.
- Ten zero-font leads are intentional Motion/Sound icon buttons: visible 18-23 px glyphs, accessible names, 44 px targets. Seven first-folder taps skip the generic welcome and play the case instruction with the premise visible, as BASELINE rule 16 allows.
- Final before/after regressions confirm poll dismissal and the early-standard reopen fix. The first capture harness omitted a scan placeholder and used a nonmatching select value; corrected the harness and repeated only these focused checks. Final capture has zero console errors, warnings or exceptions. No second full audit or review.
- Evidence: _scratch/courtroom-statistics/review-audit/audit.md, review-final-confirm/, review-fixed/, review-walk/, review-number-results.json and the named before/after JSON files. The full audit preceded its compact-layout repairs; focused confirmations use the final bundle.

## Left open

- Kept both proportion brackets and the light-oak theme, as the spec and baseline lean toward them. No unattended questions were left pending.
- Guided practice can be completed after corrections; it makes no mastery claim. Reloading intentionally clears the whole page session, as disclosed.
- No commits or shared-kit changes; all authored files remain in the two authorized folders. Temporary host removed and review-owned Chrome/server processes closed.

# Courtroom Statistics: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Build

<!-- part: codex-report.md -->

### Codex report: courtroom-statistics

#### Built
- Grade 12 offline tool with Trial, Lineup and Docket, built from the kit starter.
- Seven illustrated made-up cases; ordered stages, condition checks, live tests, verdict/context sentence, intervals and session record.
- Score-test inversion for proportions, Student t and Welch inference for means, seeded binomial simulation and exact error/power calculations.
- Build only. No git commits, branch changes or polish round. Final report is held until checks finish, honoring the user's stop instruction.

#### Numbers check
- Independently recomputed the six numerical cases with scipy before implementation: estimates, SD/SE, df, tails and all supplied intervals match the stated precision.
- Browser values match scipy within 0.000001 for statistics/tails and 0.00001 for critical values.
- All 75 Docket n/alpha/true-p combinations match scipy exact binomial tails to 0.0000000001; all cutoffs match.
- Cereal Lineup band equals its 95% t interval exactly: [363.7349714, 368.0650286].
- Seeds score band at 90%: [0.7389141, 0.8333445], versus AP [0.7426265, 0.8373735].
- Docket default seed: Type I simulated 0.054 vs exact 0.0443130; power simulated 0.624 vs exact 0.6225327.
- Contrast recomputation: ink/panel 14.01, muted/panel 5.88, brand/panel 5.76, white/brand 6.47, header 10.46, focus/panel 6.38. The spec's muted 6.35 differs; actual 5.88 still passes AA. Spec unchanged.

#### Feel check
- Played Seeds through the complete trial, including an Innocent correction, conclusion filing and sentencing, using held clicks and then keyboard only.
- Best moment: the stamped verdict becomes a movable claim in Lineup, where a filled convicted square turns into a hollow not-convicted circle at the statistical boundary.
- Flat moment 1: the compact Evidence card crowded its readouts against the next action. Changed it to one readout row in compact landscape, with a separate two-row phone arrangement.
- Flat moment 2: the conclusion felt like scattered form fragments. Changed it to one live sentence preview with the two choices and File sentence together.
- Further build fixes: gave the Docket curves real room beside the bars and put the paired-sample trap beside the advance control in short windows.
- Compared the large evidence painting and court furniture with Snowy Mail Route and Beat Lab. The court uses restrained senior-grade feedback, rich evidence paintings and stamped decisions, without celebration.
- Comparison: _scratch/courtroom-statistics/bar-comparison.jpg. Full student result: play-frames-v2/student-sentencing.png.

#### Done when
1. PASS: Seeds z -2.376, p 0.0087, 90% AP interval [0.743, 0.837]. Python, browser data and student run.
2. PASS: Cereal p 0.0284 lies between 0.01 and 0.05; 98% interval [363.3, 368.5] includes 368. Browser assertions.
3. PASS: Desks df 57.6, t 2.120, p 0.0383; 99% interval includes zero and 95% excludes it. Browser assertions and frames.
4. PASS: held alpha change raises the objection and changes the state flag; Innocent is corrected. Changing alpha clears the old verdict and conclusion.
5. PASS: Cereal band equals 95% interval exactly; Seeds shows separate score/AP brackets. Numerical checks and real slider drag.
6. PASS: n 100, alpha 0.05 gives k 59, exact Type I 0.0443 and power at 0.6 of 0.6225. Full 75-combination independent check.
7. PASS: stage card, Evidence null curve, Lineup and Docket chart are the focus at 1366x768 and 1000x625. Visual size sweep and targeted chart fixes.
8. PASS: live control changes during bar growth cancel the old simulated state immediately. Repeated verdicts during the gavel swing act immediately. Default seeded simulation meets both tolerances.
9. PASS: all seven evidence images and three object assets were generated without people or lettering. Existing empty courtroom inspected and retained. Each case maps to its own evidence token.
10. PASS: full size/mode sweep plus focused repairs keep controls and charts visible. Final compact verdict and phone Evidence scans have no small targets, overlap, clipping, hidden controls, horizontal scroll or disabled controls named by the hint. Two intentional icon-font leads remain. Keyboard-only Seeds reaches sentencing; console clean and source offline.

#### Wave lessons
- PASS: Hint and voice: hints change immediately and name controls; Read uses the hint; Curio.voice manages heard how lines and scoped events. Held 2-second inputs logged. Some obsolete queued instructions are dropped after the student advances.
- PASS: Focus and layout: stable control DOM, no focus on load, explicit preventScroll focus when a folder or disabled advance control gives way. Reserved clerk space.
- PASS: Sizes: all eight required sizes, phone in the port-8795 iframe, plus compact and targeted fixes. Focused final verdict/phone scans pass apart from intentional icon-label leads.
- PASS: No giveaways: evidence is hidden until the student locks alpha and checks admissibility. Charge translation and comparison of p with alpha are the intended tasks, not hidden-answer puzzles.
- PASS: Honest numbers: all results computed from the case; unpooled/AP versus null-SE distinction stated; exact and simulated values separated; missing raw data and independence assumptions explicit.
- PASS: Standards: student activities directly cover inference, treatment comparisons and data-gathering validity. No family engine specified.
- PASS: Motion off: gavel and bars use kit Motion behavior; explicit calm daylight rule leaves zero infinite animations in the focused check.
- PASS: Short choices: seven folders, all charge/verdict choices and all three condition checks remain visible; no choice scroll panel.
- PASS: Resize mid-animation: redraws only SVG charts and never locks controls. Complete audit resize section is clean, with no exceptions or stuck controls.
- PASS: Welcome after first tap: multi-mode welcome callback, no welcomeAfter; a folder tap speaks its own charge instruction.
- PASS: Unknown as unknown: evidence and outcomes stay concealed until the appropriate stage; no fabricated raw observations.
- PASS: One look, one meaning: filled square means convicted, hollow circle means not convicted; dashed null versus solid true curve; labels accompany colors.
- PASS: Badge truth: exact values and current state drive stamps/readouts; late alpha invalidates the previous decision.
- PASS: Hints change back: stage and mode changes update hint immediately; case reset restores the charge instruction.
- PASS: No answer by copying words: cases require directional translation and statistical decisions; conclusions must match parameter, direction and strength. No extra answer badges.

#### Audit leads
One complete audit finished with 51 leads, using Chrome 9991 and host 8795. All 97 audit PNGs were looked at in contact sheets and selected full-size frames. Each lead family is answered below.
- Fixed: Desks at 680x425 could not progress because the long charge overlapped advance controls. Shorter correct parameter notation and compact typography repaired all associated overlaps, focus-to-page and hidden keep-region leads. Real held clicks now reach its verdict; all six numerical cases reach Evidence at 680x425.
- Fixed: compact stamp bounding boxes crossed the heading and Innocent button. Header text width and stamp placement now leave at least 4.54 px clear of the verdict button. Focused final PAGE_JS finds no overlap.
- Fixed: phone alpha labels were hidden with zero font size. They now use an accessible visually hidden span, with a visible 13 px alpha selector and explicit name. Focused phone scan has no such lead.
- Fixed: the daylight pseudo-element kept looping in calm mode. An explicit animation:none rule now gives zero running infinite animations.
- Fixed: repeated taps on the selected mode hushed its welcome. Selected-mode taps now preserve the current state and speech; all three rapid double-tap checks finish with a spoken welcome and no cut entry.
- Fixed: Sound changed header widths. Reserved width gives zero header-control movement after toggling twice.
- Explained: zero-font Motion/Sound text at the five compact sizes is deliberately replaced by visible 18 to 23 px glyphs. Both controls retain 44 px targets and accessible names. These two text-node flags are the only leads in each focused final verdict/phone scan.
- Explained: each of the seven folder first taps intentionally skips the picker welcome and speaks the charge instruction. This follows STANDARDS first-action precedence; no delayed picker welcome interrupts the case. The claim card states H0 is presumed true.
- Clean in the complete audit: browser errors, repeated how lines in the five-click samples, focus after settled Enter presses, and all resize stress checks.
- Additional visual repair: SVGs observe their own size after captions/readouts settle. Six settled chart checks match viewBox and actual dimensions, including compact and phone sentencing. Phone and compact notes no longer crowd the advance control.
- The full audit and full size sweep were not repeated after these focused repairs. Final audit-states.json also adds the two Docket extremes for future review; this completed audit used the original nine named states.

#### Frames looked at
- Both bar frames, all eleven finished art assets, six early screenshots and compact/phone repairs.
- Twelve play-check frames: full student path, keyboard path, objection, dismissal, pair trap, Lineup, Docket, interruption, Motion off and grayscale.
- All 32 full-size/mode screenshots reviewed in four contact sheets, with individual phone and compact checks.
- Targeted Evidence/Lineup/Docket frames, numerical-state frame, compact paired checks and final Docket laptop/preview frames.
- All 97 mechanical audit frames, all compact case follow-ups, chart and calm follow-ups, rapid-mode/stamp checks, Docket extremes and final package frames. Contact sheets remain in Scratch.

#### Art made
- Ten new built-in image-tool paintings; one previously supplied empty courtroom retained. Full prompts in art/prompts.json; raw PNGs in art/raw.
- Eleven final WebPs total 363.2 KiB. Final bundle 573.8 KiB (587,565 bytes), under 2 MB.
- No redraws; three object assets rekeyed with despill after edge inspection. No people, faces or body parts.

#### Art still to paint
None. All requested non-person images are present. Browser narration recordings remain unmade, as this build forbids recording.

#### Engine changes wanted
None.

#### Left open
- Browser speech is a fallback and is not a listening-reviewed Iapetus recording. No audio was recorded.
- Supplied Bus and Desks data are summaries only, so the admissibility view states the large-sample condition instead of inventing a dot plot. Cereal production-size and separate-wait independence are stated assumptions.
- Random simulations can occasionally fall outside typical tolerance bands; results are not clamped to expected values.
- The required bar inspection regenerated the ignored Snowy Mail Route and Beat Lab HTML bundles early in the build, outside the requested write area. No tracked bar source was edited.
- Full post-repair audit was not repeated. Browser narration was not listening-reviewed, and this build was not tested in a live classroom.
- Context sentence fragments use two compact native selectors rather than separate chip buttons, with free selection order and a live preview.

<!-- end part -->

## Self-check

<!-- part: codex-review.md -->

### Codex review: courtroom-statistics

#### Played

- Cold Grade 12 play: Seeds from folder to interval, then Lineup and Docket, before reading the builder's report, handoff, notes or source. Strong setting and restrained verdict; condition and approval loopholes weakened the reasoning.
- Played the main path with held clicks at 2-second intervals, plus keyboard-only to Sentencing. Checked all eight required sizes, Motion off, grayscale, the seven case types and Docket extremes.

#### Findings fixed

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

#### Findings left

- Should fix, spec/catalog: AP unit labels use the older U6/U7 numbering. Current College Board labels are U3/U4. Notes identify the migration; external catalog and spec remain unchanged under this review's scope rule.
- Should fix, spec/mapping: S-IC.B.4 requires developing margin of error with simulation; B.5 requires simulation of treatment differences. The prescribed analytical cases and coin-power simulation do not fully cover those clauses. Corrected notes to say partial coverage; adding a new simulation or changing the external mapping exceeds scope.
- Production limitation, voice: native speech remains the fallback. Recording and ear review of Iapetus were outside the authorized build workflow.

#### Break it

- Charges: tried all signs, including a wrong sign after a filed result. Wrong revisions lock later stages; corrected attempts remain identified.
- Conditions: ran all-Yes, repeated toggles, a wrong revision after filing, the paired trap and voluntary-response poll. All-Yes stays at Admissibility; a bad revision cannot reach Sentencing; the poll never reaches inference.
- Verdicts: tried Innocent, both decisions in succession and a changed alpha after filing. Old verdicts and filed results are cleared; Innocent never counts as a verdict.
- Context: enumerated all six strength/direction pairs and edited a correct filed sentence to a wrong one. Only the current correct pair files; revisions revoke prior filing. Corrections are retained rather than presented as first-attempt mastery.
- Standard: tried a Lineup peek, mode return and reopening. Evidence exposure and late-standard warnings persist. An early 0.01 change survives reopening without a late-change flag. Default-alpha selection is an open modeling choice, not a scored task.
- Lineup: swept the slider endpoints and compared bands with intervals. This is labeled exploration, with no score or mastery gate to farm.
- Docket: repeated runs, changed controls during bar growth and used both parameter extremes. Old simulations clear at once; exact and sampled shares remain distinct. No best score or reflection gate exists.

#### Voice walk

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

#### Facts checked

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

#### Sensitivity

- No cultural, Indigenous, religious or hard-history content. Seven fictional cases concern data, including clinic attendance and adult workers/runners; no medical advice or actual legal defendants. Notes explain that the courtroom is a teaching analogy, not legal guidance. No depicted people or stereotypes; all assets checked.

#### Flattest moment left

- The interval page is deliberately quiet and still mostly interpretation. Its payoff is the student's verdict beside the claim and interval; preserved the strong Lineup transition instead of adding celebration.

#### Graphics

- Inspected all 11 finished assets, their styles and case mappings. Preserved courtroom, folders, gavel, coin and six other evidence paintings. Redrew only cereal with built-in imagegen; prompt and raw PNG saved in the tool, previous art preserved in Scratch.
- New WebP is 680 x 510, about 37 KB. All art totals 377,260 bytes; bundle 600,853 bytes (about 587 KiB). Paintings now fit full frames, with more height on large screens and a label positioned from the actual painted rectangle. No missing art tokens; no people assets requiring people:true.
- Computed contrast: ink/panel 14.01, muted/panel 5.88, green/panel 5.76, header 10.46, focus/panel 6.38. The spec's muted ratio 6.35 is inaccurate; actual contrast remains strong. Compared the retained court finish with the existing Beat Lab comparison frame without rebuilding another tool.

#### Audit

- Ran scripts/audit_tool.py once on Chrome 9941, host 8745, with a 40-minute limit. It finished: 145 frames, all visually inspected, 18 leads. Motion off, mid-action resize, keyboard focus, five held clicks and quick double taps passed.
- One real lead was the compact Docket cutoff collision, repaired and re-shot. Independently caught and repaired the compact Lineup bracket crossing. Targeted scans and frames at 680x425 and 800x500, plus Docket at 375-wide, are clear of overlap, clipping and disabled-control instructions.
- Ten zero-font leads are intentional Motion/Sound icon buttons: visible 18-23 px glyphs, accessible names, 44 px targets. Seven first-folder taps skip the generic welcome and play the case instruction with the premise visible, as BASELINE rule 16 allows.
- Final before/after regressions confirm poll dismissal and the early-standard reopen fix. The first capture harness omitted a scan placeholder and used a nonmatching select value; corrected the harness and repeated only these focused checks. Final capture has zero console errors, warnings or exceptions. No second full audit or review.
- Evidence: _scratch/courtroom-statistics/review-audit/audit.md, review-final-confirm/, review-fixed/, review-walk/, review-number-results.json and the named before/after JSON files. The full audit preceded its compact-layout repairs; focused confirmations use the final bundle.

#### Left open

- Kept both proportion brackets and the light-oak theme, as the spec and baseline lean toward them. No unattended questions were left pending.
- Guided practice can be completed after corrections; it makes no mastery claim. Reloading intentionally clears the whole page session, as disclosed.
- No commits or shared-kit changes; all authored files remain in the two authorized folders. Temporary host removed and review-owned Chrome/server processes closed.

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### Courtroom Statistics build handoff

#### Structure
src.html starts from kit/starter/src.html, includes the shared kit and 9-12 theme, then applies the specified light oak tokens. Static stage sections and controls stay mounted while their visibility changes. Cases, inference routines, state transitions, and responsive SVG drawing live in the single script. __tool exposes the required test API plus goStage, cases, allLines and vlog.

#### Open questions resolved
- Keep both proportion brackets. The score-test non-rejection band and AP estimated-SE interval are both shown, with an explanation. The two-proportion score test fits the constrained null proportions for each claimed difference, rather than pretending a zero-difference pooled SE works at every claim.
- Use the light oak theme override. Retain kit/theme-912.css for its instrument controls and override its palette, header and chart colors in the tool.

#### Tricky parts
- One-sided Trial intervals use C = 1 - 2 alpha. Their relevant bound corresponds to the directional test, not both outside regions. Mean Lineup uses two-sided tests and C = 1 - alpha, giving exact duality. Proportion AP intervals are not exact score-test inversions.
- Numerical t tails use incomplete beta; critical values and score endpoints use bisection. Docket binomial PMFs use log-gamma and sum the rejection tail. The cutoff deliberately uses the spec's uncorrected normal-z rule.
- Cereal and shoes use real supplied data. Bus and desks have no raw observations, so no invented dot plots are drawn. The conditions card explicitly states that limitation and uses n at least 30.
- Stage tabs unlock in order. Alpha stays live after evidence, raises an objection and invalidates the current verdict and conclusion. Session summaries remain in memory. Mode switching preserves the Trial snapshot.
- Charts measure actual CSS pixels. Resize only redraws SVG, so gavel and Docket controls remain available.
- Browser speech is the fallback; clear-teacher / Iapetus is declared in voice/lines.json. No recordings were made.

#### Art
Ten new images were made with the built-in image tool. The previously supplied courtroom-empty.webp stays in use. Full source prompts are in art/prompts.json; raw PNGs are in art/raw. No people are used. Exact curves, brackets, chips and stamps are code, as specified.

#### Engine changes wanted
None. No shared-kit edits were made.

#### Cold review repairs
- Invalidating a charge, condition, verdict or filed sentence clears later approvals and stale session results. Answer selectors also invalidate a filed conclusion as soon as they change.
- Admissibility asks explicit mixed Yes/No questions. Corrections persist per case in the page's session record and are identified as guided practice, including after reopening. There is no mastery score.
- Evidence exposure and late-alpha flags persist across Lineup visits and case reopening. Previously chosen standards survive reopening so opening a folder does not silently change alpha.
- At true p = 0.50, Docket labels its second bar as a rejection rate and explains why the unshaded area is not Type II error.
- Stage changes hush obsolete speech. Voice manifest uses a high school clerk style; native browser speech remains unrecorded.
- Proof cards show the error tradeoff. Cereal evidence was redrawn with the box physically on the scale, using built-in imagegen; its prompt and raw PNG are preserved.
- Evidence paintings fit their full frames instead of losing objects to wide or phone crops. Large screens give the art more height; the cereal label follows the painted box on load and resize. Compact headers retain the privacy disclosure even when the session panel has little room.
- Audit paths use the revised condition answers, a real Lineup drag and an added Sentencing state.
- College Board revised the AP numbering for 2026-27 to Units 3 and 4. The legacy spec/catalog labels need an owner-level migration outside this review's write scope.
- The official Common Core text includes simulation requirements in S-IC.B.4 and S-IC.B.5. The specified analytical intervals and treatment tests support only parts of those standards; Docket's coin power simulation does not fill those clauses. Notes now state this limit. Changing curriculum mappings or adding a different simulation would exceed this review's spec and write scope.

#### Sensitivity
All seven cases are fictional statistical examples. The clinic case concerns appointment attendance, with no medical advice. The courtroom is a teaching metaphor, not legal guidance. No depicted people, cultural traditions, real defendants or historical trials. Keep the notes' limits on population generalization and legal analogy.

#### Next review
Follow REFINE.md for the next cold lenses. The original build report remains historical evidence; this review's repairs and curriculum limits are described above. Native narration still needs listening review when recorded clips are produced. No git commits were made.

#### Build verification and repairs
- One complete mechanical audit finished with 51 leads. Its 97 screenshots were visually reviewed. The report is in _scratch/courtroom-statistics/audit/audit.md.
- Afterwards, focused checks repaired the compact Standing Desks charge, stamp/header spacing, same-mode rapid taps that cut welcomes, the daylight loop under Motion off, hidden phone alpha labeling and Sound-button width changes.
- Charts now observe their own rendered size and redraw on the next animation frame, fixing flattened labels after the readouts take space. Sentencing has a dedicated compact arrangement and short bound note.
- Follow-up checks used an isolated Scratch bundle while the original audit finished, then checked the final primary bundle. The full audit and full size sweep were not repeated after these focused fixes.
- Compact real-click follow-ups reached Evidence for all six numerical cases, a verdict for Desks, and dismissal for the viewer poll. Keyboard-only Seeds reached Sentencing. All 75 Docket combinations matched scipy.
- Final audit-states.json also includes the two Docket extremes for the next review. The completed audit used the original nine named states, plus its automatic mode checks.
- The remaining zero-font header leads are intentional icon buttons: visible 18 to 23 px glyphs, 44 px targets and explicit accessible names. A case-folder first tap deliberately skips the general welcome and speaks the case instruction, as STANDARDS requires.
- The context builder uses two compact native selectors for sentence fragments, selectable in either order, with a live sentence preview and File sentence control.

#### Cold review verification
- The single cold-review audit finished with 18 leads and 145 inspected frames. Its report is _scratch/courtroom-statistics/review-audit/audit.md. Compact Docket cutoff labels and a visually detected Lineup bracket crossing were repaired, then checked at the affected sizes without repeating the full audit.
- Independent SciPy comparisons passed for six case statistics/tails, 30 intervals and 75 Docket settings. Held-click voice events passed 5/5; keyboard-only Seeds reached Sentencing; the default main path was walked with Motion and Sound on.
- Final before/after regressions preserve poll dismissal through subsequent answers and preserve a pre-evidence alpha change through reopening without a late-change flag. Final focused captures have no console errors, warnings or exceptions. Bundle: 600853 bytes.
- Temporary host removed. Review evidence, previous cereal art and scripts remain in the authorized Scratch folder.

<!-- end part -->

## Log

- 2026-11-25: codex-report.md folded in (last changed 2026-11-08)
- 2026-11-25: codex-review.md folded in (last changed 2026-11-08)
- 2026-11-25: handoff.md folded in (last changed 2026-11-08)

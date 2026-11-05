# Codex report: courtroom-statistics

## Built
- Grade 12 offline tool with Trial, Lineup and Docket, built from the kit starter.
- Seven illustrated made-up cases; ordered stages, condition checks, live tests, verdict/context sentence, intervals and session record.
- Score-test inversion for proportions, Student t and Welch inference for means, seeded binomial simulation and exact error/power calculations.
- Build only. No git commits, branch changes or polish round. Final report is held until checks finish, honoring the user's stop instruction.

## Numbers check
- Independently recomputed the six numerical cases with scipy before implementation: estimates, SD/SE, df, tails and all supplied intervals match the stated precision.
- Browser values match scipy within 0.000001 for statistics/tails and 0.00001 for critical values.
- All 75 Docket n/alpha/true-p combinations match scipy exact binomial tails to 0.0000000001; all cutoffs match.
- Cereal Lineup band equals its 95% t interval exactly: [363.7349714, 368.0650286].
- Seeds score band at 90%: [0.7389141, 0.8333445], versus AP [0.7426265, 0.8373735].
- Docket default seed: Type I simulated 0.054 vs exact 0.0443130; power simulated 0.624 vs exact 0.6225327.
- Contrast recomputation: ink/panel 14.01, muted/panel 5.88, brand/panel 5.76, white/brand 6.47, header 10.46, focus/panel 6.38. The spec's muted 6.35 differs; actual 5.88 still passes AA. Spec unchanged.

## Feel check
- Played Seeds through the complete trial, including an Innocent correction, conclusion filing and sentencing, using held clicks and then keyboard only.
- Best moment: the stamped verdict becomes a movable claim in Lineup, where a filled convicted square turns into a hollow not-convicted circle at the statistical boundary.
- Flat moment 1: the compact Evidence card crowded its readouts against the next action. Changed it to one readout row in compact landscape, with a separate two-row phone arrangement.
- Flat moment 2: the conclusion felt like scattered form fragments. Changed it to one live sentence preview with the two choices and File sentence together.
- Further build fixes: gave the Docket curves real room beside the bars and put the paired-sample trap beside the advance control in short windows.
- Compared the large evidence painting and court furniture with Snowy Mail Route and Beat Lab. The court uses restrained senior-grade feedback, rich evidence paintings and stamped decisions, without celebration.
- Comparison: _scratch/courtroom-statistics/bar-comparison.jpg. Full student result: play-frames-v2/student-sentencing.png.

## Done when
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

## Wave lessons
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

## Audit leads
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

## Frames looked at
- Both bar frames, all eleven finished art assets, six early screenshots and compact/phone repairs.
- Twelve play-check frames: full student path, keyboard path, objection, dismissal, pair trap, Lineup, Docket, interruption, Motion off and grayscale.
- All 32 full-size/mode screenshots reviewed in four contact sheets, with individual phone and compact checks.
- Targeted Evidence/Lineup/Docket frames, numerical-state frame, compact paired checks and final Docket laptop/preview frames.
- All 97 mechanical audit frames, all compact case follow-ups, chart and calm follow-ups, rapid-mode/stamp checks, Docket extremes and final package frames. Contact sheets remain in Scratch.

## Art made
- Ten new built-in image-tool paintings; one previously supplied empty courtroom retained. Full prompts in art/prompts.json; raw PNGs in art/raw.
- Eleven final WebPs total 363.2 KiB. Final bundle 573.8 KiB (587,565 bytes), under 2 MB.
- No redraws; three object assets rekeyed with despill after edge inspection. No people, faces or body parts.

## Art still to paint
None. All requested non-person images are present. Browser narration recordings remain unmade, as this build forbids recording.

## Engine changes wanted
None.

## Left open
- Browser speech is a fallback and is not a listening-reviewed Iapetus recording. No audio was recorded.
- Supplied Bus and Desks data are summaries only, so the admissibility view states the large-sample condition instead of inventing a dot plot. Cereal production-size and separate-wait independence are stated assumptions.
- Random simulations can occasionally fall outside typical tolerance bands; results are not clamped to expected values.
- The required bar inspection regenerated the ignored Snowy Mail Route and Beat Lab HTML bundles early in the build, outside the requested write area. No tracked bar source was edited.
- Full post-repair audit was not repeated. Browser narration was not listening-reviewed, and this build was not tested in a live classroom.
- Context sentence fragments use two compact native selectors rather than separate chip buttons, with free selection order and a live preview.

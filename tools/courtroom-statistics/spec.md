# Courtroom Statistics

## One idea
A significance test is a trial: the null hypothesis is the defendant, presumed innocent; you set the standard of proof
before you see the evidence; the evidence is how surprising the data would be if the defendant were innocent; and the
verdict is "guilty" or "not guilty", never "innocent". Then sentencing hands down the confidence interval, and the
Lineup shows that the interval is exactly the set of claims the court would not convict.

## Not like
- design-the-study (gr 12, same group): builds an experiment and runs one shuffle check. Here finished cases, the formal z and t tests, both kinds of error and power.
- fair-dice-investigation (gr 12, same group): chi-square and slope tests as detective work. Here one- and two-sample tests for proportions and means.
- sample-machine (gr 12, same group): where sampling distributions come from. Here they are used as the null curve.
- poll-workshop (gr 11): margin of error for a poll. Here intervals come out of the test, at the matching level.

## Who and how
- Grade 12, Statistics, Math: statistics. Students drive, in pairs (prosecution and defense) or alone; a teacher can project one case. 20 to 40 minutes (a case is about 6).
- Topic line: "significance tests and confidence intervals as a trial".
- Standards (module): S-IC.B; AP-STAT.U6; AP-STAT.U7.
- CCSS clusters: Trial serves S-IC.B.4 (sentencing: estimate with a margin of error), S-IC.B.5 (cases 3 and 6 compare two treatments in randomized experiments) and S-IC.B.6 (Admissibility: judge how the data were gathered). Lineup serves S-IC.B.4. Docket serves S-IC.B.5 and the error and power ideas in AP.
- AP-STAT.U6 (Inference for Categorical Data: Proportions): cases 1 and 3, Docket. AP-STAT.U7 (Inference for Quantitative Data: Means): cases 2, 4, 5, 6.
- tool.json: driver "students or teacher", minutes "20-40", modes ["Trial", "Lineup", "Docket"], grades_label "Grade 12".

## Screens and modes
Header: title, subtitle "Innocent until proven guilty." Modes `Trial` (opens first), `Lineup`, `Docket`. Kit buttons.
Stage: the painted courtroom (art: courtroom-empty) as a dimmed backdrop, with a bench strip across the top showing
the case name and the six trial stages as tabs that unlock in order. The current stage's card sits centered on the
stage over the courtroom, large: it is the focus. Panel: the stage's controls and the clerk's line.

### Trial (one case at a time; case picker shows 7 case folders)
The picker is a row of 7 painted manila folders (art: case-folder, the case name typed in code on the blank tab).
Opening a case shows its evidence picture (art: evidence-*) on the Charges card beside the claim.
Focus by stage: Charges, the claim card with its evidence picture; Standard of proof, the three α buttons on the card;
Admissibility, the three chips with the dot plot; Evidence, the null curve with the shaded tail (the largest thing on
the stage, readouts under it); Verdict, the three verdict buttons and the sentence being built; Sentencing, the
number line with the interval and the claim marker.
1. Charges: read the claim; pick the defendant (H0, filled in) and the charge, Ha: `<`, `>` or `≠` (one is right for
   the case's wording; a wrong pick gets the clerk's correction quoting the wording).
2. Standard of proof: lock α at `0.10`, `0.05` or `0.01` before evidence. After evidence, changing it makes the clerk
   object ("The standard was set before the evidence. Changing it now isn't fair to the defendant.") and the case is
   marked "standard changed" on its summary.
3. Admissibility: three checks as yes/no chips (random sample or random assignment; 10% condition or independence;
   large counts or nearly normal, with the data's dot plot for means). Each chip shows the numbers it rests on.
4. Evidence: the null curve (normal or t with its df) centered at the claim, the observed statistic marked, the tail
   (or both tails) shaded in the accent; readouts: statistic, SE, z or t, df, p-value (4 places).
5. Verdict (a painted gavel, art: gavel, swings down once beside the stamp when a verdict is pressed, 400 ms;
   still with Motion off): `Guilty (reject H0)`, `Not guilty (fail to reject H0)`, `Innocent (accept H0)`. Innocent is never right:
   the clerk explains "Not guilty means the evidence fell short, not that the claim is true." Then write the verdict
   in context: chips build a sentence ("At the 0.05 standard, there is convincing evidence that the true germination
   rate is less than 0.85.").
6. Sentencing: the confidence interval at the matching level (C = 1 - 2α for a one-sided charge, 1 - α for two-sided),
   drawn on a number line with the claim marked; readouts: estimate, critical value, margin, interval.

### Lineup
Focus: the number line with the moving claim marker, the not-convicted band and the interval under it, centered and
wide across the stage; the slider sits directly under the line. Pick a case. A slider drags the claimed value along the number line; the trial runs live (two-sided at the chosen α)
and the claim's marker turns "convicted" (filled square) or "not convicted" (hollow circle). The values never convicted
form a band; the confidence interval at C = 1 - α is drawn under it. For means the band and the t interval match
exactly. For proportions both brackets show: the band (the test uses the claimed p in its SE) and the AP interval
(uses p̂), which differ slightly; a note says why.

### Docket (errors and power)
Focus: the two-curve picture (null and true distributions of x) with α and power shaded, centered; the two bars sit
beside it on wide screens and under it on narrow ones. A painted coin (art: coin) sits on the Docket card's title.
A fair-coin court: H0 p = 0.5, Ha p > 0.5, reject when the count of heads x is at least k. Controls: n (20, 50, 100,
200, 400), α (0.10, 0.05, 0.01), the true p (0.50 to 0.70, step 0.05). `Hold 1,000 trials` simulates; two bars show
the share convicted when H0 is true (Type I) and when the true p is the slider's (power); exact values print beside the
simulated ones. The 1,000 trials are computed at once and the bars grow over at most 1 s; changing n, α or the
true p during the growth stops it and shows the new state at once. A two-curve picture (null and true distributions of x) shades α and power, and β as the unshaded part.

## Content
All cases are made up and labeled "made-up case".
1. Seeds: a seed company claims 85% germination for a shipment of 50,000. A random sample of 200 seeds: 158 sprout.
   Ha: p < 0.85. p̂ 0.79; SE0 = √(0.85·0.15/200) = 0.025249; z = -2.376; p = 0.0087. Large counts 170 and 30 (expected
   under H0); 200 is under 10% of 50,000. SE(p̂) = 0.028801. Intervals: 80% (0.753, 0.827), 90% (0.743, 0.837),
   98% (0.723, 0.857). Lineup band (score, 90%): (0.739, 0.833) versus AP interval (0.743, 0.837).
2. Cereal: the box says 368 g. A random sample of 25 boxes (data: 372.8, 359.1, 366.7, 362.0, 370.5, 365.2, 356.6,
   371.9, 368.1, 361.3, 375.0, 363.7, 367.5, 360.4, 369.6, 362.9, 376.7, 365.8, 358.5, 371.1, 364.6, 362.5, 368.4,
   365.0, 361.6). Ha: μ < 368. x̄ 365.9, s 5.2450, t = -2.002, df 24, p = 0.0284: guilty at 0.10 and 0.05, not guilty at
   0.01. Intervals: 80% (364.5, 367.3), 90% (364.1, 367.7), 98% (363.3, 368.5).
3. Reminder texts: a clinic randomly assigns 600 patients to get a reminder text or not; 246 of 300 texted and 222 of
   300 not texted kept their appointment. Ha: p_text - p_none > 0. Pooled 0.78; z = 2.365; p = 0.0090. SE (unpooled)
   0.033665. Intervals for the difference: 80% (0.037, 0.123), 90% (0.025, 0.135), 98% (0.002, 0.158).
4. Bus: the city says the mean wait is 10 minutes; a rider group logs 40 random waits: mean 10.6, s 3.1. Ha: μ > 10.
   SE 0.4902; t = 1.224, df 39, p = 0.114: not guilty at every standard. Intervals: 80% (9.96, 11.24),
   90% (9.77, 11.43), 98% (9.41, 11.79).
5. Shoes (paired): 12 runners run 400 m in old shoes and new shoes, order randomized. Old: 64.2, 71.5, 58.9, 67.3, 62.8,
   75.1, 69.4, 60.5, 66.7, 73.0, 63.6, 70.2. New: 62.4, 70.9, 56.5, 67.8, 61.7, 73.6, 69.2, 58.5, 67.0, 71.7, 62.7, 68.6.
   Ha: μ_diff (new - old) < 0. Mean difference -1.05, s 0.9060, SE 0.2616, t = -4.015, df 11, p = 0.0010. Intervals:
   80% (-1.41, -0.69), 90% (-1.52, -0.58), 98% (-1.76, -0.34). A trap chip: running it as two samples (the clerk
   points out the pairs).
6. Standing desks (two-sample, two-sided): 60 office workers randomly assigned; steps per hour at work, standing desks
   mean 256 (s 38, n 30) versus sitting 236 (s 35, n 30). Ha: μ_stand - μ_sit ≠ 0. SE 9.432, Welch df 57.6, t = 2.120,
   p = 0.0383. Intervals: 90% (4.2, 35.8), 95% (1.1, 38.9), 99% (-5.1, 45.1).
7. Viewer poll: a TV show says 92% of 1,000 viewers who called in agree. Dismissed at Admissibility (voluntary
   response); the clerk: "No random sample, no trial. A bigger pile of call-ins doesn't fix who chose to call."
Docket cutoffs (k = smallest count with (k - n/2)/√(n/4) ≥ z*, z* one-sided): at α 0.05, k = 14, 31, 59, 112, 217 for
n = 20, 50, 100, 200, 400. Exact Type I: 0.0577, 0.0595, 0.0443, 0.0518, 0.0494. Exact power at p 0.6: 0.250, 0.446,
0.6225, 0.890, 0.991 (normal approximation at n = 100: 0.641). n = 100: α 0.01 gives k 62, power 0.382; α 0.10 gives
k 57, power 0.763; at p 0.55 and α 0.05, power 0.241.

## Interactions in detail
- p-values: normal tail for z (one-proportion and two-proportion with pooled SE under H0); t tail with df n - 1 for one
  sample and paired; Welch t with Satterthwaite df for two samples. Shown to 4 places; under 0.0001 shows "< 0.0001".
- Critical values from the same distributions (t* with the same df); intervals use unpooled SE for proportions.
- Answers checked: Ha sign against the case's stored answer; verdict = (p < α) computed live, so a changed α changes
  the right verdict; the context sentence must use the case's parameter, direction and standard (chip order free).
- Case summaries (per case: α, verdict, standard changed or not) stay for the session; nothing stored on device.
- Every control stays live while anything animates (the gavel, the Docket bars, the curve shading when α changes):
  a tap acts at once and the readouts match the new state.
- Docket simulation seeded (`?seed=n` for tests); exact binomial tails computed in code (log-gamma sums).
- `window.__tool = {state, setMode, openCase(i), setAlpha(a), stats(), interval(C), lineup(v), docket(n,a,p)}`.

## Look
Light oak theme overriding kit/theme-912.css tokens (see Open questions): paper `#e9dcc6`, panel `#f8f1e4`, sections
`#fffaf2`, ink `#2b2119`, muted `#6b5a48`, button line `#8c7656`, header bar dark walnut `#4a3322` with text `#f8f1e4`,
ok `#2d6a1f`, warn `#8a2a1e`, focus `#1f4fbf`. Accent `--brand #1d6b47` (court green: the shaded tail, the gavel button,
the not-convicted band). Serif headings. Guilty and not guilty use words and a filled versus hollow marker, not color.
Contrast (computed): ink on panel 14.01:1; muted 6.35:1; brand on panel 5.76:1, on sections 6.23:1, on paper 4.78:1;
white on brand 6.47:1; header text on walnut 10.46:1; focus 6.38:1; button line 4.17:1; ok 6.33:1; warn 8.31:1.
No celebration: the verdict is read out and stamped.

## Art
Local FLUX (`scripts/localart.py`), no people. One style (from art/prompts.json): flat illustration, warm muted oak,
walnut and cream colors, soft daylight, clean simple shapes, calm.
- courtroom-empty (made 2026-10-27, review pending): "The interior of an empty small-town courtroom seen from the back:
  a raised oak judge's bench in front of a wall of plain warm oak paneling, a witness stand beside it, wooden railings
  and rows of wooden benches, plain cream plaster walls, tall bare windows with soft daylight"; 16:9; cutout no; people
  no; dimmed backdrop behind the stage cards.
- case-folder: "A single closed manila file folder with a blank tab, lying flat, seen from above, soft daylight, flat
  illustration, plain white background"; 4:3; cutout yes; people no; the 7 cases in the picker, each labeled in code
  on the blank tab.
- gavel: "A polished walnut judge's gavel with a brass band, lying at an angle beside its round sound block, soft
  daylight, flat illustration, plain white background"; 1:1; cutout yes; people no; swings once on a verdict (rotated
  in code around its handle end).
- coin: "A single plain silver coin with a smooth blank face and a ridged edge, seen from slightly above, soft
  daylight, flat illustration, plain white background"; 1:1; cutout yes; people no; the Docket card title.
- evidence-seeds: "Rows of small seed trays on a greenhouse bench, some seedlings sprouted green and some bare soil
  cells, a seed scoop beside them, soft daylight, flat illustration"; 4:3; cutout no; people no; case 1.
- evidence-cereal: "A plain cereal box with a blank cream front on a kitchen scale beside a bowl of cereal, soft
  daylight, flat illustration"; 4:3; cutout no; people no; case 2 (the box front stays blank; the "368 g" label is code).
- evidence-texts: "A smartphone with a plain glowing blank screen lying on a clinic waiting room counter beside an
  appointment card holder and a small potted plant, soft daylight, flat illustration"; 4:3; cutout no; people no; case 3.
- evidence-bus: "An empty city bus stop shelter with a bench and a blank timetable panel on a quiet street, a bus far
  down the road, soft morning light, flat illustration"; 4:3; cutout no; people no; case 4.
- evidence-shoes: "A worn pair of running shoes and a bright new pair of running shoes side by side on the lane lines
  of a red running track, soft daylight, flat illustration"; 4:3; cutout no; people no; case 5.
- evidence-desks: "An open office with one tall standing desk and one ordinary sitting desk side by side, each with a
  laptop with a blank screen, soft daylight, flat illustration"; 4:3; cutout no; people no; case 6.
- evidence-callin: "An old landline telephone beside a television with a plain glowing blank screen on a living room
  side table, soft evening lamp light, flat illustration"; 4:3; cutout no; people no; case 7.
Curves, number lines, Docket bars, chips, stamps, the bench strip and preview.svg are drawn in code (charts and labels).

## Voice
Bank voice `clear-teacher` (Iapetus; the court clerk: plain, steady). Not used by math 9-12 neighbors or group siblings.
`Curio.voice`, `scope: () => state.mode + ':' + state.caseId`. Case text, cards and readouts are read on screen; Read
speaks the hint.
- wTrial (how, Trial welcome; stale once a case is open): "Tap a case folder to open it. Then pick the charge and lock your standard of proof before you see any evidence."
- alphaLate (event, α changed after Evidence; stale on next case): "The standard was set before the evidence. Changing it now isn't fair to the defendant."
- innocent (event, Innocent pressed; stale on next verdict): "This court never finds a claim innocent. Not guilty means the evidence fell short. Tap Guilty or Not guilty."
- sentencing (how, first Sentencing; stale on a new case): "Now the sentence: the interval of values the evidence supports. Compare it with the claim marker on the line."
- wLineup (how, Lineup welcome; stale after the first slider move): "Drag the claim slider along the line. Watch which claims this court would convict."
- wDocket (how, Docket welcome; stale after the first run): "Pick a sample size and a true p, then press Hold 1,000 trials."
- dismissed (event, case 7 dismissed; stale on next case): "No random sample, no trial. Tap another case folder."

## Family engine
none (its distributions, tails and intervals are its own; it does not use data-desk or sampling).

## Sources
- S-IC.B: Common Core State Standards for Mathematics, Making Inferences and Justifying Conclusions, https://www.thecorestandards.org/Math/Content/HSS/IC/
- AP-STAT.U6 and U7: College Board, AP Statistics Course and Exam Description, https://apcentral.collegeboard.org/courses/ap-statistics
- Tests and intervals for proportions and means, Type I and II errors, power: OpenStax, Introductory Statistics 2e, chapters 8 to 10, https://openstax.org/books/introductory-statistics-2e/pages/9-introduction
- Duality of tests and intervals; score versus Wald interval for a proportion: OpenIntro Statistics 4e, 5.3 and 6.1, https://www.openintro.org/book/os/
- Welch df (Satterthwaite): OpenStax, Introductory Statistics 2e, 10.1 "Two Population Means with Unknown Standard Deviations", https://openstax.org/books/introductory-statistics-2e/pages/10-1-two-population-means-with-unknown-standard-deviations
- All cases are made up; every statistic, p-value, interval and Docket value above was recomputed in Python (scipy) on 2026-10-27.
- Checks run again (Python, scipy, 2026-10-29), all match the Content list: case 1 SE0 0.025249, z -2.376, p 0.0087,
  SE 0.028801, intervals (0.753, 0.827), (0.743, 0.837), (0.723, 0.857), score band (0.739, 0.833); case 2 n 25, mean
  365.9, s 5.2450, t -2.002, p 0.0284, intervals to 0.1; case 3 z 2.365, p 0.0090, SE 0.033665, intervals; case 4 SE
  0.4902, t 1.224, p 0.1141; case 5 mean difference -1.05, s 0.9060, t -4.015, p 0.0010 (run as two samples by
  mistake: t -0.49, p 0.63, which is why the trap chip matters); case 6 SE 9.432, df 57.6, t 2.120, p 0.0383, 99%
  interval (-5.1, 45.1) holds 0. Docket cutoffs and exact tails at n 20, 50, 100, 200, 400; worst case n 20 at α 0.01:
  k 16, Type I 0.0059. Binomial spread of a 1,000-trial share: 0.0069 at 0.05 and 0.0153 at 0.62, so a ±0.02 and
  ±0.05 band holds three spreads.

## Done when
1. Case 1 shows z = -2.376, p = 0.0087, and at α 0.05 a 90% interval (0.743, 0.837).
2. Case 2 is guilty at 0.05 and not guilty at 0.01 (p = 0.0284); its 98% interval (363.3, 368.5) contains 368.
3. Case 6 reads df 57.6, t = 2.120, p = 0.0383; its 99% interval contains 0 and its 95% interval does not.
4. Changing α after Evidence triggers the clerk's objection and marks the case; Innocent is always corrected.
5. Lineup on case 2: the not-convicted band at α 0.05 matches the 95% t interval to 0.01; on case 1 both brackets show.
6. Docket exact values match the Content list (for example n = 100, α 0.05: k 59, Type I 0.0443, power at 0.6 0.6225).
7. Focus: at 1366x768 and 1000x625 the current stage card (Trial; the null curve on Evidence), the number line
   (Lineup) and the two-curve picture (Docket) are each the largest thing on the stage, over the dimmed courtroom.
8. Tap while it plays: during the gavel swing or the Docket bars growing, a verdict, α, n or true p tap acts at once
   and the readouts match the new state; Docket's simulated shares land within 0.02 of exact Type I and 0.05 of exact
   power.
9. Every case folder shows its evidence picture; no image has people or lettering.
10. Every size in STANDARDS.md keeps the bench strip, the curve and the verdict buttons visible without page scrolling; keyboard only works; console clean, no network.

## Open questions
- [courtroom-statistics] For proportions, the test (SE from the claim) and the AP interval (SE from p̂) don't match exactly, so the Lineup shows two brackets. Keep both, or show only the AP interval with a note?
- [courtroom-statistics] The light oak theme overrides the dark 9-12 theme. OK?

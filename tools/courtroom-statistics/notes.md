## What it teaches
Students use significance tests and confidence intervals to judge statistical claims. They distinguish insufficient evidence from proof of a null claim, check the design before calculating, and compare Type I error and power.

## Key skills
- Choose a one-sided or two-sided alternative from a question.
- Set a proof standard before seeing the results.
- Check randomization, independence and sample-size or shape conditions.
- Interpret a p-value and write a conclusion about the population or treatment difference.
- Connect test decisions with intervals and compare error rates across sample sizes.

## Support at home
- Find a claim in an advertisement. Ask what evidence would count against it before discussing any results.
- Talk about a time when there was not enough evidence to decide something. Explain why this does not prove the claim true.
- Compare asking volunteers a question with selecting people randomly. Discuss who might be missed.

## A five-minute start
Open Seeds. Pick the charge, lock 0.05, and inspect all three admissibility checks. The null curve shows z = -2.376 and p = 0.0087. Decide the verdict and file the context sentence. The resulting 90% AP interval is (0.743, 0.837).

## Modes
- Trial: seven made-up cases, six ordered stages, a context sentence and a session record. The viewer call-in poll must be dismissed before evidence. Pair work can divide prosecution and defense.
- Lineup: drag a claimed value while the data stay fixed. Tests here are always two-sided. Mean-case non-rejection bands equal their t intervals. Proportion cases show the score-test band and the AP interval separately.
- Docket: compare two independent sets of 1,000 simulated binomial trials with exact values. Type I uses true p = 0.50; power uses a selected true p above 0.50. At true p = 0.50 both bars show Type I error, and failing to reject is correct. The dashed null curve and solid true curve have shaded rejection tails. When the alternative is true, the unshaded true area is beta.

## Talk questions
- Why must alpha be set before opening evidence?
- Why is “not guilty” different from “innocent”?
- How does a paired analysis use the runners more appropriately than two independent samples?
- Why can a larger call-in poll still be biased?
- Which claim values does the court fail to reject in Lineup?
- What happens to power when sample size increases while alpha and true p stay fixed?

## Good to know
All cases are invented. This is a teaching analogy, not a description of legal standards. A p-value is a tail probability assuming the null and model conditions; it is not a probability that the null is true. Statistical significance is not a measure of practical importance.

Trial uses central confidence level C = 1 - 2 alpha for one-sided alternatives and C = 1 - alpha for two-sided alternatives. For one-sided tests, compare the relevant bound in the direction of the charge. This does not mean every value outside a central interval is rejected by that one-sided test. Proportion AP intervals use an estimated SE and do not exactly invert score tests. Lineup shows that distinction directly.

Cereal and shoes have raw-data dot plots. Bus waits and desk steps have summary statistics only, so the tool states the large-sample condition without inventing individual observations. Cereal production size, separate bus waits, and independent runners are stated assumptions. Shoe inference is conditional on these runners and the paired model; randomized order alone does not make them a random population sample.

Docket uses a normal-z cutoff without a continuity correction, then evaluates exact binomial tail probabilities. Its integer cutoff can make actual Type I error exceed the planned nominal alpha, especially at small n. Simulated results vary and can occasionally fall beyond typical tolerance bands. Add ?seed=1729 to the HTML URL for reproducible trials.

Case conclusions stay in page memory and clear on reload. The tool sends no data and works offline. Kit Motion preferences may be remembered on the device. Read uses browser speech because fixed recordings were not produced in this build.

The Yes/No chips answer their written questions. Some questions ask whether a problem is present, so three Yes taps do not admit a case. A corrected charge, condition, verdict or submitted conclusion stays marked in the session record, including after reopening that case. This is guided practice, not a mastery score. Revising a filed answer clears later approvals until the reasoning is filed again. Seeing a case in Lineup also counts as seeing its evidence; a later Trial alpha change is flagged even after reopening.

Large sample sizes support a normal approximation but cannot rule out extreme outliers. The summary-only bus and desk cases explicitly assume their absence. Random assignment supports treatment comparisons for the participants; it does not create a random population sample.

## Standards and sources
- S-IC.B.4, partial: sentencing and Lineup estimate parameters with analytical intervals. This tool does not develop a margin of error through repeated-sampling simulation.
- S-IC.B.5, partial: reminder texts and standing desks compare randomized treatments analytically. Docket simulates coin-court errors and power, not the significance of a two-treatment difference.
- S-IC.B.6: students judge admissibility, including voluntary-response bias.
- AP-STAT.U6: one- and two-proportion inference and coin error/power exploration.
- AP-STAT.U7: one-sample, paired and Welch two-sample mean inference.
- The spec's AP unit labels are legacy numbering. College Board's revised 2026-27 course places proportion inference in Unit 3 and mean inference in Unit 4. The content remains relevant; catalog/spec code migration is left to the owner because this review cannot edit those files.
- The full simulation clauses of S-IC.B.4 and S-IC.B.5 need companion work, such as the sampling and study-design tools named in the spec. Do not treat this tool alone as complete coverage of those standards.
- Common Core Making Inferences and Justifying Conclusions: https://www.thecorestandards.org/Math/Content/HSS/IC/
- College Board AP Statistics: https://apcentral.collegeboard.org/courses/ap-statistics
- OpenStax Introductory Statistics 2e, chapters 8 to 10: https://openstax.org/books/introductory-statistics-2e/pages/9-introduction
- OpenIntro Statistics 4e, sections 5.3 and 6.1: https://www.openintro.org/book/os/
- Welch inference: https://openstax.org/books/introductory-statistics-2e/pages/10-1-two-population-means-with-unknown-standard-deviations
- Wilson score-test inversion: NIST/SEMATECH e-Handbook, https://www.itl.nist.gov/div898/handbook/prc/section2/prc241.htm

Illustrations generated with OpenAI gpt-image, edited for Curio Class. Existing courtroom backdrop drawn with FLUX.1-schnell (Apache 2.0), edited for Curio Class.

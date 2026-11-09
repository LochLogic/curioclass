## What it teaches
Students choose and interpret chi-square tests for face counts and winning-seat patterns, then test and estimate a regression slope. They distinguish evidence from proof and see how sample size changes false alarms and power.

## Key skills
- Spend a limited sample budget and keep a record of tests.
- Build expected counts from row and column totals.
- Compare cell contributions to a chi-square statistic.
- Use residuals, a slope test and a confidence interval to assess a link.
- Explain simulation variation, false alarms and power.

## Support at home
- Ask your learner why a short run of uneven die rolls does not prove that a die is unfair.
- During a familiar board game, discuss how you could check whether the first player has an advantage without buying anything.
- Ask what a confidence interval containing zero says about a proposed link.

## Five-minute start
Open Cases. Select a die, press Roll 100, then Test this die. Compare the observed bars with the dashed expected count. Ask what else the student would want to know before accusing it. Test help includes a complete worked example.

## Modes
Cases progress through three files. Case 1 has 1,200 rolls and two accusations. A second wrong accusation closes that file and opens Case 2. While rolls remain, Accuse requires a current test of the selected die. At zero budget, an untested accusation is an unsupported guess and cannot earn Case closed. This preserves onward access after a poor roll allocation. Selecting the true loaded die with p at or above alpha is labeled Loaded, not established, rather than Case closed. Uncertainty is intentional: an honest die may look suspicious and a loaded die may escape detection.

Case 2 compares three separate samples of 120 games. Drag a row total and column total into a cell. Keyboard alternative: select its row total, its column total, then the cell. Build three distinct cells to enable Fill the rest. Then use Point to the cell, select the largest contribution, and press File finding. Selection has no correctness feedback before filing. A wrong first finding remains Evidence reviewed, with the comparison shown; it never earns a Case closed stamp.

Case 2 uses alpha 0.05. Case 1 and Dice lab let students choose alpha. The slope case always reports a 95 percent interval.

Case 3 compares two independent invented data sets. Test both slopes, choose a link, then cite p-value or Interval. Enter that plot's actual p-value or interval endpoints and compare with alpha 0.05 or zero. File evidence commits the first conclusion. An unsupported conclusion stays in the record as Evidence reviewed; it cannot become Case closed by trying each answer. Shuffle the y values breaks pairing and displays 1,000 shuffled slopes. Its fraction is a simulation result, with variation.

Dice lab lets students adjust six relative weights. Percentages renormalize. All-zero relative weights use a fair die, explicitly stated on screen. The history identifies each weighted die by its six relative face weights, in face order, so compare rows with the same weights and alpha when studying sample size. Compare sample sizes using 1,000 investigations; fair dice estimate false alarm rate, weighted dice estimate power.

## Talk questions
- Why can testing every honest die produce a false accusation?
- Does a large p-value establish fairness? What does the sample fail to show?
- Why is the same expected count repeated across rows in this table?
- Why does a residual plot help with linearity and spread but not prove random sampling?
- How do a slope interval and a two-sided test agree at the 5 percent level?

## Good to know
The spec uses the legacy AP unit labels: AP-STAT.U8 is practiced in the goodness-of-fit, homogeneity and simulation activities. AP-STAT.U9 is practiced through testing and estimating both slopes. College Board revised AP Statistics for 2026-27 into five units. The catalog owner must review the legacy U8/U9 mapping; this tool preserves the requested activities. Independence tests are explained in help; there is no separate independence case.

The café, tournament, records and data are made up. The records assume independent random samples. The slope plot alone cannot establish normal residuals or study design. Association alone does not prove causation. Repeated testing while accumulating data changes the overall false alarm rate.

The hidden die probabilities are 1/8, 1/6, 1/6, 1/6, 1/6, 5/24. Case 1's limited budget is deliberately difficult. There is no gambling, money, score or celebration.

Solved cases save only on this device in `curio-dice-cases`. Clear asks before deleting this progress. Sound and Motion are kit controls; Read speaks the current hint. Fixed narration currently uses browser speech because recordings have not been supplied. Simulation completion is an event and is narrated on every run; instructions are spoken once.

Sources: College Board AP Statistics Course and Exam Description; OpenStax Introductory Statistics 2e, sections 11.2 and 11.4; OpenIntro Statistics 4e, sections 7.5 and 8.4. Illustrations generated with OpenAI gpt-image, edited for Curio Class.

## Review source checks
- Goodness of fit, expected-count condition, upper-tail test and df: [OpenStax 11.2](https://openstax.org/books/introductory-statistics-2e/pages/11-2-goodness-of-fit-test).
- Homogeneity, independent samples and expected counts: [OpenStax 11.4](https://openstax.org/books/introductory-statistics-2e/pages/11-4-test-for-homogeneity); general two-way df uses (rows minus one)(columns minus one).
- Slope standard error, two-sided t, confidence interval, conditions, and multiple comparisons: [OpenIntro Statistics 4e, 8.4 and 7.5](https://www.openintro.org/book/os/).
- Curriculum revision: [College Board AP Statistics](https://apcentral.collegeboard.org/courses/ap-statistics), checked 2026-11-08.
- All numerical records are invented. An independent Python recomputation in Scratch checks every displayed worked example, table cell, contribution, slope, p-value and interval. The false alarm percentages assume one independent test per honest die at a fixed sample size. Repeated and adaptive testing does not preserve that family error calculation.

Focused closing checks also name the filed die or explanatory variable on the main paper verdict, keep empty-die instructions valid at zero budget, and explicitly name the citation inputs for accessibility.

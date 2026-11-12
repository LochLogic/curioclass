# Topics with no standards file

Written 2026-11-11, from `data/modules.csv` (797 topics, read by script).

**Status of every topic below: not yet standards-checked; load the course framework when that course's scope and sequence is
written (Cory, 2026-11-11).**

These 26 topics carry codes from four frameworks that have no file in `data/standards/`. The checker
(`scripts/standards.py`) accepts their codes by pattern only (for example AP-CALC.U1 to U10), so nothing confirms
that a code means what the topic says it does. `data/modules.csv` was not changed. The Common Core codes some
of these topics also carry are checked as usual; the note is about the AP and APA codes.

Do not lose this: when the scope and sequence for one of these courses is written, load that course's framework first, then
check each topic's codes against it.

## What each course would need

| Course | Topics | Framework to load |
|---|---|---|
| precalculus | 7 | College Board, AP Precalculus Course and Exam Description (units 1 to 4) |
| statistics | 6 | College Board, AP Statistics Course and Exam Description (units 1 to 9) |
| calculus | 6 | College Board, AP Calculus AB and BC Course and Exam Description (units 1 to 10) |
| psychology | 7 | American Psychological Association, National Standards for High School Psychology Curricula |

Notes for whoever loads them:

- Load the edition that is current on the publisher's own site on the day, and record the edition and date in
  the file header.
- From memory, not verified: the APA standards were revised in 2022. The topic codes (APA.Biological and the
  like) should be checked against that edition's own grouping, which may differ.
- From memory, not verified: AP Statistics has a revised framework arriving for the 2026-27 school year. Check
  the unit numbering before trusting AP-STAT.U1 to U9.
- Read each publisher's reuse terms before storing anything beyond ids and unit numbers.

## The topics

### AP Precalculus (course id precalculus, grade 12)

| Topic id | Title | Codes with no file |
|---|---|---|
| math-12-functions-and-their-graphs | Functions and Their Graphs | AP-PRECALC.U1, AP-PRECALC.U2 |
| math-12-trigonometric-identities-and-equations | Trigonometric Identities and Equations | AP-PRECALC.U3 |
| math-12-vectors | Vectors | AP-PRECALC.U4 |
| math-12-matrices | Matrices | AP-PRECALC.U4 |
| math-12-polar-coordinates-and-complex-plane | Polar Coordinates and Complex Plane | AP-PRECALC.U3 |
| math-12-conic-sections | Conic Sections | AP-PRECALC.U4 |
| math-12-limits-and-rates-of-change | Limits and Rates of Change | AP-PRECALC.U1 |

### AP Statistics (course id statistics, grade 12)

| Topic id | Title | Codes with no file |
|---|---|---|
| math-12-exploring-data | Exploring Data | AP-STAT.U1, AP-STAT.U2 |
| math-12-sampling-and-experiments | Sampling and Experiments | AP-STAT.U3 |
| math-12-probability-and-random-variables | Probability and Random Variables | AP-STAT.U4 |
| math-12-sampling-distributions | Sampling Distributions | AP-STAT.U5 |
| math-12-confidence-intervals-and-significance-tests | Confidence Intervals and Significance Tests | AP-STAT.U6, AP-STAT.U7 |
| math-12-chi-square-and-regression-inference | Chi-Square and Regression Inference | AP-STAT.U8, AP-STAT.U9 |

### AP Calculus (course id calculus, grade 12)

| Topic id | Title | Codes with no file |
|---|---|---|
| math-12-limits-and-continuity | Limits and Continuity | AP-CALC.U1 |
| math-12-the-derivative | The Derivative | AP-CALC.U2, AP-CALC.U3 |
| math-12-applications-of-derivatives | Applications of Derivatives | AP-CALC.U4, AP-CALC.U5 |
| math-12-the-integral | The Integral | AP-CALC.U6 |
| math-12-applications-of-integrals | Applications of Integrals | AP-CALC.U8 |
| math-12-differential-equations | Differential Equations | AP-CALC.U7 |

No calculus topic carries AP-CALC.U9 or AP-CALC.U10.

### High school psychology (course id psychology, grade 12)

| Topic id | Title | Codes with no file |
|---|---|---|
| social-studies-12-brain-and-behavior | Brain and Behavior | APA.Biological |
| social-studies-12-sensation-perception-and-memory | Sensation, Perception and Memory | APA.Biological, APA.Cognition |
| social-studies-12-learning-and-development | Learning and Development | APA.Development and Learning |
| social-studies-12-lifespan-development | Lifespan Development | APA.Development and Learning |
| social-studies-12-social-psychology-and-mental-health | Social Psychology and Mental Health | APA.Sociocultural |
| social-studies-12-personality-intelligence-and-motivation | Personality, Intelligence and Motivation | APA.Individual Variations |
| social-studies-12-psychological-disorders-and-treatment | Psychological Disorders and Treatment | APA.Mental and Physical Health |

No psychology topic carries APA.Scientific Inquiry.

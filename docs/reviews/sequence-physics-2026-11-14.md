# Sequence read: Physics (grade 11), 2026-11-14

Expert cold read of the Physics scope and sequence, done to docs/pipeline/briefs/sequence-read.md with subject science and the bar docs/RUBRIC-SCIENCE.md. Read blind: no Codex read of this course was opened. This report also holds the Across the band section for Biology, Chemistry and Physics.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/GLOSSARY.md, docs/pipeline/briefs/sequence-read.md, docs/pipeline/briefs/sequence-write.md, docs/lenses/science.md, docs/RUBRIC-SCIENCE.md.
- docs/courses/physics/frame.md, docs/courses/physics/scope-and-sequence.md, data/plans/physics/days.csv (all 160 rows, every column).
- data/progressions/science.csv (Physics rows and what they assume), data/standards/ngss-pe-dimensions.csv for the 20 owned codes.
- data/plans/calendar.csv (grade 11 rows: Algebra II, ELA 11, US History I) and docs/CALENDAR.md.
- data/plans/science-grade-6, -7, -8, biology and chemistry days.csv, to find each assumed row's last use.
- The "Settled by the expert" tables and "Across the band" sections of docs/reviews/sequence-science-grade-*-2026-11-14.md, and docs/courses/science-grade-8/frame.md's high school hand-off lines.
- Gates: `scripts/plan.py check`, `scripts/frame.py calendar`, `scripts/stale.py check`. Physics passes all three. The only plan failure is english-language-arts-kindergarten (no scope file yet), from the Codex ELA run under way, not this course.

## Verdict

A careful sequence: every grade 8 row it needs gets a readiness check in the right slot with a reserved reteach on the unit's second day, the orbit and energy work stays inside the math students have, and the course-level checks avoid repeating the unit just assessed. Two rows last used in Biology (grade 9) are treated as retrieval where the counted rule needs readiness. Three end days put three expectations in one period, two of them with visual, spoken and written communication on a new case, and the course-level checks claim every part. All fixes fit inside existing days.

## Findings

### 1. Moderate: two grade 9 rows need readiness, not retrieval (sequence, frame; REPEAT yes; firm for the first row, likely for the second)

What is wrong. The frame's Seams table (lines 41, 63, 64) gives retrieval to bio-sources-of-variation (unit 7) and s6-plate-evidence (unit 9), both last used in grade 9. Under the counted rule a row last used in grade 9 gets a readiness check in grade 11. This is the known gloss fault ("two or more grades between"); these are the rows it changes in Physics. Day 94 retrieves bio-sources-of-variation; day 129 retrieves s6-plate-evidence "kept in Biology" and says "Only idle surface-change scales get readiness".

For s6-plate-evidence, Chemistry day 32 retrieves the plate model, but no Chemistry day names the row itself, so its last use is grade 9 (Biology unit 8, where it now gets a readiness check). That is why this one is likely rather than firm.

Why it matters. Unit 7's radiation claims rest on ultraviolet light changing DNA, and unit 9's crust-age argument rests on plate evidence; both were last met two years earlier.

Fix (no day added; both units already reserve a reteach on their second day).
- Day 92: add bio-sources-of-variation to the last-ten-minutes check beside s6-light-paths; day 94's reteach covers both. Change day 94's note from "Retrieval: bio-sources-of-variation" to "respond to day 92 readiness".
- Day 127: add s6-plate-evidence to the check beside s6-surface-change-scales; day 129's reteach covers both. Delete "Only idle surface-change scales get readiness" from day 129's note.
- Scope and sequence: line 7's "Units 2 and 5 use retrieval instead" stays true, but the unit 7 and unit 9 paragraphs must name the added rows. Frame fix pass: lines 41, 63 and 64 become "last used in grade 9: readiness check".

### 2. Moderate: three end days carry three expectations in one period (sequence; REPEAT new; firm on the rule, judgment call on the split)

What is wrong. Day 91 (HS-PS4-1, HS-PS4-2, HS-PS4-5), day 126 (HS-ESS1-1, HS-ESS1-3, HS-ESS1-2) and day 144 (HS-ESS2-3, HS-ESS2-1, HS-ESS1-5) each ask for full performances on three codes in fifty minutes. Days 91 and 126 also require visual, spoken and written communication on the new case, because the scope and sequence says named products "do not replace the unseen case". sequence-write.md rule 2 says to spread such days over the unit's last days, and lets a product stand for a code where the day says so.

Why it matters. Every student giving a spoken explanation, plus written prompts on every part of three codes, does not fit one period; the communication mode is what will be cut.

Fix.
- Day 91: the day 90 technical explanation (visual, spoken and written; kept inside day 89 when day 90 folds) stands for HS-PS4-5's communication modes, and day 91's note says so. Day 91 keeps written prompts per part on the unseen medium, digital question and device.
- Day 126: the day 119 element-formation communication (visual, spoken and written) stands for HS-ESS1-3's communication modes, and day 126's note says so. Day 126 keeps written prompts per part on the new star system and cosmic evidence.
- Day 144: day 143 becomes end part 1 (HS-ESS2-3, the interior model on new evidence); day 144 is end part 2 (HS-ESS2-1, HS-ESS1-5). The Shorter path then folds day 136 into 135 in place of 143 into 142. Judgment call on that fold-in: 135 and 136 both apply the HS-ESS2-1 uplift and erosion model.
- Rewrite the scope and sequence's line 9 so a named product may stand for a communication mode where the day says so.

### 3. Moderate: course-level checks claim every part of every code (sequence; REPEAT yes, the K to 8 reads' finding; firm)

What is wrong. Day 64 lists four codes, days 156 and 157 three each, and every check day's note says "Every listed code needs evidence for every part". The scope and sequence (line 107) says the check slots "retain every part of every code".

Why it matters. Four full expectations cannot be evidenced in fifty minutes; the claim overstates coverage.

Fix. As settled in grades 6 to 8: each check day names the parts its block samples and calls itself a sample; full coverage stays with the end-of-unit assessments. Rewrite line 107 and the check-day notes on days 63, 64, 107, 108 and 156 to 158 to match.

### 4. Minor: day 117 overstates where heavy elements come from (sequence; REPEAT new; judgment call)

Day 117 says heavier nuclei form "in massive-star explosions". Much of the heaviest material also comes from neutron star mergers and from slow neutron capture in ageing stars. The code's clarification names supernovas, so this is not wrong for the code, but an absolute statement goes beyond the evidence (S10). Fix: "beyond iron, mainly in massive-star explosions and neutron star collisions", with the unit plan's data set chosen to match.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Readiness on day 1 (unit 1), days 30, 46, 76, 92, 109, 127, 145, each with the reteach on the unit's second day | Counted rule; slots match the readiness-timing decision | data/plans/physics/days.csv |
| Units 2 and 5 open with retrieval | Their rows were used earlier this year (units 1 and 3) or in Chemistry (grade 10) | docs/courses/physics/scope-and-sequence.md |
| Chemistry rows and models (attraction, energy accounting, fusion and half-life, energy budget, weathering, plate-model, rock-cycle, computational-model, design-cycle, earth-sun-moon, wave-model) stay retrieval | Chemistry days teach or assess them in grade 10 | data/plans/physics/days.csv days 31, 41, 48, 59, 111, 129, 147 |
| End days with two codes (17, 45, 61, 105) stay single days | A short prompt per part fits two codes in fifty minutes | data/plans/physics/days.csv |
| Unit 5's no-kit path stays, marked weaker for conduct | The scope and sequence already says it cannot establish physical conduct | docs/courses/physics/scope-and-sequence.md |
| No base text, no source map | Frame line 10: Curio Class's own, reference units for ideas only | docs/courses/physics/frame.md |

## For Cory

None.

## What is right and should not be touched

- The orbit work stays two-body, with T squared = a cubed only for Sun-centred orbits in years and astronomical units and a supplied coefficient for moons and satellites; no vector components or calculus.
- Same-year leans are honest: Algebra II rational exponents (days 46 to 69) avoided in unit 3; physics wave mathematics (days 79 to 82) before Algebra II trigonometry (days 113 to 136); radiometric work (days 141 and 149) after Algebra II exponentials (days 73 to 95); ELA 11 writing units finish before physics communication days. Check weeks 13, 22 and 32 match calendar.csv.
- Safety is conservative and specific: carts on the floor with a stop and nobody riding, alkaline 1.5-volt cells only with current limiting, no strong magnets near medical devices, teacher-poured warm water, damp sand crater trays.
- Sensitivity notes on crash injuries, radiation worry and deep time ask no student to disclose or renounce anything.
- Coverage table traces all 20 codes; candidate cells settled at zero added days; Shorter path present with ten fold-ins.

## Across the band

Patterns across Biology, Chemistry and Physics, the hand-offs between them, and the hand-off from grade 8.

1. **The readiness gloss is in all three frames, not just two.** Biology's frame says "idle two or more grades" and then treats every grade 7 row as one grade idle, which costs it readiness checks in seven units (Biology finding 1). Chemistry's scope and sequence corrected its frame on its own; Physics corrected it for grade 8 rows but not for grade 9 rows. The frame fix pass should cover all three frames' Seams and Models carried wording.
2. **"Maintained" or "kept in use" claims hide idle rows.** s6-insulator-design "kept in use through Biology" (Chemistry), s6-plate-evidence "maintained by s7-resource-distribution" (Biology day 113) and "kept in Biology" (Physics day 129). None of these is a day that teaches or assesses the row. Writers should check each such claim against the earlier grade's days.csv.
3. **Course-level checks claim every part in all three courses** (Biology days 44, 45, 156; Chemistry days 54, 101, 156, 157; Physics days 63, 64, 107, 108, 156 to 158). The grades 6 to 8 fix, samples with the parts named, applies to all three.
4. **End days.** Biology (four codes on days 42 and 74) and Physics (three codes on days 91, 126, 144) overload single end days; Chemistry avoids it by saying which carried product stands for which code. Chemistry's day notes on days 73 and 129 are the pattern for the other two.
5. **Math rows and readiness: one rule needed.** Chemistry gives readiness checks to grade 8 math rows (scientific notation day 41, powers of ten day 130). Biology retrieves grade 6 and 7 math leans with no readiness, and Physics retrieves "grade 8 calculator roots" (unit 3) and Algebra I work as retrieval. Under the counted rule, a math row last used in grade 8 would need readiness in grade 10 or 11 unless a science or math course used it in between, which nobody has traced. The lead should say whether the readiness rule covers math leans in science courses and, if so, who traces their last use.
6. **Grade 8 hand-off into Biology and Physics.** Every s8 row that Biology and Physics assume is taught or assessed on a grade 8 day, so the hand-off is delivered. Two lines in docs/courses/science-grade-8/frame.md are stale: line 140 says the light-ray model is used by no high school row, but Physics unit 7 reteaches s6-light-paths (reflection, absorption, transmission), the row that model carries (either add light-ray to phys-wave-particle-light's model_in or reword line 140; judgment call); and line 143's "Biology unit 8 picks the plate model up with a retrieval task" becomes a readiness check under the counted rule.
7. **Biology to Chemistry.** Bond energy, the carbon cycle, the computational model, Earth and life feedback and the engineering practices are retrieved where Chemistry needs them (days 17, 32, 57, 113), and stay retrieval once Biology adds its checks.
8. **Chemistry to Physics.** Electric attraction (Physics day 31), energy accounting (days 48, 59), fusion and half-life (days 111, 141, 147), the energy budget (day 111) and weathering (day 129) are all retrieved at first use. The periodic table hand-off the Chemistry frame names for Physics units 8 and 9 is used through chem-atomic-structure-periodic-patterns on day 111.
9. **Calendar.** Check weeks across the band are 9, 16, 32 (Biology), 11, 20 to 21, 32 (Chemistry) and 13, 22, 32 (Physics), with no stagger break in any grade.
10. **No base text in any of the three**, so no source map; each frame names the reference units as ideas only. That is consistent and correct.

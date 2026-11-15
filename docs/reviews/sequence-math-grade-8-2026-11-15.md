# Sequence read: math grade 8, 2026-11-15

Expert cold read of the Curio Class math grade 8 scope and sequence, done under docs/pipeline/briefs/sequence-read.md with the bar in docs/RUBRIC-MATH-K8.md and the math lens. Third of three middle school math reads; this report carries "Across the band" for grades 6 to 8.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/GLOSSARY.md, docs/pipeline/briefs/sequence-read.md and sequence-write.md, docs/RUBRIC-MATH-K8.md.
- docs/courses/math-grade-8/scope-and-sequence.md in full; docs/courses/math-grade-8/frame.md (course in brief, focus, units, course-level checks, cross-subject).
- data/plans/math-grade-8/days.csv (160 rows) and source-map.csv (170 rows).
- data/progressions/math.csv, grade 4 to 8 rows; data/plans/math-grade-4/6/7/days.csv for the last use of every assumed row.
- The base: Illustrative Mathematics grade 8, 1st edition (S:\CurioClass-sources\illustrative-math\grade-8), every lesson's title, teacher learning goals, student goals and the unit overviews for optional lessons.
- docs/courses/CALENDAR.md and data/plans/calendar.csv for grade 8; the science grade 8 read (2026-11-14) and science grade 8 days for the leans.
- Earlier reads: math kindergarten to grade 7 (2026-11-15), above all grade 5's "Across the band", and my grade 6 and 7 reads today.
- Gates: `plan.py check` passes for math-grade-8 (a failure elsewhere, a course another run is writing now); `sequence.py check math-grade-8` 0 failures with one note (8.F.A.3 "on no day" in unit 3, a frame punctuation fault the scope and sequence already flags; finding 8); `frame.py calendar` math weeks 14, 24, 32, no stagger break; `stale.py check` 0 failures.

## Verdict

A strong, well-argued course: IM's lesson order is kept, the one unit move (data before equations) has a reason that holds and puts scatter plots ahead of the science days that need them, readiness is right by grade number, and the shared 8.G.A.5 and the begun function codes are handled with care. As in grades 5 to 7, the weak layer is the course-level checks: all four are critique or reconstruction forms, three list 11 to 15 codes for 35 minutes, and the year-end pair never has students solve a linear equation on their own, so the named fluency 8.EE.C.7 is not sampled directly. The rest is reporting and tidying: an understated focus count, untagged retrieval rows, stale notes, one close paraphrase and a third source-map layout.

## Findings

### 1. The year-end check does not sample 8.EE.C.7 directly (serious)

- What is wrong: the frame names 8.EE.C.7 (linear equations in one variable, including rational coefficients, distribution and collecting like terms, and the one, none or infinitely many solution forms) as the grade's fluency. Day 159 lists 8.EE.C.7, 7a and 7b inside "a model-selection decision tree joining rates, equations, systems, functions and scientific notation", with "short entries" per part. Students choose and justify a model; no item asks them to carry a multi-step equation to its solution with no supplied steps. The last direct sample is day 91.
- Why it matters: the band rule says every year-end check samples each fluency standard directly. Equation solving is the skill Algebra I uses on its first day; the day 160 hand-off needs a current independent record of it, not a record of choosing among models.
- Fix: on day 159 give the decision tree 30 minutes and add a 10-minute untimed independent station of four equations: one needing distribution, one with variables on both sides and like terms, one with fraction or decimal coefficients, and one that reduces to a false or a true statement (7a). Students show every step; no supplied work. Name it in the note and the scope and sequence's check table as "direct fluency sample". Add m8-linear-equations to the day's skills.
- Evidence: days.csv days 91, 159, 160; frame fluency line; grade 5 "Across the band", grade 6 finding 1, grade 7 finding 1. Confidence: firm. LAYER: sequence. REPEAT: yes.

### 2. The course-level checks overclaim coverage and are all critique forms (moderate)

- What is wrong: day 116 lists 13 codes, day 158 11 and day 159 15, each with "short prompts for every part of every listed code" in 35 to 40 minutes. The four forms are: select and repair claims in a dossier (day 70), reconstruct missing representation matches (116), judge and repair a supplied design (158) and a decision tree (159). None asks for a solution produced from a blank page.
- Why it matters: two to three minutes a code cannot show reasoning, and every end-of-unit assessment already covered its codes in full. Four critique forms in a row show whether a student can spot good reasoning, not whether they can produce it. Day 116 also lists unit 6's function codes two days after day 114 collected them, so under collect once it should reuse that record, not re-prompt it.
- Fix: list only the codes each check samples, and say in the note and check table that the course-level check samples named parts across units. Proposals: day 116 samples 8.EE.C.7b, 8.EE.C.8b and 8.EE.C.8c from unit 5 (ended day 91) in a new context, and reuses the day 114 record for 8.F and 8.G.C.9; day 158 samples 8.G.A.2, 8.G.A.3 and 8.G.A.4 and reuses the day 156 record for 8.EE.A.2 and 8.G.B.6 to B.8 (two days back); day 159 samples 8.EE.B.6, 8.EE.C.7 (the station in finding 1), 8.EE.C.8b, 8.F.A.2 and 8.EE.A.4. Give day 116 and day 158 one short blank-page item each (solve a system by substitution; describe a sequence of moves taking one figure to another) beside the critique.
- Evidence: days.csv days 70, 114, 116, 156, 158, 159. Confidence: likely. LAYER: sequence. REPEAT: yes (grade 6 finding 2, grade 7 finding 2, science band finding 2).

### 3. The focus count is understated and computed unlike grades 6 and 7 (low)

- What is wrong: the scope and sequence credits 45 minutes on the 116 days whose codes are entirely major clusters, gets 5,220 of 8,000 minutes (65.25 percent), and its "For the lead" item 2 says the frame's 81 percent "is not established". Counting the days file: 120 of 160 days list only grade 8 major codes (75 percent of days); weighting mixed days by their code share gives about 129 days (80 percent), which agrees with the frame. Grade 6 reports strict and connected minutes; grade 7 counts each minute once per day.
- Why it matters: the reported figure sits on the 65 percent line and invites a "fix" that is not needed, and the three courses cannot be compared.
- Fix: replace the paragraph at line 44 with the day count (120 of 160 days wholly major, about 80 percent weighted) and, when unit plans are written, the grade 7 method (a per-day major-minute allocation, each minute once). Close "For the lead" item 2.
- Evidence: days.csv codes column; scope-and-sequence.md lines 44 and 154; frame focus line. Confidence: firm on the counts. LAYER: sequence. REPEAT: new.

### 4. Grade 7 retrieval rows are named in notes but not tagged in the skills column (low)

- What is wrong: 19 day notes retrieve grade 7 rows (m7-two-step-equations, m7-proportional-graphs, m7-rational-multiply-divide and 14 more); no day lists any m7 row in its skills column. Grade 7 tags its m6 retrievals (22 days, all in skills).
- Why it matters: the next grade's last-use check reads the skills column. Untagged, a reader or gate sees no grade 8 use of these rows, which does not change readiness (retrieval does not reset last use) but hides where Algebra I can expect them warm.
- Fix: add each retrieved m7 row to the skills column of the day whose note names it.
- Evidence: days.csv notes and skills; grade 7 days.csv. Confidence: firm. LAYER: process. REPEAT: new.

### 5. Stale "provisional" grade 7 last-use notes (low)

- What is wrong: the readiness section and several day notes say grade 7 last use is provisional, awaiting grade 7's days. Grade 7's days.csv exists. I checked every m7 row the course assumes: each is taught or assessed on grade 7 days, so retrieval is right. m6-four-quadrants and m6-exponents were only retrieved in grade 7, so the day 1 and day 92 readiness checks are right, as is the m4-symmetry check on day 1.
- Fix: drop the "provisional" wording from the scope and sequence and day notes, and close the matching lead item as verified.
- Confidence: firm. LAYER: process. REPEAT: yes (grade 6 finding 6).

### 6. Day 144's goal is a close paraphrase of the base goal (low)

- What is wrong: "Explain an area-rearrangement proof of the Pythagorean theorem" is 0.83 similar to base 8.8.7's teacher goal, keeping its frame and most of its words.
- Fix: "Rearrange four copies of one right triangle inside a square two ways and use the leftover areas to show why a squared plus b squared equals c squared."
- Evidence: base 8.8.7 learning goals; days.csv day 144. Confidence: firm. LAYER: base text. REPEAT: yes (grade 6, day 46).

### 7. The source map is in a third layout (low)

- What is wrong: columns base_lesson, source_url, stretch, unit, day, decision, reason. Grade 6 uses base_lesson, base_title, course, stretch, day, decision, reason, omitted_activities, source_url, license; grade 7 a second layout.
- Fix: rewrite in the grade 6 layout. Lead call below.
- Confidence: firm. LAYER: process. REPEAT: yes (grade 7 finding 6).

### 8. Frame unit 3 code list uses a comma (low)

- What is wrong: the frame's unit 3 codes read "8.EE.B.5; 8.EE.B.6; ~8.F.A.3, ~8.F.B.4", so the gate reads "~8.F.A.3, ~8.F.B.4" as one code and reports 8.F.A.3 on no day. The scope and sequence already flags it.
- Fix: in the frame, change the comma to a semicolon.
- Confidence: firm. LAYER: frame. REPEAT: yes (grade 6, 6.EE.A.1).

## Checks the brief asks for

- **Source map against the base:** every lesson in IM 8.1 to 8.9 has a row (131 base lessons). Decisions: 121 keep, 10 cut, 39 ours, no merges. All ten cuts are IM-optional (8.5.17, 8.5.18, 8.5.22, 8.6.11, and 8.9.1 to 8.9.6, the optional unit); reasons hold.
- **Base order and the one departure:** kept inside every unit. IM unit 8.6 (associations in data) moves to unit 4 (days 56 to 69), before IM 8.4 (equations) and 8.5 (functions and volume). The reason holds: scatter plots and lines of fit need only unit 3's lines and slope, and the move puts them before science 8 uses bivariate data (science days 77 and 105). Function language on scatter plots stays informal until unit 6.
- **Our words:** all 121 base-linked goal cells compared with their base lessons' titles, teacher goals and student goals. One close paraphrase at 0.83 (day 144, finding 6); the next highest is 0.65. **Copy rate: 1 of 121 (0.8 percent).**
- **Focus:** finding 3. Units 1, 2, 3, 5 and 7 hold only major clusters; supporting 8.NS and 8.SP, and additional 8.G.C.9, are confined to units 4, 6 and 8.
- **Coherence into Algebra I:** slope from similar triangles (unit 2) to y = mx + b (unit 3) to lines of fit (unit 4), multi-step equations and systems solved algebraically (unit 5), functions as a rule with graphs, tables and qualitative descriptions (unit 6), integer exponents and scientific notation (unit 7), square and cube roots, irrational numbers and Pythagorean distance (unit 8). These are the entry points of Algebra I's linear functions, systems, exponent rules and S-ID data units. The begun 8.F.A.3 and 8.F.B.4 in unit 3 complete in unit 6 with the scope and sequence saying so.
- **Rigor:** each unit has understanding, practice and application days. Fluency 8.EE.C.7: explained on days 72 to 80, practised on fluency days 75 to 79 and 90, then a 5-minute untimed mixed opening on later days ("no student timer"). Only the year-end sample is missing (finding 1).
- **Readiness:** verified by grade number (finding 5). m4-symmetry, m6-four-quadrants (signed coordinates) checked in the last 10 minutes of day 1 after the hook, rebuilt on day 2; m6-exponents checked in the last 10 minutes of day 92 (the respond day between units 5 and 6) and rebuilt on day 105, just before volume formulas need squares and cubes. Every m7 row is retrieved. No check on a unit's first day apart from unit 1's start-of-year check.
- **Assessments and end days:** every unit has an end-of-unit assessment and one respond day; each end day holds at most one extended task, with longer performances retained from the named closing teaching day. Mid-unit assessments are short and embedded (days 11, 28, 44, 62, 81, 104, 126, 145), each with its response counted once. 8.G.A.5 is shared by the frame: unit 1 carries the transversal and triangle-sum arguments (days 15 to 17), day 19 rightly leaves the code off, and day 35 completes it with the angle-angle record. That is correct.
- **Collect once and non-repeating checks:** end days reuse retained products; check forms change and draw on earlier units, and the scope and sequence says so (day 70 uses unit 1 to 3 figures and lines for the recent data unit; day 158 uses units 1, 2 and 6 for unit 8 skills). Day 116's re-prompting of day 114 is finding 2.
- **Standards in full:** every lettered part of 8.G.A.1, 8.EE.C.7 and 8.EE.C.8 is carried by teaching days.
- **Days by load:** units follow the frame's counts; equations and systems and functions with volume get the longest runs, as their content needs.
- **Calendar:** checks on weeks 14, 24 and 32, the CALENDAR.md targets. Leans: science 8 qualitative graphs (science days 1 to 46) come before math 8.F.B.5 (unit 6), and science carries its own bridge; scatter plots (math days 56 to 60) come before science days 77 and 105; scientific notation (math days 128 to 136) comes after science unit 4 (days 77 to 104), which uses powers of ten only (5.NBT.A.2) and avoids scientific notation. Each holds.
- **Candidate cells:** all settled.
- **Shorter path:** present, with a 45-minute plan and ten named fold-in days, none assessed.

## Lens checklist

| Lens item | Holds | Note |
| --- | --- | --- |
| Major work share | yes | about 80 percent of days; reported low (finding 3) |
| Progression coherence | yes | begun codes completed and named |
| Standard taught in part with no finishing day | yes | 8.G.A.5 shared and finished on day 35 |
| Problems that join units | yes | volume as a function, lines of fit from unit 3 lines, design audit |
| Fluency spaced and mixed | yes | year-end sample missing (finding 1) |
| Practices named | yes | all eight, tied to days |
| Models consistent | yes | slope triangles, balance and hanger, tables to graphs, area proofs |
| Readiness by grade number | yes | verified against grade 4, 6 and 7 days |
| End days not stacked | yes | one extended task per end day |
| Collect once | partly | day 116 (finding 2) |
| Our words | yes | 0.8 percent |
| Source-map layout | no | finding 7 |

## What is right and should not be touched

- The data unit before equations, with its reason, and the science timing it buys.
- The shared 8.G.A.5 record and the "begun in unit 3, owned in unit 6" function codes, each named in notes.
- Short embedded mid-unit assessments with one response allocation each.
- Supplied neutral data: no body measures, income or voting questions; fictional brand-free plan prices.
- Day 160's hand-off record by code and skill, with algebra and geometry strands handed on separately.

## What I could not judge

- Whether the 45-minute cores hold in a real room; the unit plans must test them.
- Whether the graphing and transformation tools named exist in the tools file.

## Settled by the expert

| Choice | Reason | File |
| --- | --- | --- |
| Day 159 gains a 10-minute untimed four-equation station | Year-end fluency sample (finding 1) | days.csv day 159 |
| Check days list sampled codes only, per finding 2; day 116 reuses the day 114 record | 35 to 40 minutes; collect once | days.csv days 116, 158, 159; check table |
| One blank-page item on days 116 and 158 | Checks not critique-only | days.csv days 116, 158 |
| Focus reported as 120 of 160 days wholly major, about 80 percent weighted; lead item 2 closed | Matches the frame | scope-and-sequence.md |
| m7 retrieval rows tagged in skills | Next grade's last-use reads skills | days.csv |
| Grade 7 last use verified; "provisional" dropped | Grade 7 days exist | scope-and-sequence.md; days.csv notes |
| Day 144 goal reworded | Close to the base goal | days.csv day 144 |
| Frame unit 3 comma becomes a semicolon | Gate note | frame.md |

## Across the band

Patterns in grades 6, 7 and 8, read beside grade 5's "Across the band".

- **Year-end fluency is never sampled directly.** Grade 6 samples neither 6.NS.B.2 nor 6.NS.B.3; grades 7 and 8 list their fluency codes inside critique forms (decision grid, claim-chain audit, decision tree) where students judge supplied work. Grade 5's read found the same. Each course's fix is a 10-minute untimed independent station inside the year-end check, no day added.
- **Course-level checks overclaim.** All three say "a short prompt for every part of every listed code" over 11 to 26 codes in 35 to 45 minutes. The fix in each is the same: list sampled codes, reuse records within 10 days, say that end-of-unit assessments carried full coverage.
- **Critique-only check forms.** Grades 7 and 8 use only judge, repair, audit or reconstruct forms for every course-level check; grade 6 varies more. Varying the form is right (the non-repeat rule); every form being critique is not.
- **Readiness by grade number is applied exactly** in all three, including the strict reading that retrieval does not reset last use (grade 8 checks m6-exponents after a year of grade 7 retrieval). Rebuild placement is the weak spot: grades 6 and 7 put rebuilds on unit first days; grade 8 does not.
- **Base fidelity is high and our words hold.** IM order kept in all three; grade 8's one unit move is reasoned. Cuts are IM-optional except grade 7's 7.8.19, which left 7.SP.B.4 untaught (grade 7 finding 3). Copy rates 0.8, 0 and 0.8 percent.
- **Process drift between the three writers' outputs:** three source-map layouts; three focus counts (connected minutes, per-day allocation, a 45-minute lower bound); grade 7 tags retrievals in skills, grade 8 does not; grade 7 counts retrieval openings as check evidence; stale "provisional" last-use notes in grades 6 and 8; frame comma faults in grades 6 and 8.

**Hand-offs between the courses (all hold):**

- Ratios and rates (grade 6 units 2 and 3) to proportional relationships and k as unit rate (grade 7 unit 2) to slope from similar triangles and y = mx + b (grade 8 units 2 and 3).
- One-step equations and equivalence (grade 6 unit 6) to both two-step forms and inequalities (grade 7 unit 6) to multi-step equations and systems (grade 8 unit 5).
- Signed numbers without arithmetic (grade 6 unit 7) to rational operations and decimal expansions (grade 7 unit 5) to rational and irrational numbers (grade 8 unit 8). Grade 6's missing year-end division sample matters here, since 7.NS.A.2d builds on long division.
- Whole-number exponents (grade 6) to integer exponents and scientific notation (grade 8 unit 7), with a readiness check between.
- Scale drawings (grade 7 unit 1) to dilations (grade 8 unit 2); angle relationships (grade 7 unit 7) to transversals (grade 8 unit 1); circles and prisms (grade 7) to cylinders, cones and spheres (grade 8 unit 6).
- Statistics: distributions (grade 6) to sampling and comparing populations (grade 7) to bivariate data (grade 8 unit 4).

**Hand-offs into Algebra I:** linear functions in all representations, solving and counting solutions of linear equations, systems by substitution and elimination, integer exponent laws, irrational numbers and roots, scatter plots with lines of fit. All are taught and assessed by end-of-unit records; the year-end fluency station (finding 1) is what gives Algebra I a current equation-solving record.

**Hand-offs science 6 to 8 leans on (all hold):** ratios and rates come before science 6 uses them; proportional tables (math 7 days 13 to 20) before science 7 days 24 to 41; percent (math 7 by day 68) before science 7 days 129 to 158; scatter plots (math 8 days 56 to 60) before science 8 days 77 and 105; science 8 avoids scientific notation until math 8 teaches it on days 128 to 136, using powers of ten only; science 6 histograms and science 8 qualitative graphs come before math and carry their own bridges.

**Calls for the lead (one rule each, for docs/pipeline/briefs/sequence-write.md):**

1. A year-end fluency sample is an independent untimed station with no supplied work; a critique form does not count.
2. A course-level check day lists only the codes it samples; the "every part of every listed code" sentence is not used on check days.
3. A retrieval opening is never retained as check evidence.
4. One source-map layout for the band (grade 6's), one focus count method (grade 7's per-day allocation, each minute once), and retrieved earlier-grade rows tagged in the skills column.

## For Cory

Nothing.

## Sources

- Illustrative Mathematics, grades 6 to 8, 1st edition (openly licensed pages), S:\CurioClass-sources\illustrative-math: lesson order, learning goals, optional lessons.
- Common Core State Standards for Mathematics, grade 8 (data/standards), and the Progressions for expressions and equations, functions, geometry and statistics (from memory for the limits named; consistent with data/progressions/math.csv).
- docs/RUBRIC-MATH-K8.md (EdReports criteria summary): focus, coherence, rigor indicators.

## For the source list

Nothing new.

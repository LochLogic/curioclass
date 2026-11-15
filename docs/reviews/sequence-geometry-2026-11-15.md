# Sequence read: Geometry, 2026-11-15

Expert cold read of the Curio Class Geometry scope and sequence (grade 10), done under docs/pipeline/briefs/sequence-read.md with the math lens. The named bar, docs/RUBRIC-MATH-K8.md, has no high school notes, so the read applies the lens, the band rules and the earlier reads' settled choices. Second of three high school math reads; "Across the band" is in the Algebra II report.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/GLOSSARY.md, docs/pipeline/briefs/sequence-read.md and sequence-write.md, docs/RUBRIC-MATH-K8.md.
- docs/courses/geometry/frame.md (brief, readiness, seams, units, checks) and scope-and-sequence.md in full.
- data/plans/geometry/days.csv (160 rows) and source-map.csv (163 rows).
- data/progressions/math.csv, grade 7 to 11 rows; data/plans/math-grade-7/8/days.csv and data/plans/algebra-i/days.csv for last use of every assumed row.
- The base: Illustrative Mathematics Geometry, 1st edition (S:\CurioClass-sources\illustrative-math\hs-geometry), every lesson's title, goals and targets, the course standards page and the eleven modeling prompts.
- data/plans/calendar.csv; the chemistry and physics sequence reads (2026-11-14) and chemistry days for the N-Q and A-CED.A.4 leans; the math grade 8 sequence read and its "Across the band".
- Gate output: plan.py check, sequence.py check, frame.py calendar, stale.py check.

## Verdict

The strongest of the three high school sequences. All 124 IM lessons kept in order; readiness verified against the grade 7, 8 and Algebra I day maps and placed correctly by grade number; one extended task per end day with named records reused; and the only year-end check in the band that samples every fluency expectation directly at untimed independent work. Its one real fault is the band's: course-level checks relist codes recorded two or three days earlier and claim "every part of each listed code". Ready after that fix.

## Findings

### 1. Course-level checks relist codes recorded days earlier and overclaim (moderate)

- What is wrong: days 46 and 47 list G-CO.B.6, B.7, B.8, C.9 and C.11, two and three days after day 44 assessed them. Day 104 lists G-MG.A.1 to A.3 and N-Q.A.1, three days after day 101 (which itself reused day 100), and its extended task is a new modeling comparison, so the note's "reuse days 100 to 101" sits beside a fresh collection. Day 159 lists S-CP.A.1 to B.7, three days after day 156. Every check note says "Sample every part of each listed code" with one extended task and 30 minutes of short prompts; day 159 lists 10 codes, and respond days list 12 to 16.
- Why it matters: collect once says a check within ten days reuses the record. Re-collecting spends the course check on what was just shown, and the "every part" sentence cannot be true for ten codes in 30 minutes; the unit planner will try to honor it.
- Fix: days 46 and 47 reuse the day 44 record for unit 2 codes and sample unit 1 codes in the new forms; day 104 keeps the cylinder comparison for G-SRT.C.8 and G-GMD.A.3 and reuses days 100 to 101 for G-MG and N-Q.A.1, removing them from its list; day 159 reuses the day 156 record for S-CP and samples G-SRT.C.8, G-GMD.A.3 and G-C.B.5 through the table audit. Replace "Sample every part of each listed code" with "samples the named parts; the end-of-unit assessments carried full coverage". Check days list only the codes they sample.
- Evidence: days.csv days 44, 46, 47, 100, 101, 104, 156, 158 to 160. Confidence: firm. LAYER: sequence. REPEAT: yes (grade 8 finding 2).

### 2. Completing the square is assessed on day 125 but not named (low)

- What is wrong: days 110 and 111 teach completing the square for a circle's centre and radius under A-SSE.B.3, and day 125's note asks for a "short circle derivation/completing square", but A-SSE.B.3 is not in day 125's codes. The same holds for the one-day contributions A-CED.A.2, A-CED.A.4, A-SSE.A.1a, A-SSE.A.1b, S-ID.B.5 and 7.G.B.4: carried by a day, named on no check.
- Why it matters: Algebra II's last-use ledger needs to know that alg1-completing-square was taught and assessed in grade 10; without the code on the record, the grade 11 writer gave it a readiness check it does not need (Algebra II finding 3).
- Fix: add "A-SSE.B.3, completing the square for a circle" to day 125's codes. The one-day contributions stay unlisted on checks, with "contribution, not assessed here" in their day notes.
- Evidence: days.csv days 110, 111, 125; Algebra II scope-and-sequence ledger. Confidence: firm. LAYER: sequence. REPEAT: new.

### 3. The source map shares Algebra I's layout, not rule 8's (low)

- What is wrong: columns are source, source_unit, source_lesson, source_url, stretch, day, decision, track, note; rule 8 asks for a reason column. Grades 6 to 8 and Algebra II use other layouts.
- Fix: the lead picks one layout for the band; rename "note" to "reason" here at the least.
- Evidence: the six source-map headers. Confidence: firm. LAYER: process. REPEAT: yes.

### 4. Tilde codes raise false gate notes (low)

- What is wrong: sequence.py check reports A-CED.A.2 (unit 5) and A-CED.A.4 (unit 6) "on no day"; both are on days, listed in the frame as "~code". The scope and sequence explains this; the gate still prints it.
- Fix: the lead decides whether the gate reads the tilde (same as Algebra I finding 7).
- Evidence: gate output; frame.md unit table. Confidence: firm. LAYER: process. REPEAT: yes.

## Checks the brief asks for

- **Source map against the base:** every IM Geometry lesson has a row, 124 base lessons in order. Decisions: 132 keep, 28 ours, 1 merge, 2 cut. Modeling prompt 1 merges into day 24 as an eight-minute public introduction. The cuts are prompts 3 (food energy and household access, replaced by a fictional equidistance siting option inside day 9) and 6 (a second modeling day in unit 3, replaced by a rolling-path comparison inside day 60). Both reasons hold: each unit keeps one modeling day, and prompt 3's household-access setting is a sensitivity cost with no mathematical gain over the siting task.
- **Base order and departures:** unit and lesson order kept; modeling prompts placed late in each unit (days 24, 43, 65, 79, 100, 124, 141, 155) with the reason "late-unit placement joins taught ideas", which holds.
- **Our words:** all 124 base-linked goal cells compared with their lesson's title, goals and targets. Highest similarity 0.67 (day 61) and 0.66 (day 29); none close. **Copy rate: 0 of 124.**
- **Focus:** the algebra-cluster count used for Algebra I and II does not fit Geometry (26 percent of teaching days carry N-Q, A-CED, A-REI or G-SRT.B and C codes). The relevant measure is the share of days on congruence, similarity and right-triangle reasoning (G-CO, G-SRT), 74 of 135 teaching days (55 percent); with G-GPE coordinate proof and G-GMD volume reasoning the share is higher. No high school bar sets a line.
- **Widely applicable prerequisites:** similarity and right-triangle trigonometry (G-SRT.B, C), coordinate proof and slope criteria (G-GPE.B), and quantity reasoning (N-Q, finished in units 4 and 5) are each taught and assessed.
- **Coherence from grade 8:** rigid motions and congruence (8.G.A) to G-CO definitions and criteria; dilations and similarity (8.G.A.3, A.4) to G-SRT.A; the Pythagorean theorem and coordinate distance (8.G.B) to trigonometry and G-GPE; cylinder, cone and sphere volume (8.G.C.9) to Cavalieri and G-GMD. The grade 8 rows skip Algebra I, so each gets a readiness check before its unit (days 1, 26, 48, 105). Correct.
- **Modeling across the course:** nine kept prompts, one or more per unit, with supplied data; synthesis days 23, 42 and 123 join units.
- **Rigor:** proof, construction and application days in every unit; fluency in the 5-minute mixed opening.
- **Year-end fluency:** day 158 directly samples G-CO.D.12, G-SRT.B.5, G-GPE.B.4 and G-GPE.B.7 at untimed independent work. Correct, and the model for the other two courses.
- **Readiness by grade number:** verified. Grade 8 and grade 7 rows idle in grade 9 get readiness on days 1, 26, 48, 81, 105 and 143; m7-circles is taught on day 90 after its day 81 check; every Algebra I row is retrieved in openings (completing the square on days 110 and 111, rearranging formulas on day 114, systems on day 118, two-way tables on day 147). Units 4 and 7 need retrieval only, and the frame says "next grade, direct" for the Algebra I rows.
- **End days:** each holds one extended task plus short items and reuses the named closing records (days 101, 125, 156). Correct.
- **Collect once and non-repeating checks:** finding 1. Check forms do change (constraint audit, evidence selection, table audit) and use earlier-unit settings.
- **Science hand-offs:** Chemistry's unit 2 (days 17 to 31) and unit 4 (days 42 to 53) come before Geometry finishes N-Q; the scope and sequence names this and Chemistry carries the bridges. Physics leans on no Geometry row by name; right-triangle trigonometry (unit 4) is available to it.
- **Calendar:** checks on days 46 to 47, 103 to 104 and 158 to 159 match calendar.csv; week 32 is finals.
- **Shorter path:** present.

## Lens checklist

| Lens item | Holds | Note |
| --- | --- | --- |
| Major work share | yes | G-CO and G-SRT on 55 percent of teaching days |
| Progression coherence | yes | begun and owned codes named |
| Standard taught in part with no finishing day | yes | N-Q finished in units 4 and 5 |
| Problems that join units | yes | synthesis days, modeling prompts, cylinder plans |
| Fluency spaced and mixed | yes | direct year-end station on day 158 |
| Practices named | yes | tied to days |
| Models consistent | yes | compass and straightedge, rigid motions, coordinates |
| Readiness by grade number | yes | verified against grade 7, 8 and Algebra I days |
| End days not stacked | yes | one extended task each |
| Collect once | partly | days 46, 47, 104, 159 (finding 1) |
| Our words | yes | 0 of 124 |
| Source-map layout | no | finding 3 |

## What is right and should not be touched

- The prerequisite audit verified against actual day maps, the cleanest in the band.
- Day 158's direct, untimed fluency sample of all four expectations.
- End days that name the records they reuse.
- Both modeling-prompt cuts and their in-day replacements.
- Day 160's hand-off to Algebra II by row: roots, transformations, triangle ratios, circle work.

## What I could not judge

- Whether the 50-minute proof and construction days hold for a class of 30; the scope and sequence flags tight days for the lead.
- Whether dynamic geometry tools named exist in the catalogue.

## Settled by the expert

| Choice | Reason | File |
| --- | --- | --- |
| Days 46, 47, 104 and 159 reuse the records of days 44, 100 to 101 and 156 and list only sampled codes | Collect once (finding 1) | days.csv; check table |
| "Sample every part of each listed code" replaced on check days | Overclaim | days.csv check notes |
| A-SSE.B.3 named on day 125 | Algebra II's ledger reads it (finding 2) | days.csv day 125 |
| Prompts 3 and 6 stay cut | Reasons hold | source-map.csv |

## For Cory

Nothing.

## Sources

- Illustrative Mathematics Geometry, 1st edition (openly licensed pages), S:\CurioClass-sources\illustrative-math\hs-geometry: lesson order, goals, modeling prompts.
- Common Core State Standards for Mathematics, high school geometry, number and quantity (data/standards), and the high school geometry Progression (from memory for the limits named; consistent with data/progressions/math.csv).
- docs/RUBRIC-MATH-K8.md: no high school criteria; the lens applied instead.

## For the source list

- The same high school bar named in the Algebra I report.

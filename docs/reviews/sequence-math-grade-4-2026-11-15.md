# Sequence read: math grade 4, 2026-11-15

Expert cold read of the Curio Class math grade 4 scope and sequence as it now stands, done under docs/pipeline/briefs/sequence-read.md with the bar in docs/RUBRIC-MATH-K8.md and the math lens. I did not open any reconcile report or earlier grade 4 work.

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/pipeline/briefs/sequence-read.md, docs/pipeline/briefs/sequence-write.md, docs/RUBRIC-MATH-K8.md.
- docs/courses/math-grade-4/scope-and-sequence.md in full and docs/courses/math-grade-4/frame.md.
- data/plans/math-grade-4/days.csv (all 160 rows) and data/plans/math-grade-4/source-map.csv (180 rows).
- data/plans/math-grade-2/days.csv and data/plans/math-grade-3/days.csv, for readiness and retrieval rows.
- The base: Illustrative Mathematics grade 4 at S:\CurioClass-sources\illustrative-math (149 lessons in 9 units), lesson purposes, learning goals and titles.
- Earlier reads for the standard: sequence-math-kindergarten, sequence-math-grade-1 and sequence-math-grade-2 (2026-11-15).
- Gates: `plan.py check` 0 failures, `sequence.py check` 0 failures for math-grade-4, `frame.py calendar` checks in weeks 12, 23 and 31 with no stagger break, `stale.py` 0 failures.

## Verdict

A careful grade 4 year: multiplication and division methods are explained before they are compacted, fractions move from equivalence to like-denominator sums to fraction times whole number to decimal notation in order, readiness is counted correctly on four grade 2 rows, and goals are in our own words. It is fit to plan from after two moderate fixes: 4.NBT.B.4 needs a direct year-end fluency sample, and the day 43 end day stacks two story performances on top of five other codes. The major share sits on the 65 percent line and holds only by counting supporting links, which the unit plans should confirm in minutes.

## Findings

### 1. No direct year-end evidence for 4.NBT.B.4

- What is wrong: the last independent performance of the standard addition and subtraction algorithm is the day 75 end day (week 15). Check 3 part 1 (day 153) only "audits whole-number calculations" in a supplied record, and day 160's handoff names "algorithm fluency" without a sample behind it.
- Evidence: days.csv days 75, 153, 160; grade 2 read finding 2 (diagnosing an error is not fluency).
- Cost: 4.NBT.B.4 is the grade 4 fluency the bar names; grade 5 starts from a week 15 record.
- Fix: inside day 153, a short untimed independent station (about 6 multi-digit addition and subtraction items, no supplied work) recorded for the day 160 handoff. No day added.
- Severity: moderate. Confidence: firm. LAYER: sequence. REPEAT: yes (grade 2 finding 2).

### 2. Day 43 end day stacks story performances

- What is wrong: day 43 lists seven codes (4.NF.B.3a to 3d and 4.NF.B.4a to 4c) and asks fresh for two story performances, a like-denominator story with model and equation (3d) and a fraction-times-whole story (4c), alongside decomposition, sums, differences and mixed numbers. No saved product is named.
- Evidence: days.csv day 43; day 39 already produces independent result-, change- and start-unknown stories with tape and equation. Day 148 has a milder version: four expectations fresh, including measuring and sketching angles and drawing figures.
- Cost: breaks the end-day rule; 45 minutes of evidence cannot give each story performance the time to show reasoning.
- Fix: on day 39, retain an independent story product as the 4.NF.B.3d record and name it on day 43, so day 43 asks short prompts plus the 4c story. On day 148, retain the day 146 measure-and-sketch product (or the day 144 drawing) so one performance is fresh.
- Severity: moderate. Confidence: firm. LAYER: sequence. REPEAT: yes (grade 2 stacked end days).

### 3. Notes point at earlier work a writer cannot see

- What is wrong: several notes cite earlier drafts instead of saying the content: "old re-plan finding 6" (day 37), "old day 87 estimate routine" (day 81), "preserves the old day 21 route" (day 21), and the "Reconciliation safeguards" section in the scope and sequence that refers to earlier reviews.
- Evidence: days.csv days 21, 37, 81; scope-and-sequence.md.
- Cost: a unit-plan writer cannot follow the pointer and may drop the safeguard it stands for.
- Fix: replace each pointer with the content it protects (for day 81, name the estimation routine), and retitle the section "Safeguards" with each item stated in full.
- Severity: low. Confidence: firm. LAYER: sequence. REPEAT: new.

### 4. Source map off the band layout, and "split" misused

- What is wrong: columns are source_unit, source_lesson, source_title, stretch, unit, day, decision, note, source_url, with no license column and note in place of reason. Single base lessons that map to one day are labelled "split" (64 rows) where they only sit at a course-unit boundary.
- Evidence: source-map.csv header and decision column.
- Cost: band tools read the layout differently per course; "split" suggests a lesson spread over several days when it is not.
- Fix: move to the band layout (base_lesson, base_title, course_unit, day, decision, reason, source_url, license), relabel one-day rows "keep", and keep "split" for lessons spread over more than one day.
- Severity: low. Confidence: firm. LAYER: process. REPEAT: yes (grade 2 layout finding).

### 5. Major share sits on the line

- What is wrong: by code share about 65 percent of days are major work (4.OA.A, 4.NBT, 4.NF), 66 percent by first code. The scope and sequence claims 67.0 percent by minutes by counting supporting links; the frame says 63 percent strict or 81 percent by indicator 1e.
- Evidence: days.csv codes; scope-and-sequence.md focus section; frame.md.
- Cost: none yet; but any unit-plan drift toward geometry or measurement drops the year below the line.
- Fix: keep the plan; ask each unit plan for units 6 to 9 to report minutes on major codes, and settle one figure in the frame (by minutes, with links counted only where the major code is assessed that day).
- Severity: low. Confidence: judgment call. LAYER: frame. REPEAT: new.

## Checks the brief asks for

- Source map against the base: every one of the 149 IM lessons has a row, titles match, base order is kept. Decisions: 60 keep, 64 split, 10 merge, 15 cut, 31 ours. Merges (2.1 with 2.2, 7.1 with 7.2, 7.3 with 7.4, 9.1 with 9.2, 9.7 with 9.8) each keep the ideas. Cuts are optional lessons and routines 9.10 to 9.12 placed into warm-ups; reasons hold.
- Departures from base order: base unit 3 splits into course units 3 and 4, base 4 into 4 and 5, base 6 into 7 and 8, base 7 and 8 join in unit 9, and base 9 serves as review. Each departure keeps the progression order and has a reason.
- Our words: copy rate about 1 of 129 goal cells (day 103, "Multiply three- and four-digit numbers by one digit with explained partial products", borderline), under 1 percent; notes and source-map cells 0.
- Focus: on the line (finding 5).
- Coherence: grade 3 rows retrieved early (m3-mult-fluency day 1, fraction rows days 9, 10 and 13); readiness on grade 2 rows: m2-money day 44 then taught day 48 and retrieved day 86; m2-three-digit-place-value and m2-compare-three-digit on day 57 (a respond day); m2-unit-size day 76; m2-halves-thirds-fourths day 127. None is on a unit's first day and all are grade g+2. Day 100 gives a full day to the grade 3 facts sample and response.
- Rigor balance: 77 understanding, 20 fluency, 37 application days.
- Fluency: 4.NBT.B.4 taught and assessed by day 75, warm-ups rotate later; year-end evidence missing (finding 1).
- End days: day 43 and day 148 (finding 2); others acceptable.
- Collect once: check 3's geometry part reuses days 145, 147 and 148, correct.
- Planning class size 30: fits.

## Lens checklist

| Lens item | Holds | Note |
| --- | --- | --- |
| Major work share | on the line | finding 5 |
| Progression coherence | yes | readiness and retrieval correct |
| Rigor balance | yes | |
| Named fluencies | partly | finding 1 |
| Practices named | yes | all eight |
| Models consistent | yes | area, partial products, tape, number line |
| Precise language | yes | remainder notation on day 119; trapezoid inclusive |
| Readiness by grade number | yes | |
| End days not stacked | partly | finding 2 |
| Collect once | yes | |
| Our words | yes | under 1 percent |
| Source-map layout | no | finding 4 |

## What is right and should not be touched

- The readiness placements on grade 2 rows, all off first days and tied to the next teaching day.
- Day 100's full day for the grade 3 facts sample and response.
- Remainder meaning on day 119 and the inclusive trapezoid definition.
- The W.4.1 and L.4.6 bridges for written math explanations.
- Ten fold-ins on the shorter path, each preserving owned parts.

## What I could not judge

- Day 48's note says the base lesson uses coin thickness; I did not open that base lesson to confirm it.
- Minute shares within days (finding 5).

## Settled by the expert

| Choice | Reason | File |
| --- | --- | --- |
| Readiness on four grade 2 rows, each before the day that needs it and none on a first day | Readiness counts by grade number (g+2) | days.csv days 44, 57, 76, 127 |
| Check 3 geometry reuses days 145, 147, 148 | Collect once | days.csv day 154 |
| Base units 7 and 8 joined in course unit 9 | One measurement and geometry arc | source-map.csv |
| Routines 9.10 to 9.12 as warm-ups | No full day needed; warm-ups named | days.csv day 160 and others |

## For Cory

Nothing.

## Sources

- Illustrative Mathematics, grade 4 (openly licensed pages), S:\CurioClass-sources\illustrative-math.
- Common Core State Standards for Mathematics, grade 4, and the progressions documents (number and operations in base ten, number and operations: fractions).

## For the source list

Nothing new.

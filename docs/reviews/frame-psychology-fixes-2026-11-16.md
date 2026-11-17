# Fixes: Psychology course frame, after the cold read (2026-11-16)

Applies the expert read (`frame-psychology-2026-11-16.md`, 12 findings) to `docs/courses/psychology/frame.md`, the 34
psy- rows of `data/progressions/social-studies.csv` (notes only) and `data/standards/apa-hs-psych-2022.txt` (one line).
Findings 1 to 8, 11 and 12 are applied; findings 9 and 10 touch files other workers own tonight, so they are written
into the frame's For the lead with the exact replacement text. Every "Settled by the expert" row is applied.

Before the safety and dated-claim flags were re-pinned, every flag was checked section by section against the base text
(Psychology-OP.pdf, text extracted with pypdf, -I), searching each section for suicide, self-harm, eating disorders,
the marshmallow study, facial feedback, the prison study, the Genovese case, the old term for intellectual disability,
the candle-flame figure, the Genie case, "imbalance", the infant sex-reassignment case, eugenics and bullying. That
check confirmed the read's placements and found more, applied below: suicide content in 15.1, 15.10, 16.2 and 16.5
and in chapter 12's summary; "chemical imbalance" in 15.3 and 15.7; the old term in 9.3 and as a clinical term in
15.7; the Genie case again in 9.1; photographs of drug preparation in 4.5; and chapter-end personal application
questions that ask students about their own stress, sleep, medication, memories, personality and bullying.

Gates after the fixes: `scripts/progression.py check social-studies` 418 rows, 0 failures; `scripts/frame.py check
psychology` 0 failures (16 units, 160 days, 156 in units, 4 for checks and respond days); `scripts/stale.py check`
0 failures; `scripts/frame.py sync` run. The course keeps 16 units and 160 days; no row moved between units.

| # | Result | What was done |
|---|---|---|
| 1 | Applied, widened | Sensitivity reads: safe-messaging guidance now for units 9, 12, 13, 14, 15 and 16; the health expert's read for units 4, 9, 10, 12, 13, 14, 15 and 16; a national eating disorders body's school guidance added for units 10 and 15. A new brief bullet lists every base section carrying suicide, self-harm or eating-disorder content (10.2, 10.3, 12.6, 15.1, 15.7, 15.10, chapter 15's review questions, 16.2, 16.5). Mental health rules: the counselor is told before the course opens, with units 9, 12, 13 and 14 to 16 named, and again before each; help is named on every page that touches suicide. Unit 12, 13 and 15 sensitive lines carry the read's text (bullying without a named death; the infant case for research ethics only, his death not described; eating disorders with no weights, sizes, calories, behaviours or body images; self-harm only as a sign to get help). Source map rows 10.3, 12.6, 15.1, 15.10, 16.2 and 16.5 carry the flag. The psy-social-influence, psy-gender-orientation and psy-disorder-categories notes match |
| 2 | Applied | Dated list adds: unit 2 and 16, the neurotransmitter "imbalance" account (3.2, also 15.3 and 15.7) replaced; unit 3, the candle-flame figure (5.1) dropped; unit 10, "seven universal emotions" (10.4) not kept as settled, taught as one recognition study beside one later study of variation (the expert's settled choice). Unit 7's sensitive line names the Genie case as optional, one scholarly account, no images, no detail of the abuse; unit 9 does not retell it (9.1). Unit 16 names medications by what they act on, with trial evidence and no single-chemical cause. Source map rows 3.2, 5.1, 7.2, 9.1, 10.4, 15.3 and 15.7 carry each flag; psy-nervous-system, psy-sensation, psy-language, psy-emotion and psy-treatment-types notes match |
| 3 | Applied | Marshmallow study pinned to unit 11 (11.4), with unit 5's check-set add kept as our own content; facial feedback to unit 10 only; the prison study to 12.2 (moved off 12.1); the Genovese case to 12.6 (moved off 12.7, which now carries newer bystander research). The old-term item now names 7.5's text and box, chapter 7's review questions, 9.3, and 16.1's law title; unit 15 says "psychomotor slowing" for 15.7's clinical term |
| 4 | Applied | Unit 8's sensitive line and psy-intelligence-testing's note: Buck v. Bell taught as the law it was, with Butler's dissent, Skinner v. Oklahoma (1942) and the later state apologies and compensation (Virginia 2002, North Carolina 2013); the science judged by values rule (b), the harm named under (c). Not sent to Cory: this is the read's own reading of rule (a) |
| 5 | Applied as given | Unit 16 7 to 8, unit 3 12 to 11, unit 13 8 to 9, unit 9 11 to 10; total stays 156. The Days bullet names the ten priority areas and states the weighting: every priority unit after unit 1 gets about one day a target or more, the non-priority units with many short targets (3, 4, 10) fewer; unit 16 gets the floor of 8 because the course ends on it. A side effect: units 1 to 8 now total 80 days, so unit 8 ends the first half on day 80 and the mid-year check is days 81 and 82 |
| 6 | Applied | Unit 1 "15 targets and 3 themes"; the "get 8" clause rewritten with the new counts; unit 15 "the disorders unit, given 10 days for the care it takes"; unit 8 "Ends the course's first half (day 80), before the mid-year check"; unit 9 "Opens the second half, after the mid-year check". Cross-subject weeks updated (unit 8 weeks 15 to 16; unit 14's action in course week 28) |
| 7 | Applied | APA22.INT.1.1 reads "Explain intelligence as a construct: an idea inferred from behaviour and measured only indirectly"; psy-intelligence-theories names "what the tests measure" as one historical position to weigh |
| 8 | Applied | Year-end check: one short item per theme A to G, each in a finding from a different unit. Mid-year check: one item each on themes A, B, C and E as taught so far |
| 9 | Moved to For the lead (item 5) | The US History I and II frames belong to other workers tonight. Item 5 gives the three rows for US History I's handed-on table (us1-news-reading unit 9, us1-research-inquiry unit 1, us1-argument-writing unit 5, as that frame places them), a sentence for its heading paragraph, and the line under US History II's timetable |
| 10 | Moved to For the lead (item 6) | data/tools-concepts.csv and data/coverage.csv belong to other workers. Item 6 gives the replacement text for case-conference (a reader of published, de-identified vignettes; no student diagnoses or plays a clinician) and go-along (the study's method, data and replications from the record; no student placed in it or deceived), and the APA22 area codes for each of the six coverage rows, to file in data/plans/later.csv |
| 11 | Applied | docs/courses/social-studies/STANDARD.md (status table, course table row, section 4), docs/ADOPTION-BAR-SUBJECTS.md (section 1 course list, the Unsupported note, the social studies status row, the AP and psychology topics row) and docs/agents/lenses/social-studies.md (the "does not cover" clause removed; a course-frame line for psychology added) now state the rule as it stands: the standard is loaded as data/standards/apa-hs-psych-2022.txt and the frame is docs/courses/psychology/frame.md |
| 12 | Applied | The inquiry bullet and psy-wellness-action's note give the classroom-only version: shared with the class and filed, unsigned, where the school permits no posting; no money, travel or public identity needed |

Added beyond the read, from the section-by-section check: unit 4 and Source map 4.5, no images of drug preparation or use
(the base text's photographs left out); a "Chapter reviews" Source map row and a dated-list item: personal application
questions are not used as written, and a useful one is rewritten for a made-up person; psy-social-influence drops the
book's question asking whether students have experienced bullying.

## Unit-level lessons pass (2026-11-16)

Brings the frame up to frame-write.md lessons 17 to 32 (evidence: frame-unit-lessons-2026-11-16.md). No unit, skills
placement, day total or owned standard changed; no lesson forced one. Gates after the pass: `scripts/frame.py check
psychology` 0 failures (16 units, 160 days, 156 in units, 4 for checks and respond days); `scripts/progression.py
check social-studies` 418 rows, 0 failures; `scripts/stale.py check` 0 failures; `scripts/frame.py sync` run.

| Lesson | What changed |
|---|---|
| 17 Day kinds | New "Day kinds." bullet: Understanding, Application, and Fluency kept little (one short retrieval-practice set a unit at most, never new content, never scored) |
| 18 Readiness evidence | New "Readiness and retrieval, counted from grade 12" bullet: every assumed row with its last-use grade, course, unit and days from the core scopes' days.csv, and its treatment; the scope gate's count governs. Two corrections from the count: bio-sources-of-variation is retrieval (last used grade 11, Physics unit 7, one hop through phys-em-radiation-effects) and s8-senses-brain was last used in grade 9 (Biology unit 1, one hop), not "four grades back". Grade 11 placement: the "if later" lines apply, bio-sources-of-variation joins the unit 2 readiness check, and the three Algebra I rows get a readiness check on unit 1's day 1. Seams and Cross-subject notes carry the same evidence. Row notes that disagree go to For the lead item 7 |
| 19 Scored evidence | Every unit's last column opens with its end-of-unit evidence form. Unit 1: the research proposal (draft day, written feedback by the next lesson, revision day, scored after revision) plus a separate sitting; unit 14: the informed action piece (drafted, feedback, revised, scored after revision) plus a sitting on the end day; every other unit a sitting with one unseen study as its single full performance |
| 20 Checks claim samples | Both check rows name the units sampled, task forms, the records reused unscored (unit 1 proposal, unit 14 piece) and that unit 8's and unit 16's items come from earlier units' content |
| 21 Inside the period | Days bullet: the 50 minutes hold handing out, collecting, pooling slips and the exit ticket; readiness ten minutes; no lab clean-up; a fold-in never takes a draft, feedback, revision or respond day |
| 22 Safety | No hands-on hazards: the research-ethics bullet says so and that the safety read checks each class task against it |
| 23 Facts sourced | New "Studies and data, with their sources" bullet: studies by authors, year and journal, figures from the study itself checked by the answer-key agent, "invented for practice" labels, and the replication record of each classic study as of 2026-11-16 |
| 24 Depth and devices | Each unit's What students learn ends with "Out: ..."; new "Devices." bullet (none per student; no owned code needs technology) |
| 25 Tools and texts | New "Tools and what Curio Class writes, by unit" bullet; no supplies beyond printing, so no cost line |
| 26 Literacy | The literacy bullet and the Cross-subject literacy heading now say "practised, not owned" |
| 27 Source map | A "How sections become days" paragraph: a section is not a lesson, check days are `ours`, goals in our words, at most about 800 words of adapted text a day |
| 29 Owned, begun, revisited | New bullet: one owner per id; later uses labelled "revisited (review)" (themes, stereotypes in unit 13, minority stress in unit 14, conditioning in unit 16, delay of gratification in unit 11); unit 5 and unit 11 cells say so |
| 30 Sensitivity by unit | The Sensitivity reads bullet is now by unit, each with its communities and their own sources (research harm, brain injury, Deaf and blind people, people who use drugs, dementia and exonerees, signers, eugenics' targets, grief, eating disorders and the Fore and Himba, bullying, LGBTQ and racial communities, crisis, mental illness and neurodiversity, psychiatric survivors) |
| 31 Grade 12 calendar | New "Senior calendar." bullet: unit 16 and the year-end check (days 159 and 160) keep every day; up to five days fold from units 9 to 13; never a readiness, draft, feedback, revision, end or respond day |
| 32 Core leans only | The grade 11 or 12 bullet states every lean is on a core course and Statistics is never assumed |
| 28 One focus method | Not applicable (math only) |

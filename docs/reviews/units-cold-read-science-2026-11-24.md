# Science unit plans: cold read from the progression down, 2026-11-24

The COURSE-RUN stage 4 gate read for science: one cold read from data/progressions/science.csv down through the
frame units tables and unit plans of the 12 core courses (kindergarten, grades 1 to 8, Biology, Chemistry, Physics).
The reader wrote and fixed none of it. Read: AGENTS.md, COURSE-RUN.md stage 4, EXPERT.md, the science lens,
UNIT-PLAN.md; the progression in grade order (all 198 rows for kindergarten to grade 11); each course's frame units
table and the "owned", "Builds on", field 4 and Goal map blocks of all 87 unit plans; whole or near-whole reads where the
chain looked weak (grade 3 s01, grade 6 s02 and s03, grade 7 s01, grade 8 s01 and s05, Chemistry s04, Biology days with
middle school codes). Helper scripts and the plan.py output are in _scratch/l87/tmp/cold-read-science/. The 2026-11-24
ledgers (units-read-<course>, units-structure-pass-science) were read after the read, only to mark what is already
fixed.

## Verdict

Not ready for owner approval yet, though close: the content chain holds. Every kindergarten to grade 11 progression
row is owned by a unit at its grade, every assumed earlier row is retrieved or readiness-checked, every model is built
before it is used, no Understanding day teaches only earlier-grade rows, and the arcs climb (particles grade 5, then
temperature in grade 6, atoms in grade 7, the mole in Chemistry; cell parts in grade 7 retrieved, not retaught, in
grade 8). Two stage 4 Make and Check items are open across many courses: in grade 7 (and a few days of grade 8,
Biology and Physics) the exit is the day's practice again on a new case, which passes the gate's string test but not
the rule; and the ledger holds no rows at all for grades 4 to 11.

## Findings, most serious first

| # | Severity | Where | What | Status |
|---|---|---|---|---|
| 1 | Major | science-grade-7 s02 to s06 Goal maps; also grade 8, Biology, Physics | The exit has the same shape as the day's practice, only on "a new" case, so the exit is the practice again. Clear cases in grade 7 (11): days 31, 34, 79, 85, 105, 112, 115, 119, 133, 138, 153 (for example day 79, exit "Revises the model for a new light, water and carbon dioxide condition", practice "Revises the plant model from contrasting light, water and carbon-dioxide conditions"). A looser match finds about 24 grade 7 rows. Near cases elsewhere: grade 8 days 15, 35, 37, 67, 68, 81, 141; Biology days 28, 38, 60, 102, 107; Physics days 122, 138, 140. unitplan.py passes them because the two cells are not equal strings. This is the clash COURSE-RUN section 4 names as its example. | Open. The grade 7 read did not raise it; the grade 8 read (finding 19) cleared a different list of days (7, 39, 42, 54, 56, 71, 72, 96) on the "new case" reasoning, which this read disagrees with for the days listed here. |
| 2 | Major | data/plans/ledgers/science.csv, grades 4 to 8, Biology, Chemistry, Physics | Stage 4 Make says "the ledger gets the unit's rows at stage planned" (ledger.py `seed (stage 4)`). The ledger has about 6,000 rows for kindergarten to grade 3 and none for the other eight courses, so no unit plan in grades 4 to 11 has review entries that point at ledger rows, the stage 4 continuity check ("reviews point to real earlier work") cannot be run on them, and stage 5's ledger gate will find nothing below grade 4. The plans' readiness and retrieval tables point at progression rows and days.csv days instead, which is why the chain still reads clean. | Open; not in any ledger. If seeding is meant to move to the section-plan step (as it did in the K to 3 ladder), that is a rule change for the lead to record. |
| 3 | Moderate | data/plans/ for grades 4, 6, 8, Biology, Chemistry, Physics; grades 5 and 7 | Stage 4 Make: "Hand-backs, materials and reserved examples are written as data." Grades 4, 6, 8 and the three high school courses have no handbacks.csv or materials.csv; grade 5 holds hand-backs for units 1 and 2 only and grade 7 for unit 1 only (the probes). The hand-backs live only in plan prose, so "hand-backs have both ends" was checked by reading, not by data. | Open. Note: the Codex draft run (HANDOFF, L105) is writing grades 4 to 6 data in a separate folder; this read did not open it. |
| 4 | Moderate | data/plans/science-grade-7/source-map.csv; latent in grades 6 and 8 | plan.py check fails grade 7 with 175 lines: 99 rows whose harms_learning is prose ("no: question and evidence order retained ...") instead of yes, no or unclear, 54 rows whose days are separated by semicolons, 15 days with no exit question in items.csv, 4 sections not in data/units.csv. Grades 6 and 8 carry the same two source-map faults (harms_learning in prose; 57 and 84 day cells with semicolons) but are not checked because they have no items.csv yet. The OpenSciEd order record (DESK-ANSWERS 2026-11-13) cannot be gated until these parse. | Open. The structure pass recorded the grade 7 count as pre-existing and left it. |
| 5 | Moderate | science-grade-7 s01 days 5 and 6; progression row s7-reactions-atoms | Days 5 and 6 compare mass in open and closed systems and teach "open system, flexible closed system and boundary" as new, but grade 5 unit 1 (s5-conserve-weight, days 8 to 15) already weighed closed bags and balloon-topped fizzing systems. s7-reactions-atoms does not list s5-conserve-weight in assumes, so neither a retrieval nor a readiness item reaches it, and the grade 5 work is taught again as new. Chemistry s04 day 42 does name its return to the grade 5 bag. | Open. |
| 6 | Low | "Progression skills owned" skel lines | The line lists rows the unit does not own: grade 6 s02 (s6-light-paths, owned by unit 1), grade 6 s03 (s6-particle-temperature, owned by unit 2), grade 8 s01 (s8-senses-brain, owned by unit 2 per the frame; unit 1 day 11 begins it), and math rows as "owned" in grade 3 s02 and s03 (m2-measure-with-tools) and Physics s01 (alg1-graph-features-rates, alg1-writing-equations-constraints). The next lines of each plan say the right thing, so a reader is not misled for long, but the owned count is wrong. | Partly addressed: the structure pass checked grade 6 s03 and kept it as a sequence call. The rest open (grade 3 is signed off; fix when next edited). |
| 7 | Low | field 4 readiness tables | Readiness checks given where the rule says retrieval (rows used the year before): grade 4 s04 (s2-erosion-solutions), grade 4 s06 (s1-light-materials, s1-parts-mimic), grade 7 s01 (s6-particle-temperature, s6-state-change), grade 7 s03 (s5-new-substances). Harmless minutes, but against sequence-write rule 2. | Partly known: grade 7 F9 was left for the lead as a generator change; the grade 4 and grade 7 s01 cases are not in any ledger. Open. |
| 8 | Low | grade 6 s02 field 4 | s02 lists s4-light-eye under "Builds on" but neither field 4 nor its retrieval table names it; the retrieval sits on unit 1 day 2, same year. | Open, wording only. |
| 9 | Note | progression assumes in grades 1 and 2 | Several assumes links carry a practice, not content (s1-parent-offspring assumes sk-forecast-severe; s2-water-where and s2-fast-slow-events assume s1-parent-offspring; s2-heat-cool-change assumes s1-like-parents), so grade 2 unit 1 day 6 and unit 2 day 11 retrieve chick-survival source work inside water and land units. | No change asked: the grade 1 read (item 11) judged it sound and K to 3 is signed off. |
| 10 | Note | earth-and-space-science, environmental-science | The two grade 12 electives have frames and scopes but no unit plans, so their 41 progression rows (ess-*, env-*) are owned by no unit. They are electives, outside this core gate; approval of the science baseline should not be read as covering them. | Not a finding against the core courses. |
| 11 | Nit | spelling | UK spellings in data: "behaviour" (Chemistry day 5), "kilometres" (Physics s09 day 138 retrieval), "centre" (Biology day 102 practice). | Fix when next edited (AGENTS.md rule). |

Checked and sound: no progression row assumes a later row; every model a row uses (particle, energy-transfer,
food-web, plate, field, periodic-table, computational) is built by an earlier row or earlier in the same unit (same-unit
pairs confirmed by first day in days.csv); Biology's middle school codes appear only on readiness and respond days;
unitplan.py check science is 155 PASS, 0 FAIL, 1 note.

## Open items for a fix pass

1. Grade 7 Goal maps: for the 11 clear days, change the practice (never the exit) so it differs in shape; then sweep
   grade 7's other near rows, grade 8 days 15, 35, 37, 67, 68, 81, 141, Biology 28, 38, 60, 102, 107 and Physics 122,
   138, 140. Retool the practice-shape check so "the same action on a new case" fails (COURSE-RUN section 4 sweep).
2. Seed data/plans/ledgers/science.csv at stage planned for grades 4 to 8, Biology, Chemistry and Physics
   (`ledger.py seed`), or have the lead record that seeding moves to the section-plan step.
3. Write handbacks.csv and materials.csv for the courses that lack them (after the Codex draft run's grades 4 to 6
   output is reviewed, so nothing is written twice).
4. Grade 7 source-map.csv (and grades 6 and 8): harms_learning to yes, no or unclear with the reason moved to `why`;
   days space separated. Rerun plan.py check for grade 7.
5. Grade 7 unit 1: add a retrieval or readiness item on s5-conserve-weight before day 5, recast day 5 as building on
   grade 5's closed-system weighing, and add s5-conserve-weight to s7-reactions-atoms' assumes (a progression change:
   owner review per stage 2 Fix).
6. Correct the "Progression skills owned" lines in grade 6 s02, grade 8 s01 and Physics s01 (math rows to the
   cross-subject line); grade 3 when next edited.
7. Readiness to retrieval where the rule says so: grade 4 s04 and s06, grade 7 s01 (with the F9 generator change).
8. Grade 6 s02 field 4: name the s4-light-eye retrieval on unit 1 day 2.

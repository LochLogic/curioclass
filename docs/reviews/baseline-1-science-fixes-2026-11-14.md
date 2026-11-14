# Baseline 1, science fixes (2026-11-14)

The science fixer's pass on the baseline 1 reads, for the 12 science frames (science-kindergarten, science-grade-1 to
science-grade-8, biology, chemistry, physics) and data/progressions/science.csv. Sources applied:
docs/reviews/baseline-1-science-2026-11-14.md (findings 1 to 8 and "Settled by the expert"), the science slice of
docs/reviews/baseline-1-structure-2026-11-14.md and docs/reviews/baseline-1-codex-2026-11-14.md, and Cory's Desk
answers of 2026-11-14 (no outside human reader; the time a day stays as picked).

Counts: 32 applied, 8 not applied (each with its reason), 1 applied in a different place than asked (literacy codes in
progression notes, not cross_subject). For Cory: none.

## Gates (run after the last edit)

| Gate | Result |
|---|---|
| `python -X utf8 scripts/frame.py check <slug>`, all 12 science slugs | 0 failures each. Notes only: "data/plans/frames.csv is behind the frame" (sync not run, see Not applied) and the usual "Seams does not name" notes |
| `python -X utf8 scripts/progression.py check science` | 198 rows, 0 failures |
| `python -X utf8 scripts/stale.py check` | 56 files, 0 failures |
| `python -X utf8 scripts/plan.py check` | exit 0, 0 failures in any course or catalogue line |

## The returning-skills rule, as applied

The expert's wording ("last used two or more grades before") reads two ways. Its own examples settle it: Biology's
grade 7 rows are "one grade before" grade 9, so retrieval; Chemistry's grade 7 rows "two grades have passed", so
readiness. Applied rule, in every frame and in the progression notes: **a row or model idle two or more grades (two
or more grades between its last use and this one) opens the first unit that needs it with a readiness check and a
one-lesson reteach, counted in the unit's days; one idle a single grade or less, or used earlier this year, opens
with a retrieval task.** "Last use" is the progression's own record: the latest row that assumes the skill, or that
the notes name as keeping it in use. Where a frame and that record disagreed, the frame now follows the record (for
example grade 6's climates, kept in use by grade 5's s5-sphere-interactions, is a retrieval task; grade 4's light
rows, kept in use by grade 2, are retrieval tasks). The lead may want lesson 16's wording in frame-write.md to say
"idle two or more grades" so the next writer does not read it the other way (the structure fixer owns the brief).

## Applied

| # | Finding | Files | What changed |
|---|---|---|---|
| 1 | Science 1: repeats across bands | biology, chemistry, physics frames | "How phenomena are chosen" now reads "not an anchor, design problem or check case any other science course uses, kindergarten to Physics, unless the unit says it returns on purpose and what is new". Biology unit 3 marks the dark-kept plant as returning on purpose from kindergarten unit 4 (new: dry mass, atoms and energy). |
| 2 | Science 2: grades 6 to 8 C3 = n/a | science-grade-6, 7, 8 | Every unit's C3 cell now names two or three practices and two crosscutting concepts from the OpenSciEd unit page's focal list; a "Practices across the year" bullet added to each. |
| 3 | Science 3: one rule for returning skills | grades 2 to 8, biology, chemistry, physics; science.csv | The rule above written into each frame's Days or Seams text; "dormant" and "reactivation" removed from all 12 frames and from the progression notes (34 "dormant knowledge" and 17 "Reactivation" notes rewritten by the rule: 63 handoffs now say readiness check, 6 former "dormant" handoffs became retrieval). Physics' grade 8 rows (idle in grades 9 and 10) now open with readiness checks; Chemistry's choice "retrieval or a readiness check" resolved row by row; grade 8 moved one day from unit 2 (no readiness check left) to unit 4 (a new readiness check on grade 5 star brightness); the shared source map rows in grades 6 and 7 updated to match. |
| 4 | Science 4: scale-proportion in grade 3 | science.csv; science-grade-3, 4, 5 | s3-fossils model_out "patterns; scale-proportion"; s4-rock-layers model_in adds scale-proportion; Models carried rows in grades 3 to 5 trace it from grade 3. |
| 5 | Science 5: nature of science name | science-kindergarten to grade 5 | Bullet "Nature of science (how science works)" in all six; every in-table "How science works:" now "Nature of science:". |
| 6 | Science 6: time and check length | science-grade-3, 4, 5; 6, 7, 8 | Grades 3 to 5 Days name the shorter path at about 120 minutes a week (three lessons, same 30 weeks, no expectation dropped); grades 6 to 8 Days give the reason a one-day course-level check is enough. Time a day kept as picked (Cory, Desk 2026-11-14). |
| 7 | Science 7: grade 7 check 2 climbs | science-grade-7 | Check 2 traces an unseen plant's mass to carbon dioxide and water atoms regrouped into sugar, with light's energy shown. |
| 8 | Science 8: places | grade 3, grade 5, chemistry, physics | Svalbard (grade 3 unit 5), Wadi Al-Hitan in Egypt (grade 3 worked case), van Helmont in Brussels (grade 5 unit 2), the Nile, Ganges-Brahmaputra and Mekong deltas (chemistry unit 11), Allende (Mexico) and Murchison (Australia) meteorites (physics unit 10). |
| 9 to 21 | Science "Settled by the expert", all 13 rows | physics units 2, 5, 10; grade 3 unit 5; grade 2 units 2, 5; grade 1 checks; chemistry units 4, 7, 11; grade 5 units 2, 4; grade 7 checks | Each row applied as written, with one wording change: chemistry unit 4 says the sealed bag returns "as the opening retrieval task", not "the readiness opener", because conservation was used in Biology the year before (the rule above). Chemistry unit 7 also drops "a chemical hand warmer" from its device list, for the same reason as the dropped chemical pack. |
| 22 | Structure 1: end-of-unit assessment named | science-kindergarten to grade 3, grade 6 | Days bullets say each unit's days include its end-of-unit assessment (K to 2: no readiness check in K). |
| 23 | Structure 3: sensitivity line | science-kindergarten, grade 1 (and all others) | Every frame carries a Sensitivity reads bullet naming the agent read. |
| 24 | Structure 5: time a day | all 12 | For the lead time items marked settled ("yes, as picked"). |
| 25 | Structure 10: one name per thing | all 12 | "Course check", "end-of-year check", bare "mid-year check" now "course-level check" (mid-year, year-end as adjectives); Course-level checks sections in the one table shape `Check, After unit, Check days, Respond days, What it checks` (all 12, including the three high school courses). |
| 26 | Codex: grade 4 calendar conversion | science-grade-3, 4, 5 | The 4n/3 conversion replaced by the shared-calendar wording with an "estimate until the calendar exists" note; the calendar itself left to the structure fixer. |
| 27 | Codex: grade 4 missing math lean | science-grade-4 | Cross-subject row for math 4.NBT.A.2 (shares of 10, labels within 1,000), math unit 5. |
| 28 | Codex 4 and Desk 2026-11-14: no outside reader | all 12 frames | Every community, health, disability, faith, counselor, nurse and science-teacher reader replaced by the matching agent read (sensitivity, safety, answer-key), each naming the community and sources the sensitivity agent studies first (for example the Lower Elwha Klallam Tribe's own published account for Biology unit 9; the Deaf and hard of hearing community's own voice for grade 8 unit 2; atomic bomb survivors' testimony and Fukushima residents' accounts for chemistry unit 8; Tohoku communities' accounts for grade 6 unit 5; Indonesia's smallholder farmers and Indigenous peoples' alliance for grade 7 unit 5). Every "People" / "who reads, and any pay, is Cory's" item removed from For the lead. |
| 29 | Codex: course ids | science-grade-6, 7, 8 | For the lead course-id items marked settled by the Codex read (slug is the course identity). |
| 30 | Extra: literacy codes | science-grade-6, 7, 8, biology, chemistry, physics; science.csv | RST and WHST codes (6-8, 9-10, 11-12 bands) placed at the end of each unit's "What students learn" cell as "Also met (literacy, no added days)", with a Literacy standards bullet; the same codes written into the notes of the 122 progression rows those units own. |
| 31 | Extra: stale Pending markers (3) | science.csv rows phys-wave-particle-light, phys-em-radiation-effects; physics/frame.md For the lead 3 | Each resolved to RST.11-12.8, met in physics unit 7 as an also-met literacy standard. |
| 32 | Extra: safety agent per hands-on unit | all 12 | Every unit with hands-on work ends "Agent reads: sensitivity; safety (hands-on)"; each brief names the safety agent's sources (school science safety guidance, a chemical society's safety guide, safety data sheets of every chemical named). |

## Applied in a different place

| Item | Why |
|---|---|
| Literacy codes in progression `cross_subject` cells | scripts/progression.py fails a lean `ela:RST...` unless an ELA row names that code (none does), and science cannot lean on itself; putting the codes in the `standard` column would make them owned. So the codes sit in each row's notes ("Also meets (literacy, no added days; course unit n): ..."). If the structure fixer lets progression.py accept a science-owned literacy lean, the notes can move to `cross_subject` mechanically. |

## Not applied

| Finding | Reason |
|---|---|
| Science 1, the frame-write.md lesson 11 addition | Brief edit: the structure fixer owns it. |
| Science 3, frame-write.md lesson 16 and the GLOSSARY "retrieval task" row | Brief and glossary edits: the structure fixer owns them (wording note above). |
| Structure 4 (course-level checks stacking in the same weeks) | Needs the shared calendar; the structure fixer's, per the brief. |
| Structure 6 (school day and week definitions, generated day citations) | Same. The frames carry the estimate note only. |
| Structure 9 (course ids fix in the scripts) | Gate and catalogue work; the structure fixer's. |
| Structure 8 (lettered parts named by code) | NGSS performance expectation codes have no lettered parts; nothing to name in science. |
| Structure 11 (unit size, per-unit pieces) | The fix is ELA K to 5's; science units are untouched. |
| `scripts/frame.py sync` (frames.csv "behind the frame" notes) | Sync rewrites data/plans/frames.csv and the shared school calendar for every course; left to the lead or the structure fixer once all fixers finish. Only a note, not a failure. |

## Settled (not raised to Cory)

| Item | Settled by | Where it shows |
|---|---|---|
| The time a day stays as picked | Cory, Desk 2026-11-14 ("yes, as picked") | For the lead items in all 12 frames |
| Year length 160 with named condensations (grades 6 to 8, high school) | Cory, Desk 2026-11-14 | science-grade-7, 8 Days and For the lead |
| Course ids: slug is the course identity | Codex baseline read | science-grade-6, 7, 8 For the lead |
| No outside human reader; agent reads instead | Cory, Desk 2026-11-14; BASELINE rule 5 | Sensitivity and safety bullets, unit rows |
| Grades 3 to 5 keep 120 days, with a named shorter path | Science For Cory 1, answered by "yes, as picked" | grades 3 to 5 Days |
| Materials costs ($25 to $50 a unit or year, K to 5) | Writer's picks kept; the time and cost items marked settled | K to 5 For the lead |
| Returning-skills rule reading (idle grades counted) | The expert's own Biology and Chemistry examples | This report, all frames |
| Grade 5 For the lead 2 (grade 5 state science tests) | Left as the writer's pick (keep the order, no added test review); it already carries a pick and changes no scope | science-grade-5 For the lead |
| Accelerated math path, personal finance, social studies period, ELA novellas | Settled in the brief; no science frame is touched by them | none |

## For Cory

None.

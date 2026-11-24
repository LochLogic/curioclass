# Units read: science grade 5, 2026-11-24

COURSE-RUN stage 4 (Reads) for science-grade-5: all six unit plans read together.

## What I read

- AGENTS.md, docs/COURSE-RUN.md stage 4, docs/agents/EXPERT.md, docs/agents/lenses/science.md, docs/courses/UNIT-PLAN.md, docs/GLOSSARY.md.
- docs/courses/science-grade-5: frame.md, scope-and-sequence.md, s01 to s06, u01-1 and u01-2.
- data/plans/science-grade-5/days.csv.
- The course's rows in data/progressions/science.csv, grade 4's last unit plan and grade 6's s01.

## Verdict

The arc holds. Units build from matter (units 1 and 3) through ecosystems, Earth and sky, and Earth systems to the protection design unit. Continuity runs in from grade 4 and out to grade 6. The shadow record threads every unit. The most serious defect ran course-wide: every field 5 Owner cell named section N.1, even for codes that later sections teach. Two exits were also faulty: one reused an assessment case and one was physically inconsistent. Two respond days held retrieval tasks that came from misread days.csv notes. All are fixed. One cap question needs the structure pass.

## Findings

| # | Severity | Finding | Outcome |
|---|---|---|---|
| F1 | moderate | Field 5 Owner was "section N.1" in every unit, including codes taught in later sections, so section-plan writers would look in the wrong section. The written days (u01-1, u01-2) were not contradicted. | Fixed. New Owners: s01 Q1 "1.1 and 1.2", Q2 to Q4 "1.3 and 1.4"; s02 "2.1 and 2.2", "2.3 and 2.4", "2.5"; s03 "3.1 and 3.2", "3.3 and 3.4"; s04 Q1 "4.2 and 4.3", Q2 "4.1", Q3 "4.4"; s05 "5.1 and 5.2", "5.3 and 5.4"; s06 "6.1 and 6.5", "6.2 to 6.4". |
| F2 | moderate | Units 1, 2, 3, 5 and 6 have several sections but carry merged U3 to U11 headings, so the gate applies the 2,300 merged cap. s01 is at 1,847 words and s06 at 1,711, both above the 1,600 unit-plan cap. The s01 U fields duplicate u01-1 and u01-2, but they agree with them. | For the structure pass. |
| F3 | minor | The day 17 readiness check in s01 U6 gave different items and timing (five minutes each) from the readiness check unit 2 owns in s02 field 4. | Fixed. s01 now points to s02 field 4 (four minutes each, two to sort). |
| F4 | moderate | The s02 day 33 exit (mice eat seeds, an owl eats mice) reused the Q2 dune food chain, which breaks rule 4. It also drifted from the goal of a newcomer with no predator. | Fixed. The new exit is a meadow where voles eat clover seeds and an introduced grasshopper has no predator; goal map row 33 updated to match. |
| F5 | minor | In the s04 day 69 exit, the shadow turned from east to northeast while growing longer toward evening, which is the wrong order for a northern site. | Fixed. Directions swapped (16 cm northeastward, then 30 cm eastward); the key still holds. |
| F6 | minor | Field 4 in s04 (day 81) and s05 (day 99) invented respond-day retrieval tasks from days.csv notes that refer to the next unit's retrieval (days 85 and 92; days 100 and 103). The tasks took five response minutes, and the next unit never used them. | Fixed. Both rows removed; field 7 changed to "fresh retry 20" (s04) and "15 to a fresh transfer" (s05). |
| F7 | minor | The day 107 materials list a scale that is not in the course supplies. | No change: the section plan settles materials. |

No change, and why:

- u01-1 already handles the H-letter timing on day 2.
- Continuity in: s4-structures-function is retrieved on day 18 and s4-light-eye on day 75.
- Continuity out: grade 6 s01 retrieves s5-star-brightness and s4-light-eye on day 2, which matches days 75 to 77.
- Shadow-record days (3, 20, 36, 53, 68, 84, 100 and 114) agree across all the plans.
- The readiness hand-backs on days 44, 61 and 84 have both ends.
- Retrieval entries point only at rows already taught.
- Course checks carry the practical records through unchanged.
- Unit loads match days.csv.

### Day faults

None. Days are written only for unit 1 (u01-1, u01-2), and no fix touches them.

### For the structure pass

- unitplan.py: apply CAP_MERGED only when days.csv shows the unit has one section. Under that rule s01 and s06 fail the 1,600 cap. Also decide whether a multi-section unit's U fields shrink to pointers once its section plans exist.
- days.csv notes for days 81 and 99: reword them so the retrieval is clearly the next unit's, for example "grade 4 weathering and maps are retrieved in unit 5 (days 85, 92)".

### For Cory

Nothing new. The frame's open question about the state-test audience is still his.

## Lead-list items worked

0. The lead list (docs/reviews/lead-list-lens-pass-2026-11-17.md) has no items for this course.

## Gate results

- unitplan.py check science-grade-5: PASS for all 8 files (s01 to s06, u01-1, u01-2).
- sequence.py check science-grade-5: 0 failures.
- goalmap.py audit science-grade-5: listing only, no faults.

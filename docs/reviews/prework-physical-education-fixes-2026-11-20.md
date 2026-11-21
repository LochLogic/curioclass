# Physical education pre-work: stage 1 fix pass, 2026-11-20

Read: the second-model read (docs/reviews/prework-physical-education-gemini-2026-11-20.md, findings 1 to 9 and its
five questions, the main list); the real-page findings of the three calibration reads
(docs/reviews/calibration-physical-education-2026-11-20.md, expert run 1 #6 to #8;
calibration-physical-education-run2-2026-11-20.md, expert run 2 #7, #10 to #12;
calibration-physical-education-run2-gemini-2026-11-20.md, Gemini cal #10 to #13); the PE parts of data/plans/later.csv
L96; and the first reads (docs/reviews/prework-physical-education-read-2026-11-19.md and
progression-physical-education-2026-11-19.md) only to see what was already handled. Settled calls read first:
DESK-ANSWERS entries for q-later-arts-health-pe, q-prework-health-pe-1 and -2, q-prework-open-1 and -2. Each row claim
was checked against our words in data/standards/shape-pe-2024.txt and the row itself in
data/progressions/physical-education.csv. `python -X utf8 scripts/progression.py check physical-education`: 0 failures
after the fixes.

| # | Source | What | Decision | Where |
|---|---|---|---|---|
| 1 | gemini #1, gemini cal #13 | Approach page sends items to the wrong plan fields (safe space and supplies under unit field 2, family note in sources and pacing, two rooms merged with supplies, tools unnumbered, "field 8" and "field 9" unnamed, daily evidence under "principle 8") | Fixed: every heading names its unit or section field by UNIT-PLAN.md number; space, supplies, safe space and tools to unit field 8, family note to unit field 9, sources to unit field 10, check to unit field 5, lesson shape to section field 6, two rooms to section field 10; one line says fields not named add nothing for PE | APPROACH.md |
| 2 | gemini #1, gemini cal #13 | No unit field 7, so the shared hands-up self-marking step would apply to a teacher-judged skill task | Fixed: unit field 7 says the skill task and conduct are marked by the teacher watching against the cue guide, and groups come from the met, partly, not yet marks | APPROACH.md, unit field 7 |
| 3 | gemini #1 | Ten fields "missing" (unit 1, 3, 4, 6; section 2, 4, 6, 7, 11) | Not a fault for all but section field 6 (now filled with the lesson shape): an approach page fills subject slots only, and the shared fields stand as UNIT-PLAN.md says, now stated in one line. Gemini's added content (talk caps of two to three minutes, a four-group cap, limits such as no inversions) is new policy and was not added | APPROACH.md opening |
| 4 | gemini #1 | Check accommodations missing from section field 9 | Fixed: the existing adaptation rule now names closure and check tasks | APPROACH.md, section field 9 |
| 5 | gemini #1 | Unit field 2 does not name the indicator ids in our words | Fixed: first bullet of unit field 2 (the indicator's wording is never quoted) | APPROACH.md, unit field 2 |
| 6 | gemini #2, expert run 2 cal #12 | g10-choose-active-apply owns all nine S4.12 ids but drops self-expression, building goals, the after-school factors, using emotion strategies and reflection; STANDARD rule 5 says grade 10 "carries" what it owns | Fixed in place: the row now teaches every part of each id in short form and adds a conduct check for the emotion strategy; rule 5 says grade 10 owns them, teaching every part. Gemini's split moving S4.12.1 to 5 to grade 9 is settled, no change: Cory put the personal plan in short form in grade 10 (q-prework-health-pe-2) | physical-education.csv; STANDARD.md section 3 rule 5 |
| 7 | gemini #2 | g9-choose-active says the ids are owned in grade 11 | Fixed: grade 10 | physical-education.csv |
| 8 | gemini #3, expert run 1 cal #8, gemini cal #13, L96 | No sensitive-ground section; sacred-dance rule only on two rows; body, food, medical, gender and emotion rules scattered | Fixed: APPROACH.md "Sensitive ground" gathers the rules the PE pages and rows already state (bodies and food, dress, injury and medical conditions, water, cultural dance and games with the sacred rule, gender, emotions) and routes cultural and disability units to the sensitivity agent (FOUNDATION.md section 7). The sacred rule is now stated once there; the two rows that held it and nine other cultural rows (g1-dance-moves, g3-dance-steps, g4-dance-sequence, g4-world-activities, g5-fair-decisions, g8-culture-matters, g9-dance-forms, g10-games-culture, g12-community) point to it; STANDARD section 4 points to it | APPROACH.md; physical-education.csv, 11 rows; STANDARD.md section 4 |
| 9 | gemini #3.4 | Four emotion rows lack the mental-health boundary; no disclosure route | Fixed for the boundary: g1-calm-steps, g3-calm, g7-manage-feelings and g10-choose-active-apply point to the section, and g12-manage-emotions' copy became the pointer. The disclosure steps are not on any PE page: question 3 | physical-education.csv; APPROACH.md |
| 10 | gemini #3.5, Q4 | No leave-out rule | Question for Cory (leave-out policy) | question 2 |
| 11 | gemini #3 | Changing rooms, supplement advice and a PE safety read are not covered | Question for Cory (not stated on any PE page) | question 3 |
| 12 | gemini #4, Q2, expert run 2 cal #10, gemini cal #11 | No single default sessions or minutes for any band, no short path | Partly fixed: pacing now says each band's scope and sequence names its short path (bar C2). The numbers are a dose choice: question 4 | APPROACH.md, Pacing |
| 13 | gemini #5.1, expert run 1 cal #7 | STANDARD section 3 says K to 2 rows carry the grade-3-start ideas as `~CODE` at most, yet S2.2.2, S2.2.7 and S4.2.2 must be owned in K to 2 | Fixed: those three are owned in grade 1 or 2 at the depth their K to 2 wording asks; the tables' forms start in grade 3 (checked: g2-chase-flee, g2-stretch-why, g1-together-favorites) | STANDARD.md section 3 |
| 14 | gemini #5.2, expert run 1 cal #6 | Rule 3 says the PECAT first grade owns a skill, then gives two exceptions | Fixed: "by default", with the two exceptions marked settled (q-prework-health-pe-2) | STANDARD.md section 3 rule 3 |
| 15 | gemini #5.3 | progression.py lets grades 11 and 12 own span 12 ids | Follow-up (scripts/progression.py) | below |
| 16 | gemini #6.1 | g2-water-skills has no dry-land skill task | Fixed: life jacket and a floor reach rescue for every school; in-water only where a pool exists | physical-education.csv |
| 17 | gemini #6.2 | g6-stretch-types says the handoff skips a grade, but it assumes g5-fitt | Fixed: stale sentence removed (g3-warm-cool reaches it through g4-pulse-body and g5-fitt, no skip) | physical-education.csv |
| 18 | gemini #6.3, expert run 2 cal #7 | `~` carries skip grades with no note | Not a fault: a `~` carry is a later use, not a handoff; rule 1 asks for no carry in every grade, and every skipped handoff (assumes) carries its written reason | none |
| 19 | gemini cal #10 | g7-rest's skip reason sits only on g10-rest | Not a fault: the reason is stated once, on the receiving row where the readiness choice is made | none |
| 20 | gemini cal #10 | g7-dance-ideas hands on to nothing | Fixed: hands on to g9-dance-forms (canon and contrast return there), with the skip reason on g9-dance-forms; edges file updated | physical-education.csv; physical-education-edges.md |
| 21 | gemini #7.1, Q1, expert run 2 cal #11, gemini cal #11 | One pe row in data/courses.csv against "four courses, one per band" | Question for Cory (catalogue rows) | question 1 |
| 22 | gemini #7.2 | STANDARD section 6 leans omit social studies, grade 5 math and grade 8 science, and say math grades 6 to 7 | Fixed: science, math and social studies bullets match the csv; one line points to the csv column for each code (codes not copied a second time) | STANDARD.md section 6 |
| 23 | gemini #7.3 | Same-year leans in grades 4, 5 and 7 have no timing note | Not a fault at pre-work: the frame writes an "if later" line for every same-year lean (docs/pipeline/briefs/frame-write.md, item 8); section 6 now points to it | STANDARD.md section 6 |
| 24 | gemini #8.1 | shape-pe-2024.txt header line 7 copies the four standard statements | Fixed: our words | shape-pe-2024.txt line 7 |
| 25 | gemini #8.2 | UNIT-PLAN.md rule 15 has no PE carve-out | Follow-up (shared file); APPROACH unit field 2 now says the wording is never quoted | below |
| 26 | gemini #8.3 | S3.5.7 paraphrase says "Show", the source verb may be "Describe"; g4-world-activities checks naming only | Fixed the row: takes part in, describes and names the culture, assessed by describing, so it meets either verb. The indicator line itself is not this pass's to change: follow-up to check the verb at source | physical-education.csv; below |
| 27 | gemini #9 | APPROACH.md says only PECAT K to 5 and standard 1 tables were read | Fixed | APPROACH.md, unit field 10 |
| 28 | gemini #9 | STANDARD.md calls the approach page "(draft)"; shape-pe-2024.txt line 9 says "ids only" | Fixed | STANDARD.md line 8; shape-pe-2024.txt line 9 |
| 29 | gemini #9 | Stale lines in ADOPTION-BAR-SUBJECTS.md (PECAT "grade tables unread", approach yes owed), the lens "(draft)", pe-2014-to-2024.md line 71 | Follow-up (files not mine) | below |
| 30 | gemini Q5 | Re-confirm the approach page after the fixes | Not a question: the fixes place fields and gather rules already stated; no new policy was added, so the 2026-11-21 yes stands | none |
| 31 | L96 (health and PE share) | The health map names PA 3, 4 and 6 in grades 6 to 8 as taught in PE; the PE page did not say so | Fixed: STANDARD section 6 health bullet states the settled call | STANDARD.md section 6 |

## Questions for Cory

All four answered 2026-11-21 (Desk q-fix-pe-1): the recommended pick each time, applied the same day.

1. Catalogue rows (item 21): split the single k-12 pe row in data/courses.csv into four band rows (pe-k-2, pe-3-5,
   pe-6-8, pe-9-12, one frame per grade year, grades 11 and 12 electives), as was done for SEL and ELD.
2. Leave-out (item 10): may a school or family leave out a PE unit, and which (in-water tasks are already the
   school's; a cultural dance or game swapped for an open one; an outdoor activity that does not fit the place)?
3. Sensitive ground not yet stated for PE (items 9 and 11): bring health's disclosure steps (listen, no secret, the
   school's duty to report, the next adult; for a parent at home the child abuse hotline and 988 by purpose) and its
   "no medical advice" line to PE teacher pages; say that changing and changing rooms follow the school's own policy
   and no task asks a student to change in front of others; and decide whether units with striking tools, mats,
   climbing, resistance or outdoor trips get a safety read (the safety agent now reads science only).
4. Dose (item 12): default sessions and minutes per band. The second-model read proposes K to 2 80 x 30 minutes,
   3 to 5 80 x 35, 6 to 8 96 x 45, 9 to 12 80 x 45 per year, short paths of 60 to 64 sessions.

## Follow-ups for the lead

- scripts/progression.py `code_grades`: for physical-education span 12, owners grades 9 and 10 only, `~` in 9 to 12
  (Cory's two required years, q-prework-health-pe-2). The csv already meets it.
- docs/courses/UNIT-PLAN.md rule 15: add Physical education beside Arts and Computer Science (cite the SHAPE id and
  give its action in our own words; the indicator's wording is never quoted).
- data/standards/shape-pe-2024.txt line 164 (SHAPE.S3.5.7): check the verb at the SHAPE America page; if it is
  "describe", change "Show" to "Describe" (an indicator line, outside this pass's header-only permission).
- docs/ADOPTION-BAR-SUBJECTS.md: the PECAT sources row still says "grade tables unread" (all were read 2026-11-16
  and 2026-11-19), and the PE "Before a scope and sequence" row still lists the approach page's yes as owed (given
  2026-11-21, q-prework-open-1).
- docs/agents/lenses/physical-education.md line 8: "APPROACH.md (draft)" is stale.
- docs/standards-notes/pe-2014-to-2024.md line 71: PECAT was read in full for the grade tables on 2026-11-19, not
  only the K to 5 overview and standard 1 tables.
- Health (not edited here): no change is needed; the health map's PA 3, 4 and 6 in PE for 6 to 8 now matches the PE
  page. If question 3's disclosure steps are taken for PE, point PE to the health approach page's section field 1
  wording rather than copying it.

## Follow-ups done 2026-11-21

- data/standards/shape-pe-2024.txt, SHAPE.S3.5.7 (line 164): the indicator's verb is Describe, not Show (SHAPE America's 2024 standards web page, read 2026-11-21). Our paraphrase now says Describe; the row g4-world-activities already asks students to describe, so no progression change.

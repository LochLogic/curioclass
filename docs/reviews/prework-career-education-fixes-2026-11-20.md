# Career education pre-work: stage 1 fix pass, 2026-11-21

Read: the second-model read (docs/reviews/prework-career-education-gemini-2026-11-20.md, the main list); the
real-page findings in docs/reviews/calibration-career-education-2026-11-20.md (run 1: #9, #10, #12, #13),
calibration-career-education-run2-2026-11-20.md (#1, #9, #11, #12, #15) and
calibration-career-education-run2-gemini-2026-11-20.md (#10, #12, #13, #16, #17); the first read
(docs/reviews/prework-career-education-read-2026-11-20.md) to keep settled points closed; data/plans/later.csv L96
(career parts), with L90, L91 and L94; the Desk entries q-later-cs-career-library, q-prework-open-2, q-fix-health-1,
q-fix-pe-1 and q-fix-arts-1. Checked against data/standards/cte-career-clusters-2024.txt, scripts/progression.py
(STD_FILES, ANCHOR, ELECTIVE_FILES, the skip-grade note), docs/courses/CALENDAR.md, docs/courses/UNIT-PLAN.md and the
ELA, math, social studies and computer science progression files (every lean id named below exists at the grade
given). Pages changed: docs/courses/career-education/STANDARD.md and APPROACH.md. The standards file needed no change.

## Findings

| Source | What | Decision | Where |
|---|---|---|---|
| gemini #1, run2 #11 | Learner-goals file not loaded; page still said the PDF awaited saving | Fixed (status): the work itself is owed and tracked (later.csv L91) | STANDARD.md owed table and section 2: PDF saved, ncdg-2024.txt follows the terms read |
| gemini #1 | No rule for splitting the guidelines' indicators by stage, or for adult-only indicators | Question for Cory (Q4) | |
| gemini #1 | Gate note put only the learner-goals file in ANCHOR, leaving all 98 cluster and practice ids unchecked (ANCHOR holds one file) | Fixed | STANDARD.md section 3, "What the gate needs": both files required, the second by the ELECTIVE_FILES route or a list |
| gemini #1, run2 #1, first read #1 | codes() collapses every CTE id to `CTE.Career` | Follow-up (scripts, later.csv L94) | |
| gemini #2, run2 #12 | Pathways owns 58 sub-clusters one student does not all meet (C1) | Settled (Cory 2026-11-21, q-prework-open-2: none excluded); the page now says what owned means under student choice | STANDARD.md section 3, "Ownership" |
| gemini #2, run2 #15, gemini cal #17 | No handoff rule or reason line for the grade 8 to 10 step | Fixed | STANDARD.md section 3, "Handoffs" |
| gemini #3, run1 #12 | 36-week pacing against the 32-week CALENDAR.md year; short path "drops the second field task" though a unit need hold only one | Fixed: 96 sessions (72 hours), short path 64 (48 hours), the scope and sequence names the 32 dropped; sessions a week and minutes unchanged | APPROACH.md "Pacing" |
| gemini #4.1 | Practice 9 leans forward to grade 12 Economics | Fixed: taught at work and wage level with the grade 7 math leans, no Economics lean | STANDARD.md section 5 |
| gemini #4.2, run1 #10 | Grade 7 or grade 9 placement breaks the grade 8 and 10 leans | Fixed: the swap rows named | STANDARD.md section 7 |
| gemini #4.3, gemini cal #17 | "The grade's economics rows (labour markets)": no such grade 8 or 10 row | Fixed | STANDARD.md section 7, social studies line |
| gemini #4.4, run1 #9 | CS data rows and library lean not named by id | Fixed: five CS row ids; library "owned in the library progression" corrected to name the row id when the library progression exists (no library.csv yet) | STANDARD.md section 7 |
| gemini #5, gemini cal #10, L96 | "Financial Services (left to Economics)" hands a whole cluster away | Fixed | STANDARD.md section 6 |
| gemini #6, gemini cal #12 | Section field 2 held unit field 3's builds on and leads to | Fixed | APPROACH.md section field 2 |
| gemini #6, gemini cal #13 | Section field 1 and unit field 2: no sub-cluster or learner-goal ids; "the verb" though cluster ids are names and the practice text may not be quoted | Fixed | APPROACH.md unit field 2, section field 1 |
| gemini #6, run2 #9 | Assessment day scores the plan and piece with no written feedback and revision first (UNIT-PLAN field 5); no accommodations line | Fixed: field task day drafts, plan day returns feedback and revises, assessment day scores | APPROACH.md "The kinds of day", unit field 5 |
| gemini #6, gemini cal #17 | Unit field 7: no marking and response times; data items with no marking rule | Fixed | APPROACH.md unit field 7 |
| gemini #6 | Unit field 8 missing the safety step | Fixed: stated in field 8 by pointer to STANDARD.md section 6; the kinds-of-day copy now points there too | APPROACH.md |
| gemini #6, gemini cal #17 | Section fields 3 and 4 missing owned item numbers, day shown, the "if many" action | Fixed | APPROACH.md section fields 3 and 4 |
| gemini #6 | Unit field 3 missing strong or weak | Fixed | APPROACH.md unit field 3 |
| gemini #7.1 | No leave-out rule for sensitive sub-clusters | Question for Cory (Q1) | |
| gemini #7.2 | No steps for when a student tells the teacher something | Question for Cory (Q2) | |
| gemini #7.3 | Approach page does not send the section 6 teacher notes to the before-you-teach text | Fixed (pointer) | APPROACH.md section field 1 |
| gemini #7.4 | Family-note question assumes a working family member | Question for Cory (Q3) | |
| gemini #7.5, gemini cal #16 | Read list misses Public Safety, Environmental Protection and disability at work | Fixed | STANDARD.md section 6, "Reads" |
| gemini #8.1 | STANDARD.md owed table said the approach page awaits Cory's yes | Fixed | STANDARD.md owed table |
| gemini #8.1 to 8.3, first read #12 | ADOPTION-BAR-SUBJECTS.md lines 379, 395 and 567 stale | Follow-up | |
| gemini #8.4, run1 #13 | data/courses.csv `typical_grade` blank on both courses | Question for Cory (Q5); the personal finance retag is settled and held (L90) | |
| first read #11 | Practices 9 to 11 keep the publisher's titles | Not a fault: STANDARD.md section 1 lets practice names be cited; only the descriptions may not be copied | |
| first read #9 | Pathways menu width | Settled (Cory 2026-11-21: all 14 clusters), no change | |
| first read #12 | Lens says the 2024 guidelines are not read; COURSES-STATUS counts three courses | Follow-up | |

Counts: 20 fixed (one of them a settled call the page now states clearly), 1 not a fault, 1 settled with no change,
5 questions, 4 follow-ups.

## Questions for Cory

1. Leave-out: may a school or family leave out a unit on a sensitive sub-cluster (Military and National Security,
   Behavioral and Mental Health, Emergency Response, Judicial Systems, Public Safety, Resource Extraction)?
   Recommended, as SEL, PE and arts: yes; a swap to another sub-cluster of the same cluster keeps the ids met, and a
   left-out unit's ids are named as not claimed that year on the course page and in the family note.
2. Disclosure: recommended, as SEL, PE and arts: every section on a cluster named in STANDARD.md section 6, and the
   pay-gap unit, carries health's steps (docs/courses/health/APPROACH.md, "If a student tells you something").
3. Family note question: recommended, as arts: the take-home question may be asked of a family member, a school
   adult or a public worker profile, or answered for an invented worker, and sharing stays the student's choice.
4. Learner-goal indicators: recommended: when ncdg-2024.txt loads, each indicator is owned where first taught in a
   task, Pathways carries it as `~` at higher demand, and indicators that need adult work experience are excluded
   with a reason.
5. Catalogue: recommended: `typical_grade` 8 for cte-explore and 10 for cte-pathways, done with the held L90 edit.

## Follow-ups for the lead

- scripts/progression.py: codes() tab split (later.csv L94); `cte` in STD_FILES with both files; the cluster file in
  ANCHOR and ncdg-2024.txt required by the ELECTIVE_FILES route (or ANCHOR as a list); code_grades returns no grade
  for `CTE.` and learner-goal ids (STANDARD.md section 3).
- docs/ADOPTION-BAR-SUBJECTS.md: line 379 "To firm it" drop the practices wording (read 2026-11-16), keep the second
  state's rubric and add the order check on careertech.org; line 395 add the 72 sub-clusters and the learner goals
  once loaded; line 567 the approach page is approved, owed are the NCDG terms read and file (L91), the gate retool
  (L94) and the second rubric.
- docs/agents/lenses/career-education.md, "Sources": the 2024 guidelines were read in text 2026-11-20 and the PDF is
  saved; the terms are unread.
- docs/COURSES-STATUS.md shows three career courses; regenerate after the L90 retag.

Lead, 2026-11-21: the bar's career row updated (part of the bar follow-up); the rest are on the lead's list. The five questions are on the Desk (q-fix-career-1).

## Cory's answers applied (2026-11-21, Desk q-fix-career-1)

1. Leave-out with a same-cluster swap: STANDARD.md section 5 (new bullet, the six sub-clusters, ids named as not
   claimed on the course page and family note); APPROACH.md unit field 9 names the left-out ids; "Sensitive ground"
   points to section 5.
2. Health's "If a student tells you something" steps: STANDARD.md section 6 (new bullet, four sections plus the
   pay-gap unit); APPROACH.md section field 1 (teacher page).
3. Family note question widened (any trusted adult, an invented worker, a public interview or profile): APPROACH.md
   unit field 9; STANDARD.md section 6 (new bullet).
4. Placement rule for the guidelines' indicators: STANDARD.md section 3, "Ownership" (replaces "owned the same way");
   adult-only indicators listed in section 5.
5. Typical grades 8 and 10: STANDARD.md intro, section 3 table, settled-year paragraph, "Course list" and
   "Ownership" (owner grade = typical grade); APPROACH.md "Questions in this draft". L90 retag still held.

## Learner goals loaded 2026-11-21

- NCDA terms read 2026-11-21: the PDF has no notice; the site legal notice reserves all rights; the framework page
  names lesson writing and tracking by indicator code among its uses. Ids kept as printed, our own words only.
- data/standards/ncdg-2024.txt (130 owned CD and ALL indicator ids) and ncdg-2024-words.txt (one line each, ours).
  The SEL goals are leans and are not listed.
- STANDARD.md: owed row done; section 2 terms finding; section 3 "Learner goal placement" (Exploration 66, Pathways
  64, all 66 carried in Pathways, 5 left out as adult-only with reasons); section 5 names the five.
- APPROACH.md unit field 2 and "Evidence and sources"; the lens "Sources" line.

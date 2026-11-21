# English language development pre-work: stage 1 fix pass, 2026-11-21

Read for this pass: AGENTS.md; docs/agents/EXPERT.md; the lens docs/agents/lenses/eld.md; docs/COURSE-RUN.md stage 1;
docs/courses/UNIT-PLAN.md ("The unit plan: fields, in order" and "The section plan: fields, in order"); the two
pages, docs/courses/eld/STANDARD.md and docs/courses/eld/APPROACH.md; data/standards/wida-2020.txt (header and all
104 ids, to check the row count, the first-appearance key language uses and the Inform ids); the skill ids of
data/progressions/ela.csv (to check every lean id); the ELD rows of data/courses.csv; bar part 10 of
docs/ADOPTION-BAR-SUBJECTS.md (items 1 to 13, and the ELD status row); the head of docs/RUBRIC-ELD.md; health's
"If a student tells you something" (docs/courses/health/APPROACH.md) and SEL's leave-out rule (docs/courses/sel/STANDARD.md);
the findings in docs/reviews/prework-eld-gemini-2026-11-20.md, the real-page lines of
docs/reviews/calibration-eld-2026-11-20.md and docs/reviews/calibration-eld-gemini-2026-11-20.md,
docs/reviews/prework-eld-read-2026-11-20.md (to avoid reopening its settled points), data/plans/later.csv L96, and the
DESK-ANSWERS entries for q-prework-open-2, q-fix-health-1, q-fix-pe-1 and q-fix-arts-1. The Arizona, Rhode Island and
Montana pages were tried by web fetch on 2026-11-21: Arizona and Rhode Island refused (403), Montana's address is gone
(404), so no state figure was checked at source in this pass.

| Source | What | Decision | Where |
|---|---|---|---|
| Gemini #1; expert calibration #3; Gemini calibration #11; later.csv L96 | Ownership says "104 owned rows" but rows pair the two modes, so 104 ids sit in 56 rows | Fixed (checked: 8 SI + 48 pairs) | STANDARD section 2, Ownership |
| Gemini #1 | SI K-3 called an exception, though grade 3 is its last grade | Fixed: SI 4-12 is the one exception | STANDARD section 2, Ownership |
| Gemini #1 | scripts/progression.py has no ELD entry | Follow-up 1 | |
| Gemini #2 | Unit field 3 "one cluster earlier" skips grades inside 2-3, 4-5, 6-8, 9-12 and fails at six first-appearance key language uses | Fixed (the six checked against wida-2020.txt) | APPROACH, unit field 3 |
| Gemini #3 | Section field 2 held the student language goal and lacked "where its own results go" | Fixed: goal moved to section fields 1 and 6, results line added | APPROACH, section fields 1, 2, 6 |
| Gemini #3 | Section field 9 lacked check accommodations, reading load and extension on the same standard | Fixed | APPROACH, section field 9 |
| Gemini #3 | Unit field 5 had no interpretive part (bar item 11) and no accommodations line | Fixed; the Check row of the kinds table matches | APPROACH, unit field 5, kinds of day |
| Gemini #3 | Unit field 2 lacked limits and withdrawal day; section field 3 lacked owned item numbers; section field 5 lacked instrument and room with nothing; STANDARD 5.7 pointed to section field 2 | Fixed | APPROACH unit field 2, section fields 3, 5; STANDARD section 4 |
| Gemini #4; Gemini calibration #12; first read #5 | Montana "45 to 135 minutes by level" is contested (two reads disagree, page gone) | Fixed: no Montana figure given, with the reason | APPROACH, Pacing |
| Gemini #4 | "about 30 minutes" where frames need a number | Fixed: 30 and 45 minutes (the settled figures, hours exact) | APPROACH, Pacing; STANDARD section 2, Time |
| Gemini #4 | Arizona and Rhode Island still per search summary | Follow-up 5 | |
| Gemini #5.1 | Section field 1 names sensitive ground but no disclosure steps | Fixed: points to "Sensitive ground" | APPROACH, section field 1 |
| Gemini #5.3 | Unit field 5 and section field 7 do not carry the invented-character option | Fixed: both point to "Sensitive ground", which holds the rule once | APPROACH, unit field 5, section field 7 |
| Gemini #5.4 | Disclosure line lacks "tell the student who the next adult is" and the at-home hotline | Fixed: points to health's steps, as PE and arts (q-fix-pe-1, q-fix-arts-1) | APPROACH, Sensitive ground |
| Gemini #5.2 and #5.4 (alternative text) | Family note preview and opt-out, and a swap or leave-out rule for migration, war or loss host texts | Question 2 | |
| Gemini #6; Gemini calibration #13 | ELD-LA Argue (from 4-5) leaned on K to 3 opinion rows; ELA ids not exact | Fixed (every id checked in ela.csv); K to 3 opinion rows now lean on ELD-SI K-3 Argue | STANDARD section 5 |
| Gemini #7 | Newcomer strand "the cluster's Inform" names ids that do not exist in MA, SC, SS from 2-3 up | Fixed (checked) | STANDARD section 2, Newcomer strand |
| Gemini #7 | Newcomer strand: inside the 160 days or beside them | Question 1 | |
| Gemini #8.1 | Catalogue text stale (`eld-k12`) | Fixed (checked against data/courses.csv) | STANDARD section 2, catalogue and grain |
| Gemini #8.2 | Owed row says "Draft for Cory's yes" | Fixed | STANDARD, owed table |
| Gemini #8.2 | ADOPTION-BAR-SUBJECTS ELD status row stale | Follow-up 2 | |
| Gemini #8.3; expert calibration #13; Gemini calibration #14 | English learners with disabilities missing from STANDARD section 3 and APPROACH "Sets the work at levels" | Fixed | STANDARD section 3; APPROACH, first list |
| Gemini #8.3; Gemini question 3 | Bar part 10 item 5 names only newcomers and long-term English learners | Question 3 | |
| Gemini #8.4 | "All four modes" (WIDA has two modes, four domains); "talk and writing both" leaves out the interpretive mode | Fixed | STANDARD section 4, 1.26 row; APPROACH, "Across the unit" |
| Gemini #8.5 | RUBRIC-ELD.md lines 3 and 26 stale | Follow-up 3 | |
| Gemini #8.6 | "WIDA ids" in unit field 2 | Fixed: "the ELD standard ids" | APPROACH, unit field 2 |
| Gemini #8.7 | COURSES-STATUS ELD rows stale | Follow-up 4 | |
| Gemini question 2 | No own-words companion file for the 104 ids | Question 4 | |
| Expert calibration #12 | Mixed-grade group uses its youngest grade's frame (judgment) | Settled, no change: Cory took the 13-frame grain with this line (q-prework-open-2), and STANDARD section 2 says it plainly | |
| Expert calibration #14 | No day ratio by kind | Not a fault: no subject's approach page sets one; days by kind are summed per unit (UNIT-PLAN unit field 1) and set by the frame | |
| First read #2, #4, #6, #7, #8, #9 | Grain, sensitive ground, tool rule, validator notes, sources, bar items 13 and 14 | Still right, no change (validator header line checked) | |

Counts: 19 fixed, 2 not a fault (one of them settled), 4 questions, 5 follow-ups.

## Questions for Cory

1. Newcomer strand placement. STANDARD section 2 says the strand is "the first 20 days of each band", but there are
   13 grade frames of 160 days. Recommended: a 20-day on-ramp beside each grade frame, not inside its 160 days, so a
   newcomer arriving at any point takes it and then joins the class's current unit. Alternative: the first 20 days
   of unit 1 inside the frame.
2. Leave-out and swap for sensitive host texts. Recommended, as SEL, PE and arts: a school or family may swap a host
   text about migration, war or loss for another grade-level text on the same language goal (the ids stay met); a
   left-out unit's ids are named as not claimed that year on the course page and in the family note; the family note
   for such a unit previews the topic and says how to ask for the other text.
3. Bar part 10 item 5 (docs/ADOPTION-BAR-SUBJECTS.md, shared). Recommended: add English learners with disabilities to
   its notes, as STANDARD section 4 proposed and the approved approach page and lens already say.
4. Own-words file for the 104 ids. Recommended: no file for now; unit writers state the ids in our own words in unit
   field 2, since WIDA's terms bar modifying its content and a full paraphrase file is closer to that than a line per
   unit. Alternative: a planning-only file data/standards/wida-2020-words.txt before stage 2.

## Follow-ups for the lead

1. scripts/progression.py: add `'eld': ['wida-2020.txt']` to STD_FILES, `'eld': 'wida-2020.txt'` to ANCHOR, and a
   code_grades branch for `WIDA.ELD-XX.<cluster>.`: K (owner K), 1 (1), 2-3 (owner 3, grades 2 and 3), 4-5 (5; 4, 5),
   6-8 (8; 6 to 8), 9-12 (12; 9 to 12), SI K-3 (3; K to 3), SI 4-12 (owner 4; 4 to 12), per STANDARD section 2.
2. docs/ADOPTION-BAR-SUBJECTS.md, ELD status row: replace "Owed: the approach page's yes" with the 2026-11-21 approval
   (q-prework-open-2), the 2026-11-20 reads, this fix pass, and the owed scripts/progression.py entry.
3. docs/RUBRIC-ELD.md: line 3 "Not yet read by the curriculum expert" and line 26 (framework pages not opened) are
   stale; Appendix C was read in full 2026-11-20 (APPROACH.md, "Evidence and sources").
4. Re-run scripts/course_status.py for docs/COURSES-STATUS.md (ELD rows still say "shared page only"; Gemini also saw
   the band name doubled, "grades K to 2, grades K to 2").
5. The Arizona and Rhode Island minute figures (APPROACH.md, Pacing) still rest on search summaries; their pages
   refuse automated fetch and the cited guides are PDFs that need a download, so a person or a download-allowed run
   checks them before any is published.

Lead, 2026-11-21: follow-up 2 done (the bar's ELD row); 1, 3, 4 and 5 are on the lead's list. The four questions are on the Desk (q-fix-eld-1).

## Cory's answers applied (2026-11-21, Desk q-fix-eld-1)

1. Newcomer strand: a 20-day on-ramp beside each grade frame, frame keeps 160 days and its pairings. STANDARD section 2, Newcomer strand; APPROACH, Sensitive ground (Reads line).
2. Swap and leave-out, as SEL, PE and arts, plus the family-note preview for migration, war or loss host texts. STANDARD section 3 (new bullet, arts wording); APPROACH, unit field 9.
3. English learners with disabilities in bar item 5. docs/ADOPTION-BAR-SUBJECTS.md part 10 item 5; STANDARD section 4, 1.23 row marked done.
4. Planning-only own-words file for all 104 ids, written from structure only. New data/standards/wida-2020-words.txt (header in the arts words file style); pointed to from STANDARD section 1 (File) and APPROACH unit field 2.

## Follow-ups done 2026-11-21

- Arizona and Rhode Island minute figures (APPROACH, Pacing): both read at the state's own web page 2026-11-21. Arizona confirmed: 120 minutes a day in K to 5 and 100 in 6 to 12 as the floor for structured English immersion models (A.R.S. 15-756.01, subsection A). Rhode Island corrected: the 45 minutes is the length of a period, not a dedicated-period floor for all; the count of periods and how many must be dedicated depends on proficiency level, in full from 2030-31 (200-RICR-20-30-3, sections 3.2 and 3.8). Sources and read dates are on the page.

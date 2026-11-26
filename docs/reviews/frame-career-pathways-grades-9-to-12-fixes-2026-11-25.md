# Frame fixes: Career Pathways, grades 9 to 12 (2026-11-25)

Course `career-pathways-grades-9-to-12` (subject cte), the last career education course. One fix pass of COURSE-RUN
stage 3 over two reads: the fresh expert (docs/reviews/frame-career-pathways-grades-9-to-12-2026-11-25.md, S1, M1 to
M6, m1 to m8, J1 and J2) and the second model (docs/reviews/frame-career-pathways-grades-9-to-12-codex-2026-11-25.md,
C1 to C12).

Files changed: docs/courses/career-pathways-grades-9-to-12/frame.md; data/progressions/cte.csv (two row notes,
g10-prac-4-teamwork and g10-cd3-r3-rate-sources, LF endings kept). No unit's day count moved, so frames.csv and the
calendar need no sync.

## Gates

| Gate | Result |
|---|---|
| `python -X utf8 scripts/frame.py check career-pathways-grades-9-to-12` | 0 failures; 6 units, 96 days (92 in units, 4 for checks and respond days) |
| `python -X utf8 scripts/progression.py check cte` | 228 rows, 0 failures |
| `python -X utf8 scripts/stale.py check` | 121 files, 0 failures |
| `python -X utf8 scripts/gate.py --course career-pathways-grades-9-to-12` | 0 new failing findings against the baseline (the one known failure, no days.csv yet, is unchanged) |

## Findings

| Read | # | Applied or rejected | What changed, or why not |
|---|---|---|---|
| Expert | S1 | Applied | Unit 6 teaches the lateral check on paper: each of the three invented sources comes with "who is behind it" sheets (an invented about page of its owner, two invented pages that report on it, one that agrees and one that does not, and the dated table it should match where it cites a figure); the student leaves the source, reads the others, comes back and rates it. Named in unit 6's What students learn, its "Curio Class writes" list (a class set, one per pair, reused), the short path row, Models carried, the Devices bullet and the library Cross-subject row; the teacher page names that the same three steps run on a live browser where a school has one. Row g10-cd3-r3-rate-sources notes match. The sister frame's unit 1 has the same flaw and was not edited (lead's call) |
| Expert | M1 | Applied | Devices bullet and unit 4: 15 pairs at five minutes is 75 minutes, so the turns run over unit 4's first three sessions on both paths, five pairs a session (about 25 minutes), each pair finishing its paper table first while the rest work on paper. Full path: the comparison table day and the two job study days; short path: sessions 1 to 3 |
| Expert | M2 | Applied | Unit 5 fold list now "the second resume day, the outside-class day (into session 3), the second workplace day, the self-employment day (into session 2), the second interview day"; What students learn says the hook opens the first resume day |
| Expert | M3 | Applied | Unit 1 short path renumbered (1 to 8, values and learner moments in 2, study log and school plan in 3; folds: the second plan-and-models day, the learner-moments day, the second sorting day, the second field task day). Unit 4 short path renumbered (4 field task, 5 trade-offs and fallback, 6 plan day, 7 assessment, 8 respond; folds: the second job study day, the steps day and the school results day into 3, the fallback day into 5, the second field task day). Unit 4's What students learn now gives each piece its day count, adding to 13 |
| Expert | M4 | Applied, with Codex's timing | Check-ins: each of the three rounds split over two packet days (2 and 3, 5 and 6, 7 and 8), half the class a day, about 23 minutes. Interview assessment: about 70 seconds on one question and one follow-up plus a ten-second changeover, 40 minutes for 30, the rest at the start of the respond day for a larger class. Panels: a four-minute slot (three and a half to present and answer, half to change over), ten a session, 40 minutes; a class over 30 adds a fourth panel day from the work sessions. The expert's two-day interview split was rejected: it puts two performances on the written assessment day for half the class |
| Expert | M5 | Applied in part; rest to the lead | scripts/frame.py already reads codes with `split_codes()` (semicolons only), so the six ~ codes came out of unit 2's Owned standards cell and the check still passes. For the lead item 2 rewritten: frame.py done; scripts/course_pages.py `codes()` and scripts/unit_skeleton.py `split_list()` still split cluster codes at commas (script changes, not this job's) |
| Expert | M6 | Applied, a different way | No day moved between units (that would shift every later course and school day cited). Inside unit 3's 11 days the uncommon-job decision (CD3.A6) gets a day of its own and the changing-work piece (ALL2.A1, R1) closes the second trends day instead of taking its own. Short path: luck and experience are two short opening pieces in session 2, the decision has the rest; the fold list names the uncommon-decision day |
| Expert | m1 | Applied | SEL rows for units 2 to 6 give their own timing from the SEL 9 to 12 frame and calendar: unit 2 (plan-and-tidy, unit 11, after); unit 3 (snap judgments, unit 9, earlier: retrieval); unit 4 (interests unit 9, earlier; i-can-try unit 12, later); unit 5 (skills-grow, unit 12, after); unit 6 (different ways unit 9, teamwork and plan-and-tidy unit 11, earlier; who-is-affected unit 12, alongside). Every bridge kept |
| Expert | m2 | Applied as both | The computer science grade 10 row keeps its course days and adds school days (55 to 73, 83 to 105, 108 to 133, from data/plans/calendar.csv). Codex is right that the course days were correctly labeled; the school days match the column's unit |
| Expert | m3 | Applied | Cross-subject opening: the computer science, library and SEL frames are on file and cited, their leans stay bridges (lesson 32). For the lead item 6 replaced by the reconcile result (no Pending marker left); the library frame is cited per the lead's note: lateral reading in grade 9 unit 1 and on machine-made text in grade 10 unit 4, both before unit 6 |
| Expert | m4 | Applied, with Codex's range | "Why 96 fits": the 51 rows outside unit 2, six more inside it; a full-path student meets 72 to 78 rows (clusters here have four to six sub-clusters, so 12 to 18, not 21). STANDARD.md section 3 keeps "about 70" as its rounding (lead's file) |
| Expert | m5 | Applied, a different way | Grade 12 bullet: panels in week 31 (school days 152 to 155). Early seniors lose six sessions, and six fold with every closing day kept: unit 5 folds its second interview day (12 sessions), unit 6 runs its short path (course days 80 to 88, panels 85 to 87), check 2 on course day 89 and its respond day on day 90 (school days 149 and 150, week 30). A mixed section runs the folded path too, and the students who stay use weeks 31 and 32 for the last revision |
| Expert | m6 | Applied | Unit 4: "The private progress check falls here, early in the year's second half (weeks 19 to 23)" |
| Expert | m7 | Applied | Unit 2 Practices: "3 practiced, not judged, on each block's failed-first-try field task (unit 6 judges it on the project's second try)" |
| Expert | m8 | Applied | FS-1077 now cites the live address Codex opened (www.extension.umd.edu); "catalogue" left for a sweep, as the expert says |
| Expert | J1 | Applied (the expert's pick) | Unit 2 explore day: where one is free to read, one real worker's dated public account (a published interview or a federal profile) with source and date, beside the invented workers |
| Expert | J2 | Applied (the expert's pick) | Sub-cluster checks: each field task sheet ends with a one-line look-for strip the teacher ticks, with one word or phrase for the fix |
| Codex | C1 | Applied | Unit 3 field task day opens with the CD2.A7 piece: from a public worker profile or an invented worker case, a choice a stereotype narrowed (the stereotype, the option it closed, the evidence), a personal example only if the student chooses. The ad rewrite is now CD2.K7 at higher demand; CD2.R7 stays the next-choice plan. The row's note already says this, so no row change |
| Codex | C2 | Applied | As S1, with Codex's dated table added to the sheets |
| Codex | C3 | Applied in part | As M5 |
| Codex | C4 | Applied | As M2 and M3; the unit 1 short path no longer reteaches unit 2's readiness on the plan day before the check: the check sits in the respond day's last ten minutes and its reteach follows, as on the full path |
| Codex | C5 | Applied | As M1 |
| Codex | C6 | Applied | As M4 |
| Codex | C7 | Applied, a different way | As m5. Codex's "the 64-session path over 30 weeks" was rejected: it drops a third of the course for a two-week loss |
| Codex | C8 | Applied | Unit 3 who-holds days add a short earnings comparison from the federal median weekly earnings table (cpsaat37, by sex, race and Hispanic or Latino ethnicity), its population, year, national scope and the eleven-month note labeled, one supported comparison and one limit (a group median is not one person's pay or pay for the same work); cpsaat39 only for one job's own comparison. Short path session 1 names it. The eleven-month note on cpsaat37 rests on Codex's read of the same survey; the data sheet writer checks it at the table |
| Codex | C9 | Applied | Unit 6 and row g10-prac-4-teamwork: teams with different roles and approaches that use every member's field knowledge, clusters and jobs mixed where choices allow, no student changes their cluster or job to form a team; the sensitive-topics cell matches |
| Codex | C10 | Applied | As m1 |
| Codex | C11 | Applied in part; rest to the lead | As m3. The ADOPTION-BAR-SUBJECTS.md career education row (drop the five resolved Cory calls from the owed list, keep the second-state-rubric item) is not this job's file |
| Codex | C12 | Applied | As m4 |

Counts: 29 findings (17 expert, 12 Codex); 25 applied in full (four of them a different way: M4's interview split, M6,
m5 and C7), 3 applied in part with the rest left for the lead (M5, C3, C11), 1 applied as both readings (m2). Also
fixed while there: "four to seven sub-clusters" (no cluster has seven) to four to six, in Why 96 fits, unit 2 and
Sub-cluster checks; Same-year load's panel days to 152 to 155; For the lead item 5 to about $174.

## Left for the lead

- scripts/course_pages.py `codes()` and scripts/unit_skeleton.py `split_list()`: a semicolon-only standard-code
  reader (frame For the lead item 2).
- The sister frame, docs/courses/career-exploration-grades-6-to-8/frame.md, unit 1: its lateral check on four sources
  has the same paper-path flaw as S1 (no "who is behind it" sheets for a student without a device). Not edited here.
- ADOPTION-BAR-SUBJECTS.md career education row (C11).
- STANDARD.md section 3's "about 70" rows a student meets: 72 to 78 by count, if the lead wants it exact.
- The calendar clashes the expert listed (school day 72, week 15) for the after-core calendar pass.
- For the lead item 1 (the 14 `g10-clu-*` and two cd1 row notes, "unit" to "block") is unchanged and still the
  lead's to apply.

## For Cory

- Scope and access: practice 5 is carried last here, so a student with no device all year meets its digital part as
  not met, recorded on the course page. Pick: keep the shared-device turn (now over three sessions) and record the gap.
- Safety and rights: should a row own a first job's safety and rights (now practiced, not owned, in unit 5's teacher
  page)? Pick: no, keep it practiced.
- Supply cost: unit 6's paper source sheets add about $9 a class (a reusable class set, one per pair), bringing
  printing to about $174 a year for a class of 30. Pick: accept.
- Scope, only if the scope read finds the 64-session path overloaded: a lighter applied project on the short path or
  more sessions. Pick: keep and test.

# Frame read: computer science, grades 6 to 12 (2026-11-25)

Expert cold read of the seven Curio Class computer science frames for grades 6 to 12, written 2026-11-25. Brief:
docs/pipeline/briefs/frame-read.md with the lead's changes (subject computer-science, one combined read). A dated
record; not rewritten.

## What was read

- AGENTS.md; docs/pipeline/briefs/frame-read.md; docs/pipeline/briefs/frame-write.md (rules 13, 16, 18, 19, 20, 21,
  30, 31, 32); docs/agents/EXPERT.md; docs/agents/lenses/computer-science.md.
- docs/courses/computer-science/STANDARD.md (sessions, ownership of MS and HS ids, Specialty standards) and
  APPROACH.md; docs/ADOPTION-BAR-SUBJECTS.md criterion C1.
- data/progressions/computer-science.csv, grade 5 to 12 rows, checked against today's row changes.
- docs/courses/computer-science-grade-5/frame.md (Handed on, for the seam into grade 6) and
  docs/courses/computer-science-grade-6 to -grade-12/frame.md in full; grade 4's frame for the named people only.
- `python -X utf8 scripts/plan.py check` (all seven frames 0 failures; one note on grade 8) and scripts/stale.py
  (no computer science hits).

## Verdict

The seven frames are well built and teachable: every owned row is placed, the units are sized to what they own, the
math leans are bridged, and the sensitivity work is careful. Three things need fixing before scope and sequence:
grades 7 to 11 assume the previous elective was taken (only grade 12 applies rule 32), grade 11's Specialty share is
over the 10 percent line once counted honestly, and the check length differs between grade 10 and the rest, with grade
10 wrongly saying the others copy it. The rest is repeated cases, stale notes from the order the frames were written
in, and small wording.

Per frame:

| Grade | Verdict |
|---|---|
| 6 | Sound. Seam with grade 5 matches. Mid-year check is heavy for one sitting; one stale lead note. |
| 7 | Sound. Stale notes on the g7-collab-text seam and on grade 8's frame; "catalogue". |
| 8 | Sound. Handed on table misses g10-network-of-networks; one stale line; readiness timing misattributed to grade 7. |
| 9 | Sound content. No path for a student who skipped grade 8; seam cites no grade 8 units (stale); census repeat in the unseen check. |
| 10 | Sound content. Check rule conflicts with every other grade; no path for a student who skipped grade 9; unit 5 does not end on its respond day. |
| 11 | Needs a fix: Specialty days over the line; no path for a student who skipped grade 10; stale lead notes. |
| 12 | Strongest seams (the only frame that applies rule 32). Wrong claim about the people picks; day 24 overloaded; COPPA and CARE repeats. |

## Findings

### Serious

**S1. Grades 7 to 11 assume the elective before them was taken.** Each high school grade, and each middle school grade,
is its own elective course (STANDARD.md: "a real elective"), and a student may skip one. Grades 10 and 11 open every
row from the grade before as a year-before retrieval task (rule 16's retrieval branch) with no fallback, and grade 9
does the same for grade 8, grades 7 and 8 for the grade before them. A student who skips grade 9 meets grade 10's
unit 1 with no lists, records, parameters or data dictionary taught; one who skips grade 10 meets grade 11's network
and cleaning work cold. Grade 9 also begins ids owned in grade 12 (for example the career note on HS-SOC-CE-46) that a
grade 12 skipper never finishes, which is fine only if grade 9's use stands alone. Grade 12's "Course order" bullet is
the right pattern: it names each row from grade 11, gives it a ten-minute readiness check at a stated day, and says
what the unit teaches if the check shows the row missing.
Why it matters: rule 32 ("a course never assumes an optional course was taken") is broken in five of seven frames, and
the scope writer will copy retrieval tasks that a real class cannot do.
Fix: copy grade 12's "Course order" bullet into grades 7, 8, 9, 10 and 11. For each row used from the grade before,
keep the retrieval task for students who took that course and add (a) a ten-minute readiness check at the rule 16
timing and (b) a worked example inside the unit's first Understanding day for the students it flags. Rows two or more
grades back already carry readiness checks and need no change. For ids an elective begins and a later elective owns,
say in the later frame that it teaches the id from the start, with the earlier grade's use treated as a head start.
LAYER: frame (and process: add a line to frame-write.md rule 32 naming the electives case). REPEAT: yes (rule 32
exists; this is the first CS band read against it). Confidence: high.

**S2. Grade 11's Specialty share is over 10 percent, and the four frames count it four ways.** Grade 11 claims about
4.5 lesson equivalents of S1 work out of 52 teaching days (9 percent), but counts unit 3 sessions 5 and 6 as one when
both are full S1 sessions. Counted session by session it is about 5.5 of 52, 10.6 percent, over C1's line. The
denominators also differ: grades 7 and 11 divide by teaching days, grades 8 and 12 by all 64 course days. C1 and
STANDARD.md both say teaching days, and S1 days count as outside the standards.
Why it matters: C1 is an adoption bar criterion; a course over it fails the bar, and the scope gate will count days,
not the frame's estimate.
Fix: (1) every frame states its outside-the-standards days as "N of T teaching days" with T = 64 minus check days.
(2) Grade 11: fold unit 3 session 6's redraw into session 7's revision (or make session 6 half S1, half the owned
visualization row with the split named), bringing the count to 4.5 of 52 or less. (3) Grade 12 recounts by teaching
days: about 5 of 54, 9.3 percent, which passes but has little room; say so. (4) Grade 8 restates 4 of 64 as about 4 of
56. LAYER: frame. REPEAT: new. Confidence: high on the method, medium on the exact grade 11 count (half sessions are a
judgment).

**S3. Course-level checks run one lesson in six grades and two in grade 10, and grade 10 says the others copy it.**
Grade 10 holds each check over two lessons (days 30 and 31, days 62 and 63); grades 6 to 9, 11 and 12 use one 40-minute
sitting. Grade 10's For the lead 2 says "Grades 6 to 9, 11 and 12 copy it", which is false. Rule 19 says an end day
holds at most one full performance, and some one-lesson checks overrun it: grade 6's mid-year check scores four DAT ids
(one a device table task) plus three sampled items in 40 minutes; grade 9's and grade 11's year-end checks are similar.
Why it matters: the calendar pass and scope writers need one rule; a check that cannot be done in the minutes becomes
an unscored skim.
Fix: one rule for grades 6 to 12. Each course-level check takes two lessons: lesson one scores the unit before it
(unseen items or the product), lesson two samples earlier units (rule 20). Each frame finds the extra day from its
largest unit (grade 6 unit 1, grade 7 unit 2, grade 8 unit 2, grade 9 unit 1, grade 11 unit 2, grade 12 unit 3).
Correct grade 10's For the lead 2 to say it sets the rule. If the lead prefers one lesson, the alternative is to cap a
one-lesson check at two scored ids and say so in each frame; either way state the rule once in frame-write.md. LAYER:
frame and process. REPEAT: new. Confidence: high on the conflict, medium on two lessons being the better rule.

### Moderate

**M1. Grade 12's people picks repeat grades 4 and 6, and the frame says they do not.** Grade 12 unit 5 uses Grace
Hopper and Katherine Johnson and says the picks were "checked against the grade 6 to 11 rows, which name neither".
Grade 6's unit 6 names Katherine Johnson (with Dorothy Vaughan), and grade 4 names both Johnson and Hopper.
Fix: keep Hopper and Johnson in grade 12, where the reading is deepest, and change grade 6's unit 6 to Dorothy Vaughan
and Mary Jackson (Johnson named in passing only); or keep grade 6 and give grade 12 a first-person account from a
different professional (for example Jerry Lawson's oral history, if grade 4's use is light, or a living engineer with
a published interview). Correct grade 12's sentence either way. LAYER: frame. REPEAT: new. Confidence: high.

**M2. The census case runs three times, twice inside grade 9.** Grade 6 has the 1890 tabulation, grade 9 unit 4 a
national census case and its year-end "unseen" case is the census move from punched cards to online forms, and grade 12
the 2020 Census disclosure avoidance case. The grade 9 unseen case is not unseen after unit 4.
Fix: grade 9's year-end check takes another trajectory case (for example library catalogs from card drawers to online
search, or paper maps to GPS). Grade 6 and grade 12 may keep theirs (different eras and questions); grade 12 names
grade 6's as background. LAYER: frame. REPEAT: new. Confidence: high.

**M3. Other repeated cases.** COPPA is grade 10 unit 6's history case and again grade 12 day 5's law card. The LBNL 2024
data center report carries grade 8 unit 5's debate and grade 11 unit 6's local case. The CARE principles run in grade 7
unit 3, grade 11 unit 5 and grade 12 unit 2. Phishing appears in grades 8, 10 and 11.
Fix: grade 12 day 5 names COPPA as a retrieval card (one minute) and teaches a different law (for example FERPA or a
state student privacy law) as its new card. Grade 11 unit 6 picks a local case other than data centers, or names the
grade 8 debate and takes a new angle (siting and water, not energy). CARE stays in all three but each later frame says
what is new (grade 11: hiring data; grade 12: disclosure avoidance) and opens CARE as retrieval. Phishing is fine as a
spiral; no change. LAYER: frame. REPEAT: new. Confidence: medium (repeats can be deliberate; the fix is to say so).

**M4. Stale notes left by the writing order.** Grade 7's Handed on table and line 204 say g7-collab-text hands on to no
row and propose g8-text-project; the csv now has that link. Grade 7's For the lead 2 ("grade 8's frame was not on
disk") and 3 are stale. Grade 8 line 194 calls the link "the row change both frames propose". Grade 9 line 150 says
grade 8 has no written frame, so its seam table cites no grade 8 units. Grade 11's For the lead 2 says the grade 12
frame does not exist. Grade 12 says grade 11's unit numbers are not cited. Grade 6's For the lead 3 says grade 7 leaves
grade 6's unit numbers to the seam read; grade 7 now cites them.
Fix: rewrite each line to what is now true (the link landed; the frame exists) and add the unit numbers to grade 9's
and grade 12's seam tables from the grade 8 and grade 11 frames. Per rule 15, notes about other files go only under
For the lead. LAYER: frame. REPEAT: yes (stale cross-frame notes are a known pattern). Confidence: high.

**M5. Row g10-design-hcd still says "User stand-ins are classmates playing roles".** The frame uses persona cards that
are "never acted", which matches g8-design-for-all's landed change ("never by acting out a disability") and the
sensitivity rule. The row change for this note did not land.
Fix: in computer-science.csv, g10-design-hcd notes: "User stand-ins are persona cards read aloud, never acted." LAYER:
progression. REPEAT: new. Confidence: high.

**M6. Grade 8's Handed on table omits g10-network-of-networks.** g8-network-failure's hands_on includes it and
plan.py raises the note. Fix: add the row to grade 8's Handed on table, naming grade 10's unit. LAYER: frame. REPEAT:
new. Confidence: high.

**M7. Grade 12 day 24 carries too much.** It is the mid-year check's respond day plus two readiness checks (grade 11
items, and grade 9 flowcharts and modules) in its last ten minutes. Fix: keep the grade 11 check on day 24 and move the
grade 9 check to the last ten minutes of day 22 (unit 2's last teaching day), still within rule 16's "a few days
ahead". LAYER: frame. REPEAT: new. Confidence: medium.

**M8. Grade 10 unit 5 ends on its portfolio lesson, after the respond lesson.** Lesson 11 (portfolio) follows respond
lesson 10, and the draft and written feedback share lesson 7. Fix: swap lessons 10 and 11 so the unit ends on its
respond day, and split lesson 7 so feedback comes a lesson after the draft (rule 19). If that needs a day, take it from
the two-lesson check change in S3 or from unit 1. LAYER: frame. REPEAT: new. Confidence: high.

### Minor

- "catalogue id" in the header of grades 7 to 11 and grade 9 line 220: US spelling "catalog". (frame, new, high)
- Cross-references "(lesson 13)", "(lesson 16)", "(lesson 19)" in grades 6, 8 and 9 read as unit lessons; write
  "frame-write.md rule 16". (frame, new, high)
- Grade 9's For the lead is numbered 1, 6, 2, 3, 4, 5: renumber. (frame, new, high)
- Grade 9 unit 3 lesson 3: "a random-pick search can find a target sooner on some lists" reads as faster in general;
  say "on some runs, though not on average". (frame, new, high)
- g7-pick-approach: the csv says an attendance example, the frame a lunch count. Pick one; the frame's lunch count is
  fine, so change the row or note it under For the lead. (progression, new, high)
- Grade 8 says its readiness check sits on day 42 "as the grade 7 frame says"; grade 7 sets no such day. Drop the
  attribution. (frame, new, high)
- Session numbering is per unit in grade 6 and by course day in grades 7 and 8; pick course-day numbering everywhere
  for the calendar pass. (frame, new, medium)
- g9-simulate-data still says "heights within a stated range"; acceptable, but the landed wording elsewhere avoids
  body measures. Optional: "reaction times within a stated range". (progression, new, low)
- Grade 11 unit 6's Washington recycling law is cited "from memory"; the scope writer checks it at source.
  (frame, new, medium)

### Judgment calls

- **Social studies leans.** Grade 7 (sovereignty), grade 8 (the 1970 Fair Credit Reporting Act), grades 10 and 12
  (laws) touch civics, yet grade 8 says no row leans on social studies and grade 12 chooses no lean. Recommend no
  formal leans (US Government is a half-year core course and timing varies), but a one-line "by course order" bridge
  note in grades 8, 10 and 12 saying the unit teaches the civics it needs. Confidence: medium.
- **Grade 11 unit 5's load.** Two ids, a hiring case (EEOC), sovereignty and large-scale data in 5 teaching days. It
  can work if the hiring case carries both ids; otherwise take a day from unit 2. Confidence: medium.
- **Days outside the standards in grades 7 and 8** total about 7 across the two; both are under the line. Leave them.

## Row changes checked

Landed in data/progressions/computer-science.csv: g7-collab-text hands_on g8-text-project and g8-text-project assumes
g7-collab-text; g7-pick-approach board game; g9-computing-history satellite; g9-emerging-differences quantum;
g10-network-of-networks assumes g8-network-failure; g10-clean-text structuring; g10-breach-causes cases and industry;
g10-human-choices Bauserman; g10-history-policy COPPA; g10-design-hcd "human-centered"; all four grade 11 changes; all
five grade 12 changes; g8-design-for-all "never by acting out a disability". No UK spellings in the grade 6 to 12 rows.

Not landed: g10-design-hcd notes still say "classmates playing roles" (M5). g9-simulate-data keeps "heights" (minor).

## Calendar clashes (for the lead's calendar pass, not counted)

- Grade 9's mid-year check in week 17 shares the week with ELD's check.
- Grade 10's checks in weeks 15 and 16 and week 31 share weeks with library and physical education checks.
- Every grade puts its year-end check in week 32, with most other courses.
- Grade 12's year-end check sits in week 28 (rule 31, short form in weeks 29 to 32): no clash found.

## Settled by the expert

| Question | Answer |
|---|---|
| Seam grade 5 to grade 6 | Matches: grade 6's Picked up table lists what grade 5 hands on. |
| Seams grade to grade | Sound in content; only the notes and grade 8's missing row are off (M4, M6). |
| Electives retrieval paths | Missing in grades 7 to 11 (S1); grade 12's Course order bullet is the model. |
| S1 share under 10 percent | Grade 12 passes (about 9.3 percent of teaching days); grade 11 is over (about 10.6 percent) and needs trimming (S2). |
| One check-day rule | Two lessons per course-level check, grades 6 to 12 (S3). |
| Repeated cases | Hopper and Johnson, census, COPPA, data centers, CARE all repeat; fixes in M1 to M3. |
| Math leans | Bridged: grade 6 to math units 6 and 8; grade 7 percent and probability; grade 8 math units 4 and 6; grade 9's grade 7 probability readiness on day 25; grades 10 and 11 fine. Rule 13 holds. |
| Social studies leans | None formal; bridge notes recommended (judgment call). |

## For Cory

- **Electives readiness rule (scope).** Should every CS course in grades 7 to 11 carry grade 12's readiness path for
  students who skipped the year before? It adds about one readiness check per unit and a worked example; the expert
  recommends yes.
- **Check length (scope).** Two lessons per course-level check moves one teaching day per check in six courses; it is a
  rule across the band.
- **NOAA download (grade 11, For the lead 6).** The Climate Data Online extract is a download that waits on Cory's yes.

## What is right and should not be touched

- Unit sizing against owned rows, and every owned row placed once (plan.py 0 failures).
- Grade 12's Course order bullet and rule 31 handling of the senior calendar.
- The sensitivity work: CARE packs with tribal nations' own sources, persona cards never acted, the telephone operators
  and MiDAS cases chosen for what they teach.
- The math bridges and the paper paths.
- The phishing spiral across grades 8, 10 and 11.

## What it could not judge

- The CSTA boundary statements in the source store were not reread for this report beyond what the frames and rows
  quote, so depth against each boundary is taken from STANDARD.md's Depth section.
- The base-text store for the named cases was not available, so dates and facts marked "from memory" (Washington law,
  NCAI on the 2020 Census) are unchecked.
- Whether the half sessions in grade 11 unit 3 are S1 or owned-row work in practice is a scope-level count.

## Sources

docs/courses/computer-science-grade-5 to -grade-12/frame.md; data/progressions/computer-science.csv;
docs/courses/computer-science/STANDARD.md and APPROACH.md; docs/ADOPTION-BAR-SUBJECTS.md (C1);
docs/pipeline/briefs/frame-write.md and frame-read.md; docs/agents/EXPERT.md; docs/agents/lenses/computer-science.md;
scripts/plan.py check output and scripts/stale.py output, 2026-11-25.

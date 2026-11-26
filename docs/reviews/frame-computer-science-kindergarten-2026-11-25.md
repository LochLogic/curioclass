# Frame read: Computer Science, Kindergarten (2026-11-25)

Expert cold read of docs/courses/computer-science-kindergarten/frame.md, the pilot frame for computer science, by
docs/pipeline/briefs/frame-read.md with the after-core changes the job set. I did not write the frame.

## What I read

- docs/agents/EXPERT.md; docs/agents/lenses/computer-science.md; docs/ADOPTION-BAR-SUBJECTS.md (pass rule, shared core
  C1 to C16, part 5 computer science, the "Before a scope and sequence" row for computer science);
  docs/courses/computer-science/STANDARD.md and APPROACH.md in full.
- docs/agents/decisions/DESK-ANSWERS.md, every entry naming computer science: 2026-11-16 (q-later-cs-career-library,
  q-later-followups-1), 2026-11-20 (q-prework-cs-1), 2026-11-21 (q-prework-open-1, q-fix-cs-1, q-fix-cs-2), and the
  2026-11-20 course run entry (dose and shape). No entry after 2026-11-22 names the subject.
- docs/pipeline/briefs/frame-write.md, including "After-core courses (added 2026-11-25)".
- The frame in full; its rows in data/plans/frames.csv (5 units, 32 days, 30 minutes, 1 a week, 32 weeks, term year)
  and data/plans/course-list.csv (rows `grade:K`, term year, so not a band course: no Year column is owed);
  data/plans/calendar.csv for this course, for math kindergarten, and for every kindergarten course with a check.
- data/progressions/computer-science.csv: the 14 kindergarten rows (16 EK ids) and the 15 grade 1 rows (the seam).
- docs/courses/math-kindergarten/frame.md, Units table (the only lean); docs/courses/CALENDAR.md (stagger rule,
  target weeks, generated breaks).
- docs/reviews/progression-computer-science-2026-11-19.md, prework-computer-science-read-2026-11-19.md,
  computer-science-open-material-2026-11-16.md (the scout).
- Gates: `python -X utf8 scripts/frame.py check computer-science-kindergarten`: 0 failures (note: 5 units, 32 days, 28
  in units, 4 for checks and respond days). `python -X utf8 scripts/frame.py calendar`: grade K clashes at week 12
  (computer-science, health) and week 27 (computer-science, health, library). `python -X utf8 scripts/stale.py check`:
  70 files, 0 failures.
- At source, 2026-11-25: the Raspberry Pi Foundation curriculum pages (archive and current), Oak National Academy's
  Year 1 computing units, section508.gov, the NCDJ style guide (see Sources).

## Verdict

The frame is sound in what it teaches: all 14 kindergarten rows and all 16 EK ids are placed once, the depth follows
the owner rows' notes with an "Out" line in every unit, every unit is unplugged first with a full paper path, the K to 1
seam is answered row for row, and the one lean on math kindergarten is cited correctly with an "if later" bridge. The
biggest risk is the time budget the other frames will copy: 14 of 32 sessions are assessments or respond days, and
weeks 10 to 13 and 25 to 28 hold four straight weeks with no new teaching, for five-year-olds who meet once a week. The
one change that matters most is to let each course-level check stand for the end-of-unit assessment of the unit just
before it (as math kindergarten's year-end check does), which returns four sessions to teaching without moving a check
week. The partial base also needs its edition named: the Year 1 units adapted here sit in the publisher's archive, no
longer maintained.

## Findings, most serious first

### 1. Four-week assessment runs, 44 percent of the year (Major; LAYER frame; REPEAT new)

**What is wrong.** Every unit carries an end-of-unit assessment and a respond day, and each course-level check carries
its own respond day, so 10 + 4 = 14 of 32 sessions are check or respond. They bunch: unit 2's assessment (day 10) and
respond (day 11), then the mid-year check (12) and its respond (13); unit 4's assessment (25) and respond (26), then the
year-end check (27) and its respond (28). Calendar.csv confirms these days fall in weeks 10 to 13 and 25 to 28. Only 18
sessions teach (units at 3, 4, 6, 3 and 2), and two of them are overloaded for the 23 usable minutes the Days bullet
leaves (30 less 3 retrieval, less 4 put-away): unit 1 session 2 (make the rules, act out right and wrong, every pair's
first device turn, say why a rule helps) and unit 2 session 2 (people made the rules, people design tools, make a game
step-card set, a partner follows it).

**Why it matters.** A month of checking twice a year in a once-a-week specials class is what an adoption reader marks as
time away from the standards (C1's "content outside the course" spirit, C2's reasoned year plan), and the units at three
teaching sessions give each row about one session. The frame's For the lead 1 and 8 hand this shape to grades 1 to 5,
so it would be built five more times.

**Fix.** Let the mid-year check stand for unit 2's end-of-unit assessment and the year-end check stand for unit 4's,
with the respond day after each check serving both, as math kindergarten's year-end check stands for unit 8's own
(calendar.csv label, math-kindergarten unit 8). Check weeks stay 12 and 27. Days become: unit 1, 6 (4 teaching, end,
respond; days 1 to 6); unit 2, 5 (5 teaching; days 7 to 11); mid-year check 12, respond 13; unit 3, 9 (7 teaching; days
14 to 22); unit 4, 4 (4 teaching; days 23 to 26); year-end check 27, respond 28; unit 5, 4 (days 29 to 32). Total 32,
teaching 22. Use the new sessions to split the two overloaded sessions above and to give unit 3 a second make or modify
session. Rewrite both "What it checks" cells: the mid-year check scores unit 2's items in full (EK-ALG-PS-01, -ML-02,
-IM-03, EK-SOC-HU-15) and samples unit 1; the year-end check scores unit 4's three DAT ids in full and samples units 1
to 3 (lesson 20 then holds, since the unit's own items are its end-of-unit evidence). Fix the Days bullet's unit counts
and the line "18 teaching sessions for 14 rows" (finding 5). If the lead reads APPROACH.md Pacing ("every unit ends with
a respond day") as forbidding a shared respond day, the lighter fallback is to drop only the end-of-unit assessments of
units 2 and 4 into the checks and keep their respond days: 2 sessions back instead of 4. Say in For the lead which
shape grades 1 to 5 copy. Confidence: likely (strong reasoning; the math kindergarten precedent is in the repo).

### 2. The partial base is the archived edition, and the frame does not say so (Moderate; LAYER base text; REPEAT new)

**What is wrong.** The three Year 1 units adapted here (Technology around us, Moving a robot, Grouping data) are listed
today only under raspberrypi.org/curriculum/archived, whose page says the resources "are no longer maintained"
(opened 2026-11-25; teacher guide dated 3 May 2023). The current England resources are served from Oak National
Academy, whose Year 1 computing list shows three units of 6 lessons: Digital painting, Digital writing and Creating
animations in programs, the three this frame leaves out. The frame, the scout and STANDARD.md name "the Teach Computing
Curriculum" with no edition.

**Why it matters.** A later writer who opens the current site finds none of the mapped units, or adapts a newer edition
whose lessons differ from the Source map. The store folder (For the lead 4) would load the wrong set. Every computer
science frame through grade 8 shares this.

**Fix.** In the Base text bullet and the Source map heading, name the edition: "Teach Computing Curriculum, archived
edition (raspberrypi.org/curriculum/archived, key stage 1, resources dated 2023), no longer maintained by its
publisher." Rewrite For the lead 4 so the store folder is loaded from the archive, with each file's own licence line
read (the archive pages carry no licence statement; the scout read the Open Government Licence v3.0 on the
teachcomputing.org terms page). The claim that the lesson files "download only after signing in" could not be confirmed
at source; mark it "to be checked when the folder is made" rather than state it. Add a For Cory line (below). Confidence:
firm (two publisher pages agree).

### 3. Unit 2 puts the make session before the modify session (Moderate; LAYER frame; REPEAT new)

**What is wrong.** The frame's Day kinds bullet and APPROACH.md both say understanding before modify before make. Unit 2
session 2 has children make their own step-card set for a game (a make), and session 4 is the unit's fluency (modify)
session, "change one step of a working step-card set". The scope writer will copy the order as written.

**Why it matters.** It is the course's own stated rule, broken in the unit every later algorithm row builds on, and
the pattern grades 1 to 5 will read.

**Fix (settled below).** Session 2 becomes the modify session: the class changes one step of a working class routine
and checks it, which is also the evidence that "a person can change it" (EK-ALG-IM-03); session 4 becomes the make: a
step-card set for a game a child knows, followed by a partner, plus sorting the same cards by a new attribute. No day
count changes. Confidence: firm (frame and APPROACH.md agree).

### 4. Check weeks 12 and 27 clash with health and library (Moderate; LAYER frame and process; REPEAT yes, stagger findings of the 2026-11-14 frame reads)

**What is wrong.** The weeks avoid the core check weeks, as the after-core brief asks (core K checks: ELA 16 and 32,
math 17 and 31, science 14 and 29, social studies 15 and 30, all matching CALENDAR.md's K row). But
`frame.py calendar` lists grade K week 12 (computer-science, health) and week 27 (computer-science, health, library) as
stagger breaks; health K to 2 uses weeks 12 and 27 and library kindergarten 13 and 27 to 28. The rule For the lead 1
gives grades 1 to 5 ("mid-year in a free week near the middle, year-end in the last free week") is the same rule the
other after-core frames used, so every subject lands on the same few weeks.

**Why it matters.** A kindergarten child would sit three course-level checks in week 27, and the generated CALENDAR.md
line will report breaks the brief says are allowed, so a later reader cannot tell a real break from an accepted one.

**Fix.** For the lead, with the pick: after-core checks in K to 5 avoid core check weeks (the brief) and also avoid any
week already holding another after-core check for that grade where a free week sits within two weeks; where none does,
the overlap is accepted and named. For this course the year-end check has no free week near 27 (weeks 26 to 32 are all
taken), so keep 27 and name the overlap; the mid-year check could move only with a unit (stagger tool 5c), so keep 12
and name it. Then add the rule to CALENDAR.md's stagger list so `frame.py calendar` reports after-core overlaps as notes,
not breaks, and change For the lead 1's method line to "check the grade's after-core weeks too". Confidence: likely.

### 5. "About two sessions a row" misquotes the progression read (Minor; LAYER frame; REPEAT new)

The progression read settled "about two sessions a row" for 14 to 16 rows against 30 to 36 sessions in all
(progression-computer-science-2026-11-19.md, Settled table), counting checks. The frame says its 18 teaching sessions
for 14 rows are "about" that; they are 1.3 a row. Fix: "32 sessions for 14 rows is the progression read's two sessions a
row; 18 of them (22 after finding 1) teach." Confidence: firm.

### 6. The sensitivity read's sources are not named (Minor; LAYER frame; REPEAT yes, lesson 30 kind)

Unit 1's line asks the agent to study "disability-led guidance on describing assistive technology" without naming it,
and the federal Section 508 site is run by the General Services Administration for federal accessibility work
(checked 2026-11-25); it has guidance pages (alternative text, captions) but no plain-language page on assistive
technology for families. Fix: name the National Center on Disability and Journalism's Disability Language Style Guide
(free, English and Spanish, revised 2021; ncdj.org/style-guide) and one disability-led organization's own language page
chosen by the agent and recorded, and keep Section 508 only as background on accessible technology. Confidence: likely.

### 7. The leave-out line offers exactly the units the bar's fail line names (Minor; LAYER frame; REPEAT new)

STANDARD.md section 3 lets a school swap or leave out a named unit "for its community's reasons". The frame names units
4 and 5, the data and society units; the bar part 5 fails a course with "nothing on data or society". Unit 4 asks about
games, weather and books and has no community ground to leave it for. Fix: name unit 5 as the leave-out (homes, jobs);
name unit 4 as swap only (a different neutral question set), and say the course page then claims all three DAT ids.
Confidence: a judgment call.

### 8. Two wording slips (Minor; LAYER frame; REPEAT new)

- Unit 3 "Why this unit, here": "Placed across weeks 14 to 21, the core check weeks". Only 14 to 17 are. Fix: "Placed
  across weeks 14 to 21, which include the core check weeks 14 to 17."
- Source map: "Programming B: Programming animations ... unit page not found 2026-11-25". The archived key stage 1 page
  lists it ("Programming B - Programming animations"), and its current version on Oak, "Creating animations in
  programs", has 6 lessons; Digital painting and Digital writing show 6 lessons each there too. Fix the three "Lesson
  count not opened" cells to "6 (Oak listing, 2026-11-25)" and drop "page not found".

## Data checks

| Check | Result |
|---|---|
| Owned skills | All 14 `grade:K` rows placed once (gate and my read); no other grade's row is taught. Review uses (attribute-cards in unit 4) are named as review in the text, not in Skills |
| Standards in full | All 16 EK ids in Owned standards, each at its owner row's depth with an "Out" line. No lettered parts in EK ids. EK-ALG-ML-02 is met unplugged as the row's notes set |
| Units and reasons | Each reason holds; order uses no model before it is taught (step-card unit 2, then arrow cards unit 3; attribute-cards unit 2, then the graph's groups unit 4). One inside-unit order fault (finding 3) |
| Days | 28 in units plus 2 checks plus 2 respond days equals 32, matching frames.csv and the 30 x 32 default (Desk q-fix-cs-1). Share fault: finding 1 |
| Calendar | Every calendar.csv row matches the frame: units 1 to 5 in weeks 1-5, 6-11, 14-21, 22-26, 29-32; checks day 12 (week 12) and day 27 (week 27); respond days 13 and 28. Clashes with health and library: finding 4 |
| Source map | Lesson titles of the three adapted units checked at source and correct (Technology around us 1 to 6, Moving a robot 1 to 6, Grouping data 1 to 6). Every lesson placed or left out with a reason. Edition: finding 2 |
| Seams | No course before. All 16 hand-ons answered by the grade 1 rows' assumes (checked by script) |
| Cross-subject | math kindergarten unit 2 (days 19 to 44, weeks 4 to 9) teaches mk-sort-count; unit 3 (days 45 to 63, weeks 9 to 13) teaches mk-shapes-positions; both citations match calendar.csv; each lean has an "if later" line |
| Stale notes | stale.py clean; the one Pending note (BASE-TEXTS.md) is true: no Teach Computing row and no store folder exist |

## Lens checklist, course frame layer

| Line | Met? |
|---|---|
| An id taught below its boundary or past it | Met: depth from owner rows, "Out" in every unit, grade 1 constructs (events, repeat) kept out |
| A Specialty id claimed wrongly, or an S2 id | Not applicable (none claimed, said so) |
| AI as one late unit with no data or algorithm work | Met: the sorting rule sits in unit 2, as an algorithm |
| No unplugged path in a unit | Met: every unit unplugged, paper path for both device days |

Bar part 5 at frame level: items 1, 2, 3, 5, 6 and 7 met; item 4 (real, current uses) met at kindergarten depth by unit
5's pictures; items 8 and 9 are for the unit plans (unit 3's end-of-unit assessment reads and fixes code, as item 8
asks).

## What the other computer science frames should copy, and should not

Copy: one unit per concept area with an order reason; the "Practices and concept areas" column with CSTA practice codes
(For the lead 3); the Out line in every unit; the device-day four ways and the paper path that meets every id; the
privacy line; per-unit costs; the "if later" lean bridges; the Swap or leave out bullet (with finding 7's correction).

Do not copy: an end-of-unit assessment and respond day directly before a course-level check (finding 1); a make session
before the modify session (finding 3); "last free week" check placement without reading the other after-core weeks
(finding 4); an unnamed base edition (finding 2); the "two sessions a row" sentence (finding 5).

## What is right and should not be touched

The unit order and its reasons; the K to 1 seam table; the floor-grid safety lines (walk, no blindfolds, tape flat, a
child who cannot walk the grid directs or moves the toy); left and right taught with hand signs and a shape, never color
alone; class data about things only; no account anywhere.

## What I could not judge

Whether the archive's lesson files need a sign-in (not stated on the pages); the archive files' own licence lines
(the store folder does not exist); the third-party content of each adapted lesson.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Unit 2: session 2 becomes the modify session (change one step of a class routine), session 4 the make (a game step-card set followed by a partner, plus a re-sort) | Restores understanding, modify, make; the modify task also evidences EK-ALG-IM-03; no day change | docs/courses/computer-science-kindergarten/frame.md |
| Unit 1 sensitivity source: NCDJ Disability Language Style Guide plus one disability-led organization's page, Section 508 as background only | A named, free, current source in English and Spanish | same |
| Source map counts for the three left-out units: 6 lessons each (Oak listing) | Checked at source 2026-11-25 | same |
| Unit 3 wording on the core check weeks | Only weeks 14 to 17 are core check weeks | same |

## For Cory

- **Which edition is the partial base.** The units this course adapts now exist only in the publisher's archive, no
  longer maintained; the current England resources live on Oak National Academy and, for Year 1, cover only the three
  units this frame leaves out. Pick: keep the archived edition for K to 8 as a fixed text (the brief's adoption stands),
  loaded once into the store, and check Oak only where a grade's frame wants a newer unit. This affects every computer
  science frame through grade 8.
- The sign-in for the store download stays as For the lead 4 says, if the archive turns out to need one (an account is
  Cory's).

## Sources

- https://www.raspberrypi.org/curriculum/archived : archive status, "no longer maintained".
- https://www.raspberrypi.org/curriculum/archived/key-stage-1 (reached as /curriculum/key-stage-1): Year 1 unit list,
  teacher guide dated 3 May 2023.
- https://www.raspberrypi.org/curriculum/key-stage-1/computing-systems-and-networks-technology-around-us and
  .../data-and-information-grouping-data, .../programming-a-moving-a-robot (search listing): lesson titles.
- https://www.raspberrypi.org/curriculum/gb : current England resources served from Oak (key stage 1, 6 units, 36
  lessons).
- https://www.thenational.academy/teachers/programmes/computing-primary/units?years=1 : Oak Year 1 computing units.
- https://www.section508.gov/ : run by the General Services Administration; guidance pages, no family-facing AT page.
- https://ncdj.org/style-guide/ (search result, not opened): NCDJ Disability Language Style Guide, revised 2021.

## For the source list

- The Raspberry Pi Foundation archive address (https://www.raspberrypi.org/curriculum/archived) and the fact that the
  current England computing resources are on Oak National Academy belong in docs/APPROACH-SOURCES.md beside the
  scout's Teach Computing entry.
- NCDJ Disability Language Style Guide, https://ncdj.org/style-guide/, free, English and Spanish.

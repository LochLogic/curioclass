# Frame read: Library and Research Skills, kindergarten, 2026-11-25

Expert cold read of docs/courses/library-and-research-skills-kindergarten/frame.md, the library subject's pilot
frame, by docs/pipeline/briefs/frame-read.md with the after-core changes in docs/pipeline/briefs/frame-write.md. I
did not write the frame. I edited no file but this report.

## What I read

- docs/agents/EXPERT.md; docs/agents/lenses/library.md; docs/ADOPTION-BAR-SUBJECTS.md (the pass rule's small-course
  paragraph, part 11 and the library row of "Before a scope and sequence in this subject"); docs/courses/library/STANDARD.md
  and APPROACH.md in full; every DESK-ANSWERS.md entry naming library (2026-11-11, 2026-11-15 L43, 2026-11-16,
  2026-11-20 course shape and dose, 2026-11-21 q-prework-open-2 and q-fix-library-1).
- docs/pipeline/briefs/frame-write.md, including "After-core courses (added 2026-11-25)".
- The frame in full; its row in data/plans/frames.csv; its rows in data/plans/calendar.csv and the kindergarten rows of
  every other course there; docs/courses/CALENDAR.md (stagger rule, target weeks).
- The rows cell `grade:K` in data/plans/course-list.csv over data/progressions/library.csv (seven K rows) and the
  eight grade 1 rows (no grade 1 library frame exists yet; this is the first library frame).
- The Units tables of the ELA, science and social studies kindergarten frames (for the cross-subject citations).
- data/standards/aasl-words.txt (the ten ids the frame names); docs/reviews/progression-library-2026-11-21.md;
  data/plans/later.csv L103.
- The continuum's PK to 2 band file (S:\CurioClass-sources\library\aasl-2026-11-21\esifc-pk-2), extracted as text
  in the scratchpad with `python -I` to spot check the frame's L103 result; nothing copied.
- Gates: `python -X utf8 scripts/frame.py check library-and-research-skills-kindergarten`: 0 failures (note: 4 units,
  30 days, 24 in units, 6 for checks and respond days). `python -X utf8 scripts/frame.py calendar`: grade K clashes in
  week 27 (computer science, health, library) and week 28 (ELD, library, physical education). `python -X utf8
  scripts/stale.py check`: 70 files, 0 failures.

## Verdict

The frame is sound in its bones and a good pilot: every K row sits in one unit, the one owned id (AASL.V.C.1) and the
nine carried ids each name their later owner correctly, the seams match the grade 1 rows' assumes both ways, every
cross-subject citation matches calendar.csv, and the checks avoid every core check week. The biggest risk is the
assessment design: the check-table minutes do not fit a 25-minute session for a class of 30, and both course-level
checks re-test the unit that has just ended (lesson 20), so a scope writer would build assessment days that cannot run
and checks that sample nothing new. The one change that matters most is to redraw the checks: spoken items in a circle
round, the fetch item at a short station, the mid-year check sampling unit 1 and the cycle, the year-end check sampling
units 1 to 3, with the just-ended unit's record reused unscored.

## Findings, most serious first

### 1. The check table does not fit the session (serious; LAYER frame; REPEAT new; confidence firm, arithmetic)

**What is wrong.** The Days bullet budgets about 3 minutes at each end of a 25-minute session, so about 19 working
minutes. Every end-of-unit assessment and both course-level checks run "at a check table in groups of four (about four
minutes a group)". The frame costs supplies for a class of 30: 8 groups of four at 4 minutes is 32 minutes, not 19. The
mid-year row says "a class of up to 24 in one session", but 6 groups at 4 minutes is 24 minutes, still over 19; one
session holds about 4 groups, 16 children. The four end-of-unit assessment days have no spill rule at all, and the
year-end check asks four tasks of each child in the same 4 minutes a group.

**Why it matters.** The scope writer will put each unit's assessment on one day it cannot hold, and the fixer below
cannot change days.csv. Half the class goes unchecked or the respond day is eaten, and the respond day's groups (from
the checklist) cannot be formed.

**Fix.** In the Evidence bullet and in each check row, state the per-child time and use forms that fit 19 minutes for
30 children: a spoken item (a wonder, a fact heard, one friend's addition) as a circle round, about 30 seconds a child,
the teacher marking the checklist as each child speaks (15 minutes); a fetch item (a book from a named bin, story or
fact) as a station of four children at a time, about 2 minutes a group (16 minutes), while the rest do the book-corner
task. Write the year-end check as two sessions with the items split between them and say which items fall on which day.
Correct "a class of up to 24" to the figure the new forms give.

### 2. Both course-level checks re-test the unit just ended (serious; LAYER frame; REPEAT yes, lesson 20, docs/reviews/frame-unit-lessons-2026-11-16.md; confidence firm)

**What is wrong.** Lesson 20: "a check right after a unit's end draws that unit's items from earlier units." The
mid-year check (week 13) comes straight after unit 2's end-of-unit assessment (week 11) and respond day (week 12) and
asks the unit 2 task again ("fetch a book from a named bin and say story book or fact book"). The year-end check (weeks
27 and 28) comes straight after unit 4 (end-of-unit assessment week 25) and asks the unit 4 task again. The frame's
reason (unit checklists are thrown away at unit end, so the check is "the term's one class record") is a records
problem, not a sampling reason.

**Why it matters.** A week-old re-test of the same move adds no evidence of retention and costs sessions in a 30-session
year. Grades 1 to 5 will copy it.

**Fix.** Mid-year check: a new-case wonder (unit 1) and the cycle (k-class-inquiry: point at the four pictures in order
and say one thing the class did at the find step), with unit 2's end-of-unit result reused unscored (keep that unit's
checklist until the mid-year check is done, then throw both away; that keeps the APPROACH.md rule's purpose, a record
held by the teacher only as long as it is used). Year-end check: units 1 to 3 on new cases (a wonder, a book from a
named bin, the answering fact), with unit 4's result reused unscored. Change both "What it checks" cells to name the
units sampled, the task forms and the record reused.

### 3. Two rows have no check anywhere in the year (moderate; LAYER frame; REPEAT new; confidence likely)

**What is wrong.** Unit 1's end-of-unit evidence checks k-wonder only; k-class-inquiry (the cycle as four pictures) is
never scored there or in either course-level check (the year-end respond day 2 look-back is unscored). Unit 2's
evidence checks k-picture-book-labels only; k-library-visit (book care, putting a book back, the stop rule) is never
checked. Bar part 11 item 2: each grade's priority skills, "each with a check".

**Why it matters.** An adoption reader tracing the seven rows to a check finds two with none; grade 1 assumes both
(g1-class-book, g1-device-stop-rule) with no evidence they landed.

**Fix.** Unit 1 evidence adds "points at the four pictured steps in order and names the step the class did today";
unit 2 evidence adds "puts the book back in its bin and says the three stop words with the picture cards". The
mid-year check in finding 2 samples k-class-inquiry again.

### 4. Unit 2 is short for what it owns (moderate; LAYER frame; REPEAT yes, lesson 9; confidence judgment call)

**What is wrong.** The Days bullet says units get the most days "where a unit introduces the cycle (unit 1) or carries
two rows and the year's last product (unit 4)". Unit 2 also carries two rows but has 5 days, of which 3 teach, and its
one show-me day carries book care, borrowing, the bin labels and the stop rule: four new routines for five-year-olds in
about 19 minutes, with the story-or-fact sort folded into the one practice day.

**Fix (weeks unchanged).** Unit 1 to 6 days, its share opening the respond day as unit 3 already does (show-me, practice,
show-me, inquiry find and draw, end-of-unit assessment, respond opening with the share circle and the self-check); unit 2
to 6 days (course days 7 to 12): show-me (care, borrowing, the stop rule), show-me (the bins, story or fact), practice,
inquiry, end-of-unit assessment, respond. Unit 2 still ends in week 12, so the mid-year check stays in week 13 and
nothing else moves. The Days bullet's load sentence then reads true.

### 5. Almost half the year is assessment and respond days (moderate; LAYER frame; REPEAT new; confidence judgment call)

**What is wrong.** Each unit spends 2 days on its end-of-unit assessment and respond day (8), and the course-level
checks take 6 more: 14 of 30 sessions, leaving 16 teaching sessions in a year. The year-end alone takes 4 sessions,
2 of them respond days, and the frame says the second respond day exists "so the course ends in week 30".

**Why it matters.** This is the pattern grades 1 to 5 copy. A 30-session course cannot afford it, and the lens's first
error ("a year of spaced units", taught on real work) is weakened when a unit has three teaching days.

**Fix.** With finding 2's narrower year-end check (three short items, no group turn), the year-end check fits one
session on finding 1's forms: make it 1 check day and 1 respond day, and turn the freed session and the look-back into
a closing inquiry day (the class wonder board looked back over, "what do I wonder about now?", which is the continuum's
own PK to 2 reflect priority). Days stay 30; teaching days rise to 18. If the lead keeps two year-end check days, say so
with the reason, not the week count.

### 6. The year-end check weeks clash with four after-core checks, unstated (minor; LAYER frame and process; REPEAT new; confidence firm)

**What is wrong.** The Placement paragraph shows the core weeks avoided (true: core K checks are weeks 14 to 17 and 29
to 32, and library's checks are weeks 13, 27 and 28; its respond days in weeks 14, 29 and 30 are allowed). But
`frame.py calendar` prints clashes in week 27 (computer science and health checks) and week 28 (ELD and physical
education). The after-core brief only forbids core weeks, so this is not a fail; but in K, weeks 26 to 28 already hold
the year-end checks of six after-core courses, and a K to 5 classroom teacher may teach several of them.

**Fix.** Add one line to Placement: "Week 27 also holds the computer science and health checks, week 28 the ELD and
physical education checks; the after-core rule allows this." Raise under For the lead whether after-core checks
should stagger among themselves in K to 5 (no clean year-end week exists in K after unit 4: every week from 26 to 32
already holds a check).

### 7. For the lead item 2 is stale (minor; LAYER process; REPEAT yes, stale notes; confidence firm)

**What is wrong.** It says "about one session every two weeks ... gives no weekly number it can read" and picks "teach
frame.py". scripts/frame.py already reads "one ... every two weeks" as 0.5 a week (lines 245 to 247, commented "library
6 to 8 and 9 to 12").

**Fix.** Rewrite item 2: "The band courses' time: frame.py reads 'about one session every two weeks' as half a session
a week, so the 6 to 8 and 9 to 12 frames keep the subject page's wording. They also need the brief's Year column (6, 7,
8; 9, 10, 11, 12) and 18 days a year (54 and 72)."

### 8. The sensitivity read's outside guidance is unnamed (minor; LAYER frame; REPEAT yes, lessons 12 and 23; confidence firm)

**What is wrong.** The Sensitivity reads bullet sends the agent to "a national children's online-safety body's guidance
for the early grades" and "guidance on children without a library card or books at home", with no title or link.

**Fix.** Name each by title with a free link on the teacher-facing frame, for example the National Center for Missing and
Exploited Children's NetSmartz K to 2 presentation ("Be Safer Online with NetSmartz: Grades K-2", listed at
https://www.missingkids.org/netsmartz/resources; its K to 2 rule is to tell a trusted adult when something online
makes you feel sad, scared or confused, which matches the stop rule). For the second, name one free source or drop the
clause and keep the frame's own borrowing rule. No name goes on a student page.

### 9. Bar part 11 item 1 lists six steps; the four pictures do not say where judge and use went (minor; LAYER frame; REPEAT new; confidence likely)

**What is wrong.** The bar and lens name ask, find, judge, use, share, reflect; the K cycle card is ask, find, share,
reflect (from the k-class-inquiry row). The frame never says how judge and use are met at K depth.

**Fix.** One sentence under The inquiry arc: "Judge, with help, is choosing the fact book over the story book at the
find step (unit 2's sort); use is drawing the found fact at the share step." Grades 1 and 2 then say when judge becomes
its own picture.

### 10. The L103 result places the story-or-fact sort in the K column; the band file has it in grade 1 (minor; LAYER progression; REPEAT new; confidence firm, checked at the band file)

**What is wrong.** For the lead item 10 says the story-or-fact sort matches the K sorting cell. In the PK to 2 band file
the K cell is sorting and categorizing objects and information; sorting books by fiction and nonfiction is the grade 1
cell (where g1-story-or-fact-book sits). The K "picture books can be true or not true" cell does match. One year early,
with help, is allowed (the lens names two or more grades as the error), and unit 2 scores it.

**Fix.** Add to item 9's row note for k-picture-book-labels: "The continuum puts sorting books by fiction and nonfiction
in grade 1; here it is done with help on a small pile and checked as story book or fact book, the K cell being that
picture books can be true or not true."

### 11. Unit 1's compelling question fits only its stand-alone case (minor; LAYER frame; REPEAT yes, lesson 10; confidence likely)

**What is wrong.** The question names seeds; the suggested host is a push-pull wonder ("why did the ball stop?") in
science unit 1. A class running on the host cannot answer a seeds question.

**Fix (settled below).** Write the question as "What do we wonder about, and how can we find out?" with seeds named as
the stand-alone case, or keep seeds and drop the push-pull host for unit 1.

## Data checks

| Check | Result |
|---|---|
| Owned skills | All seven K rows placed once (k-wonder and k-class-inquiry unit 1; k-library-visit and k-picture-book-labels unit 2; k-listen-and-retell unit 3; k-talk-in-group and k-who-made-book unit 4). No grade 1 or later row taught; the "Out" lines name the later rows. Gate agrees |
| Standards in full | AASL.V.C.1, the only owned id, taught and checked alone in unit 1. The nine carried ids each named in What students learn with their owner row, every owner verified in library.csv (I.B.3 and I.C.1 grade 3; VI.A.1 grade 3; IV.A.2 grade 2; IV.B.1 grade 4; I.B.1 grade 4; III.D.1 and II.A.1 grade 3; VI.B.2 grade 2). Phrases match aasl-words.txt; no competency text |
| Units and reasons | Order holds: question, then book, then answer inside a book, then group share and maker. No skill or model used before it is taught |
| Days | 30 = 24 + 3 check + 3 respond; 30 sessions of 25 minutes, one a week, as APPROACH.md's K to 2 default. Unit 2 short for load (finding 4); assessment share heavy (finding 5) |
| Calendar | calendar.csv: units weeks 1 to 7, 8 to 12, 15 to 19, 20 to 26; checks week 13 and weeks 27 to 28; respond weeks 14, 29, 30; matches the frame. Core K check weeks (science 14, 29; social studies 15, 30; ELA 16, 32; math 17, 31) avoided. After-core clashes in 27 and 28 (finding 6) |
| Seams | Every K row hands on to the grade 1 row whose assumes names it; research-cycle model_out matches g1-class-book model_in |
| Cross-subject | Every citation matches calendar.csv: ELA K unit 1 days 1 to 34 weeks 1 to 7, unit 2 days 35 to 76, unit 3 days 80 to 118 weeks 16 to 24; science K unit 1 days 1 to 9, unit 2 days 10 to 19, unit 4 days 32 to 43 weeks 15 to 20; social studies K unit 1 days 1 to 10 weeks 1 to 5. The skills cited sit in those units. Each lean has an "if later" line |
| Source map | Not applicable: no base text |
| Stale notes | stale.py passes; For the lead item 2 stale (finding 7); item 11 (3 to 5 band file not in the store) holds, checked against the store's README |

## Lens checklist (course frame layer)

| Line | State |
|---|---|
| A year of spaced units, not a one-off week | Met: four units over 30 weeks |
| Named priority skills per grade, none owned twice at one depth, none two or more grades early | Met (one year early on the sort, finding 10) |
| Lateral reading ownership line with social studies | Not applicable in K |
| An inquiry cycle every year | Met, with the six-step mapping unstated (finding 9) |
| Host task from another course per unit | Met: a named row and course days per unit, plus a stand-alone host |
| Source judging not a page checklist | Not applicable in K |
| A citation unit has research to cite | Met: unit 4's maker naming sits on found facts |
| End-of-unit evidence is a move done, not recall of terms | Met in form; two rows unchecked (finding 3) |
| No AASL text copied, no alignment claim | Met |
| No paid database or library assumed; no product named | Met |

## Spot checks at source (facts named from memory)

| Fact in the frame | Checked | Holds? |
|---|---|---|
| The continuum hosted by Monroe One BOCES, page last updated 2019 | libguides.monroe.edu/ESIFC | Holds: Monroe #1 BOCES School Library System, "Last Updated: Oct 23, 2019". The page itself names no author (STANDARD.md already says so) |
| AASL National School Library Standards, second edition, six Shared Foundations | standards.aasl.org | Holds: the site presents the second edition; Inquire, Include, Collaborate, Curate, Explore, Engage; no edition year on the page, copyright 2026 in the footer |
| L103 K cells: ABC order of picture books, private information never shared online, own ideas against others' ideas, own strengths, guesses from a cover, one or two new ideas from background | The PK to 2 band file in the source store | All hold in the K column. The fiction or nonfiction book sort is the grade 1 cell (finding 10) |
| A national online-safety body's early-grades guidance | missingkids.org NetSmartz resources (search) | A K to 2 presentation is listed; the frame should name it (finding 8). Its full kit was not opened |

## What the other library frames should copy, and what not

**Copy:** the Day kinds bullet in library's words; one full cycle a unit with a stand-alone host question beside a
named host row; a five-minute opening retrieval from the unit before; the skill card withdrawn on the first inquiry
day; carried ids named in What students learn with the owner row and grade, Owned standards left empty where the rows
carry only (`~`); the "Out:" line in each unit; the cross-subject table with each frame's course days and an "if
later" line, and the lesson 32 line that a core course never assumes library; the L103 cell-by-cell record against the
band file; per-unit tools, what Curio Class writes, and a cost for a class of 30; the neutral case sets and the
checklist rule (no per-child record passed on).

**Do not copy:** the check-table minutes (finding 1); course-level checks that re-test the unit just ended (finding 2);
a unit whose rows have no check (finding 3); 5-day units carrying two rows (finding 4); two year-end check days plus two
respond days to fill the weeks (finding 5); a Placement paragraph that names only the core weeks (finding 6). For grade
2, For the lead item 3 is right that its year-end check must sit by week 27 (core grade 2 science is week 28).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Spoken check items as a circle round at about 30 seconds a child; the fetch item as a station of four at about 2 minutes a group | Fits 19 working minutes for 30 children | docs/courses/library-and-research-skills-kindergarten/frame.md (Evidence bullet, Course-level checks) |
| Mid-year check items: a new-case wonder and the four-picture cycle; unit 2's result reused unscored | Lesson 20; gives k-class-inquiry a check | same, Course-level checks row 1 |
| Year-end check items: units 1 to 3 on new cases; unit 4's result reused unscored | Lesson 20 | same, Course-level checks row 2 |
| Unit 1's compelling question made topic-open, seeds named as the stand-alone case | Answerable on the host or the stand-alone | same, Units row 1 |
| Unit 1 and unit 2 end-of-unit evidence each gain the second row's item (finding 3) | Each row gets a check | same, Units rows 1 and 2 |

The day moves in findings 4 and 5 shift days between units and checks; they are recommended to the lead, not settled
here.

## For Cory

None. Every finding is inside the settled scope, dose and audience. The after-core stagger question (finding 6) is a
calendar rule for the lead.

## What this read could not judge

- Whether a classroom teacher is in the room while a librarian runs the check table; the station design in finding 1
  assumes the other children can do a book-corner task with light supervision. The subject page should say who teaches.
- The grade 1 library frame does not exist yet, so the seam was read against the grade 1 rows only.
- The NetSmartz K to 2 kit's full content was not opened.

## Sources

- https://libguides.monroe.edu/ESIFC: host, update date of the continuum.
- https://standards.aasl.org/: second edition and the six Shared Foundations.
- https://www.missingkids.org/netsmartz/resources: the K to 2 online-safety presentation for finding 8 (found by search; listing only).
- S:\CurioClass-sources\library\aasl-2026-11-21\esifc-pk-2\esifc-priority-pk-2.docx: K and grade 1 cells, read as text.

## For the source list

- NCMEC NetSmartz resources page, https://www.missingkids.org/netsmartz/resources: free K to 2 online-safety
  presentation ("Be Safer Online with NetSmartz: Grades K-2"); not yet in docs/APPROACH-SOURCES.md.

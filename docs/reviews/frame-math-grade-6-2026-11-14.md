# Frame read: math-grade-6 (Math Grade 6), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/RUBRIC-MATH-K8.md, docs/pipeline/briefs/frame-write.md
  (the "Lessons from the social studies frames" list).
- The frame docs/courses/math-grade-6/frame.md (all of it) and its row in data/plans/frames.csv (8 units, 160 days).
  data/plans/math-grade-6/source-map.csv does not exist yet; it comes with the scope and sequence.
- The grade 6 rows of data/progressions/math.csv and the grade 5 and 7 rows they meet; the frames before and after,
  docs/courses/math-grade-5/frame.md ("Handed on") and docs/courses/math-grade-7/frame.md ("Picked up").
- The base text in S:\CurioClass-sources\illustrative-math\grade-6: every unit overview and all 147 lesson pages
  (titles, optional marks, the "Addressing" standards of each activity), the prep page of 6.1.19, the IM 6 to 8
  pacing guide and dependency chart (the unit-level images), and the IM middle school teacher guide (about.md:
  each lesson fits a period of at least 45 minutes).
- data/standards/ccss-math-standards.txt and ccss-math-focus.csv (grade 6 clusters).
- The same-year frames the course leans on: docs/courses/science-grade-6/frame.md, the social studies 6 frames
  (world-geography-and-ancient-civilizations-i) and docs/courses/english-language-arts-grade-6/frame.md.
- Earlier reads: docs/reviews/frame-math-kindergarten-2026-11-14.md, the grade 2, 3 and 5 math frame reads,
  progression-math-*2026-11-13.md and progression-cross-2026-11-13.md ("For the course frames"). No earlier read of
  this frame exists.
- Gates: `plan.py check` exits 0; `frame.py check math-grade-6` 0 failures (8 units, 160 days, 154 in units, 6 for
  checks and respond days); `stale.py check` 0 failures (54 files).

## Verdict

The frame is sound: IM's unit order is kept, all 47 owned grade 6 codes sit in exactly one unit, every one of IM's
147 lessons is placed or cut with a reason, and the days add up (131 IM days plus 23 Curio Class days in units, plus
6 course-level days). The most serious problem is one cut: 6.1.19 "Designing a Tent" is not optional in IM, it is
the unit's culminating modelling lesson and the only place 6.G.A.1 and 6.G.A.4 are applied to a real problem, as both
standards require. The rest are smaller: Curio Class day composition that does not match the stated rule, cross-
subject rows written against guesses where science 6 now gives days, and a few pointers and clauses to fix.

## Findings, most serious first

### 1. 6.1.19 "Designing a Tent" is cut as if optional, but IM does not mark it optional (moderate; firm)

**What is wrong.** The source map cuts 6.1.19 as "Application lesson; an extension candidate for unit 1". IM's pacing
guide lists the grade 6 optional lessons as 6.1.16, 6.3.2, 6.5.2, 6.5.15, 6.6.11, 6.6.18 and all of 6.9; 6.1.19 is
not among them, and its prep page calls it the culminating lesson of the unit. It is IM's MP4 modelling day for unit
1, and the only day in the unit where 6.G.A.1 and 6.G.A.4 meet their last clause, "apply these techniques in the
context of solving real-world and mathematical problems". Unit 1's practices are MP7 and MP3 only.
**Why it matters.** Standards in full: without it the application half of two standards rests on practice problems.
EdReports gateway 2 also reads application and MP4 by unit; cutting a base text's only modelling day in a unit costs
evidence the frame does not get back elsewhere.
**Fix (frame, source map and unit 1).** Change the 6.1 row to "19 Designing a Tent | 1 | keep | Culminating
application of 6.G.A.1 and 6.G.A.4 (MP4)". Unit 1 becomes 18 days (16 IM + 2 ours). Fund the day from unit 8:
"6.8 | 1 to 2 | 8 | merge | Got Data? opens lesson 2's statistical questions in one day" (unit 8 becomes 16). Add MP4
to unit 1's practices. Major share is unchanged (both units are supporting or additional). If the frame prefers to
keep the cut, the reason must say IM does not mark it optional and name where the real-world application of both
standards is met. LAYER base text. REPEAT new.

### 2. The Curio Class days do not follow the frame's own rule (minor; firm)

**What is wrong.** "The course in brief" says the major-work units get "a mid-unit check, its respond day and
mixed-practice days". No unit's count includes a mixed-practice day. Units 3, 4 and 7 each have 3 Curio Class days;
unit 3's are named (mid-unit check, assessment, respond), units 4 and 7 are not, and unit 4 is major work with a mid-
unit check implied but no respond day.
**Why it matters.** Lesson 9 (days by load) and lesson 1 (a respond day after each check): a writer cannot tell what
the 3 days are, and a mid-unit check with no respond day breaks the rule the frame states.
**Fix (frame, course in brief and source map).** Replace "and mixed-practice days" with "and, where days allow, one
mixed-practice day". Name the Curio Class days in each source-map unit row, as unit 3's row does. For the 3-day units
use the pick settled below. LAYER frame. REPEAT yes (days by load).

### 3. Cross-subject rows and "For the lead" items 5 and 6 are written against guesses; science 6 now gives the days (minor; firm)

**What is wrong.** Science 6's frame is written: its base unit 6.4 runs days 93 to 116, base unit 6.5 (hazards,
histograms) days 117 to 136. This frame still says science 6.4 "should come after about day 50" (it does), calls the
histogram lean "Probably later" (it is later: math histograms days 145 to 148), and item 5 reasons that a unit 7 and 8
swap "would still not reach science's base unit 6.5", with a reopen trigger of "after day 120". With the swap, data
would start about day 120 and histograms fall about days 123 to 128, inside science's days 117 to 136, so that reason
no longer holds. ELA 6's short research (W.6.7) falls in its unit 3, early, so the "if ELA's research comes later" line
does not apply; ELA 6's display lean has its own bridge in its unit 6 (days 137 to 156).
**Why it matters.** The availability calendar is what the other frames honour; a reason that the real days contradict
invites a later reader to reopen the order for the wrong reason.
**Fix (frame, Cross-subject and For the lead).** Science 6.4 rows: "Available: science base unit 6.4 is days 93 to
116." Hazard row: "Later: science base unit 6.5 is days 117 to 136; science's bridge (a supplied histogram read, no
student builds one) applies." ELA rows: "Available: ELA 6 research is its unit 3." Item 6: closed. Item 5: "Pick: keep
IM's order. A swap would bring histograms to about days 123 to 128, inside science's base unit 6.5, but would end the
year on supporting work and leave rational numbers (major) after data; both frames carry a bridge, so the order
stands." LAYER process. REPEAT yes (lesson 15; the kindergarten read found the same).

### 4. Unit 1 claims a "first use" that grades 3 and 4 already made (minor; firm)

**What is wrong.** Unit 1's reason calls its formula work "the first use of letters standing for numbers that unit 6
names". 3.OA.D.8 and 4.OA.A.3 already represent problems "using equations with a letter standing for the unknown
quantity".
**Why it matters.** Lesson 6: "first" claims are checked. A writer would treat letters as new and slow down where
students should be reminded.
**Fix (frame, unit 1).** "the first use this year of letters in formulas, which unit 6 names as variables". LAYER
frame. REPEAT yes (lesson 6).

### 5. Two clauses of owned standards are not named (minor; firm)

**What is wrong.** 6.EE.B.6's second clause, "understand that a variable can represent an unknown number, or,
depending on the purpose at hand, any number in a specified set", is not in unit 6's "What students learn" (IM 6.7.8
to 10, the inequality lessons, carry it with solution sets). 6.G.A.3's "use coordinates to find the length of a side
joining points with the same first coordinate or the same second coordinate" is not named in unit 7 (IM 6.7.15 and
19 teach it).
**Why it matters.** Lesson 4: standards in full. The unit writer works from the text, not from the codes.
**Fix (frame, units 6 and 7).** Unit 6 add: "a variable as any number in a set, met again with inequalities in unit 7
(6.EE.B.6 in full)". Unit 7 add: "polygons on the coordinate plane, finding the length of a horizontal or vertical side
from its coordinates (6.G.A.3 in full)". LAYER standard. REPEAT yes (the kindergarten read found the same).

### 6. Progression pointers do not match IM's lessons (minor; firm)

**What is wrong.** Row notes in data/progressions/math.csv, which the frame cites: m6-order-absolute-value says IM 6.7
lessons 4 to 8 (the lessons are 3 to 7); m6-inequalities says 9 to 10 (8 to 10); m6-four-quadrants says 11 to 15 (11 to
15 and 19); m6-summarize-data names IM 6.9, which this frame cuts (the summarizing is in IM 6.8.17 and 18).
**Why it matters.** Lesson 7 (both ends): the scope and sequence will map days from these pointers.
**Fix (frame, For the lead).** Add an item: "Progression row notes to correct: m6-order-absolute-value IM 6.7 lessons
3 to 7; m6-inequalities 8 to 10; m6-four-quadrants 11 to 15 and 19; m6-summarize-data IM 6.8 lessons 17 to 18 (IM 6.9
is left out). The progression fixer edits math.csv." LAYER progression. REPEAT yes.

### 7. The focus line hides that the strict unit count is under the line (minor; firm)

**What is wrong.** "Major work" gives 65 percent strictly by days and 77 percent with connected supporting work, and
"5 of 8" units strictly: that is 62.5 percent, under the 65 percent line, and the frame does not say so. My own count
from IM's "Addressing" tags: 97 of 137 kept lessons (71 percent) have at least one activity on a grade 6 major
cluster; 57 percent if every activity must be major.
**Why it matters.** EdReports indicator 1e reads all three counts (units, lessons, time) and counts supporting work
that is connected to major work on the major side; a reviewer at 60 to 64 percent on one count looks closer.
**Fix (frame, course in brief and For the lead item 2).** "By units: 5 of 8 strictly (62.5 percent), 6 of 8 with unit
1. By lessons, from IM's own tags: 97 of 137 kept lessons touch major work (71 percent). The evidence guide counts
connected supporting work (indicator 1e), so the counts with unit 1 are the ones a reviewer reads." Close item 2 as
settled below. LAYER frame. REPEAT yes (the kindergarten read made the same counting point).

## Lens checklist, course frame layer

| Line | Result |
|---|---|
| Major work under the line, by units, days or time | Met on the guide's rule: 77 percent of days and 6 of 8 units with connected supporting work; 71 percent of kept lessons by IM's tags. Strict by units is 62.5 percent (finding 7); strict by days is 65 percent, exactly on the line, so do not add more supporting days (finding 1 is funded from unit 8 for that reason) |
| A supporting cluster that does not practise major work | Met. Unit 1's area formulas evaluate expressions (6.EE.A.2c); unit 4's prism volume uses fraction multiplication and division; unit 8 uses ratio and the number line |
| A source-map row with no keep, split, merge, cut or ours decision | Met; one cut has a wrong reason (finding 1) |
| A skill owned by two grades at the same depth, a handoff that skips a grade | None found. Grade 5's hand-ons are all picked up; grade 7's "Picked up" table matches this frame's hand-ons |
| A model used before the grade that builds it | None. Double number lines start in unit 2; the four-quadrant plane in unit 7 |
| A limit broken | None. Signed numbers are ordered and placed, not operated on (grade 7); no MAD before unit 8 |

## The brief's other checks

- **Owned skills:** all grade 6 rows placed once (my placement script and the gate agree); all 47 codes owned.
  6.EE.A.1 and 6.EE.A.2c also appear begun elsewhere (unit 1 formulas), named as such.
- **Standards in full:** two clauses unnamed (finding 5); 6.G.A.1 and 6.G.A.4's application clause lost with the cut
  (finding 1); the rest are named in full.
- **Units and reasons:** IM order kept; IM's dependency chart (6.1 to 6.4, 6.2 to 6.3 and 6.6, 6.4 to 6.5, 6.5 to 6.6,
  6.6 to 6.7; 6.8 free) is respected. One "first" claim is wrong (finding 4).
- **Days:** units 17, 21, 20, 20, 14, 23, 22, 17 = 154, plus 6 = 160; each unit's IM days match the pacing guide's
  range less merges and optional cuts. 50 minutes is IM's 45-minute lesson plus 5 minutes of spaced practice (IM
  teacher guide). No unit is far over or under its load.
- **Source map:** 147 lessons, all accounted for; every optional cut matches IM's list; one non-optional cut (finding
  1). No NC or reference source is mapped.
- **Seams:** grade 5's "Handed on" table is picked up row for row; grade 7 picks up every hand-on.
- **Cross-subject:** social studies 6 matches (timeline days 1 to 10, maps days 26 to 39, both before unit 7); science
  and ELA rows are finding 3. Each lean carries an "if later" line.
- **Lessons from the social studies frames:** 1 (respond days) finding 2; 2 (Candidate) met; 3 (time a day) met; 4
  (standards in full) finding 5; 5 (threads start where used) met; 6 ("first" claims) finding 4; 7 (both ends)
  finding 6; 8 ("if later" lines) met; 9 (days by load) finding 2; 10 (answerable questions) met; 11 (picks) met; 12
  (sensitivity reads line) met; 13 (no math ahead of math) met; 14 (paper path, no accounts) met; 15 (status lines)
  finding 3.

## What is right and should not be touched

- IM's order kept, with the dependency chart cited for every edge.
- Optional lessons kept where they carry a standard (6.3.2 for conversions, 6.6.11 for factoring, 6.6.18 for 6.EE.C.9),
  each with its reason.
- The drop of the NSPFE "Earning Income" tag (For the lead item 4): no grade 6 math row owns a personal finance
  standard.
- The negative-numbers unit's no-year-zero rule against the social studies timeline.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Keep 6.1.19 Designing a Tent; merge 6.8.1 with 6.8.2 to fund it | Not optional in IM; the unit's only application and MP4 day; unit 8's first two lessons share one aim | docs/courses/math-grade-6/frame.md, source map, units 1 and 8 |
| In a unit with 3 Curio Class days: assessment, its respond day and one mid-unit check whose respond work runs in the 5-minute openings of the next two lessons | Keeps a respond step after each check without taking an IM day | frame.md, source map rows 6.3, 6.4, 6.7 |
| Major work is counted the guide's way: connected supporting work counts; frames report the strict count beside it | EdReports evidence guide, indicator 1e | frame.md, course in brief and For the lead item 2 |
| Keep IM's order for units 7 and 8 | Ends on major work; both frames carry a histogram bridge | frame.md, For the lead item 5 |

## For Cory

None. Nothing here changes scope, money, people or audience.

## What I could not judge

Whether science 6's hazard unit needs students to build a histogram or only read one; its frame says read, and I
took it at its word.

## Sources

- IM K-12 Math 1st edition, grade 6, local copy (S:\CurioClass-sources\illustrative-math\grade-6, CC BY 4.0): lesson
  lists, optional marks, Addressing tags, prep page of 6.1.19, the 6 to 8 pacing guide and dependency chart, the
  middle school teacher guide (about.md).
- EdReports Math K-8 Evidence Guide v2.0, indicator 1e,
  https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf (three counts; connected supporting
  work counts), as read in the kindergarten frame read. Read, not copied.
- Student Achievement Partners focus documents via data/standards/ccss-math-focus.csv: cluster weights.
- CCSS text via data/standards/ccss-math-standards.txt.
- Confidence: findings 1 to 7 firm (each rests on IM's own pages, the standard's text or another frame's own table).
  The unit 7 and 8 order pick is a judgment call.

## For the source list

None new.

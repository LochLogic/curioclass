# Baseline 1: ELA subject column (subject=ela), 2026-11-14

Reader: the curriculum expert, part A (one subject column). Brief: docs/pipeline/briefs/baseline-1.md. Bar:
docs/RUBRIC-ELA.md and docs/agents/lenses/ela.md.

## What I read

- AGENTS.md, docs/pipeline/briefs/baseline-1.md, docs/pipeline/briefs/frame-write.md (format and lessons), the ELA
  lens, docs/RUBRIC-ELA.md (the writing-share line and Gateway 2).
- All 13 ELA frames, docs/courses/english-language-arts-kindergarten and -grade-1 to -grade-12 (frame.md): each
  brief, the Units table (topic, question, days, skills, anchors where the finding rests on them), the course-level
  checks, For the lead, and the Seams lines on texts not repeated.
- data/progressions/ela.csv (374 rows): every standard thread traced K to 12 by skill id, and the models K to 12.
- The band reads and fix reports, searched for each finding below before it was kept (frame-english-language-arts-*,
  frame-ela-*-fixes, the grade 6 reconcile, progression-ela-*, frame-cross-subject-2026-11-14.md).
- `python -X utf8 scripts/plan.py check`: 0 failures on every frame. Placement, owned standards and day totals are
  not repeated here.

## Verdict

The ELA column holds together as a K to 12 climb: every standard thread runs unbroken from kindergarten to grade 12
in the progression, each grade reads a long text whole, research and process writing recur every year, and the K to
5 frames use the base text in one consistent way. What no band read could see is in the seams between bands: the
grade 5 to 6 step goes backwards on long-text length, typed pages and process pieces; the Declaration's four
readings collapse into the same "who answered it, who it includes" lens in grades 8, 10 and 12; and grades 5 to 7
spend almost half their unit days on water, drought and storms, with two near-identical drought-ranch family stories.
None is a rebuild; each is a cell or a line in one or two frames. 10 findings.

## Findings, most serious first

### 1. The Declaration's "four lenses" are really two, read three times (grades 8, 10, 12)

- **Layer:** frame. **Repeat:** yes, deepened (the grade 9-10 read named the four readings and accepted the lenses;
  it did not test them against each other).
- **Files and rows.** english-language-arts-grade-10/frame.md line 101 ("each with a different lens (the founding
  thread; who liberty includes; its reasoning, RI.11-12.8; documents that answer it, Walker's Appeal in grade 12)");
  grade 8 unit 2 (line 138: "When the founders wrote that all men are created equal, who answered them, and what did
  they say?"); grade 10 unit 6 (line 137: "Liberty and who it includes ... Who did each document say liberty
  belonged to"); grade 12 unit 4 title (line 118: "the American dream and who it includes ... who is shut out?");
  grade 12 unit 7 (line 121, Walker's Appeal against the Declaration).
- **What is wrong.** Grade 8 already reads the Declaration through the people who answered it (Banneker, the 1793
  volunteers). Grade 10's "who liberty includes" is the same question in other words, on the same kind of set (later
  voices answering the founding promise). Grade 12 again reads "documents that answer it" (Walker). Only grade 11's
  lens (its reasoning, RI.11-12.8) and grade 12's court reading are new. The line that justifies the repeat names
  four lenses, but grade 8's is not "the founding thread": it is "who answered". Across grades 4, 7, 8, 10 and 12
  six compelling questions end on "who was left out / included / shut out / answered".
- **Why it matters.** The lens names a reading skill that "climbs nowhere: the same task at the same text demand in
  two grades". A student meets the same frame for the same document three times in five years.
- **Fix.** Give grade 10 the lens its own owned rows already ask for, RI.9-10.9's "related themes and concepts" and
  RI.9-10.4's cumulative word meaning (e10-ri-word-choice is owned in the same unit). Texts unchanged.
  - Grade 10 line 137, unit cell: "**Liberty and who it includes, 1776 to 1941**" becomes "**Liberty, word by word,
    1776 to 1941**"; the question "Who did each document say liberty belonged to, and what did each writer ask the
    country to change?" becomes "What did 'liberty' mean in each document, and how did each writer's words change
    what it means?"
  - Grade 10 line 101: replace the parenthesis with "(grade 8: who answered it; grade 10: what 'liberty' means, built
    word by word across documents; grade 11: its reasoning, RI.11-12.8; grade 12: how the courts have read it,
    unit 7, with Walker's Appeal as the one answering text)".
  - Grade 12 line 118, unit 4 title: "The 1920s: the American dream and who it includes" becomes "The 1920s: the
    American dream and its price"; the question becomes "What does the American dream cost the people who chase it
    in these 1920s texts, and who pays?" (the unit's texts and rows are unchanged).
  - Row e10-ri-seminal-documents notes: the fixer swaps "who liberty includes" for "what liberty means across the
    documents" if the phrase is there.

### 2. The grade 5 to 6 step goes backwards on three measures, and grade 7 repeats grade 6

- **Layer:** frame. **Repeat:** yes, partly (the grade 6 reconcile noted grade 5's 30,000 to 40,000 words and left
  "Grade 7 and 8 reconciles: check the band's long-text lengths"; no such check was done, and the typing and
  process-piece dips were not named).
- **Files and rows.**
  - Long text read whole: grade 5 unit 1 novel "about 30,000 to 40,000 words"; grade 6 unit 1 novella "about 15,000
    to 20,000 words"; grade 7 unit 1 "about 20,000 words"; grade 8 unit 1 "about 25,000 words". Grade 8, the band's
    end, still reads a shorter whole text than grade 5.
  - Typed pages: grade 5 ends at "two pages in a sitting" (grade 5 brief, Paper path); grade 6 line 61 "about one
    typed page in unit 1, two by unit 2, three in one sitting by unit 6"; grade 7 line 50 "about two pages in one
    sitting by unit 2, three by unit 6", the same end as grade 6.
  - Process pieces: grade 5 "Each unit takes at least one piece through the whole process" (4); grades 6 to 8
    "three pieces through the full writing process".
- **What is wrong.** Each thread steps down at the move from the 90-minute block to the 50-minute period, and no
  frame says the step down is on purpose. Grade 7's typing repeats grade 6's year and starts below it.
- **Why it matters.** The lens's staircase: demand climbs across the grades. The home reading the 6 to 8 frames add
  (20 minutes, four nights) is exactly what lets a longer whole text fit.
- **Fix.**
  - Grade 6 line 61: "about one typed page in unit 1, two by unit 2, three in one sitting by unit 6" becomes "two
    typed pages in unit 1 (grade 5's end, used as the readiness check), three in one sitting by unit 3 (W.6.6)".
  - Grade 7 line 50: "about two pages in one sitting by unit 2, three by unit 6" becomes "three pages in one sitting
    from unit 1 (grade 6's end), kept all year".
  - Long texts: grade 6 unit 1 "about 15,000 to 20,000 words" becomes "about 25,000 to 30,000 words"; grade 7 unit 1
    "about 20,000 words" becomes "about 30,000 to 35,000 words"; grade 8 unit 1 "about 25,000 words" becomes "about
    35,000 to 45,000 words". Home reading carries the extra pages; the commission cost is Cory's (For Cory).
  - Grade 6 brief, Writing calendar: add "Three process pieces, against grade 5's four: the 50-minute period gives
    fewer full-process cycles, and the six shorter pieces keep the year's writing volume; each process piece is
    longer than any in grade 5."

### 3. Grades 5 to 7: water and drought crowd the shelf, with the same story twice

- **Layer:** frame and progression (e7-reading-range, thread 2). **Repeat:** new (the band reads praised the
  grade 7 drought thread; none set it beside grade 5).
- **Files and rows.** Grade 5 unit 4 (line 163): "two original Curio Class survival stories ... one a girl's family
  keeping its farm through a dry year and one a boy's ranching family on a shrinking river", plus the Colorado
  River, "how should communities share it". Grade 7 unit 1 (line 132): "an original Curio Class novella ... on a
  present-day family cattle ranch in a drought year, told in alternating chapters by a brother and sister". Grade 7
  unit 2: the Dust Bowl (drought again). Grade 7 unit 6: "who should decide a river's future". Grade 5 unit 1 is also
  a farm family starting over.
- **What is wrong.** A ranch family in drought, told by children, is commissioned twice two years apart, and the
  "how should a river be shared" question returns in grade 7. Counting units on water, drought, floods and storms:
  grade 5 unit 4 (33 days), grade 6 units 1, 3, 5, 6 (100), grade 7 units 1, 2, 6 (78): 211 of 461 unit days in
  grades 5 to 7, about 46 percent, after grade 3's water unit and kindergarten's weather. The grade 3 and 5 frames
  record water as kept on purpose for grades 3, 5 and 6; grade 7 is not in that record.
- **Why it matters.** The lens: "Topic sets ... repeat the same topic at the same depth", and the year's texts
  should not lean to one kind. Thread 2 in grade 7 is "ecosystems, resources and human impact", which does not need
  two drought units back to back.
- **Fix.** Keep grade 7's thread 2 and the Dust Bowl; move unit 1's novella off drought onto the river the year
  closes on.
  - Grade 7 unit 1 (line 132): "Drought year on the ranch. 'When the rain does not come, what does a family hold on
    to, and what do they let go?'" becomes "The salmon year. 'When the river a family has fished for generations
    changes, what do they hold on to, and what do they let go?'"; the novella becomes "a present-day family that
    fishes the Klamath River in the last year before its dams come down, told in alternating chapters by a brother
    and sister, 13 and 15"; the paired drought maps and pages become federal fish and river-flow pages (the
    National Oceanic and Atmospheric Administration's fisheries pages, federal works). Unit 6 then reads the same
    river's argument with the knowledge unit 1 built. The fixer edits e7-reading-range's thread 2 sentence ("drought
    in unit 1" becomes "a river family in unit 1") and the Karuk and Yurok reader line moves to cover unit 1.
  - Grade 5 For the lead 4: add "Grade 7 reads the Dust Bowl (drought in history) and the Klamath
    (a river's ecosystem), not a family drought story; grade 5's ranch-family story is the only one."

### 4. Gene editing is taught from the same federal pages in grades 8 and 10

- **Layer:** frame. **Repeat:** new.
- **Files and rows.** Grade 8 unit 5 (line 141): National Human Genome Research Institute and Food and Drug
  Administration pages "on genes, traits and gene editing" and engineered foods. Grade 10 unit 2 (line 133): the same
  two agencies' cloning pages and "an original Curio Class essay of 2,000 to 3,000 words on gene editing". Grade 10's
  "Texts not repeated" line (101) does not name it.
- **What is wrong.** Two years apart, the same topic from the same sources; grade 10's original essay is a commission
  on grade 8's topic.
- **Why it matters.** Topic sets should connect, not repeat at near depth; and it costs a commission.
- **Fix.** Grade 10 line 133: "an original Curio Class essay of 2,000 to 3,000 words on gene editing" becomes "an
  original Curio Class essay of 2,000 to 3,000 words on growing tissues and organs in the lab, and what it means to
  'make' living things". Grade 10 line 101: add "gene editing in the news is grade 8's (unit 5); grade 10 reads
  cloning and lab-grown tissue." The For the lead 8 phrase "unit 2's gene-editing essay" becomes "unit 2's
  lab-grown tissue essay".

### 5. Literary analysis is counted as informative in grade 8 and as argument in grade 10, on a rubric line that says neither

- **Layer:** frame and the bar (RUBRIC-ELA.md). **Repeat:** new (the grade 8 read asked for the count and cited the
  rubric; the citation does not hold).
- **Files and rows.** Grade 8 line 54: "unit 1 analytical essay through the process, counted as informative as
  RUBRIC-ELA files literary analysis". docs/RUBRIC-ELA.md line 32 gives only "About 35 percent argument, 35
  informative, 30 narrative writing (2o)"; it files literary analysis nowhere. Grade 10 brief, Writing calendar:
  "argument 3 (the analytic essay counted as argument from text)".
- **What is wrong.** The same kind of piece is counted under two types two years apart, and grade 8 cites a rule
  that does not exist. The grades 6 to 12 shares cannot be compared across the column.
- **Why it matters.** The lens checks "The writing types ... are not balanced across the grades"; the count is the
  only evidence of balance.
- **Fix.** One rule, by the standard the piece is taught on. RUBRIC-ELA.md line 32, after "Grades 3 to 5: 30, 35,
  35." add: "A piece counts under the writing standard its unit teaches it on (W.1 argument, W.2 informative, W.3
  narrative); a literary analysis taught on W.9 alone counts as argument when it defends a claim about the text."
  (RUBRIC-ELA.md is a shared doc; Cory owns the bar's wording, the expert recommends it.) Grade 8 line 54: "counted
  as informative as RUBRIC-ELA files literary analysis" becomes "counted as informative, since unit 1 teaches it on
  W.8.2". Grade 10 stands as written and adds "(taught on W.9-10.9, defending a claim)".

### 6. The 6 to 8 checks follow two rules for end-of-unit tests and two for spacing

- **Layer:** frame. **Repeat:** yes for grade 6 (the grade 6 reconcile adopted "no class tested twice in a week");
  new across the band.
- **Files and rows.** Grade 6 line 172 on: "For units 2, 4 and 6 the course-level check that follows is the unit's
  end-of-unit assessment ... so no class is tested twice in a week". Grade 7 line 147 and grade 8 line 151: "Each
  unit also ends in its own end-of-unit assessment on a cold text, inside the unit's days", with a check right
  after units 2, 4, 6 (grade 7) and 3, 4, 5 (grade 8). Grade 7 line 147 also sets a spacing rule ("no stretch runs
  longer than 48 unit days without a course check"); grade 8's check 1 falls after 88 unit days.
- **What is wrong.** Three neighbouring years of the same band, written to one brief, test differently: grades 7 and
  8 test twice in a week three times a year, which grade 6 rejects for a stated reason.
- **Why it matters.** A scope and sequence writer for 7 and 8 inherits a doubled test week grade 6 ruled out, and a
  teacher moving between grades meets two systems.
- **Fix.** Adopt grade 6's rule in 7 and 8. Grade 7 line 147 and grade 8 line 151: replace "Each unit also ends in
  its own end-of-unit assessment on a cold text, inside the unit's days." with "Units not followed by a check end in
  their own end-of-unit assessment on a cold text, inside the unit's days; where a check follows a unit, the check is
  that unit's end-of-unit assessment, its informational text on the unit's topic but never a text the unit read, so
  no class is tested twice in a week." Spacing: grade 8 keeps check 1 after unit 3 (RI.8.2 is owned there) and adds
  to line 151 "Check 1 waits for unit 3, which owns RI.8.2; units 1 and 2 end in their own assessments." Grade 7's
  48-day sentence stays as grade 7's reason, not a band rule.

### 7. The grade 6 and grade 7 year-end argument items are word for word the same

- **Layer:** frame. **Repeat:** new.
- **Files and rows.** Grade 6 line 170, check 3: "a one-sitting argument from a small cold source set (W.6.1)".
  Grade 7 line 145, check 3: "a one-sitting argument from a small cold source set (W.7.1)". Grade 8 check 2 adds "with
  a counterclaim".
- **What is wrong.** The year-end item names no grade 7 step. W.7.1a adds acknowledging alternate or opposing
  claims; W.7.1b adds credible sources. The checks do not show the build the brief asks for ("what a grade 5 end
  check asks against grade 4").
- **Fix.** Grade 7 line 145: "a one-sitting argument from a small cold source set (W.7.1)" becomes "a one-sitting
  argument from a small cold source set that acknowledges an opposing claim and cites credible sources (W.7.1a,
  b)". Grade 6 line 170: add "with a claim, clear reasons and relevant evidence (W.6.1a, b)".

### 8. The start-of-year screens take 2 days in grade 3, 1 in grade 4 and none in grade 5

- **Layer:** base text. **Repeat:** new.
- **Files and rows.** Grade 3 brief, Days: "unit 1 adds 2 for the start-of-year screens". Grade 4: "unit 1 adds 1
  for the start-of-year screens". Grade 5: modules 1 to 3 "lesson for lesson (41, 39 and 40 days)", no screen day,
  yet line 172 says "The fall oral reading check and long-word screen sit inside unit 1."
- **What is wrong.** The same screens (oral reading, long-word, a writing sample) cost three different amounts in
  three neighbouring years, and grade 5 does not say where its screen time comes from, so a module 1 lesson is
  quietly shortened.
- **Fix.** Grade 5 brief, Days, after "with no days added": add "The fall oral reading check and long-word screen
  run one to one in the skills block's independent-reading minutes of weeks 1 and 2; the writing sample is unit 1's
  first exit answer, so no unit day is added (grade 3 adds two days as the first year of the long-word sequence and
  the 3 to 5 block, grade 4 one for the writing sample)." Grade 3 and grade 4's Days bullets add the same reason
  in a clause.

### 9. The size of a word list is stated two ways, and the rate falls by about two thirds from grade 6 to 9

- **Layer:** frame. **Repeat:** new.
- **Files and rows.** Grade 6 line 54: "about 8 to 10 words a week". Grade 9 line 12 and grade 10 line 12: "a unit
  word list of 10 to 15 words"; grades 11 and 12: "about 15 words" a unit, with units of 10 to 36 days. Grades 3 to 5,
  7 and 8: "The unit's word list", no size.
- **What is wrong.** At 8 to 10 a week grade 6 meets about 2 words a day; a 28-day grade 9 or 10 unit with 10 to 15
  words meets about 0.5. The vocabulary thread (L.6, e6-technical-words to e12-academic-words) climbs in demand while
  its volume drops, and five frames say nothing.
- **Fix.** One stated rate, in every frame 3 to 12: "about 8 to 10 words a week from the unit's texts, met before,
  during and after reading, plus the student's own word log from grade 9". Grades 9 and 10 line 12 and grades 11 and
  12's routines bullet: "a unit word list of 10 to 15 words" / "about 15 words" become that text. Grades 3 to 5, 7, 8:
  add it to the brief. The scope and sequence sets each list.

### 10. Grade 6's fluency screen flags students no later grade looks at again

- **Layer:** frame. **Repeat:** new. Minor.
- **Files and rows.** Grade 6 line 68: a one-minute oral reading check "flags any student below about 112 words
  correct a minute for a closer look; once a week partners reread". Grades 7 and 8: no fluency line at all. Grade 9
  check 3 asks "a short recorded or live reading aloud of a passage".
- **What is wrong.** A grade 6 student flagged in the fall has no fall check in grade 7, and grade 9 assesses oral
  reading the column stopped teaching after grade 6.
- **Fix.** Grades 7 and 8 brief: add "**Fluency.** In the first two weeks the teacher repeats the one-minute oral
  reading check for students flagged the year before and any new student; partners reread a short anchor passage
  once a week. No rate is shown to students; Curio Class is not a reading intervention."

## Settled by the expert

| Question | Settled | Why |
|---|---|---|
| Thread ids change style across the column (plain in K to 8, e9-rl-/e10-ri- in 9 and 10, e11-lit-/info- in 11 and 12) | Keep the ids | Internal ids stay stable; continuity is carried by assumes and hands_on, which run unbroken for every standard K to 12 (traced) |
| Learning to read under slavery in grade 3 (Booker T. Washington) and grade 11 (Douglass) | Keep both | Grade 3 is a short selection for questions; grade 11 reads the Narrative whole for rhetoric and ideas; a deliberate echo at a different depth |
| The Gettysburg Address in grades 9 and 12 | Keep | Said on purpose in grade 9 line 99 and grade 12 unit 7 (a new task, RI.11-12.9) |
| Spread of peoples and places K to 12 | Fair; no change | Africa (Kenya, Nigeria, South Africa), Asia (China, Korea, India, the Philippines, Japanese American), Native nations in at least eight grades, Europe, Latin America (Puerto Rico, Quechua, Mexico, Brazil, Mexican American); Latin America is thin in 6 to 12, which the public-domain rule for 9 to 12 explains |
| 9 to 12 anchors published 1930 or earlier | Cory's rule; no change | Recent texts enter as quoted passages and US government works |
| Day length 120 (K to 2), 90 (3 to 5), 50 (6 to 12) | Kept; already with Cory | Each frame states it; finding 2 deals with what the 90 to 50 step drops |
| Units a course: 4 in K to 5, then 6, 6, 5, 8, 7, 9, 8 | Kept | K to 5 follow the base modules; each 6 to 12 frame weighs units by load and says why |
| Two course checks in K to 5, three in 6 to 12; grade 12 has 11 check days | Kept | Reasons given (base text; grade 12's research unit) |
| Year-end opinion and argument climb K to 5 (familiar text, then cold texts, then an essay from several accounts) | Builds; no change | Read across the check tables |
| story-map ends in grade 7, paragraph-frame in grade 9, point-of-view starts in grade 6 | Kept | Each model hands on to a fuller one (narrative-arc, essay-structure) |
| Course id line in three forms ("ela-k12 (grade N row)", "ela-k12 (... year; slug ...)", "`english-language-arts-grade-9`") | Left to part B | Named in frame-cross-subject-2026-11-14.md; part B recommends the fix |
| "Exit answer", "exit question" against the glossary's "exit ticket"; the C3 column used for texts | Left to part B | Vocabulary and the frame format are part B's |

## For Cory

1. **Longer whole texts in grades 6 to 8 (money).** Finding 2 lengthens the three middle-school novellas to about
   25,000 to 30,000, 30,000 to 35,000 and 35,000 to 45,000 words, roughly 45,000 more words of commissioned
   fiction across the band, each read by a qualified ELA teacher. Pick: lengthen them; if the cost is too high, keep
   grade 6 as it is and lengthen grades 7 and 8 only.

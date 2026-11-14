# Frame read: math-grade-1 (Grade 1 Math), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/RUBRIC-MATH-K8.md, docs/pipeline/briefs/frame-write.md
  (the "Lessons from the social studies frames" list).
- The frame docs/courses/math-grade-1/frame.md and its row in data/plans/frames.csv (8 units, 160 days).
  data/plans/math-grade-1/source-map.csv does not exist yet; it comes with the scope and sequence.
- The 26 grade 1 rows of data/progressions/math.csv, the kindergarten rows before and the grade 2 rows after; the
  frames before and after (docs/courses/math-kindergarten/frame.md, docs/courses/math-grade-2/frame.md).
- The base text in S:\CurioClass-sources\illustrative-math\grade-1: every unit overview and all 146 lesson pages
  (titles, optional marks, the "Addressing" standards of each activity), and the text of lessons 6.11 to 6.15 and 8.6
  on diagrams; a search of grades 1 and 2 for "tape diagram".
- data/standards/ccss-math-standards.txt and ccss-math-focus.csv (grade 1 clusters).
- The same-year frames the course leans on or that lean on it: docs/courses/science-grade-1/frame.md and
  docs/courses/social-studies-grade-1/frame.md (no ELA grade 1 frame exists yet).
- Earlier reads: the social studies frame reads and fixes of 2026-11-13, docs/reviews/progression-math-*2026-11-13.md
  and progression-cross-*2026-11-13.md. No earlier math frame read exists.
- Gates: `plan.py check` exits 1 only on math-grade-6 unit 6, outside this read; `frame.py check math-grade-1`
  0 failures (8 units, 160 days, 154 in units, 6 for checks and respond days); `stale.py check` 0 failures.

## Verdict

The frame is sound: all 26 rows are placed once, every grade 1 standard and lettered part is owned, the base text's
146 lessons are all kept in its own order with no move to justify, the days add up (146 lessons and 8 assessment
days make 154) and major work is well above the K to 2 line. The biggest risk is the tape diagram: the frame says
unit 6 introduces it, but the base text never teaches a tape diagram in grade 1 (it calls its grade 1 cube diagrams
a precursor to grade 2's tape diagram), and the source map keeps unit 6 as written. The one change that matters most
is naming the unit 6 adaptation in the source map, so the model the progression hands to grade 2 is actually taught.

## Findings, most serious first

### 1. The tape diagram is said to be introduced in unit 6, but no kept base lesson teaches it (moderate; firm)

**What is wrong.** m1-all-problem-types has model_out tape-diagram ("Introduces the tape diagram late in the year"),
and the frame's Models table and unit 6 say the tape diagram is "drawn from matching drawings" there. The source map
keeps base unit 1.6 "as written" and adds no lesson. In the base text, grade 1 never names or teaches a tape
diagram: lessons 6.12 and 6.13 use rectangles of cubes to compare, and lesson 8.6 says its Compare drawing "lays the
foundation for working with tape diagrams in grade 2" (grade-1/unit-08/lesson-06.md). The first tape diagram lessons
are grade 2's 2.1.14 to 2.1.16 (Use Diagrams to Compare), built from bar graphs.
**Why it matters.** A unit 6 writer following the source map adapts lessons with no tape diagram in them, so the
model is not taught, and grade 2's readiness check assumes a model grade 1 never gave. This is the "first" claim the
brief asks to check (lesson 6).
**Fix (frame, source map and Models table).** Change the 1.6 row to: "Keep all; adapt 12 to 15: the base text's cube
and matching drawings for Compare and part-whole problems are redrawn as a tape diagram (a bar for each quantity,
labelled, a question mark for the unknown) and named; 8.6 reviews it". In the Models table say "Unit 6: the base
text's cube diagrams (6.12, 6.13) redrawn as a tape diagram". No day change. The grade 2 frame's matching edit is in
its read (finding 3 there). LAYER base text. REPEAT yes (lesson 6 of the brief: "first" and "introduces" claims
checked against the grade before and after).

### 2. Two cross-subject reasons and a status line do not match the frames now written (minor; firm)

**What is wrong.** The Cross-subject section says "The other subjects' frames are written later", yet this frame
already quotes the social studies frame's weeks (11, 27, 28), and the science frame exists. Unit 1's reason says
"Grade 1 science and social studies tally and sort in three groups early in the year": the science frame places its
three-group data lean (s1-light-materials) about week 20 and s1-daylight-seasons about week 31, and social studies'
vote is about week 11. The science table gives the 1-ESS1-2 lean "about week 2".
**Why it matters.** Unit 1 is first because of the base text's order, which stands on its own; a false seam reason
invites a later writer to move data for a lean that is not there. The stale status line breaks lesson 15 of the brief.
**Fix (frame).** Unit 1 "Why this unit, here": delete the last sentence, or replace it with "Data in three groups is
then ready long before grade 1 science (about week 20) and social studies (about week 11) use it". Cross-subject
opening: "The science and social studies grade 1 frames are written and their weeks are used below; the ELA grade 1
frame sets its own." In the science table, Needed by for m1-data-three-categories: "About week 20 (s1-light-materials;
s1-daylight-seasons records from its unit 1 but sorts in three groups about week 31)". LAYER process. REPEAT yes
(the social studies reads found stale notes about other files and lean weeks that did not match).

### 3. 1.G.A.3 is described in part (minor; firm)

**What is wrong.** Unit 7's "What students learn" gives "two and four equal shares, called halves, fourths and
quarters, and more shares means smaller shares". The standard also asks students to "use the phrases half of, fourth
of, and quarter of" and to "describe the whole as two of, or four of the shares" (data/standards). The kept base
lesson 7.10 ("One of the Pieces, All of the Pieces") teaches exactly that, so only the frame's wording is short.
**Why it matters.** Lesson 4 of the brief: a standard is never narrowed to its headline. The unit writer and the
end-of-year check ("halves and fourths") work from this cell.
**Fix (frame, unit 7).** Add: "the phrases half of, fourth of and quarter of, and the whole as two halves or four
fourths (1.G.A.3 in full)". LAYER standard. REPEAT yes (the social studies reads found standards taught only in
part).

## Lens checklist, course frame layer

| Line | Result |
|---|---|
| Major work under the line, by units, days or time | Met with room. 7 of 8 units, 133 of 160 days (83 percent), 137 of 146 lessons by the frame's count (my count from the base text's own Addressing tags: 136). The count is conservative: the EdReports evidence guide counts supporting work connected to major work (indicator 1e, PDF page 14 (printed 13)), and many unit 7 lessons also address 1.OA.C.6 and 1.NBT.C.4 |
| A supporting cluster that does not practise major work | Met. 1.MD.C.4 asks how many more and fewer (1.OA problem types); unit 7's center days and time lessons add within 100 |
| A source-map row with no keep, split, merge, cut or ours decision | Met; the 1.6 row needs its adaptation written in (finding 1) |
| A skill owned by two grades at the same depth, a handoff that skips a grade | None. Every kindergarten hand-on is picked up; every grade 1 row hands on to a grade 2 row that the grade 2 frame picks up |
| A model used before the grade that builds it | None. No number line (grade 2, after rulers); base-ten blocks in unit 3 before units 4 and 5 |
| A limit broken | None. Fluency within 10, strategies within 20, subtracting only multiples of 10, no standard algorithm, hours and half hours only |

## The brief's other checks

- **Owned skills:** all 26 rows placed once. No unit teaches another grade's skill.
- **Standards in full:** every grade 1 standard and lettered part owned; 1.G.A.3 wording short (finding 3).
  1.OA.A.1, 1.OA.C.6 and 1.NBT.C.4 are begun and finished as stated.
- **Units and reasons:** the base text's order teaches each model and skill before use; counting to 120 sits with
  measurement where it is needed, as the base text places it.
- **Days:** 154 + 4 + 2 = 160; each unit is its base lessons plus one assessment day. Unit 3 (29 days, five rows) is
  the longest, as its load asks. The 60-minute day is the base text's design.
- **Source map:** 146 lessons placed, none cut; the optional marks (1.15, 2.22, 3.28, 4.12, 4.23, 5.14, 6.17) match
  the base text. Eureka named only as a check-set reference.
- **Seams:** the kindergarten table matches the kindergarten frame row for row, including the proposed mk-one-to-one
  link; the grade 2 table matches the grade 2 frame's "Picked up" table.
- **Cross-subject:** social studies matches (vote week 11, flyer week 27, saving week 28, each after the math);
  science leans on length (weeks 11 and 24) come before math unit 6 and are bridged in the science frame, as "For the
  lead" item 3 says; science data weeks are finding 2.
- **Unit 8 with an empty Skills cell:** justified. It is the base text's spaced review of major work before the
  end-of-year check, its 10 lessons need a home in the source map, and it reviews fluency within 10, the grade's
  fluency target.
- **Lessons from the social studies frames:** 1 met; 2 met; 3 met; 4 finding 3; 5 met (readiness checks open units
  1, 3, 4 and 6 on the piece each rests on); 6 finding 1; 7 met; 8 met; 9 met; 10 met; 11 met; 12 met; 13 not
  applicable; 14 met; 15 finding 2.

## What is right and should not be touched

- The base text kept whole and in order, with no added lessons: grade 1's load fits its 146 lessons.
- Fluency within 10 checked by watching and a one-to-one card check, never timed; within 20 by strategies.
- The food drive and class pet teacher notes.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| The tape diagram is taught by adapting base lessons 6.12 to 6.15, with 8.6 as review; no lesson added | The base text's cube diagrams are the natural start, and the unit's days already fit | docs/courses/math-grade-1/frame.md, source map and Models table |

## For Cory

None. Nothing here changes scope, money, people or audience.

## What I could not judge

Whether the progression should keep the tape diagram in grade 1 at all. The row cites the Progressions (OA, PDF 27
and 31) and the base text waits until grade 2; both are defensible, and the fix above keeps the row as the contract.

## Sources

- IM K-12 Math 1st edition, Grade 1 and Grade 2, local copy (S:\CurioClass-sources\illustrative-math, CC BY 4.0):
  lesson lists, optional marks, Addressing tags; grade 1 lessons 6.12, 6.13, 7.10, 8.6; grade 2 lessons 1.14 to 1.16.
- EdReports Math K-8 Evidence Guide v2.0, indicator 1e,
  https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf, PDF pages 13 to 15 (printed 12 to
  14). Read, not copied.
- Student Achievement Partners focus documents via data/standards/ccss-math-focus.csv.
- Confidence: findings 1 to 3 firm.

## For the source list

None new.

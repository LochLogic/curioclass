# Frame read: math-kindergarten (Kindergarten Math), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/RUBRIC-MATH-K8.md, docs/pipeline/briefs/frame-write.md
  (the "Lessons from the social studies frames" list).
- The frame docs/courses/math-kindergarten/frame.md and its row in data/plans/frames.csv (8 units, 160 days).
  data/plans/math-kindergarten/source-map.csv does not exist yet; it comes with the scope and sequence (step 3).
- The 20 kindergarten rows of data/progressions/math.csv and the grade 1 rows they hand on to; the grade 1 frame
  docs/courses/math-grade-1/frame.md (the course after).
- The base text in S:\CurioClass-sources\illustrative-math\grade-K: every unit overview and all 137 lesson pages
  (titles, optional marks, the "Addressing" standards of each activity), and the activity text of lessons 3.6, 3.7,
  3.13, 5.10 and 6.12.
- data/standards/ccss-math-standards.txt and ccss-math-focus.csv (kindergarten clusters).
- The same-year frames the course leans on: docs/courses/science-kindergarten/frame.md and
  docs/courses/social-studies-kindergarten/frame.md (no ELA kindergarten frame exists yet).
- Earlier reads: the social studies frame reads and fixes of 2026-11-13, docs/reviews/progression-math-*2026-11-13.md
  and progression-cross-*2026-11-13.md ("For the course frames"). No earlier math frame read exists.
- Gates: `plan.py check` exits 1 only on math-grade-6 unit 6 (6.EE.C.9), outside this read; `frame.py check
  math-kindergarten` 0 failures (8 units, 160 days, 154 in units, 6 for checks and respond days); `stale.py check`
  0 failures.

## Verdict

The frame is sound in shape: all 20 rows are placed once, every kindergarten standard and lettered part is owned,
the base text's 137 lessons are each placed or cut with a reason, the days add up (154 in units: 136 base lessons,
10 Curio Class lessons, 8 assessment days) and major work clears the K to 2 line on all three counts. The biggest
risk is that the source map says "Keep" where the frame's own two moves require the base lessons to change: the
ten-frame is introduced in unit 2, but base lesson 5.10 (the base text's ten-frame introduction) and the unit 4
lessons that are now to use frames are kept as written. The one change that matters most is to write those
adaptations into the source map, so a day writer does not introduce the ten-frame twice.

## Findings, most serious first

### 1. The ten-frame move is not carried through the source map (moderate; firm)

**What is wrong.** The frame moves the ten-frame into unit 2 (mk-how-many owns model_out ten-frame), and the source
map adapts K.2's 5-frame lessons for it. But base lesson K.5.10 "Introduce the 10-frame" is still "Keep all": its
first activity has students cut out and join two 5-frames, and its synthesis tells the class they are meeting "a
new tool called a 10-frame" (grade-K/unit-05/lesson-10.md). The Models table also says unit 4 uses counters on frames
for joining and taking (mk-add-sub-meaning, mk-story-problems, mk-add-sub-expressions take ten-frame as model_in),
yet no K.4 lesson uses a 10-frame (none of grade-K/unit-04/lesson-*.md mentions one) and K.4 is "Keep all".
**Why it matters.** A day writer adapting K.5.10 as written introduces the ten-frame a second time in week 23, and
unit 4's days are built without the model the rows say they use. Severity follows the cost: the writer would build
wrong days from it.
**Fix (frame, source map).** Change the K.5 row to "Keep all; adapt 10: no longer the ten-frame's introduction, the
full 10-frame and how many are missing to make 10 (K.OA.A.4), with the 5 and some more already known from unit 2".
Change the K.4 row to "Keep all; adapt the joining and taking activities in lessons 1 to 12 to show counters on a
10-frame beside objects and fingers, where the count is 6 to 10". LAYER base text. REPEAT new (first base-text
frame read).

### 2. Unit 3's two added length lessons rest on a claim the base text contradicts (moderate; firm)

**What is wrong.** The Units table and source map say the base text gives K.MD.A "none on comparing lengths
directly" and that K.MD.A.2 for length "the base text never gives a lesson". Base lesson K.3.6 has an activity
"Compare Length of Rectangles" (longer, shorter, turned rectangles) and K.3.7 opens with "Compare Length of Straws",
whose stated purpose is lining up endpoints (MP6). The base text gives direct length comparison two activities,
not zero. Separately, K.MD.A.1's second clause, "Describe several measurable attributes of a single object", is not
named in unit 3's "What students learn".
**Why it matters.** The added days sit in additional work (K.MD.A) on a course whose major-work margin is 2.5
points, so their reason has to hold. A false reason also tells the unit writer to build length comparison from
nothing when two base activities exist to adapt.
**Fix (frame, Units unit 3 and source map).** Rewrite the reason: "The base text gives direct length comparison two
activities inside shape lessons (3.6, 3.7) and no lesson of its own; two Curio Class lessons give it whole days,
because the endpoint error needs time and kindergarten science leans on direct comparison." Rename the two added
lessons as settled below. Add to unit 3's "What students learn": "several measurable attributes of one object (a
box is long, heavy and holds a lot) (K.MD.A.1 in full)". LAYER base text and standard. REPEAT new.

### 3. The position-word lesson is moved to the start of unit 3 without a source-map row (minor; firm)

**What is wrong.** Unit 3's reason says "Position words come at the start" so they precede social studies' map unit
(about week 11). In the base text they are taught in K.3.13 (an I-spy activity with above, below, next to, beside),
near the end of the unit. The source map says K.3 "Keep, the unit as written". The base activity also focuses on
only four of K.G.A.1's six words (it allows others): in front of and behind are not planned in it.
**Why it matters.** The brief asks that every move from the base text's order be named and justified. A writer
following the map keeps K.3.13 in place, at about week 12, after the social studies unit that the move was for, and
teaches four words of six.
**Fix (frame, source map).** Split the K.3 row: "1 to 12, 14 | 3 | Keep" and "13 (position words) | 3 | Move to the
start of the unit; adapt to all six words of K.G.A.1, adding in front of and behind | Before social studies'
position words, about week 11". If the lesson also leans on the composed pattern-block pictures of 3.10 to 3.12, use
the room and simple shape cards instead. LAYER base text. REPEAT new.

### 4. K.G.B.4 starts in unit 3 but the frame places all of it in unit 7 (minor; firm)

**What is wrong.** mk-analyze-shapes (K.G.A.3; K.G.B.4) sits in unit 7, whose reason is that "comparing shapes by
number of sides and corners uses counting to 10 and the equations of units 4 and 5". But the base text teaches
K.G.B.4 for flat shapes in unit 3: lessons 3.1, 3.3 to 3.6, 3.8 and 3.9 all address it (describe and compare shapes,
sides and corners, rectangles and squares), and the frame keeps them there. The row's own note says "IM Kindergarten
unit 3 lessons 1 to 9 (flat) and unit 7 section B".
**Why it matters.** Lesson 5 of the frame-write brief: each thread starts where it is first used. A unit 3 writer
reading the table sees no K.G.B.4 and may drop the comparing talk the kept lessons are built on; the unit 7 reason
is not true of flat shapes.
**Fix (frame, units 3 and 7).** Unit 3 "What students learn", add: "comparing flat shapes by their sides, corners and
equal sides (K.G.B.4 for flat shapes, begun here; unit 7 owns it with solids)". Unit 7 "Why this unit, here": "Late in
the year as the base text places it: flat and solid shapes are compared together once flat shapes are secure from
unit 3, and the composing lessons (7.1 to 7.6) use the equations of units 4 and 5". The Skills column is unchanged.
LAYER frame. REPEAT yes (the social studies reads found threads that started before the unit that owned them).

### 5. Cross-subject weeks and one reason do not match the science frame now written, and a status line is stale (minor; firm)

**What is wrong.** The Cross-subject section says "The other subjects' frames are written later". The science and
social studies kindergarten frames now exist. The science frame places sk-push-pull (K.MD.A.2) in its unit 1, about
week 2, and sk-weather-watch (K.MD.B.3) about week 6; this frame gives "about week 12" for K-PS2-1 and "about week 8"
for the weather lean. Unit 3's reason for moving K.7.8 and 7.9 says it is "by the time kindergarten science compares
pushes", which it is not (week 2 against math weeks 9 to 13). The social studies frame matches (week 8 vote, week 11
position words, week 28 store).
**Why it matters.** The availability calendar is what the other frames honour; wrong weeks hide that science runs
its bridge in week 2. The move itself still holds on its other reason (all of K.MD.A in one place).
**Fix (frame, Cross-subject and unit 3).** Replace the status sentence with: "The science and social studies
kindergarten frames are written; their weeks are used below. The ELA kindergarten frame sets its own." Set the
K-PS2-1 row to "Needed by: about week 2 (science unit 1); science's bridge is direct side-by-side comparison with no
numbers" and the K-ESS2-1 row to "about week 6". In unit 3's reason and the K.7 source-map row, replace "by the time
kindergarten science compares pushes" with "so the year has one place for direct comparison, which kindergarten
science uses all year (its first push and pull unit bridges it in week 2)". LAYER process. REPEAT yes (lesson 15,
status lines about other files; the social studies reads found stale cross-subject notes).

### 6. Unit 2 says sorting "moves here" from the base text, but no base lesson moves (minor; firm)

**What is wrong.** Unit 2's reason: "Sorting moves here from the base text's scattered single lessons". The source map
moves no sorting lesson; the base text's K.MD.B.3 lessons (3.4, 7.7, 7.11, 8.1, 8.13, 8.14) stay where they are, and
unit 2 adds two Curio Class sorting lessons.
**Why it matters.** A writer may look for base sorting lessons to bring into unit 2, or think they are gone from
units 3, 7 and 8.
**Fix (frame, unit 2).** "Sorting is owned here with two Curio Class lessons, because the full standard (count each
group, order by count) needs counting to 10 and comparing, both finished in this unit; the base text's sorting
activities in units 3, 7 and 8 stay as practice." LAYER frame. REPEAT new.

## Lens checklist, course frame layer

| Line | Result |
|---|---|
| Major work under the line, by units, days or time | Met. 6 of 8 units (75.0 percent), 124 of 160 days (77.5), 121 of 136 kept lessons by the frame's count (my count from the base text's own "Addressing" tags: 124 of 137 lessons touch a major cluster). The frame counts conservatively: the EdReports evidence guide (indicator 1e, PDF page 14 (printed 13)) says connections between supporting and major work go in the count, so the true share is higher. Keep the margin: do not add more additional-cluster days |
| A supporting cluster that does not practise major work | Met. K.MD.B.3 is counted and ordered by count; unit 7's first six base lessons compose shapes with equations (K.OA.A.1 to A.5); unit 3 counts pattern-block pieces |
| A source-map row with no keep, split, merge, cut or ours decision | Met on decisions; but three "Keep" rows need "adapt" or "move" written in (findings 1 and 3) |
| A skill owned by two grades at the same depth, a handoff that skips a grade | None found. The grade 1 frame picks up every hand-on |
| A model used before the grade that builds it | None. The ten-frame is introduced in unit 2 before units 4 to 8 use it; unit 1 only explores 5-frames |
| A limit broken | None. Numerals to 20, counting to 100 orally, fluency within 5, no symbols for the unknown, no hundred chart |

## The brief's other checks

- **Owned skills:** all 20 rows placed once (gate and my read agree). No unit teaches another grade's skill.
- **Standards in full:** every K standard and lettered part is owned; K.MD.A.1's second clause is unnamed (finding
  2); everything else is named in full, including K.CC.B.5's 20 arranged and 10 scattered and K.NBT.A.1's recording.
- **Units and reasons:** order holds; the two weak reasons are findings 2 and 4.
- **Days:** 154 + 4 check + 2 respond = 160; the per-unit counts match the base lessons kept, the added lessons and one
  assessment day each. 60 minutes is the base text's own design ("Each lesson plan is designed to fit within a class
  period that is at least 60 minutes long", IM K-5 course guide). No unit is far over or under its load.
- **Source map:** 137 base lessons, 136 placed, 1 cut (K.3.15, optional art) with a reason; optional marks match the
  base text (K.6.12 carries only one optional activity and is rightly not listed as optional). Eureka is named only
  as a check-set reference, never mapped (docs/sources/BASE-TEXTS.md lists it as reference).
- **Seams:** Kindergarten has no course before. Every hand-on matches the grade 1 frame's "Picked up" table; the
  mk-one-to-one link is proposed under "For the lead" and the grade 1 frame names it too.
- **Cross-subject:** social studies kindergarten matches; science weeks are finding 5; no ELA frame yet.
- **Lessons from the social studies frames:** 1 (respond days) met; 2 (Candidate) met; 3 (time a day) met; 4
  (standards in full) finding 2; 5 (threads start where used) finding 4; 6 ("first" claims) met; 7 (both ends)
  met; 8 ("if later" lines) met; 9 (days by load) met; 10 (questions answerable) met; 11 (picks) met, contexts named;
  12 (sensitivity reads line) met; 13 (no math ahead of math) not applicable; 14 (paper path) met; 15 (status
  lines) finding 5.

## What is right and should not be touched

- The base text's unit order, kept, with every optional lesson kept as spaced practice.
- The counting routine that grows all year and closes in unit 8, and fluency within 5 checked by watching, never
  timed.
- Equations with the total on the left in units 4 and 5, on purpose.
- The teacher notes on counting objects, not children, and on food in lessons.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| K.5.10 becomes "the full 10-frame and how many are missing to make 10", not an introduction | The ten-frame is introduced in unit 2 | docs/courses/math-kindergarten/frame.md, source map |
| Unit 3's two added lessons: (1) comparing lengths and heights directly when the ends are not lined up, and turned objects (the endpoint error); (2) several measurable attributes of one object, then comparing two objects on one attribute | The base text already has two short length activities; the added days should cover what it does not | frame.md, units table unit 3 and source map |
| The position-word lesson (K.3.13) is the first lesson of unit 3, extended to all six words | Social studies uses the words about week 11 | frame.md, source map |

## For Cory

None. Nothing here changes scope, money, people or audience.

## What I could not judge

How a two-5-frames ten-frame in unit 2 works beside the base text's unit 2 activities until the unit plan adapts
them; the frame is right to leave that to the unit plan.

## Sources

- IM K-12 Math 1st edition, Kindergarten, local copy (S:\CurioClass-sources\illustrative-math\grade-K, CC BY 4.0):
  lesson lists, optional marks, Addressing tags, lessons 3.6, 3.7, 3.13, 5.10 and 6.12.
- EdReports Math K-8 Evidence Guide v2.0, indicator 1e,
  https://cdn.edreports.org/media/2026/06/Math%20K-8%20Evidence%20Guide_2.0.pdf, PDF pages 13 to 15 (printed 12 to
  14): the three counts and the rule that supporting work connected to major work is counted. Read, not copied.
- Student Achievement Partners focus documents via data/standards/ccss-math-focus.csv: cluster weights.
- Confidence: findings 1 to 6 firm (each rests on the base text's own page or the other frame's own table).

## For the source list

None new: the evidence guide is already on file in docs/RUBRIC-MATH-K8.md.

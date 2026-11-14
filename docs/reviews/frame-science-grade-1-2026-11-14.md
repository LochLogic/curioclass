# Frame read: science-grade-1 (Science, Grade 1), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md (to "How this differs").
- The frame docs/courses/science-grade-1/frame.md and its row in data/plans/frames.csv (8 units, 68 days).
- The 10 grade 1 rows of data/progressions/science.csv, the 11 kindergarten rows before and the grade 2 and grade 3
  rows that assume grade 1.
- The frames before and after: docs/courses/science-kindergarten/frame.md and docs/courses/science-grade-2/frame.md;
  for threads that skip to grade 3, docs/courses/science-grade-3/frame.md (Seams).
- Same-year frames: docs/courses/math-grade-1/frame.md (1.MD leans), docs/courses/social-studies-grade-1/frame.md
  (ss1-calendar-time's lean on 1-ESS1-2). No ELA grade 1 frame exists yet.
- docs/pipeline/briefs/frame-write.md, "Lessons from the social studies frames"; DESK-ANSWERS 2026-11-12 and
  2026-11-13 for science; docs/reviews/frame-k-2-fixes-2026-11-13.md for the kinds of earlier findings.
- Gates: `frame.py check science-grade-1` 0 failures (8 units, 68 days, 62 in units, 6 at course level);
  `plan.py check` passes for this frame; `stale.py check` 0 failures. My own script: every grade 1 hands_on and
  every K assumes it answers agree at both ends.
- Standards: codes only in data/standards/ngss-pes.txt; the performance expectations, clarification statements,
  boundaries and crosscutting concepts are judged **from my knowledge of NGSS (2013), not re-fetched**.

## Verdict

The frame is well built: all 10 rows sit once, sound and light are each taught before the message device that uses
both, the split daylight unit is counted once and started in week 4, and every clarification example is named in its
unit. The biggest risk is unit 8's observation: "light or dark at going-home time" is light in every season at almost
every school in the country, so the chart the year is built around shows no pattern, and the frame treats that as the
exception. The change that matters most is moving the daylight observation to a time that changes across the year;
next, unit 3's anchor (leaves from one tree) does not show young against their parents, which is what 1-LS3-1 asks.

## Findings, most serious first

### 1. Going-home time is light all year at most schools, so the daylight chart has no pattern (serious; firm)

**What is wrong.** Unit 8 and s1-daylight-seasons record "is it dark or light at the same clock time (going-home
time)". School ends about 2:30 to 3:30 pm. The earliest winter sunset in the contiguous United States is about
4:15 pm (northern states) and nearer 5:00 pm in the south (from memory of public sunrise and sunset tables), so the
chart reads "light" in fall, winter and spring alike. The frame's fallback, "Where going-home time is light all year,
the class marks light or dark at a fixed later clock time from a public sunrise and sunset table", is the usual case,
and as written it replaces observation with a table look-up, which 1-ESS1-2 ("make observations at different times of
year") does not intend as its main evidence.
**Why it matters.** The lens names "data with no pattern to find" as a day error; a writer builds eight months of
monthly marks and a four-day spring unit on a chart that cannot show winter is shorter. Social studies grade 1
(ss1-calendar-time) reads the same pattern.
**Fix (frame course brief "Split unit", unit 8, the "Where going-home time" note; progression row note through "For the
lead").** Observe at a time that crosses sunset during the year: 5:30 pm, "near dinner time", light in September and
April, dark in December almost everywhere in the contiguous United States. Each month a few families report light or
dark (optional, never graded, a class result needs only two or three reports), and the class also draws a monthly "day
strip" from the public sunrise and sunset table for its own town: a paper bar shaded light and dark, compared by length
only (no hours counted, the boundary). Keep going-home time only for a school where it does change. In "For the lead"
add the row change for s1-daylight-seasons: replace "(going-home time)" with "(a fixed early-evening time such as
5:30 pm, reported by families, beside a monthly light-and-dark day strip from a public table)". LAYER frame and
progression. REPEAT new.

### 2. Unit 3's anchor compares leaves of one tree, not young with their parents (moderate; firm)

**What is wrong.** The anchor is "a bag of leaves gathered from one tree" and the question "why is no leaf exactly the
same as another?" Leaves of one tree are parts of one plant. 1-LS3-1 is about young plants and animals being like, but
not exactly like, their parents (the clarification's example is leaves from the same kind of plant, and a breed of dog
and its parents). The question cannot be answered with the unit's idea, and its true answer (each leaf grew in a
different spot on the same plant) is outside the standard.
**Why it matters.** The anchor does not drive the expectation (S1, lesson 10), and a careless day could tell children
the leaves differ because they "come from different parents", which is false.
**Fix (frame unit 3).** Anchor: the young maple (or oak) seedlings under a big tree in or near the schoolyard, with
leaves from the big tree and from two or three other trees of the same kind. Question: "Are the little trees under our
big maple like it? Exactly like it?" Students line up leaves from seedlings and from parent trees by length and compare
shape; the animal photograph sets follow. The current candidate (a seedling beside its parent) becomes the anchor; the
new candidate is a class bean plant grown from a parent plant's seed. LAYER frame. REPEAT new.

### 3. Four kinds of material, "three groups" (minor; firm)

**What is wrong.** Unit 5 names all four clarification kinds (transparent, translucent, opaque, reflective), then says
students "sort and count the results in three groups" (the 1.MD.C.4 limit). A mirror is opaque and reflective, so a
writer cannot tell where it goes.
**Fix (frame unit 5 and the Mathematics table row for s1-light-materials).** "Sort by how much light gets through: all,
some, none (three groups). Then ask a second yes-or-no question of each object: does it send the light a new way? The
mirror (and kitchen foil) says yes." LAYER frame. REPEAT new.

### 4. The mid-year check asks for a written sentence before writing is taught (minor; firm)

**What is wrong.** The brief says students write a sentence with a frame "from unit 5 on"; the check after unit 4 asks
for "a drawn design ... with a sentence on how its shape helps".
**Fix (frame, Course-level checks).** "... with a spoken sentence on how its shape helps, which the teacher writes
down." LAYER frame. REPEAT yes (the social studies K to 2 reads tightened what a young child is asked to write).

### 5. Stale note: the math frame is written (minor; firm)

**What is wrong.** Cross-subject says "The other subjects' frames are written later and set their own unit numbers."
docs/courses/math-grade-1/frame.md exists: 1.MD.C.4 in its unit 1 (weeks 2 to 4), 1.MD.A.1 and 1.MD.A.2 in its unit 6
(about weeks 23 to 25), and its "For the lead" item 3 already names that science's length leans come late.
**Fix (frame, Cross-subject lead-in and Mathematics table).** Replace the sentence with: "Mathematics grade 1 teaches
1.MD.C.4 in its unit 1 (weeks 2 to 4) and 1.MD.A.1 and 1.MD.A.2 in its unit 6 (about weeks 23 to 25); unit 3 here
(week 11) runs on the direct-ordering bridge, unit 6 here (week 24) alongside math, with its own no-gaps lesson. The ELA
grade 1 frame sets its own unit numbers." LAYER process. REPEAT yes.

### 6. Teaching weeks: 34 here, 32 in kindergarten and grade 3 (minor; firm)

**What is wrong.** This frame and grade 2 count "34 teaching weeks"; kindergarten counts 32 and grade 3 "30 of the
year's 32 teaching weeks". The same school year cannot have both.
**Fix (frame "Days" bullet).** Name the year once, the same way in every science frame: "a school year of about 36
weeks, of which about 34 carry science lessons here" (or 32, whichever the lead fixes for K to 5), so the 68 days are
read as a choice, not a different year. LAYER frame. REPEAT new.

## Checked and found right (do not undo)

- **Owned skills.** All 10 rows placed once; s1-sketch-shape and s1-parts-mimic share unit 2, structure-function
  introduced before the sketch uses it; the sketch and design cycle in unit 6 named as review.
- **Standards in full (from memory of NGSS).** 1-PS4-1 both halves (paper near a speaker is the "sound makes materials
  vibrate" half); 1-PS4-2 all three observations and both kinds of illumination; 1-PS4-3 all four materials, no speed of
  light; 1-PS4-4 all three devices, no technology detail; 1-LS1-1 both moves and all four mimicry kinds; 1-LS1-2 signals
  and responses; 1-ESS1-1 sun, moon and stars with the star boundary; K-2-ETS1-2 sketch or model used to explain. The
  crosscutting concepts named per unit match the expectations' own (cause and effect for PS4, structure and function
  for LS1-1, patterns for LS1-2, LS3-1 and ESS1).
- **Order.** Sky first (fall shadows, starts the daylight chart); parts before like-parents (the features compared);
  sound and light before the device; parents and young in spring.
- **Days.** 62 in units; heaviest on unit 2 (two rows, a design) and unit 5 (two investigations); unit 8's 5 days
  rest on a year of two-minute marks. The split day is counted once.
- **Seams.** All 10 kindergarten hand-ons picked up with readiness looks named (units 1, 2, 4); every grade 1 hand-on
  answered in the grade 2 frame's "Picked up" table, and s1-sky-patterns, s1-like-parents, s1-parent-offspring and
  s1-parts-mimic in the grade 3 frame's.
- **Lessons 1 to 15.** All met except as findings 1 (lesson 10's spirit: evidence that shows the pattern), 2 (10) and
  5 (15); sensitivity reads name the adoptive and foster family reader for units 3 and 7.

## Cross-subject

Math grade 1: 1.MD.C.4 taught weeks 2 to 4, before science needs it (week 20): met. 1.MD.A.1 needed week 11, taught
week 23: bridge (direct ordering) holds. 1.MD.A.2 needed week 24, taught weeks 23 to 25: the unit's own no-gaps lesson
covers it. ELA grade 1: no frame yet; each lean has an if-later line. Social studies grade 1's calendar lean is honoured
in week 4, but reads the same pattern finding 1 breaks.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| A performance expectation for the grade has no unit, or a unit claims one it only touches | Met (1-LS3-1's anchor misses its idea, finding 2) |
| Grades 6 to 8: departure from OpenSciEd order | Not applicable |
| High school: band expectations with no owning course | Not applicable |
| No unit names its anchor phenomenon or design problem | Met |

## What I could not judge

- The ELA grade 1 frame (not written).
- Whether the moon log at home reaches enough families to show the moon's path (the class photo log is the fallback).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Daylight observed at 5:30 pm by family reports, beside a monthly light-and-dark day strip from the town's public table | Crosses sunset across the year; length compared, no hours | frame units 1 and 8; s1-daylight-seasons notes (through For the lead) |
| Unit 3 anchor: seedlings under a parent tree, leaves from parent and same-kind trees | Shows young against parents, the expectation's idea | frame unit 3 |
| Leaves gathered and pressed in October for unit 3 (about weeks 11 to 14) | Many leaves have rotted or gone under snow by late November | frame unit 3 |
| Light test: three groups by light through (all, some, none), then "sends it a new way?" yes or no | Keeps 1.MD.C.4's three groups and all four materials | frame unit 5 |
| Mid-year check sentence spoken, teacher writes | Writing with a frame starts in unit 5 | frame Course-level checks |
| Unit 4 also names a rice-on-plastic-wrap drum near a speaker for "sound makes materials vibrate" | A second case for the half children find harder | frame unit 4 |
| Unit 7's two sources: an American robin nest at feeding time and a white-tailed deer doe with her fawn | A bird and a mammal, both in public-domain federal video and photographs | frame unit 7 |

## For Cory

- Materials ceiling of about $40 a class (the frame's item 4): money.
- Elementary science time: grade 1 about 65 minutes a week against grade 3's 180 (see the kindergarten read).
- The adoptive and foster family reader for units 3 and 7, and the science teacher's safety read: people.

## Sources

From memory, not re-fetched this run: NGSS (2013) grade 1 and K-2 ETS performance expectations, clarification
statements, boundaries and foundation boxes; approximate winter sunset times in the contiguous United States from public
sunrise and sunset tables (US Naval Observatory and NOAA solar calculators). The repo files above for everything else.

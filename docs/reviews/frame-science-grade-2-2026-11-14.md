# Frame read: science-grade-2 (Science, Grade 2), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md (to "How this differs").
- The frame docs/courses/science-grade-2/frame.md and its row in data/plans/frames.csv (7 units, 76 days).
- The 12 grade 2 rows of data/progressions/science.csv, the kindergarten and grade 1 rows they assume, and the grade 3
  rows that assume grade 2.
- The frames before and after: docs/courses/science-grade-1/frame.md (and kindergarten, for the skip-grade threads)
  and docs/courses/science-grade-3/frame.md (present; its "Picked up" table read in full).
- Same-year frames: docs/courses/social-studies-grade-2/frame.md (ss2-continents-features leans on 2-ESS2-2). No math
  or ELA grade 2 frame exists yet.
- docs/pipeline/briefs/frame-write.md, "Lessons from the social studies frames"; DESK-ANSWERS 2026-11-12 and
  2026-11-13 for science; docs/reviews/frame-k-2-fixes-2026-11-13.md.
- Gates: `frame.py check science-grade-2` 0 failures (7 units, 76 days, 70 in units, 6 at course level);
  `plan.py check` passes for this frame; `stale.py check` 0 failures. My own script: every hand-on and assume between
  grades K to 3 agrees at both ends.
- Standards: codes only in data/standards/ngss-pes.txt; performance expectations, clarifications, boundaries and the
  crosscutting concepts in each expectation's foundation box are judged **from my knowledge of NGSS (2013), not
  re-fetched**.

## Verdict

The frame is sound and the strongest of the three K to 2 science frames: all 12 rows sit once, stability and change is
introduced before the erosion designs use it, K-2-ETS1-3 sits with the year's first two-design test, every
clarification example (all five material properties, dikes, windbreaks and plantings, butter, egg, leaf and paper) is
named, and the seams to grade 3 match the grade 3 frame line for line. The biggest risk is quiet narrowing by element:
two physical science units drop or only name the crosscutting concept their own expectation is built on. The one change
that matters most is naming cause and effect in unit 3 and developing energy and matter in unit 4.

## Findings, most serious first

### 1. Two units drop their expectations' own crosscutting concepts (moderate; likely, from memory of NGSS)

**What is wrong.** 2-PS1-2's crosscutting concept is cause and effect (simple tests gather evidence for or against
ideas about causes); unit 3's C3 cell lists patterns and structure and function only. 2-PS1-3's crosscutting concept is
energy and matter (objects may break into smaller pieces, be put together into larger pieces, or change shape); unit 4
lists it as "(pieces kept, named only)".
**Why it matters.** The bar counts crosscutting concepts by element (RUBRIC-SCIENCE, Gateway 2 and S11); a
performance expectation taught without its own concept is taught in part (lesson 4), and "named only" tells the unit
writer not to build it.
**Fix (frame units 3 and 4, C3 column and "Practices across the year").** Unit 3: "Crosscutting: patterns; cause and
effect (a test is designed to show which material causes the dry hat); structure and function." Unit 4: "Crosscutting:
energy and matter (the same pieces broken apart and put together into a new, larger object, developed in the account);
cause and effect (heating or cooling causes the change); systems." Add energy and matter to the brief's list of
crosscutting concepts (unit 4). LAYER frame. REPEAT yes (a standard narrowed, as in the social studies reads).

### 2. Two skip-grade threads start with no readiness look (minor; firm)

**What is wrong.** Units 1 and 5 open with readiness looks at earlier rows. Unit 2 assumes sk-forecast-severe
(kindergarten, two years back) and unit 7 assumes sk-needs-places (kindergarten), and neither names one, though the
Seams table says both threads skip grade 1 and are only "kept in use".
**Why it matters.** Lesson 5: a readiness check on an earlier grade's skill sits in the first unit that needs it. A
writer will not plan one for a two-year gap.
**Fix (frame units 2 and 7, "Why this unit, here").** Unit 2: "It opens with a one-question look back at
kindergarten's severe weather (what was coming, how people got ready) before sorting fast and slow events." Unit 7:
"It opens with the kindergarten needs-and-places picture map as a readiness look (deer near forests, fish in ponds)."
No day change. LAYER frame. REPEAT yes.

### 3. The burr anchor is a fall phenomenon taught in spring (minor; likely)

**What is wrong.** Unit 6 runs about weeks 27 to 30 (spring) and opens on "a sock walked through a patch of burrs or
weeds gone to seed". Burrs and seed heads are ripe in late summer and fall; in spring most are last year's, broken or
gone.
**Fix (frame unit 6 and the brief's materials line).** "Burrs and seed heads are gathered during unit 1 or 2's fall
outdoor time and kept dry in a labelled bag for unit 6; where none grow, a fuzzy glove walked through a tray of
hook-and-loop squares stands in, said to be a model." LAYER frame. REPEAT new.

### 4. Teaching weeks: 34 here, 32 in kindergarten and grade 3 (minor; firm)

**What is wrong.** As in the grade 1 read: this frame counts "34 teaching weeks", kindergarten 32 and grade 3 "30 of the
year's 32". The step to grade 3 is also large in time (about 80 minutes a week here, 180 in grade 3).
**Fix (frame "Days" bullet).** Name the year once as every science frame will: "a school year of about 36 weeks, of
which about 34 carry science lessons here". The time step goes to Cory (below). LAYER frame. REPEAT yes (grade 1 read
of the same date).

## Checked and found right (do not undo)

- **Owned skills.** All 12 rows placed once; s2-fast-slow-events before s2-erosion-solutions (stability-change in
  before use), s2-material-properties before s2-best-material, s2-pieces-new-object before s2-heat-cool-change; the
  compare step reused in unit 3 named as review.
- **Standards in full (from memory of NGSS).** 2-PS1-1 colour, texture, hardness, flexibility and shared properties;
  2-PS1-2 strength, flexibility, hardness, texture, absorbency, length only; 2-PS1-3 blocks, bricks, shapes; 2-PS1-4
  water, butter, egg, frozen leaf, heated paper; 2-LS2-1 one variable at a time; 2-LS2-2 seeds and pollen; 2-LS4-1
  diversity in each habitat, no names assessed; 2-ESS1-1 fast and slow, no measured time; 2-ESS2-1 dikes, windbreaks,
  shrubs, grass and trees; 2-ESS2-2 no scaling; 2-ESS2-3 solid and liquid, no water cycle; K-2-ETS1-3 two designs,
  strengths and weaknesses. Named picks (Kilauea, a road landslide, the Grand Canyon, a worn step) do not repeat
  another grade's.
- **Order and seasons.** Land and water in weeks 1 to 4, ahead of social studies grade 2's week 6; erosion in fall;
  plant test late winter; seeds, pollinators and habitats in spring.
- **Days.** 70 in units; unit 2 (16 days, three rows, a measured two-design test) the heaviest, unit 6 (one model, 6
  days) the lightest; the eight third-lesson weeks are tied to the erosion and plant follow-ups.
- **Seams.** All 11 earlier hand-ons picked up; every grade 2 hand-on to grade 3 appears in the grade 3 frame's
  "Picked up" table with the same unit sense; s2-land-water-model's empty assumes explained by the social studies lean.
- **Lessons 1 to 15.** Respond days, "Candidate:" cells, time stated, if-later lines (the ruler bridge is taught in the
  unit if math is late), nothing ahead of math (whole centimeters, scale of one), paper path, sensitivity reads with the
  disaster reader and the heating safety read. Lessons 4 and 5 are missed as findings 1 and 2.

## Cross-subject

Social studies grade 2's lean on 2-ESS2-2 (about week 6) is honoured by unit 1 (weeks 1 to 4). Math grade 2 and ELA
grade 2 have no frame, so "taught first" cannot be checked; each lean carries a bridge, and the earliest (2.MD.A.1,
week 9) teaches reading a ruler itself if math has not.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| A performance expectation for the grade has no unit, or a unit claims one it only touches | Met for core ideas and practices; two crosscutting concepts in part (finding 1) |
| Grades 6 to 8: departure from OpenSciEd order | Not applicable |
| High school: band expectations with no owning course | Not applicable |
| No unit names its anchor phenomenon or design problem | Met |

## What I could not judge

- Math and ELA grade 2 frames (not written).
- Whether $50 a class covers seeds, soil and towels for every group (Cory's money call).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Unit 3 names cause and effect; unit 4 develops energy and matter | Each is the expectation's own crosscutting concept | docs/courses/science-grade-2/frame.md |
| One-question readiness looks in units 2 (severe weather) and 7 (needs-and-places map) | Two-year gaps from kindergarten | frame units 2 and 7 |
| Burrs gathered in fall and kept dry; hook-and-loop stand-in | The anchor exists in spring | frame unit 6 |

## For Cory

- Materials ceiling of about $50 a class (the frame's item 3): money.
- Elementary science time: grade 2 at about 80 minutes a week, grade 3 at 180. One decision for K to 5 would make the
  step deliberate.
- The disaster-aware reader for unit 2 and the science teacher's safety read for unit 4's heating: people.

## Sources

From memory, not re-fetched this run: NGSS (2013) grade 2 and K-2 ETS performance expectations, clarification
statements, boundaries and foundation boxes (the crosscutting concept named in each). The repo files above for
everything else.

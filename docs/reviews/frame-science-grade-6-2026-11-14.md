# Frame read: science-grade-6 (Science, grade 6), 2026-11-14

Expert read under docs/pipeline/briefs/frame-read.md. I did not write this frame.

## What I read

- docs/courses/science-grade-6/frame.md (whole, including the source map and the loss check the grade 7 and 8 frames
  point to), with docs/courses/science-grade-5/frame.md before it and the grade 7 frame after it (seams).
- data/progressions/science.csv: all 14 grade 6 rows, and the grade 5 and grade 7 rows the seams name.
- docs/pipeline/briefs/frame-write.md (the 15 lessons), docs/agents/EXPERT.md, docs/agents/lenses/science.md,
  docs/RUBRIC-SCIENCE.md (S5, S6, S11, S12), DESK-ANSWERS science entries 2026-11-12 and 2026-11-13,
  docs/sources/BASE-TEXTS.md.
- data/progressions/math.csv and the math grade 6 frame; the social studies grade 6 frame (timeline and latitude
  work).
- The base text in S:\CurioClass-sources\openscied-ms: every grade 6 storyline and unit page (lesson lists, lesson
  days, expectation lists).
- Gates: `python -X utf8 scripts/frame.py check science-grade-6` (0 failures), `python -X utf8 scripts/plan.py
  check` (exit 0), `python -X utf8 scripts/stale.py check` (0 failures).
- NGSS performance expectations and boundaries judged from my own knowledge (data/standards/ngss-pes.txt holds codes
  only); findings that rest on it say so.

## Verdict

Go after small fixes. This is the strongest of the three middle school frames: the source map matches the base
exactly, the loss check is sound for grade 6, safety is named (lasers, hot water, dry ice, slides), sensitivity
readers are named, and the For the lead list already catches the stale row notes. The fixes are a no-microscope
path that drops the investigation without saying so, a cells unit a day short, math leans marked "later" that math 6
teaches first, a narrowed MS-ESS2-2, and a code count off by one.

## Findings, most serious first

### 1. The no-microscope path drops the investigation and does not say it is weaker (moderate; firm)

**What is wrong.** Unit 6 owns MS-LS1-1 in full: an investigation giving evidence that living things are made of
cells. The no-kit line reads "No microscopes: hand lenses and a public-domain micrograph set." A hand lens (about 10
times) cannot resolve most cells, so students would look at pictures, not gather evidence. RUBRIC-SCIENCE S6 asks that
a cheaper path keep the practice, or say plainly what it loses.

**Fix (frame).** Unit 6 note: "Low-cost path: a folding paper microscope or a clip-on phone lens (about 60 times or
more) keeps the investigation. No-kit path: micrographs plus a virtual microscope; weaker, because students read
evidence others gathered; the unit plan says so to the teacher."

LAYER frame. REPEAT new.

### 2. Unit 6 is the one unit under base time, and unit 5's MS-PS4-3 time is not named (minor to moderate; firm on the arithmetic)

**What is wrong.** Base days times 0.9: 16.2, 33.3, 37.8, 22.5, 18.9, 22.5. Unit 6 gets 22, under its base, while
carrying MS-LS1-1 in full, the starts of three later expectations, two retrieval openers and the disability lesson.
Unit 3 has about a day spare (39 against 37.8). Separately, unit 5's MS-PS4-3 (digital signals more reliable) rests on
base lesson 8 (one day) plus two openers and the wave-model reactivation; the frame does not say how much time that
gets.

**Fix (frame).** Unit 3: 39 to 38; unit 6: 22 to 23 (total unchanged). Unit 5 text: "MS-PS4-3: base lesson 8 and about
one more lesson for the wave-model reactivation and the signals comparison."

LAYER frame. REPEAT yes (days by load).

### 3. Math leans marked as supplied though math 6 teaches them first (minor; firm)

**What is wrong.** The unit 4 note says the timeline scale "is given ... until math 6 teaches ratio scaling", and the
cross-subject table treats ratio parts and ratio language as later. Math 6 teaches ratio language on days 18 to 38,
ratio problems on days 18 to 58 and unit rates on 44 to 50, before unit 4 (days 93 to 116) and unit 6 (137 to 158).
The row note itself says the scale is supplied only "until students can set a scale by ratio reasoning".

**Fix (frame).** Cross-subject rows: "Available: math 6 days 18 to 58." Unit 4 note: "Students set the timeline scale
themselves by ratio reasoning (for example 1 meter for each billion years worked out in class); the scale is given
only if math 6 runs late." Unit 6: "magnification as a ratio (math 6 ratio language, taught)". Center, histograms and
negative numbers are bridged correctly; leave them.

LAYER frame. REPEAT yes (no math ahead of math, and its other side: no supplying what math has taught).

### 4. MS-ESS2-2 narrowed to rates (minor; likely)

**What is wrong.** From my knowledge of the clarification, MS-ESS2-2 covers spatial as well as time scales (from
microscopic geochemical reactions to mountain ranges), processes of water, ice and wind, and processes that are
usually gradual but punctuated by catastrophic events (earthquakes, volcanoes, meteor impacts). Unit 4 names rates
from centimeters a year to a landslide only.

**Fix (frame).** Unit 4: add "at sizes from microscopic weathering reactions to mountain ranges; shaped by water, ice
and wind; usually gradual, sometimes sudden (an earthquake, an eruption, a meteor impact)".

LAYER frame. REPEAT yes (standards in full).

### 5. "13 codes on 14 rows" (minor; firm)

The units carry 14 codes (3, 4, 4, 2 and 1 across units 1 to 5 and 6; s6-particle-temperature owns two). Fix the
course-in-brief sentence to "14 codes on 14 rows". LAYER frame. REPEAT new.

### 6. The earlier Codex read is stale (minor; firm)

docs/reviews/frame-science-grade-6-codex-2026-11-14.md withheld its verdict because the plan gate failed; the gate now
passes. Fix: the caller adds "Superseded: the plan gate passes as of 2026-11-14; see frame-science-grade-6-2026-11-14.md."
LAYER process. REPEAT yes.

### 7. The shared loss check is too strong for grades 7 and 8 (minor here; firm)

The source map's loss check, which the grade 7 and 8 frames point to, says nothing is lost. That holds for grade 6, but
not for 7.6 (MS-ESS3-1's mineral part is an extension), 8.3 (magnets only; no electric or gravitational lessons) or
8.5 (no whole-cell model for MS-LS1-2). Fix: the shared text says "for grade 6, nothing is lost; for grades 7 and 8 see
each frame's loss check", and those frames name their gaps (see their reports). LAYER frame. REPEAT new.

## Checked and found right (do not undo)

- Source map: 6.1 18, 6.2 37, 6.3 42, 6.4 25, 6.5 21, 6.6 25 days; lesson ranges match the storylines.
- The 0.9 scaling for 50-minute lessons, and the "about 5 days" added for safety, openers and math bridges.
- Order kept as OpenSciEd's; the unit 6 starts of MS-LS1-2, LS1-3 and LS1-8 named with their later owners.
- Safety: class 2 lasers below eye level, hot water at a stated limit, dry ice teacher-only, slides by the edges, no
  body fluids. Age of the Earth and faith handled per BASELINE rule 5.
- Sensitivity readers named (disability community, unit 6 lesson 14; counselor note, unit 5).
- Seams with grade 5 match its handed-on table; the social studies grade 6 timeline (days 1 to 10) and latitude bands
  (about days 26 to 39) come before science uses them.
- For the lead items on the s6-light-paths and s6-particle-temperature notes and the MS-PS1-4 start note: right.

## Cross-subject

- Math 6: center, histograms and negative numbers bridged correctly; ratios available (finding 3). Math 6's reopen
  condition (science 6 placing base 6.5 after day 120) is borderline (6.5 starts day 117); no change needed.
- Social studies 6: in step. ELA 6 frame not yet written; needs recorded, right.

## The lens checklist (course frame layer)

| Check | Result |
|---|---|
| Phenomena named per unit | Met |
| Storyline order and reasons | Met |
| Models carried and revised | Met |
| Standards in full | Missed: finding 4 |
| Days by load | Missed: finding 2 |
| Safety (hazards and controls) | Met |
| Materials paths | Missed: finding 1 |
| Sensitivity | Met |
| Math and ELA in step | Met, with finding 3 |
| Seams both ends | Met |

## What I could not judge

- Real lesson timing at 50 minutes.
- NGSS clarification wording was not re-read from the source this session.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Move 1 day from unit 3 to unit 6 | Unit 6 is the only unit under base time and carries the most new load | docs/courses/science-grade-6/frame.md |
| Students set the timeline scale by ratio reasoning | Math 6 teaches ratios on days 18 to 58, before unit 4 | docs/courses/science-grade-6/frame.md |
| Paper or clip-on microscope as the low-cost path | Keeps the MS-LS1-1 investigation | docs/courses/science-grade-6/frame.md |

## For Cory

Nothing new beyond the frame's own For the lead (minutes per lesson, course ids, people).

## Sources

- S:\CurioClass-sources\openscied-ms: grade 6 storylines and unit pages.
- data/progressions/science.csv and math.csv; math grade 6 and social studies grade 6 frames.
- NGSS middle school performance expectations, from my knowledge.

## For the source list

- Nothing new for grade 6.

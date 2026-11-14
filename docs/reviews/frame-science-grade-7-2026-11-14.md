# Frame read: science-grade-7 (Science, grade 7), 2026-11-14

Expert read under docs/pipeline/briefs/frame-read.md. I did not write this frame.

## What I read

- docs/courses/science-grade-7/frame.md (whole), with the grade 6 frame before it and the grade 8 frame after it
  (seams), and the shared source map and loss check in the grade 6 frame.
- data/progressions/science.csv: all 18 grade 7 rows, and the grade 6 and grade 8 rows the seams name.
- docs/pipeline/briefs/frame-write.md (the 15 lessons), docs/agents/EXPERT.md, docs/agents/lenses/science.md,
  docs/RUBRIC-SCIENCE.md (S5, S6, S11, S12), DESK-ANSWERS science entries 2026-11-12 and 2026-11-13,
  docs/sources/BASE-TEXTS.md.
- data/progressions/math.csv and the math grade 6 and 7 frames.
- The base text in S:\CurioClass-sources\openscied-ms: every grade 7 storyline and unit page, and the Teacher
  Editions of 7.1 and 7.6 (extracted from the full-unit zips and searched).
- Gates: `python -X utf8 scripts/frame.py check science-grade-7` (0 failures), `python -X utf8 scripts/plan.py
  check` (exit 0), `python -X utf8 scripts/stale.py check` (0 failures).
- NGSS performance expectations and boundaries judged from my own knowledge (data/standards/ngss-pes.txt holds codes
  only); findings that rest on it say so.

## Verdict

Go after small fixes. The source map matches the base exactly, the order is OpenSciEd's, 19 codes sit on 18 rows,
the checks have respond days, and the seams and math leans line up (proportional tables and percent are taught in
math 7 before the units that use them). Three things need fixing before the scope and sequence: MS-ESS3-1 is owned
in unit 6 but base 7.6 leaves its mineral and geologic part to an extension the frame does not take up; units 4 and 5
are short for what they carry; and unit 1 names the electrolysis demonstration but not the base's flame and heating
work.

## Findings, most serious first

### 1. MS-ESS3-1 rests on an extension the frame does not name (moderate; firm)

**What is wrong.** s7-resource-distribution owns MS-ESS3-1 (uneven distribution of mineral, energy and groundwater
resources explained by past and current geoscience processes) in unit 6. Base 7.6 teaches the uneven distribution of
fresh water well, but its own Teacher Edition says the ESS3.A ideas "around mineral resources and past geologic
processes" are developed only if the home learning and the lesson 10 extension ("Uneven Distribution of Fossil Fuel
Resources", then broadened to other resources) are used. The frame gives unit 6 the base days with no added time and
names no lesson for the expectation.

**Why it matters.** The geologic half of the expectation (ores near old volcanic and tectonic zones, fossil fuels
where ancient seas and swamps were buried, groundwater in porous rock) is the part that uses the grade 6 rock-cycle
and plate models the row assumes. Without it the expectation is narrowed to water (brief lesson 4).

**Fix (frame).** Unit 6 text: "MS-ESS3-1: base lesson 10 with its extension taught in full (fossil fuel formation and
distribution), plus a Curio Class addition of about 1 day on mineral ores and groundwater, explained with the grade 6
plate and rock-cycle models." Add 1 day to unit 6. Correct the loss check: "7.6 leaves MS-ESS3-1's mineral part to an
extension; taught here as above."

LAYER base text (and frame). REPEAT new.

### 2. Units 4 and 5 are short for their load (moderate; firm on the arithmetic, judgment on the size)

**What is wrong.** Base days times 0.9: 22.5, 18.9, 26.1, 26.1, 29.7, 29.7 (153). The frame sets 23, 19, 27, 26, 31,
30. Unit 4 sits under its base time while carrying about five retrieval openers and the food-web and matter-cycle
reactivation, and its MS-PS1-3 part rests on about one day inside base lesson 12 (the unit page says "parts 3 to 6,
about a day") while the frame asks a researched material write-up (W.7.7, W.7.8). Unit 5 gets 1.3 days over base for
two readiness checks, each with a one-lesson reteach, plus several openers. Adding finding 1's day, the year is about
3 days short.

**Fix (frame).** Unit 4: 26 to 28 (openers merged into lessons where they fit; 1 day for the synthetic-material
research). Unit 5: 31 to 32. Unit 6: 30 to 31 (finding 1). That is 160 in units and 164 in the year, over the
yardstick by 4 with the reason stated; or hold 160 by taking the 4 days from named base lessons. Either way the
course-in-brief arithmetic must change, and the choice joins the minutes-per-lesson question for Cory.

LAYER frame. REPEAT yes (days by load).

### 3. Unit 1 safety names only the electrolysis demonstration (moderate; firm)

**What is wrong.** Base 7.1 runs gas tests with flames (a glowing splint that bursts into flame in oxygen, a flame
that goes out in a non-flammable gas) and heats water over two days around lesson 9. The frame's unit 1 note names
the electrolysis demonstration (lesson 10) and mixing only. Unit 3's burning of food in a closed system (base lesson
11) is named as a teacher demonstration, which is right.

**Fix (frame).** Unit 1 teacher note: "Flame tests and heating are teacher demonstrations: goggles for all, hair tied
back, a fire-safe surface, an extinguisher nearby; hot plates, not open flames, for heating water; students observe
from a set distance." Keep the unit 3 and ration-heater notes.

LAYER frame. REPEAT yes (lab safety, the lens).

### 4. MS-PS1-2's property list omits boiling point (minor; likely)

Unit 1 lists density, melting point, solubility, flammability and odour; the PE clarification (from my knowledge)
also names boiling point. Add it. LAYER frame. REPEAT yes (standards in full).

### 5. The earlier Codex read is stale (minor; firm)

docs/reviews/frame-science-grade-7-codex-2026-11-14.md withheld its verdict because the plan gate failed; the gate now
passes. Fix: the caller adds "Superseded: the plan gate passes as of 2026-11-14; see frame-science-grade-7-2026-11-14.md."
LAYER process. REPEAT yes.

## Checked and found right (do not undo)

- Source map: 7.1 25, 7.2 21, 7.3 29, 7.4 29, 7.5 33 (two optional lessons at 0 days, left out of the count), 7.6 33;
  lesson ranges match the storylines.
- MS-PS1-1's extended structures: 7.1 teaches extended structures and crystals; the frame's salt crystal pick fits.
- 19 codes on 18 rows; 7.2 to 7.4 codes from grade 6 marked as review and named so.
- The MS-LS1-5 start note under For the lead (7.3 lists it unmarked): right.
- Course checks with respond days, "Candidate:" cells, time stated, paper path, no accounts.
- Math: proportional tables (math 7 days 13 to 33) before unit 2's design work; percent (days 47 to 68) before
  unit 6. Seams with grade 6 and grade 8 match the rows.

## Cross-subject

- Math 7: in step, as above. ELA 7 frame not yet written; the W.7.7 and W.7.8 needs are recorded as needs, right.

## The lens checklist (course frame layer)

| Check | Result |
|---|---|
| Phenomena named per unit | Met |
| Storyline order and reasons | Met |
| Models carried and revised | Met |
| Standards in full | Missed: findings 1, 4 |
| Days by load | Missed: finding 2 |
| Safety (hazards and controls) | Missed: finding 3 |
| Materials paths | Met |
| Sensitivity | Met |
| Math and ELA in step | Met |
| Seams both ends | Met |

## What I could not judge

- Real lesson timing at 50 minutes; whether 164 days is acceptable is Cory's call.
- NGSS clarification wording was not re-read from the source this session.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Teach 7.6 lesson 10's extension in full plus a 1-day ore and groundwater addition | Base leaves MS-ESS3-1's geologic part to an extension | docs/courses/science-grade-7/frame.md |
| Flame tests and heating as teacher demonstrations | Open flame and hot water with 12-year-olds | docs/courses/science-grade-7/frame.md |

## For Cory

1. Year length for grade 7: about 164 days for the load, or 160 with named base lessons cut. Goes with the
   minutes-per-lesson question.

## Sources

- S:\CurioClass-sources\openscied-ms: grade 7 storylines and unit pages; Teacher Editions of 7.1 and 7.6 (7.6
  "DCIs that are fully developed if all ... extension activities are used" section and lesson 10 extension).
- data/progressions/science.csv and math.csv; math grade 6 and 7 frames.
- NGSS middle school performance expectations, from my knowledge.

## For the source list

- The Teacher Edition's section on which DCIs are fully developed only with extensions is the quickest way to find
  base gaps; worth reading for every OpenSciEd unit before a unit plan.

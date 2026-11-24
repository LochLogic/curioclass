# Math unit plans: structure pass, 2026-11-24

One pass over the "For the structure pass" and "Day faults" items of the 2026-11-24 unit reads for eleven math
courses: algebra-i, algebra-ii, geometry, math-grade-1, math-grade-2, math-grade-3, math-grade-5, math-grade-6,
math-grade-7, math-grade-8 and math-kindergarten (COURSE-RUN stage 4). Each item was checked against the current
files first. Items are grouped by target and marked **applied** (and how) or **not applied** (and why). Where an
item named a lead-list line ("as listed in the lead list"), the wording came from
docs/reviews/lead-list-lens-pass-2026-11-17.md.

Plans moved only to stay in step with the data: the generated "Day list" rows of every edited day were brought into
line with days.csv, and the skel lines for tools, supplies and safety were refreshed where those were the only
difference. Writer text was not touched except where an item asked for it.

## Gate results

| Gate | Before | After |
|---|---|---|
| `unitplan.py check` (the 11 courses, 91 unit plans) | 91 PASS, 0 FAIL | 91 PASS, 0 FAIL |
| `sequence.py check`, each of the 11 courses | 0 failures each | 0 failures each |
| `sequence.py` notes (never failures) | algebra-i 6, algebra-ii 3, geometry 3, grade 1 0, grade 2 1, grade 3 4, grade 5 0, grade 6 0, grade 7 1, grade 8 2, K 3 | the same, except algebra-ii 2 (the day 46 note cleared) |

No progression file changed, so the progression gate was not needed.

Edits undone because a gate showed a new failure or note:

- algebra-ii source map row IM Alg2.5 L11 (day 107) "keep" to "change": sequence.py fails it, since "change" is not a
  decision value (keep, split, merge, cut, ours).
- algebra-ii day 14 note, first wording: it raised six new rule 2 notes for unit 1. A second wording (below) holds.
- geometry day 1 note, dropping the opening retrieval sentence: three new rule 2 notes (m8-transformations-coordinates,
  alg1-writing-equations-constraints and alg1-vertex-form want retrieval, not only the readiness check).
- math-grade-1 1.NBT.C.5 on days 119, 120 and 128: s06 fails (no field 2 line, no day 128 field 5 item).
- math-kindergarten K.CC.C.7 and K.CC.B.4c on day 36: s02 fails (day 36 is a mid assessment with no field 5 item for
  either code).
- math-kindergarten K.CC.A.3 off days 19, 20 and 25: a new note, day 27 (Fluency) becomes the first K.CC.A.3 day.

## Day faults

None in any of the eleven reads (algebra-ii, math-grade-2, math-grade-3, math-grade-5, math-grade-7 and
math-grade-8 say so; the other five list none). No row was added to data/plans/defects.csv.

## Ledger

### Algebra I

- **A-SSE.A.1 begun in unit 2, F-LE.A.2 begun in unit 6: applied** in days.csv with the `~` mark (days 23 and 45
  `~A-SSE.A.1`; day 122 `~F-LE.A.2`), the course-local way the skeleton reads begun codes, rather than in
  data/progressions/math.csv, which other courses share. Day 20 also takes `~F-LE.A.2`, so days.csv agrees with the
  begun line s02 already printed. The s02 and s06 standards lines were taken from a fresh skeleton, and the s02 day
  45 field 5 cell now reads `~A-SSE.A.1`.
- **m8-roots "Last used: this course, last day 15" in s02 field 4: not applied, works as ruled.** Day 15 teaches
  alg1-center-spread, whose progression row assumes m8-roots, so the one-hop rule (lead, 2026-11-15) counts it as a
  use. Day 10 is a retrieval opening, which the rule says is not a use.

### Algebra II

- **Day 48 codes, drop N-RN.A.2: applied.**
- **Day 46 codes, drop N-RN.A.1: applied.** The day now carries no code; sequence.py accepts it and its day 46
  note cleared.
- **Day 121 note, exp-log retrieval: applied.**
- **Day 90 goal, last 15 minutes: applied.**
- **Day 87 note, the lettered work: applied** with the lead list's parts (A-SSE.B.3a zeros, A-SSE.B.3b extreme value,
  F-IF.C.8a symmetry, about 15 minutes). The read's "(F-IF.C.7e graphs)" does not match day 87's codes, so the
  lead-list wording was used.
- **Tools: applied.** Graphing calculator on days 82 to 84 and 94; a graphing device with a shared display on day
  105; a scientific or graphing calculator in radian mode on day 129; day 156's simulation marked "read supplied
  runs, no tool operated".
- **Day 155 supplies: applied** (printed random-number stream or eight numbered outcome slips).
- **Days 139, 140 and 143: applied in part.** Day 140's note names the support card and partner; day 143's goal names
  the normal table and the conversion to standard deviations. Day 139's tools line ("simulation follows the hand
  draw") was not added: the tools column holds tool names, and day 139 already lists the simulation.
- **Day 79 duplicated sentence: applied** (the second half-life sentence removed).
- **Day 18 codes: not applied.** Neither the read nor the lead list names the codes to add; adding A-CED.A.2,
  F-BF.A.1 or S-ID.B.6a would give s02 new owned codes. For the lead.
- **A-APR.B.2 off day 26: applied.** Kept on day 30, whose goal works from factor information.
- **Day 34 add A-APR.D.6: not applied.** s02 Teaching places the rational rewrites on days 33 and 35, which already
  carry the code.
- **Day 14 note, "unit 1 has no teaching use": applied** as "day 1 checked it and the openings of days 2 to 12 keep
  it up; unit 2's openings get their own check" (see the undone first wording above).
- **Source map day 107 "change": not applied** (see above). The layout has no "change" value; if the lead wants it
  marked, the nearest value and the column's rule are the lead's call.
- **Frame unit 3 Check set, "locating powers of i on a drawn plane": applied.** The extension is deleted from the
  frame and from the s03 skel copy; the "Working Backwards" extension stays.
- **docs/courses/algebra-ii/TOOL-ASKS.md: applied.** Created with headings s06 (live unit-circle graph, days 122 to
  124) and s07 (simulation that keeps the model; shaded normal areas). s07's link no longer says "not yet written".

### Geometry

- **docs/courses/geometry/TOOL-ASKS.md: applied** (day 8 dynamic construction view; paper fallback).
- **Day 1, drop the m8-transformations-coordinates retrieval: not applied** (undone, see above; sequence.py wants the
  retrieval).
- **Day 25 minute split: applied** (22 for E2 and E3, 13 for E1 and E4 to E7, 15 for the proof).
- **Frame and s01 skel, pentagon and "Now What Can You Build?": applied.** The pentagon extension is dropped (the
  scope already drops it). "Now What Can You Build?" is base lesson 22, verified in the local base text, now given
  with its url and placed within day 22, as the scope keeps it. "neighbourhood" became "neighborhood".
- **Supplies and safety, units 1 to 3, 8: applied.** Compass and straightedge on days 11 and 12; paper strips and
  squared paper on days 1, 2 and 10 to 18; graph paper on days 27, 31, 49, 52, 54, 56 and 66; compass on days 34
  and 40 with a compass-point safety line; ruler on day 66; tape measure or meter stick on day 64; safety on day 50
  (string) and day 64 (outdoor limits); a paper spinner, counters and a bag on days 144, 151 and 157.
- **Day 38 goal, day 43 note, days 71, 73, 129 and 138 goals: applied.** Day 138 uses US "Practice".
- **Days 28 to 42 boilerplate: applied** ("and unit-guided cylinder measurement" removed from all 17 rows). **Day 40
  note: applied**, rewritten for lesson 14.
- **Source map: applied in part.**
  - Lesson 1 and 2 titles: applied ("Build It", "Constructing Patterns", checked in the local base text).
  - Unit 5 titles: applied (the 18 base-text titles from the lead list).
  - Unit 2 rows 10, 12 and 13 (day 36 pairing): not applied; re-pairing base lessons to days is a sequence judgment,
    and it moves s02 field 10.
  - A unit 6 row for "Weighted Averages in a Triangle": not applied; the lead list leaves open whether day 121 uses it,
    and a new row needs s06 field 10 to name it.
  - Day 117's goal against L12: not applied; the two describe different lessons and the fix is a choice.
- **Scope line on unit 4 and unit 5 evidence, days 90, 94, 98 and 101 notes: applied.** "Retain", "retained" and
  "reuses" became "formative; feedback and revision before any score", in the notes and in the scope's unit 5
  Evidence paragraph.
- **Day 88 (G-MG.A.3 and the length-multiplier choice), day 92 (geo-right-triangle-trig), day 96 (rotation and
  G-GMD.B.4): applied.** s05 passes with the new codes.
- **Scope focus table, unit 6 to 720 / 900, total 4597 / 6514, 70.57 percent: applied.**
- **Fluency first days 41, 72 and 111: not applied.** "Confirm or retype" is a kind judgment for the lead.

### Grade 1

- **Days 20 and 25, drop 1.OA.D.7; day 57 "days 54 and 55"; day 68 add 1.OA.D.8: applied.** Re-cutting the s03
  section labels waits for the next skeleton run.
- **1.NBT.B.2a on days 69 and 87, 1.NBT.B.2b on day 74: applied.**
- **Loose-piece safety, days 69 to 91 and 96 to 109: applied** (as one sentence, "Keep loose pieces out of mouths,
  and adults count pieces back in.", since the skeleton splits a cell at semicolons).
- **1.NBT.C.5 on days 119, 120 and 128: not applied** (undone, see above). It needs an s06 field 2 line and a day 128
  field 5 item first. The optional day 148 prompt was not added.
- **Day 120 add 1.NBT.C.4; supplies on days 113, 128 and 146; tape diagram on days 155 and 156: applied.**
- **Days 54, 119 and 135 kinds: not applied.** A kind change moves the unit's balance line in field 2 and the section
  skeleton counts; day 54's item leaves the call to the lead. For the lead, with the next skeleton run.
- **Days 139, 140 and 146 notes and the scope (unit 7 paragraph and year-end row): applied.** Day 139's comparison
  is descriptive first-teaching evidence; the scored part comes from S1 on day 146.
- **Days 137 to 140 supplies: applied** (overlays or tracing-paper copies added; blunt scissors replaced by
  teacher-precut shapes).
- **Days 154 and 156 goals: applied** (US "labeled").
- **Frame and s04 skel, collections from home: applied.** "Request no collections from home; use the class supply."
  The run-on with "Standards in full" was in the frame cell itself, now a separate sentence; the generator needs no
  change.
- **Source map Food Drive "keep" to "change": not applied** ("change" is not a decision value).
- **unit_skeleton.py Weight line, file name only: not applied.** The grade 6 read asks the same as an open question;
  whether internal plans may name the organization is a lead call, and the line sits in every math plan.

### Grade 2

- **F1, maintained codes: applied, option (b)** (the read's recommendation; an item-level choice). Field 5 of s03 to
  s06 now opens with "Items on maintained codes are maintenance evidence for response groups and the handoff, not
  part of this unit's score."
- **F4, grade 3 s01 field 4: applied** (read the grade 2 day 160 handoff record if supplied).

### Grade 3

- **Days 81, 84, 86, 88, 90 and 147 notes: applied.** Day 90 also takes US "modeling".
- **Scope unit 5 paragraph: applied.**
- **Source map "groupss": no longer holds** (the row reads correctly).

### Grade 5

- **Day 154 note, one decimal divided by a decimal to hundredths: applied.**
- **"Progression skills owned" built from frame ownership: not applied.** It changes the shared generator's ownership
  for every math, ELA and science course, and the same list feeds begun codes and Builds on. For the lead, with tests.

### Grade 6

- **Days 28 and 29 (coordinate-plane), 65 (number-line), 71 (goal and area-model), 94 and 95 (place-value-chart),
  103 (tape-diagram; equation-balance), 130 (tools and grid paper): applied.** Ratio-table stays on days 28 and 29.
- **Days 49, 58 and 59 tools cut to two parts: not applied.** The read does not say which two, and day 49's plan row
  lets the student choose paper tools.
- **"On a 45-minute period" boilerplate: applied** on all 38 days that carried it, not only 49, 57, 58 and 59: the
  course period is 50 minutes (frames.csv). Other "45-minute path" lines were left.
- **Supplies on days 142, 144, 148, 149, 150 and 153: applied.**
- **Day 93 ruler, day 106 kind, days 90 and 91 kinds, s01 Sequence 2 tool decisions, a Fermi day: not applied.**
  Each is a choice for the lead.
- **US spelling in notes: applied** (one "labelled" left; the other words were already fixed).
- **Generator items: applied in part.**
  - The s08 hazard pointer: applied in the s08 skel line; the frame keeps its own cross-reference.
  - The Practices line "stops after MP2": not applied. The frame cell itself reads "MP6 (units and precision), MP2",
    so nothing is cut.
  - The s02 sensitive line ending in "Standards in full": not applied; it needs the frame cell read with the unit's own
    parts.
  - The s06 source-map summary filter and the Weight line naming: not applied; generator changes for the lead.
  - The s04 assumed-rows table (m5-fraction-area): not applied; it needs a progression assumes change, outside a
    structure edit.
- **Source map 6.5.14 and 6.4.17: not applied** ("change" is not a decision value).
- **Sources: not applied.** Lead lookups (IM 6.1.11, a fixed progression edition, a US school safety guide, license
  and NIST lines, the Number System draft).
- **Grade 7 s01 Handoffs, "the unit plans are unwritten": no longer holds** (the line is gone).

### Grade 7

- **Scope focus paragraph, one rule for assessment-production minutes: not applied.** It is a counting-rule choice,
  and the recount cannot be checked from the scope alone. The 65 percent line holds under either rule. For the lead.

### Grade 8

- **Day 18 (8.G.A.5, the ten-minute angle argument and peer feedback in goal and note), day 19 note, day 49
  (8.EE.B.6): applied.** s01 and s03 pass.
- **Scissors safety on days 2 to 5, 8 to 14, 18 and 19: applied**, from s01 field 8.
- **Day 114, "Pump" to "Tank" and a calculator: applied.** The plan calls the day 102 model the Tank model
  throughout, so days 102, 103 and 104 were renamed too, to keep days.csv consistent.
- **Day 37 "rule" to "ruler": no longer holds.**
- **Days 132 to 135 (place-value chart dropped) and 152 to 157 (square grid, ruler, day 156 hundredths line):
  applied.**
- **Not applied, lead choices:** day 15's section; days 25 and 26 turn-rule teaching; one tools-column rule for
  coordinate-plane and equation-balance; unit 3 and unit 4 section spans; the kinds of days 75, 76, 77, 79, 86 and 87 and
  of days 123 to 125, 129 and 130; day 92's 6.EE.A.1 (no change is named); the day 92 to 105 readiness timing; the day 118 and 123 minutes.
- **Source map U2 L7, L8, L13 and U7 L16: not applied** ("change" is not a decision value).
- **Sources: not applied.** Lead lookups (official Progressions host and edition, a school scissors safety source,
  the Utah cover edition).

### Kindergarten

- **Item 1, day 36 codes: not applied** (undone, see above).
- **Item 2, K.CC.A.3 off days 19, 20 and 25: not applied** (undone, see above). The read's other path, a labeling
  task on each day, is for the section plans.
- **Items 3 and 4, day 52, 56 and 89 kinds: not applied** (the field 2 Rigor line and section counts move with them;
  for the lead with the next skeleton run).
- **Item 5, "rubbings": applied** in day 118, the scope and the frame (with the s06 skel copy): "uses crayon marks;
  no ink and no printing of a finger".
- **Item 6, day 136 goal: applied.**
- **Item 7, safety column: applied** on days 1 to 5, 17, 58 to 62, 118, 140 and 141 (small pieces) and day 56
  (pouring). The scope's sentence now says math fills the optional column.
- **Item 8, supplies: applied for days 116 to 118** (pencils, paper mats, paper sheets). **Not applied for days 58 to
  62:** strips, tubs, vessels and water do not fit those shape days (naming, composing and turning shapes); the item
  may mean the building and pouring days 52 to 56.
- **Item 9, day 135 note: applied** ("Same-year retrieval, unscored").
- **Item 10, one course safety guide: not applied** (a source lookup).
- **Item 11, "Why this unit, here" truncated: not applied, no fault.** The generator prints the frame cell whole;
  the K frame cells simply end without a period.
- **Item 12, where U3 to U11 fields live: not applied** (a template decision for the lead).
- **Item 13, major-work table: applied** (unit 3 110, unit 8 833, total 6433, 80.7 percent).

## For Cory

None. All eleven course reads say nothing came up on scope, audience, money or people. The grade 8 read notes that
unit 6's 63.16 percent focus share is a course balance matter for the lead, not a question for Cory.

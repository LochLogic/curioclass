# Frame read: science-grade-8 (Science, grade 8), 2026-11-14

Expert read under docs/pipeline/briefs/frame-read.md. I did not write this frame.

## What I read

- docs/courses/science-grade-8/frame.md (whole), with docs/courses/science-grade-7/frame.md before it and
  docs/courses/biology/frame.md after it (seams only), and the grade 6 frame's shared source map and loss check.
- data/progressions/science.csv: all 26 grade 8 rows, and the grade 7 and biology rows the seams name.
- docs/pipeline/briefs/frame-write.md (the 15 lessons), docs/agents/EXPERT.md, docs/agents/lenses/science.md,
  docs/RUBRIC-SCIENCE.md (S5, S6, S11, S12), docs/agents/decisions/DESK-ANSWERS.md (science entries 2026-11-12 and
  2026-11-13), docs/sources/BASE-TEXTS.md.
- data/progressions/math.csv and the math grade 6, 7 and 8 frames (for "no math ahead of math").
- The base text in S:\CurioClass-sources\openscied-ms: every grade 8 unit's storyline (lesson lists and lesson
  days), each unit page's expectation list, and the Teacher Editions of 8.1, 8.2, 8.3 and 8.5 (extracted from the
  full-unit zips into the scratchpad and searched).
- Gates: `python -X utf8 scripts/frame.py check science-grade-8` (0 failures), `python -X utf8 scripts/plan.py
  check` (exit 0; science progression 198 rows, 0 failures), `python -X utf8 scripts/stale.py check` (0 failures).
- NGSS performance expectations, clarification statements and assessment boundaries: judged from my own knowledge
  (data/standards/ngss-pes.txt holds codes only). Where a finding rests on that knowledge it says so.

## Verdict

Fix first, then go. The frame is well built: the source map matches the base exactly (lesson counts and days for
all six units), the order is OpenSciEd's as the Desk asked, 26 codes sit on 26 rows, the checks have respond days,
and evolution, the paper path and the Deaf reader for unit 2 are handled. But the loss check is wrong in two places
that matter: base unit 8.3 teaches magnetism only, so the electric and gravitational parts of MS-PS2-3, MS-PS2-5 and
MS-PS3-2 have no base lessons and no days, and base 8.5 never teaches the cell parts MS-LS1-2 needs. With those
additions and twelve dormant readiness checks, the year at 156 unit days is about a week and a half short, and the
"rounded up by a day" rule the brief states was not applied to any unit.

## Findings, most serious first

### 1. Unit 3 claims electric and gravitational parts the base never teaches (serious; firm)

**What is wrong.** Base 8.3 is about magnets only. Its Teacher Edition says so outright at lesson 12: the unit is
about forces at a distance, "but the focus is only on magnetism" (TE p. 216), with electricity left to an optional
extension (lesson 8 teacher reference, and a home-learning extension on charged objects, p. 204) and gravity moved to
8.4. The storyline has no charged tape, balloon, static or gravity lesson. Yet unit 3 owns MS-PS2-3 (electric and
magnetic forces), MS-PS2-5 (fields exist between objects that do not touch; the clarification names electrically
charged pith balls or tape as well as magnets) and MS-PS3-2 (potential energy changes with arrangement, with
magnetic, electric and gravitational examples), and the rows s8-fields and s8-potential-energy name charged tape,
balloons and lifting a book. The frame gives unit 3 the base's 27 days with nothing added, and says gravity is
treated there as "a start of MS-PS2-4", which the base does not do. The loss check says the base loses nothing.

**Why it matters.** Three owned expectations would be taught at their magnetic headline only (lesson 4 of the
brief: standards in full), and the unit writer would trust a loss check that is wrong.

**Fix (frame).** In unit 3, name two Curio Class additions with their days: (a) a static-charge investigation
(rubbed balloons, charged tape strips, pith balls or foil; about 2 days) that runs the same field and
force-at-a-distance questions on electric charge, including evaluating an experimental design (the MS-PS2-5 practice);
(b) gravitational potential energy by height (lifting a book, a ramp or drop), about 1 day, either in unit 3 or
at the start of unit 4's gravity lessons (base 8.4 lessons 14 to 17), with unit 3's text saying which. Remove "a
start of MS-PS2-4" from unit 3 unless (b) sits there. Add 3 days to unit 3 (see finding 2). Correct the loss check:
"8.3 teaches magnetism only; the electric and gravitational parts of MS-PS2-3, MS-PS2-5 and MS-PS3-2 are Curio Class
additions in unit 3 (and unit 4)." Safety line for (a): no hazard beyond latex balloons (name a latex-free choice).

LAYER base text (and frame). REPEAT new.

### 2. The days do not carry the load, and the stated rounding rule was not applied (serious; firm on the arithmetic, judgment on the size)

**What is wrong.** Base days times 0.9 give 26.1, 21.6, 27.0, 27.9, 25.2 and 27.9 (155.7). The frame sets 26, 22, 27,
28, 25, 28: units 1 and 5 sit just under their base time, and no unit is "rounded up by a day where the rows add a
readiness check or a model reactivation" as the course in brief says, though every unit adds one. The year carries
twelve dormant readiness checks (s4-collisions, s3-balanced-forces, s4-speed-energy, s4-wave-model,
s3-magnet-static, s4-energy-device, s3-inherited-traits, s3-environment-traits, s3-fossils,
s3-variation-advantage, s3-habitat-survival, s3-animal-groups), about nine retrieval openers, four reactivations
(force diagram, wave model, light ray, Earth-sun-moon), a safety reteach, and now the additions in findings 1 and 3.
The pick under For the lead item 2 (reteaches as small-group work inside unit time) changes the row contract (the
rows' readiness checks come with a one-lesson reteach) and in practice pulls students out of whole-class storyline
lessons, which OpenSciEd's sequence does not allow for. My estimate: about 8 days short.

**Why it matters.** Lesson 9 of the brief (days by load). Grade 8 is the year the scope and sequence will overrun,
and the overrun would land on the storyline or on the reteaches.

**Fix (frame).** Add days by load and state the reason: for example unit 1 +2 (two readiness checks, force-diagram
reactivation, safety), unit 2 +1, unit 3 +3 (finding 1), unit 4 +1, unit 5 +2 (three readiness checks and finding 3),
unit 6 +1; about 166 in units and 170 in the year. That is over the 160 yardstick, so the year length goes to Cory
with the minutes-per-lesson question (For the lead item 1), with this frame's pick stated: either 170 days, or hold
160 by cutting named base lessons (the frame must then name which, and the loss). Change the course-in-brief
sentence so it says what was actually done. Replace For the lead item 2 with the new arithmetic.

LAYER frame. REPEAT yes (days by load, social studies lesson 9).

### 3. MS-LS1-2 is owned in unit 5, but base 8.5 never teaches cell parts (moderate; firm on the base, likely on the standard)

**What is wrong.** s8-cell-parts-function owns MS-LS1-2 (a model of how the cell as a whole and its parts, the
nucleus, chloroplasts, mitochondria, cell membrane and cell wall, function; from my knowledge of the PE and its
clarification) in unit 5. The 8.5 unit page marks LS1-2 as partial (starred), and the Teacher Edition names the
nucleus only as where chromosomes sit and touches the membrane and cell wall only in the strawberry DNA lab (pp. 245
to 253). No lesson builds the whole-cell model, and the frame adds no time.

**Why it matters.** A full owned expectation with no lesson behind it (brief lesson 4).

**Fix (frame).** In unit 5, name a Curio Class addition of about 1 day near base lessons 5 and 6 (where chromosomes
and the nucleus first come up): students build and revise a whole-cell model (plant and animal) naming each part's
function, using the grade 6 cell model as the start. Say it in the unit text and the loss check. Moving the owner to
another course would be a progression change for Cory; I do not recommend it.

LAYER base text (and frame). REPEAT new.

### 4. MS-PS4-2 is misdescribed in units 2 and 4 (moderate; firm)

**What is wrong.** Unit 4 owns MS-PS4-2 (through s8-earth-sun-moon) but describes only "the moon seen by reflected
sunlight". The row and base 8.4 teach a wave model of light: the red moon in a lunar eclipse, scattering shown in a
milk-water "atmosphere", sunrise colours, rainbows and colour-dependent bending, light crossing empty space. Unit 2
calls sound's reflection and absorption a "review of MS-PS4-2's part from grade 6", but grade 6 taught light only;
the mechanical-wave half (reflected, absorbed or transmitted through materials) is new in 8.2, and "transmitted" is
not named.

**Fix (frame).** Unit 4: "MS-PS4-2 completed: light as a wave reflects, is absorbed, is transmitted and bends
(scattering, eclipse colours, rainbows), and crosses empty space." Unit 2: "MS-PS4-2's mechanical-wave part, new
here: sound is reflected, absorbed or transmitted by materials." Match the seam line.

LAYER frame. REPEAT yes (standards in full).

### 5. MS-LS1-8's part in unit 1 and its concussion content are missing (moderate; firm)

**What is wrong.** Base 8.1 teaches touch receptors, signals to the brain and memories, and lessons 6 and 15 deal
with concussion (headgear in cheerleading and sport). The frame's unit 1 names neither the MS-LS1-8 part nor a
teacher note on concussion; the brief names only grade 7 unit 1 as an earlier part of MS-LS1-8, though 6.1, 6.6 and
8.1 all carry parts. Unit 2 completes MS-LS1-8 from 8.2 lesson 12 (one day on ear structure and hearing loss), with no
named moment that draws the senses together.

**Fix (frame).** Unit 1: name "MS-LS1-8 part: touch receptors, signals to the brain, memory" and a sensitive-topic
note: "Concussion: students may have had one or know someone who has; no student story asked for; sports
examples, not personal ones." Unit 2: name a short synthesis task (part of a lesson) across sight, touch and hearing
that completes the expectation. Correct the earlier-parts list.

LAYER frame. REPEAT new.

### 6. Laser and speaker safety missing (moderate; firm)

**What is wrong.** 8.1 and 8.2 use a laser and a mirror (the 8.2 storyline uses them to make speaker vibration
visible; the 8.1 Teacher Edition mentions lasers often). Grade 6 names the control ("class 2, below eye level"); grade
8 names none. 8.3 takes apart speakers (sharp edges, strong magnets that pinch and harm phones and cards).

**Fix (frame).** Unit 1 and unit 2 teacher notes: "Laser: class 2 only, teacher-aimed or fixed, beam below eye level,
never at a face or shiny surface." Unit 3: "Speakers opened by the teacher in advance; strong magnets kept apart and
away from phones and pacemakers." Unit 5 (fertilization at chromosome level, cattle breeding): "Follow school health
policy; examples stay with animals and plants."

LAYER frame. REPEAT yes (lab safety, the lens).

### 7. Stale progression notes not raised under For the lead (minor; firm)

**What is wrong.** Two row notes say the wrong owner. s8-wave-amplitude-energy says MS-PS4-2 is "owned by
s6-light-paths"; s8-earth-sun-moon says it "completes MS-PS4-2 in substance (the code sits on s6-light-paths)", while
the standard column gives MS-PS4-2 to s8-earth-sun-moon. The grade 6 frame raised the s6-light-paths note; this one did
not raise its own.

**Fix (frame, For the lead, row change for the fixer).** s8-wave-amplitude-energy note: "MS-PS4-2: light part begun
in grade 6 (s6-light-paths), mechanical-wave part here, owned and completed by s8-earth-sun-moon." s8-earth-sun-moon
note: "Owns and completes MS-PS4-2 (light as a wave, after s6-light-paths and s8-wave-amplitude-energy)."

LAYER progression. REPEAT yes (lesson 15).

### 8. Models table: wrong rest periods (minor; firm)

**What is wrong.** "wave-model (rests in grades 5 to 7)": grade 6 unit 5 uses it (s6-digital-signals). The
force-diagram row's origin skips the grade 5 row (s5-gravity-down) that uses it.

**Fix (frame).** "wave-model: from s4-wave-model; used in grade 6 unit 5 (s6-digital-signals); rests in grade 7;
reactivated in unit 2." Add s5-gravity-down to the force-diagram line.

LAYER frame. REPEAT yes ("first" and thread claims checked against the grade before).

### 9. Smaller standards and math wording (minor; likely)

- Unit 3 does not name MS-PS2-5's practice (plan and evaluate the experimental design); covered once finding 1 is
  fixed.
- Unit 6 does not name MS-LS4-1's assumption that natural laws worked in the past as they do today; add it.
- Unit 4: "powers of ten beyond math 8 are given ready-made" is unclear. Math 8 teaches scientific notation in unit
  7 (days 119 to 138), after unit 4. Write: "No scientific notation: distances written out in full or as powers of
  ten (5.NBT.A.2); ratios and scale drawings from math 7."
- Cross-subject: the scatter-plot "if later" lines can now say "Available: math 8 unit 4, days 56 to 60" (math 8 moved
  scatter plots there). The square of speed (6.EE.A.1) and probability for crosses (7.SP.C) are taught earlier: right.

LAYER frame. REPEAT yes (standards in full, no math ahead of math).

### 10. The earlier Codex read is stale (minor; firm)

docs/reviews/frame-science-grade-8-codex-2026-11-14.md withheld its verdict because the plan gate failed. The gate now
passes. Fix: the caller adds a line to that report: "Superseded: the plan gate passes as of 2026-11-14; see
frame-science-grade-8-2026-11-14.md." LAYER process. REPEAT yes.

## Checked and found right (do not undo)

- Source map: 8.1 33 days (29 without optional lesson 16), 8.2 24, 8.3 30, 8.4 31, 8.5 28, 8.6 31; lesson ranges match
  the storylines. Leaving out 8.1 lesson 16 (optional pitch and scale prototype) is right; it owns nothing.
- The 0.9 scaling (45 to 50 minutes) is the right method; the arithmetic is right; only its application is short.
- Order kept as OpenSciEd's, per the Desk answer; MS-LS1-4 begun in unit 5 and owned in unit 6 follows the base.
- 26 codes on 26 rows; MS-PS3-5 applied in unit 3 and owned in grade 6, marked as review.
- Course checks after units 3 and 6, each with a respond day; check-set cells start "Candidate:"; time stated.
- Seams with grade 7 and biology match the rows' assumes and hands_on (for example s8-senses-brain to
  bio-homeostasis-feedback).
- Evolution taught as science per BASELINE rule 5 with a teacher note; a reader from the Deaf and hard of hearing
  community named for unit 2; paper path and no accounts.

## Cross-subject

- Math 6 to 8: the frame uses nothing ahead of math once the unit 4 wording in finding 9 is fixed. Math 8's reopen
  condition (science 8 placing both scatter-plot uses after day 120) is not met.
- ELA 8 frame is not written; the writing and argument leans are recorded as needs, which is right.

## The lens checklist (course frame layer)

| Check | Result |
|---|---|
| Phenomena named per unit | Met |
| Storyline order and reasons | Met |
| Models carried and revised | Met, with finding 8 |
| Standards in full | Missed: findings 1, 3, 4, 5 |
| Days by load | Missed: finding 2 |
| Safety (hazards and controls) | Missed: finding 6 |
| Materials paths (kit, low-cost, no-kit) | Met |
| Sensitivity | Met, with finding 5's concussion note |
| Math and ELA in step | Met, with finding 9 |
| Seams both ends | Met |

## What I could not judge

- Whether 160 days or about 170 is right for the year: a time question for Cory.
- Classroom timing of the base lessons at 50 minutes; only a pilot shows that.
- NGSS clarification and boundary wording was not re-read from the source text this session.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Electric charge and gravitational energy taught as named Curio Class additions in unit 3 (and unit 4) | Base 8.3 is magnets only; three owned expectations need them | docs/courses/science-grade-8/frame.md |
| Whole-cell model added in unit 5 near base lessons 5 and 6 | Base 8.5 marks LS1-2 partial and builds no cell model | docs/courses/science-grade-8/frame.md |
| Reteaches stay whole lessons, not small-group work inside unit time | The row contract names a reteach lesson; storyline lessons are whole-class | docs/courses/science-grade-8/frame.md |
| Leave out 8.1 lesson 16 | Optional in the base, owns nothing | docs/courses/science-grade-8/frame.md |

## For Cory

1. Year length for grade 8: about 170 teaching days at 50 minutes (the load), or 160 with named base lessons cut. It
   goes with the minutes-per-lesson question already in the frame.
2. A science teacher's safety and materials read and a Deaf and hard of hearing reader (who, and any pay), as the
   frame says.

## Sources

- S:\CurioClass-sources\openscied-ms: grade 8 storylines and unit pages; Teacher Editions of 8.1, 8.2, 8.3, 8.5
  (8.3 TE pp. 204, 216; 8.5 TE pp. 23, 245 to 253).
- data/progressions/science.csv and math.csv; math grade 6 to 8 frames.
- NGSS middle school performance expectations, from my knowledge.

## For the source list

- The OpenSciEd full-unit zips hold the Teacher Editions as PDFs; they extract and search well. The unit pages alone
  do not show which expectation parts a unit leaves to extensions; the Teacher Edition does.

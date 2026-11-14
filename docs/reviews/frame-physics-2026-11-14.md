# Frame read: physics (Physics, grade 11), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md, docs/pipeline/briefs/frame-write.md
  (the "Lessons from the social studies frames" list).
- The frame docs/courses/physics/frame.md and its row in data/plans/frames.csv (10 units, 160 days).
- The 20 phys- rows of data/progressions/science.csv, every row they assume (chem-, bio-, s6- and s8-); the frame
  before (docs/courses/chemistry/frame.md) and, for the subject's end, docs/courses/biology/frame.md and
  data/courses.csv (Earth and Space Science and Environmental Science stay electives).
- Same-year neighbours: docs/courses/english-language-arts-grade-11/frame.md (on disk); no Algebra II frame is on
  disk, so data/progressions/math.csv alg2- rows stand in. Earlier-year: docs/courses/algebra-i/frame.md,
  docs/courses/world-history-i/frame.md.
- data/standards/ngss-pes.txt (codes only; a script confirmed all 71 high school codes are owned once, and all 19
  HS-ESS codes once across the three courses: Biology HS-ESS2-7, ESS3-3, ESS3-4; Chemistry HS-ESS2-2, 2-4, 2-5, 2-6,
  ESS3-1, 3-2, 3-5, 3-6; Physics HS-ESS1-1 to 1-6, ESS2-1, 2-3). DESK-ANSWERS 2026-11-13 (q-hs-science-core).
- Gates: `python -X utf8 scripts/plan.py check` and `python -X utf8 scripts/frame.py check physics` (0 failures;
  10 units, 160 days, 149 in units, 11 for checks); `python -X utf8 scripts/stale.py check` (0 failures).
- **Standards in full** is judged from my own knowledge of the NGSS performance expectations, clarification
  statements and assessment boundaries, checked against each row's notes; nothing was fetched.

## Verdict

The frame is sound: all 20 rows are placed once, the order (motion, design, gravitation, energy, fields, waves,
light, stars, the solid Earth, Earth's age) builds each model before it is used, and the Earth and space fold-in is
complete: every HS-ESS expectation is owned once across the three courses and Physics' eight sit in units with the
waves, nuclear and thermal models they need. The biggest risk is that four of the folded-in Earth and space
expectations are narrowed in the units' text, most of all HS-ESS1-5, which loses its continental-crust half. The one
change that matters most is restoring the clarification parts the rows already name (finding 1).

## Findings, most serious first

### 1. Five expectations are narrowed in the units' text (moderate; firm, from memory and the rows)

LAYER frame. REPEAT yes (lesson 4, standards in full).

**What is wrong.**
- HS-ESS1-5 (unit 9). The clarification and the row give two patterns: oceanic crust older away from a mid-ocean
  ridge, and North American continental crust younger away from an ancient central core. The frame keeps only the
  sea floor.
- HS-ESS2-3 (unit 9). The row names three kinds of evidence: seismic maps, records of Earth's magnetic field (limits
  on outer-core convection) and high-pressure laboratory work on rock. The frame names seismic maps only.
- HS-ESS1-6 (unit 10). The row names the sizes and make-up of solar system bodies as evidence; the frame drops it.
- HS-ESS1-1 (unit 8). The row names energy moving outward from the core and slower, non-cyclic variations in the
  Sun's output; the frame has neither (only "reaches Earth as radiation", flares and the sunspot cycle).
- HS-PS3-2 (unit 4). The row's example is energy stored between charged plates; the frame says "a stretched spring
  or a field", which a writer can satisfy with springs alone. Its boundary "two objects" is HS-PS3-5's, not HS-PS3-2's.

**Why it matters.** These are the parts the unit writer will not find anywhere else, and the Earth and space
expectations are new to these courses since 2026-11-13; an adoption reviewer counts them by element (Gateway 2).

**Fix.** Unit 9: HS-ESS1-5 sentence ends "...to explain the ages of crustal rocks: oceanic crust older with distance
from a mid-ocean ridge, and North American continental crust younger with distance from its ancient central core
(HS-ESS1-5)"; HS-ESS2-3 sentence "with evidence from seismic wave maps, records of changes in Earth's magnetic field
(limits on convection in the outer core) and high-pressure laboratory experiments on rock (HS-ESS2-3)". Unit 10:
after "the oldest minerals" add "; the sizes and make-up of the planets, moons and asteroids". Unit 8: HS-ESS1-1
sentence "...fusion in its core releases energy that moves outward through the Sun and reaches Earth as radiation,
with evidence from the masses and lifetimes of other stars, solar flares, the 11-year sunspot cycle and slower
variations over centuries (HS-ESS1-1)". Unit 4: "energy stored by height, in a stretched spring, and between two
charged plates (HS-PS3-2)"; boundary "two objects (HS-PS3-5)".

### 2. Kepler's third law invites fractional exponents, which Algebra II teaches the same year (minor; likely)

LAYER frame. REPEAT yes (lesson 13, no math ahead of math).

**What is wrong.** "Rearrange orbital relations to find a period or distance" (unit 3, weeks 7 to 10) leans only on
A-CED.A.4. Solving T squared = a cubed for a period or a distance in one step is T = a to the 3/2 or a = T to the
2/3, rational exponents (N-RN.A.1, alg2-rational-exponents, Algebra II, grade 11). No Algebra II frame is on disk, so
the order is unknown, and the frame's "Algebra II runs the same year; no unit needs it" has no if-later line.

**Fix.** Math readiness bullet, add: "Kepler's third law is used as T squared = a cubed (years and astronomical
units): students square or cube, then take a square root or cube root with a calculator (grade 8, m8-roots); no
fractional exponents." Same line in unit 3's teacher note.

### 3. The days reasoning miscounts the idle handoffs (minor; firm)

LAYER frame. REPEAT new.

**What is wrong.** The Days bullet says "twelve of its handoffs come from grade 6 or 8 rows ... each needing a
readiness check and a one-lesson reteach". The Seams table shows nine dormant entries (six distinct grade 6 rows)
with a readiness check and reteach; the grade 8 handoffs are "content revisited, opens with retrieval", with no
reteach.

**Why it matters.** It is half the stated reason Physics keeps 149 unit days with 20 expectations; the count should
match the table it rests on. The days themselves are right (about 7.5 an expectation, close to Chemistry's 7.1).

**Fix.** "...and nine of its handoffs come from six grade 6 rows idle for five years, each with a readiness check and
a one-lesson reteach; the grade 8 rows, idle three years, open with retrieval."

### 4. "Where each thread ends" leaves out the life science and chemistry threads and miscounts the design cycles (minor; firm)

LAYER frame. REPEAT new.

**What is wrong.** As the last core science course, the table should close every thread of the subject. It closes
Physics' threads and climate, but not cells and genetics, evolution and ecosystems (which end in Biology) or
matter, bonding and reactions (which end in Chemistry). The engineering row says the design cycle runs "three times
in high school"; it runs four (Biology units 9 and 10, Chemistry unit 7, Physics unit 2). Unit 3's "Why" says it
"reactivates ... earth-sun-moon", but Chemistry unit 9 used that model the year before: it is retrieval.

**Fix.** Add two rows: "Life: cells, inheritance, evolution, ecosystems | grades K to 8; Biology | Ends in Biology
(units 2, 6, 7, 5) | no Physics row carries it" and "Matter and reactions | grades 2, 5, 7; Chemistry | Ends in
Chemistry (units 1 to 6, 8) | Physics unit 8 reuses the periodic table and fusion". Engineering row: "run four times".
Unit 3: "reactivates field-model and retrieves earth-sun-moon".

### 5. The electricity rule does not say which cells (minor; firm)

LAYER frame. REPEAT new.

**What is wrong.** "Battery voltage only" and "a wire across a battery gets hot (short taps only)" are right for a
1.5-volt alkaline cell, but a shorted lithium coin cell, rechargeable pack or phone battery can overheat or burn.

**Fix.** Labs and materials bullet: "Alkaline 1.5-volt cells only; never short a lithium, rechargeable or phone
battery." Unit 5 hazards: the same line.

### 6. Same-year notes are stale for ELA 11 (minor; firm)

LAYER process. REPEAT yes (lesson 15).

**What is wrong.** "Algebra II and ELA 11 run the same year; their frames are written later": the ELA 11 frame is on
disk and teaches informative writing in unit 2 (weeks 4 to 7) and argument in unit 3 (weeks 8 to 11), before Physics
units 6 to 8.

**Fix.** Intro: "ELA 11's frame gives the weeks below; Algebra II's frame is not on disk." The three ELA rows:
"Taught first (ELA 11 unit 2, weeks 4 to 7)" and "Taught first (ELA 11 unit 3, weeks 8 to 11)"; keep the model
explainer as support, drop the if-later.

## Checked and found right (do not undo)

- All 20 rows placed once; 149 + 11 = 160; a respond day after each check; 50-minute lessons stated.
- HS-PS2-1 to PS2-5, HS-PS3-5, HS-PS4-1 to PS4-5, HS-ESS1-2, HS-ESS1-3, HS-ESS1-4 and HS-ESS2-1 are taught with their
  practice, core idea and the examples their rows name, inside their boundaries (one dimension, two bodies, no
  calculus, qualitative light models, no quantum theory), from memory.
- The order holds: unit 6's seismic waves come before unit 9 (the row fix in For the lead item 2 is right; I checked
  phys-earth-interior-convection's assumes); Chemistry's fusion and half-life come before units 8 to 10; light
  (unit 7) before spectra (unit 8).
- No vectors, no trigonometry, motion in one dimension, the orbit model supplied and stepped: the right guard for a
  course with no calculus.
- Safety rules: no lasers, no ultraviolet lamps, gratings never at the Sun, drops from a low fixed height, eggs
  bagged, magnets named as a pinch hazard.
- Deep time (units 8 to 10) taught as the evidence shows, with readers named.

## Seams

From Chemistry: all twelve links picked up in the units Chemistry names. From Biology: ultraviolet and DNA in unit 7.
Grade 6 and 8 rows: each has the handoff kind its row states. Where each thread ends: finding 4.

## Cross-subject

Algebra I (earlier year) owns every code leaned on. World History I's Scientific Revolution (grade 9 unit 9) is
earlier-year retrieval, matched in the World History I frame. ELA 11: finding 6. Algebra II: finding 2; its periodic
modeling lean onto unit 6 has a two-way line.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| A performance expectation has no unit, or a unit claims one it only touches | Placement met; five narrowed in text (finding 1) |
| Grades 6 to 8: departure from OpenSciEd order | Not applicable |
| High school: band expectations with no owning course | Met: 71 codes owned once; HS-ESS 19 of 19 owned once |
| No unit names its anchor | Met |
| Safety | Met with one gap (finding 5); course safety page owed (For the lead 6) |
| Plain facts (BASELINE rule 5) | Met |

## The brief's lessons list

1 met; 2 met; 3 met; 4 missed (finding 1); 5 met (force-diagram and field-model reactivated in their first units);
6 one wording (finding 4); 7 met (phys-earth-interior-convection row fix); 8 one missing if-later (finding 2); 9 met;
10 met; 11 met; 12 met; 13 one gap (finding 2); 14 met (phone sensors never required); 15 missed (finding 6).

## What I could not judge

- The NGSS text itself (codes only; nothing fetched). The Algebra II order, which has no frame yet.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Kepler's third law as T squared = a cubed in years and astronomical units, roots by calculator | Keeps the unit inside grade 8 and Algebra I math | docs/courses/physics/frame.md, unit 3 |
| Alkaline 1.5-volt cells only | A shorted lithium or rechargeable cell can burn | docs/courses/physics/frame.md, Labs and unit 5 |
| Charged plates named as the HS-PS3-2 field case (qualitative) | The row's example; springs alone miss the field | docs/courses/physics/frame.md, unit 4 |

## For Cory

- People (as the frame says): a qualified science teacher's safety and materials read, and the readers for units 2,
  7 and 8 to 10. Who, and any pay, is yours.

## Sources

- NGSS high school performance expectations, clarifications and boundaries (2013): from memory, not re-fetched.
- The repository files listed under "What I read".

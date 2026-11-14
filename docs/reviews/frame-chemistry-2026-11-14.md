# Frame read: chemistry (Chemistry, grade 10), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md, docs/pipeline/briefs/frame-write.md
  (the "Lessons from the social studies frames" list).
- The frame docs/courses/chemistry/frame.md and its row in data/plans/frames.csv (11 units, 160 days).
- The 20 chem- rows of data/progressions/science.csv, every row they assume (bio-, s6- to s8-) and the phys- rows
  they hand on to; the frames before (docs/courses/biology/frame.md) and after (docs/courses/physics/frame.md).
- Same-year neighbours as written today: docs/courses/geometry/frame.md and docs/courses/world-history-ii/frame.md
  (unit weeks computed from their day counts); no ELA 10 frame is on disk. Earlier-year: docs/courses/algebra-i/frame.md,
  docs/courses/world-history-i/frame.md; data/progressions/math.csv.
- data/standards/ngss-pes.txt (codes only; a script confirmed every high school code is owned once, Chemistry 21).
  DESK-ANSWERS 2026-11-13 (q-hs-science-core). The progression reads and fixes of 2026-11-13 for science (the
  chem-energy-accounting boundary finding, expert 4 and Codex 3).
- Gates: `python -X utf8 scripts/plan.py check` and `python -X utf8 scripts/frame.py check chemistry` (0 failures;
  11 units, 160 days, 149 in units, 11 for checks); `python -X utf8 scripts/stale.py check` (0 failures).
- **Standards in full** is judged from my own knowledge of the NGSS performance expectations, clarification
  statements and assessment boundaries, checked against each row's notes; nothing was fetched.

## Verdict

The frame is sound in shape: all 20 rows and 21 expectations are placed once, the atom-out order builds each model
before it is used, the days are evenly spread (6 to 8 an expectation), and every seam with Biology and Physics
matches. The biggest risk is unit 5: its anchor (first-aid hot and cold packs) is dissolving and crystallising, not a
chemical reaction, and the frame does not carry the row's rule that HS-PS3-1 proficiency is a thermal system, so a
writer would build both HS-PS1-4 and HS-PS3-1 on the wrong case. The one change that matters most is naming the
reaction cases and the thermal case in unit 5.

## Findings, most serious first

### 1. Unit 5 builds two expectations on a case outside them (moderate; firm)

LAYER frame. REPEAT yes (the progression read's finding 4 on chem-energy-accounting, same kind).

**What is wrong.**
- HS-PS1-4 is about a chemical reaction system: release or absorption of energy follows the change in total bond
  energy. The anchor's packs are, in the common commercial kinds, a salt dissolving (cold pack) and a supersaturated
  solution crystallising (snap hot pack). Neither is a reaction, so neither is evidence for the bond-energy model;
  the unit names no reaction at all.
- chem-energy-accounting says the HS-PS3-1 proficiency case is a two- or three-component thermal system (a
  calorimeter, mixing water, a warming pond) and Earth's surface energy budget, with any chemical-reaction energy
  accounting a labelled extension, outside the HS-PS3-1 boundary. The frame's HS-PS3-1 sentence names no case and
  keeps the hot-pack anchor, so the obvious build is a reaction-energy spreadsheet. The Earth's surface budget case is
  placed nowhere (unit 9 does not claim HS-PS3-1).
- HS-PS1-4's boundary excludes calculating total bond energy changes; the frame says "no calculating bond energies
  from tables beyond the row", which a writer can read as "some calculation is fine".

**Why it matters.** Writers build days from "What students learn"; this is a fault that becomes wrong days, and an
adoption reviewer marks a misplaced proficiency case under Gateway 2 and accuracy (2d).

**Fix.** Unit 5, "What students learn", replace the HS-PS1-4 sentence with: "A model, from two reactions run in
class (an air-activated iron hand warmer, which releases energy, and baking soda with vinegar, which absorbs it),
showing that release or absorption depends on the change in total bond energy; the packs of the anchor are then
explained as attractions between particles broken and formed (unit 2), a physical change, not a reaction (HS-PS1-4)."
Replace the HS-PS3-1 sentence with: "A computational model of a two- or three-component thermal system (a
calorimeter cup, mixing water, a warming pond) that finds one component's energy change from the others and the
flows in and out, each expression explained (HS-PS3-1); reaction-energy accounting is an extension, not
proficiency evidence." Boundaries: "no calculating total bond energy changes (HS-PS1-4)". Unit 9, add to its first
sentence: "and the unit 5 energy model applied to Earth's surface energy budget (HS-PS3-1, review use)". The
anchor and question can stay; the question is then answered in two parts.

### 2. Three Earth and space expectations are narrowed (moderate; firm, from memory and the rows)

LAYER frame. REPEAT yes (lesson 4, standards in full).

**What is wrong.**
- HS-ESS2-4 (unit 9). The clarification and the row name four timescales; the frame stops at tens of thousands of
  years and drops the fourth, long-term changes in atmospheric composition over millions of years.
- HS-ESS3-6 (unit 10). The row names effects on shellfish and marine populations and the boundary that students use
  published results of scientific models and do not run them. The frame drops the marine effects and writes
  "provided multi-parameter models", which is HS-ESS3-3's boundary, not this one, beside a stock and flow tool
  students run.
- HS-ESS2-5 (unit 3). The row names "melting with water present" as an investigation; the frame lists "lowers the
  melting point of rock" as a property but gives no investigation or data path for it, and drops erosion with soil
  moisture.

**Fix.** Unit 9, HS-ESS2-4 sentence: after "(orbit changes, ice ages)" add "to millions of years (long-term changes in
the atmosphere's make-up, calling back to Biology unit 8's oxygen story)". Unit 10, HS-ESS3-6 sentence: end with
"with effects on shellfish and marine populations; students read the published results of scientific models and do
not run them (the stock and flow tool serves HS-ESS2-6 only)". Unit 3: add "melting with water present read from
provided laboratory data on wet and dry rock melting temperatures (no heating of rock); erosion compared at two soil
moistures on the stream table".

### 3. Same-year notes are stale: the Geometry and World History II frames now exist (minor; firm)

LAYER process. REPEAT yes (lesson 15).

**What is wrong.** "Geometry, ELA 10 and World History II run the same year; their frames are written later" and For
the lead item 2 ("the World History II frame should state its weeks") are out of date. World History II states its
weeks: industrial revolution unit 2 (weeks 4 to 6), atomic bombs unit 6 (weeks 15 to 18), twentieth-century science
unit 9 (weeks 25 to 27), global problems unit 11 (weeks 29 to 32), and it already bridges fission itself. Geometry
teaches N-Q.A.2 and N-Q.A.3 in unit 4 (about weeks 14 to 17) and geo-modeling-objects-density (N-Q.A.1) in unit 5
(about weeks 17 to 21).

**Fix.** Cross-subject intro: "Geometry and World History II run the same year and their frames give the weeks
below; ELA 10's frame is not on disk, so its leans keep their if-later lines." Geometry table: unit 2 and unit 4
leans, "Geometry teaches it in weeks 14 to 21, after this unit: the if-later line applies"; unit 7 lean "concurrent
(Geometry unit 5, weeks 17 to 21): the if-later line applies"; unit 10 and 11 leans "taught before (Geometry units 4
and 5)". Leans onto this course: wh2-atomic-bombs and wh2-science-20th-century, "World History II is earlier (weeks
15 to 18, 25 to 27) and bridges fission itself; unit 8 calls back to it". Drop For the lead item 2.

### 4. Safety: eye protection and disposal are not a course rule (minor; firm)

LAYER frame. REPEAT new.

**What is wrong.** Eye protection is named in units 1, 2, 4 and 6 but not unit 5 (hot water, packs, and the two
reactions of finding 1) or unit 10 (indicator). Unit 1's copper with vinegar and salt makes a copper salt solution
with no disposal line; steel wool splinters with no gloves line.

**Fix.** Labs and materials bullet, add: "Eye protection on every hands-on day that uses a liquid, heat or a chemical.
Copper solutions are collected in a labelled jar, never poured down the drain. Steel wool is handled with gloves."
Unit 5 hazards: add "eye protection".

### 5. Unit 8's anchor compares with a power station that does not exist (minor; likely)

LAYER frame. REPEAT new.

**What is wrong.** "A sun-sized power station would need far less fuel than a coal plant" names no real thing:
there is no fusion power station, and "sun-sized" is not what is meant.

**Fix.** Settled below: "a uranium fuel pellet the size of a fingertip releases about as much energy as a tonne of
coal".

### 6. The Models carried section names the wrong last carriers and calls a retrieved model idle (minor; firm)

LAYER frame. REPEAT new.

**What is wrong.** The rows show water-cycle last carried by s7-climate-change-evidence (grade 7) and rock-cycle by
s7-resource-distribution (grade 7); the table names grade 6 rows. The intro says plate-model is reactivated in unit 3
"idle since grade 6, for plate-model since Biology unit 8", but Biology unit 8 used it the year before, so it is
retrieval, not reactivation.

**Fix.** Table cells: water-cycle "last carried by s7-climate-change-evidence (grade 7)"; rock-cycle "last carried by
s7-resource-distribution (grade 7)". Intro: "Three models were idle in Biology and get a reactivation task in the first
unit that uses them: water-cycle and rock-cycle in unit 3 (idle since grade 7), earth-sun-moon and wave-model in unit
9 (idle since grade 8). plate-model returns from Biology unit 8 with a retrieval task in unit 3."

## Checked and found right (do not undo)

- All 20 rows placed once; 149 + 11 = 160; respond days after each check; 50-minute lessons stated.
- HS-PS1-1, PS1-2, PS1-3, PS1-5, PS1-6, PS1-7, PS1-8, HS-PS2-6, HS-PS3-3, HS-PS3-4, HS-ETS1-2, HS-ESS2-2, HS-ESS2-6,
  HS-ESS3-1, HS-ESS3-2 and HS-ESS3-5 are taught with the practice, core idea and examples their rows name, inside
  their boundaries (from memory).
- No math ahead of math: the mole uses grade 8 scientific notation; rearranging is Algebra I; pH is powers of ten
  with no logarithm (Algebra II comes in grade 11); half-life uses Algebra I's exponential decay.
- "No open flame anywhere" is the right course rule; reactive metals by video only; no radioactive source.
- Every hands_on link to Physics is picked up in the Physics unit this frame names (units 2, 3, 4, 8, 9, 10).
- Days follow load (single-expectation Earth units at 10, the three-expectation units at 18).

## Seams

From Biology: all nine Biology links are picked up in the units the Biology frame names (5, 7, 9, 10, 11). Grade 6 to
8 rows that skip Biology open with retrieval or a readiness check, as the rows' handoff kinds say. To Physics: twelve
links, each matched to the Physics frame's "Picked up" table.

## Cross-subject

Algebra I (earlier year) owns every algebra and statistics code leaned on. Geometry and World History II: finding 3.
World History I's wh1-geography-shapes-contact (grade 9 unit 1) is earlier-year retrieval, matched in the World
History I frame.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| A performance expectation has no unit, or a unit claims one it only touches | Placement met; one misplaced case (finding 1) and three narrowed (finding 2) |
| Grades 6 to 8: departure from OpenSciEd order | Not applicable |
| High school: band expectations with no owning course | Met (71 codes owned once) |
| No unit names its anchor | Met |
| Safety | Partly (finding 4); course safety page owed (For the lead 6) |
| Plain facts (BASELINE rule 5) | Met: climate taught as the evidence shows, with the models' own uncertainty |

## The brief's lessons list

1 met; 2 met; 3 met; 4 missed (findings 1 and 2); 5 met (readiness checks sit in the first unit that uses each row);
6 met; 7 met; 8 met; 9 met; 10 met once unit 5 names its reactions; 11 met; 12 met; 13 met; 14 met; 15 missed (finding
3).

## What I could not judge

- The NGSS text itself (codes only in the repository; nothing fetched). Whether the classroom-cheap kit list fits a
  real school budget; the unit plans state cost.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Unit 5 reactions: air-activated iron hand warmer (releases) and baking soda with vinegar (absorbs) | Real reactions, household, flame-free, both directions | docs/courses/chemistry/frame.md, unit 5 |
| Unit 5 thermal case: calorimeter cup, mixing water, a warming pond | The row's proficiency case for HS-PS3-1 | docs/courses/chemistry/frame.md, unit 5 |
| Unit 8 anchor: a fingertip-sized uranium pellet against a tonne of coal | Accurate and real | docs/courses/chemistry/frame.md, unit 8 |
| Unit 3 melt generation from provided wet and dry melting data | No heating of rock in a classroom | docs/courses/chemistry/frame.md, unit 3 |

## For Cory

- People (as the frame says): a qualified science teacher's safety and materials read for every hands-on day, and a
  reader for units 8 to 11. Who, and any pay, is yours.

## Sources

- NGSS high school performance expectations, clarifications and boundaries (2013): from memory, not re-fetched.
- The repository files listed under "What I read".

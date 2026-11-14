# Fixes: high school science course frames (Biology, Chemistry, Physics), after the cold reads (2026-11-14)

Applies the expert reads (`frame-<course>-2026-11-14.md`) for Biology, Chemistry and Physics to the three frames and
`data/progressions/science.csv`. Every expert finding and every "Settled by the expert" row is applied. The three
Codex reads (`frame-<course>-codex-2026-11-14.md`) withheld their verdicts over a gate failure in the review
environment and hold no curricular finding: each is listed as blocked, rerun pending (a rerun writes
`frame-<course>-codex-rerun-2026-11-14.md`; a short follow-up pass applies it). The writers' own "For the lead" items
were weighed on their merits.

Gates after the fixes: `scripts/frame.py sync` (52 courses); `scripts/frame.py check biology chemistry physics` 0
failures each; `scripts/progression.py check science` 198 rows, 0 failures (advisory notes unchanged);
`scripts/stale.py check` 56 files, 0 failures; `scripts/plan.py check` exit 0. Every course keeps its unit count and
total days (Biology 10 and 160, Chemistry 11 and 160, Physics 10 and 160; 149 in units, 11 for checks each).

Same-year neighbours read for the weeks: Algebra I, Geometry and Algebra II (unit weeks computed from their day
counts), ELA 9, 10 and 11, World History I and II. Two facts in the expert reads were out of date or off and are
corrected here: the ELA 10 frame is now on disk (Chemistry's ELA leans now cite its weeks), and World History II's
twentieth-century science unit (weeks 25 to 27) comes after Chemistry unit 8 (weeks 21 to 23), not before; only its
atomic bombs unit (weeks 15 to 18) is earlier.

## Biology

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Unit 1 14 to 13, unit 2 13 to 12, unit 4 12 to 11, unit 9 15 to 17, unit 7 17 to 18 (149 kept); bio-group-behavior about three days; week labels recomputed (units 1 to 10: 1-3, 3-5, 6-9, 10-12, 12-15, 16-19, 19-23, 23-25, 25-28, 29-31; checks weeks 9 to 10, 16, 32); Days bullet gives the reason; every week in Cross-subject updated |
| Expert | 2 | Applied | HS-LS2-6 sentence (stable, modest change absorbed, extreme change makes a new ecosystem, scale of evidence) and HS-LS1-6 sentence (explanation from models and a simulation, revised on the dry-mass evidence) as given |
| Expert | 3 | Applied | Cross-subject intro names the Algebra I and ELA 9 frames; e9-w-informative pick replaced; unit 10 "are taught (Algebra I unit 5, weeks 17 to 22)"; ELA 9 unit 7 line under Hard content; old lead item 4 dropped. ELA 9 rows now cite its unit 6 (weeks 20 to 24) and unit 7 (weeks 24 to 26) and say the if-later line applies |
| Expert | 4 | Applied | Unit 5 teaches the step rule (plus births minus deaths, each a percent) with a worked table from grade 7 percent, in the unit row, the Algebra I lean and the Math readiness bullet; unit 10's lean is "As unit 5: retrieval of the step rule"; the row's notes say the same |
| Expert | 5 | Applied | Unit 8 anchor: grains that did not rust then; younger sandstones laid down on land stained red |
| Expert | 6 | Applied | Food-grade dry beans (units 1, 3, 6 and the Labs bullet); seed bags sealed and thrown away sealed; medical-reason recording role in unit 1 |
| Expert | 7 | Applied | Unit 6: one gene sets black or chocolate, a second hides both; 9:3:4 from a 16-box square; no other gene interactions |
| Expert | 8 | Applied | plate-model last carried by s7-resource-distribution (grade 7) |
| Expert | 9 | Applied | bio-population-carrying-capacity notes: 21 in Chemistry |
| Expert | settled | Applied | All four rows |
| Codex | 1 | Blocked, rerun pending | Gate environment failure; no curricular finding |
| Writer | lead 1 | Updated | Days settled with the move; the HS-ESS3-4 relief is a scope question, collected for Cory |
| Writer | lead 2 | Applied | bio-define-human-impact-problem notes now name m6-unit-conversion for 6.RP.A.3d; frame cell cleaned |
| Writer | lead 3 | Applied | Food-web reactivation sentence (and its "rests in grade 8" line) moved from bio-population-carrying-capacity to bio-energy-pyramids; Models carried intro rewritten |
| Writer | lead 4 | Dropped | Settled by expert 3: both neighbours' weeks are now in the frame |
| Writer | lead 5 to 7 | Kept | People (for Cory), candidates, course safety page (now naming the new course rules) |

Counts: applied 9 expert findings plus 4 settled rows and 2 writer items; rejected 0; blocked 1 (Codex); for Cory 2.

## Chemistry

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Unit 5: two reactions run in class (air-activated iron hand warmer releases, baking soda with vinegar absorbs) build HS-PS1-4; the packs explained as a physical change; HS-PS3-1 on a calorimeter cup, mixing water and a warming pond, reaction accounting an extension; boundary "no calculating total bond energy changes"; unit 9 applies the energy model to Earth's surface budget (HS-PS3-1, review use) |
| Expert | 2 | Applied | HS-ESS2-4 adds millions of years (atmosphere's make-up, Biology unit 8 call-back); HS-ESS3-6 adds shellfish and marine populations and the published-results boundary (stock and flow tool serves HS-ESS2-6 only); unit 3 adds wet and dry melting data (no heating of rock) and erosion at two soil moistures |
| Expert | 3 | Applied | Intro names the Geometry, ELA 10 and World History II frames; Geometry rows cite unit 4 (weeks 14 to 17) and unit 5 (weeks 17 to 21) and say where the if-later line applies; World History II rows give its weeks; old lead item 2 dropped. ELA 10 rows now cite its unit 4 (weeks 13 to 17) and unit 7 (weeks 26 to 31) |
| Expert | 4 | Applied | Course rules in the Labs bullet: eye protection on every day with a liquid, heat or a chemical; copper solutions in a labelled jar, never down the drain; gloves for steel wool; eye protection added to units 3, 5 and 10; sealed hand-warmer kits |
| Expert | 5 | Applied | Unit 8 anchor: a fingertip-sized uranium pellet against a tonne of coal |
| Expert | 6 | Applied | water-cycle last carried by s7-climate-change-evidence, rock-cycle by s7-resource-distribution; plate-model is retrieval from Biology unit 8 (intro and unit 3) |
| Expert | settled | Applied | All four rows |
| Codex | 1 | Blocked, rerun pending | Gate environment failure; no curricular finding |
| Writer | lead 2 | Dropped | World History II states its weeks; the timing is now in Cross-subject (WH II unit 2 and unit 6 earlier, unit 9 and unit 11 later) |
| Writer | lead 3 | Dropped | The Geometry frame already carries a Chemistry availability table for N-Q.A.1 to A.3; the leans now cite its units |
| Writer | lead 1, 4 to 6 | Kept | Days; people (for Cory); candidates; safety page (now with the course rules) |

Counts: applied 6 expert findings plus 4 settled rows; rejected 0; blocked 1 (Codex); for Cory 1.

## Physics

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | HS-ESS1-5 both crust patterns; HS-ESS2-3 seismic maps, magnetic field records, high-pressure experiments; HS-ESS1-6 sizes and make-up of planets, moons and asteroids; HS-ESS1-1 energy moving outward and slower variations over centuries; HS-PS3-2 charged plates, boundary "two objects (HS-PS3-5)" |
| Expert | 2 | Applied | Kepler's third law as T squared = a cubed with roots by calculator (m8-roots), no fractional exponents: Math readiness, unit 3 teacher note, a new grade 8 lean (row and frame), and an Algebra II line (rational exponents in its unit 3, weeks 10 to 14, after Physics unit 3) |
| Expert | 3 | Applied | Days bullet: nine handoffs from six grade 6 rows with readiness checks; grade 8 rows open with retrieval |
| Expert | 4 | Applied | Two thread rows added (life ends in Biology, matter and reactions in Chemistry); design cycle run four times; unit 3 "retrieves earth-sun-moon" |
| Expert | 5 | Applied | Alkaline 1.5-volt cells only, in the Labs bullet and unit 5 |
| Expert | 6 | Applied | Intro names both frames; ELA 11 rows "Taught first" (unit 2, weeks 4 to 7; unit 3, weeks 8 to 11); Algebra II's periodic lean now says Algebra II unit 6 (weeks 23 to 28) calls back to Physics unit 6 |
| Expert | settled | Applied | All three rows |
| Codex | 1 | Blocked, rerun pending | Gate environment failure; no curricular finding |
| Writer | lead 2 | Applied in another form | The checker requires assumes at an earlier grade, so phys-wave-math cannot go in phys-earth-interior-convection's assumes. The same-course order is written in that row's notes and the frame's lead item 2 |
| Writer | lead 3 | Kept | data/standards/ccss-ela-standards.txt still lists no RST codes, so the Pending note stays true; adding the strand is a lead item |
| Writer | lead 1, 4 to 6 | Kept | Days; people (for Cory); candidates; safety page (with the alkaline rule) |

Counts: applied 6 expert findings plus 3 settled rows and 1 writer item; rejected 0; blocked 1 (Codex); for Cory 1.

## Progression changes (data/progressions/science.csv, 5 rows)

| Row | Change |
|---|---|
| bio-define-human-impact-problem | Notes: 6.RP.A.3d in m6-unit-conversion (was m6-ratio-parts-problems) |
| bio-population-carrying-capacity | Notes: "21 in Chemistry"; the step rule taught with a worked table before Algebra I's exponential unit; food-web reactivation and "rests in grade 8" sentences moved out |
| bio-energy-pyramids | Notes: the food-web reactivation and "rests in grade 8" sentences moved in (first row to use the model) |
| phys-orbits | cross_subject adds math:m8-roots; notes add Kepler's third law as T squared = a cubed, roots by calculator, and m8-roots under Math readiness |
| phys-earth-interior-convection | Notes: phys-wave-math is taught earlier in the same course; assumes lists earlier grades only |

No assumes or hands_on changed, so both ends of every handoff are as before; the grade 8 frame's Seams table needed
no edit.

## Cross-subject notes (for those frames' owners; not edited here)

- **ELA 9** (`docs/courses/english-language-arts-grade-9/frame.md`), Cross-subject intro: "the biology and Algebra I
  frames are written later" is stale. Biology's units now run: unit 5 weeks 12 to 15, unit 6 16 to 19, unit 7 19 to
  23, unit 8 23 to 25, unit 9 25 to 28. Its leans and bridges still hold (Biology unit 7 ends before ELA 9 unit 7).
- **ELA 10** (`docs/courses/english-language-arts-grade-10/frame.md`), intro: "the chemistry frame is written later"
  is stale. Chemistry unit 1 is weeks 1 to 4, unit 2 weeks 4 to 7, unit 9 (the forecast) weeks 23 to 26, so ELA 10
  unit 7 comes after the forecast and its if-later line is not needed.
- **World History II** (`docs/courses/world-history-ii/frame.md`): wh2-science-20th-century (unit 9, weeks 25 to 27)
  comes after Chemistry unit 8 (weeks 21 to 23), so its fission bridge can be a retrieval task; wh2-global-problems
  (unit 11, weeks 29 to 32) comes after Chemistry unit 9 (weeks 23 to 26), so its if-later line is not needed.
- **Algebra I** (`docs/courses/algebra-i/frame.md`), science table: the exponential unit's population lesson ("If
  Biology comes later") can now say Biology unit 5 (weeks 12 to 15) comes first and teaches the step rule.
- **Algebra II** (`docs/courses/algebra-ii/frame.md`): "Physics' own math leans ... are all Algebra I" now misses
  phys-orbits' grade 8 lean (m8-roots); Physics avoids rational exponents on purpose.
- Geometry and ELA 11 frames match this pass; no change.

## For the lead (outside this pass's files)

- RST.11-12.8: the standards inventory lists no science and technical reading codes; phys-wave-particle-light and
  phys-em-radiation-effects keep their Pending note until the strand is added.

## For Cory

- **People.** A qualified science teacher's safety and materials read for every hands-on day in all three courses;
  Biology units 6, 7 and 9 readers (including the Lower Elwha Klallam Tribe's published materials or a reader from
  the Tribe); Chemistry units 8 to 11; Physics units 2, 7 and 8 to 10. Who, and any pay.
- **Scope, only if needed.** If the Biology scope and sequence still runs short after the day moves, moving HS-ESS3-4
  to Chemistry unit 11. Not needed now.

## Settled (for docs/reviews/DIGEST.md)

| Choice | Course | Reason |
|---|---|---|
| Four days moved from units 1, 2 and 4 to units 9 and 7; bio-group-behavior three days | Biology | Design cycle and four-expectation units were short |
| HS-LS2-6 modest and extreme change; HS-LS1-6 revised on dry-mass evidence | Biology | Standards in full |
| Unit 5 teaches the step rule before Algebra I's exponential unit | Biology | Each thread starts where it is first used |
| Unit 8 anchor: red sandstones on land, not banded rocks | Biology | Banded iron formations are often older |
| Unit 6 anchor kept with the masking gene and the 9:3:4 litter | Biology | Answerable inside HS-LS3-3 |
| Food-grade dry beans; sealed seed bags; medical-reason recording role | Biology | Safety (S5) |
| Food-web reactivation carried by bio-energy-pyramids | Biology | First row to use the model |
| Unit 5 reactions: iron hand warmer and baking soda with vinegar; packs a physical change | Chemistry | HS-PS1-4 needs real reactions |
| HS-PS3-1 on a calorimeter cup, mixing water, a warming pond; Earth's budget as review use in unit 9 | Chemistry | The row's proficiency case |
| HS-ESS2-4 to millions of years; HS-ESS3-6 marine effects, published results only; wet and dry melting data | Chemistry | Standards in full |
| Eye protection, copper disposal and steel-wool gloves as course rules | Chemistry | Safety (S5) |
| Unit 8 anchor: a fingertip uranium pellet against a tonne of coal | Chemistry | Accurate and real |
| Crust ages both patterns; interior from three evidence kinds; body sizes; Sun's slow variations; charged plates | Physics | Standards in full |
| Kepler's third law as T squared = a cubed, roots by calculator | Physics | No math ahead of Algebra II |
| Alkaline 1.5-volt cells only | Physics | A shorted lithium or rechargeable cell can burn |
| Same-course order (wave unit before interior unit) recorded in notes, not assumes | Physics | assumes lists earlier grades only |

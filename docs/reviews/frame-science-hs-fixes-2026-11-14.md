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

## Codex rerun (applied 2026-11-14)

The three blocked Codex reads were rerun (`frame-<course>-codex-rerun-2026-11-14.md`) and weighed on their merits
against the frames as fixed above, the progression and the performance expectations in full. The expert's settled
rows stand except where noted (Biology 3, a standard's revision left unsupported). Gates after:
`frame.py sync` (52 courses); `frame.py check science-kindergarten science-grade-1 science-grade-8 biology chemistry
physics` 0 failures each; `progression.py check science` 198 rows, 0 failures; `stale.py check` 56 files, 0
failures. Every course keeps its units and days (Biology 10, Chemistry 11, Physics 10; 160 each, 149 in units).

### Biology

| # | Finding | Result | What was done |
|---|---|---|---|
| 1 | Unit 4 sends all remaining energy to respiration heat | Applied | Unit 4 and bio-energy-pyramids notes: a proportional budget telling apart energy built into the next level's biomass, respiration heat, and chemical energy in uneaten material and waste entering detrital and decomposer pathways; roughly a tenth is illustrative; atoms tracked apart from energy. 11 days kept |
| 2 | Unit 1 narrows feedback to a set point | Applied | LS1.A names positive and negative feedback. Unit 1 and bio-homeostasis-feedback notes: a required, supplied organism-level positive-feedback case (simplified blood clotting, no molecular steps): counteracting against amplifying, and what stops the amplifying |
| 3 | Unit 3's dry-mass revision trigger cannot show sugar atoms in amino acids | Applied | Dry mass shows mass gained, not where sugar's atoms go, so HS-LS1-6's revision on evidence would go unsupported. The expert's revision moment stands; its evidence is now supplied carbon tracing from sugar into new amino acids with a printed atom-tracking path, other elements accounted for from the surroundings; dry mass stays the photosynthesis and respiration evidence (unit 3 and bio-carbon-molecules notes) |
| 4 | "Every investigation fits one lesson" against week-long observations | Applied | Days bullet: active sessions fit 50-minute lessons; longitudinal investigations name preparation, elapsed time, repeated measurements and teacher drying, inside units 1 and 3's days |
| 5 | Load note counts four engineering expectations | Applied | bio-population-carrying-capacity notes: 24 life science, three engineering (HS-ETS1-1, HS-ETS1-3, HS-ETS1-4), three Earth and space |
| 6 | ELA 9 says Biology and Algebra I are written later | Cross-subject | Wording below |
| 7 | RUBRIC-SCIENCE "only material" | For the lead | Wording below |
| 8 | RUBRIC-SCIENCE nature-of-science gap | For the lead | Wording below |
| For Cory | Readers | Collected | Already in "For Cory" above |

Counts: applied 5, cross-subject 1, for the lead 2, rejected 0.

### Chemistry

| # | Finding | Result | What was done |
|---|---|---|---|
| 1 | Supplied-data routes drop the investigation and build performances | Applied | Labs bullet course rule: each no-kit or simulation path names the decisions, evidence collection, construction, testing and revision it keeps; supplied results alone are partial coverage for HS-PS1-3, HS-ESS2-5, HS-PS3-4 and HS-PS3-3 (rubric S6), and the unit plan names the practical step still owed. Units 2, 3, 5 and 7 rewritten as given (student-chosen conditions and limits; supplied melting data a supplement; the water-mixing investigation kept; the device always built and tested). The same "active sessions fit 50-minute lessons" wording as Biology replaces "Every investigation fits one lesson" |
| 2 | Cooking oil does not disappear | Applied | Unit 2 anchor: water and rubbing alcohol dry at different rates while oil leaves a persistent mark; water and alcohol bead differently. Substitute note: controlled water and alcohol comparison, spreading told from drying, evaporation qualitative |
| 3 | Iron and copper reactions in a main-group unit | Applied | Unit 1: steel wool and copper are optional enrichment about chemical change, not assessed cases for HS-PS1-1 or HS-PS1-2 |
| 4 | ELA 10 unit 7 overlaps the forecast by three days | Applied | Unit 9 runs about days 113 to 130 (106 unit days and 6 check days before it); ELA 10 unit 7 starts about day 128. The lean now says ELA uses its supplied forecast reading until the forecast is complete. The ELA 10 note in "Cross-subject notes" above, that its if-later line "is not needed", is withdrawn: ELA keeps it |
| 5 | ELA 10 says the chemistry frame is written later | Cross-subject | Wording below |
| 6 | RUBRIC-SCIENCE nature-of-science gap | For the lead | Wording below |
| For Cory | Whether a no-kit route counts as full completion | For Cory | Below |

Counts: applied 4, cross-subject 1, for the lead 1, for Cory 1 new.

### Physics

| # | Finding | Result | What was done |
|---|---|---|---|
| 1 | Three anchors too absolute | Applied | Unit 4: a cart or gravity-driven ride with no added power never regains its release height. Unit 7: "Sunlight can damage skin, while a radio receiver detects broadcasts inside a room. How do different frequencies interact with matter, and what controls their effects?", with thermal absorption and photon energy against total exposure in the content. Unit 10: a sourced age table with ancient meteorites, ancient lunar samples, Earth's oldest rocks and younger lunar rocks |
| 2 | HS-PS3-2, HS-PS4-5, HS-ESS2-1 mechanisms | Applied | Unit 4: each energy change tied to particle motion and relative positions. Unit 6: absorption, detection and photoelectric response taught qualitatively before the explainer, signal traced through matter. Unit 9: uplift and erosion as interacting processes with feedback, across scales. Matching notes in phys-energy-motion-position, phys-wave-technologies, phys-landforms-scales |
| 3 | Required crosscutting concepts missing in units 6 and 9 | Applied | Unit 6 C3 adds cause and effect (HS-PS4-1, HS-PS4-5); unit 9 adds patterns (HS-ESS1-5); the Standard bullet says C3 entries are required and a dropped candidate never removes one |
| 4 | Unit 5's no-kit route drops the investigation | Applied | Both induction directions with student decisions on controls, measurements, repetitions and limits; no-kit path is selectable recorded runs or an interactive investigation keeping those decisions, said to be weaker; supplied readings alone do not count |
| 5 | T squared = a cubed needs a central-body limit | Applied | Sun-centred only, a the semimajor axis; a supplied k in T squared = k times a cubed, or a reference orbit around the same body, for moons and satellites; no derivation. Math readiness, unit 3 note, the two math table rows and phys-orbits notes |
| 6 | Unit 8 anchor gives the answer away | Applied | Opens on laboratory and stellar spectra; stellar element formation and the early universe come as explanations from that evidence; three expectations and 18 days kept |
| 7 | RUBRIC-SCIENCE "only material" | For the lead | Wording below |
| 8 | RUBRIC-SCIENCE nature-of-science gap | For the lead | Wording below |
| In passing | ELA 11 argument unit is weeks 7 to 11 | Applied | Physics ELA table corrected; availability unchanged |

Counts: applied 6 plus 1 in passing, for the lead 2, rejected 0.

### Progression changes (data/progressions/science.csv, notes only, 8 rows)

| Row | Change |
|---|---|
| bio-energy-pyramids | The three-way energy budget (biomass, respiration heat, detritus and decomposers); a tenth illustrative; atoms tracked apart from energy |
| bio-homeostasis-feedback | Required supplied positive-feedback case beside the set-point investigation |
| bio-carbon-molecules | Revision evidence is carbon traced into new amino acids; dry mass is not this revision |
| bio-population-carrying-capacity | 24 life science, three engineering, three Earth and space |
| phys-orbits | Sun-centred limit; supplied k or reference orbit otherwise |
| phys-energy-motion-position | Macroscopic change tied to particle motion and positions |
| phys-wave-technologies | Absorption, detection and photoelectric response before the explainer |
| phys-landforms-scales | Uplift and erosion feedback across scales |

No assumes or hands_on changed; the grade 8 frame's Seams table needed no edit.

### Settled (rerun)

| Choice | Course | Reason |
|---|---|---|
| Energy budget splits biomass, respiration heat and detrital energy; a tenth illustrative | Biology | HS-LS2-4 accounts for energy not passed up |
| A supplied positive-feedback case is required in unit 1 | Biology | LS1.A names both feedback kinds |
| HS-LS1-6 revision on carbon-tracing evidence, not dry mass | Biology | Dry mass cannot show sugar atoms in amino acids |
| Longitudinal investigations name elapsed time inside existing days | Biology, Chemistry | The calendar stays honest |
| No-kit routes name what they keep; supplied results alone are partial | Chemistry | Rubric S6; investigate and build verbs |
| Unit 2 anchor: water and alcohol dry, oil leaves a mark | Chemistry | Accurate observation |
| Iron and copper reactions are enrichment, not HS-PS1-1 or HS-PS1-2 evidence | Chemistry | Main-group boundary |
| ELA 10 keeps its forecast fallback | Chemistry | The units overlap on days 128 to 130 |
| Anchors: release height, frequency and exposure, a sourced age table, spectra first | Physics | Accurate, and the answer not given away |
| Particle, device-matter and landform-feedback mechanisms named | Physics | Standards in full |
| Cause and effect in unit 6, patterns in unit 9, as required C3 | Physics | Each expectation's own crosscutting concept |
| Kepler's third law Sun-centred; supplied k otherwise | Physics | Correct predictions without new math |
| Unit 5 no-kit keeps the student's investigation decisions | Physics | HS-PS2-5's practice |

### Cross-subject (for those frames' owners; not edited here)

- **ELA 9** (`docs/courses/english-language-arts-grade-9/frame.md`, line 156): replace "the biology and Algebra I
  frames are written later, so their units are not guessed." with "the world history, Biology and Algebra I frames
  are on file. Biology unit 7 runs in weeks 19 to 23, before this course's unit 7 in weeks 24 to 26; Biology unit 9
  runs in weeks 25 to 28, so this course retains its supplied-source bridge for human impacts."
- **ELA 10** (`docs/courses/english-language-arts-grade-10/frame.md`, line 154): replace "the chemistry frame is
  written later, so its units are not guessed." with "Chemistry timing is recorded in docs/courses/chemistry/frame.md.
  Its forecast unit ends on about day 130, while this course's research unit starts on about day 128; the
  forecast-reading fallback covers that overlap." Keep line 176's if-later line (this corrects the earlier note above).
- **Algebra I, Algebra II, World History II:** the earlier notes above stand.

### For the lead (outside this pass's files)

- `docs/RUBRIC-SCIENCE.md` lines 54 to 55 ("the only material"): "Science course frames and the science progression
  are now on file, alongside the grade 4 scope and sequence draft and the middle school base text. These are planning
  evidence, not completed courses; claims about lessons, assessments and classroom use require the corresponding
  materials." (Same intent as the K to 2 report's wording; use one.)
- `docs/RUBRIC-SCIENCE.md` line 64, Gateway 2 connections: replace "No plan names where the nature of science is
  taught" with "Nature-of-science locations are named in the course frames, for example Biology units 5, 7 and 8;
  Chemistry units 1, 8 and 9; Physics units 3, 7 and 8. Unit plans must specify the tasks and evidence that develop
  these ideas."
- For docs/APPROACH-SOURCES.md: the HS-LS1, HS-LS2, HS-PS1-3, HS-PS3-2 and HS-PS3-3 evidence statements; the
  orbits page of the federal space agency; the radiofrequency and lunar-sample sources the Physics rerun names; the
  two chemistry evaporation sources; the high school criteria PDF was unreachable.

### For Cory (rerun)

- **Audience and scope (Chemistry, and the same rule in Physics unit 5).** If a no-kit route is meant to count as
  full course completion, how learners get the hands-on investigation and build the standards require. The frames
  now mark supplied-data routes as partial coverage until then.
- **People.** Unchanged: the safety and materials teacher and the sensitive-topic readers.

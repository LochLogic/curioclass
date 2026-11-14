# Fixes: science course frames, grades 6 to 8, after the two cold reads (2026-11-14)

Applies the expert reads (`frame-science-grade-<n>-2026-11-14.md`) and the Codex reruns
(`frame-science-grade-<n>-codex-rerun-2026-11-14.md`, numbered as in those files) to the grade 6, 7 and 8 frames and
`data/progressions/science.csv`. The first Codex reads (`frame-science-grade-<n>-codex-2026-11-14.md`) were withheld
over a gate failure and are superseded by the reruns. Every expert finding and every "Settled by the expert" row of
both reads is applied, except where a settled row's file is outside this pass ("For the lead"). Each Codex finding
was weighed on its merits. Also applied: the grade 3 to 5 fixes report's note on grade 6's unit 3 reason cell, and
the high school fixes report's grade 8 items (the plate model's rest and Biology pick-up; phys-orbits' m8-roots
lean for Kepler's third law).

Gates after the fixes: `scripts/frame.py sync` (52 courses); `scripts/frame.py check science-grade-6
science-grade-7 science-grade-8 science-grade-5 biology chemistry physics` 0 failures each;
`scripts/progression.py check science` 198 rows, 0 failures; `scripts/stale.py check` 56 files, 1 failure, in
`docs/courses/english-language-arts-grade-3/frame.md` line 48 (another fixer's file; none in this pass's files).
No unit, skill or standard moved; every course keeps 6 units and 160 days (156 in units, 4 at course level).

Applied in all three frames: the shared source map's "Days here" column and last column now give each unit's real
days, condensations and additions; the source map's lead-in says days are base days times 0.9 "plus the openings
and Curio Class additions the rows need, less the condensations named in the last column"; the Cross-subject
tables cite the math and ELA frames' own units and days (frames on file), each "if later" cell saying whether its
bridge is still used.

The year budget, all three grades (minutes are 50 a day; base days are 45 minutes):

| Grade | Unit days | Condensed base days | Added | Without the condensations |
|---|---|---|---|---|
| 6 | 17, 34, 38, 24, 20, 23 | None | 1 day moved from unit 3 to unit 6 (expert settled); margins over base +40, +35, +10, +75, +55, +25 minutes | 160 |
| 7 | 23, 18, 25, 28, 32, 30 | 5: 7.1 L9, 7.2 L9, 7.3 L7 and L12, 7.6 L17 | Safety (50), synthetic research (50), two reteach lessons (100), ores and groundwater (50) | About 165 |
| 8 | 26, 21, 28, 27, 27, 27 | 13: 8.1 L9 and L13, 8.2 L3 and L10, 8.3 L1, L4, L9 and L11, 8.4 L13, 8.5 L1, 8.6 L1, L7 and L10 | Safety (25), five reteach lessons (250), senses synthesis (10), static charge (100), gravitational stored energy (50), whole-cell model (50) | About 170 |

Each condensation is named in the source map with how its evidence is kept (for example 7.1 lesson 9's second day
becomes the teacher demonstration the safety finding requires; 8.2 lesson 3's laser viewer becomes supplied
observations). Every unit's minutes were checked against its days: no unit is over.

## Grade 6

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied, merged with Codex 5 | Unit 6: the investigation runs on three sample kinds (unicellular organisms, cells of multicellular organisms, nonliving samples); hand lenses named as visible structures only; low-cost path a paper or clip-on lens (about 60 times or more); no-microscope path scaled micrographs and a virtual microscope with a paper equivalent, said to be weaker; s6-cells-body-systems notes |
| Expert | 2 | Applied | Unit 6 23 days (1 from unit 3, settled); unit 5 names MS-PS4-3's time (base lesson 8 plus about one more lesson) |
| Expert | 3 | Applied | Math leans cite math 6's units and days (ratio reasoning days 19 to 59, unit rates about 45 to 51, histograms about 146 to 148, center unit 8 days 143 to 158, negative numbers 121 to 142); students set the timeline scale (settled); s6-geologic-time notes |
| Expert | 4 | Applied, merged with Codex 3 | MS-ESS2-2 in full: spatial and time scales, water, ice and wind, gradual and sudden; the limestone case (Codex settled); unit 4 and s6-surface-change-scales notes |
| Expert | 5 | Applied, merged with Codex 10 | "14 performance expectations on 14 progression rows" |
| Expert | 6 | For the lead | The old Codex read's supersession line is in another file |
| Expert | 7 | Applied | Loss check: grade 6 loses nothing; grades 7 and 8 name their five gaps as additions and their condensations |
| Expert | settled | Applied | All three rows |
| Codex rerun | 1 | Applied | Unit 4: rock-cycle and plate models built together in the base's lesson order, before the timeline lessons; models carried and loss check say the same |
| Codex rerun | 2 | Applied | The membrane controls what enters and leaves; the plant cell wall gives structural support (unit 6 and s6-cells-body-systems) |
| Codex rerun | 3 | Applied | As expert 4 |
| Codex rerun | 4 | Applied | Unit 5: the plate model explains earthquakes, eruptions and tsunamis; storms are explained with unit 3's atmosphere and ocean models; s6-hazard-forecast notes |
| Codex rerun | 5 | Applied | As expert 1 |
| Codex rerun | 6 | Applied | Days bullet: the 240-minute margin is uneven by unit (figures above), not a surplus in every unit. The settled 1-day move stands over Codex's preference to keep the days (expert settled row) |
| Codex rerun | 7 | Applied | s6-light-paths: "This row contributes to MS-PS4-2, marked ~; s8-earth-sun-moon owns and completes the expectation." |
| Codex rerun | 8 | Applied | s6-particle-temperature: "This row owns MS-PS3-5; s8-energy-transfer-argument (unit 8.3) applies it later to whole objects and is marked ~." |
| Codex rerun | 9 | For the lead | The old expert review's ELA status line |
| Codex rerun | 10 | Applied | As expert 5 |
| Codex rerun | settled | Applied | All eight rows (the 160-day row as Codex 6) |
| 3-5 fixes | note | Applied | Unit 3 reason cell: "grade 5 shadow and day-length patterns; sun angle by latitude is new here" |

Unit 3 is 38 days (10 minutes over base); check 1 is days 90 and 91. "For the lead" items 3 and 4 (the two stale
notes) are removed as applied; People renumbered.

## Grade 7

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied, merged with Codex 1 | Unit 6: base lesson 10 with its extension taught in full, plus a Curio Class day on mineral ores and groundwater from maps and geologic evidence, then an unfamiliar distribution explained; loss check names the gap; s7-resource-distribution notes |
| Expert | 2 | Applied, merged with Codex 3 | Unit-by-unit minute budget in the Days bullet: unit 4 28 (1 day research), unit 5 32 (two reteach lessons), unit 6 30; 160 held by five named condensations (expert's "160 with named base lessons cut", with the evidence kept rather than lessons cut). Year length for Cory |
| Expert | 3 | Applied, merged with Codex 2 | Unit 1: student mixing limited to the named bath-bomb ingredients; flame tests (L5, 6, 9), peroxide (L6), heating (L9) and electrolysis (L10) teacher-only under a protocol each (goggles, hair tied back, fire-safe surface, extinguisher, hot plates, set distance); supplied-data fallback; the course Safety bullet matches; s7-reactions-atoms notes |
| Expert | 4 | Applied | Boiling point added to the permitted properties (unit 1 and s7-reactions-atoms). Codex calls this not a coverage gap; both hold: it is listed as permitted, not required for assessment |
| Expert | 5 | For the lead | The old Codex read's supersession line |
| Expert | settled | Applied | Both rows |
| Codex rerun | 1 | Applied | As expert 1 |
| Codex rerun | 2 | Applied | As expert 3, in Codex's words |
| Codex rerun | 3 | Applied | As expert 2; the budget names merges, support minutes, additions and totals; check days kept |
| Codex rerun | 4 | Applied | Unit 1: "some consist of discrete molecules, others form extended structures, such as a salt crystal"; unit 3: starch and proteins have linked building units, fats a glycerol part with three fatty-acid parts, contrasted with simple molecules and a salt crystal; starch removed from extended structures; s7-reactions-atoms and s7-food-molecules notes |
| Codex rerun | 5 | For the lead | Supersession line on the old Codex read |
| Codex rerun | 6 | For the lead | Old expert review's ELA line (with corrected days: argument writing is ELA 7 unit 4, days 87 to 108, not 91 to 112) |
| Codex rerun | 7, 8 | For the lead | docs/RUBRIC-SCIENCE.md |
| Codex rerun | 9, 10 | Applied (rows); lead (report) | The two CSV notes as grade 6 Codex 7 and 8; the progression fixes report's lines to the lead |
| Codex rerun | 11 | For the lead | progression-science-fixes-2026-11-13.md line 41 |
| Codex rerun | settled | Applied | All eight rows, including "individual-organism growth beside population numbers" (unit 5 now names it) and the MS-LS1-5 start note (s7-cell-respiration-growth; "For the lead" item 3 replaced) |

Also: unit day ranges 1 to 23, 24 to 41, 42 to 66, check 1 days 67 and 68, 69 to 96, 97 to 128, 129 to 158;
Cross-subject cites math 7 (proportional tables days 13 to 33, overlapping unit 2, bridge kept; percent days 47 to
68, available) and ELA 7 (informative unit 2 days 31 to 56; research unit 3 days 61 to 86; argument unit 4 days 87
to 108; evaluating arguments unit 6 days 135 to 156); the human impact thread row now says ELA supplies its own
background. Models carried and Handed on: rock-cycle and plate models last carried in unit 6, resting in grade 8,
picked up by Biology unit 8 (bio-environment-change-species).

## Grade 8

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied, merged with Codex 2 | Unit 3: base teaching named as magnetic only; static-charge addition (about 2 days, after base lesson 8: charge, separation and force, the field question, design evaluation, electric stored energy) and gravitational stored energy (about 1 day, after base lesson 11, in unit 3, so the start of MS-PS2-4 stays there); latex-free balloon; loss check corrected; s8-electromagnetic-forces, s8-fields, s8-potential-energy notes |
| Expert | 2 | Applied, merged with Codex 3 | Unit-by-unit budget; 160 held by 13 named condensations; reteaches are whole lessons (settled), one per unit with readiness checks; "For the lead" item 2 replaced with the arithmetic and the year-length question |
| Expert | 3 | Applied | Unit 5: whole-cell model addition (about 1 day, near base lessons 5 and 6, plant and animal); s8-cell-parts-function notes |
| Expert | 4 | Applied, merged with Codex 1 | Unit 4 in Codex's words (qualitative wave model of light); unit 2 "new contribution to MS-PS4-2"; seam row names both contributions |
| Expert | 5 | Applied | Unit 1: MS-LS1-8 part (touch receptors, signals, memory) and the concussion note; unit 2: the synthesis task (end of base lesson 12, sight, smell, touch, hearing); Standard bullet lists all earlier parts (grade 6 units 1 and 6, grade 7 unit 1, unit 1 here); s8-senses-brain notes |
| Expert | 6 | Applied, merged with Codex 5 | Laser: Codex's replacement rule (supplied observations unless the safety read sets a controlled apparatus: class 2, fixed by the teacher, beam and reflection below eye level, stopped on a matte surface); the expert's "never at a shiny surface" dropped, since the base apparatus uses a mirror (Codex 5). Speakers opened by the teacher; magnets kept apart and from phones, pacemakers and cards; unit 5 health policy note; s8-wave-amplitude-energy notes |
| Expert | 7 | Applied | s8-wave-amplitude-energy and s8-earth-sun-moon notes ("Owns and completes MS-PS4-2, following contributions from s6-light-paths and s8-wave-amplitude-energy") |
| Expert | 8 | Applied, merged with Codex 7 | wave-model "used for information patterns in grade 6 unit 5 (s6-digital-signals); rests in grade 7"; force-diagram adds s5-gravity-down |
| Expert | 9 | Applied | MS-PS2-5's design evaluation (unit 3); MS-LS4-1's assumption that natural laws worked then as now (unit 6); unit 4's scientific-notation line in the expert's words; scatter plots "available" (math 8 unit 4, about days 56 to 60) |
| Expert | 10 | For the lead | The old Codex read's supersession line |
| Expert | settled | Applied | All four rows (reteaches whole lessons; 8.1 lesson 16 left out) |
| Codex rerun | 1 | Applied | As expert 4 |
| Codex rerun | 2 | Applied | As expert 1 and 3; the source map's last column names each addition and where it sits |
| Codex rerun | 3 | Applied in part | The lesson-level minute budget is in the Days bullet. Rejected: allowing small-group reteaching; the expert's settled row (reteaches are whole lessons) governs |
| Codex rerun | 4 | Applied | All seven performances: graphs constructed (MS-PS3-1), senses synthesis (MS-LS1-8), design evaluated (MS-PS2-5), the solar-system and galaxy model with the disk (MS-ESS1-2), a student causal model (MS-LS3-1), embryos against adult anatomy (MS-LS4-3), the reproduction argument (MS-LS1-4) |
| Codex rerun | 5 | Applied | As expert 6; the concussion note as expert 5. Also from Codex's limits: the strawberry DNA lab's alcohol is teacher-dispensed and kept from flames |
| Codex rerun | 6 | Applied | Row ids corrected (scatter plots s8-gravity-mass; argument writing s8-energy-transfer-argument and s8-reproduction-behaviors). Calendars from the frames, which differ from Codex's figures: ELA 8 argument writing unit 2 days 31 to 62, research unit 3 days 63 to 88, gene thread unit 5 days 129 to 156; math 8 qualitative functions days 93 to 116, scatter plots about 56 to 60 |
| Codex rerun | 7 | Applied | As expert 8 |
| Codex rerun | 8, 9, 10 | Applied | CSV notes as grade 6 Codex 7 and expert 7 |
| Codex rerun | 11 to 15 | For the lead | Rubric, old reviews and the progression fixes report |
| Codex rerun | settled | Applied | All eight rows; "160-day fit provisional pending a minute budget" is met by the budget, with the scope and sequence confirming it lesson by lesson |
| HS fixes | 2 items | Applied | Threads: rock-cycle and plate models rest in grade 8, Biology unit 8 picks the plate model up; Handed on: phys-orbits takes Kepler's third law with roots by calculator from math 8 (m8-roots) |

Also: unit day ranges 1 to 26, 27 to 47, 48 to 75, check 1 days 76 and 77, 78 to 104, 105 to 131, 132 to 158; dormant
seam rows now read "readiness check, one-lesson reteach".

## Progression changes (data/progressions/science.csv, 17 rows)

| Row | Change |
|---|---|
| s6-light-paths | Notes: contributes to MS-PS4-2, marked ~; s8-earth-sun-moon owns and completes it |
| s6-particle-temperature | Notes: owns MS-PS3-5, applied later by s8-energy-transfer-argument (~); also starts MS-PS1-4 (owned by s6-state-change) |
| s6-surface-change-scales | Notes: MS-ESS2-2 in full, the limestone case |
| s6-geologic-time | Notes: students set the scale by ratio reasoning (math 6 about days 19 to 59); given only if math runs late |
| s6-hazard-forecast | Notes: plate model for quakes, eruptions and tsunamis; storms with the 6.3 models |
| s6-cells-body-systems | Notes: membrane and wall jobs; hand lens, low-cost and no-microscope paths |
| s7-reactions-atoms | Notes: boiling point; molecules and extended structures; teacher-only demonstrations with protocols and the supplied-data fallback |
| s7-food-molecules | Notes: food molecules by size and arrangement; starch out of extended structures |
| s7-cell-respiration-growth | Notes: also starts MS-LS1-5 (owned by s8-growth-factors) |
| s7-resource-distribution | Notes: the lesson 10 extension and the ores and groundwater day; plate model last carried here, Biology unit 8 picks it up |
| s8-wave-amplitude-energy | Notes: the mechanical-wave contribution to MS-PS4-2; the laser replacement |
| s8-earth-sun-moon | Notes: owns and completes MS-PS4-2 after the two contributions |
| s8-senses-brain | Notes: the synthesis task |
| s8-electromagnetic-forces | Notes: the electric part as a Curio Class addition (about 2 days, shared with s8-fields) |
| s8-fields | Notes: charged objects as an addition, latex-free balloons, design evaluation |
| s8-potential-energy | Notes: electric and gravitational cases as additions (gravity about 1 day) |
| s8-cell-parts-function | Notes: whole-cell model addition |

No assumes, hands_on, standard, model or cross_subject column changed, so no handoff moved; both ends of every
handoff named in the frames still match. The grade 5, Biology, Chemistry and Physics Seams tables were checked and
need no change (Physics' phys-orbits row already carries the m8-roots lean; Biology's models table already shows the
plate model last carried by s7-resource-distribution).

## Cross-subject notes (for those frames' owners; not edited here)

- **ELA grade 6**, `docs/courses/english-language-arts-grade-6/frame.md` line 177, column 4: replace "Science 6 unit
  3, days 52 to 90 (beside)" with "Science 6 unit 3, days 52 to 89 (beside)". Line 178, column 4: replace "Science 6
  units 4 and 5, days 93 to 136 (before)" with "Science 6 units 4 and 5, days 92 to 135 (before)".
- **ELA grade 7**, line 161, column 4: replace "Base units 7.5 and 7.6, mid to late in the year" with "Science 7 units
  5 and 6, days 97 to 158". Line 162, column 4: replace "The science course's climate work" with "Science 7 unit 6,
  days 129 to 158 (climate evidence)". The other cells stand: ELA supplies its own background and takes the climate
  facts as given, which science 7 now relies on.
- **ELA grade 8**, line 166, column 4: replace "Science 8 unit 5 (genetics), days 106 to 130" with "Science 8 unit 5
  (genetics), days 105 to 131".
- **Math grade 6**: already cites science 6's new days (92 to 115, 116 to 135, 136 to 158, 52 to 89). No change.
- **Math grade 7**, line 140, last cell: replace "science 7 unit 2 is days 24 to 42" with "science 7 unit 2 is days
  24 to 41". Line 141 stands (unit 6 days 129 to 158).
- **Math grade 8**, line 134: "science 8 unit 4 is days 78 to 105" to "science 8 unit 4 is days 78 to 104". Line 135:
  "science 8 unit 5 is days 106 to 130" to "science 8 unit 5 is days 105 to 131". Line 136: "science 8 units 1 and 2
  are days 1 to 48" to "science 8 units 1 and 2 are days 1 to 47". Line 137: "science 8 unit 4 is days 78 to 105" to
  "science 8 unit 4 is days 78 to 104". Lines 152 to 153 ("For the lead" 2): "at days 78 to 105 and its unit 5 at
  days 106 to 130" to "at days 78 to 104 and its unit 5 at days 105 to 131".

## For the lead (outside this pass's files)

- **Old Codex reads** (expert g6 6, g7 5, g8 10; Codex g7 5, g8 15): add at the top of each of
  `frame-science-grade-6-codex-2026-11-14.md`, `-7-` and `-8-`: "Superseded: the plan gate passes as of 2026-11-14;
  see frame-science-grade-N-2026-11-14.md and frame-science-grade-N-codex-rerun-2026-11-14.md." (N the grade.)
- **Old expert reads' ELA lines** (Codex g6 9, g7 6, g8 13): `frame-science-grade-6-2026-11-14.md` line 118, add
  "Superseded 2026-11-14: the ELA 6 frame is on file; science 6's leans are checked against it in
  frame-science-6-8-fixes-2026-11-14.md." Line 105 of the grade 7 read: "Superseded 2026-11-14: ELA 7 is framed.
  Research is taught on days 61 to 86, argument writing on days 87 to 108 and argument evaluation on days 135 to 156;
  science keeps its local bridges where it uses these skills earlier." Line 204 of the grade 8 read: "Superseded
  2026-11-14: ELA 8 is framed (argument writing days 31 to 62, research days 63 to 88); science 8's leans are checked
  against it in frame-science-6-8-fixes-2026-11-14.md."
- **docs/RUBRIC-SCIENCE.md** lines 54 to 55 (Codex g7 7, g8 11): "Science planning includes the Grade 4 scope and
  sequence draft, course frames in `docs/courses/`, and the middle-school base text. These are planning materials,
  not evidence of a finished or classroom-tested course."
- **docs/RUBRIC-SCIENCE.md** line 64, Gateway 2 connections row (Codex g7 8, g8 12): "Course frames locate
  nature-of-science teaching. Unit and section plans must identify the evidence, student task, and assessment that
  develop each claimed element."
- **docs/reviews/progression-science-fixes-2026-11-13.md** (Codex g7 9 to 11, g8 14): beside the MS-PS4-2 and
  MS-PS3-5 lines add "Done 2026-11-14: s8-earth-sun-moon owns MS-PS4-2 with s6-light-paths and
  s8-wave-amplitude-energy contributing; s6-particle-temperature owns MS-PS3-5 and s8-energy-transfer-argument
  applies it (~)." Line 41: replace with "High-school math progression rows now exist in
  `data/progressions/math.csv`. Check each science dependency against its actual course and unit availability;
  retain local scaffolds where science still comes first."
- Source list (docs/APPROACH-SOURCES.md): the expert's note that each OpenSciEd Teacher Edition's "fully developed
  only with extensions" section is the quickest way to find base gaps; Codex's MS-PS2-3, MS-LS1-2 and MS-ESS1-2
  evidence statements and the NSTA reflected-laser guidance.

## For Cory

- **Year length (time).** Grade 7: 160 days with 5 named condensed base days, or about 165. Grade 8: 160 with 13
  condensed base days, or about 170. Pick: 160 for both; the scope and sequence confirms it lesson by lesson. Goes
  with the minutes-per-lesson question (pick 50 minutes, five a week).
- **Course ids (structure).** Three year courses under the science-ms band name in data/courses.csv.
- **People.** A science teacher's safety and materials read (all three years: grade 7's demonstrations, grade 8's
  laser replacement, speakers and magnets); a disability-community reader (grade 6 unit 6 lesson 14); a school
  nurse or physician (grade 7 unit 3); a reader with knowledge of Indonesia's farming communities (grade 7 unit 5);
  a reader from the Deaf and hard of hearing community (grade 8 unit 2). Who, and any pay.

## Settled (for docs/reviews/DIGEST.md)

| Choice | Reason | Where |
|---|---|---|
| Grade 6 unit 3 38 days, unit 6 23 | Unit 6 was the one unit under base time | science-grade-6 frame |
| Grade 6 margins stated per unit (+40 to +75 minutes) | The year surplus is not a surplus in every unit | science-grade-6 frame |
| Grade 7 and 8 held at 160 by named condensations, each keeping its evidence | Additions and reteaches exceed the 0.9 scaling; the year yardstick holds | science-grade-7 and -8 frames, source map |
| Grade 8 reteaches are whole lessons, one per unit with readiness checks | Row contract; storyline lessons are whole-class (expert settled) | science-grade-8 frame |
| The base laser-and-mirror viewers replaced by supplied observations unless the safety read sets a controlled apparatus | Reflected beams are a hazard; a mirror apparatus cannot avoid shiny surfaces | science-grade-8 frame; s8-wave-amplitude-energy |
| Grade 7 flame tests, peroxide, heating and electrolysis teacher-only under protocols; student mixing only the bath-bomb ingredients | Open flame, hot water and gases with 12-year-olds | science-grade-7 frame; s7-reactions-atoms |
| Static charge and gravitational stored energy both in unit 3 of grade 8 | Base 8.3 is magnetic only; keeps MS-PS2-4's start in unit 3 | science-grade-8 frame; three s8 rows |
| MS-PS4-2: grade 6 ray model and grade 8 sound contribute; s8-earth-sun-moon owns with a wave model of light | Ownership already moved; notes now say so | frames; three rows |
| Boiling point listed as a permitted property, not a required one | Both reads: PE boundary lists permitted properties | science-grade-7 frame |
| Rock-cycle and plate models rest in grade 8; Biology unit 8 picks the plate model up | The base has no grade 8 Earth-materials unit | grade 7 and 8 frames; s7-resource-distribution |

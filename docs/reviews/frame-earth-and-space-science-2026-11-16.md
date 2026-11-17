# Frame read: earth-and-space-science (Earth and Space Science, grade 12 elective), 2026-11-16

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md (high school Gateways 1 and 2, rows S1
  to S13), docs/PRODUCTION-PATH.md (After the core subjects, and the "Before a new subject's scopes" checklist),
  DESK-ANSWERS entries for q-hs-science-core and the 2026-11-15 elective checklist, docs/sources/BASE-TEXTS.md (no
  entry yet for any of the four sources, as the frame's Pending note says).
- The frame docs/courses/earth-and-space-science/frame.md in full (315 lines), its row in data/plans/frames.csv (9
  units, 160 days, 50 minutes, 5 a week, 32 weeks, year) and the catalogue row in data/courses.csv (grades 9 to 12,
  typical 9, not core). No data/plans/earth-and-space-science/ folder exists yet, so there is no source-map.csv; the
  Source map is read from the frame.
- The 19 ess- rows of data/progressions/science.csv, and every earlier row they assume (s6-, s7-, s8-, bio-earth-life-
  coevolution, chem- and phys- rows), read for what each already teaches.
- data/standards/curio-science-electives.txt, CUR-ESS.1 to CUR-ESS.24 (and CUR-ENV.1 to 21 for the seam).
- The frames beside and before: docs/courses/biology/frame.md, chemistry/frame.md, physics/frame.md (unit tables and
  thread lines), docs/courses/environmental-science/frame.md (units and its "Beside this course" seam). To test
  "nothing taught twice" I also read the written day plans where the overlap is likeliest:
  docs/courses/chemistry/s09.md (days 113 to 129, the energy budget, timescales, proxies and forecast),
  docs/courses/physics/s08.md (stars: no H-R diagram is taught) and docs/courses/physics/s09.md (interior, crust
  ages, measured plate separation), and both courses' TOOL-ASKS.md.
- The base-text scout notes (side-session base-text-scout-2026-11-16.md, section 4): licences and full tables of
  contents of Physical Geology 2e, OpenStax Astronomy 1e, JetStream and Webb's Introduction to Oceanography. Every
  chapter and section in the frame's Source map was checked against them.
- Earlier reads of the same layer, for REPEAT tags: frame-chemistry-2026-11-14.md, frame-physics-2026-11-14.md,
  frame-biology-2026-11-14.md, frame-psychology-2026-11-16.md.
- Gates: `python -X utf8 scripts/plan.py check`: frame earth-and-space-science 0 failures, 9 units, 160 days (149 in
  units, 11 for checks and respond days). `python -X utf8 scripts/stale.py check`: 62 files, 0 failures.

No web source was fetched for this read. Where a finding rests on memory it says so and names what to check.

## Verdict

The frame is sound in design: all 19 rows and all 24 CUR-ESS outcomes sit in exactly one unit, every high school Earth
and space expectation is correctly named with its owning course and unit, the handoff table and readiness logic hold
row by row, the anchors are real, specific and mostly accurate, and the outward order (ground, time, plates, water,
air, ocean, climate, planets, stars) gives each unit a tool the one before built. The biggest risks are two: unit 8's
outcome promises a quantitative explanation of Venus's surface temperature with a model (a single-layer greenhouse)
that cannot produce it, and the Source map and unit 4's stream table quietly re-teach material Chemistry unit 3,
Chemistry unit 9, grade 8 and Physics unit 10 already teach, which breaks the frame's own "nothing taught twice" rule.
The one change that matters most is finding 2: mark each overlapping base section as retrieval or left out and say
what unit 4's stream table measures, since a scope writer adapts "lesson by lesson" from the Source map.

## Findings, most serious first

### 1. Unit 8's energy balance cannot explain Venus with the boundary it is given (serious; firm)

**What is wrong.** CUR-ESS.20 and the unit 8 cell ask students to explain the surface temperatures of Venus, Earth and
Mars "in a quantitative energy balance checked against spacecraft measurements". The row ess-planetary-climates sets
the boundary "a single-layer greenhouse; the radiation law supplied". A single fully absorbing layer raises the
surface temperature by the fourth root of 2 (about 1.19) over the effective temperature. Venus reflects about three
quarters of the sunlight it gets, so its effective temperature (about 230 K) is lower than Earth's (about 255 K);
one layer gives about 275 K, against a measured surface of about 735 K. The model works for Earth (about 303 K, near
the real 288 K) and for Mars (thin air, small effect) and fails for Venus by more than 400 K. (Standard radiative
balance; from memory, any introductory planetary science text, for example Astronomy 1e section 10.3.)

**Why it matters.** A writer following the boundary builds days whose model gives a wrong answer on the anchor's most
striking planet, and either hides the gap or tells students the model "explains" Venus. That is the accuracy door
(rubric 2d, row S10).

**Fix (row ess-planetary-climates boundary; frame unit 8 cell; CUR-ESS.20).** Boundary: "a layered greenhouse: the
single-layer model first, its failure for Venus found and argued, then the number of absorbing layers fitted as the
unknown (surface temperature equals effective temperature times the fourth root of n plus 1); the radiation law
supplied." Unit 8 cell adds: "the one-layer model works for Earth and Mars and fails for Venus; students find how
many layers Venus's 90-bar carbon dioxide air acts like." CUR-ESS.20 needs no new words if "a quantitative energy
balance" stays; the paper path (a worked table for three planets) gains one column. LAYER progression. REPEAT new.

### 2. The Source map and unit 4's stream table re-teach what earlier courses taught (serious; firm)

**What is wrong.** The frame promises "each unit says what the core course taught and what is new here", and labels
some sections "retrieval". These are placed as full teaching but were already taught:

| Placed here | Already taught by | Evidence |
|---|---|---|
| Physical Geology ch 19, 19.1 to 19.3, unit 7, "None left out" | Chemistry unit 9 days 117 to 121 teach the four climate timescales (19.1); day 118 the human cause (19.2); days 125 to 128 the forecast and impacts, Chemistry unit 11 sea level and migration (19.3) | docs/courses/chemistry/s09.md |
| Physical Geology 5.6 (weathering and climate), unit 7 | Chemistry day 120: mountain belts, silicate weathering and carbon dioxide over millions of years | s09.md day 120 |
| Astronomy 8.4 (life, chemical evolution, climate), unit 7 | Biology unit 8 (bio-earth-life-coevolution, oxygen in the air) | biology frame |
| Astronomy 4.5 and 4.7 (Moon phases, eclipses), unit 9 | grade 8 (s8-earth-sun-moon: phases, eclipses, seasons) | progression row |
| Astronomy 9.3 (impact craters as surface clocks), unit 8 | Physics unit 10 (phys-early-earth-history: impact craters) | progression row |
| Physical Geology 10.4 (plates, motions, boundaries), unit 3 | grade 6 (s6-plate-evidence) and Physics unit 9 | progression rows |
| JetStream 14 Tsunamis "warning, preparedness", unit 3 | grade 6 unit 6.5 (warning buoys, evacuation routes), Chemistry unit 11 | s6-hazard-forecast |
| Unit 4 "stream table (a gutter or tray of sand)" with no stated purpose | Chemistry unit 3 already runs stream-table erosion and deposition (chem-water-earth-materials) | progression row |

**Why it matters.** The scope writer adapts the base text section by section. Ch 19 alone is three sections, probably
three to four days of unit 7's 17, spent re-teaching Chemistry unit 9 to students who had it two years before; and a
student who meets the stream-table erosion lab a second time learns nothing new. The course's whole case for
existing (owning no NGSS code) is that it goes deeper.

**Fix (Source map rows; unit 4 hazards cell).** Physical Geology 19.1 and 19.2: "7, retrieval of Chemistry unit 9 (one
reading)"; 19.3 left out: "Chemistry units 9 and 11"; 5.6: "7, retrieval of Chemistry unit 9 day 120"; Astronomy 8.4
left out: "Biology unit 8"; 4.5 and 4.7: "9, retrieval of grade 8, then observed"; 9.3: "8, retrieval of Physics unit
10"; Physical Geology 10.4: "3, retrieval; the locked boundary is 12.1"; JetStream 14: "3 (causes, propagation and
inundation; warning and preparedness retrieval of grade 6, used only for the town advice)". Unit 4 cell: "the stream
table measures runoff timing and discharge from a paved and a vegetated surface (a hydrograph); erosion and
deposition are Chemistry unit 3's and are recalled, not re-run". LAYER base text. REPEAT new.

### 3. Unit 4's anchor cannot be answered from the evidence the unit teaches (moderate; likely, from memory)

**What is wrong.** CUR-ESS.12 works out recurrence from "a gauge record". The 2016 and 2018 Ellicott City floods came
down the small Tiber and Hudson branches above Main Street, which (from memory) had no long stream gauge before 2016;
what was called rare was the rainfall (the 2016 burst was put at about a 1-in-1,000-year rainfall for its duration).
The county's published hydrology study (from memory) found that the rain intensity drove most of the peak and that
upland development added a smaller share. The question "bad luck, or a changed watershed?" invites a single answer
when the evidence says both, with the rain dominant, plus the town's site in a narrow valley at a confluence.

**Why it matters.** Rubric row S1 and the lens: the anchor must be explainable with the unit's own evidence. A class
handed only a gauge record cannot reach the anchor's answer, and a "changed watershed" conclusion would overstate
the evidence.

**Fix (unit 4 anchor and What students learn).** Anchor question: "Two floods called rare in two years: how rare were
they, and how much did the built-over upland add?" Evidence named in the cell: the public-domain precipitation-
frequency estimates for the site (the federal rainfall atlas), the county's published hydrology study, and the
nearest long gauge (the Patapsco River) for the recurrence work. Check all three before the scope is written. LAYER
frame. REPEAT new.

### 4. Field and lab safety: two units missing from the safety read and five gaps in the rules (moderate; firm)

**What is wrong.**
- Unit 2 offers "a local road cut ... from safe ground well away from traffic", but unit 2 is not in the Safety read
  list and its row carries "Agent reads: sensitivity" only. Road cuts carry traffic and falling-rock hazards.
- Unit 7 has a hands-on day (wood rounds) and its row asks for a safety read, but the Safety read bullet lists units 1,
  3, 4, 5, 6, 8 and 9 only.
- Mineral sets: school mineral and rock kits often hold specimens that should not be handled freely (asbestiform
  serpentine, lead, mercury or arsenic minerals, uranium-bearing minerals). The course rules name none, and no
  handwashing after handling (NSTA safety guidance; from memory).
- Stream water: the row says "with gloves and handwashing ... never after rain"; the frame's course rule says "never
  after heavy rain" and drops gloves, handwashing and covering cuts. Urban streams after rain carry sewage overflow and
  bacteria.
- Unit 5: the common cloud-in-a-bottle recipe uses rubbing alcohol (flammable) or a pump; the rule says "pressure only,
  no matches or smoke" but does not rule out alcohol or a pumped bottle.
- Unit 8: "a desk lamp" with "the bulb is hot"; a halogen work lamp is a burn and fire hazard, and an LED lamp gives
  too little heat for the thermometer demonstration.
- Group rules differ: course rule "in groups with an adult", unit 1 "in pairs, an adult present", the row "in pairs,
  with the school's outdoor rules"; night observing in the row adds "or at a school evening event", the frame does not.

**Why it matters.** Safety is a door (rubric S5 and 3h). The writer copies the course rules onto each day's Safety and
set-up section; what the rules omit, the days omit.

**Fix (frame: Labs and materials course rules; Safety read bullet; units 1, 2, 5, 8 cells).** Add units 2 and 7 to the
safety read. Unit 2: "road cuts from photographs only; no visit". Course rules add: "mineral sets hold no asbestiform,
lead, mercury, arsenic or radioactive specimens; hands washed after handling rocks and minerals"; "stream work never
after rain, with gloves, cuts covered, hands washed"; "field work in pairs inside a group with an adult". Unit 5: "no
alcohol, no pump: a hand squeeze on a plastic bottle". Unit 8: "an incandescent bulb of 60 watts or less in a clamp
lamp; no halogen lamps". Night observing: add "or at a school evening event". LAYER frame. REPEAT yes (safety rule
gaps: chemistry 4).

### 5. Native nations content: sensitivity sources are named for unit 3 only (moderate; likely)

**What is wrong.** The task of the Sensitivity reads bullet is to name what the agent studies first. It does so for unit
3 but not for unit 1 (Monadnock's name "from an Abenaki word") or unit 9 ("a nation's star knowledge appears only from
that nation's own published material", with no nation or source named). Two further gaps:
- Unit 1: the name's language and meaning are themselves uncertain in published place-name work, and who speaks for
  the Abenaki in New Hampshire and Vermont is contested between recognised nations and state-recognised bands (from
  memory). A writer told only "an Abenaki word" may pick a source on one side.
- Unit 3: the anchor site, the Copalis River, lies in the homeland of the Copalis people, whose descendants are today
  (from memory, check) among the Quinault Indian Nation and the Confederated Tribes of the Chehalis Reservation. The
  frame names the Huu-ay-aht, Makah and Quileute accounts of 1700 (right) but not the nation whose land the drowned
  forest stands on.

**Why it matters.** The brief asks for sensitivity sources named before writing; an unnamed source becomes the writer's
own pick from a search.

**Fix (frame: Sensitivity reads; units 1, 3 and 9 cells).** Unit 1: "the agent first studies a published place-name
source for Monadnock and the W8banaki Nation's (Odanak and Wôlinak) own published material; the unit says the name is
from an Algonquian language, usually given as Abenaki, that its meaning is uncertain, and takes no side between
groups". Unit 3: "the Copalis River is in the homeland of the nations named in the Quinault Indian Nation's and the
Chehalis Tribe's own published material; the unit names them in one line". Unit 9: either "no nation's star knowledge
is used" or name the nation and its published source now. LAYER frame. REPEAT new.

### 6. Days do not follow the load the frame itself states (moderate; firm)

**What is wrong.** The Days line says the field and lab units (1, 4, 5) carry more and the record-reading units (2, 6, 8)
less. Days per owned outcome: unit 1, 16 for 4 (4.0); unit 2, 15 for 3 (5.0); unit 3, 18 for 3 (6.0); unit 4, 17 for 3
(5.7); unit 5, 17 for 2 (8.5); unit 6, 15 for 2 (7.5); unit 7, 17 for 2 (8.5); unit 8, 16 for 2 (8.0); unit 9, 18 for
3 (6.0). Course mean 6.2. Unit 1, the heaviest field and lab unit (a field map, a contour unit, mineral tests and
rock classification, plus the anchor, a class model and the end-of-unit assessment), has the fewest; unit 8, a
record-reading unit, has the third most.

**Why it matters.** Unit 1 is where the map-model and the lab routines are built for the whole year; a squeezed unit 1
leaves field mapping to one rushed day.

**Fix (frames.csv unchanged at 160; frame unit 1 and 8 day cells, the weeks in each row, the Days line).** Unit 1 to 18
days, unit 8 to 14 (8.0 then 7.0 an outcome; still above the mean, as the energy-balance and image-argument work
needs). Rewrite the Days sentence from the counts: "unit 1 carries the most outcomes and the field and lab routines;
units 5 and 7 carry a running log or a model; units 2 and 6 carry the fewest days". LAYER frame. REPEAT yes (unit days
against load: psychology 5, biology 1).

### 7. The CUR-ESS set leaves out volcanoes and severe storms (moderate; judgment call)

**What is wrong.** The 24 outcomes are in our own words, quantitative and well beyond the core rows; the wording reads
as original (no exam framework phrasing seen). As a full-year Earth and space course the set has two gaps a district
committee would notice: volcanic hazards and their monitoring (Physical Geology 4.4 and 4.5 left out; unit 3 names
the Cascade volcanoes "as context only, with no days") and severe storms (JetStream's tropical cyclone, thunderstorm
and tornado lessons all left out; lake-effect snow is the only weather hazard). Glaciers and landslides are also out,
which is defensible for a deepening elective. Both gaps fit units that already build the needed ideas: volcanoes in
unit 3 (the same subduction zone, with a dated eruption record), hurricanes in unit 5 (latent heat is CUR-ESS.14's
core idea, and unit 5 has 8.5 days an outcome).

**Why it matters.** Completeness is half of the question this read was asked; a course that names Cascadia but not
Mount St. Helens, or teaches the energy of condensation without the storm it powers, leaves the most-asked student
questions unanswered.

**Fix (standard file, rows, units 3 and 5).** Add two outcomes, for example "Read a volcano's monitoring record
(earthquakes, ground swelling, gas) and its eruption history to state its hazard" (unit 3, row ess-cascadia-hazard)
and "Explain how a tropical cyclone draws its energy from warm ocean water and condensing vapour, and read its track
and intensity forecast" (unit 5, row ess-atmosphere-moisture), with no added days. Renumber CUR-ESS after them. This
changes scope: see For Cory. LAYER standard. REPEAT new.

### 8. Anchor figures and wording to correct (minor; likely, from memory)

**What is wrong, each with its fix (frame unit cells).**
- Unit 1: Monadnock's summit is schist and quartzite of a formation that also underlies parts of the lowland around it
  (from memory); the contrast is resistance to wear, not a different rock kind. Write "a hard, quartz-rich metamorphic
  rock that wears down more slowly than the rock around it", checked on the state bedrock map. The "about 600 metres"
  relief holds (summit about 965 m).
- Unit 2: the Siccar Point sandstone dips gently; "nearly flat" becomes "gently tilted". 1788 and Hutton are right.
- Unit 5: totals south of Buffalo reached about 2 metres in places (from memory, about 88 inches at the highest site);
  write "up to about 2 metres of snow fell in three days".
- Unit 6: the tropical Pacific buoy array was built from the mid-1980s and completed in the 1990s, so the 1972 case is
  read from ship and coastal temperature records and the catch record; the buoy records serve the later El Niños.
  Say so in the cell.
- Units 3, 7, 8 and 9 checked and right: 1699 last rings and January 1700 (tree-ring and Japanese records); about
  11,700 years ago and several degrees in decades (layer-counted Greenland cores); Jezero's delta; TRAPPIST-1's seven
  transiting planets. "About thirty times the energy" per magnitude step is right (10 to the 1.5).

**Why it matters.** Anchor numbers go straight into student pages; rubric row S10. LAYER frame. REPEAT yes (anchor
accuracy: chemistry 5).

### 9. Two outcomes claim more than their method gives (minor; firm)

**What is wrong.** CUR-ESS.23 infers "each star's size, mass and stage of life" from the brightness-temperature
diagram; mass follows from it only on the main sequence. CUR-ESS.24 works out a planet's distance with Kepler's third
law; for any star but the Sun this needs the star's mass (about 0.09 Sun masses for TRAPPIST-1), and Physics used only
the Sun-centred form with a supplied coefficient (phys-orbits note).

**Fix (standard file; row ess-stars-exoplanets boundary).** CUR-ESS.23: "... infer each star's size and stage of life,
and the mass of a main-sequence star". Boundary adds: "the star's mass is supplied; distance from a cubed equals
star mass times period squared, in Sun masses, years and astronomical units". LAYER standard. REPEAT new.

### 10. Source map housekeeping (minor; firm)

**What is wrong.** The brief asks that every base lesson be placed in one unit or left out with a reason. Four places
put a section in two units (Astronomy 1.4 in 8 and 9; Astronomy 5.1 and 5.2 in 8 and again in 9's "5.1 to 5.3";
JetStream Energy Balance in 7 and 8) and three are neither placed nor left out (Physical Geology 3.2 and 3.3
"teacher background only"; Webb ch 12 "none | 7 (teacher background ...)"). Every other chapter and section matches
the scout's tables of contents; no NC or reference-only source is mapped; Astronomy is credited as 1e with its archive
revision; Physical Geology's excluded figures (19.3.8 among them) are named.

**Fix (Source map).** Place each in its first-use unit and write "returns in unit n" for the later one; write the three
teacher-background entries as "left out as student reading: teacher background for unit n". LAYER base text. REPEAT
new.

### 11. The Environmental Science seam misses two touches (minor; firm)

**What is wrong.** Both frames say the courses share "a watershed but not a skill". Two more touches exist: Environmental
Science unit 9 (Philadelphia's green stormwater: porous paving, rain gardens, runoff) against CUR-ESS.12 ("how paving,
drainage and lost vegetation change floods"); and Environmental Science unit 5 (contaminants from mine waste in wells,
CUR-ENV.10) against Physical Geology 14.4 (groundwater quality), mapped to unit 4.

**Fix (both frames' "Beside this course" prose; Source map row 14).** Add: "this course explains why paving raises
flood peaks; Environmental Science unit 9 designs and weighs the fixes"; and Physical Geology 14.4 "left out:
contaminant movement is Environmental Science unit 5's; unit 4 keeps to flow direction". LAYER frame. REPEAT yes (a
seam missing on the other side: psychology 9).

### 12. Two Check set candidates do not quote the appendix wording (minor; likely)

**What is wrong.** Unit 5's practice element ends "explanations or forecasts"; the appendix F high school element reads
"... currently accepted explanations or solutions to determine the merits of arguments". Unit 3's nature of science
element "scientific knowledge is strengthened when independent lines of evidence agree" is not appendix H wording (from
memory); the appendix element is "science arguments are strengthened by multiple lines of evidence supporting a single
explanation", which the frame gives to unit 7. **Fix:** see Settled by the expert. LAYER frame. REPEAT new.

### 13. Stale note in the Physics frame (minor; firm)

**What is wrong.** docs/courses/physics/frame.md line 72: the electives' "frames, when written, say what they pick up".
This frame is written and its Seams say it. The frame lists this for the lead (item 5) but the note stays stale until
changed. **Fix:** "Earth and Space Science picks up the Earth and space threads (docs/courses/earth-and-space-science/
frame.md, Seams); Environmental Science picks up the human impact threads (its frame, Seams)." LAYER process. REPEAT yes
(stale same-year notes: chemistry 3, physics 6, psychology 11).

### 14. Three practical gaps in the field work and paper path (minor; judgment call)

- **Sky log.** Unit 9 runs in weeks 28 to 31 (late spring, late dark, 18 days, under one lunar month counting cloudy
  nights). Start the paper sky log on unit 8's first day (week 25), allow daytime Moon observations, and keep the
  supplied sky record for any student who cannot observe.
- **Live forecast.** Unit 5's forecast for a named place needs current maps; the paper path names archived cases only.
  Add: "the teacher prints the day's surface map and sounding; on a day without them, an archived situation".
- **Measured heights.** CUR-ESS.2 asks for measured heights but the row's boundary allows only a compass and a tape.
  Add a protractor-and-string clinometer (or a hand level from a straw and a level) to the boundary and the materials
  list.

LAYER frame. REPEAT new.

## Checked and found right (do not undo)

- Ownership: 19 rows, each in one unit; CUR-ESS.1 to 24 each in one unit and taught in full as worded (CUR-ESS.11's
  "how fast and how high a stream rises" is the hydrograph; CUR-ESS.13 adds drawdown).
- Every ~CODE named against its true owner and unit: HS-ESS2-1, 2-3, 1-5 (Physics 9); 1-6 (Physics 10); 1-4 (Physics
  3); 1-3 and 1-1 (Physics 8); 2-5 (Chemistry 3); 2-2, 2-4, 3-5 (Chemistry 9); 3-1 (Chemistry 11); design practices
  in Biology 9 and 10 and Chemistry 7.
- Genuine deepening where it counts: Chemistry dates with dice and no logarithms, here ages are solved with logarithms;
  Physics gives plate separation as a supplied number, here students fit position records; Chemistry runs no climate
  model, here students step one; no H-R diagram is taught in Physics unit 8, so CUR-ESS.23 is new.
- Handoffs: each retrieval or readiness call matches the last real use (for example s8-earth-sun-moon last used in
  Chemistry unit 9, so a readiness check before unit 9; chem-thermal-equilibrium carried by Physics, so retrieval).
- Weeks: cumulative days put every unit in the weeks its row states, and the three checks in weeks 10, 21 and 32.
- Anchors do not reuse any K to 12 anchor (Physics's Atlantic floor and meteorites, Chemistry's sea ice and deltas,
  Biology's cod and Elwha, grade 6's 2011 Japan quake, Environmental Science's cases).
- Licence rules: Astronomy credited as 1e only, JetStream never as official, Physical Geology's excluded figures never
  reused, Webb's figures checked one by one. BASELINE rule 5 for deep time and climate. Unit 2 never asks a student to
  declare a belief. The Sun rule.

## Grade placement

The frame's grade 12 is right. Every unit leans on a Physics row (grade 11) or an Algebra II skill (logarithms,
rational exponents, grade 11), and a grade 9 Earth science course would now duplicate the Earth and space expectations
folded into Biology, Chemistry and Physics. The frame's reasoning against grades 11 to 12 holds (units 1 to 3 come
before Physics unit 9 in the same year). The cost is audience: the course becomes one for students who have taken
Physics and Algebra II, which many seniors have not. That is Cory's call (For Cory 1).

## Seams

Picked up: every row Physics, Chemistry and grades 6 to 8 hand on to an ess- row is in the table, with the right kind.
Handed on: none (last course in the thread); the "Where each thread ends" table is complete. Beside: see finding 11.

## Cross-subject

All math leans fall in earlier years and are correct (Geometry unit 4 trig for parallax and slope; Algebra II units 2,
3 and 4 for inverse square, rational exponents and logarithms). The World History I lean is fine. Nothing leans on this
course.

## The lens checklist (course frame layer)

| Lens line | Result |
|---|---|
| A performance expectation for the grade has no unit, or a unit claims one it only touches | Not applicable for NGSS (owns none); met for CUR-ESS; the ~CODE deepening claims hold except where finding 2 shows re-teaching |
| Grades 6 to 8 order against OpenSciEd | Not applicable |
| High school: band expectations with no owner plan | Met: owners named per unit |
| No unit names its anchor or design problem | Met: nine anchors. No unit is framed as a design problem; acceptable for an elective owning no engineering code, with unit 3's town advice using design practices |

## What I could not judge

- The Ellicott City gauge history and hydrology study, Monadnock's bedrock, and the Copalis River nations rest on
  memory (findings 3, 5, 8); each fix names what to check.
- No data/plans/earth-and-space-science/source-map.csv exists; the checklist in PRODUCTION-PATH (After the core
  subjects, item 1) requires one in the gated layout before a writer runs, not at frame stage.
- Whether ELA 12's process pieces miss unit 3 and unit 7's long writing weeks: the frame defers this to the scope.

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Unit 8's greenhouse model is single-layer first, then the number of layers fitted for Venus | The single-layer failure is the evidence that Venus's thick air matters; keeps the math at a fourth root | data/progressions/science.csv (ess-planetary-climates boundary); frame unit 8 |
| Unit 1 to 18 days, unit 8 to 14 | Puts days where the field and lab load is; total unchanged | frame units 1 and 8, Days line |
| Unit 5 anchor figure "up to about 2 metres"; unit 2 "gently tilted"; unit 1 "a hard, quartz-rich metamorphic rock that wears down more slowly" | Accuracy, smallest wording change | frame units 1, 2, 5 |
| Unit 4 anchor question "how rare were they, and how much did the built-over upland add?" | Answerable from rainfall frequency, a gauge and the published study | frame unit 4 |
| Check set: unit 3 takes "science arguments are strengthened by multiple lines of evidence supporting a single explanation"; unit 7 takes "most scientific knowledge is quite durable, but is, in principle, subject to change based on new evidence and/or reinterpretation of existing evidence"; unit 5's practice ends "explanations or solutions to determine the merits of arguments" | Appendix H and F wording; unit 3 is where independent lines meet, unit 7 is where a model fails and is revised | frame units 3, 5, 7 |
| Sky log starts on unit 8's first day, daytime Moon allowed | Six weeks of observing instead of under four, in late spring | frame units 8 and 9; row ess-sky-observation |
| Mineral sets exclude asbestiform, lead, mercury, arsenic and radioactive specimens; hands washed after handling | Standard school earth science safety practice | frame Labs and materials |

## For Cory

1. **Grade.** Change data/courses.csv for earth-space to grades 12, typical 12, and state in the catalogue that the
   course follows Physics and Algebra II. This narrows who can take it; the alternative (grades 9 to 12) would need a
   different course.
2. **Two added outcomes** (finding 7): volcanic hazard in unit 3 and tropical cyclones in unit 5, no added days. Yes
   adds CUR-ESS outcomes and renumbers; no keeps the course as framed, with volcanoes as named context.

Not logged in the defect ledger: the brief allows edits to this report only. The caller may log findings 1 to 14 with
found_by `expert`.

## Sources

- docs/courses/chemistry/s09.md, docs/courses/physics/s08.md and s09.md, data/progressions/science.csv: what the core
  courses already teach (finding 2, Checked and found right).
- Base-text scout notes 2026-11-16, section 4: tables of contents and licences for the Source map check (findings 2, 10).
- From memory, not opened: standard planetary radiative balance (finding 1; Astronomy 1e 10.3 treats Venus's
  greenhouse); Yamaguchi and others 1997 and Satake and others 1996 on the 1700 Cascadia earthquake (unit 3 dates);
  the Greenland layer-counted chronology (unit 7); the Howard County flood studies and the federal rainfall atlas
  (finding 3); NSTA safety guidance on mineral specimens (finding 4); NGSS appendices F and H (finding 12).

## For the source list

- The federal precipitation-frequency atlas (public domain) and the county's Ellicott City hydrology study, for unit
  4's anchor evidence. Not opened in this read.
- The state bedrock geologic map of New Hampshire (public), for unit 1's anchor rock.

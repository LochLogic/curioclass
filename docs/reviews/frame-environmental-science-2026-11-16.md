# Frame read: environmental-science (Environmental Science, grade 12 elective), 2026-11-16

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md (high school Gateway 2 and rows S1 to
  S13), docs/PRODUCTION-PATH.md (After the core subjects), DESK-ANSWERS (q-hs-science-core, the 2026-11-15 elective
  checklist), AGENTS.md.
- The frame docs/courses/environmental-science/frame.md in full; its row in data/plans/frames.csv (9 units, 160 days,
  year); the 20 env- rows of data/progressions/science.csv (standard, assumes, models, cross_subject, notes); the
  CUR-ENV.1 to CUR-ENV.21 lines of data/standards/curio-science-electives.txt. There is no
  data/plans/environmental-science/ folder yet; the day-level source-map.csv comes with the scope and sequence
  (PRODUCTION-PATH step 3), so the frame's Source map section is what I checked.
- The Source map against the base-text scout's tables of contents and licence notes
  (side-session-notes/.../base-text-scout-2026-11-16.md, section 5: Harris pick, Fisher runner-up).
- Frames compared unit by unit: docs/courses/biology/frame.md, chemistry/frame.md, physics/frame.md (units tables and
  the rows they own), science-grade-7/frame.md (units 5 and 6), the grade 6 frame where it treats erosion;
  beside it in grade 12: earth-and-space-science/frame.md, us-government-and-politics/frame.md, economics/frame.md,
  us-history-ii/frame.md (unit 6, redlining). docs/sources/BASE-TEXTS.md and data/courses.csv for the pending notes.
- Earlier reads of the same layer, for REPEAT tags: frame-biology-2026-11-14.md, frame-chemistry-2026-11-14.md,
  frame-psychology-2026-11-16.md (and the list of all frame reads in docs/reviews/).
- Gates: `python -X utf8 scripts/plan.py check` exits 0; frame environmental-science: 0 failures, 9 units, 160 days
  (149 in units, 11 for checks and respond days). `python -X utf8 scripts/stale.py check`: 62 files, 0 failures.
- Outside checks of the anchor figures (web, 2026-11-16): Dorcas et al. 2012 (Everglades), the Richmond 2017 heat
  mapping accounts, Wang et al. 2016 (Yellow River). Other figures rest on memory and are marked so.

Not logged with `plan.py defect`: the brief allows no edit but this report. The caller logs them.

## Verdict

The frame is sound in shape: every one of the 21 outcomes sits in exactly one unit, every NGSS expectation it says it
deepens is really owned by the core course and unit it names (all 18 checked), the "goes past" lines mostly hold, the
nine anchors are real, specific and unused elsewhere in the catalogue, and the paper path, no-kit path and values
rules are the right ones. The biggest risks are a course that is not yet complete for a full year of environmental
science (no outcome teaches water supply, solid waste, or dose-response and biomagnification, though the Source map
sends those base chapters into units), and a field safety page with a contradiction (oxygen tests under a
strips-only, no-liquid-reagent rule) and gaps (eye protection, ticks). The one change that matters most is to widen
three outcomes (finding 2), which is Cory's call; everything else is a frame edit with no change to the unit list.

## Findings, most serious first

### 1. The course safety rules contradict an outcome and miss two standard hazards (serious; likely)

LAYER frame. REPEAT yes (the chemistry frame read named missing controls).

**What is wrong.**
- CUR-ENV.7 and unit 3 name dissolved oxygen among the chemical tests, but the course rule is "water test sets of the
  strip type, with no liquid reagents". There is no reliable strip test for dissolved oxygen: classroom oxygen kits
  use liquid or tablet reagents (the Winkler-type kits carry a sulfuric acid step and, in some, sodium azide) or
  sealed glass ampoules, and the reagent-free path is an electronic meter most schools lack (from memory; the kit
  makers' safety data sheets would settle it).
- No course rule names eye protection, though settling jars, water sampling, the soil tests (an organic-matter test
  is usually done with hydrogen peroxide) and the leaching model can splash. The science lens asks for eye
  protection "where anything can splash or fly", and rubric row S5 fails a hazard named without its control.
- Unit 1 opens the year in late summer grass and meadow edges, yet ticks are not named (only stinging plants and bees).
- Unit 3's kick-net animals are handled in trays; the frame says "no handling of animals" for units 1 and 7 but gives
  unit 3 no humane-handling line (keep them wet and shaded, return them to the stream).

**Why it matters.** A writer following the rule list writes an oxygen test the rules forbid, or a strip test that does
not exist; S5 is a door, and the safety agent will fail the course page for missing eye protection.

**Fix.** In Labs and materials, add: "Eye protection for every soil, water and leaching activity. Long trousers,
socks over trouser legs and a tick check after field work in grass or woods. Stream animals are kept in shaded
water in white trays and returned where they were found." For dissolved oxygen, state one of: (a) oxygen read from
published monitoring records or a loaned meter, with strips for nitrate, pH and the transparency tube for turbidity;
or (b) a sealed-ampoule oxygen kit allowed as the one exception, with eye protection, gloves and the broken-glass
control. Edit CUR-ENV.7's unit cell and the env-water-quality note to match. I recommend (a): it keeps the
no-liquid-reagent rule whole.

### 2. The outcomes leave out three topics a full-year environmental science course is expected to teach (serious; likely)

LAYER standard. REPEAT new.

**What is wrong.** CUR-ENV.1 to 21 are in our own words, measurable, and rigorous where they reach (designed
experiments against correlation, sampling error, rival causes, exposure). But checked against the base text's own
table of contents and the common shape of a year course (the AP Environmental Science course description, used as a
reference for scope only), three topics have no outcome:
- **Water supply and use**: the water cycle as a supply, groundwater depletion, irrigation, dams and diversion.
  Harris 7.1 and 7.2 and the Aral Sea case (7.5) are mapped to unit 3, but CUR-ENV.6 and 7 are about nutrients,
  water quality and treatment. A writer will either drop those sections or teach them with no outcome to assess.
- **Solid and hazardous waste**: landfills, recycling and composting, waste reduction. Harris 12.1 and 12.2 are
  mapped to unit 5 "as mine waste", which uses almost none of what those sections teach; 12.3 goes to unit 9 as a
  policy route.
- **Toxicology**: dose-response, thresholds and the dose that harms half a test group, persistence,
  bioaccumulation and biomagnification (mercury, the old pesticide story). CUR-ENV.11 judges exposure, but the
  env-exposure-risk boundary says "no toxicology models", and Harris 6.3 (environmental toxicology) is in the
  chapter 6 cell with no unit named (finding 8).
Nothing in Biology, Chemistry or Physics teaches any of the three (I read their units tables and the rows they own),
so leaving them out is not "not teaching twice"; it is a gap.

**Why it matters.** Gateway 2 for a course with its own outcomes is read on whether those outcomes cover the course
the title promises. A teacher adopting "Environmental Science" will look for water use, waste and biomagnification
first; their absence is the first thing an adoption committee notices.

**Fix (Cory's, it changes what the course teaches).** Widen three outcomes, no new unit and no new row:
- CUR-ENV.7 (or a new CUR-ENV.7 split): "...and explain where a town's water comes from, how pumping and
  diversion draw down groundwater and rivers, and how treatment can fail." Unit 3 gains the Aral Sea as a supply case.
- CUR-ENV.10: "Trace a material from extraction to waste, including the waste a town makes and how it is reduced,
  reused, recycled or landfilled, and explain how contaminants move from waste into water, soil and air."
- CUR-ENV.11: "...judge a health risk from exposure data and a dose-response relation, explain how persistent
  substances build up in bodies and food chains, ..." and lift the env-exposure-risk boundary to "dose-response and
  biomagnification read from published data; no toxicology models built".
Days: finding 6 gives the counts with and without the widening.

### 3. Unit 5 links uranium harm to DNA change, but in drinking water uranium harms mainly as a chemical (serious; likely)

LAYER progression and frame. REPEAT new.

**What is wrong.** Unit 5 and env-exposure-risk name HS-LS3-2 (radiation and chemicals change DNA) as the idea they
deepen, and the readiness handoff is bio-sources-of-variation. For people drinking from wells near abandoned
uranium mines, the main documented harm of uranium itself is chemical damage to the kidneys; arsenic and other metals
often come with it; for miners and homes built with waste rock, radon and its decay products in air (lung cancer) are
the radiation route (from memory: the federal toxic-substances registry's uranium profile and the federal
environment agency's Navajo Nation pages; the safety and sensitivity agents should confirm). A unit built on "the
cause is now an exposure measured in a real place" with DNA change as its only mechanism would teach a false
simplification (rubric S10: "a simplification that is false, not just simple").

**Why it matters.** S10 is a door. It also matters for the community: the Nation's own studies are about kidney
disease, metals and birth outcomes, not only cancer.

**Fix.** In unit 5's What students learn and the env-exposure-risk note: "Exposure pathways are matched to their harm:
uranium in water as a chemical (kidney) toxin, radon in air as a radiation (lung) risk, and the other metals found
with it; DNA change is the radiation route only." Keep ~HS-LS3-2 but add the matching boundary.

### 4. Two causal claims are given before the evidence: unit 8's question and unit 4's outcome (moderate; likely)

LAYER frame and standard. REPEAT yes (the science reads' S1 point: an anchor that gives its answer away).

**What is wrong.**
- Unit 8's compelling question asks "how did decisions made ninety years ago help make it so?" The frame's own
  outcome (CUR-ENV.18) asks students to argue each link in the chain on its own evidence, and the published record
  supports that care: the heat-redlining association is strong across cities (the 2020 study of 108 cities from the
  same Richmond team), but the 1930s grades also recorded conditions that already existed (density, industry,
  rail lines), so the history-to-heat link is argued, not given (from memory for the second point; the sensitivity
  agent's reading list should include one study that tests the link against those prior conditions). A question that
  states the answer makes the unit a confirmation, fails S1, and puts a contested causal claim on students before the
  evidence, which is the values-rule (b) risk the frame is otherwise careful about.
- CUR-ENV.9 asks students to "explain ... which policies and prices drove the change". Units 2, 7 and 8 all weigh rival
  causes; unit 4 does not. Britain's coal fall has several candidate causes (the carbon price floor from 2013, gas
  prices, European plant-emission rules, renewables growth, falling demand), and the policy reading is the one most
  open to a political frame.

**Fix.** Unit 8's question: settled below. CUR-ENV.9 and the unit 4 cell: "...and weigh which policies, prices and
other changes drove it, against rival explanations, from grid records." Add to unit 4's Candidate the nature of
science element on weighing alternative explanations (it is already used in unit 7).

### 5. Unit 8 carries three outcomes, one not driven by its anchor, and its field walk falls in late winter (moderate; likely)

LAYER frame. REPEAT new.

**What is wrong.** Unit 8 (17 days) owns air pollutant formation and long-term monitoring (CUR-ENV.16), a field heat
transect (CUR-ENV.17) and a history-to-exposure argument (CUR-ENV.18). The anchor (a hot block) needs 17 and 18; 16 (particles,
ozone, sulfur and nitrogen oxides, inversions, clean air rules over decades) is a full topic the anchor does not ask
for, so it risks being the "separate report" S1 fails. The unit runs in weeks 24 to 28, roughly March into April in
a late-August start, while the course rule speaks of "summer heat walks": in many climates air-temperature
differences between blocks are small then, though sunlit surface differences (asphalt against grass) stay large.

**Fix.** In unit 8's cell, route the question board to CUR-ENV.16 through the anchor: "the hottest blocks are also
the ones with the most ozone days and the busiest roads; why would heat and traffic make worse air?" (ozone forms
faster in heat and sunlight, which also uses chem-reaction-rates where the row says it does). State the walk is on a
clear, sunny day with surface readings as the main measure and air readings secondary, with the 2017 summer data as
the comparison set. Give the unit 18 days (finding 6).

### 6. Days do not follow load, though the frame says they do (moderate; firm)

LAYER frame. REPEAT yes (biology and chemistry frame reads).

**What is wrong.** The brief bullet says "the field units (1, 3, 8) and the capstone (9) ... carry more, the
data-reading units less". The counts are 16, 16, 17, 16, 16, 16, 16, 17, 19: flat. Unit 1 has 3 outcomes, a
readiness check, the first field work of the year and the course's sampling habits in 16 days (5.3 an outcome);
units 4 and 6 have 2 data-reading outcomes in 16 days (8 an outcome); unit 8 has 3 outcomes and a field walk in 17.

**Fix.** Units 1 to 9: 18, 16, 17, 15, 15, 15, 15, 18, 20 (149, unchanged total). Recompute the week ranges in the
units table and Cross-subject (unit 1 runs to week 4, unit 9 to week 31; the Algebra II and social studies leans keep
their kinds, which I checked against the new weeks). If Cory widens the outcomes in finding 2, units 3 and 5 each
take one day from units 2 and 7 instead: 18, 15, 18, 15, 16, 15, 14, 18, 20 (149).

### 7. A grade 11 taker's social studies leans have no one-lesson version, though the frame says each row names one (moderate; firm)

LAYER frame. REPEAT yes (if-later lines, earlier frame reads).

**What is wrong.** The sentence after the social studies table says "every social studies lean above is then an
if-later case, and the unit's own one-lesson version (named in each row) carries it". Eight rows say only "Earlier
this year: retrieval" and name no version: gov-federalism (unit 5, tribal nations as governments), econ-scarcity-choice
(unit 7), gov-policy-debates (unit 8), us2-postwar-domestic (unit 8, redlining), econ-government-role (unit 9),
gov-local-action and gov-federalism (unit 9). Two carry the year's hardest content: a grade 11 taker reaches unit 5
with no teaching of tribal sovereignty and unit 8 with no teaching of redlining.

**Fix.** Add an if-later line to each of the eight, as the earlier rows do. Unit 5: "If later: one lesson on tribal
nations as governments, from the Nation's own government pages, before the cleanup decisions." Unit 8: "If later:
one lesson on the 1930s lending maps from the maps themselves, before the temperature data." Unit 9: the route
lesson names the levels of government in its own terms. Unit 7: opportunity cost in its own terms (as unit 6
already does).

### 8. Source map: sections listed but not placed, and one transfer case that does not test its unit (moderate; firm)

LAYER base text. REPEAT yes (the psychology read: flags and placements pinned loosely).

**What is wrong.** Checked against the scout's table of contents: every chapter and every non-resources section is
listed, and the Chapter Resources sections are correctly left out as readings. But:
- Chapter 6 lists "6.1 to 6.4; 6.5" and its unit cell places only 6.4 and 6.5; 6.1 (impacts of environmental
  conditions), 6.2 (environmental health) and 6.3 (environmental toxicology) have no unit, while "None left out" is
  claimed.
- Chapter 9 lists "9.1 to 9.5" and places only 9.4; 9.1 (soil profiles), 9.2 (soil-plant interactions), 9.3
  (conventional agriculture) and 9.5 (sustainable agriculture), the sections unit 2 needs most, are unplaced in words.
- 7.5 (the Aral Sea) is unit 3's transfer task, but it is a case of water diversion for irrigation; it does not test
  CUR-ENV.6 or 7 (nutrients, quality, treatment) as now written.
- 12.1 and 12.2 (municipal and hazardous waste) mapped "as mine waste" (finding 2).
- 3.3 (terrestrial biomes) is placed in unit 1 as "the meadow and schoolyard in their biome": fine as a framing
  reading, but say it is one reading, not a biome survey.

**Fix.** Chapter 6 cell: "5 (6.1 to 6.3, exposure, health and toxicology; 6.4 bioremediation as one cleanup choice;
6.5 Love Canal as the unseen transfer case)". Chapter 9 cell: "2 (9.1, 9.2 soil; 9.3, 9.5 practices judged; 9.4 as
one reading bridging to unit 3's runoff)". 7.5: placed with the widened CUR-ENV.7 if Cory agrees (finding 2), else
"left out: a water supply case, not a water quality one"; unit 3's transfer case is settled below.

### 9. Earth and Space Science, beside it in grade 12: three ideas both courses need, with no line for either order (moderate; likely)

LAYER frame. REPEAT new.

**What is wrong.** The Beside prose says the two share "a watershed but not a skill" and that a student taking both
meets no repeated lesson. Three ideas sit in both courses in the same year:
- **Watershed** as a drainage area: this course's unit 3 (weeks 7 to 10) traces nutrients "through a watershed";
  Earth and Space Science unit 4 (weeks 11 to 14) outlines watersheds on a map (CUR-ESS.11).
- **Groundwater flow**: this course's unit 5 (weeks 14 to 17) needs leaching to groundwater and wells; Earth and Space
  Science unit 4 (weeks 11 to 14) teaches porosity, the water table and flow (CUR-ESS.13).
- **Inversions**: this course's unit 8 (pollutants trapped); Earth and Space Science unit 5 (lapse rates, weeks 14 to 18).
A student taking only this course needs each taught here at the depth the unit uses; a student taking both meets each
twice unless the second one is retrieval.

**Fix.** Under "Beside this course", one line per idea: "Taught here in its own terms (one part-lesson: <what>); a
student who has had Earth and Space Science unit <n> earlier this year meets it as retrieval." Mirror the three lines
in the Earth and Space Science frame's Beside section when that frame is next touched.

### 10. Unit 5's sensitivity reading list misses the Nation's research rules and naming (moderate; likely)

LAYER frame. REPEAT new.

**What is wrong.** The list is good: the Navajo Nation Environmental Protection Agency, the Navajo Birth Cohort
Study's community reports, the Navajo Times, and a Native journalists' association's guide. It misses: the Navajo
Nation Human Research Review Board, which governs research and data about the Navajo people (only material the
Nation has already released may be used, and no class "study" of community health is designed); the Diné name the
people use for themselves; the Nation's own uranium commission's reports; and the 1979 Church Rock tailings spill,
which the Nation's accounts treat as central. The association should be named in this planning document so the agent
finds it (the Native American Journalists Association's reporting guide); naming it here is not student copy.

**Fix.** Add to the Sensitivity reads bullet for unit 5: "the Navajo Nation Human Research Review Board's public rules
(only data the Nation has released; no class collection of health information), the Navajo Nation's uranium
commission reports, the Church Rock spill in the Nation's own accounts, and the Native American Journalists
Association's reporting guide; the unit uses 'Diné' and 'Navajo Nation' as the Nation does."

### 11. Anchor figures: four check out; one wording over-attributes the cause (minor; firm)

LAYER frame. REPEAT yes (the psychology read: figures carried from memory).

**What checks out.**
- Everglades: Dorcas et al. 2012 (PNAS 109: 2418 to 2422): night road surveys 2003 to 2011 against the 1990s
  baseline found raccoon sightings down 99.3 per cent and opossums down 98.9 per cent, steepest in the south; surveys
  north of the park, where pythons were not yet found, matched the old numbers. That second set is the
  "places the cause has not reached" control CUR-ENV.14 asks for: name it in unit 7's cell.
- Richmond: on 13 July 2017, volunteer teams with home-made sensors on cars and bicycles measured differences of up
  to 16 degrees Fahrenheit (about 9 degrees Celsius) across neighbourhoods; the hottest were often those graded
  hazardous in the 1930s. The frame's "about 9 degrees Celsius" is right. "One summer afternoon" is fair (the
  campaign ran morning, afternoon and evening traverses; the 16 degree figure is the afternoon one).
- Loess Plateau: Wang et al. 2016 (Nature Geoscience 9: 38 to 41) report the Yellow River's sediment load down about
  90 per cent over 60 years. But they attribute it to reservoirs and dams, engineering measures (terraces, check
  dams), revegetation and climate together. The anchor's "after decades of terraces, check dams and replanting ...
  fell by about nine tenths" reads as if the slope work alone did it, which the unit then has to undo.
- From memory, consistent: Toledo, 2 to 4 August 2014, about 400,000 to 500,000 people told not to drink or boil the
  water (microcystin); Britain's coal share about 39 to 40 per cent in 2012 and Ratcliffe-on-Soar closing on 30
  September 2024; more than 500 (about 523) abandoned uranium mines, 1944 to 1986; the Nation's 2005 ban; Philadelphia's
  Green City, Clean Waters plan approved in 2011; Japan's population peaking about 2008 to 2010; Niger's fertility
  about six and growth above 3 per cent (recent United Nations estimates). The scope writer pins each to a source.

**Fix.** Unit 2's anchor wording: settled below. Name the Dorcas north-of-park comparison in unit 7's cell.

### 12. Two seams the unit cells do not name (minor; firm)

LAYER frame. REPEAT yes.

**What is wrong.** Grade 7 unit 5 (s7-biodiversity-solutions, MS-LS2-5: competing designs for keeping biodiversity and
ecosystem services, the oil palm case) is the earliest teaching of conservation choices, and unit 7's "what is new"
names only Biology. HS-ESS3-3 (Biology unit 10: a simulation of resource management, population and biodiversity) is
the expectation unit 6 and unit 7 deepen most directly, but neither names it.

**Fix.** Unit 7: "Grade 7 judged designs for one ecosystem with supplied criteria; Biology tested a rule in a
simulation; here real programmes with measured results and costs." Add "~HS-ESS3-3 (owned by Biology, unit 10)" to
unit 7's deepens list and the env-conservation-strategies standard cell.

### 13. Small inconsistencies (minor; firm)

LAYER frame and progression. REPEAT yes.

- Seams row for bio-sources-of-variation (unit 5): for a grade 11 taker the row was last used in Biology, grade 9,
  two years back, so the rule calls for a readiness check, not "the unit restates the idea in one lesson". Fix: "a
  grade 11 taker gets the readiness check in the last ten minutes of unit 4's last day; one-lesson reteach if missed".
- Heading "Picked up from Biology, Chemistry and grades 7": "grade 7".
- The brief bullet's day-load sentence (finding 6) is rewritten with the new counts.

## Lens checklist (course frame layer and the progression items a frame touches)

| Lens line | Result |
|---|---|
| An expectation for the grade has no unit, or a unit claims one it only touches | Not applicable for NGSS (the course owns none). For its own outcomes: met, all 21 placed once; three outcomes too narrow for the course (finding 2) |
| Grades 6 to 8 OpenSciEd order | Not applicable |
| High school: band expectations with no plan for which course owns which | Met: owns none; all 18 deepened codes checked against the Biology and Chemistry units tables and correct |
| No unit names its anchor or design problem | Met: nine specific anchors, none reused from another course; unit 8's question gives its answer (finding 4) |
| A core idea owned by two grades at the same depth | Met: each unit says what the core taught and what is new; holds on reading the core rows (Chemistry unit 11's farming and mining cost-benefit against units 2 and 5 is the closest, and the "regional measured records" and "decades past closure" lines hold) |
| A model assumed that no earlier grade builds | Met: the Models carried table matches the rows' model_in |
| A practice grows in no grade | Met: sampling design, rival-cause argument and a full design cycle are built past the core |
| A crosscutting concept listed everywhere and developed nowhere | Met: stability and change, scale and energy and matter each tied to a unit's work |
| Safety: hazards and controls named for the grade, a year safety sheet | Missed in part (finding 1); the course safety page is owed (lead item 7) |
| Plain facts: climate as the evidence shows, no "some say" | Met; values rule (b) is kept, with the two causal-claim fixes in finding 4 |

## Stale notes

None found. The Pending note on the base text is true (BASE-TEXTS.md has no Harris entry, and S:\CurioClass-sources
was not opened); data/courses.csv does list the course at grades 11 to 12, typical 12, as lead item 1 says.

## What is right and should not be touched

- The "deepens ~CODE (owned by <course>, unit <n>)" pattern, and each unit's "students now..." line naming the step past
  the core.
- The anchor rule (not used by any other course, local swap allowed) and the nine anchors themselves.
- The no-kit and simulation rule that names the student decisions kept and marks supplied-results-only paths as
  partial coverage for the sampling and testing outcomes. This is stricter than most frames and right.
- Unit 1's designed experiment set against the class's own correlation, and unit 7's rival causes: the course's
  nature of science spine.
- The values line: science says what can happen, values and law what should; no political view asked; outreach
  optional and through the teacher.
- The mathematics and Algebra II if-later lines (checked against the Algebra II weeks).

## What I could not judge

- The base text itself (not yet loaded) and the licence notes of Harris chapters 12 to 14 and section 11.4.
- Whether a strip or tablet kit a school can buy meets the strips-only rule for oxygen (finding 1); the kit safety
  data sheets settle it.
- The Navajo Nation, Richmond, Japan and Niger sources themselves: the sensitivity agent reads them.
- Classroom costs (the scope and sequence states them).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Unit 8's compelling question becomes: "Why is one street hotter than another in the same city at the same hour, and does a line drawn on a 1930s lending map still show in today's temperatures?" | Asks the question the evidence answers without giving the answer | docs/courses/environmental-science/frame.md, unit 8 |
| Unit 2's anchor reads: "...over the decades in which its slopes were terraced, dammed and replanted and dams were built on the river itself, the sediment the Yellow River carries fell by about nine tenths..." | Matches Wang et al. 2016's attribution and sets up the rival causes the outcome asks for | frame.md, unit 2 |
| The diversity index in unit 1 is Simpson's (one minus the sum of squared proportions), not Shannon's | No logarithm needed in weeks 1 to 4 for a grade 11 taker (Algebra II logarithms come in weeks 15 to 19) | frame.md unit 1; env-field-sampling note |
| The stream biotic index is a three-group pollution tolerance index (sensitive, somewhat tolerant, tolerant, weighted 3, 2, 1) as volunteer stream monitors use | Countable by a class with a key, no species identification | frame.md unit 3; env-water-quality note |
| Unit 3's transfer case is an unseen nutrient case (the hypoxic zone off the Mississippi mouth, from federal monitoring records), not the Aral Sea | Tests CUR-ENV.6 and 7 on a case the class has not seen | frame.md unit 3 and Source map chapter 7 |
| The heat walk runs on a clear, sunny day, surface readings first, with the 2017 summer data as the comparison set | Spring-term walk still gives a clear signal | frame.md unit 8 |

## For Cory

1. **Scope:** widen CUR-ENV.7, 10 and 11 to take in water supply, solid waste, and dose-response and
   biomagnification (finding 2). Recommended: yes; no new unit, days moved inside the year.
2. **People:** unit 5 rests on a sovereign nation's health and land. Recommended: only material the Navajo Nation has
   already released, no contact with the Nation, the sensitivity agent's read first (finding 10). Confirm.

## Sources

- Dorcas et al. 2012, PNAS 109(7): 2418 to 2422, via the federal geological survey's record
  (https://www.usgs.gov/publications/severe-mammal-declines-coincide-proliferation-invasive-burmese-pythons-everglades)
  and the Virginia Tech release (https://news.vt.edu/articles/2012/01/013112-cnre-pythonsineverglades.html): unit 7 figures and the north-of-park control.
- Richmond heat mapping: the federal climate toolkit case study
  (https://toolkit.climate.gov/case-studies/where-do-we-need-shade-mapping-urban-heat-islands-richmond-virginia),
  the Science Museum of Virginia's account
  (https://smv.org/learn/blog/new-museum-led-study-links-extreme-heat-and-historical-housing-policy/) and
  https://vpm.org/news/articles/23790/citizen-scientists-map-extreme-heat-in-richmond-virginia-cities: date, method, 16 degrees Fahrenheit.
- Wang et al. 2016, Nature Geoscience 9: 38 to 41 (https://www.nature.com/ngeo/journal/v9/n1/abs/ngeo2602.html),
  abstract only, and the 2017 Hydrology and Earth System Sciences paper summarising it
  (https://hess.copernicus.org/articles/21/4363/2017/hess-21-4363-2017.pdf): unit 2's figure and attribution.
- Base-text scout notes, 2026-11-16 (side-session notes): Harris and Fisher tables of contents and licences.
- From memory, to be pinned by the scope writer: the federal toxic-substances registry's uranium profile (finding 3);
  the AP Environmental Science course description as a scope reference (finding 2); Toledo, Britain, Philadelphia,
  Japan and Niger figures (finding 11).

## For the source list

- Dorcas et al. 2012 via the USGS publication page (above): public record, free to read.
- The Richmond heat case study on the federal climate toolkit (above): public domain, free.
- Wang et al. 2016: abstract free at the journal; full text paywalled, so nothing rests on more than the abstract and
  the open HESS 2017 paper.

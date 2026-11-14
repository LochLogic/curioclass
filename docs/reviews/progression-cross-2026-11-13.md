# Expert read across the four core progressions (2026-11-13)

The cross-subject column: what no single-subject read could see. Brief: docs/pipeline/briefs/progression-cross-read.md.
Run as the curriculum expert (docs/agents/EXPERT.md) with all four lenses (docs/agents/lenses/).

## What I read

| File | Rows | Used for |
|---|---|---|
| data/progressions/social-studies.csv | 384 | every row; 152 cross_subject entries out |
| data/progressions/science.csv | 198 | every row; 177 entries out |
| data/progressions/ela.csv | 374 | every row; 106 entries out |
| data/progressions/math.csv | 305 | every row; 52 entries out |
| docs/agents/EXPERT.md and the four lenses | | the role and what each subject counts as good |
| docs/reviews/progression-{subject}-2026-11-13.md, the four fix reports, the Codex reads | | what is settled; REPEAT tags |
| scripts/progression.py (cross-subject check, lines 239 to 272) | | what the gate proves and what it does not |
| data/courses.csv; docs/PRODUCTION-PATH.md step 1 | | course grades; what step 2 inherits |

`python -X utf8 scripts/plan.py check`: 0 failures in all four progressions (SS 384, math 305, ELA 374, science 198
rows; 1,261 in all). I resolved all 487 cross_subject entries with a script (kept in the scratchpad, not the repo):
each entry's target code or skill id, the grade of its owning row and of any earlier contributing `~` row, and the
gap in grades. Then I read the rows on both ends wherever the gap was positive, wherever the base texts' order inside
a year matters, and wherever two subjects share a term, a topic or a hard subject.

Order inside a year rests on the unit numbers already written in the rows: Illustrative Mathematics units in
math.csv notes (for example m6-statistical-questions "IM 6.8", m8-function-qualitative "IM 8.5") and OpenSciEd units
in science.csv notes ("Base unit 6.2"). EL Education module topics come from ela.csv notes. I fetched no outside
source on this run; where a point rests on memory it says so.

## Verdict

The four progressions fit together well: about 95 percent of the 487 leans name a skill the other subject has taught
by that grade, the ELA topic sets in K to 5 and the grades 6 to 12 knowledge threads sit beside the matching science
and social studies units, and the hard subjects are taught with one stance almost everywhere. The biggest risk is
timing the gate cannot see: seven leans point a year or more forward, and in grades 6 and 8 about a dozen same-grade
leans rest on math the base texts teach months after the science or social studies unit that needs it. The change
that matters most: add a grade check to the cross-subject gate and repoint those leans to the earlier math they
really use.

**Finding count: 10** (3 moderate, 7 minor). One item for Cory (an ELA grade 5 topic set).

## Findings, most serious first

### 1. Seven leans point a year or more forward, and the gate does not check grade (moderate; firm)

**LAYER** progression, with a process gap. **REPEAT** yes (social studies finding 7, ELA finding 4 and math finding 6
were leans on the wrong skill; ELA 4 was exactly a forward lean).

The gate (scripts/progression.py, lines 239 to 272) checks that some row in the other subject names the code. It does
not compare grades. The math fix report says "the lean gate rule: already in the gate"; it is not, which is why these
pass. A band code with an earlier `~` contributor (W.9-10.1, RI.11-12.9 and the like) is fine and is not listed.

| Row (grade) | Lean now | Owner (grade) | Why it matters | New cross_subject value |
|---|---|---|---|---|
| chem-human-earth-systems (10) | math:F-LE.A.4 | alg2-logarithms (11) | pH as a logarithm a year before logs | `math:8.EE.A.1 (pH steps are powers of ten: one unit is ten times the acidity)` |
| ss6-changing-interpretations (6) | science:MS-LS4-1 | s8-fossil-record (8) | fossil evidence two years early | `science:s3-fossils (fossils as evidence of life long ago); science:s6-geologic-time (rock layers and dating on the deep-time scale)` |
| ss6-mena-settlement (6) | science:MS-ESS3-1 | s7-resource-distribution (7) | uneven resources a year early | `science:4-ESS3-1 (energy and fuels come from natural resources)` (math part: see finding 2) |
| ss6-africa-geography (6) | science:MS-ESS3-3 | s7-human-impact-design (7) | human impact a year early | `science:5-ESS3-1 (communities protect resources and the environment)` |
| wh1-geography-shapes-contact (9) | science:HS-ESS3-1 | chem-resources-hazards-climate-human (10) | | `science:MS-ESS2-6 (unequal heating and the oceans shape climate, the monsoon winds); science:MS-ESS3-1 (resources are unevenly spread)` |
| wh1-farming-and-cotton (9) | science:HS-ESS3-1 | (10) | | `science:MS-ESS3-3 (human activity changes the land)` |
| wh1-scientific-revolution (9) | science:HS-ESS1-4 | phys-orbits (11) | orbital models two years early | `science:MS-ESS1-1 (the earth-sun-moon model); science:MS-ESS1-2 (gravity holds the solar system together)` |

Also in chem-human-earth-systems `notes`, the last sentence ("Math readiness: the high school math named here
(F-LE.A.4) is not yet placed ... until the math progression says when it is taught.") is stale now that math.csv
exists. Replace it with: "Math readiness: logarithms are taught in Algebra II (alg2-logarithms, grade 11); here pH is
read as a powers-of-ten scale (8.EE.A.1) from a given table, with no logarithm notation."

The reverse links already exist where they belong (chem-resources-hazards-climate-human leans back on
wh1-geography-shapes-contact). Add the one that is missing: phys-orbits `cross_subject` add
`social-studies:wh1-scientific-revolution (Kepler's and Galileo's evidence met in grade 9 history)`.

**Process fix (for the lead):** in the cross-subject loop, find the earliest grade of any row that owns or `~`
contributes the code (or the grade of the named skill id) and fail when it is later than the leaning row's grade.
A deliberate forward pointer is rare; if one is wanted, it belongs in `notes`, not in `cross_subject`.

### 2. Same-grade leans where the base texts teach the math months later (moderate; likely)

**LAYER** progression (codes) and course frame (order). **REPEAT** new.

A same-grade lean passes any check, but inside the year the math may come after the unit that needs it. Under the
base-text orders the lenses name (IM for math, OpenSciEd 6 to 8 for science), these are the clear cases:

| Row | Unit | Lean | Math taught in | Fix (cross_subject, new value) |
|---|---|---|---|---|
| s6-particle-temperature | OpenSciEd 6.2 | 6.EE.C.9 | IM 6.6 (lessons 16 to 18) | `math:5.G.A.2 (temperature against time plotted as points in the first quadrant)` |
| s6-air-masses-weather | 6.3 | 6.EE.C.9 | IM 6.6 | `math:5.G.A.2 (pressure and temperature plotted against time)` |
| s6-insulator-design | 6.2 | 6.SP.B.5 | IM 6.8 | `math:5.MD.B.2 (a line plot of repeated trials; the middle value read from it)` |
| s6-state-change | 6.3 | 6.NS.C.5 | IM 6.7 | `math:2.MD.B.6 (a thermometer is a number line; below zero read as degrees below zero)` |
| ss6-timeline-deep-time | year spine, first weeks | 6.NS.C.5; 6.NS.C.7 | IM 6.7 | `math:2.MD.B.6 (equally spaced points on a number line)` (keep the science lean) |
| ss6-mena-maps | first map unit | 6.NS.C.8 | IM 6.7 | `math:5.G.A.1 (a coordinate grid)` |
| ss6-mena-settlement | early in the year | 6.EE.C.9 | IM 6.6 | `math:3.MD.B.3 (monthly rainfall as a scaled bar graph); math:5.G.A.2 (monthly temperature as plotted points)` |
| s8-kinetic-energy-graphs | 8.1, first unit | 8.F.B.5 | IM 8.5 | `math:6.EE.C.9 (two quantities that change together, read from a graph); math:7.RP.A.2 (...)` (keep the second as is) |
| s8-wave-amplitude-energy | 8.2 | 8.F.B.5 | IM 8.5 | `math:6.EE.C.9 (amplitude and energy read from a graph)` |
| s8-solar-system-scale | 8.4 | 8.EE.A.3 | IM 8.7 | `math:5.NBT.A.2 (powers of ten for very large distances); math:7.G.A.1 (scale drawings)` |

Notes edits that go with them:
- ss6-timeline-deep-time: "(counting back from a zero point, like negative numbers)" becomes "(counting back from a
  zero point; math names these negative numbers later in grade 6)". The no-year-zero rule stays as written.
- ss6-mena-maps: "like a coordinate grid with signs" becomes "like a coordinate grid, read with north, south, east and
  west in place of signs".
- s6-state-change: add "Below-zero temperatures are read on the thermometer as degrees below zero; the minus sign is
  formal after the math unit on negative numbers (m6-negative-numbers), which reuses this thermometer."

Why it matters: a grade 6 teacher in October would be told the class can read a graph of two related quantities or
summarize trials with a mean, and IM teaches those in the spring. The fix asks only for what the unit really uses.
The rows that stay same-grade and close in time go to the course frames (see the last section).

### 3. Grade 7 social studies asks for a counterclaim a year before ELA teaches it (moderate; firm)

**LAYER** progression. **REPEAT** new.

ss7-rome-fall leans on ela:W.7.1, but its notes say "Counterclaim is taught here as a word and a move: students state
the strongest point for the other side of the debate and answer it with evidence", and its `words` list
"counterclaim". ELA grade 7 (e7-argument-writing) teaches "acknowledge alternate or opposing claims" and its notes
say "distinguishing one's claim from it and handling counterclaims is grade 8"; ELA lists "counterclaim" in grade 8.
A grade 7 student would meet a move and a word in history that English has not taught, with the lean claiming it has.

Fix, social-studies.csv, row ss7-rome-fall:
- `words`: replace "counterclaim" with "opposing claim".
- `notes`: replace the last sentence with "Students name the strongest opposing claim (the other side of the debate)
  and say why their evidence still favors their own, the grade 7 ELA move (e7-argument-writing, W.7.1a); answering a
  counterclaim in full comes in grade 8 (ss8-haudenosaunee-influence, e8-argument-writing)."

### 4. The claim and evidence model has two names, and social studies drops reasoning (minor; firm)

**LAYER** progression. **REPEAT** new.

Science and ELA carry `claim-evidence-reasoning` K to 12. Social studies carries `claim-evidence` in 50 rows K to 12.
The social studies lens itself says "reasoning says why the evidence supports it", and wh1-historical-argument lists
"reasoning" as a word. One move with two names tells three teachers in one school that it is two things, and the
shorter name invites claim-plus-quote with no reasoning.

Fix: social-studies.csv, every `model_in` and `model_out` value `claim-evidence` becomes `claim-evidence-reasoning`
(a plain replace of the whole token; `cause-effect-chain` and the rest are untouched). In ssk-i-think-because `notes`,
add "At K the reasoning is the spoken because."

### 5. Hard topics: three rows lack the stance their partners carry (minor; firm)

**LAYER** progression. **REPEAT** new.

- **Evolution.** ss6-changing-interpretations (grade 6, human origins) and bio-evidence-common-ancestry (grade 9) each
  carry a teacher note: evidence taught plainly, families' faith accounts respected, no student asked to state a
  belief. The rows where science first teaches evolution, s8-natural-selection and s8-anatomical-relationships, carry
  none. Add to both `notes`: "Teacher note: as in ss6-changing-interpretations and bio-evidence-common-ancestry,
  evolution is taught as the evidence shows (BASELINE rule 5); some families hold faith accounts of origins, and no
  student is asked to state a belief."
- **Climate.** s7-climate-change-evidence states the cause plainly (human activity, chiefly fossil fuels).
  wh2-global-problems (grade 10) names climate change with no stance line. Add: "Climate change is taught as the
  science shows (s7-climate-change-evidence, chem-climate-forecast): it is happening and human activity is the main
  cause; the open questions students weigh are what to do and who bears the costs." And `cross_subject` add
  `science:MS-ESS3-5 (rise in global temperature and its causes)`.
- **Natural against present warming.** ss6-timeline-deep-time places "the warming that made farming possible" at the end
  of the last Ice Age, the same year science has no climate-cause unit. Add: "That warming was natural and took
  thousands of years; today's faster warming and its human cause are taught in grade 7 science
  (s7-climate-change-evidence)."

Slavery (social studies from grade 3; ELA only in grade 11 with Douglass, read beside us1-slavery-resistance) and
genocide (social studies grades 10 and 12 only) are placed at matching ages with one stance. Puberty does not appear
in any core row; s8-reproduction-behaviors keeps reproduction to plants and animal behavior.

### 6. High school leans resolve to the wrong math row (minor; firm)

**LAYER** progression. **REPEAT** yes (social studies 7 and math 6: a lean naming the wrong skill).

Math high school ownership follows IM's tags, so N-Q, A-SSE.A.1, F-BF.A.1, F-IF.B.4 and A-REI.D.11 are owned by a
Geometry or Algebra II row while the skill starts in Algebra I. A writer who follows the code lands on the wrong row
(econ rows land on alg2-trig-functions-graphs for reading a supply and demand graph). Point at the skill id, as math
already does for its ELA leans.

| Row | Lean now | New value |
|---|---|---|
| bio-population-carrying-capacity | math:N-Q.A.2 | `math:alg1-writing-equations-constraints (define the quantities a population model tracks)` |
| bio-define-human-impact-problem | math:N-Q.A.1 | `math:6.RP.A.3d (convert units such as hectares or cost per year)` |
| bio-evaluate-impact-solutions | math:N-Q.A.3 | `math:alg1-scatter-linear-models (judge the precision of impact data)` |
| bio-photosynthesis-energy | math:A-SSE.A.1 | `math:6.RP.A.1 (ratios of molecules in a balanced equation)` |
| bio-biodiversity-simulation | math:F-BF.A.1 | `math:alg1-exponential-functions (a rule that steps a quantity forward)` |
| chem-energy-accounting | math:A-SSE.A.1 | drop it (the row's A-CED.A.4 lean, alg1-rearrange-formulas, carries the work) |
| chem-carbon-cycle-quantitative | math:F-BF.A.1 | `math:8.F.B.4 (a stock that changes each year by inflow minus outflow)` |
| phys-newton-second-law | math:A-CED.A.2 | `math:alg1-writing-equations-constraints (an equation relating force, mass and acceleration)` |
| phys-gravity-coulomb; phys-energy-motion-position | math:A-SSE.A.1 | `math:alg1-quadratic-patterns (read each term of an expression, squared terms included)` |
| us2-econ-toolkit; econ-scarcity-choice | math:F-IF.B.4 | `math:alg1-graph-features-rates (read key features of a graph)` |
| econ-markets-prices; econ-price-controls | math:A-REI.D.11 | `math:alg1-graph-features-rates (where two graphs cross)` |

Keep each row's reason text where it is already right; only the target changes unless the table gives a new reason.

### 7. Natural hazards are taught at the same depth in too many places in grades 4 to 6 (minor; judgment call)

**LAYER** progression (topic sets). **REPEAT** new.

Hazards appear in science 4 (s4-hazard-solutions), social studies 4 (ss4-disasters-response), ELA 4
(e4-text-structure), ELA 5 unit 4 "preparing for a disaster" (e5-research), ELA 6 thread 2 and science 6
(s6-hazard-forecast). Grade 4 is three subjects on one topic at once, which is good. Grade 6 adds forecasting, which is
new depth. ELA grade 5 stands alone and repeats grade 4's depth (ways to reduce harm), with no grade 5 science or
social studies unit beside it. The ELA lens names this as a fault: a topic repeated at the same depth.

Fix (the pick goes to Cory, below): e5-research `notes`, "unit 4 (preparing for a disaster)" becomes "unit 4 (water:
how much is usable and how communities share it, beside s5-water-distribution and s5-protect-resources)", and
e5-research `cross_subject` add `science:5-ESS2-2 (how much of Earth's water is fresh and where it is)`. Then
e6-reading-range `notes`, "inherited from grade 5's rainforest and disaster-preparedness units" becomes "inherited
from grade 5's rainforest and water units". Grade 6 thread 2 still opens on hazards, now beside science, not after a
second pass in English.

### 8. ELA and social studies run paired research projects in grades 10, 11 and 12 (minor; likely)

**LAYER** progression (notes), course frame. **REPEAT** new.

e10-w-research with wh2-research-argument, e11-research (a four-week reform-movement paper, about 1,500 words) with
us1-research-inquiry, and e12-research (about eight weeks, about 2,500 words) with us2-research-paper. Each ELA row
leans on its partner ("the same research cycle in US History I") but neither says whether it is one project or two.
Read literally, a student writes two sustained papers a year in grades 11 and 12. That is double teaching of the
same standard (W.11-12.7) and the heaviest load in the high school years.

Fix: add the same sentence to the `notes` of all six rows: "Where a school teaches both courses, one project may
serve both: the course frames write one shared brief, and each course still teaches the whole cycle for schools that
use it alone." Each course stays complete on its own (Curio Class tools are standalone), and a school using both is
spared the second paper.

### 9. Missing leans worth wiring (minor; firm)

**LAYER** progression. **REPEAT** yes (social studies 7: rows that lean on nothing).

| Row | Add to cross_subject | Why |
|---|---|---|
| s3-fossils | `ela:e2-research (fossil notes from the grade 2 fossil topic set)` | ELA grade 2 module 2 reads fossils and a fossil hunter a year before science; the unit can open on it |
| ss7-silk-road-trade | `math:6.EE.C.9 (two quantities that change together on a graph)` | it introduces the supply and demand graph with no math lean |
| ss8-election-info | `math:7.SP.A.1 (why a poll's sample decides what it can tell us)` | polling data is a sampling question; grade 7 math teaches it |
| e4-visual-info | `social-studies:ss3-timeline (reading a timeline)` | the row lists "timeline" as a word; social studies built it a year earlier |
| s6-particle-temperature | `ela:e6-argument-writing (an argument from evidence, MS-PS3-5)` | grade 6 science has one ELA lean in 14 rows |
| s6-geologic-time | `ela:e6-informative-writing (an explanation built from evidence)` | as above |
| phys-orbits | `social-studies:wh1-scientific-revolution` | given in finding 1 |

### 10. Small term and spelling mismatches across subjects (minor; firm)

**LAYER** progression. **REPEAT** yes (math 5: US spelling in words; science 11 and social studies 11: word placement).

- s6-air-masses-weather `words`: "probability" becomes "chance". Probability is taught in grade 7
  (m7-chance-probability); the row already speaks of "a range of chances".
- ss3-money-saving `words`: drop "interest rate" (a rate needs percent, grade 6); keep "interest".
- e2-opinion `words`: add "claim"; `notes` add "The opinion is the claim; science and social studies call it a claim."
  Social studies uses "claim" from grade 2 (ss2-claim-sources), and ELA otherwise first lists it in grade 4.
- s5-water-distribution keeps "percent" (see Settled); `notes` add "(percent means per hundred; it is taught in grade 6
  math, m6-percent)".
- US spelling in the student and cross-subject columns: science `words` "behaviour" in bio-group-behavior becomes
  "behavior"; ELA `words` "organise" in e7-text-organization becomes "organize"; `cross_subject` reasons: "centre"
  (bio-biodiversity-math, bio-trait-proportion-shifts) becomes "center", "centimetres" (s2-erosion-solutions)
  "centimeters", "organise" (s1-daylight-seasons) "organize", "organised" (e6-argument-writing) "organized",
  "modelling" (ss3-home-region) "modeling". Notes keep their mixed spelling for now; it is not student-facing.

## What is right and should not be touched

- **Deep time in grade 6** is built twice on purpose and wired both ways: ss6-timeline-deep-time and s6-geologic-time,
  the age of the Earth stated plainly in both, the no-year-zero rule in social studies.
- **The grade 4 hazard week** across science, social studies and ELA, and the grade 6 forecast thread.
- **ELA K to 2 topic sets meet science in the same year:** weather and trees in K, sun, moon and stars and birds in 1,
  pollinators in 2; each is leaned on.
- **ELA 6 to 8 threads** (law codes, Greece and Rome, founding documents; Earth systems, human impact, science claims)
  sit beside the social studies and science rows of the same grade, and ELA 11 and 12 American literature follows the
  US History I and II order.
- **The ratio, percent and data chain from math into science 7 and social studies 7 to 12** is on time everywhere.
- **Physics needs no trigonometry or vectors:** its rows keep to one-dimensional motion (phys-newton-second-law,
  phys-momentum-conservation), the NGSS boundary (from memory, and as the rows state). No lean is missing.
- **Chemistry's scientific notation** leans on 8.EE.A.4 two years earlier; half-life on F-LE.A.1c a year earlier.
- **Douglass's Narrative** is read whole in ELA 11 in the same year as us1-slavery-resistance, with a content note.
- **Gov and Economics assume nothing from US History I or II**, so a school can place them in grade 11.

## What I could not judge

- Order inside a year beyond the unit numbers written in the rows. The course frames set the real order; finding 2
  assumes IM and OpenSciEd order, as the lenses do.
- Whether a lean's depth matches beyond its reason text, for the many same-grade K to 5 leans (for example a grade 3
  science line plot to the quarter inch before or after IM grade 3 unit 6 fractions). Listed for the frames.
- Literacy in science and history (RST and WHST): not in the standards inventory (Codex science finding 7, parked).

## Settled by the expert

| Choice | Reason in one line | File |
|---|---|---|
| `timeline` (social studies) and `number-line` (math) both kept | K to 2 timelines are sequence strips; from grade 3 a timeline is a number line of years and already leans on 2.MD.B.6 | none |
| `data-graph` (science) kept beside math's named displays | it is the science practice; each row names the math display it uses (bar graph, line plot, coordinate graph, histogram, scatter plot) | none |
| `point of view` and `perspective` both kept | point of view is whose eyes a text is told through or an author's stance (ELA, and social studies when reading a source's author); perspective is the views of people in the past (social studies) | none |
| `cause-effect` (science) and `cause-effect-chain` (social studies) both kept | a crosscutting concept and a model of historical causation with weighed causes are different tools | none |
| `claim-evidence-reasoning` is the one name | finding 4 | social-studies.csv |
| "opposing claim" in grade 7, "counterclaim" from grade 8, in every subject | follows the ELA standards' own words (W.7.1a, W.8.1) | social-studies.csv (finding 3) |
| K and 1 use the spoken "I think ... because ..." in all subjects; "claim" as a student word from grade 2 | the K science row may keep "claim" in teacher talk; finding 10 adds it to ELA grade 2 | ela.csv |
| "percent" kept in grade 5 science with a per-hundred gloss | the hundred-square grid makes it concrete; the formal unit is grade 6 | science.csv |
| "probability" moved to "chance" in grade 6 science; "interest rate" dropped in grade 3 social studies | each needs math taught later | science.csv, social-studies.csv |
| "scale" stays one word with several meanings | map scale, graph scale, a weighing scale and scale as size are each glossed where used; the frames add the gloss | none |
| One research project may serve ELA and social studies in grades 10 to 12 | finding 8; each course still stands alone | ela.csv, social-studies.csv |
| US spelling in `words` and `cross_subject` across all four files | matches math's 2026-11-13 fix | science.csv, ela.csv, social-studies.csv |
| Physics gets no trigonometry or vector lean | one-dimensional boundary | none |

## For Cory

1. **ELA grade 5, unit 4 topic (what a grade teaches, at the topic level).** It now repeats grade 4's natural hazards at
   the same depth, with no science or social studies unit beside it. Pick: water (how much is usable and how
   communities share it), read beside grade 5 science's water and resources rows (finding 7). The alternative is to
   keep disasters and add depth (recovery and who is helped first), which leaves grade 6 as the third pass.

## Rows per grade per subject

| Grade | Social studies | Science | ELA | Math | Total |
|---|---|---|---|---|---|
| K | 19 | 11 | 29 | 20 | 79 |
| 1 | 21 | 10 | 31 | 26 | 88 |
| 2 | 18 | 12 | 30 | 28 | 88 |
| 3 | 27 | 15 | 28 | 24 | 94 |
| 4 | 17 | 14 | 30 | 27 | 88 |
| 5 | 21 | 14 | 30 | 25 | 90 |
| 6 | 29 | 14 | 29 | 26 | 98 |
| 7 | 29 | 18 | 28 | 23 | 98 |
| 8 | 27 | 26 | 29 | 24 | 106 |
| 9 | 37 (WH I) | 24 (Biology) | 24 | 28 (Algebra I) | 113 |
| 10 | 43 (WH II) | 20 (Chemistry) | 26 | 28 (Geometry) | 117 |
| 11 | 27 (US I) | 20 (Physics) | 30 | 26 (Algebra II) | 103 |
| 12 | 69 (US II 25, Gov 19, Econ 25) | 0 | 30 | 0 | 99 |

Rows are expectation owners, not days. What the table says: grade 10 is the peak (117), carried by World History II's
43 rows; grade 8 is the middle school peak, carried by science's 26 (OpenSciEd completes many expectations there).
Where a hard new idea lands in two subjects the same year: grade 6 (negative numbers in math, years before zero in
social studies, below-zero temperatures in science: one idea three ways, an asset if the frames order it); grade 8
(functions in math, energy and wave graphs in science); grade 9 (evolution in Biology, the Atlantic slave trade in
World History I); grade 10 (moles and scientific notation in Chemistry, the Holocaust and other genocides in World
History II); grade 11 (algebra-heavy Physics with Algebra II; slavery in US History I with Douglass in ELA).

## For the course frames

What step 2 must handle; none of this is a progression fix.

- **Build paired frames side by side in grades 6 and 8.** Math 6 and science 6, math 8 and science 8: after finding 2,
  the leans still close in time are s6-hazard-forecast and e6-media-integrate (histograms, IM 6.8, near OpenSciEd 6.5),
  s6-light-paths (6.SP.A.2, already marked guided), s8-gravity-mass and s8-growth-factors (scatter plots, IM 8.6).
- **Same-grade leans in K to 5 and high school to order with care:** s3-motion-patterns and s3-environment-traits (line
  plots to the quarter inch, IM grade 3 unit 6); s5-shadows-sky (5.G.A.2, IM grade 5 unit 7, late);
  bio-population-carrying-capacity (exponential growth, IM Algebra I unit 5); physics rows on A-CED in Algebra II's
  year.
- **Math grade 6's negative numbers unit (IM 6.7)** can open on the class's timeline and thermometer from social
  studies and science, as m6-negative-numbers already leans.
- **One shared research brief** for ELA and social studies in grades 10, 11 and 12 (finding 8).
- **Founding documents are read seven times** (ELA 8 thread, social studies 8, ELA 9, ELA 11, US I, ELA 12, Government).
  Give each reading one lens (rhetoric, argument, holdings) and avoid the same document in both courses in the same
  month without a reason.
- **Hard content in the same year:** grade 10 genocide units and ELA 10's world literature under colonial rule; grade
  11 slavery in US I and the Douglass Narrative in ELA 11. Coordinate content notes and do not schedule the hardest
  weeks together.
- **If an ELA 6 to 8 frame picks Holocaust literature,** it comes before social studies teaches it (grade 10); add
  context or choose another text.
- **ELA 6 to 8 thread texts** must follow the order of the social studies and science units they sit beside.
- **Check days, not rows,** in World History II (43 rows) and Economics (25 rows in a half year).
- **Gov and Economics** may be placed in grade 11; nothing in them assumes US History II.

## Sources

- data/progressions/*.csv: the rows read, and the base-text unit numbers inside them (IM for math, OpenSciEd for
  science 6 to 8, EL Education modules for ELA K to 5).
- scripts/progression.py: what the cross-subject gate checks.
- docs/agents/EXPERT.md and docs/agents/lenses/*.md: the role and each subject's errors.
- docs/reviews/progression-*-2026-11-13.md and the fix reports: settled findings and the REPEAT tags.
- From memory, not re-fetched: NGSS HS-PS2-1 and HS-PS2-2 one-dimensional boundaries (the rows say the same); IM and
  OpenSciEd unit order beyond what the rows state.

## For the source list

Nothing new; no outside source was read on this run.

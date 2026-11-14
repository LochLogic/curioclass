# Frame read: biology (Biology, grade 9), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md, docs/pipeline/briefs/frame-write.md
  (the "Lessons from the social studies frames" list).
- The frame docs/courses/biology/frame.md and its row in data/plans/frames.csv (10 units, 160 days).
- The 24 bio- rows of data/progressions/science.csv, every row they assume (grades 6 to 8) and the chem- and phys- rows
  they hand on to; the frame before (docs/courses/science-grade-8/frame.md) and after (docs/courses/chemistry/frame.md).
- Same-year neighbours as written today: docs/courses/algebra-i/frame.md (unit weeks computed from its day counts),
  docs/courses/english-language-arts-grade-9/frame.md, docs/courses/world-history-i/frame.md; data/progressions/math.csv
  (alg1-, geo-, m6- to m8- rows).
- data/standards/ngss-pes.txt (codes only: 71 high school codes; a script confirmed each is owned by exactly one row,
  Biology 30, Chemistry 21, Physics 20, and all 19 HS-ESS codes once). DESK-ANSWERS 2026-11-13 (q-hs-science-core).
  The "For the course frames" parts of docs/reviews/progression-science-2026-11-13.md,
  progression-science-codex-2026-11-13.md and progression-science-fixes-2026-11-13.md.
- Gates: `python -X utf8 scripts/plan.py check` (frame biology: 0 failures; 10 units, 160 days, 149 in units, 11 for
  checks), `python -X utf8 scripts/frame.py check biology` (0 failures), `python -X utf8 scripts/stale.py check`
  (45 files, 0 failures).
- **Standards in full** is judged from my own knowledge of the NGSS performance expectations, their clarification
  statements and assessment boundaries (the repository holds codes only), checked against each row's notes. No NGSS
  page was fetched for this read; every standards finding below rests on memory plus the row text, and says so.

## Verdict

The frame is sound and close to ready: every bio- row sits in one unit, all 30 expectations are placed, the order
(body, cell, energy, ecosystems, inheritance, evolution, Earth and life, design) builds each model before it is
used, and every seam with grade 8 and Chemistry lines up. The biggest risk is load in two places: unit 9 holds four
expectations and the year's first full design cycle in 15 days, and unit 7 four expectations in 17, while units 1, 2
and 4 run 6 to 7 days an expectation. The one change that matters most is moving four days from units 1, 2 and 4 to
units 9 and 7; the rest are short text fixes.

## Findings, most serious first

### 1. Units 9 and 7 are short for what they own; units 1, 2 and 4 are long (moderate; likely)

LAYER frame. REPEAT yes (lesson 9, days by load).

**What is wrong.** The frame's own rule (Days bullet) is about 5 days an expectation, with design-cycle units
carrying more. The counts run the other way: unit 9 has 15 days for 4 expectations (3.8 a performance) and must
define a global challenge with numbers (HS-ETS1-1), design, evaluate and refine a solution (HS-LS2-7), evaluate a
solution with impact data (HS-ESS3-4) and weigh trade-offs (HS-ETS1-3); unit 7 has 17 days for 4 (4.3), including a
written and graphic communication task (HS-LS4-1). Against them unit 1 has 14 days for 2 (7.0), unit 2 13 for 2
(6.5), unit 4 12 for 2 (6.0, a data-only unit with no investigation). Inside unit 5, bio-group-behavior at "about two
days" is thin for HS-LS2-8, which asks students to evaluate study designs, not just read a claim.

**Why it matters.** A unit writer builds days from these counts. A design cycle squeezed to fit becomes "design on
paper, no refine", which is the HS-LS2-7 performance lost; it is the first full high school design cycle and the
one Chemistry and Physics assume.

**Fix.** Unit 1 14 to 13, unit 2 13 to 12, unit 4 12 to 11, unit 9 15 to 17, unit 7 17 to 18 (total 149 kept). In
unit 5's row change "one short (bio-group-behavior, about two days inside the island case)" to "one short
(bio-group-behavior, about three days inside the island case)". Recompute the week labels (unit 1 weeks 1 to 3, unit
2 weeks 3 to 5, unit 3 weeks 6 to 9, first check weeks 9 to 10, unit 4 weeks 10 to 12, unit 5 weeks 12 to 15, second
check week 16, unit 6 weeks 16 to 19, unit 7 weeks 19 to 23, unit 8 weeks 23 to 25, unit 9 weeks 25 to 28, unit 10
weeks 29 to 31). I checked the moved weeks against the Algebra I frame: no lean changes (writing equations is taught
by week 10, centre and spread by week 4, linear models by week 12, exponential functions by week 22).

### 2. Two expectations are narrowed to their headline (moderate; firm, from memory and the rows)

LAYER frame. REPEAT yes (lesson 4, standards in full).

**What is wrong.**
- HS-LS2-6 (unit 5). The clarification and the row contrast a modest change that the ecosystem absorbs (a seasonal
  flood, moderate hunting) with an extreme one that makes a new ecosystem (sea level rise, a volcanic eruption). The
  frame keeps only "a large change can make a new ecosystem"; the modest-change half and all four examples are gone.
- HS-LS1-6 (unit 3). The performance is "construct and revise an explanation based on evidence", and the row adds
  "from models and simulations". The frame's text is "How the atoms of sugar combine with nitrogen and sulfur into
  amino acids..." with no evidence named and no revision point; the C3 cell's "revising" is attached to HS-LS2-3.

**Why it matters.** The unit writer works from "What students learn". These are the parts an adoption reviewer
checks (Gateway 2, claimed core ideas and practices by element).

**Fix.** Unit 5, replace the HS-LS2-6 sentence with: "Evaluating claims, evidence and reasoning that an ecosystem
keeps similar numbers and kinds of organisms while conditions are stable, that a modest change (a seasonal flood,
moderate hunting) is absorbed, and that an extreme change (sea level rise, a volcanic eruption) can produce a new
ecosystem; students judge whether an argument's evidence covers the scale of change it claims (HS-LS2-6)." Unit 3,
replace the HS-LS1-6 sentence with: "An explanation, built from models and a simulation and revised when the class
meets new evidence (the dry mass of the light seedlings outweighs the sugar they could store), of how the carbon,
hydrogen and oxygen of sugar combine with nitrogen and sulfur into amino acids and other large carbon-based
molecules (HS-LS1-6)."

### 3. The cross-subject section is written as if the Algebra I and ELA 9 frames did not exist, and one pick is wrong (minor; firm)

LAYER process. REPEAT yes (lesson 15, stale notes).

**What is wrong.** "Algebra I and ELA 9 run the same year; their frames are written later" is no longer true: both
frames are on disk. The e9-w-informative row in "Leans from the other subjects" picks "ELA 9 teaches explanatory
writing before week 20", but ELA 9 teaches it in its unit 7, weeks 24 to 26 (Island birds), with argument writing in
unit 6, weeks 20 to 24. Unit 10's "Algebra I's exponential functions (alg1-exponential-functions) are likely taught"
can now be stated: Algebra I unit 5, weeks 17 to 22.

**Why it matters.** The availability calendar is what the same-year frames read; a wrong week sends the ELA 9
fixer looking for a change that is not needed.

**Fix.** Cross-subject intro: "Algebra I and ELA 9 run the same year; their frames (docs/courses/algebra-i/frame.md,
docs/courses/english-language-arts-grade-9/frame.md) give the weeks below, and each lean keeps its if-later line."
In the e9-w-informative row replace the Pick with: "ELA 9 teaches explanatory writing in its unit 7 (weeks 24 to 26),
before Biology unit 9 (weeks 25 to 28); its own if-later line has the piece explain only what its sources say, so
neither frame changes." In unit 10's "Why" cell, "are likely taught" becomes "are taught (Algebra I unit 5, weeks 17
to 22)". Under Hard content add: "ELA 9 unit 7 (Darwin and island birds, weeks 24 to 26) follows Biology unit 7
directly; the two share the evolution content note." For the lead item 4 can then be dropped.

### 4. Unit 5 steps a population forward by a growth factor before Algebra I's exponential unit, and the worked step table sits in unit 10 (minor; likely)

LAYER frame. REPEAT yes (lessons 5 and 13).

**What is wrong.** Unit 5 (weeks 12 to 15) introduces computational-model with births and deaths that scale with
population, which is repeated multiplication by a factor; Algebra I teaches exponential growth in weeks 17 to 22. The
"if later" line that teaches "new amount equals old amount times a factor, plus or minus a harvest" with a worked
table sits in unit 10's lean, not in unit 5, where the step rule is first used.

**Why it matters.** Each thread starts where it is first used. The math is within reach (grade 7 percent, grade 6
expressions), but only if unit 5 teaches the step rule itself.

**Fix.** Add to the bio-population-carrying-capacity lean (Algebra I table): "Unit 5 teaches the step rule (new
amount equals old amount plus births minus deaths, each a percent of the old amount) with a worked table from grade
7 percent; no exponential notation." Change unit 10's line to "As unit 5: retrieval of the step rule."

### 5. Unit 8's anchor states a rock pattern too broadly (minor; likely, from memory)

LAYER frame. REPEAT new.

**What is wrong.** "Younger rocks are banded red with iron that did [rust]" reads as banded iron formations being
younger than 2.4 billion years. Many banded iron formations are older (some about 3.8 billion years) and formed in
seawater; the clean post-oxygen signal on land is red beds, sandstones stained by iron oxide, which appear after
about 2.3 billion years ago.

**Why it matters.** Accuracy is a door (rubric S10, Gateway 2d). An anchor students cannot trust undercuts the
argument the unit asks them to build.

**Fix.** Settled below: "rocks older than about 2.4 billion years hold grains of minerals that rust in today's air
and did not rust then; younger sandstones laid down on land are stained red by rust."

### 6. Safety lines miss three hazards the rows or common practice name (minor; firm)

LAYER frame. REPEAT new.

**What is wrong.** (a) Bean seeds in units 3 and 6: garden seed is often coated with fungicide; the frame does not
say food-grade dry beans. (b) Unit 1's roots in damp paper towels in a bag grow mould within days; no "keep sealed,
dispose sealed" line. (c) The row bio-homeostasis-feedback says students with a medical reason take the recording
role; the frame keeps "voluntary and light" but drops the medical-reason line.

**Why it matters.** S5 is a door; the course safety page is built from this column.

**Fix.** Unit 3 and unit 6 hazards: add "dry beans from the grocery store, never treated garden seed; wash hands
after handling." Unit 1: add "seed bags stay sealed and are thrown away sealed (mould); students with a medical
reason take the recording role or use the class data set."

### 7. Unit 6's anchor needs a gene that hides another, which the unit does not name (minor; judgment call)

LAYER frame. REPEAT yes (lesson 10, questions answerable from the unit).

**What is wrong.** Black, chocolate and yellow puppies from two black parents need two genes, one of which (the
yellow, ee) masks the other. "Expected ratios from a two-gene cross" does not say that one gene masks another, so a
writer may teach two independent genes and leave the anchor unanswered.

**Fix.** Unit 6, "What students learn", after the HS-LS3-3 example add: "the litter itself: one gene sets black or
chocolate, a second can hide both and make yellow, and a 16-box square gives 9 black, 3 chocolate, 4 yellow; no
other gene interactions are taught." Inside HS-LS3-3's boundary (no Hardy-Weinberg).

### 8. The Models carried table names the wrong last carrier for plate-model (minor; firm)

LAYER frame. REPEAT new.

**What is wrong.** The table says plate-model was "last carried by s6-plate-evidence (grade 6)"; the rows show
s7-resource-distribution (grade 7) carries it, and unit 8's own "Why" says "idle since grade 7".

**Fix.** Table cell: "Introduced in grade 6 (s6-plate-evidence); last carried by s7-resource-distribution (grade 7)."

### 9. A row note gives Chemistry's count as 20 (minor; firm)

LAYER progression. REPEAT yes (stale or wrong notes).

**What is wrong.** bio-population-carrying-capacity notes say Biology owns 30 "against 20 in Chemistry and 20 in
Physics"; Chemistry owns 21 (chem-energy-device-design carries two). The frame itself says 21.

**Fix.** For the lead, new item: "Row fix, bio-population-carrying-capacity notes: 'against 20 in Chemistry' should
read 'against 21 in Chemistry'."

## Checked and found right (do not undo)

- All 24 rows placed once; owned standards match the rows; 149 + 11 = 160; a respond day after every check.
- Each of the 30 expectations other than those in finding 2 is taught with its practice, core idea and the
  clarification examples its row names, inside its boundary (from memory): HS-LS1-1 to LS1-5 and LS1-7, LS2-1 to LS2-5
  and LS2-7, LS2-8, LS3-1 to LS3-3, LS4-1 to LS4-6, HS-ESS2-7 (oxygen, soil, reefs), HS-ESS3-3 (provided programs or
  simplified spreadsheets), HS-ESS3-4 (local to geoengineering), HS-ETS1-1 (framed as a global challenge, as the
  Codex progression read asked), HS-ETS1-3, HS-ETS1-4.
- The two row fixes under For the lead (6.RP.A.3d is owned by m6-unit-conversion; food-web is first used in unit 4)
  are correct; I checked both in the data.
- Every anchor is a phenomenon, not a topic, and none repeats a grade 6 to 8 base anchor I could identify.
- Nature of science is placed on purpose (units 5, 7, 8); evolution and the age of the Earth are taught as the
  evidence shows, with the right teacher notes.
- Sensitivity: units 6, 7 and 9 name the right readers; the Lower Elwha Klallam Tribe is described as a present-day
  nation in its own words, with no role play.

## Seams

From grade 8: every row the grade 8 frame hands on ("Handed on to high school") is picked up in the unit the rows
say; the grade 7 rows that skip grade 8 open with retrieval. To Chemistry: all six hands_on links (bond energy,
carbon cycle, computational model, feedback, design criteria and trade-offs, simulation) are picked up in the
Chemistry units this frame names (5, 10, 5, 9, 7 and 11, 10). To Physics: bio-sources-of-variation to Physics unit 7,
matched.

## Cross-subject

Algebra I (frame on disk): every same-year lean is met in time except S-ID.A.1 in week 1 (concurrent with Algebra I
unit 1, weeks 1 to 4), which has a sound if-later line. Earlier-year math leans are all owned by grades 6 to 8 rows
as written. ELA 9: see finding 3. World History I's unit 10 (weeks 28 to 31) is named in the writing-load line.

## The lens checklist (course frame layer)

| Line | Result |
|---|---|
| A performance expectation for the grade has no unit, or a unit claims one it only touches | Met for placement; two narrowed (finding 2) |
| Grades 6 to 8: departure from OpenSciEd order | Not applicable |
| High school: a course claims band expectations with no plan for which course owns which | Met: 71 codes, each owned once |
| No unit names its anchor phenomenon or design problem | Met |
| Safety: hazards and controls, a year safety sheet | Partly: column present, three gaps (finding 6); course safety page owed (For the lead 7) |
| Plain facts (BASELINE rule 5) | Met |

## The brief's lessons list

1 met; 2 met; 3 met (50 minutes, five a week, 32 weeks); 4 missed in two places (finding 2); 5 missed once (finding
4); 6 met ("first full design cycle" checked against grade 8: grade 8 completes MS-ETS1 only); 7 met (two row fixes
written); 8 met; 9 missed (finding 1); 10 one doubtful (finding 7); 11 met; 12 met; 13 met with finding 4; 14 met; 15
missed once (finding 3).

## What I could not judge

- The NGSS text itself: the repository has codes only and I fetched nothing, so the standards findings rest on
  memory plus the rows.
- Whether 5 days an expectation fits a real grade 9 class overall; I judge it workable because five rows combine
  performances on shared data, but the scope and sequence is the real test.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Unit 8 anchor: red sandstones on land after about 2.3 billion years, not "banded red" rocks | Accurate; banded iron formations are often older | docs/courses/biology/frame.md, unit 8 |
| Unit 6 anchor kept (Labrador litter), with one masking gene named and the 9:3:4 litter worked | The anchor stays answerable inside HS-LS3-3 | docs/courses/biology/frame.md, unit 6 |
| bio-group-behavior gets three days inside unit 5's 18 | Evaluating study designs needs more than two | docs/courses/biology/frame.md, unit 5 |
| Food-grade dry beans for units 3 and 6 | No fungicide-treated seed | docs/courses/biology/frame.md, units 3 and 6 |

## For Cory

- People (as the frame says): a qualified science teacher's safety and materials read, and the readers for units 6,
  7 and 9 (a reader from, or the published materials of, the Lower Elwha Klallam Tribe). Who, and any pay, is yours.
- Scope, only if the scope and sequence still finds Biology short after finding 1: moving one Earth and space
  expectation (HS-ESS3-4 is the lightest to move, to Chemistry unit 11) would be your call. Not needed now.

## Sources

- NGSS high school performance expectations, clarification statements and assessment boundaries (2013), and
  Appendix K (modified science domains): from memory, not re-fetched.
- The repository files listed under "What I read".

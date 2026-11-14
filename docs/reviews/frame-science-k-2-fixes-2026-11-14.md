# Fixes: science course frames, kindergarten to grade 2, after the two cold reads (2026-11-14)

Applies the expert reads (`frame-science-<course>-2026-11-14.md`) and the Codex reads
(`frame-science-<course>-codex-2026-11-14.md`) for kindergarten, grade 1 and grade 2 to the three frames and
`data/progressions/science.csv`. Every expert finding and every "Settled by the expert" row is applied; each Codex
finding was weighed on its merits. The writers' own "For the lead" items were applied where they were item-level.

Gates after the fixes: `scripts/frame.py sync` (52 courses); `scripts/frame.py check science-kindergarten
science-grade-1 science-grade-2` 0 failures each; `scripts/progression.py check science` 198 rows, 0 failures;
`scripts/stale.py check` 56 files, 0 failures; `scripts/plan.py check` exit 0. No unit, skill or standard moved;
every course keeps its unit count and total days (K 6 and 64, grade 1 8 and 68, grade 2 7 and 76). The grade 3 frame was not edited: no handoff target changed, so its Seams table still holds.

Found in passing and applied in all three frames: the storyline bullet now asks for a short individual end-of-unit
task on a case the class has not seen (Codex grade 2 F4, which the lens's "Transfer at the end" requires of every
unit, so it is applied to K and grade 1 too, in a talk-and-point form for kindergarten). The ELA K to 2 frames now
exist; each science frame's Cross-subject section now states where ELA teaches each lean and records ELA's leans
on science.

## Kindergarten

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | The weather chart starts in week 1 as a teacher-led two-minute routine with picture squares (brief "Days"); unit 2 is where it is taught and read, comparing September against October; unit 2's reason says the chart starts in week 1 so the unit has two months; sk-weather-watch notes say the same |
| Expert | 2 | Applied | Unit 4's model adds people: the class's own town and its water source on the picture map (K-ESS3-1 "including humans"); sk-needs-places notes changed to match |
| Expert | 3 | Applied | Unit 4 opens on fall photographs (taken in unit 2's outdoor looks) of the weed and the squirrel's hole, the walk only where the ground is clear; unit 5 asks "Why is the slide in the sun warmer than the one under the tree?" on any sunny day, "too hot to touch" and "Spring" dropped; "For the lead" item 3 now covers only warm-climate swaps |
| Expert | 4 | Applied | Cross-subject lead-in rewritten with math's units (K.MD.B.3 unit 2, week 8; K.MD.A.2 unit 3, weeks 12 and 13) and ELA's units (SL.K.3 and W.K.2 unit 1, SL.K.5 unit 2, W.K.1 unit 4); which uses come first and run on a bridge is stated as a note, not a new column |
| Expert | settled | Applied | All four rows (week 1 chart; the town and its water source; fall photographs; the sunny-day slide anchor) |
| Codex | 1 | Rejected | The read was withheld because of a math grade 6 gate failure (6.EE.C.9 missing from an Owned standards cell). That is another subject's frame, outside this pass; `plan.py check` now exits 0. The read has no content finding on this frame |
| Codex | settled | Nothing to apply | Its two rows withhold the verdict |
| Writer | lead 2 | Applied | sk-living-needs now "Extends the patterns model from the weather chart (sk-weather-watch) to patterns across many living things", and takes patterns as model_in; the item is rewritten as settled |
| Writer | lead 3 | Applied | Rewritten with expert 3 |
| Writer | lead 1, 4 | For Cory | Time a week (two lessons of about 30 minutes); materials ceiling of about $40 a class |
| Expert | For Cory | Collected | Materials ceiling; K to 2 science time against grade 3's 180 minutes; the disaster-aware reader and the science teacher's safety read |

Counts: applied 6 (expert 1 to 4, writer items 2 and 3), rejected 1 (Codex 1), for Cory 3.

## Grade 1

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Daylight observed light or dark at about 5:30 in the evening from two or three optional family reports, beside a monthly light-and-dark day strip from the town's public sunrise and sunset table, compared by length only; brief "Split unit", unit 1's last day, unit 8 question, anchor, content and teacher note (reports optional and never graded, a school whose going-home time does cross sunset may observe then); s1-daylight-seasons notes changed as the expert gave them; lead item 2 records it |
| Expert | 2 | Applied, merged with Codex 1 | Unit 3 question "Are the little trees under our big maple like it? Exactly like it?"; anchor the seedlings under a big tree with leaves pressed in October from it and from two or three same-kind trees; candidate now a class bean plant from a parent plant's seed |
| Expert | 3 | Applied | Unit 5 and the math table: three groups by light through (all, some, none), then "does it send the light a new way?" yes or no; s1-light-materials notes say so too |
| Expert | 4 | Applied | Mid-year check: a spoken sentence the teacher writes down |
| Expert | 5 | Applied | Cross-subject lead-in rewritten with math (1.MD.C.4 unit 1, weeks 2 to 4; 1.MD.A.1 and A.2 unit 6, weeks 23 to 25) and ELA units; "Taught by then in most orders" replaced by the unit that teaches it (math unit 1, ELA unit 1) |
| Expert | 6 | Applied | "across about 34 weeks (a school year of about 36 weeks, of which about 34 carry science lessons here)"; the same form used in K (32) and grade 2 (34) |
| Expert | settled | Applied | All seven rows; the October leaf pressing is in unit 3's anchor and reason (about weeks 11 to 14), the rice-on-plastic-wrap drum is in unit 4, the robin nest and the white-tailed deer doe and fawn are unit 7's two sources |
| Codex | 1 | Applied, merged with expert 2 | The plant comparison is required, not a candidate: one shared feature and one difference between young and parent; dated photographs of a parent plant and young grown from its seeds where no seedlings grow; the class account covers plants and animals; the unit's end task and the mid-year check each use a fresh plant pair; s1-like-parents notes changed |
| Codex | 2 | Applied | Unit 2 and s1-parts-mimic notes: plants respond too, a dated photograph sequence of a shoot turning toward the light, observation only |
| Codex | 3 | Applied | Same as expert 5 |
| Codex | 4 | Applied | The kindergarten stale note, fixed with kindergarten expert 4 |
| Codex | 5 | Not acted on here | The math grade 1 frame's stale lead-in is another subject's frame: under Cross-subject notes |
| Codex | 6 | Not acted on here | `docs/RUBRIC-SCIENCE.md` lines 54 to 55 are outside this pass's files: under "For the lead" with Codex's replacement text |
| Codex | settled | Applied | Order, days, split unit and the direct-comparison bridge kept; plant evidence and plant response added |
| Writer | lead 2 | Applied | Kept, with the new observation time |
| Writer | lead 3 | Kept | No change needed |
| Writer | lead 1, 4 | For Cory | Time a week (two lessons of 30 to 35 minutes); materials ceiling of about $40 a class |

Conflict, Codex against expert on unit 8: Codex judged the going-home-time fallback defensible; the expert showed it
is the usual case, since school ends before the earliest winter sunset in the contiguous United States, so the chart
would show no pattern. The expert's settled row is applied; it keeps the fixed-clock-time observation the evidence
statement Codex cites asks for, at a time that crosses sunset.

Counts: applied 10 (expert 1 to 6, Codex 1 to 4), not acted on 2 (Codex 5 and 6, outside this pass), for Cory 3.

## Grade 2

| Report | # | Result | What was done |
|---|---|---|---|
| Expert | 1 | Applied | Unit 3 C3 adds cause and effect (the test shows which material causes the dry hat); unit 4 develops energy and matter (pieces broken apart and put together into a new, larger object); the brief's crosscutting list adds both |
| Expert | 2 | Applied | Readiness looks: unit 2 opens with a one-question look back at kindergarten's severe weather; unit 7 with the kindergarten needs-and-places map |
| Expert | 3 | Applied | Burrs and seed heads gathered in fall and kept dry; hook-and-loop stand-in, said to be a model (unit 6 and the brief's kit list) |
| Expert | 4 | Applied | The year named the same way as K and grade 1 |
| Expert | settled | Applied | All three rows |
| Codex | F1 | Applied | Unit 7 question "What kinds of plants and animals do we find in each place, and how are the places alike and different?"; a picture inventory (sketches, photographs, agreed describing labels), counts graphed, kinds shared and different compared; the end-of-year check uses an unfamiliar pair of inventories with equal counts but different kinds; s2-habitat-diversity notes changed. Not a conflict with the expert, who judged unit 7 on its count and boundary only |
| Codex | F2 | Applied | PS1.A for 2-PS1-1 says many kinds of matter can be solid or liquid depending on temperature. Unit 3: water and ice observed, properties recorded, each sample classified, qualitative words, adult prepares; a two-temperature item in the unit's end task and the mid-year check; unit 4 retrieves the record; s2-material-properties notes changed |
| Codex | F3 | Applied | Unit 1: a supported source choice between two supplied sources before the chart, a source-choice item in the unit's end task, no student internet searching; s2-water-where notes changed |
| Codex | F4 | Applied | Storyline bullet: anchor explained with the revised model, and an individual end-of-unit task on an unstudied case, inside the unit's days (also applied to K and grade 1) |
| Codex | F5 | Applied | Math lead-in rewritten (graphs unit 1, weeks 2 to 3; ruler unit 3, weeks 8 to 12); the plant row's "Taught by then in most orders" replaced |
| Codex | F6 | Applied | The grade 1 stale note, fixed with grade 1 expert 5 |
| Codex | F7 | Not acted on here | The math grade 2 frame's stale lead-in and its unit 3 "science measures plants in fall" claim: under Cross-subject notes |
| Codex | settled | Applied | All six rows: inventories; cooler and warmer conditions; the source choice; end-of-unit transfer; two of the eight third-lesson weeks in weeks 1 to 4 so unit 1 is done by week 4 (brief "Days" and the social studies line); scale, proportion and quantity named in the brief |
| Writer | lead 1, 3 | For Cory | Time a week (two lessons of 35 to 40 minutes, a third in about 8 weeks); materials ceiling of about $50 a class |
| Writer | lead 2 | Kept | Seasonal order unchanged; the burr fix removes the spring gap |
| Codex | For Cory | Collected | K to 2 device assumption |

Counts: applied 10 (expert 1 to 4, Codex F1 to F6), not acted on 1 (Codex F7, another subject), for Cory 3.

## Progression changes (data/progressions/science.csv, 10 rows)

| Row | Change |
|---|---|
| sk-living-needs | Notes: "Extends the patterns model from the weather chart (sk-weather-watch)" in place of "Introduces"; model_in now patterns |
| sk-weather-watch | Notes: the chart starts in week 1 as a two-minute routine; the unit compares September against October |
| sk-needs-places | Notes: people in the model (the town and its water source), the part social studies grades 1 and 2 review |
| s1-parts-mimic | Notes: plants respond too (a shoot turning toward the light), observation only |
| s1-like-parents | Notes: the young-against-parent plant comparison is required; the account covers plants and animals |
| s1-daylight-seasons | Notes: "(going-home time)" replaced by the 5:30 pm family reports beside a monthly day strip, as the expert gave it |
| s1-light-materials | Notes: three groups by light through, then the "new way?" yes or no |
| s2-material-properties | Notes: the same material under cooler and warmer conditions, classified; s2-heat-cool-change retrieves it |
| s2-water-where | Notes: the supported source choice |
| s2-habitat-diversity | Notes: picture inventories; kinds shared and different as well as counts |

No assumes or hands_on changed, so both ends of every handoff are as before; the grade 3 frame's Seams table needed
no edit.

## Cross-subject notes (for those frames' owners; not edited here)

- **Math grade 1** (`docs/courses/math-grade-1/frame.md`), Cross-subject lead-in: says the other frames are written
  later. Codex grade 1 F5 replacement: "The grade 1 science and social studies frames are available. Mathematics
  teaches three-category data work in unit 1 before science uses it. Science's early leaf comparison uses its stated
  direct-comparison bridge before formal length work in mathematics unit 6." (Drop Codex's line on ELA timing being
  pending: the ELA frame exists.) Its s1-like-parents row now orders leaves of young and parent plants, still by
  lining up ends.
- **Math grade 2** (`docs/courses/math-grade-2/frame.md`): the lead-in's "written later" and unit 3's reason that
  science measures plants and seeds in fall. Science measures plants about week 23 and seeds about week 27. Codex
  grade 2 F7 replacement: "This unit establishes ruler measurement before science's later plant and seed
  investigations. Mathematics uses classroom objects and its own measurement data."
- **ELA kindergarten**: its K-ESS2-1 bridge says "science's recording deepens them later"; science's chart now runs
  from week 1 and its unit 2 runs about weeks 5 to 10, so science comes first. The bridge can stay; the wording
  could say science's chart is already running.
- **ELA grade 2**: leans on 2-LS2-2 (week 16) and 2-LS2-1 (week 18), which science teaches later (weeks 27 and 23).
  ELA's own bridge (its texts carry the facts) holds; nothing to change unless the two subjects want the pollinator
  units nearer each other, which would move a science unit and is not proposed.
- **Social studies grade 1** (ss1-calendar-time): reads the daylight pattern from science; the observation is now
  light or dark at about 5:30 in the evening with a monthly day strip. Its frame needs no change.
- **Science grade 3** (`docs/courses/science-grade-3/frame.md`), brief "Days": "30 of the year's 32 teaching weeks".
  The K to 2 frames now name the year as "a school year of about 36 weeks, of which about N carry science lessons
  here"; grade 3 could use the same form. Outside its Seams table, so not edited.

## For the lead (outside this pass's files)

- `docs/RUBRIC-SCIENCE.md` lines 54 to 55 call the grade 4 scope and sequence and the middle school base text the
  only science material. Codex grade 1 F6 replacement: "Science planning material now includes the science
  progression, course frames, the grade 4 scope and sequence draft, and the middle school base text. These
  establish planning commitments; they do not establish that a finished science course exists."
- Codex grade 1 and grade 2 both name, for the source list (docs/APPROACH-SOURCES.md), the NGSS evidence statement
  addresses for grade 1 life science and the grade 2 expectations, the K-5 science evidence guide v2.0, and the
  OpenSciEd elementary unit overview pages (public descriptions only).

## For Cory

- **Materials ceilings (money).** About $40 a class for kindergarten and grade 1, $50 for grade 2, beyond what the
  room has. Both readers ask for confirmation, Codex after a quantities-based estimate.
- **K to 2 science time (audience).** Kindergarten about 60, grade 1 about 65, grade 2 about 80 minutes a week, then
  grade 3 at 180. One decision for K to 5 would make the step deliberate.
- **Readers (people).** The disaster-aware reader for K unit 2 and grade 2 unit 2; the adoptive and foster family
  reader for grade 1 units 3 and 7; a science teacher's safety read for every hands-on unit, grade 2 unit 4's
  heating above all.
- **K to 2 device assumption (audience).** Codex grade 2 asks for it before presentation and tool requirements are
  fixed (also raised in the social studies K to 2 pass).

## Settled (for docs/reviews/DIGEST.md)

| Choice | Course | Reason |
|---|---|---|
| Weather chart starts week 1 as a two-minute routine; unit 2 compares September and October | K | Two months of data by the unit's end |
| K-ESS3-1's human case is the class's own town and its water source | K | The standard names humans; social studies grades 1 and 2 review it |
| Unit 4 opens on fall photographs; unit 5 compares sun and shade slides on any sunny day | K | Anchors visible in winter; relative-only boundary |
| sk-living-needs extends, not introduces, the patterns model | K | sk-weather-watch introduces it earlier in the year |
| Daylight observed at about 5:30 pm by family reports beside a monthly day strip | 1 | Going-home time is light all year at most schools |
| Unit 3 anchor: seedlings under a parent tree; the plant comparison is required | 1 | 1-LS3-1 is young against parents, plants and animals both |
| Plants respond too: a shoot turning toward the light, observed | 1 | 1-LS1-1's core idea includes plant responses |
| Light test: three groups (all, some, none), then "sends it a new way?" | 1 | Keeps 1.MD.C.4's three groups and all four materials |
| Robin nest and white-tailed deer doe and fawn as unit 7's two sources | 1 | A bird and a mammal in public-domain federal media |
| Unit 3 adds cause and effect; unit 4 develops energy and matter | 2 | Each expectation's own crosscutting concept |
| Habitat inventories compare which kinds as well as how many | 2 | 2-LS4-1 compares the kinds in each habitat |
| Water and ice classified at two temperatures in unit 3 | 2 | PS1.A: matter can be solid or liquid depending on temperature |
| A supported source choice before the water chart | 2 | 2-ESS2-3's obtaining practice includes useful sources |
| Burrs gathered in fall for the spring unit; hook-and-loop stand-in | 2 | The anchor exists in spring |
| Two third-lesson weeks in weeks 1 to 4 | 2 | Unit 1 done before social studies grade 2's week 6 |
| Every unit ends with an individual task on an unseen case, inside its days | K, 1, 2 | Transfer at the end (science lens) |
| The year named "about 36 weeks, of which about N carry science lessons here" | K, 1, 2 | One year, stated one way |

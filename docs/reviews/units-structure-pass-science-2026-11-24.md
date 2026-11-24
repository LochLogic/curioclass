# Science unit plans: structure pass, 2026-11-24

One pass over the "For the structure pass" and "Day faults" items of the stage 4 unit reads for the 12 science courses
(docs/reviews/units-read-<course>-2026-11-24.md: biology, chemistry, physics, kindergarten and grades 1 to 8), modeled
on the social studies pass of 2026-11-14. Items are grouped by target. Each is marked **applied** (and how) or **not
applied** (and why). Each was checked against the current file before it was changed.

Only shared files were changed: days.csv, source-map.csv, frames, scopes and sequences, TOOL-ASKS.md files, and the
mechanical parts of unit plans that copy days.csv (day-list rows, header kind counts, skel blocks, a goal-map row).
No day file was edited. Day faults went to data/plans/defects.csv (7 rows).

## Gates

| Gate | Before | After |
|---|---|---|
| `unitplan.py check science` | 155 PASS, 0 FAIL, 1 note | 155 PASS, 0 FAIL, 1 note |
| `sequence.py check <course>`, all 12 courses | 0 failures each; notes: biology 2, chemistry 25, physics 2, grade 3 2, grade 4 9, grade 7 1, others 0 | the same |
| `plan.py check`, failure lines for the 12 courses | grade 1 13, grade 2 17, grade 3 21, grade 5 19, grade 7 175, kindergarten 13; all frame gates 0 | the same |
| `lesson.py check`, FAIL lines (whole repository) | 1,049 | 1,049 |

No progression changed, so the progression gate was not run. The pre-existing plan.py and lesson.py failures in these
courses (sections missing from data/units.csv, one-ask and shape-note checks) are untouched by this pass.

Failures added along the way, and what was done:

- **Grade 2 days 23 and 24 to Check: undone.** The kind change made both written days fail lesson.py as assessment days
  (8 new failures: At home minutes, collection, hand-back, At home path). The days, the s02 day list, header and goal
  map, and the u02-3 header were put back. A Check kind for these observe days needs the two day files rewritten as
  assessment days first.
- **Kindergarten day 4 goal: undone.** The longer goal ("then pull the box ...") made plan.py fail: no item in `shows`
  shows the pull half. It waits on the day 4 day fault (defects row). The day 4 supplies, safety and kind changes stay.
- Grade 6 days 50, 67, 74, 75, 78, 80, 81 and grade 8 day 123 failed sequence.py once their supplies were filled
  (safety empty). Fixed: day 50 and day 123 safety "none"; days 67 to 81 take day 55's weather safety line, as s03
  field 8 says ("Day 55 supplies and safety apply through day 83").
- Grade 8 day 144 to Application failed unitplan.py (no goal-map row). Fixed: a goal-map row was added for day 144
  (item-level wording, mine) and field 7's respond list drops day 144.
- Grade 1 day 24's new note ("teaches the cat family") raised a sequence.py note on a Fluency day; reworded to "is the
  cat family case".

## Ledger

### data/plans/<course>/days.csv

**physics**

- **Day 151 supplies and safety: applied.** Two smooth solid spheres about 2 and 4 centimeters across (wood or hard
  plastic, no glass), spoon and catch sheet replace "small sphere"; "metre stick" became "meter stick" (US spelling);
  safety now says "contain; collect damp, never dry sweep".

**science-grade-1** (all applied as the read gave them, after checking each old value)

- Day 1 safety: outdoor looks line. Days 10, 16, 18 to 21 safety: safety glasses near fan tests and cutting.
- Day 24 note: the cat family (C24) after day 23's dogs, worded "is the cat family case" (see Gates).
- **Day 32 kind: applied**, Application to Understanding; s04 header now understanding 2, application 2, and the u04-2
  header understanding 1 (32). The optional second 4.2 day is a calendar call: **not applied** (see For Cory).
- Day 33: ruler and paper ribbon replace the tissue strip in supplies, the ruler safety line added, the note's cases
  renamed.
- Days 38 and 43 retrieval pictures; days 39, 44, 46 battery line; days 43 and 44 darkness line; day 46 stand, side
  screen, tape and peer-plan sheet; days 53 and 55 shared flashlight, day 55 paper strips; day 56 robin feeding
  photograph; day 60 waiting cards and crayons; day 63 paper token card and its safety line; day 64 waiting cards.

**science-grade-2**

- **Days 23 and 24 kind to Check: not applied** (tried and undone, see Gates). The s02 header and goal-map rows stay.
- **Day 64 note: applied.** Every child models the jay's seed job; pollen movement is checked on the day 63 retrieval
  card; both jobs are taught.

**science-grade-4**

- **Tools: applied.** Days 4 and 10 "ramp-and-cup collision tool" (s01 field 8), day 46 "wave tank tool" (s03 field 8).
  The same finding covers the other tools field 8 names, so they were filled too: days 21 and 23 "circuit paths tool",
  day 33 "resource paths tool" (s02), day 96 "light-path box tool" (s06).
- **Days 18, 25, 36, 39: applied from s02 field 8.** Day 18 shared flashlight; day 25 the optional car and solar heater
  materials, impact goggles and their two safety lines; days 36 and 39 the opaque card with adult-cut pattern, two
  folded-foil switches and "foil edges: fold smooth and adult checks" (day 25 already had it).
- **Day 23 kind: applied**, Fluency to Application; s02 header now understanding 8, application 12.
- **Days 50 to 52: applied**, the mirror safety line dropped.
- **Days 59, 60, 71 cloth barrier; 65, 67, 68 gloves; day 61 chalk or soft limestone; days 67 and 68 button or counter
  tokens: applied.**
- **Days 86 to 88: applied in part.** Splash goggles and the goggles safety line added; "soil" became "sand" in two
  safety lines. Nested trays **not added**: s05 field 8 gives them to day 85, not days 86 to 88.
- **Day 100: applied** from s06 field 8 (clear plastic enclosure, two impact goggles, the catch-station line).
- **Day 105 note: applied**, "original drawings only" for cactus spines (s06 field 10).
- **Day 106 kind: checked, no change.** The s06 U6 row says Fluency, as days.csv does.
- **Day 108: applied.** Adult-only dissection before class in goggles; tweezers adult use only; clear containers.

**science-grade-5**

- **Days 81 and 99 notes: applied.** "retrieved in unit 5 (days 85, 92)"; "grade 4 design and resources (days 100,
  103)".

**science-grade-6**

- **Kinds: applied.** Day 7 Application; day 39 Understanding; days 119 and 130 Understanding. Headers of s01, s02 and
  s05 recounted.
- **"60 C" to "40 degrees Celsius": applied** on days 23, 34, 35, 42, 59, 71, 79, 85.
- **Unit 1: applied from s01 field 8.** "uncoated clear sample" and safety glasses on the kit days 1 to 3, 5, 6, 8, 9
  and 13; splash goggles on day 14. Days 4, 7 and 16 were **left without glasses**: field 8 gives them no kit (day 16
  uses recorded views). Day 13 was added because field 8 names it a kit day.
- **Days 48 and 49 ice; day 50 supplies; days 125 and 126 smooth block; day 151 safety glasses: applied.**
- **Days 67, 74, 75, 78, 80, 81 supplies: applied** with day 55's weather instruments (s03 field 8), and the matching
  safety line (see Gates). **Day 87: not applied**: s04 field 8 names no materials for it.
- **Day 74 goal: applied**, "Draft storm and estuary explanations from the linked models."
- **Days 148 and 155: applied**, "(no-kit)" became "(printed original records, all classes)".
- **Days 153 and 154 notes: applied**, "scored once" became "retained, unscored".
- **Day 130 "add the tool" and days 143, 144, 146 "micrograph tags": not applied.** Not clear enough to place: s05
  field 8 calls day 130 paper only, and the read does not say what the tags are.
- **Days 133 and 134 notes, and the day 159 MS-ESS2-2 prompt: not applied.** Both hang on finding 1 or 2's either/or
  (a scored draft in days.csv, a rule that a course check may score new work, or moved teaching), which is a lead
  call on the UNIT-PLAN scoring rule and on minutes.

**science-grade-7**

- **Goals of days 55, 59, 61, 155: applied.** Days 55, 59 and 61 now match the plan's day list; s06's day 155 row was
  updated.
- **Day 21 and day 88 notes: applied.** The d021 day skeleton was regenerated and no longer contradicts F7.

**science-grade-8**

- **Day 21 and day 23 notes: applied** ("practices", US spelling).
- **Days 5 to 14 supplies: applied in part.** Masking tape and the 0.5 kilogram rice-bag ballast added on the hands-on
  days of s01 field 8 (5, 6, 8, 9, 10, 13, 14), not the printed days 7, 11, 12. "Measuring ruler" was already there.
  The speed-timing method and the cost line: **not applied** (no method named; days.csv has no cost column).
- **Days 13 to 15 as paper and printed tool only: not applied.** s01 field 8 lists 13 and 14 as hands-on cart days
  with no free launches; the change would contradict it. For the lead.
- **Days 20 to 24 safety, day 20 note: applied.**
- **Day 44 note "P1 revision: 5 min"; notes of days 27, 29, 30, 37, 39 to 41, 44 "supplied model records": applied.**
  The four sound makers for days 29 to 31: **not applied** (not named).
- **Day 38 s6-state-change retrieval: not applied.** An either/or sequence call (add a row or drop the need).
- **Day 47 and the hands-on days 49 to 52, 54 to 56, 60 to 62, 68 to 71: applied.** Resistor, soft stop, cardboard
  sheet and wooden block added; a 1.5-volt AA cell on day 47 (the others already hold an AA battery); the spring scale
  on days 68 to 71; the magnet swallow and count line in safety.
- **Goals of days 62 and 70; day 73 note: applied.**
- **Days 64 and 65 tools: not applied.** Conditional on what the field tool shows, which waits on its spec.
- **Days 77 to 91 codes, day 78 code and skill, and units 77 to 104 to one section 4.1: not applied.** They undo the
  six section cuts in s04 and drop MS-PS4-2 from 14 days, coverage and section calls for the lead with field 2 and
  field 5 consequences; the read does not say why the cuts should go.
- **Lamp days 85 on: applied** to the lamp days 85, 86, 88 to 91 (battery-powered LED, no cord; white paper, tape
  markers, safety glasses).
- **Day 121 note "collection 10 min"; day 122 safety; day 123 paper only: applied.** Day 123 safety is "none".
- **Day 144 kind: applied**, Respond to Application (goal-map row added, see Gates).
- **Day 148 paper slips: applied.** Day 150 left: the read made it conditional on reuse.
- **Day 154 and day 157 notes: applied.**

**science-kindergarten** (data/plans/science-kindergarten/days.csv)

- **S1 goggles on the safety page's days: applied** (safety line and supplies, 27 days).
- **S2 day 4: applied in part.** Box and string in supplies, the string safety line. The goal change was undone (see
  Gates) and waits on the day 4 day fault.
- **S3 kinds: applied.** Day 4 Understanding, day 7 Application; s01 header now understanding 5, application 2; u01-1
  and u01-2 headers recounted. The written day files carry no kind, so none needed a change.
- **S4 drawing paper and crayons; S6 weather records (day 18's forecast sequence removed); S7 day 22; S8 days 27 and
  28; S9 day 25; S10 day 35; S11 day 41; S13 day 8; S14 day 56: applied.**
- **S5 fold notes: applied** on days 7, 12, 16, 23, 26, 35, 39 and 58, in day 48's wording.
- **S12: applied** in docs/courses/science-grade-1/s01.md field 3: "Kindergarten day 64 records the grade 1 handoff."

### data/plans/science-grade-8/source-map.csv

- **Days 17, 25 and 26 rows: applied.** The `why` cells now say "Ours and original: written for Curio Class with no base
  lesson adapted" in place of "adapted from 8.1 lesson 10 / 15".
- **Lesson 15 rows and day 158: not applied.** Either/or (give day 158 lesson 15 minutes or move the row), a minutes
  call.

### data/plans/science-grade-4/source-map.csv

- **New rows for unit 1 and unit 2 sources: not applied.** Grade 4 has no source-map.csv; making one for reference
  pages (not base lessons) is a layout choice for the lead. Field 10 of both plans already names every source.

### Frames

- **science-grade-1: applied.** Units 5 and 8 "Why this unit, here" cells end with a full stop; unit 5's compelling
  question now matches s05 ("why does a beam show a bright patch behind wax paper but a shadow behind cardboard?").
- **science-grade-3 unit 1 "Why this unit, here": applied.** "the first of grades 3 to 5, building on the fair
  comparisons of grades 1 and 2".
- **science-grade-4: applied.** Unit 3 check set reads "None (the string-and-cup telephone candidate was dropped ...)",
  and s03 field 10's copy was changed to match; the unit 5 anchor names volcanoes "erupted or possibly active within
  the past 10,000 years", as s05 does.
- **science-grade-6: applied.** "60 C" to "40 degrees Celsius"; C3 practices: unit 2 adds argument from evidence, unit 4
  constructing explanations, unit 5 obtaining, evaluating and communicating information ("analysing" to "analyzing").
  **Unit 4 C3 against the s04 Q9 table: not applied** (no exact edit given).
- **physics, "Simulation to list" for units 2, 4 and 6: not applied.** Optional; only unit 2's row has it, and tool
  listings wait for step 9.

### Scopes and sequences, section plan headers

- **science-grade-2 unit 6 paragraph: applied** (every child models the jay's seed job; pollen checked on the day 63
  card).
- **science-grade-2 "Course-level checks", toast: not applied.** It names the day 74 replacement case, which the day
  fault has not chosen yet; the defects row for day 74 carries it.
- **science-grade-3: applied.** 3-LS4-4 teaching evidence "87 to 94"; the source-map sentence now says source-map.csv
  holds the section rows and teacher references G56 to G61 (paraphrase only); u02-3 header "application 2 (29, 30)".

### TOOL-ASKS.md

- **biology: applied.** New file with one heading per linked tool (body feedback, DNA-to-protein code, sealed-jar gas,
  energy pyramid and carbon reservoir, population model, cross and meiosis, natural selection, river and dam
  trade-off, fishery and species protection), each with its unit, mark, days, job and verdict from field 8. The
  detailed asks are still to write.
- **science-grade-8: applied.** Heading "Crosses over generations" (days 118 and 119, practice with feedback).

### Unit plan copies of days.csv

- Day-list rows were updated for every changed day (goal, kind or note cells only), header kind counts were recounted,
  and skel blocks that matched the earlier skeleton word for word were regenerated.
- Skel blocks that writers had already changed by hand were left: field 8 in grade 1 s01, s02, s04 to s08 and
  kindergarten s01 to s06 (they hold materials.csv lines the current generator writes differently), grade 4 s03 and
  grade 6 s02 field 10, and grade 8 s06 field 8. They still list the old supplies and safety. The gate does not check
  them; they are refreshed when each plan is next regenerated.
- Day skeletons: only grade 1 d064 and grade 7 d021 were regenerated. The other 77 sidecars for changed days in
  grades K to 3, 5 and 7 already differ from the current generator, so a refresh would change more than this pass.

### Scripts and rules

- **unitplan.py CAP_MERGED only for one-section units (grade 5): not applied.** It would fail grade 5 s01 and s06 at
  once, and whether a multi-section unit's U fields shrink to pointers is a rule call for the lead (UNIT-PLAN.md,
  "Length").
- **Readiness generation treating a row used earlier this year as retrieval (grade 7 F9): not applied.** A change to
  unit_skeleton.py and sequence.py that moves readiness counts in every subject; for the lead.
- **UNIT-PLAN rule on whether a course check may score new work (grade 6 finding 1): not applied.** A rule decision.
- **Grade 6 unit 3 skel listing s6-particle-temperature as owned: checked, no change.** The skeleton lists every skill
  unit 3's days cite; the progression gives the row to grade 6 and unit 2 first teaches it, which field 3 already
  says. Dropping it from unit 3 day rows is a sequence call.
- **Grade 7 s01 stale lines about grade 6 unit 3 and the day 90 Tomorrow line: already fixed.** Field 3 now says the
  grade 6 plans document both.

### Left for later and checks

- Grade 6 unit 3: the NOAA and USGS source pages are blocked to automated reads; status "browser check" for the lead.
- Grade 6 unit 2: the no-kit record sets are still to write.
- Biology days 102 and 126 stay Fluency, as the read advised.

## Day faults (data/plans/defects.csv)

Seven rows, found_by "units-read 2026-11-24", ref "stage 4 reads", status open, made_at day:

- science-grade-1 u05-2/d044.md: exit X44 needs a second, side-screen ask.
- science-grade-1 u05-2/d046.md: Swap line object and family line mirror.
- science-grade-2 u04-2/d043.md: exit Series B to coconut oil.
- science-grade-2 u02-1/d011.md: new duckling retrieval case.
- science-grade-2 u07-2/d074.md: replace the toast record; then the scope's course-level line.
- science-grade-2 u04-1/d040.md and u05-1/d051.md: optional spoken or drawn exit part.
- science-kindergarten u01-1/d004.md: pull-direction work before day 8 item 4; then the day 4 goal.

Biology, chemistry, physics and grades 3 to 8 reported no day faults (grade 7's d021 skeleton note cleared with the
regenerated sidecar).

## For Cory

- **Kindergarten eye protection is in no budget.** About 27 rolling, pulling and tray meetings need 31 child-sized
  Z87.1 splash goggles, and the written days run no trial without them. Options: (a) the school supplies them and the
  plans say so; (b) add them to the course budget, well past about $40; (c) keep as is, photographs where a school has
  none.
- **Kindergarten unit costs sum to $42** against the approved "about $40 a class". Options: (a) accept $42 as "about
  $40"; (b) trim unit 6's $12 (reuse school gloves and grabbers) to reach $40.
- **Grade 6 safety guide.** Which state or district safety guide should every unit cite? s06 uses a state handbook,
  the others NSTA.
- **Grade 7 costs.** Units 2 and 3 run above the scope and sequence ($255 and $94 for one child against $160 and $62;
  $80 and $37 against $64 and $30): accept the higher totals or trim the materials lists.
- **Grade 7 and ELA.** The ELA river research deadline for days 152 to 156 is still unknown and needs coordinating with
  the ELA course.
- **Grade 5.** The frame's open question about the state-test audience is still his.
- **Grade 1, optional.** A second 4.2 day before day 33 is a calendar call, for the Desk if wanted.
- Grade 8: none new; the s03 cost line still needs a stock and resistor price check, already flagged in the plan.
  Biology, chemistry, physics, grades 2 to 4: none.

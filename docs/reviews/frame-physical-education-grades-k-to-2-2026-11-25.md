# Expert read: course frame of Physical Education, grades K to 2 (2026-11-25)

Fresh expert read, cold, of docs/courses/physical-education-grades-k-to-2/frame.md, the subject's pilot after-core
frame. Brief: docs/pipeline/briefs/frame-read.md with the after-core changes the caller gave. Nothing but this report
was edited.

## What I read

- docs/agents/EXPERT.md; the lens docs/agents/lenses/physical-education.md; the bar, PE row of "Before a scope and
  sequence in this subject" and part 4 of docs/ADOPTION-BAR-SUBJECTS.md; docs/courses/physical-education/STANDARD.md
  and APPROACH.md in full; every DESK-ANSWERS.md entry naming PE (2026-11-16 q-later-arts-health-pe; 2026-11-20
  pre-work calls; the 2026-11-20 course shape and dose entry logged 2026-11-22; 2026-11-21 q-prework-open-1 and
  q-fix-pe-1; 2026-11-22 PE grades 11 and 12 flag; 2026-11-25 after-core frames).
- docs/pipeline/briefs/frame-write.md, including "After-core courses (added 2026-11-25)".
- The frame in full; its row in data/plans/frames.csv; its 35 rows in data/plans/calendar.csv.
- The rows: course-list.csv `file:physical-education&grade:K|1|2` selects the 48 K to 2 rows of
  data/progressions/physical-education.csv (read in full), with the grade 3 picker ids named in hands_on.
- data/standards/shape-pe-2024.txt, the 49 span-2 indicators in our words.
- Beside it: the Units and Cross-subject tables of the health, SEL and visual arts K to 2 frames (all written the
  same evening, after this frame), math kindergarten units 1, 2 and 8, math grade 1 unit 6, social studies grade 1
  unit 5; the core check weeks for K, 1 and 2 from calendar.csv.
- Gates: `python -X utf8 scripts/frame.py check physical-education-grades-k-to-2`: 0 failures (notes: unit days by
  year K 74, 1 74, 2 74; 22 units, 240 days, 222 in units, 18 for checks and respond days).
  `python -X utf8 scripts/stale.py check`: 70 files, 0 failures.
- Spot checks at source on the web (listed under Sources).

## Verdict

The frame is sound and is a good pilot: every one of the 48 rows is placed once, all 49 span-2 indicators have an
owner unit, each year is whole with its own units, checks and outcomes per standard, the order follows how motor
skills develop, and the calendar rows match every week and day the frame states and avoid every core check week
of the same grade. The biggest risks are two things other frames would copy: a shorter path whose arithmetic does
not reach the 64 sessions it names, and same-year overlaps with health and SEL (foods for energy, water rules,
calm steps, Ampe) that this frame was written before it could see. Fix the short path and the overlaps first; the
rest are smaller repairs.

## Findings, most serious first

### 1. The shorter path drops 10 days but names a 64-session path (serious)

- **What is wrong.** The Shorter path bullet says the 64-session path each year "drops 10 Fluency days". Each year
  is 80 days; 80 less 10 is 70, not 64. APPROACH.md "Pacing" sets short paths of 60 to 64 sessions.
- **Why it matters.** Bar C2 fails on "no short path" or days that do not add up; every other PE band will copy
  the bullet, and the scope writer will name 10 days and miss the target by 6.
- **Fix.** Rewrite the bullet: "The 64-session path each year drops 16 days, all Fluency days, at most 3 in any
  unit and never a unit's last Fluency day before its check, nor a check, respond, baseline or first-teaching day;
  both course-level checks stay. The scope and sequence names the 16 days a year and confirms each unit keeps at
  least one Fluency day." (Fluency is about half of 74 unit days, about 37 a year, so 16 fits.)
- LAYER frame. REPEAT yes (short path faults in earlier frame reads). Confidence: firm (arithmetic).

### 2. Same-year overlaps with health and SEL, and a "new" model that is not new (serious)

The lens names "PE and health both teaching ... the physical activity outcomes" as an error. Four overlaps:

- **Foods for energy, grade 2.** Health grade 2 unit 12 (weeks 1 to 5, docs/courses/health-grades-k-to-2/frame.md)
  teaches "foods that give energy for play" on its snack day and says "PE then uses it, not teaches it again". PE
  unit 18 (weeks 13 to 16) teaches the same picture sort as first teaching. PE's Cross-subject row pairs
  g2-foods-energy with health k-fn-water-first and g1-fn-plate-and-water, and For the lead 6 proposes
  `health:g1-fn-plate-and-water`; the same-year row health actually names is `g2-fn-pick-best-snack`.
- **Water rules, grade 2.** Health grade 2 unit 13 (weeks 6 to 10) teaches "rules for water, bikes, fire and
  kitchens" (g2-s-outdoor-and-home-safety). PE unit 22 teaches the same rules again (stay with a grown-up, never
  near water alone, life jacket on a boat). PE's Cross-subject line says health teaches only "the reason behind
  water rules", which is not what the health frame says.
- **Calm steps, grade 1.** SEL kindergarten (k-sm-calm-down, SEL unit 2) teaches "stop, breathe" and SEL grade 1
  adds "count to five"; health kindergarten k-meh-calm-body teaches slow breaths and counting. PE's Models table
  calls calm-steps "New (g1-calm-steps)" and unit 11 introduces "three slow breaths or a count to five" in
  different words (lesson 6: "first" claims checked; one thread keeps one wording).
- **Ampe.** SEL K to 2 unit 5 (kindergarten, weeks 20 to 25) teaches Ampe as its game from Ghana; PE grade 1
  unit 14 picks Ampe again (see finding 5).
- **Why it matters.** Children lose PE minutes, already below the national figure, re-learning what they learned
  weeks before; the end-of-unit check scores a first-taught item that was really taught in health.
- **Fix.** (a) Unit 18: "Opens with a retrieval task on health grade 2 unit 12's energy-snack sort (weeks 1 to 5);
  PE teaches its own part, choosing what to eat and drink before and while playing and the water break, and checks
  SHAPE.S2.2.11." Cross-subject row: health `g2-fn-pick-best-snack` (same year, health first); If later: PE
  teaches the sort itself. For the lead 6: replace `health:g1-fn-plate-and-water` with
  `health:g2-fn-pick-best-snack`. (b) Unit 22: "Opens with a retrieval task on health grade 2 unit 13's water
  rules; PE's days go to the dry-land skills and SHAPE.S2.2.12." Cross-subject row: "health: the water rules
  (unit 13, weeks 6 to 10); PE: the skills and showing understanding." (c) Models: calm-steps "From SEL
  kindergarten (k-sm-calm-down, 'stop, breathe') and SEL grade 1 (count to five); used in PE from unit 11", and
  unit 11 opens with a retrieval task on the SEL card in SEL's words, so S4.2.9 is taught as using the steps during
  activity. (d) Ampe: finding 5.
- LAYER frame. REPEAT yes (cross-subject "both ends" faults in earlier reads). Confidence: firm (both frames read).

### 3. Three indicators narrowed below their wording (moderate)

- **SHAPE.S2.2.3** (key ideas behind traveling, staying in place and handling objects) is taught in unit 8, a
  traveling unit with no objects: the knowledge task names ideas only in a traveling movement.
- **SHAPE.S2.2.4** (show understanding of traveling, in-place and object-handling skills while moving) is taught
  in unit 21, a dance unit; the frame's example is "move at a low level, travel a curvy path". The progression row
  g2-show-ideas itself gives an object example ("throw along a straight path"), which the frame drops.
- **SHAPE.S2.2.12** (understand water safety and basic swimming): unit 22's knowledge task covers the safety rules
  only. Understanding basic swimming can be taught on dry land for every school; only doing it (S1.2.17) needs a
  pool.
- **Why it matters.** Standards in full (C1, lesson 4); the object-handling half of two concept indicators is
  claimed but never taught or checked.
- **Fix.** Unit 8 What students learn adds: "and in place and with an object: a ball rolled along a straight or
  curvy path, a scarf tossed high or low (S2.2.3 in full)"; its knowledge task names the idea in one traveling and
  one object movement. Unit 21 adds: "and with an object: a scarf or ribbon moved along a path or level in the
  dance, named in one sentence (S2.2.4 in full)." Unit 22 adds: "what floating and kicking are and why a back float
  helps, shown lying on the floor (S2.2.12 in full)", and its knowledge task asks one swimming idea.
- LAYER frame. REPEAT yes (standards narrowed to a headline). Confidence: firm (rows and indicator words).

### 4. No course-level check samples standard 4 in any year (moderate)

- **What is wrong.** Each year ends with a unit after its "year-end" check (units 7, 14, 22), which the core check
  weeks force (K and grade 1 weeks 29 to 32 are taken). The cost: K's whole S4 outcome sits in unit 7, after both
  checks; the grade 1 checks list no S4 task though unit 11 owns S4.2.9; the grade 2 checks list none though
  unit 16 owns S4.2.6. Across the band, no course-level check samples S4 at all.
- **Why it matters.** Bar criterion 1 asks for an assessment of every standard in every grade; the end-of-unit
  assessments cover it, but the year's cumulative checks never return to the personal-skills standard, and the
  pattern is about to be copied into 3 to 5, 6 to 8 and 9 to 12.
- **Fix.** (a) Move k-class-chances (S4.2.8, choosing a station and trying again, the first goal-cycle step) from
  unit 7 into unit 5, whose early tries are the natural "pick one, try again" setting, moving 3 days with it (unit 5
  to 15, unit 7 to 7); the K year-end check adds "picks a station and keeps trying (unit 5)". (b) Grade 1 year-end
  adds "a calm step named for a hard moment (unit 11)". (c) Grade 2 year-end adds "says the goal and shows the check
  (unit 16)". (d) Pattern rule for the other bands: across a year's two checks, every standard is sampled at least
  once from units before the check.
- LAYER frame. REPEAT new. Confidence: likely (one bar line and reasoning).

### 5. Cultural picks: a repeat, a narrow range and two unchecked claims (moderate)

- **Ampe repeats SEL kindergarten** (finding 2), against lesson 11 (picks chosen so they do not repeat another
  grade's).
- **Range.** The band's six picks are from Denmark, Mexico (twice in grade 1: La Raspa and Doña Blanca), Ghana,
  Germany and the US. Nothing from Asia, the Pacific or South America; C12 fails when one group carries the
  examples.
- **Seven Jumps** is labeled "the Danish folk dance". Folk dance notes found today give it as Danish (Syvspring)
  with a near-identical Dutch dance and a claim of German origin (folkdancefootnotes.org); the label holds only as
  "danced in Denmark and the Netherlands", with the source line saying so.
- **La Raspa** is often taught in a gendered double circle (boys inside, girls outside, in the Lloyd Shaw teaching
  sheet); the unit's note should say partners are set by the teacher with no gender roles (lens: no activity split
  by gender).
- **Ampe** as commonly played has a leader replaced or players losing turns; whatever game replaces it must name
  its no-elimination form.
- **Fix.** Grade 1 unit 14: replace Ampe with a game from East Asia, candidate Korea's "Mugunghwa kkochi
  pieotseumnida" (a freeze-and-go game; from memory, checked against a Korean cultural or education source; played
  with no one out: a moving child goes back three steps), keep Doña Blanca with its chaser rotating. Unit 13: Seven
  Jumps labeled "a folk dance from Denmark and the Netherlands", La Raspa with teacher-set partners and no gender
  roles. Unit 21 keeps Kinderpolka (it holds) and names the US play-party dance now (for example "Bow Belinda" or
  "Paw Paw Patch", from memory, each checked at a folklife archive), so lesson 11's pick is not left open.
- LAYER frame. REPEAT yes (picks named and checked). Confidence: likely (web spot checks; replacements from memory).

### 6. The Alberta safety guide link is dead and the guide superseded (moderate)

- **What is wrong.** https://education.alberta.ca/media/160206/sg_pa_final_2014.pdf now returns a one-page "We've
  moved" notice. Search shows the print guidelines were replaced by the SPHEReS online resource (myspheres.ca), and
  the Alberta Schools' Athletic Association (2022) asks schools to remove older printed copies. The Nova Scotia
  guide holds ("Physical Education Safety Guidelines, Grades Primary-12", September 2021, 321 pages, opened today).
  The CDC page holds ("Preventing Drowning", dated 2025-09-29: supervision, life jackets, swim lessons).
- **Why it matters.** Lesson 22: guides by title with a free link; the safety agent would read a dead or withdrawn
  guide.
- **Fix.** Safety read bullet: replace the Alberta entry with "SPHEReS, Alberta's online safety guidelines for
  physical activity in schools (https://myspheres.ca/en/), which replaced the 2013 print guidelines; the safety
  agent opens it first". Drop "from memory" on the CDC link and "not yet opened" on Nova Scotia (both opened
  2026-11-25 by this read). For the lead 5: keep the search for a US state guide.
- LAYER frame. REPEAT yes (sources not opened). Confidence: firm (opened at source).

### 7. Stale notes (minor)

- Cross-subject, After-core courses: "Their frames are not written". The health, SEL and visual arts K to 2 frames
  exist (written 2026-11-25, minutes after this one); only dance K to 2 is unwritten. Fix: "The health, SEL and
  visual arts K to 2 frames are written (2026-11-25); their units are cited in the rows above. The dance K to 2
  frame is not, so its unit numbers are not guessed." Then add health's and SEL's unit numbers and weeks to the
  rows (health grade 2 units 12 and 13, SEL kindergarten units 2 and 5).
- Safety read bullet and For the lead 5: "not yet opened by this writer", "Both are unread": replaced by finding 6.
- LAYER process. REPEAT yes. Confidence: firm.

### 8. Math kindergarten citation names the wrong unit and code (minor)

- **What is wrong.** Cross-subject cites "Counting aloud to 10 (K.CC.A.1 in part), math grade K unit 2 (days 19 to
  44)". Counting collections to 10 starts in math K unit 1 (days 1 to 18, weeks 1 to 4, K.CC.B.4a); K.CC.A.1 is
  owned by math K unit 8 (days 135 to 151).
- **Fix.** "Counting to 10 (K.CC.B.4a, math grade K unit 1, days 1 to 18, weeks 1 to 4; counting sequence K.CC.A.1
  owned in unit 8)". The If later line stands: counts of three in weeks 1 and 2 are said with the teacher.
- LAYER frame. REPEAT yes (citations). Confidence: firm.

### 9. After-core checks stack up in the same weeks (minor)

- **What is wrong.** The rule only keeps after-core checks out of core check weeks, so the free weeks fill up:
  kindergarten week 18 holds PE, ELD and visual arts mid-year checks and week 28 PE, ELD and library; grade 1
  week 18 PE, ELD and visual arts; grade 2 week 17 PE, ELD and visual arts, and week 27 PE, ELD and health.
- **Why it matters.** A five-year-old meets three checks in one week of short sessions; the pilot's weeks are
  already being copied.
- **Fix.** For the lead, a calendar rule: at most two after-core course-level checks in a grade's week; PE moves
  its kindergarten year-end to week 27 (days 66 and 67; unit 6 ends day 65, so unit 6 becomes 8 days and unit 7
  12), or the lead spreads the after-core subjects across weeks 18 and 19 to 21, 26 to 28. The frame names its
  weeks after the lead rules.
- LAYER process. REPEAT new. Confidence: judgment call.

### 10. "Begun toward" used for codes already owned (minor)

- **What is wrong.** Units 9, 10, 12, 15, 17 and 21 write "begun toward SHAPE.S1.2.x (owned in kindergarten ...,
  used here in new settings)". Lesson 29 keeps "begun" for a code owned later and calls a revisit review or use in
  new settings; STANDARD.md 3 rule 1 says later grades carry the code "used in new settings".
- **Fix.** "Used in new settings: SHAPE.S1.2.2 and SHAPE.S1.2.5 (owned in kindergarten, units 1 and 2)". Keep
  "begun toward" only where the owner is later (unit 9's S1.2.16, unit 10's S1.2.9). If frame.py reads "begun" to
  find `~` codes, the fixer checks the gate still passes.
- LAYER frame. REPEAT yes (owned, begun, revisited wording). Confidence: firm.

### 11. Two course-wide lines missing: heat and water breaks, and the logic model (minor)

- **What is wrong.** The lens fails a day for "heat with no water break"; APPROACH.md "Safe space" asks for a
  water break in warm weather. The Space bullet does not say it, and only unit 18 mentions water. APPROACH.md
  "Sources" says each course has a one-page logic model; the frame does not say where it sits.
- **Fix.** Space bullet adds: "Outdoor days in warm weather carry a water break and shade; the unit plan names
  them." Add a bullet: "Logic model. One page in the scope and sequence, one a year (inputs: 80 sessions of 30
  minutes; activities; outcomes per standard); the course page says it has not been tried with children."
- LAYER frame. REPEAT new. Confidence: firm (lens and approach lines).

### 12. One check day holds two skill tasks and a knowledge task for 30 children (minor)

- **What is wrong.** Units 2, 4, 12, 16 and 18 have one check day holding two skill tasks, or a skill task marked
  per cue plus a knowledge task. Six groups of five at 2 to 3 minutes leaves about 30 seconds a child for all of
  it, inside a 30-minute session with set-up.
- **Fix.** The Assessment bullet adds: "A one-day check holds one skill task watched in the rotation and a
  knowledge task asked of the same group in the same visit; where a unit lists two skill tasks, the second is the
  unit's last Fluency day's closure watch, carried as a mark (not first teaching), or the unit takes a second check
  day." The scope writer settles which.
- LAYER frame. REPEAT yes (end-day load, lesson 19). Confidence: judgment call.

### 13. Grade 2 week 30 is free (nit)

- Unit 22's reason says "grade 2 weeks 28 to 32 hold the core year-end checks"; week 30 holds none (science 28,
  math 29, social studies 31, ELA 32). Fix: "grade 2 weeks 28, 29, 31 and 32 hold the core year-end checks". The
  placement stands.
- LAYER frame. REPEAT new. Confidence: firm.

## Data checks

- **Owned skills.** 48 of 48 rows placed once (gate and my count). No unit lists a row another grade owns; every
  revisit is named in the text (see finding 10 for wording).
- **Standards in full.** 49 of 49 span-2 indicators have one owner unit; S2.2.3, S2.2.4 and S2.2.12 are narrowed
  (finding 3). SHAPE indicators have no lettered parts.
- **Units and reasons.** Every reason holds; no skill or model is used before it is taught (cue-words taught on
  jump and land inside unit 1 before the traveling days; safe-space unit 1; effort-scale unit 6 before 11, 12, 15,
  18; calm-steps 11 before 14 and 22, see finding 2; pulse-check 12 before 15; team-talk 17 before 19;
  tactics-question 20).
- **Days.** 240 = 3 x 80; each year 74 in units and 6 for checks; units K 13, 10, 11, 8, 12, 10, 10; grade 1 10,
  11, 11, 10, 10, 12, 10; grade 2 10, 10, 10, 10, 9, 6, 7, 12. Unit 21 is lean (5 teaching days for two dance
  styles and a sequence) but holds; unit 20 at 6 days fits one naming-level indicator. No unit far over or under its
  share. The 80 x 30 dose follows q-fix-pe-1 (2026-11-21), which is later than the 2026-11-20 "plan to the national
  body's recommendation" call and is what APPROACH.md "Pacing" settles; the frame states the gap openly. Holds.
- **Calendar.** All 35 calendar rows match the frame: K and grade 1 mid-year in week 18 (days 43 and 44, respond
  45), year-end in week 28 (68 and 69, respond 70); grade 2 mid-year week 17 (41 and 42), respond week 18 (43),
  year-end week 27 (66 and 67), respond week 28 (68); units 7, 14 and 22 in weeks 29 to 32 (22: 28 to 32). Core
  check weeks from calendar.csv: K 14 to 17 and 29 to 32; grade 1 14 to 16, 19, 29 to 32; grade 2 14 to 16, 18 to
  20, 28, 29, 31, 32. The frame's list matches exactly, and no PE check day falls in one; two respond days do
  (grade 2 weeks 18 and 28), as For the lead 7 says.
- **Seams.** Kindergarten has no course before (correct). Every hands_on to grade 3 matches a grade 3 row id; the
  two readiness checks downstream (g1-heart-muscle to g3-benefits, g1-world-games to g4-world-activities) are
  counted right.
- **Cross-subject.** Social studies grade 1 unit 5 (maps, continents) comes before unit 14: holds. Math: finding 8.
  Health and SEL: finding 2.
- **Base text.** None; no source map owed.

## Lens checklist (course frame layer)

| Lens line | State |
|---|---|
| Outcomes stated, not a year of games | Met: grade outcomes per standard per year in The course in brief |
| A grade with no outcome for one of the four standards | Met: all four in K, 1 and 2 |
| A span indicator placed in no year | Met: 49 of 49 |
| Skills out of developmental order | Met: locomotor and balance first, weight transfer grade 1, overhand and long tools grade 2, combinations last |
| Dance or fitness taught once and never again | Met: dance units 7, 13, 21; fitness units 6, 12, 15, 18 |
| Most of the class moving most of the time | Met at frame level: stations, one item a pair, no lines |
| A safe place to try; no elimination, targets, public picks, exercise as punishment | Met (Supports bullet, units 1, 14, 16, 20) |
| Every body included; no gender split | Met, with La Raspa's formation to fix (finding 5) |
| Fitness learned, not judged | Met: no scores, heart counts never compared |
| Assessment shows growth against own baseline | Met (Assessment bullet); S4 not in checks (finding 4) |
| Works in a real space, wet day, low equipment | Met; heat and water break missing (finding 11) |
| PE and health both teaching, or neither | Missed: foods, water (finding 2) |
| PE dance and dance course in the same year | Not applicable yet: the dance K to 2 frame is unwritten; the need is recorded both ways |
| Unit and day lines | Not applicable at this layer, except static stretch after warm-up (unit 15: met) |

## What the other PE frames should copy, and should not

**Copy.**
- One file per band with a Year column, units numbered through the band, each year whole; the Days bullet giving
  the band total, then per year, the dose source and the gap to the national figure stated openly.
- Grade outcomes per standard per year in The course in brief, each naming its units and how it is checked.
- Each unit pairing a motor row with a concepts, social or personal row, so its check has a skill task, a
  knowledge task and one conduct mark against a baseline watch.
- The check-day rule by unit length, the respond-day line, the C3 column used for cues and settings (and the lead's
  rename).
- The Space, Supplies and cost, Devices, Paper path, Water safety, Swaps and leave-outs and Sensitive ground
  bullets; the hazard and control wording in the last column; the core check weeks listed by grade in Course-level
  checks.

**Do not copy.**
- The shorter path arithmetic (finding 1): compute the days to drop from the band's own dose.
- "Their frames are not written" for sibling after-core frames: read the health, SEL, arts and dance frames of the
  same grades first and cite their units (finding 2, 7).
- Calling a model new without checking SEL and health (calm steps, goal steps, feeling words).
- The year-end check that samples no S4 (finding 4): sample every standard across a year's two checks.
- Week 18 and week 28 as default check weeks: check what other after-core courses already took (finding 9).
- "Begun toward" for an earlier-owned code (finding 10).
- Unopened safety links (finding 6).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Short path drops 16 Fluency days a year, at most 3 a unit, never the last Fluency day before a check | 80 to 64; Fluency is about half of 74 unit days | frame.md, Shorter path |
| Ampe in grade 1 unit 14 replaced by a game from East Asia (candidate Mugunghwa, Korea, no one out), confirmed at source | SEL kindergarten unit 5 already uses Ampe; widens the band's range | frame.md, unit 14 |
| Seven Jumps labeled "from Denmark and the Netherlands"; La Raspa with teacher-set partners, no gender roles | Origin contested at source; lens rule on gender | frame.md, unit 13 |
| k-class-chances moves from unit 7 to unit 5, 3 days with it (unit 5 to 15 days, unit 7 to 7) | So the K year-end check can sample S4 | frame.md, units 5 and 7, K checks |
| Health row for g2-foods-energy is `g2-fn-pick-best-snack`, health first | The same-year row health names | frame.md, Cross-subject and For the lead 6 |
| Alberta guide replaced by SPHEReS (myspheres.ca) | The 2014 PDF link is a moved notice; the print guide is superseded | frame.md, Safety read |
| Math citation is math K unit 1 (days 1 to 18), K.CC.B.4a | Unit 1 counts collections to 10; K.CC.A.1 is unit 8's | frame.md, Cross-subject |

## For Cory

- Nothing new. The equipment ceiling the frame already raises (For the lead 4, about $370 across the band from
  nothing, $0 on the low-equipment path) is still his.

## What I could not judge

- The dance K to 2 seam: that frame is not written.
- Whether the swap candidates (Mugunghwa, the play-party dance) are open to be taught: that is the sensitivity
  agent's read at source; mine rest on memory.
- The Nova Scotia guide's content on striking tools and mats: opened for its title only, not read.

## Sources

- SHAPE America guidelines page, https://www.shapeamerica.org/standards/guidelines : holds, 150 minutes a week in
  elementary and 225 in middle and high school.
- Nova Scotia, Physical Education Safety Guidelines, Grades Primary-12 (September 2021), the frame's link: holds
  (opened, 321 pages).
- Alberta, https://education.alberta.ca/media/160206/sg_pa_final_2014.pdf : does not hold, a "We've moved"
  notice; superseded by SPHEReS, https://myspheres.ca/en/ (search result; Open Alberta publication page
  https://open.alberta.ca/publications/safety-guidelines-for-physical-activity-in-alberta-schools).
- CDC, Preventing Drowning, https://www.cdc.gov/drowning/prevention/index.html : holds (page dated 2025-09-29).
- Seven Jumps: https://folkdancefootnotes.org/2023/06/25/seven-jumps-l-syvspring-denmark-de-zevensprong-netherlands/
  : Danish Syvspring with a Dutch twin and a claimed German origin; "Danish" holds only in part.
- La Raspa: https://www.lloydshaw.org/uploads/3/4/2/3/3423313/la_raspa.pdf : a traditional Mexican children's
  dance; holds; gendered formation noted.
- Kinderpolka: https://folktunefinder.com/tunes/5749 and the Lloyd Shaw "Children's Polka" sheet : German
  children's partner dance; holds.
- Ampe: https://en.wikipedia.org/wiki/Ampe_(game) and the UNICEF Ghana "Ampe Challenge" coverage : a Ghanaian
  jumping and clapping game; holds.

## For the source list

- SPHEReS (Alberta's online physical activity safety guidelines, https://myspheres.ca/en/), free, replaces the
  Alberta 2013 print guidelines.
- Nova Scotia PE Safety Guidelines 2021, the frame's link, confirmed working 2026-11-25.

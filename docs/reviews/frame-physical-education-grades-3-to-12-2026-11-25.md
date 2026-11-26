# Expert read: course frames of Physical Education, grades 3 to 5, 6 to 8 and 9 to 12 (2026-11-25)

Fresh expert read, cold, of the three after-core PE band frames written beside each other on 2026-11-25, on the
pattern of the fixed K to 2 pilot. Brief: docs/pipeline/briefs/frame-read.md with the after-core changes the caller
gave. Nothing but this report was edited.

## What I read

- AGENTS.md; docs/agents/EXPERT.md; the lens docs/agents/lenses/physical-education.md; the PE part (section 4) and the
  shared core of docs/ADOPTION-BAR-SUBJECTS.md; docs/courses/physical-education/STANDARD.md and APPROACH.md in full;
  docs/pipeline/briefs/frame-write.md, "After-core courses"; docs/courses/CALENDAR.md stagger rules.
- The K to 2 pilot read and fix report (docs/reviews/frame-physical-education-grades-k-to-2-2026-11-25.md and
  -fixes-2026-11-25.md), and the K to 2 frame's Units and Handed on tables.
- The three frames in full: docs/courses/physical-education-grades-3-to-5/frame.md,
  docs/courses/physical-education-grades-6-to-8/frame.md, docs/courses/physical-education-grades-9-to-12/frame.md.
- Rows: course-list.csv `rows` cells (`file:physical-education&grade:3|4|5`, `6|7|8`, `9|10|11|12`) select 48, 58 and
  48 rows of data/progressions/physical-education.csv; the gate places them.
- Beside them: the Units tables and PE tables of the health 3 to 5, 6 to 8 and 9 to 12 frames, the SEL 3 to 5 frame
  (landed 22:18, after PE 3 to 5 at 22:11), and the dance and music K to 2 frames for cultural picks; data/plans/
  calendar.csv through `frame.py calendar`.
- Gates. `python -X utf8 scripts/frame.py check <course>`: 3 to 5, 0 failures (unit days 74, 74, 74; 24 units, 240
  days); 6 to 8, 0 failures (90, 90, 90; 22 units, 288 days); 9 to 12, 0 failures (74 a year; 24 units, 320 days).
  `progression.py check physical-education`: 203 rows, 0 failures. `stale.py check`: 4 failures, 3 of them in PE 3 to
  5 (finding 3); the fourth is in the ELD 9 to 12 frame, another file being written, so not a finding here.

## Verdict

Grades 3 to 5: sound and the closest copy of the pilot; every row and all 57 span-5 indicators are placed, days and
check weeks add up, and the seams both ways match; it needs its cultural picks widened, its SEL links written now
that SEL 3 to 5 has landed, and a fifth-grade life jacket size. Grades 6 to 8: sound in rows, days, seams and health
links, but its short path is stated as "a third of the practice" when the arithmetic removes about two thirds, and
two of its three dance picks repeat earlier grades. Grades 9 to 12: sound in shape (required years own every
indicator, electives carry them, the grade 12 calendar is well thought through), but grade 9's S4 outcome has no
scored check, grade 10's unit 12 carries eleven indicators, and none of its cultural picks or facts was spot-checked.
The one change that matters most across all three: one subject-wide pass on cultural picks, because the Virginia
Reel is now taught in grades 3, 6 and 9, tinikling in grades 2 (dance), 4 and 6, and no PE grade from K to 12 uses an
activity from Africa.

## Findings, most serious first

### 1. Cultural picks repeat across bands, and Africa is absent from K to 12 PE (serious; 3 to 5, 6 to 8, 9 to 12)

- **What is wrong.** The three frames were written side by side and each picked without seeing the others:
  - The Virginia Reel is a pick in 3 to 5 unit 8 (grade 3), 6 to 8 unit 6 (grade 6) and 9 to 12 unit 5 (grade 9).
  - Tinikling is in dance K to 2 unit 9 (grade 2), PE 3 to 5 unit 16 (grade 4) and PE 6 to 8 unit 6 (grade 6). 3 to 5
    unit 16 says "Neither is used in K to 2", which is false for tinikling.
  - Range: PE K to 2 picks Denmark and the Netherlands, Mexico twice, Germany, Korea, the US; 3 to 5 the US, Romania,
    Quebec, China, the Philippines; 6 to 8 the Philippines, the US, Serbia, Afro-Brazil, Mongolia (read only); 9 to
    12 the US, Southeast Asia, England and Brazil. No activity from any African country in 13 grades (Ampe was
    dropped from K to 2 in its fix pass because SEL used it); Europe and the US carry most examples.
  - 6 to 8 says the Virginia Reel "was not checked"; 3 to 5 checked it the same day. 3 to 5 tells the safe tinikling
    origin story; 6 to 8 does not.
- **Why it matters.** Lesson 11 of the pilot (picks do not repeat another grade's) and bar C12 (fails when one group
  carries the examples). A student meets the same dance three times and no African game at all.
- **Fix (item-level, settled below; each candidate is from memory or one search, and the sensitivity agent confirms
  it at the community's own source before a unit names it).**
  - 3 to 5 unit 16: replace tinikling with Pilolo, a search-and-race game from Ghana, played in small groups with no
    one out (Wikipedia and a Georgia early learning activity page describe it; to confirm at a Ghanaian cultural
    source). Keep jianzi. Remove "poles" from the unit's hazards and from the Safety read list ("poles (unit 16)"),
    drop the $10 elastic bands, and change the cue "step in, step out" to Pilolo's rule card. Rewrite the claim to
    "Neither is used in PE, dance or SEL K to 2."
  - 6 to 8 unit 6: replace tinikling with a gumboot dance from South Africa (a stepping and slapping dance with roots
    among mine workers, taught here as a social and performance dance; from memory, to confirm at a South African
    heritage or arts institution), which keeps a percussive style and removes moving poles; replace the Virginia Reel
    with a partner dance from a region the subject lacks, candidate cumbia's basic step (Colombia) with teacher-set
    partners and no gender roles. Drop the PVC poles ($40) and the "dance-pole work" line from Required access; drop
    "Safety read (moving poles)".
  - 9 to 12 unit 5: replace the Virginia Reel with a social folk dance not used before, candidate bhangra basic steps
    (Punjab, a harvest and festival folk dance), with no gender roles and no costume.
  - Add one line to each frame's Sensitivity reads bullet: "Picks are checked against every PE, dance, music and SEL
    frame of K to 12 so none repeats."
- LAYER frame. REPEAT yes (pilot finding 5). Confidence: firm on the repeats and the gap (frames read); likely on the
  candidates.

### 2. The 6 to 8 shorter path removes about two thirds of practice, not a third (serious; 6 to 8)

- **What is wrong.** The Shorter path bullet drops 32 of 96 days, all Fluency or Application, "at most 5 in any unit
  (about a third of its Fluency and Application days, so a 7-day unit gives up at most 2)", and the course page is to
  say "a third of the practice goes". Grade 6 has 70 teaching days (90 less 20 check and respond days); with Fluency
  and Application each about a third, about 47 are practice days. Dropping 32 of 47 is about 68 percent. "At most 5"
  and "about a third" contradict each other in every unit over 9 days, and with each unit keeping one Fluency and one
  Application day, 32 is only just reachable (about 33 droppable in grade 6). For the lead 1 also reads APPROACH as
  needing Cory to allow another figure, but APPROACH "Pacing" says a band frame may change the defaults with its
  reason.
- **Why it matters.** Bar C2 (days must add up) and an honesty claim on the course page; a scope writer following
  "a third" cannot hit 32.
- **Fix.** Rewrite the bullet: "The 64-session path each year (a school that meets twice a week) drops 32 days. It
  drops first the begun-toward days whose owner unit teaches the skill in full a year later (unit 7's first serves,
  strokes and swings; unit 9's first tries at the grade 8 skills; unit 14's walk toward S1.8.1), then Fluency and
  Application days by practice load, leaving every unit at least one Fluency and one Application day; never a check,
  respond, baseline or first-teaching day. About two thirds of the practice days go, and the course page says so."
  For the lead 1: "APPROACH lets a band frame change the short path with its reason; a 72-session path is the
  frame's own call if the lead prefers it."
- LAYER frame. REPEAT yes (pilot finding 1, short path arithmetic). Confidence: firm (arithmetic).

### 3. Stale SEL notes and a wrong conflict-step citation in 3 to 5 (moderate; 3 to 5)

- **What is wrong.** `stale.py check` fails on lines 359, 361 and 362: SEL 3 to 5 has landed. Its units: four
  calm-down steps in unit 1 (grade 3, weeks 1 to 6), g3-rel-talk-listen and g3-rel-settle-disagreements in unit 4
  (grade 3, weeks 17 to 21), g4-rel-teamwork in unit 7 (grade 4, weeks 1 to 5), g4-sm-calm-down in unit 10 (weeks 16
  to 21), g4-rel-settle-disagreements in unit 11, g5-sm-calm-down in unit 13 (grade 5, weeks 1 to 5),
  g5-rel-settle-disagreements in unit 16. SEL's own PE table names g4-team-roles. Separately, PE unit 18's row says it
  "retrieves health grade 4 unit 12's short conflict steps"; health unit 12 holds limits, saying no and speaking up
  (g4-v-limits-and-respect, g4-t-saying-no, g4-v-speak-up-notice), not conflict steps. The year-before conflict steps
  are SEL grade 4 unit 11.
- **Why it matters.** The gate fails; PE units 11 and 18 retrieve from the wrong place, so a teacher reteaches what
  SEL taught weeks before, in other words.
- **Fix.** Replace the three Pending cells: calm row, "SEL unit 1 (grade 3 weeks 1 to 6), unit 10 (grade 4 weeks 16 to
  21), unit 13 (grade 5 weeks 1 to 5): SEL first in grades 3 and 5; PE units 6 and 24 open with SEL's card as
  retrieval; in grade 4 PE unit 11 (weeks 9 to 13) uses the grade 3 card"; talk row, "SEL unit 4 (grade 3 weeks 17 to
  21) beside PE unit 5 (weeks 19 to 22): PE uses SEL's talk turn card; SEL unit 7 (grade 4 weeks 1 to 5) teaches
  teamwork first, so PE unit 11 opens with SEL's working agreement as retrieval"; conflict row, "PE unit 18 retrieves
  SEL grade 4 unit 11's settle-disagreement steps; health unit 18 and SEL unit 16 come later in grade 5". Change unit
  18's What students learn to match.
- LAYER process (stale) and frame (citation). REPEAT yes (pilot finding 7). Confidence: firm (both frames read).

### 4. Grade 9's standard 4 outcome has no assessment (moderate; 9 to 12)

- **What is wrong.** Grade 9's S4 outcome is "samples many kinds of activity and logs what each gave" (begun toward
  S4.12.1 to S4.12.5, unit 6). Unit 6's Ends check the skill retest, the principles and a peer check; the log is "kept
  private, never scored". The year-end check reads the log "unscored". Nothing in grade 9 checks S4.
- **Why it matters.** Bar criterion 1: an outcome, content and an assessment for every standard in every grade. The
  pilot's fix rule (every standard sampled across a year's two checks) is met in words only.
- **Fix.** Unit 6 Ends adds to the knowledge task: "for two sampled activities, says what each gave (expression,
  company, health, interest or challenge) and one reason, marked met, partly or not yet on the reason, never on what
  was chosen." Grade 9 year-end: "two activities and what each gave (unit 6, S4), marked as in unit 6" in place of
  "read unscored".
- LAYER frame. REPEAT yes (pilot finding 4, S4 not checked). Confidence: likely (one bar line, a plain reading).

### 5. Life jackets sized for the wrong children (moderate; 3 to 5, 6 to 8)

- **What is wrong.** 3 to 5 unit 23 uses "K to 2's four" child life jackets for grade 5 fastening, at $0. Child
  jackets are sized for about 30 to 50 pounds, youth for about 50 to 90 (Safe Kids, West Marine sizing charts); most
  grade 5 students are youth size, and a fit check ("buckle, zip, check") on a jacket too small teaches the wrong
  check. 6 to 8 unit 21 buys "youth" jackets for grade 8, when many 13 and 14 year olds are past 90 pounds.
- **Why it matters.** Bar criterion 4 (safety content accurate); the cost lines understate.
- **Fix.** 3 to 5 unit 23 and Required access: "four youth life jackets sized to the class (borrowed or about $100);
  the fastening task includes the fit check: snug, does not ride up past the chin." Raise grade 5's cost to about
  $145 and the band to about $490 (For Cory). 6 to 8 unit 21: "youth and adult sizes to fit the students".
- LAYER frame. REPEAT new. Confidence: likely (two sizing sources; student weights from memory).

### 6. Grade 10 unit 12 carries eleven indicators (moderate; 9 to 12)

- **What is wrong.** Unit 12 (16 days, 13 teaching days with a draft, feedback and revision inside them) owns
  S2.12.5, S2.12.11 and all nine S4.12 codes, in two activity blocks and a planning workshop. S4.12.7 to S4.12.9
  (what affects staying active, managing emotion, what PE has meant) each get about a day; S4.12.9 is "ending in a
  short reflection".
- **Why it matters.** Lesson 4 (standards in full): the required-years promise is that every student meets every S4
  part taught and checked; at this density several are headline only.
- **Fix (judgment call).** Move the row g10-fitness-life (S2.12.5, S2.12.11, quality of life and early adulthood)
  into unit 8, whose plan already asks why fitness matters, with its retrieval on health unit 2; unit 8 keeps 15 days
  and the mid-year check may sample it. Unit 12 then holds only the S4 plan, and its Ends add one knowledge prompt
  each for S4.12.7 and S4.12.9 in the plan. Days stay as the check weeks fix them.
- LAYER frame. REPEAT new. Confidence: judgment call.

### 7. 9 to 12 picks and facts were not spot-checked (moderate; 9 to 12)

- **What is wrong.** For the lead 3: "No page was opened for this frame", and every pick and fact is listed as a
  browser check for the lead. AGENTS.md keeps "browser check" for pages that refuse automated reads after one other
  source was tried; the pilot pattern asks every pick to be spot-checked. Unit 9's facts (1896 revival and who could
  compete, the 1863 rules, sepak takraw) hold from memory but carry no source.
- **Fix.** Before the scope, the fixer spot-checks unit 5's replacement pick (finding 1), sepak takraw (a federation
  or national body page), the 1896 Games (the IOC's history pages) and the 1863 rules (the English FA history page),
  writes each source line with its date, and keeps "browser check" only for a page that refused.
- LAYER process. REPEAT yes (pilot finding 6, sources not opened). Confidence: firm.

### 8. Unit 15's held retest leaves its respond day nowhere (minor; 6 to 8)

- **What is wrong.** Unit 15 is "11 days in weeks 1 to 4 plus one held day" (the check, day 47), and also "1 respond
  day". The respond day cannot come before the check, and day 48 belongs to unit 18. The unit is also 12 days with one
  check day, against the bullet's "longer units with two".
- **Fix.** "Unit 15: 10 days in weeks 1 to 4 (course days 1 to 10), its check on day 47 and its respond day on day 48;
  unit 16 days 11 to 25, unit 17 days 26 to 38, unit 18 days 39 to 46." The Assessment bullet adds "except unit 15,
  whose one held check day is the retest". Unit 18's day line changes to match.
- LAYER frame. REPEAT new. Confidence: firm (count).

### 9. Unit 18's reason contradicts the mid-year check (minor; 6 to 8)

- Unit 18 says it sits "just before the mid-year check, so the leadership is the year's S3 owned code sampled there";
  the grade 8 mid-year check carries unit 18's record unscored, and the year-end check samples it. Fix: "...sampled at
  the year-end check (the mid-year check carries its record)".
- LAYER frame. REPEAT new. Confidence: firm.

### 10. Choice of a more or less competitive setting is not course-wide in 6 to 8 and 9 to 12 (minor)

- 3 to 5 Supports says every small-sided game offers a more and a less competitive court; 6 to 8 says "where the unit
  says so" (two units do); 9 to 12 says nothing. The lens and STANDARD.md 4 ("Competition") ask for it. Fix: both
  Supports bullets copy 3 to 5's line: "every small-sided game offers a more and a less competitive court the
  student chooses."
- LAYER frame. REPEAT new. Confidence: firm.

### 11. Cost lines: basis differs and 9 to 12 does not add (minor; all three)

- 3 to 5 counts costs on top of the K to 2 closet; 6 to 8 and 9 to 12 from nothing. 9 to 12's unit cells sum to $535
  (grade 9), $185 (grade 10), $0 and $20, about $740, not the stated $555, $205 and $780 (the gap looks like the
  optional $120 compasses partly counted). 6 to 8 has no For Cory line though grades 6 and 8 ($355, $365) and grade 9
  are over the $150 a year ceiling asked of Cory.
- Fix: each Supplies bullet states its basis in one line ("from nothing; a middle or high school building does not
  share the elementary closet"); 9 to 12 restates totals from its cells; 6 to 8 adds a For Cory money line, joined to
  the one question below.
- LAYER frame. REPEAT new. Confidence: firm (sums).

### 12. Loaded lifts: "none in this course" and "a trained spotter for any loaded lift" (minor; 9 to 12)

- Unit 2 says loaded and maximal lifts are out of the course; units 14 and 19 name a spotter "for any loaded lift".
  Fix: one course-wide line in Space, weather and equipment: "Curio Class plans use body weight and bands; a school
  that uses its weight room does so under its own trained staff and rules, with a spotter for any loaded lift." Units
  2, 14 and 19 point to it.
- LAYER frame. REPEAT new. Confidence: firm.

### 13. 9 to 12 short path is tight (nit)

- Sixteen days from six units at "at most 3" leaves almost every unit giving 3, including units 11 (7 days) and 21
  (8 days) and the product units, whose draft and revision days are protected. Fix: "at most 4 in a unit of 13 or more
  days, at most 1 in a unit of 8 or fewer"; the scope names the split.
- LAYER frame. REPEAT yes (short path). Confidence: likely.

## Seams across the four bands

- **K to 2 to 3 to 5.** Every K to 2 Handed on row is picked up in the unit 3 to 5 names; the three readiness rows
  (g1-heart-muscle, g1-world-games, g2-foods-energy, g2-water-skills) are counted right. Holds.
- **3 to 5 to 6 to 8.** Both tables agree row by row (g3-stay-safe-own, g4-object-ideas and g4-pulse-body to readiness
  in grade 6; g5-water-skills to unit 21; g4-world-activities to unit 22). Holds.
- **6 to 8 to 9 to 12.** Both tables agree, including the grade 7 rows read again in grade 9 or 10. Holds.
- **Dose and days.** 80 x 30, 80 x 35, 96 x 45, 80 x 45 a year, each from APPROACH and each stating the gap to the
  national minutes. Holds; the 6 to 8 short path is finding 2.
- **Check weeks.** 3 to 5 weeks 18 and 26, 6 to 8 week 17 and the finals week, 9 to 12 week 16 and week 32 (grade 12
  week 28). All off same-grade core check weeks in K to 8 (checked against `frame.py calendar`).
- **Equipment.** Findings 5 and 11.
- **Safety.** The pilot's guides (Nova Scotia, SPHEReS, CDC) are carried in all three; static stretch after warm-up,
  no inverted balances, soft balls and swing space throughout. Findings 5 and 12.
- **Health.** Every health unit cited in 3 to 5, 6 to 8 and 9 to 12 matches the health frames' units and rows
  (checked), except the conflict-step citation in finding 3. HECAT PA 3, 4 and 6 sit in PE 6 to 8 units 1, 2, 3, 14
  and 20 as Cory decided. Water: health 3 to 5 unit 3 and PE grade 3's one line are ordered right.
- **SEL.** 3 to 5: finding 3. 6 to 8 and 9 to 12: SEL frames unwritten, Pending markers correct.
- **Dance.** All three use Pending for the unwritten dance frames, correctly.

## Pilot fixes carried

| Pilot fix | 3 to 5 | 6 to 8 | 9 to 12 |
|---|---|---|---|
| Short path from the band's dose | Yes | Arithmetic wrong (2) | Yes, tight (13) |
| Health and SEL read first, retrieval in their words | Health yes; SEL stale (3) | Yes | Yes |
| Every standard sampled across a year's two checks | Yes | Yes | Grade 9 S4 in words only (4) |
| One skill, one knowledge, one S3 in every Ends | Yes | Yes | Yes |
| "Begun toward" only for a later owner | Yes | Yes | Yes |
| Picks spot-checked, no-one-out, no gender roles | Yes, but repeats (1) | Partly (1) | No (7) |
| Required access, no "costs nothing" | Yes (life jackets, 5) | Yes | Yes |
| Water break and shade; logic model | Yes | Yes | Yes |
| SPHEReS in place of Alberta | Yes | Yes | Yes |
| One-day check load rule | Yes | Yes | Yes |

## Lens checklist (course frame layer)

| Lens line | 3 to 5 | 6 to 8 | 9 to 12 |
|---|---|---|---|
| Outcomes stated, not a year of games | Met | Met | Met |
| Every grade has an outcome for all four standards | Met | Met | Met in words; grade 9 S4 unchecked (4) |
| Every span indicator placed | Met (57) | Met (61) | Met (43, all in grades 9 and 10) |
| Skills in developmental order | Met (grade 4 starts kept from the tool) | Met | Met |
| Dance and fitness return | Met (units 8, 15, 22; 4, 9, 17) | Met | Met |
| Most moving, no lines | Met | Met | Met |
| Safe place, no elimination, targets, public picks | Met | Met | Met |
| Choice of competitive setting | Met | Part (10) | Missed (10) |
| Every body included, no gender split | Met | Met | Met |
| Fitness learned, not judged | Met | Met | Met |
| Growth against own baseline | Met | Met | Met |
| Real space, wet day, low equipment, heat | Met | Met | Met |
| PE and health both or neither | Met | Met | Met |
| PE dance and dance course same year | Not yet (dance unwritten) | Not yet | Not yet |
| Cultural range, no repeats (C12) | Missed (1) | Missed (1) | Missed (1) |

## Calendar clashes among after-core courses (for the lead's calendar pass, not findings)

From `frame.py calendar`:
- Grade 3 week 18: PE, visual arts. Grade 3 week 26: PE, SEL, visual arts.
- Grade 4 week 26: PE, SEL.
- Grade 5 week 18: PE, visual arts. Grade 5 week 26: PE, SEL, visual arts.
- Grade 6 school day 82: PE, ELD. Grades 6, 7 and 8 school day 84: PE, health (a stagger rule 3 break; PE For the
  lead 6 names it).
- High school week 16 (no rule outside finals weeks): grade 9 with biology and health; grade 11 with ELA 11; grade 12
  with ELD. Not breaks under rule 4, listed for the lead.

## What is right and should not be touched

- The band shape: Year column, units numbered through the band, each year whole with 74, 90 or 74 unit days and 6
  check and respond days, the check weeks off every same-grade core week.
- Grade outcomes per standard per year, each naming its indicators and units.
- 3 to 5's readiness checks placed on exact days, and its keeping of the tool's grade 4 starts.
- 6 to 8's health physical activity outcomes taught in PE and named both ways; its puberty line.
- 9 to 12's required-and-elective design (every indicator owned in grades 9 and 10, electives in new settings, the
  fallback for a student who skips grade 11) and the grade 12 week 28 year-end check with unit 24's short form.
- Every frame's seams tables: they agree with each other row for row.

## What I could not judge

- Whether the candidate picks (Pilolo, gumboot, cumbia, bhangra) are open to be taught: the sensitivity agent's read
  at source.
- The dance seams in all three bands: the dance 3 to 5, 6 to 8 and 9 to 12 frames are unwritten.
- Average student weights by grade (finding 5) rest on memory.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| 3 to 5 unit 16: Pilolo (Ghana) replaces tinikling; poles and elastic bands dropped | Tinikling is in dance K to 2 and PE 6 to 8; no African pick in PE | 3 to 5 frame, unit 16, Safety read |
| 6 to 8 unit 6: gumboot dance (South Africa) replaces tinikling; cumbia basic step (Colombia) replaces the Virginia Reel; PVC poles dropped | Repeats of grades 2, 3 and 4; widens range | 6 to 8 frame, unit 6, Required access |
| 9 to 12 unit 5: bhangra basic steps replace the Virginia Reel | Third use of the Virginia Reel | 9 to 12 frame, unit 5 |
| 6 to 8 short path drops begun-toward days first | Their owner unit teaches the skill in full a year later | 6 to 8 frame, Shorter path |
| 6 to 8 unit 15: days 1 to 10, check 47, respond 48; units 16 to 18 shift | The respond day had no place | 6 to 8 frame, units 15 to 18 |
| 9 to 12: g10-fitness-life moves from unit 12 to unit 8 (precedent: the K to 2 pilot's k-class-chances move) | Unit 12 carries eleven indicators | 9 to 12 frame, units 8 and 12 |
| Youth life jackets for grade 5, youth and adult for grade 8 | Child sizes do not fit grade 5 | 3 to 5 unit 23; 6 to 8 unit 21 |

## For Cory

- Money: with life jackets sized right, the bands' provisional new buys are about $490 (3 to 5, on top of the K to 2
  closet), $785 (6 to 8, from nothing) and $740 (9 to 12, from nothing). Grades 3, 6, 8 and 9 exceed the $150 a year
  PE ceiling already asked of you in the K to 2 fix report. Is the ceiling per year, per band, or per building?

## Sources

- Pilolo: https://en.wikipedia.org/wiki/Pilolo and https://gelds.decal.ga.gov/Activity/Detail/2520 : a Ghanaian
  search-and-race game; rules vary by source.
- Life jacket sizes: https://www.safekids.org/node/33589 and
  https://www.westmarine.com/safety-gear-hub/life-jacket-sizing-charts.html : child about 30 to 50 pounds, youth about
  50 to 90.
- From memory, not opened: gumboot dance origins, cumbia, bhangra, the 1896 Games and the 1863 rules.

## For the source list

- The Georgia early learning activity page on Pilolo (gelds.decal.ga.gov), free, a classroom description to check
  against a Ghanaian source.

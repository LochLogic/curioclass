# Physical education pre-work: second-model cold read, 2026-11-20

> Filed by the lead 2026-11-20. Gemini 4 Neon (medium effort) in Antigravity, pasted by Cory from S:/CurioClass-gemini/ (prompt 10 to 18 for this subject), after it passed calibration (docs/reviews/calibration-*-gemini-2026-11-20.md). Its saved report is S:/CurioClass-gemini/reports/prework-physical-education-read.md; text unchanged here except wording the repository checks flag.

Read as the curriculum expert (docs/agents/EXPERT.md) with the physical education lens (docs/agents/lenses/physical-education.md). I did not write these drafts. Nothing in S:\CurioClass was edited; this report is saved outside the repository as instructed. Confidence is Firm, Likely or Judgment call on each finding. Outside sources were checked via web search and are linked under Sources; anything resting on memory is marked "from memory". The earlier cold read (docs/reviews/prework-physical-education-read-2026-11-19.md) was not opened until all findings below were written; see "Against the first read" at the end.

## What I read

AGENTS.md; docs/agents/EXPERT.md; docs/agents/lenses/physical-education.md; docs/FOUNDATION.md; docs/COURSE-RUN.md; docs/APPROACH.md; docs/courses/UNIT-PLAN.md; docs/ADOPTION-BAR-SUBJECTS.md (pass rule, C1 to C16, part 4 physical education, the PE row of "Before a scope and sequence", sources table); docs/courses/physical-education/STANDARD.md and APPROACH.md; docs/standards-notes/pe-2014-to-2024.md; docs/reviews/physical-education-open-material-2026-11-16.md; docs/pipeline/briefs/sensitivity-read.md; data/standards/shape-pe-2024.txt (full); data/progressions/physical-education.csv (full); docs/courses/health/APPROACH.md and docs/courses/sel/APPROACH.md (finished examples, for comparison); docs/reviews/prework-sel-read-2026-11-19.md (report shape). Targeted reads only: scripts/progression.py lines 45 to 130 (STD_FILES, ANCHOR, SPAN, code_grades); scripts/standards.py lines 1 to 142; data/courses.csv lines 1 to 50 (PE row 34 and comparison rows); data/subjects.csv; targeted ranges in data/progressions/social-studies.csv (lines 75 to 142, 181 to 228) and data/progressions/science.csv (lines 75 to 142) to verify cross-subject lean ids and grade timing. Opened only after findings were written: docs/reviews/prework-physical-education-read-2026-11-19.md.

## Verdict

The SHAPE America 2024 indicator list is sound (all 210 ids are real, unique, contiguous, verified at the span boundaries against SHAPE America's published pages, and all 210 are owned once in data/progressions/physical-education.csv), and the appropriate-practice rules are well grounded. The biggest risk is that APPROACH.md was marked approved while still missing half of UNIT-PLAN.md's unit and section fields (notably unit field 7, leaving default hands-up self-marking unoverridden for a teacher-judged doing subject), a dedicated Sensitive ground section with sensitivity-read routing, and explicit default doses per band; meanwhile, the 2026-11-20 high school edit packed all nine SHAPE.S4.12 indicators into one grade 10 "short form" row that drops parts of five of them. The one change that matters most is completing APPROACH.md field by field against UNIT-PLAN.md with a full Sensitive ground section and default doses (findings 1, 3 and 4), and splitting grade 10's S4.12 row so every owned indicator is taught and assessed in full (finding 2).

## What I counted

| Check | Result |
|---|---|
| Ids in data/standards/shape-pe-2024.txt | 210, unique, contiguous in all 16 standard-by-span groups: S1 17/22/20/9 (68), S2 12/18/22/17 (69), S3 10/7/10/8 (35), S4 10/10/9/9 (38). Matches header line 5 and STANDARD.md line 22 |
| Live web check of SHAPE 2024 boundary codes | All 16 end-of-span codes (1.2.17, 1.5.22, 1.8.20, 1.12.9; 2.2.12, 2.5.18, 2.8.22, 2.12.17; 3.2.10, 3.5.7, 3.8.10, 3.12.8; 4.2.10, 4.5.10, 4.8.9, 4.12.9) confirmed on shapeamerica.org |
| Own-words check on shape-pe-2024.txt | All 210 indicator lines are in Curio Class's own words (no long copied runs). Header line 7 copies the four official 2024 standard statements verbatim (finding 8) |
| Validator (scripts/standards.py) | Line 109 checks `SHAPE\.S[1-4](?:\.(?:2|5|8|12)\.\d{1,2})?`; does not check that the number exists (matches STANDARD.md line 28) |
| Progression gate (scripts/progression.py) | `physical-education` is in STD_FILES (line 57), ANCHOR (line 69) and code_grades (lines 93 to 101). Span 12 still allows grades 11 and 12 as owners (finding 5) |
| Ownership in data/progressions/physical-education.csv | 203 data rows (lines 2 to 204); all 210 indicators owned by exactly one grade: K-2 (17/12/10/10), 3-5 (22/18/7/10), 6-8 (20/22/10/9), 9-12 (9/17/8/9, all owned in grades 9 and 10; grades 11 and 12 carry `~` only) |
| Cross-subject leans in physical-education.csv | 11 entries across 10 rows (science: 4-LS1-1, MS-LS1-3, MS-LS1-7, MS-PS2-2; math: 5.G.A.2, 6.RP.A.3, 6.SP.B.4; social-studies: ss4-regional-cultures, ss6-complex-societies). All 9 distinct ids exist in core standards or progressions |
| data/courses.csv | 1 row: line 34 (`pe,health-pe,Physical Education,k-12,,y,`), empty notes. Mismatches STANDARD.md ("four courses, one per band") and ADOPTION-BAR-SUBJECTS.md ("Physical education (4)") |
| APPROACH.md against UNIT-PLAN.md (10 unit + 11 section fields) | Unit fields: 2 filled/part, 3 misplaced/partial (5, 8, 9, 10), 5 missing (1, 3, 4, 6, 7). Section fields: 4 filled/part (1, 3, 5, 8, 9), 1 unnumbered/merged (10), 5 missing (2, 4, 6, 7, 11) |

## Findings, most serious first

### 1. APPROACH.md omits half of UNIT-PLAN.md's fields and misplaces three, leaving hands-up self-marking unoverridden

- **Where:** docs/courses/physical-education/APPROACH.md (whole file); docs/courses/UNIT-PLAN.md ("The unit plan: fields, in order" and "The section plan: fields, in order"); docs/courses/health/APPROACH.md and docs/courses/sel/APPROACH.md (finished examples).
- **What is wrong:** Field-by-field placement against UNIT-PLAN.md shows ten missing slots and three misplaced or merged ones:

| UNIT-PLAN.md slot | Status in PE APPROACH.md | Fault |
|---|---|---|
| Unit 1 Header | Missing | Not named (sessions by kind, sessions a week and minutes) |
| Unit 2 Standards, limits, carried | Part / mixed | Puts "Safe space" here (belongs in unit field 8, as science does) and mentions supplies/low-equipment here; omits limits/boundaries and unit-level carried cue-card withdrawal rule |
| Unit 3 Where it sits | Missing | No builds-on, handoff strength, leads-to, comes-back or cross-subject links (Health, Dance, Science, Math, SEL, Social Studies) |
| Unit 4 Readiness check | Missing | Baseline watch is on the unit's own skill, not a readiness check or retrieval task on assumed earlier-grade rows (`Given:`, `Retrieval only:`, `Start-of-year check:`) |
| Unit 5 End-of-unit assessment | Unnumbered / part | Split across "Kinds of day: Check" and "The daily evidence"; omits look-fors and two sample descriptions (meets / does not meet) for teacher-judged tasks, and accommodations line |
| Unit 6 Error register | Missing | No PE error-register rule (e.g., stepping with the same foot on an overhand throw, slapping instead of pushing on a dribble) |
| Unit 7 Response allocation | Missing (critical) | UNIT-PLAN.md line 201 defaults to "Students mark the short items against the key on the screen... Hands up by item sets the groups" unless the subject page changes it. PE skill tasks and conduct are teacher-judged and fitness records are private; hands-up self-marking violates the PE lens and bar criterion 7 |
| Unit 8 Tools and supplies | Split / unnumbered | Supplies mentioned under unit field 2; tool rules sit under an unnumbered heading; safe space sits under unit field 2; C14 room/equipment sits at the bottom |
| Unit 9 Family note | Wrong place | Buried at the last sentence of "Evidence and sources (C13, C16)" (line 122) and in "Pacing" (line 94), with no unit field 9 heading |
| Unit 10 Sources and still to make | Unnumbered / stale | Under "Evidence and sources (C13, C16)" without field 10; line 121 still says only PECAT K to 5 overview and standard 1 tables were read |
| Section 1 Standards and practices | Part | Names SHAPE ids and cues; omits adult-level teacher background and sensitive-ground teacher notes |
| Section 2 Where it sits | Missing | Not named |
| Section 3 Checks, written first | Part | Names the teacher's mark in line 54, but mixes unit-level baseline, conduct and fitness into the same section and omits unit assessment items owned |
| Section 4 Expected errors | Missing | No wrong-form beside right-form example, day shown, or 5 to 10 minute response if many made it |
| Section 5 What is carried, instruments | Part | Names cue card withdrawal and low-equipment/wet-weather swap; omits key moments with ideal instrument and spec verdict (UNIT-PLAN rule 10) |
| Section 6 Days | Missing | Lesson shape (instant activity, warm-up, focus, cool-down, closure; 50 percent MVPA) sits under "Kinds of day" instead of section field 6; no cap on opening talk minutes |
| Section 7 Talk and writing | Missing | No planned questions (such as the tactics question) or short written/spoken tasks (grades 3 to 12 exit tickets, goal plans) |
| Section 8 Practice that returns | Filled | Labelled "(field 8)"; clarify "section field 8" |
| Section 9 Supports and extension | Part | Strong on disabilities, injury, EL, reading load, extension; omits **check accommodations** (read aloud, oral answer, scribe, adapted movement check) required by UNIT-PLAN section field 9 |
| Section 10 Two rooms | Wrong place / unnumbered | Merged into "## An ordinary room, and two rooms (C14)" (lines 109 to 115) with no field number, mixing unit field 8 supplies with section field 10 (one child at home; one projector) |
| Section 11 Not in this section | Missing | Not named (needed to send nutrition/planning to Health, dance technique to Dance, in-water aquatics and adapted PE to the school) |

- **Cost:** A unit writer following UNIT-PLAN.md will put hands-up self-marking in unit field 7, put safe space in unit field 2 instead of unit field 8, drop readiness checks (unit field 4), drop check accommodations (section field 9) and omit section fields 2, 4, 6, 7 and 11. C7, C8, C9, C10 and C14 are all exposed.
- **Fix (add a complete field-map block to docs/courses/physical-education/APPROACH.md, matching docs/courses/sel/APPROACH.md, and move Safe space to unit field 8, Family note to unit field 9, and Two rooms to section field 10; ours, untested):**

> ## What PE adds to the unit and section plan fields
>
> - **Unit field 1 (Header):** sessions by kind; sessions a week and minutes, as the frame states them.
> - **Unit field 2 (Standards, limits, and what is carried):** the SHAPE indicator ids in our own words (data/standards/shape-pe-2024.txt, never quoting publisher wording), the grade outcome per standard (STANDARD.md section 3), the skill theme and its two or three cues, the setting progression (alone, changing conditions, small-sided game or routine), the limits and boundaries (for example in-place only, no inversions, no max lifts), and what is carried (the cue card and the day it is withdrawn).
> - **Unit field 3 (Where it sits):** builds on (earlier-grade PE rows, handoff strong or weak), leads to, comes back, and any cross-subject link (Health, Dance, Science, Math, SEL, Social Studies) by row id or standard code.
> - **Unit field 4 (Readiness check, whole):** for any assumed row last used two or more grades back, a short movement or concept readiness check given at the end of the previous unit (or day 1 in unit 1); for rows used the year before or earlier the same year, an opening retrieval task in the warm-up (`Retrieval only:`). Separate from the unit's own day-1 baseline watch.
> - **Unit field 5 (End-of-unit assessment, whole):** a skill task (the main cue repeated from the day-1 baseline watch), a knowledge task on movement or fitness concepts, and conduct marked once in the unit against stated S3 behaviors. Every teacher-judged item lists look-fors and two sample descriptions (meets and does not meet), plus an accommodations line. Scored work is never taken from the first day a skill is taught.
> - **Unit field 6 (Error register):** common movement and concept errors lettered once for the unit (for example stepping with the same foot on an overhand throw, slapping instead of pushing on a dribble, confusing dynamic and static stretching), each with what it shows and its source or "from memory".
> - **Unit field 7 (Response allocation):** PE skill tasks and conduct are teacher-judged against look-fors, and fitness records are private, so nothing is marked by hands up. Groups for the Respond day come from the class record sheet's "not yet" cells by cue or concept, capped at four groups; other students work on an extension task in pairs from a task card. Marking time is stated honestly in minutes.
> - **Unit field 8 (Tools and supplies across the unit):** tools with day, mark, job, verdict and link to TOOL-ASKS.md; supplies for an ordinary room (clear space, soft balls or rolled socks, rope or string, tape or chalk; low-equipment and wet-weather versions); and **Safe space** (clear-space size, one throwing direction, surface rule for hard floor or wet grass, water break in warm weather, pre-lesson equipment check; safety facts sourced or marked "from memory").
> - **Unit field 9 (Family note):** one per unit, in English and Spanish, written when the unit is finished: the skill cues, short active breaks and one home activity with no equipment to buy, plus any opt-out or safety note.
> - **Unit field 10 (Sources and what is still to make):** sources with read status, what is from memory, no claim of effect on fitness or health, and a line pointing to the course-level logic model (C16).
> - **Section field 1 (Standards and practices):** SHAPE indicator ids in our own words, cue cards in place of math's practices, what the teacher page must explain at adult level, and any sensitive-ground teacher note.
> - **Section field 2 (Where it sits):** what comes just before and after in the unit, which readiness items it uses, and where its results go.
> - **Section field 3 (Checks, written first):** unit assessment items owned, plus the day's closure evidence (the teacher's met / partly / not yet mark on one cue for a rotating group, a private self-check, or a one-line exit ticket in grades 3 to 12).
> - **Section field 4 (Expected errors and first ideas):** each error letter this section meets, shown as a wrong form beside a right form (teacher demonstrated safely, never singling out a student), the day shown, and the 5 to 10 minute repair if many made it.
> - **Section field 5 (What is carried, and instruments):** the cue card, who holds the model each day, the day the cue card is withdrawn, key moments with ideal instrument and spec verdict, and what a room with nothing (low-equipment and wet-weather) does.
> - **Section field 6 (Days):** every day follows the lesson shape (instant activity, warm-up, focus, cool-down, closure) with at least half of the lesson in moderate to vigorous activity and opening talk kept to two to three minutes. Any new skill is taught and tried with the teacher watching before game play.
> - **Section field 7 (Talk and writing):** two or three planned questions (such as the tactics question or a cue check) with their days, plus any short written or spoken task (grades 3 to 12 exit tickets, goal plans) and its look-fors.
> - **Section field 8 (Practice that returns):** earlier skills returning in new settings and fitness concepts returning in warm-ups and cool-downs.
> - **Section field 9 (Supports and extension):** disabilities, short-term injury and medical guidance, English learners, reading load, **check accommodations** (read aloud, oral answer, scribe, adapted movement check), extension on the same standard, private grouping, no punishment/elimination/human targets.
> - **Section field 10 (Two rooms):** one child at home (parent, sibling, wall, target, or own count against yesterday; no team game needed); one projector or none (every day runs from printed cue cards; a screen only shows a skill picture).
> - **Section field 11 (Not in this section, and still to make):** what belongs to Health, Dance, or the school's aquatics, medical or adapted PE specialists, and what is still to make.

- **Confidence:** Firm.

### 2. High school row `g10-choose-active-apply` packs all nine SHAPE.S4.12 indicators into one "short form" row and drops parts of five of them

- **Where:** data/progressions/physical-education.csv line 184 (`g10-choose-active-apply`) and line 170 (`g9-choose-active`); docs/courses/physical-education/STANDARD.md section 3 rule 5 (lines 72 to 76); data/standards/shape-pe-2024.txt lines 212 to 220; UNIT-PLAN.md rule 19 ("Always cover the whole standard").
- **What is wrong:** After Cory's 2026-11-20 decision to make grades 9 and 10 the two required years and grades 11 and 12 electives, all nine `SHAPE.S4.12.1` to `SHAPE.S4.12.9` indicators were moved into one grade 10 row (`g10-choose-active-apply`), described as "The personal plan in short form". Checking each of the nine statements in `data/standards/shape-pe-2024.txt` against row 184's notes and words shows five indicators are only partly met or missed:
  1. `SHAPE.S4.12.1` ("Choose and join activities, such as dance, yoga or aerobics, that let you express yourself"): **self-expression is omitted** from row 184 ("how it fits health, interests, company and challenge").
  2. `SHAPE.S4.12.6` ("Create and build movement goals tied to your interests"): **creating and building movement goals** is omitted (only "a one-page plan to stay active after school" is named).
  3. `SHAPE.S4.12.7` ("Study what affects staying active after high school, such as life choices, money, motivation and access"): **studying those factors** (life choices, money, motivation, access) is omitted.
  4. `SHAPE.S4.12.8` ("Examine and use chosen ways to manage emotions during activity"): row 184 says only "how it handled emotions" and assesses only by a knowledge task (log and plan), not *using* chosen ways during activity; it also drops the mental-health boundary note ("PE does not treat mental health conditions; the counselor is named") that `g12-manage-emotions` (line 203) carries.
  5. `SHAPE.S4.12.9` ("Think over PE experiences to understand what they mean to you"): **reflecting on PE experiences to understand what they mean** is omitted from row 184.
  In addition, `g9-choose-active` (line 170) still has the stale note: `"Works toward the choosing indicators owned in grade 11."`
- **Cost:** C1 (door criterion: every standard taught in full at the depth its wording asks) and UNIT-PLAN rule 19 fail for high school PE. A student who takes only the two required years never meets five of the nine S4.12 indicators in full.
- **Fix (requires Cory's yes because it moves ownership between grade 9 and grade 10; see Questions for Cory 3):** Split S4.12 across grades 9 and 10 so every part is taught and assessed in full inside the two required years, and update STANDARD.md section 3 rule 5 to match:
  - In **grade 9**, update `g9-choose-active` (line 170) to **own** `SHAPE.S4.12.1; SHAPE.S4.12.2; SHAPE.S4.12.3; SHAPE.S4.12.4; SHAPE.S4.12.5` (it already samples dance, yoga, aerobics, sports and outdoor activities for expression, company, health, interests and challenge level): change its `standard` column from `~` to owned, remove `"Works toward the choosing indicators owned in grade 11."`, and add a conduct/participation check alongside the private activity log.
  - In **grade 10**, split `g10-choose-active-apply` (line 184) into two rows owning `SHAPE.S4.12.6; SHAPE.S4.12.7` (movement goals tied to interests + studying life choices, money, motivation and access after high school, assessed by a goal plan and a barrier analysis) and `SHAPE.S4.12.8; SHAPE.S4.12.9` (examining and using chosen ways to manage emotions during activity, assessed by a knowledge task and conduct, with the teacher note `"PE does not treat mental health conditions; the counselor is named."`, plus reflecting on PE experiences to understand what they mean, assessed by a short reflection).
  - In **STANDARD.md section 3 rule 5**, replace `"grade 10 carries the choice and personal plan indicators (S4) in short form, so every student meets them"` with: `"grade 9 owns the activity-choice indicators (S4.12.1 to S4.12.5) and grade 10 owns the goals, post-high-school factors, emotion-management and reflection indicators (S4.12.6 to S4.12.9), each taught and assessed in full."`
- **Confidence:** Firm.

### 3. Sensitive ground is not consolidated, Cory's sacred-dance rule is missing from STANDARD.md, APPROACH.md and nine progression rows, and no sensitivity-read or reporting route is named

- **Where:** docs/courses/physical-education/STANDARD.md; docs/courses/physical-education/APPROACH.md; data/progressions/physical-education.csv lines 23, 31, 41, 57, 71, 82, 99, 135, 153, 163, 179, 181, 184, 200, 203; docs/pipeline/briefs/sensitivity-read.md; docs/ADOPTION-BAR-SUBJECTS.md C12 and "Acceptability is local".
- **What is wrong:** Stage 1 requires sensitive ground to be named with what needs a sensitivity read, and every place that touches sensitive ground to carry its teacher note, leave-out and reporting route. Five specific gaps exist:
  1. **No "Sensitive ground" section** exists in `STANDARD.md` or `APPROACH.md`, and neither file points to `docs/pipeline/briefs/sensitivity-read.md` (neither the `sensitivity` read for cultural/disability content nor the `safety` read for physical-activity hazards).
  2. **Cory's 2026-11-20 sacred-dance rule is missing from both prose docs and 9 of 11 cultural rows.** `ADOPTION-BAR-SUBJECTS.md` line 565 says `"Cory's calls applied 2026-11-20 (two required years plus two electives, water safety, sacred dances)"`, but the sacred-dance rule appears only in `physical-education.csv` lines 31 (`g1-world-games`) and 99 (`g6-dance-sequences`). It is absent from `STANDARD.md`, absent from `APPROACH.md`, and absent from nine other cultural dance/game rows in `physical-education.csv`: `g1-dance-moves` (line 23), `g2-dance-sequence` (line 41), `g3-dance-steps` (line 57), `g4-dance-sequence` (line 71), `g4-world-activities` (line 82), `g8-culture-matters` (line 153, which even lists `ritual` in its `words` column with no teacher note), `g9-dance-forms` (line 163), `g10-games-culture` (line 179), and `g12-community` (line 200).
  3. **Body size, weight, nutrition and supplement boundaries are in progression rows but missing from APPROACH.md.** Progression rows rightly forbid weighing, body measurements, calorie counting and diet talk (`g2-foods-energy`, `g3-health-fitness`, `g5-food-drink`, `g7-eat-move-well`, `g10-food`, `g12-active-adult`), and `g10-food` (line 181) adds "the limits of supplements and drinks" (which needs a no-medical-advice note). None of these rules appear in `APPROACH.md`.
  4. **Mental-health boundary and disclosure reporting route are missing from APPROACH.md and from four of five emotion-management rows.** Only `g12-manage-emotions` (line 203) says `"PE does not treat mental health conditions; the counselor is named."` Neither `APPROACH.md` nor `g1-calm-steps` (line 34), `g3-calm` (line 67), `g7-manage-feelings` (line 135) or `g10-choose-active-apply` (line 184) states this boundary or gives the teacher a reporting route if a student discloses abuse, self-harm, an eating disorder or an unsafe home situation (compare health `APPROACH.md` lines 103 to 106 and SEL `APPROACH.md` line 73).
  5. **No leave-out rule** is stated in `STANDARD.md` or `APPROACH.md` (unlike `ADOPTION-BAR-SUBJECTS.md` line 91, which says each course page states what a school may leave out), and `APPROACH.md` omits `STANDARD.md`'s gender-neutral grouping/language rule and medical-condition notes (asthma, heart, neck/back, latex/food allergies).
- **Cost:** A unit writer working from `APPROACH.md` and `STANDARD.md` can plan a ceremonial dance as a warm-up, include body-composition measurements, or miss the reporting route and sensitivity read, failing C12 and FOUNDATION promise 7.
- **Fix (add a "## Sensitive ground" section to docs/courses/physical-education/APPROACH.md, mirror the sacred-dance and leave-out rules in STANDARD.md section 4/5, and add the missing teacher notes to the nine cultural rows and four emotion rows in data/progressions/physical-education.csv; ours, untested):**

> ## Sensitive ground
>
> Units touching any topic below carry a teacher note in section field 1 and get a fresh-agent read (docs/pipeline/briefs/sensitivity-read.md) before going live:
>
> - **Cultural dances and games (sensitivity read):** every cultural claim is checked against a source before a unit names it. A sacred or ceremonial dance or game is never used as a game or a warm-up; a unit uses an activity only when its source says it is open to be taught (Cory, 2026-11-20).
> - **Bodies, weight, food and fitness records (sensitivity read):** no weighing, no body-composition measurements, no calorie counting and no diet talk; body composition is not taught as a body measure. Fitness results and heart-rate counts are private and never posted, ranked or graded. Food and hydration lessons give no medical or supplement advice.
> - **Disabilities, medical conditions and injury (sensitivity read):** adaptations keep the grade goal without singling out a student. Medical restrictions (asthma, heart or breathing conditions, neck or back concerns, latex or food allergies, injuries) follow the family's and school nurse's guidance; rest with a seated role is always allowed.
> - **Gender and grouping:** no activities split by gender, gender-neutral language throughout, and groups made privately by the teacher.
> - **Emotions and disclosure:** PE teaches simple calming steps during activity; it does not treat mental health conditions, and the school counselor is named. If a student discloses abuse, self-harm, an eating disorder or an unsafe home situation, the teacher note states: listen, do not promise to keep it secret, follow the school's duty to report, and tell the student who the next adult is (at home, name the national child abuse hotline and 988 by purpose).
> - **Water safety and physical hazards (safety read):** dry-land safety and skill tasks only in Curio Class; no child is made to enter water, and in-water tasks belong to the school's aquatics program with a qualified lifeguard (Cory, 2026-11-20). Units with striking tools, mats, climbing, resistance training or outdoor trips get a safety read.
> - **What a school or family may leave out:** in-water tasks, specific outdoor activities that do not fit local setting or policy, or any cultural dance or game a school swaps for an open alternative; a student excused from a movement task for medical or religious reasons receives an alternative role. If a school leaves out all units for an indicator, the course page does not claim that indicator.

- **Confidence:** Firm.

### 4. Dose by band is not stated as single numbers for any band

- **Where:** docs/courses/physical-education/APPROACH.md ("Pacing", lines 87 to 94); docs/ADOPTION-BAR-SUBJECTS.md C2 ("days per unit, minutes per lesson, a shorter path"); docs/courses/health/APPROACH.md lines 122 to 130 (for comparison).
- **What is wrong:** `APPROACH.md` rightly cites SHAPE America's weekly guidelines (150 minutes a week in elementary, 225 in middle and high school, confirmed via web search) and openly states that Curio Class's elementary plan is below that figure. However, it gives **no single session count or session length for any band**:
  - K to 5 says only `"about 2 to 3 sessions a week"` (a range, with no minutes per session and no sessions a year).
  - Grades 6 to 8 give no default at all (`"each band frame states its sessions a year and their length"`).
  - Grades 9 to 12 give no default at all, nor how the two required years and two elective years translate into sessions a year.
  - No short path is stated for any band.
  - `APPROACH.md` also requires at least half of each lesson in moderate to vigorous activity inside a five-part lesson shape (instant activity, warm-up, focus, cool-down, closure) without stating a minimum session length that makes that feasible.
- **Cost:** Stage 3 frame writers have no default year size, minutes per lesson or short path to build against, and C2 cannot be checked.
- **Fix (replace the first two sentences of "## Pacing" in docs/courses/physical-education/APPROACH.md; pending Cory's confirmation, see Questions for Cory 2; ours, untested):**

> Settled 2026-11-16 (Cory, Desk card q-later-arts-health-pe): elementary PE (K to 5) is about 2 to 3 sessions a week. Default time, ours and untested (each frame may change these with a reason, and states a short path): K to 2, 80 sessions a year of 30 minutes (about 2.5 a week, 75 minutes a week; short path 64 sessions); grades 3 to 5, 80 sessions a year of 35 minutes (about 88 minutes a week; short path 64 sessions); grades 6 to 8, 96 sessions a year of 45 minutes (3 a week, 135 minutes a week; short path 64 sessions); grades 9 to 12, 80 sessions a year of 45 minutes for each of the two required years (grades 9 and 10) and each elective year (grades 11 and 12; one daily semester or 2 to 3 sessions a week all year; short path 60 sessions). Sessions shorter than 30 minutes cannot hold all five lesson parts with half the time in moderate to vigorous activity.

- **Confidence:** Firm that defaults are missing; exact numbers are a Judgment call for Cory.

### 5. Ownership rule contradiction in STANDARD.md section 3 and gate gap in `scripts/progression.py`

- **Where:** docs/courses/physical-education/STANDARD.md lines 63 to 69 and lines 85 to 88; scripts/progression.py lines 74 and 93 to 101; data/progressions/physical-education.csv lines 32, 38, 42, 44.
- **What is wrong:** Three mismatches between the written rules, the gate and the progression rows:
  1. **Direct contradiction in STANDARD.md lines 85 to 88:** `"every outcome is expected in every grade, except these, which start in grade 3: alignment and muscular tension, and strategies and tactics (older S2); warming up and cooling down, and assessment and program planning (older S3); social interaction (older S5). The K to 2 progression rows carry these as ~CODE at most."` That last sentence is impossible for K to 2 span indicators (`.2.`): `SHAPE.S2.2.2` (chasing/fleeing tactics), `SHAPE.S2.2.7` (stretching before/after exercise) and `SHAPE.S4.2.2` (activities with others) MUST be owned in K, 1 or 2 under rule 1 and `scripts/progression.py`, and ARE owned in `g2-chase-flee`, `g2-stretch-why` and `g1-together-favorites`.
  2. **Soft contradiction in STANDARD.md line 63 vs lines 64 to 68:** Line 63 says `"A skill the PECAT tables first expect in a grade is owned there"`, while lines 64 to 68 override that for hand dribbling (PECAT expects in K; owned in grade 1) and self-turned rope (PECAT expects in K; owned in grade 2). State clearly that PECAT's first grade is the default unless the indicator wording requires a later grade (with the two exceptions named).
  3. **`scripts/progression.py` `code_grades` does not enforce Cory's 2026-11-20 high school ownership rule:** Lines 74 and 99 to 100 return `(['9', '10', '11', '12'], ['9', '10', '11', '12'])` for PE span 12, which allows grades 11 and 12 (electives) to own 9 to 12 indicators. Under STANDARD.md rule 5, only grades 9 and 10 may own span 12 indicators, while 11 and 12 may only carry `~CODE`.
- **Cost:** A writer reading lines 87 to 88 gets an impossible rule; a future edit to `physical-education.csv` could silently move a 9 to 12 owner into elective grades 11 or 12 without the gate catching it.
- **Fix:**
  - In **STANDARD.md line 87 to 88**, replace `"The K to 2 progression rows carry these as ~CODE at most."` with: `"Where a K to 2 span indicator touches one of these (SHAPE.S2.2.2, S2.2.7, S4.2.2), it is owned in grade 1 or 2 at naming-only depth, never scored as tactics or program planning."`
  - In **STANDARD.md line 63**, change `"A skill the PECAT tables first expect in a grade is owned there"` to `"By default, a skill the PECAT tables first expect in a grade is owned there (with the grade before carrying ~CODE), except where the 2024 indicator names a later-developing form (continuous hand dribbling owned in grade 1; self-turned rope owned in grade 2)."`
  - In **scripts/progression.py `code_grades`** (lines 93 to 101), separate `'physical-education'` span `'12'` from `'health'` so it returns `(['9', '10'], ['9', '10', '11', '12'])` (owner grades 9 and 10; all grades 9 to 12 for `~CODE`).
- **Confidence:** Firm.

### 6. Handoff and `~` carry gaps in `data/progressions/physical-education.csv`, plus a missing dry-land skill task in `g2-water-skills`

- **Where:** data/progressions/physical-education.csv lines 38 (`g2-water-skills`), 44 (`g2-stretch-why`), 47 (`g2-talk-problems`), 86 to 89 (grade 5 `~` rows), 110 (`g6-stretch-types`), 143 and 145 (grade 8 `~` rows), 185 to 204 (grades 11 and 12 `~` rows); docs/courses/physical-education/APPROACH.md lines 98 to 101.
- **What is wrong:** Checking handoffs in both directions and owned-indicator coverage across all 203 rows found three distinct issues:
  1. **Missing dry-land skill task in `g2-water-skills` (line 38):** `APPROACH.md` lines 98 to 99 promise that `"Curio Class gives dry-land safety and skill tasks every school can teach: a reach rescue, a throw rescue to a target and fastening a life jacket."` `g5-water-skills`, `g8-water` and `g10-water` all carry that dry-land skill task. `g2-water-skills` (owning `SHAPE.S1.2.17`) does not: it says `"Assessed by a knowledge task (safety rules) and, where a pool exists, a skill task (float and kick)"`, leaving schools without a pool with recall only for a motor-skill indicator (C8).
  2. **Stale skip note in `g6-stretch-types` (line 110):** The note says `"The handoff skips a grade because the stretch idea from grade 3 returns in training here."` Its `assumes` column is `g5-fitt` (grade 5, no skip), not `g3-warm-cool` (grade 3).
  3. **Skipped grades in `~` carries with no note:** `assumes`/`hands_on` pairs are symmetric and almost all skipped `assumes` rows explain the skip, **but many `~` carries skip one or two grades silently**:
     - K to 2: `~SHAPE.S2.2.6` (`g2-stretch-why`) and `~SHAPE.S3.2.3` (`g2-talk-problems`) are owned in K and skip grade 1.
     - 3 to 5: `~SHAPE.S1.5.10`, `11`, `12`, `16`, `18`, `19`, `20` (grade 5 game rows) are owned in grade 3 and skip grade 4 (only `g5-strike-field-skills` and `g5-gym-dance-sequence` note the skip on `assumes`, not on the `~` carries).
     - 6 to 8: `~SHAPE.S1.8.6`, `8`, `14`, `15`, `19` (grade 8 play rows) are owned in grade 6 and skip grade 7.
     - 9 to 12: 14 grade 9-owned indicators skip grade 10 before returning as `~` in grade 11; 10 grade 10-owned indicators skip grade 11 before returning as `~` in grade 12; and `~SHAPE.S3.12.1` (`g12-community`) is owned in grade 9 and skips both grades 10 and 11.
- **Cost:** K to 2 schools without a pool fail C8 on `SHAPE.S1.2.17`. Unexplained `~` skips and the mismatched `g6-stretch-types` note leave frame planners unsure whether a skill needs a readiness check or an opening retrieval task.
- **Fix:**
  - In **`g2-water-skills` (line 38)**, add the K to 2 dry-land skill task: `"Assessed by a knowledge task (safety rules) and a dry-land skill task for every school (fastening a life jacket and a reach rescue on the floor); in-water tasks (float and kick) only where a pool exists."`
  - In **`g6-stretch-types` (line 110)**, either add `g3-warm-cool` to `assumes` (and `g6-stretch-types` to `g3-warm-cool`'s `hands_on`) with the note explaining grades 4 and 5, or remove the stale skip sentence if `g5-fitt` is the intended handoff.
  - Add a one-line rule in **STANDARD.md section 3 rule 1** stating whether `~CODE` in a later year of a span may skip a grade (for example in high school electives or game-synthesis years) and requiring a brief note in the row when it does, then add the short note to the affected grade 2, 5, 8, 11 and 12 rows.
- **Confidence:** Firm for `g2-water-skills` and `g6-stretch-types`; Likely for the `~` carry rule.

### 7. Course list mismatch with `data/courses.csv` and incomplete cross-subject leans in `STANDARD.md`

- **Where:** data/courses.csv line 34; docs/courses/physical-education/STANDARD.md line 5 and section 6 (lines 125 to 136); data/progressions/physical-education.csv lines 79, 97, 130, 131, 153, 167, 179.
- **What is wrong:**
  1. **Catalogue mismatch:** `data/courses.csv` line 34 has one row (`pe,health-pe,Physical Education,k-12,,y,`) with empty notes, whereas `STANDARD.md` line 5 says `"four courses, one per band"`, `STANDARD.md` rule 5 sets two required and two elective high school years, and `ADOPTION-BAR-SUBJECTS.md` line 565 says `"Physical education (4)"`. Compare SEL and ELD in `data/courses.csv` lines 41 to 49, which were split on 2026-11-21 into four band rows (`sel-k-2` to `sel-9-12`, `eld-k-2` to `eld-9-12`) with `"one frame per grade year"`. Neither `STANDARD.md` nor `APPROACH.md` states the PE course ids (`pe-k-2`, `pe-3-5`, `pe-6-8`, `pe-9-12`) or whether PE has 4 band frames or 13 grade-year frames.
  2. **Cross-subject leans mismatch:** All 11 `cross_subject` ids in `physical-education.csv` exist in core standards/progressions, **but `STANDARD.md` section 6 does not match them**: it omits **Social studies** (`ss4-regional-cultures`, `ss6-complex-societies`), omits **grade 8 physical science** (`MS-PS2-2` used in `g9-force-motion`), omits **grade 5 math** (`5.G.A.2` used in `g5-goal`), and says `"ratio and data (grades 6 to 7)"` when `physical-education.csv` uses grade 6 math (`6.RP.A.3`, `6.SP.B.4`) and no grade 7 math.
  3. **Same-year core lean timing:** Four rows lean on same-grade core standards (`g4-pulse-body` on `4-LS1-1`; `g5-goal` on `5.G.A.2`; `g7-rest` and `g7-eat-move-well` on `MS-LS1-3` and `MS-LS1-7`, taught in grade 7 science unit 7.3). Only `g6-heart-rate` notes same-year timing; the other four do not remind frame planners to check unit order.
- **Cost:** Stage 3 frame planners do not know the `plan.py` course ids or frame grain; cross-subject handoffs in `STANDARD.md` drift from `physical-education.csv`.
- **Fix:**
  - Ask Cory to split `data/courses.csv` line 34 into four rows (`pe-k-2`, `pe-3-5`, `pe-6-8`, `pe-9-12`, noting one frame per grade year, grades 11 and 12 electives; see Questions for Cory 1).
  - Replace **STANDARD.md section 6** Science and Math bullets and add Social studies:
    > - **Science:** heart rate, body systems, energy and force lean on science (`4-LS1-1` in grade 4, `MS-LS1-3` and `MS-LS1-7` in grade 7, `MS-PS2-2` in grade 8); PE uses the idea, science teaches the model. Where a PE row leans on a same-grade science or math standard, the frame checks unit order and supplies a brief worked example if PE comes first.
    > - **Math:** graphing personal progress, heart-rate scaling and data plots lean on `5.G.A.2` (grade 5), `6.RP.A.3` (grade 6) and `6.SP.B.4` (grade 6).
    > - **Social studies:** cultural meaning and history of games, sports and dance lean on `ss4-regional-cultures` (grade 4) and `ss6-complex-societies` (grade 6); units name each other.
- **Confidence:** Firm.

### 8. Verbatim SHAPE 2024 standard statements in `shape-pe-2024.txt` header, missing PE carve-out in `UNIT-PLAN.md` rule 15, and minor verb drift on `SHAPE.S3.5.7`

- **Where:** data/standards/shape-pe-2024.txt line 7 and line 164; docs/courses/UNIT-PLAN.md line 133 (rule 15); data/progressions/physical-education.csv line 82 (`g4-world-activities`).
- **What is wrong:**
  1. `data/standards/shape-pe-2024.txt` line 7 (`# note: standards: S1 develops a variety of motor skills; S2 applies knowledge related to movement and fitness concepts; S3 develops social skills through movement; S4 develops personal skills, identifies personal benefits of movement, and chooses to engage in physical activity.`) reproduces SHAPE America's four 2024 standard statements verbatim (confirmed via web search on shapeamerica.org), despite line 9 noting "All Rights Reserved" and `STANDARD.md` line 23 to 24 already stating them in Curio Class's own words.
  2. `UNIT-PLAN.md` rule 15 (line 133) requires `"The standard's verb is quoted exactly"` and adds carve-outs for `*Arts:*` and `*Computer science:*`, but still has **no `*Physical education:*` carve-out** (carried over from the first read's finding 1).
  3. On `SHAPE.S3.5.7`, SHAPE America's published 2024 indicator (verified via web search) begins with `"Describes physical activities..."`, whereas `shape-pe-2024.txt` line 164 says `"Show movement activities from cultures around the world."` In `physical-education.csv` line 82 (`g4-world-activities`), the row opens with `"Show..."` but assesses only by a knowledge task (`"names where an activity comes from"`). Changing line 164 from `"Show"` to `"Describe"` aligns both the paraphrase and the assessment with the framework.
- **Cost:** Low legal/editorial risk on an internal comment line, but a unit writer following `UNIT-PLAN.md` rule 15 literally could quote SHAPE's all-rights-reserved indicator verbs onto teacher pages.
- **Fix:**
  - Replace **data/standards/shape-pe-2024.txt line 7** with: `# note: standards (our words): S1 motor skills; S2 knowledge of movement and fitness; S3 social skills through movement; S4 personal skills, benefits of movement and choosing to be active.`
  - Replace **data/standards/shape-pe-2024.txt line 164** with: `SHAPE.S3.5.7	Describe movement activities from cultures around the world.` (and update `g4-world-activities` opening verb to match).
  - Append to **docs/courses/UNIT-PLAN.md rule 15** (line 133): `*Physical education:* a plan cites the indicator id and states its action in our own words (data/standards/shape-pe-2024.txt); the publisher's wording is never quoted (all rights reserved).`
- **Confidence:** Firm.

### 9. Stale notes left behind after the 2026-11-19 to 2026-11-21 updates

- **Where:**
  - `docs/courses/physical-education/APPROACH.md` line 121: says `"PECAT 2019's K to 5 overview and standard 1 tables"` (stale: all K to 5, 6 to 8 and 9 to 12 grade tables were read 2026-11-19 per `STANDARD.md` line 16 and lines 78 to 91).
  - `docs/ADOPTION-BAR-SUBJECTS.md` line 668 (Sources table, PECAT 2019): still says `"Grade tables unread"` (contradicts lines 286 and 565 of the same file).
  - `docs/ADOPTION-BAR-SUBJECTS.md` line 565 ("Before a scope and sequence"): still says `"Owed: the approach page's yes (Desk q-prework-open-1)"`, while `APPROACH.md` line 3 says `"Approved by Cory 2026-11-21 (Desk q-prework-open-1)"`. Meanwhile `STANDARD.md` line 8 and `docs/agents/lenses/physical-education.md` line 8 still label `APPROACH.md` as `(draft)`.
  - `docs/standards-notes/pe-2014-to-2024.md` line 71: says `"PECAT 2019 was read in part on 2026-11-16 (K to 5 overview and standard 1 tables...)"` (stale after the 2026-11-19 full grade-table read).
  - `data/standards/shape-pe-2024.txt` line 9: says `"so ids only"`, superseded by line 10 (`"After each id, a tab and one line in Curio Class's own words"`).
- **What is wrong:** Contradictory read-status and approval-status notes across five files violate C13 ("approach page, with sources and how much of each was read") and confuse downstream writers.
- **Cost:** A writer or reviewer checking C13 sees three different statements of how much of PECAT was read and two different statements of whether `APPROACH.md` is approved.
- **Fix:** Update all five lines to match the current state: PECAT 2019 preliminary analyses, directions and all grade tables (K to 5, 6 to 8, 9 to 12) read 2026-11-16 and 2026-11-19; `shape-pe-2024.txt` line 9 changed to `"so ids and our own words only"`; approval status aligned once Cory signs off on the revised `APPROACH.md`.
- **Confidence:** Firm.

## What is right and should not be touched

- **The 210 ids and own-words paraphrases** in `data/standards/shape-pe-2024.txt` (aside from header line 7 and `S3.5.7`'s verb), and the single-owner placement of all 210 indicators in `data/progressions/physical-education.csv`.
- **STANDARD.md section 4** (appropriate practice guidelines in our own words: no exercise as punishment, no elimination, no human targets, no public team picks, stretching after warm-up, private fitness records never graded, grading on outcomes never dress/attendance/effort alone) and **section 5** (what is left out: pre-K, state fitness tests, individual adapted PE plans).
- **The five-to-four mapping and outcome-split rule** in `docs/standards-notes/pe-2014-to-2024.md`.
- **The open-material scout** (`docs/reviews/physical-education-open-material-2026-11-16.md`): clear licence checks and the right call to write PE fresh rather than adapt registration-gated or NC material.
- **APPROACH.md's core pedagogy:** the five kinds of day, the five-part lesson shape with at least half the lesson in moderate to vigorous activity, the day-1 baseline watch repeated on Check day for growth, private closure self-checks, the nurse/family-guided injury rule, the EL movement-words/frames/separate-marking rule, dry-land water safety, and "What a tool may and may not do".
- **All 11 cross-subject leans in `physical-education.csv`**, which all point to real core standards or progression rows.

## What I could not judge

- Individual wording of the remaining ~190 of 210 indicators on SHAPE America's live pages (web search verified the 4 standard statements, the 16 end-of-span boundary codes and a sample of `.1` and boundary indicators, not all 210 lines individually).
- Exact grade-level placements inside CDC's PECAT 2019 grade tables (the PECAT PDF was not opened in this run; grade-order notes rest on `STANDARD.md` section 3 and the progression rows).
- Oregon's 2025 PE criteria PDF and SHAPE America's 2009 Appropriate Instructional Practice Guidelines PDF (not opened in this run).
- Whether `scripts/progression.py` passes cleanly on `data/progressions/physical-education.csv` by execution (shell commands could not run in this environment; checks were performed by manual inspection of all 203 rows).

## Sources

- SHAPE America, National Physical Education Standards (2024): https://shapeamerica.org/standards/pe/new-pe-standards/ (verified the 4 standard statements, grade-span coding schema, all 16 end-of-span boundary indicator codes, and sample indicator wording via web search).
- SHAPE America, Guidelines (weekly instructional minutes and Appropriate Instructional Practice Guidelines / Essential Components): https://www.shapeamerica.org/standards/guidelines/ (verified 150 minutes/week elementary and 225 minutes/week middle and high school recommendations, and the structure of Appropriate Instructional Practice Guidelines and Essential Components via web search).
- CDC, Physical Education Curriculum Analysis Tool (PECAT), 2019: https://www.cdc.gov/physical-activity-education/media/pdfs/2025/04/18_300595-A_PECAT_042619_508tagged_CR2025-04-07_revised-clean.pdf (listed in `ADOPTION-BAR-SUBJECTS.md`; not opened directly in this run).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Fill all missing unit (1, 3, 4, 6, 7) and section (2, 4, 6, 7, 11) plan fields, move Safe space to unit field 8, Family note to unit field 9, Two rooms to section field 10, and add check accommodations to section field 9 | Aligns PE APPROACH.md with UNIT-PLAN.md and overrides default hands-up self-marking for a teacher-judged subject | docs/courses/physical-education/APPROACH.md |
| Add a dedicated Sensitive ground section naming cultural/sacred dances, no weighing/diet talk, medical/disability adaptations, gender-neutral grouping, mental-health boundary + disclosure reporting route, and sensitivity/safety reads | Consolidates Cory's 2026-11-20 calls and meets Stage 1 item 8 and C12 | docs/courses/physical-education/APPROACH.md; STANDARD.md; data/progressions/physical-education.csv (9 cultural rows, 4 emotion rows) |
| Fix STANDARD.md lines 63 and 87 to 88 so K to 2 span indicators (S2.2.2, S2.2.7, S4.2.2) are owned at naming-only depth rather than "`~CODE` at most", and narrow `code_grades` for PE span 12 to owners 9 and 10 | Removes an impossible rule contradiction and makes the gate enforce Cory's 2026-11-20 high school call | docs/courses/physical-education/STANDARD.md; scripts/progression.py |
| Add dry-land skill task (life jacket, floor reach rescue) to `g2-water-skills` | Matches APPROACH.md's promise and C8 for schools without a pool | data/progressions/physical-education.csv line 38 |
| Fix `g6-stretch-types` stale skip note and document `~` carry skip rule | Removes contradictory handoff note and clarifies readiness vs retrieval for frame planners | data/progressions/physical-education.csv line 110; STANDARD.md section 3 |
| Reword `shape-pe-2024.txt` header line 7 and `S3.5.7` ("Describe"), and add the PE carve-out to UNIT-PLAN.md rule 15 | Removes verbatim publisher standard sentences and prevents unit writers from quoting SHAPE verbs | data/standards/shape-pe-2024.txt; docs/courses/UNIT-PLAN.md |
| Align STANDARD.md section 6 with the actual cross-subject leans in `physical-education.csv` and note same-year timing for grades 4, 5 and 7 | Keeps prose and progression data consistent | docs/courses/physical-education/STANDARD.md; data/progressions/physical-education.csv |
| Fix the five stale PECAT read-status and approval-status notes | Keeps C13 source read-status accurate across all PE docs | APPROACH.md, ADOPTION-BAR-SUBJECTS.md, pe-2014-to-2024.md, shape-pe-2024.txt, STANDARD.md, lens |

## Questions for Cory

1. **Catalogue grain in `data/courses.csv` (finding 7).** `data/courses.csv` line 34 still has one `pe` row (`k-12`, blank notes), while `STANDARD.md` and `ADOPTION-BAR-SUBJECTS.md` describe four band courses (with per-grade outcomes and 2 required + 2 elective years in 9 to 12). **Recommended:** split `pe` into four rows (`pe-k-2`, `pe-3-5`, `pe-6-8`, `pe-9-12`), matching SEL and ELD, with notes stating one frame per grade year (13 frames, grades 11 and 12 electives).
2. **Default dose by band (finding 4).** Elementary PE was settled as "about 2 to 3 sessions a week", leaving exact session counts, minutes per session, short paths and 6 to 12 defaults unset. **Recommended:** adopt the single defaults in finding 4 (K to 2: 80 x 30 min; 3 to 5: 80 x 35 min; 6 to 8: 96 x 45 min; 9 to 12: 80 x 45 min per year, with 60 to 64 session short paths and frame flexibility) while keeping the open disclosure against SHAPE America's 150 and 225 minute weekly guidelines.
3. **High school S4.12 ownership split (finding 2).** Dumping all nine `SHAPE.S4.12` indicators into one grade 10 row leaves five partly unmet. Moving `S4.12.1` to `S4.12.5` to grade 9 (`g9-choose-active`) and splitting `S4.12.6` to `S4.12.9` into two grade 10 rows moves standards between grades. **Recommended:** yes, split S4.12.1 to 5 to grade 9 and S4.12.6 to 9 to grade 10 so both required years teach and assess every part in full.
4. **Leave-out rule for PE (finding 3).** **Recommended:** state on the course page that a school or family may leave out in-water tasks, specific outdoor activities or cultural dances/games that do not fit local policy or resources (using dry-land or open alternatives), and that if a school drops all units for an indicator, the course page does not claim that indicator.
5. **Confirm updated `APPROACH.md` (findings 1, 3, 4).** `APPROACH.md` was marked approved on 2026-11-21 before the missing UNIT-PLAN.md fields, Sensitive ground section and default doses were added. **Recommended:** apply findings 1, 3 and 4 and confirm approval on the updated text.

## Against the first read

Opened `docs/reviews/prework-physical-education-read-2026-11-19.md` after finishing all findings above. Because the first read ran on 2026-11-19 (before the 2026-11-19 fixes, before `data/progressions/physical-education.csv` existed, before Cory's 2026-11-20 calls, and without web search), most of its original findings (indicator paraphrases, initial ownership rule, injury line, baseline watch, conduct rule, private self-check, PECAT L46 tables, older-outcome split rule) were already fixed, and most of this read's findings are new:

- **Already in the first read (still open or only partly fixed):**
  - `UNIT-PLAN.md` rule 15 PE carve-out (first read finding 1; still missing in `UNIT-PLAN.md` line 133).
  - Unstated session length / dose by band (first read finding 8 flagged missing K to 5 session length; the fix added the SHAPE 150/225 disclosure but still left no session counts or lengths for any band).
  - Placement of Safe space under unit field 2 instead of unit field 8 (first read Q4/5 flagged space/equipment under unit field 2; the fix redirected supplies to unit field 8 and section field 5 but left Safe space under unit field 2).
- **New in this second read:**
  - Full field-by-field `UNIT-PLAN.md` audit of `APPROACH.md` (finding 1), especially missing unit field 7 (leaving hands-up self-marking unoverridden), missing unit fields 1, 3, 4, 6 and section fields 2, 4, 6, 7, 11, misplaced unit field 9 and section field 10, and missing check accommodations in section field 9.
  - High school `g10-choose-active-apply` dropping parts of five of nine `SHAPE.S4.12` indicators, plus stale grade-11 note in `g9-choose-active` (finding 2).
  - Missing Sensitive ground section, missing `sensitivity-read.md` (sensitivity and safety) routing, Cory's sacred-dance rule absent from `STANDARD.md`, `APPROACH.md` and 9 of 11 cultural rows (including `g8-culture-matters` with `ritual`), missing body/weight/diet rules and disclosure reporting route in `APPROACH.md`, and missing leave-out rule (finding 3).
  - `STANDARD.md` lines 87 to 88 contradicting K to 2 ownership (`~CODE` at most for K to 2 span indicators) and `scripts/progression.py` `code_grades` still allowing elective grades 11 and 12 to own span 12 indicators (finding 5).
  - `g2-water-skills` missing the dry-land skill task promised by `APPROACH.md`, `g6-stretch-types` stale skip note, and unexplained skipped-grade `~` carries across `physical-education.csv` (finding 6).
  - `data/courses.csv` single-row mismatch and `STANDARD.md` section 6 cross-subject lean discrepancies plus same-year timing notes (finding 7).
  - Live web verification of SHAPE America 2024 boundary codes and weekly minutes, catching verbatim SHAPE 2024 standard statements in `shape-pe-2024.txt` line 7 and verb drift on `SHAPE.S3.5.7` (finding 8).
  - Five new post-2026-11-19 stale notes across `APPROACH.md`, `ADOPTION-BAR-SUBJECTS.md`, `pe-2014-to-2024.md`, `shape-pe-2024.txt`, `STANDARD.md` and the lens (finding 9).

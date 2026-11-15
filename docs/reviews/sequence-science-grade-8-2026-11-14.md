# Sequence read: science-grade-8, 2026-11-14

Expert cold read of the scope and sequence for Science, Grade 8, done to docs/pipeline/briefs/sequence-read.md against docs/RUBRIC-SCIENCE.md (scope and sequence layer: Gateway 1 at plan level, 2a to 2c, 2e, 2h, S1, S6 costs, S7, S11). The read is my own; no Codex read was opened. The Codex read of this course was already finished when I started (S:\CurioClass-codex\_scopes\summary.txt, 22:45).

## What I read

- AGENTS.md, docs/agents/EXPERT.md, docs/GLOSSARY.md, docs/agents/lenses/science.md, docs/RUBRIC-SCIENCE.md, the brief.
- docs/courses/science-grade-8/frame.md and scope-and-sequence.md in full.
- data/plans/science-grade-8/days.csv (all 160 rows) and source-map.csv.
- data/progressions/science.csv: every row the grade 8 rows assume, traced to its last user.
- data/plans/calendar.csv (grade 8 rows for all four subjects).
- The OpenSciEd storylines for 8.1 to 8.6 in S:\CurioClass-sources\openscied-ms (lesson questions, base days, and where the base puts its own assessments; ideas only).
- A script check of the source map's minute allocations. Every day sums to 50 minutes and every lesson keeps its base minutes, except the 13 condensations the frame names and the two named 10-minute trims (8.2 lesson 14, 8.4 lesson 13).

Gates: `scripts/plan.py check` shows 0 failures for science-grade-8. `scripts/frame.py calendar` puts its course-level checks in weeks 15 and 32, on days 75 and 159, which matches the calendar. `scripts/stale.py check` shows 0 failures. Biology fails 14 checks because a Codex run is writing it now: another course, not this one.

## Verdict

This is the most carefully counted of the three middle school plans:
- every one of the 91 base lessons is placed in order;
- the three Curio Class additions sit exactly where the frame puts them;
- the minutes check out day by day.

Two problems remain:
- **The readiness rule.** The course applies its frame's version of the rule consistently, but that version is not the brief's. Four rows last used in grade 6 (the wave and light-ray models, sky patterns and geologic time) open with a retrieval task instead of a readiness check.
- **Assessment time booked as base time.** Several assessments are counted as base synthesis minutes. One of them (day 96) assesses the light model before the base lesson that builds its consensus.

Both are fixable inside the current days, with one choice for the lead.

## Findings

### 1. Four rows last used in grade 6 need readiness checks, not retrieval tasks (serious)

- **What is wrong.** Under sequence-write rule 2, only the year before (grade 7) or earlier this year earns a retrieval task. The lead confirmed this literal reading for the social studies fixes (docs/reviews/sequence-6-8-fixes-2026-11-14.md). The frame writes the rule as "two or more grades between its last use and this one" and calls grade 6 "idle one grade". Under the brief, these rows need checks:
  - **s4-wave-model and the wave model.** Last used by s6-digital-signals in grade 6; assumed by s8-wave-amplitude-energy. Days 28 and 32 open them with retrieval tasks.
  - **s6-light-paths and the light-ray model.** Grade 6 only; assumed by s8-wave-amplitude-energy and s8-earth-sun-moon. Retrieval tasks on days 28, 32 and 79.
  - **s5-shadows-sky and the earth-sun-moon model.** Last used by s6-climate-circulation; assumed by s8-earth-sun-moon. Retrieval task on day 79.
  - **s6-geologic-time.** Grade 6 only; assumed by s8-fossil-record. Retrieval task on day 134.

  Every other return is right by both readings. s4-collisions, s3-balanced-forces and s4-speed-energy are checked on day 1. s3-magnet-static, s4-energy-device and s5-gravity-down are checked on day 46. s5-star-brightness is checked on day 76, the two grade 3 trait rows on day 104, and the four grade 3 rows on day 131. All grade 7 rows get retrieval tasks.
- **Why it matters.** Nothing in grade 7 uses waves, light rays, the Earth-sun-moon model or geologic time. Students meet them in grade 8 after a full year away, which is exactly the gap the rule exists to catch. Unit 2 builds its whole wave model on that return.
- **Fix.**
  - **Day 26:** 40 minutes of response, then 10 minutes of readiness on s4-wave-model and s6-light-paths, with their models. Day 28's retrieval slot becomes the response. Unit 2 has no spare minutes, so the lead chooses one of two:
    - the response runs inside days 28 and 32, as grade 7's day 70 does, recorded as an exception to the frame's one-lesson reteach;
    - or one more base day is condensed to fund a reteach lesson, recorded in the frame's Days entry. The candidate is the Shorter path's fold of day 36 into day 35.
  - **Day 76:** add s5-shadows-sky to the s5-star-brightness check. Day 78's reteach covers both. s6-light-paths is then earlier-year use, so day 79 keeps its retrieval task for it.
  - **Day 131:** add s6-geologic-time to the unit 6 check. Readiness becomes 15 minutes and the Curio Class response 20, since five rows will not fit in ten minutes. Day 133's reteach covers it.
  - **The frame:** its rule sentence and seam rows 115 and 118 match the brief.
- LAYER: frame and sequence. REPEAT: yes (the same rule finding as the grade 6 and grade 7 reads and the social studies reads). Confidence: firm on the rule; likely on the unit 2 route, which is the lead's choice.

### 2. Assessment minutes are booked as base synthesis minutes, and day 96 assesses before the consensus (moderate)

- **What is wrong.** The scope and sequence states the policy: "assessment and its response replace the corresponding base synthesis work". The source map then books assessment minutes as base lesson minutes. Where the base puts its own assessment in that lesson (8.1 lesson 10, 8.3 lesson 12, 8.5 lesson 17), this is a fair match. Where it does not, the base's consensus lesson loses most of its time without the frame's 13-day condensation list showing it:
  - **8.3 lesson 9** (3 base days, the speaker consensus model; already condensed to 2): 35 minutes on day 65, then all of day 66 as the mid-unit assessment, then 5 minutes on day 67.
  - **8.4 lesson 12** (2 base days, the red-moon consensus): all of day 96 is the mid-unit assessment, and the consensus work comes on day 97, after students have been assessed on the light-material model it builds.
  - **8.5 lesson 7** (2 base days, putting the muscle explanation together): 45 minutes on day 115, then 40 of day 116's 45 are the mid-unit assessment. Meanwhile the base's own midpoint assessment, the goldfish transfer task in lesson 10, becomes an ordinary learning day (days 120 and 121).
  - **8.6 lesson 6** (2 base days): 5 minutes on day 142, the mid-unit assessment on day 143, 35 minutes on day 144. The base's own assessment, in lesson 11 (day 151), runs as a learning task.
- **Why it matters.**
  - **Storyline order.** The consensus model is the storyline's main product, and assessing before it is built (day 96) breaks the order the frame promises.
  - **The loss record.** The minute record overstates base time kept, so the frame's loss check reads cleaner than the plan is.
- **Fix.**
  - **Days 96 and 97 (settled below):** swap their content. Day 96 holds lesson 12's consensus (40 minutes) and lesson 13's opening (10). Day 97 holds the mid-unit assessment (40) and its response (10).
  - **Unit 5 (settled below):** move the mid-unit assessment to base lesson 10's place, rebalancing days 120 and 121 so one day holds 40 minutes of assessment and 10 of response. Day 116 returns its 40 minutes to lesson 7. The mid then covers MS-LS3-1, MS-LS1-2 and the sexual-reproduction part of MS-LS3-2, and claims nothing about asexual reproduction.
  - **Lessons 8.3 lesson 9 and 8.6 lesson 6:** the source map books the assessment minutes as "ours" and records the base minutes actually kept. The lead then either lists those as further condensations in the frame, or, for unit 6, moves the mid-unit assessment to the base's own assessment point in lesson 11.
- LAYER: base text and sequence. REPEAT: new. Confidence: firm on the accounting and the day 96 order; judgment call on unit 6.

### 3. Check days claim every part of more codes than their minutes hold (moderate)

- **What is wrong.**
  - **Day 75:** course-level check 1 runs six codes in six "short linked performances" in 50 minutes, and the note says "every part of each listed code".
  - **Day 159:** the note claims the same for seven codes, while the scope and sequence says, correctly, that it "samples complete performances... rather than attempting every owned code again".
  - **Day 157:** the end-of-unit assessment gives six codes 35 minutes after 15 minutes of embryo work. It leans on products, but the row does not say which product carries which part.
- **Why it matters.** A coverage claim the minutes cannot hold passes the problem silently to the unit-plan writer. The scope and sequence's own For the lead item 2 already sees this risk.
- **Fix.**
  - **Days 75 and 159:** the notes name the part each performance samples and call the check a sample, matching the scope and sequence.
  - **Day 157:** the note names the carriers. MS-LS4-1 and MS-LS4-2 were assessed in full on day 143 and are sampled here. MS-LS4-6 is carried by the numerical selection analysis (days 148 to 150), MS-LS4-3 by the matched-stage embryo analysis (days 155 to 157), and MS-LS1-4 by the reproduction argument (days 136 and 137). The 35 minutes go to MS-LS4-4 transfer and the parts no product holds.
- LAYER: sequence. REPEAT: yes. Confidence: firm.

### 4. Unit 5's plant DNA extraction is dropped to supplied observations against the frame (minor)

- **What is wrong.** The frame keeps the strawberry DNA extraction hands-on: rubbing alcohol dispensed by the teacher, kept from flames, with eye protection. Days 122 and 123 instead use "supplied extraction observations only". The no-kit path is meant to be the fallback, not the plan.
- **Why it matters.** Base 8.5 lesson 12 is an investigation, and this is the unit's one hands-on look at genetic material.
- **Fix (settled below, subject to the safety read).** Days 122 and 123 run the extraction with the teacher-dispensed alcohol the frame describes, and the supplied observations become the named no-kit path.
- LAYER: base text. REPEAT: new. Confidence: likely.

### 5. Days 9 and 10 list MS-LS1-8 with no touch work (minor)

The codes cells of days 9 and 10 include MS-LS1-8, but their goals are balanced motion and paired forces, and their skills cells lack s8-senses-brain. Touch receptors are taught on day 11, which lists the code but not the skill. Fix: drop MS-LS1-8 from days 9 and 10, and add s8-senses-brain to day 11's skills as a start. LAYER: process. REPEAT: new. Confidence: firm.

### 6. "Base Curio Class" labels on additions (minor)

Notes on the reteach, safety and addition days read "Base Curio Class reteach: 50 min" and "Base Curio Class safety". A credit line is owed only on adapted days, and "Base" invites one on days that adapt nothing. Fix: write "Curio Class reteach: 50 min" (no "Base") wherever no base lesson is used. LAYER: process. REPEAT: new. Confidence: firm.

### 7. Day 17 claims all of MS-PS2-1 before the design work (minor, judgment call)

Day 17's mid-unit assessment (base 8.1 lesson 10, the base's own assessment point) asks for "an unseen protective-device solution" and "every part of each listed code". MS-PS2-1's design part is built in lessons 11 to 14 (days 18 to 24). Fix: day 17 claims the paired-force explanation part of MS-PS2-1, and the design-a-solution part stays with day 25. LAYER: sequence. REPEAT: new. Confidence: judgment call.

## What is right (do not touch)

- **Base order and placement.** All 91 base lessons are placed in base order. 8.1's optional lesson 16 is cut for the stated reason, and the "+CS" variants are never mapped.
- **Minutes.** The per-day minute allocations sum to 50 on every day. The 13 named condensations and the two named 10-minute trims are the only places base time shrinks, assessment booking aside (finding 2).
- **The additions.** They sit at the frame's seams: static charge after lesson 8 (days 63 to 65), gravitational stored energy after lesson 11 (days 71 and 72), and the whole-cell model between lessons 5 and 6 (days 112 and 113). Each completes the part of its expectation that the base leaves out.
- **Readiness and reteach placement.** Every check sits in the last ten minutes of a respond day or of day 1. Every reteach is a whole-class lesson on the day after the hook, which keeps each anchor clean.
- **Course-level checks.** They draw a just-assessed unit's skills from earlier contexts (unit 3 skills through unit 1 and 2 objects; unit 6 reasoning through unit 5 plant and cattle cases), and neither repeats the end-of-unit assessment before it.
- **Cross-subject.** ELA 8's argument, research and gene-claims units are handled with named bridges. The stale math citations (units 6 and 7) are flagged rather than silently changed.
- **Care.** Evolution is taught as the evidence shows, with no "some say" softening. Family-trait, hearing and belief disclosures are ruled out on every day that could invite them. The laser and solar-viewing replacements are named.
- **Shorter path.** The section has ten unassessed folds and a stated minute gap.

## What I could not judge

- The EdReports 6 to 8 science evidence guide (not read this session).
- Whether 35 to 50 minute assessments hold in a real class.
- The element references, which I sampled, not checked row by row.
- Whether the safety read will clear a teacher-run extraction (finding 4).
- Material costs, which are unpriced.

## Sources

The OpenSciEd Middle School 2022 storylines for 8.1 to 8.6 (S:\CurioClass-sources\openscied-ms, CC BY 4.0, ideas only); data/progressions/science.csv; data/plans/calendar.csv; data/standards/ngss-pe-dimensions.csv; docs/reviews/sequence-6-8-fixes-2026-11-14.md (the lead's clarification of the readiness rule).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Readiness checks added on day 26 (s4-wave-model, s6-light-paths and their models), day 76 (adds s5-shadows-sky) and day 131 (adds s6-geologic-time; 15 minutes of readiness, 20 of response) | Applies the readiness rule by last use; the timing rule is unchanged | data/plans/science-grade-8/days.csv, scope-and-sequence.md, frame.md seams |
| The content of days 96 and 97 is swapped: consensus first, then the mid-unit assessment | The consensus is built before it is assessed | days.csv, source-map.csv |
| Unit 5's mid-unit assessment moves to base lesson 10's place (days 120 and 121), and day 116's 40 minutes return to lesson 7 | Uses the base's own midpoint and keeps the lesson 7 consensus | days.csv, source-map.csv, scope-and-sequence.md |
| Assessment minutes in 8.3 lesson 9 and 8.6 lesson 6 are booked as "ours", and the base minutes kept are recorded | Honest record of base time | source-map.csv |
| The notes for days 75, 157 and 159 name the parts each product or performance carries, and the checks are called samples | Coverage claims match the minutes | days.csv, scope-and-sequence.md |
| Days 122 and 123 run a teacher-dispensed extraction, with supplied observations as the no-kit path | Restores the frame's investigation; the safety read still decides | days.csv |
| MS-LS1-8 is dropped from days 9 and 10, and s8-senses-brain is added to day 11 | Codes match content | days.csv |
| "Base Curio Class" becomes "Curio Class" in notes on days that adapt nothing | Credit lines only on adapted days | days.csv |
| Day 17 claims MS-PS2-1's paired-force part only | The design part is taught on days 18 to 24 | days.csv |

## For Cory

Nothing needs Cory. The unit 2 reteach route in finding 1 is the lead's call, inside the 160 days Cory has already settled. Material costs stay unpriced until unit planning.

## Across the band

Patterns across science-grade-6, science-grade-7 and science-grade-8, and the hand-offs between them.

1. **The readiness rule has three readings across three courses.** All three frames carry the same gloss, "two or more grades between its last use and this one", which differs from the brief's "two or more grades back" and from the lead's clarification. Each course then does something different with it:
   - **Grade 6** mostly follows the brief, but misses s3-weather-data.
   - **Grade 7** mixes the two: two grade 5 rows are checked and six are not.
   - **Grade 8** follows the gloss consistently.

   The hand-off cost lands on grade 8. Grade 6's wave, light-ray, Earth-sun-moon and geologic-time work skips grade 7 entirely, so grade 8 meets it two grades later with no check. Fix: replace the sentence in all three frames with the brief's wording, then re-sort the three seam tables in one pass. Where a unit has no spare minutes for a one-lesson reteach, the lead sets one band-wide rule rather than three local ones: a response inside the lesson that first uses the row, or a named condensation.
2. **Every course-level check claims every part of every listed code.** All six checks (grade 6 days 90 and 159, grade 7 days 67 and 159, grade 8 days 75 and 159) state full coverage in 40 to 50 minutes. Only grade 8's scope and sequence, for day 159, says plainly that the check is a sample. Fix: one wording for all six, a sample of named parts across units, since each end-of-unit assessment already covers its codes.
3. **Assessment time is booked as base time in all three years.** Grade 8 makes this visible because its source map carries minutes. Grades 6 and 7 label their end-of-unit days with base synthesis lessons in the same way, but their maps carry no minutes, so the loss cannot be measured. Each frame's statement of "base kept" therefore reads high.
4. **Three source-map schemas.** Grades 6 and 7 use `base_unit, base_lesson, base_days, stretch, unit, days, decision, reason, source_file`. Grade 8 uses `source_unit, source_lesson, base_days, stretch, day, decision, minutes, allocation, reason, source`. Only grade 8's minutes let a reader check the frame's minute budgets and catch days counted twice (grade 7 finding 3). Fix: grades 6 and 7 adopt the grade 8 columns, and the gate learns the one schema. This is a process matter for the lead.
5. **The cross-standard hand-offs work.** These threads land where the frames say, in order:
   - **MS-PS4-2:** grade 6 unit 1 rays, then grade 8 unit 2 sound reflected, absorbed and transmitted, then grade 8 unit 4 the wave model of light.
   - **MS-LS1-8:** grade 6 light and body systems, grade 7 smell, grade 8 unit 1 touch, then the grade 8 unit 2 synthesis.
   - **MS-PS3-5:** owned in grade 6, applied in grade 8 unit 3.
   - **MS-ETS1-2 and MS-ETS1-3:** started in grade 7 unit 2, completed in grade 8 unit 1.
   - **MS-LS1-2:** grade 7 unit 4, then grade 8 unit 5's whole-cell model.
   - **MS-LS1-5:** grade 7 unit 3, then grade 8 unit 5.
   - **MS-LS1-4:** begun in grade 8 unit 5 and owned in unit 6.

   Two threads are thin but planned: the senses synthesis that completes MS-LS1-8 is ten minutes, and grade 7's added MS-PS1-3 research shares its day with a base lesson.
6. **Stale frame day citations, same cause.** The grade 6 frame cites math and social studies ranges one day off the calendar. The grade 8 frame cites math 8 units 6 and 7 one day late. The grade 7 frame is clean. In both stale cases the scope and sequence used the calendar correctly, so only the frames need the edit.
7. **Held steady across the band.** Base order in all 18 units. No "+CS" variant used. Shorter path sections in all three. Readiness never on a unit's first day. Course-level checks that reach back to earlier units' content.

# Expert read: scope and sequence of Physical Education, grades 6 to 8 (2026-11-26)

Course `physical-education-grades-6-to-8`. A cold read by the curriculum expert (PRODUCTION-PATH step 3), done as
docs/pipeline/briefs/sequence-read.md says, with build/scope-writes/AFTERCORE-READ.md and AFTERCORE-BRIEF.md. I did
not write the scope; this file is the only file I changed.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/physical-education.md, docs/ADOPTION-BAR-SUBJECTS.md (the shared core
  and "4. Physical education" with its "Fails if"), docs/courses/physical-education/STANDARD.md and APPROACH.md in
  full, build/scope-writes/AFTERCORE-BRIEF.md, and docs/courses/sel/STANDARD.md section 7 ("Shared steps").
- docs/courses/physical-education-grades-6-to-8/scope-and-sequence.md and
  data/plans/physical-education-grades-6-to-8/days.csv (all 288 rows, goals and notes), read cold.
- Beside them: the frame (docs/courses/physical-education-grades-6-to-8/frame.md, all of it), the grade 3 to 8 rows
  of data/progressions/physical-education.csv (assumes checked by script), the span-8 lines of
  data/standards/shape-pe-2024.txt, docs/courses/CALENDAR.md (grades 6 to 8 rows), data/plans/calendar.csv (this
  course and every grade 6 to 8 course-level check day), and the earlier reads
  docs/reviews/frame-physical-education-grades-3-to-12-2026-11-25.md and
  docs/reviews/sequence-dance-grades-6-to-8-2026-11-26.md (for REPEAT tags).
- Gates: `scripts/sequence.py check` (0 failures), `scripts/frame.py check` (0 failures; 90, 90, 90), `scripts/plan.py
  check` (no failure for this course), `scripts/frame.py calendar` (no PE line), `scripts/stale.py check` (0
  failures). Short scripts over days.csv: all 61 owned ids sit on a teaching day and an end-of-unit row of their own
  year; the 64-session drops per year; each unit's main checked skill on kept practice days; codes claimed outside
  their year; each unit's assumed rows against its `retrieves` and readiness notes.
- Opened today: UNESCO's entries for kolo (2017, Serbia), the capoeira circle (2014) and Naadam (2010), and CDC's
  "Preventing Drowning" page (dated 2025-09-29). Not opened: a Colombian page for cumbia (the sensitivity agent's
  step), the safety guides (the safety agent's step).

## Verdict

Sound on the full 96-session path: every owned id is taught, practiced and checked in its own year, every unit moves
from cue to drill to small-sided game, the guards (no elimination, private fitness numbers, dry-land water, teacher-set
groups, cultural picks as candidates) are on the days they apply, and the checks sit on the pinned school days. The
biggest risk is the 64-session path: in units 4, 11 and 16 the skill the check watches first gets no practice day at
all, and several owned parts and the two "kept live" uses that grade 8's retrieval rests on are dropped with it. The
one change that matters most is to fold the main cue's practice into a kept day in each of those units (finding 1).

## Findings, most serious first

### 1. On the 64-session path the unit's main checked skill goes unpracticed

LAYER sequence. REPEAT yes (the same kind as the dance 6 to 8 read's finding 1: a reduced path that keeps the check
but not what it needs). Confidence: firm (counted from days.csv).

- **What is wrong.** The path keeps each unit's last Fluency and last Application day, but those days often practice
  the second skill. Counted on kept days:

  | Unit | Main checked skill (check day 1) | Kept Fluency on it | Kept Application on it |
  |---|---|---|---|
  | 4 | catch at three heights, "give" (day 46) | none (40 dropped; 43 is passing) | none (44 dropped; 45 is passing and conduct) |
  | 5 | dribble past a defender, "head up" (day 63) | none (56, 59 dropped; 61 is the stance) | 62 only |
  | 11 | mature long-tool swing, "rotate" (day 142) | none (136 dropped; 139 is placement) | none (138, 140 dropped; 141 is settling) |
  | 12 | serves, "toss, step" (days 159, 160) | none (152 dropped) | 158 only |
  | 16 | stick dribble, "stick low" (day 215) | none (206, 211 dropped) | none (210, 212 dropped) |

- **Why it matters.** A student meets the skill on one or two Understanding days and is then checked on it, against
  APPROACH "What is carried" and bar C7; the growth mark compares a baseline with a check that had no practice
  between. A teacher on the short path would see it the day of the check.
- **Fix** (no change to the 32 drops): on the 64-session path, day 43 opens with 10 minutes of catching at three
  heights on "give" (from day 40); day 59 folds into day 61 as it already does on the short year; day 139 opens with
  10 minutes of tee and soft-toss swings on "rotate" (from day 136); in unit 12 keep day 152 and drop day 153
  instead, with day 155 taking the short-tool strokes before its closure watch; day 211 folds into day 213 (10
  minutes of stick dribble past an active defender). Add to the Shorter path rules: "every unit keeps practice on its
  main checked cue on at least one kept day".

### 2. The 64-session path also drops owned parts and the two "kept live" uses

LAYER sequence. REPEAT new. Confidence: firm.

- **What is wrong.**
  - S2.8.8 asks movement ideas used on "dance and rhythm forms"; the only rhythm-form day, 166, is dropped.
  - S2.8.1: the tag game (day 58) is dropped, yet check day 64 asks about a pictured tag game.
  - S2.8.17: planning a week with rest days is practiced only on day 182 (dropped, as is 184), and check day 188
    asks exactly that.
  - S2.8.14's "training" part is practiced only on day 19 (dropped); see finding 3 too.
  - S4.8.3: the activity record is finished on day 75 (dropped); the check asks which kind fits best.
  - g6-catch-form is kept in use only on days 102 and 138, both dropped, so grade 8's unit 19 retrieves a row last
    used two grades back with no readiness check (rule 2). g6-rules-safe's use on day 178 is dropped; day 186 takes
    the map-and-pace briefing but not the rules.
- **Why it matters.** The brief asks the reduced path to cut no assessed or owned part; these are each asked on a
  kept check day.
- **Fix.** On the 64-session path: day 170 adds the rhythm form changed with a contrast (10 minutes); day 62 opens
  with a 10-minute no-one-out tag round naming the idea; day 186's return holds the week with rest days (10
  minutes); day 21 adds static holds inside its short training block; day 76 finishes the activity record (5
  minutes); the catch cue check moves to days 105 and 141; day 186's note and `retrieves` carry g6-rules-safe with
  the briefing.

### 3. Three check items do not ask the whole of their code

LAYER sequence. REPEAT yes (the dance 6 to 8 read's finding 6, items naming codes they ask only in part).
Confidence: likely.

- **S2.8.14** (warm-ups, cool-downs and training): day 23's task asks a warm-up and a cool-down only. Fix: add one
  prompt, "a stretch for the end of a training block: dynamic or static, and why".
- **S2.8.11** (FITT, progression, overload and specificity across activities): day 131's "change a plan for a
  different goal" can be answered with one principle, and day 129's closure watch takes overload or progression.
  Fix: a prompt per part on day 131: which FITT part changed, whether the change is overload or progression, how the
  plan now fits the goal (specificity), and the second activity it applies to.
- **S2.8.7** (methods in many games): day 229 asks for one change and its result. Fix: day 229 collects both method
  records (day 224, net game; day 226, invasion game) and asks which change worked in each.
- Smaller: unit 2's one check day asks a ten-item sort, a warm-up and a cool-down in the 5-minute knowledge slot.
  Settled below: 8 minutes, from the instant activity.

### 4. Four readiness checks are on rows the progression uses the year before

LAYER frame (carried into the sequence). REPEAT new. Confidence: firm (from the progression's assumes).
This disagrees with the frame read of 2026-11-25, which held the g4-pulse-body readiness.

- **What is wrong.** By the progression, g4-pulse-body is last used by grade 5 rows (g5-fitt, g5-tech,
  g5-food-drink); g4-reasons-strengths by g5-goal and g5-review-experiences; g5-conflict-solve by
  g6-welcome-differences (retrieved on day 39); g5-review-experiences by g6-express-variety (retrieved on day 67).
  Each is a year-before row for the unit that leans on it, so rule 2 asks a retrieval task, not a readiness check.
  The frame counts them "by row" grade instead.
- **Why it matters.** Four 10-minute checks probe rows students used last year; the result tells the teacher little,
  and the retrieval the rule asks for is missing.
- **Fix.** Days 24, 79, 132 and 147 lose their readiness checks (respond time only). The retrievals go into: day 25's
  instant activity (find a pulse; unit 3's hook needs it), day 81 (with g5-goal), day 135 (with health's conflict
  steps) and day 151 (managing feelings, which needs it). The lead updates the frame's Readiness bullet and the Seams
  rows to match.

### 5. Three assumed rows have no retrieval task

LAYER sequence. REPEAT yes (the dance 6 to 8 read's finding 5). Confidence: firm.

- Unit 3 assumes g5-fitt (frame Seams: retrieval in unit 3); only unit 2 retrieves it. Fix: day 26's retrieval adds
  grade 5 FITT (which exercise raises which part).
- Unit 5 assumes g5-invasion-skills (dribbling); day 53 retrieves defending ideas, problem solving and passing. Fix:
  add the grade 5 dribble to day 53.
- Unit 9 assumes g6-strike-net-toward for its volley station (frame "Inside the band"). Fix: day 113's instant
  activity retrieves unit 7's forehand and serve.

### 6. A shorter period is not planned

LAYER sequence. REPEAT new for after-core PE. Confidence: firm (sequence-write.md, the "Shorter path" item).

- **What is wrong.** The Shorter path section covers 64 sessions and the 10-days-short year, but not a period under
  45 minutes, which sequence-write asks for and which many middle schools run.
- **Fix.** Add "A shorter period": on 35 to 40 minutes, instant activity 4, warm-up 4, focus 15, cool-down 2, closure
  3, equipment 4, so at least half stays moving; two-day checks are unchanged (rotation of six groups at about 3.5
  minutes, 21 minutes); one-check-day units (2, 15, 18, 21, 22) drop the focus block and hold a 3-minute warm-up, the
  21-minute rotation and the knowledge task.

### 7. Codes claimed in the wrong year

LAYER sequence. REPEAT new. Confidence: firm.

- The .md says a year claims only its own rows and a later use is written with `~`, but eleven check rows carry an
  earlier year's S3 code bare: days 131, 188 (S3.8.7), 173 (S3.8.2) in grade 7; 216, 229, 242, 254 (S3.8.9), 239,
  266 (S3.8.7), 273 (S3.8.2), 284 (S3.8.1) in grade 8. A coverage count would credit grade 8 with grade 7's conduct.
- Fix: write each as `~SHAPE...` (the conduct "review" the notes already name).

### 8. Marking slips in the reduced paths

LAYER sequence. REPEAT yes (the dance 6 to 8 read's finding 4, folds into the wrong day). Confidence: firm.

- Day 209 "folds into day 209" and day 280 "folds into day 280": the target cannot be told. Fix: 209 into 211, 280
  into 282.
- Day 169's note lacks "64-session path: dropped", so days.csv drops 31 days in grade 7, not the table's 32. Fix:
  "64-session path: dropped; the fix is tested on day 171 instead."
- The Shorter path says no first-teaching day is cut, but Understanding days 83, 113 and 178 are; they are the
  begun-toward days the frame says to drop first. Fix the sentence to say so.

### 9. Guards and accuracy notes

LAYER sequence (one frame item). REPEAT new. Confidence: likely.

- The .md's Sensitivity section omits two frame guards: the puberty line (a quiet role change or restroom break with
  no reason asked aloud) and health's disclosure steps on every teacher page. The frame's "every small-sided game
  offers a more and a less competitive court" is on some game days only (6, 42, 62, 86, 104, 117, 141, 154, 212,
  222, 249) and not stated course-wide. Fix: one line each in "How the band runs".
- Math grade 6 unit 2 ends on school day 39, the day unit 3 opens with beats per minute; "finished first" is a
  same-day finish. Fix: day 25's note uses the If-later wording ("beats in a minute") and ratio words from day 26.
- CDC's "Preventing Drowning" page (opened) covers life jackets, swimming skills, the buddy system and natural-water
  risks but not reach or throw rescues, which unit 21 cites it for. Fix: day 268 marks the rescue steps "from
  memory" until the safety agent names a free source for them.
- Naadam (UNESCO, opened): three games (horse racing, wrestling, archery) with ritual songs and costumes. Day 279's
  read-only case card names the rituals and imitates none.
- Frame item for the lead: unit 9's stick station (day 113) is not on the frame's safety-read list.

## The writer's "For the lead" items

1. 64 at 32 a year: agreed, once finding 8 marks day 169; findings 1 and 2 keep 32 with folds.
2. Grade 8 mid-year and unit 15 carried by collect once: agreed; the frame's check row should say so.
3. Codes no check samples: the reasons hold.
4. Confirmations: UNESCO kolo and capoeira pages opened today, so those browser checks close (kolo is taught in the
   regular school system, by its entry). Naadam opened (2010). Cumbia's Colombian page and capoeira's sensitivity
   read stay open.
5, 6. Agreed; `frame.py calendar` shows no break.

## What is right and should not be touched

- Owned ids by year (every id taught and checked in its own year), the baseline-to-check growth marks, and closure
  watches on Fluency days, never on first-teaching days.
- Unit 15's held retest with the plan in every warm-up, the private plot, and the collect-once carry.
- Dry-land water, private counts, no BMI or weight, invented tool and community cards, free options first.
- The shared cards quoted word for word in the 6 to 8 form; cultural picks named as candidates until confirmed.
- The pinned check days (76 and 77, 73 and 74, 157 and 159) on CALENDAR.md's weeks.

## Lens checklist (scope and sequence)

| Line | State |
|---|---|
| A year of games with no outcomes | Met: grade outcomes per standard per year |
| A grade with no outcome for one standard | Met |
| A span indicator placed in no year | Met: all 61 |
| Skills out of developmental order | Met (first tries in grade 6 and 7, owned a year later) |
| Dance or fitness taught once | Met: dance units 6, 13, 18, 22; fitness 2, 3, 10, 14, 15, 18 |
| Most of the class moving | Met on 45 minutes; finding 6 for shorter periods |
| Assessment shows growth, no rank | Met |

## What I could not judge

Whether the cumbia basic step and the ginga cue match the communities' own teaching (sensitivity agent), and the
safety facts the safety guides will settle.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| 64-path folds: 40 into 43, 59 into 61, 136 into 139, 211 into 213; unit 12 keeps 152 and drops 153 | Main checked cue gets practice (finding 1) | days.csv notes; .md table |
| 64-path additions on days 21, 62, 76, 105, 141, 170, 186 | Owned parts and kept-live uses stay (finding 2) | days.csv notes |
| Prompts added on days 23, 131, 229 | Whole code asked (finding 3) | days.csv goals |
| Unit 2's knowledge task 8 minutes, from the instant activity | Load of the one-day check | days.csv day 23 note |
| Readiness on days 24, 79, 132, 147 becomes retrieval on days 25, 81, 135, 151 | Year-before rows (finding 4) | days.csv; frame wording to the lead |
| Retrievals added on days 26, 53, 113 | Assumed rows (finding 5) | days.csv `retrieves` |
| Eleven bare S3 codes written with `~` | Year claims (finding 7) | days.csv codes |
| Folds 209 into 211, 280 into 282; day 169 marked dropped | Marking (finding 8) | days.csv notes |

## For the lead (not Cory)

- Frame: update the Readiness bullet and Seams rows for finding 4; add unit 9 to the safety-read list; reword the
  grade 8 mid-year check row to carry unit 15 by collect once.

## For Cory

None.

## For the source list

- UNESCO ICH entries opened directly on 2026-11-26 with no verification wall: kolo
  (https://ich.unesco.org/en/RL/kolo-traditional-folk-dance-01270), capoeira circle
  (https://ich.unesco.org/en/RL/capoeira-circle-00892), Naadam
  (https://ich.unesco.org/en/RL/naadam-mongolian-traditional-festival-00395).
- CDC "Preventing Drowning" (https://www.cdc.gov/drowning/prevention/index.html): no rescue technique content.

# Expert read: scope and sequence, Health, grades K to 2 (2026-11-26)

Reader: the Curio Class curriculum expert agent (docs/agents/EXPERT.md), reading as a K to 2 classroom teacher who
teaches health. Cold read: I did not write the scope and sequence or the days.

## What I read

- The job: build/scope-writes/AFTERCORE-READ.md, docs/pipeline/briefs/sequence-read.md, build/scope-writes/AFTERCORE-BRIEF.md
  and the parts of docs/pipeline/briefs/sequence-write.md on columns, checks and "each part of each code".
- docs/agents/EXPERT.md; the lens docs/agents/lenses/health.md.
- Under review: docs/courses/health-grades-k-to-2/scope-and-sequence.md and data/plans/health-grades-k-to-2/days.csv
  (all 84 rows).
- Beside them: docs/courses/health-grades-k-to-2/frame.md (whole); data/progressions/health.csv (every K, 1 and 2
  row: standard, assumes, model_in, model_out); data/standards/nhes-2024.txt (the 33 PreK-2 ids, our words);
  docs/courses/sel/STANDARD.md section 7 ("Shared steps"); docs/courses/social-and-emotional-learning-grades-k-to-2/frame.md
  (its health seam and units table); docs/courses/CALENDAR.md (rule 1 and the generated table); data/plans/calendar.csv
  rows for health, PE and SEL K to 2; data/plans/frames.csv row for this course.
- Earlier reads: docs/reviews/frame-health-grades-k-to-2-2026-11-25.md (findings and fact spot checks) and
  docs/reviews/sequence-computer-science-grade-1-2026-11-26.md (for REPEAT tags).
- Gates run first: `scripts/plan.py check` (no failure for this course), `scripts/frame.py calendar` (health K weeks
  12 and 27, grades 1 and 2 weeks 11 and 27; no stagger break), `scripts/sequence.py check health-grades-k-to-2` (0
  failures), `scripts/frame.py check health-grades-k-to-2` (0 failures; 17 units, 84 days, 24 unit days a year),
  `scripts/stale.py check` (nothing for this course).
- Sources opened today: CDC adult tobacco data page; CDC vaccines for children page (see Sources).

## Verdict

The scope and sequence is sound and close to ready: every one of the 33 owned ids sits on a teaching day in its owner
year, unit day counts and weeks match the frame and CALENDAR.md, every assumed row from the year before opens as a
retrieval in the right unit, and the sensitive units carry their family notes, leave-out notes, scripts and
disclosure steps. The biggest risk is assessment validity: several end and check items ask only part of the code they
claim (listening in different places, honoring others' limits, the "hurt" half of NHES.S1.2.3, "own" strengths), and
in four units the step card is first taken away on the scored day, with the said-aloud hearing taken under two
conditions. The one change that matters most is to write a prompt per part on the named check days and turn the card
over in the last rehearsal before each check; both cost no day.

## Findings, most serious first

### 1. Check items ask only part of their code (moderate; LAYER sequence; REPEAT yes)

**What is wrong.** Rule "each part of each code" (sequence-write.md) and "checks claim only what they sample":
- **NHES.S4.2.2** (practice listening carefully in different places). Days 18 and 27 claim it with "a listening step"
  picked from a pictured scene. That is recognition, not practice, and one place, not "different places". The
  said-aloud record in unit 3 hears the I-statement only.
- **NHES.S4.2.5** (act with kindness and care). Days 17, 18 and 27 claim it with "pick the kind act". Picking is not
  acting; day 17 is `observe` but the observation hears only the I-statement.
- **NHES.S4.2.4** (speak about personal limits and honor one's own and others'). Days 73, 74 and 83 ask the boundary
  steps for a character (own limit). No prompt asks what to do when someone else says stop.
- **NHES.S1.2.3** (lower the chance of getting sick or hurt). Days 39 and 55 claim it with "a germ-stopping action"
  only; the "hurt" half is not asked. (Day 32 does ask both, through the protection match.)
- **NHES.S1.2.1** (tell which of their own strengths help them stay healthy) and **NHES.S2.2.2** (how those things touch
  their own health). Days 32, 39, 45 and 55 ask for a character's strength or how a thing touches a character. The
  course's rule keeps disclosure out, but a strength here is a safe action (washing, being kind), and "how could a
  late night touch you?" is a hypothetical that asks for no history.
- **NHES.S1.2.6** (home, school and neighborhood surroundings). Day 45 asks only about a shared place.
- **NHES.S2.2.3** (how the same things touch other people). Days 74 and 83 name the item "listen before judging"; a
  busy item writer can build a listening item and miss the "other people's health" part.
- **Observe days list codes they do not observe:** day 17 lists NHES.S4.2.5, day 37 lists NHES.S4.2.3; each hears
  only the I-statement or the help request.

**Why it matters.** The unit planner writes items from these cells; as written, the K listening and kindness
indicators and the grade 2 "honor others' limits" half will never be assessed, and the grade 3 teacher receives
results that claim them.

**Fix (no day added).** Day 18: the side-table hearing also marks "says back" after the child listens to the teacher
read one line, and the pictured item shows two places (circle, lunch table) with a prompt each; day 27 keeps the two
places. Days 18 and 27: "show or say one kind thing to do for this character" (said, pointed or acted with a puppet)
in place of "pick the kind act". Days 74 and 83: add "A friend says stop. What do you do?" as its own prompt. Days 39
and 55: add one "hurt" prompt (a helmet or sun scene). Days 32 and 39: "Point to one strength card that is yours" (the
cards are actions only). Days 45 and 55: "How could this touch you if it happened?" beside the character item.
Day 45: the place prompt shows a home, a school and a street scene (all pictured, none the child's own). Days 74 and
83: rename to "how the same thing touches another character". Day 17 `codes`: NHES.S4.2.1 only on the observe slot, or
the note says the observation records NHES.S4.2.1 and the rest is teaching; day 37 likewise (NHES.S3.2.2 and
NHES.S8.2.1). Confidence: firm (the id text in data/standards/nhes-2024.txt and the brief's rule agree; the frame read
of 2026-11-25, finding 4, found the same S4.2.2 gap at the frame layer).

### 2. The step card is first withdrawn on the scored day, and the said-aloud hearing runs under two conditions (moderate; LAYER sequence and frame; REPEAT new)

**What is wrong.** The frame's unit shape says the card is withdrawn on the first application day and the check is
taken without it. The scope has one Application day in the band (day 43) and says so; in units 2 (day 11), 6 (day
32), 7 (day 38) and 14 (day 74) the card is first taken away on the check day itself, and units 3, 12, 13 and 15 do
not say when it goes. In units 7 and 14 a third of the class is heard on the Fluency day (37, 73) while pairs "hold
the card", and the rest on the check day "without the card", so one record sheet mixes two conditions.

**Why it matters.** A five-year-old meeting the task without the card for the first time on the scored day is
measuring the withdrawal, not the skill; and the said-aloud record cannot be compared child to child.

**Fix (no day added).** In each unit, the five-minute pair rehearsal on the day before the check is done with the
card turned over (days 10, 17, 23 already, 31, 37, 44 already, 49, 60, 65, 73, 77), and the note says so. On days 37
and 73 the ten children are heard with the card turned over, as on days 38 and 74. The md's "Day kinds" paragraph
says this once; "For the lead" item 2 adds the frame wording "withdrawn in the last rehearsal before the check".
Confidence: likely (gradual release from memory; the frame's own unit-shape bullet).

### 3. Twice-a-week path breaks the body-names notice and the goal week (moderate; LAYER sequence; REPEAT yes)

**What is wrong.** The "Twice a week for half the year" path keeps the day order: day 1 (body-names family note) and
day 3 (body names) then sit one week apart (kindergarten weeks 15 and 16), not the two weeks the frame requires for
preview and opt-out. The path also says "the unit 15 goal still runs at least one full week between lessons" without
saying how: at two lessons a week, days 76, 77 and 78 sit in weeks 26, 27 and 27, so the "one more week" after day 77
does not happen.

**Why it matters.** The body-names notice is a sensitivity guard Cory set (2026-11-21); a school following this path
would give families one week.

**Fix.** Add to the path: "The body-names family note goes home two weeks before day 3 (kindergarten week 14, before
the course starts), with the day 1 home task." And: "Days 77 and 78 are each moved one week later, keeping the week's
other lesson for a respond-style re-rehearsal, so the goal runs a week before the look-back and a week before the
check." Check the grade 2 checks still land on weeks 22 and 30 after that move (they do: day 83 is not moved).
Confidence: firm (arithmetic from the path's own formula).

### 4. Leave-out paths and opt-outs have gaps (moderate; LAYER sequence; REPEAT new)

**What is wrong.**
- Grade 1 with both units 10 and 11 left out is not written (grade 2 has its "both out" case). By the frame, unit 9
  gains two days and unit 8 gains two; unit 9 then ends in week 26 and the year-end check in week 27 comes right after
  its end, so its unit 9 items must come from earlier content.
- "Unit 17 out" says unit 14 gains two days "the same way" but does not say that unit 15 and 16 move (to weeks 21 to
  24 and 25 to 26) or where unit 16's family note then goes.
- Two family notes go home on a sensitive unit's day: unit 11's on day 51 (unit 10) and unit 17's on day 79 (unit 16).
  Where unit 10 or 16 is left out, nothing says the note still goes that week.
- Where one family opts out (the school keeps the unit), days 25, 51, 53, 79 and 81 do not say what the child does.
  Day 3 does (washing rehearsal with another adult).
- Day 81 (growing bodies, privacy) carries no disclosure steps; days 3, 25, 51 and 79 do.

**Why it matters.** The leave-out rule is what makes these units removable (STANDARD.md section 5); a teacher in a
school that removes two units, or a child whose family opts out, needs the plan written down.

**Fix.** Add the grade 1 "both out" bullet (unit 8 weeks 13 to 19, unit 9 weeks 20 to 26, year-end items for unit 9
drawn from unit 8 scenes, unit 11's family note dropped). Spell out the unit 17-only shift. Add: "A family note that
falls on a left-out unit's day still goes home that week." Add to each sensitive day's note: "A child opted out does
a help-steps picture sort with another adult." Add "Disclosure steps as in unit 5" to day 81's note. Confidence:
firm.

### 5. Two ten-days-short folds overload a day or move the norm onto a check day (minor; LAYER sequence; REPEAT yes)

**What is wrong.** Folding day 64 into day 63 puts the emergency rule with every child's toy-phone practice, four rule
areas with reasons, the fire scene and two retrievals into one 30-minute grade 2 lesson. Folding day 31 moves the
grade 1 norm to day 32's opening, a check day, where the frame puts each year's norm on an Understanding day.

**Fix.** Grade 2: fold day 73 (Fluency, practice only) instead of day 64: its rehearsal becomes the five-minute pair
rehearsal of days 72 and 74, and the ten-child hearing moves to day 72's last ten minutes, card turned over. Grade 1:
keep the day 31 fold but state the norm at day 30's close from the washing tally ("most of our class washed before
snack this week"), which the routine record has from day 29. Confidence: likely.

### 6. "By color" on day 6 can be read as a traffic-light food label (minor; LAYER frame and sequence; REPEAT new; judgment call)

**What is wrong.** Day 6 names "foods that help us grow and foods to have less often, by color". Many classroom
materials use green, yellow and red "go, slow, whoa" food labels, which are good-and-bad labels in another form; the
lens bars good and bad foods.

**Fix.** Day 6 note: "by color means a rainbow of fruit and vegetable colors on the plate; no red, yellow or green
food labels". Confidence: judgment call.

### 7. The leans table misses four SEL rows and one same-year overlap (minor; LAYER sequence; REPEAT new)

**What is wrong.** The SEL K to 2 frame's health seam lists k-rel-talk-listen (SEL first, the talk turn card),
k-sm-set-goal (health first, SEL K unit 6, weeks 27 to 32), g1-rds-solve-problems (the I-statement, a year after
health K) and g2-sm-set-goal (health first, SEL unit 17, weeks 21 to 26). The scope names two of them in notes but
not in "Leans on the calendar", and g2-sm-set-goal nowhere. Separately, SEL grade 1 unit 11 ("Families, friends and
me", weeks 21 to 26) runs beside health's sensitive unit 11 (weeks 25 to 26); neither course names the other.

**Fix.** Add the four rows to the leans table. Under "For the lead": "SEL grade 1 unit 11 and health unit 11 meet
families in the same weeks; confirm SEL keeps to groups and friendships (no family-structure content) so health's
opt-out holds, and each names the other." Confidence: firm for the rows (calendar.csv and the SEL frame); judgment call
on the overlap.

### 8. Shared card words not quite word for word (minor; LAYER sequence; REPEAT new)

**What is wrong.** SEL STANDARD section 7: the goal card's first rung is "my goal and one step"; the scope writes "my
goal, one step" (md and day 10). Grade 2's I-statement adds asking "What do you need?" "and a fair end"; the md and
day 70 drop "a fair end". The grade 1 rung "a helper and a check" is quoted on day 49, but no grade 1 day teaches the
check.

**Fix.** Use "my goal and one step"; add "and agree a fair end" to day 70 (it meets the conflict steps' "find a fair
way" on day 72); day 49 adds "and when we will check" as the plan's last line. Confidence: firm.

### 9. Small day fixes (minor; LAYER sequence and frame; REPEAT new)

- **Day 30, germs.** "Tiny living things" is not true of viruses. Say "germs are too small to see; some can spread
  from person to person and make people sick". Confidence: likely.
- **Day 32, doing record.** Covering a cough cannot be seen in every child on demand. The note should say the record
  judges the routines every child does daily (washing before snack, own cup), with cough covering marked when seen,
  not required. Confidence: likely. (Frame layer: the frame's unit 6 cell says the same three routines.)
- **Day 36 load.** Decision step 2 with its model, the medicine helpers, the found-vape scene, three retrievals and a
  self-check in 30 minutes. Fold the three retrievals into one opening picture ("I have a choice: leave it and tell")
  rather than three tasks. Confidence: judgment call.
- **Day 71.** g2-v-my-limits-say-stop takes the I-statement in (model_in); the note does not name it. Add "the
  I-statement opens the 'say it' step".

## Facts checked

| Fact on a day | Checked at | Holds |
|---|---|---|
| "Most grown-ups do not smoke or vape" (days 23, 65) | CDC adult tobacco data page, dated 2024-09-17: 19.8% of US adults used any tobacco product in 2022 | Holds: about four in five adults use no tobacco product, vapes included. The unit plan dates it to that 2022 figure |
| "Vaccines help protect people" (day 58) | CDC vaccines for children page, dated 2024-08-09 | Holds. Federal vaccine pages have changed since 2025; the expert read at unit plan should also check a national pediatrics association's page, so the fact does not rest on one site |
| Hand washing, about 20 seconds, a song twice (day 2) | Frame read 2026-11-25 at CDC "Clean Hands" | Holds |
| Car seat and booster pages (day 22); Poison Help pages (day 23) | Not opened (403 to the fetcher at the frame read) | Browser check |
| 911 when no adult can help; "get out, stay out"; "stop, drop and roll" (days 63, 64) | From memory | Hold as standard US guidance; the safety read opens the fire service page |

## Lens checklist (scope and sequence layer)

| Line | Result |
|---|---|
| Band reaches all eight standards | Met (each year, with sensitive units out) |
| Each skill standard practiced in two or more topics | Met, as the frame counts it |
| Coverage map with units in its cells | Met |
| A topic taught once in the band with nothing after | Met: tobacco and AOD alternate years with practice between |
| Sensitive unit removable (no skill only there, no later unit needs it, leave-out note) | Met in design; finding 4 for the written paths |
| Getting help taught outside the sensitive units | Met (units 4, 7, 13) |
| Indicators claimed in the wrong span | Met: none |
| Health reteaching a science model; health and PE both planning one lesson | Met: leans named, heart fact in one line |

## Checked and right (do not touch)

- **Owned ids.** 10, 14 and 9 ids, each in its owner year; codes only practice ids owned earlier; sensitive days
  claim none.
- **Order.** Each unit builds day on day; the found-vape scene moved to day 36 so its kindergarten retrieval comes
  first; decision steps 1 to 4 run K unit 4, grade 1 units 7 and 8, grade 2 unit 12 in order; the goal thread runs
  units 2, 9, 15.
- **Retrieval.** Every assumed row of the progression is the year before and opens as a retrieval in the unit that
  needs it, in the `retrieves` column; no readiness check is needed.
- **Calendar.** school_day 5(n - 1) + 3 by year puts every unit on the frame's weeks and every check on 12 and 27, 11
  and 27, 11 and 27; health and SEL checks never share a week.
- **Checks that do not repeat.** The three mid-year checks say they draw the just-ended unit's items from earlier
  content; collect-once records are carried.
- **Sensitive care.** Body-names guards from Cory's 2026-11-21 call kept in full; family notes two weeks ahead on
  named days; scripts only; no child plays a person who pressures.
- **Candidates.** All 17 settled at 0 days or dropped with a reason ("know my address").

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Prompts per part on days 18, 27, 32, 39, 45, 55, 74, 83, and observe-day codes cut to what is heard (days 17, 37) | Each part of each code (finding 1) | days.csv; scope-and-sequence.md |
| Card turned over in the last rehearsal before each check; days 37 and 73 hearings without the card | One condition for the record (finding 2) | days.csv; scope-and-sequence.md |
| Twice-a-week path: body-names note two weeks before day 3; days 77 and 78 each a week later | Keeps the notice and the goal week (finding 3) | scope-and-sequence.md |
| Grade 2 fold-in day 73 replaces day 64; grade 1 norm on day 30's close in the fold | Load and norm placement (finding 5) | scope-and-sequence.md |
| Day 6 "by color" means a rainbow plate, no traffic-light labels | No good or bad foods (finding 6) | days.csv |
| Goal card "my goal and one step"; grade 2 I-statement "and agree a fair end"; day 49 check line | Word for word (finding 8) | days.csv; scope-and-sequence.md |
| Day 30 germ wording; day 32 record names daily routines; day 36 one opening retrieval; day 71 names the I-statement | Accuracy, observability, load (finding 9) | days.csv |

## For Cory

None. Every finding sits inside the standards' limits or is for the writer or the lead.

## What I could not judge

- The HECAT 2021 topic modules' PreK-2 expectations were not opened; every kept Candidate stays conditional on them,
  as the scope says.
- The NHTSA and Poison Help pages (browser check).
- Whether SEL grade 1 unit 11 holds family-structure content (finding 7) needs that unit's scope.

## Sources

- CDC, adult tobacco product use data page (https://www.cdc.gov/tobacco/php/data-statistics/adult-data-cigarettes/index.html): the 2022 adult tobacco use figure behind the norm.
- CDC, vaccines for children (https://www.cdc.gov/vaccines-children/about/index.html): the plain vaccine fact.
- docs/reviews/frame-health-grades-k-to-2-2026-11-25.md: hand washing and body-names checks at source.
- data/standards/nhes-2024.txt: id text in Curio Class words, for each-part checks.

## For the source list

- The CDC adult tobacco data page address above is not in docs/APPROACH-SOURCES.md; it is the source the norm days
  should cite.

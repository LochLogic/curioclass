# Expert read: scope and sequence of Physical Education, grades 3 to 5 (2026-11-26)

Cold read by the curriculum expert (PRODUCTION-PATH step 3), on docs/pipeline/briefs/sequence-read.md and
build/scope-writes/AFTERCORE-READ.md. I did not write the scope; a fresh Claude agent did.

## What I read

- The scope and sequence (docs/courses/physical-education-grades-3-to-5/scope-and-sequence.md) and all 240 rows of
  data/plans/physical-education-grades-3-to-5/days.csv, cold.
- Beside them: the frame (frame.md, whole), the grade 3 to 5 rows of data/progressions/physical-education.csv,
  docs/courses/CALENDAR.md and the grade 3 to 5 rows of data/plans/calendar.csv, the span-5 lines of
  data/standards/shape-pe-2024.txt, build/scope-writes/AFTERCORE-BRIEF.md.
- The bar: docs/ADOPTION-BAR-SUBJECTS.md section 4, docs/courses/physical-education/STANDARD.md and APPROACH.md, the
  lens docs/agents/lenses/physical-education.md, docs/agents/EXPERT.md.
- To check leans and shared cards: SEL STANDARD section 7, the SEL 3 to 5 frame and scope, and the days.csv of SEL 3
  to 5, health 3 to 5, dance 3 to 5 and PE K to 2 (for last use of the readiness rows).
- Earlier reads: docs/reviews/frame-physical-education-grades-3-to-12-2026-11-25.md and
  frame-physical-education-grades-3-to-5-codex-2026-11-25.md.
- Gates: `plan.py check` lists no physical education 3 to 5 failure; `frame.py calendar` shows no break for this
  course; `sequence.py check` 0 failures; `frame.py check` 0 failures (unit days 74 a year, 24 units, 240 days);
  `stale.py check` 0 failures.
- Opened at source: CDC "Preventing Drowning" (cdc.gov/drowning/prevention/index.html, dated 2025-09-29), and
  encyclopedia entries for Pilolo, jianzi and the Virginia reel.

## Verdict

The scope is sound and close to ready. It follows the frame faithfully, every owned code sits on a teaching day and an
end-of-unit check in its owner's unit, the checks sit on CALENDAR.md's weeks 18 and 26 in all three years, and the
values rules (no elimination, no human targets, private fitness data, no body talk) hold on every day. The biggest
risk is a group of end-of-unit checks that ask less than the code they claim (one dance style for "several dance
styles", one rope task for "several practice tasks", no prompt for "name activities that raise your heart rate"),
together with a short path that cuts the four to six weeks S4.5.6 asks for. The one change that matters most is to add
the missing prompt per part to the seven checks in finding 1.

## Findings, most serious first

### 1. Seven checks ask less than the whole code they claim (serious)

- **What is wrong.** The day names the code but the task covers only part of it:
  - Day 89 (unit 9) and day 124 (grade 4 mid-year) claim SHAPE.S2.5.12, "find your pulse **and name activities that
    raise your heart rate**". Both ask only for the pulse and a body change (that is S2.5.14). No prompt names
    activities that raise the heart rate.
  - Day 152 (unit 15) claims S1.5.5, a sequence "in several dance styles". The skill task is one sequence to the beat.
    The unit taught three styles (the line dance, La Bastringue, the ribbon routine), but the check sees one.
  - Day 71 (unit 7) claims S1.5.6, jumping rope "through several practice tasks". The skill task is ten jumps in one
    task of the child's choice.
  - Days 20 and 21 (unit 2) claim S1.5.10 and S1.5.12. The row and day 14 teach overhand and underhand throws and
    catches at low, middle and high levels; the check watches overhand throws only and "three of five catches" with no
    level named (the mid-year check, day 43, does name two heights).
  - Day 99 (unit 10) claims S1.5.17, pass and gather. The row teaches hands and feet, standing and moving; the check is
    "five passes in a row in a pair", which a writer will build as standing chest passes.
  - Day 159 (unit 16) claims S3.5.7, "describe movement activities from cultures around the world". The knowledge task
    describes one activity from one place.
- **Why it matters.** A unit plan writer builds the check exactly as the day says, so the code is reported as met
  with a part never seen. The bar's criterion 1 asks for an assessment of each outcome; the brief asks a prompt per
  part.
- **Fix** (all inside the existing check days and minutes; settled below):
  - Day 89 knowledge task: add "names two activities that raise the heart rate". Day 124: add the same prompt.
  - Day 152 skill task: "a sequence with a clear beginning, middle and end in two of the unit's styles (the line dance
    and La Bastringue or the ribbon routine), each marked apart"; the second may be the last Fluency day's closure
    watch (day 151), carried, as the frame allows.
  - Day 71 skill task: "ten jumps in a row against the child's own first count in two tasks: self-turned forward, and
    one other of the child's choice (backward, step-and-jump, long rope or partner rope)", each marked apart.
  - Day 21: add "an underhand throw to a hoop" beside the roll, marked apart; day 20: "three of five catches, at a
    middle and a high level".
  - Day 99: "five passes in a row in a pair, the partner moving a few steps, with the hands; then three with the feet".
  - Day 159 knowledge task: "describes both games, how each is played and where each comes from".
- LAYER sequence. REPEAT yes (checks asking part of a code is the commonest finding in earlier sequence reads).
  Confidence: firm (code text against the day text).

### 2. The 64-session path cuts S4.5.6's four to six weeks (serious)

- **What is wrong.** g5-goal owns S4.5.6, a visible goal "for a longer stretch of time", which the row sets at four to
  six weeks with a check each week. On the full path the goal runs from the baseline on day 163 to the check on day 172:
  nine sessions, about 3.6 weeks at 2.5 a week, which the frame calls "about four weeks". The short path drops days 165,
  167 and 169, all between the baseline and the check, and runs at 2 sessions a week, so the goal shrinks to six
  sessions, about 3 weeks, and loses the weekly goal checks, which sit only on days 165 and 169.
- **Why it matters.** The short path's own rule is "nothing assessed and no owned part cut". A three-week goal with
  one weekly check does not meet the part of S4.5.6 that makes it a longer-term goal.
- **Fix.** (a) Put the weekly goal check in the warm-up of every unit 17 day from 164 to 171, not only on the Fluency
  days, so a dropped day never takes the week's check. (b) On the 64-session path drop only day 167 in unit 17 (its bar
  graph moves to 171, as written) and take the two other drops from day 219 (unit 22, Application) and day 200 (unit 20,
  Application, its card folding into day 201's opener), under the same extension the scope already asks for in its For
  the lead 1. That keeps seven sessions between baseline and check, about four weeks at 2 a week. Update the Shorter
  path table and the "Units at three drops" line (unit 17 then loses one day).
- LAYER sequence. REPEAT yes (short path arithmetic, the frame reads' finding 2). Confidence: firm (arithmetic).

### 3. The four-step goal steps card is used in grade 3 week 15, before SEL grows it in week 27 (moderate)

- **What is wrong.** Day 36 (unit 4, school day 72, week 15) uses "the goal steps card in SEL's grades 3 to 5 words:
  goal, steps, block and plan, check". SEL 3 to 5 grows the card to those four steps on its day 54 (school day 134,
  grade 3 week 27, unit 6). Day 67 (unit 7) lands the same school day as SEL day 54. The calm-down and talk turn cards are
  placed correctly after SEL (SEL days 4 and 33, weeks 2 and 17).
- **Why it matters.** The shared-card rule is one card in every course, met first where the band's frames say. Here PE
  silently teaches the grown card first, with no bridge, and SEL then "grows" a card children already have. A writer of
  day 36 has no words for the block-and-plan step.
- **Fix.** Day 36 and day 67 use the goal steps card in the form the class already knows from K to 2 grade 2 (retrieved
  from g2-goals: my goal and one step, a helper and a check, a changed step), and the four-step grade 3 to 5 form from
  grade 4 on (days 137 and 163). Change "units 4, 7, 14, 17" in the .md's Shared cards bullet to say so.
- LAYER sequence. REPEAT new. Confidence: firm (both days.csv files).

### 4. Two safety and fact lines need a source or a correction (moderate)

- **What is wrong.**
  - Unit 23 cites CDC's "Preventing Drowning" (day 227) for the reach and throw rescues, but the page, opened today,
    does not mention reach or throw rescue at all; it covers life jackets, lessons, close supervision and CPR. The
    rescue steps ("reach or throw, don't go") rest on memory as written.
  - Day 5's one water line says "wear a life jacket on a boat". CDC says children should wear one for all activities in
    and around natural water, not only on boats.
  - Days 81 and 82 teach the pulse "at the wrist or neck" with no caution. Pressing gently on one side of the neck only
    is the usual teaching (from memory).
- **Why it matters.** Bar criterion 4: fitness and safety content is accurate and sourced; APPROACH.md marks unsourced
  safety facts "from memory".
- **Fix.** Day 227's note: "Rescue steps: from memory until the safety agent names a national lifesaving or Red Cross
  water-safety page and opens it; CDC's page supports life jackets and supervision only." Day 5: "near open water such
  as a lake, river or the sea, stay with a grown-up, and wear a life jacket on a boat or when playing in natural water."
  Day 81 note: "at the neck, press gently with two fingers on one side only (from memory; the safety agent checks)."
- LAYER sequence. REPEAT new. Confidence: firm for the CDC page (opened), likely for the pulse caution.

### 5. g1-heart-muscle was used the year before, so unit 4 retrieves it, not a readiness check (minor)

- **What is wrong.** The frame and scope place a readiness check on day 32 for g1-heart-muscle as "two grades back".
  But PE K to 2 day 164 (grade 2, unit 15) opens with a retrieval task on it (its `retrieves` column), and g2-stretch-why
  assumes it. Its last use is grade 2, one year before, so rule 2 asks for a retrieval inside unit 4's first skill day.
  The earlier expert frame read said the readiness rows were "counted right"; this read disagrees, on the K to 2 days.csv.
- **Why it matters.** Small: ten minutes of day 32 go to a check the rule does not call for, and day 34's "readiness
  results" note rests on it.
- **Fix.** Drop the readiness check from day 32 (its last ten minutes return to the respond task; clear `readiness`
  from `assess`). Day 33's instant activity already runs the pulse-check: add "and the heart is a muscle that grows
  stronger with activity (g1-heart-muscle, K to 2 grade 2 day 164's retrieval)" and put g1-heart-muscle in day 33's
  `retrieves`. Day 34's note keeps the up-to-5-minute reteach "where the retrieval shows a gap". The frame's Readiness
  and retrieval bullet and Seams row need the same change (For the lead).
- LAYER frame. REPEAT yes (readiness classification, Codex frame read finding 5). Confidence: firm.

### 6. Readiness results are said to shape a unit's first day that does not mention them (minor)

- **What is wrong.** Days 153, 196 and 205 say "results shape unit N's day 1". Days 206 and 226 carry the results;
  day 154 (unit 16) and day 197 (unit 20) do not mention them.
- **Fix.** Day 154 note: "The readiness results on g1-world-games set how long the 'games from other places' recap runs
  (up to 5 minutes)." Day 197 note: "The readiness results on g2-foods-energy set how long the food-gives-energy recap
  runs."
- LAYER sequence. REPEAT new. Confidence: firm.

### 7. Day 1's hook is freeze tag in a shrinking area before the safe-movement cues (minor)

- **What is wrong.** Day 1 opens the band with a freeze-tag round "in a shrinking area". Eyes up, open space and
  collision control are taught on day 2; the shrinking area is the changing setting day 7 is built for.
- **Why it matters.** A shrinking area raises collisions; on day 1 of grade 3 the class has not yet met the band's
  safety cues. The lens names unsafe space as a day error.
- **Fix.** Day 1 hook: "a two-minute freeze-tag round at walking pace in a fixed marked area". Keep the shrinking area
  on day 7.
- LAYER sequence. REPEAT new. Confidence: judgment call.

### 8. Wet-day paths are named for units 1, 2 and 5 only (minor)

- **What is wrong.** The .md says each movement day's space line names "the wet-day path where the frame lists one".
  The frame asks every unit for a wet-weather version (bar criterion 5) but leaves it to the unit plan, so 209 of 240
  day notes carry no wet-day line, including the outdoor-leaning game units 18, 19 and 21.
- **Fix.** Add one wet-day clause to each unit's space line (for example unit 18: "wet day: indoors, two-a-side on
  half courts, foam balls"; unit 21: "wet day: indoor tee stations against a wall with foam balls, no running bases").
- LAYER sequence. REPEAT new. Confidence: likely.

### 9. g3-strike-tools gets a readiness check though grade 4 used the row (low; settled as is)

- **What is wrong.** Day 116 (grade 4) retrieves g3-strike-tools for paddle contact, so by the row the last use is the
  year before. The frame argues the long-tool part was last used in grade 3, so day 205 checks only that part. The
  Codex frame read raised this; the frame kept it with its reason.
- **Fix.** None to the days. The .md's Readiness bullet should say once that this is a part-level readiness check, the
  row's short-tool part having been retrieved on day 116, so a later reader does not see a rule break.
- LAYER frame. REPEAT yes (Codex frame read finding 5). Confidence: judgment call.

### 10. Two pointers and one summary line are off (low)

- **What is wrong.** (a) The .md says the shared cards are quoted from "SEL STANDARD section 7 in the grades 3 to 5
  form"; section 7 gives the K to 2, 6 to 8 and 9 to 12 forms only, and the 3 to 5 words come from the SEL 3 to 5
  frame's "Shared steps with health and PE" bullet (the words do match it). (b) "Every other earlier-grade row is
  retrieved ... on the unit's first or second day" is not so for days 67, 105, 137, 181, 190 and 207, which retrieve on
  the day the row is first needed.
- **Fix.** (a) Cite the SEL 3 to 5 frame's Shared steps bullet. (b) "on the first day that needs it".
- LAYER sequence. REPEAT new. Confidence: firm.

## Days by load

- Units 22 (8 days, no owned code, five codes in new settings) and 24 (8 days, one code, S4.5.10) are light against
  unit 5 (9 days, four codes and a conduct row) and unit 11 (11 days, five codes). The frame set these counts, and units
  22 and 24 do work as the band's spaced use of S1 before grade 6, so no move is asked; the .md's unit 24 entry should
  say in one line that days 234 to 236 are that review, so a unit plan does not pad them. No other run is far off its
  load.

## The brief's other checks

- **Owned ids and frame rows.** All 57 span-5 codes are claimed only in their owner's unit or in a course-level check;
  `~` codes are named in notes, not claimed. Holds.
- **school_day and weeks.** school_day = 2 x course day across the band; every unit and check falls in the frame's
  weeks and CALENDAR.md's (checks in weeks 18 and 26 each year, respond days included). Holds. Specials do not count in
  the K to 5 stagger, as the .md says.
- **Order inside units.** Each day builds on the last; no game comes before its skill (the day 1 hook is finding 7).
  The arcs reach each compelling question.
- **Course-level checks that do not repeat.** Each check right after a unit's check carries that unit unscored and says
  so (days 43, 63, 123, 143, 203, 223). Every standard is sampled in each year's two checks. Holds.
- **Same-year leans.** Science grade 4 (day 81), math grade 5 (day 167) and social studies grade 4 (day 154) carry their
  bridges. SEL calm-down and talk turn cards meet SEL's days (weeks 2 and 17 of grade 3 before PE days 57 and 49); SEL
  grade 4's settle-disagreement steps (weeks 23 to 26) come the year before PE unit 18; health units 1, 3, 5, 8 and 15
  and dance units 1, 5 and 9 sit where the notes say. The goal card is finding 3.
- **Candidate cells.** Every frame candidate is kept on a named day with its minutes, or dropped with its reason (unit
  16). Holds.
- **Shorter path.** Present: the 64-session path per year and a 10-days-short year by named fold-ins, and the
  leave-out and swap bridge. The scope's For the lead 1 (grades 3 and 4 cannot reach 16 Fluency drops under the frame's
  rules) is right; I checked the counts. Finding 2 is the one cut.
- **Source map.** Not applicable (no base text).
- **Sensitive ground.** Cultural picks are flagged as candidates on their days, with no gender roles, no costume, the
  Bastringue tune without lyrics, and Pilolo only in a Ghanaian-confirmed version. The encyclopedia entries I opened
  agree with the picks' descriptions (jianzi kept up with the feet, circle play and counting; Pilolo a Ghanaian
  children's search game with no ceremonial status shown; the Virginia reel's English country dance roots with Scottish
  and Irish links claimed). None is a community source, so the sensitivity agent's confirm still stands. Food, water,
  emotion and body flags sit on their days. Health's disclosure steps are on every teacher page.

## Lens checklist (scope and sequence layer)

| Line | Met? |
|---|---|
| A year of games with no outcomes | Met: outcomes per standard per grade, copied from the frame |
| A grade with no outcome for one of the four standards | Met |
| A span indicator placed in no year | Met: all 57 owned |
| Skills out of developmental order | Met: PECAT's grade 4 starts kept (passing, volleying, combinations) |
| Dance or fitness taught once and never again | Met: dance in units 8, 15, 22; fitness in 4, 9, 17, 20 |
| PE and health both or neither teaching the activity outcomes | Met: named on both sides, one log in grade 5 |
| PE dance and the dance course teaching the same thing in a year | Met: dance teaches elements first, PE the motor skill |

Bar section 4: criteria 1 (finding 1), 2, 3, 6, 7 and 8 met at this layer; 4 is finding 4; 5 is finding 8.

## What is right and should not be touched

- The collect-once rule on the course-level checks and the "carried unscored" lines.
- The baseline and check pairs on the same cue in every unit, and private skill sheets that travel to grade 6.
- S3.5.5 taught and watched in all three settings in unit 18, with scripted scenes of invented players.
- S1.5.22's dry-land part checked for every school and the swimming part left to a school's own program.
- The For the lead 1 arithmetic on the short path.

## What I could not judge

- Community sources for the five cultural picks (the sensitivity agent's task); the Library of Congress record stays a
  browser check.
- A rescue-steps source (finding 4); I did not search for one.

## Sources

- CDC, Preventing Drowning, https://www.cdc.gov/drowning/prevention/index.html (dated 2025-09-29): life jackets in and
  around natural water, supervision, lessons, CPR; no reach or throw rescue.
- https://en.wikipedia.org/wiki/Pilolo, https://en.wikipedia.org/wiki/Jianzi,
  https://en.wikipedia.org/wiki/Virginia_reel_(dance): checking the cultural picks' descriptions (not community
  sources).
- From memory: the neck-pulse caution.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Add "names two activities that raise the heart rate" to days 89 and 124 | S2.5.12's second part had no prompt | days.csv |
| Day 152 skill task in two of the unit's styles, the second carried from day 151's closure watch | S1.5.5 asks several dance styles | days.csv, .md unit 15 |
| Day 71 skill task in two rope tasks, forward plus one of the child's choice | S1.5.6 asks several tasks | days.csv, .md unit 7 |
| Day 21 adds an underhand throw to a hoop; day 20 names catches at middle and high levels | the row's two throws and levels | days.csv |
| Day 99 passes with a moving partner, hands then feet | S1.5.17 as the row teaches it | days.csv |
| Day 159 describes both games and their places | S3.5.7 is plural | days.csv |
| Weekly goal check in every unit 17 warm-up from day 164; short path drops 167, 200, 219 in place of 165 and 169 | keeps S4.5.6 near four weeks on 64 sessions | days.csv, .md Shorter path |
| Days 36 and 67 use the K to 2 goal steps card; the four-step form from grade 4 | SEL grows the card in grade 3 week 27 | days.csv, .md Shared cards |
| Day 227 rescue steps marked from memory; day 5 life jacket line widened; day 81 neck-pulse caution | accuracy and sourcing | days.csv |
| g1-heart-muscle moves from a day 32 readiness check to day 33's retrieval | last used in K to 2 grade 2 (day 164) | days.csv, .md Readiness |
| Readiness results lines on days 154 and 197 | the results must shape day 1 | days.csv |
| Day 1 hook at walking pace in a fixed area | safety cues come on day 2 | days.csv |
| A wet-day clause in each unit's space line | bar criterion 5 | days.csv |
| g3-strike-tools readiness kept as a part-level check, said once in the .md | long tools unused since grade 3 | .md Readiness |

## For the lead

- The frame's Readiness and retrieval bullet and its Seams row for g1-heart-muscle should become a retrieval (finding
  5).
- The scope's For the lead 1 (Application drops in grades 3 and 4) now also covers days 200 and 219 in grade 5
  (finding 2); the frame's short-path bullet should allow an Application drop in any unit of 6 or more days where
  Fluency runs out.

## For Cory

None: no finding changes scope, money, people or audience.

## For the source list

- CDC's Preventing Drowning page does not cover reach or throw rescues; a water-rescue source is still needed for unit
  23 (and PE K to 2 unit 22 if it cites the same page for rescues).

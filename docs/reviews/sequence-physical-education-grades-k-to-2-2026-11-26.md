# Expert read: scope and sequence of Physical Education, grades K to 2 (2026-11-26)

Reviewer: the curriculum expert (docs/agents/EXPERT.md), a fresh agent reading cold. I did not write this scope.
Brief: docs/pipeline/briefs/sequence-read.md, with the after-core notes in build/scope-writes/AFTERCORE-BRIEF.md
and build/scope-writes/AFTERCORE-READ.md.

## What I read

- docs/courses/physical-education-grades-k-to-2/scope-and-sequence.md and
  data/plans/physical-education-grades-k-to-2/days.csv (240 rows), in full.
- The frame docs/courses/physical-education-grades-k-to-2/frame.md, in full, and its three 2026-11-25 reviews
  (expert, Codex, fixes), for what was already settled.
- docs/agents/lenses/physical-education.md; docs/courses/physical-education/STANDARD.md and APPROACH.md ("Pacing");
  data/standards/shape-pe-2024.txt (the 49 span-2 indicators); data/progressions/physical-education.csv (the 48 K
  to 2 rows, their `assumes` and notes).
- docs/courses/CALENDAR.md (rule 1 and the weeks table for this course) and data/plans/calendar.csv; the days.csv
  of health K to 2, SEL K to 2 and dance K to 2 for every same-year lean; SEL STANDARD section 7 ("Shared steps")
  and health K to 2's conflict-steps wording (frame, progression, days.csv day 72).
- Gates: `scripts/plan.py check` (this course passes; failures elsewhere belong to other courses),
  `scripts/frame.py calendar`, `scripts/sequence.py check physical-education-grades-k-to-2` (0 failures),
  `scripts/frame.py check physical-education-grades-k-to-2` (0 failures; K 74, 1 74, 2 74 unit days),
  `scripts/stale.py check` (0 failures).
- Sources opened 2026-11-26: Korea's Ministry of Culture, Sports and Tourism page "Korea's Culture of Play"
  (mcst.go.kr/english/useful/month202112.jsp); CDC "Preventing Drowning" (cdc.gov/drowning/prevention/index.html,
  dated Sept. 29, 2025, recommends life jackets for children near natural water and formal swim lessons); SPHEReS
  (myspheres.ca/en/, the University of Alberta Injury Prevention Centre's school safety guidelines); the folk dance
  notes archive's index (folkdancefootnotes.org), which lists "Seven Jumps, Syvspring (Denmark), De Zevensprong (the
  Netherlands)" and "Pawpaw Patch, children's play party game, USA". The frame's old Syvspring address returns 404;
  the live one is in the source note at the end. The Nova Scotia 2021 PDF was not reopened: the frame opened it on
  2026-11-25 and nothing in this scope rests on its text.

## Verdict

The scope is sound and close to ready. Order inside units, retrieval, the calendar weeks, the shorter paths and the
candidate cells all hold, and every owned indicator is taught and checked in its owning unit. The biggest risk is
the team-talk card: it is said to be health's conflict steps "word for word", but it drops health's last step, "an
adult helps when words do not work", which is the step that keeps a seven-year-old's conflict safe. The other
serious gaps are that the 18 course-level days have no safe space or equipment in their notes, and that the "several
in-place practice tasks" indicators rest on one end task, with the closure-watch records the scope promises never
written on the days.

## Findings, most serious first

### 1. Team talk is not health's conflict steps, and loses the adult-help step (serious; LAYER sequence, with the frame and progression; REPEAT yes)

- **What is wrong.** Scope "Shared cards" and day 183 give team talk as "stop, say what happened, listen, find a
  fair way, then try it" and call it health's conflict steps "word for word". Health's own words (health K to 2
  frame unit 14, data/progressions/health.csv g2-v-settle-it-with-words, health days.csv day 72) are "stop, say what
  happened, listen, find a fair way, an adult helps when words do not work". PE swaps the fifth step for "then try
  it". The note on day 183 also says health unit 14 "opens with these steps as retrieval". Health's day 72 does not:
  it retrieves health grade 1 unit 9 and teaches the steps as a new Understanding day.
- **Why it matters.** A child meets two versions of one card in the same grade, which is exactly what the shared-steps
  rule (SEL STANDARD 7, DESK-ANSWERS 2026-11-26) is there to stop. The dropped step is the safety step: at 7 years
  old, a station quarrel that words do not fix needs an adult, and the PE card never says so.
- **Fix.** Scope "Shared cards", day 183's goal and note, day 185, day 189's knowledge prompt and conduct line, and
  any unit 19 review: use health's five steps exactly as health writes them. "Then try it" can stay as what the
  group does after step 4, never as a printed step. Change day 183's note to "health K to 2 unit 14 (weeks 13 to
  18) comes later in the year and teaches the same steps". The frame's Models carried row and the progression note
  for g2-talk-problems carry the same wording. That fix belongs to the lead (For the lead below).

### 2. The 18 course-level days have no safe space, equipment or no-equipment path (serious; LAYER sequence; REPEAT new)

- **What is wrong.** Every unit day's note names its space, equipment and no-equipment path. The six check windows
  (days 43, 44, 68, 69, 123, 124, 148, 149, 201, 202, 226, 227) and the six course-level respond days (45, 70, 125,
  150, 203, 228) name none. These are movement days. The K year-end (68, 69), grade 1 year-end (148, 149) and grade
  2 year-end (226, 227) windows run striking stations, with a long-handled tee in grade 2, while the other groups
  practice. The AFTERCORE brief and bar criterion 5 ask for space and equipment on every movement day.
- **Why it matters.** These are the days a teacher sets up the most mixed stations at once. They are also the days
  with no unit's boilerplate to fall back on. The swing-space rule is missing on exactly the days it is most needed.
- **Fix.** Give each course-level day a note in the unit pattern: the stations and their space (for every window
  with a striking station, "a full swing's space clear on every side, one swinger per space, stand beside, never in
  front"), the equipment drawn from the sampled units, the no-equipment path (rolled socks, paper-plate paddles,
  pool noodles, tape lines), and the water break on warm outdoor days. Respond days carry the same note as their
  window.

### 3. "Several in-place practice tasks" rests on one end task; the promised closure records are not on the days (moderate; LAYER sequence; REPEAT new)

- **What is wrong.** Ten owned indicators say "in several in-place practice tasks": S1.2.6 bounce, S1.2.7 roll,
  S1.2.8 catch, S1.2.9 throw, S1.2.10 kick, S1.2.11 foot dribble, S1.2.12 hand strike, S1.2.13 short tool, S1.2.14
  long tool. S1.2.16 does not. The scope (Assessment pattern) says these "stand on the record of closure watches
  across the unit's Fluency days plus the end task, never one try". But only days 22, 41 and 121 carry a
  closure-watch mark, and those marks are for a second indicator, not a second task of the same one. The Fluency
  days (for example 114, 118, 174, 206) do not say anything is recorded. Each check asks one task: five one-hand
  bounces (121), three throws at one target (179), tee contact only (57, 211), a roll to a target only (32), a
  still-ball kick only (41).
- **Why it matters.** A busy teacher checks one task, so the record shows one task. The plural, which is the whole
  point of the span-2 wording, goes unchecked. The bounce row itself names two hands, one hand, to a partner and to
  a wall.
- **Fix.** Use the pattern units 2, 4 and 11 already use. Each owning unit's last Fluency day records a second
  in-place task of the same indicator as its closure watch, carried as a mark, and the check day's note names it.
  The days and tasks are in "Settled by the expert" (row 5). No day is added.

### 4. Twelve unit days claim codes their unit does not own (moderate; LAYER sequence; REPEAT yes)

- **What is wrong.** These codes appear plain, without `~`, outside the unit that owns them in the frame's Units
  table: day 19 S3.2.4 (unit 2), 38 S3.2.3 (unit 4), 65 and 66 S3.2.4 (unit 6), 74 S3.2.3 (unit 7), 79 S1.2.2
  (unit 7's check), 88 S3.2.4 (unit 8), 118 S3.2.5 (unit 11), 142 S3.2.5 (unit 13), 167 S3.2.3 (unit 15), 183 and
  186 S3.2.3 (unit 17). Days 183 and 186 also go against the progression, which marks S3.2.3 as `~` in
  g2-talk-problems. The scope's own band section says a reused code takes `~`.
- **Why it matters.** The course page counts a plain code as claimed. Several units would then appear to own S3
  conduct codes that unit 1 or unit 10 owns, and a leave-out unit would not take them off the claim.
- **Fix.** Prefix `~` on those twelve cells. Course-level check days keep plain codes, since they sample.

### 5. Mugunghwa's spot-check source does not show the game, and its one mention sits beside the television-show image (moderate; LAYER frame; REPEAT new)

- **What is wrong.** The frame (unit 14) and this scope rest Mugunghwa on Korea's Ministry of Culture, Sports and
  Tourism page "Korea's Culture of Play", which the frame says "shows it among Korea's alleyway games". I opened the
  page on 2026-11-26. Its alleyway-games text does not name Mugunghwa. The only mention is an image's alt text,
  "game of Mugunghwa has bloomed and dalgona", which pairs it with the candy game known from the same television
  show the unit promises never to mention.
- **Why it matters.** The cultural rule (Cory 2026-11-20) names a game only after its own source says it is open to
  be taught, and this source does not carry that. The game itself is a genuine Korean children's game, and the name
  and translation are right. The source cited for it is the weak part.
- **Fix.** No day changes. The sensitivity agent finds a Korean folk-culture source that describes the game before
  unit 14 names it: the National Folk Museum of Korea's Encyclopedia of Korean Folk Culture is the first place to
  look ("browser check": not opened here). The scope's "What I am unsure of" should name Mugunghwa's source as
  unconfirmed, not only "whether the sensitivity read will confirm" it.

### 6. Unit 1's check asks only half of S3.2.4 (minor; LAYER sequence; REPEAT new)

- **What is wrong.** S3.2.4 is responding to the teacher's directions and feedback. Unit 1 owns it, and day 11's
  conduct mark is only "stops on the signal". The feedback half is first asked in unit 8 (day 89), a year later and
  as review.
- **Fix.** Day 11 conduct: "stops on the signal and acts on one cue the teacher gives (S3.2.4)".

### 7. Unit 14's S4.2.2 prompt can be answered without pointing out an activity with others (minor; LAYER sequence; REPEAT new)

- **What is wrong.** Day 159 asks for "a favorite and alone or with others". A child whose favorite is a solitary
  activity answers in full and never points out an activity that lets them be with others, which is what S4.2.2
  asks.
- **Fix.** Day 159 and the scope: "name one activity you can do with others; name your favorite and say if it is
  alone or with others" (S4.2.2 and S4.2.4 each get their own prompt).

### 8. Unit 13's check pattern does not ask for "a range of dance styles" (minor; LAYER sequence; REPEAT new)

- **What is wrong.** S1.2.15 asks for moves taken from a range of dance styles. Day 145's skill task is one pattern
  (a traveling, an in-place and a scarf move) and could be drawn from one dance.
- **Fix.** Days 145 and 146: the pattern takes moves from two of the unit's dances (for example a Seven Jumps step
  and a La Raspa move), named on the check card.

### 9. Goal steps card not quoted word for word (minor; LAYER sequence; REPEAT yes, health K to 2 read finding 8)

- **What is wrong.** Scope "Shared cards" gives the kindergarten rung as "my goal, one step". SEL STANDARD 7 gives
  "my goal and one step".
- **Fix.** Use "my goal and one step" in the scope and on every day that quotes the card (units 5, 14, 16, 22).

### 10. Unit 22's look-back days carry the water kit and no low-equipment path; one unit reference slips (minor; LAYER sequence; REPEAT new)

- **What is wrong.** Days 234 to 240 copy the life-jacket equipment line. The look-back stations on days 235 and
  236 need the band's balls, paddles and ropes, and no day in unit 22 names a no-equipment path. Day 234 says
  "grade 1 unit 11's calm steps and unit 16's goal cycle"; unit 16 is grade 2.
- **Fix.** Days 234 to 236 and 240 name the review stations' equipment and the band's no-equipment path. Days 229
  to 233 keep the life jackets as Required access, and their pool noodle and rope already work with little
  equipment. Day 234: "grade 2 unit 16's goal cycle".

### 11. Grade 2 mid-year conduct is not named (minor; LAYER sequence; REPEAT new)

- **What is wrong.** Day 201's note says "Conduct watched again at the new stations" and names no behavior. The
  other five windows name theirs.
- **Fix.** Day 201: "conduct: shares the station and its equipment with words (S3.2.3, unit 1, as in unit 17)",
  with `SHAPE.S3.2.3` added to the codes of days 201 and 202.

## What is right and should not be touched

- **Retrieval.** Every `assumes` row in the progression is retrieved, from the year before, in the instant activity
  of the first day that needs it (I checked all 31 grade 1 and grade 2 rows). No row is two grades back, so the
  course rightly has no readiness checks. No unit's day 1 carries a check.
- **Calendar.** The formula 160 x y + 2n puts every check on CALENDAR.md's weeks (K 18 and 28, grade 1 18 and 28,
  grade 2 17 and 27) and every unit in its frame weeks. The same-year leans meet calendar.csv: health K unit 2
  (weeks 6 to 11), health grade 2 units 12 and 13 (weeks 1 to 10), SEL grade 1 unit 8 (weeks 5 to 8), SEL grade 2
  unit 13 (weeks 1 to 4) and dance grade 1 unit 5 and grade 2 units 9 and 10 all come before the PE days that lean
  on them. PE unit 17 teaches team talk before health unit 14 (weeks 13 to 18) and SEL unit 15 (weeks 11 to 16).
- **Checks that do not repeat.** Every course-level check leaves out the unit just checked and carries its record.
  Reusing day 66's travel-and-freeze record at the K year-end instead of watching it again is the right call.
- **Shorter path.** 16 Fluency days a year, at most 3 a unit, none a last Fluency day, a teaching day or a check day.
  Every unit keeps a Fluency day. The 10-day-short list sits inside the 64-session list, and the leave-out bridges
  are named. I checked all 48 dropped days.
- **Every body and every culture.** No elimination, no human targets, no gender split, teacher-set partners, dry-land
  water only, no body or food judgment, and the counselor named on the emotion days. The dance and game picks are
  accurate (Syvspring and Zevensprong, La Raspa, Doña Blanca, Kinderpolka and Paw Paw Patch are what the scope says
  they are), and the swap rule is kept.
- **Lens checklist, scope layer.** Outcomes are stated per grade per standard (met). All 49 span indicators are
  owned and placed (met). Skills are in developmental order, still before moving and underhand before overhand
  (met). Dance (units 7, 13, 21) and fitness (units 6, 12, 15, 18) return every year (met). PE and health split the
  physical activity outcomes with named retrievals (met). The dance course's rows are retrieved, not retaught (met).

## What I could not judge

- Whether Mugunghwa and Doña Blanca are confirmed open to be taught by their communities' own sources. That is the
  sensitivity agent's read, and finding 5 asks for a better source.
- The safety guides' section text (Nova Scotia 2021, SPHEReS) against units 5, 9, 12, 15, 17, 19 and 22. The safety
  agent reads those before the units go live.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| 1. Team talk printed as health's five steps exactly ("stop, say what happened, listen, find a fair way, an adult helps when words do not work"); "then try it" is the group's action, never a step; day 183's note says health comes later and teaches the same steps | One card per child; keeps the adult-help step | days.csv 183, 185, 189 (and 207, 211 where quoted); scope-and-sequence.md "Shared cards", unit 17 |
| 2. Course-level days 43 to 45, 68 to 70, 123 to 125, 148 to 150, 201 to 203, 226 to 228 get a space, equipment, no-equipment and water-break note; striking windows carry the swing-space rule | Movement days need their safe space | days.csv |
| 3. `~` on days 19, 38, 65, 66, 74, 79, 88, 118, 142, 167, 183, 186 for the reused code | Claim only in the owning unit | days.csv |
| 4. Day 11 conduct adds "acts on one cue the teacher gives"; day 159 splits S4.2.2 and S4.2.4 prompts; days 145 and 146 take the pattern's moves from two dances; day 201 names S3.2.3 conduct (codes 201, 202) | Each item asks the whole of its id | days.csv; scope-and-sequence.md unit 1, 13, 14 and the checks table |
| 5. Second in-place task recorded at the last Fluency day's closure watch and named on the check: day 31 (roll to a seated partner; catch a bounced ball), day 40 (kick to a partner), day 56 (strike a self-dropped ball), day 120 (bounce to a wall and back), day 178 (throw to a partner), day 210 (strike a self-dropped ball with the long tool); day 120 also records the balloon hit with a partner | "Several in-place tasks" checked, no day added | days.csv; scope-and-sequence.md "Assessment pattern" |
| 6. Goal steps card quoted as "my goal and one step" | Word for word with SEL STANDARD 7 | scope-and-sequence.md; days.csv where quoted |
| 7. Days 234 to 236 and 240 name the review stations' equipment and the no-equipment path; day 234 reads "grade 2 unit 16" | Right kit for the look-back days | days.csv |
| 8. "What I am unsure of" names Mugunghwa's source as unconfirmed (browser check: Encyclopedia of Korean Folk Culture) | The cited page does not show the game | scope-and-sequence.md |

## For the lead (not Cory)

- The frame's Models carried row for team-talk and the g2-talk-problems progression note carry "then try it". Bring
  them to health's five steps when the frame is next touched.
- Health K to 2 day 72 teaches the conflict steps as new without naming PE unit 17, which comes first in grade 2.
  The health side should open with them as retrieval where the school runs PE, per the frame's Cross-subject row.
- The frame's unit 14 source line for Mugunghwa overstates what the cited page shows (finding 5).
- The frame's Syvspring and Zevensprong address is now
  folkdancefootnotes.org/dance/a-real-folk-dance-what-is-it/1st-generation-dances/childrens-dances-1st-generation-or-living/seven-jumps-l-syvspring-denmark-de-zevensprong-netherlands/

## For Cory

None. No finding changes scope, audience, money or outside people.

## For the source list

- Korea's Ministry of Culture, Sports and Tourism, "Korea's Culture of Play" (mcst.go.kr/english/useful/month202112.jsp):
  opened 2026-11-26. It names alleyway games but not Mugunghwa in its text. Not enough on its own for that game.
- folkdancefootnotes.org children's-dance entries for Seven Jumps and Pawpaw Patch: live addresses as above.
- CDC "Preventing Drowning": still live, dated Sept. 29, 2025.
- SPHEReS (myspheres.ca/en/): live, University of Alberta Injury Prevention Centre.

## Confidence

Findings 1, 4 and 9: firm (the files disagree on their face). Finding 2: firm. Finding 3: likely (the SHAPE wording
and the progression row agree; how many tasks count as "several" is a judgment call). Finding 5: firm on what the
page shows; a judgment call on what source will suffice. Findings 6 to 8, 10 and 11: likely.

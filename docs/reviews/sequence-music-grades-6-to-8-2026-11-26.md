# Expert cold read: scope and sequence of Music, grades 6 to 8 (2026-11-26)

Job: docs/pipeline/briefs/sequence-read.md, course `music-grades-6-to-8`, subject arts (lens docs/agents/lenses/arts.md;
bar: docs/ADOPTION-BAR-SUBJECTS.md section "2. Arts", items 1 to 9 and "Fails if", with docs/courses/arts/STANDARD.md
and docs/courses/arts/APPROACH.md), with the arts additions in build/scope-writes/ARTS-READ.md and the writer's brief
build/scope-writes/ARTS-BRIEF.md. The scope was written by a fresh agent; read cold.

## What I read

- docs/courses/music-grades-6-to-8/scope-and-sequence.md (all) and data/plans/music-grades-6-to-8/days.csv (all 192
  rows: goals, codes, assess, school_day, retrieves, and the notes of every day named below).
- docs/courses/music-grades-6-to-8/frame.md (all: the course in brief, Seams, Models carried, Units table, Course-level
  checks, Cross-subject, For the lead).
- The mu-g6, mu-g7 and mu-g8 rows of data/progressions/arts.csv (standard, assumes, cross_subject, notes), and the last
  use of every mu-g5 row in data/plans/music-grades-3-to-5/days.csv (that scope now exists).
- data/standards/ncas-performance-standards-words.txt for the Re8.1, Re7.2, Cn11.1, Pr4.3 and Cr3.2 lines of grades 6
  to 8.
- docs/courses/CALENDAR.md (rules 1 to 5 and the grade 6, 7 and 8 rows), the `frame.py calendar` output for grades 6
  to 8, docs/pipeline/briefs/sequence-write.md rules 2, 3 and 10, docs/courses/UNIT-PLAN.md rule 6 (reteach timing),
  docs/courses/arts/APPROACH.md "Readiness and the baseline look", docs/agents/EXPERT.md and the arts lens.
- Earlier reads for repeat tags: no earlier arts scope and sequence read exists in docs/reviews/; repeats are judged
  against the core-subject sequence reads (2026-11-14 to 2026-11-24, for example sequence-psychology-2026-11-24.md).
- Gates: `scripts/sequence.py check music-grades-6-to-8`: 0 failures. `scripts/plan.py check`: this course's sequence
  and frame 0 failures, "12 units, 192 days (180 in units, 12 for checks and respond days)", unit days 60 a year (the
  failures plan.py prints belong to other courses). `scripts/frame.py calendar`: music 6 to 8 checks in weeks 19 and
  32 for grades 6, 7 and 8, no break. `scripts/stale.py check`: 0 failures.
- No outside source was fetched. Two findings lean on the national standard text from memory and say so.
- EXPERT.md asks for each finding to be logged with `scripts/plan.py defect`; this job's brief says to edit no file
  but this report, so the caller logs them.

## Verdict

The scope and sequence is sound and close to ready: each year claims only its own grade's 21 ids, all 63 sit on
teaching days and end-of-unit assessments of the right year, every unit has all four processes, a technique taught
before the making, one critique, a revision and a showing, the retrieval calls are right by grade number, and the
calendar, leans and school_day count all hold. The biggest risk is in the assessed evidence at its edges: the three
year-end checks sample the Cr1.1 codes without their form and expressive-intent parts, the listening ids of units 1, 5
and 9 rest on a single teaching day each, and the once-a-week merged sittings have no minute budget (year 8's cannot
run as merged). The one change that matters most is finding 1 (a prompt per part on days 63, 127 and 191), with the
once-a-week sitting budget (finding 5) next.

## Findings, most serious first

### 1. The year-end checks sample the Cr1.1 codes without their form and intent parts

- **LAYER** sequence. **REPEAT** yes (the same kind as the part-by-part prompt findings of the core reads, for
  example sequence-psychology-2026-11-24.md finding 1).
- **What is wrong.** Day 63 claims MU:Cr1.1.6a with "compose and notate a four-bar answer phrase on a given two-chord
  pattern". The code (and its words line) asks for phrases within AB and ABA form that convey expressive intent; a
  lone answer phrase shows neither. Day 127 claims MU:Cr1.1.7a with "one variation of a given theme over a given chord
  pattern": the form is there, the expressive aim is not asked. Day 191 claims MU:Cr1.1.8a with "a short introduction
  and coda for a given tune with its tension line": the expanded form is there, the aim is not asked. The unit
  assessments (days 49, 113, 177) do ask for the stated aim; the checks drop it.
- **Why it matters.** sequence-write rule 2 "Each part of each code": a check that lists a code asks about each part.
  A unit plan writer will build the year-end item from the goal as written and score intent-free phrases as met.
- **Fix.** Day 63 goal: "compose and notate a four-bar answer phrase on a given two-chord pattern, write in one line
  the mood it aims for, and mark whether it would sit in the A or the B section of an ABA piece and why". Day 127
  goal: add "with its expressive aim written at the top and one decision that carries it named". Day 191 goal: add
  "with its expressive aim written at the top and one decision in the coda that carries it named". The scope's
  Course-level checks table samples cells change to match. Confidence: firm (the words file and rule 2 agree).

### 2. The listening ids of units 1, 5 and 9 each rest on one teaching day

- **LAYER** sequence. **REPEAT** new.
- **What is wrong.** Counting days that carry each code before the listening sitting: unit 1, MU:Pr4.2.6a 6 days and
  MU:Pr4.2.6b 5 days, but MU:Re7.2.6a 1 day (day 3, week 2) and MU:Cn11.1.6a 1 day (day 9, week 5), both then
  assessed on unseen material on day 17 (week 9); MU:Re9.1.6a 2 days. Unit 5: MU:Cn11.1.7a 1 day (73), MU:Re7.2.7a 2
  (67, 72). Unit 9: MU:Cn11.1.8a 1 day (138), MU:Re7.2.8a 2 (135, 136). The interpretation units each get a supported
  practice day before their written sitting (days 36, 100, 164); the listening units, with four written listening ids
  each, get none. The rehearsal days (12 to 15, 76 to 79, 140 to 143) carry only the reading ids.
- **Why it matters.** Rule 7 (days by load): four of seven ids get the smallest share of days, and a student meets
  "describe how elements connect to structure" once, seven weeks before an unseen-recording item. At two sessions a
  week that is a recall test, not a skill.
- **Fix (no day added).** Make the five-minute warm-up openers of the rehearsal days a rotating listening round with
  short excerpts: day 12 a structure round (where does the theme come back, MU:Re7.2.6a), day 13 a judge round on one
  teacher criterion (MU:Re9.1.6a), day 14 a connection round (one link from a new excerpt, MU:Cn11.1.6a), day 15 a
  setting match (MU:Re7.2.6b); add those codes to the four days. The same on days 76 to 79 (with 7a codes) and 140 to
  143 (with 8a codes). Day 11's and day 75's and day 139's fluency drills add one structure item each. The scope's
  unit 1, 5 and 9 sections name the openers. Confidence: likely (teaching judgment on spacing; the counts are from
  days.csv).

### 3. The retrieval and reteach minutes on each unit's day 2 do not add up

- **LAYER** sequence. **REPEAT** new.
- **What is wrong.** Day 2's note reads "Opener (10 minutes): retrieval of ... (mu-g5-read) and ... (mu-g5-respond),
  each with its ten-minute reteach"; days 20, 40 and 52 say the same. That is two ten-minute reteaches inside a
  ten-minute opener on a day that also teaches a new technique (day 2: every rhythm and pitch symbol). Years 7 and 8
  (days 66, 84, 104, 116, 130, 148, 168, 180) name no reteach at all, though the scope's mixed-class line says each
  retrieval carries one. UNIT-PLAN rule 6 already places a reteach: the next day's warm-up and first five minutes,
  whole class if more than a third missed, otherwise a small group while the rest warm up.
- **Why it matters.** Year 6 is where many students arrive without Music 3 to 5 (it is not a core course), so the
  reteach will often be whole class. A writer following the note builds a 40-minute day 2 with 26 minutes of opener,
  or drops the symbol teaching.
- **Fix.** Every unit's day 2 note: "Opener (10 minutes): retrieval of <row> and <row>, five minutes each. Any reteach
  (ten minutes per row missed) takes day 3's warm-up and first five minutes, whole class if more than a third missed,
  otherwise a small group while the rest warm up (UNIT-PLAN rule 6)." Day 3 of each unit (3, 21, 41, 53, 67, 85, 105,
  117, 131, 149, 169, 181) carries "reteach slot" in its note. Confidence: firm (UNIT-PLAN rule 6 and the arithmetic).

### 4. Year 6's Re8.1 work reads only performers, not creators

- **LAYER** standard (the words line) and sequence. **REPEAT** new.
- **What is wrong.** From memory, the national MU:Re8.1.6a and 7a name how creators' and performers' use of the
  elements and expressive qualities conveys intent (8a: creators' or performers'). The words line for 6a ("your
  reading of how elements and expression, within genre and history, convey intent") drops the creators, and unit 2
  follows it: days 19, 21 and 22 and the day 37 item are about performers' choices only (two Satie takes, du Pré, the
  alap). Year 7 meets the creator side through Astatke (composer-performer) and year 8 through Holst, Williams and
  Davids, so the gap is year 6.
- **Why it matters.** A part of an owned code with no day and no item; an adoption reviewer reading the national
  handout would mark it.
- **Fix.** Day 21 goal: add "and one choice Elgar wrote into the score (a marking, the slow opening chords) beside one
  of du Pré's". Day 37 item on two unseen takes gains one prompt: "name one choice the composer made that both
  performers keep". For the lead: check the 6a and 7a lines against the music handout and restore "creators' and
  performers'" in the words file if the handout confirms. Confidence: likely (memory of the national text, not opened
  for this read).

### 5. The once-a-week merged sittings have no minute budget, and year 8's cannot run as merged

- **LAYER** sequence. **REPEAT** new.
- **What is wrong.** The once-a-week table merges days 16+17 (and 80+81, 144+145) into "one sitting, one item per id".
  The full path spends two 38-minute sittings there. "One item per id" invites cutting MU:Re7.2.6b's three excerpts to
  one, which loses "several genres, cultures and eras". In year 8 the merge joins a performance day (each student
  sight-reads at the teacher's spot, six groups, about 18 minutes) with a listening sitting whose recordings are played
  twice, and the frame forbids the teacher hearing a group while a room works to playback. Unit 3's "48+49 (showing
  and check)" puts 15 pairs' showing to the class and the four-bar check at the teacher's spot in one 40 minutes.
- **Why it matters.** The once-a-week path must keep every assessed part (ARTS-READ); as written it either overruns
  or quietly shrinks items. The writer flagged the first of these as unsure.
- **Fix.** Add to the once-a-week section: "Merged sitting (units 1 and 5): set-up 2, items 30, collecting 3; the
  self-check moves to the respond session. Items, each recording played twice: symbols 5, culture and history 4,
  elements and structure 6, three short setting excerpts 5, a take judged 6, connection map 4." For unit 9: "the
  listening items come first with the whole class (14 minutes), then six groups sight-read at the teacher's spot
  (15 minutes) while the others write the 8c item and the connection map with no playback." For units 3, 7 and 11:
  "the showing is to the partner pair only (10 minutes), then the check; the class hears the pieces in the respond
  session." Confidence: likely (minute arithmetic from the frame's Scored evidence).

### 6. The 10-days-short fold-ins drop the baseline look on nine of twelve units

- **LAYER** sequence. **REPEAT** new.
- **What is wrong.** The baseline look at each unit's main look-for (APPROACH "Growth"; frame: two marks a unit per
  student) sits on days 5, 23, 56 and their year 7 and 8 twins (69, 87, 120, 133, 151, 184). All nine are fold-in days
  on the 10-days-short path, folded into "the next day's opener (5 minutes)". A rotating-group baseline of 30 students
  does not fit five minutes, and the fold table does not say where it goes. Units 3, 7 and 11 keep theirs (days 43,
  107, 171, not folded).
- **Why it matters.** The growth mark is half the unit's evidence of growth (bar item 8); folding it silently leaves
  one mark a unit.
- **Fix.** Fold table, "Folds into" cell for 5, 23 and 56: "the next day's opener; the baseline look moves into that
  day's first practice time, rotating groups as written". The scope's line above the table says the same holds for
  years 7 and 8. Confidence: firm (the notes on those days and the frame).

### 7. In the composing units the connecting process is a fact the teacher tells

- **LAYER** sequence. **REPEAT** new.
- **What is wrong.** The scope lists connecting in unit 3 as "41 (the tango's setting in Buenos Aires)", unit 7 as
  "103 (the tune's two national uses, a fact), 106 (Umoja's title)", unit 11 as "167, 168 (Finlandia's later uses and
  the folk tale, as facts)". Day 41's goal does not ask students to connect anything; the setting is in the note.
- **Why it matters.** ARTS-READ asks for all four processes in every unit's days; connecting is something a student
  does (relating music to another art, a setting or daily life), not a sentence heard. A reviewer would count these
  units as three-process units.
- **Fix (practice, no claim, no day added).** Day 41 goal adds "write one line on how Libertango's repeated phrase
  fits the dance it was made for". Day 106 adds "say how Umoja's title (unity) shows in what the piece keeps". Day 168
  adds "match each part of the expanded form to a moment in the Butterfly Lovers tale". The scope's process lines name
  these days. Confidence: likely.

### 8. Year 6 has no woman composer and no living woman maker; a candidate was dropped on a reason not applied elsewhere

- **LAYER** sequence (candidate cells). **REPEAT** new.
- **What is wrong.** The frame says each year has women composers and performers and living makers. Year 6's only
  woman is Jacqueline du Pré, a performer who died in 1987. Unit 2's candidate (a second interpretation tradition from
  Africa or the Arab world) was dropped because "another would cost a day", while unit 5's candidate was kept at no day
  cost by folding it into day 74's comparison. Unit 1's candidate was dropped partly because unit 4 has a living Native
  American drum group, but unit 4's powwow study may be left out (frame Leave-out), which would leave year 6 with no
  Native American maker.
- **Why it matters.** Bar item 7 and the frame's own range claim; inconsistent candidate reasoning will be copied.
- **Fix.** Keep unit 2's candidate at no day cost: day 22 hears, beside the alap, a short take by a living woman
  performer from Africa or the Arab world in a tradition where the performer shapes the music (the unit plan picks and
  checks rights, described and linked). Unit 1's dropped-candidate reason adds: "if a school leaves out unit 4's powwow
  study, the unit plan swaps one unit 1 listening work for a living Native American maker's". Confidence: a judgment
  call.

### 9. Three days that meet flagged traditions carry no flag, and day 61's item has no leave-out route

- **LAYER** sequence. **REPEAT** new.
- **What is wrong.** Day 51 plays a powwow social song with no ceremonial note (only day 53 has it). Day 115 hears
  samul nori with no pungmul note (only day 117). Day 183 studies the samba de roda circle's manners with no note (the
  frame flags its religious settings; day 179 has it). Day 61's spoken item is fixed as "how manners differ between the
  powwow and the concert hall", though a school may leave the powwow study out.
- **Why it matters.** ARTS-BRIEF and sequence-write rule 9: each day that meets a flagged work names the flag.
- **Fix.** Day 51 note: "Sensitivity: a social song only; the Grand Entry and honor songs are ceremonial, named and
  not played (see day 53); a school may leave the powwow study out." Day 115 note: "Sensitivity: pungmul's village-rite
  roots named and heard only (see day 117)." Day 183 note: "Sensitivity: samba de roda is also sung in religious
  settings; the setting studied is the secular performance the unit plan recorded (day 179)." Day 61 goal: "between the
  powwow (or, where that study was left out, the school assembly) and the concert hall". Confidence: firm.

### 10. Small order points

- **LAYER** sequence. **REPEAT** new.
- Day 85 keeps the twelve-bar blues pattern, which moves through I, IV and V, but IV is first taught on day 105
  (unit 7). Fix: day 85 note "the pattern is kept as bars and its changes heard as home, away and back; the chord
  names wait for unit 7".
- Unit 12 performs "Sambalelê" with practice true to its culture (MU:Pr6.1.8a) but never retrieves unit 9's culture
  and history work on it (MU:Pr4.2.8c, day 134). Fix: day 181 `retrieves` adds mu-g8-read, note "samba's roots in Bahia
  (day 134) retrieved in the opener".
- Days 59, 123 and 187 change the composition after the dress rehearsal, with one rehearsal left before the concert.
  Fix: each note adds "changes after the dress rehearsal stay small (a bar, a marking) so the last rehearsal can carry
  them; larger changes were made on day 54 (118, 182)".
- Confidence: likely.

### 11. Stale and contradictory lines in the .md

- **LAYER** process. **REPEAT** yes (stale notes recur in earlier reads).
- "For the lead" item 4 says Music 3 to 5 has no scope and sequence yet; it now has one (its gate passes), and every
  mu-g5 row's last use there is in year 5 (respond and choose day 144, express and invent day 158, document and revise
  day 176, read and perform day 192), so the retrieval calls stand. Fix: replace item 4 with "Checked against Music 3
  to 5's scope (2026-11-26): every mu-g5 row is last used in year 5; retrieval holds." The table's "units 12 and 9"
  cells may then cite those days.
- "Codes not sampled" lists "MU:Pr4.2.8a, 8c (sampled at mid-year)" and then says 8c is sampled on day 165. Fix:
  drop 8c from the not-sampled list.
- The writer's second question (school days or course days for the short year) is answered: fold-in days are course
  days; the "four sessions" line for a year ten school days short is a useful extra and stays.

## The lens checklist (scope and sequence layer)

| Lens line | Result |
|---|---|
| A grade's ids in the wrong year | Met: each year holds only its grade's 21 ids (checked by script) |
| A year with one artistic process missing | Met per year; per unit see finding 7 |
| Works all from one tradition or one century | Met; year 6 range gap in finding 8 |
| Technique that does not get harder across units or years | Met: symbols, then form and tempo signs, then sight-reading; AB and ABA, then variations, then expanded form |
| A plan that needs a daily period in K to 8 | Met: two 40-minute sessions, and a once-a-week path |
| No showing in a unit | Met: every unit has a showing or concert |
| Bar items 1 to 9 | 1, 2, 3, 4, 5, 6, 8, 9 met; 7 met with finding 8; 8's growth mark at risk on the short path (finding 6) |
| Fails if | None triggered |
| ARTS-READ: four processes, technique first, feedback and revision before the end, many cultures | Met but finding 7 |
| ARTS-READ: once-a-week and 10-days-short paths hold | Hold in count and coverage; minutes in findings 5 and 6 |
| ARTS-READ: each year names its grade's standards; every owned code on a day of the right year | Met |
| sequence-read: readiness or retrieval | Met: every assumed row one grade back, retrieval on day 2, no readiness check, day 1 clean; same-year retrievals placed |
| sequence-read: checks that do not repeat | Met: mid-year checks are units 2, 6, 10's own assessments; growth marks only; year-end on units 1 to 3 |
| sequence-read: calendar and leans | Met: week 19 off every grade 6 to 8 check, week 32 finals; SL.6.1 and W.8.1 bridges on days 3 and 137 |
| sequence-read: candidate cells | All settled; one reversed in finding 8 |
| Source map | Not applicable (no base text) |
| Logic model, school_day, no supplies columns | Met |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Days 63, 127, 191: add the expressive aim (and AB or ABA place on day 63) to the composing item | Each part of Cr1.1 asked on the check | days.csv; scope-and-sequence.md checks table |
| Openers of days 12 to 15, 76 to 79, 140 to 143 become rotating listening rounds; codes added; one structure item on days 11, 75, 139 | Listening ids get more than one day, no day added | days.csv; scope-and-sequence.md units 1, 5, 9 |
| Day 2 of each unit: retrieval five minutes a row; reteach in day 3's warm-up and first five minutes | UNIT-PLAN rule 6 timing | days.csv notes |
| Day 21 adds one composer's choice; day 37 adds one creator prompt | Re8.1.6a creators' part | days.csv |
| Once-a-week merged sittings get the minute budgets above; unit 9 listening first, then sight-reading; composing units show to the partner pair only before the check | Assessed parts kept whole | scope-and-sequence.md Shorter path |
| Fold table: baseline look moves into the next day's first practice time | Growth mark kept | scope-and-sequence.md Shorter path |
| Days 41, 106, 168 gain a student connecting line | Four processes in composing units | days.csv; scope-and-sequence.md units 3, 7, 11 |
| Unit 2 candidate kept on day 22 (living woman performer, Africa or the Arab world); unit 1 leave-out swap line | Year 6 range, consistent candidate reasoning | days.csv; scope-and-sequence.md units 1, 2 |
| Sensitivity notes on days 51, 115, 183; day 61 leave-out wording | Rule 9 | days.csv |
| Day 85 note, day 181 retrieval, days 59, 123, 187 notes | Order | days.csv |
| For the lead item 4 replaced; 8c dropped from not-sampled list | Stale and contradictory text | scope-and-sequence.md |

## For Cory

- None new. The frame's supplies ceiling (money) stays where the frame filed it.

## For the lead

- Check MU:Re8.1.6a and 7a's words lines against the national music handout for "creators' and performers'"
  (finding 4); the words file is shared, so the fix is the lead's, not the writer's.

## Sources

- data/standards/ncas-performance-standards-words.txt, the repo's own-words file: the ids' parts.
- From memory, not opened: the national music standards' wording for MU:Re8.1.6a to 8a (finding 4) and
  MU:Cn11.1.6a; marked likely.
- No outside source was fetched; nothing for the source list.

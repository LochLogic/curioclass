# Frame read: World Geography and Ancient Civilizations I (grade 6), 2026-11-13

Reader: the curriculum expert (docs/agents/EXPERT.md), cold. Brief: docs/pipeline/briefs/frame-read.md.

## What I read

- docs/courses/world-geography-and-ancient-civilizations-i/frame.md, in full; its row in data/plans/frames.csv
  (11 units, 160 days). No base text, so no source map.
- The 29 grade 6 rows of data/progressions/social-studies.csv, every column; the grade 5 and grade 7 rows they
  hand to or take from.
- The neighbour frames: docs/courses/social-studies-grade-5/frame.md (seams) and
  docs/courses/world-geography-and-ancient-civilizations-ii/frame.md. No World History I frame exists yet.
- The bar: docs/agents/lenses/social-studies.md, docs/ADOPTION-BAR-SUBJECTS.md (shared core and section 1),
  docs/courses/social-studies/STANDARD.md, docs/FOUNDATION.md section 7, the MA.6 lines of
  data/standards/ma-hss-2018.txt, the C3 ids in data/standards/c3-indicators.txt.
- Every cross-subject row named in the frame, and every ELA, math and science row that names an ss6 row
  (data/progressions/ela.csv, math.csv, science.csv). No grade 6 ELA, math or science frame exists yet.
- Earlier reads: docs/reviews/progression-social-studies-*2026-11-13.md, progression-cross-*2026-11-13.md. No
  earlier frame read exists.
- Gates: `python -X utf8 scripts/plan.py check` (this frame: 0 failures, 11 units, 148 days in units, 12 for
  checks); `python -X utf8 scripts/stale.py check` (16 files, 0 failures). I counted the MA.6 codes by hand: 67, as
  the frame says.

## Verdict

The frame is sound: every one of the 67 anchor codes and the grade 6 C3 indicators sits in one unit, the order is
the anchor's with the one break (Islam beside Judaism and Christianity) given a reason, and the deep-time timeline,
the regional frame and the writing ladder (short claims, Hammurabi, a first report, a longer report) give the year a
real spine. The biggest risk is the human reads: the frame sends only four units to the sensitivity read and two to
a community reader, while the bar asks the read of every unit and FOUNDATION asks a community reader for every
hard-history unit, and four units here teach slavery. The one change that matters most is that list; next, units 7
and 8 are short of days for what they own.

## Findings

### 1. The human reads are fewer than the bar and FOUNDATION require

- **What is wrong.** "Units 2, 7, 10 and 11 need the fresh-agent sensitivity read, and units 10 and 11 a qualified
  person's read." Bar item 12 (ADOPTION-BAR-SUBJECTS section 1) says the fresh-agent sensitivity read covers every
  unit, and C12 fails with no read on record. FOUNDATION section 7 asks "a reader from the community concerned" for
  Native and hard-history content. Units 4 (slavery in Mesopotamia), 5 (slavery in Egypt; Nubian peoples today),
  6 (enslaved rowers) and 9 (enslaved people in the trans-Saharan and Indian Ocean trades; how Africa is shown) are
  hard history and are left off both lists.
- **Why it matters.** Whoever plans the reads (and asks Cory for people) will plan from this sentence and come up
  short; units 4, 5, 6 and 9 would reach "live" without the read the bar makes a door.
- **Fix.** Replace the last sentence of "Sensitive content" with: "Every unit gets the fresh-agent sensitivity read
  (bar item 12). A reader from the community concerned reads units 4, 5, 6 and 9 (slavery in ancient and African
  societies, and how African peoples are shown) and units 10 and 11 (Native peoples of the Caribbean and the
  Americas)." Add "Sensitivity read; community reader" to the last column of units 4, 5, 6 and 9, and "Sensitivity
  read" to units 1, 3 and 8.
- LAYER frame. REPEAT new. Confidence: firm (bar item 12 and FOUNDATION section 7 say it in words).

### 2. Units 7 and 8 are short of days for what they own

- **What is wrong.** Unit 8 has 12 days, "about 9" of them for the research project, which leaves 3 days for
  MA.6.T3g.1 and D2.His.1.6-8: the Silk Roads and sea routes, Persian roads, Alexander's conquests (none taught
  before in grade 6) and one event traced through its causes and effects across places. Unit 7 has 13 days for 10
  codes and three faiths, each taught as history with the scripture named as its followers' account, beside
  archaeology, on a historical map, with present-day communities; that is about 4 days a faith. By comparison unit
  6 has 10 days for 3 anchor codes, unit 5 has 16 for 8, unit 9 16 for 9.
- **Why it matters.** A writer with 3 days cannot teach Persia, Alexander and the Silk Roads and a cause-and-effect
  chain; the likely day is a survey with no sources, which fails bar item 1 ("coverage without depth"). Unit 7 is
  the unit where hurried teaching costs most (sensitivity, the history-versus-scripture line).
- **Fix.** Move 4 days: unit 3 15 to 14 (its action cycle keeps its 4 days), unit 5 16 to 15, unit 9 16 to 14, unit
  7 13 to 15, unit 8 12 to 14. Totals stay 148 in units and 160 in all. New windows for the cross-subject table:
  unit 3 days 26 to 39, unit 4 days 40 to 55, unit 6 days 75 to 84, unit 8 days 100 to 113 (course check 1 after
  day 70). Update frames.csv only if the unit count changes (it does not).
- LAYER frame. REPEAT new. Confidence: likely (a judgment on depth; the arithmetic is firm).

### 3. The electronic map in unit 9 may need an account

- **What is wrong.** ss6-africa-geography and unit 9 ask that "each student makes one simple electronic map with a
  free mapping tool". The free mapping tools most teachers reach for need a sign-in, and most ask a student under 13
  for a parent's consent. FOUNDATION's promises (free, no accounts) and C14 and C15 (a paper path for every tool
  day; no account) cut against an unnamed third-party tool. There is no paper path named for this day.
- **Why it matters.** D2.Geo.3.6-8 asks for paper and electronic mapping, so the day must be built; a writer will
  pick whatever tool is common, and the day then fails C15 or excludes students without an account.
- **Fix.** In ss6-africa-geography's notes and the unit 9 cell, replace "with a free mapping tool" with "with a tool
  that needs no account and stores nothing off the device (a Curio Class single-file map tool, or a web map that
  needs no sign-in), with a paper path: the same keyed map traced and coloured by hand".
- LAYER progression (and frame). REPEAT new. Confidence: likely.

### 4. The growth in latitude and longitude is misdescribed

- **What is wrong.** The Seams table says grade 6 takes latitude and longitude "now in degrees"; Models carried
  says "into degrees"; ss6-mena-maps ends "Carries latitude-longitude from grades 3 and 4 into degrees with signs".
  Grade 4 (ss4-political-map) already finds places "by latitude and longitude in whole degrees", and the same
  ss6-mena-maps note, and the frame's own math 6 line, say grade 6 reads them "with north, south, east and west in
  place of signs". So the row's last sentence contradicts its first, and both frame cells claim as new what grade 4
  taught.
- **Why it matters.** A writer reteaches degrees from scratch (a wasted day) or, following the row's last sentence,
  adds signs that math 6 teaches later and the cross-subject line says unit 3 must not use.
- **Fix.** ss6-mena-maps notes, last sentence: "Carries grade 4's whole degrees (North America, all north and west)
  to a region that crosses the prime meridian, so east and west longitude are both read; directions, not signs."
  Seams row: "Unit 3 (ss6-mena-maps: east and west of the prime meridian)". Models carried: "Unit 3 (ss6-mena-maps,
  east and west longitude)".
- LAYER progression (stale note) and frame. REPEAT yes (the progression fixes of 2026-11-13, item 9, already
  touched ss6-mena-maps for a stale note). Confidence: firm.

### 5. Four anchor codes are taught in part in the rows the writers will build from

- **What is wrong.** Each row below omits words its standard names:
  - MA.6.T3b.3 names mining, farming and animal domestication; ss6-surplus-specialization names "animal power" but
    not mining.
  - MA.6.T3b.4e names the code's "eye for an eye" principle; ss6-hammurabi-code and unit 4 do not.
  - MA.6.T3e.2 asks students to trace the Israelite tribes' migration from Mesopotamia to Canaan; ss6-ancient-israel
    names Abraham, Moses and the tribes but no route traced on a map.
  - MA.6.T4b.4 names gold, ivory and enslaved people in West African trade; ss6-west-africa-trade names gold, salt
    and enslaved people, not ivory.
- **Why it matters.** C1 fails if a traced standard is taught below its wording, and day writers build from the row.
- **Fix.** Add to the notes: ss6-surplus-specialization "mining for copper and tin, and animal domestication";
  ss6-hammurabi-code "the 'eye for an eye' principle, and how it applied differently by class"; ss6-ancient-israel
  "the tribes' route from Mesopotamia to Canaan traced on the historical map, as the Hebrew Bible tells it";
  ss6-west-africa-trade "ivory beside gold". Echo each in the unit's "What students learn" cell.
- LAYER progression. REPEAT yes (the progression fixes made missing parts of codes explicit, item 1). Confidence:
  firm.

### 6. Unit 1 teaches how climate let people spread before the course has taught who spread

- **What is wrong.** MA.6.T2.1's second objective ("explain how those changes allowed human life to spread and
  settle") sits in unit 1 (ss6-timeline-deep-time); where modern humans arose and how they spread (MA.6.T2.2) is
  unit 2.
- **Why it matters.** A day that asks students to explain land bridges opening routes for people they have not yet
  met is answered from nothing; the check on that objective tests a guess.
- **Fix (within unit 1, no standard moves).** Teach the climate objectives last in unit 1 and use grade 4's
  Beringia land bridge (ss4-first-peoples-evidence, which the frame already revisits) as the worked case of
  objective 2, ending the unit with the out-of-Africa map as the question unit 2 opens. Add that sentence to
  ss6-timeline-deep-time's notes. See "Settled by the expert".
- LAYER progression. REPEAT new. Confidence: judgment call.

### 7. Two compelling questions do not fit their units

- **What is wrong.** Unit 1's question ("Which questions should we ask about a place we have never seen?") covers
  the five fields but not the timeline or climate, half of its days. Unit 3's is two questions joined by "and".
- **Why it matters.** Bar item 1 fails a unit whose question is answered without its content; a two-part question
  gives a writer two unit arcs.
- **Fix.** Unit 1: "How can we know anything about people who lived thousands of years ago?" (fields, dates and
  changing climate all answer it). Unit 3: "Why do people live where they do in a dry land?", with "What should we
  do about water where we live?" as the supporting question of the action days.
- LAYER frame. REPEAT new. Confidence: likely.

### 8. One cross-subject lean is missing from the table

- **What is wrong.** e6-reading-range (ELA 6, thread 1) reads "writing systems, law codes and whom they protected,
  beside social studies ss6-writing-systems and ss6-hammurabi-code". The frame lists the Hammurabi lean only.
- **Why it matters.** The ELA 6 frame will not know the writing-systems half arrives in unit 6 (days 77 to 86 now,
  75 to 84 after finding 2).
- **Fix.** In the e6-argument-writing and e6-reading-range line, add "and ss6-writing-systems (unit 6)" and in the
  last column "its writing-systems texts after unit 6".
- LAYER frame. REPEAT yes (cross-subject timing was the subject of progression-cross-2026-11-13). Confidence: firm.

### 9. Stale note: frames.csv

- **What is wrong.** "For the lead" item 5 says the frame did not edit data/plans/frames.csv and that `frame.py
  sync` writes its row. The row is there (world-geography-and-ancient-civilizations-i,11,160) and the gate reads it.
  stale.py did not flag it (unmarked).
- **Fix.** Replace item 5 with: "frames.csv carries the row (11 units, 160 days), written by `scripts/frame.py
  sync`; rerun it if the unit count changes."
- LAYER process. REPEAT yes. Confidence: firm.

## The lens checklist (course frame layer)

| Line | Met, missed or not applicable |
|---|---|
| An anchor standard in the course's topic range has no unit | Met (gate; 67 of 67 counted by hand) |
| The replaced grade 3 year or "your state" keeps Massachusetts-only content | Not applicable (no own-state content in grade 6) |
| No unit lists what the check set adds, or an addition has no recorded source | Met: every unit has the column; the two candidates name their source (New York grade 6, California 6.3) |
| Chronology across grades (lens, progression) | Met: grade 6 ends with the Maya and Andes and hands Islam's spread and Aztec and Inca to grade 9, by reason |
| History in time order, or a reason given (scope and sequence line, read early) | Met: the one break is named |
| Writing from sources builds short to long | Met: units 2, 4, 8, 11 |
| Sensitive topics and the reads | Missed in part (finding 1) |
| Informed action once a year, chosen by students | Met: unit 3, with a held look-back day |

## What is right and should not be touched

- Religions taught as history, each scripture named as its followers' account, no images of Muhammad, no
  devotional practice; the present-day conflict kept out of unit 7.
- Giza's paid and conscripted builders taught while slavery in Egypt is still named.
- Kush read as a record written by outsiders, which grade 7's Indus builds on.
- "Complex society" as a debated working definition that never ranks peoples, counting oral record keeping.
- Indigenous peoples of the Caribbean and the Americas opened in the present tense from their own pages.
- The cross-subject picks (unit 1 does not wait for science 6's geologic time; unit 3 reads coordinates with
  directions so math adds signs; unit 3 reads the two graph quantities separately).

## Settled by the expert

| Choice | Reason | File it touches |
|---|---|---|
| Unit 1 order: the five fields (3 days), the deep-time timeline (4), the climate objectives (3), with Beringia as objective 2's worked case and the out-of-Africa map as the last day's question | Teaches who spread before asking how climate let them (finding 6) | frame unit 1; ss6-timeline-deep-time notes |
| Unit 8 split at 14 days: connections and one traced event 5 days, research 9 | Gives MA.6.T3g.1 and D2.His.1 the days a sourced chain needs | frame unit 8 |
| Unit 2's worked Neolithic town: Catalhoyuk | Inside MA.6.T2.4; open museum and excavation images exist; Jericho stays a named example | frame unit 2 "Check set adds" |
| Look-back for the unit 3 action at the start of unit 5 | Agree with the frame's pick: about three and a half weeks later | frame "For the lead" 3 |
| 45 minutes a lesson | Agree with the pick; C2 needs a stated length | scope and sequence |

## For Cory

- People: with finding 1, grade 6 needs a reader from the community concerned for six units (4, 5, 6, 9, 10, 11),
  not two. Only the number and kind of people are his call.

## What I could not judge

- No grade 6 ELA, math or science frame exists, so the cross-subject leans are checked against the progression rows
  only, not against the other frames' unit order.
- No World History I frame exists, so the hand-on to grade 9 is checked against the wh1 rows only.
- The C3 indicator wording: the repo holds ids only, so the fit of each C3 code to its unit rests on my memory of
  the 2013 text. Finding 2's depth judgment and finding 7 are judgment calls.

## Sources

- data/standards/ma-hss-2018.txt: the MA.6 codes and their content, counted and traced.
- data/standards/c3-indicators.txt: C3 ids; indicator wording from memory.
- docs/ADOPTION-BAR-SUBJECTS.md (C1, C12, C14, C15, section 1 items 1, 8, 12) and docs/FOUNDATION.md section 7: the
  bar for findings 1, 3, 5, 7.
- docs/agents/lenses/social-studies.md: the checklist above.
- No outside source was fetched this run; nothing new for the source list.

Defects were not logged with `scripts/plan.py defect`: the caller asked that only this report be written.

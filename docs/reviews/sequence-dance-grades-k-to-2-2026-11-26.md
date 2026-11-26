# Expert read: scope and sequence of Dance, grades K to 2 (2026-11-26)

Course `dance-grades-k-to-2`. Brief: docs/pipeline/briefs/sequence-read.md with {subject} = arts, as
build/scope-writes/ARTS-READ.md sets it. Read cold; the reader did not write the scope.

## What I read

- docs/courses/dance-grades-k-to-2/scope-and-sequence.md and data/plans/dance-grades-k-to-2/days.csv (all 192 rows,
  every goal and note), read in full.
- Beside them: docs/courses/dance-grades-k-to-2/frame.md (course in brief, Seams, Units, Course-level checks,
  Cross-subject, For the lead); the da-k, da-g1 and da-g2 rows of data/progressions/arts.csv; the 63 K to 2 dance
  lines of data/standards/ncas-performance-standards-words.txt; data/plans/calendar.csv (physical education K to 2,
  computer science grade 2); docs/courses/CALENDAR.md weeks as the frame quotes them.
- The bar: docs/ADOPTION-BAR-SUBJECTS.md "2. Arts" (items 1 to 9, "Fails if", "Scope and sequence states");
  docs/courses/arts/STANDARD.md (3.1 band-year rule, 3.4 time and the once-a-week path); docs/courses/arts/APPROACH.md
  ("Readiness and the baseline look", the 32-session path); build/scope-writes/ARTS-BRIEF.md; the lens
  docs/agents/lenses/arts.md; docs/agents/EXPERT.md; docs/pipeline/briefs/sequence-write.md rule 2 ("Collect once",
  "Each part of each code"); docs/reviews/frame-visual-arts-dance-fixes-2026-11-26.md for what the frame fix pass
  already settled.
- Gates run first: `scripts/sequence.py check dance-grades-k-to-2` 0 failures; `scripts/plan.py check` 0 failures
  for this course (sequence and frame); `scripts/frame.py calendar` places K at arts weeks 18 and 26 and grades 1 and
  2 at 17 and 25, off every core check week; `scripts/stale.py check` 0 failures. My own script confirmed every code
  sits in its own year (K codes on days 1 to 64, grade 1 on 65 to 128, grade 2 on 129 to 192), all 63 codes are on a
  teaching day before an end-of-unit check day, and every `school_day` falls in the week the .md's rule gives.
- No outside source was opened for this read. Where a finding rests on the full NCAS text rather than the words
  file, it says "from memory".
- Not done: logging defects with `scripts/plan.py defect`, because the brief allows no edit but this report. The
  caller may log them.

## Verdict

The scope is sound and close to ready: all 63 ids sit in the right year with every lettered part taught before it
is checked, every unit has technique in steps before the making, one critique and a rehearsed change before its
showing, and works come from four continents and from 1894 to today. The biggest risk is the six course-level
checks: each one collects again, in the same showing form a week later, an id the unit just scored, which breaks
the collect-once and two-week task-form rules, and several check tasks ask only part of the codes they list. The
one change that matters most is to rewrite the six check samples so they reuse the unit record for the
just-finished unit's ids and ask every part of what they sample live. The once-a-week merges and the physical
education leans need a second pass too.

Findings: 9 (2 serious, 4 moderate, 3 minor).

## Findings, most serious first

### 1. Course-level checks re-collect the unit just scored, in the same form (serious)

LAYER frame (and sequence). REPEAT new.

- **What is wrong.** Each check falls two course days (one week) after its unit's end-of-unit days and is a
  showing, the same form. Each samples live an id the unit scored in that window: day 35 (Cr1.1.Ka, Cr2.1.Ka,
  scored on days 32 and 33), day 51 (Cr3.1.Ka, Re8.1.Ka, scored on days 48 and 49), day 97 (Cr2.1.1a, day 95), day
  113 (Cr3.1.1a, day 110), day 161 (Cr2.1.2a, day 159), day 177 (Cr3.1.2a, day 174). sequence-write rule 2 says a
  check within ten days of child-by-child evidence "reuses that record and says so; it never collects the same
  evidence again", and "never repeats a task form given in the last two weeks". The scope's answer, "drawn from
  earlier content" (a new card built from unit 1's elements), changes the material but not the evidence: the child
  shows the same id in the same way a week later. The phrase "carried unscored" is also unclear: a busy writer
  cannot tell whether the unit record is reused for the check or set aside.
- **Why it matters.** Group showing time is the scarcest thing in this course (six groups, 24 minutes). Spending a
  check on an id seen a week before buys no retention evidence and leaves 44 of 63 ids never sampled (the scope's
  own L107 list). This answers the scope's For the lead item 2: yes, the rule bars it as written.
- **Fix.** For each check, the just-finished unit's ids are reused from the unit record ("reused from day N's
  record, not collected again") and dropped from the live sample. The freed minutes sample ids from the units
  before, which are true retention items and shrink the unsampled list. Proposed live samples (same 24 minutes, at
  most one talk or show item a child):
  - Day 35 (year K mid): Pr5.1.Kb, Pr4.1.Kb (kept), plus Pr4.1.Ka (shapes and the circle) and Pr5.1.Kc (body part
    to body part, then a recalled move). Cr1.1.Ka and Cr2.1.Ka reused from days 32 and 33.
  - Day 51 (year K end): Cr1.1.Ka and Pr4.1.Kc (kept, now a unit 2 and unit 1 retention), plus Cr2.1.Kb (a feeling
    card shown). Cr3.1.Ka and Re8.1.Ka reused from days 48 and 49.
  - Day 97 (year 1 mid): Pr5.1.1c and Pr4.1.1b (kept), plus Pr4.1.1a (a path with a facing change). Cr2.1.1a
    reused from day 95.
  - Day 113 (year 1 end): Cr1.1.1b (kept) and Re7.1.1a (kept, but the teacher's phrase is unseen and the item is a
    show item, so it stays), plus Cr2.1.1b (moves for a feeling card or the music). Cr3.1.1a reused from day 110.
    Re7.1.1a was scored on day 111 in a watching day: keep it only because the phrase and the form differ
    (show item after a group dance); if the lead reads the rule strictly, swap it for Pr5.1.1a.
  - Day 161 (year 2 mid): Pr4.1.2b and Pr5.1.2c (kept), plus Pr4.1.2a (clear direction, a symmetrical and an uneven
    shape). Cr2.1.2a reused from day 159.
  - Day 177 (year 2 end): Cr1.1.2b and Re8.1.2a (kept), plus Cr2.1.2b (moves chosen for a mood, with the reason as
    the one talk item). Cr3.1.2a reused from day 174.
  The sample ids live in the frame's Course-level checks table, so the lead applies the frame change; the scope
  then edits the six check rows' `codes`, goals and notes, its Course-level checks table, the unsampled list and its
  For the lead items 1 and 2. This moves no standard between units, so it is not Cory's.
- **Confidence.** Firm on the rule (two clauses of rule 2 agree); a judgment call on which earlier ids to add.

### 2. Several check tasks ask only part of a code they list (serious)

LAYER sequence. REPEAT yes (the "each part of each code" kind found in earlier core reads).

- **What is wrong.** Rule 2 ("Each part of each code") and the read brief require every check task to ask about
  each part of each code it lists. Gaps, against the words file:
  - Day 97: Pr5.1.1c is "change movements and group layouts when asked"; the goal asks only a formation change.
    Pr4.1.1b is "quick, medium and slow speeds; a steady beat at varied tempos"; the goal asks only the beat.
  - Day 113: Cr1.1.1b is "traveling and in-place moves"; the goal says "one element changed in a sequence". Cr3.1.1a
    is "while improvising and when repeating a remembered sequence"; the goal asks only the remembered sequence.
  - Day 161: Pr4.1.2b is "tell short from long phrases; land on strong beats"; the goal asks only the landings.
  - Day 177: Cr3.1.2a is "make choices and try suggestions"; the goal asks only a chosen change. Re8.1.2a is
    "meaning and purpose"; the goal asks only what a clue means.
  - Day 110 (end of unit 7): Re9.1.1a has three parts (several eye-catching moves, what makes them interesting, why
    they were chosen). The goal names two moves "with what makes them interesting"; "why chosen" (in the full NCAS
    text, why the maker chose them; from memory) is taught on day 102 but not asked.
  - Day 159 (unit 10): Cr1.1.2a ("try moves sparked by a starting point, then suggest more places for ideas") is
    scored from the kept idea card only. The card holds the second part; the first part needs the phrase's
    look-for (moves that show the card's starting point).
- **Why it matters.** A unit plan writer builds the look-for list from the goal. A part that is not in the goal will
  not be on the guide, and the id will be marked met on half of it.
- **Fix.** Add the missing part as one more look-for on the same dance, with no time added: day 97 "and one move
  changed on the call" and "the same move at quick, medium and slow"; day 113 "a traveling and an in-place move,
  each with one element changed" and "a suggested change tried first in a short improvisation"; day 161 "and say
  whether a phrase the teacher claps is short or long" (as the show item, not a talk item); day 177 "a chosen
  change and one the teacher suggests" and "what the dance is for"; day 110 talk item "what makes it interesting,
  and why the dancer might have picked it"; day 159 "Cr1.1.2a: moves that show the card's starting point
  (look-for) and the kept card's two more idea places". Where finding 1 drops a code from a check, its gap goes with
  it.
- **Confidence.** Firm (words file and rule agree).

### 3. The once-a-week merges are uneven, and the watching and performance units are crushed (moderate)

LAYER sequence (merges) and frame (unit 4 session count). REPEAT new.

- **What is wrong.** The frame sets the session counts and the scope marks the merges. The scope's merges put
  five teaching days into one 40-minute session in the watching units: unit 3 "37 to 41" (two works, the
  candidate African dance, four response ids and a retrieval), unit 7 "99 to 103" (Kpanlogo, Bharatanatyam, four
  ids), unit 11 "163 to 167" (breaking, flamenco, four ids). The performance units put four understanding days in
  one session: unit 8 "115 to 118" and unit 12 "179 to 182" (the hoop dance, Kpanlogo, set questions and a personal
  dance, with the hoop dance's sensitivity framing). Year K unit 4 is worst: its frame-set five sessions leave two
  teaching sessions for nine teaching days and five new ids ("53 to 58": a film, the marked area, a painting, a
  prop, recalled moves and the family dance begun). Meanwhile the first unit of each year keeps a ratio near 2.4
  days a session. On this path the day 2 retrieval also lands in the hook session, which the scope does not say.
- **Why it matters.** "No assessed or owned part cut" holds on paper but not in the room: a kindergarten class
  cannot meet two works, a painting and a prop and begin a dance in 40 minutes, so a teacher on this path will cut
  something unplanned, most likely the connecting items that are checked on day 62. The response and connecting
  ids are exactly the ones a once-a-week school is most likely to lose.
- **Fix.**
  - Merges, settled here (same session counts, same kept order): unit 3: 37 to 39; 40 to 43; 44 to 47; 48; 49; 50.
    Unit 7: 99 to 101; 102 to 105; 106 to 109; 110; 111; 112. Unit 11: 163 to 165; 166 to 169; 170 to 173; 174;
    175; 176. Unit 8: 115 to 117; 118 to 121; 122 to 125; 126; 127; 128. Unit 12: 179 to 181; 182 to 185; 186 to
    189; 190; 191; 192. In each third session the critique and the rehearsed change sit together, as the frame's
    unit 4 model already allows.
  - Add one line to the Shorter path section: "On the once-a-week path the retrieval task runs in the unit's first
    session, after the hook and the question."
  - For the lead (frame): year K's once-a-week units become 9, 7, 6 and 6 sessions (unit 1 loses one: 1 to 3; 4 to
    8; 9 to 11; 12 to 14; 15; 16 and 17; 18; 19; 20), so unit 4 runs 53 to 55; 56 to 58; 59 to 61; 62; 63; 64. The
    year still totals 32.
- **Confidence.** Likely (strong reasoning from the session arithmetic; no outside source).

### 4. Same-year physical education overlaps in years 1 and 2 are missed (moderate)

LAYER sequence and frame. REPEAT yes (same kind as the frame read's DE 4 on physical education boundaries).

- **What is wrong.** The scope says "No bridge needed in years 1 and 2", following the frame's Cross-subject table,
  which names only physical education units 1, 2, 13 and 21. data/plans/calendar.csv shows two more same-week
  contacts: physical education grade 1 unit 8, "Ways to travel... change my path, my speed" (weeks 1 to 4), in the
  same weeks dance unit 5 teaches Pr5.1.1a (ways to travel) and Pr4.1.1a and 1b (paths, speeds; days 65 to 73); and
  physical education grade 2 unit 15, "Circuit sequences: link a travel, a jump and a balance" (weeks 1 to 4),
  beside dance unit 9's sequences on pathways (days 129 to 133). Physical education K unit 7, "Moving and feeling"
  (weeks 29 to 32), follows dance unit 2's feeling dances; dance teaches first, so it needs naming only.
  Separately, computer science grade 2 units 2 and 3 (weeks 7 to 20) build programs from "dance cards"; that lean is
  computer science's to bridge, and dance year 2 asks nothing of it.
- **Why it matters.** The lens names double-teaching physical education's moves as an error, and two teachers using
  different words for "path" and "speed" in the same week confuses six-year-olds.
- **Fix.** Days 66 and 70 notes: "Physical education grade 1 unit 8 (weeks 1 to 4) teaches traveling, paths and
  speed as motor skill in the same weeks; this day uses the traveling as material for paths and formations, teaches
  only the dance words, and uses physical education's cue words where the school's teacher has taught them." Day 130
  note: the same line for physical education grade 2 unit 15. Rewrite the scope's Leans paragraph to name units 7,
  8 and 15 and drop "No bridge needed". For the lead: add the two rows to the frame's physical education table and
  to the physical education K to 2 frame's matching cells.
- **Confidence.** Firm (calendar.csv rows and the lens agree).

### 5. Seven of the twelve fold-in days carry the unit's baseline look (moderate)

LAYER sequence. REPEAT new.

- **What is wrong.** Fold-in days 24, 44, 69, 86, 122, 133 and 150 each hold the unit's baseline look; the scope
  moves it "to that warm-up". A baseline look rotates through 30 children; a 5-minute warm-up cannot hold it, so on
  the short year those units lose the first of the two marks the growth evidence rests on (bar item 8, APPROACH
  "Growth").
- **Fix (settled).** Fold-in days become: year K 6, 11, 14, 27; year 1 73, 89, 103, 106; year 2 138, 153, 167, 170.
  Each is a fluency day with no baseline, no candidate work and no assessment, whose practice folds into the next
  day's warm-up (day 41 is kept because it carries year K's only African work). Move the "Fold-in day (shorter
  path)" note to those rows and remove it from 24, 44, 69, 86, 122, 133 and 150. The 160, 480 and 180 totals stand.
- **Confidence.** Likely.

### 6. Units 7 and 11 use a same-year row without retrieving it (moderate)

LAYER sequence. REPEAT yes (retrieval placement, found in earlier reads).

- **What is wrong.** Unit 3 retrieves da-k-elements on day 38 because its responses need unit 1's words. Units 7
  and 11 do the same work without the retrieval: unit 7's descriptions use unit 5's quality words (day 102 note:
  "Quality words from unit 5 carry the descriptions"; da-g1-elements), and unit 11's patterns that build need unit
  9's phrases (the scope's "Why this order"; da-g2-elements). Neither is in `retrieves`.
- **Fix.** Day 102: add da-g1-elements to `retrieves` and the note "unit 5's quality words recalled in the first
  minutes (earlier this year)". Day 165: add da-g2-elements and "unit 9's phrases and strong beats recalled in the
  first minutes (earlier this year)". Add both to the scope's same-year list in "Readiness and retrieval".
- **Confidence.** Firm (rule 2 and the scope's own unit 3 practice).

### 7. Two year-end checks ask for a dance last danced months before (minor)

LAYER sequence. REPEAT new.

- **What is wrong.** Day 113 asks for a change in "the remembered unit 5 dance", last danced on day 81 (about 16
  weeks earlier); day 177 asks for a change to "unit 9's pathways dance", last danced on day 145. Neither check day
  has relearning minutes.
- **Fix (settled).** Respond days 112 and 176: the pairs not retrying rehearse the unit 5 (or unit 9) dance from its
  step card; the check day's warm-up runs it once. Name both in the notes.
- **Confidence.** Likely.

### 8. Three baseline looks sit on the day the skill is first taught (minor)

LAYER sequence. REPEAT new.

- **What is wrong.** The frame puts the baseline look "during the first practice days" and scores nothing from a
  first-teaching day. Days 104 and 168 ("Baseline look begins") and 183 are understanding days that first teach the
  look-for's skill.
- **Fix (settled).** Move the baseline look from 104 to 106 (fluency), from 168 to 171 (first making day), and from
  183 to 185 (first build in the zones); update the notes on 103 and 189 and the scope's Assessments lines for units
  7, 11 and 12.
- **Confidence.** Likely.

### 9. Two text errors (minor)

LAYER sequence. REPEAT new.

- "Day counts" says "168 in the twelve units"; the listed counts add to 180 (60 a year), matching the frame. Change
  168 to 180.
- For the lead item 3 points to "the frame.py calendar run in the final report", which no reader of the file can
  open. Point to the frame's For the lead 1 instead, which lists the shared weeks.

## What is right and should not be touched

- The band-year statement on the first page, the per-year id lists and headings, and the mixed-grade line.
- The `school_day` rule and the check weeks (K 18 and 26; grades 1 and 2, 17 and 25), all off core check weeks.
- Technique before making in every unit, the one critique on an application day, a rehearsed change, a showing,
  then the checks and a respond day; respond days that act on the check only.
- The readiness and retrieval table: every year 1 and 2 row assumes one grade back, so retrieval, never readiness,
  and day 1 of every unit stays clean.
- The range of works and the sensitivity handling (Revelations, Bharatanatyam, the hoop dance, Kpanlogo, flamenco
  and breaking each with a named flag and a leave-out line), and the safety rules on every moving day.
- Each candidate is settled with 0 days or a reason for dropping it.

## Lens checklist (scope and sequence layer)

| Lens line | Result |
|---|---|
| A grade's ids in the wrong year | Met (script check) |
| A year with one artistic process missing | Met: every year, and every unit, touches all four (units 1, 5, 9 claim only performing) |
| Works all from one tradition or one century | Met: Africa, the Americas, Asia, Europe; 1894 to today; living makers each year |
| Technique that does not get harder | Met (frame's ladder kept in the days) |
| A plan that needs a daily period | Met: two sessions a week, once-a-week path marked (see finding 3) |
| No showing in a unit | Met: every unit shows, eight to a partner class or families |
| Response with no discipline words (unit lens, checked at scope level) | Met: words named on the days that teach them |
| Five disciplines planned as one; double-teaching physical education | Partly: see finding 4 |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Once-a-week merges for units 3, 7, 8, 11, 12 as in finding 3 | No session holds more than four teaching days or two works | docs/courses/dance-grades-k-to-2/scope-and-sequence.md |
| Fold-in days K 6, 11, 14, 27; year 1 73, 89, 103, 106; year 2 138, 153, 167, 170 | Keeps every baseline look on the short year | scope-and-sequence.md, days.csv notes |
| Same-year retrievals: da-g1-elements on day 102, da-g2-elements on day 165 | Units 7 and 11 use those rows, as unit 3 does | days.csv `retrieves` and notes; scope |
| Respond days 112 and 176 rehearse the unit 5 and unit 9 dances; check warm-ups run them | Year-end checks ask for those dances | days.csv notes |
| Baseline looks moved 104 to 106, 168 to 171, 183 to 185 | First practice day, not first teaching day | days.csv notes; scope |
| Missing parts added as look-fors on days 97, 110, 113, 159, 161, 177 (finding 2) | Each part of each code, no time added | days.csv goals and notes; scope |
| Retrieval on the once-a-week path runs in the first session after the hook | The path merges day 1 and day 2 | scope "Shorter path" |
| Text fixes: 168 to 180; For the lead 3 pointer | Arithmetic and a dead pointer | scope |

For the lead, not settled here (frame changes): the six check samples in finding 1; year K once-a-week counts 9, 7,
6, 6; the two physical education rows in finding 4.

## For Cory

Nothing new from this read. The frame's own items for Cory stand (a filmed set of unseen phrases; the $50 supplies
ceiling).

## What I could not judge

- Whether a 4-minute group slot holds the look-fors once finding 2's parts are added; the first unit plan's timing
  should test it with a class of 30.
- The suitability of the picked works and excerpts (left to the sensitivity agent, as the frame plans).

## Sources

None opened for this read; it rests on the repo's own files listed above. The Re9.1.1a "why chosen" reading rests on
the full NCAS text from memory.

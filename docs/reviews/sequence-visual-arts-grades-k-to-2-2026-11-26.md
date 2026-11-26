# Expert read: scope and sequence of Visual Arts, grades K to 2 (2026-11-26)

Course `visual-arts-grades-k-to-2`. A cold read by the curriculum expert (PRODUCTION-PATH step 3), done as
docs/pipeline/briefs/sequence-read.md says, with build/scope-writes/ARTS-READ.md and ARTS-BRIEF.md. I did not write
the scope; this file is the only file I changed.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/arts.md, docs/ADOPTION-BAR-SUBJECTS.md section "2. Arts" (items 1 to 9
  and "Fails if"), docs/courses/arts/STANDARD.md (3.1, 3.4) and docs/courses/arts/APPROACH.md ("Kinds of day",
  "Readiness and the baseline look", "Scoring creative work", "Critique", "Practice that returns", "Supports",
  "Sensitive ground", "Pacing").
- build/scope-writes/ARTS-BRIEF.md and docs/pipeline/briefs/sequence-write.md (rules 1 to 11).
- docs/courses/visual-arts-grades-k-to-2/scope-and-sequence.md and data/plans/visual-arts-grades-k-to-2/days.csv (all
  192 rows), read cold.
- Beside them: the frame (all of it), the 24 va-k, va-g1 and va-g2 rows of data/progressions/arts.csv (every
  `assumes` cell is the same thread one grade back), the 45 K to 2 visual arts lines of
  data/standards/ncas-performance-standards-words.txt, docs/courses/CALENDAR.md (the course's three rows) and the
  course's rows in data/plans/calendar.csv, the kindergarten math rows of calendar.csv (flat shapes, weeks 9 to 13),
  the frame reads (docs/reviews/frame-visual-arts-grades-k-to-2-2026-11-25.md, its codex read and its fixes, and
  frame-visual-arts-dance-fixes-2026-11-26.md) and the other arts scope reads of today (media arts 3 to 5 and 6 to 8)
  to tag repeats.
- Gates: `scripts/plan.py check` (0 failures for this course; failures elsewhere are other courses'),
  `scripts/sequence.py check visual-arts-grades-k-to-2` (0 failures), `scripts/frame.py calendar` (visual arts weeks
  18 and 26 in K and grade 1, 17 and 26 in grade 2, matching CALENDAR.md and the frame), `scripts/stale.py check`
  (0 failures). I also checked by script that the .md's per-unit "Processes" lists match the CSV notes (they do), that
  every one of the 45 ids sits only in its own year, and that `school_day` and calendar.csv give the same weeks.
- No new outside source was opened. The standards' wording rests on our own-words file; timing and room judgments
  rest on the arts approach page and on memory of K to 2 art rooms, marked so.

## Verdict

Sound and careful: the band-year rule holds (15 ids a year, each only in its own year), every unit has a critique, a
revision and a showing before its end-of-unit assessment, techniques come before the making in the full path, the
works range widely with settings and sensitivity lines, and the calendar weeks and retrieval openers are right. The
biggest risk is in the evidence, not the order: both Cr2.1 mid-year checks sample one dry medium for codes that ask
for varied materials (and, in year 2, the child's own interest), and unit 9 scores Cr2.1.2a on a piece that never got
the critique and revision. The one change that matters most is to rewrite those three Cr2.1 tasks (findings 1 and
2, settled below); the once-a-week table also needs two days moved so nothing is used before it is taught (finding
3). 11 findings, none that changes scope.

## Findings, most serious first

### 1. The Cr2.1 mid-year check tasks do not ask the parts of their codes

LAYER sequence. REPEAT yes (items that list a code but ask only some of its parts, as in today's media arts reads).
Confidence: firm against the words file.

- **What is wrong.** Day 35 (year K mid-year) claims VA:Cr2.1.Ka ("experiment ... with varied art media") on "a
  fresh crayon-and-paper making task": one medium, so "varied" cannot be seen. Day 161 (year 2 mid-year) claims
  VA:Cr2.1.2a ("try varied materials and tools ... to follow your own interests") on "a tint-and-shade mood task in
  crayon": one medium and a set subject, so neither "varied" nor "own interests" is asked. Unit 1's own look-for
  (four materials, two ways each) and unit 9's (a material chosen for the child's interest) show the scope knows
  the parts; the checks drop them.
- **Why it matters.** A unit plan writer builds the check from the day's goal. As written, a child can meet Cr2.1 on
  the year's only retention sample without using a second medium or making any choice, and the record overstates
  what was checked ("Checks claim only what they sample", rule 2).
- **The fix (settled below).** Keep check days dry, as the frame requires, and use two dry media. Day 35: the task
  uses crayon and torn paper with a glue stick, each tried two ways (the unit 1 look-for, on new paper). Day 161:
  the child picks two of crayon, colored pencil and torn paper for a picture of a subject of their own interest, with
  light and dark made by pressure or paper choice; the look-for reads "two materials chosen, used for the child's
  own subject". Day 99 (year 1) is fine as written.

### 2. Unit 9 scores Cr2.1.2a on a piece that had no critique or revision

LAYER sequence. REPEAT new. Confidence: firm (APPROACH "Critique": "the check scores work revised after it").

- **What is wrong.** Unit 9's critique (day 139) and revision (day 140) are on the mood painting, but day 143 scores
  VA:Cr2.1.2a "on the choice-day work" (day 137), a one-session piece nobody gave feedback on. The revised mood
  painting is scored for nothing. The baseline look (day 133) also watches "tints and shades for a mood", not the
  scored look-for, so the unit's growth mark compares two different things.
- **Why it matters.** The bar's item 6 and the approach page tie the score to revised work; here the feedback loop
  and the score sit on different pieces, so a child's revision cannot raise the mark.
- **The fix (settled below).** Make the mood painting follow the choice day: day 137 stays the choice day (paper,
  clay or paint on the child's interest) and its note adds "the interest found today is the subject of the mood
  painting"; days 138 to 140 paint that subject calm or stormy with tints and shades. Day 143's Cr2.1.2a look-for
  scores the revised mood painting with the choice-day work kept beside it: "a material tried for the child's own
  interest (choice day), carried into the painting with tints or shades used on purpose". The day 133 baseline
  watches the same two look-fors on the tint and shade ladders.

### 3. The once-a-week table uses two days before what they need

LAYER sequence. REPEAT yes (used before taught, as in today's media arts 3 to 5 read). Confidence: firm.

- **What is wrong.** Unit 9's first session is 129+131+135, but day 135 ("tell how tints and shades help make one
  calm and one stormy") needs tints and shades, which are shown in session 2 (130+132+133). Unit 10's session 3 is
  150+153, but day 153 practices the two-way talk "on the sketches", which are made on day 152 in session 4.
- **Why it matters.** A school on the once-a-week path (the frame's rotation answer to bar item 9) gets two
  sessions that cannot run as written.
- **The fix (settled below).** Unit 9: 129+131; 130+132+133; 134+135+136; then as written (still 8 sessions).
  Unit 10: 145+147+151; 146+148+149; 150+152; 153+154; 155; 156+157+158; 159; 160 (still 8 sessions). The
  critique stays on 155, the revision on 156.

### 4. On the once-a-week path, the exhibit units merge the check with the family showing

LAYER sequence (the frame says "the showing (the check)" but not how two end days fold). REPEAT new. Confidence:
judgment call (from memory of K to 2 family showings).

- **What is wrong.** Units 4, 8 and 12 merge their two end days (62+63, 126+127, 190+191) into one 40-minute session
  that must hold the self-check, six groups of five at the teacher's table (24 minutes) and the family showing where
  each child shows and tells. One adult cannot host families and hear six table groups in the same 40 minutes; the
  full path keeps them apart for that reason.
- **Why it matters.** The Pr4.1 look-for (reasons said as each child shows) and the talk items compete for the same
  minutes, so one gets dropped on the day.
- **The fix (settled below).** On the once-a-week path the merged session is the check: the talk items plus the
  Pr4.1 reasons heard at the teacher's table (the child tells why each work went in, or why the piece fits its group,
  or guides the teacher through the mounted work for Pr5.1.1a), scored as on the full path. The family showing is
  held as a drop-in gallery at arrival or pick-up, or at a family evening, unscored; the class still shows to an
  audience (bar item 4). Write this under the once-a-week table.

### 5. Two owned codes are taught only on the hook day

LAYER sequence. REPEAT new. Confidence: firm (days.csv and the words file).

- **What is wrong.** VA:Pr4.1.1a (why people prize some objects and artworks over others) is taught on day 117, the
  hook, and next appears on check day 126. Day 123 carries the code, but choosing a work to mount is not the code's
  demand. VA:Pr6.1.2a (how art shown inside and outside school helps communities) is taught only on day 181, the
  hook, and scored on day 190; the "inside school" part is never asked, and the talk item asks only about the public
  art or a museum.
- **Why it matters.** A hook opens a question; it is not a teaching day with practice. Grade 1 and grade 2 children
  get one exposure and then a scored talk item nine days later. Days by load: each of these units gives 3 to 5 days
  to its other ids.
- **The fix (settled below).** Day 119 adds the question "why would a museum keep this alebrije, made today, beside
  William?" and carries VA:Pr4.1.1a; day 122's fluency adds a two-minute "which would a museum keep, and why" card
  pair and carries VA:Pr4.1.1a. Drop VA:Pr4.1.1a from day 123. Day 187 adds "who our exhibit is for and how it helps
  our school" and carries VA:Pr6.1.2a; day 190's item lets the child answer about Cloud Gate, a museum or the class
  exhibit ("inside or outside school").

### 6. Year 2's drawing technique, the planned event scene, is never shown in steps

LAYER sequence. REPEAT new. Confidence: likely (the frame's technique ladder against days.csv).

- **What is wrong.** The frame's "Techniques that get harder" names drawing a planned event scene as year 2's drawing
  step (after the crayon grip in K and the line family and observational drawing in year 1). In unit 11, day 169 looks
  at "how artists picture an event" and plans the picture, then day 173 makes it. No day shows the scene's steps on a
  step card and no fluency day drills them; day 171's drill is a join drill.
- **Why it matters.** It is the lens's first unit error ("a making task with no technique taught first") and the
  bar's "Fails if" line, on a scored product (VA:Cn10.1.2a). It also flattens the drawing ladder at its top step.
- **The fix (settled below).** Day 169 shows the event scene in named steps on a step card (the ground line raised
  to make room, the main people large and in front, what is happening shown by an action, the place behind), using
  The Harvesters from day 168 as the model, then plans. Day 171's fluency adds a two-minute "person doing an action"
  drill beside the join drill.

### 7. Baseline looks often sit on days where the look-for cannot be seen, and two are lost on the short year

LAYER sequence. REPEAT yes (today's media arts 3 to 5 read found fold-in days cutting the baseline). Confidence:
firm.

- **What is wrong.** APPROACH "Growth" gives each child two marks on the same look-for, baseline and check. Here the
  baseline day often cannot show the look-for: day 22 watches "three tries on one idea page" on a mixing strip;
  day 105 watches "objects grouped by use, a label on each group" on a pinch-pot drill; day 149 watches "three
  solutions sketched with the partner" on a fold drill; day 166 watches "old use and new use shown" on a join drill;
  days 4 and 68 watch materials or prints not yet shown (paint, dough and paper; printing). Unit 9 is in finding 2.
  On the 10-days-short path, two fold-in days (122, 186) carry the baseline and the fold note does not say where it
  goes.
- **Why it matters.** A mark taken where the look-for cannot appear is "not yet" for every child, so the growth line
  in the logic model measures nothing.
- **The fix (settled below).** Give each baseline a two-minute task that shows the look-for, in that day's opener:
  day 22, three quick tries at one idea on the strip's edge; day 68, the four lines only (prints added to the
  baseline on day 74); day 4, crayon two ways only, paint and dough added on days 6 and 9; day 105, a four-card sort
  by use with a label; day 149, partners sketch two quick ways for one standing shape; day 166, "what was it, what
  could it be" told for one cast-off. On the short year, the fold notes of days 122 and 186 add "the baseline look
  moves with the drill".

### 8. Same-year rows the frame says a unit needs are leaned on with no retrieval

LAYER sequence. REPEAT yes (same-year retrieval missing, as in today's media arts read). Confidence: likely (the
`assumes` cells are only one grade back, so the gate cannot see these; the frame's "Why this unit, here" names them).

- **What is wrong.** Rule 2 opens a row used earlier the same year as a retrieval task. The scope does this well in
  units 2, 3, 4 and 6 but not where the frame names a same-year need: unit 3 judging "needs unit 1's look and tell"
  (no va-k-look retrieval in unit 3); unit 7 names features of form "using unit 6's art words" (day 101, the hook,
  asks for them with no retrieval); unit 11's "meaning from mood needs unit 9's mood" (day 168 says "Mood from unit
  9" in prose only) and day 165 "uses unit 10's many solutions".
- **Why it matters.** The `retrieves` column feeds scripts/spacing.py; prose-only retrieval is not counted, and the
  writer of day 168 has no opener to build.
- **The fix (settled below).** Add a five-minute opener and the `retrieves` entry: day 39 va-k-look (look and tell
  on a known picture); day 103 va-g1-revise (name line, shape, color, texture in a known work); day 165 va-g2-ideas
  (sketch two ways first); day 168 va-g2-look (sort three known cards by feeling). Day 101 keeps the hook clean of
  the art-words ask beyond naming what is seen.

### 9. Three items drop a part of their code

LAYER sequence. REPEAT yes (part coverage). Confidence: firm against the words file.

- **VA:Re8.1.1a** ("sorting subject matter and naming features of form"): days 101, 103 and the day 112 item ask for
  lines, shapes and colors and "what it is about", but never for sorting what is in the work. Fix: day 101's goal
  adds "sort what is in it (people, animals, things, plants)"; the day 112 item asks the child to sort two or three
  things in the unseen work before naming its lines, shapes and colors.
- **VA:Pr5.1.1a** ("pose and answer questions"): the exhibit-plan card gives the questions and the child only answers.
  Fix: day 121 and the card add one question the child asks of their own ("Where will people see it?"), dictated or
  written, read on day 127.
- **VA:Cr1.2.2a** ("... from varied materials"): day 154 says "with different materials" but the day 159 look-for
  reads only the question and the made work. Fix: the look-for adds "made with two or more materials".

### 10. Unit 9's connecting day is a responding day

LAYER sequence. REPEAT new (the reverse of today's media arts 6 to 8 finding 1). Confidence: likely.

- **What is wrong.** Unit 9's only connect day is 131, the looking walk, which is VA:Re7.1.2a (describing places), a
  responding id. The two bridges on day 129 are labeled "respond" only, with no setting. Every other unit's connect
  label sits on a work's setting or a child's life.
- **Why it matters.** The scope says every unit holds all four processes (bar item 1, the lens); unit 9 holds three
  in fact, and bar item 7 wants the setting taught.
- **The fix (settled below).** Day 129's note adds the work cards' settings (Hiroshige's print sold in a series of
  views of the city of Edo; Monet's painting of the bridge in his own garden in France) and the label "connect"; day
  131 stays respond.

### 11. The shorter-period check budget and the short year's week claim

LAYER sequence. REPEAT new. Confidence: likely (arithmetic).

- **What is wrong.** In a 30-minute period the scope keeps the six table groups at three minutes each: about 36
  seconds a child for up to two talk items and, in units 1, 5 and 9, a tray item. The full path already allows only
  48 seconds (the frame's settled figure). Separately, the 10-days-short note says "the course-level check days keep
  their weeks", which holds only if the lost days fall after the folds; years K and 1 fold only two days before the
  mid-year check.
- **Why it matters.** At 36 seconds a child the talk items become one-word answers a teacher cannot mark met or
  partly; the week claim may mislead a school that loses days in autumn.
- **The fix (settled below).** Shorter period, check days only: set-up 3 and clean-up 3 (drawing tools only), six
  groups at four minutes (24), self-check the day before: 30 minutes. Short year: replace the sentence with "the
  check days keep their weeks when the lost days fall after the folds; otherwise the check moves at most one week
  later, never into a core check week of the grade".

## What is right and should not be touched

- The band-year rule, stated once on the first page, with the mixed-grade line; no pre-kindergarten id claimed.
- `school_day` counted plainly (160 x y + ceil(5n / 2)) and matching calendar.csv and CALENDAR.md's weeks.
- Readiness: correctly none (every `assumes` cell is one grade back) and every year 1 and 2 unit retrieves its
  thread on day 2, with day 1 clean.
- The "collect once" correction of the frame's year-end rows (For the lead item 1): days 48 and 49, 112 and 113, 176
  and 177 are eight school days before each year-end check, inside the rule's ten-day window. I agree with it.
- Technique before making in every unit of the full path; one critique on the second making day, revision next,
  showing before the check; dry check days; the portfolio piece and spoken reflection in every unit.
- The works list: every year crosses regions, periods and living makers, each candidate settled with a reason, and
  every flagged work (Mahlangu, Tar Beach, Gee's Bend, Martinez, William, alebrijes, Asawa, El Anatsui, papel
  picado) carries its sensitivity line on its day.
- The cross-subject contacts timed against the kindergarten math calendar (shapes by pointing before week 9).

## What I could not judge

- Whether 48 seconds a child at the teacher's table (the frame's figure) yields markable talk in kindergarten; it
  needs a trial with children.
- Whether the step cards will make each demonstration fit in one session on the once-a-week path, where some
  sessions hold four or five course days (unit 1 session 4, unit 2 session 2, unit 7 session 1). The four kept parts
  are present in every unit; the load is the unit plan's to test.

## Sources

- docs/courses/arts/APPROACH.md and STANDARD.md 3.4: kinds of day, growth, critique, the 32-session path.
- data/standards/ncas-performance-standards-words.txt, lines 1011 to 1181: the parts of each id.
- docs/ADOPTION-BAR-SUBJECTS.md section 2: items 1 to 9 and "Fails if".
- From memory: K to 2 specials rooms and family showings (finding 4), timing per child (finding 11).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 35 task: crayon and torn paper with glue stick, each two ways | Cr2.1.Ka asks for varied media; check stays dry | days.csv day 35 goal and note; .md check table |
| Day 161 task: two of crayon, colored pencil, torn paper chosen for the child's own subject; light and dark by pressure or paper | Cr2.1.2a asks for varied materials and own interests | days.csv day 161; .md check table |
| Unit 9: choice-day interest becomes the mood painting's subject; day 143 scores the revised painting with the choice-day work beside it; day 133 baseline on the same look-fors | Score the work that was critiqued and revised | days.csv days 133, 137, 138, 143; .md unit 9 |
| Once-a-week unit 9: 129+131; 130+132+133; 134+135+136; 137; 138+139; 140+141+142; 143; 144 | Day 135 needs tints and shades first | .md once-a-week table |
| Once-a-week unit 10: 145+147+151; 146+148+149; 150+152; 153+154; 155; 156+157+158; 159; 160 | Day 153 needs day 152's sketches | .md once-a-week table |
| Once-a-week units 4, 8, 12: merged end session is the check (talk items and Pr4.1 or Pr5.1 at the table); family showing held as an unscored drop-in or evening gallery | One adult cannot host families and hear six groups at once | .md once-a-week section |
| Day 119 and day 122 carry VA:Pr4.1.1a with a "why would a museum keep it" question; drop it from day 123 | Code taught only on the hook | days.csv days 119, 122, 123 |
| Day 187 carries VA:Pr6.1.2a ("how our exhibit helps our school"); day 190 item accepts inside or outside school | Code taught only on the hook; "inside school" part | days.csv days 187, 190 |
| Day 169 shows the event scene in named steps on a step card, using The Harvesters; day 171 adds a two-minute action-figure drill | Year 2 drawing technique taught before the making | days.csv days 169, 171 |
| Baseline two-minute tasks: days 4, 22, 68, 105, 149, 166 as in finding 7; days 122 and 186 fold notes say the baseline moves with the drill | The baseline must show the look-for | days.csv those days |
| Openers and `retrieves`: day 39 va-k-look, day 103 va-g1-revise, day 165 va-g2-ideas, day 168 va-g2-look | Same-year rows the frame names | days.csv those days |
| Re8.1.1a sorting step on day 101 and the day 112 item; one child-posed question on the exhibit-plan card (days 121, 127); "two or more materials" on the day 159 Cr1.2.2a look-for | Each part of each code | days.csv days 101, 112, 121, 127, 159 |
| Day 129 note: the two bridges' settings, labeled connect | Unit 9 connect on a work's setting | days.csv day 129; .md unit 9 processes |
| Shorter period check days: set-up 3, clean-up 3, six groups at 4 minutes, self-check the day before; short-year week sentence reworded | Per-child time; honest week claim | .md "Shorter path" |

## For Cory

- Nothing new. The frame's open money item stands: a supplies ceiling of $75 a class a year for K to 2 visual arts
  (frame For the lead item 6), still unanswered.

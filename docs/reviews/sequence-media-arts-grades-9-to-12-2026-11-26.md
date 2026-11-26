# Expert read: scope and sequence, Media Arts, grades 9 to 12 (2026-11-26)

Cold read by the curriculum expert (PRODUCTION-PATH step 3), per build/scope-writes/ARTS-READ.md and
docs/pipeline/briefs/sequence-read.md. I did not write the scope. The only file written is this report; per ARTS-READ,
no `plan.py defect` rows were logged (the caller may log them from the findings below).

## What I read

- docs/agents/EXPERT.md; docs/agents/lenses/arts.md; docs/ADOPTION-BAR-SUBJECTS.md section 2 (items 1 to 9, "Fails
  if"); docs/courses/arts/STANDARD.md (3.2 in full, the rest for the rules cited); build/scope-writes/ARTS-BRIEF.md.
- docs/courses/media-arts-grades-9-to-12/scope-and-sequence.md and data/plans/media-arts-grades-9-to-12/days.csv
  (all 640 rows: goal, codes, assess, retrieves, and notes on every assessed and sampled day).
- docs/courses/media-arts-grades-9-to-12/frame.md (seams, models, the Units table, course-level checks,
  cross-subject, For the lead); docs/courses/CALENDAR.md rule 4 and its 9 to 12 media arts rows; the MA ids' lines in
  data/standards/ncas-performance-standards-words.txt.
- For REPEAT tags: the headings of today's sequence reads for music 9 to 12, visual arts 9 to 12 and media arts 6 to 8.
- Gates: `plan.py check` passes; `sequence.py check media-arts-grades-9-to-12` 0 failures (seven notes "standard
  None is on no day" for the bridge, review and Level 4 units, expected); `frame.py calendar` 0 failures, Level days
  154 each, 616 in units; `stale.py check` 0 failures.
- My own counts (script): every level carries all 18 of its own ids and no other level's; Level 4 carries exactly the
  eleven re-assessed Level 3 ids; every unit's short-path list partitions its days and matches the frame's short
  counts; all 40 ten-short fold-in days are unassessed Fluency days.
- No outside source was opened this run. Judgments on media arts practice rest on the repo's standard lines and on
  memory, marked so.

## Verdict

The scope is sound in its bones: levels claim the right ids, every owned lettered part sits on a day of the right
level, technique days mostly come before making, every unit shows its work and every made piece meets a critique and a
logged revision before it is scored, and the works range across five continents and twelve decades. The biggest risk
is the end-of-unit showing of individual work: units 4, 9, 14, 18 and 19 (and 15 as the frame writes it) schedule 30
students' pieces into one 45-minute day using a note written for six team screenings, so the scored showing cannot
happen as planned. The one change that matters most is to rewrite those showing days so each piece is scored from
the kept work or across a stated window, with the class screening as a showing, not the only scoring moment.
Thirteen findings below; none needs Cory except the community-space question.

## Findings, most serious first

### 1. Individual pieces cannot be screened and marked in one period (serious)

LAYER sequence. REPEAT new. Confidence firm (arithmetic from the days' own figures).

- **What is wrong.** Days 112, 272 and 432 (units 4, 9, 14) carry the note "six teams of five screen in turn ...
  about four minutes each (24)", but these units make one piece per student: 2 minutes (unit 4) and 2 to 3 minutes
  (units 9 and 14). Thirty pieces are 60 to 90 minutes of running time before change-overs, and the look-fors for
  MA:Cr3.1.Ia, IIa and IIIa are "marked at the screening". Day 594 (unit 18) shows 30 individual pieces to their real
  audiences in "showing 25"; day 630 (unit 19) has "each student's showing in turn across the period" for a series of
  three to five pieces each. Unit 15's frame says the cross-platform piece is "made by the student", yet days 445,
  446 and 456 speak of teams and day 470 uses the six-team note.
- **Why it matters.** A teacher following the plan runs out of period with half the class unscreened and unmarked,
  on an end-of-unit assessment day. The lens names set-up and timing that do not fit the session as a day fault; here
  it sits on the scored evidence.
- **Fix (settled below).** Units 4, 9 and 14: the screening day shows every piece in four small-group screening
  circles (or the paper forms on tables), audiences with note cards; the look-fors for Cr3.1.Ia, IIa, IIIa are scored
  from the kept piece after the session, as day 39 already does for a gallery. Unit 18: the showing runs as a window
  (days 594 and, where needed, the school's own event), each piece scored from the kept piece plus the audience
  cards; the note names the window. Unit 19: the series showing is an exhibition (all series set up at once, visitors
  walk a route) and the look-for for Pr4.1.III is marked from the set-up and the kept series, with the walk-through
  split across days 630 and 631 if the room needs it (day 631's reading of responses moves into 632). Unit 15: follow
  the frame (one piece per student), change the words "teams" on days 445, 446 and 456 to "pairs of students", and
  use the exhibition note on day 470.

### 2. Scored ids missing from the codes column on assessed days (moderate)

LAYER sequence. REPEAT yes (music 9 to 12 finding 5: Pr5.1 ids missing from units 5, 10, 15's end lists).
Confidence firm.

- **What is wrong.** MA:Pr6.1.IIa and MA:Pr6.1.IIIa are on no assessed day's codes in their levels: day 310 and day
  470 say in the goal "the kept channel plan / promotion plan scored after", but the codes hold only Pr4.1.II and
  Pr4.1.III. In unit 5 the same plan is named as scored on day 150's goal but coded on day 154. Day 256 names
  "the revision log's refinements (MA:Cr3.1.IIb)" and day 416 names "(MA:Cr3.1.IIIb)" in the goal, but neither code is
  in the column.
- **Why it matters.** Unit plans and the record sheet are built from the codes column; an owned id that is scored
  only in prose is the kind of slip the gate cannot see and a writer will drop.
- **Fix (settled).** Add MA:Pr6.1.Ia to day 150 and remove it from day 154; add MA:Pr6.1.IIa to day 310; add
  MA:Pr6.1.IIIa to day 470; add MA:Cr3.1.IIb to day 256 and MA:Cr3.1.IIIb to day 416.

### 3. End-of-unit items drop parts of their standards (moderate)

LAYER sequence (and frame, whose evidence line carries the same wording). REPEAT yes (media arts 6 to 8 finding 3).
Confidence firm.

- **MA:Re7.1.IIb** names experience, intent and persuasion through several senses. Day 196 and the year-end day 317
  ask only how the clip persuades. Fix: day 196's items take three prompts (what the viewer experiences, the intent
  the senses carry, how it persuades), each with a sight and a sound choice as evidence; day 317 keeps two of the
  three, which a course-level sample may do.
- **MA:Re8.1.II** names personal, social, historical and cultural settings. Day 275 asks for "two settings". Fix: four
  short prompts, one per setting, in the same 30 minutes (day 245 already teaches all four).
- **MA:Pr5.1.IIIc** names conventional, innovative and experimental work. Unit 13 builds only conventional and
  experimental versions. Fix: day 395's look-for asks for one innovative tool or method named in the experimental
  version (day 367 shows one).
- **MA:Cr3.1.Ib** names goals and tastes. Days 91, 98 and 105 log changes "to the stated personal goal" only. Fix:
  the revision log's entries name the goal or the taste each change serves (day 84 shows one of each).

### 4. Prototypes made before their technique is taught, in units 3 and 8 (moderate)

LAYER sequence. REPEAT yes (music 9 to 12 finding 2, visual arts 9 to 12 finding 5: making with no technique day).
Confidence firm.

- **What is wrong.** Day 50 (unit 3) offers prototype one in "erase-and-redraw charcoal, cutouts on a lit sheet, or
  marks on a paper strip"; cutouts and strip marks are first shown on days 51 and 52. Day 206 (unit 8) asks for "a
  one-choice branching sketch"; the branching piece is first shown in steps on day 208.
- **Why it matters.** The bar's item 2 and "Fails if" line: making with no technique taught.
- **Fix (settled).** Unit 3: prototype one (day 50) uses erase-and-redraw only, taught on day 47; cutouts and strip
  marks open on prototype two (day 55), after days 51 and 52. Unit 8: move the prototype-one day to follow day 208
  (new order 203, 204, 205, 207, 208, then the prototype), renumbering inside the unit.

### 5. Unit 18 makes a new piece with no technique day (moderate)

LAYER sequence. REPEAT new. Confidence likely.

- Units 16's pieces each open with "the chosen technique or a new one shown in steps ... the student naming the
  adaptation" (days 495, 509). Unit 18's piece runs nine production days (570 to 588) with no such day, though it is
  made for a new audience and may use a new form. Fix (settled): day 570 becomes that Understanding day ("the piece's
  technique shown in steps from the step cards, the adaptation for this audience named"); production one to nine
  become one to eight. No day count changes.

### 6. The second critique stage in units 3, 8 and 13 has no protocol (moderate)

LAYER sequence. REPEAT new. Confidence firm.

- Days 65, 222 and 382 are a team watching its own rough assembly ("within the team" on day 382); days 66, 223 and
  383 then revise "from the rough-assembly critique", a critique that never ran. The frame and the .md both say
  production units carry two critique stages. Fix (settled): days 65, 222 and 382 run the critique card team to team
  on the rough assembly (describe, ask, suggest, each tied to a look-for), the same form as days 60, 217 and 377.

### 7. Unit 17 claims Create and Produce on essay days (moderate)

LAYER sequence (frame allows at least two processes per unit; ARTS-READ asks all four in every unit). REPEAT yes
(visual arts 9 to 12 finding 8, media arts 6 to 8 finding 1: a process missing from units). Confidence likely.

- The .md lists "Create 537 to 538, 543; Produce or present 548". Those days are essay drafting and a teacher demo of
  the talk. Writing a critical essay is responding, not the creating process; the list pads the unit to pass a rule.
- Fix (settled, the lead may reverse): day 549 becomes "talk notes and a 30-second evidence reel cut from stills of
  the chosen public domain or openly licensed work" (Create), and the reel is shown in the defended talk (Produce or
  present, days 552 to 555); the .md's process line then names 549 and 552 to 555 truthfully. No day is added and no
  id moves. If the lead prefers to keep unit 17 pure criticism, the .md must say plainly that unit 17 is responding
  and connecting only, under the frame's rule.

### 8. The 80-day path packs five days into one while drills stand alone (moderate)

LAYER sequence. REPEAT yes (music 9 to 12 finding 1, visual arts 9 to 12 finding 7). Confidence firm.

- Five-into-one merges: 145 to 149, 305 to 309, 465 to 469 (each holds the self-check, final changes, the showing's
  consent work and the dress run), 502 to 506 and 516 to 520. Meanwhile days 114, 274 and 434, Fluency drills, stand
  as their own short-path days, and mid-unit respond days are merged with two first teachings (24+25+26, 97+98+99,
  180+181+182, 257+258+259, 290+291+292, 340+341+342, 417+418+419, 450+451+452; 576 to 579 with three production
  days). The frame says a merged day never drops a respond day; a respond day sharing 45 minutes with two new lessons
  in practice does.
- Fix (settled): fold 114 into 113, 274 into 273 and 434 into 433 (the drill becomes the written day's 5-minute
  opener), and use each freed day to split its unit's five-day merge so the dress run stands with the consent work
  only (149 alone with 148; 309 with 308; 469 with 468). For the respond merges, pair each mid-unit respond day with
  one day, not two (24 with 25; 26 with 27+28 and so on down the list), keeping each unit's count. Units 16's two
  five-day merges keep their count but split as 502+503 and 504+505+506 (the near-final look stays with production).

### 9. Readiness checks on a level's first day: frame and gate differ (moderate)

LAYER process. REPEAT new. Confidence likely.

- The scope's For the lead 1 is right that the frame puts the Level 2 and Level 3 readiness checks in the last ten
  minutes of days 161 and 321 and that the gate forbids it. In a levels course a student placing in is first present
  on the level's first day, so the rule's reason (keep a unit's first day clean, give the check before the unit)
  points the other way here: the review unit is the readiness unit. Recommendation for the lead: widen the gate's
  exception to the first day of each level in a 9 to 12 levels course, then set `assess` to readiness on 161 and 321.
  Until then the check is in the note only, which a writer may miss.
- Related, minor: Level 4 has no placement path though STANDARD.md 3.2 says each level needs the one before or a
  placement. Fix (settled): day 481's note says a student placing into Level 4 shows work scored against Level 3's
  year-end check and guides, as units 6 and 11 do.

### 10. Review units on the short path (minor)

LAYER frame. REPEAT new. Confidence judgment call.

- For the lead 4. The frame's 3 short days put a hook, the readiness check and two reteaches in one 45-minute day
  (161+162+163), which cannot hold. Recommendation: allow 4 short days for units 6 and 11 (161+162, 163+164, 165,
  166, so the check and the respond day each stand alone) and take the day from the next unit by folding its hook into
  its first study day (unit 7: 167+168+169; unit 12: 327+328+329), dropping each from 16 to 15 short days. This edits
  the frame's short counts, so it is the lead's call.

### 11. The 10-days-short year is sound; one tight day (minor)

LAYER sequence. REPEAT new. Confidence firm.

- All 40 fold-in days are unassessed drills and none cuts an owned part. Folding a drill into a sitting day (days
  114 into 115, 274 into 275, 434 into 435) fills 45 of 45 minutes. If finding 8's fix is applied, those three drills
  fold into the written days instead and the sittings keep their slack; no other change.

### 12. The unit 5 Candidate is dropped on a reason the frame contradicts (minor)

LAYER sequence. REPEAT new. Confidence firm.

- The .md drops the community-space family showing because "the frame keeps both showings on school grounds", but
  the Candidate itself says "where the school allows it, with every yes", and unit 18 already allows "a community
  space the school allows". The day cost is 0 either way. The question of naming community spaces for Level 1 goes
  to Cory (below); until then the default stays the school's space, as written.

### 13. Small text faults (minor)

LAYER sequence. REPEAT yes (stale or copied lines, as music 6 to 8 finding 11). Confidence firm.

- Day 297 and day 457: "changes from the audience-moment test", copied from unit 5; the test before them is the
  theme test (296) and the cohesion test (456).
- Days 217 and 377: "tied to the aesthetic standards or the risk", Level 1 unit 3 wording; Level 2 ties to the
  student's aesthetic and limits, Level 3 to the framework and the framed question.
- Day 375: "finish the storyboard for the piece"; unit 13's piece starts from the rule and framework, so "finish the
  production plan".
- .md unit 2 Candidate line: "the unseen clip on the end sitting (day 41's neighbor, the "sit" day)" should read "the
  unseen clip on the end sitting, day 40".
- Several "Why here" lines end without a period (units 1, 2, 3, 4, 6, 7, 8 and on).

## What is right and should not be touched

- The level claims: Level 1 the 18 Proficient ids, Level 2 the 18 Accomplished, Level 3 the 18 Advanced, Level 4 the
  eleven re-assessed ids, each level stated once in the .md and in its heading (bar's "Scope and sequence states";
  STANDARD.md 3.2). My script found no id in the wrong level and none missing.
- Retrieval on day 2 of every unit from the level before (one year back) and the bridge's readiness check on day 1;
  the table in the .md matches the days.
- Every made piece meets a critique and a logged revision before it is scored; every unit shows; each production unit
  has a mid-unit checkpoint on the planning portfolio before the team commits.
- Course-level checks on weeks 16 and 32 of every level (CALENDAR.md rule 4), each drawing its brief from an earlier
  unit's content, said so in the .md; the "not sampled" table with a reason for every id.
- Works: France, the United States, Chemehuevi, Brazil, Canada, South Africa, Argentina, Senegal, Burkina Faso, Soviet
  Russia, Chile, China, Gullah Geechee, Kanien'kehá:ka, Ho-Chunk and Pechanga, Aotearoa, Hungary, Mexico, Iran,
  Nunavut, from 1902 to 2021, with sensitivity flags carried into the notes; Level 4's source-selection checklist.
- The free path and the paper form of every piece; hazards and controls in the making-day notes; no new supply.
- The logic model on one page, with its plain statement that nothing has been tried with students.

## What I could not judge

- Whether 30 individual 2- to 3-minute pieces can be scored after the session in a teacher's week (finding 1's
  fix moves time outside class); a media arts teacher's view would settle it.
- Each work's dates, holders and living status (frame item 6; the unit plans check them).
- Whether the defended talk's 4 minutes a student with questions fits 8 students in 45 minutes in practice (it does on
  paper, 32 minutes plus change-overs).

## Sources

- None opened this run. Rests on the repo's standard lines (data/standards/ncas-performance-standards-words.txt), the
  frame, STANDARD.md, the bar and the lens, and on memory for general media arts practice (screening and critique
  routines). Confidence marks above reflect that.

## Lens checklist (scope and sequence layer)

| Lens line | Status |
|---|---|
| A grade's ids in the wrong year, or a high school level tied to a grade | Met |
| A year with one artistic process missing | Met per level; unit 17 padded (finding 7) |
| Works all from one tradition or one century | Met |
| Technique that does not get harder across units or years | Met (named methods, strategic methods, design principles, proposal; emphasis, continuity, hybridization, series) |
| A plan that needs a daily period in K to 8 | Not applicable (9 to 12 levels meet daily by design, STANDARD.md 3.2) |
| No showing in a unit | Met |

Bar items 1 to 9: 1 met (finding 7 for unit 17); 2 met except findings 4 and 5; 3 met; 4 met; 5 met; 6 met except
finding 6; 7 met; 8 met (guides, self-check days, portfolio each unit); 9 not met on the showing days (finding 1),
otherwise met. "Fails if": no line fails outright; finding 4 is the "no technique taught" line on two prototype days.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Units 4, 9, 14 showing days: small-group screening circles, look-fors scored from the kept piece after the session | 30 individual pieces cannot screen in one period | days.csv 112, 272, 432 |
| Unit 18 showing as a window, scored from the kept piece and audience cards | same | days.csv 594 |
| Unit 19 showing as an exhibition, look-fors from the set-up and kept series, across 630 and 631 if needed; 631's reading moves into 632 | same | days.csv 630 to 632 |
| Unit 15 piece made by each student, per the frame; "teams" to "pairs of students"; exhibition note on 470 | frame says made by the student | days.csv 445, 446, 456, 470 |
| Codes added or moved: Pr6.1.Ia to 150 (off 154), Pr6.1.IIa to 310, Pr6.1.IIIa to 470, Cr3.1.IIb to 256, Cr3.1.IIIb to 416 | goal names a scored id the codes omit | days.csv |
| Re7.1.IIb items: experience, intent, persuasion prompts | standard's three parts | days.csv 196 (317 keeps two) |
| Re8.1.II end sitting: one prompt per setting, four | standard names four settings | days.csv 275 |
| Pr5.1.IIIc look-for names an innovative tool or method | standard's part dropped | days.csv 395 |
| Cr3.1.Ib log entries name the goal or taste | standard's part dropped | days.csv 91, 98, 105 |
| Unit 3 prototype one uses erase-and-redraw only; other techniques open on prototype two | technique before making | days.csv 50, 55 |
| Unit 8 prototype-one day moved after day 208 | branching taught first | days.csv 203 to 208 |
| Unit 18 day 570 becomes a technique day | technique before making | days.csv 570 to 588 |
| Days 65, 222, 382 run the critique card team to team | second critique stage needs a protocol | days.csv |
| Unit 17 day 549 adds a 30-second evidence reel shown in the talks; .md process line corrected (lead may reverse) | honest four-process line | days.csv 549, 552 to 555; .md unit 17 |
| Short path: fold 114, 274, 434 into the written days; split the five-day merges; respond days paired with one day | merged days that cannot hold | .md Short path lines, days.csv notes |
| Day 481 note: placement into Level 4 against Level 3's year-end check | STANDARD.md 3.2 | days.csv 481 |
| Text fixes in finding 13 | copied or garbled lines | days.csv 217, 297, 375, 377, 457; .md |

## For the lead (process, not Cory)

- Finding 9: widen `sequence.py`'s first-day readiness exception to each level's first day in a 9 to 12 levels
  course, then set `assess` on 161 and 321. Applies to the other arts 9 to 12 courses too.
- Finding 10: the review units' short count (3 or 4).
- The scope's For the lead 2 (unit 5's three end days) and 5 (day 637 read with 638 as one evidence set): both
  sound; keep.

## For Cory

- Unit 5 (Level 1): may the family showing be held in a community partner's space where the school allows it, with
  every yes? Level 4's unit 18 already allows a community space the school allows, so this would extend the same
  rule to Level 1. Default if no answer: the school's own space.
- The supplies ceiling ($90, $80, $80, $60 a class a level, all optional beside a free path) stands from the frame;
  nothing in this scope adds to it.

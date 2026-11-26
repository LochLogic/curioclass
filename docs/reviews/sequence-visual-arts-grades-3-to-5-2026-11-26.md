# Expert read: scope and sequence of Visual Arts, grades 3 to 5 (2026-11-26)

Course `visual-arts-grades-3-to-5`. A cold read by the curriculum expert (PRODUCTION-PATH step 3), done as
docs/pipeline/briefs/sequence-read.md says, with build/scope-writes/ARTS-READ.md and ARTS-BRIEF.md. I did not write
the scope; this file is the only file I changed.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/arts.md, docs/ADOPTION-BAR-SUBJECTS.md section "2. Arts" (items 1 to 9
  and "Fails if"), build/scope-writes/ARTS-BRIEF.md, docs/pipeline/briefs/sequence-write.md rules 2 to 7.
- docs/courses/visual-arts-grades-3-to-5/scope-and-sequence.md and data/plans/visual-arts-grades-3-to-5/days.csv
  (all 192 rows), read cold.
- Beside them: the frame (docs/courses/visual-arts-grades-3-to-5/frame.md, all of it), the 24 va-g3 to va-g5 rows
  of data/progressions/arts.csv, the course's rows in docs/courses/CALENDAR.md and data/plans/calendar.csv, the ELA
  grade 3 and math grade 4 rows of calendar.csv for the two leans, the visual arts lines of
  data/standards/ncas-performance-standards-words.txt, and the earlier arts sequence reads of the same day
  (visual arts K to 2, media arts 3 to 5, music 3 to 5), so repeats are tagged.
- Gates: `scripts/plan.py check` (0 failures for this course), `scripts/sequence.py check visual-arts-grades-3-to-5`
  (0 failures), `scripts/frame.py calendar` (0 failures; unit days 60 a year; checks on weeks 18 and 26, 17 and 25,
  18 and 26), `scripts/stale.py check` (nothing for this course). I also ran three short scripts over days.csv:
  every code sits in its own year (45 ids, none misplaced); `school_day` matches the .md's formula on all 192 rows;
  and every once-a-week session group was expanded to its days (finding 1 and finding 7 come from that).
- No outside source was opened for this read. Standards wording rests on our own-words file; the room and minute
  judgments rest on APPROACH.md and on memory of elementary art specials, marked so.

## Verdict

Sound: the band-year rule holds id by id, every unit has a critique, a revision and a showing before its
end-of-unit assessment, technique is taught in steps before the making in ten of twelve units, the works range
across continents, centuries and living makers each year with their sensitivity lines carried on the days, and the
checks sit on CALENDAR.md's weeks. The biggest risk is the once-a-week path: in every unit it puts the showing and
the end-of-unit check in one 40-minute session, and in units 3, 8, 11 and 12 two or three check-length days in one
session, so assessed items cannot all be given. The one change that matters most is to hold the showing outside
art time on that path and give the check session to the check (finding 1, settled below); next is the year-end
checks, which repeat the unit's own item forms a week later while the .md says they do not (finding 2).

## Findings, most serious first

### 1. On the once-a-week path the end sessions cannot hold what they list

LAYER sequence (the frame's "the showing (the check)" does not say how two end days fold). REPEAT yes (visual arts
K to 2 finding 4; media arts 3 to 5 finding 2). Confidence: likely (arithmetic on the check-day budget; room
judgment from memory).

- **What is wrong.** Expanding each unit's session list:

  | Unit | Session | Days merged | What it must hold in 40 minutes |
  |---|---|---|---|
  | 2, 5, 6, 7, 9, 10 | last before respond | showing + check (32-33, 78-79, 94-95, 110-111, 142-143, 160-161) | a showing to a partner class or the school, and a 37 to 39-minute check day |
  | 3, 11 | 12-13 | two check days (48-49, 176-177) | two self-checks, two written sittings of 15, two tables of 12: about 78 minutes |
  | 4 | 10-11 | family show + check (62-63) | a family show and a 39-minute check |
  | 8 | 11-13 | showing + two check days (125-127) | a family showing, three written items, two self-checks |
  | 12 | 9-11 | revision + hanging + family show + check (189-191) | the last making day, the curated show and three written items |
  | 1, 9 | 14-16, 12-13 | both making-day observation days (14-15, 140-141) | the whole rotating list for VA:Cr2.2.3a or VA:Cr2.2.5a in one session |

  Unit 2's list also reads wrong: "8-9-11 / 10-12" expands, as every other range in the file does, to days 26, 27,
  29 and then 28, 29, 30, so day 29 appears twice.
- **Why it matters.** The brief and ARTS-READ ask that the once-a-week path hold with no assessed part cut. A
  teacher following these sessions drops written items or observations on the day, and one adult cannot host
  families and run a teacher's table at once.
- **The fix (settled below).** Under the Shorter path's once-a-week bullet, add: "On this path a unit's showing is
  hung at the end of its revision session and visited outside art time (a partner class walk-by, a drop-in at
  arrival or pick-up, a family evening); its look-fors are scored from the kept work as on the full path. The end
  session is the check. Where a unit has two check days, the self-check moves to the last five minutes of the
  revision session and the session holds one written sitting of all the unit's items (about 25 minutes) and the
  teacher's table (about 8)." Then change the session lists:
  - Unit 1: 1-2 / 3-5 / 6-8 / 9-11 / 12 / 13 / 14-16 / 17 / 18, with the note "observations for VA:Cr2.2.3a run on
    sessions 12 and 13 (the two making sessions) and 14-16 for any child not yet seen".
  - Unit 2: write "8, 9, 11 / 10, 12", not hyphens.
  - Unit 4: 1-4 / 5-6 / 7-9 / 11 (show 62 held outside art time) / 12.
  - Unit 8: 1-2 / 3-5 / 6-8 / 9-10 (show 125 hung at its end) / 12-13 / 14.
  - Unit 9: as now, with the note "observations for VA:Cr2.2.5a run on sessions 10-11 and 12-13".
  - Unit 12: 1-3 / 4-6 / 7-9 (show 190 hung at its end and held outside art time) / 11 / 12.
  - Units 2, 3, 5, 6, 7, 10, 11: the session counts stay; the showing in the merged session is held outside art time.
  Every count stays the frame's (9, 8, 6, 5; 8, 8, 6, 6; 8, 9, 6, 5), so the check weeks do not move.

### 2. The year-end checks repeat the unit's item forms a week later, and the .md says they do not

LAYER sequence (and the frame's year-end cells). REPEAT new. Confidence: firm (days.csv against sequence-write
rule 2, "a course-level check never repeats a task form given in the last two weeks").

- **What is wrong.** The scope rightly moved the year-end Re8 and Re9 items onto earlier units' works (rule 3), but
  kept their form. Day 48 asks how an unseen work's media build subject, form and mood; day 51, three sessions
  later, asks the same of Catlett's print. Day 49 judges a work with a new three-line checklist; day 51 judges
  Rousseau with a new three-line checklist. Days 111 and 113 both use one checklist on two works; days 176 to 177
  and 179 ask the same Re8 prompt and the same "how the judging standards differ" prompt. The .md's line "No check
  repeats a task form given in the two weeks before it" and the day notes' "a different task form" are not true.
  Day 179 also asks how the standards for judging Rivera and Hazoumè differ, but neither work's setting card in
  units 9 and 10 carries judging standards.
- **Why it matters.** A child answers the same prompt twice in eight school days, so the check samples recall of
  the last item rather than the skill on new ground, and a writer reading the .md will believe the rule is met.
- **The fix (settled below; item wording inside the standards).**
  - Day 51 (year 3): Re8.1.3a as a comparison: "Which of two unit 1 works, Catlett's Sharecropper or Bearden's The
    Block, uses its media to make the quieter mood? Name the media and one feature of form in each." Re9.1.3a: the
    child applies the given three-line checklist to a Curio Class sample student work and marks the line it does
    not yet meet, with a reason.
  - Day 113 (year 4): Re8.1.4a stays (how a new background fact changes El-Salahi's meaning is a new form).
    Re9.1.4a: a Curio Class student's filled-in checklist for the van Gogh is given; the child applies the same
    checklist to a Chicano Park mural and says whether the given marks were fair, with a reason.
  - Day 179 (year 5): Re8.1.5a as a comparison of two earlier works (the Yangliuqing print and The Flower Carrier):
    which visual elements carry the stronger mood in each. Re9.1.5a: a short Curio Class card judges Hazoumè's
    mask by one standard from another time or culture (for example, a smooth carved finish); the child says why that
    standard fits or misfires for this work, naming its style, media and setting. The card is written for the day.
  - The .md's "Drawn from earlier units" bullet: replace "No check repeats a task form given in the two weeks
    before it" with "Each year-end Re8 and Re9 item uses an earlier unit's work in a form the unit did not use: a
    comparison, a given checklist checked for fairness, or a standard tested against a work." Change the matching
    note text on days 51, 113 and 179.
- **For the lead.** The frame's year-end cells (For the lead item 1 in the scope) should take these forms when the
  frame is fixed.

### 3. Rows taught earlier the same year are leaned on with no retrieval, and unit 8's piece has no technique

LAYER sequence. REPEAT yes (visual arts K to 2 finding 8; media arts 3 to 5 finding 5). Confidence: firm (the
frame's own "Why this unit, here" cells name each lean).

- **What is wrong.** The Readiness line names only each unit's `assumes` row (one grade back), which is right. But
  the frame says unit 2's depth "uses the clue-reading" (va-g3-look, unit 1), unit 3's checklist "needs unit 1's
  clue-reading", unit 6's panel "uses the year's tested and invented marks and the tool care" (va-g4-craft, unit
  5), unit 7's judging "uses the critique protocol" (va-g4-revise, unit 6), unit 10's sculpture "uses the logged
  techniques and craft care" (va-g5-craft, unit 9) and unit 11's labels "use the statement's art words"
  (va-g5-revise, unit 10). None of the days that use them opens with a retrieval. Unit 8 is the sharpest: day 122's
  tradition piece ("paper, crayons or paint") follows a planning day, with no step card and no technique named,
  the lens's "making task with no technique taught first".
- **Why it matters.** Sequence-write rule 2 asks for a retrieval task inside a day for a row used earlier the same
  year; for unit 8, the made piece (VA:Cn10.1.4a) is scored with no technique taught or recalled.
- **The fix (settled below).** A five-minute retrieval warm-up in the opener, named in the note and in
  `retrieves`: day 21 va-g3-look; day 43 va-g3-look; day 90 va-g4-craft; day 103 va-g4-revise; day 122 va-g4-craft
  with unit 5's mark step card or unit 6's color-plan step card in hand, the child choosing which the piece uses;
  day 150 va-g5-craft; day 171 va-g5-revise. Add a "Same-year retrieval" line to the .md's Readiness and retrieval
  bullet listing these seven. No readiness check is needed (every `assumes` cell is one grade back) and no unit's
  first day changes.

### 4. Units 4 and 12 create only by calling mounting "create"

LAYER sequence. REPEAT new (the music 3 to 5 read found processes held only in a note; this is the same family).
Confidence: likely.

- **What is wrong.** The .md lists "Create 58 (mounts)" for unit 4 and "Create 186 to 189 (mounts, labels)" for
  unit 12. Mounting and preparing work for display is the presenting standard (VA:Pr5.1), not creating. Both
  units show kept work from earlier units and make nothing new.
- **Why it matters.** ARTS-READ and the brief ask for all four processes in every unit's days; the bar holds for the
  course, but these two units hold it only by a label.
- **The fix (settled below).** Day 58: before mounting, the child adds one finishing detail to the chosen work and
  says in a line why (creating, VA:Cr3.1.3a as practice, unscored). Day 188: before the work is mounted, each child
  makes one finishing change to their piece, named in its label (creating, practice). Change the two Processes
  lines to "Create 58 (a finishing detail before mounting)" and "Create 188 (a finishing change before mounting)".

### 5. Unit 6's respond day cannot redo a joined, hung panel, and its baseline is the scored sketch

LAYER sequence. REPEAT new. Confidence: likely.

- **What is wrong.** By day 96 the sections are joined (93) and hung in the entrance hall (94), so a child marked
  "not yet" on VA:Cr3.1.4a ("the planned change") cannot make it on the panel. Separately, day 85 is both the
  baseline look ("on these sketches") and the artifact scored for VA:Cr1.1.4a, so the unit's two marks are one mark.
- **Why it matters.** A respond day that cannot act on the "not yet" is no second try; a baseline on the scored
  artifact shows no growth (APPROACH "Growth").
- **The fix (settled below).** Day 96's goal: "for the planned change, the child makes it on a photocopy of their
  section, or paints a small square to paste onto the panel". Day 84 opens with a two-minute baseline task before
  the brainstorm is taught ("sketch as many ways to welcome a new student as you can"); day 85's note drops "baseline
  look ... on these sketches".

### 6. The shorter-session line keeps a 39-minute check day "whole" in a 30 to 35-minute session

LAYER sequence. REPEAT yes (visual arts K to 2 finding 11). Confidence: firm (arithmetic).

- **What is wrong.** "Shorter sessions (30 to 35 minutes, same days) ... Check days stay whole." A check day is 39
  minutes by the frame's budget.
- **The fix (settled below).** Replace with: "On check days the self-check moves to the last five minutes of the
  session before; the check runs set-up 2, written sitting 15 (every prompt read aloud once), teacher's table 10,
  clean-up 2: 29 minutes, with no mounting task for early finishers beyond labeling."

### 7. Text a writer would copy wrong

LAYER sequence. REPEAT yes (note text, media arts 3 to 5 finding 8; fold days and baselines, media arts 3 to 5
finding 9). Confidence: firm.

- **Year 4 school days in the checks table.** The .md gives (247, 249) and (287, 289); days.csv and the .md's own
  formula give 242, 244 and 282, 284. Fix the table.
- **"Respond" for the artistic process.** Each unit's Processes line says "respond 1 to 3, 6 ..." beside an Order
  line where "respond (18)" means the respond day. The lens names this mix-up. Write "responding" in every
  Processes line.
- **Day 131.** The frame lists the Yangliuqing print makers among the communities the sensitivity agent reads
  first; the day's note has no such line. Add: "sensitivity flag: the agent reads the holding museum's page and a
  source on the Yangliuqing print makers first."
- **Day 165.** The hook calls the Iznik pattern "built on symmetry" two days before the symmetry retrieval (167).
  Day 165's goal says "a pattern of repeated parts"; the word symmetry waits for day 167.
- **Unit 8 load.** VA:Pr6.1.4a (museum, gallery and community center compared) has one teaching day (119) and is
  scored on day 126 with no practice. Day 125's note adds: "visitors and children say which venue's aim the class
  show is closest to and what a visitor gets from it" (practice of VA:Pr6.1.4a).
- **Fold days and the baseline.** Days 5, 8, 10, 23, 44, 68, 102, 133 and 185 are practice days of the baseline look;
  folding them can leave a rotating group unobserved. Add to the 10-days-short bullet: "Where a fold day is a
  baseline practice day, its rotating group is observed in the next day's opener."

### 8. `school_day` and data/plans/calendar.csv count the same weeks a day apart

LAYER process. REPEAT yes (media arts 3 to 5 finding 11). Confidence: firm.

- days.csv puts course day 1 on school day 2 and day 35 on 87, counting years 4 and 5 from 161 and 321;
  calendar.csv (from the frame) puts day 1 on school day 3 and day 35 on 88, counting each grade from 1. The visual
  arts K to 2 scope uses 160 x y + ceil(5n / 2), which matches calendar.csv. Every check lands in the same week
  either way. For the lead: set one count for every arts band course so a later gate comparing the two files does
  not fail.

## The rest of the brief's checks

- **Order inside units:** holds; each technique day precedes its making (stamps 4 before 12, collage 7, modeling 9,
  overlap 22, partner talk 28 before the critique 30, tool check 70 before pointed scissors 71, critique protocol 89
  before 91, washes, mixing and scratch-through before 138, joining and sewing before 153, statement frame 154 before
  155). Unit 8 is the exception (finding 3).
- **Assessments, parts:** every lettered id is asked in full on its item or look-for (checked against the
  own-words lines, for example VA:Pr5.1.4a's three paired cases, VA:Re9.1.5a's style, media, time and culture,
  VA:Pr4.1.3a's online space). No unit is over 25 days. Respond time is counted once.
- **Readiness:** none is needed and none is placed; every `assumes` cell is one grade back, and day 1 of every unit
  is clean. The math lean (4.G.A.3, math grade 4 unit 9, weeks 26 to 30 of grade 4) is one grade back for year 5
  and opens as a retrieval with its reteach, as rule 2 says for math leans.
- **Checks that do not repeat:** drawn from earlier units and said so (finding 2 is about form, not content).
- **Standards in full:** all 45 ids on teaching days and on an end-of-unit row of their own year.
- **Days by load:** follows the rows; unit 8's VA:Pr6.1.4a is light (finding 7). Days 47 and 175 (revision and
  showing in one session) and day 91 (painting plus a 15-minute critique) are tight but workable; the unit plans
  test the minutes.
- **Calendar:** all six checks on CALENDAR.md's weeks; arts are specials in K to 5. The ELA lean (SL.3.1) is taught
  in ELA grade 3 unit 1, weeks 1 to 8 in calendar.csv, before unit 2 (weeks 10 to 17); no bridge is needed, and the
  card's rules are shown anyway.
- **Candidate cells:** all twelve settled, kept ones inside a day at no cost, dropped ones with a reason.
- **Shorter path:** present for the once-a-week path, the shorter session and the 10-days-short year (four fold
  days a year, 160 minutes, no assessed day folded). Findings 1 and 6 fix what does not hold.
- **Each year names its grade's standards:** yes, on the first page and in each year's heading; the mixed-class
  line is there once.
- **Logic model:** on the first page, as the frame asks.

## The lens checklist (scope and sequence layer, plus what shows at this layer of the others)

| Line | Result |
|---|---|
| A grade's ids in the wrong year | Met (script: none) |
| A year with one process missing | Met for every year; units 4 and 12 by a label only (finding 4) |
| Works from one tradition or century | Met: each year has Africa, Asia, Europe, the Americas, a Native maker and living makers |
| Technique that does not get harder | Met: the frame's ladder is kept |
| A plan that needs a daily period | Met: two sessions a week, a once-a-week path |
| No showing in a unit | Met: twelve showings |
| Making with no technique taught first | Missed in unit 8 (finding 3) |
| A work with no setting | Met: setting cards on every work |
| Critique with no protocol, no revision | Met: describe, ask, suggest, then the set-step protocol from unit 6; revision in every unit |
| End-of-unit assessment as a vocabulary quiz | Met: making, showing and response items |
| Copying the coalition's questions or tasks | Met: our own questions |
| Set-up and clean-up fit | Met on the full path; missed on the once-a-week end sessions (finding 1) |
| Equipment with a low-cost option | Met: a free path in every unit |
| Unsafe use of space | Met: blades by adults, walks on school grounds, the roll on tables |
| A child who must perform alone | Met: showings are class or group |
| "Respond" for the artistic process | Missed in the .md's Processes lines (finding 7) |
| A tool asked to judge a finished work | Met: none |
| Disciplines planned as one; math or PE double-taught | Met: symmetry retrieved, no measuring or scale |

## What is right and should not be touched

- The band-year rule, stated once with the mixed-grade line; each year claims its 15 ids and nothing else.
- The studio routine: monitors from day 1, dry check days, clean-up minutes and the free path on every hands-on day.
- The unit arc in all twelve units: works with setting, technique in steps, a drill, making, one critique on the
  second making day, revision, showing, check, respond; portfolio piece with a reflection each unit.
- The observation design for the handling ids (rotating list on the last two making days, never on a check day)
  and the tool-check gate before pointed scissors.
- Every flagged work carries its sensitivity line on its day (but for day 131), with the hard-history choices
  (panels without violence, Bayeux without the battle, Hine without injury, the Yellowstone sentence) kept.
- The course-level checks' move onto earlier units' content, and the L107 list of codes not sampled, with reasons.

## What I could not judge

- Whether 30 children can each pass the pointed-scissors gate inside day 71's ink session; a trial would tell. If
  not, the gate can run across days 71 and 75, still before any pointed tool is used.
- Rights lines of the works the frame leaves to the unit plans (frame For the lead item 4).
- Whether Rousseau's The Repast of the Lion (a lion with its prey) suits every grade 3 room; the sensitivity agent
  reads it with the unit.

## Sources

- docs/courses/arts/APPROACH.md and STANDARD.md 3.4: kinds of day, growth, the 32-session path.
- data/standards/ncas-performance-standards-words.txt: the parts of each id.
- docs/ADOPTION-BAR-SUBJECTS.md section 2: items 1 to 9 and "Fails if".
- docs/pipeline/briefs/sequence-write.md rules 2 and 3: retrieval, the two-week task-form rule, checks after a unit.
- data/plans/calendar.csv: the ELA grade 3 and math grade 4 timing for the two leans.
- From memory: elementary art specials rooms and family showings (findings 1 and 5), check-day timing (finding 6).

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Once-a-week: showing hung at the end of the revision session and visited outside art time; end session is the check; two-check units take one combined sitting with the self-check the session before | One session cannot hold a showing and a check, or two checks | .md Shorter path; unit 1, 2, 4, 8, 9, 12 session lists |
| Once-a-week session lists: unit 2 "8, 9, 11 / 10, 12"; unit 4 1-4 / 5-6 / 7-9 / 11 / 12; unit 8 1-2 / 3-5 / 6-8 / 9-10 / 12-13 / 14; unit 12 1-3 / 4-6 / 7-9 / 11 / 12; units 1 and 9 observation notes | Counts kept; observations get two sessions | .md unit sections |
| Year-end items: day 51 Re8 comparison and Re9 on a sample student work; day 113 Re9 fairness of a given checklist; day 179 Re8 comparison and Re9 a standard tested against Hazoumè's mask | Two-week task-form rule | days.csv days 51, 113, 179; .md checks table and "Drawn from earlier units" |
| Five-minute retrieval openers: day 21 and 43 va-g3-look; day 90 and 122 va-g4-craft (122 with a step card); day 103 va-g4-revise; day 150 va-g5-craft; day 171 va-g5-revise | Same-year rows the frame names; unit 8 technique | days.csv notes and `retrieves`; .md Readiness line |
| Day 58 and day 188: a finishing detail or change before mounting, as creating practice | A real create in units 4 and 12 | days.csv days 58, 188; .md Processes lines |
| Day 96 respond on a photocopy or a pasted square; day 84 two-minute baseline before the brainstorm; day 85 note drops its baseline | Respond that can act; two marks a unit | days.csv days 84, 85, 96 |
| Shorter session check days: self-check the session before; 2, 15, 10, 2 minutes | A 39-minute day does not fit 30 to 35 | .md Shorter path |
| Year 4 school days 242, 244, 282, 284 in the checks table | Match days.csv and the formula | .md checks table |
| "responding" for the artistic process in every Processes line | Lens: "respond" is the respond day | .md unit sections |
| Day 131 sensitivity agent line; day 165 "a pattern of repeated parts"; day 125 venue practice; fold-day baseline sentence | Frame flag; symmetry after retrieval; Pr6.1.4a practice; baseline kept | days.csv days 125, 131, 165; .md Shorter path |

## For the lead

- The frame's year-end check cells take finding 2's forms when the frame is next fixed (the scope's own For the
  lead item 1 names the cells).
- One `school_day` count for all arts band courses (finding 8).
- The scope's For the lead items 3 (stale winter-count link, the Hine link to music) and 4 stand; I agree with both.

## For Cory

- Nothing new. The supplies ceiling carried from the frame stands: $60, $50 and $50 a class of 30 for years 3, 4
  and 5, with the pick of $75 a class a year and every free path kept (frame For the lead item 3), still unanswered.

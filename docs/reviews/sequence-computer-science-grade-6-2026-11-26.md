# Expert read: scope and sequence of computer-science-grade-6 (2026-11-26)

Job: docs/pipeline/briefs/sequence-read.md through build/scope-writes/CS-READ.md, {subject} = computer science.
Read cold; this reader did not write the scope.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/computer-science.md, build/scope-writes/CS-BRIEF.md.
- docs/courses/computer-science-grade-6/scope-and-sequence.md and data/plans/computer-science-grade-6/days.csv (64 rows).
- docs/courses/computer-science-grade-6/frame.md in full, the g6 rows of data/progressions/computer-science.csv, the
  17 owned statements in data/standards/csta-2026-statements.txt, docs/courses/CALENDAR.md (stagger rule 3).
- Earlier reads for repeat tags: docs/reviews/frame-computer-science-grades-6-to-12-2026-11-25.md,
  frame-computer-science-grades-1-to-12-fixes-2026-11-26.md, sequence-visual-arts-grades-6-to-8-2026-11-26.md. No
  earlier computer science scope and sequence read exists, so REPEAT compares with other subjects' sequence reads.
- Gates: `sequence.py check computer-science-grade-6` 0 failures; `frame.py check` and `frame.py calendar` show no
  break for this course; `stale.py check` names nothing in this course. School days recomputed by hand from the
  stated formula (days 1 to 38: ceil(89n/38); days 39 to 64: 89 + ceil(71(n - 38)/26)); every row matches, and the
  checks sit on 87, 89 and 92 (weeks 18 and 19) and 155, 158 and 160 (weeks 31 and 32), as the frame pins.
- Outside sources: NASA's Dorothy Vaughan biography (nasa.gov/people/dorothy-vaughan, opened 2026-11-26). The ssa.gov
  history pages returned 403 (browser check, below). The IMLS survey page returned 404; what is said of it here is from
  memory.

## Verdict

The scope is sound and close to ready: every owned id sits on taught days in the frame's units, trace comes before
modify before make on every programming row, every device day names a paper path, and the calendar math is right. The
biggest risk is that two unit 3 ids are named more fully than they are taught: MS-DAT-DC-21's accuracy part is never
asked, and DC-21 and DC-22 are each met only on first-teach days before they are scored five weeks later. The one change
that matters most is finding 1 (accuracy on day 27, an applied DC-21 and DC-22 task on day 33, and the day 37 item
asking for accuracy); the rest are small fixes a busy writer could otherwise build wrong.

12 findings.

## Findings, most serious first

### 1. MS-DAT-DC-21's accuracy part is not carried, and DC-21 and DC-22 are never applied before they are scored

What is wrong. MS-DAT-DC-21 asks how precision and granularity affect accuracy, storage and analysis. Day 27 teaches
"what each log can answer, what it costs to store, and when more matters" (analysis and storage), and the day 37 item
asks "which of two recordings answers a question and what it costs to store". Accuracy is named nowhere. DC-21 also sits
on one Understanding day only (27) and DC-22 on two (28, 29); neither appears on an Application day, and both are first
scored on day 37 (school day 87), five weeks and nine sessions after day 27. Every other owned id in the course gets at
least one modify or make day before it is scored.

Why it matters. A lettered part is named and not taught (the brief's "Standards in full"), and an "evaluate" id is
scored after one first-teach day, against the frame's own rule that no score rests on a first teaching.

Fix. Day 27 goal adds accuracy: the whole-degree log rounds a 20.4 reading to 20, and the once-a-day log misses the
afternoon high, so the day's high it reports is wrong. Day 33 (pairs answer three questions of the table) adds a
fourth question the table's granularity or missing header cannot answer; pairs say which recording or which metadata
would answer it and at what storage cost; add MS-DAT-DC-21 and MS-DAT-DC-22 to day 33's codes. The day 37 DC-21 item
asks for one effect on accuracy beside the storage cost and the question answered.

LAYER sequence. REPEAT yes (a part named and not carried is the most common sequence-read finding; visual arts 6 to 8
reads carry the same kind). Confidence: firm (the statement's own three words; the codes column).

### 2. The shorter path cuts the device part of MS-DAT-DC-22

What is wrong. The fold "Day 29 (photo properties) folds into day 28 with the printed panel" turns the only device
session for the viewing part of DC-22 into the paper path for every school on the short year, so that part becomes
"part met without a device" even where devices exist. The section says no owned part is cut.

Why it matters. The short path must keep every owned part; this one silently downgrades an id the full year meets.

Fix. Reword the fold: "Day 29 folds into day 28's last 10 minutes: pairs open the supplied photo's properties on a
device (the printed panel only where there is none)." The count of ten fold-in days and the 54-day total stay.

LAYER sequence. REPEAT yes (shorter paths that cut a part are a repeated kind across the 2026-11-26 sequence reads).
Confidence: firm.

### 3. MS-PRO-PD-12's "for clarity and reusability" is taught but never asked on an assessment

What is wrong. Day 7 (a bad name against a good one) and day 9 (two lines on how a procedure helps) teach the why. The
assessment items are only "rewrite a repeated block as a procedure" (day 14), "a repeated block rewritten as a
procedure" (day 38) and "a procedure rewrite" (day 63). None asks the student to name the procedure well or say what
the rewrite gains.

Why it matters. The id's purpose clause (clarity and reusability) is the difference from plain refactoring; a rewrite
alone can be done by copying the pattern.

Fix. Each of the three items adds one prompt: "Name your procedure and say one way the new version is clearer or
easier to reuse (one place to change it, fewer repeated lines)." Days 14, 38 and 63 notes.

LAYER sequence. REPEAT new. Confidence: likely.

### 4. MS-SYS-HW-30 names three kinds of impact; the days and the check ask for one

What is wrong. The statement asks for differences by user needs, system requirements and "societal, environmental, and
ethical impacts". Days 54 and 55 ask for "one societal, environmental or ethical impact" and day 62 for "one impact".
A student can meet every task naming only cost.

Why it matters. Two of the three impact kinds can go untaught in practice; the frame already supplies one example of
each (the cost gap between homes, energy use and discarded devices, privacy on a shared kiosk).

Fix. Day 54 goal: compare the two systems with one impact of each kind, using the frame's three examples. Day 55 and the
day 62 item: name impacts of two different kinds and say which kind each is. Judgment call on two rather than three
in the timed item.

LAYER sequence. REPEAT yes (a list in a statement reduced to "one of"). Confidence: judgment call.

### 5. Days 36 and 61 carry `assess` = `end` on teaching days; the gate no longer needs it

What is wrong. The writer tagged the last teaching days of units 3 and 6 as end-of-unit assessments only to pass
sequence.py, and the notes and For the lead 1 explain the workaround. The lead fixed sequence.py on 2026-11-26 (line
328: a course-level check on the day right after a unit's last day stands for its end-of-unit assessment).

Why it matters. A teaching day tagged `end` will be read by the unit-plan writer and by any count of assessments as a
scored day; the notes already say it is not scored.

Fix. Clear `assess` on days 36 and 61; drop "(the end tag here holds the gate's slot, For the lead 1)" from both notes,
keeping "the unit's end-of-unit assessment is lesson one of the course-level check (day 37 / day 62)"; in the .md,
change the two "Day 36 carries ..." and "Day 61 carries ..." sentences to say the check stands for the assessment, and
delete For the lead 1. Re-run `sequence.py check`.

LAYER process. REPEAT yes (the same workaround in music 3 to 5, as the scope says). Confidence: firm.

### 6. Leaving unit 4 out breaks the year-end check's lesson two, and the scope does not say what happens

What is wrong. The scope and frame let a school leave unit 4 out (MS-ALG-ML-06 and MS-ALG-IM-09 then not claimed). Day
63 samples both ids in two of its five items, and the scope does not say what replaces them or what days 40 to 46
become.

Why it matters. A teacher who takes the leave-out has a year-end check with items on a unit never taught.

Fix. Add one bullet under Unit 4 and one sentence on day 63's note: "If unit 4 is left out, day 63's two unit 4 items
become a ten-line trace (MS-PRO-VD-16) and a sort-and-summarize item on a printed table (MS-DAT-DC-23); days 40 to 46
stay in the calendar for the school's own use, so units 5 and 6 and the pinned checks do not move."

LAYER sequence. REPEAT new. Confidence: likely.

### 7. The team program days (11 to 13) have the pair boilerplate, with a self-contradiction

What is wrong. Days 11 to 13 are team days, but their notes say "one device per pair, driver and navigator switch"; the
team size and how a team shares one program are never stated. Day 11's note also says "the shared digital tool part of
MS-PRO-PD-15 is marked part met without a device" and then "the day runs on the paper path, which meets the id in full".
Days 12 to 14 do not repeat the part-met line.

Why it matters. MS-PRO-PD-15 is the course's one inclusive-collaboration id; "everyone types" cannot be planned without
a team size and a device arrangement, and the contradiction will be copied into the day plans.

Fix (settled below). Teams of four on one device, four roles (driver, navigator, tester, recorder) rotating every eight
minutes; on paper the recorder writes and the same rotation holds. Day 11's note: delete "which meets the id in full"
and keep "the shared digital tool part of MS-PRO-PD-15 is part met without a device until the editor view exists";
days 12 to 14 repeat that line.

LAYER sequence. REPEAT new. Confidence: firm (the note text).

### 8. Day 37 holds four ids, one a tool task, in 40 minutes, with no time budget

What is wrong. Lesson one of the mid-year check scores DC-21, DC-22, DC-23 (sort, filter, group and summarize a new
table to answer two questions with a sentence per step) and DC-24 (two problems, causes, two options and their effects)
in about 40 minutes. Day 62 is similar with four written society and systems items.

Why it matters. The DC-23 task alone can fill 20 minutes; an unsized sitting is how items get cut at writing time.

Fix (settled below). Day 37 note: about 6, 6, 16 and 12 minutes for DC-21, DC-22, DC-23 and DC-24; the DC-23 table is
at most 15 rows. Day 62 note: about 10 minutes an id.

LAYER sequence. REPEAT new. Confidence: judgment call.

### 9. Day 49 is tagged Application but is a predict-and-watch session

What is wrong. Day 49 ("predict, then watch in a toy network") makes nothing; the frame defines Application as a make,
design or society session and lists only unit 5 session 5 (day 51) as Application.

Fix. Day 49 kind becomes Understanding; the .md kind count becomes 30 Understanding, 17 Application.

LAYER sequence. REPEAT new. Confidence: firm (frame "Day kinds").

### 10. Units 3, 4 and 5 run a week earlier than the frame's text says; For the lead 3 names only part of it

What is wrong. With the pinned spread, unit 3 runs weeks 13 to 17 (frame: 14 to 18), unit 4 weeks 19 to 23 (frame: 20
to 23) and unit 5 weeks 23 to 26 (frame: 24 to 27). The checks are on the frame's pinned weeks, and the cross-subject
bridges are already handled on the right days (days 31 to 33 before math unit 8; day 47 before science unit 5 on
school day 116, with the either-order bridge). Only the frame wording is stale.

Fix. For the lead 3 lists all three drifts for the next frame sync; no day changes.

LAYER frame. REPEAT new. Confidence: firm (arithmetic).

### 11. Computing and society cases: one unsupported claim, sources to date

What is wrong or at risk.
- The frame's unit 6 text says Dorothy Vaughan "learned and taught programming for its first electronic computers".
  NASA's biography (opened 2026-11-26) supports: led the segregated West Area Computing unit from 1949, the agency's
  first African-American manager, separate dining and bathroom facilities until 1958, then the integrated Analysis and
  Computation Division, an expert FORTRAN programmer. It does not support "first electronic computers". Day 58's note
  does not repeat the claim, but the unit plan writer reads the frame.
- The ssa.gov history pages refused an automated read (403): browser check, ssa.gov/history (the punched-card records
  from the 1930s and the move to electronic computers in the 1950s, from memory).
- The IMLS public library computer access figure (day 58): the agency's data releases were disrupted in 2025 (from
  memory; imls.gov's survey page returned 404). The card names the survey year it uses.
- The FTC children's privacy guidance in the sensitivity pack: the children's privacy rule was amended in 2025 (from
  memory); teacher source lines cite the current rule's date.
- Day 29's supplied photo carries a time and place in its properties: the place is an invented or public location, never
  a real school's.

Fix. Day 58's note adds the supported wording: "she led the West Area Computing unit, was the agency's first
African-American manager, and became an expert programmer in the language used on its electronic computers"; For the
lead adds the frame wording fix. Day 29's note adds "the photo's place is invented or public, never a real school".
Day 58's note adds "the IMLS card names its survey year".

LAYER sequence (and frame for the Vaughan line). REPEAT new. Confidence: firm on Vaughan (NASA page); from memory on
IMLS and the FTC rule.

### 12. A few retrieval openings are arbitrary or unnamed

What is wrong. Day 51 (a packet trip with a loss) retrieves g6-data-about-people, which the day does not use; day 28
(metadata) retrieves g6-model-algorithm. Days 17, 18, 19, 24, 28, 35 and 55 name a retrieved row but no task.

Fix (settled below). Day 51 retrieves g6-verify-algorithm (choose the inputs that would test a resend); day 28 retrieves
g5-collect-tools (name each column's unit, the opening step to metadata). The unit-plan writer names the task for the
others; no change needed to the scope there.

LAYER sequence. REPEAT new. Confidence: likely.

## What is right and should not be touched

- The trace, modify, make order in unit 1 (days 1 to 6, then 7 to 9, then the team program 10 to 13) and the first
  text view read on days 1 to 3 before any student writes text (the lens's bridge).
- The paper path on every device day, with the four ids that need a device marked "part met without a device" and
  never "met"; MS-PRO-VD-16 and MS-PRO-PD-12 met in full on paper.
- The readiness table: every assumed row is a grade 5 row, each retrieved inside its first day, no readiness check
  needed (checked against the progression's `assumes`).
- The math bridges (variable as a named box, average as the total shared out, median and spread left to math) and the
  science either-order bridge on day 47.
- Lesson two of each check drawn as new items, not the earlier end-of-unit forms, and stated so.
- No id claimed outside the frame's 17; the two begun ids (MS-DAT-IM-28, MS-SYS-SE-32) carry no codes.
- Sensitivity guards on days 29, 30, 43, 44, 58, 60 and 61, the health steps, and no company named.

## Lens checklist (scope and sequence layer)

| Line | Status |
|---|---|
| All five concepts get taught days | Met (programming 13, algorithms 15, data 10, systems 9, society 6 teaching days) |
| AI inside the concepts, not one late unit | Met (unit 4 reads unit 3's table as a training set) |
| Read before write, then modify, then make | Met |
| Unplugged teaches, plugged tests | Met; every unit has an unplugged session |
| Notional machine taught | Met (be the computer, trace-tables, days 1 and 4) |
| Debugging as a method | Met (g5-systematic-debug retrieved on days 5, 6, 12, 20, 22; day 22 hidden fault) |
| Practices inside content, pair roles | Met for pairs; team days need finding 7 |
| Society with evidence and dated cases | Met with finding 11 |
| An id claimed only by a day that teaches it | Met except finding 1 |
| Specialty or S2 id claimed | Not applicable (none) |
| Non-specialist teacher can teach it | Not judged at this layer |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 27 adds accuracy (rounded reading, missed afternoon high); day 33 adds a fourth question needing another granularity or the metadata, codes add MS-DAT-DC-21 and MS-DAT-DC-22; day 37's DC-21 item asks for one accuracy effect | Finding 1: the accuracy part and an applied day before scoring | days.csv, scope-and-sequence.md |
| Short path: day 29 folds into day 28's last 10 minutes with the device step kept | Finding 2: keeps DC-22's device part | scope-and-sequence.md |
| Procedure items on days 14, 38 and 63 add "name it and say one way it is clearer or easier to reuse" | Finding 3 | days.csv |
| Days 54, 55 and 62: impacts of two different kinds, named by kind; day 54 shows all three | Finding 4 | days.csv |
| Clear `assess` on days 36 and 61; delete For the lead 1 | Finding 5, gate fixed 2026-11-26 | days.csv, scope-and-sequence.md |
| Unit 4 leave-out: day 63 swaps its two unit 4 items for MS-PRO-VD-16 and MS-DAT-DC-23 items; days 40 to 46 stay in the calendar | Finding 6 | days.csv, scope-and-sequence.md |
| Team days: teams of four, one device, driver, navigator, tester and recorder rotating every eight minutes; day 11's contradiction removed and the part-met line on days 12 to 14 | Finding 7 | days.csv |
| Day 37 minutes 6, 6, 16, 12 and a table of at most 15 rows; day 62 about 10 minutes an id | Finding 8 | days.csv |
| Day 49 kind Understanding; kind counts 30, 3, 17, 8, 6 | Finding 9 | days.csv, scope-and-sequence.md |
| Vaughan wording as the NASA page supports; day 29 photo place invented or public; IMLS card names its year | Finding 11 | days.csv |
| Day 51 retrieves g6-verify-algorithm; day 28 retrieves g5-collect-tools | Finding 12 | days.csv |

## For the lead (not Cory)

- Frame sync: the week ranges in finding 10 and the Vaughan line in finding 11 (frame unit 6 text).
- Browser check: ssa.gov/history pages (403).

## For Cory

None. Nothing here changes scope, money, people or audience.

## For the source list

- nasa.gov/people/dorothy-vaughan: opened 2026-11-26; supports the West Area Computing, 1949 supervisor, segregated
  facilities and FORTRAN facts, not "first electronic computers".
- ssa.gov/history/hfaq.html: 403 to automated reads.

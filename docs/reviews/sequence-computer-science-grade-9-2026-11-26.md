# Expert read: scope and sequence of computer-science-grade-9 (2026-11-26)

Job: docs/pipeline/briefs/sequence-read.md through build/scope-writes/CS-READ.md, {subject} = computer science.
Read cold; this reader did not write the scope.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/computer-science.md, build/scope-writes/CS-BRIEF.md, AGENTS.md.
- The bar: docs/ADOPTION-BAR-SUBJECTS.md, the shared core (C1 to C16) and "5. Computer science"; the parts of
  docs/courses/computer-science/APPROACH.md on day kinds, how a day opens, daily evidence, unit field 5 and pacing;
  STANDARD.md on device-only ids.
- docs/courses/computer-science-grade-9/scope-and-sequence.md and data/plans/computer-science-grade-9/days.csv (64 rows),
  read in full.
- docs/courses/computer-science-grade-9/frame.md in full; the 17 g9 rows of data/progressions/computer-science.csv; the 12
  owned statements in data/standards/csta-2026-statements.txt; the boundary statements of HS-SOC-HI-38, HS-ALG-PS-04,
  HS-SYS-SE-31, HS-PRO-PD-12, HS-PRO-VD-16 and HS-SYS-HW-29 in the source store's CSTA PDF
  (S:\CurioClass-sources\computer-science\csta-2026-11-21, read, not copied); docs/courses/CALENDAR.md rule 4; the
  grade 9 rows of data/plans/calendar.csv.
- Earlier reads for repeat tags: docs/reviews/sequence-computer-science-grade-6-2026-11-26.md (its finding headings) and
  the computer science frame reviews named in CS-BRIEF.md.
- Gates: `sequence.py check computer-science-grade-9` 0 failures; `plan.py check` and `frame.py calendar` show nothing
  for this course; `stale.py check` names nothing in this course. School days rechecked by hand from the stated formula
  (odd day 5(w - 1) + 2, even 5(w - 1) + 4, w = ceil(n / 2)): every row matches, and every check sits in the frame's
  weeks (12 in 6, 24 in 12, 33 and 34 in 17, 35 in 18, 42 in 21, 53 in 27, 62 in 31, 63 and 64 in 32). scripts/sequence.py
  lines 328 to 335 now accept a course-level check on the day after a unit's last day as that unit's end-of-unit
  assessment.
- No outside page was fetched for this read. The satellite positioning, 1983 airliner, 2000 signal and 2024 encryption
  facts are checked from memory (marked so below); the unit writer opens the sources the frame names.

## Verdict

The scope is sound and close to ready: the frame's six units, owned rows and day counts are kept, trace comes before
modify before make on every programming row, every device day carries the four ways and a paper path, pair roles
switch on every device day, and the calendar math and check weeks are right. The biggest risk is in the assessments:
several owned ids are checked on fewer parts than their statements hold (VD-16's "create", SE-31's two kinds of
measure, HW-29's management of other software), and debugging is assessed twice but never taught as a method. The one
change that matters most is finding 1 with finding 2: a prompt per part on days 12, 34, 53 and 63, and a named debug
step on two device days before the first debug item. 11 findings.

## Findings, most serious first

### 1. Three owned ids are checked on fewer parts than their statements hold

What is wrong.
- HS-PRO-VD-16 is "create a program" that stores, accesses and changes data. Every unseen item on it is a trace (day 12:
  "a trace with a prompt each for store, access and change"; day 34: "trace a new list-and-record program"). The
  "create" part rests only on the day 11 product, and day 12's note scores that product as the design (HS-ALG-PS-01);
  no rubric look-for for store, access and change is named.
- HS-SYS-SE-31 asks for "different types of cybersecurity and physical security measures" and the trade-offs. Day 50
  teaches both kinds, but day 53 asks for "a new measure with its trade-offs" and day 63 for "a measure's trade-off":
  neither asks a student to tell a cyber measure from a physical one, or to name one of each.
- HS-SYS-HW-29 says the operating system manages "both the hardware and other software components". Day 53's prompts
  are "a prompt for memory and one for peripherals" (both hardware); the managing of other software (tasks waiting,
  taught on days 44 and 46) has no prompt. Day 63's item is "what the operating system does in a new case", with no
  part named.

Why it matters. The brief asks for a prompt per part of each code on every check that lists it. A student who can
trace a list program but cannot write one passes VD-16 on paper; a student who knows only passphrases passes SE-31.
The unit writer builds the items from these notes.

Fix.
- Day 11 note: "The design rubric also carries HS-PRO-VD-16's look-fors: data stored, accessed and changed in the chosen
  structure." Day 12 note: the 12-minute trace item becomes trace 8 plus a 4-minute write item (add three lines that
  store a new record and change one value). Day 34: the VD-16 item ends with one written line that changes a value.
- Day 53 and day 63: the SE-31 item names one cyber and one physical measure for the case, then a trade-off for users,
  data and devices (a prompt each). Day 53's operating system item adds a prompt on a task that has to wait; day 63's
  HW-29 item names its parts (a piece of software sorted, and one thing the operating system manages in the case).

LAYER sequence. REPEAT yes (grade 6 read findings 3 and 4, the same kind). Confidence: firm (the statements' own words
against the day notes).

### 2. Debugging is assessed twice and never taught as a method

What is wrong. Day 12's sitting has "a debug task" (10 minutes) and day 63 has "a short debug task on a modular program"
(HS-PRO-PD-12). No teaching day names a debugging step: CT9 appears as "tests before done" (day 11) and "same tests
before and after" (day 18). The lens and the frame (CT9 test, debug and refine, units 1 and 2) ask for debugging taught
as a method: predict, run, compare, find the first line where it goes wrong, change one thing, test again.

Why it matters. A busy writer will build day 12's item with no day that taught it, which is an assessment on something
untaught; and a non-specialist teacher gets no step to model.

Fix. Zero added days. Day 6 (device, make) keeps its Parsons opener and, before the make, adds "one planted bug found
with predict, run, compare, first wrong line (about 6 minutes)"; the note says it is grade 8's CT9 method retrieved, and taught in full for a student who did
not take grade 8. Day 21 (split a given program) adds one planted bug in a module call found the same way (about 5
minutes). Name CT9 on days 6 and 21.

LAYER sequence. REPEAT new. Confidence: likely (lens, frame practices line; no source fetched).

### 3. The shorter path breaks modify-before-make once and does not fit day 1 in 40 minutes

What is wrong.
- The 10-day fold "21 (given program split) into day 22, which starts from the split solution key" removes the only
  modify day for HS-PRO-PD-12: students go from a trace (day 20) to making their own modular program (day 22) after
  reading a key. APPROACH.md: "A make day never comes before a trace or modify day on the same construct"; a key read is
  not a modify.
- Each fold puts 8 to 12 minutes into a host day that already fills its minutes (day 8, 10, 15, 18, 22, 40, 45, 52), and no
  host day says what it gives up. Days 18 and 40 are device days with about 33 teaching minutes.
- "A shorter period (40 minutes). Every day holds." Day 1 is 45 minutes with no slack (hook 5, retrieval 3, worked
  program 6, roster 17, exit 4, readiness 10); cutting the exit ticket to one question saves about 2. "The second worked
  example moves into the next day's opener" does not say which example on days 2 and 4, each of which has four.

Why it matters. The short path is the plan a school with fewer days actually teaches; as written it puts a make before
a modify and leaves the writer to invent cuts.

Fix.
- Swap the fold-in: keep day 21; fold day 32 (the audit claim, begun HS-ALG-IM-10, never scored) into day 31's last 10
  minutes as the exit ticket. The total stays 10 days and 450 minutes, nothing owned is touched, and the begun-id share
  falls.
- Add one line per host day: what it cuts to take the folded minutes (for example day 18: the second test-table run is
  done as the exit ticket; day 40: the chart is drawn for one parameter change only).
- 40-minute day 1: drop the 3-minute retrieval trace (the readiness check tests the same grade 8 row) and take the hook
  to 4: 4 + 6 + 17 + 3 + 10 = 40. Days 2 and 4: "the fourth operation's worked example and change move into the next
  day's opener".

LAYER sequence. REPEAT yes (grade 6 read finding 2, a short path that cuts a part). Confidence: firm (APPROACH.md order
rule; the minutes in the day notes).

### 4. Day 28's key claim about random search is wrong as stated

What is wrong. Day 28: students "explain why a random-pick search finds a target sooner on some runs but not on
average". That is true only when every position is equally likely and picks never repeat. If picks can repeat, random
pick is slower on average (about n tries against about n/2). If targets tend to sit near the end of the list (new
entries appended last), random pick is faster on average than a front-to-back search. The CSTA boundary for HS-ALG-PS-04
itself says a random approach "might pick elements at random to find a target more quickly in certain datasets".

Why it matters. C3(a): a key that states a conditional result as a rule; a student who reasons from the boundary's own
example would be marked wrong.

Fix. Day 28 goal: "explain why a random-pick search finds a target sooner on some runs and later on others, and why it
can do better than a front-to-back search when targets tend to sit near the end". Day 27's random pick never repeats a
slot (stated in the note). The key says the "not on average" claim holds only when every position is equally likely.

LAYER sequence. REPEAT new. Confidence: firm (the arithmetic; the CSTA boundary statement).

### 5. The environmental factor for HS-SOC-HI-38 is a technical one, and the check's unseen case has a weak one

What is wrong. The boundary statement asks for "key moments where nontechnical forces directly influenced its design,
adoption, or ethical challenges". Day 56's environmental factor is "the upper atmosphere bends the signal, which led to
correction systems": a physical constraint solved by engineering, which reads as a technical factor. Day 57's draft and
the day 58 rubric then score "the environmental cause" on that fact. The year-end unseen case (library catalogs, from
card drawers to online search) asks for "one societal and one environmental point on its trajectory", and library
catalogs have no clear environmental driver, so the 200-word packet may not hold one.

Why it matters. The scored product and the check both rest on a factor the standard's boundary may not count, and the
unseen case may make the environmental prompt unanswerable from its packet.

Fix (settled below). Day 56 keeps the atmosphere point as a technical fact, and takes as its environmental factor the
uses that drove civilian adoption in the natural environment: tracking earthquakes and ground movement, precision
farming that cuts fuel and fertilizer, wildlife and weather tracking (gps.gov applications pages, opened and dated by the
unit writer). The year-end unseen case becomes numerical weather forecasting by computer (from the first computer
forecasts of the 1950s to today's national forecast models; government sources at noaa.gov), where storms and the
need for warnings directly drove the computers built, and the public's need for warnings is the societal point. If the
lead keeps library catalogs, the packet must name a dated environmental factor before the item is written.

LAYER sequence. REPEAT new. Confidence: likely (one boundary statement; reasonable readers may count the physical
environment).

### 6. Days 32 and 58 still carry `assess` = `end` on teaching days

What is wrong. Unit 3 ends on day 32 and unit 6 on day 61; the course-level checks follow on days 33 and 62, which
sequence.py now accepts as those units' end-of-unit assessments. Day 32's `end` marks an unscored begun-id claim, and
day 58's marks a feedback and revision day. The scope's unit 3 and unit 6 Assessment paragraphs, the day 32 and day 58
notes and For the lead 2 explain a gate need that no longer exists.

Why it matters. A reader of the CSV takes day 32 as unit 3's end-of-unit assessment, when it scores nothing; day 58's
mark puts a score on a teaching day.

Fix. Clear `assess` on days 32 and 58. Day 32 note: replace the sentence that begins "Unit 3's end-of-unit assessment is
the mid-year check" with "The claim is collected for grade 11, unscored." Day 58 note keeps "The revised analysis is unit 6's scored product, scored by
rubric before the year-end check and reported with it." Rewrite the two Assessment paragraphs to say the check on days
33 and 34 (62 and 63) stands for the unit's end-of-unit assessment, and delete For the lead 2.

LAYER sequence. REPEAT yes (grade 6 read finding 5). Confidence: firm (sequence.py lines 328 to 335).

### 7. Day 22's product requires an object after a single trace day

What is wrong. HS-PRO-PD-12 asks for "procedures, external libraries, or objects": any of the three. Day 22's make
requires "at least two procedures, one library function and one object", and the object (a Python class, with its
self and its set-up method) is traced once, on one screen (day 20), and changed once (day 21), the thinnest teaching of
any construct in the course. A pair whose program is clean and modular without a class would not meet the product's
look-fors.

Why it matters. The rubric would score below the standard's own bar on the least-practiced construct, and a grade 9
novice is most likely to stall there.

Fix (settled below). Keep the object on days 20 and 21. Day 22 and day 23: "at least two procedures and one library
function; one object where it fits the program", and the rubric scores PD-12 on reuse and readability, not on the count
of kinds.

LAYER sequence. REPEAT new. Confidence: a judgment call (the frame asks for one small class; the statement does not).

### 8. The device-only reasoning for the checks is applied to two of the three device-only ids

What is wrong. The Course-level checks section leaves out HS-DAT-DC-21 and HS-SYS-HW-30 "because a paper check item
would only reach part met without a device". HS-PRO-PD-12 is device-only too (frame Devices), yet day 63 samples it with
a paper debug item and does not say what that reaches.

Why it matters. The record for PD-12 at year end would claim more than the paper path can show.

Fix. Day 63 note: "The PD-12 debug item has a device version, as day 34's trace item does; on paper it is recorded part
met without a device." Add PD-12 to the sentence in Course-level checks, so the reasoning names all three ids.

LAYER sequence. REPEAT new. Confidence: firm (frame Devices; STANDARD.md "Devices and rooms").

### 9. Day 21 is a modify day tagged Application

What is wrong. The frame and the scope call day 21 "modify, device" (split a given program); APPROACH.md's kinds put
a modify day under Fluency. The CSV says Application.

Why it matters. The unit plan writer builds an Application day as a make day; that would put two make days (21, 22)
before any modify of modules.

Fix. Day 21 `kind` = Fluency. The unit's kind counts stay inside the gate (checked: Fluency days 9, 16, 18, 30, 39 plus
21).

LAYER sequence. REPEAT yes (grade 6 read finding 9). Confidence: firm.

### 10. Device boilerplate, retrieval columns and one opening do not match the day

What is wrong.
- Days 46, 47, 48 and 51 run a toy page, not the editor, but their notes say "3 minutes to open the editor file". Day 40
  names "Tool: a supplied queue simulation page" and then the editor boilerplate again.
- Day 51's note says the trade-off card game opens "in place of the retrieval trace", while its `retrieves` column names
  g9-data-and-people.
- Day 58 has no opening at all ("No retrieval trace: the feedback needs the minutes"). APPROACH.md "How a day opens":
  every day opens in its first five minutes with one of three things.

Fix. Days 46 to 48 and 51: "3 minutes to open the page". Day 40: one tool line (the queue page fed from the editor's
generator). Day 51: either clear `retrieves` or make the card game's cards carry unit 4's transit case (then keep
g9-data-and-people). Day 58: opens with (b), the commonest wrong point from day 57's drafts, two minutes.

LAYER sequence. REPEAT yes (grade 6 read findings 7 and 12). Confidence: firm.

### 11. The readiness checks leave most of the class without a task

What is wrong. Each ten-minute readiness check (days 1, 13, 25, 35, 43, 54) is "for a student who did not take grade 8";
the scope does not say what a student who took grade 8 does in those minutes, and a teacher often cannot tell who took
it (transfers, other schools' electives).

Fix (settled below). Every student sits the readiness items; for a student who took grade 8 they are the year-before
retrieval the frame asks for, and the teacher reads them to find who needs the worked example on the unit's first
understanding day. One sentence in "Earlier-grade rows and their treatment".

LAYER sequence. REPEAT new. Confidence: likely.

## Checked and right (do not touch)

- **Order inside units.** Unit 1: trace (1, 3, 5) and guided modify (2, 4) before the make on day 6; the design
  understood (7, 8), modified (9), then made (10, 11). Unit 2: trace (14, 15), modify (16, 18), modules traced (19, 20),
  modified (21), made (22, 23). Unit 4's generator traced (38), modified (39), applied (40). Each unit reaches its
  compelling question.
- **Owned ids.** All 12 sit on taught days in the frame's units, each "in full" on a named day; no id is claimed outside
  the frame's rows; the six begun ids carry the `~` mark and are never scored.
- **Calendar.** school_day formula and weeks as above; the checks miss every grade 9 core check week but the shared
  finals week; week 17 with ELD and week 31 with library are no break of rule 4.
- **Devices.** 17 of 50 teaching days are device days, every unit has unplugged days, every device day has the four
  ways, pair roles that switch, the save minutes, the screen break and the safety line; the three device-only ids are
  marked part met without a device on the paper path.
- **Checks that do not repeat.** Each check's lesson one stands for the unit's end-of-unit assessment with new items;
  lesson two draws only from earlier units and repeats no end-day item; the year-end lesson one is a timed response,
  not the drafted form of days 57 and 58.
- **Society cases and guards.** Unit 3's invented club cases with the distance-as-income note, unit 4's transit case
  with no student asked about travel or status, unit 6's airliner told as a dated fact with no images or role play, the
  private career note that may be left out. From memory: GPS began as a 1973 defense program; after the airliner was
  shot down on 1 September 1983 the President announced civilian access once the system was complete; the deliberate
  error (selective availability) was turned off on 1 May 2000; the first post-quantum encryption standards were
  published by the federal standards institute in August 2024. All accurate as the scope states them.
- **Bridge judgment.** The writer's budget (about 40 minutes on days 1 to 5) and its verdict (enough for some earlier
  programming, not for none) are honest; I agree.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Fold day 32 into day 31's exit ticket in place of folding day 21 | Keeps PD-12's modify day; the folded day is a begun id, never scored | scope-and-sequence.md, days.csv (days 31, 32 notes) |
| 40-minute day 1 drops its 3-minute retrieval trace, hook 4 | The readiness check tests the same grade 8 row | scope-and-sequence.md, day 1 note |
| Day 28 claim: random pick can beat a front-to-back search when targets sit near the end; picks never repeat | Matches the CSTA boundary and the arithmetic | days.csv days 27, 28 |
| Day 56 environmental factor: environmental uses that drove civilian adoption (gps.gov applications); atmosphere kept as a technical fact | Boundary asks for nontechnical forces | days.csv day 56, unit 6 text |
| Year-end unseen case: numerical weather forecasting by computer (noaa.gov), replacing library catalogs | Its environmental and societal drivers are plain in government sources | days.csv day 62, scope-and-sequence.md |
| Day 22 product: an object where it fits, not required | PD-12 says "or"; the class is the thinnest-taught construct | days.csv days 22, 23 |
| Every student sits the readiness items | Doubles as the year-before retrieval; the teacher cannot always tell who took grade 8 | scope-and-sequence.md |
| Day 21 kind Fluency | It is a modify day | days.csv day 21 |
| Planted-bug debug step on days 6 and 21, CT9 | Debugging taught before day 12 and day 63 assess it | days.csv days 6, 21 |
| Day 58 opens with the commonest wrong point from day 57, two minutes | Every day opens with one of APPROACH's three openings | days.csv day 58 |
| Quantum wording on day 59: "a qubit's state combines 0 and 1 until it is measured, and a measurement gives 0 or 1; it does not try every answer at once" | Heads off the commonest misreading of "a blend" | days.csv day 59 |

## For Cory

- **Entry with no programming at all** (scope For the lead 1, frame For the lead 6). The bridge is enough for a student
  with some earlier programming and not for one with none. Many grade 9 elective students will have taken no middle
  school computer science, so this decides who the course serves. The writer's pick, an entry provision of four
  worked-program sheets beside days 1 to 6 rather than a stated prerequisite, is the one I would take, with the debug
  step of finding 2 added to those sheets.
- **Begun ids and C1** (frame For the lead 5) stays the lead's call; with the fold in finding 3 the short path's share
  of begun-id days falls by one.

## For the source list

- gps.gov applications pages (agriculture, environment, surveying) for day 56's environmental factor; not opened in
  this read.
- noaa.gov history of numerical weather prediction, for the year-end unseen case; not opened in this read.

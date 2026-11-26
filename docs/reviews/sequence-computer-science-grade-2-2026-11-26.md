# Expert read: scope and sequence of computer-science-grade-2 (2026-11-26)

Cold read by a fresh Claude agent (PRODUCTION-PATH step 3, docs/pipeline/briefs/sequence-read.md, with
build/scope-writes/CS-READ.md). I did not write the scope or the frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/computer-science.md, docs/ADOPTION-BAR-SUBJECTS.md part 5,
  build/scope-writes/CS-BRIEF.md, docs/pipeline/briefs/sequence-read.md.
- docs/courses/computer-science-grade-2/scope-and-sequence.md and data/plans/computer-science-grade-2/days.csv (all 32
  rows, goal and note in full).
- docs/courses/computer-science-grade-2/frame.md in full; the g2 rows of data/progressions/computer-science.csv; the 16
  E2 statements in data/standards/csta-2026-statements.txt; docs/courses/CALENDAR.md (grade 2 rows, rule 1) and the
  grade 2 math, ELA and computer science rows of data/plans/calendar.csv.
- docs/reviews/sequence-computer-science-grade-6-2026-11-26.md, for the REPEAT tags.
- Gates: `plan.py check` (sequence computer-science-grade-2: 0 failures), `frame.py calendar` (computer science grade 2
  weeks 11 and 26, no break), `stale.py check` (nothing for this course), `gate.py --course computer-science-grade-2`
  (0 new failures; one standing lint line, frame.md "licence", finding 11).
- Outside: the Computer History Museum abacus page (opened 2026-11-26). The Smithsonian NMAI khipu page and one other
  source (Britannica, quipu) both returned 403: status "browser check" for the lead.

The gates settle day numbers, unit counts, kinds, an assessment per unit, respond days, owned ids and the calendar
weeks; I checked them by eye only where a finding needed it. All 16 E2 ids sit on days, no other id is claimed,
`school_day` = 5n puts every unit and both checks in the frame's weeks (checks 11 and 26, respond 12 and 27), and every
grade 1 row in the frame's Seams table opens as retrieval on the day that first uses its grade 2 row.

## Verdict

The scope is sound: trace, modify, make holds on both programming constructs (days 7 to 9, 13 to 17), every unit has
an unplugged path, the society cases are guarded and the readiness and retrieval logic is right. The biggest risk is
practical, not conceptual: until the picture-block editor exists, the paper path is the course for days 14 to 17, and
that path as written (one taped floor grid for 15 pairs, laid and lifted inside a 30-minute special) will not run in
most rooms. The one change that matters most is to move the paper path onto a desk mat per pair, with the floor grid
kept for the teacher's demonstration. Assessment days also need their read-aloud and spoken groups sequenced, not run
at once.

## Findings, most serious first

### 1. The paper path for days 14 to 17 (and 20) cannot run as written in a 30-minute special

LAYER frame, sequence. REPEAT new. Confidence: likely (strong reasoning; the frame's own cost line shows one grid).

**What is wrong.** Days 14, 15, 16 and 17 run on "picture-block cards laid on the floor grid and run by a partner
acting as the robot", with "the last four minutes put cards and tape away". The frame costs "two rolls of masking tape
for a floor grid", one grid. With 15 pairs working at once, one grid serves one pair at a time; a specials teacher
cannot tape and lift a grid each week inside 30 minutes; and most of unit 3's programs are dances (clap, stomp), which
need no grid at all. Since the editor does not exist (later.csv L148), this paper path is the only path the days have.

**Why it matters.** A writer builds four device-or-paper days on a set-up that leaves 13 pairs waiting. The trace and
debug evidence (E2-PRO-PD-04, E2-PRO-TR-07) depends on every pair running its program.

**Fix.** In days 14 to 17 and 20, and the Device days paragraph: the paper path is a printed desk mat per pair (a
small grid with a paper token as the robot, for movement programs such as the square) and, for dance programs, the
partner acts the cards out at the desk, seated or standing in place. The taped floor grid is used once, by the teacher
at the front (the day 13 anchor, the day 16 worked bug, the day 19 sample act-outs). Put-away stays four minutes (cards
and mats into the pair envelope). Frame edits for the lead: Paper path and Safety bullets (floor grid lines apply to
the teacher's grid only), Costs unit 3 (15 printed mats in place of one roll of tape, about the same cost).

### 2. On every assessment day the teacher is asked to read the paper task aloud and hear five spoken groups at once

LAYER frame, sequence. REPEAT new. Confidence: likely.

**What is wrong.** Days 5, 11, 19, 26 and 31: "whole-class paper task of about 15 minutes ... the spoken item heard in
five groups of six" during it. The frame's reading rule says every card is read aloud to grade 2. One teacher cannot
read items aloud to 30 children and sit with a group of six in the same minutes. Day 5's groups run about 3 minutes
each, 15 minutes, the whole task. Day 26 holds seven scored items (four unit 4 items, E2-DAT-DC-08 as two look-fors,
three sampled items) inside the same 15 minutes.

**Why it matters.** Either the read-aloud is skipped (the scores then measure reading) or the groups are rushed.

**Fix.** On each check day: items read aloud together first (about 10 minutes, collected), then the five spoken groups
(about 15 minutes) while the class does a quiet unscored picture task (draw your own step-card, color the next unit's
anchor card). With the three-minute retrieval, that is 28 of 30 minutes, so retrieval stays only if the paper part is
kept to 10 minutes. On day 26, drop the sampled E2-SYS-SE-12 item (the mid-year check already sampled it) so the paper
part fits; the frame's year-end row changes with it (lead's frame edit). The 25-minute shorter period then reads:
retrieval dropped, 10 paper plus 15 spoken.

### 3. Day 9's `observe` mark is a stale gate placeholder, and For the lead 1 is out of date

LAYER sequence. REPEAT yes (grade 6 finding 5). Confidence: firm (lead fix 2026-11-26: sequence.py accepts the
course-level check on the day after a unit's last day as its end-of-unit assessment).

**Fix.** days.csv day 9: clear `assess`; delete from its note "The observe mark is ... see For the lead)". In the .md,
unit 2 Assessment: delete the sentence beginning "Day 9 carries `observe`"; unit 4 keeps day 25's `observe` (it marks
a real record, the E2-DAT-DI-09 observation); delete For the lead 1 or replace it with "Resolved: sequence.py accepts
the check day as the unit's end (lead 2026-11-26)". Run sequence.py check after.

### 4. Two spoken look-fors sit on teaching days whose goals never name them, and one lands on a new-model day

LAYER sequence. REPEAT yes (the grade 6 read's untimed day, finding 8). Confidence: likely.

**What is wrong.** E2-SYS-HW-11's spoken part (how the parts work together for a new action) is heard on days 3 and 4,
whose goals are the benefit-risk-chart and the pretend page; only the notes mention it, with no task or card named.
E2-DAT-DI-09 is heard from ten children on each of days 23, 24 and 25, again with no task in the goals. Day 24 first
teaches the training set, a new model, in 23 teaching minutes, and loses five of them to an unrelated question task.

**Why it matters.** A section writer works from the goal; the look-for will be dropped or improvised, and day 24's new
model is squeezed.

**Fix.** Days 3 and 4 goals add: "then each child explains one new action card (a press, the part, what changes) to
the teacher, about 6 minutes, fifteen children". Days 23 and 25 goals add: "last 5 minutes (day 25: 7 minutes), each
child refines one new vague prompt card, said or drawn to the teacher, fifteen children". Day 24 carries no look-for
(settled below). Update the unit 4 Assessment paragraph and day 26's note ("days 23 and 25").

### 5. E2-SOC-HI-14's "express ideas" part is taught by the cases but never asked

LAYER sequence, standard. REPEAT yes (grade 6 finding 3, a part taught and not asked). Confidence: firm (statement:
"to help them solve problems and express ideas").

**Fix.** Day 29 goal: "say what problem each solved or what idea it helped people record or share, and for whom".
Day 31 item: "say what problem the tool solved or what idea it helped its people share". Braille (reading and writing)
and khipu (records) carry the ideas part; the abacus the problem part.

### 6. The timeline order is not fixed by the named teacher sources

LAYER sequence. REPEAT new. Confidence: likely (CHM page read 2026-11-26; khipu pages blocked).

**What is wrong.** Day 29 places the abacus, khipu and braille on a strip where "a place marks a documented use or
object". The Computer History Museum page gives no origin date for the Chinese or Japanese abacus: its dated items are
an 1878 drawing, an 1879 restaurant abacus and a 1946 contest, and it says abacuses "remain common today". A writer who
takes the dated object puts the abacus after braille (1820s, from memory), which teaches children the abacus is newer.
The NMAI khipu page returned 403 (browser check), so the khipu period cannot be confirmed here either.

**Fix.** Each case card is a span, not a point: from the earliest use its source documents to today where the source
says it is still used. Abacus: "used for centuries in China and Japan, still common today" (CHM), drawn as the longest
span; khipu: the Inka period and earlier Andean peoples, as the NMAI page words it (lead opens it in Claude in Chrome);
braille: from the 1820s to today (Library of Congress page). Day 29's note names this, and day 31's new card follows
the same rule.

### 7. The make products (days 9 and 17) have no named look-for, so bar item 8's "projects with rubrics" is thin

LAYER sequence. REPEAT new. Confidence: a judgment call.

**Fix.** Days 9 and 17 notes name a three-line by-exception look-for for the pair's product, unscored, used by the
respond days: it has a start (event); the repeat holds the steps that repeat; it was tested and changed when it went
wrong. No `assess` mark. Day 19 stays the scored code item.

### 8. Pair roles are missing on days 14 and 16, and the paper path's roles are never named

LAYER sequence. REPEAT new. Confidence: firm (lens: "pair work with no roles").

**Fix.** Days 14, 15, 16 and 17 notes: "navigator reads and lays the cards, driver (or robot on the paper path) runs
them; switch at the halfway signal (IC5)". Unit 3 Practices line: IC5 on days 14 to 17.

### 9. Small mismatches inside unit 3

LAYER sequence. REPEAT new. Confidence: firm.

- Day 14's goal labels "the score on its screen" as a named box; the paper path has no screen. Fix: on the paper path a
  labeled cup "score" sits by the mat and the teacher changes its value card after each run (labeled, not coded).
- Day 18's goal says "Unplugged telling" while the note and frame call it device session 6. Fix: "Telling (device day;
  the program open on screen, or on its block cards on the paper path)".

### 10. The shorter path folds modify days into the two heaviest days without saying where the minutes come from

LAYER sequence. REPEAT new. Confidence: likely.

**Fix.** In the Shorter path table: each fold-in replaces the host day's three-minute retrieval opening and takes about
five minutes in all (one card or one block changed, predicted and run). Add: "The course-level checks keep weeks 11
and 26; a lost week before a check moves the teaching days, never the check."

### 11. Standing lint line in the frame

LAYER frame, process. REPEAT new. Confidence: firm. frame.md Base text bullet: "Open Government Licence" is the
licence's proper name and should stay; the lint flags it as UK spelling. Fix: the lead either adds the name to the
lint's allow list or the gate baseline keeps it; nothing to change in the scope.

## What is right and should not be touched

- Order: system-diagram before the device trace, chart before online consequences, repeat on cards (unit 2) before
  blocks (unit 3), named box before the labeled score, explain after the child's own make.
- Trace, modify, make on both constructs, and debugging taught as a method on day 16 with the anchor bug from day 13.
- The math bridge (repeat count 2 to 4, counted pass by pass, before math's equal groups in weeks 27 to 29) and the ELA
  bridge on day 18; math graphs (weeks 1 to 4) precede day 21.
- Retrieval: every grade 1 row opens as retrieval on its first-use day; no readiness checks are needed, none placed.
- Machine learning sits inside the data unit with an unplugged sorter and an uneven training set, with no claim that a
  sorter thinks.
- Sensitivity guards (no home questions, health's steps on day 4, NCDJ wording on day 10, khipu not a lost mystery, no
  blindfolds) are on each day.

## Lens checklist (scope and sequence layer)

| Line | Status |
|---|---|
| All five concept areas taught, not programming alone | Met (one unit each) |
| Read, then modify, then make | Met (days 7 to 9, 13 to 17) |
| Unplugged teaches, plugged tests; every unit has unplugged work | Met; paper path not workable as written (finding 1) |
| Notional machine taught (one step at a time, named box) | Met (days 13, 14, 16) |
| Debugging as a method | Met (day 16) |
| Practices inside content; pair roles | Part met (finding 8) |
| Society with evidence, dated cases, more than one view | Met in design; dating rule needs fixing (finding 6) |
| AI not a late unit | Met |
| No id below or past its boundary; no Specialty id | Met |
| End-of-unit assessments read, lay or debug a program, not recall | Met; logistics (finding 2) |
| Project with a rubric | Thin (finding 7) |
| Tool with a named job, no install or account | Met (tools named, both queued) |
| Non-specialist teacher | Not judged at this layer |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 24 carries no E2-DAT-DI-09 look-for; days 23 and 25 hear fifteen children each | Keeps the new model's first day whole | days.csv days 23 to 26; scope unit 4 Assessment |
| Day 9 `assess` cleared | Gate placeholder no longer needed | days.csv day 9; scope unit 2, For the lead 1 |
| Timeline cases drawn as spans to today, per source | The abacus source gives no origin date | days.csv days 29, 31 |
| Day 12 retrieval becomes one input-output action laid on the system-diagram (g2-io-parts) | Day 14 repeats day 12's event-block task word for word | days.csv day 12 `retrieves` and note |
| Paper-path score on day 14 is a labeled cup the teacher updates | No screen on the paper path | days.csv day 14 |
| Fold-in modify replaces the host day's retrieval, about five minutes | Host days are full | scope Shorter path |
| Pair roles named on days 14 to 17 | Lens and frame IC5 | days.csv days 14 to 17 |

Findings 1 and 2 also need frame edits (Paper path, Safety, Costs; year-end check contents): the lead's, listed above.

## For Cory

None. Every finding is item-level or the lead's frame edit; nothing changes scope, money, people or audience.

## For the source list

- Computer History Museum, "The Versatile, Venerable Abacus" (computerhistory.org/revolution/calculators/1/1), opened
  2026-11-26: no origin date for the Chinese or Japanese abacus; dated objects 1878, 1879, 1946; "remain common today".
- Smithsonian NMAI Inka khipu page (americanindian.si.edu/exhibitions/infinityofnations/andes/143866.html): 403 on
  2026-11-26, status "browser check". Britannica "quipu" (britannica.com/technology/quipu) also 403, "browser check".

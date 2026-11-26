# Expert read: scope and sequence, Computer Science, Grade 4 (2026-11-26)

Cold read by the curriculum expert (docs/agents/EXPERT.md), on docs/pipeline/briefs/sequence-read.md as
build/scope-writes/CS-READ.md sets it. The scope was written by a fresh Claude agent; this reader did not write it.

## What I read

- docs/courses/computer-science-grade-4/scope-and-sequence.md and data/plans/computer-science-grade-4/days.csv (all 32
  rows), cold.
- Beside them: docs/courses/computer-science-grade-4/frame.md (whole), the grade 4 rows and their assumes in
  data/progressions/computer-science.csv, the E4 statements in data/standards/csta-2026-statements.txt, the grade 4 rows
  of data/plans/calendar.csv, the ELA row e4-explain-events in data/progressions/ela.csv.
- The bar: docs/ADOPTION-BAR-SUBJECTS.md part 5, docs/courses/computer-science/APPROACH.md (How a day opens, daily
  evidence, section fields), the lens docs/agents/lenses/computer-science.md, build/scope-writes/CS-BRIEF.md.
- Gates: `plan.py check` (no failure for this course), `frame.py calendar` (no failure), `sequence.py check
  computer-science-grade-4` (0 failures), `stale.py check` (its failures are in other courses' frames, none here).
- No outside source was opened on this read. The computing and society facts below (Annie Easley at the Lewis center,
  Mary Golda Ross on the 2019 Native American dollar, Jerry Lawson's cartridge console, the first programmers of an
  early electronic computer, the EPA electronics page) are checked from memory and agree with the frame; the unit
  writer opens and dates each source as the frame says.

## Verdict

The scope is sound and close to ready: it follows the frame day for day, keeps trace before modify before make in both
the algorithm and the programming units, places all 19 E4 ids, fits the frame's weeks exactly (school_day = 5n), and
handles the sensitive society and data cases with the frame's guards. The biggest risk is in the assessments: three
end-of-unit items ask about only part of their standard (hardware and software faults, workers who keep updating their
skills, individuals and groups), so a student can pass an item without the other half of the code ever being checked.
The one change that matters most is to rewrite those prompts on days 5, 17 and 31 so each part has its own prompt; the
rest are small fixes to the shorter path, the now-unneeded `end` mark on day 9 and two note lines.

## Findings, most serious first

### 1. End-of-unit items that ask about only part of a code (moderate)

LAYER sequence (and frame, which has the same wording). REPEAT yes (parts of a standard not each prompted, as in earlier
sequence reads). Confidence: firm (the statement text and the item text, side by side).

- **Day 5, E4-SYS-HW-12** ("identify and fix common hardware and software issues"): the item is "a new staged fault",
  one fault, so a student is checked on hardware or on software, never both. Day 1 teaches both kinds (cable out;
  volume, window, airplane mode). Fix: the goal and note read "two new faults, one hardware (an accessory cable) and one
  software (a setting or the wrong window), each worked through the steps to a safe fix that is checked".
- **Day 5, E4-SYS-IM-15** ("natural resources and the environment"): "one effect and one user action" lets one effect
  stand for both. Fix: "one effect on resources (material or energy in) and one on the environment (waste out), and one
  user action".
- **Day 17, E4-DAT-IM-11** ("individuals and groups"): "who could be helped and who hurt" does not ask for both an
  individual and a group, though day 16 teaches "which person and which group". Fix: "a new case card: who collects,
  what and why, and one person and one group who could be helped or hurt".
- **Day 31, E4-SOC-CE-19** ("adopts new computing technologies and continues to update their computing skills"): the
  item asks only "what they had to learn"; day 30 teaches "how they kept learning" too. Fix: "a new worker case: what
  they had to learn when the tool arrived, and one way they keep learning".

Cost: an item that checks half a code gives a met mark the course record cannot back, and the section writer builds the
key from the scope's wording. The frame's end-of-unit text for units 1 and 5 has the same gap (HW-12, CE-19); the lead
may carry the fix into the frame's Units table.

### 2. Shorter path: the folded respond day leaves two codes with no response (moderate)

LAYER sequence. REPEAT yes (shorter paths that fold a day without naming where all its work goes). Confidence: firm.

The 10-days-short year folds day 6 (unit 1 respond) and sends its reteach to day 12, but day 12 carries only
E4-SYS-HW-12 and E4-SYS-SE-13. A student who missed the E4-SYS-NT-14 or E4-SYS-IM-15 item on day 5 never answers it
again in a new form in that year. Fix, in the fold table's day 6 row: "the E4-SYS-NT-14 retry is day 11's retrieval
(already a new connection item); in the short year day 9's retrieval becomes a new device-life item for E4-SYS-IM-15 in
place of the login-or-permission cards, which day 11 samples anyway; day 12 adds both codes to its reteach".

Also in "A shorter period (30 minutes)": "The two 30-minute sittings (days 5, 11, 17, 31)" names four sittings; it
should read "The four 30-minute sittings". And day 5 is a station day: a 30-minute sitting plus the five-minute device
close does not fit a 30-minute period. Fix: add "in a 30-minute period day 5's fault items run on picture fault cards,
with no device close".

### 3. Day 9's `end` mark is no longer needed (minor)

LAYER process. REPEAT new for this subject (music 3 to 5 used the same workaround). Confidence: firm.

sequence.py now takes a course-level check on the day right after a unit's last day as that unit's end-of-unit
assessment (lead fix 2026-11-26), so day 11 stands for unit 2 without help. Day 9 is a make day whose algorithm is
explicitly unscored; an `end` mark on it reads as an assessment on a teaching day and would be counted by later tools as
one. Fix: clear day 9's `assess` cell; in its note replace "End-of-unit, kept-work part: ... it is not scored on its own"
with "The fixed algorithm is collected and read beside day 11; it is practice, not scored"; in the .md unit 2
Assessments drop "Day 9 carries `end` for the kept-work part" and delete For the lead 1 (or mark it landed). Day 23
keeps its `end`: it is the one scored product the frame sets (rule 19), built on day 22, revised on day 23 before any
score, and it is a real part of unit 4's end-of-unit assessment, not a teaching day's mark.

### 4. E4-PRO-TR-08's "repeatedly throughout the development process" rests on one item (minor)

LAYER sequence. REPEAT yes (a part of a code carried only by a single item). Confidence: likely.

Day 24's debug item is one find, fix and retest in a given build. The part of the code that makes it more than a single
fix, debugging again and again as the program grows, is what each member does on days 22 and 23 (a test-table after
each part, every test rerun after the revision), but the day 23 rubric reads only the member's part and its comment.
Fix: day 23's note adds a third rubric look-for per member, "the member's test-table rows: the part tested when it was
added and again after the revision", and day 24's note says E4-PRO-TR-08 is met by the sitting's item together with that
record.

### 5. Pair roles missing on unit 4's first two device days (minor)

LAYER sequence. REPEAT new. Confidence: likely (lens "Pair work with no roles"; frame IC5 is unit 4's practice).

Days 21 to 23 name driver and navigator switching every eight minutes; days 19 and 20, also pair device days in the same
unit, name no roles, so the first two editor sessions of the year run with whoever grabs the mouse. Days 1, 13, 14 and 15
are pair device days with the same gap. APPROACH puts the switch time in section field 7, so this is cheap: add the unit
4 line to days 19 and 20, and "pairs switch at the keys halfway" to days 1, 13, 14 and 15.

### 6. Day 11's fault item as worded cannot show a fix and a check (minor)

LAYER sequence (frame wording too). REPEAT new. Confidence: likely.

E4-SYS-HW-12 is an "apply" id whose look-for is a fault found, fixed with a safe step and checked (frame, Evidence). Day
11 samples it with "a new staged-fault picture"; a picture shows a fault but not what happens after a step. Fix: "a new
picture fault card that shows the device's response after each chosen step", the format day 1 and day 5 already use.

## What is right and should not be touched

- Trace, modify, make: unit 2 is days 7 (trace), 8 (modify), 9 (make); unit 4 is 19 (trace in a trace-table, predict
  then step through), 20 (run and compare), 21 (modify a broken build with the test-table), 22 (team make), 23 (reader
  check and revision before the score). Nothing is used before it is taught; the score logic is supplied and traced,
  never written (grade 5's).
- Day 21 typed Understanding with the reason given (it first teaches the test-table and the piece-by-piece method). I
  agree and settle it; the frame bullet's fix stays with the lead (scope For the lead 2).
- Calendar: days 11 and 24 sit in weeks 11 and 24, the frame's check weeks; respond days 12 and 25; end-of-unit days 5,
  17 and 31 in weeks 5, 17 and 31. Week 11 holds no grade 4 check (science's respond day only); week 24 shares music's
  year-end check, both specials. The three same-year leans meet calendar.csv or carry their bridge: math unit 7 (weeks 20
  to 22, bridge on day 8), science unit 3 (weeks 11 to 14, bridge on day 2), ELA unit 2 (weeks 8 to 16, met before day
  22).
- Readiness and retrieval: every assumed row is grade 3's, the year before, and each opens as a retrieval in the day
  that first uses it; no readiness check is needed and none is placed. Earlier units of this year return in the
  retrievals of days 8, 9, 11, 15, 17, 23, 24, 27 and 31.
- Every device day carries the four ways, the paper path and the Safety lines; DC-09 and DI-10 are marked part met
  without a device and every other id is met on paper, as the frame sets.
- Society and data cases: invented people for teams, data and workers; class data about books only; pretend paper
  logins with health's steps; Mary Golda Ross told as her own work; no product or company names; no claim that a machine
  thinks or that coding improves general thinking.
- The source map: every Year 5 lesson placed or cut with a reason, and the one reorder (Selection in quizzes lesson 5
  before 4) explained.
- Load: two days each for the two rows the progression read counts as two sessions, two for the data investigation and
  report; no unit over 25 days.

## Candidate cells

All settled: unit 1 kept at zero days (the systems sort as day 1's retrieval), unit 2 kept (a read-aloud partner step on
day 9), unit 3 kept (paper record cards inside day 13), unit 4 kept (the quiz-evaluating step as day 23's reader check),
unit 5 dropped with its reason (a worker's visit needs the school's own arrangement).

## Lens checklist (scope and sequence layer)

| Line | Status |
|---|---|
| All five concepts taught, not programming alone | Met (one unit each; ML inside algorithms with society) |
| Read before write, then modify, then make | Met (units 2 and 4) |
| Unplugged teaches the idea, plugged tests it | Met (every unit unplugged; device days pair with paper) |
| Notional machine taught (trace-tables, be the computer) | Met (days 19, 21, 24, partner as computer) |
| Debugging as a method | Met (days 1, 21 to 23); part of TR-08 under-read (finding 4) |
| Practices inside content, pair roles that switch | Part met (finding 5) |
| Society with evidence, dated cases, more than one view | Met (dated teacher source lines; benefit and risk charts) |
| AI not a late add-on with nothing under it | Met (unit 5 stands on unit 3's table and grade 3's sorter) |
| CSTA id at its depth, no Specialty or S2 claim | Met |
| No unit without an unplugged path | Met |
| End-of-unit reads, traces or writes a program; rubric for the project | Met (day 24 items; day 23 rubric) |
| A tool with a named job, no install, account or network | Met (table tool, editor, sorter; three modes queued, L148) |

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 5: two fault items (one hardware, one software); device-life item asks one resource effect and one environment effect | Each part of HW-12 and IM-15 gets its own prompt | days.csv day 5; .md unit 1 Assessments |
| Day 17: case card item asks one person and one group | IM-11 names individuals and groups | days.csv day 17; .md unit 3 |
| Day 31: worker item asks what they had to learn and one way they keep learning | CE-19's second part | days.csv day 31; .md unit 5 |
| Day 9: clear `assess`; note says practice, not scored; drop scope For the lead 1 | The gate now takes day 11 as unit 2's end | days.csv day 9; .md |
| Day 23 keeps `end` | The frame's one scored product, rule 19 | none |
| Day 23 rubric adds each member's test-table rows; day 24 note names TR-08 met with that record | TR-08's repeated-through-development part | days.csv days 23, 24 |
| Short year: NT-14 retry on day 11's retrieval, IM-15 retry on day 9's retrieval, both added to day 12 | Folded day 6 leaves them unanswered | .md Shorter path |
| 30-minute period: "four sittings"; day 5 fault items on picture fault cards | Count slip; device close does not fit | .md Shorter path |
| Days 19, 20: driver and navigator every eight minutes; days 1, 13 to 15: switch at the keys halfway | Lens, frame IC5 | days.csv notes |
| Day 11: "a new picture fault card that shows the device's response after each chosen step" | The apply look-for needs a fix and a check | days.csv day 11; .md mid-year check |
| Day 21 stays Understanding | First teaching of the test-table | none (frame bullet: lead) |

## What I could not judge

- The archived base lessons (later.csv L149): the Source map rests on the public unit pages, as the frame says; the
  nine provisional days are named in the .md.
- Whether a grade 4 writer can do day 11's own algorithm, a trace and a judgment in 30 minutes: plausible, untested.

## For Cory

Nothing. Every finding is item level inside the standards.

## Sources

None opened on this read; facts on the society cases are from memory and match the frame's named sources (NASA's Easley
biography, the US Mint 2019 Native American dollar page, the Computer History Museum, the EPA electronics donation and
recycling page, the BLS Occupational Outlook Handbook), which the unit writer opens and dates.

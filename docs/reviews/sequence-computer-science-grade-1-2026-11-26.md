# Expert read: scope and sequence, Computer Science, Grade 1 (2026-11-26)

Cold read by the curriculum expert (docs/agents/EXPERT.md), on docs/pipeline/briefs/sequence-read.md as
build/scope-writes/CS-READ.md sets it. The scope was written by a fresh Claude agent; this reader did not write it.

## What I read

- docs/courses/computer-science-grade-1/scope-and-sequence.md and data/plans/computer-science-grade-1/days.csv (all 32
  rows), cold.
- Beside them: docs/courses/computer-science-grade-1/frame.md (whole), the grade 1 rows and the kindergarten rows they
  assume in data/progressions/computer-science.csv, the E1 statements in data/standards/csta-2026-statements.txt, the
  grade 1 line of `frame.py calendar`.
- The bar: docs/ADOPTION-BAR-SUBJECTS.md part 5, docs/courses/computer-science/APPROACH.md (day kinds, How a day opens,
  daily evidence, Pacing), the lens docs/agents/lenses/computer-science.md, build/scope-writes/CS-BRIEF.md, and the
  grade 4 sequence read of today (docs/reviews/sequence-computer-science-grade-4-2026-11-26.md) for REPEAT tags.
- Gates: `sequence.py check computer-science-grade-1` 0 failures; `plan.py check` has failures only in other courses
  (algebra-ii items and the like), none here; `frame.py calendar` places this course's checks in weeks 13 and 27, as
  the frame and the scope say; `stale.py check` flags the frame (frame.md:286, finding 9), not the scope.
- No outside source was opened. The computing and society facts (library next-book suggestions and picture-making
  tools as pattern-finding systems; letter to text message, library book to search, paper map to phone map) are
  checked from memory and are accurate and current; the unit writer opens and dates each source as the frame says.

## Verdict

The scope is sound: it follows the frame day for day, keeps trace before modify before make in both the algorithm unit
(days 7 to 10) and the programming unit (days 16 to 20), places all 16 E1 ids and no other, puts every day in its
frame week (school_day = 5n), and gives every device day a paper path that meets the same ids. The most serious fault
is day 25's question sort, which teaches that questions of feeling cannot be answered with data while kindergarten,
day 23 and day 26 all collect class preferences as data, so a child is taught two opposite things in one unit. Three
end-of-unit or check items ask about only part of their code (E1-ALG-ML-02, E1-PRO-VD-05, E1-SOC-CE-16), and the
people-or-computer sort says computers repeat "without mistakes" in the year that teaches bugs. All the fixes are
wording and item changes inside the days; none changes what the course owns.

## Findings, most serious first

### 1. Day 25 sorts preference questions as not answerable by data, against K, day 23 and day 26 (serious)

LAYER progression, frame and sequence (the same wording in all three). REPEAT new. Confidence: firm (the statement
text and the rows side by side).

Day 25 sorts "questions we can answer by counting or looking" against "questions of feeling, guess or imagination"
(example: "which window has the best view"). But k-ask-and-count's picture graph answers "which game" by a sticker per
child, day 23 collects "which of two class games to play" by asking, and day 26's wording pair is "which game do we
like best". A class survey of feelings is a data investigation; E1-DAT-DI-09 asks children to tell a question a data
investigation can answer from one answered "through other means". As written, a careful child concludes that day 23's
own game question was not data. A section writer will build the day 27 sort's key from this wording, so the error
reaches the scored check.

Fix (days.csv day 25 goal and day 27 goal; the lead carries the same words into the frame's unit 4 cell and
g1-data-questions' notes): "Sort question cards into questions we answer by collecting data, counting, measuring,
looking or asking everyone (how many windows does our room have; which window do most of us like best), and questions
answered another way: one person's own idea or feeling (which window do I like best), imagination (what would a
dragon see from our window) or asking someone who knows (what is our school's name); say the reason to a partner."
The "most of us / I" pair is the contrast the day teaches, and it hands straight on to g2-data-questions.

### 2. Three assessment items ask about only part of their code (moderate)

LAYER sequence (and frame, which has the same wording). REPEAT yes (parts of a standard not each prompted, as in the
grade 4 read). Confidence: firm.

- **Day 13, E1-ALG-ML-02** ("use patterns in data to make decisions or generate new things"): the items are "circle
  the machine that chose by finding a pattern" and "draw a new card into the group a pattern-finder would guess", both
  on deciding. Day 11 teaches making something new too (the drawing tool), but no item asks it. Fix: "from four
  pictured machines (a light switch, a calculator, a next-book screen, a picture-making tool), circle the two that
  find patterns in many examples, and draw a new card into the group a pattern-finder would guess".
- **Day 21, E1-PRO-VD-05** ("identify terms that refer to data values that change over time"): the item is a
  picture sort and "draw one changing thing", and the frame had "name". A drawing shows no term. Fix: each card
  carries a picture and its word (temperature, score, height, time, name, birthday), read aloud by the teacher; the
  child sorts the cards and circles the word on one changing card. No spoken load is added.
- **Day 31, E1-SOC-CE-16** ("at home, at school, and in the community"): "a new place picture" is one place, so a
  child is checked on one of the three settings. Fix: "a new three-scene strip (a home, a school room, a town place):
  on paper, draw a line from each scene to the device used there; spoken, who uses one of them and for what".

Cost: a met mark the course record cannot back, and the key is built from the scope's wording.

### 3. "Without mistakes" and no wrong guess: the AI and computer cases overstate what machines do (moderate)

LAYER frame and sequence. REPEAT new. Confidence: firm (the progression row reads "repeat the same step without
tiring"; the lens names "AI is always right" as a misconception to plan for).

Day 12's computer card says a computer can "repeat a step without tiring or mistakes"; the frame added "or mistakes",
the row does not have it. The same year teaches a program with a bug (day 18), and day 11's pattern-finder is a
guesser. A grade 1 child leaves unit 2 with "computers do not make mistakes", the misconception grade 2's training-set
row has to undo. Fix: day 12 goal reads "repeat a step the same way every time without getting tired"; day 11 plants
one wrong guess from too few examples and the teacher says "a pattern-finder can guess wrong too, so people check it";
day 11 also says once "people call these systems AI", since E1-ALG-ML-02 names AI systems and a child cannot
recognize what was never named (the word is said and shown, not tested). The lead carries the day 12 wording into the
frame's unit 2 cell.

### 4. The two course-level check sittings are over-full for a 30-minute grade 1 period (moderate)

LAYER sequence (the item lists are the frame's). REPEAT new for this subject. Confidence: likely (reasoning on the
minutes; the probe will settle it).

Day 13 asks seven paper items (find the parts, order step-cards, circle a machine, draw a card, an activity sort, a
share-or-private card, a rule scene) plus a spoken reason from all 30 children; day 27 asks cube counting and colors,
a record card, an alike-and-different answer, a question sort, three unit 1 to 3 items and a spoken answer at about
25 seconds a child. Early readers need every card read aloud, and the teacher who reads aloud to the class cannot
hear groups at the same time, so the "15-minute paper task while groups are heard" cannot run as written on day 27.
Fix: each check note gives a minute plan: minutes 0 to 3 settle and instructions; minutes 3 to 8 the read-aloud items
done together (day 13: the activity sort and the share-or-private card; day 27: the question sort and the login card),
the teacher reading each card twice; minutes 8 to 26 the picture-only items done alone while the five groups are heard;
on day 27, cubes away in the last four minutes. If the probe shows day 13 still over, the unit 1 rule-scene sample is
the one to drop (E1-SYS-IM-13 was scored on days 3 to 5 and is not sampled at year-end); that is a frame change for
the lead.

### 5. Shorter path: the fold removes both spaced unit 1 retrievals before the mid-year check (minor)

LAYER sequence. REPEAT yes (shorter paths that fold a day without placing all its work). Confidence: firm.

Folding day 9 sends its keep-safe retrieval to day 14, after the day 13 check it was spaced for, and day 10's
responsible-use retrieval is replaced by the five-minute change. Day 14's opening is already the hardware-parts
retrieval. Fix, in the fold table's day 9 row: "day 10 keeps its three-minute opening as a new pretend login card
with a rule scene (g1-keep-safe and g1-responsible-use, both sampled on day 13); the five-minute one-step change to
day 7's plan comes out of the make's minutes".

### 6. Day 24's `observe` mark and the stale notes about it (minor)

LAYER process. REPEAT yes (grade 4's day 9 `end` mark, the same workaround). Confidence: firm.

sequence.py now takes the course-level check on the day after a unit's last day as that unit's end-of-unit
assessment (lead fix 2026-11-26), so unit 4 needs no mark inside its days. Day 24's checklist note is "not a score",
and an `observe` on a make day reads as an assessment. Fix: blank day 24's `assess`; keep its note as "the teacher
notes by exception which groups chose a way to collect each piece; it shapes the day 28 groups"; delete For the lead
1 and the second Unsure bullet from the .md. Days 11 and 12 keep `observe`: they carry the real E1-ALG-IM-03 record.

### 7. Three small day fixes (minor)

LAYER sequence. REPEAT new. Confidence: firm.

- **Day 23's opening** names three retrievals (k-ask-and-count, g1-patterns-ai, m1-data-three-categories) in three
  minutes on a hook day. Fix: the opening is k-ask-and-count's picture graph only (it carries the math lean, three
  groups); the attribute retrieval moves inside the description-data step, where the kept "what is an attribute?"
  Candidate already sits.
- **Day 18's bug** is "the character jumps before it moves", but no jump block is taught (K's words are forward,
  turn, left, right; days 16 and 17 add the start block). Fix: "the character moves forward before it turns, so it
  ends on the wrong square", using only taught blocks.
- **Day 10's pair work** names no roles (lens: pair work with no roles). Fix in the note: "the carrying-out pair: one
  reads each card aloud, one does the step, switching at the halfway signal (IC5)".

### 8. Retrieval on check sittings and the word "trace" (minor, for the lead)

LAYER process. REPEAT new. Confidence: a judgment call.

APPROACH.md Pacing says every K to 5 session opens with the three-minute retrieval trace, and How a day opens
defines it as a short program or algorithm from an earlier unit. This scope gives the five check sittings no opening
(For the lead 5) and opens unit 1 and several later days with recall of rules, parts or data words, not a trace. Both
readings are sound for grade 1: a check sitting is itself retrieval, and unit 1 has no earlier algorithm to trace. Fix
(APPROACH.md, the lead's wording): "every K to 5 teaching and respond session opens with a three-minute retrieval
task, a trace where the earlier row is a program or algorithm". The scope then needs no change.

### 9. The frame trips stale.py (minor, for the lead)

LAYER frame. REPEAT yes (work-status wording outside Pending, as in other frames). Confidence: firm.

frame.md:286 ("the source map stays provisional until it is loaded") is work-status wording outside a Pending(...)
marker. Fix: wrap that clause in Pending(docs/sources/BASE-TEXTS.md#teach-computing-curriculum), as the Base text
bullet already does. The scope itself passes.

## Checked and right (do not touch)

- **Order.** Unit 1 rules before parts before the first device turn before the password; unit 2 split, two orders,
  modify (day 9), make (day 10), then patterns and people-or-computer; unit 3 changing values, worked example (day
  16), read and predict (17), debug (18), modify (19), make (20). Nothing is used before it is taught, apart from the
  jump block (finding 7).
- **Readiness and retrieval.** Every assumed row is a kindergarten row (the year before) or the same-year math lean,
  so all open as retrieval on or before the row's first day; no readiness check is owed and none sits on a unit's
  first day. The table in the .md matches the rows' assumes cells.
- **Checks that do not repeat.** Days 13 and 27 are the end-of-unit assessments of units 2 and 4, so no assessment
  sits right before them; their earlier-unit items are new forms.
- **Standards.** All 16 E1 ids sit on teaching days at the rows' depth; no MS, HS, Specialty or X + CS id is claimed;
  E1-ALG-PS-01 and E1-DAT-DC-08 are scored by named look-fors.
- **Calendar.** Weeks 13 and 27 match the frame and `frame.py calendar`; K to 5 computer science is a special (rule 1);
  the measuring bridge to math unit 6 is on days 23 and 24.
- **Device and paper paths.** Days 16 to 20 name the block-card path until L148's mode exists, and the course record
  marks no E1 id part met for lack of it. Floor-grid and device safety lines are on every such day.
- **Society cases.** Day 30 gives each activity two views with dated sources, no dates or inventors for children and
  no "newer is better"; day 29 asks no child about home devices or family work.
- **Lens checklist, scope layer.** All five concept areas taught: met. AI inside the concepts (with algorithms, then
  data): met. Trace before modify before make: met. Unplugged work in every unit: met. No id past its depth and no
  Specialty id: met. Debugging taught as a method: met. Pair roles: met on device days, missed on day 10 (finding 7).
  Society with dated sources and more than one view: met. Construct before taught: one miss (finding 7). AI never
  "always right": missed (finding 3).
- **Candidates.** All five settled with zero days or a reason.
- **Shorter path.** Present, with nothing assessed and no owned part cut; finding 5 places one retrieval.

## What I could not judge

- The base text (archived Year 2 units) is not in the store (L149), so the source map is checked against the frame's
  lesson titles only; the reorder of "Programming quizzes" lessons 3 and 4 (modify before make) is sound on the
  APPROACH order but unread against the lesson files.
- Whether day 13 and day 27 fit 30 minutes is reasoning on minutes until the probe runs (finding 4).
- Real device time is day 3 alone until the K to 2 picture-block mode exists (the scope's For the lead 4). That is
  the tool queue Cory already set (L148), not a new call.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Day 25 sort: "collect data (counting, measuring, looking, asking everyone)" against "one person's idea or feeling, imagination, or asking someone who knows", with the "most of us / I" pair | Matches K, day 23 and day 26, and E1-DAT-DI-09's "other means" | days.csv days 25 and 27; frame unit 4 cell and g1-data-questions notes via the lead |
| Day 13 ML-02 item: four machines, circle the two pattern-finders (one chooses, one makes a new picture), then the card guess | Asks both "decide" and "generate" | days.csv day 13; .md Course-level checks table |
| Day 21 VD-05: worded picture cards read aloud, circle the word on one changing card | The id asks for terms | days.csv day 21 |
| Day 31 CE-16: a three-scene strip, a line from each scene to its device, one spoken use | Home, school and community each asked | days.csv day 31; .md unit 5 Assessments |
| Day 12: "repeat a step the same way every time without getting tired" | The row's wording; computers make mistakes | days.csv day 12; frame unit 2 cell via the lead |
| Day 11: one planted wrong guess, and "people call these systems AI" said once | Lens misconception; the id names AI | days.csv day 11 note |
| Days 13 and 27: a minute plan with read-aloud items first, groups heard during the picture-only items | Early readers; the teacher cannot read aloud and interview at once | days.csv days 13 and 27 notes |
| Short path: day 10 keeps its opening as a login card with a rule scene; the change comes out of the make | Keeps the spaced retrieval before day 13 | .md Shorter path |
| Day 24 `assess` blank; delete For the lead 1 and the second Unsure bullet | sequence.py fix of 2026-11-26 | days.csv day 24; .md |
| Day 23 opening: k-ask-and-count only; the attribute retrieval inside the description step | Three minutes, one retrieval, hook day | days.csv day 23 |
| Day 18 bug: forward before turn, no jump block | Only taught blocks | days.csv day 18 |
| Day 10 roles: one reads each card, one does the step, switch at the halfway signal | Pair roles on every pair task | days.csv day 10 note |

## For Cory

None. Every finding is a wording or item change inside the days, or a lead fix to the frame and APPROACH.md.

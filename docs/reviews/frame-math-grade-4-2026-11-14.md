# Frame read: math-grade-4 (Math Grade 4), 2026-11-14

Reader: the curriculum expert, cold (brief docs/pipeline/briefs/frame-read.md). I did not write this frame.

## What I read

- docs/agents/EXPERT.md, docs/agents/lenses/math.md, docs/RUBRIC-MATH-K8.md, docs/pipeline/briefs/frame-write.md
  (the "Lessons from the social studies frames" list). By the caller's instruction I did not open the earlier grade 4
  planning (docs/courses/math-4/, math-4-spine.md, math-3-5-progression*.md, data/plans/math-4/, im-g4-draft-map.csv,
  the math-4 and reconcile reviews), though the lens points to two of them.
- The frame docs/courses/math-grade-4/frame.md and its row in data/plans/frames.csv (9 units, 160 days).
  data/plans/math-grade-4/source-map.csv does not exist; it comes with the scope and sequence.
- The 27 grade 4 rows of data/progressions/math.csv, the grade 3 and grade 5 rows; the frames before and after
  (math-grade-3, math-grade-5).
- The base text in S:\CurioClass-sources\illustrative-math\grade-4: all nine unit overviews and the "Addressing",
  "Building On" and "Lesson Timeline" blocks of all 149 lesson preparation pages, read with my own script (not the
  store's im-g4-lessons.csv); searches of the lesson pages for money, coins and prices.
- data/standards/ccss-math-standards.txt and ccss-math-focus.csv (grade 4 clusters).
- The same-year frames: science-grade-4, social-studies-grade-4, english-language-arts-grade-4.
- Earlier reads: docs/reviews/frame-math-grade-4-codex-2026-11-14.md (stopped at a missing Python module, judged
  nothing; the gate ran here) and the math grade 2 expert read of today (REPEAT tags).
- Gates: `plan.py check` exit 0; `frame.py check math-grade-4` 0 failures (9 units, 160 days, 145 in units, 15 at
  course level); `stale.py check` 0 failures. My script confirmed all 27 rows placed once and each unit's Owned
  standards equal to its rows' codes.

## Verdict

The frame is sound in structure: every row and lettered part is placed once, the base text's lesson order is kept
(its unit edges moved with reasons), all 149 base lessons are placed or cut, and the days add up (125 base lessons in
122 days, 5 of our own, 18 assessment and respond days, 15 at course level). The biggest risk is that two choices
rest on a major-work count that is neither the strict nor the guide's method: three pairs of new angle lessons are
squeezed into single days to protect a line that is not tight by the guide's rule, while four grade 3 review lessons
are counted as grade 4 major work. The one change that matters most is to count by the stated rule and spend the
squeeze on the review lessons, not on 4.MD.C.7; a close second is giving money problems (4.MD.A.2) a named home,
since the base text has almost none.

## Findings, most serious first

### 1. The angle-lesson merges rest on a miscount of major work (moderate; firm)

**What is wrong.** The Major work bullet and For the lead item 2 say grade 4 is "the tightest of the three grades",
about 67 percent, and hold the line "by merging three pairs" of angle lessons (4.7.1 and 2, 3 and 4, 14 and 15) and
cutting every optional lesson. Two problems with the count:
- It counts base lessons 2.1, 2.2, 2.3 and 2.6 as grade 4 major work. Their preparation pages tag no grade 4
  standard as Addressing: they are "Building On" 3.NF.A.1, 3.NF.A.2, 3.NF.A.3 and 3.NF.A.3d. Strictly counted
  (grade 4 major clusters only, by each lesson's main standard (read from its title and Addressing tags), assessment and respond days split in the same
  share, the year review all major, the checks at about three quarters) I get about 101 of 160, 63 percent, under
  the line; with those four lessons counted, about 105 (66 percent).
- The evidence guide's rule for indicator 1e counts supporting work connected to major work (cited with page in
  docs/reviews/frame-math-grade-2-2026-11-14.md). The frame itself names those connections: factors and multiples
  feed equivalence (unit 1), line plots add fractions (unit 3), conversion uses times as many and decimals (unit 6).
  By that rule the year is about 127 to 131 of 160 (79 to 82 percent), well clear.
Each base lesson is 60 minutes (warm-up, two activities, synthesis, cool-down); a merged pair puts about 105 minutes
of activity into one day. Lessons 7.14 and 7.15 ("Reasoning about Angles", parts 1 and 2) are the base text's whole
treatment of unknown angles by equation (4.MD.C.7, every clause); halving them narrows a standard to protect a line
that holds anyway.
**Why it matters.** A writer reading "tight" will keep cutting supporting and additional days that carry major
practice, and unit 9's merged days will be overfull or will drop the equation work of 4.MD.C.7.
**Fix (frame, Major work, unit 9, Source map, For the lead item 2).** Major work: "By days, about 101 of 160 (63
percent) counting grade 4 major clusters only and the four grade 3 review lessons of unit 2 as review; about 130 (81
percent) by the evidence guide's rule, which counts supporting work that practises major work (units 1, 3, 6 and
8). The optional lessons are cut for the day budget, not the line." Source map: un-merge 4.7.14 and 4.7.15; merge
4.2.1 and 4.2.2 ("Representations of Fractions", parts 1 and 2, grade 3 review) into one readiness day. Unit 2
becomes 17 days, unit 9 22 days; units 3 to 8 move one day earlier in the Cross-subject "about days" cells. For the
lead item 2: "Settled by the expert read; not tight by the guide's rule." LAYER frame. REPEAT yes (math grade 2
finding 1).

### 2. Money problems (4.MD.A.2) have no lesson behind them (moderate; firm)

**What is wrong.** 4.MD.A.2 names money among its five contexts, "including problems involving simple fractions or
decimals". Unit 6's cell lists money, and unit 6 opens with a readiness check on grade 2 money (m2-money skips grade
3, so this is the first money since grade 2). But base unit 5 (our unit 6) has no money problems with dollars and
cents: the only money is whole-dollar book-fair totals in 5.5 (times as many). Coins appear only in 3.18 (pesos and
centavos, in our unit 4), and dollar tables in 9.7 (the year review). The source map gives money no day of its own
and names no lesson that carries it.
**Why it matters.** A scope and sequence built from the base lessons will teach no money problem, and the course
check will test a context the year never taught. The readiness check on coins would lead nowhere.
**Fix (frame, units 4 and 6, Source map).** Unit 4, add: "Base lesson 3.18 writes cents as hundredths of a dollar
($0.35 = 35/100 of a dollar)." Unit 6, add: "Money problems in dollars and cents, written as decimals, are carried in
base lessons 5.10 and 5.13 (multi-step measurement problems) beside the other contexts; the readiness check on coins
opens them." Source map note on 4.5 1 to 17: "5.10 and 5.13 add money contexts in decimal notation (4.MD.A.2 in
full)." If the unit plan finds the load too high, the day comes from the year review (7 to 6). LAYER standard.
REPEAT yes (lesson 4; math grade 2 finding 5).

### 3. The supply table is stale and leaves a social studies question open (minor; firm)

**What is wrong.** The supply table says "their frames are written later", but science-grade-4 and
social-studies-grade-4 frames exist (this table already quotes their units and days). The social studies frame's
"For the lead" item 3 asks whether the math frame can move 4.MD.A.2 earlier; this frame answers only by implication.
The science grade 4 frame says 4.OA.C.5 is taught "in its first unit" of the math base text; here it is unit 7 (days
97 to 111), and the base text's unit 1 touches it in lesson 1.3 only.
**Why it matters.** Two frames believe different things about when 4.OA.C.5 and 4.MD.A.2 arrive; the fixer of each
reads only its own file.
**Fix (frame, Cross-subject and For the lead).** Header: "This course supplies to other subjects in the same year;
their frames are written, and the bridges below are theirs." 4.MD.A.2 row, add: "Math keeps the base text's order
(unit 6, days 78 to 96): social studies unit 1 keeps its own routine and its unit 6 comes after." For the lead, new
item: "Replacement text for docs/courses/science-grade-4/frame.md, Cross-subject, 4.OA.C.5 row, third cell: 'Before
unit 3; the math course teaches it in its unit 7 (about days 97 to 111), after science unit 3, so the bridge
applies.' Replacement for docs/courses/social-studies-grade-4/frame.md, For the lead item 3: 'The math frame keeps
4.MD.A.2 in its unit 6 (days 78 to 96); unit 1's routine stays.'" LAYER process. REPEAT yes (math grade 2 finding 4;
the social studies reads).

### 4. A year-review lesson compares living costs between countries (minor; likely)

**What is wrong.** Base lesson 9.7, merged with 9.8 into a review day, compares costs by "times as much" from tables
of a meal and jeans in Bermuda and India and of rent, utilities and preschool in the United States and Ghana. The
frame's own rule in unit 6 is "Money problems use prices of class items, never family income", and its sensitivity
bullet says no unit needs a qualified reader because the contexts are measurement, food, school, building and art.
**Why it matters.** Rent and preschool are family costs, and a table that shows African and Asian countries as cheap
places invites the "poor country" framing the Curio Class sensitivity reads flag; students from those countries sit
in the room.
**Fix (frame, Course-level checks, year review row, or Source map 4.9 row).** "Lesson 9.7 keeps its multiplicative
comparison work; its country cost tables are replaced with prices of school items in two named towns." LAYER base
text. REPEAT new.

### 5. Merged lessons have no rule for what a day keeps (minor; firm)

**What is wrong.** Five merges (4.7.1 and 2, 3 and 4, and 14 and 15 in unit 9; 9.1 and 2, 9.7 and 8 in the year
review), each two 60-minute lessons in one day, with no word on what is dropped.
**Why it matters.** The day writer will overfill the day or drop a different piece each time.
**Fix (frame, Source map, each merge row).** "A merged day keeps one warm-up, the first lesson's main activity in
short form, the second lesson's activities, one synthesis and our exit question; the dropped activities are named in
the day-level source map." LAYER base text. REPEAT new.

### 6. "split" names a routine reuse in the source map (minor; firm)

**What is wrong.** Row "4.9 | 10 to 12 ... | Warm-ups through the year | split". Split is defined as one base unit
into two of ours.
**Fix (frame, Source map).** Decision "cut", note "not days; the three routines are used as warm-ups". LAYER base
text. REPEAT new.

## Lens checklist, course frame layer

| Line | Result |
|---|---|
| Major work under the line, by units, days or time | Met by units (6 of 9 outright, 67 percent) and by the guide's rule (about 81 percent by days); strictly by grade 4 major clusters alone about 63 percent. Finding 1 |
| A supporting cluster that does not practise major work | Met: 4.OA.B (equivalence), 4.MD.A (times as many, decimals), 4.MD.B (adding eighths) each practise major work, and the frame says how |
| A source-map row with no keep, split, merge, cut or ours decision | Met, one decision word wrong (finding 6) |
| A skill owned by two grades, a handoff that skips a grade | None. The four weak handoffs from grade 2 (three-digit place value, unit size, money, the circle) each get a readiness check in the first unit that needs them; the angle and symmetry threads that skip to grades 7 and 8 are named |
| A model used before the grade that builds it | None |
| A limit broken | None. Denominators 2, 3, 4, 5, 6, 8, 10, 12, 100; unlike denominators only for tenths and hundredths; no multiplication or division algorithm; remainders without "R"; three-step cap |

## The brief's other checks

- **Owned skills:** 27 rows, each in exactly one unit.
- **Standards in full:** every lettered part placed (4.NF.B.3a to d, 4.NF.B.4a to c, 4.MD.C.5a, b). In part: 4.MD.A.2
  (finding 2), and 4.MD.C.7 at risk from the merge (finding 1). The days of our own cover what the base text is thin
  on (subtracting from a mixed number, the different-wholes problem, measuring for an eighths line plot, zeros in
  division).
- **Units and reasons:** order holds: equivalence before operations, tenths before decimals, place value before
  multi-digit work, multiplication before division, times as many before conversion. Unit 6 keeps numbers within
  facts and multiples of 10, 100, 1,000, which unit 5 taught.
- **Days:** 8 + 18 + 19 + 11 + 19 + 19 + 15 + 15 + 21 = 145; checks 4, respond 4, year review 7: 160. Each unit's
  count equals its kept lesson days, its days of our own and two.
- **Source map:** 149 lessons: 125 placed in units (122 days after three merges), 12 optional cut (every optional
  lesson), 9 year-review lessons in 7 days, 3 routines as warm-ups. The new edges (base unit 3 section C joined to
  base unit 4 section A; base unit 6 split at section C; base units 7 and 8 joined) fall on section edges and keep
  every lesson in order. No NC or reference source mapped.
- **Review units (empty Skills cell):** none; the base text's unit 9 becomes 7 course-level review days (no new
  standard), justified.
- **Seams:** this "Picked up" table matches the grade 3 frame's "Handed on" table; the "Handed on" table matches the
  grade 5 frame's "Picked up" table, including m3-area-concepts passing over grade 4 to grade 5.
- **Cross-subject:** ELA grade 4 teaches W.4.1 and L.4.6 in its unit 1, before math units 2 and 6. Supplies: every
  science and social studies need has a bridge on both sides; wording in finding 3.
- **Lessons from the social studies frames:** 1 met; 2 met; 3 met (60 minutes; 120 of 149 base lessons are 60
  minutes, the rest 55 to 90 by their own timelines, which the scope and sequence should note); 4 finding 2; 5 met;
  6 met; 7 met; 8 met; 9 finding 1; 10 met; 11 met; 12 finding 4; 13 met; 14 met; 15 finding 3.

## What is right and should not be touched

- Tenths and hundredths joined to decimals as one unit, in the base text's lesson order.
- Equal groups of fractions before adding them, as the base text does; unit-fraction language throughout.
- Remainders written as 84 = 8 x 10 + 4, never "R".
- Facts checked in unit 1 and again before multi-digit multiplying, untimed and private.

## Settled by the expert

| Choice | Reason | File |
|---|---|---|
| Un-merge base lessons 7.14 and 7.15; merge 2.1 and 2.2 into one readiness day (unit 2: 17 days, unit 9: 22) | 7.14 and 7.15 carry all of 4.MD.C.7; 2.1 and 2.2 review grade 3 | docs/courses/math-grade-4/frame.md, units 2 and 9, Source map, Cross-subject days |
| Major work stated two ways: about 63 percent strict, about 81 percent by the guide's rule | The guide counts supporting work tied to major work | frame.md, Major work, For the lead item 2 |
| Money carried in base lessons 3.18 (cents as hundredths) and 5.10, 5.13 (money contexts) | 4.MD.A.2 names money; the base text has none in its unit 5 | frame.md, units 4 and 6, Source map |
| Base lesson 9.7: keep the comparison work, replace the country cost tables with school-item prices | The frame's own money-context rule | frame.md, year review |
| Merge rule: one warm-up, the first lesson's main activity short, the second lesson's activities, one synthesis | Two 60-minute lessons in one day | frame.md, Source map |
| Base lessons 9.10 to 9.12: decision "cut", routines used as warm-ups | "split" is a unit split | frame.md, Source map |

## For Cory

None new. The 60-minute day is already on the frame's "For the lead" list.

## What I could not judge

- Whether 5.10 and 5.13 can carry money without a day of their own; the unit plan decides, with the year review as the
  fallback day.
- The Progressions page pointers in the "Check set adds" cells were not re-opened.

## Sources

- IM K-12 Math 1st edition, grade 4, local copy (S:\CurioClass-sources\illustrative-math\grade-4, CC BY 4.0): unit
  overviews, optional marks, Addressing and Building On tags, Lesson Timelines; lessons 2.1 to 2.3 and 2.6 (grade 3
  review), 3.18 (coins), 5.5, 5.9 to 5.13, 7.1 to 7.4, 7.14, 7.15, 9.7. Firm.
- CCSS mathematics text (4.MD.A.2, 4.MD.C.7) and the Student Achievement Partners focus clusters (data/standards/).
  Firm.
- EdReports Math K-8 Evidence Guide v2.0, indicator 1e, as cited with page in
  docs/reviews/frame-math-grade-2-2026-11-14.md; not re-opened on this run.
- Confidence: findings 1, 2, 3, 5, 6 firm; finding 4 likely (a judgment on the context, firm on the facts).

## For the source list

None new.

**Verdict:** sound; two moderate fixes (major-work count and the angle merges; money in 4.MD.A.2). **Finding count:** 6
(2 moderate, 4 minor).

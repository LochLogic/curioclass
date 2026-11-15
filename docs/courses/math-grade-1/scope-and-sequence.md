# Scope and sequence: Grade 1 Math

Course `math-grade-1`, grade 1. Draft, 2026-11-15.

The frame's eight units keep their order, owned rows and 153 days. Four course-level check days and three respond days make 160 course days, one 60-minute meeting each school day over 32 weeks. Course day and school day are identical, so `school_day` stays empty. The authoritative daily goals, kinds, skills, codes, materials and timing notes are in `data/plans/math-grade-1/days.csv`. Sections are not divided here: each unit uses `<unit>.1` until its unit plan sets sections.

The source map places all 146 public first-edition base lessons in their original order, one per teaching day. Fourteen additional `ours` rows account for the seven original unit assessment days and seven course-level check/respond days. Unit 8's closing observation stays inside its tenth base lesson. No login-gated assessment, answer key or exit ticket is used. The map's source name and lesson titles identify credit, not classroom routine names. Adapted lessons will carry their own credit line at the lesson-writing stage.

> Adapted from Illustrative Mathematics K-12 Math, grade 1, units 1 to 8, CC BY 4.0, https://creativecommons.org/licenses/by/4.0/. Changed by Curio Class.

## Prerequisites before placing days

All earlier-grade prerequisites are kindergarten rows. Grade K is numbered 0, so grade 1 follows it directly: these receive retrieval tasks, not readiness checks. The frame's first-two-lesson and later-unit readiness wording is superseded by brief rule 2. There is no assumed row last used two or more grades back and therefore no `readiness` slot in this course. Retrieval happens inside the named day, after its hook where it opens a unit, without a separate assessment day.

The last-use column below records the latest teaching grade documented by the progression and the frame's kindergarten seam. A kindergarten `days.csv` is not present to verify that implementation. It does not justify relabelling these year-before prerequisites as older rows. The grade 1 days explicitly teach or assess their own rows; later retrieval of those rows rests on those days rather than on a passing mention.

| Earlier-grade row | Last documented teaching grade | Retrieval here and purpose |
|---|---|---|
| mk-count-on-from | K | Day 1, begin a count from a given number |
| mk-one-more | K | Day 1, each next count adds one |
| mk-how-many | K | Day 1, keep the first group's cardinality |
| mk-fluency-within-5 | K | Days 1 and 40, small addition and subtraction facts |
| mk-sort-count | K | Day 7, sort and count before representing data |
| mk-story-problems | K | Day 17, retell and act out a story |
| mk-add-sub-meaning | K | Day 17, joining and taking away |
| mk-add-sub-expressions | K | Day 17, connect actions to expressions and equations |
| mk-compare-groups | K | Day 27, match groups before finding the extra part |
| mk-decompose-to-10 | K | Day 40, find and record partners |
| mk-make-ten | K | Day 47, partners of ten before make-ten strategies |
| mk-teen-ten-ones | K | Day 47, ten ones and some more; explicitly used again on day 69 and retrieved on day 96 |
| mk-compare-numerals | K | Day 82, compare small numerals before two-digit comparisons |
| mk-measurable-attributes | K | Day 111, aligned endpoints and direct length comparison |
| mk-count-sequence | K | Day 118, count from a known start before crossing 100 |
| mk-count-to-20 | K | Day 118, match written numerals to counted objects |
| mk-one-to-one | K | Day 118, count a collection one by one before grouping tens |
| mk-shapes-positions | K | Day 129, name familiar shapes in different orientations |
| mk-analyze-shapes | K | Day 129, distinguish flat and solid shapes and describe attributes |
| mk-build-compose-shapes | K | Day 130, combine parts before treating a composite as a new unit |

The opening retrieval tasks take five minutes. Later retrieval fits the daily five-minute mixed warm-up or the named model introduction. If a gap appears, a ten-minute small-group center slot replaces repeated practice, preserving the new grade 1 goal. Readiness is not used as a label for that response.

## Evidence, practice and time

Each listed assessment code needs evidence for every part, not merely one representative question. The unit descriptions below delimit contributing evidence for a standard finished later. In particular, unit 2 begins 1.OA.A.1; its final assessment lists only the codes it completes. Unit 3's mid-unit assessment keeps within-10 fluency and early within-20 work as contributing evidence and lists the complete ten-structure and properties codes. Day 68 completes 1.OA.C.6. Unit 5 completes the no-new-ten contribution to 1.NBT.C.4.

A closing record joins independent written or drawn products to one observation per child per window. The modeled observation budget assumes 24 children. A teacher hears a child once for the named evidence and reuses the record on an end day or course-level check within ten school days. Products can establish a part of a code when the day names that product. Small groups provide access to objects and speech without making the rest of the class wait through individual turns. No timer is shown to a child. A facts record distinguishes just knows, quick strategy and counts all; objects do not establish fluency. Counting evidence is separate from arithmetic fluency.

End-of-unit response is allocated once: units 1, 2, 3, 5 and 6 use ten minutes in the next two lessons' center time; unit 4 shares day 95 with the mid-year response; unit 7 shares days 149 to 150 with year-end response; unit 8 uses the last ten minutes of day 160. Unit 3's mid-unit response is fifteen minutes on day 58. These slots replace repeat practice, not the next unit's hook. Every response ends with a short new transfer task rather than another full assessment.

Five-minute mixed warm-ups revisit taught addition and subtraction facts throughout the year, with an earlier story or place-value idea from unit 3 onward. Unit 7 reserves fifteen minutes per base lesson for number work, including its warm-up. Unit 8 targets the year-end response record. Within 20, students use strategies; grade 2 owns fluency within 20. No number line, fraction notation or standard algorithm is introduced here. Ten-frames precede ten-as-unit; towers become sticks tied to numerals; labelled tape diagrams follow matching comparisons in unit 6. Drawn tools are listed by model name. Physical materials and no-kit alternatives are in `supplies`; no digital tool or student account is needed. Math's `safety` cells remain empty as specified.

The planned major-work time remains above the frame's 7,200-minute minimum. A conservative allocation excludes all ten data-focused unit 1 days, all eighteen unit 7 days and the geometry-focused respond day 150: 131 full periods, 7,860 minutes. Adding only the explicitly reserved fifteen major-work minutes on each of unit 7's seventeen base days gives 8,115 of 9,600 minutes, about 84.5 percent. It does not count the data lessons' supporting practice as major work. By units, seven of eight teach or review major work; by base lessons, the frame's standard-tag inventory is 137 of 146. These are planning allocations, not measured lesson-part minutes; unit plans must preserve and verify them. Daily kinds mark the main purpose, while mixed warm-ups and application tasks balance understanding, fluency and application within that purpose.

All eight practices have tasks rather than assignments alone:

| Practice | Teaching task and evidence |
|---|---|
| MP.1 | Days 159 to 160: persist with a number riddle, test a possible value and revise from a conflicting clue; retain the explanation |
| MP.2 | Days 12 to 15: connect each tally to a response and interpret totals and differences; retain the survey questions and explanations |
| MP.3 | Days 106 to 110: compare two written addition methods and respond with place-value reasons; retain the closing explanation; revisit in day 160 riddles |
| MP.4 | Days 27 to 31: connect matching drawings to equations; days 122 to 128 connect those drawings to labelled tape diagrams and situation/solution equations |
| MP.5 | Days 115 to 127: choose equal length units, detect gaps or overlaps and demonstrate a valid measurement |
| MP.6 | Days 33 to 39: defend the meaning of equality in unfamiliar equation layouts; days 85 to 92 justify comparison-symbol statements |
| MP.7 | Days 41, 55 and 68: explain a preserved sum after reordering or regrouping; days 72 and 92 explain operating on tens as units |
| MP.8 | Days 57 to 59: explain the ten-and-ones pattern across sums and predict a further sum; use it in day 68 strategy explanations |

## Unit 1. Adding, subtracting and working with data

Sixteen days, course days 1 to 16, weeks 1 to 4. Counting on keeps the first quantity intact before data gives that strategy a purpose. The first six base lessons develop adding and subtracting within 10. Sorting, recording and surveying follow, then asking and answering questions about each category, the total and how many more or fewer. Days 12 to 15 deliberately reach teen totals and counting-on subtraction as an unknown addend, so m1-count-on includes both operations within 20. Data organization is ready before science and social studies use it.

Day 1 retrieves the kindergarten counting and small-fact rows; day 7 retrieves sorting. There is no readiness or mid-unit assessment. The end-of-unit assessment closes on day 16: days 14 to 15 each reserve twelve minutes for half the class's counting-on observations, and the survey product and day 16 interpretation cover every part of 1.MD.C.4. Questions must be asked as well as answered. Response occupies days 17 to 18 center slots. Surveys concern optional favorites, imagined pets and classroom objects; they never solicit family, body, income or home-life information.

Candidate settled: keep the measurement-and-data Progressions check as a unit-planning comparison, zero student days. Drop a fourth category because this grade's limit is three, and drop a separate outside-data excursion because collecting and interpreting class data already fills the needed arc. The existing survey lesson remains.

## Unit 2. Story problems

Twenty-three days, course days 17 to 39, weeks 4 to 8. Joining and taking-away situations precede part-whole reasoning; comparisons then make the difference visible through matching. Equations grow from those situations before students interpret unknowns in unfamiliar positions. Five owned rows receive unequal emphasis: the three situation families run through days 17 to 33, while equality and unknown-position reasoning recur inside them and become the focus on days 34 to 38. Early base problems within 10 extend to 20 after the representation is established. Days 20 and 36 explicitly add Take From change unknown and discussion of start unknown; no extra lesson is added.

Day 17 retrieves kindergarten stories, meanings and expressions, with matching-group retrieval on day 27. There is no readiness or mid-unit assessment. Days 37 to 38 each reserve fifteen minutes for half the class's explanation record. Day 39 closes 1.OA.B.4, 1.OA.D.7 and 1.OA.D.8: subtraction as unknown addend; equality and true/false equations in reversed and two-expression layouts; unknowns in every position of both operations. Joining, part-whole and difference-unknown comparison products contribute to 1.OA.A.1, completed in unit 6. Response is on days 40 to 41. All possessions in stories are shared classroom supplies or imagined objects and pets.

The ELA key-detail lean comes alongside math's opening, so day 17 budgets a five-minute bridge: read the story twice and model who, how many and what happened. This stays part of solving, without importing central-message work.

Candidate settled: keep the situation-table Progressions comparison in planning, zero student days. Drop two-step oral stories, since grade 1 needs the missing-number positions and comparison language in one-step stories first.

## Unit 3. Adding and subtracting within 20

Twenty-nine days, course days 40 to 68, weeks 8 to 14. This is the largest unit because five rows carry the year's central fact and strategy work. Seven base lessons build within-10 fluency; seven build ten-as-unit and teen operations; seven develop three-addend and make-ten sums; seven develop subtraction choices and mixed applications. These are successive arcs, not section plans. Day 47 establishes ten ones as one ten before a make-ten strategy can use it. Reordering and grouping are used without requiring property names. Subtraction comparisons show why reversal cannot be transferred indiscriminately.

Day 40 retrieves decompositions and within-5 facts; day 47 retrieves partners of ten and teen structure. There is no readiness check. The mid-unit assessment sits on day 57, after the first explicit make-ten work, rather than asking for it before teaching. It reuses within-10 observations from days 53 to 54, adds a make-ten sum explanation, and checks ten structure and both property strategies. The incomplete subtraction strategy range remains formative evidence until the end. Response uses fifteen minutes of day 58 centers.

Days 66 to 67 each reserve twelve minutes for half the class's closing fluency record. Day 68 combines it with short products covering all of 1.OA.C.6, both property strategies, a three-addend story with sum at most 20, and the separately coded 1.NBT.B.2a and b. Within-20 evidence includes counting on, make-ten, decompose-to-ten, related facts and known or easier sums for the appropriate operation. Response is in days 69 to 70 centers. Practice is untimed and comparisons are with the child's own earlier work.

Candidate settled: keep the operations-and-algebraic-thinking strategy-level comparison in planning, zero student days. Drop four-addend work to preserve mixed practice on the three-addend and two-addend grade 1 targets.

## Unit 4. Numbers to 99

Twenty-four days, course days 69 to 92, weeks 14 to 19. Five base lessons treat collections of tens and operations on those units. Eight then connect tens and leftover ones to numerals and mental changes of ten; five establish comparisons; five explore flexible representations. The extra closing day holds original assessment work. Zero ones and teen/decade word confusions receive explicit attention. Mental ten-more/less follows models, and comparison symbols follow quantity reasoning. Subtraction remains multiples of ten from multiples of ten, including zero differences, with an explanation tied to a written method.

Day 69 retrieves unit 3 ten structure, including the kindergarten teen row explicitly used there. Day 82 retrieves kindergarten numeral comparison. There is no readiness or mid-unit assessment. Days 89 to 91 each provide a sixteen-minute rotation for one third of the class, completing the performance record for all four owned rows. Day 92 uses that record plus short products for parent 1.NBT.B.2 and each a/b/c case, 1.NBT.B.3 with all three symbols, mental 1.NBT.C.5, and 1.NBT.C.6 with positive and zero differences, representations, written methods and reasoning. Response is day 95 only, shared with the following course-level check. Collections come from the classroom; symbols use their quantity meaning rather than animal stories.

Candidate settled: keep the base-ten Progressions comparison about teen and decade words in planning, zero student days. Drop a three-digit extension. Reading and counting to 120 belongs in unit 6; three-digit place value belongs to grade 2.

## Unit 5. Adding within 100

Fifteen days, course days 96 to 110, weeks 20 to 22. Four base lessons combine like units without making a ten, four introduce a new ten with a one-digit addend, and six extend to two-digit pairs, explanations and application. A final original assessment closes the owning row. This short unit can build on secure tens and ones instead of reteaching them. Day 100 deliberately joins unit 3's make-ten model to unit 4's tens-and-ones method, then records the strategy in writing.

Day 96 retrieves the teen row explicitly used earlier this year and unit 4's place value; no readiness or mid-unit assessment is needed. Days 108 to 109 each reserve twelve minutes for half the class's explained-method record. Day 110 reuses it and checks all of 1.NBT.C.4: two-digit plus one-digit, two-digit plus tens, and two-digit pairs, with and without a new ten, like units, models, written methods and reasoning. No standard algorithm is required. Response occupies days 111 to 112 centers. The optional food-drive context becomes a fictional class book collection, without asking for donations or discussing family giving or receiving.

Candidate settled: keep the base-ten addition comparison in planning, zero student days. Drop three two-digit addends so the short unit can complete two-addend composition and explanation without borrowing grade 2 work.

## Unit 6. Length to 120 units

Eighteen days, course days 111 to 128, weeks 23 to 26. Four base lessons establish direct and indirect comparisons, six link equal iterated units to counting and recording through 120, and seven join length contexts to all story types, followed by the original closing assessment day. The four owned rows have different loads: counting develops through measurement, while the final seven base lessons complete the story-type inventory begun in units 2 and 3. Day 118 counts a collection one by one before grouping tens; day 119 makes the new numerals and crossing 100 explicit. Rulers and a number line wait for grade 2.

Day 111 retrieves kindergarten measurable attributes. Day 118 retrieves the counting sequence, numerals to 20 and one-to-one counting. Earlier grade 1 story structures are retrieved on day 121. There is no readiness or mid-unit assessment. Days 122 to 125 redraw matched objects and cube comparisons as named, labelled tape diagrams, with a question mark for the unknown, then tie situation to solution equations. Every story quantity and answer remains within 20 even when a base measurement context uses larger measurements.

The twelve-cell inventory means three Add To cells, three Take From cells, three part-whole cells and three Compare cells. Each Compare cell also includes both more and fewer language, six variants altogether. Days 123 to 125 distribute these products, rather than demanding twelve full performances on day 128. Start-unknown and opposite-language comparisons are solved and discussed with support, without imposing grade 2 proficiency.

Day 126 provides sixteen minutes for four groups of six to demonstrate ordering and indirect comparison, and sixteen minutes for counting, reading/writing and matching a collection to a numeral. Day 127 provides sixteen minutes for whole-unit measurement with same-size units and no gaps or overlaps. Day 128 closes from these once-collected records, the story inventory and short transfer evidence: all parts of 1.MD.A.1, 1.MD.A.2, 1.NBT.A.1 and 1.OA.A.1. Response is in days 129 to 130 centers. Classroom objects replace shoe removal and body comparisons; paper comparison cards replace the optional origami craft.

Candidate settled: keep the geometric-measurement Progressions comparison in planning, zero student days. Keep measuring the same object with two unit sizes in day 117's existing ten-minute comparison discussion, zero extra days. Both sets use internally equal units; explaining the count difference supports the current length concept without claiming the grade 2 standard.

## Unit 7. Geometry and time

Eighteen days, course days 129 to 146, weeks 26 to 30. Eight base lessons develop flat/solid attributes and composition, four develop equal shares, and five develop clocks, followed by the closing assessment day. Halves of a circle precede half past. Each base day retains fifteen minutes of major number work, and the shape investigations also use counting and comparison. Day 129 retrieves kindergarten naming and analysis; day 130 retrieves composition. There is no readiness or mid-unit assessment.

The end-of-unit assessment is distributed across the last arcs. Days 135 to 136 retain flat and solid composites reused as new units, plus distinguishing attributes and building/drawing a specified shape, completing 1.G.A.1 and 1.G.A.2. The portfolio includes rectangles, squares, trapezoids, triangles, half-circles, quarter-circles, cubes, rectangular prisms, cones and cylinders. Day 136 reserves sixteen minutes for four groups of six. Days 138 and 140 each reserve twelve minutes for half the class's equal-share explanation: circles and rectangles, two and four equal shares, half/fourth/quarter-of language, the whole as two or four shares, and more shares making smaller pieces of the same whole. This completes every part of 1.G.A.3.

Days 143 to 145 reserve twelve minutes each for one third of the class to read and write whole-hour and half-hour times in analog and digital forms, including the hour hand between numbers. Day 146 closes the complete four-code record without another full performance. Its response is on days 149 to 150 only, shared with the year-end course-level check. Clock times concern school events rather than home routines; equal sharing uses paper rather than food.

Candidate settled: keep the geometry Progressions comparison in planning, zero student days. Drop a separate square-sharing extension: a square is already a rectangle, and contrasting valid circle/rectangle partitions and nonexamples in the existing equal-share work provides the needed depth.

## Unit 8. Putting it all together

Ten days, course days 151 to 160, weeks 31 to 32. This review unit owns no row and keeps all ten base lessons: three revisit facts and strategies, three revisit story structures, and four revisit collections and place-value riddles. Practice is selected from days 149 to 150's response record while preserving all three arcs. Day 156 deliberately reuses unit 6's labelled tape diagram. Retrieval is of explicit earlier grade 1 teaching; there is no readiness or mid-unit assessment.

The frame says no separate assessment lesson here. Brief rule 2 nevertheless requires every unit to close with an assessment, so days 157 to 160 provide an embedded observation, marked `observe` on day 160, with no day added and no base lesson removed. Counting and representation products cover 1.NBT.A.1 and parent 1.NBT.B.2 with a/b/c: count from a given start, read/write to 120, match collections, bundle ten ones, represent teens and decades, and explain each digit. Riddle explanations provide the final observation. The recent facts interview is reused, not collected again. The final ten minutes of day 160 respond to remaining errors and update the grade 2 handoff, including what the year-end response changed.

Candidate settled: keep the year's operations-and-base-ten thread comparison in planning, zero student days. Keep a two-clue riddle within day 160's existing writing/explanation time, zero extra days. It remains within 120 and supplies a reasoned clue rather than harder arithmetic.

## Course-level checks and the shared calendar

The grade 1 target row, rather than the calendar's general year-end example, sets math's target to weeks 19 and 30. The course-level checks stay after units 4 and 7, with their exact frame day costs. There are no additional course-level review days.

| Window | School/course days | Week | Coverage and response |
|---|---|---|---|
| Mid-year course-level check after unit 4 | 93 to 94 | 19 | Day 93 uses a new error-analysis portfolio: four different earlier-unit story types, counting related to both operations, unknown-addend meaning, equality and unknowns. Day 94 uses an incomplete strategy explanation and an untimed facts interview. Full within-20 strategy coverage and within-10 fluency are distinguished. For unit 4's skills fresh content draws only on units 1 to 3 foundations; its full place-value, comparison, mental-ten and tens-subtraction evidence is reused from days 89 to 92, with no new unit 4 task. Day 95 responds once to both records. |
| Year-end course-level check after unit 7 | 147 to 148 | 30 | Day 147 repairs a fictional measurement-and-story display and an addition explanation using units 1 to 6. It joins the full twelve-cell story inventory to fresh transfer, and covers addition within 100 and length. Day 148 uses a counting inventory through 120 and an untimed oral facts interview. Geometry, equal shares and clocks reuse days 135 to 146's full-code portfolio; no new unit 7 task follows its closing assessment. Days 149 to 150 respond, then unit 8 supplies further targeted practice. |

A course-level check does not repeat any task form from the previous ten school days. The error-analysis portfolio and incomplete strategy explanation are reserved for the mid-year check; the repaired display and counting inventory are reserved for the year-end check. Practice games remain games, not rehearsals of those forms. The mid-year oral interview was more than two weeks before the year-end oral interview. Where a child's equivalent individual evidence already exists within ten days, the check reuses it and records its source day. The two interview days each budget 36 minutes for 24 children at ninety seconds, while the class completes the independent earlier-unit work. Assessments use the complete code inventories in the unit descriptions, not just the number of fresh tasks in this table.

The grade 1 calendar puts social studies checks in weeks 14 and 31, science in weeks 15 and 29, ELA in weeks 16 and 32, and math in weeks 19 and 30. No week has two subjects' course-level checks. The nearest ELA/math check-block gaps are sixteen school days at mid-year (77 to 93) and ten at year-end (148 to 158), both beyond five. Actual math interview days are 94 and 148. No calendar tool or unit move is needed.

## Same-year leans checked against the calendar

Math's first lean is e1-key-details/SL.1.2 in ELA unit 1, school days 1 to 33. It is not safe to assume every part is completed by math day 17 merely because the unit has opened, so the day 17 bridge budgets five minutes and continues within story time if needed. Math's later RI.1.1 use on day 121 follows the whole ELA unit 1; its day still names the read-aloud question model for access.

No math row requires science first. For downstream users, math's data work on days 7 to 16 precedes social studies voting in unit 4 (school days 52 to 67), science light in unit 5 (79 to 99), and science daylight analysis in unit 8 (131 to 139). The science frame's approximate week 31 daylight note is stale; the current calendar places its analysis in weeks 27 to 28, still after math. Its fall record does not require the completed data analysis in advance.

Science leaf ordering in unit 3 (school days 45 to 56) precedes math length on day 111. Its frame's direct-ordering bridge, leaves beside each other with aligned endpoints and no units, remains necessary. Science signaling in unit 6 (101 to 116) starts before math's equal-unit work on day 115; science teaches its own end-to-end, no-gaps paper-strip or heel-to-toe bridge. Math days 111 and 115 record these timing relationships, with no added math days. Social studies unit 8 (131 to 151) follows math comparison and the completed story-type work ending on day 128. Its prices remain made-up whole dollars within 20, with no coin or decimal teaching imported into math.

## Shorter path

For a forty-five-minute period, use a five-minute mixed warm-up, a five-minute hook/model connection, twenty minutes of core work, ten minutes of practice or response and five minutes of synthesis/evidence. Preserve both the model-to-written link and the explanation; reduce repeated rounds, displays and transcription. On a rotation day the listed twelve- or sixteen-minute evidence block replaces practice and part of core work, while other groups complete the core task independently. Day 126's two sixteen-minute blocks fit with five minutes of launch, five minutes of synthesis and three minutes of recording; the measurement day follows separately. A thirty-six-minute individual course-level interview block fits with a four-minute launch and five-minute close while everyone works independently. These budgets require the unit-plan feasibility check for larger classes; extra assessment days are not silently created.

For a year ten meetings short, fold only these ten unassessed practice days into the named neighbor's existing practice slot:

| Fold-in day | Neighbor | Work preserved inside that neighbor |
|---|---|---|
| 6 | 5 | Mixed within-10 counting-on game |
| 10 | 9 | Mixed counting-on facts after representing survey data |
| 21 | 20 | Joining/taking-away story practice |
| 26 | 25 | Missing-part fact practice |
| 32 | 31 | Comparison and related-fact practice |
| 46 | 45 | Mixed within-10 facts |
| 60 | 59 | Three-addend make-ten practice in the existing strategy discussion |
| 73 | 72 | Mixed operations on tens and within-20 facts |
| 81 | 80 | Mental ten-more/less and a short tens-and-ones retrieval |
| 99 | 98 | No-new-ten addition practice |

None carries an assessment, a first prerequisite retrieval, an observation allocation, an end-of-unit response slot or a unique owned part. Keep one short round of each folded practice and reduce its repetitions. These are implementation folds, not deletions from the canonical 160-row map or changes to frame ownership. To preserve the shared check weeks, retain the named school-day positions and use those ten released positions as non-meeting days; do not renumber every subsequent lesson and bring checks forward. If a school has only 150 consecutive school days rather than ten missing math meetings within a 160-position calendar, its compressed cross-subject check calendar needs lead approval; this sequence does not claim the original weeks still apply.

## For the lead

1. The embedded unit 8 observation resolves the brief's every-unit closing requirement without an added day, while the frame still says there is no assessment of its own. Update that frame wording at its next authorized turn. Its stray reference to eleven review days also conflicts with its ten-day unit table; this sequence follows the table.
2. The frame's unit 4 and unit 7 immediate-check coverage is retained through portfolios. Unique skills in those units cannot be freshly assessed from earlier units' content without teaching them earlier. The sequence therefore uses earlier-unit foundations for fresh tasks and the completed recent record for full unique-skill coverage. The lead should confirm that this is the intended interpretation of rule 3.
3. Unit plans must test the 24-child observation and interview budgets, the forty-five-minute path and the major-work lesson-part minutes. If complete evidence cannot fit, the frame already reserves any extra day decision to Cory; no day or owned part has been removed here. The kindergarten daily record was unavailable, so the prerequisite inventory documents its progression/frame basis rather than claiming verified kindergarten lesson implementation.

All eight Candidate comparison cells and their extensions are settled above. Planning comparisons cost zero student days; kept student extensions fit named existing time. No assessment items, answer keys, section plans or lessons have been written.

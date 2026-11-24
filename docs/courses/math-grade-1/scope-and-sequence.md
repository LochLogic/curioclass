# Scope and sequence: Grade 1 Math

Course `math-grade-1`, grade 1. Draft, 2026-11-15.

The frame's eight units keep their order, owned rows and 153 days. Four course-level check days and three respond days make 160 course days, one 60-minute meeting each school day over 32 weeks. Course day and school day are identical, so `school_day` stays empty. The authoritative daily goals, kinds, skills, codes, materials and timing notes are in `data/plans/math-grade-1/days.csv`. Sections are not divided here: each unit uses `<unit>.1` until its unit plan sets sections.

The source map places all 146 public first-edition base lessons in their original order, one per teaching day. Fourteen additional `ours` rows account for the seven original unit assessment days and seven course-level check/respond days. Unit 8's closing observation stays inside its tenth base lesson. No login-gated assessment, answer key or exit ticket is used. The map's source name and lesson titles identify credit, not classroom routine names. Adapted lessons will carry their own credit line at the lesson-writing stage.

> Adapted from Illustrative Mathematics K-12 Math, grade 1, units 1 to 8, CC BY 4.0, https://creativecommons.org/licenses/by/4.0/. Changed by Curio Class.

## Prerequisites before placing days

All earlier-grade prerequisites are kindergarten rows. Grade K is numbered 0, so grade 1 follows it directly: these receive retrieval tasks, not readiness checks. The frame uses the same grade-number rule. There is no assumed row last used two or more grades back and therefore no `readiness` slot in this course. Retrieval happens inside the named day, after its hook where it opens a unit, without a separate assessment day.

Verified 2026-11-15 against `data/plans/math-kindergarten/days.csv`: all 20 distinct earlier-grade rows below have explicit kindergarten teaching or assessment days. Examples are counting from a given start on kindergarten days 106, 116 and 119, within-5 fluency on days 147 to 151, and numeral comparison on days 36 to 44. Kindergarten is the last-use grade for every row, by one method: an explicit teaching or assessment day, never a passing mention. Retrieval days carry these earlier row ids in `skills`; retrieval itself supplies no assessment evidence. Grade 1 rows later retrieved have explicit instruction earlier this year.

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

Each listed assessment code needs evidence for every part, not merely one representative question. The unit descriptions below delimit contributing evidence for a standard finished later. In particular, unit 2 begins 1.OA.A.1; its final assessment labels the taught story subtypes as contributing evidence and distinguishes the codes it completes. Unit 3's mid-unit assessment keeps within-10 fluency and early within-20 work as contributing evidence and lists the complete ten-structure and properties codes. Day 68 completes 1.OA.C.6. Unit 5 completes the no-new-ten contribution to 1.NBT.C.4.

A closing record joins independent written or drawn products to one observation per child per window. Every budget plans for 30 children. Half-class rotations mean 15 children; third-class rotations mean 10. Length and shape rotations use groups of 8, 8, 8 and 6 at eight minutes per group, with individual products read after class. A teacher hears a child once for the named evidence and reuses the record on an end day or course-level check within ten school days. Products can establish a part of a code when the day names that product. Small groups provide access to objects and speech without making the rest of the class wait through individual turns. No timer is shown to a child. A facts record distinguishes just knows, quick strategy and counts all; objects do not establish fluency. Counting evidence is separate from arithmetic fluency.

End-of-unit response is allocated once: units 1, 2, 3, 5 and 6 use ten minutes in the next two lessons' center time; unit 4 shares day 95 with the mid-year response; unit 7 shares days 149 to 150 with year-end response; unit 8 uses the last ten minutes of day 160. Unit 3's mid-unit response is fifteen minutes on day 58. These slots replace repeat practice, not the next unit's hook. Every response ends with a short new transfer task rather than another full assessment.

Five-minute mixed warm-ups revisit taught addition and subtraction facts throughout the year, with an earlier story or place-value idea from unit 3 onward. Unit 7 reserves fifteen minutes per base lesson for number work, including its warm-up. Unit 8 targets the year-end response record. Within 20, students use strategies; grade 2 owns fluency within 20. No number line, fraction notation or standard algorithm is introduced here. Ten-frames precede ten-as-unit; towers become sticks tied to numerals; labelled tape diagrams follow matching comparisons in unit 6. Drawn tools are listed by model name. Physical materials and no-kit alternatives are in `supplies`; no digital tool or student account is needed. Math's `safety` cells remain empty as specified.

Focus is counted once as minutes on major-cluster codes divided by instructional minutes, with assessment and respond days excluded. Begin with 144 instructional days at 60 minutes: exclude seven separate unit assessment days, the mid-unit assessment day, four course-level check days, three respond days and day 160's embedded closure. Subtract 411 scheduled observation minutes inside instructional days and 115 response minutes inside later lessons, each once. Retained instructional products remain instruction, with no second assessment time added. Data lessons count only their five-minute number warm-up as major work; unit 7 preserves fifteen number-work minutes per teaching day. Other data and geometry/time minutes are outside major work. The allocation is 7,011 / 8,114 instructional minutes, 86.4 percent, above the K to 2 line of 75 percent. Unit plans must preserve this allocation and verify actual lesson-part minutes.

| Unit | Major-cluster minutes | Instructional minutes |
|---|---:|---:|
| 1 | 405 | 870 |
| 2 | 1,270 | 1,270 |
| 3 | 1,525 | 1,525 |
| 4 | 1,300 | 1,300 |
| 5 | 810 | 810 |
| 6 | 906 | 906 | 60 |
| 7 | 255 | 893 |
| 8 | 540 | 540 |
| Total | 7,011 | 8,114 |

The 411 observation minutes are days 14, 15, 37, 38, 53, 54, 66, 67, 108, 109, 138 and 140 at 15 each; 89 to 91 at 20 each; 125 at 16; 126 at 31; 127 at 47; 135 to 136 at 16 each; and 143 to 145 at 15 each. The 115 response minutes are days 17, 18, 40, 41, 69, 70, 111, 112, 129 and 130 at ten each, plus day 58 at fifteen. Daily kinds mark the main purpose; mixed warm-ups and applications supply practice within that purpose.

All eight practices have tasks rather than assignments alone:

| Practice | Teaching task and evidence |
|---|---|
| MP.1 | Days 158 to 159: persist with a number riddle, test a possible value and revise from a conflicting clue; retain the explanation |
| MP.2 | Days 12 to 15: connect each tally to a response and interpret totals and differences; retain the survey questions and explanations |
| MP.3 | Days 106 to 110: compare two written addition methods and respond with place-value reasons; retain the closing explanation; revisit in days 158 to 159 riddles |
| MP.4 | Days 27 to 31: connect matching drawings to equations; days 122 to 128 connect those drawings to labelled tape diagrams and situation/solution equations |
| MP.5 | Days 115 to 127: choose equal length units, detect gaps or overlaps and demonstrate a valid measurement |
| MP.6 | Days 33 to 39: defend the meaning of equality in unfamiliar equation layouts; days 85 to 92 justify comparison-symbol statements |
| MP.7 | Days 41, 55 and 68: explain a preserved sum after reordering or regrouping; days 72 and 92 explain operating on tens as units |
| MP.8 | Days 57 to 59: explain the ten-and-ones pattern across sums and predict a further sum; use it in day 68 strategy explanations |

## Unit 1. Adding, subtracting and working with data

Sixteen days, course days 1 to 16, weeks 1 to 4. Counting on keeps the first quantity intact before data gives that strategy a purpose. The first six base lessons develop adding and subtracting within 10. Sorting, recording and surveying follow, then asking and answering questions about each category, the total and how many more or fewer. Days 12 to 15 deliberately reach teen totals and counting-on subtraction as an unknown addend, so m1-count-on includes both operations within 20. Data organization is ready before science and social studies use it.

Day 1 retrieves the kindergarten counting and small-fact rows; day 7 retrieves sorting. There is no readiness or mid-unit assessment. The end-of-unit assessment closes on day 16: days 14 to 15 each reserve fifteen minutes for half the class's counting-on observations, and the survey product and day 16 interpretation cover every part of 1.MD.C.4. Questions must be asked as well as answered. Response occupies days 17 to 18 center slots. Surveys concern optional favorites, imagined pets and classroom objects; they never solicit family, body, income or home-life information.

Candidate settled: keep the measurement-and-data Progressions check as a unit-planning comparison, zero student days. Drop a fourth category because this grade's limit is three, and drop a separate outside-data excursion because collecting and interpreting class data already fills the needed arc. The existing survey lesson remains.

## Unit 2. Story problems

Twenty-three days, course days 17 to 39, weeks 4 to 8. Joining and taking-away situations precede part-whole reasoning; comparisons then make the difference visible through matching. Equations grow from those situations before students interpret unknowns in unfamiliar positions. Five owned rows receive unequal emphasis: the three situation families run through days 17 to 33, while equality and unknown-position reasoning recur inside them and become the focus on days 34 to 38. Early base problems within 10 extend to 20 after the representation is established. Days 20 and 36 explicitly add Take From change unknown and discussion of start unknown; no extra lesson is added.

Day 17 retrieves kindergarten stories, meanings and expressions, with matching-group retrieval on day 27. There is no readiness or mid-unit assessment. Days 37 to 38 each reserve fifteen minutes for half the class's explanation record. Day 39 closes 1.OA.B.4, 1.OA.D.7 and 1.OA.D.8: subtraction as unknown addend; equality and true/false equations in reversed and two-expression layouts; unknowns in every position of both operations. Joining, part-whole and difference-unknown comparison products contribute to 1.OA.A.1, completed in unit 6. Response is on days 40 to 41. All possessions in stories are shared classroom supplies or imagined objects and pets.

The ELA key-detail lean comes alongside math's opening, so day 17 budgets a five-minute bridge: read the story twice and model who, how many and what happened. This stays part of solving, without importing central-message work.

Candidate settled: keep the situation-table Progressions comparison in planning, zero student days. Drop two-step oral stories, since grade 1 needs the missing-number positions and comparison language in one-step stories first.

## Unit 3. Adding and subtracting within 20

Twenty-nine days, course days 40 to 68, weeks 8 to 14. This is the largest unit because five rows carry the year's central fact and strategy work. Seven base lessons build within-10 fluency; seven build ten-as-unit and teen operations; seven develop three-addend and make-ten sums; seven develop subtraction choices and mixed applications. These are successive arcs, not section plans. Day 47 establishes ten ones as one ten before a make-ten strategy can use it. Reordering and grouping are used without requiring property names. Subtraction comparisons show why reversal cannot be transferred indiscriminately.

Day 40 retrieves decompositions and within-5 facts; day 47 retrieves partners of ten and teen structure. There is no readiness check. The mid-unit assessment sits on day 57, after the first explicit make-ten work, rather than asking for it before teaching. It reuses within-10 observations from days 53 to 54, adds a make-ten sum explanation, and checks ten structure and both property strategies. The incomplete subtraction strategy range remains formative evidence until the end. Response uses fifteen minutes of day 58 centers.

Days 66 to 67 each reserve fifteen minutes for 15 children's closing fluency records. Day 67 retains a three-addend story/equation, reordering/regrouping explanations, ten-ones bundle and teen representation. Day 68 names these products as its record for 1.OA.A.2, 1.OA.B.3 and 1.NBT.B.2a/b. Its only fresh work is two short equation items for 1.OA.C.6: make ten and decompose to ten. Counting-on, related-fact and easier-sum products from days 63 to 64 and earlier addition lessons complete the strategy record; days 66 to 67 supply mental fluency within 10. Nothing is re-collected child by child. Response is in days 69 to 70 centers. Practice is untimed and comparisons are with the child's own earlier work.

Candidate settled: keep the operations-and-algebraic-thinking strategy-level comparison in planning, zero student days. Drop four-addend work to preserve mixed practice on the three-addend and two-addend grade 1 targets.

## Unit 4. Numbers to 99

Twenty-four days, course days 69 to 92, weeks 14 to 19. Five base lessons treat collections of tens and operations on those units. Eight then connect tens and leftover ones to numerals and mental changes of ten; five establish comparisons; five explore flexible representations. The extra closing day holds original assessment work. Zero ones and teen/decade word confusions receive explicit attention. Mental ten-more/less follows models, and comparison symbols follow quantity reasoning. Subtraction remains multiples of ten from multiples of ten, including zero differences, with an explanation tied to a written method.

Day 69 retrieves unit 3 ten structure, including the kindergarten teen row explicitly used there. Day 82 retrieves kindergarten numeral comparison. There is no readiness or mid-unit assessment. Days 89 to 91 each provide a twenty-minute rotation for ten children. Each rotation has the same complete coverage: digit values and a/b/c cases, all three comparison symbols with reasons, mental ten-more/less, and positive/zero tens subtraction explained through a model and written method. Day 92 reuses those records. Fresh written traces are only brief comparison-symbol statements with reasons (1.NBT.B.3) and one recorded multiples-of-ten subtraction (1.NBT.C.6). It does not repeat place-value or mental-ten performances. Response is day 95 only, shared with the following course-level check. Collections come from the classroom; symbols use their quantity meaning rather than animal stories.

Candidate settled: keep the base-ten Progressions comparison about teen and decade words in planning, zero student days. Drop a three-digit extension. Reading and counting to 120 belongs in unit 6; three-digit place value belongs to grade 2.

## Unit 5. Adding within 100

Fifteen days, course days 96 to 110, weeks 20 to 22. Four base lessons combine like units without making a ten, four introduce a new ten with a one-digit addend, and six extend to two-digit pairs, explanations and application. A final original assessment closes the owning row. This short unit can build on secure tens and ones instead of reteaching them. Day 100 deliberately joins unit 3's make-ten model to unit 4's tens-and-ones method, then records the strategy in writing.

Day 96 retrieves the teen row explicitly used earlier this year and unit 4's place value; no readiness or mid-unit assessment is needed. Days 108 to 109 each reserve fifteen minutes for half the class's explained-method record. Day 110 reuses it and checks all of 1.NBT.C.4: two-digit plus one-digit, two-digit plus tens, and two-digit pairs, with and without a new ten, like units, models, written methods and reasoning. No standard algorithm is required. Response occupies days 111 to 112 centers. The optional food-drive context becomes a fictional class book collection, without asking for donations or discussing family giving or receiving.

Candidate settled: keep the base-ten addition comparison in planning, zero student days. Drop three two-digit addends so the short unit can complete two-addend composition and explanation without borrowing grade 2 work.

## Unit 6. Length to 120 units

Eighteen days, course days 111 to 128, weeks 23 to 26. Three base lessons establish direct and indirect comparisons, day 114 retrieves bounded arithmetic, six link equal iterated units to counting and recording through 120, and seven join length contexts to all story types, followed by the original closing assessment day. Day 114 adds within 100 and compares expressions within 20 for equality; it does not introduce general two-digit subtraction. The four owned rows have different loads: counting develops through measurement, while the final seven base lessons complete the story-type inventory begun in units 2 and 3. Day 118 counts a collection one by one before grouping tens; day 119 makes the new numerals and crossing 100 explicit. Rulers and a number line wait for grade 2.

Day 111 retrieves kindergarten measurable attributes. Day 118 retrieves the counting sequence, numerals to 20 and one-to-one counting. Earlier grade 1 story structures are retrieved on day 121. There is no readiness or mid-unit assessment. Days 122 to 125 redraw matched objects and cube comparisons as named, labelled tape diagrams, with a question mark for the unknown, then tie situation to solution equations. Every story quantity and answer remains within 20 even when a base measurement context uses larger measurements.

The twelve-cell inventory means three Add To cells, three Take From cells, three part-whole cells and three Compare cells. Each Compare cell also includes both more and fewer language, six variants altogether. Days 123 to 125 distribute these products, rather than demanding twelve full performances on day 128. Start-unknown and opposite-language comparisons are solved and discussed with support, without imposing grade 2 proficiency.

Days 125 to 126 each give two groups eight minutes apiece for ordering and indirect comparison: groups of 8 and 8 on day 125, then 8 and 6 on day 126. Each child leaves an ordered-strip drawing and indirect-comparison reason. Days 126 to 127 each provide fifteen minutes for 15 children's count/read evidence; independent written numerals and collection matching are retained on day 126. Day 127 provides four eight-minute measurement groups (8, 8, 8 and 6), retaining each child's drawing of identical units laid with no gaps or overlaps. Its 32 measurement minutes and 15 count/read minutes fit with a five-minute warm-up, three-minute launch and five-minute close in 60 minutes. Other students solve the lesson's stories independently; products are read after class. Day 128 closes from these once-collected records, the story inventory and short transfer evidence: all parts of 1.MD.A.1, 1.MD.A.2, 1.NBT.A.1 and 1.OA.A.1. Response is in days 129 to 130 centers. Classroom objects replace shoe removal and body comparisons; paper comparison cards replace the optional origami craft.

Candidate settled: keep the geometric-measurement Progressions comparison in planning, zero student days. Keep measuring the same object with two unit sizes in day 117's existing ten-minute comparison discussion, zero extra days. Both sets use internally equal units; explaining the count difference supports the current length concept without claiming the grade 2 standard.

## Unit 7. Geometry and time

Eighteen days, course days 129 to 146, weeks 26 to 30. Eight base lessons develop flat/solid attributes and composition, four develop equal shares, and five develop clocks, followed by the closing assessment day. Halves of a circle precede half past. Each base day retains fifteen minutes of major number work, and the shape investigations also use counting and comparison. Day 129 retrieves kindergarten naming and analysis; day 130 retrieves composition. There is no readiness or mid-unit assessment.

The end-of-unit assessment is distributed across the last arcs. Days 135 to 136 retain flat and solid composites reused as new units, plus distinguishing attributes and building/drawing a specified shape, completing 1.G.A.1 and 1.G.A.2. The portfolio includes rectangles, squares, trapezoids, triangles, half-circles, quarter-circles, cubes, rectangular prisms, cones and cylinders. Days 135 and 136 each reserve sixteen minutes for two eight-minute groups: 8 and 8 children, then 8 and 6. Every child leaves a specified-shape drawing with its defining attribute marked and evidence of non-defining changes and solid-composite reuse. Days 138 and 140 each reserve fifteen minutes for 15 children's partition and share-language explanations: circles and rectangles, two and four equal shares, half/fourth/quarter-of language and the whole as two halves or four fourths. After teaching the size relationship on day 139, retain every child's brief drawn same-whole comparison of halves and fourths in synthesis/exit-ticket time, as descriptive first-teaching evidence; the scored comparison part comes from S1 on day 146. This completes the final 1.G.A.3 part for the first 15 children as well as the second 15; day 140 reuses the product rather than asking again.

Days 143 to 145 reserve fifteen minutes each for one third of the class to read and write whole-hour and half-hour times in analog and digital forms, including the hour hand between numbers. Day 146 closes the complete four-code record, with the scored comparison part from S1 and every child's day 139 comparison as descriptive evidence, without another full performance. Its response is on days 149 to 150 only, shared with the year-end course-level check. Clock times concern school events rather than home routines; equal sharing uses paper rather than food.

Candidate settled: keep the geometry Progressions comparison in planning, zero student days. Drop a separate square-sharing extension: a square is already a rectangle, and contrasting valid circle/rectangle partitions and nonexamples in the existing equal-share work provides the needed depth.

## Unit 8. Putting it all together

Ten days, course days 151 to 160, weeks 31 to 32. This review unit owns no row and keeps all ten base lessons: three revisit facts and strategies, three revisit story structures, and four revisit collections and place-value riddles. Practice is selected from days 149 to 150's response record while preserving all three arcs. Day 156 deliberately reuses unit 6's labelled tape diagram. Retrieval is of explicit earlier grade 1 teaching; there is no readiness or mid-unit assessment.

Unit 8 has no separate assessment day. Its embedded closing observation is marked `observe` on day 160, with no day added and no base lesson removed. Day 157 is unrecorded counting practice. Days 158 to 159 retain the only new evidence: each child's MP.1/MP.3 riddle explanation and revision, fifteen minutes of existing core work each day, read after class. Day 160 closes from those products without another performance and lists no new numbered-code assessment. The handoff reuses day 148's counting and facts records and days 149 to 150 transfer evidence, without rescoring. The final ten minutes respond to riddle errors and update the grade 2 handoff. This closure observes mathematical practice without re-collecting counting or place-value evidence.

Candidate settled: keep the year's operations-and-base-ten thread comparison in planning, zero student days. Keep a two-clue riddle within day 160's existing writing/explanation time, zero extra days. It remains within 120 and supplies a reasoned clue rather than harder arithmetic.

## Course-level checks and the shared calendar

The grade 1 target row, rather than the calendar's general year-end example, sets math's target to weeks 19 and 30. The course-level checks stay after units 4 and 7, with their exact frame day costs. There are no additional course-level review days.

| Window | School/course days | Week | Coverage and response |
|---|---|---|---|
| Mid-year course-level check after unit 4 | 93 to 94 | 19 | Day 93 samples counting linked to both operations, unknown-addend meaning, equality and unknown positions through a new error-analysis portfolio of earlier-unit stories (1.OA.C.5, 1.OA.B.4, 1.OA.D.7, 1.OA.D.8); 1.OA.A.1 lists only the taught story subtypes as contributing evidence, completed in unit 6. Day 94 samples 1.OA.C.6 through a new incomplete-strategy explanation covering both operations and all named within-20 strategy families plus a separate independent mental-facts station. Unit 4's full record comes from days 89 to 92, with no rescore, new unit 4 performance or relisting of its codes. Day 95 responds once to both records. |
| Year-end course-level check after unit 7 | 147 to 148 | 30 | Day 147 samples 1.NBT.C.4, 1.OA.A.1, 1.MD.A.1 and 1.MD.A.2 through a new earlier-unit repair display with short prompts for their parts, plus the first half of the direct 1.OA.C.6 facts station. Day 148 finishes the station, uses brief strategy prompts for both operations and all within-20 strategy families, and samples 1.NBT.A.1 through a counting inventory: given start, read/write to 120 and numeral/collection matching. Unit 7's portfolio, with S1 on day 146 as the scored comparison part and the day 139 products as descriptive evidence, is reused without rescoring or relisting geometry/time codes. Days 149 to 150 respond; unit 8 supplies targeted review. |

Only newly sampled codes appear on a course-level check's CSV row. Complete unit-code evidence remains in its named end-of-unit record without another score. Short prompts or named products cover the taught parts; incomplete 1.OA.A.1 and 1.OA.C.6 samples before their owning units are explicitly labelled as contributions. An end day holds at most one extended task, with retained records and short items for its other parts.

No course-level check repeats a task form from the preceding ten school days. The mid-year error portfolio and incomplete explanation, and the year-end repair display and counting inventory, are reserved forms. The facts station is independent mental work with fresh facts, no supplied solution or objects, never a critique or timed sheet. Record just knows, quick strategy or counts all; planning minutes are not student speed thresholds. Day 94 budgets 30 children at ninety seconds, 45 minutes, alongside independent written work, with five minutes each for launch, close and transition. Year-end fluency is split across days 147 and 148: 15 children at ninety seconds, 22.5 minutes each day, one observation per child in the window. Day 148 also hears all 30 count/read at thirty seconds, fifteen minutes; written counting and strategy work runs alongside. Its 37.5-minute observation allocation leaves 22.5 minutes for launch, practice/transition and close. Facts and counting stay separate. Day 147 is part of this single window, not a repeated interview on day 148. Any equivalent individual evidence from the preceding ten days is reused with its source day named.

The grade 1 calendar puts social studies checks in weeks 14 and 31, science in weeks 15 and 29, ELA in weeks 16 and 32, and math in weeks 19 and 30. No week has two subjects' course-level checks. The nearest ELA/math check-block gaps are sixteen school days at mid-year (77 to 93) and ten at year-end (148 to 158), both beyond five. Actual math interview days are 94 and 148. No calendar tool or unit move is needed.

## Same-year leans checked against the calendar

Math's first lean is e1-key-details/SL.1.2 in ELA unit 1, school days 1 to 33. It is not safe to assume every part is completed by math day 17 merely because the unit has opened, so the day 17 bridge budgets five minutes and continues within story time if needed. Math's later RI.1.1 use on day 121 follows the whole ELA unit 1; its day still names the read-aloud question model for access.

No math row requires science first. For downstream users, math's data work on days 7 to 16 precedes social studies voting in unit 4 (school days 52 to 67), science light in unit 5 (79 to 99), and science daylight analysis in unit 8 (131 to 139). The science frame's approximate week 31 daylight note is stale; the current calendar places its analysis in weeks 27 to 28, still after math. Its fall record does not require the completed data analysis in advance.

Science leaf ordering in unit 3 (school days 45 to 56) precedes math length on day 111. Its frame's direct-ordering bridge, leaves beside each other with aligned endpoints and no units, remains necessary. Science signaling in unit 6 (101 to 116) starts before math's equal-unit work on day 115; science teaches its own end-to-end, no-gaps paper-strip or heel-to-toe bridge. Math days 111 and 115 record these timing relationships, with no added math days. Social studies unit 8 (131 to 151) follows math comparison and the completed story-type work ending on day 128. Its prices remain made-up whole dollars within 20, with no coin or decimal teaching imported into math.

## Shorter path

For a shorter period, plan a 55-minute lesson, or a 45-minute core plus a separate 15-minute number/practice block. A 45-minute-only day cannot promise the evidence and explanation budgets for 30 children; it needs a timetable decision before adoption. An ordinary 55-minute lesson keeps a five-minute mixed warm-up, five-minute hook/model connection, 25-minute core, fifteen-minute practice/response and five-minute synthesis/evidence, trimming repeated rounds. Observation days transfer five minutes of already-taught partner practice into the adjoining lesson's practice slot, without shortening an interview or omitting a child. Day 127 needs its full 60 minutes and uses the 45 plus 15 arrangement. Day 94's 45-minute station fits beside independent written work in 55 minutes with a five-minute launch and close. Unit 7 keeps all fifteen number-work minutes in the separate block where its core is 45 minutes. Unit plans must test these stated budgets; a 45-minute-only timetable is not promised.

For a year ten meetings short, fold only these ten unassessed practice days into the named neighbor's existing practice slot:

| Fold-in day | Neighbor | Work preserved inside that neighbor | Minutes saved |
|---|---|---|---:|
| 6 | 5 | Mixed within-10 counting-on game | 60 |
| 10 | 9 | Mixed counting-on facts after representing survey data | 60 |
| 21 | 20 | Joining/taking-away story practice | 60 |
| 26 | 25 | Missing-part fact practice | 60 |
| 32 | 31 | Comparison and related-fact practice | 60 |
| 46 | 45 | Mixed within-10 facts | 60 |
| 60 | 59 | Three-addend make-ten practice in the existing strategy discussion | 60 |
| 73 | 72 | Mixed operations on tens and within-20 facts | 60 |
| 81 | 80 | Mental ten-more/less and a short tens-and-ones retrieval | 60 |
| 99 | 98 | No-new-ten addition practice | 60 |

The ten folds save 600 minutes on the 60-minute timetable: 160 meetings (9,600 scheduled minutes) become 150 meetings (9,000 scheduled minutes), retaining one short round of each folded activity in its neighbor. None carries an assessment, a first prerequisite retrieval, an observation allocation, an end-of-unit response slot or a unique owned part. Keep one short round of each folded practice and reduce its repetitions. These are implementation folds, not deletions from the canonical 160-row map or changes to frame ownership. To preserve the shared check weeks, retain the named school-day positions and use those ten released positions as non-meeting days; do not renumber every subsequent lesson and bring checks forward. If a school has only 150 consecutive school days rather than ten missing math meetings within a 160-position calendar, its compressed cross-subject check calendar needs lead approval; this sequence does not claim the original weeks still apply.

## For the lead

None open within this sequence. The frame now matches the ten-day review unit and embedded closure, kindergarten teaching is verified, course-level checks reuse recent records and all minute budgets plan for 30 students. Unit plans must preserve the named models, full-code products, minutes and response allocations. No extra day, ownership change or unit move is proposed.

All eight Candidate comparison cells and their extensions are settled above. Planning comparisons cost zero student days; kept student extensions fit named existing time. No assessment items, answer keys, section plans or lessons have been written.

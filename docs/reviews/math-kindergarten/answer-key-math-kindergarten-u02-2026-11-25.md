# Answer-key read: kindergarten math, unit 2

Job 021, kit 14. Requested report date: 2026-11-25. Work performed: 2026-11-26. Scope: days 19 to 44, unit 2 only.

## Verdict

Fail as a fully cold answer-key read: my initial extraction exposed samples, and I then opened a unit plan containing keys before recording every solution. The subsequent content verification covered all 103 in-scope items and 108 wrong-answer rows, and five content faults were fixed, but a fresh reader still needs to repeat the required blind pass.

## What I studied

- `docs/pipeline/briefs/sensitivity-read.md`, sections 1 to 3 for answer-key: solve and record before comparing, check goal and standard, disclose my own errors.
- `docs/courses/math-kindergarten/DEFAULTS.md`: a 60-minute class day; spoken stems and picture or paper responses; 18 point print; 60-word student-page cap; one marking scale; six rotating observations. The root `DEFAULTS.md` does not exist; I used this course file.
- `docs/pipeline/briefs/section-write.md`, rules 7 to 10: one spoken ask, counted turns, shown/shown with help/not yet seen, one actor per scene.
- `data/plans/math-kindergarten/items.csv`, filtered to exits, readiness and end items on days 19 to 44: 25 exits, no readiness rows, 78 end rows. The 78 comprise 30 cohort conference rows, 15 numeral/picture-route rows, three one-more rows, nine group-comparison rows, three written-comparison rows, six reason rows, five category rows and seven retained-record judgments.
- Each needed exit master and end-task master in `courses/math-kindergarten/u02-1/` through `u02-7/`: I recounted the original SVG objects, separated mat exemplars from loose pieces, inspected group positions and numeral print, and worked each response. The seven `teacher-key.md` filenames were inventoried before deliberately opening them. The initial extraction mistake means this was not an uncontaminated cold solve.
- `_scratch/l87/tmp/math-kindergarten-key-u2/cold-solutions.json`: 103 individually identified answers and methods, recorded before the deliberate key comparison. These are verification answers, subject to the exposure limitation above.
- The unit 2 section plans, field 3; the unit plan; filtered `days.csv` goals/codes; all 108 corresponding `wrongs.csv` rows; unit 2 teaching pictures, practice records, day preparation notes and assessment directions: these supplied the comparison, goal, safety and rule 4 checks.
- Filtered lower-grade ledger calls: `python -X utf8 scripts/ledger.py show math --before math-kindergarten --term "<word>"`, using paper clip, bear, crayon, peg, tab and shape. No lower-grade case rows were returned. The helper suppressed the current course's entries, which the command also emits; kindergarten has no earlier math grade in this run.

## Faults and fixes

Numbered by significance. Counts use one primary kind per item: key 3, ambiguous 1, off-goal 1, rule4 0, needs-info 0, two-asks 0, key-on-child-page 0. All five listed content faults are fixed.

| # | Item | Kind | What was wrong | Exact fix | Stage that made it |
|---|---|---|---|---|---|
| 1 | s02-X22 | ambiguous | "Mark the crayon that cannot have a partner." Any of the seven can be the extra. Optional matching also allowed a guessed mark to pass without showing the day's matching. | Stem is now "Join crayons across the rows, one partner each." Require six unique cross-row links, leaving any one lower crayon unmatched. The existing K wrong row remains valid. Updated the exit master and private key. | section plan |
| 2 | s02-X27 | off-goal | Field 3 explicitly specified "Three unframed picture pairs" although day 27's goal identifies comparisons on 5-frames. The original exit offered no frames. | Replaced only the exit illustration with six filled joined-five-cell frames. Kept the cases 6/8 pencils, 9/9 pegs, 10/7 flags; retained the stem, ID, day, code and correct nine-partner response. Updated steps and the B wrong to the observed claim that equal frame size means equal quantity; synchronized the private key. | section plan |
| 3 | s02-X38 | key | "Show which number is greater" asks for a choice, but "8 indicated with quantity or counting-order evidence" makes an additional explanation compulsory. | Accept an unambiguous indication of 8. Drawing or reasoning is optional; no extra exit question. O38 retains the separately funded reason on another case. Updated answer, steps, samples and private key. | section plan |
| 4 | s02-X34 | key | "Label this empty bowl" permits a written 0, but the key required "The 0 card attached and outlined." A correct written label could fail for its method. | Accept a recognizable written 0 or the 0 card placed beside the bowl. Outlining is an optional recording method; formation support is recorded separately. Updated answer, steps, samples and private key. | section plan |
| 5 | s02-X37 | key | "Make the next tower" and the blank space permit drawing the six-square successor, but the key required exactly one supplied square attached and six squares outlined. | Accept either adding one to the five-square original or drawing its six-square successor. No numeral or additional oral ask. Do not infer a without-recounting strategy from the paper alone. Updated answer, steps, samples and private key. | section plan |

No item was added, moved, recoded or split. All existing IDs and day assignments remain. Only five item rows and one wrong row changed. No handback write was needed: the revised asks each produce one response on their existing day and repair route. All other wrong rows retain their observed-action conditions; a wrong mark alone does not establish a misconception letter.

## Answers after the fixes

I extracted only the changed stems and stimuli, answered all five again without reopening their keys, and recorded the work in `_scratch/l87/tmp/math-kindergarten-key-u2/second-solutions.json`. This checks the repairs but cannot undo the earlier exposure.

| Item | Re-solution and method |
|---|---|
| s02-X22 | Six upper crayons can each join a different lower crayon. Exactly one lower crayon remains; any of the seven can be left. The response is six one-to-one links, with no second ask. |
| s02-X27 | Frame pairs recount to 6/8, 9/9 and 10/7. Only the middle peg pair is equal: nine partners and no extras. The filled five-cell rows now supply the model in the day goal. |
| s02-X34 | The bowl has no contents. Label 0, either written in its label space or chosen from the numeral cards. Outlining a card does not change the mathematical answer. |
| s02-X37 | The starting tower has five equal units. Its next tower has six, exactly one more. Drawing six in the blank area or adding one to the original both show the same successor. |
| s02-X38 | The displayed numerals are 2 and 8. Choose 8, since an eight-object group has more than a two-object group. The single stem asks for the choice, so a clear point or mark suffices. |

## Section-plan field 3 lines for the data writer

I left section plans unchanged, as required. These lines now differ from the authoritative data or revised master:

| File and field 3 entry | Stale wording or requirement | Needed synchronization |
|---|---|---|
| `docs/courses/math-kindergarten/u02-2.md`, E21 | "Match each drum to one whistle"; key only three links and wrong K. | Existing data says "Show with matching which pile has more"; key includes indicating whistles, wrong N for a picture-size claim. This discrepancy predates my fixes. |
| `docs/courses/math-kindergarten/u02-2.md`, E22 | "Mark the crayon that cannot have a partner"; links optional. | Use the new single matching stem and require six unique links. |
| `docs/courses/math-kindergarten/u02-3.md`, E27 | "Three unframed picture pairs" with spacing-based sample wrong. | Describe the filled joined-five-cell frame pairs, unchanged counts and nine peg links; update the B sample to equal frame size mistaken for equal count. |
| `docs/courses/math-kindergarten/u02-5.md`, E34 | "0 card attached and outlined on paper." | Accept written 0 or selected 0 beside the empty bowl; outlining is optional. |
| `docs/courses/math-kindergarten/u02-6.md`, E37 | "six squares after attaching/ outlining the one new piece." | Include a drawn six-square successor as another valid construction. |
| `docs/courses/math-kindergarten/u02-6.md`, E38 | "8 marked with two/eight drawn quantities or other quantity evidence." | An indication of 8 suffices; quantity evidence is optional and O38 separately records a reason. |

Related field 3 scoring wording also needs clarity: E23 says no confirmation question, while the item steps mention confirmation of intent; the familiar finish mark supplies that evidence without a second ask. E24's field 3 phrase "and a heard quantity-based reason" must not impose a follow-up on the paper exit; the exit key accepts a paper explanation, and O24 is the distinct heard check. I treated those existing separate O checks and finish-mark routines as the governing interpretation, rather than adding child tasks or changing their collection budget.

## Rule 4, goal coverage and child access

- Teaching/practice cases use the square pictures, partial records, supplied diagrams and repair tasks. Reserved exits use their own clip, bear, drum/whistle, crayon, stamp, paint, leaf, bead, peg, flower, order, tower and sorting cases. End cases use the separate seven-tab conference, mixed numeral boxes, 9-to-10 completion, 2/3 and 4/4 comparisons, bare 4/8, 9/6 and 3/3 pairs, and 2/4/6 shape sort. I found no taught complete case or completed answer picture reused in an exit or end item.
- The section plans explicitly reserve complete cases and response formats rather than every integer. M3 necessarily contains every integer from 0 to 10. Repeated integers or a common five-cell model alone are not proof of a repeated case. I compared case identity, number combinations, arrangement and response format; I did not replace foundational numbers merely because practice also uses them.
- The repeated conference rows address different five-child cohorts, not repeated practice for the same child. M1 reuses its counted set to test invariance within the assessment. Day 44 rows judge retained work and are not new child questions. These are deliberate evidence continuations, not taught-case reuse.
- Each revised item stays on its original goal. The partial exit components do not by themselves establish every part of a broad standard: the separate numeral, oral, counting, order and retained-record components remain necessary. For example X30 recognizes the numeral, while M3 supplies actual independent numeral writing; X41 classifies, while F4 supplies classification, category counts and category order.
- All 103 rows are teacher judged. Longest child-task stem is 12 words; all are one decision or one product, including a conditional greater/equal choice. Blank masters inspected remain below the course's 60-word cap, with teacher read-aloud directions. There is no separate individual-stem word limit in the course DEFAULTS file. The seven day 44 labels are teacher record headings, not seven new spoken tasks.
- Conference budget: five prompts at 45 seconds plus 15 seconds notes is four minutes per child; five children is 20 minutes per day. The F2/F3 reason turn has two separately recorded 45-second prompts plus 30 seconds notes, two minutes per child; ten children is 20 minutes. Rotating six at 45 seconds uses 4.5 minutes plus the named launch/collection allowance. The repairs add no turns. Actual classroom speed remains untested.
- I found no assessment key on a child-held blank piece. Private keys are already named in each day's Before class and explicitly kept off child pages/displays. Printed practice claims are supplied material to critique, not exit answers. Pictures with order numerals provide the requested count, not a completed response. No key had to be moved.

## Facts, sources and safety

`sources.csv` row `s02-original` identifies these original drawings and invented quantities, with no claim about real species, people, places, events, prices or measured quantities. No item relies on an external real-world fact requiring a checked web page. I therefore opened no external factual page and made no sources.csv write. Existing base-text source rows concern lesson adaptation, not evidence for invented item quantities; their existing checked dates are not claimed as my verification.

Checked directly: every represented count, unequal/equal comparison, empty-set label, one-more result, numeral choice, grouping membership and ascending category order used above. I used the SVG object instances and positions, excluding category exemplar icons from item collections. In particular, the mitten/sock mat icons do not change the loose-piece counts 4/7, and the shape mat icons do not change the 2/4/6 loose-card counts. The revised day 27 frames were parsed independently: 6/8, 9/9, 10/7, 60 cells total, with the original 49 object pictures.

Safety judged from the authored preparation: large adult-cut paper, damaged pieces inspected, pieces kept out of mouths, no real food or metal clips, optional fingers. No item depends on handling an actual mushroom, pepper, paper clip or another small real object. I did not test a classroom, printing at actual size, individual motor access, or live turn speed. Those are judgments from the directions, not observations of children.

Browser check: none.

## My errors and limits

1. I excluded a singular `sample` field in my first extraction but failed to exclude the real `samples` field and key-bearing `steps`. Some answers were exposed before my solutions were recorded. I also opened `s02.md`, which prints keys, before completing the record. This breaks the requested cold-solve order and cannot be repaired by calling the subsequent calculations cold. A fresh reader must repeat that part.
2. I initially suspected the three F3 reason keys allowed only the example "Nine comes later than six." On reading the complete steps, all explicitly accept any valid quantity/count-order reason. I withdrew that suspicion and did not change those rows.
3. My initial retained-M2 verification answer included the picture-route evidence. The actual A44-M2 row deliberately judges count-out only; picture-route rows remain in their own retained records. I narrowed that interpretation and left the correct aggregate row unchanged. No arithmetic error was found in my recounts.
4. The first gate attempt used this environment's Python executable-directory value and could not start subprocesses. The next attempts exposed missing `markdown`, then `pypdf`. I loaded official package wheels only into the allowed scratch folder and used the installed executable with a corrected `sys.executable` for the gate. I changed no shared script or system installation.

## Gate and scope verification

Before course edits, the working gate stored `build/gates/base-math-kindergarten` and returned 0, with 302 existing failing lines. The earlier crashed attempts stored no baseline. The successful invocation used the same course gate through `runpy`, with the installed Python executable and `PYTHONPATH` pointing to the scratch dependency directory.

After fixes, the same course gate returned 0: **0 new failing findings, 6 new note lines**. The existing failure count stayed 302. The gate noted that the repository revision changed during this run; comparison still found no new failing line. The six new lines were:

```text
note courses/math-kindergarten/u02-2/exit-22.md: blank, 15 words, student page page count not checked (Chrome wrote nothing), 0 failure(s)
note courses/math-kindergarten/u02-2/teacher-key.md: story, 432 words, 0 failure(s)
note courses/math-kindergarten/u02-3/exit-27.md: blank, 18 words, student page page count not checked (Chrome wrote nothing), 0 failure(s)
note courses/math-kindergarten/u02-3/teacher-key.md: story, 427 words, 0 failure(s)
note courses/math-kindergarten/u02-5/teacher-key.md: story, 1104 words, 0 failure(s)
note courses/math-kindergarten/u02-6/teacher-key.md: story, 1190 words, 0 failure(s)
```

The two revised exit masters therefore lack a completed automatic page-count check in this run. Their SVGs retain the 700 by 330 viewBox, and the revised frame illustration was checked structurally, but I do not claim verified printed fit. No separate build was run.

Additional verification confirmed that each changed answer and sample matches its private teacher-key block, each revised stem matches its exit master, the revised frame SVG parses correctly, and the report contains all 103 item answers plus five re-solutions.

The row snapshot comparison confirms exactly five changed items and the one X27 wrong row, with no added/deleted rows and no other course rows altered. Shared-piece edits are `u02-2/exit-22.md`, `u02-3/exit-27.md`, and the affected blocks of `u02-2/teacher-key.md`, `u02-3/teacher-key.md`, `u02-5/teacher-key.md` and `u02-6/teacher-key.md`. Helper scripts, verification records and dependencies remain under the assigned scratch folder. No stray empty folder was observed.

## Could not settle

The required unexposed fresh-reader pass remains outstanding because of my review-order error. Section-plan synchronization belongs to the data writer and is listed above. Existing course gate failures remain outside this job's allowed edits; the final gate reported no added failing findings. No curriculum-scope, money, people or audience decision was made.

## Item-by-item verification answers

These are the recorded independent calculations and methods, with the cold-read limitation disclosed above. The five revised answers appear separately in the re-solution table. The retained M2 row is count-out only, as corrected in My errors.

| Item | My answer and method |
|---|---|
| s02-X19 | Seven separate clip marks; make one mark for each requested object. |
| s02-X20 | Move all five bears farther apart; still five because none enter or leave. |
| s02-X21 | Whistles: ten versus three; pair three and leave seven whistles unmatched. |
| s02-X22 | Any one of the seven lower-row crayons after six unique cross-row pairs; no specific crayon is uniquely unmatchable. |
| s02-X23 | Any intentional collection of zero to five marks; compare its count with six stamps. |
| s02-X24 | Nine brushes have more than six pots; six unique pairs leave three brushes. |
| s02-X25 | Eight leaves; visit every leaf once along the open curve. |
| s02-X26 | The two rows have five beads each; five unique cross-row matches, no extras. |
| s02-X27 | Middle peg pair: nine on each side; draw nine one-to-one links. |
| s02-X28 | Stars: nine versus six buttons; frames show five plus four versus five plus one. |
| s02-X29 | Any countable collection above three flowers; four is a sufficient example. |
| s02-X30 | 6; count six button pictures and find its numeral. |
| s02-X31 | Four disk marks in a different arrangement; count preserved. |
| s02-X32 | Select eight of ten button pieces and stop. |
| s02-X33 | No marks in the zero-order panel; finish mark indicates intentional completion. |
| s02-X34 | 0 for the empty bowl; no objects means zero. |
| s02-X35 | Select six of ten tickets and stop. |
| s02-X36 | Order four-, five-, six-square towers; each successor has one extra square. |
| s02-X37 | Make a six-square tower, one more than the five-square starting tower. |
| s02-X38 | 8 is greater than 2; an eight-object representation has six unmatched extras. |
| s02-X39 | Draw six and eight marks for the two numeral orders; eight has more. |
| s02-X40 | 10 is greater than 2 despite the larger print of 2. |
| s02-X41 | Sort four loose mittens and seven loose socks; mat icons are exemplars, not pieces. |
| s02-X42 | Sort six short cards and four long cards; ignore stripes. |
| s02-X43 | Select exactly three mushrooms from ten available and put them on the pizza. |
| s02-M1a-34 | Say one through seven, touching each of the seven tabs once; changing the starting end preserves seven. |
| s02-M1b-34 | Seven; the last count word names the whole set, and spreading changes no membership. |
| s02-M1c-34 | Seven; the last count word names the whole set, and spreading changes no membership. |
| s02-M1d-34 | Say one through seven, touching each of the seven tabs once; changing the starting end preserves seven. |
| s02-M2a-34 | Move seven tabs from ten and stop; count each moved tab once. |
| s02-M1a-35 | Say one through seven, touching each of the seven tabs once; changing the starting end preserves seven. |
| s02-M1b-35 | Seven; the last count word names the whole set, and spreading changes no membership. |
| s02-M1c-35 | Seven; the last count word names the whole set, and spreading changes no membership. |
| s02-M1d-35 | Say one through seven, touching each of the seven tabs once; changing the starting end preserves seven. |
| s02-M2a-35 | Move seven tabs from ten and stop; count each moved tab once. |
| s02-M1a-36 | Say one through seven, touching each of the seven tabs once; changing the starting end preserves seven. |
| s02-M1b-36 | Seven; the last count word names the whole set, and spreading changes no membership. |
| s02-M1c-36 | Seven; the last count word names the whole set, and spreading changes no membership. |
| s02-M1d-36 | Say one through seven, touching each of the seven tabs once; changing the starting end preserves seven. |
| s02-M2a-36 | Move seven tabs from ten and stop; count each moved tab once. |
| s02-M1a-37 | Say one through seven, touching each of the seven tabs once; changing the starting end preserves seven. |
| s02-M1b-37 | Seven; the last count word names the whole set, and spreading changes no membership. |
| s02-M1c-37 | Seven; the last count word names the whole set, and spreading changes no membership. |
| s02-M1d-37 | Say one through seven, touching each of the seven tabs once; changing the starting end preserves seven. |
| s02-M2a-37 | Move seven tabs from ten and stop; count each moved tab once. |
| s02-M1a-38 | Say one through seven, touching each of the seven tabs once; changing the starting end preserves seven. |
| s02-M1b-38 | Seven; the last count word names the whole set, and spreading changes no membership. |
| s02-M1c-38 | Seven; the last count word names the whole set, and spreading changes no membership. |
| s02-M1d-38 | Say one through seven, touching each of the seven tabs once; changing the starting end preserves seven. |
| s02-M2a-38 | Move seven tabs from ten and stop; count each moved tab once. |
| s02-M1a-39 | Say one through seven, touching each of the seven tabs once; changing the starting end preserves seven. |
| s02-M1b-39 | Seven; the last count word names the whole set, and spreading changes no membership. |
| s02-M1c-39 | Seven; the last count word names the whole set, and spreading changes no membership. |
| s02-M1d-39 | Say one through seven, touching each of the seven tabs once; changing the starting end preserves seven. |
| s02-M2a-39 | Move seven tabs from ten and stop; count each moved tab once. |
| s02-M3-1 | 6; count objects in this numbered box, using zero for the empty one. |
| s02-M2p-1 | 6 stars, each marked exactly once; track every picture without omissions or repeat visits. |
| s02-M3-2 | 0; count objects in this numbered box, using zero for the empty one. |
| s02-M3-3 | 8; count objects in this numbered box, using zero for the empty one. |
| s02-M2p-3 | 8 stars, each marked exactly once; track every picture without omissions or repeat visits. |
| s02-M3-4 | 3; count objects in this numbered box, using zero for the empty one. |
| s02-M3-5 | 10; count objects in this numbered box, using zero for the empty one. |
| s02-M2p-5 | 10 stars, each marked exactly once; track every picture without omissions or repeat visits. |
| s02-M3-6 | 1; count objects in this numbered box, using zero for the empty one. |
| s02-M3-7 | 9; count objects in this numbered box, using zero for the empty one. |
| s02-M2p-7 | 9 stars, each marked exactly once; track every picture without omissions or repeat visits. |
| s02-M3-8 | 4; count objects in this numbered box, using zero for the empty one. |
| s02-M3-9 | 2; count objects in this numbered box, using zero for the empty one. |
| s02-M3-10 | 7; count objects in this numbered box, using zero for the empty one. |
| s02-M3-11 | 5; count objects in this numbered box, using zero for the empty one. |
| s02-F1a | Circle the completely filled upper row of five cells. |
| s02-F1b | Mark the empty fifth cell of the lower row; it is the only available place after nine tabs. |
| s02-F1c | 10; nine already present plus one extra fills ten cells. |
| s02-F2um | Two unique cross-group links, leaving one of three tabs unmatched. |
| s02-F2uleft | 2; count the left tabs. |
| s02-F2uright | 3; count the right tabs. |
| s02-F2umore | Right group of three; one extra remains after matching. |
| s02-F2ufewer | Left group of two; it has no partner for the third right tab. |
| s02-F2em | Four unique cross-group links, no unmatched tabs. |
| s02-F2eleft | 4; count each group separately. |
| s02-F2eright | 4; count each group separately. |
| s02-F2esame | Ring both four-tab groups; every tab has one partner. |
| s02-F3-1 | 8, greater than 4 regardless of glyph size. |
| s02-F3-2 | 9, greater than 6 by quantity or counting order. |
| s02-F3-3 | Both 3 numerals; equal quantities. |
| s02-F2reason-40 | Two on the left and three on the right, so three is more; four and four are equal. A counted or matched quantity reason is needed. |
| s02-F3reason-40 | Choose one: eight is more than four, nine more than six, or three equals three; justify using quantity or counting order. |
| s02-F2reason-41 | Two on the left and three on the right, so three is more; four and four are equal. A counted or matched quantity reason is needed. |
| s02-F3reason-41 | Choose one: eight is more than four, nine more than six, or three equals three; justify using quantity or counting order. |
| s02-F2reason-42 | Two on the left and three on the right, so three is more; four and four are equal. A counted or matched quantity reason is needed. |
| s02-F3reason-42 | Choose one: eight is more than four, nine more than six, or three equals three; justify using quantity or counting order. |
| s02-F4a | Separate the twelve loose shape cards into two circles, four squares and six triangles; mat icons are exemplars. |
| s02-F4-circle | 2 circles; count the corresponding sorted pieces. |
| s02-F4-square | 4 squares; count the corresponding sorted pieces. |
| s02-F4-triangle | 6 triangles; count the corresponding sorted pieces. |
| s02-F4order | Circle mat, square mat, triangle mat; counts increase 2, 4, 6. |
| s02-A44-M1 | Retained count record: seven through original count, total, spread and reverse-start count. |
| s02-A44-M2 | Retained count-out: seven tabs moved from ten, then stop. Picture-route evidence is held separately. |
| s02-A44-M3 | Retained numeral boxes: 6, 0, 8, 3, 10, 1, 9, 4, 2, 7, 5. |
| s02-A44-F1 | Retained full-five circle, tenth-cell mark, new total 10; strategy needs an observation, not inferred from the numeral. |
| s02-A44-F2 | Retained 2/3 matching, counts, more/fewer and 4/4 equality, plus recorded quantity reason. |
| s02-A44-F3 | Retained choices 8, 9, both threes, plus a recorded reason. |
| s02-A44-F4 | Retained category membership 2 circles/4 squares/6 triangles, counts 2/4/6, ascending mat order. |

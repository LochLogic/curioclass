# Judge report: pilot, grade 4 math (13 tools)

Judge pass for the catalog review pilot (docs/agents/CATALOG-REVIEW.md, step 3), 2026-11-10. Read: the review plan, the
extract brief, the adoption bar (Math), BASELINE rules 1, 2, 4 and 20, the tables, the 13 rows, and all 13 specs (four
in full before looking at their rows). Read and report only. Nothing else was changed.

## Headlines

1. No standard is uncovered and no two tools clash. The problems are depth, not gaps or duplicates.
2. "Taught" in the table hides a lot. Counting by the parts of each standard's wording, about 12 of 28 standards have
   a part the default path never asks for, or a key step the tool does for the child.
3. The thinnest tools sit on the major work. recipe-scaler carries 7 codes in 12 rounds; growth-spurt has 2 multistep
   problems for 4.OA.3. The two built tools (both off the major work) are far deeper and far better closed.
4. Fluency is not a tool gap. A live generator and planned sheets cover it. The gap is that no plan yet schedules it.
5. The extract rows are honest on depth labels but the row format throws the useful signal away. Fix the format
   before the full run.

## A. Cold re-read of four rows

Tools: growth-spurt, area-model-builder, money-and-meters, and recipe-scaler (my pick: most codes in one tool).
I filled depths, kinds, paper_version and beatable from the spec first, then opened the row.

| Tool | Where I differ | Who is right |
|---|---|---|
| growth-spurt | Depths agree (3 taught). I put fluency 0, row says 1. I found one more beatable check: Tray jobs is three fixed answers (9, 8, 2) matched to three questions, so the last falls out by elimination. The row put "4.OA.2 has no division cases" under `unsure`, where no table counts it. | Row is right on depth by the brief's test. I am right on fluency and the tray hole. The missing division slice is real and was filed in the wrong field. |
| area-model-builder | Depths agree. Row caught both real holes (tiny chunks; snapped cuts need no decision). I add: the spec never shows a four-digit dividend or a divisor other than 4, and "Two slicings" has no check. Fluency 1 in the row, 0 to 1 for me. | Row is good. My adds are small. |
| money-and-meters | 4.NF.5: row says taught, I say touched. The child lays 3 dimes and 4 pennies; the tool does the trade to 30 hundredths. The step the standard names (rewrite 3/10 as 30/100) is never done by the child. 4.NF.6: the child never writes a decimal; the tool prints it under each panel. Only placing is asked, and the row itself lists placing as beatable. The row also missed that the proof panel in Compare is no test: all four panels show the same truth, so any pick passes. | I am right on all three. This is the row's weakest. |
| recipe-scaler | 4.NF.3d practiced: agree. 4.NF.3b: row says taught; with one-size scoops the spec never says how a child makes 1/8 + 2/8, so I say unsure, likely touched. Beatable: row found 1, I found 4 (each cup shows its amount in numbers, so tap until it matches the card; the tool regroups the fourths; "tap plus to add a batch" lets the tool do the multiplying; two guessable questions). The row did not flag that 7 codes share 12 rounds. | I am right on 3b and the holes. The row was generous here. |

Score: 13 of 15 depth labels match mine (misses: 4.NF.5, 4.NF.3b). One more miss turned up in part B outside the
sample: fraction-wall-duel 4.NF.1 is taught only through steals, which a child can go a whole game without playing.

**Verdict.** The rows cannot be used as they are for coverage. The cheaper model applied the depth test as written and
mostly got it right; the test is too coarse. Four fields carried no signal in this batch: `paper_version` (partial on
12 of 13), `minutes` (25 on 11 of 13, the spec template's midpoint), fluency (1 as a floor on 9 of 13, which is where
most of the 23 percent comes from), and "Depth" in the value table (taught on all 13). The real findings sat in
`unsure` and `beatable`, which the coverage table does not read.

**Wording changes for CATALOG-EXTRACT.md**

1. Add `parts_missing` to each code: "Read the standard's own wording (it is quoted in Who and how). List each part
   of it the default path never asks the student to do: an operation, a number size, a unit kind, a form such as
   symbols or a number line. Empty only if every part is asked." The script then shows taught in full or taught in part.
2. Add a second depth test: "Who does the key step, the student or the tool? If the tool snaps, trades, regroups,
   labels or computes it and the student only watches or confirms, the depth is `shown`, not `taught`." Add `shown`
   between practiced and touched.
3. Add `items` to each code: the number of checked items on the default path for that code, from the spec's counts.
4. Add a consistency rule: "If a `beatable` entry defeats the only check for a code, that code cannot be `taught`.
   If the activity sits behind a choice the student may never make (an optional move, an extra mode), it is `touched`."
5. Replace `paper_version` with `paper_gap`: "Name the one thing the student does here that a printed sheet cannot
   ask for, or write none." Three levels with no anchors gave partial every time.
6. Kinds: "0 is the default. Give 1 only when at least one checked round is that kind. Fluency needs repeated,
   varied items of one procedure, not one worked pass."
7. Drop `minutes` (the template sets it) or keep it only for built tools. `items` does its job.
8. A thing missing from the standard goes in `parts_missing`, never in `unsure`.

Built tools (egg-carton-factory, skate-park-angles) have long, exact specs and their rows were sound. The misses are
all on new-format specs, where one line can stand for a whole activity.

## B. Against the adoption bar, standard by standard

"Full" means every part of the standard's wording is asked of the child on the default path. Major work is marked M.

| Standard | Tool | Verdict | What is missing or weak |
|---|---|---|---|
| 4.OA.1 M | growth-spurt | Nearly full | Reading one equation both ways (35 is 5 times 7 and 7 times 5) is not asked. Whether the written equations are checked is not said. |
| 4.OA.2 M | growth-spurt | Part | All eight problems are multiply or add. No division cases: "how many times as tall" and "the smaller amount is unknown". The standard says multiply or divide. |
| 4.OA.3 M | growth-spurt | Part | Remainders are done well but in one-step problems with one number set (50 and 6). Only two multistep orders on the default path, both multiply then add. No subtraction or division step. The estimate is not checked. |
| 4.OA.4 | egg-carton-factory | Full | Built. All four parts have their own closed checks. |
| 4.OA.5 | rule-machine | Full | Generate, notice, explain are all asked. The 10th-shape prediction has no check; the shape tapes get one example in the spec. |
| 4.NBT.1 M | stadium-count | Touched | The zoom is watched, never answered. No item asks "how many times the value". See below. |
| 4.NBT.2 M | stadium-count | Full | Three forms and digit-by-digit compare. Typing number names is a spelling load; word tiles would be kinder. |
| 4.NBT.3 M | stadium-count | Part | Six headlines, thousands and ten thousands only. "Any place" also means tens, hundreds, hundred thousands. |
| 4.NBT.4 M | road-trip-logbook | Part | Ten problems, three- and four-digit numbers only (the standard runs to a million). Carry chips appear on their own, so the tool makes the regrouping call. Good for seeing why; not fluency. See Balance. |
| 4.NBT.5 M | area-model-builder | Full | Four of each kind. The cut needs no decision (lines snap), but the partial products and the sum are the child's. |
| 4.NBT.6 M | area-model-builder | Nearly full | Remainders are in (3 of 6). The spec shows only three-digit dividends and the divisor 4. Who works out "uses 800" is not said. |
| 4.NF.1 M | fraction-wall-duel | At risk | Taught only by steals, and a steal is the child's choice. A child can finish all three decks without one. Making an equivalent fraction (not just spotting one in hand) is not asked. |
| 4.NF.2 M | fraction-wall-duel | Nearly full | Three reasons and the same-whole trap are strong. The result is never recorded with >, = or <. Reasons can be cycled (three buttons, no cost). |
| 4.NF.3 M | recipe-scaler | Part | a: fine. b: no stated way to split another way with one-size scoops. c: two worked amounts, fourths only, and the tool regroups. d: one line ("kitchen word problems follow"). About six rounds for four sub-parts. |
| 4.NF.4 M | recipe-scaler | Part | a and b are shown well, but the plus button and the pile do the multiplying. c is two questions. Four rounds for three sub-parts. |
| 4.NF.5 M | money-and-meters | Shown | The tool does the rename. Four rounds. No sum past one whole. |
| 4.NF.6 M | money-and-meters | Part | Placing only, and the linked panels give the answer away. Writing a decimal for a fraction is never asked. |
| 4.NF.7 M | money-and-meters | Full | Strongest part of the tool. The proof-panel pick tests nothing. |
| 4.MD.1 | unit-ladder | Full | Every unit pair the standard lists, tables, skip rows. A sense of size (about how long is a kilometer) is not built. |
| 4.MD.2 | unit-ladder | Breadth yes, depth no | All five kinds appear (distance 2, time 2, volume 1, mass 2, money 1), with one fraction and one decimal. No subtraction. One or two fixed problems per kind. The number-line marker is not checked. Two of the eight are bare conversions, not story problems. |
| 4.MD.3 | community-plot-planner | Part | After the formula cards fade, one plot is left (an area one). The perimeter formula is never used without fence pieces. |
| 4.MD.4 | skate-park-angles | Full | Built. |
| 4.MD.5a | skate-park-angles | Full | Built. |
| 4.MD.5b | skate-park-angles | Touched | Only arrow keys in Explore. See below. |
| 4.MD.6, 4.MD.7 | skate-park-angles | Full | Built. Measure, sketch, add and find the missing part. |
| 4.G.1 | quilt-block-studio | Nearly full | Drawing is asked. Naming is done by the tool (it tags angles and glows on parallel lines). Who writes the block label is not said. |
| 4.G.2, 4.G.3 | quilt-block-studio | Full | Trying folds is the standard's own method, not a hole. |

Count: full or nearly full 17, part 8, shown or touched or at risk 4 (4.NBT.1, 4.NF.1, 4.NF.5, 4.MD.5b). Of the 12
that are not full, 10 are major work.

**4.NBT.1.** A real gap in the tool, cheap to close now. Add a short checked round after the zoom: "The 4 in 4,000 is
___ times the 4 in 400", "Which number has a 7 worth ten times the 7 in 3,750?", and one as division (700 / 70). The
written worksheet "Ten Times Greater" already does this on paper, so the year is not bare, but rule 2 wants it in the
tool or off the module.

**4.MD.5b.** It is a definition (an angle that turns through n one-degree steps measures n degrees), not a skill. The
tool is built, not live, so one small job can still be added at Refine: step the dial in one-degree clicks with the
count showing, and stop at a given number. That is honest, not a thin add-on, because the dial already works this way.

**Balance.** The 47 / 23 / 30 split overstates fluency. With the floor 1s removed it is nearer 55 / 10 / 35. Real
fluency work is in three tools: road-trip-logbook, egg-carton-factory and unit-ladder. That is right for tools. Fluency
comes from short, varied practice over many days, which a 25 minute sitting cannot give. What exists for it:
- `data/closet/generators.json`: 26 live generators. Four serve this grade: number-ops (K-5, "to long division, with
  or without regrouping", with an estimate-first setting), fractions (3-7), word-problems (1-6), measure-shapes (2-8).
- `docs/worksheets/math.md`, math-4: 38 planned rows, including Column Addition and Subtraction, Find the Regrouping
  Mistake, Partial Products Practice and Partial Quotients Division. `data/closet/worksheets/math-4.md` has 6 written
  by hand (rows 1, 6, 18, 31, 43, 48).
- There is no top-level `worksheets/` folder and no `data/worksheets*`.
So fluency practice exists on the right shelf. What is missing is a plan that says when it happens. The sequence puts
adding and subtracting at step 7 of 13 and nothing brings it back. That is a year spine job, not a tool job. One tool
fix helps: road-trip-logbook should end by pointing to the number-ops preset, and its "My route" mode is the tool's
own endless practice.

**Focus.** 7 of 13 tools on major work means little by itself: there is one tool per module, and tool count is not
time. Two things do matter. First, the year plan sets the time. As a guide from memory, to be checked, reviews look
for about two thirds or more of the days on major work; the spine must give the seven major modules that share of
the weeks. Second, depth runs the wrong way today. The seven major tools carry 21 codes in about 175 minutes; the six
others carry 12 codes in about 165 minutes, and the deepest tool in the grade (skate-park-angles, cost class super) is
on additional work. The fixes in part C move depth toward the major work without cutting anything.

**Beatable list (table section 6): worth a spec edit before build, or fine**

| Tool | Real hole, fix now | Fine as is |
|---|---|---|
| growth-spurt | Estimate not checked. Written equations in Growing not said to be checked. Tray jobs by elimination (mine). | Multiply or Add by guess: the equation that follows catches it. Side by side has no check: it is the closing look. |
| rule-machine | 10th-shape prediction has no check. | Random dials on mystery tapes: comparing two tapes and adjusting is reasoning; add a try count. Prediction score not gating. |
| stadium-count | Zoom has no check (this is the 4.NBT.1 gap). | Two-choice "more honest" headline: an extra, not the rounding check. |
| area-model-builder | Tiny chunks. Offer chunks by place only and have the child type what each chunk uses. | Snapped cuts: by design, and "Two slicings" gives the choice. |
| road-trip-logbook | Carry chips appear on their own. Exact total typed as the estimate. Fix the "ones column left" wording. | none |
| fraction-wall-duel | Cycling the three reasons. Steals optional (the 4.NF.1 risk). | Picking the bigger card by eye: the reason comes next. |
| recipe-scaler | Cup shows its number; tool regroups; plus button multiplies; two guessable questions. | none |
| money-and-meters | Placing with live linked panels. Proof panel tests nothing. Tool does the 4.NF.5 trade. | none |
| unit-ladder | Marker position not checked. | none |
| community-plot-planner | Only one plot after the cards fade (mine). | The loose lot (226 of 600): fitting plots is not the standard. |
| skate-park-angles, egg-carton-factory | none | All listed items are already closed by the "on your own" counts. |
| quilt-block-studio | none | Folding many lines; mirror mode drawing the other half. |

## C. Proposals

One line per tool. "Note" means a spec edit before build. Nothing is cut and no code moves.

| Tool | Proposal | The note or change |
|---|---|---|
| growth-spurt | Keep with a spec note | The eight problems cover three unknowns (the bigger amount, the smaller amount, how many times) so some need division. Four orders on the default path using all four operations, one with a remainder. The estimate is checked against a range before the answer box opens. Tray jobs get a second number set. |
| egg-carton-factory | Keep | Built and sound. |
| rule-machine | Keep with a spec note | Check the 10th-shape prediction. Name all four shape tapes. Cap tries on mystery tapes. |
| stadium-count | Keep with a spec note | Add the checked ten-times round (see 4.NBT.1). Headlines round to at least four different places. Number names from word tiles. |
| area-model-builder | Keep with a spec note | Chunks by place only; the child types what each chunk uses. Name four-digit dividends and at least three different divisors. |
| road-trip-logbook | Keep with a spec note | The child places each carry and each borrow. The estimate must be a rounded number. Two sums use five- or six-digit numbers (the odometer is there for it). The end card points to the number-ops generator. |
| fraction-wall-duel | Keep with a spec note | Each deck deals at least two rounds where the only winning play is an equal fraction, and one where the child makes the equal fraction. The reason is picked before the bars light, and a wrong reason loses the round. Each win is written with >, = or <. |
| recipe-scaler | Reshape | Two full modes on the same kitchen and scoops, each a sitting with its own end: one for 4.NF.3 (about ten rounds, more than fourths, a real way to split an amount, four named word problems, the child regroups), one for 4.NF.4 (the child types the scoop count before the pile shows, four word problems). Hide the cup's number until Check. See question 1. |
| money-and-meters | Keep with a spec note | The child types 30/100 before the trade. Add rounds where the labels are hidden and the child writes the decimal. Lock the other panels during Placing. In Compare the child builds both amounts on a panel. |
| unit-ladder | Keep with a spec note | Check the marker. Add a subtraction problem and a second set of numbers for each problem. |
| community-plot-planner | Keep with a spec note | Two more notes after the cards fade (one area, one fence), so each formula is used at least twice with no squares or fence. |
| skate-park-angles | Keep with a spec note | One counted-steps Spin job for 4.MD.5b at Refine. See question 2. |
| quilt-block-studio | Keep with a spec note | The child picks the angle tags and fills the block label; the tool checks them. |

### Questions for the owner (5)

1. **recipe-scaler carries seven codes. One tool with two full modes, or two tools?** Pick: one tool, two full modes.
   The model (one-size scoops) and the kitchen are the same, so a second tool would clash with the first.
2. **4.MD.5b on a built tool: add one small job, or leave it to the unit lesson?** Pick: add one counted-steps job at
   Refine. The dial already steps by one degree, so it is honest and small.
3. **Does 4.OA.3 (multistep problems, all four operations) need its own tool?** Pick: not now. Grow growth-spurt to
   four orders and let the spine count the multistep problems in unit-ladder and community-plot-planner. Look again
   after the unit pilot.
4. **Where does 4.NBT.4 fluency live?** Pick: the number-ops generator and the unit's daily practice, with
   road-trip-logbook as the "see why" tool that links to them. No second tool. Fluency needs days, not a sitting.
5. **Change the extract row before the full run (764 specs)?** Pick: yes, apply the eight wording changes in part A
   and re-run this packet as the test. The current rows hide the findings the review exists to make.

Everything else in the proposals table I would simply apply.

### For the grade 4 math year spine

- Mark each standard full, part or shown from the table in part B, not from "ok" in the coverage table.
- Give the seven major modules about two thirds or more of the weeks, and write the reason beside each unit's place.
- Add a fluency thread: short number-ops practice on adding and subtracting that runs for weeks after module 7, and
  one on multiplying and dividing after module 11. Name the generator setting in each unit.
- Fractions (4.NF.3 and 4.NF.4) need the most days and today have the thinnest tool. Plan two tool sittings.
- Tie supporting work to major work on purpose: factors with multiplication, unit conversions with multiplying,
  line plots with fractions, area formulas with missing-factor division.
- 4.NBT.1 and 4.MD.5b need a named lesson moment in their units even after the tool fixes.
- Multistep word problems (4.OA.3) should come back in at least three later units, since one tool will not carry it.
- The order in data/sequence.csv puts fractions (steps 3 to 5) before place value (6) and multi-digit multiplying
  last among number work (11). That follows a known order, but the spine must state why, and check that the
  conversion and area units (9, 10) do not need multiplying the students have not met yet.

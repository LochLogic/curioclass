# Catalog review tables: pilot-math-4

13 tools read (math, grades 4). Built by scripts/catalog_compute.py from docs/agents/catalog/rows/.

## 1. Coverage, standard by standard

A standard is covered when at least one tool teaches it (depth `taught`). `practiced` assumes it was taught elsewhere; `touched` can be skipped; `claimed` has no matching student action.

| Standard | Focus | Taught by | Practiced | Touched or claimed | Status |
|---|---|---|---|---|---|
| 4.OA.1 | major | growth-spurt | - | - | ok |
| 4.OA.2 | major | growth-spurt | - | - | ok |
| 4.OA.3 | major | growth-spurt | - | - | ok |
| 4.OA.4 | supporting | egg-carton-factory | - | - | ok |
| 4.OA.5 | additional | rule-machine | - | - | ok |
| 4.NBT.1 | major | - | - | stadium-count (touched) | thin |
| 4.NBT.2 | major | stadium-count | - | - | ok |
| 4.NBT.3 | major | stadium-count | - | - | ok |
| 4.NBT.4 | major | road-trip-logbook | - | - | ok |
| 4.NBT.5 | major | area-model-builder | - | - | ok |
| 4.NBT.6 | major | area-model-builder | - | - | ok |
| 4.NF.1 | major | fraction-wall-duel | - | - | ok |
| 4.NF.2 | major | fraction-wall-duel | - | - | ok |
| 4.NF.3 | major | recipe-scaler (a, b, c) | recipe-scaler (d) | - | ok |
| 4.NF.4 | major | recipe-scaler (a, b, c) | - | - | ok |
| 4.NF.5 | major | money-and-meters | - | - | ok |
| 4.NF.6 | major | money-and-meters | - | - | ok |
| 4.NF.7 | major | money-and-meters | - | - | ok |
| 4.MD.1 | supporting | unit-ladder | - | - | ok |
| 4.MD.2 | supporting | unit-ladder | - | - | ok |
| 4.MD.3 | supporting | community-plot-planner | - | - | ok |
| 4.MD.4 | supporting | skate-park-angles | - | - | ok |
| 4.MD.5 | additional | skate-park-angles (a) | - | skate-park-angles (touched) | ok |
| 4.MD.6 | additional | skate-park-angles | - | - | ok |
| 4.MD.7 | additional | skate-park-angles | - | - | ok |
| 4.G.1 | additional | quilt-block-studio | - | - | ok |
| 4.G.2 | additional | quilt-block-studio | - | - | ok |
| 4.G.3 | additional | quilt-block-studio | - | - | ok |

Count: ok 27, thin 1.

## 2. Module codes its own tool does not teach

| Tool | Module codes | Not taught or practiced (from the row) | Claimed or only touched |
|---|---|---|---|
| stadium-count | 4.NBT.A | - | 4.NBT.1 (touched) |
| area-model-builder | 4.NBT.B | 4.NBT.4 | - |
| road-trip-logbook | 4.NBT.B | 4.NBT.5, 4.NBT.6 | - |
| unit-ladder | 4.MD.A | 4.MD.3 | - |
| community-plot-planner | 4.MD.A | 4.MD.1, 4.MD.2 | - |
| skate-park-angles | 4.MD.B, 4.MD.C | - | 4.MD.5b (touched) |

## 3. Clash rule (two or more of skill key, action, setting group match, same band)

| Band | Tool A | Tool B | Matched | Shared standards |
|---|---|---|---|---|
| - | none | | | |

Rows with one match are listed only when the two tools also teach or practice the same standard.

## 4. Kinds of work and focus

Each tool splits its time across understanding, fluency and application (0 to 3 each).

| Tool | Focus | Understanding | Fluency | Application | Use | Minutes |
|---|---|---|---|---|---|---|
| growth-spurt | major | 3 | 1 | 2 | lesson | 25 |
| egg-carton-factory | supporting | 3 | 2 | 1 | ongoing | 25 |
| rule-machine | additional | 3 | 1 | 2 | lesson | 25 |
| stadium-count | major | 3 | 1 | 2 | lesson | 25 |
| area-model-builder | major | 3 | 1 | 1 | lesson | 25 |
| road-trip-logbook | major | 2 | 3 | 1 | station | 25 |
| fraction-wall-duel | major | 3 | 1 | 2 | station | 25 |
| recipe-scaler | major | 3 | 1 | 2 | lesson | 25 |
| money-and-meters | major | 3 | 1 | 1 | lesson | 25 |
| unit-ladder | supporting | 2 | 2 | 2 | station | 25 |
| community-plot-planner | supporting | 2 | 1 | 2 | lesson | 25 |
| skate-park-angles | supporting | 3 | 1 | 2 | ongoing | 30 |
| quilt-block-studio | additional | 2 | 1 | 2 | lesson | 30 |

Share of all points: understanding 47%, fluency 23%, application 30%.
Tools by focus: major 7 (54%), supporting 4 (31%), additional 2 (15%).

## 5. Value table

Depth = best depth on any code. Sole = standards only this tool teaches. Sorted so the weakest case for a tool comes first: little taught, paper could do it, costly to build. A sort order for the judge, not a verdict.

| Tool | Stage | Depth | Sole teacher of | Paper could do it | Screen adds | Cost |
|---|---|---|---|---|---|---|
| egg-carton-factory | built | taught | 4.OA.4 | partial | Eggs re-deal instantly into any carton shape and the last short column is ringed, which a printed sheet cannot show while the child drags. | new-engine |
| rule-machine | spec | taught | 4.OA.5 | partial | The tape prints on a lever pull and highlights the predicted feature, so the child commits to a prediction before the machine shows the answer. | new-engine |
| road-trip-logbook | spec | taught | 4.NBT.4 | partial | An odometer rolls its wheels as the child regroups, so a carry looks like a wheel passing 9. | new-engine |
| unit-ladder | spec | taught | 4.MD.1, 4.MD.2 | full | A ghost climber replays the child's last run and the table grows row by row. | new-engine |
| skate-park-angles | built | taught | 4.MD.4, 4.MD.5, 4.MD.6, 4.MD.7 | partial | A dial, a real protractor and a pole with eighths respond to dragging, which a sheet cannot do. | super |
| growth-spurt | spec | taught | 4.OA.1, 4.OA.2, 4.OA.3 | partial | Plants and the strip diagram redraw live as the child drags, so the fixed gap and the kept multiple can be watched side by side. | new-engine |
| stadium-count | spec | taught | 4.NBT.2, 4.NBT.3 | partial | One zoom slider turns one seat into a stadium by tens while a place-value strip slides the digit, which a sheet cannot animate. | new-engine |
| fraction-wall-duel | spec | taught | 4.NF.1, 4.NF.2 | partial | Both fractions light up as bars on one shared wall and the chosen reason animates, so a reason is shown true or false. | new-engine |
| money-and-meters | spec | taught | 4.NF.5, 4.NF.6, 4.NF.7 | partial | Four views of one amount move together, so adding a penny shifts the ribbon, grid and dot at once. | new-engine |
| community-plot-planner | spec | taught | 4.MD.3 | partial | Squares and fence pieces fade into the formula, so the child moves from picture to rule. | sibling |
| quilt-block-studio | spec | taught | 4.G.1, 4.G.2, 4.G.3 | partial | The fold test overlays the halves and shows a match or a gap, so a symmetry claim is tested. | new-engine |
| area-model-builder | spec | taught | 4.NBT.5, 4.NBT.6 | partial | Cut lines snap to place-value breaks and the equation strip builds itself from the child's pieces, so structure and equation stay linked. | sibling |
| recipe-scaler | spec | taught | 4.NF.3, 4.NF.4 | partial | The cup fills scoop by scoop and a test bake rises or falls flat on the scaled card, so each amount is tested. | sibling |

## 6. Flags, beatable checks and unsure notes

- **growth-spurt**
  - beatable: Which one: tap Multiply or Add by guess (two choices, no cap on tries stated)
  - beatable: Orders: the estimate-first step is not said to be checked, so a number can be typed after solving
  - beatable: Growing and Side by side have no check
  - unsure: 4.OA.2 shows only multiplication examples; division comparison not seen
  - unsure: whether the written equations in Growing are checked is not stated
- **egg-carton-factory**
  - unsure: use ongoing because the Order Board saves sealed orders on the device
  - unsure: single standard, so one row; depth taught for the whole 4.OA.4 bundle (pairs, multiples, prime)
- **rule-machine** [spec-thin]
  - beatable: Mystery tapes: turn dials at random until the child's tape matches Cog's (the side by side print is a hint, no cap stated)
  - beatable: Prediction menu: a guess among a short menu; the score counts only, nothing gates on it
  - beatable: Shape-tape prediction (10th shape) has no check described
  - unsure: spec-thin: four shape tapes and six mystery tapes each get one example
  - unsure: catalog family is function-machine; the spec says none, so cost class follows the spec
- **stadium-count**
  - beatable: Headlines: pick the more honest of two roundings (two choices, no reason asked)
  - beatable: Zoom has no check, so the ten-times idea can be skipped
  - unsure: 4.NBT.1 marked touched: zoom is watching, with no student response that needs the skill
- **area-model-builder**
  - beatable: Division: build the missing side from many tiny chunks (ones or tens) until the area is used up; only the leftover is checked
  - beatable: Slicing: cut lines snap only at place-value breaks, so the cut itself needs no decision
  - unsure: old tags kept; setting_group generic kept
  - unsure: no timed or repeated practice described, so fluency is low
- **road-trip-logbook**
  - beatable: Estimate: type the exact total as the estimate (whether the estimate is checked for rounding is not stated)
  - beatable: Columns: the carry chips appear on their own, so no regroup decision is asked
  - unsure: spec says digits go 'from the ones column left' in one place and 'right to left' in another
- **fraction-wall-duel**
  - beatable: Reasons: cycle through the three reason buttons until one wins (a wrong reason is only counted as a miss; no cap stated)
  - beatable: Play the bigger card by eye from the lit bars before giving any reason
  - beatable: Rosa's wrong-reason claims are optional to challenge
  - unsure: family engine fraction-wall not built yet, so cost new-engine
  - unsure: action compare kept from old tag though the format is cards
- **recipe-scaler**
  - beatable: Scaling: the spec closes multiplying both numbers but not guessing on the which-batch and between-wholes questions
  - unsure: 4.NF.3d marked practiced: the word problems get one line
  - unsure: cost sibling (fraction-food) though 13 images make it heavy
- **money-and-meters**
  - beatable: Placing: drag the dot until the linked meter-stick panel shows the target length; no skill needed
  - unsure: setting_group kept generic
- **unit-ladder**
  - beatable: Track: place the marker anywhere, then the answer box opens (marker position is not said to be checked)
  - unsure: action drill kept; the track meet is word problems
  - unsure: 4.MD.3 explicitly moved out of this tool
- **community-plot-planner**
  - beatable: The lot: five plots total 226 of 600 square feet, so almost any placement fits without the skill
  - unsure: module lists 4.MD.A (1 to 3); this tool covers only 4.MD.3
- **skate-park-angles**
  - beatable: Park: let Rae show every job; each shown job still adds its piece (only the on-your-own count differs)
  - beatable: Jump Log questions: type an axis label on screen; about 15 percent lucky per question, closed for the on-your-own mark
  - beatable: Ride and Test ride have no checks
  - unsure: 4.MD.5b touched: only Explore arrow keys and the readout; no job asks it
  - unsure: cost super from four workshops and 14 park pieces
- **quilt-block-studio**
  - beatable: Symmetry hunt: try many lines with Fold until the halves match (count accepted only after each line is folded)
  - beatable: Mirror mode: the tool draws the other half, so the child only chooses the line
  - unsure: flag proportions and sources sit in a data block; not checked here

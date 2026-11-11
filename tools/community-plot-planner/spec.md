# Community Plot Planner

## One idea
An empty city lot, 30 feet by 20 feet, is becoming a community garden, and the child is the lot planner: five families each send a note with one fixed number (the Lee family needs 48 square feet and their plot can be 6 feet wide; the Ortiz family has 30 feet of fence and wants a plot 5 feet wide), and the child finds the missing side by laying unit squares or fence pieces until the rule shows itself (48 squares in rows of 6 make 8 rows, so the plot is 8 feet long), writes the matching equation (6 x ? = 48, 2 x (5 + ?) = 30), then drags each finished plot onto the lot; the unit squares fade once the child has written the area formula, and the fence pieces fade once the perimeter formula is written; at the end every family has a plot that fits, the plots fill 226 of the lot's 600 square feet with room for paths, and the child states both rules in words, so a fourth grader learns to apply the area and perimeter formulas for rectangles in real problems, including finding a missing side.

## Not like
- garden-grid (2, spec): counting square plots, by look only. Here formulas and missing sides.
- tile-the-floor (3, spec): area by tiling, same unit grid. Here using the formula.
- fence-builder (3, spec): same perimeter, different area. Here a fixed number and a missing side.
- unit-ladder (4, concept): unit conversions. Here area and perimeter.

## Who and how
- Grade 4, Math, module "Area and Perimeter Formulas". Standards: 4.MD.3 (apply the area and perimeter formulas for rectangles in real world and mathematical problems; for example, find the width of a rectangular room given the area of the flooring and the length, by viewing the area formula as a multiplication equation with an unknown factor).
- Format: builder. Driver: one student alone (tool.json `driver: "student"`). Role: lesson. `Read` reads every card. Controls 48 px or more.
- Change note (spec fix, 2026-11-10): small additions only. The missing-side box now has two tries, and a second miss brings the squares back and adds a spare note to be done by formula alone. Before a plot goes on the lot the child now works out its other measure from both sides (the fence for an area plot, the area for a fence plot), so the formulas are also used the plain way round.
- Five family notes (three area, two fence), unit squares and fence pieces, the equation strip, the formula cards, the lot. Extra: Class lot (the teacher sets a lot size and each student plans a plot). tool.json `modes: ["Lot planner", "Class lot"]`, `minutes: "20-30"`, `grades_label: "Grade 4"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 4.MD.3 (area) | Lay squares in rows, then write width x length = area with a missing side | rows of squares; 6 x ? = 48 | 2 |
| 4.MD.3 (perimeter) | Lay fence pieces, then write 2 x (width + length) = fence | fence pieces; 2 x (5 + ?) = 30 | 3 |
| 4.MD.3 (apply) | Fit five plots on the lot and state both rules | the lot; the formula cards | 4 |
| 4.MD.3 (both sides known) | For each finished plot, type the measure the note did not give: the fence for an area plot, the area for a fence plot | the plot's tag filling in | 5 |

The standard's verb is "apply the area and perimeter formulas", and the student does it on every row: five missing sides and five both-sides sums, ten items of four kinds. The Lee plot is the model: its squares and its equation are led step by step by the welcome and first hints.

## Screens and modes
Header (kit): title "Community Plot Planner"; `Lot planner`, `Class lot`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** An empty lot with fence posts at the corners and a clipboard of five family notes. The welcome is queued (`welcomeAfter: true`): "The Lee family needs 48 square feet, and their plot is 6 feet wide. How long is it? Drag a row of squares onto the grid." First hint: "Drag a row of squares onto the grid."

**Area plots (focus: the work grid).** At 1366x768 the work grid fills the left with the note and equation strip right and the lot along the bottom; at 680x425 the lot is a tab. Rows of 6 stack until 48 squares are used: 8 rows. The strip writes 6 x 8 = 48 and asks for the missing number before showing it. Nguyen: 36 square feet, 4 wide (9 long). Clark: 60 square feet, 5 wide (12 long).

**Fence plots.** Ortiz: 30 feet of fence, 5 feet wide. Fence pieces go around; the child finds the length is 10 and writes 2 x (5 + 10) = 30. Abebe: 24 feet of fence, 8 feet long (4 wide). 
**Plot tags.** Before any plot can be dragged to the lot its tag must be complete. The note gave one measure; the child types the other from the two sides, with no squares or fence pieces shown: Lee 6 by 8, fence 28 feet; Nguyen 4 by 9, fence 26; Clark 5 by 12, fence 34; Ortiz 5 by 10, area 50 square feet; Abebe 4 by 8, area 32. Two tries, then the pieces are laid for the child to count and the tag is marked "counted".

**Formula cards.** After two of each, the child fills "area = ___ x ___" and "perimeter = 2 x (___ + ___)" and the squares and fence pieces fade: the next plots use only the formula. With the pieces gone, the missing-side box takes two tries. After a second miss the squares or fence come back for that plot, its tag is marked "built with squares", and a spare note is added that must be done by formula alone: Park, 72 square feet and 8 feet wide (9 long), or Diaz, 36 feet of fence and 12 feet long (6 wide). Spare plots do not go on the lot.

**The lot (the aha).** The child drags plots onto the 30 by 20 lot; they snap to whole feet and cannot overlap. When all five fit, the lot says 226 of 600 square feet planted. Narrator: "The squares and the fence showed you why. Now the rule does the counting."

**The end.** The lot plan with each plot's sides, area and fence. `Print` prints it.

**Class lot (extra).** The teacher sets a lot size; each student adds one plot from a note.

## Content
- Five families (made up, labeled "illustration" where pictured) with their notes, sizes in whole feet, the 30 by 20 lot, all readable with `Read`.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Plots can be moved and turned on the lot until `Check`.
- Keyboard: Tab to the squares, fence pieces, the equation boxes, the formula cards and plots on the lot; arrows move a plot one foot; R turns it; Enter places.
- With Motion off squares and fence pieces appear at once.

## Look
- Accent `--brand` #6b4423 soil brown (header, the lot border, buttons); gold #f4c542 (the plot in hand, a plot that fits); paper #f8f2ec; ink #24150a; muted #5c5249.
- Contrast (WCAG 2.1, computed): white on brand 8.48:1; brand on paper 7.63:1; ink on paper 15.93:1; muted on paper 6.85:1; ink on gold 10.88:1.
- Never color alone: plots carry family names and sizes; overlaps show a hatch and words.
- Different from this batch (tomato red, dungeon violet, kitchen-tile blue, highway green).

## Art
- People (illustrated): five family portraits on the notes, labeled "illustration" (Gemini, `people: true`, 5; cutout yes).
- Local FLUX (`scripts/localart.py`): the empty lot (1, 16:9), the planted garden (1, 16:9).
- Drawn in code: the work grid, squares, fence pieces, plots and the lot plan.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `wise-mentor` as the garden club leader; `calm-professor` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.family + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `rows`: "Drag a row of squares onto the grid."
- how `fence`: "Drag fence pieces around the plot."
- how `equation`: "Type the missing side."
- how `formula`: "Fill in the formula card."
- how `place`: "Drag the plot onto the lot."
- event, whole, the lot.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Reuses the unit grid and area counts from the marked block `/* AREA ENGINE: begin */ ... /* end */` as described in tile-the-floor's spec. Tool-only code: fence pieces, the equation strip, the formula cards, the lot with snapping and overlap checks.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Missing side | Type numbers until one works | The squares or fence must match the note first; after the cards fade there are two tries, then the pieces return, the plot is tagged and a spare note is added, so guessing makes more work than dividing. |
| Plot tags | Type the note's number again; add the two sides for the fence | The tag asks for the measure the note did not give; 14, 13 and 17 (one length plus one width) fail, and after two misses the tag reads "counted". |
| Formula cards | Fill them by guessing | Each card is tested on the next plot. |
| The lot | Stack plots | Plots cannot overlap or leave the lot. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `rows`; `equation`.
2. `fence`.
3. `formula`; `place`.
4. The lot (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 4.MD.3 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Formulas make sense when built from unit squares and lengths | Common Core Standards Writing Team (2012), "Progressions for the CCSS, Geometric Measurement" | Battista (2004), "Applying cognition-based assessment to elementary school students' development of understanding of area and volume measurement", Mathematical Thinking and Learning | yes |
Backed twice: 2. Cut: 0.

Checks run (Python, scratchpad s12, 2026-11-10): 48 / 6 = 8 with a fence of 28; 30 feet of fence 5 wide gives 10 long and 50 square feet; 36 / 4 = 9 with a fence of 26; 24 feet of fence 8 long gives 4 wide and 32 square feet; 60 / 5 = 12; the plots total 226 square feet of the 600 on the lot; contrast as in Look.
Checks run again for the spec fix (Python, scratchpad s/fx, 2026-11-10): fences 28, 26 and 34 feet; areas 50 and 32 square feet; five areas total 226; spare notes 72 / 8 = 9 and 36 feet of fence with 12 long gives 6 wide; one length plus one width (14, 13, 17) never equals a right tag.

## Done when
1. Focus and fold: at 1366x768 grid, note and lot; at 680x425 lot as a tab.
2. Three area plots have their missing side found and written as an equation. (4.MD.3)
3. Two fence plots have their missing side found and written as an equation. (4.MD.3)
4. Both formulas are written and five plots fit on the lot. (4.MD.3)
5. Each plot's tag holds the measure the note did not give, typed by the child from both sides: 28, 26, 34 feet of fence and 50, 32 square feet. (4.MD.3)
6. With the pieces faded the missing-side box allows two tries; a second miss returns the pieces and adds a spare note.
7. `Read` reads every card; every control is 48 px or more.
8. Families are labeled illustration.
9. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
10. Motion off: squares and fence appear at once; no network requests.

## Open questions
- The idea card flags overlap with garden-grid by look (default used: an empty city lot with fence posts and family notes, soil brown, no square seed plots; the title avoids "garden").

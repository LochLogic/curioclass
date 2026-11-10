# How Many Fit

## One idea
On a workbench sits a container bar and a stack of fraction bars cut from the same fraction wall, and the prompt asks "How many 3/4s fit in 2/3?" with no answer box yet; the child drags 3/4 bars into a 2/3 container, sees that not even one fits, and the part bar that does fit is shaded with its own fraction, 8/9 of a 3/4 bar, so 2/3 / 3/4 = 8/9 and the leftover is read as a fraction of the bar, not of the whole; measuring rounds come on story cards (how many 3/4-cup servings in 2 1/2 cups of yogurt is 3 1/3; how many 1/3-mile laps in 2 1/2 miles is 7 1/2); sharing rounds ask how much in one group (3 friends share 1/2 pound of chocolate, so each gets 1/6 pound); missing-side rounds use the area model (a garden strip of 1/2 square mile and length 3/4 mile is 2/3 mile wide); every answer is checked as multiplication (3/4 x 8/9 = 2/3), and after enough cases the child spots the shortcut, multiply by the flipped divisor, and tests it on new cards before it is named; at the end the child writes a story for an expression like 2/3 / 3/4, so a sixth grader learns to interpret and compute quotients of fractions and to solve word problems with them using visual models and equations.

## Not like
- fraction-wall-duel (4, spec): comparing fractions on the same wall engine. Here dividing them.
- shrink-ray (5, spec): multiplying fractions as scaling. Here dividing as measuring.
- camp-cook-share-out (5, spec): unit fractions and whole numbers. Here any fraction by any fraction.
- smoothie-lab (Grades 6-7, live): ratios in recipes. Here quotients of fractions.

## Who and how
- Grade 6, Math, module "Dividing Fractions". Standards: 6.NS.1 (interpret and compute quotients of fractions, and solve word problems involving division of fractions by fractions, e.g., by using visual fraction models and equations to represent the problem; for example, create a story context for (2/3) / (3/4) and use a visual fraction model to show the quotient; use the relationship between multiplication and division to explain that (2/3) / (3/4) = 8/9 because 3/4 of 8/9 is 2/3; how much chocolate will each person get if 3 people share 1/2 lb of chocolate equally? how many 3/4-cup servings are in 2/3 of a cup of yogurt? how wide is a rectangular strip of land with length 3/4 mi and area 1/2 square mi?).
- Format: sandbox. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Eight measuring cards, four sharing cards, four missing-side cards, the shortcut test, the story writer. Extra: Story swap (students write a story for an expression and a partner models it). tool.json `modes: ["Workbench", "Story swap"]`, `minutes: "20-30"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 6.NS.1 (measuring) | Drag divisor bars into the container; read the part bar | 8/9 of a 3/4 bar | 2 |
| 6.NS.1 (sharing, missing side) | Split a bar into groups; fill a rectangle | 1/6 lb each; a 2/3-mile width | 3 |
| 6.NS.1 (equations, stories) | Check by multiplying; test the shortcut; write a story | 3/4 x 8/9 = 2/3 | 4 |

## Screens and modes
Header (kit): title "How Many Fit"; `Workbench`, `Story swap`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A workbench with a fraction wall on the back, a container bar labeled 2/3 and a stack of 3/4 bars. The welcome is queued (`welcomeAfter: true`): "How many three fourths fit in two thirds? Drag a bar into the container." First hint: "Drag a 3/4 bar into the container."

**Measuring (focus: the container).** At 1366x768 the container runs across the middle with story cards left and the check strip right; at 680x425 the cards are a tab. A bar that is too long hangs over the end; the child taps `Trim` and the part that fits is shaded and split into the common unit (here ninths of the bar), and the strip writes 8/9. Whole bars that fit count first; the part bar is added (3 1/3 for 2 1/2 / 3/4).

**Sharing.** A card: "3 friends share 1/2 lb of chocolate." The child splits the 1/2 bar into 3 equal parts and reads one part against the whole wall: 1/6.

**Missing side.** A rectangle with area 1/2 and length 3/4; the child drags the width handle until the area matches, and the width reads 2/3.

**Check and shortcut.** Each answer is checked as multiplication in the strip (3/4 x 8/9 = 2/3). After six cards a list of every division so far appears beside its answer; the child picks the pattern from four (only "multiply by the flipped divisor" fits every row) and tests it on two new cards before it is named.

**Leftover (the aha).** Narrator: "Dividing is measuring or sharing. And the leftover is a piece of the divisor, not of the whole."

**Write a story.** The child picks a context and writes a story for 2/3 / 3/4; the tool models it beside the story.

**The end.** The card log and story. `Print` prints them.

**Story swap (extra).** A partner models the story.

## Content
- Sixteen cards with fractions and mixed numbers, denominators up to 12, all readable with `Read`.
- Bars are exact lengths drawn from the wall; context pictures are illustrations.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Bars can be removed and trimmed again until `Check`.
- Keyboard: Tab to the bar stack, the container, Trim, the width handle (arrows move one twelfth), cards and answer boxes; Enter places or checks.
- With Motion off bars appear in place.

## Look
- Accent `--brand` #0f6a62 measuring-cup teal (header, the container, buttons); gold #f4c542 (the bar in hand, the part bar); paper #ebf6f4; ink #04211e; muted #4a5856.
- Contrast (WCAG 2.1, computed): white on brand 6.45:1; brand on paper 5.84:1; ink on paper 15.32:1; muted on paper 6.74:1; ink on gold 10.40:1.
- Never color alone: the part bar is hatched and carries its fraction.
- Different from this batch (awning orange, trellis green, deep-sea navy, market plum).

## Art
- Local FLUX (`scripts/localart.py`): the workbench (1, 16:9), story card pictures for yogurt, a track, chocolate and a garden strip (4, 4:3).
- Drawn in code: the wall, every bar and the rectangle at exact lengths.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `calm-professor` as the narrator; `clear-teacher` as the hints. `Curio.voice` with `scope: () => state.mode + ':' + state.card + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `drag`: "Drag a bar into the container."
- how `trim`: "Tap Trim to fit the last bar."
- how `split`: "Tap Split, then pick the number of groups."
- how `width`: "Drag the width handle."
- how `pattern`: "Pick the pattern that fits every row."
- event, whole, leftover.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
fraction-wall, using the FRACTION-WALL ENGINE block as described in fraction-wall-duel's spec: the wall rows, bars for any a/b, row splitting by n, and exact comparison with `Frac`. Tool-only code: the container, trimming to a part bar, the area rectangle, the pattern test, the story writer.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Measuring | Read the leftover against the whole | The check strip multiplies back and fails (3/4 x 2/9 is not 2/3). |
| Shortcut | Flip the first fraction | The pattern test shows a row where it fails. |
| Story | Write any story | The tool models it; a story for 3/4 / 2/3 draws a different picture. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `drag`; `trim`.
2. `split`; `width`.
3. `pattern`.
4. Leftover (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 6.NS.1 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| The leftover in fraction division is often read against the wrong unit | Ma (1999), "Knowing and Teaching Elementary Mathematics", Lawrence Erlbaum | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 The Number System" | yes |
| Measurement and sharing models build meaning for division of fractions | Siegler and others (2010), "Developing effective fractions instruction for kindergarten through 8th grade", IES Practice Guide | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 The Number System" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s17, 2026-11-10): 2/3 / 3/4 = 8/9 and 3/4 x 8/9 = 2/3; 2 1/2 / 3/4 = 3 1/3; 2 1/2 / 1/3 = 7 1/2; 1/2 / 3 = 1/6; 1/2 / 3/4 = 2/3; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 container, cards and strip; at 680x425 cards as a tab.
2. Eight measuring cards are solved with bars, with leftovers read as part of the divisor. (6.NS.1)
3. Sharing and missing-side cards are solved with models. (6.NS.1)
4. Every answer is checked by multiplying; the shortcut is found and tested; a story is written. (6.NS.1)
5. Bars use the shared fraction-wall engine at exact lengths.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: bars appear in place; no network requests.

## Open questions
None.

# Big Wheel, Small Wheel

## One idea
In a backyard two siblings, Maya and Kip (made up, labeled "illustration"), argue over round things, and the child settles each argument at a lab bench with string, a ruler and wheels; in the circumference lab the child rolls wheels of five sizes one full turn, measures each track, records circumference and diameter in a table, and sees the ratio is always a bit more than 3 (pi, about 3.14), so C = pi x d; in the area lab the child cuts a circle into 8, then 16, then 64 wedges and lines them up head to tail, and they form a near-rectangle with height r and length half the circumference, so A = pi x r x r, which ties the two formulas together; argument rounds use both: one 18-inch pizza (about 254.5 square inches) beats two 12-inch pizzas (about 226.2), but one 14-foot trampoline (about 153.9 square feet) loses to two 10-foot ones (about 157.1), so the child has to check rather than assume; a 26-inch bike wheel turns about 776 times in a mile and a 20-inch wheel about 1,008 times; at the end the child sees that area grows with the square of the radius, so a seventh grader learns the formulas for the area and circumference of a circle, uses them to solve problems, and gives an informal derivation of the relationship between them.

## Not like
- snow-globe-maker (8, concept): volume of cylinders, cones and spheres. Here flat circles.
- blueprint-studio (7, concept): scale drawings. Here circles at true size.
- fence-builder (3, spec): area against perimeter of rectangles. Here area against circumference of circles.
- intersection-angles (7, concept): angle relationships. Here round shapes.

## Who and how
- Grade 7, Math, module "Circles". Standards: 7.G.4 (know the formulas for the area and circumference of a circle and use them to solve problems; give an informal derivation of the relationship between the circumference and area of a circle). 7.G.5 moves to intersection-angles and 7.G.6 to aquarium-builder.
- Format: lab. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Five rolling wheels, the circumference table, the wedge cutter (8, 16, 64 wedges), six arguments. Extra: My round things (the child measures round things at home and adds them to the table; they stay on the device). tool.json `modes: ["Backyard", "My round things"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 7.G.4 (circumference) | Roll wheels; record C and d; divide | the ratio near 3.14 every time | 2 |
| 7.G.4 (derivation) | Cut wedges and line them up | a near-rectangle r tall and C/2 long | 3 |
| 7.G.4 (problems) | Settle the arguments | areas and turns side by side | 4 |

## Screens and modes
Header (kit): title "Big Wheel, Small Wheel"; `Backyard`, `My round things`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A backyard picnic table with pizza boxes, Maya and Kip mid-argument ("Two 12-inch pizzas is more. Obviously."), and a lab bench with string, a ruler and five wheels. The welcome is queued (`welcomeAfter: true`): "Before pizza, let's learn circles. Drag a wheel onto the track and tap Roll." First hint: "Drag a wheel onto the track."

**Circumference lab (focus: the track).** At 1366x768 the track runs across the bottom with the table right; at 680x425 the table is a tab. A wheel with a paint dot rolls one turn and leaves a mark; the child measures the track with the ruler and the diameter with calipers. The table adds a row and a C / d column; the child divides. Five rows all land near 3.14.

**Area lab.** A circle is cut into 8 wedges; the child drags them into a row, alternating up and down. The `More wedges` button goes to 16 and 64, and the row gets closer to a rectangle. Labels appear on request: height r, length half of C, which is pi x r. The child fills in: area = r x pi x r.

**Arguments.** Six cards: pizzas, trampolines, bike wheels over a mile, a running track's curved end, a round rug against a square one, a pan. For each the child computes, picks a winner, and Maya or Kip responds. The trampoline card is the surprise: two small ones win.

**Square of the radius (the aha).** Maya: "Double the radius and the area is four times as big. That's why the big pizza wins. Mostly."

**The end.** The table and the verdicts. `Print` prints them.

**My round things (extra).** Home measurements join the table.

## Content
- Five wheels (diameters 4, 6, 8, 10, 12 cm), six arguments with sizes in inches and feet, answers rounded to tenths with pi as 3.14 or the pi key, all readable with `Read`.
- Measuring rounds accept small error (plus or minus 0.2 cm); the ratio still comes out near pi.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Measurements can be retaken until the row is saved.
- Keyboard: Tab to wheels, Roll, the ruler (arrows move 0.1 cm), the table, wedges (arrows move), More wedges and verdict buttons; Enter rolls, places or checks.
- With Motion off the wheel jumps to the end of its turn and wedges snap into place.

## Look
- Accent `--brand` #1d5591 bike-path blue (header, the track, buttons); gold #f4c542 (the wheel in hand, the paint dot); paper #edf3fa; ink #071a33; muted #4c5565.
- Contrast (WCAG 2.1, computed): white on brand 7.61:1; brand on paper 6.81:1; ink on paper 15.61:1; muted on paper 6.73:1; ink on gold 10.72:1.
- Never color alone: wedges alternate with a stripe pattern; verdicts show the winner's name.
- Different from this batch (beaker violet, asphalt slate, clay sienna, card-table green).

## Art
- People (illustrated): Maya and Kip, labeled "illustration" (Gemini, `people: true`, 2; cutout yes).
- Local FLUX (`scripts/localart.py`): the backyard (1, 16:9), pizzas, trampolines, bikes, a track, a rug and a pan (6, 4:3).
- Drawn in code: wheels, the track, calipers, wedges, the table.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `big-sister` as Maya; `playful-friend` as Kip and the hints. `Curio.voice` with `scope: () => state.mode + ':' + state.lab + ':' + state.card + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `roll`: "Drag a wheel onto the track, then tap Roll."
- how `measure`: "Drag the ruler to the paint mark."
- how `wedge`: "Drag the wedges into a row."
- how `argue`: "Work out both sides, then tap a winner."
- event, whole, square of the radius.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: rolling wheels, the measurement table with C / d, the wedge cutter, arguments with rounding to tenths.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Ratio | Type 3.14 | Each row needs a measured track first. |
| Arguments | Always pick the bigger single circle | The trampoline card is built to catch it. |
| Area | Use pi x d | The wedge row shows r x pi r, and the check uses area. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `roll`; `measure`.
2. `wedge`.
3. `argue`.
4. Square of the radius (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 7.G.4 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| The wedge rearrangement as an informal derivation of circle area | Common Core Standards Writing Team (2012), "Progressions for the CCSS, 7-8 Geometry" | Archimedes, "Measurement of a Circle" (as presented in Heath, "The Works of Archimedes", 1897) | yes |
| 1 mile = 63,360 inches | NIST, Handbook 44, Appendix C | NIST, Special Publication 811 | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s18, 2026-11-10): pi x 9^2 is about 254.5 and 2 x pi x 6^2 about 226.2; pi x 7^2 is about 153.9 and 2 x pi x 5^2 about 157.1; 63,360 / (26 pi) is about 776 and 63,360 / (20 pi) about 1,008; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 track and table; at 680x425 table as a tab.
2. Five wheels are rolled and measured, and C / d is near pi each time. (7.G.4)
3. Wedges are rearranged into a near-rectangle, and A = pi r^2 is tied to C. (7.G.4)
4. Six arguments are settled with computed areas or turns. (7.G.4)
5. Maya and Kip are labeled illustration.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: wheels jump and wedges snap; no network requests.

## Open questions
- The idea card moves 7.G.5 and 7.G.6 out of this tool (default used: 7.G.5 goes to intersection-angles and 7.G.6 to aquarium-builder; this tool keeps 7.G.4).

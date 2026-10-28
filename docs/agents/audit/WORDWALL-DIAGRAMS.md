# Word Wall diagram audit

Review of every code-drawn Word Wall picture in Curio Class (cards whose picture starts with `svg:`, drawn by `scripts/wordsvg.py` from `data/closet/words/diagrams.py`). Each diagram was rendered at full size, laid on labeled contact sheets with its word and definition, and checked for meaning, accuracy, clutter and readability. Painted specs (`paint('prompt')`) were skipped; another review covers them. Nothing in the repo was changed.

## Totals

- Diagrams reviewed: 1738 (2 paint specs skipped, 0 render errors)
- OK: 1540
- FIX: 186
- PAINT: 12

| subject | diagrams | FIX | PAINT |
|---|---|---|---|
| arts | 106 | 12 | 1 |
| computer-science | 126 | 14 | 0 |
| cte | 11 | 3 | 0 |
| ela | 240 | 16 | 1 |
| eld | 41 | 4 | 0 |
| health-pe | 53 | 5 | 3 |
| library | 20 | 1 | 0 |
| math | 716 | 81 | 1 |
| science | 243 | 23 | 2 |
| sel | 22 | 2 | 1 |
| social-studies | 87 | 13 | 0 |
| world-languages | 73 | 12 | 3 |

## Recurring problems (fix once in wordsvg.py)

- **eq() operator spacing.** `=`, `+` and `x` run into fraction bars, boxed terms and words (many math cards). Add padding around operators in `eq()` and boxed-term rows; this clears a dozen rows at once.
- **Hands drawn as oven mitts.** The open-hand glyph has no separate fingers, so ASL and greeting cards read as mittens. Redraw the hand glyph with fingers, or use `handshake()` where two hands meet.
- **clock() hands cover numerals.** Hands reach past the numeral ring, and at 12:00 the two hands overlap. Shorten the hands to inside the numerals and avoid 12:00 for minute-hand cards.
- **Line plots use dots.** Several definitions say X marks but the plot draws dots. Give the line plot helper an X marker option and use it on those cards.
- **Nothing marked.** Rounding number lines, coordinates, compare and more/less cards show the data but never mark the answer (no arrow to the nearest ten, no (x, y) label, no circle on the larger group).
- **Duplicate or near-duplicate pictures** for different words (brave and rights, family and mother, charge and Coulomb's law, month, day and year calendars).
- **Food webs without arrowheads,** so the direction of energy is lost.

## Cards to change

Numbers in the first column are contact-sheet numbers (sheets sorted by subject file, then key).

### arts

| # | module_id/slug | word | verdict | why | fix or prompt |
|---|---|---|---|---|---|
| 3 | arts-3-5-characters-and-scenes/projection | projection | PAINT | ear plus rows of dots does not read as a voice reaching an audience | simple flat illustration of an empty theater: a stage at the front and rows of seats, with curved sound-wave lines traveling from the stage all the way to the back row, no text, no people |
| 32 | arts-3-5-reading-music/measure | measure | FIX | bar lines are there but thin and nothing marks one measure, so the word does not stand out | thicken the bar lines and shade the space between two of them (one measure) in light blue |
| 43 | arts-6-8-animation-basics/timing | timing | FIX | dashed bounce path dips below the ground line and the dots do not sit on it | keep the path on or above the ground line, put each dot on the path, bunch dots near the top of each arc to show more frames there |
| 44 | arts-6-8-arranging-a-song/dynamics | dynamics | FIX | a bare hairpin does not say loud or soft | add a "p" at the narrow end and an "f" at the open end (dynamic letters) |
| 47 | arts-6-8-art-history-timeline/context | context | FIX | a small orange square on a timeline does not say "time, place and events around an artwork" | put a framed-picture icon in the middle of the timeline with a clock, a map pin and a small house/flag icon around it |
| 49 | arts-6-8-choreography/motif | motif | FIX | three identical spirals show repetition but not "changes" | keep the spiral but vary it: same spiral, then bigger, then rotated or recolored |
| 65 | arts-6-8-harmony-and-chords/minor | minor | FIX | labeled A C E but the chord drawn is D F A (steps -1, 1, 3; step 0 is the bottom line E) | staff([(3, 5, 7)], ...): A, C, E are the second space, third space and top space |
| 69 | arts-6-8-performing-in-different-spaces/spacing | spacing | FIX | footprints in a row show steps, not how far apart dancers stand | two or three dancer dots seen from above with a double-headed arrow measuring the gap between two of them |
| 77 | arts-6-8-scripts-and-staging/downstage | downstage | FIX | stage trapezoid with the front half shaded, but nothing says where the audience is | add a row of audience seat dots below the front edge (or an "audience" label) so "closest to the audience" reads |
| 78 | arts-6-8-scripts-and-staging/upstage | upstage | FIX | back half shaded, but no audience marker, so up and down cannot be told apart | same as downstage: add the audience seat dots below the front edge |
| 82 | arts-9-12-music-theory/modulation | modulation | FIX | two tiny key signatures; the second has a stray natural-looking sign and both are too small to read | draw the two staffs larger, stacked or with a bigger arrow, one sharp then two sharps, no extra signs |
| 90 | arts-k-2-high-and-low-loud-and-soft/dynamics | dynamics | FIX | bare hairpin with no p or f | add "p" at the point and "f" at the open end |
| 106 | arts-k-2-steady-beat-and-rhythm/short-sound | short sound | FIX | a lone orange bar has nothing to be short next to | show the short bar beside a long one (long then short), with the short one highlighted |

### computer-science

| # | module_id/slug | word | verdict | why | fix or prompt |
|---|---|---|---|---|---|
| 108 | computer-science-1-code-a-path/debug | debug | FIX | magnifier over an arrow shows looking, not finding and fixing a mistake | code_lines with one line highlighted red under the magnifier, and a small bug or check icon |
| 129 | computer-science-3-5-computing-inventions-and-inventors/timeline | timeline | FIX | 1940, 1970, 1990, 2010 are drawn evenly spaced though the gaps are 30, 20, 20 years, which teaches a wrong timeline habit | use evenly spaced years (1950, 1970, 1990, 2010) or space the dots by the real gaps |
| 130 | computer-science-3-5-fair-surveys/organize | organize | FIX | a tally table does not show putting things in a useful order | a jumble of mixed shapes on the left, an arrow, the same shapes sorted into rows by kind on the right |
| 145 | computer-science-4-tables-and-visualizations/sort | sort | FIX | the two bar charts are drawn tiny in the middle of a mostly empty card | draw them at least twice as large (stack them, or use size=420 with fewer bars) |
| 148 | computer-science-4-trace-the-code/comment | comment | FIX | a dark bar with a speech bubble does not read as a line of code the computer skips | code_lines(..., comment=k) with the comment line grayed and a "#" mark, and a skip arrow jumping past it |
| 150 | computer-science-4-trace-the-code/trace | trace | FIX | the code panel runs off the right edge of the card (clipped) | shrink code_lines or shift it left so the whole panel and the arrow fit inside the card |
| 164 | computer-science-5-remix-a-program/attribution | attribution | FIX | a code block with a star does not show credit to a creator | show a remixed block with an arrow pointing back to the original block and a small tag reading "by" (or a credit line under it) |
| 176 | computer-science-6-8-algorithms-and-fairness/algorithmic-bias | algorithmic bias | FIX | a level (untilted) scale and a tiny flowchart, both too small; a balanced scale says fair, the opposite of bias | enlarge, tilt the scale clearly to one side, and put the flowchart feeding into the low pan |
| 191 | computer-science-6-8-data-detectives/sort | sort | FIX | the two bar charts are tiny in a mostly empty card | draw them at least twice as large |
| 195 | computer-science-6-8-flowcharts-and-pseudocode/decision | decision | FIX | a lone diamond with "?" does not show the path splitting | add the incoming arrow and two labeled branches, yes and no, as in the conditional card |
| 200 | computer-science-6-8-machine-learning-models/accuracy | accuracy | FIX | a rising bar chart says "growth", not the share of predictions that are right | reuse the accuracy grid: 10 circles, 9 green checks and 1 red X, with "9 of 10" under it |
| 220 | computer-science-k-2-what-the-code-does/program | program | FIX | an empty square of arrows does not say "a set of code that does a job" | a stack of code blocks under a green flag (or a play button) with a check beside it |
| 222 | computer-science-k-count-and-decide/chart | chart | FIX | loose apples and bananas are a group of fruit, not a chart | line them up in a picture graph: one row per fruit, a small fruit icon label at the left of each row, on light grid boxes |
| 227 | computer-science-k-public-or-private/public | public | FIX | an eye over a paint palette does not say "OK for anyone to see" | a post or picture in a browser window with several eyes around it, or an open (unlocked) padlock beside a globe |

### cte

| # | module_id/slug | word | verdict | why | fix or prompt |
|---|---|---|---|---|---|
| 234 | cte-6-8-economy-checkup/rate | rate | FIX | a pie with a thin unlabeled wedge does not show one amount compared to another | label the wedge with its percent (for example 10%) and show "10 out of 100" under the circle |
| 235 | cte-6-8-interest-rate-dial/compound-interest | compound interest | FIX | plain growing bars look like any growth, not interest on interest | stacked bars: a constant savings base in one color and a growing interest layer in another on top |
| 239 | cte-6-8-snow-season-prices/equilibrium-price | equilibrium price | FIX | two crossing lines with no labels; the word depends on knowing which is supply and which is demand | label the lines "supply" and "demand", the axes "price" and "quantity", and the crossing point |

### ela

| # | module_id/slug | word | verdict | why | fix or prompt |
|---|---|---|---|---|---|
| 261 | ela-1-text-features/icon | icon | FIX | a star next to a gray bar does not show a small picture standing for something | a toolbar row of three familiar icons (house, trash can, magnifier), each in a small rounded square |
| 270 | ela-2-author-s-purpose/explain | explain | FIX | a cloud, rain, sun and a smile-shaped arrow do not read as "tell how or why" | cause and effect chain: cloud with rain, arrow, puddle, with a small "why?" bubble over the arrow |
| 275 | ela-2-grammar-and-spelling/apostrophe | apostrophe | FIX | a lone red comma shape; an apostrophe on its own is indistinguishable from a comma (the comma card uses the same shape) | show it in a word, as the contraction card does: "can't" or "Sam's" with the apostrophe in red, raised above the baseline |
| 279 | ela-2-grammar-and-spelling/pronoun | pronoun | FIX | three empty circles say nothing about he, she or they | show a name box "Sam" with an arrow to "he" (or the words he, she, they in three colored boxes) |
| 288 | ela-2-story-structure-and-point-of-view/problem | problem | PAINT | a kite with a question mark is puzzling, not "trouble in a story" | simple flat illustration of a red kite tangled high in the bare branches of a tall tree, string dangling, no text, no people |
| 291 | ela-2-word-building/shades-of-meaning | shades of meaning | FIX | three arrows of different lengths do not show words that mean almost the same | a word ladder: warm, hot, boiling in boxes shaded light to dark orange |
| 293 | ela-3-5-academic-and-subject-words/prefix | prefix | FIX | two empty boxes and a plus show no word parts | fill them: "re-" + "do" (or "pre-" + "view"), like the other prefix cards |
| 299 | ela-3-5-readers-theater-and-fluency/syllable | syllable | FIX | four empty colored boxes; nothing is a syllable | split a word into syllables: "but" "ter" "fly" in three colored boxes, with clap marks or dots under each |
| 313 | ela-3-opinion-and-informative-writing/linking-word | linking word | FIX | two joined puzzle pieces (the same picture as teamwork) show no linking word | keep the two pieces but write a short idea on each ("It rained" / "we stayed in") with "because" on the joint |
| 317 | ela-3-text-structure-and-search-tools/keyword | keyword | FIX | the search bar is empty, so there is no keyword in the picture | type one word into the search box (for example "volcano") and highlight it |
| 342 | ela-4-writing-with-evidence/linking-words | linking words | FIX | "rain" chained to "puddle" shows a link but no linking word | put the linking word itself between them: "rain" "so" "puddle" (or "because"), with the linking word highlighted |
| 368 | ela-5-reasons-and-evidence/statistic | statistic | FIX | an unlabeled pie chart, so there is no number in the picture | label the wedge "1 in 3" (or 33%) in large text |
| 392 | ela-6-connotation-and-context/nuance | nuance | FIX | two almost identical blue squares; the difference vanishes in black-and-white print and says nothing about meaning | three word boxes with close meanings shaded light to dark: "slim", "thin", "skinny" |
| 418 | ela-7-comparing-authors/purpose | purpose | FIX | a yellow warning triangle says "danger", not why an author writes | three small icons in a row for inform, persuade, entertain (lightbulb, megaphone, smiling face) or the target used on the other purpose card |
| 425 | ela-7-evaluating-arguments/sufficient | sufficient | FIX | a short bar and a tall bar with no target, so "enough" has nothing to be measured against | add a dashed "needed" line; the short bar stops below it (red X) and the tall bar reaches it (green check) |
| 427 | ela-7-fiction-vs-history/alter | alter | FIX | a calendar with one day crossed out reads as "cancel" or a date, not "to change" | a shape changing into another: a square, an arrow, the same square with its color and corners changed |
| 481 | ela-k-words-and-sentences/capital | capital | FIX | the red capital T is drawn as a separate item with a wide gap, so it reads "T he cat ran." | draw the sentence as one text run with the T colored (a tspan), no gap |

### eld

| # | module_id/slug | word | verdict | why | fix or prompt |
|---|---|---|---|---|---|
| 493 | eld-3-5-explaining-my-solution/solution | solution | FIX | "8 + 5" over a bar over "13" looks like a fraction | write it on one line, "8 + 5 = 13", with the 13 boxed in red (or a proper vertical sum with the + at the left) |
| 494 | eld-3-5-explaining-my-solution/strategy | strategy | FIX | a tape bar with a pencil does not read as a plan | a short numbered plan card: 1, 2, 3 with check marks, next to a puzzle piece or a question mark |
| 512 | eld-k-2-classroom-language/help | help | FIX | two sideways shapes read as oven mitts, not asking for help | a raised hand icon next to a speech bubble with a question mark (or "help?") |
| 517 | eld-k-2-classroom-language/turn | turn | FIX | a speech bubble with a star does not say "your time to go" | two seats or tokens with a curved arrow passing from one to the other, the second one highlighted |

### health-pe

| # | module_id/slug | word | verdict | why | fix or prompt |
|---|---|---|---|---|---|
| 530 | health-pe-3-5-germs-and-disease-prevention/germ | germ | FIX | a white shopping-bag shape with green specks; the bag reads as an object, not germs | replace the bag with a magnifier showing small germ blobs on a hand or a doorknob outline |
| 538 | health-pe-3-5-the-human-body-systems/circulatory-system | circulatory system | FIX | the red and blue vessels cross in an X behind the heart, so it reads as a crossed-out heart | draw the vessels leaving the top of the heart and branching up and out (red arteries, blue veins), never crossing behind it |
| 539 | health-pe-3-5-the-human-body-systems/muscles | muscles | PAINT | a red dome with a line is unreadable as a muscle | simple flat illustration of a bent upper arm cut-away showing the red biceps muscle attached to the white arm bones, no text, no people |
| 542 | health-pe-3-5-the-human-body-systems/skeletal-system | skeletal system | PAINT | a stick-figure skeleton with tangled ribs is crude and hard to read | simple flat illustration of a friendly cartoon human skeleton standing front view, clear skull, ribs, spine, arm and leg bones, plain white background, no text |
| 550 | health-pe-6-8-healthy-relationships/conflict-resolution | conflict resolution | FIX | the two hand shapes read as oven mitts | use handshake() under the two arrows meeting |
| 552 | health-pe-6-8-healthy-relationships/respect | respect | FIX | two mitten-like hands side by side say nothing about respect | handshake() between two speech bubbles, or a heart between two equal figures |
| 557 | health-pe-6-8-sport-skills-and-rules/sportsmanship | sportsmanship | FIX | two sideways mitten shapes, unreadable as a handshake | use handshake() with a small trophy or ball beside it |
| 569 | health-pe-k-2-food-groups/balanced-meal | balanced meal | PAINT | a four-color pie is a chart, not a meal | simple flat illustration of a dinner plate seen from above divided into vegetables, fruit, grains and protein, with a glass of milk beside it, no text, no people |

### library

| # | module_id/slug | word | verdict | why | fix or prompt |
|---|---|---|---|---|---|
| 588 | library-6-8-is-it-reliable/lateral-reading | lateral reading | FIX | three tiny empty browser windows in a row, with no sign of leaving one site to check others | draw them larger: one window in front with arrows out to two others, each with a check or magnifier |

### math

| # | module_id/slug | word | verdict | why | fix or prompt |
|---|---|---|---|---|---|
| 607 | math-1-addition-and-subtraction-stories/subtract | subtract | FIX | 9 red balloons, then an up arrow over 6 orange balloons: it reads as 6 flying away from a different group, so the take-away is unclear | 9 balloons in one color with 3 of them drifting up and away (faded or crossed), and "9 - 3 = 6" under them |
| 639 | math-1-telling-time-to-the-half-hour/hour-hand | hour hand | FIX | both hands are the same black, so nothing points out which one is the hour hand | color the short hand (for example orange) and leave the long hand dark; keep 7 o'clock |
| 640 | math-1-telling-time-to-the-half-hour/minute-hand | minute hand | FIX | at 12:00 the hour and minute hands lie on top of each other, so the long hand cannot be told apart | set a time like 3:00 or 9:00 and color the long hand |
| 641 | math-1-telling-time-to-the-half-hour/o-clock | o'clock | FIX | 12:00 hides one hand under the other; the card is about the minute hand being on 12 | use 3 o'clock (or 7 o'clock) so both hands show, minute hand on 12 highlighted |
| 670 | math-10-modeling-with-geometry/optimization | optimization | FIX | three containers side by side; nothing marks the best design or the limit it was chosen under | add a dashed size limit line and a star on the one container that fits it best |
| 684 | math-10-right-triangle-trigonometry/cosine | cosine | FIX | hyp and adj are labeled but the reference angle is not marked, so "adjacent" has nothing to be adjacent to | add an angle arc with a theta at the bottom-left vertex (angles=(0,) in triangle()) |
| 686 | math-10-right-triangle-trigonometry/sine | sine | FIX | hyp and opp are labeled but the reference angle is not marked, and the "opp" label touches the side | mark the angle theta at the bottom-left vertex and move the "opp" label clear of the red side |
| 688 | math-10-right-triangle-trigonometry/tangent | tangent | FIX | the "opp" label runs into the red side, and the reference angle is not marked | move "opp" right of the side, add the theta arc at the bottom-left vertex |
| 693 | math-10-rigid-motions-and-congruence/rigid-motion | rigid motion | FIX | the rotated triangle is drawn bigger than the original, which contradicts "keeps size and shape" | draw both triangles at the same scale (rotate a copy of the same triangle() item instead of a raw polygon at another size) |
| 698 | math-10-similarity/proportion | proportion | FIX | the equal sign touches the fraction bar of x/10, so it reads as one long bar | add a gap on both sides of "=" in eq() (or space the fractions apart) |
| 722 | math-11-exponential-and-logarithmic-functions/logarithmic-scale | logarithmic scale | FIX | the scale is a thin strip in a mostly empty card and the minor ticks blur together | draw it two to three times larger, fewer minor ticks, and add "x10" hop arcs between 1, 10, 100, 1000 |
| 727 | math-11-polynomial-functions/remainder-theorem | remainder theorem | FIX | "f(x) / (x - 2)" alone does not state the theorem | add a second line: "remainder = f(2)", with the 2 colored in both places |
| 734 | math-11-rational-expressions-and-equations/least-common-denominator | least common denominator | FIX | the plus sign runs into the fraction bars (same eq() spacing problem as proportion), and 1/4 + 3/4 already share a denominator, so nothing is found | add spacing around operators in eq(); use 1/4 + 1/6 with a "12" highlighted as the least common denominator |
| 752 | math-11-trigonometric-functions/phase-shift | phase shift | FIX | the shifted copy sits almost on top of the original, so the shift is hard to see | shift the orange wave by about a quarter period and add a short horizontal arrow between matching peaks |
| 753 | math-11-trigonometric-functions/unit-circle | unit circle | FIX | the "180" label sits on the circle line | move the 180 degree label outside the circle (left of it), like the 0 degree label |
| 760 | math-12-applications-of-integrals/displacement | displacement | FIX | the dashed path loops back to the start, so the picture suggests zero displacement and never shows the net change | end the path away from the start and draw a solid straight arrow from start to end labeled as the displacement |
| 793 | math-12-functions-and-their-graphs/interval-of-increase | interval of increase | FIX | the green bar floats below the vertex and stops short, so it does not mark where the function rises | draw the green interval on the x-axis from the vertex x-value to the right edge, with an arrowhead, and color the rising part of the curve green |
| 797 | math-12-limits-and-continuity/discontinuity | discontinuity | FIX | a vertical segment joins the open and closed dots, so the graph looks connected and the jump is hidden | remove the vertical connector; leave the open dot at the end of one piece and the closed dot at the start of the other |
| 801 | math-12-limits-and-continuity/squeeze-theorem | squeeze theorem | FIX | the blue curve leaves the gray bounds near both edges, which breaks the "trapped between" idea | scale the blue curve (for example x^2 sin(1/x)) so it stays between the two gray curves everywhere on the window |
| 814 | math-12-polar-coordinates-and-complex-plane/de-moivre-s-theorem | De Moivre's theorem | FIX | only the right side of the theorem is shown, so it is not a rule | show the whole identity: [r(cos theta + i sin theta)]^n = r^n(cos n theta + i sin n theta), on two lines if needed |
| 825 | math-12-sampling-and-experiments/response-bias | response bias | FIX | a speech bubble with a rising red arrow does not show answers being skewed by how a question is asked | a survey card with a leading question mark and answer boxes, most tick marks piled in one box, a red tilt arrow beside it |
| 829 | math-12-sampling-distributions/sampling-variability | sampling variability | FIX | scattered dots around one dashed line do not show a statistic changing from sample to sample | three small dot plots stacked, each with its own mean marker at a slightly different spot, a dashed line for the true value through all three |
| 835 | math-12-the-derivative/differentiable | differentiable | FIX | it shows the absolute value graph y = abs(x) with the point at its corner, which is exactly where a function is NOT differentiable | show a smooth curve with a tangent line at the marked point; if the corner is kept, label it with a red X as the counterexample |
| 838 | math-12-the-derivative/quotient-rule | quotient rule | FIX | the fraction bar runs into the equal sign (eq() spacing) | add space between "=" and the fraction in eq() |
| 851 | math-12-vectors/dot-product | dot product | FIX | "· = 0" floats with no vectors named, so the equation reads as a stray dot | write "a · b = 0" and label the two perpendicular arrows a and b |
| 867 | math-2-hundreds-tens-and-ones/expanded-form | expanded form | FIX | in "345" only the 5 is colored, so the digits do not match their parts (300 green, 40 blue) | color the 3 green and the 4 blue in 345 to match 300 and 40 |
| 877 | math-2-line-plots-and-bar-graphs/line-plot | line plot | FIX | the definition says X marks but the plot uses dots | draw X marks stacked above the numbers |
| 878 | math-2-line-plots-and-bar-graphs/title | title | FIX | the title bar over the graph is an empty dark strip, so there is no title to see | write a short title in it, for example "Our Pets", in white text |
| 884 | math-2-rulers-and-units/centimeter | centimeter | FIX | a small ruler in a mostly empty card, with the "cm" label colliding with the ticks and no single centimeter marked | draw the ruler larger, shade the space from 0 to 1 and label it "1 cm", move "cm" clear of the ticks |
| 891 | math-2-time-and-money/quarter-past | quarter past | FIX | the minute hand runs over the 3 and the hour hand over the 10, so the numbers the card is about are covered (clock() draws hands longer than the numeral ring) | in clock(): stop the minute hand short of the numerals (or move the numerals out toward the rim); applies to every clock card |
| 896 | math-2-two-step-word-problems/tape-diagram | tape diagram | FIX | the two parts 20 and 10 are shown but not the whole, so the bar model is half a problem | add a bracket over the whole bar labeled 30 (or "?") |
| 923 | math-3-perimeter/side | side | FIX | the whole outline is red, so no single side is singled out | draw the triangle dark and only one side thick red (hl_side=0) |
| 924 | math-3-perimeter/width | width | FIX | the arrow runs up the right edge, which shows height, not width | put a horizontal double arrow along the top or bottom edge |
| 930 | math-3-rounding-and-multi-digit-operations/nearest-ten | nearest ten | FIX | a dot at 82 with no arrow, so which ten is nearest is not shown | add an arrow from the dot to 80 and circle 80 |
| 933 | math-3-rounding-and-multi-digit-operations/round | round | FIX | a dot at 47 with nothing showing where it rounds to | add an arrow from 47 to 50 and circle 50 |
| 938 | math-3-scaled-graphs/line-plot | line plot | FIX | the definition says X marks but the plot uses dots | draw X marks stacked above the numbers |
| 948 | math-4-adding-and-multiplying-fractions/decompose | decompose | FIX | 5 boxes with 3 orange become just 3 boxes, so the other part is lost | split the 5-bar into a 3-part and a 2-part group below it |
| 949 | math-4-adding-and-multiplying-fractions/improper-fraction | improper fraction | FIX | loose quarter pieces with no wholes, so 9/4 being more than one whole does not show | draw quarters inside circle outlines (two full circles plus one quarter) with 9/4 beside them |
| 955 | math-4-angles-and-line-plots/degree | degree | FIX | the 360 label sits on the inner circle arc | move the label below the circle or shrink the arc marker |
| 956 | math-4-angles-and-line-plots/line-plot | line plot | FIX | the definition says Xs but the plot uses dots | draw X marks stacked above the numbers |
| 963 | math-4-decimals/place-value | place value | FIX | the hundredths header text overflows its box | widen the columns or shrink the header font |
| 981 | math-4-measurement-conversions/convert | convert | FIX | two unlabeled rulers (0-12 and 0-36) do not show what is being converted | label them 1 ft = 12 in and 1 yd = 36 in, or show 1 ft = 12 in with an equals sign |
| 988 | math-4-multi-digit-multiplication-and-division/partial-products | partial products | FIX | 80 and 12 boxes with no side labels, so the factors never appear | label the sides 20 + 3 and 4 and add 80 + 12 = 92 below |
| 999 | math-4-number-patterns/rule | rule | FIX | a lone +4 arrow has no terms, so there is no next term to get | show 3, 7, 11, 15 with +4 hops between them |
| 1005 | math-4-place-value-to-a-million/round | round | FIX | a dot near 4800 with nothing showing where it rounds to | add an arrow from the dot to 5000 and circle 5000 |
| 1012 | math-5-adding-unlike-fractions/simplify | simplify | FIX | the equals sign runs into both fraction bars | add spacing around the = in eq() |
| 1036 | math-5-operations-with-whole-numbers-and-decimals/reasonable | reasonable | FIX | a question mark and a check do not show checking an answer | show 4.9 x 3 = 14.7 next to the estimate 15 with a check |
| 1039 | math-5-patterns-and-relationships/ordered-pair | ordered pair | FIX | the point has no (3, 5) label, so the pair itself is missing | label the point (3, 5) and add dashed guides to each axis |
| 1045 | math-5-powers-of-ten-and-decimals/place-value-chart | place value chart | FIX | an empty chart whose headers are cramped and spill out of their boxes | put digits in the cells (for example 3.142) and widen columns or shrink header text |
| 1047 | math-5-powers-of-ten-and-decimals/round | round | FIX | a dot near 2.62 with nothing showing where it rounds to | add an arrow from the dot to 2.6 and circle it |
| 1048 | math-5-powers-of-ten-and-decimals/thousandths | thousandths | FIX | the ones, tenths and hundredths headers are pale text on pale fill and unreadable | use the strong header colors as in 963 and fade the cells instead |
| 1049 | math-5-the-coordinate-plane/axis | axis | FIX | both axes drawn the same with no labels, so no single axis is picked out | draw one axis thick red and label it x |
| 1051 | math-5-the-coordinate-plane/coordinates | coordinates | FIX | the star has no (4, 2) label, so the pair of numbers never appears | label the star (4, 2) with dashed guides to each axis |
| 1055 | math-5-units-and-line-plots/convert | convert | FIX | a lone cm ruler shows no change of unit | show 1 m = 100 cm or a cm ruler beside an inch ruler with an equals sign |
| 1056 | math-5-units-and-line-plots/line-plot | line plot | FIX | the definition says Xs but the plot uses dots | draw X marks stacked above the numbers |
| 1062 | math-6-area-surface-area-and-volume/area | area | FIX | the triangle with a dashed height teaches height, not area | fill the triangle or a rectangle with square units and label the count |
| 1068 | math-6-dependent-and-independent-variables/dependent-variable | dependent variable | FIX | an arrow labeled y pointing at a dollar sign does not show depending on an input | show x -> rule box -> y with y highlighted, or hours worked -> pay |
| 1071 | math-6-dependent-and-independent-variables/independent-variable | independent variable | FIX | a clock and an x arrow do not read as the input you choose | show x -> rule box -> y with x highlighted |
| 1075 | math-6-dividing-fractions/how-many-groups | how many groups | FIX | two equal three-part bars do not show how many divisor groups fit | show a 3/4 bar with 1/8 pieces marked off and count 6 groups |
| 1077 | math-6-dividing-fractions/quotient | quotient | FIX | two shaded bars with no numbers do not show the result of a division | show 12 / 3 = 4 with the 4 highlighted, or 12 dots in 3 groups of 4 |
| 1093 | math-6-negative-numbers/integer | integer | FIX | a bare number line with nothing marked | put dots on every integer, or circle a positive and a negative one |
| 1111 | math-6-statistical-variability/range | range | FIX | the range label and bracket run into the stacked dots at 3 and 4 | raise the bracket above the tallest stack |
| 1112 | math-6-statistical-variability/statistical-question | statistical question | FIX | a plain bar chart does not show a question that expects varied answers | show one question mark fanning out to several different answer bars, or pair it with a dot plot of varied answers |
| 1127 | math-7-equivalent-expressions/combine-like-terms | combine like terms | FIX | the + and = signs are jammed between the boxes | add spacing around the operators |
| 1148 | math-7-proportional-relationships/proportion | proportion | FIX | the equals sign runs into both fraction bars | add spacing around the = in eq() |
| 1169 | math-8-exponents-roots-and-scientific-notation/cube-root | cube root | FIX | an unlabeled 3x3x3 cube never shows the root or the value | label one edge 3 and add 27 cubes, cube root of 27 = 3 |
| 1197 | math-8-the-pythagorean-theorem/converse | converse | FIX | a 5-12-13 triangle shows the Pythagorean theorem, not flipping a statement around | show P -> Q above Q -> P with the swapped parts colored, or keep the triangle and add the two arrows |
| 1205 | math-8-transformations/rotation | rotation | FIX | the second flag looks like a hanging banner and no turn center is marked | rotate the same flag 90 degrees about a marked dot with a curved arrow |
| 1210 | math-8-volume-of-cylinders-cones-and-spheres/volume | volume | FIX | the r label sits on the rim of the cylinder | move r above the top ellipse |
| 1212 | math-9-creating-equations/define-a-variable | define a variable | FIX | the equals sign runs into the word hours | add spacing around the = |
| 1233 | math-9-polynomial-arithmetic/binomial | binomial | FIX | the + sign is jammed between the two boxes | add spacing around the operator |
| 1238 | math-9-polynomial-arithmetic/trinomial | trinomial | FIX | the + signs are jammed between the three boxes | add spacing around the operators |
| 1241 | math-9-quadratic-equations/root | root | FIX | two dots on bare axes with no curve, so nothing is being solved | draw a parabola crossing the x-axis at the two dots |
| 1245 | math-9-rational-exponents-and-real-numbers/closure | closure | FIX | a circle with a turning arrow does not show an operation staying inside a set | label the circle whole numbers and show 2 + 3 = 5 landing inside it |
| 1249 | math-9-rational-exponents-and-real-numbers/rational-exponent | rational exponent | FIX | the equals sign runs into the root symbol | add spacing around the = |
| 1259 | math-9-structure-of-expressions/equivalent-form | equivalent form | FIX | the equals sign is jammed between the two boxes | add spacing around the = |
| 1265 | math-9-systems-of-equations/feasible-region | feasible region | FIX | the overlap region is barely a different shade from the two half-planes | give the overlap a strong fill or outline and fade the rest |
| 1271 | math-9-units-and-quantities/unit-conversion | unit conversion | FIX | the times sign runs into the fraction bar | add spacing around the operators in eq() |
| 1272 | math-k-build-a-shape/build | build | PAINT | a flat house shape reads as house, not as putting pieces together | simple flat illustration of colorful building blocks being stacked into a small tower, one block mid-air about to land, no text, no people |
| 1277 | math-k-counting-to-100/count | count | FIX | a row of ten dots with no numbers does not show saying numbers in order | put 1 to 10 under the dots, or show a count arrow moving along them |
| 1291 | math-k-more-less-same/less | less | FIX | 2 dots and 4 dots with neither marked, so which is less is not shown | circle or highlight the group of 2 |
| 1293 | math-k-more-less-same/more | more | FIX | 5 dots and 3 dots with neither marked, so which is more is not shown | circle or highlight the group of 5 |

### science

| # | module_id/slug | word | verdict | why | fix or prompt |
|---|---|---|---|---|---|
| 1315 | science-1-sound-and-vibration/soft | soft | PAINT | a speech bubble of dots does not say quiet | simple flat illustration of a small cat tiptoeing on a soft rug past a sleeping puppy, no text, no people |
| 1330 | science-10-chemical-reactions-and-equations/chemical-equation | chemical equation | FIX | a single small line of formula leaves the card mostly empty and the subscripts tiny | scale the equation up and wrap it onto two lines, or add molecule pictures under each formula |
| 1332 | science-10-chemical-reactions-and-equations/decomposition-reaction | decomposition reaction | FIX | one water molecule becomes H2 and O2, so the atoms do not balance | start with two water molecules (2H2O -> 2H2 + O2) |
| 1341 | science-10-nuclear-chemistry/beta-particle | beta particle | FIX | motion lines and a dot with no nucleus do not show release by decay | add a nucleus on the left with the electron (labeled e-) flying out of it |
| 1362 | science-11-energy-and-work/work | work | FIX | an up arrow on a resting box shows force but no distance moved | show the box lifted to a second position with a dashed distance arrow beside the force arrow |
| 1364 | science-11-gravity-and-electrostatics/coulomb-s-law | Coulomb's law | FIX | the same picture as charge (1363) and no distance is shown | show two charge pairs, close with long arrows and far with short arrows |
| 1384 | science-12-ecosystems-and-biomes/biome | biome | FIX | the map colors continents, not biomes, which is misleading | color by biome bands (green forest, yellow desert, white tundra) or show three small landscape tiles |
| 1390 | science-12-engineering-for-global-challenges/tradeoff | tradeoff | FIX | an empty balanced scale does not show giving up one thing for another | put a different item on each pan, one side rising, with an arrow swapping them |
| 1408 | science-4-structures-and-senses/reflect | reflect | FIX | light passes straight through the apple to the eye, so nothing bounces back | draw a mirror with an incoming ray and a bounced ray at equal angles |
| 1413 | science-5-earth-s-spheres/system | system | FIX | overlapping circles read as a Venn diagram, not parts working together | draw three or four parts linked by arrows in a loop, or meshing gears |
| 1415 | science-5-food-webs-and-matter-cycles/food-web | food web | FIX | plain lines with no arrowheads, so the direction of eating is lost | add arrowheads pointing from food to eater (grass -> rabbit -> fox) |
| 1420 | science-5-matter-is-made-of-particles/conservation-of-mass | conservation of mass | FIX | two identical empty balanced scales with an arrow show no change happening | put reactant blocks on one scale and the same blocks rearranged on the other, both level |
| 1429 | science-6-cells-and-body-systems/organelle | organelle | FIX | the labels float beside the cell with no leader lines | add leader lines from each label to its part |
| 1434 | science-6-climate-and-ocean-circulation/ocean-current | ocean current | FIX | thin red arrows scattered over the map are hard to read | use fewer, thicker arrows following one or two big gyres |
| 1435 | science-6-climate-and-ocean-circulation/prevailing-winds | prevailing winds | FIX | every arrow points east at every latitude, but the trade winds blow west | make the tropics arrows point west and the middle latitudes east |
| 1455 | science-6-water-cycle-and-weather/front | front | FIX | a lone front symbol with no air masses on either side | add a cold blue mass on one side and a warm red mass on the other |
| 1463 | science-7-matter-and-energy-in-ecosystems/carbon-cycle | carbon cycle | FIX | the arrows run tree -> air, so the main flow (air into trees by photosynthesis) points the wrong way | reverse the loop to air -> tree -> soil -> air |
| 1465 | science-7-matter-and-energy-in-ecosystems/food-web | food web | FIX | plain lines with no arrowheads, so who eats whom is lost | add arrowheads from food to eater (plants -> mouse -> owl) |
| 1468 | science-7-photosynthesis-and-respiration/chloroplast | chloroplast | FIX | a whole plant cell with no chloroplast singled out | highlight one green chloroplast with a ring and fade the rest |
| 1479 | science-8-evolution-and-natural-selection/homologous-structures | homologous structures | PAINT | thin colored sticks do not read as limbs with shared bones | simple flat illustration of a bat wing, a whale flipper and a cat front leg side by side, matching bones colored the same in each, no text, no people |
| 1480 | science-8-forces-and-motion/acceleration | acceleration | FIX | a car with speed lines shows speed, not a change in speed | show the car at several positions with the gaps between them growing |
| 1494 | science-9-cell-division-and-differentiation/cell-cycle | cell cycle | FIX | a pie chart with no circular arrow or stage names does not read as a cycle | add a circular arrow around it and short stage labels (grow, copy DNA, divide) |
| 1526 | science-9-genetics-and-inheritance/dominant | dominant | FIX | a lone letter B does not show it winning over b | show the pair Bb with the trait it produces (for example a brown eye) and the b faded |
| 1534 | science-9-homeostasis/stimulus | stimulus | FIX | two nearly identical eyes do not show a change triggering a response | show a bright sun -> eye with a big pupil -> the same eye with a small pupil |
| 1541 | science-9-photosynthesis-and-cellular-respiration/calvin-cycle | Calvin cycle | FIX | a bare loop arrow does not show carbon dioxide going in or sugar coming out | add CO2 entering the loop and a glucose hexagon leaving it |

### sel

| # | module_id/slug | word | verdict | why | fix or prompt |
|---|---|---|---|---|---|
| 1562 | sel-3-5-perspective-taking/respect | respect | FIX | two hands drawn as oven mitts | use handshake() or a different symbol |
| 1576 | sel-k-2-calm-down-strategies/count | count | FIX | five dots with no numbers do not show saying numbers in order | put 1 to 5 under the dots |
| 1577 | sel-k-2-calm-down-strategies/stretch | stretch | PAINT | two green arrows do not read as stretching a body | simple flat illustration of a cat stretching long with its front paws reaching forward, no text, no people |

### social-studies

| # | module_id/slug | word | verdict | why | fix or prompt |
|---|---|---|---|---|---|
| 1591 | social-studies-1-timelines-and-me/year | year | FIX | a single month grid reads as month, not year | show 12 small month blocks in a 3x4 grid |
| 1593 | social-studies-12-brain-and-behavior/cerebral-cortex | cerebral cortex | FIX | the same brain as amygdala (1592) with no outer layer singled out | outline the outer wrinkled rim in a strong color and fade the inside |
| 1618 | social-studies-5-colonial-economies/enslaved | enslaved | FIX | a broken chain reads as freedom, the opposite of the word | use an unbroken heavy chain (or a closed shackle), no break |
| 1619 | social-studies-5-colonial-economies/triangular-trade | triangular trade | FIX | the trade arrows are tiny and the triangle is hard to see | draw three thick arrows forming a clear triangle between Europe, Africa and the Americas |
| 1622 | social-studies-5-the-constitution-and-bill-of-rights/rights | rights | FIX | the same shield and star as brave (1605), so the two cards look identical | use a distinct symbol, such as a scroll or a raised open hand |
| 1623 | social-studies-6-ancient-rome/empire | empire | FIX | the empire is a tiny red patch on Italy that is hard to see | zoom the map to the Mediterranean and shade the full empire |
| 1624 | social-studies-6-five-themes-of-geography/absolute-location | absolute location | FIX | a globe with lines but no marked spot | put a pin where one latitude and one longitude line cross |
| 1637 | social-studies-7-medieval-asia/mongol-empire | Mongol Empire | FIX | the empire is a crude orange rectangle over Asia | use the real outline shape or a zoomed map of Asia with the empire shaded |
| 1643 | social-studies-8-motion-on-the-floor/second | second | FIX | cards 1 and 2 read as the number second, not seconding a motion | show a motion card with one check, then a second check added beside it |
| 1647 | social-studies-8-the-early-republic/monroe-doctrine | Monroe Doctrine | FIX | the stop hand is drawn as an oven mitt | use a clear stop-sign hand or an octagon stop sign beside the map |
| 1653 | social-studies-9-imperialism/scramble-for-africa | Scramble for Africa | FIX | an abstract blob does not read as Africa | use the real Africa outline with the colonial borders drawn on it |
| 1655 | social-studies-9-revolutions-and-enlightenment/separation-of-powers | separation of powers | FIX | one building with columns does not show power split into branches | draw three separate small buildings or three linked boxes |
| 1657 | social-studies-k-my-place-in-the-world/map | map | FIX | rows of yellow boxes under a green bar read as a calendar or keyboard | draw a simple top-down map with a road, river, trees and houses |

### world-languages

| # | module_id/slug | word | verdict | why | fix or prompt |
|---|---|---|---|---|---|
| 1666 | world-languages-6-12-asl-grammar-and-facial-expression/fingerspelling | fingerspelling | FIX | handshapes read as mittens and fists | draw clearer handshapes for a short word, or reuse a proper hand glyph |
| 1672 | world-languages-6-12-classifiers-and-space/classifier | classifier | FIX | the hand is an oven mitt | use a flat-hand classifier glyph that reads as a hand (car or vehicle shape) |
| 1677 | world-languages-6-12-cultures-of-the-spanish-speaking-world/dialect | dialect | FIX | a single ¡Hola! bubble shows a language, not a regional form of one | show two bubbles with regional variants for the same thing (for example soda and pop) |
| 1697 | world-languages-k-12-family-and-home/mother | mother | PAINT | the same house and heart as family (1699), so mother is not shown | simple flat illustration of a mother bird feeding a chick in a nest, no text, no people |
| 1698 | world-languages-k-12-family-home-and-school/brother | brother | PAINT | two hands do not show a brother | simple flat illustration of two puppy brothers from the same litter playing together, no text, no people |
| 1702 | world-languages-k-12-family-home-and-school/sister | sister | PAINT | two hands do not show a sister | simple flat illustration of two kitten sisters from the same litter curled up together, no text, no people |
| 1705 | world-languages-k-12-fingerspelling-and-the-manual-alphabet/fingerspell | fingerspell | FIX | the handshapes read as mittens and fists | draw clearer handshapes, or reuse a proper hand glyph |
| 1706 | world-languages-k-12-fingerspelling-and-the-manual-alphabet/handshape | handshape | FIX | one big oven mitt stands for a handshape | draw a clear open-hand shape with separate fingers |
| 1708 | world-languages-k-12-fingerspelling-and-the-manual-alphabet/manual-alphabet | manual alphabet | FIX | the same four mitten-like shapes repeat, so no alphabet is shown | show a few distinct letter handshapes, each with its letter beneath (A, B, C) |
| 1713 | world-languages-k-12-greetings-and-introductions-in-asl/hello | hello | FIX | the hand is an oven mitt | draw a clear waving open hand |
| 1715 | world-languages-k-12-greetings-and-introductions-in-asl/nice-to-meet-you | nice to meet you | FIX | two hands drawn as oven mitts | use handshake() or two clear open hands facing each other |
| 1720 | world-languages-k-12-greetings-and-introductions/please | please | FIX | a leaf-like outline does not read as a hand or a sign | draw a clear flat hand on the chest with a circular arrow |
| 1726 | world-languages-k-12-numbers-colors-and-time/day | day | FIX | the same month calendar as month (1722), so a single day is not singled out | circle one square as in today (1724) |
| 1732 | world-languages-k-12-school-and-daily-routine/o-clock | o'clock | FIX | the hour hand sits on the 12 numeral | shorten the hands or pick 3:00 so no numeral is covered |
| 1736 | world-languages-k-12-the-five-parameters-of-a-sign/movement | movement | FIX | two oven mitts with motion lines | draw clear open hands with a curved movement arrow |

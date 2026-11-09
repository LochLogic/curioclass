# Bug Hunt

## One idea
You are the bird: peck the moths you can see on tree bark, the ones you miss breed, and over fourteen generations
the bark goes from lichen to soot and back while your own histogram and line graph show the dark form rise and fall,
because no moth ever changed color: the moths already differed, and the ones that blended in lived to breed.

## Not like
- membrane-gatekeeper (grade 9 arcade): reflexes serve transport rules inside one cell. Here reflexes are the
  selective force on a whole population, and the score is only a side effect of looking carefully.
- tree-of-life (grade 9 explorer): shared ancestry across deep time and many species. Here one species, a few
  generations, one trait, selection you cause yourself.
- gene-pool (grade 8 simulator): heredity, clones and seedlings, breeding on purpose for a trait. Here nobody
  chooses the parents; an environment does, through a predator.
- punnett-predictor (grade 9 simulator): predicted crosses against simulated offspring. Here genes stay in the
  background (one dominant dark copy) and the student watches a population, not one cross.
- fossil-and-bone-bench (grade 8 lab): fossils, limb bones and embryos (MS-LS4-1 to 4-3 moved there, per the idea
  card). Nothing here about fossils or anatomy.
- carrying-capacity (grade 9 simulator): population size against food. Here the size is held at 30 or 200 and only
  the mix of colors changes.
- The idea card's pooled class histogram is dropped: pooling needs counts moved between devices by hand (STANDARDS
  Scope). Pairs compare screens instead; the lesson plan says so.

## Who and how
Grade 8, science, module Evolution and Natural Selection. Driver: students, one laptop each (pairs fine). 20 to 30
minutes: Hunt about 7, Run 5 to 10, Explain 5, Real story 5. Standards: MS-LS4-4, MS-LS4-6 (MS-LS4-1, 4-2, 4-3 moved
to fossil-and-bone-bench). Prompts are not personal; no disclosure note needed. Light 6-8 theme set by the tool.
Header: title, `.seg` modes **Hunt**, **Run**, **Explain**, **Real story**, kit buttons `motion`, `sound`, `read`.

## Standards map
| Code | Student action | What they see | Done when check |
|---|---|---|---|
| MS-LS4-4 (explanation from evidence: genetic variation raises some individuals' odds of surviving and reproducing) | In Explain, picks the one explanation that fits their graph from three, then writes three sentences (variation, survival, inheritance), each starting from an evidence chip with their own numbers | Feedback on each wrong card naming why it fails; their own counts from Hunt (or Run) in the chips | The two wrong cards are refused with their reasons; each chip inserts numbers equal to that generation's histogram and line graph values |
| MS-LS4-6 (math representation of a trait increasing and decreasing over generations) | Reads the histogram (wing darkness, 10 bins) and the line graph (% dark form by generation, bark band underneath) every generation in Hunt; in Run plays History and, with Predict on, pins the generation where half are dark | Bars sliding toward the bark marker; the line rising over the soot band and falling over the clean band | Every generation, histogram total = population and dark bins (70 to 100) = the line's value; Run History rises above 50% during soot and falls below 50% in the clean stretch (see Sources) |

## Screens and modes
**On load:** Hunt, generation 1, lichen bark full-stage with 30 moths resting on it, the great tit cutout watching
from the lower left, timer ring frozen at 25 s, histogram and line graph (one point) in the panel. Nothing moves.
Hint: "<b>Hunt.</b> You are a hungry bird. Tap a moth to start eating. Up to 15 before the time runs out." The first
tap on a moth eats it and starts the clock; a first tap on bare bark is a miss (it also starts the clock). Mode
buttons switch at once. The welcome may be cut by that first tap (BASELINE 16); its content lives in the hint.

**Hunt.** Focus: the bark and its moths, the biggest thing on screen (stage about 900 x 700 at 1366x768, the panel
440 wide on the right). Panel top to bottom: "Generation 3 of 14", bark name and darkness ("Soot, darkness 85"),
eaten "7 / 15" and timer ring, histogram (400 x 170), line graph (400 x 150), buttons **Pause** and **Restart hunt**,
`hint`, `tip`. All of it above the fold at 1366x768. At 680x425 the stage keeps at least 60% of the width; the panel
shows generation, eaten and timer on one line, then one graph box with a two-button switch **Bars | Line** (Bars
first), then Pause; Restart hunt and the tip fold below. A round ends when 15 are eaten or the clock hits 0. Then the
breeding beat (2.5 s, instant with Motion off): eaten spots stay empty, survivors pulse, 30 young fade in at new
places, the histogram bars grow to the new counts and the line adds a point. Any tap during the beat finishes it at
once (a tap on a moth then counts as the first peck of the next round). The next round waits for the first peck.
Before generation 3 and before generation 9 a story card covers the stage (painted scene, two sentences, **Continue**);
the bark crossfades to soot or back to lichen as it closes (1.5 s; instant with Motion off). After generation 14's
round the end card: their line graph large, one sentence on what happened (two versions, Content), **Explain**,
**Run**, **Hunt again**.
What the picture shows: lichen bark with pale moths nearly invisible and dark ones stark; soot bark with the reverse.
At the end: if the dark form peaked at 15 or more, the end card's line shows the hill; if not, the line stays low and
the card says so honestly.

**Run** (computer birds, 200 moths). Focus: the line graph (stage bottom, 900 x 330, x generations 0 to 60, extends
to 120 by rescaling, y "% dark form" 0 to 100, bark band under the axis) with a bark strip above it (900 x 300, the
current bark with 40 moths drawn as a sample in the same mix as the 200). Panel: histogram of 200 with the bark
marker, **Bark** slider (darkness 0 to 100, ticks Lichen 20, Clearing 50, Soot 85), **Birds** on/off, **New dark
copies** on/off (mutation), **Play** / **Pause**, **Step**, **Speed** 1x (3 generations a second) or 2x, **History**
(plays 5 lichen, 25 soot, 25 clean generations, 55 in all, about 18 s at 1x), **Predict** on/off, **Reset**. All above
the fold at 1366x768; at 680x425 the bark strip shrinks to 120 tall, the histogram folds behind **Bars | Line**
like Hunt, and Speed and Predict fold below. While Play or History runs every control stays live: moving the slider
changes the bark picture and the band at once and the very next generation uses it (History then stops scripting and
says "History paused: you took the bark"); Birds off takes effect the next generation. Predict on: before Play, drag a
pin along the x axis to the generation you expect half to be dark; after, the pin shows "you: 12, run: 15".

**Explain.** Focus: the sorter, then the three sentence boxes, center stage, with the student's line graph small
beside them. Step 1, three cards (Content); tap one. Step 2 opens after the right card: three boxes labeled
**Variation**, **Survival**, **Inheritance**, each with an evidence chip button (**Use my numbers**) that inserts a
sentence with their numbers which they then edit. Uses the latest Hunt; if none, the latest Run; if neither, the chips
read "Play Hunt or Run first" and stay disabled. **Copy** puts all three sentences on the clipboard. Text saves on
this device; the line under the boxes says "Saved on this device only. It never leaves it." Fits 1366x768 without
scrolling (each box 3 lines); at 680x425 the graph folds away and the boxes page one at a time (**Back**, **Next**).

**Real story.** An explorer, no score. Focus: the painted scene for the selected stop (860 x 400, 16:9). Under it a
timeline row of eight stop buttons (Content). Panel: the stop's card text and a small chart "Dark peppered moths near
Manchester" with only the sourced points (rare in 1848, about 98% by the 1890s) and a down arrow labeled "falling
since the 1960s to 1970s"; no line is drawn between points ("not measured every year here"). Stop 8 adds a second
mini chart: the student's own Hunt line (if any) beside it, labeled "Your 14 generations".

## Content
**Darkness scale (one scale everywhere):** wing or bark darkness = 100 minus CIE lightness L* of the average pixel
as drawn. The builder measures each painted bark and tints it to darkness 20 (lichen), 50 (clearing), 85 (soot), and
draws each moth with the cutout tinted to its own darkness. Histogram bins 0-9 ... 90-100, each bar filled with its
own gray, count above it; the bark marker is a triangle on the x axis labeled "bark".
**Moths:** each has two copies of the color gene (pale or dark; one dark copy makes the dark form) and a speckle value
0 to 1. Darkness: pale form 5 + 40 x speckle, dark form 78 + 20 x speckle.
**Hunt model:** 30 moths. Start (seeded, fixed per page load and on Restart): 29 pale-pale, speckle drawn from normal
(0.42, 0.15) clipped 0 to 1; 1 with one dark copy, speckle 0.6. Bark: generations 1-2 lichen (20), 3-8 soot (85),
9-14 lichen (20). Round: 25 s or 15 eaten. Breeding: 30 young; parent A runs through the survivors in shuffled order
(so every survivor has at least one young), parent B is a random survivor; one gene copy from each at random; speckle =
parents' mean + normal(0, 0.08), clipped. New dark copies: the 8th young born into generation 2, the 4th into 3, the
19th into 4, the 10th into 5, the 22nd into 7 and the 13th into 10 gets a dark copy from parent A (six in 420 births).
Incomer: the last young of every generation is replaced by a pale-pale moth from nearby woods (speckle normal(0.42,
0.15)). Miss: a tap on bark that hits no moth freezes pecking for 1.0 s (bird flinches). Moths: 46 to 56 px long at
1366x768, seeded rotation within plus or minus 25 degrees, at least 60 px apart, fully inside the stage, never under
the bird's 130 x 130 corner.
**Run model:** 200 moths, same genes and darkness. Each generation the birds take 100, chosen by weighted draw without
replacement, weight 0.2 + (|moth darkness minus bark darkness| / 100) squared. Breeding as Hunt to 196 young, plus 4
incomers (each has a dark copy with chance 1 in 10). New dark copies on: each pale copy passed on becomes dark with
chance 1 in 500. Birds off: nobody is eaten; all 200 breed.
**Model limits line (Hunt end card, Run panel, notes):** "Game numbers. Real birds eat a smaller share, so in England
the change took decades, not a few rounds. Real dark copies were far rarer: one change, around 1819."
**Story cards in Hunt:** Before generation 3 (bh-story-mill): "Years pass. Coal smoke coats the trees in soot, and the
pale lichen dies off. The bark turns dark." Before generation 9 (bh-story-clean): "Clean air laws cut the smoke. Rain
washes the soot off, and lichen starts to grow back."
**Hunt end card:** if the dark form reached 15 or more of 30 in any of generations 3 to 8: "Your dark moths went from
{a} of 30 to {peak} of 30 on soot, then down to {end} on clean bark. No moth changed color. The population did."
Otherwise: "Your dark moths only reached {peak} of 30 this time. Chance matters in a small population. Try Run to see
200 moths."
**Explain cards** (shuffled order; right one is b):
- a. "Each moth darkened its own wings to match the sooty bark." Refusal: "No moth changed. Every moth kept its
  darkness for life; look at your bars: the new dark moths were born dark."
- b. "Some moths were already darker. Birds found fewer of them on soot, so more of them bred and passed on their
  color." Right: "That's natural selection: variation, survival, inheritance."
- c. "Soot stained the moths, and the stain passed to their young." Refusal: "A stain isn't in the genes, so it can't
  pass to young. Only gene copies pass on."
**Evidence chips** (Hunt numbers; Run uses "of 200"): Variation: "In generation 1, wing darkness ran from {min} to
{max}, and {d1} of 30 moths were the dark form." Survival: "In generation {g}, on {bark} bark, I ate {p} pale moths
and {d} dark ones." (g = the soot generation with the most eaten; their round data) Inheritance: "The dark form went
from {x} of 30 in generation 3 to {peak} of 30 in generation {gp}, because dark parents had dark young."
**Real story stops** (scene; card text):
1. "Before 1819" (bh-story-wood): "Peppered moths rest on tree bark by day. Most were pale with dark speckles, hard to
   see on bark covered in pale lichen."
2. "About 1819" (bh-story-wood, a code inset of one gene strip): "Moth DNA dates the change that makes the dark form to
   around 1819: a jumping piece of DNA landed in a gene called cortex. One dark copy makes a dark moth."
3. "1848" (bh-story-mill): "A collector in Manchester caught the first recorded dark peppered moth."
4. "1890s" (bh-story-mill): "Coal smoke darkened the bark with soot, and pollution killed many pale lichens. By the end
   of the 1800s, about 98 in 100 peppered moths near Manchester were dark."
5. "1950s" (bh-story-branch): "Bernard Kettlewell released moths in polluted woods near Birmingham and clean woods in
   Dorset. Birds took more of whichever form stood out."
6. "1956" (bh-story-clean): "Britain's Clean Air Act made towns cut smoke. From the 1960s and 1970s on, the dark form
   fell steadily. Dark moths in Michigan, USA, rose and fell the same way."
7. "Debate" (bh-story-clean): "Scientists agree that less soot mattered. How much returning lichen mattered is still
   argued: in Michigan the dark form fell even where lichen had not come back."
8. "2001 to 2007" (bh-story-branch): "Michael Majerus watched 4,864 released moths in Cambridge. Birds ate more of the
   dark ones, enough to explain why the dark form is fading."
**Hints:** Hunt: as on load; between rounds "Tap a moth to start generation {n}."; on a card "Read the card, then tap
Continue."; end "Tap Explain to say what happened, or Run to watch 200 moths." Run: "<b>Run.</b> Set the bark with the
slider, then press Play. Or press History." Explain: "<b>Explain.</b> Tap the card that fits your graph." then "Tap
Use my numbers in each box, then make each sentence your own." Real story: "<b>Real story.</b> Tap a year on the
timeline."
**Tips (rotate):** "A moth near the bark marker on the histogram is hard to see." / "Nobody chose the parents. The
moths you missed did the breeding." / "One dark copy makes a dark moth, so pale copies can hide inside dark moths." /
"With Birds off, the bars only wander."

## Interactions in detail
- Peck by pointer (tap or click), or keyboard: a crosshair moved with the arrow keys (40 px steps, Shift 10 px) and
  Space or Enter to peck. Moths are not in the tab order and get no focus ring (a ring would give them away). The
  crosshair has its own visible focus ring.
- Eat: moth vanishes with a small feather puff (static puff with Motion off), soft chirp; the bird cutout switches to
  its peck pose for 0.3 s. Miss: low thud, bird pose flinch, pointer grayed for 1.0 s; taps then do nothing. At 15
  eaten: bird switches to its full pose, the round ends.
- A round with 0 eaten (time runs out): the event line "No moths eaten, so every moth bred. Nothing chose." plays;
  breeding proceeds.
- Pause (button, P, or window blur) stops the clock and blurs the stage so moths can't be studied while paused.
- Restart hunt: `V.hush()`, same seed, generation 1. Mode switch pauses Hunt where it is; returning resumes paused.
- Run: Step does one generation (also while paused). Play stops at 120 generations ("Reset to run again"). Reset
  returns 200 pale moths with no dark copies, bark 20, Birds on, New dark copies on. With Birds off and New dark
  copies off, a run only drifts; the line stays near its start (Sources).
- Extremes: slider at 0 or 100 works (pale moths at 100 are found fast); bark 50 favors neither form strongly and the
  dark form stays near 1% (Sources). Hunt can never wipe out the moths (at least 15 survive).
- Explain text is kept in localStorage `bug-hunt-explain` inside try/catch; Copy uses the clipboard API with a
  select-the-text fallback.

## Look
Light 6-8 field-notebook theme on `:root`: `--paper #f3efe4`, `--panel #ffffff`, `--ink #1f2a24`, `--muted #55615a`,
`--line #d3cbb8`, `--focus #9a3d12`, accent `--brand #8b4a6a` (dusk mauve, the color of a moth-wing shadow; white text
on it). Graph line in brand, 3 px, with a point marker per generation; bark band: each generation's cell filled with
that bark's gray and labeled "lichen", "soot" or "clearing" in ink or white, whichever passes. Contrast (computed):
ink on paper 12.92, on panel 14.84; muted on paper 5.63; brand on paper 5.51, on panel 6.33; white on brand 6.33;
focus on paper 5.99; white on the darkest bar (#262626) 15.13; ink on the palest bar (#e8e4da) 11.69. Nearest accent
in any tool spec or build is dE 18.9 (#592439); every science neighbor's accent is 48 or more away. The moth colors
are the game and are not tuned for contrast; every graph labels values in text, so color is never the only signal.

## Art
Local FLUX, no people. House style: natural-history painting, close and real, soft daylight, rich but quiet color,
no lettering.
- bh-bark-lichen: close view of an old oak trunk's bark covered in pale gray-green crusty and leafy lichen, even soft
  light, full frame texture; 16:10; cutout no; people no; Hunt and Run background (tinted to darkness 20).
- bh-bark-clearing: the same kind of oak bark, dark gray with rain streaks and small patches of young pale lichen;
  16:10; no; no; Run around darkness 50 (the slider crossfades the three barks).
- bh-bark-soot: oak bark coated in black soot, bare of lichen, dull sooty gray-black; 16:10; no; no; darkness 85.
- bh-moth-typica: a peppered moth seen from above, wings spread flat as at rest, creamy white with fine black
  speckles, on a plain light background; 4:3; cutout yes; no; every pale moth (tinted per speckle).
- bh-moth-carbonaria: the same moth and pose, wings an even sooty black, on a plain light background; 4:3; cutout yes;
  no; every dark moth.
- bh-bird-watch, bh-bird-peck, bh-bird-full: a great tit perched on a twig in side view (watching; leaning forward
  with beak open; feathers fluffed round and content); 1:1; cutout yes; no; Hunt's lower-left corner, 130 px, fully
  inside the stage in every size, poses as in Interactions.
- bh-story-wood: a quiet English oak woodland in the early 1800s, trunks pale with lichen, soft morning light; 16:9;
  no; no; Real story stops 1 and 2.
- bh-story-mill: an 1800s English mill town under smoky skies, tall brick chimneys, soot-blackened walls and dark
  tree trunks in the foreground; 16:9; no; no; Hunt card before generation 3, stops 3 and 4.
- bh-story-clean: the same town decades later, clear blue sky, clean brick, green trees with lichen returning on the
  trunks; 16:9; no; no; Hunt card before generation 9, stops 6 and 7.
- bh-story-branch: a pale peppered moth and a dark one resting under a mossy branch in a garden at dawn; 16:9; no; no;
  stops 5 and 8.
Graphs, crosshair, timer ring, feather puff, gene strip and timeline stay in code.

## Voice
Bank `casual-peer`, restyled "Say casually and naturally, like a teen birder showing a friend a cool trick" (no
neighbor in this group uses it). `Curio.voice`, scope = mode. How lines speak once per page load, then hint only.
- welcomeHunt (how; entering Hunt; stale once a moth is eaten): "You're a hungry bird. Tap a moth to start eating.
  Up to fifteen before the time runs out."
- miss (how; first miss; stale after 3 s): "That was bark. A miss spooks you for a second, so look before you peck."
- breed (how; first breeding beat; stale when the next round starts): "The moths you missed are the parents. Their
  young get their colors. Watch the bars."
- nextGen (how; first wait for generation 2; stale on the next peck): "Tap a moth to start the next generation."
- sootCard (event; once per hunt, before generation 3; whole; Continue waits for it): the card text.
- cleanCard (event; once per hunt, before generation 9; whole; Continue waits): the card text.
- noneEaten (event; each round that ends with 0 eaten; stale on the next peck): "No moths eaten, so every moth bred.
  Nothing chose."
- huntEnd (event; each hunt end; whole): the end card sentence with its numbers, then "Tap Explain to say what
  happened."
- welcomeRun (how; entering Run; stale once Play, Step or History is pressed): "Run lets birds hunt for you. Set the
  bark with the slider, then press Play and watch the line."
- history (how; first History; stale when it ends): "History plays clean bark, then soot, then clean air again."
- historyTaken (event; slider moved during History; once per History run): "History paused. You took the bark."
- welcomeExplain (how; entering Explain; stale once a card is tapped): "Tap the card that fits your graph."
- cardRight (event; stale when a box is edited): the card b reply. cardWrong (event; once per card per visit): its
  refusal.
- chips (how; after the right card; stale on the first chip tap): "Tap Use my numbers in each box, then make each
  sentence your own."
- welcomeStory (how; entering Real story; stale once a stop is tapped): "Tap a year on the timeline to see what
  really happened to England's peppered moths."
- stop1 to stop8 (event; each stop tap; stale when another stop is tapped): the stop's card text.
No line names Continue unless a card is up, or a chip when chips are disabled.

## Family engine
none

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| The dark form's mutation is a transposable element in the gene cortex, dated to about 1819 | van't Hof et al., Nature 534:102-105 (2016), abstract | Univ. of Liverpool news, "Jumping gene took peppered moths to the dark side", 2016-06-01 | yes |
| First recorded dark peppered moth, Manchester, 1848 | Wikipedia, "Peppered moth evolution" (Edleston, reported 1864) | Univ. of Liverpool news 2016 | yes |
| About 98% dark near Manchester by the end of the 1800s | Wikipedia, "Peppered moth evolution" (98% in 1895) | ASU Ask A Biologist, peppered moths game, "Natural Selection" (98% by 1900 near cities); Cook and Saccheri, Heredity 110:207 (2013) (typical nearly lost) | yes on "end of the 1800s"; the exact year differs, so the tool says "by the end of the 1800s" |
| Soot darkened bark; pollution killed many pale lichens | Wikipedia, "Peppered moth evolution" (sulphur dioxide killed lichens) | Cook and Saccheri 2013 (industry changes epiphyte cover); Cook et al., Biol. Lett. 8:609 (2012) (soot-darkened bark) | yes |
| One dark copy makes a dark moth (dominant, one gene) | Cook and Saccheri 2013 (Bowater 1914, dominant alleles at one locus) | Wikipedia, "Peppered moth" (melanic allele dominant) | yes |
| Kettlewell, 1950s, Birmingham (polluted) and Dorset (clean): birds took the conspicuous form | Wikipedia, "Peppered moth evolution" (75% of white eaten in Birmingham, 86% of dark in Dorset) | Cook and Saccheri 2013 (Kettlewell's 2:1 results) | yes (percentages not shown on screen: one source) |
| Clean Air Act, UK, 1956 | legislation.gov.uk, Clean Air Act 1956 c.52 | Wikipedia, "Clean Air Act 1956" | yes |
| Dark form fell from the 1960s and 1970s on | Wikipedia (fallen steadily since about 1962) | Cook et al. 2012 ("since 1970 a rapid reversal") | yes on direction; start differs, so "1960s and 1970s" |
| Michigan's dark moths rose and fell the same way | Grant, Owen and Clarke, J. Heredity 87:351 (1996) | Cook and Saccheri 2013 (American decline at similar rates) | yes |
| Lichen's part in the fall is debated | Grant et al. (Michigan: allele change without perceptible lichen change) | Wikipedia (fall correlated with lichen return, typica camouflaged on lichen) | they disagree; the tool says so (stop 7) |
| Majerus, Cambridge 2001-2007, 4,864 moths, more dark ones eaten, enough to explain the decline | Cook et al. 2012 (PMC3391436, Table 2, s about 0.1 a day) | Wikipedia, "Peppered moth evolution" (4,864 moths, published 2012) | yes |
Claims: 11 backed twice (one is a stated disagreement). Cut for one source only: Cambridge yearly frequencies
(0.12 to 0.01), Wirral 25.8% in 1991, "6% by 2001", Kettlewell percentages, a dark specimen before 1811, one
generation a year (so no years on Hunt or Run axes), Edleston's name on screen.
Number checks (Python, scratch S:/CurioClass-codex-scratch/specs/bug-hunt/, 2000 seeded runs each):
- Hunt (`hunt_final.py`), dark moths of 30 by generation 0 to 14, scripted players (careful = eats 15 a round by
  weighted draw 0.05 + contrast squared, about 9:1 for the plainest moth): careful median 1,1,1,3,5,8,14,20,24,21,14,
  4,0,0,0; peak 15+ on soot in 87%, ends at half its peak or less in 96%, both 83%. Wrong behaviors: idle (eats 0)
  peak 15+ in 2.4%; masher (2 eaten a round, misses freeze) 2.9%, score 2 a round vs careful 15; random eater 8%;
  "eat only camouflaged" 0%, median ends 12 dark (reverse selection). Without incomers or with uneven breeding, the
  lone dark moth was lost too often (peak 15+ in 54 to 75%); both fixes are in Content.
- Run (`run5.py`, 400 runs, History): dark % median (p10 to p90) at generation 5: 0.5 (0 to 1); 10: 6.5 (1 to 18.5);
  15: 44.5 (9 to 75.5); 20: 87.5 (50 to 94); 30: 96.5 (93.5 to 98); 35: 85.5 (68.5 to 93.5); 40: 27 (2 to 70.5);
  45: 0.5 (0 to 4.5). Never rose above 50% in soot: 0.25%. Stuck above 90% at the end: 0%. Birds off, generation 30:
  7.5 (2 to 15.5). Bark 50 for 40 generations: 1 (0 to 4). Without incomers 22.5% of runs stuck fully dark and never
  fell (the pale copy was lost), so incomers are required.
- Colors: WCAG ratios and dE in `colors.py` (Look).

## Done when
1. Focus: at 1366x768 and 680x425 the bark with its moths is the largest thing in Hunt, and the line graph with the
   bark strip in Run; every control each mode needs is above the fold at 1366x768 with no page scroll.
2. On load nothing moves; the first tap on a moth eats it and starts the 25 s clock; a first tap on bark is a miss.
3. A scripted careful player over 50 seeded hunts gets the dark form to 15+ in about 85% and back to half its peak or
   less in about 95%; an idle player rarely (under 5%); a masher eats about 2 a round.
4. Every generation, histogram counts sum to 30 (or 200), bins 70 to 100 equal the line's value, and the bark marker
   sits at the bark's darkness; the measured darkness of each bark is within 3 of 20, 50 and 85.
5. A tap while anything plays: a tap during the breeding beat finishes it at once; moving the slider during Play or
   History changes the bark and band at once and the next generation uses it.
6. Run History (Birds on, both toggles on) passes 50% during soot and drops under 50% by the end in at least 9 of 10
   seeded runs; Birds off stays under 25%.
7. Explain: cards a and c are refused with their reasons, b opens the boxes; each chip's numbers match the
   graphs of the hunt they came from; text survives a reload and the privacy line shows.
8. Real story shows only the sourced points, no connecting line, and stop 7 states the lichen disagreement.
9. Keyboard: the crosshair hunt works with arrows and Space; moths never take focus.
10. Each how line speaks once in five repeated actions; sootCard and cleanCard play whole before Continue acts;
    no line names a disabled control.
11. All 12 images load from the bundle; no network; no em dashes; the model limits line shows in Hunt end, Run and notes.

## Open questions
none

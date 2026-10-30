# Design the Study

## One idea
You write the methods section for a real-feeling experiment (does an energy drink speed up reaction time?), a skeptical
journal editor sends it back with one flaw named each time, and every flaw you leave in shows up as its own colored bar
in the result: the gamers you let choose, the practice from the second session, the timer who knew. The true effect is
small (10 ms), so only a design that removes every bar can find it.

## Not like
- poll-workshop (gr 11, sampling family): who you ask and how many in a survey. Here no survey and no sampling frame: assignment, control, placebo and blinding in an experiment. The two tools hand off at S-IC.B.3.
- courtroom-statistics (gr 12, same group): judges finished evidence. Here you build the study that makes the evidence.
- sample-machine (gr 12, same group): what random sampling does to a statistic. Here what random assignment does to a comparison.
- science lab tools with "fair test" variables (gr 5 to 8): one variable changed by the student. Here people as subjects, with lurking traits, expectations and a biased measurer.

## Who and how
- Grade 12, Statistics, Math: statistics. Students drive, alone or in pairs. 20 to 40 minutes (one Story run is about 15).
- Topic line: "experiments: random assignment, control and blinding".
- Standards (module): S-IC.B; AP-STAT.U3.
- CCSS clusters: Story serves S-IC.B.3 (experiment versus observational study, and why randomization matters), S-IC.B.5 (the shuffle check: is a difference between treatments bigger than chance?) and S-IC.B.6 (the editor's letters judge a reported study). Bench serves S-IC.B.5. S-IC.B.4 (margin of error from a survey) is left to poll-workshop; see Open questions.
- AP-STAT.U3 (Collecting Data): the experiment half (3.5 to 3.7: experiments, confounding, control, placebo, blinding, blocking, matched pairs, random assignment and scope of inference). The sampling half (3.2 to 3.4) is poll-workshop's.
- tool.json: driver "students", minutes "20-40", modes ["Story", "Bench"], grades_label "Grade 12".

## Screens and modes
Header: title, subtitle "Can you find a 10 millisecond effect?" Modes `Story` (opens first), `Bench`. Kit buttons.
Layout: left, the manuscript (a paper sheet with a Methods section built from draft rows); right, the lab: the painted
reaction lab (art: reaction-lab) as a dimmed header strip, the 40 volunteer cards in an 8 by 5 grid, the result chart
under them. Chips that name a thing show its painted picture small beside the words: Water (art: water-glass), Look-alike
placebo and the drink (art: drink-can, the same can for both, since they look alike), Stopwatch (art: stopwatch),
Computer (art: reaction-box).

### Story
Focus: while drafting, the manuscript (left, the larger column); after `Run the study`, the result chart: the lab
column widens, the volunteer grid shrinks to a strip of small cards above it, and the waterfall (then the shuffle dot
plot) is the largest thing on the stage. Editing any row returns the focus to the manuscript.
1. The editor's opening letter (portrait, three sentences): a reader claims the drink makes people faster; design a
   study the journal can trust.
2. Draft: six rows in the Methods section (the six draft rows in Content), each a set of choice chips (see Content). Rows that don't apply gray out
   with a one-line reason ("With water as the control, volunteers can tell what they drank").
3. `Run the study`: cards flash as each volunteer is timed, all 40 within 1.5 s (instant with Motion off); the result
   is computed at once, so a tap on any control during the flashes (a row chip, Shuffle check, Submit) stops them and
   acts at once. Readouts: groups and their sizes,
   mean reaction time per group (or mean difference per person), the estimate in ms.
4. Result chart: a waterfall, from 0 to the estimate, with one bar per part (True effect, Expectation, Practice,
   Stopwatch bias, Gamer mix, Sleep mix, Chance). Bars are hidden as "?" until the editor's letter comes back; then the
   bars the editor named are uncovered, so the student sees the flaw cost in ms.
5. `Shuffle check` (its 1,000 dots drop in over at most 1.5 s; any tap during the drop shows all dots at once and
   acts): re-deals the group labels 1,000 times (or flips the sign of each person's difference for designs
   where everyone does both), draws the 1,000 results as a dot plot with the real estimate marked, and counts how many
   are at least as far from 0 as the real one. Readout: "34 of 1,000 at least this far out".
6. `Submit to the journal`: the editor replies (see Content: letters). Rejection returns to Draft with the named row
   outlined. Two more buttons after a rejection: `Revise` and `Skip the journal: post it online`.
7. Endings: Published, Pilot, Retracted. An ending card names the design and the endings found so far (3 badges);
   localStorage `curio-dts-endings`, try/catch, with `Clear`.

### Bench
Focus: the histogram of the 400 estimates with the dashed true-effect line, centered and large; pinned designs stack
under it on the same x axis. Same draft rows, no editor. `Run 400 studies` repeats the chosen design with 400 new seeds (same model, new random
person effects, new assignment) and draws a histogram of the 400 estimates with a dashed line at the true effect,
-10 ms (the 400 bars fill in over at most 1.5 s; a row change during it cancels the run and shows the new draft at
once). Readouts: mean estimate, SD of the estimates, share of runs the shuffle check would flag. Pin up to 3 designs
to compare side by side (same x axis). This is the bias versus spread picture: a biased design is centered in the
wrong place; a weak design is centered right but wide.

## Content
Setting (made up, labeled "made-up lab, made-up numbers"): the reaction lab at an invented university; 40 adult
volunteers aged 18 to 22; an unbranded energy drink. The editor is Dr. Mara Quill of The Open Bench Journal (invented).
A health note on the first screen: this is a study of adults; the American Academy of Pediatrics advises that children
and teens should not drink energy drinks.

Volunteer cards 1 to 40 (traits are hidden until a bar or the card back reveals them):
- Cards 1 to 12 are gamers: -30 ms. Cards 13 to 22 are short sleepers: +25 ms. Others: no trait.
- "Would choose the drink" if allowed: cards 1 to 10, 13 to 17, 23 to 27 (20 people).

Model for a recorded time (ms), seeded: 280 + trait + person effect u (normal, mean 0, SD 20, fixed per person)
+ drink -10 (the true effect) + expectation -15 (only if the volunteer knows they had the drink) + practice -15 (second
session only) + session noise (normal, SD 8). With stopwatch timing, add normal noise SD 30, and -12 for a drink
session if the timer knows who had the drink. Computer timing adds nothing.

Draft rows:
1. Compare: `Before and after` (everyone without, then with the drink) / `Two groups` / `Both days` (everyone does both, on two days).
2. Assignment (Two groups): `Volunteers choose` / `Researcher picks who looks tired` (drink group = the 10 short sleepers, then non-gamers in card order: cards 13 to 32) / `Random shuffle` / `Random within gamers` (gamers split 6 and 6 at random, others split at random). Assignment (Both days): `Drink on day 2` / `Random order, half each`.
3. Control drink: `Water` / `Look-alike placebo`.
4. Who knows: `Everyone` / `Volunteers don't` / `Neither volunteers nor timer` (double blind). The last two need the placebo.
5. Timing: `Stopwatch` / `Computer`.
6. Size: `20` (odd-numbered cards) / `40`.

Results the model gives (Python, 400 seeds, n = 40, computer timing unless noted; "flagged" = shuffle check two-sided, under 50 of 1,000):

| Design | Mean estimate (ms) | SD | Flagged |
|---|---|---|---|
| Before and after | -40.0 | 1.80 | |
| Before and after, stopwatch | -52.0 | 7.0 | |
| Two groups, volunteers choose, water | -37.1 | | |
| Two groups, researcher picks tired, water | +5.5 | | 8% |
| Two groups, random, water | -24.8 | | |
| Two groups, random, placebo, double blind | -9.8 | 9.4 | 18% |
| Two groups, random within gamers, placebo, double blind | -10.2 | 7.6 | |
| Both days, drink on day 2, placebo, double blind | -25.0 | | |
| Both days, random order, placebo, double blind | -9.9 | 1.80 | 99% (64% at n = 20) |

Exact mix bars (they depend only on who is in which group):
- Volunteers choose, n = 40: groups 20 and 20; Gamer mix -30 × (10/20 - 2/20) = -12.0; Sleep mix 25 × (5/20 - 5/20) = 0.
- Researcher picks tired, n = 40: Gamer mix -30 × (0 - 12/20) = +18.0; Sleep mix 25 × (10/20 - 0) = +12.5.
- Volunteers choose, n = 20: groups 11 and 9; Gamer mix -30 × (5/11 - 1/9) = -10.30; Sleep mix 25 × (3/11 - 2/9) = +1.26.
- Random within gamers: Gamer mix 0 by construction.
- Expectation bar = -15 × (share of drink sessions where the volunteer knew). Practice bar = -15 × (share of drink sessions on day 2 minus share of control sessions on day 2). Stopwatch bias = -12 when the timer knew. Chance = the estimate minus every other bar.

Editor letters (one flaw per letter, the first in this order that applies; each names the row):
1. Before and after: "Day 2 is also the day they've practiced. Your drink and your practice arrive together."
2. Volunteers choose: "Your volunteers picked their own group. Whatever made them pick may also make them fast."
3. Researcher picks: "You chose who got the drink. Nobody, including you, should choose."
4. Water control: "Your volunteers knew what they drank. Expecting to be faster can make people faster."
5. Timer knows (stopwatch, not double blind): "Your timer knew who had the drink. That's a thumb on the stopwatch."
6. Stopwatch (double blind): "A human thumb adds 30 ms of noise to a 10 ms question."
7. Drink on day 2: "Everyone had the drink on the second day. Practice is still riding along."
Then, for a design with no flaw: shuffle check flagged gives Published ("Accepted. Random assignment, a placebo, and
nobody knowing: this is what a fair test looks like."); not flagged gives Pilot ("Sound design, but chance could
explain this. Bigger, or have everyone do both days."). `Skip the journal: post it online` after a rejection gives
Retracted: a replication by another lab (a fresh run of the best design) finds about -10 ms and the post's headline
claim comes down.

## Interactions in detail
- Seeds from the time unless the URL has `?seed=n`. A run uses one seed for person effects, assignment and noise.
- Estimate: mean(drink group) - mean(control group) for Two groups; mean of (drink time - control time) per person for
  Before and after and Both days. Negative means faster with the drink.
- Shuffle check: 1,000 re-deals with the same seed stream; count of |shuffled| ≥ |estimate|. Paired designs flip signs
  of the differences instead of re-dealing labels. The editor's line: under 50 of 1,000.
- The waterfall bars are computed from the model's known parts for that run, and they sum exactly to the estimate
  (Chance is the remainder). Bars carry their value as text, so color is never the only signal.
- Volunteer cards: tap a card to flip it after a run (shows trait, group, times). Keyboard: arrows move across cards.
- `Random order, half each` gives exactly half the volunteers (shuffled) the drink on day 1, never a coin flip per
  person.
- Bench pins persist for the session only. `Clear` empties pins and endings.
- `window.__tool = {state, setMode, seed(n), setDraft(obj), run(), shuffle(k), bench(k), bars()}`.

## Look
Light manuscript theme overriding kit/theme-912.css tokens (see Open questions): paper `#f3eee2`, panel `#fbf7ee`,
sections `#fffdf8`, ink `#2a2723`, muted `#6a6358`, button line `#8a7f6a`, header `#ece5d4`, ok `#1e6b3a`, warn
`#9b1c1c`, focus `#0b7285`. Accent `--brand #1d5bbf` (the editor's blue pencil): the editor's margin notes and outlines.
Serif for the manuscript, kit sans for controls. Waterfall bars: True effect in the accent, every bias bar in warm
grays with a hatch pattern, Chance dotted.
Contrast (computed): ink on panel 13.9:1; muted on sections 5.84:1; brand on panel 5.95:1, on sections 6.26:1, on paper
5.49:1; white on brand 6.36:1; header text 11.84:1; focus 5.22:1; button line 3.88:1 (non-text); ok 6.42:1; warn 8.02:1.
Minimal celebration: Published is a stamped "Accepted" in the accent, no confetti.

## Art
Local FLUX (`scripts/localart.py`) unless marked people. One style: flat editorial illustration, clean shapes, soft
shading, warm paper colors with the editor's blue.
- editor-quill: "Chest-up portrait of a sharp-eyed woman in her fifties with short dark hair streaked with gray and
  round tortoiseshell glasses, wearing a dark blazer over a white collar, holding a blue pencil over a paper manuscript
  whose lines are plain gray strokes, a dry, kind expression, flat editorial illustration, plain warm paper
  background"; 1:1; cutout yes; people: true (Gemini, `scripts/art.py`, Cory reviews; the 2026-10-27 Codex image is
  replaced, see Open questions); the opening letter, every rejection letter and the ending cards.
- reaction-lab: "A small university lab room with a desk holding a reaction-time button box and a monitor with a plain
  glowing blank screen, a shelf of binders with blank spines, a clock on the wall with no hands, soft daylight, flat
  editorial illustration"; 16:9; cutout no; people no; dimmed header strip of the lab column and the preview.
- drink-can: "A single slim drink can with a plain matte silver body and a blank band around the middle, beads of cold
  water on it, soft light, flat editorial illustration, plain white background"; 3:4; cutout yes; people no; the drink
  and the Look-alike placebo chips, and the drink group's label on the chart.
- water-glass: "A clear glass of water with a few ice cubes, soft light, flat editorial illustration, plain white
  background"; 3:4; cutout yes; people no; the Water chip and the control group's label when water is the control.
- stopwatch: "A silver mechanical stopwatch with a blank white face, soft light, flat editorial illustration, plain white
  background"; 1:1; cutout yes; people no; the Stopwatch chip and the Stopwatch bias bar's label.
- reaction-box: "A small black box with one large round red push button on top, a cable trailing from it, soft light,
  flat editorial illustration, plain white background"; 1:1; cutout yes; people no; the Computer chip.
Volunteers are numbered cards, never pictured. Cards, manuscript, waterfall, dot plots, histograms and stamps are drawn
in code (charts and labels).

## Voice
Bank voice `news-reader` (Rasalgethi; crisp and steady: the editor reading her letters). Not used by group siblings;
work-rate-crew (gr 11) also uses it (see Open questions). `Curio.voice`, `scope: () => state.mode`. The letters are
on screen in full; Read speaks the hint.
- wStory (how, Story welcome; stale once the first row chip is tapped): "I'm Mara Quill, editor. Tap one chip in each row of your methods, then press Run the study."
- shuffle (how, first finished run in Story; stale once Shuffle check is pressed): "Before you submit, press Shuffle check. It shows what chance alone would give."
- submit (how, first Shuffle check finished; stale once Submit to the journal is pressed): "Now press Submit to the journal, and I'll read it."
- letter (event, each rejection; stale on Revise or Skip the journal): reads that letter's text from Content, then "Press Revise to fix that row."
- published (event, Published ending; stale on a new Draft): "Accepted. This is what a fair test looks like."
- pilot (event, Pilot ending; stale on a new Draft): "Sound design, but chance could explain this. Try having everyone do both days."
- retracted (event, Retracted ending; stale on a new Draft): "Another lab ran it properly. The headline didn't survive."
- wBench (how, Bench welcome; stale after the first run): "Tap a chip in each row and press Run 400 studies. Watch where the results land compared with the dashed line."

## Family engine
none (its model and charts are its own; the shuffle check is ten lines).

## Sources
- S-IC.B: Common Core State Standards for Mathematics, Making Inferences and Justifying Conclusions, https://www.thecorestandards.org/Math/Content/HSS/IC/
- AP-STAT.U3: College Board, AP Statistics Course and Exam Description, Unit 3 "Collecting Data", https://apcentral.collegeboard.org/courses/ap-statistics
- Experiments, control, placebo, blinding, random assignment: OpenStax, Introductory Statistics 2e, 1.4 "Experimental Design and Ethics", https://openstax.org/books/introductory-statistics-2e/pages/1-4-experimental-design-and-ethics
- Randomization (shuffle) tests: OpenIntro Statistics 4e, 2.3 "Case study: using randomization to analyze an experiment", https://www.openintro.org/book/os/
- Energy drinks and children: American Academy of Pediatrics, Committee on Nutrition and Council on Sports Medicine and Fitness, "Sports Drinks and Energy Drinks for Children and Adolescents: Are They Appropriate?", Pediatrics 127(6):1182-1189, 2011, https://doi.org/10.1542/peds.2011-0965
- The lab, the volunteers, the model and every number are made up; the table above was recomputed in Python (400 seeds) on 2026-10-27.
- Checks run again (Python, numpy, 2026-10-29): the model rebuilt from Content, 400 seeds with 1,000 shuffles each
  and 4,000 seeds for the spreads. Means: before and after -40.0, with stopwatch -52.0 (exactly -40 - 12 in the
  model), volunteers choose -37.1, researcher picks +5.0 to +5.5, random water -24.9, random double blind -9.9,
  within gamers -9.7 to -10.0, drink on day 2 -25.0, random order -9.9. Flagged shares: researcher picks 7%, random
  double blind 18%, random order 98% (64% at n = 20). Spreads: before and after 1.80 and random order 1.80 (theory
  8 × √2 / √40 = 1.79), random double blind 9.4, within gamers 7.6, stopwatch 7.0. The first draft's SDs 1.66, 1.78,
  9.5 and 7.4 and the stopwatch mean -52.4 were small sampling slips; the table now gives the steadier values. Random
  order must give exactly half the people the drink on day 1: a coin flip per person lets practice leak in and the SD
  grows to 3.1. Mix bars: volunteers choose -12.0 and 0 (n = 40), groups 11 and 9 with -10.30 and +1.26 (n = 20);
  researcher picks cards 13 to 32, +18.0 and +12.5.

## Done when
1. With `?seed=1`, the waterfall bars sum to the estimate exactly, and `bars()` returns them.
2. Volunteers choose, n = 40: Gamer mix reads -12.0 and Sleep mix 0.0; n = 20 gives groups 11 and 9, -10.30 and +1.26.
3. Researcher picks tired: drink group is cards 13 to 32; Gamer mix +18.0, Sleep mix +12.5.
4. Bench, 400 studies: each design's mean estimate is within 1.5 ms of the table, and Both days with random order has SD under 2.5.
5. Every rejection names the row and outlines it; Water greys out the two blinding chips with the reason shown.
6. The shuffle check count matches a recount from the run's data for a fixed seed; paired designs use sign flips.
7. All three endings reachable; badges survive reload; `Clear` clears them.
8. Focus: at 1366x768 and 1000x625 the manuscript is the largest thing while drafting, the waterfall (then the dot
   plot) after a run, and the histogram in Bench.
9. Tap while it plays: during the card flashes, the shuffle drop or the 400-study fill, a row chip, Shuffle check or
   Submit acts at once and the readouts match the new state.
10. Every chip that names a drink, water or a timer shows its picture; the only person pictured is the editor.
11. Every size in STANDARDS.md keeps the manuscript, Run button and chart visible without page scrolling; keyboard only works; console clean, no network.

## Open questions
- [design-the-study] Voice: news-reader is also work-rate-crew's (gr 11, listed as a neighbor). Every kept 9-12 voice is already used by a math 9-12 neighbor; the only free ones are the K-2 teachers and lively-host, which do not fit a dry journal editor. Keep news-reader, or take lively-host?
- [design-the-study] The editor portrait was redrawn in words: the old one (silver bun, reading glasses on a chain) matched fair-dice-investigation's librarian almost exactly. The new one needs Gemini and your review; the Codex image from 2026-10-27 is no longer used.
- [design-the-study] An energy drink study, even with adult volunteers and the AAP note, is it fine for a school audience? Fallback: caffeine-free "a song with a beat" versus silence, same model.
- [design-the-study] S-IC.B.4 (estimating with margin of error from a survey) and the sampling half of AP-STAT.U3 are left to poll-workshop. OK?
- [design-the-study] The light manuscript theme overrides the dark 9-12 theme. OK?

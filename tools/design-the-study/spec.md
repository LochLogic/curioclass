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
Layout: left, the manuscript (a paper sheet with a Methods section built from draft rows); right, the lab (40
volunteer cards in a 8 by 5 grid, the result chart under them).

### Story
1. The editor's opening letter (portrait, three sentences): a reader claims the drink makes people faster; design a
   study the journal can trust.
2. Draft: seven rows in the Methods section, each a set of choice chips (see Content). Rows that don't apply gray out
   with a one-line reason ("With water as the control, volunteers can tell what they drank").
3. `Run the study`: cards flash as each volunteer is timed (instant with Motion off). Readouts: groups and their sizes,
   mean reaction time per group (or mean difference per person), the estimate in ms.
4. Result chart: a waterfall, from 0 to the estimate, with one bar per part (True effect, Expectation, Practice,
   Stopwatch bias, Gamer mix, Sleep mix, Chance). Bars are hidden as "?" until the editor's letter comes back; then the
   bars the editor named are uncovered, so the student sees the flaw cost in ms.
5. `Shuffle check`: re-deals the group labels 1,000 times (or flips the sign of each person's difference for designs
   where everyone does both), draws the 1,000 results as a dot plot with the real estimate marked, and counts how many
   are at least as far from 0 as the real one. Readout: "34 of 1,000 at least this far out".
6. `Submit to the journal`: the editor replies (see Content: letters). Rejection returns to Draft with the named row
   outlined. Two more buttons after a rejection: `Revise` and `Skip the journal: post it online`.
7. Endings: Published, Pilot, Retracted. An ending card names the design and the endings found so far (3 badges);
   localStorage `curio-dts-endings`, try/catch, with `Clear`.

### Bench
Same draft rows, no editor. `Run 400 studies` repeats the chosen design with 400 new seeds (same model, new random
person effects, new assignment) and draws a histogram of the 400 estimates with a dashed line at the true effect,
-10 ms. Readouts: mean estimate, SD of the estimates, share of runs the shuffle check would flag. Pin up to 3 designs
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
| Before and after | -40.0 | 1.66 | |
| Before and after, stopwatch | -52.4 | | |
| Two groups, volunteers choose, water | -37.1 | | |
| Two groups, researcher picks tired, water | +5.5 | | 8% |
| Two groups, random, water | -24.8 | | |
| Two groups, random, placebo, double blind | -9.8 | 9.5 | 18% |
| Two groups, random within gamers, placebo, double blind | -10.2 | 7.4 | |
| Both days, drink on day 2, placebo, double blind | -25.0 | | |
| Both days, random order, placebo, double blind | -9.9 | 1.78 | 99% (64% at n = 20) |

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
- `editor-quill`: "portrait of a sharp-eyed woman in her sixties with silver hair in a low bun and reading glasses on a
  chain, holding a blue pencil over a manuscript, flat illustration, plain warm paper background, chest up"; 1:1;
  cutout yes; `people: true`; Codex (`scripts/gptart.py`), Cory reviews.
Everything else (cards, manuscript, waterfall, dot plots, histograms) is drawn in code. Volunteers are cards with
numbers, never pictured.

## Voice
Bank voice `news-reader` (crisp, formal: the editor reading her letters). Not used by math 9-12 neighbors or group siblings.
- wStory (how, Story welcome): "I'm Mara Quill, editor. Fill in each row of your methods, then press Run the study."
- wBench (how, Bench welcome): "Pick a design and press Run 400 studies. Watch where the results land compared with the dashed line."
- shuffle (how, first Run in Story): "Before you submit, press Shuffle check. It shows what chance alone would give."
- letter (event, each rejection; stale on Revise): reads the letter's text from Content.
- published (event, Published ending; stale on new Draft): "Accepted. This is what a fair test looks like."
- pilot (event, Pilot ending; stale on new Draft): "Sound design, but chance could explain this. Try having everyone do both days."
- retracted (event, Retracted ending; stale on new Draft): "Another lab ran it properly. The headline didn't survive."

## Family engine
none (its model and charts are its own; the shuffle check is ten lines).

## Sources
- S-IC.B: Common Core State Standards for Mathematics, Making Inferences and Justifying Conclusions, https://www.thecorestandards.org/Math/Content/HSS/IC/
- AP-STAT.U3: College Board, AP Statistics Course and Exam Description, Unit 3 "Collecting Data", https://apcentral.collegeboard.org/courses/ap-statistics
- Experiments, control, placebo, blinding, random assignment: OpenStax, Introductory Statistics 2e, 1.4 "Experimental Design and Ethics", https://openstax.org/books/introductory-statistics-2e/pages/1-4-experimental-design-and-ethics
- Randomization (shuffle) tests: OpenIntro Statistics 4e, 2.3 "Case study: using randomization to analyze an experiment", https://www.openintro.org/book/os/
- Energy drinks and children: American Academy of Pediatrics, Committee on Nutrition and Council on Sports Medicine and Fitness, "Sports Drinks and Energy Drinks for Children and Adolescents: Are They Appropriate?", Pediatrics 127(6):1182-1189, 2011, https://doi.org/10.1542/peds.2011-0965
- The lab, the volunteers, the model and every number are made up; the table above was recomputed in Python (400 seeds) on 2026-10-27.

## Done when
1. With `?seed=1`, the waterfall bars sum to the estimate exactly, and `bars()` returns them.
2. Volunteers choose, n = 40: Gamer mix reads -12.0 and Sleep mix 0.0; n = 20 gives groups 11 and 9, -10.30 and +1.26.
3. Researcher picks tired: drink group is cards 13 to 32; Gamer mix +18.0, Sleep mix +12.5.
4. Bench, 400 studies: each design's mean estimate is within 1.5 ms of the table, and Both days with random order has SD under 2.5.
5. Every rejection names the row and outlines it; Water greys out the two blinding chips with the reason shown.
6. The shuffle check count matches a recount from the run's data for a fixed seed; paired designs use sign flips.
7. All three endings reachable; badges survive reload; `Clear` clears them.
8. Every size in STANDARDS.md keeps the manuscript, Run button and chart visible without page scrolling; keyboard only works; console clean, no network.

## Open questions
- [design-the-study] An energy drink study, even with adult volunteers and the AAP note, is it fine for a school audience? Fallback: caffeine-free "a song with a beat" versus silence, same model.
- [design-the-study] S-IC.B.4 (estimating with margin of error from a survey) and the sampling half of AP-STAT.U3 are left to poll-workshop. OK?
- [design-the-study] The light manuscript theme overrides the dark 9-12 theme. OK?

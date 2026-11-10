# Jellybean Jar

## One idea
In a candy shop window sits a jar of 10,000 jellybeans and a contest card, "Guess the share of red beans", and the shopkeeper, Mr. Ito (made up, labeled "illustration"), hands the child a small scoop; in the bias round the jar was filled in layers, so a scoop off the unstirred top is almost all green, and the child stirs before scooping (random sampling) and explains when a sample stands for the whole jar; estimate rounds take a scoop of 20 (7 red, so 35%), predict the jar, then take 50 scoops and stack their estimates on a dot plot, and bigger scoops make a tighter pile, so the child states an estimate and how far off it might be; two-jar rounds set a second candy maker's jar beside the first, and the child samples bean weights from each, builds two dot plots on one scale, and judges the overlap by the difference in medians measured in MADs (maker B's beans sit about 2 MADs heavier, or hardly apart in another pair); at the reveal the shop counts the jar (30% red), and the child sees how close the sampled estimate came; at the end the child sees that a fair random sample can stand for a huge jar and that the spread of many samples tells how much to trust one, so a seventh grader learns to use random samples to draw inferences about a population, gauge the variation in estimates, and compare two populations informally.

## Not like
- carnival-odds (7, spec): probability of chance events. Here sampling a population.
- poll-workshop (11, live): polls and margin of error, same sampling family. Here informal variation.
- box-plot-builder (6, spec): summarizing one data set. Here comparing two populations from samples.
- question-lab (6, spec): what makes a question statistical. Here sampling to answer one.

## Who and how
- Grade 7, Math, module "Sampling and Inference". Standards: 7.SP.1 (understand that statistics can be used to gain information about a population by examining a sample of the population; generalizations about a population from a sample are valid only if the sample is representative of that population; understand that random sampling tends to produce representative samples and support valid inferences), 7.SP.2 (use data from a random sample to draw inferences about a population with an unknown characteristic of interest; generate multiple samples (or simulated samples) of the same size to gauge the variation in estimates or predictions), 7.SP.3 (informally assess the degree of visual overlap of two numerical data distributions with similar variabilities, measuring the difference between the centers by expressing it as a multiple of a measure of variability), 7.SP.4 (use measures of center and measures of variability for numerical data from random samples to draw informal comparative inferences about two populations).
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- The layered jar, scoops of 10, 20 and 50, the many-scoops dot plot, three two-jar pairs, the reveal. Extra: Class scoops (the class pools its scoop estimates on one dot plot). tool.json `modes: ["Candy shop", "Class scoops"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 7.SP.1 | Scoop the top; stir; scoop again | a green-heavy top scoop; a mixed one | 2 |
| 7.SP.2 | Estimate from a scoop; stack 50 scoops | a pile of estimates; bigger scoops, tighter pile | 3 |
| 7.SP.3, 7.SP.4 | Sample weights from two jars; compare | two dot plots; the gap in MADs | 4 |

## Screens and modes
Header (kit): title "Jellybean Jar"; `Candy shop`, `Class scoops`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A candy shop window, a giant jar with visible color layers, a contest card, and Mr. Ito holding out a small scoop. The welcome is queued (`welcomeAfter: true`): "Guess the share of red beans. Tap the scoop on the jar." First hint: "Tap the scoop on the jar."

**Bias (focus: the jar).** At 1366x768 the jar fills the left with the scoop tray and plots right; at 680x425 plots are a tab. The first scoop comes off the top: 19 green, 1 red. The child taps `Stir` (the jar mixes) and scoops again. A card asks when a scoop stands for the jar; the child picks reasons.

**Estimate.** A scoop of 20 is counted and the share typed (7 of 20 is 35%). The child predicts reds in the jar (3,500). `50 more scoops` stacks estimates on a dot plot. A size switch (10, 20, 50 beans) redraws the pile; the child says which size gives a tighter pile and gives an estimate with a likely range.

**Two jars.** Maker A's and maker B's jars. The child scoops 20 beans from each and weighs them; two dot plots share one scale. The tool shows each median and MAD; the child types the gap in MADs and sorts the pair as "clearly apart" or "hardly apart". Three pairs.

**Reveal.** The shop counts the jar: 3,000 red of 10,000, 30%. The child's estimate and range sit beside it.

**Trust the spread (the aha).** Mr. Ito: "One fair scoop can stand for the jar. Many scoops show you how far to trust it."

**The end.** The contest card with the estimate and the plots. `Print` prints them.

**Class scoops (extra).** Pooled estimates on the projector.

## Content
- Jar contents seeded and labeled "simulated", bean weights in grams to tenths, all readable with `Read`.
- No real brand names; the contest prize is a jar of beans.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A scoop can be retaken until its estimate is typed; the size switch can be used any time.
- Keyboard: Tab to the scoop, Stir, the tray, answer boxes, the size switch, plots (arrows move between dots) and the sort; Enter scoops or checks.
- With Motion off beans appear in the tray and dots appear on the plot.

## Look
- Accent `--brand` #5d2f78 licorice purple (header, plot axes, buttons); gold #f4c542 (the scoop, the median marker); paper #f5eff8; ink #1d0c27; muted #56505b.
- Contrast (WCAG 2.1, computed): white on brand 9.80:1; brand on paper 8.67:1; ink on paper 16.39:1; muted on paper 6.90:1; ink on gold 11.38:1.
- Never color alone: bean colors carry letters in the tray count (R, G, Y, B, W); plots are labeled by maker.
- Different from this batch (signal orange, balloon sky blue, midway red, diner teal).

## Art
- People (illustrated): Mr. Ito, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the candy shop window (1, 16:9), two jars (2, 1:1).
- Drawn in code: beans, scoops, the tray, dot plots, medians and MAD bars, so counts are exact.
About 4 images.

## Voice
Two bank voices, each unique in this batch: `curious-librarian` as Mr. Ito; `calm-professor` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.scoop + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `scoop`: "Tap the scoop on the jar."
- how `stir`: "Tap Stir, then scoop again."
- how `estimate`: "Type the share of red."
- how `more`: "Tap 50 more scoops."
- how `compare`: "Type the gap in MADs."
- event, whole, trust the spread.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
sampling (`kit/sampling.js`), as described in sample-machine's spec. Uses `rng(seed)`, `S.hopper` for the jar, `S.draw` without replacement for scoops, `S.stat.prop`, `median` and `mean`, and `S.repeat` for 50 scoops. MAD is tool-only code (mean absolute deviation from the mean). Tool-only code: the layered jar and stirring, the tray, two-jar plots.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Bias | Skip stirring | The top scoop is green-heavy, and the reason card asks why. |
| Estimate | Type 50% | Estimates are checked against the child's own scoop. |
| Overlap | Compare medians only | The gap must be typed in MADs. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `scoop`; `stir`.
2. `estimate`; `more`.
3. `compare`.
4. Trust the spread (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 7.SP.1 to 7.SP.4 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Random sampling makes samples representative; many samples show variation | American Statistical Association, "GAISE II" (2020) | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 Statistics and Probability" | yes |
| Comparing centers in units of variability | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 Statistics and Probability" | Franklin and others (2015), "Statistical Education of Teachers", American Statistical Association | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s19, 2026-11-10): 3,000 of 10,000 is 30%; 7 of 20 is 35%; medians of 1.1 g and 1.3 g with a MAD of 0.1 g are 2 MADs apart; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 jar, tray and plots; at 680x425 plots as a tab.
2. A biased scoop is compared with a stirred one and explained. (7.SP.1)
3. Estimates come from scoops, and 50 scoops show the variation by size. (7.SP.2)
4. Three two-jar pairs are compared by medians and MADs. (7.SP.3, 7.SP.4)
5. Jar contents are labeled simulated; no brand names.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: beans and dots appear at once; no network requests.

## Open questions
None.

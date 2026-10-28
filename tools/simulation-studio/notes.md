## A 5-minute start

1. On **Raw log**, look at the scatter: r = −0.64, so longer eruptions come with *shorter* waits in the same row. Read the ranger's rule in the panel (a longer eruption means a longer wait after it). Ask: can both be true?
2. Read the three **Data notes**. The second one is the key: `waiting` is the time *since the eruption before*, not the time until the next one.
3. Tap **Clean**, then **Pair each eruption with the wait after it**. r jumps to 0.89 and the line now slopes up: the rangers were right, and so was the log. They answer different questions.
4. Add **Drop night-coded rows**, then move it above Pair with its up arrow. A warning appears: 26 pairs now join eruptions that were not next to each other, and r falls to 0.82. Move it back.
5. Tap **Model**, **Fill from my clean log**, **Run 299 eruptions**: Match 89 percent, and the simulated geyser, like the real one, never follows a short eruption with a short one.

## The four benches

- **Raw log:** the 299 eruptions of 1 to 15 August 1985 exactly as published (Azzalini and Bowman 1990, MASS `geyser`), 15 rows a page. Night durations were written as short, medium or long and coded 2, 3 or 4 minutes (78 rows, marked ☾).
- **Clean:** a recipe of three steps written as real pandas, which can be reordered and removed:
  - `log["wait_after"] = log["waiting"].shift(-1)`
  - `log["night"] = log["duration"].isin([2, 3, 4])`
  - `log = log[~log["duration"].isin([2, 3, 4])]`

  The scatter, the line, the histogram, the box plots by class and the class table all follow the recipe. Tap a histogram bar or a class row to mark those rows; **N marked: see on Raw log** jumps back to them.
- **Model:** a two-state geyser. After each eruption it rolls whether the next is long, then draws the wait from the class's mean and spread (the standard deviation, SD). Real waits are blue outlines with circles, simulated ones yellow fills with triangles. Match is the share of eruptions the two histograms have in common, on the bin width the student picks (2, 5 or 10 minutes). The pairs table counts short then short, short then long and so on in both. It counts a pair only when the two eruptions were next to each other in the log.
- **Answer:** the ranger's sign ("under 3 minutes, next in A; otherwise next in B; give or take W"). **Test the sign** checks it three ways:
  - against every real eruption (298 have a next one; in sample);
  - against the later 148 eruptions with times filled from the first 150 (out of sample);
  - against a simulated summer of about 1,830 eruptions from the Model bench.

## Numbers to expect (all recomputed from the data file)

| Recipe | Rows on the scatter | r | Line |
|---|---|---|---|
| none (raw) | 299 | −0.64 | waiting = 99.31 − 7.80 × duration |
| Pair | 298 | 0.89 | wait_after = 34.95 + 10.78 × duration |
| Pair, then Flag | 221 | 0.90 | wait_after = 34.88 + 10.63 × duration |
| Pair, then Drop | 221 | 0.90 | the same line, on 78 fewer eruptions |
| Drop, then Pair (wrong order) | 220 | 0.82 | 26 wrong pairs |

- Class means after Pair: 55.6 minutes after a short eruption (104 of them), 81.2 after a long one (194). In the raw log the same split gives 83.2 and 66.4, backwards. After Pair, then Drop: 55.3 (82) and 81.8 (139).
- Model, seed 1, filled from the clean log (1.00, 0.46, 55.6 and 6.3, 81.2 and 6.8): Match 89 percent at 5 minute bins (86 at 2, 95 at 10), pairs 0, 100, 100, 98 (real 0, 104, 105, 89). The starting rules (0.5, 0.5, 70 and 10) give 66 percent. Both chances at 0.65 still match about 90 percent, but short then short jumps to 37: the histogram alone cannot tell the two geysers apart.
- Sign tests on the real log, window 10: 56 and 81 gives 269 of 298 (90 percent); 72 for both gives 136; the raw-log fill (83 and 66) gives 49. Out of sample (filled from the first 150, tested on the other 148): 131 of 148 (89 percent); from the raw log, 25 of 148. The simulated summer for 56 and 81 is 88 percent (seed 1; 87 to 91 percent over other seeds).

## Why these choices

- **Both correlations are real.** The raw r = −0.64 is the wait *before* an eruption against its length. It is negative for a true reason: a short eruption is always followed by a long one, so short waits come before long eruptions. The ranger's r = 0.89 is the wait *after*. The pairing decides which question you asked; the error is only in reading one as the other.
- **Why Flag fits this log better than Drop.** Only the coded night durations are untrustworthy. The waits and the timeline are real, and a code of 2 or 4 still says short or long. Drop throws away 78 eruptions (26 percent of the log) and with them 29 short-then-long and 34 long-then-short pairs. Flag keeps every eruption in the classes and the pairs, and only takes the coded durations off the scatter.
- **A cleaning rule is a guess that can catch good rows too.** Flag and Drop treat every duration of exactly 2:00, 3:00 or 4:00 as a code. Real measured neighbors exist (2:01 twice, 2:02, 4:01, 4:02), so one or two of the 78 may be real daytime measurements.
- **A perfect geyser does not score 100.** Two runs of the same geyser match each other only about 86 to 94 percent at 5 minute bins (79 to 87 at 2 minutes, 89 to 97 at 10), because 299 eruptions is a small sample. **New run** shows the wobble. Wider bins hide detail and raise every Match, so a match number means little without its bins.
- **What a simulation can and cannot show.** It shows the spread of outcomes (how the on-time rate wobbles from summer to summer) and lets you try rules you never saw in the data. It cannot show anything the model leaves out: it is built from the same 1985 numbers, so it cannot say whether the geyser still acts this way. Only new data can (the out-of-sample row is a small version of that, inside the 1985 log).

## Talk about it

- The file was not wrong; the column's meaning was. How would you find a problem like this in a data set you did not collect?
- Why does the order of cleaning steps matter here? Which steps can swap without changing anything?
- Drop and Flag give the same scatter. What does each one cost?
- A geyser with both chances at 0.65 matches the histogram as well as the clean fill. What evidence tells them apart?
- The sign scores 90 percent in sample and 89 percent out of sample. Why test it on eruptions it was not built from?
- The park says about 90 percent of predictions land within 10 minutes. The park's 2018 worksheet uses 68 and 94 minutes, longer than in 1985. What might have changed at the geyser, and why can't the simulated summer tell you?

## Good to know

- Alt plus the up or down arrow moves a recipe step; arrow keys move between benches.
- **New run** uses the next seed; every run with the same rules and seed gives the same geyser.
- Everything is computed in the browser; nothing is saved or sent anywhere.

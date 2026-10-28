# simulation-studio: Teaching lens (round 1, 2026-10-28)

Read cold: REFINE.md (Teaching lens), STANDARDS.md, BASELINE.md, spec.md, handoff.md, notes.md, tool.draft.json, src.html.
Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py simulation-studio` (149 KB) and driven with `scripts/drive.py`
(own profile, port 9741; frames raw, pair, dropfirst, pairdrop-model, model, answer, answer-unrun, v-pages, v-recipe,
v-model-answer, clean-1366, model-680, answer-1366, pairdrop-model-1366; 0 console errors). Every number below was
recomputed in Python from a fresh download of the Rdatasets CSV (299 rows), with the tool's mulberry32, Box-Muller,
JS rounding, clamp and 5 minute bins ported exactly.

Counts: blockers 1, should fix 6, polish 3, nits 2.

## Blocker

**B1. The pairs table and the model fill join eruptions that were not next to each other whenever Drop is in the
recipe, including the right order.** general
- Where: src.html:426-430 (`pairsOf(state.res.rows)`), used by the pairs table (804-812), "Fill from my clean log"
  (766-768), the result line choice (786-787) and the pair-row marks (742).
- What: `pairsOf` pairs consecutive rows of the cleaned log. After Drop, consecutive rows are not consecutive
  eruptions. With Pair, then Drop (the order the tool approves: hint "Your log is clean. Tap Model to build a geyser
  from it.") the Real column reads Short then short 3, Short then long 78, Long then short 79, Long then long 60. The
  real geyser has none: on the true timeline the counts are 0, 104, 105, 89. The 3 fake pairs are file rows 51 and 53,
  200 and 202, 268 and 270, each two short eruptions joined across a dropped night-coded long one (rows 52, 201, 269,
  coded 4.0). "Fill" then sets 0.96 and 0.43 instead of 1.00 and 0.46; seed 1 gives Match 88 percent and simulated
  Short then short 3, so the student sees 3 beside 3, is told "The humps match. Now check the pairs table", and the
  key result ("never follows a short one with a short one") can no longer be reached. The same 3 appear with Drop
  first.
- Why it blocks: this is the exact pairing error the tool teaches (the "26 pairs now join eruptions that were not next
  to each other" warning), made silently by the tool itself on the order it calls clean, and it reverses the Model
  bench's main finding.
- How seen: drive.py `__tool.readout()` after addStep pair, drop (realPairs {SS:3, SL:78, LS:79, LL:60}; model
  {pS:0.96, pL:0.43}; Match 0.880; simPairs SS 3), frame pairdrop-model-1366.png; Python on the CSV.
- Fix direction: count a pair only when the two rows are neighbors in the file (`rows[k+1].i === rows[k].i + 1`), or
  always count pairs on the full timeline and say so under the table.

## Should fix

**S1. Drop's cost is never shown or named.** general
- Where: Clean bench readout (src.html:711-718) and hint `cleanDone`; notes.md.
- What: Pair then Flag and Pair then Drop give the same scatter (r = 0.90 on 221, line 34.88 + 10.63 x duration) and
  the same "Your log is clean." Drop silently removes 78 eruptions (26 percent of the log, all at night): the class
  counts fall from 104 and 194 to 82 and 139 (means 55.3 and 81.8, spreads 6.7 and 6.7) and the geyser is then fitted
  on daytime eruptions only. "Cleaning choices and their effect" is the core of the DC codes, and here the choice
  has no visible effect except the B1 bug.
- How seen: drive readout pairThenDrop; Python.
- Better: a readout line when Drop is in the recipe ("78 eruptions dropped, 26 percent of the log, all at night"), and
  a notes line on why Flag fits this log (only the coded durations are untrustworthy; the waits and the timeline are
  real, so keep the rows).

**S2. The recipe code is not real code.** general
- Where: src.html:304-306 and 362-364 (Clean step buttons and recipe lines); spec Clean.
- What: written like pandas, but three of the four parts fail in pandas: `log.duration in [2, 3, 4]` raises ValueError
  (the truth value of a Series is ambiguous), `log.drop(mask)` drops by index labels, not by a mask, and
  `log.night = ...` sets an attribute, not a column (pandas warns and makes no column). Only `.shift(-1)` is right.
  9-12 tools should work like the real thing; a student who types these into Python gets errors.
- Better: real pandas, about the same length on screen: `log["wait_after"] = log["waiting"].shift(-1)`,
  `log["night"] = log["duration"].isin([2, 3, 4])`, `log = log[~log["duration"].isin([2, 3, 4])]`; or label the
  lines as pseudocode.

**S3. The simulated summer reads as a second test of the sign, but it is built from the same 1985 numbers.** general
- Where: Answer bench, second result bar (src.html:878-880); notes.md "Talk about it".
- What: the summer geyser's waits are normal with spreads 6.3 and 6.8, so its on-time rate is what those spreads imply
  (about 87 to 89 percent within 10 minutes for this mix of short and long eruptions), not evidence that the sign works
  on the real geyser. Over seeds 1 to 200 it runs 86.6 to 90.7 percent (seed 1: 1,616 of 1,830, 88.3 percent). Nothing
  on screen or in the notes says what the simulation cannot show, and the Talk question "What does a simulation let you
  test that the 15 days of real data cannot?" invites the overclaim. 3B-DA-07 (evaluate what models and simulations
  can test) is the code this should teach. Also, 269 of 298 is in sample: the sign is filled from the same eruptions
  it is tested on.
- How seen: Python (normal-theory estimate and 200 seeds); frame answer-1366.png.
- Better: one small line under the summer bar ("Built from the same 1985 numbers: it shows how the on-time rate
  wobbles from summer to summer, not whether the geyser still acts this way"), and a notes answer: a simulation shows
  the spread of outcomes (New run) and lets you try rules you never saw; it cannot show anything the model leaves out
  (the drift since 1985 that the park's 68 and 94 show, earthquakes, the night codes). An honest out-of-sample check
  for the notes: fill from the first 150 eruptions (means 56 and 81) and test on the other 148: 131 of 148, 89
  percent; the reverse (55 and 82) gets 136 of 150, 91 percent. So the 90 percent holds up.

**S4. The raw r = -0.64 is a real pattern, not a mistake, and nothing says so.** general
- Where: welcome line ("Something in it is backwards"), Raw readout (src.html:579, "wait = 99.31 - 7.80 x duration"),
  notes.md step 1 ("who is wrong, the rangers or the log?").
- What: the same-row scatter is the wait before an eruption against that eruption's length. It is negative for a true
  reason: a short eruption is always followed by a long one (Short then short = 0, the Model bench's finding), so a
  short wait comes before a long eruption. The error is reading "the wait before" as "the wait after", not the
  correlation. As written, a student can leave thinking a negative r meant bad data. The readout also calls the
  column "wait" when it is the file's "waiting" (the wait before).
- Better: the Raw readout says "waiting" (or "wait before"); a notes paragraph: both correlations are real and answer
  different questions (what comes before an eruption, what comes after); the pairing decides which question you
  asked. "Talk about it" already has "The file was not wrong; the column's meaning was"; this completes it.

**S5. The public sources for the park's numbers are wrong.** general
- Where: tool.draft.json `sources`.
- What: it lists https://www.nps.gov/yell/planyourvisit/predict-old-faithful.htm, which returns 404 (curl,
  2026-10-28). The on-screen claims come from two other pages, both checked and both missing from tool.draft.json:
  the YELL 003 worksheet PDF (https://www.nps.gov/common/uploads/teachers/lessonplans/YELL_003-PredictOldFaithful.pdf:
  "< 3 minutes, 68 minutes; > 3 minutes, 94 minutes", confirmed) and the virtual visitor center exhibit
  https://home.nps.gov/features/yell/ofvec/exhibits/eruption/prediction/predict7.htm ("about 90 percent" of
  predictions within plus or minus 10 minutes, confirmed; predict8.htm confirms only one eruption ahead can be
  predicted).
- Better: replace the dead link with those two URLs.

**S6. One crosswalked code is only lightly taught: 3A-DA-11, create interactive data visualizations.** general
- Where: the module codes (HS-DAT-DC-21, DC-23, DI-25, DI-26; crosswalk 3A-DA-11, 3A-DA-12, 3B-DA-05, 3B-DA-07).
- What: modeling (3A-DA-12), finding patterns (3B-DA-05) and judging a model (3B-DA-07, once S3 is done) are taught by
  what the student does. Creating a visualization is not: every chart is fixed; the student never picks what is
  plotted, how it is binned or which chart answers the question. Bin taps and marks are reading, not making. Which
  2026 id carries 3A-DA-11 could not be confirmed here (data/standards has ids only; the CSTA page renders by script),
  so check that before acting.
- Better (only if it teaches well, BASELINE rule 2): a real choice with a consequence, such as the bin width on the
  Model histogram (Match changes with it, which itself teaches that a fit measure depends on choices), or the x and y
  columns on Clean. Otherwise move that code to a tool where building the chart is the job.

## Polish

**P1. Match has no yardstick.** general. A perfect model cannot reach 100 percent with 299 eruptions: two runs of the
clean-fill geyser against each other (seeds s and s + 1000, 200 pairs) overlap 86 to 94 percent (median 90); the real
log's first half against its second half overlaps 88 percent. So 89 percent is as good as a run can show, and students
chasing 100 would be chasing noise. Say this in the notes and in a short line by Match ("A perfect geyser scores about
86 to 94 percent: New run shows the wobble").

**P2. "spread" is never named.** general. For 9-12, name it once as the standard deviation (class table header
"spread (SD)" or the notes). The fill uses the sample SD (6.31, 6.80), which matches.

**P3. The night-code rule is an assumption.** general. Flag and Drop treat every duration of exactly 2:00, 3:00 or 4:00
as a code. Measured neighbors appear once or twice each (2:01 twice, 2:02, 4:01 and 4:02 once), so one or two of the
78 may be real daytime measurements. One notes line ("a cleaning rule is a guess that can catch good rows too") turns
this into the lesson the DC codes ask for.

## Nits

**N1.** The comparison line (src.html:881) says "The park's worksheet today"; the worksheet PDF is dated 2018-08-16
(its metadata). "The park's 2018 worksheet" is exact.

**N2.** Spec Sources call the exhibit the "Old Faithful Visitor Education Center exhibit"; the page is the "Old
Faithful Virtual Visitor Center". Spec wording only.

## Checked and right

- Data: the 299 waiting and duration values in src.html equal the Rdatasets CSV exactly. Night codes 78 (2.0 x 23,
  3.0 x 2, 4.0 x 53). The data notes match the MASS documentation (nocturnal codes 2, 3, 4 for short, medium, long;
  waiting described as the time to the next eruption in the original files, corrected in MASS 7.3-30; 1 to 15 August
  1985).
- Clean: raw r -0.6446, line 99.31 - 7.80 x duration, 299 rows (the tool shows -0.64, correct rounding; the spec's
  -0.65 is already in handoff). Pair r 0.8885, 34.95 + 10.78 x duration, 298. Pair then Flag r 0.8980,
  34.88 + 10.63 x duration, 221. Drop then Pair r 0.8164 on 220, 26 wrong pairs. Class means after Pair 55.6 (SD 6.3,
  n 104) and 81.2 (6.8, 194); raw 83.2 (6.6, 105) and 66.4 (13.2, 194). Waits 43 to 108, mean 72.3, SD 13.9; the
  histogram from 40 matches the spec.
- Model (seeds 1 to 200, 5th to 95th percentile): start 0.60 to 0.69, seed 1 0.656, SS 59 to 89; clean fill 0.85 to
  0.93, seed 1 0.8903 with pairs 0, 100, 100, 98, SS always 0; 0.65 and 0.65 0.85 to 0.93, seed 1 0.9017 with SS 37,
  SS 25 to 46; raw fill 0.78 to 0.86, seed 1 0.840. Fill gives 1.00 and 0.46.
- Answer: 56 and 81 gives 163, 269, 294 at windows 5, 10, 15; 72 always gives 60, 136, 205; 83 and 66 gives 49 at 10.
  Summer seed 1: 1,616 of 1,830 (88 percent), 91.7 days. The park's 68 and 94 on the 1985 log get 106 of 298, which
  supports "the 1985 sign would not work now".
- Every number in notes.md matches (including "87 to 91 percent over other seeds": seeds 1 to 200 round to 87 to 91).
- Nothing gives an answer away: there is no predict, quiz or hidden-information mode.
- Language is plain and right for 9-12. No sensitive topics in these standards (rule 8). Nothing cultural, Native or
  hard-history: no sensitivity referral.

## Done when

| # | Result |
|---|---|
| 1 | Pass: 299 rows, 20 pages, r = -0.64 (the spec's -0.65 is the rounding note already in handoff) |
| 2 | Pass: r 0.89, means 55.6 and 81.2; with Flag r 0.90 on 221 |
| 3 | Pass: Drop before Pair shows the 26-pair warning and r 0.82; moved after, r 0.90 (but see B1: the pairs table is wrong in both orders) |
| 4 | Pass: seed 1 clean fill Match 89 percent, pairs 0, 100, 100, 98; 0.65 and 0.65 Match 90 percent, SS 37 |
| 5 | Pass: 269, 136, 49 |
| 6 | Pass: 88 percent (seed 1); seeds 1 to 50 run 86.8 to 90.5, already in handoff |
| 7 | Pass: held clicks; 5 page turns speak `notes` once; the recipe line is spoken once, then silent; `modelHow` and `answerHow` once; `onTime` on 5 of 5 tests |
| 8 | Pass: pipeline, main chart and Run button visible at 1366x768 and 680x425 (frames model-680, pairdrop-model-1366); real is outline plus circle, simulated is fill plus triangle |

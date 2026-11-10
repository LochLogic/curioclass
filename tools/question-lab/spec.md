# Question Lab

## One idea
At a lab bench of question cards the lab lead, Priya (made up, labeled "illustration"), gives the child one test for every card, "Would the answers vary?", and two bins, statistical and not; sort rounds put "How tall am I?" in one bin and "How tall are the students in my grade?" in the other, and near misses teach (one person's answer against many people's answers; a fact against a question that expects variety), with a reason picked for every card; rewrite rounds turn "How long did I sleep last night?" into "How long did students in my class sleep last night?"; survey rounds send the child's own number question to a simulated class of 30 (labeled "simulated"), and a dot plot builds dot by dot, so "How many pets does each student have?" lumps at 0 and 1, trails off to 5, has a median of 1 and a mean near 1.5; the child describes where the middle is, how spread out the answers are and whether the shape is lumped, lopsided or flat; a center and spread round sets two plots side by side with the same median of 30 minutes but ranges of 16 and 60, so one number for the middle is not the whole story; at the end the child sees that a statistical question expects variety and that variety has a center, a spread and a shape, so a sixth grader learns to recognize statistical questions and to describe a distribution by its center, spread and overall shape.

## Not like
- box-plot-builder (6, spec): computing five-number summaries and drawing box plots. Here what a statistical question is and how a distribution looks.
- poll-workshop (11, live): sampling and bias. Here one class's answers.
- lunch-survey-cleanup (6, spec): cleaning messy survey data. Here asking and describing.
- seed-sprout-data (5, spec): line plots of measurements in eighths. Here the question comes first, and the plot is described.

## Who and how
- Grade 6, Math, module "Statistical Variability". Standards: 6.SP.1 (recognize a statistical question as one that anticipates variability in the data related to the question and accounts for it in the answers; for example, "How old am I?" is not a statistical question, but "How old are the students in my school?" is a statistical question because one anticipates variability in students' ages), 6.SP.2 (understand that a set of data collected to answer a statistical question has a distribution which can be described by its center, spread, and overall shape), 6.SP.3 (recognize that a measure of center for a numerical data set summarizes all of its values with a single number, while a measure of variation describes how its values vary with a single number).
- Format: sort. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Twenty question cards, six rewrite cards, six survey questions with simulated answers, four center and spread pairs. Extra: Real class (the class answers one question on a single device; answers stay on the device, said on screen). tool.json `modes: ["Lab", "Real class"]`, `minutes: "20-30"`, `grades_label: "Grade 6"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 6.SP.1 | Sort cards with a reason; rewrite non-statistical ones | two bins; the "would it vary?" test | 2 |
| 6.SP.2 | Run a survey; describe the plot | dots piling up; shape words | 3 |
| 6.SP.3 | Pick one number for the middle and one for spread | two plots, same median, different ranges | 4 |

## Screens and modes
Header (kit): title "Question Lab"; `Lab`, `Real class`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A bright lab bench, a stack of question cards, two glass bins labeled "Statistical" and "Not statistical", and Priya in a lab coat. The welcome is queued (`welcomeAfter: true`): "One test for every card: would the answers vary? Drag the top card into a bin." First hint: "Drag the top card into a bin."

**Sort (focus: the bench).** At 1366x768 the bench fills the left with the bins right; at 680x425 the bins sit below. After each drop the child picks a reason ("one person, one answer"; "many people, many answers"; "a fact that doesn't change"). Wrong drops bounce back with the reason that fits.

**Rewrite.** A non-statistical card and a word bank; the child rebuilds it so many answers are expected, and the test runs again.

**Survey (focus: the plot).** The child picks or writes a number question and taps `Ask the class`. Thirty simulated students answer, and dots drop onto a dot plot one by one. The child picks shape words (lumped, lopsided, flat, a gap, an outlier), drags a marker to the middle and stretches a bar over where most answers sit.

**Center and spread.** Two plots side by side with the same median. The child taps the median on each (both 30) and the range on each (16 and 60), and answers which class's answers vary more.

**Variety has a shape (the aha).** Priya: "If the answers vary, it's statistical. And the variety has a middle, a spread and a shape you can describe."

**The end.** The sorted bins and survey plots. `Print` prints them.

**Real class (extra).** The class answers on one device.

## Content
- Twenty question cards across school, home and sport, six simulated surveys of 30 labeled "simulated", all readable with `Read`.
- Questions avoid weight, income, health and family situations.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cards can be moved between bins until `Check`; markers can be moved any time.
- Keyboard: Tab to cards, bins, reasons, the word bank, Ask the class, the plot (arrows move a marker) and shape words; Enter drops or checks.
- With Motion off dots appear at once.

## Look
- Accent `--brand` #5b3a8c beaker violet (header, bins, buttons); gold #f4c542 (the card in hand, the median marker); paper #f3f0f9; ink #1a0d2e; muted #544f5e.
- Contrast (WCAG 2.1, computed): white on brand 8.65:1; brand on paper 7.68:1; ink on paper 16.34:1; muted on paper 7.02:1; ink on gold 11.32:1.
- Never color alone: bins are labeled in words; markers carry "median" and "range".
- Different from this batch (asphalt slate, bike-path blue, clay sienna, card-table green).

## Art
- People (illustrated): Priya and a varied class of 30 as small portraits, labeled "illustration" (Gemini, `people: true`, 7 with portraits reused; cutout yes).
- Local FLUX (`scripts/localart.py`): the lab bench (1, 16:9).
- Drawn in code: cards, bins, dot plots and markers.
About 8 images.

## Voice
Two bank voices, each unique in this batch: `bright-teacher` as Priya; `news-reader` as the survey results and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.round + ':' + state.card + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `sort`: "Drag the card into a bin."
- how `reason`: "Pick the reason that fits."
- how `rewrite`: "Drag words to rebuild the question."
- how `ask`: "Tap Ask the class."
- how `describe`: "Pick words for the shape."
- event, whole, variety has a shape.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the sort and reasons, the rewrite bank, seeded simulated answers, the dot plot with median and range markers.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sort | Look for "students" in the card | Near misses like "How many students are in my class?" have one answer. |
| Reason | Pick reasons at random | Each reason is checked against its card. |
| Spread | Read the medians | The pair has equal medians; the range answer is checked. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `sort`; `reason`.
2. `rewrite`.
3. `ask`; `describe`.
4. Variety has a shape (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 6.SP.1 to 6.SP.3 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Anticipating variability is what makes a question statistical | American Statistical Association, "GAISE II: Guidelines for Assessment and Instruction in Statistics Education" (2020) | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 Statistics and Probability" | yes |
| Describing distributions by center, spread and shape | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 Statistics and Probability" | American Statistical Association, "GAISE II" (2020) | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s18, 2026-11-10): thirty pet counts (8 zeros, 10 ones, 6 twos, 3 threes, 2 fours, 1 five) give median 1 and mean 44/30, about 1.5; two plots with median 30 have ranges 16 and 60; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 bench and bins; at 680x425 bins below.
2. Twenty cards are sorted with reasons and six are rewritten. (6.SP.1)
3. Six surveys are run and described by center, spread and shape. (6.SP.2)
4. Paired plots show one number for center and one for variation. (6.SP.3)
5. Simulated answers are labeled; Real class answers stay on the device.
6. `Read` reads every card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: dots appear at once; no network requests.

## Open questions
None.

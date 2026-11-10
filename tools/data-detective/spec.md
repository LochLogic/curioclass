# Data Detective

## One idea
At a detective's desk Inspector Kaya (made up, labeled "illustration") opens case files that can only be cracked with paired data, and the first case is a footprint in the mud: given the foot length and height of a real sample of adults, how tall was the person who left it; the child plots each pair on a scatter, names the pattern (positive, linear, a tight cloud with one outlier to explain), drags a line by eye through the cloud while a closeness meter shows how far the points sit from it, writes the line's equation, and says what the slope means (centimeters of height for each extra centimeter of foot, read from the sample) and why the intercept (a person with a foot of 0 cm) means nothing here; the prediction is then checked against a held-back case; later files bring hours of daylight against temperature, a nonlinear seasonal loop, and a case with no association at all that the child must call "no pattern"; the last file is a two-way table from a made-up survey of 100 students (labeled "illustration") asking whether those with a curfew also do chores, and row percentages crack it: 30 of 40 with a curfew have chores (75%) against 20 of 60 without (about 33%), so the two go together; at the end the child sees that paired data have patterns, a line can summarize a linear one, and the slope tells the story of the case, so an eighth grader learns to build and read scatter plots, fit and judge a line, use its slope and intercept to predict, and find association in a two-way table.

## Not like
- box-plot-builder (6, spec): one variable, same data-desk engine. Here two variables.
- correlation-guessing-game (9, spec): correlation coefficients and residuals. Here lines by eye.
- which-model-wins (9, spec): choosing among model types. Here one line and its meaning.
- jellybean-jar (7, spec): sampling one population. Here association between two variables.

## Who and how
- Grade 8, Math, module "Bivariate Data". Standards: 8.SP.1 (construct and interpret scatter plots for bivariate measurement data to investigate patterns of association between two quantities; describe patterns such as clustering, outliers, positive or negative association, linear association, and nonlinear association), 8.SP.2 (know that straight lines are widely used to model relationships between two quantitative variables; for scatter plots that suggest a linear association, informally fit a straight line, and informally assess the model fit by judging the closeness of the data points to the line), 8.SP.3 (use the equation of a linear model to solve problems in the context of bivariate measurement data, interpreting the slope and intercept), 8.SP.4 (understand that patterns of association can also be seen in bivariate categorical data by displaying frequencies and relative frequencies in a two-way table; construct and interpret a two-way table summarizing data on two categorical variables collected from the same subjects; use relative frequencies calculated for rows or columns to describe possible association between the two variables).
- Format: data. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Six case files (footprint, daylight and temperature, a no-pattern case, a clustered case, a prediction check, the curfew table). Extra: Class case (the class measures arm span and height; data stay on the device). tool.json `modes: ["Case files", "Class case"]`, `minutes: "25-35"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 8.SP.1 | Plot pairs; name the pattern | clusters, outliers, no pattern, a loop | 2 |
| 8.SP.2 | Drag a line; watch the closeness meter | the cloud hugging or leaving the line | 3 |
| 8.SP.3 | Write the equation; predict; explain slope and intercept | the held-back case | 3 |
| 8.SP.4 | Fill row percentages; judge association | 75% against 33% | 4 |

## Screens and modes
Header (kit): title "Data Detective"; `Case files`, `Class case`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A detective's office at dusk, a desk lamp, a stack of case files, a plaster footprint cast, and Inspector Kaya with a notebook. The welcome is queued (`welcomeAfter: true`): "A footprint, 27 centimeters. How tall was the person? Open the file and plot the first pair." First hint: "Tap the first row to plot it."

**Scatter (focus: the plot).** At 1366x768 the plot fills the left with the data table and case notes right; at 680x425 the table is a tab. The child plots the first five pairs by tapping, then `Plot the rest` fills in the sample. A pattern card asks for direction, form, clusters and outliers; the child taps an outlier to read its row.

**Fit.** The child drags two handles to place a line. A closeness meter shows the average distance of points from the line; the child improves it, then types slope and intercept (rounded to a tenth) and picks sentences for each.

**Predict.** The child uses the line to answer the case, then `Open the evidence` reveals a held-back person; the error is shown in centimeters.

**More cases.** Daylight against temperature (a loop, not a line), a no-pattern case (shoe size against birthday), a clustered case.

**The table.** A two-way table of curfew and chores. The child fills row totals and row percentages and says whether the two are associated.

**The slope tells it (the aha).** Inspector Kaya: "Paired data leave a pattern. A line sums it up, and the slope tells the story."

**The end.** The case board with each verdict. `Print` prints it.

**Class case (extra).** Arm span and height measured in class; no names, nothing leaves the device.

## Content
- Paired data from openly licensed public samples, credited on each card; survey tables labeled "illustration", all readable with `Read`.
- Heights and feet are adult samples; no child body data are shipped.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- The line can be moved until `Lock line`; table cells can be retyped.
- Keyboard: Tab to table rows, the plot (arrows move between points), the line handles (arrows move them), the meter, answer boxes and table cells; Enter plots or checks.
- With Motion off points appear at once and the meter does not animate.

## Look
- Accent `--brand` #6d4a22 case-file brown (header, axes, buttons); gold #f4c542 (the point in hand, the line handles); paper #f8f2ea; ink #231806; muted #5a5348.
- Contrast (WCAG 2.1, computed): white on brand 7.92:1; brand on paper 7.12:1; ink on paper 15.67:1; muted on paper 6.83:1; ink on gold 10.72:1.
- Never color alone: outliers carry a ring and a label; table cells show percent signs.
- Different from this batch (blueprint blue, reef green, loop indigo, factory red).

## Art
- People (illustrated): Inspector Kaya, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the office at dusk (1, 16:9), the case-file stack (1, 4:3), the footprint cast (1, 1:1).
- Drawn in code: every plot, line, meter and table.
About 4 images.

## Voice
Two bank voices, each unique in this batch: `firm-captain` as Inspector Kaya; `news-reader` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.case + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `plot`: "Tap the next row to plot it."
- how `pattern`: "Tap the words that fit the pattern."
- how `fit`: "Drag the handles to fit the line."
- how `equation`: "Type the slope and intercept."
- how `predict`: "Type your prediction, then tap Open the evidence."
- how `table`: "Type the row percent."
- event, whole, the slope tells it.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
data-desk (`kit/data-desk.js`), as described in data-desk-distributions' spec. Uses `DataTable` for each case, `Chart` scatter with `highlight` and `onPoint`, and `chart.fit('linear')` only to score the closeness meter, never to place the child's line. Tool-only code: the draggable line with closeness, the held-back check, the two-way table.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Line | Drag anywhere | The meter must fall under a set distance before `Lock line`. |
| Pattern | Call every case positive and linear | The loop and no-pattern cases catch it. |
| Table | Compare counts, 30 against 20 | The check asks for row percentages. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `plot`; `pattern`.
2. `fit`; `equation`; `predict`.
3. `table`.
4. The slope tells it (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 8.SP.1 to 8.SP.4 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Foot length and stature are strongly and linearly associated in adults | Gordon and others (2014), "2012 Anthropometric Survey of U.S. Army Personnel (ANSUR II)" | CDC, National Health and Nutrition Examination Survey (NHANES) body measures | yes |
| Daylight and temperature follow the seasons with a lag | NOAA National Centers for Environmental Information, Climate Normals | U.S. Naval Observatory, sun rise and set tables | yes |
| Informal line fitting and row percentages in two-way tables | Common Core Standards Writing Team (2011), "Progressions for the CCSS, 6-8 Statistics and Probability" | American Statistical Association, "GAISE II" (2020) | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad s20, 2026-11-10): 30 + 10 = 40 with a curfew and 20 + 40 = 60 without make 100; 30/40 = 75% and 20/60 is about 33%; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 plot, table and notes; at 680x425 table as a tab.
2. Six scatters are plotted and their patterns named, including a no-pattern case. (8.SP.1)
3. Lines are fit by eye, judged by closeness, written as equations and used to predict with slope and intercept explained. (8.SP.2, 8.SP.3)
4. The two-way table is completed with row percentages and association judged. (8.SP.4)
5. Each data card credits its public source; class data stay on the device.
6. `Read` reads every card and row; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: points appear at once; no network requests.

## Open questions
- Which paired data ship (default used: an adult foot length and stature sample from ANSUR II or NHANES, and NOAA daylight and temperature normals; the geyser data on the idea card is left to simulation-studio).

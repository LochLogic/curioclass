# Graph Glow-Up

## One idea
The school newsletter's editor, Jo (made up, labeled "illustration"), has a crowded club-vote picture graph that runs off the page (80 soccer stickers in a row), so the child gives it a makeover by picking a key (1 picture = 2, 5 or 10 votes) and the graph rebuilds, with half-pictures when needed (35 chess votes at a key of 10 is 3 and a half pictures); a goal card asks for a graph that fits the page and still answers the newsletter's questions ("How many more votes did soccer get than chess?", "How many more did art and music get together than chess?"), so the child tests the redesign by answering them; bar graphs get the same makeover with axis steps of 5 or 10; then the science club's 15 bean pods, measured with rulers marked in halves and fourths of an inch, go on a line plot with quarter-inch marks after the child measures a few on screen; at the end the before and after sit side by side and the right scale makes the comparison readable without changing the data, so a third grader learns to draw scaled picture graphs and scaled bar graphs, to solve one- and two-step "how many more" and "how many less" problems from them, and to measure lengths to the nearest half and quarter inch and show the data on a line plot marked in halves or quarters.

## Not like
- lunch-line-data (2, spec): a scale of one and whole inches. Here scaled keys and quarter inches.
- class-poll (1, spec): first picture graphs. Here choosing a scale.
- data-desk-distributions (12, spec): statistics and distributions. Here scale and line plots.
- pattern-painter (3, spec): two-step problems from claims. Here two-step problems from graphs.

## Who and how
- Grade 3, Math, module "Scaled Graphs". Standards: 3.MD.3 (draw a scaled picture graph and a scaled bar graph to represent a data set with several categories; solve one- and two-step "how many more" and "how many less" problems using information presented in scaled bar graphs), 3.MD.4 (generate measurement data by measuring lengths using rulers marked with halves and fourths of an inch; show the data by making a line plot, where the horizontal scale is marked off in appropriate units: whole numbers, halves, or quarters).
- Format: builder. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 48 px or more.
- Three crowded graphs (club votes, books read, recycling bags), three keys, two bar-graph makeovers, nine questions, a crate of 15 bean pods, the line plot, before and after. Extra: Tricky axis (a bar graph whose axis starts at 50 makes a small gap look huge; the child fixes it). tool.json `modes: ["Newsletter", "Tricky axis"]`, `minutes: "20-30"`, `grades_label: "Grade 3"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 3.MD.3 (draw) | Pick a key or an axis step; rebuild | the graph fitting; half-pictures | 2 |
| 3.MD.3 (solve) | Answer one- and two-step how many more or less | the rows lined up with the key | 3 |
| 3.MD.4 | Measure pods to the quarter inch; build the line plot | the ruler; Xs above quarter marks | 4 |

## Screens and modes
Header (kit): title "Graph Glow-Up"; `Newsletter`, `Tricky axis`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A newsletter page on a desk with a picture graph whose soccer row runs off the edge, and Jo with a pencil behind one ear. The welcome is queued (`welcomeAfter: true`): "This graph runs right off the page! Can you give it a glow-up? Tap a key to choose how many votes each picture shows." First hint: "Tap a key: 2, 5 or 10."

**Makeover (focus: the graph).** At 1366x768 the newsletter page fills the middle with keys and the goal card at the right; at 680x425 the goal card folds under the page. Picking a key rebuilds the graph and redraws the key box ("each ball = 5 votes"). The page edge glows gold when everything fits. Half-pictures appear for odd counts.

**Questions.** "How many more votes did soccer get than chess?" "How many more did art and music get together than chess?" The child reads with the key and types the answer; the rows slide together to check.

**Bar graphs.** A crowded bar graph with 1-step ticks; the child picks an axis step of 5 or 10 and the bars redraw.

**Bean pods (3.MD.4).** A crate of bean pods and a ruler marked in halves and fourths. The child measures four pods by sliding the ruler (end at 0) and tapping the nearest quarter inch; the rest of the 15 are given. Each gets an X on a line plot marked in quarters. "Which length is most common? How much longer is the longest pod than the shortest?"

**Before and after (the aha).** The crowded graph and the glow-up side by side. Jo: "Same votes, same story. The right scale just makes it readable."

**The end.** The finished newsletter page. `Print` prints it.

**Tricky axis (extra).** A bar graph starting at 50 makes 55 look double 52; the child resets the axis to 0.

## Content
- Three data sets (labeled made up for practice), keys of 2, 5 and 10, axis steps of 5 and 10, 15 bean pods from 2 1/4 to 4 inches, all readable with `Read`.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Keys and steps can be switched at any time; the data never changes.
- Keyboard: Tab to keys, steps, the graph rows, the ruler and the plot; arrows slide the ruler; Enter picks.
- With Motion off graphs rebuild at once.

## Look
- Accent `--brand` #136470 newsletter teal (header, the key box, buttons); gold #f4c542 (the fitting page edge, the pod in hand); paper #edf6f7; ink #05202a; muted #455a5f.
- Contrast (WCAG 2.1, computed): white on brand 6.81:1; brand on paper 6.20:1; ink on paper 15.34:1; muted on paper 6.64:1; ink on gold 10.36:1.
- Never color alone: rows carry labels and the key box is always shown.
- Different from this batch (penguin navy, mural magenta, backyard green, picnic red).

## Art
- People (illustrated): Jo, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the newsletter desk (1, 16:9), the bean pod crate (1, 1:1), four category icons (4, 1:1).
- Drawn in code: graphs, keys, half-pictures, the ruler, the line plot.
About 7 images.

## Voice
Two bank voices, each unique in this batch: `casual-peer` as Jo; `clear-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.graph + ':' + state.key + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `key`: "Tap a key: 2, 5 or 10."
- how `step`: "Tap an axis step: 5 or 10."
- how `ask`: "Type the answer."
- how `measure`: "Slide the ruler to the pod, then tap the nearest quarter inch."
- event, whole, before and after.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
graphs (family "graphs"; no engine file yet). This tool builds the family's shared pieces first, in a marked block `/* GRAPHS ENGINE: begin */ ... /* end */`: scaled picture graphs with keys and partial pictures, bar graphs with chosen axis steps, and line plots marked in wholes, halves or quarters; later graphs tools reuse them. (The grade 8 to 12 coordinate-plane family, `kit/graphing.js`, is separate.)

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Key | Pick any key | Key 2 still runs off the page; the goal card needs fit and answers. |
| Questions | Count pictures, ignore the key | Answers must use the key; the check multiplies it out. |
| Measure | Tap any mark | The nearest quarter mark glows on a miss. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `key`.
2. `ask`; `step`.
3. `measure`.
4. Before and after (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 3.MD.3, 3.MD.4 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| Scaled graphs and quarter-inch line plots belong in grade 3 | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-3 Categorical Data; Grades 2-5 Measurement Data" | National Council of Teachers of Mathematics, "Principles and Standards", grades 3 to 5 data analysis | yes |
| A bar axis that doesn't start at zero exaggerates differences | Tufte (2001), "The Visual Display of Quantitative Information" | Huff (1954), "How to Lie with Statistics" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r11, 2026-11-10): 80, 35, 50 and 45 votes make 16, 7, 10 and 9 pictures at a key of 5 and 8, 3 1/2, 5 and 4 1/2 at a key of 10; soccer beats chess by 45 and art and music together beat chess by 60; the 15 pods run from 2 1/4 to 4 inches with 3 inches most common; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 page, keys and card; at 680x425 card under page.
2. Three picture graphs and two bar graphs are rescaled to fit. (3.MD.3)
3. Nine one- and two-step questions are answered with the key. (3.MD.3)
4. Fifteen pods are on a quarter-inch line plot, four measured by the child. (3.MD.4)
5. `Read` reads every card; every control is 48 px or more.
6. Data is labeled made up; Jo is labeled illustration.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: graphs rebuild at once; no network requests.

## Open questions
None.

# Fair Survey Kit

## One idea
The student council president, Jordan (made up, labeled "illustration"), brings the child a request, "Which playground should we build: a climbing dome, a swing circle or a garden path?", and the child plans the survey before anyone is asked: who to ask (only 5th graders at lunch, one class, or every grade), the answer type for each question (a pick from a list, a number, or words), and whether there is a "skip this" choice; the plan runs and a 60-row table of answers arrives with the mistakes real surveys get, "swngs" typed in a word box, a blank, "grade 40", and the same name twice; the child flags each problem, chooses a fix, and sees that pick-lists would have prevented the spelling mix-ups, then sorts the cleaned 56 rows by grade and by choice while a bar chart updates as rows change; the surprise comes in the comparison: asking only 5th graders made the climbing dome win 11 of 20, but with every grade asked the swing circle wins with 24 of 56, because the kindergartners and first graders who were never asked change the answer; at the end the child sees that a fair plan includes everyone and that answers must be checked and organized before they are counted, so a student in grades 3 to 5 learns to plan a data collection that includes everyone and to check and organize the answers.

## Not like
- lunch-survey-cleanup (Grades 6-8, spec): cleaning trade-offs and a written report. Here planning first, grade 3-5 depth.
- data-table-builder (4, spec): tables and charts from class data. Here survey plans and messy rows.
- question-jar (K, spec): which questions data can answer. Here running a full survey.
- three-route-rules (3, concept): who a rule leaves out. Here who a survey leaves out.

## Who and how
- Grades 3-5, Computer Science, module "Fair Surveys". Standards: E3-DAT-IM-11, E3-DAT-DC-09, E4-DAT-DC-09, E5-DAT-DC-09 (CSTA 2026 codes; module line quoted, as the CSTA 2026 wording is not in data/standards: "Plan a data collection that includes everyone; check and organize the answers").
- Format: data. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every row and card. Controls 48 px or more.
- Three plans, a 60-row answer table with four kinds of mistakes, the sort and chart, the plan comparison. Extra: Council meeting (the class compares plans on the projector). tool.json `modes: ["Survey", "Council meeting"]`, `minutes: "20-30"`, `grades_label: "Grades 3-5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| E3-DAT-DC-09 | Pick answer types; see pick-lists prevent mix-ups | "swngs" in a word box | 2 |
| E4-DAT-DC-09 | Flag and fix blanks, misspellings, impossible values, duplicates | 60 rows to 56 | 3 |
| E5-DAT-DC-09 | Sort by grade and choice; answer the question | the bar chart | 3 |
| E3-DAT-IM-11 | Compare plans; see who was left out | dome wins, then swings win | 4 |

## Screens and modes
Header (kit): title "Fair Survey Kit"; `Survey`, `Council meeting`; `Read`, `Motion`, `Sound`, `Print`. Controls 48 px or more.

**On load and first tap.** A student council table with three playground posters (a climbing dome, a swing circle, a garden path), a clipboard, and Jordan holding the request. The welcome is queued (`welcomeAfter: true`): "Help us ask fairly. Tap Who to ask to start your plan." First hint: "Tap Who to ask."

**Plan (focus: the clipboard).** At 1366x768 the clipboard is left with posters right; at 680x425 posters are a tab. Three choices: who, answer type, skip box. `Send survey` runs it.

**Answers arrive.** A table fills row by row (grade, name, choice, age). Mistakes are seeded by the plan: word boxes bring misspellings; no skip box brings blanks.

**Check.** The child taps a problem cell, names the problem (blank, misspelled, impossible, duplicate) and picks a fix (correct, remove, keep as "skipped").

**Sort and count.** Sort buttons for grade and choice; the bar chart updates.

**Compare plans.** The 5th-grade-only plan and the every-grade plan side by side; the child says whose voice changed the answer.

**Everyone counts (the aha).** Jordan: "When we asked everyone and cleaned the answers, we heard the whole school."

**The end.** The cleaned table, the chart and the council note. `Print` prints them.

**Council meeting (extra).** Plans compared in class.

## Content
- All rows made up, labeled "illustration data"; names are first names only.
- Each grade's preferences are seeded so the comparison always shows the change.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Fixes can be undone until `Count`; plans can be re-sent.
- Keyboard: Tab to plan choices, Send survey, the table (arrows move between cells), problem and fix menus, sort buttons and the chart; Enter picks or sorts.
- With Motion off rows appear at once.

## Look
- Accent `--brand` #b0341e council red (header, the clipboard, buttons); gold #f4c542 (the cell in focus, the winning bar); paper #fcf0ed; ink #2e0e07; muted #5e504c.
- Contrast (WCAG 2.1, computed): white on brand 6.26:1; brand on paper 5.61:1; ink on paper 15.93:1; muted on paper 6.90:1; ink on gold 10.92:1.
- Never color alone: flagged cells carry an icon and the problem's name; bars carry counts.
- Different from this batch (map blue, relay purple, museum brown, workday green).

## Art
- People (illustrated): Jordan, labeled "illustration" (Gemini, `people: true`, 1; cutout yes).
- Local FLUX (`scripts/localart.py`): the council table (1, 16:9), three playground options (3, 4:3).
- Drawn in code: the clipboard, the table and the bar chart.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `firm-captain` as Jordan; `bright-teacher` as the narrator and hints. `Curio.voice` with `scope: () => state.mode + ':' + state.plan + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `plan`: "Pick who to ask, the answer type and the skip box."
- how `send`: "Tap Send survey."
- how `check`: "Tap a cell with a problem."
- how `fix`: "Name the problem, then pick a fix."
- how `sort`: "Tap a sort button."
- how `compare`: "Tap whose voice changed the answer."
- event, whole, everyone counts.
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the plan runner over a seeded school of every grade, mistake seeding by answer type, the editable table, sort, the bar chart.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Check | Delete every odd row | Misspellings must be corrected, not removed, or the count drops. |
| Count | Count before cleaning | `Count` waits until every flagged cell has a fix. |
| Compare | Pick any grade | Only the grades left out change the winner. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `plan`; `send`.
2. `check`; `fix`; `sort`.
3. `compare`.
4. Everyone counts (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CSTA 2026 codes and the module line | data/modules.csv | data/standards/csta-2026-ids.txt | yes |
| Who is asked changes survey results (sampling bias) | American Statistical Association, "GAISE II" (2020), Level A and B | U.S. Census Bureau, "Statistics in Schools", sampling activities | yes |
| Closed answer lists reduce entry errors; data are cleaned before analysis | CSTA K-12 Computer Science Standards (2017), 1B-DA-06 | K-12 Computer Science Framework (2016), Data and Analysis, "Collection" and "Storage" | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad s23, 2026-11-10): 11 + 6 + 3 = 20 with dome first; 60 - 2 duplicates - 1 impossible - 1 blank = 56; 24 + 18 + 14 = 56 with swings first; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 clipboard and posters; at 680x425 posters as a tab.
2. Answer types are chosen and their effect on mistakes is seen. (E3-DAT-DC-09)
3. Rows are checked, fixed, sorted and counted. (E4-DAT-DC-09, E5-DAT-DC-09)
4. Two plans are compared, and the left-out voices are named. (E3-DAT-IM-11)
5. All rows are labeled illustration data.
6. `Read` reads every row and card; every control is 48 px or more.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: rows appear at once; no network requests.

## Open questions
- Overlap with lunch-survey-cleanup and catalog-column-rules, which also fix messy rows (default used: keep; this one plans first at grade 3-5 depth).

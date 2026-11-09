# Bike Lane Briefing

## One idea
Two articles disagree about whether the town of Alder Falls made its streets safer with new bike lanes, and the student, as the mayor's aide with the town's crash and traffic data open, pulls each claim onto a board, traces it to its evidence, stamps each disagreement Fact (the numbers themselves differ) or Interpretation (same numbers, different meaning), flags evidence that doesn't bear on the question, and writes the council a briefing, so they learn where texts really disagree and which side the evidence supports.

## Not like
- fake-or-fact-lab (6-8, spec): lateral reading on made-up web pages. Here two articles checked against the data they both cite, grade 8.
- two-authors-one-event (7, spec): same event, different spin. Here disagreement split into fact and interpretation.
- source-mixer (11, concept): several media for one answer. Here two opposing articles and a data drawer.
- logic-gym (7, spec): relevance and sufficiency in quick reps. Here a full case with real data work.
- verb-switchboard (8, spec, this batch): grammar of blame in headlines. Here what the numbers say.

## Who and how
- Grade 8, ELA, module "Conflicting Information" (Reading Informational Text). Standards: RI.8.9, RI.8.8.
- Driver: one student; class mode is a second case, a school's new lunch schedule and tardies, run on the projector (tool.json `driver: "student"`). Every claim is read on tap.
- The bike lane case (two articles, about 400 words each) and the lunch case. tool.json `modes: ["Bike lanes", "Lunch schedule", "Briefing"]`, `minutes: "35-45"`, `grades_label: "Grade 8"`.
- Nothing is saved; `Print` prints the claim board and the briefing. All data and articles are made up and labeled practice.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RI.8.9 (fact) | Stamp a disagreement Fact when the texts use different numbers, and find why (all crashes against bike crashes) | the stamped pair with both numbers from the drawer | 2 |
| RI.8.9 (interpretation) | Stamp a disagreement Interpretation when the numbers match and the meaning differs | the stamped pair and the chart | 2 |
| RI.8.8 (trace and evaluate) | Link each claim to the evidence its article gives, then check it in the data drawer | the claim board with links and checks | 3 |
| RI.8.8 (irrelevant evidence) | Stamp evidence that doesn't bear on safety Irrelevant | the Irrelevant stamp | 4 |
| RI.8.9, RI.8.8 | Write a briefing: fact disputes, interpretation disputes, what the data supports, one thing no one can know yet | the briefing | 5 |

## Screens and modes
Header (kit): title "Bike Lane Briefing"; `Articles`, `Claim board`, `Data drawer`, `Briefing`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** The mayor's office: two printed articles on the desk, a claim board on the wall, and a data drawer; Mayor Tom Brennan leans in the doorway with a coffee. First hint: "Tap the mayor's note to hear it." The note: "Council votes Thursday on more bike lanes. Tell me who's right." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**The articles** (written for Curio Class, labeled practice).
- City blog, "Bike Lanes Are Working": bike crashes fell from 14 in the year before the lanes to 11 in the year after; bike trips on Main Street rose by about a third; "biking is better for the planet".
- Neighborhood newsletter, "Lanes Made Main Street Worse": crashes rose from 212 to 230; October had the most crashes in three years; 40 parking spaces were lost.

**Claim board.** The student drags each claim from an article to the board and links it to the evidence its article gives. Pairs of opposing claims sit side by side.

**Data drawer.** Built on the data desk engine: a table of monthly crash counts for three years (all crashes and bike crashes as separate columns), bike counts on Main Street, and a map of crash spots. The student filters and charts. Charting all crashes and bike crashes shows the fact dispute: the blog counts bike crashes only, the newsletter counts all crashes. Charting October in full shows the newsletter's month was during a week of ice storms that raised crashes town-wide, including streets with no lanes. Dividing bike crashes by bike trips shows the rate fell more than the count.

**Stamps.** Each opposing pair gets Fact or Interpretation; each piece of evidence can get Irrelevant ("better for the planet" and "parking spaces" bear on other questions, not safety). The interpretation pair is 14 against 11: is it a real drop or chance? A "Could this be chance?" card shows that counts this small move up and down by a few from year to year by chance alone.

**Briefing.** About 150 words for the council, built from parts: where the texts disagree on fact (and why), where on interpretation, which claims the data supports, and one thing nobody can know yet (whether one year is a trend).

**Lunch schedule.** A second case on the projector with the same board: a school moved lunch later, and two posts disagree about tardies.

At 1366x768 the board and drawer fit side by side; at 680x425 the drawer is a tab.

## Content
Written for Curio Class: Alder Falls (made up), both articles, three years of monthly data with keyed fact and interpretation pairs, the October storm week, the lunch case. Every screen with data says "Practice data, made up."

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Stamps and links can be changed at any time.
- With Motion off stamps appear without the thump and charts draw at once.

## Look
- Accent `--brand` #2f6b3b bike-lane green (header, board pins, stamps); gold #f4c542 (a checked link, a glowing cherry-picked month); paper #f1f7f2; ink #0c2312; muted #4b5e4f. Scene: a small-town mayor's office with a window on Main Street.
- Contrast (WCAG 2.1, computed): white on brand 6.39:1; brand on paper 5.88:1; ink on paper 15.28:1; muted on paper 6.41:1; ink on gold 10.21:1.
- Never color alone: stamps carry words; chart series use shapes and dashes from the data desk engine.
- Different from this batch (newsroom navy, rust, club purple, calendar teal).

## Art
- People art goes to Gemini: Mayor Tom Brennan (an Irish American man in his fifties with rolled sleeves), 3 poses; "illustrated small-town mayor <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): a mayor's office (1); Main Street with a green bike lane, no faces (1); an icy street (1); a school cafeteria clock (1).
About 7 images. Drawn in code: articles, board, charts, map.

## Voice
Bank voice `friendly-dad` as Mayor Brennan and the hint voice (unique in this batch); articles and data cards are read by `science-narrator` (unique in this batch). `Curio.voice` with `scope: () => state.case + ':' + state.view + ':' + state.claim`, `welcomeAfter: true`.
- how `welcome`: "Two articles, one question: did the lanes make streets safer? Find where they really disagree, and check them against the numbers."
- event, whole, `claim`: the tapped claim.
- event `link`: "What evidence does it give?"
- event `stamp`: "Fact or interpretation?"
- event `irrelevant`: "Does that tell us about safety?"
- event `chance`: "Fourteen to eleven. Could that be chance?"
- event, whole, `briefing`: the briefing.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
data desk (`kit/data-desk.js`, described in full in docs/families/data-desk.md). This tool uses: `DataTable` for the monthly crash and traffic data, `t.where` for the filters, `Chart` (`line` and `bar`) for the drawer, and `renderTable` for the table view. The claim board, stamps, articles and briefing are tool-only code.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Stamps | Stamp every pair Fact | Each pair is keyed; the fact pair must also name the column difference (all crashes, bike crashes). |
| Irrelevant | Stamp every piece of evidence Irrelevant | Keyed relevant evidence stamped Irrelevant is counted and shown in the print. |
| Data checks | Skip the drawer | Board checks need a chart or filter opened for each claim. |
| Briefing | Pick a side and stop | The briefing needs all four parts, including one thing no one can know yet. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the mayor's note: note, `welcome` (queued, first time).
2. Board: `claim` on tap; `link` when placed; `stamp` when a pair forms.
3. Evidence: `irrelevant` as it fires. Drawer: `chance` when the 14 and 11 are charted.
4. Briefing: `briefing` (whole) on Read.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RI.8.8 and RI.8.9 wording | thecorestandards.org, Reading Informational Text Grade 8 | CCSS ELA 2010 PDF | yes |
| Small counts vary from year to year by chance; a change from 14 to 11 is within that range | Federal Highway Administration, Highway Safety Manual guidance on random variation and regression to the mean in crash counts | Khan Academy, statistical significance and chance variation | yes |
| A rate (crashes per trip) can fall while a count rises or holds, when exposure changes | Federal Highway Administration, safety performance measures (rates and counts) | Khan Academy, rates and ratios | yes |
Backed twice: 3. Cut: 0.

Design choices (not claims): Alder Falls, its articles and all data are made up and labeled practice.

Checks run (Python, scratchpad b24, 2026-11-09): with 25 bike crashes over two years, an 11 to 14 split has a two-sided exact binomial p of about 0.69, far from rare; the practice table's all-crash totals give 212 and 230 and bike-crash totals 14 and 11; bike crashes per 1,000 trips fall when trips rise by a third; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 board and drawer fit; at 680x425 the drawer is a tab.
2. Fact and Interpretation stamps check against keyed pairs with the reason. (RI.8.9)
3. Claims link to evidence and to a drawer check. (RI.8.8)
4. Irrelevant stamps work with keyed relevance. (RI.8.8)
5. The briefing needs its four parts. (RI.8.9, RI.8.8)
6. The lunch case works on the projector.
7. Print shows the board and briefing; data screens say practice.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: stamps and charts appear at once; no network requests.

## Open questions
- None for Cory.

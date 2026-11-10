# Printing Press

## One idea
The child runs a print shop in Wittenberg in the 1520s while a scribe at the desk next door copies the same text by hand: they choose what to print (a Bible page in Latin, a short pamphlet in German, a woodcut broadsheet with pictures), set type letter by letter, ink the forme, pull sheets on the press, and ship bundles to other cities, while copies spread across a map of Europe and the scribe's single copy crawls; paper supply, costs and how many readers each city has all matter; then a question builder about Gutenberg, the printers, readers who couldn't read, and Martin Luther leads to a written judgment of why the press mattered, and a board sorts what printing changed (cheaper books, faster spread, books in everyday languages) from what it didn't (most people still couldn't read; pictures, preachers and talk still carried ideas aloud), so a seventh grader learns to classify change and continuity and to ask questions about people to judge historical significance.

## Not like
- house-of-wisdom (7, spec): copying by hand and translating, earlier. Here the leap to printing.
- colonial-newsroom (8, concept): writing slanted headlines. Here making and shipping copies.
- mongol-messenger (7, spec): moving one message fast. Here making many copies.
- salt-and-gold-caravan (7, spec): a trading ledger. Here a shop's costs and readers.

## Who and how
- Grade 7, Social Studies (History), module "Renaissance and Reformation". Standards: D2.His.2.6-8 (classify series of historical events and developments as examples of change and/or continuity), D2.His.3.6-8 (use questions generated about individuals and groups to analyze why they, and the developments they shaped, are seen as historically significant).
- Format: simulator. Driver: one child alone, or two rival shops (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Six print runs, the map, the question builder, the significance judgment, the board. Extra: Rival shops (two players compete for paper and readers). tool.json `modes: ["Print shop", "Rival shops"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.2.6-8 | Sort eight cards into Changed and Stayed the same after the runs | the board with reasons | 4 |
| D2.His.3.6-8 | Build questions about four people or groups, read the answers, and write a significance judgment | the question builder; four answer cards; the judgment card | 3, 5 |
| D2.His.2.6-8 (runs) | Print and ship six runs, comparing the press counter with the scribe's | the two counters; copies spreading on the map | 2 |

## Screens and modes
Header (kit): title "Printing Press"; `Print shop`, `Rival shops`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A print shop: a type case with hundreds of little metal letters, a composing stick, a wooden press with a big screw, ink balls, stacks of paper and drying lines of printed sheets. Next door, a scribe at a slanted desk with a quill. Two counters: Press copies 0, Scribe copies 0. A map of Europe on the wall. The welcome is queued (`welcomeAfter: true`): "It's the 1520s in Wittenberg. Your shop has a printing press. Next door, a scribe copies by hand. Pick something to print." First hint: "Tap a job on the order board."

**Print runs (focus: the shop).** At 1366x768 the shop fills the left with the map right; at 680x425 they're tabs.
- Order board: a Bible page in Latin (for scholars and clergy), a short pamphlet in German (cheap, fast, for townspeople), a woodcut broadsheet (a big picture with a few words, for people who can't read well).
- Set type: the child drops letters into the composing stick for one short line (a few letters only; the rest fill in), then taps through ink, place paper, pull, hang to dry. Each step shows what it is.
- The model (made for this game, from historians' estimates): the press makes hundreds of sheets a day; the scribe makes a few pages a day. One run of 1,000 pamphlets takes the press a few days and would take the scribe years.
- Ship: the child picks cities on the map (Leipzig, Nuremberg, Augsburg, Strasbourg, Basel, Antwerp); copies spread as dots. Cities with more readers buy more; paper runs short if the shop overprints.
- Cards: Gutenberg printed his Bible in Mainz about 1455; by 1500 presses ran in more than 250 European towns; in the years after 1517 Luther's German pamphlets became best-sellers, and his opponents printed replies too.

**The question builder (D2.His.3.6-8).** Four people or groups: Johannes Gutenberg; the printers (the shop's own master and workers); readers and listeners (including those who couldn't read and heard pamphlets read aloud); Martin Luther and his opponents. For each, the child builds a question from tiles (Who? What did they want? What changed because of them? Who disagreed?), then opens the answer card. Each answer is short, sourced, and fair to Catholic and Protestant sides.

**The board (D2.His.2.6-8).** Eight cards: Changed (books much cheaper; ideas spread in weeks, not years; more books in German and other everyday languages; the same text in every copy) or Stayed the same (most people couldn't read; priests and preachers still spoke to crowds; pictures still carried ideas; the Church remained powerful in much of Europe). Each sort plays a reason line.

**The judgment (the aha).** "The printing press mattered because ___, but it didn't change ___." (tiles plus a free line), with one person from the question builder named. Narrator: "Significance isn't just how big a change was. It's who it changed, and who it left out."

**The end.** The counters, the map, the board and the judgment. `Print` prints them.

**Rival shops (extra).** Two shops share the paper supply and the cities' readers.

## Content
- Three job types, a press and scribe model (made for this game), six cities with reader counts (made for this game, scaled from town sizes), fact cards, four question-builder subjects with answers, eight board cards.
- The shop, its workers and the model are made up and labeled; Gutenberg, Luther, his opponents, dates and the spread of printing are real.
- The Reformation is shown fairly to all sides: Catholic replies are printed too, and no side's woodcuts are shown as true.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Typesetting asks for only a few letters so it never drags; the rest fill in.
- Overprinting runs paper short and the next run waits.
- Keyboard: Tab to the order board, type case, press steps, map cities, builder tiles and board; Enter to choose.
- With Motion off the press doesn't swing and dots appear on the map without spreading.

## Look
- Accent `--brand` #5a3e2b printer's sepia (header, the press, the order board); gold #f4c542 (the job in hand, a right sort); paper #f8f4ef; ink #1f140c; muted #5c544d.
- Contrast (WCAG 2.1, computed): white on brand 9.73:1; brand on paper 8.88:1; ink on paper 16.48:1; muted on paper 6.78:1; ink on gold 11.10:1.
- Never color alone: counters carry numbers and labels; map dots grow in size, not only shade.
- Different from this batch (archive green, Philadelphia navy, canal blue, signal orange).

## Art
- Public domain: a Gutenberg Bible page (Library of Congress); a 1520s German pamphlet title page by Luther and one by a Catholic opponent (Library of Congress or a public domain digital library, checked at build); the 1568 woodcut of a print shop by Jost Amman (public domain). Each with credit.
- Local FLUX (`scripts/localart.py`): the print shop (1, 16:9); the scribe's desk (1, 3:2); a map of Europe styled as an old print (1, 16:9).
- People art goes to Gemini with `people: true`: the print master, a compositor, the scribe, Gutenberg, Luther, a Catholic writer, a townswoman listening to a reading (7; cutout yes).
About 13 images.

## Voice
Two bank voices, each unique in this batch: `lively-host` as the print master and narrator; `wise-mentor` as the scribe and the answer cards. `Curio.voice` with `scope: () => state.mode + ':' + state.run + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `job`: "Pick a job from the order board."
- how `set`: "Drop the letters into the stick, then tap Ink."
- how `ship`: "Tap cities to ship your copies."
- event, whole, each fact card.
- how `ask`: "Build a question about this person, then open the answer."
- event, whole, each answer card.
- how `sort`: "Drag each card to Changed or Stayed the same."
- how `judge`: "Finish the judgment."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the shop steps, the press and scribe model, the shipping map, the question builder, the board, the judgment card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Runs | Print only Latin Bibles | Few readers buy them; the map stays thin and the card says why. |
| Questions | Open answers without building a question | Each answer opens only after a question is built. |
| Board | Put everything in Changed | Each card checks; "most people couldn't read" in Changed plays a reason line. |
| Judgment | Leave the "didn't change" blank | Print waits for it. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `job`; `set`; `ship`.
2. Fact cards (whole), each waits.
3. `ask`; answer cards (whole).
4. `sort`; `judge`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.2.6-8 and D2.His.3.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Gutenberg printed his Bible in Mainz about 1455 | Library of Congress, "The Gutenberg Bible" | Encyclopaedia Britannica, "Johannes Gutenberg" | yes |
| By 1500 presses ran in more than 250 European towns | Eisenstein, "The Printing Revolution in Early Modern Europe" (Cambridge, 1983) | Britannica, "Printing: the spread of printing" | yes |
| A press made hundreds of sheets a day; a scribe a few pages | Britannica, "Printing: Gutenberg's press" | Pettegree, "The Book in the Renaissance" (Yale, 2010) | yes, as estimates |
| Luther's German pamphlets were best-sellers after 1517; opponents printed replies | Edwards, "Printing, Propaganda, and Martin Luther" (University of California Press, 1994) | Pettegree, "Brand Luther" (Penguin, 2015) | yes |
| Most people couldn't read; pamphlets were read aloud and pictures carried ideas | Scribner, "For the Sake of Simple Folk" (Cambridge, 1981) | Pettegree (2015) | yes |
| Jost Amman's 1568 print-shop woodcut | Britannica, "Jost Amman" | The Met, Amman's "Book of Trades" prints | yes |
Backed twice: 7. Cut: 0.

Sensitivity note: the Reformation is shown fairly to all sides; Catholic and Protestant writers both appear, and the harsh woodcut propaganda of both sides is described, not displayed. A fresh-agent read of the answer cards is needed before build.

Checks run (Python, scratchpad r14, 2026-11-09): 1,000 pamphlets of 8 pages at a few hundred sheets a day take the press a few days, and at 3 pages a day take one scribe about 7 years; four Changed and four Stayed cards; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 shop and map; at 680x425 tabs.
2. Six runs print and ship with both counters. (D2.His.2.6-8)
3. Four questions are built and answered. (D2.His.3.6-8)
4. The board sorts eight cards with reasons. (D2.His.2.6-8)
5. The judgment names a change, a limit and a person. (D2.His.3.6-8)
6. Rival shops share paper and readers.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no swinging press or spreading dots; no network requests.

## Open questions
- Sensitivity flag: Reformation religious conflict (default used: Catholic and Protestant voices both shown, propaganda described not displayed, fresh-agent read before build).

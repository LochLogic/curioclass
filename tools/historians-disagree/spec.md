# Historians Disagree

## One idea
Two short history articles sit side by side, each explaining why the Mongol Empire grew so fast in the early 1200s: one says it was horse archers and organization (riders with spare horses, an army in units of ten, a hundred, a thousand and ten thousand, a relay of messengers), the other says a run of unusually wet years, found in the tree rings of old Mongolian pines, fed the grasslands and the horses; the child highlights each article's central claim and restates it, opens the footnote drawer and sorts every source by kind (a chronicle from the Mongol court, a chronicle by a Persian official serving the Mongols, a chronicle by a victim's neighbor, a traveler's report, archaeology, tree rings), fills a credibility card for each (who made it, when, and what it can and can't show), and writes a verdict; both arguments can be partly right, and a source's kind shapes what it can prove (tree rings show rain, not decisions), so a seventh grader learns to explain the central arguments in secondary works, classify the sources they rest on, and critique arguments for credibility.

## Not like
- mongol-messenger (7, concept): the same empire as a relay race. Here two historians' arguments about it.
- panel-of-experts (7, concept): four fields answer one question. Here two arguments and their sources.
- unlabeled-archive (7, concept): identifying primary sources. Here secondary works and what they rest on.
- museum-label-writer (6, spec): writing one explanation. Here judging two.

## Who and how
- Grade 7, Social Studies (History), module "Historians Disagree". Standards: D2.His.17.6-8 (explain the central arguments in secondary works of history on related topics in multiple media), D2.His.9.6-8 (classify the kinds of historical sources used in a secondary interpretation), D4.4.6-8 (critique arguments for credibility).
- Format: explorer. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Two articles, the footnote drawers, credibility cards, the verdict. Extra: A third article (a short piece combining both, with its own footnotes to sort and judge). tool.json `modes: ["Two articles", "A third article"]`, `minutes: "25-35"`, `grades_label: "Grade 7"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.17.6-8 | Highlight each article's central claim and restate it from tiles plus one free line | the highlighted sentence; the restated claim under each article | 2 |
| D2.His.9.6-8 | Open each footnote and sort its source into one of six kinds | the sorting shelf with six labeled bins; each article's source mix bar | 3 |
| D4.4.6-8 | Fill a credibility card for each source (who, when, what it can show, what it can't) and write a verdict | the cards; the verdict card with a reason and one weakness for each article | 4, 5 |

## Screens and modes
Header (kit): title "Historians Disagree"; `Two articles`, `A third article`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** Two short articles side by side, each a page with a title and footnote numbers, a closed drawer under each. Above them a question: "Why did the Mongol Empire grow so fast?" The welcome is queued (`welcomeAfter: true`): "Two historians answer the same question in different ways. Your job is to find each one's main argument, check their sources, and decide which holds up better. Tap the first article to read it." First hint: "Tap Article A."

**The articles (made for this game, built from real scholarship and labeled).** At 1366x768 the articles sit side by side with the drawer below; at 680x425 one article at a time with tabs.
- Article A, "Riders, Ranks and Relays" (about 200 words): Chinggis Khan united the steppe peoples by 1206 and organized his army into units of 10, 100, 1,000 and 10,000, mixing clans so loyalty went to the army; each rider kept several horses; horse archers struck fast; a relay of messenger stations carried orders. Footnotes: the Secret History of the Mongols; Juvaini's History of the World Conqueror; the report of John of Plano Carpini (1240s); a modern historian's study of Mongol warfare.
- Article B, "Fifteen Wet Years" (about 200 words): tree rings from very old Siberian pines on a lava field in central Mongolia show that 1211 to 1225 were the wettest, mildest years in more than a thousand, just as the empire spread fastest; more rain meant more grass, more horses and more food for the armies; a drought before 1206 may have pushed the steppe into war. Footnotes: the tree-ring study (Pederson and others, 2014); Ibn al-Athir's chronicle of the invasions; archaeology of Karakorum, the Mongol capital.

**Central claim (D2.His.17.6-8).** The child highlights the one sentence in each article that holds its argument, then restates it from tiles ("A says the Mongols grew fast because ___"). Highlighting a detail instead plays "That's a detail. Which sentence does the rest of the article try to prove?"

**The footnote drawer (D2.His.9.6-8).** Each footnote opens a card with a picture and a short description. The child sorts each into one of six bins: chronicle from the Mongol court (the Secret History, written within decades of Chinggis Khan); chronicle by an official serving the Mongols (Juvaini, a Persian who worked for them); chronicle from the conquered side (Ibn al-Athir, an Arab historian in Mosul who called the invasions a great disaster); traveler's report (Carpini, sent by the Pope); archaeology (Karakorum's streets and workshops); natural science (tree rings). Each article gets a bar showing its mix of kinds.

**Credibility cards (D4.4.6-8).** For each source, the child fills four lines from tiles: who made it; when; what it can show (the Secret History: how the Mongols saw themselves; tree rings: how wet each year was); what it can't show (tree rings can't show decisions; Juvaini worked for the Mongols and may flatter them; Ibn al-Athir saw them as enemies; the Secret History tells the story the court wanted).

**The verdict (the aha).** The child picks one: A holds up better, B holds up better, or both are partly right; then writes one reason and one weakness for each article. Narrator: "Good historians often find several causes. Here, the rain may have fed the horses, but someone still had to lead the riders. And each source can only prove what it can see."

**The end.** The two restated claims, the sorted shelf, the credibility cards and the verdict. `Print` prints them.

**A third article (extra).** "Rain and Riders" combines both, with new footnotes to sort and judge.

## Content
- Two articles (about 200 words each) and a third, made for this game from real scholarship and labeled "written for this game"; seven real sources with descriptions; six source kinds; credibility tiles; verdict tiles.
- Every source and fact named in the articles is real; the articles themselves are made up and labeled.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Highlighting snaps to whole sentences.
- A credibility card can't be done until its four lines are filled.
- Keyboard: Tab to articles, sentences, footnotes, bins and cards; Enter to highlight, open, sort and pick.
- With Motion off the drawer opens without sliding.

## Look
- Accent `--brand` #9b2335 editor's red (header, highlights, footnote numbers); gold #f4c542 (the active sentence, a filled card); paper #fbf1f2; ink #2e0a10; muted #62504f.
- Contrast (WCAG 2.1, computed): white on brand 7.82:1; brand on paper 7.06:1; ink on paper 16.25:1; muted on paper 6.82:1; ink on gold 11.06:1.
- Never color alone: highlights are underlined too; each bin carries a label and an icon.
- Different from this batch (atlas indigo, Atlantic ochre, lake jade, purple).

## Art
- Public domain: illustrated pages of Mongol riders from Rashid al-Din's Jami al-Tawarikh (Bibliothèque nationale de France or Staatsbibliothek Berlin, rights checked at build), with credit.
- Local FLUX (`scripts/localart.py`): an old Siberian pine on a lava field (1, 3:2); a cut tree section with rings (1, 1:1); Karakorum excavation (1, 3:2).
- Drawn in code: the tree-ring chart of wet and dry years for Article B (from the published study's data, rounded), the article pages, bins, cards.
About 5 images.

## Voice
Two bank voices, each unique in this batch: `knowing-guide` as the narrator; `news-reader` as the reader of both articles and footnote cards. `Curio.voice` with `scope: () => state.mode + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each article when the child taps Read article.
- how `claim`: "Highlight the sentence that holds the main argument."
- how `restate`: "Say the argument in your own words with the tiles."
- how `sort`: "Open a footnote and drag it to its kind."
- how `cred`: "Fill the four lines on this card."
- how `verdict`: "Pick your verdict, then give a reason and a weakness for each."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: two article pages with sentence highlighting, footnote drawers, the six-bin shelf, credibility cards, the verdict.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Claim | Highlight the first sentence | Each article's claim sits elsewhere; a detail plays the hint. |
| Sort | Drop all footnotes in one bin | Each source checks its kind; the miss says what made it ("Who wrote this, and for whom?"). |
| Credibility | Fill tiles at random | Each line checks against the source; "can't show" must name a limit. |
| Verdict | Pick with no reasons | Print waits for a reason and a weakness for each. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Article (whole), when tapped.
2. `claim`; `restate`.
3. `sort`; `cred`.
4. `verdict`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.17.6-8, D2.His.9.6-8 and D4.4.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Tree rings show 1211 to 1225 as an unusually wet, mild run as the empire spread; drought before | Pederson, Hessl and others, "Pluvials, droughts, the Mongol Empire, and modern Mongolia," PNAS (2014) | Smithsonian Magazine and Columbia's Lamont-Doherty Earth Observatory news on the study (2014) | yes |
| Chinggis Khan united the steppe by 1206; decimal army units; spare horses; messenger relays | Encyclopaedia Britannica, "Genghis Khan" | May, "The Mongol Art of War" (Westholme, 2007) | yes |
| The Secret History of the Mongols, a Mongol court chronicle of the 1200s | Britannica, "The Secret History of the Mongols" | de Rachewiltz, translation and commentary (Brill, 2004) | yes |
| Juvaini, a Persian official serving the Mongols, wrote the History of the World Conqueror | Britannica, "Juvaini" | Encyclopaedia Iranica, "Jovayni, Ala-al-Din" | yes |
| Ibn al-Athir wrote of the invasions as a great disaster | Britannica, "Ibn al-Athir" | Richards, translation of "The Chronicle of Ibn al-Athir" (Ashgate, 2006 to 2008) | yes |
| John of Plano Carpini's report from the 1240s | Britannica, "Giovanni da Pian del Carpine" | Dawson, "The Mongol Mission" (1955) | yes |
| Archaeology of Karakorum | Britannica, "Karakorum" | German Archaeological Institute, Karakorum excavations | yes |
Backed twice: 8. Cut: 0.

Checks run (Python, scratchpad r12, 2026-11-09): seven footnotes span all six kinds; 1211 to 1225 is fifteen years counting both ends; each article is under 220 words in the draft; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 articles side by side; at 680x425 tabs.
2. Each article's central claim is highlighted and restated. (D2.His.17.6-8)
3. All footnotes sort into six kinds with source-mix bars. (D2.His.9.6-8)
4. Each credibility card checks four lines. (D4.4.6-8)
5. The verdict needs a reason and a weakness for each article. (D4.4.6-8)
6. A third article loads its own footnotes.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no sliding; no network requests.

## Open questions
None.

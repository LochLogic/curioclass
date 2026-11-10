# Inflation Wallet

## One idea
The student keeps the wallet, the pantry and the savings book of the Keller family (made for this game) in Berlin from 1919 to 1933, a clerk, a seamstress, a grandmother with war bonds and a teenage son; each turn is a month in 1922 to 1924 and a year after that, prices follow real series, and the student decides when to shop, whether to hold marks, buy goods or trade for dollars, while the family's savings melt in 1923 (a dollar cost 4.2 marks in 1914 and about 4.2 trillion in November 1923), the new Rentenmark steadies things, and the Depression brings mass unemployment from 1930; at each real election the family members say what worries them and a chart shows the real national vote, including the Nazi party's climb from under 3 percent in 1928 to the largest party in July 1932; at the end the student weighs six causes on a board (hyperinflation, the Depression, the Versailles burden, street violence, the constitution's emergency powers, and elite deals) and finds that the Nazi surge came after 1929, not in 1923, then a constitution panel shows how Weimar's own democratic rules were used to dismantle it in 1933, so a tenth grader learns to analyze complex causes and their timing and to evaluate a democratic system and how it failed.

## Not like
- stock-market-1929 (11, spec): U.S. margin trading. Here a German family's wallet.
- behind-the-podcast (11, concept): sources about the U.S. Depression. Here living through Germany's two crises.
- alliance-web (9, spec): the causes of the war. Here what the peace and the crises did next.
- ideas-that-spread (9, spec): scoring new constitutions. Here one constitution under strain.

## Who and how
- Grade 10, Social Studies (World History and Civics), module "Between the Wars". Standards: D2.His.14.9-12 (analyze multiple and complex causes and effects of events in the past), D2.Civ.8.9-12 (evaluate social and political systems in different contexts, times, and places, that promote civic virtues and enact democratic principles).
- Format: simulator. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- About 40 turns from 1919 to 1933, the wallet, pantry and savings book, the election chart, the cause board, the constitution panel. Extra: Same years elsewhere (Italy under Mussolini from 1922 and the Soviet Union under Stalin, compared on the same constitution panel). tool.json `modes: ["The Kellers", "Same years elsewhere"]`, `minutes: "35-45"`, `grades_label: "Grade 10"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.14.9-12 | Live through both crises, then weigh and date six causes on the board | the wallet and price line; the election chart; the cause board with a timeline | 2, 3, 4 |
| D2.Civ.8.9-12 | On the constitution panel, rate each democratic rule and mark how it was used against democracy | the panel: rights, elections, proportional representation, Article 48 | 5 |

## Screens and modes
Header (kit): title "Inflation Wallet"; `The Kellers`, `Same years elsewhere`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A Berlin kitchen in 1922: a loaf of bread, Otto's pay packet, Grandma Ilse's savings book and war bonds, Greta's sewing, Paul at the table. The welcome is queued (`welcomeAfter: true`): "This is Berlin, 1922. The war is over, the Kaiser is gone, and Germany is a democracy. Prices are rising. Spend now or save? Tap the pay packet." First hint: "Tap the pay packet."

**The wallet years (focus: the kitchen and the wallet).** At 1366x768 the kitchen fills the left with the wallet, pantry and price line right; at 680x425 the wallet is a tab.
- 1919: the Weimar constitution; the Versailles Treaty and reparations; a short catch-up card.
- 1922 to 1923, monthly turns: the student chooses shop now, hold marks, buy goods to store, or trade for dollars. Prices follow the real Berlin series, rounded and labeled. January 1923: France and Belgium occupy the Ruhr; the government prints money to pay striking workers. By autumn, Otto is paid twice a day and Greta runs to the shop at lunch. Grandma Ilse's savings and war bonds become worthless.
- November 1923: the Rentenmark (one trillion paper marks for one new mark); prices steady. 1924: the Dawes Plan and American loans.
- 1924 to 1928, yearly turns: steadier years.
- 1929 to 1932: the Depression; loans dry up; Otto loses his job; about six million registered unemployed by early 1932.
- 1933: the close.
- Each turn a reason line explains what happened to the family's money and why.

**Elections (the ballot layer).** At each real Reichstag election (1919, 1920, May and December 1924, 1928, 1930, July and November 1932, March 1933) each family member says in one line what worries them. The student does not cast votes for parties. A chart shows the real national vote shares; the student marks the year the Nazi vote first passes 10 percent (1930). Party programs are summed up in plain words by a historian's note, and the Nazis' antisemitism and violence are named plainly with what followed. No Nazi symbols are shown.

**The cause board (the aha, D2.His.14.9-12).** Six causes: hyperinflation (1923), the Depression (1929 to 1932), the Versailles burden, street violence by armed party groups, Article 48 emergency powers, and elite deals (Hindenburg's circle appointing Hitler chancellor on January 30, 1933). The student weights each and places it on a timeline under the vote chart. The board checks timing: the Nazi vote was 2.6 percent in 1928, after the hyperinflation was over, and rose to 37.3 percent in July 1932 during the Depression. Narrator: "The memory of 1923 made people afraid. But the votes came after 1929."

**The constitution panel (D2.Civ.8.9-12).** Weimar's rules: equal voting rights for men and women from age 20; a bill of rights; proportional representation; Article 48 emergency decrees. The student rates each as a democratic principle, then marks how it was used against democracy: chancellors governed by decree from 1930; after the Reichstag fire (February 27, 1933) a decree suspended rights; the Enabling Act (March 23, 1933) let Hitler make laws without the Reichstag; in April 1933 the regime organized a boycott of Jewish businesses and removed Jewish civil servants. One line from the student: "One rule I would change to protect a democracy is ___ because ___."

**The end.** The wallet history, the vote chart, the board and the panel. `Print` prints them.

**Same years elsewhere (extra).** Italy under Mussolini from 1922 and the Soviet Union under Stalin on the same constitution panel.

## Content
- About 40 turns with real price and exchange-rate series (rounded, labeled), event cards, the family's lines, nine elections with real vote shares, six causes, the constitution panel with four rules and how each was used.
- The Keller family is made up and labeled; prices, events, votes, laws and quotes are real and sourced.
- Nazi antisemitism and violence are named plainly; no Nazi symbols or posters appear.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each turn waits for a choice; the student can't skip months in 1923.
- Holding marks in 1923 always loses value, with a reason line; buying goods or dollars protects some.
- Keyboard: Tab to the wallet choices, the chart, the board and the panel; Enter to choose and place.
- With Motion off banknotes don't pile up and the price line draws at once.

## Look
- Accent `--brand` #5a2b2b wallet maroon (header, the wallet, the board); gold #f4c542 (the choice in hand, the year marked); paper #f9f2f1; ink #1e0b0b; muted #5e5050.
- Contrast (WCAG 2.1, computed): white on brand 11.57:1; brand on paper 10.47:1; ink on paper 17.15:1; muted on paper 6.94:1; ink on gold 11.65:1.
- Never color alone: party lines on the vote chart carry names and patterns; prices carry numbers.
- Different from this batch (workbench green, sea teal, terracotta, circuit violet).

## Art
- Public domain banknotes (Reichsbank notes of 1922 and 1923, including the 100 trillion mark note, and a Rentenmark note; checked at build), each with credit.
- Local FLUX (`scripts/localart.py`): the Keller kitchen at four moments (1922, autumn 1923, 1928, 1932) (4, 16:9); a Berlin street with a bread line (1, 16:9).
- People art goes to Gemini with `people: true`: Otto, Greta, Grandma Ilse, Paul (4; cutout yes).
- Drawn in code: the wallet, the price line, the vote chart, the board, the panel.
About 12 images.

## Voice
Two bank voices, each unique in this batch: `gentle-storyteller` as the narrator and hints; `friendly-dad` as Otto, who speaks the family's worries. `Curio.voice` with `scope: () => state.mode + ':' + state.turn + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `choose`: "Pick what to do with this month's pay."
- event, whole, each turn's reason line.
- event, whole, each family line at an election.
- how `chart`: "Mark the year the Nazi vote first passed 10 percent."
- how `board`: "Weigh each cause and place it on the timeline."
- how `panel`: "Rate each rule, then mark how it was used."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the turn model with real price series, the wallet and pantry, the vote chart, the cause board with timing checks, the constitution panel.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Cause board | Weight hyperinflation highest and place it in 1932 | Each cause's date checks against the record. |
| Timing | Skip the vote chart | The board opens only after the 10 percent year is marked. |
| Panel | Rate every rule as harmful | Each rule needs its democratic purpose named before how it was used. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `choose`; reason line (whole), each turn.
2. Family lines (whole) at each election; `chart`.
3. `board`.
4. `panel`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.14.9-12 and D2.Civ.8.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| The mark: 4.2 to the dollar in 1914, about 4.2 trillion in November 1923; the Rentenmark at one trillion to one | Bresciani-Turroni, "The Economics of Inflation" (1937) | Fergusson, "When Money Dies" (1975) | yes |
| The Ruhr occupation (January 1923) and money printing to pay strikers | Feldman, "The Great Disorder" (Oxford, 1993) | Britannica, "Ruhr occupation" | yes |
| About six million registered unemployed by early 1932 | Evans, "The Coming of the Third Reich" (Penguin, 2003) | German Historical Institute, German History in Documents and Images | yes |
| Nazi vote shares: 2.6% (1928), 18.3% (1930), 37.3% (July 1932), 33.1% (November 1932), 43.9% (March 1933) | Falter et al., "Wahlen und Abstimmungen in der Weimarer Republik" (1986) | United States Holocaust Memorial Museum, "Nazi Party election results" | yes |
| The Weimar constitution: voting from 20 for men and women, proportional representation, Article 48 | German Historical Institute, Weimar constitution text | Britannica, "Weimar Republic" | yes |
| Governing by decree from 1930; the Reichstag fire decree (February 28, 1933); the Enabling Act (March 23, 1933) | United States Holocaust Memorial Museum, Holocaust Encyclopedia | Evans (2003) | yes |
| The April 1, 1933 boycott and the April 1933 civil service law | United States Holocaust Memorial Museum | Yad Vashem, "1933" | yes |
Backed twice: 8. Cut: 0.

Sensitivity note: the Nazi rise and its antisemitism are named plainly with sources; no Nazi symbols or posters appear; the student never casts a vote for a party, and the family's worries are voiced without endorsing any party. A fresh-agent read of the election and panel cards is needed before build.

Checks run (Python, scratchpad r18, 2026-11-09): 4.2 trillion over 4.2 is one trillion, matching the Rentenmark rate; the Nazi vote rose 34.7 points from 1928 to July 1932; nine elections in date order; the 10 percent year is 1930; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 kitchen and wallet; at 680x425 tab.
2. Monthly turns in 1923 follow real prices and melt the savings. (D2.His.14.9-12)
3. The vote chart shows real shares and the 10 percent year is marked. (D2.His.14.9-12)
4. The cause board checks each cause's timing. (D2.His.14.9-12)
5. The constitution panel rates each rule and marks how it was used. (D2.Civ.8.9-12)
6. No Nazi symbols appear and the student never votes for a party.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no piling notes; no network requests.

## Open questions
- Sensitivity flag: the Nazi rise and antisemitism (default used: named plainly with sources, no Nazi symbols, fresh-agent read before build).
- The idea card has family members weigh parties at each election; letting the student pick a party risks a student "voting Nazi" as a game move (default used: family members voice worries only, and the student reads the real results).

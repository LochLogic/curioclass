# Tools for Change

## One idea
The town library is about to close on Saturdays, and the child holds a hand of six strategy cards (petition, boycott, letter, speaking at a meeting, voting, volunteering), each backed by one real example from long ago and one from recent years (an 11-year-old's 1860 letter to Abraham Lincoln and an 8-year-old's 2016 letter to President Obama about Flint's water); they flip the cards, play up to three on the problem, predict what each will do, and watch the town respond with an honest, modeled result (some tools need many people or a long time, and a boycott of a free library hurts only the boycotters), then turn the plan into a letter or poster for someone outside the classroom, so a fifth grader learns how people have changed society and how to match a tool to the person who decides.

## Not like
- changemaker-cards (2, spec): collecting people who made a difference. Here choosing strategies and predicting results.
- town-council (2, spec): how a council decides. Here how people outside the council push for a change.
- bill-to-law-board-game (4, spec): one path through the legislature. Here six tools for any problem.
- levers-of-power (8, concept): roles and levels of government. Here strategies for citizens.

## Who and how
- Grade 5, Social Studies (Civics and Taking Action), module "Tools for Change". Standards: D2.Civ.14.3-5 (illustrate historical and contemporary means of changing society), D4.6.3-5 (draw on disciplinary concepts to explain the challenges people have faced and opportunities they have created, in addressing local, regional, and global problems at various times and places), D4.7.3-5 (explain different strategies and approaches students and others could take in working alone and together to address local, regional, and global problems, and predict possible results of their actions), D4.3.3-5 (present a summary of arguments and explanations to others outside the classroom using print and oral technologies).
- Format: cards. Driver: one child alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Three parts: Flip the cards, Play a plan, Make it. Extra: two more local problems (a park with broken swings, a truck route past the school). tool.json `modes: ["Library", "Swings", "Truck route"]`, `minutes: "25-35"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.Civ.14.3-5 | Flip each strategy card to read its past and recent example | the two examples on every card back, with dates | 2 |
| D4.6.3-5 | For each example, pick the challenge the people faced and the opening they used | the challenge and opening chips on the card back | 3 |
| D4.7.3-5 | Play up to three cards and predict a result for each before the town responds | the prediction tiles; the town's modeled response | 4 |
| D4.3.3-5 | Build a letter or a poster from the plan and print it | the letter or poster maker | 5 |

## Screens and modes
Header (kit): title "Tools for Change"; `Library`, `Swings`, `Truck route`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A town map. A pin on the library with a sign: "Closed Saturdays starting next month." A fan of six face-down cards at the bottom. Who decides is shown on the map: the Library Board meets the first Tuesday of each month; the City Council sets the library's budget. The welcome is queued (`welcomeAfter: true`): "The library might close on Saturdays. People have changed things like this before. Flip a card to see how." First hint: "Tap a card to flip it."

**Flip the cards (focus: one card back at a time).** Each card back has two examples, each with a picture, a date, what the people faced and what changed. After reading, the child picks the challenge and the opening from chips (D4.6.3-5).
1. Petition. Long ago: in the 1830s women and men sent thousands of antislavery petitions to Congress; the House passed a "gag rule" in 1836 to ignore them; people kept sending them, and the rule ended in 1844. Recent: in 2012, Julia Bluhm, 14, started an online petition asking Seventeen magazine to print one photo spread a month that wasn't digitally changed; tens of thousands signed and the editors promised to stop changing girls' bodies and faces in photos.
2. Boycott. Long ago: the Montgomery Bus Boycott, 1955 to 1956, 381 days, ended with the Supreme Court ruling that segregated buses were unconstitutional. Later: the grape boycott led by Cesar Chavez and Dolores Huerta, 1965 to 1970, ended with the first contracts for grape workers (see Open questions).
3. Letter. Long ago: in October 1860, Grace Bedell, 11, wrote to Abraham Lincoln that he'd look better with whiskers; he grew a beard and met her on his way to Washington in February 1861. Recent: in 2016, Mari Copeny, 8, wrote to President Obama about Flint, Michigan's water; he wrote back and visited Flint that May.
4. Speaking at a meeting. Long ago: in 1851, Sojourner Truth spoke at a women's rights convention in Akron, Ohio, about the rights of women, including Black women. Recent: in 2018, Dane Best, 9, spoke to the town board of Severance, Colorado, and the board voted unanimously to end its old ban on throwing snowballs.
5. Voting. Long ago: in 1920 the 19th Amendment gave women the right to vote across the country. Recent: in 2013 Takoma Park, Maryland, became the first U.S. city to let 16- and 17-year-olds vote in city elections.
6. Volunteering. Long ago: Clara Barton nursed soldiers in the Civil War and founded the American Red Cross in 1881. Recent: in 2008 Katie Stagliano, 9, grew a 40-pound cabbage that helped feed about 275 people at a soup kitchen and started Katie's Krops, which grows food for people in need.

**Play a plan (focus: the library and the played cards).** At 1366x768 the map sits above three play slots; at 680x425 the map shrinks and the slots stack.
- The child plays up to three cards. For each, they predict on three tiles: Who does it reach? (the Library Board, the City Council, nobody who decides); How many people does it need? (one, a few, many); How fast? (this month, this year, years).
- `See what happens` plays the town's modeled response, honest and made for this game:
  - Letter to the Library Board: the board chair reads it at the next meeting and puts Saturdays on the agenda.
  - Petition: 300 signatures from library users; the board sees how many people care.
  - Speaking at the meeting: three kids and a parent speak; the board asks the librarian what Saturday mornings would cost ($9,000 a year for one staff member, four hours a week).
  - Volunteering: the Friends of the Library offer to run a Saturday story time, but volunteers can't check out books or run the desk, so it helps a little.
  - Voting: the library budget is on the ballot next November; it could add money, but not until next year.
  - Boycott: the library is free; staying away makes the visitor count drop and gives the board a reason to cut more. The narrator: "A boycott works when it costs the decision maker money. This one costs only you."
- The best plans match the tool to the decision maker: a letter, a petition and speaking at the meeting together lead to the board finding money for Saturday mornings, 9 to 1. Any plan gets an honest result and a "what could make it stronger" line; no plan "loses".
- Predictions are compared with results: each match lights a check; each miss shows why.

**Make it (D4.3.3-5).** The child picks Letter (to the Library Board) or Poster (for the library door). Letter: tiles for the opening (who I am), the problem, two reasons (from the played cards and the town facts), the ask (open Saturdays 9 to 1), and a thank-you, plus a free-text line. Poster: a headline, one fact, one ask, the meeting date. `Print` prints the letter or poster.

**The end.** The map with the library open Saturday mornings (or the child's honest result) and the six cards. Narrator: "People have used these tools for two hundred years. Pick the tool that reaches the person who decides, and bring friends."

**Swings and Truck route (extras).** Swings: the Parks Department fixes playground equipment; a letter with photos and a call to the city's 311 line works fastest. Truck route: the City Council sets truck routes; speaking at a meeting with a petition and a traffic count works; a boycott of local stores turns businesses against the kids.

## Content
- Six strategy cards with two real examples each (12 examples, each with a date, challenge, opening and result); challenge and opening chips; the library problem with six modeled responses; the letter and poster makers; two extra problems with their own decision makers and responses.
- The town, the library board, the costs and the responses are made for this game and labeled; every example on the cards is real and sourced.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `See what happens` shows only after each played card has three predictions.
- A played card can be taken back before `See what happens`.
- Keyboard: Tab through cards and tiles; Enter to flip or play; arrows choose a slot or tile.
- With Motion off cards turn without flipping and the map changes without fading.

## Look
- Accent `--brand` #00607a town teal (header, card backs, play slots); gold #f4c542 (the played card, a matched prediction); paper #edf6f8; ink #022029; muted #4a5a5f.
- Contrast (WCAG 2.1, computed): white on brand 7.11:1; brand on paper 6.48:1; ink on paper 15.42:1; muted on paper 6.56:1; ink on gold 10.40:1.
- Never color alone: predictions that match carry a check and the word "matched"; each card has an icon (a clipboard, a closed shop sign, an envelope, a microphone, a ballot, a helping hand).
- Different from this batch (scout amber, revolution navy, rights plum, Pony Express saddle rust).

## Art
- People art goes to Gemini with `people: true`, illustrated, respectful and drawn from public photos for likeness: Julia Bluhm, Grace Bedell with Lincoln, Mari Copeny, Sojourner Truth, Dane Best, Takoma Park voters, Clara Barton, Katie Stagliano, petition signers (1830s), Montgomery riders walking, grape workers (12, cutout yes); the town kids at the board meeting (1).
- Public domain, checked at spec: Grace Bedell's letter (Detroit Public Library Burton Collection, 1860) shown beside her picture, with credit.
- Local FLUX (`scripts/localart.py`): the town map (1, 16:9), the park (1), the truck route street (1).
- Drawn in code: cards, slots, tiles, the letter and poster makers.
About 17 images.

## Voice
Two bank voices, each unique in this batch: `bright-teacher` as the narrator and card reader; `casual-peer` as a classmate, Theo (made for this game), who suggests plays ("What if we all wrote letters?"). `Curio.voice` with `scope: () => state.mode + ':' + state.part + ':' + state.card`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `flip`: "Tap a card to flip it."
- event, whole, each card's examples.
- how `chips`: "Pick the challenge and the opening."
- how `play`: "Drag a card to a slot. You can play up to three."
- how `predict`: "Pick who it reaches, how many people and how fast."
- how `see`: "Tap See what happens."
- event, whole, each town response.
- how `make`: "Pick Letter or Poster, then fill it in."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: flip cards with examples and chips, play slots with predictions, a response table keyed by problem and card, the letter and poster makers.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Flip | Skip reading | The chips must be picked before the card can be played. |
| Predict | Pick the same tiles for every card | Each misses some results; the miss lines say why (a boycott reaches nobody who decides). |
| Plan | Play any three | Every plan gets an honest result; mismatched plans show slow or no change and a "stronger plan" line. |
| Letter | Leave it blank | Print stays waiting until the problem, one reason and the ask are filled. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `flip`.
2. Card examples (whole), each waits. `chips`.
3. `play`, `predict`, `see`; responses (whole), each waits.
4. `make`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.Civ.14.3-5, D4.6.3-5, D4.7.3-5 and D4.3.3-5 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Antislavery petitions and the House gag rule, 1836 to 1844 | U.S. House of Representatives History, Art and Archives, "The Gag Rule" | National Archives, "Petitions against slavery" | yes |
| Julia Bluhm's 2012 petition to Seventeen and the magazine's pledge | NPR, "Teen's petition prompts Seventeen to change" (2012) | The New York Times, "Seventeen pledges not to alter images" (2012) | yes |
| Montgomery Bus Boycott, 381 days; Browder v. Gayle | National Park Service, "Montgomery Bus Boycott" | Stanford King Institute, "Montgomery Bus Boycott" | yes |
| Grape boycott 1965 to 1970 and the 1970 contracts | National Park Service, Cesar E. Chavez National Monument | U.S. Department of Labor, Hall of Honor, Cesar Chavez | yes |
| Grace Bedell's 1860 letter and Lincoln's beard; they met in Westfield in February 1861 | Library of Congress, "Lincoln and Grace Bedell" | Detroit Public Library, Burton Historical Collection | yes |
| Mari Copeny's 2016 letter; Obama visited Flint in May 2016 | Obama White House archives, "Letter from Mari" (2016) | CNN, "8-year-old Flint girl writes Obama" (2016) | yes |
| Sojourner Truth spoke in Akron, Ohio, in 1851 | National Park Service, "Sojourner Truth" | Library of Congress, "Sojourner Truth" | yes |
| Dane Best, 9, and the Severance, Colorado, snowball ban vote, December 2018 | CNN (2018) | Yahoo News / Greeley Tribune (2018) | yes |
| 19th Amendment, 1920 | National Archives, "19th Amendment" | Library of Congress, "Women's suffrage" | yes |
| Takoma Park, Maryland, first U.S. city to let 16- and 17-year-olds vote in city elections, 2013 | City of Takoma Park, elections page | The Washington Post (2013) | yes |
| Clara Barton founded the American Red Cross in 1881 | American Red Cross, "Founder Clara Barton" | National Park Service, Clara Barton National Historic Site | yes |
| Katie Stagliano's 40-pound cabbage fed about 275 people; Katie's Krops, 2008 | Katie's Krops, "Our story" | CBS News / People (2010s) | yes |
Backed twice: 13. Cut: 0.

Checks run (Python, scratchpad r9, 2026-11-09): every card has one example before 1925 and one after 1960 except Boycott (1955 and 1965, see Open questions); Montgomery December 1955 to December 1956 is 381 days; Saturday 9 to 1 is 4 hours a week, 208 hours a year; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map above three slots; at 680x425 slots stack.
2. Every card back shows a long-ago and a recent example with dates. (D2.Civ.14.3-5)
3. Each example takes its challenge and opening chips. (D4.6.3-5)
4. Predictions are required before results; results compare to predictions. (D4.7.3-5)
5. The letter or poster prints with the ask filled in. (D4.3.3-5)
6. The boycott response explains why it fails for a free library.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no flipping or fading; no network requests.

## Open questions
- The boycott card's recent example is the 1965 to 1970 grape boycott; a well-sourced, kid-safe boycott from the last 20 years was not found (default used: the grape boycott labeled "Later", checked again at build).

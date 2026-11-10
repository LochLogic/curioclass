# Two Parties

## One idea
The child sits at a long table in the 1790s with two tall stacks of letters and papers, one from Alexander Hamilton's Federalists and one from Thomas Jefferson's Democratic-Republicans; for each of six fights (paying the war debt in 1790, the national bank in 1791, the whiskey tax and the Whiskey Rebellion in 1794, Jay's Treaty with Britain in 1795, the Alien and Sedition Acts in 1798, and the tied election of 1800) the child reads one short real line from each side, sorts the reasons into "what this side feared" and "what this side wanted," and sees who each side's supporters were (merchants and bankers in port cities; farmers and planters inland); then a press table shows how each side built its own newspapers and clubs, and a cause chain shows why parties formed at all when Washington had warned against them; at the end the child writes how a party, a newspaper and a citizen each had a different power in the fight, so an eighth grader learns the causes of the first parties, the factors that shaped each side's view, and the separate roles of citizens, parties and the press.

## Not like
- constitutional-convention (8, spec): writing the rules in 1787. Here the fights after.
- colonial-newsroom (8, spec): two papers in 1765 and 1770. Here two parties in the 1790s.
- levers-of-power (8, spec): civic action today. Here the first parties.
- bill-to-law-board-game (4, spec): how a bill moves. Here why people split over bills.

## Who and how
- Grade 8, Social Studies (History and Civics), module "The New Republic". Standards: D2.His.14.6-8 (explain multiple causes and effects of events and developments in the past), D2.His.4.6-8 (analyze multiple factors that influenced the perspectives of people during different historical eras), D2.Civ.1.6-8 (distinguish the powers and responsibilities of citizens, political parties, interest groups, and the media in a variety of governmental and nongovernmental contexts).
- Format: sorter. Driver: one child alone, or the class splitting into two sides (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Six fights, the supporters map, the press table, the cause chain, the roles card. Extra: Class split (half the class reads for each side and argues each fight before sorting). tool.json `modes: ["The table", "Class split"]`, `minutes: "30-40"`, `grades_label: "Grade 8"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.4.6-8 | For each fight, sort each side's reasons into feared and wanted, then match each side to its supporters | the two stacks; the sorter; the supporters map | 2 |
| D2.His.14.6-8 | Build the cause chain from the debt plan to the 1800 election and the 12th Amendment | the chain with because lines | 3 |
| D2.Civ.1.6-8 | Sort actions on the press table by who did them (party, newspaper, citizen), then finish the roles card | the press table; the roles card | 4 |

## Screens and modes
Header (kit): title "Two Parties"; `The table`, `Class split`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A candlelit table in Philadelphia, the capital in the 1790s. Two stacks of papers, left marked with an eagle and "Federalists," right marked with a plow and "Democratic-Republicans." A small framed note from George Washington. The welcome is queued (`welcomeAfter: true`): "The Constitution never mentions parties. Washington hoped there would be none. Within five years there were two. Open the first fight." First hint: "Tap Fight 1."

**The fights (focus: the two stacks and the sorter).** At 1366x768 the stacks sit left and right with the sorter between; at 680x425 the stacks are tabs. Each fight shows the plan in plain words, one short real line from each side (under 15 words, credited), and reason tiles to sort into "feared" and "wanted" for each side.
1. 1790, paying the debt: Hamilton's plan has the national government pay the states' war debts in full. Federalists want strong credit; Jefferson's side fears speculators who bought old notes cheap will profit, and states that already paid will lose.
2. 1791, the national bank: Hamilton says the Constitution allows it as "necessary and proper"; Jefferson says the Constitution doesn't list it. The first argument over loose and strict reading.
3. 1794, the whiskey tax: farmers in western Pennsylvania who turned grain into whiskey refuse a federal tax; Washington leads about 13,000 militia to end the revolt. One side sees order kept; the other sees troops used on farmers.
4. 1795, Jay's Treaty: peace and trade with Britain. Merchants want the trade; others want to side with revolutionary France.
5. 1798, the Alien and Sedition Acts: it becomes a crime to publish "false, scandalous and malicious" writing against the government. Congressman Matthew Lyon of Vermont is jailed; the Kentucky and Virginia Resolutions (secretly by Jefferson and Madison) call the acts unconstitutional.
6. 1800, the tie: Jefferson and Aaron Burr tie in electoral votes; the House decides on the 36th ballot in February 1801. Power passes peacefully from one party to the other. The 12th Amendment (1804) changes how electors vote.

**The supporters map.** A map of the states in 1796 with port cities and farm country. The child matches each side to its main supporters (Federalists: merchants, bankers, New England; Democratic-Republicans: farmers and planters, the South and the West). A plain note: both leaders' lives were tied to slavery. Jefferson enslaved more than 600 people over his life; Hamilton's family records show he took part in buying and selling enslaved people for relatives, though he also joined the New York Manumission Society. Named plainly with sources; no images.

**The press table (D2.Civ.1.6-8).** Actions to sort by who did them: a party leader pays a friendly editor (Hamilton and the Gazette of the United States; Jefferson gives Philip Freneau a State Department job, and Freneau starts the National Gazette); a newspaper prints attacks and is charged under the Sedition Act (Benjamin Franklin Bache of the Aurora); citizens form clubs (the Democratic-Republican Societies) and petition and vote. Each sort plays a reason line about that group's power and responsibility.

**The cause chain (the aha, D2.His.14.6-8).** Cards: the debt plan; the bank; the whiskey tax; Jay's Treaty; the Sedition Act; the 1800 tie; the 12th Amendment. The child links them with because lines. Narrator: "Each fight made the two sides firmer, and the newspapers made sure everyone took a side."

**The roles card.** The child finishes: "A party could ___. A newspaper could ___. A citizen could ___. The Sedition Act tried to limit ___." Then Washington's Farewell Address warning (1796), with one question: "Was he right to worry?"

**The end.** The six sorters, the map, the press table, the chain and the roles card. `Print` prints them.

**Class split (extra).** Half the class reads each side's stack and argues each fight out loud before the sort.

## Content
- Six fights with plain summaries, one short real line per side, reason tiles; the supporters map; the plain note on slavery; the press table with nine actions; seven chain cards; the roles card; Washington's warning.
- All people, events, quotes, papers and figures are real and sourced; quotes are under 15 words.
- Both sides are shown with their reasons and their failings; neither is the hero.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Fights open in order; any opened fight can be reopened.
- A wrong sort plays a reason line and leaves the tile to move again.
- Keyboard: Tab to fights, tiles, sorter slots, the map, the press table and the chain; Enter to pick and place.
- With Motion off papers don't slide and candles don't flicker.

## Look
- Accent `--brand` #7a2e4a claret (header, the stacks, the chain); gold #f4c542 (the tile in hand, a linked card); paper #faf1f4; ink #260b15; muted #5f5157.
- Contrast (WCAG 2.1, computed): white on brand 9.06:1; brand on paper 8.18:1; ink on paper 16.61:1; muted on paper 6.77:1; ink on gold 11.32:1.
- Never color alone: each side carries its icon (eagle or plow) and its name; sort results carry words.
- Different from this batch (dusk violet, map slate, ballot green, prairie rust).

## Art
- Public domain portraits and papers (National Portrait Gallery, Library of Congress, ids checked at build): Hamilton (Trumbull, 1806), Jefferson (Peale, 1791), Washington (Stuart), John Adams, Matthew Lyon; mastheads of the Gazette of the United States, the National Gazette and the Aurora; a cartoon of the Lyon and Griswold brawl in Congress (1798). Each with credit.
- Local FLUX (`scripts/localart.py`): the candlelit table (1, 16:9).
- Drawn in code: the stacks, the sorter, the map, the press table, the chain.
About 10 images.

## Voice
Two bank voices, each unique in this batch: `lively-host` as the narrator and hints; `knowing-guide` as the reader of real lines from both sides, introduced each time as "from" the writer, never playing them. `Curio.voice` with `scope: () => state.mode + ':' + state.fight + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each fight's plan.
- event, whole, each side's line.
- how `sort`: "Sort each reason into feared or wanted, for each side."
- how `map`: "Match each side to its main supporters."
- event, whole, the plain note.
- how `press`: "Sort each action by who did it."
- how `chain`: "Link each fight to what it led to."
- how `roles`: "Finish the roles card."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: two stacks, the feared and wanted sorter, the supporters map, the press table, the chain, the roles card.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Sorter | Put every tile under "wanted" | Each tile checks against its side and column. |
| Map | Match both sides to everyone | Each side takes only its main supporters, checked. |
| Press | Sort every action as "party" | Each action checks; the reason line names who did it. |
| Chain | Link in any order | Each link checks dates and needs a because. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Fight plan (whole), waits; each side's line (whole).
2. `sort`, for each fight.
3. `map`; plain note (whole).
4. `press`; `chain`; `roles`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.14.6-8, D2.His.4.6-8 and D2.Civ.1.6-8 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Hamilton's debt plan (1790) and the bank (1791), with Jefferson's strict-reading objection | National Archives, Founders Online (Hamilton's Report on Public Credit; Jefferson's opinion on the bank) | Library of Congress, "Creating the United States" | yes |
| The Whiskey Rebellion (1794) and about 13,000 militia | Mount Vernon (George Washington's Mount Vernon), "Whiskey Rebellion" | Britannica, "Whiskey Rebellion" | yes |
| Jay's Treaty (1795) and the split over Britain and France | U.S. Department of State, Office of the Historian, "John Jay's Treaty" | Britannica, "Jay Treaty" | yes |
| The Alien and Sedition Acts (1798), Matthew Lyon jailed, Bache charged; the Kentucky and Virginia Resolutions | National Archives, "Alien and Sedition Acts" | Library of Congress, "Alien and Sedition Acts" primary documents | yes |
| The 1800 tie decided on the 36th ballot in February 1801; the 12th Amendment (1804) | U.S. House of Representatives History, "The Election of 1800" | National Archives, 12th Amendment | yes |
| Jefferson enslaved more than 600 people over his life | Monticello (Thomas Jefferson Foundation), "Slavery at Monticello" | National Park Service, "Thomas Jefferson and slavery" | yes |
| Hamilton took part in buying and selling enslaved people for relatives; he also joined the Manumission Society | Serfilippi, "As Odious and Immoral a Thing" (Schuyler Mansion State Historic Site, 2020) | National Park Service, Hamilton Grange, "Hamilton and slavery" | yes |
| Freneau's National Gazette and the State Department job; Fenno's Gazette of the United States | National Archives, Founders Online | Library of Congress, Chronicling America notes | yes |
Backed twice: 9. Cut: 0.

Sensitivity note: both founders' ties to slavery are named in one plain card with sources and no images; both parties are shown with their reasons and their failings. A fresh-agent read of that card and the real lines is needed before build.

Checks run (Python, scratchpad r16, 2026-11-09): fights in date order (1790, 1791, 1794, 1795, 1798, 1800); the 12th Amendment follows the tie by 3 to 4 years; each side has at least one feared and one wanted tile per fight; nine press actions, three per group; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 stacks and sorter; at 680x425 tabs.
2. Six fights sort each side's reasons, and the map matches supporters. (D2.His.4.6-8)
3. The chain links the fights from 1790 to 1804. (D2.His.14.6-8)
4. The press table sorts actions by party, newspaper and citizen, and the roles card prints. (D2.Civ.1.6-8)
5. The plain note on slavery appears once, with sources.
6. Class split runs the arguments before each sort.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no sliding or flicker; no network requests.

## Open questions
- Sensitivity flag: Jefferson's and Hamilton's ties to slavery (default used: one plain card with sources, no images, both parties shown with failings, fresh-agent read before build).

# Ideas That Spread

## One idea
An Atlantic map from 1690 to 1830 holds five idea tokens in Europe (natural rights, consent of the governed, separation of powers, equality, liberty), with presses, salons and ports marked; the student carries each idea along real routes (a book, a newspaper, a returning soldier, a ship's crew, and enslaved people's own networks in Saint-Domingue) to four revolutions (the American, the French, the Haitian and the Spanish American), and at each one a short source shows how local people used the idea while a context card (slavery, debt, class, the Church, Napoleon's invasion of Spain) explains why their reading differed; a cause web for each revolution lets the student weight and link ideas, debt and taxes, war, elite rivalry and uprisings, so ideas show up as one cause among several, with effects rippling into the next revolution; at the end four founding documents sit side by side (the U.S. Constitution of 1787, the French Declaration of 1789, the Haitian Constitution of 1805, and Gran Colombia's Constitution of 1821), and the student scores each on who could vote, who was free and how power was checked, and finds that Haiti is the one that ended slavery outright, so a ninth grader learns how context shaped and still shapes perspectives, how to evaluate political systems against democratic principles, and the complex causes and effects of the revolutions.

## Not like
- expansion-map (8, spec): U.S. territory on a map. Here ideas crossing an ocean.
- constitutional-convention (8, spec): one convention in roleplay. Here four revolutions compared.
- alliance-web (9, spec): the cause web of one war. Here ideas and causes across four revolutions.
- printing-press (7, spec): a press spreading ideas in one city. Here ideas crossing an ocean.

## Who and how
- Grade 9, Social Studies (World History and Civics), module "Revolutions and the Enlightenment". Standards: D2.His.5.9-12 (analyze how historical contexts shaped and continue to shape people's perspectives), D2.Civ.8.9-12 (evaluate social and political systems in different contexts, times, and places, that promote civic virtues and enact democratic principles), D2.His.14.9-12 (analyze multiple and complex causes and effects of events in the past).
- Format: map. Driver: one student alone (tool.json `driver: "student"`). `Read` reads every card. Controls 44 px or more.
- Five ideas, four revolutions, routes, context cards, four cause webs, the founding-documents scorecard. Extra: 1830 report card (the class debates which revolution best kept its promises, with the scorecards printed). tool.json `modes: ["Atlantic map", "1830 report card"]`, `minutes: "35-45"`, `grades_label: "Grade 9"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.5.9-12 | At each revolution, read the source and context card, then explain how this group read the idea and why | the source; the context card; the reading card with the student's line | 2 |
| D2.His.14.9-12 | Weight and link causes on each revolution's web, and trace effects into the next revolution | four cause webs; ripple arrows between them | 3 |
| D2.Civ.8.9-12 | Score four founding documents on voting, freedom and checks on power, and defend one score | the scorecard side by side | 4 |

## Screens and modes
Header (kit): title "Ideas That Spread"; `Atlantic map`, `1830 report card`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** An Atlantic map in 1750: Europe, West Africa, the Caribbean, the Americas. Five idea tokens sit in London, Paris and Edinburgh, each with its source (Locke's Two Treatises, 1689; Montesquieu's Spirit of the Laws, 1748; Rousseau's Social Contract, 1762). Ports, presses and salons glow. The welcome is queued (`welcomeAfter: true`): "These ideas began in books. Where will 'all men are created equal' go, and who will it include? Pick an idea and send it." First hint: "Tap an idea token."

**Routes (focus: the map).** At 1366x768 the map fills the screen with the card panel right; at 680x425 the panel is a sheet. The student drags an idea along a real route: Paine's Common Sense (1776) printed in Philadelphia; Lafayette and French soldiers returning from America (1780s); newspapers and pamphlets in ports; sailors and free people of color moving between France and Saint-Domingue; enslaved people's own networks, meetings and the Bois Caiman gathering (August 1791); Spanish American students in Europe; Haiti's President Petion aiding Bolivar in 1816 on condition that he free enslaved people.

**The four revolutions (D2.His.5.9-12).** At each, a short source (under 15 words quoted, credited) and a context card:
1. America (1776 to 1787): the Declaration's "all men are created equal" alongside slavery kept in law; context: taxes after the Seven Years' War, colonial assemblies, slavery.
2. France (1789 to 1799): the Declaration of the Rights of Man; Olympe de Gouges's Declaration of the Rights of Woman (1791), and her execution in 1793; slavery abolished in 1794, restored by Napoleon in 1802; context: royal debt, a hungry Paris, the Church, class privilege.
3. Haiti (1791 to 1805): the uprising of the enslaved in Saint-Domingue; Toussaint Louverture; independence on January 1, 1804 under Dessalines; the 1805 Constitution ends slavery forever; context: the largest slave colony in the Caribbean, French revolution, British and Spanish invasions. The violence on all sides, including the 1804 killings of French residents, is told plainly without images.
4. Spanish America (1810 to 1825): juntas after Napoleon invades Spain (1808); Bolivar's Jamaica Letter (1815); Gran Colombia's 1821 Constitution with a free-womb law that freed children born to enslaved mothers, not their parents; context: creole elites, the Church, Indigenous and enslaved majorities, Napoleon.
- After each, the student writes one line: "These people read [idea] as ___ because ___." A note shows how the same context still shapes views today (for example how Haiti's revolution is remembered in Haiti and in France).

**Cause webs (D2.His.14.9-12).** For each revolution, five cause nodes (ideas, debt and taxes, war, elite rivalry, uprisings from below). The student weights each (small, medium, large) and links them with because lines. Ripple arrows carry effects into the next revolution (French debt from aiding America; Napoleon's invasion of Spain; Haiti's example and aid).

**The scorecard (the aha, D2.Civ.8.9-12).** Four documents side by side: the U.S. Constitution (1787), the French Declaration (1789), the Haitian Constitution (1805), Gran Colombia's Constitution (1821). The student scores each on three rows from evidence clauses: who could vote; who was free; how power was checked. Haiti is the only one to end slavery outright; it also made Dessalines emperor for life, which scores low on checks. The student defends one score in a line. Narrator: "Each revolution wrote liberty into its founding words. None of them gave it to everyone at once."

**The end.** The routes, reading cards, cause webs and scorecard. `Print` prints them.

**1830 report card (extra).** The class debates which revolution best kept its promises by 1830, with the scorecards printed.

## Content
- Five idea tokens with their books, about twelve routes, four revolutions with sources and context cards, four cause webs, ripple arrows, four documents with evidence clauses, the scorecard.
- All people, documents, dates and quotes are real and sourced; quotes are under 15 words.
- Violence in each revolution is told plainly and evenly, without images.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Each revolution opens once at least one idea reaches it; all four must be visited before the scorecard opens.
- Weights and links can change until the scorecard opens.
- Keyboard: Tab to tokens, routes, revolutions, cause nodes and the scorecard; arrows move a token along a route; Enter to send, link and score.
- With Motion off tokens jump to their destinations.

## Look
- Accent `--brand` #2f3f7a Atlantic indigo (header, routes, the scorecard); gold #f4c542 (the token in motion, a linked cause); paper #f2f3fa; ink #0d1230; muted #545870.
- Contrast (WCAG 2.1, computed): white on brand 9.94:1; brand on paper 8.98:1; ink on paper 16.55:1; muted on paper 6.31:1; ink on gold 11.26:1.
- Never color alone: each idea token carries its name and icon; scorecard cells carry words and marks.
- Different from this batch (ochre, mill soot, cartographer blue, field olive).

## Art
- Public domain portraits and documents (Library of Congress, Bibliotheque nationale de France, National Archives, ids checked at build): Locke, Montesquieu, Rousseau; Toussaint Louverture (1802 engraving); Olympe de Gouges (1780s portrait); Simon Bolivar (about 1825 portrait); title pages of Common Sense and the Declaration of the Rights of Man; the Haitian Act of Independence (1804, UK National Archives copy). Each with credit.
- Local FLUX (`scripts/localart.py`): a period-style Atlantic map base (1, 16:9); a Paris salon, no people (1, 16:9); a Cap-Francais harbor (1, 16:9).
- Real faces only for real people.
About 14 images.

## Voice
Two bank voices, each unique in this batch: `smooth-narrator` as the narrator; `knowing-guide` as the hints and the reader of sources, introduced each time as "from" the writer. `Curio.voice` with `scope: () => state.mode + ':' + state.place + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `send`: "Drag an idea along a route to a revolution."
- event, whole, each source.
- event, whole, each context card.
- how `reading`: "Write how these people read the idea, and why."
- how `web`: "Weight each cause, then link them with because lines."
- how `score`: "Score each document on voting, freedom and checks."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the Atlantic map with routes and tokens, revolution cards, cause webs with ripples, the scorecard.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Reading | Write the same line everywhere | Each line must name a context item from that revolution's card. |
| Webs | Weight ideas "large" everywhere and link nothing | Each web needs three links with becauses before the scorecard opens. |
| Scorecard | Give every document top marks | Each score cites a clause; "everyone free" for 1787 plays the three-fifths clause. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). `send`.
2. Source (whole), waits; context card (whole); `reading`.
3. `web`, for each revolution.
4. `score`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.5.9-12, D2.Civ.8.9-12 and D2.His.14.9-12 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Locke (1689), Montesquieu (1748), Rousseau (1762) | Stanford Encyclopedia of Philosophy entries | Britannica entries | yes |
| The Declaration of the Rights of Man (1789); de Gouges (1791) executed 1793 | Avalon Project (Yale Law School) and Liberty, Equality, Fraternity (George Mason University) | Britannica, "Olympe de Gouges" | yes |
| France abolished slavery in 1794; Napoleon restored it in 1802 | Dubois, "Avengers of the New World" (Harvard, 2004) | Britannica, "Haitian Revolution" | yes |
| The 1791 uprising, Toussaint Louverture, independence January 1, 1804, the 1805 Constitution ending slavery | Dubois (2004) | Duke University, Haiti Digital Library (1805 Constitution text) | yes |
| The 1804 killings of French residents | Dubois (2004) | Geggus, "Haitian Revolutionary Studies" (Indiana, 2002) | yes |
| Napoleon's invasion of Spain (1808) set off juntas in Spanish America; Bolivar's Jamaica Letter (1815) | Lynch, "Simon Bolivar: A Life" (Yale, 2006) | Britannica, "Latin American independence" | yes |
| Petion's aid to Bolivar in 1816 on condition of freeing the enslaved | Lynch (2006) | Dubois, "Haiti: The Aftershocks of History" (Metropolitan, 2012) | yes |
| Gran Colombia's 1821 Constitution and free-womb law | Lynch (2006) | Biblioteca Virtual Miguel de Cervantes, Constitution of Cucuta text | yes |
| The U.S. Constitution's three-fifths clause and voting left to states | National Archives, Constitution transcript | Keyssar, "The Right to Vote" (2009) | yes |
Backed twice: 10. Cut: 0.

Sensitivity note: slavery and the violence of the Haitian Revolution, including the 1804 killings, are told plainly and evenly with sources and no images; real faces only; Haiti's role is shown as central, not as a side story. A fresh-agent read of the context cards is needed before build.

Checks run (Python, scratchpad r17, 2026-11-09): revolutions in order of start (1776, 1789, 1791, 1810); documents in date order (1787, 1789, 1805, 1821); slavery in French law was abolished for 8 years (1794 to 1802); exactly one document of four ends slavery outright; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 map and panel; at 680x425 sheet.
2. Each revolution's reading card names a context item. (D2.His.5.9-12)
3. Four cause webs are weighted and linked, with ripples between them. (D2.His.14.9-12)
4. The scorecard scores four documents from clauses and defends one score. (D2.Civ.8.9-12)
5. Haiti is the only document that scores "ended slavery outright".
6. 1830 report card prints the scorecards for debate.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: tokens jump; no network requests.

## Open questions
- Sensitivity flag: slavery and the Haitian Revolution's violence, including the 1804 killings (default used: told plainly and evenly with sources, no images, real faces only, Haiti central, fresh-agent read before build).

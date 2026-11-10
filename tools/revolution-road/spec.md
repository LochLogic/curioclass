# Revolution Road

## One idea
The child walks a road from 1763 to the Treaty of Paris in 1783 that runs in four parallel lanes (Patriots, Loyalists, Native nations, and enslaved and free Black Americans), and at each of nine milestones the same event shows up differently in each lane; they link causes to effects across milestones, stop at four real people (a Boston printer, a Loyalist who wrote as "a farmer", an Oneida couple, a man who escaped from Mount Vernon to the British) to explain each one's choice from their situation, and reach the treaty to see what each lane gained or lost, so a fifth grader learns that people living at the same time chose different sides for reasons rooted in their own lives, and that independence meant different things to different people.

## Not like
- history-article-review (5, spec): reviewing articles about the Revolution for evidence and order. Here walking the events in four lanes and explaining choices.
- rights-match (5, spec): the Bill of Rights after the war. Here the war years and who stood where.
- colonial-trade-routes (5, spec): the colonies' trade before the Revolution. Here 1763 to 1783.
- ship-s-log (5, spec): 1620. Here a century and a half later.

## Who and how
- Grade 5, Social Studies (History), module "The American Revolution". Standards: D2.His.1.3-5 (create and use a chronological sequence of related events to compare developments that happened at the same time), D2.His.4.3-5 (explain why individuals and groups during the same historical period differed in their perspectives), D2.His.5.3-5 (explain connections among historical contexts and people's perspectives at the time), D2.His.14.3-5 (explain probable causes and effects of events and developments).
- Format: timeline. Driver: one child alone, or the teacher on the projector (tool.json `driver: "either"`). `Read` reads every card. Controls 44 px or more.
- Nine milestones in four lanes, four "Why that side?" stops, cause links, and the treaty. Extra: Lanes for groups (the teacher assigns each group a lane and each reports what its lane gained or lost). tool.json `modes: ["Walk the road", "Lanes for groups"]`, `minutes: "30-40"`, `grades_label: "Grade 5"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| D2.His.1.3-5 | Walk the milestones in order and open each lane at each one | four lanes side by side at the same date | 2 |
| D2.His.4.3-5 | Compare the four lane cards at one milestone and pick which lane each quote belongs to | the lane cards; the quote match | 3 |
| D2.His.5.3-5 | At each "Why that side?" stop, pick the two situation facts that best explain the person's choice | the person's card with six facts, two of which matter most | 4 |
| D2.His.14.3-5 | Draw links from a cause milestone to an effect milestone and pick the link word | cause arrows across the road | 5 |

## Screens and modes
Header (kit): title "Revolution Road"; `Walk the road`, `Lanes for groups`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more.

**On load and first tap.** A long road drawn across the screen with four lanes, each with a small banner (Patriots, Loyalists, Native nations, Black Americans), and the first milestone stone: 1763. The welcome is queued (`welcomeAfter: true`): "This road runs from 1763 to 1783. Four groups of people walk it side by side. Tap the milestone to see what each lane hears about it." First hint: "Tap the 1763 milestone."

**The road (focus: the current milestone and its four lane cards).** At 1366x768 the road scrolls sideways with the four lane cards stacked above the current stone; at 680x425 one lane card shows at a time with lane tabs and the road becomes a strip of stones at the bottom.

The nine milestones, with one short card per lane (examples):
1. 1763, the French and Indian War ends; the Proclamation Line. Patriots: colonists who wanted western land are angry at the line. Loyalists: many accept it as the king's law. Native nations: the line is a promise that lands west of the mountains stay theirs; it follows a year of war led by Pontiac against British forts. Black Americans: most are enslaved; the war's end changes little for them.
2. 1765, the Stamp Act. Patriots: "No taxation without representation"; the Stamp Act Congress meets. Loyalists: some stamp collectors are threatened and quit. Native nations: settlers keep crossing the line. Black Americans: enslaved people hear the colonists' talk of liberty.
3. 1770, the Boston Massacre. Patriots: Paul Revere's print spreads the story. Loyalists: John Adams, a Patriot, defends the soldiers in court, and most are found not guilty. Native nations: the 1768 Treaty of Fort Stanwix moves the line west. Black Americans: Crispus Attucks, a man of African and Native descent, is among the five killed.
4. 1775, Lexington and Concord. Patriots: militia fight British soldiers. Loyalists: neighbors who side with the king are watched, some driven from their homes. Native nations: both sides ask nations to stay out or join them. Black Americans: Black militiamen, free and enslaved, fight at Lexington, Concord and Bunker Hill (Peter Salem).
5. November 1775, Lord Dunmore's Proclamation. Patriots: Virginia planters are alarmed. Loyalists: the royal governor offers freedom to enslaved men who join the British. Native nations: no change yet. Black Americans: hundreds escape to Dunmore's lines.
6. July 1776, the Declaration of Independence. Patriots: "all men are created equal." Loyalists: their choice is now treason in Patriot eyes. Native nations: the Declaration calls Native peoples "savages" in its list of complaints (shown with a teacher note). Black Americans: free and enslaved people point out that equality was not meant for them yet.
7. October 1777, Saratoga. Patriots: a big win that brings France in. Loyalists: British hopes in the north fade. Native nations: at Oriskany that August, Oneida fought beside Patriots against Mohawk and Seneca fighting beside the British, nation against nation within the Haudenosaunee Confederacy. Black Americans: Rhode Island forms the 1st Rhode Island Regiment in 1778, promising freedom to enslaved men who join.
8. October 1781, Yorktown. Patriots: the British army surrenders. Loyalists: many plan to leave. Native nations: in 1779 the Sullivan Expedition burned about 40 Haudenosaunee towns and their crops. Black Americans: Black soldiers serve on both sides at Yorktown; thousands who escaped to the British are in the British camps.
9. 1783, the Treaty of Paris (the end card, see below).

- Quote match (D2.His.4.3-5): at milestones 2, 5 and 6 the child gets one short real quote and drags it to the lane it came from (e.g. Dunmore's offer to the Loyalists' lane, read as the governor's words; Phillis Wheatley's 1774 letter about freedom to the Black Americans' lane).
- Cause links (D2.His.14.3-5): at milestones 3, 5, 7 and 8 the child draws an arrow back to an earlier milestone that helped cause it and picks a link word ("led to", "made angry", "gave hope to", "brought in"). Example: Saratoga "brought in" France, which led toward Yorktown.

**Why that side? (four stops).** Each person's card shows a picture, a short life sketch and six facts; the child picks the two that best explain the choice, then hears the person's reason read by the narrator.
1. Benjamin Edes, Boston printer: printed the Boston Gazette; a member of the Sons of Liberty; the Stamp Act taxed every newspaper he printed. Patriot.
2. Samuel Seabury, a minister in Westchester, New York, who wrote pamphlets as "A. W. Farmer" in 1774: his church was the Church of England; he feared a war would ruin farmers and trade; he believed the king's law kept order. Loyalist.
3. Han Yerry (Tewahangarahken) and Tyonajanegen (Two Kettles Together), an Oneida couple: their nation's Protestant missionary and neighbors leaned to the Patriots; the Oneida hoped to keep their lands by siding with the colonists; both fought at Oriskany in 1777. Patriot side.
4. Harry Washington: enslaved at Mount Vernon by George Washington; escaped in 1776 to join Dunmore; served with the Black Pioneers; left New York with the British in 1783 for Nova Scotia, and later Sierra Leone. British side.

**The treaty (the end card).** 1783: the four lanes meet at the last stone. Patriots: independence and land to the Mississippi. Loyalists: tens of thousands leave for Canada, Britain and the Caribbean. Native nations: the treaty hands their lands to the United States without them at the table, including the lands of nations who fought for the Patriots. Black Americans: about 3,000 Black Loyalists leave New York with the British as free people (their names recorded in the "Book of Negroes"); slavery remains in every state, though Vermont (1777) and Massachusetts (court rulings, 1781 to 1783) begin to end it. The child picks a word for each lane from tiles ("gained", "lost", "both"). Narrator: "Same war, same treaty, four different endings." `Print` prints the road with the child's links and lane words.

**Lanes for groups (extra).** The teacher view gives each group a lane; each walks only its lane and reports at the treaty stone.

## Content
- Nine milestones, four lane cards each (about 36 cards, two or three sentences each), three quotes to match, four cause links, four person cards with six facts each, the treaty card, teacher notes on the Declaration's words about Native peoples and on slavery.
- All people and events are real. Quotes are short and from public-domain documents; the narrator reads Native and Black historical figures' situations, not invented speech.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Milestones open in order; any opened milestone can be revisited.
- Cause arrows draw by tapping the effect stone, then the cause stone, then a link word.
- Keyboard: Tab to stones and cards; Enter to open; arrows choose a lane or link word.
- With Motion off the road jumps to the next stone instead of scrolling.

## Look
- Accent `--brand` #233d7b road navy (header, milestone stones, arrows); gold #f4c542 (the current stone, a picked fact); paper #f1f3f9; ink #0b142b; muted #4f5566.
- Contrast (WCAG 2.1, computed): white on brand 10.37:1; brand on paper 9.35:1; ink on paper 16.47:1; muted on paper 6.70:1; ink on gold 11.24:1.
- Never color alone: each lane has its own banner icon and label (a liberty cap, a crown, a longhouse, a broken chain), not only a tint.
- Different from this batch (scout amber, rights plum, change teal, Pony Express saddle rust).

## Art
- Public domain, checked at spec: Paul Revere's "The Bloody Massacre" engraving (1770, Library of Congress); the Proclamation of 1763 map (Library of Congress); John Trumbull's "Surrender of Lord Cornwallis" (1820, Architect of the Capitol); the Stamp Act's "the fatal Stamp" newspaper mock-up (Pennsylvania Journal, 1765). Each used as a milestone picture with its credit.
- People art goes to Gemini with `people: true`: Benjamin Edes, Samuel Seabury, Han Yerry and Tyonajanegen (one picture), Harry Washington (1 each, cutout yes); Oneida dress drawn from the Oneida Indian Nation's own published images.
- Local FLUX (`scripts/localart.py`): the road landscape (1, 16:9).
- Drawn in code: the lanes, stones, banners, arrows, cards.
About 9 images.

## Voice
Two bank voices, each unique in this batch: `calm-professor` as the narrator and card reader; `wise-mentor` as the voice reading each person's reason in third person ("Edes printed..."). `Curio.voice` with `scope: () => state.mode + ':' + state.stone + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- event, whole, each lane card.
- how `next`: "Tap the next milestone."
- how `quote`: "Drag the quote to the lane it came from."
- how `link`: "Tap this stone, then the earlier stone that helped cause it."
- how `why`: "Pick the two facts that best explain this choice."
- event, whole, each person's reason.
- how `treaty`: "Pick gained, lost or both for each lane."
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the four-lane road, stones in order, quote match, cause arrows, the person cards with fact picks and the treaty tiles.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Quote match | Drop each quote in lane 1 | Wrong lanes play "Who would say this? Read the lane cards again." and the quote returns. |
| Cause links | Link to the stone just before | Each link is checked against the allowed causes; a wrong one plays "Did that cause this? Look at the dates and the cards." |
| Why that side? | Pick any two facts | Each person has two key facts; others play "That's true, but did it shape the choice?" |
| Treaty | Mark "gained" for all | The Native nations' lane with "gained" plays "Look at who was at the table." |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued). Lane cards (whole), each waits.
2. `next`; `quote`, `link` at their stones.
3. `why`; reasons (whole).
4. `treaty`; `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| C3 wording for D2.His.1.3-5, D2.His.4.3-5, D2.His.5.3-5 and D2.His.14.3-5 | C3 Framework (NCSS, 2013, rev. 2017) | data/standards/c3-indicators.txt | yes |
| Proclamation of 1763 and Pontiac's War | Office of the Historian (U.S. State Department), "Proclamation Line of 1763" | Library of Congress, "The Proclamation of 1763" | yes |
| Crispus Attucks, of African and Native descent, killed in the Boston Massacre, 1770; Adams defended the soldiers | Massachusetts Historical Society, "The Boston Massacre" | Revolutionary Spaces (Old State House), "Boston Massacre" | yes |
| Dunmore's Proclamation, November 7, 1775 | Library of Congress, Dunmore broadside | Museum of the American Revolution, "Dunmore's Proclamation" | yes |
| The Declaration's words about Native peoples | National Archives, Declaration transcript | Smithsonian National Museum of the American Indian, teaching notes | yes |
| Oneida fought with the Patriots at Oriskany, 1777; Han Yerry and Tyonajanegen | Oneida Indian Nation, "Revolutionary War" and "Oriskany" | National Park Service, Fort Stanwix National Monument | yes |
| 1st Rhode Island Regiment, 1778 | National Park Service, "Black soldiers in the Revolution" | Museum of the American Revolution, "Black founders" | yes |
| Sullivan Expedition burned about 40 Haudenosaunee towns, 1779 | National Park Service, Fort Stanwix and Sullivan expedition pages | Encyclopaedia Britannica, "Sullivan Expedition" | yes |
| Benjamin Edes printed the Boston Gazette and was in the Sons of Liberty | Massachusetts Historical Society | American Antiquarian Society | yes |
| Samuel Seabury wrote as "A. W. Farmer" (1774) | Encyclopaedia Britannica, "Samuel Seabury" | Columbia University Libraries, Seabury pamphlets | yes |
| Harry Washington escaped Mount Vernon, joined the British, went to Nova Scotia and Sierra Leone | George Washington's Mount Vernon, "Harry Washington" | Nova Scotia Archives, "Book of Negroes" | yes |
| About 3,000 Black Loyalists left New York in 1783; Vermont 1777 and Massachusetts court rulings | Nova Scotia Archives, "Black Loyalists" | Massachusetts Historical Society, "Quock Walker case" | yes |
Backed twice: 12. Cut: 0.

Sensitivity note: the road covers slavery, the Declaration's words about Native peoples, the Sullivan Expedition and the treaty's loss of Native land. Each lane card is plain and factual; Native and Black people are shown making choices for their own reasons, not as background; the Declaration line comes with a teacher note; a fresh-agent read of every lane card and person card is needed before build.

Checks run (Python, scratchpad r9, 2026-11-09): the nine milestones sort in date order (1763, 1765, 1770, April 1775, November 1775, July 1776, October 1777, October 1781, 1783); each allowed cause link points to an earlier stone; Oriskany (August 1777) comes before Saratoga's end (October 1777); contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 four lane cards above the road; at 680x425 one lane with tabs.
2. Each milestone shows four lane cards for the same date. (D2.His.1.3-5)
3. Quote match places each quote in its lane. (D2.His.4.3-5)
4. Each "Why that side?" stop takes its two key facts. (D2.His.5.3-5)
5. Cause arrows accept only earlier, allowed causes. (D2.His.14.3-5)
6. The treaty card shows each lane's outcome and takes the child's tiles.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: no scrolling road; no network requests.

## Open questions
- Sensitivity flag: four lanes include slavery and Native nations, and the Declaration's words about Native peoples (default used: plain factual lane cards from nation and museum sources, teacher note on the Declaration line, fresh-agent read before build).

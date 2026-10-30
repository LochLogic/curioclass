# Founding Words Explorer

## One idea
Some of the plainest words in the founding documents have drifted since 1787: read a sentence the way it sounds today, then flip each drifted word back to its 1828 dictionary sense and watch the plain-English reading rebuild itself, so "insure domestic Tranquility" turns from "buy peace at home" into "make sure there are no uprisings inside the country", and you can say which words changed the meaning and which only sound old.

## Not like
- premise-inspector (ela 11, family sibling): lays later speeches over the Declaration's premises. Here there are no later speakers; the unit is the single word, and the comparison is 1787 against today.
- reconstruction-amendments (social studies 8, family sibling): what three amendments promised and what undid them. Here the text is the 1787 Constitution, the First Amendment and Washington's Farewell, and the subject is word meaning.
- rights-match (social studies 5, family sibling): sorts scenarios into amendments. Here nothing is sorted; sentences are re-read.
- word-family-tree (ela 12): roots and descent of words. Here a word's history is only two points, then and now, inside one sentence that depends on it.
- rhetoric-spotter (ela 9): sorts speech lines by appeal and device. Here no line is judged for effect; it is decoded.
- key-term-tracker (social studies, not built): owns "faction" and Federalist No. 10. This tool does not use either.

## Who and how
- Grade 9 ELA, module Seminal US Documents (Reading Informational Text): "Foundational documents and their themes".
- Driver: students on laptops, alone or in pairs; a teacher can project Read and do the Preamble together first. 25 to 40 minutes.
- Standards: RI.9-10.4 (determine the meaning of words and phrases as they are used in a text; cumulative impact of word choices): Read and Drift. RI.9-10.9 (analyze seminal U.S. documents of historical and literary significance, including how they address related themes and concepts): Trail and the Left out layer.
- tool.json: driver "students", minutes "25-40", modes ["Read", "Drift", "Trail"], grades_label "Grade 9". Kit starter plus `kit:founding-docs`; light theme with its own `:root` (Look).

## Screens and modes
Header: title "Founding Words Explorer", small line "Same words, different meanings."; document tabs **Preamble**, **First Amendment**, **Commerce Clause**, **Farewell Address**; mode buttons **Read** (opens first), **Drift**, **Trail**; Motion, Sound, Read. Layout: the section ribbon (engine Reader) across the top; the document on a parchment card in the center; a word card panel on the right with `#hint`. At 760 wide and below the panel becomes a bottom sheet; at 375 the document tabs become a select box.

### Read (opens first)
- The document text, exact. Drift words (Content) carry a dotted underline and a small clock glyph. Tapping one opens its word card (engine Lens): **1828** (Webster's sense, quoted, with its sense number), **Today** (a plain gloss), **In this sentence** (one line), and a drift badge: **Big shift**, **Some shift** or **Hardly moved**.
- Layer toggles (engine Layers), each with glyph and word: **Plain English** (one plain line under each clause), **Context** (a pin glyph; short cards from Content), **Left out** (an open bracket glyph; marks the words and clauses that excluded people, with cards L1 to L6).
- **Show all drift words** lists the document's drift words as chips under the text; tapping a chip jumps to the word.

### Drift
- One sentence at a time (the excerpts in Content, picker arrows **Previous** and **Next**). Under it, the **Today reading**: a plain paraphrase built as if every drift word had its most common modern meaning. Each drift word in the paraphrase is a two-position switch labeled **Now** and **1787**.
- Flip a switch and that phrase in the paraphrase swaps (Content gives both fills), with a brief highlight (no motion with Motion off). A **Drift meter** under the paraphrase counts "Words flipped: 2 of 3" and, beside it, "Meaning changed: yes / no" for the sentence as a whole, decided by the student with two buttons once at least one switch is flipped.
- **Check the clue** (one per sentence) shows a second piece of evidence from the same documents, for example Article IV's "against domestic Violence" for "domestic Tranquility", and asks "Does the clue fit the Now reading or the 1787 reading?" with buttons **Now**, **1787**, **Both**. The answer is followed by one line from Content; no score.
- **My best reading**: a private text box per sentence for the student's own paraphrase (localStorage, **Clear my readings** button with confirm).

### Trail
- The Preamble's six purposes as six labeled tiles across the top: **a more perfect Union**, **establish Justice**, **insure domestic Tranquility**, **provide for the common defence**, **promote the general Welfare**, **secure the Blessings of Liberty**.
- Tap a tile: a trail line draws down into a column of clause cards (Content, Trails) showing where the Constitution puts that purpose to work, each with its article and section and the exact words.
- The **Left out** toggle works here too: when on, the clause column also shows the clauses that limited who "the People" and "ourselves and our Posterity" covered (L1 to L5), each with a plain card.
- Panel prompt per tile (private note box): "Which clause does the most to carry out this purpose?"

## Content
Document text from the National Archives transcripts (Constitution, Bill of Rights) and the Avalon Project (Farewell Address), spelling kept ("defence", "Tranquility" as printed in the Constitution). Webster quotations from Noah Webster, An American Dictionary of the English Language (1828).

**Excerpts** (Drift order)
- E1 Preamble: "We the People of the United States, in Order to form a more perfect Union, establish Justice, insure domestic Tranquility, provide for the common defence, promote the general Welfare, and secure the Blessings of Liberty to ourselves and our Posterity, do ordain and establish this Constitution for the United States of America."
- E2 First Amendment: "Congress shall make no law respecting an establishment of religion, or prohibiting the free exercise thereof; or abridging the freedom of speech, or of the press; or the right of the people peaceably to assemble, and to petition the Government for a redress of grievances."
- E3 Article I, Section 8: "To regulate Commerce with foreign Nations, and among the several States, and with the Indian Tribes;"
- E4 Farewell: "accustoming yourselves to think and speak of it as of the palladium of your political safety and prosperity; watching for its preservation with jealous anxiety".
- E5 Farewell: "the jealousy of a free people ought to be constantly awake".
- E6 Farewell: "Why, by interweaving our destiny with that of any part of Europe, entangle our peace and prosperity in the toils of European ambition, rivalship, interest, humor or caprice?"
- E7 Farewell: "warn you in the most solemn manner against the baneful effects of the spirit of party generally."

**Drift words** (word, excerpt; 1828 quoted with sense; Today gloss; badge; Now fill / 1787 fill for the Drift paraphrase)
- insure (E1). 1828: "To make sure or secure". Today: to buy insurance against loss. Big. Now "buy protection for" / 1787 "make sure of".
- domestic (E1). 1828 sense 4: "Pertaining to a nation considered as a family, or to ones own country; intestine; not foreign; as domestic troubles; domestic dissensions." Today: about home and family life. Big. Now "peace at home in our families" / 1787 "calm inside the country, with no uprisings".
- Tranquility (E1). 1828: "Quietness; a calm state; freedom from disturbance or agitation." Today: calm. Hardly moved (paired with domestic in one switch).
- Welfare (E1). 1828 sense 2: "the enjoyment of peace and prosperity, or the ordinary blessings of society and civil government; applied to states." Today: often government aid to people in need. Big. Now "government aid" / 1787 "the country's peace and prosperity".
- Posterity (E1). 1828 sense 2: "succeeding generations; opposed to ancestors." Today: future generations. Hardly moved. Now and 1787 fill the same: "our descendants" (the switch shows "Same either way").
- ordain (E1). 1828 sense 3: "To set; to establish; to institute; to constitute." Today: to make someone a priest or minister. Big. Now "make holy" / 1787 "set up".
- establishment (E2). 1828 sense 6: "The episcopal form of religion, so called in England." Today: a business, or "the Establishment", people in power. Big. Now "a business or group of powerful people connected to" / 1787 "an official state church, like the Church of England, for".
- abridging (E2). 1828 sense 3: "To deprive; to cut off from"; sense 2: "to abridge power of rights". Today: shortening a book. Big. Now "shortening" / 1787 "cutting back".
- press (E2). 1828 sense 3: "The art or business of printing and publishing. A free press is a great blessing to a free people". Today: news reporters and outlets. Some. Now "news reporters" / 1787 "anyone printing and publishing".
- redress (E2). 1828 noun sense 2: "Relief; remedy; deliverance from wrong, injury or oppression; as the redress of grievances." Today: setting a wrong right (a rare word). Hardly moved. Both fills "a fix for".
- regulate (E3). 1828 sense 3: "To subject to rules or restrictions; as, to regulate trade". Today: control by rules. Hardly moved. Both fills "set the rules for".
- Commerce (E3). 1828 sense 1: "an interchange or mutual change of goods, wares, productions, or property of any kind, between nations or individuals"; sense 2: "Intercourse between individuals". Today: buying and selling. Some. Now "buying and selling" / 1787 "trade and dealings of every kind".
- palladium (E4). 1828 sense 2: "Something that affords effectual defense, protection and safety"; sense 1 tells of the statue of Pallas on which "depended the safety of Troy". Today: a silvery metal. Big. Now "a precious metal" / 1787 "the shield".
- jealous, jealousy (E4, E5). 1828 sense 3: "Suspicious caution or vigilance, an earnest concern or solicitude for the welfare or honor of others." Today: envy of a rival. Big. Now "envious worry" / 1787 "watchful care" (E4); Now "envy" / 1787 "watchful suspicion" (E5).
- entangle (E6). 1828 sense 3: "To involve in difficulties; to perplex; to embarrass; as, to entangle a nation in alliances." Today: to tangle up. Hardly moved. Both fills "tangle up". The card notes that Webster's own example sentence is about alliances.
- party (E7). 1828 sense 1: "A number of persons united in opinion or design, in opposition to others in the community." Today: a political party, or a celebration. Some. Now "a political party" / 1787 "groups set against each other".

**Clues** (Drift, Check the clue)
- E1: Article IV, Section 4: the United States shall protect each State "against Invasion; and on Application of the Legislature, or of the Executive (when the Legislature cannot be convened) against domestic Violence." Line: "Here 'domestic Violence' means an uprising inside a state. The 1787 reading fits."
- E2: Webster 1828, establishment sense 6, names England's church. Line: "The 1787 reading fits: the clause is about an official church."
- E3: the clause lists three partners: "foreign Nations", "the several States", "the Indian Tribes". Line: "Both: trade is trade, but the clause treats Native nations as separate from the states."
- E4 to E7: Washington's own next words (E5 follows a warning about "the insidious wiles of foreign influence"). Line: "1787: he wants citizens watchful, not envious."

**Trails** (Trail mode; exact words from the transcript)
- a more perfect Union: Article IV, Section 1 ("Full Faith and Credit shall be given in each State to the public Acts, Records, and judicial Proceedings of every other State"); Article VI ("This Constitution, and the Laws of the United States which shall be made in Pursuance thereof ... shall be the supreme Law of the Land").
- establish Justice: Article III, Section 1 ("The judicial Power of the United States, shall be vested in one supreme Court, and in such inferior Courts as the Congress may from time to time ordain and establish").
- insure domestic Tranquility: Article I, Section 8 ("To provide for calling forth the Militia to execute the Laws of the Union, suppress Insurrections and repel Invasions"); Article IV, Section 4 (above).
- provide for the common defence: Article I, Section 8 ("To raise and support Armies", "To provide and maintain a Navy").
- promote the general Welfare: Article I, Section 8 ("To lay and collect Taxes, Duties, Imposts and Excises, to pay the Debts and provide for the common Defence and general Welfare of the United States").
- secure the Blessings of Liberty: Article I, Section 9 ("The Privilege of the Writ of Habeas Corpus shall not be suspended, unless when in Cases of Rebellion or Invasion the public Safety may require it").

**Left out** (cards; exact words then one plain line)
- L1 Article I, Section 2: "adding to the whole Number of free Persons ... and excluding Indians not taxed, three fifths of all other Persons." Plain: Enslaved people were counted as three fifths of a person to give slaveholding states more seats; they had no vote.
- L2 same clause, "Indians not taxed": Native people living in their own nations were not counted at all.
- L3 Article I, Section 9: "The Migration or Importation of such Persons as any of the States now existing shall think proper to admit, shall not be prohibited by the Congress prior to the Year one thousand eight hundred and eight". Plain: Congress could not ban the slave trade before 1808.
- L4 Article IV, Section 2: "No Person held to Service or Labour in one State ... escaping into another, shall ... be discharged from such Service or Labour, but shall be delivered up". Plain: People who escaped slavery had to be returned.
- L5 Article I, Section 2: "the Electors in each State shall have the Qualifications requisite for Electors of the most numerous Branch of the State Legislature." Plain: The Constitution left voting to the states, and nearly all of them barred women.
- L6 (Commerce Clause): "with the Indian Tribes": Native nations are named only as trading partners, outside "We the People".
- Note shown with L1: the words "slave" and "slavery" do not appear in the 1787 Constitution; it says "Persons held to Service" and "all other Persons".

**Context cards**: Preamble (written by the Committee of Style, September 1787); First Amendment (ratified 1791, the first of ten ratified); Farewell (published September 1796, in Philadelphia's American Daily Advertiser); Webster's dictionary (1828, the first big American dictionary, so it shows senses close to the founders' time but 41 years later).

## Interactions in detail
- Word cards open on tap, Enter or Space; Escape closes. One card open at a time; on narrow screens the card is a bottom sheet that does not cover the tapped word.
- Drift switches: Space or Enter flips; switch state shows by its word (Now / 1787) and position, never color alone. "Meaning changed" buttons wait until one switch is flipped. Words marked Hardly moved still flip but show "Same either way" and change nothing; that is the point.
- Flipping all switches back to Now restores the original Today reading exactly.
- Trail draws one trail at a time; a second tile replaces the first. With Motion off the line appears without drawing.
- localStorage key `fwe.v1` (try/catch): switch states, "Meaning changed" choices, notes. Without storage everything works for the session and the panel says so.
- At 680 x 425 the Drift paraphrase and the meter stay visible with the sentence; the clue opens in the panel.

## Look
Light parchment, a different world from premise-inspector's dark light table. Paper #f4ecd8, panel #fbf6e9, ink #2a1d14, muted #5f4c3c. Accent brand #8c5138 (iron-gall brown); white text on brand fills. 1828 marks #3d5a1e (green-black ink) with the clock glyph; Context pins #7a1f3d; focus ring #1f5fa8.
Contrast (WCAG): brand on paper 5.33, on panel 5.81, white on brand 6.27; ink on paper 13.89; muted on paper 6.9; 1828 green on paper 6.66; context on paper 8.53; focus on paper 5.47. Nearest catalog accent: nations-of-north-america #5a3b25 at dE 18.1.
Type: a serif for document text at 1.1 rem with generous leading; the kit sans for UI. Drift badges are pill shapes with the badge word.

## Art
Six painted images, all local FLUX (`scripts/localart.py`), people: false. This tool touches hard history (the Left out layer): no image shows a person, and the Left out cards stay text only, with no pictures.
- `parchment`: "Close-up of plain cream laid paper, soft fibers and faint chain lines, even light, filling the frame". 16:10; cutout no; people: false. A full-frame texture under the document card, blended over `--paper` at 35 percent so the measured text contrast in Look still holds (check ink on the texture's darkest patch at build).
- Then-and-now kit (2 cutouts, one shared prompt: "single object, three-quarter view, soft studio light, plain light backdrop, painted"): `quill` a goose quill pen standing in a glass inkwell; `laptop` an open laptop with a blank glowing screen. 1:1; cutout yes; people: false. Sizing rule: 24 px beside the **1787** and **Now** labels of every Drift switch, 40 px beside the **1828** and **Today** headings of the word card.
- `webster`: "A thick old leather-bound dictionary, closed, worn gilt page edges, blank spine". 1:1; cutout yes; people: false. On the word card's 1828 section header (40 px) and the Webster's dictionary context card (120 px).
- `assembly`: "Empty eighteenth-century assembly room, rows of wooden Windsor chairs, tables with green cloth, tall paned windows, quill pens on the tables, summer light". 16:9; cutout no; people: false. Header picture on the Preamble, First Amendment and Commerce Clause context cards (about 280 px wide).
- `press`: "A wooden hand printing press of the 1790s in a print shop, a tray of metal type, stacks of blank paper, window light". 16:9; cutout no; people: false. Header picture on the Farewell Address context card.
Drawn in code: the clock glyph, drift badges, switches, the Drift meter, the section ribbon, Trail tiles and trail lines, and the layer glyphs.

## Voice
Bank voice `news-reader`, style "Say clearly and steadily, like an evening news anchor explaining a story." Not used by a family sibling, a grade 9 ELA neighbor or another spec in this batch. `Curio.voice`, `scope: () => state.mode + state.doc`. Document text is not read by the voice (Read speaks the hint).
- w-read (how, Read welcome; stale once a word card opens): "Words with a dotted line have changed since 1787. Tap one to open its card."
- layers (how, first layer toggle; stale on mode change): "Layers add notes. Tap Left out to see who these words did not cover."
- w-drift (how, Drift welcome; stale once a switch is flipped): "This is how the sentence sounds today. Tap a switch to 1787 and watch the reading change."
- same (how, first Hardly moved switch flipped; stale on the next flip): "That word has hardly moved. The sentence stays the same."
- meaning (how, first flip of any switch, when the Yes and No buttons turn on; stale once Yes or No is chosen): "Did the meaning of the whole sentence change? Tap Yes or No."
- clue (how, first Check the clue; stale once Now, 1787 or Both is tapped, or on Next, Previous or tab change): "The clue comes from the same documents. Tap Now, 1787 or Both."
- w-trail (how, Trail welcome; stale once a tile is tapped): "Tap a purpose to follow it into the Constitution."

## Family engine
Uses `kit/founding-docs.js` as described in full in tools/premise-inspector/spec.md (Family engine).
- Doc: the Preamble, First Amendment, Commerce Clause and Farewell excerpts above, plus the Trail and Left out clauses as spans of a Constitution doc.
- Layers: `plain`, `context`, `leftout`.
- Lens: one entry per drift word `{then:{sense, source:'Webster 1828, sense n'}, today:{sense, source:'plain gloss'}, note, badge}`. This tool is the Lens's main user; the Drift switch reads `then`/`today` fills from an added `fills:{now, then}` field on each entry.
- Reader: section ribbon and goto.
- Not used: Links, Bins.

## Sources
- Constitution text (Preamble, Art. I s2, s8, s9; Art. III s1; Art. IV s1, s2, s4; Art. VI): National Archives transcript, https://www.archives.gov/founding-docs/constitution-transcript. Absence of "slave" and "slavery" checked by search of that transcript.
- First Amendment: National Archives, Bill of Rights transcript ("Article the third"), https://www.archives.gov/founding-docs/bill-of-rights-transcript.
- Washington's Farewell Address, 1796: Avalon Project, Yale Law School, https://avalon.law.yale.edu/18th_century/washing.asp.
- Webster 1828 senses: Noah Webster, An American Dictionary of the English Language (1828), online at https://webstersdictionary1828.com/Dictionary/<word> (insure, domestic, tranquillity, welfare, posterity, ordain, establishment, abridge, press, redress, regulate, commerce, palladium, jealousy, entangle, party), checked 2026-10-27.
- Today glosses: the tool's own plain wording, checked against Merriam-Webster online; no definitions copied.
- Committee of Style, September 1787; First Amendment ratified 1791; Farewell first printed in the American Daily Advertiser, September 1796: National Archives "Constitution of the United States: A History" and Mount Vernon's Farewell Address page; confirm both at build.
- Checks run in Python (2026-10-29): Webster 1828 is 41 years after 1787 (as the context card says); E1 has five switches (insure, domestic Tranquility, Welfare, Posterity, ordain), four of which change a fill.
- Voting left to the states: Article I, Section 2 (transcript above). Women barred in nearly every state, New Jersey the exception for property-owning women until its 1807 law: Wikipedia, "Women's suffrage in New Jersey", checked 2026-10-27; confirm at build against NPS or the New Jersey State Archives.

## Done when
1. Focus: at 1366x768 and 680x425 the document text is the largest thing on screen in Read, the paraphrase with its switches in Drift, and the trail column in Trail.
2. Every document tab shows the exact transcript text, and every drift word in Content has a dotted underline and opens its card with the 1828 quotation and sense number.
3. In Drift E1, flipping insure, domestic Tranquility, Welfare and ordain changes the paraphrase to the 1787 fills; flipping Posterity shows "Same either way".
4. Flipping every switch back restores the Today reading exactly.
5. Check the clue on E1 shows the Article IV words and its line; no score appears anywhere.
6. Trail draws each of the six purposes to its clause cards with article and section; tapping a second tile while a trail is still drawing replaces it at once, and flipping a switch during its highlight acts at once.
7. Left out shows L1 to L6 in Read and L1 to L5 in Trail, each with exact words and a plain line, and the "slave" note with L1; the Left out cards carry no images.
8. The Drift switches show the quill (1787) and laptop (Now) icons beside their words; context cards show their paintings; no people appear anywhere.
9. No voice line names a control that is hidden or disabled ("Tap Yes or No" plays only once a switch has been flipped and the buttons are on).
10. Notes and switch states survive a reload; Clear my readings wipes them; with storage blocked the tool runs and says so.
11. At 680 x 425 and 375 wide no horizontal scroll; switches, meter and tabs are reachable without scrolling.

## Open questions
- founding-words-explorer: Today glosses are the tool's own plain wording; use Wiktionary quotations instead (open licence, but long)?
- founding-words-explorer: The concept also mentions "how phrases echo in later speeches"; that now lives in premise-inspector. Is the split right?
- founding-words-explorer: Webster's dictionary is 1828, 41 years after the Constitution. Acceptable as "close to the founders' time", or add Johnson's 1755 dictionary as a second "then"?

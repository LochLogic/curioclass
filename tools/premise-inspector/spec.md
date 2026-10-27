# Premise Inspector

## One idea
The Declaration of Independence argues from four premises to one conclusion; lay a later speaker's words over it like a sheet on a light table and stamp each premise Accepts, Stretches, Rejects or Not addressed, and the finished bench shows a pattern you can explain: the people the Declaration left out mostly accepted its premises and stretched them to cover themselves, while the one speaker who rejected the first premise did it to found a nation on slavery, and still kept the right to throw off a government.

## Not like
- founding-words-explorer (ela 9, family sibling): reads the Preamble and Washington's Farewell word by word with then-and-now senses. Here words are not glossed; the unit is the premise, and the subject is how later arguments use it.
- reconstruction-amendments (social studies 8, family sibling): promises in the amendments against what undid them. Here no law is tracked; speakers are compared as arguers.
- argument-map (ela 12, rhetoric family): the student builds one essay's support tree and pulls claims out. Here the Declaration's structure is given; the work is comparing five other texts against it.
- rhetorical-situation-simulator (ela 11): changes the room around a fixed speech. Here the speeches are fixed and in their own rooms; the comparison is between their premises.
- american-lit-timeline (ela 11): pairs works from the same years by theme. Here the pairing is always "this text against the Declaration", across 27 years and five speakers.
- satire-decoder (ela 11): what a text means beneath what it says. Here every speaker means what they say.

## Who and how
- Grade 11 ELA, module Founding Documents and Rhetoric (Reading Informational Text): "Analyze 17th-19th century US documents and their premises".
- Driver: students, alone or in pairs, on laptops. A teacher can project the Bench for the first ten minutes. 40 to 50 minutes for all five sheets; one sheet plus the Bench fits 20.
- Standards: RI.11-12.8 (delineate and evaluate the reasoning in seminal U.S. texts, including premises, purposes and arguments): Bench and Overlay. RI.11-12.9 (analyze foundational U.S. documents of historical and literary significance for their themes, purposes and rhetorical features): Overlay and Pattern.
- tool.json: driver "students", minutes "20-50", modes ["Bench", "Overlay", "Pattern"], grades_label "Grade 11". Kit starter plus `kit:founding-docs` and `kit:theme-912`.
- Hard history: slavery, Native dispossession and an openly white-supremacist speech appear. Explorer only: no points, timers or win states. A **For teachers** drawer (header) holds the notes under Content, "Teacher notes".

## Screens and modes
Header: title "Premise Inspector", small line "Four premises, five later voices."; mode buttons **Bench** (opens first), **Overlay**, **Pattern**; **For teachers**; Motion, Sound, Read. Layout: a section ribbon across the top of the work area (engine Reader), the light table in the middle, a panel on the right with `#hint`. At 760 wide and below the panel drops under the table; at 375 the ribbon becomes a select box.

### Bench (opens first)
- The light table shows the Declaration (National Archives transcript) as five lit cards in argument order, not page order: **P1** truths, **P2** governments and consent, **P3** right to alter or abolish, **P4** the King's history, **C** conclusion. Lines run P1 to P2 to P3 ("so, when..."), P4 into P3 ("this is that case"), P3 and P4 into C. Each card shows the exact words from Content; a small **In the text** link scrolls the reader strip below the table to that sentence with a highlight.
- Under P4 sits the **Evidence drawer** (button **Open the 27 grievances**). It slides up as 27 small tags G1 to G27 with their opening words. Filter chips: **All**, **Laws and assemblies**, **Courts**, **Armies and war**, **Trade, taxes and land** (one grouping, Content). Tapping a tag shows its full sentence. A chip count reads "10 of 27 are about laws made or blocked without the colonists' assemblies: the consent premise (P2) at work inside P4."
- Two **Objection answered** pins hang off P3 and P4: the prudence sentence and the petitions sentence (Content). The panel says what objection each answers.
- **Left out** layer toggle (engine Layers, glyph: an open bracket): marks the words "all men", "the People", "domestic insurrections" and "merciless Indian Savages" and opens context cards X1 to X4. Off by default; the hint suggests it once P1 has been opened.
- Panel: the selected card's plain-English line (Content), and a one-line question per card: P1 "Is this a fact, a value or a promise?", P2 "Who counted as 'the governed' who could consent?", P3 "Who decides when a government is destructive?", P4 "Does a list of facts prove a design?" Answers are private notes (one box per card).

### Overlay
- A row of five sheet buttons in date order: **Apess 1836**, **Seneca Falls 1848**, **Douglass 1852**, **Stephens 1861**, **Lincoln 1863**. Each shows a context strip first (speaker, date, place, audience: Content) with **Lay it on the table**.
- The sheet slides over the bench as a translucent layer (fade only with Motion off). Its excerpt lines (Content, R-ids) float near the premise they bear on; lines bearing on none sit at the edge.
- On each premise card an empty stamp slot. The student picks a stamp (**Accepts**, **Stretches**, **Rejects**, **Not addressed**), then taps one or more sheet lines as the evidence. A stamp without evidence shows "Pin a line"; Not addressed needs none. Stamps show their word and glyph (check, outward arrows, cross, dash).
- Definitions on the stamp tray: Accepts: the speaker uses the premise as it stands. Stretches: keeps the premise but applies it to people or cases the 1776 text did not. Rejects: says the premise is false. Not addressed: the text leaves it alone.
- **Compare with one reading** (after all four premises are stamped): each slot shows Same, Also fair or Another reading (engine Links compare) with the one-line reason from Content. Never "wrong", no score.
- **Next sheet** and **Lift sheet**. Stamps persist per sheet in localStorage.

### Pattern
- A 5 x 4 grid: sheets down, premises across, filled with the student's stamps (unstamped cells dashed). **Show one reading** switches the grid to the key; **Show both** splits each cell.
- Column readouts computed from whichever grid is shown, for example "P1: 2 accept, 2 stretch, 1 rejects."
- Three pattern prompts, each with a private answer box: "Which premise did the most work for people the Declaration left out?", "Stephens rejects P1 and keeps P3. What does that show about how premises can be separated?", "Lincoln calls P1 a 'proposition'. What changes when a self-evident truth becomes a proposition to be tested?"
- **Clear my notes and stamps** (confirm step) wipes this tool's storage.

## Content
Text from the National Archives transcript, spelling kept ("Brittish", "endeavoured"). Source dashes are shown as "--" (group open question).

**Declaration cards**
- P1: "We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable Rights, that among these are Life, Liberty and the pursuit of Happiness." Plain: Everyone has the same basic rights from birth, and no government gives them.
- P2: "That to secure these rights, Governments are instituted among Men, deriving their just powers from the consent of the governed". Plain: Governments exist to protect those rights, and their power is fair only if the people agree to it.
- P3: "That whenever any Form of Government becomes destructive of these ends, it is the Right of the People to alter or to abolish it". Plain: When a government attacks those rights, the people may change it or end it.
- P4: "The history of the present King of Great Britain is a history of repeated injuries and usurpations, all having in direct object the establishment of an absolute Tyranny over these States. To prove this, let Facts be submitted to a candid world." Plain: The King has done exactly that, on purpose, and here is the list.
- C: "That these United Colonies are, and of Right ought to be Free and Independent States". Plain: So we are leaving.
- Objection pin on P3: "Prudence, indeed, will dictate that Governments long established should not be changed for light and transient causes". Answers: "Revolution over small things is reckless."
- Objection pin on P4: "In every stage of these Oppressions We have Petitioned for Redress in the most humble terms: Our repeated Petitions have been answered only by repeated injury." Answers: "Why not ask first?"

**Grievances** (full sentences from the transcript; id, opening words, group: L laws and assemblies, J courts, W armies and war, T trade, taxes and land)
G1 "He has refused his Assent to Laws" L; G2 "He has forbidden his Governors to pass Laws" L; G3 "He has refused to pass other Laws for the accommodation of large districts" L; G4 "He has called together legislative bodies at places unusual" L; G5 "He has dissolved Representative Houses repeatedly" L; G6 "He has refused for a long time, after such dissolutions" L; G7 "He has endeavoured to prevent the population of these States" T; G8 "He has obstructed the Administration of Justice" J; G9 "He has made Judges dependent on his Will alone" J; G10 "He has erected a multitude of New Offices" T; G11 "He has kept among us, in times of peace, Standing Armies" W; G12 "He has affected to render the Military independent" W; G13 "He has combined with others to subject us to a jurisdiction" L; G14 "For Quartering large bodies of armed troops" W; G15 "For protecting them, by a mock Trial" J; G16 "For cutting off our Trade" T; G17 "For imposing Taxes on us without our Consent" T; G18 "For depriving us in many cases, of the benefits of Trial by Jury" J; G19 "For transporting us beyond Seas" J; G20 "For abolishing the free System of English Laws in a neighbouring Province" L; G21 "For taking away our Charters" L; G22 "For suspending our own Legislatures" L; G23 "He has abdicated Government here" W; G24 "He has plundered our seas" W; G25 "He is at this time transporting large Armies of foreign Mercenaries" W; G26 "He has constrained our fellow Citizens taken Captive" W; G27 "He has excited domestic insurrections amongst us" W.
Counts: L 10, J 5, W 8, T 4. The grouping is the tool's own; the panel says "one grouping".

**Left out cards**
- X1 "all men": The text does not say whom "men" covers. Its author, Thomas Jefferson, held people in slavery. The sheets argue over exactly this word: Native people (1836), women (1848), the enslaved (1852).
- X2 "the People" and "consent": The text does not say who counts as "the governed" who can consent. The Seneca Falls sheet answers for women: laws "in the formation of which she had no voice".
- X3 "domestic insurrections" (G27): In November 1775 Virginia's royal governor, Lord Dunmore, declared "all indented Servants, Negroes, or others, (appertaining to Rebels,) free that are able and willing to bear Arms". Jefferson's rough draft had a longer passage blaming the King for the slave trade and for "exciting those very people to rise in arms among us"; that passage is not in the text Congress adopted.
- X4 "merciless Indian Savages" (G27): The Declaration names Native nations only as enemies on the frontier. They are not part of "the People" it speaks for.

**Sheets** (speaker, date, place; excerpt lines R; one reading per premise with evidence and reason)
- Apess 1836. William Apess (Pequot), "Eulogy on King Philip", the Odeon, Boston, January 8, 1836 (second edition 1837). Audience: Boston, white and Native listeners.
  - A1 (title page): "Who shall stand in after years in this famous temple, and declare that Indians are not men? if men, then heirs to the same inheritance."
  - A2: "the pilgrims landed at Plymouth; and without asking liberty from any one, they possessed themselves of a portion of the country, and built themselves houses, and then made a treaty, and commanded them to accede to it."
  - A3: "every white man would be called to go out and act the part of a patriot, to defend their country's rights"
  - A4: "let every man of color wrap himself in mourning, for the 22d of December and the 4th of July are days of mourning and not of joy."
  - Key: P1 Stretches (A1: "if men, then heirs"); P2 Stretches (A2: a treaty Native people were commanded to accept is not consent), also fair Not addressed; P3 Stretches (A3: Philip's people did what white patriots would be praised for); P4 Not addressed, also fair Stretches (the eulogy is its own history of injuries).
- Seneca Falls 1848. Declaration of Sentiments, Elizabeth Cady Stanton, Women's Rights Convention, Seneca Falls, New York, July 19 to 20, 1848; signed by 68 women and 32 men, Frederick Douglass among them.
  - S1: "We hold these truths to be self-evident; that all men and women are created equal".
  - S2: "He has never permitted her to exercise her inalienable right to the elective franchise. He has compelled her to submit to laws, in the formation of which she had no voice."
  - S3: "it is the right of those who suffer from it to refuse allegiance to it".
  - S4: "The history of mankind is a history of repeated injuries and usurpations on the part of man toward woman".
  - S5 (its own left-out line): "He has withheld from her rights which are given to the most ignorant and degraded men - both natives and foreigners."
  - Key: Stretches on all four (S1 to S4). S5 bears on no premise; the panel asks "Whom does this sentence rank below women?"
- Douglass 1852. Frederick Douglass, "What to the Slave Is the Fourth of July?", Corinthian Hall, Rochester, New York, July 5, 1852.
  - D1: "Are the great principles of political freedom and of natural justice, embodied in that Declaration of Independence, extended to us?"
  - D2: "Must I undertake to prove that the slave is a man? That point is conceded already."
  - D3: "The principles contained in that instrument are saving principles."
  - D4: "They were peace men; but they preferred revolution to peaceful submission to bondage."
  - D5: "This Fourth July is yours, not mine."
  - Key: P1 Accepts (D2, D3: the premise already covers the enslaved; the nation breaks it), also fair Stretches; P2 Not addressed; P3 Accepts (D4, praising the founders), also fair Not addressed; P4 Not addressed.
- Stephens 1861. Alexander H. Stephens, Vice-President of the Confederate States, "Cornerstone Speech", the Athenaeum, Savannah, Georgia, March 21, 1861 (text as reported in a newspaper account).
  - T1: "Those ideas, however, were fundamentally wrong. They rested upon the assumption of the equality of races. This was an error."
  - T2: "Our new government is founded upon exactly the opposite idea".
  - T3: "Seven States have within the last three months thrown off an old government and formed a new."
  - The "corner-stone" sentence that follows T2 is summarized on screen, not shown: he says the new government rests on the claim that Black people are not equal to white people and that slavery is their natural condition. (Open question.)
  - Key: P1 Rejects (T1, T2); P2 Not addressed; P3 Accepts (T3 echoes "throw off such Government"); P4 Not addressed.
- Lincoln 1863. Abraham Lincoln, Gettysburg Address (Bliss copy), Gettysburg, Pennsylvania, November 19, 1863.
  - N1: "dedicated to the proposition that all men are created equal."
  - N2: "testing whether that nation, or any nation so conceived and so dedicated, can long endure."
  - N3: "that government of the people, by the people, for the people, shall not perish from the earth."
  - Key: P1 Accepts (N1, N2: now a proposition under test); P2 Accepts (N3); P3 Not addressed (panel: the seceding states claimed this premise; the speech does not answer them); P4 Not addressed.

**Teacher notes** (For teachers drawer): Read Stephens with the class, not alone; he is here because rejecting the equality premise was the stated foundation of the Confederacy, in its Vice-President's words. Apess calls Metacom (King Philip) a patriot to Boston listeners in 1836. Douglass signed the Seneca Falls declaration four years before his Rochester speech. Suggested order: Seneca Falls, Douglass, Lincoln, Apess, Stephens.

## Interactions in detail
- Stamping: tap a slot, pick a stamp, tap lines (they gain a pin glyph and the slot lists their ids). Keyboard: Tab to slot, 1 to 4 for stamps, then arrows and Enter to pin lines, Escape to finish. Changing a stamp keeps its pins unless it becomes Not addressed (pins cleared, with an **Undo** for 5 seconds).
- Compare is enabled only when all four slots on the sheet are filled; before that it reads "Stamp all four first".
- A sheet line can be pinned to more than one premise.
- The Pattern grid works with any number of sheets stamped; unstamped rows say "Not inspected yet" and are left out of the counts.
- Lift sheet keeps stamps. Clear wipes stamps and notes for this tool only.
- localStorage key `pi.v1`, wrapped in try/catch; without storage the tool works for the session and the panel says "Your stamps will not be kept after you close this."
- At 680 x 425 the evidence drawer opens over the table rather than pushing it; every main control stays on screen without scrolling.

## Look
Dark light-table: the table is paper #0d1219 with a faint 24 px grid in #18202b; cards are panel #141b25 with a soft top glow when lit; sheets are a #e8edf3 layer at 8 percent opacity with lines in ink. Accent brand #cccc14 (inspection-lamp yellow), brand-ink #1a1a00 on brand fills. Stamps: Accepts #6fdca6, Stretches #8fc7ff, Rejects #ffb8a8, Not addressed muted #a6b3c4; each also carries its word and glyph. Focus ring #ff9ad5.
Contrast (WCAG): brand on panel 10.07, on paper 10.93; brand-ink on brand 10.25; Accepts on panel 10.27; Stretches 9.71; Rejects 10.45; Not addressed 8.13; focus 8.93; ink #e8edf3 on panel 14.7. Nearest catalog accent: zipline-energy #d0c440 at dE 15.1.
Type: kit 9-12 sans for UI; quotations in the kit serif at 1.05 rem with source ids in small caps.

## Art
none: drawn in code (cards, stamps, grid, sheet layer). No people.

## Voice
Bank voice `science-narrator`, style "Say evenly, like an inspector reading findings into a record." Not used by any family sibling or grade 9-12 ELA neighbor. `Curio.voice`, `scope: () => state.mode + state.sheet`. The voice never reads the historical texts aloud (Read speaks the hint).
- w-bench (how): "Four premises lead to one conclusion. Tap a card to see its words."
- drawer (how, first open): "These are the facts offered for premise four. Try a filter."
- left (how, first Left out toggle): "Bracketed words mark who the text left out. Tap one."
- w-overlay (how): "Lay a sheet on the table, then stamp each premise."
- pin (how, first stamp without evidence): "Now tap the line that shows it."
- compared (event, after Compare; stale on any stamp change or sheet change): "Here is one reading beside yours."
- stephens (how, first time the Stephens strip opens): "This speech defends slavery. Read it as evidence of an argument, not as an argument to accept."
- w-pattern (how): "Each row is a speaker. Each column is a premise. Read down a column."

## Family engine
`kit/founding-docs.js` (family founding-docs: rights-match, grade 5; constitutional-convention, grade 8; reconstruction-amendments, grade 8; founding-words-explorer, grade 9; premise-inspector, grade 11). No family doc exists; this spec holds the full description. Pure parts in one marked block, exposed as `__tool.fd`.
- **Doc**: `{id, title, author, date, place, edition, source, sections:[{id, label, spans:[{id, text, start, end}]}]}`. Text stored exactly as in the edition; spans are character ranges, checked by `fd.check(doc)` (console error on drift).
- **Layers**: `fd.layer(doc, {id, label, glyph, items:[{span, card:{title, text, source}}]})`. Standard layers: `plain` (plain-English line per span), `context`, `leftout`. Each layer has a glyph and a word as well as a color; toggles are independent.
- **Lens**: `fd.lens(word, {then:{sense, source}, today:{sense, source}, note})` opens a word card on tap. Used by founding-words-explorer (Webster 1828 against today); not used here.
- **Links**: `{from:{doc, span}, to:{doc, span}, stance: 'accepts'|'stretches'|'rejects'|'silent', evidence:[span], reason}`. `fd.links.matrix(rows, cols, links)` returns the grid and column counts; `fd.links.compare(mine, key)` returns `same | also | different` per cell with the reason; it never returns "wrong".
- **Reader**: a section ribbon (one block per section, width by length, labeled) above a scrolling reader; `fd.reader.goto(span)` scrolls and highlights; ribbon becomes a select at 375 wide.
- **Bins**: `fd.bins(items, bins, key)` for sorting tasks (rights-match sorts scenarios into amendments), with the same compare rule.
This tool uses: Doc (Declaration and five sheets), Layers (plain, leftout), Links, Reader. Not Lens or Bins.

## Sources
- Declaration of Independence: National Archives transcript, https://www.archives.gov/founding-docs/declaration-transcript (grievance count and order checked against it).
- Jefferson's rough draft passage: Library of Congress, "Declaring Independence: Drafting the Documents", https://www.loc.gov/exhibits/declara/ruffdrft.html (Boyd's reconstruction, Papers of Thomas Jefferson vol. 1); absence from the adopted text checked against the Archives transcript.
- Dunmore's Proclamation, November 7, 1775: text on Wikisource, "Dunmore's Proclamation", https://en.wikisource.org/wiki/Dunmore%27s_Proclamation.
- Declaration of Sentiments and its 68 women and 32 men signers, including Frederick Douglass: Women's Rights National Historical Park, https://www.nps.gov/wori/learn/historyculture/declaration-of-sentiments.htm. Convention dates July 19 to 20, 1848: https://www.nps.gov/wori/index.htm.
- Douglass, "What to the Slave Is the Fourth of July?", July 5, 1852, Corinthian Hall, Rochester: Wikisource transcription of the 1852 pamphlet, https://en.wikisource.org/wiki/What_to_the_Slave_Is_the_Fourth_of_July%3F.
- Apess, Eulogy on King Philip, second edition, Boston, 1837, title page and text: Internet Archive, https://archive.org/details/eulogyonkingphil00apes. Apess, Pequot, 1798 to 1839: Wikipedia, "William Apess", checked 2026-10-27; confirm at build.
- Stephens, "Cornerstone Speech", March 21, 1861, Savannah, as reported: Wikisource, https://en.wikisource.org/wiki/Cornerstone_Speech (title "Vice-President" from the report's own text).
- Gettysburg Address, Bliss copy, November 19, 1863: Wikisource, https://en.wikisource.org/wiki/Gettysburg_Address_(Bliss_copy).
- Jefferson as an enslaver (more than 600 people over his adult life): Wikipedia, "Thomas Jefferson and slavery", checked 2026-10-27; confirm at build against the Thomas Jefferson Foundation, https://www.monticello.org/slavery/.

## Done when
1. Bench opens with five cards whose words match the Archives transcript exactly, and the lines run P1 to P2 to P3, P4 to P3, P3 and P4 to C.
2. The evidence drawer lists G1 to G27; filter counts read L 10, J 5, W 8, T 4.
3. Left out toggle marks four phrases and opens X1 to X4; X3 shows the Dunmore words and the rough-draft words.
4. Each of the five sheets lays over the table, and a stamp other than Not addressed cannot be saved without a pinned line.
5. Compare shows Same, Also fair or Another reading with a reason on every slot, never "wrong" and never a score.
6. Pattern grid counts match the stamps shown; Show one reading gives P1: 2 accept, 2 stretch, 1 rejects.
7. Stamps and notes survive a reload; Clear wipes them; with storage blocked the tool still runs and says so.
8. At 680 x 425 and 375 wide no horizontal scroll, and the stamp tray and sheet buttons are visible without scrolling.
9. Every stamp is readable without color (word and glyph).

## Open questions
- premise-inspector: Show Stephens' full "corner-stone" sentence on screen, or keep the summary used here?
- premise-inspector: Is the Stephens sheet right for grade 11 at all, or should it be teacher-unlocked from the For teachers drawer?
- premise-inspector: Should a Native reviewer (ideally Pequot or Mashpee) read the Apess sheet and the X4 card, as with Chief Joseph in rhetorical-situation-simulator?

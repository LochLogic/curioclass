# Usage Panel

## One idea
You chair a dictionary's usage panel: hear five panelists argue over one contested usage, rule on it separately for each setting, then drag a year slider and watch real style guides and the real American Heritage Dictionary Usage Panel change their minds, so you see that a usage "rule" has a birth year and often a reversal.

## Not like
- socratic-seminar-board: a projector board for a live class discussion; here the panel is scripted, a student chairs it alone or in a pair, and the evidence is a dated record of real rulings.
- argument-map: maps the structure of a whole essay; here the argument is over one word, and the output is a ruling and a usage note, not a node map.
- rhetorical-situation-simulator: changes speaker and audience for a speech; here the settings grid only decides whether one usage is acceptable where, and nothing is rewritten.
- tone-dial: rewrites a paragraph by mood; nothing here rewrites text.
- word-family-tree: traces where words came from; here the history is of opinions about a use, not of roots.
- fallacy-field-guide: spots and collects named fallacies; panelists here are never labeled or scored.
- punctuation-power-ups: a race with right answers; Usage Panel has no right answers, no score and no timer.
- american-lit-timeline: literary movements on a timeline; this timeline holds rulings and examples for one usage at a time.

## Who and how
- Grade 11, ELA (Language). Format: Role Play (council). Students drive on their own laptops, alone or in pairs; a teacher can also project it and let the class vote out loud.
- 20 to 40 minutes for one case; each case stands alone.
- Standards: L.11-12.1 (and its sub-point that usage is a matter of convention, can change over time, and is sometimes contested; L.11-12.1a). SL.11-12.1 (collaborative discussion when used in pairs: weigh and synthesize the claims on all sides).
- Look: 9-12 dark instrument theme. Link `kit:curio`, then `kit:theme-912`. Tool accent `--brand` a warm ink red (the copy editor's pencil), checked for AA contrast on the theme panel color. No confetti, no mascots.

## Screens and modes
Header: title "Usage Panel", three mode buttons in a `.seg` group: **Hearing**, **Record**, **Ruling**; then icon buttons **Motion**, **Sound**, **Read** (ids `motion`, `sound`, `read`).

Docket strip (always visible under the header): five case tabs, one per contested usage: **They**, **Literally**, **Hopefully**, **To boldly**, **Less**. Each tab shows the word in a large serif and a small status dot plus text ("not ruled" / "ruled"). Picking a tab keeps the current mode and swaps the case. First load opens **They** in Hearing.

### Hearing (start here)
- Stage: a long hearing table seen from the front, drawn in code (a dark bar with five nameplates). Above each nameplate sits a panelist card: a simple non-human icon drawn in SVG and the role name. No portraits, no faces.
- Center of the table: the **test sentence** card, large, with the contested word underlined. Arrows **Previous sentence** and **Next sentence** move through the case's 3 or 4 test sentences.
- Tap a panelist card (or press keys 1 to 5): the card lifts and its statement on the current case appears in a speech panel beside the table. Two small buttons under the statement: **Persuasive** and **Not for me**. They only tint that card (a filled pencil mark or an empty circle, plus the word) as a private note; nothing is scored.
- **Evidence** drawer (button at the bottom of the stage): opens the case's dated evidence cards (quotes from public-domain writers and style-guide rulings). Each card has the year in large readout type.
- **Your vote** row under the test sentence: **Acceptable**, **Acceptable in casual use only**, **Not acceptable**. After you vote, a **Real panel** bar slides in under the sentence if real American Heritage Dictionary (AHD) Usage Panel figures exist for that sentence: "In 2015, 48 percent of the AHD Usage Panel rejected this sentence. In 1996, 80 percent did." Sentences with no real panel figure show "No real panel vote on record for this sentence." The bar never shows before you vote.
- Panel side text (`hint`): "Pick a panelist to hear them. Vote on the sentence, then see how a real panel voted."

### Record
- Stage: a horizontal time axis from the case's earliest year to 2026, drawn in code, with tick labels. Markers sit on the axis: a round marker for "in use" (a writer using it), a square marker for "ruling" (a style guide or panel deciding on it). Shape plus a text label, never color alone.
- Below the axis: a **stance board**, one row per authority that has dated rulings in this case (for example AP Stylebook, Chicago Manual of Style, APA, AHD Usage Panel). Each row shows that authority's stance as of the slider year: **Accepts**, **Accepts in limited cases**, **Advises against**, **No ruling on record** (grey, dashed). Panel rows with percentages show a thin bar with the percent number.
- **Year** slider (big thumb, readout above it in large digits) from the case's earliest year to 2026. Dragging it moves a vertical line across the axis; markers left of the line light up, the stance board updates.
- Buttons: **Play the record** (sweeps the slider from start to 2026 over about 12 seconds, pausing 1.5 seconds at each marker so its card can be read; with Motion off the slider jumps marker to marker on the same timing), **Stop**, **Your ruling** (adds a diamond marker at 2026 labeled "Your panel, 2026" using the ruling from Ruling mode, or "Not ruled yet" if none).
- Tap any marker: its card opens in the side panel with the year, who, what they said or did, and the source line.

### Ruling
- Stage: a grid. Rows are the four settings: **Text to a friend**, **News story**, **School essay**, **Graduation speech**. Columns are **Accept**, **Accept with a note**, **Avoid**. One choice per row (radio groups, big targets).
- Under the grid: **Reasons** checklist, one checkbox per panelist argument ("The Linguist: people have used it this way for centuries" and so on). Pre-checked if you marked that panelist **Persuasive** in Hearing.
- **Usage note** panel: a generated note in dictionary style, rebuilt live as you change choices, then freely editable in a textarea. Buttons: **Rebuild note** (overwrites edits after a confirm), **Copy note**, **Clear ruling**.
- The note template: "Usage: [word, use]. Our panel accepts it in [settings marked Accept], accepts it with a note in [settings], and advises against it in [settings]. [One sentence per checked reason.] This ruling was made in 2026; earlier authorities ruled differently, beginning in [first ruling year on record]." Lists with one item read naturally ("in a news story"); empty groups are dropped.
- Saved per case in localStorage (`usage-panel-rulings`), wrapped in try/catch; works without it.

## Content
Panelists (the same five in every case; role names on cards, no personal names):
1. **The Copy Editor**: icon a red pencil. Cares about what readers expect and consistent house style.
2. **The Linguist**: icon a sound wave in a magnifier. Cares about evidence of how people actually speak and write.
3. **The Teacher**: icon a stack of papers with a check mark. Cares about clarity and what students will be graded on.
4. **The Poet**: icon a quill. Cares about rhythm, force and effect.
5. **The Reporter**: icon a notebook and microphone. Cares about readers of every age and not distracting from the news.

### Case 1: They (singular they)
Test sentences: (a) "If anyone calls, tell them I can't come to the phone." Real panel: 2008, 56 percent accepted. (b) "A person at that level should not have to keep track of the hours they put in." Real panel: 1996, 80 percent rejected; 2015, 48 percent rejected. (c) "We thank the anonymous reviewer for their helpful comments." Real panel: 2015, 58 percent rejected. (d) "Jordan uses they as their pronoun, and they will chair the meeting." No real panel vote shown (see Open question); a note card under it reads "For a person who uses they, AP (2017), Chicago (2017), APA (2019) and Merriam-Webster (2019) all use the person's pronoun." On sentence (d) the panelists all say a version of "We use the pronoun a person uses; the open question is the generic use," and the vote row is replaced by that note.
Statements: Copy Editor: "Many readers were taught that they must be plural. If a sentence makes them stop and wonder, it costs us. I rewrite when I can, and I allow it when rewriting is clumsy." Linguist: "Speakers have used they for one unknown person since around 1300. Shakespeare and Austen did it. A rule that most fluent speakers break every day is describing a style, not the language." Teacher: "He or she is clunky, and alternating he and she confuses readers. Generic they is clear. I want students to know some readers still object, so I teach both." Poet: "He or she breaks the rhythm of a sentence. They keeps it moving and includes everyone." Reporter: "Our readers range widely. I use it for anyone or a person, but I would rather name the person or make the subject plural."
Evidence and record (round = in use, square = ruling): about 1300, plural pronouns with singular antecedents in use (AHD note) (round). Early 1590s, Shakespeare, The Comedy of Errors: "There's not a man I meet but doth salute me / As if I were their well-acquainted friend" (round). 1813, Austen, Pride and Prejudice: "everybody said, they never saw so fat a haunch" (round). 1993, Chicago 14th edition spoke in favor of reviving singular they, as described by its 18th edition reviser (square). 1996, AHD panel: 80 percent reject sentence (b) (square). 2008, AHD panel: 56 percent accept (a), 59 percent accept "Everyone returned to their seats" (square). 2015, AHD panel: 48 percent reject (b), 58 percent reject (c) (square). March 2017, AP: they for people who do not use he or she; generic they only in limited cases where rewording is overly awkward (square). 2017, Chicago 17th edition: they for a person who prefers it; generic they still not fully accepted in formal writing (square). 2019, APA 7th edition: endorses singular they as a generic pronoun (square). September 2019, Merriam-Webster adds the nonbinary sense; December 2019, names they its Word of the Year (square). September 2024, Chicago 18th edition: generic singular they acceptable even in formal writing (square).
Stance board (generic they in formal writing): AP: No ruling on record before 2017, Accepts in limited cases from 2017. Chicago: Advises against from 2017, Accepts from 2024 (1993 shown as a marker only). APA: Accepts from 2019. AHD panel, sentence (b): 20 percent accept in 1996, 52 percent in 2015.

### Case 2: Literally (as an intensifier)
Test sentences: (a) "I literally died laughing." (b) "He literally glowed." (Fitzgerald, 1925) (c) "Tom was literally rolling in wealth." (Twain, 1876). No real panel figures; the bar says so.
Statements: Copy Editor: "Literally is the one word that promises no exaggeration. If it can also mean the opposite, I lose a tool. I cut it from formal copy." Linguist: "Dickens, Twain and Fitzgerald all used it to intensify. Merriam-Webster lists the sense, and its usage guide calls it hyperbole, not a mistake." Teacher: "In an essay it usually adds nothing and can make a reader laugh at the wrong moment. Cut it and the sentence gets stronger." Poet: "Gatsby literally glowed is a great line. Overstatement is a figure of speech, and this is how you mark it." Reporter: "A reader might take it at its word. In news, literally should mean literally."
Record: 1838 to 1839, Dickens, Nicholas Nickleby: "after he had literally feasted his eyes" (round). 1876, Twain, The Adventures of Tom Sawyer: "Tom was literally rolling in wealth" (round). 1925, Fitzgerald, The Great Gatsby: "He literally glowed" (round). Merriam-Webster today: lists the "in effect, virtually" sense with a usage note; its Dictionary of English Usage calls it hyperbole that needs care (square, placed at 2026 with the label "current entry", since the year it was added is not confirmed). Stance board: Merriam-Webster: Accepts in limited cases (listed, with a usage note) at 2026 only, No ruling on record before.

### Case 3: Hopefully (meaning "I hope")
Test sentences: (a) "Hopefully, the treaty will be ratified." Real panel: 1999, 34 percent accepted; 2012, 63 percent accepted. (b) "Hopefully, the bus is on time." (c) "She looked hopefully at the door." (the older sense, shown with the label "the sense no one disputes"). Extra card in the Real panel bar for (a): "In 2012, 89 percent accepted the same kind of sentence with mercifully."
Statements: Copy Editor: "Who is doing the hoping? The sentence does not say. I write we hope, which is clearer." Linguist: "The use goes back to at least 1648. Nobody objects to frankly or mercifully at the start of a sentence. The objection started in the 1960s." Teacher: "Students hear this one argued about in class. I tell them it is accepted now, and that some graders still circle it." Poet: "There is no single word that does its job. It sounds natural, which is the point." Reporter: "AP accepted it in 2012. It is fine in our pages."
Record: 1648, earliest known sentence-adverb use (Merriam-Webster) (round). 1960s, critics begin objecting (AHD note) (square). 1999, AHD panel: 34 percent accept (a) (square). April 2012, AP accepts the "it is hoped" sense (square). 2012, AHD panel: 63 percent accept (a) (square). Stance board: AP: No ruling on record before 2012, Accepts from 2012. AHD panel, sentence (a): 34 percent in 1999, 63 percent in 2012.

### Case 4: To boldly (the split infinitive)
Test sentences: (a) "She decided to quickly finish the essay." (b) "We expect to more than double the club's members." (c) "He wanted to really try."
Statements: Copy Editor: "Many readers still notice it. When the adverb can move without harm, I move it." Linguist: "Writers split infinitives in the 1200s and 1300s. The rule against it first appeared in print in the 1800s, with no reason older than taste." Teacher: "Try sentence (b) unsplit. To double more than our members? The split is the only clear version. Clarity wins." Poet: "Sometimes the adverb belongs right against the verb, for the beat." Reporter: "Readers do not complain about it any more than they complain about commas. If it reads cleanly, it stays."
Record: early 1200s, Layamon's Brut has a split infinitive (round). 1300s, John Wycliffe often splits infinitives (round). 1834, a writer in the New-England Magazine proposes a rule against it (square). 1864, Henry Alford, A Plea for the Queen's English, condemns it (square). 1926, H. W. Fowler, Modern English Usage: avoiding a split means rewriting the sentence, not just moving one word, and that is not always worth it (square). 1994, Merriam-Webster's Dictionary of English Usage: the objection never had a rational basis (square). 2018, The Economist Style Guide, 12th edition: split when moving the modifier would ruin rhythm or meaning (square). Stance board: Alford: Advises against from 1864. Fowler: Accepts in limited cases from 1926. Merriam-Webster usage guide: Accepts from 1994. The Economist: Advises against from 2012 (10th edition), Accepts in limited cases from 2018.

### Case 5: Less (with things you count)
Test sentences: (a) "Ten items or less." (b) "Less people came this year." (c) "The school is less than 50 miles away." (shown with the label "distance, time and money take less even for strict editors").
Statements: Copy Editor: "Fewer for things you count, less for amounts. It is a clean rule and readers expect it." Linguist: "Less with countable nouns goes back to King Alfred in 888. The rule began in 1770 as one writer's personal preference." Teacher: "Students lose points for this on tests. Know the rule, then decide when it matters." Poet: "Ten items or fewer is clunky on a sign. Less is shorter and sounds better." Reporter: "Less people sounds wrong to many of our readers. I use fewer in copy."
Record: 888, Alfred the Great writes "laes worda," less of words (OED, via secondary source) (round; display "læs worda" with the ash letter). 1770, Robert Baker, Reflections on the English Language: "most commonly used in speaking of a Number; where I should think Fewer would do better" (square). 1995, Merriam-Webster's Dictionary of English Usage: the rule is Baker's preference made absolute (square). 2004, The Cambridge Guide to English Usage: the choice is a matter of style (square). Stance board: Baker: Advises against from 1770. Merriam-Webster usage guide: Accepts in limited cases from 1995. Cambridge Guide: Accepts in limited cases from 2004.

## Interactions in detail
- Changing case or mode calls `Curio.stop()`. The Record slider resets to the case's earliest year on case change; Hearing returns to sentence (a).
- Votes and Persuasive marks persist per case for the session (and in the same localStorage key). The Real panel bar shows only after a vote on that sentence; changing the vote keeps the bar.
- Slider extremes: at the earliest year only the first marker is lit and all stance rows read No ruling on record unless a ruling sits on that year; at 2026 everything is lit. Keyboard: arrow keys move one year, Page Up and Page Down jump to the next or previous marker, Home and End go to the ends.
- Markers closer than 4 percent of the axis width stack vertically with a thin leader line so labels never overlap (the 2015 to 2019 cluster in Case 1 needs this).
- Ruling mode with nothing chosen: the note says "Choose a ruling for at least one setting to build a usage note." Clear ruling asks "Clear this case's ruling?" before clearing.
- Your ruling marker in Record: a diamond at 2026, label lists the four settings with short words ("Text: accept, News: avoid ...").
- Pair mode needs no extra screen; the Hearing vote row is enough for two students to argue over.
- Narrow screens (under 760 px): the hearing table becomes a two-row grid of cards; the stance board stacks under the axis.
- Read button reads the visible statement, sentence or marker card through the kit fallback.

## Art
- dictionary-desk: an old open dictionary on a dark wooden desk, low warm lamp light, shallow depth of field, no text legible, no people or hands; 16:9; cutout no; people no. Used faded behind the docket strip on first load only.
- Everything else (table, nameplates, the five panelist icons, axis, markers, stance board) is drawn in code.

## Voice
Bank `hs-narrator`, voice `Kore`, style "Read clearly and naturally, at a moderate pace". 11 lines:
1. welcome: "Welcome to the Usage Panel. You are the chair. Five panelists will argue about one word, and you will make the ruling."
2. hearing: "Pick a panelist to hear their case. Then vote on the sentence and see how a real dictionary panel voted."
3. record: "This is the record. Drag the year and watch real style guides change their minds."
4. ruling: "Now rule. Decide where this use belongs, from a text to a friend to a graduation speech, and write the usage note."
5. case-they: "Singular they. Can one person, or anyone at all, be they?"
6. case-literally: "Literally. Can a word that means exactly also mean the opposite?"
7. case-hopefully: "Hopefully. Can it mean I hope, at the start of a sentence?"
8. case-split: "The split infinitive. Is it wrong to put a word between to and its verb?"
9. case-less: "Less or fewer. Does ten items or less break a rule, and whose rule is it?"
10. record-end: "That is the record so far. Your panel's ruling is the newest entry."
11. note-done: "Your usage note is ready. Compare it with the rulings that came before it."
Lines 1 to 4 play once per mode on first visit (1 on the first tap anywhere), 5 to 9 when a case opens, 10 when Play the record reaches 2026, 11 the first time a note is built for a case.

## Family engine
none. Keep the case data (one `CASES` array) and the timeline and stance-board logic in one clearly marked block.

## Sources
- AHD usage notes, singular they (1300 date; 1996, 2008, 2015 panel figures): https://ahdictionary.com/word/search.html?q=they
- AHD usage note, hopefully (1960s objections; 1999 34 percent, 2012 63 percent, mercifully 89 percent): https://ahdictionary.com/word/search.html?q=hopefully
- AP and Chicago 17th edition singular they, March 2017: https://www.cjr.org/language_corner/stylebooks-single-they-ap-chicago-gender-neutral.php
- APA 7th edition singular they: https://libraries.indiana.edu/academic-style-guides-singular-pronoun-they
- Chicago 18th edition generic they (2024) and 14th edition (1993) remark: https://cmosshoptalk.com/2024/04/16/announcing-the-chicago-manual-of-style-18th-edition/ and https://www.chicagomanualofstyle.org/help-tools/what-s-new.html
- Merriam-Webster nonbinary they, September 2019, Word of the Year 2019: https://whyy.org/articles/merriam-webster-declares-they-its-2019-word-of-the-year
- Shakespeare, The Comedy of Errors, Act 4 Scene 3: https://www.gutenberg.org/ebooks/1504
- Austen, Pride and Prejudice (1813), Mrs. Bennet after the dinner: https://www.gutenberg.org/ebooks/1342
- Literally: Merriam-Webster, "Did we change the definition of literally?": https://www.merriam-webster.com/grammar/misuse-of-literally
- Dickens, Nicholas Nickleby: https://www.gutenberg.org/ebooks/967 ; Twain, Tom Sawyer, chapter 2: https://www.gutenberg.org/ebooks/74 ; Fitzgerald, The Great Gatsby, chapter 5: https://www.gutenberg.org/ebooks/64317
- Hopefully, 1648 and AP April 2012: https://www.merriam-webster.com/grammar/yes-you-can-use-hopefully-to-mean-i-hope
- Split infinitive history (Layamon, Wycliffe, 1834, Alford 1864, Fowler 1926, MWDEU 1994, Economist 2012 and 2018): https://en.wikipedia.org/wiki/Split_infinitive (builder: keep its cited works in the source comment)
- Less and fewer (Alfred 888, Baker 1770 quote, MWDEU 1995, Cambridge Guide 2004): https://en.wikipedia.org/wiki/Fewer_versus_less
- Test sentences without a credit are original writing.

## Done when
1. All five cases open from the docket strip, each with its panelists' statements, 3 or 4 test sentences and evidence cards, and no text says "and so on".
2. No image or icon shows a person, face or hand; panelists are role-named cards with SVG icons.
3. The Real panel bar appears only after a vote and shows the exact figures listed above (for example sentence (b) in They: 80 percent rejected in 1996, 48 percent in 2015).
4. In Record, dragging They to 2016 shows Chicago "No ruling on record" or blank, 2017 shows "Advises against", 2024 shows "Accepts"; keyboard arrows and Page Up/Down work.
5. Play the record sweeps to 2026 and plays line 10; with Motion off it jumps marker to marker on the same timing.
6. Overlapping markers (They, 2015 to 2019) stack and every label is readable at 1280 by 800 and at 375 px wide.
7. Ruling builds a grammatical usage note that updates live, survives a reload (when storage works), copies, and clears after a confirm.
8. Your ruling appears as a diamond at 2026 in Record.
9. Stance never depends on color alone (shape plus words), the accent passes AA, and every target is at least 44 px.
10. Voice plays only after the first tap, each mode line once, and Curio.stop() cuts speech on mode or case change.

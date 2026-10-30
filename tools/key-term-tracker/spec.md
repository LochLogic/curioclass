# Key Term Tracker

## One idea
A key term is a word an author keeps working on: follow one loaded word (faction in Federalist No. 10, nature in King Lear) stop by stop, decide at each stop whether the author defines it, narrows it, widens it or bends it into a figure, and watch its meaning card grow in layers until you can set the author's meaning beside today's dictionary and see what changed (Madison's faction can be a majority).

## Not like
- word-family-tree (ela 12, explorer, this group and family): where many words came from over centuries. Here one word inside one text, and how the author shapes it.
- context-roots-dictionary (ela 6-8, puzzle, family, not specced): cracks unfamiliar academic words by context, roots, then dictionary. Here that is the side tool (Word help); the main work is tracking a term's meaning across a whole text.
- founding-words-explorer (ela 9, explorer, founding-docs family, not specced): plain-English layers over founding documents, section by section. Here only one term is followed, and the second text is a play.
- idea-threads (ela 9-12, explorer, not specced): threads a central idea through sentences that develop it. Here the unit is one word and its forms, classified by what the author does to its meaning.
- theme-ledger (ela 9-12, data, spec): weighs passages for two themes in short stories. Here no weights or chart: the output is a layered definition.
- argument-map (ela 12, builder, spec): the structure of Federalist No. 51. Here Federalist No. 10, and vocabulary, not structure.

## Who and how
- Grades 9 to 12 ELA. Module: Key Terms and Academic Vocabulary (Language).
- Topic line: "how authors define key terms".
- Driver: students on laptops, alone or in pairs. 30 to 45 minutes per text.
- Standards: L.9-10.4 (unknown and multiple-meaning words: 4a context, 4b patterns of word changes, 4c reference materials for pronunciation, part of speech and etymology, 4d verifying): Word help, with its Forms row and the entry's respelling and etymology. L.9-10.6 and L.11-12.6 (acquire and use general academic and domain-specific words, and gather vocabulary knowledge independently): the Word bank, **My own word** (the student picks any word in the text to work up) and Use it. RI.11-12.4 (how an author uses and refines the meaning of a key term over a text; the standard's own example is Madison's faction in Federalist No. 10): the Federalist track and its meaning card. RL.11-12.4 (word meanings in a literary text, including figurative and connotative meanings and words with multiple meanings; the standard names Shakespeare): the King Lear track.
- Content notes (a line on the tool page and in the teacher notes): "The Federalist context card names who could not vote in 1787 and that Madison enslaved people. The King Lear track includes a father who calls daughters 'unnatural hags' and a son born outside marriage."
- Grade setting in the panel: **9-10** opens Federalist No. 10 with Word help first and the move chips explained; **11-12** opens either text and adds the Then and now comparison and the Unnamed stops challenge. Both texts are open at either setting.
- tool.json: driver "students", minutes "30-45", modes ["Track", "Meaning card", "Word help", "Use it"], grades_label "Grades 9-12". Kit starter plus `kit:wordlab`.

## Screens and modes
Header: title "Key Term Tracker", small line "One word, every stop."; text picker **Federalist No. 10: faction** / **King Lear: nature**, each button with its painted picture (Art); mode buttons **Track** (opens first), **Meaning card**, **Word help**, **Use it**; Motion, Sound, Read. Panel: `#hint`, the stop counter ("Stops logged: 6 of 13"), the move key, the Word bank count, **About this text** (context card), **Clear this text** (asks Yes / No).

### Track (opens first)
Focus: the text with its highlighted stops (left, the widest column) and the open stop card beside it.
- Left: the text as an excerpt, stop passages in order with "[text skipped]" markers between them and a location label on each (Federalist: sentence number in the edition; Lear: act, scene and the speaker). Every form of the term is highlighted like a highlighter stroke (faction, factions, factious; nature, nature's, natural, unnatural) and is a stop.
- Hard words are dotted-underlined; tapping one opens Word help for it in a side sheet.
- Tap a stop: the stop card opens on the right with:
  - **What does the author do with the word here?** chips: **Defines** (says what it means), **Narrows** (limits it to part of what it meant), **Widens** (stretches it to cover more), **Bends** (uses it as a figure or shifts its feeling), **Uses** (uses it plainly, nothing new). One chip, or two at the 11-12 setting.
  - **What it means here**: a short box in the student's words.
  - **Feeling**: a three-step dial, **negative / neutral / positive**, for the word's connotation at this stop.
  - **Log stop** adds the stop to the meaning card as a new layer.
- **One reading** (after a stop is logged): shows the tool's move and a one-line note for that stop (Content), with "One reader's call. Yours can differ."
- **Unnamed stops** (11-12): the line "Madison sometimes talks about faction without the word. Find 2 places." Tapping a sentence that isn't a stop lets the student **Mark as unnamed stop**; the tool confirms the two in Content ("Found: the idea without the word") and leaves any others as the student's own.

### Meaning card
Focus: the meaning card, centered and the biggest thing on screen.
- The term's card grows from the bottom up: each logged stop is a layer showing its location, the move chip's glyph, the student's words and the feeling dial. Layers are colored by move and carry its glyph and name.
- **Today's dictionary** sits as a separate tab on the card (Content), and at 11-12 **Then and now** sets the student's final meaning beside it in two columns with prompts: "What does the author's meaning include that today's doesn't?" and "What does today's include that the author's doesn't?"
- **My definition**: the student writes the author's meaning of the term in one or two sentences; a check lists which logged layers the definition draws on (the student ticks them), so the definition is built from the stops.
- **Feeling line**: a small strip across the card showing the feeling dial at each stop in order, so a shift in connotation shows as a change in the strip (with words: "negative at 1 to 5, mixed at 6").

### Word help
Focus: the current word's step card, under the painted magnifier (Art).
- The hard words of the current text (Content), each a row. Tapping one runs the word-lab steps in order: **Context** (the student's guess from the sentence), **Parts** (split into parts with meanings, when it has them), **Dictionary** (the entry: respelling, part of speech, etymology line, meaning in this text, today's meaning when different, source line), **Forms** (the word's family with the changing part lit, Content: "adverse, adversity, adversary"), **Verify** (the student ticks "My guess fit" or "I needed the dictionary").
- **Add to Word bank** puts the word in the student's bank. The Strategy log shows which step cracked each word.
- **My own word**: the student taps any word in the text and adds it to the list. Its steps run the same way, except Dictionary has no built-in entry: the card says "Look it up in a print or online dictionary, then write its part of speech and the meaning that fits this sentence," with boxes for both. The word can go to the Word bank like any other.

### Use it
Focus: the two sentence boxes.
- Two sentence boxes for the term: "Use faction the way Madison does." and "Use faction the way people use it today." (Lear: "Use nature the way Edmund means it." and "Use nature the way Lear means it in 'The offices of nature'.")
- Word bank practice: for each banked word, a box "Your own sentence" with the word's meaning shown above it. A small count: "5 words used in your own sentences".

## Content
### Federalist No. 10 (Madison, as Publius, 1787): term faction
- Edition: The Federalist Papers, Project Gutenberg eBook #1404 (Sources). Text printed exactly, including the edition's "adversed" (glossed in Word help). Sentence numbers below count from the essay's first sentence.
- Context card (About this text): "Published in a New York newspaper, the Daily Advertiser, on November 22, 1787, under the pen name Publius, to argue that New York should ratify the Constitution. Madison wrote it. In 1787 only some men could vote: most states required property or tax payment, and women, enslaved people and most Native people had no vote. Madison enslaved people at Montpelier, his Virginia plantation. When Madison worries about 'the rights of other citizens', ask who counted as a citizen."
- Stops (location; text; one reading's move and note):
  1. s1: "AMONG the numerous advantages promised by a well constructed Union, none deserves to be more accurately developed than its tendency to break and control the violence of faction." Uses. "Names the problem and pairs it with violence from the first sentence."
  2. s9: "These must be chiefly, if not wholly, effects of the unsteadiness and injustice with which a factious spirit has tainted our public administrations." Bends. "Factious spirit 'taints': faction as a stain or poison."
  3. s10: "By a faction, I understand a number of citizens, whether amounting to a majority or a minority of the whole, who are united and actuated by some common impulse of passion, or of interest, adversed to the rights of other citizens, or to the permanent and aggregate interests of the community." Defines. "The key stop: size doesn't matter (majority or minority); what makes a faction is being united against others' rights or the common good."
  4. s11: "There are two methods of curing the mischiefs of faction: the one, by removing its causes; the other, by controlling its effects." Bends. "Faction as a disease to be cured."
  5. s14: "Liberty is to faction what air is to fire, an aliment without which it instantly expires." Bends. "Faction as fire, liberty as its air: you can't remove one without the other."
  6. s22: "The latent causes of faction are thus sown in the nature of man; and we see them everywhere brought into different degrees of activity, according to the different circumstances of civil society." Widens. "Faction is part of human nature, everywhere."
  7. s25: "But the most common and durable source of factions has been the various and unequal distribution of property." Narrows. "Names its main source: unequal property."
  8. s36: "Yet the parties are, and must be, themselves the judges; and the most numerous party, or, in other words, the most powerful faction must be expected to prevail." Widens. "A party in power can be a faction too."
  9. s43: "The inference to which we are brought is, that the CAUSES of faction cannot be removed, and that relief is only to be sought in the means of controlling its EFFECTS." Narrows. "The task narrows to controlling effects."
  10. s44: "If a faction consists of less than a majority, relief is supplied by the republican principle, which enables the majority to defeat its sinister views by regular vote." Narrows. "A minority faction is easy: outvote it."
  11. s46: "When a majority is included in a faction, the form of popular government, on the other hand, enables it to sacrifice to its ruling passion or interest both the public good and the rights of other citizens." Narrows. "The real danger is a majority faction."
  12. s82: "The influence of factious leaders may kindle a flame within their particular States, but will be unable to spread a general conflagration through the other States." Bends. "The fire figure returns: a large Union keeps the fire local."
  13. s83: "A religious sect may degenerate into a political faction in a part of the Confederacy; but the variety of sects dispersed over the entire face of it must secure the national councils against any danger from that source." Bends. "'Degenerate into': a faction is a group gone bad."
- Unnamed stops (11-12): s73: "Extend the sphere, and you take in a greater variety of parties and interests; you make it less probable that a majority of the whole will have a common motive to invade the rights of other citizens; or if such a common motive exists, it will be more difficult for all who feel it to discover their own strength, and to act in unison with each other." and s85: "In the extent and proper structure of the Union, therefore, we behold a republican remedy for the diseases most incident to republican government."
- Sentence numbers: the builder recounts them from the edition (the Avalon split used for this spec gave s1, s9, s10, s11, s14, s22, s25, s36, s43, s44, s46, s82, s83, s73, s85 with the title and "To the People of the State of New York:" not counted; adjust to the edition and keep the order).
- Today's dictionary (paraphrase, Merriam-Webster): "a group within a larger group, often one that quarrels or works for its own interests." At 11-12, Johnson's Dictionary (1755) entry for faction, quoted only if confirmed at build (Sources).
- Forms rows (L.9-10.4b): faction, factions, factious, factional; adverse, adversity, adversary (the edition's adversed); act, actuate, actuated, action; aggregate, aggregation; infer, inference, inferential; nature, natural, unnatural, naturally; merit, meritorious; superfluous, superfluity. Respellings for every hard word come from Merriam-Webster at build.
- Hard words (Word help): actuated (moved to act; act + -uate); aggregate (taken all together; ad- "to" + grex "flock"); adversed (an older form of adverse, opposed; ad- "toward" + vertere "to turn"); mischiefs (harms; stronger then than today's playful sense); aliment (food, nourishment; Latin alere "to nourish"); latent (present but hidden; Latin latere "to lie hidden"); sinister (harmful, evil; Latin for "left"); inference (a conclusion reached by reasoning; in- + ferre "to carry"); sphere (here, the territory a government covers); conflagration (a huge fire; con- + flagrare "to burn"); factious (inclined to form factions; causing division).

### King Lear (Shakespeare): term nature (and natural, unnatural)
- Edition: The Tragedy of King Lear, Project Gutenberg eBook #1532 (Sources). The edition's em dashes are shown as "--". Only the stop passages are printed; Edmund's stop stops before the lines where he repeats the play's word for a child born outside marriage, so that word never appears on screen.
- Context card: "Lear, king of Britain, divides his kingdom among his daughters by how much they say they love him. Edmund, the Earl of Gloucester's son born outside marriage, plots against his brother. Everyone in the play argues about what is 'natural'."
- Stops (act.scene, speaker; text; one reading's move and note):
  1. 1.1 Lear: "Which of you shall we say doth love us most? / That we our largest bounty may extend / Where nature doth with merit challenge." Uses. "Nature here is the bond of parent and child, set beside merit."
  2. 1.2 Edmund: "Thou, Nature, art my goddess; to thy law / My services are bound. Wherefore should I / Stand in the plague of custom, and permit / The curiosity of nations to deprive me?" Bends. "Nature as a goddess and raw force, against custom and law."
  3. 1.2 Gloucester: "though the wisdom of Nature can reason it thus and thus, yet nature finds itself scourged by the sequent effects. Love cools, friendship falls off, brothers divide" and "the King falls from bias of nature; there's father against child." Widens. "Nature as the order of the world, which family breakups shake."
  4. 1.4 Lear: "O most small fault, / How ugly didst thou in Cordelia show! / Which, like an engine, wrench'd my frame of nature / From the fix'd place" Bends. "His own nature as a structure, wrenched loose."
  5. 1.4 Lear: "Hear, nature, hear; dear goddess, hear! / Suspend thy purpose, if thou didst intend / To make this creature fruitful!" Bends. "Lear calls Nature a goddess too, the same move as Edmund."
  6. 2.1 Gloucester (to Edmund): "and of my land, / Loyal and natural boy, I'll work the means / To make thee capable." Bends. "Two meanings at once: 'natural' as a loving son should be, and 'natural' as born outside marriage. Gloucester means the first; the audience hears both."
  7. 2.4 Lear: "we are not ourselves / When nature, being oppress'd, commands the mind / To suffer with the body" Narrows. "Nature as the body and its health."
  8. 2.4 Lear: "Thou better know'st / The offices of nature, bond of childhood, / Effects of courtesy, dues of gratitude" Defines. "Nature as the duties a child owes a parent."
  9. 2.4 Lear: "O, reason not the need: our basest beggars / Are in the poorest thing superfluous: / Allow not nature more than nature needs, / Man's life is cheap as beast's." Narrows. "Nature as bare need; people need more than that to be human."
  10. 2.4 Lear: "No, you unnatural hags," Widens. "The opposite form: daughters who break the bond are 'unnatural'."
  11. 3.6 Lear: "Then let them anatomize Regan; see what breeds about her heart. Is there any cause in nature that makes these hard hearts?" Widens. "Nature as physical cause, something you could cut open and study."
  12. 4.2 Albany: "That nature which contemns its origin / Cannot be bordered certain in itself." Defines. "Nature as character, rooted in where you come from." These lines are in the 1608 Quarto and missing from the Folio; if the edition used lacks them, this stop becomes 1.1 Lear on Cordelia, "a wretch whom nature is asham'd / Almost t' acknowledge hers." Bends. "Nature as a mother who disowns her child: Lear's anger, put in nature's mouth."
  13. 4.7 Cordelia: "O you kind gods, / Cure this great breach in his abused nature!" Bends. "Nature as a mind that can be broken and healed."
- Today's dictionary (paraphrase, Merriam-Webster): several senses: "the physical world and its forces", "the basic character of a person or thing", "the body's needs and functions".
- Meaning card prompt for Lear (RL.11-12.4, impact on tone): "The word keeps changing hands: a bond, a goddess, a body, a cause. What does that fight over one word do to the feeling of the play?"
- Hard words (Word help, meanings in this text written for Curio Class and checked against the Folger notes): capable (here, legally able to inherit), bounty (generous gifts), merit (deserving), custom (tradition, law), curiosity (fussy distinctions), sequent (following), engine (a machine, or a rack for torture), offices (duties), superfluous (more than needed), anatomize (dissect), contemns (scorns), bordered (kept within limits).

## Interactions in detail
- Stops are word ranges in the edition's text; the highlighter marks every listed form. A stop can be logged, edited and re-logged; the meaning card keeps one layer per stop, in text order.
- One reading appears only after the student logs that stop. With two chips allowed at 11-12, a match on either chip shows "Same call".
- Unnamed stops: only the two listed sentences confirm; the student may mark others, kept as "your own" layers.
- Lear has 13 stops after the 2.1 stop is added, matching Federalist No. 10's 13, so the counter reads "of 13" for both.
- Word help uses the word-lab engine's Split, Lookup and Strategy log; the dictionary entry shows "meaning here" and "today's meaning" when they differ (mischiefs, sinister, engine, offices, curiosity).
- Nothing plays on its own. A logged layer slides onto the card over 300 ms (instant with Motion off); a tap during the slide acts at once and the layer lands where it belongs.
- Storage per text in localStorage `key-term-tracker:v1` (try/catch): logged stops, unnamed stops, definition, Then and now, Word bank, sentences, strategy log. Clear this text asks first.
- Sizes: at 1000 px and up, text and stop card side by side; at 760 and below the stop card and Word help open as bottom sheets. At 680x425 a stop passage and its card are visible together. At 375 the meaning card shows layers as a scrolling list. No horizontal scroll.

## Look
- Accent `--brand #7a4b00` (dark highlighter amber: header rule, active mode, Log stop, the meaning card's frame). Own light `:root`, a cool index-card desk (changed in revision so it no longer shares editors-in-the-margin's warm paper): `--paper #f3f5f8`, `--panel #ffffff`, `--ink #1f1b16`, `--muted #5a5247`, `--line #dde2e8`, `--btn #7a4b00`, `--head-ink #ffffff`, `--focus #1a5fa0`. Term highlight `#ffe27a` behind ink text (a highlighter stroke); hard words dotted underline in `--muted`.
- Move layers (glyph, name and color): Defines ■ `#1a5fa0`, Narrows ▼ `#2f6b2f`, Widens ▲ `#7a3fa0`, Bends ~ `#a33a2a`, Uses ● `#5a5247`.
- Contrast (WCAG 2.1, recomputed 2026-10-29 on the new paper): brand on paper 6.78:1, on panel 7.41:1; white on brand 7.41:1; ink on paper 15.68:1; muted on paper 7.04:1; focus on paper 6.03:1; ink on the highlight 13.38:1; move colors on panel: Defines 6.59, Narrows 6.43, Widens 6.89, Bends 6.57, Uses 7.68 (on paper each above 5.8).
- Different from ELA 9-12 neighbors (theme-ledger wine, research-notebook blue, source-portfolio green, all light) and this group (editors-in-the-margin red on warm paper, personal-essay-studio rose, socratic-seminar-board teal, all light; founding-words-explorer iron-gall brown on parchment, dE 22 from this accent and a much warmer paper).

## Art
Three painted images, all local FLUX (`scripts/localart.py`), people: false. The texts and the meaning card are the point; the paintings mark which text is open and where Word help lives.
- `pick-federalist`: "A stack of folded 1780s newspapers tied with twine on a wooden windowsill, plain blank pages, winter light". 4:3; cutout no; people: false. On the Federalist No. 10 picker button (about 120 px wide) and at the top of its About this text card (about 280 px).
- `pick-lear`: "A gold crown lying in wet heath grass under a dark storm sky, lightning far off on the horizon". 4:3; cutout no; people: false. On the King Lear picker button and its About this text card.
- `magnifier`: "A brass magnifying glass resting on a blank white index card, soft studio light, plain light backdrop". 1:1; cutout yes; people: false. Word help's header (64 px) and the Word bank count in the panel (24 px).
Drawn in code: the highlighter strokes, stop cards, move glyphs, the growing meaning card, the feeling line and the Forms rows.

## Voice
Bank voice `curious-librarian`, style "Say curiously and warmly, like a school librarian who loves a good word." Not used by this group, any neighbor or another spec in this batch; the other 9-12 ELA user, ambiguity-lab (grade 12), is not a neighbor. The kit voice queue (`Curio.voice`), `scope: () => state.mode + ':' + state.text`. The texts are never voiced.
- w-track (how, Track welcome; stale once a stop card opens): "Every highlighted word is a stop. Tap one, choose what the author does with it, and tap Log stop."
- moves (how, first stop card opened; stale once a chip is chosen): "Tap Defines, Narrows, Widens, Bends or Uses. Then write what it means here."
- reading (how, first One reading shown; stale when the next stop opens): "That's one reader's call. Yours can differ."
- unnamed (how, first Unnamed stops prompt at 11-12; stale once a sentence is marked): "Look for the idea without the word. Tap a sentence, then tap Mark as unnamed stop."
- w-card (how, Meaning card welcome; stale once My definition has text): "Each layer is a stop you logged. Write your definition in the My definition box."
- w-help (how, Word help welcome; stale once a word is opened): "Tap a word. Type your guess from the sentence first, then try Parts, then Dictionary."
- w-use (how, Use it welcome; stale once a box has text): "Write the word two ways in the two boxes: the author's way and today's."
- majority (event, each time the student logs Federalist stop 3; stale on the next stop): "Notice: a faction can be a majority."

## Family engine
`kit/wordlab.js`, the word-lab family engine, described in full in tools/word-family-tree/spec.md (siblings word-lab, root-detective-cards, glossary-makers, context-roots-dictionary, key-term-tracker, word-family-tree). This tool feeds it: word records for the term's forms and for each hard word (parts where they exist, the meaning-here and today's senses, sources); Card view for the growing meaning card, with each logged stop as a layer `{loc, move, text, feeling}`; Split, Lookup, Strategy log and Guess and verify for Word help. It does not use Tree view or Build.

## Sources
- Standards: CCSS ELA L.9-10.4 and L.9-10.6, https://www.thecorestandards.org/ELA-Literacy/L/9-10/; RL.11-12.4 and RI.11-12.4, https://www.thecorestandards.org/ELA-Literacy/RL/11-12/ and https://www.thecorestandards.org/ELA-Literacy/RI/11-12/; L.11-12.6, https://www.thecorestandards.org/ELA-Literacy/L/11-12/.
- Federalist No. 10 text: The Federalist Papers, Project Gutenberg eBook #1404, https://www.gutenberg.org/ebooks/1404 (header: "From the Daily Advertiser. Thursday, November 22, 1787." and "MADISON"); checked against the Avalon Project, https://avalon.law.yale.edu/18th_century/fed10.asp (Avalon prints "wellconstructed"; Gutenberg "well constructed"; both print "adversed").
- King Lear text: Project Gutenberg eBook #1532, https://www.gutenberg.org/ebooks/1532 (stop lines quoted from it; act and scene from its headings). Glosses checked against the Folger Shakespeare edition notes, https://www.folger.edu/explore/shakespeares-works/king-lear/.
- Voting in 1787 (property or tax requirements; women, enslaved people and most Native people excluded): National Archives or Library of Congress page on voting rights in the early republic; confirm at build, and if no page states it plainly, keep only "In 1787 only some men could vote."
- Madison enslaved people at Montpelier: James Madison's Montpelier, https://www.montpelier.org/ (confirm the page at build).
- Today's senses of faction and nature (paraphrased): Merriam-Webster.com Dictionary.
- Johnson's Dictionary (1755) entry for faction: https://johnsonsdictionaryonline.com/ (shown at 11-12 only if the entry is confirmed there).
- Word parts for the Federalist hard words: Merriam-Webster etymologies.
- Checks run 2026-10-29: Federalist stops listed 13, Lear stops listed 13 (with 2.1), unnamed stops 2, so the counter reads "of 13" on both; contrast ratios in Look recomputed in Python for the new paper.

## Done when
- Focus: at 1366x768 and 680x425 in Track, the text with its highlighted stops is the largest thing on screen and an open stop card sits beside it; in Meaning card, the card is.
- Every listed form of the term is highlighted in both texts and every stop opens a card; the stop texts match the editions.
- Logging a stop adds a layer to the meaning card in text order with its glyph, words and feeling; a tap during the layer's slide acts at once.
- One reading appears only after logging and shows the Content move and note.
- At 11-12 the two Unnamed stops in Federalist No. 10 confirm; other marked sentences stay as the student's own.
- Logging Federalist stop 3 speaks the majority line each time it is logged.
- Word help runs Context, Parts (where parts exist), Dictionary (with respelling and etymology), Forms, Verify in order and logs the cracking step; My own word works for any tapped word with the look-it-up boxes; Add to Word bank and Use it work.
- The Lear 2.1 stop shows its double-meaning note; the stop counter reads "of 13" on both texts.
- The Federalist context card names who could not vote and that Madison enslaved people.
- The picker buttons and context cards show their paintings; no people appear; no voice line names a control that is hidden or disabled.
- Work survives a reload; Clear this text asks first.
- At 375 and 760 wide the stop card opens as a bottom sheet with no horizontal scroll; at 680x425 a passage and its card are visible together.

## Open questions
None. Settled:
- The Madison and voting lines stay as written: founding documents are taught plainly, including who they left out (wave rule, BASELINE rule 5); a Content notes line covers the parent-preview concern (BASELINE specific call).
- Lear: only stop passages are printed, and Edmund's stop ends before the word "bastard" appears, so no on-screen use (rule 6). "Unnatural hags" is Shakespeare's insult, not a slur or expletive, and stays, named in Content notes.
- No third "liberty" track: liberty appears in only three sentences of Federalist No. 10, so a track would be thin (rule 2). Liberty is met at faction stop 5 (air to fire).

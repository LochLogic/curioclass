# Thesis Workshop

## One idea
A thesis is a promise about the whole text: build one from a topic, a move the author makes and a meaning, and the tool lights every passage your promise would oblige you to explain, so you can see at once when it is too broad (half the story lights up), too narrow (one line), only a summary (nobody could disagree) or contradicted by lines you hoped no one would notice, and tune it until it lights a handful of passages you can prove it with.

## Not like
- theme-ledger (ela 9): logs evidence for a stated theme across a story and charts it. Here the claim itself is the thing being built and tested; evidence comes second.
- argument-builder-pro (ela 9): outlines an argument about a civic question with counterclaims. Here the claim is about a literary text and the test is scope and fit against the text.
- character-web (ela 9): motivations pulling a character through a novel. Here the subject is the analyst's claim, not a character.
- question-sharpener (ela 12): narrows a research question by its cost. Here the thing narrowed is a claim, and the measure is which passages it covers.
- argument-map (ela 12): rebuilds someone else's argument. Here the student makes the claim.
- fallacy-field-guide (ela 10): faulty reasoning in everyday arguments. Here reasoning is about a text's evidence.

## Who and how
- Grade 10 ELA, module Literary Analysis (Writing): "Analysis essays supported by textual evidence".
- Driver: students on laptops, alone or in pairs. A teacher can project Build for the first text. 30 to 45 minutes.
- Standards: W.9-10.2 (write informative or explanatory texts, including a clear thesis and well-chosen evidence): Build and Draft. W.9-10.9 (draw evidence from literary texts to support analysis): Prove. RL.9-10.1 (cite strong and thorough textual evidence for what the text says explicitly and what can be inferred): Prove's because check and the contradiction readout.
- tool.json: driver "students", minutes "30-45", modes ["Build", "Prove", "Draft"], grades_label "Grade 10". Kit starter; light theme with its own `:root`.

## Screens and modes
Header: title "Thesis Workshop", small line "A thesis is a promise."; text picker **The Open Window** (Saki) / **The Road Not Taken** (Frost); mode buttons **Build** (opens first), **Prove**, **Draft**; Motion, Sound, Read. Layout: the text in a left column (about 45 percent) with passage ids in the margin; the workbench on the right with `#hint`. At 760 wide and below the text is a tab beside the bench (**Text** / **Bench**), and passages lit by the thesis show a count on the Text tab.

### Build (opens first)
- Three chip rows on the bench: **Topic**, **Move** (what the author does), **Meaning** (what it adds up to), from Content. Each row also has **Any** (a deliberately loose choice). The chosen chips form a sentence in a frame: "In [text], [author] uses [move] with [topic] to show that [meaning]." A **My own words** box lets the student rewrite that sentence freely; the test still runs on the chips.
- **Promise light**: as soon as Topic and Move are chosen, every passage tagged with both glows in the text (outline plus a small lamp glyph, not only color). Meaning adds a second mark: lit passages that fit the meaning get a check glyph; lit passages that cut against it get a cross glyph and a warn tint.
- **Promise meter** (four readouts, each word plus glyph):
  - **Arguable**: "Yes, a reader could disagree" (shows the meaning's counter-reading from Content), or "Summary: this is what happens, not what it means" for a summary chip.
  - **Scope**: lit count: 0 to 1 "Too narrow: one line can't carry an essay"; 2 "Thin"; 3 to 8 "Workable"; 9 or more "Too broad: you would have to explain most of the text".
  - **Fit**: "Meaning fits 5 of 6 lit passages". Under half: "This meaning doesn't fit most of your passages. Change one chip."
  - **Against you**: "2 lit passages cut against this" (or "None found"), each a link that scrolls to the passage.
- **Save this thesis** stores it (up to five per text) in a list under the bench with its meter readings, so students can compare drafts. **Use this one** carries it to Prove.

### Prove
- The chosen thesis at the top. The lit passages are listed; the student picks three as evidence (taps **Use as evidence**). Each becomes a card with the quotation and a **Because** box: "This shows [meaning] because ..."
- **Because check** per card, two nudges, never a grade: "Names words from the quote" (looks for at least one word of four or more letters from the passage) and "Links to your meaning" (looks for one of the meaning's keywords in Content). Each shows a check or an open circle with the word.
- If any lit passage is marked against the thesis, a fourth card **Answer the line against you** appears: "Some readers will point to [passage]. Here is why it doesn't sink my claim: ..." It can be left empty, but Draft notes it.
- **Swap evidence** returns a card to the list.

### Draft
- Assembles a paragraph from the thesis sentence, the three evidence cards (quotation in quotation marks with its passage id) and the answer card, in order, into one editable text area.
- **Copy** puts the paragraph on the clipboard. **Clear my work** (confirm) wipes this tool's storage. Nothing leaves the browser.
- A short checklist beside it, read from the state: thesis meter Workable or better, three because lines with both checks, the line against you answered.

## Content
Texts verbatim: Saki, "The Open Window", Beasts and Super-Beasts (John Lane, 1914), Project Gutenberg #269; Robert Frost, "The Road Not Taken", Mountain Interval (Henry Holt, 1916), Project Gutenberg #29345. The Gutenberg "--" in Frost's line 18 is kept as "--" (group open question). Passages are character ranges in the full text; ids and openings below.

**The Open Window: passages** (id, opening words; topic tags V Vera, W the window, F Framton, A the aunt; move tags P planted detail, I narrator's irony, H hiding things from the reader, S story inside the story, E the ending; meaning tags)
- W1 "My aunt will be down presently, Mr. Nuttel," ... "put up with me." V; I; N1
- W2 "Framton Nuttel endeavoured to say the correct something" (to "undergoing.") F A; I; N2
- W3 "I know how it will be," his sister had said (to "quite nice.") F; I; N2
- W4 "Do you know many of the people round here?" (to "Only her name and address,") V F; H; N1 N3
- W5 "An undefinable something about the room seemed to suggest masculine habitation." F A; P H; N3
- W6 "Her great tragedy happened just three years ago," V; S; N1
- W7 "You may wonder why we keep that window wide open on an October afternoon," V W; S P; N1
- W8 "Out through that window, three years ago to a day" (to "That was the dreadful part of it.") V W; S; N1 N3
- W9 "Here the child's voice lost its self-possessed note and became falteringly human." V; I H; N1
- W10 "Poor aunt always thinks that they will come back some day" (to "got on her nerves.") V; P S; N1
- W11 "Do you know, sometimes on still, quiet evenings like this" (to "a little shudder.") V W; S H; N1 N3
- W12 "I hope Vera has been amusing you?" ... "She has been very interesting," V A F; I; N2
- W13 "I hope you don't mind the open window," (to "isn't it?") A W; H; N3
- W14 "To Framton it was all purely horrible." (to "the lawn beyond.") F A W; H I; N3
- W15 "It was certainly an unfortunate coincidence that he should have paid his visit on this tragic anniversary." F; I H; N3
- W16 "The doctors agree in ordering me complete rest" (to "not so much in agreement,") F; I; N2
- W17 "No?" said Mrs. Sappleton, in a voice which only replaced a yawn at the last moment. A; I; N2
- W18 "The child was staring out through the open window with dazed horror in her eyes." V W; H; N1 N3
- W19 "In the deepening twilight three figures" (to "why do you bound?") W; P; N3
- W20 "Framton grabbed wildly at his stick and hat" (to "imminent collision.") F; I; N3
- W21 "A most extraordinary man, a Mr. Nuttel," (to "seen a ghost.") A F; I; N2
- W22 "I expect it was the spaniel," said the niece calmly (to "lose their nerve.") V; S E; N1
- W23 "Romance at short notice was her speciality." V; E I; N1
Counts: V 12, W 7, F 10, A 7; P 4, I 12, H 8, S 6, E 2. Examples: Vera + Story inside the story lights 6 (W6, W7, W8, W10, W11, W22); Window + Planted detail lights 2; Framton + Irony lights 8; Any + Any lights 23.

**The Open Window: chips**
- Topic: Vera, The open window, Framton, Mrs. Sappleton, Any.
- Move: Planted details, The narrator's irony, Hiding things from the reader, A story inside the story, The last line, Any.
- Meaning:
  - N1 "a well-told story can beat the truth." Counter-reading: "Vera is simply cruel; the story is about a bully, not about stories." Keywords: story, stories, tell, telling, believe, invent, romance, imagination.
  - N2 "good manners can hide boredom and unkindness." Counter: "The adults are only awkward, not unkind." Keywords: polite, manners, bored, boredom, rude, unkind, pretend.
  - N3 "people believe what fits what they already fear." Counter: "Anyone would have believed Vera; Framton's nerves don't matter." Keywords: fear, nerves, believe, afraid, panic, expect.
  - N0 (summary) "Vera tricks Framton with a made-up story." Arguable reads Summary. No against-you tags in this text: the meter says "None found" and the panel asks the student to hunt for one in their own words.

**The Road Not Taken: passages** (R1 to R20 are the poem's twenty lines in order; topic tags C the choice, R the roads, T telling it later; move tags Q the roads described as equal, G regret words, F future telling, S the ambiguous sigh and difference, D the repeated line with its dash; meaning tags; "x" marks against)
- R1 "Two roads diverged in a yellow wood," R
- R2 "And sorry I could not travel both" C; G; N2
- R3 "And be one traveler, long I stood" C; N2
- R4 "And looked down one as far as I could" R C; N2
- R5 "To where it bent in the undergrowth;" R; N2
- R6 "Then took the other, as just as fair," R C; Q; N1
- R7 "And having perhaps the better claim," R C; Q; N1
- R8 "Because it was grassy and wanted wear;" R; N3
- R9 "Though as for that the passing there" R; Q; N1, x N3
- R10 "Had worn them really about the same," R; Q; N1, x N3
- R11 "And both that morning equally lay" R; Q; N1, x N3
- R12 "In leaves no step had trodden black." R; Q; N1, x N3
- R13 "Oh, I kept the first for another day!" C; G; N2
- R14 "Yet knowing how way leads on to way," C; G; N2
- R15 "I doubted if I should ever come back." C; G; N2
- R16 "I shall be telling this with a sigh" T; F S; N1 N2
- R17 "Somewhere ages and ages hence:" T; F; N1
- R18 "Two roads diverged in a wood, and I--" T R; F D; N1
- R19 "I took the one less traveled by," T C R; F; N1 N3
- R20 "And that has made all the difference." T C; F S; N1 N3
Counts: R 12, C 10, T 5; Q 6, G 4, F 5, S 2, D 1.

**The Road Not Taken: chips**
- Topic: The choice, The two roads, Telling it later, Any.
- Move: Roads described as equal, Regret words, Future telling, The sigh and "difference", The repeated line, Any.
- Meaning:
  - N1 "we give our choices their meaning later, in the stories we tell about them." Counter: "The speaker really did choose the better road." Keywords: story, tell, telling, later, meaning, remember, explain.
  - N2 "every choice closes off other lives, and the speaker knows it." Counter: "The speaker is content; there is no real regret." Keywords: regret, sorry, lose, loss, never, other, both.
  - N3 (the popular reading) "taking the road less traveled made the speaker's life better." Counter: "The roads were the same, so the choice could not be bold." Keywords: different, better, bold, unusual, nonconform.
  - N0 (summary) "The speaker chooses one of two roads."
- With Topic The two roads and Move Roads described as equal, N3 shows "Against you: 4" (R9 to R12); that is the poem's lesson and the panel says so once: "The popular reading has to get past these four lines."

**Context cards**: Saki was the pen name of H. H. Munro; "The Open Window" is in Beasts and Super-Beasts (1914). "The Road Not Taken" first appeared in the Atlantic Monthly, August 1915, and opens Mountain Interval (1916).

## Interactions in detail
- Light updates on every chip change, with a 150 ms fade (none with Motion off). The text column scrolls to the first lit passage only when the student presses **Show me**, never on its own.
- Any + Any lights everything and the meter says "Too broad" for Scope and "Pick a meaning" for Fit.
- Choosing N0 sets Arguable to Summary and greys Fit; Prove is still allowed, with a note "Most teachers would ask for a claim, not a summary."
- Free text in My own words does not change the light; if it no longer mentions the chosen topic word, the panel says "Your sentence and your chips have drifted apart."
- Because check is case-insensitive and ignores punctuation; words like "that", "this", "with" (a short stop list in Content of the build) do not count as quote words.
- Saved theses: up to five per text; a sixth asks which to replace.
- localStorage key `tw.v1` (try/catch). Without storage the tool works for the session and says so.
- At 680 x 425 the chip rows wrap to two lines and the meter collapses to four icons with words under them; all stay visible with the text.

## Look
Light and cool, a writing room. Paper #f4f4fa, panel #ffffff, ink #1c1d2b, muted #555870. Accent brand #5b63a6 (slate indigo), white text on brand. Chip rows have their own ink: Topic #0b6e75, Move #8a4b00, Meaning #8a2b6e; each row also has its label word. Lit passages: brand outline plus lamp glyph; against-you: #b02a1a outline plus cross glyph. Focus ring #b3541e.
Contrast (WCAG): brand on white 5.56, on paper 5.07; white on brand 5.56; ink on paper 15.21; muted on paper 6.35; Topic 5.47, Move 6.21, Meaning 7.23, against #b02a1a 6.0 on paper; focus 4.56 on paper (non-text, over 3). Nearest catalog accent: animal-moves #1f6fb2 at dE 15.1.

## Art
none: drawn in code (lamp, check and cross glyphs, meter). No people.

## Voice
Bank voice `wise-mentor`, style "Say warmly and plainly, like a writing teacher leaning over your shoulder." Not used by a grade 9-12 ELA neighbor. `Curio.voice`, `scope: () => state.mode + state.text`. Texts are not read aloud by the voice (Read speaks the hint).
- w-build (how): "Pick a topic and a move. Watch which passages light up."
- meaning (how, first time Topic and Move are set): "Now pick a meaning. Checks show where it fits."
- broad (event, Scope reaches Too broad; stale on any chip change): "That promise covers too much. Tighten one chip."
- narrow (event, Scope reaches Too narrow; stale on any chip change): "One line can't carry a whole essay. Loosen one chip."
- against (how, first against-you mark): "A crossed passage cuts against your claim. You'll have to answer it."
- w-prove (how): "Pick three lit passages, then finish each because."
- w-draft (how): "Here is your paragraph. Edit it, then copy it."

## Family engine
none.

## Sources
- Saki, "The Open Window", in Beasts and Super-Beasts (London: John Lane, The Bodley Head, 1914): Project Gutenberg eBook #269, https://www.gutenberg.org/ebooks/269. Saki as H. H. Munro: same eBook's catalog record.
- Robert Frost, "The Road Not Taken", in Mountain Interval (New York: Henry Holt, 1916): Project Gutenberg eBook #29345, https://www.gutenberg.org/ebooks/29345. First printing in the Atlantic Monthly, August 1915, and its place as the collection's first poem: Wikipedia, "The Road Not Taken", checked 2026-10-27.
- Passage tags, chips, meanings and counter-readings: the tool's own analysis; counts above computed from the tags.

## Done when
1. Choosing Vera + A story inside the story lights exactly W6, W7, W8, W10, W11 and W22, and the meter reads Workable.
2. Any + Any lights all 23 passages and reads Too broad; Window + Planted details reads Thin.
3. In Frost, The two roads + Roads described as equal + N3 shows Against you: 4 and links to R9 to R12.
4. Choosing N0 sets Arguable to Summary in both texts.
5. In Prove, a because line with no quote word and no meaning keyword shows two open circles; adding one of each turns both to checks.
6. Draft assembles thesis, three quoted pieces of evidence with ids and the answer card; Copy works; nothing is sent anywhere.
7. Saved theses, evidence and drafts survive a reload; Clear my work wipes them.
8. At 680 x 425 and 375 wide no horizontal scroll; chips and meter visible with the text tab or column.

## Open questions
- thesis-workshop: The Open Window has a mild ghost-story fright (three men believed drowned in a bog). Fine for grade 10?
- thesis-workshop: Show the popular reading of Frost (N3) as a chip, knowing the tool then shows it failing on four lines?

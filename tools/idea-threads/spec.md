# Idea Threads

## One idea
A central idea runs through a speech or essay like a thread through cloth: pick a colored thread and stitch it through every sentence that develops the idea, naming what each stitch does (introduces, explains, gives an example, raises a problem, concludes), and in the 11-12 view a second thread runs through the same text, so wherever both threads pass through one sentence they tie a knot, and a knot only holds when you quote the exact words that carry both ideas at once.

## Not like
- theme-ledger (ela 9-12, spec): two themes in a story, logged as weighted entries and charted by position. Here informational texts, sentence by sentence, and the subject is how the ideas build and interact, with the knots as the point.
- key-term-tracker (ela 9-12, concept): one loaded word followed through a text. Here whole ideas, carried by sentences that may never repeat a word.
- research-notebook (ela 9, spec): threads from the student's sentences back to sources. Here the threads run through someone else's text.
- premise-inspector (ela 11, spec): premises of an argument, stamped against a later speech. Here no premises or verdicts: only what each sentence does for an idea.
- rhetoric-spotter (ela 9, spec): persuasive devices. Here the ideas themselves, not how they persuade.

## Who and how
- Grades 9-12 ELA, module Central Ideas and Their Development: "Cite evidence, determine central ideas, and analyze how ideas and claims unfold and build".
- Standards: RI.9-10.1, RI.9-10.2, RI.9-10.3, RI.9-10.5, RI.11-12.1, RI.11-12.2, RI.11-12.3.
- Driver: students on laptops, alone or in pairs, 20 to 30 minutes per text. A teacher can project a text and stitch it with the class.
- tool.json: driver "students", minutes "20-30", modes ["One thread", "Two threads"], grades_label "Grades 9-12". Kit starter with `kit:theme-912` (dark) and an accent override.

## Screens and modes
Kit frame. Header: "Idea Threads", small line with the text; **Change text**; Motion, Sound, Read. A text picker of three cards (a painted picture, author, title, year, words, one-line setup), and the mode switch **One thread** (labeled "Grades 9-10") | **Two threads** (labeled "Grades 11-12"). The labels are advice; any student can use either.

Focus: the cloth (the text with its threads) is the biggest, central thing in both modes; spools sit pinned above it and readouts in the panel.

**The cloth.** The text, one sentence per line group, on a painted dark linen ground (Art), with a wide right margin. The thread is drawn in the margin: a colored line that runs down the page and loops into the text at each stitched sentence (a small stitch mark at the sentence's left edge), so a long run of stitches looks dense and a gap looks like bare cloth.

**Stitching.** Above the cloth, the thread spool(s), each a painted spool (Art) with the thread's name in code; tap a spool (or press 1 or 2) to make its thread active. Each thread gets a name the student writes (up to 40 characters, for example "security") with a suggested starter from ours. Tap a sentence with a thread active: a painted needle (Art) dips into the sentence's left edge, and a stitch card asks **What does this sentence do for the idea?** with five chips: **Introduces**, **Explains**, **Gives an example**, **Raises a problem**, **Concludes**. Tap again to unstitch.

**Knots** (Two threads only). When both threads pass through the same sentence, a knot icon appears and the knot card opens: **Quote the words that carry both ideas** (the student selects a span inside the sentence; the span must be inside that sentence and at least 3 words) and **How do the two ideas meet here?** with chips **One limits the other**, **One causes the other**, **They pull against each other**, **They join into one**, plus a line of their own (up to 160 characters). An untied knot (no quote) shows as a loose loop and does not count.

**Readouts** (under the spools): **Stitches** (per thread, with the share of the text's sentences), **Longest gap** (most sentences in a row without that thread), **Shape** (the sequence of chips as small icons, for example Introduces, Explains, Raises a problem, Concludes), and **Knots** (tied, of found).

**Central idea card** (opens after 4 stitches on a thread): "In one sentence, the central idea is ___." and "It builds from ___ to ___ by ___." (up to 200 characters each). In Two threads, a third prompt: "The two ideas meet at the knot in paragraph ___, where ___." **Compare with ours** draws our threads as thin dotted lines beside the student's and lists our knots with their quotes.

Panel (right): `#hint`, the text's word count and source line, and **Clear my work** (asks Yes / No).

## Content
Three texts, each quoted exactly from the named source; source em dashes show as two hyphens (--). Setups, thread names and our stitches are written for Curio Class. Sentences are split by hand in `tools/idea-threads/texts.json` (Du Bois's p0 keeps its inner questions inside their sentences). Word counts by script on 2026-10-27, every space-separated token with a letter or digit.

1. **Dwight D. Eisenhower, Farewell Address, January 17, 1961, section IV** (538 words, 11 paragraphs, p0 to p10 after the join below), from "A vital element in keeping the peace is our military establishment." to "...ever aiming toward the supreme goals of our free society." Source: Public Papers of the Presidents of the United States: Dwight D. Eisenhower, 1960-61, pp. 1035-1040 (a United States government work). The Avalon Project copy used for checking has two dropped hyphens and one broken paragraph: show "military-industrial complex" and "scientific-technological elite", and join "...is ever present" with "and is gravely to be regarded." into one paragraph. The address's own "--" stays as two hyphens. Setup: a retiring president and former general warns the country about the defense industry it has built.
   - Our threads: **Security** ("we must stay strong") and **Liberty** ("we must stay free").
   - Security stitches: p0 both sentences (Introduces); p2 "But now we can no longer risk emergency improvisation..." (Explains) and "We annually spend on military security more than the net income of all United States corporations." (Gives an example); p3 "We recognize the imperative need for this development." (Explains).
   - Liberty stitches: p3 "The total influence..." (Raises a problem) and "Yet we must not fail to comprehend its grave implications." (Raises a problem); p4 both sentences (Explains); p5 "We must never let the weight of this combination endanger our liberties or democratic processes." (Concludes); p9 (the joined paragraph) "The prospect of domination of the nation's scholars..." (Gives an example) and "...the captive of a scientific-technological elite." (Raises a problem).
   - Both threads (the knot sentences, which a knot needs both threads to pass through): p5 "Only an alert and knowledgeable citizenry..." (Security: Concludes; Liberty: Concludes); p10 "It is the task of statesmanship..." (Security: Concludes; Liberty: Concludes).
   - Our knots: p5 "so that security and liberty may prosper together" (They join into one); p10 "to mold, to balance, and to integrate these and other forces" (One limits the other).

2. **W. E. B. Du Bois, "Of Our Spiritual Strivings," The Souls of Black Folk (Chicago: A. C. McClurg, 1903), opening** (366 words): paragraphs p0, p2 and p3 of the chapter (numbered from 0, so the left-out paragraph is p1), from "Between me and the other world there is ever an unasked question:" to "...without having the doors of Opportunity closed roughly in his face." The second paragraph (his boyhood memory of a classmate refusing his visiting card, 391 words) is left out and marked "[One paragraph left out: a schoolroom memory. Read it in the full chapter.]". Setup: Du Bois, a historian and sociologist, writes about being Black in America forty years after emancipation.
   - Our threads: **Seen by others** (being looked at as "a problem") and **Two selves** (striving to be both American and Black).
   - Seen by others: p0 first sentence (Introduces), the "they say" sentence (Gives an example), "To the real question, How does it feel to be a problem? I answer seldom a word." (Concludes); p2 first sentence (Explains).
   - Two selves: p2 "One ever feels his twoness..." (Explains); p3 first sentence (Explains), "He would not Africanize America..." and "He would not bleach his Negro soul..." (Explains), last sentence (Concludes).
   - Both threads (knot sentences): p2 "It is a peculiar sensation, this double-consciousness..." (Seen by others: Explains; Two selves: Introduces); p3 last sentence, "He simply wishes to make it possible..." (Seen by others: Raises a problem; Two selves: Concludes, as above).
   - Our knots: p2 "this sense of always looking at one's self through the eyes of others" (One causes the other); p3 "without being cursed and spit upon by his fellows" (They pull against each other).
   - Context line on the card, plainly: in 1903 Black Americans in the South lived under Jim Crow segregation laws, were kept from voting, and faced lynching; "Southern outrages" in p0 refers to this violence. "Negro" was the respectful term of Du Bois's time; the tool uses "Black" in its own words.

3. **Henry David Thoreau, "Resistance to Civil Government" (1849; later titled "Civil Disobedience"), opening** (422 words): p0 (185 words), p2 (51) and the first eight sentences of p3 (186), numbered from 0, through "The only obligation which I have a right to assume, is to do at any time what I think right." p1 is left out and marked "[One paragraph left out: why the government is 'a sort of wooden gun.']". Italic _at once_ in p2 stays italic. Setup: Thoreau spent a night in jail in 1846 for refusing to pay a tax, in protest against slavery and the war with Mexico.
   - Our threads: **Less government** and **Conscience first**.
   - Less government: p0 first sentence (Introduces), second (Explains), "Government is at best but an expedient..." (Explains), "Witness the present Mexican war..." (Gives an example).
   - Conscience first: p2 "Let every man make known what kind of government would command his respect..." (Explains); p3 "But a government in which the majority rule in all cases can not be based on justice..." (Raises a problem), "Must the citizen ever for a moment..." (Explains), "I think that we should be men first, and subjects afterward." (Concludes), "The only obligation..." (Concludes).
   - Both threads (knot sentences): p2 "But, to speak practically and as a citizen..." (Less government: Concludes; Conscience first: Introduces); p3 "Can there not be a government in which the majorities do not virtually decide right and wrong, but conscience?..." (Less government: Explains; Conscience first: Explains).
   - Our knots: p2 "not at once no government, but at once a better government" (One limits the other); p3 "Can there not be a government in which the majorities do not virtually decide right and wrong, but conscience?" (They join into one).

## Interactions in detail
- Sentences are buttons; Tab moves through them; Enter stitches with the active thread; 1 and 2 switch threads in Two threads.
- A knot appears only on a sentence that both threads are stitched through (ours are, at every knot listed in Content).
- The thread redraws in under 100 ms; with Motion on, a new stitch pulls the thread in over 300 ms and the needle dips; with Motion off it appears. A tap on another sentence during the pull stitches it at once (the first pull jumps to its end).
- Knot quotes: select with mouse or touch, or with the keyboard (Shift plus arrows inside the focused sentence, then Enter). A quote outside the sentence or under 3 words is refused with "Pick words from this sentence, at least three."
- Readouts update live; screen readers hear, for example with ours on Eisenhower (28 sentences), "Security, 7 stitches, 25 percent; longest gap 9 sentences".
- Store: localStorage `idea-threads` (per text and mode: thread names, stitches with chips, knots with quotes, card text), try/catch. Clear my work (after Yes) empties it.
- Sizes: at 1366x768 and 1280x720 the cloth fills the stage with the margin on the right and readouts in the panel; at 680x425 the cloth scrolls inside its box with spools pinned on top; at 760 and 375 wide the margin narrows to 40 px and readouts move under the cloth.

## Look
- `kit:theme-912` dark, accent `--brand #ff6fd0` (magenta thread: thread A, stitch marks, header rule, buttons), `--btn #ff6fd0`, brand text on brand `--brand-ink #1c1203`.
- Thread B `#ffcf5c` (gold). Threads also differ in pattern (A solid, B dashed) and each stitch shows the thread's initial; knots are drawn in `--ink` as a small square knot.
- Cloth: the painted linen (Art) blended over `--panel` at 30 percent, text in `--ink`; contrast is measured on `--panel` and checked on the texture's lightest patch at build.
- Neighbors: tone-dial orchid (this group, dE 24), character-web rose (this group), theme-ledger wine. Nearest catalog color: boolean-builder's pink (dE 23).
- Contrast (WCAG 2.1): brand on paper `#0d1219` 7.55:1, on panel 6.95:1, on sec-bg 6.59:1; brand-ink on brand 7.42:1; thread B `#ffcf5c` on panel 11.81:1. All pass AA.

## Art
Seven painted images, all local FLUX (`scripts/localart.py`), people: false. No portraits: the picker shows a thing from each text's world.
- `linen`: "Close-up of dark indigo linen cloth, even weave, soft even light, filling the frame, seamless". 1:1; cutout no; people: false. Tiled under the cloth at 30 percent over `--panel`.
- Sewing kit (3 cutouts, shared prompt: "single object, painted, soft studio light, plain dark backdrop"): `spool-a` a wooden spool wound with magenta thread; `spool-b` a wooden spool wound with gold thread; `needle` a long steel sewing needle, eye at the top, at a slight angle. Spools 1:1, needle 9:16; cutout yes; people: false. Sizing rule: spools 48 px tall above the cloth (40 px at 375 wide); the needle 36 px tall, drawn at the stitch's left edge for 300 ms. The thread itself, stitches and knots stay in code because they bend.
- Picker kit (3 images, shared prompt: "painted, quiet light, no lettering on any surface"): `pick-eisenhower` a 1960s desk microphone on a polished wooden desk beside a closed folder; `pick-dubois` an old cloth-bound book with a blank cover on a wooden desk by a window, autumn light; `pick-thoreau` a small wooden cabin beside a pond in autumn, pine woods behind. 4:3; cutout no; people: false. Picker card pictures, about 200 px wide.
Drawn in code: threads, stitch marks, knots, readouts, the Shape icons and preview.svg.

## Voice
Bank voice `bright-teacher` (Autonoe), style "Say brightly and clearly, like an energetic high school teacher". Not used by any 9-12 tool or another spec in this batch (its one other use is a grade 3-5 tool with a first-grade style). `Curio.voice`, scope the text and mode. The texts are never voiced; Read speaks the hint.
- welcome (how, first open, picker showing; stale when a text is picked): "Tap a text to open it. Then tap every sentence that builds one idea."
- stitch (how, first stitch; stale once a chip is chosen): "Good. Now tap a chip to say what that sentence does for the idea."
- gap (event, each time Longest gap reaches 6 sentences; stale on the next stitch): "That's a long stretch of bare cloth. Read it again, and tap any sentence that still carries the idea."
- two (how, first Two threads; stale once the second thread has a stitch): "Two ideas now. Tap the gold spool, then stitch the second idea. Where both threads meet, you'll tie a knot."
- knot (how, first knot found; stale once it is tied): "To tie it, select the words in that sentence that carry both ideas, then pick how they meet."
- card (how, Central idea card opens; stale once its first box has text): "Now write the central idea in one sentence, and how it builds."

## Family engine
none

## Sources
- Eisenhower: Public Papers of the Presidents of the United States: Dwight D. Eisenhower, 1960-61 (Washington: Government Printing Office, 1961), "Farewell Radio and Television Address to the American People," January 17, 1961, pp. 1035-1040; checked against the Avalon Project copy, https://avalon.law.yale.edu/20th_century/eisenhower001.asp , with the two hyphens and one paragraph break restored as noted.
- Du Bois: The Souls of Black Folk (Chicago: A. C. McClurg, 1903), Project Gutenberg eBook #408, https://www.gutenberg.org/ebooks/408 ; Jim Crow, voting and lynching context: Britannica, "Jim Crow law" and "W. E. B. Du Bois".
- Thoreau: "On the Duty of Civil Disobedience," Project Gutenberg eBook #71, https://www.gutenberg.org/ebooks/71 ; first publication as "Resistance to Civil Government" in Aesthetic Papers (1849), the night in jail in 1846 and its reasons: Britannica, "Civil Disobedience" and "Henry David Thoreau".
- Standards: CCSS ELA RI.9-10.1, .2, .3, .5 and RI.11-12.1, .2, .3, https://www.thecorestandards.org/ELA-Literacy/RI/9-10/ and https://www.thecorestandards.org/ELA-Literacy/RI/11-12/
- Setups, thread names, chips and our stitches: written for Curio Class.
- Checks run 2026-10-29 against the Avalon Eisenhower copy, Gutenberg #408 and Gutenberg #71: every one of our six knot quotes sat in a sentence that the old stitch lists did not stitch with both threads (Eisenhower's knots, for instance, sat in p5's third sentence and p10, which neither thread stitched), so no knot of ours could ever form. Both threads now pass through each knot sentence (Content). Eisenhower section IV has 28 sentences after the join; with ours, Security has 7 stitches (25 percent, longest gap 9) and Liberty 9 (32 percent, longest gap 9). The Thoreau knot's "the majorities" matches Gutenberg #71.

## Done when
1. Focus: at 1366x768 and 680x425 the cloth is the largest thing on screen and the spools stay visible above it.
2. The three texts match their sources word for word (538, 366 and 422 words by the stated rule), with "military-industrial" and "scientific-technological" hyphenated, the Avalon copy's split paragraph joined into Eisenhower p9, the two left-out paragraphs marked, and "--" for every source dash.
3. Stitching draws the thread into the sentence and asks for a chip; unstitching removes both; a tap on another sentence during the 300 ms pull stitches it at once.
4. In Two threads, a sentence with both threads shows a loose knot until a quote of 3 or more words inside it is chosen.
5. With ours loaded, Eisenhower shows 2 tied knots, at p5 ("so that security and liberty may prosper together") and p10; Du Bois and Thoreau show 2 each.
6. Longest gap and Shape match the stitches (with ours: Eisenhower Security 7 stitches, longest gap 9; Thoreau Less government Shape Introduces, Explains, Explains, Gives an example, Concludes, Explains).
7. Compare with ours shows dotted threads beside the student's and lists our knots with quotes.
8. The spools, needle, linen and picker pictures are painted; no people appear; no voice line names a control that is hidden or disabled.
9. Reload keeps all work per text and mode; Clear my work (after Yes) empties it; no network; console clean.
10. At every size in STANDARDS.md the cloth and spools are reachable without page scroll; 375 wide works in `drive.py --host`.

## Open questions
- [idea-threads] Du Bois's chapter uses "Negro," the respectful term of 1903, and his opening refers to the violence of the time ("Southern outrages"); the card says so plainly and the tool uses "Black" in its own words. Anything a parent might want to see first?
- [idea-threads] The Eisenhower text corrects the Avalon copy (two hyphens, one paragraph break) to match the Public Papers. If Cory prefers, the builder can check page images of the Public Papers on GovInfo before shipping.
- [idea-threads] Two Du Bois and Thoreau paragraphs are left out to keep each text under about 550 words. OK, or include them whole?

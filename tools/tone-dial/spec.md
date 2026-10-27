# Tone Dial

## One idea
Tone lives in a handful of words: turn one dial and the same evening scene (same train, same house, same dog, same woman at the gate) rewrites itself ominous, playful, bitter, tender or awed, eight words at a time, with a heat strip showing which words carry the tone and a meaning check showing which swaps only change the feeling and which quietly change the facts; then take the dial to Poe, Austen and Irving, find the words that set their tone, and drain them one by one to hear the tone go.

## Not like
- word-thermometer (ela 6, concept): near-synonyms sorted cool to hot. Here whole tones (not one scale) built from many slots at once, plus figures of speech, and real classic openings.
- satire-decoder (ela 11, wave 4): what a satire really means. Here how word choice alone sets a feeling; Austen's irony appears only as one tone among several.
- rhetoric-spotter (ela 9, spec): devices that persuade. Here words that make a mood, not an argument.
- page-to-screen and ambiguity-lab (this group): medium and structure as the variables. Here only diction and figures change.
- world-lit-atlas (ela 10, this group): what a word assumes the reader knows. Here what a word makes the reader feel.

## Who and how
- Grade 10 ELA, module Figurative Language and Tone: "How word choices shape meaning and tone".
- Standards: RL.9-10.4, L.9-10.5.
- Driver: students on laptops, alone or in pairs, 20 to 30 minutes. A teacher can project the dial and let the room call out tones.
- tool.json: driver "students", minutes "20-30", modes ["Dial", "Classics"], grades_label "Grade 10". Kit starter with `kit:theme-912` (dark) and an accent override.

## Screens and modes
Kit frame. Header: "Tone Dial", small line "Same scene, different words"; Motion, Sound, Read.

**Dial.** Left: the dial, a large knob with six labeled stops around it (Matter-of-fact at the top, then Ominous, Playful, Bitter, Tender, Awed), each with its icon (ruler, moon, star, lemon, heart, mountain). Turning it snaps to a stop and rewrites every slot to that tone. Middle: the paragraph, large, with its 8 slots underlined; a swapped word cross-fades (instant with Motion off). Under it:
- the **heat strip**: 8 cells, one per slot, colored by the slot's tone with a 1 to 3 bar for how strong the word is (our rating);
- the **meaning check**: each slot's current word marked **Feeling only** (same facts, new connotation) or **Adds a fact** (a reader learns something new: who, how, how often, how big), with a dotted underline on Adds a fact words;
- **Figure** tags on slots that hold a figure of speech (simile, metaphor, personification), named.
Tap a slot to open its six choices and set it alone (the dial's pointer goes grey: **Mixed**). The **Tone reading** then names the leading tone by summed strength ("Mostly tender"), adds "with a touch of ominous" when another tone holds 2 or more slots, and says "Mixed: ominous and tender" when the top two sums are within 1 point. **Hear it** reads the current paragraph aloud only when all 8 slots share one tone (the six pure versions are recorded; the voice and its style never change, so only the words change the feeling). **Lock** on a slot keeps it when the dial turns.

**Mystery mix** (button): shows one of six mixed paragraphs written for Curio Class with the heat strip hidden; the student picks the leading tone and taps the one word that gives it away most, then the strip appears.

**Classics.** Three openings, each as printed:
- the student taps up to 6 words or phrases that set the tone, then picks the tone from chips (the six above plus **Gloomy**, **Ironic**, **Affectionate**);
- **Show ours** lights our tone words and our tone;
- **Drain** toggles, one per lit word, swap it for a plain word written for Curio Class (shown in `--muted` italics); **Drain all** shows our whole plain rewrite, labeled "Our plain rewrite, not the author's".
- A note box: "The word that does the most work is ___ because ___." (up to 200 characters, saved).

Panel (right): `#hint`, the tone legend with icons, **Mystery mixes solved** (n of 6), and **Clear my work** (asks Yes / No).

## Content
**The scene** (written for Curio Class): "The evening train {1} into the station as the sun {2} behind the hills. Across the tracks stood the {3} house, its windows {4}. A dog {5} the platform. By the gate a woman {6}, her coat {7}. The bell rang once, and then the platform was {8}."

| Slot | Matter-of-fact | Ominous | Playful | Bitter | Tender | Awed |
|---|---|---|---|---|---|---|
| 1 | came | crawled | puffed and bustled | dragged itself | eased | thundered (A) |
| 2 | went down | bled out (F metaphor) | ducked (F personification) | gave up (F personification) | settled | blazed down |
| 3 | old | crumbling (A) | lopsided (A) | neglected (A) | weathered | towering (A) |
| 4 | reflecting the sunset | staring out like dead eyes (F simile) | winking like a row of jack-o'-lanterns (F simile) | glaring like unpaid bills (F simile) | glowing like a lamp left on for someone (F simile) | burning like stained glass in a cathedral (F simile) |
| 5 | crossed | slunk across | trotted across | limped across (A) | padded across | bounded across |
| 6 | waited | lurked (A) | bounced on her toes (A) | waited, as she always did (A) | waited patiently | stood perfectly still |
| 7 | buttoned | clutched tight | flapping | worn thin (A) | wrapped snug | billowing |
| 8 | quiet | deathly still | hushed, as if holding back a giggle (F personification) | empty again (A) | peaceful | silent |
(A) = Adds a fact; (F) = Figure, named. Every other variant is Feeling only. Strength ratings (1 to 3) for each cell are ours, stored in `tools/tone-dial/scene.json`; Matter-of-fact cells are 0.

**Mystery mixes** (written for Curio Class, in scene.json): six slot settings, each with a leading tone and our giveaway word, for example: slots 1 to 8 = Tender, Tender, Ominous, Tender, Tender, Tender, Ominous, Tender, leading Tender, giveaway "glowing like a lamp left on for someone", with the ominous slots as the twist to discuss.

**Classics** (quoted exactly; dashes as two hyphens):
1. **Edgar Allan Poe, "The Fall of the House of Usher"** (1839), first sentence: "During the whole of a dull, dark, and soundless day in the autumn of the year, when the clouds hung oppressively low in the heavens, I had been passing alone, on horseback, through a singularly dreary tract of country; and at length found myself, as the shades of the evening drew on, within view of the melancholy House of Usher." Ours: tone **Gloomy**; words "dull, dark, and soundless", "oppressively", "alone", "singularly dreary", "the shades of the evening drew on", "melancholy". Our plain rewrite: "During a cloudy, quiet autumn day, when the clouds were low, I had been riding by myself through a stretch of country; and at evening I came within view of the House of Usher."
2. **Jane Austen, Pride and Prejudice** (1813), chapter 1, first two paragraphs: "It is a truth universally acknowledged, that a single man in possession of a good fortune must be in want of a wife." / "However little known the feelings or views of such a man may be on his first entering a neighbourhood, this truth is so well fixed in the minds of the surrounding families, that he is considered as the rightful property of some one or other of their daughters." Ours: tone **Ironic**; words "a truth universally acknowledged", "must be in want of", "so well fixed", "rightful property". Our plain rewrite: "Many families believe that a rich single man wants a wife. When such a man moves into a neighbourhood, the families there, without knowing what he thinks, expect him to marry one of their daughters." Note on the card: the irony is that the families, not the man, are the ones in want.
3. **Washington Irving, "Rip Van Winkle,"** The Sketch-Book of Geoffrey Crayon (1819), first paragraph, through "...will glow and light up like a crown of glory." (the source prints its first word in capitals, "WHOEVER"; show "Whoever"). Ours: tone **Affectionate** with **Awed**; words "dismembered branch of the great Appalachian family" (F metaphor), "lording it over" (F personification), "magical hues", "perfect barometers" (F metaphor), "clothed in blue and purple" (F personification), "a hood of gray vapors" (F metaphor), "like a crown of glory" (F simile). Our plain rewrite: "Anyone who has sailed up the Hudson will remember the Catskill mountains. They are part of the Appalachians, west of the river, and they rise above the country around them. Their colors and shapes change with the season, the weather and the hour, and the local women use them to forecast the weather. In fair weather they look blue and purple against the evening sky; sometimes, when the rest of the sky is clear, clouds gather on their tops and glow in the sunset."

## Interactions in detail
- Dial: drag, click a stop, or focus and use arrow keys (Left and Right step through stops; Home returns to Matter-of-fact). Each stop has a visible label; screen readers hear "Tone: ominous, 8 slots set".
- Slot menu: Enter opens six choices as a radio group with the tone icons; choosing one sets Mixed if the slots now differ.
- Swaps cross-fade over 250 ms; with Motion off they cut.
- Heat strip cells are buttons that focus their slot. Strength bars carry numbers on focus.
- Hear it is disabled with "Hear it works on a pure tone" in Mixed.
- Classics: words are tappable spans in exact source text; a seventh tap asks to untap one first. Drain toggles are per word and reversible.
- Store: localStorage `tone-dial` (slot settings, locks, mystery answers, classics taps and notes), try/catch. Clear my work (after Yes) empties it.
- Sizes: at 1366x768 and 1280x720 dial left, paragraph and strip right; at 680x425 the dial shrinks to 160 px above the paragraph; at 760 and 375 wide the dial becomes a row of six tone buttons above the paragraph.

## Look
- `kit:theme-912` dark, accent `--brand #f29ff0` (orchid: the dial pointer, slot underlines, header rule, buttons), `--btn #f29ff0`, brand text on brand `--brand-ink #1c1203`.
- Tone colors, always with icon and label: Matter-of-fact `#a6b3c4` (ruler), Ominous `#9fa8ff` (moon), Playful `#ffcf5c` (star), Bitter `#a8d65a` (lemon), Tender `#ffb08a` (heart), Awed `#5ad1ff` (mountain). Nearest pair: Matter-of-fact and Awed, dE 30, separated by icons.
- The dial: a dark knob with a soft orchid ring, stops as small labeled ticks.
- Neighbors: idea-threads magenta (this group, dE 24), character-web rose (this group). Nearest catalog color: `--gr-2` (dE 17).
- Contrast (WCAG 2.1): brand on paper `#0d1219` 9.84:1, on panel 9.06:1, on sec-bg 8.59:1; brand-ink on brand 9.67:1; tone colors on sec-bg: `#a6b3c4` 7.71:1, `#9fa8ff` 7.44:1, `#ffcf5c` 11.19:1, `#a8d65a` 9.71:1, `#ffb08a` 9.24:1, `#5ad1ff` 9.37:1. All pass AA.

## Art
None needed: the dial, icons, heat strip and preview.svg (an orchid knob beside one sentence with three words lit in different tone colors) are drawn in code.

## Voice
Bank voice `gentle-storyteller` (Vindemiatrix), style "Say gently and expressively, like a storyteller reading aloud". Not used by any 9-12 ELA tool or this group. `Curio.voice`, scope the mode. The six pure-tone paragraphs are recorded as their own clips in the same voice and style; the classics are never voiced.
- welcome (how, first open): "Same evening, same station. Turn the dial and listen to the words change the feeling."
- slot (how, first slot opened): "Pick a word for just this slot. Now the scene is mixed."
- fact (event, first Adds a fact word appears; stale on the next swap): "Careful. That word didn't just change the feeling. It changed the facts."
- mystery (how, first Mystery mix): "Which tone is leading? Tap the word that gives it away."
- classics (how, first Classics): "Now a real opening. Tap the words you think set its tone."
- drain (how, first Drain): "Drain one word at a time. Which one takes the most tone with it?"
- scene-matter-of-fact, scene-ominous, scene-playful, scene-bitter, scene-tender, scene-awed (event, Hear it on that pure tone; stale on the next swap): the full paragraph for that tone, built from the template and the table above.

## Family engine
none

## Sources
- Poe: "The Fall of the House of Usher" (Burton's Gentleman's Magazine, 1839), in The Works of Edgar Allan Poe, Raven Edition, vol. 2, Project Gutenberg eBook #2148, https://www.gutenberg.org/ebooks/2148 ; Britannica, "The Fall of the House of Usher".
- Austen: Pride and Prejudice (1813), Project Gutenberg eBook #1342, https://www.gutenberg.org/ebooks/1342 ; Britannica, "Pride and Prejudice".
- Irving: "Rip Van Winkle," in The Sketch-Book of Geoffrey Crayon (1819), Project Gutenberg eBook #2048, https://www.gutenberg.org/ebooks/2048 ; Britannica, "Rip Van Winkle".
- Figures of speech (simile, metaphor, personification) and tone: Britannica, "figure of speech" and "tone".
- Standards: CCSS ELA RL.9-10.4 and L.9-10.5, https://www.thecorestandards.org/ELA-Literacy/
- The scene, its variants, strength ratings, mystery mixes, our tone words and plain rewrites: written for Curio Class.

## Done when
1. Each of the six dial stops produces the paragraph built from its column of the table, exactly.
2. The meaning check marks the (A) cells Adds a fact and all others Feeling only; (F) cells show their figure name.
3. The Tone reading follows its rule on two cases the builder computes by hand from scene.json, including the Tender and Ominous mystery mix ("Mostly tender, with a touch of ominous" unless the sums fall within 1 point).
4. Hear it plays only on a pure tone and plays the matching recorded paragraph.
5. Classics show the three passages exactly as printed ("Whoever" for Irving's capitals); Drain all shows the plain rewrite with its label.
6. Six mystery mixes; each records the guess and the giveaway word and then shows the strip.
7. Reload keeps all work; Clear my work (after Yes) empties it; no network; console clean.
8. At every size in STANDARDS.md the dial (or its button row) and the paragraph are reachable without page scroll; 375 wide works in `drive.py --host`.

## Open questions
- [tone-dial] The ominous column ("bled out", "staring out like dead eyes", "lurked") and Poe's opening are spooky but not violent. Fine for grade 10 as written?
- [tone-dial] The six pure paragraphs are recorded in one unchanging voice so only the words carry tone. Would Cory rather have no audio for the scene at all?

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

**Dial.** Focus: the paragraph with its 8 slots, the largest thing on the stage, in the middle column; the dial is the control beside it, not the center. Left: the dial, a large knob with six labeled stops around it (Matter-of-fact at the top, then Ominous, Playful, Bitter, Tender, Awed), each with its icon (ruler, moon, star, lemon, heart, mountain). Turning it snaps to a stop and rewrites every slot to that tone. Under the dial, a small painted postcard of the scene (Art) in plain evening light, captioned "The facts never change": the station, the train, the house, the dog and the gate, painted once and never retinted, so only the words carry the tone. Middle: the paragraph, large, with its 8 slots underlined; a swapped word cross-fades (instant with Motion off). Under it:
- the **heat strip**: 8 cells, one per slot, colored by the slot's tone with a 1 to 3 bar for how strong the word is (our rating);
- the **meaning check**: each slot's current word marked **Feeling only** (same facts, new connotation) or **Adds a fact** (a reader learns something new: who, how, how often, how big), with a dotted underline on Adds a fact words;
- **Figure** tags on slots that hold a figure of speech (simile, metaphor, personification), named.
Tap a slot to open its six choices and set it alone (the dial's pointer goes grey: **Mixed**). The **Tone reading** then names the leading tone by summed strength ("Mostly tender"), adds "with a touch of ominous" when another tone holds 2 or more slots, and says "Mixed: ominous and tender" when the top two sums are within 1 point (full rule in Content). **Hear it** reads the current paragraph aloud only when all 8 slots share one tone (the six pure versions are recorded, each about 15 s; the voice and its style never change, so only the words change the feeling). Turning the dial or tapping a slot while it plays stops the clip at once and rewrites the paragraph. **Lock** on a slot keeps it when the dial turns.

**Mystery mix** (button): focus the mixed paragraph, in the same middle column. It shows one of six mixed paragraphs written for Curio Class with the heat strip hidden; the student picks the leading tone and taps the one word that gives it away most, then the strip appears.

**Classics.** Focus: the opening's text, large in the middle column, with the tone chips under it. Three openings, each as printed:
- the student taps up to 6 words or phrases that set the tone, then picks the tone from chips (the six above plus **Gloomy**, **Ironic**, **Affectionate**);
- **Show ours** lights our tone words and our tone, and only then shows a painting of the opening's place in that tone (Art), captioned "One painter's mood for this opening"; before Show ours no picture is shown, so the picture never gives the tone away;
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
(A) = Adds a fact; (F) = Figure, named. Every other variant is Feeling only. Strength ratings (1 to 3, ours, stored in `tools/tone-dial/scene.json`; Matter-of-fact cells are 0), slots 1 to 8:
- Ominous 2, 3, 2, 3, 2, 3, 1, 3 (pure total 19)
- Playful 2, 2, 1, 3, 1, 2, 1, 3 (15)
- Bitter 2, 2, 2, 3, 1, 3, 2, 2 (17)
- Tender 1, 1, 1, 3, 1, 2, 2, 2 (13)
- Awed 3, 2, 2, 3, 1, 1, 2, 1 (15)

**Tone reading rule.** On a pure stop: the tone's name ("All ominous"). Otherwise sum each tone's strengths over the slots it holds. If 5 or more slots are Matter-of-fact: "Mostly matter-of-fact", plus ", with a touch of [tone]" for the strongest other tone if any. Else if the top two sums are within 1 point (and the second is above 0): "Mixed: [top] and [second]". Else "Mostly [top]", plus ", with a touch of [tone]" for the strongest other tone that holds 2 or more slots.

**Mystery mixes** (written for Curio Class, in scene.json): six slot settings (slots 1 to 8; O ominous, P playful, B bitter, T tender, A awed, M matter-of-fact), each with its reading by the rule and our giveaway word:
1. T T O T T T O T: "Mostly tender, with a touch of ominous" (tender 10, ominous 3). Giveaway "glowing like a lamp left on for someone"; the ominous slots are the twist to discuss.
2. P P B P P P B P: "Mostly playful, with a touch of bitter" (13, 4). Giveaway "hushed, as if holding back a giggle".
3. O T O T O T O T: "Mixed: tender and ominous" (8, 7). Either tone matches ours; no single giveaway, so the card names the strongest word of each ("glowing like a lamp left on for someone" for tender; "crawled", "crumbling" and "slunk across", 2 each, for ominous) and asks which one the student heard first.
4. A A M A M M A M: "Mostly awed" (10; the 4 Matter-of-fact slots add nothing). Giveaway "burning like stained glass in a cathedral".
5. B B B T B B B T: "Mostly bitter, with a touch of tender" (12, 5). Giveaway "waited, as she always did".
6. O O P O O O P O: "Mostly ominous, with a touch of playful" (16, 2). Giveaway "lurked".

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
- The dial: a dark knob with a soft orchid ring, stops as small labeled ticks. The scene postcard sits in a thin `--line` frame; the classics paintings in a thin frame of their tone's color.
- Neighbors: idea-threads magenta (this group, dE 24), character-web rose (this group), punctuation-power-ups magenta #ff4fd8 (dE 38). Nearest catalog color: `--gr-2` (dE 17).
- Contrast (WCAG 2.1): brand on paper `#0d1219` 9.84:1, on panel 9.06:1, on sec-bg 8.59:1; brand-ink on brand 9.67:1; tone colors on sec-bg: `#a6b3c4` 7.71:1, `#9fa8ff` 7.44:1, `#ffcf5c` 11.19:1, `#a8d65a` 9.71:1, `#ffb08a` 9.24:1, `#5ad1ff` 9.37:1. All pass AA. Captions sit on solid panel, never on the paintings.

## Art
House style "painterly realistic illustration, oil paint texture". 5 images. Places and props go to local FLUX (`scripts/localart.py`); the one person goes to Gemini (`scripts/art.py`), set aside for now, so she waits on Cory's review.
- td-station: a small country railway station at early evening in plain even light, a steam train standing at the platform, a dog standing on the platform, across the tracks an old two-story house with lit windows, a wooden gate by the road in the lower right with an open space beside it, low hills behind; 16:9; cutout no; people no; the scene postcard under the dial. It is painted in neutral light and never retinted by the dial.
- td-woman: a woman in a long buttoned coat standing still beside a gate, full figure, seen from behind and a little to the side, small and plain, plain white background; 3:4; cutout yes; people: true; Gemini, Cory reviews; placed in the open space by the gate in td-station at the postcard's figure scale (her height about a quarter of the postcard). Until approved, the postcard shows without her.
- td-usher: a grim old stone manor beside a still black pond under low heavy autumn clouds, bare trees and grey reeds; 16:9; cutout no; people no; the Poe painting, shown after Show ours.
- td-netherfield: a large handsome Georgian country house with a gravel drive and a closed carriage at the door, green lawns and tall trees, bright morning; 16:9; cutout no; people no; the Austen painting, shown after Show ours.
- td-catskills: the Catskill mountains in blue and purple seen across the wide Hudson River at sunset, a small village of rooftops at their foot and a band of glowing cloud on the peaks; 16:9; cutout no; people no; the Irving painting, shown after Show ours.
Drawn in code: the dial, icons, heat strip, slots, chips and preview.svg (an orchid knob beside one sentence with three words lit in different tone colors).

## Voice
Bank voice `gentle-storyteller` (Vindemiatrix), style "Say gently and expressively, like a storyteller reading aloud". Not used by any 9-12 ELA tool or this group. `Curio.voice`, scope the mode. The six pure-tone paragraphs are recorded as their own clips in the same voice and style; the classics are never voiced.
- welcome (how; on entering Dial; stale once the dial turns or a slot opens): "Same evening, same station. Turn the dial on the left and watch the words change the feeling."
- slot (how; the first slot menu opened; stale once a word is picked): "Pick a word for just this slot. Now the scene is mixed."
- fact (how; the first time an Adds a fact word appears; stale on the next swap): "Careful. That word didn't just change the feeling. It changed the facts."
- mystery (how; the first Mystery mix shown; stale once a tone is picked): "Tap the tone you think is leading. Then tap the word that gives it away."
- classics (how; on entering Classics; stale once a word is tapped): "Now a real opening. Tap up to six words that set its tone, then tap a tone chip."
- drain (how; the first time Show ours lights the words; stale once a word is drained): "Tap Drain on one lit word at a time. Which one takes the most tone with it?"
- scene-matter-of-fact, scene-ominous, scene-playful, scene-bitter, scene-tender, scene-awed (event; each Hear it on that pure tone; stale on the next swap, dial turn or mode change): the full paragraph for that tone, built from the template and the table above.

## Family engine
none

## Sources
- Poe: "The Fall of the House of Usher" (Burton's Gentleman's Magazine, 1839), in The Works of Edgar Allan Poe, Raven Edition, vol. 2, Project Gutenberg eBook #2148, https://www.gutenberg.org/ebooks/2148 ; Britannica, "The Fall of the House of Usher".
- Austen: Pride and Prejudice (1813), Project Gutenberg eBook #1342, https://www.gutenberg.org/ebooks/1342 ; Britannica, "Pride and Prejudice".
- Irving: "Rip Van Winkle," in The Sketch-Book of Geoffrey Crayon (1819), Project Gutenberg eBook #2048, https://www.gutenberg.org/ebooks/2048 ; Britannica, "Rip Van Winkle".
- Figures of speech (simile, metaphor, personification) and tone: Britannica, "figure of speech" and "tone".
- Standards: CCSS ELA RL.9-10.4 and L.9-10.5, https://www.thecorestandards.org/ELA-Literacy/
- The scene, its variants, strength ratings, mystery mixes, our tone words and plain rewrites: written for Curio Class.
- Number checks (Python, 2026-10-29): the strength table and the reading rule above give, for the six mystery mixes, the readings listed in Content (tender 10 against ominous 3; playful 13 against bitter 4; tender 8 against ominous 7, Mixed; awed 10 alone; bitter 12 against tender 5; ominous 16 against playful 2). Edge cases: all Matter-of-fact reads "Mostly matter-of-fact"; one ominous slot among seven Matter-of-fact reads "Mostly matter-of-fact, with a touch of ominous"; four ominous and four playful reads "Mostly ominous, with a touch of playful" (10 against 7); four ominous and four tender reads "Mostly ominous, with a touch of tender". Over every one of the 6 to the 8th (1,679,616) slot settings, 45 percent read Mixed, so a student mixing freely will often see the Mixed reading; that is expected, not a fault. The old spec left the strength values and five of the six mixes to the build; they are now written out so the readings can be checked.

## Done when
1. Each of the six dial stops produces the paragraph built from its column of the table, exactly.
2. The meaning check marks the (A) cells Adds a fact and all others Feeling only; (F) cells show their figure name.
3. The Tone reading follows its rule: the six mystery mixes read exactly as listed in Content, and all Matter-of-fact reads "Mostly matter-of-fact".
4. Hear it plays only on a pure tone and plays the matching recorded paragraph.
5. Classics show the three passages exactly as printed ("Whoever" for Irving's capitals); Drain all shows the plain rewrite with its label; each painting appears only after Show ours.
6. Six mystery mixes; each records the guess and the giveaway word and then shows the strip; in mix 3 either tender or ominous matches ours.
7. Focus: at 1366x768 and 680x425 the paragraph is the largest text on the stage and sits in the middle, with the dial beside or above it, never over it.
8. A tap while anything plays: turning the dial during Hear it stops the clip at once and shows the new paragraph; a second dial step during a 250 ms cross-fade lands on the newer stop at once.
9. Reload keeps all work; Clear my work (after Yes) empties it; no network; console clean.
10. At every size in STANDARDS.md the dial (or its button row) and the paragraph are reachable without page scroll; 375 wide works in `drive.py --host`.
11. Voice: each how line plays once and names an enabled control; the four FLUX images load with no person; until Cory approves td-woman the postcard shows without her.

## Open questions
- [tone-dial] The ominous column ("bled out", "staring out like dead eyes", "lurked") and Poe's opening are spooky but not violent. Fine for grade 10 as written?
- [tone-dial] The six pure paragraphs are recorded in one unchanging voice so only the words carry tone. Would Cory rather have no audio for the scene at all?
- [tone-dial] The scene postcard needs the woman at the gate (one people image, Gemini, Cory reviews). Keep her, or leave the gate empty in the painting and let the words alone place her?
- [tone-dial] The three classics paintings show only after Show ours, as one painter's mood. Keep them, or leave the classics as text only?

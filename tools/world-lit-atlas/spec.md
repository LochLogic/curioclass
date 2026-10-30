# World Lit Atlas

## One idea
Every story assumes its first readers already know things: open a pin on the map, and the words a reader at home would never have stopped on glow; for each one you guess whether a first reader needed it explained, then see who actually explained it (the author, the translator, or nobody), and the pattern tells you whose eyes the passage was written for and whose experience it shows from the inside.

## Not like
- american-lit-timeline (ela 11, this group): works placed in time. Here works placed in the world, read for what they take for granted.
- art-through-time and art-passport (arts, live): artworks by place and period. Here the content is translated literature, and the work is reading, not looking.
- world-music-map and biome-atlas (live): maps of music and biomes. Here the map is only the door; each pin holds a passage to read closely.
- shakespeare-remix (ela 9, this group): what one writer took from another. Here what a culture's readers already carried in their heads.
- satire-decoder (ela 11, wave 4): said versus meant. Here said versus assumed.

## Who and how
- Grade 10 ELA, module World Literature: "Point of view and cultural experience in literature from outside the United States".
- Standards: RL.9-10.6.
- Driver: students on laptops, alone or in pairs, 25 to 40 minutes for three or four pins; a teacher can project one pin and poll the room on each glowing word.
- tool.json: driver "students", minutes "25-40", modes [] (pure explore), grades_label "Grade 10". Kit starter with `kit:theme-912` (dark) and an accent override.

## Screens and modes
Kit frame. Header: "World Lit Atlas", small line "Seven stories, seven first audiences"; Motion, Sound, Read.

**Map.** Focus: the map, filling the stage until a pin is opened. A world map drawn in code (Natural Earth land outline, dark land on darker sea) with seven pins, each a book icon with the author's name and year. A pin that has been read gets a filled ring. A **List** toggle shows the same seven as cards (author, title, place, year, translator) for keyboard and narrow screens.

**Reader** (opens beside the map, or over it on narrow screens), for the chosen pin. Focus: the passage. When the reader opens, it takes about two thirds of the stage and the map shrinks to the remaining third (still live, the open pin ringed).
- A painted picture of one thing from the passage that its first readers knew at a glance (Art), as a short strip at the top of the reader, captioned with the glowing word it shows.
- Header: title, author, place, year of first publication, original language, and the English edition used ("Translated by C. F. Andrews with the author, 1916"). A one-line setup written for Curio Class.
- **The passage**, with 4 to 6 **glowing words** (a soft accent underline and a small dot after each).
- Tap a glowing word: a small question card asks "Would a first reader in [place], [year] need this explained?" with **Yes** and **No**. After the choice, the card turns over: **What a reader at home knew** (two sentences, with its source), and **Who explained it in this passage**: **The author**, **The translator** (for a footnote or added phrase), or **Nobody**. A glowing word whose explanation sits in the passage itself also lights those words.
- When every glowing word is turned, the **Explained-o-meter** appears: a bar split into Author, Translator and Nobody, with counts.
- Then the **Reader card**: "Who was this passage written for?" with three chips (**Readers at home who knew all this**, **Readers far away**, **Both**), then **Show ours** with our answer and reason. Last, **Inside view**: "Whose experience does this passage show from the inside, and what does it take for granted?" (up to 240 characters, saved).

**Compare** (button on the map once two pins are read; focus the row of meters): the read pins' Explained-o-meters side by side, sorted from most explained to least, with one sentence per pin from the student's Reader card.

Panel (right): `#hint`, **Read** count (n of 7), a **Who's missing** note ("This atlas has no pin yet for the Middle East, South America or Oceania. Which story would you add?"), and **Clear my work** (asks Yes / No).

## Content
Passages are quoted exactly from the editions in Sources, each 100 to 310 words (Ibsen is the longest, 306); where a source has an em dash, show two hyphens (--). Setups, glosses and our answers are written for Curio Class and each gloss names its source.

1. **India (Kolkata). Rabindranath Tagore, "The Cabuliwallah"** (Bengali, 1892), translated by C. F. Andrews with the author, in The Hungry Stones and Other Stories (Macmillan, 1916). Passage: from "Then the Cabuliwallah, not to be behindhand, would take his turn:" to "...in which her formidable friend would join." Setup: a father in Calcutta watches his small daughter, Mini, befriend a peddler from Afghanistan. Glowing words: **Cabuliwallah** (a man from Kabul; such traders came to Calcutta each year to sell dried fruit; nobody explains it here; source: the story's own opening and Britannica, "Kabul"); **father-in-law's house** (a Bengali girl was raised knowing she would marry and go to live in her husband's family's house; the author explains the double meaning, "It is a euphemism for jail"); **Bengali** (the people and language of Bengal, Tagore's own; nobody); **new-fangled** (the family is modern enough to keep marriage talk from a small child; the author, in the same sentence); **policeman** (the peddler jokes about prison; nobody). Our Reader card: "Both. Tagore wrote for Bengali readers, but even they might not know a Kabul peddler's slang, so the narrator explains that one joke and nothing else." Explained-o-meter: Author 2, Translator 0, Nobody 3.

2. **Japan. Natsume Sōseki, Botchan** (Japanese, 1906), translated by Yasotaro Mori (1918). Passage: from "She wished to eat “sasa-ame”" to "She looked very small." (omit the transcriber's mark "[A]"; keep the translator's footnote 1 as a footnote). Setup: a young man leaves Tokyo to teach in a country school; Kiyo, the old servant who raised him, sees him off. Glowing words: **sasa-ame** (rice jelly wrapped in bamboo leaves; the translator explains it in footnote 1); **Echigo province** (a province on the Sea of Japan coast, far north-west of Tokyo, now Niigata Prefecture; nobody; Britannica, "Niigata"); **Hakone** (a mountain pass just west of Tokyo on the old road to Kyoto; Kiyo thinks anything far away is "the other side of Hakone", and readers in Tokyo would smile; nobody; Britannica, "Hakone"); **westward** (he is going to a town on the island of Shikoku; nobody; Britannica, "Botchan"); **rikishas** (rickshaws, pulled by a runner; nobody). Our Reader card: "Readers at home. Sōseki explains nothing; only the translator stops for one word, because English readers would never have tasted it." Explained-o-meter: Author 0, Translator 1, Nobody 4.

3. **China. Li Bai, "The River-Merchant's Wife: a Letter"** (Chinese, 8th century), as rendered by Ezra Pound in Cathay (London: Elkin Mathews, 1915), under the name "Rihaku". Passage: the whole poem. Setup: a young wife writes to her husband, away on a trading voyage. Glowing words: **Rihaku** (the Japanese reading of Li Bai's name; Pound worked from Ernest Fenollosa's notes, which used Japanese readings; nobody; Britannica, "Cathay" and "Li Bai"); **At fourteen I married** (marriages were arranged, and brides were often this young; nobody; Britannica, "Li Bai" for the period and Poetry Foundation's note on the poem); **Ku-to-Yen** (a dangerous gorge on the river upstream; nobody; Poetry Foundation); **Kiang** (Pound's form of jiang, "river", here the great river, the Yangtze; nobody); **Cho-fu-Sa** (a place downriver where she offers to meet him; nobody). Our Reader card: "Readers at home, twice over. Li Bai's readers knew every place; Pound kept the names unexplained, so English readers feel the distance too." Explained-o-meter: Author 0, Translator 0, Nobody 5.

4. **Russia. Anton Chekhov, "The Schoolmistress"** (Russian, 1897), translated by Constance Garnett, in The Schoolmistress and Other Stories (1920). Passage: from "The highroad was dry, a lovely April sun was shining warmly," to "...to get to the end of her journey as quickly as could be." (the builder ends at the first full stop after "quickly"). Setup: a village teacher rides home from town in a cart. Glowing words: **Marya Vassilyevna** (a first name and a name from her father, the polite Russian form; nobody; Britannica, "patronymic"); **highroad** (the main road between towns, unpaved, deep in mud after the thaw, as the story's puddles "like lakes" show; nobody); **her salary** (she has to ride to town herself to collect her pay, as the story says; nobody); **thirteen years** (a village teacher's life, poor and alone; nobody, the story itself shows it); **April** (the thaw comes late and suddenly in central Russia; the author, "spring had come all of a sudden"). Our Reader card: "Readers at home. Chekhov shows her tiredness from the inside and explains nothing about Russian village life, because his readers lived beside it." Explained-o-meter: Author 1, Translator 0, Nobody 4.

5. **Mexico. Mariano Azuela, The Underdogs** (Los de abajo, Spanish, 1915), translated by E. Munguía Jr. (Brentano's, 1929). Passage: Part One, chapter I, from "That's no animal, I tell you!" to "...vanishing into the impenetrable darkness of the night." with one cut, shown as "[...]": "said a man, who sat [...] eating," (removes a dated phrase in the translation). Setup: a farmer's family hears horses in the dark mountains. Glowing words: **soldiers** (here the government's federal troops, who hunted rebels during the Mexican Revolution, 1910 to 1920; nobody; Britannica, "Mexican Revolution" and "Mariano Azuela"); **sierra** (the mountain range, Spanish kept in English; nobody); **cantaro** (a clay water jar; nobody, the translator keeps the Spanish word); **tortillas** (flat corn bread, the daily food; nobody); **adobe** (sun-dried mud brick; nobody); **broad Mexican hat** (the translator's phrase for a sombrero, written for English readers; the translator). Our Reader card: "Readers at home, through a translator who now and then turns a Mexican thing into English words. Azuela, a doctor who rode with the revolutionaries, does not stop to explain." Explained-o-meter: Author 0, Translator 1, Nobody 5.

6. **West Africa (Igbo land, in present-day Nigeria). Olaudah Equiano, The Interesting Narrative of the Life of Olaudah Equiano** (English, London, 1789). Passage: from "We are almost a nation of dancers, musicians, and poets." to "...This is usually dyed blue, which is our favourite colour." (omit his footnote mark "[B]"). Setup: Equiano describes the home he says he was taken from as a child. Glowing words: **four divisions** (the author explains who dances in each); **stickado** (a kind of xylophone-like instrument Europeans knew; the author compares, "much like a stickado"); **guitar** (the author's comparison for a stringed instrument); **highland plaid** (a Scottish wrapped cloth his British readers knew well; the author compares); **callico, or muslin** (cotton cloths sold in Britain; the author). Our Reader card: "Readers far away. Equiano wrote in English for British readers, to turn them against the slave trade, so he explains his home in their terms." Context on the card, plainly: he was kidnapped and sold into slavery, bought his freedom in 1766 and campaigned for abolition; some historians, from baptism and navy records, think he may have been born in South Carolina, and others accept his account. Explained-o-meter: Author 5, Translator 0, Nobody 0.

7. **Norway. Henrik Ibsen, A Doll's House** (Norwegian, 1879), translated by R. Farquharson Sharp. Passage: Act III, Nora's speech from "It is perfectly true, Torvald. When I was at home with papa," through "That is what our marriage has been, Torvald." with Helmer's interruptions kept. Setup: at the end of the play, Nora tells her husband what their marriage has been. Glowing words: **papa's hands into yours** (a daughter passed from father to husband; the play's first audience knew that a wife could not borrow money without her husband's consent, as Mrs Linde says in Act I, and Nora's secret loan is the heart of the play; nobody); **doll-child** (Nora explains her own image); **from hand to mouth** (living with nothing of her own; nobody); **perform tricks** (in Act I Helmer calls her his skylark and his squirrel, like a pet; nobody, the play itself shows it); **great sin** (a strong word for a wife to use to her husband on stage in 1879; nobody). Our Reader card: "Readers at home, and it shocked them. Ibsen's first audiences knew these marriages from the inside; that is why the ending was argued over across Europe." Explained-o-meter: Author 1, Translator 0, Nobody 4.

## Interactions in detail
- Map: pins are buttons in reading order west to east (Mexico, Norway, West Africa, Russia, India, China, Japan); arrow keys move between them; Enter opens. Zoom is fixed; the map fits the stage.
- Glowing words: Tab moves through them; Enter opens the question card; Yes or No must be chosen before the card turns (the guess is kept and shown on the turned card: "You said: needed").
- Explained-o-meter: three segments with counts and words; screen readers hear "Author 5, translator 0, nobody 0".
- Show ours appears after a chip is chosen. Inside view saves on blur.
- Compare sorts by the share explained by Author plus Translator, most first; ties keep the map's west-to-east order.
- The question card turns over in 300 ms (instant with Motion off). Tapping another glowing word during the turn finishes this turn at once and opens the new word's card.
- Store: localStorage `atlas-work` (guesses, chips, Inside view text per pin), try/catch. Clear my work (after Yes) empties it.
- Sizes: at 1366x768 and 1280x720 the map fills the stage until a pin opens; then the map takes the left third and the reader the right two thirds, the passage scrolling inside its box (the picture strip is 96 px high). At 680x425 the reader covers the map with a Back to map button. At 760 and 375 wide the List view is the default and the map is a small strip at the top.

## Look
- `kit:theme-912` dark, accent `--brand #8ff05a` (atlas green: pins, glow underlines, header rule, buttons), `--btn #8ff05a`, brand text on brand `--brand-ink #1c1203`.
- Map: land `#1f2a36` with a `--line` coastline, sea `--paper`, graticule faint `#16202b`. Pins: a book icon in the accent with the author's name in `--ink`.
- Explained-o-meter segments with words and patterns: Author solid `#5aa9ff`, Translator striped `#ffcf5c`, Nobody outlined `--muted`.
- Neighbors: american-lit-timeline parchment (this group), portrait-in-four-media coral, premise-inspector citron (planned). Nearest catalog colors: `--gr-3` (dE 45), `--ok` (dE 46); green on dark is new among 9-12 ELA tools.
- Contrast (WCAG 2.1): brand on paper `#0d1219` 13.22:1, on panel 12.18:1, on sec-bg 11.54:1; brand-ink on brand 13.00:1; brand on land `#1f2a36` 10.3:1 or better (builder recheck); Author `#5aa9ff` on sec-bg 6.68:1; Translator `#ffcf5c` on sec-bg 11.19:1. All pass AA.

## Art
Local FLUX (`scripts/localart.py`), no people, house style "still life and landscape painting, soft natural light, rich earthy colors". 7 images, one per pin: each shows a thing named by one of that passage's glowing words, the kind of thing a first reader at home never needed explained. All 16:9; cutout no; people no; the strip at the top of that pin's reader (cropped to 96 px high, centered) and full size in that word's turned card. The map outline reuses art-passport's `world.json` (Natural Earth 1:110m land, public domain); pins, icons, the meter and preview.svg (the map with three pins and a reader card) are drawn in code. No portraits of the authors.
- wla-cabul-fruit (Tagore, "Cabuliwallah"): a loose cloth bundle opened on a wooden step, heaped with dried apricots, raisins, almonds and pistachios, a brass weighing scale beside it.
- wla-sasa-ame (Sōseki, "sasa-ame"): small pale rice jellies wrapped in fresh green bamboo leaves and tied with straw, on a plain wooden tray.
- wla-river-gorge (Li Bai, "Ku-to-Yen"): a narrow river gorge between towering cliffs, fast swirling water and rocks, a small wooden boat with a curved roof near the bank, morning mist.
- wla-spring-road (Chekhov, "highroad"): a wide unpaved country road in early spring, deep mud and puddles like small lakes, a wooden cart with one horse standing at the side, bare birch trees and patches of old snow.
- wla-cantaro (Azuela, "cantaro"): a round red clay water jar with a narrow neck standing beside a sun-dried adobe wall, a stack of tortillas wrapped in cloth on a bench, dark mountains at dusk behind.
- wla-stickado (Equiano, "stickado"): a wooden West African xylophone with gourd resonators hung beneath its keys, two beaters, and a folded length of indigo-dyed cotton cloth beside it.
- wla-parlor (Ibsen, "papa's hands into yours"): a cozy 1870s Norwegian parlor at Christmas, a decorated fir tree, a piano, a stove, and a closed door with a small brass letter box.

## Voice
Bank voice `upbeat-guide` (Zephyr), style "Say brightly and clearly, like an upbeat tour guide". `Curio.voice`, scope the pin.
- welcome (how; on first open; stale once a pin opens): "Seven stories, seven places. Tap a pin on the map, or a card in the List."
- glow (how; the first passage opened; stale once a glowing word is tapped): "Tap a glowing word. Then tap Yes or No: would a reader there and then need it explained?"
- turned (how; the first card turned; stale when the next glowing word is tapped): "Now see who explained it: the author, the translator, or nobody."
- meter (event; each Explained-o-meter completed; stale when a Reader card chip is tapped or another pin opens): "That's the pattern. Tap the chip that says who this was written for."
- compare (how; the first Compare; stale when Compare closes): "Line them up. Who explains the most, and why?"
- missing (how; when the seventh pin is read; stale when any pin opens): "That's all seven. Which part of the world is missing? Say which story you'd add."

## Family engine
none

## Sources
- Tagore: The Hungry Stones and Other Stories (London: Macmillan, 1916), Project Gutenberg eBook #2518, https://www.gutenberg.org/ebooks/2518 ; Britannica, "Rabindranath Tagore" and "Kabul".
- Sōseki: Botchan (Master Darling), translated by Yasotaro Mori (Tokyo: Ogawa Seibundo, 1918), Project Gutenberg eBook #8868, https://www.gutenberg.org/ebooks/8868 ; Britannica, "Natsume Sōseki," "Botchan," "Hakone," "Niigata".
- Li Bai and Pound: Ezra Pound, Cathay (London: Elkin Mathews, 1915), Project Gutenberg eBook #50155, https://www.gutenberg.org/ebooks/50155 ; Britannica, "Li Bai" and "Cathay"; Poetry Foundation, "The River-Merchant's Wife: a Letter," https://www.poetryfoundation.org/poems/47546/the-river-merchants-wife-a-letter (place names).
- Chekhov: The Schoolmistress and Other Stories, translated by Constance Garnett, Project Gutenberg eBook #1732, https://www.gutenberg.org/ebooks/1732 ; Britannica, "Anton Chekhov" and "patronymic".
- Azuela: The Underdogs, translated by E. Munguía Jr. (New York: Brentano's, 1929), Project Gutenberg eBook #549, https://www.gutenberg.org/ebooks/549 ; Britannica, "Mariano Azuela" and "Mexican Revolution".
- Equiano: The Interesting Narrative of the Life of Olaudah Equiano (1789), Project Gutenberg eBook #15399, https://www.gutenberg.org/ebooks/15399 ; Britannica, "Olaudah Equiano" (kidnapping, freedom bought in 1766, abolition work, the birthplace debate).
- Ibsen: A Doll's House, translated by R. Farquharson Sharp, Project Gutenberg eBook #2542, https://www.gutenberg.org/ebooks/2542 ; Britannica, "A Doll's House" (the 1879 premiere and the debate over the ending); the loan rule is quoted from the play itself (Act I).
- Map: Natural Earth 1:110m land, public domain, https://www.naturalearthdata.com/ (as in art-passport).
- Standards: CCSS ELA RL.9-10.6, https://www.thecorestandards.org/ELA-Literacy/RL/9-10/
- Number checks (Python, 2026-10-29), the Explained-o-meters recounted from each glowing word's "who explained it": Tagore 2, 0, 3; Sōseki 0, 1, 4; Li Bai 0, 0, 5; Chekhov 1, 0, 4; Azuela 0, 1, 5; Equiano 5, 0, 0; Ibsen 1, 0, 4; all as stated, each pin 5 or 6 words (within 4 to 6). Compare shares (Author plus Translator over words): Equiano 1.00, Tagore 0.40, Chekhov 0.20, Sōseki 0.20, Ibsen 0.20, Azuela 0.17, Li Bai 0.00; three pins tie at 0.20, so the sort now names its tie rule (map order, west to east: Ibsen, Chekhov, Sōseki).
Every passage boundary above was checked against its Gutenberg file on 2026-10-27; the builder copies the text between the stated first and last words exactly.

## Done when
1. Seven pins open seven passages that match their editions word for word, with the stated cuts and omitted marks, and "--" for em dashes (Chekhov's "always--invariably--longed" shows as printed).
2. Each passage shows its glowing words; a card cannot turn before Yes or No.
3. Explained-o-meters match Content: Equiano Author 5, Translator 0, Nobody 0; Botchan 0, 1, 4; Pound 0, 0, 5.
4. Tapping "father-in-law's house" in Tagore lights the narrator's explaining sentence in the passage.
5. Show ours appears only after a chip; Inside view keeps up to 240 characters.
6. Compare with two read pins sorts them by share explained and shows each Reader card sentence; with Chekhov, Sōseki and Ibsen read, the order is Ibsen, Chekhov, Sōseki.
7. Focus: at 1366x768 and 680x425 the map fills the stage before a pin opens; with a pin open the passage is the largest thing on screen.
8. A tap during a card turn: tapping a second glowing word mid-turn opens its card at once with no lost tap.
9. Reload keeps work per pin; Clear my work (after Yes) empties it; no network (the map and images are bundled); console clean.
10. At every size in STANDARDS.md the pins or List cards are reachable and the reader opens without page scroll; 375 wide works in `drive.py --host`.
11. All 7 images load, show no person and match their glowing word; each how line plays once and names an enabled control.

## Open questions
- [world-lit-atlas] Equiano's passage is from a narrative of enslavement (this excerpt describes his home, not the slave ship); the card states his kidnapping and the birthplace debate plainly. Anything a parent might want to see first?
- [world-lit-atlas] The Underdogs cut removes the translation's phrase "Indian-fashion" ("sat cross-legged"). Cut it as planned, or keep it with a gloss on dated wording?
- [world-lit-atlas] No pin yet for the Middle East, South America or Oceania (the tool asks students which story they would add). Add pins in a later pass? Candidates must be public domain in the US (published before 1930) with a pre-1930 English translation.

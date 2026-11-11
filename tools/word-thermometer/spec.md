# Word Thermometer

## One idea
The student lines up near-synonyms on a thermometer from warm praise at the top to cold insult at the bottom (thrifty, frugal, careful, cheap, stingy), defending each placement with a context card, then swaps them into a story about a shopkeeper and a news paragraph about a city budget and watches a tone gauge move while the facts stay the same, and finally rewrites one passage twice, once to make readers admire a character and once to make them dislike her, changing only five words, so they learn that words with the same meaning carry different feelings and that writers choose them on purpose.

## Not like
- double-meanings (8, concept): puns, irony and allusions. Here connotation, grade 6.
- tone-dial (10, concept): rewriting a scene in five tones. Here single-word swaps that shift tone.
- rhetoric-spotter (9, concept): persuasive appeals. Here word feelings.
- simile-slam (5, spec): figurative comparisons. Here near-synonyms and their heat.
- perspective-camera (6, spec): narrator judgment words in a scene. Here building and testing a scale of word feelings.

## Who and how
- Grade 6, ELA, module "Connotation and Context" (Language and Reading). Standards: L.6.5 (a, b, c), RL.6.4, RI.6.4. (L.6.4 word-solving strategy belongs to context-roots-dictionary.)
- Driver: one student; class mode is a shared thermometer (tool.json `driver: "student"`). Role: lesson. Every word and sentence is read on tap.
- Change note (spec fix, 2026-11-10): the thermometer, Gale and the six sets stay. Added: Gale places one set first as the model; a set is now tested as a whole and the student writes how two of its words differ; eight figures of speech (three personification) whose meaning the student types before placing; six relationship cards, with cause and effect and part and whole, each with a check; in every passage the student works out two words from context and one figure of speech before any swap; the gauge is hidden until the student predicts, and hidden during the rewrite; four more story passages and four more information paragraphs, one with technical words; a written line on how the words changed the tone. One part a sitting.
- Six word sets, eight figures, six relationship cards, ten passages (five story, five information), then the two-way rewrite. tool.json `modes: ["Solo", "Class thermometer"]`, `minutes: "20-30"`, `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the rewrites side by side. The class thermometer keeps counts only while the page is open.
- Change note (hooks, 2026-11-11): Added the three hooks: the last items of each kind are done on your own with the end screen by code, English learner supports, access.
- English learners: every spoken line is also on screen in short sentences. The words connotation, figure of speech, personification, context and tone each show with an example from Gale's model the first time they are used. The written line offers a frame the student may take or leave: "__ feels stronger than __ because __."

## Standards map
| Code | The standard's verb and its parts | Who does the verb | Student action that teaches it | Items that differ | What they see | Done when check |
|---|---|---|---|---|---|---|
| L.6.5c | distinguish among the connotations of words with similar denotations | the student | Place five near-synonyms, test the set as a whole, then write how two of them differ | 6 sets of 5 | the scale with words at their heat | 2 |
| L.6.5a | interpret figures of speech (such as personification) in context | the student | Read the phrase in its sentence, type what it means in plain words, pick the closest meaning, then place it | 8 (3 personification) | the phrase in its sentence and on the scale | 3 |
| L.6.5b | use the relationship between particular words (cause and effect, part and whole, item and category) to better understand each word | the student | Pick the relationship between a known word and a hard word, then type what the hard word must mean | 6 | the relationship chip and the student's meaning | 4 |
| RL.6.4 | determine the meaning of words and phrases as used in a text, including figurative and connotative meanings; analyze the impact of a specific word choice on meaning and tone | the student | In each story work out two words from context and one figure; predict each swap's effect before the gauge shows; write how one word changed the tone | 5 stories | the story with swapped words and the gauge | 5, 6 |
| RI.6.4 | determine the meaning of words and phrases as used in a text, including figurative, connotative and technical meanings | the student | In each paragraph work out two words from context (one technical where the text has them) and one figure; predict each swap before the gauge shows | 5 paragraphs | the paragraph, the gauge and a fact list that doesn't change | 5 |

## Screens and modes
Header (kit): title "Word Thermometer"; `Scale`, `Passages`, `Rewrite`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A tall glass thermometer on a wall, warm and sunny at the top (Admiring), cool and frosty at the bottom (Insulting), a neutral band in the middle, and a bin of five tiles. A little weather vane rooster named Gale stands on top. First hint: "Tap a word tile to hear it." The first tap says the word; the welcome is queued after it (`welcomeAfter: true`).

**Gale goes first (the model).** Gale places one set alone: scent, aroma, smell, odor, stench. For each she says where and why ("You'd thank someone for an aroma. Nobody thanks you for a stench."), then writes one line on two of them: "Smell and stench both mean something your nose picks up, but stench says it is awful." It cannot be skipped the first time and `Gale's set` reopens it.

**Scale.** Six sets: doesn't spend much (thrifty, frugal, careful, cheap, stingy); talks a lot (chatty, talkative, outgoing, wordy, loudmouthed); sure of themselves (confident, self-assured, bold, cocky, arrogant); thin (slender, slim, lean, skinny, scrawny); curious (inquisitive, curious, interested, nosy, prying); old (antique, vintage, old, dated, decrepit). The student drags tiles onto the scale; each placement asks for a context card from three ("You'd call your grandmother this to her face", "You'd say this when you're annoyed", "A news report would use this"). The key gives each word a heat band (warm, mild, neutral, cool, cold). Nothing is judged while tiles move. `Check the set` tests all five at once: a tile within one band of its key stands, since the bands are a reading. If any tile is two or more bands off, the first check says only how many; the second asks about each one ("Would you say {stingy} to her face?"). A tile still two bands off after that is moved by Gale and tagged "Gale moved it". Then the student picks two words from the set and writes one line in a frame, "{thrifty} and {stingy} both mean ___, but {stingy} ___", beside Gale's model line and a two-box guide: says what they share; says what feeling the second one adds.

**Figures.** Eight phrases, each shown first in a sentence. The student types what it means in plain words, then picks the closest of three meanings (one takes it word for word, one misses the feeling). A wrong pick can be tried once more; then Gale explains and the phrase is tagged "Gale explained". For the three personification items the student also taps the thing that is being treated as a person. Then the phrase goes on the scale.

**Relationships.** Six cards. Each gives a word the student knows, a hard word and a sentence using both. The student picks the relationship from five chips (opposite; a kind of; a stronger form of; cause and effect; part and whole), then types what the hard word must mean and picks the closest of three meanings. A wrong chip can be tried once more; after a second miss Gale names it and a spare card of the same kind is added.

**Passages.** Five stories and five information paragraphs, 100 to 200 words each. Each opens with Word work, before any swap: two words the passage does not explain are underlined. For each the student taps the nearby words that give it away, types a meaning and picks the closest of three; then does the same for one figure of speech in the passage. One retry, then "Gale explained". After Word work, three highlighted slots (five in the Mrs. Alvarado story and the council paragraph) take any word from that slot's set, shown in mixed order. Before the tone gauge (admiring to scornful) moves, the student taps `warmer`, `cooler` or `no change`; then the gauge shows. A wrong call is counted on the passage's card. A fact list beside the passage (what she did, what the council voted) never changes.

**Rewrite.** On the Mrs. Alvarado story and one other story of the student's choice, the student writes two versions by changing five words: Admire and Dislike. The gauge is covered while they work and slot words are in mixed order. `Test both` then shows the two side by side with the facts lit in both and the five changed words underlined. They must sit at least two bands apart on average; if not, the tool says how far apart they are and the student changes words and tests again, and the number of tests is printed. Last, the student writes two sentences: which one word did the most to change how a reader feels, and how. A guide: names the word; says the feeling it brings; says the facts stayed the same.

**Class thermometer.** One contested word ("cheap"); each student taps where they'd place it on the projector; the spread shows.

At 1366x768 the thermometer and passage fit side by side; at 680x425 the thermometer is a slim column beside the passage.
**On your own.** The last two word sets, the last two figures, the last two relationship cards, the fifth story and the fifth paragraph run with Gale quiet: no model, no list of meanings to pick from (the meaning is typed), no hints, and one Check for each.

**Results strip (on the end screen).** For the teacher: for each of L.6.5a, L.6.5b, L.6.5c, RL.6.4 and RI.6.4, how many of its items on your own were right, in numbers and words, with each one missed and what the student placed or typed. It prints with the rest.

## Content
Written for Curio Class: six word sets with heat bands and context-card keys, and the model set (scent, aroma, smell, odor, stench).
- Figures, each in a sentence with three meanings keyed: "a heart of stone"; "tight-fisted"; "a fountain of ideas"; "a sharp tongue"; "time crawled"; and personification: "the wind whispered through the pines"; "the old house groaned"; "the alarm clock screamed".
- Relationship cards (known word, hard word, relationship): stingy, miser (a kind of); thrifty, spendthrift (opposite); rain, torrent (a stronger form of); drought, famine (cause and effect); carelessness, mishap (cause and effect); poem, stanza (part and whole). Spares: sprout, seed (cause and effect); play, prologue (part and whole); tool, chisel (a kind of).
- Stories (narrator describing someone or somewhere): Mrs. Alvarado, a shopkeeper (about 200 words); Coach Bell at practice; Uncle Dev and his truck; Wren, the new girl on the bus; the house at the end of Pike Street. People and places are made up.
- Information paragraphs: a city council's budget vote (about 150 words); a volcano explainer with technical words (dormant, vent, magma); a game report; a storm bulletin (technical: gust, advisory); a museum label for an old loom. All made up and labeled, except the volcano terms, which follow their dictionary meanings.
- Each passage carries in data: two context words with their clue words and three meanings, one figure with three meanings, its slots and sets, and its fact list.
- On your own, with what each common wrong answer means:
  - L.6.5c: words placed by how long or how rare they are, not by feeling, mean the student is ranking difficulty and not connotation.
  - L.6.5a: a meaning that reads the phrase word for word ("the wind was shouting") means the figure was not seen as a figure.
  - L.6.5b: naming the relationship rightly but giving no meaning for the hard word means the link is seen and not yet used.
  - RL.6.4 and RI.6.4: giving a word's most common meaning where the text uses another means the student is not reading the sentences around it; a word-choice answer that only repeats the definition means meaning and effect on tone are not yet apart.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- With Motion off the mercury jumps.
- Heat bands are the key's reading; the tool says so ("most readers feel {cocky} as cool") and accepts the student's placement with a card.
- Access: every action works by tap and by keyboard. Words and phrases can be dragged, or picked with a tap and placed with a tap, or moved along the scale with arrow keys. Heat is shown by height and a number on the scale, never color alone. Motion can be paused.
- On your own: one answer each, no feedback until the last part is in.

## Look
- Accent `--brand` #b02a2a thermometer red (header, mercury, gauge needle); gold #f4c542 (the warm band, swapped words); paper #fcf3f3; ink #2b0909; muted #6a5050. Scene: a sunny porch wall with frost at the bottom.
- Contrast (WCAG 2.1, computed): white on brand 6.54:1; brand on paper 6.00:1; ink on paper 16.80:1; muted on paper 6.69:1; ink on gold 11.27:1.
- Never color alone: bands are labeled in words; the gauge has words at both ends.
- Different from this batch (lab teal, x-ray blue, night indigo, desk brown).

## Art
- People art goes to Gemini: Mrs. Alvarado (a Mexican American woman in her sixties behind a hardware store counter), 2 pictures (warm and cool light on the same scene); "children's book illustration <scene>, warm gouache, no text"; 4:3.
- Local FLUX (`scripts/localart.py`): thermometer wall (1); Gale (4 poses: point, shiver, sunbathe, think), "A friendly weather vane rooster character <pose>, soft gouache, plain white background"; 1:1; cutout yes; city hall meeting room with no people (1).
About 8 images. Drawn in code: thermometer, tiles, gauge.

## Voice
Bank voice `warm-teacher` as Gale (unique in this batch); the story is read by `gentle-storyteller` and the news paragraph by `news-reader` (each unique in this batch). `Curio.voice` with `scope: () => state.view + ':' + state.set + ':' + state.word`, `welcomeAfter: true`.
- event `word`: the tapped word.
- how `welcome`: "These words all mean nearly the same thing. But they don't feel the same. Put them where they belong."
- event `askCard`: "Would you say {stingy} to her face?"
- event `gauge`: "Same facts. Now readers feel {scornful}."
- event, whole, `passage`: the passage with the student's words.
- how `rewriteHow`: "Change five words. Make us admire her. Then make us dislike her."
- how `checkSet`: "Place all five. Then tap Check the set."
- how `meaning`: "Type what it means in plain words. Then pick the closest one."
- how `relate`: "Pick how the two words go together."
- how `clues`: "Tap the words nearby that give it away."
- how `call`: "Will that make it warmer, cooler or no change? Tap one."
- event, whole, Gale's set.
Read speaks the hint, which names the next action and control and never a disabled one.
- how `own`: "These last ones are on your own. Type what you think. I will stay quiet."
Every `how` line is also shown as text beside its control. Instructions use no idioms.

## Family engine
None. Tool-only code: heat scale with keyed bands, context cards, passage slots with a tone gauge, two-version rewrite.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Scale | Put tiles anywhere; nudge until the question stops | The set is tested whole and the first check gives only a count; a tile still far off is moved and tagged, and the print shows it. |
| Differ line | Type filler | The tool cannot judge it; Gale's model, the guide and the printout carry it. |
| Figures and context words | Pick meanings until one sticks | The meaning is typed first; three choices with one retry, then a "Gale explained" tag. |
| Relationships | Tap chips until right | Five chips; a second miss adds a spare card. |
| Passages | Swap and watch the gauge | The gauge stays still until the student calls the direction; wrong calls are counted. |
| Rewrite | Watch the gauge and tune; change facts | The gauge is covered and words are in mixed order until `Test both`; tests are counted; changing a fact is flagged "That changes what happened." |
| On your own | Retry until right; lean on the hints | One answer each, no hints or models, and nothing is marked until all are in. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. First visit: Gale's set (whole). Tap a tile: `word`, `welcome` (queued, first time). `checkSet`.
2. Placements: `askCard` on a second check. Figures: `meaning`. Relationships: `relate`.
3. Passages: `clues`, `meaning`; `call` before each swap, then `gauge`; `passage` on Play.
4. Rewrite: `rewriteHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.6.5, RL.6.4, RI.6.4 wording | thecorestandards.org, Grade 6 | CCSS ELA 2010 PDF | yes |
| Connotation is the feeling a word carries beyond its dictionary meaning | Merriam-Webster, connotation | Purdue OWL, diction and connotation | yes |
| Meanings of the near-synonyms and phrases (thrifty, frugal, stingy, miser, tight-fisted, a heart of stone, and others) | Merriam-Webster, each entry | Cambridge Dictionary, each entry | yes |
Backed twice: 3. Cut: 0.

Design choices (not claims): the heat bands are a reading, labeled as one on screen.

Checks run (Python, scratchpad b19, 2026-11-09): every sample set has a word in at least four of the five bands; a sample admire and dislike rewrite differs by at least two bands on average; contrast as in Look.

Spec fix checks (2026-11-10): counted, not run: 8 figures of which 3 are personification; 6 relationship cards cover all five chips with 3 spares; 5 stories and 5 paragraphs, each with 2 context words and 1 figure, give 20 context words and 10 figures. The new words' meanings (torrent, famine, mishap, stanza, prologue, chisel, dormant, vent, magma, gust, advisory) fall under the dictionary row above and were not looked up again in this pass.

## Done when
1. Focus and fold: at 1366x768 thermometer and passage fit; at 680x425 the thermometer is a slim column.
2. Six sets place with context cards and are tested whole; each ends with the student's line on how two words differ. (L.6.5c)
3. Eight figures, three of them personification, take a typed meaning and a keyed pick before they are placed. (L.6.5a)
4. Six relationship cards take a chip and a typed meaning; a second miss adds a spare. (L.6.5b)
5. Each of ten passages opens with two context words and one figure; each swap needs a call before the gauge moves; facts stay. (RL.6.4, RI.6.4)
6. The two-way rewrite is done on two stories with the gauge covered, needs five changes and a clear difference, and ends with two sentences on tone. (RL.6.4)
7. Gale's set plays first and can be reopened.
8. The class thermometer shows the spread and keeps nothing after closing.
9. Print shows the rewrites, the written lines and any tags.
10. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
11. Motion off: the mercury jumps; no network requests.
12. The last two sets, figures and cards and the fifth story and paragraph run with no model, choices or hints and one Check each; the end screen shows the result for each of the five codes. (L.6.5a, L.6.5b, L.6.5c, RL.6.4, RI.6.4)
13. Every spoken instruction is also on screen; each key word shows with a picture or example at first use; any sentence frame can be left.
14. Every action works by keyboard as well as tap, drags have a tap way, nothing is shown by color alone, and motion can be paused.

## Open questions
- None for Cory.

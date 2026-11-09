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
- Driver: one student; class mode is a shared thermometer (tool.json `driver: "student"`). Every word and sentence is read on tap.
- Six word sets, two passages, then the two-way rewrite. tool.json `modes: ["Solo", "Class thermometer"]`, `minutes: "20-30"`, `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the rewrites side by side. The class thermometer keeps counts only while the page is open.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.6.5c | Place near-synonyms on the thermometer and pick a context card for each | the scale with words at their heat | 2 |
| L.6.5a | Read figurative phrases in a sentence first ("a heart of stone", "tight-fisted"), then place them | the phrase in its sentence and on the scale | 3 |
| L.6.5b | Name a relationship to place a hard word (stingy and generous are opposites; a miser is a kind of stingy person) | the relationship chip | 3 |
| RL.6.4 | Swap words into the story; the tone gauge moves | the story with swapped words and the gauge | 4 |
| RI.6.4 | Swap words into the news paragraph; see how readers judge the same facts | the paragraph, the gauge and a fact list that doesn't change | 4 |
| RL.6.4, RI.6.4 | Rewrite one passage twice (admire and dislike) by changing five words | two versions side by side with the facts lit | 5 |

## Screens and modes
Header (kit): title "Word Thermometer"; `Scale`, `Passages`, `Rewrite`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A tall glass thermometer on a wall, warm and sunny at the top (Admiring), cool and frosty at the bottom (Insulting), a neutral band in the middle, and a bin of five tiles. A little weather vane rooster named Gale stands on top. First hint: "Tap a word tile to hear it." The first tap says the word; the welcome is queued after it (`welcomeAfter: true`).

**Scale.** Six sets: doesn't spend much (thrifty, frugal, careful, cheap, stingy); talks a lot (chatty, talkative, outgoing, wordy, loudmouthed); sure of themselves (confident, self-assured, bold, cocky, arrogant); thin (slender, slim, lean, skinny, scrawny); curious (inquisitive, curious, interested, nosy, prying); old (antique, vintage, old, dated, decrepit). The student drags tiles onto the scale; each placement asks for a context card from three ("You'd call your grandmother this to her face", "You'd say this when you're annoyed", "A news report would use this"). The key gives each word a heat band (warm, mild, neutral, cool, cold); a placement two bands off asks "Would you say {stingy} to her face?" and the student may keep their placement with a card.

**Figurative and relationships.** Later sets add phrases ("a heart of stone", "tight-fisted", "a fountain of ideas") shown first in a sentence, and hard words (miser, spendthrift) placed by naming a relationship to a word already on the scale (opposite of, a kind of, a stronger form of).

**Passages.** The story (about 200 words): a narrator describing Mrs. Alvarado, a shopkeeper. The news paragraph (about 150 words): a city council's budget vote. Five highlighted slots in each take any word from that slot's set. A tone gauge (admiring to scornful) moves with the average heat; a fact list beside the passage (what she did, what the council voted) never changes.

**Rewrite.** The student writes two versions of the story by changing five words: Admire and Dislike. The two sit side by side with the facts lit in both and the five changed words underlined.

**Class thermometer.** One contested word ("cheap"); each student taps where they'd place it on the projector; the spread shows.

At 1366x768 the thermometer and passage fit side by side; at 680x425 the thermometer is a slim column beside the passage.

## Content
Written for Curio Class: six word sets with heat bands and context-card keys; figurative phrases with sentences; the story and news passages with slots; relationship chips.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- With Motion off the mercury jumps.
- Heat bands are the key's reading; the tool says so ("most readers feel {cocky} as cool") and accepts the student's placement with a card.

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
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: heat scale with keyed bands, context cards, passage slots with a tone gauge, two-version rewrite.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Scale | Put tiles anywhere | Two-band misses ask a question; the print shows placements beside the key. |
| Passages | Swap at random | The gauge reads the swaps back; the rewrite needs a clear admire and dislike difference (at least two bands apart on average). |
| Rewrite | Change facts | The fact list lights; changing a fact is flagged "That changes what happened." |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a tile: `word`, `welcome` (queued, first time).
2. Placements: `askCard` as it fires.
3. Passages: `gauge` per swap; `passage` on Play.
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

## Done when
1. Focus and fold: at 1366x768 thermometer and passage fit; at 680x425 the thermometer is a slim column.
2. Tiles place with context cards and two-band questions. (L.6.5c)
3. Figurative phrases and relationship chips work. (L.6.5a, L.6.5b)
4. Passage swaps move the gauge; facts stay. (RL.6.4, RI.6.4)
5. The two-way rewrite needs five changes and a clear difference.
6. The class thermometer shows the spread and keeps nothing after closing.
7. Print shows the rewrites.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: the mercury jumps; no network requests.

## Open questions
- None for Cory.

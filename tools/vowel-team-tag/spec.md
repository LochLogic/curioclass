# Vowel Team Tag

## One idea
On a playground maze, each vowel team is a pair of letter kids holding hands (the Train team is a and i, the Coat team is o and a), and the child steers one team at a time to tag only the words it belongs in: a team that runs into a word gap fills it, and the right team makes a real word that is said out loud while the wrong one makes a jumble that fizzles, so the child learns which letters team up to say which long vowel; later gates split long words into syllables and peel off prefixes and suffixes before the team reads, and a rule-breaker wall holds the words no team can read.

## Not like
- blend-bakery (1, spec): blending single-syllable words from sound jars, with magic-e and vowel-team counters. Here grade 2: choosing between teams that make the same sound, two-syllable words, affixes for decoding, and odd patterns, as a steering race.
- nonsense-words (2, built): a calm drill of made-up words. Here real words, picked by spelling pattern.
- sight-words (2, built): Dolch and Fry practice. Here the rule-breaker wall is one level, framed as words no team can sound out.
- word-lab (2, spec): affixes for meaning. Here affixes peeled off for reading.
- syllable-surgeon (3, concept): multisyllable and Latin suffixes. Here two syllables and common affixes.

## Who and how
- Grade 2, ELA, module "Long Vowels and Two-Syllable Words" (Foundational Skills). Standard: RF.2.3 (a to f).
- Driver: one student (tool.json `driver: "student"`). Keyboard arrows, a tap on the direction pad, or dragging the team steers it. Every word is said on tag and on tap; the child echoes it aloud (no microphone, no checking).
- Six levels: `Short or Long`, `Vowel Teams`, `Two Syllables`, `Prefix and Suffix Gates`, `Odd Patterns`, `Rule-Breaker Wall`. A `Race` switch adds a timer and a ghost of the best run on this device. tool.json `modes: ["race"]`, `minutes: "10-20"`, `grades_label: "Grade 2"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RF.2.3a | Short or Long: the Magic-e team tags only the platforms whose picture shows the long word (cape, not cap) | platform with a picture and a gap | 2 |
| RF.2.3b | Vowel Teams: steer one team (ai, ay, ee, ea, oa, ow) to tag only its words | gap words with pictures; a fizzle for the wrong team | 3 |
| RF.2.3c | Two Syllables: tap the split gate where the word breaks, then each part is read | the word cut in two | 4 |
| RF.2.3d | Prefix and Suffix Gates: the gate peels off the affix; tap the base word, then hear the whole word | the affix in a different shape | 5 |
| RF.2.3e | Odd Patterns: sort ea and ow words by the sound they make (head and leaf; cow and snow) | two slides, each with a picture key | 6 |
| RF.2.3f | Rule-Breaker Wall: hear a word, tag it among look-alikes | the wall of bricks | 7 |
| RF.2.3b | End sort board: every tagged long e word grouped by spelling (ee, ea, e with a magic e) | the sort board | 8 |

## Screens and modes
Header (kit): title "Vowel Team Tag"; `Levels`; `Race`, `Read`, `Motion`, `Sound`. Controls 60 px or more at 1366x768 (44 px at 680x425), icon plus word. The direction pad (four 72 px arrows) sits bottom right.

**On load and first tap.** The playground gate with Coach Kit the kangaroo and a whistle. First hint: "Tap a level to start." The first tap opens the level with its line; the welcome is queued after it (`welcomeAfter: true`).

**The maze.** Focus: a playground maze (1100 x 560 at 1366x768; slides, swings and sandboxes are the walls) with 8 to 12 word platforms. Each platform shows a picture and a word with a gap (tr _ _ n). The team (two letter kids holding hands, 64 px) starts at the gate. Steering moves the team one path cell per step. Running into a platform tags it:
- Right team: the gap fills, the platform lights, the word clip plays ("train"), and the hint says "Say it too!" The team's sound clip (a clean recorded long vowel) plays first, then the word.
- Wrong team: the letters jumble and fizzle with a soft buzz; the gap stays empty; Coach says "That doesn't make a word. This one needs another team." No made-up word is ever said.
Tagging every right platform opens the next team's gate.
**Race.** With Race on, a timer runs and a faint ghost team replays the best run on this device. Wrong tags add 3 s. Best times are kept in localStorage per level (wrapped in try/catch; without storage there is no ghost). Race off: no timer at all.

**Levels.**
1. Short or Long: the Magic-e team (a tall e with a wand). Platforms: cap, cape, kit, kite, hop, hope, tub, tube, pin, pine, cub, cube. Each shows its picture and the word without an e plus a gap. Tag only those whose picture shows the long word.
2. Vowel Teams: six runs (Train team ai, Clay team ay, Sheep team ee, Wheat team ea, Coat team oa, Snow team ow), one at a time; each maze holds its team's four words and eight words from other teams.
3. Two Syllables: platforms hold whole two-syllable words; tagging opens the split gate: the child taps between letters where the word breaks; right: each part is read, then the whole word.
4. Prefix and Suffix Gates: gates on the path hold re-, un-, -ful, -less, -er, -ly; a word passing through gets its affix peeled into a different shape (a tag hanging off the word); the child taps the base word; it is read, then the affix, then the whole word with what it means ("re- means again: repaint, paint again").
5. Odd Patterns: two slides, one with a picture key of a long sound (leaf; snow) and one of another sound (head; cow); words slide down when steered to the right slide: head, bread, thread, sweat (ea short) and leaf, seat, dream, peach; cow, town, now, owl and snow, bowl, crow, grow.
6. Rule-Breaker Wall: a word is said; three bricks show it and two look-alikes; steer to the right brick. Words: said, again, because, could, would, does, were, two, friend, people.

**Sort board.** After Vowel Teams and Short or Long: a board with three columns for the long e sound (ee, ea, e with a magic e: these, eve) and every tagged word placed; Coach says "Three spellings, one sound!"

At 1366x768 the maze and pad fit above the fold. At 680x425 the maze scales to 640 x 330.

## Content
**Vowel Teams words** (picked so only one team makes a real word in each gap; easy words like rain, tree, boat and road are left out because another team also makes a word there: roan, tray, beet, reed): ai: train, chain, snail, paint. ay: clay, sway, crayon, hooray. ee: sheep, cheek, sleep, teeth. ea: seat, dream, beak, wheat. oa: coat, toast, cloak, foam. ow: snow, blow, yellow, window.
**Two Syllables:** rainbow (rain|bow), sailboat (sail|boat), seaweed (sea|weed), railway (rail|way), peanut (pea|nut), oatmeal (oat|meal), daydream (day|dream), snowman (snow|man).
**Gates:** repaint, reload, replay, unseen, unload, playful, painless, sweetly, teacher, speaker.
**Sound clips** (recorded separately as clean isolated long vowel sounds, plus every word as a whole-word clip): the long vowels for each team, short e and the /ow/ in cow for Odd Patterns, and every word above. Voice lines never say a letter name or sound; the teams are called by their names (the Train team) and the sound comes from the clip.

## Interactions in detail
- Every tap acts at once; a new clip or line stops the old one.
- Steering: held arrows repeat every 160 ms; the pad and drag step one cell per tap; the team cannot pass walls.
- A tagged platform can be tapped again to hear the word.
- Split gate: taps between any two letters; a wrong split reads the two pieces ("rai" "nbow" are never read; Coach says "Try a split between the two parts you can read") and lets the child try again.
- Odd Patterns slides take each word once; a wrong slide plays the word and Coach asks "Does it sound like {leaf}?"
- Levels unlock in order but all are open after the first is done; a teacher can open all from `Levels` with one confirm.

## Look
- Accent `--brand` #b3461a playground orange (header, team jerseys, gates); gold #f4c542 (lit platforms, stars); paper #fff8f0; ink #2a160b; muted #6b5547. Each team wears its own jersey pattern (stripes, dots, stars, zigzags, checks, waves) and number.
- Contrast (WCAG 2.1, computed): white on brand 5.52:1; brand on paper 5.24:1; ink on paper 16.37:1; muted on paper 6.61:1; ink on gold 10.60:1.
- Never color alone: teams differ by jersey pattern and their letters; right and wrong tags differ by the filled gap versus the fizzle and a word line; affixes hang as tags.
- Different from this batch (rain blue, wine table, velvet red, lab purple).

## Art
Local FLUX (`scripts/localart.py`); no people (the letter kids are drawn in code).
- playground (1): "A bright top-down cartoon playground with slides, swings and sandboxes forming a maze, soft gouache, no text"; 16:9; cutout no.
- Coach Kit (3, whistle, cheer, point): "A sporty kangaroo coach with a whistle <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- word pictures (about 70): "<a train / a chain / a snail / ...>, simple soft gouache icon, plain white background"; 1:1; cutout yes.
About 74 images. Drawn in code: letter kids and jerseys, platforms, gates, slides for Odd Patterns, the wall, the pad, controls.

## Voice
Bank voice `hero-coach` as Coach Kit (unique in this batch). `Curio.voice` with `scope: () => state.level + ':' + state.team`, `welcomeAfter: true`.
- event `level`: "{Vowel Teams}! On your marks."
- how `welcome`: "I'm Coach Kit! Steer your team to tag the words it belongs in. Use the arrows."
- event `team`: "Here comes the {Train team}!" (then its sound clip)
- event `tag`: the word clip, then how `sayIt`: "Say it too!"
- event `fizzle`: "That doesn't make a word. This one needs another team."
- event `gateOpen`: "Every {Train team} word tagged! Next team."
- how `splitHow`: "Tap where the word breaks into two parts."
- event `splitNo`: "Try a split between the two parts you can read."
- how `baseHow`: "Tap the base word."
- event, whole, `affix`: "{re} means {again}: {repaint}, {paint again}." (the affix is said as a whole recorded clip, never spelled)
- event `slideAsk`: "Does it sound like {leaf}?"
- event, whole, `wallSay`: "Find {said}."
- event `sortBoard`: "Three spellings, one sound!"
- event `best`: "New best time!"
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Vowel Teams | Tag every platform | Two-thirds of platforms are other teams' (8 of 12, computed); each wrong tag fizzles and in Race adds 3 s. |
| Vowel Teams | Use the pictures only | The picture tells the word, not which of two same-sound teams spells it (ee or ea, ai or ay, oa or ow). |
| Short or Long | Tag every platform | Half are short pictures (6 of 12). |
| Split gate | Tap anywhere | Each word has one break; a 7- or 8-letter word has 6 or 7 places (computed). |
| Odd Patterns | Alternate slides | Words come in a fixed mixed order with three same-slide runs of two (computed). |
| Rule-Breaker Wall | Pick the middle brick | The right brick's position is set in data, 3 or 4 times in each spot (computed). |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a level: `level`, `welcome` (queued, first time), `team` and its sound clip.
2. Tag: `tag` (word clip) then `sayIt`; or `fizzle`. All tagged: `gateOpen`.
3. Two Syllables: `splitHow`, `splitNo` on a miss, then the two parts and the word.
4. Gates: `baseHow`, then `affix` (whole).
5. Odd Patterns: word clip, `slideAsk` on a miss. Wall: `wallSay` (whole).
6. `sortBoard`; Race: `best`.
No voice line contains a bare letter or letter sound; sounds and affixes are recorded clips.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RF.2.3 wording (a to f) | thecorestandards.org, RF Grade 2 | CCSS ELA 2010 PDF | yes |
| The long e sound is commonly spelled ee, ea and e-consonant-e; ea also spells short e (head, bread); ow spells both the long o (snow) and the /ow/ in cow | Reading Rockets, phonics spelling patterns | Moats, Speech to Print (2nd ed., 2010), vowel spellings | yes |
| Each gap word fills to a real word with only its own team (checked word by word) | Merriam-Webster.com Dictionary | Collins English Dictionary online | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad b7, 2026-11-08): 4 words per team and 8 of 12 platforms from other teams; for each of the 24 gaps, the other five teams' fills (120 strings) checked against a common-word list, none found (a build check against Merriam-Webster is listed in Done when 3); 6 of 12 short pictures; split positions; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the maze and pad fit with no scroll; at 680x425 the maze scales down.
2. Short or Long: the Magic-e team fills only long-picture platforms. (RF.2.3a)
3. Vowel Teams: each gap fills only with its own team; at build, every other team's fill is checked against Merriam-Webster and is not an entry. (RF.2.3b)
4. Two Syllables: each word splits only at its break, then reads both parts and the whole word. (RF.2.3c)
5. Gates: each affix peels off; the base is tapped and read; the meaning line plays. (RF.2.3d)
6. Odd Patterns: each word goes only on its slide. (RF.2.3e)
7. Rule-Breaker Wall: each word is tagged only on its brick. (RF.2.3f)
8. The sort board places every tagged long e word under its spelling.
9. Race: timer and ghost appear only with Race on; best time survives a reload where storage works and the tool runs without it.
10. Tap while it plays: any tap during a clip acts at once; no older line plays after a newer one.
11. Motion off: the team jumps cell to cell, no fizzle animation (a gray gap instead), no ghost motion (ghost shown as a time only); no network requests.

## Open questions
- None for Cory.

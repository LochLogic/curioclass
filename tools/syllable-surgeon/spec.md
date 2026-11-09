# Syllable Surgeon

## One idea
Long words arrive at a cheerful word clinic too tangled to read, and the child operates step by step: clip off the prefix and the suffix, split the middle into syllables at their vowel patterns with the syllable scalpel, read each piece, then stitch the word back together and read it whole, and a meaning check shows what the clipped parts did to the word, so they learn a step-by-step way into any long word; words that won't follow the rules go to a "learn whole" chart, and a root-family ward uses a known root to work out a new word.

## Not like
- vowel-team-tag (2, spec): which vowel team says which sound, in one-syllable words first. Here grade 3 long words split by syllable type and affix.
- word-lab (2, spec): mixing word parts for meaning. Here decoding first, with meaning as a check.
- root-detective-cards (4, concept): Greek and Latin roots. Here common English affixes and simple root families.
- story-blanks (3, spec): word jobs in sentences. Here reading the word itself.
- idiom-illustrator (3, spec): phrases whose meaning isn't literal. Here word parts whose meaning adds up.

## Who and how
- Grade 3, ELA, module "Multisyllable Decoding" (Foundational Skills). Standards: RF.3.3a, RF.3.3b, RF.3.3c, RF.3.3d, L.3.4b, L.3.4c (taken in from idiom-illustrator).
- Driver: one student (tool.json `driver: "student"`). Pieces are read on tap from recorded clips; whole words are read on tap.
- Four wards: Prefix and Suffix, Syllable Split, Latin Suffix, Root Family, plus the Rule-Breaker chart. tool.json `modes: []`, `minutes: "10-20"`, `grades_label: "Grade 3"`.
- Nothing is saved; `Print` prints the student's "learn whole" chart and a ward's word list.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RF.3.3a, L.3.4b | Clip prefixes and suffixes, then the meaning check: what did un- or -less do to the word? | the clipped parts on a tray with their meanings | 2, 3 |
| RF.3.3c | Split the base into syllables with the scalpel at the right place for its pattern (closed, open, silent e, vowel team, r-controlled, consonant-le) | the split word with each piece's pattern tag | 4 |
| RF.3.3b | Latin Suffix ward: clip -tion, -sion, -ment, -ous, -ible, -able and read the base | the word with its suffix lit | 5 |
| RF.3.3d | Rule-Breaker chart: words the scalpel can't split by the rules go to "learn whole" and are practiced as wholes | the chart with the tricky part marked | 6 |
| L.3.4c | Root Family ward: snip family members back to the root, say what the root means, then work out a new family word in a sentence | the family tree around the root | 7 |

## Screens and modes
Header (kit): title "Syllable Surgeon"; `Wards`, `Learn whole`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A bright, friendly clinic (no blood, no needles) with a patient word lying on a cushion table, "unbelievable", and Dr. Tabby, a cat in green scrubs and a head mirror. First hint: "Tap the word to hear its trouble." The first tap plays the patient line; the welcome is queued after it (`welcomeAfter: true`).

**Operating table.** Focus: the word in big letters (48 px) on the table. Three tools on a tray (each 60 x 60 with a name): Prefix Clip, Suffix Clip, Syllable Scalpel. Steps:
1. Clip: drag the Prefix Clip to the start; tap between the letters where the prefix ends (data accepts one place). Same for the suffix at the end.
2. Meaning check: the clipped parts sit on a tray; pick what each does (un-: not; -able: can be), then what the whole word means.
3. Split: the scalpel cuts between letters; data gives each base its accepted split(s) (rab|bit; ro|bot; ta|ble). A wrong cut shows the pattern hint ("Two consonants between vowels? Split between them.").
4. Read each piece: tap to hear the recorded piece (clips, not voice lines); then tap `Stitch` and hear the whole word.

**Wards.** Prefix and Suffix (12 words), Syllable Split (18 words, three per pattern), Latin Suffix (12 words), Root Family (4 families). Final reading: a short paragraph packed with words from the wards, each tap-to-split.

**Rule-Breaker chart.** When the scalpel is used on a word marked irregular (laugh, through, island, people, again, enough, busy, ocean), the cut won't stick and Dr. Tabby says "This one doesn't follow the rules. Let's learn it whole." The word goes to the chart with its tricky part outlined (gh in laugh, s in island).

At 1366x768 the table and tray fit; at 680x425 the tray sits under the word.

## Content
- Prefix and Suffix: unbelievable (un|believ|able), careful, hopeless, rewrite, disagree, preheat, misspell, kindness, unhappy, replay, helpful, untidy. Meanings: un- not; re- again; dis- not or opposite of; pre- before; mis- wrongly; -ful full of; -less without; -able can be; -ness the state of being.
- Syllable Split (base words, by pattern): closed (rab|bit, nap|kin, sun|set), open (ro|bot, ti|ger, mu|sic), silent e (cup|cake, in|vite, base|ball), vowel team (rain|coat, sea|son, tea|pot), r-controlled (gar|den, per|fect, cor|ner), consonant-le (ta|ble, pud|dle, bot|tle).
- Latin Suffix: action, vacation, invention, division, television, movement, enjoyment, famous, dangerous, visible, possible, comfortable.
- Root Family: act (action, actor, react, active); help (helper, helpful, helpless, unhelpful); play (player, replay, playful, playground); kind (kindness, unkind, kindly). New-word sentences: "The actress waved from the stage." "The kitten was playful."
- The final paragraph: about 80 words, written for Curio Class, using at least one word from each ward.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Cuts land between letters only; each gap is a 44 px wide target at 48 px type.
- Pieces are played from recorded clips (no letter sounds in voice lines); a piece's clip says the syllable as it sounds in the word.
- A wrong clip or cut never ends the operation; the hint shows and the tool waits.
- Motion off: the stitch is instant.

## Look
- Accent `--brand` #1e6a8a clinic blue (header, tools, scrubs trim); gold #f4c542 (the cut line, stitches); paper #f2f8fb; ink #0c2230; muted #4a5d68. Scene: a bright, friendly word clinic with plants and posters.
- Contrast (WCAG 2.1, computed): white on brand 6.03:1; brand on paper 5.62:1; ink on paper 15.22:1; muted on paper 6.41:1; ink on gold 10.03:1.
- Never color alone: prefix, base and suffix pieces have labels under them; pattern tags are words.
- Different from this batch (game-show violet, block brick, trail green, fair red).

## Art
Local FLUX (`scripts/localart.py`).
- clinic (1): "A bright friendly cartoon clinic for words with plants and a cushioned table, soft gouache, no text, no medical gore"; 16:9; cutout no.
- Dr. Tabby (5, wave, inspect, cut, stitch, cheer): "A friendly cat doctor in green scrubs with a head mirror <pose>, soft gouache, plain white background"; 1:1; cutout yes.
- tools (3): "<a big friendly clip / a rounded toy scalpel / a needle and thread made of light>, toy-like, plain white background"; 1:1; cutout yes.
- ward signs (4) and root family trees (4); 4:3.
About 17 images. Drawn in code: words, gaps, tags, chart.

## Voice
Bank voice `warm-teacher` as Dr. Tabby (unique in this batch). Syllable pieces and whole words are recorded clips. `Curio.voice` with `scope: () => state.ward + ':' + state.word + ':' + state.step`, `welcomeAfter: true`.
- event `patient`: "This word is too tangled to read. Let's operate!"
- how `welcome`: "Welcome to the clinic. We clip the front and back, split the middle, read each piece, then stitch it together."
- how `clipHow`: "Drag the Prefix Clip to the front, then tap where the prefix ends."
- how `meaningHow`: "What did this part do to the word? Tap a meaning."
- how `splitHow`: "Use the scalpel. Tap between the letters where the word splits."
- event `cutHint`: the pattern hint.
- event `stitch`: "Stitched! Read it whole."
- event `ruleBreaker`: "This one doesn't follow the rules. Let's learn it whole."
- how `familyHow`: "Snip each family member back to the root. What does the root mean?"
Read speaks the hint, which names the next action and control and never a disabled one. No voice line says a bare letter or letter sound; pattern hints describe ("two consonants between vowels") and the screen shows the letters.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Clip place | Tap every gap | Each tap is a cut; a wrong cut shows a hint, and the word holds only the accepted cut (one gap of 3 to 11 per affix, checked). |
| Split | Cut after every vowel | Accepted splits are one gap per base (two for a few); patterns differ (rab|bit vs ro|bot), so one rule fails on the others (checked). |
| Meaning check | Guess | One of three; a wrong pick shows the meaning in a sentence. |
| Rule-breakers | Cut them anyway | The cut won't stick; the word goes to the chart. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap the word: `patient`, `welcome` (queued, first time).
2. Clip: `clipHow`; meaning: `meaningHow`.
3. Split: `splitHow`; wrong cut: `cutHint`; stitch: `stitch`.
4. Irregular word: `ruleBreaker`. Root Family: `familyHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RF.3.3a to d and L.3.4b, c wording | thecorestandards.org, Foundational Skills and Language Grade 3 | CCSS ELA 2010 PDF | yes |
| Six syllable types (closed, open, silent e, vowel team, r-controlled, consonant-le) and the VC/CV and V/CV split patterns | Reading Rockets, syllable types | UFLI Foundations (University of Florida Literacy Institute), multisyllabic word lessons | yes |
| The prefix and suffix meanings listed (un-, re-, dis-, pre-, mis-, -ful, -less, -able, -ness) | Merriam-Webster entries for each affix | Reading Rockets, roots and affixes | yes |
| un-, re-, in-/im- and dis- account for most prefixed words in school texts | White, Sowell and Yanagihara (1989), The Reading Teacher | Reading Rockets, affixes article citing it | yes |
Backed twice: 4. Cut: 0.

Checks run (Python, scratchpad b10, 2026-11-08): every split piece has a vowel letter (y counts at the end); each of the 6 pattern lists has 3 words; one split rule (cut after the first vowel) fails on all 3 closed-syllable words; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the table and tray fit; at 680x425 the tray sits under the word.
2. Clips accept only the data gap for each affix. (RF.3.3a)
3. The meaning check covers each affix and the whole word. (L.3.4b)
4. The scalpel accepts data splits and shows pattern hints. (RF.3.3c)
5. The Latin Suffix ward reads bases after clipping. (RF.3.3b)
6. Irregular words go to the chart with the tricky part marked. (RF.3.3d)
7. The Root Family ward snips to the root and asks for a new word's meaning in a sentence. (L.3.4c)
8. The final paragraph is tap-to-split.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: the stitch is instant; no network requests.

## Open questions
- None for Cory.

# Sentence Remixer

## One idea
The student remixes a paragraph of eight short, choppy sentences about two friends fixing a bike before a race into varied ones on a mixing deck, joining them with and, but, because, when and who or opening with a phrase, while a rhythm strip shows the new sentence lengths; every time a merge causes a pronoun problem (a "she" that could mean Ana or Lena, "Him and me checked the chain", a shift from "you" to "they") the sentence glitches until it is fixed, so they learn to vary sentences without losing who is who.

## Not like
- parallel-parking (9, concept): parallel structure. Here sentence variety and pronouns, grade 6.
- sentence-diagram-builder (7, concept): clause types as a tree. Here combining for rhythm.
- comma-chameleon (4, spec): commas. Here combining and pronouns.
- pause-and-break (6-8, spec): punctuation as pauses. Here sentence patterns.
- grammar-garage (4, spec): grade 4 grammar. Here grade 6 pronouns.

## Who and how
- Grade 6, ELA, module "Pronouns and Sentence Variety" (Language). Standards: L.6.1 (a, b, c, d, e), L.6.3 (a, b).
- Driver: one student (tool.json `driver: "student"`). Every sentence is read on tap.
- Three paragraphs: The Bike Race, The Bakery, The Storm Drill; a fourth with Grandpa Joe's voice. tool.json `modes: ["Remix", "Three ways"]`, `minutes: "20-30"`, `grades_label: "Grade 6"`.
- Nothing is saved; `Print` prints the before-and-after paragraph and the glitch log.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| L.6.1a | Fix case glitches ("Him and me checked the chain" to "He and I") | the glitch and its fix | 2 |
| L.6.1b | Add an intensive pronoun where the meaning needs it ("Lena fixed it herself") | the pronoun and its picture | 2 |
| L.6.1c | Fix shifts in number and person ("you" to "they", "a racer" to "they") | the glitch log | 2 |
| L.6.1d | Fix vague pronouns after a merge (a "she" that could mean two people) | two flashing pictures and the fix | 3 |
| L.6.1e | Decide where Grandpa Joe's informal English belongs (his dialogue) and where the narration uses standard forms | the paragraph with voice marks | 4 |
| L.6.3a | Merge and open with phrases until the rhythm strip shows variety | the rhythm strip before and after | 5 |
| L.6.3b | Keep style and tone: a chat-slang remix in a formal paragraph glitches | the tone glitch | 5 |

## Screens and modes
Header (kit): title "Sentence Remixer"; `Remix`, `Three ways`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A DJ mixing deck with eight sentence tracks stacked like faders, the rhythm strip under them (all bars the same short length), and DJ Fader, a fox in big headphones. First hint: "Tap a sentence to hear it." The first tap reads it; the welcome is queued after it (`welcomeAfter: true`).

**Remix.** The student selects two adjacent tracks and picks a joiner (and, but, so, because, when, while, who, which) or "open with a phrase" (the second sentence's time or place phrase moves to the front of the first). Each combination is built from data: every pair of sentences has its merged forms written out, including the ones that cause glitches. The rhythm strip updates.

**Glitches.** A sentence with a problem shakes and shows a glitch stripe (Motion off: a stripe only):
- Vague: "Ana handed Lena the wrench, and she tightened the bolt." Two pictures flash (Ana tightening, Lena tightening); the student fixes it with a name chip or by picking a rebuild.
- Case: merging "Dad checked the chain." and "I checked the chain too." offers "Him and me checked the chain."; fix to "He and I".
- Shift: "If you want to win, racers have to check their tires."
- Intensive: a sentence where the meaning needs "herself" (no one helped Lena); the picture shows Lena alone.
- Tone: a remix choice that drops "lol it was totally broken" into the narration.
The glitch log names each fix.

**Grandpa Joe.** The fourth paragraph includes Grandpa Joe, who talks the way people in his town do ("We was fixing bikes before you was born"). The student marks which lines are his dialogue (keep his voice) and which are narration (standard forms). Changing his dialogue is answered with "That's how Grandpa Joe talks. His voice belongs in his own words."

**Finish.** The remixed paragraph reads aloud; a before-and-after rhythm strip and the glitch log show what changed.

**Three ways.** The same paragraph remixed three times; the strips compare.

At 1366x768 the deck and strip fit; at 680x425 the strip is under the deck.

## Content
Written for Curio Class: four paragraphs of 8 sentences each; for each adjacent pair, all joiner forms with glitch tags; pictures for vague and intensive glitches.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Merges can be split back.
- The rhythm strip shows word counts as numbers above each bar.
- Done needs no open glitches and sentences in all three length ranges (short under 8, medium 8 to 15, long over 15 words).

## Look
- Accent `--brand` #0d6e8a mixer cyan (header, deck, faders); gold #f4c542 (rhythm bars, fixed glitches); paper #f0f7fa; ink #062431; muted #475c66. Scene: a small bedroom DJ desk.
- Contrast (WCAG 2.1, computed): white on brand 5.81:1; brand on paper 5.36:1; ink on paper 14.86:1; muted on paper 6.48:1; ink on gold 9.90:1.
- Never color alone: glitches show a stripe and a label; bars show numbers.
- Different from this batch (studio slate, camera purple, raspberry, press olive).

## Art
- People art goes to Gemini: Ana (a Mexican American girl about 11 in a bike helmet), Lena (a white girl about 11 with a wrench), Grandpa Joe (an older white man from a rural town, flannel shirt); each in the vague and intensive pictures (8 pictures); "children's book illustration <scene>, warm gouache, no text"; 4:3.
- Local FLUX (`scripts/localart.py`): DJ desk (1); DJ Fader (4 poses), "A friendly fox DJ with big headphones at a mixing deck <pose>, soft gouache, plain white background"; 1:1; cutout yes; paragraph scenes (3: a bike race start, a bakery counter, a school hallway during a storm drill, no people).
About 16 images. Drawn in code: deck, strip, glitch effect.

## Voice
Bank voice `warm-teacher` as DJ Fader and the paragraph reader (unique in this batch); Grandpa Joe's lines are `friendly-dad` (unique in this batch). `Curio.voice` with `scope: () => state.paragraph + ':' + state.track`, `welcomeAfter: true`.
- how `welcome`: "Eight sentences, all the same length. Remix them, and keep track of who's who."
- event, whole, `sentence`: the tapped sentence.
- event `vague`: "Who tightened the bolt, Ana or Lena?"
- event `caseFix`: "{He and I} checked the chain."
- event `shift`: "{You}, then {racers}. Pick one."
- event `voiceBelongs`: "That's how Grandpa Joe talks. His voice belongs in his own words."
- event `finish`: the paragraph, read whole.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: pairwise merge data with glitch tags, rhythm strip, glitch log, voice marks.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Variety | Merge everything into one sentence | Done needs short, medium and long sentences. |
| Glitches | Pick any fix | Each glitch has keyed fixes; wrong fixes keep the glitch. |
| Grandpa Joe | Standardize everything | Changing his dialogue is turned back with a reason; the narration must be standard. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a sentence: `sentence`, `welcome` (queued, first time).
2. Merges: glitches `vague`, `caseFix`, `shift` as they fire.
3. Grandpa Joe: `voiceBelongs` as it fires.
4. Finish: `finish`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| L.6.1 (a to e) and L.6.3 (a, b) wording | thecorestandards.org, Language Grade 6 | CCSS ELA 2010 PDF | yes |
| Subject pronouns (I, he) are used in compound subjects; intensive pronouns end in -self or -selves | Purdue OWL, pronoun case | Merriam-Webster, intensive pronoun | yes |
| Sentence combining builds variety and is effective for teaching syntax | Graham and Perin, "Writing Next" (2007), Carnegie Corporation | Reading Rockets, sentence combining | yes |
| Regional and informal varieties of English are rule-governed ways of speaking | Linguistic Society of America, statement on language varieties | Center for Applied Linguistics, dialects in schools | yes |
Backed twice: 4. Cut: 0.

Sensitivity note: Grandpa Joe's English is presented as a real way of speaking that belongs in his dialogue, never as wrong speech; the tool goes to the fresh-agent review.

Checks run (Python, scratchpad b18, 2026-11-09): the sample bike paragraph has 8 sentences of 4 to 7 words; one sample remix reaches short, medium and long ranges; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 deck and strip fit; at 680x425 the strip is under the deck.
2. Case, intensive and shift glitches fire and fix. (L.6.1a, b, c)
3. Vague pronoun glitches flash two pictures and fix. (L.6.1d)
4. Grandpa Joe's lines are marked dialogue and kept. (L.6.1e)
5. The rhythm strip shows variety and done needs three ranges. (L.6.3a)
6. Tone glitches fire for slang in narration. (L.6.3b)
7. Three ways compares strips; Print shows before and after with the log.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: glitches show a stripe only; no network requests.

## Open questions
- None for Cory.

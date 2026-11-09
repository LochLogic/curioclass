# Stay in Character

## One idea
The child reads a short story about Kai, who wants to win the town kite contest and hates to lose, and at each fork predicts what Kai would really do (not what the child would do) by pointing to a clue on Kai's character card; the story then plays what Kai did and a cause line links that action to the next event, and one "out of character" path shows the whole chain of events falling apart, so the child sees that a character's traits, wants and feelings drive the plot.

## Not like
- two-sides-theater (2, spec): one event told from two characters' sides. Here one character's choices and their causes.
- story-building-blocks (3, concept): story structure parts. Here characters as the engine of events.
- plot-rollercoaster (6, concept): plot arc shape. Here cause and effect from one character's traits.
- moral-of-the-story (2, spec): lessons of fables. Here traits and motives.
- swap-the-teller (3-5, concept): who tells the story. Here what a character does.

## Who and how
- Grade 3, ELA, module "Characters and Their Choices" (Reading Literature). Standard: RL.3.3.
- Driver: one student or a pair (tool.json `driver: "student"`). Every page is read on tap.
- Two stories: "Kai and the Kite Contest" (a bold character) and "Nell's Quiet Plan" (a quieter character). tool.json `modes: []`, `minutes: "15-20 per story"`, `grades_label: "Grade 3"`.
- Nothing is saved; `Print` prints the cause chain and the character card.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.3.3 (traits) | Tap clue words on each page to add them to Kai's character card under Traits | the card filling with clues | 2 |
| RL.3.3 (motivations) | Add want clues under Wants | the Wants row | 2 |
| RL.3.3 (feelings) | Pick Kai's feeling at each page turn from faces with words; feelings can change | the feeling track on the card | 3 |
| RL.3.3 (predict from clues) | At each fork, pick what Kai would do and point to the clue that says so | the fork with three choices and a clue pin | 4 |
| RL.3.3 (actions cause events) | After each fork, finish the cause line: "Because Kai ___, ___" from tiles | the cause chain growing | 5 |
| RL.3.3 (actions cause events) | Out-of-character path: replay with one changed choice and see the chain change; write "Kai's choice to ___ caused ___" | two chains side by side | 6 |

## Screens and modes
Header (kit): title "Stay in Character"; `Stories`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A story book opens on a windy hill with kites, and Gran Willa, a gray goose storyteller in a rocking chair, beside it. First hint: "Tap the first page to meet Kai." The first tap reads page 1; the welcome is queued after it (`welcomeAfter: true`).

**Story page.** Focus: a page (picture 640 x 360 above 3 to 5 sentences). Some words glow as clue words (data); tapping one offers "Trait", "Want" or "Not a clue" and drops it on the character card at the right (Traits, Wants, Feelings track). Wrong sorts show why ("Hates to lose tells what Kai is like. That's a trait.").

**Fork.** At 4 points in each story, three choice pictures with captions: one in character, one the child might do but Kai wouldn't, one random. The child picks and pins a clue from the card that supports it. The in-character choice with a fitting clue plays on; an out-of-character choice gets Gran Willa: "Would Kai do that? Look at the card." and the child picks again. A fork may test a change: after Kai's kite breaks and Mo helps fix it, the card gains a new feeling and trait (grateful; can be a good teammate), and the next fork expects the changed Kai.

**Cause line.** After each fork, a cause tile pair appears: "Because Kai ___" and "___ happened"; the child picks the matching effect from three tiles. The chain grows across the bottom.

**Out of character.** At the end, Gran Willa offers: "What if Kai hadn't bragged at the start?" The story replays from fork 1 with that choice; the chain changes (Mo never gets annoyed, so the help comes earlier, so the kite flies at noon). Both chains show side by side; the child finishes "Kai's choice to ___ caused ___" from tiles or by typing.

At 1366x768 the page and card fit side by side; at 680x425 the card is a drawer.

## Content
"Kai and the Kite Contest" (original, 10 pages): Kai wants to win the kite contest (want), hates to lose and brags (traits), and is a loyal friend (trait). Forks: (1) Kai brags about his kite to Mo (in character: brags); (2) the wind tears Kai's kite; Kai wants to quit or fix it (in character: fix it, wants to win); (3) Mo offers help after being bragged at; Kai feels sorry and says so (a change); (4) contest: Mo's kite tangles; Kai stops to help even though he might lose (loyal friend). Ending: they fly together and tie for "Best Teamwork"; Kai is surprised to feel happy.
"Nell's Quiet Plan" (original, 10 pages): Nell is shy (trait), careful (trait), and wants to plant a class garden (want). Forks test a quiet character: she writes a note instead of speaking up; she asks one friend first; she shows the plan with drawings; she speaks to the class when her friend nods. Ending: the class plants the garden; Nell's feeling moves from nervous to proud.
Each story has 12 to 16 clue words, 4 forks with 3 choices each, 4 cause pairs, and one out-of-character replay.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- A fork needs both a choice and a clue pin; a choice with a clue that doesn't fit gets "That clue doesn't show it. Try another."
- Cause tiles: three per fork, one fits.
- The out-of-character replay runs the same pages with changed text from data; changed sentences are underlined.

## Look
- Accent `--brand` #0f6670 story teal (header, card, chain links); gold #f4c542 (clue glow, pins); paper #f2f9f9; ink #0b2427; muted #4a5e60. Scene: a breezy hill with kites and a story book.
- Contrast (WCAG 2.1, computed): white on brand 6.66:1; brand on paper 6.24:1; ink on paper 15.20:1; muted on paper 6.43:1; ink on gold 9.96:1.
- Never color alone: card rows have names and icons; feelings are faces with words.
- Different from this batch (gallery plum, planetarium navy, radio orange, reading-table green).

## Art
- People art goes to Gemini: Kai (a Pacific Islander boy about 8), Mo (a Black boy about 8), Nell (a white girl about 8 with glasses), her friend June (a South Asian girl about 8); about 28 poses and feelings across the stories, "illustrated children's book character <description> <pose or feeling>, warm illustrated style, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): Gran Willa (4 poses), "A kind gray goose grandmother storyteller in a rocking chair with a shawl <pose>, soft gouache, plain white background"; 1:1; cutout yes. Page scenes without people (hill with kites, a park, a classroom, a garden), 12 total; 16:9; characters are placed as cutouts.
About 44 images. Drawn in code: card, chain, tiles, pins.

## Voice
Bank voice `gentle-storyteller` as Gran Willa and the story reader (unique in this batch). `Curio.voice` with `scope: () => state.story + ':' + state.page`, `welcomeAfter: true`.
- event, whole, `page`: the page text.
- how `welcome`: "You'll meet Kai. He wants to win the kite contest. At each fork, choose what Kai would really do. The clues are on his card."
- how `clueHow`: "Tap a glowing word to put it on Kai's card."
- event `sortWhy`: the clue's reason.
- how `forkHow`: "What would Kai do? Pick one, then pin the clue that tells you."
- event `wouldThey`: "Would Kai do that? Look at the card."
- event `change`: "Something changed in Kai. Look at his card."
- how `causeHow`: "Finish the cause line: because Kai did that, what happened?"
- event `whatIf`: "What if Kai hadn't bragged at the start? Let's see."
- event `compare`: "One choice changed everything after it."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
choose-path. No engine exists yet; this spec describes `__tool.cp` (kit/choose-path.js): a page list with fork nodes; each fork holds choices with `fits: true|false`, `clueIds` that support it, and a `next` page; cause pairs per fork; `replay` maps (fork id to forced choice) that swap page text by id. Reused by later choose-path tools.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Fork | Try all choices | Allowed, but each needs a fitting clue pin too; the clue step is the reading. |
| Clue pin | Pin any clue | Only 1 or 2 card clues support each choice (checked); others get "That clue doesn't show it." |
| Cause line | Guess | One of three per fork; wrong tiles show the page that proves the real effect. |
| Clue sort | All "Trait" | Each story has wants and non-clues too; all-trait leaves at least 4 wrong (checked). |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap page 1: `page` (whole), `welcome` (queued, first time), then `clueHow`.
2. Clue sort: `sortWhy` when wrong.
3. Fork: `forkHow`; wrong: `wouldThey`; change fork: `change` (waits).
4. Cause: `causeHow`. End: `whatIf`, replay, `compare`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.3.3 wording | thecorestandards.org, Reading Literature Grade 3 | CCSS ELA 2010 PDF | yes |
Backed twice: 1. Cut: 0. The stories are original; no other facts are claimed.

Sensitivity note: the four kid characters (several backgrounds) go to the fresh-agent review. The storyteller is a goose on purpose, so no culture is cast as the wise elder.

Checks run (Python, scratchpad b9, 2026-11-08): supporting clues per choice 1 or 2; all-trait sort leaves 8 of 15 Kai clues wrong; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the page and card fit; at 680x425 the card is a drawer.
2. Clue words sort to Traits or Wants with reasons. (RL.3.3)
3. The feeling track takes a pick per page and shows changes. (RL.3.3)
4. Forks need an in-character choice and a fitting clue pin. (RL.3.3)
5. Cause lines grow a chain. (RL.3.3)
6. The out-of-character replay changes the chain and ends with the cause sentence. (RL.3.3)
7. Both stories run on `__tool.cp` with no story-specific code.
8. Print gives the chain and card.
9. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
10. Motion off: the chain doesn't animate; no network requests.

## Open questions
- None for Cory.

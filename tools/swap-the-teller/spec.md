# Swap the Teller

## One idea
The prize pie goes missing at the county fair, and the story is told in four parts by whichever teller the student picks each time: Jun, age 9, who says "I" and only knows what Jun saw; the narrator, who sees the whole fair; and Grumpy Gus the goose, who thinks the pie was a gift; a clue board fills with facts only some tellers include, and at the end the student names who took the pie and why, then reads the fair manager's newsletter, which has its own view, so they learn that who tells a story decides what you learn, what you miss and how you feel about it, and that their own view can differ from all of them.

## Not like
- two-sides-theater (2, spec): voicing two characters' sides of one scene. Here narrators: first person, third person, and a character teller, plus the student's own view.
- who-said-that (1, spec): who is talking. Here who is telling and what they can know.
- perspective-camera (6, concept): how an author builds a narrator. Here grades 3-5 comparing tellers.
- stay-in-character (3, spec): a character's choices drive events. Here the teller shapes what we hear.
- side-by-side-reader (3-5, spec): two different texts. Here one event retold.

## Who and how
- Grades 3-5, ELA, module "Narrators and Points of View" (Reading). Standards: RL.3.6, RI.3.6, RL.4.6, RL.5.6.
- Driver: one student or a pair (tool.json `driver: "student"`). Every passage is read on tap.
- Four parts plus the newsletter; grade picker (3, 4, 5) sets which questions show. tool.json `modes: []`, `minutes: "20-30"`, `grades_label: "Grades 3-5"`.
- Nothing is saved; `Print` prints the clue board and the student's view. Extra: write part five from a teller of your choice (kept until the page closes).

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| RL.3.6 | Name who took the pie and why, then set your view beside Jun's, the narrator's and Gus's | four view cards side by side | 5 |
| RI.3.6 | Read the fair manager's newsletter; mark where your view matches or differs from the author's | the article with agree and differ marks | 6 |
| RL.4.6 | At each part, mark "I, me, my" telling (first person) or "he, she, they" telling (third person), and compare what Jun and the narrator can know | the teller badge and a "knows / can't know" chart | 2, 3 |
| RL.5.6 | On the clue board, see how each teller's view changes how the same event is described (Gus calls it "a gift", Jun "a disaster") | the same event in three wordings | 4 |

## Screens and modes
Header (kit): title "Swap the Teller"; `Parts`; `Read`, `Motion`, `Sound`, `Print`. Controls 44 px or more, icon plus word.

**On load and first tap.** A fairground map with a pie tent, a goose pen and a Ferris wheel, and three teller badges: "I" (Jun), "the narrator", and Gus the goose. First hint: "Tap a badge to pick who tells part one." The first tap plays that teller's first line; the welcome is queued after it (`welcomeAfter: true`).

**Part.** Focus: the passage (8 to 12 sentences) with the teller's badge and picture. Each part exists in three tellings (data), all true to the same events but differing in what is known and how it's worded. After reading:
- Grade 3 and up: "Who is telling? I, me, my or he, she, they?" (two big buttons); and "What does this teller not know?" (three choices).
- Grade 4 and up: a "knows / can't know" chart for the part, where the student drags facts to Jun's column or the narrator's.
- The student can switch tellers and reread the same part; each new teller adds clue cards.

**Clue board.** Facts collect as cards with the teller who gave them; some appear in only one telling (only the narrator sees the pie-judge's dog near the tent; only Gus knows the pie was set on the low table by the pen; only Jun hears the judge say "leave it for the ribbon"). Grade 5: the board shows the same event in each teller's words side by side, and the student picks what the wording makes you feel about it.

**Who took the pie?** After part four: pick the culprit and the reason from cards (the judge's dog, Gus, Jun's cousin, a mix-up), each needing two clue cards to support it. The story's answer (the dog nudged the pie off the low table to Gus, who "accepted the gift") is revealed only after the student commits.

**Newsletter.** The fair manager's article, "Goose Ruins Pie Contest", an informational text with its own view (Gus is a menace; the low table is not mentioned). The student marks each paragraph "I agree", "I see it differently" and picks the clue that shows why.

At 1366x768 the passage and clue board fit; at 680x425 the board is a drawer.

## Content
Original story set at the Pine County Fair, 4 parts in 3 tellings each (12 passages) plus the newsletter (5 paragraphs). Characters: Jun (narrates in first person), his cousin Bea, Judge Ortiz and her dog Biscuit, Gus the goose, the fair manager Mr. Hale. No one is punished; the ending has the judge give a ribbon for "Best Pie, as Judged by a Goose".
Clue cards: 14, each with which tellers include it. Every telling of a part includes at least one clue the others don't.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Switching tellers keeps the part and swaps the passage; read tellings are ticked on the badges.
- Culprit picks need two supporting clue cards; a pick with clues that don't support it gets "Does that clue show it?"
- The newsletter marks take a clue each; there is no right view, only supported ones; the student's own view card is never marked wrong, only asked to cite a clue.

## Look
- Accent `--brand` #9b2c2c fair red (header, badges, ribbons); gold #f4c542 (clue card glow, the prize ribbon); paper #fcf6f2; ink #2a1414; muted #66524f. Scene: a county fair in late summer.
- Contrast (WCAG 2.1, computed): white on brand 7.53:1; brand on paper 7.03:1; ink on paper 16.22:1; muted on paper 6.80:1; ink on gold 10.68:1.
- Never color alone: each teller has a badge with a word and an icon (I, an eye over the fair, a goose foot).
- Different from this batch (game-show violet, block brick, trail green, clinic blue).

## Art
- People art goes to Gemini: Jun (a Korean American boy about 9), Bea (his cousin, about 7), Judge Ortiz (a Latina woman in her sixties with a ribbon badge), Mr. Hale (a white man in his fifties with a fair cap); about 16 poses, "illustrated children's book character <description> <pose>, warm illustrated style, plain white background"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): fair map (1), "A cheerful county fair map with a pie tent, goose pen and Ferris wheel, soft gouache, no text"; 16:9. Gus (5 moods), "A grumpy white farm goose <mood>, soft gouache, plain white background"; 1:1; cutout yes. Biscuit the dog (3), scene backgrounds (6).
About 31 images. Drawn in code: badges, board, cards, charts.

## Voice
Three tellers and a host, all unique in this batch: `casual-peer` as Jun, `smooth-narrator` as the narrator, `gravel-ranger` as Gus, and `firm-captain` as Mr. Hale reading the newsletter. Hints come from the narrator voice. `Curio.voice` with `scope: () => state.part + ':' + state.teller`, `welcomeAfter: true`.
- event, whole, `passage`: the part in the teller's voice.
- how `welcome`: "The prize pie is missing! Three tellers know different things. Pick who tells each part, and swap to hear the others."
- how `whoHow`: "Who is telling this part? Tap I, me, my or he, she, they."
- how `knowHow`: "What does this teller not know? Tap an answer."
- event `newClue`: "A new clue for the board!"
- how `culpritHow`: "Who took the pie? Pick, then pin two clues that show it."
- event `reveal`: the story's answer.
- how `paperHow`: "Mr. Hale wrote about it. Do you see it the same way? Mark each part and pick a clue."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
none

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Teller person | Always tap "I" | The narrator's telling of every part is third person; Jun and Gus both say "I", so the student compares two first-person tellers who know different things (checked). |
| Can't know | Guess | One of three, with the sentence that shows it after. |
| Culprit | Guess the goose | Needs two supporting clues; the full answer is a chain only clues from several tellers can show. |
| Newsletter | Agree with everything | Not wrong, but each mark needs a clue, and the low-table clue is missing from the article. |

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a badge: `passage` (whole), `welcome` (queued, first time).
2. After a part: `whoHow`, `knowHow`; new clues: `newClue`.
3. After part four: `culpritHow`, then `reveal` (waits).
4. Newsletter: `paperHow`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| RL.3.6, RI.3.6, RL.4.6, RL.5.6 wording | thecorestandards.org, Reading Grades 3 to 5 | CCSS ELA 2010 PDF | yes |
Backed twice: 1. Cut: 0. The story is original; no other facts are claimed.

Sensitivity note: people characters go to the fresh-agent review.

Checks run (Python, scratchpad b10, 2026-11-08): each teller has at least one unique clue per part; the narrator's 4 tellings are third person and Jun's and Gus's 8 are first person; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 the passage and board fit; at 680x425 the board is a drawer.
2. Each part has three tellings and can be switched. (RL.4.6)
3. The person question and the knows chart work at their grades. (RL.4.6)
4. The clue board fills and, at grade 5, shows one event in three wordings. (RL.5.6)
5. The culprit pick needs two clues; the student's view card sits beside the tellers'. (RL.3.6)
6. Newsletter marks take a clue each. (RI.3.6)
7. Part five writing works and prints.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: no bouncing badges; no network requests.

## Open questions
- None for Cory.

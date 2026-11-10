# Story Replay

## One idea
Short cartoon stories (birds on a wire, apples in a basket, shells on a beach) play on a little stage and stop at the question, the child drags counters onto a tray to act the story out, then picks a number sentence from three cards, and the cartoon replays exactly the way that sentence says, so a right pick ends the story true and a wrong pick plays out visibly wrong (Ana finds 8 more shells instead of 5 and ends up with 21, and the birds look puzzled); stories rotate through every type within 20 (add to, take from, put together, take apart and compare) with the unknown at the end, in the change or at the start, plus three-group shows like 3 + 5 + 7 apples; in compare stories ("Mia has 9 stickers, Leo has 6, how many more does Mia have?") both 6 + 3 = 9 and 9 - 6 = 3 replay true; at the end a playbill lists every show with the sentence that fit it, so a first grader learns to use addition and subtraction within 20 to solve word problems of every kind, with the unknown in any position, using objects and equations with a symbol for the unknown, and to solve word problems that add three whole numbers whose sum is 20 or less.

## Not like
- bus-stop (K, spec): within 10, only getting on and off. Here every story type within 20.
- lost-and-found (2, concept): two-step stories within 100. Here one step within 20.
- make-ten-machine (1, spec): fact strategies, no stories. Here stories, any strategy.
- sheep-count (K, spec): counting one set. Here choosing which operation fits.

## Who and how
- Grade 1, Math, module "Story Problems". Standards: 1.OA.1 (use addition and subtraction within 20 to solve word problems involving situations of adding to, taking from, putting together, taking apart, and comparing, with unknowns in all positions, e.g., by using objects, drawings, and equations with a symbol for the unknown number to represent the problem), 1.OA.2 (solve word problems that call for addition of three whole numbers whose sum is less than or equal to 20, e.g., by using objects, drawings, and equations with a symbol for the unknown number to represent the problem).
- Format: story. Driver: one student (tool.json `driver: "student"`). Every card is spoken. Controls 56 px or more.
- Fifteen shows (three each of add to, take from, put together, take apart, compare), unknowns in all three spots, three three-group shows, a counter tray of 20, three sentence cards per show. Extra: Act it out (the class acts with real objects before the replay). tool.json `modes: ["Stage", "Act it out"]`, `minutes: "15-20"`, `grades_label: "Grade 1"`.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| 1.OA.1 (types and unknowns) | Act out each story and pick its sentence | the replay matching or not | 2 |
| 1.OA.1 (compare) | Solve "how many more" by adding or subtracting | both sentences replaying true | 3 |
| 1.OA.2 | Act out three groups and pick the sentence | 3 + 5 + 7 = ? replayed | 4 |

## Screens and modes
Header (kit): title "Story Replay"; `Stage`, `Act it out`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more.

**On load and first tap.** A small stage with a red curtain, a counter tray of 20 round counters, three empty card slots. The welcome is queued (`welcomeAfter: true`): "Welcome to Story Replay! Each show stops at a question. Then you pick the number sentence, and the show plays it back. Tap the curtain." First hint: "Tap the curtain."

**A show (focus: the stage).** At 1366x768 the stage fills the top with the tray and cards below; at 680x425 the stage is on top and the tray and cards share one row. A 20-second cartoon plays: Ana has 8 shells, finds some more, now she has 13. The curtain freezes: "How many shells did Ana find?" The child drags counters onto the tray to act it out, then taps one of three cards (8 + ? = 13, 13 + 8 = ?, 13 - 5 = ?).

**The replay.** The show plays again, following the chosen sentence. Right: Ana finds 5 and has 13. Wrong (13 + 8): Ana finds 8 more and ends up with 21; the shells pile up and the gulls look puzzled. "Hmm, that's not what happened. Try another card."

**Story types.** Add to, take from, put together, take apart and compare, with the unknown at the end, the change or the start ("Some birds sat on a wire. 4 flew away. Now 9 are left. How many were there at first?").

**Three groups (1.OA.2).** "3 red apples, 5 green, 7 yellow. How many?" Cards: 3 + 5 + 7 = ?, 3 + 5 = ?, 7 - 3 = ?.

**Compare (the aha).** "Mia has 9 stickers. Leo has 6. How many more does Mia have?" Both 6 + 3 = 9 and 9 - 6 = 3 replay true. "Adding or taking away, both fit this story!"

**The end.** A playbill of every show with its sentence. `Print` prints it.

**Act it out (extra).** A pause before the replay so the class acts with real objects.

## Content
- Fifteen shows within 20 across five types and three unknown spots, three three-group shows, made-up cartoon kids labeled "illustration", all spoken. Nothing is broken or lost for good; wrong replays are funny, never sad.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- `Watch again` replays the story before the question at any time.
- Keyboard: Tab to the curtain, counters, the tray and cards; Enter picks and places.
- With Motion off the replay shows still frames with captions.

## Look
- Accent `--brand` #9b1c31 curtain crimson (header, curtain, buttons); gold #f4c542 (the chosen card, the spotlight); paper #fcf0f2; ink #2a0710; muted #5e4b50.
- Contrast (WCAG 2.1, computed): white on brand 8.06:1; brand on paper 7.25:1; ink on paper 16.62:1; muted on paper 7.27:1; ink on gold 11.36:1.
- Never color alone: the right card gets a check and words; counters are all one color with numbers on demand.
- Different from this batch (leaf green, bead teal, river blue, factory orange).

## Art
- People (illustrated): five cartoon kids from different families (Ana, Mia, Leo, Sam, Kai), labeled "illustration" (Gemini, `people: true`, 5; cutout yes).
- Local FLUX (`scripts/localart.py`): the stage (1, 16:9), three story settings (beach, orchard, wire and sky) (3, 16:9), birds, shells, apples, stickers (4, 1:1).
- Drawn in code: counters, the tray, cards, the playbill.
About 13 images.

## Voice
Two bank voices, each unique in this batch: `lively-host` as the show narrator; `curious-librarian` as the hints. `Curio.voice` with `scope: () => state.mode + ':' + state.show + ':' + state.step + ':' + state.line`, `welcomeAfter: true`.
- how `welcome`: as on load.
- how `act`: "Drag counters to act it out."
- how `pick`: "Tap the number sentence that fits."
- event, whole, each show.
- event, whole, each replay.
- event, whole, compare (the aha).
- event, whole, `end`.
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None (family "none"). Tool-only code: the show player that replays from a sentence, the counter tray, the cards. Shows sit in a marked block `/* STORY-REPLAY DATA: begin */ ... /* end */`.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Pick | Tap cards until one fits | Each wrong replay shows why; the next show changes type. |
| Counters | Skip acting out | Allowed; the replay still tests the sentence. |
| Compare | Always add | Both fit only in compare shows; take-from shows need subtraction. |

## Heard in order
Waits means the next line or tap waits for it to finish; taps act at once and never wait.
1. Load: `welcome` (queued).
2. Show (whole), waits. `act`; `pick`.
3. Replay (whole), waits.
4. Compare (whole), waits.
5. `end` (whole).

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CCSS wording for 1.OA.1, 1.OA.2 | National Governors Association Center and CCSSO, "Common Core State Standards for Mathematics" (2010) | data/standards/ccss-math-clusters.txt | yes |
| The problem types (add to, take from, put together, take apart, compare) and unknown positions | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking", Table 2 | Carpenter and others, "Children's Mathematics: Cognitively Guided Instruction" (1999) | yes |
| Start-unknown and compare problems are the hardest for first graders | Common Core Standards Writing Team (2011), "Progressions for the CCSS, K-5 Operations and Algebraic Thinking" | Carpenter and others, "Children's Mathematics: Cognitively Guided Instruction" (1999) | yes |
Backed twice: 3. Cut: 0.

Checks run (Python, scratchpad r7, 2026-11-10): 8 + 5 = 13 and the wrong card gives 21; 3 + 5 + 7 = 15; 9 - 6 = 3 and 6 + 3 = 9; every total is 20 or less; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 stage over tray; at 680x425 one row.
2. Fifteen shows cover five types with the unknown in all three spots. (1.OA.1)
3. A compare show replays true for both an addition and a subtraction sentence. (1.OA.1)
4. Three three-group shows total 20 or less. (1.OA.2)
5. Every card is spoken; every control is 56 px or more.
6. The cartoon kids are labeled illustration; wrong replays are funny, never sad.
7. Tap while it plays: a tap during a line acts at once; no older line plays after a newer one.
8. Motion off: still frames; no network requests.

## Open questions
None.

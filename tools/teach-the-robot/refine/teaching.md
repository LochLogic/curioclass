# Teaching lens: teach-the-robot (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json, tool.draft.json; bundled with
`CURIO_DRAFT=1 python scripts/bundle_tool.py teach-the-robot` (112 KB). Numbers recomputed in Python (independent
k = 1 nearest neighbor over the six features, exact-fraction tie check). Frames and voice runs with
`scripts/drive.py` (held clicks), own profile, ports 9500-9507. Scratch: lens-ttr-teaching (calc.py, calc2.py,
frames f1 to f6).

Counts: blockers 2 (general 1, family 1), should fix 1 (general 1), polish 4, nit 2.

## Standards (rule 2)

- **E2-ALG-ML-02** (module: "How data trains a machine learning model"): taught by doing. The class labels examples,
  Kip guesses from them, and the parade score and chart show what the data did. Taught, but B1 and B2 both damage
  what the data appears to teach.
- CSTA 1A-DA-07 (crosswalk only) and AI4K12 Big Idea 3 (reference): see P1 and N1.

## Done when

| # | Result | How checked |
|---|---|---|
| 1 | pass | held clicks stage, Next pet, Cat (8 s gaps): teachWelcome, catOrDog, remCat all spoken; wall `Marmalade:cat` (f4 v-dw1) |
| 2 | pass | 2 cards: 4 of 10; misses Rusty, Luna, Noodle, Pippin, Waffles, Bramble (Python and tool agree) |
| 3 | pass | 16 cards: 10 of 10; chart bars carry their paw counts (2, 11, 12, 16, 2 in f2 parade-runs) |
| 4 | pass | 11 cards: 9, Pippin missed; plus Ziggy: 10, line 29 "more" then line 33 "better" spoken (f4 v-better2) |
| 5 | pass as written | Marmalade as dog: 6 vs 4; Forget puts Marmalade at the deck front; relabeled cat: 4 again (f5 d5). But see B2 |
| 6 | pass | 10 truth frames (f2 ptruth01-10): one line, ending on the card Python picks; truth matches the table; no distance ties at any minimum |
| 7 | pass | five Next/label rounds: catOrDog spoken 1, silent 4; tryMystery spoken 1, silent 3; startHow spoken 1; score line every run (3 of 3); "same" 2 of 2; againHow spoken 1, then silent |
| 8 | pass | Next pet, Cat, Dog, Mystery pet, Start parade on screen and 60 px tall at 680x425, 1366x768 and 375x812 (host iframe, no horizontal scroll) |
| 9 | pass | Motion off: slots 2.64 s apart (1842 to 25642 ms), score 4 |

Facts: the parade score table for N = 1 to 16 (4, 4, 5, 7, 8, 8, 8, 8, 8, 9, 9, then 10), the six 2-card misses and
their look-alikes (Marmalade for Rusty, Noodle, Pippin, Waffles; Bear for Luna, Bramble), Pippin fixed by Ziggy and
Waffles by Pudding all match the spec and notes. Sources and attribution are as stated.

## Findings

**B1. blocker, family:ml-lab. The dogs are drawn as cats, so the class's labels and the "truth" disagree with what
the class sees.** (src.html `drawHead`/`drawPet`; frames f1 deck06 Rocket, deck10 Pudding, deck12 Ziggy,
f1 pippin-truth, f2 ptruth07 Pippin, ptruth10 Juniper.) Every pet has the same cat body: long whiskers, an upright
curled tail, a small round muzzle. The snout value (.15 to .75) barely changes the muzzle, so it is not the visible
clue the spec says it is. Rocket and Ziggy look like cats; Juniper (dog) and Bramble (cat) look almost the same;
Pippin, the talk-point pet, reads as an orange cat. The core action is "Say it out loud. Then tap Cat or Dog" and
labels are never checked, so a grade 2 class will call Ziggy and Rocket "cat". Then the score table, Done-when 4 and
the Ziggy-fixes-Pippin lesson stop happening. When the truth badge says "Dog" over Pippin, children will decide
Kip was right and the tool was wrong; the notes' question "Why did Kip think Pippin was a cat?" gets the answer
"because it is one". Better: every dog reads as a dog at a glance, including the pointy-eared and short-nosed ones.
Let the snout value drive a clearly longer muzzle with a dog nose pad, draw low whisker values as short stubs or
dots, and give dogs a dog tail. If a cue Kip does not use is needed, that is fine (and a talk point: people use more
clues than Kip). The ear and snout data may need retuning with the drawing; judge it by frames, not numbers.

**B2. blocker, general. The wrong-label experiment the notes suggest makes Kip score higher.** (notes.md "Talk
about it" item 4 and "Good to know" item 3; tool.draft.json outcome "wrong labels make them worse"; calc2.py.)
Labeling Marmalade as a dog raises the parade score at every memory size from 1 to 9 cards (2 cards: 6 vs 4;
5 cards: 9 vs 8; 9 cards: 9 vs 8), and the tool then says "That's more than last time!", the opposite of line 31's
lesson. Root cause: 6 of the 10 parade pets are dogs, so with 1 or 2 right cards Kip (4 of 10) does worse than a
robot that always says dog (6). A Marmalade-as-dog card catches Pippin and Waffles: right answers for the wrong
reason. Other cards behave (at 5 cards, mislabeling any other card drops the score to 6 or 7). Better: data in
which an early wrong label lowers the score (for example a 5 and 5 parade, or retuned Marmalade, Pippin and Waffles),
and notes that name a mislabel that clearly hurts. Rerun the full mislabel table (calc2.py) after any data change.
This changes spec numbers, so it is a spec fix.

**S1. should fix, general. "Show Kip more pets" when no pets are left.** (src.html `paradeHow`, and `startParade`
queuing `againHow`.) After all 16 cards, every parade ends with "Tap Teach and show Kip more pets. Then run the
parade again." In Teach, Next pet then answers "That's every example card! Tap Pet Parade", a loop. Seen in f2
parade-runs and by reading the code (no deck check). Better: once the deck is empty, the parade hint says something
true, such as "Kip has seen every pet. Try Forget, or Start over to teach Kip again."

**P1. polish, general. Nothing on screen invites the class to predict Kip's guess.** (Mystery think phase, 1.2 s;
spec "Who and how" says the class predicts Kip's guesses; CSTA 1A-DA-07 crosswalk.) The prediction lives only in
the notes ("Ask first: What will Kip say?"). Better: during Mystery's think, the hint and line say "What will Kip
guess? Say it out loud!" and the think holds a beat longer, so the class predicts before the look-alike line draws.

**P2. polish, general. Line 10 blames missing examples even when a wrong label caused the miss.** ("Oops! Kip
guessed wrong. Kip needs more examples.") During the wrong-label experiment this points the class at the wrong cause.
Better: when the deciding card's label differs from that pet's real label (the deciding card is known), use a line
like "Oops! Kip remembered that pet wrong."

**P3. polish, general. Line 33 teaches "more" when the data teaches "different".** ("The more examples Kip saw, the
better Kip guessed!") Cards 5 to 9 add nothing (8 stays 8); Ziggy alone fixes Pippin; the notes say "Kip needs an
example like the new pet, not just more of the same." Better: "The more different pets Kip saw, the better Kip
guessed!"

**P4. polish, family:ml-lab. In the parade, Kip's guess shows only 0.6 s before the truth badge.** (`startParade`:
line 0.3 s, hold 0.3 s.) The spec says guesses are shown, not spoken, "so the class can call them out"; in 0.6 s a
class can only react to the check or X. Better: hold the guess about 1 s before the truth and keep 2.6 s per pet by
shortening the walk or the truth hold.

**N1. nit, general.** The spec and code paraphrase 1A-DA-07 as "identify and describe patterns in data to make
predictions"; the standard says patterns "in data visualizations, such as charts or graphs". Kip's Chart is one: a
notes prompt such as "Look at Kip's Chart. What will happen if we teach four more pets?" would use it.

**N2. nit, general.** Notes and spec say Waffles is fixed "only by Pudding". Scout (card 16) also fixes it (distance
.534 vs Marmalade .545), which shows if Pudding is forgotten after all 16 cards. Say "Pudding fixes it first".

## Guardrails and sensitivity

K-2 teacher led; no hard history, health or cultural content; the only score is the parade tally, which is the
measurement. Language is plain and short for grade 2. Rule 8: no sensitive topics in scope. Nothing to flag for a
sensitivity agent.

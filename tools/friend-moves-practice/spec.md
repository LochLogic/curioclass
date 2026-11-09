# Friend Moves Practice

## One idea
The student steps into four short playtime scenes as the new kid in class (joining a block tower, sharing the last red crayon, taking turns on the swing, bumping someone's sandcastle), and at the key moment picks a friend move with real words to say, then sees the other kid's face, hears their words and watches what happens next, rewinds to try another move, and practices what to do when a friend says "not now", so they learn to ask to join, share, take turns and fix a small mistake with words.

## Not like
- conflict-coach (6-8, live): I-statements for bigger conflicts. Here first friend moves for K-2.
- feelings-faces (K-2, live): naming feelings on a board. Here acting on them with a friend.
- recess-upstander (3-5, idea): standing up for someone being picked on. Here making and keeping friends.
- talk-moves-trainer (3-5, spec): moves in a book discussion. Here moves at play.
- i-choose-because (K-2, spec): choosing and saying why. Here choosing what to do with another kid.

## Who and how
- Grades K to 2, Social and Emotional Learning, module "Making and Keeping Friends". Standard: CASEL Relationship Skills (communicating clearly, cooperating, resolving conflicts, seeking and offering help).
- Driver: one student, or a teacher on the projector with the class choosing together ("Class choice": tool.json `driver: "student"`). Every card, line and button is read on tap; controls are 56 px or more.
- Four scenes plus a "Not now" practice for each and a Fix-it scene. No reading is required. tool.json `modes: ["Play spots", "My friend moves", "Class choice"]`, `minutes: "10-15"`, `grades_label: "Grades K-2"`.
- Nothing is saved; `Print` prints the friend moves pocket as a take-home card.

## Standards map
| Code | Student action that teaches it | What they see | Done when check |
|---|---|---|---|
| CASEL Relationship Skills (communicating clearly) | Pick a move with words ("Can I build too?") and hear your kid say it | the friend's face and words | 2 |
| CASEL Relationship Skills (cooperating, sharing, taking turns) | Choose share and turn moves in the crayon and swing scenes | what happens next in play | 3 |
| CASEL Relationship Skills (handling "no" kindly) | Choose a next move after "Not now" (wait, ask later, find another game) | the friend coming back or a new game starting | 4 |
| CASEL Relationship Skills (resolving conflicts) | Say sorry and offer a fix after the bump | the different face for sorry plus fix | 5 |

## Screens and modes
Header (kit): title "Friend Moves Practice"; `Play spots`, `My friend moves`; `Read`, `Motion`, `Sound`, `Print`. Controls 56 px or more, icon plus word.

**On load and first tap.** A bright classroom playroom with four glowing play spots: a block corner, an art table, a swing set through the window, a sandbox. The student's kid, Pip (choose a look from six), stands at the door with a backpack. First hint: "Tap a glowing spot to play there." The first tap walks Pip there; the welcome is queued after it (`welcomeAfter: true`).

**A scene.** Each scene plays a few seconds and stops at one moment, with three move cards (picture plus words, all read on tap):
- Blocks: Mina is building a tower. Cards: "Can I build too?" (ask to join); grab a block and add it (no words); stand and watch.
- Crayons: one red crayon left, and Jamal needs it too. Cards: "Can we take turns? You first." (share); "Mine!" and grab it; "I'll use orange." (a fine choice too).
- Swing: Rosa has been on the swing a long time. Cards: "Can I have a turn after you?" (ask for a turn); push in front; walk away sad.
- Sandbox: Pip bumps Leo's sandcastle by accident.
The student taps a card and hears Pip say it. The friend's face changes (clear, big expressions) and they answer: "Sure! Get the blue ones." or "Hey, I was using that." Then play continues for a few seconds to show what happens next. `Try another move` rewinds to the moment.

**Not now.** Each scene has a second run where the friend answers a good ask with "Not now, I'm almost done." Three next-move cards: wait and watch, "Can I play when you're done?", find another game nearby. Each works in its own way; giving up and walking away sad is shown kindly as a choice that leaves Pip alone, with "Try another move."

**Fix-it.** After the sandcastle bump: "Sorry." alone gets a small nod and a sad face; "I'm sorry. Can I help build it back?" gets a smile and the two build it together. "It wasn't me!" gets a frown.

**My friend moves.** A pocket fills with the moves that worked, each with its picture and words, ready to print as a card for recess.

**Class choice.** On the projector, the class picks the move together.

At 1366x768 the scene and cards fit; at 680x425 cards stack below the scene.

## Content
- Four scenes, Not now runs, the Fix-it scene and all lines written for Curio Class, with short, kind words a K-2 child can say.
- No move is called "bad"; each card's result is shown honestly, and the hint says what to try next.

## Interactions in detail
- Every tap acts at once; a new line stops the old one.
- Rewind is always available; there is no score.
- With Motion off play shows as two still frames (the moment and what happens next) and faces change without animation.

## Look
- Accent `--brand` #a84600 playroom orange (header, play spots, move card frames); gold #f4c542 (the glowing spot, moves in the pocket); paper #fff5ec; ink #2b1200; muted #6b5444. Scene: a sunny classroom playroom.
- Contrast (WCAG 2.1, computed): white on brand 5.93:1; brand on paper 5.51:1; ink on paper 16.42:1; muted on paper 6.56:1; ink on gold 10.86:1.
- Never color alone: every card has a picture and words; faces carry the feedback along with the friend's words.
- Different from this batch (plaza green, rally red, lab blue, plum).

## Art
- People art goes to Gemini: Pip in six looks (varied skin tones, hair and one with a hearing aid), 4 poses each; Mina (a Korean American girl), Jamal (a Black boy), Rosa (a Mexican American girl), Leo (a white boy with glasses), each about six, with 5 clear expressions (happy, surprised, sad, frowning, smiling) and 2 action poses; "illustrated kindergarten child <expression or pose>, soft gouache, plain white background, big clear face"; 1:1; cutout yes.
- Local FLUX (`scripts/localart.py`): the playroom (1); block corner, art table, swing set and sandbox backdrops (4).
About 57 images. Drawn in code: move cards, the pocket.

## Voice
Bank voice `warm-teacher` as the hint voice and the reader of cards (unique in this batch); Pip is read by `playful-friend`, Mina and Rosa by `big-sister`, and Jamal and Leo by `hero-coach` (each unique in this batch), all styled as young children. `Curio.voice` with `scope: () => state.scene + ':' + state.run`, `welcomeAfter: true`.
- how `welcome`: "You're the new kid. Pick a play spot, then choose what to do and say."
- event `card`: the move card's words.
- event `pip`: Pip saying the move.
- event `friend`: the friend's answer.
- event `notnow`: "Not now, I'm almost done."
- event `pocket`: "That one worked. It's in your pocket."
Read speaks the hint, which names the next action and control and never a disabled one.

## Family engine
None. Tool-only code: scenes with a stop moment, move cards with results, rewind, Not now runs, the Fix-it scene and the pocket.

## Can it be beaten?
| Check | Ways to pass without the skill | Why each fails |
|---|---|---|
| Moves | Tap any card | Each card shows its own honest result; only moves that worked go in the pocket. |
| Not now | Ask again right away | The friend says "I'm still busy"; the pocket needs a next move. |
| Fix-it | Say sorry only | Sorry alone gets a nod, not the build-it-back ending. |
There is no score to beat, by design.

## Heard in order
Waits means the next line waits for it to finish; taps act at once and never wait.
1. Tap a spot: `welcome` (queued, first time).
2. At the moment: `card` on tap; after choosing, `pip` (waits), then `friend`.
3. Not now: `notnow`; then the next move. A working move: `pocket`.

## Sources
| Claim | Source 1 | Source 2 | Agree? |
|---|---|---|---|
| CASEL Relationship Skills include communicating clearly, cooperating, resolving conflicts constructively, and seeking or offering help | CASEL, "What Is the CASEL Framework?" (casel.org) | CASEL, SEL competencies wheel (2020 update) | yes |
| Young children's peer entry goes better with asking or joining the play's theme than with disrupting it | Putallaz and Gottman, "An interactional model of children's entry into peer groups" (Child Development, 1981) | Dodge, Schlundt, Schocken and Delugach, "Social competence and children's sociometric status: the role of peer group entry strategies" (Merrill-Palmer Quarterly, 1983) | yes |
Backed twice: 2. Cut: 0.

Checks run (Python, scratchpad b28, 2026-11-09): every scene has three cards, at least one of which works and goes in the pocket; every Not now run has at least two working next moves; the Fix-it scene's three cards give three different endings; contrast as in Look.

## Done when
1. Focus and fold: at 1366x768 scene and cards fit; at 680x425 cards stack below.
2. Each move plays Pip's words, the friend's face and answer. (CASEL Relationship Skills)
3. Sharing and turn moves change what happens next. (CASEL Relationship Skills)
4. Not now runs offer next moves that work. (CASEL Relationship Skills)
5. Sorry plus fix gets a different ending than sorry alone. (CASEL Relationship Skills)
6. Rewind works everywhere; the pocket fills and prints.
7. Class choice works; every tile and card is read on tap.
8. Tap while it plays: any tap during a line acts at once; no older line plays after a newer one.
9. Motion off: still frames replace play; no network requests.

## Open questions
- None for Cory.

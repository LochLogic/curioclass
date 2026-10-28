# Play lens: teach-the-robot (round 1)

Cold read of spec.md, src.html, notes.md, voice/lines.json; bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py
teach-the-robot` (112 KB). Driven with `scripts/drive.py` (held clicks, muted Chrome, own profile, ports 9510-9515),
frames in the lens scratch folder (f1 to f5). Played twice: as a grade 2 student alone (real clicks only, hint and
voice log polled every 200 ms) and as a teacher projecting at 1366x768.

Frames looked at: default, Next pet wait, labelled, Mystery think, guess and truth (2 cards and 16 cards), card
selected with Forget, deck used up, Parade default, mid parade, parade end (4 runs and 9 runs, chart at 8 bars),
empty-wall Start parade and Mystery, Start over, Forget; each of 680x425, 800x500, 1000x625, 1280x720, 1920x1080,
760x900 (default, wait, 16-card truth, selected, parade end) and 375 wide in the iframe host; Motion off; every one
of the 16 deck pets and 10 parade pets in the spotlight. No console errors (one favicon 404 from the test host only).

Counts: blockers 0, should fix 6, polish 7, nit 2.

## Should fix

1. **Several dogs are drawn as cats, so the class labels them wrong in good faith.** (stage drawing, `drawHead` /
   `drawPet`, src.html:324-409) Seen in the per-pet frames (f4/g06, g12, p07, p10 and the dogs.png crop): Rocket,
   Ziggy, Pippin and Juniper are pointy-eared, whiskered, upright-tailed animals any 7-year-old calls a cat. The snout
   clue, which is the strongest cat/dog difference in the data (cats .15-.30, dogs .50-.75), is drawn as a small
   muzzle oval that barely changes; on dark coats the ears vanish (Bear's .50 ears sit behind the ruff, Moose's
   floppy ears are coat-dark on coat-dark), and every pet has the same upright cat tail. Teach never checks labels, so
   a class that says "cat" for Ziggy breaks the tool's own talk point (Ziggy is the only card that fixes Pippin), and
   in Parade a big "Dog" badge lands on a cat-looking picture, which reads as the tool being wrong. Better: make the
   snout read as a real dog snout at high values (longer, deeper muzzle, visible nose at the tip), show floppy and
   half ears in a lighter or outlined shade on dark coats, and let the tail follow a clue (or be neutral) so it does
   not say "cat" on every pet. Keep Pippin and Juniper honestly tricky, but tricky to Kip, not to the class. general.
2. **Start parade with an empty wall: nothing for about 5 s, then a line naming a hidden button.** (Parade,
   `startParade`, src.html:855) Real clicks Pet Parade then Start parade (f2/21): the welcome keeps playing, the
   "empty" line only starts at 4.7 s and says "Tap Next pet first!", but Next pet is hidden in Parade. The Teach pulse
   that should point the way is invisible: `.pulse` is on `#m-teach` (class and box-shadow confirmed, f3/c-pulse) but
   the `.seg` has `overflow: hidden`, which clips the ring. Better: the tap's own line cuts the welcome (hush first), a
   Parade version of the line names Teach ("Kip doesn't remember any pets yet. Tap Teach first!"), and the pulse shows.
   general.
3. **Event lines replace the hint and leave no next step.** (Teach: after a Mystery result, Forget, Start over) Polled
   hints (f2/22, 27, 28): the hint ends on "Yes! Kip got it right!", "Oops! Kip guessed wrong. Kip needs more
   examples.", "Kip forgot that one." or "Starting over! Kip's memory is empty." and stays there. A solo student
   pressing Read hears only the result, not what to tap next (rule 4, "say how to act"). Better: after the event line,
   the hint falls back to the current how-to (teachHow(): Next pet / Mystery pet), silently. general.
4. **The "Kip looks..." teaching line plays on every Mystery pet and runs about 2 s behind the screen.**
   (`mystery`, src.html:802-812) Five Mysteries in a row (f2/24): the 4 s line is spoken 4 times (once dropped). Kip
   thinks only 1.2 s, so the look-alike line and Kip's guess are on screen while the voice is still on "looks the
   most alike"; "Kip thinks it's a cat!" comes at 4.5 s, two seconds after the cat face appeared, and the truth waits
   for it. By the third pet it is the slow part of every round. Better: treat it as a teaching line (spoken the first
   time, hint after), and hold the thinking swirl until it ends that first time, so the guess lands right after the
   words. general.
5. **Shelf counters say "8 of 16" when the deck is finished.** (stage, `drawShelves`, src.html:538) Frames f1/09, f1/12
   and every 16-card frame: each shelf shows 16 slots and "8 of 16" while the panel says "That's every example card!".
   A class reads that as eight more cats to find. Better: show only the count with the icon (or "8 cats") and let
   empty slots grow with the wall rather than promising 16 per shelf. general.
6. **"Show Kip more pets" when there are none.** (Parade end, `againHow`) Frames f1/12, f1/13: after all 16 cards and a
   10 of 10 run, the hint (and the first-run voice) still says "Tap Teach and show Kip more pets." Words don't match the
   state. Better: when the deck is empty, a different how-to (for example try a wrong label, or Start over), or no
   prompt to teach more. general.

## Polish

1. **Kip's guess is on screen for only about 0.6 s in the parade.** (`startParade`, src.html:867-873) Think 0.4 s,
   line 0.3 s, then 0.3 s before the truth badge. The class is meant to call out Kip's guess, but the cat or dog face
   barely shows before the check or X covers the moment. Better: hold the guess about 1 s before the truth (the
   2.6 s per pet can come from a shorter truth hold or walk). general.
2. **The end of the parade is flat on the stage.** (f1/12) Kip shows its idle face at "10 of 10", the same as at "4 of
   10". Better: Kip's screen reacts to the score (a big smile and blinking antenna for a high score, a thinking face
   for a low one), which is the moment the class has been counting toward. general.
3. **In the preview size the pet is tiny.** (680x425 and 800x500, f3/s680x425-wait) Two rows of empty dashed slots per
   shelf take over half the stage; Marmalade is about 55 px wide and Kip about 60 px tall. Better: lay out only the rows
   the wall needs now so the pet and Kip get the floor. general.
4. **The glow on a top-left matched card covers the shelf chip, and the line's end dot sits on the card's name.**
   (f1/05, f1/06: Marmalade; f3/s1920 truth: "Zig.."). Better: end the line at the card's lower edge beside the name,
   and keep the glow inside the shelf. general.
5. **Chart and score text are small for a projector.** (Kip's Chart: axis 11 px, bar values and memory counts 12 px;
   slot numbers 12 px.) The class counts bars together. Better: about 16 px values and memory counts at 1366x768. general.
6. **Teach panel at 1366x768 is half empty.** (f1/01 to f1/09) Below "Kip remembers" there are ~350 px of blank panel
   while the paws are 16 px. Better: a bigger memory counter (larger paws, maybe split by cat and dog icons), which is
   the number the parade chart talks about. general.
7. **Deck used up, Next pet still looks like the main move.** (f1/09) The hint says tap Pet Parade, but the big blue
   button is Next pet; tapping it just repeats the line. Better: pulse Pet Parade when Next pet is tapped with an empty
   deck (and fix the clipped pulse, should fix 2). general.

## Nits

1. After a label, the hint keeps "Then tap Cat or Dog." for about a second after Cat and Dog are dimmed (until "Kip
   remembers" starts) (f2/20). general.
2. At 680x425 with a card selected, the paws row is cut at the bottom of the panel (f3/s680x425-select). general.

## Checked and fine

- First screen says what to do (welcome names Next pet); first tap on the stage or Next pet behaves (welcome on a
  stage tap, Next pet's own line otherwise); Sound off then on brings the welcome once; Read during a line reads the
  hint.
- How-to lines once: "Cat or Dog" and "Now tap Mystery pet" each spoken once in five label rounds; "Kip remembers"
  every time; results every time.
- Next pet, Cat, Dog, Mystery pet and Start parade visible and 60 px tall at every size checked, including 375 wide.
- Motion off: no walking, same timing (Mystery 4449 ms off vs 4438 ms on), same scores.
- Parade scores match the spec at 1, 2, 3, 4, 5, 10, 12 and 16 cards; the chart keeps 8 bars and stacks equal runs;
  "10 of 10" on the stage and in the panel match.

# target-toss: Play lens (round 1)

Played cold, mostly as a K-2 PE teacher running a block on a projector (tapping where each ball hit at about one tap a
second while the class waits), once as a non-reading K-2 child watching the screen. Draft bundle 95 KB. Real held
clicks over CDP (own runner on drive.py's Chrome, port 9972), frames at every STANDARDS size, 375 through
`drive.py --host` (port 9973; host.html deleted after). No console errors in any run.

Runs: (1) full Test it, "Close or far?", 10 + 10 real taps at 1 s, Look, Show the answer, voice log; (2) Free throw,
17 real taps at 1 s (5 above, 5 hits, 5 side, 2 Too short), then Clear; (3) Form: Show me, Throw with Bo, Overhand +
Left hand, Next cue x6 at 1 s, cue cards; (4) nine states (Ask, Guess far, Way A 20 throws, Way A done, Way B small
target, Look 20 answered, Look 5 answered, Free throw 43 throws, setup card) at 680x425, 800x500, 1000x625, 1280x720,
1366x768, 1920x1080, 760x900 and 375 host. Tap counts checked by hand: Way A 7 of 10, Way B 7 of 10, graph showed 7
and 7 (tie). Coach lines matched the rules (Too high, Great aiming, side tip).

## Blockers

None.

## Should fix

1. **Stop test and Clear the wall wipe everything with one tap, and sit right next to Undo.** (general)
   Where: `#t-stop` beside `#t-undo` in the Test round row (src.html:211-215, `stopTest` 1024); `#r-clear` beside
   `#r-undo` (src.html:226-230, `freeClear` 1058). Same size, same style, no confirm, no way back. Seen in frames
   t1-04, f-shorts; after Clear, Undo is disabled and 17 throws were gone (run 2). A teacher reaching for Undo after a
   stray tap, with 20 kids watching, can lose a whole Way A plus Way B (up to 40 throws) or a Free throw session. The
   mode buttons and keys 1 to 3 also reset a test in progress with no prompt. Better: make Stop test and Clear undoable
   (one "Undo clear" / "Bring it back" for a few seconds) or a two-tap confirm, and move them away from Undo (own row,
   quieter style).

2. **Start Way B appears exactly where Undo was.** (general; BR1 lesson "nothing rebuilds under the pointer", "panels
   don't jump")
   Where: `#t-startb` (src.html:210) is shown above the Too short / Undo / Stop row when Way A fills. At 1366x768 the
   row was at y 459-519 (probe); after throw 10, Start Way B occupies y 460-518 and the row drops to 528 (frame
   t1-05). The likeliest moment for an Undo is right after a mis-tapped last throw, and that tap now lands on Start Way
   B, which can't be undone back into Way A. Better: reserve the slot (Start Way B in its own fixed place, or the row
   above it), so nothing moves under the finger.

3. **No recovery from a mis-tapped last throw of Way B.** (general)
   Where: `roundThrow` (src.html:986-989) moves to Look 1.3 s after throw 10; Look has no Undo (`#tg-look`). At a
   1 tap/s pace the teacher sees the wrong dot after the screen has already changed (run 1, frame t1-08 then t1-09). The
   only fix is Stop test and redo both rounds. Better: keep an Undo (or "Back to Way B") on the Look step until Show
   the answer, or stay on Way B with a "See the results" button like Way A's Start Way B.

4. **Misses above the target are hidden under the Way banner in every Test round.** (general)
   Where: `#banner` (src.html:115, placed in `placeOverlays` 836) sits directly above the target, and `targetBox`
   leaves almost no wall above the rings in Test it. A tap at ny -1.18 and -1.25 (real taps, run 1; scripted in the
   size sweep) is counted as a miss in the ten-frame, but its dot is drawn under the banner and never seen, at all
   eight sizes (t1-05, roundA20-*). "Too high" is the most common K-2 miss and the teacher can't check the tap landed.
   Better: draw ball dots above the overlays, or move the banner off the throwing area (into the strip row or the
   panel) and leave a band of wall above the rings.

5. **Guess step has no way back.** (general)
   Where: `#tg-guess` (src.html:194-206). No Stop test or Back on the Guess step (frame t1-02, guessfar-*); the
   handoff says "Stop test is also shown on the Guess step", but it is not. A teacher who tapped the wrong question
   card has to know to press the Test it mode button again. Better: a "Back" / "Other question" button on the Guess step.

6. **"Now Way B! Same throwers, same line." is wrong for Close or far?** (general; words match the state)
   Where: `L.startB` (src.html:313), spoken in run 1 at the start of Way B for "Close or far?", where Way B is "Throw
   from the far line" (banner in frame t1-08 says so). It contradicts the screen and the fair-test idea. Better: a
   per-question line, or "Same throwers. Only one thing changes."

7. **The Free throw welcome says "Throw at the target!" while the screen shows only a big target.** (general; BASELINE
   w1-49)
   Where: `L.wFree` (src.html:301), also the Free throw hint (frame f-00-start). The setup is a paper target beside
   the screen and the safety tip says never throw at the screen; a K-2 child who hears "Throw at the target!" while
   looking at a huge projected target is told the opposite. Better: "Throw at the paper target! Then tap the screen
   where each ball hit." Check the other lines the same way (startA "Tap where each ball hits" is fine).

8. **The setup card leaves the hint (and Read) on the old step, and its steps fall below the fold in small boxes.**
   (general; BR1 lesson "the hint changes at once, Read speaks it")
   Where: `openSetup` (src.html:1108) never sets the hint; the setup line is `hint: false`. With the card open the
   hint still says "Let's learn to throw like Bo. Press Show me..." (setup-* frames), so Read speaks that, not the
   setup. At 680x425, 800x500, 375 and 760x900 the card scrolls and steps 3 and 4 ("Throw soft balls at the paper
   target", "Then tap the screen") are out of view (setup-a sheet); at 760x900 even the picture's labels are cut.
   Better: set the hint to the setup steps (and back on Close), and let the card use the whole page or a side layout
   so all four steps show.

## Polish

1. **The way name comes last in a round intro.** (general) First run of a session: "Way A! Throw one at a time. Tap
   where each ball hits." then "Way A:" "Throw from the close line." took about 10 s (log 8.7 s to 19 s); for Way B the
   way name ("Throw from the far line.") was still playing at 32-35 s, after throw 8 of 10. Non-readers need the way
   before they throw. Better: speak "Way B: throw from the far line" first, then the how line.
2. **Throw with Bo has no time to do each move.** (general) Each cue starts as soon as the last one ends (log:
   cues 1.5 to 2.9 s apart; minimum beat 1400 ms, shorter than Show me's 1600). A class shadowing a throw needs a beat
   after hearing the cue. Better: a hold of about 1 s after each spoken cue in Throw with Bo (a real "slow beat").
3. **On a projector the score lives in a small side panel.** (general) In a round the stage shows only the target;
   "Throw 3 of 10" (19 px), "Hits: 3" (16 px muted) and a small ten-frame are in the 360 px panel, unchanged at
   1920x1080 (roundA20-1920x1080). The class at the back can't follow the count. Better: a large ten-frame or count
   on the stage (the floor strip has room), as Free throw does with its tally.
4. **Payoff text is small at 1920x1080.** (general) The answer card (`--afs` max 18 px) and Guess cards (way text
   about 20 px in 480 px cards, mostly empty) don't grow on a big screen (look20-1920x1080, t1-02). Better: let them
   scale with the stage like the "13 hits" numerals do.
5. **First coach line is lost at a 1 tap/s pace.** (general) Run 2: the coach line after throw 5 waited behind the
   safety line and welcome (about 10 s of speech) and was dropped when throw 6 came. The card shows it, so nothing is
   lost on screen. Better: let a coach line cut in ahead of a welcome, or shorten the opening lines.
6. **The "Close or far?" tip after Show the answer is a setup instruction.** (general, spec level) After the result
   the tip card says "Make two tape lines: three giant steps..." (t1-11), which belonged before the test. Better: a
   takeaway line ("Closer is easier. Step back when you are ready for a challenge."). This is in the spec's table, so
   it goes to the spec's open questions.

## Nits

1. Guess Way A, result a tie: "That's different from our guess." A tie line ("It came out even!") would fit better.
2. After switching Overhand or Left hand, the hint still says "Great throwing! Press Throw with Bo to go again."
   (fm-over-left).
3. The crown stars on Look touch the bottom of the step strip at 1366x768 and 680x425 (t1-11, look20-a).
4. "Throw 0 of 10" at the start of a round reads oddly; "Throw 1 of 10" (next throw) or "0 throws" would be clearer.
5. ✋ Right hand and 🤚 Left hand icons look almost the same on a projector.
6. Setup picture: the dashed ball path runs through the "Paper target: throw here" label.

## Feel

The Test it loop works and is satisfying: ten-frames filling, the purple and star dots, the big "7 hits" columns, the
crown. A 10-throw round at 1 tap/s took about 10 s of tapping and felt right; 20 throws with two ten-frames stays
readable at every size except a tight 375 Look. 5 throws feels short but is fine for a first test. Form is clear and
Bo reads well at every size. The slow and fragile moments are all around mis-taps: the teacher's recovery controls
(Undo) sit next to destructive ones, move under the finger, or vanish at the end of Way B. No step is boring on a
projector, but the opening speech is long (safety line plus welcome about 10 s before the first coach or round line).

## Frames looked at

s-t1: t1-00 to t1-12 (default, Ask, Guess far, Way A start/5/done/done later, Way B start/done beat, Look, Look later,
answer, answer later). s-t2: f-00-start, f-above, f-hits, f-side, f-shorts, f-cleared. s-t3: fm-show-1, fm-show-3,
fm-show-end, fm-show-after, fm-bo-1, fm-bo-end, fm-over-left, fm-next6, fm-cue4. s-t4: ask, guessfar, roundA20, doneA,
wayBsmall, look20, look5, free, setup at all eight sizes (contact sheets in mont/). Audit frames: size-* and calm.
All in the scratch folder lens-tt-play.

## Teaching lens comparison

(written after the findings above) Agree on "same line" (they rank it a blocker, I rank it should fix; their
fair-test framing is the stronger case, so I would accept blocker), the missing Back on Guess and the long guess
read-out; they add teaching items I did not look for (Way A always the coached way with 👍, same throwers, foot not
voiced, catching, setup ring sizes); I add the mis-tap recovery and projector items they did not cover.

## Audit pilot

Confirmed: 0 leads, and its first-screen checks agree with my frames (no clipping, 60 px controls, no fold problem in
Form at any size, Motion off clean, Form controls speak right). Wrong leads: none.
Missed (all past one click): the banner hiding above-target misses, Start Way B appearing under Undo at the end of
Way A, no Undo after Way B's last throw, Stop test / Clear next to Undo, no Back on Guess, wrong "same line" line,
setup card hint/Read and cut-off steps, the first coach line lost at 1 tap/s, and the projector-scale issues.

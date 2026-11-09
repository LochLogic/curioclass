# Play lens: puppet-show-feelings (round 1)

Cold Play lens, 2026-11-05. Played twice: as a K-2 child alone at home (rule 4), and as a teacher projecting it.
Shared audit: S:/CurioClass-codex-scratch/puppet-show-feelings/audit-r1 (its size, state, Motion off and resize rows are
clean and cited, not re-shot). My frames and logs: S:/CurioClass-codex-scratch/puppet-show-feelings/play/
(frames/, out2.txt, out3.txt, shots1-3.json, zoom-*.png).

Counts: blocker 0, should fix 4, polish 5, nit 1.

## Should fix

1. **Show, first screen: the first instruction skips the first scene.** (src.html:886, 451, 881-883; general)
   On load nothing plays (idle-8s: empty voice log, no babble after 8 s). The hint says "Welcome to the puppet show!
   Watch Pom. Then tap Next." A child who does what it says taps Next and lands on scene 2: scene 1 (Pom and the new
   kite, the happy baseline) is never narrated, babbled or asked about (frames/first-next.png, log: only "Whoosh!").
   The scene only starts from a tap on the theater or Again, and neither is named anywhere; a tap on Motion or the
   Show button also leaves it unplayed (audit one-click table). Better: any first tap starts scene 1 (or Next on an
   unplayed scene 1 plays it), and the waiting hint names the real action, for example "Tap Pom to start the show."
2. **Like me: Pom is cut off mid-body with a hard edge in mid-air.** (src.html:124-125, `.shelf .puppet-window`;
   general, a POLISH.md Art lesson: never crop a character mid-body)
   The sock ends in a straight horizontal cut below the shelf, floating over the wall, at every size I looked at
   (audit state-like-feeling-1366x768.png, state-like-vote-1366x768.png, state-like-feeling-680x425.png,
   frames/like-sad-1366.png). Better: hide the cuff behind the shelf board or a ledge, as Show and Backstage do.
3. **Ending "Dot helps": Dot is mostly hidden behind the left curtain, and the stick runs across Pom's face.**
   (src.html:55, 70; general)
   At 1366x768 only Dot's eye patch and a strip of purple show (audit state-ending-0-1366x768.png); at 1920x1080 and
   375 she is half behind the curtain (frames/ending0-1920.png, audit state-ending-0-375x812.png). The ending is about a
   friend helping, and the friend is barely on stage. The stick crosses Pom's eye and mouth instead of reaching the
   kite in the tree. Better: Dot fully inside the opening beside Pom, the stick from Dot up to the tree.
4. **Sad and worried faces look the same at button size.** (src.html:460-468; general)
   Both are a slanted brow pair over a down-curved mouth; at the 38 px Like me size they are hard to tell apart, and
   calm reads as sleepy (play/zoom-faces.png, audit state-like-feeling-1366x768.png). K and grade 1 children who
   cannot read the word rely on the face, and these two are the feelings the tool most needs them to separate
   (scenes 3 and 4 are worried then sad). Better: worried with raised, pinched inner brows and a small wavy or
   flat-open mouth; sad with drooping outer brows and a clear frown; add simple eyes so faces read as faces.

## Polish

5. **"Only one thing changed, and the feeling changed!" is spent on the first tap.** (src.html:685-691; general)
   From the default (Up, Middle, Small: happy) the very first change, Head Down, flips the reading to worried, so the
   one-time line plays before the child has seen any reading at all (frames/backstage-first-change log: welcome,
   "Say a clue...", flip line). It never plays again (backstage-flip-walk: second flip "silent"), so the Down-Slow-Still
   walk the teacher notes describe never gets it. Better: speak it on the first flip after Audience says has been
   shown once, when the child has a reading to compare against.
6. **The first Backstage change speaks before Pom performs it.** (src.html:694-696)
   The narrator says "Say a clue. Tap Audience says." first and Pom only babbles after the line ends, so the child is
   asked for a clue about a performance not yet seen or heard. "Clue" is also an abstract word for kindergarten.
   Better: Pom babbles at once, then "What did Pom do? Say it. Then tap Audience says."
7. **Show me cuts Pom's babble.** (src.html:807-815)
   The question card and Show me are live from the start of the scene; a tap while the narrator or Pom is talking
   stops the babble, so the voice-speed clue is lost and the answer comes with no performance. Better: keep the babble
   running when Show me is tapped (only the voice lines need to stop), or hold the reveal until the babble ends.
8. **Head icons don't show up and down.** (src.html:777)
   A rotated sock emoji at 24 px reads as three slightly different socks, not Down, Straight, Up (play/zoom-controls.png,
   audit state-backstage-audience-1366x768.png). Voice (snail, shoe, hare) and Bounce (dot, small arc, big arc) read
   well. Better: a small drawn Pom head with a clear down, level and up tilt, or the sock plus an arrow.
9. **Backstage Pom is small for the job.** At 1366x768 Pom fills about a fifth of a wide, mostly empty stage
   (frames/backstage-flip-walk.png, frames/tryit-sweep.png), so the 18 to 28 degree tilt difference is subtle from the
   back of a room. Done when 1 holds, but a bigger Pom (or a stage cropped closer) would make the clues land for a
   projected class.

## Nit

10. **Stage sign text spills over the sign top** at 680x425 and 375 ("Pom" clipped at the sign edge):
    frames/show-ending-choice-680.png, audit state-ending-0-375x812.png.

## What works

- The full Show run as a solo child (frames/show-full-run, out2.txt): every scene line, the question each scene, the
  reveal, the ending choice and its line in order, babble at the right speeds (150, 95, 95, 260, 260 ms). Next is
  disabled on scene 5 and no line names it. Pacing is about 12 s from scene start to the question: room to guess.
- Try it praises a met target and moves on after 2 s (tryit-sweep). It can be solved by sweeping buttons; the notes
  say so honestly and treat it as exploration, which fits K-2.
- Audience card hides on every change; Read describes only the settings while it is hidden, so it gives nothing away.
- Like me: "Tell Pom, or pass." keeps it safe and solo-friendly; the vote has no counts.
- Feel: the cardboard theater, the kite moving between scenes and the three ending pictures are charming, and the
  three-ending choice is the moment a child would replay for.

## Audit pilot

- Leads confirmed: "welcome not heard" after a first tap on Next (part of finding 1: the real cost is that scene 1 is
  skipped, not just the welcome).
- Leads wrong: Next two quick taps "event line cut (hush)": the second Next changes the scene, so dropping "Whoosh!"
  is correct. "Welcome not heard" after Show me, Back and Again: those taps speak their own lines, which is right.
- Missed: the first screen never starts the show on its own and its hint points at the control that skips scene 1;
  the Like me mid-air crop; Dot hidden by the curtain; sad and worried faces alike; the flip line's timing. Also a
  harness note: drive.py's plain `wait` showed the voice queue stalled after the first line (out2.txt stage-tap-2),
  but with the page polled every second the same tap ran normally (out3.txt diag-stage), so it was not reported.
- Nothing cultural, Native or hard-history: no sensitivity review needed.

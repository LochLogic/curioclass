# Play lens: data-defenders (round 1)

Played twice: as a grade 5 student alone at home (real clicks, held presses, voice log read after each run) and as a
teacher projecting at 1366x768 and 1920x1080. Bundle `CURIO_DRAFT=1`, 181 KB. Driven with `scripts/drive.py` on port
9540 (own profile), 375 wide through `drive.py --host 9541` (host.html deleted after). No console errors in any of the
82 shots (the only log line was the host server's missing favicon).

Counts: blockers 0, should fix 4 (general 4, family 0), polish 7 (general 6, family 1), nits 5.

## Should fix

1. **I2 log gives away I1** (Grade Book Room, both puzzles; src.html LOG row 4, "changed Cy's scores"). Rooms and
   puzzles can be done in any order, and in the split view the log sits right beside the seal cards. Row 4's action
   names Cy, so the answer to "which card was changed" is on screen before any adding (frames `i1-1366x768`,
   `i2-wrongfix`). It also makes I2 a word search for "Cy" instead of reading times and devices. Better: a neutral
   action ("changed quiz scores") until I1 is solved, or for good. The wording is in the spec's Content, so the
   integrator decides. Tag: general (POLISH, Games and quizzes).
2. **A2 strips show the answer before any pick** (Server Closet, Backup plan). Every plan's Mon to Fri strip is shown
   from the start, so the question "which plan loses the least work?" becomes "which card has the fewest red X's"
   (plan C has four green ticks, frame `a2-1366x768`). The thinking the clues ask for (same machine breaks with it, more
   often loses less) is never needed. Better: show a plan's strip after it is picked (wrong picks show their loss, the
   right one shows only Thursday lost), or have the student predict first. The spec draws the strips, so this may go
   to the spec's open questions. Tag: general (POLISH, Games and quizzes).
3. **375 wide: the I2 fix buttons are off screen** (`drive.py --host`, frame `f2/n-i2b`). After tapping row 4 the hint
   says "Now pick the first fix." but the three fix buttons sit at y 903 to 960 in an 812 tall phone, under the
   8-row log, with nothing in view pointing down. Done when 8 asks for the active puzzle's check control without
   scrolling. Better: scroll the fixes into view (preventScroll off for this one move, or scrollIntoView on the fix
   group) or dock them above the log on phones. Tag: general.
4. **The hint can stick on the room's story and never name the control** (any room, first entry). On first entry the
   hint shows the story (also shown in the story card) and only changes to the how-to when that line is spoken, about
   6 s later (`f4/h-door`: story at 3.5 to 5.5 s, "Add up each card..." at 7.5 s). If the how line is dropped, the
   hint never changes: pressing Read during the Server Closet story dropped `a1`, and 6 s later the hint still showed
   the story, which names no control (`f4/h-readdur`). A solo student is left without "press Set servers". Better: put
   the how-to in the hint at once on entry (the story already lives in the story card) and let the voice speak story
   then how-to. Tag: general (rule 4, "say how to act").

## Polish

5. **C2 is solved by the meter word alone** (Records Room, Pick the password). Testing all four cards shows "Strong"
   on one, so the pick needs no judgment (frame `c2-1366x768`). Better: the meter shows the bar and the reason, and
   the band word appears after "Use this one", so the student weighs length and names first. Tag: family:security
   (the meter is the engine's `band`).
6. **Locked Exit as the first tap goes quiet, then the hint is overwritten.** Fresh page, tap the Exit: only a low
   tone, the hint shows "The exit opens when all three rooms are secured...", then about 4 s later the welcome is
   spoken and replaces that hint (`f4/h-exitlocked1`, welcome at 5.4 s, final hint = welcome). Better: speak the
   welcome within half a second and keep the locked hint, or give the locked door its own spoken line. Tag: general.
7. **All three rooms secured: the Exit door does not invite a tap** (frame `hall-all`). The door just shows an open
   padlock; the hint says "The exit door is waiting." without naming the action. Better: a soft brass glow on the Exit
   (an outline flash with Motion off) and "Tap the Exit door to open it." Tag: general.
8. **I1 sums read wrong after solving, and bare on small screens.** After the seal check is done, Cy's card shows
   "Added: 0" while the done bar says his scores add to 79 (frame `i2b-1366x768`). At 680x425 and 375 the "Added:"
   label is hidden, leaving a lone "0" next to a button that only says "Changed" (frames `i1-680x425`, `f2/n-i1`).
   Better: keep the last sum (or show 79 on Cy's card when done) and keep a short "Sum" label. Tag: general.
9. **A2 wrong pick explains nothing.** A wrong plan gets a dashed red outline and "Not yet. Look again, or press
   Clue." only (frame `a2-1366x768`); PLANS already holds a `why` for plan A that is never shown. Better: one line per
   wrong plan in the result area ("Plan B loses Monday to Thursday: a week-old backup."). Tag: general.
10. **Projected A2 day chips are tiny.** At 1920x1080 the "last Fri / Mon ..." chips are about 11 px with a strike
    through, hard to read from the back of a room, while half the station is empty (frame `a1-1920x1080`). Better:
    scale the plan cards and chips with the station. Tag: general.
11. **Spoken wrong reason for a wrong fix in I2 is missing.** The why ("The log is how you found the change...") shows
    in the panel but only "Not yet" is spoken, unlike C2 where the meter reason is spoken. Better: speak the why as
    the event line, like C2. Tag: general.

## Nits

12. Exit slot head truncates to "Confidenti..." at 680x425 and 375, and at 680x425 the slot boxes are mostly below
    the station's fold (frames `exit-680x425`, `f2/n-exit`).
13. A1 chart: the value labels "450" (1 server) and "300" sit on the dashed capacity line (frames `a1-1366x768`,
    `a1-680x425`).
14. Escape card: behind the dialog the empty pool still reads "All six cards are in slots. Press Open the exit."; the
    exit station header says "Puzzle 1" though there is only one (frame `escaped`).
15. 375 hallway: "Grade Book Room" wraps to two lines, so the first row's doors differ in height (284 vs 303 px).
16. I2: the fix the student picked wrongly gets no visual mark (only the result text).

## What worked

- First screen says what to do ("Tap a door to go in"), the hallway reads at once, doors are big at every size.
- Voice (held clicks, 3.5 s gaps): five wrong checks in C1 gave 4 spoken "Not yet" plus 1 dropped as stale on the next
  tap, as the spec asks; C2 meter reasons spoken each time; how lines spoken once then `silent` on tab switches; Sound
  off and on brings the welcome once; Read speaks the hint and clues; rapid taps then Back then a new door left no
  stale line.
- Keyboard: Tab through header and panel to the doors, Enter opens a room and focus lands on the first grid cell.
- Calm mode keeps the same timing (door 450 ms, auto-advance 1600 ms either way); Team timer 20 min counts, at 0 shows
  "Time!" and nothing locks.
- Main controls in view at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760 wide; in the 375 host
  every check control is in view except the I2 fixes (item 3).

## Frames looked at

Scratch: `C:\Users\Cory\AppData\Local\Temp\claude\S--\98b8b046-f7f2-48d0-a719-c61ce01237be\scratchpad\lens-dd-play`
- `f1/`: hallway at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000; each of C1, C2, I1, I2
  step 2, A1, A2, exit at 1366x768, 800x500, 760x1000, 1920x1080, 680x425; extremes c1-badges, c1-clue2, c1-done,
  c-secured, hall-1secured, i2-wrongrow, i2-wrongfix, a1-two, a1-four, a1-done, hall-all, exit-partial, exit-wrong,
  escaped, timer20, timeup, startover, exitlocked-tap, calm-hall.
- `f2/` (375 host): hallway, C1, C1 wrong x2, C2 tested, I1, I2, I2 step 2, A1 two servers, A2, exit, all secured,
  escaped.
- `f3/`, `f4/`, `f5/`: voice and hint runs (first taps, Read, Sound, tab switches, fast taps, keyboard, Sound off).

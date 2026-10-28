# Craft lens: target-toss

Cold Craft lens, round 1 (2026-10-28). Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py target-toss`, 95 KB.
Driven with `scripts/drive.py` (held clicks, 0.12 s), muted headless Chrome, own profile, ports 9940-9946.

**Counts: blockers 0, should fix 5 (general 5, family 0), polish 2 (general 2), nit 2 (general 2).**

## Findings

### Should fix

1. **Focus falls to the page when a Test it step hides the control that was pressed** (general).
   Where: `src.html:957-973` (pickQuestion, makeGuess, startRound), `1024-1029` (stopTest), `1176-1177` (Test again,
   New question). The pressed control's panel or card grid goes `hidden`, nothing else is focused, so a keyboard user
   is dropped to `<body>` and the next Tab starts again at the header.
   How seen: keyboard shots (Enter on the focused control, then `document.activeElement` after 1.8 s). Question card,
   Way A guess, Skip the guess, Start Way B, Stop test, New question and Test again all ended on `BODY` (hidden).
   The good cases already exist in the same file: Way A done focuses Start Way B, Look focuses Show the answer, Show the
   answer focuses Test again, Clear the wall focuses Too short, Escape returns to How to set up. Do the same for the
   rest: after a question card or guess, focus the stage target (it is focusable in a round) or the first control of
   the new step; after Stop test / New question, the first question card; after Test again, Way A's guess button.
   BR1 lesson missed ("focus is kept when controls rebuild").

2. **Start Way B appears exactly where Undo was** (general).
   Where: `src.html:210-215` and `938`. When the last Way A throw lands, Start Way B is unhidden above the Too short /
   Undo / Stop row and pushes it down 68 px.
   How seen: control positions at 1366x768. During Way A, Undo is centered at (1188, 489); after the 10th throw, Start
   Way B is centered at (1188, 489) and Undo moves to (1188, 557). A teacher who reaches for Undo after a stray last tap
   presses Start Way B instead, and from Way B there is no way back into Way A. At 375 wide (iframe host) the same
   jump pushes Too short, Undo and Stop test below the fold (bottom 823 in an 812 px frame).
   Better: keep the row where it is and put Start Way B in a reserved slot (for example in place of Too short, which is
   disabled then, or below the row). BR1 lesson missed ("nothing rebuilds under the pointer").

3. **The first Throw with Bo (and the first How to set up) waits about 7 s behind the safety line** (general).
   Where: `src.html:376`, `888` (`await V.say(withSafety(['ready']), {wait: true})`), `1111`.
   How seen: voice log, fresh page, first tap on Throw with Bo: the safety line starts at 1.3 s, "Ready, aim..." at
   8.1 s; Bo stands still the whole time and the class waiting to shadow him hears a long rule first. How to set up as
   the first tap: safety at 1.3 s, the setup description not before about 6 s. BR1 lesson missed ("the first action
   never waits behind a line"). Better: start the action at once and let the safety line come after (or ride on the
   end of the run, as Show me already does with "Now you try!").

4. **The answer card is clipped at 680x425 and at 375 wide** (general).
   Where: `src.html:142` (`#answer`), `781` (answerH), `837` (`max-height`).
   How seen: Look step with Show the answer pressed (20 throws, tie, guess made). The card's content is 81 px tall in a
   73 px box at 680x425 (68 px at 375); the second line of the voiced tip ("get even better.") is cut at the bottom
   edge (frames `680x425_look20.png`, `375_look20.png`). Fine at 800x500 and up. Clipped text at a STANDARDS size.

5. **"Now you try!" does not name the control** (general).
   Where: `src.html:910` (nextCue, fifth cue). The spoken line is "Now you try!"; the hint says "Now you try! Press
   Throw with Bo to throw together." STANDARDS (Say how to act): the line and the hint name the next action and the
   control. How seen: voice log of six Next cue taps. The tool already has the full line (`tryBo`, spoken after Show
   me); speak that one here too (and `nowYou` can leave `allLines()` and lines.json if nothing else uses it).

### Polish

6. **Coach says keeps a tip from a throw that was undone** (general). `src.html:1057` (freeUndo). Five throws above
   the target give "Too high..."; Undo takes the fifth away, the card still says "Too high..." about four throws.
   Better: on Undo past a multiple of five, put the card back to the tip for the last full five (or the starting
   "Throw five balls. Then look here."), the way `setThrow` already recomputes it.
7. **How to set up is not modal** (general). `src.html:246-247`, `1108-1118`. With the card open, the panel buttons
   still work: Show me runs Bo and speaks the cues under the card. Better: close the card on any panel or mode action
   (mode switch already does), or mark it `aria-modal` and keep Tab inside it.

### Nit

8. **Cue lines and "Ready, aim..." are events in the code, how lines in the spec's Voice table** (general).
   `src.html:865, 888, 894, 911, 917`. The code is right for the class (Show me and Throw with Bo must say every cue on
   every run, and a tapped cue card should always speak), and it passes the repeat check that way; but Done when 6
   ("each how-to line once per load") reads wrong against the spec table. Update the spec's table (kind event) so the
   exit check doesn't trip on it.
9. **Short-box toggle labels clip a pixel or two** (general). At 680x425, 800x500 and 1000x625 the Under / Over /
   Right / Left labels are 16 px tall in a 14 px line box (`src.html:83`, line-height 1.05). Not visible in the
   frames; line-height 1.15 would clear it.

## Checks that passed

- **Contract:** one file, 95 KB, no network requests (the only URL in the bundle is the SVG namespace), kit used
  (`Curio.voice`, `Curio.tone`, the kit's `Curio.audio()` context for the whoosh, `Curio.reduce`/`onMotion`), no
  console errors or exceptions in any run (about 110 shots). Nothing takes focus on load (`BODY`).
- **Hit tapping, pointer:** a full Test it run with real held clicks at 1366x768 (Step or stay?, guess Way A,
  10 taps in Way A including one Too short, Start Way B, 12 taps in Way B including one Too short and one Undo,
  Show the answer). I computed each tap's ring from the target box (center 503,461, R 238) before the run: Way A
  `G R B x x S R x G x` (5 hits), Way B `G R B x R S G R B x` (7 hits). The tool recorded exactly those, the panel
  ten-frame, the Look ten-frames (filled left to right, top row first, stars on the gold hits), the big numerals
  (5 hits / 7 hits), the bars (5/10, 7/10) and the SVG description all agree; "Way B got more hits!" and "That's
  different from our guess" are right (guess was A). Undo in Way B removed only the Way B throw.
- **Small target:** real clicks in Way B of Big or small?: gold = hit with a star, red and blue = misses, rings grey
  with "Only the gold counts"; panel says "Throw 3 of 10, Hits: 1" after the gold, red, blue taps.
- **Keyboard:** Tab reaches the target in a round and in Free throw; the arrow keys move a visible crosshair, Enter
  and Space throw at it (Free throw: 9 x ArrowUp gave a miss at ny -1.08, then hits at ny 0.36); Shift-Tab into the
  stage and Enter finished Way B and focus went to Show the answer. Visible focus ring on the stage and buttons.
  Keys 1 to 3 switch modes; Escape closes the setup card and returns focus.
- **Touch:** the stage listens to `click` with `touch-action: manipulation`, so a finger tap lands where it touches
  (same handler as the mouse path above).
- **Free throw coach (Done when 5):** 25 real taps 2 s apart: 5 above, 5 hits, 5 Too short, 5 to the side, then a
  mix gave "Too high. Let go lower...", "Great aiming!...", "Too short...", "Face the target, and point your hand...",
  "Keep going..." in that order, each spoken.
- **Lines:** `allLines()` returns 74 lines and `voice/lines.json` holds the same 74, word for word and in the same
  order. Every `V.say` uses a key or a value of the line table, so no spoken text is outside it. No em dashes in
  src.html, notes.md, tool.draft.json, prompts.json or lines.json; "Curio Class" never "Curio" alone.
- **Motion off:** the audit found nothing running forever; the Look bars are full on the first frame (frame
  `calmlook.png`), Bo jumps between poses, and the ball lands after the same 760 ms.
- **Saving and reset:** the tool stores nothing (only the kit's Motion choice), and the notes say so. Clear the wall
  empties the dots and the coach card and moves focus to Too short; Stop test and New question return to Ask with
  nothing kept; a mode switch resets Test it and keeps the Free throw dots, as the spec says.
- **Contrast** (recomputed): accent on paper 6.79, white on accent 7.38, ink on paper 14.45, muted on paper 6.43,
  red ring on white 4.85, blue ring on white 5.72, star on gold 8.14, gold button text 9.53, accent text on the wall
  6.05. Rings also differ by edge (dashed, solid, double).
- **Layout:** every state below at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000 and 375x812
  (my own iframe host page, served from my scratch folder): Form, Form left hand overhand, Ask, Guess (Close or far?
  with its tape-line note), Way A done, Way B with 20 throws and four Too shorts, Look with 20 throws and the answer,
  Free throw with 44 throws, the setup card. No sideways scroll, no overlapping controls, no hint clipped or below the
  fold, every control 60 px at 1280x720 and up (Done when 7), 48 px in the short boxes (the spec's Layout rule),
  stage and panel side by side at 1000x625. Only findings 2 and 4 above.

## Standard voice check

Sound on, Motion on, held clicks, fresh page per run, `__tool.vlog` read after each.

| Line | Kind | Run | Expected | Spoken |
|---|---|---|---|---|
| Safety ("Soft balls only...") | how (welcome) | any first tap, then every run | 1 per load | 1 |
| wForm / wTest / wFree | how (welcome) | modes cycled twice, 4.5 s apart | 1 each | 1 each (wTest dropped by a fast switch the first time, spoken at the next entry) |
| Face the target. ... (cue card 3 tapped) | event (see nit 8) | cue card x5, 2.5 s apart | 5 | 5 |
| Next cue lines | event | Next cue x6, 3.5 s apart | 1 each, then wrap | 1 each, cue 1 again on the 6th |
| Now you try! | how | same | 1 | 1 |
| Ready, aim... | event | Throw with Bo x5, 11 s apart (alternate presses stop the run) | 1 per run started | 3 of 3 runs started |
| Great throwing! Press Throw with Bo... | event | same | 1 per finished run | 1 of 1 finished |
| Now you try! Press Throw with Bo... | how | Show me x2, 13 s apart | 1 | 1 (the first dropped by the second Show me, spoken after it) |
| Setup line | how | How to set up / Close x5 | 1 | 1, then silent (heard) |
| Question title + Way A/B lines | event | 3 rounds via Test again | 3 | 3 (2 dropped by my fast Skip the guess, as they should) |
| Make a guess! | how | same | 1 | 0, dropped each time by the fast Skip (never stale-spoken) |
| Way A! / Now Way B! (start) | how | 3 rounds | 1 each | 1 each, then silent |
| Way A: + way line (round start) | event | 3 rounds | 3 | 3 |
| Way A: No hits. Way A is done! | event | 3 rounds | 3 | 3 |
| Way A: / Way B: counts + "Which way got more hits?" | event | 3 rounds | 3 | 3 |
| It's a tie! Try more throws. | event | 3 rounds | 3 | 3 |
| Tip (step) | event | 3 rounds | 3 | 3 |
| Press Test again... | how | 3 rounds | 1 | 1, then silent |
| Coach lines | event | 25 Free throw taps, 2 s apart | 5 | 5, one per fifth throw, right rule each time |
| Single throws | none | every tap | 0 | 0 |

- **Stale lines:** Test it, a card, a guess, two Too shorts and Stop test 0.2 s apart: the round-start lines were
  dropped (`hush`) at Stop test and nothing from the round played after it. Show me, Next cue x2, Free throw, Too
  short, Form 0.2 s apart: each cue cut the one before, the Free throw welcome was dropped at the switch, Form's
  welcome played. A Way A result was dropped (`newer`) once Start Way B was pressed. No line named a hidden or
  disabled control (doneA needs Start Way B, look needs Show the answer, again needs Test again).
- **First-tap timing:** plain stage tap: the welcome (safety first) at about 0.1 s after the tap. Next cue: only its
  cue. Cue card: only its cue. Mode button: safety, then that mode's welcome. Read: the hint only. Sound: nothing;
  Sound off and on brought the skipped welcome once. A key (Tab): the welcome. Throw with Bo: safety first, then
  "Ready, aim..." 7 s later (finding 3).
- **Read:** during Show me, Read cut the cue and spoke the hint, and the run went on with the next cue; with Sound off,
  Read still spoke the hint; a mode change right after Read let the next line start at once.
- **Order:** every spoken line followed the order of its action in every log.

## Audit pilot

`python scripts/audit_tool.py target-toss <scratch>/audit --port 9940` reported **0 leads** (every size clean,
Motion off clean, 19 one-click walks clean, the five-click checks clean). I confirmed what it covered: first screens
at all eight sizes, Motion off, focus on load and the Form controls' voice all hold on my own frames; none of its rows
was wrong.

It missed everything past one click from Form: focus dropped to the page on six Test it controls (finding 1), Start
Way B landing under Undo (2), the answer card clipped at 680x425 and 375 (4), the ten-frame counts against the taps,
and the 7 s wait in front of the first Throw with Bo (3; its walk logged that the safety line was spoken but does not
judge delay). Its target rule (44 px in the preview sizes) also differs from the BUILD lesson's wording (60 px for
K-2 at every size); this tool's spec allows 48 px in short boxes, so I did not file it, but the two texts should agree.

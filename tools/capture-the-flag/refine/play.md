# capture-the-flag: Play lens (Refine round 1)

Cold read of spec.md, src.html, notes.md, handoff.md, voice/lines.json; bundled with `CURIO_DRAFT=1` (147 KB). Driven
in my own muted headless Chrome (port 9950, own profile) with real held clicks, real keys and `Input.insertText`
typing; 375 wide through an iframe host page served on port 9951 (`host.html?w=375&h=812` and `h=667`). Frames and
scripts in my scratch folder `lens-ctf-play2/out` (about 150 frames). Console clean in every run, no network requests
(the only 404 was the host page's favicon).

Counts: blockers 0, should fix 3 (general 2, family 1), polish 5, nit 4.

## What works

- **Every size:** at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x900 and 375x812 / 375x667,
  in all twelve challenges, Flag, Submit, Back to board and the hint are in view with no page scrolling and no sideways
  page scroll (measured per tile). Board tiles are never under 94x86 px (151x110 at 375, two bands of two categories
  with row labels). The board fits without scrolling at every desktop size.
- **Keyboard only:** one tile per category solved with Tab, arrows, Enter, Space and typing: P100 (Tab to the bkoh
  row, Enter copies password1 into Strength, "On the common list: yes"), C100 (Enter on the message, arrows to Base64,
  Decode gives `flag{not_a_lock}`), S100 (Space on lines 2 and 5, Check lines), L300 (Enter on T, R, A, C, E) and
  L100 (filter and sort buttons, then Flag). Tab order from load: Board, Toolbox, Motion, Sound, Read, then tiles in
  column order; arrows move by position; Enter opens with focus on Back to board; after a right flag focus lands on the
  first patch choice; Back returns focus to the tile just closed. Focus ring always visible.
- **Saving:** tile states, hint use and patch tries survive a reload (score 800 then 1000 with a flag-found S200 that
  reopens straight to its Patch card). Nothing typed is stored. **Clear progress** asks Yes/No, focus on No; No keeps
  everything, Yes resets the board and storage, and a reload stays at 0.
- **Toolbox drawer:** each challenge opens it on its own tool (C100 on Shift, on purpose), a tapped spot copies into
  the open tool, the text follows to an empty tool on a tab switch, and the drawer closes after a right flag.
- **Motion off:** no flip, no wheel transition, the sticky note sits straight, the Hint glow after three misses is a
  static ring (no running animations). Timing is unchanged.
- **End of the board:** 3,000 points, "Every hole is patched." under the score, all green tiles with shield and word,
  the hint names the next action (look back, or Clear progress). No celebration beyond that, as the 9-12 band asks.

## Voice check (held clicks, Sound on, Motion on; browser voice)

Run A at a 2 s student pace: first tap on the C200 tile, five wrong flags, the right flag, a wrong patch, the right
patch, Back; then four more tiles (C100, S200, L100, L200) flag and patch each. Run B at 0.2 s: L300 flag then Back
at once, reopen, patch, Toolbox, Board.

| line | kind | expected | spoken |
|---|---|---|---|
| notyet ("Not this one. Read the artifact again...") | how | 1 of 5 | 1 (then 1 dropped newer, 3 silent heard) |
| flag ("Flag found. Now patch the hole.") | event | 5 | 5 |
| patched ("Patched.") | event | 5 | 5 |
| w-board | welcome | 1, at the first board entry with no tile tapped | 1 (after Back from the first tile) |
| w-toolbox | welcome | 1 | 1 |
| all (twelfth patch) | event | 1, after "Patched." | 1 (patched, then all, 1.1 s apart) |

- **Stale lines (run B):** nothing played after its moment: Back, Toolbox and Board each cut the line before it, and
  no old line followed a newer action. Order always matched the actions.
- **First tap:** blank stage and the score pill and Motion get the welcome within 1.3 s of load+tap; a tile tap opens
  silently and the welcome comes on Back; the Toolbox button gets only `w-toolbox`; Read reads the hint only; Sound
  says nothing, and Sound on again brings the skipped welcome once.
- **Read:** Read during the welcome reads the hint; Read with Sound off still reads; with a paid hint shown Read
  speaks the hint and then the paid hint.

## Findings

### Should fix

1. **The tool's answer lands out of sight after you tap an artifact, at every size below 1366x768.** (general)
   Where: the challenge view's Toolbox drawer (`#tbSlot` inside `.pscroll`, and below the stage in the stack layout);
   also Toolbox mode at 680x425.
   What: tapping a spot copies the text into the drawer, but the part the student needs to see stays below the fold.
   Measured after a real tap (top of the target vs window height):
   - P200 (the printed flag `#pwFlag`): off screen at 680x425, 800x500, 1000x625, **1280x720** (top 720 of 720) and
     760x900 (1384 of 900).
   - C200 (Text out): off at 680x425 through 1280x720 (671 of 720) and at 760x900.
   - P100 (Strength readouts) and C300 (Keyword box): off at 680x425 to 1000x625 and at 760 wide.
   - At 375x812 the drawer starts at 930 px; the page does not move, so the tap looks like it did nothing (frame
     `ph-C200-copied-375x812`). Working the shift then means scrolling down to the plus button and Text out, and back
     up to Flag (`ph-C200-shifted-375x812`).
   - Toolbox mode at 680x425: Text out sits below the stage fold (`toolbox-680x425`).
   How seen: `copyvis.py` and the frames named. A solo student taps "copy", sees nothing change, and does not know the
   meter or decoder ran. At 1280x720, the main laptop size, P200's whole point (the meter prints the flag) is hidden.
   Better: after a copy, scroll the drawer's tool into view inside the panel (and on stack layouts bring the tool up,
   keeping Flag reachable), or show a short "Copied into Shift" line beside the spot. In Toolbox mode at short heights,
   a smaller wheel so Text out stays in view.

2. **Most flags can be found by trying every option, at no cost.** (family:security)
   Where: `submit()` and `s100Check()`/`l300Tap()`; a miss only shows "Not this one." and, after three, the Hint glow.
   What: the flag is one of a few things already on screen, and wrong tries cost nothing, so full points come from
   guessing. Probed with `__tool.submit` and `__tool.s100` on a cleared board:
   - P100: 6 account names (found on try 2); L100: 6 accounts; L200: 5 accounts (try 1); S300: 2 sender domains;
     S200: 10 times (try 5). Each scored full points.
   - S100: 28 line pairs through Check lines, no limit or cost (2 pairs open it).
   - L300: four cards carry times, so only R ("no time") is unknown; 5 placements find TRACE.
   - P200 and P300 by design ask you to try each candidate or row; that is the activity, so they are fine.
   How seen: the probe in `feel.py`; the score stayed at full value. A 9-12 student playing for score will learn this
   in one tile, and the score then measures guessing rather than reading the artifact.
   Better: each wrong flag on a tile lowers its flag points (say a tenth, never below half), shown on the points pill;
   or Check lines and the L300 order count misses the same way. This changes the spec's scoring, so it may belong in
   the spec's open questions rather than a silent fix.

3. **L300's payoff is hidden below the fold of the artifact.** (general)
   Where: L300, `#l300order` and `#l300spell` under the cards.
   What: at 1366x768 the spell line ("The letters spell TRACE: flag{TRACE}") is at 921 px, below the artifact card's
   bottom at 768; at every smaller size it is further down. With all five in order the cards turn green, but the
   letters show only in the order list and the spell line, both out of sight. The order list also repeats all five
   card texts, which is what pushes it down.
   How seen: `kb-L300-ordered` and the rect measure in `feel.py`. The student sees green cards, no letters, and a hint
   that says "When the letters spell the flag".
   Better: show each card's letter on the card itself once the order is right (the `tag` already shows its number),
   and put the spell line above the cards or scroll it into view when the fifth card lands; shorten the order list to
   numbers and times.

### Polish

1. **Two spoken lines leave out the control.** (general) `flag`: "Flag found. Now patch the hole." and `patched`:
   "Patched." are the only things heard at those waiting moments, but they don't name the control (STANDARDS, say how
   to act; the hints `hPatch` and `hPatched` do). Better: "Flag found. Now tap the patch that fixes the hole." and
   "Patched. Tap Back to board for another tile."
2. **Opening a challenge is silent.** (general) A solo student whose first tap is a tile hears nothing until Back,
   when "Pick any tile..." plays after they already finished one (run A, w-board at 29 s). Each challenge's first step
   (`L.find`) is hint-only, so a non-reader in a challenge gets nothing spoken. Better: one how line the first time any
   challenge opens ("Find the flag in the artifact, type it in Flag, then press Submit."), spoken once per load.
3. **Wide screens: the stage is mostly empty while the tools are squeezed into the 360 px panel.** (general)
   At 1366x768 and 1920x1080 (frames `C200-copied-1366x768`, `S300-1920x1080`) the artifact fills a third of the
   stage and the wheel, readouts and Text out stack down the narrow panel. For a teacher projecting at 1920x1080 the
   artifact text stays at 14 px. Better: on wide stages, place the open tool beside the artifact in the stage (it would
   also fix should-fix 1 at those sizes), and let artifact type grow with the stage.
4. **P300 at 375 hides the key column.** (family:security) The sign-in table scrolls sideways inside its card and the
   "second step" and "result" columns start off screen (`ph-P300-375x812`), so the "denied" that answers the brief is
   not visible without a sideways swipe nobody hints at. Better: on a narrow card, drop the place column or stack each
   row's sub-lines, or say "swipe the table" in the copy note.
5. **Phone board runs past the fold.** (general) At 375x812 the last row of tiles ends at 918 px (tiles 110 px tall,
   the spec allows 64), and the panel's hint is further below. Better: shorter tiles on phones so all twelve fit.

### Nit

1. At 760 wide the header wraps Read onto its own row (`C200-760x900`).
2. `justPatched` is written into localStorage with each tile (`save()` stores the whole tile object); it is ignored on
   load, so harmless, but the stored record is meant to be only state, hint and patch tries.
3. S300: the shorter email card has an empty gray band at its foot where the two cards are stretched to one height
   (`S300-1920x1080`).
4. The Strength bar has a 70 tick but no unit or end label; "bits" beside it would read better.

## Frames looked at

Board, Toolbox, Toolbox Strength, P300, S100, L300, S300, C200 (open and copied), P200, P100 (patch card and
patched) and the board after one patch, at all seven desktop sizes; the twelve challenges at 375x812 and 375x667
plus C200 copy, shift, flag, wrong patch and patched; keyboard frames (`kb-*`); voice run frames (`v-C200-5miss`,
`v-all-chal`, `v-all-board`); Motion off (`calm-C300-3miss`, `calm-C200`); reload and Clear progress frames; the
feel run (`f-P200-pw0..3`, `f-P300-details`, `f-P300-hint`, `f-board-hinttag`, `f-L300-wrongorder`).

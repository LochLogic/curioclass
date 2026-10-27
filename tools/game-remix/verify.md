PASS WITH FIXES

# Verify: game-remix (Remix a Program, grade 5, computer science)

Checked cold on 2026-10-26 against docs/agents/VERIFY.md, STANDARDS.md (including the "Say how to act" rule) and
BATCH-CS.md, and against every Done-when item in spec.md. Build: `CURIO_DRAFT=1 python scripts/bundle_tool.py game-remix`
(163 KB, one file, only "no recording yet" warnings). Test rig: my own CDP driver, muted headless Chrome on port 9661,
a static server on 8971, held clicks (120 ms), real key events, an iframe host page for the 375 wide sizes. The art is
still stand-ins and the voice is not recorded, so neither is flagged; the voice log shows which clip starts and when.

The builder's list of 20 spec deviations is not in notes.md or src.html (BATCH-CS-LOG only says "20 spec deviations
listed in the build report"), so I worked them out by comparing spec.md with src.html. They are judged under
"Builder's deviations" below.

## What passed

- **Remix code, round trip.** The 4 built-in codes decode, re-encode to the same string and show exactly the specced
  changes (Upside Fetch: one row, "move puppy up → down 30"; Pumpkin Rush: two rows; Skunk Trouble: both credits). A
  12-edit mixed remix of Fetch Turbo, shared and loaded back, gives the same program, credits and change rows, loaded
  locked. Branching it as a third remixer and loading again is also identical (201 characters). A 3-deep family refuses
  further edits.
- **Hostile codes.** All 4712 single-character swaps, 142 transpositions and 152 deletions of a real code give "typo".
  Empty, HTML, 10,000 characters, null, objects and a GR2 prefix give a plain refusal and never throw. Lowercase,
  spaces, I/L/O and extra hyphens are accepted. 20,000 random strings with a valid checksum are all refused as not a
  code. 6000 structured random op lists: decode success always matches build success and re-encoding is identical; 150
  of them loaded in the UI with no console errors. No eval, new Function, fetch, XHR or WebSocket; no network requests
  besides the page.
- **Done when 2.** Fetch ends "Time's up!" with time 0 at 30.2 s. Snow Bounce loses a life on each bottom hit and ends
  "Game over" with lives 0 at 11.6 s, which I recomputed by hand from the program.
- **Change list after mixed edits.** Move then delete a block; move a line out then delete the source block; add a
  sprite and a line then remove the sprite; swap then remove; delete, edit a neighbour, Put back (order restored);
  move to the top ("up 2 lines"); hat edits. Every list matched a by-hand diff. Undo is exact apart from should-fix 7.
- **Credit lines** are not chips, have no handle and cannot be selected. Delete, Backspace, Enter, Space and Alt+Arrows
  on a focused credit change nothing, and the focus tooltip explains why.
- **Step and Slow-mo.** Step runs exactly one line per press (button or S key) and the lit row stays while paused.
  Slow-mo runs 333 game ms per real second, Normal 1000. Compare uses the same seed (ball's first spot (339, 206) in
  both).
- **Keyboard only.** Holding ArrowUp 0.5 s on the focused stage moves the puppy 120. Chip edit by keyboard (Enter,
  ArrowDown, Enter) keeps focus on the chip; Escape closes with no change. Handle then Delete moves focus to the next
  handle; Alt+Down moves a line across blocks and keeps focus; Ctrl+Z undoes. The Start over confirm traps Tab. Focus
  never fell to body. Tab order matches the spec.
- **Drag a start spot** with jitter gives "bee starts at (220, 160)". The "was 1" tooltip, Put back, Show changes off
  and row click to focus all work.
- **Save, Clear, Load.** Nothing is stored before Save. Open restores the exact code, title, rows and unlocked state.
  Clear saved asks first and empties storage. Corrupt or hostile storage is ignored. The 6-save limit works.
- **Print card** is one 5.5 x 8.5 page for a 3-level, 4-credit family and for a 12-change remix ("and 4 more"), with
  title, by, credits, snapshot, changes and code.
- **Sizes.** No horizontal or page scroll at any STANDARDS size, 375x667 or 375x812. Play, Step and the arrow pad are
  visible at every size. Code font is 15px at 1366x768 and 17px at 1920x1080.
- **Voice.** voice/lines.json equals the lines in the code (35). Held-click walks of every flow never started the same
  clip twice. The first tap on a bug card skips the welcome correctly. Console clean in every run.
- **Pumpkin Rush fix** through the UI meets the challenge, queues "fixed", and the score now goes up (2 after 2 clicks).

## Must fix

1. **Typed Title and Remixer are not counted in the code-length guard, so a remix can vanish or become unloadable.**
   Repro: remix Fetch Turbo, make 40 changes, type a 20-capital title and a 12-capital name. Share shows a 278-character
   code and Save says "Saved on this device.", but readSaved drops anything over 240, so the remix never appears in My
   saved remixes. Loading that same code says "That code isn't a Game Remix code." Second repro: load a 2-level code
   whose names are long capitals (217 characters); the first edit is refused with "too long... Undo a change first",
   and there is nothing to undo, so the code can never be remixed.
   Fix: measure the real encoded length on every name input and edit (names included); cap or refuse the name with a
   plain message naming the field, never refuse Save after saying "Saved", and give the edit refusal a way out
   ("Make the title shorter") when the overflow comes from inherited names.

2. **The voice queue plays stale lines and delays praise by about 26 seconds.** Repro: pick Upside Fetch, Remix this,
   fix the down line. The queue is fixRemix (stale), first, credit, how:changed, fixed, how:fixed. "Tap a row in the
   earlier changes..." plays after the bug is already fixed, and "You fixed it!" starts at 39.6 s for a fix made at
   about 13 s. Also, compare and how:compare stay queued after switching back to My remix. STANDARDS says to drop a
   queued line whose moment has passed.
   Fix: a how line drops itself if state.howto no longer equals its key when its turn comes; a newer how line drops
   older queued how lines; when the first change is the fix, say "fixed" first and skip first/credit (or fold them in
   later).

## Should fix

3. **Loading a 3-deep code says to remix it, but it can't be remixed.** Repro: load a code at the family limit. The hint
   and voice say "Press Play to try their game, then change any word to start your own remix"; any edit is then refused
   as "family is full". Fix: use HINT.full (and its voice line) when the loaded code is locked and already 3 deep.

4. **Compact tier hides the controls the hints name.** At 680x425, 800x500, 1000x625 and 760x600: in Arcade, What
   changed is not reachable (section display none, toggle hidden) while the bug line says "Check What changed". In
   Remix, the earlier changes list sits in the icon-only ≠ drawer while the hint says "tap a row in the earlier
   changes". Icon-only panel buttons are named by words the child can't see ("Copy code", "Load a code", "What
   changed"). Fix: show the What changed toggle in compact Arcade, and either keep short text labels on the drawer
   buttons or have hints name the icon ("the ≠ button").

5. **Wide 1366x768 and 1280x720: picking a card low in the shelf scrolls the hint and Remix this off-screen.** Repro:
   click Upside Fetch or Pumpkin Rush in the shelf; the panel scrolls so Remix this sits at top -83 and -180. Fix:
   scroll the shelf on its own and keep the hint and Remix this sticky below it.

6. **While a game plays, nothing names its controls.** The hint stays "Pick a game and press Play" and no line says
   "Press the arrow keys or the arrow pad", "Click the pumpkin" or "Press 1 to 5". This is a waiting moment under "Say
   how to act". Fix: on Play, set a how hint built from the program's hats (key, click, number) and voice it once.

7. **Undo reverts two steps after editing the same chip twice.** Repro: change a speed 1 to 3, then 3 to 5, press Undo:
   it goes back to 1. Done-when 3 says Undo reverses each step. Cause: collapse runs on the op log itself. Fix: collapse
   only when encoding, or keep a separate undo stack.

8. **Remix this skips the "your changes will be gone" confirm after later edits.** w.saved is set on Save and never
   cleared by later edits, so remixOf thinks the work is saved and the new edits are lost silently. Fix: clear the flag
   on every edit (or compare the current code with the saved code).

9. **375x667: the arrow pad wraps and pushes the hint and Remix this below the fold.** 4 x 60 px plus Space plus gaps is
   344 px in a 343 px row, so Space drops to a second row; the hint ends up at y 637 to 685 and Remix this at 695 to 751
   on a 667 high screen. Fix: gap 4px or less Space padding at narrow widths.

10. **The Upside Fetch challenge accepts a false fix.** Repro: add "move puppy up 30" to the up-arrow block and keep
    "move puppy down 30". The puppy nets zero and the game is still broken, but the challenge is met. Fix: require no
    "move puppy down" in the up-arrow block, or a net upward move.

## Nice to have

11. findRef focuses the ≡ handle before the chip; after Remix this focus lands on Show changes; after deleting an event
    focus goes to Undo. Land on the changed chip, the first chip, and the next block.
12. Moving a line down then up leaves two no-op ops: Undo and Start over are enabled while the list says "No changes
    yet", and the no-ops ride in the code. Drop ops that cancel out.
13. The print card wraps the code mid-group (word-break: break-all). Break at hyphens.
14. Credit wording "Remix of Remix of Fetch Turbo by Clever Fox" and the level-3 default title "My Remix" read oddly.
    Prefer "Remix of Fetch Turbo (by Clever Fox, remixed by ...)" and "Fox's Fetch Turbo Remix".
15. The borrowed credit stays after the borrowed sprite is removed. Fine as honest history; say so in notes.md.
16. Challenge 2 ("change the animal") accepts ball or pumpkin costumes. Check the animal set.
17. Step on a program with no timers silently runs up to 60 s of game time to find the next line. Say "Nothing runs
    until you press a key" instead.
18. Confirm dialogs and the copy fallback have no narration or how line. Give them one ("Press Yes to start over, or
    No to keep your work").
19. Compact Arcade cards hide their notes, so the bug cards lose their "This one has a bug" cue. Keep a short tag.
20. art/prompts.json says "No people, no animals, no writing"; STANDARDS asks prompts to describe what is there, not
    what isn't.
21. The compare line says "Switch to Original" when the child has already switched (spec wording). Use a second line
    for the Original view.
22. Pumpkin Rush's fix hint says "that line" while two rows are listed. Name the click block.

## Builder's deviations

Inferred from spec vs src (the list itself was not in the files given). Acceptable unless marked.

1. Run bar above the stage in wide (spec: under it). Acceptable; Play stays next to the stage.
2. Compact layout with the run bar on top and What changed, Sprites, Challenges, Saved and Load as drawers.
   Acceptable as a layout, but breaks intent where hints name hidden controls (should-fix 4).
3. Challenges as a drawer in wide. Acceptable.
4. Added "Earlier changes" section for loaded families. Acceptable, it shows the bug's history well.
5. Added a "Start spot" keyboard button for sprites. Acceptable, it gives keyboard parity with dragging.
6. One costume of each kind (swap and add refuse duplicates). Acceptable.
7. Space activates the focused button rather than pausing. Acceptable (button convention wins).
8. 20 extra HOW lines and HINT lines beyond the spec's 15. Acceptable, required by "Say how to act"; the spec's 15 are
   present word for word.
9. Default titles "X Remix" and "My Remix". Acceptable, wording nit in item 14.
10. A loaded code stays locked and branches a new level on first edit. Acceptable, matches the credit intent.
11. Credit wording for earlier levels ("X is a remix of Y by Z"). Acceptable.
12. Save list stores a "mine" flag and shows a 6-limit message. Acceptable.
13. Copy fallback (select-the-code box) when the clipboard is blocked. Acceptable.
14. Decode accepts I, L and O as 1, 1 and 0. Acceptable, kinder to children copying by hand.
15. Arcade card notes hidden in compact. Acceptable as a layout, nit in item 19.
16. Undo collapses repeat edits of one chip. Breaks the spec's intent (Done-when 3, should-fix 7).
17. Stage gets an aria label and number keys 1 to 5. Acceptable.
18. Load input capped at 600 characters. Acceptable.
19. Remove disabled for the first sprite. Acceptable, keeps a game playable.
20. Share card shows the first 8 rows then "and N more". Matches the spec.

## Sizes checked

1920x1080, 1366x768, 1280x720, 1000x625, 800x500, 680x425, 760x600, 375x667 and 375x812 (the last two through an
iframe host). No page or horizontal scroll and no clipped text at any size. Issues only where listed: 1366x768 and
1280x720 (should-fix 5), the compact sizes (should-fix 4), 375x667 (should-fix 9).

## Fixes

Fix round 1 (2026-10-26). Rechecked at every size above with 0 console errors.

1. **Fixed.** edit() measures the real encoded code, names included. Untouched default names are shortened first ("Your
   title and name were made shorter so the remix code fits."); otherwise the change is refused with a way out ("Undo a
   change, or make the title shorter"). Typing a title or name is cut at the 240 limit with "That title (remixer name)
   is as long as the remix code can hold." Save refuses an over-long code before saying anything. A loaded family whose
   names leave no room for one more remixer is read only (full). Checked: 40 changes plus capital names give a code of
   exactly 240 that saves and reloads.
2. **Fixed.** A MOMENT map gates every queued line; a how line plays only while the hint still shows it, and a newer how
   line drops older queued ones. When a change is the fix, "fixed" plays first and first, credit and the changed how
   line are skipped. Checked: "You fixed it!" plays about 1 s after the fix in a real-click run, and compare lines are
   dropped once their moment has passed.
3. **Fixed.** A loaded code at the family limit uses the full hint and the new loadedFull how line.
4. **Fixed.** Compact keeps short text labels on the buttons the hints name (Undo, What changed, Sprites, Copy code,
   Print card, Save, My saved, Load a code). Compact Arcade gets a What changed button for remix cards. The earlier
   changes list is in What changed. The panel scrolls in compact so the pad never covers the program.
5. **Fixed.** In wide, the hint and Remix this sit in a sticky header at the top of the panel. Checked at 1366x768,
   1280x720 and 1280x600 with Upside Fetch and Pumpkin Rush.
6. **Fixed.** Play sets a how line from the program's events (playKeys, playClick, playBoth, playWatch), voiced once.
   Stop and the end banner restore the hint from before Play.
7. **Fixed.** Undo uses a snapshot per change, so 1, 3, 5 undoes to 3 then 1. Start over can be undone; typed names
   are kept.
8. **Fixed.** Every edit clears the saved flag, so Remix this asks before replacing unsaved changes.
9. **Fixed.** Under 440 px the pad gap is 4 px and Space is narrower: one row at 375. In stack Arcade the stage
   shrinks so Remix this stays above the fold at 375x667.
10. **Fixed.** Challenge 7 needs a move up and no move down in the up-arrow block. The false fix is not met.
11. **Done.** findRef lands on the changed chip; Remix this and Try it focus the first chip; deleting an event focuses
    the next block's first chip.
12. **Done.** Edits are trimmed to the shortest op list giving the same program, so a move down then up leaves no ops
    and turns Undo and Start over off with "No changes yet".
13. **Done.** The share and print code breaks only after hyphens.
14. **Done.** Credit lines quote a title that starts "Remix of". A remix of a Remix title defaults to "[Animal]'s
    [title]" from the nickname, never "Remix of Remix of".
15. **Done.** notes.md says the borrowed credit stays as honest history.
16. **Done.** Challenge 2 accepts only the animal costumes.
17. **Done.** Step looks at most 10 s ahead, then says "Nothing ran for 10 seconds. Press Resume, then press a key or
    click a sprite to make something happen."
18. **Done.** Every confirm box shows and voices a how line naming both buttons. The copy fallback box says how to copy.
19. **Done.** Compact bug cards keep a "Has a bug" tag.
20. **Skipped** at the coordinator's request; art/prompts.json is unchanged and the art is final.
21. **Done.** A separate original-view line plays in Original. The compare line plays after the first run of a changed
    remix, with the how line "tryOrig".
22. **Done.** The bug how lines are split by game; Pumpkin Rush names Jay's score change in "when pumpkin is clicked".

Voice: voice/lines.json is regenerated from allLines() (49 lines, was 35). 17 new, 3 removed (old fixArc, fixRemix and
saved); the new lines need recording.

Art: the 13 final assets render at every size. Sprites draw aspect-fit to 50 units with a soft shadow; cutouts are
clean (a faint light fringe on the penguin is acceptable). The 4:3 stage, the one-page print card and preview.svg are
fine. Bundle without voice: about 805 KB.

"But don't nag" check (2026-10-26): every line, how-to or not, is spoken at most once per page load. narrate() marks a
line said only when it actually plays (a line dropped because its moment passed stays unmarked), and `said` is never
cleared. After that, howTo() only updates the hint silently, and Read still says it. No line needed changing.

## Re-verify

FAIL. Both must-fix items and should-fix 3 to 10 hold up, but four new problems need a fix first (N1 to N4 below), and should-fix 3 is only half done (the voice still contradicts the hint).

Checked cold on 2026-10-26. Build: `CURIO_DRAFT=1 python scripts/bundle_tool.py game-remix` (802 KB; the only warnings are "no recording yet"). Rig: a copy of scripts/drive.py on port 9623, run as muted headless Chrome with its own profile, held clicks (120 ms) at selectors computed at click time, and the page's own `vlog` for which line starts and when. The 375 wide and 375 tall sizes ran in an iframe host on a scratch server. Voice is not recorded, so lines fall back to speech synthesis and take up to the queue's time cap. Delays below are only relative. Console was clean in every run.

### Earlier findings

1. **Must fix 1 (code length): fixed.** Fetch Turbo plus addLine changes: the guard shortens the default names once ("My Remix"), then refuses with "Undo a change, or make the title shorter" (33 changes of this kind fit; 40 do not, which is a capacity fact, not a bug). Typing a 20-capital title and a 12-capital name cuts them to "ABCDEF" and "ABCDEFG", shows "That title (remixer name) is as long as the remix code can hold", and leaves exactly 240 characters, with the box matching the code. One more edit is refused and the code stays the same. Save then gives 240 in readSaved, and the share box shows all 240. Open and Load both restore the same code. A 240-character load is read only (full): the hint is the full hint and the edit is refused with the full message. Second repro: a 212-character 2-level code with capital names now branches, with the names shortened to "Remix" and the animal (238 characters), and saves. A 232-character one is full and read only. Nothing says "Saved" without saving.
2. **Must fix 2 (stale lines, late praise): fixed.** Held clicks: the fix 1.5 s after Remix this gives "You fixed it!" once the welcome in progress ends. fixRemixUp, first, credit and how:changed are dropped. A wrong word first, then the fix: first, credit and changed are dropped, and the praise comes next. A slow fix (13 s) waits only for the how line already playing. Compare: going to Original and straight back drops how:compare. No line ever started twice in any run.
3. **Should fix 3: half fixed.** A 3-deep code loaded through Load: the hint and how line are loadedFull (correct). But the voice first says the Remix welcome "This is your copy now. Click any word in a box to change it, or add a line", then L.loaded "...keep their credit when you remix it". Two of the three lines tell the child to change something that can't be changed. See N3.
4. **Should fix 4: fixed.** At 1000x625, 800x500, 680x425 and 760x600, Remix shows text labels on Undo, What changed and Sprites. Share shows Copy code, Print card, Save (short label), My saved and Load a code. Compact Arcade has a What changed button on remix cards. Bug cards keep "Has a bug".
5. **Should fix 5: fixed.** A real click on Upside Fetch and on Pumpkin Rush at 1366x768, 1280x720 and 1280x600: the hint and Remix this stay in view (Remix this at 207 to 263 at 1366x768).
6. **Should fix 6: fixed.** Play sets playKeys / playClick / playBoth / playWatch. The hint shows it while playing and goes back on Stop. It is voiced once (but see N2).
7. **Should fix 7: fixed.** Speed 3 to 5 to 7, then Undo, Undo gives 5, then 3, and Undo turns off.
8. **Should fix 8: fixed.** Save, edit, then Remix this in Arcade: the "Start a new remix?" confirm appears.
9. **Should fix 9: fixed** at first load. At 375x667 the pad is one row, the hint is at 545 to 593 and Remix this at 603 to 659. But see N4 for what happens after Remix this.
10. **Should fix 10: fixed.** "move puppy up 30" added with "move puppy down 30" kept: challenge 7 is not met.
11. Nice to have, checked: delete event, Keep it / Delete, focus goes to the next block's chip (11). Move down then up leaves 0 changes, "No changes yet" and Start over off (12). Undo stays on, though: the notes say it turns off; it steps back to the moved state, which is fine, but the note is wrong. The share code has `<wbr>` after each hyphen (13). Challenge 2 accepts cat and crow, refuses ball, pumpkin, carrot and snowball (16). voice/lines.json equals allLines(), 49 lines, no em dashes, none over 200 characters.

### "But don't nag" count

Five Play/Stop presses in a row: playKeys spoken once. Five edits in a row: first and credit once each, how:changed never twice. Five Undos: undo once. Three event deletes: askDel once. No line was spoken twice in any run. The rule itself holds.

### New findings

- **N1 (should fix, Done-when 5): a second fix is not praised.** Fix Upside Fetch, then Arcade, Pumpkin Rush, Remix this, Start new, fix the score. Challenge 8 is met, but "You fixed it!" stays silent because L lines are once per page load. The only voice is "Press Play to test your fix." Done-when 5 says fixing meets the challenge and plays line 9. It is a result with new information (a different bug), so it should play again. Same for any later fix in the session.
- **N2 (should fix): the first tap on Play is followed by the Arcade welcome.** On a fresh load, press Play. vlog: "Press the key buttons..." at 0.1 s, then "Welcome to the arcade... Pick one, press Play" at 5.6 s while the game runs (seen twice, E and L runs). The first-tap check looks at `queued` after the click, but the how line has already started and left the queue, so the welcome is not skipped. STANDARDS: if the tap queued its own line, skip the welcome. The bug-card tap only works because it queues two lines.
- **N3 (should fix, Say how to act): spoken lines that name controls the child can't use.** (a) Share before any remix: the voice says "Ready to share? Copy your remix code, or print a card" while the hint says "Nothing to share yet..." and Copy and Print are off. The share welcome is then used up for when there is something to share. (b) A full family loaded by code: the welcome and L.loaded say to change or remix it (item 3 above).
- **N4 (should fix, STANDARDS main controls): at 375 wide, Remix this scrolls Play, the pad and the hint off screen.** Focus now goes to the first chip (nice to have 11), and the page scrolls to it: scrollTop 1005 at 375x667 and 932 at 375x812. Play is at -618 and the hint at -378, and a real click on Play at its old place does nothing. Seen in the 375x667_1remix frame. The child lands on the program with no Play and no hint in view.
- **N5 (should fix): passing a challenge gives no feedback.** Try it on "Make the ball worth 3 points", then change 1 to 3. Challenge 1 is met, but nothing is said or shown outside the closed Challenges drawer (1366x768 frame I_challenge). After Try it, the challenge's goal is shown nowhere either; the hint is the general Remix hint.
- **N6 (nit, don't nag goes too far): retries that fail are silent.** A second bad code (after "Hmm, that code doesn't work" has played once) is silent, and so is a second good load. Only the small load message changes. A child who can't read doesn't learn that the retry failed. The badCode result is worth saying again; the how line can stay silent.
- **N7 (nit, outside the STANDARDS sizes): landscape phones lose the arrow pad.** At 812x375 and 667x375 (compact), the four arrow buttons sit under the stage canvas (elementFromPoint gives `cv`), so only Space can be tapped. Fetch and Upside Fetch can't be played by touch. 680x425 is fine.
- **N8 (nit): the Paused hint is never voiced,** and a Step that finds nothing in 10 s only shows a message. These are waiting moments with a how-to that is written but never spoken.

### Sizes rechecked

1920x1080, 1366x768, 1280x720, 1280x600, 1000x625, 800x500, 680x425, 760x600, 375x667, 375x812 (iframe), plus 812x375 and 667x375. No horizontal scroll anywhere. At wide and compact sizes there is no page scroll, and Play, Step, the pad, the hint and Remix this are all in view (except N7). At 375 the page scrolls as a stack, which is expected. The problem there is only the jump in N4.

## Fixes round 2

Rechecked with held clicks at 1366x768, the compact sizes, 375x667 and 375x812 (iframe), 812x375 and 667x375; 0
console errors.

- Voice now has two kinds of line. Teaching and how-to lines are spoken once. Event lines (fixed, chal, badCode,
  loaded, loadedFull, saved, stepIdle) are spoken every time their event happens, still dropped when stale.
- N1: fixing Pumpkin Rush after Upside Fetch says "You fixed it!" again (checked). Praise plays whenever a bug game goes
  from broken to fixed.
- N5: meeting any other challenge says "Challenge done! It has a check mark in Challenges now." and shows "Challenge
  done: [challenge]". After Try it, a banner under the hint shows "Challenge: ..." and turns to "✓ Challenge done: ...".
- Should fix 3 / N3: a loaded code no longer uses the Remix welcome; a full family says "Code loaded. This remix family
  is full, so you can play it but not change it." Share with nothing to share says the shareEmpty how line, and the
  Share welcome waits until there is a remix.
- N2: the first-tap welcome is skipped when that tap's own line has already started (vlog checked, not only the queue).
  First tap on Play: only the play how line.
- N4: Remix this focuses the first chip without scrolling; scrollTop stays 0 at 375x667 and 375x812, and Play, the pad
  and the hint stay on the first screen (the stage shrinks in stack Remix too).
- N6: a second failed load is spoken again (checked 7 s apart).
- N8: the paused hint is voiced once; a Step that finds nothing in 10 s says so (event).
- N7: compact under 440 px tall keeps the pad in one row of 44 px buttons; at 812x375 and 667x375 all five pad buttons
  are tappable (elementFromPoint checked).
- spec.md's Undo note corrected: Start over turns off after changes cancel out, Undo stays on.

Voice lines: 52 (was 49). New: loadedFull event line, chal, stepIdle. The HOW keys paused and shareEmpty reuse the
existing hint text, so they add no new line.

## Re-verify 2

PASS with notes. Should-fix 3, N1 to N8 and the Undo note are all fixed. Nothing regressed. Two nits remain, listed at the end.

Checked cold on 2026-10-26 after rebuilding with `CURIO_DRAFT=1 python scripts/bundle_tool.py game-remix` (805 KB; the only warnings are "no recording yet"). Same rig as in Re-verify: muted headless Chrome on port 9623 with its own profile, held clicks (120 ms), and the page's `vlog`. The 375 wide and 375 tall sizes ran in an iframe host. Console was clean in every run. voice/lines.json equals allLines(): 52 lines, no em dashes, none over 200 characters.

### Items

- **Should fix 3 / N3: fixed.** Loading a full 3-deep code says only "Code loaded. This remix family is full, so you can play it but not change it.", then the loadedFull how line. The Remix welcome no longer plays. Share before any remix says "Nothing to share yet. Pick a game in the Arcade and press Remix this." The Share welcome ("Ready to share?") plays later, when there is a remix.
- **N1: fixed.** Upside Fetch fixed, then Pumpkin Rush: "You fixed it!" plays both times (9.1 s and 26.1 s). It also plays again after a fix is undone and redone, which is right because that is a real event.
- **N2: fixed.** With Play as the first tap, only "Press the key buttons..." plays. No Arcade welcome follows (two runs). A bug card as the first tap still skips the welcome.
- **N4: fixed.** Remix this at 375x667 and 375x812: scrollTop stays 0 and focus is on the first chip. At 375x667, Play is at 348, the pad at 518 and the hint at 588 to 659. A real click on Play starts the game, and the hint changes to the play line.
- **N5: fixed.** Try it on "Make the ball worth 3 points", then change 1 to 3. "Challenge done! It has a check mark in Challenges now." plays, the message shows, and the banner under the hint turns from "Challenge: ..." to "✓ Challenge done: ...".
- **N6: fixed.** A second bad code is spoken again ("Hmm, that code doesn't work" at 9.9 s and 18.1 s), and a second good load says "Code loaded" again. A bad code that was still waiting behind a long welcome was dropped once a good code loaded, which is the right stale drop.
- **N7: fixed** with a nit. At 812x375 and 667x375 the pad is one row, and elementFromPoint finds all five buttons themselves. 680x425 is unchanged and fine.
- **N8: fixed.** Pause says the paused hint once. On Pumpkin Pop with its three "every" events deleted, each Step that finds nothing says "Nothing ran for 10 seconds..." (three times, as an event).
- **Undo note: fixed.** spec.md and notes.md now say Undo stays on and Start over turns off when the changes cancel out, which matches what I saw.

### Regression

- **240 limit:** same results as before. Typed names are cut with the field message and the box matches the code (237 to 240 depending on the random name). One more edit at the limit is refused. Save, readSaved, Open and Load round-trip the code. A loaded code with no room is full. The 212-character inherited-names code branches with shortened names (238). Nothing says "Saved" falsely.
- **Stale and ordered lines:** a quick fix, a slow fix and a wrong-word-first fix all drop fixRemixUp, first, credit and changed, and the praise comes next. Original and back drops how:compare. The confirm how line is said once.
- **Don't nag:** over five Play/Stop presses, five edits, five Undos and three deletes, each how-to and teaching line was spoken at most once. Event lines repeat only on new events.
- **Sizes:** 1366x768, 680x425, 812x375, 667x375, 375x667 and 375x812 (default, after Remix this, playing, a bug card picked). No horizontal scroll. Play, Step, the pad and the hint are in view at every one; at 375 wide the page itself scrolls (stack), which is expected. At 1366x768, picking Upside Fetch keeps the hint and Remix this in view.

### Notes (nits)

- At 812x375 and 667x375 the four arrow buttons are 42 px wide and 44 px tall, just under the 44 px target. The notes say 44 px.
- If a Step-idle line starts and the child presses Resume during it, the line finishes ("Press Resume...") after they already have. It is harmless and short.

## Integrator fix (2026-10-27)
Both Re-verify 2 nits are fixed in src.html:
- **Arrow button width:** in compact layouts the pad buttons now have `min-width:44px; flex-shrink:0`. Measured at 812x375, 667x375 and 680x425: every arrow button is 44x44 and can be tapped (checked with elementFromPoint), and the page has no horizontal scroll.
- **"Nothing ran for 10 seconds":** the narration queue now records which line is playing. If that line is stepIdle when the child presses Resume, Resume stops it, because its "press Resume" is already done.

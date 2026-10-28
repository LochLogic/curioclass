# capture-the-flag: Craft lens (Refine round 1)

Cold read of spec.md, src.html, notes.md, handoff.md, art/prompts.json, voice/lines.json, kit/security.js (and its
diff against git HEAD) and docs/families/security.md. Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py
capture-the-flag` (147 KB). Driven with `scripts/drive.py` in muted headless Chrome. I used my own profile, port 9960
and `--host 9961` for 375 wide. About 170 frames and checks; the frames are in the lens-ctf-craft2 scratch folder.

Counts: blockers 0, should fix 2 (general 1, family 1), polish 1 (family 1), nits 7 (general 4: items 4, 8, 9, 10;
family 3: items 5, 6, 7).

## Findings

### Should fix

1. **P300 at 680x425, 800x500 and 375 wide: the flag in the open 03:02 row is cut off.** The log card scrolls
   sideways (overflow 134 px at 680, 54 px at 800, 197 px at 375). The details row spans the whole table (`colspan`),
   so its line runs to the table's far edge, past the visible part of the card. Measured with the 03:02 details open:
   the text ends at x=515 and the scroll box ends at x=419 (680) or 499 (800). The frame `func/p300det-680.png` shows
   "Second step denied by the account owner. flag{secon" and nothing more. The `result` column (blocked, signed in)
   is also off screen at those sizes. Nothing on screen says the card scrolls sideways: scrollbars are thin or
   hidden, and on a phone there are none. The 680x425 preview is the tool page's first look, and this is the tile's
   one answer. Better: let the details cell wrap to the card's visible width. For example, wrap the details content
   in a block that is `position: sticky; left: 0` with its width set to the `.sec-scroll` clientWidth, set on toggle
   and on resize. Also give the card a sideways-scroll cue, such as a fade at the right edge. Seen in `kit/security.js`
   `detailRow`, drawn as P300 at every STANDARDS size. **family:security** (any log with `details` and many columns).

2. **The tile flip never plays.** `toBoard()` (src.html:922 to 924) calls `renderBoard()`, which adds `.flip` to a
   tile whose state changed and updates `shown`. Then `relayout(true)` calls `renderBoard()` again
   (src.html:1249, `force`), rebuilding the grid without the class. Check `fin/flip`, Motion on: after a flag on C200
   and Back, the C200 tile class is `tile st-flag` with no `flip`, and `document.getAnimations()` is empty. The spec
   (Motion off: "no tile flip") and the handoff ("A changed tile flips once") both expect it. Better: in toBoard, call
   relayout first and render once, or don't re-render when the board was already drawn in the same call.
   **general**

### Polish

3. **The log's column names scroll away.** `.sec-table th` is `position: sticky; top: 0`, but the box that scrolls
   up and down is the tool's `.artwrap`, not `.sec-scroll`. At 680x425, scrolling down to the open 03:02 row hides
   the time / device / second step headers (`func/p300det-680.png`). Better: give `.sec-scroll` a max height inside
   the challenge, so the header sticks inside the card, or make the header stick to the outer scroller.
   **family:security**

### Nits

4. `save()` writes the screen-only flag `justPatched: true` into localStorage (seen in the stored JSON after a patch,
   check `func/k3b`). `load()` drops it, so nothing breaks, and it is not typed text. Better: save only st, hint,
   tried, first. **general**
5. `kit/security.js:323`: the comment's opts list leaves out `onDetails`, `statusText` and `fieldNote`. The family
   doc says a details row "is never rebuilt", but a sort or filter rebuilds it (it stays open; only a toggle keeps
   the same element). Say "a toggle never rebuilds the row". **family:security**
6. `handle.tag()` labels on log rows are lost when the log re-sorts or filters: `draw()` reapplies marks but not
   tags. The doc says only marks survive, and no tool tags a sortable log yet. Worth a line in the doc, or keep tags
   in a map like marks. **family:security**
7. docs/families/security.md calls `Sec.COMMON` "the 20 most-used passwords (UK NCSC 2019 list)". The engine's own
   comment is more accurate: 20 passwords that are all on the NCSC list. Several (sunshine, princess, letmein,
   welcome, qwerty123) are not in that list's top 20. This predates this build. **family:security**
8. Two text bits are 11 px: the Strength bar's "70" tick label and the tile "hint" tag. The rest of the tool is 12 px
   or more (my minimum-font scan at every size). **general**
9. `tools/capture-the-flag/host.html` was left in the tool folder from the builder's `--host` run (RUNBOOK, Agent
   Chrome hygiene: delete after). I left it as I found it. **general**
10. In the 680x425 drawer (panel 250 to 320 px) the four tool tabs have 3 px side padding, and "Strength" nearly
    touches its tab's edges (`sizes/P100-680x425.png`). It is not clipped. **general**

## Contract
- One file, 147 KB. There are no `src=` or `href=` URLs. The only URLs are an SVG namespace and the engine's
  `https://x.test` example comment. `fetch`, XHR and `import()` are absent. `performance.getEntriesByType('resource')`
  is empty after opening all twelve tiles and the Toolbox (`fin/net`).
- Console: clean in every shot at every size. The one 404 was the host page's favicon at 375.
- The kit is used, not re-implemented: `Sec.world`, `Sec.artifact` (log, note, file, call, email), `Sec.pure`
  (strength, guessSeconds, caesar, vigenere, b64, lock, hostOf) and `Curio.voice`. The note-lines helper builds a
  second note artifact to get engine spots. That is unusual but uses the engine's own spot handling.
- Guard: `Sec.safeDomain('evil.com')` is false. `world.ok` is true. larkspur.example, birchline.example and
  birchline-billing.example all pass.

## Engine check (kit/security.js against docs/families/security.md, line by line)
- The pure API matches the doc: hostOf, safeDomain (with the real-TLD rule), COMMON, POOLS, strength, band, reasons,
  guessSeconds, seal, caesar, vigenere, b64, lock, clock and mmss. The DOM API also matches: guard, world, h
  (flattens nested lists, `kids.flat(Infinity)`) and artifact with every kind in the table.
- Log, as documented:
  - Details rows toggle in place (the same `tr`; `tr.sec-details` is inserted after it or removed).
  - A details row without a spot gets `tabIndex=0`, `role=button`, a label ending ". Details" and `aria-expanded`.
    Enter and Space toggle it.
  - `onDetails(row, isOpen)` fires on each toggle.
  - Sort: numbers compare as numbers only when both values are plain numbers. "07:41" and "Mon 08:02" sort as text.
  - Ties keep their first order. Check `func/k2b`: result ascending then descending put the rows in the right order,
    with Tue 03:02 before 03:04 and the open details row still under 03:02.
  - Marks: ↕ ▲ ▼. `aria-sort` is set only when `data.sort` is on.
  - The 44 px rows have a visible focus ring (`func/k2.png`).
  - Marks survive a re-sort.
- One behavior the doc doesn't state: on a row with both a spot and details, Enter or Space fires `onSpot` and also
  toggles the details. A click already did both before this change. No tool has such a row.
- Backward compatibility with data-defenders: I copied tools/data-defenders into my scratch folder and bundled the
  copy with the new engine (`bundle_tool.bundle()` on the copy; DD's real files were not touched). I drove it
  against DD's current bundle (old engine), at 1366x768 and 680x425:
  - I captured the hall, all eight puzzles in solved state (c1, c2, i1, i2, a1, a2, a3, exit) and the hall at the
    end.
  - I also captured frames of the hall and of I2 after a wrong row.
  - `body.innerHTML` is identical apart from the inlined engine source text inside the script tags.
  - Every frame is pixel-identical (PIL difference bounding box None).
  - The console is clean.
  - DD uses `Sec.h` everywhere but no log sort or details, so the deeper flattening is the only change it meets, and
    nothing it draws changed.

## Access
- **Keyboard** (`func/k1` to `k7`):
  - Load, then Tab: Board, Toolbox, Motion, Sound, Read, then the P100 tile.
  - Arrows move by position: from P100, right goes to C100 and down to C200. Enter opens a tile and focus goes to
    Back to board.
  - In a challenge, Tab goes: the artifact spot, Flag, Submit, Hint, Toolbox, then the tool tab and its controls.
  - P300 by keyboard: Enter on a row opens it and focus stays on the row.
  - Flag by keyboard: Enter in Flag. Focus moves to the first patch choice.
  - A wrong patch by Enter shows its reason and focus stays on it. The right one turns every choice aria-disabled,
    and focus stays on the chosen one.
  - S100: Space on lines 2 and 5, Tab on to Check lines, Enter shows `flag{call_back}`.
  - L300: Enter on T, R, A, C, E spells TRACE.
  - Toolbox tabs: the arrows wrap, use a roving tabindex, and change the hint at once.
  - Nothing moves focus on load.
- **Focus when controls rebuild:**
  - The board re-render keeps focus on the same tile (focusId).
  - Back returns focus to the tile just closed.
  - Clear progress: focus goes to No, No returns it to Clear progress, and Yes also returns it to Clear progress.
  - The patch card updates in place. The Hint and Toolbox buttons keep their element.
  - Copying a spot into a tool keeps focus on the spot.
  - Log sort and details keep focus on the header button or the row.
- **44 px targets:** none under 44 at any size, by a scan of every visible button, role=button, tab, input, select,
  textarea and tabindex element.
- **Color is never the only signal:** tile states and the challenge pill have an icon and a word. At a narrow stage
  the pill's word hides, but the icon and points stay. Patch choices have a check or a cross plus the reason.
- **Motion off** (`fin`/`func/calm`): no running animations, the sticky note is not rotated, and the wheel has no
  transition. The Hint pulse becomes a static ring (CSS). With Motion on, the flip is broken (should fix 2).
- **Saving:**
  - localStorage `curio-capture-the-flag` holds only tile st, hint, tried and first (plus nit 4), never typed text.
  - Progress survives a reload (`func/k4` read L100 patched after a new tab).
  - Clear progress after Yes resets every tile and the score to 0.
  - Privacy is stated on the Board ("saved on this device only ... never what you type") and in the Toolbox.

## Layout (STANDARDS sizes; `sizes/`, `host/`)
I checked the Board, the Toolbox, eleven tiles, P300 with details open and the patch card. The sizes were 680x425,
800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000, and 375x812 inside the iframe host.
- No sideways page scroll at any size, and no header overflow.
- Flag and Submit are in view in every challenge at every size: y 166 to 210 at 680x425, 178 to 222 wide, 927 to 971
  at 760x1000 and 739 to 783 at 375.
- No clipped labels by scan.
- Wide logs: P300 scrolls sideways inside its card at 680, 800 and 375 (should fix 1). The other logs (P100, S200,
  L100, L200) fit at every size.
- The 375 board is two bands of two categories with row labels. The 375 Toolbox fits with a 124 px wheel.

## Lines and voice
- `allLines()` (41) matches `voice/lines.json` (41) word for word, both ways. There are no em dashes in src, notes,
  handoff, lines, the engine or the family doc. "Curio Class" is always written in full. The words are
  classroom-safe.
- Art: prompts.json has no assets and src has no `art:` tokens, as the spec says (drawn in code).
- The standard voice check, with held clicks (0.12 s) and Sound and Motion on:

| line | kind | expected | spoken |
|---|---|---|---|
| notyet (5 wrong flags on C100, 3.5 s apart) | how | 1, then silent | 1 spoken, 4 silent (heard) |
| flag (5 tiles) | event | 5 | 5 |
| patched (5 tiles) | event | 5 | 5 |
| w-board (Back after the first tile, then four more Backs) | welcome | 1 | 1 |
| all (12th patch, Back 0.3 s later) | event | heard once | `patched` spoken, `all` dropped (hush) and spoken again on the board 4 ms later |

- **Stale** (taps 0.33 s apart: tile, right flag, wrong patch, right patch, Back, Toolbox, Board):
  - `flag` at the flag, then cut in by `patched` at the right patch.
  - `w-board` at Back, then `w-toolbox` at the Toolbox.
  - Nothing played after its moment, and nothing came out of order.
- **First tap** (one fresh page each):
  - The stage: w-board at once.
  - A tile: nothing. The tile has no line of its own, and the board welcome no longer fits.
  - Toolbox: w-toolbox.
  - Read: the read entry only.
  - Sound: nothing. Sound off then on: w-board once.
  - Tab key: w-board.
  - Tile then Toolbox drawer: nothing.
- **Read:** Read during w-toolbox cut it and spoke the hint. A mode change 0.5 s after Read started w-board at once
  (4 ms). With Sound off, Read still speaks, on the board and in P100.
- Every spoken line matched the screen at its time (the log against the click times above).

# data-defenders: Craft lens (round 1)

Cold read of spec.md, src.html, notes.md, handoff.md, art/prompts.json, voice/lines.json, kit/security.js and
docs/families/security.md (the new family engine and its doc). Bundled with `CURIO_DRAFT=1` (181 KB). Driven with
`scripts/drive.py` and held clicks (`hold 0.12`) on ports 9550-9556, own profiles in the lens scratch folder; about 90
shots. Browser voice (no clips yet) and placeholder art are expected and not reported.

Counts: blocker 1, should fix 4, polish 5, nit 4.

## Contract

| Check | How | Result |
|---|---|---|
| One file | bundle `tools/data-defenders/data-defenders.html` | pass, 187,622 bytes (181 KB), under 2 MB |
| No network requests | `performance.getEntriesByType('resource')` after load: `[]`; grep of the bundle for `http`: only the SVG namespace and a code comment | pass |
| Nothing stored | localStorage holds only the kit's `curio-motion`; sessionStorage and cookies empty | pass; privacy line on screen ("Nothing you do here is saved or sent anywhere") |
| Console | every drive.py shot (about 90, every size and room, full solves, voice runs): no errors, warnings or exceptions | pass |
| Kit used | `Curio.voice`, `Curio.yes/tone`, kit header and Motion; `Sec.lock`, `Sec.clock`, `Sec.strength/band`, `Sec.seal`, `Sec.artifact('file' row / 'log')`, `Sec.world` | pass, nothing re-implemented |
| `sec.safeDomain` | `evil.com`, `gmail.com`, `x.test.evil.com`, `http://localhost`, `test`, `.test` false; `cedarhollow.example`, `https://x.example.com/a`, `a@b.test`, `EXAMPLE.ORG`, `https://evil.com@x.test` (real host x.test) true | pass |
| Engine numbers | bands Weak, Weak, Weak, Strong (with the tool's names); seals 70, 67, 79, 65 | pass |

## Engine against the spec's family description, and the doc against the code

The engine matches the spec's family section: World `{name, people, accounts, files, domains}` with a guard that logs
one console error per non-reserved name; artifacts email, sms, login (fields never take typing), log, file, call, note;
spots with tap, Enter and Space; links that never navigate and show the real href in a status bar; `strength` pools
26/26/10/33, `bits`, `wordBits` (7776 words), the 20-password common list exactly as the spec lists it, `band` cut-offs
8 and 15, `seal` = sum, `caesar`, `vigenere(text, key, dir)`, `b64` (UTF-8 safe); `lock({check, normalize})` with
trim and lowercase default; `clock({mode, ms, onEnd})` with pause and reset; the pure block has no DOM and is
`__tool.sec`. `world()` does not look inside `files` (the spec lists files in the World); nit 3. Doc drift is in
nit 4 and polish 5.

## Findings

### Blocker

**B1. Split rooms swallow the first tap on the other puzzle (1280x720, 1366x768, 1920x1080).** general
- Where: src.html:836-837 (`renderRoom`: station `pointerdown` calls `setActive`, `focusin` calls `setActive` in split
  mode) with src.html:809/842 (focus restored by `data-k` after the rebuild).
- What: in split mode (stage at least 880 px wide, so every laptop and big-screen size) both puzzles show side by side.
  Pressing any control in the inactive station runs `setActive` on `pointerdown`, which rebuilds the station DOM under
  the pointer, so the `click` never reaches the button. Worse, the rebuild restores focus to the element focused before
  (`enter()` focuses the first C1 cell), whose `focusin` calls `setActive` back to the first puzzle. Net effect: the
  first one or two taps on Puzzle 2 do nothing, and the first puzzle's how-to line plays while the student is working
  on the second.
- How seen: `drive.py` held clicks at 1366x768, `__tool.state` after each (scratch sp0-sp3, spA, spI, spM):
  1 tap on "Tap to test" in Pick the password: active still `c1`, nothing tested; 2 taps: active `c2`, still nothing
  tested; 3 taps: tested. With no prior focus (mouse only): 1 tap only switches. A2 plan B and I2 row 2: first tap
  ignored. Voice logs: rep_c2 (5 taps on "Use this one" gave 3 results; "Tap a box to take a folder away. Then press
  Check lock." spoken at 11.5 s, after the student tapped the password station), rep_a2 (5 taps, 4 results), rep_i2
  (6 taps, 4 results), i2b (the right row needed three taps; "Add up each card..." spoken after the first tap on the log). At 1000x625 and below (tabbed) the bug does not occur.
- Better: switch the active station without rebuilding the pressed control (toggle classes on `pointerdown`, render on
  the next frame after `click`), and do not restore focus into the other station after a pointer switch.

### Should fix

**S1. Focus is invisible on a marked score chip (Seal check).** family:security
- Where: kit/security.js:191-192 (`.sec-spot:focus-visible` and `.sec-spot.sec-marked` have the same specificity; the
  later `sec-marked` outline wins) and :254.
- What: a keyboard user who presses Enter on a score chip marks it; the chip is rebuilt and refocused, and its focus
  ring is replaced by the pale gold "marked" outline (`#ffd27a` on white), identical to the other marked chips. You
  cannot tell where focus is. Same for any marked/right/wrong spot that uses an outline in the siblings.
- How seen: frame `kb_i1_marked` (Enter on Ari Q1, Tab, Enter on Ari Q2; `document.activeElement` is Ari Q2, which
  looks the same as Q1).
- Better: give `.sec-spot:focus-visible` higher specificity (or put it after the mark rules) and draw marks with
  background/border so the focus outline stays on top.

**S2. Tap targets under 44 px.** family:security (chips, rows), general (Back)
- Where: kit/security.js:248 (`.sec-chip` min-width 40), src.html:242 (`.compactui .sec-chip{min-width:34px}`),
  kit/security.js:225 (`.sec-table` cell padding 6/8 px), src.html:224 (`.tabtop .back>span{display:none}`).
- What: Seal-check score chips are 40x44 at 1280 to 1920 and 760 wide, 34x44 at 680x425, 800x500, 1000x625 and 375
  wide (16 tap targets the student uses in every attempt). Change-log rows (the I2 spots) are 29-31 px tall at
  800x500, 1000x625 and 1920x1080. The icon-only Back button is 40x44 at 680x425, 800x500, 1000x625 and 375 wide.
- How seen: bounding boxes of every visible button and `role=button` per size (scratch m_*.json, h375_*).
- Better: chips at least 44 px wide (two rows of chips or a tighter seal chip in compact), `min-height: 44px` on
  spot rows in the engine, Back padding to 44 px.

**S3. The locked Exit door says nothing; its tap brings a late welcome over its hint.** general
- Where: src.html:715-717 (`doorTap`, locked Exit: `setHint(L.hExitLocked)` and a low tone only) with `speaks: '.door'`
  and `welcomeAfter` (src.html:632).
- What: a solo student who cannot read taps the Exit (the brass door is the most inviting) and hears only a buzz. The
  waiting moment does not say how to act (STANDARDS, "Say how to act"). On a first tap the welcome then arrives about
  4 s later and overwrites the "The exit opens when all three rooms are secured" hint.
- How seen: voice check first-tap run `ft_exitlocked`: tap at 1.21 s, welcome spoken at 5.35 s, final hint = welcome.
  Every later locked-Exit tap: no line at all.
- Better: speak `hExitLocked` as a how line (once, then hint only), and let it count as the tap's own line so the
  welcome is queued after it, or skipped.

**S4. Focus ring on the compact puzzle tabs is dark blue on the room's blue bar.** general
- Where: src.html:185 (`.tab:focus-visible` uses `--focus` #1d4ed8 inset) with src.html:216-219 (tabs moved into the
  room-colored `.rtop` in `compactui`).
- What: at 1000x625, 800x500, 680x425 and 375 wide the unselected tab is translucent white over #2f5ea8 (Records Room);
  the focus outline #1d4ed8 on it is about 1.7:1, below the 3:1 a focus indicator needs. On the green and orange rooms
  it is low too.
- How seen: frames `ctab_kb` (Shift+Tab from the first cell onto "Password"), zoomed.
- Better: in `.rtop` use the gold focus the Back button already uses (`outline: 4px solid var(--gold)`).

### Polish

**P1. Lock slots never "pop" with Motion on.** general
- Where: src.html:176-178. `.rlock .ls.pop{animation:pop}` is followed by `.rlock .ls.pop{animation:flash}` (it was
  meant to be `.calm .rlock .ls.pop`), and line 177 repeats `.rlock .cnt` under `.calm`.
- What: Motion on and off both show the calm outline flash when a symbol is found; the pop the code defines never runs.
- How seen: `getComputedStyle(.rlock .ls.pop).animationName` = `flash` with Motion on (shot `pop_on`) and off.
- Better: scope the flash rule to `.calm`, so the found symbol pops with Motion on (same 0.6 s).

**P2. On room entry the hint, and so Read, is the story, not the action.** general
- Where: src.html:734 (`setHint(story)` on a first entry).
- What: while the story plays (about 10 s with the browser voice), Read speaks the story again, and Read pressed then
  also drops the queued how-to ("Tap a box to take a folder away...") until the next action. A non-reader who presses
  Read to learn what to do hears the story twice.
- How seen: voice run `read_during`: Read at 3.0 s spoke the story text; `c1` dropped (hush); nothing re-queued it.
- Better: keep the room's how line in the hint from the start (the story card in the panel already shows the story),
  or have `read` return the story plus the how line.

**P3. Wrong results wait behind the 10 s room story.** general
- Where: src.html:736 (story and how queued as one sequence) with `sayWrong` (src.html:647).
- What: a team that presses Check lock while the story is still playing hears "Not yet" only after the story ends, by
  then often dropped by their next tap. The panel result shows at once, so this is about the voice only.
- How seen: probe run: Check lock at 5.3 s, its "Not yet" dropped as newer at 9.6 s; the second one spoken at 11.7 s.
- Better: shorter story lines, or let a check result cut a how/story line already playing (`now: true` for results).

**P4. Engine controls the siblings will use are under 44 px.** family:security
- Where: kit/security.js:227 (`.sec-table th button` sort buttons, min-height 28 px), :240 (`.sec-tools select`,
  32 px), :220 and :222 (login fields and fake button, 40 px).
- What: not used by Data Defenders, but phishing-spotter and capture-the-flag will inherit them.
- How seen: code read.
- Better: 44 px minimums in the engine now, before the siblings build on it.

**P5. `Sec.band(string)` silently ignores names.** family:security
- Where: kit/security.js:56-58; docs/families/security.md "Pure checks".
- What: `band('Cedar2026')` is `OK`; only `band(strength('Cedar2026', ['cedar','hollow']))` is `Weak`. Data Defenders
  does it right, but the doc shows `Sec.band(r)` and the string shortcut is undocumented, so a sibling passing a string
  would teach a wrong band.
- How seen: shot `contract`: `Cedar2026` Weak with names, OK as a string.
- Better: `band(r, names)` (names passed through when r is a string), and say so in the doc.

### Nit

**N1.** src.html:891-892, 905: `b` is computed and unused in `meterKey`; `i2Row` bumps `LK.i2.misses` directly
(src.html:988) instead of going through the lock. general

**N2.** Escape card (src.html:1169) has `role="dialog"` but no `aria-modal` or focus trap; Tab leaves it for the
panel behind the scrim. general

**N3.** `Sec.world` (kit/security.js:158-168) checks `domains`, `accounts` and `people` but not `files`, which the
spec's World includes. family:security

**N4.** Doc drift in docs/families/security.md: the `note` row says "`sticky` or `text`" (the code reads
`style: 'text'`, else sticky, plus `text`); the file-row seal's `icon` and the file `title` are not listed;
`onSpot` is called with `(id, el, tell, e)`, not `(id, el)`; the code comment at kit/security.js:389 lists `sort` as a
column key where the code and doc use `nowrap`. family:security

## Access

- Keyboard: Tab goes header (Escape, Motion, Sound, Read), panel (timer, Start over, and in rooms Check lock / Clue),
  then Back, then the puzzle; in the hallway the four doors come after the panel (shots `kb_hall`, `kb_roomC`). Space
  and Enter toggle the C1 checkboxes; Enter on a log row picks it; Enter on an exit card then Enter on a slot head sorts
  it (`kb_exit_sort`). Tabbing from Puzzle 1 into Puzzle 2 in split mode switches the active station correctly
  (`kb_roomC_fwd`).
- Visible focus: kit 4 px outline everywhere except S1 and S4; doors and Back use gold on the dark/colored bars.
- Color never the only signal: C1 cells show a check or an x with "can open" / "no"; meter has the word and a pattern
  bar; A1 over-capacity bars are striped and labeled "too many" (or the number at narrow widths); A2 lost days are
  struck through with an x; doors carry their letter and icon.
- Motion: door swing and card slides off with Motion off, replaced by outline flashes of the same length (shots
  `door_calm`, `pop_calm`); see P1. Sound off: lines go silent and the hint still updates (`read_soundoff`). Read works
  with Sound off.

## Lines

`__tool.allLines()` returns 48 strings; `voice/lines.json` has the same 48, word for word and in the same order. All
under 200 characters, no em dashes, nothing a voice would misread. Every spoken line in the runs below matched the
state on screen at its time (checked against the hint, room and active puzzle sampled when each line started), except
the stale `c1` line in B1.

## Standard voice check

Held clicks, Sound and Motion on, 1366x768 unless named. Logs read from `__tool.vlog`.

**1. Repeats** (each action five times in a row; `rounds` = five full games on one page, with Start over between)

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| welcome | welcome | 1 | 1 (stage, mode button, timer, Tab key; 0 after Sound first, then 1 on Sound on, not again on off/on) |
| storyC, storyI, storyA | how | 1 each per page | 1 each, then silent 4 (rounds); storyC 1 over 5 entries (rep_enterC) |
| c1 | how | 1 | 1, then silent (rep_enterC: dropped by Back once, spoken on the next entry, silent 3) |
| c2, i1, i2, a1, a2, exit | how | 1 each | 1 each, then silent 4 (rounds) |
| i2b | how | 1 | 1 (run i2b) |
| back | how | 1 | 1, then silent 9 (rounds) |
| exitOpen | how | 1 | 1, then silent 9 (rounds) |
| hPlace (Open the exit with cards left) | how | 1 | 1, then silent 3 (exit_hplace) |
| wrong, C1 Check lock x5 | event | 5 | 5 |
| rShortName + wrong, C2 "Use this one" on "cedar" x5 | event | 5 + 5 | **3 + 3** (B1: first two taps swallowed) |
| i1wrong + wrong, I1 "This one was changed" on Ari x5 | event | 5 + 5 | 5 + 5 |
| wrong, I2 row 1 x5 (6 taps) | event | 5 | **4** (B1) |
| wrong, I2 wrong fix x5 | event | 5 | 5 |
| a1four + wrong, A1 Set servers at 4 x5 | event | 5 + 5 | 5 + 5 |
| wrong, A2 plan A x5 | event | 5 | **4** (B1) |
| wrong, exit with wrong cards x5 | event | 5 | 5 |
| symbol | event | 30 (6 per game x 5) | 30 |
| secC, secI, secA | event | 5 each | 5 each |
| escaped | event | 5 | 5 |
| time (timer at 0) | event | 1 | 1 queued, hint "Time! Keep going to finish." at once (time_evt) |

**2. Stale lines.** Fast taps (gap 0.2-0.25 s) through Check lock x3, Back, Start over, Yes (stale_c); Check lock, the
Password tab, two "Use this one", Back, Server Closet door at 1000x625 (stale_tabs); three "This one was changed" then
Back at 1366 (stale_late). Every overtaken line was dropped (`newer`, `chain`, `hush`); no line played after its
moment, none named a hidden control. The one stale line found is B1's (the first puzzle's how-to spoken after a tap on
the second puzzle, in split mode).

**3. First-tap timing.** Stage: welcome at +0.12 s. Mode button: +0.14 s. Timer button: +0.12 s. Tab key: at once.
Read: speaks the hint only ("Tap a door to go in...."), no welcome. Sound: nothing; Sound on brings the welcome once,
a second off/on does not repeat it. Door (its own line): story then how-to, no welcome (by design: the welcome is
valid only in the hall before any room). Locked Exit door: no line of its own, welcome 4.1 s later over its hint (S3).

**4. Read.** Read during the room story stops it and speaks the hint (read_during); with Sound off Read speaks the hint
(read_soundoff); Back right after Read takes the next line at once (read_then_back). See P2: during the story the hint
is the story.

**5. Order.** In every log the spoken lines follow the order of the actions; no older action's line played after a newer
one's.

## Words

No em dashes in src.html, notes.md, voice/lines.json, kit/security.js or the family doc. "Curio Class" only (every
other "Curio" is `Curio.` code). Language classroom safe. Privacy stated on screen and in notes. Art: one token,
`art:dd-night-hallway`, has its prompts.json entry; no people.

## Frames and runs looked at

contract; hall, C, I, I2, A, X at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000 (target and
fold measurements); 375x812 via `--host` (hall, C, I, A, X); kb_hall, kb_roomC, kb_roomC_fwd, kb_c1_space,
kb_i1_marked, kb_exit_sort, kb_compact_tabfocus, ctab_kb, ctab_kb2, kb_i2_rowfocus, i2row_kb, kb_i2_enter; pop_on,
pop_calm, door_calm, esc_card, esc_card_375; split0-3, splitI, splitA, splitC_mouseonly; voice runs probe, rep_c1,
rep_c2, rep_i1, rep_i2, rep_a1, rep_a2, rep_enterC, rep_exit, exit_hplace, exit_wrong, ft_stage, ft_door,
ft_exitlocked, ft_mode, ft_read, ft_sound, ft_timer, ft_key, read_during, read_then_back, read_soundoff, stale_c,
stale_tabs, stale_late, time_evt, rounds, i2b.

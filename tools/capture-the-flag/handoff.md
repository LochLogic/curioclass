# capture-the-flag: handoff (Build, batch BR; Refine round 1)

## What it is

- `src.html` on the kit starter with `kit:curio`, `kit:theme-912` and `kit:security`; brand `#ff7ac8` on the 9-12 dark theme.
- Two modes, Board (opens first) and Toolbox, as spec.md lays out.
- **Board:** a 4 by 3 grid (Passwords, Codes, People, Logs; 100, 200, 300) with Score, "Flags N of 12" and "Patched N of 12".
  - Tile states each have an icon and a word: open, patch it (amber border, flag), patched (green fill, shield). A "hint" tag shows on a tile whose hint was used.
  - Arrow keys move between tiles by where they sit; Back to board returns focus to the tile just closed. A changed tile flips once (Motion on only).
  - Under 400 px of stage the board becomes two bands of two categories, and the tile rows shrink (64 to 110 px) so the board fits a phone window.
  - The panel says how scoring works (including the cost of a wrong flag) and the ethics line: only ever test a real system you own or have written permission to test.
- **Challenge view:** Back to board, the title, a state and points pill (it shows what the tile is worth now), the brief, the artifacts (all drawn by the engine).
  - Panel order: hint, Flag and Submit (with "A wrong flag takes N points off this tile." before the first try), the Patch card after the flag, Hint (half points), the Toolbox drawer.
  - Every artifact spot copies its text into the open tool and opens the drawer; the tool's answer is then brought into view (smooth only with Motion on) and "Copied into Strength." (or the tool's name) shows above the artifact.
- **Toolbox:** one instance, moved between the Toolbox stage and the challenge drawer, sized by container queries. Shift (two-ring wheel), Keyword (Vigenere), Base64, Strength.
- **Scoring:** a flag is worth 100, 200 or 300. A hint takes half; each wrong flag, wrong S100 Check lines or wrong full L300 order takes a quarter of the tile's value, never below a quarter. A first-try patch adds 50. Most is 3,000.
- **Saved** in localStorage `curio-capture-the-flag`: per tile only st, hint, wrong, tried, first (never typed text), inside try/catch. Clear progress asks Yes or No.
- **Voice:** `Curio.voice` with `hint: false`, `read`, and scope. Welcomes `w-board`, `w-toolbox`; how line `w-chal` the first time an open challenge is shown; events `flag`, `patched` (both name the next control) and `all` (alone on the twelfth patch); `notyet` on a wrong flag. voice/lines.json is regenerated from `allLines()`.

## Answer key (teacher copy; deliberately not in notes.md, which the public page shows)

| Tile | Flag | Where it is |
|---|---|---|
| P100 | `flag{bkoh}` | the account whose password is on the common list (password1) |
| P200 | `flag{77_bits}` | Strength prints it for the six-word passphrase (77.5 bits) |
| P300 | `flag{code_denied}` | details of the Tue 03:02 sign-in row |
| C100 | `flag{dock_door_2580}` | Base64 decode of the night guard's note |
| C200 | `flag{dispatch_password}` | Shift back 7 |
| C300 | `flag{key_in_readme}` | Keyword decode with LANTERN (the key is in readme.txt) |
| S100 | `flag{rush_and_code}` | mark lines 2 (or 7) and 5, then Check lines |
| S200 | `flag{0752}` | the badge log time when two came in on one badge |
| S300 | `flag{birchline-billing.example}` | the look-alike sender domain |
| L100 | `flag{gnair}` | five failed sign-ins in a row from a new device |
| L200 | `flag{hwu}` | sort by files read: 312 and 140 at 01:47 and 01:49 |
| L300 | `flag{TRACE}` | cards in the order T, R, A, C, E |

Right patches: P100 refuse breached-list passwords; P200 allow passphrases of 64 or more with spaces; P300 app prompt with number matching; C100 password manager entry for the guard; C200 password manager; C300 AES with the key in a key manager; S100 call IT back at the directory number; S200 badge in plus count-gap alerts; S300 call the supplier at the number on file; L100 slow sign-ins plus a second step; L200 remove hwu's Finance access; L300 a security key for people who move money.

## Refine round 1: what changed (refine.md item numbers)

- **B1 Strength meter.** New `Sec.pattern(pw)` in kit/security.js rates pattern passwords by their parts (dictionary-like words, a capital, swaps such as 0 for o undone, a year, digits, symbols, separators, keyboard runs); `strength()` returns `pattern` and `patternBits` and uses the lowest of bits by characters, by words, by pattern. Winter2026! now reads 26.6 bits, Kettle Orbit Maple 44.1, Gr4v1ty#7 24.3, xK9#mQ2$vL stays 65.7 (no pattern). On screen: "Bits by characters (if every character were picked at random)", "Bits by words or pattern" with the parts listed, "Bits used (the lowest)", a pattern warning line, and "On a list of 20 very common passwords". Documented in docs/families/security.md (COMMON wording, `Sec.pattern`, checked values).
- **B2 Tradeoff patches.** Every patch question states a constraint (who uses it, what it costs, what it protects); all three choices are defensible and each shows its cost and gain; the right one depends on the constraint; a patched tile shows "Traded: ...".
- **3 Give-aways.** Seven flags renamed so none names the fix (table above); S100 line 8 cut; the right choice sits in varied positions and is the longest on only 4 of 12 tiles, with lengths within about 8 characters.
- **4 Guessing costs.** Wrong flag, wrong Check lines (S100) and wrong full order (L300) each take a quarter, floor a quarter, said before the first try; wrong tries are saved. spec.md updated. Not done: an evidence tap for tiny searches (see gaps).
- **5 P200.** Right choice now "Let passphrases run to 64 characters or more, with spaces"; the reason quotes NIST (allow 64 or more).
- **6 L300 reason.** "the chain stops at A (a passkey, with no password at all, would stop R too)".
- **7 notes.md.** The flag list is gone; the answer key is here only.
- **8 Result in view.** After a copy the tool's answer is scrolled into view (`block: 'nearest'`, smooth only with Motion on) and "Copied into X." shows; the copy note sits above the artifact. Toolbox text boxes are 48 px tall under 520 px of window height so Text out stays in view at 680x425 and 800x500.
- **9 L300 payoff.** The order chips and the spell line sit above the cards; placed cards show their place, and their letter once the order is right ("1: T").
- **10 P300 details.** Engine: details sit in a `.sec-detailbox` sized to the visible width of the scroller (sticky at the left), so text wraps in view; a table wider than its card fades at the right edge (`.sec-more`). P300 dropped its place column (folded into the device cell) and says "Swipe the table sideways" on a narrow stage.
- **11 Flip.** `toBoard()` draws once through `relayout(true)`; the flip plays (checked).
- **12** Assumption line under the time: an offline attack on stolen password hashes.
- **13** C300's right fix is AES with the key in a key manager.
- **14** Ethics line on the board.
- **15** Times in words: million, billion, trillion, "more than a thousand trillion years".
- **16** `flag` and `patched` lines name the next control.
- **17** `w-chal` on opening an open challenge.
- **18** Wide screens: panel `clamp(360px, 30vw, 560px)`; on a stage of 1200 x 820 or more, artifact text 16 px.
- **19** P300's second step column is in view at 375 (5 columns now).
- **20** Phone board rows shrink to fit (see host check).
- **21** A log's own scroller gets a max height from the stage space (`--logmax`), so its sticky column names stay in view.
- **22** `justPatched` is in memory only (`state.justPatched`).
- **23** At 561 to 999 px wide the header keeps one row (the subtitle hides).
- **24** `.arts.two` aligns to the top: no gray band under the short email.
- **25** The bar has a "70 bits" tick label and a "128" end label.
- **26** Engine: opts comment lists every option; row tags survive a re-sort or filter (kept in a map); COMMON comment says "a short sample: 20 very common passwords".
- **27** host.html deleted after the 375 run.
- **28** Nits: clearing the patch box removes `dataset.tile` (so `__tool.open` reads null), pill and tab padding, 12 px hint tag, Base64 hint wording, P300 copy note.

## Exit check round 2

1. `Sec.pattern` no longer skips runs with odd capitals or repeats. Letter runs split before a Title-case word after a capital run (I + Love, NY + Knicks); a capital run of 3+ with a vowel keeps its letters (LOL + password); a capital run of up to 4 that is not word-like counts as letters; one character 3+ times in a row is a repeat; a whole password that is one unit typed again is rated as the unit plus log2(times) + 1. Empty result now reads "no pattern this meter knows (it has no dictionary, so names and phrases can still be guessed sooner)". The family doc no longer says "never over-rated". Recomputed (used bits, by characters in brackets): ILoveMyDog2008! 57.6 (98.5), IHateMath1! 41.9 (72.3), NYKnicks2026 33.0 (71.5), ILoveYou123 43.5 (65.5), LOLpassword 26.8 (62.7), twenty z's 10.0 (94.0), Ab1!Ab1!Ab1! 28.9 (78.8). Spec values unchanged: P100 rows 36.8, 36.2, 38.8, 26.6, 28.8 (password1 16.2); P200 24.3, 37.6, 38.8, 77.5 (677,000 years, shown as about 700,000). data-defenders scratch bundle: 4 frames pixel-identical again.
2. C200's title is now "Only 25 keys", matching its reason and Traded line.
3. Strength readouts stack (name over value) in a Toolbox narrower than 380 px, so at 375 each value has the full width.

## Engine changes in kit/security.js (all backward compatible)

From Build:
1. Log rows with `details` open and close in place (a `tr.sec-details` is inserted or removed); details rows without a spot get a tab stop, `role=button`, `aria-expanded`; optional `opts.onDetails(row, isOpen)`.
2. Log sort compares as numbers only when both values are plain numbers; ties keep their order; sort buttons show arrows and headers get `aria-sort` when `data.sort` is set.
3. `Sec.h` flattens nested child lists.

From Refine round 1:
4. `Sec.pattern(pw)` (pure, exported; repeats and capital-run splits added at exit check round 2) and the `pattern` and `patternBits` fields on `strength()`; `used` is the lowest of the three.
5. Log tables sit in `div.sec-scroll`; details sit in `div.sec-detailbox`, sized to the scroller's visible width and sticky at its left edge; `.sec-more` fades the right edge while more columns are off to the right (a ResizeObserver and a scroll listener keep both current).
6. Marks and tags are kept in maps and re-applied on every redraw, so they survive a sort or filter.
7. Comments: the opts list and the COMMON sample.

docs/families/security.md is in step with all of these.

**data-defenders re-check (Refine round 1):** a fresh scratch copy of DD bundled against the changed engine (its real files untouched), driven at 680x425 and 1366x768 (hall and the I2 log). All four frames are pixel-identical to the baseline frames taken before any engine change (PIL difference bbox None); console clean.

**Note for whoever edits security.js:** its stylesheet is a JS template string, so a CSS escape like `'\25B8'` is an octal-escape SyntaxError that kills the whole engine. Use the literal character.

## Checked in Refine round 1 (drive.py, ports 9861 to 9863, own profiles in scratch)

- Function run at 1366x768: every flag opens only its own tile; a cross-tile flag is refused and costs (P100 to 75); decodes match; L300 wrong order costs, right order shows TRACE with "1: T" tags; P200 prints "Rated 77.5 bits: flag{77_bits}"; Strength texts as above; the flip plays; the saved JSON holds no justPatched; a reload keeps wrong counts; console clean.
- Size audit at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900 on the board, P300 (details open), P200 and C200 (after a copy), L300 (ordered), S100, S300, L100, a patch card and the Toolbox: clean (44 px targets, no clipping, no overlap, no page sideways scroll). P300's details box sits inside the visible scroller at every size; the copied result, the L300 spell line and Toolbox Text out end inside the window at every size.
- 375x812 through `--host` (every tile, Toolbox, a patch): clean. The board fits (last tile ends at 762 of 812, tiles 84 px); P300 shows the swipe line, fades at the right, and its open details (`flag{code_denied}`) wrap inside the visible card; after a tap the P200 flag (792-812) and C200 Text out (748-812) end inside the window; the L300 spell line is at 334.
- audit_tool.py: clean at every size and with Motion off; one held click per control and five held clicks at 2 s are clean. Three leads, answered: 760x900 "h1 clipped" is a false lead (h1 measures 180/180; the hidden subtitle's text is counted); at 375 the board hint and Clear progress sit below the board, which fills the phone window and is itself the next control.
- Bundled with `CURIO_DRAFT=1`.

## Known gaps

- **Tiny searches cost but ask for no evidence (item 4).** S300 has 2 domains and S200 a handful of times; a wrong try costs a quarter (75 or 50 points), which makes sweeping a poor trade, but the tool does not ask students to tap the row or line that proves the answer. Adding evidence forms per tile was more change than the round allowed.
- **L300's order can still be found by trying orders,** now at a quarter of the tile per wrong full order.
- **The P200 flag prints only for the exact six-word candidate while P200 is open.**
- **No recorded voice yet** (draft build: the system voice stands in).

## For Cory

- Nothing is committed. Files changed: `tools/capture-the-flag/` (src.html, bundle, spec.md, notes.md, handoff.md, voice/lines.json), `kit/security.js`, `docs/families/security.md`.
- The engine change touches every security tool. It is additive, and data-defenders is unchanged pixel for pixel.

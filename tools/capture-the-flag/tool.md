# Capture the Flag: the record

Everything after Spec for this tool, one part per old record file (scripts/tool_record.py). The spec is
[spec.md](spec.md); the teacher notes are [notes.md](notes.md).

## Refine

<!-- part: refine.md -->

PASS
Counts: blockers 2 (general 1, family 1), should fix 9 (general 7, family 2), polish accepted 17

### capture-the-flag: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames and detail.
Checked and correct (T): all 12 flags reproduce, ciphers and Base64 match, all Strength math matches the spec, the
common-list line is accurate, NIST, CISA and business-email-scam claims hold, nothing teaches misuse. Engine changes
are backward compatible: data-defenders is pixel-identical on a scratch bundle (C). No rule-5 content.

#### Blockers
1. **The Strength meter rates pattern passwords as very strong** (T-B1; family:security). Winter2026! reads 72.3
   bits and ~18,000 years while its own patch calls it predictable; capitalizing or hyphenating "kettle orbit maple"
   turns 47 seconds into billions of years. Students learn that a capital, hyphen, year or ! makes a password safe.
   Fix: one plain on-screen line that "bits by character set" assumes random characters; detect common patterns
   (dictionary words with a capital, a year, trailing digits or !, keyboard runs, words joined by - or space) and
   rate those by words, not characters, with a "pattern" warning; "list of 20" wording for COMMON. Document it in
   docs/families/security.md (STANDARDS: a meter states its assumption; REFINE: a misleading meter is a blocker).
2. **No student activity teaches the tradeoff codes** (T-B2; general). 3A-NI-07 and 3A-NI-08 (spec crosswalk) are
   only a teacher question; a solo student never meets a tradeoff (rule 2). Fix: each patch card's options carry a
   real cost and benefit (usability, money, time), with at least two reasonable options, and the right pick depends
   on a constraint stated in the challenge (who uses it, what it protects); the result line says what was traded.

#### Should fix
3. **The patch is given away** (T-S3; general). On 7 of 12 tiles the flag names the fix (keep_keys_apart, call_back,
   ...), Dana's line 8 states S100's fix, and the right option is always the longest. Rename those flags, cut the
   line, and even out option lengths (vary which is longest).
4. **Guessing every option is free** (T-S4, P-S2; family:security). P100, L100, L200 (account names), S200 (10
   times), S300 (2 domains), S100 (28 line pairs), L300 (5 positions for R). Fix: a wrong flag or check costs points
   (for example 25 percent of the tile, floor at a set minimum) and says so before the first try; where the search is
   tiny, ask for the evidence too (tap the log row or line that proves it). Settled with BASELINE (quality over
   saved work): this changes the spec's scoring; update spec.md to match.
5. **P200 "Long passphrases: at least 64 characters" reads as a minimum** (T-S5; general). NIST: allow at least 64
   as the maximum. The rewarded 35-character passphrase would fail the line as written.
6. **L300's reason "It breaks the chain at R" is wrong** (T-S6; general). A security key stops the chain at A (the
   sign-in); only a passkey removes R. Fix the reason text.
7. **All 12 flags are in notes.md, which the public page shows open under the preview** (T-S7; general). Move the
   answer key out of notes.md (a collapsed teacher section that starts closed, or handoff.md only).
8. **After tapping an artifact, the result is out of sight below 1366x768** (P-S1; general). At 1280x720 P200's flag
   prints at 720 of 720; at 375 the tap looks like nothing happened; Toolbox Text out is below the fold at 680x425.
   Scroll the result into view (respect Motion) or place it beside the tapped spot.
9. **L300's payoff is hidden** (P-S3; general). At 1366x768 the TRACE line is at 921 px, below the card; the cards
   turn green but never show their letters. Show the letters on the cards and the word in view.
10. **P300's flag is cut off at small sizes** (C-S1; family:security). At 680x425, 800x500 and 375 the open 03:02
    details row spans the whole table and reads only "flag{secon"; the result column is off screen with no sign the
    card scrolls. Fix `detailRow` in kit/security.js (details wrap within the visible width) and show a scroll cue.
11. **The tile flip never plays** (C-S2; general). `toBoard()` renders, then `relayout(true)` renders again without
    `.flip`. Render once, or keep the class.

#### Polish accepted
12. Say what the 10 billion guesses a second models (an offline attack on a stolen hash) (T).
13. C300's right fix still keeps the Vigenere cipher; the fix should drop it for real encryption (T).
14. A one-line frame: only test systems you have permission to test (T).
15. Big times read as words ("about 120 billion trillion years"), not "120,000,000,000 billion years" (T).
16. The spoken flag and patched lines name the next control (P; how-to rule).
17. Opening a challenge says one short line (P).
18. Wide screens: give the tools more room than the 360 px panel, and artifact text larger than 14 px at 1920 (P).
19. At 375 the P300 "second step" column is reachable (with 10) (P).
20. At 375x812 the board's last row fits or the page says it scrolls (P).
21. The log's sticky column names stay visible (the card scrolls, not .artwrap) (C).
22. Don't write `justPatched` to localStorage (P, C nit).
23. At 760 wide the header keeps Read on the same row (P nit).
24. The shorter S300 email card has no empty gray band (P nit).
25. The Strength bar gets a unit label (P nit).
26. kit/security.js: fix the stale opts comment, keep row tags on re-sort, and "20 most-used" wording (C nits).
27. host.html left in tools/capture-the-flag by a --host run: delete it (C).
28. Remaining Teaching and Craft nits in the lens files, where they stay inside the spec (T, C).

#### Settled calls
- The common-list line under Strength (builder asked for an OK): accepted by the integrator, checked accurate by T.
- C100's drawer opens on Shift, not Base64 (builder's change from the spec, so it doesn't give away the paid hint):
  accepted; update spec.md to match.

#### Exit check, round 1

Fresh cold agent, 2026-10-28. Read REFINE (Exit check, Rounds), STANDARDS, BASELINE, the BUILD wave lessons, spec.md,
handoff.md (Refine round 1), the three lens files and this list. Bundled with `CURIO_DRAFT=1` (167 KB). Driven with
`scripts/drive.py` in my own muted headless Chrome (ports 9950 to 9954, own profiles, all in my scratch folder
`exit-ctf`); 375 wide through my own iframe host served from scratch (no host.html in the tool folder). Strength and
pattern numbers recomputed with the engine's pure block in Node and checked against the page's readouts. Console
clean in every shot; no resource requests (`performance.getEntriesByType('resource')` empty after all twelve tiles and
the Toolbox); `allLines()` 41 = voice/lines.json 41, word for word; no em dashes.

##### Item by item

1. **Strength meter: OPEN (blocker, family:security), narrowed.** What was asked is in: the assumption line ("if
   every character were picked at random"), "Bits by words or pattern", "Bits used (the lowest)", the pattern warning,
   "On a list of 20 very common passwords", the offline-attack line, and the family doc. Recomputed and read back from
   the page, all match the spec: P100 Tidepool-Lantern-88 36.8, Orchard9Comet! 36.2, violet harbor bicycle 38.8,
   Winter2026! 26.6 (72.3 by characters), m0nkeyB@rs 28.8, password1 16.2 and "yes"; P200 Gr4v1ty#7 24.3, bluemoon
   37.6, kettle orbit maple 38.8, the six words 77.5 (about 700,000 years; 701,300 computed). Also Kettle Orbit Maple
   44.1, kettle-orbit-maple 41.1, Password123! 28.9, P@ssw0rd 15.9, Tr0ub4dor&3 24.3, xK9#mQ2$vL 65.7 (no pattern).
   But `Sec.pattern` gives up (returns null) on a letter run whose capitals don't follow word case, so a word password
   with a capital, a year and ! still reads as random, and the screen then says **"no words or pattern found"**, which
   vouches for it (frame `d1/02-strength.png`):
   - ILoveMyDog2008!: 98.5 bits, "about 1.5 trillion years", no warning ("ILove" is neither lower, Title nor CAPS).
   - IHateMath1!: 72.3 bits, past the 70 tick, about 18,000 years. NYKnicks2026: 71.5. ILoveYou123: 65.5 (iloveyou
     is on the list of 20 itself). LOLpassword: 62.7.
   - Repeats are never seen: zzzzzzzzzzzzzzzzzzzz 94.0 bits, 11111111111111111111 66.4, Ab1!Ab1!Ab1! 78.8.
   This is the round 1 blocker's own lesson (a capital, a year or ! makes a word password safe), on input a 9-12
   student types early in the Toolbox, and REFINE says a meter that misleads when its assumption doesn't hold is a
   blocker. docs/families/security.md (Sec.pattern) also claims "a random run can be under-rated, never a pattern
   over-rated", which these cases disprove. Narrow fix: in `pattern()`, also split a letter run before a capital that
   starts a Title-case word (`(?<=[A-Z])(?=[A-Z][a-z])`: I+Love, NY+Knicks) and let a short all-caps run count as
   letters (or a word when word-like), so LOL+password parses; rate a repeated unit (zzzz, 1111, Ab1! three times) by
   the unit plus a few bits; and when nothing is found say something like "no pattern this meter knows" (it knows
   only some), not "no words or pattern found". Re-check the P100 and P200 values after, and the doc's claim. P200's
   flag cannot leak: it prints only for the exact six-word candidate in P200 (IHateMath1! there prints "not one of
   the four choices").
2. **Tradeoff patches: PASS.** All twelve questions state the constraint; each pick shows its cost and gain; the right
   one turns on the constraint (P300: keys are strongest but the budget says no; L300: keys are right because "most
   reliably" is the ask); patched tiles show "Traded: ...". At least two options on every tile are reasonable; a few
   third options stay weak on purpose (Base64 twice, reply to the email) and say why.
3. **Give-aways: PASS.** No flag names its fix. The right choice sits first, second and third four times each; it is
   the longest on 4 of 12; the length spread is 1 to 9 characters (measured in Python). S100 line 8 is gone.
4. **Guessing costs: PASS; the evidence tap is not needed.** A wrong flag, wrong Check lines or a wrong full L300
   order each take a quarter, floor a quarter, said before the first try ("A wrong flag takes 75 points off this
   tile."), in the board's scoring line and in the points pill; cross-tile flags cost too; wrong tries survive a
   reload (S300 two wrong -> 150, P100 one wrong -> 75, S200 hint plus one wrong -> 50; score 275 after the reload).
   Expected score from blind guessing (exact, without replacement) against the Hint (half) and reading (full):
   S300 two domains 262.5 vs Hint 150; S200 ten times 80 vs 100; P100 and L100 six accounts 50 vs 50; L200 five
   accounts 110 vs 100; S100 any pair 38.8 (caller lines only 52.8) vs 50; L300 sorting the three timed cards, then
   guessing, 97.5 (120 with R before A) vs 150. Guessing never beats reading anywhere. It beats the Hint only on S300,
   and by a hair on L200 and S100. On S300 the two candidates are the two sender addresses, so to type either the
   student has already compared them, which is the skill; an evidence tap would add a step and teach nothing new.
5. P200 choice and reason: PASS ("Let passphrases run to 64 characters or more"; NIST: allow 64 or more, 15 alone).
6. L300 reason: PASS (the chain stops at A; a passkey would stop R too).
7. Answer key out of notes.md: PASS (no flag strings in notes; handoff.md holds the key).
8. Result in view after a tap: PASS. P200's printed flag ends at 720 of 720 at 1280x720, 425 of 425 at 680x425, 500
   of 500 at 800x500, 900 of 900 at 760x900, 812 of 812 at 375; C200 Text out 377 to 425 at 680x425, 656 to 720 at
   1280x720, 748 to 812 at 375; "Copied into Strength." and "Copied into Shift." show.
9. L300 payoff: PASS. The spell line is at 241 of 768 (334 at 375); cards tagged "1: T" to "5: E"; a wrong order says
   "That is not the order it happened. This tile is now worth 225." and shows no letters.
10. P300 details: PASS. The details box wraps inside the visible scroller at 680x425 (box 19 to 409 in 11 to 419),
    800x500, 1366x768 and 375 (23 to 350 in 15 to 360); "flag{code_denied}" is whole; the right edge fades and
    "Swipe the table sideways" shows on narrow stages, not at 1366.
11. Flip: PASS (`tile st-flag flip` and one running `flip` animation after Back, Motion on).
12 to 27: PASS. 12 offline-attack line; 13 AES with a key manager; 14 ethics line on the board; 15 times in words
    ("about 1.5 trillion years"); 16 the flag and patched lines name the control; 17 w-chal on the first open
    challenge; 18 the panel widens at 1920 (about 560 px); 19 the second step column starts in view at 375; 20 the
    board ends at 762 of 812 at 375; 21 a log scrolls in its own card when there is room (1000x625: max-height 361 px,
    the column names stay at the card top while rows scroll), and at 680x425, with under 150 px of room, the page card
    scrolls instead (by design); 22 no justPatched in storage; 23 header on one row at 760; 24 the stretched gray band
    is gone (each email keeps its own short foot strip, engine styling); 25 "70 bits" and "128" labels; 26 engine
    comments, tags kept in a map, COMMON wording in engine and doc; 27 no host.html in the tool folder.
28. Nits: PASS as listed.

##### Regressions and new findings

- None in function: all twelve flags open on their own tile in the promised forms (`flag{ bkoh }`,
  `BILLING@birchline-billing.example`, `flag{DISPATCH_password}`, `flag{trace}`); decodes recomputed (Base64, shift
  7, LANTERN).
- data-defenders with the changed engine: a scratch copy bundled twice, against `git show HEAD:kit/security.js` and
  against the working engine (DD's real files untouched). Hall, rooms C, I, A, X and puzzles c2 and i2 at 1366x768
  and 680x425: all 14 frame pairs pixel-identical (PIL difference bbox None), console clean; `body.innerHTML` differs
  by the same 8,424 characters in every state (the inlined engine text).
- Voice (held clicks 2 s apart, Sound and Motion on): w-chal spoken once, then silent (heard) on the next tile;
  notyet spoken once over five wrong flags (two dropped for newer, then silent); flag 1 of 1; patched 1 of 1; w-board
  on Back. The twelfth patch says `all`, not `patched`; Back 2.5 s later cut it and it played again whole on the
  board (by design: a dropped `all` comes back once). C200 with five wrong flags and a first-try patch scores 100.
- nit (general): C200's tile title is "Only 26 keys" while its reason and Traded line say "only 25 real keys".
- polish (general): at 375 the Strength readouts sit in a narrow right column, so "lower 26 + symbol (and space) 33 =
  59" wraps over four lines (`d4/h-p200.png`). Stack label over value below about 420 px.

##### Gate

1. Done when: 1 and 3 to 8 pass; 2 passes as written for the spec's rows, but the meter it describes still misleads
(item 1). 2. Codes taught: yes (patch tradeoffs). 3. Solo defaults: yes. 4. Sensitivity: not needed (rule 5 does not
apply). 5. Open: item 1 (blocker). 6. Bundle 167 KB, one file, no console errors, no network requests. 7. Voice counts
right. **ROUND 2, item 1 only.** It is narrow (one function in kit/security.js, one phrase in the Strength readout,
one sentence in the family doc); the integrator may fix it and send this check back.

##### Audit pilot

`python scripts/audit_tool.py capture-the-flag <scratch>/audit --port 9950`: 3 leads.
- Wrong: 760x900 "h1 clipped": the subtitle is hidden by design at 561 to 999 px wide; the title shows whole.
- Confirmed but fine: at 375, Clear progress (top 1001) and most of the board hint sit below the fold; the twelve
  tiles fill the phone window and are the next control, and the hint's first line shows at the bottom.
- Its walk matched mine: every tile's first click spoke w-chal, Toolbox w-toolbox, Read the hint, Sound nothing; the
  five held clicks were clean.
- It missed: the meter misreading common inputs (item 1, a teaching check), the guessing economics (item 4), every
  state past one click (P300 details wrap, the copied result in view, L300 tags and spell line, the flip, wrong-try
  costs and the reload), the data-defenders engine regression check, the twelfth-patch line, and the 375 Strength
  readout wrap.

#### Exit check, round 2

Same exit agent, scoped (REFINE, Rounds): item 1, the C200 nit and the 375 Strength polish, then a short
no-regression look at the Toolbox frames and voice they touch. Rebundled with `CURIO_DRAFT=1` (170 KB). Driven with
`scripts/drive.py` (port 9953, own profile) and my own iframe host from scratch (port 9954, stopped after); no
host.html in the tool folder. Strength numbers recomputed with the engine's pure block in Node and read back from the
page.

##### Item 1: still OPEN (blocker, family:security), narrower again

What round 1's exit check asked for is in, and works:
- Splits: ILoveMyDog2008! 57.6 (I + Love + My + Dog + 2008 + !; was 98.5), IHateMath1! 41.9 (was 72.3), NYKnicks2026
  33.0, LOLpassword 26.8 (LOL + password), ILoveYou123 43.5. All show the pattern warning.
- Repeats rated by the unit: twenty z's 10.0, twenty 1s 8.6, Ab1!Ab1!Ab1! 28.9, !!!!!!!!!!!!!!!! 10.0,
  2026202620262026 16.3, letmeinletmein 34.9; a random unit typed twice (xK9#mQ2$vL twice) 67.7, fair.
- Wording: "no pattern this meter knows (it has no dictionary, so names and phrases can still be guessed sooner)".
- docs/families/security.md now says the model can over-rate a pattern it doesn't know; the false "never over-rated"
  claim is gone.
- Spec values hold: P100 36.8, 16.2 and "yes", 36.2, 38.8, 26.6, 28.8; P200 24.3, 37.6, 38.8, 77.5; the P200 flag
  prints "Rated 77.5 bits: flag{77_bits}" with "about 700,000 years" (375: flag at 792 to 812 of 812).
- Fresh tries that now read fairly: MyNameIsJake2009 58.3, TheQuickBrownFox! 60.7, CorrectHorseBatteryStaple 55.7,
  ILikePizzaAndTacos 61.4, S3cur1ty!2026 28.6, Pa55word!! 41.1, qwertyQWERTY1 23.3, HappyBirthday2010 35.5,
  PSG2026Mbappe! 43.7, DONTHACKME2026 34.5, JakeJakeJake2009 49.4, Mississippi2026! 39.5.

Still over-rated, found with fresh adversarial input:
- **The same word typed six times passes as six random words.** "password password password password password
  password" reads "77.5 (6 random words from a list of 7,776)", about 700,000 years, past the 70 tick, though
  password is on the list of 20 (frame `d11/tb-1366-1.png`). "dog dog dog dog dog dog" and "summer summer ..." read
  the same. `strength()` takes the words path for any lowercase words split by spaces and never calls `pattern()`, so
  the new whole-password repeat check never runs. The screen states something false ("random words"), on input a
  student trying to beat the meter types early.
- **Alphabet and cross-row sequences.** abcdefghijklmnop 75.2 bits, about 140,000 years (lowercase letters with no
  capital or digit give no pattern signal, and the alphabet is not in RUNS); abcdefghijklmnopqrstuvwxyz 122.2;
  zyxwvutsrqponmlk 75.2; qwertyuiopasdfghjkl 89.3 (a run across two keyboard rows is not one run);
  1234567890987654321 63.1 (up then down). These show "no pattern this meter knows", which is honest about the
  meter, but the bits and time still say very strong.

Narrow fix (kit/security.js only): in `strength()`, take the words path only when the words are all different (or
count each different word once, and let a repeated word fall through to `pattern()`'s repeat check); add
`abcdefghijklmnopqrstuvwxyz` to RUNS and let a letter or digit token that is not a run be split into runs where
possible (qwertyuiop + asdfghjkl, 1234567890 + 987654321), each run counting as a sign of a pattern. Re-check the P100
and P200 values and the doc's checked values after.

##### The other two

- C200 nit: PASS. The tile is "Only 25 keys" on the board and in the challenge title, matching its reason.
- 375 Strength readouts: PASS. Below the breakpoint each label sits over its value (`d11/h-tb-375.png`), no sideways
  scroll; 680x425 and 1920x1080 keep the two columns.

##### No regressions

- Toolbox Strength frames at 1366x768, 680x425 and 1920x1080 for six inputs, and 375: nothing clipped or
  overlapping, readouts and warnings as above, console clean.
- Voice (held clicks 2 s apart): Toolbox speaks w-toolbox, the Strength tab changes the hint without speaking, Read
  reads "Type a made-up password in the box...", Board speaks w-board. Nothing stale or repeated.
- data-defenders, bundled from a scratch copy against the changed engine: all 14 frames (hall, rooms C, I, A, X, c2,
  i2 at 1366x768 and 680x425) pixel-identical to the round 1 baseline built against `git show HEAD:kit/security.js`,
  console clean.

##### Gate

All gate points hold except 5: item 1 is still a blocker (a meter that misleads when its assumption fails). This is
round 2, so per REFINE (Rounds) the tool does not go on as is: the integrator either makes the narrow fix above itself
with an "Integrator fix" note, or brings it to Cory with this list.

#### Integrator fix (after exit round 2)
Item 1's two remaining gaps, fixed in kit/security.js by the integrator: `strength()` takes the words path only when
the words are all different (otherwise `pattern()` runs); `pattern()` rates one unit typed again with a separator as
the unit (a lowercase unit is one word) + 2.3 + log2(times) + 1; the alphabet joins RUNS; a stretch made only of runs
back to back counts as each run. Node: six "password"s 18.8, "dog" x6 18.8, abcdefghijklmnop 10.0, the alphabet 10.0,
qwertyuiopasdfghjkl 20.0, 1234567890987654321 20.0; P100 and P200 values unchanged (77.5 for the six different
words). docs/families/security.md updated. Sent back to the same exit agent for a re-check.

#### Exit re-check (integrator fix)

Same exit agent. Re-checked the two round 2 cases on screen (Toolbox Strength at 1366x768 after the rebundle), fresh
adversarial input in Node against the engine's pure block, the spec's values, and data-defenders.

- **Fixed, on screen:** six "password"s read "18.8 (pattern: password (word) + space (between words) + typed 6
  times)", less than a second; "dog" and "summer" six times 18.8; "Password Password Password" 18.8;
  password-password-password-password 18.2. abcdefghijklmnop 10.0 and the alphabet 10.0 (run); zyxwvutsrqponmlk 10.0;
  qwertyuiopasdfghjkl 20.0 (two runs); 1234567890987654321 20.0; mnbvcxzlkjhgfdsa 20.0; qwerty123456 20.0;
  abcd1234efgh 30.0. Round 1 and 2 fixes still hold (ILoveMyDog2008! 57.6, IHateMath1! 41.9, twenty z's 10.0,
  Ab1!Ab1!Ab1! 28.9).
- **Spec values hold:** P100 rows read back from the page 36.8, 16.2 and "yes", 36.2, 38.8, 26.6, 28.8 (only password1
  "yes"); P200 24.3, 37.6, 38.8, 77.5; the flag prints "Rated 77.5 bits: flag{77_bits}" with "about 700,000 years".
- **data-defenders:** a scratch copy bundled against the new engine; all 14 frames (hall, rooms C, I, A, X, c2, i2 at
  1366x768 and 680x425) pixel-identical to the baseline built on `git show HEAD:kit/security.js`; console clean.
- **Still over-rated (blocker, family:security):** words that repeat, but not as one clean unit, now leave the words
  path and go to `pattern()`, which charges every word in full (12.9 bits) plus the separator, so they rate *above* six
  different random words:
  - "kettle orbit maple kettle orbit maple" (P200's own phrase typed twice): 79.9 bits, past the 70 tick
    (frame `d13/tb-4.png`). In P200 that is the cheap way to reach the target, and the meter backs it.
  - "dog dog dog dog dog cat" 79.9 (`d13/tb-3.png`); "the the the cat cat cat" 79.9; "red green blue red green blue"
    79.9; "jake jake jake jake jake jake 2009" 87.5.
  Before the fix these read 77.5 through the words path; now they read higher. Narrow fix in `pattern()`: a word
  already used earlier in the password costs about log2(words so far) + 1 instead of a full word (a guesser tries
  repeats first), and a multi-word unit typed again with separators (kettle orbit maple twice) goes to the unit-repeat
  rule. Then re-check these five, the six "password"s and P200's 77.5.
- Minor, not blocking: "aaa bbb ccc ddd eee fff" still reads as six random words (77.5).

**Verdict: still ROUND 2**, item 1 only, this one case (repeated words inside a longer password). Nothing else open.

#### Integrator fix 2 and close
The re-check's last case (words repeated inside a longer password rated as new words) fixed in `pattern()`: a word
used again costs log2(the words so far) + 1. Node, the same function the page calls: kettle orbit maple twice 48.9,
red green blue twice 48.9, dog x5 cat 32.2, the x3 cat x3 34.2, jake x6 2009 27.9; six "password"s 18.8; P100 36.8,
16.2, 36.2, 38.8, 26.6, 28.8 and P200 24.3, 37.6, 38.8, 77.5 (the flag) unchanged. The exit agent had already
confirmed the screen plumbing for these numbers, so the integrator closed it here instead of a fourth look.
Known, not done: six different nonsense words such as "aaa bbb ccc ddd eee fff" still rate as six random list words
(77.5); the meter has no dictionary and says so on screen.

<!-- end part -->

<!-- part: refine/craft.md -->

### capture-the-flag: Craft lens (Refine round 1)

Cold read of spec.md, src.html, notes.md, handoff.md, art/prompts.json, voice/lines.json, kit/security.js (and its
diff against git HEAD) and docs/families/security.md. Bundled with `CURIO_DRAFT=1 python scripts/bundle_tool.py
capture-the-flag` (147 KB). Driven with `scripts/drive.py` in muted headless Chrome. I used my own profile, port 9960
and `--host 9961` for 375 wide. About 170 frames and checks; the frames are in the lens-ctf-craft2 scratch folder.

Counts: blockers 0, should fix 2 (general 1, family 1), polish 1 (family 1), nits 7 (general 4: items 4, 8, 9, 10;
family 3: items 5, 6, 7).

#### Findings

##### Should fix

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

##### Polish

3. **The log's column names scroll away.** `.sec-table th` is `position: sticky; top: 0`, but the box that scrolls
   up and down is the tool's `.artwrap`, not `.sec-scroll`. At 680x425, scrolling down to the open 03:02 row hides
   the time / device / second step headers (`func/p300det-680.png`). Better: give `.sec-scroll` a max height inside
   the challenge, so the header sticks inside the card, or make the header stick to the outer scroller.
   **family:security**

##### Nits

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

#### Contract
- One file, 147 KB. There are no `src=` or `href=` URLs. The only URLs are an SVG namespace and the engine's
  `https://x.test` example comment. `fetch`, XHR and `import()` are absent. `performance.getEntriesByType('resource')`
  is empty after opening all twelve tiles and the Toolbox (`fin/net`).
- Console: clean in every shot at every size. The one 404 was the host page's favicon at 375.
- The kit is used, not re-implemented: `Sec.world`, `Sec.artifact` (log, note, file, call, email), `Sec.pure`
  (strength, guessSeconds, caesar, vigenere, b64, lock, hostOf) and `Curio.voice`. The note-lines helper builds a
  second note artifact to get engine spots. That is unusual but uses the engine's own spot handling.
- Guard: `Sec.safeDomain('evil.com')` is false. `world.ok` is true. larkspur.example, birchline.example and
  birchline-billing.example all pass.

#### Engine check (kit/security.js against docs/families/security.md, line by line)
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

#### Access
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

#### Layout (STANDARDS sizes; `sizes/`, `host/`)
I checked the Board, the Toolbox, eleven tiles, P300 with details open and the patch card. The sizes were 680x425,
800x500, 1000x625, 1280x720, 1366x768, 1920x1080, 760x1000, and 375x812 inside the iframe host.
- No sideways page scroll at any size, and no header overflow.
- Flag and Submit are in view in every challenge at every size: y 166 to 210 at 680x425, 178 to 222 wide, 927 to 971
  at 760x1000 and 739 to 783 at 375.
- No clipped labels by scan.
- Wide logs: P300 scrolls sideways inside its card at 680, 800 and 375 (should fix 1). The other logs (P100, S200,
  L100, L200) fit at every size.
- The 375 board is two bands of two categories with row labels. The 375 Toolbox fits with a 124 px wheel.

#### Lines and voice
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

<!-- end part -->

<!-- part: refine/play.md -->

### capture-the-flag: Play lens (Refine round 1)

Cold read of spec.md, src.html, notes.md, handoff.md, voice/lines.json; bundled with `CURIO_DRAFT=1` (147 KB). Driven
in my own muted headless Chrome (port 9950, own profile) with real held clicks, real keys and `Input.insertText`
typing; 375 wide through an iframe host page served on port 9951 (`host.html?w=375&h=812` and `h=667`). Frames and
scripts in my scratch folder `lens-ctf-play2/out` (about 150 frames). Console clean in every run, no network requests
(the only 404 was the host page's favicon).

Counts: blockers 0, should fix 3 (general 2, family 1), polish 5, nit 4.

#### What works

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

#### Voice check (held clicks, Sound on, Motion on; browser voice)

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

#### Findings

##### Should fix

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

##### Polish

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

##### Nit

1. At 760 wide the header wraps Read onto its own row (`C200-760x900`).
2. `justPatched` is written into localStorage with each tile (`save()` stores the whole tile object); it is ignored on
   load, so harmless, but the stored record is meant to be only state, hint and patch tries.
3. S300: the shorter email card has an empty gray band at its foot where the two cards are stretched to one height
   (`S300-1920x1080`).
4. The Strength bar has a 70 tick but no unit or end label; "bits" beside it would read better.

#### Frames looked at

Board, Toolbox, Toolbox Strength, P300, S100, L300, S300, C200 (open and copied), P200, P100 (patch card and
patched) and the board after one patch, at all seven desktop sizes; the twelve challenges at 375x812 and 375x667
plus C200 copy, shift, flag, wrong patch and patched; keyboard frames (`kb-*`); voice run frames (`v-C200-5miss`,
`v-all-chal`, `v-all-board`); Motion off (`calm-C300-3miss`, `calm-C200`); reload and Clear progress frames; the
feel run (`f-P200-pw0..3`, `f-P300-details`, `f-P300-hint`, `f-board-hinttag`, `f-L300-wrongorder`).

<!-- end part -->

<!-- part: refine/teaching.md -->

### capture-the-flag: Teaching lens (Refine round 1)

Cold read of spec.md, src.html, notes.md, handoff.md, tool.draft.json, art/prompts.json, voice/lines.json, plus
kit/security.js (strength, COMMON, caesar, vigenere, b64, lock). Bundled with `CURIO_DRAFT=1` (147 KB). Driven with
`scripts/drive.py` on ports 9901 to 9903, own profiles in my scratch folder (removed after). Every number recomputed in
Python (`lens-ctf-teaching/v.py`) and read back from the live Strength readout (`strength.json`).

Counts: blockers 2 (general 1, family 1), should fix 5 (general 4, family 1), polish 4, nit 3.

#### What checks out

- **Encodings and ciphers.** Base64 `ZmxhZ3tub3RfYV9sb2NrfQ==` decodes to `flag{not_a_lock}`; `mshn{vusf_26_rlfz}`
  shifted back 7 (forward 19) is `flag{only_26_keys}`; Vigenere with LANTERN decodes `qlnz{ovra_krrw_rclrg}` to
  `flag{keep_keys_apart}` and encodes it back. The kit's `caesar`, `vigenere` (key advances only on letters) and `b64`
  give the same results in the page.
- **Strength math.** bits = length x log2(pool), wordBits = words x log2(7776) = 12.92 per word, time = 2^bits / 1e10.
  All four P200 values match the spec: Gr4v1ty#7 59.1 bits, about 2 years; bluemoon 37.6, about 21 seconds; kettle orbit
  maple 105.9 by letters, 38.8 by words, about 47 seconds; the six words 205.9 / 77.5, about 700,000 years
  (700,488 computed). The flag prints only for the six-word candidate, only inside P200.
- **The common-list line** ("Guessers try the common list first, so this one falls almost at once, whatever the time
  above says") is accurate: list-first (dictionary) guessing is how cracking works, and password1 is in the NCSC 2019
  list (it is in its top ten). The 20 entries in `COMMON` are all well-known NCSC list entries. Of the P100 rows only
  password1 reads "yes". The line fixes a real problem: without it password1 reads "about 2.8 hours".
- **Every flag reproduces** on a cleared board: all twelve open with their Content flags in the forms promised
  (`FLAG{six_random_words}`, ` second_step_held `, `flag{ bkoh }`, `07:52`, `billing@birchline-billing.example`,
  `flag{HWU}`). A flag on the wrong tile is refused (`hwu` on P100, `bkoh` on L200). S100 opens for 2+5 and 7+5, not
  2+7. L300 shows TRACE only for T, R, A, C, E. The P300 03:02 details read "Second step denied by the account owner.
  flag{second_step_held}". Score reaches 3,000; a hint plus a wrong first patch on P300 scores 150. Saved data holds
  tile state, hint use and patch tries only, no typed text.
- **Other facts.** NIST 800-63B-4: blocklist check, no composition rules, no forced periodic changes (the source says
  SHALL NOT), salted hashes, rate limiting: all as stated. Base64 has no key (RFC 4648). The BEC, pretext-call, MFA-code
  theft and tailgating scenarios are accurate and match CISA and IC3 guidance. Log data is internally consistent
  (gnair: five failures then a success from a new device; evance: one typo; hwu: 312 + 140 files at 01:47 to 01:49;
  S200: only 07:52 has 2 through on one badge).
- **No unsafe or real-world-misuse content.** Reserved `.example` domains, no real brands, no attack tools, and the
  Strength note says not to type a real password. Nothing cultural, Native or hard history: no sensitivity referral.
- Language is plain and right for 9-12.

#### Blockers

1. **The Strength meter teaches that a pattern password is strong, on the tile's own artifact.**
   Where: src.html:748-758 (Strength readout), src.html:525 (P100 rows), kit/security.js:49-61. family:security.
   What: "bits by letters" assumes every character is random, and the word check only fires on all-lowercase words split
   by single spaces. The P100 hint tells the student to run every row through the meter, and they see:
   - Winter2026!: 72.3 bits, "about 18,000 years", the bar past the 70 tick, common list "no". The same tile's patch C
     names Winter2026! as the predictable pattern people pick.
   - Tidepool-Lantern-88: "about 120,000,000,000 billion years", while dfinch's violet harbor bicycle, the same
     two-or-three-words build, reads "about 47 seconds".
   - In Toolbox, kettle orbit maple reads 47 seconds, but Kettle Orbit Maple reads "about 170,000,000 billion years" and
     kettle-orbit-maple "about 240,000 billion years". m0nkeyB@rs reads about 190 years; password1! about 7.8 years
     and "no" (P100's patch B says password1! would pass, which is right, but the meter calls it strong).
   The lesson a student takes is the unsafe habit: add a capital, a hyphen, a year or a ! and a word password becomes
   uncrackable. Real guessers apply exactly these rules (capitalize, swap letters for symbols, append a year or !).
   How seen: Strength readouts read back from the page (`strength.json`), recomputed in Python.
   Better: on screen, say plainly what "bits by letters" assumes ("if every character were picked at random"), and
   either widen the word and pattern check (any case, hyphens or digits between words, a season or year, common
   letter-for-symbol swaps; then "bits used" takes the lower count) or add a warning line like the common-list one for
   these patterns. Also say the list is a short sample ("On a list of 20 very common passwords"), so "no" does not read
   as "safe". Check P200's four values still match after the change.

2. **The tradeoff codes are not taught by anything the student does (rule 2).**
   Where: every patch card, src.html:446-517; notes.md:22. general.
   What: the module carries HS-SYS-SE-31 to 33; the spec's crosswalk names 3A-NI-07 (tradeoffs between usability and
   security) and 3A-NI-08 (tradeoffs of cybersecurity recommendations). The patch step is the only place a student
   recommends a fix, and on all twelve tiles it is one sensible fix against two strawmen ("A bigger mailbox", "Allow
   unlimited tries", "Give everyone every share", "Write it in capitals", "Pay half to the new account"). No choice
   carries a cost, and no reason mentions one. Tradeoffs appear only in a teacher discussion question ("Each patch has
   a cost..."), which a solo student never sees (rule 4). (The 2026 code text is not in the repo, only the ids in
   data/standards/csta-2026-ids.txt, so I judged against the spec's 2017 crosswalk.)
   How seen: read all 36 choices and reasons.
   Better: make the patch a real choice between defensible fixes with a stated cost, so the student weighs usability
   against security. Examples: L100 lock the account after 5 tries (stops guessing, but lets an attacker lock real
   users out) vs slow down tries vs a second step; P300 a texted code vs an app prompt vs a security key (cost, phishing
   resistance, a lost phone); L200 remove Finance access vs alert only vs review monthly; S200 a turnstile vs a guard vs
   training. Each reason names what the fix costs as well as what it stops. Or, if the integrator decides the
   tradeoff codes cannot be taught well here, write down their move to another tool.

#### Should fix

3. **The flags and the option length give the patch away.** Where: TILES flags and patch choices, src.html:446-517.
   general.
   What: on 7 of 12 tiles the flag just typed names the right patch: six_random_words / "Long passphrases",
   second_step_held / "Turn on a second step", not_a_lock / "Base64 is encoding, not encryption", only_26_keys / "a
   shift cipher has only 26 keys", keep_keys_apart / "Keep keys apart", call_back / "call the help desk" (and Dana's own
   line 8 says "I'll call the help desk back first"). And on all 12 tiles the right choice is the longest, most specific
   one (P300 44 vs 31 and 40 characters; C100 94 vs 15 and 20; L300 80 vs 38 and 16). The +50 first-try bonus then
   rewards test-taking, not judgment. How seen: listed flags against choices; measured choice lengths in Python.
   Better: flag strings that name the finding, not the fix (for example `flag{plain_base64}`, `flag{shift_7}`,
   `flag{key_in_readme}`, `flag{code_denied}`), drop or move Dana's line 8, and write the choices to similar length and
   specificity (this goes with blocker 2).

4. **Many tiles can be solved by trying every option, at no cost.** Where: submit(), src.html:1004-1028; s100Check,
   l300Render. general.
   What: a wrong flag costs nothing (only the Hint glow after 3). P100 has six account names to type in turn, L100
   seven accounts, L200 five, S200 ten times, S300 two domains; S100 is 28 pairs with "Not these two." feedback; in
   L300 four of five cards carry times, so sorting them leaves five places for R. A student can collect most flags
   without reading the evidence. How seen: code read; S100 and L300 driven (2+7 refused, a wrong order refused, retries
   free).
   Better: one of: a small visible cost per wrong flag ("Wrong flags take 10 points off this tile"), or flags that need
   the evidence as well as the name (L100 `gnair_5` for the failure count, L200 `hwu_finance`, S200 the badge
   `b-2011`), and remove the time from one more L300 card (or ask for the step where the chain could first be broken).

5. **"Long passphrases: at least 64 characters" reads as a 64-character minimum.** Where: P200 patch A, src.html:456.
   general.
   What: NIST 800-63B-4 says verifiers SHOULD permit a maximum length of at least 64 characters (and require a minimum
   of 15 for a password used alone). "At least 64 characters" in the option reads as "passwords must be 64 or longer",
   which is not NIST's rule, and the six-word passphrase the tile just rewarded is 35 characters, so it would fail its
   own patch. How seen: read against the source.
   Better: "Allow long passphrases: up to 64 characters or more, spaces allowed" (and the reason could add NIST's
   15-character minimum).

6. **L300's right reason is not quite right: a security key breaks the chain at A, not at R.** Where: src.html:516.
   general.
   What: with a security key added to a password, jlam can still type the password into the fake page (R happens); the
   stolen password just cannot sign in from the attacker's device, so the chain stops at A. Only a passwordless key
   (a passkey) removes R itself. A teacher who knows the topic will catch this. How seen: read against CISA's
   phishing-resistant MFA fact sheet.
   Better: "The stolen password is useless without the key, so the sign-in at A fails" (or say passkey and keep R).

7. **The answer key is public on the tool page.** Where: notes.md:28; site/templates/tool.html:41-43 (Teacher notes is
   the default tab, open under the preview). family:security.
   What: all twelve flags with how to get them sit in the open notes, one scroll below "Play full screen", where a
   student opening the tool finds them. In a capture-the-flag game that is the whole answer set.
   How seen: read the template.
   Better: put the flag list in a collapsed "Answer key" (a `<details>` in notes, closed by default), or keep only how
   each tile is solved and leave the flag strings out.

#### Polish

8. **Say what the guess rate models.** Strength's "10 billion guesses a second" is an offline rate (stolen hashes on a
   fast hash), while L100 is online guessing that rate limits stop. One line under the time ("if the stored hashes were
   stolen; a sign-in page that slows tries is far slower") ties P100's salted-hash note, the meter and L100 together.
   general.
9. **C300's right patch keeps the Vigenere cipher.** The fix keeps the key apart, but the plan is still locked with a
   cipher a student can attack: the known `flag{` start already gives the first four key letters (q-f = L, l-l = A,
   n-a = N, z-g = T). The reason could add "and use a modern cipher such as AES", or a talk question could point out the
   known-start attack (a nice next step for strong students). general.
10. **Add a one-line ethics frame.** Real CTFs open with "only test systems you own or have written permission to
    test". One line in the Board how-it-works or in notes ("Larkspur is made up so you can practice; trying this on a
    real system without permission is against the law") makes the norm explicit for a 9-12 security tool. general.
11. **Big times read badly.** "about 120,000,000,000 billion years" and "about 170,000,000 billion years" (fmtTime,
    src.html:735-745): cap at "more than a trillion years" or use powers of ten. general.

#### Nits

12. "a shift cipher has only 26 keys" (C200): 25 change the text (shift 0 leaves it as is). Fine as a teaching
    round number; "only 25 real keys" is exact. general.
13. A space counts in the 33-symbol pool, so "kettle orbit maple" shows "lower 26 + symbol 33 = 59". Correct for the
    model but puzzling; "symbol (and space) 33" would say why. family:security.
14. Test API only: `__tool.open()` threw `Cannot set properties of null (setting 'hidden')` in renderPatch after a
    sequence that opened a tile from another tile's challenge without toBoard. Real clicks (open, flag, Back, reopen)
    are fine, so this is not a user bug; noted for whoever scripts the exit check. general.

#### Done when (spec)

1. Pass: every flag in every promised form, own tile only; the three decodes reproduce.
2. Pass as written (P200 values and flag; common list yes only for password1 in P100). See blocker 1 for what the same
   meter says about the other P100 rows.
3. Pass: P300 03:02 details, S100 2+5 and 7+5 (2+7 refused), L300 TRACE only in order.
4. Pass: hint halves, +50 only first try, 3,000 maximum; state icons and words present.
5. Pass: progress survived reloads across runs; no typed text stored. (Clear progress driven through the API only.)
6 to 8: sizes, keyboard, voice, console and network are the Play and Craft lenses' checks; the console was clean in
   every shot I drove (one exception was from my own test-API sequence, item 14).

<!-- end part -->

## Handoff

<!-- part: handoff.md -->

### capture-the-flag: handoff (Build, batch BR; Refine round 1)

#### What it is

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

#### Answer key (teacher copy; deliberately not in notes.md, which the public page shows)

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

#### Refine round 1: what changed (refine.md item numbers)

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

#### Exit check round 2

1. `Sec.pattern` no longer skips runs with odd capitals or repeats. Letter runs split before a Title-case word after a capital run (I + Love, NY + Knicks); a capital run of 3+ with a vowel keeps its letters (LOL + password); a capital run of up to 4 that is not word-like counts as letters; one character 3+ times in a row is a repeat; a whole password that is one unit typed again is rated as the unit plus log2(times) + 1. Empty result now reads "no pattern this meter knows (it has no dictionary, so names and phrases can still be guessed sooner)". The family doc no longer says "never over-rated". Recomputed (used bits, by characters in brackets): ILoveMyDog2008! 57.6 (98.5), IHateMath1! 41.9 (72.3), NYKnicks2026 33.0 (71.5), ILoveYou123 43.5 (65.5), LOLpassword 26.8 (62.7), twenty z's 10.0 (94.0), Ab1!Ab1!Ab1! 28.9 (78.8). Spec values unchanged: P100 rows 36.8, 36.2, 38.8, 26.6, 28.8 (password1 16.2); P200 24.3, 37.6, 38.8, 77.5 (677,000 years, shown as about 700,000). data-defenders scratch bundle: 4 frames pixel-identical again.
2. C200's title is now "Only 25 keys", matching its reason and Traded line.
3. Strength readouts stack (name over value) in a Toolbox narrower than 380 px, so at 375 each value has the full width.

#### Engine changes in kit/security.js (all backward compatible)

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

#### Checked in Refine round 1 (drive.py, ports 9861 to 9863, own profiles in scratch)

- Function run at 1366x768: every flag opens only its own tile; a cross-tile flag is refused and costs (P100 to 75); decodes match; L300 wrong order costs, right order shows TRACE with "1: T" tags; P200 prints "Rated 77.5 bits: flag{77_bits}"; Strength texts as above; the flip plays; the saved JSON holds no justPatched; a reload keeps wrong counts; console clean.
- Size audit at 680x425, 800x500, 1000x625, 1280x720, 1366x768, 1920x1080 and 760x900 on the board, P300 (details open), P200 and C200 (after a copy), L300 (ordered), S100, S300, L100, a patch card and the Toolbox: clean (44 px targets, no clipping, no overlap, no page sideways scroll). P300's details box sits inside the visible scroller at every size; the copied result, the L300 spell line and Toolbox Text out end inside the window at every size.
- 375x812 through `--host` (every tile, Toolbox, a patch): clean. The board fits (last tile ends at 762 of 812, tiles 84 px); P300 shows the swipe line, fades at the right, and its open details (`flag{code_denied}`) wrap inside the visible card; after a tap the P200 flag (792-812) and C200 Text out (748-812) end inside the window; the L300 spell line is at 334.
- audit_tool.py: clean at every size and with Motion off; one held click per control and five held clicks at 2 s are clean. Three leads, answered: 760x900 "h1 clipped" is a false lead (h1 measures 180/180; the hidden subtitle's text is counted); at 375 the board hint and Clear progress sit below the board, which fills the phone window and is itself the next control.
- Bundled with `CURIO_DRAFT=1`.

#### Known gaps

- **Tiny searches cost but ask for no evidence (item 4).** S300 has 2 domains and S200 a handful of times; a wrong try costs a quarter (75 or 50 points), which makes sweeping a poor trade, but the tool does not ask students to tap the row or line that proves the answer. Adding evidence forms per tile was more change than the round allowed.
- **L300's order can still be found by trying orders,** now at a quarter of the tile per wrong full order.
- **The P200 flag prints only for the exact six-word candidate while P200 is open.**
- **No recorded voice yet** (draft build: the system voice stands in).

#### For Cory

- Nothing is committed. Files changed: `tools/capture-the-flag/` (src.html, bundle, spec.md, notes.md, handoff.md, voice/lines.json), `kit/security.js`, `docs/families/security.md`.
- The engine change touches every security tool. It is additive, and data-defenders is unchanged pixel for pixel.

<!-- end part -->

## Log

- 2026-11-25: refine.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/craft.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/play.md folded in (last changed 2026-10-28)
- 2026-11-25: refine/teaching.md folded in (last changed 2026-10-28)
- 2026-11-25: handoff.md folded in (last changed 2026-10-28)

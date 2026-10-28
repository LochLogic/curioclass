PASS
Counts: blockers 2 (general 1, family 1), should fix 9 (general 7, family 2), polish accepted 17

# capture-the-flag: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames and detail.
Checked and correct (T): all 12 flags reproduce, ciphers and Base64 match, all Strength math matches the spec, the
common-list line is accurate, NIST, CISA and business-email-scam claims hold, nothing teaches misuse. Engine changes
are backward compatible: data-defenders is pixel-identical on a scratch bundle (C). No rule-5 content.

## Blockers
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

## Should fix
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

## Polish accepted
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

## Settled calls
- The common-list line under Strength (builder asked for an OK): accepted by the integrator, checked accurate by T.
- C100's drawer opens on Shift, not Base64 (builder's change from the spec, so it doesn't give away the paid hint):
  accepted; update spec.md to match.

## Exit check, round 1

Fresh cold agent, 2026-10-28. Read REFINE (Exit check, Rounds), STANDARDS, BASELINE, the BUILD wave lessons, spec.md,
handoff.md (Refine round 1), the three lens files and this list. Bundled with `CURIO_DRAFT=1` (167 KB). Driven with
`scripts/drive.py` in my own muted headless Chrome (ports 9950 to 9954, own profiles, all in my scratch folder
`exit-ctf`); 375 wide through my own iframe host served from scratch (no host.html in the tool folder). Strength and
pattern numbers recomputed with the engine's pure block in Node and checked against the page's readouts. Console
clean in every shot; no resource requests (`performance.getEntriesByType('resource')` empty after all twelve tiles and
the Toolbox); `allLines()` 41 = voice/lines.json 41, word for word; no em dashes.

### Item by item

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

### Regressions and new findings

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

### Gate

1. Done when: 1 and 3 to 8 pass; 2 passes as written for the spec's rows, but the meter it describes still misleads
(item 1). 2. Codes taught: yes (patch tradeoffs). 3. Solo defaults: yes. 4. Sensitivity: not needed (rule 5 does not
apply). 5. Open: item 1 (blocker). 6. Bundle 167 KB, one file, no console errors, no network requests. 7. Voice counts
right. **ROUND 2, item 1 only.** It is narrow (one function in kit/security.js, one phrase in the Strength readout,
one sentence in the family doc); the integrator may fix it and send this check back.

### Audit pilot

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

## Exit check, round 2

Same exit agent, scoped (REFINE, Rounds): item 1, the C200 nit and the 375 Strength polish, then a short
no-regression look at the Toolbox frames and voice they touch. Rebundled with `CURIO_DRAFT=1` (170 KB). Driven with
`scripts/drive.py` (port 9953, own profile) and my own iframe host from scratch (port 9954, stopped after); no
host.html in the tool folder. Strength numbers recomputed with the engine's pure block in Node and read back from the
page.

### Item 1: still OPEN (blocker, family:security), narrower again

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

### The other two

- C200 nit: PASS. The tile is "Only 25 keys" on the board and in the challenge title, matching its reason.
- 375 Strength readouts: PASS. Below the breakpoint each label sits over its value (`d11/h-tb-375.png`), no sideways
  scroll; 680x425 and 1920x1080 keep the two columns.

### No regressions

- Toolbox Strength frames at 1366x768, 680x425 and 1920x1080 for six inputs, and 375: nothing clipped or
  overlapping, readouts and warnings as above, console clean.
- Voice (held clicks 2 s apart): Toolbox speaks w-toolbox, the Strength tab changes the hint without speaking, Read
  reads "Type a made-up password in the box...", Board speaks w-board. Nothing stale or repeated.
- data-defenders, bundled from a scratch copy against the changed engine: all 14 frames (hall, rooms C, I, A, X, c2,
  i2 at 1366x768 and 680x425) pixel-identical to the round 1 baseline built against `git show HEAD:kit/security.js`,
  console clean.

### Gate

All gate points hold except 5: item 1 is still a blocker (a meter that misleads when its assumption fails). This is
round 2, so per REFINE (Rounds) the tool does not go on as is: the integrator either makes the narrow fix above itself
with an "Integrator fix" note, or brings it to Cory with this list.

## Integrator fix (after exit round 2)
Item 1's two remaining gaps, fixed in kit/security.js by the integrator: `strength()` takes the words path only when
the words are all different (otherwise `pattern()` runs); `pattern()` rates one unit typed again with a separator as
the unit (a lowercase unit is one word) + 2.3 + log2(times) + 1; the alphabet joins RUNS; a stretch made only of runs
back to back counts as each run. Node: six "password"s 18.8, "dog" x6 18.8, abcdefghijklmnop 10.0, the alphabet 10.0,
qwertyuiopasdfghjkl 20.0, 1234567890987654321 20.0; P100 and P200 values unchanged (77.5 for the six different
words). docs/families/security.md updated. Sent back to the same exit agent for a re-check.

## Exit re-check (integrator fix)

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

## Integrator fix 2 and close
The re-check's last case (words repeated inside a longer password rated as new words) fixed in `pattern()`: a word
used again costs log2(the words so far) + 1. Node, the same function the page calls: kettle orbit maple twice 48.9,
red green blue twice 48.9, dog x5 cat 32.2, the x3 cat x3 34.2, jake x6 2009 27.9; six "password"s 18.8; P100 36.8,
16.2, 36.2, 38.8, 26.6, 28.8 and P200 24.3, 37.6, 38.8, 77.5 (the flag) unchanged. The exit agent had already
confirmed the screen plumbing for these numbers, so the integrator closed it here instead of a fourth look.
Known, not done: six different nonsense words such as "aaa bbb ccc ddd eee fff" still rate as six random list words
(77.5); the meter has no dictionary and says so on screen.

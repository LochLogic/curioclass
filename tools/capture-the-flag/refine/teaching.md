# capture-the-flag: Teaching lens (Refine round 1)

Cold read of spec.md, src.html, notes.md, handoff.md, tool.draft.json, art/prompts.json, voice/lines.json, plus
kit/security.js (strength, COMMON, caesar, vigenere, b64, lock). Bundled with `CURIO_DRAFT=1` (147 KB). Driven with
`scripts/drive.py` on ports 9901 to 9903, own profiles in my scratch folder (removed after). Every number recomputed in
Python (`lens-ctf-teaching/v.py`) and read back from the live Strength readout (`strength.json`).

Counts: blockers 2 (general 1, family 1), should fix 5 (general 4, family 1), polish 4, nit 3.

## What checks out

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

## Blockers

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

## Should fix

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

## Polish

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

## Nits

12. "a shift cipher has only 26 keys" (C200): 25 change the text (shift 0 leaves it as is). Fine as a teaching
    round number; "only 25 real keys" is exact. general.
13. A space counts in the 33-symbol pool, so "kettle orbit maple" shows "lower 26 + symbol 33 = 59". Correct for the
    model but puzzling; "symbol (and space) 33" would say why. family:security.
14. Test API only: `__tool.open()` threw `Cannot set properties of null (setting 'hidden')` in renderPatch after a
    sequence that opened a tile from another tile's challenge without toBoard. Real clicks (open, flag, Back, reopen)
    are fine, so this is not a user bug; noted for whoever scripts the exit check. general.

## Done when (spec)

1. Pass: every flag in every promised form, own tile only; the three decodes reproduce.
2. Pass as written (P200 values and flag; common list yes only for password1 in P100). See blocker 1 for what the same
   meter says about the other P100 rows.
3. Pass: P300 03:02 details, S100 2+5 and 7+5 (2+7 refused), L300 TRACE only in order.
4. Pass: hint halves, +50 only first try, 3,000 maximum; state icons and words present.
5. Pass: progress survived reloads across runs; no typed text stored. (Clear progress driven through the API only.)
6 to 8: sizes, keyboard, voice, console and network are the Play and Craft lenses' checks; the console was clean in
   every shot I drove (one exception was from my own test-API sequence, item 14).

PASS (re-check 2026-10-29: all 3 should-fix items and polish items 4 and 5 fixed and confirmed; no regressions)

Round 1 verdict, kept for the record: (1) the Snow Town welcome holds the voice queue: its second line plays after its moment, and result lines land up to 13 s late; (2) a level intro keeps talking over the walk after Go, and the bump line comes about 5 s after the bump; (3) the welcome take reads "Welcome to Snow Town, Pip. The penguin carries the mail."

# snowy-mail-route: Final look (round 1, 2026-10-29)

Cold Final look with the real assets: 47 recorded clips (local Qwen3-TTS, voice/*.mp3), pictures drawn in code (no art
files). I read refine.md and handoff.md first. Everything settled there still holds unless listed below.
Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py snowy-mail-route`, 963 KB, and the bundler reported no missing
recordings. Muted headless Chrome on ports 9211 and 9212. A scratch iframe host served the 375 run on port 8812, so
nothing was written to the tool folder. Everything is in `S:/CurioClass-codex-scratch/final/snowy-mail-route/`:
- `audit/`: the fresh audit_tool.py run (127 leads)
- `a/`: 1366x768 with Motion on, and 680x425 with Motion off
- `b/`: 800x500, 1000x625, 1280x720, 1920x1080 and 760x900
- `c/out/`: 375x812 through the host
- `v/`: the voice runs, with full logs (`*.json`), timestamps on every clip and `show.py`
- `asr.json`: a Whisper transcript of every clip

Counts: blockers 0, should fix 3 (general 3, family 0), polish 3.

## Should fix

1. **The Snow Town welcome holds the queue, so result lines land late and its second line plays after its moment**
   (general; wave lesson "a welcome put off past a first tap's own line lands late", `welcomeAfter: true` at
   src.html:1197 in a two-mode tool).
   - Where: src.html:1192 to 1198, the welcome lines `wTown` and `hTown`. Each has only `valid: idle`.
   - Why it matters now: with the real clips the two lines are 7.4 s and 5.9 s, so 13.3 s of talk. The queue plays
     them before any later line, and `hTown` still plays once the class has done what it asks.
   - Seen 1 (`v/v10-first-go-guess.json`, `v/w5-first-go-frame.png`): tap Star, Up, Go at 0.8 s gaps. Pip stops in
     the snow at about 4.5 s. Then "Tap a house to choose where the letter goes. Then tap the arrows..." plays from
     8.95 s to 15.0 s, with the house picked and a card already walked. "Pip stopped in the snow" comes at 15.1 s,
     about 10.5 s after the stop.
   - Seen 2 (`v/w1-burst-again.json`, `v/w3-clear-plain.json`): Clear pressed during the welcome. "All clear" waits
     behind `hTown`, 6 s late in w2 and still not played 8 s after the tap in w1 and w3.
   - Seen 3 (`v/w4-first-guess-frame.png`, `v/v4-first-guess.json`): the first tap is Guess. The hint says "Tap the
     square where you think Pip will stop." At 12.1 s the voice says "Tap a house to choose where the letter goes",
     but a house tap there would place the flag.
   - The audit confirms it: the welcome is late after the first tap on Up, Left, Right, Down, Guess, Go, Step and
     Clear (`audit/audit.md`, walk table).
   - Better: drop `welcomeAfter` (a skipped welcome comes back on the next mode entry or Sound on). Give `hTown`
     `valid: () => howNow() === 'hTown'`. Let a result line or Clear hush a welcome that has not started. Done when, at
     a 0.8 s first-tap pace, no result line plays more than about 1 s after Pip stops, and no line names a house
     while Guess is on.

2. **A level intro talks over the walk, and the bump line lands about 5 s late** (general).
   - Where: `go()` at src.html:1058 to 1068 only hushes hGuess, hFlag and hGo.
   - Seen (`v/v3-l4-go-during.json`): level 4, Go pressed 3 s into the 13.75 s intro. The intro plays on to 17.5 s,
     still saying "Press Go, then find it" while Pip walks and bumps at about 12 s. "Flump! Pip bumped into a
     snowbank" starts at 17.6 s, about 5.5 s after the bump.
   - The same thing happens on level 1 (`v/v7-l1-deliver.json`) and level 8 (`v/v8-l8-allDone.json`): the level line
     and hBuild run during the walk. Those are shorter, so the result there is under 1 s late.
   - Teachers will press Go early on fix-it levels, because the class can see the cards.
   - Better: Go also hushes a playing level intro and the build or fix how line (lv1 to lv8, hBuild, hFix, hFix6,
     hFix7, hCard), as it already does for the guess lines. The hint still shows them, and Read still says them.

3. **Take 0 (the Snow Town welcome) puts its pause in the wrong place** (general; voice).
   - Where: voice/9ceae64313f5.mp3.
   - Seen (`asr.json`): Whisper base.en and large-v3 both transcribe "Welcome to Snowtown Pip. The penguin carries the
     mail."
   - The raw take bears that out: there is no pause between "Town" and "Pip" (60 ms gap at 1.97 s), then a 0.41 s
     pause after "Pip" (2.37 to 2.78 s). So it reads as welcoming Pip, and "the penguin" loses its name.
   - It is the first line every student hears. The liveliness reading does not measure this, so it did not flag it.
   - Fix: `localvoice.py snowy-mail-route --redo 0`, then listen to the new take.
   - Every other take matches its line word for word in large-v3 or base.en (the rest of the differences were "1"
     for "one", "treehouse" and "male carrier" in base.en, and large-v3 hears "mail carrier").

## Polish

4. **The level 4 clip only just beats the kit's hold cap** (general; kit/curio.js:83).
   - `cap = 2500 + 80 * length` gives 14.02 s for a 144-character line. The take is 13.75 s.
   - In `v/v2-l4-listen.json` it played 3683 to 17515 ms, with 170 ms to spare before hCard would have cut its tail
     ("then find it"). Not cut in any of my runs, but a slower laptop could cut it.
   - Better: the cap uses the clip's own duration when there is one. Or split lv4 into two lines, which would also
     help item 2.
   - No other clip is within 1.6 s of its cap.
5. **680x425: on a wrong-house stop, Pip and the number circle cover about half the Fish symbol**
   (`a/z-680-wrong-fish.png`; the same at 800x500, `b/800x500-town-wrong.png`). The fish is still readable, and at
   1366 and up the symbol is clear (`a/1366-town-wrong.png`). The preview size only.
6. **Arrow names go quiet while the welcome or an intro plays.** "Up!" and "Right!" are dropped as `newer` or `stale`
   (maxAge 1800) in every run that starts with arrows (`v/v1`, `v/v7`, `v/v8`). That is by design (latest only), but
   with 13 s of welcome a class tapping arrows hears nothing back. Item 1 mostly fixes this.

## Checked and clean

- **Frames** (looked at every one):
  - Default screen, Snow Town delivered, wrong house, bank bump, Guess with the flag, Mail Route level 1, the picker,
    the level 4 bump, the level 4 footprint tap (badge on card 5 only after the tap), the level 8 finale and its end.
    All of these at 1366x768 with Motion on and at 680x425 with Motion off (`a/`).
  - Default, wrong house, level 4 bump and level 8 end at 800x500, 1000x625, 1280x720, 1920x1080 and 760x900 (`b/`).
  - Town wrong house, route delivered and Guess at 375x812 (`c/out/`).
  - The audit's size and mode frames (`audit/`).
  - No overlaps, clipping, sideways scroll or placeholders anywhere. The tray, Go and all 12 slots are in view at
    every size. The caption plate stays readable over the sky. Footprints point the way Pip stepped and are readable
    at 1366.
- **Art:** none by spec (art/prompts.json has no assets), no `art:` tokens in the bundle, and no people.
- **Targets:** 1280x720, 1366x768, 1920x1080 and 760x900 are clean at 60 px (audit). Under 60 px only at the preview
  sizes and 375, where the spec and refine.md settled a 44 px floor. Nothing is under 44.
- **Motion off:** nothing runs forever (audit `calm`). In the 680 runs the flakes stand still and the hearts show.
- **Voice, the standard checks:**
  - Five held clicks 2 s apart and two quick taps are clean on every control that speaks (audit).
  - Read speaks the hint only. Sound as the first tap says nothing.
  - A mode switch, the picker and Start over cut the line playing, as designed (`v/v9`, `v/v2`).
  - The finale sequence (Delivered, then allDone, then hAgain) plays whole with no cuts (`v/v8`).
  - Every played clip's text is in voice/lines.json. `__tool.allLines` equals lines.json, all 47 lines, and every
    line has its clip (K-2).
- **Contract:** 963 KB, under 2 MB. No console errors or exceptions in any run. No network requests from the tool:
  the resource list was empty on file://, and the 375 run fetched only the host page and its favicon. No em dashes,
  and "Curio" never appears alone in the words.
- **Solo student and teacher run:** the Snow Town free play and all eight levels through the picker play end to end.
  The finale lands warmly. The one flat or confusing stretch is the opening: 13 s of Snow Town welcome, and 15.6 s
  into Mail Route level 1 (wRoute, lv1, hBuild). The class's first actions get no voice back, and a result arrives
  late (items 1 and 2). On a projector the screen itself reads clearly.

## Audit pilot

- **Leads confirmed:** the welcome is late after the first tap on 8 controls. That is item 1, and my runs show the
  worse effect: result lines held behind hTown.
- **Leads that were wrong or already settled:** the small-target rows at 680x425, 800x500, 1000x625 and 375 are the
  spec's 44 px floor, settled in refine.md.
- **What it missed:** a level intro running over a walk (item 2), a take's phrasing (item 3), and how close a clip is
  to the kit cap (item 4). It has no way to see lines that wait long behind the queue.

## Re-check (2026-10-29, after final-fix.md)

I read final-fix.md as claims and checked each one on my own runs.
- Bundle: 970 KB, with the new take in.
- Ports: 9211 and 9212. The scratch host on 8812 got a copy of the new bundle.
- Output: `S:/CurioClass-codex-scratch/final/snowy-mail-route/r2/`. The voice runs are in `v/` (full logs with clip
  start, end and cut times, plus walk start and stop times). The frames are in `a/` and `b/` (the same plans as
  round 1), with contact sheets `sheet-a.png` and `sheet-b.png`, and 375 is in `c/`.
- Kit change: kit/curio.js only adds an opt-in `hold` (max of the cap and hold, never shorter).
  `python scripts/test_voice.py` gives 42 passed, 0 failed.

### Items
1. **Fixed.** The welcome no longer holds the queue.
   - Star, Up, Go at 0.8 s (`v/f1`): the welcome is cut at Go (3278 ms), and "Pip stopped in the snow" starts at
     4385 ms, the same ms the walk stops.
   - Clear during the welcome (`v/f2`, `v/f10` burst): "All clear" starts at the tap, about 10 ms later.
   - First tap Guess (`v/f3`): only "Tap the square..." is said. Guess pressed during the welcome (`v/f4`): hTown is
     dropped as stale, and "Tap the square..." follows. No line names a house while Guess is on.
   - A plain first tap (`v/f5`) still gets wTown then hTown whole.
   - Sound as the first tap, then Sound on (`v/r7`), brings the welcome once.
   - Read cuts the welcome and speaks the hint (`v/r6`).
2. **Fixed.** Go cuts the intro, and the bump line comes at the bump.
   - Level 4, Go 3 s into the intro (`v/f6`): the intro is cut at 7656 ms (Go) and the queued hCard is dropped.
     "Flump!" starts at 13191 ms, the same ms the walk stops, and hLast follows.
   - On levels 1 and 8 (`v/f8`, `v/f9`) the intro or hBuild is cut at Go, and Delivered starts at the stop ms.
   - The level 8 finale (Delivered, allDone, hAgain) plays whole with no cuts.
3. **Fixed.** The new take reads right.
   - Whisper: base.en hears "Welcome to Snow Town. Pip, the penguin, carries the mail." and large-v3 hears
     "Welcome to Snowtown! Pip the Penguin carries the mail." Both now put the sentence break after "Town". The rest
     of the line is word for word (`r2/asr-*-0.json`).
   - The raw take bears that out: 0.30 s pause after "Town" (2.03 to 2.33 s), "Pip" from 2.33 to 2.52 s, then a
     0.34 s breath before "the penguin". It reads as a name with an appositive, not "Welcome to Snow Town, Pip".
     I did not listen myself.
   - The take is 8.03 s, inside its 10.0 s cap.
4. **Fixed.** Level 4 left alone (`v/f7`) plays 3656 to 17483 ms, uncut, then hCard plays whole.
5. **Fixed.** At 680x425 and 800x500 the Fish symbol is clear of Pip and the number circle (`r2/z-680-fish.png`,
   `r2/z-800-fish.png`). The same holds at 1366, at 375 (`r2/c/375-town-wrong.png`) and on deliveries.

### Repeat counts (five each, real clips)
| Line | Kind | Expected | Spoken |
|---|---|---|---|
| Up! (5 taps, 2 s apart, `v/r1`) | event | 5 | 5 |
| Add an arrow card first! (Go x5 on empty, `v/r2`) | event | 5 | 5 |
| All clear (x5, `v/r4`) | event | 5 | 5 |
| Flump! bank (Go x5, `v/r3`) | event | 5 | 5, each at its walk stop |
| Wrong house (Go x5, `v/r5`) | event | 5 | 5, each at its walk stop |
| hLast, hFoot (during those runs) | how | 1 | 1 each, at the first quiet moment, dropped unmarked before then |
| wTown, hTown | welcome | 1 | 1 |

- **K-2 lines:** every fixed line has its clip. `__tool.allLines` equals voice/lines.json (47 of 47). No line text
  changed, and only take 0 was re-recorded. No played clip was cut except by Go, Step, a result, a mode or level
  switch, or Read, as designed.

### No regression
- **Frames:** all 22 of set A (1366 with Motion on, 680 with Motion off) and all 20 of set B (800x500, 1000x625,
  1280x720, 1920x1080, 760x900) were re-shot and looked at, plus three at 375. No overlaps, clipping or controls out
  of view.
- **Console and network:** no console errors, and no network requests beyond the 375 host page and its favicon.

### The two known items (not blocking)
- **Arrow names drop while the welcome plays:** they are latest-only events with a 1.8 s maxAge, by design. Any
  result or Clear now cuts the welcome, so nothing waits behind it. A nit.
- **Level 8 hBuild after cards are down** (`v/f9`): "Tap the arrows to make Pip's path. Then press Go" started at
  9966 ms with cards on the strip, and Go cut it at 10316 ms. Its second half is still the next action, and Go cuts
  it. A nit.

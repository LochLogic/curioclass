PASS (round 2 re-check, 2026-10-28): B1, S1 to S4 and the bow polish met; small-stage wave misses at 375 and 680x425 recorded as a known gap
Counts: blockers 2 (general 0, family 2), should fix 10 (general 8, family 2), polish accepted 8

# levels-and-pathways: Refine

Lens files: refine/teaching.md (T), refine/play.md (P), refine/craft.md (C). Read them for frames and detail.

## Blockers
1. **Big zigzags are named straight** (T-B1; family:dance, the path classifier in kit/dance.js). Two or more sharp
   corners turning alternately left and right make a zigzag at any leg length. Test with real drags: full-floor
   zigzags with legs 30 to 60, a 3-leg zigzag, plus the cases T found correct (line, arc, scribble, too short).
2. **Low reads tall or standing from the front** (P-B1, T-S3; family:dance, the pose library). Every Low pose and its
   count-8 freeze must sit clearly lower than any Middle pose from the front (Curl's open star at Low goes to the
   floor; Stretch and Bend at Low are distinct and clearly low). Check a contact sheet of every move at each level
   from the front: a K-2 child copying it must get close to the floor.

## Should fix
3. **Drawn path split wrong** (P-S6, C-S4; family:dance). A straight, zigzag, arch line names three parts; a smooth
   arch is one curved part and an S-curve is curved (Done when 5). Fix the reach rule and the extra straight-run
   rule together with item 1; keep one test table of drawn shapes in handoff.md.
4. **Header buttons under 60 px** (C-S1). 60 px at every size, in this tool's CSS (as robot-dance does), no kit change.
5. **Mystery after Next** (P-S1, C-S2). The "Tap Go" how-to is not dropped while the dancer walks back; the hint names
   Go when Go is the action; Read speaks it.
6. **Welcome during a round** (C-S3). Coming back to Mystery mid-round or Sound off and on brings the line for the
   round's current step, not "Tap Go".
7. **Round 8 to gallery** (P-S2). The last right answer gets its "Yes!", the hint changes with the gallery, and the
   gallery line follows without a 4 s silence.
8. **Waiting hints name the next action** (P-S3, C polish). Levels after "And freeze!", Pathways after a trip, the
   right-level line not repeating "Tap Next" every round once said.
9. **Move icons look the same** (P-S4; family:dance). Each move's icon is distinct at every level (at High five of six
   are the same; Stretch and Twist at Middle).
10. **Gallery crowded** (P-S5). End badges don't overlap; the bowing dancer doesn't cover the front-row ribbons; High
    ribbons stay visible.
11. **Mystery cites the wrong code** (T-S1). It teaches DA:Re7.1.Kb, not Ka; fix the cite in notes.md and the spec,
    and the Cr1.1 wording. The grade 1 and 2 Re7 codes move off this module (the integrator moves them to
    dance-pattern-puzzle and dance-styles-explorer; record it in handoff.md, don't edit other tools).
12. **Draw a path claims Cr3.1.1b, Cr3.1.2b and Cr1.1.2b without teaching them** (T-S2). Settled with BASELINE
    (standards taught well): after drawing, the class taps a numbered part to give it a level (high, middle, low,
    with the level icons), so one drawn dance can change level part by part, and the dancer performs each part at its
    level; Surprise path sets mixed levels. Voice the new step once (how line). Add it to the spec under "Refine
    changes".

## Polish accepted
13. A "Yes!" that comes while the class answers during the question isn't late (P).
14. No leftover phrase boxes in the count strip (P).
15. The Low end pose doesn't look like a fall (P).
16. Surprise paths don't cross themselves; the round 7 circle stays on the floor (P).
17. The count-in doesn't start under Read (P).
18. Mystery round dots clear the mirror frame (C).
19. At 760x900 the move grid is in view; at 375 the Level row is in view; the 680x425 hint isn't clipped (P, C nits).
20. dance.md lists flat, skeleton, shade and heard, and says what facing angles mean (C, family:dance).

Nits are optional; fix the cheap ones (narrow-header mode buttons get aria-labels, the curved ribbon starting off the
star in calm mode, the first-action long drag playing the welcome before the part names).

## Settled calls
- The gold Mystery ribbon until the level answer (builder's call) stays: it keeps the level hidden.
- No shared movement.js: BASELINE w1-21 (PE and dance each get their own figure). fitness-circuit's spec note about a
  shared figure is out of date; the integrator fixes it before that tool is built.

## Exit check (round 1, 2026-10-28, fresh cold agent)

Checked cold against the REFINE.md Exit check, STANDARDS.md and BASELINE.md. I read handoff.md but did not trust it.
Every item below was re-checked with real drags, held clicks and frames. The bundle was rebuilt with CURIO_DRAFT=1
(168 KB). Frames and shot lists are in the checker's scratch folder (exit-lp), not in the repo. host.html was deleted.

### Open (blocks PASS)

B1. Blocker, family:dance (same class as merged 1). Dance.readPath still names smooth front-to-back curves wrong:
- A vertical S drawn on screen (amplitude 0.14 to 0.20 of floor width) reads "straight" three or four times,
  "straight, curved, straight", or "zigzag". At amplitude 0.10 it reads "straight, curved".
- A smooth 3-hump wave reads "zigzag, curved, straight" or "zigzag, curved, zigzag".
- The red overlay in the frames shows the drawing is smooth.
- Merged 3 ("an S-curve is curved") holds only for an S drawn side to side.
- Done when 5 fails for a 3-corner scribble whose turns do not alternate (-113, +133, +128). It reads "straight,
  curved, straight, straight", so a sharp V tip is named curved.
- Every zigzag case passes (see merged 1 below). The gap is curve detection along the depth axis and at gentle bends.

S1. Should fix, family:dance (merged 2 and 15 not fully met). In Low Curl, the move from the kneeling ball to lying on
the back lifts the head to 0.71 to 0.72 of standing height mid-count, on every count. The frame looks like a backward
fall with the legs splayed (MOVES curl low, src.html:265). handoff.md says every count is at most 0.62, which is not
true for Curl. The keyframes themselves are fine.

S2. Should fix, general. This happens when a class calls out both answers at once, so the level is tapped during the
1.5 s right-path paint:
- (a) answerPath ends the paint with tr.end(badge(R.path, null)) before its live check (src.html:735). The ribbon's
  level badge is replaced by the gold path-only badge.
- (b) In round 8, the gallery cell for that ribbon loses its level icon the same way.
- (c) The late askLevel line drops the queued nextHow line. The hint stays "Yes! That's the level." and never names
  Next. In a fast full run, nextHow was never spoken.

Slow answers work: askLevel is spoken, nextHow follows 4.3 s after rightLevel, and the hint reads "Tap Next for a
new mystery."

S3. Should fix, general (gate 2). Cr3.1.1b (show several types of movement by picture or symbol) is claimed but not
taught:
- spec.md and the src.html header still claim it through "Cr3.1.Kb to Cr3.1.2b".
- The way to move is one choice for the whole drawn path, and it does not appear on the map.
- Fix: put a way icon on each part's badge, or drop the claim and write down where the code moves (rule 2).

The new per-part levels do teach Cr3.1.2b. The mixed path-and-level dance arguably teaches Cr1.1.2b (combine
movements while changing the elements), but spec.md, the header and notes don't cite it. Cite it if it stays.

S4. Should fix, general. Part badges on small stages, counted over 40 Surprise paths:

| Stage | Off the stage | Number covered |
|---|---|---|
| 375 wide (via host) | 4 of 89 (pushed above the top, can't be reached) | 17 of 89, mostly badge 1 behind the dancer at the star |
| 680x425 | 0 | 9 of 88 |
| 1280x720 and 760x900 | 0 | 0 |

At 1280, badge 1 also sits behind the dancer when there is a lead part. The cause: the overlap nudge only moves a
badge up, by s*1.25, up to 6 times.

Also noted (not blocking):
- Polish: the gallery bow pose looks odd from the front, with one arm up and back.
- Record fix: handoff.md says Middle is at least 0.80. The measured Middle minimum is 0.77 (Bend B), still clearly
  above every Low keyframe.

### Merged list, re-checked

1. Met for zigzags. Real drags at 1280x720, 1366x768 and 760x900, seeds 7, 3, 5, 29 and 11:
   - Read zigzag: full-floor zigzags with legs 30, 40, 50 and 60, a tall 5-leg zigzag, 3-leg zigzags (legs 34 and
     43 to 50), a many-corner scribble, and zigzags drawn on screen.
   - Straight, then zigzag, then arch (small and big) reads "straight, zigzag, curved".
   - A 2-leg V reads "straight, straight" (acceptable).
   - For curves, see B1.
2. Met for keyframes, not for the Curl move between them (S1). From the front, Low head height as a share of
   standing height: stretch 0.30 to 0.52, twist 0.56, bend 0.47 to 0.53, swing 0.43, shake 0.08, curl 0.08. A K-2
   child copying gets close to the floor on every Low pose.
3. Partly met. These read right: line, diagonal, arc, smooth arch, tall rainbow, side-to-side S and gentle wave. Too
   short gives the tooShort line. The front-to-back S and the 3-hump wave fail (B1).
4. Met: header buttons are 60 px at every size.
5. Met: after Next, the hint is the Go line.
6. Met: the welcome does not replay mid-round. On return to Mystery, askPath is silent "heard" and the hint keeps the
   path question.
7. Met at real speed:
   - Round 8 Yes at 175.35 s. "Yes! That's the level." shows for 2.1 s, then allDone at 177.45 s, with no silence
     after the Yes line.
   - Final buttons are Play again only, and all 8 round dots are checked.
   - Fast answers break it (S2).
8. Partly met.
   - Per-part levels work with real clicks. Badge 2 tapped twice goes middle, low, high; badge 3 tapped once goes
     low. With mixed parts, no level tile shows pressed.
   - Dance it changes level at counts 1, 3 and 15 of 22. The ribbon look changes per part, and the guide follows.
   - Voice: tapPart is spoken once per load and is silent "heard" on the next 4 drawings. danceIt is spoken once.
   - Minor: with very fast taps, danceIt is dropped and the hint shows the level line until the teacher waits.
   - For the standards side, see S3.
9. Met: move icons are distinct at 60 px.
10. Met, except the fast-answer gallery badge (S2).
11. Met: the Re7.1.Kb cite is present.
12. Met: Surprise mixes levels and does not cross itself in 40 paths.
13. Met.
14. Met: no leftover phrase boxes in the count strip in any frame.
15. Not met for Curl (S1). The other Low end poses read as low shapes, not falls.
16. Met: no self-crossing in 40 Surprise paths, and the round 7 circle stays on the floor.
17. Met: Read during a move hushes the count and the queued lines. stretch was spoken, atMiddle and copyMe were
    dropped "hush", then read. There is no count-in under Read.
18. Met: the dots clear the mirror frame.
19. Met: at 760x900 the move grid is in view, at 375 the Level row is in view, and the 680x425 hint is not clipped.
20. Met: docs/families/dance.md lists flat, skeleton, shade and heard, and explains facing angles.

### Regressions

I re-shot the default screen, every mode and the frames tied to each fix at 680x425, 800x500, 1000x625, 1280x720,
1366x768, 1920x1080, 760x900, and 375 wide through drive.py --host.
- No control is under 60 px, and part hit areas are at least 98x64.
- Every control has an icon.
- No horizontal scroll, and no hint is clipped.
- At 760x900, Up and down, Surprise and the way row sit below the fold, which matches the designed stack order.
- No console errors. The only failed request is the host favicon (404).
- The dancer lives in kit/dance.js, with no movement.js (BASELINE w1-21).
- kit/dance.js and docs/families/dance.md are still untracked (nothing committed).

### Gate

1. Done when: fails. Not every item passes (B1 against Done when 5 and the S-curve item; S1).
2. Codes: fails. Cr3.1.1b is claimed but not taught, and Cr1.1.2b is taught but not cited (S3).
3. Solo defaults: passes. A solo student gets the welcome, a working stretch at Middle, and Draw a path with Surprise.
4. Sensitivity agent: not needed for this tool.
5. Open blockers or should-fix items: fails. B1, S1, S2, S3 and S4 are open.
6. Bundle: passes.
   - 168 KB, built with CURIO_DRAFT=1.
   - Only the expected "no recording yet" warnings, no console errors, and no network requests beyond the file.
   - Art drawn in code and browser voice with no clips are expected.
7. Voice counts: passes (table below; held clicks, hold 0.12).

| Line | Kind | Expected | Spoken |
|---|---|---|---|
| wLevels (load) | welcome | silent until the first tap, then once | silent "early", spoken once on the first stage tap (1.37 s) |
| stretch x5 | event | 5 | 5 |
| atMiddle x5 | event | 5 | 5 |
| copyMe x5 | how | 1 | 1, then silent "heard" x4 |
| atHigh x5 | event | 5 | 5 |
| curved x5 | event | 5 (the first may yield to the mode welcome) | 4; the first was dropped "newer" behind wPaths |
| Go x3 (straight, walk) | event | 3 | 3 each; ribbon spoken 2 |
| Surprise x5 | event | 5 | 5, with the part names spoken each time |
| tapPart, danceIt over 5 drawings | how | 1 each | 1 each, then silent "heard" |
| Stale taps (move, move, level, mode, path, mode in 1.2 s) | stale | dropped | twist, atMiddle, copyMe and zigzag dropped "hush"/"chain"; the last mode welcome spoken |
| Read | read | read, hushes the queue | read; queued lines dropped "hush" |
| Read with sound off | read | read | read |
| Sound toggle as the first tap | first tap | silent while off | silent; welcome spoken once when sound is back on |
| Mystery (full run) | mixed | rightPath 8, rightLevel 8, wrong 1, wMystery 1, askPath 1, allDone 1 | as expected; nextHow 4 at slow pace, 0 at fast pace (S2) |
| Order | order | event, then how | event always first, how after |

## Exit check, round 2 (2026-10-28, same cold checker)

I re-checked B1, S1 to S4 and the polish item myself, with real drags and clicks. I read the builder's Refine round 2
account but did not trust it. The bundle was rebuilt with CURIO_DRAFT=1 (174 KB). Frames and logs are in the
checker's scratch folder (exit-lp), not in the repo. host.html was deleted afterwards.

### B1, readPath: met

Test set:
- 17 shapes, each drawn in six directions: side to side (0), front to back (90), back to front (270), right to left
  (180) and both slants (45, -45).
- Each shape is fitted as big as it goes into the floor, and drawn with a wobbly hand at 3 to 9 px samples, as real CDP
  drags.
- The shapes: line, arc, arch, S at amplitudes 0.20, 0.35 and 0.50, the 3-hump wave, a 4-hump wave, a gentle wave,
  3-leg, 4-leg, tall 5-leg and small 6-leg zigzags, the round 1 non-alternating 3-corner scribble, an alternating
  scribble, straight then zigzag then arch, and too short. A lead part is ignored.

Results:

| Size | Right | Misses |
|---|---|---|
| 1280x720, seed 7 | 102 of 102 | none |
| 1280x720, seed 23 | 102 of 102 | none |
| 1366x768 | 102 of 102 | none |
| 760x900 | 100 of 102 | 4-hump wave at 90 read "curved, curved"; straight-zigzag-arch at 90 read "straight, straight, curved" |
| 680x425 | 94 of 102 | 4-hump wave x4, mostly "curved, curved"; 3-hump wave at 180 read "straight, curved"; zig3 at -45 read "straight, zigzag"; the scribble at 90 and -45 read "straight, straight, zigzag" |
| 375 (host) | 93 of 102 | all 9 are 3-hump or 4-hump waves, 3 of them read with a zigzag piece |

- The shapes that failed in round 1 now read right at the projector sizes in every direction: vertical S, 3-hump wave,
  gentle wave and the 3-corner scribble.
- Done when 5 holds at the projector sizes.

Small-stage judgement: acceptable, because the stage is too small to draw on; the classifier is not the cause.
- At 375, a front-to-back wave fits into about 110 px of stage height, so each hump is 25 to 30 px tall against a few
  px of hand wobble. The humps are already pointed in the drawn line itself (frame r2-small-miss.png).
- Every zigzag case still reads zigzag at 375 and nearly every one at 680x425. The misses are waves and corners that
  are squeezed small.
- Done when 8 asks only that buttons stay 60 px at 375, and the K-2 class draws on the projector.
- Recorded as a known gap (handoff.md already lists it). Not open.

### S1, Low Curl: met

I sampled the head height on every animation frame, 22,561 frames over 55 runs, as a share of standing height:
- Static in-betweens at Low, 81 per move: stretch 0.52, twist 0.56, bend 0.53, swing 0.43, shake 0.08, curl 0.53.
- Every Low move played in full one after another, every ordered pair of Low moves cut 0.3 to 1.0 s into the counts,
  and three Low moves tapped 0.2 s apart: the maximum is 0.563, with no frame over 0.62.
- The only frames above 0.62 are the very first sit-down from the standing start (7 frames, 0.66). That is sitting
  down, not a fall.

### S2, fast level answer: met

I played two full real-speed games with a real first tap and held clicks: all answers fast (level 0.3 s after the
path) and all slow (level 2.4 s after).
- In both games, every round ends with the full badge (0 gold badges) and the hint reads "Tap Next for a new mystery."
- Round 8 keeps all 8 gallery badges with their level icons (0 gold) and the hint reads allDone.
- A wrong level called during the paint (round 3) shows the path-only badge while the level is still open, then the
  full badge after the right answer.
- Voice, both games: rightPath 8, rightLevel 8, nextHow spoken 1 then silent 6, allDone 1, wMystery and askPath 1 each.
  askLevel is spoken 1 in the slow game; the fast game says it once, after the wrong answer.

### S3, standards: met

- DA:Cr1.1.2b is cited in spec.md (Standards line and Refine round 2), the src.html header and notes.md.
- DA:Cr3.1.1b is gone from every claim. Its move off this module is written down for the integrator (spec.md and
  handoff.md), which satisfies rule 2.

### S4, part badges: met

45 Surprise paths per size, plus 5 checked after Dance it:
- At 375 (host), 680x425, 760x900, 1000x625 and 1280x720: 0 off the stage, 0 badges overlapping, every hit area at
  least 64 px.
- Number circle covered: 0 on Surprise paths at every size.
- Nit: after Dance it, with the dancer standing at the path's end, a number circle is sometimes partly under the
  dancer's shadow or another part's line. This happened 1 time at 375, 2 at 680x425 and 1 at 1000x625. The badge
  stays tappable.

### Polish, bow: met

The gallery bow now reads as a fold at the hips, turned toward the ribbons (frame s2-fast.png).

### Regressions

- Zigzag family: all zigzag and scribble cases right at 1280, 1366 and 760x900 in all six directions (table above).
- Round 8 to the gallery: met in both games (above).
- No console errors in any run. The only failed request is the host favicon (404).
- Voice repeats, held clicks: the same counts as the round 1 table. copyMe 1 then silent "heard" x4; stretch,
  atMiddle and atHigh 5 each; curved 4 with the first dropped "newer"; tapPart and danceIt 1 each then silent over 5
  drawings; Go events 3 each.
- Voice, the rest of the standard check (held clicks), also the same as round 1:
  - Stale taps are dropped "hush"/"chain".
  - First tap: the stage tap speaks the welcome once; a first Sound-off tap stays silent.
  - Read reads and hushes the queued lines, with sound on or off.
  - Coming back to Mystery keeps askPath silent "heard".

### Gate

1. Done when: passes. Item 5 holds at the projector sizes; the small-stage waves are a recorded gap.
2. Codes: passes. Every cited code is taught, and the Cr3.1.1b move is written down.
3. Solo defaults: passes.
4. Sensitivity agent: not needed for this tool.
5. Open blockers or should-fix items: none.
6. Bundle: passes. 174 KB, CURIO_DRAFT=1, only the expected "no recording yet" warnings, no console errors and no
   network requests.
7. Voice counts: passes.

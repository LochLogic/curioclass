# Teaching lens: letter-lanterns (round 1)

Cold read of spec.md, src.html, notes.md, lesson.json, voice/lines.json, tool.draft.json, audit-r1. Driven with
scripts/drive.py (port 9868, muted). My frames and logs: `S:/CurioClass-codex-scratch/letter-lanterns/teaching/out/`
(shot lists shots.json to shots4.json, glow sim glow.py beside them).

Counts: blocker 2, should fix 4, polish 3, nit 2.

## Blockers

1. **Every sound inside a sentence is written as a bare letter, so the voice says letter names, not sounds.**
   Where: lesson.json `lines` find.* (26), wrong.* (26), intro.* (26), short.* (5), twinDiff.* (10): "Which lantern
   says t? Tap it.", "T. T says t, like turtle.", "A. A says a, like ant.", "Short glow: a, like ant.", "a. o. Cat.
   Cot." Only m, s, n, f, r, l, v, z are spelled as sayable sounds (mmm, sss); t p d b c k g h j w y, x (ks), q (kw)
   and all five vowels are single letters. How seen: the voice log in out/01, 02, 04, 06 shows these exact texts going
   to the voice; a lone "t" or "a" is read "tee", "ay" by the browser voice and by any text-to-speech model. In
   voice/lines.json only the 31 `sound.*` / `longSound.*` ids carry the "isolated sound, not the letter name"
   instruction (`phoneme_takes_required`); the 93 sentence lines that also carry a sound have none, and Done when 9
   checks only the 31 clips. Effect: the Find question for 18 of 26 letters asks for the letter name; intro.a says
   "Ay says ay, like ant", which teaches the wrong short a; short.a and long.a sound the same ("ay"), so RF.K.3b's
   contrast is never heard in words. This is the core of RF.K.3a and b. Fix direction: play the recorded `sound.<l>`
   clip inside these lines (sequence: "Which lantern says" + sound clip + "Tap it."), or give every such line its own
   phoneme direction and add them all to Done when 9. Also longSound.* is recorded but never played (src.html has no
   `longSound` reference); findLong.* should use it. Tag: general (any phonics tool).

2. **Lantern check Finds always use the same three lanterns, so the third Find is free by elimination and glow
   inflates.** Where: src.html:717-718 (`makeChoices(target, true)` pool = the other check targets only), spec
   Interactions "choices from lit letters". How seen: out/40-check-trio (10 lit letters): the three Finds offered
   {a,m,s}, {a,s,m}, {s,m,a}; the last one is the only letter not yet asked. glow.py: a class that knows none of the
   three sounds but remembers which were asked raises about 2.4 letters to two stars in 4 checks, against 0.8 for
   blind guessing (spec's sim assumed blind 1/3 guessing). Glow is the tool's picture of what the child knows (One
   idea), so a meter that rises on elimination misleads. Fix: draw the two distractors from all lit letters (spec), or
   at least not from the round's other targets. Tag: family:letter-pals.

## Should fix

3. **The vowel flame question always has the same answer: the tall flame on the right.** Where: src.html:1580-1585
   (short always left, long always right, labelled "Short" / "Long") and 837-858 (only `findLong` is ever asked).
   How seen: out/03-flames-a.png and out/04 log (short, long, then "Which flame says A?" and the right answer is the
   tall flame every time, for all five vowels). A child passes RF.K.3b's flame check without listening. Fix: ask for
   the short or the long sound at random, and swap the flame sides at random. Tag: family:letter-pals.

4. **The long/short word pick always asks for the short word, which is also always the longer word with the small
   flame.** Where: src.html:1214-1215 (`good = word === pair[1]`), lesson.json lsWhich.0-5 (not, got, met, hen, hit,
   wet), spec "Asked: the second word". How seen: out/05-long-0.png: the answer board is the 3-letter one with the
   small flame, in all six pairs. Cheap way: always tap the longer word. Fix: ask either word of the pair (for example
   "Which word says no?"). Also the spec's vowel lantern over each board is missing (only a loose flame shape, set
   between n and o on "no", not over the vowel). Tag: family:letter-pals.

5. **"Wake more lanterns to open it" plays on shops whose lanterns are all awake.** Where: src.html:1424-1436
   (`tapShop` says `asleep` for any shop not yet opened by its sign event) and 1506 (no sleeping lantern is drawn when
   every letter is lit). How seen: out/11-shops-zoom.png (street 2 with every letter lit, shops closed, no sleeper);
   by the EVENTS table this is the real state of sun after lantern 12, fan after 13, pen after 15 and hat after 16,
   and of any shop after a class leaves for Village mid-events. The line is false then. Fix: for a shop whose letters
   are all lit, a line such as "This shop opens soon. Tap Wake to read its sign." (and a waiting cue on the shop).
   Tag: general.

6. **Teacher notes and the public source list carry build-process text.** Where: notes.md:53 ("Clean isolated sound
   recordings still require the listening review described in the build report. The build is a draft and is not ready
   for a solo nonreader until that check passes."), notes.md:57 ("spec.md and codex-report.md ... recomputed in
   Scratch"), tool.draft.json sources ("supplied catalog verified in Scratch"). A teacher reading the tool page sees
   internal files and a "draft" warning. Fix: name the real sources (Dolch pre-primer, Fry first 100, the CCSS PDF,
   Moats, Reading Rockets) and drop the build-state lines. Tag: general.

## Polish

7. **Say step: the model sound plays right after "Say its sound", before the class can try.** Where:
   src.html:817 (`speak([say, intro.<l>])`). How seen: out/02 log: "Say its sound. Tap the lantern to check." at 8.7 s,
   then "Mmm. M says mmm, like moth." at 12.1 s with no tap. notes.md Key skills says "Say a sound before checking it
   against the model", which is not what Wake does. Better: intro first (as the spec orders it), then the "Your turn"
   line, and the model again only on the tap. Tag: family:letter-pals.

8. **Banner words fall back to a double-story a.** Where: src.html:198 (`'Century Gothic','Trebuchet MS',sans-serif`).
   Century Gothic is not on Chromebooks or a stock Mac; out/24-bannerfind-fallback.png shows the sight word "a" as a
   double-story a while every lantern and sign teaches the single-story form (spec Look). Better: draw banner words
   with the same `glyph()` paths as the signs (they exist for a, g, and capital I). Tag: general.

9. **Glow states are hard to see on the string.** out/10-string-zoom.png: 1 to 3 stars at about 10 px, halos not
   visible at string size. Done when 7 holds only up close. Better: bigger stars on the string, or show glow on the
   lanterns in Village's own view. (Play/Craft may weigh this more.) Tag: family:letter-pals.

## Nits

10. umbrellabird (short u anchor) is a word few five-year-olds know; the picture carries it, but "up" or "umbrella"
    is the usual anchor. Tag: general.
11. Trace check on short straight strokes rejects some wobbly but right traces through the direction rule: with
    white jitter of plus or minus .03h, m stroke 1 passed 85%, k stroke 3 88%, i stroke 1 90% (out/20-dbg); long
    strokes 97-100%. Real finger ink is smoother than white noise, so this may overstate it; worth one real-touch try.
    Tag: family:letter-pals.

## Done when

| # | Result | How |
|---|---|---|
| 1 | pass | audit sizes and states clean at every size |
| 2 | pass | out/31: welcome at 1.4 s, then "Which lantern says mmm?" at 6.8 s; hint changed at once |
| 3 | not re-tested | audit voice rows clean; left to Play/Craft |
| 4 | pass with blockers 1-4 | Find wrong stays asleep (out/02); See and say silent until tapped (code, src.html:1265); banner check 3 choices; twins: all 10 pairs differ in one place, shared lantern gives twinSame (out/06) |
| 5 | pass | out/07: three sound keys and two wrong pictures, "map" first spoken in open.map after the right pick; banners have no sound keys |
| 6 | pass | out/12: backward, half, tap-only and scribble failed on every stroke of all 52 letters, guided and free; third miss auto-completes (audit assisted-stroke) |
| 7 | weak | see polish 9 |
| 8 | not re-tested | Craft |
| 9 | fail | no clips in the bundle yet; and see blocker 1 (the check covers only 31 of the 120+ lines that carry a sound) |
| 10 | pass | out/13: Start over clears `curio-letter-lanterns`, shows Wake the village; reload resumed (out/02 loaded out/01's Find); privacy line in Teacher |

Event schedule recomputed in Python from lesson.json with every letter on: all 56 events play, none dropped, all 24
shops open, every twin follows both its signs, every long/short pair's letters are lit when it plays.

Facts spot-checked against my own knowledge of the sources: all 10 sight words are on the Dolch pre-primer list and
in Fry's first 100; c /k/, g /g/, x /ks/ at word end, qu /kw/; anchors ant, inchworm, octopus, elephant and
umbrellabird start with the short vowel; acorn, emu, ivy, ocean and unicorn with the long one; the six open/closed
pairs follow the open-syllable rule; stroke paths for a, b, c, d, e, g, s, u, J, U checked for direction
(counterclockwise a/c/d/e/g, clockwise b/p bowls, ball-and-stick). No cultural, Native or hard-history content; no
sensitivity review needed. No sensitive standard topics for the teacher notes.

## Audit pilot

- Leads confirmed: none that bear on teaching. The first-tap welcome rows for a lantern and Teacher are real but
  allowed by BASELINE rule 16 (nothing the welcome says is needed later).
- Leads wrong: "#begin Wake the village: welcome not heard". out/31 polled the voice every second: the welcome was
  spoken whole (no cut) and the Find question followed at 6.8 s.
- Missed (outside what it can see): blockers 1 and 2, should fix 3 to 6, polish 7 to 9. Tooling note: in my shots a
  drive.py `"wait"` after clicks did not seem to delay the `"after"` script (out/22 read an unplayed queue at "16 s");
  polling inside `"after"` gave the true timeline.

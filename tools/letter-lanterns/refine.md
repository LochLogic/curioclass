OPEN (round 1, Claude Refine 2026-11-06; Codex fixes next)
Counts: blockers 3 (general 2, family 1), should fix 15 (general 10, family 5), polish accepted 10
Traced to spec: blockers 1, should fix 7

# Refine: letter-lanterns

Lens files: refine/teaching.md, refine/play.md, refine/craft.md. Frames: teaching `S:/CurioClass-codex-scratch/letter-lanterns/teaching/out/`,
play `S:/CurioClass-codex-scratch/letter-lanterns/play/`, craft `S:/CurioClass-codex-scratch/letter-lanterns/craft/out/`, shared audit
`S:/CurioClass-codex-scratch/letter-lanterns/audit-r1/`. Integrator spot-checked: lesson.json find.t / intro.a / short.a /
twinDiff.0 text (blocker 1), `glyph()` at src.html:679-692 (blocker 2), `makeChoices` at src.html:717-718 (blocker 3).
(spec) = the cause is in spec.md; (build) = the spec was right and the build missed it.

## Blocker
1. **Sounds inside sentences are bare letters, so the voice says letter names, not sounds.** lesson.json `lines`
   find.* (26), wrong.* (26), intro.* (26), short.* (5), twinDiff.* (10). Integrator read: find.t "Which lantern says t?
   Tap it.", intro.a "A. A says a, like ant.", short.a "Short glow: a, like ant.", twinDiff.0 "a. i. Pan. Pin." A lone
   "t" or "a" is read "tee", "ay" by any voice; only m s n f r l v z are spelled as sayable sounds. Effect: 18 of 26 Find
   questions ask for the letter name, intro.a teaches long a as the short sound, and short.a and long.a sound alike, so
   RF.K.3a and b are not heard (teaching out/01, 02, 04, 06 voice logs). Fixed: every line that carries a letter sound
   plays the recorded isolated clip in sequence (for example "Which lantern says" + `sound.t` + "Tap it."; intro
   "T." + "T says" + `sound.t` + "like turtle."; twinDiff `sound.a`, `sound.i`, then the words). Long-vowel lines keep
   the letter name (the long sound is the name). Play the recorded `longSound.<v>` where the long sound is meant (it is
   recorded but never referenced in src.html). The shown hint text may stay as written; only the voice changes. Update
   voice/lines.json so every sentence piece is recorded once and Done when 9 covers every place a sound is heard.
   (general) (spec: the Content intro lines and the Voice table write the sounds as bare letters)
2. **Shop signs and long/short boards draw each letter scaled to its own box: no shared baseline, lowercase reads as
   capitals.** src.html:679-692 `glyph()` (viewBox cropped to each letter's own bounds; integrator confirmed), used at
   :1510 (signs) and :1601 (boards). "cot" reads "COt", the descenders of p and g ride up level ("pup", "pig", "dog"),
   the o in "dog" sits high. These are the words the child decodes, in a tool that teaches letter forms. Seen:
   craft out/Z-signs-village2.png, out/L-sign-680x425.png, out/L-twins-1366x768.png, out/H-twins-375x812.png. Fixed:
   lay each word out in one slate box (top line 0, midline .5, baseline 1, descender 1.5) with fixed advance widths,
   as the trace slate already does; use it for signs, twins, boards and banners (should fix 9). (general) (build)
3. **Lantern check Finds use only the round's other targets as distractors, so the third Find is free by elimination
   and glow rises without knowing.** src.html:717-718 (`makeChoices(target, true)` pool = `state.checkTargets`;
   integrator confirmed). Seen: teaching out/40-check-trio (10 lit): the three Finds offered {a,m,s}, {a,s,m}, {s,m,a}.
   glow.py: a class that knows none of the three but remembers what was asked raises about 2.4 letters to two stars in
   4 checks, against 0.8 for blind guessing. Glow is the tool's outcome picture, so this misleads. Fixed: draw the two
   distractors at random from all lit, enabled letters other than the target, as the spec says; fall back to the
   round's targets only when fewer than two other letters are lit; shuffle positions. (family:letter-pals) (build)

## Should fix
4. **The vowel flame question always has the same answer: the tall flame on the right.** src.html:1580-1585 (short
   always left, long always right) and 837-858 (only findLong is asked). Seen: teaching out/03-flames-a.png, out/04
   log. Fixed: ask for the short or the long sound at random per vowel (short plays the `sound.<v>` clip, long the
   name), and swap the flame sides at random; the flames keep their shapes (small round, tall). (family:letter-pals)
   (spec: "Which flame says ā?" names only the long sound and fixes nothing about position)
5. **The long/short word pick always asks for the short word, which is always the longer board.** src.html:1214-1215
   (`good = word === pair[1]`), lesson.json lsWhich.0-5. Cheap pass: tap the longer word. Seen: teaching
   out/05-long-0.png. Fixed: ask either word of the pair at random ("Which word says no?" / "Which word says not?") and
   shuffle board sides; record lsWhich for both words. (family:letter-pals) (spec: "Asked: the second word")
6. **Twins: open shop windows give the answer away.** Wake, Twins (for example pan/pin after lantern 7): the window
   shows a frying pan under "pan" and a pincushion under "pin", so "Which sign says pin?" is answered from pictures,
   not from the letter that differs (RF.K.3d). Seen: play f2/e03-twin-diff.png. Fixed: in the Twins step both shops
   show closed windows (goods hidden) until the sign pick is right, then the picked shop lights. (family:letter-pals)
   (spec: "Two open shops side by side")
7. **Say step speaks the instruction before the model, and the model answers it at once.** src.html:817
   (`speak([['say',{kind:'how'}],'intro.'+letter])`). Heard: "Say its sound. Tap the lantern to check." then at once
   "Mmm. M says mmm, like moth." (teaching out/02 log 8.7 s then 12.1 s; play f1/p04-right-m.png; craft v1 log). Fixed:
   intro on the right Find first, then the spec's full turn line ("Your turn. Say its sound out loud. Then tap the
   lantern to check."), and the model again only on the tap. Same order in a check's See and say. (family:letter-pals)
   (build)
8. **After the Say tap the next action is never spoken.** answerLetter, the say/seeSay branch (`hint('next');
   speak('sound.'+letter)`): the child hears "mmm" then silence beside a gold Next they cannot read; "Tap Next." only
   appears as a dropped placeholder in the log. Seen: play f1/p05-say-tap.png (log `[["spoken","mmm"]]`), f2/c02.
   Fixed: a how line "Tap Next." after the sound the first time (then hint only), the way other done moments end.
   (general) (spec: the Voice table has no line naming Next after Say)
9. **Banner words use a system font: double-story a where the fallback lands, and capital I is a bare bar like l.**
   src.html:198-199 (`'Century Gothic','Trebuchet MS',sans-serif`). Chromebooks and stock Macs have neither font.
   Seen: teaching out/24-bannerfind-fallback.png, play zoom-banner.png and f2/f02-banner-find.png ("I my the").
   Fixed: draw banner words with the shared word layout from blocker 2 (capital I with its bars, single-story a and g).
   (general) (build: the spec's Look sets ball-and-stick, single-story a and g)
10. **Sign and Twins say "lantern" over plain letter tiles.** src.html:1514-1515 vs lines `sign`, `twinIntro`: "Tap
    each lantern to hear it", "Tap the different lantern", but the sign shows cream tiles. Seen: craft
    out/L-sign-680x425.png, out/L-twins-1366x768.png; play f2/d01-sign-map.png, f2/e01-twins.png. Fixed: hang the small
    awake lantern art (already loaded) over each letter, as the spec says, so the lines are true. (general) (build)
11. **Glow levels cannot be told apart at a glance on the string.** `.string .stars { font-size:10px }`, halo via
    `::before` opacity; creatures differ in drawn size, so size reads as glow more than glow does. Done when 7 holds only
    up close. Seen: teaching out/10-string-zoom.png, play zoom-string.png, f3/v04, f3/v09. Fixed: one shared lantern box
    size on the string, stars about 16 px or more, a halo that steps visibly per level (none, small, bigger, full),
    with the sparkle on bright unless Motion is off. (family:letter-pals) (build)
12. **"Wake more lanterns to open it" plays on shops whose letters are all lit.** src.html:1424-1436 (`tapShop` says
    asleep for any shop not opened by its sign event), 1506. True for sun, fan, pen, hat between their letters and
    their sign events, and for any shop after a class leaves for Village mid-events. Seen: teaching out/11-shops-zoom.png.
    Fixed: a shop whose letters are all lit says a different line ("This shop opens soon. Tap Wake to read its sign.")
    and shows a waiting cue. (general) (spec: one asleep line for every closed shop)
13. **Village at 0 lit points at things that are not there.** Village welcome "Tap a lantern, a shop or a banner. Or
    tap Read the street." and the hint, with no lanterns or banners, every shop asleep, and Read the street answering
    "still asleep". Seen: play f3/v00-fresh-village, f3/v00b; audit lead #read-street. Fixed: at 0 lit the Village line
    and hint say the street is asleep and to tap Wake. (general) (spec: no 0-lit Village case)
14. **Below 800 px wide the Village shows no lanterns, but the welcome says "Tap a lantern".** At 680x425 and 760x900
    Village shows only the "26 lit" chip; at 760x900 the top half is empty sky. Seen: play f3/v11-680.png,
    f3/v13-760.png, audit state-demo-village-680x425.png. Fixed: at 760x900 hang the string in the sky (two rows if
    needed); at 680x425 drop "a lantern" from the line and hint when none is shown. (general) (build: the spec's chip
    is a Wake rule; Village hangs its lit lanterns)
15. **Opening Teacher speaks its how-to and the privacy line every time.** src.html:1764, 578-580 (`teacher`,
    `privacy`, `glowHonesty` queued as event lines): five opens spoke it 5 of 5 (craft v2-teacher-repeats,
    voiceA.txt). Fixed: `teacher` is a how line (once); privacy and glow lines stay on screen and in Read. (general)
    (build)
16. **The voice matches the nearest K neighbors.** voice/lines.json `bank: warm-teacher` (Sulafat), the same as
    calm-corner and sight-words. Fixed: switch to bank voice **playful-friend** (Laomedeia), kept, no K tool uses it;
    set `bank`/`voice` and the style in lines.json before the Forge records. (general) (spec: the spec named
    warm-teacher while noting Sulafat is a neighbor's voice)
17. **Teacher notes and the source list carry build-process text.** notes.md:53 ("the listening review described in
    the build report... The build is a draft and is not ready for a solo nonreader"), notes.md:57 ("spec.md and
    codex-report.md ... recomputed in Scratch"), tool.draft.json sources ("supplied catalog verified in Scratch").
    Fixed: name the real sources (CCSS RF.K.3 and L.K.1, Dolch pre-primer, Fry first 100, Moats Speech to Print,
    Reading Rockets, Zaner-Bloser and Learning Without Tears charts) and drop the build-state lines. (general) (build)
18. **Write it yourself has no way out before drawing.** Only Teacher shows; Next appears after a miss or pass, so a
    child who tapped it by accident must scribble a failure to leave. The spec says it never blocks. Seen: audit
    state-independent-writing-1366x768.png. Fixed: Next visible from the start of Write it yourself. (general) (build)

## Polish accepted
19. 760x900: size the solo and cart lanterns from the stage height and seat them on the cart, so the lantern is the
    biggest thing (audit state-say-760x900.png). (general)
20. Trace: show the whole letter very faint under the current stroke (current stroke as now, done strokes gold), and
    after a Write it yourself miss show the full letter model over the ink, not one stroke (audit
    state-trace-1366x768.png, play f4/x07-free-miss.png). (family:letter-pals)
21. Long/short boards: the vowel's awake lantern over the vowel of each word with the same small/tall flame shapes as
    the flames step, replacing the CSS blobs (play f2/f01-long.png, craft out/L-long-1366x768.png). (family:letter-pals)
22. End card: every lantern swings onto the string and the shops light down the street before Go to Village, instead
    of the three cart lanterns (play f2/g01-end.png). (general)
23. The new lantern flies to the slot it will hang in on the string, not the top-left corner (`@keyframes fly`; audit
    state-independent-writing-1366x768.png, state-first-shop-sign-680x425.png). (general)
24. Twins marker: replace the `outline:4px solid #7fe3ff` (the kit focus ring) with the spec's flicker plus an amber
    glow, distinct from focus (craft out/L-twins-1366x768.png). (general)
25. Twins at 680x425 and 800x500: move or drop the "Find what changed" label so the tile row does not sit on it or
    crowd the chip, as `.signing` does (craft out/L-twins-680x425.png). (general)
26. Say step shows a glow star before the lantern is lit (chip "0 lit"); show no star until lit (play
    f1/p05-say-tap.png). (family:letter-pals)
27. First screen: hide Hear it again until there is something to hear, instead of a half-opacity dead button
    (src.html:1631). (general)
28. `listenLantern`, `listenBanner`, `listenSign`, `listenWord` are never spoken (Read speaks `hintSpoken`): mark them
    hint-only in voice/lines.json so the Forge does not record them. (general)

## Settled calls
- Say order (all three lenses): Teaching called it polish, Play and Craft should fix. Settled as should fix
  (7): the spec orders intro then turn, and the model answering its own instruction defeats the step.
- Flames, long/short and twins giveaways (4, 5, 6): settled by "a check must reward the right practice" (BASELINE rule
  2), not sent to Cory. Keep the flame shapes and both anchor pictures; only which sound is asked and the sides change.
- Voice (16): settled by the curio-variety rule from voices/bank.json: playful-friend (Laomedeia). Not bright-teacher
  (bus-stop, a K sibling in this batch) and not gentle-storyteller (act-it-out, snowy-mail-route, K).
- Blocker 1 route: play the isolated `sound.<l>` clip inside sequences rather than spelling sounds in text, so each
  sound is recorded once, clean, and is the same everywhere. Do not rewrite displayed hints to phonetic spellings.
- Village below 800 px (14): a chip is fine at 680x425; the line must not name what is not shown.
- Done when 9 (clips) fails only because clips are not recorded yet; that is the Forge, not this round.
- Audit lead "#begin Wake the village: welcome not heard" is wrong (teaching out/31 and craft v1, v4, v8a logs: the
  welcome is spoken). Welcome cut by a first tap on Teacher, a cart lantern or a double tap is allowed (rule 16).
- Do not change: the trace check (backward, half, tap-only and scribble fail on every stroke of all 52 letters; three
  misses auto-finish), wrong-answer lines that name themselves, Read behavior, line order on taps, frame times.

## To the spec's open questions
- spec.md Art says "All local FLUX"; prompts.json says gpt-image. The art is fine; the integrator updates the spec
  line (and the Voice line to playful-friend). Codex does not touch spec.md.

## Not taken
- Craft nit 11 (Sound back on re-speaks the question): repeating the current question is helpful; leave it.
- Craft nit 13 (2.93 MB): 2 MB is a goal (rule 12); add the `Size:` line only if the bundle passes 6 MB with clips.
- Teaching nit 10 (umbrellabird anchor): the picture carries it and the art is made; not worth a redraw.
- Teaching nit 11 (short wobbly strokes fail sometimes): white-noise sim overstates real finger ink; the exit check
  does one real-touch try on m, k and i instead of a change now.

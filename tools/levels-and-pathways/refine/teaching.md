# Teaching lens: levels-and-pathways (round 1)

Cold read of spec.md, src.html, notes.md, tool.draft.json, art/prompts.json and voice/lines.json, then the bundled
draft (CURIO_DRAFT=1) driven in muted headless Chrome (port 9761/9762, own profile) with real held clicks, real drags
and keys. Frames and logs: `scratchpad/refine/levels-and-pathways/teaching/` (f/, poses/, poses-sheet.png).

Counts: blockers 0, should fix 1, polish 7, nit 3.

## Findings

### Should fix

1. **DA:Pr4.1.2a is cited for pathways only** (spec "Who and how"; notes.md line 49; src.html header comment).
   general. The repo holds codes only (`data/standards/ncas-performance-standards.txt`), so I checked against the NCAS
   text as I know it: the grade 2 expectation is clear directionality and intent in locomotor and nonlocomotor moves
   that change body shapes, facings and pathways, plus symmetrical and asymmetrical shapes and circling versus turning.
   The tool gives grade 2 the same straight, curved and zigzag pathways it gives grade 1 (DA:Pr4.1.1a); facings,
   symmetry and circling versus turning are not done by any student activity. Under rule 2 and the K-2 span call
   (gf-04), either move the code to a dance sibling that can teach it well (choreography-board is the likely home) or
   have the integrator confirm the official wording first and record why pathways alone carry it. Don't add a thin
   activity just to keep the code. How seen: read the code list against every mode played below.

### Polish

2. **"Middle level. Stay in the middle." gives no body cue** (src.html line 266, `atMiddle`; voice/lines.json).
   general. High says "Reach up to the sky!" and Low says "Get close to the floor.", but "the middle" of what? A
   kindergartner copying the dancer gets nothing to do. Better: "Middle level. Feet on the floor, between the sky and
   the ground." (a new clip; the spec voice table changes with it). How seen: line list and run logs.
3. **High reads only by the arms** (family:dance; poses-sheet.png, mid-after-high.png). Every High keyframe is
   "on tiptoes", but from the front the painted shoes look flat and the head rises only about 16 px on a 320 px figure
   (head y 194 at High against 210 at Middle, 1366x768). Twist, Bend and Shake High differ from Middle mostly by arms
   up, so the class can learn "high = arms up" rather than "the whole body rises". Better: a visible heel lift (a
   small rise of the whole figure, or a three-quarter turn of the feet), or a tiny hop in Shake High.
4. **Locomotor and nonlocomotor are never named to the class** (header subtitle; notes "Talk about it"). general.
   The topic line promises the distinction, and the modes split it cleanly (Levels stays in place, Pathways travels),
   but nothing spoken or shown says "these moves stay in your bubble space, these moves travel". Better: one how line
   in each welcome ("These moves stay in one place." / "Now we travel!") and a matching notes line.
5. **Support at home is thin and not about this tool** (notes.md lines 16 to 18). general. "Make a high shape and a low
   shape together using comfortable arm movements" is vague, and no idea uses pathways on the floor or a drawn map,
   the heart of Pathways and Draw a path. Better, all doable tonight: "Draw a pathway on paper (straight, then
   zigzag), then walk it across the room." / "Call sky, table or grass and freeze in a shape at that level." / "Walk a
   curved pathway around a chair, then a straight one back."
6. **Notes say low is on the floor; the traveling dancer crouches** (notes.md line 47). general. In Levels every Low
   keyframe sits, kneels or lies, but in Pathways and Mystery the Low walk, gallop and slide are a deep crouch
   (paths-trip4.png, mys4-travel, mys6-travel). A teacher reading the note then watching a crouched trip sees a
   mismatch. Better: "Low level is close to the floor: on the floor for moves in place, a deep crouch when traveling."
7. **Older ribbons lose their end badges** (family:dance; paths-trip3.png). All three pathways end at x 90, z 50, so
   the newest badge covers the older two: three ribbons on the floor, one badge. The pattern still carries the level,
   but the class can't read an older ribbon's icon pair when the teacher asks "which one was the zigzag?". Better:
   stagger older badges (or put each at its ribbon's start or middle).
8. **Round 7's circle is answered "Curved" with no word on why** (Mystery round 7; mys7 frames and the gallery).
   general. A full circle back to the star is a good stretch, but the answer button shows an arch and the class may
   hesitate. A one-time line after the right answer ("A circle is a curved pathway too!") turns it into a teaching
   moment.

### Nit

9. **"Which level was the dancer?"** (src.html line 280, `askLevel`). general. Reads oddly aloud; "Which level did the
   dancer dance at?" or "Was the dancer high, middle or low?" Needs a new clip.
10. **Small zigzags and clipped loops read wrong** (family:dance, `Dance.readPath`). A screen zigzag of 30 px corners
    (about a child's quick scribble at 1366x768) read as one curved part (draw-scr-small-zig.png); 40 px read zigzag.
    A loop drawn around the star runs off the left edge, is clamped to a straight edge and reads curved, straight,
    curved (draw-big-circle.png); the same loop drawn to the right of the star reads one curved part. A shallow
    diagonal zigzag (74 degree turns on the floor, flatter on screen) read as four straight parts (draw-diag-zig.png),
    which is defensible from how it looks. Edge cases only.
11. **The spec's open question is already settled** (spec.md "Open questions"). general. BASELINE "Specific calls"
    says levels-and-pathways must not share one dancer figure with PE (w1-21); the question asking whether to share it
    should be closed in the spec.

## Teaching checklist

**1. Standards taught by something the student does.**

| Code | Taught by | Verdict |
|---|---|---|
| DA:Cr1.1.Ka (respond in movement to a cue) | copying the narrator, the count-in and the music in every mode | taught |
| DA:Cr1.1.Kb (change one element) | Levels: same move at three levels; Pathways: path, way and level | taught |
| DA:Cr1.1.2b (combine, changing elements) | Draw a path: levels per part, Dance it (trace changed level at count 5) | taught |
| DA:Pr4.1.Ka (levels) | Levels, Up and down | taught |
| DA:Pr4.1.1a (straight, curved, zigzag pathways) | Pathways, Mystery, Draw a path | taught |
| DA:Pr4.1.2a | pathways only | finding 1 |
| DA:Re7.1.Kb (demonstrate or describe observed movement) | Mystery: draw it in the air, name it, then the level | taught |
| DA:Cr3.1.Kb and 2b (symbol or map for a pathway) | Draw a path: the class draws the map; ribbons and badges as symbols | taught |
| DA:Pr5.1.Kb (start and stop on cue, own space) | count-in, "And freeze!", bubble space line | taught |
| SHAPE.S2 (movement concepts) | levels and pathways throughout | taught |

**2. Done when.**

| # | Check | Result |
|---|---|---|
| 1 | 36 keyframes shot (6 moves, 3 levels, A and B; poses-sheet.png): every one its own shape, Low all on the floor; guide band = `shownLevel` = chosen level on every count; the call ("Stretch!", "Low level...") logs at 3.0 to 4.3 s and the pose tween waits for it | pass (finding 3 on how High reads) |
| 2 | High tapped at count 3 of Twist: trace middle, middle, middle, high x5; Up and down: 40 counts, 8 each High, Middle, Low, Middle, High, each level line on its count | pass |
| 3 | Four trips (zigzag skip high, curved gallop low, straight slide middle, zigzag walk low): ribbon shape per path, level color and pattern, icon at the end; after trip 4 the first ribbon is gone, two older at half | pass (finding 7) |
| 4 | All 8 rounds played: rounds match Content; answer buttons dimmed and disabled in every travel sample (572 samples); wrong path replays once without ribbon; right path paints in; wrong level replays; gallery after round 8 with the bow | pass |
| 5 | Real drags: straight line one straight; half-circle arc curved; three-corner zigzag zigzag; tiny line tooShort; S wave one curved; straight then zigzag two parts; off-star start gets a lead straight part. Keyboard only: focus Surprise path, Enter, then Dance it, Enter | pass (finding 10) |
| 6 | Twist tapped at count 3 of Stretch: old counts stop at 3, only the new run counts; mode switch mid-Bend: no new counts, no music, no lines in 6 s | pass |
| 7 | Three moves in a row: copyMe spoken 1, silent 2; wLevels spoken once; move, level and freeze lines spoken every time | pass |
| 8 | Not re-shot: the audit's size rows are clean at all eight sizes (60 px targets, fold, 375 host) | pass on the audit |
| 9 | Curved walk trip measured 12000 ms with Motion on, 11999 ms Motion off, 11999 ms Sound off (4 + 16 counts at 100 bpm = 12.0 s); localStorage holds only `curio-motion`, stated in notes | pass |

**3. Facts.** Recomputed: tempos (walk and slide 100, skip and gallop 120 swung, Levels 96) match the spec; a trip is
4 + 16 counts; Draw counts 16 per 100 units clamped 8 to 32; zigzag corners at x 30, 50, 70; round 7 circle center
(25, 35.5), radius 20.86, so z 14.6 to 56.4 on the floor, as the code comment says. Notes and tool.draft.json match
the spec's Sources and the tool's behavior, apart from finding 6.

**4. Giveaways.** None. In Mystery the level guide stays blank through every trip (`shownLevel` null in all 572
samples, the stage description names no level), the hidden ribbon is invisible until a right path answer, the painted
ribbon is plain (no level pattern) until the level is answered, every trip ends at the same spot (x 90) except the
circle, and the dancer ends in a plain stand. Level answers only show after the path is right.

**5. Language and notes.** Plain and short for K-2, every line voiced. Findings 2, 4, 5, 6, 9. No sensitive topics
in these standards; the notes' adaptation line for children who can't kneel or go on tiptoe is good.

**6. Guardrails.** Teacher led, no points or timers; Mystery's 8 dots and gallery are fine for this topic.

**7. Sensitivity.** Nothing cultural, Native or hard-history; rule 5 does not apply. The painted guides are people art
(rule 11), marked `people: true` with a recorded review; that is Craft's check.

## Audit pilot

Leads confirmed:
- Welcome not heard on a first tap of a level, a move, Up and down or Surprise: confirmed, but the premise comes back:
  wLevels is logged `silent, early` on load and then spoken right after the first move's freeze (19.6 s in the Low
  Stretch run). Not a teaching gap.
- Size and state rows clean: my own frames at 1366x768 in every mode agree; I cited the audit for Done when 8.

Leads that were wrong:
- "Stretch: event line lost (spoken 0 of 5, dropped 5: stale)". Five held taps 2 s apart: "Stretch!" spoken 5 of 5,
  each followed by "Middle level". The 5 dropped entries are the tool's empty-key barrier item (`key: ""`), not the
  Stretch line; the audit counted them as the event.

Not checked by me: the `#d-surprise` left disabled after a mid-action resize (Craft and Play's area).

What it missed (teaching, outside what it can see): the grade 2 code covered only by pathways (1), the middle-level
line with no body cue (2), High reading by arms only (3), locomotor and nonlocomotor never named (4), the home ideas
(5), the low-level note against the crouched trips (6), hidden older badges (7), and the drawn-path edge readings
(10).

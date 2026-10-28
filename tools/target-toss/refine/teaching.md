# target-toss: Teaching lens (round 1)

Cold read of spec.md, src.html, notes.md, art/prompts.json, voice/lines.json, handoff.md; STANDARDS, BASELINE (w1-49),
BUILD BR1 lessons. Bundle: `CURIO_DRAFT=1 python scripts/bundle_tool.py target-toss` (95 KB, clean). Frames and logs in
my scratch folder (lens-tt-teaching): r1/ (a full held-click Test it run), f/ (all ten Form poses, Left hand),
c/ (coach and Show me timing), audit/.

Counts: blockers 1 (general 0, family 1), should fix 5 (general 3, family 2), polish 6, nit 2.
(family = family:target-toss / throwing-lab format; the tool has no engine, so "family" here means "comes from this
tool's experiment format".)

## Blocker

1. **"Same line" is wrong for the Close or far? card.** src.html:313 `startB` ("Now Way B! Same throwers, same line.")
   is spoken and set as the hint at the start of every Way B, including `far`, where the one thing that changes IS the
   line (Way B = "Throw from the far line"). At the exact moment the tool teaches the fair test it tells the class the
   variable stayed the same. Seen in code (startRound, src.html:968-973; testHint B = L.startB) and the Way B hint frame
   (r1/t5_B3.png shows the line on screen). Fix: a per-question start line, e.g. far: "Now Way B! Same throwers. Now
   use the far line." (and say the kept-same parts per card: step/look/size "same throwers, same line"; far "same
   throwers, same target"). Tag: family (fair-test format). The spec's own Voice table carries the error.

## Should fix

2. **Way A is always the coached way, and it is labeled 👍; Way B is always 👎.** QS (src.html:344-349): Way A is
   step / eyes on target / close / big in all four cards, and the Guess buttons and cards mark A with a thumbs up and
   B with a thumbs down (src.html:202-203, 814; frame r1/t2_guess.png). By the second question the class learns
   "Way A wins", and a thumbs-down on a side reads as "the bad one" to a five-year-old. BR1 lesson "No giveaways:
   ... the position of the right option reveals nothing" (missed lesson, so at least should fix). Better: put the
   coached way on side B in some cards (or shuffle per question load), and use neutral vote signs (✋ one hand up for
   A, ✌ two fingers for B, or point left / point right). Tag: family.
3. **"Same throwers" is never set up, and the notes contradict it.** Nothing at Ask, Guess or Way A tells the teacher
   to pick the throwers who will throw both ways; the idea first appears at Way B (`startB`), after Way A is thrown.
   notes.md step 3 says "each child throws at the wall target", but a round is 5, 10 or 20 throws, so in a class of
   25 the Way B throwers will be different children and the test is not fair. Fix: Way A's line/hint (or the Guess
   step) says "Pick ten throwers. The same ten throw again in Way B." (number from T.n), and notes.md explains it
   (same children, same order). Tag: family.
4. **K-2 narrator rule: the key teaching words on screen are not voiced.** The foot tag "👣 Step: LEFT foot" /
   "RIGHT foot" (src.html:713) is the K outcome itself (S1.E13.K: underhand while stepping with the foot opposite the
   throwing arm), but the narrator only ever says "Step with the opposite foot." Non-readers never hear which foot.
   Also the coach card's fixed "Throw five balls. Then look here." (src.html:231, 1061) is not a line at all. Fix:
   cue 3 spoken as "Step with your left foot, the opposite foot." (right/left from Hand; two lines per throw type), and
   voice the coach placeholder once. Checked against voice/lines.json and the Show me log (c/: cue 3 spoken as
   "Step with the opposite foot." only). Tag: general.
5. **Module is "Throwing and Catching"; the tool teaches no catching (BASELINE rule 2).** data/modules.csv:
   health-pe-k-2-throwing-and-catching, "Manipulative skill basics", SHAPE.S1, and target-toss is the only tool on it
   (data/tools-concepts.csv). SHAPE.S1 is taught well for underhand and overhand throwing (all five critical elements,
   above the K and 1 minimums), but catching (S1.E16) has no activity here and none elsewhere for K-2. Not a thin add:
   either the module is renamed/re-described to throwing, or catching is queued for another K-2 PE tool (rule 10).
   This is a module-scope call for the integrator / spec open questions, not the builder. Tag: general.
6. **Setup card leaves out what the data and the safety depend on.** The setup card and notes (src.html:273-278,
   notes.md step 1) say only "Tape a paper target on the wall beside the screen." (a) The tap mapping, the coach's
   above / low / side rules and the "Small target: only the gold counts" card all assume the paper target has the
   screen's three rings (gold center, red, blue edge); nothing says to draw them or how big (a paper plate with no
   rings breaks Big or small? and the coach). (b) "Beside the screen" puts the screen in the path of every miss on
   that side; the safety tip says never throw at the screen. Say: three rings like the screen, about the size of a
   poster (a practical suggestion, labelled as such), and leave space between the target and the screen (e.g. hang it
   on the side away from the laptop, a couple of big steps away). Retrieving balls (only when the teacher says, after
   everyone has thrown) belongs in the safety note too (Appropriate Instructional Practice Guidelines are the cited
   source for spacing). Tag: general.

## Polish

7. **The tip can overrule the class's own result without saying so.** showAnswer (src.html:1015) always shows e.g.
   "Good throwers look at the target the whole time." even when Way B (eyes on feet) got more hits. Right after "That's
   why we test!" that teaches "the data don't matter". Better: when the result goes against the tip, lead with "Our
   test came out different. Try more throws, then test again." before the tip. Tag: family.
8. **Look ten-frames are in throw order, so the ten-frame does not do its job.** tenFrames (src.html:618-624) fills
   hits and misses interleaved (r1/t9_answer.png: A reads ★ ● ● ✕ ✕ / ★ ● ● ✕ ●). K-1 children read a ten-frame by
   its shape (7 = a full row and 2). In the Look picture graph, put hits first, then misses, so 7 and 4 can be seen at
   a glance; keep throw order in the round panel. Tag: family.
9. **Per-grade targets missing from teacher notes (K-2 span, BASELINE gf-04).** SHAPE outcomes step up by grade:
   S1.E13.K step with the opposite foot; S1.E13.1 two of five elements; S1.E13.2 a mature pattern (all five). A
   secondary source puts the first overhand outcome (S1.E14) at grade 2, two of five elements; confirm against the
   2014 table. notes.md "Good to know" should say what to look for at each grade (K: the step; grade 1: two cues;
   grade 2: all five, and start overhand). Tag: general.
10. **Overhand cue 2 drops "elbow up".** The SHAPE element is arm back and extended, elbow at shoulder height or above;
    Bo's pose shows it (f/f_over2.png) but the card and line say only "Bring your arm way back." Better: "Arm way
    back, elbow up." Tag: general.
11. **The guess intro is long and its how-to is lost at a teacher's pace.** After a question tap the narrator reads
    title, Way A, Way B and only then "Make a guess! Thumbs up...", about 10 s later (13 s with the first-tap safety
    line). In run r1 I pressed Way A 8 s after the card and "Make a guess!" was dropped (vlog: dropped at 12043 ms).
    Better: say the guess instruction first or shorten the read-out. Overlaps Play / Craft. Tag: general.
12. **Handoff deviation 6 is not built: no Stop test on the Guess step.** tg-guess has only 5/10/20, Way A, Way B,
    Skip (r1 JS "guessVisible"). A teacher who tapped the wrong card has no way back except the mode button. Add the
    Stop test (or a "Back to questions") on Guess as the handoff says. Tag: general.

## Nit

13. Switching Throw after a coach line rewrites the advice for the throws already made (underhand "Too high. Let go
    lower..." becomes the overhand line at once; c/ "highU_after_switch"). Fine as advice for the next throws; maybe
    keep the text until the next five. Tag: family.
14. Overhand cue 5 "Follow through across your body." drops "toward the target" from the SHAPE element. Tag: general.

## Standards (rule 2)

SHAPE.S1, underhand (S1.E13) and overhand (S1.E14): taught by Form (Bo's five poses, glow on the throwing arm and
stepping foot, Throw with Bo shadowing) and practised with real throws in Test it and Free throw, with outcome-based
coaching tied to the cues. All ten cues match the critical elements in the Sources (face, arm back, opposite-foot step,
release knee to waist, follow through to target; side to target, arm back, step, hip and shoulder rotation, follow
through across the body). Poses checked frame by frame (f/form sheet): underhand release at thigh height (computed: ball
at y 66 model units, hip 70, knee 36), overhand arm back with the elbow at shoulder height, the far (opposite) foot
steps and glows, Left hand mirrors and the tag reads "Step: RIGHT foot". Catching: finding 5.
The fair test (NGSS SEP 3, a source, not a module code) is really done by the class (guess, two rounds, compare), with
findings 1-3.

## Done when

1. Pass. Show me: cue highlight and spoken cue start in the same tick for all five (c/ log: 1341/1341, 3037/3037,
   4817/4817, 7037/7037, 9921/9921 ms), then the ball flies to the bullseye. Left hand: tag "Step: RIGHT foot".
2. Pass. Held-click run (size card, guess A, 10 + 10 real taps at computed ring radii, R 238 px at 1366x768): my
   recompute A 7 hits (gold 2, red 3, blue 2; misses 3), B 4 (gold only); the graph, numerals, bars, desc and spoken
   counts ("Seven hits", "Four hits") match. "Way A got more hits!" and "That matches our guess!" correct.
3. Pass. Way B small target: red and blue taps miss, gold taps hit (r1/t5_B3.png).
4. Pass. Four Undos after three Way B throws: B 0, A still 10 (7 hits), Undo disabled. Too short adds a miss.
5. Pass. Five misses above: underhand "Too high. Let go lower...", overhand "Too high. Follow through down...";
   3 hits in 5: "Great aiming!". Low, side and keep rules also checked in order.
6. Pass for what I saw: no throw tap spoke in a 20-throw run; doneA, Look counts, result and tip spoke. Five-in-a-row
   counts are the Craft lens's table.
7. Pass per audit (0 leads at every size including 375 host) and my 1366x768 frames.
8. Pass. Dashed blue, solid red, double-edged gold; all contrast values recomputed and hold (6.79, 7.38, 14.45, 6.43,
   4.85, 5.72; dark star on gold 8.14).
9. Pass per audit (Motion off: nothing runs forever) and code (poseTo jumps, beats unchanged).

## Giveaways

Nothing on the Look step crowns a side before Show the answer; tips appear only after it; the Guess cards have no
badge, order or length tell except finding 2 (position and thumbs). The counts on the graph are the class's own data,
which is the point.

## Builder's spec deviations

1. w1-49 setup card and wall-target safety lines: accept; the gaps are finding 6.
2. Cue and `ready` lines as event lines: accept (a silent second demo would teach nothing).
3. Added `tryBo`, `boDone`, `again`: accept; all name a live control and are in lines.json.
4. Coach 7 lines, not 9: accept; the spec's table has 7.
5. Safety after the first Show me run: accept; no ball is thrown in Show me, and it plays before Throw with Bo,
   Test it or Free throw.
6. Stop test on Guess: not built (finding 12). Way B to Look after 1.3 s: accept.

## Sensitivity

Nothing cultural, Native or hard-history. No sensitivity agent needed.

## Audit pilot

- Confirmed: 0 leads, and my frames at 1366x768 agree (no clipping, 60 px controls, first-tap safety line, cue lines
  per tap). Wrong leads: none.
- Missed (outside what it can see): the "same line" error (1), the position/thumbs giveaway (2), the fair-test setup
  (3), unvoiced foot tag (4), module scope (5), setup gaps (6), the guess how-line dropped at a teacher's pace after a
  long read-out (11), and the handoff's unbuilt Stop on Guess (12), which needs a screen past one click.
